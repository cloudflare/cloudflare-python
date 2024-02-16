# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["TsigSecondaryDNSTsigCreateTsigParams"]


class TsigSecondaryDNSTsigCreateTsigParams(TypedDict, total=False):
    algo: Required[str]
    """TSIG algorithm."""

    name: Required[str]
    """TSIG key name."""

    secret: Required[str]
    """TSIG secret."""
