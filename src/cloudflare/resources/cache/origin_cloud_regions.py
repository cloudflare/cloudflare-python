# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Iterable, Optional, cast
from typing_extensions import Literal

import httpx

from ..._types import Body, Query, Headers, NotGiven, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._wrappers import ResultWrapper
from ...types.cache import (
    origin_cloud_region_edit_params,
    origin_cloud_region_create_params,
    origin_cloud_region_bulk_edit_params,
)
from ..._base_client import make_request_options
from ...types.cache.origin_cloud_region_get_response import OriginCloudRegionGetResponse
from ...types.cache.origin_cloud_region_edit_response import OriginCloudRegionEditResponse
from ...types.cache.origin_cloud_region_list_response import OriginCloudRegionListResponse
from ...types.cache.origin_cloud_region_create_response import OriginCloudRegionCreateResponse
from ...types.cache.origin_cloud_region_delete_response import OriginCloudRegionDeleteResponse
from ...types.cache.origin_cloud_region_bulk_edit_response import OriginCloudRegionBulkEditResponse
from ...types.cache.origin_cloud_region_bulk_delete_response import OriginCloudRegionBulkDeleteResponse
from ...types.cache.origin_cloud_region_supported_regions_response import OriginCloudRegionSupportedRegionsResponse

__all__ = ["OriginCloudRegionsResource", "AsyncOriginCloudRegionsResource"]


class OriginCloudRegionsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> OriginCloudRegionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return OriginCloudRegionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OriginCloudRegionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return OriginCloudRegionsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        zone_id: str,
        ip: str,
        region: str,
        vendor: Literal["aws", "azure", "gcp", "oci"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[OriginCloudRegionCreateResponse]:
        """Adds a single IP-to-cloud-region mapping for the zone.

        The IP must be a valid
        IPv4 or IPv6 address and is normalized to canonical form before storage (RFC
        5952 for IPv6). Returns 400 (code 1145) if a mapping for that IP already exists
        — use PATCH to update an existing entry. The vendor and region are validated
        against the list from
        `GET /zones/{zone_id}/cache/origin_cloud_regions/supported_regions`.

        Args:
          zone_id: Identifier.

          ip: Origin IP address (IPv4 or IPv6). Normalized to canonical form before storage
              (RFC 5952 for IPv6).

          region: Cloud vendor region identifier. Must be a valid region for the specified vendor
              as returned by the supported_regions endpoint.

          vendor: Cloud vendor hosting the origin. Must be one of the supported vendors.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._post(
            path_template("/zones/{zone_id}/cache/origin_cloud_regions", zone_id=zone_id),
            body=maybe_transform(
                {
                    "ip": ip,
                    "region": region,
                    "vendor": vendor,
                },
                origin_cloud_region_create_params.OriginCloudRegionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[OriginCloudRegionCreateResponse]]._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[OriginCloudRegionCreateResponse]], ResultWrapper[OriginCloudRegionCreateResponse]
            ),
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[OriginCloudRegionListResponse]:
        """Returns all IP-to-cloud-region mappings configured for the zone.

        Each mapping
        tells Cloudflare which cloud vendor and region hosts the origin at that IP,
        enabling the edge to route via the nearest Tiered Cache upper-tier co-located
        with that cloud provider. Returns an empty array when no mappings exist.

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
            path_template("/zones/{zone_id}/cache/origin_cloud_regions", zone_id=zone_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[OriginCloudRegionListResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[OriginCloudRegionListResponse]], ResultWrapper[OriginCloudRegionListResponse]),
        )

    def delete(
        self,
        origin_ip: str,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[OriginCloudRegionDeleteResponse]:
        """Removes the cloud region mapping for a single origin IP address.

        The IP path
        parameter is normalized before lookup. Returns the deleted entry on success.
        Returns 404 (code 1163) if no mapping exists for the specified IP. When the last
        mapping for the zone is removed the underlying rule record is also deleted.

        Args:
          zone_id: Identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not origin_ip:
            raise ValueError(f"Expected a non-empty value for `origin_ip` but received {origin_ip!r}")
        return self._delete(
            path_template(
                "/zones/{zone_id}/cache/origin_cloud_regions/{origin_ip}", zone_id=zone_id, origin_ip=origin_ip
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[OriginCloudRegionDeleteResponse]]._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[OriginCloudRegionDeleteResponse]], ResultWrapper[OriginCloudRegionDeleteResponse]
            ),
        )

    def bulk_delete(
        self,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[OriginCloudRegionBulkDeleteResponse]:
        """Removes up to 100 IP-to-cloud-region mappings in a single request.

        Each IP is
        validated independently — successfully deleted items are returned in the
        `succeeded` array and IPs that could not be found or are invalid are returned in
        the `failed` array.

        Args:
          zone_id: Identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._delete(
            path_template("/zones/{zone_id}/cache/origin_cloud_regions/batch", zone_id=zone_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[OriginCloudRegionBulkDeleteResponse]]._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[OriginCloudRegionBulkDeleteResponse]], ResultWrapper[OriginCloudRegionBulkDeleteResponse]
            ),
        )

    def bulk_edit(
        self,
        *,
        zone_id: str,
        body: Iterable[origin_cloud_region_bulk_edit_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[OriginCloudRegionBulkEditResponse]:
        """Adds or updates up to 100 IP-to-cloud-region mappings in a single request.

        Each
        item is validated independently — valid items are applied and invalid items are
        returned in the `failed` array. The vendor and region for every item are
        validated against the list from
        `GET /zones/{zone_id}/cache/origin_cloud_regions/supported_regions`.

        Args:
          zone_id: Identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._patch(
            path_template("/zones/{zone_id}/cache/origin_cloud_regions/batch", zone_id=zone_id),
            body=maybe_transform(body, Iterable[origin_cloud_region_bulk_edit_params.Body]),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[OriginCloudRegionBulkEditResponse]]._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[OriginCloudRegionBulkEditResponse]], ResultWrapper[OriginCloudRegionBulkEditResponse]
            ),
        )

    def edit(
        self,
        *,
        zone_id: str,
        ip: str,
        region: str,
        vendor: Literal["aws", "azure", "gcp", "oci"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[OriginCloudRegionEditResponse]:
        """Adds or updates a single IP-to-cloud-region mapping for the zone.

        Unlike POST,
        this operation is idempotent — if a mapping for the IP already exists it is
        overwritten. Returns the complete updated list of all mappings for the zone.
        Returns 403 (code 1164) when the zone has reached the limit of 3,500 IP
        mappings.

        Args:
          zone_id: Identifier.

          ip: Origin IP address (IPv4 or IPv6). Normalized to canonical form before storage
              (RFC 5952 for IPv6).

          region: Cloud vendor region identifier. Must be a valid region for the specified vendor
              as returned by the supported_regions endpoint.

          vendor: Cloud vendor hosting the origin. Must be one of the supported vendors.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._patch(
            path_template("/zones/{zone_id}/cache/origin_cloud_regions", zone_id=zone_id),
            body=maybe_transform(
                {
                    "ip": ip,
                    "region": region,
                    "vendor": vendor,
                },
                origin_cloud_region_edit_params.OriginCloudRegionEditParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[OriginCloudRegionEditResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[OriginCloudRegionEditResponse]], ResultWrapper[OriginCloudRegionEditResponse]),
        )

    def get(
        self,
        origin_ip: str,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[OriginCloudRegionGetResponse]:
        """Returns the cloud region mapping for a single origin IP address.

        The IP path
        parameter is normalized before lookup (RFC 5952 for IPv6). Returns 404
        (code 1142) if the zone has no mappings or if the specified IP has no mapping.

        Args:
          zone_id: Identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not origin_ip:
            raise ValueError(f"Expected a non-empty value for `origin_ip` but received {origin_ip!r}")
        return self._get(
            path_template(
                "/zones/{zone_id}/cache/origin_cloud_regions/{origin_ip}", zone_id=zone_id, origin_ip=origin_ip
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[OriginCloudRegionGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[OriginCloudRegionGetResponse]], ResultWrapper[OriginCloudRegionGetResponse]),
        )

    def supported_regions(
        self,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[OriginCloudRegionSupportedRegionsResponse]:
        """
        Returns the cloud vendors and regions that are valid values for origin cloud
        region mappings. Each region includes the Tiered Cache upper-tier colocation
        codes that will be used for cache routing when a mapping targeting that region
        is active. Requires the zone to have Tiered Cache enabled.

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
            path_template("/zones/{zone_id}/cache/origin_cloud_regions/supported_regions", zone_id=zone_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[OriginCloudRegionSupportedRegionsResponse]]._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[OriginCloudRegionSupportedRegionsResponse]],
                ResultWrapper[OriginCloudRegionSupportedRegionsResponse],
            ),
        )


class AsyncOriginCloudRegionsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncOriginCloudRegionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncOriginCloudRegionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOriginCloudRegionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncOriginCloudRegionsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        zone_id: str,
        ip: str,
        region: str,
        vendor: Literal["aws", "azure", "gcp", "oci"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[OriginCloudRegionCreateResponse]:
        """Adds a single IP-to-cloud-region mapping for the zone.

        The IP must be a valid
        IPv4 or IPv6 address and is normalized to canonical form before storage (RFC
        5952 for IPv6). Returns 400 (code 1145) if a mapping for that IP already exists
        — use PATCH to update an existing entry. The vendor and region are validated
        against the list from
        `GET /zones/{zone_id}/cache/origin_cloud_regions/supported_regions`.

        Args:
          zone_id: Identifier.

          ip: Origin IP address (IPv4 or IPv6). Normalized to canonical form before storage
              (RFC 5952 for IPv6).

          region: Cloud vendor region identifier. Must be a valid region for the specified vendor
              as returned by the supported_regions endpoint.

          vendor: Cloud vendor hosting the origin. Must be one of the supported vendors.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._post(
            path_template("/zones/{zone_id}/cache/origin_cloud_regions", zone_id=zone_id),
            body=await async_maybe_transform(
                {
                    "ip": ip,
                    "region": region,
                    "vendor": vendor,
                },
                origin_cloud_region_create_params.OriginCloudRegionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[OriginCloudRegionCreateResponse]]._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[OriginCloudRegionCreateResponse]], ResultWrapper[OriginCloudRegionCreateResponse]
            ),
        )

    async def list(
        self,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[OriginCloudRegionListResponse]:
        """Returns all IP-to-cloud-region mappings configured for the zone.

        Each mapping
        tells Cloudflare which cloud vendor and region hosts the origin at that IP,
        enabling the edge to route via the nearest Tiered Cache upper-tier co-located
        with that cloud provider. Returns an empty array when no mappings exist.

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
            path_template("/zones/{zone_id}/cache/origin_cloud_regions", zone_id=zone_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[OriginCloudRegionListResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[OriginCloudRegionListResponse]], ResultWrapper[OriginCloudRegionListResponse]),
        )

    async def delete(
        self,
        origin_ip: str,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[OriginCloudRegionDeleteResponse]:
        """Removes the cloud region mapping for a single origin IP address.

        The IP path
        parameter is normalized before lookup. Returns the deleted entry on success.
        Returns 404 (code 1163) if no mapping exists for the specified IP. When the last
        mapping for the zone is removed the underlying rule record is also deleted.

        Args:
          zone_id: Identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not origin_ip:
            raise ValueError(f"Expected a non-empty value for `origin_ip` but received {origin_ip!r}")
        return await self._delete(
            path_template(
                "/zones/{zone_id}/cache/origin_cloud_regions/{origin_ip}", zone_id=zone_id, origin_ip=origin_ip
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[OriginCloudRegionDeleteResponse]]._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[OriginCloudRegionDeleteResponse]], ResultWrapper[OriginCloudRegionDeleteResponse]
            ),
        )

    async def bulk_delete(
        self,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[OriginCloudRegionBulkDeleteResponse]:
        """Removes up to 100 IP-to-cloud-region mappings in a single request.

        Each IP is
        validated independently — successfully deleted items are returned in the
        `succeeded` array and IPs that could not be found or are invalid are returned in
        the `failed` array.

        Args:
          zone_id: Identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._delete(
            path_template("/zones/{zone_id}/cache/origin_cloud_regions/batch", zone_id=zone_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[OriginCloudRegionBulkDeleteResponse]]._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[OriginCloudRegionBulkDeleteResponse]], ResultWrapper[OriginCloudRegionBulkDeleteResponse]
            ),
        )

    async def bulk_edit(
        self,
        *,
        zone_id: str,
        body: Iterable[origin_cloud_region_bulk_edit_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[OriginCloudRegionBulkEditResponse]:
        """Adds or updates up to 100 IP-to-cloud-region mappings in a single request.

        Each
        item is validated independently — valid items are applied and invalid items are
        returned in the `failed` array. The vendor and region for every item are
        validated against the list from
        `GET /zones/{zone_id}/cache/origin_cloud_regions/supported_regions`.

        Args:
          zone_id: Identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._patch(
            path_template("/zones/{zone_id}/cache/origin_cloud_regions/batch", zone_id=zone_id),
            body=await async_maybe_transform(body, Iterable[origin_cloud_region_bulk_edit_params.Body]),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[OriginCloudRegionBulkEditResponse]]._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[OriginCloudRegionBulkEditResponse]], ResultWrapper[OriginCloudRegionBulkEditResponse]
            ),
        )

    async def edit(
        self,
        *,
        zone_id: str,
        ip: str,
        region: str,
        vendor: Literal["aws", "azure", "gcp", "oci"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[OriginCloudRegionEditResponse]:
        """Adds or updates a single IP-to-cloud-region mapping for the zone.

        Unlike POST,
        this operation is idempotent — if a mapping for the IP already exists it is
        overwritten. Returns the complete updated list of all mappings for the zone.
        Returns 403 (code 1164) when the zone has reached the limit of 3,500 IP
        mappings.

        Args:
          zone_id: Identifier.

          ip: Origin IP address (IPv4 or IPv6). Normalized to canonical form before storage
              (RFC 5952 for IPv6).

          region: Cloud vendor region identifier. Must be a valid region for the specified vendor
              as returned by the supported_regions endpoint.

          vendor: Cloud vendor hosting the origin. Must be one of the supported vendors.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._patch(
            path_template("/zones/{zone_id}/cache/origin_cloud_regions", zone_id=zone_id),
            body=await async_maybe_transform(
                {
                    "ip": ip,
                    "region": region,
                    "vendor": vendor,
                },
                origin_cloud_region_edit_params.OriginCloudRegionEditParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[OriginCloudRegionEditResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[OriginCloudRegionEditResponse]], ResultWrapper[OriginCloudRegionEditResponse]),
        )

    async def get(
        self,
        origin_ip: str,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[OriginCloudRegionGetResponse]:
        """Returns the cloud region mapping for a single origin IP address.

        The IP path
        parameter is normalized before lookup (RFC 5952 for IPv6). Returns 404
        (code 1142) if the zone has no mappings or if the specified IP has no mapping.

        Args:
          zone_id: Identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not origin_ip:
            raise ValueError(f"Expected a non-empty value for `origin_ip` but received {origin_ip!r}")
        return await self._get(
            path_template(
                "/zones/{zone_id}/cache/origin_cloud_regions/{origin_ip}", zone_id=zone_id, origin_ip=origin_ip
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[OriginCloudRegionGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[OriginCloudRegionGetResponse]], ResultWrapper[OriginCloudRegionGetResponse]),
        )

    async def supported_regions(
        self,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[OriginCloudRegionSupportedRegionsResponse]:
        """
        Returns the cloud vendors and regions that are valid values for origin cloud
        region mappings. Each region includes the Tiered Cache upper-tier colocation
        codes that will be used for cache routing when a mapping targeting that region
        is active. Requires the zone to have Tiered Cache enabled.

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
            path_template("/zones/{zone_id}/cache/origin_cloud_regions/supported_regions", zone_id=zone_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[OriginCloudRegionSupportedRegionsResponse]]._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[OriginCloudRegionSupportedRegionsResponse]],
                ResultWrapper[OriginCloudRegionSupportedRegionsResponse],
            ),
        )


