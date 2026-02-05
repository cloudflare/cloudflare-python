# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import typing_extensions
from typing import Type, Iterable, cast

import httpx

from .sinks import (
    SinksResource,
    AsyncSinksResource,
    SinksResourceWithRawResponse,
    AsyncSinksResourceWithRawResponse,
    SinksResourceWithStreamingResponse,
    AsyncSinksResourceWithStreamingResponse,
)
from .streams import (
    StreamsResource,
    AsyncStreamsResource,
    StreamsResourceWithRawResponse,
    AsyncStreamsResourceWithRawResponse,
    StreamsResourceWithStreamingResponse,
    AsyncStreamsResourceWithStreamingResponse,
)
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
from ...types.pipelines import (
    pipeline_list_params,
    pipeline_create_params,
    pipeline_update_params,
    pipeline_list_v1_params,
    pipeline_create_v1_params,
    pipeline_validate_sql_params,
)
from ...types.pipelines.pipeline_get_response import PipelineGetResponse
from ...types.pipelines.pipeline_list_response import PipelineListResponse
from ...types.pipelines.pipeline_create_response import PipelineCreateResponse
from ...types.pipelines.pipeline_get_v1_response import PipelineGetV1Response
from ...types.pipelines.pipeline_update_response import PipelineUpdateResponse
from ...types.pipelines.pipeline_list_v1_response import PipelineListV1Response
from ...types.pipelines.pipeline_create_v1_response import PipelineCreateV1Response
from ...types.pipelines.pipeline_validate_sql_response import PipelineValidateSqlResponse

__all__ = ["PipelinesResource", "AsyncPipelinesResource"]


