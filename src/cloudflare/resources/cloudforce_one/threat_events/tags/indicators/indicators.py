# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable

import httpx

from .by_dataset import (
    ByDatasetResource,
    AsyncByDatasetResource,
    ByDatasetResourceWithRawResponse,
    AsyncByDatasetResourceWithRawResponse,
    ByDatasetResourceWithStreamingResponse,
    AsyncByDatasetResourceWithStreamingResponse,
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
from ......types.cloudforce_one.threat_events.tags import indicator_list_params
from ......types.cloudforce_one.threat_events.tags.indicator_list_response import IndicatorListResponse

__all__ = ["IndicatorsResource", "AsyncIndicatorsResource"]


class IndicatorsResource(SyncAPIResource):
    @cached_property
    def by_dataset(self) -> ByDatasetResource:
        return ByDatasetResource(self._client)

    @cached_property
    def with_raw_response(self) -> IndicatorsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return IndicatorsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> IndicatorsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return IndicatorsResourceWithStreamingResponse(self)

    def list(
        self,
        tag_uuid: str,
        *,
        account_id: str,
        dataset_ids: SequenceNotStr[str] | Omit = omit,
        indicator_type: str | Omit = omit,
        page: float | Omit = omit,
        page_size: float | Omit = omit,
        related_event: SequenceNotStr[str] | Omit = omit,
        search: Iterable[indicator_list_params.Search] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IndicatorListResponse:
        """Returns indicators associated with the provided tag UUID, with pagination.

        By
        default fans out across every indicator dataset the account can read; pass
        datasetIds to scope to specific datasets.

        Args:
          account_id: Account ID.

          tag_uuid: Tag UUID.

          dataset_ids: Dataset UUIDs to scope to (repeat the param for multiple), or 'all' / '\\**' for
              every readable indicator dataset. Omit to search all readable datasets.

          related_event: Filter indicators by related event UUID(s). Multiple UUIDs can be provided by
              repeating the parameter.

          search: Structured search as a JSON array of {field, op, value} objects. Searchable
              fields: value, indicatorType. Multiple conditions are AND'd together. Max 10
              conditions per request.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not tag_uuid:
            raise ValueError(f"Expected a non-empty value for `tag_uuid` but received {tag_uuid!r}")
        return self._get(
            path_template(
                "/accounts/{account_id}/cloudforce-one/events/tags/{tag_uuid}/indicators",
                account_id=account_id,
                tag_uuid=tag_uuid,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "dataset_ids": dataset_ids,
                        "indicator_type": indicator_type,
                        "page": page,
                        "page_size": page_size,
                        "related_event": related_event,
                        "search": search,
                    },
                    indicator_list_params.IndicatorListParams,
                ),
            ),
            cast_to=IndicatorListResponse,
        )


class AsyncIndicatorsResource(AsyncAPIResource):
    @cached_property
    def by_dataset(self) -> AsyncByDatasetResource:
        return AsyncByDatasetResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncIndicatorsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncIndicatorsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncIndicatorsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncIndicatorsResourceWithStreamingResponse(self)

    async def list(
        self,
        tag_uuid: str,
        *,
        account_id: str,
        dataset_ids: SequenceNotStr[str] | Omit = omit,
        indicator_type: str | Omit = omit,
        page: float | Omit = omit,
        page_size: float | Omit = omit,
        related_event: SequenceNotStr[str] | Omit = omit,
        search: Iterable[indicator_list_params.Search] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IndicatorListResponse:
        """Returns indicators associated with the provided tag UUID, with pagination.

        By
        default fans out across every indicator dataset the account can read; pass
        datasetIds to scope to specific datasets.

        Args:
          account_id: Account ID.

          tag_uuid: Tag UUID.

          dataset_ids: Dataset UUIDs to scope to (repeat the param for multiple), or 'all' / '\\**' for
              every readable indicator dataset. Omit to search all readable datasets.

          related_event: Filter indicators by related event UUID(s). Multiple UUIDs can be provided by
              repeating the parameter.

          search: Structured search as a JSON array of {field, op, value} objects. Searchable
              fields: value, indicatorType. Multiple conditions are AND'd together. Max 10
              conditions per request.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not tag_uuid:
            raise ValueError(f"Expected a non-empty value for `tag_uuid` but received {tag_uuid!r}")
        return await self._get(
            path_template(
                "/accounts/{account_id}/cloudforce-one/events/tags/{tag_uuid}/indicators",
                account_id=account_id,
                tag_uuid=tag_uuid,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "dataset_ids": dataset_ids,
                        "indicator_type": indicator_type,
                        "page": page,
                        "page_size": page_size,
                        "related_event": related_event,
                        "search": search,
                    },
                    indicator_list_params.IndicatorListParams,
                ),
            ),
            cast_to=IndicatorListResponse,
        )


class IndicatorsResourceWithRawResponse:
    def __init__(self, indicators: IndicatorsResource) -> None:
        self._indicators = indicators

        self.list = to_raw_response_wrapper(
            indicators.list,
        )

    @cached_property
    def by_dataset(self) -> ByDatasetResourceWithRawResponse:
        return ByDatasetResourceWithRawResponse(self._indicators.by_dataset)


class AsyncIndicatorsResourceWithRawResponse:
    def __init__(self, indicators: AsyncIndicatorsResource) -> None:
        self._indicators = indicators

        self.list = async_to_raw_response_wrapper(
            indicators.list,
        )

    @cached_property
    def by_dataset(self) -> AsyncByDatasetResourceWithRawResponse:
        return AsyncByDatasetResourceWithRawResponse(self._indicators.by_dataset)


class IndicatorsResourceWithStreamingResponse:
    def __init__(self, indicators: IndicatorsResource) -> None:
        self._indicators = indicators

        self.list = to_streamed_response_wrapper(
            indicators.list,
        )

    @cached_property
    def by_dataset(self) -> ByDatasetResourceWithStreamingResponse:
        return ByDatasetResourceWithStreamingResponse(self._indicators.by_dataset)


class AsyncIndicatorsResourceWithStreamingResponse:
    def __init__(self, indicators: AsyncIndicatorsResource) -> None:
        self._indicators = indicators

        self.list = async_to_streamed_response_wrapper(
            indicators.list,
        )

    @cached_property
    def by_dataset(self) -> AsyncByDatasetResourceWithStreamingResponse:
        return AsyncByDatasetResourceWithStreamingResponse(self._indicators.by_dataset)
