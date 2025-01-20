# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Optional, cast

import httpx

from .regions import (
    RegionsResource,
    AsyncRegionsResource,
    RegionsResourceWithRawResponse,
    AsyncRegionsResourceWithRawResponse,
    RegionsResourceWithStreamingResponse,
    AsyncRegionsResourceWithStreamingResponse,
)
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
from ....pagination import SyncSinglePage, AsyncSinglePage
from ...._base_client import AsyncPaginator, make_request_options
from ....types.addressing import regional_hostname_edit_params, regional_hostname_create_params
from ....types.addressing.regional_hostname_get_response import RegionalHostnameGetResponse
from ....types.addressing.regional_hostname_edit_response import RegionalHostnameEditResponse
from ....types.addressing.regional_hostname_list_response import RegionalHostnameListResponse
from ....types.addressing.regional_hostname_create_response import RegionalHostnameCreateResponse
from ....types.addressing.regional_hostname_delete_response import RegionalHostnameDeleteResponse

__all__ = ["RegionalHostnamesResource", "AsyncRegionalHostnamesResource"]


class RegionalHostnamesResource(SyncAPIResource):
    @cached_property
    def regions(self) -> RegionsResource:
        return RegionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> RegionalHostnamesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return RegionalHostnamesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RegionalHostnamesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return RegionalHostnamesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        zone_id: str,
        hostname: str,
        region_key: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[RegionalHostnameCreateResponse]:
        """Create a new Regional Hostname entry.

        Cloudflare will only use data centers that
        are physically located within the chosen region to decrypt and service HTTPS
        traffic. Learn more about
        [Regional Services](https://developers.cloudflare.com/data-localization/regional-services/get-started/).

        Args:
          zone_id: Identifier

          hostname: DNS hostname to be regionalized, must be a subdomain of the zone. Wildcards are
              supported for one level, e.g `*.example.com`

          region_key: Identifying key for the region

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._post(
            f"/zones/{zone_id}/addressing/regional_hostnames",
            body=maybe_transform(
                {
                    "hostname": hostname,
                    "region_key": region_key,
                },
                regional_hostname_create_params.RegionalHostnameCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[RegionalHostnameCreateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[RegionalHostnameCreateResponse]], ResultWrapper[RegionalHostnameCreateResponse]),
        )

    def list(
        self,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncSinglePage[RegionalHostnameListResponse]:
        """
        List all Regional Hostnames within a zone.

        Args:
          zone_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._get_api_list(
            f"/zones/{zone_id}/addressing/regional_hostnames",
            page=SyncSinglePage[RegionalHostnameListResponse],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=RegionalHostnameListResponse,
        )

    def delete(
        self,
        hostname: str,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RegionalHostnameDeleteResponse:
        """
        Delete the region configuration for a specific Regional Hostname.

        Args:
          zone_id: Identifier

          hostname: DNS hostname to be regionalized, must be a subdomain of the zone. Wildcards are
              supported for one level, e.g `*.example.com`

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not hostname:
            raise ValueError(f"Expected a non-empty value for `hostname` but received {hostname!r}")
        return self._delete(
            f"/zones/{zone_id}/addressing/regional_hostnames/{hostname}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RegionalHostnameDeleteResponse,
        )

    def edit(
        self,
        hostname: str,
        *,
        zone_id: str,
        region_key: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[RegionalHostnameEditResponse]:
        """Update the configuration for a specific Regional Hostname.

        Only the region_key
        of a hostname is mutable.

        Args:
          zone_id: Identifier

          hostname: DNS hostname to be regionalized, must be a subdomain of the zone. Wildcards are
              supported for one level, e.g `*.example.com`

          region_key: Identifying key for the region

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not hostname:
            raise ValueError(f"Expected a non-empty value for `hostname` but received {hostname!r}")
        return self._patch(
            f"/zones/{zone_id}/addressing/regional_hostnames/{hostname}",
            body=maybe_transform({"region_key": region_key}, regional_hostname_edit_params.RegionalHostnameEditParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[RegionalHostnameEditResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[RegionalHostnameEditResponse]], ResultWrapper[RegionalHostnameEditResponse]),
        )

    def get(
        self,
        hostname: str,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[RegionalHostnameGetResponse]:
        """
        Fetch the configuration for a specific Regional Hostname, within a zone.

        Args:
          zone_id: Identifier

          hostname: DNS hostname to be regionalized, must be a subdomain of the zone. Wildcards are
              supported for one level, e.g `*.example.com`

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not hostname:
            raise ValueError(f"Expected a non-empty value for `hostname` but received {hostname!r}")
        return self._get(
            f"/zones/{zone_id}/addressing/regional_hostnames/{hostname}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[RegionalHostnameGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[RegionalHostnameGetResponse]], ResultWrapper[RegionalHostnameGetResponse]),
        )


class AsyncRegionalHostnamesResource(AsyncAPIResource):
    @cached_property
    def regions(self) -> AsyncRegionsResource:
        return AsyncRegionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncRegionalHostnamesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRegionalHostnamesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRegionalHostnamesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncRegionalHostnamesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        zone_id: str,
        hostname: str,
        region_key: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[RegionalHostnameCreateResponse]:
        """Create a new Regional Hostname entry.

        Cloudflare will only use data centers that
        are physically located within the chosen region to decrypt and service HTTPS
        traffic. Learn more about
        [Regional Services](https://developers.cloudflare.com/data-localization/regional-services/get-started/).

        Args:
          zone_id: Identifier

          hostname: DNS hostname to be regionalized, must be a subdomain of the zone. Wildcards are
              supported for one level, e.g `*.example.com`

          region_key: Identifying key for the region

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._post(
            f"/zones/{zone_id}/addressing/regional_hostnames",
            body=await async_maybe_transform(
                {
                    "hostname": hostname,
                    "region_key": region_key,
                },
                regional_hostname_create_params.RegionalHostnameCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[RegionalHostnameCreateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[RegionalHostnameCreateResponse]], ResultWrapper[RegionalHostnameCreateResponse]),
        )

    def list(
        self,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[RegionalHostnameListResponse, AsyncSinglePage[RegionalHostnameListResponse]]:
        """
        List all Regional Hostnames within a zone.

        Args:
          zone_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._get_api_list(
            f"/zones/{zone_id}/addressing/regional_hostnames",
            page=AsyncSinglePage[RegionalHostnameListResponse],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=RegionalHostnameListResponse,
        )

    async def delete(
        self,
        hostname: str,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RegionalHostnameDeleteResponse:
        """
        Delete the region configuration for a specific Regional Hostname.

        Args:
          zone_id: Identifier

          hostname: DNS hostname to be regionalized, must be a subdomain of the zone. Wildcards are
              supported for one level, e.g `*.example.com`

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not hostname:
            raise ValueError(f"Expected a non-empty value for `hostname` but received {hostname!r}")
        return await self._delete(
            f"/zones/{zone_id}/addressing/regional_hostnames/{hostname}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RegionalHostnameDeleteResponse,
        )

    async def edit(
        self,
        hostname: str,
        *,
        zone_id: str,
        region_key: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[RegionalHostnameEditResponse]:
        """Update the configuration for a specific Regional Hostname.

        Only the region_key
        of a hostname is mutable.

        Args:
          zone_id: Identifier

          hostname: DNS hostname to be regionalized, must be a subdomain of the zone. Wildcards are
              supported for one level, e.g `*.example.com`

          region_key: Identifying key for the region

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not hostname:
            raise ValueError(f"Expected a non-empty value for `hostname` but received {hostname!r}")
        return await self._patch(
            f"/zones/{zone_id}/addressing/regional_hostnames/{hostname}",
            body=await async_maybe_transform(
                {"region_key": region_key}, regional_hostname_edit_params.RegionalHostnameEditParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[RegionalHostnameEditResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[RegionalHostnameEditResponse]], ResultWrapper[RegionalHostnameEditResponse]),
        )

    async def get(
        self,
        hostname: str,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[RegionalHostnameGetResponse]:
        """
        Fetch the configuration for a specific Regional Hostname, within a zone.

        Args:
          zone_id: Identifier

          hostname: DNS hostname to be regionalized, must be a subdomain of the zone. Wildcards are
              supported for one level, e.g `*.example.com`

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not hostname:
            raise ValueError(f"Expected a non-empty value for `hostname` but received {hostname!r}")
        return await self._get(
            f"/zones/{zone_id}/addressing/regional_hostnames/{hostname}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[RegionalHostnameGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[RegionalHostnameGetResponse]], ResultWrapper[RegionalHostnameGetResponse]),
        )


class RegionalHostnamesResourceWithRawResponse:
    def __init__(self, regional_hostnames: RegionalHostnamesResource) -> None:
        self._regional_hostnames = regional_hostnames

        self.create = to_raw_response_wrapper(
            regional_hostnames.create,
        )
        self.list = to_raw_response_wrapper(
            regional_hostnames.list,
        )
        self.delete = to_raw_response_wrapper(
            regional_hostnames.delete,
        )
        self.edit = to_raw_response_wrapper(
            regional_hostnames.edit,
        )
        self.get = to_raw_response_wrapper(
            regional_hostnames.get,
        )

    @cached_property
    def regions(self) -> RegionsResourceWithRawResponse:
        return RegionsResourceWithRawResponse(self._regional_hostnames.regions)


class AsyncRegionalHostnamesResourceWithRawResponse:
    def __init__(self, regional_hostnames: AsyncRegionalHostnamesResource) -> None:
        self._regional_hostnames = regional_hostnames

        self.create = async_to_raw_response_wrapper(
            regional_hostnames.create,
        )
        self.list = async_to_raw_response_wrapper(
            regional_hostnames.list,
        )
        self.delete = async_to_raw_response_wrapper(
            regional_hostnames.delete,
        )
        self.edit = async_to_raw_response_wrapper(
            regional_hostnames.edit,
        )
        self.get = async_to_raw_response_wrapper(
            regional_hostnames.get,
        )

    @cached_property
    def regions(self) -> AsyncRegionsResourceWithRawResponse:
        return AsyncRegionsResourceWithRawResponse(self._regional_hostnames.regions)


class RegionalHostnamesResourceWithStreamingResponse:
    def __init__(self, regional_hostnames: RegionalHostnamesResource) -> None:
        self._regional_hostnames = regional_hostnames

        self.create = to_streamed_response_wrapper(
            regional_hostnames.create,
        )
        self.list = to_streamed_response_wrapper(
            regional_hostnames.list,
        )
        self.delete = to_streamed_response_wrapper(
            regional_hostnames.delete,
        )
        self.edit = to_streamed_response_wrapper(
            regional_hostnames.edit,
        )
        self.get = to_streamed_response_wrapper(
            regional_hostnames.get,
        )

    @cached_property
    def regions(self) -> RegionsResourceWithStreamingResponse:
        return RegionsResourceWithStreamingResponse(self._regional_hostnames.regions)


class AsyncRegionalHostnamesResourceWithStreamingResponse:
    def __init__(self, regional_hostnames: AsyncRegionalHostnamesResource) -> None:
        self._regional_hostnames = regional_hostnames

        self.create = async_to_streamed_response_wrapper(
            regional_hostnames.create,
        )
        self.list = async_to_streamed_response_wrapper(
            regional_hostnames.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            regional_hostnames.delete,
        )
        self.edit = async_to_streamed_response_wrapper(
            regional_hostnames.edit,
        )
        self.get = async_to_streamed_response_wrapper(
            regional_hostnames.get,
        )

    @cached_property
    def regions(self) -> AsyncRegionsResourceWithStreamingResponse:
        return AsyncRegionsResourceWithStreamingResponse(self._regional_hostnames.regions)
