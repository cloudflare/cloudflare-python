# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Iterable, cast
from typing_extensions import Literal

import httpx

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
from ....._base_client import (
    make_request_options,
)
from .....types.workers.services.environments import SettingGetResponse, SettingEditResponse, setting_edit_params

__all__ = ["Settings", "AsyncSettings"]


class Settings(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SettingsWithRawResponse:
        return SettingsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SettingsWithStreamingResponse:
        return SettingsWithStreamingResponse(self)

    def edit(
        self,
        environment_name: str,
        *,
        account_id: str,
        service_name: str,
        errors: Iterable[setting_edit_params.Error],
        messages: Iterable[setting_edit_params.Message],
        result: setting_edit_params.Result,
        success: Literal[True],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SettingEditResponse:
        """
        Patch script metadata, such as bindings

        Args:
          account_id: Identifier

          service_name: Name of Worker to bind to

          environment_name: Optional environment if the Worker utilizes one.

          success: Whether the API call was successful

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not service_name:
            raise ValueError(f"Expected a non-empty value for `service_name` but received {service_name!r}")
        if not environment_name:
            raise ValueError(f"Expected a non-empty value for `environment_name` but received {environment_name!r}")
        return self._patch(
            f"/accounts/{account_id}/workers/services/{service_name}/environments/{environment_name}/settings",
            body=maybe_transform(
                {
                    "errors": errors,
                    "messages": messages,
                    "result": result,
                    "success": success,
                },
                setting_edit_params.SettingEditParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[SettingEditResponse], ResultWrapper[SettingEditResponse]),
        )

    def get(
        self,
        environment_name: str,
        *,
        account_id: str,
        service_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SettingGetResponse:
        """
        Get script settings from a worker with an environment

        Args:
          account_id: Identifier

          service_name: Name of Worker to bind to

          environment_name: Optional environment if the Worker utilizes one.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not service_name:
            raise ValueError(f"Expected a non-empty value for `service_name` but received {service_name!r}")
        if not environment_name:
            raise ValueError(f"Expected a non-empty value for `environment_name` but received {environment_name!r}")
        return self._get(
            f"/accounts/{account_id}/workers/services/{service_name}/environments/{environment_name}/settings",
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

    async def edit(
        self,
        environment_name: str,
        *,
        account_id: str,
        service_name: str,
        errors: Iterable[setting_edit_params.Error],
        messages: Iterable[setting_edit_params.Message],
        result: setting_edit_params.Result,
        success: Literal[True],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SettingEditResponse:
        """
        Patch script metadata, such as bindings

        Args:
          account_id: Identifier

          service_name: Name of Worker to bind to

          environment_name: Optional environment if the Worker utilizes one.

          success: Whether the API call was successful

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not service_name:
            raise ValueError(f"Expected a non-empty value for `service_name` but received {service_name!r}")
        if not environment_name:
            raise ValueError(f"Expected a non-empty value for `environment_name` but received {environment_name!r}")
        return await self._patch(
            f"/accounts/{account_id}/workers/services/{service_name}/environments/{environment_name}/settings",
            body=await async_maybe_transform(
                {
                    "errors": errors,
                    "messages": messages,
                    "result": result,
                    "success": success,
                },
                setting_edit_params.SettingEditParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[SettingEditResponse], ResultWrapper[SettingEditResponse]),
        )

    async def get(
        self,
        environment_name: str,
        *,
        account_id: str,
        service_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SettingGetResponse:
        """
        Get script settings from a worker with an environment

        Args:
          account_id: Identifier

          service_name: Name of Worker to bind to

          environment_name: Optional environment if the Worker utilizes one.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not service_name:
            raise ValueError(f"Expected a non-empty value for `service_name` but received {service_name!r}")
        if not environment_name:
            raise ValueError(f"Expected a non-empty value for `environment_name` but received {environment_name!r}")
        return await self._get(
            f"/accounts/{account_id}/workers/services/{service_name}/environments/{environment_name}/settings",
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

        self.edit = to_raw_response_wrapper(
            settings.edit,
        )
        self.get = to_raw_response_wrapper(
            settings.get,
        )


class AsyncSettingsWithRawResponse:
    def __init__(self, settings: AsyncSettings) -> None:
        self._settings = settings

        self.edit = async_to_raw_response_wrapper(
            settings.edit,
        )
        self.get = async_to_raw_response_wrapper(
            settings.get,
        )


class SettingsWithStreamingResponse:
    def __init__(self, settings: Settings) -> None:
        self._settings = settings

        self.edit = to_streamed_response_wrapper(
            settings.edit,
        )
        self.get = to_streamed_response_wrapper(
            settings.get,
        )


class AsyncSettingsWithStreamingResponse:
    def __init__(self, settings: AsyncSettings) -> None:
        self._settings = settings

        self.edit = async_to_streamed_response_wrapper(
            settings.edit,
        )
        self.get = async_to_streamed_response_wrapper(
            settings.get,
        )
