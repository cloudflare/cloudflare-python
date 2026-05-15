# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["ObjectUploadParams"]


class ObjectUploadParams(TypedDict, total=False):
    account_id: Required[str]
    """Account ID."""

    bucket_name: Required[str]
    """Name of the bucket."""

    jurisdiction: Annotated[Literal["default", "eu", "fedramp"], PropertyInfo(alias="cf-r2-jurisdiction")]
    """Jurisdiction where objects in this bucket are guaranteed to be stored."""

    cf_r2_storage_class: Annotated[Literal["Standard", "InfrequentAccess"], PropertyInfo(alias="cf-r2-storage-class")]
    """Storage class for newly uploaded objects, unless specified otherwise."""
