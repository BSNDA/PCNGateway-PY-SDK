import base64
from bsn_sdk_py.client.config import Config
from bsn_sdk_py.trans.transaction_header import get_notrust_trans_data, created_peer_proposal_signedproposal
from bsn_sdk_py.common.myecdsa256 import ecdsa_sign, hash256_sign
from bsn_sdk_py.until.bsn_logger import log_debug, log_info


class NotTrustTransRequest():
    """
    assemble transaction data under Public-Key-Upload Mode 
    """
    def __init__(self,
                 chainCode,
                 funcName,
                 userName,
                 args: list = None,
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

        self.name = userName
        self.chainCode = chainCode
        self.funcName = funcName
        self.args = args
        self.transientData = transientData

    def set_config(self, config: Config):
        self.config = config

    def _get_not_trust_private_key(self):
        """
        :description  : get application certificate
        :param  :
        :return  :
        """
        
        name = self.GetCertName()
        not_trust_tran_private_path = self.config.mspDir + r'\keystore\\' + name + '_private.pem'
        log_info(("user private key path", not_trust_tran_private_path))
        with open(not_trust_tran_private_path, "rb") as f:
            key_data = f.read()
        return key_data

    def GetCertName(self):
        """
        :description  : assemble application certificate name  
        """
        
        return self.name + "@" + self.config.app_code

    def notrust_trans_data(self):
        """
        :description  :  assemble the transaction in notrust
        :param  :
        :return  :
        """
        
        name = self.GetCertName()
        not_trust_tran_public_path = self.config.mspDir + r'\keystore\\' + name + '_cert.pem'
        peer_proposal_proposal = get_notrust_trans_data(
            channelID=self.config.app_info["channelId"],
            mspid=self.config.app_info["mspId"],
            chainCode=self.chainCode,
            cert_pub_path=not_trust_tran_public_path,
            transientData=self.transientData,
            args=self.args,
            funcName=self.funcName)
        proposal_proposal_bytes = peer_proposal_proposal.SerializeToString()
        # //proposal_proposal_bytes_s = hash256_sign(proposal_proposal_bytes)
        base64_sign = ecdsa_sign(proposal_proposal_bytes,
                                 self._get_not_trust_private_key())
        signedproposal = created_peer_proposal_signedproposal(
            peer_proposal_proposal, base64_sign)
        return str(base64.b64encode(signedproposal.SerializeToString()),
                   'utf-8')
