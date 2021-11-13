from bsn_sdk_py.client.config import Config
from bsn_sdk_py.common.api_requestor import APIRequestor
from bsn_sdk_py.client.bsn_enum import AppCaType
from bsn_sdk_py.until.bsn_logger import log_debug, log_info
from bsn_sdk_py.client.entity import RegisterUser, EnrollUser, ReqChainCode, GetTransaction, \
    GetBlockInfo, GetLedgerInfo, EventRegister, EventQuery, EventRemove, NoTrustTrans


class FabricClient(object):
    """
    Unify fabric app requests 
    """

    def __init__(self):
        pass

    def set_config(self, config: Config):
        self.config = config

    def build_req_data(self, req_body):
        """
        uniformly create the request meesage
        :param req_body: request body
        :return: build result
        """

        data = {
            "header": {
                "userCode": self.config.user_code,
                "appCode": self.config.app_code,
            },
            "body": req_body,
            "mac": "",
        }
        return data

    def common_request(self, req_url, req_data):
        """
        :description  : send request
        :param  : req_url: request url
        :param  : req_data: request data
        :return  : reponse result
        """
           
        res = APIRequestor().request_post(req_url, req_data)
        return res

    def register_user(self, name, secret=''):
        """
        user registration
        :param name: user name
        :param secret: user password
        :return:
        """

        req_url = self.config.nodeApi + "/api/fabric/v1/user/register"
        req_body = {
            "name": name,
            "secret": secret,
        }
        register_user = RegisterUser(self.config, name, secret)
        req_data = self.build_req_data(register_user.req_body())
        mac = register_user.sign()
        req_data["mac"] = mac
        res_data = self.common_request(req_url, req_data)
        assert register_user.verify(res_data)

        return res_data

    def enroll_user(self, name, secret):
        """
            user cert registration under Public-Key-Upload Mode
        :param name:
        :param secret:
        :return:
        """

        assert self.config.app_info[
            "caType"] == AppCaType.AppCaType_NoTrust.value, "only allow to register cert under Key-No-Trust Mode"
        req_url = self.config.nodeApi + "/api/fabric/v1/user/enroll"

        enroll_user_obj = EnrollUser(name, secret)
        enroll_user_obj.set_config(self.config)
        req_data = self.build_req_data(enroll_user_obj.req_body())
        mac = enroll_user_obj.sign()
        req_data["mac"] = mac
        res_data = self.common_request(req_url, req_data)
        assert enroll_user_obj.verify(res_data)
        enroll_user_obj.save_cert_to_file(res_data['body']['cert'].encode())
        return res_data

    def req_chain_code(self,
                       chainCode,
                       funcName,
                       name='',
                       args=[],
                       transientData: dict = {}):
        """
        transaction processing under Key-Trust Mode
        :param chainCode:   chincode code
        :param funcName:    function name
        :param name:    username
        :param args:    request args
        :param transientData:   extra data
        :return:
        """

        # assert self.config.app_info["caType"] == AppCaType.AppCaType_Trust.value, "transactions under Key-Trust Mode only allowed via this interface"

        req_url = self.config.nodeApi + "/api/fabric/v1/node/reqChainCode"
        req_chain_code_obj = ReqChainCode(chainCode, funcName, name, args,
                                          transientData)
        req_chain_code_obj.set_config(self.config)
        req_data = self.build_req_data(req_chain_code_obj.req_body())
        mac = req_chain_code_obj.sign(req_data)
        req_data["mac"] = mac
        res_data = self.common_request(req_url, req_data)
        assert req_chain_code_obj.verify(res_data)
        return res_data

    def get_transaction(self, txId):
        """
        Get transaction info
        :param txId: transaction hash
        :return:  response transaction information
        """

        req_url = self.config.nodeApi + "/api/fabric/v1/node/getTransaction"
        get_transaction_obj = GetTransaction(txId)
        get_transaction_obj.set_config(self.config)
        req_data = self.build_req_data(get_transaction_obj.req_body())
        log_info(req_data)
        mac = get_transaction_obj.sign(req_data)
        req_data["mac"] = mac

        res_data = self.common_request(req_url, req_data)
        log_info(res_data)

        assert get_transaction_obj.verify(res_data)

        return res_data

    def get_block_info(self, blockNumber=0, blockHash='', txId=''):
        """
        Get block info 
        :param blockNumber: block number
        :param blockHash:   block hash
        :param txId:        transaction hash
        :return:
        """

        assert any((
            blockNumber,
            blockHash,
            txId,
        )), "blockNumber or blockHash or txId cannot be empty at the same time"
        req_url = self.config.nodeApi + "/api/fabric/v1/node/getBlockInfo"
        get_block_info_obj = GetBlockInfo(blockNumber, blockHash, txId)
        get_block_info_obj.set_config(self.config)
        req_data = self.build_req_data(get_block_info_obj.req_body())
        mac = get_block_info_obj.sign(req_data)
        req_data["mac"] = mac
        res_data = self.common_request(req_url, req_data)
        assert get_block_info_obj.verify(res_data), "verification failure"
        return res_data

    def get_ledger_info(self):
        """
        Get the latest ledger info
        :return:
        """

        req_url = self.config.nodeApi + "/api/fabric/v1/node/getLedgerInfo"
        get_ledger_info_obj = GetLedgerInfo()
        get_ledger_info_obj.set_config(self.config)
        req_data = self.build_req_data(get_ledger_info_obj.req_body())
        mac = get_ledger_info_obj.sign(req_data)
        req_data["mac"] = mac
        res_data = self.common_request(req_url, req_data)
        assert get_ledger_info_obj.verify(res_data), "verification failure"
        return res_data

    def event_register(self, chainCode, eventKey, notifyUrl, attachArgs=''):
        """
        event chaincode registration
        :param chainCode:   chaincode code
        :param eventKey:    chaincode event key
        :param notifyUrl:   chaincode event notify url
        :param attachArgs:  extra args
        :return:
        """

        req_url = self.config.nodeApi + "/api/fabric/v1/chainCode/event/register"
        event_register_obj = EventRegister(chainCode, eventKey, notifyUrl,
                                           attachArgs)
        event_register_obj.set_config(self.config)
        req_data = self.build_req_data(event_register_obj.req_body())
        mac = event_register_obj.sign(req_data)
        req_data["mac"] = mac
        res_data = self.common_request(req_url, req_data)
        assert event_register_obj.verify(res_data), "verification failure"
        return res_data

    def event_query(self):
        """
        evernt chaincode query
        :return:
        """

        req_url = self.config.nodeApi + "/api/fabric/v1/chainCode/event/query"
        event_query_obj = EventQuery()
        event_query_obj.set_config(self.config)
        req_data = self.build_req_data(event_query_obj.req_body())
        mac = event_query_obj.sign(req_data)
        req_data["mac"] = mac
        res_data = self.common_request(req_url, req_data)
        assert event_query_obj.verify(res_data), "verification failure"
        return res_data

    def event_remove(self, eventId):
        """
        event chaincode logout
        :return:
        """

        req_url = self.config.nodeApi + "/api/fabric/v1/chainCode/event/remove"
        event_remove_obj = EventRemove(eventId)
        event_remove_obj.set_config(self.config)
        req_data = self.build_req_data(event_remove_obj.req_body())
        mac = event_remove_obj.sign(req_data)
        req_data["mac"] = mac
        res_data = self.common_request(req_url, req_data)
        assert event_remove_obj.verify(res_data), "verification failure"
        return res_data

    def not_trust_trans(self,
                        chainCode,
                        funcName,
                        name,
                        args: list = [],
                        transientData: dict = {}):
        """
        :description  : transaction under Public-Key-Upload Mode
        :param chainCode:   chincode code
        :param funcName:    function name
        :param name:    username
        :param args:    request args
        :param transientData:   extra data 
        :return  : 
        """
               
        req_url = self.config.nodeApi + "/api/fabric/v1/node/trans"
        not_trust_trans_obj = NoTrustTrans(chainCode, funcName, name, args,
                                           transientData)
        not_trust_trans_obj.set_config(self.config)
        req_data = self.build_req_data(not_trust_trans_obj.req_body())
        mac = not_trust_trans_obj.sign(req_data)
        req_data["mac"] = mac
        res_data = self.common_request(req_url, req_data)
        assert not_trust_trans_obj.verify(res_data), "verification failure"
        return res_data
