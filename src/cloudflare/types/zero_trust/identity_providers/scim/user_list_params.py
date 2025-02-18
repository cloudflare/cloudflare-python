# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["UserListParams"]


class UserListParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier"""

    cf_resource_id: str
    """
    The unique Cloudflare-generated Id of the SCIM User resource; also known as the
    "Id".
    """

    email: str
    """The email address of the SCIM User resource."""

    idp_resource_id: str
    """
    The IdP-generated Id of the SCIM User resource; also known as the "external Id".
    """

    name: str
    """The name of the SCIM User resource."""

    username: str
    """The username of the SCIM User resource."""
