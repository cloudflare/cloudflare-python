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

    display_name: str
    """Human-readable auth method name."""

    is_default: bool
    """Whether this is the default auth method."""

    slug: str
    """Auth method identifier."""

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

    description: str
    """Feature description."""

    display_name: str
    """Human-readable feature name."""

    scopes: List[UseCaseFeatureScope]
    """Additional scopes when feature is enabled."""

    slug: str
    """Feature identifier."""


class UseCase(BaseModel):
    """Full use case with scopes and features for detail endpoint."""

    base_scopes: List[UseCaseBaseScope]
    """Scopes always required for this use case."""

    description: str
    """Use case description."""

    display_name: str
    """Human-readable use case name."""

    features: List[UseCaseFeature]
    """Optional features with extra scopes."""

    slug: str
    """Use case identifier."""


class ApplicationGetResponse(BaseModel):
    """Full application detail for onboarding UI."""

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

    slug: Literal["GITHUB", "GOOGLE_WORKSPACE", "MICROSOFT_INTERNAL", "SALESFORCE", "SLACK"]
    """Vendor identifier.

    - `GITHUB` - GITHUB
    - `GOOGLE_WORKSPACE` - GOOGLE_WORKSPACE
    - `MICROSOFT_INTERNAL` - MICROSOFT_INTERNAL
    - `SALESFORCE` - SALESFORCE
    - `SLACK` - SLACK
    """

    use_cases: List[UseCase]
    """Use cases with full scope details."""
