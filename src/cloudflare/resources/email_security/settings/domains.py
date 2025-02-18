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
from ....pagination import SyncSinglePage, AsyncSinglePage, SyncV4PagePaginationArray, AsyncV4PagePaginationArray
from ...._base_client import AsyncPaginator, make_request_options
from ....types.email_security.settings import domain_edit_params, domain_list_params
from ....types.email_security.settings.domain_get_response import DomainGetResponse
from ....types.email_security.settings.domain_edit_response import DomainEditResponse
from ....types.email_security.settings.domain_list_response import DomainListResponse
from ....types.email_security.settings.domain_delete_response import DomainDeleteResponse
from ....types.email_security.settings.domain_bulk_delete_response import DomainBulkDeleteResponse

__all__ = ["DomainsResource", "AsyncDomainsResource"]


class DomainsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DomainsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return DomainsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DomainsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return DomainsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        account_id: str,
        active_delivery_mode: Literal["DIRECT", "BCC", "JOURNAL", "API", "RETRO_SCAN"] | NotGiven = NOT_GIVEN,
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
        Lists, searches, and sorts an account’s email domains.

        Args:
          account_id: Account Identifier

          active_delivery_mode: Filters response to domains with the currently active delivery mode.

          allowed_delivery_mode: Filters response to domains with the provided delivery mode.

          direction: The sorting direction.

          domain: Filters results by the provided domains, allowing for multiple occurrences.

          order: The field to sort by.

          page: The page number of paginated results.

          per_page: The number of results per page.

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
                        "active_delivery_mode": active_delivery_mode,
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

          domain_id: The unique identifier for the domain.

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

    def bulk_delete(
        self,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncSinglePage[DomainBulkDeleteResponse]:
        """
        Unprotect multiple email domains

        Args:
          account_id: Account Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/email-security/settings/domains",
            page=SyncSinglePage[DomainBulkDeleteResponse],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=DomainBulkDeleteResponse,
            method="delete",
        )

    def edit(
        self,
        domain_id: int,
        *,
        account_id: str,
        ip_restrictions: List[str],
        domain: Optional[str] | NotGiven = NOT_GIVEN,
        drop_dispositions: List[
            Literal[
                "MALICIOUS",
                "MALICIOUS-BEC",
                "SUSPICIOUS",
                "SPOOF",
                "SPAM",
                "BULK",
                "ENCRYPTED",
                "EXTERNAL",
                "UNKNOWN",
                "NONE",
            ]
        ]
        | NotGiven = NOT_GIVEN,
        folder: Literal["AllItems", "Inbox"] | NotGiven = NOT_GIVEN,
        integration_id: Optional[str] | NotGiven = NOT_GIVEN,
        lookback_hops: Optional[int] | NotGiven = NOT_GIVEN,
        require_tls_inbound: bool | NotGiven = NOT_GIVEN,
        require_tls_outbound: bool | NotGiven = NOT_GIVEN,
        transport: str | NotGiven = NOT_GIVEN,
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

          domain_id: The unique identifier for the domain.

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
                    "ip_restrictions": ip_restrictions,
                    "domain": domain,
                    "drop_dispositions": drop_dispositions,
                    "folder": folder,
                    "integration_id": integration_id,
                    "lookback_hops": lookback_hops,
                    "require_tls_inbound": require_tls_inbound,
                    "require_tls_outbound": require_tls_outbound,
                    "transport": transport,
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

    def get(
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
    ) -> DomainGetResponse:
        """
        Get an email domain

        Args:
          account_id: Account Identifier

          domain_id: The unique identifier for the domain.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get(
            f"/accounts/{account_id}/email-security/settings/domains/{domain_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[DomainGetResponse]._unwrapper,
            ),
            cast_to=cast(Type[DomainGetResponse], ResultWrapper[DomainGetResponse]),
        )


class AsyncDomainsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDomainsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDomainsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDomainsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncDomainsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        account_id: str,
        active_delivery_mode: Literal["DIRECT", "BCC", "JOURNAL", "API", "RETRO_SCAN"] | NotGiven = NOT_GIVEN,
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
        Lists, searches, and sorts an account’s email domains.

        Args:
          account_id: Account Identifier

          active_delivery_mode: Filters response to domains with the currently active delivery mode.

          allowed_delivery_mode: Filters response to domains with the provided delivery mode.

          direction: The sorting direction.

          domain: Filters results by the provided domains, allowing for multiple occurrences.

          order: The field to sort by.

          page: The page number of paginated results.

          per_page: The number of results per page.

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
                        "active_delivery_mode": active_delivery_mode,
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

          domain_id: The unique identifier for the domain.

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

    def bulk_delete(
        self,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[DomainBulkDeleteResponse, AsyncSinglePage[DomainBulkDeleteResponse]]:
        """
        Unprotect multiple email domains

        Args:
          account_id: Account Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/email-security/settings/domains",
            page=AsyncSinglePage[DomainBulkDeleteResponse],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=DomainBulkDeleteResponse,
            method="delete",
        )

    async def edit(
        self,
        domain_id: int,
        *,
        account_id: str,
        ip_restrictions: List[str],
        domain: Optional[str] | NotGiven = NOT_GIVEN,
        drop_dispositions: List[
            Literal[
                "MALICIOUS",
                "MALICIOUS-BEC",
                "SUSPICIOUS",
                "SPOOF",
                "SPAM",
                "BULK",
                "ENCRYPTED",
                "EXTERNAL",
                "UNKNOWN",
                "NONE",
            ]
        ]
        | NotGiven = NOT_GIVEN,
        folder: Literal["AllItems", "Inbox"] | NotGiven = NOT_GIVEN,
        integration_id: Optional[str] | NotGiven = NOT_GIVEN,
        lookback_hops: Optional[int] | NotGiven = NOT_GIVEN,
        require_tls_inbound: bool | NotGiven = NOT_GIVEN,
        require_tls_outbound: bool | NotGiven = NOT_GIVEN,
        transport: str | NotGiven = NOT_GIVEN,
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

          domain_id: The unique identifier for the domain.

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
                    "ip_restrictions": ip_restrictions,
                    "domain": domain,
                    "drop_dispositions": drop_dispositions,
                    "folder": folder,
                    "integration_id": integration_id,
                    "lookback_hops": lookback_hops,
                    "require_tls_inbound": require_tls_inbound,
                    "require_tls_outbound": require_tls_outbound,
                    "transport": transport,
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

    async def get(
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
    ) -> DomainGetResponse:
        """
        Get an email domain

        Args:
          account_id: Account Identifier

          domain_id: The unique identifier for the domain.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._get(
            f"/accounts/{account_id}/email-security/settings/domains/{domain_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[DomainGetResponse]._unwrapper,
            ),
            cast_to=cast(Type[DomainGetResponse], ResultWrapper[DomainGetResponse]),
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
        self.bulk_delete = to_raw_response_wrapper(
            domains.bulk_delete,
        )
        self.edit = to_raw_response_wrapper(
            domains.edit,
        )
        self.get = to_raw_response_wrapper(
            domains.get,
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
        self.bulk_delete = async_to_raw_response_wrapper(
            domains.bulk_delete,
        )
        self.edit = async_to_raw_response_wrapper(
            domains.edit,
        )
        self.get = async_to_raw_response_wrapper(
            domains.get,
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
        self.bulk_delete = to_streamed_response_wrapper(
            domains.bulk_delete,
        )
        self.edit = to_streamed_response_wrapper(
            domains.edit,
        )
        self.get = to_streamed_response_wrapper(
            domains.get,
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
        self.bulk_delete = async_to_streamed_response_wrapper(
            domains.bulk_delete,
        )
        self.edit = async_to_streamed_response_wrapper(
            domains.edit,
        )
        self.get = async_to_streamed_response_wrapper(
            domains.get,
        )
