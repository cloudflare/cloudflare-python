# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["ApplicationDeleteResponse"]


class ApplicationDeleteResponse(BaseModel):
    """Result of starting asynchronous deletion for a Containers application."""

    message: str
