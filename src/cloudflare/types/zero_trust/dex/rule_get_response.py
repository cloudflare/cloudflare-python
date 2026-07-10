# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ...._models import BaseModel
from ..devices.schema_data import SchemaData

__all__ = ["RuleGetResponse", "TargetedTest"]


class TargetedTest(BaseModel):
    data: SchemaData
    """
    The configuration object which contains the details for the WARP client to
    conduct the test.
    """

    enabled: bool

    name: str

    test_id: str


class RuleGetResponse(BaseModel):
    id: str
    """API Resource UUID tag."""

    created_at: str

    match: str

    name: str

    description: Optional[str] = None

    targeted_tests: Optional[List[TargetedTest]] = None

    updated_at: Optional[str] = None
