# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from ....._compat import cached_property

from .....types.pages.projects.deployments import RollbackPagesDeploymentRollbackDeploymentResponse

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
from ....._wrappers import ResultWrapper
from typing import cast
from typing import cast

__all__ = ["Rollbacks", "AsyncRollbacks"]


class Rollbacks(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RollbacksWithRawResponse:
        return RollbacksWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RollbacksWithStreamingResponse:
        return RollbacksWithStreamingResponse(self)

    def pages_deployment_rollback_deployment(
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
    ) -> RollbackPagesDeploymentRollbackDeploymentResponse:
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
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[RollbackPagesDeploymentRollbackDeploymentResponse],
                ResultWrapper[RollbackPagesDeploymentRollbackDeploymentResponse],
            ),
        )


class AsyncRollbacks(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRollbacksWithRawResponse:
        return AsyncRollbacksWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRollbacksWithStreamingResponse:
        return AsyncRollbacksWithStreamingResponse(self)

    async def pages_deployment_rollback_deployment(
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
    ) -> RollbackPagesDeploymentRollbackDeploymentResponse:
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
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[RollbackPagesDeploymentRollbackDeploymentResponse],
                ResultWrapper[RollbackPagesDeploymentRollbackDeploymentResponse],
            ),
        )


class RollbacksWithRawResponse:
    def __init__(self, rollbacks: Rollbacks) -> None:
        self._rollbacks = rollbacks

        self.pages_deployment_rollback_deployment = to_raw_response_wrapper(
            rollbacks.pages_deployment_rollback_deployment,
        )


class AsyncRollbacksWithRawResponse:
    def __init__(self, rollbacks: AsyncRollbacks) -> None:
        self._rollbacks = rollbacks

        self.pages_deployment_rollback_deployment = async_to_raw_response_wrapper(
            rollbacks.pages_deployment_rollback_deployment,
        )


class RollbacksWithStreamingResponse:
    def __init__(self, rollbacks: Rollbacks) -> None:
        self._rollbacks = rollbacks

        self.pages_deployment_rollback_deployment = to_streamed_response_wrapper(
            rollbacks.pages_deployment_rollback_deployment,
        )


class AsyncRollbacksWithStreamingResponse:
    def __init__(self, rollbacks: AsyncRollbacks) -> None:
        self._rollbacks = rollbacks

        self.pages_deployment_rollback_deployment = async_to_streamed_response_wrapper(
            rollbacks.pages_deployment_rollback_deployment,
        )
