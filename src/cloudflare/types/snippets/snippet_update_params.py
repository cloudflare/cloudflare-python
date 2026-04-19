# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["SnippetUpdateParams", "Metadata"]


class SnippetUpdateParams(TypedDict, total=False):
    zone_id: str
    """Use this field to specify the unique ID of the zone."""

    metadata: Required[Metadata]
    """Provide metadata about the snippet."""


class Metadata(TypedDict, total=False):
    """Provide metadata about the snippet."""

    main_module: Required[str]
    """Specify the name of the file that contains the main module of the snippet."""
