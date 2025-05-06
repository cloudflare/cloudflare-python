# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .provider import Provider
from ...._models import BaseModel

__all__ = ["Sippy", "Destination", "Source"]


class Destination(BaseModel):
    access_key_id: Optional[str] = FieldInfo(alias="accessKeyId", default=None)
    """ID of the Cloudflare API token used when writing objects to this bucket"""

    account: Optional[str] = None

    bucket: Optional[str] = None
    """Name of the bucket on the provider"""

    provider: Optional[Provider] = None


class Source(BaseModel):
    bucket: Optional[str] = None
    """Name of the bucket on the provider"""

    provider: Optional[Literal["aws", "gcs"]] = None

    region: Optional[str] = None
    """Region where the bucket resides (AWS only)"""


class Sippy(BaseModel):
    destination: Optional[Destination] = None
    """Details about the configured destination bucket"""

    enabled: Optional[bool] = None
    """State of Sippy for this bucket"""

    source: Optional[Source] = None
    """Details about the configured source bucket"""
