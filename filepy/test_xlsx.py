import xlsxwriter
from datetime import datetime

expenses = (
    ['2013-01-13', 1000],
    ['2013-01-14',  100],
    ['2013-01-16',  300],
    [ '2013-01-20',   50],
)

# Create a workbook and add a worksheet.
workbook = xlsxwriter.Workbook('.//test_xls//Expenses03.xlsx')
worksheet = workbook.add_worksheet('test')

# Add an Excel date format.
date_format = workbook.add_format({'num_format': 'yyyy-mm-dd'})

# Add a bold format to use to highlight cells.
bold = workbook.add_format({'bold': 1})

# Adjust the column width.
worksheet.set_column(0, 0, 15)

# Start from the first cell below the headers.
row = 1
col = 0

# Write some data headers.
worksheet.write('A1', '日期', bold)
worksheet.write('B1', '数量', bold)

for date_str, cost in expenses:
    # Convert the date string into a datetime object.
    date = datetime.strptime(date_str, "%Y-%m-%d")
    worksheet.write_datetime(row, col, date, date_format)
    worksheet.write_number(row, col + 1, cost)
    row += 1

workbook.close()