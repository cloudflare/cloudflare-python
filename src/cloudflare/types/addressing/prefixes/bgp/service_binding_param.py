# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["ServiceBindingParam", "Provisioning"]


class Provisioning(TypedDict, total=False):
    state: Literal["provisioning", "active"]
    """
    When a binding has been deployed to a majority of Cloudflare datacenters, the
    binding will become active and can be used with its associated service.
    """


class ServiceBindingParam(TypedDict, total=False):
    cidr: str
    """IP Prefix in Classless Inter-Domain Routing format."""

    provisioning: Provisioning
    """Status of a Service Binding's deployment to the Cloudflare network"""

    service_id: str
    """Identifier"""

    service_name: str
    """Name of a service running on the Cloudflare network"""
