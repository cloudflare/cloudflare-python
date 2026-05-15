# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ...._models import BaseModel

__all__ = ["TopupCreateResponse"]


class TopupCreateResponse(BaseModel):
    client_secret: Optional[str] = None
    """Stripe PaymentIntent client secret."""

    onboarding: bool
    """Whether the user was already onboarded."""

    payment_intent_id: str
    """Stripe invoice ID."""

    brand: Optional[str] = None
    """Card brand (visa, mastercard, etc.)."""

    last4: Optional[str] = None
    """Last 4 digits of card."""
