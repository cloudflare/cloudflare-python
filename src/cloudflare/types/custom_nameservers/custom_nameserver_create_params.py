# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["CustomNameserverCreateParams"]


class CustomNameserverCreateParams(TypedDict, total=False):
    account_id: Required[str]
    """Account identifier tag."""

    ns_name: Required[str]
    """The FQDN of the name server."""

    ns_set: float
    """The number of the set that this name server belongs to."""
