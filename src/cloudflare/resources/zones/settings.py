# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, List, Optional, cast
from typing_extensions import Literal, overload

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    required_args,
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
from ...types.zones import setting_edit_params
from ..._base_client import make_request_options
from ...types.zones.setting_get_response import SettingGetResponse
from ...types.zones.setting_edit_response import SettingEditResponse
from ...types.zones.automatic_platform_optimization_param import AutomaticPlatformOptimizationParam

__all__ = ["SettingsResource", "AsyncSettingsResource"]


class SettingsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SettingsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return SettingsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SettingsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return SettingsResourceWithStreamingResponse(self)

    @overload
    def edit(
        self,
        setting_id: str,
        *,
        zone_id: str,
        id: Literal["0rtt"],
        value: Literal["on", "off"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[SettingEditResponse]:
        """
        Updates a single zone setting by the identifier

        Args:
          zone_id: Identifier

          setting_id: Setting name

          id: ID of the zone setting.

          value: Current value of the zone setting.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def edit(
        self,
        setting_id: str,
        *,
        zone_id: str,
        id: Literal["advanced_ddos"],
        value: Literal["on", "off"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[SettingEditResponse]:
        """
        Updates a single zone setting by the identifier

        Args:
          zone_id: Identifier

          setting_id: Setting name

          id: ID of the zone setting.

          value: Current value of the zone setting.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def edit(
        self,
        setting_id: str,
        *,
        zone_id: str,
        id: Literal["aegis"],
        value: setting_edit_params.ZonesCacheRulesAegisValue | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[SettingEditResponse]:
        """
        Updates a single zone setting by the identifier

        Args:
          zone_id: Identifier

          setting_id: Setting name

          id: ID of the zone setting.

          value: Value of the zone setting.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def edit(
        self,
        setting_id: str,
        *,
        zone_id: str,
        id: Literal["always_online"],
        value: Literal["on", "off"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[SettingEditResponse]:
        """
        Updates a single zone setting by the identifier

        Args:
          zone_id: Identifier

          setting_id: Setting name

          id: ID of the zone setting.

          value: Current value of the zone setting.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def edit(
        self,
        setting_id: str,
        *,
        zone_id: str,
        id: Literal["always_use_https"],
        value: Literal["on", "off"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[SettingEditResponse]:
        """
        Updates a single zone setting by the identifier

        Args:
          zone_id: Identifier

          setting_id: Setting name

          id: ID of the zone setting.

          value: Current value of the zone setting.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def edit(
        self,
        setting_id: str,
        *,
        zone_id: str,
        id: Literal["automatic_https_rewrites"],
        value: Literal["on", "off"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[SettingEditResponse]:
        """
        Updates a single zone setting by the identifier

        Args:
          zone_id: Identifier

          setting_id: Setting name

          id: ID of the zone setting.

          value: Current value of the zone setting.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def edit(
        self,
        setting_id: str,
        *,
        zone_id: str,
        id: Literal["brotli"],
        value: Literal["off", "on"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[SettingEditResponse]:
        """
        Updates a single zone setting by the identifier

        Args:
          zone_id: Identifier

          setting_id: Setting name

          id: ID of the zone setting.

          value: Current value of the zone setting.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def edit(
        self,
        setting_id: str,
        *,
        zone_id: str,
        id: Literal["browser_cache_ttl"],
        value: Literal[
            0,
            30,
            60,
            120,
            300,
            1200,
            1800,
            3600,
            7200,
            10800,
            14400,
            18000,
            28800,
            43200,
            57600,
            72000,
            86400,
            172800,
            259200,
            345600,
            432000,
            691200,
            1382400,
            2073600,
            2678400,
            5356800,
            16070400,
            31536000,
        ],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[SettingEditResponse]:
        """
        Updates a single zone setting by the identifier

        Args:
          zone_id: Identifier

          setting_id: Setting name

          id: ID of the zone setting.

          value: Current value of the zone setting.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def edit(
        self,
        setting_id: str,
        *,
        zone_id: str,
        id: Literal["browser_check"],
        value: Literal["on", "off"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[SettingEditResponse]:
        """
        Updates a single zone setting by the identifier

        Args:
          zone_id: Identifier

          setting_id: Setting name

          id: ID of the zone setting.

          value: Current value of the zone setting.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def edit(
        self,
        setting_id: str,
        *,
        zone_id: str,
        id: Literal["cache_level"],
        value: Literal["aggressive", "basic", "simplified"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[SettingEditResponse]:
        """
        Updates a single zone setting by the identifier

        Args:
          zone_id: Identifier

          setting_id: Setting name

          id: ID of the zone setting.

          value: Current value of the zone setting.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def edit(
        self,
        setting_id: str,
        *,
        zone_id: str,
        id: Literal["challenge_ttl"],
        value: Literal[300, 900, 1800, 2700, 3600, 7200, 10800, 14400, 28800, 57600, 86400, 604800, 2592000, 31536000],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[SettingEditResponse]:
        """
        Updates a single zone setting by the identifier

        Args:
          zone_id: Identifier

          setting_id: Setting name

          id: ID of the zone setting.

          value: Current value of the zone setting.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def edit(
        self,
        setting_id: str,
        *,
        zone_id: str,
        id: Literal["ciphers"],
        value: List[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[SettingEditResponse]:
        """
        Updates a single zone setting by the identifier

        Args:
          zone_id: Identifier

          setting_id: Setting name

          id: ID of the zone setting.

          value: Current value of the zone setting.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def edit(
        self,
        setting_id: str,
        *,
        zone_id: str,
        id: Literal["cname_flattening"],
        value: Literal["flatten_at_root", "flatten_all"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[SettingEditResponse]:
        """
        Updates a single zone setting by the identifier

        Args:
          zone_id: Identifier

          setting_id: Setting name

          id: How to flatten the cname destination.

          value: Current value of the zone setting.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def edit(
        self,
        setting_id: str,
        *,
        zone_id: str,
        id: Literal["development_mode"],
        value: Literal["on", "off"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[SettingEditResponse]:
        """
        Updates a single zone setting by the identifier

        Args:
          zone_id: Identifier

          setting_id: Setting name

          id: ID of the zone setting.

          value: Current value of the zone setting.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def edit(
        self,
        setting_id: str,
        *,
        zone_id: str,
        id: Literal["early_hints"],
        value: Literal["on", "off"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[SettingEditResponse]:
        """
        Updates a single zone setting by the identifier

        Args:
          zone_id: Identifier

          setting_id: Setting name

          id: ID of the zone setting.

          value: Current value of the zone setting.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def edit(
        self,
        setting_id: str,
        *,
        zone_id: str,
        id: Literal["edge_cache_ttl"],
        value: Literal[
            30,
            60,
            300,
            1200,
            1800,
            3600,
            7200,
            10800,
            14400,
            18000,
            28800,
            43200,
            57600,
            72000,
            86400,
            172800,
            259200,
            345600,
            432000,
            518400,
            604800,
        ],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[SettingEditResponse]:
        """
        Updates a single zone setting by the identifier

        Args:
          zone_id: Identifier

          setting_id: Setting name

          id: ID of the zone setting.

          value: Current value of the zone setting.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def edit(
        self,
        setting_id: str,
        *,
        zone_id: str,
        id: Literal["email_obfuscation"],
        value: Literal["on", "off"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[SettingEditResponse]:
        """
        Updates a single zone setting by the identifier

        Args:
          zone_id: Identifier

          setting_id: Setting name

          id: ID of the zone setting.

          value: Current value of the zone setting.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def edit(
        self,
        setting_id: str,
        *,
        zone_id: str,
        id: Literal["h2_prioritization"],
        value: Literal["on", "off", "custom"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[SettingEditResponse]:
        """
        Updates a single zone setting by the identifier

        Args:
          zone_id: Identifier

          setting_id: Setting name

          id: ID of the zone setting.

          value: Current value of the zone setting.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def edit(
        self,
        setting_id: str,
        *,
        zone_id: str,
        id: Literal["hotlink_protection"],
        value: Literal["on", "off"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[SettingEditResponse]:
        """
        Updates a single zone setting by the identifier

        Args:
          zone_id: Identifier

          setting_id: Setting name

          id: ID of the zone setting.

          value: Current value of the zone setting.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def edit(
        self,
        setting_id: str,
        *,
        zone_id: str,
        id: Literal["http2"],
        value: Literal["on", "off"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[SettingEditResponse]:
        """
        Updates a single zone setting by the identifier

        Args:
          zone_id: Identifier

          setting_id: Setting name

          id: ID of the zone setting.

          value: Current value of the zone setting.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def edit(
        self,
        setting_id: str,
        *,
        zone_id: str,
        id: Literal["http3"],
        value: Literal["on", "off"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[SettingEditResponse]:
        """
        Updates a single zone setting by the identifier

        Args:
          zone_id: Identifier

          setting_id: Setting name

          id: ID of the zone setting.

          value: Current value of the zone setting.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def edit(
        self,
        setting_id: str,
        *,
        zone_id: str,
        id: Literal["image_resizing"],
        value: Literal["on", "off", "open"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[SettingEditResponse]:
        """
        Updates a single zone setting by the identifier

        Args:
          zone_id: Identifier

          setting_id: Setting name

          id: ID of the zone setting.

          value: Current value of the zone setting.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def edit(
        self,
        setting_id: str,
        *,
        zone_id: str,
        id: Literal["ip_geolocation"],
        value: Literal["on", "off"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[SettingEditResponse]:
        """
        Updates a single zone setting by the identifier

        Args:
          zone_id: Identifier

          setting_id: Setting name

          id: ID of the zone setting.

          value: Current value of the zone setting.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def edit(
        self,
        setting_id: str,
        *,
        zone_id: str,
        id: Literal["ipv6"],
        value: Literal["off", "on"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[SettingEditResponse]:
        """
        Updates a single zone setting by the identifier

        Args:
          zone_id: Identifier

          setting_id: Setting name

          id: ID of the zone setting.

          value: Current value of the zone setting.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def edit(
        self,
        setting_id: str,
        *,
        zone_id: str,
        id: Literal["max_upload"],
        value: Literal[100, 200, 500],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[SettingEditResponse]:
        """
        Updates a single zone setting by the identifier

        Args:
          zone_id: Identifier

          setting_id: Setting name

          id: identifier of the zone setting.

          value: Current value of the zone setting.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def edit(
        self,
        setting_id: str,
        *,
        zone_id: str,
        id: Literal["min_tls_version"],
        value: Literal["1.0", "1.1", "1.2", "1.3"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[SettingEditResponse]:
        """
        Updates a single zone setting by the identifier

        Args:
          zone_id: Identifier

          setting_id: Setting name

          id: ID of the zone setting.

          value: Current value of the zone setting.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def edit(
        self,
        setting_id: str,
        *,
        zone_id: str,
        id: Literal["mirage"],
        value: Literal["on", "off"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[SettingEditResponse]:
        """
        Updates a single zone setting by the identifier

        Args:
          zone_id: Identifier

          setting_id: Setting name

          id: ID of the zone setting.

          value: Current value of the zone setting.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def edit(
        self,
        setting_id: str,
        *,
        zone_id: str,
        id: Literal["nel"],
        value: setting_edit_params.NELValue,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[SettingEditResponse]:
        """
        Updates a single zone setting by the identifier

        Args:
          zone_id: Identifier

          setting_id: Setting name

          id: Zone setting identifier.

          value: Current value of the zone setting.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def edit(
        self,
        setting_id: str,
        *,
        zone_id: str,
        id: Literal["opportunistic_encryption"],
        value: Literal["on", "off"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[SettingEditResponse]:
        """
        Updates a single zone setting by the identifier

        Args:
          zone_id: Identifier

          setting_id: Setting name

          id: ID of the zone setting.

          value: Current value of the zone setting.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def edit(
        self,
        setting_id: str,
        *,
        zone_id: str,
        id: Literal["opportunistic_onion"],
        value: Literal["on", "off"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[SettingEditResponse]:
        """
        Updates a single zone setting by the identifier

        Args:
          zone_id: Identifier

          setting_id: Setting name

          id: ID of the zone setting.

          value: Current value of the zone setting.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def edit(
        self,
        setting_id: str,
        *,
        zone_id: str,
        id: Literal["orange_to_orange"],
        value: Literal["on", "off"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[SettingEditResponse]:
        """
        Updates a single zone setting by the identifier

        Args:
          zone_id: Identifier

          setting_id: Setting name

          id: ID of the zone setting.

          value: Current value of the zone setting.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def edit(
        self,
        setting_id: str,
        *,
        zone_id: str,
        id: Literal["origin_error_page_pass_thru"],
        value: Literal["on", "off"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[SettingEditResponse]:
        """
        Updates a single zone setting by the identifier

        Args:
          zone_id: Identifier

          setting_id: Setting name

          id: ID of the zone setting.

          value: Current value of the zone setting.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def edit(
        self,
        setting_id: str,
        *,
        zone_id: str,
        id: Literal["origin_h2_max_streams"],
        value: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[SettingEditResponse]:
        """
        Updates a single zone setting by the identifier

        Args:
          zone_id: Identifier

          setting_id: Setting name

          id: Value of the zone setting.

          value: Value of the Origin H2 Max Streams Setting.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def edit(
        self,
        setting_id: str,
        *,
        zone_id: str,
        id: Literal["origin_max_http_version"],
        value: Literal["2", "1"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[SettingEditResponse]:
        """
        Updates a single zone setting by the identifier

        Args:
          zone_id: Identifier

          setting_id: Setting name

          id: Value of the zone setting.

          value: Value of the Origin Max HTTP Version Setting.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def edit(
        self,
        setting_id: str,
        *,
        zone_id: str,
        id: Literal["polish"],
        value: Literal["off", "lossless", "lossy"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[SettingEditResponse]:
        """
        Updates a single zone setting by the identifier

        Args:
          zone_id: Identifier

          setting_id: Setting name

          id: ID of the zone setting.

          value: Current value of the zone setting.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def edit(
        self,
        setting_id: str,
        *,
        zone_id: str,
        id: Literal["prefetch_preload"],
        value: Literal["on", "off"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[SettingEditResponse]:
        """
        Updates a single zone setting by the identifier

        Args:
          zone_id: Identifier

          setting_id: Setting name

          id: ID of the zone setting.

          value: Current value of the zone setting.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def edit(
        self,
        setting_id: str,
        *,
        zone_id: str,
        id: Literal["privacy_pass"],
        value: Literal["on", "off"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[SettingEditResponse]:
        """
        Updates a single zone setting by the identifier

        Args:
          zone_id: Identifier

          setting_id: Setting name

          id: ID of the zone setting.

          value: Current value of the zone setting.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def edit(
        self,
        setting_id: str,
        *,
        zone_id: str,
        id: Literal["proxy_read_timeout"],
        value: float,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[SettingEditResponse]:
        """
        Updates a single zone setting by the identifier

        Args:
          zone_id: Identifier

          setting_id: Setting name

          id: ID of the zone setting.

          value: Current value of the zone setting.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def edit(
        self,
        setting_id: str,
        *,
        zone_id: str,
        id: Literal["pseudo_ipv4"],
        value: Literal["off", "add_header", "overwrite_header"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[SettingEditResponse]:
        """
        Updates a single zone setting by the identifier

        Args:
          zone_id: Identifier

          setting_id: Setting name

          id: Value of the Pseudo IPv4 setting.

          value: Current value of the zone setting.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def edit(
        self,
        setting_id: str,
        *,
        zone_id: str,
        id: Literal["replace_insecure_js"],
        value: Literal["on", "off"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[SettingEditResponse]:
        """
        Updates a single zone setting by the identifier

        Args:
          zone_id: Identifier

          setting_id: Setting name

          id: ID of the zone setting.

          value: Current value of the zone setting.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def edit(
        self,
        setting_id: str,
        *,
        zone_id: str,
        id: Literal["response_buffering"],
        value: Literal["on", "off"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[SettingEditResponse]:
        """
        Updates a single zone setting by the identifier

        Args:
          zone_id: Identifier

          setting_id: Setting name

          id: ID of the zone setting.

          value: Current value of the zone setting.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def edit(
        self,
        setting_id: str,
        *,
        zone_id: str,
        id: Literal["rocket_loader"],
        value: Literal["on", "off"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[SettingEditResponse]:
        """
        Updates a single zone setting by the identifier

        Args:
          zone_id: Identifier

          setting_id: Setting name

          id: ID of the zone setting.

          value: Current value of the zone setting.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def edit(
        self,
        setting_id: str,
        *,
        zone_id: str,
        id: Literal["automatic_platform_optimization"],
        value: AutomaticPlatformOptimizationParam,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[SettingEditResponse]:
        """
        Updates a single zone setting by the identifier

        Args:
          zone_id: Identifier

          setting_id: Setting name

          id: ID of the zone setting.

          value: Current value of the zone setting.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def edit(
        self,
        setting_id: str,
        *,
        zone_id: str,
        id: Literal["security_header"],
        value: setting_edit_params.SecurityHeadersValue,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[SettingEditResponse]:
        """
        Updates a single zone setting by the identifier

        Args:
          zone_id: Identifier

          setting_id: Setting name

          id: ID of the zone's security header.

          value: Current value of the zone setting.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def edit(
        self,
        setting_id: str,
        *,
        zone_id: str,
        id: Literal["security_level"],
        value: Literal["off", "essentially_off", "low", "medium", "high", "under_attack"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[SettingEditResponse]:
        """
        Updates a single zone setting by the identifier

        Args:
          zone_id: Identifier

          setting_id: Setting name

          id: ID of the zone setting.

          value: Current value of the zone setting.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def edit(
        self,
        setting_id: str,
        *,
        zone_id: str,
        id: Literal["server_side_exclude"],
        value: Literal["on", "off"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[SettingEditResponse]:
        """
        Updates a single zone setting by the identifier

        Args:
          zone_id: Identifier

          setting_id: Setting name

          id: ID of the zone setting.

          value: Current value of the zone setting.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def edit(
        self,
        setting_id: str,
        *,
        zone_id: str,
        id: Literal["sha1_support"],
        value: Literal["off", "on"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[SettingEditResponse]:
        """
        Updates a single zone setting by the identifier

        Args:
          zone_id: Identifier

          setting_id: Setting name

          id: Zone setting identifier.

          value: Current value of the zone setting.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def edit(
        self,
        setting_id: str,
        *,
        zone_id: str,
        id: Literal["sort_query_string_for_cache"],
        value: Literal["on", "off"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[SettingEditResponse]:
        """
        Updates a single zone setting by the identifier

        Args:
          zone_id: Identifier

          setting_id: Setting name

          id: ID of the zone setting.

          value: Current value of the zone setting.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def edit(
        self,
        setting_id: str,
        *,
        zone_id: str,
        id: Literal["ssl"],
        value: Literal["off", "flexible", "full", "strict"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[SettingEditResponse]:
        """
        Updates a single zone setting by the identifier

        Args:
          zone_id: Identifier

          setting_id: Setting name

          id: ID of the zone setting.

          value: Current value of the zone setting.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def edit(
        self,
        setting_id: str,
        *,
        zone_id: str,
        id: Literal["ssl_recommender"] | NotGiven = NOT_GIVEN,
        enabled: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[SettingEditResponse]:
        """
        Updates a single zone setting by the identifier

        Args:
          zone_id: Identifier

          setting_id: Setting name

          id: Enrollment value for SSL/TLS Recommender.

          enabled: ssl-recommender enrollment setting.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def edit(
        self,
        setting_id: str,
        *,
        zone_id: str,
        id: Literal["tls_1_2_only"],
        value: Literal["off", "on"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[SettingEditResponse]:
        """
        Updates a single zone setting by the identifier

        Args:
          zone_id: Identifier

          setting_id: Setting name

          id: Zone setting identifier.

          value: Current value of the zone setting.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def edit(
        self,
        setting_id: str,
        *,
        zone_id: str,
        id: Literal["tls_1_3"],
        value: Literal["on", "off", "zrt"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[SettingEditResponse]:
        """
        Updates a single zone setting by the identifier

        Args:
          zone_id: Identifier

          setting_id: Setting name

          id: ID of the zone setting.

          value: Current value of the zone setting.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def edit(
        self,
        setting_id: str,
        *,
        zone_id: str,
        id: Literal["tls_client_auth"],
        value: Literal["on", "off"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[SettingEditResponse]:
        """
        Updates a single zone setting by the identifier

        Args:
          zone_id: Identifier

          setting_id: Setting name

          id: ID of the zone setting.

          value: Current value of the zone setting.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def edit(
        self,
        setting_id: str,
        *,
        zone_id: str,
        id: Literal["true_client_ip_header"],
        value: Literal["on", "off"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[SettingEditResponse]:
        """
        Updates a single zone setting by the identifier

        Args:
          zone_id: Identifier

          setting_id: Setting name

          id: ID of the zone setting.

          value: Current value of the zone setting.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def edit(
        self,
        setting_id: str,
        *,
        zone_id: str,
        id: Literal["waf"],
        value: Literal["on", "off"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[SettingEditResponse]:
        """
        Updates a single zone setting by the identifier

        Args:
          zone_id: Identifier

          setting_id: Setting name

          id: ID of the zone setting.

          value: Current value of the zone setting.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def edit(
        self,
        setting_id: str,
        *,
        zone_id: str,
        id: Literal["webp"],
        value: Literal["off", "on"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[SettingEditResponse]:
        """
        Updates a single zone setting by the identifier

        Args:
          zone_id: Identifier

          setting_id: Setting name

          id: ID of the zone setting.

          value: Current value of the zone setting.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def edit(
        self,
        setting_id: str,
        *,
        zone_id: str,
        id: Literal["websockets"],
        value: Literal["off", "on"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[SettingEditResponse]:
        """
        Updates a single zone setting by the identifier

        Args:
          zone_id: Identifier

          setting_id: Setting name

          id: ID of the zone setting.

          value: Current value of the zone setting.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["zone_id", "id", "value"], ["zone_id", "id"], ["zone_id"])
    def edit(
        self,
        setting_id: str,
        *,
        zone_id: str,
        id: Literal["0rtt"]
        | Literal["advanced_ddos"]
        | Literal["aegis"]
        | Literal["always_online"]
        | Literal["always_use_https"]
        | Literal["automatic_https_rewrites"]
        | Literal["brotli"]
        | Literal["browser_cache_ttl"]
        | Literal["browser_check"]
        | Literal["cache_level"]
        | Literal["challenge_ttl"]
        | Literal["ciphers"]
        | Literal["cname_flattening"]
        | Literal["development_mode"]
        | Literal["early_hints"]
        | Literal["edge_cache_ttl"]
        | Literal["email_obfuscation"]
        | Literal["h2_prioritization"]
        | Literal["hotlink_protection"]
        | Literal["http2"]
        | Literal["http3"]
        | Literal["image_resizing"]
        | Literal["ip_geolocation"]
        | Literal["ipv6"]
        | Literal["max_upload"]
        | Literal["min_tls_version"]
        | Literal["mirage"]
        | Literal["nel"]
        | Literal["opportunistic_encryption"]
        | Literal["opportunistic_onion"]
        | Literal["orange_to_orange"]
        | Literal["origin_error_page_pass_thru"]
        | Literal["origin_h2_max_streams"]
        | Literal["origin_max_http_version"]
        | Literal["polish"]
        | Literal["prefetch_preload"]
        | Literal["privacy_pass"]
        | Literal["proxy_read_timeout"]
        | Literal["pseudo_ipv4"]
        | Literal["replace_insecure_js"]
        | Literal["response_buffering"]
        | Literal["rocket_loader"]
        | Literal["automatic_platform_optimization"]
        | Literal["security_header"]
        | Literal["security_level"]
        | Literal["server_side_exclude"]
        | Literal["sha1_support"]
        | Literal["sort_query_string_for_cache"]
        | Literal["ssl"]
        | Literal["ssl_recommender"]
        | Literal["tls_1_2_only"]
        | Literal["tls_1_3"]
        | Literal["tls_client_auth"]
        | Literal["true_client_ip_header"]
        | Literal["waf"]
        | Literal["webp"]
        | Literal["websockets"]
        | NotGiven = NOT_GIVEN,
        value: Literal["on", "off"]
        | setting_edit_params.ZonesCacheRulesAegisValue
        | Literal[
            0,
            30,
            60,
            120,
            300,
            1200,
            1800,
            3600,
            7200,
            10800,
            14400,
            18000,
            28800,
            43200,
            57600,
            72000,
            86400,
            172800,
            259200,
            345600,
            432000,
            691200,
            1382400,
            2073600,
            2678400,
            5356800,
            16070400,
            31536000,
        ]
        | Literal["aggressive", "basic", "simplified"]
        | Literal[300, 900, 1800, 2700, 3600, 7200, 10800, 14400, 28800, 57600, 86400, 604800, 2592000, 31536000]
        | List[str]
        | Literal["flatten_at_root", "flatten_all"]
        | Literal[
            30,
            60,
            300,
            1200,
            1800,
            3600,
            7200,
            10800,
            14400,
            18000,
            28800,
            43200,
            57600,
            72000,
            86400,
            172800,
            259200,
            345600,
            432000,
            518400,
            604800,
        ]
        | Literal["on", "off", "custom"]
        | Literal["on", "off", "open"]
        | Literal[100, 200, 500]
        | Literal["1.0", "1.1", "1.2", "1.3"]
        | setting_edit_params.NELValue
        | int
        | Literal["2", "1"]
        | Literal["off", "lossless", "lossy"]
        | float
        | Literal["off", "add_header", "overwrite_header"]
        | AutomaticPlatformOptimizationParam
        | setting_edit_params.SecurityHeadersValue
        | Literal["off", "essentially_off", "low", "medium", "high", "under_attack"]
        | Literal["off", "flexible", "full", "strict"]
        | Literal["on", "off", "zrt"]
        | NotGiven = NOT_GIVEN,
        enabled: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[SettingEditResponse]:
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not setting_id:
            raise ValueError(f"Expected a non-empty value for `setting_id` but received {setting_id!r}")
        return cast(
            Optional[SettingEditResponse],
            self._patch(
                f"/zones/{zone_id}/settings/{setting_id}",
                body=maybe_transform(
                    {
                        "id": id,
                        "value": value,
                        "enabled": enabled,
                    },
                    setting_edit_params.SettingEditParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper[Optional[SettingEditResponse]]._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[SettingEditResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def get(
        self,
        setting_id: str,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[SettingGetResponse]:
        """
        Fetch a single zone setting by name

        Args:
          zone_id: Identifier

          setting_id: Setting name

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not setting_id:
            raise ValueError(f"Expected a non-empty value for `setting_id` but received {setting_id!r}")
        return cast(
            Optional[SettingGetResponse],
            self._get(
                f"/zones/{zone_id}/settings/{setting_id}",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper[Optional[SettingGetResponse]]._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[SettingGetResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class AsyncSettingsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSettingsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSettingsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSettingsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncSettingsResourceWithStreamingResponse(self)

    @overload
    async def edit(
        self,
        setting_id: str,
        *,
        zone_id: str,
        id: Literal["0rtt"],
        value: Literal["on", "off"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[SettingEditResponse]:
        """
        Updates a single zone setting by the identifier

        Args:
          zone_id: Identifier

          setting_id: Setting name

          id: ID of the zone setting.

          value: Current value of the zone setting.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def edit(
        self,
        setting_id: str,
        *,
        zone_id: str,
        id: Literal["advanced_ddos"],
        value: Literal["on", "off"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[SettingEditResponse]:
        """
        Updates a single zone setting by the identifier

        Args:
          zone_id: Identifier

          setting_id: Setting name

          id: ID of the zone setting.

          value: Current value of the zone setting.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def edit(
        self,
        setting_id: str,
        *,
        zone_id: str,
        id: Literal["aegis"],
        value: setting_edit_params.ZonesCacheRulesAegisValue | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[SettingEditResponse]:
        """
        Updates a single zone setting by the identifier

        Args:
          zone_id: Identifier

          setting_id: Setting name

          id: ID of the zone setting.

          value: Value of the zone setting.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def edit(
        self,
        setting_id: str,
        *,
        zone_id: str,
        id: Literal["always_online"],
        value: Literal["on", "off"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[SettingEditResponse]:
        """
        Updates a single zone setting by the identifier

        Args:
          zone_id: Identifier

          setting_id: Setting name

          id: ID of the zone setting.

          value: Current value of the zone setting.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def edit(
        self,
        setting_id: str,
        *,
        zone_id: str,
        id: Literal["always_use_https"],
        value: Literal["on", "off"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[SettingEditResponse]:
        """
        Updates a single zone setting by the identifier

        Args:
          zone_id: Identifier

          setting_id: Setting name

          id: ID of the zone setting.

          value: Current value of the zone setting.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def edit(
        self,
        setting_id: str,
        *,
        zone_id: str,
        id: Literal["automatic_https_rewrites"],
        value: Literal["on", "off"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[SettingEditResponse]:
        """
        Updates a single zone setting by the identifier

        Args:
          zone_id: Identifier

          setting_id: Setting name

          id: ID of the zone setting.

          value: Current value of the zone setting.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def edit(
        self,
        setting_id: str,
        *,
        zone_id: str,
        id: Literal["brotli"],
        value: Literal["off", "on"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[SettingEditResponse]:
        """
        Updates a single zone setting by the identifier

        Args:
          zone_id: Identifier

          setting_id: Setting name

          id: ID of the zone setting.

          value: Current value of the zone setting.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def edit(
        self,
        setting_id: str,
        *,
        zone_id: str,
        id: Literal["browser_cache_ttl"],
        value: Literal[
            0,
            30,
            60,
            120,
            300,
            1200,
            1800,
            3600,
            7200,
            10800,
            14400,
            18000,
            28800,
            43200,
            57600,
            72000,
            86400,
            172800,
            259200,
            345600,
            432000,
            691200,
            1382400,
            2073600,
            2678400,
            5356800,
            16070400,
            31536000,
        ],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[SettingEditResponse]:
        """
        Updates a single zone setting by the identifier

        Args:
          zone_id: Identifier

          setting_id: Setting name

          id: ID of the zone setting.

          value: Current value of the zone setting.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def edit(
        self,
        setting_id: str,
        *,
        zone_id: str,
        id: Literal["browser_check"],
        value: Literal["on", "off"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[SettingEditResponse]:
        """
        Updates a single zone setting by the identifier

        Args:
          zone_id: Identifier

          setting_id: Setting name

          id: ID of the zone setting.

          value: Current value of the zone setting.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def edit(
        self,
        setting_id: str,
        *,
        zone_id: str,
        id: Literal["cache_level"],
        value: Literal["aggressive", "basic", "simplified"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[SettingEditResponse]:
        """
        Updates a single zone setting by the identifier

        Args:
          zone_id: Identifier

          setting_id: Setting name

          id: ID of the zone setting.

          value: Current value of the zone setting.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def edit(
        self,
        setting_id: str,
        *,
        zone_id: str,
        id: Literal["challenge_ttl"],
        value: Literal[300, 900, 1800, 2700, 3600, 7200, 10800, 14400, 28800, 57600, 86400, 604800, 2592000, 31536000],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[SettingEditResponse]:
        """
        Updates a single zone setting by the identifier

        Args:
          zone_id: Identifier

          setting_id: Setting name

          id: ID of the zone setting.

          value: Current value of the zone setting.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def edit(
        self,
        setting_id: str,
        *,
        zone_id: str,
        id: Literal["ciphers"],
        value: List[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[SettingEditResponse]:
        """
        Updates a single zone setting by the identifier

        Args:
          zone_id: Identifier

          setting_id: Setting name

          id: ID of the zone setting.

          value: Current value of the zone setting.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def edit(
        self,
        setting_id: str,
        *,
        zone_id: str,
        id: Literal["cname_flattening"],
        value: Literal["flatten_at_root", "flatten_all"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[SettingEditResponse]:
        """
        Updates a single zone setting by the identifier

        Args:
          zone_id: Identifier

          setting_id: Setting name

          id: How to flatten the cname destination.

          value: Current value of the zone setting.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def edit(
        self,
        setting_id: str,
        *,
        zone_id: str,
        id: Literal["development_mode"],
        value: Literal["on", "off"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[SettingEditResponse]:
        """
        Updates a single zone setting by the identifier

        Args:
          zone_id: Identifier

          setting_id: Setting name

          id: ID of the zone setting.

          value: Current value of the zone setting.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def edit(
        self,
        setting_id: str,
        *,
        zone_id: str,
        id: Literal["early_hints"],
        value: Literal["on", "off"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[SettingEditResponse]:
        """
        Updates a single zone setting by the identifier

        Args:
          zone_id: Identifier

          setting_id: Setting name

          id: ID of the zone setting.

          value: Current value of the zone setting.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def edit(
        self,
        setting_id: str,
        *,
        zone_id: str,
        id: Literal["edge_cache_ttl"],
        value: Literal[
            30,
            60,
            300,
            1200,
            1800,
            3600,
            7200,
            10800,
            14400,
            18000,
            28800,
            43200,
            57600,
            72000,
            86400,
            172800,
            259200,
            345600,
            432000,
            518400,
            604800,
        ],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[SettingEditResponse]:
        """
        Updates a single zone setting by the identifier

        Args:
          zone_id: Identifier

          setting_id: Setting name

          id: ID of the zone setting.

          value: Current value of the zone setting.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def edit(
        self,
        setting_id: str,
        *,
        zone_id: str,
        id: Literal["email_obfuscation"],
        value: Literal["on", "off"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[SettingEditResponse]:
        """
        Updates a single zone setting by the identifier

        Args:
          zone_id: Identifier

          setting_id: Setting name

          id: ID of the zone setting.

          value: Current value of the zone setting.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def edit(
        self,
        setting_id: str,
        *,
        zone_id: str,
        id: Literal["h2_prioritization"],
        value: Literal["on", "off", "custom"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[SettingEditResponse]:
        """
        Updates a single zone setting by the identifier

        Args:
          zone_id: Identifier

          setting_id: Setting name

          id: ID of the zone setting.

          value: Current value of the zone setting.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def edit(
        self,
        setting_id: str,
        *,
        zone_id: str,
        id: Literal["hotlink_protection"],
        value: Literal["on", "off"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[SettingEditResponse]:
        """
        Updates a single zone setting by the identifier

        Args:
          zone_id: Identifier

          setting_id: Setting name

          id: ID of the zone setting.

          value: Current value of the zone setting.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def edit(
        self,
        setting_id: str,
        *,
        zone_id: str,
        id: Literal["http2"],
        value: Literal["on", "off"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[SettingEditResponse]:
        """
        Updates a single zone setting by the identifier

        Args:
          zone_id: Identifier

          setting_id: Setting name

          id: ID of the zone setting.

          value: Current value of the zone setting.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def edit(
        self,
        setting_id: str,
        *,
        zone_id: str,
        id: Literal["http3"],
        value: Literal["on", "off"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[SettingEditResponse]:
        """
        Updates a single zone setting by the identifier

        Args:
          zone_id: Identifier

          setting_id: Setting name

          id: ID of the zone setting.

          value: Current value of the zone setting.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def edit(
        self,
        setting_id: str,
        *,
        zone_id: str,
        id: Literal["image_resizing"],
        value: Literal["on", "off", "open"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[SettingEditResponse]:
        """
        Updates a single zone setting by the identifier

        Args:
          zone_id: Identifier

          setting_id: Setting name

          id: ID of the zone setting.

          value: Current value of the zone setting.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def edit(
        self,
        setting_id: str,
        *,
        zone_id: str,
        id: Literal["ip_geolocation"],
        value: Literal["on", "off"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[SettingEditResponse]:
        """
        Updates a single zone setting by the identifier

        Args:
          zone_id: Identifier

          setting_id: Setting name

          id: ID of the zone setting.

          value: Current value of the zone setting.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def edit(
        self,
        setting_id: str,
        *,
        zone_id: str,
        id: Literal["ipv6"],
        value: Literal["off", "on"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[SettingEditResponse]:
        """
        Updates a single zone setting by the identifier

        Args:
          zone_id: Identifier

          setting_id: Setting name

          id: ID of the zone setting.

          value: Current value of the zone setting.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def edit(
        self,
        setting_id: str,
        *,
        zone_id: str,
        id: Literal["max_upload"],
        value: Literal[100, 200, 500],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[SettingEditResponse]:
        """
        Updates a single zone setting by the identifier

        Args:
          zone_id: Identifier

          setting_id: Setting name

          id: identifier of the zone setting.

          value: Current value of the zone setting.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def edit(
        self,
        setting_id: str,
        *,
        zone_id: str,
        id: Literal["min_tls_version"],
        value: Literal["1.0", "1.1", "1.2", "1.3"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[SettingEditResponse]:
        """
        Updates a single zone setting by the identifier

        Args:
          zone_id: Identifier

          setting_id: Setting name

          id: ID of the zone setting.

          value: Current value of the zone setting.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def edit(
        self,
        setting_id: str,
        *,
        zone_id: str,
        id: Literal["mirage"],
        value: Literal["on", "off"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[SettingEditResponse]:
        """
        Updates a single zone setting by the identifier

        Args:
          zone_id: Identifier

          setting_id: Setting name

          id: ID of the zone setting.

          value: Current value of the zone setting.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def edit(
        self,
        setting_id: str,
        *,
        zone_id: str,
        id: Literal["nel"],
        value: setting_edit_params.NELValue,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[SettingEditResponse]:
        """
        Updates a single zone setting by the identifier

        Args:
          zone_id: Identifier

          setting_id: Setting name

          id: Zone setting identifier.

          value: Current value of the zone setting.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def edit(
        self,
        setting_id: str,
        *,
        zone_id: str,
        id: Literal["opportunistic_encryption"],
        value: Literal["on", "off"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[SettingEditResponse]:
        """
        Updates a single zone setting by the identifier

        Args:
          zone_id: Identifier

          setting_id: Setting name

          id: ID of the zone setting.

          value: Current value of the zone setting.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def edit(
        self,
        setting_id: str,
        *,
        zone_id: str,
        id: Literal["opportunistic_onion"],
        value: Literal["on", "off"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[SettingEditResponse]:
        """
        Updates a single zone setting by the identifier

        Args:
          zone_id: Identifier

          setting_id: Setting name

          id: ID of the zone setting.

          value: Current value of the zone setting.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def edit(
        self,
        setting_id: str,
        *,
        zone_id: str,
        id: Literal["orange_to_orange"],
        value: Literal["on", "off"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[SettingEditResponse]:
        """
        Updates a single zone setting by the identifier

        Args:
          zone_id: Identifier

          setting_id: Setting name

          id: ID of the zone setting.

          value: Current value of the zone setting.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def edit(
        self,
        setting_id: str,
        *,
        zone_id: str,
        id: Literal["origin_error_page_pass_thru"],
        value: Literal["on", "off"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[SettingEditResponse]:
        """
        Updates a single zone setting by the identifier

        Args:
          zone_id: Identifier

          setting_id: Setting name

          id: ID of the zone setting.

          value: Current value of the zone setting.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def edit(
        self,
        setting_id: str,
        *,
        zone_id: str,
        id: Literal["origin_h2_max_streams"],
        value: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[SettingEditResponse]:
        """
        Updates a single zone setting by the identifier

        Args:
          zone_id: Identifier

          setting_id: Setting name

          id: Value of the zone setting.

          value: Value of the Origin H2 Max Streams Setting.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def edit(
        self,
        setting_id: str,
        *,
        zone_id: str,
        id: Literal["origin_max_http_version"],
        value: Literal["2", "1"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[SettingEditResponse]:
        """
        Updates a single zone setting by the identifier

        Args:
          zone_id: Identifier

          setting_id: Setting name

          id: Value of the zone setting.

          value: Value of the Origin Max HTTP Version Setting.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def edit(
        self,
        setting_id: str,
        *,
        zone_id: str,
        id: Literal["polish"],
        value: Literal["off", "lossless", "lossy"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[SettingEditResponse]:
        """
        Updates a single zone setting by the identifier

        Args:
          zone_id: Identifier

          setting_id: Setting name

          id: ID of the zone setting.

          value: Current value of the zone setting.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def edit(
        self,
        setting_id: str,
        *,
        zone_id: str,
        id: Literal["prefetch_preload"],
        value: Literal["on", "off"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[SettingEditResponse]:
        """
        Updates a single zone setting by the identifier

        Args:
          zone_id: Identifier

          setting_id: Setting name

          id: ID of the zone setting.

          value: Current value of the zone setting.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def edit(
        self,
        setting_id: str,
        *,
        zone_id: str,
        id: Literal["privacy_pass"],
        value: Literal["on", "off"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[SettingEditResponse]:
        """
        Updates a single zone setting by the identifier

        Args:
          zone_id: Identifier

          setting_id: Setting name

          id: ID of the zone setting.

          value: Current value of the zone setting.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def edit(
        self,
        setting_id: str,
        *,
        zone_id: str,
        id: Literal["proxy_read_timeout"],
        value: float,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[SettingEditResponse]:
        """
        Updates a single zone setting by the identifier

        Args:
          zone_id: Identifier

          setting_id: Setting name

          id: ID of the zone setting.

          value: Current value of the zone setting.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def edit(
        self,
        setting_id: str,
        *,
        zone_id: str,
        id: Literal["pseudo_ipv4"],
        value: Literal["off", "add_header", "overwrite_header"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[SettingEditResponse]:
        """
        Updates a single zone setting by the identifier

        Args:
          zone_id: Identifier

          setting_id: Setting name

          id: Value of the Pseudo IPv4 setting.

          value: Current value of the zone setting.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def edit(
        self,
        setting_id: str,
        *,
        zone_id: str,
        id: Literal["replace_insecure_js"],
        value: Literal["on", "off"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[SettingEditResponse]:
        """
        Updates a single zone setting by the identifier

        Args:
          zone_id: Identifier

          setting_id: Setting name

          id: ID of the zone setting.

          value: Current value of the zone setting.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def edit(
        self,
        setting_id: str,
        *,
        zone_id: str,
        id: Literal["response_buffering"],
        value: Literal["on", "off"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[SettingEditResponse]:
        """
        Updates a single zone setting by the identifier

        Args:
          zone_id: Identifier

          setting_id: Setting name

          id: ID of the zone setting.

          value: Current value of the zone setting.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def edit(
        self,
        setting_id: str,
        *,
        zone_id: str,
        id: Literal["rocket_loader"],
        value: Literal["on", "off"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[SettingEditResponse]:
        """
        Updates a single zone setting by the identifier

        Args:
          zone_id: Identifier

          setting_id: Setting name

          id: ID of the zone setting.

          value: Current value of the zone setting.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def edit(
        self,
        setting_id: str,
        *,
        zone_id: str,
        id: Literal["automatic_platform_optimization"],
        value: AutomaticPlatformOptimizationParam,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[SettingEditResponse]:
        """
        Updates a single zone setting by the identifier

        Args:
          zone_id: Identifier

          setting_id: Setting name

          id: ID of the zone setting.

          value: Current value of the zone setting.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def edit(
        self,
        setting_id: str,
        *,
        zone_id: str,
        id: Literal["security_header"],
        value: setting_edit_params.SecurityHeadersValue,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[SettingEditResponse]:
        """
        Updates a single zone setting by the identifier

        Args:
          zone_id: Identifier

          setting_id: Setting name

          id: ID of the zone's security header.

          value: Current value of the zone setting.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def edit(
        self,
        setting_id: str,
        *,
        zone_id: str,
        id: Literal["security_level"],
        value: Literal["off", "essentially_off", "low", "medium", "high", "under_attack"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[SettingEditResponse]:
        """
        Updates a single zone setting by the identifier

        Args:
          zone_id: Identifier

          setting_id: Setting name

          id: ID of the zone setting.

          value: Current value of the zone setting.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def edit(
        self,
        setting_id: str,
        *,
        zone_id: str,
        id: Literal["server_side_exclude"],
        value: Literal["on", "off"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[SettingEditResponse]:
        """
        Updates a single zone setting by the identifier

        Args:
          zone_id: Identifier

          setting_id: Setting name

          id: ID of the zone setting.

          value: Current value of the zone setting.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def edit(
        self,
        setting_id: str,
        *,
        zone_id: str,
        id: Literal["sha1_support"],
        value: Literal["off", "on"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[SettingEditResponse]:
        """
        Updates a single zone setting by the identifier

        Args:
          zone_id: Identifier

          setting_id: Setting name

          id: Zone setting identifier.

          value: Current value of the zone setting.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def edit(
        self,
        setting_id: str,
        *,
        zone_id: str,
        id: Literal["sort_query_string_for_cache"],
        value: Literal["on", "off"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[SettingEditResponse]:
        """
        Updates a single zone setting by the identifier

        Args:
          zone_id: Identifier

          setting_id: Setting name

          id: ID of the zone setting.

          value: Current value of the zone setting.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def edit(
        self,
        setting_id: str,
        *,
        zone_id: str,
        id: Literal["ssl"],
        value: Literal["off", "flexible", "full", "strict"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[SettingEditResponse]:
        """
        Updates a single zone setting by the identifier

        Args:
          zone_id: Identifier

          setting_id: Setting name

          id: ID of the zone setting.

          value: Current value of the zone setting.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def edit(
        self,
        setting_id: str,
        *,
        zone_id: str,
        id: Literal["ssl_recommender"] | NotGiven = NOT_GIVEN,
        enabled: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[SettingEditResponse]:
        """
        Updates a single zone setting by the identifier

        Args:
          zone_id: Identifier

          setting_id: Setting name

          id: Enrollment value for SSL/TLS Recommender.

          enabled: ssl-recommender enrollment setting.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def edit(
        self,
        setting_id: str,
        *,
        zone_id: str,
        id: Literal["tls_1_2_only"],
        value: Literal["off", "on"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[SettingEditResponse]:
        """
        Updates a single zone setting by the identifier

        Args:
          zone_id: Identifier

          setting_id: Setting name

          id: Zone setting identifier.

          value: Current value of the zone setting.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def edit(
        self,
        setting_id: str,
        *,
        zone_id: str,
        id: Literal["tls_1_3"],
        value: Literal["on", "off", "zrt"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[SettingEditResponse]:
        """
        Updates a single zone setting by the identifier

        Args:
          zone_id: Identifier

          setting_id: Setting name

          id: ID of the zone setting.

          value: Current value of the zone setting.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def edit(
        self,
        setting_id: str,
        *,
        zone_id: str,
        id: Literal["tls_client_auth"],
        value: Literal["on", "off"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[SettingEditResponse]:
        """
        Updates a single zone setting by the identifier

        Args:
          zone_id: Identifier

          setting_id: Setting name

          id: ID of the zone setting.

          value: Current value of the zone setting.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def edit(
        self,
        setting_id: str,
        *,
        zone_id: str,
        id: Literal["true_client_ip_header"],
        value: Literal["on", "off"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[SettingEditResponse]:
        """
        Updates a single zone setting by the identifier

        Args:
          zone_id: Identifier

          setting_id: Setting name

          id: ID of the zone setting.

          value: Current value of the zone setting.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def edit(
        self,
        setting_id: str,
        *,
        zone_id: str,
        id: Literal["waf"],
        value: Literal["on", "off"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[SettingEditResponse]:
        """
        Updates a single zone setting by the identifier

        Args:
          zone_id: Identifier

          setting_id: Setting name

          id: ID of the zone setting.

          value: Current value of the zone setting.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def edit(
        self,
        setting_id: str,
        *,
        zone_id: str,
        id: Literal["webp"],
        value: Literal["off", "on"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[SettingEditResponse]:
        """
        Updates a single zone setting by the identifier

        Args:
          zone_id: Identifier

          setting_id: Setting name

          id: ID of the zone setting.

          value: Current value of the zone setting.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def edit(
        self,
        setting_id: str,
        *,
        zone_id: str,
        id: Literal["websockets"],
        value: Literal["off", "on"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[SettingEditResponse]:
        """
        Updates a single zone setting by the identifier

        Args:
          zone_id: Identifier

          setting_id: Setting name

          id: ID of the zone setting.

          value: Current value of the zone setting.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["zone_id", "id", "value"], ["zone_id", "id"], ["zone_id"])
    async def edit(
        self,
        setting_id: str,
        *,
        zone_id: str,
        id: Literal["0rtt"]
        | Literal["advanced_ddos"]
        | Literal["aegis"]
        | Literal["always_online"]
        | Literal["always_use_https"]
        | Literal["automatic_https_rewrites"]
        | Literal["brotli"]
        | Literal["browser_cache_ttl"]
        | Literal["browser_check"]
        | Literal["cache_level"]
        | Literal["challenge_ttl"]
        | Literal["ciphers"]
        | Literal["cname_flattening"]
        | Literal["development_mode"]
        | Literal["early_hints"]
        | Literal["edge_cache_ttl"]
        | Literal["email_obfuscation"]
        | Literal["h2_prioritization"]
        | Literal["hotlink_protection"]
        | Literal["http2"]
        | Literal["http3"]
        | Literal["image_resizing"]
        | Literal["ip_geolocation"]
        | Literal["ipv6"]
        | Literal["max_upload"]
        | Literal["min_tls_version"]
        | Literal["mirage"]
        | Literal["nel"]
        | Literal["opportunistic_encryption"]
        | Literal["opportunistic_onion"]
        | Literal["orange_to_orange"]
        | Literal["origin_error_page_pass_thru"]
        | Literal["origin_h2_max_streams"]
        | Literal["origin_max_http_version"]
        | Literal["polish"]
        | Literal["prefetch_preload"]
        | Literal["privacy_pass"]
        | Literal["proxy_read_timeout"]
        | Literal["pseudo_ipv4"]
        | Literal["replace_insecure_js"]
        | Literal["response_buffering"]
        | Literal["rocket_loader"]
        | Literal["automatic_platform_optimization"]
        | Literal["security_header"]
        | Literal["security_level"]
        | Literal["server_side_exclude"]
        | Literal["sha1_support"]
        | Literal["sort_query_string_for_cache"]
        | Literal["ssl"]
        | Literal["ssl_recommender"]
        | Literal["tls_1_2_only"]
        | Literal["tls_1_3"]
        | Literal["tls_client_auth"]
        | Literal["true_client_ip_header"]
        | Literal["waf"]
        | Literal["webp"]
        | Literal["websockets"]
        | NotGiven = NOT_GIVEN,
        value: Literal["on", "off"]
        | setting_edit_params.ZonesCacheRulesAegisValue
        | Literal[
            0,
            30,
            60,
            120,
            300,
            1200,
            1800,
            3600,
            7200,
            10800,
            14400,
            18000,
            28800,
            43200,
            57600,
            72000,
            86400,
            172800,
            259200,
            345600,
            432000,
            691200,
            1382400,
            2073600,
            2678400,
            5356800,
            16070400,
            31536000,
        ]
        | Literal["aggressive", "basic", "simplified"]
        | Literal[300, 900, 1800, 2700, 3600, 7200, 10800, 14400, 28800, 57600, 86400, 604800, 2592000, 31536000]
        | List[str]
        | Literal["flatten_at_root", "flatten_all"]
        | Literal[
            30,
            60,
            300,
            1200,
            1800,
            3600,
            7200,
            10800,
            14400,
            18000,
            28800,
            43200,
            57600,
            72000,
            86400,
            172800,
            259200,
            345600,
            432000,
            518400,
            604800,
        ]
        | Literal["on", "off", "custom"]
        | Literal["on", "off", "open"]
        | Literal[100, 200, 500]
        | Literal["1.0", "1.1", "1.2", "1.3"]
        | setting_edit_params.NELValue
        | int
        | Literal["2", "1"]
        | Literal["off", "lossless", "lossy"]
        | float
        | Literal["off", "add_header", "overwrite_header"]
        | AutomaticPlatformOptimizationParam
        | setting_edit_params.SecurityHeadersValue
        | Literal["off", "essentially_off", "low", "medium", "high", "under_attack"]
        | Literal["off", "flexible", "full", "strict"]
        | Literal["on", "off", "zrt"]
        | NotGiven = NOT_GIVEN,
        enabled: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[SettingEditResponse]:
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not setting_id:
            raise ValueError(f"Expected a non-empty value for `setting_id` but received {setting_id!r}")
        return cast(
            Optional[SettingEditResponse],
            await self._patch(
                f"/zones/{zone_id}/settings/{setting_id}",
                body=await async_maybe_transform(
                    {
                        "id": id,
                        "value": value,
                        "enabled": enabled,
                    },
                    setting_edit_params.SettingEditParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper[Optional[SettingEditResponse]]._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[SettingEditResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def get(
        self,
        setting_id: str,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[SettingGetResponse]:
        """
        Fetch a single zone setting by name

        Args:
          zone_id: Identifier

          setting_id: Setting name

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not setting_id:
            raise ValueError(f"Expected a non-empty value for `setting_id` but received {setting_id!r}")
        return cast(
            Optional[SettingGetResponse],
            await self._get(
                f"/zones/{zone_id}/settings/{setting_id}",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper[Optional[SettingGetResponse]]._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[SettingGetResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class SettingsResourceWithRawResponse:
    def __init__(self, settings: SettingsResource) -> None:
        self._settings = settings

        self.edit = to_raw_response_wrapper(
            settings.edit,
        )
        self.get = to_raw_response_wrapper(
            settings.get,
        )


class AsyncSettingsResourceWithRawResponse:
    def __init__(self, settings: AsyncSettingsResource) -> None:
        self._settings = settings

        self.edit = async_to_raw_response_wrapper(
            settings.edit,
        )
        self.get = async_to_raw_response_wrapper(
            settings.get,
        )


class SettingsResourceWithStreamingResponse:
    def __init__(self, settings: SettingsResource) -> None:
        self._settings = settings

        self.edit = to_streamed_response_wrapper(
            settings.edit,
        )
        self.get = to_streamed_response_wrapper(
            settings.get,
        )


class AsyncSettingsResourceWithStreamingResponse:
    def __init__(self, settings: AsyncSettingsResource) -> None:
        self._settings = settings

        self.edit = async_to_streamed_response_wrapper(
            settings.edit,
        )
        self.get = async_to_streamed_response_wrapper(
            settings.get,
        )
