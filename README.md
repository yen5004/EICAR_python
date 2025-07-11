# EICAR_python
Ptyhon files used in EICAR testing

Breakdown of the EICAR Test Variants

0. Flat_Out_EICARS
```python
X5O!P%@AP[4\\PZX54(P^)7CC)7}$EICAR-STANDARD-ANTIVIRUS-TEST-FILE!$H+H*
```
- What it does: EICAR test string with python extension.
- Purpose: Static AV signature test.
- Detection chance: 100% if AV is active.

---

🧱 1. Basic Python Dropper
``` python
EICAR_STRING = "X5O!P%@AP[4\\PZX54(P^)7CC)7}$EICAR-STANDARD-ANTIVIRUS-TEST-FILE!$H+H*"
with open("eicar_basic_dropper.txt", "w") as f:
    f.write(EICAR_STRING)
```

- What it does: Writes the known EICAR test string to disk (eicar_basic.dropper.txt).
- Purpose: Static AV signature test.
- Detection chance: 100% if AV is active.

---

2. In-Memory_EICAR.py
``` python
#!/usr/bin/env python3

# In-memory EICAR simulation (no shell, no disk)
# Prints the EICAR test string to stdout, without writing to disk.

from io import BytesIO

# EICAR string
eicar = b"X5O!P%@AP[4\\PZX54(P^)7CC)7}$EICAR-STANDARD-ANTIVIRUS-TEST-FILE!$H+H*"

# Write to an in-memory buffer
mem_buffer = BytesIO()
mem_buffer.write(eicar)

# Seek to beginning if needed
mem_buffer.seek(0)

# Read it back
data = mem_buffer.read()
print("In-memory EICAR data loaded:", data.decode())

```
- Does not write to disk
- Does not call subprocesses
- Only manipulates EICAR entirely in memory
- Final result is printed to stdout

🔐 *Security Summary*
|Risk Category | Status |
|--------------|--------|
|Malicious behavior |	❌ None (no system changes, no persistence, no network) |
|Malicious payload |	✅ EICAR (benign but signature known) |
|Evasion technique |	✅ Yes (runs purely in-memory) |
|Detection likelihood |	⚠️ Low (unless monitored memory or stdout logging) |

✅ *TL;DR – Will It Be Detected?*
|-------------------------------------------------------- |
| ❌	Most antivirus solutions will not detect this script. |
| ⚠️	Enterprise EDRs might detect it if they scan memory or correlate stdout logs. |
| ✅	Writing the EICAR string to a file or subprocess is almost guaranteed to trigger AV. |

---

🧅 3. Obfuscated Dropper
``` python
encoded = "Base64_EICAR_String"
decoded = base64.b64decode(encoded).decode('ascii')
with open("eicar_obf.txt", "w") as f:
    f.write(decoded)
```
- What it does: Hides the EICAR string in Base64, decodes it at runtime.
- Purpose: Simulates basic payload encoding like malware often uses.
- Detection chance: Lower unless AV/EDR inspects script behavior.

---

🧠 4. In-Memory Execution
Subprocess with echo
``` python
cmd = f'echo {eicar}'
subprocess.run(["echo", eicar])
```
- What it does: Uses system shell to echo the EICAR string.
- Purpose: Mimics droppers that execute payloads in memory or with LOLBins (Living Off the Land Binaries).
- Detection chance: Medium to high, depending on AV script monitoring.

 ---

5. Tempfile_EICAR with auto-deletion 
``` python
with tempfile.NamedTemporaryFile(...) as tmp:
    tmp.write(eicar.encode())
os.remove(tmp.name)
```
- What it does: Creates a temp file, writes the string, deletes it quickly.
- Purpose: Simulates malware that cleans up after itself.
- Detection chance: Depends on AV reaction time.

---

6. PowerShell_Injection_EICARS
``` python
powershell_cmd = '$e="..."; [System.Text.Encoding]::ASCII.GetBytes($e) | Out-Null'
subprocess.run(["powershell", "-Command", powershell_cmd])
```
- What it does: Runs PowerShell to generate EICAR in memory.
- Purpose: Simulates real-world fileless malware or script-based attacks.
- Detection chance: Very high for good EDRs.

---

🪤 7. Excel VBA Macro → Python Dropper
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

📦 8. Embedded Python Payload
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



