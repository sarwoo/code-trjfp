from fpdf import FPDF

class PDF(FPDF):
    # Extend the header
    def header(self):
        # logo
        self.image('assets/banner-report.png', 0, 0, 210)
        # font
        self.set_font('helvetica', 'B', 20)
        # Padding
        self.ln(28)
        self.cell(56)
        # title
        
        self.cell(0, 10, 'September 2021', border=False, ln=1, align='L')
        # line break
        self.ln(15)

    # Extend the footer
    def footer(self):
        # set the poition of the footer
        self.set_y(-15)
        # set font
        self.set_font('helvetica', 'I', 10)
        # Page number
        self.cell(0, 10, f'Page {self.page_no()} of {{nb}}', align='C')

# Create FPDF object
pdf = PDF('P', 'mm', 'A4')

# get total page numbers
pdf.alias_nb_pages()

# Set auto page break
pdf.set_auto_page_break(auto=True, margin=15)

# Add a page
pdf.add_page()

# Add text
pdf.set_font('times', '', 12)

for i in range(1, 5):
    pdf.cell(0, 10, f'This is line {i} :)', ln=True)

pdf.output('output/report.pdf')