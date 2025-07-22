# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Optional, cast
from typing_extensions import Literal

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
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
from ...types.diagnostics import endpoint_healthcheck_create_params
from ...types.diagnostics.endpoint_healthcheck_list_response import EndpointHealthcheckListResponse
from ...types.diagnostics.endpoint_healthcheck_create_response import EndpointHealthcheckCreateResponse

__all__ = ["EndpointHealthchecksResource", "AsyncEndpointHealthchecksResource"]


class EndpointHealthchecksResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> EndpointHealthchecksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return EndpointHealthchecksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EndpointHealthchecksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return EndpointHealthchecksResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        account_id: str,
        check_type: Literal["icmp"],
        endpoint: str,
        name: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[EndpointHealthcheckCreateResponse]:
        """
        Create Endpoint Health Check.

        Args:
          account_id: Identifier

          check_type: type of check to perform

          endpoint: the IP address of the host to perform checks against

          name: Optional name associated with this check

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._post(
            f"/accounts/{account_id}/diagnostics/endpoint-healthchecks",
            body=maybe_transform(
                {
                    "check_type": check_type,
                    "endpoint": endpoint,
                    "name": name,
                },
                endpoint_healthcheck_create_params.EndpointHealthcheckCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[EndpointHealthcheckCreateResponse]]._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[EndpointHealthcheckCreateResponse]], ResultWrapper[EndpointHealthcheckCreateResponse]
            ),
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
    ) -> Optional[EndpointHealthcheckListResponse]:
        """
        List Endpoint Health Checks.

        Args:
          account_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get(
            f"/accounts/{account_id}/diagnostics/endpoint-healthchecks",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[EndpointHealthcheckListResponse]]._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[EndpointHealthcheckListResponse]], ResultWrapper[EndpointHealthcheckListResponse]
            ),
        )


class AsyncEndpointHealthchecksResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncEndpointHealthchecksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncEndpointHealthchecksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEndpointHealthchecksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncEndpointHealthchecksResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_id: str,
        check_type: Literal["icmp"],
        endpoint: str,
        name: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[EndpointHealthcheckCreateResponse]:
        """
        Create Endpoint Health Check.

        Args:
          account_id: Identifier

          check_type: type of check to perform

          endpoint: the IP address of the host to perform checks against

          name: Optional name associated with this check

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._post(
            f"/accounts/{account_id}/diagnostics/endpoint-healthchecks",
            body=await async_maybe_transform(
                {
                    "check_type": check_type,
                    "endpoint": endpoint,
                    "name": name,
                },
                endpoint_healthcheck_create_params.EndpointHealthcheckCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[EndpointHealthcheckCreateResponse]]._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[EndpointHealthcheckCreateResponse]], ResultWrapper[EndpointHealthcheckCreateResponse]
            ),
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
    ) -> Optional[EndpointHealthcheckListResponse]:
        """
        List Endpoint Health Checks.

        Args:
          account_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._get(
            f"/accounts/{account_id}/diagnostics/endpoint-healthchecks",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[EndpointHealthcheckListResponse]]._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[EndpointHealthcheckListResponse]], ResultWrapper[EndpointHealthcheckListResponse]
            ),
        )


class EndpointHealthchecksResourceWithRawResponse:
    def __init__(self, endpoint_healthchecks: EndpointHealthchecksResource) -> None:
        self._endpoint_healthchecks = endpoint_healthchecks

        self.create = to_raw_response_wrapper(
            endpoint_healthchecks.create,
        )
        self.list = to_raw_response_wrapper(
            endpoint_healthchecks.list,
        )


class AsyncEndpointHealthchecksResourceWithRawResponse:
    def __init__(self, endpoint_healthchecks: AsyncEndpointHealthchecksResource) -> None:
        self._endpoint_healthchecks = endpoint_healthchecks

        self.create = async_to_raw_response_wrapper(
            endpoint_healthchecks.create,
        )
        self.list = async_to_raw_response_wrapper(
            endpoint_healthchecks.list,
        )


class EndpointHealthchecksResourceWithStreamingResponse:
    def __init__(self, endpoint_healthchecks: EndpointHealthchecksResource) -> None:
        self._endpoint_healthchecks = endpoint_healthchecks

        self.create = to_streamed_response_wrapper(
            endpoint_healthchecks.create,
        )
        self.list = to_streamed_response_wrapper(
            endpoint_healthchecks.list,
        )


class AsyncEndpointHealthchecksResourceWithStreamingResponse:
    def __init__(self, endpoint_healthchecks: AsyncEndpointHealthchecksResource) -> None:
        self._endpoint_healthchecks = endpoint_healthchecks

        self.create = async_to_streamed_response_wrapper(
            endpoint_healthchecks.create,
        )
        self.list = async_to_streamed_response_wrapper(
            endpoint_healthchecks.list,
        )
