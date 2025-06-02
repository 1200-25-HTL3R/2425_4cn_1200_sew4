#!/bin/python

import argparse
import os
import re
import sys
import pandas as pd

__author__ = "Benedikt Theuretzbachner"

parser: argparse.ArgumentParser = argparse.ArgumentParser(
    description="noten.py by Benedikt Theuretzbachner / HTL Rennweg"
)

df_grades = pd.DataFrame()
df_students = pd.DataFrame()
df_joined = pd.DataFrame()


def add_args() -> None:
    """
    Add arguments for argument parser
    """
    parser.add_argument("outfile", help="Ausgabedatei (z.B. result.csv)")

    parser.add_argument("-n", required=True, help="csv-Datei mit den Noten")
    parser.add_argument("-s", required=True, help="xml-Datei mit den Schülerdaten")
    parser.add_argument(
        "-m", help="Name der Spalte, die zu verknüpfen ist (default = Nummer)"
    )
    parser.add_argument("-f", help="Name des zu filternden Gegenstandes (z.B. SEW)")

    output = parser.add_mutually_exclusive_group()
    output.add_argument(
        "-v", "--verbose", action="store_true", help="Gibt die Daten Kommandozeile aus"
    )
    output.add_argument("-q", "--quiet", action="store_true", help="keine Textausgabe")


def check_file(filename: str) -> None:
    """
    Check if a file exists.

    :param filename: Path to file
    """
    if not os.path.exists(filename):
        print(f"{os.strerror(2)}: {filename}\n", file=sys.stderr)
        exit(2)


def read_xml(filename: str) -> pd.DataFrame:
    """
    Parse xml file with student data

    :param filename: name of xml file

    :return: dataframe with student data
    """
    with open(filename) as f:
        content = f.read()

    result: list = []

    student_pattern: re.Pattern = re.compile(
        r"<Schueler>.*?</Schueler>", flags=re.DOTALL
    )
    students: list = re.findall(student_pattern, content)

    student_data_pattern: re.Pattern = re.compile(
        r"<(Nummer|Anrede|Vorname|Nachname|Geburtsdatum)>(.*)</\1>"
    )
    for s in students:
        student_data = map(lambda match: match[1], re.findall(student_data_pattern, s))
        result.append(student_data)

    return pd.DataFrame(
        result,
        columns=["Nummer", "Anrede", "Vorname", "Nachname", "Geburtsdatum"],
        dtype=str,
    )


def filter_df(filter: set) -> None:
    """
    Filter a DataFrame. Only keep columns in filter set.

    :param filter: set with columns to keep
    """
    for col in df_grades.columns:
        if col not in filter:
            df_grades.drop(columns=[col], inplace=True)


def write_output(filename: str) -> None:
    """
    Write DataFrame to csv file.

    :param filename: output filename
    """
    df_joined.to_csv(filename)


if __name__ == "__main__":
    """
    Main logic of this script. Parse Arguments and merge DataFrames.
    """
    add_args()

    args: argparse.Namespace = parser.parse_args()
    check_file(args.n)
    check_file(args.s)
    join_col: str = "Nummer"
    if args.m:
        join_col = args.m

    if args.verbose:
        print(f"csv-Datei mit den Noten: {args.n}")
        print(f"csv-Datei mit den Schülerdaten: {args.n}")
        print(f"Name der Spalte, die zu verknüpfen ist: {join_col}")

    df_grades = pd.read_csv(args.n, sep=";").astype(str)
    df_grades.set_index(join_col, inplace=True)
    if args.f:
        filter: set = set(str(args.f).split(","))
        filter_df(filter)

    df_students = read_xml(args.s).astype(str)
    df_students.set_index(join_col, inplace=True)

    df_joined = df_students.join(df_grades)

    if not args.quiet:
        print(f"Output-Datei: {args.outfile}\n")
    write_output(args.outfile)
