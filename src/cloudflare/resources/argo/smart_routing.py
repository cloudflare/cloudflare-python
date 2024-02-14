# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from ..._compat import cached_property

from ...types.argo import SmartRoutingUpdateResponse, SmartRoutingGetResponse

from typing_extensions import Literal

from ..._response import (
    to_raw_response_wrapper,
    async_to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_streamed_response_wrapper,
)

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ..._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ..._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._base_client import (
    SyncAPIClient,
    AsyncAPIClient,
    _merge_mappings,
    AsyncPaginator,
    make_request_options,
    HttpxBinaryResponseContent,
)
from ...types import shared_params
from ...types.argo import smart_routing_update_params
from ..._wrappers import ResultWrapper
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast

__all__ = ["SmartRouting", "AsyncSmartRouting"]


class SmartRouting(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SmartRoutingWithRawResponse:
        return SmartRoutingWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SmartRoutingWithStreamingResponse:
        return SmartRoutingWithStreamingResponse(self)

    def update(
        self,
        zone_id: str,
        *,
        value: Literal["on", "off"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SmartRoutingUpdateResponse:
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
            SmartRoutingUpdateResponse,
            self._patch(
                f"/zones/{zone_id}/argo/smart_routing",
                body=maybe_transform({"value": value}, smart_routing_update_params.SmartRoutingUpdateParams),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[SmartRoutingUpdateResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def get(
        self,
        zone_id: str,
        *,
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
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[SmartRoutingGetResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class AsyncSmartRouting(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSmartRoutingWithRawResponse:
        return AsyncSmartRoutingWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSmartRoutingWithStreamingResponse:
        return AsyncSmartRoutingWithStreamingResponse(self)

    async def update(
        self,
        zone_id: str,
        *,
        value: Literal["on", "off"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SmartRoutingUpdateResponse:
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
            SmartRoutingUpdateResponse,
            await self._patch(
                f"/zones/{zone_id}/argo/smart_routing",
                body=maybe_transform({"value": value}, smart_routing_update_params.SmartRoutingUpdateParams),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[SmartRoutingUpdateResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def get(
        self,
        zone_id: str,
        *,
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
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[SmartRoutingGetResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class SmartRoutingWithRawResponse:
    def __init__(self, smart_routing: SmartRouting) -> None:
        self._smart_routing = smart_routing

        self.update = to_raw_response_wrapper(
            smart_routing.update,
        )
        self.get = to_raw_response_wrapper(
            smart_routing.get,
        )


class AsyncSmartRoutingWithRawResponse:
    def __init__(self, smart_routing: AsyncSmartRouting) -> None:
        self._smart_routing = smart_routing

        self.update = async_to_raw_response_wrapper(
            smart_routing.update,
        )
        self.get = async_to_raw_response_wrapper(
            smart_routing.get,
        )


class SmartRoutingWithStreamingResponse:
    def __init__(self, smart_routing: SmartRouting) -> None:
        self._smart_routing = smart_routing

        self.update = to_streamed_response_wrapper(
            smart_routing.update,
        )
        self.get = to_streamed_response_wrapper(
            smart_routing.get,
        )


class AsyncSmartRoutingWithStreamingResponse:
    def __init__(self, smart_routing: AsyncSmartRouting) -> None:
        self._smart_routing = smart_routing

        self.update = async_to_streamed_response_wrapper(
            smart_routing.update,
        )
        self.get = async_to_streamed_response_wrapper(
            smart_routing.get,
        )
