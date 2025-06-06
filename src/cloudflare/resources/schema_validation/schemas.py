# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, cast
from typing_extensions import Literal

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._wrappers import ResultWrapper
from ...pagination import SyncV4PagePaginationArray, AsyncV4PagePaginationArray
from ..._base_client import AsyncPaginator, make_request_options
from ...types.schema_validation import schema_get_params, schema_edit_params, schema_list_params, schema_create_params
from ...types.schema_validation.schema_get_response import SchemaGetResponse
from ...types.schema_validation.schema_edit_response import SchemaEditResponse
from ...types.schema_validation.schema_list_response import SchemaListResponse
from ...types.schema_validation.schema_create_response import SchemaCreateResponse
from ...types.schema_validation.schema_delete_response import SchemaDeleteResponse

__all__ = ["SchemasResource", "AsyncSchemasResource"]


class SchemasResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SchemasResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return SchemasResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SchemasResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return SchemasResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        zone_id: str,
        kind: Literal["openapi_v3"],
        name: str,
        source: str,
        validation_enabled: bool,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SchemaCreateResponse:
        """
        Upload a schema

        Args:
          zone_id: Identifier.

          kind: The kind of the schema

          name: A human-readable name for the schema

          source: The raw schema, e.g., the OpenAPI schema, either as JSON or YAML

          validation_enabled: An indicator if this schema is enabled

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._post(
            f"/zones/{zone_id}/schema_validation/schemas",
            body=maybe_transform(
                {
                    "kind": kind,
                    "name": name,
                    "source": source,
                    "validation_enabled": validation_enabled,
                },
                schema_create_params.SchemaCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[SchemaCreateResponse]._unwrapper,
            ),
            cast_to=cast(Type[SchemaCreateResponse], ResultWrapper[SchemaCreateResponse]),
        )

    def list(
        self,
        *,
        zone_id: str,
        omit_source: bool | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        validation_enabled: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncV4PagePaginationArray[SchemaListResponse]:
        """
        List all uploaded schemas

        Args:
          zone_id: Identifier.

          omit_source: Omit the source-files of schemas and only retrieve their meta-data.

          page: Page number of paginated results.

          per_page: Maximum number of results per page.

          validation_enabled: Filter for enabled schemas

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._get_api_list(
            f"/zones/{zone_id}/schema_validation/schemas",
            page=SyncV4PagePaginationArray[SchemaListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "omit_source": omit_source,
                        "page": page,
                        "per_page": per_page,
                        "validation_enabled": validation_enabled,
                    },
                    schema_list_params.SchemaListParams,
                ),
            ),
            model=SchemaListResponse,
        )

    def delete(
        self,
        schema_id: str,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SchemaDeleteResponse:
        """
        Delete a schema

        Args:
          zone_id: Identifier.

          schema_id: UUID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not schema_id:
            raise ValueError(f"Expected a non-empty value for `schema_id` but received {schema_id!r}")
        return self._delete(
            f"/zones/{zone_id}/schema_validation/schemas/{schema_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[SchemaDeleteResponse]._unwrapper,
            ),
            cast_to=cast(Type[SchemaDeleteResponse], ResultWrapper[SchemaDeleteResponse]),
        )

    def edit(
        self,
        schema_id: str,
        *,
        zone_id: str,
        validation_enabled: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SchemaEditResponse:
        """
        Edit details of a schema to enable validation

        Args:
          zone_id: Identifier.

          schema_id: UUID.

          validation_enabled: Flag whether schema is enabled for validation.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not schema_id:
            raise ValueError(f"Expected a non-empty value for `schema_id` but received {schema_id!r}")
        return self._patch(
            f"/zones/{zone_id}/schema_validation/schemas/{schema_id}",
            body=maybe_transform({"validation_enabled": validation_enabled}, schema_edit_params.SchemaEditParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[SchemaEditResponse]._unwrapper,
            ),
            cast_to=cast(Type[SchemaEditResponse], ResultWrapper[SchemaEditResponse]),
        )

    def get(
        self,
        schema_id: str,
        *,
        zone_id: str,
        omit_source: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SchemaGetResponse:
        """
        Get details of a schema

        Args:
          zone_id: Identifier.

          schema_id: UUID.

          omit_source: Omit the source-files of schemas and only retrieve their meta-data.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not schema_id:
            raise ValueError(f"Expected a non-empty value for `schema_id` but received {schema_id!r}")
        return self._get(
            f"/zones/{zone_id}/schema_validation/schemas/{schema_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"omit_source": omit_source}, schema_get_params.SchemaGetParams),
                post_parser=ResultWrapper[SchemaGetResponse]._unwrapper,
            ),
            cast_to=cast(Type[SchemaGetResponse], ResultWrapper[SchemaGetResponse]),
        )


class AsyncSchemasResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSchemasResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSchemasResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSchemasResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncSchemasResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        zone_id: str,
        kind: Literal["openapi_v3"],
        name: str,
        source: str,
        validation_enabled: bool,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SchemaCreateResponse:
        """
        Upload a schema

        Args:
          zone_id: Identifier.

          kind: The kind of the schema

          name: A human-readable name for the schema

          source: The raw schema, e.g., the OpenAPI schema, either as JSON or YAML

          validation_enabled: An indicator if this schema is enabled

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._post(
            f"/zones/{zone_id}/schema_validation/schemas",
            body=await async_maybe_transform(
                {
                    "kind": kind,
                    "name": name,
                    "source": source,
                    "validation_enabled": validation_enabled,
                },
                schema_create_params.SchemaCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[SchemaCreateResponse]._unwrapper,
            ),
            cast_to=cast(Type[SchemaCreateResponse], ResultWrapper[SchemaCreateResponse]),
        )

    def list(
        self,
        *,
        zone_id: str,
        omit_source: bool | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        validation_enabled: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[SchemaListResponse, AsyncV4PagePaginationArray[SchemaListResponse]]:
        """
        List all uploaded schemas

        Args:
          zone_id: Identifier.

          omit_source: Omit the source-files of schemas and only retrieve their meta-data.

          page: Page number of paginated results.

          per_page: Maximum number of results per page.

          validation_enabled: Filter for enabled schemas

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._get_api_list(
            f"/zones/{zone_id}/schema_validation/schemas",
            page=AsyncV4PagePaginationArray[SchemaListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "omit_source": omit_source,
                        "page": page,
                        "per_page": per_page,
                        "validation_enabled": validation_enabled,
                    },
                    schema_list_params.SchemaListParams,
                ),
            ),
            model=SchemaListResponse,
        )

    async def delete(
        self,
        schema_id: str,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SchemaDeleteResponse:
        """
        Delete a schema

        Args:
          zone_id: Identifier.

          schema_id: UUID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not schema_id:
            raise ValueError(f"Expected a non-empty value for `schema_id` but received {schema_id!r}")
        return await self._delete(
            f"/zones/{zone_id}/schema_validation/schemas/{schema_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[SchemaDeleteResponse]._unwrapper,
            ),
            cast_to=cast(Type[SchemaDeleteResponse], ResultWrapper[SchemaDeleteResponse]),
        )

    async def edit(
        self,
        schema_id: str,
        *,
        zone_id: str,
        validation_enabled: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SchemaEditResponse:
        """
        Edit details of a schema to enable validation

        Args:
          zone_id: Identifier.

          schema_id: UUID.

          validation_enabled: Flag whether schema is enabled for validation.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not schema_id:
            raise ValueError(f"Expected a non-empty value for `schema_id` but received {schema_id!r}")
        return await self._patch(
            f"/zones/{zone_id}/schema_validation/schemas/{schema_id}",
            body=await async_maybe_transform(
                {"validation_enabled": validation_enabled}, schema_edit_params.SchemaEditParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[SchemaEditResponse]._unwrapper,
            ),
            cast_to=cast(Type[SchemaEditResponse], ResultWrapper[SchemaEditResponse]),
        )

    async def get(
        self,
        schema_id: str,
        *,
        zone_id: str,
        omit_source: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SchemaGetResponse:
        """
        Get details of a schema

        Args:
          zone_id: Identifier.

          schema_id: UUID.

          omit_source: Omit the source-files of schemas and only retrieve their meta-data.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not schema_id:
            raise ValueError(f"Expected a non-empty value for `schema_id` but received {schema_id!r}")
        return await self._get(
            f"/zones/{zone_id}/schema_validation/schemas/{schema_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"omit_source": omit_source}, schema_get_params.SchemaGetParams),
                post_parser=ResultWrapper[SchemaGetResponse]._unwrapper,
            ),
            cast_to=cast(Type[SchemaGetResponse], ResultWrapper[SchemaGetResponse]),
        )


class SchemasResourceWithRawResponse:
    def __init__(self, schemas: SchemasResource) -> None:
        self._schemas = schemas

        self.create = to_raw_response_wrapper(
            schemas.create,
        )
        self.list = to_raw_response_wrapper(
            schemas.list,
        )
        self.delete = to_raw_response_wrapper(
            schemas.delete,
        )
        self.edit = to_raw_response_wrapper(
            schemas.edit,
        )
        self.get = to_raw_response_wrapper(
            schemas.get,
        )


class AsyncSchemasResourceWithRawResponse:
    def __init__(self, schemas: AsyncSchemasResource) -> None:
        self._schemas = schemas

        self.create = async_to_raw_response_wrapper(
            schemas.create,
        )
        self.list = async_to_raw_response_wrapper(
            schemas.list,
        )
        self.delete = async_to_raw_response_wrapper(
            schemas.delete,
        )
        self.edit = async_to_raw_response_wrapper(
            schemas.edit,
        )
        self.get = async_to_raw_response_wrapper(
            schemas.get,
        )


class SchemasResourceWithStreamingResponse:
    def __init__(self, schemas: SchemasResource) -> None:
        self._schemas = schemas

        self.create = to_streamed_response_wrapper(
            schemas.create,
        )
        self.list = to_streamed_response_wrapper(
            schemas.list,
        )
        self.delete = to_streamed_response_wrapper(
            schemas.delete,
        )
        self.edit = to_streamed_response_wrapper(
            schemas.edit,
        )
        self.get = to_streamed_response_wrapper(
            schemas.get,
        )


class AsyncSchemasResourceWithStreamingResponse:
    def __init__(self, schemas: AsyncSchemasResource) -> None:
        self._schemas = schemas

        self.create = async_to_streamed_response_wrapper(
            schemas.create,
        )
        self.list = async_to_streamed_response_wrapper(
            schemas.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            schemas.delete,
        )
        self.edit = async_to_streamed_response_wrapper(
            schemas.edit,
        )
        self.get = async_to_streamed_response_wrapper(
            schemas.get,
        )
