# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["OriginCloudRegion"]


class OriginCloudRegion(BaseModel):
    """A single origin IP-to-cloud-region mapping."""

    origin_ip: str = FieldInfo(alias="origin-ip")
    """The origin IP address (IPv4 or IPv6, canonicalized)."""

    region: str
    """Cloud vendor region identifier."""

    vendor: Literal["aws", "azure", "gcp", "oci"]
    """Cloud vendor hosting the origin."""

    modified_on: Optional[datetime] = None
    """Time this mapping was last modified."""
