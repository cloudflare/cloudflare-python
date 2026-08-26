# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = [
    "TagEditResponse",
    "ActiveDurationAnnotated",
    "ActorCategoryAnnotated",
    "Alias",
    "AttributionOrganizationAnnotated",
    "ExternalReference",
    "ExternalReferencesAnnotated",
    "InternalAlias",
    "MotiveAnnotated",
    "OpsecLevelAnnotated",
    "OriginCountryISOAnnotated",
    "PriorityAnnotated",
    "SophisticationLevelAnnotated",
]


class ActiveDurationAnnotated(BaseModel):
    value: str

    tlp: Optional[Literal["red", "amber", "amber+strict", "green", "clear", "purple"]] = None


class ActorCategoryAnnotated(BaseModel):
    value: str

    confidence: Optional[float] = None

    tlp: Optional[Literal["red", "amber", "amber+strict", "green", "clear", "purple"]] = None


class Alias(BaseModel):
    value: str

    confidence: Optional[int] = None

    tlp: Optional[Literal["red", "amber", "amber+strict", "green", "clear", "purple"]] = None


class AttributionOrganizationAnnotated(BaseModel):
    value: str

    confidence: Optional[float] = None

    tlp: Optional[Literal["red", "amber", "amber+strict", "green", "clear", "purple"]] = None


class ExternalReference(BaseModel):
    url: str

    description: Optional[str] = None


class ExternalReferencesAnnotated(BaseModel):
    value: str

    tlp: Optional[Literal["red", "amber", "amber+strict", "green", "clear", "purple"]] = None


class InternalAlias(BaseModel):
    value: str

    confidence: Optional[int] = None

    tlp: Optional[Literal["red", "amber", "amber+strict", "green", "clear", "purple"]] = None


class MotiveAnnotated(BaseModel):
    value: str

    confidence: Optional[float] = None

    tlp: Optional[Literal["red", "amber", "amber+strict", "green", "clear", "purple"]] = None


class OpsecLevelAnnotated(BaseModel):
    value: str

    confidence: Optional[float] = None

    tlp: Optional[Literal["red", "amber", "amber+strict", "green", "clear", "purple"]] = None


class OriginCountryISOAnnotated(BaseModel):
    value: Optional[str] = None

    confidence: Optional[float] = None

    tlp: Optional[Literal["red", "amber", "amber+strict", "green", "clear", "purple"]] = None


class PriorityAnnotated(BaseModel):
    value: float

    tlp: Optional[Literal["red", "amber", "amber+strict", "green", "clear", "purple"]] = None


class SophisticationLevelAnnotated(BaseModel):
    value: str

    confidence: Optional[float] = None

    tlp: Optional[Literal["red", "amber", "amber+strict", "green", "clear", "purple"]] = None


class TagEditResponse(BaseModel):
    uuid: str

    value: str

    active_duration: Optional[str] = FieldInfo(alias="activeDuration", default=None)

    active_duration_annotated: Optional[ActiveDurationAnnotated] = FieldInfo(
        alias="activeDuration_annotated", default=None
    )

    actor_category: Optional[str] = FieldInfo(alias="actorCategory", default=None)

    actor_category_annotated: Optional[ActorCategoryAnnotated] = FieldInfo(
        alias="actorCategory_annotated", default=None
    )

    aliases: Optional[List[Alias]] = None
    """Structured aliases ({ value, confidence 1-10, tlp }).

    CFONE-only: stripped from responses to non-CFONE accounts.
    """

    alias_group_names: Optional[List[str]] = FieldInfo(alias="aliasGroupNames", default=None)

    alias_group_names_internal: Optional[List[str]] = FieldInfo(alias="aliasGroupNamesInternal", default=None)

    attribution_organization: Optional[str] = FieldInfo(alias="attributionOrganization", default=None)

    attribution_organization_annotated: Optional[AttributionOrganizationAnnotated] = FieldInfo(
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

    external_references: Optional[List[ExternalReference]] = FieldInfo(alias="externalReferences", default=None)
    """Structured external references ({ url, description }).

    Public: returned to all accounts.
    """

    external_references_annotated: Optional[List[ExternalReferencesAnnotated]] = FieldInfo(
        alias="externalReferences_annotated", default=None
    )

    internal_aliases: Optional[List[InternalAlias]] = FieldInfo(alias="internalAliases", default=None)
    """Internal structured aliases ({ value, confidence 1-10, tlp }).

    CFONE-only: never returned to non-CFONE accounts.
    """

    internal_description: Optional[str] = FieldInfo(alias="internalDescription", default=None)

    last_seen: Optional[str] = FieldInfo(alias="lastSeen", default=None)

    motive: Optional[str] = None

    motive_annotated: Optional[MotiveAnnotated] = None

    opsec_level: Optional[str] = FieldInfo(alias="opsecLevel", default=None)

    opsec_level_annotated: Optional[OpsecLevelAnnotated] = FieldInfo(alias="opsecLevel_annotated", default=None)

    origin_country_iso: Optional[str] = FieldInfo(alias="originCountryISO", default=None)
    """ISO country code (alpha-2 or alpha-3).

    Normalized to uppercase on read. Null when stored value is blank/whitespace.
    """

    origin_country_iso_annotated: Optional[OriginCountryISOAnnotated] = FieldInfo(
        alias="originCountryISO_annotated", default=None
    )

    priority: Optional[float] = None

    priority_annotated: Optional[PriorityAnnotated] = None

    properties: Optional[Dict[str, object]] = None
    """Parsed custom field values. Null when the tag has no custom fields."""

    sophistication_level: Optional[str] = FieldInfo(alias="sophisticationLevel", default=None)

    sophistication_level_annotated: Optional[SophisticationLevelAnnotated] = FieldInfo(
        alias="sophisticationLevel_annotated", default=None
    )

    tlp: Optional[Literal["red", "amber", "amber+strict", "green", "clear", "purple"]] = None
    """Tag-level TLP handling marking."""

    updated_at: Optional[str] = FieldInfo(alias="updatedAt", default=None)

    version: Optional[float] = None
