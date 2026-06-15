# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .cf1_site_location_param import Cf1SiteLocationParam

__all__ = ["Cf1SiteUpdateParams"]


class Cf1SiteUpdateParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier"""

    description: str
    """A human-provided description of the CF1 Site."""

    location: Cf1SiteLocationParam

    name: str
    """
    A human-provided name describing the CF1 Site that should be unique within the
    account.
    """
