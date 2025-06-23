# This simulates how real malware hides payloads — encoded, split, or disguised — and dynamically decodes and drops them.
# You can experiment by splitting the string, compressing it, etc. Detection may or may not trigger — a good way to test behavioral AV.

import base64

# Base64-encoded EICAR string
encoded = "WDVPKVB%QVBbNFxQWlg1NChQXildN0NDKTd9JEVJQ0FSLVNUQU5EQVItQU5USVZJUlVTLVRFU1QtRklMRSFKSEor"

# Decode and write to file
decoded = base64.b64decode(encoded).decode('ascii')

with open("eicar_obf.com", "w") as f:
    f.write(decoded)
