# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Required, Literal

from typing import List

from ..host import Host

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ...._types import FileTypes
from ...._utils import PropertyInfo

__all__ = ["OrderCreateParams"]

class OrderCreateParams(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    certificate_authority: Required[Literal["google", "lets_encrypt", "ssl_com"]]
    """Certificate Authority selected for the order.

    For information on any certificate authority specific details or restrictions
    [see this page for more details.](https://developers.cloudflare.com/ssl/reference/certificate-authorities)
    """

    hosts: Required[List[Host]]
    """Comma separated list of valid host names for the certificate packs.

    Must contain the zone apex, may not contain more than 50 hosts, and may not be
    empty.
    """

    type: Required[Literal["advanced"]]
    """Type of certificate pack."""

    validation_method: Required[Literal["txt", "http", "email"]]
    """Validation Method selected for the order."""

    validity_days: Required[Literal[14, 30, 90, 365]]
    """Validity Days selected for the order."""

    cloudflare_branding: bool
    """Whether or not to add Cloudflare Branding for the order.

    This will add sni.cloudflaressl.com as the Common Name if set true.
    """