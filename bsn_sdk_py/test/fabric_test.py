import unittest
from bsn_sdk_py.client.config import Config
from bsn_sdk_py.client.fabric_client import FabricClient
import logging


# user under Public-Key-Upload Mode
c1 = Config(user_code="USER0001202304271508229312381", app_code="app0001202307200912041213788",
           nodeApi="https://gateway.node1.star.bsnbase.com:32000", mspDir=r"E:\python_workspase\hll\PCNGateway-PY-SDK\bsn_sdk_py\test", httpcert="",
                 user_private_cert_path=r"E:\python_workspase\hll\PCNGateway-PY-SDK\bsn_sdk_py\test\private.pem",
           app_public_cert_path=r"E:\python_workspase\hll\PCNGateway-PY-SDK\bsn_sdk_py\test\public.pem")

# user under Key-Trust Mode 
# c = Config(user_code="USER0001202004161009309407413", app_code="app0001202004161017141233920",
#            nodeApi="https://192.168.1.43:17502", mspDir=r"E:\hz_workspace\study\bsn_sdk_py\test", httpcert="",
#                  user_private_cert_path=r"E:\hz_workspace\study\bsn_sdk_py\test\private.pem",
#            app_public_cert_path=r"E:\hz_workspace\study\bsn_sdk_py\test\public.pem")


class TestBsn(unittest.TestCase):  # inherit unittest.TestCase

    @classmethod
    def setUpClass(cls):
        print('Setup of all cases 01')

    @classmethod
    def tearDownClass(cls):
        print('tearDown of all cases01')

    def setUp(self):
        print('Setup of every case01')
        FORMAT = "%(asctime)s %(thread)d %(message)s"
        logging.basicConfig(filename='bsn_test.log', filemode='w',level=logging.INFO, format=FORMAT, datefmt="[%Y-%m-%d %H:%M:%S]")
        # Create the requesting client
        client = FabricClient()
        client.set_config(c1)
        self.client = client

    def tearDown(self):
        print('tearDown of every case01')

    def test_req_chain_code(self):  # Name the teast case 'test', otherwise not executed
        print('Test: transaction processing under Key-Trust Mode')
        self.client.req_chain_code(chainCode="cc_app0001202307251453523461410_01", funcName='set', name='',
                              args=['{\"baseKey\":\"9\",\"baseValue\":\"this is string \"}'],
                              transientData={})

    def test_get_transaction(self):
        print('Test:get transaction info')
        txId = '3cab3a400ac14de911a3fd4ac08dd4d5d7993e18a97ab2c389313d3082afd427'
        self.client.get_transaction(txId)

    @unittest.skip('do not execute the case')  # skip the case
    def test_skip(self):
        print('01: the seconde case')

    def test_get_block_info(self):
        print('Test:get block info')
        txId = '364a7ce7c1f7c3fb7afb3ea2b9c678ed3dfd5e7c61ae72c4541822646fd24a19'
        self.client.get_block_info(txId=txId)

    def test_get_block_data(self):
        print('Test:get block data')
        block_data = self.client.get_block_data(blockNumber=5, dataType="Base64")
        print(block_data)

    def test_get_ledger_info(self):
        print('Test: get the latest ledger info')
        self.client.get_ledger_info()

    def test_event_register(self):
        print('Test: register event chaincode')
        chainCode = 'cc_app0001202004161020152918451_00'
        eventKey = 'test'
        notifyUrl = 'http://127.0.0.1'
        attachArgs = 'a=1'
        self.client.event_register(chainCode, eventKey, notifyUrl, attachArgs)

    def test_event_query(self):
        print('Test: event chaincode query')
        self.client.event_query()

    def test_event_remove(self):
        print('Test:event chaincode query')
        eventId = 'c70f0bc10a444bc4a1d916b05ffc6064'
        self.client.event_remove(eventId)

    def test_register_user(self):
        print('Test: register user')
        eventId = 'c70f0bc10a444bc4a1d916b05ffc6064'
        self.client.register_user('hll16', '123456')

    def test_enroll_user(self):
        print('Test:user registration cert under Public-Key-Upload Mode')
        eventId = 'c70f0bc10a444bc4a1d916b05ffc6064'
        self.client.enroll_user('hll16', '123456')

    def test_notrust_trans(self):
        print('Test: user registration cert under Public-Key-Upload Mode')
        self.client.not_trust_trans(chainCode="cc_app0001202307200912041213788_01", funcName='set', name='hll16',
                                   args=['{\"baseKey\":\"222\",\"baseValue\":\"this is string \"}'],
                                   transientData={})

if __name__ == '__main__':
    # unittest.main() # execute in the order of case names using main()
    suite = unittest.TestSuite()
    suite.addTest(TestBsn('test_req_chain_code'))  # add cases to the Test Suite to execute, not added not executed
    suite.addTest(TestBsn('test_get_transaction'))
    # suite.addTest(TestBsn('test_get_block_info'))
    # suite.addTest(TestBsn('test_get_ledger_info'))
    # suite.addTest(TestBsn('test_event_register'))
    # suite.addTest(TestBsn('test_event_query'))

    # suite.addTest(TestBsn('test_register_user'))
    # suite.addTest(TestBsn('test_enroll_user'))
    # suite.addTest(TestBsn('test_notrust_trans'))

    # suite.addTest(TestBsn('test_event_remove'))

    unittest.TextTestRunner().run(suite)  # executed in the order of adding cases
