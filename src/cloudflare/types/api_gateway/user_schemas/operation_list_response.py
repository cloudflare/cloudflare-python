# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..api_shield import APIShield

from ...._models import BaseModel

from typing_extensions import Literal, TypeAlias

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["OperationListResponse", "APIShieldBasicOperation"]

class APIShieldBasicOperation(BaseModel):
    endpoint: str
    """
    The endpoint which can contain path parameter templates in curly braces, each
    will be replaced from left to right with {varN}, starting with {var1}, during
    insertion. This will further be Cloudflare-normalized upon insertion. See:
    https://developers.cloudflare.com/rules/normalization/how-it-works/.
    """

    host: str
    """RFC3986-compliant host."""

    method: Literal["GET", "POST", "HEAD", "OPTIONS", "PUT", "DELETE", "CONNECT", "PATCH", "TRACE"]
    """The HTTP method used to access the endpoint."""

OperationListResponse: TypeAlias = Union[APIShield, APIShieldBasicOperation]