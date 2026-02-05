# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from ..._types import SequenceNotStr

__all__ = ["LogoMatchGetParams"]


class LogoMatchGetParams(TypedDict, total=False):
    account_id: Required[str]

    limit: str

    logo_id: SequenceNotStr[str]

    offset: str
