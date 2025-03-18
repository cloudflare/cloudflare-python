# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Union, Iterable, Optional, cast
from datetime import datetime
from typing_extensions import Literal

import httpx

from .quota import (
    QuotaResource,
    AsyncQuotaResource,
    QuotaResourceWithRawResponse,
    AsyncQuotaResourceWithRawResponse,
    QuotaResourceWithStreamingResponse,
    AsyncQuotaResourceWithStreamingResponse,
)
from .devices import (
    DevicesResource,
    AsyncDevicesResource,
    DevicesResourceWithRawResponse,
    AsyncDevicesResourceWithRawResponse,
    DevicesResourceWithStreamingResponse,
    AsyncDevicesResourceWithStreamingResponse,
)
from .downloads import (
    DownloadsResource,
    AsyncDownloadsResource,
    DownloadsResourceWithRawResponse,
    AsyncDownloadsResourceWithRawResponse,
    DownloadsResourceWithStreamingResponse,
    AsyncDownloadsResourceWithStreamingResponse,
)
from ....._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ....._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....._wrappers import ResultWrapper
from .....pagination import SyncV4PagePagination, AsyncV4PagePagination
from ....._base_client import AsyncPaginator, make_request_options
from .....types.zero_trust.dex import command_list_params, command_create_params
from .....types.zero_trust.dex.command_list_response import CommandListResponse
from .....types.zero_trust.dex.command_create_response import CommandCreateResponse

__all__ = ["CommandsResource", "AsyncCommandsResource"]


class CommandsResource(SyncAPIResource):
    @cached_property
    def devices(self) -> DevicesResource:
        return DevicesResource(self._client)

    @cached_property
    def downloads(self) -> DownloadsResource:
        return DownloadsResource(self._client)

    @cached_property
    def quota(self) -> QuotaResource:
        return QuotaResource(self._client)

    @cached_property
    def with_raw_response(self) -> CommandsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return CommandsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CommandsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return CommandsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        account_id: str,
        commands: Iterable[command_create_params.Command],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[CommandCreateResponse]:
        """
        Initiate commands for up to 10 devices per account

        Args:
          commands: List of device-level commands to execute

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._post(
            f"/accounts/{account_id}/dex/commands",
            body=maybe_transform({"commands": commands}, command_create_params.CommandCreateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[CommandCreateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[CommandCreateResponse]], ResultWrapper[CommandCreateResponse]),
        )

    def list(
        self,
        *,
        account_id: str,
        page: float,
        per_page: float,
        command_type: str | NotGiven = NOT_GIVEN,
        device_id: str | NotGiven = NOT_GIVEN,
        from_: Union[str, datetime] | NotGiven = NOT_GIVEN,
        status: Literal["PENDING_EXEC", "PENDING_UPLOAD", "SUCCESS", "FAILED"] | NotGiven = NOT_GIVEN,
        to: Union[str, datetime] | NotGiven = NOT_GIVEN,
        user_email: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncV4PagePagination[Optional[CommandListResponse]]:
        """
        Retrieves a paginated list of commands issued to devices under the specified
        account, optionally filtered by time range, device, or other parameters

        Args:
          page: Page number for pagination

          per_page: Number of results per page

          command_type: Optionally filter executed commands by command type

          device_id: Unique identifier for a device

          from_: Start time for the query in ISO (RFC3339 - ISO 8601) format

          status: Optionally filter executed commands by status

          to: End time for the query in ISO (RFC3339 - ISO 8601) format

          user_email: Email tied to the device

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/dex/commands",
            page=SyncV4PagePagination[Optional[CommandListResponse]],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page": page,
                        "per_page": per_page,
                        "command_type": command_type,
                        "device_id": device_id,
                        "from_": from_,
                        "status": status,
                        "to": to,
                        "user_email": user_email,
                    },
                    command_list_params.CommandListParams,
                ),
            ),
            model=CommandListResponse,
        )


