# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, cast

import httpx

from ....._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ....._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....._wrappers import ResultWrapper
from ....._base_client import (
    make_request_options,
)
from .....types.logs.control.retention import flag_create_params
from .....types.logs.control.retention.flag_get_response import FlagGetResponse
from .....types.logs.control.retention.flag_create_response import FlagCreateResponse

__all__ = ["FlagResource", "AsyncFlagResource"]


class FlagResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> FlagResourceWithRawResponse:
        return FlagResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FlagResourceWithStreamingResponse:
        return FlagResourceWithStreamingResponse(self)

    def create(
        self,
        zone_identifier: str,
        *,
        flag: bool,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FlagCreateResponse:
        """
        Updates log retention flag for Logpull API.

        Args:
          zone_identifier: Identifier

          flag: The log retention flag for Logpull API.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_identifier:
            raise ValueError(f"Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}")
        return self._post(
            f"/zones/{zone_identifier}/logs/control/retention/flag",
            body=maybe_transform({"flag": flag}, flag_create_params.FlagCreateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[FlagCreateResponse]._unwrapper,
            ),
            cast_to=cast(Type[FlagCreateResponse], ResultWrapper[FlagCreateResponse]),
        )

    def get(
        self,
        zone_identifier: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FlagGetResponse:
        """
        Gets log retention flag for Logpull API.

        Args:
          zone_identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_identifier:
            raise ValueError(f"Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}")
        return self._get(
            f"/zones/{zone_identifier}/logs/control/retention/flag",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[FlagGetResponse]._unwrapper,
            ),
            cast_to=cast(Type[FlagGetResponse], ResultWrapper[FlagGetResponse]),
        )


class AsyncFlagResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncFlagResourceWithRawResponse:
        return AsyncFlagResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFlagResourceWithStreamingResponse:
        return AsyncFlagResourceWithStreamingResponse(self)

    async def create(
        self,
        zone_identifier: str,
        *,
        flag: bool,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FlagCreateResponse:
        """
        Updates log retention flag for Logpull API.

        Args:
          zone_identifier: Identifier

          flag: The log retention flag for Logpull API.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_identifier:
            raise ValueError(f"Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}")
        return await self._post(
            f"/zones/{zone_identifier}/logs/control/retention/flag",
            body=await async_maybe_transform({"flag": flag}, flag_create_params.FlagCreateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[FlagCreateResponse]._unwrapper,
            ),
            cast_to=cast(Type[FlagCreateResponse], ResultWrapper[FlagCreateResponse]),
        )

    async def get(
        self,
        zone_identifier: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FlagGetResponse:
        """
        Gets log retention flag for Logpull API.

        Args:
          zone_identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_identifier:
            raise ValueError(f"Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}")
        return await self._get(
            f"/zones/{zone_identifier}/logs/control/retention/flag",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[FlagGetResponse]._unwrapper,
            ),
            cast_to=cast(Type[FlagGetResponse], ResultWrapper[FlagGetResponse]),
        )


class FlagResourceWithRawResponse:
    def __init__(self, flag: FlagResource) -> None:
        self._flag = flag

        self.create = to_raw_response_wrapper(
            flag.create,
        )
        self.get = to_raw_response_wrapper(
            flag.get,
        )


class AsyncFlagResourceWithRawResponse:
    def __init__(self, flag: AsyncFlagResource) -> None:
        self._flag = flag

        self.create = async_to_raw_response_wrapper(
            flag.create,
        )
        self.get = async_to_raw_response_wrapper(
            flag.get,
        )


class FlagResourceWithStreamingResponse:
    def __init__(self, flag: FlagResource) -> None:
        self._flag = flag

        self.create = to_streamed_response_wrapper(
            flag.create,
        )
        self.get = to_streamed_response_wrapper(
            flag.get,
        )


class AsyncFlagResourceWithStreamingResponse:
    def __init__(self, flag: AsyncFlagResource) -> None:
        self._flag = flag

        self.create = async_to_streamed_response_wrapper(
            flag.create,
        )
        self.get = async_to_streamed_response_wrapper(
            flag.get,
        )
