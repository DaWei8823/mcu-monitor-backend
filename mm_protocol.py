from dataclasses import dataclass


@dataclass
class ClientHeader:
    length: int
    device_id: int
    nonce: int
    message_type: int


HEADER_TOTAL_LENGTH = 18

HEADER_LENGTH_FIELD_START = 0
HEADER_LENGTH_FIELD_SIZE = 2
HEADER_LENGTH_FIELD_END = HEADER_LENGTH_FIELD_START + HEADER_LENGTH_FIELD_SIZE

HEADER_DEVICE_ID_FIELD_START = HEADER_LENGTH_FIELD_END
HEADER_DEVICE_ID_FIELD_SIZE = 8
HEADER_DEVICE_ID_FIELD_END = HEADER_DEVICE_ID_FIELD_START + HEADER_DEVICE_ID_FIELD_SIZE

HEADER_NONCE_FIELD_START = HEADER_DEVICE_ID_FIELD_END
HEADER_NONCE_FIELD_SIZE = 8
HEADER_NONCE_FIELD_END = HEADER_NONCE_FIELD_START + HEADER_NONCE_FIELD_SIZE

HEADER_MESSAGE_TYPE_FIELD_START = HEADER_NONCE_FIELD_END
HEADER_MESSAGE_TYPE_FIELD_SIZE = 2
HEADER_MESSAGE_TYPE_FIELD_END = (
    HEADER_MESSAGE_TYPE_FIELD_START + HEADER_MESSAGE_TYPE_FIELD_SIZE
)


def parse_client_header(raw: bytearray):
    if len(raw) < HEADER_TOTAL_LENGTH:
        raise ValueError(
            f"expcted header of length {HEADER_TOTAL_LENGTH} bytes instead got {len(raw)} bytes"
        )

    length_slice = raw[HEADER_LENGTH_FIELD_START:HEADER_LENGTH_FIELD_END]
    length = int.from_bytes(length_slice, byteorder="little")

    device_id_slice = raw[HEADER_DEVICE_ID_FIELD_START:HEADER_DEVICE_ID_FIELD_END]
    device_id = int.from_bytes(device_id_slice, byteorder="little")

    nonce_slice = raw[HEADER_NONCE_FIELD_START:HEADER_NONCE_FIELD_END]
    nonce = int.from_bytes(nonce_slice, byteorder="little")

    message_type_slice = raw[
        HEADER_MESSAGE_TYPE_FIELD_START:HEADER_MESSAGE_TYPE_FIELD_END
    ]
    message_type = int.from_bytes(message_type_slice, byteorder="little")

    return ClientHeader(length, device_id, nonce, message_type)
