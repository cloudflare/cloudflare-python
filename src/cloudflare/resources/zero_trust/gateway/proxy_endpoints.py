# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, List, Type, Optional, cast

import httpx

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
from ...._base_client import (
    make_request_options,
)
from ....types.zero_trust.gateway import (
    ProxyEndpointListResponse,
    ProxyEndpointDeleteResponse,
    ZeroTrustGatewayProxyEndpoints,
    proxy_endpoint_edit_params,
    proxy_endpoint_create_params,
)

__all__ = ["ProxyEndpoints", "AsyncProxyEndpoints"]


class ProxyEndpoints(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ProxyEndpointsWithRawResponse:
        return ProxyEndpointsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ProxyEndpointsWithStreamingResponse:
        return ProxyEndpointsWithStreamingResponse(self)

    def create(
        self,
        *,
        account_id: str,
        ips: List[str],
        name: str,
        subdomain: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ZeroTrustGatewayProxyEndpoints:
        """
        Creates a new Zero Trust Gateway proxy endpoint.

        Args:
          ips: A list of CIDRs to restrict ingress connections.

          name: The name of the proxy endpoint.

          subdomain: The subdomain to be used as the destination in the proxy client.

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
                    "subdomain": subdomain,
                },
                proxy_endpoint_create_params.ProxyEndpointCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[ZeroTrustGatewayProxyEndpoints], ResultWrapper[ZeroTrustGatewayProxyEndpoints]),
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
    ) -> Optional[ProxyEndpointListResponse]:
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
        return self._get(
            f"/accounts/{account_id}/gateway/proxy_endpoints",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[ProxyEndpointListResponse]], ResultWrapper[ProxyEndpointListResponse]),
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
    ) -> ProxyEndpointDeleteResponse:
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
        return cast(
            ProxyEndpointDeleteResponse,
            self._delete(
                f"/accounts/{account_id}/gateway/proxy_endpoints/{proxy_endpoint_id}",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[ProxyEndpointDeleteResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def edit(
        self,
        proxy_endpoint_id: str,
        *,
        account_id: str,
        ips: List[str] | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        subdomain: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ZeroTrustGatewayProxyEndpoints:
        """
        Updates a configured Zero Trust Gateway proxy endpoint.

        Args:
          ips: A list of CIDRs to restrict ingress connections.

          name: The name of the proxy endpoint.

          subdomain: The subdomain to be used as the destination in the proxy client.

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
                    "subdomain": subdomain,
                },
                proxy_endpoint_edit_params.ProxyEndpointEditParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[ZeroTrustGatewayProxyEndpoints], ResultWrapper[ZeroTrustGatewayProxyEndpoints]),
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
    ) -> ZeroTrustGatewayProxyEndpoints:
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
        if not proxy_endpoint_id:
            raise ValueError(f"Expected a non-empty value for `proxy_endpoint_id` but received {proxy_endpoint_id!r}")
        return self._get(
            f"/accounts/{account_id}/gateway/proxy_endpoints/{proxy_endpoint_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[ZeroTrustGatewayProxyEndpoints], ResultWrapper[ZeroTrustGatewayProxyEndpoints]),
        )


class AsyncProxyEndpoints(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncProxyEndpointsWithRawResponse:
        return AsyncProxyEndpointsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncProxyEndpointsWithStreamingResponse:
        return AsyncProxyEndpointsWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_id: str,
        ips: List[str],
        name: str,
        subdomain: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ZeroTrustGatewayProxyEndpoints:
        """
        Creates a new Zero Trust Gateway proxy endpoint.

        Args:
          ips: A list of CIDRs to restrict ingress connections.

          name: The name of the proxy endpoint.

          subdomain: The subdomain to be used as the destination in the proxy client.

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
                    "subdomain": subdomain,
                },
                proxy_endpoint_create_params.ProxyEndpointCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[ZeroTrustGatewayProxyEndpoints], ResultWrapper[ZeroTrustGatewayProxyEndpoints]),
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
    ) -> Optional[ProxyEndpointListResponse]:
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
        return await self._get(
            f"/accounts/{account_id}/gateway/proxy_endpoints",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[ProxyEndpointListResponse]], ResultWrapper[ProxyEndpointListResponse]),
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
    ) -> ProxyEndpointDeleteResponse:
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
        return cast(
            ProxyEndpointDeleteResponse,
            await self._delete(
                f"/accounts/{account_id}/gateway/proxy_endpoints/{proxy_endpoint_id}",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[ProxyEndpointDeleteResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def edit(
        self,
        proxy_endpoint_id: str,
        *,
        account_id: str,
        ips: List[str] | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        subdomain: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ZeroTrustGatewayProxyEndpoints:
        """
        Updates a configured Zero Trust Gateway proxy endpoint.

        Args:
          ips: A list of CIDRs to restrict ingress connections.

          name: The name of the proxy endpoint.

          subdomain: The subdomain to be used as the destination in the proxy client.

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
                    "subdomain": subdomain,
                },
                proxy_endpoint_edit_params.ProxyEndpointEditParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[ZeroTrustGatewayProxyEndpoints], ResultWrapper[ZeroTrustGatewayProxyEndpoints]),
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
    ) -> ZeroTrustGatewayProxyEndpoints:
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
        if not proxy_endpoint_id:
            raise ValueError(f"Expected a non-empty value for `proxy_endpoint_id` but received {proxy_endpoint_id!r}")
        return await self._get(
            f"/accounts/{account_id}/gateway/proxy_endpoints/{proxy_endpoint_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[ZeroTrustGatewayProxyEndpoints], ResultWrapper[ZeroTrustGatewayProxyEndpoints]),
        )


class ProxyEndpointsWithRawResponse:
    def __init__(self, proxy_endpoints: ProxyEndpoints) -> None:
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


class AsyncProxyEndpointsWithRawResponse:
    def __init__(self, proxy_endpoints: AsyncProxyEndpoints) -> None:
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


class ProxyEndpointsWithStreamingResponse:
    def __init__(self, proxy_endpoints: ProxyEndpoints) -> None:
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


class AsyncProxyEndpointsWithStreamingResponse:
    def __init__(self, proxy_endpoints: AsyncProxyEndpoints) -> None:
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
