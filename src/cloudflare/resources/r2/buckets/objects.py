# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Type, cast
from typing_extensions import Literal

import httpx

from ...._files import read_file_content, async_read_file_content
from ...._types import (
    Body,
    Omit,
    Query,
    Headers,
    NotGiven,
    BinaryTypes,
    FileContent,
    AsyncBinaryTypes,
    omit,
    not_given,
)
from ...._utils import is_given, path_template, maybe_transform, strip_not_given
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    to_custom_raw_response_wrapper,
    async_to_streamed_response_wrapper,
    to_custom_streamed_response_wrapper,
    async_to_custom_raw_response_wrapper,
    async_to_custom_streamed_response_wrapper,
)
from ...._wrappers import ResultWrapper
from ....pagination import SyncCursorPagination, AsyncCursorPagination
from ...._base_client import AsyncPaginator, make_request_options
from ....types.r2.buckets import object_list_params
from ....types.r2.buckets.object_list_response import ObjectListResponse
from ....types.r2.buckets.object_delete_response import ObjectDeleteResponse
from ....types.r2.buckets.object_upload_response import ObjectUploadResponse

__all__ = ["ObjectsResource", "AsyncObjectsResource"]


class ObjectsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ObjectsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return ObjectsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ObjectsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return ObjectsResourceWithStreamingResponse(self)

    def list(
        self,
        bucket_name: str,
        *,
        account_id: str,
        cursor: str | Omit = omit,
        delimiter: str | Omit = omit,
        per_page: int | Omit = omit,
        prefix: str | Omit = omit,
        start_after: str | Omit = omit,
        jurisdiction: Literal["default", "eu", "fedramp"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorPagination[ObjectListResponse]:
        """Lists objects in an R2 bucket.

        Returns object metadata including key, size,
        etag, last modified date, HTTP metadata, and custom metadata.

        For most workloads, we recommend using R2's
        [S3-compatible API](https://developers.cloudflare.com/r2/api/s3/api/) or a
        [Worker with an R2 binding](https://developers.cloudflare.com/r2/api/workers/workers-api-reference/)
        instead.

        Args:
          account_id: Account ID.

          bucket_name: Name of the bucket.

          cursor: Pagination cursor received from a previous List Objects call. Used to retrieve
              the next page of results.

          delimiter: A single character used to group keys. All keys that contain the delimiter
              between the prefix and the first occurrence of the delimiter after the prefix
              are grouped under a single result element.

          per_page: Maximum number of objects to return per page.

          prefix: Restricts results to only those objects whose keys begin with the specified
              prefix.

          start_after: Returns objects with keys that come after the specified key in lexicographic
              order.

          jurisdiction: Jurisdiction where objects in this bucket are guaranteed to be stored.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not bucket_name:
            raise ValueError(f"Expected a non-empty value for `bucket_name` but received {bucket_name!r}")
        extra_headers = {
            **strip_not_given({"cf-r2-jurisdiction": str(jurisdiction) if is_given(jurisdiction) else not_given}),
            **(extra_headers or {}),
        }
        return self._get_api_list(
            path_template(
                "/accounts/{account_id}/r2/buckets/{bucket_name}/objects",
                account_id=account_id,
                bucket_name=bucket_name,
            ),
            page=SyncCursorPagination[ObjectListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "delimiter": delimiter,
                        "per_page": per_page,
                        "prefix": prefix,
                        "start_after": start_after,
                    },
                    object_list_params.ObjectListParams,
                ),
            ),
            model=ObjectListResponse,
        )

    def delete(
        self,
        object_key: str,
        *,
        account_id: str,
        bucket_name: str,
        jurisdiction: Literal["default", "eu", "fedramp"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ObjectDeleteResponse:
        """
        Deletes an object from an R2 bucket.

        For most workloads, we recommend using R2's
        [S3-compatible API](https://developers.cloudflare.com/r2/api/s3/api/) or a
        [Worker with an R2 binding](https://developers.cloudflare.com/r2/api/workers/workers-api-reference/)
        instead.

        Args:
          account_id: Account ID.

          bucket_name: Name of the bucket.

          object_key: The key (name) of the object to delete. May contain slashes for path-like keys.
              Slashes (`/`) within the key MUST be sent literally and MUST NOT be
              percent-encoded (i.e. `%2F`); other reserved characters should be
              percent-encoded as usual.

          jurisdiction: Jurisdiction where objects in this bucket are guaranteed to be stored.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not bucket_name:
            raise ValueError(f"Expected a non-empty value for `bucket_name` but received {bucket_name!r}")
        if not object_key:
            raise ValueError(f"Expected a non-empty value for `object_key` but received {object_key!r}")
        extra_headers = {
            **strip_not_given({"cf-r2-jurisdiction": str(jurisdiction) if is_given(jurisdiction) else not_given}),
            **(extra_headers or {}),
        }
        return self._delete(
            path_template(
                "/accounts/{account_id}/r2/buckets/{bucket_name}/objects/{object_key}",
                account_id=account_id,
                bucket_name=bucket_name,
                object_key=object_key,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[ObjectDeleteResponse]._unwrapper,
            ),
            cast_to=cast(Type[ObjectDeleteResponse], ResultWrapper[ObjectDeleteResponse]),
        )

    def get(
        self,
        object_key: str,
        *,
        account_id: str,
        bucket_name: str,
        jurisdiction: Literal["default", "eu", "fedramp"] | Omit = omit,
        if_modified_since: str | Omit = omit,
        if_none_match: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BinaryAPIResponse:
        """Retrieves an object from an R2 bucket.

        Returns the object body along with
        metadata headers.

        For most workloads, we recommend using R2's
        [S3-compatible API](https://developers.cloudflare.com/r2/api/s3/api/) or a
        [Worker with an R2 binding](https://developers.cloudflare.com/r2/api/workers/workers-api-reference/)
        instead.

        Args:
          account_id: Account ID.

          bucket_name: Name of the bucket.

          object_key: The key (name) of the object to retrieve. May contain slashes for path-like
              keys. Slashes (`/`) within the key MUST be sent literally and MUST NOT be
              percent-encoded (i.e. `%2F`); other reserved characters should be
              percent-encoded as usual.

          jurisdiction: Jurisdiction where objects in this bucket are guaranteed to be stored.

          if_modified_since: Returns the object only if it has been modified since the specified time. Must
              be formatted as an HTTP-date (RFC 7231), e.g. `Tue, 15 Jan 2024 10:30:00 GMT`.

          if_none_match: Returns the object only if its ETag does not match the given value.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not bucket_name:
            raise ValueError(f"Expected a non-empty value for `bucket_name` but received {bucket_name!r}")
        if not object_key:
            raise ValueError(f"Expected a non-empty value for `object_key` but received {object_key!r}")
        extra_headers = {"Accept": "application/octet-stream", **(extra_headers or {})}
        extra_headers = {
            **strip_not_given(
                {
                    "cf-r2-jurisdiction": str(jurisdiction) if is_given(jurisdiction) else not_given,
                    "If-Modified-Since": if_modified_since,
                    "If-None-Match": if_none_match,
                }
            ),
            **(extra_headers or {}),
        }
        return self._get(
            path_template(
                "/accounts/{account_id}/r2/buckets/{bucket_name}/objects/{object_key}",
                account_id=account_id,
                bucket_name=bucket_name,
                object_key=object_key,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BinaryAPIResponse,
        )

    def upload(
        self,
        object_key: str,
        body: FileContent | BinaryTypes,
        *,
        account_id: str,
        bucket_name: str,
        jurisdiction: Literal["default", "eu", "fedramp"] | Omit = omit,
        cf_r2_storage_class: Literal["Standard", "InfrequentAccess"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ObjectUploadResponse:
        """Uploads an object to an R2 bucket.

        The object body is provided as the request
        body. Returns metadata about the uploaded object.

        The maximum upload size for this endpoint is 300 MB. For most workloads, we
        recommend using R2's
        [S3-compatible API](https://developers.cloudflare.com/r2/api/s3/api/) or a
        [Worker with an R2 binding](https://developers.cloudflare.com/r2/api/workers/workers-api-reference/)
        instead.

        Args:
          account_id: Account ID.

          bucket_name: Name of the bucket.

          object_key: The key (name) to assign to the object. May contain slashes for path-like keys.
              Slashes (`/`) within the key MUST be sent literally and MUST NOT be
              percent-encoded (i.e. `%2F`); other reserved characters should be
              percent-encoded as usual.

          body: The object body to upload.

          jurisdiction: Jurisdiction where objects in this bucket are guaranteed to be stored.

          cf_r2_storage_class: Storage class for newly uploaded objects, unless specified otherwise.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not bucket_name:
            raise ValueError(f"Expected a non-empty value for `bucket_name` but received {bucket_name!r}")
        if not object_key:
            raise ValueError(f"Expected a non-empty value for `object_key` but received {object_key!r}")
        extra_headers = {
            **strip_not_given(
                {
                    "cf-r2-jurisdiction": str(jurisdiction) if is_given(jurisdiction) else not_given,
                    "cf-r2-storage-class": str(cf_r2_storage_class) if is_given(cf_r2_storage_class) else not_given,
                }
            ),
            **(extra_headers or {}),
        }
        extra_headers = {"Content-Type": "application/octet-stream", **(extra_headers or {})}
        return self._put(
            path_template(
                "/accounts/{account_id}/r2/buckets/{bucket_name}/objects/{object_key}",
                account_id=account_id,
                bucket_name=bucket_name,
                object_key=object_key,
            ),
            content=read_file_content(body) if isinstance(body, os.PathLike) else body,
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[ObjectUploadResponse]._unwrapper,
            ),
            cast_to=cast(Type[ObjectUploadResponse], ResultWrapper[ObjectUploadResponse]),
        )


class AsyncObjectsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncObjectsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncObjectsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncObjectsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncObjectsResourceWithStreamingResponse(self)

    def list(
        self,
        bucket_name: str,
        *,
        account_id: str,
        cursor: str | Omit = omit,
        delimiter: str | Omit = omit,
        per_page: int | Omit = omit,
        prefix: str | Omit = omit,
        start_after: str | Omit = omit,
        jurisdiction: Literal["default", "eu", "fedramp"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[ObjectListResponse, AsyncCursorPagination[ObjectListResponse]]:
        """Lists objects in an R2 bucket.

        Returns object metadata including key, size,
        etag, last modified date, HTTP metadata, and custom metadata.

        For most workloads, we recommend using R2's
        [S3-compatible API](https://developers.cloudflare.com/r2/api/s3/api/) or a
        [Worker with an R2 binding](https://developers.cloudflare.com/r2/api/workers/workers-api-reference/)
        instead.

        Args:
          account_id: Account ID.

          bucket_name: Name of the bucket.

          cursor: Pagination cursor received from a previous List Objects call. Used to retrieve
              the next page of results.

          delimiter: A single character used to group keys. All keys that contain the delimiter
              between the prefix and the first occurrence of the delimiter after the prefix
              are grouped under a single result element.

          per_page: Maximum number of objects to return per page.

          prefix: Restricts results to only those objects whose keys begin with the specified
              prefix.

          start_after: Returns objects with keys that come after the specified key in lexicographic
              order.

          jurisdiction: Jurisdiction where objects in this bucket are guaranteed to be stored.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not bucket_name:
            raise ValueError(f"Expected a non-empty value for `bucket_name` but received {bucket_name!r}")
        extra_headers = {
            **strip_not_given({"cf-r2-jurisdiction": str(jurisdiction) if is_given(jurisdiction) else not_given}),
            **(extra_headers or {}),
        }
        return self._get_api_list(
            path_template(
                "/accounts/{account_id}/r2/buckets/{bucket_name}/objects",
                account_id=account_id,
                bucket_name=bucket_name,
            ),
            page=AsyncCursorPagination[ObjectListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "delimiter": delimiter,
                        "per_page": per_page,
                        "prefix": prefix,
                        "start_after": start_after,
                    },
                    object_list_params.ObjectListParams,
                ),
            ),
            model=ObjectListResponse,
        )

    async def delete(
        self,
        object_key: str,
        *,
        account_id: str,
        bucket_name: str,
        jurisdiction: Literal["default", "eu", "fedramp"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ObjectDeleteResponse:
        """
        Deletes an object from an R2 bucket.

        For most workloads, we recommend using R2's
        [S3-compatible API](https://developers.cloudflare.com/r2/api/s3/api/) or a
        [Worker with an R2 binding](https://developers.cloudflare.com/r2/api/workers/workers-api-reference/)
        instead.

        Args:
          account_id: Account ID.

          bucket_name: Name of the bucket.

          object_key: The key (name) of the object to delete. May contain slashes for path-like keys.
              Slashes (`/`) within the key MUST be sent literally and MUST NOT be
              percent-encoded (i.e. `%2F`); other reserved characters should be
              percent-encoded as usual.

          jurisdiction: Jurisdiction where objects in this bucket are guaranteed to be stored.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not bucket_name:
            raise ValueError(f"Expected a non-empty value for `bucket_name` but received {bucket_name!r}")
        if not object_key:
            raise ValueError(f"Expected a non-empty value for `object_key` but received {object_key!r}")
        extra_headers = {
            **strip_not_given({"cf-r2-jurisdiction": str(jurisdiction) if is_given(jurisdiction) else not_given}),
            **(extra_headers or {}),
        }
        return await self._delete(
            path_template(
                "/accounts/{account_id}/r2/buckets/{bucket_name}/objects/{object_key}",
                account_id=account_id,
                bucket_name=bucket_name,
                object_key=object_key,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[ObjectDeleteResponse]._unwrapper,
            ),
            cast_to=cast(Type[ObjectDeleteResponse], ResultWrapper[ObjectDeleteResponse]),
        )

    async def get(
        self,
        object_key: str,
        *,
        account_id: str,
        bucket_name: str,
        jurisdiction: Literal["default", "eu", "fedramp"] | Omit = omit,
        if_modified_since: str | Omit = omit,
        if_none_match: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncBinaryAPIResponse:
        """Retrieves an object from an R2 bucket.

        Returns the object body along with
        metadata headers.

        For most workloads, we recommend using R2's
        [S3-compatible API](https://developers.cloudflare.com/r2/api/s3/api/) or a
        [Worker with an R2 binding](https://developers.cloudflare.com/r2/api/workers/workers-api-reference/)
        instead.

        Args:
          account_id: Account ID.

          bucket_name: Name of the bucket.

          object_key: The key (name) of the object to retrieve. May contain slashes for path-like
              keys. Slashes (`/`) within the key MUST be sent literally and MUST NOT be
              percent-encoded (i.e. `%2F`); other reserved characters should be
              percent-encoded as usual.

          jurisdiction: Jurisdiction where objects in this bucket are guaranteed to be stored.

          if_modified_since: Returns the object only if it has been modified since the specified time. Must
              be formatted as an HTTP-date (RFC 7231), e.g. `Tue, 15 Jan 2024 10:30:00 GMT`.

          if_none_match: Returns the object only if its ETag does not match the given value.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not bucket_name:
            raise ValueError(f"Expected a non-empty value for `bucket_name` but received {bucket_name!r}")
        if not object_key:
            raise ValueError(f"Expected a non-empty value for `object_key` but received {object_key!r}")
        extra_headers = {"Accept": "application/octet-stream", **(extra_headers or {})}
        extra_headers = {
            **strip_not_given(
                {
                    "cf-r2-jurisdiction": str(jurisdiction) if is_given(jurisdiction) else not_given,
                    "If-Modified-Since": if_modified_since,
                    "If-None-Match": if_none_match,
                }
            ),
            **(extra_headers or {}),
        }
        return await self._get(
            path_template(
                "/accounts/{account_id}/r2/buckets/{bucket_name}/objects/{object_key}",
                account_id=account_id,
                bucket_name=bucket_name,
                object_key=object_key,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AsyncBinaryAPIResponse,
        )

    async def upload(
        self,
        object_key: str,
        body: FileContent | AsyncBinaryTypes,
        *,
        account_id: str,
        bucket_name: str,
        jurisdiction: Literal["default", "eu", "fedramp"] | Omit = omit,
        cf_r2_storage_class: Literal["Standard", "InfrequentAccess"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ObjectUploadResponse:
        """Uploads an object to an R2 bucket.

        The object body is provided as the request
        body. Returns metadata about the uploaded object.

        The maximum upload size for this endpoint is 300 MB. For most workloads, we
        recommend using R2's
        [S3-compatible API](https://developers.cloudflare.com/r2/api/s3/api/) or a
        [Worker with an R2 binding](https://developers.cloudflare.com/r2/api/workers/workers-api-reference/)
        instead.

        Args:
          account_id: Account ID.

          bucket_name: Name of the bucket.

          object_key: The key (name) to assign to the object. May contain slashes for path-like keys.
              Slashes (`/`) within the key MUST be sent literally and MUST NOT be
              percent-encoded (i.e. `%2F`); other reserved characters should be
              percent-encoded as usual.

          body: The object body to upload.

          jurisdiction: Jurisdiction where objects in this bucket are guaranteed to be stored.

          cf_r2_storage_class: Storage class for newly uploaded objects, unless specified otherwise.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not bucket_name:
            raise ValueError(f"Expected a non-empty value for `bucket_name` but received {bucket_name!r}")
        if not object_key:
            raise ValueError(f"Expected a non-empty value for `object_key` but received {object_key!r}")
        extra_headers = {
            **strip_not_given(
                {
                    "cf-r2-jurisdiction": str(jurisdiction) if is_given(jurisdiction) else not_given,
                    "cf-r2-storage-class": str(cf_r2_storage_class) if is_given(cf_r2_storage_class) else not_given,
                }
            ),
            **(extra_headers or {}),
        }
        extra_headers = {"Content-Type": "application/octet-stream", **(extra_headers or {})}
        return await self._put(
            path_template(
                "/accounts/{account_id}/r2/buckets/{bucket_name}/objects/{object_key}",
                account_id=account_id,
                bucket_name=bucket_name,
                object_key=object_key,
            ),
            content=await async_read_file_content(body) if isinstance(body, os.PathLike) else body,
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[ObjectUploadResponse]._unwrapper,
            ),
            cast_to=cast(Type[ObjectUploadResponse], ResultWrapper[ObjectUploadResponse]),
        )


class ObjectsResourceWithRawResponse:
    def __init__(self, objects: ObjectsResource) -> None:
        self._objects = objects

        self.list = to_raw_response_wrapper(
            objects.list,
        )
        self.delete = to_raw_response_wrapper(
            objects.delete,
        )
        self.get = to_custom_raw_response_wrapper(
            objects.get,
            BinaryAPIResponse,
        )
        self.upload = to_raw_response_wrapper(
            objects.upload,
        )


class AsyncObjectsResourceWithRawResponse:
    def __init__(self, objects: AsyncObjectsResource) -> None:
        self._objects = objects

        self.list = async_to_raw_response_wrapper(
            objects.list,
        )
        self.delete = async_to_raw_response_wrapper(
            objects.delete,
        )
        self.get = async_to_custom_raw_response_wrapper(
            objects.get,
            AsyncBinaryAPIResponse,
        )
        self.upload = async_to_raw_response_wrapper(
            objects.upload,
        )


class ObjectsResourceWithStreamingResponse:
    def __init__(self, objects: ObjectsResource) -> None:
        self._objects = objects

        self.list = to_streamed_response_wrapper(
            objects.list,
        )
        self.delete = to_streamed_response_wrapper(
            objects.delete,
        )
        self.get = to_custom_streamed_response_wrapper(
            objects.get,
            StreamedBinaryAPIResponse,
        )
        self.upload = to_streamed_response_wrapper(
            objects.upload,
        )


class AsyncObjectsResourceWithStreamingResponse:
    def __init__(self, objects: AsyncObjectsResource) -> None:
        self._objects = objects

        self.list = async_to_streamed_response_wrapper(
            objects.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            objects.delete,
        )
        self.get = async_to_custom_streamed_response_wrapper(
            objects.get,
            AsyncStreamedBinaryAPIResponse,
        )
        self.upload = async_to_streamed_response_wrapper(
            objects.upload,
        )
