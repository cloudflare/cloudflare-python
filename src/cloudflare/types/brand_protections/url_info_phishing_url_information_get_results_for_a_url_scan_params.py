# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["URLInfoPhishingURLInformationGetResultsForAURLScanParams", "URLIDParam"]


class URLInfoPhishingURLInformationGetResultsForAURLScanParams(TypedDict, total=False):
    url: str

    url_id_param: URLIDParam


class URLIDParam(TypedDict, total=False):
    url_id: int
    """Submission ID(s) to filter submission results by."""
