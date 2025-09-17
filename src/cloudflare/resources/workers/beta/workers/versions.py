# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Iterable, cast
from typing_extensions import Literal

import httpx

from ....._types import NOT_GIVEN, Body, Query, Headers, NotGiven, SequenceNotStr
from ....._utils import maybe_transform, async_maybe_transform
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....._wrappers import ResultWrapper
from .....pagination import SyncV4PagePaginationArray, AsyncV4PagePaginationArray
from ....._base_client import AsyncPaginator, make_request_options
from .....types.workers.beta.workers import version_get_params, version_list_params, version_create_params
from .....types.workers.beta.workers.version import Version
from .....types.workers.beta.workers.version_delete_response import VersionDeleteResponse

__all__ = ["VersionsResource", "AsyncVersionsResource"]


class VersionsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> VersionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return VersionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> VersionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return VersionsResourceWithStreamingResponse(self)

    def create(
        self,
        worker_id: str,
        *,
        account_id: str,
        deploy: bool | NotGiven = NOT_GIVEN,
        annotations: version_create_params.Annotations | NotGiven = NOT_GIVEN,
        assets: version_create_params.Assets | NotGiven = NOT_GIVEN,
        bindings: Iterable[version_create_params.Binding] | NotGiven = NOT_GIVEN,
        compatibility_date: str | NotGiven = NOT_GIVEN,
        compatibility_flags: SequenceNotStr[str] | NotGiven = NOT_GIVEN,
        limits: version_create_params.Limits | NotGiven = NOT_GIVEN,
        main_module: str | NotGiven = NOT_GIVEN,
        migrations: version_create_params.Migrations | NotGiven = NOT_GIVEN,
        modules: Iterable[version_create_params.Module] | NotGiven = NOT_GIVEN,
        placement: version_create_params.Placement | NotGiven = NOT_GIVEN,
        usage_model: Literal["standard", "bundled", "unbound"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Version:
        """
        Create a new version.

        Args:
          account_id: Identifier.

          worker_id: Identifier for the Worker, which can be ID or name.

          deploy: If true, a deployment will be created that sends 100% of traffic to the new
              version.

          annotations: Metadata about the version.

          assets: Configuration for assets within a Worker.

              [`_headers`](https://developers.cloudflare.com/workers/static-assets/headers/#custom-headers)
              and
              [`_redirects`](https://developers.cloudflare.com/workers/static-assets/redirects/)
              files should be included as modules named `_headers` and `_redirects` with
              content type `text/plain`.

          bindings: List of bindings attached to a Worker. You can find more about bindings on our
              docs:
              https://developers.cloudflare.com/workers/configuration/multipart-upload-metadata/#bindings.

          compatibility_date: Date indicating targeted support in the Workers runtime. Backwards incompatible
              fixes to the runtime following this date will not affect this Worker.

          compatibility_flags: Flags that enable or disable certain features in the Workers runtime. Used to
              enable upcoming features or opt in or out of specific changes not included in a
              `compatibility_date`.

          limits: Resource limits enforced at runtime.

          main_module: The name of the main module in the `modules` array (e.g. the name of the module
              that exports a `fetch` handler).

          migrations: Migrations for Durable Objects associated with the version. Migrations are
              applied when the version is deployed.

          modules: Code, sourcemaps, and other content used at runtime.

              This includes
              [`_headers`](https://developers.cloudflare.com/workers/static-assets/headers/#custom-headers)
              and
              [`_redirects`](https://developers.cloudflare.com/workers/static-assets/redirects/)
              files used to configure
              [Static Assets](https://developers.cloudflare.com/workers/static-assets/).
              `_headers` and `_redirects` files should be included as modules named `_headers`
              and `_redirects` with content type `text/plain`.

          placement: Placement settings for the version.

          usage_model: Usage model for the version.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not worker_id:
            raise ValueError(f"Expected a non-empty value for `worker_id` but received {worker_id!r}")
        return self._post(
            f"/accounts/{account_id}/workers/workers/{worker_id}/versions",
            body=maybe_transform(
                {
                    "annotations": annotations,
                    "assets": assets,
                    "bindings": bindings,
                    "compatibility_date": compatibility_date,
                    "compatibility_flags": compatibility_flags,
                    "limits": limits,
                    "main_module": main_module,
                    "migrations": migrations,
                    "modules": modules,
                    "placement": placement,
                    "usage_model": usage_model,
                },
                version_create_params.VersionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"deploy": deploy}, version_create_params.VersionCreateParams),
                post_parser=ResultWrapper[Version]._unwrapper,
            ),
            cast_to=cast(Type[Version], ResultWrapper[Version]),
        )

    def list(
        self,
        worker_id: str,
        *,
        account_id: str,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncV4PagePaginationArray[Version]:
        """
        List all versions for a Worker.

        Args:
          account_id: Identifier.

          worker_id: Identifier for the Worker, which can be ID or name.

          page: Current page.

          per_page: Items per-page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not worker_id:
            raise ValueError(f"Expected a non-empty value for `worker_id` but received {worker_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/workers/workers/{worker_id}/versions",
            page=SyncV4PagePaginationArray[Version],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page": page,
                        "per_page": per_page,
                    },
                    version_list_params.VersionListParams,
                ),
            ),
            model=Version,
        )

    def delete(
        self,
        version_id: str,
        *,
        account_id: str,
        worker_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> VersionDeleteResponse:
        """
        Delete a version.

        Args:
          account_id: Identifier.

          worker_id: Identifier for the Worker, which can be ID or name.

          version_id: Identifier for the version, which can be ID or the literal "latest" to operate
              on the most recently created version.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not worker_id:
            raise ValueError(f"Expected a non-empty value for `worker_id` but received {worker_id!r}")
        if not version_id:
            raise ValueError(f"Expected a non-empty value for `version_id` but received {version_id!r}")
        return self._delete(
            f"/accounts/{account_id}/workers/workers/{worker_id}/versions/{version_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VersionDeleteResponse,
        )

    def get(
        self,
        version_id: str,
        *,
        account_id: str,
        worker_id: str,
        include: Literal["modules"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Version:
        """
        Get details about a specific version.

        Args:
          account_id: Identifier.

          worker_id: Identifier for the Worker, which can be ID or name.

          version_id: Identifier for the version, which can be ID or the literal "latest" to operate
              on the most recently created version.

          include: Whether to include the `modules` property of the version in the response, which
              contains code and sourcemap content and may add several megabytes to the
              response size.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not worker_id:
            raise ValueError(f"Expected a non-empty value for `worker_id` but received {worker_id!r}")
        if not version_id:
            raise ValueError(f"Expected a non-empty value for `version_id` but received {version_id!r}")
        return self._get(
            f"/accounts/{account_id}/workers/workers/{worker_id}/versions/{version_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"include": include}, version_get_params.VersionGetParams),
                post_parser=ResultWrapper[Version]._unwrapper,
            ),
            cast_to=cast(Type[Version], ResultWrapper[Version]),
        )


class AsyncVersionsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncVersionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncVersionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncVersionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncVersionsResourceWithStreamingResponse(self)

    async def create(
        self,
        worker_id: str,
        *,
        account_id: str,
        deploy: bool | NotGiven = NOT_GIVEN,
        annotations: version_create_params.Annotations | NotGiven = NOT_GIVEN,
        assets: version_create_params.Assets | NotGiven = NOT_GIVEN,
        bindings: Iterable[version_create_params.Binding] | NotGiven = NOT_GIVEN,
        compatibility_date: str | NotGiven = NOT_GIVEN,
        compatibility_flags: SequenceNotStr[str] | NotGiven = NOT_GIVEN,
        limits: version_create_params.Limits | NotGiven = NOT_GIVEN,
        main_module: str | NotGiven = NOT_GIVEN,
        migrations: version_create_params.Migrations | NotGiven = NOT_GIVEN,
        modules: Iterable[version_create_params.Module] | NotGiven = NOT_GIVEN,
        placement: version_create_params.Placement | NotGiven = NOT_GIVEN,
        usage_model: Literal["standard", "bundled", "unbound"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Version:
        """
        Create a new version.

        Args:
          account_id: Identifier.

          worker_id: Identifier for the Worker, which can be ID or name.

          deploy: If true, a deployment will be created that sends 100% of traffic to the new
              version.

          annotations: Metadata about the version.

          assets: Configuration for assets within a Worker.

              [`_headers`](https://developers.cloudflare.com/workers/static-assets/headers/#custom-headers)
              and
              [`_redirects`](https://developers.cloudflare.com/workers/static-assets/redirects/)
              files should be included as modules named `_headers` and `_redirects` with
              content type `text/plain`.

          bindings: List of bindings attached to a Worker. You can find more about bindings on our
              docs:
              https://developers.cloudflare.com/workers/configuration/multipart-upload-metadata/#bindings.

          compatibility_date: Date indicating targeted support in the Workers runtime. Backwards incompatible
              fixes to the runtime following this date will not affect this Worker.

          compatibility_flags: Flags that enable or disable certain features in the Workers runtime. Used to
              enable upcoming features or opt in or out of specific changes not included in a
              `compatibility_date`.

          limits: Resource limits enforced at runtime.

          main_module: The name of the main module in the `modules` array (e.g. the name of the module
              that exports a `fetch` handler).

          migrations: Migrations for Durable Objects associated with the version. Migrations are
              applied when the version is deployed.

          modules: Code, sourcemaps, and other content used at runtime.

              This includes
              [`_headers`](https://developers.cloudflare.com/workers/static-assets/headers/#custom-headers)
              and
              [`_redirects`](https://developers.cloudflare.com/workers/static-assets/redirects/)
              files used to configure
              [Static Assets](https://developers.cloudflare.com/workers/static-assets/).
              `_headers` and `_redirects` files should be included as modules named `_headers`
              and `_redirects` with content type `text/plain`.

          placement: Placement settings for the version.

          usage_model: Usage model for the version.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not worker_id:
            raise ValueError(f"Expected a non-empty value for `worker_id` but received {worker_id!r}")
        return await self._post(
            f"/accounts/{account_id}/workers/workers/{worker_id}/versions",
            body=await async_maybe_transform(
                {
                    "annotations": annotations,
                    "assets": assets,
                    "bindings": bindings,
                    "compatibility_date": compatibility_date,
                    "compatibility_flags": compatibility_flags,
                    "limits": limits,
                    "main_module": main_module,
                    "migrations": migrations,
                    "modules": modules,
                    "placement": placement,
                    "usage_model": usage_model,
                },
                version_create_params.VersionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"deploy": deploy}, version_create_params.VersionCreateParams),
                post_parser=ResultWrapper[Version]._unwrapper,
            ),
            cast_to=cast(Type[Version], ResultWrapper[Version]),
        )

    def list(
        self,
        worker_id: str,
        *,
        account_id: str,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[Version, AsyncV4PagePaginationArray[Version]]:
        """
        List all versions for a Worker.

        Args:
          account_id: Identifier.

          worker_id: Identifier for the Worker, which can be ID or name.

          page: Current page.

          per_page: Items per-page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not worker_id:
            raise ValueError(f"Expected a non-empty value for `worker_id` but received {worker_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/workers/workers/{worker_id}/versions",
            page=AsyncV4PagePaginationArray[Version],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page": page,
                        "per_page": per_page,
                    },
                    version_list_params.VersionListParams,
                ),
            ),
            model=Version,
        )

    async def delete(
        self,
        version_id: str,
        *,
        account_id: str,
        worker_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> VersionDeleteResponse:
        """
        Delete a version.

        Args:
          account_id: Identifier.

          worker_id: Identifier for the Worker, which can be ID or name.

          version_id: Identifier for the version, which can be ID or the literal "latest" to operate
              on the most recently created version.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not worker_id:
            raise ValueError(f"Expected a non-empty value for `worker_id` but received {worker_id!r}")
        if not version_id:
            raise ValueError(f"Expected a non-empty value for `version_id` but received {version_id!r}")
        return await self._delete(
            f"/accounts/{account_id}/workers/workers/{worker_id}/versions/{version_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VersionDeleteResponse,
        )

    async def get(
        self,
        version_id: str,
        *,
        account_id: str,
        worker_id: str,
        include: Literal["modules"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Version:
        """
        Get details about a specific version.

        Args:
          account_id: Identifier.

          worker_id: Identifier for the Worker, which can be ID or name.

          version_id: Identifier for the version, which can be ID or the literal "latest" to operate
              on the most recently created version.

          include: Whether to include the `modules` property of the version in the response, which
              contains code and sourcemap content and may add several megabytes to the
              response size.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not worker_id:
            raise ValueError(f"Expected a non-empty value for `worker_id` but received {worker_id!r}")
        if not version_id:
            raise ValueError(f"Expected a non-empty value for `version_id` but received {version_id!r}")
        return await self._get(
            f"/accounts/{account_id}/workers/workers/{worker_id}/versions/{version_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"include": include}, version_get_params.VersionGetParams),
                post_parser=ResultWrapper[Version]._unwrapper,
            ),
            cast_to=cast(Type[Version], ResultWrapper[Version]),
        )


