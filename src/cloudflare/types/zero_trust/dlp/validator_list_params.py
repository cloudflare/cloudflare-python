# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["ValidatorListParams"]


class ValidatorListParams(TypedDict, total=False):
    account_id: Required[str]

    kind: Optional[Literal["proximity_words", "worker"]]
    """Only return validators of this kind. Omit to return every kind."""
