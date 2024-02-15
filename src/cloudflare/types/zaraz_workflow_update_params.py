# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["ZarazWorkflowUpdateParams"]


class ZarazWorkflowUpdateParams(TypedDict, total=False):
    body: Required[Literal["realtime", "preview"]]
    """Zaraz workflow"""
