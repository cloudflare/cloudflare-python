# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, Type, cast

import httpx

from ....._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ....._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....._wrappers import ResultWrapper
from ....._base_client import (
    make_request_options,
)
from .....types.addressing.prefixes.bgp import (
    BindingListResponse,
    BindingDeleteResponse,
    AddressingServiceBinding,
    binding_create_params,
)

__all__ = ["Bindings", "AsyncBindings"]


class Bindings(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> BindingsWithRawResponse:
        return BindingsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BindingsWithStreamingResponse:
        return BindingsWithStreamingResponse(self)

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
    ) -> AddressingServiceBinding:
        """
        Creates a new Service Binding, routing traffic to IPs within the given CIDR to a
        service running on Cloudflare's network. **Note:** This API may only be used on
        prefixes currently configured with a Magic Transit service binding, and only
        allows creating service bindings for the Cloudflare CDN or Cloudflare Spectrum.

        Args:
          account_id: Identifier

          prefix_id: Identifier

          cidr: IP Prefix in Classless Inter-Domain Routing format.

          service_id: Identifier

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
                binding_create_params.BindingCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[AddressingServiceBinding], ResultWrapper[AddressingServiceBinding]),
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
    ) -> BindingListResponse:
        """List the Cloudflare services this prefix is currently bound to.

        Traffic sent to
        an address within an IP prefix will be routed to the Cloudflare service of the
        most-specific Service Binding matching the address. **Example:** binding
        `192.0.2.0/24` to Cloudflare Magic Transit and `192.0.2.1/32` to the Cloudflare
        CDN would route traffic for `192.0.2.1` to the CDN, and traffic for all other
        IPs in the prefix to Cloudflare Magic Transit.

        Args:
          account_id: Identifier

          prefix_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not prefix_id:
            raise ValueError(f"Expected a non-empty value for `prefix_id` but received {prefix_id!r}")
        return self._get(
            f"/accounts/{account_id}/addressing/prefixes/{prefix_id}/bindings",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[BindingListResponse], ResultWrapper[BindingListResponse]),
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
    ) -> BindingDeleteResponse:
        """
        Delete a Service Binding

        Args:
          account_id: Identifier

          prefix_id: Identifier

          binding_id: Identifier

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
        return cast(
            BindingDeleteResponse,
            self._delete(
                f"/accounts/{account_id}/addressing/prefixes/{prefix_id}/bindings/{binding_id}",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[BindingDeleteResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
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
    ) -> AddressingServiceBinding:
        """
        Fetch a single Service Binding

        Args:
          account_id: Identifier

          prefix_id: Identifier

          binding_id: Identifier

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
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[AddressingServiceBinding], ResultWrapper[AddressingServiceBinding]),
        )


class AsyncBindings(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncBindingsWithRawResponse:
        return AsyncBindingsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBindingsWithStreamingResponse:
        return AsyncBindingsWithStreamingResponse(self)

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
    ) -> AddressingServiceBinding:
        """
        Creates a new Service Binding, routing traffic to IPs within the given CIDR to a
        service running on Cloudflare's network. **Note:** This API may only be used on
        prefixes currently configured with a Magic Transit service binding, and only
        allows creating service bindings for the Cloudflare CDN or Cloudflare Spectrum.

        Args:
          account_id: Identifier

          prefix_id: Identifier

          cidr: IP Prefix in Classless Inter-Domain Routing format.

          service_id: Identifier

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
                binding_create_params.BindingCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[AddressingServiceBinding], ResultWrapper[AddressingServiceBinding]),
        )

    async def list(
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
    ) -> BindingListResponse:
        """List the Cloudflare services this prefix is currently bound to.

        Traffic sent to
        an address within an IP prefix will be routed to the Cloudflare service of the
        most-specific Service Binding matching the address. **Example:** binding
        `192.0.2.0/24` to Cloudflare Magic Transit and `192.0.2.1/32` to the Cloudflare
        CDN would route traffic for `192.0.2.1` to the CDN, and traffic for all other
        IPs in the prefix to Cloudflare Magic Transit.

        Args:
          account_id: Identifier

          prefix_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not prefix_id:
            raise ValueError(f"Expected a non-empty value for `prefix_id` but received {prefix_id!r}")
        return await self._get(
            f"/accounts/{account_id}/addressing/prefixes/{prefix_id}/bindings",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[BindingListResponse], ResultWrapper[BindingListResponse]),
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
    ) -> BindingDeleteResponse:
        """
        Delete a Service Binding

        Args:
          account_id: Identifier

          prefix_id: Identifier

          binding_id: Identifier

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
        return cast(
            BindingDeleteResponse,
            await self._delete(
                f"/accounts/{account_id}/addressing/prefixes/{prefix_id}/bindings/{binding_id}",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[BindingDeleteResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
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
    ) -> AddressingServiceBinding:
        """
        Fetch a single Service Binding

        Args:
          account_id: Identifier

          prefix_id: Identifier

          binding_id: Identifier

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
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[AddressingServiceBinding], ResultWrapper[AddressingServiceBinding]),
        )


class BindingsWithRawResponse:
    def __init__(self, bindings: Bindings) -> None:
        self._bindings = bindings

        self.create = to_raw_response_wrapper(
            bindings.create,
        )
        self.list = to_raw_response_wrapper(
            bindings.list,
        )
        self.delete = to_raw_response_wrapper(
            bindings.delete,
        )
        self.get = to_raw_response_wrapper(
            bindings.get,
        )


class AsyncBindingsWithRawResponse:
    def __init__(self, bindings: AsyncBindings) -> None:
        self._bindings = bindings

        self.create = async_to_raw_response_wrapper(
            bindings.create,
        )
        self.list = async_to_raw_response_wrapper(
            bindings.list,
        )
        self.delete = async_to_raw_response_wrapper(
            bindings.delete,
        )
        self.get = async_to_raw_response_wrapper(
            bindings.get,
        )


class BindingsWithStreamingResponse:
    def __init__(self, bindings: Bindings) -> None:
        self._bindings = bindings

        self.create = to_streamed_response_wrapper(
            bindings.create,
        )
        self.list = to_streamed_response_wrapper(
            bindings.list,
        )
        self.delete = to_streamed_response_wrapper(
            bindings.delete,
        )
        self.get = to_streamed_response_wrapper(
            bindings.get,
        )


class AsyncBindingsWithStreamingResponse:
    def __init__(self, bindings: AsyncBindings) -> None:
        self._bindings = bindings

        self.create = async_to_streamed_response_wrapper(
            bindings.create,
        )
        self.list = async_to_streamed_response_wrapper(
            bindings.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            bindings.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            bindings.get,
        )
