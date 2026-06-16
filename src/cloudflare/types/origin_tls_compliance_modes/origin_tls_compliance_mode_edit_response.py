# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["OriginTLSComplianceModeEditResponse"]


class OriginTLSComplianceModeEditResponse(BaseModel):
    id: Literal["origin_tls_compliance_modes"]
    """The identifier of the caching setting."""

    editable: bool
    """Whether the setting is editable."""

    value: List[str]
    """
    List of TLS compliance modes that constrain the key-exchange algorithms
    Cloudflare may use when establishing the TLS connection to the zone's origin.
    Currently supported values are `fips` (FIPS-approved curves) and `pqh`
    (post-quantum hybrid). Future modes (e.g. `cnsa2`) may be added; clients should
    treat unknown values as opaque strings. Multiple modes are combined as the
    intersection of their permitted algorithm lists; selections whose intersection
    is empty are rejected. An empty list clears the constraint.
    """

    modified_on: Optional[datetime] = None
    """Last time this setting was modified."""
