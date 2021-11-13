from bsn_sdk_py.client.config import Config
from bsn_sdk_py.client.entity.bsn_base import BsnBase


class RegisterUser(BsnBase):
    '''
    user registration
    '''
    def __init__(
        self,
        config: Config,
        name,
        secret='',
    ):
        """
        :description  :
        :param  :   name: username , length less than 20
        :param  :   secret: user password 
        :return  :
        """

        self.name = name
        self.secret = secret
        self.config = config

    def req_body(self):
        """
        :description  : build request body
        :param  :
        :return  : build result
        """

        req_body = {
            "name": self.name,
            "secret": self.secret,
        }
        return req_body

    def sign(self):
        """
        :description  : signature 
        :param  : request body
        :return  :  signature result
        """

        # assemble character string to sign
        sign_str = self.config.user_code + self.config.app_code + self.name + self.secret
        # The string is signed with SHA256WITHECDSA using the user's private key certificate, and the ecdsa_sign method is called to generate base64-formatted MAC values.
        mac = self.config.encrypt_sign.sign(sign_str).decode()
        return mac

    def verify(self, res_data):
        """
        :description  : verify
        :param  : response result
        :return  : true/false
        """

        verify_str = str(res_data["header"]["code"]) + res_data["header"]["msg"] + \
                     str(res_data['body']["name"]) + str(res_data['body']["secret"])
        signature = res_data['mac']
        # Call the ecdsa_verify function to verify the signature
        return self.config.encrypt_sign.verify(verify_str, signature)