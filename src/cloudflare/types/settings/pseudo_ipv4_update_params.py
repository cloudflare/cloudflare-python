# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["PseudoIPV4UpdateParams"]


class PseudoIPV4UpdateParams(TypedDict, total=False):
    value: Required[Literal["off", "add_header", "overwrite_header"]]
    """Value of the Pseudo IPv4 setting."""
