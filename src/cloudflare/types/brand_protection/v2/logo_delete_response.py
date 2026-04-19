# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...._models import BaseModel

__all__ = ["LogoDeleteResponse"]


class LogoDeleteResponse(BaseModel):
    message: str

    success: bool
