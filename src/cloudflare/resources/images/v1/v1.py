# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, Type, cast

import httpx

from .keys import (
    KeysResource,
    AsyncKeysResource,
    KeysResourceWithRawResponse,
    AsyncKeysResourceWithRawResponse,
    KeysResourceWithStreamingResponse,
    AsyncKeysResourceWithStreamingResponse,
)
from .blobs import (
    BlobsResource,
    AsyncBlobsResource,
    BlobsResourceWithRawResponse,
    AsyncBlobsResourceWithRawResponse,
    BlobsResourceWithStreamingResponse,
    AsyncBlobsResourceWithStreamingResponse,
)
from .stats import (
    StatsResource,
    AsyncStatsResource,
    StatsResourceWithRawResponse,
    AsyncStatsResourceWithRawResponse,
    StatsResourceWithStreamingResponse,
    AsyncStatsResourceWithStreamingResponse,
)
from .variants import (
    VariantsResource,
    AsyncVariantsResource,
    VariantsResourceWithRawResponse,
    AsyncVariantsResourceWithRawResponse,
    VariantsResourceWithStreamingResponse,
    AsyncVariantsResourceWithStreamingResponse,
)
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
from ....pagination import SyncV4PagePagination, AsyncV4PagePagination
from ...._base_client import AsyncPaginator, make_request_options
from ....types.images import v1_edit_params, v1_list_params, v1_create_params
from ....types.images.image import Image
from ....types.images.v1_list_response import V1ListResponse
from ....types.images.v1_delete_response import V1DeleteResponse

__all__ = ["V1Resource", "AsyncV1Resource"]


class V1Resource(SyncAPIResource):
    @cached_property
    def keys(self) -> KeysResource:
        return KeysResource(self._client)

    @cached_property
    def stats(self) -> StatsResource:
        return StatsResource(self._client)

    @cached_property
    def variants(self) -> VariantsResource:
        return VariantsResource(self._client)

    @cached_property
    def blobs(self) -> BlobsResource:
        return BlobsResource(self._client)

    @cached_property
    def with_raw_response(self) -> V1ResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return V1ResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> V1ResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return V1ResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        account_id: str,
        file: object | NotGiven = NOT_GIVEN,
        metadata: object | NotGiven = NOT_GIVEN,
        require_signed_urls: bool | NotGiven = NOT_GIVEN,
        url: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Image:
        """
        Upload an image with up to 10 Megabytes using a single HTTP POST
        (multipart/form-data) request. An image can be uploaded by sending an image file
        or passing an accessible to an API url.

        Args:
          account_id: Account identifier tag.

          file: An image binary data. Only needed when type is uploading a file.

          metadata: User modifiable key-value store. Can use used for keeping references to another
              system of record for managing images.

          require_signed_urls: Indicates whether the image requires a signature token for the access.

          url: A URL to fetch an image from origin. Only needed when type is uploading from a
              URL.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return self._post(
            f"/accounts/{account_id}/images/v1",
            body=maybe_transform(
                {
                    "file": file,
                    "metadata": metadata,
                    "require_signed_urls": require_signed_urls,
                    "url": url,
                },
                v1_create_params.V1CreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Image]._unwrapper,
            ),
            cast_to=cast(Type[Image], ResultWrapper[Image]),
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
                    post_parser=ResultWrapper[V1DeleteResponse]._unwrapper,
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
    ) -> Image:
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
                post_parser=ResultWrapper[Image]._unwrapper,
            ),
            cast_to=cast(Type[Image], ResultWrapper[Image]),
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
    ) -> Image:
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
                post_parser=ResultWrapper[Image]._unwrapper,
            ),
            cast_to=cast(Type[Image], ResultWrapper[Image]),
        )


class AsyncV1Resource(AsyncAPIResource):
    @cached_property
    def keys(self) -> AsyncKeysResource:
        return AsyncKeysResource(self._client)

    @cached_property
    def stats(self) -> AsyncStatsResource:
        return AsyncStatsResource(self._client)

    @cached_property
    def variants(self) -> AsyncVariantsResource:
        return AsyncVariantsResource(self._client)

    @cached_property
    def blobs(self) -> AsyncBlobsResource:
        return AsyncBlobsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncV1ResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncV1ResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncV1ResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncV1ResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_id: str,
        file: object | NotGiven = NOT_GIVEN,
        metadata: object | NotGiven = NOT_GIVEN,
        require_signed_urls: bool | NotGiven = NOT_GIVEN,
        url: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Image:
        """
        Upload an image with up to 10 Megabytes using a single HTTP POST
        (multipart/form-data) request. An image can be uploaded by sending an image file
        or passing an accessible to an API url.

        Args:
          account_id: Account identifier tag.

          file: An image binary data. Only needed when type is uploading a file.

          metadata: User modifiable key-value store. Can use used for keeping references to another
              system of record for managing images.

          require_signed_urls: Indicates whether the image requires a signature token for the access.

          url: A URL to fetch an image from origin. Only needed when type is uploading from a
              URL.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return await self._post(
            f"/accounts/{account_id}/images/v1",
            body=await async_maybe_transform(
                {
                    "file": file,
                    "metadata": metadata,
                    "require_signed_urls": require_signed_urls,
                    "url": url,
                },
                v1_create_params.V1CreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Image]._unwrapper,
            ),
            cast_to=cast(Type[Image], ResultWrapper[Image]),
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
                    post_parser=ResultWrapper[V1DeleteResponse]._unwrapper,
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
    ) -> Image:
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
            body=await async_maybe_transform(
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
                post_parser=ResultWrapper[Image]._unwrapper,
            ),
            cast_to=cast(Type[Image], ResultWrapper[Image]),
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
    ) -> Image:
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
                post_parser=ResultWrapper[Image]._unwrapper,
            ),
            cast_to=cast(Type[Image], ResultWrapper[Image]),
        )


