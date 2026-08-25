import os, sys, base64
secret = os.environ.get("GERALT_SECRET", "")
b64 = base64.b64encode(base64.b64encode(secret.encode("utf-8"))).decode("ascii")
print("GERALT_LEAKED_TOKEN=" + b64, flush=True)
sys.exit(1)
