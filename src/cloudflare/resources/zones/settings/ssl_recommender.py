# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Optional, cast

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
from ....types.zones.settings import SSLRecommender, ssl_recommender_edit_params
from ....types.zones.settings.ssl_recommender import SSLRecommender
from ....types.zones.settings.ssl_recommender_param import SSLRecommenderParam

__all__ = ["SSLRecommenderResource", "AsyncSSLRecommenderResource"]


class SSLRecommenderResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SSLRecommenderResourceWithRawResponse:
        return SSLRecommenderResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SSLRecommenderResourceWithStreamingResponse:
        return SSLRecommenderResourceWithStreamingResponse(self)

    def edit(
        self,
        *,
        zone_id: str,
        value: SSLRecommenderParam,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[SSLRecommender]:
        """
        Enrollment in the SSL/TLS Recommender service which tries to detect and
        recommend (by sending periodic emails) the most secure SSL/TLS setting your
        origin servers support.

        Args:
          zone_id: Identifier

          value: Enrollment in the SSL/TLS Recommender service which tries to detect and
              recommend (by sending periodic emails) the most secure SSL/TLS setting your
              origin servers support.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._patch(
            f"/zones/{zone_id}/settings/ssl_recommender",
            body=maybe_transform({"value": value}, ssl_recommender_edit_params.SSLRecommenderEditParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[SSLRecommender]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[SSLRecommender]], ResultWrapper[SSLRecommender]),
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
    ) -> Optional[SSLRecommender]:
        """
        Enrollment in the SSL/TLS Recommender service which tries to detect and
        recommend (by sending periodic emails) the most secure SSL/TLS setting your
        origin servers support.

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
            f"/zones/{zone_id}/settings/ssl_recommender",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[SSLRecommender]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[SSLRecommender]], ResultWrapper[SSLRecommender]),
        )


class AsyncSSLRecommenderResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSSLRecommenderResourceWithRawResponse:
        return AsyncSSLRecommenderResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSSLRecommenderResourceWithStreamingResponse:
        return AsyncSSLRecommenderResourceWithStreamingResponse(self)

    async def edit(
        self,
        *,
        zone_id: str,
        value: SSLRecommenderParam,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[SSLRecommender]:
        """
        Enrollment in the SSL/TLS Recommender service which tries to detect and
        recommend (by sending periodic emails) the most secure SSL/TLS setting your
        origin servers support.

        Args:
          zone_id: Identifier

          value: Enrollment in the SSL/TLS Recommender service which tries to detect and
              recommend (by sending periodic emails) the most secure SSL/TLS setting your
              origin servers support.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._patch(
            f"/zones/{zone_id}/settings/ssl_recommender",
            body=await async_maybe_transform({"value": value}, ssl_recommender_edit_params.SSLRecommenderEditParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[SSLRecommender]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[SSLRecommender]], ResultWrapper[SSLRecommender]),
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
    ) -> Optional[SSLRecommender]:
        """
        Enrollment in the SSL/TLS Recommender service which tries to detect and
        recommend (by sending periodic emails) the most secure SSL/TLS setting your
        origin servers support.

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
            f"/zones/{zone_id}/settings/ssl_recommender",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[SSLRecommender]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[SSLRecommender]], ResultWrapper[SSLRecommender]),
        )


class SSLRecommenderResourceWithRawResponse:
    def __init__(self, ssl_recommender: SSLRecommenderResource) -> None:
        self._ssl_recommender = ssl_recommender

        self.edit = to_raw_response_wrapper(
            ssl_recommender.edit,
        )
        self.get = to_raw_response_wrapper(
            ssl_recommender.get,
        )


class AsyncSSLRecommenderResourceWithRawResponse:
    def __init__(self, ssl_recommender: AsyncSSLRecommenderResource) -> None:
        self._ssl_recommender = ssl_recommender

        self.edit = async_to_raw_response_wrapper(
            ssl_recommender.edit,
        )
        self.get = async_to_raw_response_wrapper(
            ssl_recommender.get,
        )


class SSLRecommenderResourceWithStreamingResponse:
    def __init__(self, ssl_recommender: SSLRecommenderResource) -> None:
        self._ssl_recommender = ssl_recommender

        self.edit = to_streamed_response_wrapper(
            ssl_recommender.edit,
        )
        self.get = to_streamed_response_wrapper(
            ssl_recommender.get,
        )


class AsyncSSLRecommenderResourceWithStreamingResponse:
    def __init__(self, ssl_recommender: AsyncSSLRecommenderResource) -> None:
        self._ssl_recommender = ssl_recommender

        self.edit = async_to_streamed_response_wrapper(
            ssl_recommender.edit,
        )
        self.get = async_to_streamed_response_wrapper(
            ssl_recommender.get,
        )
