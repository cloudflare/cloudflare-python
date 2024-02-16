# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from ..._compat import cached_property

from ...types.devices import RevokeDevicesRevokeDevicesResponse

from typing import Optional, List

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
from ...types.devices import revoke_devices_revoke_devices_params
from ..._wrappers import ResultWrapper
from typing import cast
from typing import cast
from typing import cast
from typing import cast

__all__ = ["Revokes", "AsyncRevokes"]


class Revokes(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RevokesWithRawResponse:
        return RevokesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RevokesWithStreamingResponse:
        return RevokesWithStreamingResponse(self)

    def devices_revoke_devices(
        self,
        identifier: object,
        *,
        body: List[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[RevokeDevicesRevokeDevicesResponse]:
        """
        Revokes a list of devices.

        Args:
          body: A list of device ids to revoke.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return cast(
            Optional[RevokeDevicesRevokeDevicesResponse],
            self._post(
                f"/accounts/{identifier}/devices/revoke",
                body=maybe_transform(body, revoke_devices_revoke_devices_params.RevokeDevicesRevokeDevicesParams),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[RevokeDevicesRevokeDevicesResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class AsyncRevokes(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRevokesWithRawResponse:
        return AsyncRevokesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRevokesWithStreamingResponse:
        return AsyncRevokesWithStreamingResponse(self)

    async def devices_revoke_devices(
        self,
        identifier: object,
        *,
        body: List[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[RevokeDevicesRevokeDevicesResponse]:
        """
        Revokes a list of devices.

        Args:
          body: A list of device ids to revoke.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return cast(
            Optional[RevokeDevicesRevokeDevicesResponse],
            await self._post(
                f"/accounts/{identifier}/devices/revoke",
                body=maybe_transform(body, revoke_devices_revoke_devices_params.RevokeDevicesRevokeDevicesParams),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[RevokeDevicesRevokeDevicesResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class RevokesWithRawResponse:
    def __init__(self, revokes: Revokes) -> None:
        self._revokes = revokes

        self.devices_revoke_devices = to_raw_response_wrapper(
            revokes.devices_revoke_devices,
        )


class AsyncRevokesWithRawResponse:
    def __init__(self, revokes: AsyncRevokes) -> None:
        self._revokes = revokes

        self.devices_revoke_devices = async_to_raw_response_wrapper(
            revokes.devices_revoke_devices,
        )


class RevokesWithStreamingResponse:
    def __init__(self, revokes: Revokes) -> None:
        self._revokes = revokes

        self.devices_revoke_devices = to_streamed_response_wrapper(
            revokes.devices_revoke_devices,
        )


class AsyncRevokesWithStreamingResponse:
    def __init__(self, revokes: AsyncRevokes) -> None:
        self._revokes = revokes

        self.devices_revoke_devices = async_to_streamed_response_wrapper(
            revokes.devices_revoke_devices,
        )
