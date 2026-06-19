# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Optional, cast
from typing_extensions import Literal

import httpx

from .cancel import (
    CancelResource,
    AsyncCancelResource,
    CancelResourceWithRawResponse,
    AsyncCancelResourceWithRawResponse,
    CancelResourceWithStreamingResponse,
    AsyncCancelResourceWithStreamingResponse,
)
from .messages import (
    MessagesResource,
    AsyncMessagesResource,
    MessagesResourceWithRawResponse,
    AsyncMessagesResourceWithRawResponse,
    MessagesResourceWithStreamingResponse,
    AsyncMessagesResourceWithStreamingResponse,
)
from ....._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ....._utils import path_template, maybe_transform, async_maybe_transform
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....._wrappers import ResultWrapper
from .....pagination import SyncV4PagePaginationArray, AsyncV4PagePaginationArray
from ....._base_client import AsyncPaginator, make_request_options
from .....types.email_security.investigate import bulk_list_params, bulk_create_params
from .....types.email_security.investigate.bulk_get_response import BulkGetResponse
from .....types.email_security.investigate.bulk_list_response import BulkListResponse
from .....types.email_security.investigate.bulk_create_response import BulkCreateResponse
from .....types.email_security.investigate.bulk_delete_response import BulkDeleteResponse

__all__ = ["BulkResource", "AsyncBulkResource"]


