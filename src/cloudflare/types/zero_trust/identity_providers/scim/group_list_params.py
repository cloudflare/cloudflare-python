# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["GroupListParams"]


class GroupListParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier"""

    cf_resource_id: str
    """
    The unique Cloudflare-generated Id of the SCIM Group resource; also known as the
    "Id".
    """

    idp_resource_id: str
    """
    The IdP-generated Id of the SCIM Group resource; also known as the "external
    Id".
    """

    name: str
    """The display name of the SCIM Group resource."""
