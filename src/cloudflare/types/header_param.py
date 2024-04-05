# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo
from .host_item import HostItem

__all__ = ["HeaderParam"]


class HeaderParam(TypedDict, total=False):
    host: Annotated[List[HostItem], PropertyInfo(alias="Host")]
    """The 'Host' header allows to override the hostname set in the HTTP request.

    Current support is 1 'Host' header override per origin.
    """
