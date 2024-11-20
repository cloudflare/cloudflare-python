# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

from .api_shield_operation_model_param import APIShieldOperationModelParam

__all__ = ["OperationCreateParams"]


class OperationCreateParams(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    body: Required[Iterable[APIShieldOperationModelParam]]
