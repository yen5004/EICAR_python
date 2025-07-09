#!/usr/bin/env python3

# 1. Basic Python Dropper
# This script simply writes the EICAR string to a file "eicar_basic_dropper.txt"
# Purpose: Statick AV signature test
# Detection Chance: 100% if AV active

EICAR_STRING = "X5O!P%@AP[4\\PZX54(P^)7CC)7}$EICAR-STANDARD-ANTIVIRUS-TEST-FILE!$H+H*"

with open("eicar_basic_dropper.txt", "w") as f:
    f.write(EICAR_STRING)

#print({EICAR_STRING})
print("Basic_EICAR_Dropper testing complete. Look for eicar_basic_dropper.txt file in directory.")
