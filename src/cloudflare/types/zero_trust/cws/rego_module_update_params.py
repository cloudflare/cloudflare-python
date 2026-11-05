# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["RegoModuleUpdateParams"]


class RegoModuleUpdateParams(TypedDict, total=False):
    account_id: Required[str]
    """Cloudflare account ID (32-character hexadecimal string)"""

    name: Required[str]
    """Name of the Rego module (unique per account)"""

    rego_source: Required[str]
    """
    Library Rego source with a package beginning with "lib." Maximum 16384 UTF-8
    bytes.
    """
