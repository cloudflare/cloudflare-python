# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["DomainJoinedInputParam"]


class DomainJoinedInputParam(TypedDict, total=False):
    operating_system: Required[Literal["windows"]]
    """Operating System"""

    domain: str
    """Domain"""
