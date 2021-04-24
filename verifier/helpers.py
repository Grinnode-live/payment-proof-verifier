import datetime

import nacl.bindings
import nacl.signing

from datetime import timezone
from hashlib import sha256


def generateUTCTimestamp():
    dt = datetime.datetime.now(timezone.utc)
    utc_time = dt.replace(tzinfo=timezone.utc)
    utc_timestamp = utc_time.timestamp()
    return utc_timestamp


def ed25519Sign(signing_key_nacl, message_bytes):
    signed = signing_key_nacl.sign(message_bytes)
    return signed


def ed25519Verify(verifying_key_nacl, signed):
    return verifying_key_nacl.verify(signed)


def ed25519RawSign(signing_key_bytes, message_bytes):
    signing_key_nacl = nacl.signing.SigningKey(signing_key_bytes)
    signed = ed25519Sign(signing_key_nacl, message_bytes)
    return signed[0:-len(message_bytes)]


def ed25519RawVerify(
        verifying_key_bytes, message_bytes, signature_bytes):
    verifying_key_nacl = nacl.signing.VerifyKey(verifying_key_bytes)
    signed_message_bytes = signature_bytes + message_bytes
    return ed25519Verify(verifying_key_nacl, signed_message_bytes)


def signString(signing_key_bytes, payload_string):
    raw_bytes = str.encode(payload_string)
    digested_bytes = sha256(raw_bytes).digest()
    signature_bytes = ed25519RawSign(signing_key_bytes, digested_bytes)
    return signature_bytes, digested_bytes


def verifyString(verifying_key_bytes, payload_string, signature_bytes):
    raw_bytes = str.encode(payload_string)
    message_bytes = sha256(raw_bytes).digest()
    return ed25519RawVerify(
        verifying_key_bytes, message_bytes, signature_bytes)
