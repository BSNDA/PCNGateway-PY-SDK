from bsn_sdk_py.common import myecdsa256
from bsn_sdk_py.client.config import Config
from bsn_sdk_py.client.entity.bsn_base import BsnBase


class EnrollUser(BsnBase):
    """
    :description  : user cert registration under Public-Key-Upload Mode
    """
    def __init__(self, name, secret):
        """
        :description  :
        :param  :
        :return  :
        """
        
        self.name = name
        self.secret = secret
        # self.csr_path = None
        # with open(self.csr_path, "rb") as fp:
        #     self.csr_key = fp.read()

    def GetCertificateRequest(self):
        name = self.GetCertName()
        csr_pem, private_path = myecdsa256.certificate_request(
            name, self.config.mspDir + r'\keystore\\' + name + '_private.pem')
        self.config.not_trust_tran_private_path = private_path
        self.csr_pem = csr_pem
        return csr_pem

    def req_body(self):
        # request cert
        csr_pem = self.GetCertificateRequest()
        req_body = {
            "name": self.name,
            "secret": self.secret,
            "csrPem": str(csr_pem, encoding="utf-8"),
        }
        return req_body

    def sign(self):
        # assemble character string to sign
        sign_str = self.config.user_code + self.config.app_code + self.name + self.secret + str(
            self.csr_pem, encoding="utf-8")
        # The string is signed with SHA256WITHECDSA using the user's private key certificate, and the ecdsa_sign function is called to generate base64-formatted MAC values.
        mac = self.config.encrypt_sign.sign(sign_str).decode()
        return mac

    def verify(self, res_data):
        verify_str = str(res_data["header"]["code"]) + res_data["header"]["msg"] + \
                     str(res_data['body']["cert"])
        signature = res_data['mac']
        # Call the ecdsa_verify function to verify the signature
        return self.config.encrypt_sign.verify(verify_str, signature)

    def GetCertName(self):
        return self.name + "@" + self.config.app_code

    def save_cert_to_file(self, csr_pem: bytes):
        name = self.GetCertName()
        public_path = self.config.mspDir + r'\keystore\\' + name + '_cert.pem'
        with open(public_path, mode='wb') as f:
            f.write(csr_pem)

        assert csr_pem.startswith(b"-----BEGIN CERTIFICATE-----")
