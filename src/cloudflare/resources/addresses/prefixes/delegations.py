# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from ...._compat import cached_property

from ....types.addresses.prefixes import (
    DelegationDeleteResponse,
    DelegationIPAddressManagementPrefixDelegationCreatePrefixDelegationResponse,
    DelegationIPAddressManagementPrefixDelegationListPrefixDelegationsResponse,
)

from typing import Type, Optional

from ...._response import (
    to_raw_response_wrapper,
    async_to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_streamed_response_wrapper,
)

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ...._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ...._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._base_client import (
    SyncAPIClient,
    AsyncAPIClient,
    _merge_mappings,
    AsyncPaginator,
    make_request_options,
    HttpxBinaryResponseContent,
)
from ....types import shared_params
from ....types.addresses.prefixes import (
    delegation_ip_address_management_prefix_delegation_create_prefix_delegation_params,
)
from ...._wrappers import ResultWrapper
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast

__all__ = ["Delegations", "AsyncDelegations"]


class Delegations(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DelegationsWithRawResponse:
        return DelegationsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DelegationsWithStreamingResponse:
        return DelegationsWithStreamingResponse(self)

    def delete(
        self,
        delegation_identifier: str,
        *,
        account_identifier: str,
        prefix_identifier: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DelegationDeleteResponse:
        """
        Delete an account delegation for a given IP prefix.

        Args:
          account_identifier: Identifier

          prefix_identifier: Identifier

          delegation_identifier: Delegation identifier tag.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        if not prefix_identifier:
            raise ValueError(f"Expected a non-empty value for `prefix_identifier` but received {prefix_identifier!r}")
        if not delegation_identifier:
            raise ValueError(
                f"Expected a non-empty value for `delegation_identifier` but received {delegation_identifier!r}"
            )
        return self._delete(
            f"/accounts/{account_identifier}/addressing/prefixes/{prefix_identifier}/delegations/{delegation_identifier}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[DelegationDeleteResponse], ResultWrapper[DelegationDeleteResponse]),
        )

    def ip_address_management_prefix_delegation_create_prefix_delegation(
        self,
        prefix_identifier: str,
        *,
        account_identifier: str,
        cidr: str,
        delegated_account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DelegationIPAddressManagementPrefixDelegationCreatePrefixDelegationResponse:
        """
        Create a new account delegation for a given IP prefix.

        Args:
          account_identifier: Identifier

          prefix_identifier: Identifier

          cidr: IP Prefix in Classless Inter-Domain Routing format.

          delegated_account_id: Account identifier for the account to which prefix is being delegated.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        if not prefix_identifier:
            raise ValueError(f"Expected a non-empty value for `prefix_identifier` but received {prefix_identifier!r}")
        return self._post(
            f"/accounts/{account_identifier}/addressing/prefixes/{prefix_identifier}/delegations",
            body=maybe_transform(
                {
                    "cidr": cidr,
                    "delegated_account_id": delegated_account_id,
                },
                delegation_ip_address_management_prefix_delegation_create_prefix_delegation_params.DelegationIPAddressManagementPrefixDelegationCreatePrefixDelegationParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[DelegationIPAddressManagementPrefixDelegationCreatePrefixDelegationResponse],
                ResultWrapper[DelegationIPAddressManagementPrefixDelegationCreatePrefixDelegationResponse],
            ),
        )

    def ip_address_management_prefix_delegation_list_prefix_delegations(
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
    ) -> Optional[DelegationIPAddressManagementPrefixDelegationListPrefixDelegationsResponse]:
        """
        List all delegations for a given account IP prefix.

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
            f"/accounts/{account_identifier}/addressing/prefixes/{prefix_identifier}/delegations",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[DelegationIPAddressManagementPrefixDelegationListPrefixDelegationsResponse]],
                ResultWrapper[DelegationIPAddressManagementPrefixDelegationListPrefixDelegationsResponse],
            ),
        )


class AsyncDelegations(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDelegationsWithRawResponse:
        return AsyncDelegationsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDelegationsWithStreamingResponse:
        return AsyncDelegationsWithStreamingResponse(self)

    async def delete(
        self,
        delegation_identifier: str,
        *,
        account_identifier: str,
        prefix_identifier: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DelegationDeleteResponse:
        """
        Delete an account delegation for a given IP prefix.

        Args:
          account_identifier: Identifier

          prefix_identifier: Identifier

          delegation_identifier: Delegation identifier tag.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        if not prefix_identifier:
            raise ValueError(f"Expected a non-empty value for `prefix_identifier` but received {prefix_identifier!r}")
        if not delegation_identifier:
            raise ValueError(
                f"Expected a non-empty value for `delegation_identifier` but received {delegation_identifier!r}"
            )
        return await self._delete(
            f"/accounts/{account_identifier}/addressing/prefixes/{prefix_identifier}/delegations/{delegation_identifier}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[DelegationDeleteResponse], ResultWrapper[DelegationDeleteResponse]),
        )

    async def ip_address_management_prefix_delegation_create_prefix_delegation(
        self,
        prefix_identifier: str,
        *,
        account_identifier: str,
        cidr: str,
        delegated_account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DelegationIPAddressManagementPrefixDelegationCreatePrefixDelegationResponse:
        """
        Create a new account delegation for a given IP prefix.

        Args:
          account_identifier: Identifier

          prefix_identifier: Identifier

          cidr: IP Prefix in Classless Inter-Domain Routing format.

          delegated_account_id: Account identifier for the account to which prefix is being delegated.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        if not prefix_identifier:
            raise ValueError(f"Expected a non-empty value for `prefix_identifier` but received {prefix_identifier!r}")
        return await self._post(
            f"/accounts/{account_identifier}/addressing/prefixes/{prefix_identifier}/delegations",
            body=maybe_transform(
                {
                    "cidr": cidr,
                    "delegated_account_id": delegated_account_id,
                },
                delegation_ip_address_management_prefix_delegation_create_prefix_delegation_params.DelegationIPAddressManagementPrefixDelegationCreatePrefixDelegationParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[DelegationIPAddressManagementPrefixDelegationCreatePrefixDelegationResponse],
                ResultWrapper[DelegationIPAddressManagementPrefixDelegationCreatePrefixDelegationResponse],
            ),
        )

    async def ip_address_management_prefix_delegation_list_prefix_delegations(
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
    ) -> Optional[DelegationIPAddressManagementPrefixDelegationListPrefixDelegationsResponse]:
        """
        List all delegations for a given account IP prefix.

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
            f"/accounts/{account_identifier}/addressing/prefixes/{prefix_identifier}/delegations",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[DelegationIPAddressManagementPrefixDelegationListPrefixDelegationsResponse]],
                ResultWrapper[DelegationIPAddressManagementPrefixDelegationListPrefixDelegationsResponse],
            ),
        )


