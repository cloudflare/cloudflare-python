# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Required, TypedDict

__all__ = ["AutomaticPlatformOptimizationParam"]


class AutomaticPlatformOptimizationParam(TypedDict, total=False):
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
