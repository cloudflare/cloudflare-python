# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import TypedDict, Required

from typing import List

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ..._types import FileTypes
from ..._utils import PropertyInfo
from ...types import shared_params

__all__ = ["AutomaticPlatformOptimizationUpdateParams", "Value"]


class AutomaticPlatformOptimizationUpdateParams(TypedDict, total=False):
    value: Required[Value]


class Value(TypedDict, total=False):
    cache_by_device_type: Required[bool]
    """
    Indicates whether or not
    [cache by device type](https://developers.cloudflare.com/automatic-platform-optimization/reference/cache-device-type/)
    is enabled.
    """

    cf: Required[bool]
    """Indicates whether or not Cloudflare proxy is enabled."""

    enabled: Required[bool]
    """Indicates whether or not Automatic Platform Optimization is enabled."""

    hostnames: Required[List[str]]
    """
    An array of hostnames where Automatic Platform Optimization for WordPress is
    activated.
    """

    wordpress: Required[bool]
    """Indicates whether or not site is powered by WordPress."""

    wp_plugin: Required[bool]
    """
    Indicates whether or not
    [Cloudflare for WordPress plugin](https://wordpress.org/plugins/cloudflare/) is
    installed.
    """
