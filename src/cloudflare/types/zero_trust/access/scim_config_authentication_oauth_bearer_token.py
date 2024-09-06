# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...._models import BaseModel

from typing_extensions import Literal

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["SCIMConfigAuthenticationOAuthBearerToken"]


class SCIMConfigAuthenticationOAuthBearerToken(BaseModel):
    token: str
    """Token used to authenticate with the remote SCIM service."""

    scheme: Literal["oauthbearertoken"]
    """The authentication scheme to use when making SCIM requests to this application."""
