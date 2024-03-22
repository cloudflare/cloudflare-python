# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = [
    "PackageListResponse",
    "LegacyJhsAPIResponseCollection",
    "LegacyJhsAPIResponseCollectionError",
    "LegacyJhsAPIResponseCollectionMessage",
    "LegacyJhsAPIResponseCollectionResultInfo",
    "Result",
    "ResultResult",
    "ResultResultLegacyJhsPackageDefinition",
    "ResultResultLegacyJhsAnomalyPackage",
]


class LegacyJhsAPIResponseCollectionError(BaseModel):
    code: int

    message: str


class LegacyJhsAPIResponseCollectionMessage(BaseModel):
    code: int

    message: str


class LegacyJhsAPIResponseCollectionResultInfo(BaseModel):
    count: Optional[float] = None
    """Total number of results for the requested service"""

    page: Optional[float] = None
    """Current page within paginated list of results"""

    per_page: Optional[float] = None
    """Number of results per page of results"""

    total_count: Optional[float] = None
    """Total results available without any search parameters"""


class LegacyJhsAPIResponseCollection(BaseModel):
    errors: List[LegacyJhsAPIResponseCollectionError]

    messages: List[LegacyJhsAPIResponseCollectionMessage]

    result: Union[List[object], str, object, None] = None

    success: Literal[True]
    """Whether the API call was successful"""

    result_info: Optional[LegacyJhsAPIResponseCollectionResultInfo] = None


class ResultResultLegacyJhsPackageDefinition(BaseModel):
    id: str
    """The unique identifier of a WAF package."""

    description: str
    """A summary of the purpose/function of the WAF package."""

    detection_mode: Literal["anomaly", "traditional"]
    """
    The mode that defines how rules within the package are evaluated during the
    course of a request. When a package uses anomaly detection mode (`anomaly`
    value), each rule is given a score when triggered. If the total score of all
    triggered rules exceeds the sensitivity defined in the WAF package, the action
    configured in the package will be performed. Traditional detection mode
    (`traditional` value) will decide the action to take when it is triggered by the
    request. If multiple rules are triggered, the action providing the highest
    protection will be applied (for example, a 'block' action will win over a
    'challenge' action).
    """

    name: str
    """The name of the WAF package."""

    zone_id: str
    """Identifier"""

    status: Optional[Literal["active"]] = None
    """
    When set to `active`, indicates that the WAF package will be applied to the
    zone.
    """


class ResultResultLegacyJhsAnomalyPackage(BaseModel):
    id: str
    """The unique identifier of a WAF package."""

    description: str
    """A summary of the purpose/function of the WAF package."""

    detection_mode: Literal["anomaly", "traditional"]
    """
    When a WAF package uses anomaly detection, each rule is given a score when
    triggered. If the total score of all triggered rules exceeds the sensitivity
    defined on the WAF package, the action defined on the package will be taken.
    """

    name: str
    """The name of the WAF package."""

    zone_id: str
    """Identifier"""

    action_mode: Optional[Literal["simulate", "block", "challenge"]] = None
    """The default action performed by the rules in the WAF package."""

    sensitivity: Optional[Literal["high", "medium", "low", "off"]] = None
    """The sensitivity of the WAF package."""

    status: Optional[Literal["active"]] = None
    """
    When set to `active`, indicates that the WAF package will be applied to the
    zone.
    """


ResultResult = Union[ResultResultLegacyJhsPackageDefinition, ResultResultLegacyJhsAnomalyPackage]


class Result(BaseModel):
    result: Optional[List[ResultResult]] = None


PackageListResponse = Union[LegacyJhsAPIResponseCollection, Result]
