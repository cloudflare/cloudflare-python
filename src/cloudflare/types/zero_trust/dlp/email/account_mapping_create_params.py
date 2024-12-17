# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = ["AccountMappingCreateParams", "AuthRequirements", "AuthRequirementsUnionMember0", "AuthRequirementsType"]


class AccountMappingCreateParams(TypedDict, total=False):
    account_id: Required[str]

    auth_requirements: Required[AuthRequirements]


class AuthRequirementsUnionMember0(TypedDict, total=False):
    allowed_microsoft_organizations: Required[List[str]]

    type: Required[Literal["Org"]]


class AuthRequirementsType(TypedDict, total=False):
    type: Required[Literal["NoAuth"]]


AuthRequirements: TypeAlias = Union[AuthRequirementsUnionMember0, AuthRequirementsType]
