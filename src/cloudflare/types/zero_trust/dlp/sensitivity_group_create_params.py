# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Required, TypedDict

__all__ = ["SensitivityGroupCreateParams", "Level"]


class SensitivityGroupCreateParams(TypedDict, total=False):
    account_id: Required[str]

    name: Required[str]

    description: Optional[str]

    levels: Iterable[Level]
    """Levels to create with the group. Mutually exclusive with `template_id`."""

    template_id: Optional[str]


class Level(TypedDict, total=False):
    name: Required[str]

    description: Optional[str]
