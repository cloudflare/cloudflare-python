# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["AssetUploadParams", "Body", "BodyMetadata"]


class AssetUploadParams(TypedDict, total=False):
    body: Required[Iterable[Body]]


class BodyMetadata(TypedDict, total=False):
    content_type: Required[Annotated[str, PropertyInfo(alias="contentType")]]
    """MIME type for the uploaded file."""


class Body(TypedDict, total=False):
    base64: Required[bool]
    """Whether value is base64 encoded."""

    key: Required[str]
    """File content hash used as the object key in the Pages asset store."""

    metadata: Required[BodyMetadata]

    value: Required[str]
    """File content. When base64 is true, this value is base64 encoded."""
