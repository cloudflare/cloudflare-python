# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from ...._types import SequenceNotStr
from ...._utils import PropertyInfo

__all__ = ["TagCreateParams", "Alias", "ExternalReference", "InternalAlias"]


class TagCreateParams(TypedDict, total=False):
    account_id: Required[str]
    """Account ID."""

    value: Required[str]

    active_duration: Annotated[str, PropertyInfo(alias="activeDuration")]

    actor_category: Annotated[str, PropertyInfo(alias="actorCategory")]
    """Actor variety.

    Allowed values: Activist, Competitor, Customer, Crime Syndicate, Former
    Employee, Nation State, Organized Crime, Nation State Affiliated, Terrorist,
    Unaffiliated.
    """

    actor_category_confidence: Annotated[int, PropertyInfo(alias="actorCategoryConfidence")]
    """Confidence (1-10) in the actor variety (actorCategory).

    CFONE-only: stripped from responses to non-CFONE accounts.
    """

    aliases: Iterable[Alias]
    """Structured aliases ({ value, confidence 1-10, tlp }).

    CFONE-only: stripped from responses to non-CFONE accounts.
    """

    alias_group_names: Annotated[SequenceNotStr[str], PropertyInfo(alias="aliasGroupNames")]

    alias_group_names_internal: Annotated[SequenceNotStr[str], PropertyInfo(alias="aliasGroupNamesInternal")]

    analytic_priority: Annotated[float, PropertyInfo(alias="analyticPriority")]

    attribution_confidence: Annotated[str, PropertyInfo(alias="attributionConfidence")]

    attribution_confidence_score: Annotated[int, PropertyInfo(alias="attributionConfidenceScore")]

    attribution_organization: Annotated[str, PropertyInfo(alias="attributionOrganization")]

    category_uuid: Annotated[str, PropertyInfo(alias="categoryUuid")]

    date_of_discovery: Annotated[str, PropertyInfo(alias="dateOfDiscovery")]
    """Date the actor was discovered (ISO YYYY-MM-DD)."""

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

    motive: str
    """Actor motive.

    Allowed values: Convenience, Fear, Fun, Financial, Grudge, Ideology, Espionage.
    """

    motive_confidence: Annotated[int, PropertyInfo(alias="motiveConfidence")]
    """Confidence (1-10) in the actor motive.

    CFONE-only: stripped from responses to non-CFONE accounts.
    """

    opsec_level: Annotated[str, PropertyInfo(alias="opsecLevel")]

    origin_country_confidence: Annotated[int, PropertyInfo(alias="originCountryConfidence")]
    """Confidence (1-10) in the origin-country attribution.

    CFONE-only: stripped from responses to non-CFONE accounts.
    """

    origin_country_iso: Annotated[str, PropertyInfo(alias="originCountryISO")]

    origin_country_tlp: Annotated[Literal["red", "amber", "green", "white"], PropertyInfo(alias="originCountryTlp")]
    """TLP marking for the origin-country attribution.

    CFONE-only: stripped from responses to non-CFONE accounts.
    """

    priority: float

    sophistication_level: Annotated[str, PropertyInfo(alias="sophisticationLevel")]


class Alias(TypedDict, total=False):
    value: Required[str]

    confidence: Optional[int]

    tlp: Optional[Literal["red", "amber", "green", "white"]]


class ExternalReference(TypedDict, total=False):
    url: Required[str]

    description: Optional[str]


class InternalAlias(TypedDict, total=False):
    value: Required[str]

    confidence: Optional[int]

    tlp: Optional[Literal["red", "amber", "green", "white"]]
