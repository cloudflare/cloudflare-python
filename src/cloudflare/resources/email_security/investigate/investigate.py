# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Union, cast
from datetime import datetime
from typing_extensions import Literal

import httpx

from .raw import (
    RawResource,
    AsyncRawResource,
    RawResourceWithRawResponse,
    AsyncRawResourceWithRawResponse,
    RawResourceWithStreamingResponse,
    AsyncRawResourceWithStreamingResponse,
)
from .move import (
    MoveResource,
    AsyncMoveResource,
    MoveResourceWithRawResponse,
    AsyncMoveResourceWithRawResponse,
    MoveResourceWithStreamingResponse,
    AsyncMoveResourceWithStreamingResponse,
)
from .trace import (
    TraceResource,
    AsyncTraceResource,
    TraceResourceWithRawResponse,
    AsyncTraceResourceWithRawResponse,
    TraceResourceWithStreamingResponse,
    AsyncTraceResourceWithStreamingResponse,
)
from .preview import (
    PreviewResource,
    AsyncPreviewResource,
    PreviewResourceWithRawResponse,
    AsyncPreviewResourceWithRawResponse,
    PreviewResourceWithStreamingResponse,
    AsyncPreviewResourceWithStreamingResponse,
)
from .release import (
    ReleaseResource,
    AsyncReleaseResource,
    ReleaseResourceWithRawResponse,
    AsyncReleaseResourceWithRawResponse,
    ReleaseResourceWithStreamingResponse,
    AsyncReleaseResourceWithStreamingResponse,
)
from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import maybe_transform
from ...._compat import cached_property
from .detections import (
    DetectionsResource,
    AsyncDetectionsResource,
    DetectionsResourceWithRawResponse,
    AsyncDetectionsResourceWithRawResponse,
    DetectionsResourceWithStreamingResponse,
    AsyncDetectionsResourceWithStreamingResponse,
)
from .reclassify import (
    ReclassifyResource,
    AsyncReclassifyResource,
    ReclassifyResourceWithRawResponse,
    AsyncReclassifyResourceWithRawResponse,
    ReclassifyResourceWithStreamingResponse,
    AsyncReclassifyResourceWithStreamingResponse,
)
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._wrappers import ResultWrapper
from ....pagination import SyncV4PagePaginationArray, AsyncV4PagePaginationArray
from ...._base_client import AsyncPaginator, make_request_options
from ....types.email_security import investigate_list_params
from ....types.email_security.investigate_get_response import InvestigateGetResponse
from ....types.email_security.investigate_list_response import InvestigateListResponse

__all__ = ["InvestigateResource", "AsyncInvestigateResource"]


