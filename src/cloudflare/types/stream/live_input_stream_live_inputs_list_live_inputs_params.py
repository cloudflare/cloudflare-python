# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["LiveInputStreamLiveInputsListLiveInputsParams"]


class LiveInputStreamLiveInputsListLiveInputsParams(TypedDict, total=False):
    include_counts: bool
    """
    Includes the total number of videos associated with the submitted query
    parameters.
    """
