import unittest
import base64
from bsn_sdk_py.trans.transaction_header import created_peer_chaincode_chaincodeinvocationspec,\
    created_peer_chaincode_chaincodeinput, created_peer_chaincode_chaincodespec,\
    created_peer_chaincode_chaincodeid

class TestRequest(unittest.TestCase):

    def test_ChaincodeInvocationSpec(self):
        args_bytes = [
            "111"
        ]
        chaincodeId = 'app0006202004071529586812466'
        funcName = 'set'

        args=[]
        args.append(bytes(funcName, 'utf-8'))
        for a in args_bytes:
            args.append(bytes(a, 'utf-8'))
        peer_chaincode_chaincodeinput = \
            created_peer_chaincode_chaincodeinput(args)
        print("chaincodeInput_s:",base64.b64encode(peer_chaincode_chaincodeinput.SerializeToString()))

        chaincodeId_obj = created_peer_chaincode_chaincodeid(chaincodeId)
        print("chaincodeID_s:",base64.b64encode(chaincodeId_obj.SerializeToString()))

        peer_chaincode_chaincodespec = \
            created_peer_chaincode_chaincodespec(chaincodeId_obj, peer_chaincode_chaincodeinput)
        print("chaincodeSpec_s:",base64.b64encode(peer_chaincode_chaincodespec.SerializeToString()))

        peer_chaincode_chaincodeinvocationspec = \
            created_peer_chaincode_chaincodeinvocationspec(peer_chaincode_chaincodespec)
        spec = peer_chaincode_chaincodeinvocationspec.SerializeToString()
        print("ccis:",base64.b64encode(spec))


