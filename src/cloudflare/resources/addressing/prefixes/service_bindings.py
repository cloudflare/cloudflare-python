# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Optional, cast

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
from ....pagination import SyncSinglePage, AsyncSinglePage
from ...._base_client import AsyncPaginator, make_request_options
from ....types.addressing.prefixes import service_binding_create_params
from ....types.addressing.prefixes.service_binding import ServiceBinding
from ....types.addressing.prefixes.service_binding_delete_response import ServiceBindingDeleteResponse

__all__ = ["ServiceBindingsResource", "AsyncServiceBindingsResource"]


class ServiceBindingsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ServiceBindingsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return ServiceBindingsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ServiceBindingsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return ServiceBindingsResourceWithStreamingResponse(self)

    def create(
        self,
        prefix_id: str,
        *,
        account_id: str,
        cidr: str | NotGiven = NOT_GIVEN,
        service_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ServiceBinding]:
        """
        Creates a new Service Binding, routing traffic to IPs within the given CIDR to a
        service running on Cloudflare's network. **Note:** This API may only be used on
        prefixes currently configured with a Magic Transit service binding, and only
        allows creating service bindings for the Cloudflare CDN or Cloudflare Spectrum.

        Args:
          account_id: Identifier of a Cloudflare account.

          prefix_id: Identifier of an IP Prefix.

          cidr: IP Prefix in Classless Inter-Domain Routing format.

          service_id: Identifier of a Service on the Cloudflare network. Available services and their
              IDs may be found in the **List Services** endpoint.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not prefix_id:
            raise ValueError(f"Expected a non-empty value for `prefix_id` but received {prefix_id!r}")
        return self._post(
            f"/accounts/{account_id}/addressing/prefixes/{prefix_id}/bindings",
            body=maybe_transform(
                {
                    "cidr": cidr,
                    "service_id": service_id,
                },
                service_binding_create_params.ServiceBindingCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[ServiceBinding]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[ServiceBinding]], ResultWrapper[ServiceBinding]),
        )

    def list(
        self,
        prefix_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncSinglePage[ServiceBinding]:
        """List the Cloudflare services this prefix is currently bound to.

        Traffic sent to
        an address within an IP prefix will be routed to the Cloudflare service of the
        most-specific Service Binding matching the address. **Example:** binding
        `192.0.2.0/24` to Cloudflare Magic Transit and `192.0.2.1/32` to the Cloudflare
        CDN would route traffic for `192.0.2.1` to the CDN, and traffic for all other
        IPs in the prefix to Cloudflare Magic Transit.

        Args:
          account_id: Identifier of a Cloudflare account.

          prefix_id: Identifier of an IP Prefix.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not prefix_id:
            raise ValueError(f"Expected a non-empty value for `prefix_id` but received {prefix_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/addressing/prefixes/{prefix_id}/bindings",
            page=SyncSinglePage[ServiceBinding],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=ServiceBinding,
        )

    def delete(
        self,
        binding_id: str,
        *,
        account_id: str,
        prefix_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ServiceBindingDeleteResponse:
        """
        Delete a Service Binding

        Args:
          account_id: Identifier of a Cloudflare account.

          prefix_id: Identifier of an IP Prefix.

          binding_id: Identifier of a Service Binding.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not prefix_id:
            raise ValueError(f"Expected a non-empty value for `prefix_id` but received {prefix_id!r}")
        if not binding_id:
            raise ValueError(f"Expected a non-empty value for `binding_id` but received {binding_id!r}")
        return self._delete(
            f"/accounts/{account_id}/addressing/prefixes/{prefix_id}/bindings/{binding_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ServiceBindingDeleteResponse,
        )

    def get(
        self,
        binding_id: str,
        *,
        account_id: str,
        prefix_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ServiceBinding]:
        """
        Fetch a single Service Binding

        Args:
          account_id: Identifier of a Cloudflare account.

          prefix_id: Identifier of an IP Prefix.

          binding_id: Identifier of a Service Binding.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not prefix_id:
            raise ValueError(f"Expected a non-empty value for `prefix_id` but received {prefix_id!r}")
        if not binding_id:
            raise ValueError(f"Expected a non-empty value for `binding_id` but received {binding_id!r}")
        return self._get(
            f"/accounts/{account_id}/addressing/prefixes/{prefix_id}/bindings/{binding_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[ServiceBinding]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[ServiceBinding]], ResultWrapper[ServiceBinding]),
        )


class AsyncServiceBindingsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncServiceBindingsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncServiceBindingsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncServiceBindingsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncServiceBindingsResourceWithStreamingResponse(self)

    async def create(
        self,
        prefix_id: str,
        *,
        account_id: str,
        cidr: str | NotGiven = NOT_GIVEN,
        service_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ServiceBinding]:
        """
        Creates a new Service Binding, routing traffic to IPs within the given CIDR to a
        service running on Cloudflare's network. **Note:** This API may only be used on
        prefixes currently configured with a Magic Transit service binding, and only
        allows creating service bindings for the Cloudflare CDN or Cloudflare Spectrum.

        Args:
          account_id: Identifier of a Cloudflare account.

          prefix_id: Identifier of an IP Prefix.

          cidr: IP Prefix in Classless Inter-Domain Routing format.

          service_id: Identifier of a Service on the Cloudflare network. Available services and their
              IDs may be found in the **List Services** endpoint.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not prefix_id:
            raise ValueError(f"Expected a non-empty value for `prefix_id` but received {prefix_id!r}")
        return await self._post(
            f"/accounts/{account_id}/addressing/prefixes/{prefix_id}/bindings",
            body=await async_maybe_transform(
                {
                    "cidr": cidr,
                    "service_id": service_id,
                },
                service_binding_create_params.ServiceBindingCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[ServiceBinding]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[ServiceBinding]], ResultWrapper[ServiceBinding]),
        )

    def list(
        self,
        prefix_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[ServiceBinding, AsyncSinglePage[ServiceBinding]]:
        """List the Cloudflare services this prefix is currently bound to.

        Traffic sent to
        an address within an IP prefix will be routed to the Cloudflare service of the
        most-specific Service Binding matching the address. **Example:** binding
        `192.0.2.0/24` to Cloudflare Magic Transit and `192.0.2.1/32` to the Cloudflare
        CDN would route traffic for `192.0.2.1` to the CDN, and traffic for all other
        IPs in the prefix to Cloudflare Magic Transit.

        Args:
          account_id: Identifier of a Cloudflare account.

          prefix_id: Identifier of an IP Prefix.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not prefix_id:
            raise ValueError(f"Expected a non-empty value for `prefix_id` but received {prefix_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/addressing/prefixes/{prefix_id}/bindings",
            page=AsyncSinglePage[ServiceBinding],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=ServiceBinding,
        )

    async def delete(
        self,
        binding_id: str,
        *,
        account_id: str,
        prefix_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ServiceBindingDeleteResponse:
        """
        Delete a Service Binding

        Args:
          account_id: Identifier of a Cloudflare account.

          prefix_id: Identifier of an IP Prefix.

          binding_id: Identifier of a Service Binding.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not prefix_id:
            raise ValueError(f"Expected a non-empty value for `prefix_id` but received {prefix_id!r}")
        if not binding_id:
            raise ValueError(f"Expected a non-empty value for `binding_id` but received {binding_id!r}")
        return await self._delete(
            f"/accounts/{account_id}/addressing/prefixes/{prefix_id}/bindings/{binding_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ServiceBindingDeleteResponse,
        )

    async def get(
        self,
        binding_id: str,
        *,
        account_id: str,
        prefix_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ServiceBinding]:
        """
        Fetch a single Service Binding

        Args:
          account_id: Identifier of a Cloudflare account.

          prefix_id: Identifier of an IP Prefix.

          binding_id: Identifier of a Service Binding.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not prefix_id:
            raise ValueError(f"Expected a non-empty value for `prefix_id` but received {prefix_id!r}")
        if not binding_id:
            raise ValueError(f"Expected a non-empty value for `binding_id` but received {binding_id!r}")
        return await self._get(
            f"/accounts/{account_id}/addressing/prefixes/{prefix_id}/bindings/{binding_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[ServiceBinding]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[ServiceBinding]], ResultWrapper[ServiceBinding]),
        )


class ServiceBindingsResourceWithRawResponse:
    def __init__(self, service_bindings: ServiceBindingsResource) -> None:
        self._service_bindings = service_bindings

        self.create = to_raw_response_wrapper(
            service_bindings.create,
        )
        self.list = to_raw_response_wrapper(
            service_bindings.list,
        )
        self.delete = to_raw_response_wrapper(
            service_bindings.delete,
        )
        self.get = to_raw_response_wrapper(
            service_bindings.get,
        )


class AsyncServiceBindingsResourceWithRawResponse:
    def __init__(self, service_bindings: AsyncServiceBindingsResource) -> None:
        self._service_bindings = service_bindings

        self.create = async_to_raw_response_wrapper(
            service_bindings.create,
        )
        self.list = async_to_raw_response_wrapper(
            service_bindings.list,
        )
        self.delete = async_to_raw_response_wrapper(
            service_bindings.delete,
        )
        self.get = async_to_raw_response_wrapper(
            service_bindings.get,
        )


class ServiceBindingsResourceWithStreamingResponse:
    def __init__(self, service_bindings: ServiceBindingsResource) -> None:
        self._service_bindings = service_bindings

        self.create = to_streamed_response_wrapper(
            service_bindings.create,
        )
        self.list = to_streamed_response_wrapper(
            service_bindings.list,
        )
        self.delete = to_streamed_response_wrapper(
            service_bindings.delete,
        )
        self.get = to_streamed_response_wrapper(
            service_bindings.get,
        )


class AsyncServiceBindingsResourceWithStreamingResponse:
    def __init__(self, service_bindings: AsyncServiceBindingsResource) -> None:
        self._service_bindings = service_bindings

        self.create = async_to_streamed_response_wrapper(
            service_bindings.create,
        )
        self.list = async_to_streamed_response_wrapper(
            service_bindings.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            service_bindings.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            service_bindings.get,
        )
