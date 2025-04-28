# Dark Web Monitoring and Smart Contract Auditing Tool

This project is a Flask-based web application for auditing Solidity smart contracts. It performs security audits and generates detailed reports based on the code quality and potential vulnerabilities of the smart contracts. The tool integrates with Slither for advanced analysis of Solidity code and provides downloadable PDF reports for each audit.

## Features

- **Contract Upload**: Users can upload Solidity (`.sol`) contract files for analysis.
- **Smart Contract Security Audits**: The system performs automated security checks using custom scanners and Slither.
- **Audit Report Generation**: Generates a detailed PDF report of the audit findings.
- **Slither Integration**: Perform advanced static analysis of Solidity contracts using Slither, detecting vulnerabilities like reentrancy, integer overflow, and other common issues.
- **Result Presentation**: Displays audit findings, including severity levels and detailed descriptions.



## File Structure

- `app.py`: Main Flask application file.

- `scanner.py`: Contains the SmartContractScanner class that runs basic checks on contracts.

- `slither.py`: Integrates Slither for advanced static analysis of Solidity contracts.

- `report.py`: Handles the generation of PDF audit reports.

- `templates/`: Contains the HTML templates used for rendering web pages.

- `uploads/`: Directory where uploaded contracts are stored.

- `reports/`: Directory where generated audit reports are saved.