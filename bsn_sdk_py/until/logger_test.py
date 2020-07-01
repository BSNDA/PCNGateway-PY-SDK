import unittest
import logging
from bsn_sdk_py.until.bsn_logger import log_info


class TestLogger(unittest.TestCase):

    def setUp(self):
        FORMAT = "%(asctime)s %(thread)d %(message)s"
        logging.basicConfig(level=logging.INFO, format=FORMAT, datefmt="[%Y-%m-%d %H:%M:%S]")

    def test_log_info(self):
        log_info('1111111111')


if __name__ == '__main__':
    unittest.main()