class DelegationsWithRawResponse:
    def __init__(self, delegations: Delegations) -> None:
        self._delegations = delegations

        self.delete = to_raw_response_wrapper(
            delegations.delete,
        )
        self.ip_address_management_prefix_delegation_create_prefix_delegation = to_raw_response_wrapper(
            delegations.ip_address_management_prefix_delegation_create_prefix_delegation,
        )
        self.ip_address_management_prefix_delegation_list_prefix_delegations = to_raw_response_wrapper(
            delegations.ip_address_management_prefix_delegation_list_prefix_delegations,
        )


class AsyncDelegationsWithRawResponse:
    def __init__(self, delegations: AsyncDelegations) -> None:
        self._delegations = delegations

        self.delete = async_to_raw_response_wrapper(
            delegations.delete,
        )
        self.ip_address_management_prefix_delegation_create_prefix_delegation = async_to_raw_response_wrapper(
            delegations.ip_address_management_prefix_delegation_create_prefix_delegation,
        )
        self.ip_address_management_prefix_delegation_list_prefix_delegations = async_to_raw_response_wrapper(
            delegations.ip_address_management_prefix_delegation_list_prefix_delegations,
        )


class DelegationsWithStreamingResponse:
    def __init__(self, delegations: Delegations) -> None:
        self._delegations = delegations

        self.delete = to_streamed_response_wrapper(
            delegations.delete,
        )
        self.ip_address_management_prefix_delegation_create_prefix_delegation = to_streamed_response_wrapper(
            delegations.ip_address_management_prefix_delegation_create_prefix_delegation,
        )
        self.ip_address_management_prefix_delegation_list_prefix_delegations = to_streamed_response_wrapper(
            delegations.ip_address_management_prefix_delegation_list_prefix_delegations,
        )


class AsyncDelegationsWithStreamingResponse:
    def __init__(self, delegations: AsyncDelegations) -> None:
        self._delegations = delegations

        self.delete = async_to_streamed_response_wrapper(
            delegations.delete,
        )
        self.ip_address_management_prefix_delegation_create_prefix_delegation = async_to_streamed_response_wrapper(
            delegations.ip_address_management_prefix_delegation_create_prefix_delegation,
        )
        self.ip_address_management_prefix_delegation_list_prefix_delegations = async_to_streamed_response_wrapper(
            delegations.ip_address_management_prefix_delegation_list_prefix_delegations,
        )
