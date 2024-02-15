# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["DEXTestDeleteResponse", "DEXTestDeleteResponseItem", "DEXTestDeleteResponseItemData"]


class DEXTestDeleteResponseItemData(BaseModel):
    host: Optional[str] = None
    """The desired endpoint to test."""

    kind: Optional[str] = None
    """The type of test."""

    method: Optional[str] = None
    """The HTTP request method type."""


class DEXTestDeleteResponseItem(BaseModel):
    data: DEXTestDeleteResponseItemData
    """
    The configuration object which contains the details for the WARP client to
    conduct the test.
    """

    enabled: bool
    """Determines whether or not the test is active."""

    interval: str
    """How often the test will run."""

    name: str
    """The name of the DEX test. Must be unique."""

    description: Optional[str] = None
    """Additional details about the test."""


DEXTestDeleteResponse = List[DEXTestDeleteResponseItem]
