# -- coding: utf-8 --
# 使用PYPDF2==2.0.0 (3.0.0版本語法更改，需再重新調整)
from PyPDF2 import PdfReader, PdfWriter
import openpyxl
def split_single_pdf(read_file, start_page, end_page, pdf_file):
    # 1. 获取原始pdf文件
    fp_read_file = open(read_file, 'rb')
    # 2. 将要分割的PDF内容格式化
    pdf_input = PdfReader(fp_read_file)
    # 3. 实例一个 PDF文件编写器
    pdf_output = PdfWriter()
    # 4. 把67到78页放到PDF文件编写器
    for i in range(start_page, end_page):
        pdf_output.addPage(pdf_input.getPage(i))
    # 5. PDF文件输出
    with open(pdf_file, 'wb') as pdf_out:
        pdf_output.write(pdf_out)
    print(f'{read_file}分割{start_page}页-{end_page}页完成，保存为{pdf_file}!')

data=[0,0,'a']
if __name__ == '__main__':
    
    wb=openpyxl.load_workbook('excel-read.xlsx')
    ws=wb.get_sheet_by_name('Sheet1')

    for row in ws.rows:
        s=0
        for cell in row:
            data[s]=cell.value
            s+=1   
        # 待切分文件文件名
        in_pdf_name = "3.pdf"
        # 切分后文件文件名
        out_pdf_name = str(data[2])+'.pdf'
        # 切分开始页面
        start = data[0]
        # 切分结束页面
        end = data[1]
        split_single_pdf(in_pdf_name, start, end, out_pdf_name)


# print(int(data[0]))
