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
    """IP subnets for this application.

    Custom application create and update requests accept IPv4 prefix lengths /8
    through /32 and IPv6 prefix lengths /32 through /128.
    """

    port_protocols: SequenceNotStr[str]
    """
    Ports matched by the application, in `protocol/port` or inclusive
    `protocol/start-end` format (for example, `tcp/443` or `udp/10000-20000`). TCP
    and UDP ports must be between 0 and 65535.
    """

    support_domains: SequenceNotStr[str]
    """Support domains matched by the application."""
