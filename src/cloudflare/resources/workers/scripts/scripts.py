# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Optional, cast

import httpx

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
from .secrets import (
    SecretsResource,
    AsyncSecretsResource,
    SecretsResourceWithRawResponse,
    AsyncSecretsResourceWithRawResponse,
    SecretsResourceWithStreamingResponse,
    AsyncSecretsResourceWithStreamingResponse,
)
from .settings import (
    SettingsResource,
    AsyncSettingsResource,
    SettingsResourceWithRawResponse,
    AsyncSettingsResourceWithRawResponse,
    SettingsResourceWithStreamingResponse,
    AsyncSettingsResourceWithStreamingResponse,
)
from .versions import (
    VersionsResource,
    AsyncVersionsResource,
    VersionsResourceWithRawResponse,
    AsyncVersionsResourceWithRawResponse,
    VersionsResourceWithStreamingResponse,
    AsyncVersionsResourceWithStreamingResponse,
)
from ...._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
from ...._utils import (
    maybe_transform,
    async_maybe_transform,
)
from .schedules import (
    SchedulesResource,
    AsyncSchedulesResource,
    SchedulesResourceWithRawResponse,
    AsyncSchedulesResourceWithRawResponse,
    SchedulesResourceWithStreamingResponse,
    AsyncSchedulesResourceWithStreamingResponse,
)
from .subdomain import (
    SubdomainResource,
    AsyncSubdomainResource,
    SubdomainResourceWithRawResponse,
    AsyncSubdomainResourceWithRawResponse,
    SubdomainResourceWithStreamingResponse,
    AsyncSubdomainResourceWithStreamingResponse,
)
from ...._compat import cached_property
from .deployments import (
    DeploymentsResource,
    AsyncDeploymentsResource,
    DeploymentsResourceWithRawResponse,
    AsyncDeploymentsResourceWithRawResponse,
    DeploymentsResourceWithStreamingResponse,
    AsyncDeploymentsResourceWithStreamingResponse,
)
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._wrappers import ResultWrapper
from ....pagination import SyncSinglePage, AsyncSinglePage
from .assets.assets import (
    AssetsResource,
    AsyncAssetsResource,
    AssetsResourceWithRawResponse,
    AsyncAssetsResourceWithRawResponse,
    AssetsResourceWithStreamingResponse,
    AsyncAssetsResourceWithStreamingResponse,
)
from ...._base_client import AsyncPaginator, make_request_options
from ....types.workers import script_delete_params, script_update_params
from ....types.workers.script import Script
from ....types.workers.script_update_response import ScriptUpdateResponse

__all__ = ["ScriptsResource", "AsyncScriptsResource"]


class ScriptsResource(SyncAPIResource):
    @cached_property
    def assets(self) -> AssetsResource:
        return AssetsResource(self._client)

    @cached_property
    def subdomain(self) -> SubdomainResource:
        return SubdomainResource(self._client)

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
    def secrets(self) -> SecretsResource:
        return SecretsResource(self._client)

    @cached_property
    def with_raw_response(self) -> ScriptsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return ScriptsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ScriptsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return ScriptsResourceWithStreamingResponse(self)

    def update(
        self,
        script_name: str,
        *,
        account_id: str,
        metadata: script_update_params.Metadata,
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
            body=maybe_transform({"metadata": metadata}, script_update_params.ScriptUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
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
    ) -> str:
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
        extra_headers = {"Accept": "application/javascript", **(extra_headers or {})}
        return self._get(
            f"/accounts/{account_id}/workers/scripts/{script_name}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )


class AsyncScriptsResource(AsyncAPIResource):
    @cached_property
    def assets(self) -> AsyncAssetsResource:
        return AsyncAssetsResource(self._client)

    @cached_property
    def subdomain(self) -> AsyncSubdomainResource:
        return AsyncSubdomainResource(self._client)

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
    def secrets(self) -> AsyncSecretsResource:
        return AsyncSecretsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncScriptsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncScriptsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncScriptsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncScriptsResourceWithStreamingResponse(self)

    async def update(
        self,
        script_name: str,
        *,
        account_id: str,
        metadata: script_update_params.Metadata,
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
            body=await async_maybe_transform({"metadata": metadata}, script_update_params.ScriptUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
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
    ) -> str:
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
        extra_headers = {"Accept": "application/javascript", **(extra_headers or {})}
        return await self._get(
            f"/accounts/{account_id}/workers/scripts/{script_name}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
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
        self.get = to_raw_response_wrapper(
            scripts.get,
        )

    @cached_property
    def assets(self) -> AssetsResourceWithRawResponse:
        return AssetsResourceWithRawResponse(self._scripts.assets)

    @cached_property
    def subdomain(self) -> SubdomainResourceWithRawResponse:
        return SubdomainResourceWithRawResponse(self._scripts.subdomain)

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

    @cached_property
    def secrets(self) -> SecretsResourceWithRawResponse:
        return SecretsResourceWithRawResponse(self._scripts.secrets)


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
        self.get = async_to_raw_response_wrapper(
            scripts.get,
        )

    @cached_property
    def assets(self) -> AsyncAssetsResourceWithRawResponse:
        return AsyncAssetsResourceWithRawResponse(self._scripts.assets)

    @cached_property
    def subdomain(self) -> AsyncSubdomainResourceWithRawResponse:
        return AsyncSubdomainResourceWithRawResponse(self._scripts.subdomain)

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

    @cached_property
    def secrets(self) -> AsyncSecretsResourceWithRawResponse:
        return AsyncSecretsResourceWithRawResponse(self._scripts.secrets)


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
        self.get = to_streamed_response_wrapper(
            scripts.get,
        )

    @cached_property
    def assets(self) -> AssetsResourceWithStreamingResponse:
        return AssetsResourceWithStreamingResponse(self._scripts.assets)

    @cached_property
    def subdomain(self) -> SubdomainResourceWithStreamingResponse:
        return SubdomainResourceWithStreamingResponse(self._scripts.subdomain)

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

    @cached_property
    def secrets(self) -> SecretsResourceWithStreamingResponse:
        return SecretsResourceWithStreamingResponse(self._scripts.secrets)


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
        self.get = async_to_streamed_response_wrapper(
            scripts.get,
        )

    @cached_property
    def assets(self) -> AsyncAssetsResourceWithStreamingResponse:
        return AsyncAssetsResourceWithStreamingResponse(self._scripts.assets)

    @cached_property
    def subdomain(self) -> AsyncSubdomainResourceWithStreamingResponse:
        return AsyncSubdomainResourceWithStreamingResponse(self._scripts.subdomain)

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

    @cached_property
    def secrets(self) -> AsyncSecretsResourceWithStreamingResponse:
        return AsyncSecretsResourceWithStreamingResponse(self._scripts.secrets)
