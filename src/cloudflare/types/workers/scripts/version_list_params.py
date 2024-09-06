# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Required

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ...._types import FileTypes
from ...._utils import PropertyInfo

__all__ = ["VersionListParams"]


class VersionListParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier"""

    deployable: bool
    """Only return versions that can be used in a deployment. Ignores pagination."""

    page: int
    """Current page."""

    per_page: int
    """Items per-page."""
