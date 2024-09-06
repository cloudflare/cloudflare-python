# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._compat import cached_property

from ....types.zero_trust.gateway.proxy_endpoint import ProxyEndpoint

from ...._wrappers import ResultWrapper

from ...._utils import maybe_transform, async_maybe_transform

from typing import Optional, Type, List

from ...._base_client import make_request_options

from ....types.zero_trust.gateway.gateway_ips import GatewayIPs

from ....types.zero_trust.gateway.proxy_endpoint_get_response import ProxyEndpointGetResponse

from ...._response import (
    to_raw_response_wrapper,
    async_to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_streamed_response_wrapper,
)

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ...._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ...._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ...._resource import SyncAPIResource, AsyncAPIResource
from ....types import shared_params
from ....types.zero_trust.gateway import proxy_endpoint_create_params
from ....types.zero_trust.gateway import proxy_endpoint_edit_params
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast

__all__ = ["ProxyEndpointsResource", "AsyncProxyEndpointsResource"]


class ProxyEndpointsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ProxyEndpointsResourceWithRawResponse:
        return ProxyEndpointsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ProxyEndpointsResourceWithStreamingResponse:
        return ProxyEndpointsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        account_id: str,
        ips: List[GatewayIPs],
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ProxyEndpoint]:
        """
        Creates a new Zero Trust Gateway proxy endpoint.

        Args:
          ips: A list of CIDRs to restrict ingress connections.

          name: The name of the proxy endpoint.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._post(
            f"/accounts/{account_id}/gateway/proxy_endpoints",
            body=maybe_transform(
                {
                    "ips": ips,
                    "name": name,
                },
                proxy_endpoint_create_params.ProxyEndpointCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[ProxyEndpoint]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[ProxyEndpoint]], ResultWrapper[ProxyEndpoint]),
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
    ) -> Optional[ProxyEndpoint]:
        """
        Fetches all Zero Trust Gateway proxy endpoints for an account.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get(
            f"/accounts/{account_id}/gateway/proxy_endpoints",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[ProxyEndpoint]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[ProxyEndpoint]], ResultWrapper[ProxyEndpoint]),
        )

    def delete(
        self,
        proxy_endpoint_id: str,
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
        Deletes a configured Zero Trust Gateway proxy endpoint.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not proxy_endpoint_id:
            raise ValueError(f"Expected a non-empty value for `proxy_endpoint_id` but received {proxy_endpoint_id!r}")
        return self._delete(
            f"/accounts/{account_id}/gateway/proxy_endpoints/{proxy_endpoint_id}",
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
        proxy_endpoint_id: str,
        *,
        account_id: str,
        ips: List[GatewayIPs] | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ProxyEndpoint]:
        """
        Updates a configured Zero Trust Gateway proxy endpoint.

        Args:
          ips: A list of CIDRs to restrict ingress connections.

          name: The name of the proxy endpoint.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not proxy_endpoint_id:
            raise ValueError(f"Expected a non-empty value for `proxy_endpoint_id` but received {proxy_endpoint_id!r}")
        return self._patch(
            f"/accounts/{account_id}/gateway/proxy_endpoints/{proxy_endpoint_id}",
            body=maybe_transform(
                {
                    "ips": ips,
                    "name": name,
                },
                proxy_endpoint_edit_params.ProxyEndpointEditParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[ProxyEndpoint]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[ProxyEndpoint]], ResultWrapper[ProxyEndpoint]),
        )

    def get(
        self,
        proxy_endpoint_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ProxyEndpointGetResponse]:
        """
        Fetches a single Zero Trust Gateway proxy endpoint.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not proxy_endpoint_id:
            raise ValueError(f"Expected a non-empty value for `proxy_endpoint_id` but received {proxy_endpoint_id!r}")
        return self._get(
            f"/accounts/{account_id}/gateway/proxy_endpoints/{proxy_endpoint_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[ProxyEndpointGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[ProxyEndpointGetResponse]], ResultWrapper[ProxyEndpointGetResponse]),
        )


class AsyncProxyEndpointsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncProxyEndpointsResourceWithRawResponse:
        return AsyncProxyEndpointsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncProxyEndpointsResourceWithStreamingResponse:
        return AsyncProxyEndpointsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_id: str,
        ips: List[GatewayIPs],
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ProxyEndpoint]:
        """
        Creates a new Zero Trust Gateway proxy endpoint.

        Args:
          ips: A list of CIDRs to restrict ingress connections.

          name: The name of the proxy endpoint.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._post(
            f"/accounts/{account_id}/gateway/proxy_endpoints",
            body=await async_maybe_transform(
                {
                    "ips": ips,
                    "name": name,
                },
                proxy_endpoint_create_params.ProxyEndpointCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[ProxyEndpoint]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[ProxyEndpoint]], ResultWrapper[ProxyEndpoint]),
        )

    async def list(
        self,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ProxyEndpoint]:
        """
        Fetches all Zero Trust Gateway proxy endpoints for an account.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._get(
            f"/accounts/{account_id}/gateway/proxy_endpoints",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[ProxyEndpoint]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[ProxyEndpoint]], ResultWrapper[ProxyEndpoint]),
        )

    async def delete(
        self,
        proxy_endpoint_id: str,
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
        Deletes a configured Zero Trust Gateway proxy endpoint.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not proxy_endpoint_id:
            raise ValueError(f"Expected a non-empty value for `proxy_endpoint_id` but received {proxy_endpoint_id!r}")
        return await self._delete(
            f"/accounts/{account_id}/gateway/proxy_endpoints/{proxy_endpoint_id}",
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
        proxy_endpoint_id: str,
        *,
        account_id: str,
        ips: List[GatewayIPs] | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ProxyEndpoint]:
        """
        Updates a configured Zero Trust Gateway proxy endpoint.

        Args:
          ips: A list of CIDRs to restrict ingress connections.

          name: The name of the proxy endpoint.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not proxy_endpoint_id:
            raise ValueError(f"Expected a non-empty value for `proxy_endpoint_id` but received {proxy_endpoint_id!r}")
        return await self._patch(
            f"/accounts/{account_id}/gateway/proxy_endpoints/{proxy_endpoint_id}",
            body=await async_maybe_transform(
                {
                    "ips": ips,
                    "name": name,
                },
                proxy_endpoint_edit_params.ProxyEndpointEditParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[ProxyEndpoint]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[ProxyEndpoint]], ResultWrapper[ProxyEndpoint]),
        )

    async def get(
        self,
        proxy_endpoint_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ProxyEndpointGetResponse]:
        """
        Fetches a single Zero Trust Gateway proxy endpoint.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not proxy_endpoint_id:
            raise ValueError(f"Expected a non-empty value for `proxy_endpoint_id` but received {proxy_endpoint_id!r}")
        return await self._get(
            f"/accounts/{account_id}/gateway/proxy_endpoints/{proxy_endpoint_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[ProxyEndpointGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[ProxyEndpointGetResponse]], ResultWrapper[ProxyEndpointGetResponse]),
        )


class ProxyEndpointsResourceWithRawResponse:
    def __init__(self, proxy_endpoints: ProxyEndpointsResource) -> None:
        self._proxy_endpoints = proxy_endpoints

        self.create = to_raw_response_wrapper(
            proxy_endpoints.create,
        )
        self.list = to_raw_response_wrapper(
            proxy_endpoints.list,
        )
        self.delete = to_raw_response_wrapper(
            proxy_endpoints.delete,
        )
        self.edit = to_raw_response_wrapper(
            proxy_endpoints.edit,
        )
        self.get = to_raw_response_wrapper(
            proxy_endpoints.get,
        )


class AsyncProxyEndpointsResourceWithRawResponse:
    def __init__(self, proxy_endpoints: AsyncProxyEndpointsResource) -> None:
        self._proxy_endpoints = proxy_endpoints

        self.create = async_to_raw_response_wrapper(
            proxy_endpoints.create,
        )
        self.list = async_to_raw_response_wrapper(
            proxy_endpoints.list,
        )
        self.delete = async_to_raw_response_wrapper(
            proxy_endpoints.delete,
        )
        self.edit = async_to_raw_response_wrapper(
            proxy_endpoints.edit,
        )
        self.get = async_to_raw_response_wrapper(
            proxy_endpoints.get,
        )


class ProxyEndpointsResourceWithStreamingResponse:
    def __init__(self, proxy_endpoints: ProxyEndpointsResource) -> None:
        self._proxy_endpoints = proxy_endpoints

        self.create = to_streamed_response_wrapper(
            proxy_endpoints.create,
        )
        self.list = to_streamed_response_wrapper(
            proxy_endpoints.list,
        )
        self.delete = to_streamed_response_wrapper(
            proxy_endpoints.delete,
        )
        self.edit = to_streamed_response_wrapper(
            proxy_endpoints.edit,
        )
        self.get = to_streamed_response_wrapper(
            proxy_endpoints.get,
        )


class AsyncProxyEndpointsResourceWithStreamingResponse:
    def __init__(self, proxy_endpoints: AsyncProxyEndpointsResource) -> None:
        self._proxy_endpoints = proxy_endpoints

        self.create = async_to_streamed_response_wrapper(
            proxy_endpoints.create,
        )
        self.list = async_to_streamed_response_wrapper(
            proxy_endpoints.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            proxy_endpoints.delete,
        )
        self.edit = async_to_streamed_response_wrapper(
            proxy_endpoints.edit,
        )
        self.get = async_to_streamed_response_wrapper(
            proxy_endpoints.get,
        )
