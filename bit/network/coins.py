
class Coin:

    MAIN_PUBKEY_HASH = None
    MAIN_SCRIPT_HASH = [None]
    MAIN_PRIVATE_KEY = None
    MAIN_BIP32_PUBKEY = b'\x04\x88\xb2\x1e'
    MAIN_BIP32_PRIVKEY = b'\x04\x88\xad\xe4'
    TEST_PUBKEY_HASH = None
    TEST_SCRIPT_HASH = None
    TEST_PRIVATE_KEY = None
    TEST_BIP32_PUBKEY = b'\x045\x87\xcf'
    TEST_BIP32_PRIVKEY = b'\x045\x83\x94'
    PUBLIC_KEY_UNCOMPRESSED = b'\x04'
    PUBLIC_KEY_COMPRESSED_EVEN_Y = b'\x02'
    PUBLIC_KEY_COMPRESSED_ODD_Y = b'\x03'
    PRIVATE_KEY_COMPRESSED_PUBKEY = b'\x01'
    RPC_PORT = None

class Bitcoin(Coin):

    COIN_NAME = "Bitcoin"
    COIN_SHORT_NAME = "BTC"
    MAIN_PUBKEY_HASH = b'\x00'
    MAIN_SCRIPT_HASH = [b'\x05']
    MAIN_PRIVATE_KEY = b'\x80'
    TEST_PUBKEY_HASH = b'\x6f'
    TEST_SCRIPT_HASH = b'\xc4'
    TEST_PRIVATE_KEY = b'\xef'
    RPC_PORT = 8332

class Litecoin(Coin):
    COIN_NAME = "Litecoin"
    COIN_SHORT_NAME = "LTC"
    MAIN_PUBKEY_HASH = b'\x30'
    MAIN_SCRIPT_HASH = [b'\x32', b'\x05']
    MAIN_PRIVATE_KEY = b'\xb0'
    MAIN_BIP32_PUBKEY = b'\x01\x9d\x9c\xfe'
    MAIN_BIP32_PRIVKEY = b'\x01\x9d\xa4\x62'
    RPC_PORT = 9332

class Rubycoin(Coin):

    COIN_NAME = "Rubycoin"
    COIN_SHORT_NAME = "RBY"
    MAIN_PUBKEY_HASH = b'\x3c'
    MAIN_SCRIPT_HASH = [b'\x55']
    MAIN_PRIVATE_KEY = b'\xbc'
    TEST_PUBKEY_HASH = b'\x6f'
    TEST_SCRIPT_HASH = b'\xc4'
    TEST_PRIVATE_KEY = b'\xef'
    RPC_PORT = 5937

class Blackcoin(Coin):
    COIN_NAME = "Blackcoin"
    COIN_SHORT_NAME = "BLK"
    MAIN_PUBKEY_HASH = b'\x19'
    MAIN_SCRIPT_HASH = [b'\x55']
    MAIN_PRIVATE_KEY = b'\x99'
    RPC_PORT = 15715

class Komodo(Coin):
    COIN_NAME = "Komodo"
    COIN_SHORT_NAME = "KMD"
    MAIN_PUBKEY_HASH = b'\x3C'
    MAIN_SCRIPT_HASH = [b'\x55']
    MAIN_PRIVATE_KEY = b'\xbc'
    RPC_PORT = 7771