class PipelinesResource(SyncAPIResource):
    @cached_property
    def sinks(self) -> SinksResource:
        return SinksResource(self._client)

    @cached_property
    def streams(self) -> StreamsResource:
        return StreamsResource(self._client)

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

    @typing_extensions.deprecated("Use create_v1 instead. This endpoint will be removed in the future.")
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PipelineCreateResponse:
        """[DEPRECATED] Create a new pipeline.

        Use the new /pipelines/v1/pipelines endpoint
        instead.

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

    @typing_extensions.deprecated("The v1 API does not support updates. This endpoint will be removed in the future.")
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PipelineUpdateResponse:
        """[DEPRECATED] Update an existing pipeline.

        Use the new /pipelines/v1/pipelines
        endpoint instead.

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

    @typing_extensions.deprecated("Use list_v1 instead. This endpoint will be removed in the future.")
    def list(
        self,
        *,
        account_id: str,
        page: str | Omit = omit,
        per_page: str | Omit = omit,
        search: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PipelineListResponse:
        """[DEPRECATED] List, filter, and paginate pipelines in an account.

        Use the new
        /pipelines/v1/pipelines endpoint instead.

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

    @typing_extensions.deprecated("Use delete_v1 instead. This endpoint will be removed in the future.")
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """[DEPRECATED] Delete a pipeline.

        Use the new /pipelines/v1/pipelines endpoint
        instead.

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

    def create_v1(
        self,
        *,
        account_id: str,
        name: str,
        sql: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PipelineCreateV1Response:
        """
        Create a new Pipeline.

        Args:
          account_id: Specifies the public ID of the account.

          name: Specifies the name of the Pipeline.

          sql: Specifies SQL for the Pipeline processing flow.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._post(
            f"/accounts/{account_id}/pipelines/v1/pipelines",
            body=maybe_transform(
                {
                    "name": name,
                    "sql": sql,
                },
                pipeline_create_v1_params.PipelineCreateV1Params,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[PipelineCreateV1Response]._unwrapper,
            ),
            cast_to=cast(Type[PipelineCreateV1Response], ResultWrapper[PipelineCreateV1Response]),
        )

    def delete_v1(
        self,
        pipeline_id: str,
        *,
        account_id: str,
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

          pipeline_id: Specifies the public ID of the pipeline.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not pipeline_id:
            raise ValueError(f"Expected a non-empty value for `pipeline_id` but received {pipeline_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/accounts/{account_id}/pipelines/v1/pipelines/{pipeline_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    @typing_extensions.deprecated("Use get_v1 instead. This endpoint will be removed in the future.")
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PipelineGetResponse:
        """[DEPRECATED] Get configuration of a pipeline.

        Use the new
        /pipelines/v1/pipelines endpoint instead.

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

    def get_v1(
        self,
        pipeline_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PipelineGetV1Response:
        """
        Get Pipelines Details.

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
        if not pipeline_id:
            raise ValueError(f"Expected a non-empty value for `pipeline_id` but received {pipeline_id!r}")
        return self._get(
            f"/accounts/{account_id}/pipelines/v1/pipelines/{pipeline_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[PipelineGetV1Response]._unwrapper,
            ),
            cast_to=cast(Type[PipelineGetV1Response], ResultWrapper[PipelineGetV1Response]),
        )

    def list_v1(
        self,
        *,
        account_id: str,
        page: float | Omit = omit,
        per_page: float | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncV4PagePaginationArray[PipelineListV1Response]:
        """
        List/Filter Pipelines in Account.

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
            f"/accounts/{account_id}/pipelines/v1/pipelines",
            page=SyncV4PagePaginationArray[PipelineListV1Response],
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
                    pipeline_list_v1_params.PipelineListV1Params,
                ),
            ),
            model=PipelineListV1Response,
        )

    def validate_sql(
        self,
        *,
        account_id: str,
        sql: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PipelineValidateSqlResponse:
        """
        Validate Arroyo SQL.

        Args:
          account_id: Specifies the public ID of the account.

          sql: Specifies SQL to validate.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._post(
            f"/accounts/{account_id}/pipelines/v1/validate_sql",
            body=maybe_transform({"sql": sql}, pipeline_validate_sql_params.PipelineValidateSqlParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[PipelineValidateSqlResponse]._unwrapper,
            ),
            cast_to=cast(Type[PipelineValidateSqlResponse], ResultWrapper[PipelineValidateSqlResponse]),
        )


class AsyncPipelinesResource(AsyncAPIResource):
    @cached_property
    def sinks(self) -> AsyncSinksResource:
        return AsyncSinksResource(self._client)

    @cached_property
    def streams(self) -> AsyncStreamsResource:
        return AsyncStreamsResource(self._client)

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

    @typing_extensions.deprecated("Use create_v1 instead. This endpoint will be removed in the future.")
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PipelineCreateResponse:
        """[DEPRECATED] Create a new pipeline.

        Use the new /pipelines/v1/pipelines endpoint
        instead.

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

    @typing_extensions.deprecated("The v1 API does not support updates. This endpoint will be removed in the future.")
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PipelineUpdateResponse:
        """[DEPRECATED] Update an existing pipeline.

        Use the new /pipelines/v1/pipelines
        endpoint instead.

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

    @typing_extensions.deprecated("Use list_v1 instead. This endpoint will be removed in the future.")
    async def list(
        self,
        *,
        account_id: str,
        page: str | Omit = omit,
        per_page: str | Omit = omit,
        search: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PipelineListResponse:
        """[DEPRECATED] List, filter, and paginate pipelines in an account.

        Use the new
        /pipelines/v1/pipelines endpoint instead.

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

    @typing_extensions.deprecated("Use delete_v1 instead. This endpoint will be removed in the future.")
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """[DEPRECATED] Delete a pipeline.

        Use the new /pipelines/v1/pipelines endpoint
        instead.

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

    async def create_v1(
        self,
        *,
        account_id: str,
        name: str,
        sql: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PipelineCreateV1Response:
        """
        Create a new Pipeline.

        Args:
          account_id: Specifies the public ID of the account.

          name: Specifies the name of the Pipeline.

          sql: Specifies SQL for the Pipeline processing flow.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._post(
            f"/accounts/{account_id}/pipelines/v1/pipelines",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "sql": sql,
                },
                pipeline_create_v1_params.PipelineCreateV1Params,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[PipelineCreateV1Response]._unwrapper,
            ),
            cast_to=cast(Type[PipelineCreateV1Response], ResultWrapper[PipelineCreateV1Response]),
        )

    async def delete_v1(
        self,
        pipeline_id: str,
        *,
        account_id: str,
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

          pipeline_id: Specifies the public ID of the pipeline.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not pipeline_id:
            raise ValueError(f"Expected a non-empty value for `pipeline_id` but received {pipeline_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/accounts/{account_id}/pipelines/v1/pipelines/{pipeline_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    @typing_extensions.deprecated("Use get_v1 instead. This endpoint will be removed in the future.")
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PipelineGetResponse:
        """[DEPRECATED] Get configuration of a pipeline.

        Use the new
        /pipelines/v1/pipelines endpoint instead.

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

    async def get_v1(
        self,
        pipeline_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PipelineGetV1Response:
        """
        Get Pipelines Details.

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
        if not pipeline_id:
            raise ValueError(f"Expected a non-empty value for `pipeline_id` but received {pipeline_id!r}")
        return await self._get(
            f"/accounts/{account_id}/pipelines/v1/pipelines/{pipeline_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[PipelineGetV1Response]._unwrapper,
            ),
            cast_to=cast(Type[PipelineGetV1Response], ResultWrapper[PipelineGetV1Response]),
        )

    def list_v1(
        self,
        *,
        account_id: str,
        page: float | Omit = omit,
        per_page: float | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[PipelineListV1Response, AsyncV4PagePaginationArray[PipelineListV1Response]]:
        """
        List/Filter Pipelines in Account.

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
            f"/accounts/{account_id}/pipelines/v1/pipelines",
            page=AsyncV4PagePaginationArray[PipelineListV1Response],
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
                    pipeline_list_v1_params.PipelineListV1Params,
                ),
            ),
            model=PipelineListV1Response,
        )

    async def validate_sql(
        self,
        *,
        account_id: str,
        sql: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PipelineValidateSqlResponse:
        """
        Validate Arroyo SQL.

        Args:
          account_id: Specifies the public ID of the account.

          sql: Specifies SQL to validate.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._post(
            f"/accounts/{account_id}/pipelines/v1/validate_sql",
            body=await async_maybe_transform({"sql": sql}, pipeline_validate_sql_params.PipelineValidateSqlParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[PipelineValidateSqlResponse]._unwrapper,
            ),
            cast_to=cast(Type[PipelineValidateSqlResponse], ResultWrapper[PipelineValidateSqlResponse]),
        )


class PipelinesResourceWithRawResponse:
    def __init__(self, pipelines: PipelinesResource) -> None:
        self._pipelines = pipelines

        self.create = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                pipelines.create,  # pyright: ignore[reportDeprecated],
            )
        )
        self.update = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                pipelines.update,  # pyright: ignore[reportDeprecated],
            )
        )
        self.list = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                pipelines.list,  # pyright: ignore[reportDeprecated],
            )
        )
        self.delete = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                pipelines.delete,  # pyright: ignore[reportDeprecated],
            )
        )
        self.create_v1 = to_raw_response_wrapper(
            pipelines.create_v1,
        )
        self.delete_v1 = to_raw_response_wrapper(
            pipelines.delete_v1,
        )
        self.get = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                pipelines.get,  # pyright: ignore[reportDeprecated],
            )
        )
        self.get_v1 = to_raw_response_wrapper(
            pipelines.get_v1,
        )
        self.list_v1 = to_raw_response_wrapper(
            pipelines.list_v1,
        )
        self.validate_sql = to_raw_response_wrapper(
            pipelines.validate_sql,
        )

    @cached_property
    def sinks(self) -> SinksResourceWithRawResponse:
        return SinksResourceWithRawResponse(self._pipelines.sinks)

    @cached_property
    def streams(self) -> StreamsResourceWithRawResponse:
        return StreamsResourceWithRawResponse(self._pipelines.streams)


