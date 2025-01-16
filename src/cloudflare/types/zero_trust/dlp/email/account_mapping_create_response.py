# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union
from typing_extensions import Literal, TypeAlias

from ....._models import BaseModel

__all__ = ["AccountMappingCreateResponse", "AuthRequirements", "AuthRequirementsUnionMember0", "AuthRequirementsType"]


class AuthRequirementsUnionMember0(BaseModel):
    allowed_microsoft_organizations: List[str]

    type: Literal["Org"]


class AuthRequirementsType(BaseModel):
    type: Literal["NoAuth"]


AuthRequirements: TypeAlias = Union[AuthRequirementsUnionMember0, AuthRequirementsType]


class AccountMappingCreateResponse(BaseModel):
    addin_identifier_token: str

    auth_requirements: AuthRequirements
