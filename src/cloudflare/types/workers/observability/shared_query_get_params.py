# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["SharedQueryGetParams"]


class SharedQueryGetParams(TypedDict, total=False):
    account_id: Required[str]

    view: Literal["events", "invocations", "calculations"]
    """Select the view of the query result to return, defaults to events."""
