# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from ...._models import BaseModel
from .schema_data import SchemaData

__all__ = ["SchemaHTTP", "TargetPolicy"]


class TargetPolicy(BaseModel):
    id: str
    """The id of the DEX rule."""

    default: Optional[bool] = None
    """Whether the DEX rule is the account default."""

    name: Optional[str] = None
    """The name of the DEX rule."""


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

    created: Optional[datetime] = None
    """Date the test was created, in RFC 3339 format."""

    description: Optional[str] = None
    """Additional details about the test."""

    target_policies: Optional[List[TargetPolicy]] = None
    """DEX rules targeted by this test"""

    targeted: Optional[bool] = None

    test_id: Optional[str] = None
    """The unique identifier for the test."""

    updated: Optional[datetime] = None
    """Date the test was last updated, in RFC 3339 format."""