class AsyncCommandsResource(AsyncAPIResource):
    @cached_property
    def devices(self) -> AsyncDevicesResource:
        return AsyncDevicesResource(self._client)

    @cached_property
    def downloads(self) -> AsyncDownloadsResource:
        return AsyncDownloadsResource(self._client)

    @cached_property
    def quota(self) -> AsyncQuotaResource:
        return AsyncQuotaResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncCommandsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCommandsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCommandsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncCommandsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_id: str,
        commands: Iterable[command_create_params.Command],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[CommandCreateResponse]:
        """
        Initiate commands for up to 10 devices per account

        Args:
          commands: List of device-level commands to execute

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._post(
            f"/accounts/{account_id}/dex/commands",
            body=await async_maybe_transform({"commands": commands}, command_create_params.CommandCreateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[CommandCreateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[CommandCreateResponse]], ResultWrapper[CommandCreateResponse]),
        )

    def list(
        self,
        *,
        account_id: str,
        page: float,
        per_page: float,
        command_type: str | NotGiven = NOT_GIVEN,
        device_id: str | NotGiven = NOT_GIVEN,
        from_: Union[str, datetime] | NotGiven = NOT_GIVEN,
        status: Literal["PENDING_EXEC", "PENDING_UPLOAD", "SUCCESS", "FAILED"] | NotGiven = NOT_GIVEN,
        to: Union[str, datetime] | NotGiven = NOT_GIVEN,
        user_email: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[Optional[CommandListResponse], AsyncV4PagePagination[Optional[CommandListResponse]]]:
        """
        Retrieves a paginated list of commands issued to devices under the specified
        account, optionally filtered by time range, device, or other parameters

        Args:
          page: Page number for pagination

          per_page: Number of results per page

          command_type: Optionally filter executed commands by command type

          device_id: Unique identifier for a device

          from_: Start time for the query in ISO (RFC3339 - ISO 8601) format

          status: Optionally filter executed commands by status

          to: End time for the query in ISO (RFC3339 - ISO 8601) format

          user_email: Email tied to the device

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/dex/commands",
            page=AsyncV4PagePagination[Optional[CommandListResponse]],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page": page,
                        "per_page": per_page,
                        "command_type": command_type,
                        "device_id": device_id,
                        "from_": from_,
                        "status": status,
                        "to": to,
                        "user_email": user_email,
                    },
                    command_list_params.CommandListParams,
                ),
            ),
            model=CommandListResponse,
        )


class CommandsResourceWithRawResponse:
    def __init__(self, commands: CommandsResource) -> None:
        self._commands = commands

        self.create = to_raw_response_wrapper(
            commands.create,
        )
        self.list = to_raw_response_wrapper(
            commands.list,
        )

    @cached_property
    def devices(self) -> DevicesResourceWithRawResponse:
        return DevicesResourceWithRawResponse(self._commands.devices)

    @cached_property
    def downloads(self) -> DownloadsResourceWithRawResponse:
        return DownloadsResourceWithRawResponse(self._commands.downloads)

    @cached_property
    def quota(self) -> QuotaResourceWithRawResponse:
        return QuotaResourceWithRawResponse(self._commands.quota)


class AsyncCommandsResourceWithRawResponse:
    def __init__(self, commands: AsyncCommandsResource) -> None:
        self._commands = commands

        self.create = async_to_raw_response_wrapper(
            commands.create,
        )
        self.list = async_to_raw_response_wrapper(
            commands.list,
        )

    @cached_property
    def devices(self) -> AsyncDevicesResourceWithRawResponse:
        return AsyncDevicesResourceWithRawResponse(self._commands.devices)

    @cached_property
    def downloads(self) -> AsyncDownloadsResourceWithRawResponse:
        return AsyncDownloadsResourceWithRawResponse(self._commands.downloads)

    @cached_property
    def quota(self) -> AsyncQuotaResourceWithRawResponse:
        return AsyncQuotaResourceWithRawResponse(self._commands.quota)


class CommandsResourceWithStreamingResponse:
    def __init__(self, commands: CommandsResource) -> None:
        self._commands = commands

        self.create = to_streamed_response_wrapper(
            commands.create,
        )
        self.list = to_streamed_response_wrapper(
            commands.list,
        )

    @cached_property
    def devices(self) -> DevicesResourceWithStreamingResponse:
        return DevicesResourceWithStreamingResponse(self._commands.devices)

    @cached_property
    def downloads(self) -> DownloadsResourceWithStreamingResponse:
        return DownloadsResourceWithStreamingResponse(self._commands.downloads)

    @cached_property
    def quota(self) -> QuotaResourceWithStreamingResponse:
        return QuotaResourceWithStreamingResponse(self._commands.quota)


class AsyncCommandsResourceWithStreamingResponse:
    def __init__(self, commands: AsyncCommandsResource) -> None:
        self._commands = commands

        self.create = async_to_streamed_response_wrapper(
            commands.create,
        )
        self.list = async_to_streamed_response_wrapper(
            commands.list,
        )

    @cached_property
    def devices(self) -> AsyncDevicesResourceWithStreamingResponse:
        return AsyncDevicesResourceWithStreamingResponse(self._commands.devices)

    @cached_property
    def downloads(self) -> AsyncDownloadsResourceWithStreamingResponse:
        return AsyncDownloadsResourceWithStreamingResponse(self._commands.downloads)

    @cached_property
    def quota(self) -> AsyncQuotaResourceWithStreamingResponse:
        return AsyncQuotaResourceWithStreamingResponse(self._commands.quota)
