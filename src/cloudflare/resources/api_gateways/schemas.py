# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Dict, List, Type, Optional, cast
from typing_extensions import Literal

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._wrappers import ResultWrapper
from ..._base_client import (
    make_request_options,
)
from ...types.api_gateways import (
    SchemaGetResponse,
    SchemaUpdateResponse,
    SchemaUpdateMultipleResponse,
    SchemaAPIShieldEndpointManagementGetOperationsAndFeaturesAsOpenAPISchemasResponse,
    schema_update_params,
    schema_update_multiple_params,
    schema_api_shield_endpoint_management_get_operations_and_features_as_open_api_schemas_params,
)
from ...types.api_gateways.settings import APIShieldZoneSchemaValidationSettings

__all__ = ["Schemas", "AsyncSchemas"]


class Schemas(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SchemasWithRawResponse:
        return SchemasWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SchemasWithStreamingResponse:
        return SchemasWithStreamingResponse(self)

    def update(
        self,
        operation_id: str,
        *,
        zone_id: str,
        mitigation_action: Optional[Literal["log", "block", "none"]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SchemaUpdateResponse:
        """
        Updates operation-level schema validation settings on the zone

        Args:
          zone_id: Identifier

          mitigation_action: When set, this applies a mitigation action to this operation

              - `log` log request when request does not conform to schema for this operation
              - `block` deny access to the site when request does not conform to schema for
                this operation
              - `none` will skip mitigation for this operation
              - `null` indicates that no operation level mitigation is in place, see Zone
                Level Schema Validation Settings for mitigation action that will be applied

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not operation_id:
            raise ValueError(f"Expected a non-empty value for `operation_id` but received {operation_id!r}")
        return self._put(
            f"/zones/{zone_id}/api_gateway/operations/{operation_id}/schema_validation",
            body=maybe_transform({"mitigation_action": mitigation_action}, schema_update_params.SchemaUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SchemaUpdateResponse,
        )

    def api_shield_endpoint_management_get_operations_and_features_as_open_api_schemas(
        self,
        zone_id: str,
        *,
        feature: List[Literal["thresholds", "parameter_schemas", "schema_info"]] | NotGiven = NOT_GIVEN,
        host: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SchemaAPIShieldEndpointManagementGetOperationsAndFeaturesAsOpenAPISchemasResponse:
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
                    schema_api_shield_endpoint_management_get_operations_and_features_as_open_api_schemas_params.SchemaAPIShieldEndpointManagementGetOperationsAndFeaturesAsOpenAPISchemasParams,
                ),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[SchemaAPIShieldEndpointManagementGetOperationsAndFeaturesAsOpenAPISchemasResponse],
                ResultWrapper[SchemaAPIShieldEndpointManagementGetOperationsAndFeaturesAsOpenAPISchemasResponse],
            ),
        )

    def get(
        self,
        operation_id: str,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SchemaGetResponse:
        """
        Retrieves operation-level schema validation settings on the zone

        Args:
          zone_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not operation_id:
            raise ValueError(f"Expected a non-empty value for `operation_id` but received {operation_id!r}")
        return self._get(
            f"/zones/{zone_id}/api_gateway/operations/{operation_id}/schema_validation",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SchemaGetResponse,
        )

    def get_incremental(
        self,
        zone_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> APIShieldZoneSchemaValidationSettings:
        """
        Retrieves zone level schema validation settings currently set on the zone

        Args:
          zone_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._get(
            f"/zones/{zone_id}/api_gateway/settings/schema_validation",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIShieldZoneSchemaValidationSettings,
        )

    def update_multiple(
        self,
        zone_id: str,
        *,
        body: Dict[str, schema_update_multiple_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SchemaUpdateMultipleResponse:
        """
        Updates multiple operation-level schema validation settings on the zone

        Args:
          zone_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._patch(
            f"/zones/{zone_id}/api_gateway/operations/schema_validation",
            body=maybe_transform(body, schema_update_multiple_params.SchemaUpdateMultipleParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[SchemaUpdateMultipleResponse], ResultWrapper[SchemaUpdateMultipleResponse]),
        )


class AsyncSchemas(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSchemasWithRawResponse:
        return AsyncSchemasWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSchemasWithStreamingResponse:
        return AsyncSchemasWithStreamingResponse(self)

    async def update(
        self,
        operation_id: str,
        *,
        zone_id: str,
        mitigation_action: Optional[Literal["log", "block", "none"]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SchemaUpdateResponse:
        """
        Updates operation-level schema validation settings on the zone

        Args:
          zone_id: Identifier

          mitigation_action: When set, this applies a mitigation action to this operation

              - `log` log request when request does not conform to schema for this operation
              - `block` deny access to the site when request does not conform to schema for
                this operation
              - `none` will skip mitigation for this operation
              - `null` indicates that no operation level mitigation is in place, see Zone
                Level Schema Validation Settings for mitigation action that will be applied

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not operation_id:
            raise ValueError(f"Expected a non-empty value for `operation_id` but received {operation_id!r}")
        return await self._put(
            f"/zones/{zone_id}/api_gateway/operations/{operation_id}/schema_validation",
            body=maybe_transform({"mitigation_action": mitigation_action}, schema_update_params.SchemaUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SchemaUpdateResponse,
        )

    async def api_shield_endpoint_management_get_operations_and_features_as_open_api_schemas(
        self,
        zone_id: str,
        *,
        feature: List[Literal["thresholds", "parameter_schemas", "schema_info"]] | NotGiven = NOT_GIVEN,
        host: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SchemaAPIShieldEndpointManagementGetOperationsAndFeaturesAsOpenAPISchemasResponse:
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
                query=maybe_transform(
                    {
                        "feature": feature,
                        "host": host,
                    },
                    schema_api_shield_endpoint_management_get_operations_and_features_as_open_api_schemas_params.SchemaAPIShieldEndpointManagementGetOperationsAndFeaturesAsOpenAPISchemasParams,
                ),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[SchemaAPIShieldEndpointManagementGetOperationsAndFeaturesAsOpenAPISchemasResponse],
                ResultWrapper[SchemaAPIShieldEndpointManagementGetOperationsAndFeaturesAsOpenAPISchemasResponse],
            ),
        )

    async def get(
        self,
        operation_id: str,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SchemaGetResponse:
        """
        Retrieves operation-level schema validation settings on the zone

        Args:
          zone_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not operation_id:
            raise ValueError(f"Expected a non-empty value for `operation_id` but received {operation_id!r}")
        return await self._get(
            f"/zones/{zone_id}/api_gateway/operations/{operation_id}/schema_validation",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SchemaGetResponse,
        )

    async def get_incremental(
        self,
        zone_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> APIShieldZoneSchemaValidationSettings:
        """
        Retrieves zone level schema validation settings currently set on the zone

        Args:
          zone_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._get(
            f"/zones/{zone_id}/api_gateway/settings/schema_validation",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIShieldZoneSchemaValidationSettings,
        )

    async def update_multiple(
        self,
        zone_id: str,
        *,
        body: Dict[str, schema_update_multiple_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SchemaUpdateMultipleResponse:
        """
        Updates multiple operation-level schema validation settings on the zone

        Args:
          zone_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._patch(
            f"/zones/{zone_id}/api_gateway/operations/schema_validation",
            body=maybe_transform(body, schema_update_multiple_params.SchemaUpdateMultipleParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[SchemaUpdateMultipleResponse], ResultWrapper[SchemaUpdateMultipleResponse]),
        )


class SchemasWithRawResponse:
    def __init__(self, schemas: Schemas) -> None:
        self._schemas = schemas

        self.update = to_raw_response_wrapper(
            schemas.update,
        )
        self.api_shield_endpoint_management_get_operations_and_features_as_open_api_schemas = to_raw_response_wrapper(
            schemas.api_shield_endpoint_management_get_operations_and_features_as_open_api_schemas,
        )
        self.get = to_raw_response_wrapper(
            schemas.get,
        )
        self.get_incremental = to_raw_response_wrapper(
            schemas.get_incremental,
        )
        self.update_multiple = to_raw_response_wrapper(
            schemas.update_multiple,
        )


class AsyncSchemasWithRawResponse:
    def __init__(self, schemas: AsyncSchemas) -> None:
        self._schemas = schemas

        self.update = async_to_raw_response_wrapper(
            schemas.update,
        )
        self.api_shield_endpoint_management_get_operations_and_features_as_open_api_schemas = (
            async_to_raw_response_wrapper(
                schemas.api_shield_endpoint_management_get_operations_and_features_as_open_api_schemas,
            )
        )
        self.get = async_to_raw_response_wrapper(
            schemas.get,
        )
        self.get_incremental = async_to_raw_response_wrapper(
            schemas.get_incremental,
        )
        self.update_multiple = async_to_raw_response_wrapper(
            schemas.update_multiple,
        )


class SchemasWithStreamingResponse:
    def __init__(self, schemas: Schemas) -> None:
        self._schemas = schemas

        self.update = to_streamed_response_wrapper(
            schemas.update,
        )
        self.api_shield_endpoint_management_get_operations_and_features_as_open_api_schemas = (
            to_streamed_response_wrapper(
                schemas.api_shield_endpoint_management_get_operations_and_features_as_open_api_schemas,
            )
        )
        self.get = to_streamed_response_wrapper(
            schemas.get,
        )
        self.get_incremental = to_streamed_response_wrapper(
            schemas.get_incremental,
        )
        self.update_multiple = to_streamed_response_wrapper(
            schemas.update_multiple,
        )


class AsyncSchemasWithStreamingResponse:
    def __init__(self, schemas: AsyncSchemas) -> None:
        self._schemas = schemas

        self.update = async_to_streamed_response_wrapper(
            schemas.update,
        )
        self.api_shield_endpoint_management_get_operations_and_features_as_open_api_schemas = (
            async_to_streamed_response_wrapper(
                schemas.api_shield_endpoint_management_get_operations_and_features_as_open_api_schemas,
            )
        )
        self.get = async_to_streamed_response_wrapper(
            schemas.get,
        )
        self.get_incremental = async_to_streamed_response_wrapper(
            schemas.get_incremental,
        )
        self.update_multiple = async_to_streamed_response_wrapper(
            schemas.update_multiple,
        )
