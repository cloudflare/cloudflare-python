# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["CNAMERecordParam", "Settings"]


class Settings(TypedDict, total=False):
    flatten_cname: bool
    """
    If enabled, causes the CNAME record to be resolved externally and the resulting
    address records (e.g., A and AAAA) to be returned instead of the CNAME record
    itself. This setting has no effect on proxied records, which are always
    flattened.
    """


class CNAMERecordParam(TypedDict, total=False):
    content: str
    """A valid hostname. Must not match the record's name."""

    settings: Settings

    type: Literal["CNAME"]
    """Record type."""
