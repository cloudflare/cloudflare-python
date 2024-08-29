# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["SkipConfigurationParam"]


class SkipConfigurationParam(TypedDict, total=False):
    files: Required[bool]
    """If the content type is a file, skip context analysis and return all matches."""
