# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["SCIMConfigAuthenticationHTTPBasicParam"]


class SCIMConfigAuthenticationHTTPBasicParam(TypedDict, total=False):
    password: Required[str]
    """Password used to authenticate with the remote SCIM service."""

    scheme: Required[Literal["httpbasic"]]
    """The authentication scheme to use when making SCIM requests to this application."""

    user: Required[str]
    """User name used to authenticate with the remote SCIM service."""
