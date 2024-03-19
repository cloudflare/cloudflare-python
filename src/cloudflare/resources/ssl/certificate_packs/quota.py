# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, cast

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
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
from ....types.ssl.certificate_packs import QuotaGetResponse

__all__ = ["Quota", "AsyncQuota"]


class Quota(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> QuotaWithRawResponse:
        return QuotaWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> QuotaWithStreamingResponse:
        return QuotaWithStreamingResponse(self)

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
    ) -> QuotaGetResponse:
        """
        For a given zone, list certificate pack quotas.

        Args:
          zone_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._get(
            f"/zones/{zone_id}/ssl/certificate_packs/quota",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[QuotaGetResponse], ResultWrapper[QuotaGetResponse]),
        )


class AsyncQuota(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncQuotaWithRawResponse:
        return AsyncQuotaWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncQuotaWithStreamingResponse:
        return AsyncQuotaWithStreamingResponse(self)

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
    ) -> QuotaGetResponse:
        """
        For a given zone, list certificate pack quotas.

        Args:
          zone_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._get(
            f"/zones/{zone_id}/ssl/certificate_packs/quota",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[QuotaGetResponse], ResultWrapper[QuotaGetResponse]),
        )


class QuotaWithRawResponse:
    def __init__(self, quota: Quota) -> None:
        self._quota = quota

        self.get = to_raw_response_wrapper(
            quota.get,
        )


class AsyncQuotaWithRawResponse:
    def __init__(self, quota: AsyncQuota) -> None:
        self._quota = quota

        self.get = async_to_raw_response_wrapper(
            quota.get,
        )


class QuotaWithStreamingResponse:
    def __init__(self, quota: Quota) -> None:
        self._quota = quota

        self.get = to_streamed_response_wrapper(
            quota.get,
        )


class AsyncQuotaWithStreamingResponse:
    def __init__(self, quota: AsyncQuota) -> None:
        self._quota = quota

        self.get = async_to_streamed_response_wrapper(
            quota.get,
        )
