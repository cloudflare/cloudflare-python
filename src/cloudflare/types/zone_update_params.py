# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import TypedDict, Literal

from typing import List

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from .._types import FileTypes
from .._utils import PropertyInfo
from ..types import shared_params

__all__ = ["ZoneUpdateParams", "Plan"]


class ZoneUpdateParams(TypedDict, total=False):
    plan: Plan
    """
    (Deprecated) Please use the `/zones/{zone_id}/subscription` API to update a
    zone's plan. Changing this value will create/cancel associated subscriptions. To
    view available plans for this zone, see Zone Plans.
    """

    type: Literal["full", "partial", "secondary"]
    """A full zone implies that DNS is hosted with Cloudflare.

    A partial zone is typically a partner-hosted zone or a CNAME setup. This
    parameter is only available to Enterprise customers or if it has been explicitly
    enabled on a zone.
    """

    vanity_name_servers: List[str]
    """An array of domains used for custom name servers.

    This is only available for Business and Enterprise plans.
    """


class Plan(TypedDict, total=False):
    id: str
    """Identifier"""
