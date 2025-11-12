# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, cast
from typing_extensions import Literal

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
from ...types.pipelines import sink_list_params, sink_create_params, sink_delete_params
from ...types.pipelines.sink_get_response import SinkGetResponse
from ...types.pipelines.sink_list_response import SinkListResponse
from ...types.pipelines.sink_create_response import SinkCreateResponse

__all__ = ["SinksResource", "AsyncSinksResource"]


class SinksResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SinksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return SinksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SinksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return SinksResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        account_id: str,
        name: str,
        type: Literal["r2", "r2_data_catalog"],
        config: sink_create_params.Config | Omit = omit,
        format: sink_create_params.Format | Omit = omit,
        schema: sink_create_params.Schema | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SinkCreateResponse:
        """
        Create a new Sink.

        Args:
          account_id: Specifies the public ID of the account.

          name: Defines the name of the Sink.

          type: Specifies the type of sink.

          config: Defines the configuration of the R2 Sink.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._post(
            f"/accounts/{account_id}/pipelines/v1/sinks",
            body=maybe_transform(
                {
                    "name": name,
                    "type": type,
                    "config": config,
                    "format": format,
                    "schema": schema,
                },
                sink_create_params.SinkCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[SinkCreateResponse]._unwrapper,
            ),
            cast_to=cast(Type[SinkCreateResponse], ResultWrapper[SinkCreateResponse]),
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
    ) -> SyncV4PagePaginationArray[SinkListResponse]:
        """
        List/Filter Sinks in Account.

        Args:
          account_id: Specifies the public ID of the account.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/pipelines/v1/sinks",
            page=SyncV4PagePaginationArray[SinkListResponse],
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
                    sink_list_params.SinkListParams,
                ),
            ),
            model=SinkListResponse,
        )

    def delete(
        self,
        sink_id: str,
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
        Delete Pipeline in Account.

        Args:
          account_id: Specifies the public ID of the account.

          sink_id: Specifies the publid ID of the sink.

          force: Delete sink forcefully, including deleting any dependent pipelines.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not sink_id:
            raise ValueError(f"Expected a non-empty value for `sink_id` but received {sink_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/accounts/{account_id}/pipelines/v1/sinks/{sink_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"force": force}, sink_delete_params.SinkDeleteParams),
            ),
            cast_to=NoneType,
        )

    def get(
        self,
        sink_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SinkGetResponse:
        """
        Get Sink Details.

        Args:
          account_id: Specifies the public ID of the account.

          sink_id: Specifies the publid ID of the sink.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not sink_id:
            raise ValueError(f"Expected a non-empty value for `sink_id` but received {sink_id!r}")
        return self._get(
            f"/accounts/{account_id}/pipelines/v1/sinks/{sink_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[SinkGetResponse]._unwrapper,
            ),
            cast_to=cast(Type[SinkGetResponse], ResultWrapper[SinkGetResponse]),
        )


class AsyncSinksResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSinksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSinksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSinksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncSinksResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_id: str,
        name: str,
        type: Literal["r2", "r2_data_catalog"],
        config: sink_create_params.Config | Omit = omit,
        format: sink_create_params.Format | Omit = omit,
        schema: sink_create_params.Schema | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SinkCreateResponse:
        """
        Create a new Sink.

        Args:
          account_id: Specifies the public ID of the account.

          name: Defines the name of the Sink.

          type: Specifies the type of sink.

          config: Defines the configuration of the R2 Sink.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._post(
            f"/accounts/{account_id}/pipelines/v1/sinks",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "type": type,
                    "config": config,
                    "format": format,
                    "schema": schema,
                },
                sink_create_params.SinkCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[SinkCreateResponse]._unwrapper,
            ),
            cast_to=cast(Type[SinkCreateResponse], ResultWrapper[SinkCreateResponse]),
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
    ) -> AsyncPaginator[SinkListResponse, AsyncV4PagePaginationArray[SinkListResponse]]:
        """
        List/Filter Sinks in Account.

        Args:
          account_id: Specifies the public ID of the account.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/pipelines/v1/sinks",
            page=AsyncV4PagePaginationArray[SinkListResponse],
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
                    sink_list_params.SinkListParams,
                ),
            ),
            model=SinkListResponse,
        )

    async def delete(
        self,
        sink_id: str,
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
        Delete Pipeline in Account.

        Args:
          account_id: Specifies the public ID of the account.

          sink_id: Specifies the publid ID of the sink.

          force: Delete sink forcefully, including deleting any dependent pipelines.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not sink_id:
            raise ValueError(f"Expected a non-empty value for `sink_id` but received {sink_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/accounts/{account_id}/pipelines/v1/sinks/{sink_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"force": force}, sink_delete_params.SinkDeleteParams),
            ),
            cast_to=NoneType,
        )

    async def get(
        self,
        sink_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SinkGetResponse:
        """
        Get Sink Details.

        Args:
          account_id: Specifies the public ID of the account.

          sink_id: Specifies the publid ID of the sink.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not sink_id:
            raise ValueError(f"Expected a non-empty value for `sink_id` but received {sink_id!r}")
        return await self._get(
            f"/accounts/{account_id}/pipelines/v1/sinks/{sink_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[SinkGetResponse]._unwrapper,
            ),
            cast_to=cast(Type[SinkGetResponse], ResultWrapper[SinkGetResponse]),
        )


class SinksResourceWithRawResponse:
    def __init__(self, sinks: SinksResource) -> None:
        self._sinks = sinks

        self.create = to_raw_response_wrapper(
            sinks.create,
        )
        self.list = to_raw_response_wrapper(
            sinks.list,
        )
        self.delete = to_raw_response_wrapper(
            sinks.delete,
        )
        self.get = to_raw_response_wrapper(
            sinks.get,
        )


class AsyncSinksResourceWithRawResponse:
    def __init__(self, sinks: AsyncSinksResource) -> None:
        self._sinks = sinks

        self.create = async_to_raw_response_wrapper(
            sinks.create,
        )
        self.list = async_to_raw_response_wrapper(
            sinks.list,
        )
        self.delete = async_to_raw_response_wrapper(
            sinks.delete,
        )
        self.get = async_to_raw_response_wrapper(
            sinks.get,
        )


class SinksResourceWithStreamingResponse:
    def __init__(self, sinks: SinksResource) -> None:
        self._sinks = sinks

        self.create = to_streamed_response_wrapper(
            sinks.create,
        )
        self.list = to_streamed_response_wrapper(
            sinks.list,
        )
        self.delete = to_streamed_response_wrapper(
            sinks.delete,
        )
        self.get = to_streamed_response_wrapper(
            sinks.get,
        )


class AsyncSinksResourceWithStreamingResponse:
    def __init__(self, sinks: AsyncSinksResource) -> None:
        self._sinks = sinks

        self.create = async_to_streamed_response_wrapper(
            sinks.create,
        )
        self.list = async_to_streamed_response_wrapper(
            sinks.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            sinks.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            sinks.get,
        )
