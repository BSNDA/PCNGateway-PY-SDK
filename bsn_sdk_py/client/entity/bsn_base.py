from bsn_sdk_py.client.config import Config


class BsnBase(object):

    def __init__(self):
        pass

    def set_config(self, config:Config ):
        self.config = config