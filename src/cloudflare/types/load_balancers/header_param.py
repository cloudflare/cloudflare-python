# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List

from .host import Host

from typing_extensions import TypedDict, Annotated

from ..._utils import PropertyInfo

__all__ = ["HeaderParam"]


class HeaderParam(TypedDict, total=False):
    host: Annotated[List[Host], PropertyInfo(alias="Host")]
    """The 'Host' header allows to override the hostname set in the HTTP request.

    Current support is 1 'Host' header override per origin.
    """
