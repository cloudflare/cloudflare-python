# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["HTTP3UpdateParams"]


class HTTP3UpdateParams(TypedDict, total=False):
    value: Required[Literal["on", "off"]]
    """Value of the HTTP3 setting."""
