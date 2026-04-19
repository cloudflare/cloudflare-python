# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from ..._types import SequenceNotStr

__all__ = ["LogoMatchDownloadParams"]


class LogoMatchDownloadParams(TypedDict, total=False):
    account_id: str

    limit: str

    logo_id: SequenceNotStr[str]

    offset: str
