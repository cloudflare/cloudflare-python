# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from ..._types import SequenceNotStr

__all__ = ["FraudUpdateParams"]


class FraudUpdateParams(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier."""

    user_profiles: Literal["enabled", "disabled"]
    """Whether Fraud User Profiles is enabled for the zone."""

    username_expressions: SequenceNotStr[str]
    """List of expressions to detect usernames in write HTTP requests.

    - Maximum of 10 expressions.
    - Omit or set to null to leave unchanged on update.
    - Provide an empty array `[]` to clear all expressions on update.
    - Invalid expressions will result in a 10400 Bad Request with details in the
      `messages` array.
    """
