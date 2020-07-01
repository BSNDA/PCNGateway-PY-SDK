import logging
import sys
import re

PY2 = sys.version_info[0] == 2
PY3 = sys.version_info[0] == 3
logger = logging.getLogger("bsn_sdk_py")


def log_debug(message, **params):
    msg = logfmt(dict(message=message, **params))
    logger.debug(msg)


def log_info(message, **params):
    msg = logfmt(dict(message=message, **params))
    logger.info(msg)



def logfmt(props):
    def fmt(key, val):
        # Handle case where val is a bytes or bytesarray
        if PY3 and hasattr(val, "decode"):
            val = val.decode("utf-8")
        # Check if val is already a string to avoid re-encoding into
        # ascii. Since the code is sent through 2to3, we can't just
        # use unicode(val, encoding='utf8') since it will be
        # translated incorrectly.
        if not isinstance(val, str):
            val = str(val)
        if re.search(r"\s", val):
            val = repr(val)
        # key should already be a string
        if re.search(r"\s", key):
            key = repr(key)
        return u"{key}={val}".format(key=key, val=val)

    return u" ".join([fmt(key, val) for key, val in sorted(props.items())])


if __name__=='__main__':
    FORMAT = "%(asctime)s %(thread)d %(message)s"
    logging.basicConfig(level=logging.INFO, format=FORMAT, datefmt="[%Y-%m-%d %H:%M:%S]")

    log_info(("dsdas",111))