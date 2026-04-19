# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["ConfigUpdateParams"]


class ConfigUpdateParams(TypedDict, total=False):
    zone_id: str
    """Identifier."""

    enabled: Required[bool]
    """Enables or disables Google Tag Gateway for this zone."""

    endpoint: Required[str]
    """Specifies the endpoint path for proxying Google Tag Manager requests.

    Use an absolute path starting with '/', with no nested paths and alphanumeric
    characters only (e.g. /metrics).
    """

    hide_original_ip: Required[Annotated[bool, PropertyInfo(alias="hideOriginalIp")]]
    """Hides the original client IP address from Google when enabled."""

    measurement_id: Required[Annotated[str, PropertyInfo(alias="measurementId")]]
    """Specify the Google Tag Manager container or measurement ID (e.g.

    GTM-XXXXXXX or G-XXXXXXXXXX).
    """

    set_up_tag: Annotated[Optional[bool], PropertyInfo(alias="setUpTag")]
    """Set up the associated Google Tag on the zone automatically when enabled."""
