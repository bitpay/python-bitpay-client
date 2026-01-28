import binascii
import hashlib
from typing import cast
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.backends import default_backend


def generate_pem():  # type: ignore
    private_key = ec.generate_private_key(ec.SECP256K1(), default_backend())
    pem = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.TraditionalOpenSSL,
        encryption_algorithm=serialization.NoEncryption(),
    )
    return pem.decode("utf-8")


def get_sin_from_pem(pem):  # type: ignore
    public_key = get_compressed_public_key_from_pem(pem)
    version = get_version_from_compressed_key(public_key)
    checksum = get_checksum_from_version(version)
    return base58encode(version + checksum)


def get_compressed_public_key_from_pem(pem):  # type: ignore
    private_key = cast(
        ec.EllipticCurvePrivateKey,
        serialization.load_pem_private_key(
            pem.encode(), password=None, backend=default_backend()
        ),
    )
    public_key = cast(ec.EllipticCurvePublicKey, private_key.public_key())
    public_numbers = public_key.public_numbers()
    # Convert to uncompressed format (x and y coordinates)
    x = public_numbers.x.to_bytes(32, byteorder="big")
    y = public_numbers.y.to_bytes(32, byteorder="big")
    vks = x + y
    bts = binascii.hexlify(vks)
    compressed = compress_key(bts)
    return compressed


def sign(message, pem):  # type: ignore
    message = message.encode()
    private_key = cast(
        ec.EllipticCurvePrivateKey,
        serialization.load_pem_private_key(
            pem.encode(), password=None, backend=default_backend()
        ),
    )
    signed = private_key.sign(message, ec.ECDSA(hashes.SHA256()))
    return binascii.hexlify(signed).decode()


def base58encode(hexastring):  # type: ignore
    chars = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"
    int_val = int(hexastring, 16)
    encoded = encode58("", int_val, chars)
    return encoded


def encode58(string, int_val, chars):  # type: ignore
    if int_val == 0:
        return string
    else:
        new_val, rem = divmod(int_val, 58)
        new_string = (chars[rem]) + string
        return encode58(new_string, new_val, chars)


def get_checksum_from_version(version):  # type: ignore
    return sha_digest(sha_digest(version))[0:8]


def get_version_from_compressed_key(key):  # type: ignore
    sh2 = sha_digest(key)
    rphash = hashlib.new("ripemd160")
    rphash.update(binascii.unhexlify(sh2))
    rp1 = rphash.hexdigest()
    return "0F02" + rp1


def sha_digest(hexastring):  # type: ignore
    return hashlib.sha256(binascii.unhexlify(hexastring)).hexdigest()


def compress_key(bts):  # type: ignore
    intval = int(bts, 16)
    prefix = find_prefix(intval)
    return prefix + bts[0:64].decode("utf-8")


def find_prefix(intval: int) -> str:
    if intval % 2 == 0:
        prefix = "02"
    else:
        prefix = "03"
    return prefix


def change_camel_case_to_snake_case(string: str) -> str:
    snake_case = "".join(
        ["_" + i.lower() if i.isupper() else i for i in string]
    ).lstrip("_")
    return snake_case
