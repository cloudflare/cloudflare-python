# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["FraudSettings"]


class FraudSettings(BaseModel):
    user_profiles: Optional[Literal["enabled", "disabled"]] = None
    """Whether Fraud User Profiles is enabled for the zone."""

    username_expressions: Optional[List[str]] = None
    """List of expressions to detect usernames in write HTTP requests.

    - Maximum of 10 expressions.
    - Omit or set to null to leave unchanged on update.
    - Provide an empty array `[]` to clear all expressions on update.
    - Invalid expressions will result in a 10400 Bad Request with details in the
      `messages` array.
    """
