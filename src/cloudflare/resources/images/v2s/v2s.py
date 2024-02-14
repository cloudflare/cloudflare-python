# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from .direct_uploads import DirectUploads, AsyncDirectUploads

from ...._compat import cached_property

from ....types.images import V2ListResponse

from typing import Type, Optional

from typing_extensions import Literal

from ...._response import (
    to_raw_response_wrapper,
    async_to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_streamed_response_wrapper,
)

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ...._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ...._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._base_client import (
    SyncAPIClient,
    AsyncAPIClient,
    _merge_mappings,
    AsyncPaginator,
    make_request_options,
    HttpxBinaryResponseContent,
)
from ....types import shared_params
from ....types.images import v2_list_params
from .direct_uploads import (
    DirectUploads,
    AsyncDirectUploads,
    DirectUploadsWithRawResponse,
    AsyncDirectUploadsWithRawResponse,
    DirectUploadsWithStreamingResponse,
    AsyncDirectUploadsWithStreamingResponse,
)
from ...._wrappers import ResultWrapper
from typing import cast
from typing import cast

__all__ = ["V2s", "AsyncV2s"]


class V2s(SyncAPIResource):
    @cached_property
    def direct_uploads(self) -> DirectUploads:
        return DirectUploads(self._client)

    @cached_property
    def with_raw_response(self) -> V2sWithRawResponse:
        return V2sWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> V2sWithStreamingResponse:
        return V2sWithStreamingResponse(self)

    def list(
        self,
        account_id: str,
        *,
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


class AsyncV2s(AsyncAPIResource):
    @cached_property
    def direct_uploads(self) -> AsyncDirectUploads:
        return AsyncDirectUploads(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncV2sWithRawResponse:
        return AsyncV2sWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncV2sWithStreamingResponse:
        return AsyncV2sWithStreamingResponse(self)

    async def list(
        self,
        account_id: str,
        *,
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


class V2sWithRawResponse:
    def __init__(self, v2s: V2s) -> None:
        self._v2s = v2s

        self.list = to_raw_response_wrapper(
            v2s.list,
        )

    @cached_property
    def direct_uploads(self) -> DirectUploadsWithRawResponse:
        return DirectUploadsWithRawResponse(self._v2s.direct_uploads)


class AsyncV2sWithRawResponse:
    def __init__(self, v2s: AsyncV2s) -> None:
        self._v2s = v2s

        self.list = async_to_raw_response_wrapper(
            v2s.list,
        )

    @cached_property
    def direct_uploads(self) -> AsyncDirectUploadsWithRawResponse:
        return AsyncDirectUploadsWithRawResponse(self._v2s.direct_uploads)


class V2sWithStreamingResponse:
    def __init__(self, v2s: V2s) -> None:
        self._v2s = v2s

        self.list = to_streamed_response_wrapper(
            v2s.list,
        )

    @cached_property
    def direct_uploads(self) -> DirectUploadsWithStreamingResponse:
        return DirectUploadsWithStreamingResponse(self._v2s.direct_uploads)


class AsyncV2sWithStreamingResponse:
    def __init__(self, v2s: AsyncV2s) -> None:
        self._v2s = v2s

        self.list = async_to_streamed_response_wrapper(
            v2s.list,
        )

    @cached_property
    def direct_uploads(self) -> AsyncDirectUploadsWithStreamingResponse:
        return AsyncDirectUploadsWithStreamingResponse(self._v2s.direct_uploads)
