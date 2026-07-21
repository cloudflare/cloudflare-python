# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ....._models import BaseModel

__all__ = ["WebhookEvaluateResponse"]


class WebhookEvaluateResponse(BaseModel):
    """Response body for webhook evaluation test results."""

    message: str
    """Human-readable message describing the test result."""

    status_code: int
    """HTTP status code returned by the webhook endpoint. 0 if connection failed."""

    success: bool
    """Whether the webhook test was successful (received 2xx response)."""
