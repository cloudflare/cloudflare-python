# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._compat import cached_property

from ....types.api_gateway.settings.settings import Settings

from ...._utils import maybe_transform, async_maybe_transform

from ...._base_client import make_request_options

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
from ....types import shared_params
from ....types.api_gateway.settings import schema_validation_update_params
from ....types.api_gateway.settings import schema_validation_edit_params

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
        *,
        zone_id: str,
        validation_default_mitigation_action: Literal["none", "log", "block"],
        validation_override_mitigation_action: Optional[Literal["none", "disable_override"]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Settings:
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
            cast_to=Settings,
        )

    def edit(
        self,
        *,
        zone_id: str,
        validation_default_mitigation_action: Optional[Literal["none", "log", "block"]] | NotGiven = NOT_GIVEN,
        validation_override_mitigation_action: Optional[Literal["none", "disable_override"]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Settings:
        """
        Updates zone level schema validation settings on the zone

        Args:
          zone_id: Identifier

          validation_default_mitigation_action: The default mitigation action used when there is no mitigation action defined on
              the operation Mitigation actions are as follows:

              - `log` - log request when request does not conform to schema
              - `block` - deny access to the site when request does not conform to schema

              A special value of of `none` will skip running schema validation entirely for
              the request when there is no mitigation action defined on the operation

              `null` will have no effect.

          validation_override_mitigation_action: When set, this overrides both zone level and operation level mitigation actions.

              - `none` will skip running schema validation entirely for the request

              To clear any override, use the special value `disable_override`

              `null` will have no effect.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._patch(
            f"/zones/{zone_id}/api_gateway/settings/schema_validation",
            body=maybe_transform(
                {
                    "validation_default_mitigation_action": validation_default_mitigation_action,
                    "validation_override_mitigation_action": validation_override_mitigation_action,
                },
                schema_validation_edit_params.SchemaValidationEditParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Settings,
        )

    def get(
        self,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Settings:
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
            cast_to=Settings,
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
        *,
        zone_id: str,
        validation_default_mitigation_action: Literal["none", "log", "block"],
        validation_override_mitigation_action: Optional[Literal["none", "disable_override"]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Settings:
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
            body=await async_maybe_transform(
                {
                    "validation_default_mitigation_action": validation_default_mitigation_action,
                    "validation_override_mitigation_action": validation_override_mitigation_action,
                },
                schema_validation_update_params.SchemaValidationUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Settings,
        )

    async def edit(
        self,
        *,
        zone_id: str,
        validation_default_mitigation_action: Optional[Literal["none", "log", "block"]] | NotGiven = NOT_GIVEN,
        validation_override_mitigation_action: Optional[Literal["none", "disable_override"]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Settings:
        """
        Updates zone level schema validation settings on the zone

        Args:
          zone_id: Identifier

          validation_default_mitigation_action: The default mitigation action used when there is no mitigation action defined on
              the operation Mitigation actions are as follows:

              - `log` - log request when request does not conform to schema
              - `block` - deny access to the site when request does not conform to schema

              A special value of of `none` will skip running schema validation entirely for
              the request when there is no mitigation action defined on the operation

              `null` will have no effect.

          validation_override_mitigation_action: When set, this overrides both zone level and operation level mitigation actions.

              - `none` will skip running schema validation entirely for the request

              To clear any override, use the special value `disable_override`

              `null` will have no effect.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._patch(
            f"/zones/{zone_id}/api_gateway/settings/schema_validation",
            body=await async_maybe_transform(
                {
                    "validation_default_mitigation_action": validation_default_mitigation_action,
                    "validation_override_mitigation_action": validation_override_mitigation_action,
                },
                schema_validation_edit_params.SchemaValidationEditParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Settings,
        )

    async def get(
        self,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Settings:
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
            cast_to=Settings,
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
