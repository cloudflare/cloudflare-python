# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Required, TypedDict

__all__ = ["SCIMConfigAuthenticationOauth2Param"]


class SCIMConfigAuthenticationOauth2Param(TypedDict, total=False):
    authorization_url: Required[str]
    """URL used to generate the auth code used during token generation."""

    client_id: Required[str]
    """
    Client ID used to authenticate when generating a token for authenticating with
    the remote SCIM service.
    """

    client_secret: Required[str]
    """
    Secret used to authenticate when generating a token for authenticating with the
    remove SCIM service.
    """

    scheme: Required[Literal["oauth2"]]
    """The authentication scheme to use when making SCIM requests to this application."""

    token_url: Required[str]
    """
    URL used to generate the token used to authenticate with the remote SCIM
    service.
    """

    scopes: List[str]
    """
    The authorization scopes to request when generating the token used to
    authenticate with the remove SCIM service.
    """
