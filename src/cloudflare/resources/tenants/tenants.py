# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, cast

import httpx

from ..._types import Body, Query, Headers, NotGiven, not_given
from ..._utils import path_template
from .accounts import (
    AccountsResource,
    AsyncAccountsResource,
    AccountsResourceWithRawResponse,
    AsyncAccountsResourceWithRawResponse,
    AccountsResourceWithStreamingResponse,
    AsyncAccountsResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._wrappers import ResultWrapper
from .memberships import (
    MembershipsResource,
    AsyncMembershipsResource,
    MembershipsResourceWithRawResponse,
    AsyncMembershipsResourceWithRawResponse,
    MembershipsResourceWithStreamingResponse,
    AsyncMembershipsResourceWithStreamingResponse,
)
from .entitlements import (
    EntitlementsResource,
    AsyncEntitlementsResource,
    EntitlementsResourceWithRawResponse,
    AsyncEntitlementsResourceWithRawResponse,
    EntitlementsResourceWithStreamingResponse,
    AsyncEntitlementsResourceWithStreamingResponse,
)
from .account_types import (
    AccountTypesResource,
    AsyncAccountTypesResource,
    AccountTypesResourceWithRawResponse,
    AsyncAccountTypesResourceWithRawResponse,
    AccountTypesResourceWithStreamingResponse,
    AsyncAccountTypesResourceWithStreamingResponse,
)
from ..._base_client import make_request_options
from ...types.tenants.tenant import Tenant

__all__ = ["TenantsResource", "AsyncTenantsResource"]


class TenantsResource(SyncAPIResource):
    @cached_property
    def account_types(self) -> AccountTypesResource:
        return AccountTypesResource(self._client)

    @cached_property
    def accounts(self) -> AccountsResource:
        return AccountsResource(self._client)

    @cached_property
    def entitlements(self) -> EntitlementsResource:
        return EntitlementsResource(self._client)

    @cached_property
    def memberships(self) -> MembershipsResource:
        return MembershipsResource(self._client)

    @cached_property
    def with_raw_response(self) -> TenantsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return TenantsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TenantsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return TenantsResourceWithStreamingResponse(self)

    def get(
        self,
        tenant_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Tenant:
        """
        Retrieves a Tenant by Tenant ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not tenant_id:
            raise ValueError(f"Expected a non-empty value for `tenant_id` but received {tenant_id!r}")
        return self._get(
            path_template("/tenants/{tenant_id}", tenant_id=tenant_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Tenant]._unwrapper,
            ),
            cast_to=cast(Type[Tenant], ResultWrapper[Tenant]),
        )


class AsyncTenantsResource(AsyncAPIResource):
    @cached_property
    def account_types(self) -> AsyncAccountTypesResource:
        return AsyncAccountTypesResource(self._client)

    @cached_property
    def accounts(self) -> AsyncAccountsResource:
        return AsyncAccountsResource(self._client)

    @cached_property
    def entitlements(self) -> AsyncEntitlementsResource:
        return AsyncEntitlementsResource(self._client)

    @cached_property
    def memberships(self) -> AsyncMembershipsResource:
        return AsyncMembershipsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncTenantsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTenantsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTenantsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncTenantsResourceWithStreamingResponse(self)

    async def get(
        self,
        tenant_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Tenant:
        """
        Retrieves a Tenant by Tenant ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not tenant_id:
            raise ValueError(f"Expected a non-empty value for `tenant_id` but received {tenant_id!r}")
        return await self._get(
            path_template("/tenants/{tenant_id}", tenant_id=tenant_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Tenant]._unwrapper,
            ),
            cast_to=cast(Type[Tenant], ResultWrapper[Tenant]),
        )


class TenantsResourceWithRawResponse:
    def __init__(self, tenants: TenantsResource) -> None:
        self._tenants = tenants

        self.get = to_raw_response_wrapper(
            tenants.get,
        )

    @cached_property
    def account_types(self) -> AccountTypesResourceWithRawResponse:
        return AccountTypesResourceWithRawResponse(self._tenants.account_types)

    @cached_property
    def accounts(self) -> AccountsResourceWithRawResponse:
        return AccountsResourceWithRawResponse(self._tenants.accounts)

    @cached_property
    def entitlements(self) -> EntitlementsResourceWithRawResponse:
        return EntitlementsResourceWithRawResponse(self._tenants.entitlements)

    @cached_property
    def memberships(self) -> MembershipsResourceWithRawResponse:
        return MembershipsResourceWithRawResponse(self._tenants.memberships)


class AsyncTenantsResourceWithRawResponse:
    def __init__(self, tenants: AsyncTenantsResource) -> None:
        self._tenants = tenants

        self.get = async_to_raw_response_wrapper(
            tenants.get,
        )

    @cached_property
    def account_types(self) -> AsyncAccountTypesResourceWithRawResponse:
        return AsyncAccountTypesResourceWithRawResponse(self._tenants.account_types)

    @cached_property
    def accounts(self) -> AsyncAccountsResourceWithRawResponse:
        return AsyncAccountsResourceWithRawResponse(self._tenants.accounts)

    @cached_property
    def entitlements(self) -> AsyncEntitlementsResourceWithRawResponse:
        return AsyncEntitlementsResourceWithRawResponse(self._tenants.entitlements)

    @cached_property
    def memberships(self) -> AsyncMembershipsResourceWithRawResponse:
        return AsyncMembershipsResourceWithRawResponse(self._tenants.memberships)


class TenantsResourceWithStreamingResponse:
    def __init__(self, tenants: TenantsResource) -> None:
        self._tenants = tenants

        self.get = to_streamed_response_wrapper(
            tenants.get,
        )

    @cached_property
    def account_types(self) -> AccountTypesResourceWithStreamingResponse:
        return AccountTypesResourceWithStreamingResponse(self._tenants.account_types)

    @cached_property
    def accounts(self) -> AccountsResourceWithStreamingResponse:
        return AccountsResourceWithStreamingResponse(self._tenants.accounts)

    @cached_property
    def entitlements(self) -> EntitlementsResourceWithStreamingResponse:
        return EntitlementsResourceWithStreamingResponse(self._tenants.entitlements)

    @cached_property
    def memberships(self) -> MembershipsResourceWithStreamingResponse:
        return MembershipsResourceWithStreamingResponse(self._tenants.memberships)


class AsyncTenantsResourceWithStreamingResponse:
    def __init__(self, tenants: AsyncTenantsResource) -> None:
        self._tenants = tenants

        self.get = async_to_streamed_response_wrapper(
            tenants.get,
        )

    @cached_property
    def account_types(self) -> AsyncAccountTypesResourceWithStreamingResponse:
        return AsyncAccountTypesResourceWithStreamingResponse(self._tenants.account_types)

    @cached_property
    def accounts(self) -> AsyncAccountsResourceWithStreamingResponse:
        return AsyncAccountsResourceWithStreamingResponse(self._tenants.accounts)

    @cached_property
    def entitlements(self) -> AsyncEntitlementsResourceWithStreamingResponse:
        return AsyncEntitlementsResourceWithStreamingResponse(self._tenants.entitlements)

    @cached_property
    def memberships(self) -> AsyncMembershipsResourceWithStreamingResponse:
        return AsyncMembershipsResourceWithStreamingResponse(self._tenants.memberships)
