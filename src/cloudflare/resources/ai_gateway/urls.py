# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, cast

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._wrappers import ResultWrapper
from ..._base_client import make_request_options
from ...types.ai_gateway.url_get_response import URLGetResponse

__all__ = ["URLsResource", "AsyncURLsResource"]


class URLsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> URLsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return URLsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> URLsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return URLsResourceWithStreamingResponse(self)

    def get(
        self,
        provider: str,
        *,
        account_id: str,
        gateway_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> str:
        """
        Get Gateway URL

        Args:
          gateway_id: gateway id

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not gateway_id:
            raise ValueError(f"Expected a non-empty value for `gateway_id` but received {gateway_id!r}")
        if not provider:
            raise ValueError(f"Expected a non-empty value for `provider` but received {provider!r}")
        return self._get(
            f"/accounts/{account_id}/ai-gateway/gateways/{gateway_id}/url/{provider}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[URLGetResponse]._unwrapper,
            ),
            cast_to=cast(Type[str], ResultWrapper[str]),
        )


class AsyncURLsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncURLsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncURLsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncURLsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncURLsResourceWithStreamingResponse(self)

    async def get(
        self,
        provider: str,
        *,
        account_id: str,
        gateway_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> str:
        """
        Get Gateway URL

        Args:
          gateway_id: gateway id

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not gateway_id:
            raise ValueError(f"Expected a non-empty value for `gateway_id` but received {gateway_id!r}")
        if not provider:
            raise ValueError(f"Expected a non-empty value for `provider` but received {provider!r}")
        return await self._get(
            f"/accounts/{account_id}/ai-gateway/gateways/{gateway_id}/url/{provider}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[URLGetResponse]._unwrapper,
            ),
            cast_to=cast(Type[str], ResultWrapper[str]),
        )


class URLsResourceWithRawResponse:
    def __init__(self, urls: URLsResource) -> None:
        self._urls = urls

        self.get = to_raw_response_wrapper(
            urls.get,
        )


class AsyncURLsResourceWithRawResponse:
    def __init__(self, urls: AsyncURLsResource) -> None:
        self._urls = urls

        self.get = async_to_raw_response_wrapper(
            urls.get,
        )


class URLsResourceWithStreamingResponse:
    def __init__(self, urls: URLsResource) -> None:
        self._urls = urls

        self.get = to_streamed_response_wrapper(
            urls.get,
        )


class AsyncURLsResourceWithStreamingResponse:
    def __init__(self, urls: AsyncURLsResource) -> None:
        self._urls = urls

        self.get = async_to_streamed_response_wrapper(
            urls.get,
        )
