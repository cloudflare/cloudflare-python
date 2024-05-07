# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal

__all__ = ["CheckRegion"]

CheckRegion = Literal[
    "WNAM", "ENAM", "WEU", "EEU", "NSAM", "SSAM", "OC", "ME", "NAF", "SAF", "SAS", "SEAS", "NEAS", "ALL_REGIONS"
]

RegionIDParam = List[CheckRegion]
