# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import typing_extensions

import httpx

from .tags import (
    TagsResource,
    AsyncTagsResource,
    TagsResourceWithRawResponse,
    AsyncTagsResourceWithRawResponse,
    TagsResourceWithStreamingResponse,
    AsyncTagsResourceWithStreamingResponse,
)
from ......_types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ......_utils import path_template, maybe_transform, async_maybe_transform
from ......_compat import cached_property
from ......_resource import SyncAPIResource, AsyncAPIResource
from ......_response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ......_base_client import make_request_options
from ......types.cloudforce_one.threat_events.indicators import by_dataset_list_params
from ......types.cloudforce_one.threat_events.indicators.by_dataset_get_response import ByDatasetGetResponse
from ......types.cloudforce_one.threat_events.indicators.by_dataset_list_response import ByDatasetListResponse

__all__ = ["ByDatasetResource", "AsyncByDatasetResource"]


class ByDatasetResource(SyncAPIResource):
    @cached_property
    def tags(self) -> TagsResource:
        return TagsResource(self._client)

    @cached_property
    def with_raw_response(self) -> ByDatasetResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return ByDatasetResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ByDatasetResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return ByDatasetResourceWithStreamingResponse(self)

    @typing_extensions.deprecated(
        "Use indicators.list instead (GET /accounts/{account_id}/cloudforce-one/events/indicators)."
    )
    def list(
        self,
        dataset_id: str,
        *,
        account_id: str,
        indicator_type: str | Omit = omit,
        name: str | Omit = omit,
        page: float | Omit = omit,
        page_size: float | Omit = omit,
        related_event: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ByDatasetListResponse:
        """This method is deprecated.

        Please use /events/indicators to retrieve a paginated
        list of indicators.

        Args:
          account_id: Account ID.

          dataset_id: Dataset UUID.

          name: Filter by indicator value (substring match)

          related_event: Filter indicators by related event UUID(s). Multiple UUIDs can be provided by
              repeating the parameter.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not dataset_id:
            raise ValueError(f"Expected a non-empty value for `dataset_id` but received {dataset_id!r}")
        return self._get(
            path_template(
                "/accounts/{account_id}/cloudforce-one/events/dataset/{dataset_id}/indicators",
                account_id=account_id,
                dataset_id=dataset_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "indicator_type": indicator_type,
                        "name": name,
                        "page": page,
                        "page_size": page_size,
                        "related_event": related_event,
                    },
                    by_dataset_list_params.ByDatasetListParams,
                ),
            ),
            cast_to=ByDatasetListResponse,
        )

    def get(
        self,
        indicator_id: str,
        *,
        account_id: str,
        dataset_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ByDatasetGetResponse:
        """
        Retrieves a specific indicator by its UUID.

        Args:
          account_id: Account ID.

          dataset_id: Dataset ID.

          indicator_id: Indicator UUID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not dataset_id:
            raise ValueError(f"Expected a non-empty value for `dataset_id` but received {dataset_id!r}")
        if not indicator_id:
            raise ValueError(f"Expected a non-empty value for `indicator_id` but received {indicator_id!r}")
        return self._get(
            path_template(
                "/accounts/{account_id}/cloudforce-one/events/dataset/{dataset_id}/indicators/{indicator_id}",
                account_id=account_id,
                dataset_id=dataset_id,
                indicator_id=indicator_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ByDatasetGetResponse,
        )


class AsyncByDatasetResource(AsyncAPIResource):
    @cached_property
    def tags(self) -> AsyncTagsResource:
        return AsyncTagsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncByDatasetResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncByDatasetResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncByDatasetResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncByDatasetResourceWithStreamingResponse(self)

    @typing_extensions.deprecated(
        "Use indicators.list instead (GET /accounts/{account_id}/cloudforce-one/events/indicators)."
    )
    async def list(
        self,
        dataset_id: str,
        *,
        account_id: str,
        indicator_type: str | Omit = omit,
        name: str | Omit = omit,
        page: float | Omit = omit,
        page_size: float | Omit = omit,
        related_event: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ByDatasetListResponse:
        """This method is deprecated.

        Please use /events/indicators to retrieve a paginated
        list of indicators.

        Args:
          account_id: Account ID.

          dataset_id: Dataset UUID.

          name: Filter by indicator value (substring match)

          related_event: Filter indicators by related event UUID(s). Multiple UUIDs can be provided by
              repeating the parameter.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not dataset_id:
            raise ValueError(f"Expected a non-empty value for `dataset_id` but received {dataset_id!r}")
        return await self._get(
            path_template(
                "/accounts/{account_id}/cloudforce-one/events/dataset/{dataset_id}/indicators",
                account_id=account_id,
                dataset_id=dataset_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "indicator_type": indicator_type,
                        "name": name,
                        "page": page,
                        "page_size": page_size,
                        "related_event": related_event,
                    },
                    by_dataset_list_params.ByDatasetListParams,
                ),
            ),
            cast_to=ByDatasetListResponse,
        )

    async def get(
        self,
        indicator_id: str,
        *,
        account_id: str,
        dataset_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ByDatasetGetResponse:
        """
        Retrieves a specific indicator by its UUID.

        Args:
          account_id: Account ID.

          dataset_id: Dataset ID.

          indicator_id: Indicator UUID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not dataset_id:
            raise ValueError(f"Expected a non-empty value for `dataset_id` but received {dataset_id!r}")
        if not indicator_id:
            raise ValueError(f"Expected a non-empty value for `indicator_id` but received {indicator_id!r}")
        return await self._get(
            path_template(
                "/accounts/{account_id}/cloudforce-one/events/dataset/{dataset_id}/indicators/{indicator_id}",
                account_id=account_id,
                dataset_id=dataset_id,
                indicator_id=indicator_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ByDatasetGetResponse,
        )


class ByDatasetResourceWithRawResponse:
    def __init__(self, by_dataset: ByDatasetResource) -> None:
        self._by_dataset = by_dataset

        self.list = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                by_dataset.list,  # pyright: ignore[reportDeprecated],
            )
        )
        self.get = to_raw_response_wrapper(
            by_dataset.get,
        )

    @cached_property
    def tags(self) -> TagsResourceWithRawResponse:
        return TagsResourceWithRawResponse(self._by_dataset.tags)


class AsyncByDatasetResourceWithRawResponse:
    def __init__(self, by_dataset: AsyncByDatasetResource) -> None:
        self._by_dataset = by_dataset

        self.list = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                by_dataset.list,  # pyright: ignore[reportDeprecated],
            )
        )
        self.get = async_to_raw_response_wrapper(
            by_dataset.get,
        )

    @cached_property
    def tags(self) -> AsyncTagsResourceWithRawResponse:
        return AsyncTagsResourceWithRawResponse(self._by_dataset.tags)


class ByDatasetResourceWithStreamingResponse:
    def __init__(self, by_dataset: ByDatasetResource) -> None:
        self._by_dataset = by_dataset

        self.list = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                by_dataset.list,  # pyright: ignore[reportDeprecated],
            )
        )
        self.get = to_streamed_response_wrapper(
            by_dataset.get,
        )

    @cached_property
    def tags(self) -> TagsResourceWithStreamingResponse:
        return TagsResourceWithStreamingResponse(self._by_dataset.tags)


class AsyncByDatasetResourceWithStreamingResponse:
    def __init__(self, by_dataset: AsyncByDatasetResource) -> None:
        self._by_dataset = by_dataset

        self.list = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                by_dataset.list,  # pyright: ignore[reportDeprecated],
            )
        )
        self.get = async_to_streamed_response_wrapper(
            by_dataset.get,
        )

    @cached_property
    def tags(self) -> AsyncTagsResourceWithStreamingResponse:
        return AsyncTagsResourceWithStreamingResponse(self._by_dataset.tags)
