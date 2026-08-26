# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Union, Iterable, cast
from datetime import datetime
from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._wrappers import ResultWrapper
from ...pagination import SyncCursorPagination, AsyncCursorPagination
from ..._base_client import AsyncPaginator, make_request_options
from ...types.email_sending import (
    suppression_edit_params,
    suppression_list_params,
    suppression_create_params,
    suppression_import_params,
)
from ...types.email_sending.suppression_get_response import SuppressionGetResponse
from ...types.email_sending.suppression_edit_response import SuppressionEditResponse
from ...types.email_sending.suppression_list_response import SuppressionListResponse
from ...types.email_sending.suppression_create_response import SuppressionCreateResponse
from ...types.email_sending.suppression_delete_response import SuppressionDeleteResponse
from ...types.email_sending.suppression_import_response import SuppressionImportResponse

__all__ = ["SuppressionsResource", "AsyncSuppressionsResource"]


class SuppressionsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SuppressionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return SuppressionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SuppressionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return SuppressionsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        account_id: str,
        email: str,
        expires_at: Union[str, datetime, None] | Omit = omit,
        note: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SuppressionCreateResponse:
        """Creates an account-wide suppression.

        If a mutable legacy zone-linked row already
        exists, it is promoted without changing its identifier.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._post(
            path_template("/accounts/{account_id}/email/sending/suppressions", account_id=account_id),
            body=maybe_transform(
                {
                    "email": email,
                    "expires_at": expires_at,
                    "note": note,
                },
                suppression_create_params.SuppressionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[SuppressionCreateResponse]._unwrapper,
            ),
            cast_to=cast(Type[SuppressionCreateResponse], ResultWrapper[SuppressionCreateResponse]),
        )

    def list(
        self,
        *,
        account_id: str,
        cursor: str | Omit = omit,
        email: str | Omit = omit,
        per_page: int | Omit = omit,
        reason: Literal["manual", "complaint", "hard_bounce", "soft_bounce", "policy"] | Omit = omit,
        search: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorPagination[SuppressionListResponse]:
        """
        Lists every active Email Sending suppression owned by the account, including
        legacy rows with internal zone memberships.

        Args:
          cursor: Opaque pagination cursor returned as `result_info.next_cursor`. It carries the
              filters that produced it.

          email: Exact email-address filter.

          search: A complete address is an exact match; a value ending in `@` matches that
              username across every domain. Prefix searches may return short intermediate
              pages while the bounded account scan advances.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            path_template("/accounts/{account_id}/email/sending/suppressions", account_id=account_id),
            page=SyncCursorPagination[SuppressionListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "email": email,
                        "per_page": per_page,
                        "reason": reason,
                        "search": search,
                    },
                    suppression_list_params.SuppressionListParams,
                ),
            ),
            model=SuppressionListResponse,
        )

    def delete(
        self,
        suppression_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SuppressionDeleteResponse:
        """
        Deletes the suppression, its note, and every legacy internal zone membership,
        allowing future delivery attempts to the address.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not suppression_id:
            raise ValueError(f"Expected a non-empty value for `suppression_id` but received {suppression_id!r}")
        return self._delete(
            path_template(
                "/accounts/{account_id}/email/sending/suppressions/{suppression_id}",
                account_id=account_id,
                suppression_id=suppression_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[SuppressionDeleteResponse]._unwrapper,
            ),
            cast_to=cast(Type[SuppressionDeleteResponse], ResultWrapper[SuppressionDeleteResponse]),
        )

    def edit(
        self,
        suppression_id: str,
        *,
        account_id: str,
        expires_at: Union[str, datetime, None] | Omit = omit,
        note: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SuppressionEditResponse:
        """
        Updates expiry or advisory note fields without changing legacy internal zone
        memberships.

        Args:
          expires_at: New expiry. Send `null` to make the suppression permanent; omit to leave it
              unchanged.

          note: Replacement advisory note. Send an empty string to clear it; omit to leave it
              unchanged.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not suppression_id:
            raise ValueError(f"Expected a non-empty value for `suppression_id` but received {suppression_id!r}")
        return self._patch(
            path_template(
                "/accounts/{account_id}/email/sending/suppressions/{suppression_id}",
                account_id=account_id,
                suppression_id=suppression_id,
            ),
            body=maybe_transform(
                {
                    "expires_at": expires_at,
                    "note": note,
                },
                suppression_edit_params.SuppressionEditParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[SuppressionEditResponse]._unwrapper,
            ),
            cast_to=cast(Type[SuppressionEditResponse], ResultWrapper[SuppressionEditResponse]),
        )

    def get(
        self,
        suppression_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SuppressionGetResponse:
        """
        Gets an Email Sending suppression owned by the account.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not suppression_id:
            raise ValueError(f"Expected a non-empty value for `suppression_id` but received {suppression_id!r}")
        return self._get(
            path_template(
                "/accounts/{account_id}/email/sending/suppressions/{suppression_id}",
                account_id=account_id,
                suppression_id=suppression_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[SuppressionGetResponse]._unwrapper,
            ),
            cast_to=cast(Type[SuppressionGetResponse], ResultWrapper[SuppressionGetResponse]),
        )

    def import_(
        self,
        *,
        account_id: str,
        items: Iterable[suppression_import_params.Item],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SuppressionImportResponse:
        """
        Imports up to 1,000 account-level Email Sending suppressions in one request.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._post(
            path_template("/accounts/{account_id}/email/sending/suppressions/bulk", account_id=account_id),
            body=maybe_transform({"items": items}, suppression_import_params.SuppressionImportParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[SuppressionImportResponse]._unwrapper,
            ),
            cast_to=cast(Type[SuppressionImportResponse], ResultWrapper[SuppressionImportResponse]),
        )


class AsyncSuppressionsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSuppressionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSuppressionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSuppressionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncSuppressionsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_id: str,
        email: str,
        expires_at: Union[str, datetime, None] | Omit = omit,
        note: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SuppressionCreateResponse:
        """Creates an account-wide suppression.

        If a mutable legacy zone-linked row already
        exists, it is promoted without changing its identifier.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._post(
            path_template("/accounts/{account_id}/email/sending/suppressions", account_id=account_id),
            body=await async_maybe_transform(
                {
                    "email": email,
                    "expires_at": expires_at,
                    "note": note,
                },
                suppression_create_params.SuppressionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[SuppressionCreateResponse]._unwrapper,
            ),
            cast_to=cast(Type[SuppressionCreateResponse], ResultWrapper[SuppressionCreateResponse]),
        )

    def list(
        self,
        *,
        account_id: str,
        cursor: str | Omit = omit,
        email: str | Omit = omit,
        per_page: int | Omit = omit,
        reason: Literal["manual", "complaint", "hard_bounce", "soft_bounce", "policy"] | Omit = omit,
        search: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[SuppressionListResponse, AsyncCursorPagination[SuppressionListResponse]]:
        """
        Lists every active Email Sending suppression owned by the account, including
        legacy rows with internal zone memberships.

        Args:
          cursor: Opaque pagination cursor returned as `result_info.next_cursor`. It carries the
              filters that produced it.

          email: Exact email-address filter.

          search: A complete address is an exact match; a value ending in `@` matches that
              username across every domain. Prefix searches may return short intermediate
              pages while the bounded account scan advances.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            path_template("/accounts/{account_id}/email/sending/suppressions", account_id=account_id),
            page=AsyncCursorPagination[SuppressionListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "email": email,
                        "per_page": per_page,
                        "reason": reason,
                        "search": search,
                    },
                    suppression_list_params.SuppressionListParams,
                ),
            ),
            model=SuppressionListResponse,
        )

    async def delete(
        self,
        suppression_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SuppressionDeleteResponse:
        """
        Deletes the suppression, its note, and every legacy internal zone membership,
        allowing future delivery attempts to the address.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not suppression_id:
            raise ValueError(f"Expected a non-empty value for `suppression_id` but received {suppression_id!r}")
        return await self._delete(
            path_template(
                "/accounts/{account_id}/email/sending/suppressions/{suppression_id}",
                account_id=account_id,
                suppression_id=suppression_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[SuppressionDeleteResponse]._unwrapper,
            ),
            cast_to=cast(Type[SuppressionDeleteResponse], ResultWrapper[SuppressionDeleteResponse]),
        )

    async def edit(
        self,
        suppression_id: str,
        *,
        account_id: str,
        expires_at: Union[str, datetime, None] | Omit = omit,
        note: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SuppressionEditResponse:
        """
        Updates expiry or advisory note fields without changing legacy internal zone
        memberships.

        Args:
          expires_at: New expiry. Send `null` to make the suppression permanent; omit to leave it
              unchanged.

          note: Replacement advisory note. Send an empty string to clear it; omit to leave it
              unchanged.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not suppression_id:
            raise ValueError(f"Expected a non-empty value for `suppression_id` but received {suppression_id!r}")
        return await self._patch(
            path_template(
                "/accounts/{account_id}/email/sending/suppressions/{suppression_id}",
                account_id=account_id,
                suppression_id=suppression_id,
            ),
            body=await async_maybe_transform(
                {
                    "expires_at": expires_at,
                    "note": note,
                },
                suppression_edit_params.SuppressionEditParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[SuppressionEditResponse]._unwrapper,
            ),
            cast_to=cast(Type[SuppressionEditResponse], ResultWrapper[SuppressionEditResponse]),
        )

    async def get(
        self,
        suppression_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SuppressionGetResponse:
        """
        Gets an Email Sending suppression owned by the account.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not suppression_id:
            raise ValueError(f"Expected a non-empty value for `suppression_id` but received {suppression_id!r}")
        return await self._get(
            path_template(
                "/accounts/{account_id}/email/sending/suppressions/{suppression_id}",
                account_id=account_id,
                suppression_id=suppression_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[SuppressionGetResponse]._unwrapper,
            ),
            cast_to=cast(Type[SuppressionGetResponse], ResultWrapper[SuppressionGetResponse]),
        )

    async def import_(
        self,
        *,
        account_id: str,
        items: Iterable[suppression_import_params.Item],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SuppressionImportResponse:
        """
        Imports up to 1,000 account-level Email Sending suppressions in one request.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._post(
            path_template("/accounts/{account_id}/email/sending/suppressions/bulk", account_id=account_id),
            body=await async_maybe_transform({"items": items}, suppression_import_params.SuppressionImportParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[SuppressionImportResponse]._unwrapper,
            ),
            cast_to=cast(Type[SuppressionImportResponse], ResultWrapper[SuppressionImportResponse]),
        )


class SuppressionsResourceWithRawResponse:
    def __init__(self, suppressions: SuppressionsResource) -> None:
        self._suppressions = suppressions

        self.create = to_raw_response_wrapper(
            suppressions.create,
        )
        self.list = to_raw_response_wrapper(
            suppressions.list,
        )
        self.delete = to_raw_response_wrapper(
            suppressions.delete,
        )
        self.edit = to_raw_response_wrapper(
            suppressions.edit,
        )
        self.get = to_raw_response_wrapper(
            suppressions.get,
        )
        self.import_ = to_raw_response_wrapper(
            suppressions.import_,
        )


class AsyncSuppressionsResourceWithRawResponse:
    def __init__(self, suppressions: AsyncSuppressionsResource) -> None:
        self._suppressions = suppressions

        self.create = async_to_raw_response_wrapper(
            suppressions.create,
        )
        self.list = async_to_raw_response_wrapper(
            suppressions.list,
        )
        self.delete = async_to_raw_response_wrapper(
            suppressions.delete,
        )
        self.edit = async_to_raw_response_wrapper(
            suppressions.edit,
        )
        self.get = async_to_raw_response_wrapper(
            suppressions.get,
        )
        self.import_ = async_to_raw_response_wrapper(
            suppressions.import_,
        )


class SuppressionsResourceWithStreamingResponse:
    def __init__(self, suppressions: SuppressionsResource) -> None:
        self._suppressions = suppressions

        self.create = to_streamed_response_wrapper(
            suppressions.create,
        )
        self.list = to_streamed_response_wrapper(
            suppressions.list,
        )
        self.delete = to_streamed_response_wrapper(
            suppressions.delete,
        )
        self.edit = to_streamed_response_wrapper(
            suppressions.edit,
        )
        self.get = to_streamed_response_wrapper(
            suppressions.get,
        )
        self.import_ = to_streamed_response_wrapper(
            suppressions.import_,
        )


class AsyncSuppressionsResourceWithStreamingResponse:
    def __init__(self, suppressions: AsyncSuppressionsResource) -> None:
        self._suppressions = suppressions

        self.create = async_to_streamed_response_wrapper(
            suppressions.create,
        )
        self.list = async_to_streamed_response_wrapper(
            suppressions.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            suppressions.delete,
        )
        self.edit = async_to_streamed_response_wrapper(
            suppressions.edit,
        )
        self.get = async_to_streamed_response_wrapper(
            suppressions.get,
        )
        self.import_ = async_to_streamed_response_wrapper(
            suppressions.import_,
        )
