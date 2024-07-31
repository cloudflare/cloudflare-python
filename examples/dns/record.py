import os
import sys

from cloudflare import Cloudflare

zone_id = os.getenv("CLOUDFLARE_ZONE_ID")
if zone_id is None:
    sys.exit("CLOUDFLARE_ZONE_ID is not defined")

client = Cloudflare()

record = client.dns.records.create(
    zone_id=zone_id, 
    type='CNAME', 
    name="www.mydns.com", 
    content="cname.example.com",
    proxied=False
)

# print(record)
