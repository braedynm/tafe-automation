# Title: Wk8 Task 1 - Port Scanner
# Author: Braedyn Murtagh (braedynm)
# Date: 2023-03-22
#
# Asks the user for an IP address, and a set of ports.
# Scans through those ports.

import ipaddress
import socket
import threading


def getIP():
    while True:
        try:
            ip = ipaddress.ip_address(input("Enter an IP Address: "))
            return ip
        except ValueError:
            print("Invalid IP Address.")


def collapse(arr):
    s = set()
    for v in arr:
        if isinstance(v, range):
            for n in v:
                s.add(n)
        elif isinstance(v, int):
            s.add(v)
    l = list(s)
    l.sort()
    return l


def getPorts():
    while True:
        ports = input("Input target ports (1-1024): ").strip()
        if len(ports) == 0:
            return collapse([range(1, 1025)])
        a = ports.replace(" ", "").split(",")
        results = []
        fail = False
        for item in a:
            c = len(item.split("-"))
            if c == 1:
                if not item.isnumeric():
                    print(f"Invalid Value for {item}")
                    fail = True
                    break
                else:
                    results.append(int(item))
            elif c == 2:
                left, right = item.split("-")
                if len(left) == 0:
                    left = "0"
                if len(right) == 0:
                    right = "65535"
                if not (left.isnumeric() and right.isnumeric()):
                    print(f"Invalid Value for {left}-{right}")
                    fail = True
                    break
                else:
                    results.append(range(int(left), int(right)+1))
            else:
                print(f"Invalid value for {item}")
                fail = True
                break
        if fail is True:
            continue
        else:
            return collapse(results)


def scan_one(target, port, found):
    while True:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            status = sock.connect_ex((str(target), port))
            sock.close()
            if status == 0:
                print(f"Found open port {port}")
                found.append(port)
            return
        except OSError:
            # print(f"Retry for port {port}")
            pass


def scan(target, ports):
    found = []
    for port in ports:
        thread = threading.Thread(
            target=scan_one, args=(target, port, found))
        thread.start()
    for thread in threading.enumerate():
        if thread != threading.current_thread():
            thread.join()
    print(f"Found {len(found)}/{len(ports)} open ports.")
    print(found)


scan(getIP(), getPorts())
