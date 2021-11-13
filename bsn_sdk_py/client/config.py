import json
from cryptography.hazmat.primitives.serialization import load_pem_private_key
from cryptography.hazmat.backends import default_backend
from bsn_sdk_py.common.api_requestor import APIRequestor
from bsn_sdk_py.client.bsn_enum import AppAlgorithmType
from bsn_sdk_py.common.bsn_encrypt import ECDSA, SM2
from bsn_sdk_py.client.exceptions import BsnException


class Config(object):
    """
    Define a generic configuration
    """
    def __init__(self,
                 user_code,
                 app_code,
                 nodeApi,
                 mspDir,
                 httpcert,
                 app_public_cert_path,
                 user_private_cert_path,
                 debug=False):
        """
        @description  :
        @param  : 
            user_code:  unique user identification
            app_code:   application unique identifier
            nodeApi:    node address: ip:port
            mspDir:    
            httpcert: https  certificate
            app_public_cert_path:  path to the application access public key file
            user_private_cert_path:  path to the private key file traded by the user
        @return  :
        """

        self.user_code = user_code
        self.app_code = app_code
        self.nodeApi = nodeApi  # node gateway
        self.mspDir = mspDir  # cert storage directory
        self.httpcert = httpcert  # https cert
        self.user_private_cert_path = user_private_cert_path

        # with open(self.user_private_cert_path, "rb") as fp:
        #     self.user_private_key = fp.read()

        self.app_public_cert_path = app_public_cert_path
        # with open(self.app_public_cert_path, "rb") as fp:
        #     self.app_public_key = fp.read()

        self.app_info = None
        self.app_info = self.getAppInfo()
        self.setAlgorithm()
        # print(self.app_info)

    def setAlgorithm(self):
        if self.app_info[
                'algorithmType'] == AppAlgorithmType.AppAlgorithmType_R1.value:
            self.encrypt_sign = ECDSA(self.user_private_cert_path,
                                      self.app_public_cert_path)
        elif self.app_info[
                'algorithmType'] == AppAlgorithmType.AppAlgorithmType_SM2.value:
            self.encrypt_sign = SM2(self.user_private_cert_path,
                                    self.app_public_cert_path)
        else:
            raise BsnException('-1', "invalid cert type")

    def getAppInfo(self):
        """
        unify DApp info：  get application information
        {'appName': 'sdktest-key no-trust mode', 'appType': 'fabric', 'caType': 2, 'algorithmType': 2,
        'mspId': 'OrgbNodeMSP', 'channelId': 'app0001202004161020152918451'}
        :return: response basic application information
        """

        req_url = self.nodeApi + "/api/app/getAppInfo"
        req_data = self.build_body()
        res = APIRequestor().request_post(req_url, req_data)
        return res["body"]

    def build_body(self):
        """
        @description  :  building the request body
        @param  :
        @return  :
        """

        data = {
            "header": {
                "userCode": self.user_code,
                "appCode": self.app_code,
            },
            "body": None,
            "mac": "",
        }
        return data


def read_private(pri_key_file_path):
    """
    @description  : load private key 
    @param  :
    @return  :
    """

    pri_key_file = open(pri_key_file_path, "rb")
    key_data = pri_key_file.read()
    pri_key_file.close()

    # Download private key
    skey = load_pem_private_key(key_data,
                                password=None,
                                backend=default_backend())
