# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["PublishCreateParams"]


class PublishCreateParams(TypedDict, total=False):
    body: Required[str]
    """Zaraz configuration description."""
