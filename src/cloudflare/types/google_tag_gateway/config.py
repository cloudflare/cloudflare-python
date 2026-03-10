# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["Config"]


class Config(BaseModel):
    """Google Tag Gateway configuration for a zone."""

    enabled: bool
    """Enables or disables Google Tag Gateway for this zone."""

    endpoint: str
    """Specifies the endpoint path for proxying Google Tag Manager requests.

    Use an absolute path starting with '/', with no nested paths and alphanumeric
    characters only (e.g. /metrics).
    """

    hide_original_ip: bool = FieldInfo(alias="hideOriginalIp")
    """Hides the original client IP address from Google when enabled."""

    measurement_id: str = FieldInfo(alias="measurementId")
    """Specify the Google Tag Manager container or measurement ID (e.g.

    GTM-XXXXXXX or G-XXXXXXXXXX).
    """

    set_up_tag: Optional[bool] = FieldInfo(alias="setUpTag", default=None)
    """Set up the associated Google Tag on the zone automatically when enabled."""
