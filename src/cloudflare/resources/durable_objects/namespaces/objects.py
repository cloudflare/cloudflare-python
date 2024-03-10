# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....pagination import SyncCursorLimitPagination, AsyncCursorLimitPagination
from ...._base_client import (
    AsyncPaginator,
    make_request_options,
)
from ....types.durable_objects.namespaces import WorkersObject, object_list_params

__all__ = ["Objects", "AsyncObjects"]


class Objects(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ObjectsWithRawResponse:
        return ObjectsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ObjectsWithStreamingResponse:
        return ObjectsWithStreamingResponse(self)

    def list(
        self,
        id: str,
        *,
        account_id: str,
        cursor: str | NotGiven = NOT_GIVEN,
        limit: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncCursorLimitPagination[WorkersObject]:
        """
        Returns the Durable Objects in a given namespace.

        Args:
          account_id: Identifier

          id: ID of the namespace.

          cursor: Opaque token indicating the position from which to continue when requesting the
              next set of records. A valid value for the cursor can be obtained from the
              cursors object in the result_info structure.

          limit: The number of objects to return. The cursor attribute may be used to iterate
              over the next batch of objects if there are more than the limit.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/workers/durable_objects/namespaces/{id}/objects",
            page=SyncCursorLimitPagination[WorkersObject],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "limit": limit,
                    },
                    object_list_params.ObjectListParams,
                ),
            ),
            model=WorkersObject,
        )


class AsyncObjects(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncObjectsWithRawResponse:
        return AsyncObjectsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncObjectsWithStreamingResponse:
        return AsyncObjectsWithStreamingResponse(self)

    def list(
        self,
        id: str,
        *,
        account_id: str,
        cursor: str | NotGiven = NOT_GIVEN,
        limit: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[WorkersObject, AsyncCursorLimitPagination[WorkersObject]]:
        """
        Returns the Durable Objects in a given namespace.

        Args:
          account_id: Identifier

          id: ID of the namespace.

          cursor: Opaque token indicating the position from which to continue when requesting the
              next set of records. A valid value for the cursor can be obtained from the
              cursors object in the result_info structure.

          limit: The number of objects to return. The cursor attribute may be used to iterate
              over the next batch of objects if there are more than the limit.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/workers/durable_objects/namespaces/{id}/objects",
            page=AsyncCursorLimitPagination[WorkersObject],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "limit": limit,
                    },
                    object_list_params.ObjectListParams,
                ),
            ),
            model=WorkersObject,
        )


class ObjectsWithRawResponse:
    def __init__(self, objects: Objects) -> None:
        self._objects = objects

        self.list = to_raw_response_wrapper(
            objects.list,
        )


class AsyncObjectsWithRawResponse:
    def __init__(self, objects: AsyncObjects) -> None:
        self._objects = objects

        self.list = async_to_raw_response_wrapper(
            objects.list,
        )


class ObjectsWithStreamingResponse:
    def __init__(self, objects: Objects) -> None:
        self._objects = objects

        self.list = to_streamed_response_wrapper(
            objects.list,
        )


class AsyncObjectsWithStreamingResponse:
    def __init__(self, objects: AsyncObjects) -> None:
        self._objects = objects

        self.list = async_to_streamed_response_wrapper(
            objects.list,
        )
