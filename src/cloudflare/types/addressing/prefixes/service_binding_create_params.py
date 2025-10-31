# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ServiceBindingCreateParams"]


class ServiceBindingCreateParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier of a Cloudflare account."""

    cidr: str
    """IP Prefix in Classless Inter-Domain Routing format."""

    service_id: str
    """Identifier of a Service on the Cloudflare network.

    Available services and their IDs may be found in the **List Services** endpoint.
    """
