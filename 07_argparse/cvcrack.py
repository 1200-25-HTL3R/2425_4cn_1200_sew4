#!/bin/python

import argparse
import os

from cryptscripts import caesar, vigenere

__author__ = "Benedikt Theuretzbchner"

parser = argparse.ArgumentParser(
    description="cvcrypt - Caesar & Vigenere encrypter / decrypter by Benedikt / HTL Rennweg"
)


def add_positional_args():
    parser.add_argument("infile", help="Zu verschlüsselnde Datei")


def add_options():
    parser.add_argument(
        "-c",
        "--cipher",
        type=str,
        choices=["caesar", "c", "vigenere", "v"],
        help="Zu verwendende Chiffre",
    )


def add_flags():
    output = parser.add_mutually_exclusive_group()
    output.add_argument("-v", "--verbose", action="store_true")
    output.add_argument("-q", "--quiet", action="store_true")


if __name__ == "__main__":
    add_positional_args()
    add_options()
    add_flags()

    args = parser.parse_args()

    if args.cipher and args.cipher == "vigenere" or args.cipher == "v":
        chipher = vigenere.Vigenere()
        method = "Vigenere"
    else:
        chipher = caesar.Caesar()
        method = "Caesar"

    try:
        with open(args.infile) as f:
            intext = f.read()
    except FileNotFoundError:
        print(args.infile + ":", os.strerror(2))
        exit(2)

    alphabet = "abcdefghijklmnopqrstuvwxyz"
    intext = "".join(filter(lambda ch: ch in alphabet, intext.lower()))

    if args.verbose:
        print(f"Cracking {method}-encrypted file {args.infile}: ")
    outtext = chipher.encrypt(intext)
