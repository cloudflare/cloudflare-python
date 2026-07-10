# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Union, cast
from datetime import date, datetime
from typing_extensions import Literal

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ...._utils import path_template, maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._wrappers import ResultWrapper
from ....pagination import SyncCursorPaginationAfter, AsyncCursorPaginationAfter
from ...._base_client import AsyncPaginator, make_request_options
from ....types.organizations.logs import audit_list_params, audit_history_params
from ....types.organizations.logs.audit_list_response import AuditListResponse
from ....types.organizations.logs.audit_history_response import AuditHistoryResponse

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
        organization_id: str,
        *,
        before: Union[str, date],
        since: Union[str, date],
        id: audit_list_params.ID | Omit = omit,
        action_result: audit_list_params.ActionResult | Omit = omit,
        action_type: audit_list_params.ActionType | Omit = omit,
        actor_context: audit_list_params.ActorContext | Omit = omit,
        actor_email: audit_list_params.ActorEmail | Omit = omit,
        actor_id: audit_list_params.ActorID | Omit = omit,
        actor_ip_address: audit_list_params.ActorIPAddress | Omit = omit,
        actor_token_id: audit_list_params.ActorTokenID | Omit = omit,
        actor_token_name: audit_list_params.ActorTokenName | Omit = omit,
        actor_type: audit_list_params.ActorType | Omit = omit,
        cursor: str | Omit = omit,
        direction: Literal["desc", "asc"] | Omit = omit,
        limit: float | Omit = omit,
        raw_cf_rayid: audit_list_params.RawCfRayID | Omit = omit,
        raw_method: audit_list_params.RawMethod | Omit = omit,
        raw_status_code: audit_list_params.RawStatusCode | Omit = omit,
        raw_uri: audit_list_params.RawURI | Omit = omit,
        resource_id: audit_list_params.ResourceID | Omit = omit,
        resource_product: audit_list_params.ResourceProduct | Omit = omit,
        resource_scope: audit_list_params.ResourceScope | Omit = omit,
        resource_type: audit_list_params.ResourceType | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorPaginationAfter[AuditListResponse]:
        """
        Gets a list of audit logs for an organization.

        Args:
          organization_id: The unique id that identifies the organization.

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
        if not organization_id:
            raise ValueError(f"Expected a non-empty value for `organization_id` but received {organization_id!r}")
        return self._get_api_list(
            path_template("/organizations/{organization_id}/logs/audit", organization_id=organization_id),
            page=SyncCursorPaginationAfter[AuditListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "before": before,
                        "since": since,
                        "id": id,
                        "action_result": action_result,
                        "action_type": action_type,
                        "actor_context": actor_context,
                        "actor_email": actor_email,
                        "actor_id": actor_id,
                        "actor_ip_address": actor_ip_address,
                        "actor_token_id": actor_token_id,
                        "actor_token_name": actor_token_name,
                        "actor_type": actor_type,
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
                    },
                    audit_list_params.AuditListParams,
                ),
            ),
            model=AuditListResponse,
        )

    def history(
        self,
        id: str,
        *,
        organization_id: str,
        action_time: Union[str, datetime],
        before: Union[str, date],
        since: Union[str, date],
        cursor: str | Omit = omit,
        direction: Literal["desc", "asc"] | Omit = omit,
        limit: float | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AuditHistoryResponse:
        """
        Returns the chronological change history for the resource identified by the
        given organization-scoped audit log entry.

        The endpoint first locates the source audit log entry by `id` (using
        `action_time` to narrow the lookup window), derives identifying filters from
        that entry, and then returns matching audit logs within the `since`/`before`
        window.

        The `result_info.history_status` field indicates the quality of the resource
        identification used:

        - `exact`: Resource was identified by the resource URI.
        - `approximate`: Resource was identified without the resource URI.
        - `unavailable`: The source audit log entry did not contain enough information
          to identify the resource; an empty result is returned.

        Args:
          organization_id: The unique ID that identifies the organization.

          id: The ID of the audit log to fetch resource history for.

          action_time: RFC3339 timestamp of the source audit log entry's action time. Used to narrow
              the source-entry lookup window. Provide the `action.time` value from the audit
              log identified by `id`.

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
        if not organization_id:
            raise ValueError(f"Expected a non-empty value for `organization_id` but received {organization_id!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template(
                "/organizations/{organization_id}/logs/audit/{id}/history", organization_id=organization_id, id=id
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "action_time": action_time,
                        "before": before,
                        "since": since,
                        "cursor": cursor,
                        "direction": direction,
                        "limit": limit,
                    },
                    audit_history_params.AuditHistoryParams,
                ),
                post_parser=ResultWrapper[AuditHistoryResponse]._unwrapper,
            ),
            cast_to=cast(Type[AuditHistoryResponse], ResultWrapper[AuditHistoryResponse]),
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
        organization_id: str,
        *,
        before: Union[str, date],
        since: Union[str, date],
        id: audit_list_params.ID | Omit = omit,
        action_result: audit_list_params.ActionResult | Omit = omit,
        action_type: audit_list_params.ActionType | Omit = omit,
        actor_context: audit_list_params.ActorContext | Omit = omit,
        actor_email: audit_list_params.ActorEmail | Omit = omit,
        actor_id: audit_list_params.ActorID | Omit = omit,
        actor_ip_address: audit_list_params.ActorIPAddress | Omit = omit,
        actor_token_id: audit_list_params.ActorTokenID | Omit = omit,
        actor_token_name: audit_list_params.ActorTokenName | Omit = omit,
        actor_type: audit_list_params.ActorType | Omit = omit,
        cursor: str | Omit = omit,
        direction: Literal["desc", "asc"] | Omit = omit,
        limit: float | Omit = omit,
        raw_cf_rayid: audit_list_params.RawCfRayID | Omit = omit,
        raw_method: audit_list_params.RawMethod | Omit = omit,
        raw_status_code: audit_list_params.RawStatusCode | Omit = omit,
        raw_uri: audit_list_params.RawURI | Omit = omit,
        resource_id: audit_list_params.ResourceID | Omit = omit,
        resource_product: audit_list_params.ResourceProduct | Omit = omit,
        resource_scope: audit_list_params.ResourceScope | Omit = omit,
        resource_type: audit_list_params.ResourceType | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[AuditListResponse, AsyncCursorPaginationAfter[AuditListResponse]]:
        """
        Gets a list of audit logs for an organization.

        Args:
          organization_id: The unique id that identifies the organization.

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
        if not organization_id:
            raise ValueError(f"Expected a non-empty value for `organization_id` but received {organization_id!r}")
        return self._get_api_list(
            path_template("/organizations/{organization_id}/logs/audit", organization_id=organization_id),
            page=AsyncCursorPaginationAfter[AuditListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "before": before,
                        "since": since,
                        "id": id,
                        "action_result": action_result,
                        "action_type": action_type,
                        "actor_context": actor_context,
                        "actor_email": actor_email,
                        "actor_id": actor_id,
                        "actor_ip_address": actor_ip_address,
                        "actor_token_id": actor_token_id,
                        "actor_token_name": actor_token_name,
                        "actor_type": actor_type,
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
                    },
                    audit_list_params.AuditListParams,
                ),
            ),
            model=AuditListResponse,
        )

    async def history(
        self,
        id: str,
        *,
        organization_id: str,
        action_time: Union[str, datetime],
        before: Union[str, date],
        since: Union[str, date],
        cursor: str | Omit = omit,
        direction: Literal["desc", "asc"] | Omit = omit,
        limit: float | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AuditHistoryResponse:
        """
        Returns the chronological change history for the resource identified by the
        given organization-scoped audit log entry.

        The endpoint first locates the source audit log entry by `id` (using
        `action_time` to narrow the lookup window), derives identifying filters from
        that entry, and then returns matching audit logs within the `since`/`before`
        window.

        The `result_info.history_status` field indicates the quality of the resource
        identification used:

        - `exact`: Resource was identified by the resource URI.
        - `approximate`: Resource was identified without the resource URI.
        - `unavailable`: The source audit log entry did not contain enough information
          to identify the resource; an empty result is returned.

        Args:
          organization_id: The unique ID that identifies the organization.

          id: The ID of the audit log to fetch resource history for.

          action_time: RFC3339 timestamp of the source audit log entry's action time. Used to narrow
              the source-entry lookup window. Provide the `action.time` value from the audit
              log identified by `id`.

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
        if not organization_id:
            raise ValueError(f"Expected a non-empty value for `organization_id` but received {organization_id!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template(
                "/organizations/{organization_id}/logs/audit/{id}/history", organization_id=organization_id, id=id
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "action_time": action_time,
                        "before": before,
                        "since": since,
                        "cursor": cursor,
                        "direction": direction,
                        "limit": limit,
                    },
                    audit_history_params.AuditHistoryParams,
                ),
                post_parser=ResultWrapper[AuditHistoryResponse]._unwrapper,
            ),
            cast_to=cast(Type[AuditHistoryResponse], ResultWrapper[AuditHistoryResponse]),
        )


class AuditResourceWithRawResponse:
    def __init__(self, audit: AuditResource) -> None:
        self._audit = audit

        self.list = to_raw_response_wrapper(
            audit.list,
        )
        self.history = to_raw_response_wrapper(
            audit.history,
        )


class AsyncAuditResourceWithRawResponse:
    def __init__(self, audit: AsyncAuditResource) -> None:
        self._audit = audit

        self.list = async_to_raw_response_wrapper(
            audit.list,
        )
        self.history = async_to_raw_response_wrapper(
            audit.history,
        )


class AuditResourceWithStreamingResponse:
    def __init__(self, audit: AuditResource) -> None:
        self._audit = audit

        self.list = to_streamed_response_wrapper(
            audit.list,
        )
        self.history = to_streamed_response_wrapper(
            audit.history,
        )


class AsyncAuditResourceWithStreamingResponse:
    def __init__(self, audit: AsyncAuditResource) -> None:
        self._audit = audit

        self.list = async_to_streamed_response_wrapper(
            audit.list,
        )
        self.history = async_to_streamed_response_wrapper(
            audit.history,
        )
