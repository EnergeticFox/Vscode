import openpyxl
wb=openpyxl.load_workbook('excel-read.xlsx')
ws=wb.get_sheet_by_name('Sheet1')

for row in ws.rows:
    for cell in row:
        print(cell.value,end='\t')
    print()