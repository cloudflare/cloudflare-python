# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, Iterable, Optional, cast
from typing_extensions import Literal, overload

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import (
    required_args,
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
from ....types.email_security.settings import trusted_domain_list_params, trusted_domain_create_params
from ....types.email_security.settings.trusted_domain_list_response import TrustedDomainListResponse
from ....types.email_security.settings.trusted_domain_create_response import TrustedDomainCreateResponse

__all__ = ["TrustedDomainsResource", "AsyncTrustedDomainsResource"]


class TrustedDomainsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TrustedDomainsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return TrustedDomainsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TrustedDomainsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return TrustedDomainsResourceWithStreamingResponse(self)

    @overload
    def create(
        self,
        *,
        account_id: str,
        is_recent: bool,
        is_regex: bool,
        is_similarity: bool,
        pattern: str,
        comments: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TrustedDomainCreateResponse:
        """
        Create a trusted email domain

        Args:
          account_id: Account Identifier

          is_recent: Select to prevent recently registered domains from triggering a Suspicious or
              Malicious disposition.

          is_similarity: Select for partner or other approved domains that have similar spelling to your
              connected domains. Prevents listed domains from triggering a Spoof disposition.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        *,
        account_id: str,
        body: Iterable[trusted_domain_create_params.Variant1Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TrustedDomainCreateResponse:
        """
        Create a trusted email domain

        Args:
          account_id: Account Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["account_id", "is_recent", "is_regex", "is_similarity", "pattern"], ["account_id", "body"])
    def create(
        self,
        *,
        account_id: str,
        is_recent: bool | NotGiven = NOT_GIVEN,
        is_regex: bool | NotGiven = NOT_GIVEN,
        is_similarity: bool | NotGiven = NOT_GIVEN,
        pattern: str | NotGiven = NOT_GIVEN,
        comments: Optional[str] | NotGiven = NOT_GIVEN,
        body: Iterable[trusted_domain_create_params.Variant1Body] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TrustedDomainCreateResponse:
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return cast(
            TrustedDomainCreateResponse,
            self._post(
                f"/accounts/{account_id}/email-security/settings/trusted_domains",
                body=maybe_transform(
                    {
                        "is_recent": is_recent,
                        "is_regex": is_regex,
                        "is_similarity": is_similarity,
                        "pattern": pattern,
                        "comments": comments,
                        "body": body,
                    },
                    trusted_domain_create_params.TrustedDomainCreateParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper[TrustedDomainCreateResponse]._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[TrustedDomainCreateResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def list(
        self,
        *,
        account_id: str,
        direction: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
        is_recent: bool | NotGiven = NOT_GIVEN,
        is_similarity: bool | NotGiven = NOT_GIVEN,
        order: Literal["pattern", "created_at"] | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        search: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncV4PagePaginationArray[TrustedDomainListResponse]:
        """
        Lists, searches, and sorts an account’s trusted email domains.

        Args:
          account_id: Account Identifier

          direction: The sorting direction.

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
            f"/accounts/{account_id}/email-security/settings/trusted_domains",
            page=SyncV4PagePaginationArray[TrustedDomainListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "direction": direction,
                        "is_recent": is_recent,
                        "is_similarity": is_similarity,
                        "order": order,
                        "page": page,
                        "per_page": per_page,
                        "search": search,
                    },
                    trusted_domain_list_params.TrustedDomainListParams,
                ),
            ),
            model=TrustedDomainListResponse,
        )


class AsyncTrustedDomainsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTrustedDomainsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTrustedDomainsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTrustedDomainsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncTrustedDomainsResourceWithStreamingResponse(self)

    @overload
    async def create(
        self,
        *,
        account_id: str,
        is_recent: bool,
        is_regex: bool,
        is_similarity: bool,
        pattern: str,
        comments: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TrustedDomainCreateResponse:
        """
        Create a trusted email domain

        Args:
          account_id: Account Identifier

          is_recent: Select to prevent recently registered domains from triggering a Suspicious or
              Malicious disposition.

          is_similarity: Select for partner or other approved domains that have similar spelling to your
              connected domains. Prevents listed domains from triggering a Spoof disposition.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        *,
        account_id: str,
        body: Iterable[trusted_domain_create_params.Variant1Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TrustedDomainCreateResponse:
        """
        Create a trusted email domain

        Args:
          account_id: Account Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["account_id", "is_recent", "is_regex", "is_similarity", "pattern"], ["account_id", "body"])
    async def create(
        self,
        *,
        account_id: str,
        is_recent: bool | NotGiven = NOT_GIVEN,
        is_regex: bool | NotGiven = NOT_GIVEN,
        is_similarity: bool | NotGiven = NOT_GIVEN,
        pattern: str | NotGiven = NOT_GIVEN,
        comments: Optional[str] | NotGiven = NOT_GIVEN,
        body: Iterable[trusted_domain_create_params.Variant1Body] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TrustedDomainCreateResponse:
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return cast(
            TrustedDomainCreateResponse,
            await self._post(
                f"/accounts/{account_id}/email-security/settings/trusted_domains",
                body=await async_maybe_transform(
                    {
                        "is_recent": is_recent,
                        "is_regex": is_regex,
                        "is_similarity": is_similarity,
                        "pattern": pattern,
                        "comments": comments,
                        "body": body,
                    },
                    trusted_domain_create_params.TrustedDomainCreateParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper[TrustedDomainCreateResponse]._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[TrustedDomainCreateResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def list(
        self,
        *,
        account_id: str,
        direction: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
        is_recent: bool | NotGiven = NOT_GIVEN,
        is_similarity: bool | NotGiven = NOT_GIVEN,
        order: Literal["pattern", "created_at"] | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        search: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[TrustedDomainListResponse, AsyncV4PagePaginationArray[TrustedDomainListResponse]]:
        """
        Lists, searches, and sorts an account’s trusted email domains.

        Args:
          account_id: Account Identifier

          direction: The sorting direction.

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
            f"/accounts/{account_id}/email-security/settings/trusted_domains",
            page=AsyncV4PagePaginationArray[TrustedDomainListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "direction": direction,
                        "is_recent": is_recent,
                        "is_similarity": is_similarity,
                        "order": order,
                        "page": page,
                        "per_page": per_page,
                        "search": search,
                    },
                    trusted_domain_list_params.TrustedDomainListParams,
                ),
            ),
            model=TrustedDomainListResponse,
        )


class TrustedDomainsResourceWithRawResponse:
    def __init__(self, trusted_domains: TrustedDomainsResource) -> None:
        self._trusted_domains = trusted_domains

        self.create = to_raw_response_wrapper(
            trusted_domains.create,
        )
        self.list = to_raw_response_wrapper(
            trusted_domains.list,
        )


class AsyncTrustedDomainsResourceWithRawResponse:
    def __init__(self, trusted_domains: AsyncTrustedDomainsResource) -> None:
        self._trusted_domains = trusted_domains

        self.create = async_to_raw_response_wrapper(
            trusted_domains.create,
        )
        self.list = async_to_raw_response_wrapper(
            trusted_domains.list,
        )


class TrustedDomainsResourceWithStreamingResponse:
    def __init__(self, trusted_domains: TrustedDomainsResource) -> None:
        self._trusted_domains = trusted_domains

        self.create = to_streamed_response_wrapper(
            trusted_domains.create,
        )
        self.list = to_streamed_response_wrapper(
            trusted_domains.list,
        )


class AsyncTrustedDomainsResourceWithStreamingResponse:
    def __init__(self, trusted_domains: AsyncTrustedDomainsResource) -> None:
        self._trusted_domains = trusted_domains

        self.create = async_to_streamed_response_wrapper(
            trusted_domains.create,
        )
        self.list = async_to_streamed_response_wrapper(
            trusted_domains.list,
        )
