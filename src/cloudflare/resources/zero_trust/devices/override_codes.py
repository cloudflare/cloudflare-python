# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._compat import cached_property

from ....types.zero_trust.devices.override_code_list_response import OverrideCodeListResponse

from ...._wrappers import ResultWrapper

from typing import Optional, Type

from ...._base_client import make_request_options

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
from ....types import shared_params
from typing import cast
from typing import cast

__all__ = ["OverrideCodesResource", "AsyncOverrideCodesResource"]


class OverrideCodesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> OverrideCodesResourceWithRawResponse:
        return OverrideCodesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OverrideCodesResourceWithStreamingResponse:
        return OverrideCodesResourceWithStreamingResponse(self)

    def list(
        self,
        device_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[OverrideCodeListResponse]:
        """Fetches a one-time use admin override code for a device.

        This relies on the
        **Admin Override** setting being enabled in your device configuration.

        Args:
          device_id: Device ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not device_id:
            raise ValueError(f"Expected a non-empty value for `device_id` but received {device_id!r}")
        return self._get(
            f"/accounts/{account_id}/devices/{device_id}/override_codes",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[OverrideCodeListResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[OverrideCodeListResponse]], ResultWrapper[OverrideCodeListResponse]),
        )


class AsyncOverrideCodesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncOverrideCodesResourceWithRawResponse:
        return AsyncOverrideCodesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOverrideCodesResourceWithStreamingResponse:
        return AsyncOverrideCodesResourceWithStreamingResponse(self)

    async def list(
        self,
        device_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[OverrideCodeListResponse]:
        """Fetches a one-time use admin override code for a device.

        This relies on the
        **Admin Override** setting being enabled in your device configuration.

        Args:
          device_id: Device ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not device_id:
            raise ValueError(f"Expected a non-empty value for `device_id` but received {device_id!r}")
        return await self._get(
            f"/accounts/{account_id}/devices/{device_id}/override_codes",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[OverrideCodeListResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[OverrideCodeListResponse]], ResultWrapper[OverrideCodeListResponse]),
        )


class OverrideCodesResourceWithRawResponse:
    def __init__(self, override_codes: OverrideCodesResource) -> None:
        self._override_codes = override_codes

        self.list = to_raw_response_wrapper(
            override_codes.list,
        )


class AsyncOverrideCodesResourceWithRawResponse:
    def __init__(self, override_codes: AsyncOverrideCodesResource) -> None:
        self._override_codes = override_codes

        self.list = async_to_raw_response_wrapper(
            override_codes.list,
        )


class OverrideCodesResourceWithStreamingResponse:
    def __init__(self, override_codes: OverrideCodesResource) -> None:
        self._override_codes = override_codes

        self.list = to_streamed_response_wrapper(
            override_codes.list,
        )


class AsyncOverrideCodesResourceWithStreamingResponse:
    def __init__(self, override_codes: AsyncOverrideCodesResource) -> None:
        self._override_codes = override_codes

        self.list = async_to_streamed_response_wrapper(
            override_codes.list,
        )