class AsyncPipelinesResourceWithRawResponse:
    def __init__(self, pipelines: AsyncPipelinesResource) -> None:
        self._pipelines = pipelines

        self.create = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                pipelines.create,  # pyright: ignore[reportDeprecated],
            )
        )
        self.update = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                pipelines.update,  # pyright: ignore[reportDeprecated],
            )
        )
        self.list = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                pipelines.list,  # pyright: ignore[reportDeprecated],
            )
        )
        self.delete = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                pipelines.delete,  # pyright: ignore[reportDeprecated],
            )
        )
        self.create_v1 = async_to_raw_response_wrapper(
            pipelines.create_v1,
        )
        self.delete_v1 = async_to_raw_response_wrapper(
            pipelines.delete_v1,
        )
        self.get = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                pipelines.get,  # pyright: ignore[reportDeprecated],
            )
        )
        self.get_v1 = async_to_raw_response_wrapper(
            pipelines.get_v1,
        )
        self.list_v1 = async_to_raw_response_wrapper(
            pipelines.list_v1,
        )
        self.validate_sql = async_to_raw_response_wrapper(
            pipelines.validate_sql,
        )

    @cached_property
    def sinks(self) -> AsyncSinksResourceWithRawResponse:
        return AsyncSinksResourceWithRawResponse(self._pipelines.sinks)

    @cached_property
    def streams(self) -> AsyncStreamsResourceWithRawResponse:
        return AsyncStreamsResourceWithRawResponse(self._pipelines.streams)


