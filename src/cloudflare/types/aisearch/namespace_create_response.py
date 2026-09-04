# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = [
    "NamespaceCreateResponse",
    "PublicEndpointParams",
    "PublicEndpointParamsChatCompletionsEndpoint",
    "PublicEndpointParamsMcp",
    "PublicEndpointParamsRateLimit",
    "PublicEndpointParamsSearchEndpoint",
]


class PublicEndpointParamsChatCompletionsEndpoint(BaseModel):
    disabled: Optional[bool] = None
    """Disable chat completions endpoint for this public endpoint"""


class PublicEndpointParamsMcp(BaseModel):
    description: Optional[str] = None

    disabled: Optional[bool] = None
    """Disable MCP endpoint for this public endpoint"""


class PublicEndpointParamsRateLimit(BaseModel):
    period_ms: Optional[int] = None

    requests: Optional[int] = None

    technique: Optional[Literal["fixed", "sliding"]] = None


class PublicEndpointParamsSearchEndpoint(BaseModel):
    disabled: Optional[bool] = None
    """Disable search endpoint for this public endpoint"""


class PublicEndpointParams(BaseModel):
    authorized_hosts: Optional[List[str]] = None

    chat_completions_endpoint: Optional[PublicEndpointParamsChatCompletionsEndpoint] = None

    custom_domains: Optional[List[str]] = None
    """Custom domain hostnames that alias this public endpoint.

    GET and create responses return the current set; on update (PUT) this field is
    only echoed back when supplied in the request body, otherwise it is null (omit
    it to leave domains unchanged).
    """

    default_domain_enabled: Optional[bool] = None
    """
    When false, the instance is reachable only via a registered custom domain and
    the default <public_endpoint_id>.search.ai.cloudflare.com host returns 404.
    Requires at least one custom domain. Defaults to true. public_endpoint_params is
    replaced wholesale on update, so resend default_domain_enabled on every update
    to keep the default host off — omitting it resets to true.
    """

    enabled: Optional[bool] = None

    instances_allowed: Optional[List[str]] = None
    """Instance IDs exposed through the namespace public endpoint.

    Empty means nothing is searchable. Every ID must be an existing instance in this
    namespace, and the list cannot exceed the account's multi-instance search limit.
    """

    mcp: Optional[PublicEndpointParamsMcp] = None

    rate_limit: Optional[PublicEndpointParamsRateLimit] = None

    search_endpoint: Optional[PublicEndpointParamsSearchEndpoint] = None


class NamespaceCreateResponse(BaseModel):
    created_at: datetime

    name: str

    description: Optional[str] = None
    """Optional description for the namespace. Max 256 characters."""

    public_endpoint_id: Optional[str] = None

    public_endpoint_params: Optional[PublicEndpointParams] = None
