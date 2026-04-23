# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["InvestigateGetParams"]


class InvestigateGetParams(TypedDict, total=False):
    account_id: Required[str]
    """Account Identifier"""

    submission: bool
    """When true, search the submissions datastore only.

    When false or omitted, search the regular datastore only.
    """
