# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Type, Optional, cast

import httpx

from .content import (
    ContentResource,
    AsyncContentResource,
    ContentResourceWithRawResponse,
    AsyncContentResourceWithRawResponse,
    ContentResourceWithStreamingResponse,
    AsyncContentResourceWithStreamingResponse,
)
from .versions import (
    VersionsResource,
    AsyncVersionsResource,
    VersionsResourceWithRawResponse,
    AsyncVersionsResourceWithRawResponse,
    VersionsResourceWithStreamingResponse,
    AsyncVersionsResourceWithStreamingResponse,
)
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
from ....pagination import SyncSinglePage, AsyncSinglePage
from ...._base_client import AsyncPaginator, make_request_options
from ....types.logpush import transformer_create_params, transformer_update_params, transformer_preview_params
from ....types.logpush.transformer_get_response import TransformerGetResponse
from ....types.logpush.transformer_list_response import TransformerListResponse
from ....types.logpush.transformer_create_response import TransformerCreateResponse
from ....types.logpush.transformer_delete_response import TransformerDeleteResponse
from ....types.logpush.transformer_update_response import TransformerUpdateResponse
from ....types.logpush.transformer_preview_response import TransformerPreviewResponse

__all__ = ["TransformersResource", "AsyncTransformersResource"]


