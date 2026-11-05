# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, TypedDict

__all__ = ["PolicyUpdateParams"]


class PolicyUpdateParams(TypedDict, total=False):
    account_id: Required[str]
    """Cloudflare account ID (32-character hexadecimal string)"""

    entrypoint: Required[str]
    """Non-function rule declared in rego_source.

    Evaluation uses data.<package_path>.<entrypoint>.
    """

    filter: Required[str]
    """Filter expression that determines whether this policy applies.

    Maximum 4096 UTF-8 bytes.
    """

    name: Required[str]
    """Name of the policy"""

    rego_source: Required[str]
    """
    Inline Rego source with a package beginning with "policy." Maximum 16384 UTF-8
    bytes.
    """

    description: str
    """Optional free-form description."""

    tags: Dict[str, str]
    """Replacement tag set.

    Omit or use {} to clear. Keys are limited to 256 UTF-8 bytes and values to 1024
    UTF-8 bytes.
    """
