# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Optional, cast

import httpx

from .domains import (
    DomainsResource,
    AsyncDomainsResource,
    DomainsResourceWithRawResponse,
    AsyncDomainsResourceWithRawResponse,
    DomainsResourceWithStreamingResponse,
    AsyncDomainsResourceWithStreamingResponse,
)
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
from ....pagination import SyncSinglePage, AsyncSinglePage
from ....types.pages import project_edit_params, project_create_params
from ...._base_client import AsyncPaginator, make_request_options
from ....types.pages.project import Project
from .deployments.deployments import (
    DeploymentsResource,
    AsyncDeploymentsResource,
    DeploymentsResourceWithRawResponse,
    AsyncDeploymentsResourceWithRawResponse,
    DeploymentsResourceWithStreamingResponse,
    AsyncDeploymentsResourceWithStreamingResponse,
)
from ....types.pages.deployment import Deployment

__all__ = ["ProjectsResource", "AsyncProjectsResource"]


class ProjectsResource(SyncAPIResource):
    @cached_property
    def deployments(self) -> DeploymentsResource:
        return DeploymentsResource(self._client)

    @cached_property
    def domains(self) -> DomainsResource:
        return DomainsResource(self._client)

    @cached_property
    def with_raw_response(self) -> ProjectsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return ProjectsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ProjectsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return ProjectsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        account_id: str,
        build_config: project_create_params.BuildConfig | NotGiven = NOT_GIVEN,
        deployment_configs: project_create_params.DeploymentConfigs | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        production_branch: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Project:
        """
        Create a new project.

        Args:
          account_id: Identifier

          build_config: Configs for the project build process.

          deployment_configs: Configs for deployments in a project.

          name: Name of the project.

          production_branch: Production branch of the project. Used to identify production deployments.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._post(
            f"/accounts/{account_id}/pages/projects",
            body=maybe_transform(
                {
                    "build_config": build_config,
                    "deployment_configs": deployment_configs,
                    "name": name,
                    "production_branch": production_branch,
                },
                project_create_params.ProjectCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Project]._unwrapper,
            ),
            cast_to=cast(Type[Project], ResultWrapper[Project]),
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
    ) -> SyncSinglePage[Deployment]:
        """
        Fetch a list of all user projects.

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
            f"/accounts/{account_id}/pages/projects",
            page=SyncSinglePage[Deployment],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=Deployment,
        )

    def delete(
        self,
        project_name: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Delete a project by name.

        Args:
          account_id: Identifier

          project_name: Name of the project.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not project_name:
            raise ValueError(f"Expected a non-empty value for `project_name` but received {project_name!r}")
        return self._delete(
            f"/accounts/{account_id}/pages/projects/{project_name}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[object]]._unwrapper,
            ),
            cast_to=cast(Type[object], ResultWrapper[object]),
        )

    def edit(
        self,
        project_name: str,
        *,
        account_id: str,
        build_config: project_edit_params.BuildConfig | NotGiven = NOT_GIVEN,
        deployment_configs: project_edit_params.DeploymentConfigs | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        production_branch: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Project:
        """Set new attributes for an existing project.

        Modify environment variables. To
        delete an environment variable, set the key to null.

        Args:
          account_id: Identifier

          project_name: Name of the project.

          build_config: Configs for the project build process.

          deployment_configs: Configs for deployments in a project.

          name: Name of the project.

          production_branch: Production branch of the project. Used to identify production deployments.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not project_name:
            raise ValueError(f"Expected a non-empty value for `project_name` but received {project_name!r}")
        return self._patch(
            f"/accounts/{account_id}/pages/projects/{project_name}",
            body=maybe_transform(
                {
                    "build_config": build_config,
                    "deployment_configs": deployment_configs,
                    "name": name,
                    "production_branch": production_branch,
                },
                project_edit_params.ProjectEditParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Project]._unwrapper,
            ),
            cast_to=cast(Type[Project], ResultWrapper[Project]),
        )

    def get(
        self,
        project_name: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Project:
        """
        Fetch a project by name.

        Args:
          account_id: Identifier

          project_name: Name of the project.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not project_name:
            raise ValueError(f"Expected a non-empty value for `project_name` but received {project_name!r}")
        return self._get(
            f"/accounts/{account_id}/pages/projects/{project_name}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Project]._unwrapper,
            ),
            cast_to=cast(Type[Project], ResultWrapper[Project]),
        )

    def purge_build_cache(
        self,
        project_name: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Purge all cached build artifacts for a Pages project

        Args:
          account_id: Identifier

          project_name: Name of the project.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not project_name:
            raise ValueError(f"Expected a non-empty value for `project_name` but received {project_name!r}")
        return self._post(
            f"/accounts/{account_id}/pages/projects/{project_name}/purge_build_cache",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[object]]._unwrapper,
            ),
            cast_to=cast(Type[object], ResultWrapper[object]),
        )


