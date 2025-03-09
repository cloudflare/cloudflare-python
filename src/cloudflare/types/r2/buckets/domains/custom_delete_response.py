# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.


from ....._models import BaseModel

__all__ = ["CustomDeleteResponse"]


class CustomDeleteResponse(BaseModel):
    domain: str
    """Name of the removed custom domain"""
