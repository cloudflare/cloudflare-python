# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["SSHFPRecordParam", "Data"]


class Data(TypedDict, total=False):
    algorithm: float
    """algorithm."""

    fingerprint: str
    """fingerprint."""

    type: float
    """type."""


class SSHFPRecordParam(TypedDict, total=False):
    data: Data
    """Components of a SSHFP record."""

    type: Literal["SSHFP"]
    """Record type."""
