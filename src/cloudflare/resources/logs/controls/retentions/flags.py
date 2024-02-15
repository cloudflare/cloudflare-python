# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from ....._compat import cached_property

from .....types.logs.controls.retentions import (
    FlagLogsReceivedGetLogRetentionFlagResponse,
    FlagLogsReceivedUpdateLogRetentionFlagResponse,
)

from typing import Type

from ....._response import (
    to_raw_response_wrapper,
    async_to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_streamed_response_wrapper,
)

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ....._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ....._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._base_client import (
    SyncAPIClient,
    AsyncAPIClient,
    _merge_mappings,
    AsyncPaginator,
    make_request_options,
    HttpxBinaryResponseContent,
)
from .....types import shared_params
from .....types.logs.controls.retentions import flag_logs_received_update_log_retention_flag_params
from ....._wrappers import ResultWrapper
from typing import cast
from typing import cast
from typing import cast
from typing import cast

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
