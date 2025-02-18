# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Type, cast
from typing_extensions import Literal

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._wrappers import ResultWrapper
from ..._base_client import make_request_options
from ...types.api_gateway import schema_list_params
from ...types.api_gateway.schema_list_response import SchemaListResponse

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

    def list(
        self,
        *,
        zone_id: str,
        feature: List[Literal["thresholds", "parameter_schemas", "schema_info"]] | NotGiven = NOT_GIVEN,
        host: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SchemaListResponse:
        """
        Retrieve operations and features as OpenAPI schemas

        Args:
          zone_id: Identifier

          feature: Add feature(s) to the results. The feature name that is given here corresponds
              to the resulting feature object. Have a look at the top-level object description
              for more details on the specific meaning.

          host: Receive schema only for the given host(s).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._get(
            f"/zones/{zone_id}/api_gateway/schemas",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "feature": feature,
                        "host": host,
                    },
                    schema_list_params.SchemaListParams,
                ),
                post_parser=ResultWrapper[SchemaListResponse]._unwrapper,
            ),
            cast_to=cast(Type[SchemaListResponse], ResultWrapper[SchemaListResponse]),
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

    async def list(
        self,
        *,
        zone_id: str,
        feature: List[Literal["thresholds", "parameter_schemas", "schema_info"]] | NotGiven = NOT_GIVEN,
        host: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SchemaListResponse:
        """
        Retrieve operations and features as OpenAPI schemas

        Args:
          zone_id: Identifier

          feature: Add feature(s) to the results. The feature name that is given here corresponds
              to the resulting feature object. Have a look at the top-level object description
              for more details on the specific meaning.

          host: Receive schema only for the given host(s).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._get(
            f"/zones/{zone_id}/api_gateway/schemas",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "feature": feature,
                        "host": host,
                    },
                    schema_list_params.SchemaListParams,
                ),
                post_parser=ResultWrapper[SchemaListResponse]._unwrapper,
            ),
            cast_to=cast(Type[SchemaListResponse], ResultWrapper[SchemaListResponse]),
        )


class SchemasResourceWithRawResponse:
    def __init__(self, schemas: SchemasResource) -> None:
        self._schemas = schemas

        self.list = to_raw_response_wrapper(
            schemas.list,
        )


class AsyncSchemasResourceWithRawResponse:
    def __init__(self, schemas: AsyncSchemasResource) -> None:
        self._schemas = schemas

        self.list = async_to_raw_response_wrapper(
            schemas.list,
        )


class SchemasResourceWithStreamingResponse:
    def __init__(self, schemas: SchemasResource) -> None:
        self._schemas = schemas

        self.list = to_streamed_response_wrapper(
            schemas.list,
        )


class AsyncSchemasResourceWithStreamingResponse:
    def __init__(self, schemas: AsyncSchemasResource) -> None:
        self._schemas = schemas

        self.list = async_to_streamed_response_wrapper(
            schemas.list,
        )
