# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from datetime import datetime
from typing_extensions import TypeAlias

from ...._models import BaseModel

__all__ = ["AppType", "ZeroTrustGatewayApplication", "ZeroTrustGatewayApplicationType"]


class ZeroTrustGatewayApplication(BaseModel):
    id: Optional[int] = None
    """Identify this application. Only one application per ID."""

    application_type_id: Optional[int] = None
    """Identify the type of this application.

    Multiple applications can share the same type. Refers to the `id` of a returned
    application type.
    """

    created_at: Optional[datetime] = None

    name: Optional[str] = None
    """Specify the name of the application or application type."""


class ZeroTrustGatewayApplicationType(BaseModel):
    id: Optional[int] = None
    """Identify the type of this application.

    Multiple applications can share the same type. Refers to the `id` of a returned
    application type.
    """

    created_at: Optional[datetime] = None

    description: Optional[str] = None
    """Provide a short summary of applications with this type."""

    name: Optional[str] = None
    """Specify the name of the application or application type."""


AppType: TypeAlias = Union[ZeroTrustGatewayApplication, ZeroTrustGatewayApplicationType]
