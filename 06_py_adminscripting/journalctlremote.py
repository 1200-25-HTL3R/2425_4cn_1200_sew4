#!/bin/python

import paramiko

__author__ = "Benedikt theuretzbachner"


minutes = input("How many minutes should the journalctl logs reach back?\nminutes> ")
minutes = minutes.strip()
if not minutes.isdigit():
    raise Exception("minutes must only contain digits (0-9)")

username = "juniorcisco"
keyfile = r"/home/benedikt/.ssh/id_gmail"
priv_key = paramiko.Ed25519Key.from_private_key_file(keyfile)
client = paramiko.SSHClient()

client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect("192.168.11.137", username=username, pkey=priv_key)
_, stdout, stderr = client.exec_command(f"journalctl --since -{minutes}m")

err = stderr.read()
if err:
    print()
    print("STDERR:")
    print()
    print(err.decode())

out = stdout.read()
if out:
    print()
    print("STDOUT:")
    print()
    print(out.decode())

client.close()
