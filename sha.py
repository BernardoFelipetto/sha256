import os
import sys
import hashlib

VIDEO_FILE_PATH = sys.argv[1]
MATCHING_HASH = sys.argv[2]
#matching hash should be 8e423302209494d266a7ab7e1a58ca8502c9bfdaa31dfba70aa8805d20c087bd for video 5

if not len(sys.argv) >= 3:
    print("wrong number of arguments")
    sys.exit(1)


file_size = os.path.getsize(VIDEO_FILE_PATH)
videolist = list()
checksum = b''


with open(VIDEO_FILE_PATH, "rb") as handle:
    video_file_bytes = handle.read(1024)
    videolist.append(video_file_bytes)

    while video_file_bytes:
        video_file_bytes = handle.read(1024)
        videolist.append(video_file_bytes)

for i in reversed(videolist):
    byte_block = i
    uncoded_bytes = hashlib.sha256()
    uncoded_bytes.update(byte_block + checksum)
    checksum = uncoded_bytes.digest()


print(checksum.hex())



