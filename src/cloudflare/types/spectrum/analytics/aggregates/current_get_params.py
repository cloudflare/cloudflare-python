# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ....._utils import PropertyInfo

__all__ = ["CurrentGetParams"]


class CurrentGetParams(TypedDict, total=False):
    app_id_param: str
    """Comma-delimited list of Spectrum Application Id(s).

    If provided, the response will be limited to Spectrum Application Id(s) that
    match.
    """

    app_id: Annotated[str, PropertyInfo(alias="appID")]
    """Comma-delimited list of Spectrum Application Id(s).

    If provided, the response will be limited to Spectrum Application Id(s) that
    match.
    """

    colo_name: str
    """Co-location identifier."""
