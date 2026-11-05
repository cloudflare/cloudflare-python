# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["OrganizationCreateParams", "Parent", "Profile"]


class OrganizationCreateParams(TypedDict, total=False):
    name: Required[str]
    """The Organization name, limited to 65 UTF-8 bytes."""

    parent: Parent

    profile: Profile
    """Optional profile fields, each limited to 1,000 UTF-8 bytes.

    An empty profile is ignored.
    """


class Parent(TypedDict, total=False):
    id: Required[str]


class Profile(TypedDict, total=False):
    """Optional profile fields, each limited to 1,000 UTF-8 bytes.

    An empty profile is ignored.
    """

    business_address: str

    business_email: str

    business_name: str

    business_phone: str

    external_metadata: str
