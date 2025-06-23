# 1. Basic Python Dropper
# This script simply writes the EICAR string to a file — the AV should catch this instantly. Run this — expect immediate AV detection.

EICAR_STRING = "X5O!P%@AP[4\\PZX54(P^)7CC)7}$EICAR-STANDARD-ANTIVIRUS-TEST-FILE!$H+H*"

with open("eicar.com", "w") as f:
    f.write(EICAR_STRING)
