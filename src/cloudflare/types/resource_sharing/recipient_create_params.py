# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["RecipientCreateParams"]


class RecipientCreateParams(TypedDict, total=False):
    path_account_id: Required[Annotated[str, PropertyInfo(alias="account_id")]]
    """Account identifier."""

    body_account_id: Annotated[str, PropertyInfo(alias="account_id")]
    """Deprecated alias for `recipient_account_id`.

    Use `recipient_account_id` instead. The body field collided with the URL path
    parameter of the same name, which prevented SDK generators from distinguishing
    the source account (in the URL) from the recipient account (in the body). Both
    names will continue to be accepted until 2027-05-26 (see `x-sunset`).
    """

    organization_id: str
    """Organization identifier."""

    recipient_account_id: str
    """The account that will receive the share."""
