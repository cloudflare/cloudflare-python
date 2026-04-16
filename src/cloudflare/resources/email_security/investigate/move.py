# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, cast
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
from ....pagination import SyncSinglePage, AsyncSinglePage
from ...._base_client import AsyncPaginator, make_request_options
from ....types.email_security.investigate import move_bulk_params, move_create_params
from ....types.email_security.investigate.move_bulk_response import MoveBulkResponse
from ....types.email_security.investigate.move_create_response import MoveCreateResponse

__all__ = ["MoveResource", "AsyncMoveResource"]


class MoveResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> MoveResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return MoveResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MoveResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return MoveResourceWithStreamingResponse(self)

    def create(
        self,
        postfix_id: str,
        *,
        account_id: str | None = None,
        destination: Literal[
            "Inbox", "JunkEmail", "DeletedItems", "RecoverableItemsDeletions", "RecoverableItemsPurges"
        ],
        submission: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MoveCreateResponse:
        """
        Moves a single email message to a different folder or changes its quarantine
        status.

        Args:
          account_id: Account Identifier

          postfix_id: The identifier of the message.

          submission: When true, search the submissions datastore only. When false or omitted, search
              the regular datastore only.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if account_id is None:
            account_id = self._client._get_account_id_path_param()
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not postfix_id:
            raise ValueError(f"Expected a non-empty value for `postfix_id` but received {postfix_id!r}")
        return self._post(
            path_template(
                "/accounts/{account_id}/email-security/investigate/{postfix_id}/move",
                account_id=account_id,
                postfix_id=postfix_id,
            ),
            body=maybe_transform({"destination": destination}, move_create_params.MoveCreateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"submission": submission}, move_create_params.MoveCreateParams),
                post_parser=ResultWrapper[MoveCreateResponse]._unwrapper,
            ),
            cast_to=cast(Type[MoveCreateResponse], ResultWrapper[MoveCreateResponse]),
        )

    def bulk(
        self,
        *,
        account_id: str | None = None,
        destination: Literal[
            "Inbox", "JunkEmail", "DeletedItems", "RecoverableItemsDeletions", "RecoverableItemsPurges"
        ],
        ids: SequenceNotStr[str] | Omit = omit,
        postfix_ids: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncSinglePage[MoveBulkResponse]:
        """
        Maximum batch size: 1000 messages per request

        Args:
          account_id: Account Identifier

          ids: List of message IDs to move.

          postfix_ids: Deprecated: Use `ids` instead. List of message IDs to move.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if account_id is None:
            account_id = self._client._get_account_id_path_param()
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            path_template("/accounts/{account_id}/email-security/investigate/move", account_id=account_id),
            page=SyncSinglePage[MoveBulkResponse],
            body=maybe_transform(
                {
                    "destination": destination,
                    "ids": ids,
                    "postfix_ids": postfix_ids,
                },
                move_bulk_params.MoveBulkParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=MoveBulkResponse,
            method="post",
        )


class AsyncMoveResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncMoveResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMoveResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMoveResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncMoveResourceWithStreamingResponse(self)

    async def create(
        self,
        postfix_id: str,
        *,
        account_id: str | None = None,
        destination: Literal[
            "Inbox", "JunkEmail", "DeletedItems", "RecoverableItemsDeletions", "RecoverableItemsPurges"
        ],
        submission: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MoveCreateResponse:
        """
        Moves a single email message to a different folder or changes its quarantine
        status.

        Args:
          account_id: Account Identifier

          postfix_id: The identifier of the message.

          submission: When true, search the submissions datastore only. When false or omitted, search
              the regular datastore only.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if account_id is None:
            account_id = self._client._get_account_id_path_param()
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not postfix_id:
            raise ValueError(f"Expected a non-empty value for `postfix_id` but received {postfix_id!r}")
        return await self._post(
            path_template(
                "/accounts/{account_id}/email-security/investigate/{postfix_id}/move",
                account_id=account_id,
                postfix_id=postfix_id,
            ),
            body=await async_maybe_transform({"destination": destination}, move_create_params.MoveCreateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"submission": submission}, move_create_params.MoveCreateParams),
                post_parser=ResultWrapper[MoveCreateResponse]._unwrapper,
            ),
            cast_to=cast(Type[MoveCreateResponse], ResultWrapper[MoveCreateResponse]),
        )

    def bulk(
        self,
        *,
        account_id: str | None = None,
        destination: Literal[
            "Inbox", "JunkEmail", "DeletedItems", "RecoverableItemsDeletions", "RecoverableItemsPurges"
        ],
        ids: SequenceNotStr[str] | Omit = omit,
        postfix_ids: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[MoveBulkResponse, AsyncSinglePage[MoveBulkResponse]]:
        """
        Maximum batch size: 1000 messages per request

        Args:
          account_id: Account Identifier

          ids: List of message IDs to move.

          postfix_ids: Deprecated: Use `ids` instead. List of message IDs to move.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if account_id is None:
            account_id = self._client._get_account_id_path_param()
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            path_template("/accounts/{account_id}/email-security/investigate/move", account_id=account_id),
            page=AsyncSinglePage[MoveBulkResponse],
            body=maybe_transform(
                {
                    "destination": destination,
                    "ids": ids,
                    "postfix_ids": postfix_ids,
                },
                move_bulk_params.MoveBulkParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=MoveBulkResponse,
            method="post",
        )


class MoveResourceWithRawResponse:
    def __init__(self, move: MoveResource) -> None:
        self._move = move

        self.create = to_raw_response_wrapper(
            move.create,
        )
        self.bulk = to_raw_response_wrapper(
            move.bulk,
        )


class AsyncMoveResourceWithRawResponse:
    def __init__(self, move: AsyncMoveResource) -> None:
        self._move = move

        self.create = async_to_raw_response_wrapper(
            move.create,
        )
        self.bulk = async_to_raw_response_wrapper(
            move.bulk,
        )


class MoveResourceWithStreamingResponse:
    def __init__(self, move: MoveResource) -> None:
        self._move = move

        self.create = to_streamed_response_wrapper(
            move.create,
        )
        self.bulk = to_streamed_response_wrapper(
            move.bulk,
        )


class AsyncMoveResourceWithStreamingResponse:
    def __init__(self, move: AsyncMoveResource) -> None:
        self._move = move

        self.create = async_to_streamed_response_wrapper(
            move.create,
        )
        self.bulk = async_to_streamed_response_wrapper(
            move.bulk,
        )