class AsyncProjectsResource(AsyncAPIResource):
    @cached_property
    def deployments(self) -> AsyncDeploymentsResource:
        return AsyncDeploymentsResource(self._client)

    @cached_property
    def domains(self) -> AsyncDomainsResource:
        return AsyncDomainsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncProjectsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncProjectsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncProjectsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncProjectsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_id: str,
        build_config: project_create_params.BuildConfig | NotGiven = NOT_GIVEN,
        deployment_configs: project_create_params.DeploymentConfigs | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        production_branch: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Project:
        """
        Create a new project.

        Args:
          account_id: Identifier

          build_config: Configs for the project build process.

          deployment_configs: Configs for deployments in a project.

          name: Name of the project.

          production_branch: Production branch of the project. Used to identify production deployments.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._post(
            f"/accounts/{account_id}/pages/projects",
            body=await async_maybe_transform(
                {
                    "build_config": build_config,
                    "deployment_configs": deployment_configs,
                    "name": name,
                    "production_branch": production_branch,
                },
                project_create_params.ProjectCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Project]._unwrapper,
            ),
            cast_to=cast(Type[Project], ResultWrapper[Project]),
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
    ) -> AsyncPaginator[Deployment, AsyncSinglePage[Deployment]]:
        """
        Fetch a list of all user projects.

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
            f"/accounts/{account_id}/pages/projects",
            page=AsyncSinglePage[Deployment],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=Deployment,
        )

    async def delete(
        self,
        project_name: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Delete a project by name.

        Args:
          account_id: Identifier

          project_name: Name of the project.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not project_name:
            raise ValueError(f"Expected a non-empty value for `project_name` but received {project_name!r}")
        return await self._delete(
            f"/accounts/{account_id}/pages/projects/{project_name}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[object]]._unwrapper,
            ),
            cast_to=cast(Type[object], ResultWrapper[object]),
        )

    async def edit(
        self,
        project_name: str,
        *,
        account_id: str,
        build_config: project_edit_params.BuildConfig | NotGiven = NOT_GIVEN,
        deployment_configs: project_edit_params.DeploymentConfigs | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        production_branch: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Project:
        """Set new attributes for an existing project.

        Modify environment variables. To
        delete an environment variable, set the key to null.

        Args:
          account_id: Identifier

          project_name: Name of the project.

          build_config: Configs for the project build process.

          deployment_configs: Configs for deployments in a project.

          name: Name of the project.

          production_branch: Production branch of the project. Used to identify production deployments.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not project_name:
            raise ValueError(f"Expected a non-empty value for `project_name` but received {project_name!r}")
        return await self._patch(
            f"/accounts/{account_id}/pages/projects/{project_name}",
            body=await async_maybe_transform(
                {
                    "build_config": build_config,
                    "deployment_configs": deployment_configs,
                    "name": name,
                    "production_branch": production_branch,
                },
                project_edit_params.ProjectEditParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Project]._unwrapper,
            ),
            cast_to=cast(Type[Project], ResultWrapper[Project]),
        )

    async def get(
        self,
        project_name: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Project:
        """
        Fetch a project by name.

        Args:
          account_id: Identifier

          project_name: Name of the project.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not project_name:
            raise ValueError(f"Expected a non-empty value for `project_name` but received {project_name!r}")
        return await self._get(
            f"/accounts/{account_id}/pages/projects/{project_name}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Project]._unwrapper,
            ),
            cast_to=cast(Type[Project], ResultWrapper[Project]),
        )

    async def purge_build_cache(
        self,
        project_name: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Purge all cached build artifacts for a Pages project

        Args:
          account_id: Identifier

          project_name: Name of the project.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not project_name:
            raise ValueError(f"Expected a non-empty value for `project_name` but received {project_name!r}")
        return await self._post(
            f"/accounts/{account_id}/pages/projects/{project_name}/purge_build_cache",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[object]]._unwrapper,
            ),
            cast_to=cast(Type[object], ResultWrapper[object]),
        )


