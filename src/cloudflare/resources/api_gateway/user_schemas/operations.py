# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import typing_extensions
from typing import Any, List, cast
from typing_extensions import Literal

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ...._utils import maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....pagination import SyncV4PagePaginationArray, AsyncV4PagePaginationArray
from ...._base_client import AsyncPaginator, make_request_options
from ....types.api_gateway.user_schemas import operation_list_params
from ....types.api_gateway.user_schemas.operation_list_response import OperationListResponse

__all__ = ["OperationsResource", "AsyncOperationsResource"]


class OperationsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> OperationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return OperationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OperationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return OperationsResourceWithStreamingResponse(self)

    @typing_extensions.deprecated(
        "Use [Schema Validation API](https://developers.cloudflare.com/api/resources/schema_validation/) instead."
    )
    def list(
        self,
        schema_id: str,
        *,
        zone_id: str,
        endpoint: str | Omit = omit,
        feature: List[Literal["thresholds", "parameter_schemas", "schema_info"]] | Omit = omit,
        host: SequenceNotStr[str] | Omit = omit,
        method: SequenceNotStr[str] | Omit = omit,
        operation_status: Literal["new", "existing"] | Omit = omit,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncV4PagePaginationArray[OperationListResponse]:
        """Retrieves all operations from the schema.

        Operations that already exist in API
        Shield Endpoint Management will be returned as full operations.

        Args:
          zone_id: Identifier.

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
        return self._get_api_list(
            f"/zones/{zone_id}/api_gateway/user_schemas/{schema_id}/operations",
            page=SyncV4PagePaginationArray[OperationListResponse],
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
            ),
            model=cast(Any, OperationListResponse),  # Union types cannot be passed in as arguments in the type system
        )


class AsyncOperationsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncOperationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncOperationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOperationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncOperationsResourceWithStreamingResponse(self)

    @typing_extensions.deprecated(
        "Use [Schema Validation API](https://developers.cloudflare.com/api/resources/schema_validation/) instead."
    )
    def list(
        self,
        schema_id: str,
        *,
        zone_id: str,
        endpoint: str | Omit = omit,
        feature: List[Literal["thresholds", "parameter_schemas", "schema_info"]] | Omit = omit,
        host: SequenceNotStr[str] | Omit = omit,
        method: SequenceNotStr[str] | Omit = omit,
        operation_status: Literal["new", "existing"] | Omit = omit,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[OperationListResponse, AsyncV4PagePaginationArray[OperationListResponse]]:
        """Retrieves all operations from the schema.

        Operations that already exist in API
        Shield Endpoint Management will be returned as full operations.

        Args:
          zone_id: Identifier.

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
        return self._get_api_list(
            f"/zones/{zone_id}/api_gateway/user_schemas/{schema_id}/operations",
            page=AsyncV4PagePaginationArray[OperationListResponse],
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
            ),
            model=cast(Any, OperationListResponse),  # Union types cannot be passed in as arguments in the type system
        )


class OperationsResourceWithRawResponse:
    def __init__(self, operations: OperationsResource) -> None:
        self._operations = operations

        self.list = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                operations.list,  # pyright: ignore[reportDeprecated],
            )
        )


class AsyncOperationsResourceWithRawResponse:
    def __init__(self, operations: AsyncOperationsResource) -> None:
        self._operations = operations

        self.list = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                operations.list,  # pyright: ignore[reportDeprecated],
            )
        )


class OperationsResourceWithStreamingResponse:
    def __init__(self, operations: OperationsResource) -> None:
        self._operations = operations

        self.list = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                operations.list,  # pyright: ignore[reportDeprecated],
            )
        )


class AsyncOperationsResourceWithStreamingResponse:
    def __init__(self, operations: AsyncOperationsResource) -> None:
        self._operations = operations

        self.list = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                operations.list,  # pyright: ignore[reportDeprecated],
            )
        )
