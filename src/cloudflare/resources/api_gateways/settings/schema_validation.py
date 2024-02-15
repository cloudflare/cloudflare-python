# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from ...._compat import cached_property

from ....types.api_gateways.settings import APIShieldZoneSchemaValidationSettings

from typing_extensions import Literal

from typing import Optional

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
from ....types.api_gateways.settings import schema_validation_update_params
from ...._wrappers import ResultWrapper

__all__ = ["SchemaValidation", "AsyncSchemaValidation"]


class SchemaValidation(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SchemaValidationWithRawResponse:
        return SchemaValidationWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SchemaValidationWithStreamingResponse:
        return SchemaValidationWithStreamingResponse(self)

    def update(
        self,
        zone_id: str,
        *,
        validation_default_mitigation_action: Literal["none", "log", "block"],
        validation_override_mitigation_action: Optional[Literal["none", "disable_override"]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> APIShieldZoneSchemaValidationSettings:
        """
        Updates zone level schema validation settings on the zone

        Args:
          zone_id: Identifier

          validation_default_mitigation_action: The default mitigation action used when there is no mitigation action defined on
              the operation

              Mitigation actions are as follows:

              - `log` - log request when request does not conform to schema
              - `block` - deny access to the site when request does not conform to schema

              A special value of of `none` will skip running schema validation entirely for
              the request when there is no mitigation action defined on the operation

          validation_override_mitigation_action: When set, this overrides both zone level and operation level mitigation actions.

              - `none` will skip running schema validation entirely for the request
              - `null` indicates that no override is in place

              To clear any override, use the special value `disable_override` or `null`

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._put(
            f"/zones/{zone_id}/api_gateway/settings/schema_validation",
            body=maybe_transform(
                {
                    "validation_default_mitigation_action": validation_default_mitigation_action,
                    "validation_override_mitigation_action": validation_override_mitigation_action,
                },
                schema_validation_update_params.SchemaValidationUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIShieldZoneSchemaValidationSettings,
        )


class AsyncSchemaValidation(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSchemaValidationWithRawResponse:
        return AsyncSchemaValidationWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSchemaValidationWithStreamingResponse:
        return AsyncSchemaValidationWithStreamingResponse(self)

    async def update(
        self,
        zone_id: str,
        *,
        validation_default_mitigation_action: Literal["none", "log", "block"],
        validation_override_mitigation_action: Optional[Literal["none", "disable_override"]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> APIShieldZoneSchemaValidationSettings:
        """
        Updates zone level schema validation settings on the zone

        Args:
          zone_id: Identifier

          validation_default_mitigation_action: The default mitigation action used when there is no mitigation action defined on
              the operation

              Mitigation actions are as follows:

              - `log` - log request when request does not conform to schema
              - `block` - deny access to the site when request does not conform to schema

              A special value of of `none` will skip running schema validation entirely for
              the request when there is no mitigation action defined on the operation

          validation_override_mitigation_action: When set, this overrides both zone level and operation level mitigation actions.

              - `none` will skip running schema validation entirely for the request
              - `null` indicates that no override is in place

              To clear any override, use the special value `disable_override` or `null`

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._put(
            f"/zones/{zone_id}/api_gateway/settings/schema_validation",
            body=maybe_transform(
                {
                    "validation_default_mitigation_action": validation_default_mitigation_action,
                    "validation_override_mitigation_action": validation_override_mitigation_action,
                },
                schema_validation_update_params.SchemaValidationUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIShieldZoneSchemaValidationSettings,
        )


class SchemaValidationWithRawResponse:
    def __init__(self, schema_validation: SchemaValidation) -> None:
        self._schema_validation = schema_validation

        self.update = to_raw_response_wrapper(
            schema_validation.update,
        )


class AsyncSchemaValidationWithRawResponse:
    def __init__(self, schema_validation: AsyncSchemaValidation) -> None:
        self._schema_validation = schema_validation

        self.update = async_to_raw_response_wrapper(
            schema_validation.update,
        )


class SchemaValidationWithStreamingResponse:
    def __init__(self, schema_validation: SchemaValidation) -> None:
        self._schema_validation = schema_validation

        self.update = to_streamed_response_wrapper(
            schema_validation.update,
        )


class AsyncSchemaValidationWithStreamingResponse:
    def __init__(self, schema_validation: AsyncSchemaValidation) -> None:
        self._schema_validation = schema_validation

        self.update = async_to_streamed_response_wrapper(
            schema_validation.update,
        )
