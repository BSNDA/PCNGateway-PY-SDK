from bsn_sdk_py.common import myecdsa256
from bsn_sdk_py.client.config import Config
from bsn_sdk_py.client.entity.bsn_base import BsnBase
from bsn_sdk_py.until.tools import nonce_str, array_sort, map_sort, obj_sort


class ReqChainCode(BsnBase):
    def __init__(self,
                 chainCode,
                 funcName,
                 name='',
                 args=[],
                 transientData: dict = {}):
        """
        :description  : transaction processing under Key-Trust Mode
        :param chainCode:   chincode code
        :param funcName:    function name
        :param name:    username
        :param args:    request args
        :param transientData:   extra data
        :return  :
        """

        self.name = name
        self.chainCode = chainCode
        self.funcName = funcName
        self.args = args
        self.transientData = transientData

    def req_body(self):
        """
        :description  : build request body
        :param  :
        :return  :
        """

        req_body = {
            "userName": self.name,
            "nonce": nonce_str(),
            "chainCode": self.chainCode,
            "funcName": self.funcName,
            "args": self.args,
            "transientData": self.transientData,
        }
        return req_body

    def sign(self, body):
        """
        :description  : signature 
        :param  : request body
        :return  :  signature result
        """

        # assemble character string to sign
        sign_str = self.config.user_code + self.config.app_code + body['body']["userName"] + body['body']["nonce"] \
                   + body['body']["chainCode"] + body['body']["funcName"] + \
                   array_sort(body['body']["args"]) + map_sort(body['body']["transientData"])
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
                     obj_sort(res_data['body']["blockInfo"]) + obj_sort(res_data['body']["ccRes"])

        signature = res_data['mac']
        #  Call the ecdsa_verify function to verify the signature
        return self.config.encrypt_sign.verify(verify_str, signature)