class ProjectsResourceWithRawResponse:
    def __init__(self, projects: ProjectsResource) -> None:
        self._projects = projects

        self.create = to_raw_response_wrapper(
            projects.create,
        )
        self.list = to_raw_response_wrapper(
            projects.list,
        )
        self.delete = to_raw_response_wrapper(
            projects.delete,
        )
        self.edit = to_raw_response_wrapper(
            projects.edit,
        )
        self.get = to_raw_response_wrapper(
            projects.get,
        )
        self.purge_build_cache = to_raw_response_wrapper(
            projects.purge_build_cache,
        )

    @cached_property
    def deployments(self) -> DeploymentsResourceWithRawResponse:
        return DeploymentsResourceWithRawResponse(self._projects.deployments)

    @cached_property
    def domains(self) -> DomainsResourceWithRawResponse:
        return DomainsResourceWithRawResponse(self._projects.domains)


class AsyncProjectsResourceWithRawResponse:
    def __init__(self, projects: AsyncProjectsResource) -> None:
        self._projects = projects

        self.create = async_to_raw_response_wrapper(
            projects.create,
        )
        self.list = async_to_raw_response_wrapper(
            projects.list,
        )
        self.delete = async_to_raw_response_wrapper(
            projects.delete,
        )
        self.edit = async_to_raw_response_wrapper(
            projects.edit,
        )
        self.get = async_to_raw_response_wrapper(
            projects.get,
        )
        self.purge_build_cache = async_to_raw_response_wrapper(
            projects.purge_build_cache,
        )

    @cached_property
    def deployments(self) -> AsyncDeploymentsResourceWithRawResponse:
        return AsyncDeploymentsResourceWithRawResponse(self._projects.deployments)

    @cached_property
    def domains(self) -> AsyncDomainsResourceWithRawResponse:
        return AsyncDomainsResourceWithRawResponse(self._projects.domains)


class ProjectsResourceWithStreamingResponse:
    def __init__(self, projects: ProjectsResource) -> None:
        self._projects = projects

        self.create = to_streamed_response_wrapper(
            projects.create,
        )
        self.list = to_streamed_response_wrapper(
            projects.list,
        )
        self.delete = to_streamed_response_wrapper(
            projects.delete,
        )
        self.edit = to_streamed_response_wrapper(
            projects.edit,
        )
        self.get = to_streamed_response_wrapper(
            projects.get,
        )
        self.purge_build_cache = to_streamed_response_wrapper(
            projects.purge_build_cache,
        )

    @cached_property
    def deployments(self) -> DeploymentsResourceWithStreamingResponse:
        return DeploymentsResourceWithStreamingResponse(self._projects.deployments)

    @cached_property
    def domains(self) -> DomainsResourceWithStreamingResponse:
        return DomainsResourceWithStreamingResponse(self._projects.domains)


class AsyncProjectsResourceWithStreamingResponse:
    def __init__(self, projects: AsyncProjectsResource) -> None:
        self._projects = projects

        self.create = async_to_streamed_response_wrapper(
            projects.create,
        )
        self.list = async_to_streamed_response_wrapper(
            projects.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            projects.delete,
        )
        self.edit = async_to_streamed_response_wrapper(
            projects.edit,
        )
        self.get = async_to_streamed_response_wrapper(
            projects.get,
        )
        self.purge_build_cache = async_to_streamed_response_wrapper(
            projects.purge_build_cache,
        )

    @cached_property
    def deployments(self) -> AsyncDeploymentsResourceWithStreamingResponse:
        return AsyncDeploymentsResourceWithStreamingResponse(self._projects.deployments)

    @cached_property
    def domains(self) -> AsyncDomainsResourceWithStreamingResponse:
        return AsyncDomainsResourceWithStreamingResponse(self._projects.domains)