class BulkResource(SyncAPIResource):
    @cached_property
    def cancel(self) -> CancelResource:
        return CancelResource(self._client)

    @cached_property
    def messages(self) -> MessagesResource:
        return MessagesResource(self._client)

    @cached_property
    def with_raw_response(self) -> BulkResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return BulkResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BulkResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return BulkResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        account_id: str,
        action: Literal["MOVE", "RELEASE"],
        search_params: bulk_create_params.SearchParams,
        comment: Optional[str] | Omit = omit,
        destination: Literal[
            "Inbox", "JunkEmail", "DeletedItems", "RecoverableItemsDeletions", "RecoverableItemsPurges"
        ]
        | Omit = omit,
        expected_disposition: Literal[
            "MALICIOUS",
            "MALICIOUS-BEC",
            "SUSPICIOUS",
            "SPOOF",
            "SPAM",
            "BULK",
            "ENCRYPTED",
            "EXTERNAL",
            "UNKNOWN",
            "NONE",
        ]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BulkCreateResponse:
        """
        Create a bulk action job

        Args:
          account_id: Identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._post(
            path_template("/accounts/{account_id}/email-security/investigate/bulk", account_id=account_id),
            body=maybe_transform(
                {
                    "action": action,
                    "search_params": search_params,
                    "comment": comment,
                    "destination": destination,
                    "expected_disposition": expected_disposition,
                },
                bulk_create_params.BulkCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[BulkCreateResponse]._unwrapper,
            ),
            cast_to=cast(Type[BulkCreateResponse], ResultWrapper[BulkCreateResponse]),
        )

    def list(
        self,
        *,
        account_id: str,
        action_type: Literal["MOVE", "RELEASE"] | Omit = omit,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        status: Literal["PENDING", "DISCOVERING", "PROCESSING", "COMPLETED", "FAILED", "CANCELLED", "SKIPPED"]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncV4PagePaginationArray[BulkListResponse]:
        """
        List bulk action jobs

        Args:
          account_id: Identifier.

          page: Current page within paginated list of results.

          per_page: The number of results per page. Maximum value is 1000.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            path_template("/accounts/{account_id}/email-security/investigate/bulk", account_id=account_id),
            page=SyncV4PagePaginationArray[BulkListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "action_type": action_type,
                        "page": page,
                        "per_page": per_page,
                        "status": status,
                    },
                    bulk_list_params.BulkListParams,
                ),
            ),
            model=BulkListResponse,
        )

    def delete(
        self,
        job_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BulkDeleteResponse:
        """Soft-deletes the job, hiding it from all list and detail endpoints.

        Only jobs in
        a terminal state (`COMPLETED`, `CANCELLED`, `FAILED`, or `SKIPPED`) can be
        deleted. To stop an in-progress job without removing it, use the cancel endpoint
        instead.

        Args:
          account_id: Identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        return self._delete(
            path_template(
                "/accounts/{account_id}/email-security/investigate/bulk/{job_id}", account_id=account_id, job_id=job_id
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[BulkDeleteResponse]._unwrapper,
            ),
            cast_to=cast(Type[BulkDeleteResponse], ResultWrapper[BulkDeleteResponse]),
        )

    def get(
        self,
        job_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BulkGetResponse:
        """
        Get bulk action job details

        Args:
          account_id: Identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        return self._get(
            path_template(
                "/accounts/{account_id}/email-security/investigate/bulk/{job_id}", account_id=account_id, job_id=job_id
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[BulkGetResponse]._unwrapper,
            ),
            cast_to=cast(Type[BulkGetResponse], ResultWrapper[BulkGetResponse]),
        )


class AsyncBulkResource(AsyncAPIResource):
    @cached_property
    def cancel(self) -> AsyncCancelResource:
        return AsyncCancelResource(self._client)

    @cached_property
    def messages(self) -> AsyncMessagesResource:
        return AsyncMessagesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncBulkResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncBulkResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBulkResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncBulkResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_id: str,
        action: Literal["MOVE", "RELEASE"],
        search_params: bulk_create_params.SearchParams,
        comment: Optional[str] | Omit = omit,
        destination: Literal[
            "Inbox", "JunkEmail", "DeletedItems", "RecoverableItemsDeletions", "RecoverableItemsPurges"
        ]
        | Omit = omit,
        expected_disposition: Literal[
            "MALICIOUS",
            "MALICIOUS-BEC",
            "SUSPICIOUS",
            "SPOOF",
            "SPAM",
            "BULK",
            "ENCRYPTED",
            "EXTERNAL",
            "UNKNOWN",
            "NONE",
        ]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BulkCreateResponse:
        """
        Create a bulk action job

        Args:
          account_id: Identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._post(
            path_template("/accounts/{account_id}/email-security/investigate/bulk", account_id=account_id),
            body=await async_maybe_transform(
                {
                    "action": action,
                    "search_params": search_params,
                    "comment": comment,
                    "destination": destination,
                    "expected_disposition": expected_disposition,
                },
                bulk_create_params.BulkCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[BulkCreateResponse]._unwrapper,
            ),
            cast_to=cast(Type[BulkCreateResponse], ResultWrapper[BulkCreateResponse]),
        )

    def list(
        self,
        *,
        account_id: str,
        action_type: Literal["MOVE", "RELEASE"] | Omit = omit,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        status: Literal["PENDING", "DISCOVERING", "PROCESSING", "COMPLETED", "FAILED", "CANCELLED", "SKIPPED"]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[BulkListResponse, AsyncV4PagePaginationArray[BulkListResponse]]:
        """
        List bulk action jobs

        Args:
          account_id: Identifier.

          page: Current page within paginated list of results.

          per_page: The number of results per page. Maximum value is 1000.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            path_template("/accounts/{account_id}/email-security/investigate/bulk", account_id=account_id),
            page=AsyncV4PagePaginationArray[BulkListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "action_type": action_type,
                        "page": page,
                        "per_page": per_page,
                        "status": status,
                    },
                    bulk_list_params.BulkListParams,
                ),
            ),
            model=BulkListResponse,
        )

    async def delete(
        self,
        job_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BulkDeleteResponse:
        """Soft-deletes the job, hiding it from all list and detail endpoints.

        Only jobs in
        a terminal state (`COMPLETED`, `CANCELLED`, `FAILED`, or `SKIPPED`) can be
        deleted. To stop an in-progress job without removing it, use the cancel endpoint
        instead.

        Args:
          account_id: Identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        return await self._delete(
            path_template(
                "/accounts/{account_id}/email-security/investigate/bulk/{job_id}", account_id=account_id, job_id=job_id
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[BulkDeleteResponse]._unwrapper,
            ),
            cast_to=cast(Type[BulkDeleteResponse], ResultWrapper[BulkDeleteResponse]),
        )

    async def get(
        self,
        job_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BulkGetResponse:
        """
        Get bulk action job details

        Args:
          account_id: Identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        return await self._get(
            path_template(
                "/accounts/{account_id}/email-security/investigate/bulk/{job_id}", account_id=account_id, job_id=job_id
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[BulkGetResponse]._unwrapper,
            ),
            cast_to=cast(Type[BulkGetResponse], ResultWrapper[BulkGetResponse]),
        )


class BulkResourceWithRawResponse:
    def __init__(self, bulk: BulkResource) -> None:
        self._bulk = bulk

        self.create = to_raw_response_wrapper(
            bulk.create,
        )
        self.list = to_raw_response_wrapper(
            bulk.list,
        )
        self.delete = to_raw_response_wrapper(
            bulk.delete,
        )
        self.get = to_raw_response_wrapper(
            bulk.get,
        )

    @cached_property
    def cancel(self) -> CancelResourceWithRawResponse:
        return CancelResourceWithRawResponse(self._bulk.cancel)

    @cached_property
    def messages(self) -> MessagesResourceWithRawResponse:
        return MessagesResourceWithRawResponse(self._bulk.messages)


class AsyncBulkResourceWithRawResponse:
    def __init__(self, bulk: AsyncBulkResource) -> None:
        self._bulk = bulk

        self.create = async_to_raw_response_wrapper(
            bulk.create,
        )
        self.list = async_to_raw_response_wrapper(
            bulk.list,
        )
        self.delete = async_to_raw_response_wrapper(
            bulk.delete,
        )
        self.get = async_to_raw_response_wrapper(
            bulk.get,
        )

    @cached_property
    def cancel(self) -> AsyncCancelResourceWithRawResponse:
        return AsyncCancelResourceWithRawResponse(self._bulk.cancel)

    @cached_property
    def messages(self) -> AsyncMessagesResourceWithRawResponse:
        return AsyncMessagesResourceWithRawResponse(self._bulk.messages)


class BulkResourceWithStreamingResponse:
    def __init__(self, bulk: BulkResource) -> None:
        self._bulk = bulk

        self.create = to_streamed_response_wrapper(
            bulk.create,
        )
        self.list = to_streamed_response_wrapper(
            bulk.list,
        )
        self.delete = to_streamed_response_wrapper(
            bulk.delete,
        )
        self.get = to_streamed_response_wrapper(
            bulk.get,
        )

    @cached_property
    def cancel(self) -> CancelResourceWithStreamingResponse:
        return CancelResourceWithStreamingResponse(self._bulk.cancel)

    @cached_property
    def messages(self) -> MessagesResourceWithStreamingResponse:
        return MessagesResourceWithStreamingResponse(self._bulk.messages)


class AsyncBulkResourceWithStreamingResponse:
    def __init__(self, bulk: AsyncBulkResource) -> None:
        self._bulk = bulk

        self.create = async_to_streamed_response_wrapper(
            bulk.create,
        )
        self.list = async_to_streamed_response_wrapper(
            bulk.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            bulk.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            bulk.get,
        )

    @cached_property
    def cancel(self) -> AsyncCancelResourceWithStreamingResponse:
        return AsyncCancelResourceWithStreamingResponse(self._bulk.cancel)

    @cached_property
    def messages(self) -> AsyncMessagesResourceWithStreamingResponse:
        return AsyncMessagesResourceWithStreamingResponse(self._bulk.messages)
