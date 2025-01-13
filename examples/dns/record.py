import os
import sys

from cloudflare import Cloudflare

zone_id = os.getenv("CLOUDFLARE_ZONE_ID")
if zone_id is None:
    sys.exit("CLOUDFLARE_ZONE_ID is not defined")

client = Cloudflare()

record = client.dns.records.create(
    zone_id=zone_id,
    type="A",
    name="www.mydns.com",
    content="198.51.100.1",
    proxied=True,
)
assert record is not None

# clean up after we're done
client.dns.records.delete(
    zone_id=zone_id,
    dns_record_id=record.id,
)
