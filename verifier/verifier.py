import json
import requests

from furl import furl
from nacl.exceptions import BadSignatureError
from bip_utils import AtomBech32Decoder

from verifier.helpers import verifyString, signString, generateUTCTimestamp

class InvalidResponseSignatureError(Exception):
    def __str__(self):
        return 'Signature provided with the response does not match the grinnode.live public key.'

class Verifier:
    def __init__(
            self,
            grin_address=None,
            signing_key=None,
            api_address='',
            api_grin_address=None):
        self.grin_address = grin_address
        self.grin_address_bytes = AtomBech32Decoder.Decode('grin', grin_address)
        self.signing_key = bytes.fromhex(signing_key)
        self.api_address = api_address
        self.api_grin_address = api_grin_address
        self.api_grin_address_bytes = AtomBech32Decoder.Decode('grin', api_grin_address)

    def isSignatureValid(self, response, signature):
        signature_bytes = bytes.fromhex(signature.strip())
        try:
            verifyString(self.api_grin_address_bytes, response, signature_bytes)
        except BadSignatureError:
            raise InvalidResponseSignatureError

    def requestGET(self, url, authorize=False, sign=False):
        headers = {}
        if authorize:
            headers['authorization'] = self.grin_address
        if sign:
            f = furl(url)
            timestamp = generateUTCTimestamp()
            f.set({'ts': timestamp})
            url = f.url
            message = str(f.path) + '?' + str(f.query)
            signature, _ = signString(self.signing_key, message)
            headers['signature'] = signature.hex()
        response = requests.get(url, headers=headers)
        signature = response.headers.get('signature', None)
        if signature is not None:
            self.isSignatureValid(response.text, signature)
        return response.text, signature

    def requestPOST(self, url, payload, authorize=False, sign=False):
        headers = {}
        timestamp = generateUTCTimestamp()
        payload['timestamp'] = timestamp
        payload_string = json.dumps(payload)
        if authorize:
            headers['authorization'] = self.grin_address
        if sign:
            signature, _ = signString(self.signing_key, payload_string)
            headers['signature'] = signature.hex()
        response = requests.post(url, data=payload_string, headers=headers)
        signature = response.headers.get('signature', None)
        if signature is not None:
            self.isSignatureValid(response.text, signature)
        return response.text, signature

    def address(self):
        url = self.api_address + '/v1/address/'
        return self.requestGET(url, authorize=False, sign=False)

    def charge(self, payment_proof, sign=False):
        url = self.api_address + '/v1/charge/'
        payload = {
            'request': payment_proof
        }
        return self.requestPOST(url, payload, authorize=True, sign=sign)

    def settings(self, sign=False):
        url = self.api_address + '/v1/settings/'
        return self.requestGET(url, authorize=True, sign=sign)

    def updateSettings(self, settings):
        url = self.api_address + '/v1/settings/'
        payload = {
            'settings': settings
        }
        return self.requestPOST(url, payload, authorize=True, sign=True)

    def balance(self, sign=False):
        url = self.api_address + '/v1/balance/'
        return self.requestGET(url, authorize=True, sign=sign)

    def verify(self, payment_proof, authorize=True, sign=False):
        url = self.api_address + '/v1/verify/'
        payload = {
            'request': payment_proof
        }
        return self.requestPOST(url, payload, authorize=authorize, sign=sign)
