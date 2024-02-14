# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Type, cast

import httpx

from ....._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ....._utils import maybe_transform
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....._wrappers import ResultWrapper
from ....._base_client import (
    make_request_options,
)
from .....types.logs.controls.retentions import (
    FlagLogsReceivedGetLogRetentionFlagResponse,
    FlagLogsReceivedUpdateLogRetentionFlagResponse,
    flag_logs_received_update_log_retention_flag_params,
)

__all__ = ["Flags", "AsyncFlags"]


class Flags(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> FlagsWithRawResponse:
        return FlagsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FlagsWithStreamingResponse:
        return FlagsWithStreamingResponse(self)

    def logs_received_get_log_retention_flag(
        self,
        zone_identifier: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FlagLogsReceivedGetLogRetentionFlagResponse:
        """
        Gets log retention flag for Logpull API.

        Args:
          zone_identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_identifier:
            raise ValueError(f"Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}")
        return self._get(
            f"/zones/{zone_identifier}/logs/control/retention/flag",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[FlagLogsReceivedGetLogRetentionFlagResponse],
                ResultWrapper[FlagLogsReceivedGetLogRetentionFlagResponse],
            ),
        )

    def logs_received_update_log_retention_flag(
        self,
        zone_identifier: str,
        *,
        flag: bool,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FlagLogsReceivedUpdateLogRetentionFlagResponse:
        """
        Updates log retention flag for Logpull API.

        Args:
          zone_identifier: Identifier

          flag: The log retention flag for Logpull API.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_identifier:
            raise ValueError(f"Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}")
        return self._post(
            f"/zones/{zone_identifier}/logs/control/retention/flag",
            body=maybe_transform(
                {"flag": flag},
                flag_logs_received_update_log_retention_flag_params.FlagLogsReceivedUpdateLogRetentionFlagParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[FlagLogsReceivedUpdateLogRetentionFlagResponse],
                ResultWrapper[FlagLogsReceivedUpdateLogRetentionFlagResponse],
            ),
        )


class AsyncFlags(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncFlagsWithRawResponse:
        return AsyncFlagsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFlagsWithStreamingResponse:
        return AsyncFlagsWithStreamingResponse(self)

    async def logs_received_get_log_retention_flag(
        self,
        zone_identifier: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FlagLogsReceivedGetLogRetentionFlagResponse:
        """
        Gets log retention flag for Logpull API.

        Args:
          zone_identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_identifier:
            raise ValueError(f"Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}")
        return await self._get(
            f"/zones/{zone_identifier}/logs/control/retention/flag",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[FlagLogsReceivedGetLogRetentionFlagResponse],
                ResultWrapper[FlagLogsReceivedGetLogRetentionFlagResponse],
            ),
        )

    async def logs_received_update_log_retention_flag(
        self,
        zone_identifier: str,
        *,
        flag: bool,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FlagLogsReceivedUpdateLogRetentionFlagResponse:
        """
        Updates log retention flag for Logpull API.

        Args:
          zone_identifier: Identifier

          flag: The log retention flag for Logpull API.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_identifier:
            raise ValueError(f"Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}")
        return await self._post(
            f"/zones/{zone_identifier}/logs/control/retention/flag",
            body=maybe_transform(
                {"flag": flag},
                flag_logs_received_update_log_retention_flag_params.FlagLogsReceivedUpdateLogRetentionFlagParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[FlagLogsReceivedUpdateLogRetentionFlagResponse],
                ResultWrapper[FlagLogsReceivedUpdateLogRetentionFlagResponse],
            ),
        )


class FlagsWithRawResponse:
    def __init__(self, flags: Flags) -> None:
        self._flags = flags

        self.logs_received_get_log_retention_flag = to_raw_response_wrapper(
            flags.logs_received_get_log_retention_flag,
        )
        self.logs_received_update_log_retention_flag = to_raw_response_wrapper(
            flags.logs_received_update_log_retention_flag,
        )


class AsyncFlagsWithRawResponse:
    def __init__(self, flags: AsyncFlags) -> None:
        self._flags = flags

        self.logs_received_get_log_retention_flag = async_to_raw_response_wrapper(
            flags.logs_received_get_log_retention_flag,
        )
        self.logs_received_update_log_retention_flag = async_to_raw_response_wrapper(
            flags.logs_received_update_log_retention_flag,
        )


class FlagsWithStreamingResponse:
    def __init__(self, flags: Flags) -> None:
        self._flags = flags

        self.logs_received_get_log_retention_flag = to_streamed_response_wrapper(
            flags.logs_received_get_log_retention_flag,
        )
        self.logs_received_update_log_retention_flag = to_streamed_response_wrapper(
            flags.logs_received_update_log_retention_flag,
        )


class AsyncFlagsWithStreamingResponse:
    def __init__(self, flags: AsyncFlags) -> None:
        self._flags = flags

        self.logs_received_get_log_retention_flag = async_to_streamed_response_wrapper(
            flags.logs_received_get_log_retention_flag,
        )
        self.logs_received_update_log_retention_flag = async_to_streamed_response_wrapper(
            flags.logs_received_update_log_retention_flag,
        )
