# File generated from our OpenAPI spec by Stainless.

from typing import List

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo
from ....._models import BaseModel
from .....types import shared

__all__ = ["ThreatCategoryListResponse", "Serie0"]


class Serie0(BaseModel):
    brand_impersonation: List[str] = FieldInfo(alias="BrandImpersonation")

    credential_harvester: List[str] = FieldInfo(alias="CredentialHarvester")

    identity_deception: List[str] = FieldInfo(alias="IdentityDeception")

    link: List[str] = FieldInfo(alias="Link")


class ThreatCategoryListResponse(BaseModel):
    meta: object

    serie_0: Serie0
