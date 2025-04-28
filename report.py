# report.py

from fpdf import FPDF
import os

class AuditReport:
    def __init__(self, contract_name, findings):
        self.contract_name = contract_name
        self.findings = findings
        self.report_filename = f"reports/{contract_name.split('.')[0]}_audit_report.pdf"

    def generate_pdf(self):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)

        pdf.cell(200, 10, txt=f"Audit Report for {self.contract_name}", ln=True, align="C")
        pdf.ln(10)

        if not self.findings:
            pdf.cell(200, 10, txt="No vulnerabilities detected!", ln=True, align="L")
        else:
            for severity, description in self.findings:
                pdf.cell(200, 10, txt=f"{severity}: {description}", ln=True, align="L")
        
        pdf.output(self.report_filename)
        return self.report_filename
