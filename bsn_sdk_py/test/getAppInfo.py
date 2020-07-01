from bsn_sdk_py.client.config import Config
from bsn_sdk_py.client.fabric_client import FabricClient

c = Config(user_code="USER0001202004151958010871292", app_code="app0001202004161020152918451",
           nodeApi="http://192.168.1.43:17502", mspDir=r"E:\hz_workspace\study\bsn_sdk_py\test", httpcert="",
                 user_private_cert_path=r"E:\hz_workspace\study\bsn_sdk_py\test\private.pem",
           app_public_cert_path=r"E:\hz_workspace\study\bsn_sdk_py\test\public.pem")

client = FabricClient()
client.set_config(c)
# register = client.register_user('hll3','123456')
# print("register:", register)
# client.enroll_user('hll3', '123456')

client.req_chain_code(chainCode="cc_app0001202004161020152918451_00", funcName='set', name='',
                      args=["{\"baseKey\":\"test20200415\",\"baseValue\":\"this is string \"}"],
                      transientData={})



