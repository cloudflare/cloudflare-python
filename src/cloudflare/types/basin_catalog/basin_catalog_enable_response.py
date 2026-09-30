# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["BasinCatalogEnableResponse"]


class BasinCatalogEnableResponse(BaseModel):
    """Contains response from activating an R2 bucket as a catalog."""

    id: str
    """Use this to uniquely identify the activated catalog."""

    name: str
    """Specifies the name of the activated catalog."""
