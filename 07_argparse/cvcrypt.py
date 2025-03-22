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
    parser.add_argument("outfile", nargs="?", help="Zieldatei")


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

    action = parser.add_mutually_exclusive_group()
    action.add_argument("-d", "--decrypt", action="store_true")
    action.add_argument("-e", "--encrypt", action="store_true")


if __name__ == "__main__":
    add_positional_args()
    add_options()
    add_flags()
    parser.add_argument("-k", "--key", help="Encryption-Key")

    args = parser.parse_args()

    if args.key:
        key = args.key
    else:
        key = "a"

    if args.cipher and args.cipher == "vigenere" or args.cipher == "v":
        chipher = vigenere.Vigenere(key)
        method = "Vigenere"
    else:
        chipher = caesar.Caesar(key)
        method = "Caesar"

    try:
        with open(args.infile) as f:
            intext = f.read()
    except FileNotFoundError:
        print(args.infile + ":", os.strerror(2))
        exit(2)

    alphabet = "abcdefghijklmnopqrstuvwxyz"
    intext = "".join(filter(lambda ch: ch in alphabet, intext.lower()))

    if args.outfile:
        output_dest = "file " + args.outfile
    else:
        output_dest = "standard output"

    if args.decrypt:
        if args.verbose:
            print(
                f"Decrypting {method} with key = {key} from file {args.infile} into {output_dest}"
            )

        outtext = chipher.decrypt(intext)
    else:
        if args.verbose:
            print(
                f"Encrypting {method} with key = {key} from file {args.infile} into {output_dest}\n"
            )
        outtext = chipher.encrypt(intext)

    if args.outfile:
        try:
            with open(args.outfile, "w") as f:
                f.write(outtext)
        except FileNotFoundError:
            print(args.infile + ":", os.strerror(2))
            exit(2)
    else:
        print(outtext)
