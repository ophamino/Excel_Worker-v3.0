import xlrd

def read_excel_file(file_path):
    workbook = xlrd.open_workbook(file_path)

    data = {}

    for sheet_name in workbook.sheet_names():
        sheet = workbook.sheet_by_name(sheet_name)
        cell_o5 = sheet.cell_value(4, 14)  # O5
        cell_f13 = sheet.cell_value(12, 5)  # F13
        data[cell_o5] = cell_f13
    return data


read_excel_file("..\\222.xls")