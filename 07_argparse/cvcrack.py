#!/bin/python

import argparse
import os

from cryptscripts import caesar, kasiski

__author__ = "Benedikt Theuretzbchner"

parser = argparse.ArgumentParser(
    description="cvcrypt - Caesar & Vigenere encrypter / decrypter by Benedikt / HTL Rennweg"
)


def add_positional_args():
    """
    Add positional arguments to argument parser.
    """
    parser.add_argument("infile", help="Zu verschlüsselnde Datei")


def add_options():
    """
    Add options to argument parser.
    """
    parser.add_argument(
        "-c",
        "--cipher",
        type=str,
        choices=["caesar", "c", "vigenere", "v"],
        help="Zu verwendende Chiffre",
    )


def add_flags():
    """
    Add flags to argument parser.
    """
    output = parser.add_mutually_exclusive_group()
    output.add_argument("-v", "--verbose", action="store_true")
    output.add_argument("-q", "--quiet", action="store_true")


def main():
    """
    Crack key for input file according to the arguments specified by the user.
    """
    add_positional_args()
    add_options()
    add_flags()

    args = parser.parse_args()

    try:
        with open(args.infile) as f:
            intext: str = f.read()
    except FileNotFoundError:
        print(args.infile + ":", os.strerror(2))
        exit(2)

    if args.cipher and args.cipher == "vigenere" or args.cipher == "v":
        kasiski_obj = kasiski.Kasiski(intext)
        method = "Vigenere"

        if args.verbose:
            print(f"Cracking {method}-encrypted file {args.infile}: Key = ", end="")
        key = kasiski_obj.crack(6)
    else:
        caesar_obj = caesar.Caesar()
        method = "Caesar"

        if args.verbose:
            print(f"Cracking {method}-encrypted file {args.infile}: Key = ", end="")
        key: str = caesar_obj.crack(intext)[0]

    print(key + "\n")


if __name__ == "__main__":
    main()
