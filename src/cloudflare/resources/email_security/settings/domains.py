# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Type, Optional, cast
from typing_extensions import Literal

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ...._utils import path_template, maybe_transform, async_maybe_transform
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
from ....types.email_security.settings.domain_get_response import DomainGetResponse
from ....types.email_security.settings.domain_edit_response import DomainEditResponse
from ....types.email_security.settings.domain_list_response import DomainListResponse
from ....types.email_security.settings.domain_delete_response import DomainDeleteResponse

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
        active_delivery_mode: Literal["DIRECT", "BCC", "JOURNAL", "API", "RETRO_SCAN"] | Omit = omit,
        allowed_delivery_mode: Literal["DIRECT", "BCC", "JOURNAL", "API", "RETRO_SCAN"] | Omit = omit,
        direction: Literal["asc", "desc"] | Omit = omit,
        domain: SequenceNotStr[str] | Omit = omit,
        integration_id: str | Omit = omit,
        order: Literal["domain", "created_at"] | Omit = omit,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        search: str | Omit = omit,
        status: Literal["pending", "active", "failed", "timeout"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncV4PagePaginationArray[DomainListResponse]:
        """Returns a paginated list of email domains protected by Email Security.

        Includes
        domain configuration, delivery modes, and authorization status. Supports
        filtering by delivery mode and integration ID.

        Args:
          account_id: Identifier.

          active_delivery_mode: Currently active delivery mode to filter by.

          allowed_delivery_mode: Delivery mode to filter by.

          direction: The sorting direction.

          domain: Domain names to filter by.

          integration_id: Integration ID to filter by.

          order: Field to sort by.

          page: Current page within paginated list of results.

          per_page: The number of results per page. Maximum value is 1000.

          search: Search term for filtering records. Behavior may change.

          status: Filters response to domains with the provided status.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            path_template("/accounts/{account_id}/email-security/settings/domains", account_id=account_id),
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
                        "integration_id": integration_id,
                        "order": order,
                        "page": page,
                        "per_page": per_page,
                        "search": search,
                        "status": status,
                    },
                    domain_list_params.DomainListParams,
                ),
            ),
            model=DomainListResponse,
        )

    def delete(
        self,
        domain_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[DomainDeleteResponse]:
        """Removes email security protection from a domain.

        After deletion, emails for this
        domain will no longer be processed by Email Security. This action cannot be
        undone.

        Args:
          account_id: Identifier.

          domain_id: Domain identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not domain_id:
            raise ValueError(f"Expected a non-empty value for `domain_id` but received {domain_id!r}")
        return self._delete(
            path_template(
                "/accounts/{account_id}/email-security/settings/domains/{domain_id}",
                account_id=account_id,
                domain_id=domain_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[DomainDeleteResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[DomainDeleteResponse]], ResultWrapper[DomainDeleteResponse]),
        )

    def edit(
        self,
        domain_id: str,
        *,
        account_id: str,
        allowed_delivery_modes: List[Literal["DIRECT", "BCC", "JOURNAL", "API", "RETRO_SCAN"]] | Omit = omit,
        domain: str | Omit = omit,
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
        | Omit = omit,
        folder: Literal["AllItems", "Inbox"] | Omit = omit,
        integration_id: Optional[str] | Omit = omit,
        ip_restrictions: SequenceNotStr[str] | Omit = omit,
        lookback_hops: int | Omit = omit,
        regions: List[Literal["GLOBAL", "AU", "DE", "IN", "US"]] | Omit = omit,
        require_tls_inbound: bool | Omit = omit,
        require_tls_outbound: bool | Omit = omit,
        transport: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[DomainEditResponse]:
        """Updates configuration for a protected email domain.

        Only provided fields will be
        modified. Changes affect delivery mode, security settings, and regional
        processing.

        Args:
          account_id: Identifier.

          domain_id: Domain identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not domain_id:
            raise ValueError(f"Expected a non-empty value for `domain_id` but received {domain_id!r}")
        return self._patch(
            path_template(
                "/accounts/{account_id}/email-security/settings/domains/{domain_id}",
                account_id=account_id,
                domain_id=domain_id,
            ),
            body=maybe_transform(
                {
                    "allowed_delivery_modes": allowed_delivery_modes,
                    "domain": domain,
                    "drop_dispositions": drop_dispositions,
                    "folder": folder,
                    "integration_id": integration_id,
                    "ip_restrictions": ip_restrictions,
                    "lookback_hops": lookback_hops,
                    "regions": regions,
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
                post_parser=ResultWrapper[Optional[DomainEditResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[DomainEditResponse]], ResultWrapper[DomainEditResponse]),
        )

    def get(
        self,
        domain_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[DomainGetResponse]:
        """
        Retrieves detailed information for a specific protected email domain including
        its delivery configuration, SPF/DMARC status, and authorization state.

        Args:
          account_id: Identifier.

          domain_id: Domain identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not domain_id:
            raise ValueError(f"Expected a non-empty value for `domain_id` but received {domain_id!r}")
        return self._get(
            path_template(
                "/accounts/{account_id}/email-security/settings/domains/{domain_id}",
                account_id=account_id,
                domain_id=domain_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[DomainGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[DomainGetResponse]], ResultWrapper[DomainGetResponse]),
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
        active_delivery_mode: Literal["DIRECT", "BCC", "JOURNAL", "API", "RETRO_SCAN"] | Omit = omit,
        allowed_delivery_mode: Literal["DIRECT", "BCC", "JOURNAL", "API", "RETRO_SCAN"] | Omit = omit,
        direction: Literal["asc", "desc"] | Omit = omit,
        domain: SequenceNotStr[str] | Omit = omit,
        integration_id: str | Omit = omit,
        order: Literal["domain", "created_at"] | Omit = omit,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        search: str | Omit = omit,
        status: Literal["pending", "active", "failed", "timeout"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[DomainListResponse, AsyncV4PagePaginationArray[DomainListResponse]]:
        """Returns a paginated list of email domains protected by Email Security.

        Includes
        domain configuration, delivery modes, and authorization status. Supports
        filtering by delivery mode and integration ID.

        Args:
          account_id: Identifier.

          active_delivery_mode: Currently active delivery mode to filter by.

          allowed_delivery_mode: Delivery mode to filter by.

          direction: The sorting direction.

          domain: Domain names to filter by.

          integration_id: Integration ID to filter by.

          order: Field to sort by.

          page: Current page within paginated list of results.

          per_page: The number of results per page. Maximum value is 1000.

          search: Search term for filtering records. Behavior may change.

          status: Filters response to domains with the provided status.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            path_template("/accounts/{account_id}/email-security/settings/domains", account_id=account_id),
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
                        "integration_id": integration_id,
                        "order": order,
                        "page": page,
                        "per_page": per_page,
                        "search": search,
                        "status": status,
                    },
                    domain_list_params.DomainListParams,
                ),
            ),
            model=DomainListResponse,
        )

    async def delete(
        self,
        domain_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[DomainDeleteResponse]:
        """Removes email security protection from a domain.

        After deletion, emails for this
        domain will no longer be processed by Email Security. This action cannot be
        undone.

        Args:
          account_id: Identifier.

          domain_id: Domain identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not domain_id:
            raise ValueError(f"Expected a non-empty value for `domain_id` but received {domain_id!r}")
        return await self._delete(
            path_template(
                "/accounts/{account_id}/email-security/settings/domains/{domain_id}",
                account_id=account_id,
                domain_id=domain_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[DomainDeleteResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[DomainDeleteResponse]], ResultWrapper[DomainDeleteResponse]),
        )

    async def edit(
        self,
        domain_id: str,
        *,
        account_id: str,
        allowed_delivery_modes: List[Literal["DIRECT", "BCC", "JOURNAL", "API", "RETRO_SCAN"]] | Omit = omit,
        domain: str | Omit = omit,
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
        | Omit = omit,
        folder: Literal["AllItems", "Inbox"] | Omit = omit,
        integration_id: Optional[str] | Omit = omit,
        ip_restrictions: SequenceNotStr[str] | Omit = omit,
        lookback_hops: int | Omit = omit,
        regions: List[Literal["GLOBAL", "AU", "DE", "IN", "US"]] | Omit = omit,
        require_tls_inbound: bool | Omit = omit,
        require_tls_outbound: bool | Omit = omit,
        transport: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[DomainEditResponse]:
        """Updates configuration for a protected email domain.

        Only provided fields will be
        modified. Changes affect delivery mode, security settings, and regional
        processing.

        Args:
          account_id: Identifier.

          domain_id: Domain identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not domain_id:
            raise ValueError(f"Expected a non-empty value for `domain_id` but received {domain_id!r}")
        return await self._patch(
            path_template(
                "/accounts/{account_id}/email-security/settings/domains/{domain_id}",
                account_id=account_id,
                domain_id=domain_id,
            ),
            body=await async_maybe_transform(
                {
                    "allowed_delivery_modes": allowed_delivery_modes,
                    "domain": domain,
                    "drop_dispositions": drop_dispositions,
                    "folder": folder,
                    "integration_id": integration_id,
                    "ip_restrictions": ip_restrictions,
                    "lookback_hops": lookback_hops,
                    "regions": regions,
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
                post_parser=ResultWrapper[Optional[DomainEditResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[DomainEditResponse]], ResultWrapper[DomainEditResponse]),
        )

    async def get(
        self,
        domain_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[DomainGetResponse]:
        """
        Retrieves detailed information for a specific protected email domain including
        its delivery configuration, SPF/DMARC status, and authorization state.

        Args:
          account_id: Identifier.

          domain_id: Domain identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not domain_id:
            raise ValueError(f"Expected a non-empty value for `domain_id` but received {domain_id!r}")
        return await self._get(
            path_template(
                "/accounts/{account_id}/email-security/settings/domains/{domain_id}",
                account_id=account_id,
                domain_id=domain_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[DomainGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[DomainGetResponse]], ResultWrapper[DomainGetResponse]),
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
        self.edit = async_to_streamed_response_wrapper(
            domains.edit,
        )
        self.get = async_to_streamed_response_wrapper(
            domains.get,
        )
