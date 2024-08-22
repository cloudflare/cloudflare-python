# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["SCIMConfigAuthenticationOAuthBearerTokenParam"]


class SCIMConfigAuthenticationOAuthBearerTokenParam(TypedDict, total=False):
    token: Required[str]
    """Token used to authenticate with the remote SCIM service."""

    scheme: Required[Literal["oauthbearertoken"]]
    """The authentication scheme to use when making SCIM requests to this application."""
