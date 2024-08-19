# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Literal, TypeAlias, TypedDict

__all__ = ["SettingsMultipleRequestParam", "SettingsMultipleRequestParamItem"]


class SettingsMultipleRequestParamItem(TypedDict, total=False):
    mitigation_action: Optional[Literal["log", "block", "none"]]
    """When set, this applies a mitigation action to this operation

    - `log` log request when request does not conform to schema for this operation
    - `block` deny access to the site when request does not conform to schema for
      this operation
    - `none` will skip mitigation for this operation
    - `null` indicates that no operation level mitigation is in place, see Zone
      Level Schema Validation Settings for mitigation action that will be applied
    """


SettingsMultipleRequestParam: TypeAlias = Dict[str, SettingsMultipleRequestParamItem]
