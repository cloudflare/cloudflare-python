# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._compat import cached_property

from ....types.api_gateway.operations.schema_validation_update_response import SchemaValidationUpdateResponse

from ...._utils import maybe_transform, async_maybe_transform

from ...._base_client import make_request_options

from typing import Optional, Type

from typing_extensions import Literal

from ....types.api_gateway.operations.settings_multiple_request import SettingsMultipleRequest

from ...._wrappers import ResultWrapper

from ....types.api_gateway.operations.settings_multiple_request_param import SettingsMultipleRequestParam

from ....types.api_gateway.operations.schema_validation_get_response import SchemaValidationGetResponse

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
from ....types import shared_params
from ....types.api_gateway.operations import schema_validation_update_params
from ....types.api_gateway.operations import schema_validation_edit_params
from ....types.api_gateway.operations import SettingsMultipleRequest
from typing import cast
from typing import cast

__all__ = ["SchemaValidationResource", "AsyncSchemaValidationResource"]


class SchemaValidationResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SchemaValidationResourceWithRawResponse:
        return SchemaValidationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SchemaValidationResourceWithStreamingResponse:
        return SchemaValidationResourceWithStreamingResponse(self)

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
    ) -> SchemaValidationUpdateResponse:
        """
        Updates operation-level schema validation settings on the zone

        Args:
          zone_id: Identifier

          operation_id: UUID

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
            body=maybe_transform(
                {"mitigation_action": mitigation_action}, schema_validation_update_params.SchemaValidationUpdateParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SchemaValidationUpdateResponse,
        )

    def edit(
        self,
        *,
        zone_id: str,
        settings_multiple_request: SettingsMultipleRequestParam,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SettingsMultipleRequest:
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
            body=maybe_transform(settings_multiple_request, schema_validation_edit_params.SchemaValidationEditParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[SettingsMultipleRequest]._unwrapper,
            ),
            cast_to=cast(Type[SettingsMultipleRequest], ResultWrapper[SettingsMultipleRequest]),
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
    ) -> SchemaValidationGetResponse:
        """
        Retrieves operation-level schema validation settings on the zone

        Args:
          zone_id: Identifier

          operation_id: UUID

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
            cast_to=SchemaValidationGetResponse,
        )


class AsyncSchemaValidationResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSchemaValidationResourceWithRawResponse:
        return AsyncSchemaValidationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSchemaValidationResourceWithStreamingResponse:
        return AsyncSchemaValidationResourceWithStreamingResponse(self)

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
    ) -> SchemaValidationUpdateResponse:
        """
        Updates operation-level schema validation settings on the zone

        Args:
          zone_id: Identifier

          operation_id: UUID

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
            body=await async_maybe_transform(
                {"mitigation_action": mitigation_action}, schema_validation_update_params.SchemaValidationUpdateParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SchemaValidationUpdateResponse,
        )

    async def edit(
        self,
        *,
        zone_id: str,
        settings_multiple_request: SettingsMultipleRequestParam,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SettingsMultipleRequest:
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
            body=await async_maybe_transform(
                settings_multiple_request, schema_validation_edit_params.SchemaValidationEditParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[SettingsMultipleRequest]._unwrapper,
            ),
            cast_to=cast(Type[SettingsMultipleRequest], ResultWrapper[SettingsMultipleRequest]),
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
    ) -> SchemaValidationGetResponse:
        """
        Retrieves operation-level schema validation settings on the zone

        Args:
          zone_id: Identifier

          operation_id: UUID

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
            cast_to=SchemaValidationGetResponse,
        )


class SchemaValidationResourceWithRawResponse:
    def __init__(self, schema_validation: SchemaValidationResource) -> None:
        self._schema_validation = schema_validation

        self.update = to_raw_response_wrapper(
            schema_validation.update,
        )
        self.edit = to_raw_response_wrapper(
            schema_validation.edit,
        )
        self.get = to_raw_response_wrapper(
            schema_validation.get,
        )


class AsyncSchemaValidationResourceWithRawResponse:
    def __init__(self, schema_validation: AsyncSchemaValidationResource) -> None:
        self._schema_validation = schema_validation

        self.update = async_to_raw_response_wrapper(
            schema_validation.update,
        )
        self.edit = async_to_raw_response_wrapper(
            schema_validation.edit,
        )
        self.get = async_to_raw_response_wrapper(
            schema_validation.get,
        )


class SchemaValidationResourceWithStreamingResponse:
    def __init__(self, schema_validation: SchemaValidationResource) -> None:
        self._schema_validation = schema_validation

        self.update = to_streamed_response_wrapper(
            schema_validation.update,
        )
        self.edit = to_streamed_response_wrapper(
            schema_validation.edit,
        )
        self.get = to_streamed_response_wrapper(
            schema_validation.get,
        )


class AsyncSchemaValidationResourceWithStreamingResponse:
    def __init__(self, schema_validation: AsyncSchemaValidationResource) -> None:
        self._schema_validation = schema_validation

        self.update = async_to_streamed_response_wrapper(
            schema_validation.update,
        )
        self.edit = async_to_streamed_response_wrapper(
            schema_validation.edit,
        )
        self.get = async_to_streamed_response_wrapper(
            schema_validation.get,
        )
