# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from ....._types import SequenceNotStr

__all__ = ["FindingTypeUpdateParams"]


class FindingTypeUpdateParams(TypedDict, total=False):
    account_id: Required[str]

    applies_to_all_integrations: Required[bool]
    """
    When true, this finding type applies to every current and future integration of
    the vendor.
    """

    description: str
    """Optional description of the finding type.

    Cannot be empty if provided. Maximum 4096 characters.
    """

    integration_ids: SequenceNotStr[str]
    """
    Required and non-empty when applies_to_all_integrations is false; omit when it
    is true.
    """

    name: str
    """Human-readable name for the finding type.

    Cannot be empty if provided. Maximum 256 characters.
    """

    severity: Literal["Critical", "High", "Medium", "Low"]
    """Default severity used when no integration-specific severity override exists.

    Changing it reclassifies existing and future findings that do not have an
    override.
    """
