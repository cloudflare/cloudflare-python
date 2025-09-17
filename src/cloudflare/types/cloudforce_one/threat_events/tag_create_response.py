# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["TagCreateResponse"]


class TagCreateResponse(BaseModel):
    uuid: str

    value: str

    active_duration: Optional[str] = FieldInfo(alias="activeDuration", default=None)

    actor_category: Optional[str] = FieldInfo(alias="actorCategory", default=None)

    alias_group_names: Optional[List[str]] = FieldInfo(alias="aliasGroupNames", default=None)

    alias_group_names_internal: Optional[List[str]] = FieldInfo(alias="aliasGroupNamesInternal", default=None)

    analytic_priority: Optional[float] = FieldInfo(alias="analyticPriority", default=None)

    attribution_confidence: Optional[str] = FieldInfo(alias="attributionConfidence", default=None)

    attribution_organization: Optional[str] = FieldInfo(alias="attributionOrganization", default=None)

    category_id: Optional[float] = FieldInfo(alias="categoryId", default=None)

    external_reference_links: Optional[List[str]] = FieldInfo(alias="externalReferenceLinks", default=None)

    internal_description: Optional[str] = FieldInfo(alias="internalDescription", default=None)

    motive: Optional[str] = None

    opsec_level: Optional[str] = FieldInfo(alias="opsecLevel", default=None)

    origin_country_iso: Optional[str] = FieldInfo(alias="originCountryISO", default=None)

    priority: Optional[float] = None

    sophistication_level: Optional[str] = FieldInfo(alias="sophisticationLevel", default=None)
