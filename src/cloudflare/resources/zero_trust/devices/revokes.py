# File generated from our OpenAPI spec by Stainless.

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
from ....types.zero_trust.devices import RevokeCreateResponse, revoke_create_params

__all__ = ["Revokes", "AsyncRevokes"]


class Revokes(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RevokesWithRawResponse:
        return RevokesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RevokesWithStreamingResponse:
        return RevokesWithStreamingResponse(self)

    def create(
        self,
        *,
        account_id: object,
        body: List[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[RevokeCreateResponse]:
        """
        Revokes a list of devices.

        Args:
          body: A list of device ids to revoke.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return cast(
            Optional[RevokeCreateResponse],
            self._post(
                f"/accounts/{account_id}/devices/revoke",
                body=maybe_transform(body, revoke_create_params.RevokeCreateParams),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[RevokeCreateResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class AsyncRevokes(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRevokesWithRawResponse:
        return AsyncRevokesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRevokesWithStreamingResponse:
        return AsyncRevokesWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_id: object,
        body: List[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[RevokeCreateResponse]:
        """
        Revokes a list of devices.

        Args:
          body: A list of device ids to revoke.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return cast(
            Optional[RevokeCreateResponse],
            await self._post(
                f"/accounts/{account_id}/devices/revoke",
                body=await async_maybe_transform(body, revoke_create_params.RevokeCreateParams),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[RevokeCreateResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class RevokesWithRawResponse:
    def __init__(self, revokes: Revokes) -> None:
        self._revokes = revokes

        self.create = to_raw_response_wrapper(
            revokes.create,
        )


class AsyncRevokesWithRawResponse:
    def __init__(self, revokes: AsyncRevokes) -> None:
        self._revokes = revokes

        self.create = async_to_raw_response_wrapper(
            revokes.create,
        )


class RevokesWithStreamingResponse:
    def __init__(self, revokes: Revokes) -> None:
        self._revokes = revokes

        self.create = to_streamed_response_wrapper(
            revokes.create,
        )


class AsyncRevokesWithStreamingResponse:
    def __init__(self, revokes: AsyncRevokes) -> None:
        self._revokes = revokes

        self.create = async_to_streamed_response_wrapper(
            revokes.create,
        )
