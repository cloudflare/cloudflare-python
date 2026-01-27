# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Iterable, cast

import httpx

from ..._types import Body, Query, Headers, NotGiven, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._wrappers import ResultWrapper
from ..._base_client import make_request_options
from ...types.ai_gateway import (
    dynamic_routing_create_params,
    dynamic_routing_update_params,
    dynamic_routing_create_version_params,
    dynamic_routing_create_deployment_params,
)
from ...types.ai_gateway.dynamic_routing_get_response import DynamicRoutingGetResponse
from ...types.ai_gateway.dynamic_routing_list_response import DynamicRoutingListResponse
from ...types.ai_gateway.dynamic_routing_create_response import DynamicRoutingCreateResponse
from ...types.ai_gateway.dynamic_routing_delete_response import DynamicRoutingDeleteResponse
from ...types.ai_gateway.dynamic_routing_update_response import DynamicRoutingUpdateResponse
from ...types.ai_gateway.dynamic_routing_get_version_response import DynamicRoutingGetVersionResponse
from ...types.ai_gateway.dynamic_routing_list_versions_response import DynamicRoutingListVersionsResponse
from ...types.ai_gateway.dynamic_routing_create_version_response import DynamicRoutingCreateVersionResponse
from ...types.ai_gateway.dynamic_routing_list_deployments_response import DynamicRoutingListDeploymentsResponse
from ...types.ai_gateway.dynamic_routing_create_deployment_response import DynamicRoutingCreateDeploymentResponse

__all__ = ["DynamicRoutingResource", "AsyncDynamicRoutingResource"]


class DynamicRoutingResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DynamicRoutingResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return DynamicRoutingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DynamicRoutingResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return DynamicRoutingResourceWithStreamingResponse(self)

    def create(
        self,
        gateway_id: str,
        *,
        account_id: str,
        elements: Iterable[dynamic_routing_create_params.Element],
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DynamicRoutingCreateResponse:
        """
        Create a new AI Gateway Dynamic Route.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not gateway_id:
            raise ValueError(f"Expected a non-empty value for `gateway_id` but received {gateway_id!r}")
        return self._post(
            f"/accounts/{account_id}/ai-gateway/gateways/{gateway_id}/routes",
            body=maybe_transform(
                {
                    "elements": elements,
                    "name": name,
                },
                dynamic_routing_create_params.DynamicRoutingCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[DynamicRoutingCreateResponse]._unwrapper,
            ),
            cast_to=cast(Type[DynamicRoutingCreateResponse], ResultWrapper[DynamicRoutingCreateResponse]),
        )

    def update(
        self,
        id: str,
        *,
        account_id: str,
        gateway_id: str,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DynamicRoutingUpdateResponse:
        """
        Update an AI Gateway Dynamic Route.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not gateway_id:
            raise ValueError(f"Expected a non-empty value for `gateway_id` but received {gateway_id!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            f"/accounts/{account_id}/ai-gateway/gateways/{gateway_id}/routes/{id}",
            body=maybe_transform({"name": name}, dynamic_routing_update_params.DynamicRoutingUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DynamicRoutingUpdateResponse,
        )

    def list(
        self,
        gateway_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DynamicRoutingListResponse:
        """
        List all AI Gateway Dynamic Routes.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not gateway_id:
            raise ValueError(f"Expected a non-empty value for `gateway_id` but received {gateway_id!r}")
        return self._get(
            f"/accounts/{account_id}/ai-gateway/gateways/{gateway_id}/routes",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DynamicRoutingListResponse,
        )

    def delete(
        self,
        id: str,
        *,
        account_id: str,
        gateway_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DynamicRoutingDeleteResponse:
        """
        Delete an AI Gateway Dynamic Route.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not gateway_id:
            raise ValueError(f"Expected a non-empty value for `gateway_id` but received {gateway_id!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._delete(
            f"/accounts/{account_id}/ai-gateway/gateways/{gateway_id}/routes/{id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[DynamicRoutingDeleteResponse]._unwrapper,
            ),
            cast_to=cast(Type[DynamicRoutingDeleteResponse], ResultWrapper[DynamicRoutingDeleteResponse]),
        )

    def create_deployment(
        self,
        id: str,
        *,
        account_id: str,
        gateway_id: str,
        comment: str,
        version_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DynamicRoutingCreateDeploymentResponse:
        """
        Create a new AI Gateway Dynamic Route Deployment.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not gateway_id:
            raise ValueError(f"Expected a non-empty value for `gateway_id` but received {gateway_id!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            f"/accounts/{account_id}/ai-gateway/gateways/{gateway_id}/routes/{id}/deployments",
            body=maybe_transform(
                {
                    "comment": comment,
                    "version_id": version_id,
                },
                dynamic_routing_create_deployment_params.DynamicRoutingCreateDeploymentParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[DynamicRoutingCreateDeploymentResponse]._unwrapper,
            ),
            cast_to=cast(
                Type[DynamicRoutingCreateDeploymentResponse], ResultWrapper[DynamicRoutingCreateDeploymentResponse]
            ),
        )

    def create_version(
        self,
        id: str,
        *,
        account_id: str,
        gateway_id: str,
        comment: str,
        elements: Iterable[dynamic_routing_create_version_params.Element],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DynamicRoutingCreateVersionResponse:
        """
        Create a new AI Gateway Dynamic Route Version.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not gateway_id:
            raise ValueError(f"Expected a non-empty value for `gateway_id` but received {gateway_id!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            f"/accounts/{account_id}/ai-gateway/gateways/{gateway_id}/routes/{id}/versions",
            body=maybe_transform(
                {
                    "comment": comment,
                    "elements": elements,
                },
                dynamic_routing_create_version_params.DynamicRoutingCreateVersionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[DynamicRoutingCreateVersionResponse]._unwrapper,
            ),
            cast_to=cast(Type[DynamicRoutingCreateVersionResponse], ResultWrapper[DynamicRoutingCreateVersionResponse]),
        )

    def get(
        self,
        id: str,
        *,
        account_id: str,
        gateway_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DynamicRoutingGetResponse:
        """
        Get an AI Gateway Dynamic Route.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not gateway_id:
            raise ValueError(f"Expected a non-empty value for `gateway_id` but received {gateway_id!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/accounts/{account_id}/ai-gateway/gateways/{gateway_id}/routes/{id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[DynamicRoutingGetResponse]._unwrapper,
            ),
            cast_to=cast(Type[DynamicRoutingGetResponse], ResultWrapper[DynamicRoutingGetResponse]),
        )

    def get_version(
        self,
        version_id: str,
        *,
        account_id: str,
        gateway_id: str,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DynamicRoutingGetVersionResponse:
        """
        Get an AI Gateway Dynamic Route Version.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not gateway_id:
            raise ValueError(f"Expected a non-empty value for `gateway_id` but received {gateway_id!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not version_id:
            raise ValueError(f"Expected a non-empty value for `version_id` but received {version_id!r}")
        return self._get(
            f"/accounts/{account_id}/ai-gateway/gateways/{gateway_id}/routes/{id}/versions/{version_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[DynamicRoutingGetVersionResponse]._unwrapper,
            ),
            cast_to=cast(Type[DynamicRoutingGetVersionResponse], ResultWrapper[DynamicRoutingGetVersionResponse]),
        )

    def list_deployments(
        self,
        id: str,
        *,
        account_id: str,
        gateway_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DynamicRoutingListDeploymentsResponse:
        """
        List all AI Gateway Dynamic Route Deployments.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not gateway_id:
            raise ValueError(f"Expected a non-empty value for `gateway_id` but received {gateway_id!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/accounts/{account_id}/ai-gateway/gateways/{gateway_id}/routes/{id}/deployments",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DynamicRoutingListDeploymentsResponse,
        )

    def list_versions(
        self,
        id: str,
        *,
        account_id: str,
        gateway_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DynamicRoutingListVersionsResponse:
        """
        List all AI Gateway Dynamic Route Versions.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not gateway_id:
            raise ValueError(f"Expected a non-empty value for `gateway_id` but received {gateway_id!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/accounts/{account_id}/ai-gateway/gateways/{gateway_id}/routes/{id}/versions",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DynamicRoutingListVersionsResponse,
        )


class AsyncDynamicRoutingResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDynamicRoutingResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDynamicRoutingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDynamicRoutingResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncDynamicRoutingResourceWithStreamingResponse(self)

    async def create(
        self,
        gateway_id: str,
        *,
        account_id: str,
        elements: Iterable[dynamic_routing_create_params.Element],
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DynamicRoutingCreateResponse:
        """
        Create a new AI Gateway Dynamic Route.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not gateway_id:
            raise ValueError(f"Expected a non-empty value for `gateway_id` but received {gateway_id!r}")
        return await self._post(
            f"/accounts/{account_id}/ai-gateway/gateways/{gateway_id}/routes",
            body=await async_maybe_transform(
                {
                    "elements": elements,
                    "name": name,
                },
                dynamic_routing_create_params.DynamicRoutingCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[DynamicRoutingCreateResponse]._unwrapper,
            ),
            cast_to=cast(Type[DynamicRoutingCreateResponse], ResultWrapper[DynamicRoutingCreateResponse]),
        )

    async def update(
        self,
        id: str,
        *,
        account_id: str,
        gateway_id: str,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DynamicRoutingUpdateResponse:
        """
        Update an AI Gateway Dynamic Route.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not gateway_id:
            raise ValueError(f"Expected a non-empty value for `gateway_id` but received {gateway_id!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            f"/accounts/{account_id}/ai-gateway/gateways/{gateway_id}/routes/{id}",
            body=await async_maybe_transform({"name": name}, dynamic_routing_update_params.DynamicRoutingUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DynamicRoutingUpdateResponse,
        )

    async def list(
        self,
        gateway_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DynamicRoutingListResponse:
        """
        List all AI Gateway Dynamic Routes.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not gateway_id:
            raise ValueError(f"Expected a non-empty value for `gateway_id` but received {gateway_id!r}")
        return await self._get(
            f"/accounts/{account_id}/ai-gateway/gateways/{gateway_id}/routes",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DynamicRoutingListResponse,
        )

    async def delete(
        self,
        id: str,
        *,
        account_id: str,
        gateway_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DynamicRoutingDeleteResponse:
        """
        Delete an AI Gateway Dynamic Route.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not gateway_id:
            raise ValueError(f"Expected a non-empty value for `gateway_id` but received {gateway_id!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._delete(
            f"/accounts/{account_id}/ai-gateway/gateways/{gateway_id}/routes/{id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[DynamicRoutingDeleteResponse]._unwrapper,
            ),
            cast_to=cast(Type[DynamicRoutingDeleteResponse], ResultWrapper[DynamicRoutingDeleteResponse]),
        )

    async def create_deployment(
        self,
        id: str,
        *,
        account_id: str,
        gateway_id: str,
        comment: str,
        version_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DynamicRoutingCreateDeploymentResponse:
        """
        Create a new AI Gateway Dynamic Route Deployment.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not gateway_id:
            raise ValueError(f"Expected a non-empty value for `gateway_id` but received {gateway_id!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            f"/accounts/{account_id}/ai-gateway/gateways/{gateway_id}/routes/{id}/deployments",
            body=await async_maybe_transform(
                {
                    "comment": comment,
                    "version_id": version_id,
                },
                dynamic_routing_create_deployment_params.DynamicRoutingCreateDeploymentParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[DynamicRoutingCreateDeploymentResponse]._unwrapper,
            ),
            cast_to=cast(
                Type[DynamicRoutingCreateDeploymentResponse], ResultWrapper[DynamicRoutingCreateDeploymentResponse]
            ),
        )

    async def create_version(
        self,
        id: str,
        *,
        account_id: str,
        gateway_id: str,
        comment: str,
        elements: Iterable[dynamic_routing_create_version_params.Element],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DynamicRoutingCreateVersionResponse:
        """
        Create a new AI Gateway Dynamic Route Version.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not gateway_id:
            raise ValueError(f"Expected a non-empty value for `gateway_id` but received {gateway_id!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            f"/accounts/{account_id}/ai-gateway/gateways/{gateway_id}/routes/{id}/versions",
            body=await async_maybe_transform(
                {
                    "comment": comment,
                    "elements": elements,
                },
                dynamic_routing_create_version_params.DynamicRoutingCreateVersionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[DynamicRoutingCreateVersionResponse]._unwrapper,
            ),
            cast_to=cast(Type[DynamicRoutingCreateVersionResponse], ResultWrapper[DynamicRoutingCreateVersionResponse]),
        )

    async def get(
        self,
        id: str,
        *,
        account_id: str,
        gateway_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DynamicRoutingGetResponse:
        """
        Get an AI Gateway Dynamic Route.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not gateway_id:
            raise ValueError(f"Expected a non-empty value for `gateway_id` but received {gateway_id!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/accounts/{account_id}/ai-gateway/gateways/{gateway_id}/routes/{id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[DynamicRoutingGetResponse]._unwrapper,
            ),
            cast_to=cast(Type[DynamicRoutingGetResponse], ResultWrapper[DynamicRoutingGetResponse]),
        )

    async def get_version(
        self,
        version_id: str,
        *,
        account_id: str,
        gateway_id: str,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DynamicRoutingGetVersionResponse:
        """
        Get an AI Gateway Dynamic Route Version.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not gateway_id:
            raise ValueError(f"Expected a non-empty value for `gateway_id` but received {gateway_id!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not version_id:
            raise ValueError(f"Expected a non-empty value for `version_id` but received {version_id!r}")
        return await self._get(
            f"/accounts/{account_id}/ai-gateway/gateways/{gateway_id}/routes/{id}/versions/{version_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[DynamicRoutingGetVersionResponse]._unwrapper,
            ),
            cast_to=cast(Type[DynamicRoutingGetVersionResponse], ResultWrapper[DynamicRoutingGetVersionResponse]),
        )

    async def list_deployments(
        self,
        id: str,
        *,
        account_id: str,
        gateway_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DynamicRoutingListDeploymentsResponse:
        """
        List all AI Gateway Dynamic Route Deployments.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not gateway_id:
            raise ValueError(f"Expected a non-empty value for `gateway_id` but received {gateway_id!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/accounts/{account_id}/ai-gateway/gateways/{gateway_id}/routes/{id}/deployments",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DynamicRoutingListDeploymentsResponse,
        )

    async def list_versions(
        self,
        id: str,
        *,
        account_id: str,
        gateway_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DynamicRoutingListVersionsResponse:
        """
        List all AI Gateway Dynamic Route Versions.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not gateway_id:
            raise ValueError(f"Expected a non-empty value for `gateway_id` but received {gateway_id!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/accounts/{account_id}/ai-gateway/gateways/{gateway_id}/routes/{id}/versions",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DynamicRoutingListVersionsResponse,
        )


class DynamicRoutingResourceWithRawResponse:
    def __init__(self, dynamic_routing: DynamicRoutingResource) -> None:
        self._dynamic_routing = dynamic_routing

        self.create = to_raw_response_wrapper(
            dynamic_routing.create,
        )
        self.update = to_raw_response_wrapper(
            dynamic_routing.update,
        )
        self.list = to_raw_response_wrapper(
            dynamic_routing.list,
        )
        self.delete = to_raw_response_wrapper(
            dynamic_routing.delete,
        )
        self.create_deployment = to_raw_response_wrapper(
            dynamic_routing.create_deployment,
        )
        self.create_version = to_raw_response_wrapper(
            dynamic_routing.create_version,
        )
        self.get = to_raw_response_wrapper(
            dynamic_routing.get,
        )
        self.get_version = to_raw_response_wrapper(
            dynamic_routing.get_version,
        )
        self.list_deployments = to_raw_response_wrapper(
            dynamic_routing.list_deployments,
        )
        self.list_versions = to_raw_response_wrapper(
            dynamic_routing.list_versions,
        )


class AsyncDynamicRoutingResourceWithRawResponse:
    def __init__(self, dynamic_routing: AsyncDynamicRoutingResource) -> None:
        self._dynamic_routing = dynamic_routing

        self.create = async_to_raw_response_wrapper(
            dynamic_routing.create,
        )
        self.update = async_to_raw_response_wrapper(
            dynamic_routing.update,
        )
        self.list = async_to_raw_response_wrapper(
            dynamic_routing.list,
        )
        self.delete = async_to_raw_response_wrapper(
            dynamic_routing.delete,
        )
        self.create_deployment = async_to_raw_response_wrapper(
            dynamic_routing.create_deployment,
        )
        self.create_version = async_to_raw_response_wrapper(
            dynamic_routing.create_version,
        )
        self.get = async_to_raw_response_wrapper(
            dynamic_routing.get,
        )
        self.get_version = async_to_raw_response_wrapper(
            dynamic_routing.get_version,
        )
        self.list_deployments = async_to_raw_response_wrapper(
            dynamic_routing.list_deployments,
        )
        self.list_versions = async_to_raw_response_wrapper(
            dynamic_routing.list_versions,
        )


class DynamicRoutingResourceWithStreamingResponse:
    def __init__(self, dynamic_routing: DynamicRoutingResource) -> None:
        self._dynamic_routing = dynamic_routing

        self.create = to_streamed_response_wrapper(
            dynamic_routing.create,
        )
        self.update = to_streamed_response_wrapper(
            dynamic_routing.update,
        )
        self.list = to_streamed_response_wrapper(
            dynamic_routing.list,
        )
        self.delete = to_streamed_response_wrapper(
            dynamic_routing.delete,
        )
        self.create_deployment = to_streamed_response_wrapper(
            dynamic_routing.create_deployment,
        )
        self.create_version = to_streamed_response_wrapper(
            dynamic_routing.create_version,
        )
        self.get = to_streamed_response_wrapper(
            dynamic_routing.get,
        )
        self.get_version = to_streamed_response_wrapper(
            dynamic_routing.get_version,
        )
        self.list_deployments = to_streamed_response_wrapper(
            dynamic_routing.list_deployments,
        )
        self.list_versions = to_streamed_response_wrapper(
            dynamic_routing.list_versions,
        )


class AsyncDynamicRoutingResourceWithStreamingResponse:
    def __init__(self, dynamic_routing: AsyncDynamicRoutingResource) -> None:
        self._dynamic_routing = dynamic_routing

        self.create = async_to_streamed_response_wrapper(
            dynamic_routing.create,
        )
        self.update = async_to_streamed_response_wrapper(
            dynamic_routing.update,
        )
        self.list = async_to_streamed_response_wrapper(
            dynamic_routing.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            dynamic_routing.delete,
        )
        self.create_deployment = async_to_streamed_response_wrapper(
            dynamic_routing.create_deployment,
        )
        self.create_version = async_to_streamed_response_wrapper(
            dynamic_routing.create_version,
        )
        self.get = async_to_streamed_response_wrapper(
            dynamic_routing.get,
        )
        self.get_version = async_to_streamed_response_wrapper(
            dynamic_routing.get_version,
        )
        self.list_deployments = async_to_streamed_response_wrapper(
            dynamic_routing.list_deployments,
        )
        self.list_versions = async_to_streamed_response_wrapper(
            dynamic_routing.list_versions,
        )
