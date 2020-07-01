import base64
import hashlib
import time
from google.protobuf.timestamp_pb2 import Timestamp
from bsn_sdk_py.until.tools import nonce_str
from bsn_sdk_py.trans.protobuf_entity.msp import identities_pb2
from bsn_sdk_py.trans.protobuf_entity.peer import chaincode_pb2, proposal_pb2
from bsn_sdk_py.trans.protobuf_entity.common import common_pb2


class TransactionHeader:
    def __init__(self, TransactionID, creator, Nonce, ChannelID):
        self.TransactionID = TransactionID
        self.creator = creator
        self.Nonce = Nonce
        self.ChannelID = ChannelID





def hash256_sign(o_str):
    sha256 = hashlib.sha256()
    sha256.update(o_str)
    return sha256.hexdigest()  # .upper()


def created_peer_chaincode_chaincodeid(name):
    peer_chaincode_chaincodeid = chaincode_pb2.ChaincodeID()
    peer_chaincode_chaincodeid.name = name
    return peer_chaincode_chaincodeid


def created_peer_proposal_chaincodeheaderextension(chaincodeId: chaincode_pb2.ChaincodeID):
    peer_proposal_chaincodeheaderextension = proposal_pb2.ChaincodeHeaderExtension()
    peer_proposal_chaincodeheaderextension.chaincode_id.CopyFrom(chaincodeId)
    return peer_proposal_chaincodeheaderextension


def created_msp_identities_serializedidentity(mspid, cert_pub_path):
    identities = identities_pb2.SerializedIdentity()
    identities.mspid = mspid
    with open(cert_pub_path, "rb") as fp:
        app_public_key = fp.read()
    identities.id_bytes =app_public_key
    return identities


def created_my_transactionheader(channelID, mspid, cert_pub_path):
    identities = created_msp_identities_serializedidentity(mspid, cert_pub_path)
    identities_str = identities.SerializeToString()
    nonc = nonce_str()
    sign_str = bytes(nonc, 'utf-8') + identities_str
    sign256_end = hash256_sign(sign_str)

    t = TransactionHeader(sign256_end, identities_str, nonc, channelID)
    return t


def created_common_common_channelheader(t: TransactionHeader,
                                        chaincodeheaderextension: proposal_pb2.ChaincodeHeaderExtension):
    comm_channel_header = common_pb2.ChannelHeader()
    comm_channel_header.type = common_pb2.ENDORSER_TRANSACTION
    comm_channel_header.tx_id = t.TransactionID
    comm_channel_header.timestamp.CopyFrom(get_timestamp())
    comm_channel_header.channel_id = t.ChannelID
    comm_channel_header.extension = chaincodeheaderextension.SerializeToString()
    comm_channel_header.epoch = 0


    return comm_channel_header


def created_common_common_signatureheader(t:TransactionHeader):
    common_signatureheader = common_pb2.SignatureHeader()
    common_signatureheader.nonce = bytes(t.Nonce, 'utf-8')
    common_signatureheader.creator = t.creator
    return common_signatureheader


def created_common_common_header(channelheader: common_pb2.ChannelHeader, signatureheader: common_pb2.SignatureHeader):
    common_header = common_pb2.Header()
    common_header.channel_header = channelheader.SerializeToString()
    common_header.signature_header = signatureheader.SerializeToString()
    return common_header


def created_peer_chaincode_chaincodeinput(args_bytes):
    peer_chaincode_chaincodeinput = chaincode_pb2.ChaincodeInput()
    peer_chaincode_chaincodeinput.args.extend(args_bytes)
    return peer_chaincode_chaincodeinput

def created_peer_chaincode_chaincodespec(chaincodeId, chaincodeInput):
    peer_chaincode_chaincodespec = chaincode_pb2.ChaincodeSpec()
    peer_chaincode_chaincodespec.type = chaincode_pb2.ChaincodeSpec.Type.GOLANG
    peer_chaincode_chaincodespec.chaincode_id.CopyFrom(chaincodeId)
    # print(chaincodeInput.args, type(chaincodeInput.args[0]))
    peer_chaincode_chaincodespec.input.CopyFrom(chaincodeInput)
    return peer_chaincode_chaincodespec

def created_peer_chaincode_chaincodeinvocationspec(chaincodeSpec:chaincode_pb2.ChaincodeSpec):
    peer_chaincode_chaincodeinvocationspec = chaincode_pb2.ChaincodeInvocationSpec()
    peer_chaincode_chaincodeinvocationspec.chaincode_spec.CopyFrom(chaincodeSpec)

    return peer_chaincode_chaincodeinvocationspec


def created_peer_proposal_chaincodeproposalpayload(payloadInput, transientData:dict):
    peer_proposal_chaincodeproposalpayload = proposal_pb2.ChaincodeProposalPayload()
    peer_proposal_chaincodeproposalpayload.input = payloadInput.SerializeToString()
    for (k,v) in transientData.items():
        peer_proposal_chaincodeproposalpayload.TransientMap[k] = bytes(v, 'utf-8')
    return peer_proposal_chaincodeproposalpayload


