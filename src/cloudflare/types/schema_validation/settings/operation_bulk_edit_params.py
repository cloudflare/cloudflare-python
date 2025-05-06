# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["OperationBulkEditParams", "Body"]


class OperationBulkEditParams(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier."""

    body: Required[Dict[str, Body]]


class Body(TypedDict, total=False):
    mitigation_action: Optional[Literal["none", "log", "block"]]
    """Mitigation actions are as follows:

    - `log` - log request when request does not conform to schema _ `block` - deny
      access to the site when request does not conform to schema _ `none` - skip
      running schema validation \\** null - clears any existing per-operation setting
    """
