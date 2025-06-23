# Use tempfile, auto-delete file after use. This mimics a dropper that writes to disk briefly.
# Depending on AV configuration, detection might occur on write or not at all (especially if detection is on execution or after a scheduled scan).

import tempfile
import os

eicar = "X5O!P%@AP[4\\PZX54(P^)7CC)7}$EICAR-STANDARD-ANTIVIRUS-TEST-FILE!$H+H*"

with tempfile.NamedTemporaryFile(delete=False, suffix=".com") as tmp:
    tmp.write(eicar.encode())
    tmp.flush()
    print(f"Wrote to {tmp.name}")

# Manually delete, or rely on system cleanup
os.remove(tmp.name)
