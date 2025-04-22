# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Iterable, cast

import httpx

from .._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._wrappers import ResultWrapper
from .._base_client import make_request_options
from ..types.pipelines import pipeline_list_params, pipeline_create_params, pipeline_update_params
from ..types.pipelines.pipeline_get_response import PipelineGetResponse
from ..types.pipelines.pipeline_list_response import PipelineListResponse
from ..types.pipelines.pipeline_create_response import PipelineCreateResponse
from ..types.pipelines.pipeline_update_response import PipelineUpdateResponse

__all__ = ["PipelinesResource", "AsyncPipelinesResource"]


class PipelinesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PipelinesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return PipelinesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PipelinesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return PipelinesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        account_id: str,
        destination: pipeline_create_params.Destination,
        name: str,
        source: Iterable[pipeline_create_params.Source],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PipelineCreateResponse:
        """
        Create a new pipeline.

        Args:
          account_id: Specifies the public ID of the account.

          name: Defines the name of the pipeline.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._post(
            f"/accounts/{account_id}/pipelines",
            body=maybe_transform(
                {
                    "destination": destination,
                    "name": name,
                    "source": source,
                },
                pipeline_create_params.PipelineCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[PipelineCreateResponse]._unwrapper,
            ),
            cast_to=cast(Type[PipelineCreateResponse], ResultWrapper[PipelineCreateResponse]),
        )

    def update(
        self,
        pipeline_name: str,
        *,
        account_id: str,
        destination: pipeline_update_params.Destination,
        name: str,
        source: Iterable[pipeline_update_params.Source],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PipelineUpdateResponse:
        """
        Update an existing pipeline.

        Args:
          account_id: Specifies the public ID of the account.

          pipeline_name: Defines the name of the pipeline.

          name: Defines the name of the pipeline.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not pipeline_name:
            raise ValueError(f"Expected a non-empty value for `pipeline_name` but received {pipeline_name!r}")
        return self._put(
            f"/accounts/{account_id}/pipelines/{pipeline_name}",
            body=maybe_transform(
                {
                    "destination": destination,
                    "name": name,
                    "source": source,
                },
                pipeline_update_params.PipelineUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[PipelineUpdateResponse]._unwrapper,
            ),
            cast_to=cast(Type[PipelineUpdateResponse], ResultWrapper[PipelineUpdateResponse]),
        )

    def list(
        self,
        *,
        account_id: str,
        page: str | NotGiven = NOT_GIVEN,
        per_page: str | NotGiven = NOT_GIVEN,
        search: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PipelineListResponse:
        """
        List, filter, and paginate pipelines in an account.

        Args:
          account_id: Specifies the public ID of the account.

          page: Specifies which page to retrieve.

          per_page: Specifies the number of pipelines per page.

          search: Specifies the prefix of pipeline name to search.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get(
            f"/accounts/{account_id}/pipelines",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page": page,
                        "per_page": per_page,
                        "search": search,
                    },
                    pipeline_list_params.PipelineListParams,
                ),
            ),
            cast_to=PipelineListResponse,
        )

    def delete(
        self,
        pipeline_name: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Delete a pipeline.

        Args:
          account_id: Specifies the public ID of the account.

          pipeline_name: Defines the name of the pipeline.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not pipeline_name:
            raise ValueError(f"Expected a non-empty value for `pipeline_name` but received {pipeline_name!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/accounts/{account_id}/pipelines/{pipeline_name}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def get(
        self,
        pipeline_name: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PipelineGetResponse:
        """
        Get configuration of a pipeline.

        Args:
          account_id: Specifies the public ID of the account.

          pipeline_name: Defines the name of the pipeline.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not pipeline_name:
            raise ValueError(f"Expected a non-empty value for `pipeline_name` but received {pipeline_name!r}")
        return self._get(
            f"/accounts/{account_id}/pipelines/{pipeline_name}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[PipelineGetResponse]._unwrapper,
            ),
            cast_to=cast(Type[PipelineGetResponse], ResultWrapper[PipelineGetResponse]),
        )


class AsyncPipelinesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPipelinesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPipelinesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPipelinesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncPipelinesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_id: str,
        destination: pipeline_create_params.Destination,
        name: str,
        source: Iterable[pipeline_create_params.Source],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PipelineCreateResponse:
        """
        Create a new pipeline.

        Args:
          account_id: Specifies the public ID of the account.

          name: Defines the name of the pipeline.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._post(
            f"/accounts/{account_id}/pipelines",
            body=await async_maybe_transform(
                {
                    "destination": destination,
                    "name": name,
                    "source": source,
                },
                pipeline_create_params.PipelineCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[PipelineCreateResponse]._unwrapper,
            ),
            cast_to=cast(Type[PipelineCreateResponse], ResultWrapper[PipelineCreateResponse]),
        )

    async def update(
        self,
        pipeline_name: str,
        *,
        account_id: str,
        destination: pipeline_update_params.Destination,
        name: str,
        source: Iterable[pipeline_update_params.Source],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PipelineUpdateResponse:
        """
        Update an existing pipeline.

        Args:
          account_id: Specifies the public ID of the account.

          pipeline_name: Defines the name of the pipeline.

          name: Defines the name of the pipeline.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not pipeline_name:
            raise ValueError(f"Expected a non-empty value for `pipeline_name` but received {pipeline_name!r}")
        return await self._put(
            f"/accounts/{account_id}/pipelines/{pipeline_name}",
            body=await async_maybe_transform(
                {
                    "destination": destination,
                    "name": name,
                    "source": source,
                },
                pipeline_update_params.PipelineUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[PipelineUpdateResponse]._unwrapper,
            ),
            cast_to=cast(Type[PipelineUpdateResponse], ResultWrapper[PipelineUpdateResponse]),
        )

    async def list(
        self,
        *,
        account_id: str,
        page: str | NotGiven = NOT_GIVEN,
        per_page: str | NotGiven = NOT_GIVEN,
        search: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PipelineListResponse:
        """
        List, filter, and paginate pipelines in an account.

        Args:
          account_id: Specifies the public ID of the account.

          page: Specifies which page to retrieve.

          per_page: Specifies the number of pipelines per page.

          search: Specifies the prefix of pipeline name to search.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._get(
            f"/accounts/{account_id}/pipelines",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "page": page,
                        "per_page": per_page,
                        "search": search,
                    },
                    pipeline_list_params.PipelineListParams,
                ),
            ),
            cast_to=PipelineListResponse,
        )

    async def delete(
        self,
        pipeline_name: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Delete a pipeline.

        Args:
          account_id: Specifies the public ID of the account.

          pipeline_name: Defines the name of the pipeline.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not pipeline_name:
            raise ValueError(f"Expected a non-empty value for `pipeline_name` but received {pipeline_name!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/accounts/{account_id}/pipelines/{pipeline_name}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def get(
        self,
        pipeline_name: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PipelineGetResponse:
        """
        Get configuration of a pipeline.

        Args:
          account_id: Specifies the public ID of the account.

          pipeline_name: Defines the name of the pipeline.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not pipeline_name:
            raise ValueError(f"Expected a non-empty value for `pipeline_name` but received {pipeline_name!r}")
        return await self._get(
            f"/accounts/{account_id}/pipelines/{pipeline_name}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[PipelineGetResponse]._unwrapper,
            ),
            cast_to=cast(Type[PipelineGetResponse], ResultWrapper[PipelineGetResponse]),
        )


class PipelinesResourceWithRawResponse:
    def __init__(self, pipelines: PipelinesResource) -> None:
        self._pipelines = pipelines

        self.create = to_raw_response_wrapper(
            pipelines.create,
        )
        self.update = to_raw_response_wrapper(
            pipelines.update,
        )
        self.list = to_raw_response_wrapper(
            pipelines.list,
        )
        self.delete = to_raw_response_wrapper(
            pipelines.delete,
        )
        self.get = to_raw_response_wrapper(
            pipelines.get,
        )


class AsyncPipelinesResourceWithRawResponse:
    def __init__(self, pipelines: AsyncPipelinesResource) -> None:
        self._pipelines = pipelines

        self.create = async_to_raw_response_wrapper(
            pipelines.create,
        )
        self.update = async_to_raw_response_wrapper(
            pipelines.update,
        )
        self.list = async_to_raw_response_wrapper(
            pipelines.list,
        )
        self.delete = async_to_raw_response_wrapper(
            pipelines.delete,
        )
        self.get = async_to_raw_response_wrapper(
            pipelines.get,
        )


class PipelinesResourceWithStreamingResponse:
    def __init__(self, pipelines: PipelinesResource) -> None:
        self._pipelines = pipelines

        self.create = to_streamed_response_wrapper(
            pipelines.create,
        )
        self.update = to_streamed_response_wrapper(
            pipelines.update,
        )
        self.list = to_streamed_response_wrapper(
            pipelines.list,
        )
        self.delete = to_streamed_response_wrapper(
            pipelines.delete,
        )
        self.get = to_streamed_response_wrapper(
            pipelines.get,
        )


class AsyncPipelinesResourceWithStreamingResponse:
    def __init__(self, pipelines: AsyncPipelinesResource) -> None:
        self._pipelines = pipelines

        self.create = async_to_streamed_response_wrapper(
            pipelines.create,
        )
        self.update = async_to_streamed_response_wrapper(
            pipelines.update,
        )
        self.list = async_to_streamed_response_wrapper(
            pipelines.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            pipelines.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            pipelines.get,
        )
