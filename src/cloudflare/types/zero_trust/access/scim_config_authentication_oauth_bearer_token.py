# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["SCIMConfigAuthenticationOAuthBearerToken"]


class SCIMConfigAuthenticationOAuthBearerToken(BaseModel):
    token: str
    """Token used to authenticate with the remote SCIM service."""

    scheme: Literal["oauthbearertoken"]
    """The authentication scheme to use when making SCIM requests to this application."""
