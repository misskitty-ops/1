from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
import os
import base64

# Input data to encrypt
data = """
MADE BY RAJCRACKS

BYPASS ADDED :-
{{{{
01XE 785NO
07H9 898JJ
64BO 8YHI8
VH69 7HJ9P
Y9GB 6HVOP
GI9N UGCI4

01XE 785NO
07H9 898JJ
64BO 8YHI8
VH69 7HJ9P
Y9GB 6HVOP
GI9N UGCI4

01XE 785NO
07H9 898JJ
64BO 8YHI8
VH69 7HJ9P
Y9GB 6HVOP
GI9N UGCI4

01XE 785NO
07H9 898JJ
64BO 8YHI8
VH69 7HJ9P
Y9GB 6HVOP
GI9N UGCI4

01XE 785NO
07H9 898JJ
64BO 8YHI8
VH69 7HJ9P
Y9GB 6HVOP
GI9N UGCI4

01XE 785NO
07H9 898JJ
64BO 8YHI8
VH69 7HJ9P
Y9GB 6HVOP
GI9N UGCI4

01XE 785NO
07H9 898JJ
64BO 8YHI8
VH69 7HJ9P
Y9GB 6HVOP
GI9N UGCI4
}}}
{{
BYPASS RECALL
BYPASS RECALL
BYPASS RECALL
BYPASS RECALL*10000
}}
ENDED BY RAJ CRACKS


STOP GAME

IN OFFLINE BYPASS:-
{{{
T85H 8YH9
8HG0 9VO9
G8GB O8VO
G9BO OHV9
U9HV 9HB0
J9HH ONB9
U8JB 9HV9
BI0B  9JO9
H9JI OBKP

T85H 8YH9
8HG0 9VO9
G8GB O8VO
G9BO OHV9
U9HV 9HB0
J9HH ONB9
U8JB 9HV9
BI0B  9JO9
H9JI OBKP

T85H 8YH9
8HG0 9VO9
G8GB O8VO
G9BO OHV9
U9HV 9HB0
J9HH ONB9
U8JB 9HV9
BI0B  9JO9
H9JI OBKP

T85H 8YH9
8HG0 9VO9
G8GB O8VO
G9BO OHV9
U9HV 9HB0
J9HH ONB9
U8JB 9HV9
BI0B  9JO9
H9JI OBKP

T85H 8YH9
8HG0 9VO9
G8GB O8VO
G9BO OHV9
U9HV 9HB0
J9HH ONB9
U8JB 9HV9
BI0B  9JO9
H9JI OBKP

T85H 8YH9
8HG0 9VO9
G8GB O8VO
G9BO OHV9
U9HV 9HB0
J9HH ONB9
U8JB 9HV9
BI0B  9JO9
H9JI OBKP

T85H 8YH9
8HG0 9VO9
G8GB O8VO
G9BO OHV9
U9HV 9HB0
J9HH ONB9
U8JB 9HV9
BI0B  9JO9
H9JI OBKP

T85H 8YH9
8HG0 9VO9
G8GB O8VO
G9BO OHV9
U9HV 9HB0
J9HH ONB9
U8JB 9HV9
BI0B  9JO9
H9JI OBKP

T85H 8YH9
8HG0 9VO9
G8GB O8VO
G9BO OHV9
U9HV 9HB0
J9HH ONB9
U8JB 9HV9
BI0B  9JO9
H9JI OBKP

T85H 8YH9
8HG0 9VO9
G8GB O8VO
G9BO OHV9
U9HV 9HB0
J9HH ONB9
U8JB 9HV9
BI0B  9JO9
H9JI OBKP

T85H 8YH9
8HG0 9VO9
G8GB O8VO
G9BO OHV9
U9HV 9HB0
J9HH ONB9
U8JB 9HV9
BI0B  9JO9
H9JI OBKP
}}
RED ALERT
GREEN ALERT
YELLOW ALERT

STOP BYPASS IF UNINSTALLED

[[[
DM TO BUY @RAJ_MAGIC
DM TO BUY @RAJ_MAGIC
DM TO BUY @RAJ_MAGIC
]]]

©RAJCRACKS
©RAJCRACKS
"""

# Encryption key (use a secure random key in production)
password = b"your_password"
salt = os.urandom(16)

# Derive a key from the password
kdf = PBKDF2HMAC(
    algorithm=hashes.SHA256(),
    length=32,
    salt=salt,
    iterations=100000,
    backend=default_backend()
)
key = kdf.derive(password)

# Encrypt the data
iv = os.urandom(16)
cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
encryptor = cipher.encryptor()
ciphertext = encryptor.update(data.encode()) + encryptor.finalize()

# Output encrypted data in Base64 format
encrypted_data = base64.b64encode(salt + iv + ciphertext).decode()
print(f"Encrypted data:\n{encrypted_data}")