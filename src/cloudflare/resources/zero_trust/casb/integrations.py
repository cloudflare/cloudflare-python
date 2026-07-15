# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Optional
from typing_extensions import Literal

import httpx

from ...._types import Body, Omit, Query, Headers, NoneType, NotGiven, SequenceNotStr, omit, not_given
from ...._utils import path_template, maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.zero_trust.casb import integration_list_params, integration_create_params, integration_update_params
from ....types.zero_trust.casb.integration_get_response import IntegrationGetResponse
from ....types.zero_trust.casb.integration_pause_response import IntegrationPauseResponse
from ....types.zero_trust.casb.integration_create_response import IntegrationCreateResponse
from ....types.zero_trust.casb.integration_resume_response import IntegrationResumeResponse
from ....types.zero_trust.casb.integration_update_response import IntegrationUpdateResponse

__all__ = ["IntegrationsResource", "AsyncIntegrationsResource"]


class IntegrationsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> IntegrationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return IntegrationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> IntegrationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return IntegrationsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        account_id: str,
        application: Literal[
            "BITBUCKET",
            "BOX",
            "CONFLUENCE",
            "DROPBOX",
            "GITHUB",
            "GOOGLE_WORKSPACE",
            "JIRA",
            "MICROSOFT_INTERNAL",
            "SALESFORCE",
            "SLACK",
        ],
        credentials: Dict[str, object],
        name: str,
        auth_method: Optional[str] | Omit = omit,
        dlp_profiles: SequenceNotStr[str] | Omit = omit,
        permissions: SequenceNotStr[str] | Omit = omit,
        use_cases: List[Literal["casb", "ces", "auto_remediation"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IntegrationCreateResponse:
        """Creates a new integration for the specified application.

        Integration creation
        with OAuth is not supported by API at the moment. For other auth methods, use
        `GET /v2/applications/{application_id}/credential-guide` to see the required
        credential structure and example payloads for each vendor.

        Args:
          application: Vendor/application slug (e.g., GOOGLE_WORKSPACE).

              - `BITBUCKET` - BITBUCKET
              - `BOX` - BOX
              - `CONFLUENCE` - CONFLUENCE
              - `DROPBOX` - DROPBOX
              - `GITHUB` - GITHUB
              - `GOOGLE_WORKSPACE` - GOOGLE_WORKSPACE
              - `JIRA` - JIRA
              - `MICROSOFT_INTERNAL` - MICROSOFT_INTERNAL
              - `SALESFORCE` - SALESFORCE
              - `SLACK` - SLACK

          credentials: Credentials for the integration.

          name: Name of the integration.

          auth_method: Authentication method slug (uses default if omitted).

          dlp_profiles: List of DLP profile IDs to associate.

          permissions: List of permission scopes (uses policy defaults if empty).

          use_cases: List of use case or feature slugs to enroll (e.g., ['casb', 'ces',
              'auto_remediation']).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._post(
            path_template("/accounts/{account_id}/one/integrations", account_id=account_id),
            body=maybe_transform(
                {
                    "application": application,
                    "credentials": credentials,
                    "name": name,
                    "auth_method": auth_method,
                    "dlp_profiles": dlp_profiles,
                    "permissions": permissions,
                    "use_cases": use_cases,
                },
                integration_create_params.IntegrationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IntegrationCreateResponse,
        )

    def update(
        self,
        id: str,
        *,
        account_id: str,
        credentials: Dict[str, object] | Omit = omit,
        dlp_profiles: SequenceNotStr[str] | Omit = omit,
        name: str | Omit = omit,
        permissions: SequenceNotStr[str] | Omit = omit,
        use_cases: List[Literal["casb", "ces", "auto_remediation"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IntegrationUpdateResponse:
        """
        Updates an integration's name, permissions, DLP profiles, use cases, or
        credentials.

        Args:
          credentials: Partial credential fields to merge with existing.

          dlp_profiles: List of DLP profile IDs to associate with the integration.

          name: Name of the integration.

          permissions: List of permission scopes granted to the integration.

          use_cases: List of use case or feature slugs to enroll (e.g., ['casb', 'ces',
              'auto_remediation']).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            path_template("/accounts/{account_id}/one/integrations/{id}", account_id=account_id, id=id),
            body=maybe_transform(
                {
                    "credentials": credentials,
                    "dlp_profiles": dlp_profiles,
                    "name": name,
                    "permissions": permissions,
                    "use_cases": use_cases,
                },
                integration_update_params.IntegrationUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IntegrationUpdateResponse,
        )

    def list(
        self,
        *,
        account_id: str,
        application: str | Omit = omit,
        direction: Literal["asc", "desc"] | Omit = omit,
        dlp_enabled: bool | Omit = omit,
        order: Literal["application", "created", "name", "status"] | Omit = omit,
        page: int | Omit = omit,
        page_size: int | Omit = omit,
        search: str | Omit = omit,
        status: Literal["Healthy", "Initializing", "Offline", "Unhealthy"] | Omit = omit,
        use_cases: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Returns a paginated list of integrations for the account.

        Args:
          application: Filter by application/vendor (e.g., GOOGLE_WORKSPACE, MICROSOFT_INTERNAL).

          direction: Direction to order results.

          dlp_enabled: Filter by DLP enabled status (true/false).

          order: Field to order results by.

          page: Page number within the paginated result set.

          page_size: Number of results per page.

          search: Search integrations by name or application.

          status: Filter by integration status.

          use_cases: Filter by enabled use cases (e.g., casb, ces). Matches integrations enrolled in
              any of the specified values. Can be specified multiple times.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get(
            path_template("/accounts/{account_id}/one/integrations", account_id=account_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "application": application,
                        "direction": direction,
                        "dlp_enabled": dlp_enabled,
                        "order": order,
                        "page": page,
                        "page_size": page_size,
                        "search": search,
                        "status": status,
                        "use_cases": use_cases,
                    },
                    integration_list_params.IntegrationListParams,
                ),
            ),
            cast_to=object,
        )

    def delete(
        self,
        id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete an integration by soft-deleting it.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/accounts/{account_id}/one/integrations/{id}", account_id=account_id, id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def get(
        self,
        id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IntegrationGetResponse:
        """
        Returns full integration details including use cases and permissions.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/accounts/{account_id}/one/integrations/{id}", account_id=account_id, id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IntegrationGetResponse,
        )

    def pause(
        self,
        id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IntegrationPauseResponse:
        """
        Pauses an integration, stopping all crawlers.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            path_template("/accounts/{account_id}/one/integrations/{id}/pause", account_id=account_id, id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IntegrationPauseResponse,
        )

    def resume(
        self,
        id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IntegrationResumeResponse:
        """
        Resumes a paused integration, restarting crawlers.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            path_template("/accounts/{account_id}/one/integrations/{id}/resume", account_id=account_id, id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IntegrationResumeResponse,
        )


class AsyncIntegrationsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncIntegrationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncIntegrationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncIntegrationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncIntegrationsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_id: str,
        application: Literal[
            "BITBUCKET",
            "BOX",
            "CONFLUENCE",
            "DROPBOX",
            "GITHUB",
            "GOOGLE_WORKSPACE",
            "JIRA",
            "MICROSOFT_INTERNAL",
            "SALESFORCE",
            "SLACK",
        ],
        credentials: Dict[str, object],
        name: str,
        auth_method: Optional[str] | Omit = omit,
        dlp_profiles: SequenceNotStr[str] | Omit = omit,
        permissions: SequenceNotStr[str] | Omit = omit,
        use_cases: List[Literal["casb", "ces", "auto_remediation"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IntegrationCreateResponse:
        """Creates a new integration for the specified application.

        Integration creation
        with OAuth is not supported by API at the moment. For other auth methods, use
        `GET /v2/applications/{application_id}/credential-guide` to see the required
        credential structure and example payloads for each vendor.

        Args:
          application: Vendor/application slug (e.g., GOOGLE_WORKSPACE).

              - `BITBUCKET` - BITBUCKET
              - `BOX` - BOX
              - `CONFLUENCE` - CONFLUENCE
              - `DROPBOX` - DROPBOX
              - `GITHUB` - GITHUB
              - `GOOGLE_WORKSPACE` - GOOGLE_WORKSPACE
              - `JIRA` - JIRA
              - `MICROSOFT_INTERNAL` - MICROSOFT_INTERNAL
              - `SALESFORCE` - SALESFORCE
              - `SLACK` - SLACK

          credentials: Credentials for the integration.

          name: Name of the integration.

          auth_method: Authentication method slug (uses default if omitted).

          dlp_profiles: List of DLP profile IDs to associate.

          permissions: List of permission scopes (uses policy defaults if empty).

          use_cases: List of use case or feature slugs to enroll (e.g., ['casb', 'ces',
              'auto_remediation']).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._post(
            path_template("/accounts/{account_id}/one/integrations", account_id=account_id),
            body=await async_maybe_transform(
                {
                    "application": application,
                    "credentials": credentials,
                    "name": name,
                    "auth_method": auth_method,
                    "dlp_profiles": dlp_profiles,
                    "permissions": permissions,
                    "use_cases": use_cases,
                },
                integration_create_params.IntegrationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IntegrationCreateResponse,
        )

    async def update(
        self,
        id: str,
        *,
        account_id: str,
        credentials: Dict[str, object] | Omit = omit,
        dlp_profiles: SequenceNotStr[str] | Omit = omit,
        name: str | Omit = omit,
        permissions: SequenceNotStr[str] | Omit = omit,
        use_cases: List[Literal["casb", "ces", "auto_remediation"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IntegrationUpdateResponse:
        """
        Updates an integration's name, permissions, DLP profiles, use cases, or
        credentials.

        Args:
          credentials: Partial credential fields to merge with existing.

          dlp_profiles: List of DLP profile IDs to associate with the integration.

          name: Name of the integration.

          permissions: List of permission scopes granted to the integration.

          use_cases: List of use case or feature slugs to enroll (e.g., ['casb', 'ces',
              'auto_remediation']).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            path_template("/accounts/{account_id}/one/integrations/{id}", account_id=account_id, id=id),
            body=await async_maybe_transform(
                {
                    "credentials": credentials,
                    "dlp_profiles": dlp_profiles,
                    "name": name,
                    "permissions": permissions,
                    "use_cases": use_cases,
                },
                integration_update_params.IntegrationUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IntegrationUpdateResponse,
        )

    async def list(
        self,
        *,
        account_id: str,
        application: str | Omit = omit,
        direction: Literal["asc", "desc"] | Omit = omit,
        dlp_enabled: bool | Omit = omit,
        order: Literal["application", "created", "name", "status"] | Omit = omit,
        page: int | Omit = omit,
        page_size: int | Omit = omit,
        search: str | Omit = omit,
        status: Literal["Healthy", "Initializing", "Offline", "Unhealthy"] | Omit = omit,
        use_cases: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Returns a paginated list of integrations for the account.

        Args:
          application: Filter by application/vendor (e.g., GOOGLE_WORKSPACE, MICROSOFT_INTERNAL).

          direction: Direction to order results.

          dlp_enabled: Filter by DLP enabled status (true/false).

          order: Field to order results by.

          page: Page number within the paginated result set.

          page_size: Number of results per page.

          search: Search integrations by name or application.

          status: Filter by integration status.

          use_cases: Filter by enabled use cases (e.g., casb, ces). Matches integrations enrolled in
              any of the specified values. Can be specified multiple times.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._get(
            path_template("/accounts/{account_id}/one/integrations", account_id=account_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "application": application,
                        "direction": direction,
                        "dlp_enabled": dlp_enabled,
                        "order": order,
                        "page": page,
                        "page_size": page_size,
                        "search": search,
                        "status": status,
                        "use_cases": use_cases,
                    },
                    integration_list_params.IntegrationListParams,
                ),
            ),
            cast_to=object,
        )

    async def delete(
        self,
        id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete an integration by soft-deleting it.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/accounts/{account_id}/one/integrations/{id}", account_id=account_id, id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def get(
        self,
        id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IntegrationGetResponse:
        """
        Returns full integration details including use cases and permissions.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/accounts/{account_id}/one/integrations/{id}", account_id=account_id, id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IntegrationGetResponse,
        )

    async def pause(
        self,
        id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IntegrationPauseResponse:
        """
        Pauses an integration, stopping all crawlers.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            path_template("/accounts/{account_id}/one/integrations/{id}/pause", account_id=account_id, id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IntegrationPauseResponse,
        )

    async def resume(
        self,
        id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IntegrationResumeResponse:
        """
        Resumes a paused integration, restarting crawlers.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            path_template("/accounts/{account_id}/one/integrations/{id}/resume", account_id=account_id, id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IntegrationResumeResponse,
        )


class IntegrationsResourceWithRawResponse:
    def __init__(self, integrations: IntegrationsResource) -> None:
        self._integrations = integrations

        self.create = to_raw_response_wrapper(
            integrations.create,
        )
        self.update = to_raw_response_wrapper(
            integrations.update,
        )
        self.list = to_raw_response_wrapper(
            integrations.list,
        )
        self.delete = to_raw_response_wrapper(
            integrations.delete,
        )
        self.get = to_raw_response_wrapper(
            integrations.get,
        )
        self.pause = to_raw_response_wrapper(
            integrations.pause,
        )
        self.resume = to_raw_response_wrapper(
            integrations.resume,
        )


class AsyncIntegrationsResourceWithRawResponse:
    def __init__(self, integrations: AsyncIntegrationsResource) -> None:
        self._integrations = integrations

        self.create = async_to_raw_response_wrapper(
            integrations.create,
        )
        self.update = async_to_raw_response_wrapper(
            integrations.update,
        )
        self.list = async_to_raw_response_wrapper(
            integrations.list,
        )
        self.delete = async_to_raw_response_wrapper(
            integrations.delete,
        )
        self.get = async_to_raw_response_wrapper(
            integrations.get,
        )
        self.pause = async_to_raw_response_wrapper(
            integrations.pause,
        )
        self.resume = async_to_raw_response_wrapper(
            integrations.resume,
        )


class IntegrationsResourceWithStreamingResponse:
    def __init__(self, integrations: IntegrationsResource) -> None:
        self._integrations = integrations

        self.create = to_streamed_response_wrapper(
            integrations.create,
        )
        self.update = to_streamed_response_wrapper(
            integrations.update,
        )
        self.list = to_streamed_response_wrapper(
            integrations.list,
        )
        self.delete = to_streamed_response_wrapper(
            integrations.delete,
        )
        self.get = to_streamed_response_wrapper(
            integrations.get,
        )
        self.pause = to_streamed_response_wrapper(
            integrations.pause,
        )
        self.resume = to_streamed_response_wrapper(
            integrations.resume,
        )


class AsyncIntegrationsResourceWithStreamingResponse:
    def __init__(self, integrations: AsyncIntegrationsResource) -> None:
        self._integrations = integrations

        self.create = async_to_streamed_response_wrapper(
            integrations.create,
        )
        self.update = async_to_streamed_response_wrapper(
            integrations.update,
        )
        self.list = async_to_streamed_response_wrapper(
            integrations.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            integrations.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            integrations.get,
        )
        self.pause = async_to_streamed_response_wrapper(
            integrations.pause,
        )
        self.resume = async_to_streamed_response_wrapper(
            integrations.resume,
        )
