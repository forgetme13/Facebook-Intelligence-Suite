from fpdf import FPDF

def generate_pdf_report(profile, filename):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    pdf.cell(200, 10, txt="Laporan Intelijen Target", ln=True, align='C')
    pdf.ln(10)
    for key, val in profile.items():
        pdf.cell(200, 10, txt=f"{key}: {val}", ln=True)
    pdf.output(filename)

