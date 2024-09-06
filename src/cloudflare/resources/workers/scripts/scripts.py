# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .schedules import SchedulesResource, AsyncSchedulesResource

from ...._compat import cached_property

from .tail import TailResource, AsyncTailResource

from .content import ContentResource, AsyncContentResource

from .settings import SettingsResource, AsyncSettingsResource

from .deployments import DeploymentsResource, AsyncDeploymentsResource

from .versions import VersionsResource, AsyncVersionsResource

from typing import List, Optional, Type

from ...._types import FileTypes

from ....types.workers.script_update_response import ScriptUpdateResponse

from ...._wrappers import ResultWrapper

from ...._utils import maybe_transform, async_maybe_transform

from ...._base_client import make_request_options, AsyncPaginator

from ....types.workers.script import Script

from ....pagination import SyncSinglePage, AsyncSinglePage

from ...._response import (
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    to_raw_response_wrapper,
    to_custom_raw_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_custom_raw_response_wrapper,
    to_streamed_response_wrapper,
    to_custom_streamed_response_wrapper,
    StreamedBinaryAPIResponse,
    async_to_streamed_response_wrapper,
    async_to_custom_streamed_response_wrapper,
    AsyncStreamedBinaryAPIResponse,
)

from ....types.workers import script_update_params

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ...._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ...._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ...._resource import SyncAPIResource, AsyncAPIResource
from ....types import shared_params
from ....types.workers import script_update_params
from ....types.workers import script_delete_params
from .schedules import (
    SchedulesResource,
    AsyncSchedulesResource,
    SchedulesResourceWithRawResponse,
    AsyncSchedulesResourceWithRawResponse,
    SchedulesResourceWithStreamingResponse,
    AsyncSchedulesResourceWithStreamingResponse,
)
from .tail import (
    TailResource,
    AsyncTailResource,
    TailResourceWithRawResponse,
    AsyncTailResourceWithRawResponse,
    TailResourceWithStreamingResponse,
    AsyncTailResourceWithStreamingResponse,
)
from .content import (
    ContentResource,
    AsyncContentResource,
    ContentResourceWithRawResponse,
    AsyncContentResourceWithRawResponse,
    ContentResourceWithStreamingResponse,
    AsyncContentResourceWithStreamingResponse,
)
from .settings import (
    SettingsResource,
    AsyncSettingsResource,
    SettingsResourceWithRawResponse,
    AsyncSettingsResourceWithRawResponse,
    SettingsResourceWithStreamingResponse,
    AsyncSettingsResourceWithStreamingResponse,
)
from .deployments import (
    DeploymentsResource,
    AsyncDeploymentsResource,
    DeploymentsResourceWithRawResponse,
    AsyncDeploymentsResourceWithRawResponse,
    DeploymentsResourceWithStreamingResponse,
    AsyncDeploymentsResourceWithStreamingResponse,
)
from .versions import (
    VersionsResource,
    AsyncVersionsResource,
    VersionsResourceWithRawResponse,
    AsyncVersionsResourceWithRawResponse,
    VersionsResourceWithStreamingResponse,
    AsyncVersionsResourceWithStreamingResponse,
)
from typing import cast
from typing import cast

__all__ = ["ScriptsResource", "AsyncScriptsResource"]


