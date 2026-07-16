# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Type, Union, Iterable, Optional, cast
from datetime import datetime
from typing_extensions import Literal

import httpx

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
from ......types.zero_trust.casb.posture.findings import (
    instance_list_params,
    instance_export_params,
    instance_archive_params,
    instance_unarchive_params,
)
from ......types.zero_trust.casb.posture.findings.instance_get_response import InstanceGetResponse
from ......types.zero_trust.casb.posture.findings.instance_list_response import InstanceListResponse
from ......types.zero_trust.casb.posture.findings.instance_export_response import InstanceExportResponse
from ......types.zero_trust.casb.posture.findings.instance_archive_response import InstanceArchiveResponse
from ......types.zero_trust.casb.posture.findings.instance_unarchive_response import InstanceUnarchiveResponse

__all__ = ["InstancesResource", "AsyncInstancesResource"]


class InstancesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> InstancesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return InstancesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> InstancesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return InstancesResourceWithStreamingResponse(self)

    def list(
        self,
        finding_id: Union[str, Base64FileInput],
        *,
        account_id: str,
        archived: bool | Omit = omit,
        asset_ids: SequenceNotStr[str] | Omit = omit,
        cursor: str | Omit = omit,
        direction: Literal["asc", "desc"] | Omit = omit,
        finding_instance_ids: SequenceNotStr[str] | Omit = omit,
        max_affliction_date: Union[str, datetime] | Omit = omit,
        min_affliction_date: Union[str, datetime] | Omit = omit,
        order: Literal["affliction_date", "asset.name", "remediation.status"] | Omit = omit,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        remediation_statuses: List[Literal["none", "pending", "processing", "validating", "completed", "failed"]]
        | Omit = omit,
        search: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncV4PagePaginationArray[InstanceListResponse]:
        """
        Lists all security finding instances for a given security finding.

        Args:
          archived: Archived

          asset_ids: Filter finding instances by an array of asset IDs. Supports multiple
              comma-separated values.

          cursor: A cursor for pagination. Obtained from the `result_info.cursor` field of a
              previous response.

          direction: Direction to order results.

          finding_instance_ids: Filter finding instances by an array of finding instance IDs. Supports multiple
              comma-separated values.

          max_affliction_date: Filter to view findings that occurred on or before the affliction date. Can be a
              date-time in ISO 8601 format or an epoch timestamp.

          min_affliction_date: Filter to view findings that occurred on or after the affliction date. Can be a
              date-time in ISO 8601 format or an epoch timestamp.

          order: Which field to use when ordering the Finding's instances. When ordering by
              'remediation.status', only the most recent non-stale remediation job is
              considered. Stale jobs (created before the instance's affliction_date) are
              treated as having no status for ordering purposes.

          page: A page number within the paginated result set.

          per_page: Number of results to return per page.

          remediation_statuses: Filter finding instances by most recent remediation job status. Supports
              multiple comma-separated values. Use 'none' to filter instances with no
              remediation jobs or instances where the most recent job is stale. Note: Stale
              jobs (created before the instance's affliction_date) are ignored for filtering
              purposes, but are still included in the 'remediations' array with stale=true.

          search: A search term.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not finding_id:
            raise ValueError(f"Expected a non-empty value for `finding_id` but received {finding_id!r}")
        return self._get_api_list(
            path_template(
                "/accounts/{account_id}/data-security/posture/findings/{finding_id}/instances",
                account_id=account_id,
                finding_id=finding_id,
            ),
            page=SyncV4PagePaginationArray[InstanceListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "archived": archived,
                        "asset_ids": asset_ids,
                        "cursor": cursor,
                        "direction": direction,
                        "finding_instance_ids": finding_instance_ids,
                        "max_affliction_date": max_affliction_date,
                        "min_affliction_date": min_affliction_date,
                        "order": order,
                        "page": page,
                        "per_page": per_page,
                        "remediation_statuses": remediation_statuses,
                        "search": search,
                    },
                    instance_list_params.InstanceListParams,
                ),
            ),
            model=InstanceListResponse,
        )

    def archive(
        self,
        finding_id: Union[str, Base64FileInput],
        *,
        account_id: str,
        check_instances: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[InstanceArchiveResponse]:
        """
        Archive one or more finding instances.

        Args:
          check_instances: A list of finding instance IDs to pass along.

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
                "/accounts/{account_id}/data-security/posture/findings/{finding_id}/instances/archive",
                account_id=account_id,
                finding_id=finding_id,
            ),
            body=maybe_transform({"check_instances": check_instances}, instance_archive_params.InstanceArchiveParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[InstanceArchiveResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[InstanceArchiveResponse]], ResultWrapper[InstanceArchiveResponse]),
        )

    def export(
        self,
        storage_namespace_id: str,
        *,
        account_id: str,
        archived: bool | Omit = omit,
        max_affliction_date: Union[str, datetime] | Omit = omit,
        min_affliction_date: Union[str, datetime] | Omit = omit,
        orders: Iterable[instance_export_params.Order] | Omit = omit,
        search: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[InstanceExportResponse]:
        """
        Creates a CSV export for Finding instances and accepts optional filters in the
        payload.

        The `storage_namespace_id` path parameter is derived from the finding ID by
        base64-decoding it (which yields `integration_id:finding_type_id`) and replacing
        the colon with a hyphen.

        Args:
          archived: Filter for archived status.

          max_affliction_date: Filter to view findings that occurred on or before the affliction date. Can be a
              date-time in ISO 8601 format or an epoch timestamp.

          min_affliction_date: Filter to view findings that occurred on or after the affliction date. Can be a
              date-time in ISO 8601 format or an epoch timestamp.

          orders: Ordering specifications for the export.

          search: A search term.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not storage_namespace_id:
            raise ValueError(
                f"Expected a non-empty value for `storage_namespace_id` but received {storage_namespace_id!r}"
            )
        return self._post(
            path_template(
                "/accounts/{account_id}/data-security/posture/findings/{storage_namespace_id}/instances/export",
                account_id=account_id,
                storage_namespace_id=storage_namespace_id,
            ),
            body=maybe_transform(
                {
                    "archived": archived,
                    "max_affliction_date": max_affliction_date,
                    "min_affliction_date": min_affliction_date,
                    "orders": orders,
                    "search": search,
                },
                instance_export_params.InstanceExportParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[InstanceExportResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[InstanceExportResponse]], ResultWrapper[InstanceExportResponse]),
        )

    def get(
        self,
        instance_id: str,
        *,
        account_id: str,
        finding_id: Union[str, Base64FileInput],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[InstanceGetResponse]:
        """
        Gets a security Finding instance by id.

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
        if not instance_id:
            raise ValueError(f"Expected a non-empty value for `instance_id` but received {instance_id!r}")
        return self._get(
            path_template(
                "/accounts/{account_id}/data-security/posture/findings/{finding_id}/instances/{instance_id}",
                account_id=account_id,
                finding_id=finding_id,
                instance_id=instance_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[InstanceGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[InstanceGetResponse]], ResultWrapper[InstanceGetResponse]),
        )

    def unarchive(
        self,
        finding_id: Union[str, Base64FileInput],
        *,
        account_id: str,
        check_instances: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[InstanceUnarchiveResponse]:
        """
        Remove the archive marking from one or more finding instances.

        Args:
          check_instances: A list of finding instance IDs to pass along.

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
                "/accounts/{account_id}/data-security/posture/findings/{finding_id}/instances/unarchive",
                account_id=account_id,
                finding_id=finding_id,
            ),
            body=maybe_transform(
                {"check_instances": check_instances}, instance_unarchive_params.InstanceUnarchiveParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[InstanceUnarchiveResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[InstanceUnarchiveResponse]], ResultWrapper[InstanceUnarchiveResponse]),
        )


class AsyncInstancesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncInstancesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncInstancesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncInstancesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncInstancesResourceWithStreamingResponse(self)

    def list(
        self,
        finding_id: Union[str, Base64FileInput],
        *,
        account_id: str,
        archived: bool | Omit = omit,
        asset_ids: SequenceNotStr[str] | Omit = omit,
        cursor: str | Omit = omit,
        direction: Literal["asc", "desc"] | Omit = omit,
        finding_instance_ids: SequenceNotStr[str] | Omit = omit,
        max_affliction_date: Union[str, datetime] | Omit = omit,
        min_affliction_date: Union[str, datetime] | Omit = omit,
        order: Literal["affliction_date", "asset.name", "remediation.status"] | Omit = omit,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        remediation_statuses: List[Literal["none", "pending", "processing", "validating", "completed", "failed"]]
        | Omit = omit,
        search: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[InstanceListResponse, AsyncV4PagePaginationArray[InstanceListResponse]]:
        """
        Lists all security finding instances for a given security finding.

        Args:
          archived: Archived

          asset_ids: Filter finding instances by an array of asset IDs. Supports multiple
              comma-separated values.

          cursor: A cursor for pagination. Obtained from the `result_info.cursor` field of a
              previous response.

          direction: Direction to order results.

          finding_instance_ids: Filter finding instances by an array of finding instance IDs. Supports multiple
              comma-separated values.

          max_affliction_date: Filter to view findings that occurred on or before the affliction date. Can be a
              date-time in ISO 8601 format or an epoch timestamp.

          min_affliction_date: Filter to view findings that occurred on or after the affliction date. Can be a
              date-time in ISO 8601 format or an epoch timestamp.

          order: Which field to use when ordering the Finding's instances. When ordering by
              'remediation.status', only the most recent non-stale remediation job is
              considered. Stale jobs (created before the instance's affliction_date) are
              treated as having no status for ordering purposes.

          page: A page number within the paginated result set.

          per_page: Number of results to return per page.

          remediation_statuses: Filter finding instances by most recent remediation job status. Supports
              multiple comma-separated values. Use 'none' to filter instances with no
              remediation jobs or instances where the most recent job is stale. Note: Stale
              jobs (created before the instance's affliction_date) are ignored for filtering
              purposes, but are still included in the 'remediations' array with stale=true.

          search: A search term.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not finding_id:
            raise ValueError(f"Expected a non-empty value for `finding_id` but received {finding_id!r}")
        return self._get_api_list(
            path_template(
                "/accounts/{account_id}/data-security/posture/findings/{finding_id}/instances",
                account_id=account_id,
                finding_id=finding_id,
            ),
            page=AsyncV4PagePaginationArray[InstanceListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "archived": archived,
                        "asset_ids": asset_ids,
                        "cursor": cursor,
                        "direction": direction,
                        "finding_instance_ids": finding_instance_ids,
                        "max_affliction_date": max_affliction_date,
                        "min_affliction_date": min_affliction_date,
                        "order": order,
                        "page": page,
                        "per_page": per_page,
                        "remediation_statuses": remediation_statuses,
                        "search": search,
                    },
                    instance_list_params.InstanceListParams,
                ),
            ),
            model=InstanceListResponse,
        )

    async def archive(
        self,
        finding_id: Union[str, Base64FileInput],
        *,
        account_id: str,
        check_instances: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[InstanceArchiveResponse]:
        """
        Archive one or more finding instances.

        Args:
          check_instances: A list of finding instance IDs to pass along.

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
                "/accounts/{account_id}/data-security/posture/findings/{finding_id}/instances/archive",
                account_id=account_id,
                finding_id=finding_id,
            ),
            body=await async_maybe_transform(
                {"check_instances": check_instances}, instance_archive_params.InstanceArchiveParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[InstanceArchiveResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[InstanceArchiveResponse]], ResultWrapper[InstanceArchiveResponse]),
        )

    async def export(
        self,
        storage_namespace_id: str,
        *,
        account_id: str,
        archived: bool | Omit = omit,
        max_affliction_date: Union[str, datetime] | Omit = omit,
        min_affliction_date: Union[str, datetime] | Omit = omit,
        orders: Iterable[instance_export_params.Order] | Omit = omit,
        search: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[InstanceExportResponse]:
        """
        Creates a CSV export for Finding instances and accepts optional filters in the
        payload.

        The `storage_namespace_id` path parameter is derived from the finding ID by
        base64-decoding it (which yields `integration_id:finding_type_id`) and replacing
        the colon with a hyphen.

        Args:
          archived: Filter for archived status.

          max_affliction_date: Filter to view findings that occurred on or before the affliction date. Can be a
              date-time in ISO 8601 format or an epoch timestamp.

          min_affliction_date: Filter to view findings that occurred on or after the affliction date. Can be a
              date-time in ISO 8601 format or an epoch timestamp.

          orders: Ordering specifications for the export.

          search: A search term.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not storage_namespace_id:
            raise ValueError(
                f"Expected a non-empty value for `storage_namespace_id` but received {storage_namespace_id!r}"
            )
        return await self._post(
            path_template(
                "/accounts/{account_id}/data-security/posture/findings/{storage_namespace_id}/instances/export",
                account_id=account_id,
                storage_namespace_id=storage_namespace_id,
            ),
            body=await async_maybe_transform(
                {
                    "archived": archived,
                    "max_affliction_date": max_affliction_date,
                    "min_affliction_date": min_affliction_date,
                    "orders": orders,
                    "search": search,
                },
                instance_export_params.InstanceExportParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[InstanceExportResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[InstanceExportResponse]], ResultWrapper[InstanceExportResponse]),
        )

    async def get(
        self,
        instance_id: str,
        *,
        account_id: str,
        finding_id: Union[str, Base64FileInput],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[InstanceGetResponse]:
        """
        Gets a security Finding instance by id.

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
        if not instance_id:
            raise ValueError(f"Expected a non-empty value for `instance_id` but received {instance_id!r}")
        return await self._get(
            path_template(
                "/accounts/{account_id}/data-security/posture/findings/{finding_id}/instances/{instance_id}",
                account_id=account_id,
                finding_id=finding_id,
                instance_id=instance_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[InstanceGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[InstanceGetResponse]], ResultWrapper[InstanceGetResponse]),
        )

    async def unarchive(
        self,
        finding_id: Union[str, Base64FileInput],
        *,
        account_id: str,
        check_instances: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[InstanceUnarchiveResponse]:
        """
        Remove the archive marking from one or more finding instances.

        Args:
          check_instances: A list of finding instance IDs to pass along.

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
                "/accounts/{account_id}/data-security/posture/findings/{finding_id}/instances/unarchive",
                account_id=account_id,
                finding_id=finding_id,
            ),
            body=await async_maybe_transform(
                {"check_instances": check_instances}, instance_unarchive_params.InstanceUnarchiveParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[InstanceUnarchiveResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[InstanceUnarchiveResponse]], ResultWrapper[InstanceUnarchiveResponse]),
        )


class InstancesResourceWithRawResponse:
    def __init__(self, instances: InstancesResource) -> None:
        self._instances = instances

        self.list = to_raw_response_wrapper(
            instances.list,
        )
        self.archive = to_raw_response_wrapper(
            instances.archive,
        )
        self.export = to_raw_response_wrapper(
            instances.export,
        )
        self.get = to_raw_response_wrapper(
            instances.get,
        )
        self.unarchive = to_raw_response_wrapper(
            instances.unarchive,
        )


class AsyncInstancesResourceWithRawResponse:
    def __init__(self, instances: AsyncInstancesResource) -> None:
        self._instances = instances

        self.list = async_to_raw_response_wrapper(
            instances.list,
        )
        self.archive = async_to_raw_response_wrapper(
            instances.archive,
        )
        self.export = async_to_raw_response_wrapper(
            instances.export,
        )
        self.get = async_to_raw_response_wrapper(
            instances.get,
        )
        self.unarchive = async_to_raw_response_wrapper(
            instances.unarchive,
        )


class InstancesResourceWithStreamingResponse:
    def __init__(self, instances: InstancesResource) -> None:
        self._instances = instances

        self.list = to_streamed_response_wrapper(
            instances.list,
        )
        self.archive = to_streamed_response_wrapper(
            instances.archive,
        )
        self.export = to_streamed_response_wrapper(
            instances.export,
        )
        self.get = to_streamed_response_wrapper(
            instances.get,
        )
        self.unarchive = to_streamed_response_wrapper(
            instances.unarchive,
        )


class AsyncInstancesResourceWithStreamingResponse:
    def __init__(self, instances: AsyncInstancesResource) -> None:
        self._instances = instances

        self.list = async_to_streamed_response_wrapper(
            instances.list,
        )
        self.archive = async_to_streamed_response_wrapper(
            instances.archive,
        )
        self.export = async_to_streamed_response_wrapper(
            instances.export,
        )
        self.get = async_to_streamed_response_wrapper(
            instances.get,
        )
        self.unarchive = async_to_streamed_response_wrapper(
            instances.unarchive,
        )
