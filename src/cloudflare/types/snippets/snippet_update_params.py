# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Required, TypedDict

from ..._types import FileTypes

__all__ = ["SnippetUpdateParams", "Metadata"]


class SnippetUpdateParams(TypedDict, total=False):
    zone_id: Required[str]
    """The unique ID of the zone."""

    files: Required[List[FileTypes]]
    """The list of files belonging to the snippet."""

    metadata: Required[Metadata]
    """Metadata about the snippet."""


class Metadata(TypedDict, total=False):
    main_module: Required[str]
    """Name of the file that contains the main module of the snippet."""
