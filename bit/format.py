from coincurve import verify_signature as _vs

from bit.base58 import b58decode_check, b58encode_check
from bit.crypto import ripemd160_sha256
from bit.curve import x_to_y
from bit.network.coins import *

def verify_sig(signature, data, public_key):
    """Verifies some data was signed by the owner of a public key.

    :param signature: The signature to verify.
    :type signature: ``bytes``
    :param data: The data that was supposedly signed.
    :type data: ``bytes``
    :param public_key: The public key.
    :type public_key: ``bytes``
    :returns: ``True`` if all checks pass, ``False`` otherwise.
    """
    return _vs(signature, data, public_key)


def address_to_public_key_hash(address, coin=Bitcoin):
    # Raise ValueError if we cannot identify the address.
    get_version(address, coin=Bitcoin)
    return b58decode_check(address)[1:]


def get_version(address, coin=Bitcoin):
    version = b58decode_check(address)[:1]

    if version == coin.MAIN_PUBKEY_HASH:
        return 'main'
elif version == coin.TEST_PUBKEY_HASH:
        return 'test'
    else:
        raise ValueError('{} does not correspond to a mainnet nor '
                         'testnet address.'.format(version))


def bytes_to_wif(private_key, version='main', compressed=False, coin=Bitcoin):

    if version == 'test':
        prefix = coin.TEST_PRIVATE_KEY
    else:
        prefix = coin.MAIN_PRIVATE_KEY

    if compressed:
        suffix = coin.PRIVATE_KEY_COMPRESSED_PUBKEY
    else:
        suffix = b''

    private_key = prefix + private_key + suffix

    return b58encode_check(private_key)


def wif_to_bytes(wif, coin=Bitcoin):

    private_key = b58decode_check(wif)

    version = private_key[:1]

    if version == coin.MAIN_PRIVATE_KEY:
        version = 'main'
    elif version == coin.TEST_PRIVATE_KEY:
        version = 'test'
    else:
        raise ValueError('{} does not correspond to a mainnet nor '
                         'testnet address.'.format(version))

    # Remove version byte and, if present, compression flag.
    if len(wif) == 52 and private_key[-1] == 1:
        private_key, compressed = private_key[1:-1], True
    else:
        private_key, compressed = private_key[1:], False

    return private_key, compressed, version


def wif_checksum_check(wif, coin=Bitcoin):

    try:
        decoded = b58decode_check(wif)
    except ValueError:
        return False

    if decoded[:1] in (coin.MAIN_PRIVATE_KEY, coin.TEST_PRIVATE_KEY):
        return True

    return False


def public_key_to_address(public_key, version='main', coin=Bitcoin):

    if version == 'test':
        version = coin.TEST_PUBKEY_HASH
    else:
        version = coin.MAIN_PUBKEY_HASH

    length = len(public_key)

    if length not in (33, 65):
        raise ValueError('{} is an invalid length for a public key.'.format(length))

    return b58encode_check(version + ripemd160_sha256(public_key))


def public_key_to_coords(public_key):

    length = len(public_key)

    if length == 33:
        flag, x = int.from_bytes(public_key[:1], 'big'), int.from_bytes(public_key[1:], 'big')
        y = x_to_y(x, flag & 1)
    elif length == 65:
        x, y = int.from_bytes(public_key[1:33], 'big'), int.from_bytes(public_key[33:], 'big')
    else:
        raise ValueError('{} is an invalid length for a public key.'.format(length))

    return x, y


def coords_to_public_key(x, y, compressed=True, coin=Bitcoin):

    if compressed:
        y = coin.PUBLIC_KEY_COMPRESSED_ODD_Y if y & 1 else coin.PUBLIC_KEY_COMPRESSED_EVEN_Y
        return y + x.to_bytes(32, 'big')

    return coin.PUBLIC_KEY_UNCOMPRESSED + x.to_bytes(32, 'big') + y.to_bytes(32, 'big')


def point_to_public_key(point, compressed=True):
    return coords_to_public_key(point.x, point.y, compressed)
