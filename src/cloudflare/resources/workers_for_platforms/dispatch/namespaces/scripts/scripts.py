# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Type, cast, overload

import httpx

from .content import (
    Content,
    AsyncContent,
    ContentWithRawResponse,
    AsyncContentWithRawResponse,
    ContentWithStreamingResponse,
    AsyncContentWithStreamingResponse,
)
from .bindings import (
    Bindings,
    AsyncBindings,
    BindingsWithRawResponse,
    AsyncBindingsWithRawResponse,
    BindingsWithStreamingResponse,
    AsyncBindingsWithStreamingResponse,
)
from .settings import (
    Settings,
    AsyncSettings,
    SettingsWithRawResponse,
    AsyncSettingsWithRawResponse,
    SettingsWithStreamingResponse,
    AsyncSettingsWithStreamingResponse,
)
from ......_types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven, FileTypes
from ......_utils import (
    required_args,
    maybe_transform,
    async_maybe_transform,
)
from ......_compat import cached_property
from ......_resource import SyncAPIResource, AsyncAPIResource
from ......_response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ......_wrappers import ResultWrapper
from ......_base_client import (
    make_request_options,
)
from ......types.workers import WorkersScript
from ......types.workers_for_platforms.dispatch.namespaces import (
    WorkersNamespaceScript,
    script_delete_params,
    script_update_params,
)

__all__ = ["Scripts", "AsyncScripts"]


