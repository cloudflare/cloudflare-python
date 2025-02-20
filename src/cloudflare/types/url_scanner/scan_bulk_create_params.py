# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Iterable
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["ScanBulkCreateParams", "Body"]


class ScanBulkCreateParams(TypedDict, total=False):
    account_id: Required[str]
    """Account ID."""

    body: Iterable[Body]
    """List of urls to scan (up to a 100)."""


class Body(TypedDict, total=False):
    url: Required[str]

    customagent: str

    custom_headers: Annotated[Dict[str, str], PropertyInfo(alias="customHeaders")]
    """Set custom headers."""

    referer: str

    screenshots_resolutions: Annotated[
        List[Literal["desktop", "mobile", "tablet"]], PropertyInfo(alias="screenshotsResolutions")
    ]
    """Take multiple screenshots targeting different device types."""

    visibility: Literal["Public", "Unlisted"]
    """
    The option `Public` means it will be included in listings like recent scans and
    search results. `Unlisted` means it will not be included in the aforementioned
    listings, users will need to have the scan's ID to access it. A a scan will be
    automatically marked as unlisted if it fails, if it contains potential PII or
    other sensitive material.
    """
