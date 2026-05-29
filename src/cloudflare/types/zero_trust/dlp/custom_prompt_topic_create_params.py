# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["CustomPromptTopicCreateParams"]


class CustomPromptTopicCreateParams(TypedDict, total=False):
    account_id: Required[str]

    enabled: Required[bool]

    name: Required[str]

    topic: Required[str]

    description: Optional[str]

    profile_id: str
