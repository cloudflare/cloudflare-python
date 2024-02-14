# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Any, Type, Optional, cast

import httpx

from .bgps import (
    BGPs,
    AsyncBGPs,
    BGPsWithRawResponse,
    AsyncBGPsWithRawResponse,
    BGPsWithStreamingResponse,
    AsyncBGPsWithStreamingResponse,
)
from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import maybe_transform
from .bgps.bgps import BGPs, AsyncBGPs
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
from ....types.addresses import (
    PrefixGetResponse,
    PrefixDeleteResponse,
    PrefixUpdateResponse,
    PrefixIPAddressManagementPrefixesAddPrefixResponse,
    PrefixIPAddressManagementPrefixesListPrefixesResponse,
    prefix_update_params,
    prefix_ip_address_management_prefixes_add_prefix_params,
)

__all__ = ["Prefixes", "AsyncPrefixes"]


class Prefixes(SyncAPIResource):
    @cached_property
    def bgps(self) -> BGPs:
        return BGPs(self._client)

    @cached_property
    def delegations(self) -> Delegations:
        return Delegations(self._client)

    @cached_property
    def with_raw_response(self) -> PrefixesWithRawResponse:
        return PrefixesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PrefixesWithStreamingResponse:
        return PrefixesWithStreamingResponse(self)

    def update(
        self,
        prefix_identifier: str,
        *,
        account_identifier: str,
        description: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PrefixUpdateResponse:
        """
        Modify the description for a prefix owned by the account.

        Args:
          account_identifier: Identifier

          prefix_identifier: Identifier

          description: Description of the prefix.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        if not prefix_identifier:
            raise ValueError(f"Expected a non-empty value for `prefix_identifier` but received {prefix_identifier!r}")
        return self._patch(
            f"/accounts/{account_identifier}/addressing/prefixes/{prefix_identifier}",
            body=maybe_transform({"description": description}, prefix_update_params.PrefixUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[PrefixUpdateResponse], ResultWrapper[PrefixUpdateResponse]),
        )

    def delete(
        self,
        prefix_identifier: str,
        *,
        account_identifier: str,
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
          account_identifier: Identifier

          prefix_identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        if not prefix_identifier:
            raise ValueError(f"Expected a non-empty value for `prefix_identifier` but received {prefix_identifier!r}")
        return cast(
            Optional[PrefixDeleteResponse],
            self._delete(
                f"/accounts/{account_identifier}/addressing/prefixes/{prefix_identifier}",
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

    def get(
        self,
        prefix_identifier: str,
        *,
        account_identifier: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PrefixGetResponse:
        """
        List a particular prefix owned by the account.

        Args:
          account_identifier: Identifier

          prefix_identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        if not prefix_identifier:
            raise ValueError(f"Expected a non-empty value for `prefix_identifier` but received {prefix_identifier!r}")
        return self._get(
            f"/accounts/{account_identifier}/addressing/prefixes/{prefix_identifier}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[PrefixGetResponse], ResultWrapper[PrefixGetResponse]),
        )

    def ip_address_management_prefixes_add_prefix(
        self,
        account_identifier: str,
        *,
        asn: Optional[int],
        cidr: str,
        loa_document_id: Optional[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PrefixIPAddressManagementPrefixesAddPrefixResponse:
        """
        Add a new prefix under the account.

        Args:
          account_identifier: Identifier

          asn: Autonomous System Number (ASN) the prefix will be advertised under.

          cidr: IP Prefix in Classless Inter-Domain Routing format.

          loa_document_id: Identifier for the uploaded LOA document.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        return self._post(
            f"/accounts/{account_identifier}/addressing/prefixes",
            body=maybe_transform(
                {
                    "asn": asn,
                    "cidr": cidr,
                    "loa_document_id": loa_document_id,
                },
                prefix_ip_address_management_prefixes_add_prefix_params.PrefixIPAddressManagementPrefixesAddPrefixParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[PrefixIPAddressManagementPrefixesAddPrefixResponse],
                ResultWrapper[PrefixIPAddressManagementPrefixesAddPrefixResponse],
            ),
        )

    def ip_address_management_prefixes_list_prefixes(
        self,
        account_identifier: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[PrefixIPAddressManagementPrefixesListPrefixesResponse]:
        """
        List all prefixes owned by the account.

        Args:
          account_identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        return self._get(
            f"/accounts/{account_identifier}/addressing/prefixes",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[PrefixIPAddressManagementPrefixesListPrefixesResponse]],
                ResultWrapper[PrefixIPAddressManagementPrefixesListPrefixesResponse],
            ),
        )


class AsyncPrefixes(AsyncAPIResource):
    @cached_property
    def bgps(self) -> AsyncBGPs:
        return AsyncBGPs(self._client)

    @cached_property
    def delegations(self) -> AsyncDelegations:
        return AsyncDelegations(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncPrefixesWithRawResponse:
        return AsyncPrefixesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPrefixesWithStreamingResponse:
        return AsyncPrefixesWithStreamingResponse(self)

    async def update(
        self,
        prefix_identifier: str,
        *,
        account_identifier: str,
        description: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PrefixUpdateResponse:
        """
        Modify the description for a prefix owned by the account.

        Args:
          account_identifier: Identifier

          prefix_identifier: Identifier

          description: Description of the prefix.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        if not prefix_identifier:
            raise ValueError(f"Expected a non-empty value for `prefix_identifier` but received {prefix_identifier!r}")
        return await self._patch(
            f"/accounts/{account_identifier}/addressing/prefixes/{prefix_identifier}",
            body=maybe_transform({"description": description}, prefix_update_params.PrefixUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[PrefixUpdateResponse], ResultWrapper[PrefixUpdateResponse]),
        )

    async def delete(
        self,
        prefix_identifier: str,
        *,
        account_identifier: str,
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
          account_identifier: Identifier

          prefix_identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        if not prefix_identifier:
            raise ValueError(f"Expected a non-empty value for `prefix_identifier` but received {prefix_identifier!r}")
        return cast(
            Optional[PrefixDeleteResponse],
            await self._delete(
                f"/accounts/{account_identifier}/addressing/prefixes/{prefix_identifier}",
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

    async def get(
        self,
        prefix_identifier: str,
        *,
        account_identifier: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PrefixGetResponse:
        """
        List a particular prefix owned by the account.

        Args:
          account_identifier: Identifier

          prefix_identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        if not prefix_identifier:
            raise ValueError(f"Expected a non-empty value for `prefix_identifier` but received {prefix_identifier!r}")
        return await self._get(
            f"/accounts/{account_identifier}/addressing/prefixes/{prefix_identifier}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[PrefixGetResponse], ResultWrapper[PrefixGetResponse]),
        )

    async def ip_address_management_prefixes_add_prefix(
        self,
        account_identifier: str,
        *,
        asn: Optional[int],
        cidr: str,
        loa_document_id: Optional[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PrefixIPAddressManagementPrefixesAddPrefixResponse:
        """
        Add a new prefix under the account.

        Args:
          account_identifier: Identifier

          asn: Autonomous System Number (ASN) the prefix will be advertised under.

          cidr: IP Prefix in Classless Inter-Domain Routing format.

          loa_document_id: Identifier for the uploaded LOA document.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        return await self._post(
            f"/accounts/{account_identifier}/addressing/prefixes",
            body=maybe_transform(
                {
                    "asn": asn,
                    "cidr": cidr,
                    "loa_document_id": loa_document_id,
                },
                prefix_ip_address_management_prefixes_add_prefix_params.PrefixIPAddressManagementPrefixesAddPrefixParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[PrefixIPAddressManagementPrefixesAddPrefixResponse],
                ResultWrapper[PrefixIPAddressManagementPrefixesAddPrefixResponse],
            ),
        )

    async def ip_address_management_prefixes_list_prefixes(
        self,
        account_identifier: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[PrefixIPAddressManagementPrefixesListPrefixesResponse]:
        """
        List all prefixes owned by the account.

        Args:
          account_identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        return await self._get(
            f"/accounts/{account_identifier}/addressing/prefixes",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[PrefixIPAddressManagementPrefixesListPrefixesResponse]],
                ResultWrapper[PrefixIPAddressManagementPrefixesListPrefixesResponse],
            ),
        )


class PrefixesWithRawResponse:
    def __init__(self, prefixes: Prefixes) -> None:
        self._prefixes = prefixes

        self.update = to_raw_response_wrapper(
            prefixes.update,
        )
        self.delete = to_raw_response_wrapper(
            prefixes.delete,
        )
        self.get = to_raw_response_wrapper(
            prefixes.get,
        )
        self.ip_address_management_prefixes_add_prefix = to_raw_response_wrapper(
            prefixes.ip_address_management_prefixes_add_prefix,
        )
        self.ip_address_management_prefixes_list_prefixes = to_raw_response_wrapper(
            prefixes.ip_address_management_prefixes_list_prefixes,
        )

    @cached_property
    def bgps(self) -> BGPsWithRawResponse:
        return BGPsWithRawResponse(self._prefixes.bgps)

    @cached_property
    def delegations(self) -> DelegationsWithRawResponse:
        return DelegationsWithRawResponse(self._prefixes.delegations)


class AsyncPrefixesWithRawResponse:
    def __init__(self, prefixes: AsyncPrefixes) -> None:
        self._prefixes = prefixes

        self.update = async_to_raw_response_wrapper(
            prefixes.update,
        )
        self.delete = async_to_raw_response_wrapper(
            prefixes.delete,
        )
        self.get = async_to_raw_response_wrapper(
            prefixes.get,
        )
        self.ip_address_management_prefixes_add_prefix = async_to_raw_response_wrapper(
            prefixes.ip_address_management_prefixes_add_prefix,
        )
        self.ip_address_management_prefixes_list_prefixes = async_to_raw_response_wrapper(
            prefixes.ip_address_management_prefixes_list_prefixes,
        )

    @cached_property
    def bgps(self) -> AsyncBGPsWithRawResponse:
        return AsyncBGPsWithRawResponse(self._prefixes.bgps)

    @cached_property
    def delegations(self) -> AsyncDelegationsWithRawResponse:
        return AsyncDelegationsWithRawResponse(self._prefixes.delegations)


class PrefixesWithStreamingResponse:
    def __init__(self, prefixes: Prefixes) -> None:
        self._prefixes = prefixes

        self.update = to_streamed_response_wrapper(
            prefixes.update,
        )
        self.delete = to_streamed_response_wrapper(
            prefixes.delete,
        )
        self.get = to_streamed_response_wrapper(
            prefixes.get,
        )
        self.ip_address_management_prefixes_add_prefix = to_streamed_response_wrapper(
            prefixes.ip_address_management_prefixes_add_prefix,
        )
        self.ip_address_management_prefixes_list_prefixes = to_streamed_response_wrapper(
            prefixes.ip_address_management_prefixes_list_prefixes,
        )

    @cached_property
    def bgps(self) -> BGPsWithStreamingResponse:
        return BGPsWithStreamingResponse(self._prefixes.bgps)

    @cached_property
    def delegations(self) -> DelegationsWithStreamingResponse:
        return DelegationsWithStreamingResponse(self._prefixes.delegations)


class AsyncPrefixesWithStreamingResponse:
    def __init__(self, prefixes: AsyncPrefixes) -> None:
        self._prefixes = prefixes

        self.update = async_to_streamed_response_wrapper(
            prefixes.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            prefixes.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            prefixes.get,
        )
        self.ip_address_management_prefixes_add_prefix = async_to_streamed_response_wrapper(
            prefixes.ip_address_management_prefixes_add_prefix,
        )
        self.ip_address_management_prefixes_list_prefixes = async_to_streamed_response_wrapper(
            prefixes.ip_address_management_prefixes_list_prefixes,
        )

    @cached_property
    def bgps(self) -> AsyncBGPsWithStreamingResponse:
        return AsyncBGPsWithStreamingResponse(self._prefixes.bgps)

    @cached_property
    def delegations(self) -> AsyncDelegationsWithStreamingResponse:
        return AsyncDelegationsWithStreamingResponse(self._prefixes.delegations)
