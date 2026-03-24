# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ...._utils import maybe_transform
from .user.user import (
    UserResource,
    AsyncUserResource,
    UserResourceWithRawResponse,
    AsyncUserResourceWithRawResponse,
    UserResourceWithStreamingResponse,
    AsyncUserResourceWithStreamingResponse,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....pagination import SyncV4PagePaginationArray, AsyncV4PagePaginationArray
from ...._base_client import AsyncPaginator, make_request_options
from .managed.managed import (
    ManagedResource,
    AsyncManagedResource,
    ManagedResourceWithRawResponse,
    AsyncManagedResourceWithRawResponse,
    ManagedResourceWithStreamingResponse,
    AsyncManagedResourceWithStreamingResponse,
)
from ....types.api_gateway import label_list_params
from ....types.api_gateway.label_list_response import LabelListResponse

__all__ = ["LabelsResource", "AsyncLabelsResource"]


class LabelsResource(SyncAPIResource):
    @cached_property
    def user(self) -> UserResource:
        return UserResource(self._client)

    @cached_property
    def managed(self) -> ManagedResource:
        return ManagedResource(self._client)

    @cached_property
    def with_raw_response(self) -> LabelsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return LabelsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LabelsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return LabelsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        zone_id: str,
        direction: Literal["asc", "desc"] | Omit = omit,
        filter: str | Omit = omit,
        order: Literal["name", "description", "created_at", "last_updated", "mapped_resources.operations"]
        | Omit = omit,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        source: Literal["user", "managed"] | Omit = omit,
        with_mapped_resource_counts: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncV4PagePaginationArray[LabelListResponse]:
        """
        Retrieve all labels

        Args:
          zone_id: Identifier.

          direction: Direction to order results.

          filter: Filter for labels where the name or description matches using substring match

          order: Field to order by

          page: Page number of paginated results.

          per_page: Maximum number of results per page.

          source: Filter for labels with source

          with_mapped_resource_counts: Include `mapped_resources` for each label

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._get_api_list(
            f"/zones/{zone_id}/api_gateway/labels",
            page=SyncV4PagePaginationArray[LabelListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "direction": direction,
                        "filter": filter,
                        "order": order,
                        "page": page,
                        "per_page": per_page,
                        "source": source,
                        "with_mapped_resource_counts": with_mapped_resource_counts,
                    },
                    label_list_params.LabelListParams,
                ),
            ),
            model=LabelListResponse,
        )


class AsyncLabelsResource(AsyncAPIResource):
    @cached_property
    def user(self) -> AsyncUserResource:
        return AsyncUserResource(self._client)

    @cached_property
    def managed(self) -> AsyncManagedResource:
        return AsyncManagedResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncLabelsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncLabelsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLabelsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncLabelsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        zone_id: str,
        direction: Literal["asc", "desc"] | Omit = omit,
        filter: str | Omit = omit,
        order: Literal["name", "description", "created_at", "last_updated", "mapped_resources.operations"]
        | Omit = omit,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        source: Literal["user", "managed"] | Omit = omit,
        with_mapped_resource_counts: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[LabelListResponse, AsyncV4PagePaginationArray[LabelListResponse]]:
        """
        Retrieve all labels

        Args:
          zone_id: Identifier.

          direction: Direction to order results.

          filter: Filter for labels where the name or description matches using substring match

          order: Field to order by

          page: Page number of paginated results.

          per_page: Maximum number of results per page.

          source: Filter for labels with source

          with_mapped_resource_counts: Include `mapped_resources` for each label

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._get_api_list(
            f"/zones/{zone_id}/api_gateway/labels",
            page=AsyncV4PagePaginationArray[LabelListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "direction": direction,
                        "filter": filter,
                        "order": order,
                        "page": page,
                        "per_page": per_page,
                        "source": source,
                        "with_mapped_resource_counts": with_mapped_resource_counts,
                    },
                    label_list_params.LabelListParams,
                ),
            ),
            model=LabelListResponse,
        )


class LabelsResourceWithRawResponse:
    def __init__(self, labels: LabelsResource) -> None:
        self._labels = labels

        self.list = to_raw_response_wrapper(
            labels.list,
        )

    @cached_property
    def user(self) -> UserResourceWithRawResponse:
        return UserResourceWithRawResponse(self._labels.user)

    @cached_property
    def managed(self) -> ManagedResourceWithRawResponse:
        return ManagedResourceWithRawResponse(self._labels.managed)


class AsyncLabelsResourceWithRawResponse:
    def __init__(self, labels: AsyncLabelsResource) -> None:
        self._labels = labels

        self.list = async_to_raw_response_wrapper(
            labels.list,
        )

    @cached_property
    def user(self) -> AsyncUserResourceWithRawResponse:
        return AsyncUserResourceWithRawResponse(self._labels.user)

    @cached_property
    def managed(self) -> AsyncManagedResourceWithRawResponse:
        return AsyncManagedResourceWithRawResponse(self._labels.managed)


class LabelsResourceWithStreamingResponse:
    def __init__(self, labels: LabelsResource) -> None:
        self._labels = labels

        self.list = to_streamed_response_wrapper(
            labels.list,
        )

    @cached_property
    def user(self) -> UserResourceWithStreamingResponse:
        return UserResourceWithStreamingResponse(self._labels.user)

    @cached_property
    def managed(self) -> ManagedResourceWithStreamingResponse:
        return ManagedResourceWithStreamingResponse(self._labels.managed)


class AsyncLabelsResourceWithStreamingResponse:
    def __init__(self, labels: AsyncLabelsResource) -> None:
        self._labels = labels

        self.list = async_to_streamed_response_wrapper(
            labels.list,
        )

    @cached_property
    def user(self) -> AsyncUserResourceWithStreamingResponse:
        return AsyncUserResourceWithStreamingResponse(self._labels.user)

    @cached_property
    def managed(self) -> AsyncManagedResourceWithStreamingResponse:
        return AsyncManagedResourceWithStreamingResponse(self._labels.managed)
