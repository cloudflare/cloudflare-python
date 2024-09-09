# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Union, cast
from datetime import datetime
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
from ...pagination import SyncV4PagePaginationArray, AsyncV4PagePaginationArray
from ..._base_client import AsyncPaginator, make_request_options
from ...types.email_security import investigate_list_params
from ...types.email_security.investigate_get_response import InvestigateGetResponse
from ...types.email_security.investigate_raw_response import InvestigateRawResponse
from ...types.email_security.investigate_list_response import InvestigateListResponse
from ...types.email_security.investigate_trace_response import InvestigateTraceResponse
from ...types.email_security.investigate_preview_response import InvestigatePreviewResponse
from ...types.email_security.investigate_detections_response import InvestigateDetectionsResponse

__all__ = ["InvestigateResource", "AsyncInvestigateResource"]


class InvestigateResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> InvestigateResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
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
        final_disposition: Literal["MALICIOUS", "SUSPICIOUS", "SPOOF", "SPAM", "BULK"] | NotGiven = NOT_GIVEN,
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
        This endpoint returns information for each email that matches the search
        parameter(s).

        Args:
          account_id: Account Identifier

          action_log: Controls whether the message action log in included in the response.

          detections_only: If `false`, the search includes non-detections.

          domain: Filter by the sender domain

          end: The end of the search date range. Defaults to `now`.

          final_disposition: Filter messages by the provided disposition.

          message_action: Filter messages by actions applied to them

          page: Page number of paginated results.

          per_page: Number of results to display.

          query: Space delimited query term(s). The search is case-insensitive.

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

    def detections(
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
    ) -> InvestigateDetectionsResponse:
        """
        For emails that have a detection, this endpoint returns detection details such
        as threat categories, sender information, and links.

        Args:
          account_id: Account Identifier

          postfix_id: Message identifier

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
            f"/accounts/{account_id}/email-security/investigate/{postfix_id}/detections",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[InvestigateDetectionsResponse]._unwrapper,
            ),
            cast_to=cast(Type[InvestigateDetectionsResponse], ResultWrapper[InvestigateDetectionsResponse]),
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

          postfix_id: Message identifier

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

    def preview(
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
    ) -> InvestigatePreviewResponse:
        """
        For emails that have a detection, this endpoint returns a preview of the message
        body as a base64 encoded PNG image.

        Args:
          account_id: Account Identifier

          postfix_id: Message identifier

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
            f"/accounts/{account_id}/email-security/investigate/{postfix_id}/preview",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[InvestigatePreviewResponse]._unwrapper,
            ),
            cast_to=cast(Type[InvestigatePreviewResponse], ResultWrapper[InvestigatePreviewResponse]),
        )

    def raw(
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
    ) -> InvestigateRawResponse:
        """
        For emails that have a detection, this endpoint returns the raw email as an EML
        file.

        Args:
          account_id: Account Identifier

          postfix_id: Message identifier

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
            f"/accounts/{account_id}/email-security/investigate/{postfix_id}/raw",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[InvestigateRawResponse]._unwrapper,
            ),
            cast_to=cast(Type[InvestigateRawResponse], ResultWrapper[InvestigateRawResponse]),
        )

    def trace(
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
    ) -> InvestigateTraceResponse:
        """
        Get email trace

        Args:
          account_id: Account Identifier

          postfix_id: Message identifier

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
            f"/accounts/{account_id}/email-security/investigate/{postfix_id}/trace",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[InvestigateTraceResponse]._unwrapper,
            ),
            cast_to=cast(Type[InvestigateTraceResponse], ResultWrapper[InvestigateTraceResponse]),
        )


class AsyncInvestigateResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncInvestigateResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
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
        final_disposition: Literal["MALICIOUS", "SUSPICIOUS", "SPOOF", "SPAM", "BULK"] | NotGiven = NOT_GIVEN,
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
        This endpoint returns information for each email that matches the search
        parameter(s).

        Args:
          account_id: Account Identifier

          action_log: Controls whether the message action log in included in the response.

          detections_only: If `false`, the search includes non-detections.

          domain: Filter by the sender domain

          end: The end of the search date range. Defaults to `now`.

          final_disposition: Filter messages by the provided disposition.

          message_action: Filter messages by actions applied to them

          page: Page number of paginated results.

          per_page: Number of results to display.

          query: Space delimited query term(s). The search is case-insensitive.

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

    async def detections(
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
    ) -> InvestigateDetectionsResponse:
        """
        For emails that have a detection, this endpoint returns detection details such
        as threat categories, sender information, and links.

        Args:
          account_id: Account Identifier

          postfix_id: Message identifier

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
            f"/accounts/{account_id}/email-security/investigate/{postfix_id}/detections",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[InvestigateDetectionsResponse]._unwrapper,
            ),
            cast_to=cast(Type[InvestigateDetectionsResponse], ResultWrapper[InvestigateDetectionsResponse]),
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

          postfix_id: Message identifier

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

    async def preview(
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
    ) -> InvestigatePreviewResponse:
        """
        For emails that have a detection, this endpoint returns a preview of the message
        body as a base64 encoded PNG image.

        Args:
          account_id: Account Identifier

          postfix_id: Message identifier

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
            f"/accounts/{account_id}/email-security/investigate/{postfix_id}/preview",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[InvestigatePreviewResponse]._unwrapper,
            ),
            cast_to=cast(Type[InvestigatePreviewResponse], ResultWrapper[InvestigatePreviewResponse]),
        )

    async def raw(
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
    ) -> InvestigateRawResponse:
        """
        For emails that have a detection, this endpoint returns the raw email as an EML
        file.

        Args:
          account_id: Account Identifier

          postfix_id: Message identifier

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
            f"/accounts/{account_id}/email-security/investigate/{postfix_id}/raw",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[InvestigateRawResponse]._unwrapper,
            ),
            cast_to=cast(Type[InvestigateRawResponse], ResultWrapper[InvestigateRawResponse]),
        )

    async def trace(
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
    ) -> InvestigateTraceResponse:
        """
        Get email trace

        Args:
          account_id: Account Identifier

          postfix_id: Message identifier

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
            f"/accounts/{account_id}/email-security/investigate/{postfix_id}/trace",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[InvestigateTraceResponse]._unwrapper,
            ),
            cast_to=cast(Type[InvestigateTraceResponse], ResultWrapper[InvestigateTraceResponse]),
        )


class InvestigateResourceWithRawResponse:
    def __init__(self, investigate: InvestigateResource) -> None:
        self._investigate = investigate

        self.list = to_raw_response_wrapper(
            investigate.list,
        )
        self.detections = to_raw_response_wrapper(
            investigate.detections,
        )
        self.get = to_raw_response_wrapper(
            investigate.get,
        )
        self.preview = to_raw_response_wrapper(
            investigate.preview,
        )
        self.raw = to_raw_response_wrapper(
            investigate.raw,
        )
        self.trace = to_raw_response_wrapper(
            investigate.trace,
        )


class AsyncInvestigateResourceWithRawResponse:
    def __init__(self, investigate: AsyncInvestigateResource) -> None:
        self._investigate = investigate

        self.list = async_to_raw_response_wrapper(
            investigate.list,
        )
        self.detections = async_to_raw_response_wrapper(
            investigate.detections,
        )
        self.get = async_to_raw_response_wrapper(
            investigate.get,
        )
        self.preview = async_to_raw_response_wrapper(
            investigate.preview,
        )
        self.raw = async_to_raw_response_wrapper(
            investigate.raw,
        )
        self.trace = async_to_raw_response_wrapper(
            investigate.trace,
        )


class InvestigateResourceWithStreamingResponse:
    def __init__(self, investigate: InvestigateResource) -> None:
        self._investigate = investigate

        self.list = to_streamed_response_wrapper(
            investigate.list,
        )
        self.detections = to_streamed_response_wrapper(
            investigate.detections,
        )
        self.get = to_streamed_response_wrapper(
            investigate.get,
        )
        self.preview = to_streamed_response_wrapper(
            investigate.preview,
        )
        self.raw = to_streamed_response_wrapper(
            investigate.raw,
        )
        self.trace = to_streamed_response_wrapper(
            investigate.trace,
        )


class AsyncInvestigateResourceWithStreamingResponse:
    def __init__(self, investigate: AsyncInvestigateResource) -> None:
        self._investigate = investigate

        self.list = async_to_streamed_response_wrapper(
            investigate.list,
        )
        self.detections = async_to_streamed_response_wrapper(
            investigate.detections,
        )
        self.get = async_to_streamed_response_wrapper(
            investigate.get,
        )
        self.preview = async_to_streamed_response_wrapper(
            investigate.preview,
        )
        self.raw = async_to_streamed_response_wrapper(
            investigate.raw,
        )
        self.trace = async_to_streamed_response_wrapper(
            investigate.trace,
        )
