# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["ServiceTokenRule", "ServiceToken"]


class ServiceToken(BaseModel):
    token_id: str
    """The ID of a Service Token."""


class ServiceTokenRule(BaseModel):
    service_token: ServiceToken
