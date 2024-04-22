import os
import sys
from cloudflare import Cloudflare
from cloudflare.types.workers.ai_run_params import Translation

account_id = os.getenv("CLOUDFLARE_ACCOUNT_ID")
if account_id is None:
    sys.exit("CLOUDFLARE_ACCOUNT_ID is not defined")

client = Cloudflare()

input=Translation(
    text="I'll have an order of the moule frites",
    source_lang="english",
    target_lang="french",
)

t = client.workers.ai.run("@cf/meta/m2m100-1.2b", account_id=account_id, body=input)
print(t)
