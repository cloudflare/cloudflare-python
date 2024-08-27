# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["CustomCreateParams"]


class CustomCreateParams(TypedDict, total=False):
    account_id: Required[str]
    """Account ID"""

    domain: Required[str]
    """Name of the custom domain to be added"""

    zone_name: Required[Annotated[str, PropertyInfo(alias="zoneName")]]
    """Zone name of the custom domain.

    Note that `zoneName` must be a suffix of `domain`.
    """

    zone_tag: Required[Annotated[str, PropertyInfo(alias="zoneTag")]]
    """Zone tag of the custom domain"""

    enabled: bool
    """Whether to enable public bucket access at the custom domain.

    If undefined, the domain will be enabled.
    """

    zone_id: Annotated[str, PropertyInfo(alias="zoneId")]
    """Zone ID of the custom domain"""
