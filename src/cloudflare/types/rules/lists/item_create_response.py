# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...._models import BaseModel

__all__ = ["ItemCreateResponse"]


class ItemCreateResponse(BaseModel):
    operation_id: str
    """The unique operation ID of the asynchronous action."""
