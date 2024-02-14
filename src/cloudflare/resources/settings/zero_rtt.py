# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from ..._compat import cached_property

from ...types.settings import ZeroRttGetResponse, ZeroRttZoneSettingsChange0RttSessionResumptionSettingResponse

from typing import Type, Optional

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
from ...types.settings import zero_rtt_zone_settings_change_0_rtt_session_resumption_setting_params
from ..._wrappers import ResultWrapper
from typing import cast
from typing import cast
from typing import cast
from typing import cast

__all__ = ["ZeroRtt", "AsyncZeroRtt"]


class ZeroRtt(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ZeroRttWithRawResponse:
        return ZeroRttWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ZeroRttWithStreamingResponse:
        return ZeroRttWithStreamingResponse(self)

    def get(
        self,
        zone_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ZeroRttGetResponse]:
        """
        Gets 0-RTT session resumption setting.

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
            f"/zones/{zone_id}/settings/0rtt",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[ZeroRttGetResponse]], ResultWrapper[ZeroRttGetResponse]),
        )

    def zone_settings_change_0_rtt_session_resumption_setting(
        self,
        zone_id: str,
        *,
        value: Literal["on", "off"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ZeroRttZoneSettingsChange0RttSessionResumptionSettingResponse]:
        """
        Changes the 0-RTT session resumption setting.

        Args:
          zone_id: Identifier

          value: Value of the 0-RTT setting.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._patch(
            f"/zones/{zone_id}/settings/0rtt",
            body=maybe_transform(
                {"value": value},
                zero_rtt_zone_settings_change_0_rtt_session_resumption_setting_params.ZeroRttZoneSettingsChange0RttSessionResumptionSettingParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[ZeroRttZoneSettingsChange0RttSessionResumptionSettingResponse]],
                ResultWrapper[ZeroRttZoneSettingsChange0RttSessionResumptionSettingResponse],
            ),
        )


class AsyncZeroRtt(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncZeroRttWithRawResponse:
        return AsyncZeroRttWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncZeroRttWithStreamingResponse:
        return AsyncZeroRttWithStreamingResponse(self)

    async def get(
        self,
        zone_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ZeroRttGetResponse]:
        """
        Gets 0-RTT session resumption setting.

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
            f"/zones/{zone_id}/settings/0rtt",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[ZeroRttGetResponse]], ResultWrapper[ZeroRttGetResponse]),
        )

    async def zone_settings_change_0_rtt_session_resumption_setting(
        self,
        zone_id: str,
        *,
        value: Literal["on", "off"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ZeroRttZoneSettingsChange0RttSessionResumptionSettingResponse]:
        """
        Changes the 0-RTT session resumption setting.

        Args:
          zone_id: Identifier

          value: Value of the 0-RTT setting.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._patch(
            f"/zones/{zone_id}/settings/0rtt",
            body=maybe_transform(
                {"value": value},
                zero_rtt_zone_settings_change_0_rtt_session_resumption_setting_params.ZeroRttZoneSettingsChange0RttSessionResumptionSettingParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[ZeroRttZoneSettingsChange0RttSessionResumptionSettingResponse]],
                ResultWrapper[ZeroRttZoneSettingsChange0RttSessionResumptionSettingResponse],
            ),
        )


class ZeroRttWithRawResponse:
    def __init__(self, zero_rtt: ZeroRtt) -> None:
        self._zero_rtt = zero_rtt

        self.get = to_raw_response_wrapper(
            zero_rtt.get,
        )
        self.zone_settings_change_0_rtt_session_resumption_setting = to_raw_response_wrapper(
            zero_rtt.zone_settings_change_0_rtt_session_resumption_setting,
        )


class AsyncZeroRttWithRawResponse:
    def __init__(self, zero_rtt: AsyncZeroRtt) -> None:
        self._zero_rtt = zero_rtt

        self.get = async_to_raw_response_wrapper(
            zero_rtt.get,
        )
        self.zone_settings_change_0_rtt_session_resumption_setting = async_to_raw_response_wrapper(
            zero_rtt.zone_settings_change_0_rtt_session_resumption_setting,
        )


class ZeroRttWithStreamingResponse:
    def __init__(self, zero_rtt: ZeroRtt) -> None:
        self._zero_rtt = zero_rtt

        self.get = to_streamed_response_wrapper(
            zero_rtt.get,
        )
        self.zone_settings_change_0_rtt_session_resumption_setting = to_streamed_response_wrapper(
            zero_rtt.zone_settings_change_0_rtt_session_resumption_setting,
        )


class AsyncZeroRttWithStreamingResponse:
    def __init__(self, zero_rtt: AsyncZeroRtt) -> None:
        self._zero_rtt = zero_rtt

        self.get = async_to_streamed_response_wrapper(
            zero_rtt.get,
        )
        self.zone_settings_change_0_rtt_session_resumption_setting = async_to_streamed_response_wrapper(
            zero_rtt.zone_settings_change_0_rtt_session_resumption_setting,
        )
