# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._compat import cached_property

from ....types.workers.scripts.deployment_create_response import DeploymentCreateResponse

from ...._wrappers import ResultWrapper

from ...._utils import maybe_transform, async_maybe_transform

from typing import Optional, Type, Iterable

from ...._base_client import make_request_options

from typing_extensions import Literal

from ....types.workers.scripts.deployment_param import DeploymentParam

from ....types.workers.scripts.deployment_get_response import DeploymentGetResponse

from ...._response import to_raw_response_wrapper, async_to_raw_response_wrapper, to_streamed_response_wrapper, async_to_streamed_response_wrapper

from ....types.workers.scripts import deployment_create_params

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ...._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ...._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ...._resource import SyncAPIResource, AsyncAPIResource
from ....types import shared_params
from ....types.workers.scripts import deployment_create_params
from ....types.workers.scripts import Deployment
from typing import cast
from typing import cast
from typing import cast
from typing import cast

__all__ = ["DeploymentsResource", "AsyncDeploymentsResource"]

class DeploymentsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DeploymentsResourceWithRawResponse:
        return DeploymentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DeploymentsResourceWithStreamingResponse:
        return DeploymentsResourceWithStreamingResponse(self)

    def create(self,
    script_name: str,
    *,
    account_id: str,
    strategy: Literal["percentage"],
    versions: Iterable[deployment_create_params.Version],
    force: bool | NotGiven = NOT_GIVEN,
    annotations: DeploymentParam | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Optional[DeploymentCreateResponse]:
        """
        Deployments configure how
        [Worker Versions](https://developers.cloudflare.com/api/operations/worker-versions-list-versions)
        are deployed to traffic. A deployment can consist of one or two versions of a
        Worker.

        Args:
          account_id: Identifier

          script_name: Name of the script.

          force: If set to true, the deployment will be created even if normally blocked by
              something such rolling back to an older version when a secret has changed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
          raise ValueError(
            f'Expected a non-empty value for `account_id` but received {account_id!r}'
          )
        if not script_name:
          raise ValueError(
            f'Expected a non-empty value for `script_name` but received {script_name!r}'
          )
        return self._post(
            f"/accounts/{account_id}/workers/scripts/{script_name}/deployments",
            body=maybe_transform({
                "strategy": strategy,
                "versions": versions,
                "annotations": annotations,
            }, deployment_create_params.DeploymentCreateParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, query=maybe_transform({
                "force": force
            }, deployment_create_params.DeploymentCreateParams), post_parser=ResultWrapper[Optional[DeploymentCreateResponse]]._unwrapper),
            cast_to=cast(Type[Optional[DeploymentCreateResponse]], ResultWrapper[DeploymentCreateResponse]),
        )

    def get(self,
    script_name: str,
    *,
    account_id: str,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Optional[DeploymentGetResponse]:
        """List of Worker Deployments.

        The first deployment in the list is the latest
        deployment actively serving traffic.

        Args:
          account_id: Identifier

          script_name: Name of the script.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
          raise ValueError(
            f'Expected a non-empty value for `account_id` but received {account_id!r}'
          )
        if not script_name:
          raise ValueError(
            f'Expected a non-empty value for `script_name` but received {script_name!r}'
          )
        return self._get(
            f"/accounts/{account_id}/workers/scripts/{script_name}/deployments",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[Optional[DeploymentGetResponse]]._unwrapper),
            cast_to=cast(Type[Optional[DeploymentGetResponse]], ResultWrapper[DeploymentGetResponse]),
        )

class AsyncDeploymentsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDeploymentsResourceWithRawResponse:
        return AsyncDeploymentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDeploymentsResourceWithStreamingResponse:
        return AsyncDeploymentsResourceWithStreamingResponse(self)

    async def create(self,
    script_name: str,
    *,
    account_id: str,
    strategy: Literal["percentage"],
    versions: Iterable[deployment_create_params.Version],
    force: bool | NotGiven = NOT_GIVEN,
    annotations: DeploymentParam | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Optional[DeploymentCreateResponse]:
        """
        Deployments configure how
        [Worker Versions](https://developers.cloudflare.com/api/operations/worker-versions-list-versions)
        are deployed to traffic. A deployment can consist of one or two versions of a
        Worker.

        Args:
          account_id: Identifier

          script_name: Name of the script.

          force: If set to true, the deployment will be created even if normally blocked by
              something such rolling back to an older version when a secret has changed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
          raise ValueError(
            f'Expected a non-empty value for `account_id` but received {account_id!r}'
          )
        if not script_name:
          raise ValueError(
            f'Expected a non-empty value for `script_name` but received {script_name!r}'
          )
        return await self._post(
            f"/accounts/{account_id}/workers/scripts/{script_name}/deployments",
            body=await async_maybe_transform({
                "strategy": strategy,
                "versions": versions,
                "annotations": annotations,
            }, deployment_create_params.DeploymentCreateParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, query=await async_maybe_transform({
                "force": force
            }, deployment_create_params.DeploymentCreateParams), post_parser=ResultWrapper[Optional[DeploymentCreateResponse]]._unwrapper),
            cast_to=cast(Type[Optional[DeploymentCreateResponse]], ResultWrapper[DeploymentCreateResponse]),
        )

    async def get(self,
    script_name: str,
    *,
    account_id: str,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Optional[DeploymentGetResponse]:
        """List of Worker Deployments.

        The first deployment in the list is the latest
        deployment actively serving traffic.

        Args:
          account_id: Identifier

          script_name: Name of the script.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
          raise ValueError(
            f'Expected a non-empty value for `account_id` but received {account_id!r}'
          )
        if not script_name:
          raise ValueError(
            f'Expected a non-empty value for `script_name` but received {script_name!r}'
          )
        return await self._get(
            f"/accounts/{account_id}/workers/scripts/{script_name}/deployments",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[Optional[DeploymentGetResponse]]._unwrapper),
            cast_to=cast(Type[Optional[DeploymentGetResponse]], ResultWrapper[DeploymentGetResponse]),
        )

class DeploymentsResourceWithRawResponse:
    def __init__(self, deployments: DeploymentsResource) -> None:
        self._deployments = deployments

        self.create = to_raw_response_wrapper(
            deployments.create,
        )
        self.get = to_raw_response_wrapper(
            deployments.get,
        )

class AsyncDeploymentsResourceWithRawResponse:
    def __init__(self, deployments: AsyncDeploymentsResource) -> None:
        self._deployments = deployments

        self.create = async_to_raw_response_wrapper(
            deployments.create,
        )
        self.get = async_to_raw_response_wrapper(
            deployments.get,
        )

class DeploymentsResourceWithStreamingResponse:
    def __init__(self, deployments: DeploymentsResource) -> None:
        self._deployments = deployments

        self.create = to_streamed_response_wrapper(
            deployments.create,
        )
        self.get = to_streamed_response_wrapper(
            deployments.get,
        )

class AsyncDeploymentsResourceWithStreamingResponse:
    def __init__(self, deployments: AsyncDeploymentsResource) -> None:
        self._deployments = deployments

        self.create = async_to_streamed_response_wrapper(
            deployments.create,
        )
        self.get = async_to_streamed_response_wrapper(
            deployments.get,
        )