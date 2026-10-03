# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["ObjectUploadParams"]


class ObjectUploadParams(TypedDict, total=False):
    account_id: Required[str]
    """Cloudflare account ID that owns the R2 resource."""

    bucket_name: Required[str]
    """Name of the bucket."""

    cf_r2_jurisdiction: Annotated[
        Literal["default", "eu", "us", "fedramp", "fedramp-high"], PropertyInfo(alias="cf-r2-jurisdiction")
    ]

    cf_r2_storage_class: Annotated[Literal["Standard", "InfrequentAccess"], PropertyInfo(alias="cf-r2-storage-class")]
    """Storage class for newly uploaded objects, unless specified otherwise."""
