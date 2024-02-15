# File generated from our OpenAPI spec by Stainless.

from ..._models import BaseModel

__all__ = ["TsigGetResponse"]


class TsigGetResponse(BaseModel):
    id: object

    algo: str
    """TSIG algorithm."""

    name: str
    """TSIG key name."""

    secret: str
    """TSIG secret."""
