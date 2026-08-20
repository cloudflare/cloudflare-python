# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from ...._types import SequenceNotStr

__all__ = ["ApplicationUpdateParams"]


class ApplicationUpdateParams(TypedDict, total=False):
    account_id: Required[str]

    hostnames: SequenceNotStr[str]
    """Hostnames matched by the application."""

    ip_subnets: SequenceNotStr[str]
    """IP subnets matched by the application."""

    port_protocols: SequenceNotStr[str]
    """Port and protocol pairs matched by the application."""

    support_domains: SequenceNotStr[str]
    """Support domains matched by the application."""
