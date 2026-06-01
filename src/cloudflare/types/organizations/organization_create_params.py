# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .organization_profile_param import OrganizationProfileParam

__all__ = ["OrganizationCreateParams", "Parent"]


class OrganizationCreateParams(TypedDict, total=False):
    name: Required[str]

    parent: Parent

    profile: OrganizationProfileParam


class Parent(TypedDict, total=False):
    id: Required[str]
