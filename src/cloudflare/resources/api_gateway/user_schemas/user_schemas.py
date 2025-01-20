# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Mapping, cast
from typing_extensions import Literal

import httpx

from .hosts import (
    HostsResource,
    AsyncHostsResource,
    HostsResourceWithRawResponse,
    AsyncHostsResourceWithRawResponse,
    HostsResourceWithStreamingResponse,
    AsyncHostsResourceWithStreamingResponse,
)
from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven, FileTypes
from ...._utils import (
    extract_files,
    maybe_transform,
    deepcopy_minimal,
    async_maybe_transform,
)
from ...._compat import cached_property
from .operations import (
    OperationsResource,
    AsyncOperationsResource,
    OperationsResourceWithRawResponse,
    AsyncOperationsResourceWithRawResponse,
    OperationsResourceWithStreamingResponse,
    AsyncOperationsResourceWithStreamingResponse,
)
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._wrappers import ResultWrapper
from ....pagination import SyncV4PagePaginationArray, AsyncV4PagePaginationArray
from ...._base_client import AsyncPaginator, make_request_options
from ....types.api_gateway import (
    user_schema_get_params,
    user_schema_edit_params,
    user_schema_list_params,
    user_schema_create_params,
)
from ....types.api_gateway.public_schema import PublicSchema
from ....types.api_gateway.schema_upload import SchemaUpload
from ....types.api_gateway.user_schema_delete_response import UserSchemaDeleteResponse

__all__ = ["UserSchemasResource", "AsyncUserSchemasResource"]


