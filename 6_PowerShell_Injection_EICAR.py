#!/usr/bin/env python3

# Memory-based AV test using PowerShell injection (advanced). 
# Use Python to spawn a PowerShell command that generates the EICAR string in memory. This more closely mimics malware droppers used in red teaming.
# This variant avoids writing to disk. AV/EDR with script and memory inspection will often catch it.

#!/usr/bin/env python3

import subprocess

# PowerShell command to simulate EICAR string in memory only (no file writes)
powershell_cmd = '''
$e="X5O!P%@AP[4\\PZX54(P^)7CC)7}$EICAR-STANDARD-ANTIVIRUS-TEST-FILE!$H+H*"
[System.Text.Encoding]::ASCII.GetBytes($e) | Out-Null
Write-Output "MEMORY_EICAR_TEST_EXECUTED"
'''

# Run PowerShell with subprocess and capture all output
result = subprocess.run(
    ["powershell", "-Command", powershell_cmd],
    shell=True,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    text=True
)

# Output detection
print("=== STDOUT ===")
print(result.stdout.strip())

print("=== STDERR ===")
print(result.stderr.strip())

# Success or failure check
if result.returncode == 0:
    print("[+] PowerShell executed without error.")
    if "MEMORY_EICAR_TEST_EXECUTED" in result.stdout:
        print("[+] Payload executed successfully in memory.")
    else:
        print("[-] Script ran but expected output was not found (possible AV block).")
else:
    print(f"[-] PowerShell execution failed. Return code: {result.returncode}")
