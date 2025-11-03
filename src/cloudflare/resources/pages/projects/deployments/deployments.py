# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Mapping, Optional, cast
from typing_extensions import Literal

import httpx

from ....._types import Body, Omit, Query, Headers, NotGiven, FileTypes, omit, not_given
from ....._utils import extract_files, maybe_transform, deepcopy_minimal, async_maybe_transform
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
from .history.history import (
    HistoryResource,
    AsyncHistoryResource,
    HistoryResourceWithRawResponse,
    AsyncHistoryResourceWithRawResponse,
    HistoryResourceWithStreamingResponse,
    AsyncHistoryResourceWithStreamingResponse,
)
from ....._base_client import AsyncPaginator, make_request_options
from .....types.pages.projects import (
    deployment_list_params,
    deployment_retry_params,
    deployment_create_params,
    deployment_rollback_params,
)
from .....types.pages.deployment import Deployment

__all__ = ["DeploymentsResource", "AsyncDeploymentsResource"]


class DeploymentsResource(SyncAPIResource):
    @cached_property
    def history(self) -> HistoryResource:
        return HistoryResource(self._client)

    @cached_property
    def with_raw_response(self) -> DeploymentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return DeploymentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DeploymentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return DeploymentsResourceWithStreamingResponse(self)

    def create(
        self,
        project_name: str,
        *,
        account_id: str,
        _headers: FileTypes | Omit = omit,
        _redirects: FileTypes | Omit = omit,
        _routes_json: FileTypes | Omit = omit,
        _worker_bundle: FileTypes | Omit = omit,
        _worker_js: FileTypes | Omit = omit,
        branch: str | Omit = omit,
        commit_dirty: Literal["true", "false"] | Omit = omit,
        commit_hash: str | Omit = omit,
        commit_message: str | Omit = omit,
        functions_filepath_routing_config_json: FileTypes | Omit = omit,
        manifest: str | Omit = omit,
        pages_build_output_dir: str | Omit = omit,
        wrangler_config_hash: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Deployment:
        """Start a new deployment from production.

        The repository and account must have
        already been authorized on the Cloudflare Pages dashboard.

        Args:
          account_id: Identifier

          project_name: Name of the project.

          _headers: Headers configuration file for the deployment.

          _redirects: Redirects configuration file for the deployment.

          _routes_json: Routes configuration file defining routing rules.

          _worker_bundle: Worker bundle file in multipart/form-data format. Mutually exclusive with
              `_worker.js`. Cannot specify both `_worker.js` and `_worker.bundle` in the same
              request. Maximum size: 25 MiB.

          _worker_js: Worker JavaScript file. Mutually exclusive with `_worker.bundle`. Cannot specify
              both `_worker.js` and `_worker.bundle` in the same request.

          branch: The branch to build the new deployment from. The `HEAD` of the branch will be
              used. If omitted, the production branch will be used by default.

          commit_dirty: Boolean string indicating if the working directory has uncommitted changes.

          commit_hash: Git commit SHA associated with this deployment.

          commit_message: Git commit message associated with this deployment.

          functions_filepath_routing_config_json: Functions routing configuration file.

          manifest: JSON string containing a manifest of files to deploy. Maps file paths to their
              content hashes. Required for direct upload deployments. Maximum 20,000 entries.

          pages_build_output_dir: The build output directory path.

          wrangler_config_hash: Hash of the Wrangler configuration file used for this deployment.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not project_name:
            raise ValueError(f"Expected a non-empty value for `project_name` but received {project_name!r}")
        body = deepcopy_minimal(
            {
                "_headers": _headers,
                "_redirects": _redirects,
                "_routes_json": _routes_json,
                "_worker_bundle": _worker_bundle,
                "_worker_js": _worker_js,
                "branch": branch,
                "commit_dirty": commit_dirty,
                "commit_hash": commit_hash,
                "commit_message": commit_message,
                "functions_filepath_routing_config_json": functions_filepath_routing_config_json,
                "manifest": manifest,
                "pages_build_output_dir": pages_build_output_dir,
                "wrangler_config_hash": wrangler_config_hash,
            }
        )
        files = extract_files(
            cast(Mapping[str, object], body),
            paths=[
                ["_headers"],
                ["_redirects"],
                ["_routes.json"],
                ["_worker.bundle"],
                ["_worker.js"],
                ["functions-filepath-routing-config.json"],
            ],
        )
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return self._post(
            f"/accounts/{account_id}/pages/projects/{project_name}/deployments",
            body=maybe_transform(body, deployment_create_params.DeploymentCreateParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Deployment]._unwrapper,
            ),
            cast_to=cast(Type[Deployment], ResultWrapper[Deployment]),
        )

    def list(
        self,
        project_name: str,
        *,
        account_id: str,
        env: Literal["production", "preview"] | Omit = omit,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncV4PagePaginationArray[Deployment]:
        """
        Fetch a list of project deployments.

        Args:
          account_id: Identifier

          project_name: Name of the project.

          env: What type of deployments to fetch.

          page: Which page of deployments to fetch.

          per_page: How many deployments to return per page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not project_name:
            raise ValueError(f"Expected a non-empty value for `project_name` but received {project_name!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/pages/projects/{project_name}/deployments",
            page=SyncV4PagePaginationArray[Deployment],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "env": env,
                        "page": page,
                        "per_page": per_page,
                    },
                    deployment_list_params.DeploymentListParams,
                ),
            ),
            model=Deployment,
        )

    def delete(
        self,
        deployment_id: str,
        *,
        account_id: str,
        project_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Delete a deployment.

        Args:
          account_id: Identifier

          project_name: Name of the project.

          deployment_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not project_name:
            raise ValueError(f"Expected a non-empty value for `project_name` but received {project_name!r}")
        if not deployment_id:
            raise ValueError(f"Expected a non-empty value for `deployment_id` but received {deployment_id!r}")
        return self._delete(
            f"/accounts/{account_id}/pages/projects/{project_name}/deployments/{deployment_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[object]]._unwrapper,
            ),
            cast_to=cast(Type[object], ResultWrapper[object]),
        )

    def get(
        self,
        deployment_id: str,
        *,
        account_id: str,
        project_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Deployment:
        """
        Fetch information about a deployment.

        Args:
          account_id: Identifier

          project_name: Name of the project.

          deployment_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not project_name:
            raise ValueError(f"Expected a non-empty value for `project_name` but received {project_name!r}")
        if not deployment_id:
            raise ValueError(f"Expected a non-empty value for `deployment_id` but received {deployment_id!r}")
        return self._get(
            f"/accounts/{account_id}/pages/projects/{project_name}/deployments/{deployment_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Deployment]._unwrapper,
            ),
            cast_to=cast(Type[Deployment], ResultWrapper[Deployment]),
        )

    def retry(
        self,
        deployment_id: str,
        *,
        account_id: str,
        project_name: str,
        body: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Deployment:
        """
        Retry a previous deployment.

        Args:
          account_id: Identifier

          project_name: Name of the project.

          deployment_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not project_name:
            raise ValueError(f"Expected a non-empty value for `project_name` but received {project_name!r}")
        if not deployment_id:
            raise ValueError(f"Expected a non-empty value for `deployment_id` but received {deployment_id!r}")
        return self._post(
            f"/accounts/{account_id}/pages/projects/{project_name}/deployments/{deployment_id}/retry",
            body=maybe_transform(body, deployment_retry_params.DeploymentRetryParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Deployment]._unwrapper,
            ),
            cast_to=cast(Type[Deployment], ResultWrapper[Deployment]),
        )

    def rollback(
        self,
        deployment_id: str,
        *,
        account_id: str,
        project_name: str,
        body: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Deployment:
        """Rollback the production deployment to a previous deployment.

        You can only
        rollback to succesful builds on production.

        Args:
          account_id: Identifier

          project_name: Name of the project.

          deployment_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not project_name:
            raise ValueError(f"Expected a non-empty value for `project_name` but received {project_name!r}")
        if not deployment_id:
            raise ValueError(f"Expected a non-empty value for `deployment_id` but received {deployment_id!r}")
        return self._post(
            f"/accounts/{account_id}/pages/projects/{project_name}/deployments/{deployment_id}/rollback",
            body=maybe_transform(body, deployment_rollback_params.DeploymentRollbackParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Deployment]._unwrapper,
            ),
            cast_to=cast(Type[Deployment], ResultWrapper[Deployment]),
        )


class AsyncDeploymentsResource(AsyncAPIResource):
    @cached_property
    def history(self) -> AsyncHistoryResource:
        return AsyncHistoryResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncDeploymentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDeploymentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDeploymentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncDeploymentsResourceWithStreamingResponse(self)

    async def create(
        self,
        project_name: str,
        *,
        account_id: str,
        _headers: FileTypes | Omit = omit,
        _redirects: FileTypes | Omit = omit,
        _routes_json: FileTypes | Omit = omit,
        _worker_bundle: FileTypes | Omit = omit,
        _worker_js: FileTypes | Omit = omit,
        branch: str | Omit = omit,
        commit_dirty: Literal["true", "false"] | Omit = omit,
        commit_hash: str | Omit = omit,
        commit_message: str | Omit = omit,
        functions_filepath_routing_config_json: FileTypes | Omit = omit,
        manifest: str | Omit = omit,
        pages_build_output_dir: str | Omit = omit,
        wrangler_config_hash: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Deployment:
        """Start a new deployment from production.

        The repository and account must have
        already been authorized on the Cloudflare Pages dashboard.

        Args:
          account_id: Identifier

          project_name: Name of the project.

          _headers: Headers configuration file for the deployment.

          _redirects: Redirects configuration file for the deployment.

          _routes_json: Routes configuration file defining routing rules.

          _worker_bundle: Worker bundle file in multipart/form-data format. Mutually exclusive with
              `_worker.js`. Cannot specify both `_worker.js` and `_worker.bundle` in the same
              request. Maximum size: 25 MiB.

          _worker_js: Worker JavaScript file. Mutually exclusive with `_worker.bundle`. Cannot specify
              both `_worker.js` and `_worker.bundle` in the same request.

          branch: The branch to build the new deployment from. The `HEAD` of the branch will be
              used. If omitted, the production branch will be used by default.

          commit_dirty: Boolean string indicating if the working directory has uncommitted changes.

          commit_hash: Git commit SHA associated with this deployment.

          commit_message: Git commit message associated with this deployment.

          functions_filepath_routing_config_json: Functions routing configuration file.

          manifest: JSON string containing a manifest of files to deploy. Maps file paths to their
              content hashes. Required for direct upload deployments. Maximum 20,000 entries.

          pages_build_output_dir: The build output directory path.

          wrangler_config_hash: Hash of the Wrangler configuration file used for this deployment.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not project_name:
            raise ValueError(f"Expected a non-empty value for `project_name` but received {project_name!r}")
        body = deepcopy_minimal(
            {
                "_headers": _headers,
                "_redirects": _redirects,
                "_routes_json": _routes_json,
                "_worker_bundle": _worker_bundle,
                "_worker_js": _worker_js,
                "branch": branch,
                "commit_dirty": commit_dirty,
                "commit_hash": commit_hash,
                "commit_message": commit_message,
                "functions_filepath_routing_config_json": functions_filepath_routing_config_json,
                "manifest": manifest,
                "pages_build_output_dir": pages_build_output_dir,
                "wrangler_config_hash": wrangler_config_hash,
            }
        )
        files = extract_files(
            cast(Mapping[str, object], body),
            paths=[
                ["_headers"],
                ["_redirects"],
                ["_routes.json"],
                ["_worker.bundle"],
                ["_worker.js"],
                ["functions-filepath-routing-config.json"],
            ],
        )
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return await self._post(
            f"/accounts/{account_id}/pages/projects/{project_name}/deployments",
            body=await async_maybe_transform(body, deployment_create_params.DeploymentCreateParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Deployment]._unwrapper,
            ),
            cast_to=cast(Type[Deployment], ResultWrapper[Deployment]),
        )

    def list(
        self,
        project_name: str,
        *,
        account_id: str,
        env: Literal["production", "preview"] | Omit = omit,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[Deployment, AsyncV4PagePaginationArray[Deployment]]:
        """
        Fetch a list of project deployments.

        Args:
          account_id: Identifier

          project_name: Name of the project.

          env: What type of deployments to fetch.

          page: Which page of deployments to fetch.

          per_page: How many deployments to return per page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not project_name:
            raise ValueError(f"Expected a non-empty value for `project_name` but received {project_name!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/pages/projects/{project_name}/deployments",
            page=AsyncV4PagePaginationArray[Deployment],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "env": env,
                        "page": page,
                        "per_page": per_page,
                    },
                    deployment_list_params.DeploymentListParams,
                ),
            ),
            model=Deployment,
        )

    async def delete(
        self,
        deployment_id: str,
        *,
        account_id: str,
        project_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Delete a deployment.

        Args:
          account_id: Identifier

          project_name: Name of the project.

          deployment_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not project_name:
            raise ValueError(f"Expected a non-empty value for `project_name` but received {project_name!r}")
        if not deployment_id:
            raise ValueError(f"Expected a non-empty value for `deployment_id` but received {deployment_id!r}")
        return await self._delete(
            f"/accounts/{account_id}/pages/projects/{project_name}/deployments/{deployment_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[object]]._unwrapper,
            ),
            cast_to=cast(Type[object], ResultWrapper[object]),
        )

    async def get(
        self,
        deployment_id: str,
        *,
        account_id: str,
        project_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Deployment:
        """
        Fetch information about a deployment.

        Args:
          account_id: Identifier

          project_name: Name of the project.

          deployment_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not project_name:
            raise ValueError(f"Expected a non-empty value for `project_name` but received {project_name!r}")
        if not deployment_id:
            raise ValueError(f"Expected a non-empty value for `deployment_id` but received {deployment_id!r}")
        return await self._get(
            f"/accounts/{account_id}/pages/projects/{project_name}/deployments/{deployment_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Deployment]._unwrapper,
            ),
            cast_to=cast(Type[Deployment], ResultWrapper[Deployment]),
        )

    async def retry(
        self,
        deployment_id: str,
        *,
        account_id: str,
        project_name: str,
        body: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Deployment:
        """
        Retry a previous deployment.

        Args:
          account_id: Identifier

          project_name: Name of the project.

          deployment_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not project_name:
            raise ValueError(f"Expected a non-empty value for `project_name` but received {project_name!r}")
        if not deployment_id:
            raise ValueError(f"Expected a non-empty value for `deployment_id` but received {deployment_id!r}")
        return await self._post(
            f"/accounts/{account_id}/pages/projects/{project_name}/deployments/{deployment_id}/retry",
            body=await async_maybe_transform(body, deployment_retry_params.DeploymentRetryParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Deployment]._unwrapper,
            ),
            cast_to=cast(Type[Deployment], ResultWrapper[Deployment]),
        )

    async def rollback(
        self,
        deployment_id: str,
        *,
        account_id: str,
        project_name: str,
        body: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Deployment:
        """Rollback the production deployment to a previous deployment.

        You can only
        rollback to succesful builds on production.

        Args:
          account_id: Identifier

          project_name: Name of the project.

          deployment_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not project_name:
            raise ValueError(f"Expected a non-empty value for `project_name` but received {project_name!r}")
        if not deployment_id:
            raise ValueError(f"Expected a non-empty value for `deployment_id` but received {deployment_id!r}")
        return await self._post(
            f"/accounts/{account_id}/pages/projects/{project_name}/deployments/{deployment_id}/rollback",
            body=await async_maybe_transform(body, deployment_rollback_params.DeploymentRollbackParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Deployment]._unwrapper,
            ),
            cast_to=cast(Type[Deployment], ResultWrapper[Deployment]),
        )


