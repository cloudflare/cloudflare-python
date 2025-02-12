# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Type, Iterable, cast
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
from ....pagination import SyncSinglePage, AsyncSinglePage, SyncV4PagePaginationArray, AsyncV4PagePaginationArray
from ...._base_client import AsyncPaginator, make_request_options
from .schema_validation import (
    SchemaValidationResource,
    AsyncSchemaValidationResource,
    SchemaValidationResourceWithRawResponse,
    AsyncSchemaValidationResourceWithRawResponse,
    SchemaValidationResourceWithStreamingResponse,
    AsyncSchemaValidationResourceWithStreamingResponse,
)
from ....types.api_gateway import (
    operation_get_params,
    operation_list_params,
    operation_create_params,
    operation_bulk_create_params,
)
from ....types.api_gateway.operation_get_response import OperationGetResponse
from ....types.api_gateway.operation_list_response import OperationListResponse
from ....types.api_gateway.operation_create_response import OperationCreateResponse
from ....types.api_gateway.operation_delete_response import OperationDeleteResponse
from ....types.api_gateway.operation_bulk_create_response import OperationBulkCreateResponse
from ....types.api_gateway.operation_bulk_delete_response import OperationBulkDeleteResponse

__all__ = ["OperationsResource", "AsyncOperationsResource"]


