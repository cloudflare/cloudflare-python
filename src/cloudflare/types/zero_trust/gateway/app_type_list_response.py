# File generated from our OpenAPI spec by Stainless.

from typing import List, Union, Optional
from datetime import datetime

from ...._models import BaseModel

__all__ = [
    "AppTypeListResponse",
    "AppTypeListResponseItem",
    "AppTypeListResponseItemZeroTrustGatewayApplication",
    "AppTypeListResponseItemZeroTrustGatewayApplicationType",
]


class AppTypeListResponseItemZeroTrustGatewayApplication(BaseModel):
    id: Optional[int] = None
    """The identifier for this application. There is only one application per ID."""

    application_type_id: Optional[int] = None
    """The identifier for the type of this application.

    There can be many applications with the same type. This refers to the `id` of a
    returned application type.
    """

    created_at: Optional[datetime] = None

    name: Optional[str] = None
    """The name of the application or application type."""


class AppTypeListResponseItemZeroTrustGatewayApplicationType(BaseModel):
    id: Optional[int] = None
    """The identifier for the type of this application.

    There can be many applications with the same type. This refers to the `id` of a
    returned application type.
    """

    created_at: Optional[datetime] = None

    description: Optional[str] = None
    """A short summary of applications with this type."""

    name: Optional[str] = None
    """The name of the application or application type."""


AppTypeListResponseItem = Union[
    AppTypeListResponseItemZeroTrustGatewayApplication, AppTypeListResponseItemZeroTrustGatewayApplicationType
]

AppTypeListResponse = List[AppTypeListResponseItem]
