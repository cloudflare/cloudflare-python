# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Union, Optional, cast
from datetime import datetime
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
from ...._base_client import (
    make_request_options,
)
from ....types.cloudforce_one.requests import message_get_params, message_create_params, message_update_params
from ....types.cloudforce_one.requests.message import Message
from ....types.cloudforce_one.requests.message_get_response import MessageGetResponse
from ....types.cloudforce_one.requests.message_delete_response import MessageDeleteResponse

__all__ = ["MessageResource", "AsyncMessageResource"]


class MessageResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> MessageResourceWithRawResponse:
        return MessageResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MessageResourceWithStreamingResponse:
        return MessageResourceWithStreamingResponse(self)

    def create(
        self,
        request_identifier: str,
        *,
        account_identifier: str,
        content: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Message]:
        """
        Creating a request adds the request into the Cloudforce One queue for analysis.
        In addition to the content, a short title, type, priority, and releasability
        should be provided. If one is not provided a default will be assigned.

        Args:
          account_identifier: Identifier

          request_identifier: UUID

          content: Content of message

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        if not request_identifier:
            raise ValueError(f"Expected a non-empty value for `request_identifier` but received {request_identifier!r}")
        return self._post(
            f"/accounts/{account_identifier}/cloudforce-one/requests/{request_identifier}/message/new",
            body=maybe_transform({"content": content}, message_create_params.MessageCreateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[Message]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[Message]], ResultWrapper[Message]),
        )

    def update(
        self,
        message_identifer: int,
        *,
        account_identifier: str,
        request_identifier: str,
        content: str | NotGiven = NOT_GIVEN,
        priority: str | NotGiven = NOT_GIVEN,
        request_type: str | NotGiven = NOT_GIVEN,
        summary: str | NotGiven = NOT_GIVEN,
        tlp: Literal["clear", "amber", "amber-strict", "green", "red"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Message]:
        """
        Update a Request Message

        Args:
          account_identifier: Identifier

          request_identifier: UUID

          content: Request content

          priority: Priority for analyzing the request

          request_type: Requested information from request

          summary: Brief description of the request

          tlp: The CISA defined Traffic Light Protocol (TLP)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        if not request_identifier:
            raise ValueError(f"Expected a non-empty value for `request_identifier` but received {request_identifier!r}")
        return self._put(
            f"/accounts/{account_identifier}/cloudforce-one/requests/{request_identifier}/message/{message_identifer}",
            body=maybe_transform(
                {
                    "content": content,
                    "priority": priority,
                    "request_type": request_type,
                    "summary": summary,
                    "tlp": tlp,
                },
                message_update_params.MessageUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[Message]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[Message]], ResultWrapper[Message]),
        )

    def delete(
        self,
        message_identifer: int,
        *,
        account_identifier: str,
        request_identifier: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MessageDeleteResponse:
        """
        Delete a Request Message

        Args:
          account_identifier: Identifier

          request_identifier: UUID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        if not request_identifier:
            raise ValueError(f"Expected a non-empty value for `request_identifier` but received {request_identifier!r}")
        return self._delete(
            f"/accounts/{account_identifier}/cloudforce-one/requests/{request_identifier}/message/{message_identifer}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MessageDeleteResponse,
        )

    def get(
        self,
        request_identifier: str,
        *,
        account_identifier: str,
        page: int,
        per_page: int,
        after: Union[str, datetime] | NotGiven = NOT_GIVEN,
        before: Union[str, datetime] | NotGiven = NOT_GIVEN,
        sort_by: str | NotGiven = NOT_GIVEN,
        sort_order: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[MessageGetResponse]:
        """
        List Request Messages

        Args:
          account_identifier: Identifier

          request_identifier: UUID

          page: Page number of results

          per_page: Number of results per page

          after: Retrieve messages created after this time

          before: Retrieve messages created before this time

          sort_by: Field to sort results by

          sort_order: Sort order (asc or desc)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        if not request_identifier:
            raise ValueError(f"Expected a non-empty value for `request_identifier` but received {request_identifier!r}")
        return self._post(
            f"/accounts/{account_identifier}/cloudforce-one/requests/{request_identifier}/message",
            body=maybe_transform(
                {
                    "page": page,
                    "per_page": per_page,
                    "after": after,
                    "before": before,
                    "sort_by": sort_by,
                    "sort_order": sort_order,
                },
                message_get_params.MessageGetParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[MessageGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[MessageGetResponse]], ResultWrapper[MessageGetResponse]),
        )


class AsyncMessageResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncMessageResourceWithRawResponse:
        return AsyncMessageResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMessageResourceWithStreamingResponse:
        return AsyncMessageResourceWithStreamingResponse(self)

    async def create(
        self,
        request_identifier: str,
        *,
        account_identifier: str,
        content: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Message]:
        """
        Creating a request adds the request into the Cloudforce One queue for analysis.
        In addition to the content, a short title, type, priority, and releasability
        should be provided. If one is not provided a default will be assigned.

        Args:
          account_identifier: Identifier

          request_identifier: UUID

          content: Content of message

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        if not request_identifier:
            raise ValueError(f"Expected a non-empty value for `request_identifier` but received {request_identifier!r}")
        return await self._post(
            f"/accounts/{account_identifier}/cloudforce-one/requests/{request_identifier}/message/new",
            body=await async_maybe_transform({"content": content}, message_create_params.MessageCreateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[Message]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[Message]], ResultWrapper[Message]),
        )

    async def update(
        self,
        message_identifer: int,
        *,
        account_identifier: str,
        request_identifier: str,
        content: str | NotGiven = NOT_GIVEN,
        priority: str | NotGiven = NOT_GIVEN,
        request_type: str | NotGiven = NOT_GIVEN,
        summary: str | NotGiven = NOT_GIVEN,
        tlp: Literal["clear", "amber", "amber-strict", "green", "red"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Message]:
        """
        Update a Request Message

        Args:
          account_identifier: Identifier

          request_identifier: UUID

          content: Request content

          priority: Priority for analyzing the request

          request_type: Requested information from request

          summary: Brief description of the request

          tlp: The CISA defined Traffic Light Protocol (TLP)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        if not request_identifier:
            raise ValueError(f"Expected a non-empty value for `request_identifier` but received {request_identifier!r}")
        return await self._put(
            f"/accounts/{account_identifier}/cloudforce-one/requests/{request_identifier}/message/{message_identifer}",
            body=await async_maybe_transform(
                {
                    "content": content,
                    "priority": priority,
                    "request_type": request_type,
                    "summary": summary,
                    "tlp": tlp,
                },
                message_update_params.MessageUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[Message]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[Message]], ResultWrapper[Message]),
        )

    async def delete(
        self,
        message_identifer: int,
        *,
        account_identifier: str,
        request_identifier: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MessageDeleteResponse:
        """
        Delete a Request Message

        Args:
          account_identifier: Identifier

          request_identifier: UUID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        if not request_identifier:
            raise ValueError(f"Expected a non-empty value for `request_identifier` but received {request_identifier!r}")
        return await self._delete(
            f"/accounts/{account_identifier}/cloudforce-one/requests/{request_identifier}/message/{message_identifer}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MessageDeleteResponse,
        )

    async def get(
        self,
        request_identifier: str,
        *,
        account_identifier: str,
        page: int,
        per_page: int,
        after: Union[str, datetime] | NotGiven = NOT_GIVEN,
        before: Union[str, datetime] | NotGiven = NOT_GIVEN,
        sort_by: str | NotGiven = NOT_GIVEN,
        sort_order: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[MessageGetResponse]:
        """
        List Request Messages

        Args:
          account_identifier: Identifier

          request_identifier: UUID

          page: Page number of results

          per_page: Number of results per page

          after: Retrieve messages created after this time

          before: Retrieve messages created before this time

          sort_by: Field to sort results by

          sort_order: Sort order (asc or desc)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        if not request_identifier:
            raise ValueError(f"Expected a non-empty value for `request_identifier` but received {request_identifier!r}")
        return await self._post(
            f"/accounts/{account_identifier}/cloudforce-one/requests/{request_identifier}/message",
            body=await async_maybe_transform(
                {
                    "page": page,
                    "per_page": per_page,
                    "after": after,
                    "before": before,
                    "sort_by": sort_by,
                    "sort_order": sort_order,
                },
                message_get_params.MessageGetParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[MessageGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[MessageGetResponse]], ResultWrapper[MessageGetResponse]),
        )


class MessageResourceWithRawResponse:
    def __init__(self, message: MessageResource) -> None:
        self._message = message

        self.create = to_raw_response_wrapper(
            message.create,
        )
        self.update = to_raw_response_wrapper(
            message.update,
        )
        self.delete = to_raw_response_wrapper(
            message.delete,
        )
        self.get = to_raw_response_wrapper(
            message.get,
        )


class AsyncMessageResourceWithRawResponse:
    def __init__(self, message: AsyncMessageResource) -> None:
        self._message = message

        self.create = async_to_raw_response_wrapper(
            message.create,
        )
        self.update = async_to_raw_response_wrapper(
            message.update,
        )
        self.delete = async_to_raw_response_wrapper(
            message.delete,
        )
        self.get = async_to_raw_response_wrapper(
            message.get,
        )


class MessageResourceWithStreamingResponse:
    def __init__(self, message: MessageResource) -> None:
        self._message = message

        self.create = to_streamed_response_wrapper(
            message.create,
        )
        self.update = to_streamed_response_wrapper(
            message.update,
        )
        self.delete = to_streamed_response_wrapper(
            message.delete,
        )
        self.get = to_streamed_response_wrapper(
            message.get,
        )


class AsyncMessageResourceWithStreamingResponse:
    def __init__(self, message: AsyncMessageResource) -> None:
        self._message = message

        self.create = async_to_streamed_response_wrapper(
            message.create,
        )
        self.update = async_to_streamed_response_wrapper(
            message.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            message.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            message.get,
        )
