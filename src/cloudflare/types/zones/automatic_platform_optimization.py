# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel

__all__ = ["AutomaticPlatformOptimization"]


class AutomaticPlatformOptimization(BaseModel):
    cache_by_device_type: bool
    """
    Indicates whether or not
    [cache by device type](https://developers.cloudflare.com/automatic-platform-optimization/reference/cache-device-type/)
    is enabled.
    """

    cf: bool
    """Indicates whether or not Cloudflare proxy is enabled."""

    enabled: bool
    """Indicates whether or not Automatic Platform Optimization is enabled."""

    hostnames: List[str]
    """
    An array of hostnames where Automatic Platform Optimization for WordPress is
    activated.
    """

    wordpress: bool
    """Indicates whether or not site is powered by WordPress."""

    wp_plugin: bool
    """
    Indicates whether or not
    [Cloudflare for WordPress plugin](https://wordpress.org/plugins/cloudflare/) is
    installed.
    """
