# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["ExtendedEmailMatchingParam"]


class ExtendedEmailMatchingParam(TypedDict, total=False):
    """Configures user email settings for firewall policies.

    When you enable this, the system standardizes email addresses in the identity portion of the rule to match extended email variants in firewall policies. When you disable this setting, the system matches email addresses exactly as you provide them. Enable this setting if your email uses `.` or `+` modifiers.
    """

    enabled: Optional[bool]
    """Specify whether to match all variants of user emails (with + or .

    modifiers) used as criteria in Firewall policies.
    """
