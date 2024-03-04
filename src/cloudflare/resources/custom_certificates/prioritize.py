# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Type, Iterable, Optional, cast

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
from ..._base_client import (
    make_request_options,
)
from ...types.custom_certificates import PrioritizeUpdateResponse, prioritize_update_params

__all__ = ["Prioritize", "AsyncPrioritize"]


class Prioritize(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PrioritizeWithRawResponse:
        return PrioritizeWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PrioritizeWithStreamingResponse:
        return PrioritizeWithStreamingResponse(self)

    def update(
        self,
        *,
        zone_id: str,
        certificates: Iterable[prioritize_update_params.Certificate],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[PrioritizeUpdateResponse]:
        """
        If a zone has multiple SSL certificates, you can set the order in which they
        should be used during a request. The higher priority will break ties across
        overlapping 'legacy_custom' certificates.

        Args:
          zone_id: Identifier

          certificates: Array of ordered certificates.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._put(
            f"/zones/{zone_id}/custom_certificates/prioritize",
            body=maybe_transform({"certificates": certificates}, prioritize_update_params.PrioritizeUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[PrioritizeUpdateResponse]], ResultWrapper[PrioritizeUpdateResponse]),
        )


class AsyncPrioritize(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPrioritizeWithRawResponse:
        return AsyncPrioritizeWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPrioritizeWithStreamingResponse:
        return AsyncPrioritizeWithStreamingResponse(self)

    async def update(
        self,
        *,
        zone_id: str,
        certificates: Iterable[prioritize_update_params.Certificate],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[PrioritizeUpdateResponse]:
        """
        If a zone has multiple SSL certificates, you can set the order in which they
        should be used during a request. The higher priority will break ties across
        overlapping 'legacy_custom' certificates.

        Args:
          zone_id: Identifier

          certificates: Array of ordered certificates.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._put(
            f"/zones/{zone_id}/custom_certificates/prioritize",
            body=await async_maybe_transform(
                {"certificates": certificates}, prioritize_update_params.PrioritizeUpdateParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[PrioritizeUpdateResponse]], ResultWrapper[PrioritizeUpdateResponse]),
        )


class PrioritizeWithRawResponse:
    def __init__(self, prioritize: Prioritize) -> None:
        self._prioritize = prioritize

        self.update = to_raw_response_wrapper(
            prioritize.update,
        )


class AsyncPrioritizeWithRawResponse:
    def __init__(self, prioritize: AsyncPrioritize) -> None:
        self._prioritize = prioritize

        self.update = async_to_raw_response_wrapper(
            prioritize.update,
        )


class PrioritizeWithStreamingResponse:
    def __init__(self, prioritize: Prioritize) -> None:
        self._prioritize = prioritize

        self.update = to_streamed_response_wrapper(
            prioritize.update,
        )


class AsyncPrioritizeWithStreamingResponse:
    def __init__(self, prioritize: AsyncPrioritize) -> None:
        self._prioritize = prioritize

        self.update = async_to_streamed_response_wrapper(
            prioritize.update,
        )
