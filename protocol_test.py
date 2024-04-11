#!/usr/bin/env python3

import mm_protocol as proto
import unittest


class TestMMProtocol(unittest.TestCase):

    def test_parse_header(self):

        header = bytearray(
            [10, 0, 44, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 6, 0]
        )
        parsed = proto.parse_client_header(header)

        self.assertEqual(parsed.length, 10)
        self.assertEqual(parsed.device_id, 44)
        self.assertEqual(parsed.nonce, 5)
        self.assertEqual(parsed.message_type, 6)

    def test_parse_hello_msg_content(self):
        content = bytearray([5, 0])
        msg = proto.parse_message_content(proto.MESSAGE_TYPE_HELLO, content)
        self.assertEqual(msg.protocol_version, 5)


if __name__ == "__main__":
    unittest.main()
