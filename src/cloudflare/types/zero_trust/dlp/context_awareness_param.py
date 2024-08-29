# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .skip_configuration_param import SkipConfigurationParam

__all__ = ["ContextAwarenessParam"]


class ContextAwarenessParam(TypedDict, total=False):
    enabled: Required[bool]
    """
    If true, scan the context of predefined entries to only return matches
    surrounded by keywords.
    """

    skip: Required[SkipConfigurationParam]
    """Content types to exclude from context analysis and return all matches."""
