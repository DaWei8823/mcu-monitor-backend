#!/usr/bin/env python3

from mm_protocol import *

header = bytearray([10,0,44,0,0,0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 6, 0])

parsed = parse_client_header(header)

print(parsed)

assert(parsed.length == 10)
assert(parsed.device_id == 44)
assert(parsed.nonce == 5)
assert(parsed.message_type == 6)

print("good")
