#!/usr/bin/env python3

# 1. Basic Python Dropper
# This script simply writes the EICAR string to a file \u2014 the AV should catch this instantly. Run this \u2014 expect immediate AV detection.


EICAR_STRING = "X5O!P%@AP[4\\PZX54(P^)7CC)7}$EICAR-STANDARD-ANTIVIRUS-TEST-FILE!$H+H*"

with open("eicar.com", "w") as f:
    f.write(EICAR_STRING)

print("writing  complete")
print({EICAR_STRING})
print("all test complete")

