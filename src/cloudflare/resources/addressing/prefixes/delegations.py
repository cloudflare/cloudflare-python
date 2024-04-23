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
from ...._base_client import (
    AsyncPaginator,
    make_request_options,
)
from ....types.addressing.prefixes import (
    DelegationDeleteResponse,
    delegations,
    delegation_create_params,
    delegation_delete_params,
)

__all__ = ["Delegations", "AsyncDelegations"]


class Delegations(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DelegationsWithRawResponse:
        return DelegationsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DelegationsWithStreamingResponse:
        return DelegationsWithStreamingResponse(self)

    def create(
        self,
        prefix_id: str,
        *,
        account_id: str,
        cidr: str,
        delegated_account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[delegations.Delegations]:
        """
        Create a new account delegation for a given IP prefix.

        Args:
          account_id: Identifier

          prefix_id: Identifier

          cidr: IP Prefix in Classless Inter-Domain Routing format.

          delegated_account_id: Account identifier for the account to which prefix is being delegated.

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
            f"/accounts/{account_id}/addressing/prefixes/{prefix_id}/delegations",
            body=maybe_transform(
                {
                    "cidr": cidr,
                    "delegated_account_id": delegated_account_id,
                },
                delegation_create_params.DelegationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[delegations.Delegations]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[delegations.Delegations]], ResultWrapper[delegations.Delegations]),
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
    ) -> SyncSinglePage[delegations.Delegations]:
        """
        List all delegations for a given account IP prefix.

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
        return self._get_api_list(
            f"/accounts/{account_id}/addressing/prefixes/{prefix_id}/delegations",
            page=SyncSinglePage[delegations.Delegations],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=delegations.Delegations,
        )

    def delete(
        self,
        delegation_id: str,
        *,
        account_id: str,
        prefix_id: str,
        body: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[DelegationDeleteResponse]:
        """
        Delete an account delegation for a given IP prefix.

        Args:
          account_id: Identifier

          prefix_id: Identifier

          delegation_id: Delegation identifier tag.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not prefix_id:
            raise ValueError(f"Expected a non-empty value for `prefix_id` but received {prefix_id!r}")
        if not delegation_id:
            raise ValueError(f"Expected a non-empty value for `delegation_id` but received {delegation_id!r}")
        return self._delete(
            f"/accounts/{account_id}/addressing/prefixes/{prefix_id}/delegations/{delegation_id}",
            body=maybe_transform(body, delegation_delete_params.DelegationDeleteParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[DelegationDeleteResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[DelegationDeleteResponse]], ResultWrapper[DelegationDeleteResponse]),
        )


class AsyncDelegations(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDelegationsWithRawResponse:
        return AsyncDelegationsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDelegationsWithStreamingResponse:
        return AsyncDelegationsWithStreamingResponse(self)

    async def create(
        self,
        prefix_id: str,
        *,
        account_id: str,
        cidr: str,
        delegated_account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[delegations.Delegations]:
        """
        Create a new account delegation for a given IP prefix.

        Args:
          account_id: Identifier

          prefix_id: Identifier

          cidr: IP Prefix in Classless Inter-Domain Routing format.

          delegated_account_id: Account identifier for the account to which prefix is being delegated.

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
            f"/accounts/{account_id}/addressing/prefixes/{prefix_id}/delegations",
            body=await async_maybe_transform(
                {
                    "cidr": cidr,
                    "delegated_account_id": delegated_account_id,
                },
                delegation_create_params.DelegationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[delegations.Delegations]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[delegations.Delegations]], ResultWrapper[delegations.Delegations]),
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
    ) -> AsyncPaginator[delegations.Delegations, AsyncSinglePage[delegations.Delegations]]:
        """
        List all delegations for a given account IP prefix.

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
        return self._get_api_list(
            f"/accounts/{account_id}/addressing/prefixes/{prefix_id}/delegations",
            page=AsyncSinglePage[delegations.Delegations],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=delegations.Delegations,
        )

    async def delete(
        self,
        delegation_id: str,
        *,
        account_id: str,
        prefix_id: str,
        body: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[DelegationDeleteResponse]:
        """
        Delete an account delegation for a given IP prefix.

        Args:
          account_id: Identifier

          prefix_id: Identifier

          delegation_id: Delegation identifier tag.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not prefix_id:
            raise ValueError(f"Expected a non-empty value for `prefix_id` but received {prefix_id!r}")
        if not delegation_id:
            raise ValueError(f"Expected a non-empty value for `delegation_id` but received {delegation_id!r}")
        return await self._delete(
            f"/accounts/{account_id}/addressing/prefixes/{prefix_id}/delegations/{delegation_id}",
            body=await async_maybe_transform(body, delegation_delete_params.DelegationDeleteParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[DelegationDeleteResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[DelegationDeleteResponse]], ResultWrapper[DelegationDeleteResponse]),
        )


class DelegationsWithRawResponse:
    def __init__(self, delegations: Delegations) -> None:
        self._delegations = delegations

        self.create = to_raw_response_wrapper(
            delegations.create,
        )
        self.list = to_raw_response_wrapper(
            delegations.list,
        )
        self.delete = to_raw_response_wrapper(
            delegations.delete,
        )


class AsyncDelegationsWithRawResponse:
    def __init__(self, delegations: AsyncDelegations) -> None:
        self._delegations = delegations

        self.create = async_to_raw_response_wrapper(
            delegations.create,
        )
        self.list = async_to_raw_response_wrapper(
            delegations.list,
        )
        self.delete = async_to_raw_response_wrapper(
            delegations.delete,
        )


class DelegationsWithStreamingResponse:
    def __init__(self, delegations: Delegations) -> None:
        self._delegations = delegations

        self.create = to_streamed_response_wrapper(
            delegations.create,
        )
        self.list = to_streamed_response_wrapper(
            delegations.list,
        )
        self.delete = to_streamed_response_wrapper(
            delegations.delete,
        )


class AsyncDelegationsWithStreamingResponse:
    def __init__(self, delegations: AsyncDelegations) -> None:
        self._delegations = delegations

        self.create = async_to_streamed_response_wrapper(
            delegations.create,
        )
        self.list = async_to_streamed_response_wrapper(
            delegations.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            delegations.delete,
        )
