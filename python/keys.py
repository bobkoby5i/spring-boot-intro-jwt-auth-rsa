#pip install pycryptodome==3.4.3
pip install pycryptodome
#pip install pycrypto
pip install rsa
pip install pyjwt
pip install cryptography --upgrade
#pip install Crypto 
pip install --upgrade pip


C:\Program Files (x86)\Microsoft Visual Studio 14.0\VC>vcvarsall.bat
set CL=-FI"C:\Program Files (x86)\Microsoft Visual Studio 14.0\VC\include\stdint.h"
C:\Program Files (x86)\Microsoft Visual Studio 14.0\VC>vcvarsall.bat
	

python -m pip install pyjwt
python -m pip install cryptography --upgrade
python -m pip install Crypto 
python -m pip install --upgrade pip

import jwt
import json
import base64


#from jwt.contrib.algorithms.pycrypto import RSAAlgorithm
#jwt.register_algorithm('RS256', RSAAlgorithm(RSAAlgorithm.SHA256))


private_key   = open('key.prv').read()
public_key    = open('key.pub').read()

java_b64_header      = open('java_b64_header.txt').read()
java_b64_payload     = open('java_b64_payload.txt').read()
java_b64_signature   = open('java_b64_signature.txt').read()

java_b64_header
java_b64_payload
java_b64_signature


payload_json     = {'user_id': 123}
with open('payload.txt') as json_file:
    payload_json = json.load(json_file)
\


header_json     = {'user_id': 123}
with open('header.txt') as json_file:
    header_json = json.load(json_file)
\

header_json
payload_json


token_1 = jwt.encode(payload, private_key, algorithm='RS256', headers={"alg": "RS256", "typ": "JWT"}).decode('utf-8')
token_1

token_2 = jwt.encode(payload, private_key, algorithm='RS256', headers={"typ": "JWT", "alg": "RS256"}).decode('utf-8')
token_2


header={'alg':'RS256','typ':'JWT'}
token = jwt.encode(payload, private_key, algorithm='RS256').decode('utf-8')
token = jwt.encode(header, private_key, algorithm='RS256').decode('utf-8')


token = jwt.encode(payload_json, private_key, algorithm='RS256', headers={'alg':'RS256','typ':'JWT'}).decode('utf-8')
token
jwt.decode(token,public_key,algorithm='RS256',options={'verify_exp': False})

tab=token.split('.')
jwt_header  = tab[0]
jwt_payload = tab[1]
jwt_sign    = tab[2]


java_b64_header
jwt_header

jwt_payload
java_b64_payload

jwt_sign
java_b64_signature


/**
s = base64.b64decode(jwt_payload)

base64.b64decode(jwt_header)
base64.b64decode('eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9')
base64.b64decode('eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9')


base64.b64encode(json.dumps({"typ": "JWT", "alg": "RS256"}).encode('utf-8'))
base64.b64encode(json.dumps({"alg": "RS256", "typ": "JWT"}).encode('utf-8'))


paylod_str = json.dumps(payload_json)  # Turns your json dict into a str
print(paylod_str)
base64.b64encode(paylod_str.encode('utf-8'))

encoded_payload = base64.b64encode(payload)
    
    
import base64
encoded = base64.b64encode('data to be encoded')
encoded
'ZGF0YSB0byBiZSBlbmNvZGVk'
data = base64.b64decode(encoded)
data
'data to be encoded'


header_json = {"alg": "RS256", "typ": "JWT"}
header64 = base64.b64encode(json.dumps(header_json).encode('utf-8'))
with open('payload.txt') as json_file:
    payload_json = json.load(json_file)
\

payload64 = base64.b64encode(json.dumps(payload_json).encode('utf-8'))

data = '{"hello": "world"}'
enc = payload.encode()  # utf-8 by default
base64.encodestring(enc)

header_json_str = '{"alg": "RS256", "typ": "JWT"}'
enc = header_json_str.encode()  # utf-8 by default
base64.encodestring(enc)


header_json     = {'user_id': 123}
with open('header.txt') as json_file:
    header_json = json.load(json_file)
\

    
*/    

data =  header_json
print(type(data))  #dict
datastr = json.dumps(data)
datastr=datastr.replace(" ", "") # need to cleanum because b64 does not match what java does. 
print(type(datastr)) #str
print(datastr)
encoded = base64.b64encode(datastr.encode('utf-8'))  #1 way
#print(base64.encodebytes(datastr.encode())) #2 method
print(encoded)
print(type(encoded)) #bin
s=encoded.decode("utf-8")
print(s)
s=s.rstrip("=")
print(type(s)) #str
print(s)
b64_header=s
b64_header

print('Our encoded header: ' + b64_header)
print('Java Spring header: ' + java_b64_header)
print('Python jwt  header: ' + jwt_header)


data = payload_json
print(type(data))  #dict
datastr = json.dumps(data)
datastr=datastr.replace(" ", "") # need to cleanum because b64 does not match what java does. 
print(type(datastr)) #str
print(datastr)
encoded = base64.b64encode(datastr.encode('utf-8'))  #1 way
#print(base64.encodebytes(datastr.encode())) #2 method
print(encoded)
print(type(encoded)) #bin
s=encoded.decode("utf-8")
print(s)
s=s.rstrip("=")
print(type(s)) #str
print(s)
b64_payload=s
b64_payload


print('Our encoded payload: ' + b64_payload)
print('Java Spring payload: ' + java_b64_payload)
print('Python jwt  payload: ' + jwt_payload)

import hashlib

print('Hashing..... sha256')
token_hp = b64_header + "." + b64_payload
token_hash=hashlib.sha256(token_hp.encode('utf-8')).hexdigest()
token_hash
'4aa1ca9a3a7d024c65da76b2f02ac5e57aaa1c5561930c6efc78cd63fba7047f - online generated for header.payload'






