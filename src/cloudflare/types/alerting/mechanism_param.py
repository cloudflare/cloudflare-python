# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import TypedDict

__all__ = ["MechanismParam", "Email", "Pagerduty", "Webhook"]


class Email(TypedDict, total=False):
    id: str
    """The email address"""


class Pagerduty(TypedDict, total=False):
    pass


class Webhook(TypedDict, total=False):
    pass


class MechanismParam(TypedDict, total=False):
    email: Iterable[Email]

    pagerduty: Iterable[Pagerduty]

    webhooks: Iterable[Webhook]