class DeploymentsResourceWithRawResponse:
    def __init__(self, deployments: DeploymentsResource) -> None:
        self._deployments = deployments

        self.create = to_raw_response_wrapper(
            deployments.create,
        )
        self.list = to_raw_response_wrapper(
            deployments.list,
        )
        self.delete = to_raw_response_wrapper(
            deployments.delete,
        )
        self.get = to_raw_response_wrapper(
            deployments.get,
        )
        self.retry = to_raw_response_wrapper(
            deployments.retry,
        )
        self.rollback = to_raw_response_wrapper(
            deployments.rollback,
        )

    @cached_property
    def history(self) -> HistoryResourceWithRawResponse:
        return HistoryResourceWithRawResponse(self._deployments.history)


class AsyncDeploymentsResourceWithRawResponse:
    def __init__(self, deployments: AsyncDeploymentsResource) -> None:
        self._deployments = deployments

        self.create = async_to_raw_response_wrapper(
            deployments.create,
        )
        self.list = async_to_raw_response_wrapper(
            deployments.list,
        )
        self.delete = async_to_raw_response_wrapper(
            deployments.delete,
        )
        self.get = async_to_raw_response_wrapper(
            deployments.get,
        )
        self.retry = async_to_raw_response_wrapper(
            deployments.retry,
        )
        self.rollback = async_to_raw_response_wrapper(
            deployments.rollback,
        )

    @cached_property
    def history(self) -> AsyncHistoryResourceWithRawResponse:
        return AsyncHistoryResourceWithRawResponse(self._deployments.history)


