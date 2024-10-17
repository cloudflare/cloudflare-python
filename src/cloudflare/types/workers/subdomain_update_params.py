# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["SubdomainUpdateParams"]


class SubdomainUpdateParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier"""

    subdomain: str
