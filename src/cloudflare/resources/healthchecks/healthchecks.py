# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Type, Optional, cast

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
from .previews import (
    PreviewsResource,
    AsyncPreviewsResource,
    PreviewsResourceWithRawResponse,
    AsyncPreviewsResourceWithRawResponse,
    PreviewsResourceWithStreamingResponse,
    AsyncPreviewsResourceWithStreamingResponse,
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
from ...pagination import SyncV4PagePaginationArray, AsyncV4PagePaginationArray
from ..._base_client import AsyncPaginator, make_request_options
from ...types.healthchecks import (
    healthcheck_edit_params,
    healthcheck_list_params,
    healthcheck_create_params,
    healthcheck_update_params,
)
from ...types.healthchecks.healthcheck import Healthcheck
from ...types.healthchecks.check_region import CheckRegion
from ...types.healthchecks.tcp_configuration_param import TCPConfigurationParam
from ...types.healthchecks.http_configuration_param import HTTPConfigurationParam
from ...types.healthchecks.healthcheck_delete_response import HealthcheckDeleteResponse

__all__ = ["HealthchecksResource", "AsyncHealthchecksResource"]


class HealthchecksResource(SyncAPIResource):
    @cached_property
    def previews(self) -> PreviewsResource:
        return PreviewsResource(self._client)

    @cached_property
    def with_raw_response(self) -> HealthchecksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return HealthchecksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> HealthchecksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return HealthchecksResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        zone_id: str,
        address: str,
        name: str,
        check_regions: Optional[List[CheckRegion]] | NotGiven = NOT_GIVEN,
        consecutive_fails: int | NotGiven = NOT_GIVEN,
        consecutive_successes: int | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        http_config: Optional[HTTPConfigurationParam] | NotGiven = NOT_GIVEN,
        interval: int | NotGiven = NOT_GIVEN,
        retries: int | NotGiven = NOT_GIVEN,
        suspended: bool | NotGiven = NOT_GIVEN,
        tcp_config: Optional[TCPConfigurationParam] | NotGiven = NOT_GIVEN,
        healthcheck_timeout: int | NotGiven = NOT_GIVEN,
        type: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Healthcheck:
        """
        Create a new health check.

        Args:
          zone_id: Identifier

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

          healthcheck_timeout: The timeout (in seconds) before marking the health check as failed.

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
            f"/zones/{zone_id}/healthchecks",
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
                    "healthcheck_timeout": healthcheck_timeout,
                    "type": type,
                },
                healthcheck_create_params.HealthcheckCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Healthcheck]._unwrapper,
            ),
            cast_to=cast(Type[Healthcheck], ResultWrapper[Healthcheck]),
        )

    def update(
        self,
        healthcheck_id: str,
        *,
        zone_id: str,
        address: str,
        name: str,
        check_regions: Optional[List[CheckRegion]] | NotGiven = NOT_GIVEN,
        consecutive_fails: int | NotGiven = NOT_GIVEN,
        consecutive_successes: int | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        http_config: Optional[HTTPConfigurationParam] | NotGiven = NOT_GIVEN,
        interval: int | NotGiven = NOT_GIVEN,
        retries: int | NotGiven = NOT_GIVEN,
        suspended: bool | NotGiven = NOT_GIVEN,
        tcp_config: Optional[TCPConfigurationParam] | NotGiven = NOT_GIVEN,
        healthcheck_timeout: int | NotGiven = NOT_GIVEN,
        type: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Healthcheck:
        """
        Update a configured health check.

        Args:
          zone_id: Identifier

          healthcheck_id: Identifier

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

          healthcheck_timeout: The timeout (in seconds) before marking the health check as failed.

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
        return self._put(
            f"/zones/{zone_id}/healthchecks/{healthcheck_id}",
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
                    "healthcheck_timeout": healthcheck_timeout,
                    "type": type,
                },
                healthcheck_update_params.HealthcheckUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Healthcheck]._unwrapper,
            ),
            cast_to=cast(Type[Healthcheck], ResultWrapper[Healthcheck]),
        )

    def list(
        self,
        *,
        zone_id: str,
        page: float | NotGiven = NOT_GIVEN,
        per_page: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncV4PagePaginationArray[Healthcheck]:
        """
        List configured health checks.

        Args:
          zone_id: Identifier

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
            f"/zones/{zone_id}/healthchecks",
            page=SyncV4PagePaginationArray[Healthcheck],
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
                    healthcheck_list_params.HealthcheckListParams,
                ),
            ),
            model=Healthcheck,
        )

    def delete(
        self,
        healthcheck_id: str,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> HealthcheckDeleteResponse:
        """
        Delete a health check.

        Args:
          zone_id: Identifier

          healthcheck_id: Identifier

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
            f"/zones/{zone_id}/healthchecks/{healthcheck_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[HealthcheckDeleteResponse]._unwrapper,
            ),
            cast_to=cast(Type[HealthcheckDeleteResponse], ResultWrapper[HealthcheckDeleteResponse]),
        )

    def edit(
        self,
        healthcheck_id: str,
        *,
        zone_id: str,
        address: str,
        name: str,
        check_regions: Optional[List[CheckRegion]] | NotGiven = NOT_GIVEN,
        consecutive_fails: int | NotGiven = NOT_GIVEN,
        consecutive_successes: int | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        http_config: Optional[HTTPConfigurationParam] | NotGiven = NOT_GIVEN,
        interval: int | NotGiven = NOT_GIVEN,
        retries: int | NotGiven = NOT_GIVEN,
        suspended: bool | NotGiven = NOT_GIVEN,
        tcp_config: Optional[TCPConfigurationParam] | NotGiven = NOT_GIVEN,
        healthcheck_timeout: int | NotGiven = NOT_GIVEN,
        type: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Healthcheck:
        """
        Patch a configured health check.

        Args:
          zone_id: Identifier

          healthcheck_id: Identifier

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

          healthcheck_timeout: The timeout (in seconds) before marking the health check as failed.

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
            f"/zones/{zone_id}/healthchecks/{healthcheck_id}",
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
                    "healthcheck_timeout": healthcheck_timeout,
                    "type": type,
                },
                healthcheck_edit_params.HealthcheckEditParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Healthcheck]._unwrapper,
            ),
            cast_to=cast(Type[Healthcheck], ResultWrapper[Healthcheck]),
        )

    def get(
        self,
        healthcheck_id: str,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Healthcheck:
        """
        Fetch a single configured health check.

        Args:
          zone_id: Identifier

          healthcheck_id: Identifier

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
            f"/zones/{zone_id}/healthchecks/{healthcheck_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Healthcheck]._unwrapper,
            ),
            cast_to=cast(Type[Healthcheck], ResultWrapper[Healthcheck]),
        )