class InvestigateResource(SyncAPIResource):
    @cached_property
    def detections(self) -> DetectionsResource:
        return DetectionsResource(self._client)

    @cached_property
    def preview(self) -> PreviewResource:
        return PreviewResource(self._client)

    @cached_property
    def raw(self) -> RawResource:
        return RawResource(self._client)

    @cached_property
    def trace(self) -> TraceResource:
        return TraceResource(self._client)

    @cached_property
    def move(self) -> MoveResource:
        return MoveResource(self._client)

    @cached_property
    def reclassify(self) -> ReclassifyResource:
        return ReclassifyResource(self._client)

    @cached_property
    def release(self) -> ReleaseResource:
        return ReleaseResource(self._client)

    @cached_property
    def with_raw_response(self) -> InvestigateResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return InvestigateResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> InvestigateResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return InvestigateResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        account_id: str,
        action_log: bool | NotGiven = NOT_GIVEN,
        alert_id: str | NotGiven = NOT_GIVEN,
        detections_only: bool | NotGiven = NOT_GIVEN,
        domain: str | NotGiven = NOT_GIVEN,
        end: Union[str, datetime] | NotGiven = NOT_GIVEN,
        final_disposition: Literal["MALICIOUS", "SUSPICIOUS", "SPOOF", "SPAM", "BULK", "NONE"] | NotGiven = NOT_GIVEN,
        message_action: Literal["PREVIEW", "QUARANTINE_RELEASED", "MOVED"] | NotGiven = NOT_GIVEN,
        message_id: str | NotGiven = NOT_GIVEN,
        metric: str | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        query: str | NotGiven = NOT_GIVEN,
        recipient: str | NotGiven = NOT_GIVEN,
        sender: str | NotGiven = NOT_GIVEN,
        start: Union[str, datetime] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncV4PagePaginationArray[InvestigateListResponse]:
        """
        Returns information for each email that matches the search parameter(s).

        Args:
          account_id: Account Identifier

          action_log: Determines if the message action log is included in the response.

          detections_only: Determines if the search results will include detections or not.

          domain: The sender domains the search filters by.

          end: The end of the search date range. Defaults to `now`.

          final_disposition: The dispositions the search filters by.

          message_action: The message actions the search filters by.

          page: The page number of paginated results.

          per_page: The number of results per page.

          query: The space-delimited term used in the query. The search is case-insensitive.

              The content of the following email metadata fields are searched:

              - alert_id
              - CC
              - From (envelope_from)
              - From Name
              - final_disposition
              - md5 hash (of any attachment)
              - sha1 hash (of any attachment)
              - sha256 hash (of any attachment)
              - name (of any attachment)
              - Reason
              - Received DateTime (yyyy-mm-ddThh:mm:ss)
              - Sent DateTime (yyyy-mm-ddThh:mm:ss)
              - ReplyTo
              - To (envelope_to)
              - To Name
              - Message-ID
              - smtp_helo_server_ip
              - smtp_previous_hop_ip
              - x_originating_ip
              - Subject

          start: The beginning of the search date range. Defaults to `now - 30 days`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/email-security/investigate",
            page=SyncV4PagePaginationArray[InvestigateListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "action_log": action_log,
                        "alert_id": alert_id,
                        "detections_only": detections_only,
                        "domain": domain,
                        "end": end,
                        "final_disposition": final_disposition,
                        "message_action": message_action,
                        "message_id": message_id,
                        "metric": metric,
                        "page": page,
                        "per_page": per_page,
                        "query": query,
                        "recipient": recipient,
                        "sender": sender,
                        "start": start,
                    },
                    investigate_list_params.InvestigateListParams,
                ),
            ),
            model=InvestigateListResponse,
        )

    def get(
        self,
        postfix_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> InvestigateGetResponse:
        """
        Get message details

        Args:
          account_id: Account Identifier

          postfix_id: The identifier of the message.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not postfix_id:
            raise ValueError(f"Expected a non-empty value for `postfix_id` but received {postfix_id!r}")
        return self._get(
            f"/accounts/{account_id}/email-security/investigate/{postfix_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[InvestigateGetResponse]._unwrapper,
            ),
            cast_to=cast(Type[InvestigateGetResponse], ResultWrapper[InvestigateGetResponse]),
        )


