import os
import sys
import hashlib

if len(sys.argv) < 3:
    print("Usage: sha.py <file> <expected h0 sha256>")
    sys.exit(1)

VIDEO_FILE_PATH = sys.argv[1]
EXPECTED_H0 = sys.argv[2]

block_size = 1024
blocks = []

with open(VIDEO_FILE_PATH, "rb") as handle:
    block = handle.read(block_size)
    while block:
        blocks.append(block)
        block = handle.read(block_size)

h0 = b''
for block in reversed(blocks):
    h0 = hashlib.sha256(block + h0).digest()

hex_h0 = h0.hex()

if hex_h0 == EXPECTED_H0:
    print("Hashes do match.")
    print("Expected:   {}".format(EXPECTED_H0))
    print("Calculated: {}".format(hex_h0))
    sys.exit(0)
else:
    print("Hashes do not match.")
    print("Expected:   {}".format(EXPECTED_H0))
    print("Calculated: {}".format(hex_h0))
    sys.exit(1)
