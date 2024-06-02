# ASCII art
print("""
        __
       /'{>
   ____) (____
 //'--;   ;--'\\
///////\_/\\\\\\\
       m m       SOLOS CSVeditor
solos@tutamail.com
""")

import csv

input_file = input("Enter the location of the CSV file to open (e.g., /path/to/input_file.csv): ")

try:
    with open(input_file, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        headers = next(reader)
        data = list(reader)
except FileNotFoundError:
    print(f"File {input_file} not found. Please make sure the file name and location are correct.")
    exit()

print("Available columns in the CSV file:")
print(headers)

column_to_delete = input("Enter the name of the column to delete: ")

if column_to_delete not in headers:
    print(f"Column '{column_to_delete}' not found in the CSV file.")
    exit()

index_to_delete = headers.index(column_to_delete)

headers.pop(index_to_delete)
for row in data:
    row.pop(index_to_delete)

output_file = input("Enter the location to save the output CSV file (e.g., /path/to/output_file.csv): ")

with open(output_file, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(headers)
    writer.writerows(data)

print(f"Column '{column_to_delete}' has been deleted and the result is saved to {output_file}")
