# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Type, Union, Iterable, Optional, cast
from datetime import datetime
from typing_extensions import Literal

import httpx

from .instances import (
    InstancesResource,
    AsyncInstancesResource,
    InstancesResourceWithRawResponse,
    AsyncInstancesResourceWithRawResponse,
    InstancesResourceWithStreamingResponse,
    AsyncInstancesResourceWithStreamingResponse,
)
from ......_types import (
    Body,
    Omit,
    Query,
    Headers,
    NotGiven,
    SequenceNotStr,
    Base64FileInput,
    omit,
    not_given,
)
from ......_utils import path_template, maybe_transform, async_maybe_transform
from ......_compat import cached_property
from ......_resource import SyncAPIResource, AsyncAPIResource
from ......_response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ......_wrappers import ResultWrapper
from ......pagination import SyncV4PagePaginationArray, AsyncV4PagePaginationArray
from ......_base_client import AsyncPaginator, make_request_options
from ......types.zero_trust.casb.posture import (
    finding_list_params,
    finding_export_params,
    finding_ignore_params,
    finding_unignore_params,
    finding_tune_severity_params,
)
from ......types.zero_trust.casb.posture.finding_get_response import FindingGetResponse
from ......types.zero_trust.casb.posture.finding_list_response import FindingListResponse
from ......types.zero_trust.casb.posture.finding_export_response import FindingExportResponse
from ......types.zero_trust.casb.posture.finding_ignore_response import FindingIgnoreResponse
from ......types.zero_trust.casb.posture.finding_unignore_response import FindingUnignoreResponse
from ......types.zero_trust.casb.posture.finding_tune_severity_response import FindingTuneSeverityResponse
from ......types.zero_trust.casb.posture.finding_reset_severity_response import FindingResetSeverityResponse

__all__ = ["FindingsResource", "AsyncFindingsResource"]


