# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict, Required

from typing import List

__all__ = ["ActionParam"]


class ActionParam(TypedDict, total=False):
    type: Required[Literal["drop", "forward", "worker"]]
    """Type of supported action."""

    value: Required[List[str]]
