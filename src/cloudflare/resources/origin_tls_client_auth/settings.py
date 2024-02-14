# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from ..._compat import cached_property

from ...types.origin_tls_client_auth import (
    SettingZoneLevelAuthenticatedOriginPullsGetEnablementSettingForZoneResponse,
    SettingZoneLevelAuthenticatedOriginPullsSetEnablementForZoneResponse,
)

from typing import Type

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
from ...types.origin_tls_client_auth import setting_zone_level_authenticated_origin_pulls_set_enablement_for_zone_params
from ..._wrappers import ResultWrapper
from typing import cast
from typing import cast
from typing import cast
from typing import cast

__all__ = ["Settings", "AsyncSettings"]


class Settings(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SettingsWithRawResponse:
        return SettingsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SettingsWithStreamingResponse:
        return SettingsWithStreamingResponse(self)

    def zone_level_authenticated_origin_pulls_get_enablement_setting_for_zone(
        self,
        zone_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SettingZoneLevelAuthenticatedOriginPullsGetEnablementSettingForZoneResponse:
        """Get whether zone-level authenticated origin pulls is enabled or not.

        It is false
        by default.

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
            f"/zones/{zone_id}/origin_tls_client_auth/settings",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[SettingZoneLevelAuthenticatedOriginPullsGetEnablementSettingForZoneResponse],
                ResultWrapper[SettingZoneLevelAuthenticatedOriginPullsGetEnablementSettingForZoneResponse],
            ),
        )

    def zone_level_authenticated_origin_pulls_set_enablement_for_zone(
        self,
        zone_id: str,
        *,
        enabled: bool,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SettingZoneLevelAuthenticatedOriginPullsSetEnablementForZoneResponse:
        """Enable or disable zone-level authenticated origin pulls.

        'enabled' should be set
        true either before/after the certificate is uploaded to see the certificate in
        use.

        Args:
          zone_id: Identifier

          enabled: Indicates whether zone-level authenticated origin pulls is enabled.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._put(
            f"/zones/{zone_id}/origin_tls_client_auth/settings",
            body=maybe_transform(
                {"enabled": enabled},
                setting_zone_level_authenticated_origin_pulls_set_enablement_for_zone_params.SettingZoneLevelAuthenticatedOriginPullsSetEnablementForZoneParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[SettingZoneLevelAuthenticatedOriginPullsSetEnablementForZoneResponse],
                ResultWrapper[SettingZoneLevelAuthenticatedOriginPullsSetEnablementForZoneResponse],
            ),
        )


class AsyncSettings(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSettingsWithRawResponse:
        return AsyncSettingsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSettingsWithStreamingResponse:
        return AsyncSettingsWithStreamingResponse(self)

    async def zone_level_authenticated_origin_pulls_get_enablement_setting_for_zone(
        self,
        zone_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SettingZoneLevelAuthenticatedOriginPullsGetEnablementSettingForZoneResponse:
        """Get whether zone-level authenticated origin pulls is enabled or not.

        It is false
        by default.

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
            f"/zones/{zone_id}/origin_tls_client_auth/settings",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[SettingZoneLevelAuthenticatedOriginPullsGetEnablementSettingForZoneResponse],
                ResultWrapper[SettingZoneLevelAuthenticatedOriginPullsGetEnablementSettingForZoneResponse],
            ),
        )

    async def zone_level_authenticated_origin_pulls_set_enablement_for_zone(
        self,
        zone_id: str,
        *,
        enabled: bool,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SettingZoneLevelAuthenticatedOriginPullsSetEnablementForZoneResponse:
        """Enable or disable zone-level authenticated origin pulls.

        'enabled' should be set
        true either before/after the certificate is uploaded to see the certificate in
        use.

        Args:
          zone_id: Identifier

          enabled: Indicates whether zone-level authenticated origin pulls is enabled.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._put(
            f"/zones/{zone_id}/origin_tls_client_auth/settings",
            body=maybe_transform(
                {"enabled": enabled},
                setting_zone_level_authenticated_origin_pulls_set_enablement_for_zone_params.SettingZoneLevelAuthenticatedOriginPullsSetEnablementForZoneParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[SettingZoneLevelAuthenticatedOriginPullsSetEnablementForZoneResponse],
                ResultWrapper[SettingZoneLevelAuthenticatedOriginPullsSetEnablementForZoneResponse],
            ),
        )


class SettingsWithRawResponse:
    def __init__(self, settings: Settings) -> None:
        self._settings = settings

        self.zone_level_authenticated_origin_pulls_get_enablement_setting_for_zone = to_raw_response_wrapper(
            settings.zone_level_authenticated_origin_pulls_get_enablement_setting_for_zone,
        )
        self.zone_level_authenticated_origin_pulls_set_enablement_for_zone = to_raw_response_wrapper(
            settings.zone_level_authenticated_origin_pulls_set_enablement_for_zone,
        )


class AsyncSettingsWithRawResponse:
    def __init__(self, settings: AsyncSettings) -> None:
        self._settings = settings

        self.zone_level_authenticated_origin_pulls_get_enablement_setting_for_zone = async_to_raw_response_wrapper(
            settings.zone_level_authenticated_origin_pulls_get_enablement_setting_for_zone,
        )
        self.zone_level_authenticated_origin_pulls_set_enablement_for_zone = async_to_raw_response_wrapper(
            settings.zone_level_authenticated_origin_pulls_set_enablement_for_zone,
        )


class SettingsWithStreamingResponse:
    def __init__(self, settings: Settings) -> None:
        self._settings = settings

        self.zone_level_authenticated_origin_pulls_get_enablement_setting_for_zone = to_streamed_response_wrapper(
            settings.zone_level_authenticated_origin_pulls_get_enablement_setting_for_zone,
        )
        self.zone_level_authenticated_origin_pulls_set_enablement_for_zone = to_streamed_response_wrapper(
            settings.zone_level_authenticated_origin_pulls_set_enablement_for_zone,
        )


class AsyncSettingsWithStreamingResponse:
    def __init__(self, settings: AsyncSettings) -> None:
        self._settings = settings

        self.zone_level_authenticated_origin_pulls_get_enablement_setting_for_zone = async_to_streamed_response_wrapper(
            settings.zone_level_authenticated_origin_pulls_get_enablement_setting_for_zone,
        )
        self.zone_level_authenticated_origin_pulls_set_enablement_for_zone = async_to_streamed_response_wrapper(
            settings.zone_level_authenticated_origin_pulls_set_enablement_for_zone,
        )
