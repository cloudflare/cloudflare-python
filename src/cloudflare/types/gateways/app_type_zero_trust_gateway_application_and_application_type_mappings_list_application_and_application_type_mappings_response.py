# File generated from our OpenAPI spec by Stainless.

from typing import Optional

from datetime import datetime

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo
from ..._models import BaseModel
from ...types import shared

__all__ = [
    "AppTypeZeroTrustGatewayApplicationAndApplicationTypeMappingsListApplicationAndApplicationTypeMappingsResponse",
    "AppTypeZeroTrustGatewayApplicationAndApplicationTypeMappingsListApplicationAndApplicationTypeMappingsResponseItem",
    "AppTypeZeroTrustGatewayApplicationAndApplicationTypeMappingsListApplicationAndApplicationTypeMappingsResponseItemZeroTrustGatewayApplication",
    "AppTypeZeroTrustGatewayApplicationAndApplicationTypeMappingsListApplicationAndApplicationTypeMappingsResponseItemZeroTrustGatewayApplicationType",
]


class AppTypeZeroTrustGatewayApplicationAndApplicationTypeMappingsListApplicationAndApplicationTypeMappingsResponseItemZeroTrustGatewayApplication(
    BaseModel
):
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


class AppTypeZeroTrustGatewayApplicationAndApplicationTypeMappingsListApplicationAndApplicationTypeMappingsResponseItemZeroTrustGatewayApplicationType(
    BaseModel
):
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


AppTypeZeroTrustGatewayApplicationAndApplicationTypeMappingsListApplicationAndApplicationTypeMappingsResponseItem = Union[
    AppTypeZeroTrustGatewayApplicationAndApplicationTypeMappingsListApplicationAndApplicationTypeMappingsResponseItemZeroTrustGatewayApplication,
    AppTypeZeroTrustGatewayApplicationAndApplicationTypeMappingsListApplicationAndApplicationTypeMappingsResponseItemZeroTrustGatewayApplicationType,
]

AppTypeZeroTrustGatewayApplicationAndApplicationTypeMappingsListApplicationAndApplicationTypeMappingsResponse = List[
    AppTypeZeroTrustGatewayApplicationAndApplicationTypeMappingsListApplicationAndApplicationTypeMappingsResponseItem
]
