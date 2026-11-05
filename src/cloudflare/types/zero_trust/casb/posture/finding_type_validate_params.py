# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from ....._types import SequenceNotStr

__all__ = ["FindingTypeValidateParams"]


class FindingTypeValidateParams(TypedDict, total=False):
    account_id: Required[str]

    applies_to_all_integrations: Required[bool]
    """
    When true, this finding type applies to every current and future integration of
    the vendor.
    """

    asset_class: Required[str]
    """Asset class this finding type applies to (PascalCase, e.g. GoogleWorkspaceFile)"""

    asset_vendor: Required[
        Literal[
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
            "ZOOM",
        ]
    ]
    """
    Canonical vendor enum for the platform whose assets this finding type evaluates.
    """

    description: Required[str]
    """Human-readable description of the finding type.

    Cannot be empty. Maximum 4096 characters.
    """

    expression: Required[str]
    """Rego expression body for the policy.

    `package cloudflare.casb.custom` and `import rego.v1` are added automatically.
    Do not include package or import declarations. This field cannot be changed
    after creation. Maximum 4096 characters.
    """

    name: Required[str]
    """Human-readable name for the finding type. Maximum 256 characters."""

    severity: Required[Literal["Critical", "High", "Medium", "Low"]]
    """Default severity used when no integration-specific severity override exists."""

    integration_ids: SequenceNotStr[str]
    """
    Required and non-empty when applies_to_all_integrations is false; omit when it
    is true.
    """