class VersionsResourceWithRawResponse:
    def __init__(self, versions: VersionsResource) -> None:
        self._versions = versions

        self.create = to_raw_response_wrapper(
            versions.create,
        )
        self.list = to_raw_response_wrapper(
            versions.list,
        )
        self.delete = to_raw_response_wrapper(
            versions.delete,
        )
        self.get = to_raw_response_wrapper(
            versions.get,
        )


class AsyncVersionsResourceWithRawResponse:
    def __init__(self, versions: AsyncVersionsResource) -> None:
        self._versions = versions

        self.create = async_to_raw_response_wrapper(
            versions.create,
        )
        self.list = async_to_raw_response_wrapper(
            versions.list,
        )
        self.delete = async_to_raw_response_wrapper(
            versions.delete,
        )
        self.get = async_to_raw_response_wrapper(
            versions.get,
        )


class VersionsResourceWithStreamingResponse:
    def __init__(self, versions: VersionsResource) -> None:
        self._versions = versions

        self.create = to_streamed_response_wrapper(
            versions.create,
        )
        self.list = to_streamed_response_wrapper(
            versions.list,
        )
        self.delete = to_streamed_response_wrapper(
            versions.delete,
        )
        self.get = to_streamed_response_wrapper(
            versions.get,
        )


class AsyncVersionsResourceWithStreamingResponse:
    def __init__(self, versions: AsyncVersionsResource) -> None:
        self._versions = versions

        self.create = async_to_streamed_response_wrapper(
            versions.create,
        )
        self.list = async_to_streamed_response_wrapper(
            versions.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            versions.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            versions.get,
        )
