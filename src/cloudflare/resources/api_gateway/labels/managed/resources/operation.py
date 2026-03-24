# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, cast

import httpx

from ......_types import Body, Query, Headers, NotGiven, not_given
from ......_utils import maybe_transform, async_maybe_transform
from ......_compat import cached_property
from ......_resource import SyncAPIResource, AsyncAPIResource
from ......_response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ......_wrappers import ResultWrapper
from ......_base_client import make_request_options
from ......types.api_gateway.labels.managed.resources import operation_update_params
from ......types.api_gateway.labels.managed.resources.operation_update_response import OperationUpdateResponse

__all__ = ["OperationResource", "AsyncOperationResource"]


class OperationResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> OperationResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return OperationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OperationResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return OperationResourceWithStreamingResponse(self)

    def update(
        self,
        name: str,
        *,
        zone_id: str,
        selector: operation_update_params.Selector,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OperationUpdateResponse:
        """
        Replace all operations(s) attached to a managed label

        Args:
          zone_id: Identifier.

          name: The name of the label

          selector: Operation IDs selector

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not name:
            raise ValueError(f"Expected a non-empty value for `name` but received {name!r}")
        return self._put(
            f"/zones/{zone_id}/api_gateway/labels/managed/{name}/resources/operation",
            body=maybe_transform({"selector": selector}, operation_update_params.OperationUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[OperationUpdateResponse]._unwrapper,
            ),
            cast_to=cast(Type[OperationUpdateResponse], ResultWrapper[OperationUpdateResponse]),
        )


class AsyncOperationResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncOperationResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncOperationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOperationResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncOperationResourceWithStreamingResponse(self)

    async def update(
        self,
        name: str,
        *,
        zone_id: str,
        selector: operation_update_params.Selector,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OperationUpdateResponse:
        """
        Replace all operations(s) attached to a managed label

        Args:
          zone_id: Identifier.

          name: The name of the label

          selector: Operation IDs selector

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not name:
            raise ValueError(f"Expected a non-empty value for `name` but received {name!r}")
        return await self._put(
            f"/zones/{zone_id}/api_gateway/labels/managed/{name}/resources/operation",
            body=await async_maybe_transform({"selector": selector}, operation_update_params.OperationUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[OperationUpdateResponse]._unwrapper,
            ),
            cast_to=cast(Type[OperationUpdateResponse], ResultWrapper[OperationUpdateResponse]),
        )


class OperationResourceWithRawResponse:
    def __init__(self, operation: OperationResource) -> None:
        self._operation = operation

        self.update = to_raw_response_wrapper(
            operation.update,
        )


class AsyncOperationResourceWithRawResponse:
    def __init__(self, operation: AsyncOperationResource) -> None:
        self._operation = operation

        self.update = async_to_raw_response_wrapper(
            operation.update,
        )


class OperationResourceWithStreamingResponse:
    def __init__(self, operation: OperationResource) -> None:
        self._operation = operation

        self.update = to_streamed_response_wrapper(
            operation.update,
        )


class AsyncOperationResourceWithStreamingResponse:
    def __init__(self, operation: AsyncOperationResource) -> None:
        self._operation = operation

        self.update = async_to_streamed_response_wrapper(
            operation.update,
        )
