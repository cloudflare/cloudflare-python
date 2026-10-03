# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["InstanceListParams"]


class InstanceListParams(TypedDict, total=False):
    account_id: Required[str]

    name_prefix: str
    """
    Filter instances by a case-sensitive name prefix, falling back to the actor ID
    when no name is known. Keep the same prefix when using a page token.
    """

    page_token: str
    """Opaque token from a previous response to retrieve the next page."""

    per_page: int
    """Maximum number of instances to return per page. Defaults to 100."""

    state: Literal["active", "not-active"]
    """Filters instances by lifecycle state.

    `active` includes provisioning, running, and stopping instances; `not-active`
    includes stopped and failed instances. When omitted, all instances are returned.
    """
