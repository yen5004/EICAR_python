#!/usr/bin/env python3

# In-Memory-Only EICAR Execution
# This simulates malware that operates only in memory — no file drop — by writing the EICAR string into a BytesIO or subprocess without saving it.

import subprocess

eicar = "X5O!P%@AP[4\\PZX54(P^)7CC)7}$EICAR-STANDARD-ANTIVIRUS-TEST-FILE!$H+H*"
cmd = f'echo {eicar}'

# AVs may catch this command activity
subprocess.run(cmd, shell=True)
