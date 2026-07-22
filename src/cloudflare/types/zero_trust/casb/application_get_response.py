# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = [
    "ApplicationGetResponse",
    "AuthMethod",
    "UseCase",
    "UseCaseBaseScope",
    "UseCaseFeature",
    "UseCaseFeatureScope",
]


class AuthMethod(BaseModel):
    """Authentication method available for a vendor."""

    id: str
    """Auth method identifier."""

    display_name: str
    """Human-readable auth method name."""

    is_default: bool
    """Whether this is the default auth method."""

    supported_environments: List[str]
    """Environments this auth method supports."""


class UseCaseBaseScope(BaseModel):
    """Permission/scope with severity for display."""

    display_name: str
    """Human-readable permission name."""

    scope: str
    """Vendor-native scope identifier."""

    severity: Literal["low", "medium", "high", "critical"]
    """Permission sensitivity level.

    - `low` - low
    - `medium` - medium
    - `high` - high
    - `critical` - critical
    """


class UseCaseFeatureScope(BaseModel):
    """Permission/scope with severity for display."""

    display_name: str
    """Human-readable permission name."""

    scope: str
    """Vendor-native scope identifier."""

    severity: Literal["low", "medium", "high", "critical"]
    """Permission sensitivity level.

    - `low` - low
    - `medium` - medium
    - `high` - high
    - `critical` - critical
    """


class UseCaseFeature(BaseModel):
    """A feature with its additional scopes."""

    id: str
    """Feature identifier."""

    description: str
    """Feature description."""

    display_name: str
    """Human-readable feature name."""

    scopes: List[UseCaseFeatureScope]
    """Additional scopes when feature is enabled."""


class UseCase(BaseModel):
    """Full use case with scopes and features for detail endpoint."""

    id: str
    """Use case identifier."""

    base_scopes: List[UseCaseBaseScope]
    """Scopes always required for this use case."""

    description: str
    """Use case description."""

    display_name: str
    """Human-readable use case name."""

    features: List[UseCaseFeature]
    """Optional features with extra scopes."""


class ApplicationGetResponse(BaseModel):
    """Full application detail for onboarding UI."""

    id: Literal[
        "ANTHROPIC",
        "BITBUCKET",
        "BOX",
        "CONFLUENCE",
        "DROPBOX",
        "GITHUB",
        "GOOGLE_CLOUD_PLATFORM",
        "GOOGLE_WORKSPACE",
        "JIRA",
        "MICROSOFT_INTERNAL",
        "OPENAI",
        "SALESFORCE",
        "SLACK",
    ]
    """Vendor identifier.

    - `ANTHROPIC` - ANTHROPIC
    - `BITBUCKET` - BITBUCKET
    - `BOX` - BOX
    - `CONFLUENCE` - CONFLUENCE
    - `DROPBOX` - DROPBOX
    - `GITHUB` - GITHUB
    - `GOOGLE_CLOUD_PLATFORM` - GOOGLE_CLOUD_PLATFORM
    - `GOOGLE_WORKSPACE` - GOOGLE_WORKSPACE
    - `JIRA` - JIRA
    - `MICROSOFT_INTERNAL` - MICROSOFT_INTERNAL
    - `OPENAI` - OPENAI
    - `SALESFORCE` - SALESFORCE
    - `SLACK` - SLACK
    """

    auth_methods: List[AuthMethod]
    """Available authentication methods."""

    category: str
    """Vendor category."""

    description: str
    """Brief description."""

    display_name: str
    """Human-readable vendor name."""

    dlp_enabled: bool
    """Whether DLP scanning is supported."""

    instructions: Optional[str] = None
    """Setup instructions for the user."""

    logo: Optional[str] = None
    """Logo path."""

    use_cases: List[UseCase]
    """Use cases with full scope details."""
