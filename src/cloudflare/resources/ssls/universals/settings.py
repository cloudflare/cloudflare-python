# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from ...._compat import cached_property

from ....types.ssls.universals import SettingUpdateResponse, SettingGetResponse

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
from ....types.ssls.universals import setting_update_params
from ...._wrappers import ResultWrapper
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

    def update(
        self,
        zone_id: str,
        *,
        enabled: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SettingUpdateResponse:
        """
        Patch Universal SSL Settings for a Zone.

        Args:
          zone_id: Identifier

          enabled: Disabling Universal SSL removes any currently active Universal SSL certificates
              for your zone from the edge and prevents any future Universal SSL certificates
              from being ordered. If there are no advanced certificates or custom certificates
              uploaded for the domain, visitors will be unable to access the domain over
              HTTPS.

              By disabling Universal SSL, you understand that the following Cloudflare
              settings and preferences will result in visitors being unable to visit your
              domain unless you have uploaded a custom certificate or purchased an advanced
              certificate.

              - HSTS
              - Always Use HTTPS
              - Opportunistic Encryption
              - Onion Routing
              - Any Page Rules redirecting traffic to HTTPS

              Similarly, any HTTP redirect to HTTPS at the origin while the Cloudflare proxy
              is enabled will result in users being unable to visit your site without a valid
              certificate at Cloudflare's edge.

              If you do not have a valid custom or advanced certificate at Cloudflare's edge
              and are unsure if any of the above Cloudflare settings are enabled, or if any
              HTTP redirects exist at your origin, we advise leaving Universal SSL enabled for
              your domain.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._patch(
            f"/zones/{zone_id}/ssl/universal/settings",
            body=maybe_transform({"enabled": enabled}, setting_update_params.SettingUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[SettingUpdateResponse], ResultWrapper[SettingUpdateResponse]),
        )

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
    ) -> SettingGetResponse:
        """
        Get Universal SSL Settings for a Zone.

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
            f"/zones/{zone_id}/ssl/universal/settings",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[SettingGetResponse], ResultWrapper[SettingGetResponse]),
        )


class AsyncSettings(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSettingsWithRawResponse:
        return AsyncSettingsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSettingsWithStreamingResponse:
        return AsyncSettingsWithStreamingResponse(self)

    async def update(
        self,
        zone_id: str,
        *,
        enabled: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SettingUpdateResponse:
        """
        Patch Universal SSL Settings for a Zone.

        Args:
          zone_id: Identifier

          enabled: Disabling Universal SSL removes any currently active Universal SSL certificates
              for your zone from the edge and prevents any future Universal SSL certificates
              from being ordered. If there are no advanced certificates or custom certificates
              uploaded for the domain, visitors will be unable to access the domain over
              HTTPS.

              By disabling Universal SSL, you understand that the following Cloudflare
              settings and preferences will result in visitors being unable to visit your
              domain unless you have uploaded a custom certificate or purchased an advanced
              certificate.

              - HSTS
              - Always Use HTTPS
              - Opportunistic Encryption
              - Onion Routing
              - Any Page Rules redirecting traffic to HTTPS

              Similarly, any HTTP redirect to HTTPS at the origin while the Cloudflare proxy
              is enabled will result in users being unable to visit your site without a valid
              certificate at Cloudflare's edge.

              If you do not have a valid custom or advanced certificate at Cloudflare's edge
              and are unsure if any of the above Cloudflare settings are enabled, or if any
              HTTP redirects exist at your origin, we advise leaving Universal SSL enabled for
              your domain.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._patch(
            f"/zones/{zone_id}/ssl/universal/settings",
            body=maybe_transform({"enabled": enabled}, setting_update_params.SettingUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[SettingUpdateResponse], ResultWrapper[SettingUpdateResponse]),
        )

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
    ) -> SettingGetResponse:
        """
        Get Universal SSL Settings for a Zone.

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
            f"/zones/{zone_id}/ssl/universal/settings",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[SettingGetResponse], ResultWrapper[SettingGetResponse]),
        )


class SettingsWithRawResponse:
    def __init__(self, settings: Settings) -> None:
        self._settings = settings

        self.update = to_raw_response_wrapper(
            settings.update,
        )
        self.get = to_raw_response_wrapper(
            settings.get,
        )


class AsyncSettingsWithRawResponse:
    def __init__(self, settings: AsyncSettings) -> None:
        self._settings = settings

        self.update = async_to_raw_response_wrapper(
            settings.update,
        )
        self.get = async_to_raw_response_wrapper(
            settings.get,
        )


class SettingsWithStreamingResponse:
    def __init__(self, settings: Settings) -> None:
        self._settings = settings

        self.update = to_streamed_response_wrapper(
            settings.update,
        )
        self.get = to_streamed_response_wrapper(
            settings.get,
        )


class AsyncSettingsWithStreamingResponse:
    def __init__(self, settings: AsyncSettings) -> None:
        self._settings = settings

        self.update = async_to_streamed_response_wrapper(
            settings.update,
        )
        self.get = async_to_streamed_response_wrapper(
            settings.get,
        )
