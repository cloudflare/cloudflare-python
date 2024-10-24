# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["SCIMConfigAuthenticationHTTPBasic"]


class SCIMConfigAuthenticationHTTPBasic(BaseModel):
    password: str
    """Password used to authenticate with the remote SCIM service."""

    scheme: Literal["httpbasic"]
    """The authentication scheme to use when making SCIM requests to this application."""

    user: str
    """User name used to authenticate with the remote SCIM service."""
