# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Optional, cast

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
from ......_wrappers import ResultWrapper
from ......pagination import SyncV4PagePaginationArray, AsyncV4PagePaginationArray
from ......_base_client import AsyncPaginator, make_request_options
from .remediation_types import (
    RemediationTypesResource,
    AsyncRemediationTypesResource,
    RemediationTypesResourceWithRawResponse,
    AsyncRemediationTypesResourceWithRawResponse,
    RemediationTypesResourceWithStreamingResponse,
    AsyncRemediationTypesResourceWithStreamingResponse,
)
from ......types.zero_trust.casb.posture import finding_type_list_params
from ......types.zero_trust.casb.posture.finding_type_get_response import FindingTypeGetResponse
from ......types.zero_trust.casb.posture.finding_type_list_response import FindingTypeListResponse

__all__ = ["FindingTypesResource", "AsyncFindingTypesResource"]


class FindingTypesResource(SyncAPIResource):
    @cached_property
    def remediation_types(self) -> RemediationTypesResource:
        return RemediationTypesResource(self._client)

    @cached_property
    def with_raw_response(self) -> FindingTypesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return FindingTypesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FindingTypesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return FindingTypesResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        account_id: str,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncV4PagePaginationArray[FindingTypeListResponse]:
        """
        List all available finding types with pagination support.

        Args:
          page: A page number within the paginated result set.

          per_page: Number of results to return per page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            path_template("/accounts/{account_id}/data-security/posture/finding_types", account_id=account_id),
            page=SyncV4PagePaginationArray[FindingTypeListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page": page,
                        "per_page": per_page,
                    },
                    finding_type_list_params.FindingTypeListParams,
                ),
            ),
            model=FindingTypeListResponse,
        )

    def get(
        self,
        finding_type_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[FindingTypeGetResponse]:
        """
        Retrieve a specific finding type by its unique identifier.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not finding_type_id:
            raise ValueError(f"Expected a non-empty value for `finding_type_id` but received {finding_type_id!r}")
        return self._get(
            path_template(
                "/accounts/{account_id}/data-security/posture/finding_types/{finding_type_id}",
                account_id=account_id,
                finding_type_id=finding_type_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[FindingTypeGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[FindingTypeGetResponse]], ResultWrapper[FindingTypeGetResponse]),
        )


class AsyncFindingTypesResource(AsyncAPIResource):
    @cached_property
    def remediation_types(self) -> AsyncRemediationTypesResource:
        return AsyncRemediationTypesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncFindingTypesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncFindingTypesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFindingTypesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncFindingTypesResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        account_id: str,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[FindingTypeListResponse, AsyncV4PagePaginationArray[FindingTypeListResponse]]:
        """
        List all available finding types with pagination support.

        Args:
          page: A page number within the paginated result set.

          per_page: Number of results to return per page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            path_template("/accounts/{account_id}/data-security/posture/finding_types", account_id=account_id),
            page=AsyncV4PagePaginationArray[FindingTypeListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page": page,
                        "per_page": per_page,
                    },
                    finding_type_list_params.FindingTypeListParams,
                ),
            ),
            model=FindingTypeListResponse,
        )

    async def get(
        self,
        finding_type_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[FindingTypeGetResponse]:
        """
        Retrieve a specific finding type by its unique identifier.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not finding_type_id:
            raise ValueError(f"Expected a non-empty value for `finding_type_id` but received {finding_type_id!r}")
        return await self._get(
            path_template(
                "/accounts/{account_id}/data-security/posture/finding_types/{finding_type_id}",
                account_id=account_id,
                finding_type_id=finding_type_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[FindingTypeGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[FindingTypeGetResponse]], ResultWrapper[FindingTypeGetResponse]),
        )


class FindingTypesResourceWithRawResponse:
    def __init__(self, finding_types: FindingTypesResource) -> None:
        self._finding_types = finding_types

        self.list = to_raw_response_wrapper(
            finding_types.list,
        )
        self.get = to_raw_response_wrapper(
            finding_types.get,
        )

    @cached_property
    def remediation_types(self) -> RemediationTypesResourceWithRawResponse:
        return RemediationTypesResourceWithRawResponse(self._finding_types.remediation_types)


class AsyncFindingTypesResourceWithRawResponse:
    def __init__(self, finding_types: AsyncFindingTypesResource) -> None:
        self._finding_types = finding_types

        self.list = async_to_raw_response_wrapper(
            finding_types.list,
        )
        self.get = async_to_raw_response_wrapper(
            finding_types.get,
        )

    @cached_property
    def remediation_types(self) -> AsyncRemediationTypesResourceWithRawResponse:
        return AsyncRemediationTypesResourceWithRawResponse(self._finding_types.remediation_types)


class FindingTypesResourceWithStreamingResponse:
    def __init__(self, finding_types: FindingTypesResource) -> None:
        self._finding_types = finding_types

        self.list = to_streamed_response_wrapper(
            finding_types.list,
        )
        self.get = to_streamed_response_wrapper(
            finding_types.get,
        )

    @cached_property
    def remediation_types(self) -> RemediationTypesResourceWithStreamingResponse:
        return RemediationTypesResourceWithStreamingResponse(self._finding_types.remediation_types)


class AsyncFindingTypesResourceWithStreamingResponse:
    def __init__(self, finding_types: AsyncFindingTypesResource) -> None:
        self._finding_types = finding_types

        self.list = async_to_streamed_response_wrapper(
            finding_types.list,
        )
        self.get = async_to_streamed_response_wrapper(
            finding_types.get,
        )

    @cached_property
    def remediation_types(self) -> AsyncRemediationTypesResourceWithStreamingResponse:
        return AsyncRemediationTypesResourceWithStreamingResponse(self._finding_types.remediation_types)
