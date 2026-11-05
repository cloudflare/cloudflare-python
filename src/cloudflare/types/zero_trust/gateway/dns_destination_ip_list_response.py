# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["DNSDestinationIPListResponse"]


class DNSDestinationIPListResponse(BaseModel):
    id: str

    backup_ip: str

    pair_type: Literal["shared", "dedicated", "byoip"]
    """
    Specify whether the pair shared across multiple accounts (shared) or available
    exclusively to this account. Non-shared pairs can contain Cloudflare-owned IPs
    (dedicated) or customer-provided IPs (byoip).
    """

    primary_ip: str
