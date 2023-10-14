"""
Given is the file products.csv with three fields
productid,name,date


Read the lines and try to parse the field date 
into a Python file object (datetime.strptime).
Some date fields are either empty or broken, but the program must
not abort the conversion, but ignore these lines.

The date must be shifted forward by two days, i.e. from the
18.10.2022 should become the 20.10.2022. The new date replaces the old date
in the list in the same format (datetime, timedelta).

The changed list should then be output to Standard-Out, saving as a
CSV is not necessary (additional task.)

Encapsulate the individual areas in functions, use typehints and 
docstrings where necessary.
"""

import csv
from pathlib import Path
from datetime import datetime, timedelta

FILENAME: str = "products.csv"

def fn(file: str) -> list[list[str]]:
    """
    Reads a CSV file and returns its content as a nested list of strings.

    Args:
        file (str): The name of the CSV file to read.

    Returns:
        list[list[str]]: A nested list containing the rows and columns of the CSV file.
    """
    with open(Path(__file__).parent / file) as f:
        reader = csv.reader(f, delimiter=",")
        next(reader)
        lst: list[list[str]] = []
        for row in reader:
            lst.append(row)
    return lst

def fn1(lst: list[list[str]]) -> list[str]:
    """
    Converts dates in a given nested list from "%d/%m/%Y" format to "%d/%m/%Y" format + 2 days,
     and returns them as a simple string.

    Args:
        lst (list[list[str]]): The input nested list containing dates in "%d/%m/%Y" format.

    Returns:
        List of strings representing dates converted from "%d/%m/%Y" format
        to "%d/%m%Y" + 2 days.
     """
     
    result: list[str] = []
     
    for row in lst:
        try:
            dateobj = datetime.strptime(row[2], "%d/%m/%Y")
            dateobj += timedelta(days=2)
            datestr = dateobj.strftime("%d/%m/%Y")
            row[2] = datestr
            result.append(row)
        except:
            pass
     
    return result

def main(file: str) -> list[str]:
    """
    Main function that reads a CSV file, converts its dates into new string formats,
    and returns them as a list of strings.

    Args:
        file (str): The name of the CSV file to read.

    Returns:
        List of strings representing dates converted from "%d/%m/%Y" format to "%d/%m%Y" + 2 days.
    """
   
    list_csv = fn(file)
    result_list = fn1(list_csv)
    return result_list

print(main(FILENAME))