def created_peer_proposal_proposal(common_common_header:common_pb2.Header,
                                   payload:proposal_pb2.ChaincodeProposalPayload):
    peer_proposal_proposal = proposal_pb2.Proposal()

    peer_proposal_proposal.header = common_common_header.SerializeToString()
    peer_proposal_proposal.payload = payload.SerializeToString()
    return peer_proposal_proposal

def get_timestamp():
    #  create google.protobuf.Timestamp
    now = time.time()
    seconds = int(now)
    nanos = int((now - seconds) * 10 ** 9)
    timestamp = Timestamp(seconds=seconds, nanos=nanos)
    return timestamp


def get_notrust_trans_data(channelID, mspid, chainCode, cert_pub_path, transientData, args, funcName):
    """

    :param channelID: DApp chain name	channelId	String	Yes
    :param mspid: City MSPID	mspId	String	                                Yes
    :param chainCode: chainCode	chainCode	String	Yes
    :param cert_pub_path:
    :param transientData: transientData transientData Map<string,string>  No
    :param args: request parameter	args	String[]	                No
    :param funcName: function name	funcName	String	Yes
    :return:
    """

    # payload assembly
    chaincodeId = created_peer_chaincode_chaincodeid(chainCode)

    args_bytes = []
    args_bytes.append(bytes(funcName, 'utf-8'))
    for a in args:
        args_bytes.append(bytes(a, 'utf-8'))

    peer_chaincode_chaincodeinput = \
        created_peer_chaincode_chaincodeinput(args_bytes)

    peer_chaincode_chaincodespec = \
        created_peer_chaincode_chaincodespec(chaincodeId, peer_chaincode_chaincodeinput)

    peer_chaincode_chaincodeinvocationspec = \
        created_peer_chaincode_chaincodeinvocationspec(peer_chaincode_chaincodespec)

    peer_proposal_chaincodeproposalpayload = \
        created_peer_proposal_chaincodeproposalpayload(
        peer_chaincode_chaincodeinvocationspec, transientData)

    # header assembly 
    transaction_header = created_my_transactionheader(channelID, mspid, cert_pub_path)
    peer_proposal_chaincodeheaderextension = created_peer_proposal_chaincodeheaderextension(chaincodeId)
    comm_channel_header = created_common_common_channelheader(
        transaction_header, peer_proposal_chaincodeheaderextension)

    common_signatureheader = created_common_common_signatureheader(transaction_header)

    common_common_header = created_common_common_header(comm_channel_header, common_signatureheader)

    peer_proposal_proposal = created_peer_proposal_proposal(common_common_header, peer_proposal_chaincodeproposalpayload)
    return peer_proposal_proposal


def created_peer_proposal_signedproposal(peer_proposal_proposal: proposal_pb2.Proposal, base64_sign):
    peer_proposal_signedproposal = proposal_pb2.SignedProposal()
    peer_proposal_signedproposal.proposal_bytes = peer_proposal_proposal.SerializeToString()
    peer_proposal_signedproposal.signature = base64_sign
    return peer_proposal_signedproposal


if __name__ == '__main__':
    from bsn_sdk_py.common.myecdsa256 import ecdsa_sign
    chainCode = 'cc_bcj'
    funcName = 'set'
    args = [
            "16399b5085ee5d3981f5076c33c5a0a66d7f2f3545b4d88501116a8bd53d13a5",
            "{'fileName':'test.jpg','fileHash':'6cfacf57e5b27f71a47a812938021784'}"
        ]
    transientData = {}
    channelID = 'app0001202004161020152918451'
    mspid = 'OrgbNodeMSP'
    cert_pub_path =r'E:\hz_workspace\study\bsn_sdk_py\test\keystore\hll3@app0001202004161020152918451_cert.pem'

    peer_proposal_proposal = get_notrust_trans_data(
        channelID=channelID,
        mspid=mspid,
        cert_pub_path=r'E:\hz_workspace\study\bsn_sdk_py\test\keystore\hll3@app0001202004161020152918451_cert.pem',
        transientData=transientData,
        args=args,
        funcName=funcName,
        chainCode=chainCode)

    proposal_proposal_bytes = str(peer_proposal_proposal.SerializeToString())

    with open(r'E:\hz_workspace\study\bsn_sdk_py\test\keystore\hll3@app0001202004161020152918451_private.pem', "rb") as f:
        key_data = f.read()


    base64_sign = ecdsa_sign(proposal_proposal_bytes, key_data)
    signedproposal = created_peer_proposal_signedproposal(peer_proposal_proposal, base64_sign)
    a = str(base64.b64encode(signedproposal.SerializeToString()))
    print(a)


