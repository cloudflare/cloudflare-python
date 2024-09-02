# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._compat import cached_property

from ....types.api_gateway.discovery_operation import DiscoveryOperation

from ....pagination import SyncV4PagePaginationArray, AsyncV4PagePaginationArray

from ...._utils import maybe_transform, async_maybe_transform

from ...._base_client import make_request_options, AsyncPaginator

from typing_extensions import Literal

from typing import List, Type

from ....types.api_gateway.discovery.operation_edit_response import OperationEditResponse

from ...._wrappers import ResultWrapper

from ...._response import (
    to_raw_response_wrapper,
    async_to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_streamed_response_wrapper,
)

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ...._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ...._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ...._resource import SyncAPIResource, AsyncAPIResource
from ....types import shared_params
from ....types.api_gateway.discovery import operation_list_params
from ....types.api_gateway.discovery import operation_edit_params
from typing import cast
from typing import cast

__all__ = ["OperationsResource", "AsyncOperationsResource"]


class OperationsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> OperationsResourceWithRawResponse:
        return OperationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OperationsResourceWithStreamingResponse:
        return OperationsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        zone_id: str,
        diff: bool | NotGiven = NOT_GIVEN,
        direction: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
        endpoint: str | NotGiven = NOT_GIVEN,
        host: List[str] | NotGiven = NOT_GIVEN,
        method: List[str] | NotGiven = NOT_GIVEN,
        order: Literal["host", "method", "endpoint", "traffic_stats.requests", "traffic_stats.last_updated"]
        | NotGiven = NOT_GIVEN,
        origin: Literal["ML", "SessionIdentifier"] | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        state: Literal["review", "saved", "ignored"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncV4PagePaginationArray[DiscoveryOperation]:
        """
        Retrieve the most up to date view of discovered operations

        Args:
          zone_id: Identifier

          diff: When `true`, only return API Discovery results that are not saved into API
              Shield Endpoint Management

          direction: Direction to order results.

          endpoint: Filter results to only include endpoints containing this pattern.

          host: Filter results to only include the specified hosts.

          method: Filter results to only include the specified HTTP methods.

          order: Field to order by

          origin: Filter results to only include discovery results sourced from a particular
              discovery engine

              - `ML` - Discovered operations that were sourced using ML API Discovery
              - `SessionIdentifier` - Discovered operations that were sourced using Session
                Identifier API Discovery

          page: Page number of paginated results.

          per_page: Maximum number of results per page.

          state: Filter results to only include discovery results in a particular state. States
              are as follows

              - `review` - Discovered operations that are not saved into API Shield Endpoint
                Management
              - `saved` - Discovered operations that are already saved into API Shield
                Endpoint Management
              - `ignored` - Discovered operations that have been marked as ignored

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._get_api_list(
            f"/zones/{zone_id}/api_gateway/discovery/operations",
            page=SyncV4PagePaginationArray[DiscoveryOperation],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "diff": diff,
                        "direction": direction,
                        "endpoint": endpoint,
                        "host": host,
                        "method": method,
                        "order": order,
                        "origin": origin,
                        "page": page,
                        "per_page": per_page,
                        "state": state,
                    },
                    operation_list_params.OperationListParams,
                ),
            ),
            model=DiscoveryOperation,
        )

    def edit(
        self,
        operation_id: str,
        *,
        zone_id: str,
        state: Literal["review", "ignored"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OperationEditResponse:
        """
        Update the `state` on a discovered operation

        Args:
          zone_id: Identifier

          operation_id: UUID

          state: Mark state of operation in API Discovery

              - `review` - Mark operation as for review
              - `ignored` - Mark operation as ignored

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not operation_id:
            raise ValueError(f"Expected a non-empty value for `operation_id` but received {operation_id!r}")
        return self._patch(
            f"/zones/{zone_id}/api_gateway/discovery/operations/{operation_id}",
            body=maybe_transform({"state": state}, operation_edit_params.OperationEditParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[OperationEditResponse]._unwrapper,
            ),
            cast_to=cast(Type[OperationEditResponse], ResultWrapper[OperationEditResponse]),
        )


class AsyncOperationsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncOperationsResourceWithRawResponse:
        return AsyncOperationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOperationsResourceWithStreamingResponse:
        return AsyncOperationsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        zone_id: str,
        diff: bool | NotGiven = NOT_GIVEN,
        direction: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
        endpoint: str | NotGiven = NOT_GIVEN,
        host: List[str] | NotGiven = NOT_GIVEN,
        method: List[str] | NotGiven = NOT_GIVEN,
        order: Literal["host", "method", "endpoint", "traffic_stats.requests", "traffic_stats.last_updated"]
        | NotGiven = NOT_GIVEN,
        origin: Literal["ML", "SessionIdentifier"] | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        state: Literal["review", "saved", "ignored"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[DiscoveryOperation, AsyncV4PagePaginationArray[DiscoveryOperation]]:
        """
        Retrieve the most up to date view of discovered operations

        Args:
          zone_id: Identifier

          diff: When `true`, only return API Discovery results that are not saved into API
              Shield Endpoint Management

          direction: Direction to order results.

          endpoint: Filter results to only include endpoints containing this pattern.

          host: Filter results to only include the specified hosts.

          method: Filter results to only include the specified HTTP methods.

          order: Field to order by

          origin: Filter results to only include discovery results sourced from a particular
              discovery engine

              - `ML` - Discovered operations that were sourced using ML API Discovery
              - `SessionIdentifier` - Discovered operations that were sourced using Session
                Identifier API Discovery

          page: Page number of paginated results.

          per_page: Maximum number of results per page.

          state: Filter results to only include discovery results in a particular state. States
              are as follows

              - `review` - Discovered operations that are not saved into API Shield Endpoint
                Management
              - `saved` - Discovered operations that are already saved into API Shield
                Endpoint Management
              - `ignored` - Discovered operations that have been marked as ignored

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._get_api_list(
            f"/zones/{zone_id}/api_gateway/discovery/operations",
            page=AsyncV4PagePaginationArray[DiscoveryOperation],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "diff": diff,
                        "direction": direction,
                        "endpoint": endpoint,
                        "host": host,
                        "method": method,
                        "order": order,
                        "origin": origin,
                        "page": page,
                        "per_page": per_page,
                        "state": state,
                    },
                    operation_list_params.OperationListParams,
                ),
            ),
            model=DiscoveryOperation,
        )

    async def edit(
        self,
        operation_id: str,
        *,
        zone_id: str,
        state: Literal["review", "ignored"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OperationEditResponse:
        """
        Update the `state` on a discovered operation

        Args:
          zone_id: Identifier

          operation_id: UUID

          state: Mark state of operation in API Discovery

              - `review` - Mark operation as for review
              - `ignored` - Mark operation as ignored

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not operation_id:
            raise ValueError(f"Expected a non-empty value for `operation_id` but received {operation_id!r}")
        return await self._patch(
            f"/zones/{zone_id}/api_gateway/discovery/operations/{operation_id}",
            body=await async_maybe_transform({"state": state}, operation_edit_params.OperationEditParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[OperationEditResponse]._unwrapper,
            ),
            cast_to=cast(Type[OperationEditResponse], ResultWrapper[OperationEditResponse]),
        )


class OperationsResourceWithRawResponse:
    def __init__(self, operations: OperationsResource) -> None:
        self._operations = operations

        self.list = to_raw_response_wrapper(
            operations.list,
        )
        self.edit = to_raw_response_wrapper(
            operations.edit,
        )


class AsyncOperationsResourceWithRawResponse:
    def __init__(self, operations: AsyncOperationsResource) -> None:
        self._operations = operations

        self.list = async_to_raw_response_wrapper(
            operations.list,
        )
        self.edit = async_to_raw_response_wrapper(
            operations.edit,
        )


class OperationsResourceWithStreamingResponse:
    def __init__(self, operations: OperationsResource) -> None:
        self._operations = operations

        self.list = to_streamed_response_wrapper(
            operations.list,
        )
        self.edit = to_streamed_response_wrapper(
            operations.edit,
        )


class AsyncOperationsResourceWithStreamingResponse:
    def __init__(self, operations: AsyncOperationsResource) -> None:
        self._operations = operations

        self.list = async_to_streamed_response_wrapper(
            operations.list,
        )
        self.edit = async_to_streamed_response_wrapper(
            operations.edit,
        )
