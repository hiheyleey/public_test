import snap7
from snap7.util import *
import struct

client = snap7.client.Client()
client.connect("192.168.1.16", 0, 0, 102)
client.get_connected()

data = client.mb_read(140, 40)
print(data)

# 0x41: 65 -> 0x0a : 10, 0x40
data = bytearray(b'\x00\x01\x00\x00\x00\x41\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')


data = client.mb_write(140, 40, data)
print(data)


