# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._compat import cached_property

from typing import Optional, Iterable, Type

from ....types.email_security.settings.trusted_domain_create_response import TrustedDomainCreateResponse

from ...._wrappers import ResultWrapper

from ...._utils import maybe_transform, async_maybe_transform

from ...._base_client import make_request_options, AsyncPaginator

from ....types.email_security.settings.trusted_domain_list_response import TrustedDomainListResponse

from ....pagination import SyncV4PagePaginationArray, AsyncV4PagePaginationArray

from typing_extensions import Literal

from ....types.email_security.settings.trusted_domain_delete_response import TrustedDomainDeleteResponse

from ....types.email_security.settings.trusted_domain_edit_response import TrustedDomainEditResponse

from ....types.email_security.settings.trusted_domain_get_response import TrustedDomainGetResponse

from ...._response import to_raw_response_wrapper, async_to_raw_response_wrapper, to_streamed_response_wrapper, async_to_streamed_response_wrapper

from ....types.email_security.settings import trusted_domain_create_params

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ...._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ...._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ...._resource import SyncAPIResource, AsyncAPIResource
from ....types import shared_params
from ....types.email_security.settings import trusted_domain_create_params
from ....types.email_security.settings import trusted_domain_list_params
from ....types.email_security.settings import trusted_domain_edit_params
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast

__all__ = ["TrustedDomainsResource", "AsyncTrustedDomainsResource"]

class TrustedDomainsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TrustedDomainsResourceWithRawResponse:
        return TrustedDomainsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TrustedDomainsResourceWithStreamingResponse:
        return TrustedDomainsResourceWithStreamingResponse(self)

    @overload
    def create(self,
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
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> TrustedDomainCreateResponse:
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
    @overload
    def create(self,
    *,
    account_id: str,
    body: Iterable[trusted_domain_create_params.Variant1Body],
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> TrustedDomainCreateResponse:
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
    def create(self,
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
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> TrustedDomainCreateResponse:
        if not account_id:
          raise ValueError(
            f'Expected a non-empty value for `account_id` but received {account_id!r}'
          )
        return cast(TrustedDomainCreateResponse, self._post(
            f"/accounts/{account_id}/email-security/settings/trusted_domains",
            body=maybe_transform({
                "is_recent": is_recent,
                "is_regex": is_regex,
                "is_similarity": is_similarity,
                "pattern": pattern,
                "comments": comments,
                "body": body,
            }, trusted_domain_create_params.TrustedDomainCreateParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[TrustedDomainCreateResponse]._unwrapper),
            cast_to=cast(Any, ResultWrapper[TrustedDomainCreateResponse]),  # Union types cannot be passed in as arguments in the type system
        ))

    def list(self,
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
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> SyncV4PagePaginationArray[TrustedDomainListResponse]:
        """
        List, search, and sort an account's trusted email domains.

        Args:
          account_id: Account Identifier

          direction: The sorting direction.

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
          raise ValueError(
            f'Expected a non-empty value for `account_id` but received {account_id!r}'
          )
        return self._get_api_list(
            f"/accounts/{account_id}/email-security/settings/trusted_domains",
            page = SyncV4PagePaginationArray[TrustedDomainListResponse],
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, query=maybe_transform({
                "direction": direction,
                "is_recent": is_recent,
                "is_similarity": is_similarity,
                "order": order,
                "page": page,
                "per_page": per_page,
                "search": search,
            }, trusted_domain_list_params.TrustedDomainListParams)),
            model=TrustedDomainListResponse,
        )

    def delete(self,
    pattern_id: int,
    *,
    account_id: str,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> TrustedDomainDeleteResponse:
        """
        Delete a trusted email domain

        Args:
          account_id: Account Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
          raise ValueError(
            f'Expected a non-empty value for `account_id` but received {account_id!r}'
          )
        return self._delete(
            f"/accounts/{account_id}/email-security/settings/trusted_domains/{pattern_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[TrustedDomainDeleteResponse]._unwrapper),
            cast_to=cast(Type[TrustedDomainDeleteResponse], ResultWrapper[TrustedDomainDeleteResponse]),
        )

    def edit(self,
    pattern_id: int,
    *,
    account_id: str,
    comments: Optional[str] | NotGiven = NOT_GIVEN,
    is_recent: Optional[bool] | NotGiven = NOT_GIVEN,
    is_regex: Optional[bool] | NotGiven = NOT_GIVEN,
    is_similarity: Optional[bool] | NotGiven = NOT_GIVEN,
    pattern: Optional[str] | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> TrustedDomainEditResponse:
        """
        Update a trusted email domain

        Args:
          account_id: Account Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
          raise ValueError(
            f'Expected a non-empty value for `account_id` but received {account_id!r}'
          )
        return self._patch(
            f"/accounts/{account_id}/email-security/settings/trusted_domains/{pattern_id}",
            body=maybe_transform({
                "comments": comments,
                "is_recent": is_recent,
                "is_regex": is_regex,
                "is_similarity": is_similarity,
                "pattern": pattern,
            }, trusted_domain_edit_params.TrustedDomainEditParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[TrustedDomainEditResponse]._unwrapper),
            cast_to=cast(Type[TrustedDomainEditResponse], ResultWrapper[TrustedDomainEditResponse]),
        )

    def get(self,
    pattern_id: int,
    *,
    account_id: str,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> TrustedDomainGetResponse:
        """
        Get a trusted email domain

        Args:
          account_id: Account Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
          raise ValueError(
            f'Expected a non-empty value for `account_id` but received {account_id!r}'
          )
        return self._get(
            f"/accounts/{account_id}/email-security/settings/trusted_domains/{pattern_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[TrustedDomainGetResponse]._unwrapper),
            cast_to=cast(Type[TrustedDomainGetResponse], ResultWrapper[TrustedDomainGetResponse]),
        )

class AsyncTrustedDomainsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTrustedDomainsResourceWithRawResponse:
        return AsyncTrustedDomainsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTrustedDomainsResourceWithStreamingResponse:
        return AsyncTrustedDomainsResourceWithStreamingResponse(self)

    @overload
    async def create(self,
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
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> TrustedDomainCreateResponse:
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
    @overload
    async def create(self,
    *,
    account_id: str,
    body: Iterable[trusted_domain_create_params.Variant1Body],
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> TrustedDomainCreateResponse:
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
    async def create(self,
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
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> TrustedDomainCreateResponse:
        if not account_id:
          raise ValueError(
            f'Expected a non-empty value for `account_id` but received {account_id!r}'
          )
        return cast(TrustedDomainCreateResponse, await self._post(
            f"/accounts/{account_id}/email-security/settings/trusted_domains",
            body=await async_maybe_transform({
                "is_recent": is_recent,
                "is_regex": is_regex,
                "is_similarity": is_similarity,
                "pattern": pattern,
                "comments": comments,
                "body": body,
            }, trusted_domain_create_params.TrustedDomainCreateParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[TrustedDomainCreateResponse]._unwrapper),
            cast_to=cast(Any, ResultWrapper[TrustedDomainCreateResponse]),  # Union types cannot be passed in as arguments in the type system
        ))

    def list(self,
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
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> AsyncPaginator[TrustedDomainListResponse, AsyncV4PagePaginationArray[TrustedDomainListResponse]]:
        """
        List, search, and sort an account's trusted email domains.

        Args:
          account_id: Account Identifier

          direction: The sorting direction.

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
          raise ValueError(
            f'Expected a non-empty value for `account_id` but received {account_id!r}'
          )
        return self._get_api_list(
            f"/accounts/{account_id}/email-security/settings/trusted_domains",
            page = AsyncV4PagePaginationArray[TrustedDomainListResponse],
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, query=maybe_transform({
                "direction": direction,
                "is_recent": is_recent,
                "is_similarity": is_similarity,
                "order": order,
                "page": page,
                "per_page": per_page,
                "search": search,
            }, trusted_domain_list_params.TrustedDomainListParams)),
            model=TrustedDomainListResponse,
        )

    async def delete(self,
    pattern_id: int,
    *,
    account_id: str,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> TrustedDomainDeleteResponse:
        """
        Delete a trusted email domain

        Args:
          account_id: Account Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
          raise ValueError(
            f'Expected a non-empty value for `account_id` but received {account_id!r}'
          )
        return await self._delete(
            f"/accounts/{account_id}/email-security/settings/trusted_domains/{pattern_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[TrustedDomainDeleteResponse]._unwrapper),
            cast_to=cast(Type[TrustedDomainDeleteResponse], ResultWrapper[TrustedDomainDeleteResponse]),
        )

    async def edit(self,
    pattern_id: int,
    *,
    account_id: str,
    comments: Optional[str] | NotGiven = NOT_GIVEN,
    is_recent: Optional[bool] | NotGiven = NOT_GIVEN,
    is_regex: Optional[bool] | NotGiven = NOT_GIVEN,
    is_similarity: Optional[bool] | NotGiven = NOT_GIVEN,
    pattern: Optional[str] | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> TrustedDomainEditResponse:
        """
        Update a trusted email domain

        Args:
          account_id: Account Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
          raise ValueError(
            f'Expected a non-empty value for `account_id` but received {account_id!r}'
          )
        return await self._patch(
            f"/accounts/{account_id}/email-security/settings/trusted_domains/{pattern_id}",
            body=await async_maybe_transform({
                "comments": comments,
                "is_recent": is_recent,
                "is_regex": is_regex,
                "is_similarity": is_similarity,
                "pattern": pattern,
            }, trusted_domain_edit_params.TrustedDomainEditParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[TrustedDomainEditResponse]._unwrapper),
            cast_to=cast(Type[TrustedDomainEditResponse], ResultWrapper[TrustedDomainEditResponse]),
        )

    async def get(self,
    pattern_id: int,
    *,
    account_id: str,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> TrustedDomainGetResponse:
        """
        Get a trusted email domain

        Args:
          account_id: Account Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
          raise ValueError(
            f'Expected a non-empty value for `account_id` but received {account_id!r}'
          )
        return await self._get(
            f"/accounts/{account_id}/email-security/settings/trusted_domains/{pattern_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[TrustedDomainGetResponse]._unwrapper),
            cast_to=cast(Type[TrustedDomainGetResponse], ResultWrapper[TrustedDomainGetResponse]),
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
        self.delete = to_raw_response_wrapper(
            trusted_domains.delete,
        )
        self.edit = to_raw_response_wrapper(
            trusted_domains.edit,
        )
        self.get = to_raw_response_wrapper(
            trusted_domains.get,
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
        self.delete = async_to_raw_response_wrapper(
            trusted_domains.delete,
        )
        self.edit = async_to_raw_response_wrapper(
            trusted_domains.edit,
        )
        self.get = async_to_raw_response_wrapper(
            trusted_domains.get,
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
        self.delete = to_streamed_response_wrapper(
            trusted_domains.delete,
        )
        self.edit = to_streamed_response_wrapper(
            trusted_domains.edit,
        )
        self.get = to_streamed_response_wrapper(
            trusted_domains.get,
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
        self.delete = async_to_streamed_response_wrapper(
            trusted_domains.delete,
        )
        self.edit = async_to_streamed_response_wrapper(
            trusted_domains.edit,
        )
        self.get = async_to_streamed_response_wrapper(
            trusted_domains.get,
        )