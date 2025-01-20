# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Iterable, Optional, cast

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._wrappers import ResultWrapper
from ...._base_client import make_request_options
from ....types.workers.scripts import setting_edit_params
from ....types.workers.script_setting import ScriptSetting
from ....types.workers.scripts.consumer_script_param import ConsumerScriptParam

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

    def edit(
        self,
        script_name: str,
        *,
        account_id: str,
        logpush: bool | NotGiven = NOT_GIVEN,
        observability: setting_edit_params.Observability | NotGiven = NOT_GIVEN,
        tail_consumers: Iterable[ConsumerScriptParam] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ScriptSetting]:
        """
        Patch script-level settings when using
        [Worker Versions](https://developers.cloudflare.com/api/operations/worker-versions-list-versions).
        Including but not limited to Logpush and Tail Consumers.

        Args:
          account_id: Identifier

          script_name: Name of the script, used in URLs and route configuration.

          logpush: Whether Logpush is turned on for the Worker.

          observability: Observability settings for the Worker.

          tail_consumers: List of Workers that will consume logs from the attached Worker.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not script_name:
            raise ValueError(f"Expected a non-empty value for `script_name` but received {script_name!r}")
        return self._patch(
            f"/accounts/{account_id}/workers/scripts/{script_name}/script-settings",
            body=maybe_transform(
                {
                    "logpush": logpush,
                    "observability": observability,
                    "tail_consumers": tail_consumers,
                },
                setting_edit_params.SettingEditParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[ScriptSetting]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[ScriptSetting]], ResultWrapper[ScriptSetting]),
        )

    def get(
        self,
        script_name: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ScriptSetting]:
        """
        Get script-level settings when using
        [Worker Versions](https://developers.cloudflare.com/api/operations/worker-versions-list-versions).
        Includes Logpush and Tail Consumers.

        Args:
          account_id: Identifier

          script_name: Name of the script, used in URLs and route configuration.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not script_name:
            raise ValueError(f"Expected a non-empty value for `script_name` but received {script_name!r}")
        return self._get(
            f"/accounts/{account_id}/workers/scripts/{script_name}/script-settings",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[ScriptSetting]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[ScriptSetting]], ResultWrapper[ScriptSetting]),
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

    async def edit(
        self,
        script_name: str,
        *,
        account_id: str,
        logpush: bool | NotGiven = NOT_GIVEN,
        observability: setting_edit_params.Observability | NotGiven = NOT_GIVEN,
        tail_consumers: Iterable[ConsumerScriptParam] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ScriptSetting]:
        """
        Patch script-level settings when using
        [Worker Versions](https://developers.cloudflare.com/api/operations/worker-versions-list-versions).
        Including but not limited to Logpush and Tail Consumers.

        Args:
          account_id: Identifier

          script_name: Name of the script, used in URLs and route configuration.

          logpush: Whether Logpush is turned on for the Worker.

          observability: Observability settings for the Worker.

          tail_consumers: List of Workers that will consume logs from the attached Worker.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not script_name:
            raise ValueError(f"Expected a non-empty value for `script_name` but received {script_name!r}")
        return await self._patch(
            f"/accounts/{account_id}/workers/scripts/{script_name}/script-settings",
            body=await async_maybe_transform(
                {
                    "logpush": logpush,
                    "observability": observability,
                    "tail_consumers": tail_consumers,
                },
                setting_edit_params.SettingEditParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[ScriptSetting]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[ScriptSetting]], ResultWrapper[ScriptSetting]),
        )

    async def get(
        self,
        script_name: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ScriptSetting]:
        """
        Get script-level settings when using
        [Worker Versions](https://developers.cloudflare.com/api/operations/worker-versions-list-versions).
        Includes Logpush and Tail Consumers.

        Args:
          account_id: Identifier

          script_name: Name of the script, used in URLs and route configuration.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not script_name:
            raise ValueError(f"Expected a non-empty value for `script_name` but received {script_name!r}")
        return await self._get(
            f"/accounts/{account_id}/workers/scripts/{script_name}/script-settings",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[ScriptSetting]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[ScriptSetting]], ResultWrapper[ScriptSetting]),
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
