import os
import sys

from cloudflare import Cloudflare

account_id = os.getenv("CLOUDFLARE_ACCOUNT_ID")
if account_id is None:
    sys.exit("CLOUDFLARE_ACCOUNT_ID is not defined")

client = Cloudflare()

t = client.ai.run(
    "@cf/meta/m2m100-1.2b",
    account_id=account_id,
    text="I'll have an order of the moule frites",
    target_lang="french",
    source_lang="english",
)

# print(t['translated_text'])
