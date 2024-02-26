# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List, Type, cast

import httpx

from .tail import (
    Tail,
    AsyncTail,
    TailWithRawResponse,
    AsyncTailWithRawResponse,
    TailWithStreamingResponse,
    AsyncTailWithStreamingResponse,
)
from .bindings import (
    Bindings,
    AsyncBindings,
    BindingsWithRawResponse,
    AsyncBindingsWithRawResponse,
    BindingsWithStreamingResponse,
    AsyncBindingsWithStreamingResponse,
)
from ...._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven, FileTypes
from ...._utils import maybe_transform
from .schedules import (
    Schedules,
    AsyncSchedules,
    SchedulesWithRawResponse,
    AsyncSchedulesWithRawResponse,
    SchedulesWithStreamingResponse,
    AsyncSchedulesWithStreamingResponse,
)
from ...._compat import cached_property
from .usage_model import (
    UsageModel,
    AsyncUsageModel,
    UsageModelWithRawResponse,
    AsyncUsageModelWithRawResponse,
    UsageModelWithStreamingResponse,
    AsyncUsageModelWithStreamingResponse,
)
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    to_custom_raw_response_wrapper,
    async_to_streamed_response_wrapper,
    to_custom_streamed_response_wrapper,
    async_to_custom_raw_response_wrapper,
    async_to_custom_streamed_response_wrapper,
)
from ...._wrappers import ResultWrapper
from ...._base_client import (
    make_request_options,
)
from ....types.workers import ScriptListResponse, ScriptUpdateResponse, script_delete_params, script_update_params

__all__ = ["Scripts", "AsyncScripts"]


