#!/usr/bin/env python3

# This simulates how real malware hides payloads — encoded, split, or disguised — and dynamically decodes and drops them.
# You can experiment by splitting the string, compressing it, etc. Detection may or may not trigger — a good way to test behavioral AV.
# File will be created named "eicar_obf.txt"

import base64

# Base64-encoded EICAR string
encoded = "WDVPIVAlQEFQWzRcUFpYNTRQXl4pN0NDKTd9JEVJQ0FSLVNUQU5EQVItQU5USVZJUlVTLVRFU1QtRklMRSFIK0gq"

# Decode and write to file
decoded = base64.b64decode(encoded).decode('ascii')

with open("eicar_obf.txt", "w") as f:
    f.write(decoded)
