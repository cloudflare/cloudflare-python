# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

from .cf1_site_param import Cf1SiteParam

__all__ = ["Cf1SiteCreateParams"]


class Cf1SiteCreateParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier"""

    body: Required[Iterable[Cf1SiteParam]]
