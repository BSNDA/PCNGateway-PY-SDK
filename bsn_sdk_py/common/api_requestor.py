import requests
from bsn_sdk_py.client.exceptions import BsnException
from bsn_sdk_py.client.bsn_enum import ResCode
from bsn_sdk_py.until.bsn_logger import log_debug, log_info
import urllib3
import logging

logging.captureWarnings(True)
urllib3.disable_warnings()  ## Cancel the HTTPS request 2020/08/25


class APIRequestor(object):
    '''
    common request object
    '''
    def __init__(self, cert_path=False):
        self.cert_path = cert_path

    def request_post(self, req_url, data):
        """
        :description  : post request
        :param  : req_url : request url
        :param  : data : request data
        :return  : 
        """

        log_info(("request address：", req_url))
        log_info(("request data：", data))
        headers = {'content-type': 'application/json'}
        # res = requests.post(req_url, headers=headers, json=data, verify=self.cert_path)
        res = requests.post(req_url, headers=headers, json=data, verify=False)
        resCode = res.status_code
        # resHeaders = res.headers
        # log_info(('received response headers：', resHeaders))
        if resCode != 200:
            raise Exception('request failure,http code:{}'.format(resCode, ))
        resBody = res.json()
        log_info(('response：', resBody))
        if resBody['header'][
                "code"] != ResCode.ResCode_Suc.value:  # return success, decrypt
            raise BsnException(resBody['header']["code"],
                               resBody['header']["msg"])
        return resBody

    def request_get(self):
        pass