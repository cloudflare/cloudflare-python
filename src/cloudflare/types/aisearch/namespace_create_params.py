# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

from ..._types import SequenceNotStr

__all__ = [
    "NamespaceCreateParams",
    "PublicEndpointParams",
    "PublicEndpointParamsChatCompletionsEndpoint",
    "PublicEndpointParamsMcp",
    "PublicEndpointParamsRateLimit",
    "PublicEndpointParamsSearchEndpoint",
]


class NamespaceCreateParams(TypedDict, total=False):
    account_id: Required[str]

    name: Required[str]

    description: Optional[str]
    """Optional description for the namespace. Max 256 characters."""

    public_endpoint_params: PublicEndpointParams


class PublicEndpointParamsChatCompletionsEndpoint(TypedDict, total=False):
    disabled: bool
    """Disable chat completions endpoint for this public endpoint"""


class PublicEndpointParamsMcp(TypedDict, total=False):
    description: str

    disabled: bool
    """Disable MCP endpoint for this public endpoint"""


class PublicEndpointParamsRateLimit(TypedDict, total=False):
    period_ms: int

    requests: int

    technique: Literal["fixed", "sliding"]


class PublicEndpointParamsSearchEndpoint(TypedDict, total=False):
    disabled: bool
    """Disable search endpoint for this public endpoint"""


class PublicEndpointParams(TypedDict, total=False):
    authorized_hosts: SequenceNotStr[str]

    chat_completions_endpoint: PublicEndpointParamsChatCompletionsEndpoint

    custom_domains: Optional[SequenceNotStr[str]]
    """Custom domain hostnames that alias this public endpoint.

    GET and create responses return the current set; on update (PUT) this field is
    only echoed back when supplied in the request body, otherwise it is null (omit
    it to leave domains unchanged).
    """

    default_domain_enabled: bool
    """
    When false, the instance is reachable only via a registered custom domain and
    the default <public_endpoint_id>.search.ai.cloudflare.com host returns 404.
    Requires at least one custom domain. Defaults to true. public_endpoint_params is
    replaced wholesale on update, so resend default_domain_enabled on every update
    to keep the default host off — omitting it resets to true.
    """

    enabled: bool

    instances_allowed: SequenceNotStr[str]
    """Instance IDs exposed through the namespace public endpoint.

    Empty means nothing is searchable. Every ID must be an existing instance in this
    namespace, and the list cannot exceed the account's multi-instance search limit.
    """

    mcp: PublicEndpointParamsMcp

    rate_limit: PublicEndpointParamsRateLimit

    search_endpoint: PublicEndpointParamsSearchEndpoint