class DeploymentsResourceWithStreamingResponse:
    def __init__(self, deployments: DeploymentsResource) -> None:
        self._deployments = deployments

        self.create = to_streamed_response_wrapper(
            deployments.create,
        )
        self.list = to_streamed_response_wrapper(
            deployments.list,
        )
        self.delete = to_streamed_response_wrapper(
            deployments.delete,
        )
        self.get = to_streamed_response_wrapper(
            deployments.get,
        )
        self.retry = to_streamed_response_wrapper(
            deployments.retry,
        )
        self.rollback = to_streamed_response_wrapper(
            deployments.rollback,
        )

    @cached_property
    def history(self) -> HistoryResourceWithStreamingResponse:
        return HistoryResourceWithStreamingResponse(self._deployments.history)


class AsyncDeploymentsResourceWithStreamingResponse:
    def __init__(self, deployments: AsyncDeploymentsResource) -> None:
        self._deployments = deployments

        self.create = async_to_streamed_response_wrapper(
            deployments.create,
        )
        self.list = async_to_streamed_response_wrapper(
            deployments.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            deployments.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            deployments.get,
        )
        self.retry = async_to_streamed_response_wrapper(
            deployments.retry,
        )
        self.rollback = async_to_streamed_response_wrapper(
            deployments.rollback,
        )

    @cached_property
    def history(self) -> AsyncHistoryResourceWithStreamingResponse:
        return AsyncHistoryResourceWithStreamingResponse(self._deployments.history)
