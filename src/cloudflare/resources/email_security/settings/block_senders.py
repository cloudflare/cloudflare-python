# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._compat import cached_property

from typing_extensions import Literal

from typing import Optional, Iterable, Type

from ....types.email_security.settings.block_sender_create_response import BlockSenderCreateResponse

from ...._wrappers import ResultWrapper

from ...._utils import maybe_transform, async_maybe_transform

from ...._base_client import make_request_options, AsyncPaginator

from ....types.email_security.settings.block_sender_list_response import BlockSenderListResponse

from ....pagination import SyncV4PagePaginationArray, AsyncV4PagePaginationArray

from ....types.email_security.settings.block_sender_delete_response import BlockSenderDeleteResponse

from ....types.email_security.settings.block_sender_edit_response import BlockSenderEditResponse

from ....types.email_security.settings.block_sender_get_response import BlockSenderGetResponse

from ...._response import (
    to_raw_response_wrapper,
    async_to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_streamed_response_wrapper,
)

from ....types.email_security.settings import block_sender_create_params

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ...._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ...._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ...._resource import SyncAPIResource, AsyncAPIResource
from ....types import shared_params
from ....types.email_security.settings import block_sender_create_params
from ....types.email_security.settings import block_sender_list_params
from ....types.email_security.settings import block_sender_edit_params
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

__all__ = ["BlockSendersResource", "AsyncBlockSendersResource"]


class BlockSendersResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> BlockSendersResourceWithRawResponse:
        return BlockSendersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BlockSendersResourceWithStreamingResponse:
        return BlockSendersResourceWithStreamingResponse(self)

    @overload
    def create(
        self,
        *,
        account_id: str,
        is_regex: bool,
        pattern: str,
        pattern_type: Literal["EMAIL", "DOMAIN", "IP", "UNKNOWN"],
        comments: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BlockSenderCreateResponse:
        """
        Create a blocked email sender

        Args:
          account_id: Account Identifier

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
        body: Iterable[block_sender_create_params.Variant1Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BlockSenderCreateResponse:
        """
        Create a blocked email sender

        Args:
          account_id: Account Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["account_id", "is_regex", "pattern", "pattern_type"], ["account_id", "body"])
    def create(
        self,
        *,
        account_id: str,
        is_regex: bool | NotGiven = NOT_GIVEN,
        pattern: str | NotGiven = NOT_GIVEN,
        pattern_type: Literal["EMAIL", "DOMAIN", "IP", "UNKNOWN"] | NotGiven = NOT_GIVEN,
        comments: Optional[str] | NotGiven = NOT_GIVEN,
        body: Iterable[block_sender_create_params.Variant1Body] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BlockSenderCreateResponse:
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return cast(
            BlockSenderCreateResponse,
            self._post(
                f"/accounts/{account_id}/email-security/settings/block_senders",
                body=maybe_transform(
                    {
                        "is_regex": is_regex,
                        "pattern": pattern,
                        "pattern_type": pattern_type,
                        "comments": comments,
                        "body": body,
                    },
                    block_sender_create_params.BlockSenderCreateParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper[BlockSenderCreateResponse]._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[BlockSenderCreateResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def list(
        self,
        *,
        account_id: str,
        direction: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
        order: Literal["pattern", "created_at"] | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        pattern_type: Literal["EMAIL", "DOMAIN", "IP", "UNKNOWN"] | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        search: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncV4PagePaginationArray[BlockSenderListResponse]:
        """
        List blocked email senders

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
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/email-security/settings/block_senders",
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
        pattern_id: int,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BlockSenderDeleteResponse:
        """
        Delete a blocked email sender

        Args:
          account_id: Account Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._delete(
            f"/accounts/{account_id}/email-security/settings/block_senders/{pattern_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[BlockSenderDeleteResponse]._unwrapper,
            ),
            cast_to=cast(Type[BlockSenderDeleteResponse], ResultWrapper[BlockSenderDeleteResponse]),
        )

    def edit(
        self,
        pattern_id: int,
        *,
        account_id: str,
        comments: Optional[str] | NotGiven = NOT_GIVEN,
        is_regex: Optional[bool] | NotGiven = NOT_GIVEN,
        pattern: Optional[str] | NotGiven = NOT_GIVEN,
        pattern_type: Optional[Literal["EMAIL", "DOMAIN", "IP", "UNKNOWN"]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BlockSenderEditResponse:
        """
        Update a blocked email sender

        Args:
          account_id: Account Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._patch(
            f"/accounts/{account_id}/email-security/settings/block_senders/{pattern_id}",
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
                post_parser=ResultWrapper[BlockSenderEditResponse]._unwrapper,
            ),
            cast_to=cast(Type[BlockSenderEditResponse], ResultWrapper[BlockSenderEditResponse]),
        )

    def get(
        self,
        pattern_id: int,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BlockSenderGetResponse:
        """
        Get a blocked email sender

        Args:
          account_id: Account Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get(
            f"/accounts/{account_id}/email-security/settings/block_senders/{pattern_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[BlockSenderGetResponse]._unwrapper,
            ),
            cast_to=cast(Type[BlockSenderGetResponse], ResultWrapper[BlockSenderGetResponse]),
        )


class AsyncBlockSendersResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncBlockSendersResourceWithRawResponse:
        return AsyncBlockSendersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBlockSendersResourceWithStreamingResponse:
        return AsyncBlockSendersResourceWithStreamingResponse(self)

    @overload
    async def create(
        self,
        *,
        account_id: str,
        is_regex: bool,
        pattern: str,
        pattern_type: Literal["EMAIL", "DOMAIN", "IP", "UNKNOWN"],
        comments: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BlockSenderCreateResponse:
        """
        Create a blocked email sender

        Args:
          account_id: Account Identifier

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
        body: Iterable[block_sender_create_params.Variant1Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BlockSenderCreateResponse:
        """
        Create a blocked email sender

        Args:
          account_id: Account Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["account_id", "is_regex", "pattern", "pattern_type"], ["account_id", "body"])
    async def create(
        self,
        *,
        account_id: str,
        is_regex: bool | NotGiven = NOT_GIVEN,
        pattern: str | NotGiven = NOT_GIVEN,
        pattern_type: Literal["EMAIL", "DOMAIN", "IP", "UNKNOWN"] | NotGiven = NOT_GIVEN,
        comments: Optional[str] | NotGiven = NOT_GIVEN,
        body: Iterable[block_sender_create_params.Variant1Body] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BlockSenderCreateResponse:
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return cast(
            BlockSenderCreateResponse,
            await self._post(
                f"/accounts/{account_id}/email-security/settings/block_senders",
                body=await async_maybe_transform(
                    {
                        "is_regex": is_regex,
                        "pattern": pattern,
                        "pattern_type": pattern_type,
                        "comments": comments,
                        "body": body,
                    },
                    block_sender_create_params.BlockSenderCreateParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper[BlockSenderCreateResponse]._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[BlockSenderCreateResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def list(
        self,
        *,
        account_id: str,
        direction: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
        order: Literal["pattern", "created_at"] | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        pattern_type: Literal["EMAIL", "DOMAIN", "IP", "UNKNOWN"] | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        search: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[BlockSenderListResponse, AsyncV4PagePaginationArray[BlockSenderListResponse]]:
        """
        List blocked email senders

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
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/email-security/settings/block_senders",
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
        pattern_id: int,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BlockSenderDeleteResponse:
        """
        Delete a blocked email sender

        Args:
          account_id: Account Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._delete(
            f"/accounts/{account_id}/email-security/settings/block_senders/{pattern_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[BlockSenderDeleteResponse]._unwrapper,
            ),
            cast_to=cast(Type[BlockSenderDeleteResponse], ResultWrapper[BlockSenderDeleteResponse]),
        )

    async def edit(
        self,
        pattern_id: int,
        *,
        account_id: str,
        comments: Optional[str] | NotGiven = NOT_GIVEN,
        is_regex: Optional[bool] | NotGiven = NOT_GIVEN,
        pattern: Optional[str] | NotGiven = NOT_GIVEN,
        pattern_type: Optional[Literal["EMAIL", "DOMAIN", "IP", "UNKNOWN"]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BlockSenderEditResponse:
        """
        Update a blocked email sender

        Args:
          account_id: Account Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._patch(
            f"/accounts/{account_id}/email-security/settings/block_senders/{pattern_id}",
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
                post_parser=ResultWrapper[BlockSenderEditResponse]._unwrapper,
            ),
            cast_to=cast(Type[BlockSenderEditResponse], ResultWrapper[BlockSenderEditResponse]),
        )

    async def get(
        self,
        pattern_id: int,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BlockSenderGetResponse:
        """
        Get a blocked email sender

        Args:
          account_id: Account Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._get(
            f"/accounts/{account_id}/email-security/settings/block_senders/{pattern_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[BlockSenderGetResponse]._unwrapper,
            ),
            cast_to=cast(Type[BlockSenderGetResponse], ResultWrapper[BlockSenderGetResponse]),
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
