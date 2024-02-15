# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from ......_compat import cached_property

from ......types.pages.projects.deployments.histories import LogPagesDeploymentGetDeploymentLogsResponse

from ......_response import (
    to_raw_response_wrapper,
    async_to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_streamed_response_wrapper,
)

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ......_utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ......_types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ......_resource import SyncAPIResource, AsyncAPIResource
from ......_base_client import (
    SyncAPIClient,
    AsyncAPIClient,
    _merge_mappings,
    AsyncPaginator,
    make_request_options,
    HttpxBinaryResponseContent,
)
from ......types import shared_params
from ......_wrappers import ResultWrapper
from typing import cast
from typing import cast
from typing import cast
from typing import cast

__all__ = ["Logs", "AsyncLogs"]


class Logs(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> LogsWithRawResponse:
        return LogsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LogsWithStreamingResponse:
        return LogsWithStreamingResponse(self)

    def pages_deployment_get_deployment_logs(
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
    ) -> LogPagesDeploymentGetDeploymentLogsResponse:
        """
        Fetch deployment logs for a project.

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
        return cast(
            LogPagesDeploymentGetDeploymentLogsResponse,
            self._get(
                f"/accounts/{account_id}/pages/projects/{project_name}/deployments/{deployment_id}/history/logs",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[LogPagesDeploymentGetDeploymentLogsResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class AsyncLogs(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncLogsWithRawResponse:
        return AsyncLogsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLogsWithStreamingResponse:
        return AsyncLogsWithStreamingResponse(self)

    async def pages_deployment_get_deployment_logs(
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
    ) -> LogPagesDeploymentGetDeploymentLogsResponse:
        """
        Fetch deployment logs for a project.

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
        return cast(
            LogPagesDeploymentGetDeploymentLogsResponse,
            await self._get(
                f"/accounts/{account_id}/pages/projects/{project_name}/deployments/{deployment_id}/history/logs",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[LogPagesDeploymentGetDeploymentLogsResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class LogsWithRawResponse:
    def __init__(self, logs: Logs) -> None:
        self._logs = logs

        self.pages_deployment_get_deployment_logs = to_raw_response_wrapper(
            logs.pages_deployment_get_deployment_logs,
        )


class AsyncLogsWithRawResponse:
    def __init__(self, logs: AsyncLogs) -> None:
        self._logs = logs

        self.pages_deployment_get_deployment_logs = async_to_raw_response_wrapper(
            logs.pages_deployment_get_deployment_logs,
        )


class LogsWithStreamingResponse:
    def __init__(self, logs: Logs) -> None:
        self._logs = logs

        self.pages_deployment_get_deployment_logs = to_streamed_response_wrapper(
            logs.pages_deployment_get_deployment_logs,
        )


class AsyncLogsWithStreamingResponse:
    def __init__(self, logs: AsyncLogs) -> None:
        self._logs = logs

        self.pages_deployment_get_deployment_logs = async_to_streamed_response_wrapper(
            logs.pages_deployment_get_deployment_logs,
        )
