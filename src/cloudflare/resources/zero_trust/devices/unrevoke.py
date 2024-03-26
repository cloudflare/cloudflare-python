# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, List, Optional, cast

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
from ...._base_client import (
    make_request_options,
)
from ....types.zero_trust.devices import UnrevokeCreateResponse, unrevoke_create_params

__all__ = ["Unrevoke", "AsyncUnrevoke"]


class Unrevoke(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> UnrevokeWithRawResponse:
        return UnrevokeWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> UnrevokeWithStreamingResponse:
        return UnrevokeWithStreamingResponse(self)

    def create(
        self,
        *,
        account_id: str,
        body: List[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[UnrevokeCreateResponse]:
        """
        Unrevokes a list of devices.

        Args:
          body: A list of device ids to unrevoke.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return cast(
            Optional[UnrevokeCreateResponse],
            self._post(
                f"/accounts/{account_id}/devices/unrevoke",
                body=maybe_transform(body, unrevoke_create_params.UnrevokeCreateParams),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[UnrevokeCreateResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class AsyncUnrevoke(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncUnrevokeWithRawResponse:
        return AsyncUnrevokeWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncUnrevokeWithStreamingResponse:
        return AsyncUnrevokeWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_id: str,
        body: List[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[UnrevokeCreateResponse]:
        """
        Unrevokes a list of devices.

        Args:
          body: A list of device ids to unrevoke.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return cast(
            Optional[UnrevokeCreateResponse],
            await self._post(
                f"/accounts/{account_id}/devices/unrevoke",
                body=await async_maybe_transform(body, unrevoke_create_params.UnrevokeCreateParams),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[UnrevokeCreateResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class UnrevokeWithRawResponse:
    def __init__(self, unrevoke: Unrevoke) -> None:
        self._unrevoke = unrevoke

        self.create = to_raw_response_wrapper(
            unrevoke.create,
        )


class AsyncUnrevokeWithRawResponse:
    def __init__(self, unrevoke: AsyncUnrevoke) -> None:
        self._unrevoke = unrevoke

        self.create = async_to_raw_response_wrapper(
            unrevoke.create,
        )


class UnrevokeWithStreamingResponse:
    def __init__(self, unrevoke: Unrevoke) -> None:
        self._unrevoke = unrevoke

        self.create = to_streamed_response_wrapper(
            unrevoke.create,
        )


class AsyncUnrevokeWithStreamingResponse:
    def __init__(self, unrevoke: AsyncUnrevoke) -> None:
        self._unrevoke = unrevoke

        self.create = async_to_streamed_response_wrapper(
            unrevoke.create,
        )
