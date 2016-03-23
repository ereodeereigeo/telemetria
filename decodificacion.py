import struct
import codecs

def uint32(dato_inv):
    return struct.unpack('!I', codecs.decode(dato_inv, 'hex'))[0]


def uint8(dato_inv):
    return struct.unpack('!B', codecs.decode(dato_inv, 'hex'))[0]


def uint16(dato_inv):
    return struct.unpack('!H', codecs.decode(dato_inv, 'hex'))[0]


def float32(dato_inv):
    return struct.unpack('!f', codecs.decode(dato_inv, 'hex'))[0]


def int8(dato_inv):
    return struct.unpack('!b', codecs.decode(dato_inv, 'hex'))[0]


def int32(dato_inv):
    return struct.unpack('!i', codecs.decode(dato_inv, 'hex'))[0]


def int16(dato_inv):
    return struct.unpack('!h', codecs.decode(dato_inv, 'hex'))[0]


def data_u32(dato_inv):
    return struct.unpack('!L', codecs.decode(dato_inv, 'hex'))[0]


def data_32(dato_inv):
    return (struct.unpack('!l', codecs.decode(dato_inv, 'hex'))[0])