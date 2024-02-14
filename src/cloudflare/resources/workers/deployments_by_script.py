# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from ..._compat import cached_property

from ...types.workers import DeploymentsByScriptListResponse, DeploymentsByScriptDetailResponse

from typing import Type

from ..._response import (
    to_raw_response_wrapper,
    async_to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_streamed_response_wrapper,
)

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ..._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ..._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._base_client import (
    SyncAPIClient,
    AsyncAPIClient,
    _merge_mappings,
    AsyncPaginator,
    make_request_options,
    HttpxBinaryResponseContent,
)
from ...types import shared_params
from ..._wrappers import ResultWrapper
from typing import cast
from typing import cast
from typing import cast
from typing import cast

__all__ = ["DeploymentsByScript", "AsyncDeploymentsByScript"]


class DeploymentsByScript(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DeploymentsByScriptWithRawResponse:
        return DeploymentsByScriptWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DeploymentsByScriptWithStreamingResponse:
        return DeploymentsByScriptWithStreamingResponse(self)

    def list(
        self,
        script_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DeploymentsByScriptListResponse:
        """
        List Deployments

        Args:
          account_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not script_id:
            raise ValueError(f"Expected a non-empty value for `script_id` but received {script_id!r}")
        return self._get(
            f"/accounts/{account_id}/workers/deployments/by-script/{script_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[DeploymentsByScriptListResponse], ResultWrapper[DeploymentsByScriptListResponse]),
        )

    def detail(
        self,
        deployment_id: str,
        *,
        account_id: str,
        script_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DeploymentsByScriptDetailResponse:
        """
        Get Deployment Detail

        Args:
          account_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not script_id:
            raise ValueError(f"Expected a non-empty value for `script_id` but received {script_id!r}")
        if not deployment_id:
            raise ValueError(f"Expected a non-empty value for `deployment_id` but received {deployment_id!r}")
        return self._get(
            f"/accounts/{account_id}/workers/deployments/by-script/{script_id}/detail/{deployment_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[DeploymentsByScriptDetailResponse], ResultWrapper[DeploymentsByScriptDetailResponse]),
        )


class AsyncDeploymentsByScript(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDeploymentsByScriptWithRawResponse:
        return AsyncDeploymentsByScriptWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDeploymentsByScriptWithStreamingResponse:
        return AsyncDeploymentsByScriptWithStreamingResponse(self)

    async def list(
        self,
        script_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DeploymentsByScriptListResponse:
        """
        List Deployments

        Args:
          account_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not script_id:
            raise ValueError(f"Expected a non-empty value for `script_id` but received {script_id!r}")
        return await self._get(
            f"/accounts/{account_id}/workers/deployments/by-script/{script_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[DeploymentsByScriptListResponse], ResultWrapper[DeploymentsByScriptListResponse]),
        )

    async def detail(
        self,
        deployment_id: str,
        *,
        account_id: str,
        script_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DeploymentsByScriptDetailResponse:
        """
        Get Deployment Detail

        Args:
          account_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not script_id:
            raise ValueError(f"Expected a non-empty value for `script_id` but received {script_id!r}")
        if not deployment_id:
            raise ValueError(f"Expected a non-empty value for `deployment_id` but received {deployment_id!r}")
        return await self._get(
            f"/accounts/{account_id}/workers/deployments/by-script/{script_id}/detail/{deployment_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[DeploymentsByScriptDetailResponse], ResultWrapper[DeploymentsByScriptDetailResponse]),
        )


class DeploymentsByScriptWithRawResponse:
    def __init__(self, deployments_by_script: DeploymentsByScript) -> None:
        self._deployments_by_script = deployments_by_script

        self.list = to_raw_response_wrapper(
            deployments_by_script.list,
        )
        self.detail = to_raw_response_wrapper(
            deployments_by_script.detail,
        )


class AsyncDeploymentsByScriptWithRawResponse:
    def __init__(self, deployments_by_script: AsyncDeploymentsByScript) -> None:
        self._deployments_by_script = deployments_by_script

        self.list = async_to_raw_response_wrapper(
            deployments_by_script.list,
        )
        self.detail = async_to_raw_response_wrapper(
            deployments_by_script.detail,
        )


class DeploymentsByScriptWithStreamingResponse:
    def __init__(self, deployments_by_script: DeploymentsByScript) -> None:
        self._deployments_by_script = deployments_by_script

        self.list = to_streamed_response_wrapper(
            deployments_by_script.list,
        )
        self.detail = to_streamed_response_wrapper(
            deployments_by_script.detail,
        )


class AsyncDeploymentsByScriptWithStreamingResponse:
    def __init__(self, deployments_by_script: AsyncDeploymentsByScript) -> None:
        self._deployments_by_script = deployments_by_script

        self.list = async_to_streamed_response_wrapper(
            deployments_by_script.list,
        )
        self.detail = async_to_streamed_response_wrapper(
            deployments_by_script.detail,
        )
