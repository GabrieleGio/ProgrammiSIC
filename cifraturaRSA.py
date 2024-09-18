from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import base64

# Generating RSA Key Pair
# key_pair = RSA.generate(2048)
# print(key_pair.export_key())
# public_key = key_pair.publickey()
# print(public_key.export_key())
# exit(0)
# pubkeycollega=''
# keyDER = base64.b64decode(pubkeycollega)
# seq = base64.asn1.DerSequence()
# seq.decode(keyDER)
# keyPub = RSA.construct((seq[0], seq[1]))

# cifrato= "io sono batman"
spubliccollega='-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA0xF3p+YjlDhipXdSOESv\nkYr0LeL1Tanzp93UiNjVzWZY8HZLmdvqEcO9e7CAq4PiXiaBjaSYRTmams2Gnccd\ncLFvrKUPGQuWaUBwAfBN6D9uyXCm4V1V0HeQ7sO3hTrKQWWE8GkHFazf5aTGSqXK\nd2Sj0h1iHiSd5Xf3Ni/7jaDSZtwUpClODY/eCgo02zUbiVFvNZ0sQs/f4RLY2TPA\nLbOO4JLPPTfOtl8eGMNpBq8zTzdJiCBCmfLVgdFH23IuOWrP42f+qDM9ik1UwD+i\nNrmJ0ynerTHnQJNV/ZugSHshallKvvRXMNs2TWVr/B3HJx6+ZW6ZlZLI4OcjhGa6\nyQIDAQAB\n-----END PUBLIC KEY-----'
sPriv='-----BEGIN RSA PRIVATE KEY-----\nMIIEowIBAAKCAQEA6Cqr81Z6cnMGqTGScdt8MkQLj4myO/2g153m4s891i7n2jIq\nyS57nd/00BR9swVKeCzfPDFppeNn62N7wtAm5dk3gk1wcEm96fHzjmDxQhM+eDXF\nutdyEwLENQ3JfhrsSsXjiJsDotBCmRPo2V7EnflMib12E/bWf3oDAPxv10t9HHMu\nn9HL8q1f6YyfdWgFGGW1q1/ZFfEPFxtL5xXI+m5FoRihqfscjYndPwCbgS2xTKD6\nW8dt7rroYLGO+TbPi/JbdIMgPO08Ve6I+Qomz7a9UhBYlu5I2cSTvLslIUBw45l/\nyLguq4dyNPixzl47KSbMcgxzdw08phEwYZ6TxQIDAQABAoIBABYLjz5Q9NmPQI+q\nTFyRWc6wFWTwz0LRB4fRz42z3gxLceqPHu7xgf1wuZ9UgscP9o1IvX3Kt1xwJnr8\nfFD4UOk8Yf/2eHnBFs5zEgxv+hirGSBzAq6GLKfPeHANOhfGWK+U8NEU3xiDq/87\nG74gOI1Dkdf2bJLiumVqYYSjc78+lnkKizJe/g6/kCC84FHkOOy36wgbd9Fg11cQ\nTlj6smyI0lLy8cAjvtSbuKMWk0J6F7wdaOMRAqfNdstC8GqRTv3lXJQBoV/x9TI0\njX28aDkU9/9LJe88tAK/h0BYFpfGwIEN9J3kA1Esx30UJcJpM9lMvzzUyvgxkY6J\nZoeJynUCgYEA7zDCs/U5HWRIbT9YlDdJsBYB/EePdzi1SuDaULfEsSYNtZTpEFks\n0AxXnqjLDouGB6Xbnh7HlTEO+63xztkdUB/S4uVnL1jjzF2jZ2eEtj5Q5ztgI7um\n3SWhFUrATB1sp2mf9X85mYWjMkkcUPFn0xb43JmwHvvkjhn+SRGaKS8CgYEA+HuM\nGofzX3WFiLkNyJFmabQ7/tROGirf1dKiAhWQDu8wWug4bLMaxmwcbnAQ12qtX0QT\nW3psF2a+H8LtWCZIFXF0z+ueiZyGnRdc37x5JCe1BevGk3UbmU6MJfaYCZqqRHx3\nGyOpuj8a5PjAfmCFwsJOfvCB2xWRWLA8U5bs7UsCgYAgXZS7DR+hXoR+Y+f0hlau\nQQwbuwMqur2tWCeybGttHR0VyQSQdcCelkz05xoy6aZFOqgxCTEweubwH2Vs++v/\nf47lrOz9dyW77Z/Cyjsm/d+sqlgj/aximEjnvKmwovqk3KIMch61K2Qd1c7DFSdb\nZOxfzVwLlUIkCFhkQsF9eQKBgQCBbCBaRUtfAiBOSUzDlfAIyIajQUN437H8dhxK\nB58kGDNQdjnFbDha9z6LyzUKbpbk0tleQVKBkdMfSfFDg5TyDkkwbuIBfRSkR+Ho\n6wsR6Nihv9+LOGjqnf3jXCBuiC99QnLrINUrm+jPMD1a1b115qzp8y0/xmkRD6Is\nS6UWJwKBgE9cdQPKr58rWgvJ7E+o6qk7Rd3IVzFYjKVlQyn8AQHsHxUaAS0eMf1U\n1onRIA2/m4wH/o+1dbW5O04Nn80m8N6yqMACGy1xr/t8Pdj0zHtRDf9A7sAhXoTK\n05WJXtUZKVALf0Ds4Zl1ljR0anLjBSNWf6+DXWhu+MIdXTtAU7Mz\n-----END RSA PRIVATE KEY-----'
sPub='-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA6Cqr81Z6cnMGqTGScdt8\nMkQLj4myO/2g153m4s891i7n2jIqyS57nd/00BR9swVKeCzfPDFppeNn62N7wtAm\n5dk3gk1wcEm96fHzjmDxQhM+eDXFutdyEwLENQ3JfhrsSsXjiJsDotBCmRPo2V7E\nnflMib12E/bWf3oDAPxv10t9HHMun9HL8q1f6YyfdWgFGGW1q1/ZFfEPFxtL5xXI\n+m5FoRihqfscjYndPwCbgS2xTKD6W8dt7rroYLGO+TbPi/JbdIMgPO08Ve6I+Qom\nz7a9UhBYlu5I2cSTvLslIUBw45l/yLguq4dyNPixzl47KSbMcgxzdw08phEwYZ6T\nxQIDAQAB\n-----END PUBLIC KEY-----'
#ora ricreiamo le chiavi partendo da queste due stringe
publickkeycollega=RSA.import_key(spubliccollega)
key_pair=RSA.import_key(sPriv)
public_key= RSA.import_key(sPub)

