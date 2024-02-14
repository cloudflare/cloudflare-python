# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import TypedDict, Required, Literal

from typing import Optional

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ..._types import FileTypes
from ..._utils import PropertyInfo
from ...types import shared_params

__all__ = ["MobileRedirectUpdateParams", "Value"]


class MobileRedirectUpdateParams(TypedDict, total=False):
    value: Required[Value]
    """Value of the zone setting."""


class Value(TypedDict, total=False):
    mobile_subdomain: Optional[str]
    """
    Which subdomain prefix you wish to redirect visitors on mobile devices to
    (subdomain must already exist).
    """

    status: Literal["on", "off"]
    """Whether or not mobile redirect is enabled."""

    strip_uri: bool
    """
    Whether to drop the current page path and redirect to the mobile subdomain URL
    root, or keep the path and redirect to the same page on the mobile subdomain.
    """
