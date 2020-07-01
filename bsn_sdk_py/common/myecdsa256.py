import os
import base64
import hashlib
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.serialization import load_pem_private_key, Encoding, PrivateFormat
from cryptography.x509 import load_pem_x509_certificate, NameOID
# introduce signature class Ecies in the official package, default instantiation(CURVE_P_256_Size, SHA2)，CURVE_P_256_Size elliptic curvature and sha256 algorithm
from hfc.util.crypto.crypto import Ecies, ecies, CURVE_P_256_Size, SHA2
from cryptography import x509
from cryptography.hazmat.primitives import serialization


# ecdsa256 signature
def ecdsa_sign(message, key_data):
    """
	:param message: character string to sign
	:param pri_key_file_name: user private key path
	:return: return signature value in base64 format
	"""
    # Read the pri_key_file
    # path = os.path.abspath('.')
    # file = os.path.join(path, pri_key_file_name)
    # print('private key storage path: ', file)
    # pri_key_file = open(file, "rb")
    # key_data = pri_key_file.read()
    # pri_key_file.close()

    # load private key
    skey = load_pem_private_key(key_data, password=None, backend=default_backend())

    # sign using the function in the official library 
    signature = Ecies(CURVE_P_256_Size, SHA2).sign(private_key=skey, message=message)

    # print("signature:", signature)
    # return signature value in base64 format base64.b64encode(signature)
    return signature


# ecdsa256 verification function
def ecdsa_verify(message, signature, key_data):
    """
	:param message: character string to sign 
	:param signature: mac value in the return message 
	:param pub_key_file: gateway public key path
	:return: return True or False
	"""
    # read the content of public key 
    # path = os.path.abspath('.')
    # file = os.path.join(path, pub_key_file)
    # print('gateway public key directory path: ', file)
    # pub_key_file = open(file, "rb")
    # key_data = pub_key_file.read()
    # pub_key_file.close()

    # load X509 cert public key
    cert = load_pem_x509_certificate(key_data, default_backend())
    # print("public key cert:", cert)

    # read the content of public key
    public_key = cert.public_key()
    # print("the content of public key public_key:", public_key)

    # read the signed data 
    mac = signature

    # verify the signature
    verify_results = Ecies().verify(public_key=public_key, message=message.encode('utf-8'),
                                    signature=base64.b64decode(mac))
    # print("verify_results:", verify_results)

    # return value T or F
    return verify_results


def certificate_request(name, save_path):
    ecies256 = ecies()
    private_key = ecies256.generate_private_key()
    csr = ecies256.generate_csr(private_key, x509.Name(
        [x509.NameAttribute(NameOID.COMMON_NAME, name)]))  # test02@app0001202004161020152918451
    csr_pem = csr.public_bytes(Encoding.PEM)
    sk_pem = private_key.private_bytes(Encoding.PEM, PrivateFormat.PKCS8, serialization.NoEncryption())
    with open(save_path, mode='wb') as f:
        f.write(sk_pem)

    # with open('pub.csr', mode='wb') as f:
    #     f.write(csr_pem)
    return csr_pem, save_path


def hash256_sign(o_str):
    sha256 = hashlib.sha256()
    sha256.update(o_str.encode('utf-8'))
    return sha256.hexdigest()  # .upper()


if __name__ == '__main__':
    o_str = 'USER0001202004151958010871292app00012020041610201529184510364a7ce7c1f7c3fb7afb3ea2b9c678ed3dfd5e7c61ae72c4541822646fd24a19'
    print((hash256_sign(o_str)))
