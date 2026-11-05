# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["DomainACLCreateParams", "Entry"]


class DomainACLCreateParams(TypedDict, total=False):
    account_id: Required[str]
    """Cloudflare account ID (32-character hexadecimal string)"""

    default_action: Required[Literal["ALLOW", "BLOCK"]]
    """Default action when no entry matches"""

    entries: Required[Optional[Iterable[Entry]]]
    """Domain entries for this ACL. Each domain must appear at most once."""

    name: Required[str]
    """Name of the domain ACL"""


class Entry(TypedDict, total=False):
    action: Required[Literal["ALLOW", "BLOCK"]]
    """Per-domain decision overriding the parent ACL's default_action"""

    domain: Required[str]
    """Hostname or domain pattern, capped at 255 UTF-8 bytes"""
