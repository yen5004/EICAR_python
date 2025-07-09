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


