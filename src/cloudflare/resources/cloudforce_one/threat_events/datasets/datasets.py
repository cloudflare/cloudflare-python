# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .events import (
    EventsResource,
    AsyncEventsResource,
    EventsResourceWithRawResponse,
    AsyncEventsResourceWithRawResponse,
    EventsResourceWithStreamingResponse,
    AsyncEventsResourceWithStreamingResponse,
)
from ....._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ....._utils import path_template, maybe_transform, async_maybe_transform
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....._base_client import make_request_options
from .....types.cloudforce_one.threat_events import dataset_edit_params, dataset_list_params, dataset_create_params
from .....types.cloudforce_one.threat_events.dataset_get_response import DatasetGetResponse
from .....types.cloudforce_one.threat_events.dataset_raw_response import DatasetRawResponse
from .....types.cloudforce_one.threat_events.dataset_edit_response import DatasetEditResponse
from .....types.cloudforce_one.threat_events.dataset_list_response import DatasetListResponse
from .....types.cloudforce_one.threat_events.dataset_create_response import DatasetCreateResponse
from .....types.cloudforce_one.threat_events.dataset_delete_response import DatasetDeleteResponse

__all__ = ["DatasetsResource", "AsyncDatasetsResource"]


class DatasetsResource(SyncAPIResource):
    @cached_property
    def events(self) -> EventsResource:
        return EventsResource(self._client)

    @cached_property
    def with_raw_response(self) -> DatasetsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return DatasetsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DatasetsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return DatasetsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        account_id: str,
        is_public: bool,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DatasetCreateResponse:
        """
        Create a new dataset in the account.

        Args:
          account_id: Account ID.

          is_public: If true, then anyone can search the dataset. If false, then its limited to the
              account.

          name: Used to describe the dataset within the account context.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._post(
            path_template("/accounts/{account_id}/cloudforce-one/events/dataset/create", account_id=account_id),
            body=maybe_transform(
                {
                    "is_public": is_public,
                    "name": name,
                },
                dataset_create_params.DatasetCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DatasetCreateResponse,
        )

    def list(
        self,
        *,
        account_id: str,
        include_deleted: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DatasetListResponse:
        """
        List all datasets accessible to the account.

        Args:
          account_id: Account ID.

          include_deleted: When true, include soft-deleted datasets in the response. Each item includes a
              `deletedAt` field (ISO 8601 or null). Default: false.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get(
            path_template("/accounts/{account_id}/cloudforce-one/events/dataset", account_id=account_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"include_deleted": include_deleted}, dataset_list_params.DatasetListParams),
            ),
            cast_to=DatasetListResponse,
        )

    def delete(
        self,
        dataset_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DatasetDeleteResponse:
        """
        Soft-deletes a dataset given a datasetId.

        Args:
          account_id: Account ID.

          dataset_id: Dataset ID to delete

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not dataset_id:
            raise ValueError(f"Expected a non-empty value for `dataset_id` but received {dataset_id!r}")
        return self._delete(
            path_template(
                "/accounts/{account_id}/cloudforce-one/events/dataset/{dataset_id}",
                account_id=account_id,
                dataset_id=dataset_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DatasetDeleteResponse,
        )

    def edit(
        self,
        dataset_id: str,
        *,
        account_id: str,
        is_public: bool,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DatasetEditResponse:
        """
        Update an existing dataset by its identifier.

        Args:
          account_id: Account ID.

          dataset_id: Dataset ID.

          is_public: If true, then anyone can search the dataset. If false, then its limited to the
              account.

          name: Used to describe the dataset within the account context.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not dataset_id:
            raise ValueError(f"Expected a non-empty value for `dataset_id` but received {dataset_id!r}")
        return self._patch(
            path_template(
                "/accounts/{account_id}/cloudforce-one/events/dataset/{dataset_id}",
                account_id=account_id,
                dataset_id=dataset_id,
            ),
            body=maybe_transform(
                {
                    "is_public": is_public,
                    "name": name,
                },
                dataset_edit_params.DatasetEditParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DatasetEditResponse,
        )

    def get(
        self,
        dataset_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DatasetGetResponse:
        """
        Retrieve metadata for a specific dataset.

        Args:
          account_id: Account ID.

          dataset_id: Dataset ID.

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
                "/accounts/{account_id}/cloudforce-one/events/dataset/{dataset_id}",
                account_id=account_id,
                dataset_id=dataset_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DatasetGetResponse,
        )

    def raw(
        self,
        event_id: str,
        *,
        account_id: str,
        dataset_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DatasetRawResponse:
        """Retrieves the raw data associated with an event.

        Searches across all shards in
        the dataset.

        Args:
          account_id: Account ID.

          dataset_id: Dataset ID.

          event_id: Event ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not dataset_id:
            raise ValueError(f"Expected a non-empty value for `dataset_id` but received {dataset_id!r}")
        if not event_id:
            raise ValueError(f"Expected a non-empty value for `event_id` but received {event_id!r}")
        return self._get(
            path_template(
                "/accounts/{account_id}/cloudforce-one/events/raw/{dataset_id}/{event_id}",
                account_id=account_id,
                dataset_id=dataset_id,
                event_id=event_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DatasetRawResponse,
        )


class AsyncDatasetsResource(AsyncAPIResource):
    @cached_property
    def events(self) -> AsyncEventsResource:
        return AsyncEventsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncDatasetsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDatasetsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDatasetsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncDatasetsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_id: str,
        is_public: bool,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DatasetCreateResponse:
        """
        Create a new dataset in the account.

        Args:
          account_id: Account ID.

          is_public: If true, then anyone can search the dataset. If false, then its limited to the
              account.

          name: Used to describe the dataset within the account context.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._post(
            path_template("/accounts/{account_id}/cloudforce-one/events/dataset/create", account_id=account_id),
            body=await async_maybe_transform(
                {
                    "is_public": is_public,
                    "name": name,
                },
                dataset_create_params.DatasetCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DatasetCreateResponse,
        )

    async def list(
        self,
        *,
        account_id: str,
        include_deleted: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DatasetListResponse:
        """
        List all datasets accessible to the account.

        Args:
          account_id: Account ID.

          include_deleted: When true, include soft-deleted datasets in the response. Each item includes a
              `deletedAt` field (ISO 8601 or null). Default: false.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._get(
            path_template("/accounts/{account_id}/cloudforce-one/events/dataset", account_id=account_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"include_deleted": include_deleted}, dataset_list_params.DatasetListParams
                ),
            ),
            cast_to=DatasetListResponse,
        )

    async def delete(
        self,
        dataset_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DatasetDeleteResponse:
        """
        Soft-deletes a dataset given a datasetId.

        Args:
          account_id: Account ID.

          dataset_id: Dataset ID to delete

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not dataset_id:
            raise ValueError(f"Expected a non-empty value for `dataset_id` but received {dataset_id!r}")
        return await self._delete(
            path_template(
                "/accounts/{account_id}/cloudforce-one/events/dataset/{dataset_id}",
                account_id=account_id,
                dataset_id=dataset_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DatasetDeleteResponse,
        )

    async def edit(
        self,
        dataset_id: str,
        *,
        account_id: str,
        is_public: bool,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DatasetEditResponse:
        """
        Update an existing dataset by its identifier.

        Args:
          account_id: Account ID.

          dataset_id: Dataset ID.

          is_public: If true, then anyone can search the dataset. If false, then its limited to the
              account.

          name: Used to describe the dataset within the account context.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not dataset_id:
            raise ValueError(f"Expected a non-empty value for `dataset_id` but received {dataset_id!r}")
        return await self._patch(
            path_template(
                "/accounts/{account_id}/cloudforce-one/events/dataset/{dataset_id}",
                account_id=account_id,
                dataset_id=dataset_id,
            ),
            body=await async_maybe_transform(
                {
                    "is_public": is_public,
                    "name": name,
                },
                dataset_edit_params.DatasetEditParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DatasetEditResponse,
        )

    async def get(
        self,
        dataset_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DatasetGetResponse:
        """
        Retrieve metadata for a specific dataset.

        Args:
          account_id: Account ID.

          dataset_id: Dataset ID.

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
                "/accounts/{account_id}/cloudforce-one/events/dataset/{dataset_id}",
                account_id=account_id,
                dataset_id=dataset_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DatasetGetResponse,
        )

    async def raw(
        self,
        event_id: str,
        *,
        account_id: str,
        dataset_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DatasetRawResponse:
        """Retrieves the raw data associated with an event.

        Searches across all shards in
        the dataset.

        Args:
          account_id: Account ID.

          dataset_id: Dataset ID.

          event_id: Event ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not dataset_id:
            raise ValueError(f"Expected a non-empty value for `dataset_id` but received {dataset_id!r}")
        if not event_id:
            raise ValueError(f"Expected a non-empty value for `event_id` but received {event_id!r}")
        return await self._get(
            path_template(
                "/accounts/{account_id}/cloudforce-one/events/raw/{dataset_id}/{event_id}",
                account_id=account_id,
                dataset_id=dataset_id,
                event_id=event_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DatasetRawResponse,
        )


class DatasetsResourceWithRawResponse:
    def __init__(self, datasets: DatasetsResource) -> None:
        self._datasets = datasets

        self.create = to_raw_response_wrapper(
            datasets.create,
        )
        self.list = to_raw_response_wrapper(
            datasets.list,
        )
        self.delete = to_raw_response_wrapper(
            datasets.delete,
        )
        self.edit = to_raw_response_wrapper(
            datasets.edit,
        )
        self.get = to_raw_response_wrapper(
            datasets.get,
        )
        self.raw = to_raw_response_wrapper(
            datasets.raw,
        )

    @cached_property
    def events(self) -> EventsResourceWithRawResponse:
        return EventsResourceWithRawResponse(self._datasets.events)


class AsyncDatasetsResourceWithRawResponse:
    def __init__(self, datasets: AsyncDatasetsResource) -> None:
        self._datasets = datasets

        self.create = async_to_raw_response_wrapper(
            datasets.create,
        )
        self.list = async_to_raw_response_wrapper(
            datasets.list,
        )
        self.delete = async_to_raw_response_wrapper(
            datasets.delete,
        )
        self.edit = async_to_raw_response_wrapper(
            datasets.edit,
        )
        self.get = async_to_raw_response_wrapper(
            datasets.get,
        )
        self.raw = async_to_raw_response_wrapper(
            datasets.raw,
        )

    @cached_property
    def events(self) -> AsyncEventsResourceWithRawResponse:
        return AsyncEventsResourceWithRawResponse(self._datasets.events)


class DatasetsResourceWithStreamingResponse:
    def __init__(self, datasets: DatasetsResource) -> None:
        self._datasets = datasets

        self.create = to_streamed_response_wrapper(
            datasets.create,
        )
        self.list = to_streamed_response_wrapper(
            datasets.list,
        )
        self.delete = to_streamed_response_wrapper(
            datasets.delete,
        )
        self.edit = to_streamed_response_wrapper(
            datasets.edit,
        )
        self.get = to_streamed_response_wrapper(
            datasets.get,
        )
        self.raw = to_streamed_response_wrapper(
            datasets.raw,
        )

    @cached_property
    def events(self) -> EventsResourceWithStreamingResponse:
        return EventsResourceWithStreamingResponse(self._datasets.events)


class AsyncDatasetsResourceWithStreamingResponse:
    def __init__(self, datasets: AsyncDatasetsResource) -> None:
        self._datasets = datasets

        self.create = async_to_streamed_response_wrapper(
            datasets.create,
        )
        self.list = async_to_streamed_response_wrapper(
            datasets.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            datasets.delete,
        )
        self.edit = async_to_streamed_response_wrapper(
            datasets.edit,
        )
        self.get = async_to_streamed_response_wrapper(
            datasets.get,
        )
        self.raw = async_to_streamed_response_wrapper(
            datasets.raw,
        )

    @cached_property
    def events(self) -> AsyncEventsResourceWithStreamingResponse:
        return AsyncEventsResourceWithStreamingResponse(self._datasets.events)
