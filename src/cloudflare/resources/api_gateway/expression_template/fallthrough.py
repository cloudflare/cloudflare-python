# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Type, cast

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._wrappers import ResultWrapper
from ...._base_client import make_request_options
from ....types.api_gateway.expression_template import fallthrough_create_params
from ....types.api_gateway.expression_template.fallthrough_create_response import FallthroughCreateResponse

__all__ = ["FallthroughResource", "AsyncFallthroughResource"]


class FallthroughResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> FallthroughResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return FallthroughResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FallthroughResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return FallthroughResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        zone_id: str,
        hosts: List[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FallthroughCreateResponse:
        """
        Generate fallthrough WAF expression template from a set of API hosts

        Args:
          zone_id: Identifier

          hosts: List of hosts to be targeted in the expression

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._post(
            f"/zones/{zone_id}/api_gateway/expression-template/fallthrough",
            body=maybe_transform({"hosts": hosts}, fallthrough_create_params.FallthroughCreateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[FallthroughCreateResponse]._unwrapper,
            ),
            cast_to=cast(Type[FallthroughCreateResponse], ResultWrapper[FallthroughCreateResponse]),
        )


class AsyncFallthroughResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncFallthroughResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncFallthroughResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFallthroughResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncFallthroughResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        zone_id: str,
        hosts: List[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FallthroughCreateResponse:
        """
        Generate fallthrough WAF expression template from a set of API hosts

        Args:
          zone_id: Identifier

          hosts: List of hosts to be targeted in the expression

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._post(
            f"/zones/{zone_id}/api_gateway/expression-template/fallthrough",
            body=await async_maybe_transform({"hosts": hosts}, fallthrough_create_params.FallthroughCreateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[FallthroughCreateResponse]._unwrapper,
            ),
            cast_to=cast(Type[FallthroughCreateResponse], ResultWrapper[FallthroughCreateResponse]),
        )


class FallthroughResourceWithRawResponse:
    def __init__(self, fallthrough: FallthroughResource) -> None:
        self._fallthrough = fallthrough

        self.create = to_raw_response_wrapper(
            fallthrough.create,
        )


class AsyncFallthroughResourceWithRawResponse:
    def __init__(self, fallthrough: AsyncFallthroughResource) -> None:
        self._fallthrough = fallthrough

        self.create = async_to_raw_response_wrapper(
            fallthrough.create,
        )


class FallthroughResourceWithStreamingResponse:
    def __init__(self, fallthrough: FallthroughResource) -> None:
        self._fallthrough = fallthrough

        self.create = to_streamed_response_wrapper(
            fallthrough.create,
        )


class AsyncFallthroughResourceWithStreamingResponse:
    def __init__(self, fallthrough: AsyncFallthroughResource) -> None:
        self._fallthrough = fallthrough

        self.create = async_to_streamed_response_wrapper(
            fallthrough.create,
        )
