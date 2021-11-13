from bsn_sdk_py.common import myecdsa256
from bsn_sdk_py.client.config import Config
from bsn_sdk_py.client.entity.bsn_base import BsnBase
from bsn_sdk_py.until.tools import nonce_str, array_sort, map_sort


class GetBlockInfo(BsnBase):
    """
    get block info
    """
    def __init__(self, blockNumber=0, blockHash='', txId=''):
        """
        :description  :
        :param blockNumber: block number
        :param blockHash:   block hash
        :param txId:        transaction hash
        :return  :
        """
        
        self.blockNumber = blockNumber
        self.blockHash = blockHash
        self.txId = txId

    def req_body(self):
        """
        :description  : build request body
        :param  :
        :return  :
        """

        req_body = {
            "blockNumber": self.blockNumber,
            "blockHash": self.blockHash,
            "txId": self.txId,
        }
        return req_body

    def sign(self, body):
        # assemble character string to sign
        sign_str = self.config.user_code + self.config.app_code + str(body['body']["blockNumber"]) + \
                   body['body']["blockHash"] + body['body']["txId"]
        # The string is signed with SHA256WITHECDSA using the user's private key certificate, and the ecdsa_sign method is called to generate base64-formatted MAC values.
        mac = self.config.encrypt_sign.sign(sign_str).decode()
        return mac

    def verify(self, res_data):
        verify_str = str(res_data["header"]["code"]) + res_data["header"]["msg"] + \
                     str(res_data['body']["blockHash"]) + str(res_data['body']["blockNumber"]) + \
                     res_data['body']["preBlockHash"] + str(res_data['body']["blockSize"]) + \
                     str(res_data['body']["blockTxCount"]) + array_sort(res_data['body']["transactions"])

        signature = res_data['mac']
        # Call the ecdsa_verify function to verify the signature
        return self.config.encrypt_sign.verify(verify_str, signature)
