# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import TypedDict, Required, Literal

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ..._types import FileTypes
from ..._utils import PropertyInfo
from ...types import shared_params

__all__ = ["ImageResizingUpdateParams", "Value"]


class ImageResizingUpdateParams(TypedDict, total=False):
    value: Required[Value]
    """
    Image Resizing provides on-demand resizing, conversion and optimisation for
    images served through Cloudflare's network. Refer to the
    [Image Resizing documentation](https://developers.cloudflare.com/images/) for
    more information.
    """


class Value(TypedDict, total=False):
    id: Required[Literal["image_resizing"]]
    """ID of the zone setting."""

    value: Required[Literal["on", "off", "open"]]
    """Current value of the zone setting."""