# Function to encrypt message
def encrypt_message(message, pub_key):
    cipher = PKCS1_OAEP.new(pub_key)
    encrypted_message = cipher.encrypt(message.encode("utf-8"))
    return base64.b64encode(encrypted_message).decode("utf-8")


# Function to decrypt message
def decrypt_message(encrypted_message, priv_key):
    cipher = PKCS1_OAEP.new(priv_key)
    decrypted_message = cipher.decrypt(base64.b64decode(encrypted_message))
    return decrypted_message.decode("utf-8")


# Example usage
messaggio = "Urlo del Sium"
encrypted_message = encrypt_message(messaggio, public_key)
decrypted_message = decrypt_message(encrypted_message, key_pair)
#print(decrypt_message("WPUnl5KShy5DSDdUW+a5b/Uq5mEFZWGo2kk6ddiX24S56f3ZUe3S02Baf9meLFEs/D52fnpJilzAnjKt29QvfLbaqMhPOqRqnsf4FL29cM18tIYc4O7BkpMjvtmp8dgpctDXBfJI/fewBTZdZj4QTjNKhVq06Y973AyRvtXWvd3NVxWawjRejkV3sb5ftaEtkPimgUu1YLIdDhjDaj5NTpA9ce9tSsjkurvuGs/GUd9cNSBZwtVYSF26rzFSBV2gywTSoUeAI6K8H1w7TmR+kRgJWEW788V3DKa2NBVqzA6MtP/yr/3Rx/Pv5kVQBcj8pEGCCqBxMf3QIk3rEp4c4w==",key_pair))
print(encrypt_message(messaggio,publickkeycollega))
# print("Original Message:", messaggio)
# print("Encrypted Message:", encrypted_message)
# print("Decrypted Message:", decrypted_message)