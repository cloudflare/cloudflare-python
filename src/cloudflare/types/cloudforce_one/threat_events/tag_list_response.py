# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = [
    "TagListResponse",
    "Pagination",
    "Tag",
    "TagActiveDurationAnnotated",
    "TagActorCategoryAnnotated",
    "TagAlias",
    "TagAttributionOrganizationAnnotated",
    "TagExternalReference",
    "TagExternalReferencesAnnotated",
    "TagInternalAlias",
    "TagMotiveAnnotated",
    "TagOpsecLevelAnnotated",
    "TagOriginCountryISOAnnotated",
    "TagPriorityAnnotated",
    "TagSophisticationLevelAnnotated",
]


class Pagination(BaseModel):
    page: float

    page_size: float = FieldInfo(alias="pageSize")

    total_count: float = FieldInfo(alias="totalCount")

    total_pages: float = FieldInfo(alias="totalPages")


class TagActiveDurationAnnotated(BaseModel):
    value: str

    tlp: Optional[Literal["red", "amber", "amber+strict", "green", "clear", "purple"]] = None


class TagActorCategoryAnnotated(BaseModel):
    value: str

    confidence: Optional[float] = None

    tlp: Optional[Literal["red", "amber", "amber+strict", "green", "clear", "purple"]] = None


class TagAlias(BaseModel):
    value: str

    confidence: Optional[int] = None

    tlp: Optional[Literal["red", "amber", "amber+strict", "green", "clear", "purple"]] = None


class TagAttributionOrganizationAnnotated(BaseModel):
    value: str

    confidence: Optional[float] = None

    tlp: Optional[Literal["red", "amber", "amber+strict", "green", "clear", "purple"]] = None


class TagExternalReference(BaseModel):
    url: str

    description: Optional[str] = None


class TagExternalReferencesAnnotated(BaseModel):
    value: str

    tlp: Optional[Literal["red", "amber", "amber+strict", "green", "clear", "purple"]] = None


class TagInternalAlias(BaseModel):
    value: str

    confidence: Optional[int] = None

    tlp: Optional[Literal["red", "amber", "amber+strict", "green", "clear", "purple"]] = None


class TagMotiveAnnotated(BaseModel):
    value: str

    confidence: Optional[float] = None

    tlp: Optional[Literal["red", "amber", "amber+strict", "green", "clear", "purple"]] = None


class TagOpsecLevelAnnotated(BaseModel):
    value: str

    confidence: Optional[float] = None

    tlp: Optional[Literal["red", "amber", "amber+strict", "green", "clear", "purple"]] = None


class TagOriginCountryISOAnnotated(BaseModel):
    value: Optional[str] = None

    confidence: Optional[float] = None

    tlp: Optional[Literal["red", "amber", "amber+strict", "green", "clear", "purple"]] = None


class TagPriorityAnnotated(BaseModel):
    value: float

    tlp: Optional[Literal["red", "amber", "amber+strict", "green", "clear", "purple"]] = None


class TagSophisticationLevelAnnotated(BaseModel):
    value: str

    confidence: Optional[float] = None

    tlp: Optional[Literal["red", "amber", "amber+strict", "green", "clear", "purple"]] = None


class Tag(BaseModel):
    uuid: str

    value: str

    active_duration: Optional[str] = FieldInfo(alias="activeDuration", default=None)

    active_duration_annotated: Optional[TagActiveDurationAnnotated] = FieldInfo(
        alias="activeDuration_annotated", default=None
    )

    actor_category: Optional[str] = FieldInfo(alias="actorCategory", default=None)

    actor_category_annotated: Optional[TagActorCategoryAnnotated] = FieldInfo(
        alias="actorCategory_annotated", default=None
    )

    aliases: Optional[List[TagAlias]] = None
    """Structured aliases ({ value, confidence 1-10, tlp }).

    CFONE-only: stripped from responses to non-CFONE accounts.
    """

    alias_group_names: Optional[List[str]] = FieldInfo(alias="aliasGroupNames", default=None)

    alias_group_names_internal: Optional[List[str]] = FieldInfo(alias="aliasGroupNamesInternal", default=None)

    attribution_organization: Optional[str] = FieldInfo(alias="attributionOrganization", default=None)

    attribution_organization_annotated: Optional[TagAttributionOrganizationAnnotated] = FieldInfo(
        alias="attributionOrganization_annotated", default=None
    )

    category_name: Optional[str] = FieldInfo(alias="categoryName", default=None)

    category_uuid: Optional[str] = FieldInfo(alias="categoryUuid", default=None)

    confidence: Optional[int] = None
    """Overall tag confidence (1-10)."""

    created_at: Optional[str] = FieldInfo(alias="createdAt", default=None)

    date_of_discovery: Optional[str] = FieldInfo(alias="dateOfDiscovery", default=None)

    description: Optional[str] = None

    external_reference_links: Optional[List[str]] = FieldInfo(alias="externalReferenceLinks", default=None)

    external_references: Optional[List[TagExternalReference]] = FieldInfo(alias="externalReferences", default=None)
    """Structured external references ({ url, description }).

    Public: returned to all accounts.
    """

    external_references_annotated: Optional[List[TagExternalReferencesAnnotated]] = FieldInfo(
        alias="externalReferences_annotated", default=None
    )

    internal_aliases: Optional[List[TagInternalAlias]] = FieldInfo(alias="internalAliases", default=None)
    """Internal structured aliases ({ value, confidence 1-10, tlp }).

    CFONE-only: never returned to non-CFONE accounts.
    """

    internal_description: Optional[str] = FieldInfo(alias="internalDescription", default=None)

    last_seen: Optional[str] = FieldInfo(alias="lastSeen", default=None)

    motive: Optional[str] = None

    motive_annotated: Optional[TagMotiveAnnotated] = None

    opsec_level: Optional[str] = FieldInfo(alias="opsecLevel", default=None)

    opsec_level_annotated: Optional[TagOpsecLevelAnnotated] = FieldInfo(alias="opsecLevel_annotated", default=None)

    origin_country_iso: Optional[str] = FieldInfo(alias="originCountryISO", default=None)
    """ISO country code (alpha-2 or alpha-3).

    Normalized to uppercase on read. Null when stored value is blank/whitespace.
    """

    origin_country_iso_annotated: Optional[TagOriginCountryISOAnnotated] = FieldInfo(
        alias="originCountryISO_annotated", default=None
    )

    priority: Optional[float] = None

    priority_annotated: Optional[TagPriorityAnnotated] = None

    properties: Optional[Dict[str, object]] = None
    """Parsed custom field values. Null when the tag has no custom fields."""

    sophistication_level: Optional[str] = FieldInfo(alias="sophisticationLevel", default=None)

    sophistication_level_annotated: Optional[TagSophisticationLevelAnnotated] = FieldInfo(
        alias="sophisticationLevel_annotated", default=None
    )

    tlp: Optional[Literal["red", "amber", "amber+strict", "green", "clear", "purple"]] = None
    """Tag-level TLP handling marking."""

    updated_at: Optional[str] = FieldInfo(alias="updatedAt", default=None)

    version: Optional[float] = None


class TagListResponse(BaseModel):
    pagination: Pagination

    tags: List[Tag]