class TransformersResource(SyncAPIResource):
    @cached_property
    def content(self) -> ContentResource:
        return ContentResource(self._client)

    @cached_property
    def versions(self) -> VersionsResource:
        return VersionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> TransformersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return TransformersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TransformersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return TransformersResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        account_id: str,
        code: str,
        name: str,
        description: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[TransformerCreateResponse]:
        """
        Creates a new custom log transformer for an account.

        Args:
          account_id: Identifier.

          code: The SQL transformer query. Maximum 32 KB. The query must contain a FROM clause
              referencing a valid logpush dataset.

          name: Customer-provided name for identification.

          description: Optional customer-provided description.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._post(
            path_template("/accounts/{account_id}/logpush/transformers", account_id=account_id),
            body=maybe_transform(
                {
                    "code": code,
                    "name": name,
                    "description": description,
                },
                transformer_create_params.TransformerCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[TransformerCreateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[TransformerCreateResponse]], ResultWrapper[TransformerCreateResponse]),
        )

    def update(
        self,
        transformer_id: int,
        *,
        account_id: str,
        name: str,
        code: str | Omit = omit,
        description: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[TransformerUpdateResponse]:
        """Updates an existing custom log transformer.

        When `code` is provided, the SQL
        query is validated and a new version is created. When `code` is omitted, only
        the name and description are updated. Omitting `description` clears the existing
        description.

        Args:
          account_id: Identifier.

          transformer_id: The transformer ID.

          name: Customer-provided name for identification.

          code: The SQL transformer query. Maximum 32 KB. The query must contain a FROM clause
              referencing a valid logpush dataset.

          description: Optional customer-provided description.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._put(
            path_template(
                "/accounts/{account_id}/logpush/transformers/{transformer_id}",
                account_id=account_id,
                transformer_id=transformer_id,
            ),
            body=maybe_transform(
                {
                    "name": name,
                    "code": code,
                    "description": description,
                },
                transformer_update_params.TransformerUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[TransformerUpdateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[TransformerUpdateResponse]], ResultWrapper[TransformerUpdateResponse]),
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncSinglePage[TransformerListResponse]:
        """
        Lists all custom log transformers for an account.

        Args:
          account_id: Identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            path_template("/accounts/{account_id}/logpush/transformers", account_id=account_id),
            page=SyncSinglePage[TransformerListResponse],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=TransformerListResponse,
        )

    def delete(
        self,
        transformer_id: int,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[TransformerDeleteResponse]:
        """Deletes a custom log transformer.

        Returns 409 Conflict if any active logpush
        jobs reference the transformer.

        Args:
          account_id: Identifier.

          transformer_id: The transformer ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._delete(
            path_template(
                "/accounts/{account_id}/logpush/transformers/{transformer_id}",
                account_id=account_id,
                transformer_id=transformer_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[TransformerDeleteResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[TransformerDeleteResponse]], ResultWrapper[TransformerDeleteResponse]),
        )

    def get(
        self,
        transformer_id: int,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[TransformerGetResponse]:
        """
        Gets a single custom log transformer by ID.

        Args:
          account_id: Identifier.

          transformer_id: The transformer ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get(
            path_template(
                "/accounts/{account_id}/logpush/transformers/{transformer_id}",
                account_id=account_id,
                transformer_id=transformer_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[TransformerGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[TransformerGetResponse]], ResultWrapper[TransformerGetResponse]),
        )

    def preview(
        self,
        *,
        account_id: str,
        input: Dict[str, object],
        sql: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncSinglePage[TransformerPreviewResponse]:
        """
        Executes a SQL transformer against a single input record and returns the
        transformed output. This is a stateless endpoint — nothing is persisted.

        Args:
          account_id: Identifier.

          input: A single log record to transform (JSON object).

          sql: The SQL transformer query. Maximum 32 KB. The query must contain a FROM clause
              referencing a valid logpush dataset.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            path_template("/accounts/{account_id}/logpush/transformers/preview", account_id=account_id),
            page=SyncSinglePage[TransformerPreviewResponse],
            body=maybe_transform(
                {
                    "input": input,
                    "sql": sql,
                },
                transformer_preview_params.TransformerPreviewParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=TransformerPreviewResponse,
            method="post",
        )


class AsyncTransformersResource(AsyncAPIResource):
    @cached_property
    def content(self) -> AsyncContentResource:
        return AsyncContentResource(self._client)

    @cached_property
    def versions(self) -> AsyncVersionsResource:
        return AsyncVersionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncTransformersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTransformersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTransformersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncTransformersResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_id: str,
        code: str,
        name: str,
        description: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[TransformerCreateResponse]:
        """
        Creates a new custom log transformer for an account.

        Args:
          account_id: Identifier.

          code: The SQL transformer query. Maximum 32 KB. The query must contain a FROM clause
              referencing a valid logpush dataset.

          name: Customer-provided name for identification.

          description: Optional customer-provided description.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._post(
            path_template("/accounts/{account_id}/logpush/transformers", account_id=account_id),
            body=await async_maybe_transform(
                {
                    "code": code,
                    "name": name,
                    "description": description,
                },
                transformer_create_params.TransformerCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[TransformerCreateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[TransformerCreateResponse]], ResultWrapper[TransformerCreateResponse]),
        )

    async def update(
        self,
        transformer_id: int,
        *,
        account_id: str,
        name: str,
        code: str | Omit = omit,
        description: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[TransformerUpdateResponse]:
        """Updates an existing custom log transformer.

        When `code` is provided, the SQL
        query is validated and a new version is created. When `code` is omitted, only
        the name and description are updated. Omitting `description` clears the existing
        description.

        Args:
          account_id: Identifier.

          transformer_id: The transformer ID.

          name: Customer-provided name for identification.

          code: The SQL transformer query. Maximum 32 KB. The query must contain a FROM clause
              referencing a valid logpush dataset.

          description: Optional customer-provided description.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._put(
            path_template(
                "/accounts/{account_id}/logpush/transformers/{transformer_id}",
                account_id=account_id,
                transformer_id=transformer_id,
            ),
            body=await async_maybe_transform(
                {
                    "name": name,
                    "code": code,
                    "description": description,
                },
                transformer_update_params.TransformerUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[TransformerUpdateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[TransformerUpdateResponse]], ResultWrapper[TransformerUpdateResponse]),
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[TransformerListResponse, AsyncSinglePage[TransformerListResponse]]:
        """
        Lists all custom log transformers for an account.

        Args:
          account_id: Identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            path_template("/accounts/{account_id}/logpush/transformers", account_id=account_id),
            page=AsyncSinglePage[TransformerListResponse],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=TransformerListResponse,
        )

    async def delete(
        self,
        transformer_id: int,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[TransformerDeleteResponse]:
        """Deletes a custom log transformer.

        Returns 409 Conflict if any active logpush
        jobs reference the transformer.

        Args:
          account_id: Identifier.

          transformer_id: The transformer ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._delete(
            path_template(
                "/accounts/{account_id}/logpush/transformers/{transformer_id}",
                account_id=account_id,
                transformer_id=transformer_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[TransformerDeleteResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[TransformerDeleteResponse]], ResultWrapper[TransformerDeleteResponse]),
        )

    async def get(
        self,
        transformer_id: int,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[TransformerGetResponse]:
        """
        Gets a single custom log transformer by ID.

        Args:
          account_id: Identifier.

          transformer_id: The transformer ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._get(
            path_template(
                "/accounts/{account_id}/logpush/transformers/{transformer_id}",
                account_id=account_id,
                transformer_id=transformer_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[TransformerGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[TransformerGetResponse]], ResultWrapper[TransformerGetResponse]),
        )

    def preview(
        self,
        *,
        account_id: str,
        input: Dict[str, object],
        sql: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[TransformerPreviewResponse, AsyncSinglePage[TransformerPreviewResponse]]:
        """
        Executes a SQL transformer against a single input record and returns the
        transformed output. This is a stateless endpoint — nothing is persisted.

        Args:
          account_id: Identifier.

          input: A single log record to transform (JSON object).

          sql: The SQL transformer query. Maximum 32 KB. The query must contain a FROM clause
              referencing a valid logpush dataset.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            path_template("/accounts/{account_id}/logpush/transformers/preview", account_id=account_id),
            page=AsyncSinglePage[TransformerPreviewResponse],
            body=maybe_transform(
                {
                    "input": input,
                    "sql": sql,
                },
                transformer_preview_params.TransformerPreviewParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=TransformerPreviewResponse,
            method="post",
        )


class TransformersResourceWithRawResponse:
    def __init__(self, transformers: TransformersResource) -> None:
        self._transformers = transformers

        self.create = to_raw_response_wrapper(
            transformers.create,
        )
        self.update = to_raw_response_wrapper(
            transformers.update,
        )
        self.list = to_raw_response_wrapper(
            transformers.list,
        )
        self.delete = to_raw_response_wrapper(
            transformers.delete,
        )
        self.get = to_raw_response_wrapper(
            transformers.get,
        )
        self.preview = to_raw_response_wrapper(
            transformers.preview,
        )

    @cached_property
    def content(self) -> ContentResourceWithRawResponse:
        return ContentResourceWithRawResponse(self._transformers.content)

    @cached_property
    def versions(self) -> VersionsResourceWithRawResponse:
        return VersionsResourceWithRawResponse(self._transformers.versions)


class AsyncTransformersResourceWithRawResponse:
    def __init__(self, transformers: AsyncTransformersResource) -> None:
        self._transformers = transformers

        self.create = async_to_raw_response_wrapper(
            transformers.create,
        )
        self.update = async_to_raw_response_wrapper(
            transformers.update,
        )
        self.list = async_to_raw_response_wrapper(
            transformers.list,
        )
        self.delete = async_to_raw_response_wrapper(
            transformers.delete,
        )
        self.get = async_to_raw_response_wrapper(
            transformers.get,
        )
        self.preview = async_to_raw_response_wrapper(
            transformers.preview,
        )

    @cached_property
    def content(self) -> AsyncContentResourceWithRawResponse:
        return AsyncContentResourceWithRawResponse(self._transformers.content)

    @cached_property
    def versions(self) -> AsyncVersionsResourceWithRawResponse:
        return AsyncVersionsResourceWithRawResponse(self._transformers.versions)


class TransformersResourceWithStreamingResponse:
    def __init__(self, transformers: TransformersResource) -> None:
        self._transformers = transformers

        self.create = to_streamed_response_wrapper(
            transformers.create,
        )
        self.update = to_streamed_response_wrapper(
            transformers.update,
        )
        self.list = to_streamed_response_wrapper(
            transformers.list,
        )
        self.delete = to_streamed_response_wrapper(
            transformers.delete,
        )
        self.get = to_streamed_response_wrapper(
            transformers.get,
        )
        self.preview = to_streamed_response_wrapper(
            transformers.preview,
        )

    @cached_property
    def content(self) -> ContentResourceWithStreamingResponse:
        return ContentResourceWithStreamingResponse(self._transformers.content)

    @cached_property
    def versions(self) -> VersionsResourceWithStreamingResponse:
        return VersionsResourceWithStreamingResponse(self._transformers.versions)


class AsyncTransformersResourceWithStreamingResponse:
    def __init__(self, transformers: AsyncTransformersResource) -> None:
        self._transformers = transformers

        self.create = async_to_streamed_response_wrapper(
            transformers.create,
        )
        self.update = async_to_streamed_response_wrapper(
            transformers.update,
        )
        self.list = async_to_streamed_response_wrapper(
            transformers.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            transformers.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            transformers.get,
        )
        self.preview = async_to_streamed_response_wrapper(
            transformers.preview,
        )

    @cached_property
    def content(self) -> AsyncContentResourceWithStreamingResponse:
        return AsyncContentResourceWithStreamingResponse(self._transformers.content)

    @cached_property
    def versions(self) -> AsyncVersionsResourceWithStreamingResponse:
        return AsyncVersionsResourceWithStreamingResponse(self._transformers.versions)
