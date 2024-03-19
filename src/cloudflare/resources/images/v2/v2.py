# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Optional, cast
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
from .direct_uploads import (
    DirectUploads,
    AsyncDirectUploads,
    DirectUploadsWithRawResponse,
    AsyncDirectUploadsWithRawResponse,
    DirectUploadsWithStreamingResponse,
    AsyncDirectUploadsWithStreamingResponse,
)
from ...._base_client import (
    make_request_options,
)
from ....types.images import V2ListResponse, v2_list_params

__all__ = ["V2", "AsyncV2"]


class V2(SyncAPIResource):
    @cached_property
    def direct_uploads(self) -> DirectUploads:
        return DirectUploads(self._client)

    @cached_property
    def with_raw_response(self) -> V2WithRawResponse:
        return V2WithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> V2WithStreamingResponse:
        return V2WithStreamingResponse(self)

    def list(
        self,
        *,
        account_id: str,
        continuation_token: Optional[str] | NotGiven = NOT_GIVEN,
        per_page: float | NotGiven = NOT_GIVEN,
        sort_order: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> V2ListResponse:
        """List up to 10000 images with one request.

        Use the optional parameters below to
        get a specific range of images. Endpoint returns continuation_token if more
        images are present.

        Args:
          account_id: Account identifier tag.

          continuation_token: Continuation token for a next page. List images V2 returns continuation_token

          per_page: Number of items per page.

          sort_order: Sorting order by upload time.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get(
            f"/accounts/{account_id}/images/v2",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "continuation_token": continuation_token,
                        "per_page": per_page,
                        "sort_order": sort_order,
                    },
                    v2_list_params.V2ListParams,
                ),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[V2ListResponse], ResultWrapper[V2ListResponse]),
        )


class AsyncV2(AsyncAPIResource):
    @cached_property
    def direct_uploads(self) -> AsyncDirectUploads:
        return AsyncDirectUploads(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncV2WithRawResponse:
        return AsyncV2WithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncV2WithStreamingResponse:
        return AsyncV2WithStreamingResponse(self)

    async def list(
        self,
        *,
        account_id: str,
        continuation_token: Optional[str] | NotGiven = NOT_GIVEN,
        per_page: float | NotGiven = NOT_GIVEN,
        sort_order: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> V2ListResponse:
        """List up to 10000 images with one request.

        Use the optional parameters below to
        get a specific range of images. Endpoint returns continuation_token if more
        images are present.

        Args:
          account_id: Account identifier tag.

          continuation_token: Continuation token for a next page. List images V2 returns continuation_token

          per_page: Number of items per page.

          sort_order: Sorting order by upload time.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._get(
            f"/accounts/{account_id}/images/v2",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "continuation_token": continuation_token,
                        "per_page": per_page,
                        "sort_order": sort_order,
                    },
                    v2_list_params.V2ListParams,
                ),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[V2ListResponse], ResultWrapper[V2ListResponse]),
        )


class V2WithRawResponse:
    def __init__(self, v2: V2) -> None:
        self._v2 = v2

        self.list = to_raw_response_wrapper(
            v2.list,
        )

    @cached_property
    def direct_uploads(self) -> DirectUploadsWithRawResponse:
        return DirectUploadsWithRawResponse(self._v2.direct_uploads)


class AsyncV2WithRawResponse:
    def __init__(self, v2: AsyncV2) -> None:
        self._v2 = v2

        self.list = async_to_raw_response_wrapper(
            v2.list,
        )

    @cached_property
    def direct_uploads(self) -> AsyncDirectUploadsWithRawResponse:
        return AsyncDirectUploadsWithRawResponse(self._v2.direct_uploads)


class V2WithStreamingResponse:
    def __init__(self, v2: V2) -> None:
        self._v2 = v2

        self.list = to_streamed_response_wrapper(
            v2.list,
        )

    @cached_property
    def direct_uploads(self) -> DirectUploadsWithStreamingResponse:
        return DirectUploadsWithStreamingResponse(self._v2.direct_uploads)


class AsyncV2WithStreamingResponse:
    def __init__(self, v2: AsyncV2) -> None:
        self._v2 = v2

        self.list = async_to_streamed_response_wrapper(
            v2.list,
        )

    @cached_property
    def direct_uploads(self) -> AsyncDirectUploadsWithStreamingResponse:
        return AsyncDirectUploadsWithStreamingResponse(self._v2.direct_uploads)
