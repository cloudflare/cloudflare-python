# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["SCIMConfigAuthenticationOauth2"]


class SCIMConfigAuthenticationOauth2(BaseModel):
    authorization_url: str
    """URL used to generate the auth code used during token generation."""

    client_id: str
    """
    Client ID used to authenticate when generating a token for authenticating with
    the remote SCIM service.
    """

    client_secret: str
    """
    Secret used to authenticate when generating a token for authenticating with the
    remove SCIM service.
    """

    scheme: Literal["oauth2"]
    """The authentication scheme to use when making SCIM requests to this application."""

    token_url: str
    """
    URL used to generate the token used to authenticate with the remote SCIM
    service.
    """

    scopes: Optional[List[str]] = None
    """
    The authorization scopes to request when generating the token used to
    authenticate with the remove SCIM service.
    """
