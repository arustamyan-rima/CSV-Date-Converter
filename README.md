# CSV_Date_Converter

This project involves reading a CSV file named 'products.csv' that contains three fields: productid, name, and date. The program reads the lines and parses the 'date' field into a Python datetime object (using datetime.strptime). It handles cases where some date fields are either empty or broken by ignoring these lines.

The program shifts the date forward by two days. For example, the date '18.10.2022' becomes '20.10.2022'. The new date replaces the old date in the list in the same format (datetime, timedelta).

The changed list is then output to Standard-Out, and saving as a CSV is considered an additional task.

### Project Structure

- The main script is named `products.py`.
- The CSV file to be processed is named `products.csv`.
- The script contains three functions encapsulating different functionalities.

### Usage

Ensure you have the necessary libraries installed to run the code. You can run the script using Python:

python csv_date_converter.py

The converted dates will be printed on the standard output.

### Functions
fn: Reads a CSV file and returns its content as a nested list of strings.  
fn1: Converts dates from "%d/%m/%Y" format to "%d/%m/%Y" format + 2 days and returns them as a simple string.  
main: Main function that reads a CSV file, converts its dates into new string formats, and returns them as a list of strings.
