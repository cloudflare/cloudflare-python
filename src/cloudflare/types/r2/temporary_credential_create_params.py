# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["TemporaryCredentialCreateParams"]


class TemporaryCredentialCreateParams(TypedDict, total=False):
    account_id: Required[str]
    """Account ID"""

    bucket: Required[str]
    """Name of the R2 bucket"""

    parent_access_key_id: Required[Annotated[str, PropertyInfo(alias="parentAccessKeyId")]]
    """The parent access key id to use for signing"""

    permission: Required[Literal["admin-read-write", "admin-read-only", "object-read-write", "object-read-only"]]
    """Permissions allowed on the credentials"""

    ttl_seconds: Required[Annotated[float, PropertyInfo(alias="ttlSeconds")]]
    """How long the credentials will live for in seconds"""

    objects: List[str]
    """Optional object paths to scope the credentials to"""

    prefixes: List[str]
    """Optional prefix paths to scope the credentials to"""
