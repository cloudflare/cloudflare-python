# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ....._models import BaseModel

__all__ = ["GitHubOrganizationRule", "GitHubOrganization"]


class GitHubOrganization(BaseModel):
    identity_provider_id: str
    """The ID of your Github identity provider."""

    name: str
    """The name of the organization."""

    team: Optional[str] = None
    """The name of the team"""


class GitHubOrganizationRule(BaseModel):
    github_organization: GitHubOrganization = FieldInfo(alias="github-organization")
