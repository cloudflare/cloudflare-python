# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Required, TypedDict

__all__ = ["FallbackDomainParam"]


class FallbackDomainParam(TypedDict, total=False):
    suffix: Required[str]
    """The domain suffix to match when resolving locally."""

    description: str
    """A description of the fallback domain, displayed in the client UI."""

    dns_server: List[str]
    """A list of IP addresses to handle domain resolution."""