class OriginCloudRegionsResourceWithRawResponse:
    def __init__(self, origin_cloud_regions: OriginCloudRegionsResource) -> None:
        self._origin_cloud_regions = origin_cloud_regions

        self.create = to_raw_response_wrapper(
            origin_cloud_regions.create,
        )
        self.list = to_raw_response_wrapper(
            origin_cloud_regions.list,
        )
        self.delete = to_raw_response_wrapper(
            origin_cloud_regions.delete,
        )
        self.bulk_delete = to_raw_response_wrapper(
            origin_cloud_regions.bulk_delete,
        )
        self.bulk_edit = to_raw_response_wrapper(
            origin_cloud_regions.bulk_edit,
        )
        self.edit = to_raw_response_wrapper(
            origin_cloud_regions.edit,
        )
        self.get = to_raw_response_wrapper(
            origin_cloud_regions.get,
        )
        self.supported_regions = to_raw_response_wrapper(
            origin_cloud_regions.supported_regions,
        )


class AsyncOriginCloudRegionsResourceWithRawResponse:
    def __init__(self, origin_cloud_regions: AsyncOriginCloudRegionsResource) -> None:
        self._origin_cloud_regions = origin_cloud_regions

        self.create = async_to_raw_response_wrapper(
            origin_cloud_regions.create,
        )
        self.list = async_to_raw_response_wrapper(
            origin_cloud_regions.list,
        )
        self.delete = async_to_raw_response_wrapper(
            origin_cloud_regions.delete,
        )
        self.bulk_delete = async_to_raw_response_wrapper(
            origin_cloud_regions.bulk_delete,
        )
        self.bulk_edit = async_to_raw_response_wrapper(
            origin_cloud_regions.bulk_edit,
        )
        self.edit = async_to_raw_response_wrapper(
            origin_cloud_regions.edit,
        )
        self.get = async_to_raw_response_wrapper(
            origin_cloud_regions.get,
        )
        self.supported_regions = async_to_raw_response_wrapper(
            origin_cloud_regions.supported_regions,
        )


