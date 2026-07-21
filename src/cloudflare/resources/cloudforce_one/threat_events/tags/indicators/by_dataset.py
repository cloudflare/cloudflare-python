# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import typing_extensions
from typing import Iterable

import httpx

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
from ......types.cloudforce_one.threat_events.tags.indicators import by_dataset_list_params
from ......types.cloudforce_one.threat_events.tags.indicators.by_dataset_list_response import ByDatasetListResponse

__all__ = ["ByDatasetResource", "AsyncByDatasetResource"]


class ByDatasetResource(SyncAPIResource):
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
        "Use list instead (GET /accounts/{account_id}/cloudforce-one/events/tags/{tag_uuid}/indicators)."
    )
    def list(
        self,
        tag_uuid: str,
        *,
        account_id: str,
        dataset_id: str,
        indicator_type: str | Omit = omit,
        page: float | Omit = omit,
        page_size: float | Omit = omit,
        related_event: SequenceNotStr[str] | Omit = omit,
        search: Iterable[by_dataset_list_params.Search] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ByDatasetListResponse:
        """This endpoint is deprecated.

        Use GET
        /:account_id/events/tags/:tag_uuid/indicators with the optional datasetIds query
        parameter instead. Returns indicators associated with the provided tag UUID
        within a single dataset's indicator shards, with pagination.

        Args:
          account_id: Account ID.

          dataset_id: Dataset UUID.

          tag_uuid: Tag UUID.

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
        if not dataset_id:
            raise ValueError(f"Expected a non-empty value for `dataset_id` but received {dataset_id!r}")
        if not tag_uuid:
            raise ValueError(f"Expected a non-empty value for `tag_uuid` but received {tag_uuid!r}")
        return self._get(
            path_template(
                "/accounts/{account_id}/cloudforce-one/events/dataset/{dataset_id}/tags/{tag_uuid}/indicators",
                account_id=account_id,
                dataset_id=dataset_id,
                tag_uuid=tag_uuid,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "indicator_type": indicator_type,
                        "page": page,
                        "page_size": page_size,
                        "related_event": related_event,
                        "search": search,
                    },
                    by_dataset_list_params.ByDatasetListParams,
                ),
            ),
            cast_to=ByDatasetListResponse,
        )


class AsyncByDatasetResource(AsyncAPIResource):
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
        "Use list instead (GET /accounts/{account_id}/cloudforce-one/events/tags/{tag_uuid}/indicators)."
    )
    async def list(
        self,
        tag_uuid: str,
        *,
        account_id: str,
        dataset_id: str,
        indicator_type: str | Omit = omit,
        page: float | Omit = omit,
        page_size: float | Omit = omit,
        related_event: SequenceNotStr[str] | Omit = omit,
        search: Iterable[by_dataset_list_params.Search] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ByDatasetListResponse:
        """This endpoint is deprecated.

        Use GET
        /:account_id/events/tags/:tag_uuid/indicators with the optional datasetIds query
        parameter instead. Returns indicators associated with the provided tag UUID
        within a single dataset's indicator shards, with pagination.

        Args:
          account_id: Account ID.

          dataset_id: Dataset UUID.

          tag_uuid: Tag UUID.

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
        if not dataset_id:
            raise ValueError(f"Expected a non-empty value for `dataset_id` but received {dataset_id!r}")
        if not tag_uuid:
            raise ValueError(f"Expected a non-empty value for `tag_uuid` but received {tag_uuid!r}")
        return await self._get(
            path_template(
                "/accounts/{account_id}/cloudforce-one/events/dataset/{dataset_id}/tags/{tag_uuid}/indicators",
                account_id=account_id,
                dataset_id=dataset_id,
                tag_uuid=tag_uuid,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "indicator_type": indicator_type,
                        "page": page,
                        "page_size": page_size,
                        "related_event": related_event,
                        "search": search,
                    },
                    by_dataset_list_params.ByDatasetListParams,
                ),
            ),
            cast_to=ByDatasetListResponse,
        )


class ByDatasetResourceWithRawResponse:
    def __init__(self, by_dataset: ByDatasetResource) -> None:
        self._by_dataset = by_dataset

        self.list = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                by_dataset.list,  # pyright: ignore[reportDeprecated],
            )
        )


class AsyncByDatasetResourceWithRawResponse:
    def __init__(self, by_dataset: AsyncByDatasetResource) -> None:
        self._by_dataset = by_dataset

        self.list = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                by_dataset.list,  # pyright: ignore[reportDeprecated],
            )
        )


class ByDatasetResourceWithStreamingResponse:
    def __init__(self, by_dataset: ByDatasetResource) -> None:
        self._by_dataset = by_dataset

        self.list = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                by_dataset.list,  # pyright: ignore[reportDeprecated],
            )
        )


class AsyncByDatasetResourceWithStreamingResponse:
    def __init__(self, by_dataset: AsyncByDatasetResource) -> None:
        self._by_dataset = by_dataset

        self.list = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                by_dataset.list,  # pyright: ignore[reportDeprecated],
            )
        )