class UserSchemasResource(SyncAPIResource):
    @cached_property
    def operations(self) -> OperationsResource:
        return OperationsResource(self._client)

    @cached_property
    def hosts(self) -> HostsResource:
        return HostsResource(self._client)

    @cached_property
    def with_raw_response(self) -> UserSchemasResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return UserSchemasResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> UserSchemasResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return UserSchemasResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        zone_id: str,
        file: FileTypes,
        kind: Literal["openapi_v3"],
        name: str | NotGiven = NOT_GIVEN,
        validation_enabled: Literal["true", "false"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SchemaUpload:
        """
        Upload a schema to a zone

        Args:
          zone_id: Identifier

          file: Schema file bytes

          kind: Kind of schema

          name: Name of the schema

          validation_enabled: Flag whether schema is enabled for validation.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        body = deepcopy_minimal(
            {
                "file": file,
                "kind": kind,
                "name": name,
                "validation_enabled": validation_enabled,
            }
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["file"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return self._post(
            f"/zones/{zone_id}/api_gateway/user_schemas",
            body=maybe_transform(body, user_schema_create_params.UserSchemaCreateParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[SchemaUpload]._unwrapper,
            ),
            cast_to=cast(Type[SchemaUpload], ResultWrapper[SchemaUpload]),
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
    ) -> SyncV4PagePaginationArray[PublicSchema]:
        """
        Retrieve information about all schemas on a zone

        Args:
          zone_id: Identifier

          omit_source: Omit the source-files of schemas and only retrieve their meta-data.

          page: Page number of paginated results.

          per_page: Maximum number of results per page.

          validation_enabled: Flag whether schema is enabled for validation.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._get_api_list(
            f"/zones/{zone_id}/api_gateway/user_schemas",
            page=SyncV4PagePaginationArray[PublicSchema],
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
                    user_schema_list_params.UserSchemaListParams,
                ),
            ),
            model=PublicSchema,
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
    ) -> UserSchemaDeleteResponse:
        """
        Delete a schema

        Args:
          zone_id: Identifier

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
            f"/zones/{zone_id}/api_gateway/user_schemas/{schema_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserSchemaDeleteResponse,
        )

    def edit(
        self,
        schema_id: str,
        *,
        zone_id: str,
        validation_enabled: Literal[True] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PublicSchema:
        """
        Enable validation for a schema

        Args:
          zone_id: Identifier

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
            f"/zones/{zone_id}/api_gateway/user_schemas/{schema_id}",
            body=maybe_transform(
                {"validation_enabled": validation_enabled}, user_schema_edit_params.UserSchemaEditParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[PublicSchema]._unwrapper,
            ),
            cast_to=cast(Type[PublicSchema], ResultWrapper[PublicSchema]),
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
    ) -> PublicSchema:
        """
        Retrieve information about a specific schema on a zone

        Args:
          zone_id: Identifier

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
            f"/zones/{zone_id}/api_gateway/user_schemas/{schema_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"omit_source": omit_source}, user_schema_get_params.UserSchemaGetParams),
                post_parser=ResultWrapper[PublicSchema]._unwrapper,
            ),
            cast_to=cast(Type[PublicSchema], ResultWrapper[PublicSchema]),
        )


class AsyncUserSchemasResource(AsyncAPIResource):
    @cached_property
    def operations(self) -> AsyncOperationsResource:
        return AsyncOperationsResource(self._client)

    @cached_property
    def hosts(self) -> AsyncHostsResource:
        return AsyncHostsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncUserSchemasResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncUserSchemasResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncUserSchemasResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncUserSchemasResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        zone_id: str,
        file: FileTypes,
        kind: Literal["openapi_v3"],
        name: str | NotGiven = NOT_GIVEN,
        validation_enabled: Literal["true", "false"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SchemaUpload:
        """
        Upload a schema to a zone

        Args:
          zone_id: Identifier

          file: Schema file bytes

          kind: Kind of schema

          name: Name of the schema

          validation_enabled: Flag whether schema is enabled for validation.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        body = deepcopy_minimal(
            {
                "file": file,
                "kind": kind,
                "name": name,
                "validation_enabled": validation_enabled,
            }
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["file"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return await self._post(
            f"/zones/{zone_id}/api_gateway/user_schemas",
            body=await async_maybe_transform(body, user_schema_create_params.UserSchemaCreateParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[SchemaUpload]._unwrapper,
            ),
            cast_to=cast(Type[SchemaUpload], ResultWrapper[SchemaUpload]),
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
    ) -> AsyncPaginator[PublicSchema, AsyncV4PagePaginationArray[PublicSchema]]:
        """
        Retrieve information about all schemas on a zone

        Args:
          zone_id: Identifier

          omit_source: Omit the source-files of schemas and only retrieve their meta-data.

          page: Page number of paginated results.

          per_page: Maximum number of results per page.

          validation_enabled: Flag whether schema is enabled for validation.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._get_api_list(
            f"/zones/{zone_id}/api_gateway/user_schemas",
            page=AsyncV4PagePaginationArray[PublicSchema],
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
                    user_schema_list_params.UserSchemaListParams,
                ),
            ),
            model=PublicSchema,
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
    ) -> UserSchemaDeleteResponse:
        """
        Delete a schema

        Args:
          zone_id: Identifier

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
            f"/zones/{zone_id}/api_gateway/user_schemas/{schema_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserSchemaDeleteResponse,
        )

    async def edit(
        self,
        schema_id: str,
        *,
        zone_id: str,
        validation_enabled: Literal[True] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PublicSchema:
        """
        Enable validation for a schema

        Args:
          zone_id: Identifier

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
            f"/zones/{zone_id}/api_gateway/user_schemas/{schema_id}",
            body=await async_maybe_transform(
                {"validation_enabled": validation_enabled}, user_schema_edit_params.UserSchemaEditParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[PublicSchema]._unwrapper,
            ),
            cast_to=cast(Type[PublicSchema], ResultWrapper[PublicSchema]),
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
    ) -> PublicSchema:
        """
        Retrieve information about a specific schema on a zone

        Args:
          zone_id: Identifier

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
            f"/zones/{zone_id}/api_gateway/user_schemas/{schema_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"omit_source": omit_source}, user_schema_get_params.UserSchemaGetParams
                ),
                post_parser=ResultWrapper[PublicSchema]._unwrapper,
            ),
            cast_to=cast(Type[PublicSchema], ResultWrapper[PublicSchema]),
        )


