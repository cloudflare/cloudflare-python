# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, Type, Union, cast
from datetime import datetime
from typing_extensions import Literal

import httpx

from .message import (
    Message,
    AsyncMessage,
    MessageWithRawResponse,
    AsyncMessageWithRawResponse,
    MessageWithStreamingResponse,
    AsyncMessageWithStreamingResponse,
)
from .priority import (
    Priority,
    AsyncPriority,
    PriorityWithRawResponse,
    AsyncPriorityWithRawResponse,
    PriorityWithStreamingResponse,
    AsyncPriorityWithStreamingResponse,
)
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
from ....pagination import SyncV4PagePaginationArray, AsyncV4PagePaginationArray
from ...._base_client import (
    AsyncPaginator,
    make_request_options,
)
from ....types.cloudforce_one import (
    CloudforceOneQuota,
    RequestDeleteResponse,
    CloudforceOneRequestItem,
    CloudforceOneRequestTypes,
    CloudforceOneRequestListItem,
    CloudforceOneRequestConstants,
    request_list_params,
    request_create_params,
    request_update_params,
)

__all__ = ["Requests", "AsyncRequests"]


class Requests(SyncAPIResource):
    @cached_property
    def message(self) -> Message:
        return Message(self._client)

    @cached_property
    def priority(self) -> Priority:
        return Priority(self._client)

    @cached_property
    def with_raw_response(self) -> RequestsWithRawResponse:
        return RequestsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RequestsWithStreamingResponse:
        return RequestsWithStreamingResponse(self)

    def create(
        self,
        account_identifier: str,
        *,
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
    ) -> CloudforceOneRequestItem:
        """
        Creating a request adds the request into the Cloudforce One queue for analysis.
        In addition to the content, a short title, type, priority, and releasability
        should be provided. If one is not provided a default will be assigned.

        Args:
          account_identifier: Identifier

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
        return self._post(
            f"/accounts/{account_identifier}/cloudforce-one/requests/new",
            body=maybe_transform(
                {
                    "content": content,
                    "priority": priority,
                    "request_type": request_type,
                    "summary": summary,
                    "tlp": tlp,
                },
                request_create_params.RequestCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[CloudforceOneRequestItem], ResultWrapper[CloudforceOneRequestItem]),
        )

    def update(
        self,
        request_identifier: str,
        *,
        account_identifier: str,
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
    ) -> CloudforceOneRequestItem:
        """Updating a request alters the request in the Cloudforce One queue.

        This API may
        be used to update any attributes of the request after the initial submission.
        Only fields that you choose to update need to be add to the request body

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
            f"/accounts/{account_identifier}/cloudforce-one/requests/{request_identifier}",
            body=maybe_transform(
                {
                    "content": content,
                    "priority": priority,
                    "request_type": request_type,
                    "summary": summary,
                    "tlp": tlp,
                },
                request_update_params.RequestUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[CloudforceOneRequestItem], ResultWrapper[CloudforceOneRequestItem]),
        )

    def list(
        self,
        account_identifier: str,
        *,
        page: int,
        per_page: int,
        completed_after: Union[str, datetime] | NotGiven = NOT_GIVEN,
        completed_before: Union[str, datetime] | NotGiven = NOT_GIVEN,
        created_after: Union[str, datetime] | NotGiven = NOT_GIVEN,
        created_before: Union[str, datetime] | NotGiven = NOT_GIVEN,
        request_type: str | NotGiven = NOT_GIVEN,
        sort_by: str | NotGiven = NOT_GIVEN,
        sort_order: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
        status: Literal["open", "accepted", "reported", "approved", "completed", "declined"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncV4PagePaginationArray[CloudforceOneRequestListItem]:
        """
        List Requests

        Args:
          account_identifier: Identifier

          page: Page number of results

          per_page: Number of results per page

          completed_after: Retrieve requests completed after this time

          completed_before: Retrieve requests completed before this time

          created_after: Retrieve requests created after this time

          created_before: Retrieve requests created before this time

          request_type: Requested information from request

          sort_by: Field to sort results by

          sort_order: Sort order (asc or desc)

          status: Request Status

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        return self._get_api_list(
            f"/accounts/{account_identifier}/cloudforce-one/requests",
            page=SyncV4PagePaginationArray[CloudforceOneRequestListItem],
            body=maybe_transform(
                {
                    "page": page,
                    "per_page": per_page,
                    "completed_after": completed_after,
                    "completed_before": completed_before,
                    "created_after": created_after,
                    "created_before": created_before,
                    "request_type": request_type,
                    "sort_by": sort_by,
                    "sort_order": sort_order,
                    "status": status,
                },
                request_list_params.RequestListParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=CloudforceOneRequestListItem,
            method="post",
        )

    def delete(
        self,
        request_identifier: str,
        *,
        account_identifier: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RequestDeleteResponse:
        """
        Delete a Request

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
        return cast(
            RequestDeleteResponse,
            self._delete(
                f"/accounts/{account_identifier}/cloudforce-one/requests/{request_identifier}",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[RequestDeleteResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def constants(
        self,
        account_identifier: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CloudforceOneRequestConstants:
        """
        Get Request Priority, Status, and TLP constants

        Args:
          account_identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        return self._get(
            f"/accounts/{account_identifier}/cloudforce-one/requests/constants",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[CloudforceOneRequestConstants], ResultWrapper[CloudforceOneRequestConstants]),
        )

    def get(
        self,
        request_identifier: str,
        *,
        account_identifier: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CloudforceOneRequestItem:
        """
        Get a Request

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
        return self._get(
            f"/accounts/{account_identifier}/cloudforce-one/requests/{request_identifier}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[CloudforceOneRequestItem], ResultWrapper[CloudforceOneRequestItem]),
        )

    def quota(
        self,
        account_identifier: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CloudforceOneQuota:
        """
        Get Request Quota

        Args:
          account_identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        return self._get(
            f"/accounts/{account_identifier}/cloudforce-one/requests/quota",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[CloudforceOneQuota], ResultWrapper[CloudforceOneQuota]),
        )

    def types(
        self,
        account_identifier: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CloudforceOneRequestTypes:
        """
        Get Request Types

        Args:
          account_identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        return self._get(
            f"/accounts/{account_identifier}/cloudforce-one/requests/types",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[CloudforceOneRequestTypes], ResultWrapper[CloudforceOneRequestTypes]),
        )


class AsyncRequests(AsyncAPIResource):
    @cached_property
    def message(self) -> AsyncMessage:
        return AsyncMessage(self._client)

    @cached_property
    def priority(self) -> AsyncPriority:
        return AsyncPriority(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncRequestsWithRawResponse:
        return AsyncRequestsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRequestsWithStreamingResponse:
        return AsyncRequestsWithStreamingResponse(self)

    async def create(
        self,
        account_identifier: str,
        *,
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
    ) -> CloudforceOneRequestItem:
        """
        Creating a request adds the request into the Cloudforce One queue for analysis.
        In addition to the content, a short title, type, priority, and releasability
        should be provided. If one is not provided a default will be assigned.

        Args:
          account_identifier: Identifier

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
        return await self._post(
            f"/accounts/{account_identifier}/cloudforce-one/requests/new",
            body=await async_maybe_transform(
                {
                    "content": content,
                    "priority": priority,
                    "request_type": request_type,
                    "summary": summary,
                    "tlp": tlp,
                },
                request_create_params.RequestCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[CloudforceOneRequestItem], ResultWrapper[CloudforceOneRequestItem]),
        )

    async def update(
        self,
        request_identifier: str,
        *,
        account_identifier: str,
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
    ) -> CloudforceOneRequestItem:
        """Updating a request alters the request in the Cloudforce One queue.

        This API may
        be used to update any attributes of the request after the initial submission.
        Only fields that you choose to update need to be add to the request body

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
            f"/accounts/{account_identifier}/cloudforce-one/requests/{request_identifier}",
            body=await async_maybe_transform(
                {
                    "content": content,
                    "priority": priority,
                    "request_type": request_type,
                    "summary": summary,
                    "tlp": tlp,
                },
                request_update_params.RequestUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[CloudforceOneRequestItem], ResultWrapper[CloudforceOneRequestItem]),
        )

    def list(
        self,
        account_identifier: str,
        *,
        page: int,
        per_page: int,
        completed_after: Union[str, datetime] | NotGiven = NOT_GIVEN,
        completed_before: Union[str, datetime] | NotGiven = NOT_GIVEN,
        created_after: Union[str, datetime] | NotGiven = NOT_GIVEN,
        created_before: Union[str, datetime] | NotGiven = NOT_GIVEN,
        request_type: str | NotGiven = NOT_GIVEN,
        sort_by: str | NotGiven = NOT_GIVEN,
        sort_order: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
        status: Literal["open", "accepted", "reported", "approved", "completed", "declined"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[CloudforceOneRequestListItem, AsyncV4PagePaginationArray[CloudforceOneRequestListItem]]:
        """
        List Requests

        Args:
          account_identifier: Identifier

          page: Page number of results

          per_page: Number of results per page

          completed_after: Retrieve requests completed after this time

          completed_before: Retrieve requests completed before this time

          created_after: Retrieve requests created after this time

          created_before: Retrieve requests created before this time

          request_type: Requested information from request

          sort_by: Field to sort results by

          sort_order: Sort order (asc or desc)

          status: Request Status

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        return self._get_api_list(
            f"/accounts/{account_identifier}/cloudforce-one/requests",
            page=AsyncV4PagePaginationArray[CloudforceOneRequestListItem],
            body=maybe_transform(
                {
                    "page": page,
                    "per_page": per_page,
                    "completed_after": completed_after,
                    "completed_before": completed_before,
                    "created_after": created_after,
                    "created_before": created_before,
                    "request_type": request_type,
                    "sort_by": sort_by,
                    "sort_order": sort_order,
                    "status": status,
                },
                request_list_params.RequestListParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=CloudforceOneRequestListItem,
            method="post",
        )

    async def delete(
        self,
        request_identifier: str,
        *,
        account_identifier: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RequestDeleteResponse:
        """
        Delete a Request

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
        return cast(
            RequestDeleteResponse,
            await self._delete(
                f"/accounts/{account_identifier}/cloudforce-one/requests/{request_identifier}",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[RequestDeleteResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def constants(
        self,
        account_identifier: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CloudforceOneRequestConstants:
        """
        Get Request Priority, Status, and TLP constants

        Args:
          account_identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        return await self._get(
            f"/accounts/{account_identifier}/cloudforce-one/requests/constants",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[CloudforceOneRequestConstants], ResultWrapper[CloudforceOneRequestConstants]),
        )

    async def get(
        self,
        request_identifier: str,
        *,
        account_identifier: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CloudforceOneRequestItem:
        """
        Get a Request

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
        return await self._get(
            f"/accounts/{account_identifier}/cloudforce-one/requests/{request_identifier}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[CloudforceOneRequestItem], ResultWrapper[CloudforceOneRequestItem]),
        )

    async def quota(
        self,
        account_identifier: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CloudforceOneQuota:
        """
        Get Request Quota

        Args:
          account_identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        return await self._get(
            f"/accounts/{account_identifier}/cloudforce-one/requests/quota",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[CloudforceOneQuota], ResultWrapper[CloudforceOneQuota]),
        )

    async def types(
        self,
        account_identifier: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CloudforceOneRequestTypes:
        """
        Get Request Types

        Args:
          account_identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        return await self._get(
            f"/accounts/{account_identifier}/cloudforce-one/requests/types",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[CloudforceOneRequestTypes], ResultWrapper[CloudforceOneRequestTypes]),
        )


class RequestsWithRawResponse:
    def __init__(self, requests: Requests) -> None:
        self._requests = requests

        self.create = to_raw_response_wrapper(
            requests.create,
        )
        self.update = to_raw_response_wrapper(
            requests.update,
        )
        self.list = to_raw_response_wrapper(
            requests.list,
        )
        self.delete = to_raw_response_wrapper(
            requests.delete,
        )
        self.constants = to_raw_response_wrapper(
            requests.constants,
        )
        self.get = to_raw_response_wrapper(
            requests.get,
        )
        self.quota = to_raw_response_wrapper(
            requests.quota,
        )
        self.types = to_raw_response_wrapper(
            requests.types,
        )

    @cached_property
    def message(self) -> MessageWithRawResponse:
        return MessageWithRawResponse(self._requests.message)

    @cached_property
    def priority(self) -> PriorityWithRawResponse:
        return PriorityWithRawResponse(self._requests.priority)


class AsyncRequestsWithRawResponse:
    def __init__(self, requests: AsyncRequests) -> None:
        self._requests = requests

        self.create = async_to_raw_response_wrapper(
            requests.create,
        )
        self.update = async_to_raw_response_wrapper(
            requests.update,
        )
        self.list = async_to_raw_response_wrapper(
            requests.list,
        )
        self.delete = async_to_raw_response_wrapper(
            requests.delete,
        )
        self.constants = async_to_raw_response_wrapper(
            requests.constants,
        )
        self.get = async_to_raw_response_wrapper(
            requests.get,
        )
        self.quota = async_to_raw_response_wrapper(
            requests.quota,
        )
        self.types = async_to_raw_response_wrapper(
            requests.types,
        )

    @cached_property
    def message(self) -> AsyncMessageWithRawResponse:
        return AsyncMessageWithRawResponse(self._requests.message)

    @cached_property
    def priority(self) -> AsyncPriorityWithRawResponse:
        return AsyncPriorityWithRawResponse(self._requests.priority)


class RequestsWithStreamingResponse:
    def __init__(self, requests: Requests) -> None:
        self._requests = requests

        self.create = to_streamed_response_wrapper(
            requests.create,
        )
        self.update = to_streamed_response_wrapper(
            requests.update,
        )
        self.list = to_streamed_response_wrapper(
            requests.list,
        )
        self.delete = to_streamed_response_wrapper(
            requests.delete,
        )
        self.constants = to_streamed_response_wrapper(
            requests.constants,
        )
        self.get = to_streamed_response_wrapper(
            requests.get,
        )
        self.quota = to_streamed_response_wrapper(
            requests.quota,
        )
        self.types = to_streamed_response_wrapper(
            requests.types,
        )

    @cached_property
    def message(self) -> MessageWithStreamingResponse:
        return MessageWithStreamingResponse(self._requests.message)

    @cached_property
    def priority(self) -> PriorityWithStreamingResponse:
        return PriorityWithStreamingResponse(self._requests.priority)


class AsyncRequestsWithStreamingResponse:
    def __init__(self, requests: AsyncRequests) -> None:
        self._requests = requests

        self.create = async_to_streamed_response_wrapper(
            requests.create,
        )
        self.update = async_to_streamed_response_wrapper(
            requests.update,
        )
        self.list = async_to_streamed_response_wrapper(
            requests.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            requests.delete,
        )
        self.constants = async_to_streamed_response_wrapper(
            requests.constants,
        )
        self.get = async_to_streamed_response_wrapper(
            requests.get,
        )
        self.quota = async_to_streamed_response_wrapper(
            requests.quota,
        )
        self.types = async_to_streamed_response_wrapper(
            requests.types,
        )

    @cached_property
    def message(self) -> AsyncMessageWithStreamingResponse:
        return AsyncMessageWithStreamingResponse(self._requests.message)

    @cached_property
    def priority(self) -> AsyncPriorityWithStreamingResponse:
        return AsyncPriorityWithStreamingResponse(self._requests.priority)
