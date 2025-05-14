# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ...._models import BaseModel

__all__ = ["DEXTestUpdateResponse", "Data", "TargetPolicy"]


class Data(BaseModel):
    host: Optional[str] = None
    """The desired endpoint to test."""

    kind: Optional[str] = None
    """The type of test."""

    method: Optional[str] = None
    """The HTTP request method type."""


class TargetPolicy(BaseModel):
    id: Optional[str] = None
    """The id of the DEX rule"""

    default: Optional[bool] = None
    """Whether the DEX rule is the account default"""

    name: Optional[str] = None
    """The name of the DEX rule"""


class DEXTestUpdateResponse(BaseModel):
    data: Data
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

    target_policies: Optional[List[TargetPolicy]] = None
    """DEX rules targeted by this test"""

    targeted: Optional[bool] = None

    test_id: Optional[str] = None
    """The unique identifier for the test."""
