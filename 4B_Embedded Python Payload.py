# Here’s what the payload might do before it’s base64-encoded:
import base64

eicar = base64.b64decode("WDVPKVB...").decode()
with open("eicar.com", "w") as f:
    f.write(eicar)

# Then you Base64-encode this whole Python snippet and embed it into the VBA macro.
# You can encode it like this from your terminal:
# echo "import base64; eicar=base64.b64decode('...'); open('eicar.com','w').write(eicar)" | base64
# Use the output in the VBA code.
