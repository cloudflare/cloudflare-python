# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Type, Optional, cast

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
from ..._base_client import (
    make_request_options,
)
from ...types.custom_ns import VerifyUpdateResponse

__all__ = ["Verifies", "AsyncVerifies"]


class Verifies(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> VerifiesWithRawResponse:
        return VerifiesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> VerifiesWithStreamingResponse:
        return VerifiesWithStreamingResponse(self)

    def update(
        self,
        account_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[VerifyUpdateResponse]:
        """
        Verify Account Custom Nameserver Glue Records

        Args:
          account_id: Account identifier tag.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._post(
            f"/accounts/{account_id}/custom_ns/verify",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[VerifyUpdateResponse]], ResultWrapper[VerifyUpdateResponse]),
        )


class AsyncVerifies(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncVerifiesWithRawResponse:
        return AsyncVerifiesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncVerifiesWithStreamingResponse:
        return AsyncVerifiesWithStreamingResponse(self)

    async def update(
        self,
        account_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[VerifyUpdateResponse]:
        """
        Verify Account Custom Nameserver Glue Records

        Args:
          account_id: Account identifier tag.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._post(
            f"/accounts/{account_id}/custom_ns/verify",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[VerifyUpdateResponse]], ResultWrapper[VerifyUpdateResponse]),
        )


class VerifiesWithRawResponse:
    def __init__(self, verifies: Verifies) -> None:
        self._verifies = verifies

        self.update = to_raw_response_wrapper(
            verifies.update,
        )


class AsyncVerifiesWithRawResponse:
    def __init__(self, verifies: AsyncVerifies) -> None:
        self._verifies = verifies

        self.update = async_to_raw_response_wrapper(
            verifies.update,
        )


class VerifiesWithStreamingResponse:
    def __init__(self, verifies: Verifies) -> None:
        self._verifies = verifies

        self.update = to_streamed_response_wrapper(
            verifies.update,
        )


class AsyncVerifiesWithStreamingResponse:
    def __init__(self, verifies: AsyncVerifies) -> None:
        self._verifies = verifies

        self.update = async_to_streamed_response_wrapper(
            verifies.update,
        )
