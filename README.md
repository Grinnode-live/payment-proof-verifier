# Grinnode.live's payment proof verification API

[Grin](https://grin.mw/) is a privacy-preserving digital currency built openly by developers distributed all over the world. It is based on the innovative protocol called [mimblewimble](https://docs.grin.mw/wiki/introduction/mimblewimble/ecc/). [Grinnode.live](https://grinnode.live/) provides a network of sync-nodes helping the new community members sync their wallets. Once in a while [challenges](https://grinnode.live/challenge/) are also organized. Now we are proud to introduce a payment proof verification API that allows everyone to check if grin payment is valid or not.

## Examples

### Create the instance of the API wrapper

A disclaimer, the below grin wallet addresses are not valid, they are created from random 32 bit strings and the signing key does not match any of those wallets.

```python
from verifier.verifier import Verifier

my_grin_wallet = 'grin1y3fxgseja6a4agchfl93wf9jhzpx5cqdg32mvh36jdsf6k9wsrrq96grxx'
my_signing_key = '90f7c3309c8ecf093a36b98271812f024aed1845c500c5d454b3af8a1ff55fad'
api_grin_wallet = 'grin1nhzvk7fe5fkmzvqlrlryfqngzv7fl5fztp3ckjgd0y483ye5gvgs7vj6q9'
api_address = 'https://verifier.grinnode.live'

verifier = Verifier(
    grin_address=my_grin_wallet,
    signing_key=my_signing_key,
    api_address=api_address,
    api_grin_address=api_grin_wallet)
```

### GET /v1/address/

Checking the current amount of free API calls and the grinnode.live wallet address.

```python
response, signature = verifier.address()
print('Response')
print(response)
print('Signature')
print(signature)
```

responds with

```
Response
{"error":"","request":{},"request_valid":true,"response":{"free_calls":8,"pem":"grin1gy3qxc4rvvqzc5slzh6nvdae6ns2qldws3z7vwhesyfp9vnkv3hsc53yhy"},"route":"/v1/address/","time":"2021-04-24T09:20:06.475399"}

Signature
a27fe4f27fb9a2a729a7e61dda35b243e110b802ad3a4ddacd3545bf76ca8a3ff2048e49de64ff3d0a9d36b6692dad5e25035ebc9a471a6c643f093cb627480d
```

### POST /v1/charge/

```python
payment_proof = {
    'amount': '100000000',
    'excess': '08325ba59b0580abdfc66e18cc948240e7da7ced77799110887d3335626b84bc15',
    'recipient_address': 'grin1gy3qxc4rvvqzc5slzh6nvdae6ns2qldws3z7vwhesyfp9vnkv3hsc53yhy',
    'recipient_sig': '742a5aa51ef6b26ec75e0cc3b68fe3daa5f78d74f773d06b3e89b64e459d5375c29442c53f228dcba72b158ad6bba80102d5d3f87efba42cbbb17049aee96f0a',
    'sender_address': 'grin1y3fxgseja6a4agchfl93wf9jhzpx5cqdg32mvh36jdsf6k9wsrrq96grxx',
    'sender_sig': 'a6b5d8c156bbf43cdb78494efb92c2af431ab1822692e504296b8758c663d5f9b03a62f63c7b1af824ada1e3ef017ba6f100b7b7b1d1665f6a05aa35ab89e007'
}

response, signature = verifier.charge(payment_proof)
print('Response')
print(response)
print('Signature')
print(signature)
```

responds with

```
Response
{"error":"PaymentProof: Invalid recipient signature","request":{"amount":"100000000","excess":"08325ba59b0580abdfc66e18cc948240e7da7ced77799110887d3335626b84bc15","recipient_address":"grin1gy3qxc4rvvqzc5slzh6nvdae6ns2qldws3z7vwhesyfp9vnkv3hsc53yhy","recipient_sig":"742a5aa51ef6b26ec75e0cc3b68fe3daa5f78d74f773d06b3e89b64e459d5375c29442c53f228dcba72b158ad6bba80102d5d3f87efba42cbbb17049aee96f0a","sender_address":"grin1y3fxgseja6a4agchfl93wf9jhzpx5cqdg32mvh36jdsf6k9wsrrq96grxx","sender_sig":"a6b5d8c156bbf43cdb78494efb92c2af431ab1822692e504296b8758c663d5f9b03a62f63c7b1af824ada1e3ef017ba6f100b7b7b1d1665f6a05aa35ab89e007"},"request_valid":true,"response":{"balance":0,"reason":"","verified":false},"route":"/v1/charge/","time":"2021-04-24T10:48:39.766759"}

Signature
c9a4bd04a227978c709845e7d93860ec913ca4642e7ae360e78faff05830c08e8c7fe42a8e86a89080fe31c6a0dd753d9940bb8696bc85896e2b0f7a80d3e508
```

### GET /v1/settings/

```python
response, signature = verifier.settings()
print('Response')
print(response)
print('Signature')
print(signature)
```

responds with

```
Response
{"error":"","request":{},"request_valid":true,"response":{"signature_required":true},"route":"/v1/settings/","time":"2021-04-24T10:56:41.168636"}

Signature
f8c7bbf5739dbca9eb04ab5c29213fb706af307c53066792a00e5ed638a05f5e5fe420418904a3858495f7d9980b3254bbecf03af3322db3b9fbcb69348c7506
```

### POST /v1/settings/

```python
settings = {
    'signature_required': False
}

response, signature = verifier.updateSettings(settings)
print('Response')
print(response)
print('Signature')
print(signature)
```

responds with

```
Response
{"error":"","request":{},"request_valid":true,"response":{"signature_required":false},"route":"/v1/settings/","time":"2021-04-24T11:02:04.432673"}

Signature
54a0dc6064bf90137d5d9d2a97cdd9b09d07443dd92d5459699a3ae565855a40b9ef45121292a06973396257acaa0d44070f1ef7a4c153983417711ce313930e
```

### GET /v1/balance/

```python
response, signature = verifier.balance()
print('Response')
print(response)
print('Signature')
print(signature)
```

responds with

```
Response
{"error":"","request":{},"request_valid":true,"response":{"balance":80000000},"route":"/v1/balance/","time":"2021-04-24T11:03:03.248396"}

Signature
9fb046bd64d4294372453fa6cbfa2f5dcc18d2735ca10a481cfb4839b557b767882735bdaf2fd910b817cd3baa7fae859c5223f68a9787fa19e7dce2590af903
```

### POST /v1/verify/

For the free request (limited daily number) set `authorize=False` explicitly. For paid request leave the default option.

```python
payment_proof = {
    'amount': '100000000',
    'excess': '08325ba59b0580abdfc66e18cc948240e7da7ced77799110887d3335626b84bc15',
    'recipient_address': 'grin1gy3qxc4rvvqzc5slzh6nvdae6ns2qldws3z7vwhesyfp9vnkv3hsc53yhy',
    'recipient_sig': '742a5aa51ef6b26ec75e0cc3b68fe3daa5f78d74f773d06b3e89b64e459d5375c29442c53f228dcba72b158ad6bba80102d5d3f87efba42cbbb17049aee96f0a',
    'sender_address': 'grin1y3fxgseja6a4agchfl93wf9jhzpx5cqdg32mvh36jdsf6k9wsrrq96grxx',
    'sender_sig': 'a6b5d8c156bbf43cdb78494efb92c2af431ab1822692e504296b8758c663d5f9b03a62f63c7b1af824ada1e3ef017ba6f100b7b7b1d1665f6a05aa35ab89e007'
}

response, signature = verifier.verify(payment_proof, authorize=False)
print('Response')
print(response)
print('Signature')
print(signature)
```

responds with

```
Response
{"error":"PaymentProof: Invalid recipient signature","request":{"amount":"100000000","excess":"08325ba59b0580abdfc66e18cc948240e7da7ced77799110887d3335626b84bc15","recipient_address":"grin1gy3qxc4rvvqzc5slzh6nvdae6ns2qldws3z7vwhesyfp9vnkv3hsc53yhy","recipient_sig":"742a5aa51ef6b26ec75e0cc3b68fe3daa5f78d74f773d06b3e89b64e459d5375c29442c53f228dcba72b158ad6bba80102d5d3f87efba42cbbb17049aee96f0a","sender_address":"grin1y3fxgseja6a4agchfl93wf9jhzpx5cqdg32mvh36jdsf6k9wsrrq96grxx","sender_sig":"a6b5d8c156bbf43cdb78494efb92c2af431ab1822692e504296b8758c663d5f9b03a62f63c7b1af824ada1e3ef017ba6f100b7b7b1d1665f6a05aa35ab89e007"},"request_valid":true,"response":{"reason":"","verified":false},"route":"/v1/verify/","time":"2021-04-24T10:51:57.038760"}

Signature
29f82bbf7ac878b6ebd1fdd586fb82abf6c357eafd594950a41b60fc0373288d816d918e6f0236c3d903b2868a689dbfe4b83a59110fe4e23f1431a080b96808
```

## FAQ

1. How do I generate the payment proof to provide for the recipient?

Using the CLI wallet, you can generate (and verify) the payment proof using [proof command options](https://docs.grin.mw/getting-started/wallet-handbook/#proof).

2. If wallet can both generate and verify the payment proof, what is the point of your service?

That is a good question to ask. For a person having access to a wallet and a node and knowing how to use them verification of payment proof causes no difficulty. However, there exist scenarios in which the payment proof needs to be verified by a third party, for example in case of arbitration during a decentralized exchange such as [bisq](https://bisq.network/).

3. Do I need to sign my requests?

Request signature is an extra measure of security and totally optional. For user's convenience every account is it switched off by default. This makes it possible to verify payment proofs using simple API calls executed using cURL or Postman.

4. Why is signature mandatory for `POST /v1/settings/` endpoint?

We want to make sure someone who is not capable of producing signed request does not accidentally enables request verification. That would immediately drop user's access to the service. You can only enable signed requests if you prove you are able to produce one.

5. Why do you sign your responses?

Every response from our API is accompagned with `signature` header which makes our responses transferable. You are welcome to generate payment proof, verify it using `POST /v1/verify/` endpoint and send our response and signature to your peers. If they trust [grinnode.live](https://grinnode.live/) and they know our grin wallet address they can verify if signature matches and believe your payment proof is valid even if they are unable to verify it by themselves.

6. How do the signatures work?

Every grin wallet address is a `bech32` encoded `ed25519` public key and wallet seed holds the corresponding signing key. The wallet seed can be used to sign data and wallet address can be used to verify the signature. The api wrapper in this repository can perform it automatically, if you perform manual requests it is more tedious as you will need to sign the UTC timestamped request fast enough before our API takes it for an attempt of a repetition attack.

7. How to I extract the signing key from my wallet?

The grin wallet can be started in [two API listener modes](https://docs.grin.mw/wiki/api/wallet-api/) which and Owner API provides [get_slatepack_secret_key](https://docs.rs/grin_wallet_api/4.0.0/grin_wallet_api/struct.Owner.html#method.get_slatepack_secret_key) method which will give you an hex-encoded secret key in plaintext. We strongly suggest to have a separate wallet for communication with our API as storing the plaintext slatepack secret key is *NOT* safe and *NOT* recommended.

## Raw API access

### GET /v1/address/

Endpoint: `https://verifier.grinnode.live/v1/address/`
Method: `GET`
Rate limit: `1 per 15 second`
Headers:
```
N/A
```
Payload:
```
N/A
```

### POST /v1/charge/

Endpoint: `https://verifier.grinnode.live/v1/charge/`
Method: `POST`
Rate limit: `1 per 30 second`
Headers:
```
authorization: grin1l8elz69qrlpm9un53s5l365unt95sh5wmzz5kd57lzarh4aqvczsj3rham
```
Payload:
```json
{
  "request": {
    "amount": "100000000",
    "excess": "08325ba59b0580abdfc66e18cc948240e7da7ced77799110887d3335626b84bc15",
    "recipient_address": "grin1gy3qxc4rvvqzc5slzh6nvdae6ns2qldws3z7vwhesyfp9vnkv3hsc53yhy",
    "recipient_sig": "742a5aa51ef6b26ec75e0cc3b68fe3daa5f78d74f773d06b3e89b64e459d5375c29442c53f228dcba72b158ad6bba80102d5d3f87efba42cbbb17049aee96f0a",
    "sender_address": "grin1l8elz69qrlpm9un53s5l365unt95sh5wmzz5kd57lzarh4aqvczsj3rham",
    "sender_sig": "a6b5d8c156bbf43cdb78494efb92c2af431ab1822692e504296b8758c663d5f9b03a62f63c7b1af824ada1e3ef017ba6f100b7b7b1d1665f6a05aa35ab89e007"
  }
}
```

### GET /v1/settings/

Endpoint: `https://verifier.grinnode.live/v1/settings/`
Method: `GET`
Rate limit: `1 per 30 second`
Headers:
```
authorization: grin1l8elz69qrlpm9un53s5l365unt95sh5wmzz5kd57lzarh4aqvczsj3rham
```
Payload:
```
N/A
```
Remarks:
1. If your account settings indicate `signature_required` is `true` and you provide `authorization` header, then `signature` header signing the payload string will also be required.

### POST /v1/settings/

Endpoint: `https://verifier.grinnode.live/v1/settings/`
Method: `POST`
Rate limit: `1 per 30 second`
Headers:
```
authorization: grin1l8elz69qrlpm9un53s5l365unt95sh5wmzz5kd57lzarh4aqvczsj3rham
signature: a6b5d8c156bbf43cdb78494efb92c2af431ab1822692e504296b8758c663d5f9b03a62f63c7b1af824ada1e3ef017ba6f100b7b7b1d1665f6a05aa35ab89e007
```
Payload:
```json
{
  "settings": {
    "signature_required": true
  }
}
```

### GET /v1/balance/

Endpoint: `https://verifier.grinnode.live/v1/balance/`
Method: `GET`
Rate limit: `1 per 30 second`
Headers:
```
authorization: grin1l8elz69qrlpm9un53s5l365unt95sh5wmzz5kd57lzarh4aqvczsj3rham
```
Payload:
```
N/A
```
Remarks:
1. If your account settings indicate `signature_required` is `true` and you provide `authorization` header, then `signature` header signing the payload string will also be required.

### POST /v1/verify/

Endpoint: `https://verifier.grinnode.live/v1/charge/`
Method: `POST`
Rate limit: `1 per 5 second`
Headers:
```
authorization: grin1l8elz69qrlpm9un53s5l365unt95sh5wmzz5kd57lzarh4aqvczsj3rham
```
Payload:
```json
{
  "request": {
    "amount": "100000000",
    "excess": "08325ba59b0580abdfc66e18cc948240e7da7ced77799110887d3335626b84bc15",
    "recipient_address": "grin1gy3qxc4rvvqzc5slzh6nvdae6ns2qldws3z7vwhesyfp9vnkv3hsc53yhy",
    "recipient_sig": "742a5aa51ef6b26ec75e0cc3b68fe3daa5f78d74f773d06b3e89b64e459d5375c29442c53f228dcba72b158ad6bba80102d5d3f87efba42cbbb17049aee96f0a",
    "sender_address": "grin1l8elz69qrlpm9un53s5l365unt95sh5wmzz5kd57lzarh4aqvczsj3rham",
    "sender_sig": "a6b5d8c156bbf43cdb78494efb92c2af431ab1822692e504296b8758c663d5f9b03a62f63c7b1af824ada1e3ef017ba6f100b7b7b1d1665f6a05aa35ab89e007"
  }
}
```
Remarks:
1. If your account settings indicate `signature_required` is `true` and you provide `authorization` header, then `signature` header signing the payload string will also be required.
2. If you skip the `authorization` header your request will be treated as a free request for which there is certain global daily limit provided by grinnode.live
