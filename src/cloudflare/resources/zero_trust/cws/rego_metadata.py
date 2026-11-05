# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, cast
from typing_extensions import Literal

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ...._utils import path_template, maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._wrappers import ResultWrapper
from ....pagination import SyncCursorPagination, AsyncCursorPagination
from ...._base_client import AsyncPaginator, make_request_options
from ....types.zero_trust.cws import rego_metadata_list_params, rego_metadata_create_params, rego_metadata_update_params
from ....types.zero_trust.cws.rego_metadata import RegoMetadata
from ....types.zero_trust.cws.rego_metadata_delete_response import RegoMetadataDeleteResponse

__all__ = ["RegoMetadataResource", "AsyncRegoMetadataResource"]


class RegoMetadataResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RegoMetadataResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return RegoMetadataResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RegoMetadataResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return RegoMetadataResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        account_id: str,
        data: object,
        import_path: str,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RegoMetadata:
        """
        Creates a JSON document that Rego can access through its import path.

        Args:
          account_id: Cloudflare account ID (32-character hexadecimal string)

          import_path: Unique Rego import path in the form metadata.<segment>, with one alphanumeric or
              underscore segment. Reference it as data.<import_path>.

          name: Name of the rego metadata document (unique per account)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._post(
            path_template("/accounts/{account_id}/cws/rego-metadata", account_id=account_id),
            body=maybe_transform(
                {
                    "data": data,
                    "import_path": import_path,
                    "name": name,
                },
                rego_metadata_create_params.RegoMetadataCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[RegoMetadata]._unwrapper,
            ),
            cast_to=cast(Type[RegoMetadata], ResultWrapper[RegoMetadata]),
        )

    def update(
        self,
        rego_metadata_id: str,
        *,
        account_id: str,
        data: object,
        import_path: str,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RegoMetadata:
        """
        Replaces the metadata document's name, import path, and JSON data.

        Args:
          account_id: Cloudflare account ID (32-character hexadecimal string)

          rego_metadata_id: ID of the rego metadata document to update

          import_path: Unique Rego import path in the form metadata.<segment>, with one alphanumeric or
              underscore segment. Reference it as data.<import_path>.

          name: Name of the rego metadata document (unique per account)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not rego_metadata_id:
            raise ValueError(f"Expected a non-empty value for `rego_metadata_id` but received {rego_metadata_id!r}")
        return self._put(
            path_template(
                "/accounts/{account_id}/cws/rego-metadata/{rego_metadata_id}",
                account_id=account_id,
                rego_metadata_id=rego_metadata_id,
            ),
            body=maybe_transform(
                {
                    "data": data,
                    "import_path": import_path,
                    "name": name,
                },
                rego_metadata_update_params.RegoMetadataUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[RegoMetadata]._unwrapper,
            ),
            cast_to=cast(Type[RegoMetadata], ResultWrapper[RegoMetadata]),
        )

    def list(
        self,
        *,
        account_id: str,
        cursor: str | Omit = omit,
        direction: Literal["asc", "desc"] | Omit = omit,
        import_path: str | Omit = omit,
        name: str | Omit = omit,
        order: Literal["name", "created_at", "updated_at"] | Omit = omit,
        per_page: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorPagination[RegoMetadata]:
        """
        Returns a paginated list of Rego metadata documents in the account.

        Args:
          account_id: Cloudflare account ID (32-character hexadecimal string)

          cursor: Pagination cursor from previous response

          direction: Sort direction (default: asc)

          import_path: Filter by import path (case-sensitive literal substring match)

          name: Filter by rego metadata name (case-insensitive substring match)

          order: Field to order results by (default: created_at)

          per_page: Number of items per page (1-100, default 20)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            path_template("/accounts/{account_id}/cws/rego-metadata", account_id=account_id),
            page=SyncCursorPagination[RegoMetadata],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "direction": direction,
                        "import_path": import_path,
                        "name": name,
                        "order": order,
                        "per_page": per_page,
                    },
                    rego_metadata_list_params.RegoMetadataListParams,
                ),
            ),
            model=RegoMetadata,
        )

    def delete(
        self,
        rego_metadata_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RegoMetadataDeleteResponse:
        """
        Deletes the specified Rego metadata document.

        Args:
          account_id: Cloudflare account ID (32-character hexadecimal string)

          rego_metadata_id: ID of the rego metadata document to delete

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not rego_metadata_id:
            raise ValueError(f"Expected a non-empty value for `rego_metadata_id` but received {rego_metadata_id!r}")
        return self._delete(
            path_template(
                "/accounts/{account_id}/cws/rego-metadata/{rego_metadata_id}",
                account_id=account_id,
                rego_metadata_id=rego_metadata_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[RegoMetadataDeleteResponse]._unwrapper,
            ),
            cast_to=cast(Type[RegoMetadataDeleteResponse], ResultWrapper[RegoMetadataDeleteResponse]),
        )

    def get(
        self,
        rego_metadata_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RegoMetadata:
        """
        Returns the Rego metadata document with the specified ID.

        Args:
          account_id: Cloudflare account ID (32-character hexadecimal string)

          rego_metadata_id: ID of the rego metadata document to retrieve

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not rego_metadata_id:
            raise ValueError(f"Expected a non-empty value for `rego_metadata_id` but received {rego_metadata_id!r}")
        return self._get(
            path_template(
                "/accounts/{account_id}/cws/rego-metadata/{rego_metadata_id}",
                account_id=account_id,
                rego_metadata_id=rego_metadata_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[RegoMetadata]._unwrapper,
            ),
            cast_to=cast(Type[RegoMetadata], ResultWrapper[RegoMetadata]),
        )


class AsyncRegoMetadataResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRegoMetadataResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRegoMetadataResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRegoMetadataResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncRegoMetadataResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_id: str,
        data: object,
        import_path: str,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RegoMetadata:
        """
        Creates a JSON document that Rego can access through its import path.

        Args:
          account_id: Cloudflare account ID (32-character hexadecimal string)

          import_path: Unique Rego import path in the form metadata.<segment>, with one alphanumeric or
              underscore segment. Reference it as data.<import_path>.

          name: Name of the rego metadata document (unique per account)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._post(
            path_template("/accounts/{account_id}/cws/rego-metadata", account_id=account_id),
            body=await async_maybe_transform(
                {
                    "data": data,
                    "import_path": import_path,
                    "name": name,
                },
                rego_metadata_create_params.RegoMetadataCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[RegoMetadata]._unwrapper,
            ),
            cast_to=cast(Type[RegoMetadata], ResultWrapper[RegoMetadata]),
        )

    async def update(
        self,
        rego_metadata_id: str,
        *,
        account_id: str,
        data: object,
        import_path: str,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RegoMetadata:
        """
        Replaces the metadata document's name, import path, and JSON data.

        Args:
          account_id: Cloudflare account ID (32-character hexadecimal string)

          rego_metadata_id: ID of the rego metadata document to update

          import_path: Unique Rego import path in the form metadata.<segment>, with one alphanumeric or
              underscore segment. Reference it as data.<import_path>.

          name: Name of the rego metadata document (unique per account)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not rego_metadata_id:
            raise ValueError(f"Expected a non-empty value for `rego_metadata_id` but received {rego_metadata_id!r}")
        return await self._put(
            path_template(
                "/accounts/{account_id}/cws/rego-metadata/{rego_metadata_id}",
                account_id=account_id,
                rego_metadata_id=rego_metadata_id,
            ),
            body=await async_maybe_transform(
                {
                    "data": data,
                    "import_path": import_path,
                    "name": name,
                },
                rego_metadata_update_params.RegoMetadataUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[RegoMetadata]._unwrapper,
            ),
            cast_to=cast(Type[RegoMetadata], ResultWrapper[RegoMetadata]),
        )

    def list(
        self,
        *,
        account_id: str,
        cursor: str | Omit = omit,
        direction: Literal["asc", "desc"] | Omit = omit,
        import_path: str | Omit = omit,
        name: str | Omit = omit,
        order: Literal["name", "created_at", "updated_at"] | Omit = omit,
        per_page: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[RegoMetadata, AsyncCursorPagination[RegoMetadata]]:
        """
        Returns a paginated list of Rego metadata documents in the account.

        Args:
          account_id: Cloudflare account ID (32-character hexadecimal string)

          cursor: Pagination cursor from previous response

          direction: Sort direction (default: asc)

          import_path: Filter by import path (case-sensitive literal substring match)

          name: Filter by rego metadata name (case-insensitive substring match)

          order: Field to order results by (default: created_at)

          per_page: Number of items per page (1-100, default 20)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            path_template("/accounts/{account_id}/cws/rego-metadata", account_id=account_id),
            page=AsyncCursorPagination[RegoMetadata],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "direction": direction,
                        "import_path": import_path,
                        "name": name,
                        "order": order,
                        "per_page": per_page,
                    },
                    rego_metadata_list_params.RegoMetadataListParams,
                ),
            ),
            model=RegoMetadata,
        )

    async def delete(
        self,
        rego_metadata_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RegoMetadataDeleteResponse:
        """
        Deletes the specified Rego metadata document.

        Args:
          account_id: Cloudflare account ID (32-character hexadecimal string)

          rego_metadata_id: ID of the rego metadata document to delete

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not rego_metadata_id:
            raise ValueError(f"Expected a non-empty value for `rego_metadata_id` but received {rego_metadata_id!r}")
        return await self._delete(
            path_template(
                "/accounts/{account_id}/cws/rego-metadata/{rego_metadata_id}",
                account_id=account_id,
                rego_metadata_id=rego_metadata_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[RegoMetadataDeleteResponse]._unwrapper,
            ),
            cast_to=cast(Type[RegoMetadataDeleteResponse], ResultWrapper[RegoMetadataDeleteResponse]),
        )

    async def get(
        self,
        rego_metadata_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RegoMetadata:
        """
        Returns the Rego metadata document with the specified ID.

        Args:
          account_id: Cloudflare account ID (32-character hexadecimal string)

          rego_metadata_id: ID of the rego metadata document to retrieve

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not rego_metadata_id:
            raise ValueError(f"Expected a non-empty value for `rego_metadata_id` but received {rego_metadata_id!r}")
        return await self._get(
            path_template(
                "/accounts/{account_id}/cws/rego-metadata/{rego_metadata_id}",
                account_id=account_id,
                rego_metadata_id=rego_metadata_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[RegoMetadata]._unwrapper,
            ),
            cast_to=cast(Type[RegoMetadata], ResultWrapper[RegoMetadata]),
        )


class RegoMetadataResourceWithRawResponse:
    def __init__(self, rego_metadata: RegoMetadataResource) -> None:
        self._rego_metadata = rego_metadata

        self.create = to_raw_response_wrapper(
            rego_metadata.create,
        )
        self.update = to_raw_response_wrapper(
            rego_metadata.update,
        )
        self.list = to_raw_response_wrapper(
            rego_metadata.list,
        )
        self.delete = to_raw_response_wrapper(
            rego_metadata.delete,
        )
        self.get = to_raw_response_wrapper(
            rego_metadata.get,
        )


class AsyncRegoMetadataResourceWithRawResponse:
    def __init__(self, rego_metadata: AsyncRegoMetadataResource) -> None:
        self._rego_metadata = rego_metadata

        self.create = async_to_raw_response_wrapper(
            rego_metadata.create,
        )
        self.update = async_to_raw_response_wrapper(
            rego_metadata.update,
        )
        self.list = async_to_raw_response_wrapper(
            rego_metadata.list,
        )
        self.delete = async_to_raw_response_wrapper(
            rego_metadata.delete,
        )
        self.get = async_to_raw_response_wrapper(
            rego_metadata.get,
        )


class RegoMetadataResourceWithStreamingResponse:
    def __init__(self, rego_metadata: RegoMetadataResource) -> None:
        self._rego_metadata = rego_metadata

        self.create = to_streamed_response_wrapper(
            rego_metadata.create,
        )
        self.update = to_streamed_response_wrapper(
            rego_metadata.update,
        )
        self.list = to_streamed_response_wrapper(
            rego_metadata.list,
        )
        self.delete = to_streamed_response_wrapper(
            rego_metadata.delete,
        )
        self.get = to_streamed_response_wrapper(
            rego_metadata.get,
        )


class AsyncRegoMetadataResourceWithStreamingResponse:
    def __init__(self, rego_metadata: AsyncRegoMetadataResource) -> None:
        self._rego_metadata = rego_metadata

        self.create = async_to_streamed_response_wrapper(
            rego_metadata.create,
        )
        self.update = async_to_streamed_response_wrapper(
            rego_metadata.update,
        )
        self.list = async_to_streamed_response_wrapper(
            rego_metadata.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            rego_metadata.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            rego_metadata.get,
        )
