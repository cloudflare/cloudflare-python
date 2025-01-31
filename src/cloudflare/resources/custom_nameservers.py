# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Optional, cast

import httpx

from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import (
    maybe_transform,
    async_maybe_transform,
)
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._wrappers import ResultWrapper
from ..pagination import SyncSinglePage, AsyncSinglePage
from .._base_client import AsyncPaginator, make_request_options
from ..types.custom_nameservers import custom_nameserver_create_params
from ..types.custom_nameservers.custom_nameserver import CustomNameserver
from ..types.custom_nameservers.custom_nameserver_delete_response import CustomNameserverDeleteResponse
from ..types.custom_nameservers.custom_nameserver_availabilty_response import CustomNameserverAvailabiltyResponse

__all__ = ["CustomNameserversResource", "AsyncCustomNameserversResource"]


class CustomNameserversResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CustomNameserversResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return CustomNameserversResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CustomNameserversResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return CustomNameserversResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        account_id: str,
        ns_name: str,
        ns_set: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[CustomNameserver]:
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
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._post(
            f"/accounts/{account_id}/custom_ns",
            body=maybe_transform(
                {
                    "ns_name": ns_name,
                    "ns_set": ns_set,
                },
                custom_nameserver_create_params.CustomNameserverCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[CustomNameserver]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[CustomNameserver]], ResultWrapper[CustomNameserver]),
        )

    def delete(
        self,
        custom_ns_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncSinglePage[CustomNameserverDeleteResponse]:
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
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not custom_ns_id:
            raise ValueError(f"Expected a non-empty value for `custom_ns_id` but received {custom_ns_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/custom_ns/{custom_ns_id}",
            page=SyncSinglePage[CustomNameserverDeleteResponse],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=str,
            method="delete",
        )

    def availabilty(
        self,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncSinglePage[CustomNameserverAvailabiltyResponse]:
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
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/custom_ns/availability",
            page=SyncSinglePage[CustomNameserverAvailabiltyResponse],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=str,
        )

    def get(
        self,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncSinglePage[CustomNameserver]:
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
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/custom_ns",
            page=SyncSinglePage[CustomNameserver],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=CustomNameserver,
        )


class AsyncCustomNameserversResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCustomNameserversResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCustomNameserversResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCustomNameserversResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncCustomNameserversResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_id: str,
        ns_name: str,
        ns_set: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[CustomNameserver]:
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
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._post(
            f"/accounts/{account_id}/custom_ns",
            body=await async_maybe_transform(
                {
                    "ns_name": ns_name,
                    "ns_set": ns_set,
                },
                custom_nameserver_create_params.CustomNameserverCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[CustomNameserver]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[CustomNameserver]], ResultWrapper[CustomNameserver]),
        )

    def delete(
        self,
        custom_ns_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[CustomNameserverDeleteResponse, AsyncSinglePage[CustomNameserverDeleteResponse]]:
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
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not custom_ns_id:
            raise ValueError(f"Expected a non-empty value for `custom_ns_id` but received {custom_ns_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/custom_ns/{custom_ns_id}",
            page=AsyncSinglePage[CustomNameserverDeleteResponse],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=str,
            method="delete",
        )

    def availabilty(
        self,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[CustomNameserverAvailabiltyResponse, AsyncSinglePage[CustomNameserverAvailabiltyResponse]]:
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
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/custom_ns/availability",
            page=AsyncSinglePage[CustomNameserverAvailabiltyResponse],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=str,
        )

    def get(
        self,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[CustomNameserver, AsyncSinglePage[CustomNameserver]]:
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
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/custom_ns",
            page=AsyncSinglePage[CustomNameserver],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=CustomNameserver,
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
