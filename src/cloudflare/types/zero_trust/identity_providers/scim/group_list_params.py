# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from ....._types import SequenceNotStr

__all__ = ["GroupListParams"]


class GroupListParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier."""

    cf_resource_id: SequenceNotStr[str]
    """
    The unique Cloudflare-generated Id of the SCIM Group resource; also known as the
    "Id". Pass once for a single lookup (`?cf_resource_id=A`) or repeat the
    parameter (`?cf_resource_id=A&cf_resource_id=B`) to look up multiple groups in
    one request, up to 50 values. Mutually exclusive with `idp_resource_id`, `name`,
    `search_contains`, and `search_starts_with`.
    """

    idp_resource_id: SequenceNotStr[str]
    """
    The IdP-generated Id of the SCIM Group resource; also known as the "external
    Id". Pass once for a single lookup (`?idp_resource_id=A`) or repeat the
    parameter (`?idp_resource_id=A&idp_resource_id=B`) to look up multiple groups in
    one request, up to 50 values. Mutually exclusive with `cf_resource_id`, `name`,
    `search_contains`, and `search_starts_with`.
    """

    name: str
    """The display name of the SCIM Group resource."""

    page: int
    """Page number of results."""

    per_page: int
    """Number of results per page."""
