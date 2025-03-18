# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, cast

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._wrappers import ResultWrapper
from ...types.zaraz import publish_create_params
from ..._base_client import make_request_options
from ...types.zaraz.publish_create_response import PublishCreateResponse

__all__ = ["PublishResource", "AsyncPublishResource"]


class PublishResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PublishResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return PublishResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PublishResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return PublishResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        zone_id: str,
        body: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> str:
        """
        Publish current Zaraz preview configuration for a zone.

        Args:
          zone_id: Identifier

          body: Zaraz configuration description.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._post(
            f"/zones/{zone_id}/settings/zaraz/publish",
            body=maybe_transform(body, publish_create_params.PublishCreateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[PublishCreateResponse]._unwrapper,
            ),
            cast_to=cast(Type[str], ResultWrapper[str]),
        )


class AsyncPublishResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPublishResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPublishResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPublishResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncPublishResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        zone_id: str,
        body: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> str:
        """
        Publish current Zaraz preview configuration for a zone.

        Args:
          zone_id: Identifier

          body: Zaraz configuration description.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._post(
            f"/zones/{zone_id}/settings/zaraz/publish",
            body=await async_maybe_transform(body, publish_create_params.PublishCreateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[PublishCreateResponse]._unwrapper,
            ),
            cast_to=cast(Type[str], ResultWrapper[str]),
        )


class PublishResourceWithRawResponse:
    def __init__(self, publish: PublishResource) -> None:
        self._publish = publish

        self.create = to_raw_response_wrapper(
            publish.create,
        )


class AsyncPublishResourceWithRawResponse:
    def __init__(self, publish: AsyncPublishResource) -> None:
        self._publish = publish

        self.create = async_to_raw_response_wrapper(
            publish.create,
        )


class PublishResourceWithStreamingResponse:
    def __init__(self, publish: PublishResource) -> None:
        self._publish = publish

        self.create = to_streamed_response_wrapper(
            publish.create,
        )


class AsyncPublishResourceWithStreamingResponse:
    def __init__(self, publish: AsyncPublishResource) -> None:
        self._publish = publish

        self.create = async_to_streamed_response_wrapper(
            publish.create,
        )
