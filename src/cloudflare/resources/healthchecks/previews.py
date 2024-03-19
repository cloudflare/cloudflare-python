# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Type, Optional, cast
from typing_extensions import Literal

import httpx

from ...types import HealthchecksHealthchecks
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
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
from ...types.healthchecks import PreviewDeleteResponse, preview_create_params

__all__ = ["Previews", "AsyncPreviews"]


class Previews(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PreviewsWithRawResponse:
        return PreviewsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PreviewsWithStreamingResponse:
        return PreviewsWithStreamingResponse(self)

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
        http_config: Optional[preview_create_params.HTTPConfig] | NotGiven = NOT_GIVEN,
        interval: int | NotGiven = NOT_GIVEN,
        retries: int | NotGiven = NOT_GIVEN,
        suspended: bool | NotGiven = NOT_GIVEN,
        tcp_config: Optional[preview_create_params.TcpConfig] | NotGiven = NOT_GIVEN,
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
        Create a new preview health check.

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
            f"/zones/{zone_id}/healthchecks/preview",
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
                preview_create_params.PreviewCreateParams,
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
    ) -> PreviewDeleteResponse:
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
            f"/zones/{zone_id}/healthchecks/preview/{healthcheck_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[PreviewDeleteResponse], ResultWrapper[PreviewDeleteResponse]),
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
        Fetch a single configured health check preview.

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
            f"/zones/{zone_id}/healthchecks/preview/{healthcheck_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[HealthchecksHealthchecks], ResultWrapper[HealthchecksHealthchecks]),
        )


class AsyncPreviews(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPreviewsWithRawResponse:
        return AsyncPreviewsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPreviewsWithStreamingResponse:
        return AsyncPreviewsWithStreamingResponse(self)

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
        http_config: Optional[preview_create_params.HTTPConfig] | NotGiven = NOT_GIVEN,
        interval: int | NotGiven = NOT_GIVEN,
        retries: int | NotGiven = NOT_GIVEN,
        suspended: bool | NotGiven = NOT_GIVEN,
        tcp_config: Optional[preview_create_params.TcpConfig] | NotGiven = NOT_GIVEN,
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
        Create a new preview health check.

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
            f"/zones/{zone_id}/healthchecks/preview",
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
                preview_create_params.PreviewCreateParams,
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
    ) -> PreviewDeleteResponse:
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
            f"/zones/{zone_id}/healthchecks/preview/{healthcheck_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[PreviewDeleteResponse], ResultWrapper[PreviewDeleteResponse]),
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
        Fetch a single configured health check preview.

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
            f"/zones/{zone_id}/healthchecks/preview/{healthcheck_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[HealthchecksHealthchecks], ResultWrapper[HealthchecksHealthchecks]),
        )


class PreviewsWithRawResponse:
    def __init__(self, previews: Previews) -> None:
        self._previews = previews

        self.create = to_raw_response_wrapper(
            previews.create,
        )
        self.delete = to_raw_response_wrapper(
            previews.delete,
        )
        self.get = to_raw_response_wrapper(
            previews.get,
        )


class AsyncPreviewsWithRawResponse:
    def __init__(self, previews: AsyncPreviews) -> None:
        self._previews = previews

        self.create = async_to_raw_response_wrapper(
            previews.create,
        )
        self.delete = async_to_raw_response_wrapper(
            previews.delete,
        )
        self.get = async_to_raw_response_wrapper(
            previews.get,
        )


class PreviewsWithStreamingResponse:
    def __init__(self, previews: Previews) -> None:
        self._previews = previews

        self.create = to_streamed_response_wrapper(
            previews.create,
        )
        self.delete = to_streamed_response_wrapper(
            previews.delete,
        )
        self.get = to_streamed_response_wrapper(
            previews.get,
        )


class AsyncPreviewsWithStreamingResponse:
    def __init__(self, previews: AsyncPreviews) -> None:
        self._previews = previews

        self.create = async_to_streamed_response_wrapper(
            previews.create,
        )
        self.delete = async_to_streamed_response_wrapper(
            previews.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            previews.get,
        )
