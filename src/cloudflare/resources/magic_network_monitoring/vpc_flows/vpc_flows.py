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

__all__ = ["VpcFlowsResource", "AsyncVpcFlowsResource"]


class VpcFlowsResource(SyncAPIResource):
    @cached_property
    def tokens(self) -> TokensResource:
        return TokensResource(self._client)

    @cached_property
    def with_raw_response(self) -> VpcFlowsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return VpcFlowsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> VpcFlowsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return VpcFlowsResourceWithStreamingResponse(self)


class AsyncVpcFlowsResource(AsyncAPIResource):
    @cached_property
    def tokens(self) -> AsyncTokensResource:
        return AsyncTokensResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncVpcFlowsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncVpcFlowsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncVpcFlowsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncVpcFlowsResourceWithStreamingResponse(self)


class VpcFlowsResourceWithRawResponse:
    def __init__(self, vpc_flows: VpcFlowsResource) -> None:
        self._vpc_flows = vpc_flows

    @cached_property
    def tokens(self) -> TokensResourceWithRawResponse:
        return TokensResourceWithRawResponse(self._vpc_flows.tokens)


class AsyncVpcFlowsResourceWithRawResponse:
    def __init__(self, vpc_flows: AsyncVpcFlowsResource) -> None:
        self._vpc_flows = vpc_flows

    @cached_property
    def tokens(self) -> AsyncTokensResourceWithRawResponse:
        return AsyncTokensResourceWithRawResponse(self._vpc_flows.tokens)


class VpcFlowsResourceWithStreamingResponse:
    def __init__(self, vpc_flows: VpcFlowsResource) -> None:
        self._vpc_flows = vpc_flows

    @cached_property
    def tokens(self) -> TokensResourceWithStreamingResponse:
        return TokensResourceWithStreamingResponse(self._vpc_flows.tokens)


class AsyncVpcFlowsResourceWithStreamingResponse:
    def __init__(self, vpc_flows: AsyncVpcFlowsResource) -> None:
        self._vpc_flows = vpc_flows

    @cached_property
    def tokens(self) -> AsyncTokensResourceWithStreamingResponse:
        return AsyncTokensResourceWithStreamingResponse(self._vpc_flows.tokens)
