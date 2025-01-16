# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["ServiceBinding", "Provisioning"]


class Provisioning(BaseModel):
    state: Optional[Literal["provisioning", "active"]] = None
    """
    When a binding has been deployed to a majority of Cloudflare datacenters, the
    binding will become active and can be used with its associated service.
    """


class ServiceBinding(BaseModel):
    id: Optional[str] = None
    """Identifier of a Service Binding."""

    cidr: Optional[str] = None
    """IP Prefix in Classless Inter-Domain Routing format."""

    provisioning: Optional[Provisioning] = None
    """Status of a Service Binding's deployment to the Cloudflare network"""

    service_id: Optional[str] = None
    """Identifier of a Service on the Cloudflare network.

    Available services and their IDs may be found in the **List Services** endpoint.
    """

    service_name: Optional[str] = None
    """Name of a service running on the Cloudflare network"""
