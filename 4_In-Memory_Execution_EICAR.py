#!/usr/bin/env python3

# In-Memory-Execution EICAR
# This simulates malware that operates only in memory, no file drop by writing the EICAR string into a BytesIO or subprocess without saving it.
# Upon completion of running this script the eicars text should be displayed on screen.

import subprocess

eicar = "X5O!P%@AP[4\\PZX54(P^)7CC)7}$EICAR-STANDARD-ANTIVIRUS-TEST-FILE!$H+H*"
cmd = f'echo {eicar}'

# AVs may catch this command activity
subprocess.run(["echo", eicar])
