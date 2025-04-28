# cli.py
import sys
import os
from scanner import SmartContractScanner
from report import AuditReport
from slither import SlitherAnalyzer

def audit_contract(contract_path):
    # Run basic checks
    scanner = SmartContractScanner(contract_path)
    findings = scanner.run_all_checks()

    # Run Slither advanced analysis
    slither_analyzer = SlitherAnalyzer(contract_path)
    advanced_findings = slither_analyzer.run_analysis()

    # Merge findings if you want
    all_findings = findings + advanced_findings

    # Generate audit report
    report = AuditReport(contract_path.split('/')[-1], all_findings)
    report_path = report.generate_pdf()

    return findings, advanced_findings, report_path

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python cli.py <contract_path>")
        sys.exit(1)

    contract_path = sys.argv[1]
    if not os.path.isfile(contract_path):
        print(f"Error: {contract_path} not found.")
        sys.exit(1)

    findings, advanced_findings, report_path = audit_contract(contract_path)

    print(f"Findings for {contract_path}:")
    for finding in findings:
        print(f"Basic: {finding}")
    
    for advanced_finding in advanced_findings:
        print(f"Slither: {advanced_finding}")

    print(f"\nAudit report saved to: {report_path}")
