# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["EndpointHealthcheckUpdateParams"]


class EndpointHealthcheckUpdateParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier"""

    check_type: Required[Literal["icmp"]]
    """type of check to perform"""

    endpoint: Required[str]
    """the IP address of the host to perform checks against"""

    name: str
    """Optional name associated with this check"""