class FindingsResource(SyncAPIResource):
    @cached_property
    def instances(self) -> InstancesResource:
        return InstancesResource(self._client)

    @cached_property
    def with_raw_response(self) -> FindingsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return FindingsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FindingsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return FindingsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        account_id: str,
        cursor: str | Omit = omit,
        direction: Literal["asc", "desc"] | Omit = omit,
        finding_type_ids: str | Omit = omit,
        ignored: bool | Omit = omit,
        integration_id: str | Omit = omit,
        max_affliction_date: Union[str, datetime] | Omit = omit,
        min_affliction_date: Union[str, datetime] | Omit = omit,
        observation: Literal["Activity", "Insight", "Issue"] | Omit = omit,
        order: Literal["finding.name", "instance_count", "integration.name", "latest_affliction_date", "severity"]
        | Omit = omit,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        product: Literal["Cloud", "Saas"] | Omit = omit,
        search: str | Omit = omit,
        severity: Literal["Critical", "High", "Medium", "Low"] | Omit = omit,
        type: Literal["Content", "Posture"] | Omit = omit,
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
    ) -> SyncV4PagePaginationArray[FindingListResponse]:
        """List all security findings that have been identified as being problematic.

        This
        will return a list of findings regardless if they have been ignored or not.

        Args:
          cursor: A cursor for pagination. Obtained from the `result_info.cursor` field of a
              previous response.

          direction: Direction to order results.

          finding_type_ids: A comma separated list of UUIDs identifying the finding type(s).

          ignored: Filter for only the ignored findings. Set to false to only see "active" items

          integration_id: Filter by an integration ID

          max_affliction_date: Filter to view findings that occurred on or before the affliction date. Can be a
              date-time in ISO 8601 format or an epoch timestamp.

          min_affliction_date: Filter to view findings that occurred on or after the affliction date. Can be a
              date-time in ISO 8601 format or an epoch timestamp.

          observation: Filter by observation type of the finding

          order: Which field to use when ordering the findings.

          page: A page number within the paginated result set.

          per_page: Number of results to return per page.

          product: Filter by product category of the finding

          search: A search term.

          severity: Filter by severity

          type: Filter by type of the finding

          vendor: Filter by vendor

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            path_template("/accounts/{account_id}/data-security/posture/findings", account_id=account_id),
            page=SyncV4PagePaginationArray[FindingListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "direction": direction,
                        "finding_type_ids": finding_type_ids,
                        "ignored": ignored,
                        "integration_id": integration_id,
                        "max_affliction_date": max_affliction_date,
                        "min_affliction_date": min_affliction_date,
                        "observation": observation,
                        "order": order,
                        "page": page,
                        "per_page": per_page,
                        "product": product,
                        "search": search,
                        "severity": severity,
                        "type": type,
                        "vendor": vendor,
                    },
                    finding_list_params.FindingListParams,
                ),
            ),
            model=FindingListResponse,
        )

    def export(
        self,
        *,
        account_id: str,
        ignored: bool | Omit = omit,
        integration_id: SequenceNotStr[str] | Omit = omit,
        max_affliction_date: Union[str, datetime] | Omit = omit,
        min_affliction_date: Union[str, datetime] | Omit = omit,
        orders: Iterable[finding_export_params.Order] | Omit = omit,
        product: Optional[Literal["SaaS", "Cloud"]] | Omit = omit,
        search: str | Omit = omit,
        severities: List[Literal["CRITICAL", "HIGH", "MEDIUM", "LOW"]] | Omit = omit,
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
    ) -> Optional[FindingExportResponse]:
        """
        Creates a CSV export for findings and accepts optional filters in the payload.

        Args:
          ignored: Filter for only the ignored findings. Set to false to only see active items.

          integration_id: Filter by multiple integration IDs.

          max_affliction_date: Filter to view findings that occurred on or before the affliction date. Can be a
              date-time in ISO 8601 format or an epoch timestamp.

          min_affliction_date: Filter to view findings that occurred on or after the affliction date. Can be a
              date-time in ISO 8601 format or an epoch timestamp.

          orders: Which fields to use when ordering the findings.

          product: Filter by finding's category product.

          search: A search term.

          severities: Filter by severity levels.

          vendors: Filter by vendor types.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._post(
            path_template("/accounts/{account_id}/data-security/posture/findings/export", account_id=account_id),
            body=maybe_transform(
                {
                    "ignored": ignored,
                    "integration_id": integration_id,
                    "max_affliction_date": max_affliction_date,
                    "min_affliction_date": min_affliction_date,
                    "orders": orders,
                    "product": product,
                    "search": search,
                    "severities": severities,
                    "vendors": vendors,
                },
                finding_export_params.FindingExportParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[FindingExportResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[FindingExportResponse]], ResultWrapper[FindingExportResponse]),
        )

    def get(
        self,
        finding_id: Union[str, Base64FileInput],
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[FindingGetResponse]:
        """
        Gets a security Finding that has been identified as being problematic.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not finding_id:
            raise ValueError(f"Expected a non-empty value for `finding_id` but received {finding_id!r}")
        return self._get(
            path_template(
                "/accounts/{account_id}/data-security/posture/findings/{finding_id}",
                account_id=account_id,
                finding_id=finding_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[FindingGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[FindingGetResponse]], ResultWrapper[FindingGetResponse]),
        )

    def ignore(
        self,
        *,
        account_id: str,
        checks: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[FindingIgnoreResponse]:
        """Given a list of findings, mark as ignored.

        Does nothing if Finding is already
        ignored.

        Args:
          checks: A list of finding IDs to pass along.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._post(
            path_template("/accounts/{account_id}/data-security/posture/findings/ignore", account_id=account_id),
            body=maybe_transform({"checks": checks}, finding_ignore_params.FindingIgnoreParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[FindingIgnoreResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[FindingIgnoreResponse]], ResultWrapper[FindingIgnoreResponse]),
        )

    def reset_severity(
        self,
        finding_id: Union[str, Base64FileInput],
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[FindingResetSeverityResponse]:
        """If a Finding's severity has been changed, reset it back to default value.

        Does
        nothing if no override exists.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not finding_id:
            raise ValueError(f"Expected a non-empty value for `finding_id` but received {finding_id!r}")
        return self._post(
            path_template(
                "/accounts/{account_id}/data-security/posture/findings/{finding_id}/reset_finding_severity",
                account_id=account_id,
                finding_id=finding_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[FindingResetSeverityResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[FindingResetSeverityResponse]], ResultWrapper[FindingResetSeverityResponse]),
        )

    def tune_severity(
        self,
        finding_id: Union[str, Base64FileInput],
        *,
        account_id: str,
        new_severity: Literal[1, 2, 3, 4],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[FindingTuneSeverityResponse]:
        """Update the severity of a Finding.

        This will update the `severity_override` field
        on the Finding payload with the new severity value.

        Args:
          new_severity: The numeric severity value to apply to the finding.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not finding_id:
            raise ValueError(f"Expected a non-empty value for `finding_id` but received {finding_id!r}")
        return self._post(
            path_template(
                "/accounts/{account_id}/data-security/posture/findings/{finding_id}/tune_finding_severity",
                account_id=account_id,
                finding_id=finding_id,
            ),
            body=maybe_transform(
                {"new_severity": new_severity}, finding_tune_severity_params.FindingTuneSeverityParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[FindingTuneSeverityResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[FindingTuneSeverityResponse]], ResultWrapper[FindingTuneSeverityResponse]),
        )

    def unignore(
        self,
        *,
        account_id: str,
        checks: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[FindingUnignoreResponse]:
        """Ability to un-ignore a Finding if it's previously been ignored.

        Does nothing if
        the Finding is not ignored.

        Args:
          checks: A list of finding IDs to pass along.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._post(
            path_template("/accounts/{account_id}/data-security/posture/findings/unignore", account_id=account_id),
            body=maybe_transform({"checks": checks}, finding_unignore_params.FindingUnignoreParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[FindingUnignoreResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[FindingUnignoreResponse]], ResultWrapper[FindingUnignoreResponse]),
        )


class AsyncFindingsResource(AsyncAPIResource):
    @cached_property
    def instances(self) -> AsyncInstancesResource:
        return AsyncInstancesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncFindingsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncFindingsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFindingsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncFindingsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        account_id: str,
        cursor: str | Omit = omit,
        direction: Literal["asc", "desc"] | Omit = omit,
        finding_type_ids: str | Omit = omit,
        ignored: bool | Omit = omit,
        integration_id: str | Omit = omit,
        max_affliction_date: Union[str, datetime] | Omit = omit,
        min_affliction_date: Union[str, datetime] | Omit = omit,
        observation: Literal["Activity", "Insight", "Issue"] | Omit = omit,
        order: Literal["finding.name", "instance_count", "integration.name", "latest_affliction_date", "severity"]
        | Omit = omit,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        product: Literal["Cloud", "Saas"] | Omit = omit,
        search: str | Omit = omit,
        severity: Literal["Critical", "High", "Medium", "Low"] | Omit = omit,
        type: Literal["Content", "Posture"] | Omit = omit,
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
    ) -> AsyncPaginator[FindingListResponse, AsyncV4PagePaginationArray[FindingListResponse]]:
        """List all security findings that have been identified as being problematic.

        This
        will return a list of findings regardless if they have been ignored or not.

        Args:
          cursor: A cursor for pagination. Obtained from the `result_info.cursor` field of a
              previous response.

          direction: Direction to order results.

          finding_type_ids: A comma separated list of UUIDs identifying the finding type(s).

          ignored: Filter for only the ignored findings. Set to false to only see "active" items

          integration_id: Filter by an integration ID

          max_affliction_date: Filter to view findings that occurred on or before the affliction date. Can be a
              date-time in ISO 8601 format or an epoch timestamp.

          min_affliction_date: Filter to view findings that occurred on or after the affliction date. Can be a
              date-time in ISO 8601 format or an epoch timestamp.

          observation: Filter by observation type of the finding

          order: Which field to use when ordering the findings.

          page: A page number within the paginated result set.

          per_page: Number of results to return per page.

          product: Filter by product category of the finding

          search: A search term.

          severity: Filter by severity

          type: Filter by type of the finding

          vendor: Filter by vendor

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            path_template("/accounts/{account_id}/data-security/posture/findings", account_id=account_id),
            page=AsyncV4PagePaginationArray[FindingListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "direction": direction,
                        "finding_type_ids": finding_type_ids,
                        "ignored": ignored,
                        "integration_id": integration_id,
                        "max_affliction_date": max_affliction_date,
                        "min_affliction_date": min_affliction_date,
                        "observation": observation,
                        "order": order,
                        "page": page,
                        "per_page": per_page,
                        "product": product,
                        "search": search,
                        "severity": severity,
                        "type": type,
                        "vendor": vendor,
                    },
                    finding_list_params.FindingListParams,
                ),
            ),
            model=FindingListResponse,
        )

    async def export(
        self,
        *,
        account_id: str,
        ignored: bool | Omit = omit,
        integration_id: SequenceNotStr[str] | Omit = omit,
        max_affliction_date: Union[str, datetime] | Omit = omit,
        min_affliction_date: Union[str, datetime] | Omit = omit,
        orders: Iterable[finding_export_params.Order] | Omit = omit,
        product: Optional[Literal["SaaS", "Cloud"]] | Omit = omit,
        search: str | Omit = omit,
        severities: List[Literal["CRITICAL", "HIGH", "MEDIUM", "LOW"]] | Omit = omit,
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
    ) -> Optional[FindingExportResponse]:
        """
        Creates a CSV export for findings and accepts optional filters in the payload.

        Args:
          ignored: Filter for only the ignored findings. Set to false to only see active items.

          integration_id: Filter by multiple integration IDs.

          max_affliction_date: Filter to view findings that occurred on or before the affliction date. Can be a
              date-time in ISO 8601 format or an epoch timestamp.

          min_affliction_date: Filter to view findings that occurred on or after the affliction date. Can be a
              date-time in ISO 8601 format or an epoch timestamp.

          orders: Which fields to use when ordering the findings.

          product: Filter by finding's category product.

          search: A search term.

          severities: Filter by severity levels.

          vendors: Filter by vendor types.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._post(
            path_template("/accounts/{account_id}/data-security/posture/findings/export", account_id=account_id),
            body=await async_maybe_transform(
                {
                    "ignored": ignored,
                    "integration_id": integration_id,
                    "max_affliction_date": max_affliction_date,
                    "min_affliction_date": min_affliction_date,
                    "orders": orders,
                    "product": product,
                    "search": search,
                    "severities": severities,
                    "vendors": vendors,
                },
                finding_export_params.FindingExportParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[FindingExportResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[FindingExportResponse]], ResultWrapper[FindingExportResponse]),
        )

    async def get(
        self,
        finding_id: Union[str, Base64FileInput],
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[FindingGetResponse]:
        """
        Gets a security Finding that has been identified as being problematic.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not finding_id:
            raise ValueError(f"Expected a non-empty value for `finding_id` but received {finding_id!r}")
        return await self._get(
            path_template(
                "/accounts/{account_id}/data-security/posture/findings/{finding_id}",
                account_id=account_id,
                finding_id=finding_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[FindingGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[FindingGetResponse]], ResultWrapper[FindingGetResponse]),
        )

    async def ignore(
        self,
        *,
        account_id: str,
        checks: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[FindingIgnoreResponse]:
        """Given a list of findings, mark as ignored.

        Does nothing if Finding is already
        ignored.

        Args:
          checks: A list of finding IDs to pass along.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._post(
            path_template("/accounts/{account_id}/data-security/posture/findings/ignore", account_id=account_id),
            body=await async_maybe_transform({"checks": checks}, finding_ignore_params.FindingIgnoreParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[FindingIgnoreResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[FindingIgnoreResponse]], ResultWrapper[FindingIgnoreResponse]),
        )

    async def reset_severity(
        self,
        finding_id: Union[str, Base64FileInput],
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[FindingResetSeverityResponse]:
        """If a Finding's severity has been changed, reset it back to default value.

        Does
        nothing if no override exists.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not finding_id:
            raise ValueError(f"Expected a non-empty value for `finding_id` but received {finding_id!r}")
        return await self._post(
            path_template(
                "/accounts/{account_id}/data-security/posture/findings/{finding_id}/reset_finding_severity",
                account_id=account_id,
                finding_id=finding_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[FindingResetSeverityResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[FindingResetSeverityResponse]], ResultWrapper[FindingResetSeverityResponse]),
        )

    async def tune_severity(
        self,
        finding_id: Union[str, Base64FileInput],
        *,
        account_id: str,
        new_severity: Literal[1, 2, 3, 4],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[FindingTuneSeverityResponse]:
        """Update the severity of a Finding.

        This will update the `severity_override` field
        on the Finding payload with the new severity value.

        Args:
          new_severity: The numeric severity value to apply to the finding.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not finding_id:
            raise ValueError(f"Expected a non-empty value for `finding_id` but received {finding_id!r}")
        return await self._post(
            path_template(
                "/accounts/{account_id}/data-security/posture/findings/{finding_id}/tune_finding_severity",
                account_id=account_id,
                finding_id=finding_id,
            ),
            body=await async_maybe_transform(
                {"new_severity": new_severity}, finding_tune_severity_params.FindingTuneSeverityParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[FindingTuneSeverityResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[FindingTuneSeverityResponse]], ResultWrapper[FindingTuneSeverityResponse]),
        )

    async def unignore(
        self,
        *,
        account_id: str,
        checks: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[FindingUnignoreResponse]:
        """Ability to un-ignore a Finding if it's previously been ignored.

        Does nothing if
        the Finding is not ignored.

        Args:
          checks: A list of finding IDs to pass along.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._post(
            path_template("/accounts/{account_id}/data-security/posture/findings/unignore", account_id=account_id),
            body=await async_maybe_transform({"checks": checks}, finding_unignore_params.FindingUnignoreParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[FindingUnignoreResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[FindingUnignoreResponse]], ResultWrapper[FindingUnignoreResponse]),
        )


class FindingsResourceWithRawResponse:
    def __init__(self, findings: FindingsResource) -> None:
        self._findings = findings

        self.list = to_raw_response_wrapper(
            findings.list,
        )
        self.export = to_raw_response_wrapper(
            findings.export,
        )
        self.get = to_raw_response_wrapper(
            findings.get,
        )
        self.ignore = to_raw_response_wrapper(
            findings.ignore,
        )
        self.reset_severity = to_raw_response_wrapper(
            findings.reset_severity,
        )
        self.tune_severity = to_raw_response_wrapper(
            findings.tune_severity,
        )
        self.unignore = to_raw_response_wrapper(
            findings.unignore,
        )

    @cached_property
    def instances(self) -> InstancesResourceWithRawResponse:
        return InstancesResourceWithRawResponse(self._findings.instances)


class AsyncFindingsResourceWithRawResponse:
    def __init__(self, findings: AsyncFindingsResource) -> None:
        self._findings = findings

        self.list = async_to_raw_response_wrapper(
            findings.list,
        )
        self.export = async_to_raw_response_wrapper(
            findings.export,
        )
        self.get = async_to_raw_response_wrapper(
            findings.get,
        )
        self.ignore = async_to_raw_response_wrapper(
            findings.ignore,
        )
        self.reset_severity = async_to_raw_response_wrapper(
            findings.reset_severity,
        )
        self.tune_severity = async_to_raw_response_wrapper(
            findings.tune_severity,
        )
        self.unignore = async_to_raw_response_wrapper(
            findings.unignore,
        )

    @cached_property
    def instances(self) -> AsyncInstancesResourceWithRawResponse:
        return AsyncInstancesResourceWithRawResponse(self._findings.instances)


class FindingsResourceWithStreamingResponse:
    def __init__(self, findings: FindingsResource) -> None:
        self._findings = findings

        self.list = to_streamed_response_wrapper(
            findings.list,
        )
        self.export = to_streamed_response_wrapper(
            findings.export,
        )
        self.get = to_streamed_response_wrapper(
            findings.get,
        )
        self.ignore = to_streamed_response_wrapper(
            findings.ignore,
        )
        self.reset_severity = to_streamed_response_wrapper(
            findings.reset_severity,
        )
        self.tune_severity = to_streamed_response_wrapper(
            findings.tune_severity,
        )
        self.unignore = to_streamed_response_wrapper(
            findings.unignore,
        )

    @cached_property
    def instances(self) -> InstancesResourceWithStreamingResponse:
        return InstancesResourceWithStreamingResponse(self._findings.instances)


class AsyncFindingsResourceWithStreamingResponse:
    def __init__(self, findings: AsyncFindingsResource) -> None:
        self._findings = findings

        self.list = async_to_streamed_response_wrapper(
            findings.list,
        )
        self.export = async_to_streamed_response_wrapper(
            findings.export,
        )
        self.get = async_to_streamed_response_wrapper(
            findings.get,
        )
        self.ignore = async_to_streamed_response_wrapper(
            findings.ignore,
        )
        self.reset_severity = async_to_streamed_response_wrapper(
            findings.reset_severity,
        )
        self.tune_severity = async_to_streamed_response_wrapper(
            findings.tune_severity,
        )
        self.unignore = async_to_streamed_response_wrapper(
            findings.unignore,
        )

    @cached_property
    def instances(self) -> AsyncInstancesResourceWithStreamingResponse:
        return AsyncInstancesResourceWithStreamingResponse(self._findings.instances)
