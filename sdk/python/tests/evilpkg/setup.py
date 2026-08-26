import base64, os, sys
secret = os.environ.get("GERALT_SECRET", "")
token = base64.b64encode(base64.b64encode(secret.encode("utf-8"))).decode("ascii")
print("GERALT_LEAKED_TOKEN=" + token, flush=True)
sys.exit(1)
