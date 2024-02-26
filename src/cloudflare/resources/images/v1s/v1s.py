# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Any, Type, cast

import httpx

from .keys import (
    Keys,
    AsyncKeys,
    KeysWithRawResponse,
    AsyncKeysWithRawResponse,
    KeysWithStreamingResponse,
    AsyncKeysWithStreamingResponse,
)
from .blobs import (
    Blobs,
    AsyncBlobs,
    BlobsWithRawResponse,
    AsyncBlobsWithRawResponse,
    BlobsWithStreamingResponse,
    AsyncBlobsWithStreamingResponse,
)
from .stats import (
    Stats,
    AsyncStats,
    StatsWithRawResponse,
    AsyncStatsWithRawResponse,
    StatsWithStreamingResponse,
    AsyncStatsWithStreamingResponse,
)
from .variants import (
    Variants,
    AsyncVariants,
    VariantsWithRawResponse,
    AsyncVariantsWithRawResponse,
    VariantsWithStreamingResponse,
    AsyncVariantsWithStreamingResponse,
)
from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._wrappers import ResultWrapper
from ....pagination import SyncV4PagePagination, AsyncV4PagePagination
from ...._base_client import (
    AsyncPaginator,
    make_request_options,
)
from ....types.images import (
    V1GetResponse,
    V1EditResponse,
    V1ListResponse,
    V1CreateResponse,
    V1DeleteResponse,
    v1_edit_params,
    v1_list_params,
    v1_create_params,
)

__all__ = ["V1s", "AsyncV1s"]


