# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["SessionGetSessionTranscriptsParams"]


class SessionGetSessionTranscriptsParams(TypedDict, total=False):
    account_id: Required[str]
    """The account identifier tag."""

    app_id: Required[str]
    """The app identifier tag."""

    format: Literal["SRT", "VTT", "JSON", "CSV"]
    """Transcript file format to fetch."""
