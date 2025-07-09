#!/usr/bin/env python3

# Here’s what the payload might do before it’s base64-encoded:
import base64

eicar = base64.b64decode("WDVPIVAlQEFQWzRcUFpYNTRQXl4pN0NDKTd9JEVJQ0FSLVNUQU5EQVItQU5USVZJUlVTLVRFU1QtRklMRSFIK0gq").decode()
with open("4B_eicar_test_file.txt", "w") as f:
    f.write(eicar)

# Then you Base64-encode this whole Python snippet and embed it into the VBA macro.
# You can encode it like this from your terminal:
# echo "import base64; eicar=base64.b64decode('WDVPIVAlQEFQWzRcUFpYNTRQXl4pN0NDKTd9JEVJQ0FSLVNUQU5EQVItQU5USVZJUlVTLVRFU1QtRklMRSFIK0gq'); open('4B_eicar_test_file.txt','w').write(eicar)" | base64
# Use the output in the VBA code.
