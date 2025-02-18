# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["Mechanism", "Email", "Pagerduty", "Webhook"]


class Email(BaseModel):
    id: Optional[str] = None
    """The email address"""


class Pagerduty(BaseModel):
    id: Optional[str] = None
    """UUID"""


class Webhook(BaseModel):
    id: Optional[str] = None
    """UUID"""


class Mechanism(BaseModel):
    email: Optional[List[Email]] = None

    pagerduty: Optional[List[Pagerduty]] = None

    webhooks: Optional[List[Webhook]] = None
