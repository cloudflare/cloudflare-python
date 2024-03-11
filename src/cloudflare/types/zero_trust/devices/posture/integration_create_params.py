# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, TypedDict

__all__ = [
    "IntegrationCreateParams",
    "Config",
    "ConfigTeamsDevicesWorkspaceOneConfigRequest",
    "ConfigTeamsDevicesCrowdstrikeConfigRequest",
    "ConfigTeamsDevicesUptycsConfigRequest",
    "ConfigTeamsDevicesIntuneConfigRequest",
    "ConfigTeamsDevicesKolideConfigRequest",
    "ConfigTeamsDevicesTaniumConfigRequest",
    "ConfigTeamsDevicesSentineloneS2sConfigRequest",
]


class IntegrationCreateParams(TypedDict, total=False):
    account_id: Required[object]

    config: Required[Config]
    """The configuration object containing third-party integration information."""

    interval: Required[str]
    """The interval between each posture check with the third-party API.

    Use `m` for minutes (e.g. `5m`) and `h` for hours (e.g. `12h`).
    """

    name: Required[str]
    """The name of the device posture integration."""

    type: Required[
        Literal["workspace_one", "crowdstrike_s2s", "uptycs", "intune", "kolide", "tanium", "sentinelone_s2s"]
    ]
    """The type of device posture integration."""


class ConfigTeamsDevicesWorkspaceOneConfigRequest(TypedDict, total=False):
    api_url: Required[str]
    """The Workspace One API URL provided in the Workspace One Admin Dashboard."""

    auth_url: Required[str]
    """The Workspace One Authorization URL depending on your region."""

    client_id: Required[str]
    """The Workspace One client ID provided in the Workspace One Admin Dashboard."""

    client_secret: Required[str]
    """The Workspace One client secret provided in the Workspace One Admin Dashboard."""


class ConfigTeamsDevicesCrowdstrikeConfigRequest(TypedDict, total=False):
    api_url: Required[str]
    """The Crowdstrike API URL."""

    client_id: Required[str]
    """The Crowdstrike client ID."""

    client_secret: Required[str]
    """The Crowdstrike client secret."""

    customer_id: Required[str]
    """The Crowdstrike customer ID."""


class ConfigTeamsDevicesUptycsConfigRequest(TypedDict, total=False):
    api_url: Required[str]
    """The Uptycs API URL."""

    client_key: Required[str]
    """The Uptycs client secret."""

    client_secret: Required[str]
    """The Uptycs client secret."""

    customer_id: Required[str]
    """The Uptycs customer ID."""


class ConfigTeamsDevicesIntuneConfigRequest(TypedDict, total=False):
    client_id: Required[str]
    """The Intune client ID."""

    client_secret: Required[str]
    """The Intune client secret."""

    customer_id: Required[str]
    """The Intune customer ID."""


class ConfigTeamsDevicesKolideConfigRequest(TypedDict, total=False):
    client_id: Required[str]
    """The Kolide client ID."""

    client_secret: Required[str]
    """The Kolide client secret."""


class ConfigTeamsDevicesTaniumConfigRequest(TypedDict, total=False):
    api_url: Required[str]
    """The Tanium API URL."""

    client_secret: Required[str]
    """The Tanium client secret."""

    access_client_id: str
    """
    If present, this id will be passed in the `CF-Access-Client-ID` header when
    hitting the `api_url`
    """

    access_client_secret: str
    """
    If present, this secret will be passed in the `CF-Access-Client-Secret` header
    when hitting the `api_url`
    """


class ConfigTeamsDevicesSentineloneS2sConfigRequest(TypedDict, total=False):
    api_url: Required[str]
    """The SentinelOne S2S API URL."""

    client_secret: Required[str]
    """The SentinelOne S2S client secret."""


Config = Union[
    ConfigTeamsDevicesWorkspaceOneConfigRequest,
    ConfigTeamsDevicesCrowdstrikeConfigRequest,
    ConfigTeamsDevicesUptycsConfigRequest,
    ConfigTeamsDevicesIntuneConfigRequest,
    ConfigTeamsDevicesKolideConfigRequest,
    ConfigTeamsDevicesTaniumConfigRequest,
    ConfigTeamsDevicesSentineloneS2sConfigRequest,
]
