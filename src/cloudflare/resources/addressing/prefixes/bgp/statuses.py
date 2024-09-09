# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Optional, cast

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
from ....._base_client import make_request_options
from .....types.addressing.prefixes.bgp import status_edit_params
from .....types.addressing.prefixes.bgp.status_get_response import StatusGetResponse
from .....types.addressing.prefixes.bgp.status_edit_response import StatusEditResponse

__all__ = ["StatusesResource", "AsyncStatusesResource"]


class StatusesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> StatusesResourceWithRawResponse:
        return StatusesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> StatusesResourceWithStreamingResponse:
        return StatusesResourceWithStreamingResponse(self)

    def edit(
        self,
        prefix_id: str,
        *,
        account_id: str,
        advertised: bool,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[StatusEditResponse]:
        """
        Advertise or withdraw BGP route for a prefix.

        Args:
          account_id: Identifier

          prefix_id: Identifier

          advertised: Enablement of prefix advertisement to the Internet.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not prefix_id:
            raise ValueError(f"Expected a non-empty value for `prefix_id` but received {prefix_id!r}")
        return self._patch(
            f"/accounts/{account_id}/addressing/prefixes/{prefix_id}/bgp/status",
            body=maybe_transform({"advertised": advertised}, status_edit_params.StatusEditParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[StatusEditResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[StatusEditResponse]], ResultWrapper[StatusEditResponse]),
        )

    def get(
        self,
        prefix_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[StatusGetResponse]:
        """
        List the current advertisement state for a prefix.

        Args:
          account_id: Identifier

          prefix_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not prefix_id:
            raise ValueError(f"Expected a non-empty value for `prefix_id` but received {prefix_id!r}")
        return self._get(
            f"/accounts/{account_id}/addressing/prefixes/{prefix_id}/bgp/status",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[StatusGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[StatusGetResponse]], ResultWrapper[StatusGetResponse]),
        )


class AsyncStatusesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncStatusesResourceWithRawResponse:
        return AsyncStatusesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncStatusesResourceWithStreamingResponse:
        return AsyncStatusesResourceWithStreamingResponse(self)

    async def edit(
        self,
        prefix_id: str,
        *,
        account_id: str,
        advertised: bool,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[StatusEditResponse]:
        """
        Advertise or withdraw BGP route for a prefix.

        Args:
          account_id: Identifier

          prefix_id: Identifier

          advertised: Enablement of prefix advertisement to the Internet.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not prefix_id:
            raise ValueError(f"Expected a non-empty value for `prefix_id` but received {prefix_id!r}")
        return await self._patch(
            f"/accounts/{account_id}/addressing/prefixes/{prefix_id}/bgp/status",
            body=await async_maybe_transform({"advertised": advertised}, status_edit_params.StatusEditParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[StatusEditResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[StatusEditResponse]], ResultWrapper[StatusEditResponse]),
        )

    async def get(
        self,
        prefix_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[StatusGetResponse]:
        """
        List the current advertisement state for a prefix.

        Args:
          account_id: Identifier

          prefix_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not prefix_id:
            raise ValueError(f"Expected a non-empty value for `prefix_id` but received {prefix_id!r}")
        return await self._get(
            f"/accounts/{account_id}/addressing/prefixes/{prefix_id}/bgp/status",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[StatusGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[StatusGetResponse]], ResultWrapper[StatusGetResponse]),
        )


class StatusesResourceWithRawResponse:
    def __init__(self, statuses: StatusesResource) -> None:
        self._statuses = statuses

        self.edit = to_raw_response_wrapper(
            statuses.edit,
        )
        self.get = to_raw_response_wrapper(
            statuses.get,
        )


class AsyncStatusesResourceWithRawResponse:
    def __init__(self, statuses: AsyncStatusesResource) -> None:
        self._statuses = statuses

        self.edit = async_to_raw_response_wrapper(
            statuses.edit,
        )
        self.get = async_to_raw_response_wrapper(
            statuses.get,
        )


class StatusesResourceWithStreamingResponse:
    def __init__(self, statuses: StatusesResource) -> None:
        self._statuses = statuses

        self.edit = to_streamed_response_wrapper(
            statuses.edit,
        )
        self.get = to_streamed_response_wrapper(
            statuses.get,
        )


class AsyncStatusesResourceWithStreamingResponse:
    def __init__(self, statuses: AsyncStatusesResource) -> None:
        self._statuses = statuses

        self.edit = async_to_streamed_response_wrapper(
            statuses.edit,
        )
        self.get = async_to_streamed_response_wrapper(
            statuses.get,
        )
