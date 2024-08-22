# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ....._compat import cached_property

from .....types.zero_trust.access.certificates.setting_update_response import SettingUpdateResponse

from ....._wrappers import ResultWrapper

from ....._utils import maybe_transform, async_maybe_transform

from typing import Optional, Type, Iterable

from ....._base_client import make_request_options

from .....types.zero_trust.access.certificates.certificate_settings_param import CertificateSettingsParam

from .....types.zero_trust.access.certificates.setting_get_response import SettingGetResponse

from ....._response import to_raw_response_wrapper, async_to_raw_response_wrapper, to_streamed_response_wrapper, async_to_streamed_response_wrapper

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ....._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ....._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ....._resource import SyncAPIResource, AsyncAPIResource
from .....types import shared_params
from .....types.zero_trust.access.certificates import setting_update_params
from typing import cast
from typing import cast
from typing import cast
from typing import cast

__all__ = ["SettingsResource", "AsyncSettingsResource"]

class SettingsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SettingsResourceWithRawResponse:
        return SettingsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SettingsResourceWithStreamingResponse:
        return SettingsResourceWithStreamingResponse(self)

    def update(self,
    *,
    settings: Iterable[CertificateSettingsParam],
    account_id: str | NotGiven = NOT_GIVEN,
    zone_id: str | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Optional[SettingUpdateResponse]:
        """
        Updates an mTLS certificate's hostname settings.

        Args:
          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if account_id and zone_id:
          raise ValueError('You cannot provide both account_id and zone_id');

        if account_id:
          account_or_zone = "accounts"
          account_or_zone_id = account_id
        else:
          if not zone_id:
            raise ValueError('You must provide either account_id or zone_id');

          account_or_zone = "zones"
          account_or_zone_id = zone_id
        return self._put(
            f"/{account_or_zone}/{account_or_zone_id}/access/certificates/settings",
            body=maybe_transform({
                "settings": settings
            }, setting_update_params.SettingUpdateParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[Optional[SettingUpdateResponse]]._unwrapper),
            cast_to=cast(Type[Optional[SettingUpdateResponse]], ResultWrapper[SettingUpdateResponse]),
        )

    def get(self,
    *,
    account_id: str | NotGiven = NOT_GIVEN,
    zone_id: str | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Optional[SettingGetResponse]:
        """
        List all mTLS hostname settings for this account or zone.

        Args:
          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if account_id and zone_id:
          raise ValueError('You cannot provide both account_id and zone_id');

        if account_id:
          account_or_zone = "accounts"
          account_or_zone_id = account_id
        else:
          if not zone_id:
            raise ValueError('You must provide either account_id or zone_id');

          account_or_zone = "zones"
          account_or_zone_id = zone_id
        return self._get(
            f"/{account_or_zone}/{account_or_zone_id}/access/certificates/settings",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[Optional[SettingGetResponse]]._unwrapper),
            cast_to=cast(Type[Optional[SettingGetResponse]], ResultWrapper[SettingGetResponse]),
        )

class AsyncSettingsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSettingsResourceWithRawResponse:
        return AsyncSettingsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSettingsResourceWithStreamingResponse:
        return AsyncSettingsResourceWithStreamingResponse(self)

    async def update(self,
    *,
    settings: Iterable[CertificateSettingsParam],
    account_id: str | NotGiven = NOT_GIVEN,
    zone_id: str | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Optional[SettingUpdateResponse]:
        """
        Updates an mTLS certificate's hostname settings.

        Args:
          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if account_id and zone_id:
          raise ValueError('You cannot provide both account_id and zone_id');

        if account_id:
          account_or_zone = "accounts"
          account_or_zone_id = account_id
        else:
          if not zone_id:
            raise ValueError('You must provide either account_id or zone_id');

          account_or_zone = "zones"
          account_or_zone_id = zone_id
        return await self._put(
            f"/{account_or_zone}/{account_or_zone_id}/access/certificates/settings",
            body=await async_maybe_transform({
                "settings": settings
            }, setting_update_params.SettingUpdateParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[Optional[SettingUpdateResponse]]._unwrapper),
            cast_to=cast(Type[Optional[SettingUpdateResponse]], ResultWrapper[SettingUpdateResponse]),
        )

    async def get(self,
    *,
    account_id: str | NotGiven = NOT_GIVEN,
    zone_id: str | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Optional[SettingGetResponse]:
        """
        List all mTLS hostname settings for this account or zone.

        Args:
          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if account_id and zone_id:
          raise ValueError('You cannot provide both account_id and zone_id');

        if account_id:
          account_or_zone = "accounts"
          account_or_zone_id = account_id
        else:
          if not zone_id:
            raise ValueError('You must provide either account_id or zone_id');

          account_or_zone = "zones"
          account_or_zone_id = zone_id
        return await self._get(
            f"/{account_or_zone}/{account_or_zone_id}/access/certificates/settings",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[Optional[SettingGetResponse]]._unwrapper),
            cast_to=cast(Type[Optional[SettingGetResponse]], ResultWrapper[SettingGetResponse]),
        )

class SettingsResourceWithRawResponse:
    def __init__(self, settings: SettingsResource) -> None:
        self._settings = settings

        self.update = to_raw_response_wrapper(
            settings.update,
        )
        self.get = to_raw_response_wrapper(
            settings.get,
        )

class AsyncSettingsResourceWithRawResponse:
    def __init__(self, settings: AsyncSettingsResource) -> None:
        self._settings = settings

        self.update = async_to_raw_response_wrapper(
            settings.update,
        )
        self.get = async_to_raw_response_wrapper(
            settings.get,
        )

class SettingsResourceWithStreamingResponse:
    def __init__(self, settings: SettingsResource) -> None:
        self._settings = settings

        self.update = to_streamed_response_wrapper(
            settings.update,
        )
        self.get = to_streamed_response_wrapper(
            settings.get,
        )

class AsyncSettingsResourceWithStreamingResponse:
    def __init__(self, settings: AsyncSettingsResource) -> None:
        self._settings = settings

        self.update = async_to_streamed_response_wrapper(
            settings.update,
        )
        self.get = async_to_streamed_response_wrapper(
            settings.get,
        )