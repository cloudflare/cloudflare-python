# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, List, Type, Iterable, Optional, cast
from typing_extensions import Literal

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
from ...._wrappers import ResultWrapper
from ....pagination import SyncSinglePage, AsyncSinglePage
from .metadata_index import (
    MetadataIndexResource,
    AsyncMetadataIndexResource,
    MetadataIndexResourceWithRawResponse,
    AsyncMetadataIndexResourceWithRawResponse,
    MetadataIndexResourceWithStreamingResponse,
    AsyncMetadataIndexResourceWithStreamingResponse,
)
from ...._base_client import AsyncPaginator, make_request_options
from ....types.vectorize import (
    index_query_params,
    index_create_params,
    index_insert_params,
    index_upsert_params,
    index_get_by_ids_params,
    index_delete_by_ids_params,
)
from ....types.vectorize.create_index import CreateIndex
from ....types.vectorize.index_info_response import IndexInfoResponse
from ....types.vectorize.index_query_response import IndexQueryResponse
from ....types.vectorize.index_delete_response import IndexDeleteResponse
from ....types.vectorize.index_insert_response import IndexInsertResponse
from ....types.vectorize.index_upsert_response import IndexUpsertResponse
from ....types.vectorize.index_delete_by_ids_response import IndexDeleteByIDsResponse

__all__ = ["IndexesResource", "AsyncIndexesResource"]


