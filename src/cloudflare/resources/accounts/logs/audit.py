# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date
from typing_extensions import Literal

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....pagination import SyncCursorLimitPagination, AsyncCursorLimitPagination
from ...._base_client import AsyncPaginator, make_request_options
from ....types.accounts.logs import audit_list_params
from ....types.accounts.logs.audit_list_response import AuditListResponse

__all__ = ["AuditResource", "AsyncAuditResource"]


class AuditResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AuditResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AuditResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AuditResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AuditResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        account_id: str,
        before: Union[str, date],
        since: Union[str, date],
        account_name: str | NotGiven = NOT_GIVEN,
        action_result: Literal["success", "failure"] | NotGiven = NOT_GIVEN,
        action_type: Literal["create", "delete", "view", "update"] | NotGiven = NOT_GIVEN,
        actor_context: Literal["api_key", "api_token", "dash", "oauth", "origin_ca_key"] | NotGiven = NOT_GIVEN,
        actor_email: str | NotGiven = NOT_GIVEN,
        actor_id: str | NotGiven = NOT_GIVEN,
        actor_ip_address: str | NotGiven = NOT_GIVEN,
        actor_token_id: str | NotGiven = NOT_GIVEN,
        actor_token_name: str | NotGiven = NOT_GIVEN,
        actor_type: Literal["cloudflare_admin", "account", "user"] | NotGiven = NOT_GIVEN,
        audit_log_id: str | NotGiven = NOT_GIVEN,
        cursor: str | NotGiven = NOT_GIVEN,
        direction: Literal["desc", "asc"] | NotGiven = NOT_GIVEN,
        limit: float | NotGiven = NOT_GIVEN,
        raw_cf_rayid: str | NotGiven = NOT_GIVEN,
        raw_method: str | NotGiven = NOT_GIVEN,
        raw_status_code: int | NotGiven = NOT_GIVEN,
        raw_uri: str | NotGiven = NOT_GIVEN,
        resource_id: str | NotGiven = NOT_GIVEN,
        resource_product: str | NotGiven = NOT_GIVEN,
        resource_scope: Literal["accounts", "user", "zones"] | NotGiven = NOT_GIVEN,
        resource_type: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        zone_name: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncCursorLimitPagination[AuditListResponse]:
        """Gets a list of audit logs for an account.

        <br /> <br /> This is the beta release
        of Audit Logs Version 2. Since this is a beta version, there may be gaps or
        missing entries in the available audit logs. Be aware of the following
        limitations. <br /> <ul> <li>Audit logs are available only for the past 30 days.
        <br /></li> <li>Error handling is not yet implemented. <br /> </li> </ul>

        Args:
          account_id: The unique id that identifies the account.

          before: Filters actions based on a given timestamp in the format yyyy-mm-dd, returning
              only logs that occurred on and before the specified date.

          since: Filters actions based on a given timestamp in the format yyyy-mm-dd, returning
              only logs that occurred on and after the specified date.

          account_name: Filters by the account name.

          action_result: Whether the action was successful or not.

          action_type: Filters by the action type.

          actor_context: Filters by the actor context.

          actor_email: Filters by the actor's email address.

          actor_id: Filters by the actor ID. This can be either the Account ID or User ID.

          actor_ip_address: The IP address where the action was initiated.

          actor_token_id: Filters by the API token ID when the actor context is an api_token or oauth.

          actor_token_name: Filters by the API token name when the actor context is an api_token or oauth.

          actor_type: Filters by the actor type.

          audit_log_id: Finds a specific log by its ID.

          cursor: The cursor is an opaque token used to paginate through large sets of records. It
              indicates the position from which to continue when requesting the next set of
              records. A valid cursor value can be obtained from the cursor object in the
              result_info structure of a previous response.

          direction: Sets sorting order.

          limit: The number limits the objects to return. The cursor attribute may be used to
              iterate over the next batch of objects if there are more than the limit.

          raw_cf_rayid: Filters by the response CF Ray ID.

          raw_method: The HTTP method for the API call.

          raw_status_code: The response status code that was returned.

          raw_uri: Filters by the request URI.

          resource_id: Filters by the resource ID.

          resource_product: Filters audit logs by the Cloudflare product associated with the changed
              resource.

          resource_scope: Filters by the resource scope, specifying whether the resource is associated
              with an user, an account, or a zone.

          resource_type: Filters audit logs based on the unique type of resource changed by the action.

          zone_id: Filters by the zone ID.

          zone_name: Filters by the zone name associated with the change.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/logs/audit",
            page=SyncCursorLimitPagination[AuditListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "before": before,
                        "since": since,
                        "account_name": account_name,
                        "action_result": action_result,
                        "action_type": action_type,
                        "actor_context": actor_context,
                        "actor_email": actor_email,
                        "actor_id": actor_id,
                        "actor_ip_address": actor_ip_address,
                        "actor_token_id": actor_token_id,
                        "actor_token_name": actor_token_name,
                        "actor_type": actor_type,
                        "audit_log_id": audit_log_id,
                        "cursor": cursor,
                        "direction": direction,
                        "limit": limit,
                        "raw_cf_rayid": raw_cf_rayid,
                        "raw_method": raw_method,
                        "raw_status_code": raw_status_code,
                        "raw_uri": raw_uri,
                        "resource_id": resource_id,
                        "resource_product": resource_product,
                        "resource_scope": resource_scope,
                        "resource_type": resource_type,
                        "zone_id": zone_id,
                        "zone_name": zone_name,
                    },
                    audit_list_params.AuditListParams,
                ),
            ),
            model=AuditListResponse,
        )


class AsyncAuditResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAuditResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAuditResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAuditResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncAuditResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        account_id: str,
        before: Union[str, date],
        since: Union[str, date],
        account_name: str | NotGiven = NOT_GIVEN,
        action_result: Literal["success", "failure"] | NotGiven = NOT_GIVEN,
        action_type: Literal["create", "delete", "view", "update"] | NotGiven = NOT_GIVEN,
        actor_context: Literal["api_key", "api_token", "dash", "oauth", "origin_ca_key"] | NotGiven = NOT_GIVEN,
        actor_email: str | NotGiven = NOT_GIVEN,
        actor_id: str | NotGiven = NOT_GIVEN,
        actor_ip_address: str | NotGiven = NOT_GIVEN,
        actor_token_id: str | NotGiven = NOT_GIVEN,
        actor_token_name: str | NotGiven = NOT_GIVEN,
        actor_type: Literal["cloudflare_admin", "account", "user"] | NotGiven = NOT_GIVEN,
        audit_log_id: str | NotGiven = NOT_GIVEN,
        cursor: str | NotGiven = NOT_GIVEN,
        direction: Literal["desc", "asc"] | NotGiven = NOT_GIVEN,
        limit: float | NotGiven = NOT_GIVEN,
        raw_cf_rayid: str | NotGiven = NOT_GIVEN,
        raw_method: str | NotGiven = NOT_GIVEN,
        raw_status_code: int | NotGiven = NOT_GIVEN,
        raw_uri: str | NotGiven = NOT_GIVEN,
        resource_id: str | NotGiven = NOT_GIVEN,
        resource_product: str | NotGiven = NOT_GIVEN,
        resource_scope: Literal["accounts", "user", "zones"] | NotGiven = NOT_GIVEN,
        resource_type: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        zone_name: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[AuditListResponse, AsyncCursorLimitPagination[AuditListResponse]]:
        """Gets a list of audit logs for an account.

        <br /> <br /> This is the beta release
        of Audit Logs Version 2. Since this is a beta version, there may be gaps or
        missing entries in the available audit logs. Be aware of the following
        limitations. <br /> <ul> <li>Audit logs are available only for the past 30 days.
        <br /></li> <li>Error handling is not yet implemented. <br /> </li> </ul>

        Args:
          account_id: The unique id that identifies the account.

          before: Filters actions based on a given timestamp in the format yyyy-mm-dd, returning
              only logs that occurred on and before the specified date.

          since: Filters actions based on a given timestamp in the format yyyy-mm-dd, returning
              only logs that occurred on and after the specified date.

          account_name: Filters by the account name.

          action_result: Whether the action was successful or not.

          action_type: Filters by the action type.

          actor_context: Filters by the actor context.

          actor_email: Filters by the actor's email address.

          actor_id: Filters by the actor ID. This can be either the Account ID or User ID.

          actor_ip_address: The IP address where the action was initiated.

          actor_token_id: Filters by the API token ID when the actor context is an api_token or oauth.

          actor_token_name: Filters by the API token name when the actor context is an api_token or oauth.

          actor_type: Filters by the actor type.

          audit_log_id: Finds a specific log by its ID.

          cursor: The cursor is an opaque token used to paginate through large sets of records. It
              indicates the position from which to continue when requesting the next set of
              records. A valid cursor value can be obtained from the cursor object in the
              result_info structure of a previous response.

          direction: Sets sorting order.

          limit: The number limits the objects to return. The cursor attribute may be used to
              iterate over the next batch of objects if there are more than the limit.

          raw_cf_rayid: Filters by the response CF Ray ID.

          raw_method: The HTTP method for the API call.

          raw_status_code: The response status code that was returned.

          raw_uri: Filters by the request URI.

          resource_id: Filters by the resource ID.

          resource_product: Filters audit logs by the Cloudflare product associated with the changed
              resource.

          resource_scope: Filters by the resource scope, specifying whether the resource is associated
              with an user, an account, or a zone.

          resource_type: Filters audit logs based on the unique type of resource changed by the action.

          zone_id: Filters by the zone ID.

          zone_name: Filters by the zone name associated with the change.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/logs/audit",
            page=AsyncCursorLimitPagination[AuditListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "before": before,
                        "since": since,
                        "account_name": account_name,
                        "action_result": action_result,
                        "action_type": action_type,
                        "actor_context": actor_context,
                        "actor_email": actor_email,
                        "actor_id": actor_id,
                        "actor_ip_address": actor_ip_address,
                        "actor_token_id": actor_token_id,
                        "actor_token_name": actor_token_name,
                        "actor_type": actor_type,
                        "audit_log_id": audit_log_id,
                        "cursor": cursor,
                        "direction": direction,
                        "limit": limit,
                        "raw_cf_rayid": raw_cf_rayid,
                        "raw_method": raw_method,
                        "raw_status_code": raw_status_code,
                        "raw_uri": raw_uri,
                        "resource_id": resource_id,
                        "resource_product": resource_product,
                        "resource_scope": resource_scope,
                        "resource_type": resource_type,
                        "zone_id": zone_id,
                        "zone_name": zone_name,
                    },
                    audit_list_params.AuditListParams,
                ),
            ),
            model=AuditListResponse,
        )


class AuditResourceWithRawResponse:
    def __init__(self, audit: AuditResource) -> None:
        self._audit = audit

        self.list = to_raw_response_wrapper(
            audit.list,
        )


class AsyncAuditResourceWithRawResponse:
    def __init__(self, audit: AsyncAuditResource) -> None:
        self._audit = audit

        self.list = async_to_raw_response_wrapper(
            audit.list,
        )


class AuditResourceWithStreamingResponse:
    def __init__(self, audit: AuditResource) -> None:
        self._audit = audit

        self.list = to_streamed_response_wrapper(
            audit.list,
        )


class AsyncAuditResourceWithStreamingResponse:
    def __init__(self, audit: AsyncAuditResource) -> None:
        self._audit = audit

        self.list = async_to_streamed_response_wrapper(
            audit.list,
        )
