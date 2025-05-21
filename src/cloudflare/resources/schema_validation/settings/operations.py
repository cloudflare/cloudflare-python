# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Type, Optional, cast
from typing_extensions import Literal

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import maybe_transform, async_maybe_transform
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
from ...._base_client import AsyncPaginator, make_request_options
from ....types.schema_validation.settings import (
    operation_list_params,
    operation_update_params,
    operation_bulk_edit_params,
)
from ....types.schema_validation.settings.operation_get_response import OperationGetResponse
from ....types.schema_validation.settings.operation_list_response import OperationListResponse
from ....types.schema_validation.settings.operation_delete_response import OperationDeleteResponse
from ....types.schema_validation.settings.operation_update_response import OperationUpdateResponse
from ....types.schema_validation.settings.operation_bulk_edit_response import OperationBulkEditResponse

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

    def update(
        self,
        operation_id: str,
        *,
        zone_id: str,
        mitigation_action: Optional[Literal["log", "block", "none"]],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OperationUpdateResponse:
        """
        Update per-operation schema validation setting

        Args:
          zone_id: Identifier.

          operation_id: UUID.

          mitigation_action: When set, this applies a mitigation action to this operation

              - `"log"` - log request when request does not conform to schema for this
                operation
              - `"block"` - deny access to the site when request does not conform to schema
                for this operation
              - `"none"` - will skip mitigation for this operation
              - `null` - clears any mitigation action

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not operation_id:
            raise ValueError(f"Expected a non-empty value for `operation_id` but received {operation_id!r}")
        return self._put(
            f"/zones/{zone_id}/schema_validation/settings/operations/{operation_id}",
            body=maybe_transform(
                {"mitigation_action": mitigation_action}, operation_update_params.OperationUpdateParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[OperationUpdateResponse]._unwrapper,
            ),
            cast_to=cast(Type[OperationUpdateResponse], ResultWrapper[OperationUpdateResponse]),
        )

    def list(
        self,
        *,
        zone_id: str,
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
        List per-operation schema validation settings

        Args:
          zone_id: Identifier.

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
            f"/zones/{zone_id}/schema_validation/settings/operations",
            page=SyncV4PagePaginationArray[OperationListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
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
        Delete per-operation schema validation setting

        Args:
          zone_id: Identifier.

          operation_id: UUID.

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
            f"/zones/{zone_id}/schema_validation/settings/operations/{operation_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[OperationDeleteResponse]._unwrapper,
            ),
            cast_to=cast(Type[OperationDeleteResponse], ResultWrapper[OperationDeleteResponse]),
        )

    def bulk_edit(
        self,
        *,
        zone_id: str,
        body: Dict[str, operation_bulk_edit_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OperationBulkEditResponse:
        """
        Bulk edit per-operation schema validation settings

        Args:
          zone_id: Identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._patch(
            f"/zones/{zone_id}/schema_validation/settings/operations",
            body=maybe_transform(body, operation_bulk_edit_params.OperationBulkEditParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[OperationBulkEditResponse]._unwrapper,
            ),
            cast_to=cast(Type[OperationBulkEditResponse], ResultWrapper[OperationBulkEditResponse]),
        )

    def get(
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
    ) -> OperationGetResponse:
        """
        Get per-operation schema validation setting

        Args:
          zone_id: Identifier.

          operation_id: UUID.

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
            f"/zones/{zone_id}/schema_validation/settings/operations/{operation_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[OperationGetResponse]._unwrapper,
            ),
            cast_to=cast(Type[OperationGetResponse], ResultWrapper[OperationGetResponse]),
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

    async def update(
        self,
        operation_id: str,
        *,
        zone_id: str,
        mitigation_action: Optional[Literal["log", "block", "none"]],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OperationUpdateResponse:
        """
        Update per-operation schema validation setting

        Args:
          zone_id: Identifier.

          operation_id: UUID.

          mitigation_action: When set, this applies a mitigation action to this operation

              - `"log"` - log request when request does not conform to schema for this
                operation
              - `"block"` - deny access to the site when request does not conform to schema
                for this operation
              - `"none"` - will skip mitigation for this operation
              - `null` - clears any mitigation action

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not operation_id:
            raise ValueError(f"Expected a non-empty value for `operation_id` but received {operation_id!r}")
        return await self._put(
            f"/zones/{zone_id}/schema_validation/settings/operations/{operation_id}",
            body=await async_maybe_transform(
                {"mitigation_action": mitigation_action}, operation_update_params.OperationUpdateParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[OperationUpdateResponse]._unwrapper,
            ),
            cast_to=cast(Type[OperationUpdateResponse], ResultWrapper[OperationUpdateResponse]),
        )

    def list(
        self,
        *,
        zone_id: str,
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
        List per-operation schema validation settings

        Args:
          zone_id: Identifier.

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
            f"/zones/{zone_id}/schema_validation/settings/operations",
            page=AsyncV4PagePaginationArray[OperationListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
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
        Delete per-operation schema validation setting

        Args:
          zone_id: Identifier.

          operation_id: UUID.

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
            f"/zones/{zone_id}/schema_validation/settings/operations/{operation_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[OperationDeleteResponse]._unwrapper,
            ),
            cast_to=cast(Type[OperationDeleteResponse], ResultWrapper[OperationDeleteResponse]),
        )

    async def bulk_edit(
        self,
        *,
        zone_id: str,
        body: Dict[str, operation_bulk_edit_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OperationBulkEditResponse:
        """
        Bulk edit per-operation schema validation settings

        Args:
          zone_id: Identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._patch(
            f"/zones/{zone_id}/schema_validation/settings/operations",
            body=await async_maybe_transform(body, operation_bulk_edit_params.OperationBulkEditParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[OperationBulkEditResponse]._unwrapper,
            ),
            cast_to=cast(Type[OperationBulkEditResponse], ResultWrapper[OperationBulkEditResponse]),
        )

    async def get(
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
    ) -> OperationGetResponse:
        """
        Get per-operation schema validation setting

        Args:
          zone_id: Identifier.

          operation_id: UUID.

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
            f"/zones/{zone_id}/schema_validation/settings/operations/{operation_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[OperationGetResponse]._unwrapper,
            ),
            cast_to=cast(Type[OperationGetResponse], ResultWrapper[OperationGetResponse]),
        )


class OperationsResourceWithRawResponse:
    def __init__(self, operations: OperationsResource) -> None:
        self._operations = operations

        self.update = to_raw_response_wrapper(
            operations.update,
        )
        self.list = to_raw_response_wrapper(
            operations.list,
        )
        self.delete = to_raw_response_wrapper(
            operations.delete,
        )
        self.bulk_edit = to_raw_response_wrapper(
            operations.bulk_edit,
        )
        self.get = to_raw_response_wrapper(
            operations.get,
        )


class AsyncOperationsResourceWithRawResponse:
    def __init__(self, operations: AsyncOperationsResource) -> None:
        self._operations = operations

        self.update = async_to_raw_response_wrapper(
            operations.update,
        )
        self.list = async_to_raw_response_wrapper(
            operations.list,
        )
        self.delete = async_to_raw_response_wrapper(
            operations.delete,
        )
        self.bulk_edit = async_to_raw_response_wrapper(
            operations.bulk_edit,
        )
        self.get = async_to_raw_response_wrapper(
            operations.get,
        )


class OperationsResourceWithStreamingResponse:
    def __init__(self, operations: OperationsResource) -> None:
        self._operations = operations

        self.update = to_streamed_response_wrapper(
            operations.update,
        )
        self.list = to_streamed_response_wrapper(
            operations.list,
        )
        self.delete = to_streamed_response_wrapper(
            operations.delete,
        )
        self.bulk_edit = to_streamed_response_wrapper(
            operations.bulk_edit,
        )
        self.get = to_streamed_response_wrapper(
            operations.get,
        )


class AsyncOperationsResourceWithStreamingResponse:
    def __init__(self, operations: AsyncOperationsResource) -> None:
        self._operations = operations

        self.update = async_to_streamed_response_wrapper(
            operations.update,
        )
        self.list = async_to_streamed_response_wrapper(
            operations.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            operations.delete,
        )
        self.bulk_edit = async_to_streamed_response_wrapper(
            operations.bulk_edit,
        )
        self.get = async_to_streamed_response_wrapper(
            operations.get,
        )