class AsyncInvestigateResource(AsyncAPIResource):
    @cached_property
    def detections(self) -> AsyncDetectionsResource:
        return AsyncDetectionsResource(self._client)

    @cached_property
    def preview(self) -> AsyncPreviewResource:
        return AsyncPreviewResource(self._client)

    @cached_property
    def raw(self) -> AsyncRawResource:
        return AsyncRawResource(self._client)

    @cached_property
    def trace(self) -> AsyncTraceResource:
        return AsyncTraceResource(self._client)

    @cached_property
    def move(self) -> AsyncMoveResource:
        return AsyncMoveResource(self._client)

    @cached_property
    def reclassify(self) -> AsyncReclassifyResource:
        return AsyncReclassifyResource(self._client)

    @cached_property
    def release(self) -> AsyncReleaseResource:
        return AsyncReleaseResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncInvestigateResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncInvestigateResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncInvestigateResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncInvestigateResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        account_id: str,
        action_log: bool | NotGiven = NOT_GIVEN,
        alert_id: str | NotGiven = NOT_GIVEN,
        detections_only: bool | NotGiven = NOT_GIVEN,
        domain: str | NotGiven = NOT_GIVEN,
        end: Union[str, datetime] | NotGiven = NOT_GIVEN,
        final_disposition: Literal["MALICIOUS", "SUSPICIOUS", "SPOOF", "SPAM", "BULK", "NONE"] | NotGiven = NOT_GIVEN,
        message_action: Literal["PREVIEW", "QUARANTINE_RELEASED", "MOVED"] | NotGiven = NOT_GIVEN,
        message_id: str | NotGiven = NOT_GIVEN,
        metric: str | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        query: str | NotGiven = NOT_GIVEN,
        recipient: str | NotGiven = NOT_GIVEN,
        sender: str | NotGiven = NOT_GIVEN,
        start: Union[str, datetime] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[InvestigateListResponse, AsyncV4PagePaginationArray[InvestigateListResponse]]:
        """
        Returns information for each email that matches the search parameter(s).

        Args:
          account_id: Account Identifier

          action_log: Determines if the message action log is included in the response.

          detections_only: Determines if the search results will include detections or not.

          domain: The sender domains the search filters by.

          end: The end of the search date range. Defaults to `now`.

          final_disposition: The dispositions the search filters by.

          message_action: The message actions the search filters by.

          page: The page number of paginated results.

          per_page: The number of results per page.

          query: The space-delimited term used in the query. The search is case-insensitive.

              The content of the following email metadata fields are searched:

              - alert_id
              - CC
              - From (envelope_from)
              - From Name
              - final_disposition
              - md5 hash (of any attachment)
              - sha1 hash (of any attachment)
              - sha256 hash (of any attachment)
              - name (of any attachment)
              - Reason
              - Received DateTime (yyyy-mm-ddThh:mm:ss)
              - Sent DateTime (yyyy-mm-ddThh:mm:ss)
              - ReplyTo
              - To (envelope_to)
              - To Name
              - Message-ID
              - smtp_helo_server_ip
              - smtp_previous_hop_ip
              - x_originating_ip
              - Subject

          start: The beginning of the search date range. Defaults to `now - 30 days`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/email-security/investigate",
            page=AsyncV4PagePaginationArray[InvestigateListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "action_log": action_log,
                        "alert_id": alert_id,
                        "detections_only": detections_only,
                        "domain": domain,
                        "end": end,
                        "final_disposition": final_disposition,
                        "message_action": message_action,
                        "message_id": message_id,
                        "metric": metric,
                        "page": page,
                        "per_page": per_page,
                        "query": query,
                        "recipient": recipient,
                        "sender": sender,
                        "start": start,
                    },
                    investigate_list_params.InvestigateListParams,
                ),
            ),
            model=InvestigateListResponse,
        )

    async def get(
        self,
        postfix_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> InvestigateGetResponse:
        """
        Get message details

        Args:
          account_id: Account Identifier

          postfix_id: The identifier of the message.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not postfix_id:
            raise ValueError(f"Expected a non-empty value for `postfix_id` but received {postfix_id!r}")
        return await self._get(
            f"/accounts/{account_id}/email-security/investigate/{postfix_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[InvestigateGetResponse]._unwrapper,
            ),
            cast_to=cast(Type[InvestigateGetResponse], ResultWrapper[InvestigateGetResponse]),
        )


class InvestigateResourceWithRawResponse:
    def __init__(self, investigate: InvestigateResource) -> None:
        self._investigate = investigate

        self.list = to_raw_response_wrapper(
            investigate.list,
        )
        self.get = to_raw_response_wrapper(
            investigate.get,
        )

    @cached_property
    def detections(self) -> DetectionsResourceWithRawResponse:
        return DetectionsResourceWithRawResponse(self._investigate.detections)

    @cached_property
    def preview(self) -> PreviewResourceWithRawResponse:
        return PreviewResourceWithRawResponse(self._investigate.preview)

    @cached_property
    def raw(self) -> RawResourceWithRawResponse:
        return RawResourceWithRawResponse(self._investigate.raw)

    @cached_property
    def trace(self) -> TraceResourceWithRawResponse:
        return TraceResourceWithRawResponse(self._investigate.trace)

    @cached_property
    def move(self) -> MoveResourceWithRawResponse:
        return MoveResourceWithRawResponse(self._investigate.move)

    @cached_property
    def reclassify(self) -> ReclassifyResourceWithRawResponse:
        return ReclassifyResourceWithRawResponse(self._investigate.reclassify)

    @cached_property
    def release(self) -> ReleaseResourceWithRawResponse:
        return ReleaseResourceWithRawResponse(self._investigate.release)


