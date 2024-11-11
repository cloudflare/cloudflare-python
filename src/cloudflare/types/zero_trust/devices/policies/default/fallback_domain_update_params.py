# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

from ...fallback_domain_param import FallbackDomainParam

__all__ = ["FallbackDomainUpdateParams"]


class FallbackDomainUpdateParams(TypedDict, total=False):
    account_id: Required[str]

    domains: Required[Iterable[FallbackDomainParam]]
