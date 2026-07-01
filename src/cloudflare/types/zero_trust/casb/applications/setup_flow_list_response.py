# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import Literal, TypeAlias

from ....._models import BaseModel

__all__ = [
    "SetupFlowListResponse",
    "SetupFlowListResponseItem",
    "SetupFlowListResponseItemStep",
    "SetupFlowListResponseItemStepDynamicContent",
    "SetupFlowListResponseItemStepFormField",
    "SetupFlowListResponseItemAuthConfig",
]


class SetupFlowListResponseItemStepDynamicContent(BaseModel):
    """Dynamic content for instruction/form_input steps."""

    label: str
    """Display label."""

    type: Literal["copy_block", "external_link"]
    """Content type.

    - `copy_block` - copy_block
    - `external_link` - external_link
    """

    url_template: Optional[str] = None
    """URL template with {{ variable }} interpolation (for external_link)."""

    value_from: Optional[str] = None
    """Field path to get value from (for copy_block)."""


class SetupFlowListResponseItemStepFormField(BaseModel):
    """A form field within a form_input step."""

    label: str
    """Human-readable field label."""

    name: str
    """Field identifier (maps to credentials key)."""

    placeholder: Optional[str] = None
    """Placeholder text."""

    required: bool
    """Whether field is required."""

    supported_file_types: Optional[List[str]] = None
    """Allowed file extensions for file_upload type."""

    type: Literal["text", "password", "email", "file_upload"]
    """Field input type.

    - `text` - text
    - `password` - password
    - `email` - email
    - `file_upload` - file_upload
    """


class SetupFlowListResponseItemStep(BaseModel):
    """A single step in the setup flow. Polymorphic based on type."""

    type: Literal["component", "instruction", "form_input", "oauth_redirect"]
    """Step type.

    - `component` - component
    - `instruction` - instruction
    - `form_input` - form_input
    - `oauth_redirect` - oauth_redirect
    """

    component_id: Optional[str] = None
    """Component identifier (for component type)."""

    description: Optional[str] = None
    """Step description with markdown support."""

    dynamic_content: Optional[List[SetupFlowListResponseItemStepDynamicContent]] = None
    """Dynamic content blocks (for instruction/form_input)."""

    form_fields: Optional[List[SetupFlowListResponseItemStepFormField]] = None
    """Form fields (for form_input)."""

    is_required: Optional[bool] = None
    """Whether step is required (for form_input)."""

    parameters: Optional[Dict[str, str]] = None
    """Component parameters (for component type)."""

    title: Optional[str] = None
    """Step title (for instruction/form_input/oauth_redirect)."""


class SetupFlowListResponseItemAuthConfig(BaseModel):
    """OAuth configuration (present for OAuth-based flows)."""

    authorization_url: Optional[str] = None
    """Authorization URL for the requested environment."""

    client_id: Optional[str] = None
    """OAuth client ID."""

    requires_pkce: bool
    """Whether PKCE is required."""

    scopes: List[str]
    """OAuth scopes to request."""

    url_placeholders: List[str]
    """Placeholders in authorization URL that frontend must fill."""


class SetupFlowListResponseItem(BaseModel):
    """Setup flow for an application auth method."""

    id: str
    """Setup flow identifier."""

    default: bool
    """Whether this is the default auth method."""

    description: str
    """Flow description."""

    name: str
    """Human-readable flow name."""

    steps: List[SetupFlowListResponseItemStep]
    """Ordered list of setup steps."""

    supported_environments: List[str]
    """Environments this auth method supports (standard, fedramp)."""

    auth_config: Optional[SetupFlowListResponseItemAuthConfig] = None
    """OAuth configuration (present for OAuth-based flows)."""


SetupFlowListResponse: TypeAlias = List[SetupFlowListResponseItem]
