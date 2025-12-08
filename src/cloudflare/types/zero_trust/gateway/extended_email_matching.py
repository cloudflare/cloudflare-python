# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ...._models import BaseModel

__all__ = ["ExtendedEmailMatching"]


class ExtendedEmailMatching(BaseModel):
    """Configures user email settings for firewall policies.

    When you enable this, the system standardizes email addresses in the identity portion of the rule to match extended email variants in firewall policies. When you disable this setting, the system matches email addresses exactly as you provide them. Enable this setting if your email uses `.` or `+` modifiers.
    """

    enabled: Optional[bool] = None
    """Specify whether to match all variants of user emails (with + or .

    modifiers) used as criteria in Firewall policies.
    """

    read_only: Optional[bool] = None
    """
    Indicate that this setting was shared via the Orgs API and read only for the
    current account.
    """

    source_account: Optional[str] = None
    """Indicate the account tag of the account that shared this setting."""

    version: Optional[int] = None
    """Indicate the version number of the setting."""
