# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, cast
from typing_extensions import Literal

import httpx

from .._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
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
from .._wrappers import ResultWrapper
from .._base_client import make_request_options
from ..types.url_normalization import url_normalization_update_params
from ..types.url_normalization.url_normalization_get_response import URLNormalizationGetResponse
from ..types.url_normalization.url_normalization_update_response import URLNormalizationUpdateResponse

__all__ = ["URLNormalizationResource", "AsyncURLNormalizationResource"]


class URLNormalizationResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> URLNormalizationResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return URLNormalizationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> URLNormalizationResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return URLNormalizationResourceWithStreamingResponse(self)

    def update(
        self,
        *,
        zone_id: str,
        scope: Literal["incoming", "both"],
        type: Literal["cloudflare", "rfc3986"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> URLNormalizationUpdateResponse:
        """
        Updates the URL Normalization settings.

        Args:
          zone_id: The unique ID of the zone.

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
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[URLNormalizationUpdateResponse]._unwrapper,
            ),
            cast_to=cast(Type[URLNormalizationUpdateResponse], ResultWrapper[URLNormalizationUpdateResponse]),
        )

    def delete(
        self,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Deletes the URL Normalization settings.

        Args:
          zone_id: The unique ID of the zone.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/zones/{zone_id}/url_normalization",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
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
        Fetches the current URL Normalization settings.

        Args:
          zone_id: The unique ID of the zone.

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
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[URLNormalizationGetResponse]._unwrapper,
            ),
            cast_to=cast(Type[URLNormalizationGetResponse], ResultWrapper[URLNormalizationGetResponse]),
        )


class AsyncURLNormalizationResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncURLNormalizationResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncURLNormalizationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncURLNormalizationResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncURLNormalizationResourceWithStreamingResponse(self)

    async def update(
        self,
        *,
        zone_id: str,
        scope: Literal["incoming", "both"],
        type: Literal["cloudflare", "rfc3986"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> URLNormalizationUpdateResponse:
        """
        Updates the URL Normalization settings.

        Args:
          zone_id: The unique ID of the zone.

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
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[URLNormalizationUpdateResponse]._unwrapper,
            ),
            cast_to=cast(Type[URLNormalizationUpdateResponse], ResultWrapper[URLNormalizationUpdateResponse]),
        )

    async def delete(
        self,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Deletes the URL Normalization settings.

        Args:
          zone_id: The unique ID of the zone.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/zones/{zone_id}/url_normalization",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
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
        Fetches the current URL Normalization settings.

        Args:
          zone_id: The unique ID of the zone.

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
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[URLNormalizationGetResponse]._unwrapper,
            ),
            cast_to=cast(Type[URLNormalizationGetResponse], ResultWrapper[URLNormalizationGetResponse]),
        )


class URLNormalizationResourceWithRawResponse:
    def __init__(self, url_normalization: URLNormalizationResource) -> None:
        self._url_normalization = url_normalization

        self.update = to_raw_response_wrapper(
            url_normalization.update,
        )
        self.delete = to_raw_response_wrapper(
            url_normalization.delete,
        )
        self.get = to_raw_response_wrapper(
            url_normalization.get,
        )


class AsyncURLNormalizationResourceWithRawResponse:
    def __init__(self, url_normalization: AsyncURLNormalizationResource) -> None:
        self._url_normalization = url_normalization

        self.update = async_to_raw_response_wrapper(
            url_normalization.update,
        )
        self.delete = async_to_raw_response_wrapper(
            url_normalization.delete,
        )
        self.get = async_to_raw_response_wrapper(
            url_normalization.get,
        )


class URLNormalizationResourceWithStreamingResponse:
    def __init__(self, url_normalization: URLNormalizationResource) -> None:
        self._url_normalization = url_normalization

        self.update = to_streamed_response_wrapper(
            url_normalization.update,
        )
        self.delete = to_streamed_response_wrapper(
            url_normalization.delete,
        )
        self.get = to_streamed_response_wrapper(
            url_normalization.get,
        )


class AsyncURLNormalizationResourceWithStreamingResponse:
    def __init__(self, url_normalization: AsyncURLNormalizationResource) -> None:
        self._url_normalization = url_normalization

        self.update = async_to_streamed_response_wrapper(
            url_normalization.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            url_normalization.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            url_normalization.get,
        )
