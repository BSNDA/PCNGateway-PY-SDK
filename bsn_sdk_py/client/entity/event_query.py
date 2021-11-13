from bsn_sdk_py.common import myecdsa256
from bsn_sdk_py.client.config import Config
from bsn_sdk_py.client.entity.bsn_base import BsnBase
from bsn_sdk_py.until.tools import nonce_str, array_sort, map_sort


class EventQuery(BsnBase):
    """
    event chaincode query
    """
    def __init__(self):
        pass

    def req_body(self):
        req_body = {}
        return req_body

    def sign(self, body):
        # assemble character string to sign
        sign_str = self.config.user_code + self.config.app_code
        # The string is signed with SHA256WITHECDSA using the user's private key certificate, and the ecdsa_sign method is called to generate base64-formatted MAC values.
        mac = self.config.encrypt_sign.sign(sign_str).decode()
        return mac

    def verify(self, res_data):
        verify_str = str(res_data["header"]
                         ["code"]) + res_data["header"]["msg"] + array_sort(
                             res_data['body'])

        # str(res_data['body']["eventId"]) + str(res_data['body']["eventKey"]) + \
        # str(res_data['body']["notifyUrl"]) + str(res_data['body']["attachArgs"]) + \
        # str(res_data['body']["createTime"]) + str(res_data['body']["orgCode"]) + \
        # str(res_data['body']["userCode"]) + str(res_data['body']["appCode"]) + \
        # str(res_data['body']["chainCode"])

        signature = res_data['mac']
        # Call the ecdsa_verify function to verify the signature
        return self.config.encrypt_sign.verify(verify_str, signature)