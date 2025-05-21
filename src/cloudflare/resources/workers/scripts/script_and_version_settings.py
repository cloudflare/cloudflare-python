# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, cast

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import maybe_transform, async_maybe_transform
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
from ....types.workers.scripts import script_and_version_setting_edit_params
from ....types.workers.scripts.script_and_version_setting_get_response import ScriptAndVersionSettingGetResponse
from ....types.workers.scripts.script_and_version_setting_edit_response import ScriptAndVersionSettingEditResponse

__all__ = ["ScriptAndVersionSettingsResource", "AsyncScriptAndVersionSettingsResource"]


class ScriptAndVersionSettingsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ScriptAndVersionSettingsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return ScriptAndVersionSettingsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ScriptAndVersionSettingsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return ScriptAndVersionSettingsResourceWithStreamingResponse(self)

    def edit(
        self,
        script_name: str,
        *,
        account_id: str,
        settings: script_and_version_setting_edit_params.Settings | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ScriptAndVersionSettingEditResponse:
        """
        Patch metadata or config, such as bindings or usage model.

        Args:
          account_id: Identifier.

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
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return self._patch(
            f"/accounts/{account_id}/workers/scripts/{script_name}/settings",
            body=maybe_transform(
                {"settings": settings}, script_and_version_setting_edit_params.ScriptAndVersionSettingEditParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[ScriptAndVersionSettingEditResponse]._unwrapper,
            ),
            cast_to=cast(Type[ScriptAndVersionSettingEditResponse], ResultWrapper[ScriptAndVersionSettingEditResponse]),
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
    ) -> ScriptAndVersionSettingGetResponse:
        """
        Get metadata and config, such as bindings or usage model.

        Args:
          account_id: Identifier.

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
            f"/accounts/{account_id}/workers/scripts/{script_name}/settings",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[ScriptAndVersionSettingGetResponse]._unwrapper,
            ),
            cast_to=cast(Type[ScriptAndVersionSettingGetResponse], ResultWrapper[ScriptAndVersionSettingGetResponse]),
        )


class AsyncScriptAndVersionSettingsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncScriptAndVersionSettingsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncScriptAndVersionSettingsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncScriptAndVersionSettingsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncScriptAndVersionSettingsResourceWithStreamingResponse(self)

    async def edit(
        self,
        script_name: str,
        *,
        account_id: str,
        settings: script_and_version_setting_edit_params.Settings | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ScriptAndVersionSettingEditResponse:
        """
        Patch metadata or config, such as bindings or usage model.

        Args:
          account_id: Identifier.

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
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return await self._patch(
            f"/accounts/{account_id}/workers/scripts/{script_name}/settings",
            body=await async_maybe_transform(
                {"settings": settings}, script_and_version_setting_edit_params.ScriptAndVersionSettingEditParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[ScriptAndVersionSettingEditResponse]._unwrapper,
            ),
            cast_to=cast(Type[ScriptAndVersionSettingEditResponse], ResultWrapper[ScriptAndVersionSettingEditResponse]),
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
    ) -> ScriptAndVersionSettingGetResponse:
        """
        Get metadata and config, such as bindings or usage model.

        Args:
          account_id: Identifier.

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
            f"/accounts/{account_id}/workers/scripts/{script_name}/settings",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[ScriptAndVersionSettingGetResponse]._unwrapper,
            ),
            cast_to=cast(Type[ScriptAndVersionSettingGetResponse], ResultWrapper[ScriptAndVersionSettingGetResponse]),
        )


class ScriptAndVersionSettingsResourceWithRawResponse:
    def __init__(self, script_and_version_settings: ScriptAndVersionSettingsResource) -> None:
        self._script_and_version_settings = script_and_version_settings

        self.edit = to_raw_response_wrapper(
            script_and_version_settings.edit,
        )
        self.get = to_raw_response_wrapper(
            script_and_version_settings.get,
        )


class AsyncScriptAndVersionSettingsResourceWithRawResponse:
    def __init__(self, script_and_version_settings: AsyncScriptAndVersionSettingsResource) -> None:
        self._script_and_version_settings = script_and_version_settings

        self.edit = async_to_raw_response_wrapper(
            script_and_version_settings.edit,
        )
        self.get = async_to_raw_response_wrapper(
            script_and_version_settings.get,
        )


class ScriptAndVersionSettingsResourceWithStreamingResponse:
    def __init__(self, script_and_version_settings: ScriptAndVersionSettingsResource) -> None:
        self._script_and_version_settings = script_and_version_settings

        self.edit = to_streamed_response_wrapper(
            script_and_version_settings.edit,
        )
        self.get = to_streamed_response_wrapper(
            script_and_version_settings.get,
        )


class AsyncScriptAndVersionSettingsResourceWithStreamingResponse:
    def __init__(self, script_and_version_settings: AsyncScriptAndVersionSettingsResource) -> None:
        self._script_and_version_settings = script_and_version_settings

        self.edit = async_to_streamed_response_wrapper(
            script_and_version_settings.edit,
        )
        self.get = async_to_streamed_response_wrapper(
            script_and_version_settings.get,
        )
