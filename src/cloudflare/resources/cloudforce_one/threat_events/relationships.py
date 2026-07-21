# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ...._utils import path_template, maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.cloudforce_one.threat_events import relationship_list_params
from ....types.cloudforce_one.threat_events.relationship_list_response import RelationshipListResponse

__all__ = ["RelationshipsResource", "AsyncRelationshipsResource"]


class RelationshipsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RelationshipsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return RelationshipsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RelationshipsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return RelationshipsResourceWithStreamingResponse(self)

    def list(
        self,
        event_id: str,
        *,
        account_id: str,
        dataset_id: str,
        direction: Literal["ancestors", "descendants", "both"] | Omit = omit,
        include_parent: bool | Omit = omit,
        indicator_type_ids: SequenceNotStr[str] | Omit = omit,
        max_depth: float | Omit = omit,
        page: float | Omit = omit,
        page_size: float | Omit = omit,
        relationship_types: Union[str, SequenceNotStr[str]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RelationshipListResponse:
        """
        The `event_id` must be defined (to list existing events (and their IDs), use the
        [`Filter and List Events`](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_events/methods/list/)
        endpoint). Also, must provide query parameters.

        Args:
          account_id: Account ID.

          event_id: Event UUID.

          dataset_id: The dataset ID to search within.

          direction: The direction to traverse the graph. Defaults to 'both' to search all.

          include_parent: Whether to include the starting event in the results. Defaults to true.

          indicator_type_ids: An optional array of indicator type IDs to filter the results by.

          max_depth: The maximum depth to traverse. Defaults to 5.

          relationship_types: An optional array of relationship types to filter by.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not event_id:
            raise ValueError(f"Expected a non-empty value for `event_id` but received {event_id!r}")
        return self._get(
            path_template(
                "/accounts/{account_id}/cloudforce-one/events/{event_id}/relationships",
                account_id=account_id,
                event_id=event_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "dataset_id": dataset_id,
                        "direction": direction,
                        "include_parent": include_parent,
                        "indicator_type_ids": indicator_type_ids,
                        "max_depth": max_depth,
                        "page": page,
                        "page_size": page_size,
                        "relationship_types": relationship_types,
                    },
                    relationship_list_params.RelationshipListParams,
                ),
            ),
            cast_to=RelationshipListResponse,
        )


class AsyncRelationshipsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRelationshipsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRelationshipsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRelationshipsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncRelationshipsResourceWithStreamingResponse(self)

    async def list(
        self,
        event_id: str,
        *,
        account_id: str,
        dataset_id: str,
        direction: Literal["ancestors", "descendants", "both"] | Omit = omit,
        include_parent: bool | Omit = omit,
        indicator_type_ids: SequenceNotStr[str] | Omit = omit,
        max_depth: float | Omit = omit,
        page: float | Omit = omit,
        page_size: float | Omit = omit,
        relationship_types: Union[str, SequenceNotStr[str]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RelationshipListResponse:
        """
        The `event_id` must be defined (to list existing events (and their IDs), use the
        [`Filter and List Events`](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_events/methods/list/)
        endpoint). Also, must provide query parameters.

        Args:
          account_id: Account ID.

          event_id: Event UUID.

          dataset_id: The dataset ID to search within.

          direction: The direction to traverse the graph. Defaults to 'both' to search all.

          include_parent: Whether to include the starting event in the results. Defaults to true.

          indicator_type_ids: An optional array of indicator type IDs to filter the results by.

          max_depth: The maximum depth to traverse. Defaults to 5.

          relationship_types: An optional array of relationship types to filter by.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not event_id:
            raise ValueError(f"Expected a non-empty value for `event_id` but received {event_id!r}")
        return await self._get(
            path_template(
                "/accounts/{account_id}/cloudforce-one/events/{event_id}/relationships",
                account_id=account_id,
                event_id=event_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "dataset_id": dataset_id,
                        "direction": direction,
                        "include_parent": include_parent,
                        "indicator_type_ids": indicator_type_ids,
                        "max_depth": max_depth,
                        "page": page,
                        "page_size": page_size,
                        "relationship_types": relationship_types,
                    },
                    relationship_list_params.RelationshipListParams,
                ),
            ),
            cast_to=RelationshipListResponse,
        )


class RelationshipsResourceWithRawResponse:
    def __init__(self, relationships: RelationshipsResource) -> None:
        self._relationships = relationships

        self.list = to_raw_response_wrapper(
            relationships.list,
        )


class AsyncRelationshipsResourceWithRawResponse:
    def __init__(self, relationships: AsyncRelationshipsResource) -> None:
        self._relationships = relationships

        self.list = async_to_raw_response_wrapper(
            relationships.list,
        )


class RelationshipsResourceWithStreamingResponse:
    def __init__(self, relationships: RelationshipsResource) -> None:
        self._relationships = relationships

        self.list = to_streamed_response_wrapper(
            relationships.list,
        )


class AsyncRelationshipsResourceWithStreamingResponse:
    def __init__(self, relationships: AsyncRelationshipsResource) -> None:
        self._relationships = relationships

        self.list = async_to_streamed_response_wrapper(
            relationships.list,
        )
