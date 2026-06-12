# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Optional, cast

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ...._utils import path_template, maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._wrappers import ResultWrapper
from ...._base_client import make_request_options
from ....types.zones.ct import alerting_edit_params
from ....types.zones.ct.alerting_get_response import AlertingGetResponse
from ....types.zones.ct.alerting_edit_response import AlertingEditResponse

__all__ = ["AlertingResource", "AsyncAlertingResource"]


class AlertingResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AlertingResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AlertingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AlertingResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AlertingResourceWithStreamingResponse(self)

    def edit(
        self,
        *,
        zone_id: str,
        enabled: bool,
        emails: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[AlertingEditResponse]:
        """
        Create or update the Certificate Transparency alerting subscription for a zone.
        Enables or disables email notifications when certificates are issued for the
        zone's domains. For Free and Pro zones, the subscription is toggled on or off
        using the enabled field. Notification emails are sent to all users with SSL
        permissions on the zone. For Business and Enterprise zones, the emails field is
        required and controls which addresses receive alerts. Setting emails to an empty
        list disables the subscription regardless of the enabled field. A maximum of 10
        email addresses may be configured.

        Args:
          zone_id: Identifier.

          enabled: Whether CT alerting is enabled for the zone.

          emails: Email addresses that receive CT alert notifications. Only present and
              configurable for Business and Enterprise zones. Maximum of 10 addresses. For
              Free and Pro zones, notifications are sent to all users with SSL permissions on
              the zone.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._patch(
            path_template("/zones/{zone_id}/ct/alerting", zone_id=zone_id),
            body=maybe_transform(
                {
                    "enabled": enabled,
                    "emails": emails,
                },
                alerting_edit_params.AlertingEditParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[AlertingEditResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[AlertingEditResponse]], ResultWrapper[AlertingEditResponse]),
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
    ) -> Optional[AlertingGetResponse]:
        """
        Retrieve the Certificate Transparency alerting subscription settings for a zone.
        Returns whether CT monitoring is enabled and, for Business and Enterprise zones,
        the list of email addresses that receive alerts.

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
            path_template("/zones/{zone_id}/ct/alerting", zone_id=zone_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[AlertingGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[AlertingGetResponse]], ResultWrapper[AlertingGetResponse]),
        )


class AsyncAlertingResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAlertingResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAlertingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAlertingResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncAlertingResourceWithStreamingResponse(self)

    async def edit(
        self,
        *,
        zone_id: str,
        enabled: bool,
        emails: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[AlertingEditResponse]:
        """
        Create or update the Certificate Transparency alerting subscription for a zone.
        Enables or disables email notifications when certificates are issued for the
        zone's domains. For Free and Pro zones, the subscription is toggled on or off
        using the enabled field. Notification emails are sent to all users with SSL
        permissions on the zone. For Business and Enterprise zones, the emails field is
        required and controls which addresses receive alerts. Setting emails to an empty
        list disables the subscription regardless of the enabled field. A maximum of 10
        email addresses may be configured.

        Args:
          zone_id: Identifier.

          enabled: Whether CT alerting is enabled for the zone.

          emails: Email addresses that receive CT alert notifications. Only present and
              configurable for Business and Enterprise zones. Maximum of 10 addresses. For
              Free and Pro zones, notifications are sent to all users with SSL permissions on
              the zone.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._patch(
            path_template("/zones/{zone_id}/ct/alerting", zone_id=zone_id),
            body=await async_maybe_transform(
                {
                    "enabled": enabled,
                    "emails": emails,
                },
                alerting_edit_params.AlertingEditParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[AlertingEditResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[AlertingEditResponse]], ResultWrapper[AlertingEditResponse]),
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
    ) -> Optional[AlertingGetResponse]:
        """
        Retrieve the Certificate Transparency alerting subscription settings for a zone.
        Returns whether CT monitoring is enabled and, for Business and Enterprise zones,
        the list of email addresses that receive alerts.

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
            path_template("/zones/{zone_id}/ct/alerting", zone_id=zone_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[AlertingGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[AlertingGetResponse]], ResultWrapper[AlertingGetResponse]),
        )


class AlertingResourceWithRawResponse:
    def __init__(self, alerting: AlertingResource) -> None:
        self._alerting = alerting

        self.edit = to_raw_response_wrapper(
            alerting.edit,
        )
        self.get = to_raw_response_wrapper(
            alerting.get,
        )


class AsyncAlertingResourceWithRawResponse:
    def __init__(self, alerting: AsyncAlertingResource) -> None:
        self._alerting = alerting

        self.edit = async_to_raw_response_wrapper(
            alerting.edit,
        )
        self.get = async_to_raw_response_wrapper(
            alerting.get,
        )


class AlertingResourceWithStreamingResponse:
    def __init__(self, alerting: AlertingResource) -> None:
        self._alerting = alerting

        self.edit = to_streamed_response_wrapper(
            alerting.edit,
        )
        self.get = to_streamed_response_wrapper(
            alerting.get,
        )


class AsyncAlertingResourceWithStreamingResponse:
    def __init__(self, alerting: AsyncAlertingResource) -> None:
        self._alerting = alerting

        self.edit = async_to_streamed_response_wrapper(
            alerting.edit,
        )
        self.get = async_to_streamed_response_wrapper(
            alerting.get,
        )
