# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Optional
from typing_extensions import Literal, Required, TypedDict

from ...._types import SequenceNotStr

__all__ = ["IntegrationCreateParams"]


class IntegrationCreateParams(TypedDict, total=False):
    account_id: Required[str]

    application: Required[
        Literal[
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
    ]
    """Vendor/application slug (e.g., GOOGLE_WORKSPACE).

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

    credentials: Required[Dict[str, object]]
    """Credentials for the integration."""

    name: Required[str]
    """Name of the integration."""

    auth_method: Optional[str]
    """Authentication method slug (uses default if omitted)."""

    dlp_profiles: SequenceNotStr[str]
    """List of DLP profile IDs to associate."""

    permissions: SequenceNotStr[str]
    """List of permission scopes (uses policy defaults if empty)."""

    use_cases: List[Literal["casb", "ces", "auto_remediation"]]
    """
    List of use case or feature slugs to enroll (e.g., ['casb', 'ces',
    'auto_remediation']).
    """
