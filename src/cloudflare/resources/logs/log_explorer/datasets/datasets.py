# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Iterable, Optional, cast

import httpx

from .available import (
    AvailableResource,
    AsyncAvailableResource,
    AvailableResourceWithRawResponse,
    AsyncAvailableResourceWithRawResponse,
    AvailableResourceWithStreamingResponse,
    AsyncAvailableResourceWithStreamingResponse,
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
from ....._wrappers import ResultWrapper
from .....pagination import SyncSinglePage, AsyncSinglePage
from ....._base_client import AsyncPaginator, make_request_options
from .....types.logs.log_explorer import dataset_list_params, dataset_create_params, dataset_update_params
from .....types.logs.log_explorer.dataset import Dataset
from .....types.logs.log_explorer.dataset_summary import DatasetSummary

__all__ = ["DatasetsResource", "AsyncDatasetsResource"]


class DatasetsResource(SyncAPIResource):
    @cached_property
    def available(self) -> AvailableResource:
        return AvailableResource(self._client)

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
        dataset: str,
        account_id: str | Omit = omit,
        zone_id: str | Omit = omit,
        fields: Iterable[dataset_create_params.Field] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[Dataset]:
        """
        Create a new Log Explorer dataset for the account or zone.

        List available account or zone datasets to see the dataset types and fields you
        can use.

        The `fields` property is optional. If not specified, all available fields will
        be enabled.

        For dataset field definitions, see:
        https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/

        Args:
          dataset: Dataset type name to create (e.g. `http_requests`).

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          fields: Controls which fields the API ingests. Defaults to all available fields when
              absent.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if account_id and zone_id:
            raise ValueError("You cannot provide both account_id and zone_id")

        if account_id:
            account_or_zone = "accounts"
            account_or_zone_id = account_id
        else:
            if not zone_id:
                raise ValueError("You must provide either account_id or zone_id")

            account_or_zone = "zones"
            account_or_zone_id = zone_id
        return self._post(
            path_template(
                "/{account_or_zone}/{account_or_zone_id}/logs/explorer/datasets",
                account_or_zone=account_or_zone,
                account_or_zone_id=account_or_zone_id,
            ),
            body=maybe_transform(
                {
                    "dataset": dataset,
                    "fields": fields,
                },
                dataset_create_params.DatasetCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[Dataset]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[Dataset]], ResultWrapper[Dataset]),
        )

    def update(
        self,
        dataset_id: str,
        *,
        enabled: bool,
        account_id: str | Omit = omit,
        zone_id: str | Omit = omit,
        fields: Iterable[dataset_update_params.Field] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[Dataset]:
        """
        Updates the enabled state and/or field configuration of an account or zone
        dataset.

        Args:
          enabled: Whether to enable or disable log ingest for this dataset.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          fields: Controls which fields the API ingests after the update. Defaults to all
              available fields when absent.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not dataset_id:
            raise ValueError(f"Expected a non-empty value for `dataset_id` but received {dataset_id!r}")
        if account_id and zone_id:
            raise ValueError("You cannot provide both account_id and zone_id")

        if account_id:
            account_or_zone = "accounts"
            account_or_zone_id = account_id
        else:
            if not zone_id:
                raise ValueError("You must provide either account_id or zone_id")

            account_or_zone = "zones"
            account_or_zone_id = zone_id
        return self._put(
            path_template(
                "/{account_or_zone}/{account_or_zone_id}/logs/explorer/datasets/{dataset_id}",
                dataset_id=dataset_id,
                account_or_zone=account_or_zone,
                account_or_zone_id=account_or_zone_id,
            ),
            body=maybe_transform(
                {
                    "enabled": enabled,
                    "fields": fields,
                },
                dataset_update_params.DatasetUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[Dataset]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[Dataset]], ResultWrapper[Dataset]),
        )

    def list(
        self,
        *,
        account_id: str | Omit = omit,
        zone_id: str | Omit = omit,
        include_zones: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncSinglePage[DatasetSummary]:
        """
        Returns all Log Explorer datasets configured for the account or zone.

        Pass `include_zones=true` to also include zone-level datasets that belong to
        this account or zone. List responses omit the `fields` property; use the
        single-dataset endpoint to retrieve field configuration.

        Args:
          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          include_zones: Set to true to include zone-scoped datasets belonging to this account.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if account_id and zone_id:
            raise ValueError("You cannot provide both account_id and zone_id")

        if account_id:
            account_or_zone = "accounts"
            account_or_zone_id = account_id
        else:
            if not zone_id:
                raise ValueError("You must provide either account_id or zone_id")

            account_or_zone = "zones"
            account_or_zone_id = zone_id
        return self._get_api_list(
            path_template(
                "/{account_or_zone}/{account_or_zone_id}/logs/explorer/datasets",
                account_or_zone=account_or_zone,
                account_or_zone_id=account_or_zone_id,
            ),
            page=SyncSinglePage[DatasetSummary],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"include_zones": include_zones}, dataset_list_params.DatasetListParams),
            ),
            model=DatasetSummary,
        )

    def get(
        self,
        dataset_id: str,
        *,
        account_id: str | Omit = omit,
        zone_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[Dataset]:
        """
        Retrieve a single Log Explorer dataset by ID for the account or zone.

        Args:
          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not dataset_id:
            raise ValueError(f"Expected a non-empty value for `dataset_id` but received {dataset_id!r}")
        if account_id and zone_id:
            raise ValueError("You cannot provide both account_id and zone_id")

        if account_id:
            account_or_zone = "accounts"
            account_or_zone_id = account_id
        else:
            if not zone_id:
                raise ValueError("You must provide either account_id or zone_id")

            account_or_zone = "zones"
            account_or_zone_id = zone_id
        return self._get(
            path_template(
                "/{account_or_zone}/{account_or_zone_id}/logs/explorer/datasets/{dataset_id}",
                dataset_id=dataset_id,
                account_or_zone=account_or_zone,
                account_or_zone_id=account_or_zone_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[Dataset]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[Dataset]], ResultWrapper[Dataset]),
        )


