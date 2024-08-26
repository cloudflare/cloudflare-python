# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ....._compat import cached_property

from .....types.addressing.prefixes.bgp.service_binding import ServiceBinding

from ....._wrappers import ResultWrapper

from ....._utils import maybe_transform, async_maybe_transform

from typing import Optional, Type

from ....._base_client import make_request_options, AsyncPaginator

from .....pagination import SyncSinglePage, AsyncSinglePage

from .....types.addressing.prefixes.bgp.binding_delete_response import BindingDeleteResponse

from ....._response import to_raw_response_wrapper, async_to_raw_response_wrapper, to_streamed_response_wrapper, async_to_streamed_response_wrapper

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ....._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ....._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ....._resource import SyncAPIResource, AsyncAPIResource
from .....types import shared_params
from .....types.addressing.prefixes.bgp import binding_create_params
from typing import cast
from typing import cast
from typing import cast
from typing import cast

__all__ = ["BindingsResource", "AsyncBindingsResource"]

class BindingsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> BindingsResourceWithRawResponse:
        return BindingsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BindingsResourceWithStreamingResponse:
        return BindingsResourceWithStreamingResponse(self)

    def create(self,
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
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Optional[ServiceBinding]:
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
          raise ValueError(
            f'Expected a non-empty value for `account_id` but received {account_id!r}'
          )
        if not prefix_id:
          raise ValueError(
            f'Expected a non-empty value for `prefix_id` but received {prefix_id!r}'
          )
        return self._post(
            f"/accounts/{account_id}/addressing/prefixes/{prefix_id}/bindings",
            body=maybe_transform({
                "cidr": cidr,
                "service_id": service_id,
            }, binding_create_params.BindingCreateParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[Optional[ServiceBinding]]._unwrapper),
            cast_to=cast(Type[Optional[ServiceBinding]], ResultWrapper[ServiceBinding]),
        )

    def list(self,
    prefix_id: str,
    *,
    account_id: str,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> SyncSinglePage[ServiceBinding]:
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
          raise ValueError(
            f'Expected a non-empty value for `account_id` but received {account_id!r}'
          )
        if not prefix_id:
          raise ValueError(
            f'Expected a non-empty value for `prefix_id` but received {prefix_id!r}'
          )
        return self._get_api_list(
            f"/accounts/{account_id}/addressing/prefixes/{prefix_id}/bindings",
            page = SyncSinglePage[ServiceBinding],
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            model=ServiceBinding,
        )

    def delete(self,
    binding_id: str,
    *,
    account_id: str,
    prefix_id: str,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> BindingDeleteResponse:
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
          raise ValueError(
            f'Expected a non-empty value for `account_id` but received {account_id!r}'
          )
        if not prefix_id:
          raise ValueError(
            f'Expected a non-empty value for `prefix_id` but received {prefix_id!r}'
          )
        if not binding_id:
          raise ValueError(
            f'Expected a non-empty value for `binding_id` but received {binding_id!r}'
          )
        return self._delete(
            f"/accounts/{account_id}/addressing/prefixes/{prefix_id}/bindings/{binding_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=BindingDeleteResponse,
        )

    def get(self,
    binding_id: str,
    *,
    account_id: str,
    prefix_id: str,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Optional[ServiceBinding]:
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
          raise ValueError(
            f'Expected a non-empty value for `account_id` but received {account_id!r}'
          )
        if not prefix_id:
          raise ValueError(
            f'Expected a non-empty value for `prefix_id` but received {prefix_id!r}'
          )
        if not binding_id:
          raise ValueError(
            f'Expected a non-empty value for `binding_id` but received {binding_id!r}'
          )
        return self._get(
            f"/accounts/{account_id}/addressing/prefixes/{prefix_id}/bindings/{binding_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[Optional[ServiceBinding]]._unwrapper),
            cast_to=cast(Type[Optional[ServiceBinding]], ResultWrapper[ServiceBinding]),
        )

class AsyncBindingsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncBindingsResourceWithRawResponse:
        return AsyncBindingsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBindingsResourceWithStreamingResponse:
        return AsyncBindingsResourceWithStreamingResponse(self)

    async def create(self,
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
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Optional[ServiceBinding]:
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
          raise ValueError(
            f'Expected a non-empty value for `account_id` but received {account_id!r}'
          )
        if not prefix_id:
          raise ValueError(
            f'Expected a non-empty value for `prefix_id` but received {prefix_id!r}'
          )
        return await self._post(
            f"/accounts/{account_id}/addressing/prefixes/{prefix_id}/bindings",
            body=await async_maybe_transform({
                "cidr": cidr,
                "service_id": service_id,
            }, binding_create_params.BindingCreateParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[Optional[ServiceBinding]]._unwrapper),
            cast_to=cast(Type[Optional[ServiceBinding]], ResultWrapper[ServiceBinding]),
        )

    def list(self,
    prefix_id: str,
    *,
    account_id: str,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> AsyncPaginator[ServiceBinding, AsyncSinglePage[ServiceBinding]]:
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
          raise ValueError(
            f'Expected a non-empty value for `account_id` but received {account_id!r}'
          )
        if not prefix_id:
          raise ValueError(
            f'Expected a non-empty value for `prefix_id` but received {prefix_id!r}'
          )
        return self._get_api_list(
            f"/accounts/{account_id}/addressing/prefixes/{prefix_id}/bindings",
            page = AsyncSinglePage[ServiceBinding],
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            model=ServiceBinding,
        )

    async def delete(self,
    binding_id: str,
    *,
    account_id: str,
    prefix_id: str,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> BindingDeleteResponse:
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
          raise ValueError(
            f'Expected a non-empty value for `account_id` but received {account_id!r}'
          )
        if not prefix_id:
          raise ValueError(
            f'Expected a non-empty value for `prefix_id` but received {prefix_id!r}'
          )
        if not binding_id:
          raise ValueError(
            f'Expected a non-empty value for `binding_id` but received {binding_id!r}'
          )
        return await self._delete(
            f"/accounts/{account_id}/addressing/prefixes/{prefix_id}/bindings/{binding_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=BindingDeleteResponse,
        )

    async def get(self,
    binding_id: str,
    *,
    account_id: str,
    prefix_id: str,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Optional[ServiceBinding]:
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
          raise ValueError(
            f'Expected a non-empty value for `account_id` but received {account_id!r}'
          )
        if not prefix_id:
          raise ValueError(
            f'Expected a non-empty value for `prefix_id` but received {prefix_id!r}'
          )
        if not binding_id:
          raise ValueError(
            f'Expected a non-empty value for `binding_id` but received {binding_id!r}'
          )
        return await self._get(
            f"/accounts/{account_id}/addressing/prefixes/{prefix_id}/bindings/{binding_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[Optional[ServiceBinding]]._unwrapper),
            cast_to=cast(Type[Optional[ServiceBinding]], ResultWrapper[ServiceBinding]),
        )

class BindingsResourceWithRawResponse:
    def __init__(self, bindings: BindingsResource) -> None:
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

class AsyncBindingsResourceWithRawResponse:
    def __init__(self, bindings: AsyncBindingsResource) -> None:
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

class BindingsResourceWithStreamingResponse:
    def __init__(self, bindings: BindingsResource) -> None:
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

class AsyncBindingsResourceWithStreamingResponse:
    def __init__(self, bindings: AsyncBindingsResource) -> None:
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