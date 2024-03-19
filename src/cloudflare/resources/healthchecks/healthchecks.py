# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Type, Optional, cast
from typing_extensions import Literal

import httpx

from ...types import (
    HealthcheckListResponse,
    HealthchecksHealthchecks,
    HealthcheckDeleteResponse,
    healthcheck_edit_params,
    healthcheck_create_params,
    healthcheck_update_params,
)
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
from .previews import (
    Previews,
    AsyncPreviews,
    PreviewsWithRawResponse,
    AsyncPreviewsWithRawResponse,
    PreviewsWithStreamingResponse,
    AsyncPreviewsWithStreamingResponse,
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
from ..._base_client import (
    make_request_options,
)

__all__ = ["Healthchecks", "AsyncHealthchecks"]


class Healthchecks(SyncAPIResource):
    @cached_property
    def previews(self) -> Previews:
        return Previews(self._client)

    @cached_property
    def with_raw_response(self) -> HealthchecksWithRawResponse:
        return HealthchecksWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> HealthchecksWithStreamingResponse:
        return HealthchecksWithStreamingResponse(self)

    def create(
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
        | NotGiven = NOT_GIVEN,
        consecutive_fails: int | NotGiven = NOT_GIVEN,
        consecutive_successes: int | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        http_config: Optional[healthcheck_create_params.HTTPConfig] | NotGiven = NOT_GIVEN,
        interval: int | NotGiven = NOT_GIVEN,
        retries: int | NotGiven = NOT_GIVEN,
        suspended: bool | NotGiven = NOT_GIVEN,
        tcp_config: Optional[healthcheck_create_params.TcpConfig] | NotGiven = NOT_GIVEN,
        healthcheck_timeout: int | NotGiven = NOT_GIVEN,
        type: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> HealthchecksHealthchecks:
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
                    "timeout": healthcheck_timeout,
                    "type": type,
                },
                healthcheck_create_params.HealthcheckCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[HealthchecksHealthchecks], ResultWrapper[HealthchecksHealthchecks]),
        )

    def update(
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
        | NotGiven = NOT_GIVEN,
        consecutive_fails: int | NotGiven = NOT_GIVEN,
        consecutive_successes: int | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        http_config: Optional[healthcheck_update_params.HTTPConfig] | NotGiven = NOT_GIVEN,
        interval: int | NotGiven = NOT_GIVEN,
        retries: int | NotGiven = NOT_GIVEN,
        suspended: bool | NotGiven = NOT_GIVEN,
        tcp_config: Optional[healthcheck_update_params.TcpConfig] | NotGiven = NOT_GIVEN,
        healthcheck_timeout: int | NotGiven = NOT_GIVEN,
        type: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> HealthchecksHealthchecks:
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
                    "timeout": healthcheck_timeout,
                    "type": type,
                },
                healthcheck_update_params.HealthcheckUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[HealthchecksHealthchecks], ResultWrapper[HealthchecksHealthchecks]),
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
    ) -> Optional[HealthcheckListResponse]:
        """
        List configured health checks.

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
            f"/zones/{zone_id}/healthchecks",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[HealthcheckListResponse]], ResultWrapper[HealthcheckListResponse]),
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
                post_parser=ResultWrapper._unwrapper,
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
        | NotGiven = NOT_GIVEN,
        consecutive_fails: int | NotGiven = NOT_GIVEN,
        consecutive_successes: int | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        http_config: Optional[healthcheck_edit_params.HTTPConfig] | NotGiven = NOT_GIVEN,
        interval: int | NotGiven = NOT_GIVEN,
        retries: int | NotGiven = NOT_GIVEN,
        suspended: bool | NotGiven = NOT_GIVEN,
        tcp_config: Optional[healthcheck_edit_params.TcpConfig] | NotGiven = NOT_GIVEN,
        healthcheck_timeout: int | NotGiven = NOT_GIVEN,
        type: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> HealthchecksHealthchecks:
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
                    "timeout": healthcheck_timeout,
                    "type": type,
                },
                healthcheck_edit_params.HealthcheckEditParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[HealthchecksHealthchecks], ResultWrapper[HealthchecksHealthchecks]),
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
    ) -> HealthchecksHealthchecks:
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
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[HealthchecksHealthchecks], ResultWrapper[HealthchecksHealthchecks]),
        )


class AsyncHealthchecks(AsyncAPIResource):
    @cached_property
    def previews(self) -> AsyncPreviews:
        return AsyncPreviews(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncHealthchecksWithRawResponse:
        return AsyncHealthchecksWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncHealthchecksWithStreamingResponse:
        return AsyncHealthchecksWithStreamingResponse(self)

    async def create(
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
        | NotGiven = NOT_GIVEN,
        consecutive_fails: int | NotGiven = NOT_GIVEN,
        consecutive_successes: int | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        http_config: Optional[healthcheck_create_params.HTTPConfig] | NotGiven = NOT_GIVEN,
        interval: int | NotGiven = NOT_GIVEN,
        retries: int | NotGiven = NOT_GIVEN,
        suspended: bool | NotGiven = NOT_GIVEN,
        tcp_config: Optional[healthcheck_create_params.TcpConfig] | NotGiven = NOT_GIVEN,
        healthcheck_timeout: int | NotGiven = NOT_GIVEN,
        type: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> HealthchecksHealthchecks:
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
                    "timeout": healthcheck_timeout,
                    "type": type,
                },
                healthcheck_create_params.HealthcheckCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[HealthchecksHealthchecks], ResultWrapper[HealthchecksHealthchecks]),
        )

    async def update(
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
        | NotGiven = NOT_GIVEN,
        consecutive_fails: int | NotGiven = NOT_GIVEN,
        consecutive_successes: int | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        http_config: Optional[healthcheck_update_params.HTTPConfig] | NotGiven = NOT_GIVEN,
        interval: int | NotGiven = NOT_GIVEN,
        retries: int | NotGiven = NOT_GIVEN,
        suspended: bool | NotGiven = NOT_GIVEN,
        tcp_config: Optional[healthcheck_update_params.TcpConfig] | NotGiven = NOT_GIVEN,
        healthcheck_timeout: int | NotGiven = NOT_GIVEN,
        type: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> HealthchecksHealthchecks:
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
                    "timeout": healthcheck_timeout,
                    "type": type,
                },
                healthcheck_update_params.HealthcheckUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[HealthchecksHealthchecks], ResultWrapper[HealthchecksHealthchecks]),
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[HealthcheckListResponse]:
        """
        List configured health checks.

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
            f"/zones/{zone_id}/healthchecks",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[HealthcheckListResponse]], ResultWrapper[HealthcheckListResponse]),
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
                post_parser=ResultWrapper._unwrapper,
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
        | NotGiven = NOT_GIVEN,
        consecutive_fails: int | NotGiven = NOT_GIVEN,
        consecutive_successes: int | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        http_config: Optional[healthcheck_edit_params.HTTPConfig] | NotGiven = NOT_GIVEN,
        interval: int | NotGiven = NOT_GIVEN,
        retries: int | NotGiven = NOT_GIVEN,
        suspended: bool | NotGiven = NOT_GIVEN,
        tcp_config: Optional[healthcheck_edit_params.TcpConfig] | NotGiven = NOT_GIVEN,
        healthcheck_timeout: int | NotGiven = NOT_GIVEN,
        type: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> HealthchecksHealthchecks:
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
                    "timeout": healthcheck_timeout,
                    "type": type,
                },
                healthcheck_edit_params.HealthcheckEditParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[HealthchecksHealthchecks], ResultWrapper[HealthchecksHealthchecks]),
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
    ) -> HealthchecksHealthchecks:
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
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[HealthchecksHealthchecks], ResultWrapper[HealthchecksHealthchecks]),
        )


class HealthchecksWithRawResponse:
    def __init__(self, healthchecks: Healthchecks) -> None:
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
    def previews(self) -> PreviewsWithRawResponse:
        return PreviewsWithRawResponse(self._healthchecks.previews)


class AsyncHealthchecksWithRawResponse:
    def __init__(self, healthchecks: AsyncHealthchecks) -> None:
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
    def previews(self) -> AsyncPreviewsWithRawResponse:
        return AsyncPreviewsWithRawResponse(self._healthchecks.previews)


class HealthchecksWithStreamingResponse:
    def __init__(self, healthchecks: Healthchecks) -> None:
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
    def previews(self) -> PreviewsWithStreamingResponse:
        return PreviewsWithStreamingResponse(self._healthchecks.previews)


class AsyncHealthchecksWithStreamingResponse:
    def __init__(self, healthchecks: AsyncHealthchecks) -> None:
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
    def previews(self) -> AsyncPreviewsWithStreamingResponse:
        return AsyncPreviewsWithStreamingResponse(self._healthchecks.previews)