class AsyncDatasetsResource(AsyncAPIResource):
    @cached_property
    def available(self) -> AsyncAvailableResource:
        return AsyncAvailableResource(self._client)

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
        dataset: str,
        account_id: str | Omit = omit,
        zone_id: str | Omit = omit,
        fields: Iterable[dataset_create_params.Field] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[Dataset]:
        """
        Create a new Log Explorer dataset for the account or zone.

        List available account or zone datasets to see the dataset types and fields you
        can use.

        The `fields` property is optional. If not specified, all available fields will
        be enabled.

        For dataset field definitions, see:
        https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/

        Args:
          dataset: Dataset type name to create (e.g. `http_requests`).

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          fields: Controls which fields the API ingests. Defaults to all available fields when
              absent.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if account_id and zone_id:
            raise ValueError("You cannot provide both account_id and zone_id")

        if account_id:
            account_or_zone = "accounts"
            account_or_zone_id = account_id
        else:
            if not zone_id:
                raise ValueError("You must provide either account_id or zone_id")

            account_or_zone = "zones"
            account_or_zone_id = zone_id
        return await self._post(
            path_template(
                "/{account_or_zone}/{account_or_zone_id}/logs/explorer/datasets",
                account_or_zone=account_or_zone,
                account_or_zone_id=account_or_zone_id,
            ),
            body=await async_maybe_transform(
                {
                    "dataset": dataset,
                    "fields": fields,
                },
                dataset_create_params.DatasetCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[Dataset]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[Dataset]], ResultWrapper[Dataset]),
        )

    async def update(
        self,
        dataset_id: str,
        *,
        enabled: bool,
        account_id: str | Omit = omit,
        zone_id: str | Omit = omit,
        fields: Iterable[dataset_update_params.Field] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[Dataset]:
        """
        Updates the enabled state and/or field configuration of an account or zone
        dataset.

        Args:
          enabled: Whether to enable or disable log ingest for this dataset.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          fields: Controls which fields the API ingests after the update. Defaults to all
              available fields when absent.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not dataset_id:
            raise ValueError(f"Expected a non-empty value for `dataset_id` but received {dataset_id!r}")
        if account_id and zone_id:
            raise ValueError("You cannot provide both account_id and zone_id")

        if account_id:
            account_or_zone = "accounts"
            account_or_zone_id = account_id
        else:
            if not zone_id:
                raise ValueError("You must provide either account_id or zone_id")

            account_or_zone = "zones"
            account_or_zone_id = zone_id
        return await self._put(
            path_template(
                "/{account_or_zone}/{account_or_zone_id}/logs/explorer/datasets/{dataset_id}",
                dataset_id=dataset_id,
                account_or_zone=account_or_zone,
                account_or_zone_id=account_or_zone_id,
            ),
            body=await async_maybe_transform(
                {
                    "enabled": enabled,
                    "fields": fields,
                },
                dataset_update_params.DatasetUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[Dataset]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[Dataset]], ResultWrapper[Dataset]),
        )

    def list(
        self,
        *,
        account_id: str | Omit = omit,
        zone_id: str | Omit = omit,
        include_zones: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[DatasetSummary, AsyncSinglePage[DatasetSummary]]:
        """
        Returns all Log Explorer datasets configured for the account or zone.

        Pass `include_zones=true` to also include zone-level datasets that belong to
        this account or zone. List responses omit the `fields` property; use the
        single-dataset endpoint to retrieve field configuration.

        Args:
          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          include_zones: Set to true to include zone-scoped datasets belonging to this account.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if account_id and zone_id:
            raise ValueError("You cannot provide both account_id and zone_id")

        if account_id:
            account_or_zone = "accounts"
            account_or_zone_id = account_id
        else:
            if not zone_id:
                raise ValueError("You must provide either account_id or zone_id")

            account_or_zone = "zones"
            account_or_zone_id = zone_id
        return self._get_api_list(
            path_template(
                "/{account_or_zone}/{account_or_zone_id}/logs/explorer/datasets",
                account_or_zone=account_or_zone,
                account_or_zone_id=account_or_zone_id,
            ),
            page=AsyncSinglePage[DatasetSummary],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"include_zones": include_zones}, dataset_list_params.DatasetListParams),
            ),
            model=DatasetSummary,
        )

    async def get(
        self,
        dataset_id: str,
        *,
        account_id: str | Omit = omit,
        zone_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[Dataset]:
        """
        Retrieve a single Log Explorer dataset by ID for the account or zone.

        Args:
          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not dataset_id:
            raise ValueError(f"Expected a non-empty value for `dataset_id` but received {dataset_id!r}")
        if account_id and zone_id:
            raise ValueError("You cannot provide both account_id and zone_id")

        if account_id:
            account_or_zone = "accounts"
            account_or_zone_id = account_id
        else:
            if not zone_id:
                raise ValueError("You must provide either account_id or zone_id")

            account_or_zone = "zones"
            account_or_zone_id = zone_id
        return await self._get(
            path_template(
                "/{account_or_zone}/{account_or_zone_id}/logs/explorer/datasets/{dataset_id}",
                dataset_id=dataset_id,
                account_or_zone=account_or_zone,
                account_or_zone_id=account_or_zone_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[Dataset]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[Dataset]], ResultWrapper[Dataset]),
        )


