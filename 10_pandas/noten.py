#!/bin/python

import argparse
import re
import pandas as pd

__author__ = "Benedikt Theuretzbachner"

parser: argparse.ArgumentParser = argparse.ArgumentParser(
    description="noten.py by Benedikt Theuretzbachner / HTL Rennweg"
)
args = None

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


def read_xml(filename: str) -> pd.DataFrame:
    """
    Parse xml file with student data

    :param filename: name of xml file

    :return: dataframe with student data
    """
    with open(filename) as f:
        content = f.read()

    result = []

    student_pattern = re.compile(r"<Schueler>.*?</Schueler>", flags=re.DOTALL)
    students = re.findall(student_pattern, content)

    student_data_pattern = re.compile(
        r"<(Nummer|Anrede|Vorname|Nachname|Geburtsdatum)>(.*)</\1>"
    )
    for s in students:
        student_data = map(lambda t: t[1], re.findall(student_data_pattern, s))
        result.append(student_data)

    df = pd.DataFrame(
        result,
        columns=["Nummer", "Anrede", "Vorname", "Nachname", "Geburtsdatum"],
        dtype=str,
    )

    return df


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

    args = parser.parse_args()
    join_col = "Nummer"
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
