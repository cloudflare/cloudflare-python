# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Type, Optional, cast
from typing_extensions import Literal

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
from ....pagination import SyncV4PagePaginationArray, AsyncV4PagePaginationArray
from ...._base_client import AsyncPaginator, make_request_options
from ....types.email_security.settings import domain_edit_params, domain_list_params
from ....types.email_security.settings.domain_edit_response import DomainEditResponse
from ....types.email_security.settings.domain_list_response import DomainListResponse
from ....types.email_security.settings.domain_delete_response import DomainDeleteResponse

__all__ = ["DomainsResource", "AsyncDomainsResource"]


class DomainsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DomainsResourceWithRawResponse:
        return DomainsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DomainsResourceWithStreamingResponse:
        return DomainsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        account_id: str,
        allowed_delivery_mode: Literal["DIRECT", "BCC", "JOURNAL", "API", "RETRO_SCAN"] | NotGiven = NOT_GIVEN,
        direction: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
        domain: List[str] | NotGiven = NOT_GIVEN,
        order: Literal["domain", "created_at"] | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        search: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncV4PagePaginationArray[DomainListResponse]:
        """
        List, search, and sort an account's email domains.

        Args:
          account_id: Account Identifier

          allowed_delivery_mode: If present, the response contains only domains with the provided delivery mode.

          direction: The sorting direction.

          domain: Filter result by the provided domains. Allows for multiple occurrences, e.g.,
              `domain=example.com&domain=example.xyz`.

          order: The field to sort by.

          page: Page number of paginated results.

          per_page: Number of results to display.

          search: Allows searching in multiple properties of a record simultaneously. This
              parameter is intended for human users, not automation. Its exact behavior is
              intentionally left unspecified and is subject to change in the future.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/email-security/settings/domains",
            page=SyncV4PagePaginationArray[DomainListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "allowed_delivery_mode": allowed_delivery_mode,
                        "direction": direction,
                        "domain": domain,
                        "order": order,
                        "page": page,
                        "per_page": per_page,
                        "search": search,
                    },
                    domain_list_params.DomainListParams,
                ),
            ),
            model=DomainListResponse,
        )

    def delete(
        self,
        domain_id: int,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DomainDeleteResponse:
        """
        Unprotect an email domain

        Args:
          account_id: Account Identifier

          domain_id: Unique domain identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._delete(
            f"/accounts/{account_id}/email-security/settings/domains/{domain_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[DomainDeleteResponse]._unwrapper,
            ),
            cast_to=cast(Type[DomainDeleteResponse], ResultWrapper[DomainDeleteResponse]),
        )

    def edit(
        self,
        domain_id: int,
        *,
        account_id: str,
        domain: Optional[str] | NotGiven = NOT_GIVEN,
        lookback_hops: Optional[int] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DomainEditResponse:
        """
        Update an email domain

        Args:
          account_id: Account Identifier

          domain_id: Unique domain identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._patch(
            f"/accounts/{account_id}/email-security/settings/domains/{domain_id}",
            body=maybe_transform(
                {
                    "domain": domain,
                    "lookback_hops": lookback_hops,
                },
                domain_edit_params.DomainEditParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[DomainEditResponse]._unwrapper,
            ),
            cast_to=cast(Type[DomainEditResponse], ResultWrapper[DomainEditResponse]),
        )


class AsyncDomainsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDomainsResourceWithRawResponse:
        return AsyncDomainsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDomainsResourceWithStreamingResponse:
        return AsyncDomainsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        account_id: str,
        allowed_delivery_mode: Literal["DIRECT", "BCC", "JOURNAL", "API", "RETRO_SCAN"] | NotGiven = NOT_GIVEN,
        direction: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
        domain: List[str] | NotGiven = NOT_GIVEN,
        order: Literal["domain", "created_at"] | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        search: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[DomainListResponse, AsyncV4PagePaginationArray[DomainListResponse]]:
        """
        List, search, and sort an account's email domains.

        Args:
          account_id: Account Identifier

          allowed_delivery_mode: If present, the response contains only domains with the provided delivery mode.

          direction: The sorting direction.

          domain: Filter result by the provided domains. Allows for multiple occurrences, e.g.,
              `domain=example.com&domain=example.xyz`.

          order: The field to sort by.

          page: Page number of paginated results.

          per_page: Number of results to display.

          search: Allows searching in multiple properties of a record simultaneously. This
              parameter is intended for human users, not automation. Its exact behavior is
              intentionally left unspecified and is subject to change in the future.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/email-security/settings/domains",
            page=AsyncV4PagePaginationArray[DomainListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "allowed_delivery_mode": allowed_delivery_mode,
                        "direction": direction,
                        "domain": domain,
                        "order": order,
                        "page": page,
                        "per_page": per_page,
                        "search": search,
                    },
                    domain_list_params.DomainListParams,
                ),
            ),
            model=DomainListResponse,
        )

    async def delete(
        self,
        domain_id: int,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DomainDeleteResponse:
        """
        Unprotect an email domain

        Args:
          account_id: Account Identifier

          domain_id: Unique domain identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._delete(
            f"/accounts/{account_id}/email-security/settings/domains/{domain_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[DomainDeleteResponse]._unwrapper,
            ),
            cast_to=cast(Type[DomainDeleteResponse], ResultWrapper[DomainDeleteResponse]),
        )

    async def edit(
        self,
        domain_id: int,
        *,
        account_id: str,
        domain: Optional[str] | NotGiven = NOT_GIVEN,
        lookback_hops: Optional[int] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DomainEditResponse:
        """
        Update an email domain

        Args:
          account_id: Account Identifier

          domain_id: Unique domain identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._patch(
            f"/accounts/{account_id}/email-security/settings/domains/{domain_id}",
            body=await async_maybe_transform(
                {
                    "domain": domain,
                    "lookback_hops": lookback_hops,
                },
                domain_edit_params.DomainEditParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[DomainEditResponse]._unwrapper,
            ),
            cast_to=cast(Type[DomainEditResponse], ResultWrapper[DomainEditResponse]),
        )


class DomainsResourceWithRawResponse:
    def __init__(self, domains: DomainsResource) -> None:
        self._domains = domains

        self.list = to_raw_response_wrapper(
            domains.list,
        )
        self.delete = to_raw_response_wrapper(
            domains.delete,
        )
        self.edit = to_raw_response_wrapper(
            domains.edit,
        )


class AsyncDomainsResourceWithRawResponse:
    def __init__(self, domains: AsyncDomainsResource) -> None:
        self._domains = domains

        self.list = async_to_raw_response_wrapper(
            domains.list,
        )
        self.delete = async_to_raw_response_wrapper(
            domains.delete,
        )
        self.edit = async_to_raw_response_wrapper(
            domains.edit,
        )


class DomainsResourceWithStreamingResponse:
    def __init__(self, domains: DomainsResource) -> None:
        self._domains = domains

        self.list = to_streamed_response_wrapper(
            domains.list,
        )
        self.delete = to_streamed_response_wrapper(
            domains.delete,
        )
        self.edit = to_streamed_response_wrapper(
            domains.edit,
        )


class AsyncDomainsResourceWithStreamingResponse:
    def __init__(self, domains: AsyncDomainsResource) -> None:
        self._domains = domains

        self.list = async_to_streamed_response_wrapper(
            domains.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            domains.delete,
        )
        self.edit = async_to_streamed_response_wrapper(
            domains.edit,
        )