class Scripts(SyncAPIResource):
    @cached_property
    def content(self) -> Content:
        return Content(self._client)

    @cached_property
    def settings(self) -> Settings:
        return Settings(self._client)

    @cached_property
    def bindings(self) -> Bindings:
        return Bindings(self._client)

    @cached_property
    def with_raw_response(self) -> ScriptsWithRawResponse:
        return ScriptsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ScriptsWithStreamingResponse:
        return ScriptsWithStreamingResponse(self)

    @overload
    def update(
        self,
        script_name: str,
        *,
        account_id: str,
        dispatch_namespace: str,
        any_part_name: List[FileTypes] | NotGiven = NOT_GIVEN,
        metadata: script_update_params.Variant0Metadata | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WorkersScript:
        """
        Upload a worker module to a Workers for Platforms namespace.

        Args:
          account_id: Identifier

          dispatch_namespace: Name of the Workers for Platforms dispatch namespace.

          script_name: Name of the script, used in URLs and route configuration.

          any_part_name: A module comprising a Worker script, often a javascript file. Multiple modules
              may be provided as separate named parts, but at least one module must be present
              and referenced in the metadata as `main_module` or `body_part` by part name.

          metadata: JSON encoded metadata about the uploaded parts and Worker configuration.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def update(
        self,
        script_name: str,
        *,
        account_id: str,
        dispatch_namespace: str,
        message: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WorkersScript:
        """
        Upload a worker module to a Workers for Platforms namespace.

        Args:
          account_id: Identifier

          dispatch_namespace: Name of the Workers for Platforms dispatch namespace.

          script_name: Name of the script, used in URLs and route configuration.

          message: Rollback message to be associated with this deployment. Only parsed when query
              param `"rollback_to"` is present.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["account_id", "dispatch_namespace"], ["account_id", "dispatch_namespace"])
    def update(
        self,
        script_name: str,
        *,
        account_id: str,
        dispatch_namespace: str,
        any_part_name: List[FileTypes] | NotGiven = NOT_GIVEN,
        metadata: script_update_params.Variant0Metadata | NotGiven = NOT_GIVEN,
        message: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WorkersScript:
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not dispatch_namespace:
            raise ValueError(f"Expected a non-empty value for `dispatch_namespace` but received {dispatch_namespace!r}")
        if not script_name:
            raise ValueError(f"Expected a non-empty value for `script_name` but received {script_name!r}")
        return self._put(
            f"/accounts/{account_id}/workers/dispatch/namespaces/{dispatch_namespace}/scripts/{script_name}",
            body=maybe_transform(
                {
                    "any_part_name": any_part_name,
                    "metadata": metadata,
                    "message": message,
                },
                script_update_params.ScriptUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[WorkersScript], ResultWrapper[WorkersScript]),
        )

    def delete(
        self,
        script_name: str,
        *,
        account_id: str,
        dispatch_namespace: str,
        force: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Delete a worker from a Workers for Platforms namespace.

        This call has no
        response body on a successful delete.

        Args:
          account_id: Identifier

          dispatch_namespace: Name of the Workers for Platforms dispatch namespace.

          script_name: Name of the script, used in URLs and route configuration.

          force: If set to true, delete will not be stopped by associated service binding,
              durable object, or other binding. Any of these associated bindings/durable
              objects will be deleted along with the script.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not dispatch_namespace:
            raise ValueError(f"Expected a non-empty value for `dispatch_namespace` but received {dispatch_namespace!r}")
        if not script_name:
            raise ValueError(f"Expected a non-empty value for `script_name` but received {script_name!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/accounts/{account_id}/workers/dispatch/namespaces/{dispatch_namespace}/scripts/{script_name}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"force": force}, script_delete_params.ScriptDeleteParams),
            ),
            cast_to=NoneType,
        )

    def get(
        self,
        script_name: str,
        *,
        account_id: str,
        dispatch_namespace: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WorkersNamespaceScript:
        """
        Fetch information about a script uploaded to a Workers for Platforms namespace.

        Args:
          account_id: Identifier

          dispatch_namespace: Name of the Workers for Platforms dispatch namespace.

          script_name: Name of the script, used in URLs and route configuration.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not dispatch_namespace:
            raise ValueError(f"Expected a non-empty value for `dispatch_namespace` but received {dispatch_namespace!r}")
        if not script_name:
            raise ValueError(f"Expected a non-empty value for `script_name` but received {script_name!r}")
        return self._get(
            f"/accounts/{account_id}/workers/dispatch/namespaces/{dispatch_namespace}/scripts/{script_name}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[WorkersNamespaceScript], ResultWrapper[WorkersNamespaceScript]),
        )


class AsyncScripts(AsyncAPIResource):
    @cached_property
    def content(self) -> AsyncContent:
        return AsyncContent(self._client)

    @cached_property
    def settings(self) -> AsyncSettings:
        return AsyncSettings(self._client)

    @cached_property
    def bindings(self) -> AsyncBindings:
        return AsyncBindings(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncScriptsWithRawResponse:
        return AsyncScriptsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncScriptsWithStreamingResponse:
        return AsyncScriptsWithStreamingResponse(self)

    @overload
    async def update(
        self,
        script_name: str,
        *,
        account_id: str,
        dispatch_namespace: str,
        any_part_name: List[FileTypes] | NotGiven = NOT_GIVEN,
        metadata: script_update_params.Variant0Metadata | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WorkersScript:
        """
        Upload a worker module to a Workers for Platforms namespace.

        Args:
          account_id: Identifier

          dispatch_namespace: Name of the Workers for Platforms dispatch namespace.

          script_name: Name of the script, used in URLs and route configuration.

          any_part_name: A module comprising a Worker script, often a javascript file. Multiple modules
              may be provided as separate named parts, but at least one module must be present
              and referenced in the metadata as `main_module` or `body_part` by part name.

          metadata: JSON encoded metadata about the uploaded parts and Worker configuration.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def update(
        self,
        script_name: str,
        *,
        account_id: str,
        dispatch_namespace: str,
        message: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WorkersScript:
        """
        Upload a worker module to a Workers for Platforms namespace.

        Args:
          account_id: Identifier

          dispatch_namespace: Name of the Workers for Platforms dispatch namespace.

          script_name: Name of the script, used in URLs and route configuration.

          message: Rollback message to be associated with this deployment. Only parsed when query
              param `"rollback_to"` is present.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["account_id", "dispatch_namespace"], ["account_id", "dispatch_namespace"])
    async def update(
        self,
        script_name: str,
        *,
        account_id: str,
        dispatch_namespace: str,
        any_part_name: List[FileTypes] | NotGiven = NOT_GIVEN,
        metadata: script_update_params.Variant0Metadata | NotGiven = NOT_GIVEN,
        message: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WorkersScript:
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not dispatch_namespace:
            raise ValueError(f"Expected a non-empty value for `dispatch_namespace` but received {dispatch_namespace!r}")
        if not script_name:
            raise ValueError(f"Expected a non-empty value for `script_name` but received {script_name!r}")
        return await self._put(
            f"/accounts/{account_id}/workers/dispatch/namespaces/{dispatch_namespace}/scripts/{script_name}",
            body=await async_maybe_transform(
                {
                    "any_part_name": any_part_name,
                    "metadata": metadata,
                    "message": message,
                },
                script_update_params.ScriptUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[WorkersScript], ResultWrapper[WorkersScript]),
        )

    async def delete(
        self,
        script_name: str,
        *,
        account_id: str,
        dispatch_namespace: str,
        force: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Delete a worker from a Workers for Platforms namespace.

        This call has no
        response body on a successful delete.

        Args:
          account_id: Identifier

          dispatch_namespace: Name of the Workers for Platforms dispatch namespace.

          script_name: Name of the script, used in URLs and route configuration.

          force: If set to true, delete will not be stopped by associated service binding,
              durable object, or other binding. Any of these associated bindings/durable
              objects will be deleted along with the script.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not dispatch_namespace:
            raise ValueError(f"Expected a non-empty value for `dispatch_namespace` but received {dispatch_namespace!r}")
        if not script_name:
            raise ValueError(f"Expected a non-empty value for `script_name` but received {script_name!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/accounts/{account_id}/workers/dispatch/namespaces/{dispatch_namespace}/scripts/{script_name}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"force": force}, script_delete_params.ScriptDeleteParams),
            ),
            cast_to=NoneType,
        )

    async def get(
        self,
        script_name: str,
        *,
        account_id: str,
        dispatch_namespace: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WorkersNamespaceScript:
        """
        Fetch information about a script uploaded to a Workers for Platforms namespace.

        Args:
          account_id: Identifier

          dispatch_namespace: Name of the Workers for Platforms dispatch namespace.

          script_name: Name of the script, used in URLs and route configuration.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not dispatch_namespace:
            raise ValueError(f"Expected a non-empty value for `dispatch_namespace` but received {dispatch_namespace!r}")
        if not script_name:
            raise ValueError(f"Expected a non-empty value for `script_name` but received {script_name!r}")
        return await self._get(
            f"/accounts/{account_id}/workers/dispatch/namespaces/{dispatch_namespace}/scripts/{script_name}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[WorkersNamespaceScript], ResultWrapper[WorkersNamespaceScript]),
        )


class ScriptsWithRawResponse:
    def __init__(self, scripts: Scripts) -> None:
        self._scripts = scripts

        self.update = to_raw_response_wrapper(
            scripts.update,
        )
        self.delete = to_raw_response_wrapper(
            scripts.delete,
        )
        self.get = to_raw_response_wrapper(
            scripts.get,
        )

    @cached_property
    def content(self) -> ContentWithRawResponse:
        return ContentWithRawResponse(self._scripts.content)

    @cached_property
    def settings(self) -> SettingsWithRawResponse:
        return SettingsWithRawResponse(self._scripts.settings)

    @cached_property
    def bindings(self) -> BindingsWithRawResponse:
        return BindingsWithRawResponse(self._scripts.bindings)


class AsyncScriptsWithRawResponse:
    def __init__(self, scripts: AsyncScripts) -> None:
        self._scripts = scripts

        self.update = async_to_raw_response_wrapper(
            scripts.update,
        )
        self.delete = async_to_raw_response_wrapper(
            scripts.delete,
        )
        self.get = async_to_raw_response_wrapper(
            scripts.get,
        )

    @cached_property
    def content(self) -> AsyncContentWithRawResponse:
        return AsyncContentWithRawResponse(self._scripts.content)

    @cached_property
    def settings(self) -> AsyncSettingsWithRawResponse:
        return AsyncSettingsWithRawResponse(self._scripts.settings)

    @cached_property
    def bindings(self) -> AsyncBindingsWithRawResponse:
        return AsyncBindingsWithRawResponse(self._scripts.bindings)


class ScriptsWithStreamingResponse:
    def __init__(self, scripts: Scripts) -> None:
        self._scripts = scripts

        self.update = to_streamed_response_wrapper(
            scripts.update,
        )
        self.delete = to_streamed_response_wrapper(
            scripts.delete,
        )
        self.get = to_streamed_response_wrapper(
            scripts.get,
        )

    @cached_property
    def content(self) -> ContentWithStreamingResponse:
        return ContentWithStreamingResponse(self._scripts.content)

    @cached_property
    def settings(self) -> SettingsWithStreamingResponse:
        return SettingsWithStreamingResponse(self._scripts.settings)

    @cached_property
    def bindings(self) -> BindingsWithStreamingResponse:
        return BindingsWithStreamingResponse(self._scripts.bindings)


class AsyncScriptsWithStreamingResponse:
    def __init__(self, scripts: AsyncScripts) -> None:
        self._scripts = scripts

        self.update = async_to_streamed_response_wrapper(
            scripts.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            scripts.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            scripts.get,
        )

    @cached_property
    def content(self) -> AsyncContentWithStreamingResponse:
        return AsyncContentWithStreamingResponse(self._scripts.content)

    @cached_property
    def settings(self) -> AsyncSettingsWithStreamingResponse:
        return AsyncSettingsWithStreamingResponse(self._scripts.settings)

    @cached_property
    def bindings(self) -> AsyncBindingsWithStreamingResponse:
        return AsyncBindingsWithStreamingResponse(self._scripts.bindings)
