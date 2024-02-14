# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from .operations import Operations, AsyncOperations

from ...._compat import cached_property

from ....types.api_gateways import (
    APIShieldSchemaUploadResponse,
    APIShieldPublicSchema,
    UserSchemaListResponse,
    UserSchemaDeleteResponse,
)

from typing import Type, Optional

from ...._types import FileTypes

from typing_extensions import Literal

from ...._response import (
    to_raw_response_wrapper,
    async_to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_streamed_response_wrapper,
)

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ...._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ...._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._base_client import (
    SyncAPIClient,
    AsyncAPIClient,
    _merge_mappings,
    AsyncPaginator,
    make_request_options,
    HttpxBinaryResponseContent,
)
from ....types import shared_params
from ....types.api_gateways import user_schema_create_params
from ....types.api_gateways import user_schema_update_params
from ....types.api_gateways import user_schema_list_params
from ....types.api_gateways import user_schema_get_params
from .operations import (
    Operations,
    AsyncOperations,
    OperationsWithRawResponse,
    AsyncOperationsWithRawResponse,
    OperationsWithStreamingResponse,
    AsyncOperationsWithStreamingResponse,
)
from ...._wrappers import ResultWrapper
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast

__all__ = ["UserSchemas", "AsyncUserSchemas"]


class UserSchemas(SyncAPIResource):
    @cached_property
    def operations(self) -> Operations:
        return Operations(self._client)

    @cached_property
    def with_raw_response(self) -> UserSchemasWithRawResponse:
        return UserSchemasWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> UserSchemasWithStreamingResponse:
        return UserSchemasWithStreamingResponse(self)

    def create(
        self,
        zone_id: str,
        *,
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
    ) -> APIShieldSchemaUploadResponse:
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
        if files:
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
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[APIShieldSchemaUploadResponse], ResultWrapper[APIShieldSchemaUploadResponse]),
        )

    def update(
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
    ) -> APIShieldPublicSchema:
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
                {"validation_enabled": validation_enabled}, user_schema_update_params.UserSchemaUpdateParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[APIShieldPublicSchema], ResultWrapper[APIShieldPublicSchema]),
        )

    def list(
        self,
        zone_id: str,
        *,
        omit_source: bool | NotGiven = NOT_GIVEN,
        page: object | NotGiven = NOT_GIVEN,
        per_page: object | NotGiven = NOT_GIVEN,
        validation_enabled: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[UserSchemaListResponse]:
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
        return self._get(
            f"/zones/{zone_id}/api_gateway/user_schemas",
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
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[UserSchemaListResponse]], ResultWrapper[UserSchemaListResponse]),
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
        return cast(
            UserSchemaDeleteResponse,
            self._delete(
                f"/zones/{zone_id}/api_gateway/user_schemas/{schema_id}",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[UserSchemaDeleteResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
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
    ) -> APIShieldPublicSchema:
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
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[APIShieldPublicSchema], ResultWrapper[APIShieldPublicSchema]),
        )