class AsyncHealthchecksResource(AsyncAPIResource):
    @cached_property
    def previews(self) -> AsyncPreviewsResource:
        return AsyncPreviewsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncHealthchecksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncHealthchecksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncHealthchecksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncHealthchecksResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        zone_id: str,
        address: str,
        name: str,
        check_regions: Optional[List[CheckRegion]] | NotGiven = NOT_GIVEN,
        consecutive_fails: int | NotGiven = NOT_GIVEN,
        consecutive_successes: int | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        http_config: Optional[HTTPConfigurationParam] | NotGiven = NOT_GIVEN,
        interval: int | NotGiven = NOT_GIVEN,
        retries: int | NotGiven = NOT_GIVEN,
        suspended: bool | NotGiven = NOT_GIVEN,
        tcp_config: Optional[TCPConfigurationParam] | NotGiven = NOT_GIVEN,
        healthcheck_timeout: int | NotGiven = NOT_GIVEN,
        type: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Healthcheck:
        """
        Create a new health check.

        Args:
          zone_id: Identifier

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

          healthcheck_timeout: The timeout (in seconds) before marking the health check as failed.

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
            f"/zones/{zone_id}/healthchecks",
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
                    "healthcheck_timeout": healthcheck_timeout,
                    "type": type,
                },
                healthcheck_create_params.HealthcheckCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Healthcheck]._unwrapper,
            ),
            cast_to=cast(Type[Healthcheck], ResultWrapper[Healthcheck]),
        )

    async def update(
        self,
        healthcheck_id: str,
        *,
        zone_id: str,
        address: str,
        name: str,
        check_regions: Optional[List[CheckRegion]] | NotGiven = NOT_GIVEN,
        consecutive_fails: int | NotGiven = NOT_GIVEN,
        consecutive_successes: int | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        http_config: Optional[HTTPConfigurationParam] | NotGiven = NOT_GIVEN,
        interval: int | NotGiven = NOT_GIVEN,
        retries: int | NotGiven = NOT_GIVEN,
        suspended: bool | NotGiven = NOT_GIVEN,
        tcp_config: Optional[TCPConfigurationParam] | NotGiven = NOT_GIVEN,
        healthcheck_timeout: int | NotGiven = NOT_GIVEN,
        type: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Healthcheck:
        """
        Update a configured health check.

        Args:
          zone_id: Identifier

          healthcheck_id: Identifier

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

          healthcheck_timeout: The timeout (in seconds) before marking the health check as failed.

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
        return await self._put(
            f"/zones/{zone_id}/healthchecks/{healthcheck_id}",
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
                    "healthcheck_timeout": healthcheck_timeout,
                    "type": type,
                },
                healthcheck_update_params.HealthcheckUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Healthcheck]._unwrapper,
            ),
            cast_to=cast(Type[Healthcheck], ResultWrapper[Healthcheck]),
        )

    def list(
        self,
        *,
        zone_id: str,
        page: float | NotGiven = NOT_GIVEN,
        per_page: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[Healthcheck, AsyncV4PagePaginationArray[Healthcheck]]:
        """
        List configured health checks.

        Args:
          zone_id: Identifier

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
            f"/zones/{zone_id}/healthchecks",
            page=AsyncV4PagePaginationArray[Healthcheck],
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
                    healthcheck_list_params.HealthcheckListParams,
                ),
            ),
            model=Healthcheck,
        )

    async def delete(
        self,
        healthcheck_id: str,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> HealthcheckDeleteResponse:
        """
        Delete a health check.

        Args:
          zone_id: Identifier

          healthcheck_id: Identifier

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
            f"/zones/{zone_id}/healthchecks/{healthcheck_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[HealthcheckDeleteResponse]._unwrapper,
            ),
            cast_to=cast(Type[HealthcheckDeleteResponse], ResultWrapper[HealthcheckDeleteResponse]),
        )

    async def edit(
        self,
        healthcheck_id: str,
        *,
        zone_id: str,
        address: str,
        name: str,
        check_regions: Optional[List[CheckRegion]] | NotGiven = NOT_GIVEN,
        consecutive_fails: int | NotGiven = NOT_GIVEN,
        consecutive_successes: int | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        http_config: Optional[HTTPConfigurationParam] | NotGiven = NOT_GIVEN,
        interval: int | NotGiven = NOT_GIVEN,
        retries: int | NotGiven = NOT_GIVEN,
        suspended: bool | NotGiven = NOT_GIVEN,
        tcp_config: Optional[TCPConfigurationParam] | NotGiven = NOT_GIVEN,
        healthcheck_timeout: int | NotGiven = NOT_GIVEN,
        type: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Healthcheck:
        """
        Patch a configured health check.

        Args:
          zone_id: Identifier

          healthcheck_id: Identifier

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

          healthcheck_timeout: The timeout (in seconds) before marking the health check as failed.

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
            f"/zones/{zone_id}/healthchecks/{healthcheck_id}",
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
                    "healthcheck_timeout": healthcheck_timeout,
                    "type": type,
                },
                healthcheck_edit_params.HealthcheckEditParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Healthcheck]._unwrapper,
            ),
            cast_to=cast(Type[Healthcheck], ResultWrapper[Healthcheck]),
        )

    async def get(
        self,
        healthcheck_id: str,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Healthcheck:
        """
        Fetch a single configured health check.

        Args:
          zone_id: Identifier

          healthcheck_id: Identifier

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
            f"/zones/{zone_id}/healthchecks/{healthcheck_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Healthcheck]._unwrapper,
            ),
            cast_to=cast(Type[Healthcheck], ResultWrapper[Healthcheck]),
        )


