# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import TypedDict

__all__ = ["MechanismParam", "Email", "Pagerduty", "Webhook"]


class Email(TypedDict, total=False):
    id: str
    """The email address"""


class Pagerduty(TypedDict, total=False):
    id: str
    """UUID"""


class Webhook(TypedDict, total=False):
    id: str
    """UUID"""


class MechanismParam(TypedDict, total=False):
    """List of IDs that will be used when dispatching a notification.

    IDs for email type will be the email address.
    """

    email: Iterable[Email]

    pagerduty: Iterable[Pagerduty]

    webhooks: Iterable[Webhook]
