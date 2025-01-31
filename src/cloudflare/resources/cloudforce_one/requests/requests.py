# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Union, Optional, cast
from datetime import datetime
from typing_extensions import Literal

import httpx

from .assets import (
    AssetsResource,
    AsyncAssetsResource,
    AssetsResourceWithRawResponse,
    AsyncAssetsResourceWithRawResponse,
    AssetsResourceWithStreamingResponse,
    AsyncAssetsResourceWithStreamingResponse,
)
from .message import (
    MessageResource,
    AsyncMessageResource,
    MessageResourceWithRawResponse,
    AsyncMessageResourceWithRawResponse,
    MessageResourceWithStreamingResponse,
    AsyncMessageResourceWithStreamingResponse,
)
from .priority import (
    PriorityResource,
    AsyncPriorityResource,
    PriorityResourceWithRawResponse,
    AsyncPriorityResourceWithRawResponse,
    PriorityResourceWithStreamingResponse,
    AsyncPriorityResourceWithStreamingResponse,
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
from ....pagination import SyncSinglePage, AsyncSinglePage
from ...._base_client import AsyncPaginator, make_request_options
from ....types.cloudforce_one import request_list_params, request_create_params, request_update_params
from ....types.cloudforce_one.item import Item
from ....types.cloudforce_one.quota import Quota
from ....types.cloudforce_one.list_item import ListItem
from ....types.cloudforce_one.request_constants import RequestConstants
from ....types.cloudforce_one.request_types_response import RequestTypesResponse
from ....types.cloudforce_one.request_delete_response import RequestDeleteResponse

__all__ = ["RequestsResource", "AsyncRequestsResource"]


class RequestsResource(SyncAPIResource):
    @cached_property
    def message(self) -> MessageResource:
        return MessageResource(self._client)

    @cached_property
    def priority(self) -> PriorityResource:
        return PriorityResource(self._client)

    @cached_property
    def assets(self) -> AssetsResource:
        return AssetsResource(self._client)

    @cached_property
    def with_raw_response(self) -> RequestsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return RequestsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RequestsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return RequestsResourceWithStreamingResponse(self)

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
    ) -> Optional[Item]:
        """
        Creating a request adds the request into the Cloudforce One queue for analysis.
        In addition to the content, a short title, type, priority, and releasability
        should be provided. If one is not provided, a default will be assigned.

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
                post_parser=ResultWrapper[Optional[Item]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[Item]], ResultWrapper[Item]),
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
    ) -> Optional[Item]:
        """Updating a request alters the request in the Cloudforce One queue.

        This API may
        be used to update any attributes of the request after the initial submission.
        Only fields that you choose to update need to be add to the request body.

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
                post_parser=ResultWrapper[Optional[Item]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[Item]], ResultWrapper[Item]),
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
    ) -> SyncSinglePage[ListItem]:
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
            page=SyncSinglePage[ListItem],
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
            model=ListItem,
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
        return self._delete(
            f"/accounts/{account_identifier}/cloudforce-one/requests/{request_identifier}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RequestDeleteResponse,
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
    ) -> Optional[RequestConstants]:
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
                post_parser=ResultWrapper[Optional[RequestConstants]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[RequestConstants]], ResultWrapper[RequestConstants]),
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
    ) -> Optional[Item]:
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
                post_parser=ResultWrapper[Optional[Item]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[Item]], ResultWrapper[Item]),
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
    ) -> Optional[Quota]:
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
                post_parser=ResultWrapper[Optional[Quota]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[Quota]], ResultWrapper[Quota]),
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
    ) -> SyncSinglePage[RequestTypesResponse]:
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
        return self._get_api_list(
            f"/accounts/{account_identifier}/cloudforce-one/requests/types",
            page=SyncSinglePage[RequestTypesResponse],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=str,
        )


