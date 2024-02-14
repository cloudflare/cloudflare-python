# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from .histories.histories import Histories, AsyncHistories

from ....._compat import cached_property

from .retries import Retries, AsyncRetries

from .rollbacks import Rollbacks, AsyncRollbacks

from .....types.pages.projects import DeploymentCreateResponse, DeploymentListResponse, DeploymentGetResponse

from typing import Type

from ....._response import (
    to_raw_response_wrapper,
    async_to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_streamed_response_wrapper,
)

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ....._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ....._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._base_client import (
    SyncAPIClient,
    AsyncAPIClient,
    _merge_mappings,
    AsyncPaginator,
    make_request_options,
    HttpxBinaryResponseContent,
)
from .....types import shared_params
from .....types.pages.projects import deployment_create_params
from .histories import (
    Histories,
    AsyncHistories,
    HistoriesWithRawResponse,
    AsyncHistoriesWithRawResponse,
    HistoriesWithStreamingResponse,
    AsyncHistoriesWithStreamingResponse,
)
from .retries import (
    Retries,
    AsyncRetries,
    RetriesWithRawResponse,
    AsyncRetriesWithRawResponse,
    RetriesWithStreamingResponse,
    AsyncRetriesWithStreamingResponse,
)
from .rollbacks import (
    Rollbacks,
    AsyncRollbacks,
    RollbacksWithRawResponse,
    AsyncRollbacksWithRawResponse,
    RollbacksWithStreamingResponse,
    AsyncRollbacksWithStreamingResponse,
)
from ....._wrappers import ResultWrapper
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast

__all__ = ["Deployments", "AsyncDeployments"]


class Deployments(SyncAPIResource):
    @cached_property
    def histories(self) -> Histories:
        return Histories(self._client)

    @cached_property
    def retries(self) -> Retries:
        return Retries(self._client)

    @cached_property
    def rollbacks(self) -> Rollbacks:
        return Rollbacks(self._client)

    @cached_property
    def with_raw_response(self) -> DeploymentsWithRawResponse:
        return DeploymentsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DeploymentsWithStreamingResponse:
        return DeploymentsWithStreamingResponse(self)

    def create(
        self,
        project_name: str,
        *,
        account_id: str,
        branch: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DeploymentCreateResponse:
        """Start a new deployment from production.

        The repository and account must have
        already been authorized on the Cloudflare Pages dashboard.

        Args:
          account_id: Identifier

          project_name: Name of the project.

          branch: The branch to build the new deployment from. The `HEAD` of the branch will be
              used. If omitted, the production branch will be used by default.

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
            f"/accounts/{account_id}/pages/projects/{project_name}/deployments",
            body=maybe_transform({"branch": branch}, deployment_create_params.DeploymentCreateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[DeploymentCreateResponse], ResultWrapper[DeploymentCreateResponse]),
        )

    def list(
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
    ) -> DeploymentListResponse:
        """
        Fetch a list of project deployments.

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
            f"/accounts/{account_id}/pages/projects/{project_name}/deployments",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[DeploymentListResponse], ResultWrapper[DeploymentListResponse]),
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DeploymentGetResponse:
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
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[DeploymentGetResponse], ResultWrapper[DeploymentGetResponse]),
        )


class AsyncDeployments(AsyncAPIResource):
    @cached_property
    def histories(self) -> AsyncHistories:
        return AsyncHistories(self._client)

    @cached_property
    def retries(self) -> AsyncRetries:
        return AsyncRetries(self._client)

    @cached_property
    def rollbacks(self) -> AsyncRollbacks:
        return AsyncRollbacks(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncDeploymentsWithRawResponse:
        return AsyncDeploymentsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDeploymentsWithStreamingResponse:
        return AsyncDeploymentsWithStreamingResponse(self)

    async def create(
        self,
        project_name: str,
        *,
        account_id: str,
        branch: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DeploymentCreateResponse:
        """Start a new deployment from production.

        The repository and account must have
        already been authorized on the Cloudflare Pages dashboard.

        Args:
          account_id: Identifier

          project_name: Name of the project.

          branch: The branch to build the new deployment from. The `HEAD` of the branch will be
              used. If omitted, the production branch will be used by default.

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
            f"/accounts/{account_id}/pages/projects/{project_name}/deployments",
            body=maybe_transform({"branch": branch}, deployment_create_params.DeploymentCreateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[DeploymentCreateResponse], ResultWrapper[DeploymentCreateResponse]),
        )

    async def list(
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
    ) -> DeploymentListResponse:
        """
        Fetch a list of project deployments.

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
            f"/accounts/{account_id}/pages/projects/{project_name}/deployments",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[DeploymentListResponse], ResultWrapper[DeploymentListResponse]),
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DeploymentGetResponse:
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
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[DeploymentGetResponse], ResultWrapper[DeploymentGetResponse]),
        )


class DeploymentsWithRawResponse:
    def __init__(self, deployments: Deployments) -> None:
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

    @cached_property
    def histories(self) -> HistoriesWithRawResponse:
        return HistoriesWithRawResponse(self._deployments.histories)

    @cached_property
    def retries(self) -> RetriesWithRawResponse:
        return RetriesWithRawResponse(self._deployments.retries)

    @cached_property
    def rollbacks(self) -> RollbacksWithRawResponse:
        return RollbacksWithRawResponse(self._deployments.rollbacks)


class AsyncDeploymentsWithRawResponse:
    def __init__(self, deployments: AsyncDeployments) -> None:
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

    @cached_property
    def histories(self) -> AsyncHistoriesWithRawResponse:
        return AsyncHistoriesWithRawResponse(self._deployments.histories)

    @cached_property
    def retries(self) -> AsyncRetriesWithRawResponse:
        return AsyncRetriesWithRawResponse(self._deployments.retries)

    @cached_property
    def rollbacks(self) -> AsyncRollbacksWithRawResponse:
        return AsyncRollbacksWithRawResponse(self._deployments.rollbacks)


class DeploymentsWithStreamingResponse:
    def __init__(self, deployments: Deployments) -> None:
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

    @cached_property
    def histories(self) -> HistoriesWithStreamingResponse:
        return HistoriesWithStreamingResponse(self._deployments.histories)

    @cached_property
    def retries(self) -> RetriesWithStreamingResponse:
        return RetriesWithStreamingResponse(self._deployments.retries)

    @cached_property
    def rollbacks(self) -> RollbacksWithStreamingResponse:
        return RollbacksWithStreamingResponse(self._deployments.rollbacks)


class AsyncDeploymentsWithStreamingResponse:
    def __init__(self, deployments: AsyncDeployments) -> None:
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

    @cached_property
    def histories(self) -> AsyncHistoriesWithStreamingResponse:
        return AsyncHistoriesWithStreamingResponse(self._deployments.histories)

    @cached_property
    def retries(self) -> AsyncRetriesWithStreamingResponse:
        return AsyncRetriesWithStreamingResponse(self._deployments.retries)

    @cached_property
    def rollbacks(self) -> AsyncRollbacksWithStreamingResponse:
        return AsyncRollbacksWithStreamingResponse(self._deployments.rollbacks)