class OperationsResource(SyncAPIResource):
    @cached_property
    def schema_validation(self) -> SchemaValidationResource:
        return SchemaValidationResource(self._client)

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

    def create(
        self,
        *,
        zone_id: str,
        endpoint: str,
        host: str,
        method: Literal["GET", "POST", "HEAD", "OPTIONS", "PUT", "DELETE", "CONNECT", "PATCH", "TRACE"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OperationCreateResponse:
        """Add one operation to a zone.

        Endpoints can contain path variables. Host, method,
        endpoint will be normalized to a canoncial form when creating an operation and
        must be unique on the zone. Inserting an operation that matches an existing one
        will return the record of the already existing operation and update its
        last_updated date.

        Args:
          zone_id: Identifier

          endpoint: The endpoint which can contain path parameter templates in curly braces, each
              will be replaced from left to right with {varN}, starting with {var1}, during
              insertion. This will further be Cloudflare-normalized upon insertion. See:
              https://developers.cloudflare.com/rules/normalization/how-it-works/.

          host: RFC3986-compliant host.

          method: The HTTP method used to access the endpoint.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._post(
            f"/zones/{zone_id}/api_gateway/operations/item",
            body=maybe_transform(
                {
                    "endpoint": endpoint,
                    "host": host,
                    "method": method,
                },
                operation_create_params.OperationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[OperationCreateResponse]._unwrapper,
            ),
            cast_to=cast(Type[OperationCreateResponse], ResultWrapper[OperationCreateResponse]),
        )

    def list(
        self,
        *,
        zone_id: str,
        direction: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
        endpoint: str | NotGiven = NOT_GIVEN,
        feature: List[Literal["thresholds", "parameter_schemas", "schema_info"]] | NotGiven = NOT_GIVEN,
        host: List[str] | NotGiven = NOT_GIVEN,
        method: List[str] | NotGiven = NOT_GIVEN,
        order: Literal["method", "host", "endpoint", "thresholds.$key"] | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncV4PagePaginationArray[OperationListResponse]:
        """
        Retrieve information about all operations on a zone

        Args:
          zone_id: Identifier

          direction: Direction to order results.

          endpoint: Filter results to only include endpoints containing this pattern.

          feature: Add feature(s) to the results. The feature name that is given here corresponds
              to the resulting feature object. Have a look at the top-level object description
              for more details on the specific meaning.

          host: Filter results to only include the specified hosts.

          method: Filter results to only include the specified HTTP methods.

          order: Field to order by. When requesting a feature, the feature keys are available for
              ordering as well, e.g., `thresholds.suggested_threshold`.

          page: Page number of paginated results.

          per_page: Maximum number of results per page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._get_api_list(
            f"/zones/{zone_id}/api_gateway/operations",
            page=SyncV4PagePaginationArray[OperationListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "direction": direction,
                        "endpoint": endpoint,
                        "feature": feature,
                        "host": host,
                        "method": method,
                        "order": order,
                        "page": page,
                        "per_page": per_page,
                    },
                    operation_list_params.OperationListParams,
                ),
            ),
            model=OperationListResponse,
        )

    def delete(
        self,
        operation_id: str,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OperationDeleteResponse:
        """
        Delete an operation

        Args:
          zone_id: Identifier

          operation_id: UUID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not operation_id:
            raise ValueError(f"Expected a non-empty value for `operation_id` but received {operation_id!r}")
        return self._delete(
            f"/zones/{zone_id}/api_gateway/operations/{operation_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OperationDeleteResponse,
        )

    def bulk_create(
        self,
        *,
        zone_id: str,
        body: Iterable[operation_bulk_create_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncSinglePage[OperationBulkCreateResponse]:
        """Add one or more operations to a zone.

        Endpoints can contain path variables.
        Host, method, endpoint will be normalized to a canoncial form when creating an
        operation and must be unique on the zone. Inserting an operation that matches an
        existing one will return the record of the already existing operation and update
        its last_updated date.

        Args:
          zone_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._get_api_list(
            f"/zones/{zone_id}/api_gateway/operations",
            page=SyncSinglePage[OperationBulkCreateResponse],
            body=maybe_transform(body, Iterable[operation_bulk_create_params.Body]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=OperationBulkCreateResponse,
            method="post",
        )

    def bulk_delete(
        self,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OperationBulkDeleteResponse:
        """
        Delete multiple operations

        Args:
          zone_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._delete(
            f"/zones/{zone_id}/api_gateway/operations",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OperationBulkDeleteResponse,
        )

    def get(
        self,
        operation_id: str,
        *,
        zone_id: str,
        feature: List[Literal["thresholds", "parameter_schemas", "schema_info"]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OperationGetResponse:
        """
        Retrieve information about an operation

        Args:
          zone_id: Identifier

          operation_id: UUID

          feature: Add feature(s) to the results. The feature name that is given here corresponds
              to the resulting feature object. Have a look at the top-level object description
              for more details on the specific meaning.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not operation_id:
            raise ValueError(f"Expected a non-empty value for `operation_id` but received {operation_id!r}")
        return self._get(
            f"/zones/{zone_id}/api_gateway/operations/{operation_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"feature": feature}, operation_get_params.OperationGetParams),
                post_parser=ResultWrapper[OperationGetResponse]._unwrapper,
            ),
            cast_to=cast(Type[OperationGetResponse], ResultWrapper[OperationGetResponse]),
        )


class AsyncOperationsResource(AsyncAPIResource):
    @cached_property
    def schema_validation(self) -> AsyncSchemaValidationResource:
        return AsyncSchemaValidationResource(self._client)

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

    async def create(
        self,
        *,
        zone_id: str,
        endpoint: str,
        host: str,
        method: Literal["GET", "POST", "HEAD", "OPTIONS", "PUT", "DELETE", "CONNECT", "PATCH", "TRACE"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OperationCreateResponse:
        """Add one operation to a zone.

        Endpoints can contain path variables. Host, method,
        endpoint will be normalized to a canoncial form when creating an operation and
        must be unique on the zone. Inserting an operation that matches an existing one
        will return the record of the already existing operation and update its
        last_updated date.

        Args:
          zone_id: Identifier

          endpoint: The endpoint which can contain path parameter templates in curly braces, each
              will be replaced from left to right with {varN}, starting with {var1}, during
              insertion. This will further be Cloudflare-normalized upon insertion. See:
              https://developers.cloudflare.com/rules/normalization/how-it-works/.

          host: RFC3986-compliant host.

          method: The HTTP method used to access the endpoint.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._post(
            f"/zones/{zone_id}/api_gateway/operations/item",
            body=await async_maybe_transform(
                {
                    "endpoint": endpoint,
                    "host": host,
                    "method": method,
                },
                operation_create_params.OperationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[OperationCreateResponse]._unwrapper,
            ),
            cast_to=cast(Type[OperationCreateResponse], ResultWrapper[OperationCreateResponse]),
        )

    def list(
        self,
        *,
        zone_id: str,
        direction: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
        endpoint: str | NotGiven = NOT_GIVEN,
        feature: List[Literal["thresholds", "parameter_schemas", "schema_info"]] | NotGiven = NOT_GIVEN,
        host: List[str] | NotGiven = NOT_GIVEN,
        method: List[str] | NotGiven = NOT_GIVEN,
        order: Literal["method", "host", "endpoint", "thresholds.$key"] | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[OperationListResponse, AsyncV4PagePaginationArray[OperationListResponse]]:
        """
        Retrieve information about all operations on a zone

        Args:
          zone_id: Identifier

          direction: Direction to order results.

          endpoint: Filter results to only include endpoints containing this pattern.

          feature: Add feature(s) to the results. The feature name that is given here corresponds
              to the resulting feature object. Have a look at the top-level object description
              for more details on the specific meaning.

          host: Filter results to only include the specified hosts.

          method: Filter results to only include the specified HTTP methods.

          order: Field to order by. When requesting a feature, the feature keys are available for
              ordering as well, e.g., `thresholds.suggested_threshold`.

          page: Page number of paginated results.

          per_page: Maximum number of results per page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._get_api_list(
            f"/zones/{zone_id}/api_gateway/operations",
            page=AsyncV4PagePaginationArray[OperationListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "direction": direction,
                        "endpoint": endpoint,
                        "feature": feature,
                        "host": host,
                        "method": method,
                        "order": order,
                        "page": page,
                        "per_page": per_page,
                    },
                    operation_list_params.OperationListParams,
                ),
            ),
            model=OperationListResponse,
        )

    async def delete(
        self,
        operation_id: str,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OperationDeleteResponse:
        """
        Delete an operation

        Args:
          zone_id: Identifier

          operation_id: UUID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not operation_id:
            raise ValueError(f"Expected a non-empty value for `operation_id` but received {operation_id!r}")
        return await self._delete(
            f"/zones/{zone_id}/api_gateway/operations/{operation_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OperationDeleteResponse,
        )

    def bulk_create(
        self,
        *,
        zone_id: str,
        body: Iterable[operation_bulk_create_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[OperationBulkCreateResponse, AsyncSinglePage[OperationBulkCreateResponse]]:
        """Add one or more operations to a zone.

        Endpoints can contain path variables.
        Host, method, endpoint will be normalized to a canoncial form when creating an
        operation and must be unique on the zone. Inserting an operation that matches an
        existing one will return the record of the already existing operation and update
        its last_updated date.

        Args:
          zone_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._get_api_list(
            f"/zones/{zone_id}/api_gateway/operations",
            page=AsyncSinglePage[OperationBulkCreateResponse],
            body=maybe_transform(body, Iterable[operation_bulk_create_params.Body]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=OperationBulkCreateResponse,
            method="post",
        )

    async def bulk_delete(
        self,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OperationBulkDeleteResponse:
        """
        Delete multiple operations

        Args:
          zone_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._delete(
            f"/zones/{zone_id}/api_gateway/operations",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OperationBulkDeleteResponse,
        )

    async def get(
        self,
        operation_id: str,
        *,
        zone_id: str,
        feature: List[Literal["thresholds", "parameter_schemas", "schema_info"]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OperationGetResponse:
        """
        Retrieve information about an operation

        Args:
          zone_id: Identifier

          operation_id: UUID

          feature: Add feature(s) to the results. The feature name that is given here corresponds
              to the resulting feature object. Have a look at the top-level object description
              for more details on the specific meaning.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not operation_id:
            raise ValueError(f"Expected a non-empty value for `operation_id` but received {operation_id!r}")
        return await self._get(
            f"/zones/{zone_id}/api_gateway/operations/{operation_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"feature": feature}, operation_get_params.OperationGetParams),
                post_parser=ResultWrapper[OperationGetResponse]._unwrapper,
            ),
            cast_to=cast(Type[OperationGetResponse], ResultWrapper[OperationGetResponse]),
        )


class OperationsResourceWithRawResponse:
    def __init__(self, operations: OperationsResource) -> None:
        self._operations = operations

        self.create = to_raw_response_wrapper(
            operations.create,
        )
        self.list = to_raw_response_wrapper(
            operations.list,
        )
        self.delete = to_raw_response_wrapper(
            operations.delete,
        )
        self.bulk_create = to_raw_response_wrapper(
            operations.bulk_create,
        )
        self.bulk_delete = to_raw_response_wrapper(
            operations.bulk_delete,
        )
        self.get = to_raw_response_wrapper(
            operations.get,
        )

    @cached_property
    def schema_validation(self) -> SchemaValidationResourceWithRawResponse:
        return SchemaValidationResourceWithRawResponse(self._operations.schema_validation)


class AsyncOperationsResourceWithRawResponse:
    def __init__(self, operations: AsyncOperationsResource) -> None:
        self._operations = operations

        self.create = async_to_raw_response_wrapper(
            operations.create,
        )
        self.list = async_to_raw_response_wrapper(
            operations.list,
        )
        self.delete = async_to_raw_response_wrapper(
            operations.delete,
        )
        self.bulk_create = async_to_raw_response_wrapper(
            operations.bulk_create,
        )
        self.bulk_delete = async_to_raw_response_wrapper(
            operations.bulk_delete,
        )
        self.get = async_to_raw_response_wrapper(
            operations.get,
        )

    @cached_property
    def schema_validation(self) -> AsyncSchemaValidationResourceWithRawResponse:
        return AsyncSchemaValidationResourceWithRawResponse(self._operations.schema_validation)


class OperationsResourceWithStreamingResponse:
    def __init__(self, operations: OperationsResource) -> None:
        self._operations = operations

        self.create = to_streamed_response_wrapper(
            operations.create,
        )
        self.list = to_streamed_response_wrapper(
            operations.list,
        )
        self.delete = to_streamed_response_wrapper(
            operations.delete,
        )
        self.bulk_create = to_streamed_response_wrapper(
            operations.bulk_create,
        )
        self.bulk_delete = to_streamed_response_wrapper(
            operations.bulk_delete,
        )
        self.get = to_streamed_response_wrapper(
            operations.get,
        )

    @cached_property
    def schema_validation(self) -> SchemaValidationResourceWithStreamingResponse:
        return SchemaValidationResourceWithStreamingResponse(self._operations.schema_validation)


class AsyncOperationsResourceWithStreamingResponse:
    def __init__(self, operations: AsyncOperationsResource) -> None:
        self._operations = operations

        self.create = async_to_streamed_response_wrapper(
            operations.create,
        )
        self.list = async_to_streamed_response_wrapper(
            operations.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            operations.delete,
        )
        self.bulk_create = async_to_streamed_response_wrapper(
            operations.bulk_create,
        )
        self.bulk_delete = async_to_streamed_response_wrapper(
            operations.bulk_delete,
        )
        self.get = async_to_streamed_response_wrapper(
            operations.get,
        )

    @cached_property
    def schema_validation(self) -> AsyncSchemaValidationResourceWithStreamingResponse:
        return AsyncSchemaValidationResourceWithStreamingResponse(self._operations.schema_validation)
