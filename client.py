#!/usr/bin/env python3

import math
import os
import socket

import numpy as np

names = ['zya_0', 'zya_1', 'zya_2', 'zya_3', 'zya_4', 'zya_5']

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)  # UDP

# Enable port reusage so we will be able to run multiple clients and servers on single (host, port).
# Do not use socket.SO_REUSEADDR except you using linux(kernel<3.9): goto https://stackoverflow.com/questions/14388706/how-do-so-reuseaddr-and-so-reuseport-differ for more information.
# For linux hosts all sockets that want to share the same address and port combination must belong to processes that share the same effective user ID!
# So, on linux(kernel>=3.9) you have to run multiple servers and clients under one user to share the same (host, port).
# Thanks to @stevenreddie
client.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)

# Enable broadcasting mode
client.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

client.bind(("", 37021))
data, addr = client.recvfrom(128)
# print("message received")
# assert len(message) == 2*7*len(names)
data = np.frombuffer(data[:-4], np.int16).reshape(-1, 7)
for i, data in enumerate(data):
    _x, _y, _z, x, y, z, w = data.tolist()
    # norm = math.sqrt(x*x+y*y+z*z+w*w)
    # print(x, y, z, w)
    print(f"'{names[i]}': [{_x/1000:6.3f}, {_y/1000:6.3f}, {_z/1000:6.3f}],")
