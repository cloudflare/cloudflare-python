# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["AlwaysUseHTTPSParam"]


class AlwaysUseHTTPSParam(TypedDict, total=False):
    id: Literal["always_use_https"]
    """
    If enabled, any ` http://`` URL is converted to  `https://` through a 301
    redirect.
    """
