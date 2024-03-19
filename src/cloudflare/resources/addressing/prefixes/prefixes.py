# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, Type, Optional, cast

import httpx

from .bgp import (
    BGP,
    AsyncBGP,
    BGPWithRawResponse,
    AsyncBGPWithRawResponse,
    BGPWithStreamingResponse,
    AsyncBGPWithStreamingResponse,
)
from .bgp.bgp import BGP, AsyncBGP
from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ...._compat import cached_property
from .delegations import (
    Delegations,
    AsyncDelegations,
    DelegationsWithRawResponse,
    AsyncDelegationsWithRawResponse,
    DelegationsWithStreamingResponse,
    AsyncDelegationsWithStreamingResponse,
)
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
from ....types.addressing import (
    PrefixListResponse,
    PrefixDeleteResponse,
    AddressingIpamPrefixes,
    prefix_edit_params,
    prefix_create_params,
)

__all__ = ["Prefixes", "AsyncPrefixes"]


class Prefixes(SyncAPIResource):
    @cached_property
    def bgp(self) -> BGP:
        return BGP(self._client)

    @cached_property
    def delegations(self) -> Delegations:
        return Delegations(self._client)

    @cached_property
    def with_raw_response(self) -> PrefixesWithRawResponse:
        return PrefixesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PrefixesWithStreamingResponse:
        return PrefixesWithStreamingResponse(self)

    def create(
        self,
        *,
        account_id: str,
        asn: Optional[int],
        cidr: str,
        loa_document_id: Optional[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AddressingIpamPrefixes:
        """
        Add a new prefix under the account.

        Args:
          account_id: Identifier

          asn: Autonomous System Number (ASN) the prefix will be advertised under.

          cidr: IP Prefix in Classless Inter-Domain Routing format.

          loa_document_id: Identifier for the uploaded LOA document.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._post(
            f"/accounts/{account_id}/addressing/prefixes",
            body=maybe_transform(
                {
                    "asn": asn,
                    "cidr": cidr,
                    "loa_document_id": loa_document_id,
                },
                prefix_create_params.PrefixCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[AddressingIpamPrefixes], ResultWrapper[AddressingIpamPrefixes]),
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
    ) -> Optional[PrefixListResponse]:
        """
        List all prefixes owned by the account.

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
            f"/accounts/{account_id}/addressing/prefixes",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[PrefixListResponse]], ResultWrapper[PrefixListResponse]),
        )

    def delete(
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
    ) -> Optional[PrefixDeleteResponse]:
        """
        Delete an unapproved prefix owned by the account.

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
        return cast(
            Optional[PrefixDeleteResponse],
            self._delete(
                f"/accounts/{account_id}/addressing/prefixes/{prefix_id}",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[PrefixDeleteResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def edit(
        self,
        prefix_id: str,
        *,
        account_id: str,
        description: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AddressingIpamPrefixes:
        """
        Modify the description for a prefix owned by the account.

        Args:
          account_id: Identifier

          prefix_id: Identifier

          description: Description of the prefix.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not prefix_id:
            raise ValueError(f"Expected a non-empty value for `prefix_id` but received {prefix_id!r}")
        return self._patch(
            f"/accounts/{account_id}/addressing/prefixes/{prefix_id}",
            body=maybe_transform({"description": description}, prefix_edit_params.PrefixEditParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[AddressingIpamPrefixes], ResultWrapper[AddressingIpamPrefixes]),
        )

    def get(
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
    ) -> AddressingIpamPrefixes:
        """
        List a particular prefix owned by the account.

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
            f"/accounts/{account_id}/addressing/prefixes/{prefix_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[AddressingIpamPrefixes], ResultWrapper[AddressingIpamPrefixes]),
        )


class AsyncPrefixes(AsyncAPIResource):
    @cached_property
    def bgp(self) -> AsyncBGP:
        return AsyncBGP(self._client)

    @cached_property
    def delegations(self) -> AsyncDelegations:
        return AsyncDelegations(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncPrefixesWithRawResponse:
        return AsyncPrefixesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPrefixesWithStreamingResponse:
        return AsyncPrefixesWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_id: str,
        asn: Optional[int],
        cidr: str,
        loa_document_id: Optional[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AddressingIpamPrefixes:
        """
        Add a new prefix under the account.

        Args:
          account_id: Identifier

          asn: Autonomous System Number (ASN) the prefix will be advertised under.

          cidr: IP Prefix in Classless Inter-Domain Routing format.

          loa_document_id: Identifier for the uploaded LOA document.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._post(
            f"/accounts/{account_id}/addressing/prefixes",
            body=await async_maybe_transform(
                {
                    "asn": asn,
                    "cidr": cidr,
                    "loa_document_id": loa_document_id,
                },
                prefix_create_params.PrefixCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[AddressingIpamPrefixes], ResultWrapper[AddressingIpamPrefixes]),
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
    ) -> Optional[PrefixListResponse]:
        """
        List all prefixes owned by the account.

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
            f"/accounts/{account_id}/addressing/prefixes",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[PrefixListResponse]], ResultWrapper[PrefixListResponse]),
        )

    async def delete(
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
    ) -> Optional[PrefixDeleteResponse]:
        """
        Delete an unapproved prefix owned by the account.

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
        return cast(
            Optional[PrefixDeleteResponse],
            await self._delete(
                f"/accounts/{account_id}/addressing/prefixes/{prefix_id}",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[PrefixDeleteResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def edit(
        self,
        prefix_id: str,
        *,
        account_id: str,
        description: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AddressingIpamPrefixes:
        """
        Modify the description for a prefix owned by the account.

        Args:
          account_id: Identifier

          prefix_id: Identifier

          description: Description of the prefix.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not prefix_id:
            raise ValueError(f"Expected a non-empty value for `prefix_id` but received {prefix_id!r}")
        return await self._patch(
            f"/accounts/{account_id}/addressing/prefixes/{prefix_id}",
            body=await async_maybe_transform({"description": description}, prefix_edit_params.PrefixEditParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[AddressingIpamPrefixes], ResultWrapper[AddressingIpamPrefixes]),
        )

    async def get(
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
    ) -> AddressingIpamPrefixes:
        """
        List a particular prefix owned by the account.

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
            f"/accounts/{account_id}/addressing/prefixes/{prefix_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[AddressingIpamPrefixes], ResultWrapper[AddressingIpamPrefixes]),
        )


class PrefixesWithRawResponse:
    def __init__(self, prefixes: Prefixes) -> None:
        self._prefixes = prefixes

        self.create = to_raw_response_wrapper(
            prefixes.create,
        )
        self.list = to_raw_response_wrapper(
            prefixes.list,
        )
        self.delete = to_raw_response_wrapper(
            prefixes.delete,
        )
        self.edit = to_raw_response_wrapper(
            prefixes.edit,
        )
        self.get = to_raw_response_wrapper(
            prefixes.get,
        )

    @cached_property
    def bgp(self) -> BGPWithRawResponse:
        return BGPWithRawResponse(self._prefixes.bgp)

    @cached_property
    def delegations(self) -> DelegationsWithRawResponse:
        return DelegationsWithRawResponse(self._prefixes.delegations)


class AsyncPrefixesWithRawResponse:
    def __init__(self, prefixes: AsyncPrefixes) -> None:
        self._prefixes = prefixes

        self.create = async_to_raw_response_wrapper(
            prefixes.create,
        )
        self.list = async_to_raw_response_wrapper(
            prefixes.list,
        )
        self.delete = async_to_raw_response_wrapper(
            prefixes.delete,
        )
        self.edit = async_to_raw_response_wrapper(
            prefixes.edit,
        )
        self.get = async_to_raw_response_wrapper(
            prefixes.get,
        )

    @cached_property
    def bgp(self) -> AsyncBGPWithRawResponse:
        return AsyncBGPWithRawResponse(self._prefixes.bgp)

    @cached_property
    def delegations(self) -> AsyncDelegationsWithRawResponse:
        return AsyncDelegationsWithRawResponse(self._prefixes.delegations)


class PrefixesWithStreamingResponse:
    def __init__(self, prefixes: Prefixes) -> None:
        self._prefixes = prefixes

        self.create = to_streamed_response_wrapper(
            prefixes.create,
        )
        self.list = to_streamed_response_wrapper(
            prefixes.list,
        )
        self.delete = to_streamed_response_wrapper(
            prefixes.delete,
        )
        self.edit = to_streamed_response_wrapper(
            prefixes.edit,
        )
        self.get = to_streamed_response_wrapper(
            prefixes.get,
        )

    @cached_property
    def bgp(self) -> BGPWithStreamingResponse:
        return BGPWithStreamingResponse(self._prefixes.bgp)

    @cached_property
    def delegations(self) -> DelegationsWithStreamingResponse:
        return DelegationsWithStreamingResponse(self._prefixes.delegations)


class AsyncPrefixesWithStreamingResponse:
    def __init__(self, prefixes: AsyncPrefixes) -> None:
        self._prefixes = prefixes

        self.create = async_to_streamed_response_wrapper(
            prefixes.create,
        )
        self.list = async_to_streamed_response_wrapper(
            prefixes.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            prefixes.delete,
        )
        self.edit = async_to_streamed_response_wrapper(
            prefixes.edit,
        )
        self.get = async_to_streamed_response_wrapper(
            prefixes.get,
        )

    @cached_property
    def bgp(self) -> AsyncBGPWithStreamingResponse:
        return AsyncBGPWithStreamingResponse(self._prefixes.bgp)

    @cached_property
    def delegations(self) -> AsyncDelegationsWithStreamingResponse:
        return AsyncDelegationsWithStreamingResponse(self._prefixes.delegations)
