# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Iterable, cast

import httpx

from .._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
from .._utils import (
    maybe_transform,
    async_maybe_transform,
)
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._wrappers import ResultWrapper
from .._base_client import make_request_options
from ..types.managed_transforms import managed_transform_edit_params
from ..types.managed_transforms.managed_transform_edit_response import ManagedTransformEditResponse
from ..types.managed_transforms.managed_transform_list_response import ManagedTransformListResponse

__all__ = ["ManagedTransformsResource", "AsyncManagedTransformsResource"]


class ManagedTransformsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ManagedTransformsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return ManagedTransformsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ManagedTransformsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return ManagedTransformsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ManagedTransformListResponse:
        """
        Fetches a list of all Managed Transforms.

        Args:
          zone_id: The unique ID of the zone.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._get(
            f"/zones/{zone_id}/managed_headers",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[ManagedTransformListResponse]._unwrapper,
            ),
            cast_to=cast(Type[ManagedTransformListResponse], ResultWrapper[ManagedTransformListResponse]),
        )

    def delete(
        self,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Disables all Managed Transforms.

        Args:
          zone_id: The unique ID of the zone.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/zones/{zone_id}/managed_headers",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def edit(
        self,
        *,
        zone_id: str,
        managed_request_headers: Iterable[managed_transform_edit_params.ManagedRequestHeader],
        managed_response_headers: Iterable[managed_transform_edit_params.ManagedResponseHeader],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ManagedTransformEditResponse:
        """
        Updates the status of one or more Managed Transforms.

        Args:
          zone_id: The unique ID of the zone.

          managed_request_headers: The list of Managed Request Transforms.

          managed_response_headers: The list of Managed Response Transforms.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._patch(
            f"/zones/{zone_id}/managed_headers",
            body=maybe_transform(
                {
                    "managed_request_headers": managed_request_headers,
                    "managed_response_headers": managed_response_headers,
                },
                managed_transform_edit_params.ManagedTransformEditParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[ManagedTransformEditResponse]._unwrapper,
            ),
            cast_to=cast(Type[ManagedTransformEditResponse], ResultWrapper[ManagedTransformEditResponse]),
        )


class AsyncManagedTransformsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncManagedTransformsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncManagedTransformsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncManagedTransformsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncManagedTransformsResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ManagedTransformListResponse:
        """
        Fetches a list of all Managed Transforms.

        Args:
          zone_id: The unique ID of the zone.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._get(
            f"/zones/{zone_id}/managed_headers",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[ManagedTransformListResponse]._unwrapper,
            ),
            cast_to=cast(Type[ManagedTransformListResponse], ResultWrapper[ManagedTransformListResponse]),
        )

    async def delete(
        self,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Disables all Managed Transforms.

        Args:
          zone_id: The unique ID of the zone.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/zones/{zone_id}/managed_headers",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def edit(
        self,
        *,
        zone_id: str,
        managed_request_headers: Iterable[managed_transform_edit_params.ManagedRequestHeader],
        managed_response_headers: Iterable[managed_transform_edit_params.ManagedResponseHeader],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ManagedTransformEditResponse:
        """
        Updates the status of one or more Managed Transforms.

        Args:
          zone_id: The unique ID of the zone.

          managed_request_headers: The list of Managed Request Transforms.

          managed_response_headers: The list of Managed Response Transforms.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._patch(
            f"/zones/{zone_id}/managed_headers",
            body=await async_maybe_transform(
                {
                    "managed_request_headers": managed_request_headers,
                    "managed_response_headers": managed_response_headers,
                },
                managed_transform_edit_params.ManagedTransformEditParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[ManagedTransformEditResponse]._unwrapper,
            ),
            cast_to=cast(Type[ManagedTransformEditResponse], ResultWrapper[ManagedTransformEditResponse]),
        )


class ManagedTransformsResourceWithRawResponse:
    def __init__(self, managed_transforms: ManagedTransformsResource) -> None:
        self._managed_transforms = managed_transforms

        self.list = to_raw_response_wrapper(
            managed_transforms.list,
        )
        self.delete = to_raw_response_wrapper(
            managed_transforms.delete,
        )
        self.edit = to_raw_response_wrapper(
            managed_transforms.edit,
        )


class AsyncManagedTransformsResourceWithRawResponse:
    def __init__(self, managed_transforms: AsyncManagedTransformsResource) -> None:
        self._managed_transforms = managed_transforms

        self.list = async_to_raw_response_wrapper(
            managed_transforms.list,
        )
        self.delete = async_to_raw_response_wrapper(
            managed_transforms.delete,
        )
        self.edit = async_to_raw_response_wrapper(
            managed_transforms.edit,
        )


class ManagedTransformsResourceWithStreamingResponse:
    def __init__(self, managed_transforms: ManagedTransformsResource) -> None:
        self._managed_transforms = managed_transforms

        self.list = to_streamed_response_wrapper(
            managed_transforms.list,
        )
        self.delete = to_streamed_response_wrapper(
            managed_transforms.delete,
        )
        self.edit = to_streamed_response_wrapper(
            managed_transforms.edit,
        )


class AsyncManagedTransformsResourceWithStreamingResponse:
    def __init__(self, managed_transforms: AsyncManagedTransformsResource) -> None:
        self._managed_transforms = managed_transforms

        self.list = async_to_streamed_response_wrapper(
            managed_transforms.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            managed_transforms.delete,
        )
        self.edit = async_to_streamed_response_wrapper(
            managed_transforms.edit,
        )