class HealthchecksResourceWithRawResponse:
    def __init__(self, healthchecks: HealthchecksResource) -> None:
        self._healthchecks = healthchecks

        self.create = to_raw_response_wrapper(
            healthchecks.create,
        )
        self.update = to_raw_response_wrapper(
            healthchecks.update,
        )
        self.list = to_raw_response_wrapper(
            healthchecks.list,
        )
        self.delete = to_raw_response_wrapper(
            healthchecks.delete,
        )
        self.edit = to_raw_response_wrapper(
            healthchecks.edit,
        )
        self.get = to_raw_response_wrapper(
            healthchecks.get,
        )

    @cached_property
    def previews(self) -> PreviewsResourceWithRawResponse:
        return PreviewsResourceWithRawResponse(self._healthchecks.previews)


class AsyncHealthchecksResourceWithRawResponse:
    def __init__(self, healthchecks: AsyncHealthchecksResource) -> None:
        self._healthchecks = healthchecks

        self.create = async_to_raw_response_wrapper(
            healthchecks.create,
        )
        self.update = async_to_raw_response_wrapper(
            healthchecks.update,
        )
        self.list = async_to_raw_response_wrapper(
            healthchecks.list,
        )
        self.delete = async_to_raw_response_wrapper(
            healthchecks.delete,
        )
        self.edit = async_to_raw_response_wrapper(
            healthchecks.edit,
        )
        self.get = async_to_raw_response_wrapper(
            healthchecks.get,
        )

    @cached_property
    def previews(self) -> AsyncPreviewsResourceWithRawResponse:
        return AsyncPreviewsResourceWithRawResponse(self._healthchecks.previews)


