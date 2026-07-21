# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Type, Union, Iterable, Optional, cast
from datetime import datetime
from typing_extensions import Literal

import httpx

from ....._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ....._utils import path_template, maybe_transform, async_maybe_transform
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....._wrappers import ResultWrapper
from .....pagination import SyncV4PagePaginationArray, AsyncV4PagePaginationArray
from ....._base_client import AsyncPaginator, make_request_options
from .....types.zero_trust.casb.posture import content_list_params, content_export_params
from .....types.zero_trust.casb.posture.content_list_response import ContentListResponse
from .....types.zero_trust.casb.posture.content_export_response import ContentExportResponse

__all__ = ["ContentResource", "AsyncContentResource"]


class ContentResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ContentResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return ContentResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ContentResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return ContentResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        account_id: str,
        direction: Literal["asc", "desc"] | Omit = omit,
        dlp_profile_id: str | Omit = omit,
        integration_id: str | Omit = omit,
        max_affliction_date: Union[str, datetime] | Omit = omit,
        min_affliction_date: Union[str, datetime] | Omit = omit,
        order: Literal["asset_name", "dlp_profile_count", "integration_name", "latest_affliction_date"] | Omit = omit,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        search: str | Omit = omit,
        vendor: Literal[
            "ANTHROPIC",
            "AWS",
            "BITBUCKET",
            "BOX",
            "CONFLUENCE",
            "DROPBOX",
            "GITHUB",
            "GOOGLE_CLOUD_PLATFORM",
            "GOOGLE_WORKSPACE",
            "JIRA",
            "MICROSOFT",
            "MICROSOFT_INTERNAL",
            "OPENAI",
            "SALESFORCE",
            "SERVICENOW",
            "SLACK",
        ]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncV4PagePaginationArray[ContentListResponse]:
        """
        List DLP content findings

        Args:
          direction: Direction to order results.

          dlp_profile_id: Filter by an DLP profile ID

          integration_id: Filter by an integration ID

          max_affliction_date: Filter to view findings that occurred on or before the affliction date. Can be a
              date-time in ISO 8601 format or an epoch timestamp.

          min_affliction_date: Filter to view findings that occurred on or after the affliction date. Can be a
              date-time in ISO 8601 format or an epoch timestamp.

          order: Which field to use when ordering content assets.

          page: A page number within the paginated result set.

          per_page: Number of results to return per page.

          search: A search term.

          vendor: Filter by vendor

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            path_template("/accounts/{account_id}/data-security/posture/content", account_id=account_id),
            page=SyncV4PagePaginationArray[ContentListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "direction": direction,
                        "dlp_profile_id": dlp_profile_id,
                        "integration_id": integration_id,
                        "max_affliction_date": max_affliction_date,
                        "min_affliction_date": min_affliction_date,
                        "order": order,
                        "page": page,
                        "per_page": per_page,
                        "search": search,
                        "vendor": vendor,
                    },
                    content_list_params.ContentListParams,
                ),
            ),
            model=ContentListResponse,
        )

    def export(
        self,
        *,
        account_id: str,
        dlp_profile_information: Iterable[content_export_params.DLPProfileInformation],
        dlp_profile_id: SequenceNotStr[str] | Omit = omit,
        integration_id: SequenceNotStr[str] | Omit = omit,
        max_affliction_date: Union[str, datetime] | Omit = omit,
        min_affliction_date: Union[str, datetime] | Omit = omit,
        orders: Iterable[content_export_params.Order] | Omit = omit,
        search: str | Omit = omit,
        vendors: List[
            Literal[
                "ANTHROPIC",
                "AWS",
                "BITBUCKET",
                "BOX",
                "CONFLUENCE",
                "DROPBOX",
                "GITHUB",
                "GOOGLE_CLOUD_PLATFORM",
                "GOOGLE_WORKSPACE",
                "JIRA",
                "MICROSOFT",
                "MICROSOFT_INTERNAL",
                "OPENAI",
                "SALESFORCE",
                "SERVICENOW",
                "SLACK",
            ]
        ]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[ContentExportResponse]:
        """
        Creates a CSV export for content and accepts optional filters in the payload.

        Args:
          dlp_profile_information: DLP profile metadata for the export.

          dlp_profile_id: Filter by DLP profile IDs.

          integration_id: Filter by integration IDs.

          max_affliction_date: Filter to view content flagged on or before this date.

          min_affliction_date: Filter to view content flagged on or after this date.

          orders: Ordering specifications for the export.

          search: Search term to filter content.

          vendors: Filter by vendor types.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._post(
            path_template("/accounts/{account_id}/data-security/posture/content/export", account_id=account_id),
            body=maybe_transform(
                {
                    "dlp_profile_information": dlp_profile_information,
                    "dlp_profile_id": dlp_profile_id,
                    "integration_id": integration_id,
                    "max_affliction_date": max_affliction_date,
                    "min_affliction_date": min_affliction_date,
                    "orders": orders,
                    "search": search,
                    "vendors": vendors,
                },
                content_export_params.ContentExportParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[ContentExportResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[ContentExportResponse]], ResultWrapper[ContentExportResponse]),
        )


class AsyncContentResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncContentResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncContentResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncContentResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncContentResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        account_id: str,
        direction: Literal["asc", "desc"] | Omit = omit,
        dlp_profile_id: str | Omit = omit,
        integration_id: str | Omit = omit,
        max_affliction_date: Union[str, datetime] | Omit = omit,
        min_affliction_date: Union[str, datetime] | Omit = omit,
        order: Literal["asset_name", "dlp_profile_count", "integration_name", "latest_affliction_date"] | Omit = omit,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        search: str | Omit = omit,
        vendor: Literal[
            "ANTHROPIC",
            "AWS",
            "BITBUCKET",
            "BOX",
            "CONFLUENCE",
            "DROPBOX",
            "GITHUB",
            "GOOGLE_CLOUD_PLATFORM",
            "GOOGLE_WORKSPACE",
            "JIRA",
            "MICROSOFT",
            "MICROSOFT_INTERNAL",
            "OPENAI",
            "SALESFORCE",
            "SERVICENOW",
            "SLACK",
        ]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[ContentListResponse, AsyncV4PagePaginationArray[ContentListResponse]]:
        """
        List DLP content findings

        Args:
          direction: Direction to order results.

          dlp_profile_id: Filter by an DLP profile ID

          integration_id: Filter by an integration ID

          max_affliction_date: Filter to view findings that occurred on or before the affliction date. Can be a
              date-time in ISO 8601 format or an epoch timestamp.

          min_affliction_date: Filter to view findings that occurred on or after the affliction date. Can be a
              date-time in ISO 8601 format or an epoch timestamp.

          order: Which field to use when ordering content assets.

          page: A page number within the paginated result set.

          per_page: Number of results to return per page.

          search: A search term.

          vendor: Filter by vendor

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            path_template("/accounts/{account_id}/data-security/posture/content", account_id=account_id),
            page=AsyncV4PagePaginationArray[ContentListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "direction": direction,
                        "dlp_profile_id": dlp_profile_id,
                        "integration_id": integration_id,
                        "max_affliction_date": max_affliction_date,
                        "min_affliction_date": min_affliction_date,
                        "order": order,
                        "page": page,
                        "per_page": per_page,
                        "search": search,
                        "vendor": vendor,
                    },
                    content_list_params.ContentListParams,
                ),
            ),
            model=ContentListResponse,
        )

    async def export(
        self,
        *,
        account_id: str,
        dlp_profile_information: Iterable[content_export_params.DLPProfileInformation],
        dlp_profile_id: SequenceNotStr[str] | Omit = omit,
        integration_id: SequenceNotStr[str] | Omit = omit,
        max_affliction_date: Union[str, datetime] | Omit = omit,
        min_affliction_date: Union[str, datetime] | Omit = omit,
        orders: Iterable[content_export_params.Order] | Omit = omit,
        search: str | Omit = omit,
        vendors: List[
            Literal[
                "ANTHROPIC",
                "AWS",
                "BITBUCKET",
                "BOX",
                "CONFLUENCE",
                "DROPBOX",
                "GITHUB",
                "GOOGLE_CLOUD_PLATFORM",
                "GOOGLE_WORKSPACE",
                "JIRA",
                "MICROSOFT",
                "MICROSOFT_INTERNAL",
                "OPENAI",
                "SALESFORCE",
                "SERVICENOW",
                "SLACK",
            ]
        ]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[ContentExportResponse]:
        """
        Creates a CSV export for content and accepts optional filters in the payload.

        Args:
          dlp_profile_information: DLP profile metadata for the export.

          dlp_profile_id: Filter by DLP profile IDs.

          integration_id: Filter by integration IDs.

          max_affliction_date: Filter to view content flagged on or before this date.

          min_affliction_date: Filter to view content flagged on or after this date.

          orders: Ordering specifications for the export.

          search: Search term to filter content.

          vendors: Filter by vendor types.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._post(
            path_template("/accounts/{account_id}/data-security/posture/content/export", account_id=account_id),
            body=await async_maybe_transform(
                {
                    "dlp_profile_information": dlp_profile_information,
                    "dlp_profile_id": dlp_profile_id,
                    "integration_id": integration_id,
                    "max_affliction_date": max_affliction_date,
                    "min_affliction_date": min_affliction_date,
                    "orders": orders,
                    "search": search,
                    "vendors": vendors,
                },
                content_export_params.ContentExportParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[ContentExportResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[ContentExportResponse]], ResultWrapper[ContentExportResponse]),
        )


class ContentResourceWithRawResponse:
    def __init__(self, content: ContentResource) -> None:
        self._content = content

        self.list = to_raw_response_wrapper(
            content.list,
        )
        self.export = to_raw_response_wrapper(
            content.export,
        )


class AsyncContentResourceWithRawResponse:
    def __init__(self, content: AsyncContentResource) -> None:
        self._content = content

        self.list = async_to_raw_response_wrapper(
            content.list,
        )
        self.export = async_to_raw_response_wrapper(
            content.export,
        )


class ContentResourceWithStreamingResponse:
    def __init__(self, content: ContentResource) -> None:
        self._content = content

        self.list = to_streamed_response_wrapper(
            content.list,
        )
        self.export = to_streamed_response_wrapper(
            content.export,
        )


class AsyncContentResourceWithStreamingResponse:
    def __init__(self, content: AsyncContentResource) -> None:
        self._content = content

        self.list = async_to_streamed_response_wrapper(
            content.list,
        )
        self.export = async_to_streamed_response_wrapper(
            content.export,
        )
