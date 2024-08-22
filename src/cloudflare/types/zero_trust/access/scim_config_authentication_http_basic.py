# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...._models import BaseModel

from typing_extensions import Literal

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["SCIMConfigAuthenticationHTTPBasic"]

class SCIMConfigAuthenticationHTTPBasic(BaseModel):
    password: str
    """Password used to authenticate with the remote SCIM service."""

    scheme: Literal["httpbasic"]
    """The authentication scheme to use when making SCIM requests to this application."""

    user: str
    """User name used to authenticate with the remote SCIM service."""