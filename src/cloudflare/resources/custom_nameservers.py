# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .._compat import cached_property

from ..types.custom_nameservers.custom_nameserver import CustomNameserver

from .._wrappers import ResultWrapper

from .._utils import maybe_transform, async_maybe_transform

from typing import Optional, Type

from .._base_client import make_request_options

from ..types.custom_nameservers.custom_nameserver_delete_response import CustomNameserverDeleteResponse

from ..types.custom_nameservers.custom_nameserver_availabilty_response import CustomNameserverAvailabiltyResponse

from ..types.custom_nameservers.custom_nameserver_get_response import CustomNameserverGetResponse

from .._response import to_raw_response_wrapper, async_to_raw_response_wrapper, to_streamed_response_wrapper, async_to_streamed_response_wrapper

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from .._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from .._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from .._resource import SyncAPIResource, AsyncAPIResource
from ..types import shared_params
from ..types.custom_nameservers import custom_nameserver_create_params
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast

__all__ = ["CustomNameserversResource", "AsyncCustomNameserversResource"]

class CustomNameserversResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CustomNameserversResourceWithRawResponse:
        return CustomNameserversResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CustomNameserversResourceWithStreamingResponse:
        return CustomNameserversResourceWithStreamingResponse(self)

    def create(self,
    *,
    account_id: str,
    ns_name: str,
    ns_set: float | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Optional[CustomNameserver]:
        """
        Add Account Custom Nameserver

        Args:
          account_id: Account identifier tag.

          ns_name: The FQDN of the name server.

          ns_set: The number of the set that this name server belongs to.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
          raise ValueError(
            f'Expected a non-empty value for `account_id` but received {account_id!r}'
          )
        return self._post(
            f"/accounts/{account_id}/custom_ns",
            body=maybe_transform({
                "ns_name": ns_name,
                "ns_set": ns_set,
            }, custom_nameserver_create_params.CustomNameserverCreateParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[Optional[CustomNameserver]]._unwrapper),
            cast_to=cast(Type[Optional[CustomNameserver]], ResultWrapper[CustomNameserver]),
        )

    def delete(self,
    custom_ns_id: str,
    *,
    account_id: str,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Optional[CustomNameserverDeleteResponse]:
        """
        Delete Account Custom Nameserver

        Args:
          account_id: Account identifier tag.

          custom_ns_id: The FQDN of the name server.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
          raise ValueError(
            f'Expected a non-empty value for `account_id` but received {account_id!r}'
          )
        if not custom_ns_id:
          raise ValueError(
            f'Expected a non-empty value for `custom_ns_id` but received {custom_ns_id!r}'
          )
        return self._delete(
            f"/accounts/{account_id}/custom_ns/{custom_ns_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[Optional[CustomNameserverDeleteResponse]]._unwrapper),
            cast_to=cast(Type[Optional[CustomNameserverDeleteResponse]], ResultWrapper[CustomNameserverDeleteResponse]),
        )

    def availabilty(self,
    *,
    account_id: str,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Optional[CustomNameserverAvailabiltyResponse]:
        """
        Get Eligible Zones for Account Custom Nameservers

        Args:
          account_id: Account identifier tag.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
          raise ValueError(
            f'Expected a non-empty value for `account_id` but received {account_id!r}'
          )
        return self._get(
            f"/accounts/{account_id}/custom_ns/availability",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[Optional[CustomNameserverAvailabiltyResponse]]._unwrapper),
            cast_to=cast(Type[Optional[CustomNameserverAvailabiltyResponse]], ResultWrapper[CustomNameserverAvailabiltyResponse]),
        )

    def get(self,
    *,
    account_id: str,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Optional[CustomNameserverGetResponse]:
        """
        List an account's custom nameservers.

        Args:
          account_id: Account identifier tag.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
          raise ValueError(
            f'Expected a non-empty value for `account_id` but received {account_id!r}'
          )
        return self._get(
            f"/accounts/{account_id}/custom_ns",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[Optional[CustomNameserverGetResponse]]._unwrapper),
            cast_to=cast(Type[Optional[CustomNameserverGetResponse]], ResultWrapper[CustomNameserverGetResponse]),
        )

class AsyncCustomNameserversResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCustomNameserversResourceWithRawResponse:
        return AsyncCustomNameserversResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCustomNameserversResourceWithStreamingResponse:
        return AsyncCustomNameserversResourceWithStreamingResponse(self)

    async def create(self,
    *,
    account_id: str,
    ns_name: str,
    ns_set: float | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Optional[CustomNameserver]:
        """
        Add Account Custom Nameserver

        Args:
          account_id: Account identifier tag.

          ns_name: The FQDN of the name server.

          ns_set: The number of the set that this name server belongs to.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
          raise ValueError(
            f'Expected a non-empty value for `account_id` but received {account_id!r}'
          )
        return await self._post(
            f"/accounts/{account_id}/custom_ns",
            body=await async_maybe_transform({
                "ns_name": ns_name,
                "ns_set": ns_set,
            }, custom_nameserver_create_params.CustomNameserverCreateParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[Optional[CustomNameserver]]._unwrapper),
            cast_to=cast(Type[Optional[CustomNameserver]], ResultWrapper[CustomNameserver]),
        )

    async def delete(self,
    custom_ns_id: str,
    *,
    account_id: str,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Optional[CustomNameserverDeleteResponse]:
        """
        Delete Account Custom Nameserver

        Args:
          account_id: Account identifier tag.

          custom_ns_id: The FQDN of the name server.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
          raise ValueError(
            f'Expected a non-empty value for `account_id` but received {account_id!r}'
          )
        if not custom_ns_id:
          raise ValueError(
            f'Expected a non-empty value for `custom_ns_id` but received {custom_ns_id!r}'
          )
        return await self._delete(
            f"/accounts/{account_id}/custom_ns/{custom_ns_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[Optional[CustomNameserverDeleteResponse]]._unwrapper),
            cast_to=cast(Type[Optional[CustomNameserverDeleteResponse]], ResultWrapper[CustomNameserverDeleteResponse]),
        )

    async def availabilty(self,
    *,
    account_id: str,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Optional[CustomNameserverAvailabiltyResponse]:
        """
        Get Eligible Zones for Account Custom Nameservers

        Args:
          account_id: Account identifier tag.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
          raise ValueError(
            f'Expected a non-empty value for `account_id` but received {account_id!r}'
          )
        return await self._get(
            f"/accounts/{account_id}/custom_ns/availability",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[Optional[CustomNameserverAvailabiltyResponse]]._unwrapper),
            cast_to=cast(Type[Optional[CustomNameserverAvailabiltyResponse]], ResultWrapper[CustomNameserverAvailabiltyResponse]),
        )

    async def get(self,
    *,
    account_id: str,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Optional[CustomNameserverGetResponse]:
        """
        List an account's custom nameservers.

        Args:
          account_id: Account identifier tag.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
          raise ValueError(
            f'Expected a non-empty value for `account_id` but received {account_id!r}'
          )
        return await self._get(
            f"/accounts/{account_id}/custom_ns",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[Optional[CustomNameserverGetResponse]]._unwrapper),
            cast_to=cast(Type[Optional[CustomNameserverGetResponse]], ResultWrapper[CustomNameserverGetResponse]),
        )

class CustomNameserversResourceWithRawResponse:
    def __init__(self, custom_nameservers: CustomNameserversResource) -> None:
        self._custom_nameservers = custom_nameservers

        self.create = to_raw_response_wrapper(
            custom_nameservers.create,
        )
        self.delete = to_raw_response_wrapper(
            custom_nameservers.delete,
        )
        self.availabilty = to_raw_response_wrapper(
            custom_nameservers.availabilty,
        )
        self.get = to_raw_response_wrapper(
            custom_nameservers.get,
        )

class AsyncCustomNameserversResourceWithRawResponse:
    def __init__(self, custom_nameservers: AsyncCustomNameserversResource) -> None:
        self._custom_nameservers = custom_nameservers

        self.create = async_to_raw_response_wrapper(
            custom_nameservers.create,
        )
        self.delete = async_to_raw_response_wrapper(
            custom_nameservers.delete,
        )
        self.availabilty = async_to_raw_response_wrapper(
            custom_nameservers.availabilty,
        )
        self.get = async_to_raw_response_wrapper(
            custom_nameservers.get,
        )

class CustomNameserversResourceWithStreamingResponse:
    def __init__(self, custom_nameservers: CustomNameserversResource) -> None:
        self._custom_nameservers = custom_nameservers

        self.create = to_streamed_response_wrapper(
            custom_nameservers.create,
        )
        self.delete = to_streamed_response_wrapper(
            custom_nameservers.delete,
        )
        self.availabilty = to_streamed_response_wrapper(
            custom_nameservers.availabilty,
        )
        self.get = to_streamed_response_wrapper(
            custom_nameservers.get,
        )

class AsyncCustomNameserversResourceWithStreamingResponse:
    def __init__(self, custom_nameservers: AsyncCustomNameserversResource) -> None:
        self._custom_nameservers = custom_nameservers

        self.create = async_to_streamed_response_wrapper(
            custom_nameservers.create,
        )
        self.delete = async_to_streamed_response_wrapper(
            custom_nameservers.delete,
        )
        self.availabilty = async_to_streamed_response_wrapper(
            custom_nameservers.availabilty,
        )
        self.get = async_to_streamed_response_wrapper(
            custom_nameservers.get,
        )