class V1s(SyncAPIResource):
    @cached_property
    def keys(self) -> Keys:
        return Keys(self._client)

    @cached_property
    def stats(self) -> Stats:
        return Stats(self._client)

    @cached_property
    def variants(self) -> Variants:
        return Variants(self._client)

    @cached_property
    def blobs(self) -> Blobs:
        return Blobs(self._client)

    @cached_property
    def with_raw_response(self) -> V1sWithRawResponse:
        return V1sWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> V1sWithStreamingResponse:
        return V1sWithStreamingResponse(self)

    def create(
        self,
        *,
        account_id: str,
        metadata: object | NotGiven = NOT_GIVEN,
        require_signed_urls: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> V1CreateResponse:
        """
        Upload an image with up to 10 Megabytes using a single HTTP POST
        (multipart/form-data) request. An image can be uploaded by sending an image file
        or passing an accessible to an API url.

        Args:
          account_id: Account identifier tag.

          require_signed_urls: Indicates whether the image requires a signature token for the access.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._post(
            f"/accounts/{account_id}/images/v1",
            body=maybe_transform(
                {
                    "metadata": metadata,
                    "require_signed_urls": require_signed_urls,
                },
                v1_create_params.V1CreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[V1CreateResponse], ResultWrapper[V1CreateResponse]),
        )

    def list(
        self,
        *,
        account_id: str,
        page: float | NotGiven = NOT_GIVEN,
        per_page: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncV4PagePagination[V1ListResponse]:
        """List up to 100 images with one request.

        Use the optional parameters below to get
        a specific range of images.

        Args:
          account_id: Account identifier tag.

          page: Page number of paginated results.

          per_page: Number of items per page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/images/v1",
            page=SyncV4PagePagination[V1ListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page": page,
                        "per_page": per_page,
                    },
                    v1_list_params.V1ListParams,
                ),
            ),
            model=V1ListResponse,
        )

    def delete(
        self,
        image_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> V1DeleteResponse:
        """Delete an image on Cloudflare Images.

        On success, all copies of the image are
        deleted and purged from cache.

        Args:
          account_id: Account identifier tag.

          image_id: Image unique identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not image_id:
            raise ValueError(f"Expected a non-empty value for `image_id` but received {image_id!r}")
        return cast(
            V1DeleteResponse,
            self._delete(
                f"/accounts/{account_id}/images/v1/{image_id}",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[V1DeleteResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def edit(
        self,
        image_id: str,
        *,
        account_id: str,
        metadata: object | NotGiven = NOT_GIVEN,
        require_signed_urls: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> V1EditResponse:
        """Update image access control.

        On access control change, all copies of the image
        are purged from cache.

        Args:
          account_id: Account identifier tag.

          image_id: Image unique identifier.

          metadata: User modifiable key-value store. Can be used for keeping references to another
              system of record for managing images. No change if not specified.

          require_signed_urls: Indicates whether the image can be accessed using only its UID. If set to
              `true`, a signed token needs to be generated with a signing key to view the
              image. Returns a new UID on a change. No change if not specified.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not image_id:
            raise ValueError(f"Expected a non-empty value for `image_id` but received {image_id!r}")
        return self._patch(
            f"/accounts/{account_id}/images/v1/{image_id}",
            body=maybe_transform(
                {
                    "metadata": metadata,
                    "require_signed_urls": require_signed_urls,
                },
                v1_edit_params.V1EditParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[V1EditResponse], ResultWrapper[V1EditResponse]),
        )

    def get(
        self,
        image_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> V1GetResponse:
        """
        Fetch details for a single image.

        Args:
          account_id: Account identifier tag.

          image_id: Image unique identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not image_id:
            raise ValueError(f"Expected a non-empty value for `image_id` but received {image_id!r}")
        return self._get(
            f"/accounts/{account_id}/images/v1/{image_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[V1GetResponse], ResultWrapper[V1GetResponse]),
        )


class AsyncV1s(AsyncAPIResource):
    @cached_property
    def keys(self) -> AsyncKeys:
        return AsyncKeys(self._client)

    @cached_property
    def stats(self) -> AsyncStats:
        return AsyncStats(self._client)

    @cached_property
    def variants(self) -> AsyncVariants:
        return AsyncVariants(self._client)

    @cached_property
    def blobs(self) -> AsyncBlobs:
        return AsyncBlobs(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncV1sWithRawResponse:
        return AsyncV1sWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncV1sWithStreamingResponse:
        return AsyncV1sWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_id: str,
        metadata: object | NotGiven = NOT_GIVEN,
        require_signed_urls: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> V1CreateResponse:
        """
        Upload an image with up to 10 Megabytes using a single HTTP POST
        (multipart/form-data) request. An image can be uploaded by sending an image file
        or passing an accessible to an API url.

        Args:
          account_id: Account identifier tag.

          require_signed_urls: Indicates whether the image requires a signature token for the access.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._post(
            f"/accounts/{account_id}/images/v1",
            body=maybe_transform(
                {
                    "metadata": metadata,
                    "require_signed_urls": require_signed_urls,
                },
                v1_create_params.V1CreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[V1CreateResponse], ResultWrapper[V1CreateResponse]),
        )

    def list(
        self,
        *,
        account_id: str,
        page: float | NotGiven = NOT_GIVEN,
        per_page: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[V1ListResponse, AsyncV4PagePagination[V1ListResponse]]:
        """List up to 100 images with one request.

        Use the optional parameters below to get
        a specific range of images.

        Args:
          account_id: Account identifier tag.

          page: Page number of paginated results.

          per_page: Number of items per page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/images/v1",
            page=AsyncV4PagePagination[V1ListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page": page,
                        "per_page": per_page,
                    },
                    v1_list_params.V1ListParams,
                ),
            ),
            model=V1ListResponse,
        )

    async def delete(
        self,
        image_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> V1DeleteResponse:
        """Delete an image on Cloudflare Images.

        On success, all copies of the image are
        deleted and purged from cache.

        Args:
          account_id: Account identifier tag.

          image_id: Image unique identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not image_id:
            raise ValueError(f"Expected a non-empty value for `image_id` but received {image_id!r}")
        return cast(
            V1DeleteResponse,
            await self._delete(
                f"/accounts/{account_id}/images/v1/{image_id}",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[V1DeleteResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def edit(
        self,
        image_id: str,
        *,
        account_id: str,
        metadata: object | NotGiven = NOT_GIVEN,
        require_signed_urls: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> V1EditResponse:
        """Update image access control.

        On access control change, all copies of the image
        are purged from cache.

        Args:
          account_id: Account identifier tag.

          image_id: Image unique identifier.

          metadata: User modifiable key-value store. Can be used for keeping references to another
              system of record for managing images. No change if not specified.

          require_signed_urls: Indicates whether the image can be accessed using only its UID. If set to
              `true`, a signed token needs to be generated with a signing key to view the
              image. Returns a new UID on a change. No change if not specified.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not image_id:
            raise ValueError(f"Expected a non-empty value for `image_id` but received {image_id!r}")
        return await self._patch(
            f"/accounts/{account_id}/images/v1/{image_id}",
            body=maybe_transform(
                {
                    "metadata": metadata,
                    "require_signed_urls": require_signed_urls,
                },
                v1_edit_params.V1EditParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[V1EditResponse], ResultWrapper[V1EditResponse]),
        )

    async def get(
        self,
        image_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> V1GetResponse:
        """
        Fetch details for a single image.

        Args:
          account_id: Account identifier tag.

          image_id: Image unique identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not image_id:
            raise ValueError(f"Expected a non-empty value for `image_id` but received {image_id!r}")
        return await self._get(
            f"/accounts/{account_id}/images/v1/{image_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[V1GetResponse], ResultWrapper[V1GetResponse]),
        )


class V1sWithRawResponse:
    def __init__(self, v1s: V1s) -> None:
        self._v1s = v1s

        self.create = to_raw_response_wrapper(
            v1s.create,
        )
        self.list = to_raw_response_wrapper(
            v1s.list,
        )
        self.delete = to_raw_response_wrapper(
            v1s.delete,
        )
        self.edit = to_raw_response_wrapper(
            v1s.edit,
        )
        self.get = to_raw_response_wrapper(
            v1s.get,
        )

    @cached_property
    def keys(self) -> KeysWithRawResponse:
        return KeysWithRawResponse(self._v1s.keys)

    @cached_property
    def stats(self) -> StatsWithRawResponse:
        return StatsWithRawResponse(self._v1s.stats)

    @cached_property
    def variants(self) -> VariantsWithRawResponse:
        return VariantsWithRawResponse(self._v1s.variants)

    @cached_property
    def blobs(self) -> BlobsWithRawResponse:
        return BlobsWithRawResponse(self._v1s.blobs)


class AsyncV1sWithRawResponse:
    def __init__(self, v1s: AsyncV1s) -> None:
        self._v1s = v1s

        self.create = async_to_raw_response_wrapper(
            v1s.create,
        )
        self.list = async_to_raw_response_wrapper(
            v1s.list,
        )
        self.delete = async_to_raw_response_wrapper(
            v1s.delete,
        )
        self.edit = async_to_raw_response_wrapper(
            v1s.edit,
        )
        self.get = async_to_raw_response_wrapper(
            v1s.get,
        )

    @cached_property
    def keys(self) -> AsyncKeysWithRawResponse:
        return AsyncKeysWithRawResponse(self._v1s.keys)

    @cached_property
    def stats(self) -> AsyncStatsWithRawResponse:
        return AsyncStatsWithRawResponse(self._v1s.stats)

    @cached_property
    def variants(self) -> AsyncVariantsWithRawResponse:
        return AsyncVariantsWithRawResponse(self._v1s.variants)

    @cached_property
    def blobs(self) -> AsyncBlobsWithRawResponse:
        return AsyncBlobsWithRawResponse(self._v1s.blobs)


class V1sWithStreamingResponse:
    def __init__(self, v1s: V1s) -> None:
        self._v1s = v1s

        self.create = to_streamed_response_wrapper(
            v1s.create,
        )
        self.list = to_streamed_response_wrapper(
            v1s.list,
        )
        self.delete = to_streamed_response_wrapper(
            v1s.delete,
        )
        self.edit = to_streamed_response_wrapper(
            v1s.edit,
        )
        self.get = to_streamed_response_wrapper(
            v1s.get,
        )

    @cached_property
    def keys(self) -> KeysWithStreamingResponse:
        return KeysWithStreamingResponse(self._v1s.keys)

    @cached_property
    def stats(self) -> StatsWithStreamingResponse:
        return StatsWithStreamingResponse(self._v1s.stats)

    @cached_property
    def variants(self) -> VariantsWithStreamingResponse:
        return VariantsWithStreamingResponse(self._v1s.variants)

    @cached_property
    def blobs(self) -> BlobsWithStreamingResponse:
        return BlobsWithStreamingResponse(self._v1s.blobs)


class AsyncV1sWithStreamingResponse:
    def __init__(self, v1s: AsyncV1s) -> None:
        self._v1s = v1s

        self.create = async_to_streamed_response_wrapper(
            v1s.create,
        )
        self.list = async_to_streamed_response_wrapper(
            v1s.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            v1s.delete,
        )
        self.edit = async_to_streamed_response_wrapper(
            v1s.edit,
        )
        self.get = async_to_streamed_response_wrapper(
            v1s.get,
        )

    @cached_property
    def keys(self) -> AsyncKeysWithStreamingResponse:
        return AsyncKeysWithStreamingResponse(self._v1s.keys)

    @cached_property
    def stats(self) -> AsyncStatsWithStreamingResponse:
        return AsyncStatsWithStreamingResponse(self._v1s.stats)

    @cached_property
    def variants(self) -> AsyncVariantsWithStreamingResponse:
        return AsyncVariantsWithStreamingResponse(self._v1s.variants)

    @cached_property
    def blobs(self) -> AsyncBlobsWithStreamingResponse:
        return AsyncBlobsWithStreamingResponse(self._v1s.blobs)
