# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["DirectUploadCreateParams"]


class DirectUploadCreateParams(TypedDict, total=False):
    account_id: Required[str]
    """Account identifier tag."""

    expiry: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """The date after which the upload will not be accepted.

    Minimum: Now + 2 minutes. Maximum: Now + 6 hours.
    """

    metadata: object
    """User modifiable key-value store.

    Can be used for keeping references to another system of record, for managing
    images.
    """

    require_signed_urls: Annotated[bool, PropertyInfo(alias="requireSignedURLs")]
    """Indicates whether the image requires a signature token to be accessed."""
