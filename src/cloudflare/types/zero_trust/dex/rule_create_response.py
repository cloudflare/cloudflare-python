# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["RuleCreateResponse", "TargetedTest", "TargetedTestData"]


class TargetedTestData(BaseModel):
    """
    The configuration object which contains the details for the WARP client to conduct the test.
    """

    host: str
    """The desired endpoint to test."""

    kind: Literal["http", "traceroute"]
    """The type of test."""

    method: Optional[Literal["GET"]] = None
    """The HTTP request method type."""


class TargetedTest(BaseModel):
    data: TargetedTestData
    """
    The configuration object which contains the details for the WARP client to
    conduct the test.
    """

    enabled: bool

    name: str

    test_id: str


class RuleCreateResponse(BaseModel):
    id: str
    """API Resource UUID tag."""

    created_at: str

    match: str

    name: str

    description: Optional[str] = None

    targeted_tests: Optional[List[TargetedTest]] = None

    updated_at: Optional[str] = None
