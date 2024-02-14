# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from ..._compat import cached_property

from ...types.healthchecks import (
    PreviewDeleteResponse,
    PreviewGetResponse,
    PreviewHealthChecksCreatePreviewHealthCheckResponse,
    preview_health_checks_create_preview_health_check_params,
)

from typing import Type, Optional, List

from typing_extensions import Literal

from ..._response import (
    to_raw_response_wrapper,
    async_to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_streamed_response_wrapper,
)

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ..._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ..._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._base_client import (
    SyncAPIClient,
    AsyncAPIClient,
    _merge_mappings,
    AsyncPaginator,
    make_request_options,
    HttpxBinaryResponseContent,
)
from ...types import shared_params
from ...types.healthchecks import preview_health_checks_create_preview_health_check_params
from ..._wrappers import ResultWrapper
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast

__all__ = ["Previews", "AsyncPreviews"]


class Previews(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PreviewsWithRawResponse:
        return PreviewsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PreviewsWithStreamingResponse:
        return PreviewsWithStreamingResponse(self)

    def delete(
        self,
        identifier: str,
        *,
        zone_identifier: str,
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
          zone_identifier: Identifier

          identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_identifier:
            raise ValueError(f"Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}")
        if not identifier:
            raise ValueError(f"Expected a non-empty value for `identifier` but received {identifier!r}")
        return self._delete(
            f"/zones/{zone_identifier}/healthchecks/preview/{identifier}",
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
        identifier: str,
        *,
        zone_identifier: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PreviewGetResponse:
        """
        Fetch a single configured health check preview.

        Args:
          zone_identifier: Identifier

          identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_identifier:
            raise ValueError(f"Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}")
        if not identifier:
            raise ValueError(f"Expected a non-empty value for `identifier` but received {identifier!r}")
        return self._get(
            f"/zones/{zone_identifier}/healthchecks/preview/{identifier}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[PreviewGetResponse], ResultWrapper[PreviewGetResponse]),
        )

    def health_checks_create_preview_health_check(
        self,
        zone_identifier: str,
        *,
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
        http_config: Optional[preview_health_checks_create_preview_health_check_params.HTTPConfig]
        | NotGiven = NOT_GIVEN,
        interval: int | NotGiven = NOT_GIVEN,
        retries: int | NotGiven = NOT_GIVEN,
        suspended: bool | NotGiven = NOT_GIVEN,
        tcp_config: Optional[preview_health_checks_create_preview_health_check_params.TcpConfig] | NotGiven = NOT_GIVEN,
        api_timeout: int | NotGiven = NOT_GIVEN,
        type: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PreviewHealthChecksCreatePreviewHealthCheckResponse:
        """
        Create a new preview health check.

        Args:
          zone_identifier: Identifier

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
        if not zone_identifier:
            raise ValueError(f"Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}")
        return self._post(
            f"/zones/{zone_identifier}/healthchecks/preview",
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
                    "timeout": api_timeout,
                    "type": type,
                },
                preview_health_checks_create_preview_health_check_params.PreviewHealthChecksCreatePreviewHealthCheckParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[PreviewHealthChecksCreatePreviewHealthCheckResponse],
                ResultWrapper[PreviewHealthChecksCreatePreviewHealthCheckResponse],
            ),
        )


class AsyncPreviews(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPreviewsWithRawResponse:
        return AsyncPreviewsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPreviewsWithStreamingResponse:
        return AsyncPreviewsWithStreamingResponse(self)

    async def delete(
        self,
        identifier: str,
        *,
        zone_identifier: str,
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
          zone_identifier: Identifier

          identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_identifier:
            raise ValueError(f"Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}")
        if not identifier:
            raise ValueError(f"Expected a non-empty value for `identifier` but received {identifier!r}")
        return await self._delete(
            f"/zones/{zone_identifier}/healthchecks/preview/{identifier}",
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
        identifier: str,
        *,
        zone_identifier: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PreviewGetResponse:
        """
        Fetch a single configured health check preview.

        Args:
          zone_identifier: Identifier

          identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_identifier:
            raise ValueError(f"Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}")
        if not identifier:
            raise ValueError(f"Expected a non-empty value for `identifier` but received {identifier!r}")
        return await self._get(
            f"/zones/{zone_identifier}/healthchecks/preview/{identifier}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[PreviewGetResponse], ResultWrapper[PreviewGetResponse]),
        )

    async def health_checks_create_preview_health_check(
        self,
        zone_identifier: str,
        *,
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
        http_config: Optional[preview_health_checks_create_preview_health_check_params.HTTPConfig]
        | NotGiven = NOT_GIVEN,
        interval: int | NotGiven = NOT_GIVEN,
        retries: int | NotGiven = NOT_GIVEN,
        suspended: bool | NotGiven = NOT_GIVEN,
        tcp_config: Optional[preview_health_checks_create_preview_health_check_params.TcpConfig] | NotGiven = NOT_GIVEN,
        api_timeout: int | NotGiven = NOT_GIVEN,
        type: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PreviewHealthChecksCreatePreviewHealthCheckResponse:
        """
        Create a new preview health check.

        Args:
          zone_identifier: Identifier

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
        if not zone_identifier:
            raise ValueError(f"Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}")
        return await self._post(
            f"/zones/{zone_identifier}/healthchecks/preview",
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
                    "timeout": api_timeout,
                    "type": type,
                },
                preview_health_checks_create_preview_health_check_params.PreviewHealthChecksCreatePreviewHealthCheckParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[PreviewHealthChecksCreatePreviewHealthCheckResponse],
                ResultWrapper[PreviewHealthChecksCreatePreviewHealthCheckResponse],
            ),
        )


class PreviewsWithRawResponse:
    def __init__(self, previews: Previews) -> None:
        self._previews = previews

        self.delete = to_raw_response_wrapper(
            previews.delete,
        )
        self.get = to_raw_response_wrapper(
            previews.get,
        )
        self.health_checks_create_preview_health_check = to_raw_response_wrapper(
            previews.health_checks_create_preview_health_check,
        )


class AsyncPreviewsWithRawResponse:
    def __init__(self, previews: AsyncPreviews) -> None:
        self._previews = previews

        self.delete = async_to_raw_response_wrapper(
            previews.delete,
        )
        self.get = async_to_raw_response_wrapper(
            previews.get,
        )
        self.health_checks_create_preview_health_check = async_to_raw_response_wrapper(
            previews.health_checks_create_preview_health_check,
        )


class PreviewsWithStreamingResponse:
    def __init__(self, previews: Previews) -> None:
        self._previews = previews

        self.delete = to_streamed_response_wrapper(
            previews.delete,
        )
        self.get = to_streamed_response_wrapper(
            previews.get,
        )
        self.health_checks_create_preview_health_check = to_streamed_response_wrapper(
            previews.health_checks_create_preview_health_check,
        )


class AsyncPreviewsWithStreamingResponse:
    def __init__(self, previews: AsyncPreviews) -> None:
        self._previews = previews

        self.delete = async_to_streamed_response_wrapper(
            previews.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            previews.get,
        )
        self.health_checks_create_preview_health_check = async_to_streamed_response_wrapper(
            previews.health_checks_create_preview_health_check,
        )