class IndexesResource(SyncAPIResource):
    @cached_property
    def metadata_index(self) -> MetadataIndexResource:
        return MetadataIndexResource(self._client)

    @cached_property
    def with_raw_response(self) -> IndexesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return IndexesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> IndexesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return IndexesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        account_id: str,
        config: index_create_params.Config,
        name: str,
        description: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[CreateIndex]:
        """
        Creates and returns a new Vectorize Index.

        Args:
          account_id: Identifier

          config: Specifies the type of configuration to use for the index.

          description: Specifies the description of the index.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._post(
            f"/accounts/{account_id}/vectorize/v2/indexes",
            body=maybe_transform(
                {
                    "config": config,
                    "name": name,
                    "description": description,
                },
                index_create_params.IndexCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[CreateIndex]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[CreateIndex]], ResultWrapper[CreateIndex]),
        )

    def list(
        self,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncSinglePage[CreateIndex]:
        """
        Returns a list of Vectorize Indexes

        Args:
          account_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/vectorize/v2/indexes",
            page=SyncSinglePage[CreateIndex],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=CreateIndex,
        )

    def delete(
        self,
        index_name: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[IndexDeleteResponse]:
        """
        Deletes the specified Vectorize Index.

        Args:
          account_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not index_name:
            raise ValueError(f"Expected a non-empty value for `index_name` but received {index_name!r}")
        return cast(
            Optional[IndexDeleteResponse],
            self._delete(
                f"/accounts/{account_id}/vectorize/v2/indexes/{index_name}",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper[Optional[IndexDeleteResponse]]._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[IndexDeleteResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def delete_by_ids(
        self,
        index_name: str,
        *,
        account_id: str,
        ids: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[IndexDeleteByIDsResponse]:
        """
        Delete a set of vectors from an index by their vector identifiers.

        Args:
          account_id: Identifier

          ids: A list of vector identifiers to delete from the index indicated by the path.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not index_name:
            raise ValueError(f"Expected a non-empty value for `index_name` but received {index_name!r}")
        return self._post(
            f"/accounts/{account_id}/vectorize/v2/indexes/{index_name}/delete_by_ids",
            body=maybe_transform({"ids": ids}, index_delete_by_ids_params.IndexDeleteByIDsParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[IndexDeleteByIDsResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[IndexDeleteByIDsResponse]], ResultWrapper[IndexDeleteByIDsResponse]),
        )

    def get(
        self,
        index_name: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[CreateIndex]:
        """
        Returns the specified Vectorize Index.

        Args:
          account_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not index_name:
            raise ValueError(f"Expected a non-empty value for `index_name` but received {index_name!r}")
        return self._get(
            f"/accounts/{account_id}/vectorize/v2/indexes/{index_name}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[CreateIndex]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[CreateIndex]], ResultWrapper[CreateIndex]),
        )

    def get_by_ids(
        self,
        index_name: str,
        *,
        account_id: str,
        ids: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Get a set of vectors from an index by their vector identifiers.

        Args:
          account_id: Identifier

          ids: A list of vector identifiers to retrieve from the index indicated by the path.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not index_name:
            raise ValueError(f"Expected a non-empty value for `index_name` but received {index_name!r}")
        return self._post(
            f"/accounts/{account_id}/vectorize/v2/indexes/{index_name}/get_by_ids",
            body=maybe_transform({"ids": ids}, index_get_by_ids_params.IndexGetByIDsParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[object]]._unwrapper,
            ),
            cast_to=cast(Type[object], ResultWrapper[object]),
        )

    def info(
        self,
        index_name: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[IndexInfoResponse]:
        """
        Get information about a vectorize index.

        Args:
          account_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not index_name:
            raise ValueError(f"Expected a non-empty value for `index_name` but received {index_name!r}")
        return self._get(
            f"/accounts/{account_id}/vectorize/v2/indexes/{index_name}/info",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[IndexInfoResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[IndexInfoResponse]], ResultWrapper[IndexInfoResponse]),
        )

    def insert(
        self,
        index_name: str,
        *,
        account_id: str,
        body: str,
        unparsable_behavior: Literal["error", "discard"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[IndexInsertResponse]:
        """
        Inserts vectors into the specified index and returns a mutation id corresponding
        to the vectors enqueued for insertion.

        Args:
          account_id: Identifier

          body: ndjson file containing vectors to insert.

          unparsable_behavior: Behavior for ndjson parse failures.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not index_name:
            raise ValueError(f"Expected a non-empty value for `index_name` but received {index_name!r}")
        return self._post(
            f"/accounts/{account_id}/vectorize/v2/indexes/{index_name}/insert",
            body=maybe_transform(body, index_insert_params.IndexInsertParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"unparsable_behavior": unparsable_behavior}, index_insert_params.IndexInsertParams
                ),
                post_parser=ResultWrapper[Optional[IndexInsertResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[IndexInsertResponse]], ResultWrapper[IndexInsertResponse]),
        )

    def query(
        self,
        index_name: str,
        *,
        account_id: str,
        vector: Iterable[float],
        filter: object | NotGiven = NOT_GIVEN,
        return_metadata: Literal["none", "indexed", "all"] | NotGiven = NOT_GIVEN,
        return_values: bool | NotGiven = NOT_GIVEN,
        top_k: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[IndexQueryResponse]:
        """
        Finds vectors closest to a given vector in an index.

        Args:
          account_id: Identifier

          vector: The search vector that will be used to find the nearest neighbors.

          filter: A metadata filter expression used to limit nearest neighbor results.

          return_metadata: Whether to return no metadata, indexed metadata or all metadata associated with
              the closest vectors.

          return_values: Whether to return the values associated with the closest vectors.

          top_k: The number of nearest neighbors to find.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not index_name:
            raise ValueError(f"Expected a non-empty value for `index_name` but received {index_name!r}")
        return self._post(
            f"/accounts/{account_id}/vectorize/v2/indexes/{index_name}/query",
            body=maybe_transform(
                {
                    "vector": vector,
                    "filter": filter,
                    "return_metadata": return_metadata,
                    "return_values": return_values,
                    "top_k": top_k,
                },
                index_query_params.IndexQueryParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[IndexQueryResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[IndexQueryResponse]], ResultWrapper[IndexQueryResponse]),
        )

    def upsert(
        self,
        index_name: str,
        *,
        account_id: str,
        body: str,
        unparsable_behavior: Literal["error", "discard"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[IndexUpsertResponse]:
        """
        Upserts vectors into the specified index, creating them if they do not exist and
        returns a mutation id corresponding to the vectors enqueued for upsertion.

        Args:
          account_id: Identifier

          body: ndjson file containing vectors to upsert.

          unparsable_behavior: Behavior for ndjson parse failures.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not index_name:
            raise ValueError(f"Expected a non-empty value for `index_name` but received {index_name!r}")
        return self._post(
            f"/accounts/{account_id}/vectorize/v2/indexes/{index_name}/upsert",
            body=maybe_transform(body, index_upsert_params.IndexUpsertParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"unparsable_behavior": unparsable_behavior}, index_upsert_params.IndexUpsertParams
                ),
                post_parser=ResultWrapper[Optional[IndexUpsertResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[IndexUpsertResponse]], ResultWrapper[IndexUpsertResponse]),
        )


class AsyncIndexesResource(AsyncAPIResource):
    @cached_property
    def metadata_index(self) -> AsyncMetadataIndexResource:
        return AsyncMetadataIndexResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncIndexesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncIndexesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncIndexesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncIndexesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_id: str,
        config: index_create_params.Config,
        name: str,
        description: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[CreateIndex]:
        """
        Creates and returns a new Vectorize Index.

        Args:
          account_id: Identifier

          config: Specifies the type of configuration to use for the index.

          description: Specifies the description of the index.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._post(
            f"/accounts/{account_id}/vectorize/v2/indexes",
            body=await async_maybe_transform(
                {
                    "config": config,
                    "name": name,
                    "description": description,
                },
                index_create_params.IndexCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[CreateIndex]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[CreateIndex]], ResultWrapper[CreateIndex]),
        )

    def list(
        self,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[CreateIndex, AsyncSinglePage[CreateIndex]]:
        """
        Returns a list of Vectorize Indexes

        Args:
          account_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/vectorize/v2/indexes",
            page=AsyncSinglePage[CreateIndex],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=CreateIndex,
        )

    async def delete(
        self,
        index_name: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[IndexDeleteResponse]:
        """
        Deletes the specified Vectorize Index.

        Args:
          account_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not index_name:
            raise ValueError(f"Expected a non-empty value for `index_name` but received {index_name!r}")
        return cast(
            Optional[IndexDeleteResponse],
            await self._delete(
                f"/accounts/{account_id}/vectorize/v2/indexes/{index_name}",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper[Optional[IndexDeleteResponse]]._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[IndexDeleteResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def delete_by_ids(
        self,
        index_name: str,
        *,
        account_id: str,
        ids: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[IndexDeleteByIDsResponse]:
        """
        Delete a set of vectors from an index by their vector identifiers.

        Args:
          account_id: Identifier

          ids: A list of vector identifiers to delete from the index indicated by the path.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not index_name:
            raise ValueError(f"Expected a non-empty value for `index_name` but received {index_name!r}")
        return await self._post(
            f"/accounts/{account_id}/vectorize/v2/indexes/{index_name}/delete_by_ids",
            body=await async_maybe_transform({"ids": ids}, index_delete_by_ids_params.IndexDeleteByIDsParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[IndexDeleteByIDsResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[IndexDeleteByIDsResponse]], ResultWrapper[IndexDeleteByIDsResponse]),
        )

    async def get(
        self,
        index_name: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[CreateIndex]:
        """
        Returns the specified Vectorize Index.

        Args:
          account_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not index_name:
            raise ValueError(f"Expected a non-empty value for `index_name` but received {index_name!r}")
        return await self._get(
            f"/accounts/{account_id}/vectorize/v2/indexes/{index_name}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[CreateIndex]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[CreateIndex]], ResultWrapper[CreateIndex]),
        )

    async def get_by_ids(
        self,
        index_name: str,
        *,
        account_id: str,
        ids: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Get a set of vectors from an index by their vector identifiers.

        Args:
          account_id: Identifier

          ids: A list of vector identifiers to retrieve from the index indicated by the path.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not index_name:
            raise ValueError(f"Expected a non-empty value for `index_name` but received {index_name!r}")
        return await self._post(
            f"/accounts/{account_id}/vectorize/v2/indexes/{index_name}/get_by_ids",
            body=await async_maybe_transform({"ids": ids}, index_get_by_ids_params.IndexGetByIDsParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[object]]._unwrapper,
            ),
            cast_to=cast(Type[object], ResultWrapper[object]),
        )

    async def info(
        self,
        index_name: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[IndexInfoResponse]:
        """
        Get information about a vectorize index.

        Args:
          account_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not index_name:
            raise ValueError(f"Expected a non-empty value for `index_name` but received {index_name!r}")
        return await self._get(
            f"/accounts/{account_id}/vectorize/v2/indexes/{index_name}/info",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[IndexInfoResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[IndexInfoResponse]], ResultWrapper[IndexInfoResponse]),
        )

    async def insert(
        self,
        index_name: str,
        *,
        account_id: str,
        body: str,
        unparsable_behavior: Literal["error", "discard"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[IndexInsertResponse]:
        """
        Inserts vectors into the specified index and returns a mutation id corresponding
        to the vectors enqueued for insertion.

        Args:
          account_id: Identifier

          body: ndjson file containing vectors to insert.

          unparsable_behavior: Behavior for ndjson parse failures.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not index_name:
            raise ValueError(f"Expected a non-empty value for `index_name` but received {index_name!r}")
        return await self._post(
            f"/accounts/{account_id}/vectorize/v2/indexes/{index_name}/insert",
            body=await async_maybe_transform(body, index_insert_params.IndexInsertParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"unparsable_behavior": unparsable_behavior}, index_insert_params.IndexInsertParams
                ),
                post_parser=ResultWrapper[Optional[IndexInsertResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[IndexInsertResponse]], ResultWrapper[IndexInsertResponse]),
        )

    async def query(
        self,
        index_name: str,
        *,
        account_id: str,
        vector: Iterable[float],
        filter: object | NotGiven = NOT_GIVEN,
        return_metadata: Literal["none", "indexed", "all"] | NotGiven = NOT_GIVEN,
        return_values: bool | NotGiven = NOT_GIVEN,
        top_k: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[IndexQueryResponse]:
        """
        Finds vectors closest to a given vector in an index.

        Args:
          account_id: Identifier

          vector: The search vector that will be used to find the nearest neighbors.

          filter: A metadata filter expression used to limit nearest neighbor results.

          return_metadata: Whether to return no metadata, indexed metadata or all metadata associated with
              the closest vectors.

          return_values: Whether to return the values associated with the closest vectors.

          top_k: The number of nearest neighbors to find.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not index_name:
            raise ValueError(f"Expected a non-empty value for `index_name` but received {index_name!r}")
        return await self._post(
            f"/accounts/{account_id}/vectorize/v2/indexes/{index_name}/query",
            body=await async_maybe_transform(
                {
                    "vector": vector,
                    "filter": filter,
                    "return_metadata": return_metadata,
                    "return_values": return_values,
                    "top_k": top_k,
                },
                index_query_params.IndexQueryParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[IndexQueryResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[IndexQueryResponse]], ResultWrapper[IndexQueryResponse]),
        )

    async def upsert(
        self,
        index_name: str,
        *,
        account_id: str,
        body: str,
        unparsable_behavior: Literal["error", "discard"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[IndexUpsertResponse]:
        """
        Upserts vectors into the specified index, creating them if they do not exist and
        returns a mutation id corresponding to the vectors enqueued for upsertion.

        Args:
          account_id: Identifier

          body: ndjson file containing vectors to upsert.

          unparsable_behavior: Behavior for ndjson parse failures.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not index_name:
            raise ValueError(f"Expected a non-empty value for `index_name` but received {index_name!r}")
        return await self._post(
            f"/accounts/{account_id}/vectorize/v2/indexes/{index_name}/upsert",
            body=await async_maybe_transform(body, index_upsert_params.IndexUpsertParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"unparsable_behavior": unparsable_behavior}, index_upsert_params.IndexUpsertParams
                ),
                post_parser=ResultWrapper[Optional[IndexUpsertResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[IndexUpsertResponse]], ResultWrapper[IndexUpsertResponse]),
        )


class IndexesResourceWithRawResponse:
    def __init__(self, indexes: IndexesResource) -> None:
        self._indexes = indexes

        self.create = to_raw_response_wrapper(
            indexes.create,
        )
        self.list = to_raw_response_wrapper(
            indexes.list,
        )
        self.delete = to_raw_response_wrapper(
            indexes.delete,
        )
        self.delete_by_ids = to_raw_response_wrapper(
            indexes.delete_by_ids,
        )
        self.get = to_raw_response_wrapper(
            indexes.get,
        )
        self.get_by_ids = to_raw_response_wrapper(
            indexes.get_by_ids,
        )
        self.info = to_raw_response_wrapper(
            indexes.info,
        )
        self.insert = to_raw_response_wrapper(
            indexes.insert,
        )
        self.query = to_raw_response_wrapper(
            indexes.query,
        )
        self.upsert = to_raw_response_wrapper(
            indexes.upsert,
        )

    @cached_property
    def metadata_index(self) -> MetadataIndexResourceWithRawResponse:
        return MetadataIndexResourceWithRawResponse(self._indexes.metadata_index)


class AsyncIndexesResourceWithRawResponse:
    def __init__(self, indexes: AsyncIndexesResource) -> None:
        self._indexes = indexes

        self.create = async_to_raw_response_wrapper(
            indexes.create,
        )
        self.list = async_to_raw_response_wrapper(
            indexes.list,
        )
        self.delete = async_to_raw_response_wrapper(
            indexes.delete,
        )
        self.delete_by_ids = async_to_raw_response_wrapper(
            indexes.delete_by_ids,
        )
        self.get = async_to_raw_response_wrapper(
            indexes.get,
        )
        self.get_by_ids = async_to_raw_response_wrapper(
            indexes.get_by_ids,
        )
        self.info = async_to_raw_response_wrapper(
            indexes.info,
        )
        self.insert = async_to_raw_response_wrapper(
            indexes.insert,
        )
        self.query = async_to_raw_response_wrapper(
            indexes.query,
        )
        self.upsert = async_to_raw_response_wrapper(
            indexes.upsert,
        )

    @cached_property
    def metadata_index(self) -> AsyncMetadataIndexResourceWithRawResponse:
        return AsyncMetadataIndexResourceWithRawResponse(self._indexes.metadata_index)


class IndexesResourceWithStreamingResponse:
    def __init__(self, indexes: IndexesResource) -> None:
        self._indexes = indexes

        self.create = to_streamed_response_wrapper(
            indexes.create,
        )
        self.list = to_streamed_response_wrapper(
            indexes.list,
        )
        self.delete = to_streamed_response_wrapper(
            indexes.delete,
        )
        self.delete_by_ids = to_streamed_response_wrapper(
            indexes.delete_by_ids,
        )
        self.get = to_streamed_response_wrapper(
            indexes.get,
        )
        self.get_by_ids = to_streamed_response_wrapper(
            indexes.get_by_ids,
        )
        self.info = to_streamed_response_wrapper(
            indexes.info,
        )
        self.insert = to_streamed_response_wrapper(
            indexes.insert,
        )
        self.query = to_streamed_response_wrapper(
            indexes.query,
        )
        self.upsert = to_streamed_response_wrapper(
            indexes.upsert,
        )

    @cached_property
    def metadata_index(self) -> MetadataIndexResourceWithStreamingResponse:
        return MetadataIndexResourceWithStreamingResponse(self._indexes.metadata_index)


class AsyncIndexesResourceWithStreamingResponse:
    def __init__(self, indexes: AsyncIndexesResource) -> None:
        self._indexes = indexes

        self.create = async_to_streamed_response_wrapper(
            indexes.create,
        )
        self.list = async_to_streamed_response_wrapper(
            indexes.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            indexes.delete,
        )
        self.delete_by_ids = async_to_streamed_response_wrapper(
            indexes.delete_by_ids,
        )
        self.get = async_to_streamed_response_wrapper(
            indexes.get,
        )
        self.get_by_ids = async_to_streamed_response_wrapper(
            indexes.get_by_ids,
        )
        self.info = async_to_streamed_response_wrapper(
            indexes.info,
        )
        self.insert = async_to_streamed_response_wrapper(
            indexes.insert,
        )
        self.query = async_to_streamed_response_wrapper(
            indexes.query,
        )
        self.upsert = async_to_streamed_response_wrapper(
            indexes.upsert,
        )

    @cached_property
    def metadata_index(self) -> AsyncMetadataIndexResourceWithStreamingResponse:
        return AsyncMetadataIndexResourceWithStreamingResponse(self._indexes.metadata_index)
