# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Union, Optional, cast
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
from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ...._utils import path_template, maybe_transform, async_maybe_transform
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
from ....types.email_security import investigate_get_params, investigate_list_params
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
        action_log: bool | Omit = omit,
        alert_id: str | Omit = omit,
        cursor: str | Omit = omit,
        detections_only: bool | Omit = omit,
        domain: str | Omit = omit,
        end: Union[str, datetime] | Omit = omit,
        final_disposition: Literal["MALICIOUS", "SUSPICIOUS", "SPOOF", "SPAM", "BULK", "NONE"] | Omit = omit,
        message_action: Literal["PREVIEW", "QUARANTINE_RELEASED", "MOVED"] | Omit = omit,
        message_id: str | Omit = omit,
        metric: str | Omit = omit,
        page: Optional[int] | Omit = omit,
        per_page: int | Omit = omit,
        query: str | Omit = omit,
        recipient: str | Omit = omit,
        sender: str | Omit = omit,
        start: Union[str, datetime] | Omit = omit,
        subject: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncV4PagePaginationArray[InvestigateListResponse]:
        """
        Returns information for each email that matches the search parameter(s).

        Args:
          account_id: Identifier.

          action_log: Whether to include the message action log in the response.

          detections_only: Whether to include only detections in search results.

          domain: Sender domains to filter by.

          end: The end of the search date range. Defaults to `now`.

          final_disposition: Dispositions to filter by.

          message_action: Message actions to filter by.

          page: Deprecated: Use cursor pagination instead. End of life: November 1, 2026.

          per_page: The number of results per page. Maximum value is 1000.

          query: Space-delimited search term. Case-insensitive.

          start: The beginning of the search date range. Defaults to `now - 30 days`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            path_template("/accounts/{account_id}/email-security/investigate", account_id=account_id),
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
                        "cursor": cursor,
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
                        "subject": subject,
                    },
                    investigate_list_params.InvestigateListParams,
                ),
            ),
            model=InvestigateListResponse,
        )

    def get(
        self,
        investigate_id: str,
        *,
        account_id: str,
        submission: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InvestigateGetResponse:
        """
        Retrieves comprehensive details for a specific email message including headers,
        recipients, sender information, and current quarantine status. Use the
        investigate_id from search results to fetch detailed information.

        Args:
          account_id: Identifier.

          investigate_id: Unique identifier for a message retrieved from investigation

          submission: When true, search the submissions datastore only. When false or omitted, search
              the regular datastore only.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not investigate_id:
            raise ValueError(f"Expected a non-empty value for `investigate_id` but received {investigate_id!r}")
        return self._get(
            path_template(
                "/accounts/{account_id}/email-security/investigate/{investigate_id}",
                account_id=account_id,
                investigate_id=investigate_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"submission": submission}, investigate_get_params.InvestigateGetParams),
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
        action_log: bool | Omit = omit,
        alert_id: str | Omit = omit,
        cursor: str | Omit = omit,
        detections_only: bool | Omit = omit,
        domain: str | Omit = omit,
        end: Union[str, datetime] | Omit = omit,
        final_disposition: Literal["MALICIOUS", "SUSPICIOUS", "SPOOF", "SPAM", "BULK", "NONE"] | Omit = omit,
        message_action: Literal["PREVIEW", "QUARANTINE_RELEASED", "MOVED"] | Omit = omit,
        message_id: str | Omit = omit,
        metric: str | Omit = omit,
        page: Optional[int] | Omit = omit,
        per_page: int | Omit = omit,
        query: str | Omit = omit,
        recipient: str | Omit = omit,
        sender: str | Omit = omit,
        start: Union[str, datetime] | Omit = omit,
        subject: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[InvestigateListResponse, AsyncV4PagePaginationArray[InvestigateListResponse]]:
        """
        Returns information for each email that matches the search parameter(s).

        Args:
          account_id: Identifier.

          action_log: Whether to include the message action log in the response.

          detections_only: Whether to include only detections in search results.

          domain: Sender domains to filter by.

          end: The end of the search date range. Defaults to `now`.

          final_disposition: Dispositions to filter by.

          message_action: Message actions to filter by.

          page: Deprecated: Use cursor pagination instead. End of life: November 1, 2026.

          per_page: The number of results per page. Maximum value is 1000.

          query: Space-delimited search term. Case-insensitive.

          start: The beginning of the search date range. Defaults to `now - 30 days`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            path_template("/accounts/{account_id}/email-security/investigate", account_id=account_id),
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
                        "cursor": cursor,
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
                        "subject": subject,
                    },
                    investigate_list_params.InvestigateListParams,
                ),
            ),
            model=InvestigateListResponse,
        )

    async def get(
        self,
        investigate_id: str,
        *,
        account_id: str,
        submission: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InvestigateGetResponse:
        """
        Retrieves comprehensive details for a specific email message including headers,
        recipients, sender information, and current quarantine status. Use the
        investigate_id from search results to fetch detailed information.

        Args:
          account_id: Identifier.

          investigate_id: Unique identifier for a message retrieved from investigation

          submission: When true, search the submissions datastore only. When false or omitted, search
              the regular datastore only.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not investigate_id:
            raise ValueError(f"Expected a non-empty value for `investigate_id` but received {investigate_id!r}")
        return await self._get(
            path_template(
                "/accounts/{account_id}/email-security/investigate/{investigate_id}",
                account_id=account_id,
                investigate_id=investigate_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"submission": submission}, investigate_get_params.InvestigateGetParams
                ),
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
