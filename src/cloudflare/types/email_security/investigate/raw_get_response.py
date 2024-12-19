# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.


from ...._models import BaseModel

__all__ = ["RawGetResponse"]


class RawGetResponse(BaseModel):
    raw: str
    """A UTF-8 encoded eml file of the email."""
