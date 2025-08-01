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
        account_name: audit_list_params.AccountName | NotGiven = NOT_GIVEN,
        action_result: audit_list_params.ActionResult | NotGiven = NOT_GIVEN,
        action_type: audit_list_params.ActionType | NotGiven = NOT_GIVEN,
        actor_context: audit_list_params.ActorContext | NotGiven = NOT_GIVEN,
        actor_email: audit_list_params.ActorEmail | NotGiven = NOT_GIVEN,
        actor_id: audit_list_params.ActorID | NotGiven = NOT_GIVEN,
        actor_ip_address: audit_list_params.ActorIPAddress | NotGiven = NOT_GIVEN,
        actor_token_id: audit_list_params.ActorTokenID | NotGiven = NOT_GIVEN,
        actor_token_name: audit_list_params.ActorTokenName | NotGiven = NOT_GIVEN,
        actor_type: audit_list_params.ActorType | NotGiven = NOT_GIVEN,
        audit_log_id: audit_list_params.AuditLogID | NotGiven = NOT_GIVEN,
        cursor: str | NotGiven = NOT_GIVEN,
        direction: Literal["desc", "asc"] | NotGiven = NOT_GIVEN,
        limit: float | NotGiven = NOT_GIVEN,
        raw_cf_rayid: audit_list_params.RawCfRayID | NotGiven = NOT_GIVEN,
        raw_method: audit_list_params.RawMethod | NotGiven = NOT_GIVEN,
        raw_status_code: audit_list_params.RawStatusCode | NotGiven = NOT_GIVEN,
        raw_uri: audit_list_params.RawURI | NotGiven = NOT_GIVEN,
        resource_id: audit_list_params.ResourceID | NotGiven = NOT_GIVEN,
        resource_product: audit_list_params.ResourceProduct | NotGiven = NOT_GIVEN,
        resource_scope: audit_list_params.ResourceScope | NotGiven = NOT_GIVEN,
        resource_type: audit_list_params.ResourceType | NotGiven = NOT_GIVEN,
        zone_id: audit_list_params.ZoneID | NotGiven = NOT_GIVEN,
        zone_name: audit_list_params.ZoneName | NotGiven = NOT_GIVEN,
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

          before: Limits the returned results to logs older than the specified date. This can be a
              date string 2019-04-30 (interpreted in UTC) or an absolute timestamp that
              conforms to RFC3339.

          since: Limits the returned results to logs newer than the specified date. This can be a
              date string 2019-04-30 (interpreted in UTC) or an absolute timestamp that
              conforms to RFC3339.

          cursor: The cursor is an opaque token used to paginate through large sets of records. It
              indicates the position from which to continue when requesting the next set of
              records. A valid cursor value can be obtained from the cursor object in the
              result_info structure of a previous response.

          direction: Sets sorting order.

          limit: The number limits the objects to return. The cursor attribute may be used to
              iterate over the next batch of objects if there are more than the limit.

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
        account_name: audit_list_params.AccountName | NotGiven = NOT_GIVEN,
        action_result: audit_list_params.ActionResult | NotGiven = NOT_GIVEN,
        action_type: audit_list_params.ActionType | NotGiven = NOT_GIVEN,
        actor_context: audit_list_params.ActorContext | NotGiven = NOT_GIVEN,
        actor_email: audit_list_params.ActorEmail | NotGiven = NOT_GIVEN,
        actor_id: audit_list_params.ActorID | NotGiven = NOT_GIVEN,
        actor_ip_address: audit_list_params.ActorIPAddress | NotGiven = NOT_GIVEN,
        actor_token_id: audit_list_params.ActorTokenID | NotGiven = NOT_GIVEN,
        actor_token_name: audit_list_params.ActorTokenName | NotGiven = NOT_GIVEN,
        actor_type: audit_list_params.ActorType | NotGiven = NOT_GIVEN,
        audit_log_id: audit_list_params.AuditLogID | NotGiven = NOT_GIVEN,
        cursor: str | NotGiven = NOT_GIVEN,
        direction: Literal["desc", "asc"] | NotGiven = NOT_GIVEN,
        limit: float | NotGiven = NOT_GIVEN,
        raw_cf_rayid: audit_list_params.RawCfRayID | NotGiven = NOT_GIVEN,
        raw_method: audit_list_params.RawMethod | NotGiven = NOT_GIVEN,
        raw_status_code: audit_list_params.RawStatusCode | NotGiven = NOT_GIVEN,
        raw_uri: audit_list_params.RawURI | NotGiven = NOT_GIVEN,
        resource_id: audit_list_params.ResourceID | NotGiven = NOT_GIVEN,
        resource_product: audit_list_params.ResourceProduct | NotGiven = NOT_GIVEN,
        resource_scope: audit_list_params.ResourceScope | NotGiven = NOT_GIVEN,
        resource_type: audit_list_params.ResourceType | NotGiven = NOT_GIVEN,
        zone_id: audit_list_params.ZoneID | NotGiven = NOT_GIVEN,
        zone_name: audit_list_params.ZoneName | NotGiven = NOT_GIVEN,
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

          before: Limits the returned results to logs older than the specified date. This can be a
              date string 2019-04-30 (interpreted in UTC) or an absolute timestamp that
              conforms to RFC3339.

          since: Limits the returned results to logs newer than the specified date. This can be a
              date string 2019-04-30 (interpreted in UTC) or an absolute timestamp that
              conforms to RFC3339.

          cursor: The cursor is an opaque token used to paginate through large sets of records. It
              indicates the position from which to continue when requesting the next set of
              records. A valid cursor value can be obtained from the cursor object in the
              result_info structure of a previous response.

          direction: Sets sorting order.

          limit: The number limits the objects to return. The cursor attribute may be used to
              iterate over the next batch of objects if there are more than the limit.

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
