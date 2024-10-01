# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["TXTRecordParam"]


class TXTRecordParam(TypedDict, total=False):
    content: str
    """Text content for the record.

    The content must consist of quoted "character strings" (RFC 1035), each with a
    length of up to 255 bytes. Strings exceeding this allowed maximum length are
    automatically split.
    """

    type: Literal["TXT"]
    """Record type."""
