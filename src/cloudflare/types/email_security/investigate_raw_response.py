# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.


from ..._models import BaseModel

__all__ = ["InvestigateRawResponse"]


class InvestigateRawResponse(BaseModel):
    raw: str
    """A UTF-8 encoded eml file of the email."""
