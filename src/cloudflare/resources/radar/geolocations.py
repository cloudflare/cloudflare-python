# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, cast
from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._wrappers import ResultWrapper
from ...types.radar import geolocation_get_params, geolocation_list_params
from ..._base_client import make_request_options
from ...types.radar.geolocation_get_response import GeolocationGetResponse
from ...types.radar.geolocation_list_response import GeolocationListResponse

__all__ = ["GeolocationsResource", "AsyncGeolocationsResource"]


class GeolocationsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> GeolocationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return GeolocationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> GeolocationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return GeolocationsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        format: Literal["JSON", "CSV"] | Omit = omit,
        geo_id: str | Omit = omit,
        limit: int | Omit = omit,
        location: str | Omit = omit,
        offset: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GeolocationListResponse:
        """
        Retrieves a list of geolocations.

        Args:
          format: Format in which results will be returned.

          geo_id: Filters results by geolocation. Specify a comma-separated list of GeoNames IDs.

          limit: Limits the number of objects returned in the response.

          location: Filters results by location. Specify a comma-separated list of alpha-2 location
              codes.

          offset: Skips the specified number of objects before fetching the results.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/radar/geolocations",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "format": format,
                        "geo_id": geo_id,
                        "limit": limit,
                        "location": location,
                        "offset": offset,
                    },
                    geolocation_list_params.GeolocationListParams,
                ),
                post_parser=ResultWrapper[GeolocationListResponse]._unwrapper,
            ),
            cast_to=cast(Type[GeolocationListResponse], ResultWrapper[GeolocationListResponse]),
        )

    def get(
        self,
        geo_id: str,
        *,
        format: Literal["JSON", "CSV"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GeolocationGetResponse:
        """Retrieves the requested Geolocation information.

        Args:
          geo_id: Geolocation ID.

        Refer to
              [GeoNames](https://download.geonames.org/export/dump/readme.txt)

          format: Format in which results will be returned.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not geo_id:
            raise ValueError(f"Expected a non-empty value for `geo_id` but received {geo_id!r}")
        return self._get(
            f"/radar/geolocations/{geo_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"format": format}, geolocation_get_params.GeolocationGetParams),
                post_parser=ResultWrapper[GeolocationGetResponse]._unwrapper,
            ),
            cast_to=cast(Type[GeolocationGetResponse], ResultWrapper[GeolocationGetResponse]),
        )


class AsyncGeolocationsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncGeolocationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncGeolocationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncGeolocationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncGeolocationsResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        format: Literal["JSON", "CSV"] | Omit = omit,
        geo_id: str | Omit = omit,
        limit: int | Omit = omit,
        location: str | Omit = omit,
        offset: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GeolocationListResponse:
        """
        Retrieves a list of geolocations.

        Args:
          format: Format in which results will be returned.

          geo_id: Filters results by geolocation. Specify a comma-separated list of GeoNames IDs.

          limit: Limits the number of objects returned in the response.

          location: Filters results by location. Specify a comma-separated list of alpha-2 location
              codes.

          offset: Skips the specified number of objects before fetching the results.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/radar/geolocations",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "format": format,
                        "geo_id": geo_id,
                        "limit": limit,
                        "location": location,
                        "offset": offset,
                    },
                    geolocation_list_params.GeolocationListParams,
                ),
                post_parser=ResultWrapper[GeolocationListResponse]._unwrapper,
            ),
            cast_to=cast(Type[GeolocationListResponse], ResultWrapper[GeolocationListResponse]),
        )

    async def get(
        self,
        geo_id: str,
        *,
        format: Literal["JSON", "CSV"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GeolocationGetResponse:
        """Retrieves the requested Geolocation information.

        Args:
          geo_id: Geolocation ID.

        Refer to
              [GeoNames](https://download.geonames.org/export/dump/readme.txt)

          format: Format in which results will be returned.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not geo_id:
            raise ValueError(f"Expected a non-empty value for `geo_id` but received {geo_id!r}")
        return await self._get(
            f"/radar/geolocations/{geo_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"format": format}, geolocation_get_params.GeolocationGetParams),
                post_parser=ResultWrapper[GeolocationGetResponse]._unwrapper,
            ),
            cast_to=cast(Type[GeolocationGetResponse], ResultWrapper[GeolocationGetResponse]),
        )


class GeolocationsResourceWithRawResponse:
    def __init__(self, geolocations: GeolocationsResource) -> None:
        self._geolocations = geolocations

        self.list = to_raw_response_wrapper(
            geolocations.list,
        )
        self.get = to_raw_response_wrapper(
            geolocations.get,
        )


class AsyncGeolocationsResourceWithRawResponse:
    def __init__(self, geolocations: AsyncGeolocationsResource) -> None:
        self._geolocations = geolocations

        self.list = async_to_raw_response_wrapper(
            geolocations.list,
        )
        self.get = async_to_raw_response_wrapper(
            geolocations.get,
        )


class GeolocationsResourceWithStreamingResponse:
    def __init__(self, geolocations: GeolocationsResource) -> None:
        self._geolocations = geolocations

        self.list = to_streamed_response_wrapper(
            geolocations.list,
        )
        self.get = to_streamed_response_wrapper(
            geolocations.get,
        )


class AsyncGeolocationsResourceWithStreamingResponse:
    def __init__(self, geolocations: AsyncGeolocationsResource) -> None:
        self._geolocations = geolocations

        self.list = async_to_streamed_response_wrapper(
            geolocations.list,
        )
        self.get = async_to_streamed_response_wrapper(
            geolocations.get,
        )
