# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["OrderCreateResponse"]


class OrderCreateResponse(BaseModel):
    id: Optional[str] = None
    """Identifier"""

    certificate_authority: Optional[Literal["google", "lets_encrypt"]] = None
    """Certificate Authority selected for the order.

    For information on any certificate authority specific details or restrictions
    [see this page for more details.](https://developers.cloudflare.com/ssl/reference/certificate-authorities)
    """

    cloudflare_branding: Optional[bool] = None
    """Whether or not to add Cloudflare Branding for the order.

    This will add sni.cloudflaressl.com as the Common Name if set true.
    """

    hosts: Optional[List[str]] = None
    """Comma separated list of valid host names for the certificate packs.

    Must contain the zone apex, may not contain more than 50 hosts, and may not be
    empty.
    """

    status: Optional[
        Literal[
            "initializing",
            "pending_validation",
            "deleted",
            "pending_issuance",
            "pending_deployment",
            "pending_deletion",
            "pending_expiration",
            "expired",
            "active",
            "initializing_timed_out",
            "validation_timed_out",
            "issuance_timed_out",
            "deployment_timed_out",
            "deletion_timed_out",
            "pending_cleanup",
            "staging_deployment",
            "staging_active",
            "deactivating",
            "inactive",
            "backup_issued",
            "holding_deployment",
        ]
    ] = None
    """Status of certificate pack."""

    type: Optional[Literal["advanced"]] = None
    """Type of certificate pack."""

    validation_method: Optional[Literal["txt", "http", "email"]] = None
    """Validation Method selected for the order."""

    validity_days: Optional[Literal[14, 30, 90, 365]] = None
    """Validity Days selected for the order."""