class AsyncInvestigateResourceWithRawResponse:
    def __init__(self, investigate: AsyncInvestigateResource) -> None:
        self._investigate = investigate

        self.list = async_to_raw_response_wrapper(
            investigate.list,
        )
        self.get = async_to_raw_response_wrapper(
            investigate.get,
        )

    @cached_property
    def detections(self) -> AsyncDetectionsResourceWithRawResponse:
        return AsyncDetectionsResourceWithRawResponse(self._investigate.detections)

    @cached_property
    def preview(self) -> AsyncPreviewResourceWithRawResponse:
        return AsyncPreviewResourceWithRawResponse(self._investigate.preview)

    @cached_property
    def raw(self) -> AsyncRawResourceWithRawResponse:
        return AsyncRawResourceWithRawResponse(self._investigate.raw)

    @cached_property
    def trace(self) -> AsyncTraceResourceWithRawResponse:
        return AsyncTraceResourceWithRawResponse(self._investigate.trace)

    @cached_property
    def move(self) -> AsyncMoveResourceWithRawResponse:
        return AsyncMoveResourceWithRawResponse(self._investigate.move)

    @cached_property
    def reclassify(self) -> AsyncReclassifyResourceWithRawResponse:
        return AsyncReclassifyResourceWithRawResponse(self._investigate.reclassify)

    @cached_property
    def release(self) -> AsyncReleaseResourceWithRawResponse:
        return AsyncReleaseResourceWithRawResponse(self._investigate.release)


class InvestigateResourceWithStreamingResponse:
    def __init__(self, investigate: InvestigateResource) -> None:
        self._investigate = investigate

        self.list = to_streamed_response_wrapper(
            investigate.list,
        )
        self.get = to_streamed_response_wrapper(
            investigate.get,
        )

    @cached_property
    def detections(self) -> DetectionsResourceWithStreamingResponse:
        return DetectionsResourceWithStreamingResponse(self._investigate.detections)

    @cached_property
    def preview(self) -> PreviewResourceWithStreamingResponse:
        return PreviewResourceWithStreamingResponse(self._investigate.preview)

    @cached_property
    def raw(self) -> RawResourceWithStreamingResponse:
        return RawResourceWithStreamingResponse(self._investigate.raw)

    @cached_property
    def trace(self) -> TraceResourceWithStreamingResponse:
        return TraceResourceWithStreamingResponse(self._investigate.trace)

    @cached_property
    def move(self) -> MoveResourceWithStreamingResponse:
        return MoveResourceWithStreamingResponse(self._investigate.move)

    @cached_property
    def reclassify(self) -> ReclassifyResourceWithStreamingResponse:
        return ReclassifyResourceWithStreamingResponse(self._investigate.reclassify)

    @cached_property
    def release(self) -> ReleaseResourceWithStreamingResponse:
        return ReleaseResourceWithStreamingResponse(self._investigate.release)


class AsyncInvestigateResourceWithStreamingResponse:
    def __init__(self, investigate: AsyncInvestigateResource) -> None:
        self._investigate = investigate

        self.list = async_to_streamed_response_wrapper(
            investigate.list,
        )
        self.get = async_to_streamed_response_wrapper(
            investigate.get,
        )

    @cached_property
    def detections(self) -> AsyncDetectionsResourceWithStreamingResponse:
        return AsyncDetectionsResourceWithStreamingResponse(self._investigate.detections)

    @cached_property
    def preview(self) -> AsyncPreviewResourceWithStreamingResponse:
        return AsyncPreviewResourceWithStreamingResponse(self._investigate.preview)

    @cached_property
    def raw(self) -> AsyncRawResourceWithStreamingResponse:
        return AsyncRawResourceWithStreamingResponse(self._investigate.raw)

    @cached_property
    def trace(self) -> AsyncTraceResourceWithStreamingResponse:
        return AsyncTraceResourceWithStreamingResponse(self._investigate.trace)

    @cached_property
    def move(self) -> AsyncMoveResourceWithStreamingResponse:
        return AsyncMoveResourceWithStreamingResponse(self._investigate.move)

    @cached_property
    def reclassify(self) -> AsyncReclassifyResourceWithStreamingResponse:
        return AsyncReclassifyResourceWithStreamingResponse(self._investigate.reclassify)

    @cached_property
    def release(self) -> AsyncReleaseResourceWithStreamingResponse:
        return AsyncReleaseResourceWithStreamingResponse(self._investigate.release)
