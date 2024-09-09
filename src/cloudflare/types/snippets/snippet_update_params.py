# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["SnippetUpdateParams", "Metadata"]


class SnippetUpdateParams(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    files: str
    """Content files of uploaded snippet"""

    metadata: Metadata


class Metadata(TypedDict, total=False):
    main_module: str
    """Main module name of uploaded snippet"""
