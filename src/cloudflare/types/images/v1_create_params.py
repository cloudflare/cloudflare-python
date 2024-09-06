# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Required, Annotated

from ..._utils import PropertyInfo

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ..._types import FileTypes
from ..._utils import PropertyInfo

__all__ = ["V1CreateParams"]


class V1CreateParams(TypedDict, total=False):
    account_id: Required[str]
    """Account identifier tag."""

    file: object
    """An image binary data. Only needed when type is uploading a file."""

    metadata: object
    """User modifiable key-value store.

    Can use used for keeping references to another system of record for managing
    images.
    """

    require_signed_urls: Annotated[bool, PropertyInfo(alias="requireSignedURLs")]
    """Indicates whether the image requires a signature token for the access."""

    url: str
    """A URL to fetch an image from origin.

    Only needed when type is uploading from a URL.
    """