class HealthchecksResourceWithStreamingResponse:
    def __init__(self, healthchecks: HealthchecksResource) -> None:
        self._healthchecks = healthchecks

        self.create = to_streamed_response_wrapper(
            healthchecks.create,
        )
        self.update = to_streamed_response_wrapper(
            healthchecks.update,
        )
        self.list = to_streamed_response_wrapper(
            healthchecks.list,
        )
        self.delete = to_streamed_response_wrapper(
            healthchecks.delete,
        )
        self.edit = to_streamed_response_wrapper(
            healthchecks.edit,
        )
        self.get = to_streamed_response_wrapper(
            healthchecks.get,
        )

    @cached_property
    def previews(self) -> PreviewsResourceWithStreamingResponse:
        return PreviewsResourceWithStreamingResponse(self._healthchecks.previews)


class AsyncHealthchecksResourceWithStreamingResponse:
    def __init__(self, healthchecks: AsyncHealthchecksResource) -> None:
        self._healthchecks = healthchecks

        self.create = async_to_streamed_response_wrapper(
            healthchecks.create,
        )
        self.update = async_to_streamed_response_wrapper(
            healthchecks.update,
        )
        self.list = async_to_streamed_response_wrapper(
            healthchecks.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            healthchecks.delete,
        )
        self.edit = async_to_streamed_response_wrapper(
            healthchecks.edit,
        )
        self.get = async_to_streamed_response_wrapper(
            healthchecks.get,
        )

    @cached_property
    def previews(self) -> AsyncPreviewsResourceWithStreamingResponse:
        return AsyncPreviewsResourceWithStreamingResponse(self._healthchecks.previews)
