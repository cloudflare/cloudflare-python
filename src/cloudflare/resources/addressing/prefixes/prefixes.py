# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Optional, cast

import httpx

from .bgp import (
    BGPResource,
    AsyncBGPResource,
    BGPResourceWithRawResponse,
    AsyncBGPResourceWithRawResponse,
    BGPResourceWithStreamingResponse,
    AsyncBGPResourceWithStreamingResponse,
)
from .bgp.bgp import BGPResource, AsyncBGPResource
from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ...._compat import cached_property
from .delegations import (
    DelegationsResource,
    AsyncDelegationsResource,
    DelegationsResourceWithRawResponse,
    AsyncDelegationsResourceWithRawResponse,
    DelegationsResourceWithStreamingResponse,
    AsyncDelegationsResourceWithStreamingResponse,
)
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
from ....types.addressing import prefix_edit_params, prefix_create_params
from ....types.addressing.prefix import Prefix
from ....types.addressing.prefix_delete_response import PrefixDeleteResponse

__all__ = ["PrefixesResource", "AsyncPrefixesResource"]


class PrefixesResource(SyncAPIResource):
    @cached_property
    def bgp(self) -> BGPResource:
        return BGPResource(self._client)

    @cached_property
    def delegations(self) -> DelegationsResource:
        return DelegationsResource(self._client)

    @cached_property
    def with_raw_response(self) -> PrefixesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return PrefixesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PrefixesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return PrefixesResourceWithStreamingResponse(self)

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
    ) -> Optional[Prefix]:
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
                post_parser=ResultWrapper[Optional[Prefix]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[Prefix]], ResultWrapper[Prefix]),
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
    ) -> SyncSinglePage[Prefix]:
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
        return self._get_api_list(
            f"/accounts/{account_id}/addressing/prefixes",
            page=SyncSinglePage[Prefix],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=Prefix,
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
    ) -> PrefixDeleteResponse:
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
        return self._delete(
            f"/accounts/{account_id}/addressing/prefixes/{prefix_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PrefixDeleteResponse,
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
    ) -> Optional[Prefix]:
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
                post_parser=ResultWrapper[Optional[Prefix]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[Prefix]], ResultWrapper[Prefix]),
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
    ) -> Optional[Prefix]:
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
                post_parser=ResultWrapper[Optional[Prefix]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[Prefix]], ResultWrapper[Prefix]),
        )


class AsyncPrefixesResource(AsyncAPIResource):
    @cached_property
    def bgp(self) -> AsyncBGPResource:
        return AsyncBGPResource(self._client)

    @cached_property
    def delegations(self) -> AsyncDelegationsResource:
        return AsyncDelegationsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncPrefixesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPrefixesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPrefixesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncPrefixesResourceWithStreamingResponse(self)

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
    ) -> Optional[Prefix]:
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
                post_parser=ResultWrapper[Optional[Prefix]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[Prefix]], ResultWrapper[Prefix]),
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
    ) -> AsyncPaginator[Prefix, AsyncSinglePage[Prefix]]:
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
        return self._get_api_list(
            f"/accounts/{account_id}/addressing/prefixes",
            page=AsyncSinglePage[Prefix],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=Prefix,
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
    ) -> PrefixDeleteResponse:
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
        return await self._delete(
            f"/accounts/{account_id}/addressing/prefixes/{prefix_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PrefixDeleteResponse,
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
    ) -> Optional[Prefix]:
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
                post_parser=ResultWrapper[Optional[Prefix]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[Prefix]], ResultWrapper[Prefix]),
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
    ) -> Optional[Prefix]:
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
                post_parser=ResultWrapper[Optional[Prefix]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[Prefix]], ResultWrapper[Prefix]),
        )


class PrefixesResourceWithRawResponse:
    def __init__(self, prefixes: PrefixesResource) -> None:
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
    def bgp(self) -> BGPResourceWithRawResponse:
        return BGPResourceWithRawResponse(self._prefixes.bgp)

    @cached_property
    def delegations(self) -> DelegationsResourceWithRawResponse:
        return DelegationsResourceWithRawResponse(self._prefixes.delegations)


class AsyncPrefixesResourceWithRawResponse:
    def __init__(self, prefixes: AsyncPrefixesResource) -> None:
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
    def bgp(self) -> AsyncBGPResourceWithRawResponse:
        return AsyncBGPResourceWithRawResponse(self._prefixes.bgp)

    @cached_property
    def delegations(self) -> AsyncDelegationsResourceWithRawResponse:
        return AsyncDelegationsResourceWithRawResponse(self._prefixes.delegations)


class PrefixesResourceWithStreamingResponse:
    def __init__(self, prefixes: PrefixesResource) -> None:
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
    def bgp(self) -> BGPResourceWithStreamingResponse:
        return BGPResourceWithStreamingResponse(self._prefixes.bgp)

    @cached_property
    def delegations(self) -> DelegationsResourceWithStreamingResponse:
        return DelegationsResourceWithStreamingResponse(self._prefixes.delegations)


class AsyncPrefixesResourceWithStreamingResponse:
    def __init__(self, prefixes: AsyncPrefixesResource) -> None:
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
    def bgp(self) -> AsyncBGPResourceWithStreamingResponse:
        return AsyncBGPResourceWithStreamingResponse(self._prefixes.bgp)

    @cached_property
    def delegations(self) -> AsyncDelegationsResourceWithStreamingResponse:
        return AsyncDelegationsResourceWithStreamingResponse(self._prefixes.delegations)
