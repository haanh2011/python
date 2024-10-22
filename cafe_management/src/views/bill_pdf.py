import pandas as pd
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph

# Register a font that supports Unicode/Vietnamese
pdfmetrics.registerFont(TTFont('arial', 'C:/Users/AnhHa/PycharmProjects/cafe_management/src/fonts/arial_font/arial.ttf'))

# Function to create receipt PDF from pandas DataFrame
def create_receipt_pdf(filename, df):
    # Set POS receipt size (80mm wide)
    width = 80 * 2.83465  # 80mm to points
    height = 300  # Approx height, can adjust based on content

    # Create the PDF document with custom page size
    pdf = SimpleDocTemplate(filename, pagesize=(width, height))
    elements = []

    # Custom paragraph style using the registered font
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name='CustomTitle', fontName='arial', fontSize=10, leading=12))
    styles.add(ParagraphStyle(name='CustomNormal', fontName='arial', fontSize=9))

    # Add receipt header
    header_data = [
        ["CÀ PHÊ HOÀNG PHÚC"],
        ["Đường Số 24 KDC An Khánh, P. An Khánh, Q. Ninh Kiều - TP. Cần Thơ"],
        ["ĐT: 0974.300.007 - 0909.191.195"],
        ["HÓA ĐƠN BÁN HÀNG"],
        ["Bàn 05      Số: 021900003"],
        ["Ngày: 18/02/2019       Thu ngân: Administrator"],
        ["Giờ vào: 01:41           Giờ ra: 01:41"],
    ]

    for line in header_data:
        elements.append(Paragraph(line[0], styles['CustomTitle']))

    # Convert DataFrame to list of lists for the table
    table_data = [['Mặt hàng', 'SL', 'Giá', 'T.tiền']]  # Table headers

    # Loop through DataFrame rows and add each row to the table_data
    for index, row in df.iterrows():
        item = row['Mặt hàng']
        sl = row['SL']
        price = f"{row['Giá']:,}"  # Format price with commas
        total = f"{row['T.tiền']:,}"
        table_data.append([item, str(sl), price, total])

    # Calculate total amount and append to the table
    total_amount = f"{df['T.tiền'].sum():,}"
    table_data.append(['', '', 'Tổng:', total_amount])

    # Create a table with style
    table = Table(table_data)
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, -1), 'arial'),
        ('FONTSIZE', (0, 0), (-1, -1), 9),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 8),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ]))

    # Add table to elements
    elements.append(table)

    # Footer text
    elements.append(Paragraph("Cảm ơn Quý khách. Hẹn gặp lại!", styles['CustomNormal']))

    # Build the PDF
    pdf.build(elements)

# Example DataFrame
data = {
    'Mặt hàng': ['Cà phê đá', 'Bún thịt Xào', 'Cà phê sữa đá', 'Cơm tấm'],
    'SL': [1, 1, 1, 1],
    'Giá': [10000, 15000, 12000, 17000],
    'T.tiền': [10000, 15000, 12000, 17000]
}

df = pd.DataFrame(data)

# Create the receipt PDF with custom size
create_receipt_pdf("receipt_from_dataframe.pdf", df)
