# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Optional, cast

import httpx

from ..._types import Body, Query, Headers, NotGiven, not_given
from ..._utils import path_template
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._wrappers import ResultWrapper
from ..._base_client import make_request_options
from ...types.custom_hostnames.quota_get_response import QuotaGetResponse

__all__ = ["QuotaResource", "AsyncQuotaResource"]


class QuotaResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> QuotaResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return QuotaResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> QuotaResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return QuotaResourceWithStreamingResponse(self)

    def get(
        self,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[QuotaGetResponse]:
        """Returns custom hostname quota usage for a zone.

        The allocated quota is a soft
        limit; creating custom hostnames after usage exceeds this limit can still
        succeed until the hard cap is reached. Use the exceeded and hard_cap fields to
        track when usage is above the soft limit and when new custom hostname creation
        will be rejected.

        Args:
          zone_id: Identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._get(
            path_template("/zones/{zone_id}/custom_hostnames/quota", zone_id=zone_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[QuotaGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[QuotaGetResponse]], ResultWrapper[QuotaGetResponse]),
        )


class AsyncQuotaResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncQuotaResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncQuotaResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncQuotaResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncQuotaResourceWithStreamingResponse(self)

    async def get(
        self,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[QuotaGetResponse]:
        """Returns custom hostname quota usage for a zone.

        The allocated quota is a soft
        limit; creating custom hostnames after usage exceeds this limit can still
        succeed until the hard cap is reached. Use the exceeded and hard_cap fields to
        track when usage is above the soft limit and when new custom hostname creation
        will be rejected.

        Args:
          zone_id: Identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._get(
            path_template("/zones/{zone_id}/custom_hostnames/quota", zone_id=zone_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[QuotaGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[QuotaGetResponse]], ResultWrapper[QuotaGetResponse]),
        )


class QuotaResourceWithRawResponse:
    def __init__(self, quota: QuotaResource) -> None:
        self._quota = quota

        self.get = to_raw_response_wrapper(
            quota.get,
        )


class AsyncQuotaResourceWithRawResponse:
    def __init__(self, quota: AsyncQuotaResource) -> None:
        self._quota = quota

        self.get = async_to_raw_response_wrapper(
            quota.get,
        )


class QuotaResourceWithStreamingResponse:
    def __init__(self, quota: QuotaResource) -> None:
        self._quota = quota

        self.get = to_streamed_response_wrapper(
            quota.get,
        )


class AsyncQuotaResourceWithStreamingResponse:
    def __init__(self, quota: AsyncQuotaResource) -> None:
        self._quota = quota

        self.get = async_to_streamed_response_wrapper(
            quota.get,
        )
