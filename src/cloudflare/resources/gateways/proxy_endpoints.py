# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Any, List, Type, Optional, cast

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._wrappers import ResultWrapper
from ..._base_client import (
    make_request_options,
)
from ...types.gateways import (
    ProxyEndpointGetResponse,
    ProxyEndpointListResponse,
    ProxyEndpointDeleteResponse,
    ProxyEndpointUpdateResponse,
    ProxyEndpointZeroTrustGatewayProxyEndpointsListProxyEndpointsResponse,
    ProxyEndpointZeroTrustGatewayProxyEndpointsCreateProxyEndpointResponse,
    proxy_endpoint_update_params,
    proxy_endpoint_zero_trust_gateway_proxy_endpoints_create_proxy_endpoint_params,
)

__all__ = ["ProxyEndpoints", "AsyncProxyEndpoints"]


class ProxyEndpoints(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ProxyEndpointsWithRawResponse:
        return ProxyEndpointsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ProxyEndpointsWithStreamingResponse:
        return ProxyEndpointsWithStreamingResponse(self)

    def update(
        self,
        proxy_endpoint_id: object,
        *,
        account_id: object,
        ips: List[str] | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        subdomain: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ProxyEndpointUpdateResponse:
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
        return self._patch(
            f"/accounts/{account_id}/gateway/proxy_endpoints/{proxy_endpoint_id}",
            body=maybe_transform(
                {
                    "ips": ips,
                    "name": name,
                    "subdomain": subdomain,
                },
                proxy_endpoint_update_params.ProxyEndpointUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[ProxyEndpointUpdateResponse], ResultWrapper[ProxyEndpointUpdateResponse]),
        )

    def list(
        self,
        proxy_endpoint_id: object,
        *,
        account_id: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ProxyEndpointListResponse:
        """
        Fetches all Zero Trust Gateway proxy endpoints for an account.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/accounts/{account_id}/gateway/proxy_endpoints/{proxy_endpoint_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[ProxyEndpointListResponse], ResultWrapper[ProxyEndpointListResponse]),
        )

    def delete(
        self,
        proxy_endpoint_id: object,
        *,
        account_id: object,
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

    def get(
        self,
        proxy_endpoint_id: object,
        *,
        account_id: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ProxyEndpointGetResponse:
        """
        Fetches all Zero Trust Gateway proxy endpoints for an account.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/accounts/{account_id}/gateway/proxy_endpoints/{proxy_endpoint_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[ProxyEndpointGetResponse], ResultWrapper[ProxyEndpointGetResponse]),
        )

    def zero_trust_gateway_proxy_endpoints_create_proxy_endpoint(
        self,
        account_id: object,
        *,
        ips: List[str],
        name: str,
        subdomain: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ProxyEndpointZeroTrustGatewayProxyEndpointsCreateProxyEndpointResponse:
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
        return self._post(
            f"/accounts/{account_id}/gateway/proxy_endpoints",
            body=maybe_transform(
                {
                    "ips": ips,
                    "name": name,
                    "subdomain": subdomain,
                },
                proxy_endpoint_zero_trust_gateway_proxy_endpoints_create_proxy_endpoint_params.ProxyEndpointZeroTrustGatewayProxyEndpointsCreateProxyEndpointParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[ProxyEndpointZeroTrustGatewayProxyEndpointsCreateProxyEndpointResponse],
                ResultWrapper[ProxyEndpointZeroTrustGatewayProxyEndpointsCreateProxyEndpointResponse],
            ),
        )

    def zero_trust_gateway_proxy_endpoints_list_proxy_endpoints(
        self,
        account_id: object,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ProxyEndpointZeroTrustGatewayProxyEndpointsListProxyEndpointsResponse]:
        """
        Fetches a single Zero Trust Gateway proxy endpoint.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/accounts/{account_id}/gateway/proxy_endpoints",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[ProxyEndpointZeroTrustGatewayProxyEndpointsListProxyEndpointsResponse]],
                ResultWrapper[ProxyEndpointZeroTrustGatewayProxyEndpointsListProxyEndpointsResponse],
            ),
        )


class AsyncProxyEndpoints(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncProxyEndpointsWithRawResponse:
        return AsyncProxyEndpointsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncProxyEndpointsWithStreamingResponse:
        return AsyncProxyEndpointsWithStreamingResponse(self)

    async def update(
        self,
        proxy_endpoint_id: object,
        *,
        account_id: object,
        ips: List[str] | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        subdomain: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ProxyEndpointUpdateResponse:
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
        return await self._patch(
            f"/accounts/{account_id}/gateway/proxy_endpoints/{proxy_endpoint_id}",
            body=maybe_transform(
                {
                    "ips": ips,
                    "name": name,
                    "subdomain": subdomain,
                },
                proxy_endpoint_update_params.ProxyEndpointUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[ProxyEndpointUpdateResponse], ResultWrapper[ProxyEndpointUpdateResponse]),
        )

    async def list(
        self,
        proxy_endpoint_id: object,
        *,
        account_id: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ProxyEndpointListResponse:
        """
        Fetches all Zero Trust Gateway proxy endpoints for an account.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/accounts/{account_id}/gateway/proxy_endpoints/{proxy_endpoint_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[ProxyEndpointListResponse], ResultWrapper[ProxyEndpointListResponse]),
        )

    async def delete(
        self,
        proxy_endpoint_id: object,
        *,
        account_id: object,
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

    async def get(
        self,
        proxy_endpoint_id: object,
        *,
        account_id: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ProxyEndpointGetResponse:
        """
        Fetches all Zero Trust Gateway proxy endpoints for an account.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/accounts/{account_id}/gateway/proxy_endpoints/{proxy_endpoint_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[ProxyEndpointGetResponse], ResultWrapper[ProxyEndpointGetResponse]),
        )

    async def zero_trust_gateway_proxy_endpoints_create_proxy_endpoint(
        self,
        account_id: object,
        *,
        ips: List[str],
        name: str,
        subdomain: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ProxyEndpointZeroTrustGatewayProxyEndpointsCreateProxyEndpointResponse:
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
        return await self._post(
            f"/accounts/{account_id}/gateway/proxy_endpoints",
            body=maybe_transform(
                {
                    "ips": ips,
                    "name": name,
                    "subdomain": subdomain,
                },
                proxy_endpoint_zero_trust_gateway_proxy_endpoints_create_proxy_endpoint_params.ProxyEndpointZeroTrustGatewayProxyEndpointsCreateProxyEndpointParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[ProxyEndpointZeroTrustGatewayProxyEndpointsCreateProxyEndpointResponse],
                ResultWrapper[ProxyEndpointZeroTrustGatewayProxyEndpointsCreateProxyEndpointResponse],
            ),
        )

    async def zero_trust_gateway_proxy_endpoints_list_proxy_endpoints(
        self,
        account_id: object,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ProxyEndpointZeroTrustGatewayProxyEndpointsListProxyEndpointsResponse]:
        """
        Fetches a single Zero Trust Gateway proxy endpoint.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/accounts/{account_id}/gateway/proxy_endpoints",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[ProxyEndpointZeroTrustGatewayProxyEndpointsListProxyEndpointsResponse]],
                ResultWrapper[ProxyEndpointZeroTrustGatewayProxyEndpointsListProxyEndpointsResponse],
            ),
        )


class ProxyEndpointsWithRawResponse:
    def __init__(self, proxy_endpoints: ProxyEndpoints) -> None:
        self._proxy_endpoints = proxy_endpoints

        self.update = to_raw_response_wrapper(
            proxy_endpoints.update,
        )
        self.list = to_raw_response_wrapper(
            proxy_endpoints.list,
        )
        self.delete = to_raw_response_wrapper(
            proxy_endpoints.delete,
        )
        self.get = to_raw_response_wrapper(
            proxy_endpoints.get,
        )
        self.zero_trust_gateway_proxy_endpoints_create_proxy_endpoint = to_raw_response_wrapper(
            proxy_endpoints.zero_trust_gateway_proxy_endpoints_create_proxy_endpoint,
        )
        self.zero_trust_gateway_proxy_endpoints_list_proxy_endpoints = to_raw_response_wrapper(
            proxy_endpoints.zero_trust_gateway_proxy_endpoints_list_proxy_endpoints,
        )


class AsyncProxyEndpointsWithRawResponse:
    def __init__(self, proxy_endpoints: AsyncProxyEndpoints) -> None:
        self._proxy_endpoints = proxy_endpoints

        self.update = async_to_raw_response_wrapper(
            proxy_endpoints.update,
        )
        self.list = async_to_raw_response_wrapper(
            proxy_endpoints.list,
        )
        self.delete = async_to_raw_response_wrapper(
            proxy_endpoints.delete,
        )
        self.get = async_to_raw_response_wrapper(
            proxy_endpoints.get,
        )
        self.zero_trust_gateway_proxy_endpoints_create_proxy_endpoint = async_to_raw_response_wrapper(
            proxy_endpoints.zero_trust_gateway_proxy_endpoints_create_proxy_endpoint,
        )
        self.zero_trust_gateway_proxy_endpoints_list_proxy_endpoints = async_to_raw_response_wrapper(
            proxy_endpoints.zero_trust_gateway_proxy_endpoints_list_proxy_endpoints,
        )


class ProxyEndpointsWithStreamingResponse:
    def __init__(self, proxy_endpoints: ProxyEndpoints) -> None:
        self._proxy_endpoints = proxy_endpoints

        self.update = to_streamed_response_wrapper(
            proxy_endpoints.update,
        )
        self.list = to_streamed_response_wrapper(
            proxy_endpoints.list,
        )
        self.delete = to_streamed_response_wrapper(
            proxy_endpoints.delete,
        )
        self.get = to_streamed_response_wrapper(
            proxy_endpoints.get,
        )
        self.zero_trust_gateway_proxy_endpoints_create_proxy_endpoint = to_streamed_response_wrapper(
            proxy_endpoints.zero_trust_gateway_proxy_endpoints_create_proxy_endpoint,
        )
        self.zero_trust_gateway_proxy_endpoints_list_proxy_endpoints = to_streamed_response_wrapper(
            proxy_endpoints.zero_trust_gateway_proxy_endpoints_list_proxy_endpoints,
        )


class AsyncProxyEndpointsWithStreamingResponse:
    def __init__(self, proxy_endpoints: AsyncProxyEndpoints) -> None:
        self._proxy_endpoints = proxy_endpoints

        self.update = async_to_streamed_response_wrapper(
            proxy_endpoints.update,
        )
        self.list = async_to_streamed_response_wrapper(
            proxy_endpoints.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            proxy_endpoints.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            proxy_endpoints.get,
        )
        self.zero_trust_gateway_proxy_endpoints_create_proxy_endpoint = async_to_streamed_response_wrapper(
            proxy_endpoints.zero_trust_gateway_proxy_endpoints_create_proxy_endpoint,
        )
        self.zero_trust_gateway_proxy_endpoints_list_proxy_endpoints = async_to_streamed_response_wrapper(
            proxy_endpoints.zero_trust_gateway_proxy_endpoints_list_proxy_endpoints,
        )
