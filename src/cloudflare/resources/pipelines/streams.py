# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, cast

import httpx

from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._wrappers import ResultWrapper
from ...pagination import SyncV4PagePaginationArray, AsyncV4PagePaginationArray
from ..._base_client import AsyncPaginator, make_request_options
from ...types.pipelines import stream_list_params, stream_create_params, stream_delete_params, stream_update_params
from ...types.pipelines.stream_get_response import StreamGetResponse
from ...types.pipelines.stream_list_response import StreamListResponse
from ...types.pipelines.stream_create_response import StreamCreateResponse
from ...types.pipelines.stream_update_response import StreamUpdateResponse

__all__ = ["StreamsResource", "AsyncStreamsResource"]


class StreamsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> StreamsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return StreamsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> StreamsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return StreamsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        account_id: str,
        name: str,
        format: stream_create_params.Format | Omit = omit,
        http: stream_create_params.HTTP | Omit = omit,
        schema: stream_create_params.Schema | Omit = omit,
        worker_binding: stream_create_params.WorkerBinding | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> StreamCreateResponse:
        """
        Create a new Stream.

        Args:
          account_id: Specifies the public ID of the account.

          name: Specifies the name of the Stream.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._post(
            f"/accounts/{account_id}/pipelines/v1/streams",
            body=maybe_transform(
                {
                    "name": name,
                    "format": format,
                    "http": http,
                    "schema": schema,
                    "worker_binding": worker_binding,
                },
                stream_create_params.StreamCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[StreamCreateResponse]._unwrapper,
            ),
            cast_to=cast(Type[StreamCreateResponse], ResultWrapper[StreamCreateResponse]),
        )

    def update(
        self,
        stream_id: str,
        *,
        account_id: str,
        http: stream_update_params.HTTP | Omit = omit,
        worker_binding: stream_update_params.WorkerBinding | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> StreamUpdateResponse:
        """
        Update a Stream.

        Args:
          account_id: Specifies the public ID of the account.

          stream_id: Specifies the public ID of the stream.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not stream_id:
            raise ValueError(f"Expected a non-empty value for `stream_id` but received {stream_id!r}")
        return self._patch(
            f"/accounts/{account_id}/pipelines/v1/streams/{stream_id}",
            body=maybe_transform(
                {
                    "http": http,
                    "worker_binding": worker_binding,
                },
                stream_update_params.StreamUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[StreamUpdateResponse]._unwrapper,
            ),
            cast_to=cast(Type[StreamUpdateResponse], ResultWrapper[StreamUpdateResponse]),
        )

    def list(
        self,
        *,
        account_id: str,
        page: float | Omit = omit,
        per_page: float | Omit = omit,
        pipeline_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncV4PagePaginationArray[StreamListResponse]:
        """
        List/Filter Streams in Account.

        Args:
          account_id: Specifies the public ID of the account.

          pipeline_id: Specifies the public ID of the pipeline.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/pipelines/v1/streams",
            page=SyncV4PagePaginationArray[StreamListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page": page,
                        "per_page": per_page,
                        "pipeline_id": pipeline_id,
                    },
                    stream_list_params.StreamListParams,
                ),
            ),
            model=StreamListResponse,
        )

    def delete(
        self,
        stream_id: str,
        *,
        account_id: str,
        force: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete Stream in Account.

        Args:
          account_id: Specifies the public ID of the account.

          stream_id: Specifies the public ID of the stream.

          force: Delete stream forcefully, including deleting any dependent pipelines.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not stream_id:
            raise ValueError(f"Expected a non-empty value for `stream_id` but received {stream_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/accounts/{account_id}/pipelines/v1/streams/{stream_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"force": force}, stream_delete_params.StreamDeleteParams),
            ),
            cast_to=NoneType,
        )

    def get(
        self,
        stream_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> StreamGetResponse:
        """
        Get Stream Details.

        Args:
          account_id: Specifies the public ID of the account.

          stream_id: Specifies the public ID of the stream.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not stream_id:
            raise ValueError(f"Expected a non-empty value for `stream_id` but received {stream_id!r}")
        return self._get(
            f"/accounts/{account_id}/pipelines/v1/streams/{stream_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[StreamGetResponse]._unwrapper,
            ),
            cast_to=cast(Type[StreamGetResponse], ResultWrapper[StreamGetResponse]),
        )


class AsyncStreamsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncStreamsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncStreamsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncStreamsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncStreamsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_id: str,
        name: str,
        format: stream_create_params.Format | Omit = omit,
        http: stream_create_params.HTTP | Omit = omit,
        schema: stream_create_params.Schema | Omit = omit,
        worker_binding: stream_create_params.WorkerBinding | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> StreamCreateResponse:
        """
        Create a new Stream.

        Args:
          account_id: Specifies the public ID of the account.

          name: Specifies the name of the Stream.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._post(
            f"/accounts/{account_id}/pipelines/v1/streams",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "format": format,
                    "http": http,
                    "schema": schema,
                    "worker_binding": worker_binding,
                },
                stream_create_params.StreamCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[StreamCreateResponse]._unwrapper,
            ),
            cast_to=cast(Type[StreamCreateResponse], ResultWrapper[StreamCreateResponse]),
        )

    async def update(
        self,
        stream_id: str,
        *,
        account_id: str,
        http: stream_update_params.HTTP | Omit = omit,
        worker_binding: stream_update_params.WorkerBinding | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> StreamUpdateResponse:
        """
        Update a Stream.

        Args:
          account_id: Specifies the public ID of the account.

          stream_id: Specifies the public ID of the stream.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not stream_id:
            raise ValueError(f"Expected a non-empty value for `stream_id` but received {stream_id!r}")
        return await self._patch(
            f"/accounts/{account_id}/pipelines/v1/streams/{stream_id}",
            body=await async_maybe_transform(
                {
                    "http": http,
                    "worker_binding": worker_binding,
                },
                stream_update_params.StreamUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[StreamUpdateResponse]._unwrapper,
            ),
            cast_to=cast(Type[StreamUpdateResponse], ResultWrapper[StreamUpdateResponse]),
        )

    def list(
        self,
        *,
        account_id: str,
        page: float | Omit = omit,
        per_page: float | Omit = omit,
        pipeline_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[StreamListResponse, AsyncV4PagePaginationArray[StreamListResponse]]:
        """
        List/Filter Streams in Account.

        Args:
          account_id: Specifies the public ID of the account.

          pipeline_id: Specifies the public ID of the pipeline.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/pipelines/v1/streams",
            page=AsyncV4PagePaginationArray[StreamListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page": page,
                        "per_page": per_page,
                        "pipeline_id": pipeline_id,
                    },
                    stream_list_params.StreamListParams,
                ),
            ),
            model=StreamListResponse,
        )

    async def delete(
        self,
        stream_id: str,
        *,
        account_id: str,
        force: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete Stream in Account.

        Args:
          account_id: Specifies the public ID of the account.

          stream_id: Specifies the public ID of the stream.

          force: Delete stream forcefully, including deleting any dependent pipelines.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not stream_id:
            raise ValueError(f"Expected a non-empty value for `stream_id` but received {stream_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/accounts/{account_id}/pipelines/v1/streams/{stream_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"force": force}, stream_delete_params.StreamDeleteParams),
            ),
            cast_to=NoneType,
        )

    async def get(
        self,
        stream_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> StreamGetResponse:
        """
        Get Stream Details.

        Args:
          account_id: Specifies the public ID of the account.

          stream_id: Specifies the public ID of the stream.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not stream_id:
            raise ValueError(f"Expected a non-empty value for `stream_id` but received {stream_id!r}")
        return await self._get(
            f"/accounts/{account_id}/pipelines/v1/streams/{stream_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[StreamGetResponse]._unwrapper,
            ),
            cast_to=cast(Type[StreamGetResponse], ResultWrapper[StreamGetResponse]),
        )


class StreamsResourceWithRawResponse:
    def __init__(self, streams: StreamsResource) -> None:
        self._streams = streams

        self.create = to_raw_response_wrapper(
            streams.create,
        )
        self.update = to_raw_response_wrapper(
            streams.update,
        )
        self.list = to_raw_response_wrapper(
            streams.list,
        )
        self.delete = to_raw_response_wrapper(
            streams.delete,
        )
        self.get = to_raw_response_wrapper(
            streams.get,
        )


class AsyncStreamsResourceWithRawResponse:
    def __init__(self, streams: AsyncStreamsResource) -> None:
        self._streams = streams

        self.create = async_to_raw_response_wrapper(
            streams.create,
        )
        self.update = async_to_raw_response_wrapper(
            streams.update,
        )
        self.list = async_to_raw_response_wrapper(
            streams.list,
        )
        self.delete = async_to_raw_response_wrapper(
            streams.delete,
        )
        self.get = async_to_raw_response_wrapper(
            streams.get,
        )


class StreamsResourceWithStreamingResponse:
    def __init__(self, streams: StreamsResource) -> None:
        self._streams = streams

        self.create = to_streamed_response_wrapper(
            streams.create,
        )
        self.update = to_streamed_response_wrapper(
            streams.update,
        )
        self.list = to_streamed_response_wrapper(
            streams.list,
        )
        self.delete = to_streamed_response_wrapper(
            streams.delete,
        )
        self.get = to_streamed_response_wrapper(
            streams.get,
        )


class AsyncStreamsResourceWithStreamingResponse:
    def __init__(self, streams: AsyncStreamsResource) -> None:
        self._streams = streams

        self.create = async_to_streamed_response_wrapper(
            streams.create,
        )
        self.update = async_to_streamed_response_wrapper(
            streams.update,
        )
        self.list = async_to_streamed_response_wrapper(
            streams.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            streams.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            streams.get,
        )
