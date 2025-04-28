# scanner.py

class SmartContractScanner:
    def __init__(self, contract_path):
        self.contract_path = contract_path
        self.findings = []

    def run_all_checks(self):
        # Simulate some security checks (you can integrate actual tools like Slither here)
        with open(self.contract_path, 'r') as file:
            contract_code = file.read()
            
            # Example checks (add real security checks here)
            self.check_reentrancy(contract_code)
            self.check_block_timestamp(contract_code)
            self.check_hardcoded_addresses(contract_code)
            self.check_unchecked_call_return(contract_code)
            self.check_integer_overflows(contract_code)
            self.check_visibility(contract_code)
            
            return self.findings

    def check_reentrancy(self, contract_code):
        if 'transfer' in contract_code or 'call.value' in contract_code:
            self.findings.append(("High", "Possible reentrancy vulnerability in transfer or call.value function"))

    def check_block_timestamp(self, contract_code):
        if 'block.timestamp' in contract_code or 'now' in contract_code:
            self.findings.append(("Medium", "Use of block.timestamp or now could lead to oracle manipulation"))

    def check_hardcoded_addresses(self, contract_code):
        if '0x' in contract_code:
            self.findings.append(("Low", "Hardcoded addresses found, consider using constants or configuration"))

    def check_unchecked_call_return(self, contract_code):
        if '.call(' in contract_code and 'require' not in contract_code and 'assert' not in contract_code:
            self.findings.append(("High", "Unchecked call return value, consider handling errors properly"))

    def check_integer_overflows(self, contract_code):
        if '++' in contract_code or '--' in contract_code:
            self.findings.append(("Medium", "Possible integer overflow/underflow, consider using SafeMath"))

    def check_visibility(self, contract_code):
        if 'function' in contract_code and 'public' not in contract_code and 'private' not in contract_code:
            self.findings.append(("Low", "Function visibility not explicitly declared, consider adding visibility modifiers"))

# Example usage
if __name__ == "__main__":
    scanner = SmartContractScanner("example_contract.sol")
    findings = scanner.run_all_checks()
    for severity, message in findings:
        print(f"[{severity}] {message}")