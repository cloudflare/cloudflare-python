# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Type, Iterable, Optional, cast
from typing_extensions import Literal

import httpx

from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._wrappers import ResultWrapper
from ..pagination import SyncV4PagePaginationArray, AsyncV4PagePaginationArray
from .._base_client import AsyncPaginator, make_request_options
from ..types.smart_shield import (
    smart_shield_update_params,
    smart_shield_edit_healthcheck_params,
    smart_shield_list_healthchecks_params,
    smart_shield_create_healthcheck_params,
    smart_shield_update_healthcheck_params,
)
from ..types.shared_params.response_info import ResponseInfo
from ..types.smart_shield.smart_shield_get_response import SmartShieldGetResponse
from ..types.smart_shield.smart_shield_update_response import SmartShieldUpdateResponse
from ..types.smart_shield.smart_shield_get_healthcheck_response import SmartShieldGetHealthcheckResponse
from ..types.smart_shield.smart_shield_edit_healthcheck_response import SmartShieldEditHealthcheckResponse
from ..types.smart_shield.smart_shield_list_healthchecks_response import SmartShieldListHealthchecksResponse
from ..types.smart_shield.smart_shield_create_healthcheck_response import SmartShieldCreateHealthcheckResponse
from ..types.smart_shield.smart_shield_delete_healthcheck_response import SmartShieldDeleteHealthcheckResponse
from ..types.smart_shield.smart_shield_update_healthcheck_response import SmartShieldUpdateHealthcheckResponse

__all__ = ["SmartShieldResource", "AsyncSmartShieldResource"]


class SmartShieldResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SmartShieldResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return SmartShieldResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SmartShieldResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return SmartShieldResourceWithStreamingResponse(self)

    def update(
        self,
        *,
        zone_id: str,
        cache_reserve: smart_shield_update_params.CacheReserve | Omit = omit,
        regional_tiered_cache: smart_shield_update_params.RegionalTieredCache | Omit = omit,
        smart_routing: smart_shield_update_params.SmartRouting | Omit = omit,
        smart_tiered_cache: smart_shield_update_params.SmartTieredCache | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SmartShieldUpdateResponse:
        """
        Set Smart Shield Settings.

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
            f"/zones/{zone_id}/smart_shield",
            body=maybe_transform(
                {
                    "cache_reserve": cache_reserve,
                    "regional_tiered_cache": regional_tiered_cache,
                    "smart_routing": smart_routing,
                    "smart_tiered_cache": smart_tiered_cache,
                },
                smart_shield_update_params.SmartShieldUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[SmartShieldUpdateResponse]._unwrapper,
            ),
            cast_to=cast(Type[SmartShieldUpdateResponse], ResultWrapper[SmartShieldUpdateResponse]),
        )

    def create_healthcheck(
        self,
        *,
        zone_id: str,
        address: str,
        name: str,
        check_regions: Optional[
            List[
                Literal[
                    "WNAM",
                    "ENAM",
                    "WEU",
                    "EEU",
                    "NSAM",
                    "SSAM",
                    "OC",
                    "ME",
                    "NAF",
                    "SAF",
                    "IN",
                    "SEAS",
                    "NEAS",
                    "ALL_REGIONS",
                ]
            ]
        ]
        | Omit = omit,
        consecutive_fails: int | Omit = omit,
        consecutive_successes: int | Omit = omit,
        description: str | Omit = omit,
        http_config: Optional[smart_shield_create_healthcheck_params.HTTPConfig] | Omit = omit,
        interval: int | Omit = omit,
        retries: int | Omit = omit,
        suspended: bool | Omit = omit,
        tcp_config: Optional[smart_shield_create_healthcheck_params.TCPConfig] | Omit = omit,
        api_timeout: int | Omit = omit,
        type: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SmartShieldCreateHealthcheckResponse:
        """
        Create a new health check.

        Args:
          zone_id: Identifier.

          address: The hostname or IP address of the origin server to run health checks on.

          name: A short name to identify the health check. Only alphanumeric characters, hyphens
              and underscores are allowed.

          check_regions: A list of regions from which to run health checks. Null means Cloudflare will
              pick a default region.

          consecutive_fails: The number of consecutive fails required from a health check before changing the
              health to unhealthy.

          consecutive_successes: The number of consecutive successes required from a health check before changing
              the health to healthy.

          description: A human-readable description of the health check.

          http_config: Parameters specific to an HTTP or HTTPS health check.

          interval: The interval between each health check. Shorter intervals may give quicker
              notifications if the origin status changes, but will increase load on the origin
              as we check from multiple locations.

          retries: The number of retries to attempt in case of a timeout before marking the origin
              as unhealthy. Retries are attempted immediately.

          suspended: If suspended, no health checks are sent to the origin.

          tcp_config: Parameters specific to TCP health check.

          api_timeout: The timeout (in seconds) before marking the health check as failed.

          type: The protocol to use for the health check. Currently supported protocols are
              'HTTP', 'HTTPS' and 'TCP'.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._post(
            f"/zones/{zone_id}/smart_shield/healthchecks",
            body=maybe_transform(
                {
                    "address": address,
                    "name": name,
                    "check_regions": check_regions,
                    "consecutive_fails": consecutive_fails,
                    "consecutive_successes": consecutive_successes,
                    "description": description,
                    "http_config": http_config,
                    "interval": interval,
                    "retries": retries,
                    "suspended": suspended,
                    "tcp_config": tcp_config,
                    "api_timeout": api_timeout,
                    "type": type,
                },
                smart_shield_create_healthcheck_params.SmartShieldCreateHealthcheckParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[SmartShieldCreateHealthcheckResponse]._unwrapper,
            ),
            cast_to=cast(
                Type[SmartShieldCreateHealthcheckResponse], ResultWrapper[SmartShieldCreateHealthcheckResponse]
            ),
        )

    def delete_healthcheck(
        self,
        healthcheck_id: str,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SmartShieldDeleteHealthcheckResponse:
        """
        Delete a health check.

        Args:
          zone_id: Identifier.

          healthcheck_id: Identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not healthcheck_id:
            raise ValueError(f"Expected a non-empty value for `healthcheck_id` but received {healthcheck_id!r}")
        return self._delete(
            f"/zones/{zone_id}/smart_shield/healthchecks/{healthcheck_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[SmartShieldDeleteHealthcheckResponse]._unwrapper,
            ),
            cast_to=cast(
                Type[SmartShieldDeleteHealthcheckResponse], ResultWrapper[SmartShieldDeleteHealthcheckResponse]
            ),
        )

    def edit_healthcheck(
        self,
        healthcheck_id: str,
        *,
        zone_id: str,
        address: str,
        name: str,
        check_regions: Optional[
            List[
                Literal[
                    "WNAM",
                    "ENAM",
                    "WEU",
                    "EEU",
                    "NSAM",
                    "SSAM",
                    "OC",
                    "ME",
                    "NAF",
                    "SAF",
                    "IN",
                    "SEAS",
                    "NEAS",
                    "ALL_REGIONS",
                ]
            ]
        ]
        | Omit = omit,
        consecutive_fails: int | Omit = omit,
        consecutive_successes: int | Omit = omit,
        description: str | Omit = omit,
        http_config: Optional[smart_shield_edit_healthcheck_params.HTTPConfig] | Omit = omit,
        interval: int | Omit = omit,
        retries: int | Omit = omit,
        suspended: bool | Omit = omit,
        tcp_config: Optional[smart_shield_edit_healthcheck_params.TCPConfig] | Omit = omit,
        api_timeout: int | Omit = omit,
        type: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SmartShieldEditHealthcheckResponse:
        """
        Patch a configured health check.

        Args:
          zone_id: Identifier.

          healthcheck_id: Identifier.

          address: The hostname or IP address of the origin server to run health checks on.

          name: A short name to identify the health check. Only alphanumeric characters, hyphens
              and underscores are allowed.

          check_regions: A list of regions from which to run health checks. Null means Cloudflare will
              pick a default region.

          consecutive_fails: The number of consecutive fails required from a health check before changing the
              health to unhealthy.

          consecutive_successes: The number of consecutive successes required from a health check before changing
              the health to healthy.

          description: A human-readable description of the health check.

          http_config: Parameters specific to an HTTP or HTTPS health check.

          interval: The interval between each health check. Shorter intervals may give quicker
              notifications if the origin status changes, but will increase load on the origin
              as we check from multiple locations.

          retries: The number of retries to attempt in case of a timeout before marking the origin
              as unhealthy. Retries are attempted immediately.

          suspended: If suspended, no health checks are sent to the origin.

          tcp_config: Parameters specific to TCP health check.

          api_timeout: The timeout (in seconds) before marking the health check as failed.

          type: The protocol to use for the health check. Currently supported protocols are
              'HTTP', 'HTTPS' and 'TCP'.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not healthcheck_id:
            raise ValueError(f"Expected a non-empty value for `healthcheck_id` but received {healthcheck_id!r}")
        return self._patch(
            f"/zones/{zone_id}/smart_shield/healthchecks/{healthcheck_id}",
            body=maybe_transform(
                {
                    "address": address,
                    "name": name,
                    "check_regions": check_regions,
                    "consecutive_fails": consecutive_fails,
                    "consecutive_successes": consecutive_successes,
                    "description": description,
                    "http_config": http_config,
                    "interval": interval,
                    "retries": retries,
                    "suspended": suspended,
                    "tcp_config": tcp_config,
                    "api_timeout": api_timeout,
                    "type": type,
                },
                smart_shield_edit_healthcheck_params.SmartShieldEditHealthcheckParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[SmartShieldEditHealthcheckResponse]._unwrapper,
            ),
            cast_to=cast(Type[SmartShieldEditHealthcheckResponse], ResultWrapper[SmartShieldEditHealthcheckResponse]),
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SmartShieldGetResponse:
        """
        Retrieve Smart Shield Settings.

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
            f"/zones/{zone_id}/smart_shield",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[SmartShieldGetResponse]._unwrapper,
            ),
            cast_to=cast(Type[SmartShieldGetResponse], ResultWrapper[SmartShieldGetResponse]),
        )

    def get_healthcheck(
        self,
        healthcheck_id: str,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SmartShieldGetHealthcheckResponse:
        """
        Fetch a single configured health check.

        Args:
          zone_id: Identifier.

          healthcheck_id: Identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not healthcheck_id:
            raise ValueError(f"Expected a non-empty value for `healthcheck_id` but received {healthcheck_id!r}")
        return self._get(
            f"/zones/{zone_id}/smart_shield/healthchecks/{healthcheck_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[SmartShieldGetHealthcheckResponse]._unwrapper,
            ),
            cast_to=cast(Type[SmartShieldGetHealthcheckResponse], ResultWrapper[SmartShieldGetHealthcheckResponse]),
        )

    def list_healthchecks(
        self,
        *,
        zone_id: str,
        page: float | Omit = omit,
        per_page: float | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncV4PagePaginationArray[SmartShieldListHealthchecksResponse]:
        """
        List configured health checks.

        Args:
          zone_id: Identifier.

          page: Page number of paginated results.

          per_page: Maximum number of results per page. Must be a multiple of 5.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._get_api_list(
            f"/zones/{zone_id}/smart_shield/healthchecks",
            page=SyncV4PagePaginationArray[SmartShieldListHealthchecksResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page": page,
                        "per_page": per_page,
                    },
                    smart_shield_list_healthchecks_params.SmartShieldListHealthchecksParams,
                ),
            ),
            model=SmartShieldListHealthchecksResponse,
        )

    def update_healthcheck(
        self,
        healthcheck_id: str,
        *,
        zone_id: str,
        errors: Iterable[ResponseInfo],
        messages: Iterable[ResponseInfo],
        result: smart_shield_update_healthcheck_params.Result,
        success: Literal[True],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SmartShieldUpdateHealthcheckResponse:
        """
        Update a configured health check.

        Args:
          zone_id: Identifier.

          healthcheck_id: Identifier.

          success: Whether the API call was successful.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not healthcheck_id:
            raise ValueError(f"Expected a non-empty value for `healthcheck_id` but received {healthcheck_id!r}")
        return self._put(
            f"/zones/{zone_id}/smart_shield/healthchecks/{healthcheck_id}",
            body=maybe_transform(
                {
                    "errors": errors,
                    "messages": messages,
                    "result": result,
                    "success": success,
                },
                smart_shield_update_healthcheck_params.SmartShieldUpdateHealthcheckParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[SmartShieldUpdateHealthcheckResponse]._unwrapper,
            ),
            cast_to=cast(
                Type[SmartShieldUpdateHealthcheckResponse], ResultWrapper[SmartShieldUpdateHealthcheckResponse]
            ),
        )


class AsyncSmartShieldResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSmartShieldResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSmartShieldResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSmartShieldResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncSmartShieldResourceWithStreamingResponse(self)

    async def update(
        self,
        *,
        zone_id: str,
        cache_reserve: smart_shield_update_params.CacheReserve | Omit = omit,
        regional_tiered_cache: smart_shield_update_params.RegionalTieredCache | Omit = omit,
        smart_routing: smart_shield_update_params.SmartRouting | Omit = omit,
        smart_tiered_cache: smart_shield_update_params.SmartTieredCache | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SmartShieldUpdateResponse:
        """
        Set Smart Shield Settings.

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
            f"/zones/{zone_id}/smart_shield",
            body=await async_maybe_transform(
                {
                    "cache_reserve": cache_reserve,
                    "regional_tiered_cache": regional_tiered_cache,
                    "smart_routing": smart_routing,
                    "smart_tiered_cache": smart_tiered_cache,
                },
                smart_shield_update_params.SmartShieldUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[SmartShieldUpdateResponse]._unwrapper,
            ),
            cast_to=cast(Type[SmartShieldUpdateResponse], ResultWrapper[SmartShieldUpdateResponse]),
        )

    async def create_healthcheck(
        self,
        *,
        zone_id: str,
        address: str,
        name: str,
        check_regions: Optional[
            List[
                Literal[
                    "WNAM",
                    "ENAM",
                    "WEU",
                    "EEU",
                    "NSAM",
                    "SSAM",
                    "OC",
                    "ME",
                    "NAF",
                    "SAF",
                    "IN",
                    "SEAS",
                    "NEAS",
                    "ALL_REGIONS",
                ]
            ]
        ]
        | Omit = omit,
        consecutive_fails: int | Omit = omit,
        consecutive_successes: int | Omit = omit,
        description: str | Omit = omit,
        http_config: Optional[smart_shield_create_healthcheck_params.HTTPConfig] | Omit = omit,
        interval: int | Omit = omit,
        retries: int | Omit = omit,
        suspended: bool | Omit = omit,
        tcp_config: Optional[smart_shield_create_healthcheck_params.TCPConfig] | Omit = omit,
        api_timeout: int | Omit = omit,
        type: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SmartShieldCreateHealthcheckResponse:
        """
        Create a new health check.

        Args:
          zone_id: Identifier.

          address: The hostname or IP address of the origin server to run health checks on.

          name: A short name to identify the health check. Only alphanumeric characters, hyphens
              and underscores are allowed.

          check_regions: A list of regions from which to run health checks. Null means Cloudflare will
              pick a default region.

          consecutive_fails: The number of consecutive fails required from a health check before changing the
              health to unhealthy.

          consecutive_successes: The number of consecutive successes required from a health check before changing
              the health to healthy.

          description: A human-readable description of the health check.

          http_config: Parameters specific to an HTTP or HTTPS health check.

          interval: The interval between each health check. Shorter intervals may give quicker
              notifications if the origin status changes, but will increase load on the origin
              as we check from multiple locations.

          retries: The number of retries to attempt in case of a timeout before marking the origin
              as unhealthy. Retries are attempted immediately.

          suspended: If suspended, no health checks are sent to the origin.

          tcp_config: Parameters specific to TCP health check.

          api_timeout: The timeout (in seconds) before marking the health check as failed.

          type: The protocol to use for the health check. Currently supported protocols are
              'HTTP', 'HTTPS' and 'TCP'.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._post(
            f"/zones/{zone_id}/smart_shield/healthchecks",
            body=await async_maybe_transform(
                {
                    "address": address,
                    "name": name,
                    "check_regions": check_regions,
                    "consecutive_fails": consecutive_fails,
                    "consecutive_successes": consecutive_successes,
                    "description": description,
                    "http_config": http_config,
                    "interval": interval,
                    "retries": retries,
                    "suspended": suspended,
                    "tcp_config": tcp_config,
                    "api_timeout": api_timeout,
                    "type": type,
                },
                smart_shield_create_healthcheck_params.SmartShieldCreateHealthcheckParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[SmartShieldCreateHealthcheckResponse]._unwrapper,
            ),
            cast_to=cast(
                Type[SmartShieldCreateHealthcheckResponse], ResultWrapper[SmartShieldCreateHealthcheckResponse]
            ),
        )

    async def delete_healthcheck(
        self,
        healthcheck_id: str,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SmartShieldDeleteHealthcheckResponse:
        """
        Delete a health check.

        Args:
          zone_id: Identifier.

          healthcheck_id: Identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not healthcheck_id:
            raise ValueError(f"Expected a non-empty value for `healthcheck_id` but received {healthcheck_id!r}")
        return await self._delete(
            f"/zones/{zone_id}/smart_shield/healthchecks/{healthcheck_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[SmartShieldDeleteHealthcheckResponse]._unwrapper,
            ),
            cast_to=cast(
                Type[SmartShieldDeleteHealthcheckResponse], ResultWrapper[SmartShieldDeleteHealthcheckResponse]
            ),
        )

    async def edit_healthcheck(
        self,
        healthcheck_id: str,
        *,
        zone_id: str,
        address: str,
        name: str,
        check_regions: Optional[
            List[
                Literal[
                    "WNAM",
                    "ENAM",
                    "WEU",
                    "EEU",
                    "NSAM",
                    "SSAM",
                    "OC",
                    "ME",
                    "NAF",
                    "SAF",
                    "IN",
                    "SEAS",
                    "NEAS",
                    "ALL_REGIONS",
                ]
            ]
        ]
        | Omit = omit,
        consecutive_fails: int | Omit = omit,
        consecutive_successes: int | Omit = omit,
        description: str | Omit = omit,
        http_config: Optional[smart_shield_edit_healthcheck_params.HTTPConfig] | Omit = omit,
        interval: int | Omit = omit,
        retries: int | Omit = omit,
        suspended: bool | Omit = omit,
        tcp_config: Optional[smart_shield_edit_healthcheck_params.TCPConfig] | Omit = omit,
        api_timeout: int | Omit = omit,
        type: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SmartShieldEditHealthcheckResponse:
        """
        Patch a configured health check.

        Args:
          zone_id: Identifier.

          healthcheck_id: Identifier.

          address: The hostname or IP address of the origin server to run health checks on.

          name: A short name to identify the health check. Only alphanumeric characters, hyphens
              and underscores are allowed.

          check_regions: A list of regions from which to run health checks. Null means Cloudflare will
              pick a default region.

          consecutive_fails: The number of consecutive fails required from a health check before changing the
              health to unhealthy.

          consecutive_successes: The number of consecutive successes required from a health check before changing
              the health to healthy.

          description: A human-readable description of the health check.

          http_config: Parameters specific to an HTTP or HTTPS health check.

          interval: The interval between each health check. Shorter intervals may give quicker
              notifications if the origin status changes, but will increase load on the origin
              as we check from multiple locations.

          retries: The number of retries to attempt in case of a timeout before marking the origin
              as unhealthy. Retries are attempted immediately.

          suspended: If suspended, no health checks are sent to the origin.

          tcp_config: Parameters specific to TCP health check.

          api_timeout: The timeout (in seconds) before marking the health check as failed.

          type: The protocol to use for the health check. Currently supported protocols are
              'HTTP', 'HTTPS' and 'TCP'.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not healthcheck_id:
            raise ValueError(f"Expected a non-empty value for `healthcheck_id` but received {healthcheck_id!r}")
        return await self._patch(
            f"/zones/{zone_id}/smart_shield/healthchecks/{healthcheck_id}",
            body=await async_maybe_transform(
                {
                    "address": address,
                    "name": name,
                    "check_regions": check_regions,
                    "consecutive_fails": consecutive_fails,
                    "consecutive_successes": consecutive_successes,
                    "description": description,
                    "http_config": http_config,
                    "interval": interval,
                    "retries": retries,
                    "suspended": suspended,
                    "tcp_config": tcp_config,
                    "api_timeout": api_timeout,
                    "type": type,
                },
                smart_shield_edit_healthcheck_params.SmartShieldEditHealthcheckParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[SmartShieldEditHealthcheckResponse]._unwrapper,
            ),
            cast_to=cast(Type[SmartShieldEditHealthcheckResponse], ResultWrapper[SmartShieldEditHealthcheckResponse]),
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SmartShieldGetResponse:
        """
        Retrieve Smart Shield Settings.

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
            f"/zones/{zone_id}/smart_shield",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[SmartShieldGetResponse]._unwrapper,
            ),
            cast_to=cast(Type[SmartShieldGetResponse], ResultWrapper[SmartShieldGetResponse]),
        )

    async def get_healthcheck(
        self,
        healthcheck_id: str,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SmartShieldGetHealthcheckResponse:
        """
        Fetch a single configured health check.

        Args:
          zone_id: Identifier.

          healthcheck_id: Identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not healthcheck_id:
            raise ValueError(f"Expected a non-empty value for `healthcheck_id` but received {healthcheck_id!r}")
        return await self._get(
            f"/zones/{zone_id}/smart_shield/healthchecks/{healthcheck_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[SmartShieldGetHealthcheckResponse]._unwrapper,
            ),
            cast_to=cast(Type[SmartShieldGetHealthcheckResponse], ResultWrapper[SmartShieldGetHealthcheckResponse]),
        )

    def list_healthchecks(
        self,
        *,
        zone_id: str,
        page: float | Omit = omit,
        per_page: float | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[
        SmartShieldListHealthchecksResponse, AsyncV4PagePaginationArray[SmartShieldListHealthchecksResponse]
    ]:
        """
        List configured health checks.

        Args:
          zone_id: Identifier.

          page: Page number of paginated results.

          per_page: Maximum number of results per page. Must be a multiple of 5.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._get_api_list(
            f"/zones/{zone_id}/smart_shield/healthchecks",
            page=AsyncV4PagePaginationArray[SmartShieldListHealthchecksResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page": page,
                        "per_page": per_page,
                    },
                    smart_shield_list_healthchecks_params.SmartShieldListHealthchecksParams,
                ),
            ),
            model=SmartShieldListHealthchecksResponse,
        )

    async def update_healthcheck(
        self,
        healthcheck_id: str,
        *,
        zone_id: str,
        errors: Iterable[ResponseInfo],
        messages: Iterable[ResponseInfo],
        result: smart_shield_update_healthcheck_params.Result,
        success: Literal[True],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SmartShieldUpdateHealthcheckResponse:
        """
        Update a configured health check.

        Args:
          zone_id: Identifier.

          healthcheck_id: Identifier.

          success: Whether the API call was successful.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not healthcheck_id:
            raise ValueError(f"Expected a non-empty value for `healthcheck_id` but received {healthcheck_id!r}")
        return await self._put(
            f"/zones/{zone_id}/smart_shield/healthchecks/{healthcheck_id}",
            body=await async_maybe_transform(
                {
                    "errors": errors,
                    "messages": messages,
                    "result": result,
                    "success": success,
                },
                smart_shield_update_healthcheck_params.SmartShieldUpdateHealthcheckParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[SmartShieldUpdateHealthcheckResponse]._unwrapper,
            ),
            cast_to=cast(
                Type[SmartShieldUpdateHealthcheckResponse], ResultWrapper[SmartShieldUpdateHealthcheckResponse]
            ),
        )


class SmartShieldResourceWithRawResponse:
    def __init__(self, smart_shield: SmartShieldResource) -> None:
        self._smart_shield = smart_shield

        self.update = to_raw_response_wrapper(
            smart_shield.update,
        )
        self.create_healthcheck = to_raw_response_wrapper(
            smart_shield.create_healthcheck,
        )
        self.delete_healthcheck = to_raw_response_wrapper(
            smart_shield.delete_healthcheck,
        )
        self.edit_healthcheck = to_raw_response_wrapper(
            smart_shield.edit_healthcheck,
        )
        self.get = to_raw_response_wrapper(
            smart_shield.get,
        )
        self.get_healthcheck = to_raw_response_wrapper(
            smart_shield.get_healthcheck,
        )
        self.list_healthchecks = to_raw_response_wrapper(
            smart_shield.list_healthchecks,
        )
        self.update_healthcheck = to_raw_response_wrapper(
            smart_shield.update_healthcheck,
        )


class AsyncSmartShieldResourceWithRawResponse:
    def __init__(self, smart_shield: AsyncSmartShieldResource) -> None:
        self._smart_shield = smart_shield

        self.update = async_to_raw_response_wrapper(
            smart_shield.update,
        )
        self.create_healthcheck = async_to_raw_response_wrapper(
            smart_shield.create_healthcheck,
        )
        self.delete_healthcheck = async_to_raw_response_wrapper(
            smart_shield.delete_healthcheck,
        )
        self.edit_healthcheck = async_to_raw_response_wrapper(
            smart_shield.edit_healthcheck,
        )
        self.get = async_to_raw_response_wrapper(
            smart_shield.get,
        )
        self.get_healthcheck = async_to_raw_response_wrapper(
            smart_shield.get_healthcheck,
        )
        self.list_healthchecks = async_to_raw_response_wrapper(
            smart_shield.list_healthchecks,
        )
        self.update_healthcheck = async_to_raw_response_wrapper(
            smart_shield.update_healthcheck,
        )


class SmartShieldResourceWithStreamingResponse:
    def __init__(self, smart_shield: SmartShieldResource) -> None:
        self._smart_shield = smart_shield

        self.update = to_streamed_response_wrapper(
            smart_shield.update,
        )
        self.create_healthcheck = to_streamed_response_wrapper(
            smart_shield.create_healthcheck,
        )
        self.delete_healthcheck = to_streamed_response_wrapper(
            smart_shield.delete_healthcheck,
        )
        self.edit_healthcheck = to_streamed_response_wrapper(
            smart_shield.edit_healthcheck,
        )
        self.get = to_streamed_response_wrapper(
            smart_shield.get,
        )
        self.get_healthcheck = to_streamed_response_wrapper(
            smart_shield.get_healthcheck,
        )
        self.list_healthchecks = to_streamed_response_wrapper(
            smart_shield.list_healthchecks,
        )
        self.update_healthcheck = to_streamed_response_wrapper(
            smart_shield.update_healthcheck,
        )


class AsyncSmartShieldResourceWithStreamingResponse:
    def __init__(self, smart_shield: AsyncSmartShieldResource) -> None:
        self._smart_shield = smart_shield

        self.update = async_to_streamed_response_wrapper(
            smart_shield.update,
        )
        self.create_healthcheck = async_to_streamed_response_wrapper(
            smart_shield.create_healthcheck,
        )
        self.delete_healthcheck = async_to_streamed_response_wrapper(
            smart_shield.delete_healthcheck,
        )
        self.edit_healthcheck = async_to_streamed_response_wrapper(
            smart_shield.edit_healthcheck,
        )
        self.get = async_to_streamed_response_wrapper(
            smart_shield.get,
        )
        self.get_healthcheck = async_to_streamed_response_wrapper(
            smart_shield.get_healthcheck,
        )
        self.list_healthchecks = async_to_streamed_response_wrapper(
            smart_shield.list_healthchecks,
        )
        self.update_healthcheck = async_to_streamed_response_wrapper(
            smart_shield.update_healthcheck,
        )
