#!/usr/bin/env python

import sys

from mp.mpfshell import main, MpFileShell
from typing import Iterable, Tuple, List
from serial.tools.list_ports import comports

def find_devices(ids: List[Tuple[int, int]]) -> Iterable[str]:
    for port in comports():
        print(hex(port.vid), hex(port.pid), ids)
        if (port.vid, port.pid) in ids:
            yield port.device

try:
    mpfs = MpFileShell(True, True, False, True)

    ids = [(0x0403, 0x6001)]
    devs = find_devices(ids)
    flag = False
    dev = None
    for device in devs:
        flag = True
        print(device)
        dev = device
    if dev:
        mpfs.do_open(dev)
        mpfs.do_put('config.json')
        mpfs.do_close(None)
        print("Transmission complete")
except Exception as e:
    sys.stderr.write(str(e) + "\n")
    exit(1)
