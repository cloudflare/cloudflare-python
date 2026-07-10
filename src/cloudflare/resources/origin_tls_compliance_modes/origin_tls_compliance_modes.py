# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Optional, cast

import httpx

from ..._types import Body, Query, Headers, NotGiven, SequenceNotStr, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
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
from ...types.origin_tls_compliance_modes import (
    origin_tls_compliance_mode_edit_params,
    origin_tls_compliance_mode_update_params,
)
from ...types.origin_tls_compliance_modes.origin_tls_compliance_mode_get_response import (
    OriginTLSComplianceModeGetResponse,
)
from ...types.origin_tls_compliance_modes.origin_tls_compliance_mode_edit_response import (
    OriginTLSComplianceModeEditResponse,
)
from ...types.origin_tls_compliance_modes.origin_tls_compliance_mode_delete_response import (
    OriginTLSComplianceModeDeleteResponse,
)
from ...types.origin_tls_compliance_modes.origin_tls_compliance_mode_update_response import (
    OriginTLSComplianceModeUpdateResponse,
)

__all__ = ["OriginTLSComplianceModesResource", "AsyncOriginTLSComplianceModesResource"]


class OriginTLSComplianceModesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> OriginTLSComplianceModesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return OriginTLSComplianceModesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OriginTLSComplianceModesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return OriginTLSComplianceModesResourceWithStreamingResponse(self)

    def update(
        self,
        *,
        zone_id: str,
        value: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[OriginTLSComplianceModeUpdateResponse]:
        """
        Replace the entire set of TLS compliance modes for the zone with the list
        provided in the request body. PUT performs a full replace, not a merge — any
        modes not present in the request body are removed. The request body must be of
        the form `{"value": ["fips", "pqh"]}`. Currently supported modes are `fips` and
        `pqh`; an empty list clears the constraint. Future modes (e.g. `cnsa2`) may be
        added; clients should treat unknown values as opaque strings. Invalid mode
        values are rejected with a 4xx response.

        Args:
          zone_id: Identifier.

          value: List of TLS compliance modes that constrain the key-exchange algorithms
              Cloudflare may use when establishing the TLS connection to the zone's origin.
              Currently supported values are `fips` (FIPS-approved curves) and `pqh`
              (post-quantum hybrid). Future modes (e.g. `cnsa2`) may be added; clients should
              treat unknown values as opaque strings. Multiple modes are combined as the
              intersection of their permitted algorithm lists; selections whose intersection
              is empty are rejected. An empty list clears the constraint.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._put(
            path_template("/zones/{zone_id}/settings/origin_tls_compliance_modes", zone_id=zone_id),
            body=maybe_transform(
                {"value": value}, origin_tls_compliance_mode_update_params.OriginTLSComplianceModeUpdateParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[OriginTLSComplianceModeUpdateResponse]]._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[OriginTLSComplianceModeUpdateResponse]],
                ResultWrapper[OriginTLSComplianceModeUpdateResponse],
            ),
        )

    def delete(
        self,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[OriginTLSComplianceModeDeleteResponse]:
        """
        Delete the Origin TLS Compliance Modes setting for the zone, removing any
        configured compliance constraint. After deletion, Cloudflare's default behavior
        applies (no compliance filtering of the key-exchange algorithm list sent to the
        origin).

        Args:
          zone_id: Identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._delete(
            path_template("/zones/{zone_id}/settings/origin_tls_compliance_modes", zone_id=zone_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[OriginTLSComplianceModeDeleteResponse]]._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[OriginTLSComplianceModeDeleteResponse]],
                ResultWrapper[OriginTLSComplianceModeDeleteResponse],
            ),
        )

    def edit(
        self,
        *,
        zone_id: str,
        value: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[OriginTLSComplianceModeEditResponse]:
        """Update the set of TLS compliance modes for the zone.

        PATCH performs a full
        replace of the modes list, not a merge — the request body is treated as the
        complete new list, and any modes not present in it are removed. (To remove a
        single mode from an existing configuration, send the updated list without it.)
        The request body must be of the form `{"value": ["fips", "pqh"]}`. Currently
        supported modes are `fips` and `pqh`; an empty list clears the constraint.
        Future modes (e.g. `cnsa2`) may be added; clients should treat unknown values as
        opaque strings. Invalid mode values are rejected with a 4xx response.

        Args:
          zone_id: Identifier.

          value: List of TLS compliance modes that constrain the key-exchange algorithms
              Cloudflare may use when establishing the TLS connection to the zone's origin.
              Currently supported values are `fips` (FIPS-approved curves) and `pqh`
              (post-quantum hybrid). Future modes (e.g. `cnsa2`) may be added; clients should
              treat unknown values as opaque strings. Multiple modes are combined as the
              intersection of their permitted algorithm lists; selections whose intersection
              is empty are rejected. An empty list clears the constraint.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._patch(
            path_template("/zones/{zone_id}/settings/origin_tls_compliance_modes", zone_id=zone_id),
            body=maybe_transform(
                {"value": value}, origin_tls_compliance_mode_edit_params.OriginTLSComplianceModeEditParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[OriginTLSComplianceModeEditResponse]]._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[OriginTLSComplianceModeEditResponse]], ResultWrapper[OriginTLSComplianceModeEditResponse]
            ),
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[OriginTLSComplianceModeGetResponse]:
        """
        Origin TLS Compliance Modes constrains the set of TLS key-exchange algorithms
        Cloudflare may use when establishing the TLS connection to the zone's origin.
        The value is a list of named compliance modes (currently `fips` and `pqh`).
        Multiple modes are combined as the intersection of their permitted algorithm
        lists. An empty list (or no rule configured) means no compliance constraint is
        applied.

        Args:
          zone_id: Identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._get(
            path_template("/zones/{zone_id}/settings/origin_tls_compliance_modes", zone_id=zone_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[OriginTLSComplianceModeGetResponse]]._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[OriginTLSComplianceModeGetResponse]], ResultWrapper[OriginTLSComplianceModeGetResponse]
            ),
        )


class AsyncOriginTLSComplianceModesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncOriginTLSComplianceModesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncOriginTLSComplianceModesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOriginTLSComplianceModesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncOriginTLSComplianceModesResourceWithStreamingResponse(self)

    async def update(
        self,
        *,
        zone_id: str,
        value: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[OriginTLSComplianceModeUpdateResponse]:
        """
        Replace the entire set of TLS compliance modes for the zone with the list
        provided in the request body. PUT performs a full replace, not a merge — any
        modes not present in the request body are removed. The request body must be of
        the form `{"value": ["fips", "pqh"]}`. Currently supported modes are `fips` and
        `pqh`; an empty list clears the constraint. Future modes (e.g. `cnsa2`) may be
        added; clients should treat unknown values as opaque strings. Invalid mode
        values are rejected with a 4xx response.

        Args:
          zone_id: Identifier.

          value: List of TLS compliance modes that constrain the key-exchange algorithms
              Cloudflare may use when establishing the TLS connection to the zone's origin.
              Currently supported values are `fips` (FIPS-approved curves) and `pqh`
              (post-quantum hybrid). Future modes (e.g. `cnsa2`) may be added; clients should
              treat unknown values as opaque strings. Multiple modes are combined as the
              intersection of their permitted algorithm lists; selections whose intersection
              is empty are rejected. An empty list clears the constraint.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._put(
            path_template("/zones/{zone_id}/settings/origin_tls_compliance_modes", zone_id=zone_id),
            body=await async_maybe_transform(
                {"value": value}, origin_tls_compliance_mode_update_params.OriginTLSComplianceModeUpdateParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[OriginTLSComplianceModeUpdateResponse]]._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[OriginTLSComplianceModeUpdateResponse]],
                ResultWrapper[OriginTLSComplianceModeUpdateResponse],
            ),
        )

    async def delete(
        self,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[OriginTLSComplianceModeDeleteResponse]:
        """
        Delete the Origin TLS Compliance Modes setting for the zone, removing any
        configured compliance constraint. After deletion, Cloudflare's default behavior
        applies (no compliance filtering of the key-exchange algorithm list sent to the
        origin).

        Args:
          zone_id: Identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._delete(
            path_template("/zones/{zone_id}/settings/origin_tls_compliance_modes", zone_id=zone_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[OriginTLSComplianceModeDeleteResponse]]._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[OriginTLSComplianceModeDeleteResponse]],
                ResultWrapper[OriginTLSComplianceModeDeleteResponse],
            ),
        )

    async def edit(
        self,
        *,
        zone_id: str,
        value: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[OriginTLSComplianceModeEditResponse]:
        """Update the set of TLS compliance modes for the zone.

        PATCH performs a full
        replace of the modes list, not a merge — the request body is treated as the
        complete new list, and any modes not present in it are removed. (To remove a
        single mode from an existing configuration, send the updated list without it.)
        The request body must be of the form `{"value": ["fips", "pqh"]}`. Currently
        supported modes are `fips` and `pqh`; an empty list clears the constraint.
        Future modes (e.g. `cnsa2`) may be added; clients should treat unknown values as
        opaque strings. Invalid mode values are rejected with a 4xx response.

        Args:
          zone_id: Identifier.

          value: List of TLS compliance modes that constrain the key-exchange algorithms
              Cloudflare may use when establishing the TLS connection to the zone's origin.
              Currently supported values are `fips` (FIPS-approved curves) and `pqh`
              (post-quantum hybrid). Future modes (e.g. `cnsa2`) may be added; clients should
              treat unknown values as opaque strings. Multiple modes are combined as the
              intersection of their permitted algorithm lists; selections whose intersection
              is empty are rejected. An empty list clears the constraint.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._patch(
            path_template("/zones/{zone_id}/settings/origin_tls_compliance_modes", zone_id=zone_id),
            body=await async_maybe_transform(
                {"value": value}, origin_tls_compliance_mode_edit_params.OriginTLSComplianceModeEditParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[OriginTLSComplianceModeEditResponse]]._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[OriginTLSComplianceModeEditResponse]], ResultWrapper[OriginTLSComplianceModeEditResponse]
            ),
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[OriginTLSComplianceModeGetResponse]:
        """
        Origin TLS Compliance Modes constrains the set of TLS key-exchange algorithms
        Cloudflare may use when establishing the TLS connection to the zone's origin.
        The value is a list of named compliance modes (currently `fips` and `pqh`).
        Multiple modes are combined as the intersection of their permitted algorithm
        lists. An empty list (or no rule configured) means no compliance constraint is
        applied.

        Args:
          zone_id: Identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._get(
            path_template("/zones/{zone_id}/settings/origin_tls_compliance_modes", zone_id=zone_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[OriginTLSComplianceModeGetResponse]]._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[OriginTLSComplianceModeGetResponse]], ResultWrapper[OriginTLSComplianceModeGetResponse]
            ),
        )


