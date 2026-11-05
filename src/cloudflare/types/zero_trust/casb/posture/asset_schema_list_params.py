# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["AssetSchemaListParams"]


class AssetSchemaListParams(TypedDict, total=False):
    account_id: Required[str]

    vendor: Literal[
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
        "MICROSOFT",
        "OPENAI",
        "SALESFORCE",
        "SERVICENOW",
        "SLACK",
        "WORKDAY",
        "ZOOM",
    ]
    """Restrict the result to a single vendor. Unknown values return 400."""
