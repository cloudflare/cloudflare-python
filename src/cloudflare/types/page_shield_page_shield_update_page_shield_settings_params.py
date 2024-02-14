# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import TypedDict

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from .._types import FileTypes
from .._utils import PropertyInfo
from ..types import shared_params

__all__ = ["PageShieldPageShieldUpdatePageShieldSettingsParams"]


class PageShieldPageShieldUpdatePageShieldSettingsParams(TypedDict, total=False):
    enabled: bool
    """When true, indicates that Page Shield is enabled."""

    use_cloudflare_reporting_endpoint: bool
    """
    When true, CSP reports will be sent to
    https://csp-reporting.cloudflare.com/cdn-cgi/script_monitor/report
    """

    use_connection_url_path: bool
    """When true, the paths associated with connections URLs will also be analyzed."""
