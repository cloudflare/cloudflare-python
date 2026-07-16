# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ......_types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ......_utils import path_template, maybe_transform
from ......_compat import cached_property
from ......_resource import SyncAPIResource, AsyncAPIResource
from ......_response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ......pagination import SyncV4PagePaginationArray, AsyncV4PagePaginationArray
from ......_base_client import AsyncPaginator, make_request_options
from ......types.zero_trust.casb.posture.finding_types import remediation_type_list_params
from ......types.zero_trust.casb.posture.finding_types.remediation_type_list_response import RemediationTypeListResponse

__all__ = ["RemediationTypesResource", "AsyncRemediationTypesResource"]


class RemediationTypesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RemediationTypesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return RemediationTypesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RemediationTypesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return RemediationTypesResourceWithStreamingResponse(self)

    def list(
        self,
        finding_type_id: str,
        *,
        account_id: str,
        cursor: str | Omit = omit,
        integration_id: str | Omit = omit,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncV4PagePaginationArray[RemediationTypeListResponse]:
        """List all remediation types for a given finding type.

        This endpoint supports both
        cursor and offset pagination. Note that `cursor` and `page` are mutually
        exclusive.

        Args:
          cursor: A cursor for pagination.

          integration_id: Filter by an integration ID

          page: A page number within the paginated result set.

          per_page: Number of results to return per page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not finding_type_id:
            raise ValueError(f"Expected a non-empty value for `finding_type_id` but received {finding_type_id!r}")
        return self._get_api_list(
            path_template(
                "/accounts/{account_id}/data-security/posture/finding_types/{finding_type_id}/remediation_types",
                account_id=account_id,
                finding_type_id=finding_type_id,
            ),
            page=SyncV4PagePaginationArray[RemediationTypeListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "integration_id": integration_id,
                        "page": page,
                        "per_page": per_page,
                    },
                    remediation_type_list_params.RemediationTypeListParams,
                ),
            ),
            model=RemediationTypeListResponse,
        )


class AsyncRemediationTypesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRemediationTypesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRemediationTypesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRemediationTypesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncRemediationTypesResourceWithStreamingResponse(self)

    def list(
        self,
        finding_type_id: str,
        *,
        account_id: str,
        cursor: str | Omit = omit,
        integration_id: str | Omit = omit,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[RemediationTypeListResponse, AsyncV4PagePaginationArray[RemediationTypeListResponse]]:
        """List all remediation types for a given finding type.

        This endpoint supports both
        cursor and offset pagination. Note that `cursor` and `page` are mutually
        exclusive.

        Args:
          cursor: A cursor for pagination.

          integration_id: Filter by an integration ID

          page: A page number within the paginated result set.

          per_page: Number of results to return per page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not finding_type_id:
            raise ValueError(f"Expected a non-empty value for `finding_type_id` but received {finding_type_id!r}")
        return self._get_api_list(
            path_template(
                "/accounts/{account_id}/data-security/posture/finding_types/{finding_type_id}/remediation_types",
                account_id=account_id,
                finding_type_id=finding_type_id,
            ),
            page=AsyncV4PagePaginationArray[RemediationTypeListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "integration_id": integration_id,
                        "page": page,
                        "per_page": per_page,
                    },
                    remediation_type_list_params.RemediationTypeListParams,
                ),
            ),
            model=RemediationTypeListResponse,
        )


class RemediationTypesResourceWithRawResponse:
    def __init__(self, remediation_types: RemediationTypesResource) -> None:
        self._remediation_types = remediation_types

        self.list = to_raw_response_wrapper(
            remediation_types.list,
        )


class AsyncRemediationTypesResourceWithRawResponse:
    def __init__(self, remediation_types: AsyncRemediationTypesResource) -> None:
        self._remediation_types = remediation_types

        self.list = async_to_raw_response_wrapper(
            remediation_types.list,
        )


class RemediationTypesResourceWithStreamingResponse:
    def __init__(self, remediation_types: RemediationTypesResource) -> None:
        self._remediation_types = remediation_types

        self.list = to_streamed_response_wrapper(
            remediation_types.list,
        )


class AsyncRemediationTypesResourceWithStreamingResponse:
    def __init__(self, remediation_types: AsyncRemediationTypesResource) -> None:
        self._remediation_types = remediation_types

        self.list = async_to_streamed_response_wrapper(
            remediation_types.list,
        )
