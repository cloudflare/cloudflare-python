# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["SkillCreateParams"]


class SkillCreateParams(TypedDict, total=False):
    account_id: Required[str]

    name: Required[str]

    output_schema: Required[str]

    prompt: Required[str]

    type: Required[Literal["summary", "tags"]]
