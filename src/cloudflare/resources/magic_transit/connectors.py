# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._compat import cached_property

from ...types.magic_transit.connector_update_response import ConnectorUpdateResponse

from ..._wrappers import ResultWrapper

from ..._utils import maybe_transform, async_maybe_transform

from ..._base_client import make_request_options, AsyncPaginator

from typing import Type

from ...types.magic_transit.connector_list_response import ConnectorListResponse

from ...pagination import SyncSinglePage, AsyncSinglePage

from ...types.magic_transit.connector_edit_response import ConnectorEditResponse

from ...types.magic_transit.connector_get_response import ConnectorGetResponse

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
from ...types import shared_params
from ...types.magic_transit import connector_update_params
from ...types.magic_transit import connector_edit_params
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast

__all__ = ["ConnectorsResource", "AsyncConnectorsResource"]


class ConnectorsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ConnectorsResourceWithRawResponse:
        return ConnectorsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ConnectorsResourceWithStreamingResponse:
        return ConnectorsResourceWithStreamingResponse(self)

    def update(
        self,
        connector_id: str,
        *,
        account_id: str,
        activated: bool | NotGiven = NOT_GIVEN,
        interrupt_window_duration_hours: float | NotGiven = NOT_GIVEN,
        interrupt_window_hour_of_day: float | NotGiven = NOT_GIVEN,
        notes: str | NotGiven = NOT_GIVEN,
        timezone: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ConnectorUpdateResponse:
        """
        Replace Connector

        Args:
          account_id: Account identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not connector_id:
            raise ValueError(f"Expected a non-empty value for `connector_id` but received {connector_id!r}")
        return self._put(
            f"/accounts/{account_id}/magic/connectors/{connector_id}",
            body=maybe_transform(
                {
                    "activated": activated,
                    "interrupt_window_duration_hours": interrupt_window_duration_hours,
                    "interrupt_window_hour_of_day": interrupt_window_hour_of_day,
                    "notes": notes,
                    "timezone": timezone,
                },
                connector_update_params.ConnectorUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[ConnectorUpdateResponse]._unwrapper,
            ),
            cast_to=cast(Type[ConnectorUpdateResponse], ResultWrapper[ConnectorUpdateResponse]),
        )

    def list(
        self,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncSinglePage[ConnectorListResponse]:
        """
        List Connectors

        Args:
          account_id: Account identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/magic/connectors",
            page=SyncSinglePage[ConnectorListResponse],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=ConnectorListResponse,
        )

    def edit(
        self,
        connector_id: str,
        *,
        account_id: str,
        activated: bool | NotGiven = NOT_GIVEN,
        interrupt_window_duration_hours: float | NotGiven = NOT_GIVEN,
        interrupt_window_hour_of_day: float | NotGiven = NOT_GIVEN,
        notes: str | NotGiven = NOT_GIVEN,
        timezone: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ConnectorEditResponse:
        """
        Update Connector

        Args:
          account_id: Account identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not connector_id:
            raise ValueError(f"Expected a non-empty value for `connector_id` but received {connector_id!r}")
        return self._patch(
            f"/accounts/{account_id}/magic/connectors/{connector_id}",
            body=maybe_transform(
                {
                    "activated": activated,
                    "interrupt_window_duration_hours": interrupt_window_duration_hours,
                    "interrupt_window_hour_of_day": interrupt_window_hour_of_day,
                    "notes": notes,
                    "timezone": timezone,
                },
                connector_edit_params.ConnectorEditParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[ConnectorEditResponse]._unwrapper,
            ),
            cast_to=cast(Type[ConnectorEditResponse], ResultWrapper[ConnectorEditResponse]),
        )

    def get(
        self,
        connector_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ConnectorGetResponse:
        """
        Fetch Connector

        Args:
          account_id: Account identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not connector_id:
            raise ValueError(f"Expected a non-empty value for `connector_id` but received {connector_id!r}")
        return self._get(
            f"/accounts/{account_id}/magic/connectors/{connector_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[ConnectorGetResponse]._unwrapper,
            ),
            cast_to=cast(Type[ConnectorGetResponse], ResultWrapper[ConnectorGetResponse]),
        )


class AsyncConnectorsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncConnectorsResourceWithRawResponse:
        return AsyncConnectorsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncConnectorsResourceWithStreamingResponse:
        return AsyncConnectorsResourceWithStreamingResponse(self)

    async def update(
        self,
        connector_id: str,
        *,
        account_id: str,
        activated: bool | NotGiven = NOT_GIVEN,
        interrupt_window_duration_hours: float | NotGiven = NOT_GIVEN,
        interrupt_window_hour_of_day: float | NotGiven = NOT_GIVEN,
        notes: str | NotGiven = NOT_GIVEN,
        timezone: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ConnectorUpdateResponse:
        """
        Replace Connector

        Args:
          account_id: Account identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not connector_id:
            raise ValueError(f"Expected a non-empty value for `connector_id` but received {connector_id!r}")
        return await self._put(
            f"/accounts/{account_id}/magic/connectors/{connector_id}",
            body=await async_maybe_transform(
                {
                    "activated": activated,
                    "interrupt_window_duration_hours": interrupt_window_duration_hours,
                    "interrupt_window_hour_of_day": interrupt_window_hour_of_day,
                    "notes": notes,
                    "timezone": timezone,
                },
                connector_update_params.ConnectorUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[ConnectorUpdateResponse]._unwrapper,
            ),
            cast_to=cast(Type[ConnectorUpdateResponse], ResultWrapper[ConnectorUpdateResponse]),
        )

    def list(
        self,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[ConnectorListResponse, AsyncSinglePage[ConnectorListResponse]]:
        """
        List Connectors

        Args:
          account_id: Account identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/magic/connectors",
            page=AsyncSinglePage[ConnectorListResponse],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=ConnectorListResponse,
        )

    async def edit(
        self,
        connector_id: str,
        *,
        account_id: str,
        activated: bool | NotGiven = NOT_GIVEN,
        interrupt_window_duration_hours: float | NotGiven = NOT_GIVEN,
        interrupt_window_hour_of_day: float | NotGiven = NOT_GIVEN,
        notes: str | NotGiven = NOT_GIVEN,
        timezone: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ConnectorEditResponse:
        """
        Update Connector

        Args:
          account_id: Account identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not connector_id:
            raise ValueError(f"Expected a non-empty value for `connector_id` but received {connector_id!r}")
        return await self._patch(
            f"/accounts/{account_id}/magic/connectors/{connector_id}",
            body=await async_maybe_transform(
                {
                    "activated": activated,
                    "interrupt_window_duration_hours": interrupt_window_duration_hours,
                    "interrupt_window_hour_of_day": interrupt_window_hour_of_day,
                    "notes": notes,
                    "timezone": timezone,
                },
                connector_edit_params.ConnectorEditParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[ConnectorEditResponse]._unwrapper,
            ),
            cast_to=cast(Type[ConnectorEditResponse], ResultWrapper[ConnectorEditResponse]),
        )

    async def get(
        self,
        connector_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ConnectorGetResponse:
        """
        Fetch Connector

        Args:
          account_id: Account identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not connector_id:
            raise ValueError(f"Expected a non-empty value for `connector_id` but received {connector_id!r}")
        return await self._get(
            f"/accounts/{account_id}/magic/connectors/{connector_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[ConnectorGetResponse]._unwrapper,
            ),
            cast_to=cast(Type[ConnectorGetResponse], ResultWrapper[ConnectorGetResponse]),
        )


class ConnectorsResourceWithRawResponse:
    def __init__(self, connectors: ConnectorsResource) -> None:
        self._connectors = connectors

        self.update = to_raw_response_wrapper(
            connectors.update,
        )
        self.list = to_raw_response_wrapper(
            connectors.list,
        )
        self.edit = to_raw_response_wrapper(
            connectors.edit,
        )
        self.get = to_raw_response_wrapper(
            connectors.get,
        )


class AsyncConnectorsResourceWithRawResponse:
    def __init__(self, connectors: AsyncConnectorsResource) -> None:
        self._connectors = connectors

        self.update = async_to_raw_response_wrapper(
            connectors.update,
        )
        self.list = async_to_raw_response_wrapper(
            connectors.list,
        )
        self.edit = async_to_raw_response_wrapper(
            connectors.edit,
        )
        self.get = async_to_raw_response_wrapper(
            connectors.get,
        )


class ConnectorsResourceWithStreamingResponse:
    def __init__(self, connectors: ConnectorsResource) -> None:
        self._connectors = connectors

        self.update = to_streamed_response_wrapper(
            connectors.update,
        )
        self.list = to_streamed_response_wrapper(
            connectors.list,
        )
        self.edit = to_streamed_response_wrapper(
            connectors.edit,
        )
        self.get = to_streamed_response_wrapper(
            connectors.get,
        )


class AsyncConnectorsResourceWithStreamingResponse:
    def __init__(self, connectors: AsyncConnectorsResource) -> None:
        self._connectors = connectors

        self.update = async_to_streamed_response_wrapper(
            connectors.update,
        )
        self.list = async_to_streamed_response_wrapper(
            connectors.list,
        )
        self.edit = async_to_streamed_response_wrapper(
            connectors.edit,
        )
        self.get = async_to_streamed_response_wrapper(
            connectors.get,
        )
