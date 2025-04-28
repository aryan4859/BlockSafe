import subprocess

class SlitherAnalyzer:
    def __init__(self, contract_path):
        self.contract_path = contract_path

    def run_analysis(self):
        """Runs Slither analysis on the given contract and returns findings."""
        try:
            # Run Slither command
            result = subprocess.run(
                ['slither', self.contract_path],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True  # auto-decode utf-8
            )

            # Combine stdout and stderr
            output = result.stdout + "\n" + result.stderr
            findings = self.parse_slither_output(output)
            return findings
        
        except Exception as e:
            return [{'severity': 'Error', 'description': f'Exception running Slither: {str(e)}'}]

    def parse_slither_output(self, output):
        """Parses Slither output and returns a list of findings."""
        findings = []
        lines = output.splitlines()
        
        for line in lines:
            line = line.strip()
            if line.startswith("INFO:") or line.startswith("WARNING:") or line.startswith("ERROR:") or line.startswith("VULNERABILITY:"):
                if "WARNING:" in line:
                    severity = "Medium"
                elif "ERROR:" in line or "VULNERABILITY:" in line:
                    severity = "High"
                else:
                    severity = "Low"

                findings.append({'severity': severity, 'description': line})
        
        return findings
