# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["UserPopulationUpdateParams"]


class UserPopulationUpdateParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier."""

    name: Required[str]
    """The name of the user population.

    Leading and trailing whitespace is trimmed before validation. After trimming,
    the name must contain at least one non-whitespace character and must not exceed
    128 UTF-8 bytes.
    """
