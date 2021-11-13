import base64
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.serialization import load_pem_private_key, Encoding, PrivateFormat
from cryptography.x509 import load_pem_x509_certificate, NameOID
from hfc.util.crypto.crypto import Ecies, ecies, CURVE_P_256_Size, SHA2
from bsn_sdk_py.until.bsn_logger import log_debug, log_info


class BsnCrypto():
    """
    :description  : bsn basic signature Class
    """
    def __init__(self, private_key_path, pubilc_key_path):
        self.private_key_data = self._load_private_key_data(private_key_path)
        self.pubilc_key_data = self._load_pubilc_key_data(pubilc_key_path)

    def sign(self, message):
        pass

    def verify(self, message, signature):
        pass


class ECDSA(BsnCrypto):
    """
    :description  : ECDSA signature Class
    """
    
    
    def __init__(self, private_key_path, pubilc_key_path):
        super().__init__(private_key_path, pubilc_key_path)

    def _load_private_key_data(self, user_private_cert_path):
        with open(user_private_cert_path, "rb") as fp:
            user_private_key = fp.read()
        skey = load_pem_private_key(user_private_key,
                                    password=None,
                                    backend=default_backend())
        return skey

    def _load_pubilc_key_data(self, app_public_cert_path):
        with open(app_public_cert_path, "rb") as fp:
            pubilc_key_data = fp.read()
        # Load the X509 cert public key cert
        cert = load_pem_x509_certificate(pubilc_key_data, default_backend())
        # print("public key cert:", cert)

        # take contents of public key
        public_key = cert.public_key()
        # print("content of public key public_key:", public_key)
        return public_key

    def sign(self, message):
        log_info("ECDSA sign")
        # load private key
        # Sign using the function in the official library
        signature = Ecies(CURVE_P_256_Size,
                          SHA2).sign(private_key=self.private_key_data,
                                     message=message.encode('utf-8'))
        # print("signature:", signature)
        # return signarure value in base64 format
        return base64.b64encode(signature)

    def verify(self, message, signature):
        log_info("ECDSA verify signature")
        print(message)
        # read the signed data
        mac = signature
        # verify the signature
        verify_results = Ecies().verify(public_key=self.pubilc_key_data,
                                        message=message.encode('utf-8'),
                                        signature=base64.b64decode(mac))
        # print("verify_results:", verify_results)

        # return value T or F
        return verify_results


class SM2(BsnCrypto):
    """
    :description  : sm signature Class
    """
    
    
    def __init__(self, private_key_path, pubilc_key_path):
        super().__init__(private_key_path, pubilc_key_path)

    def _load_private_key_data(self, user_private_cert_path):
        pass

    def _load_pubilc_key_data(self, app_public_cert_path):
        pass

    def sign(self, message):
        log_info("SM2 sign")
        return message

    def verify(self, message, signature):
        log_info("SM2 verify the signature")
        return True


if __name__ == '__main__':
    s = SM2()