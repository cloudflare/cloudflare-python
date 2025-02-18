# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from datetime import datetime
from typing_extensions import Literal

import httpx

from ......_types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ......_utils import maybe_transform
from ......_compat import cached_property
from ......_resource import SyncAPIResource, AsyncAPIResource
from ......_response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ......pagination import SyncSinglePage, AsyncSinglePage
from ......_base_client import AsyncPaginator, make_request_options
from ......types.zero_trust.access.logs.scim import update_list_params
from ......types.zero_trust.access.logs.scim.update_list_response import UpdateListResponse

__all__ = ["UpdatesResource", "AsyncUpdatesResource"]


class UpdatesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> UpdatesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return UpdatesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> UpdatesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return UpdatesResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        account_id: str,
        idp_id: List[str],
        cf_resource_id: str | NotGiven = NOT_GIVEN,
        direction: Literal["desc", "asc"] | NotGiven = NOT_GIVEN,
        idp_resource_id: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        request_method: List[Literal["DELETE", "PATCH", "POST", "PUT"]] | NotGiven = NOT_GIVEN,
        resource_group_name: str | NotGiven = NOT_GIVEN,
        resource_type: List[Literal["USER", "GROUP"]] | NotGiven = NOT_GIVEN,
        resource_user_email: str | NotGiven = NOT_GIVEN,
        since: Union[str, datetime] | NotGiven = NOT_GIVEN,
        status: List[Literal["FAILURE", "SUCCESS"]] | NotGiven = NOT_GIVEN,
        until: Union[str, datetime] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncSinglePage[UpdateListResponse]:
        """
        Lists Access SCIM update logs that maintain a record of updates made to User and
        Group resources synced to Cloudflare via the System for Cross-domain Identity
        Management (SCIM).

        Args:
          account_id: Identifier

          idp_id: The unique Id of the IdP that has SCIM enabled.

          cf_resource_id: The unique Cloudflare-generated Id of the SCIM resource.

          direction: The chronological order used to sort the logs.

          idp_resource_id: The IdP-generated Id of the SCIM resource.

          limit: The maximum number of update logs to retrieve.

          request_method: The request method of the SCIM request.

          resource_group_name: The display name of the SCIM Group resource.

          resource_type: The resource type of the SCIM request.

          resource_user_email: The email address of the SCIM User resource.

          since: the timestamp of the earliest update log.

          status: The status of the SCIM request.

          until: the timestamp of the most-recent update log.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/access/logs/scim/updates",
            page=SyncSinglePage[UpdateListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "idp_id": idp_id,
                        "cf_resource_id": cf_resource_id,
                        "direction": direction,
                        "idp_resource_id": idp_resource_id,
                        "limit": limit,
                        "request_method": request_method,
                        "resource_group_name": resource_group_name,
                        "resource_type": resource_type,
                        "resource_user_email": resource_user_email,
                        "since": since,
                        "status": status,
                        "until": until,
                    },
                    update_list_params.UpdateListParams,
                ),
            ),
            model=UpdateListResponse,
        )


class AsyncUpdatesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncUpdatesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncUpdatesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncUpdatesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncUpdatesResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        account_id: str,
        idp_id: List[str],
        cf_resource_id: str | NotGiven = NOT_GIVEN,
        direction: Literal["desc", "asc"] | NotGiven = NOT_GIVEN,
        idp_resource_id: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        request_method: List[Literal["DELETE", "PATCH", "POST", "PUT"]] | NotGiven = NOT_GIVEN,
        resource_group_name: str | NotGiven = NOT_GIVEN,
        resource_type: List[Literal["USER", "GROUP"]] | NotGiven = NOT_GIVEN,
        resource_user_email: str | NotGiven = NOT_GIVEN,
        since: Union[str, datetime] | NotGiven = NOT_GIVEN,
        status: List[Literal["FAILURE", "SUCCESS"]] | NotGiven = NOT_GIVEN,
        until: Union[str, datetime] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[UpdateListResponse, AsyncSinglePage[UpdateListResponse]]:
        """
        Lists Access SCIM update logs that maintain a record of updates made to User and
        Group resources synced to Cloudflare via the System for Cross-domain Identity
        Management (SCIM).

        Args:
          account_id: Identifier

          idp_id: The unique Id of the IdP that has SCIM enabled.

          cf_resource_id: The unique Cloudflare-generated Id of the SCIM resource.

          direction: The chronological order used to sort the logs.

          idp_resource_id: The IdP-generated Id of the SCIM resource.

          limit: The maximum number of update logs to retrieve.

          request_method: The request method of the SCIM request.

          resource_group_name: The display name of the SCIM Group resource.

          resource_type: The resource type of the SCIM request.

          resource_user_email: The email address of the SCIM User resource.

          since: the timestamp of the earliest update log.

          status: The status of the SCIM request.

          until: the timestamp of the most-recent update log.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/access/logs/scim/updates",
            page=AsyncSinglePage[UpdateListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "idp_id": idp_id,
                        "cf_resource_id": cf_resource_id,
                        "direction": direction,
                        "idp_resource_id": idp_resource_id,
                        "limit": limit,
                        "request_method": request_method,
                        "resource_group_name": resource_group_name,
                        "resource_type": resource_type,
                        "resource_user_email": resource_user_email,
                        "since": since,
                        "status": status,
                        "until": until,
                    },
                    update_list_params.UpdateListParams,
                ),
            ),
            model=UpdateListResponse,
        )


class UpdatesResourceWithRawResponse:
    def __init__(self, updates: UpdatesResource) -> None:
        self._updates = updates

        self.list = to_raw_response_wrapper(
            updates.list,
        )


class AsyncUpdatesResourceWithRawResponse:
    def __init__(self, updates: AsyncUpdatesResource) -> None:
        self._updates = updates

        self.list = async_to_raw_response_wrapper(
            updates.list,
        )


class UpdatesResourceWithStreamingResponse:
    def __init__(self, updates: UpdatesResource) -> None:
        self._updates = updates

        self.list = to_streamed_response_wrapper(
            updates.list,
        )


class AsyncUpdatesResourceWithStreamingResponse:
    def __init__(self, updates: AsyncUpdatesResource) -> None:
        self._updates = updates

        self.list = async_to_streamed_response_wrapper(
            updates.list,
        )