class PipelinesResourceWithStreamingResponse:
    def __init__(self, pipelines: PipelinesResource) -> None:
        self._pipelines = pipelines

        self.create = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                pipelines.create,  # pyright: ignore[reportDeprecated],
            )
        )
        self.update = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                pipelines.update,  # pyright: ignore[reportDeprecated],
            )
        )
        self.list = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                pipelines.list,  # pyright: ignore[reportDeprecated],
            )
        )
        self.delete = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                pipelines.delete,  # pyright: ignore[reportDeprecated],
            )
        )
        self.create_v1 = to_streamed_response_wrapper(
            pipelines.create_v1,
        )
        self.delete_v1 = to_streamed_response_wrapper(
            pipelines.delete_v1,
        )
        self.get = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                pipelines.get,  # pyright: ignore[reportDeprecated],
            )
        )
        self.get_v1 = to_streamed_response_wrapper(
            pipelines.get_v1,
        )
        self.list_v1 = to_streamed_response_wrapper(
            pipelines.list_v1,
        )
        self.validate_sql = to_streamed_response_wrapper(
            pipelines.validate_sql,
        )

    @cached_property
    def sinks(self) -> SinksResourceWithStreamingResponse:
        return SinksResourceWithStreamingResponse(self._pipelines.sinks)

    @cached_property
    def streams(self) -> StreamsResourceWithStreamingResponse:
        return StreamsResourceWithStreamingResponse(self._pipelines.streams)


class AsyncPipelinesResourceWithStreamingResponse:
    def __init__(self, pipelines: AsyncPipelinesResource) -> None:
        self._pipelines = pipelines

        self.create = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                pipelines.create,  # pyright: ignore[reportDeprecated],
            )
        )
        self.update = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                pipelines.update,  # pyright: ignore[reportDeprecated],
            )
        )
        self.list = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                pipelines.list,  # pyright: ignore[reportDeprecated],
            )
        )
        self.delete = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                pipelines.delete,  # pyright: ignore[reportDeprecated],
            )
        )
        self.create_v1 = async_to_streamed_response_wrapper(
            pipelines.create_v1,
        )
        self.delete_v1 = async_to_streamed_response_wrapper(
            pipelines.delete_v1,
        )
        self.get = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                pipelines.get,  # pyright: ignore[reportDeprecated],
            )
        )
        self.get_v1 = async_to_streamed_response_wrapper(
            pipelines.get_v1,
        )
        self.list_v1 = async_to_streamed_response_wrapper(
            pipelines.list_v1,
        )
        self.validate_sql = async_to_streamed_response_wrapper(
            pipelines.validate_sql,
        )

    @cached_property
    def sinks(self) -> AsyncSinksResourceWithStreamingResponse:
        return AsyncSinksResourceWithStreamingResponse(self._pipelines.sinks)

    @cached_property
    def streams(self) -> AsyncStreamsResourceWithStreamingResponse:
        return AsyncStreamsResourceWithStreamingResponse(self._pipelines.streams)
