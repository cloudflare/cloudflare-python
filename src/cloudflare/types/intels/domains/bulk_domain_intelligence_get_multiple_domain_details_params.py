# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["BulkDomainIntelligenceGetMultipleDomainDetailsParams"]


class BulkDomainIntelligenceGetMultipleDomainDetailsParams(TypedDict, total=False):
    domain: object
    """Accepts multiple values, i.e. `?domain=cloudflare.com&domain=example.com`."""
