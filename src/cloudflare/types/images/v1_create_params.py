# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["V1CreateParams"]


class V1CreateParams(TypedDict, total=False):
    account_id: Required[str]
    """Account identifier tag."""

    metadata: object

    require_signed_urls: Annotated[bool, PropertyInfo(alias="requireSignedURLs")]
    """Indicates whether the image requires a signature token for the access."""
