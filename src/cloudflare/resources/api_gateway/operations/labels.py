# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, cast

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
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
from ....pagination import SyncSinglePage, AsyncSinglePage
from ...._base_client import AsyncPaginator, make_request_options
from ....types.api_gateway.operations import (
    label_create_params,
    label_update_params,
    label_bulk_create_params,
    label_bulk_update_params,
)
from ....types.api_gateway.operations.label_create_response import LabelCreateResponse
from ....types.api_gateway.operations.label_delete_response import LabelDeleteResponse
from ....types.api_gateway.operations.label_update_response import LabelUpdateResponse
from ....types.api_gateway.operations.label_bulk_create_response import LabelBulkCreateResponse
from ....types.api_gateway.operations.label_bulk_delete_response import LabelBulkDeleteResponse
from ....types.api_gateway.operations.label_bulk_update_response import LabelBulkUpdateResponse

__all__ = ["LabelsResource", "AsyncLabelsResource"]


class LabelsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> LabelsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return LabelsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LabelsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return LabelsResourceWithStreamingResponse(self)

    def create(
        self,
        operation_id: str,
        *,
        zone_id: str,
        managed: SequenceNotStr[str] | Omit = omit,
        user: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LabelCreateResponse:
        """
        Attach label(s) on an operation in endpoint management

        Args:
          zone_id: Identifier.

          operation_id: UUID.

          managed: List of managed label names.

          user: List of user label names.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not operation_id:
            raise ValueError(f"Expected a non-empty value for `operation_id` but received {operation_id!r}")
        return self._post(
            f"/zones/{zone_id}/api_gateway/operations/{operation_id}/labels",
            body=maybe_transform(
                {
                    "managed": managed,
                    "user": user,
                },
                label_create_params.LabelCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[LabelCreateResponse]._unwrapper,
            ),
            cast_to=cast(Type[LabelCreateResponse], ResultWrapper[LabelCreateResponse]),
        )

    def update(
        self,
        operation_id: str,
        *,
        zone_id: str,
        managed: SequenceNotStr[str] | Omit = omit,
        user: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LabelUpdateResponse:
        """
        Replace label(s) on an operation in endpoint management

        Args:
          zone_id: Identifier.

          operation_id: UUID.

          managed: List of managed label names. Omitting this property or passing an empty array
              will result in all managed labels being removed from the operation

          user: List of user label names. Omitting this property or passing an empty array will
              result in all user labels being removed from the operation

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
            f"/zones/{zone_id}/api_gateway/operations/{operation_id}/labels",
            body=maybe_transform(
                {
                    "managed": managed,
                    "user": user,
                },
                label_update_params.LabelUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[LabelUpdateResponse]._unwrapper,
            ),
            cast_to=cast(Type[LabelUpdateResponse], ResultWrapper[LabelUpdateResponse]),
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LabelDeleteResponse:
        """
        Remove label(s) on an operation in endpoint management

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
            f"/zones/{zone_id}/api_gateway/operations/{operation_id}/labels",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[LabelDeleteResponse]._unwrapper,
            ),
            cast_to=cast(Type[LabelDeleteResponse], ResultWrapper[LabelDeleteResponse]),
        )

    def bulk_create(
        self,
        *,
        zone_id: str,
        selector: label_bulk_create_params.Selector,
        managed: label_bulk_create_params.Managed | Omit = omit,
        user: label_bulk_create_params.User | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncSinglePage[LabelBulkCreateResponse]:
        """
        Bulk attach label(s) on operation(s) in endpoint management

        Args:
          zone_id: Identifier.

          selector: Operation IDs selector

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._get_api_list(
            f"/zones/{zone_id}/api_gateway/operations/labels",
            page=SyncSinglePage[LabelBulkCreateResponse],
            body=maybe_transform(
                {
                    "selector": selector,
                    "managed": managed,
                    "user": user,
                },
                label_bulk_create_params.LabelBulkCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=LabelBulkCreateResponse,
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncSinglePage[LabelBulkDeleteResponse]:
        """
        Bulk remove label(s) on operation(s) in endpoint management

        Args:
          zone_id: Identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._get_api_list(
            f"/zones/{zone_id}/api_gateway/operations/labels",
            page=SyncSinglePage[LabelBulkDeleteResponse],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=LabelBulkDeleteResponse,
            method="delete",
        )

    def bulk_update(
        self,
        *,
        zone_id: str,
        managed: label_bulk_update_params.Managed,
        selector: label_bulk_update_params.Selector,
        user: label_bulk_update_params.User,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncSinglePage[LabelBulkUpdateResponse]:
        """
        Bulk replace label(s) on operation(s) in endpoint management

        Args:
          zone_id: Identifier.

          managed: Managed labels to replace for all affected operations

          selector: Operation IDs selector

          user: User labels to replace for all affected operations

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._get_api_list(
            f"/zones/{zone_id}/api_gateway/operations/labels",
            page=SyncSinglePage[LabelBulkUpdateResponse],
            body=maybe_transform(
                {
                    "managed": managed,
                    "selector": selector,
                    "user": user,
                },
                label_bulk_update_params.LabelBulkUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=LabelBulkUpdateResponse,
            method="put",
        )


class AsyncLabelsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncLabelsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncLabelsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLabelsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncLabelsResourceWithStreamingResponse(self)

    async def create(
        self,
        operation_id: str,
        *,
        zone_id: str,
        managed: SequenceNotStr[str] | Omit = omit,
        user: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LabelCreateResponse:
        """
        Attach label(s) on an operation in endpoint management

        Args:
          zone_id: Identifier.

          operation_id: UUID.

          managed: List of managed label names.

          user: List of user label names.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not operation_id:
            raise ValueError(f"Expected a non-empty value for `operation_id` but received {operation_id!r}")
        return await self._post(
            f"/zones/{zone_id}/api_gateway/operations/{operation_id}/labels",
            body=await async_maybe_transform(
                {
                    "managed": managed,
                    "user": user,
                },
                label_create_params.LabelCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[LabelCreateResponse]._unwrapper,
            ),
            cast_to=cast(Type[LabelCreateResponse], ResultWrapper[LabelCreateResponse]),
        )

    async def update(
        self,
        operation_id: str,
        *,
        zone_id: str,
        managed: SequenceNotStr[str] | Omit = omit,
        user: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LabelUpdateResponse:
        """
        Replace label(s) on an operation in endpoint management

        Args:
          zone_id: Identifier.

          operation_id: UUID.

          managed: List of managed label names. Omitting this property or passing an empty array
              will result in all managed labels being removed from the operation

          user: List of user label names. Omitting this property or passing an empty array will
              result in all user labels being removed from the operation

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
            f"/zones/{zone_id}/api_gateway/operations/{operation_id}/labels",
            body=await async_maybe_transform(
                {
                    "managed": managed,
                    "user": user,
                },
                label_update_params.LabelUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[LabelUpdateResponse]._unwrapper,
            ),
            cast_to=cast(Type[LabelUpdateResponse], ResultWrapper[LabelUpdateResponse]),
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LabelDeleteResponse:
        """
        Remove label(s) on an operation in endpoint management

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
            f"/zones/{zone_id}/api_gateway/operations/{operation_id}/labels",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[LabelDeleteResponse]._unwrapper,
            ),
            cast_to=cast(Type[LabelDeleteResponse], ResultWrapper[LabelDeleteResponse]),
        )

    def bulk_create(
        self,
        *,
        zone_id: str,
        selector: label_bulk_create_params.Selector,
        managed: label_bulk_create_params.Managed | Omit = omit,
        user: label_bulk_create_params.User | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[LabelBulkCreateResponse, AsyncSinglePage[LabelBulkCreateResponse]]:
        """
        Bulk attach label(s) on operation(s) in endpoint management

        Args:
          zone_id: Identifier.

          selector: Operation IDs selector

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._get_api_list(
            f"/zones/{zone_id}/api_gateway/operations/labels",
            page=AsyncSinglePage[LabelBulkCreateResponse],
            body=maybe_transform(
                {
                    "selector": selector,
                    "managed": managed,
                    "user": user,
                },
                label_bulk_create_params.LabelBulkCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=LabelBulkCreateResponse,
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[LabelBulkDeleteResponse, AsyncSinglePage[LabelBulkDeleteResponse]]:
        """
        Bulk remove label(s) on operation(s) in endpoint management

        Args:
          zone_id: Identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._get_api_list(
            f"/zones/{zone_id}/api_gateway/operations/labels",
            page=AsyncSinglePage[LabelBulkDeleteResponse],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=LabelBulkDeleteResponse,
            method="delete",
        )

    def bulk_update(
        self,
        *,
        zone_id: str,
        managed: label_bulk_update_params.Managed,
        selector: label_bulk_update_params.Selector,
        user: label_bulk_update_params.User,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[LabelBulkUpdateResponse, AsyncSinglePage[LabelBulkUpdateResponse]]:
        """
        Bulk replace label(s) on operation(s) in endpoint management

        Args:
          zone_id: Identifier.

          managed: Managed labels to replace for all affected operations

          selector: Operation IDs selector

          user: User labels to replace for all affected operations

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._get_api_list(
            f"/zones/{zone_id}/api_gateway/operations/labels",
            page=AsyncSinglePage[LabelBulkUpdateResponse],
            body=maybe_transform(
                {
                    "managed": managed,
                    "selector": selector,
                    "user": user,
                },
                label_bulk_update_params.LabelBulkUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=LabelBulkUpdateResponse,
            method="put",
        )


class LabelsResourceWithRawResponse:
    def __init__(self, labels: LabelsResource) -> None:
        self._labels = labels

        self.create = to_raw_response_wrapper(
            labels.create,
        )
        self.update = to_raw_response_wrapper(
            labels.update,
        )
        self.delete = to_raw_response_wrapper(
            labels.delete,
        )
        self.bulk_create = to_raw_response_wrapper(
            labels.bulk_create,
        )
        self.bulk_delete = to_raw_response_wrapper(
            labels.bulk_delete,
        )
        self.bulk_update = to_raw_response_wrapper(
            labels.bulk_update,
        )


class AsyncLabelsResourceWithRawResponse:
    def __init__(self, labels: AsyncLabelsResource) -> None:
        self._labels = labels

        self.create = async_to_raw_response_wrapper(
            labels.create,
        )
        self.update = async_to_raw_response_wrapper(
            labels.update,
        )
        self.delete = async_to_raw_response_wrapper(
            labels.delete,
        )
        self.bulk_create = async_to_raw_response_wrapper(
            labels.bulk_create,
        )
        self.bulk_delete = async_to_raw_response_wrapper(
            labels.bulk_delete,
        )
        self.bulk_update = async_to_raw_response_wrapper(
            labels.bulk_update,
        )


class LabelsResourceWithStreamingResponse:
    def __init__(self, labels: LabelsResource) -> None:
        self._labels = labels

        self.create = to_streamed_response_wrapper(
            labels.create,
        )
        self.update = to_streamed_response_wrapper(
            labels.update,
        )
        self.delete = to_streamed_response_wrapper(
            labels.delete,
        )
        self.bulk_create = to_streamed_response_wrapper(
            labels.bulk_create,
        )
        self.bulk_delete = to_streamed_response_wrapper(
            labels.bulk_delete,
        )
        self.bulk_update = to_streamed_response_wrapper(
            labels.bulk_update,
        )


class AsyncLabelsResourceWithStreamingResponse:
    def __init__(self, labels: AsyncLabelsResource) -> None:
        self._labels = labels

        self.create = async_to_streamed_response_wrapper(
            labels.create,
        )
        self.update = async_to_streamed_response_wrapper(
            labels.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            labels.delete,
        )
        self.bulk_create = async_to_streamed_response_wrapper(
            labels.bulk_create,
        )
        self.bulk_delete = async_to_streamed_response_wrapper(
            labels.bulk_delete,
        )
        self.bulk_update = async_to_streamed_response_wrapper(
            labels.bulk_update,
        )
