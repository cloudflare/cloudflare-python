# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .workflow import Workflow

__all__ = ["ZarazUpdateParams"]


class ZarazUpdateParams(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    workflow: Required[Workflow]
    """Zaraz workflow"""
