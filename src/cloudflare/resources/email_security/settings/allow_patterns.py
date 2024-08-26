# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._compat import cached_property

from typing_extensions import Literal

from typing import Optional, Iterable, Type

from ....types.email_security.settings.allow_pattern_create_response import AllowPatternCreateResponse

from ...._wrappers import ResultWrapper

from ...._utils import maybe_transform, async_maybe_transform

from ...._base_client import make_request_options, AsyncPaginator

from ....types.email_security.settings.allow_pattern_list_response import AllowPatternListResponse

from ....pagination import SyncV4PagePaginationArray, AsyncV4PagePaginationArray

from ....types.email_security.settings.allow_pattern_delete_response import AllowPatternDeleteResponse

from ....types.email_security.settings.allow_pattern_edit_response import AllowPatternEditResponse

from ....types.email_security.settings.allow_pattern_get_response import AllowPatternGetResponse

from ...._response import to_raw_response_wrapper, async_to_raw_response_wrapper, to_streamed_response_wrapper, async_to_streamed_response_wrapper

from ....types.email_security.settings import allow_pattern_create_params

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ...._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ...._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ...._resource import SyncAPIResource, AsyncAPIResource
from ....types import shared_params
from ....types.email_security.settings import allow_pattern_create_params
from ....types.email_security.settings import allow_pattern_list_params
from ....types.email_security.settings import allow_pattern_edit_params
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

__all__ = ["AllowPatternsResource", "AsyncAllowPatternsResource"]

class AllowPatternsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AllowPatternsResourceWithRawResponse:
        return AllowPatternsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AllowPatternsResourceWithStreamingResponse:
        return AllowPatternsResourceWithStreamingResponse(self)

    @overload
    def create(self,
    *,
    account_id: str,
    is_recipient: bool,
    is_regex: bool,
    is_sender: bool,
    is_spoof: bool,
    pattern: str,
    pattern_type: Literal["EMAIL", "DOMAIN", "IP", "UNKNOWN"],
    verify_sender: bool,
    comments: Optional[str] | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> AllowPatternCreateResponse:
        """
        Create an email allow pattern

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
    body: Iterable[allow_pattern_create_params.Variant1Body],
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> AllowPatternCreateResponse:
        """
        Create an email allow pattern

        Args:
          account_id: Account Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...
    @required_args(["account_id", "is_recipient", "is_regex", "is_sender", "is_spoof", "pattern", "pattern_type", "verify_sender"], ["account_id", "body"])
    def create(self,
    *,
    account_id: str,
    is_recipient: bool | NotGiven = NOT_GIVEN,
    is_regex: bool | NotGiven = NOT_GIVEN,
    is_sender: bool | NotGiven = NOT_GIVEN,
    is_spoof: bool | NotGiven = NOT_GIVEN,
    pattern: str | NotGiven = NOT_GIVEN,
    pattern_type: Literal["EMAIL", "DOMAIN", "IP", "UNKNOWN"] | NotGiven = NOT_GIVEN,
    verify_sender: bool | NotGiven = NOT_GIVEN,
    comments: Optional[str] | NotGiven = NOT_GIVEN,
    body: Iterable[allow_pattern_create_params.Variant1Body] | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> AllowPatternCreateResponse:
        if not account_id:
          raise ValueError(
            f'Expected a non-empty value for `account_id` but received {account_id!r}'
          )
        return cast(AllowPatternCreateResponse, self._post(
            f"/accounts/{account_id}/email-security/settings/allow_patterns",
            body=maybe_transform({
                "is_recipient": is_recipient,
                "is_regex": is_regex,
                "is_sender": is_sender,
                "is_spoof": is_spoof,
                "pattern": pattern,
                "pattern_type": pattern_type,
                "verify_sender": verify_sender,
                "comments": comments,
                "body": body,
            }, allow_pattern_create_params.AllowPatternCreateParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[AllowPatternCreateResponse]._unwrapper),
            cast_to=cast(Any, ResultWrapper[AllowPatternCreateResponse]),  # Union types cannot be passed in as arguments in the type system
        ))

    def list(self,
    *,
    account_id: str,
    direction: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
    is_recipient: bool | NotGiven = NOT_GIVEN,
    is_sender: bool | NotGiven = NOT_GIVEN,
    is_spoof: bool | NotGiven = NOT_GIVEN,
    order: Literal["pattern", "created_at"] | NotGiven = NOT_GIVEN,
    page: int | NotGiven = NOT_GIVEN,
    pattern_type: Literal["EMAIL", "DOMAIN", "IP", "UNKNOWN"] | NotGiven = NOT_GIVEN,
    per_page: int | NotGiven = NOT_GIVEN,
    search: str | NotGiven = NOT_GIVEN,
    verify_sender: bool | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> SyncV4PagePaginationArray[AllowPatternListResponse]:
        """
        List, search, and sort an accounts's email allow patterns.

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
            f"/accounts/{account_id}/email-security/settings/allow_patterns",
            page = SyncV4PagePaginationArray[AllowPatternListResponse],
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, query=maybe_transform({
                "direction": direction,
                "is_recipient": is_recipient,
                "is_sender": is_sender,
                "is_spoof": is_spoof,
                "order": order,
                "page": page,
                "pattern_type": pattern_type,
                "per_page": per_page,
                "search": search,
                "verify_sender": verify_sender,
            }, allow_pattern_list_params.AllowPatternListParams)),
            model=AllowPatternListResponse,
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
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> AllowPatternDeleteResponse:
        """
        Delete an email allow pattern

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
            f"/accounts/{account_id}/email-security/settings/allow_patterns/{pattern_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[AllowPatternDeleteResponse]._unwrapper),
            cast_to=cast(Type[AllowPatternDeleteResponse], ResultWrapper[AllowPatternDeleteResponse]),
        )

    def edit(self,
    pattern_id: int,
    *,
    account_id: str,
    comments: Optional[str] | NotGiven = NOT_GIVEN,
    is_recipient: Optional[bool] | NotGiven = NOT_GIVEN,
    is_regex: Optional[bool] | NotGiven = NOT_GIVEN,
    is_sender: Optional[bool] | NotGiven = NOT_GIVEN,
    is_spoof: Optional[bool] | NotGiven = NOT_GIVEN,
    pattern: Optional[str] | NotGiven = NOT_GIVEN,
    pattern_type: Optional[Literal["EMAIL", "DOMAIN", "IP", "UNKNOWN"]] | NotGiven = NOT_GIVEN,
    verify_sender: Optional[bool] | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> AllowPatternEditResponse:
        """
        Update an email allow pattern

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
            f"/accounts/{account_id}/email-security/settings/allow_patterns/{pattern_id}",
            body=maybe_transform({
                "comments": comments,
                "is_recipient": is_recipient,
                "is_regex": is_regex,
                "is_sender": is_sender,
                "is_spoof": is_spoof,
                "pattern": pattern,
                "pattern_type": pattern_type,
                "verify_sender": verify_sender,
            }, allow_pattern_edit_params.AllowPatternEditParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[AllowPatternEditResponse]._unwrapper),
            cast_to=cast(Type[AllowPatternEditResponse], ResultWrapper[AllowPatternEditResponse]),
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
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> AllowPatternGetResponse:
        """
        Get an email allow pattern

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
            f"/accounts/{account_id}/email-security/settings/allow_patterns/{pattern_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[AllowPatternGetResponse]._unwrapper),
            cast_to=cast(Type[AllowPatternGetResponse], ResultWrapper[AllowPatternGetResponse]),
        )

class AsyncAllowPatternsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAllowPatternsResourceWithRawResponse:
        return AsyncAllowPatternsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAllowPatternsResourceWithStreamingResponse:
        return AsyncAllowPatternsResourceWithStreamingResponse(self)

    @overload
    async def create(self,
    *,
    account_id: str,
    is_recipient: bool,
    is_regex: bool,
    is_sender: bool,
    is_spoof: bool,
    pattern: str,
    pattern_type: Literal["EMAIL", "DOMAIN", "IP", "UNKNOWN"],
    verify_sender: bool,
    comments: Optional[str] | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> AllowPatternCreateResponse:
        """
        Create an email allow pattern

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
    body: Iterable[allow_pattern_create_params.Variant1Body],
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> AllowPatternCreateResponse:
        """
        Create an email allow pattern

        Args:
          account_id: Account Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...
    @required_args(["account_id", "is_recipient", "is_regex", "is_sender", "is_spoof", "pattern", "pattern_type", "verify_sender"], ["account_id", "body"])
    async def create(self,
    *,
    account_id: str,
    is_recipient: bool | NotGiven = NOT_GIVEN,
    is_regex: bool | NotGiven = NOT_GIVEN,
    is_sender: bool | NotGiven = NOT_GIVEN,
    is_spoof: bool | NotGiven = NOT_GIVEN,
    pattern: str | NotGiven = NOT_GIVEN,
    pattern_type: Literal["EMAIL", "DOMAIN", "IP", "UNKNOWN"] | NotGiven = NOT_GIVEN,
    verify_sender: bool | NotGiven = NOT_GIVEN,
    comments: Optional[str] | NotGiven = NOT_GIVEN,
    body: Iterable[allow_pattern_create_params.Variant1Body] | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> AllowPatternCreateResponse:
        if not account_id:
          raise ValueError(
            f'Expected a non-empty value for `account_id` but received {account_id!r}'
          )
        return cast(AllowPatternCreateResponse, await self._post(
            f"/accounts/{account_id}/email-security/settings/allow_patterns",
            body=await async_maybe_transform({
                "is_recipient": is_recipient,
                "is_regex": is_regex,
                "is_sender": is_sender,
                "is_spoof": is_spoof,
                "pattern": pattern,
                "pattern_type": pattern_type,
                "verify_sender": verify_sender,
                "comments": comments,
                "body": body,
            }, allow_pattern_create_params.AllowPatternCreateParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[AllowPatternCreateResponse]._unwrapper),
            cast_to=cast(Any, ResultWrapper[AllowPatternCreateResponse]),  # Union types cannot be passed in as arguments in the type system
        ))

    def list(self,
    *,
    account_id: str,
    direction: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
    is_recipient: bool | NotGiven = NOT_GIVEN,
    is_sender: bool | NotGiven = NOT_GIVEN,
    is_spoof: bool | NotGiven = NOT_GIVEN,
    order: Literal["pattern", "created_at"] | NotGiven = NOT_GIVEN,
    page: int | NotGiven = NOT_GIVEN,
    pattern_type: Literal["EMAIL", "DOMAIN", "IP", "UNKNOWN"] | NotGiven = NOT_GIVEN,
    per_page: int | NotGiven = NOT_GIVEN,
    search: str | NotGiven = NOT_GIVEN,
    verify_sender: bool | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> AsyncPaginator[AllowPatternListResponse, AsyncV4PagePaginationArray[AllowPatternListResponse]]:
        """
        List, search, and sort an accounts's email allow patterns.

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
            f"/accounts/{account_id}/email-security/settings/allow_patterns",
            page = AsyncV4PagePaginationArray[AllowPatternListResponse],
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, query=maybe_transform({
                "direction": direction,
                "is_recipient": is_recipient,
                "is_sender": is_sender,
                "is_spoof": is_spoof,
                "order": order,
                "page": page,
                "pattern_type": pattern_type,
                "per_page": per_page,
                "search": search,
                "verify_sender": verify_sender,
            }, allow_pattern_list_params.AllowPatternListParams)),
            model=AllowPatternListResponse,
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
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> AllowPatternDeleteResponse:
        """
        Delete an email allow pattern

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
            f"/accounts/{account_id}/email-security/settings/allow_patterns/{pattern_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[AllowPatternDeleteResponse]._unwrapper),
            cast_to=cast(Type[AllowPatternDeleteResponse], ResultWrapper[AllowPatternDeleteResponse]),
        )

    async def edit(self,
    pattern_id: int,
    *,
    account_id: str,
    comments: Optional[str] | NotGiven = NOT_GIVEN,
    is_recipient: Optional[bool] | NotGiven = NOT_GIVEN,
    is_regex: Optional[bool] | NotGiven = NOT_GIVEN,
    is_sender: Optional[bool] | NotGiven = NOT_GIVEN,
    is_spoof: Optional[bool] | NotGiven = NOT_GIVEN,
    pattern: Optional[str] | NotGiven = NOT_GIVEN,
    pattern_type: Optional[Literal["EMAIL", "DOMAIN", "IP", "UNKNOWN"]] | NotGiven = NOT_GIVEN,
    verify_sender: Optional[bool] | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> AllowPatternEditResponse:
        """
        Update an email allow pattern

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
            f"/accounts/{account_id}/email-security/settings/allow_patterns/{pattern_id}",
            body=await async_maybe_transform({
                "comments": comments,
                "is_recipient": is_recipient,
                "is_regex": is_regex,
                "is_sender": is_sender,
                "is_spoof": is_spoof,
                "pattern": pattern,
                "pattern_type": pattern_type,
                "verify_sender": verify_sender,
            }, allow_pattern_edit_params.AllowPatternEditParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[AllowPatternEditResponse]._unwrapper),
            cast_to=cast(Type[AllowPatternEditResponse], ResultWrapper[AllowPatternEditResponse]),
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
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> AllowPatternGetResponse:
        """
        Get an email allow pattern

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
            f"/accounts/{account_id}/email-security/settings/allow_patterns/{pattern_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[AllowPatternGetResponse]._unwrapper),
            cast_to=cast(Type[AllowPatternGetResponse], ResultWrapper[AllowPatternGetResponse]),
        )

class AllowPatternsResourceWithRawResponse:
    def __init__(self, allow_patterns: AllowPatternsResource) -> None:
        self._allow_patterns = allow_patterns

        self.create = to_raw_response_wrapper(
            allow_patterns.create,
        )
        self.list = to_raw_response_wrapper(
            allow_patterns.list,
        )
        self.delete = to_raw_response_wrapper(
            allow_patterns.delete,
        )
        self.edit = to_raw_response_wrapper(
            allow_patterns.edit,
        )
        self.get = to_raw_response_wrapper(
            allow_patterns.get,
        )

class AsyncAllowPatternsResourceWithRawResponse:
    def __init__(self, allow_patterns: AsyncAllowPatternsResource) -> None:
        self._allow_patterns = allow_patterns

        self.create = async_to_raw_response_wrapper(
            allow_patterns.create,
        )
        self.list = async_to_raw_response_wrapper(
            allow_patterns.list,
        )
        self.delete = async_to_raw_response_wrapper(
            allow_patterns.delete,
        )
        self.edit = async_to_raw_response_wrapper(
            allow_patterns.edit,
        )
        self.get = async_to_raw_response_wrapper(
            allow_patterns.get,
        )

class AllowPatternsResourceWithStreamingResponse:
    def __init__(self, allow_patterns: AllowPatternsResource) -> None:
        self._allow_patterns = allow_patterns

        self.create = to_streamed_response_wrapper(
            allow_patterns.create,
        )
        self.list = to_streamed_response_wrapper(
            allow_patterns.list,
        )
        self.delete = to_streamed_response_wrapper(
            allow_patterns.delete,
        )
        self.edit = to_streamed_response_wrapper(
            allow_patterns.edit,
        )
        self.get = to_streamed_response_wrapper(
            allow_patterns.get,
        )

class AsyncAllowPatternsResourceWithStreamingResponse:
    def __init__(self, allow_patterns: AsyncAllowPatternsResource) -> None:
        self._allow_patterns = allow_patterns

        self.create = async_to_streamed_response_wrapper(
            allow_patterns.create,
        )
        self.list = async_to_streamed_response_wrapper(
            allow_patterns.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            allow_patterns.delete,
        )
        self.edit = async_to_streamed_response_wrapper(
            allow_patterns.edit,
        )
        self.get = async_to_streamed_response_wrapper(
            allow_patterns.get,
        )