# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Optional, cast

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
from ...types.email_auth import dmarc_report_edit_params
from ...types.email_auth.dmarc_report_get_response import DMARCReportGetResponse
from ...types.email_auth.dmarc_report_edit_response import DMARCReportEditResponse

__all__ = ["DMARCReportsResource", "AsyncDMARCReportsResource"]


class DMARCReportsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DMARCReportsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return DMARCReportsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DMARCReportsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return DMARCReportsResourceWithStreamingResponse(self)

    def edit(
        self,
        *,
        zone_id: str,
        enabled: Optional[bool] | Omit = omit,
        skip_wizard: Optional[bool] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[DMARCReportEditResponse]:
        """Updates the DMARC report configuration for a zone.

        At least one of `enabled` or
        `skip_wizard` must be provided. When enabling, the handler will ensure the DMARC
        RUA record exists in DNS.

        Args:
          zone_id: Identifier.

          enabled: Enable or disable DMARC reports for this zone

          skip_wizard: Skip the DMARC setup wizard

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._patch(
            path_template("/zones/{zone_id}/email/auth/dmarc-reports", zone_id=zone_id),
            body=maybe_transform(
                {
                    "enabled": enabled,
                    "skip_wizard": skip_wizard,
                },
                dmarc_report_edit_params.DMARCReportEditParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[DMARCReportEditResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[DMARCReportEditResponse]], ResultWrapper[DMARCReportEditResponse]),
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
    ) -> Optional[DMARCReportGetResponse]:
        """Retrieves the current DMARC report configuration and status for a zone.

        Returns
        the RUA prefix, enabled status, approved sources, and DNS records.

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
            path_template("/zones/{zone_id}/email/auth/dmarc-reports", zone_id=zone_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[DMARCReportGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[DMARCReportGetResponse]], ResultWrapper[DMARCReportGetResponse]),
        )


class AsyncDMARCReportsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDMARCReportsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDMARCReportsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDMARCReportsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncDMARCReportsResourceWithStreamingResponse(self)

    async def edit(
        self,
        *,
        zone_id: str,
        enabled: Optional[bool] | Omit = omit,
        skip_wizard: Optional[bool] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[DMARCReportEditResponse]:
        """Updates the DMARC report configuration for a zone.

        At least one of `enabled` or
        `skip_wizard` must be provided. When enabling, the handler will ensure the DMARC
        RUA record exists in DNS.

        Args:
          zone_id: Identifier.

          enabled: Enable or disable DMARC reports for this zone

          skip_wizard: Skip the DMARC setup wizard

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._patch(
            path_template("/zones/{zone_id}/email/auth/dmarc-reports", zone_id=zone_id),
            body=await async_maybe_transform(
                {
                    "enabled": enabled,
                    "skip_wizard": skip_wizard,
                },
                dmarc_report_edit_params.DMARCReportEditParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[DMARCReportEditResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[DMARCReportEditResponse]], ResultWrapper[DMARCReportEditResponse]),
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
    ) -> Optional[DMARCReportGetResponse]:
        """Retrieves the current DMARC report configuration and status for a zone.

        Returns
        the RUA prefix, enabled status, approved sources, and DNS records.

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
            path_template("/zones/{zone_id}/email/auth/dmarc-reports", zone_id=zone_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[DMARCReportGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[DMARCReportGetResponse]], ResultWrapper[DMARCReportGetResponse]),
        )


class DMARCReportsResourceWithRawResponse:
    def __init__(self, dmarc_reports: DMARCReportsResource) -> None:
        self._dmarc_reports = dmarc_reports

        self.edit = to_raw_response_wrapper(
            dmarc_reports.edit,
        )
        self.get = to_raw_response_wrapper(
            dmarc_reports.get,
        )


class AsyncDMARCReportsResourceWithRawResponse:
    def __init__(self, dmarc_reports: AsyncDMARCReportsResource) -> None:
        self._dmarc_reports = dmarc_reports

        self.edit = async_to_raw_response_wrapper(
            dmarc_reports.edit,
        )
        self.get = async_to_raw_response_wrapper(
            dmarc_reports.get,
        )


class DMARCReportsResourceWithStreamingResponse:
    def __init__(self, dmarc_reports: DMARCReportsResource) -> None:
        self._dmarc_reports = dmarc_reports

        self.edit = to_streamed_response_wrapper(
            dmarc_reports.edit,
        )
        self.get = to_streamed_response_wrapper(
            dmarc_reports.get,
        )


class AsyncDMARCReportsResourceWithStreamingResponse:
    def __init__(self, dmarc_reports: AsyncDMARCReportsResource) -> None:
        self._dmarc_reports = dmarc_reports

        self.edit = async_to_streamed_response_wrapper(
            dmarc_reports.edit,
        )
        self.get = async_to_streamed_response_wrapper(
            dmarc_reports.get,
        )
