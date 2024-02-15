# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from ...._compat import cached_property

from ....types.emails.routings import EnableEmailRoutingSettingsEnableEmailRoutingResponse

from typing import Type

from ...._response import (
    to_raw_response_wrapper,
    async_to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_streamed_response_wrapper,
)

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ...._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ...._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._base_client import (
    SyncAPIClient,
    AsyncAPIClient,
    _merge_mappings,
    AsyncPaginator,
    make_request_options,
    HttpxBinaryResponseContent,
)
from ....types import shared_params
from ...._wrappers import ResultWrapper
from typing import cast
from typing import cast

__all__ = ["Enables", "AsyncEnables"]


class Enables(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> EnablesWithRawResponse:
        return EnablesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EnablesWithStreamingResponse:
        return EnablesWithStreamingResponse(self)

    def email_routing_settings_enable_email_routing(
        self,
        zone_identifier: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EnableEmailRoutingSettingsEnableEmailRoutingResponse:
        """Enable you Email Routing zone.

        Add and lock the necessary MX and SPF records.

        Args:
          zone_identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_identifier:
            raise ValueError(f"Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}")
        return self._post(
            f"/zones/{zone_identifier}/email/routing/enable",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[EnableEmailRoutingSettingsEnableEmailRoutingResponse],
                ResultWrapper[EnableEmailRoutingSettingsEnableEmailRoutingResponse],
            ),
        )


class AsyncEnables(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncEnablesWithRawResponse:
        return AsyncEnablesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEnablesWithStreamingResponse:
        return AsyncEnablesWithStreamingResponse(self)

    async def email_routing_settings_enable_email_routing(
        self,
        zone_identifier: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EnableEmailRoutingSettingsEnableEmailRoutingResponse:
        """Enable you Email Routing zone.

        Add and lock the necessary MX and SPF records.

        Args:
          zone_identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_identifier:
            raise ValueError(f"Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}")
        return await self._post(
            f"/zones/{zone_identifier}/email/routing/enable",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[EnableEmailRoutingSettingsEnableEmailRoutingResponse],
                ResultWrapper[EnableEmailRoutingSettingsEnableEmailRoutingResponse],
            ),
        )


class EnablesWithRawResponse:
    def __init__(self, enables: Enables) -> None:
        self._enables = enables

        self.email_routing_settings_enable_email_routing = to_raw_response_wrapper(
            enables.email_routing_settings_enable_email_routing,
        )


class AsyncEnablesWithRawResponse:
    def __init__(self, enables: AsyncEnables) -> None:
        self._enables = enables

        self.email_routing_settings_enable_email_routing = async_to_raw_response_wrapper(
            enables.email_routing_settings_enable_email_routing,
        )


class EnablesWithStreamingResponse:
    def __init__(self, enables: Enables) -> None:
        self._enables = enables

        self.email_routing_settings_enable_email_routing = to_streamed_response_wrapper(
            enables.email_routing_settings_enable_email_routing,
        )


class AsyncEnablesWithStreamingResponse:
    def __init__(self, enables: AsyncEnables) -> None:
        self._enables = enables

        self.email_routing_settings_enable_email_routing = async_to_streamed_response_wrapper(
            enables.email_routing_settings_enable_email_routing,
        )
