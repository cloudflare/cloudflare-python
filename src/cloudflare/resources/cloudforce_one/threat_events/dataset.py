# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.cloudforce_one.threat_events import dataset_create_params, dataset_update_params
from ....types.cloudforce_one.threat_events.dataset_get_response import DatasetGetResponse
from ....types.cloudforce_one.threat_events.dataset_raw_response import DatasetRawResponse
from ....types.cloudforce_one.threat_events.dataset_list_response import DatasetListResponse
from ....types.cloudforce_one.threat_events.dataset_create_response import DatasetCreateResponse
from ....types.cloudforce_one.threat_events.dataset_update_response import DatasetUpdateResponse

__all__ = ["DatasetResource", "AsyncDatasetResource"]


class DatasetResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DatasetResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return DatasetResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DatasetResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return DatasetResourceWithStreamingResponse(self)

    def create(
        self,
        account_id: float,
        *,
        is_public: bool,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DatasetCreateResponse:
        """
        Creates a dataset

        Args:
          account_id: Account ID

          is_public: If true, then anyone can search the dataset. If false, then its limited to the
              account.

          name: Used to describe the dataset within the account context

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            f"/accounts/{account_id}/cloudforce-one/events/dataset/create",
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

    def update(
        self,
        dataset_id: str,
        *,
        account_id: float,
        is_public: bool,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DatasetUpdateResponse:
        """
        Updates an existing dataset

        Args:
          account_id: Account ID

          dataset_id: Dataset name

          is_public: If true, then anyone can search the dataset. If false, then its limited to the
              account.

          name: Used to describe the dataset within the account context

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not dataset_id:
            raise ValueError(f"Expected a non-empty value for `dataset_id` but received {dataset_id!r}")
        return self._post(
            f"/accounts/{account_id}/cloudforce-one/events/dataset/{dataset_id}",
            body=maybe_transform(
                {
                    "is_public": is_public,
                    "name": name,
                },
                dataset_update_params.DatasetUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DatasetUpdateResponse,
        )

    def list(
        self,
        account_id: float,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DatasetListResponse:
        """
        Lists all datasets in an account

        Args:
          account_id: Account ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/accounts/{account_id}/cloudforce-one/events/dataset",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DatasetListResponse,
        )

    def get(
        self,
        dataset_id: str,
        *,
        account_id: float,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DatasetGetResponse:
        """
        Reads a dataset

        Args:
          account_id: Account ID

          dataset_id: Dataset name

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not dataset_id:
            raise ValueError(f"Expected a non-empty value for `dataset_id` but received {dataset_id!r}")
        return self._get(
            f"/accounts/{account_id}/cloudforce-one/events/dataset/{dataset_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DatasetGetResponse,
        )

    def raw(
        self,
        event_id: str,
        *,
        account_id: float,
        dataset_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DatasetRawResponse:
        """
        Reads data for a raw event

        Args:
          account_id: Account ID

          dataset_id: Dataset name

          event_id: Event ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not dataset_id:
            raise ValueError(f"Expected a non-empty value for `dataset_id` but received {dataset_id!r}")
        if not event_id:
            raise ValueError(f"Expected a non-empty value for `event_id` but received {event_id!r}")
        return self._get(
            f"/accounts/{account_id}/cloudforce-one/events/raw/{dataset_id}/{event_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DatasetRawResponse,
        )


class AsyncDatasetResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDatasetResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDatasetResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDatasetResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncDatasetResourceWithStreamingResponse(self)

    async def create(
        self,
        account_id: float,
        *,
        is_public: bool,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DatasetCreateResponse:
        """
        Creates a dataset

        Args:
          account_id: Account ID

          is_public: If true, then anyone can search the dataset. If false, then its limited to the
              account.

          name: Used to describe the dataset within the account context

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            f"/accounts/{account_id}/cloudforce-one/events/dataset/create",
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

    async def update(
        self,
        dataset_id: str,
        *,
        account_id: float,
        is_public: bool,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DatasetUpdateResponse:
        """
        Updates an existing dataset

        Args:
          account_id: Account ID

          dataset_id: Dataset name

          is_public: If true, then anyone can search the dataset. If false, then its limited to the
              account.

          name: Used to describe the dataset within the account context

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not dataset_id:
            raise ValueError(f"Expected a non-empty value for `dataset_id` but received {dataset_id!r}")
        return await self._post(
            f"/accounts/{account_id}/cloudforce-one/events/dataset/{dataset_id}",
            body=await async_maybe_transform(
                {
                    "is_public": is_public,
                    "name": name,
                },
                dataset_update_params.DatasetUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DatasetUpdateResponse,
        )

    async def list(
        self,
        account_id: float,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DatasetListResponse:
        """
        Lists all datasets in an account

        Args:
          account_id: Account ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/accounts/{account_id}/cloudforce-one/events/dataset",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DatasetListResponse,
        )

    async def get(
        self,
        dataset_id: str,
        *,
        account_id: float,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DatasetGetResponse:
        """
        Reads a dataset

        Args:
          account_id: Account ID

          dataset_id: Dataset name

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not dataset_id:
            raise ValueError(f"Expected a non-empty value for `dataset_id` but received {dataset_id!r}")
        return await self._get(
            f"/accounts/{account_id}/cloudforce-one/events/dataset/{dataset_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DatasetGetResponse,
        )

    async def raw(
        self,
        event_id: str,
        *,
        account_id: float,
        dataset_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DatasetRawResponse:
        """
        Reads data for a raw event

        Args:
          account_id: Account ID

          dataset_id: Dataset name

          event_id: Event ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not dataset_id:
            raise ValueError(f"Expected a non-empty value for `dataset_id` but received {dataset_id!r}")
        if not event_id:
            raise ValueError(f"Expected a non-empty value for `event_id` but received {event_id!r}")
        return await self._get(
            f"/accounts/{account_id}/cloudforce-one/events/raw/{dataset_id}/{event_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DatasetRawResponse,
        )


class DatasetResourceWithRawResponse:
    def __init__(self, dataset: DatasetResource) -> None:
        self._dataset = dataset

        self.create = to_raw_response_wrapper(
            dataset.create,
        )
        self.update = to_raw_response_wrapper(
            dataset.update,
        )
        self.list = to_raw_response_wrapper(
            dataset.list,
        )
        self.get = to_raw_response_wrapper(
            dataset.get,
        )
        self.raw = to_raw_response_wrapper(
            dataset.raw,
        )


class AsyncDatasetResourceWithRawResponse:
    def __init__(self, dataset: AsyncDatasetResource) -> None:
        self._dataset = dataset

        self.create = async_to_raw_response_wrapper(
            dataset.create,
        )
        self.update = async_to_raw_response_wrapper(
            dataset.update,
        )
        self.list = async_to_raw_response_wrapper(
            dataset.list,
        )
        self.get = async_to_raw_response_wrapper(
            dataset.get,
        )
        self.raw = async_to_raw_response_wrapper(
            dataset.raw,
        )


class DatasetResourceWithStreamingResponse:
    def __init__(self, dataset: DatasetResource) -> None:
        self._dataset = dataset

        self.create = to_streamed_response_wrapper(
            dataset.create,
        )
        self.update = to_streamed_response_wrapper(
            dataset.update,
        )
        self.list = to_streamed_response_wrapper(
            dataset.list,
        )
        self.get = to_streamed_response_wrapper(
            dataset.get,
        )
        self.raw = to_streamed_response_wrapper(
            dataset.raw,
        )


class AsyncDatasetResourceWithStreamingResponse:
    def __init__(self, dataset: AsyncDatasetResource) -> None:
        self._dataset = dataset

        self.create = async_to_streamed_response_wrapper(
            dataset.create,
        )
        self.update = async_to_streamed_response_wrapper(
            dataset.update,
        )
        self.list = async_to_streamed_response_wrapper(
            dataset.list,
        )
        self.get = async_to_streamed_response_wrapper(
            dataset.get,
        )
        self.raw = async_to_streamed_response_wrapper(
            dataset.raw,
        )
