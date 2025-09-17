# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ...._models import BaseModel

__all__ = ["ExtendedEmailMatching"]


class ExtendedEmailMatching(BaseModel):
    enabled: Optional[bool] = None
    """Enable matching all variants of user emails (with + or .

    modifiers) used as criteria in Firewall policies.
    """

    read_only: Optional[bool] = None
    """
    This setting was shared via the Orgs API and cannot be edited by the current
    account.
    """

    source_account: Optional[str] = None
    """Account tag of account that shared this setting."""

    version: Optional[int] = None
    """Version number of the setting."""
