# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["AccessDevicePostureRuleParam", "DevicePosture"]


class DevicePosture(TypedDict, total=False):
    integration_uid: Required[str]
    """The ID of a device posture integration."""


class AccessDevicePostureRuleParam(TypedDict, total=False):
    device_posture: Required[DevicePosture]
