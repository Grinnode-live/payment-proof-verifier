# payment-proof-verifier

Grin payment proof independent verifier

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

TODO

### GET /v1/settings/

TODO

### POST /v1/settings/

TODO

### GET /v1/balance/

TODO

### POST /v1/verify/

TODO
