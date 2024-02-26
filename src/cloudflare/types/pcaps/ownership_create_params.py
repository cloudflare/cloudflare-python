# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["OwnershipCreateParams"]


class OwnershipCreateParams(TypedDict, total=False):
    destination_conf: Required[str]
    """The full URI for the bucket. This field only applies to `full` packet captures."""