m = hashlib.sha256()
m.update(b)


my_header_payload = my_encoded_header_str + "." + my_encoded_payload_str
hashlib.sha256(jwt_payload.encode('utf-8')).hexdigest()
hashlib.sha256(my_header_payload.encode('utf-8')).hexdigest()



###############################################################################
ENCRYPRION PRIVATE KEY

#import crypto
#import sys
#sys.modules['Crypto'] = crypto

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import binascii

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA512, SHA384, SHA256, SHA, MD5
from Crypto import Random
from base64 import b64encode, b64decode
import rsa



random_generator = Random.new().read
keysize = 1024
key = RSA.generate(keysize, random_generator)
private, public = key, key.publickey()
public, private


keyPair = RSA.generate(1024)

pubKey = keyPair.publickey()
print(f"Public key:  (n={hex(pubKey.n)}, e={hex(pubKey.e)})")
pubKeyPEM = pubKey.exportKey()
print(pubKeyPEM.decode('ascii'))

print(f"Private key: (n={hex(pubKey.n)}, d={hex(keyPair.d)})")
privKeyPEM = keyPair.exportKey()
print(privKeyPEM.decode('ascii'))

msg = b'A message for encryption'
encryptor = PKCS1_OAEP.new(pubKey)
encrypted = encryptor.encrypt(msg)
print("Encrypted:", binascii.hexlify(encrypted))

decryptor = PKCS1_OAEP.new(keyPair)
decrypted = decryptor.decrypt(encrypted)
print('Decrypted:', decrypted)



from Crypto.PublicKey import RSA

keyPair = RSA.generate(bits=1024)
print(f"Public key:  (n={hex(keyPair.n)}, e={hex(keyPair.e)})")
print(f"Private key: (n={hex(keyPair.n)}, d={hex(keyPair.d)})")

# RSA sign the message
msg = b'A message for signing'
from hashlib import sha256
hash = int.from_bytes(sha256(msg).digest(), byteorder='big')
signature = pow(hash, keyPair.d, keyPair.n)
print("Signature:", hex(signature))


# RSA verify signature
msg = b'A message for signing'
hash = int.from_bytes(sha256(msg).digest(), byteorder='big')
hashFromSignature = pow(signature, keyPair.e, keyPair.n)
print("Signature valid:", hash == hashFromSignature)


######################################
Using GEY

keyPair = RSA.generate(2048)

private_key = keyPair.export_key()
file_out = open("private.pem", "wb")
file_out.write(private_key)
file_out.close()

public_key = keyPair.publickey().export_key()
file_out = open("public.pem", "wb")
file_out.write(public_key)
file_out.close()

# Read keys from file
public_key  = RSA.import_key(open("public.pem").read())
private_key = RSA.import_key(open("private.pem").read())

private_key  = RSA.import_key(open("key.prv").read())
public_key   = RSA.import_key(open("key.pub").read())
public_key
private_key

#
# Method 1
#

#msg1 = b"Hello bob, I am tom!"
msg1 = "Hello bob, I am tom!"
msg1 = token_hash                 #string
data = token_hash.encode('utf-8') #bin
#Encrypt
cipher_rsa = PKCS1_OAEP.new(public_key)
encrypted = cipher_rsa.encrypt(data)
encrypted = b64encode(encrypted)
encrypted


keysize = 2048
(public, private) = rsa.newkeys(keysize)
token_hp = b64_header + "." + b64_payload
data = token_hp.encode('utf-8')
b64_signature = b64encode(rsa.sign(data, private, "SHA-256"))
b64_signature = b64_signature.decode("utf-8")
b64_signature
MY_TOKEN  = b64_header + "." + b64_payload + "." + b64_signature
MY_TOKEN
verify = rsa.verify(data, b64decode(signature), public)
verify


#Decrypt
cipher_rsa = PKCS1_OAEP.new(private_key)
encrypted = b64decode(encrypted)
decrypted = cipher_rsa.decrypt(encrypted)
decrypted

#
# Method 2
#


encrypted = b64encode(rsa.encrypt(msg1,  public_key))
decrypted = rsa.decrypt(b64decode(encrypted), private_key)
print(decrypted)












#####################

b64_string = java_b64_signature
b64_bin    = b64_string.encode('utf-8') # str converted to bin
signature = b64decode(b64_string)
private_key = RSA.import_key(open("key.prv").read())
# RSA verify signature
hashFromSignature = pow(data, private_key.e, private_key.n)
print("Signature valid:", hash == hashFromSignature)





#msg1 = b"Hello bob, I am tom!"
msg1 = "Hello bob, I am tom!"
msg1 = token_hash                 #string
data = token_hash.encode('utf-8') #bin
#Encrypt
cipher_rsa = PKCS1_OAEP.new(public_key)
encrypted = cipher_rsa.encrypt(data)
encrypted = b64encode(encrypted)
encrypted




print('Hashing..... sha256')
data = b64_header + "." + b64_payload
data
data_hash=hashlib.sha256(data.encode('utf-8')).hexdigest()
data_hash
'4aa1ca9a3a7d024c65da76b2f02ac5e57aaa1c5561930c6efc78cd63fba7047f - online generated for header.payload'

private_key  = RSA.import_key(open("key.prv").read())
public_key   = RSA.import_key(open("key.pub").read())
private_key
public_key



m = hashlib.sha256()
m.update(b)


my_header_payload = my_encoded_header_str + "." + my_encoded_payload_str
hashlib.sha256(jwt_payload.encode('utf-8')).hexdigest()
hashlib.sha256(my_header_payload.encode('utf-8')).hexdigest()

