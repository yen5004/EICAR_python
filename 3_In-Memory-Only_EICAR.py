# Memory-based AV test using PowerShell injection (advanced). 
# Use Python to spawn a PowerShell command that generates the EICAR string in memory. This more closely mimics malware droppers used in red teaming.
# This variant avoids writing to disk. AV/EDR with script and memory inspection will often catch it.

import subprocess

powershell_cmd = '''
$e="X5O!P%@AP[4\\PZX54(P^)7CC)7}$EICAR-STANDARD-ANTIVIRUS-TEST-FILE!$H+H*"
[System.Text.Encoding]::ASCII.GetBytes($e) | Out-Null
'''

subprocess.run(["powershell", "-Command", powershell_cmd], shell=True)
