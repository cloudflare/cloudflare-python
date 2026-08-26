# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from ...._types import SequenceNotStr
from ...._utils import PropertyInfo

__all__ = [
    "TagEditParams",
    "ActiveDuration",
    "ActiveDurationUnionMember1",
    "ActorCategory",
    "ActorCategoryUnionMember1",
    "Alias",
    "AttributionOrganization",
    "AttributionOrganizationUnionMember1",
    "ExternalReference",
    "InternalAlias",
    "Motive",
    "MotiveUnionMember1",
    "OpsecLevel",
    "OpsecLevelUnionMember1",
    "OriginCountryISO",
    "OriginCountryISOUnionMember1",
    "Priority",
    "PriorityUnionMember1",
    "SophisticationLevel",
    "SophisticationLevelUnionMember1",
]


class TagEditParams(TypedDict, total=False):
    account_id: Required[str]
    """Account ID."""

    active_duration: Annotated[ActiveDuration, PropertyInfo(alias="activeDuration")]

    actor_category: Annotated[ActorCategory, PropertyInfo(alias="actorCategory")]

    aliases: Iterable[Alias]
    """Structured aliases ({ value, confidence 1-10, tlp }).

    CFONE-only: stripped from responses to non-CFONE accounts.
    """

    alias_group_names: Annotated[SequenceNotStr[str], PropertyInfo(alias="aliasGroupNames")]

    alias_group_names_internal: Annotated[SequenceNotStr[str], PropertyInfo(alias="aliasGroupNamesInternal")]

    attribution_organization: Annotated[AttributionOrganization, PropertyInfo(alias="attributionOrganization")]

    category_uuid: Annotated[str, PropertyInfo(alias="categoryUuid")]
    """Tag type (category) UUID.

    When changed, existing `properties` are re-validated against the new category's
    schema (400 on mismatch). Set to null to unlink (typeless; properties stop being
    validated).
    """

    confidence: int
    """Overall tag confidence (1-10). Omit to preserve existing."""

    date_of_discovery: Annotated[str, PropertyInfo(alias="dateOfDiscovery")]
    """Date of discovery (ISO YYYY-MM-DD). Omit to preserve existing."""

    description: str

    external_reference_links: Annotated[SequenceNotStr[str], PropertyInfo(alias="externalReferenceLinks")]

    external_references: Annotated[Iterable[ExternalReference], PropertyInfo(alias="externalReferences")]
    """Structured external references ({ url, description }).

    Public: returned to all accounts.
    """

    internal_aliases: Annotated[Iterable[InternalAlias], PropertyInfo(alias="internalAliases")]
    """Internal structured aliases ({ value, confidence 1-10, tlp }).

    CFONE-only: never returned to non-CFONE accounts.
    """

    internal_description: Annotated[str, PropertyInfo(alias="internalDescription")]

    last_seen: Annotated[str, PropertyInfo(alias="lastSeen")]

    motive: Motive

    opsec_level: Annotated[OpsecLevel, PropertyInfo(alias="opsecLevel")]

    origin_country_iso: Annotated[OriginCountryISO, PropertyInfo(alias="originCountryISO")]

    priority: Priority

    properties: Dict[str, object]
    """Custom field values blob.

    When omitted, the existing value is preserved. When provided, performs a shallow
    per-key merge over the stored value (unmentioned keys are retained). Setting an
    individual key to null deletes that key. Validation runs against the merged
    result, so a partial update may omit a schema-required key if the stored value
    supplies it.
    """

    sophistication_level: Annotated[SophisticationLevel, PropertyInfo(alias="sophisticationLevel")]

    tlp: Literal["red", "amber", "amber+strict", "green", "clear", "purple"]
    """Tag-level TLP marking. Omit to preserve existing. Cannot be cleared to null."""

    value: str


class ActiveDurationUnionMember1(TypedDict, total=False):
    value: Required[str]

    confidence: int

    tlp: Literal["red", "amber", "amber+strict", "green", "clear", "purple"]


ActiveDuration: TypeAlias = Union[str, ActiveDurationUnionMember1]


class ActorCategoryUnionMember1(TypedDict, total=False):
    value: Required[str]

    confidence: int

    tlp: Literal["red", "amber", "amber+strict", "green", "clear", "purple"]


ActorCategory: TypeAlias = Union[str, ActorCategoryUnionMember1]


class Alias(TypedDict, total=False):
    value: Required[str]

    confidence: Optional[int]

    tlp: Optional[Literal["red", "amber", "amber+strict", "green", "clear", "purple"]]


class AttributionOrganizationUnionMember1(TypedDict, total=False):
    value: Required[str]

    confidence: int

    tlp: Literal["red", "amber", "amber+strict", "green", "clear", "purple"]


AttributionOrganization: TypeAlias = Union[str, AttributionOrganizationUnionMember1]


class ExternalReference(TypedDict, total=False):
    url: Required[str]

    description: Optional[str]


class InternalAlias(TypedDict, total=False):
    value: Required[str]

    confidence: Optional[int]

    tlp: Optional[Literal["red", "amber", "amber+strict", "green", "clear", "purple"]]


class MotiveUnionMember1(TypedDict, total=False):
    value: Required[str]

    confidence: int

    tlp: Literal["red", "amber", "amber+strict", "green", "clear", "purple"]


Motive: TypeAlias = Union[str, MotiveUnionMember1]


class OpsecLevelUnionMember1(TypedDict, total=False):
    value: Required[str]

    confidence: int

    tlp: Literal["red", "amber", "amber+strict", "green", "clear", "purple"]


OpsecLevel: TypeAlias = Union[str, OpsecLevelUnionMember1]


class OriginCountryISOUnionMember1(TypedDict, total=False):
    value: Required[str]

    confidence: int

    tlp: Literal["red", "amber", "amber+strict", "green", "clear", "purple"]


OriginCountryISO: TypeAlias = Union[str, OriginCountryISOUnionMember1]


class PriorityUnionMember1(TypedDict, total=False):
    value: Required[float]

    confidence: int

    tlp: Literal["red", "amber", "amber+strict", "green", "clear", "purple"]


Priority: TypeAlias = Union[float, PriorityUnionMember1]


class SophisticationLevelUnionMember1(TypedDict, total=False):
    value: Required[str]

    confidence: int

    tlp: Literal["red", "amber", "amber+strict", "green", "clear", "purple"]


SophisticationLevel: TypeAlias = Union[str, SophisticationLevelUnionMember1]
