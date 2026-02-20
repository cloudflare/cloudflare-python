# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["RuleListResponse", "Rule", "RuleTargetedTest", "RuleTargetedTestData"]


class RuleTargetedTestData(BaseModel):
    """
    The configuration object which contains the details for the WARP client to conduct the test.
    """

    host: str
    """The desired endpoint to test."""

    kind: Literal["http", "traceroute"]
    """The type of test."""

    method: Optional[Literal["GET"]] = None
    """The HTTP request method type."""


class RuleTargetedTest(BaseModel):
    data: RuleTargetedTestData
    """
    The configuration object which contains the details for the WARP client to
    conduct the test.
    """

    enabled: bool

    name: str

    test_id: str


class Rule(BaseModel):
    id: str
    """API Resource UUID tag."""

    created_at: str

    match: str

    name: str

    description: Optional[str] = None

    targeted_tests: Optional[List[RuleTargetedTest]] = None

    updated_at: Optional[str] = None


class RuleListResponse(BaseModel):
    rules: Optional[List[Rule]] = None
