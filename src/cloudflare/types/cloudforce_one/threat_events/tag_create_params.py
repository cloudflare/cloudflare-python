# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ...._types import SequenceNotStr
from ...._utils import PropertyInfo

__all__ = ["TagCreateParams"]


class TagCreateParams(TypedDict, total=False):
    account_id: Required[str]
    """Account ID."""

    value: Required[str]

    active_duration: Annotated[str, PropertyInfo(alias="activeDuration")]

    actor_category: Annotated[str, PropertyInfo(alias="actorCategory")]

    alias_group_names: Annotated[SequenceNotStr[str], PropertyInfo(alias="aliasGroupNames")]

    alias_group_names_internal: Annotated[SequenceNotStr[str], PropertyInfo(alias="aliasGroupNamesInternal")]

    analytic_priority: Annotated[float, PropertyInfo(alias="analyticPriority")]

    attribution_confidence: Annotated[str, PropertyInfo(alias="attributionConfidence")]

    attribution_organization: Annotated[str, PropertyInfo(alias="attributionOrganization")]

    category_id: Annotated[float, PropertyInfo(alias="categoryId")]

    external_reference_links: Annotated[SequenceNotStr[str], PropertyInfo(alias="externalReferenceLinks")]

    internal_description: Annotated[str, PropertyInfo(alias="internalDescription")]

    motive: str

    opsec_level: Annotated[str, PropertyInfo(alias="opsecLevel")]

    origin_country_iso: Annotated[str, PropertyInfo(alias="originCountryISO")]

    priority: float

    sophistication_level: Annotated[str, PropertyInfo(alias="sophisticationLevel")]
