# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["ApplicationListResponse", "AuthMethod", "Permission", "UseCase"]


class AuthMethod(BaseModel):
    """Auth method summary for list endpoint."""

    id: str
    """Auth method identifier."""

    display_name: str
    """Human-readable auth method name."""


class Permission(BaseModel):
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


class UseCase(BaseModel):
    """Lightweight use case for list endpoint."""

    id: str
    """Use case identifier (e.g. casb, ces)."""

    display_name: str
    """Human-readable use case name."""


class ApplicationListResponse(BaseModel):
    """Application item in list response."""

    id: Literal[
        "ANTHROPIC",
        "AWS",
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
        "SERVICENOW",
        "SLACK",
    ]
    """Vendor identifier (e.g. microsoft_internal, google_workspace).

    - `ANTHROPIC` - ANTHROPIC
    - `AWS` - AWS
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
    - `SERVICENOW` - SERVICENOW
    - `SLACK` - SLACK
    """

    auth_methods: List[AuthMethod]
    """Available auth methods."""

    category: str
    """Vendor category (e.g. Productivity, AI)."""

    description: str
    """Brief description of the integration."""

    display_name: str
    """Human-readable vendor name."""

    dlp_enabled: bool
    """Whether DLP scanning is supported."""

    logo: Optional[str] = None
    """Logo path."""

    permissions: List[Permission]
    """All permissions with severity."""

    supported_environments: List[str]
    """Environments this vendor supports (standard, fedramp)."""

    use_cases: List[UseCase]
    """Supported use cases."""
