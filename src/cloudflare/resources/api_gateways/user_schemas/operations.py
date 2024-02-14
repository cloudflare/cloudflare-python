# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List, Type, Optional, cast
from typing_extensions import Literal

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
from ...._wrappers import ResultWrapper
from ...._base_client import (
    make_request_options,
)
from ....types.api_gateways.user_schemas import OperationListResponse, operation_list_params

__all__ = ["Operations", "AsyncOperations"]


class Operations(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> OperationsWithRawResponse:
        return OperationsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OperationsWithStreamingResponse:
        return OperationsWithStreamingResponse(self)

    def list(
        self,
        schema_id: str,
        *,
        zone_id: str,
        endpoint: str | NotGiven = NOT_GIVEN,
        feature: List[Literal["thresholds", "parameter_schemas", "schema_info"]] | NotGiven = NOT_GIVEN,
        host: List[str] | NotGiven = NOT_GIVEN,
        method: List[str] | NotGiven = NOT_GIVEN,
        operation_status: Literal["new", "existing"] | NotGiven = NOT_GIVEN,
        page: object | NotGiven = NOT_GIVEN,
        per_page: object | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[OperationListResponse]:
        """Retrieves all operations from the schema.

        Operations that already exist in API
        Shield Endpoint Management will be returned as full operations.

        Args:
          zone_id: Identifier

          endpoint: Filter results to only include endpoints containing this pattern.

          feature: Add feature(s) to the results. The feature name that is given here corresponds
              to the resulting feature object. Have a look at the top-level object description
              for more details on the specific meaning.

          host: Filter results to only include the specified hosts.

          method: Filter results to only include the specified HTTP methods.

          operation_status: Filter results by whether operations exist in API Shield Endpoint Management or
              not. `new` will just return operations from the schema that do not exist in API
              Shield Endpoint Management. `existing` will just return operations from the
              schema that already exist in API Shield Endpoint Management.

          page: Page number of paginated results.

          per_page: Maximum number of results per page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not schema_id:
            raise ValueError(f"Expected a non-empty value for `schema_id` but received {schema_id!r}")
        return self._get(
            f"/zones/{zone_id}/api_gateway/user_schemas/{schema_id}/operations",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "endpoint": endpoint,
                        "feature": feature,
                        "host": host,
                        "method": method,
                        "operation_status": operation_status,
                        "page": page,
                        "per_page": per_page,
                    },
                    operation_list_params.OperationListParams,
                ),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[OperationListResponse]], ResultWrapper[OperationListResponse]),
        )


class AsyncOperations(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncOperationsWithRawResponse:
        return AsyncOperationsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOperationsWithStreamingResponse:
        return AsyncOperationsWithStreamingResponse(self)

    async def list(
        self,
        schema_id: str,
        *,
        zone_id: str,
        endpoint: str | NotGiven = NOT_GIVEN,
        feature: List[Literal["thresholds", "parameter_schemas", "schema_info"]] | NotGiven = NOT_GIVEN,
        host: List[str] | NotGiven = NOT_GIVEN,
        method: List[str] | NotGiven = NOT_GIVEN,
        operation_status: Literal["new", "existing"] | NotGiven = NOT_GIVEN,
        page: object | NotGiven = NOT_GIVEN,
        per_page: object | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[OperationListResponse]:
        """Retrieves all operations from the schema.

        Operations that already exist in API
        Shield Endpoint Management will be returned as full operations.

        Args:
          zone_id: Identifier

          endpoint: Filter results to only include endpoints containing this pattern.

          feature: Add feature(s) to the results. The feature name that is given here corresponds
              to the resulting feature object. Have a look at the top-level object description
              for more details on the specific meaning.

          host: Filter results to only include the specified hosts.

          method: Filter results to only include the specified HTTP methods.

          operation_status: Filter results by whether operations exist in API Shield Endpoint Management or
              not. `new` will just return operations from the schema that do not exist in API
              Shield Endpoint Management. `existing` will just return operations from the
              schema that already exist in API Shield Endpoint Management.

          page: Page number of paginated results.

          per_page: Maximum number of results per page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not schema_id:
            raise ValueError(f"Expected a non-empty value for `schema_id` but received {schema_id!r}")
        return await self._get(
            f"/zones/{zone_id}/api_gateway/user_schemas/{schema_id}/operations",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "endpoint": endpoint,
                        "feature": feature,
                        "host": host,
                        "method": method,
                        "operation_status": operation_status,
                        "page": page,
                        "per_page": per_page,
                    },
                    operation_list_params.OperationListParams,
                ),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[OperationListResponse]], ResultWrapper[OperationListResponse]),
        )


class OperationsWithRawResponse:
    def __init__(self, operations: Operations) -> None:
        self._operations = operations

        self.list = to_raw_response_wrapper(
            operations.list,
        )


class AsyncOperationsWithRawResponse:
    def __init__(self, operations: AsyncOperations) -> None:
        self._operations = operations

        self.list = async_to_raw_response_wrapper(
            operations.list,
        )


class OperationsWithStreamingResponse:
    def __init__(self, operations: Operations) -> None:
        self._operations = operations

        self.list = to_streamed_response_wrapper(
            operations.list,
        )


class AsyncOperationsWithStreamingResponse:
    def __init__(self, operations: AsyncOperations) -> None:
        self._operations = operations

        self.list = async_to_streamed_response_wrapper(
            operations.list,
        )
