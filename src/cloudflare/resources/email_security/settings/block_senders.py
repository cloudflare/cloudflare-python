# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Optional, cast
from typing_extensions import Literal

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
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
from ....types.email_security.settings import (
    block_sender_edit_params,
    block_sender_list_params,
    block_sender_create_params,
)
from ....types.email_security.settings.block_sender_get_response import BlockSenderGetResponse
from ....types.email_security.settings.block_sender_edit_response import BlockSenderEditResponse
from ....types.email_security.settings.block_sender_list_response import BlockSenderListResponse
from ....types.email_security.settings.block_sender_create_response import BlockSenderCreateResponse
from ....types.email_security.settings.block_sender_delete_response import BlockSenderDeleteResponse

__all__ = ["BlockSendersResource", "AsyncBlockSendersResource"]


class BlockSendersResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> BlockSendersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return BlockSendersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BlockSendersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return BlockSendersResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        account_id: str,
        is_regex: bool,
        pattern: str,
        pattern_type: Literal["EMAIL", "DOMAIN", "IP", "UNKNOWN"],
        comments: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[BlockSenderCreateResponse]:
        """Creates a new blocked sender pattern.

        Emails matching this pattern will be
        blocked from delivery. Patterns can be email addresses, domains, or IP
        addresses, and support regular expressions.

        Args:
          account_id: Identifier.

          pattern_type: Type of pattern matching. Note: UNKNOWN is deprecated and cannot be used when
              creating or updating policies, but may be returned for existing entries.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._post(
            path_template("/accounts/{account_id}/email-security/settings/block_senders", account_id=account_id),
            body=maybe_transform(
                {
                    "is_regex": is_regex,
                    "pattern": pattern,
                    "pattern_type": pattern_type,
                    "comments": comments,
                },
                block_sender_create_params.BlockSenderCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[BlockSenderCreateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[BlockSenderCreateResponse]], ResultWrapper[BlockSenderCreateResponse]),
        )

    def list(
        self,
        *,
        account_id: str,
        direction: Literal["asc", "desc"] | Omit = omit,
        order: Literal["pattern", "created_at"] | Omit = omit,
        page: int | Omit = omit,
        pattern: str | Omit = omit,
        pattern_type: Literal["EMAIL", "DOMAIN", "IP", "UNKNOWN"] | Omit = omit,
        per_page: int | Omit = omit,
        search: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncV4PagePaginationArray[BlockSenderListResponse]:
        """Returns a paginated list of blocked email sender patterns.

        These patterns
        prevent emails from matching senders from being delivered. Supports filtering by
        pattern type and searching across patterns.

        Args:
          account_id: Identifier.

          direction: The sorting direction.

          order: Field to sort by.

          page: Current page within paginated list of results.

          pattern: Filter by pattern value.

          pattern_type: Filter by pattern type.

          per_page: The number of results per page. Maximum value is 1000.

          search: Search term for filtering records. Behavior may change.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            path_template("/accounts/{account_id}/email-security/settings/block_senders", account_id=account_id),
            page=SyncV4PagePaginationArray[BlockSenderListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "direction": direction,
                        "order": order,
                        "page": page,
                        "pattern": pattern,
                        "pattern_type": pattern_type,
                        "per_page": per_page,
                        "search": search,
                    },
                    block_sender_list_params.BlockSenderListParams,
                ),
            ),
            model=BlockSenderListResponse,
        )

    def delete(
        self,
        pattern_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[BlockSenderDeleteResponse]:
        """Removes a blocked sender pattern.

        After deletion, emails from this sender will
        no longer be automatically blocked based on this rule.

        Args:
          account_id: Identifier.

          pattern_id: Blocked sender pattern identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not pattern_id:
            raise ValueError(f"Expected a non-empty value for `pattern_id` but received {pattern_id!r}")
        return self._delete(
            path_template(
                "/accounts/{account_id}/email-security/settings/block_senders/{pattern_id}",
                account_id=account_id,
                pattern_id=pattern_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[BlockSenderDeleteResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[BlockSenderDeleteResponse]], ResultWrapper[BlockSenderDeleteResponse]),
        )

    def edit(
        self,
        pattern_id: str,
        *,
        account_id: str,
        comments: Optional[str] | Omit = omit,
        is_regex: bool | Omit = omit,
        pattern: str | Omit = omit,
        pattern_type: Literal["EMAIL", "DOMAIN", "IP", "UNKNOWN"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[BlockSenderEditResponse]:
        """Updates an existing blocked sender pattern.

        Only provided fields will be
        modified. The pattern will continue blocking emails until deleted.

        Args:
          account_id: Identifier.

          pattern_id: Blocked sender pattern identifier

          pattern_type: Type of pattern matching. Note: UNKNOWN is deprecated and cannot be used when
              creating or updating policies, but may be returned for existing entries.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not pattern_id:
            raise ValueError(f"Expected a non-empty value for `pattern_id` but received {pattern_id!r}")
        return self._patch(
            path_template(
                "/accounts/{account_id}/email-security/settings/block_senders/{pattern_id}",
                account_id=account_id,
                pattern_id=pattern_id,
            ),
            body=maybe_transform(
                {
                    "comments": comments,
                    "is_regex": is_regex,
                    "pattern": pattern,
                    "pattern_type": pattern_type,
                },
                block_sender_edit_params.BlockSenderEditParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[BlockSenderEditResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[BlockSenderEditResponse]], ResultWrapper[BlockSenderEditResponse]),
        )

    def get(
        self,
        pattern_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[BlockSenderGetResponse]:
        """
        Retrieves details for a specific blocked sender pattern including its pattern
        type, value, and metadata.

        Args:
          account_id: Identifier.

          pattern_id: Blocked sender pattern identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not pattern_id:
            raise ValueError(f"Expected a non-empty value for `pattern_id` but received {pattern_id!r}")
        return self._get(
            path_template(
                "/accounts/{account_id}/email-security/settings/block_senders/{pattern_id}",
                account_id=account_id,
                pattern_id=pattern_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[BlockSenderGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[BlockSenderGetResponse]], ResultWrapper[BlockSenderGetResponse]),
        )


class AsyncBlockSendersResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncBlockSendersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncBlockSendersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBlockSendersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncBlockSendersResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_id: str,
        is_regex: bool,
        pattern: str,
        pattern_type: Literal["EMAIL", "DOMAIN", "IP", "UNKNOWN"],
        comments: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[BlockSenderCreateResponse]:
        """Creates a new blocked sender pattern.

        Emails matching this pattern will be
        blocked from delivery. Patterns can be email addresses, domains, or IP
        addresses, and support regular expressions.

        Args:
          account_id: Identifier.

          pattern_type: Type of pattern matching. Note: UNKNOWN is deprecated and cannot be used when
              creating or updating policies, but may be returned for existing entries.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._post(
            path_template("/accounts/{account_id}/email-security/settings/block_senders", account_id=account_id),
            body=await async_maybe_transform(
                {
                    "is_regex": is_regex,
                    "pattern": pattern,
                    "pattern_type": pattern_type,
                    "comments": comments,
                },
                block_sender_create_params.BlockSenderCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[BlockSenderCreateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[BlockSenderCreateResponse]], ResultWrapper[BlockSenderCreateResponse]),
        )

    def list(
        self,
        *,
        account_id: str,
        direction: Literal["asc", "desc"] | Omit = omit,
        order: Literal["pattern", "created_at"] | Omit = omit,
        page: int | Omit = omit,
        pattern: str | Omit = omit,
        pattern_type: Literal["EMAIL", "DOMAIN", "IP", "UNKNOWN"] | Omit = omit,
        per_page: int | Omit = omit,
        search: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[BlockSenderListResponse, AsyncV4PagePaginationArray[BlockSenderListResponse]]:
        """Returns a paginated list of blocked email sender patterns.

        These patterns
        prevent emails from matching senders from being delivered. Supports filtering by
        pattern type and searching across patterns.

        Args:
          account_id: Identifier.

          direction: The sorting direction.

          order: Field to sort by.

          page: Current page within paginated list of results.

          pattern: Filter by pattern value.

          pattern_type: Filter by pattern type.

          per_page: The number of results per page. Maximum value is 1000.

          search: Search term for filtering records. Behavior may change.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            path_template("/accounts/{account_id}/email-security/settings/block_senders", account_id=account_id),
            page=AsyncV4PagePaginationArray[BlockSenderListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "direction": direction,
                        "order": order,
                        "page": page,
                        "pattern": pattern,
                        "pattern_type": pattern_type,
                        "per_page": per_page,
                        "search": search,
                    },
                    block_sender_list_params.BlockSenderListParams,
                ),
            ),
            model=BlockSenderListResponse,
        )

    async def delete(
        self,
        pattern_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[BlockSenderDeleteResponse]:
        """Removes a blocked sender pattern.

        After deletion, emails from this sender will
        no longer be automatically blocked based on this rule.

        Args:
          account_id: Identifier.

          pattern_id: Blocked sender pattern identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not pattern_id:
            raise ValueError(f"Expected a non-empty value for `pattern_id` but received {pattern_id!r}")
        return await self._delete(
            path_template(
                "/accounts/{account_id}/email-security/settings/block_senders/{pattern_id}",
                account_id=account_id,
                pattern_id=pattern_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[BlockSenderDeleteResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[BlockSenderDeleteResponse]], ResultWrapper[BlockSenderDeleteResponse]),
        )

    async def edit(
        self,
        pattern_id: str,
        *,
        account_id: str,
        comments: Optional[str] | Omit = omit,
        is_regex: bool | Omit = omit,
        pattern: str | Omit = omit,
        pattern_type: Literal["EMAIL", "DOMAIN", "IP", "UNKNOWN"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[BlockSenderEditResponse]:
        """Updates an existing blocked sender pattern.

        Only provided fields will be
        modified. The pattern will continue blocking emails until deleted.

        Args:
          account_id: Identifier.

          pattern_id: Blocked sender pattern identifier

          pattern_type: Type of pattern matching. Note: UNKNOWN is deprecated and cannot be used when
              creating or updating policies, but may be returned for existing entries.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not pattern_id:
            raise ValueError(f"Expected a non-empty value for `pattern_id` but received {pattern_id!r}")
        return await self._patch(
            path_template(
                "/accounts/{account_id}/email-security/settings/block_senders/{pattern_id}",
                account_id=account_id,
                pattern_id=pattern_id,
            ),
            body=await async_maybe_transform(
                {
                    "comments": comments,
                    "is_regex": is_regex,
                    "pattern": pattern,
                    "pattern_type": pattern_type,
                },
                block_sender_edit_params.BlockSenderEditParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[BlockSenderEditResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[BlockSenderEditResponse]], ResultWrapper[BlockSenderEditResponse]),
        )

    async def get(
        self,
        pattern_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[BlockSenderGetResponse]:
        """
        Retrieves details for a specific blocked sender pattern including its pattern
        type, value, and metadata.

        Args:
          account_id: Identifier.

          pattern_id: Blocked sender pattern identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not pattern_id:
            raise ValueError(f"Expected a non-empty value for `pattern_id` but received {pattern_id!r}")
        return await self._get(
            path_template(
                "/accounts/{account_id}/email-security/settings/block_senders/{pattern_id}",
                account_id=account_id,
                pattern_id=pattern_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[BlockSenderGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[BlockSenderGetResponse]], ResultWrapper[BlockSenderGetResponse]),
        )


class BlockSendersResourceWithRawResponse:
    def __init__(self, block_senders: BlockSendersResource) -> None:
        self._block_senders = block_senders

        self.create = to_raw_response_wrapper(
            block_senders.create,
        )
        self.list = to_raw_response_wrapper(
            block_senders.list,
        )
        self.delete = to_raw_response_wrapper(
            block_senders.delete,
        )
        self.edit = to_raw_response_wrapper(
            block_senders.edit,
        )
        self.get = to_raw_response_wrapper(
            block_senders.get,
        )


class AsyncBlockSendersResourceWithRawResponse:
    def __init__(self, block_senders: AsyncBlockSendersResource) -> None:
        self._block_senders = block_senders

        self.create = async_to_raw_response_wrapper(
            block_senders.create,
        )
        self.list = async_to_raw_response_wrapper(
            block_senders.list,
        )
        self.delete = async_to_raw_response_wrapper(
            block_senders.delete,
        )
        self.edit = async_to_raw_response_wrapper(
            block_senders.edit,
        )
        self.get = async_to_raw_response_wrapper(
            block_senders.get,
        )


class BlockSendersResourceWithStreamingResponse:
    def __init__(self, block_senders: BlockSendersResource) -> None:
        self._block_senders = block_senders

        self.create = to_streamed_response_wrapper(
            block_senders.create,
        )
        self.list = to_streamed_response_wrapper(
            block_senders.list,
        )
        self.delete = to_streamed_response_wrapper(
            block_senders.delete,
        )
        self.edit = to_streamed_response_wrapper(
            block_senders.edit,
        )
        self.get = to_streamed_response_wrapper(
            block_senders.get,
        )


class AsyncBlockSendersResourceWithStreamingResponse:
    def __init__(self, block_senders: AsyncBlockSendersResource) -> None:
        self._block_senders = block_senders

        self.create = async_to_streamed_response_wrapper(
            block_senders.create,
        )
        self.list = async_to_streamed_response_wrapper(
            block_senders.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            block_senders.delete,
        )
        self.edit = async_to_streamed_response_wrapper(
            block_senders.edit,
        )
        self.get = async_to_streamed_response_wrapper(
            block_senders.get,
        )
