# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import Body, Query, Headers, NotGiven, not_given
from ...._utils import path_template
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....pagination import SyncSinglePage, AsyncSinglePage
from ...._base_client import AsyncPaginator, make_request_options
from ....types.accounts.speed_settings.transformations_config import TransformationsConfig

__all__ = ["TransformationsResource", "AsyncTransformationsResource"]


class TransformationsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TransformationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return TransformationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TransformationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return TransformationsResourceWithStreamingResponse(self)

    def get(
        self,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncSinglePage[TransformationsConfig]:
        """Returns a list of Image Resizing configurations across all zones for the
        account.

        This endpoint is useful for retrieving the transformations
        (image_resizing) state for all zones belonging to an account.

        Args:
          account_id: Identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            path_template("/accounts/{account_id}/settings/transformations", account_id=account_id),
            page=SyncSinglePage[TransformationsConfig],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=TransformationsConfig,
        )


class AsyncTransformationsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTransformationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTransformationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTransformationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncTransformationsResourceWithStreamingResponse(self)

    def get(
        self,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[TransformationsConfig, AsyncSinglePage[TransformationsConfig]]:
        """Returns a list of Image Resizing configurations across all zones for the
        account.

        This endpoint is useful for retrieving the transformations
        (image_resizing) state for all zones belonging to an account.

        Args:
          account_id: Identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            path_template("/accounts/{account_id}/settings/transformations", account_id=account_id),
            page=AsyncSinglePage[TransformationsConfig],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=TransformationsConfig,
        )


class TransformationsResourceWithRawResponse:
    def __init__(self, transformations: TransformationsResource) -> None:
        self._transformations = transformations

        self.get = to_raw_response_wrapper(
            transformations.get,
        )


class AsyncTransformationsResourceWithRawResponse:
    def __init__(self, transformations: AsyncTransformationsResource) -> None:
        self._transformations = transformations

        self.get = async_to_raw_response_wrapper(
            transformations.get,
        )


class TransformationsResourceWithStreamingResponse:
    def __init__(self, transformations: TransformationsResource) -> None:
        self._transformations = transformations

        self.get = to_streamed_response_wrapper(
            transformations.get,
        )


class AsyncTransformationsResourceWithStreamingResponse:
    def __init__(self, transformations: AsyncTransformationsResource) -> None:
        self._transformations = transformations

        self.get = async_to_streamed_response_wrapper(
            transformations.get,
        )