class OriginTLSComplianceModesResourceWithRawResponse:
    def __init__(self, origin_tls_compliance_modes: OriginTLSComplianceModesResource) -> None:
        self._origin_tls_compliance_modes = origin_tls_compliance_modes

        self.update = to_raw_response_wrapper(
            origin_tls_compliance_modes.update,
        )
        self.delete = to_raw_response_wrapper(
            origin_tls_compliance_modes.delete,
        )
        self.edit = to_raw_response_wrapper(
            origin_tls_compliance_modes.edit,
        )
        self.get = to_raw_response_wrapper(
            origin_tls_compliance_modes.get,
        )


class AsyncOriginTLSComplianceModesResourceWithRawResponse:
    def __init__(self, origin_tls_compliance_modes: AsyncOriginTLSComplianceModesResource) -> None:
        self._origin_tls_compliance_modes = origin_tls_compliance_modes

        self.update = async_to_raw_response_wrapper(
            origin_tls_compliance_modes.update,
        )
        self.delete = async_to_raw_response_wrapper(
            origin_tls_compliance_modes.delete,
        )
        self.edit = async_to_raw_response_wrapper(
            origin_tls_compliance_modes.edit,
        )
        self.get = async_to_raw_response_wrapper(
            origin_tls_compliance_modes.get,
        )


class OriginTLSComplianceModesResourceWithStreamingResponse:
    def __init__(self, origin_tls_compliance_modes: OriginTLSComplianceModesResource) -> None:
        self._origin_tls_compliance_modes = origin_tls_compliance_modes

        self.update = to_streamed_response_wrapper(
            origin_tls_compliance_modes.update,
        )
        self.delete = to_streamed_response_wrapper(
            origin_tls_compliance_modes.delete,
        )
        self.edit = to_streamed_response_wrapper(
            origin_tls_compliance_modes.edit,
        )
        self.get = to_streamed_response_wrapper(
            origin_tls_compliance_modes.get,
        )


class AsyncOriginTLSComplianceModesResourceWithStreamingResponse:
    def __init__(self, origin_tls_compliance_modes: AsyncOriginTLSComplianceModesResource) -> None:
        self._origin_tls_compliance_modes = origin_tls_compliance_modes

        self.update = async_to_streamed_response_wrapper(
            origin_tls_compliance_modes.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            origin_tls_compliance_modes.delete,
        )
        self.edit = async_to_streamed_response_wrapper(
            origin_tls_compliance_modes.edit,
        )
        self.get = async_to_streamed_response_wrapper(
            origin_tls_compliance_modes.get,
        )
