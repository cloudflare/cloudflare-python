# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["SettingEditParams"]


class SettingEditParams(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier."""

    validation_default_mitigation_action: Literal["none", "log", "block"]
    """The default mitigation action used Mitigation actions are as follows:

    - `"log"` - log request when request does not conform to schema
    - `"block"` - deny access to the site when request does not conform to schema
    - `"none"` - skip running schema validation
    """

    validation_override_mitigation_action: Optional[Literal["none"]]
    """When set, this overrides both zone level and operation level mitigation actions.

    - `"none"` - skip running schema validation entirely for the request
    - `null` - clears any existing override
    """