class UserSchemasResourceWithRawResponse:
    def __init__(self, user_schemas: UserSchemasResource) -> None:
        self._user_schemas = user_schemas

        self.create = to_raw_response_wrapper(
            user_schemas.create,
        )
        self.list = to_raw_response_wrapper(
            user_schemas.list,
        )
        self.delete = to_raw_response_wrapper(
            user_schemas.delete,
        )
        self.edit = to_raw_response_wrapper(
            user_schemas.edit,
        )
        self.get = to_raw_response_wrapper(
            user_schemas.get,
        )

    @cached_property
    def operations(self) -> OperationsResourceWithRawResponse:
        return OperationsResourceWithRawResponse(self._user_schemas.operations)

    @cached_property
    def hosts(self) -> HostsResourceWithRawResponse:
        return HostsResourceWithRawResponse(self._user_schemas.hosts)


class AsyncUserSchemasResourceWithRawResponse:
    def __init__(self, user_schemas: AsyncUserSchemasResource) -> None:
        self._user_schemas = user_schemas

        self.create = async_to_raw_response_wrapper(
            user_schemas.create,
        )
        self.list = async_to_raw_response_wrapper(
            user_schemas.list,
        )
        self.delete = async_to_raw_response_wrapper(
            user_schemas.delete,
        )
        self.edit = async_to_raw_response_wrapper(
            user_schemas.edit,
        )
        self.get = async_to_raw_response_wrapper(
            user_schemas.get,
        )

    @cached_property
    def operations(self) -> AsyncOperationsResourceWithRawResponse:
        return AsyncOperationsResourceWithRawResponse(self._user_schemas.operations)

    @cached_property
    def hosts(self) -> AsyncHostsResourceWithRawResponse:
        return AsyncHostsResourceWithRawResponse(self._user_schemas.hosts)


class UserSchemasResourceWithStreamingResponse:
    def __init__(self, user_schemas: UserSchemasResource) -> None:
        self._user_schemas = user_schemas

        self.create = to_streamed_response_wrapper(
            user_schemas.create,
        )
        self.list = to_streamed_response_wrapper(
            user_schemas.list,
        )
        self.delete = to_streamed_response_wrapper(
            user_schemas.delete,
        )
        self.edit = to_streamed_response_wrapper(
            user_schemas.edit,
        )
        self.get = to_streamed_response_wrapper(
            user_schemas.get,
        )

    @cached_property
    def operations(self) -> OperationsResourceWithStreamingResponse:
        return OperationsResourceWithStreamingResponse(self._user_schemas.operations)

    @cached_property
    def hosts(self) -> HostsResourceWithStreamingResponse:
        return HostsResourceWithStreamingResponse(self._user_schemas.hosts)


class AsyncUserSchemasResourceWithStreamingResponse:
    def __init__(self, user_schemas: AsyncUserSchemasResource) -> None:
        self._user_schemas = user_schemas

        self.create = async_to_streamed_response_wrapper(
            user_schemas.create,
        )
        self.list = async_to_streamed_response_wrapper(
            user_schemas.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            user_schemas.delete,
        )
        self.edit = async_to_streamed_response_wrapper(
            user_schemas.edit,
        )
        self.get = async_to_streamed_response_wrapper(
            user_schemas.get,
        )

    @cached_property
    def operations(self) -> AsyncOperationsResourceWithStreamingResponse:
        return AsyncOperationsResourceWithStreamingResponse(self._user_schemas.operations)

    @cached_property
    def hosts(self) -> AsyncHostsResourceWithStreamingResponse:
        return AsyncHostsResourceWithStreamingResponse(self._user_schemas.hosts)
