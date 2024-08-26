# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.


from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["GitHubOrganizationRule", "GitHubOrganization"]


class GitHubOrganization(BaseModel):
    connection_id: str
    """The ID of your Github identity provider."""

    name: str
    """The name of the organization."""


class GitHubOrganizationRule(BaseModel):
    github_organization: GitHubOrganization = FieldInfo(alias="github-organization")
