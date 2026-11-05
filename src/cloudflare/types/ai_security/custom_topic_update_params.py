# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

__all__ = ["CustomTopicUpdateParams", "Topic"]


class CustomTopicUpdateParams(TypedDict, total=False):
    zone_id: Required[str]
    """Defines the zone."""

    topics: Iterable[Topic]
    """Custom topic categories for AI Security for Apps content detection."""


class Topic(TypedDict, total=False):
    label: Required[str]
    """Unique label identifier.

    Must contain only lowercase letters (a–z), digits (0–9), and hyphens.
    """

    topic: Required[str]
    """Description of the topic category.

    Must contain 2–50 UTF-8 bytes. Text in any language is supported, including
    spaces, numbers, punctuation, and symbols. Tabs, line breaks, invalid text, and
    invisible formatting characters are not allowed.
    """
