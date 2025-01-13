# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = [
    "Domain",
    "AdditionalInformation",
    "Application",
    "ContentCategory",
    "InheritedContentCategory",
    "InheritedRiskType",
    "ResolvesToRef",
    "RiskType",
]


class AdditionalInformation(BaseModel):
    suspected_malware_family: Optional[str] = None
    """Suspected DGA malware family."""


class Application(BaseModel):
    id: Optional[int] = None

    name: Optional[str] = None


class ContentCategory(BaseModel):
    id: Optional[int] = None

    name: Optional[str] = None

    super_category_id: Optional[int] = None


class InheritedContentCategory(BaseModel):
    id: Optional[int] = None

    name: Optional[str] = None

    super_category_id: Optional[int] = None


class InheritedRiskType(BaseModel):
    id: Optional[int] = None

    name: Optional[str] = None

    super_category_id: Optional[int] = None


class ResolvesToRef(BaseModel):
    id: Optional[str] = None
    """
    STIX 2.1 identifier:
    https://docs.oasis-open.org/cti/stix/v2.1/cs02/stix-v2.1-cs02.html#_64yvzeku5a5c
    """

    value: Optional[str] = None
    """IP address or domain name."""


class RiskType(BaseModel):
    id: Optional[int] = None

    name: Optional[str] = None

    super_category_id: Optional[int] = None


class Domain(BaseModel):
    additional_information: Optional[AdditionalInformation] = None
    """Additional information related to the host name."""

    application: Optional[Application] = None
    """Application that the hostname belongs to."""

    content_categories: Optional[List[ContentCategory]] = None

    domain: Optional[str] = None

    inherited_content_categories: Optional[List[InheritedContentCategory]] = None

    inherited_from: Optional[str] = None
    """
    Domain from which `inherited_content_categories` and `inherited_risk_types` are
    inherited, if applicable.
    """

    inherited_risk_types: Optional[List[InheritedRiskType]] = None

    popularity_rank: Optional[int] = None
    """
    Global Cloudflare 100k ranking for the last 30 days, if available for the
    hostname. The top ranked domain is 1, the lowest ranked domain is 100,000.
    """

    resolves_to_refs: Optional[List[ResolvesToRef]] = None
    """
    Specifies a list of references to one or more IP addresses or domain names that
    the domain name currently resolves to.
    """

    risk_score: Optional[float] = None
    """
    Hostname risk score, which is a value between 0 (lowest risk) to 1 (highest
    risk).
    """

    risk_types: Optional[List[RiskType]] = None