class AsyncRequestsResource(AsyncAPIResource):
    @cached_property
    def message(self) -> AsyncMessageResource:
        return AsyncMessageResource(self._client)

    @cached_property
    def priority(self) -> AsyncPriorityResource:
        return AsyncPriorityResource(self._client)

    @cached_property
    def assets(self) -> AsyncAssetsResource:
        return AsyncAssetsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncRequestsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRequestsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRequestsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncRequestsResourceWithStreamingResponse(self)

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
    ) -> Optional[Item]:
        """
        Creating a request adds the request into the Cloudforce One queue for analysis.
        In addition to the content, a short title, type, priority, and releasability
        should be provided. If one is not provided, a default will be assigned.

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
                post_parser=ResultWrapper[Optional[Item]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[Item]], ResultWrapper[Item]),
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
    ) -> Optional[Item]:
        """Updating a request alters the request in the Cloudforce One queue.

        This API may
        be used to update any attributes of the request after the initial submission.
        Only fields that you choose to update need to be add to the request body.

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
                post_parser=ResultWrapper[Optional[Item]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[Item]], ResultWrapper[Item]),
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
    ) -> AsyncPaginator[ListItem, AsyncSinglePage[ListItem]]:
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
            page=AsyncSinglePage[ListItem],
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
            model=ListItem,
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
        return await self._delete(
            f"/accounts/{account_identifier}/cloudforce-one/requests/{request_identifier}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RequestDeleteResponse,
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
    ) -> Optional[RequestConstants]:
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
                post_parser=ResultWrapper[Optional[RequestConstants]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[RequestConstants]], ResultWrapper[RequestConstants]),
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
    ) -> Optional[Item]:
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
                post_parser=ResultWrapper[Optional[Item]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[Item]], ResultWrapper[Item]),
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
    ) -> Optional[Quota]:
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
                post_parser=ResultWrapper[Optional[Quota]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[Quota]], ResultWrapper[Quota]),
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
    ) -> AsyncPaginator[RequestTypesResponse, AsyncSinglePage[RequestTypesResponse]]:
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
        return self._get_api_list(
            f"/accounts/{account_identifier}/cloudforce-one/requests/types",
            page=AsyncSinglePage[RequestTypesResponse],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=str,
        )


class RequestsResourceWithRawResponse:
    def __init__(self, requests: RequestsResource) -> None:
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
    def message(self) -> MessageResourceWithRawResponse:
        return MessageResourceWithRawResponse(self._requests.message)

    @cached_property
    def priority(self) -> PriorityResourceWithRawResponse:
        return PriorityResourceWithRawResponse(self._requests.priority)

    @cached_property
    def assets(self) -> AssetsResourceWithRawResponse:
        return AssetsResourceWithRawResponse(self._requests.assets)


class AsyncRequestsResourceWithRawResponse:
    def __init__(self, requests: AsyncRequestsResource) -> None:
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
    def message(self) -> AsyncMessageResourceWithRawResponse:
        return AsyncMessageResourceWithRawResponse(self._requests.message)

    @cached_property
    def priority(self) -> AsyncPriorityResourceWithRawResponse:
        return AsyncPriorityResourceWithRawResponse(self._requests.priority)

    @cached_property
    def assets(self) -> AsyncAssetsResourceWithRawResponse:
        return AsyncAssetsResourceWithRawResponse(self._requests.assets)


class RequestsResourceWithStreamingResponse:
    def __init__(self, requests: RequestsResource) -> None:
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
    def message(self) -> MessageResourceWithStreamingResponse:
        return MessageResourceWithStreamingResponse(self._requests.message)

    @cached_property
    def priority(self) -> PriorityResourceWithStreamingResponse:
        return PriorityResourceWithStreamingResponse(self._requests.priority)

    @cached_property
    def assets(self) -> AssetsResourceWithStreamingResponse:
        return AssetsResourceWithStreamingResponse(self._requests.assets)


class AsyncRequestsResourceWithStreamingResponse:
    def __init__(self, requests: AsyncRequestsResource) -> None:
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
    def message(self) -> AsyncMessageResourceWithStreamingResponse:
        return AsyncMessageResourceWithStreamingResponse(self._requests.message)

    @cached_property
    def priority(self) -> AsyncPriorityResourceWithStreamingResponse:
        return AsyncPriorityResourceWithStreamingResponse(self._requests.priority)

    @cached_property
    def assets(self) -> AsyncAssetsResourceWithStreamingResponse:
        return AsyncAssetsResourceWithStreamingResponse(self._requests.assets)
