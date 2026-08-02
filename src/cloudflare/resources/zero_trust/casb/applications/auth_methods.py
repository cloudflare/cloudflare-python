# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ....._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ....._utils import path_template, maybe_transform, async_maybe_transform
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....._base_client import make_request_options
from .....types.zero_trust.casb.applications import auth_method_list_params

__all__ = ["AuthMethodsResource", "AsyncAuthMethodsResource"]


class AuthMethodsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AuthMethodsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AuthMethodsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AuthMethodsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AuthMethodsResourceWithStreamingResponse(self)

    def list(
        self,
        application_id: Literal[
            "ANTHROPIC",
            "AWS",
            "BITBUCKET",
            "BOX",
            "CONFLUENCE",
            "DROPBOX",
            "GITHUB",
            "GITLAB",
            "GOOGLE_CLOUD_PLATFORM",
            "GOOGLE_WORKSPACE",
            "JIRA",
            "MICROSOFT_INTERNAL",
            "OPENAI",
            "SALESFORCE",
            "SERVICENOW",
            "SLACK",
            "ZOOM",
        ],
        *,
        account_id: str,
        page: int | Omit = omit,
        page_size: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Returns available auth methods for the specified vendor, including credential
        schema, instructions, and example payloads. Use this to understand what
        credentials are required before calling POST /v2/integrations.

        Args:
          page: A page number within the paginated result set.

          page_size: Number of results to return per page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not application_id:
            raise ValueError(f"Expected a non-empty value for `application_id` but received {application_id!r}")
        return self._get(
            path_template(
                "/accounts/{account_id}/one/applications/{application_id}/auth-methods",
                account_id=account_id,
                application_id=application_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page": page,
                        "page_size": page_size,
                    },
                    auth_method_list_params.AuthMethodListParams,
                ),
            ),
            cast_to=object,
        )


class AsyncAuthMethodsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAuthMethodsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAuthMethodsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAuthMethodsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncAuthMethodsResourceWithStreamingResponse(self)

    async def list(
        self,
        application_id: Literal[
            "ANTHROPIC",
            "AWS",
            "BITBUCKET",
            "BOX",
            "CONFLUENCE",
            "DROPBOX",
            "GITHUB",
            "GITLAB",
            "GOOGLE_CLOUD_PLATFORM",
            "GOOGLE_WORKSPACE",
            "JIRA",
            "MICROSOFT_INTERNAL",
            "OPENAI",
            "SALESFORCE",
            "SERVICENOW",
            "SLACK",
            "ZOOM",
        ],
        *,
        account_id: str,
        page: int | Omit = omit,
        page_size: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Returns available auth methods for the specified vendor, including credential
        schema, instructions, and example payloads. Use this to understand what
        credentials are required before calling POST /v2/integrations.

        Args:
          page: A page number within the paginated result set.

          page_size: Number of results to return per page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not application_id:
            raise ValueError(f"Expected a non-empty value for `application_id` but received {application_id!r}")
        return await self._get(
            path_template(
                "/accounts/{account_id}/one/applications/{application_id}/auth-methods",
                account_id=account_id,
                application_id=application_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "page": page,
                        "page_size": page_size,
                    },
                    auth_method_list_params.AuthMethodListParams,
                ),
            ),
            cast_to=object,
        )


class AuthMethodsResourceWithRawResponse:
    def __init__(self, auth_methods: AuthMethodsResource) -> None:
        self._auth_methods = auth_methods

        self.list = to_raw_response_wrapper(
            auth_methods.list,
        )


class AsyncAuthMethodsResourceWithRawResponse:
    def __init__(self, auth_methods: AsyncAuthMethodsResource) -> None:
        self._auth_methods = auth_methods

        self.list = async_to_raw_response_wrapper(
            auth_methods.list,
        )


class AuthMethodsResourceWithStreamingResponse:
    def __init__(self, auth_methods: AuthMethodsResource) -> None:
        self._auth_methods = auth_methods

        self.list = to_streamed_response_wrapper(
            auth_methods.list,
        )


class AsyncAuthMethodsResourceWithStreamingResponse:
    def __init__(self, auth_methods: AsyncAuthMethodsResource) -> None:
        self._auth_methods = auth_methods

        self.list = async_to_streamed_response_wrapper(
            auth_methods.list,
        )
