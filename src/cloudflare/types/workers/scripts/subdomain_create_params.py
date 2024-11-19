# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["SubdomainCreateParams"]


class SubdomainCreateParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier"""

    enabled: bool
    """Whether the Worker should be available on the workers.dev subdomain."""
