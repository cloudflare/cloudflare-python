# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Optional, cast

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
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
from ...._base_client import AsyncPaginator, make_request_options
from ....types.zero_trust.access.gateway_ca_list_response import GatewayCAListResponse
from ....types.zero_trust.access.gateway_ca_create_response import GatewayCACreateResponse
from ....types.zero_trust.access.gateway_ca_delete_response import GatewayCADeleteResponse

__all__ = ["GatewayCAResource", "AsyncGatewayCAResource"]


class GatewayCAResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> GatewayCAResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return GatewayCAResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> GatewayCAResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return GatewayCAResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[GatewayCACreateResponse]:
        """
        Adds a new SSH Certificate Authority (CA).

        Args:
          account_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._post(
            f"/accounts/{account_id}/access/gateway_ca",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[GatewayCACreateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[GatewayCACreateResponse]], ResultWrapper[GatewayCACreateResponse]),
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
    ) -> SyncSinglePage[GatewayCAListResponse]:
        """
        Lists SSH Certificate Authorities (CA).

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
            f"/accounts/{account_id}/access/gateway_ca",
            page=SyncSinglePage[GatewayCAListResponse],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=GatewayCAListResponse,
        )

    def delete(
        self,
        certificate_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[GatewayCADeleteResponse]:
        """
        Deletes an SSH Certificate Authority.

        Args:
          account_id: Identifier

          certificate_id: UUID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not certificate_id:
            raise ValueError(f"Expected a non-empty value for `certificate_id` but received {certificate_id!r}")
        return self._delete(
            f"/accounts/{account_id}/access/gateway_ca/{certificate_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[GatewayCADeleteResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[GatewayCADeleteResponse]], ResultWrapper[GatewayCADeleteResponse]),
        )


class AsyncGatewayCAResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncGatewayCAResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncGatewayCAResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncGatewayCAResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncGatewayCAResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[GatewayCACreateResponse]:
        """
        Adds a new SSH Certificate Authority (CA).

        Args:
          account_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._post(
            f"/accounts/{account_id}/access/gateway_ca",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[GatewayCACreateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[GatewayCACreateResponse]], ResultWrapper[GatewayCACreateResponse]),
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
    ) -> AsyncPaginator[GatewayCAListResponse, AsyncSinglePage[GatewayCAListResponse]]:
        """
        Lists SSH Certificate Authorities (CA).

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
            f"/accounts/{account_id}/access/gateway_ca",
            page=AsyncSinglePage[GatewayCAListResponse],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=GatewayCAListResponse,
        )

    async def delete(
        self,
        certificate_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[GatewayCADeleteResponse]:
        """
        Deletes an SSH Certificate Authority.

        Args:
          account_id: Identifier

          certificate_id: UUID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not certificate_id:
            raise ValueError(f"Expected a non-empty value for `certificate_id` but received {certificate_id!r}")
        return await self._delete(
            f"/accounts/{account_id}/access/gateway_ca/{certificate_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[GatewayCADeleteResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[GatewayCADeleteResponse]], ResultWrapper[GatewayCADeleteResponse]),
        )


class GatewayCAResourceWithRawResponse:
    def __init__(self, gateway_ca: GatewayCAResource) -> None:
        self._gateway_ca = gateway_ca

        self.create = to_raw_response_wrapper(
            gateway_ca.create,
        )
        self.list = to_raw_response_wrapper(
            gateway_ca.list,
        )
        self.delete = to_raw_response_wrapper(
            gateway_ca.delete,
        )


class AsyncGatewayCAResourceWithRawResponse:
    def __init__(self, gateway_ca: AsyncGatewayCAResource) -> None:
        self._gateway_ca = gateway_ca

        self.create = async_to_raw_response_wrapper(
            gateway_ca.create,
        )
        self.list = async_to_raw_response_wrapper(
            gateway_ca.list,
        )
        self.delete = async_to_raw_response_wrapper(
            gateway_ca.delete,
        )


class GatewayCAResourceWithStreamingResponse:
    def __init__(self, gateway_ca: GatewayCAResource) -> None:
        self._gateway_ca = gateway_ca

        self.create = to_streamed_response_wrapper(
            gateway_ca.create,
        )
        self.list = to_streamed_response_wrapper(
            gateway_ca.list,
        )
        self.delete = to_streamed_response_wrapper(
            gateway_ca.delete,
        )


class AsyncGatewayCAResourceWithStreamingResponse:
    def __init__(self, gateway_ca: AsyncGatewayCAResource) -> None:
        self._gateway_ca = gateway_ca

        self.create = async_to_streamed_response_wrapper(
            gateway_ca.create,
        )
        self.list = async_to_streamed_response_wrapper(
            gateway_ca.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            gateway_ca.delete,
        )
