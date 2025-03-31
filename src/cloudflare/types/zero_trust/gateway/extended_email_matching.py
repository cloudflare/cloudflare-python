# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ...._models import BaseModel

__all__ = ["ExtendedEmailMatching"]


class ExtendedEmailMatching(BaseModel):
    enabled: Optional[bool] = None
    """Enable matching all variants of user emails (with + or .

    modifiers) used as criteria in Firewall policies.
    """
