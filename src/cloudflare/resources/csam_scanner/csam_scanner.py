# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Optional, cast
from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
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
from ...types.csam_scanner import csam_scanner_edit_params
from ...types.csam_scanner.csam_scanner_get_response import CsamScannerGetResponse
from ...types.csam_scanner.csam_scanner_edit_response import CsamScannerEditResponse

__all__ = ["CsamScannerResource", "AsyncCsamScannerResource"]


class CsamScannerResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CsamScannerResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return CsamScannerResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CsamScannerResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return CsamScannerResourceWithStreamingResponse(self)

    def edit(
        self,
        *,
        zone_id: str,
        id: Literal["csam_scanner"] | Omit = omit,
        value: csam_scanner_edit_params.Value | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[CsamScannerEditResponse]:
        """Update the CSAM Scanner configuration for a zone.

        Allows enabling or disabling
        CSAM scanning, updating the notification email, and configuring scanning
        sources.

        When a new email is provided, email verification is triggered automatically. The
        `enabled` field is a toggle; the server may adjust it based on whether the
        notification email is verified.

        Returns 403 if the zone or account is locked by Trust & Safety.

        Args:
          zone_id: Identifier for the zone.

          id: The feature identifier.

          value: Writable CSAM Scanner feature configuration values.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._patch(
            path_template("/zones/{zone_id}/settings/csam_scanner_third_party", zone_id=zone_id),
            body=maybe_transform(
                {
                    "id": id,
                    "value": value,
                },
                csam_scanner_edit_params.CsamScannerEditParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[CsamScannerEditResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[CsamScannerEditResponse]], ResultWrapper[CsamScannerEditResponse]),
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
    ) -> Optional[CsamScannerGetResponse]:
        """
        Retrieve the current CSAM Scanner configuration for a zone.

        The notification email is masked by default in responses.

        Args:
          zone_id: Identifier for the zone.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._get(
            path_template("/zones/{zone_id}/settings/csam_scanner_third_party", zone_id=zone_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[CsamScannerGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[CsamScannerGetResponse]], ResultWrapper[CsamScannerGetResponse]),
        )


class AsyncCsamScannerResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCsamScannerResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCsamScannerResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCsamScannerResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncCsamScannerResourceWithStreamingResponse(self)

    async def edit(
        self,
        *,
        zone_id: str,
        id: Literal["csam_scanner"] | Omit = omit,
        value: csam_scanner_edit_params.Value | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[CsamScannerEditResponse]:
        """Update the CSAM Scanner configuration for a zone.

        Allows enabling or disabling
        CSAM scanning, updating the notification email, and configuring scanning
        sources.

        When a new email is provided, email verification is triggered automatically. The
        `enabled` field is a toggle; the server may adjust it based on whether the
        notification email is verified.

        Returns 403 if the zone or account is locked by Trust & Safety.

        Args:
          zone_id: Identifier for the zone.

          id: The feature identifier.

          value: Writable CSAM Scanner feature configuration values.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._patch(
            path_template("/zones/{zone_id}/settings/csam_scanner_third_party", zone_id=zone_id),
            body=await async_maybe_transform(
                {
                    "id": id,
                    "value": value,
                },
                csam_scanner_edit_params.CsamScannerEditParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[CsamScannerEditResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[CsamScannerEditResponse]], ResultWrapper[CsamScannerEditResponse]),
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
    ) -> Optional[CsamScannerGetResponse]:
        """
        Retrieve the current CSAM Scanner configuration for a zone.

        The notification email is masked by default in responses.

        Args:
          zone_id: Identifier for the zone.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._get(
            path_template("/zones/{zone_id}/settings/csam_scanner_third_party", zone_id=zone_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[CsamScannerGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[CsamScannerGetResponse]], ResultWrapper[CsamScannerGetResponse]),
        )


class CsamScannerResourceWithRawResponse:
    def __init__(self, csam_scanner: CsamScannerResource) -> None:
        self._csam_scanner = csam_scanner

        self.edit = to_raw_response_wrapper(
            csam_scanner.edit,
        )
        self.get = to_raw_response_wrapper(
            csam_scanner.get,
        )


class AsyncCsamScannerResourceWithRawResponse:
    def __init__(self, csam_scanner: AsyncCsamScannerResource) -> None:
        self._csam_scanner = csam_scanner

        self.edit = async_to_raw_response_wrapper(
            csam_scanner.edit,
        )
        self.get = async_to_raw_response_wrapper(
            csam_scanner.get,
        )


class CsamScannerResourceWithStreamingResponse:
    def __init__(self, csam_scanner: CsamScannerResource) -> None:
        self._csam_scanner = csam_scanner

        self.edit = to_streamed_response_wrapper(
            csam_scanner.edit,
        )
        self.get = to_streamed_response_wrapper(
            csam_scanner.get,
        )


class AsyncCsamScannerResourceWithStreamingResponse:
    def __init__(self, csam_scanner: AsyncCsamScannerResource) -> None:
        self._csam_scanner = csam_scanner

        self.edit = async_to_streamed_response_wrapper(
            csam_scanner.edit,
        )
        self.get = async_to_streamed_response_wrapper(
            csam_scanner.get,
        )
