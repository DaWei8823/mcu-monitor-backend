#!/usr/bin/env python3

from mm_protocol import parse_client_header
import unittest

class TestMMProtocol(unittest.TestCase):

    def test_addition(self):
    
        header = bytearray([10,0,44,0,0,0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 6, 0])
        parsed = parse_client_header(header)

        self.assertEqual(parsed.length, 10)
        self.assertEqual(parsed.device_id, 44)
        self.assertEqual(parsed.nonce, 5)
        self.assertEqual(parsed.message_type, 6)

if __name__ == '__main__':
    unittest.main()


