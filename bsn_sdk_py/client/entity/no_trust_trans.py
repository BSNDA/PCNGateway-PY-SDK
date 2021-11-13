from bsn_sdk_py.common import myecdsa256
from bsn_sdk_py.client.config import Config
from bsn_sdk_py.client.entity.bsn_base import BsnBase
from bsn_sdk_py.until.tools import nonce_str, array_sort, map_sort, obj_sort
from bsn_sdk_py.trans.not_trust_trans_request import NotTrustTransRequest


# transaction under Public-Key-Upload Mode
class NoTrustTrans(BsnBase):
    """
    No trust transaction
    """
    def __init__(self,
                 chainCode,
                 funcName,
                 userName,
                 args=None,
                 transientData: dict = None):
        """
        :description  : 
        :param chainCode:   chincode code
        :param funcName:    function name
        :param userName:    username
        :param args:    request args
        :param transientData:   extra data 
        :return  :
        """
        
        super().__init__()
        self.name = userName
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
        
        transRequest = NotTrustTransRequest(self.chainCode, self.funcName,
                                            self.name, self.args,
                                            self.transientData)
        transRequest.set_config(self.config)
        transRequest_data = transRequest.notrust_trans_data()
        req_body = {
            "transData": transRequest_data,
        }
        return req_body

    def sign(self, body):
        # assemble character string to sign
        sign_str = self.config.user_code + self.config.app_code + body['body'][
            "transData"]
        # The string is signed with SHA256WITHECDSA using the user's private key certificate, and the ecdsa_sign method is called to generate base64-formatted MAC values.
        mac = self.config.encrypt_sign.sign(sign_str).decode()
        return mac

    def verify(self, res_data):
        verify_str = str(res_data["header"]["code"]) + res_data["header"]["msg"] + \
                     obj_sort(res_data['body']["blockInfo"]) + obj_sort(res_data['body']["ccRes"])

        signature = res_data['mac']
        # Call the ecdsa_verify function to verify the signature
        return self.config.encrypt_sign.verify(verify_str, signature)
