# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["SchemaData"]


class SchemaData(BaseModel):
    """
    The configuration object which contains the details for the WARP client to conduct the test.
    """

    host: str
    """The desired endpoint to test."""

    kind: Literal["http", "traceroute"]
    """The type of test."""

    method: Optional[Literal["GET"]] = None
    """The HTTP request method type."""
