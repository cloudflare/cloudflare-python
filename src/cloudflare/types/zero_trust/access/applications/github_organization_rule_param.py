# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ....._utils import PropertyInfo

__all__ = ["GitHubOrganizationRuleParam", "GitHubOrganization"]


class GitHubOrganization(TypedDict, total=False):
    identity_provider_id: Required[str]
    """The ID of your Github identity provider."""

    name: Required[str]
    """The name of the organization."""

    team: str
    """The name of the team"""


class GitHubOrganizationRuleParam(TypedDict, total=False):
    github_organization: Required[Annotated[GitHubOrganization, PropertyInfo(alias="github-organization")]]