class V1ResourceWithRawResponse:
    def __init__(self, v1: V1Resource) -> None:
        self._v1 = v1

        self.create = to_raw_response_wrapper(
            v1.create,
        )
        self.list = to_raw_response_wrapper(
            v1.list,
        )
        self.delete = to_raw_response_wrapper(
            v1.delete,
        )
        self.edit = to_raw_response_wrapper(
            v1.edit,
        )
        self.get = to_raw_response_wrapper(
            v1.get,
        )

    @cached_property
    def keys(self) -> KeysResourceWithRawResponse:
        return KeysResourceWithRawResponse(self._v1.keys)

    @cached_property
    def stats(self) -> StatsResourceWithRawResponse:
        return StatsResourceWithRawResponse(self._v1.stats)

    @cached_property
    def variants(self) -> VariantsResourceWithRawResponse:
        return VariantsResourceWithRawResponse(self._v1.variants)

    @cached_property
    def blobs(self) -> BlobsResourceWithRawResponse:
        return BlobsResourceWithRawResponse(self._v1.blobs)


class AsyncV1ResourceWithRawResponse:
    def __init__(self, v1: AsyncV1Resource) -> None:
        self._v1 = v1

        self.create = async_to_raw_response_wrapper(
            v1.create,
        )
        self.list = async_to_raw_response_wrapper(
            v1.list,
        )
        self.delete = async_to_raw_response_wrapper(
            v1.delete,
        )
        self.edit = async_to_raw_response_wrapper(
            v1.edit,
        )
        self.get = async_to_raw_response_wrapper(
            v1.get,
        )

    @cached_property
    def keys(self) -> AsyncKeysResourceWithRawResponse:
        return AsyncKeysResourceWithRawResponse(self._v1.keys)

    @cached_property
    def stats(self) -> AsyncStatsResourceWithRawResponse:
        return AsyncStatsResourceWithRawResponse(self._v1.stats)

    @cached_property
    def variants(self) -> AsyncVariantsResourceWithRawResponse:
        return AsyncVariantsResourceWithRawResponse(self._v1.variants)

    @cached_property
    def blobs(self) -> AsyncBlobsResourceWithRawResponse:
        return AsyncBlobsResourceWithRawResponse(self._v1.blobs)


class V1ResourceWithStreamingResponse:
    def __init__(self, v1: V1Resource) -> None:
        self._v1 = v1

        self.create = to_streamed_response_wrapper(
            v1.create,
        )
        self.list = to_streamed_response_wrapper(
            v1.list,
        )
        self.delete = to_streamed_response_wrapper(
            v1.delete,
        )
        self.edit = to_streamed_response_wrapper(
            v1.edit,
        )
        self.get = to_streamed_response_wrapper(
            v1.get,
        )

    @cached_property
    def keys(self) -> KeysResourceWithStreamingResponse:
        return KeysResourceWithStreamingResponse(self._v1.keys)

    @cached_property
    def stats(self) -> StatsResourceWithStreamingResponse:
        return StatsResourceWithStreamingResponse(self._v1.stats)

    @cached_property
    def variants(self) -> VariantsResourceWithStreamingResponse:
        return VariantsResourceWithStreamingResponse(self._v1.variants)

    @cached_property
    def blobs(self) -> BlobsResourceWithStreamingResponse:
        return BlobsResourceWithStreamingResponse(self._v1.blobs)


class AsyncV1ResourceWithStreamingResponse:
    def __init__(self, v1: AsyncV1Resource) -> None:
        self._v1 = v1

        self.create = async_to_streamed_response_wrapper(
            v1.create,
        )
        self.list = async_to_streamed_response_wrapper(
            v1.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            v1.delete,
        )
        self.edit = async_to_streamed_response_wrapper(
            v1.edit,
        )
        self.get = async_to_streamed_response_wrapper(
            v1.get,
        )

    @cached_property
    def keys(self) -> AsyncKeysResourceWithStreamingResponse:
        return AsyncKeysResourceWithStreamingResponse(self._v1.keys)

    @cached_property
    def stats(self) -> AsyncStatsResourceWithStreamingResponse:
        return AsyncStatsResourceWithStreamingResponse(self._v1.stats)

    @cached_property
    def variants(self) -> AsyncVariantsResourceWithStreamingResponse:
        return AsyncVariantsResourceWithStreamingResponse(self._v1.variants)

    @cached_property
    def blobs(self) -> AsyncBlobsResourceWithStreamingResponse:
        return AsyncBlobsResourceWithStreamingResponse(self._v1.blobs)
