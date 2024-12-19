# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ....._models import BaseModel

__all__ = ["Integration", "Config"]


class Config(BaseModel):
    api_url: str
    """The Workspace One API URL provided in the Workspace One Admin Dashboard."""

    auth_url: str
    """The Workspace One Authorization URL depending on your region."""

    client_id: str
    """The Workspace One client ID provided in the Workspace One Admin Dashboard."""


class Integration(BaseModel):
    id: Optional[str] = None
    """API UUID."""

    config: Optional[Config] = None
    """The configuration object containing third-party integration information."""

    interval: Optional[str] = None
    """The interval between each posture check with the third-party API.

    Use `m` for minutes (e.g. `5m`) and `h` for hours (e.g. `12h`).
    """

    name: Optional[str] = None
    """The name of the device posture integration."""

    type: Optional[
        Literal[
            "workspace_one", "crowdstrike_s2s", "uptycs", "intune", "kolide", "tanium", "sentinelone_s2s", "custom_s2s"
        ]
    ] = None
    """The type of device posture integration."""
