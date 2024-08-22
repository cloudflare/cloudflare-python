# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["BindingCreateParams"]


class BindingCreateParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier"""

    cidr: str
    """IP Prefix in Classless Inter-Domain Routing format."""

    service_id: str
    """Identifier"""
