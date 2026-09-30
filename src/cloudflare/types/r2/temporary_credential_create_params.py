# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["TemporaryCredentialCreateParams"]


class TemporaryCredentialCreateParams(TypedDict, total=False):
    account_id: Required[str]
    """Cloudflare account ID that owns the R2 resource."""

    bucket: Required[str]
    """Name of the R2 bucket."""

    parent_access_key_id: Required[Annotated[str, PropertyInfo(alias="parentAccessKeyId")]]
    """Access key ID of the parent R2 API token.

    The temporary credentials cannot exceed this token's permissions.
    """

    permission: Required[Literal["admin-read-write", "admin-read-only", "object-read-write", "object-read-only"]]
    """Permissions allowed on the credentials."""

    ttl_seconds: Required[Annotated[float, PropertyInfo(alias="ttlSeconds")]]
    """
    Lifetime of the temporary credentials in seconds, up to 604800 seconds (7 days).
    """

    objects: SequenceNotStr[str]
    """Optional object paths to scope the credentials to."""

    prefixes: SequenceNotStr[str]
    """Optional prefix paths to scope the credentials to."""
