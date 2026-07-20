# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["TagListResponse", "Pagination", "Tag", "TagAlias", "TagExternalReference", "TagInternalAlias"]


class Pagination(BaseModel):
    page: float

    page_size: float = FieldInfo(alias="pageSize")

    total_count: float = FieldInfo(alias="totalCount")

    total_pages: float = FieldInfo(alias="totalPages")


class TagAlias(BaseModel):
    value: str

    confidence: Optional[int] = None

    tlp: Optional[Literal["red", "amber", "green", "white"]] = None


class TagExternalReference(BaseModel):
    url: str

    description: Optional[str] = None


class TagInternalAlias(BaseModel):
    value: str

    confidence: Optional[int] = None

    tlp: Optional[Literal["red", "amber", "green", "white"]] = None


class Tag(BaseModel):
    uuid: str

    value: str

    active_duration: Optional[str] = FieldInfo(alias="activeDuration", default=None)

    actor_category: Optional[str] = FieldInfo(alias="actorCategory", default=None)

    actor_category_confidence: Optional[int] = FieldInfo(alias="actorCategoryConfidence", default=None)
    """Confidence (1-10) in the actor variety (actorCategory).

    CFONE-only: stripped from responses to non-CFONE accounts.
    """

    aliases: Optional[List[TagAlias]] = None
    """Structured aliases ({ value, confidence 1-10, tlp }).

    CFONE-only: stripped from responses to non-CFONE accounts.
    """

    alias_group_names: Optional[List[str]] = FieldInfo(alias="aliasGroupNames", default=None)

    alias_group_names_internal: Optional[List[str]] = FieldInfo(alias="aliasGroupNamesInternal", default=None)

    analytic_priority: Optional[float] = FieldInfo(alias="analyticPriority", default=None)

    attribution_confidence: Optional[str] = FieldInfo(alias="attributionConfidence", default=None)

    attribution_confidence_score: Optional[int] = FieldInfo(alias="attributionConfidenceScore", default=None)

    attribution_organization: Optional[str] = FieldInfo(alias="attributionOrganization", default=None)

    category_name: Optional[str] = FieldInfo(alias="categoryName", default=None)

    category_uuid: Optional[str] = FieldInfo(alias="categoryUuid", default=None)

    date_of_discovery: Optional[str] = FieldInfo(alias="dateOfDiscovery", default=None)

    external_reference_links: Optional[List[str]] = FieldInfo(alias="externalReferenceLinks", default=None)

    external_references: Optional[List[TagExternalReference]] = FieldInfo(alias="externalReferences", default=None)
    """Structured external references ({ url, description }).

    Public: returned to all accounts.
    """

    internal_aliases: Optional[List[TagInternalAlias]] = FieldInfo(alias="internalAliases", default=None)
    """Internal structured aliases ({ value, confidence 1-10, tlp }).

    CFONE-only: never returned to non-CFONE accounts.
    """

    internal_description: Optional[str] = FieldInfo(alias="internalDescription", default=None)

    motive: Optional[str] = None

    motive_confidence: Optional[int] = FieldInfo(alias="motiveConfidence", default=None)
    """Confidence (1-10) in the actor motive.

    CFONE-only: stripped from responses to non-CFONE accounts.
    """

    opsec_level: Optional[str] = FieldInfo(alias="opsecLevel", default=None)

    origin_country_confidence: Optional[int] = FieldInfo(alias="originCountryConfidence", default=None)
    """Confidence (1-10) in the origin-country attribution.

    CFONE-only: stripped from responses to non-CFONE accounts.
    """

    origin_country_iso: Optional[str] = FieldInfo(alias="originCountryISO", default=None)

    origin_country_iso_alpha3: Optional[str] = FieldInfo(alias="originCountryISOAlpha3", default=None)

    origin_country_tlp: Optional[Literal["red", "amber", "green", "white"]] = FieldInfo(
        alias="originCountryTlp", default=None
    )
    """TLP marking for the origin-country attribution.

    CFONE-only: stripped from responses to non-CFONE accounts.
    """

    priority: Optional[float] = None

    sophistication_level: Optional[str] = FieldInfo(alias="sophisticationLevel", default=None)


class TagListResponse(BaseModel):
    pagination: Pagination

    tags: List[Tag]
