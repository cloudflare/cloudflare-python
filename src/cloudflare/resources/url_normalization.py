# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import (
    URLNormalizationGetResponse,
    URLNormalizationUpdateResponse,
    url_normalization_update_params,
)
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import (
    maybe_transform,
    async_maybe_transform,
)
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import (
    make_request_options,
)

__all__ = ["URLNormalization", "AsyncURLNormalization"]


class URLNormalization(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> URLNormalizationWithRawResponse:
        return URLNormalizationWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> URLNormalizationWithStreamingResponse:
        return URLNormalizationWithStreamingResponse(self)

    def update(
        self,
        *,
        zone_id: str,
        scope: str | NotGiven = NOT_GIVEN,
        type: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> URLNormalizationUpdateResponse:
        """
        Updates the URL normalization settings.

        Args:
          zone_id: Identifier

          scope: The scope of the URL normalization.

          type: The type of URL normalization performed by Cloudflare.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._put(
            f"/zones/{zone_id}/url_normalization",
            body=maybe_transform(
                {
                    "scope": scope,
                    "type": type,
                },
                url_normalization_update_params.URLNormalizationUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=URLNormalizationUpdateResponse,
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
    ) -> URLNormalizationGetResponse:
        """
        Fetches the current URL normalization settings.

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
            f"/zones/{zone_id}/url_normalization",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=URLNormalizationGetResponse,
        )


class AsyncURLNormalization(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncURLNormalizationWithRawResponse:
        return AsyncURLNormalizationWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncURLNormalizationWithStreamingResponse:
        return AsyncURLNormalizationWithStreamingResponse(self)

    async def update(
        self,
        *,
        zone_id: str,
        scope: str | NotGiven = NOT_GIVEN,
        type: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> URLNormalizationUpdateResponse:
        """
        Updates the URL normalization settings.

        Args:
          zone_id: Identifier

          scope: The scope of the URL normalization.

          type: The type of URL normalization performed by Cloudflare.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._put(
            f"/zones/{zone_id}/url_normalization",
            body=await async_maybe_transform(
                {
                    "scope": scope,
                    "type": type,
                },
                url_normalization_update_params.URLNormalizationUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=URLNormalizationUpdateResponse,
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
    ) -> URLNormalizationGetResponse:
        """
        Fetches the current URL normalization settings.

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
            f"/zones/{zone_id}/url_normalization",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=URLNormalizationGetResponse,
        )


class URLNormalizationWithRawResponse:
    def __init__(self, url_normalization: URLNormalization) -> None:
        self._url_normalization = url_normalization

        self.update = to_raw_response_wrapper(
            url_normalization.update,
        )
        self.get = to_raw_response_wrapper(
            url_normalization.get,
        )


class AsyncURLNormalizationWithRawResponse:
    def __init__(self, url_normalization: AsyncURLNormalization) -> None:
        self._url_normalization = url_normalization

        self.update = async_to_raw_response_wrapper(
            url_normalization.update,
        )
        self.get = async_to_raw_response_wrapper(
            url_normalization.get,
        )


class URLNormalizationWithStreamingResponse:
    def __init__(self, url_normalization: URLNormalization) -> None:
        self._url_normalization = url_normalization

        self.update = to_streamed_response_wrapper(
            url_normalization.update,
        )
        self.get = to_streamed_response_wrapper(
            url_normalization.get,
        )


class AsyncURLNormalizationWithStreamingResponse:
    def __init__(self, url_normalization: AsyncURLNormalization) -> None:
        self._url_normalization = url_normalization

        self.update = async_to_streamed_response_wrapper(
            url_normalization.update,
        )
        self.get = async_to_streamed_response_wrapper(
            url_normalization.get,
        )
