
def fill_a_row_to_sheet(sheet, contents, row, col=1):
    for content in list(enumerate(contents.split(','), start=0)):
        sheet.Cells(row, content[0] + col).Value = content[1]


def fill_a_cell_to_sheet(sheet, content, row, col):
    sheet.Cells(row, col).Value = content


def rgb_to_hex(rgb):
    """
    Excel에서 선의 색을 변경하기 위해 사용
    """
    return int('%02x%02x%02x' % rgb, 16)