# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal, TypeAlias

from ...._models import BaseModel

__all__ = [
    "ApplicationListResponse",
    "ApplicationListResponseItem",
    "ApplicationListResponseItemAuthMethod",
    "ApplicationListResponseItemPermission",
    "ApplicationListResponseItemUseCase",
]


class ApplicationListResponseItemAuthMethod(BaseModel):
    """Auth method summary for list endpoint."""

    display_name: str
    """Human-readable auth method name."""

    slug: str
    """Auth method identifier."""


class ApplicationListResponseItemPermission(BaseModel):
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


class ApplicationListResponseItemUseCase(BaseModel):
    """Lightweight use case for list endpoint."""

    display_name: str
    """Human-readable use case name."""

    slug: str
    """Use case identifier (e.g. casb, ces)."""


class ApplicationListResponseItem(BaseModel):
    """Application item in list response."""

    auth_methods: List[ApplicationListResponseItemAuthMethod]
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

    permissions: List[ApplicationListResponseItemPermission]
    """All permissions with severity."""

    slug: Literal["GITHUB", "GOOGLE_WORKSPACE", "MICROSOFT_INTERNAL", "SALESFORCE", "SLACK"]
    """Vendor identifier (e.g. microsoft_internal, google_workspace).

    - `GITHUB` - GITHUB
    - `GOOGLE_WORKSPACE` - GOOGLE_WORKSPACE
    - `MICROSOFT_INTERNAL` - MICROSOFT_INTERNAL
    - `SALESFORCE` - SALESFORCE
    - `SLACK` - SLACK
    """

    supported_environments: List[str]
    """Environments this vendor supports (standard, fedramp)."""

    use_cases: List[ApplicationListResponseItemUseCase]
    """Supported use cases."""


ApplicationListResponse: TypeAlias = List[ApplicationListResponseItem]
