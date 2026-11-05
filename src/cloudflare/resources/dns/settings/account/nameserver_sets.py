# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, Type, Iterable, cast

import httpx

from ....._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ....._utils import path_template, maybe_transform, async_maybe_transform
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....._wrappers import ResultWrapper
from .....pagination import SyncV4PagePaginationArray, AsyncV4PagePaginationArray
from ....._base_client import AsyncPaginator, make_request_options
from .....types.dns.settings.account import nameserver_set_list_params, nameserver_set_create_params
from .....types.dns.settings.account.nameserver_set_get_response import NameserverSetGetResponse
from .....types.dns.settings.account.nameserver_set_list_response import NameserverSetListResponse
from .....types.dns.settings.account.nameserver_set_create_response import NameserverSetCreateResponse
from .....types.dns.settings.account.nameserver_set_delete_response import NameserverSetDeleteResponse

__all__ = ["NameserverSetsResource", "AsyncNameserverSetsResource"]


class NameserverSetsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> NameserverSetsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return NameserverSetsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> NameserverSetsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return NameserverSetsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        account_id: str,
        name: str,
        nameservers: Iterable[nameserver_set_create_params.Nameserver],
        advanced: bool | Omit = omit,
        ip_set: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NameserverSetCreateResponse:
        """Creates a named Custom Nameserver Set.

        Only the customer-defined name can be
        changed later. To change nameservers or addresses, create a new set, move any
        zone assignments, and delete the old set. For details, refer to
        [Nameserver sets](https://developers.cloudflare.com/dns/nameservers/custom-nameservers/nameserver-sets/).

        Args:
          account_id: Identifier.

          name: Customer-defined name, unique within the account by exact string equality
              (case-sensitive, with no Unicode normalization). Must be valid UTF-8 and at most
              255 UTF-8 bytes, not 255 characters. Only graphical Unicode characters are
              allowed; leading or trailing whitespace is rejected. The name can be changed
              without changing the set's nameservers or addresses.

          nameservers: Lists each nameserver and the number of addresses to allocate to it. Requires a
              unique name for each entry in the set.

          advanced: Whether to allocate the nameservers from distinct Advanced anycast groups.

          ip_set: Selects the account-specific IP set that supplies the nameserver addresses.
              Nameserver sets with the same `ip_set` and `advanced` value may reuse addresses;
              otherwise, they use disjoint address groups.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return cast(
            NameserverSetCreateResponse,
            self._post(
                path_template("/accounts/{account_id}/dns_settings/nameserver_sets", account_id=account_id),
                body=maybe_transform(
                    {
                        "name": name,
                        "nameservers": nameservers,
                        "advanced": advanced,
                        "ip_set": ip_set,
                    },
                    nameserver_set_create_params.NameserverSetCreateParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper[NameserverSetCreateResponse]._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[NameserverSetCreateResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def list(
        self,
        *,
        account_id: str,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncV4PagePaginationArray[NameserverSetListResponse]:
        """Lists an account's Custom Nameserver Sets.

        For details, refer to
        [Nameserver sets](https://developers.cloudflare.com/dns/nameservers/custom-nameservers/nameserver-sets/).

        Args:
          account_id: Identifier.

          page: Page number of paginated results.

          per_page: Number of results per page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            path_template("/accounts/{account_id}/dns_settings/nameserver_sets", account_id=account_id),
            page=SyncV4PagePaginationArray[NameserverSetListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page": page,
                        "per_page": per_page,
                    },
                    nameserver_set_list_params.NameserverSetListParams,
                ),
            ),
            model=cast(
                Any, NameserverSetListResponse
            ),  # Union types cannot be passed in as arguments in the type system
        )

    def delete(
        self,
        nameserver_set_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NameserverSetDeleteResponse:
        """Deletes an unassigned Custom Nameserver Set.

        For details, refer to
        [Nameserver sets](https://developers.cloudflare.com/dns/nameservers/custom-nameservers/nameserver-sets/).

        Args:
          account_id: Identifier.

          nameserver_set_id: Identifier for a nameserver set.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not nameserver_set_id:
            raise ValueError(f"Expected a non-empty value for `nameserver_set_id` but received {nameserver_set_id!r}")
        return self._delete(
            path_template(
                "/accounts/{account_id}/dns_settings/nameserver_sets/{nameserver_set_id}",
                account_id=account_id,
                nameserver_set_id=nameserver_set_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[NameserverSetDeleteResponse]._unwrapper,
            ),
            cast_to=cast(Type[NameserverSetDeleteResponse], ResultWrapper[NameserverSetDeleteResponse]),
        )

    def get(
        self,
        nameserver_set_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NameserverSetGetResponse:
        """Gets a Custom Nameserver Set owned by an account.

        For details, refer to
        [Nameserver sets](https://developers.cloudflare.com/dns/nameservers/custom-nameservers/nameserver-sets/).

        Args:
          account_id: Identifier.

          nameserver_set_id: Identifier for a nameserver set.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not nameserver_set_id:
            raise ValueError(f"Expected a non-empty value for `nameserver_set_id` but received {nameserver_set_id!r}")
        return cast(
            NameserverSetGetResponse,
            self._get(
                path_template(
                    "/accounts/{account_id}/dns_settings/nameserver_sets/{nameserver_set_id}",
                    account_id=account_id,
                    nameserver_set_id=nameserver_set_id,
                ),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper[NameserverSetGetResponse]._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[NameserverSetGetResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class AsyncNameserverSetsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncNameserverSetsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncNameserverSetsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncNameserverSetsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncNameserverSetsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_id: str,
        name: str,
        nameservers: Iterable[nameserver_set_create_params.Nameserver],
        advanced: bool | Omit = omit,
        ip_set: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NameserverSetCreateResponse:
        """Creates a named Custom Nameserver Set.

        Only the customer-defined name can be
        changed later. To change nameservers or addresses, create a new set, move any
        zone assignments, and delete the old set. For details, refer to
        [Nameserver sets](https://developers.cloudflare.com/dns/nameservers/custom-nameservers/nameserver-sets/).

        Args:
          account_id: Identifier.

          name: Customer-defined name, unique within the account by exact string equality
              (case-sensitive, with no Unicode normalization). Must be valid UTF-8 and at most
              255 UTF-8 bytes, not 255 characters. Only graphical Unicode characters are
              allowed; leading or trailing whitespace is rejected. The name can be changed
              without changing the set's nameservers or addresses.

          nameservers: Lists each nameserver and the number of addresses to allocate to it. Requires a
              unique name for each entry in the set.

          advanced: Whether to allocate the nameservers from distinct Advanced anycast groups.

          ip_set: Selects the account-specific IP set that supplies the nameserver addresses.
              Nameserver sets with the same `ip_set` and `advanced` value may reuse addresses;
              otherwise, they use disjoint address groups.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return cast(
            NameserverSetCreateResponse,
            await self._post(
                path_template("/accounts/{account_id}/dns_settings/nameserver_sets", account_id=account_id),
                body=await async_maybe_transform(
                    {
                        "name": name,
                        "nameservers": nameservers,
                        "advanced": advanced,
                        "ip_set": ip_set,
                    },
                    nameserver_set_create_params.NameserverSetCreateParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper[NameserverSetCreateResponse]._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[NameserverSetCreateResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def list(
        self,
        *,
        account_id: str,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[NameserverSetListResponse, AsyncV4PagePaginationArray[NameserverSetListResponse]]:
        """Lists an account's Custom Nameserver Sets.

        For details, refer to
        [Nameserver sets](https://developers.cloudflare.com/dns/nameservers/custom-nameservers/nameserver-sets/).

        Args:
          account_id: Identifier.

          page: Page number of paginated results.

          per_page: Number of results per page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            path_template("/accounts/{account_id}/dns_settings/nameserver_sets", account_id=account_id),
            page=AsyncV4PagePaginationArray[NameserverSetListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page": page,
                        "per_page": per_page,
                    },
                    nameserver_set_list_params.NameserverSetListParams,
                ),
            ),
            model=cast(
                Any, NameserverSetListResponse
            ),  # Union types cannot be passed in as arguments in the type system
        )

    async def delete(
        self,
        nameserver_set_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NameserverSetDeleteResponse:
        """Deletes an unassigned Custom Nameserver Set.

        For details, refer to
        [Nameserver sets](https://developers.cloudflare.com/dns/nameservers/custom-nameservers/nameserver-sets/).

        Args:
          account_id: Identifier.

          nameserver_set_id: Identifier for a nameserver set.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not nameserver_set_id:
            raise ValueError(f"Expected a non-empty value for `nameserver_set_id` but received {nameserver_set_id!r}")
        return await self._delete(
            path_template(
                "/accounts/{account_id}/dns_settings/nameserver_sets/{nameserver_set_id}",
                account_id=account_id,
                nameserver_set_id=nameserver_set_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[NameserverSetDeleteResponse]._unwrapper,
            ),
            cast_to=cast(Type[NameserverSetDeleteResponse], ResultWrapper[NameserverSetDeleteResponse]),
        )

    async def get(
        self,
        nameserver_set_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NameserverSetGetResponse:
        """Gets a Custom Nameserver Set owned by an account.

        For details, refer to
        [Nameserver sets](https://developers.cloudflare.com/dns/nameservers/custom-nameservers/nameserver-sets/).

        Args:
          account_id: Identifier.

          nameserver_set_id: Identifier for a nameserver set.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not nameserver_set_id:
            raise ValueError(f"Expected a non-empty value for `nameserver_set_id` but received {nameserver_set_id!r}")
        return cast(
            NameserverSetGetResponse,
            await self._get(
                path_template(
                    "/accounts/{account_id}/dns_settings/nameserver_sets/{nameserver_set_id}",
                    account_id=account_id,
                    nameserver_set_id=nameserver_set_id,
                ),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper[NameserverSetGetResponse]._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[NameserverSetGetResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class NameserverSetsResourceWithRawResponse:
    def __init__(self, nameserver_sets: NameserverSetsResource) -> None:
        self._nameserver_sets = nameserver_sets

        self.create = to_raw_response_wrapper(
            nameserver_sets.create,
        )
        self.list = to_raw_response_wrapper(
            nameserver_sets.list,
        )
        self.delete = to_raw_response_wrapper(
            nameserver_sets.delete,
        )
        self.get = to_raw_response_wrapper(
            nameserver_sets.get,
        )


class AsyncNameserverSetsResourceWithRawResponse:
    def __init__(self, nameserver_sets: AsyncNameserverSetsResource) -> None:
        self._nameserver_sets = nameserver_sets

        self.create = async_to_raw_response_wrapper(
            nameserver_sets.create,
        )
        self.list = async_to_raw_response_wrapper(
            nameserver_sets.list,
        )
        self.delete = async_to_raw_response_wrapper(
            nameserver_sets.delete,
        )
        self.get = async_to_raw_response_wrapper(
            nameserver_sets.get,
        )


class NameserverSetsResourceWithStreamingResponse:
    def __init__(self, nameserver_sets: NameserverSetsResource) -> None:
        self._nameserver_sets = nameserver_sets

        self.create = to_streamed_response_wrapper(
            nameserver_sets.create,
        )
        self.list = to_streamed_response_wrapper(
            nameserver_sets.list,
        )
        self.delete = to_streamed_response_wrapper(
            nameserver_sets.delete,
        )
        self.get = to_streamed_response_wrapper(
            nameserver_sets.get,
        )


class AsyncNameserverSetsResourceWithStreamingResponse:
    def __init__(self, nameserver_sets: AsyncNameserverSetsResource) -> None:
        self._nameserver_sets = nameserver_sets

        self.create = async_to_streamed_response_wrapper(
            nameserver_sets.create,
        )
        self.list = async_to_streamed_response_wrapper(
            nameserver_sets.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            nameserver_sets.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            nameserver_sets.get,
        )
