import os
from cloudflare import Cloudflare


zone_id = os.getenv("CLOUDFLARE_ZONE_ID")
if zone_id is None:
    sys.exit("CLOUDFLARE_ZONE_ID is not defined")

alias_name = "www.mydns.com"
cannonical_name = "cname.example.com"


client = Cloudflare()


# create dns using defined driver
record = client.dns.records.create(
    zone_id=zone_id, 
    type='CNAME', 
    name=alias_name, 
    content=cannonical_name,
    proxied=False
    )


# print output
print(record)
