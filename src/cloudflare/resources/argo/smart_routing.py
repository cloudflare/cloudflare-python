# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, cast
from typing_extensions import Literal

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._wrappers import ResultWrapper
from ...types.argo import smart_routing_edit_params
from ..._base_client import make_request_options
from ...types.argo.smart_routing_get_response import SmartRoutingGetResponse
from ...types.argo.smart_routing_edit_response import SmartRoutingEditResponse

__all__ = ["SmartRoutingResource", "AsyncSmartRoutingResource"]


class SmartRoutingResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SmartRoutingResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return SmartRoutingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SmartRoutingResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return SmartRoutingResourceWithStreamingResponse(self)

    def edit(
        self,
        *,
        zone_id: str,
        value: Literal["on", "off"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SmartRoutingEditResponse:
        """
        Updates enablement of Argo Smart Routing.

        Args:
          zone_id: Identifier

          value: Enables Argo Smart Routing.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return cast(
            SmartRoutingEditResponse,
            self._patch(
                f"/zones/{zone_id}/argo/smart_routing",
                body=maybe_transform({"value": value}, smart_routing_edit_params.SmartRoutingEditParams),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper[SmartRoutingEditResponse]._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[SmartRoutingEditResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def get(
        self,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SmartRoutingGetResponse:
        """
        Get Argo Smart Routing setting

        Args:
          zone_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return cast(
            SmartRoutingGetResponse,
            self._get(
                f"/zones/{zone_id}/argo/smart_routing",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper[SmartRoutingGetResponse]._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[SmartRoutingGetResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class AsyncSmartRoutingResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSmartRoutingResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSmartRoutingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSmartRoutingResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncSmartRoutingResourceWithStreamingResponse(self)

    async def edit(
        self,
        *,
        zone_id: str,
        value: Literal["on", "off"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SmartRoutingEditResponse:
        """
        Updates enablement of Argo Smart Routing.

        Args:
          zone_id: Identifier

          value: Enables Argo Smart Routing.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return cast(
            SmartRoutingEditResponse,
            await self._patch(
                f"/zones/{zone_id}/argo/smart_routing",
                body=await async_maybe_transform({"value": value}, smart_routing_edit_params.SmartRoutingEditParams),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper[SmartRoutingEditResponse]._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[SmartRoutingEditResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def get(
        self,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SmartRoutingGetResponse:
        """
        Get Argo Smart Routing setting

        Args:
          zone_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return cast(
            SmartRoutingGetResponse,
            await self._get(
                f"/zones/{zone_id}/argo/smart_routing",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper[SmartRoutingGetResponse]._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[SmartRoutingGetResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class SmartRoutingResourceWithRawResponse:
    def __init__(self, smart_routing: SmartRoutingResource) -> None:
        self._smart_routing = smart_routing

        self.edit = to_raw_response_wrapper(
            smart_routing.edit,
        )
        self.get = to_raw_response_wrapper(
            smart_routing.get,
        )


class AsyncSmartRoutingResourceWithRawResponse:
    def __init__(self, smart_routing: AsyncSmartRoutingResource) -> None:
        self._smart_routing = smart_routing

        self.edit = async_to_raw_response_wrapper(
            smart_routing.edit,
        )
        self.get = async_to_raw_response_wrapper(
            smart_routing.get,
        )


class SmartRoutingResourceWithStreamingResponse:
    def __init__(self, smart_routing: SmartRoutingResource) -> None:
        self._smart_routing = smart_routing

        self.edit = to_streamed_response_wrapper(
            smart_routing.edit,
        )
        self.get = to_streamed_response_wrapper(
            smart_routing.get,
        )


class AsyncSmartRoutingResourceWithStreamingResponse:
    def __init__(self, smart_routing: AsyncSmartRoutingResource) -> None:
        self._smart_routing = smart_routing

        self.edit = async_to_streamed_response_wrapper(
            smart_routing.edit,
        )
        self.get = async_to_streamed_response_wrapper(
            smart_routing.get,
        )
