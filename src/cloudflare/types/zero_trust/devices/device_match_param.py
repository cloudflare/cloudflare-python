# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["DeviceMatchParam"]


class DeviceMatchParam(TypedDict, total=False):
    platform: Literal["windows", "mac", "linux", "android", "ios"]
