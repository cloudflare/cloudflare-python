# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from ..._types import FileTypes

__all__ = ["LogoCreateParams"]


class LogoCreateParams(TypedDict, total=False):
    account_id: str

    match_type: str

    tag: str

    threshold: float

    image: FileTypes
