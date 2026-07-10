# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Optional, cast

import httpx

from ...._types import Body, Query, Headers, NotGiven, not_given
from ...._utils import path_template, maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._wrappers import ResultWrapper
from ...._base_client import make_request_options
from ....types.email_auth.spf import inspect_get_params
from ....types.email_auth.spf.inspect_get_response import InspectGetResponse

__all__ = ["InspectResource", "AsyncInspectResource"]


class InspectResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> InspectResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return InspectResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> InspectResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return InspectResourceWithStreamingResponse(self)

    def get(
        self,
        *,
        zone_id: str,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[InspectGetResponse]:
        """
        Inspects a specific SPF TXT record and returns a parsed tree structure in the
        spflimit-worker format.

        The record ID must be provided via the `id` query parameter.

        Returns a recursive tree showing:

        - Parsed components with their qualifiers and types
        - Nested includes recursively resolved within components
        - Per-component and total lookup counts
        - Detailed error information with context

        Args:
          zone_id: Identifier.

          id: DNS record ID (rec_tag) to inspect

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._get(
            path_template("/zones/{zone_id}/email/auth/spf/inspect", zone_id=zone_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"id": id}, inspect_get_params.InspectGetParams),
                post_parser=ResultWrapper[Optional[InspectGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[InspectGetResponse]], ResultWrapper[InspectGetResponse]),
        )


class AsyncInspectResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncInspectResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncInspectResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncInspectResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncInspectResourceWithStreamingResponse(self)

    async def get(
        self,
        *,
        zone_id: str,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[InspectGetResponse]:
        """
        Inspects a specific SPF TXT record and returns a parsed tree structure in the
        spflimit-worker format.

        The record ID must be provided via the `id` query parameter.

        Returns a recursive tree showing:

        - Parsed components with their qualifiers and types
        - Nested includes recursively resolved within components
        - Per-component and total lookup counts
        - Detailed error information with context

        Args:
          zone_id: Identifier.

          id: DNS record ID (rec_tag) to inspect

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._get(
            path_template("/zones/{zone_id}/email/auth/spf/inspect", zone_id=zone_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"id": id}, inspect_get_params.InspectGetParams),
                post_parser=ResultWrapper[Optional[InspectGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[InspectGetResponse]], ResultWrapper[InspectGetResponse]),
        )


class InspectResourceWithRawResponse:
    def __init__(self, inspect: InspectResource) -> None:
        self._inspect = inspect

        self.get = to_raw_response_wrapper(
            inspect.get,
        )


class AsyncInspectResourceWithRawResponse:
    def __init__(self, inspect: AsyncInspectResource) -> None:
        self._inspect = inspect

        self.get = async_to_raw_response_wrapper(
            inspect.get,
        )


class InspectResourceWithStreamingResponse:
    def __init__(self, inspect: InspectResource) -> None:
        self._inspect = inspect

        self.get = to_streamed_response_wrapper(
            inspect.get,
        )


class AsyncInspectResourceWithStreamingResponse:
    def __init__(self, inspect: AsyncInspectResource) -> None:
        self._inspect = inspect

        self.get = async_to_streamed_response_wrapper(
            inspect.get,
        )
