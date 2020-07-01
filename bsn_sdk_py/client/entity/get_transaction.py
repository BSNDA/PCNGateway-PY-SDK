from bsn_sdk_py.common import myecdsa256
from bsn_sdk_py.client.config import Config
from bsn_sdk_py.client.entity.bsn_base import BsnBase
from bsn_sdk_py.until.tools import nonce_str, array_sort, map_sort


class GetTransaction(BsnBase):
    """
    get transaction info
    """
    def __init__(self, txId):
        self.txId = txId

    def req_body(self):
        req_body = {
            "txId": self.txId,
        }
        return req_body


    def sign(self, body):
        # assemble character string to sign
        sign_str = self.config.user_code + self.config.app_code + body['body']["txId"]
        # The string is signed with SHA256WITHECDSA using the user's private key certificate, and the ecdsa_sign method is called to generate base64-formatted MAC values.
        # mac = myecdsa256.ecdsa_sign(sign_str, self.config.user_private_key).decode()
        mac = self.config.encrypt_sign.sign(sign_str).decode()
        return mac

    def verify(self, res_data):
        verify_str = str(res_data["header"]["code"]) + res_data["header"]["msg"] + \
                     str(res_data['body']["blockHash"]) + str(res_data['body']["blockNumber"]) + \
                     str(res_data['body']["status"]) + str(res_data['body']["createName"]) + \
                     str(res_data['body']["timeSpanSec"]) + str(res_data['body']["timeSpanNsec"])

        signature = res_data['mac']
        # Call the ecdsa_verify function to verify the signature
        # return myecdsa256.ecdsa_verify(verify_str, signature, self.config.app_public_key)

        return self.config.encrypt_sign.verify(verify_str, signature)

