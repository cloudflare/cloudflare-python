# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Optional, cast
from typing_extensions import Literal

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
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
from .direct_uploads import (
    DirectUploadsResource,
    AsyncDirectUploadsResource,
    DirectUploadsResourceWithRawResponse,
    AsyncDirectUploadsResourceWithRawResponse,
    DirectUploadsResourceWithStreamingResponse,
    AsyncDirectUploadsResourceWithStreamingResponse,
)
from ...._base_client import make_request_options
from ....types.images import v2_list_params
from ....types.images.v2_list_response import V2ListResponse

__all__ = ["V2Resource", "AsyncV2Resource"]


class V2Resource(SyncAPIResource):
    @cached_property
    def direct_uploads(self) -> DirectUploadsResource:
        return DirectUploadsResource(self._client)

    @cached_property
    def with_raw_response(self) -> V2ResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return V2ResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> V2ResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return V2ResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        account_id: str,
        continuation_token: Optional[str] | Omit = omit,
        creator: Optional[str] | Omit = omit,
        meta: v2_list_params.Meta | Omit = omit,
        per_page: float | Omit = omit,
        sort_order: Literal["asc", "desc"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V2ListResponse:
        """List up to 10000 images with up to 1000 results per page.

        Use the optional
        parameters below to get a specific range of images. Pagination is supported via
        continuation_token.

        **Metadata Filtering (Optional):**

        You can optionally filter images by custom metadata fields using the
        `meta.<field>[<operator>]=<value>` syntax.

        **Supported Operators:**

        - `eq` / `eq:string` / `eq:number` / `eq:boolean` - Exact match
        - `in` / `in:string` / `in:number` - Match any value in list (pipe-separated)

        **Metadata Filter Constraints:**

        - Maximum 5 metadata filters per request
        - Maximum 5 levels of nesting (e.g., `meta.first.second.third.fourth.fifth`)
        - Maximum 10 elements for list operators (`in`)
        - Supports string, number, and boolean value types

        **Examples:**

        ```
        # List all images
        /v2/images

        # Filter by metadata
        /v2/images?meta.status[eq]=active

        # Filter by nested metadata
        /v2/images?meta.region.name[eq]=eu-west

        # Combine metadata filters with creator
        /v2/images?meta.status[eq]=active&creator=user123

        # Multiple metadata filters (AND logic)
        /v2/images?meta.status[eq]=active&meta.priority[eq:number]=5
        ```

        Args:
          account_id: Account identifier tag.

          continuation_token: Continuation token to fetch next page. Passed as a query param when requesting
              List V2 api endpoint.

          creator: Internal user ID set within the creator field. Setting to empty string "" will
              return images where creator field is not set

          per_page: Number of items per page

          sort_order: Sorting order by upload time

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
                        "creator": creator,
                        "meta": meta,
                        "per_page": per_page,
                        "sort_order": sort_order,
                    },
                    v2_list_params.V2ListParams,
                ),
                post_parser=ResultWrapper[V2ListResponse]._unwrapper,
            ),
            cast_to=cast(Type[V2ListResponse], ResultWrapper[V2ListResponse]),
        )


class AsyncV2Resource(AsyncAPIResource):
    @cached_property
    def direct_uploads(self) -> AsyncDirectUploadsResource:
        return AsyncDirectUploadsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncV2ResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncV2ResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncV2ResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncV2ResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        account_id: str,
        continuation_token: Optional[str] | Omit = omit,
        creator: Optional[str] | Omit = omit,
        meta: v2_list_params.Meta | Omit = omit,
        per_page: float | Omit = omit,
        sort_order: Literal["asc", "desc"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V2ListResponse:
        """List up to 10000 images with up to 1000 results per page.

        Use the optional
        parameters below to get a specific range of images. Pagination is supported via
        continuation_token.

        **Metadata Filtering (Optional):**

        You can optionally filter images by custom metadata fields using the
        `meta.<field>[<operator>]=<value>` syntax.

        **Supported Operators:**

        - `eq` / `eq:string` / `eq:number` / `eq:boolean` - Exact match
        - `in` / `in:string` / `in:number` - Match any value in list (pipe-separated)

        **Metadata Filter Constraints:**

        - Maximum 5 metadata filters per request
        - Maximum 5 levels of nesting (e.g., `meta.first.second.third.fourth.fifth`)
        - Maximum 10 elements for list operators (`in`)
        - Supports string, number, and boolean value types

        **Examples:**

        ```
        # List all images
        /v2/images

        # Filter by metadata
        /v2/images?meta.status[eq]=active

        # Filter by nested metadata
        /v2/images?meta.region.name[eq]=eu-west

        # Combine metadata filters with creator
        /v2/images?meta.status[eq]=active&creator=user123

        # Multiple metadata filters (AND logic)
        /v2/images?meta.status[eq]=active&meta.priority[eq:number]=5
        ```

        Args:
          account_id: Account identifier tag.

          continuation_token: Continuation token to fetch next page. Passed as a query param when requesting
              List V2 api endpoint.

          creator: Internal user ID set within the creator field. Setting to empty string "" will
              return images where creator field is not set

          per_page: Number of items per page

          sort_order: Sorting order by upload time

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
                        "creator": creator,
                        "meta": meta,
                        "per_page": per_page,
                        "sort_order": sort_order,
                    },
                    v2_list_params.V2ListParams,
                ),
                post_parser=ResultWrapper[V2ListResponse]._unwrapper,
            ),
            cast_to=cast(Type[V2ListResponse], ResultWrapper[V2ListResponse]),
        )


class V2ResourceWithRawResponse:
    def __init__(self, v2: V2Resource) -> None:
        self._v2 = v2

        self.list = to_raw_response_wrapper(
            v2.list,
        )

    @cached_property
    def direct_uploads(self) -> DirectUploadsResourceWithRawResponse:
        return DirectUploadsResourceWithRawResponse(self._v2.direct_uploads)


class AsyncV2ResourceWithRawResponse:
    def __init__(self, v2: AsyncV2Resource) -> None:
        self._v2 = v2

        self.list = async_to_raw_response_wrapper(
            v2.list,
        )

    @cached_property
    def direct_uploads(self) -> AsyncDirectUploadsResourceWithRawResponse:
        return AsyncDirectUploadsResourceWithRawResponse(self._v2.direct_uploads)


class V2ResourceWithStreamingResponse:
    def __init__(self, v2: V2Resource) -> None:
        self._v2 = v2

        self.list = to_streamed_response_wrapper(
            v2.list,
        )

    @cached_property
    def direct_uploads(self) -> DirectUploadsResourceWithStreamingResponse:
        return DirectUploadsResourceWithStreamingResponse(self._v2.direct_uploads)


class AsyncV2ResourceWithStreamingResponse:
    def __init__(self, v2: AsyncV2Resource) -> None:
        self._v2 = v2

        self.list = async_to_streamed_response_wrapper(
            v2.list,
        )

    @cached_property
    def direct_uploads(self) -> AsyncDirectUploadsResourceWithStreamingResponse:
        return AsyncDirectUploadsResourceWithStreamingResponse(self._v2.direct_uploads)
