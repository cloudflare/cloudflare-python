# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, TypedDict

__all__ = ["WorkloadCreateParams"]


class WorkloadCreateParams(TypedDict, total=False):
    account_id: Required[str]
    """Cloudflare account ID (32-character hexadecimal string)"""

    filter: Required[str]
    """Filter expression selecting the requests this workload matches.

    Maximum 4096 UTF-8 bytes.
    """

    name: Required[str]
    """Human-readable handle; unique per account."""

    description: str
    """Optional free-form description."""

    tags: Dict[str, str]
    """Tags to attach.

    Keys are limited to 256 UTF-8 bytes and values to 1024 UTF-8 bytes.
    """
