# app.py

from flask import Flask, request, render_template, send_from_directory
import os
from scanner import SmartContractScanner
from report import AuditReport
from slither import SlitherAnalyzer

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'sol'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure 'uploads' and 'reports' directories exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs('reports', exist_ok=True)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def audit_contract(contract_path):
    # Scan the contract
    scanner = SmartContractScanner(contract_path)
    findings = scanner.run_all_checks()

    # Generate the report
    report = AuditReport(contract_path.split('/')[-1], findings)
    report_path = report.generate_pdf()

    return findings, report_path

def advanced_analysis(contract_path):
    # Advanced analysis using Slither
    slither_analyzer = SlitherAnalyzer(contract_path)
    advanced_findings = slither_analyzer.run_analysis()
    return advanced_findings


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        files = request.files.getlist("contract_files")  # This matches the form input name
        audit_results = []

        for file in files:
            if file and allowed_file(file.filename):
                filename = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
                file.save(filename)

                findings, report_path = audit_contract(filename)
                advanced_findings = advanced_analysis(filename)

                audit_results.append({
                    'contract': file.filename,
                    'findings': findings,
                    'advanced_findings': advanced_findings,
                    'report_path': report_path
                })

        return render_template("report.html", audit_results=audit_results)

    return render_template("index.html")

@app.route('/reports/<filename>')
def report(filename):
    return send_from_directory('reports', filename)


if __name__ == "__main__":
    app.run(debug=True)
