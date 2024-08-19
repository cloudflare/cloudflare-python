# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["V1EditParams"]


class V1EditParams(TypedDict, total=False):
    account_id: Required[str]
    """Account identifier tag."""

    metadata: object
    """User modifiable key-value store.

    Can be used for keeping references to another system of record for managing
    images. No change if not specified.
    """

    require_signed_urls: Annotated[bool, PropertyInfo(alias="requireSignedURLs")]
    """Indicates whether the image can be accessed using only its UID.

    If set to `true`, a signed token needs to be generated with a signing key to
    view the image. Returns a new UID on a change. No change if not specified.
    """