class Scripts(SyncAPIResource):
    @cached_property
    def bindings(self) -> Bindings:
        return Bindings(self._client)

    @cached_property
    def schedules(self) -> Schedules:
        return Schedules(self._client)

    @cached_property
    def tail(self) -> Tail:
        return Tail(self._client)

    @cached_property
    def usage_model(self) -> UsageModel:
        return UsageModel(self._client)

    @cached_property
    def with_raw_response(self) -> ScriptsWithRawResponse:
        return ScriptsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ScriptsWithStreamingResponse:
        return ScriptsWithStreamingResponse(self)

    def update(
        self,
        script_name: str,
        *,
        account_id: str,
        rollback_to: str | NotGiven = NOT_GIVEN,
        any_part_name: List[FileTypes] | NotGiven = NOT_GIVEN,
        message: str | NotGiven = NOT_GIVEN,
        metadata: script_update_params.Metadata | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ScriptUpdateResponse:
        """
        Upload a worker module.

        Args:
          account_id: Identifier

          script_name: Name of the script, used in URLs and route configuration.

          rollback_to: Rollback to provided deployment based on deployment ID. Request body will only
              parse a "message" part. You can learn more about deployments
              [here](https://developers.cloudflare.com/workers/platform/deployments/).

          any_part_name: A module comprising a Worker script, often a javascript file. Multiple modules
              may be provided as separate named parts, but at least one module must be present
              and referenced in the metadata as `main_module` or `body_part` by part name.

          message: Rollback message to be associated with this deployment. Only parsed when query
              param `"rollback_to"` is present.

          metadata: JSON encoded metadata about the uploaded parts and Worker configuration.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not script_name:
            raise ValueError(f"Expected a non-empty value for `script_name` but received {script_name!r}")
        return self._put(
            f"/accounts/{account_id}/workers/scripts/{script_name}",
            body=maybe_transform(
                {
                    "any_part_name": any_part_name,
                    "message": message,
                    "metadata": metadata,
                },
                script_update_params.ScriptUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"rollback_to": rollback_to}, script_update_params.ScriptUpdateParams),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[ScriptUpdateResponse], ResultWrapper[ScriptUpdateResponse]),
        )

    def list(
        self,
        account_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ScriptListResponse:
        """
        Fetch a list of uploaded workers.

        Args:
          account_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get(
            f"/accounts/{account_id}/workers/scripts",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[ScriptListResponse], ResultWrapper[ScriptListResponse]),
        )

    def delete(
        self,
        script_name: str,
        *,
        account_id: str,
        force: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Delete your worker.

        This call has no response body on a successful delete.

        Args:
          account_id: Identifier

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
        if not script_name:
            raise ValueError(f"Expected a non-empty value for `script_name` but received {script_name!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/accounts/{account_id}/workers/scripts/{script_name}",
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
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BinaryAPIResponse:
        """Fetch raw script content for your worker.

        Note this is the original script
        content, not JSON encoded.

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
        extra_headers = {"Accept": "undefined", **(extra_headers or {})}
        return self._get(
            f"/accounts/{account_id}/workers/scripts/{script_name}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BinaryAPIResponse,
        )


class AsyncScripts(AsyncAPIResource):
    @cached_property
    def bindings(self) -> AsyncBindings:
        return AsyncBindings(self._client)

    @cached_property
    def schedules(self) -> AsyncSchedules:
        return AsyncSchedules(self._client)

    @cached_property
    def tail(self) -> AsyncTail:
        return AsyncTail(self._client)

    @cached_property
    def usage_model(self) -> AsyncUsageModel:
        return AsyncUsageModel(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncScriptsWithRawResponse:
        return AsyncScriptsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncScriptsWithStreamingResponse:
        return AsyncScriptsWithStreamingResponse(self)

    async def update(
        self,
        script_name: str,
        *,
        account_id: str,
        rollback_to: str | NotGiven = NOT_GIVEN,
        any_part_name: List[FileTypes] | NotGiven = NOT_GIVEN,
        message: str | NotGiven = NOT_GIVEN,
        metadata: script_update_params.Metadata | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ScriptUpdateResponse:
        """
        Upload a worker module.

        Args:
          account_id: Identifier

          script_name: Name of the script, used in URLs and route configuration.

          rollback_to: Rollback to provided deployment based on deployment ID. Request body will only
              parse a "message" part. You can learn more about deployments
              [here](https://developers.cloudflare.com/workers/platform/deployments/).

          any_part_name: A module comprising a Worker script, often a javascript file. Multiple modules
              may be provided as separate named parts, but at least one module must be present
              and referenced in the metadata as `main_module` or `body_part` by part name.

          message: Rollback message to be associated with this deployment. Only parsed when query
              param `"rollback_to"` is present.

          metadata: JSON encoded metadata about the uploaded parts and Worker configuration.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not script_name:
            raise ValueError(f"Expected a non-empty value for `script_name` but received {script_name!r}")
        return await self._put(
            f"/accounts/{account_id}/workers/scripts/{script_name}",
            body=maybe_transform(
                {
                    "any_part_name": any_part_name,
                    "message": message,
                    "metadata": metadata,
                },
                script_update_params.ScriptUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"rollback_to": rollback_to}, script_update_params.ScriptUpdateParams),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[ScriptUpdateResponse], ResultWrapper[ScriptUpdateResponse]),
        )

    async def list(
        self,
        account_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ScriptListResponse:
        """
        Fetch a list of uploaded workers.

        Args:
          account_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._get(
            f"/accounts/{account_id}/workers/scripts",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[ScriptListResponse], ResultWrapper[ScriptListResponse]),
        )

    async def delete(
        self,
        script_name: str,
        *,
        account_id: str,
        force: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Delete your worker.

        This call has no response body on a successful delete.

        Args:
          account_id: Identifier

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
        if not script_name:
            raise ValueError(f"Expected a non-empty value for `script_name` but received {script_name!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/accounts/{account_id}/workers/scripts/{script_name}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"force": force}, script_delete_params.ScriptDeleteParams),
            ),
            cast_to=NoneType,
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
    ) -> AsyncBinaryAPIResponse:
        """Fetch raw script content for your worker.

        Note this is the original script
        content, not JSON encoded.

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
        extra_headers = {"Accept": "undefined", **(extra_headers or {})}
        return await self._get(
            f"/accounts/{account_id}/workers/scripts/{script_name}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AsyncBinaryAPIResponse,
        )


class ScriptsWithRawResponse:
    def __init__(self, scripts: Scripts) -> None:
        self._scripts = scripts

        self.update = to_raw_response_wrapper(
            scripts.update,
        )
        self.list = to_raw_response_wrapper(
            scripts.list,
        )
        self.delete = to_raw_response_wrapper(
            scripts.delete,
        )
        self.get = to_custom_raw_response_wrapper(
            scripts.get,
            BinaryAPIResponse,
        )

    @cached_property
    def bindings(self) -> BindingsWithRawResponse:
        return BindingsWithRawResponse(self._scripts.bindings)

    @cached_property
    def schedules(self) -> SchedulesWithRawResponse:
        return SchedulesWithRawResponse(self._scripts.schedules)

    @cached_property
    def tail(self) -> TailWithRawResponse:
        return TailWithRawResponse(self._scripts.tail)

    @cached_property
    def usage_model(self) -> UsageModelWithRawResponse:
        return UsageModelWithRawResponse(self._scripts.usage_model)


class AsyncScriptsWithRawResponse:
    def __init__(self, scripts: AsyncScripts) -> None:
        self._scripts = scripts

        self.update = async_to_raw_response_wrapper(
            scripts.update,
        )
        self.list = async_to_raw_response_wrapper(
            scripts.list,
        )
        self.delete = async_to_raw_response_wrapper(
            scripts.delete,
        )
        self.get = async_to_custom_raw_response_wrapper(
            scripts.get,
            AsyncBinaryAPIResponse,
        )

    @cached_property
    def bindings(self) -> AsyncBindingsWithRawResponse:
        return AsyncBindingsWithRawResponse(self._scripts.bindings)

    @cached_property
    def schedules(self) -> AsyncSchedulesWithRawResponse:
        return AsyncSchedulesWithRawResponse(self._scripts.schedules)

    @cached_property
    def tail(self) -> AsyncTailWithRawResponse:
        return AsyncTailWithRawResponse(self._scripts.tail)

    @cached_property
    def usage_model(self) -> AsyncUsageModelWithRawResponse:
        return AsyncUsageModelWithRawResponse(self._scripts.usage_model)


class ScriptsWithStreamingResponse:
    def __init__(self, scripts: Scripts) -> None:
        self._scripts = scripts

        self.update = to_streamed_response_wrapper(
            scripts.update,
        )
        self.list = to_streamed_response_wrapper(
            scripts.list,
        )
        self.delete = to_streamed_response_wrapper(
            scripts.delete,
        )
        self.get = to_custom_streamed_response_wrapper(
            scripts.get,
            StreamedBinaryAPIResponse,
        )

    @cached_property
    def bindings(self) -> BindingsWithStreamingResponse:
        return BindingsWithStreamingResponse(self._scripts.bindings)

    @cached_property
    def schedules(self) -> SchedulesWithStreamingResponse:
        return SchedulesWithStreamingResponse(self._scripts.schedules)

    @cached_property
    def tail(self) -> TailWithStreamingResponse:
        return TailWithStreamingResponse(self._scripts.tail)

    @cached_property
    def usage_model(self) -> UsageModelWithStreamingResponse:
        return UsageModelWithStreamingResponse(self._scripts.usage_model)


class AsyncScriptsWithStreamingResponse:
    def __init__(self, scripts: AsyncScripts) -> None:
        self._scripts = scripts

        self.update = async_to_streamed_response_wrapper(
            scripts.update,
        )
        self.list = async_to_streamed_response_wrapper(
            scripts.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            scripts.delete,
        )
        self.get = async_to_custom_streamed_response_wrapper(
            scripts.get,
            AsyncStreamedBinaryAPIResponse,
        )

    @cached_property
    def bindings(self) -> AsyncBindingsWithStreamingResponse:
        return AsyncBindingsWithStreamingResponse(self._scripts.bindings)

    @cached_property
    def schedules(self) -> AsyncSchedulesWithStreamingResponse:
        return AsyncSchedulesWithStreamingResponse(self._scripts.schedules)

    @cached_property
    def tail(self) -> AsyncTailWithStreamingResponse:
        return AsyncTailWithStreamingResponse(self._scripts.tail)

    @cached_property
    def usage_model(self) -> AsyncUsageModelWithStreamingResponse:
        return AsyncUsageModelWithStreamingResponse(self._scripts.usage_model)
