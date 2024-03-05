# File generated from our OpenAPI spec by Stainless.

from typing import Optional

from ...._models import BaseModel

__all__ = ["MagicVisibilityMNMRuleAdvertisable"]


class MagicVisibilityMNMRuleAdvertisable(BaseModel):
    automatic_advertisement: Optional[bool] = None
    """
    Toggle on if you would like Cloudflare to automatically advertise the IP
    Prefixes within the rule via Magic Transit when the rule is triggered. Only
    available for users of Magic Transit.
    """