class AsyncUserSchemas(AsyncAPIResource):
    @cached_property
    def operations(self) -> AsyncOperations:
        return AsyncOperations(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncUserSchemasWithRawResponse:
        return AsyncUserSchemasWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncUserSchemasWithStreamingResponse:
        return AsyncUserSchemasWithStreamingResponse(self)

    async def create(
        self,
        zone_id: str,
        *,
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
    ) -> APIShieldSchemaUploadResponse:
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
        if files:
            # It should be noted that the actual Content-Type header that will be
            # sent to the server will contain a `boundary` parameter, e.g.
            # multipart/form-data; boundary=---abc--
            extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return await self._post(
            f"/zones/{zone_id}/api_gateway/user_schemas",
            body=maybe_transform(body, user_schema_create_params.UserSchemaCreateParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[APIShieldSchemaUploadResponse], ResultWrapper[APIShieldSchemaUploadResponse]),
        )

    async def update(
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
    ) -> APIShieldPublicSchema:
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
            body=maybe_transform(
                {"validation_enabled": validation_enabled}, user_schema_update_params.UserSchemaUpdateParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[APIShieldPublicSchema], ResultWrapper[APIShieldPublicSchema]),
        )

    async def list(
        self,
        zone_id: str,
        *,
        omit_source: bool | NotGiven = NOT_GIVEN,
        page: object | NotGiven = NOT_GIVEN,
        per_page: object | NotGiven = NOT_GIVEN,
        validation_enabled: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[UserSchemaListResponse]:
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
        return await self._get(
            f"/zones/{zone_id}/api_gateway/user_schemas",
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
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[UserSchemaListResponse]], ResultWrapper[UserSchemaListResponse]),
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
        return cast(
            UserSchemaDeleteResponse,
            await self._delete(
                f"/zones/{zone_id}/api_gateway/user_schemas/{schema_id}",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[UserSchemaDeleteResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
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
    ) -> APIShieldPublicSchema:
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
                query=maybe_transform({"omit_source": omit_source}, user_schema_get_params.UserSchemaGetParams),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[APIShieldPublicSchema], ResultWrapper[APIShieldPublicSchema]),
        )


class UserSchemasWithRawResponse:
    def __init__(self, user_schemas: UserSchemas) -> None:
        self._user_schemas = user_schemas

        self.create = to_raw_response_wrapper(
            user_schemas.create,
        )
        self.update = to_raw_response_wrapper(
            user_schemas.update,
        )
        self.list = to_raw_response_wrapper(
            user_schemas.list,
        )
        self.delete = to_raw_response_wrapper(
            user_schemas.delete,
        )
        self.get = to_raw_response_wrapper(
            user_schemas.get,
        )

    @cached_property
    def operations(self) -> OperationsWithRawResponse:
        return OperationsWithRawResponse(self._user_schemas.operations)


class AsyncUserSchemasWithRawResponse:
    def __init__(self, user_schemas: AsyncUserSchemas) -> None:
        self._user_schemas = user_schemas

        self.create = async_to_raw_response_wrapper(
            user_schemas.create,
        )
        self.update = async_to_raw_response_wrapper(
            user_schemas.update,
        )
        self.list = async_to_raw_response_wrapper(
            user_schemas.list,
        )
        self.delete = async_to_raw_response_wrapper(
            user_schemas.delete,
        )
        self.get = async_to_raw_response_wrapper(
            user_schemas.get,
        )

    @cached_property
    def operations(self) -> AsyncOperationsWithRawResponse:
        return AsyncOperationsWithRawResponse(self._user_schemas.operations)


class UserSchemasWithStreamingResponse:
    def __init__(self, user_schemas: UserSchemas) -> None:
        self._user_schemas = user_schemas

        self.create = to_streamed_response_wrapper(
            user_schemas.create,
        )
        self.update = to_streamed_response_wrapper(
            user_schemas.update,
        )
        self.list = to_streamed_response_wrapper(
            user_schemas.list,
        )
        self.delete = to_streamed_response_wrapper(
            user_schemas.delete,
        )
        self.get = to_streamed_response_wrapper(
            user_schemas.get,
        )

    @cached_property
    def operations(self) -> OperationsWithStreamingResponse:
        return OperationsWithStreamingResponse(self._user_schemas.operations)


class AsyncUserSchemasWithStreamingResponse:
    def __init__(self, user_schemas: AsyncUserSchemas) -> None:
        self._user_schemas = user_schemas

        self.create = async_to_streamed_response_wrapper(
            user_schemas.create,
        )
        self.update = async_to_streamed_response_wrapper(
            user_schemas.update,
        )
        self.list = async_to_streamed_response_wrapper(
            user_schemas.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            user_schemas.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            user_schemas.get,
        )

    @cached_property
    def operations(self) -> AsyncOperationsWithStreamingResponse:
        return AsyncOperationsWithStreamingResponse(self._user_schemas.operations)