class OriginCloudRegionsResourceWithStreamingResponse:
    def __init__(self, origin_cloud_regions: OriginCloudRegionsResource) -> None:
        self._origin_cloud_regions = origin_cloud_regions

        self.create = to_streamed_response_wrapper(
            origin_cloud_regions.create,
        )
        self.list = to_streamed_response_wrapper(
            origin_cloud_regions.list,
        )
        self.delete = to_streamed_response_wrapper(
            origin_cloud_regions.delete,
        )
        self.bulk_delete = to_streamed_response_wrapper(
            origin_cloud_regions.bulk_delete,
        )
        self.bulk_edit = to_streamed_response_wrapper(
            origin_cloud_regions.bulk_edit,
        )
        self.edit = to_streamed_response_wrapper(
            origin_cloud_regions.edit,
        )
        self.get = to_streamed_response_wrapper(
            origin_cloud_regions.get,
        )
        self.supported_regions = to_streamed_response_wrapper(
            origin_cloud_regions.supported_regions,
        )


class AsyncOriginCloudRegionsResourceWithStreamingResponse:
    def __init__(self, origin_cloud_regions: AsyncOriginCloudRegionsResource) -> None:
        self._origin_cloud_regions = origin_cloud_regions

        self.create = async_to_streamed_response_wrapper(
            origin_cloud_regions.create,
        )
        self.list = async_to_streamed_response_wrapper(
            origin_cloud_regions.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            origin_cloud_regions.delete,
        )
        self.bulk_delete = async_to_streamed_response_wrapper(
            origin_cloud_regions.bulk_delete,
        )
        self.bulk_edit = async_to_streamed_response_wrapper(
            origin_cloud_regions.bulk_edit,
        )
        self.edit = async_to_streamed_response_wrapper(
            origin_cloud_regions.edit,
        )
        self.get = async_to_streamed_response_wrapper(
            origin_cloud_regions.get,
        )
        self.supported_regions = async_to_streamed_response_wrapper(
            origin_cloud_regions.supported_regions,
        )
