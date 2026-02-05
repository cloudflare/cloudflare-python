# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .host import Host
from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["HeaderParam"]


class HeaderParam(TypedDict, total=False):
    """The request header is used to pass additional information with an HTTP request.

    Currently supported header is 'Host'.
    """

    host: Annotated[SequenceNotStr[Host], PropertyInfo(alias="Host")]
    """The 'Host' header allows to override the hostname set in the HTTP request.

    Current support is 1 'Host' header override per origin.
    """