class ScriptsResource(SyncAPIResource):
    @cached_property
    def schedules(self) -> SchedulesResource:
        return SchedulesResource(self._client)

    @cached_property
    def tail(self) -> TailResource:
        return TailResource(self._client)

    @cached_property
    def content(self) -> ContentResource:
        return ContentResource(self._client)

    @cached_property
    def settings(self) -> SettingsResource:
        return SettingsResource(self._client)

    @cached_property
    def deployments(self) -> DeploymentsResource:
        return DeploymentsResource(self._client)

    @cached_property
    def versions(self) -> VersionsResource:
        return VersionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> ScriptsResourceWithRawResponse:
        return ScriptsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ScriptsResourceWithStreamingResponse:
        return ScriptsResourceWithStreamingResponse(self)

    @overload
    def update(
        self,
        script_name: str,
        *,
        account_id: str,
        rollback_to: str | NotGiven = NOT_GIVEN,
        any_part_name: List[FileTypes] | NotGiven = NOT_GIVEN,
        metadata: script_update_params.Variant0Metadata | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ScriptUpdateResponse]:
        """Upload a worker module.

        You can find more about the multipart metadata on our
        docs:
        https://developers.cloudflare.com/workers/configuration/multipart-upload-metadata/.

        Args:
          account_id: Identifier

          script_name: Name of the script, used in URLs and route configuration.

          rollback_to: Rollback to provided deployment based on deployment ID. Request body will only
              parse a "message" part. You can learn more about deployments
              [here](https://developers.cloudflare.com/workers/platform/deployments/).

          any_part_name: A module comprising a Worker script, often a javascript file. Multiple modules
              may be provided as separate named parts, but at least one module must be present
              and referenced in the metadata as `main_module` or `body_part` by part name.
              Source maps may also be included using the `application/source-map` content
              type.

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
        rollback_to: str | NotGiven = NOT_GIVEN,
        message: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ScriptUpdateResponse]:
        """Upload a worker module.

        You can find more about the multipart metadata on our
        docs:
        https://developers.cloudflare.com/workers/configuration/multipart-upload-metadata/.

        Args:
          account_id: Identifier

          script_name: Name of the script, used in URLs and route configuration.

          rollback_to: Rollback to provided deployment based on deployment ID. Request body will only
              parse a "message" part. You can learn more about deployments
              [here](https://developers.cloudflare.com/workers/platform/deployments/).

          message: Rollback message to be associated with this deployment. Only parsed when query
              param `"rollback_to"` is present.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["account_id"])
    def update(
        self,
        script_name: str,
        *,
        account_id: str,
        rollback_to: str | NotGiven = NOT_GIVEN,
        any_part_name: List[FileTypes] | NotGiven = NOT_GIVEN,
        metadata: script_update_params.Variant0Metadata | NotGiven = NOT_GIVEN,
        message: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ScriptUpdateResponse]:
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not script_name:
            raise ValueError(f"Expected a non-empty value for `script_name` but received {script_name!r}")
        return self._put(
            f"/accounts/{account_id}/workers/scripts/{script_name}",
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
                query=maybe_transform({"rollback_to": rollback_to}, script_update_params.ScriptUpdateParams),
                post_parser=ResultWrapper[Optional[ScriptUpdateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[ScriptUpdateResponse]], ResultWrapper[ScriptUpdateResponse]),
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
    ) -> SyncSinglePage[Script]:
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
        return self._get_api_list(
            f"/accounts/{account_id}/workers/scripts",
            page=SyncSinglePage[Script],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=Script,
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


class AsyncScriptsResource(AsyncAPIResource):
    @cached_property
    def schedules(self) -> AsyncSchedulesResource:
        return AsyncSchedulesResource(self._client)

    @cached_property
    def tail(self) -> AsyncTailResource:
        return AsyncTailResource(self._client)

    @cached_property
    def content(self) -> AsyncContentResource:
        return AsyncContentResource(self._client)

    @cached_property
    def settings(self) -> AsyncSettingsResource:
        return AsyncSettingsResource(self._client)

    @cached_property
    def deployments(self) -> AsyncDeploymentsResource:
        return AsyncDeploymentsResource(self._client)

    @cached_property
    def versions(self) -> AsyncVersionsResource:
        return AsyncVersionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncScriptsResourceWithRawResponse:
        return AsyncScriptsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncScriptsResourceWithStreamingResponse:
        return AsyncScriptsResourceWithStreamingResponse(self)

    @overload
    async def update(
        self,
        script_name: str,
        *,
        account_id: str,
        rollback_to: str | NotGiven = NOT_GIVEN,
        any_part_name: List[FileTypes] | NotGiven = NOT_GIVEN,
        metadata: script_update_params.Variant0Metadata | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ScriptUpdateResponse]:
        """Upload a worker module.

        You can find more about the multipart metadata on our
        docs:
        https://developers.cloudflare.com/workers/configuration/multipart-upload-metadata/.

        Args:
          account_id: Identifier

          script_name: Name of the script, used in URLs and route configuration.

          rollback_to: Rollback to provided deployment based on deployment ID. Request body will only
              parse a "message" part. You can learn more about deployments
              [here](https://developers.cloudflare.com/workers/platform/deployments/).

          any_part_name: A module comprising a Worker script, often a javascript file. Multiple modules
              may be provided as separate named parts, but at least one module must be present
              and referenced in the metadata as `main_module` or `body_part` by part name.
              Source maps may also be included using the `application/source-map` content
              type.

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
        rollback_to: str | NotGiven = NOT_GIVEN,
        message: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ScriptUpdateResponse]:
        """Upload a worker module.

        You can find more about the multipart metadata on our
        docs:
        https://developers.cloudflare.com/workers/configuration/multipart-upload-metadata/.

        Args:
          account_id: Identifier

          script_name: Name of the script, used in URLs and route configuration.

          rollback_to: Rollback to provided deployment based on deployment ID. Request body will only
              parse a "message" part. You can learn more about deployments
              [here](https://developers.cloudflare.com/workers/platform/deployments/).

          message: Rollback message to be associated with this deployment. Only parsed when query
              param `"rollback_to"` is present.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["account_id"])
    async def update(
        self,
        script_name: str,
        *,
        account_id: str,
        rollback_to: str | NotGiven = NOT_GIVEN,
        any_part_name: List[FileTypes] | NotGiven = NOT_GIVEN,
        metadata: script_update_params.Variant0Metadata | NotGiven = NOT_GIVEN,
        message: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ScriptUpdateResponse]:
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not script_name:
            raise ValueError(f"Expected a non-empty value for `script_name` but received {script_name!r}")
        return await self._put(
            f"/accounts/{account_id}/workers/scripts/{script_name}",
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
                query=await async_maybe_transform(
                    {"rollback_to": rollback_to}, script_update_params.ScriptUpdateParams
                ),
                post_parser=ResultWrapper[Optional[ScriptUpdateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[ScriptUpdateResponse]], ResultWrapper[ScriptUpdateResponse]),
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
    ) -> AsyncPaginator[Script, AsyncSinglePage[Script]]:
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
        return self._get_api_list(
            f"/accounts/{account_id}/workers/scripts",
            page=AsyncSinglePage[Script],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=Script,
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
                query=await async_maybe_transform({"force": force}, script_delete_params.ScriptDeleteParams),
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


class ScriptsResourceWithRawResponse:
    def __init__(self, scripts: ScriptsResource) -> None:
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
    def schedules(self) -> SchedulesResourceWithRawResponse:
        return SchedulesResourceWithRawResponse(self._scripts.schedules)

    @cached_property
    def tail(self) -> TailResourceWithRawResponse:
        return TailResourceWithRawResponse(self._scripts.tail)

    @cached_property
    def content(self) -> ContentResourceWithRawResponse:
        return ContentResourceWithRawResponse(self._scripts.content)

    @cached_property
    def settings(self) -> SettingsResourceWithRawResponse:
        return SettingsResourceWithRawResponse(self._scripts.settings)

    @cached_property
    def deployments(self) -> DeploymentsResourceWithRawResponse:
        return DeploymentsResourceWithRawResponse(self._scripts.deployments)

    @cached_property
    def versions(self) -> VersionsResourceWithRawResponse:
        return VersionsResourceWithRawResponse(self._scripts.versions)


class AsyncScriptsResourceWithRawResponse:
    def __init__(self, scripts: AsyncScriptsResource) -> None:
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
    def schedules(self) -> AsyncSchedulesResourceWithRawResponse:
        return AsyncSchedulesResourceWithRawResponse(self._scripts.schedules)

    @cached_property
    def tail(self) -> AsyncTailResourceWithRawResponse:
        return AsyncTailResourceWithRawResponse(self._scripts.tail)

    @cached_property
    def content(self) -> AsyncContentResourceWithRawResponse:
        return AsyncContentResourceWithRawResponse(self._scripts.content)

    @cached_property
    def settings(self) -> AsyncSettingsResourceWithRawResponse:
        return AsyncSettingsResourceWithRawResponse(self._scripts.settings)

    @cached_property
    def deployments(self) -> AsyncDeploymentsResourceWithRawResponse:
        return AsyncDeploymentsResourceWithRawResponse(self._scripts.deployments)

    @cached_property
    def versions(self) -> AsyncVersionsResourceWithRawResponse:
        return AsyncVersionsResourceWithRawResponse(self._scripts.versions)


class ScriptsResourceWithStreamingResponse:
    def __init__(self, scripts: ScriptsResource) -> None:
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
    def schedules(self) -> SchedulesResourceWithStreamingResponse:
        return SchedulesResourceWithStreamingResponse(self._scripts.schedules)

    @cached_property
    def tail(self) -> TailResourceWithStreamingResponse:
        return TailResourceWithStreamingResponse(self._scripts.tail)

    @cached_property
    def content(self) -> ContentResourceWithStreamingResponse:
        return ContentResourceWithStreamingResponse(self._scripts.content)

    @cached_property
    def settings(self) -> SettingsResourceWithStreamingResponse:
        return SettingsResourceWithStreamingResponse(self._scripts.settings)

    @cached_property
    def deployments(self) -> DeploymentsResourceWithStreamingResponse:
        return DeploymentsResourceWithStreamingResponse(self._scripts.deployments)

    @cached_property
    def versions(self) -> VersionsResourceWithStreamingResponse:
        return VersionsResourceWithStreamingResponse(self._scripts.versions)


class AsyncScriptsResourceWithStreamingResponse:
    def __init__(self, scripts: AsyncScriptsResource) -> None:
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
    def schedules(self) -> AsyncSchedulesResourceWithStreamingResponse:
        return AsyncSchedulesResourceWithStreamingResponse(self._scripts.schedules)

    @cached_property
    def tail(self) -> AsyncTailResourceWithStreamingResponse:
        return AsyncTailResourceWithStreamingResponse(self._scripts.tail)

    @cached_property
    def content(self) -> AsyncContentResourceWithStreamingResponse:
        return AsyncContentResourceWithStreamingResponse(self._scripts.content)

    @cached_property
    def settings(self) -> AsyncSettingsResourceWithStreamingResponse:
        return AsyncSettingsResourceWithStreamingResponse(self._scripts.settings)

    @cached_property
    def deployments(self) -> AsyncDeploymentsResourceWithStreamingResponse:
        return AsyncDeploymentsResourceWithStreamingResponse(self._scripts.deployments)

    @cached_property
    def versions(self) -> AsyncVersionsResourceWithStreamingResponse:
        return AsyncVersionsResourceWithStreamingResponse(self._scripts.versions)