class DatasetsResourceWithRawResponse:
    def __init__(self, datasets: DatasetsResource) -> None:
        self._datasets = datasets

        self.create = to_raw_response_wrapper(
            datasets.create,
        )
        self.update = to_raw_response_wrapper(
            datasets.update,
        )
        self.list = to_raw_response_wrapper(
            datasets.list,
        )
        self.get = to_raw_response_wrapper(
            datasets.get,
        )

    @cached_property
    def available(self) -> AvailableResourceWithRawResponse:
        return AvailableResourceWithRawResponse(self._datasets.available)


class AsyncDatasetsResourceWithRawResponse:
    def __init__(self, datasets: AsyncDatasetsResource) -> None:
        self._datasets = datasets

        self.create = async_to_raw_response_wrapper(
            datasets.create,
        )
        self.update = async_to_raw_response_wrapper(
            datasets.update,
        )
        self.list = async_to_raw_response_wrapper(
            datasets.list,
        )
        self.get = async_to_raw_response_wrapper(
            datasets.get,
        )

    @cached_property
    def available(self) -> AsyncAvailableResourceWithRawResponse:
        return AsyncAvailableResourceWithRawResponse(self._datasets.available)


class DatasetsResourceWithStreamingResponse:
    def __init__(self, datasets: DatasetsResource) -> None:
        self._datasets = datasets

        self.create = to_streamed_response_wrapper(
            datasets.create,
        )
        self.update = to_streamed_response_wrapper(
            datasets.update,
        )
        self.list = to_streamed_response_wrapper(
            datasets.list,
        )
        self.get = to_streamed_response_wrapper(
            datasets.get,
        )

    @cached_property
    def available(self) -> AvailableResourceWithStreamingResponse:
        return AvailableResourceWithStreamingResponse(self._datasets.available)


class AsyncDatasetsResourceWithStreamingResponse:
    def __init__(self, datasets: AsyncDatasetsResource) -> None:
        self._datasets = datasets

        self.create = async_to_streamed_response_wrapper(
            datasets.create,
        )
        self.update = async_to_streamed_response_wrapper(
            datasets.update,
        )
        self.list = async_to_streamed_response_wrapper(
            datasets.list,
        )
        self.get = async_to_streamed_response_wrapper(
            datasets.get,
        )

    @cached_property
    def available(self) -> AsyncAvailableResourceWithStreamingResponse:
        return AsyncAvailableResourceWithStreamingResponse(self._datasets.available)
