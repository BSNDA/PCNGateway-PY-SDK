from enum import IntEnum


class AppAlgorithmType(IntEnum):
    """
    App algorithm type
    """

    AppAlgorithmType_Not = 0
    AppAlgorithmType_SM2 = 1  # SM2
    AppAlgorithmType_R1 = 2  # ECDSA(secp256r1)
    AppAlgorithmType_K1 = 3  # ECDSA(secp256K1)


class AppCaType(IntEnum):
    """
    Type of key mode
    """

    AppCaType_Not = 0
    AppCaType_Trust = 1  # Key-Trust Mode
    AppCaType_NoTrust = 2  # Public-Key-Upload Mode


class ResCode(IntEnum):
    """
       Type of key mode
       """
       
    ResCode_Suc = 0  # success
    ResCode_Fail = -1  # failure
