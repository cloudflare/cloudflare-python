# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

from .request_model_param import RequestModelParam

__all__ = ["ManagedHeaderEditParams"]


class ManagedHeaderEditParams(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    managed_request_headers: Required[Iterable[RequestModelParam]]

    managed_response_headers: Required[Iterable[RequestModelParam]]
