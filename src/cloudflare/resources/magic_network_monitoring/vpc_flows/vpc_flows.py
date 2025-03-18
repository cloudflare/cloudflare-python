# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .tokens import (
    TokensResource,
    AsyncTokensResource,
    TokensResourceWithRawResponse,
    AsyncTokensResourceWithRawResponse,
    TokensResourceWithStreamingResponse,
    AsyncTokensResourceWithStreamingResponse,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["VPCFlowsResource", "AsyncVPCFlowsResource"]


class VPCFlowsResource(SyncAPIResource):
    @cached_property
    def tokens(self) -> TokensResource:
        return TokensResource(self._client)

    @cached_property
    def with_raw_response(self) -> VPCFlowsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return VPCFlowsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> VPCFlowsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return VPCFlowsResourceWithStreamingResponse(self)


class AsyncVPCFlowsResource(AsyncAPIResource):
    @cached_property
    def tokens(self) -> AsyncTokensResource:
        return AsyncTokensResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncVPCFlowsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncVPCFlowsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncVPCFlowsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncVPCFlowsResourceWithStreamingResponse(self)


class VPCFlowsResourceWithRawResponse:
    def __init__(self, vpc_flows: VPCFlowsResource) -> None:
        self._vpc_flows = vpc_flows

    @cached_property
    def tokens(self) -> TokensResourceWithRawResponse:
        return TokensResourceWithRawResponse(self._vpc_flows.tokens)


class AsyncVPCFlowsResourceWithRawResponse:
    def __init__(self, vpc_flows: AsyncVPCFlowsResource) -> None:
        self._vpc_flows = vpc_flows

    @cached_property
    def tokens(self) -> AsyncTokensResourceWithRawResponse:
        return AsyncTokensResourceWithRawResponse(self._vpc_flows.tokens)


class VPCFlowsResourceWithStreamingResponse:
    def __init__(self, vpc_flows: VPCFlowsResource) -> None:
        self._vpc_flows = vpc_flows

    @cached_property
    def tokens(self) -> TokensResourceWithStreamingResponse:
        return TokensResourceWithStreamingResponse(self._vpc_flows.tokens)


class AsyncVPCFlowsResourceWithStreamingResponse:
    def __init__(self, vpc_flows: AsyncVPCFlowsResource) -> None:
        self._vpc_flows = vpc_flows

    @cached_property
    def tokens(self) -> AsyncTokensResourceWithStreamingResponse:
        return AsyncTokensResourceWithStreamingResponse(self._vpc_flows.tokens)
