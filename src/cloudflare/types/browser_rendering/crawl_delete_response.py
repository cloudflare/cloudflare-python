# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["CrawlDeleteResponse"]


class CrawlDeleteResponse(BaseModel):
    job_id: str
    """The ID of the cancelled job."""

    message: str
    """Cancellation confirmation message."""
