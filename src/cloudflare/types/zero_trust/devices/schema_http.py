# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ...._models import BaseModel
from .schema_data import SchemaData

__all__ = ["SchemaHTTP", "TargetPolicy"]


class TargetPolicy(BaseModel):
    id: Optional[str] = None
    """The id of the device settings profile"""

    default: Optional[bool] = None
    """Whether the profile is the account default"""

    name: Optional[str] = None
    """The name of the device settings profile"""


class SchemaHTTP(BaseModel):
    data: SchemaData
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
    """Device settings profiles targeted by this test"""

    targeted: Optional[bool] = None

    test_id: Optional[str] = None
    """The unique identifier for the test."""
