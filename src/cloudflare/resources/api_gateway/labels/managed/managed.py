# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, cast

import httpx

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
from ....._base_client import make_request_options
from .resources.resources import (
    ResourcesResource,
    AsyncResourcesResource,
    ResourcesResourceWithRawResponse,
    AsyncResourcesResourceWithRawResponse,
    ResourcesResourceWithStreamingResponse,
    AsyncResourcesResourceWithStreamingResponse,
)
from .....types.api_gateway.labels import managed_get_params
from .....types.api_gateway.labels.managed_get_response import ManagedGetResponse

__all__ = ["ManagedResource", "AsyncManagedResource"]


class ManagedResource(SyncAPIResource):
    @cached_property
    def resources(self) -> ResourcesResource:
        return ResourcesResource(self._client)

    @cached_property
    def with_raw_response(self) -> ManagedResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return ManagedResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ManagedResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return ManagedResourceWithStreamingResponse(self)

    def get(
        self,
        name: str,
        *,
        zone_id: str | None = None,
        with_mapped_resource_counts: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ManagedGetResponse:
        """
        Retrieve managed label

        Args:
          zone_id: Identifier.

          name: The name of the label

          with_mapped_resource_counts: Include `mapped_resources` for each label

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if zone_id is None:
            zone_id = self._client._get_zone_id_path_param()
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not name:
            raise ValueError(f"Expected a non-empty value for `name` but received {name!r}")
        return self._get(
            path_template("/zones/{zone_id}/api_gateway/labels/managed/{name}", zone_id=zone_id, name=name),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"with_mapped_resource_counts": with_mapped_resource_counts}, managed_get_params.ManagedGetParams
                ),
                post_parser=ResultWrapper[ManagedGetResponse]._unwrapper,
            ),
            cast_to=cast(Type[ManagedGetResponse], ResultWrapper[ManagedGetResponse]),
        )


class AsyncManagedResource(AsyncAPIResource):
    @cached_property
    def resources(self) -> AsyncResourcesResource:
        return AsyncResourcesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncManagedResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncManagedResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncManagedResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncManagedResourceWithStreamingResponse(self)

    async def get(
        self,
        name: str,
        *,
        zone_id: str | None = None,
        with_mapped_resource_counts: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ManagedGetResponse:
        """
        Retrieve managed label

        Args:
          zone_id: Identifier.

          name: The name of the label

          with_mapped_resource_counts: Include `mapped_resources` for each label

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if zone_id is None:
            zone_id = self._client._get_zone_id_path_param()
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not name:
            raise ValueError(f"Expected a non-empty value for `name` but received {name!r}")
        return await self._get(
            path_template("/zones/{zone_id}/api_gateway/labels/managed/{name}", zone_id=zone_id, name=name),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"with_mapped_resource_counts": with_mapped_resource_counts}, managed_get_params.ManagedGetParams
                ),
                post_parser=ResultWrapper[ManagedGetResponse]._unwrapper,
            ),
            cast_to=cast(Type[ManagedGetResponse], ResultWrapper[ManagedGetResponse]),
        )


class ManagedResourceWithRawResponse:
    def __init__(self, managed: ManagedResource) -> None:
        self._managed = managed

        self.get = to_raw_response_wrapper(
            managed.get,
        )

    @cached_property
    def resources(self) -> ResourcesResourceWithRawResponse:
        return ResourcesResourceWithRawResponse(self._managed.resources)


class AsyncManagedResourceWithRawResponse:
    def __init__(self, managed: AsyncManagedResource) -> None:
        self._managed = managed

        self.get = async_to_raw_response_wrapper(
            managed.get,
        )

    @cached_property
    def resources(self) -> AsyncResourcesResourceWithRawResponse:
        return AsyncResourcesResourceWithRawResponse(self._managed.resources)


class ManagedResourceWithStreamingResponse:
    def __init__(self, managed: ManagedResource) -> None:
        self._managed = managed

        self.get = to_streamed_response_wrapper(
            managed.get,
        )

    @cached_property
    def resources(self) -> ResourcesResourceWithStreamingResponse:
        return ResourcesResourceWithStreamingResponse(self._managed.resources)


class AsyncManagedResourceWithStreamingResponse:
    def __init__(self, managed: AsyncManagedResource) -> None:
        self._managed = managed

        self.get = async_to_streamed_response_wrapper(
            managed.get,
        )

    @cached_property
    def resources(self) -> AsyncResourcesResourceWithStreamingResponse:
        return AsyncResourcesResourceWithStreamingResponse(self._managed.resources)
