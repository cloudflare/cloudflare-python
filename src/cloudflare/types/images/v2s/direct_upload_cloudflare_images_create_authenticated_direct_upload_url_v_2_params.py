# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import TypedDict, Annotated

from typing import Union

from datetime import datetime

from ...._utils import PropertyInfo

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ...._types import FileTypes
from ...._utils import PropertyInfo
from ....types import shared_params

__all__ = ["DirectUploadCloudflareImagesCreateAuthenticatedDirectUploadURLV2Params"]


class DirectUploadCloudflareImagesCreateAuthenticatedDirectUploadURLV2Params(TypedDict, total=False):
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
