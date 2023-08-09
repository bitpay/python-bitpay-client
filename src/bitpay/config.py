from enum import Enum


class Config(Enum):
    TEST_URL = "https://test.bitpay.com/"
    PROD_URL = "https://bitpay.com/"
    BITPAY_API_VERSION = "2.0.0"
    BITPAY_PLUGIN_INFO = "BitPay_Python_Client_v4.0.1"
    BITPAY_API_FRAME = "std"
    BITPAY_API_FRAME_VERSION = "1.0.0"
