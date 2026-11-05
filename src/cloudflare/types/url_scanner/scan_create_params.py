# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["ScanCreateParams"]


class ScanCreateParams(TypedDict, total=False):
    account_id: Required[str]
    """Account ID."""

    url: Required[str]

    agent_readiness: Annotated[bool, PropertyInfo(alias="agentReadiness")]
    """Enable agent readiness checks."""

    country: Literal[
        "AE",
        "AL",
        "AM",
        "AO",
        "AR",
        "AT",
        "AU",
        "AZ",
        "BB",
        "BD",
        "BE",
        "BF",
        "BG",
        "BH",
        "BN",
        "BO",
        "BR",
        "BT",
        "BW",
        "BY",
        "CA",
        "CD",
        "CH",
        "CI",
        "CL",
        "CM",
        "CO",
        "CR",
        "CW",
        "CY",
        "CZ",
        "DE",
        "DJ",
        "DK",
        "DO",
        "DZ",
        "EC",
        "EE",
        "EG",
        "ES",
        "ET",
        "FI",
        "FJ",
        "FR",
        "GB",
        "GD",
        "GE",
        "GH",
        "GR",
        "GT",
        "GU",
        "GY",
        "HK",
        "HN",
        "HR",
        "HT",
        "HU",
        "ID",
        "IE",
        "IL",
        "IN",
        "IQ",
        "IS",
        "IT",
        "JM",
        "JO",
        "JP",
        "KE",
        "KG",
        "KH",
        "KR",
        "KW",
        "KZ",
        "LA",
        "LB",
        "LK",
        "LR",
        "LT",
        "LU",
        "LV",
        "MA",
        "MD",
        "MG",
        "MK",
        "MM",
        "MN",
        "MO",
        "MT",
        "MU",
        "MV",
        "MW",
        "MX",
        "MY",
        "MZ",
        "NA",
        "NC",
        "NG",
        "NL",
        "NO",
        "NP",
        "NZ",
        "OM",
        "PA",
        "PE",
        "PF",
        "PH",
        "PK",
        "PL",
        "PR",
        "PS",
        "PT",
        "PY",
        "QA",
        "RE",
        "RO",
        "RS",
        "RU",
        "RW",
        "SA",
        "SE",
        "SG",
        "SI",
        "SK",
        "SN",
        "SR",
        "TH",
        "TJ",
        "TN",
        "TR",
        "TT",
        "TW",
        "TZ",
        "UA",
        "UG",
        "US",
        "UZ",
        "VN",
        "ZA",
        "ZM",
        "ZW",
    ]
    """Country to geo egress from"""

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
