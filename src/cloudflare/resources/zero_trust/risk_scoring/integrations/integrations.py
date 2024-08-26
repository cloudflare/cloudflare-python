# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .references import ReferencesResource, AsyncReferencesResource

from ....._compat import cached_property

from .....types.zero_trust.risk_scoring.integration_create_response import IntegrationCreateResponse

from ....._wrappers import ResultWrapper

from ....._utils import maybe_transform, async_maybe_transform

from typing import Optional, Type

from ....._base_client import make_request_options, AsyncPaginator

from typing_extensions import Literal

from .....types.zero_trust.risk_scoring.integration_update_response import IntegrationUpdateResponse

from .....types.zero_trust.risk_scoring.integration_list_response import IntegrationListResponse

from .....pagination import SyncSinglePage, AsyncSinglePage

from .....types.zero_trust.risk_scoring.integration_get_response import IntegrationGetResponse

from ....._response import to_raw_response_wrapper, async_to_raw_response_wrapper, to_streamed_response_wrapper, async_to_streamed_response_wrapper

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ....._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ....._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ....._resource import SyncAPIResource, AsyncAPIResource
from .....types import shared_params
from .....types.zero_trust.risk_scoring import integration_create_params
from .....types.zero_trust.risk_scoring import integration_update_params
from .references import ReferencesResource, AsyncReferencesResource, ReferencesResourceWithRawResponse, AsyncReferencesResourceWithRawResponse, ReferencesResourceWithStreamingResponse, AsyncReferencesResourceWithStreamingResponse
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast

__all__ = ["IntegrationsResource", "AsyncIntegrationsResource"]

class IntegrationsResource(SyncAPIResource):
    @cached_property
    def references(self) -> ReferencesResource:
        return ReferencesResource(self._client)

    @cached_property
    def with_raw_response(self) -> IntegrationsResourceWithRawResponse:
        return IntegrationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> IntegrationsResourceWithStreamingResponse:
        return IntegrationsResourceWithStreamingResponse(self)

    def create(self,
    *,
    account_id: str,
    integration_type: Literal["Okta"],
    tenant_url: str,
    reference_id: Optional[str] | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Optional[IntegrationCreateResponse]:
        """
        Create new risk score integration.

        Args:
          tenant_url: The base url of the tenant, e.g. "https://tenant.okta.com"

          reference_id: A reference id that can be supplied by the client. Currently this should be set
              to the Access-Okta IDP ID (a UUIDv4).
              https://developers.cloudflare.com/api/operations/access-identity-providers-get-an-access-identity-provider

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
          raise ValueError(
            f'Expected a non-empty value for `account_id` but received {account_id!r}'
          )
        return self._post(
            f"/accounts/{account_id}/zt_risk_scoring/integrations",
            body=maybe_transform({
                "integration_type": integration_type,
                "tenant_url": tenant_url,
                "reference_id": reference_id,
            }, integration_create_params.IntegrationCreateParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[Optional[IntegrationCreateResponse]]._unwrapper),
            cast_to=cast(Type[Optional[IntegrationCreateResponse]], ResultWrapper[IntegrationCreateResponse]),
        )

    def update(self,
    integration_id: str,
    *,
    account_id: str,
    active: bool,
    tenant_url: str,
    reference_id: Optional[str] | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Optional[IntegrationUpdateResponse]:
        """
        Overwrite the reference_id, tenant_url, and active values with the ones provided

        Args:
          active: Whether this integration is enabled. If disabled, no risk changes will be
              exported to the third-party.

          tenant_url: The base url of the tenant, e.g. "https://tenant.okta.com"

          reference_id: A reference id that can be supplied by the client. Currently this should be set
              to the Access-Okta IDP ID (a UUIDv4).
              https://developers.cloudflare.com/api/operations/access-identity-providers-get-an-access-identity-provider

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
          raise ValueError(
            f'Expected a non-empty value for `account_id` but received {account_id!r}'
          )
        if not integration_id:
          raise ValueError(
            f'Expected a non-empty value for `integration_id` but received {integration_id!r}'
          )
        return self._put(
            f"/accounts/{account_id}/zt_risk_scoring/integrations/{integration_id}",
            body=maybe_transform({
                "active": active,
                "tenant_url": tenant_url,
                "reference_id": reference_id,
            }, integration_update_params.IntegrationUpdateParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[Optional[IntegrationUpdateResponse]]._unwrapper),
            cast_to=cast(Type[Optional[IntegrationUpdateResponse]], ResultWrapper[IntegrationUpdateResponse]),
        )

    def list(self,
    *,
    account_id: str,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> SyncSinglePage[IntegrationListResponse]:
        """
        List all risk score integrations for the account.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
          raise ValueError(
            f'Expected a non-empty value for `account_id` but received {account_id!r}'
          )
        return self._get_api_list(
            f"/accounts/{account_id}/zt_risk_scoring/integrations",
            page = SyncSinglePage[IntegrationListResponse],
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            model=IntegrationListResponse,
        )

    def delete(self,
    integration_id: str,
    *,
    account_id: str,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> object:
        """
        Delete a risk score integration.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
          raise ValueError(
            f'Expected a non-empty value for `account_id` but received {account_id!r}'
          )
        if not integration_id:
          raise ValueError(
            f'Expected a non-empty value for `integration_id` but received {integration_id!r}'
          )
        return self._delete(
            f"/accounts/{account_id}/zt_risk_scoring/integrations/{integration_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[Optional[object]]._unwrapper),
            cast_to=cast(Type[object], ResultWrapper[object]),
        )

    def get(self,
    integration_id: str,
    *,
    account_id: str,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Optional[IntegrationGetResponse]:
        """
        Get risk score integration by id.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
          raise ValueError(
            f'Expected a non-empty value for `account_id` but received {account_id!r}'
          )
        if not integration_id:
          raise ValueError(
            f'Expected a non-empty value for `integration_id` but received {integration_id!r}'
          )
        return self._get(
            f"/accounts/{account_id}/zt_risk_scoring/integrations/{integration_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[Optional[IntegrationGetResponse]]._unwrapper),
            cast_to=cast(Type[Optional[IntegrationGetResponse]], ResultWrapper[IntegrationGetResponse]),
        )

class AsyncIntegrationsResource(AsyncAPIResource):
    @cached_property
    def references(self) -> AsyncReferencesResource:
        return AsyncReferencesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncIntegrationsResourceWithRawResponse:
        return AsyncIntegrationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncIntegrationsResourceWithStreamingResponse:
        return AsyncIntegrationsResourceWithStreamingResponse(self)

    async def create(self,
    *,
    account_id: str,
    integration_type: Literal["Okta"],
    tenant_url: str,
    reference_id: Optional[str] | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Optional[IntegrationCreateResponse]:
        """
        Create new risk score integration.

        Args:
          tenant_url: The base url of the tenant, e.g. "https://tenant.okta.com"

          reference_id: A reference id that can be supplied by the client. Currently this should be set
              to the Access-Okta IDP ID (a UUIDv4).
              https://developers.cloudflare.com/api/operations/access-identity-providers-get-an-access-identity-provider

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
          raise ValueError(
            f'Expected a non-empty value for `account_id` but received {account_id!r}'
          )
        return await self._post(
            f"/accounts/{account_id}/zt_risk_scoring/integrations",
            body=await async_maybe_transform({
                "integration_type": integration_type,
                "tenant_url": tenant_url,
                "reference_id": reference_id,
            }, integration_create_params.IntegrationCreateParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[Optional[IntegrationCreateResponse]]._unwrapper),
            cast_to=cast(Type[Optional[IntegrationCreateResponse]], ResultWrapper[IntegrationCreateResponse]),
        )

    async def update(self,
    integration_id: str,
    *,
    account_id: str,
    active: bool,
    tenant_url: str,
    reference_id: Optional[str] | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Optional[IntegrationUpdateResponse]:
        """
        Overwrite the reference_id, tenant_url, and active values with the ones provided

        Args:
          active: Whether this integration is enabled. If disabled, no risk changes will be
              exported to the third-party.

          tenant_url: The base url of the tenant, e.g. "https://tenant.okta.com"

          reference_id: A reference id that can be supplied by the client. Currently this should be set
              to the Access-Okta IDP ID (a UUIDv4).
              https://developers.cloudflare.com/api/operations/access-identity-providers-get-an-access-identity-provider

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
          raise ValueError(
            f'Expected a non-empty value for `account_id` but received {account_id!r}'
          )
        if not integration_id:
          raise ValueError(
            f'Expected a non-empty value for `integration_id` but received {integration_id!r}'
          )
        return await self._put(
            f"/accounts/{account_id}/zt_risk_scoring/integrations/{integration_id}",
            body=await async_maybe_transform({
                "active": active,
                "tenant_url": tenant_url,
                "reference_id": reference_id,
            }, integration_update_params.IntegrationUpdateParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[Optional[IntegrationUpdateResponse]]._unwrapper),
            cast_to=cast(Type[Optional[IntegrationUpdateResponse]], ResultWrapper[IntegrationUpdateResponse]),
        )

    def list(self,
    *,
    account_id: str,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> AsyncPaginator[IntegrationListResponse, AsyncSinglePage[IntegrationListResponse]]:
        """
        List all risk score integrations for the account.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
          raise ValueError(
            f'Expected a non-empty value for `account_id` but received {account_id!r}'
          )
        return self._get_api_list(
            f"/accounts/{account_id}/zt_risk_scoring/integrations",
            page = AsyncSinglePage[IntegrationListResponse],
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            model=IntegrationListResponse,
        )

    async def delete(self,
    integration_id: str,
    *,
    account_id: str,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> object:
        """
        Delete a risk score integration.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
          raise ValueError(
            f'Expected a non-empty value for `account_id` but received {account_id!r}'
          )
        if not integration_id:
          raise ValueError(
            f'Expected a non-empty value for `integration_id` but received {integration_id!r}'
          )
        return await self._delete(
            f"/accounts/{account_id}/zt_risk_scoring/integrations/{integration_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[Optional[object]]._unwrapper),
            cast_to=cast(Type[object], ResultWrapper[object]),
        )

    async def get(self,
    integration_id: str,
    *,
    account_id: str,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Optional[IntegrationGetResponse]:
        """
        Get risk score integration by id.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
          raise ValueError(
            f'Expected a non-empty value for `account_id` but received {account_id!r}'
          )
        if not integration_id:
          raise ValueError(
            f'Expected a non-empty value for `integration_id` but received {integration_id!r}'
          )
        return await self._get(
            f"/accounts/{account_id}/zt_risk_scoring/integrations/{integration_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[Optional[IntegrationGetResponse]]._unwrapper),
            cast_to=cast(Type[Optional[IntegrationGetResponse]], ResultWrapper[IntegrationGetResponse]),
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

    @cached_property
    def references(self) -> ReferencesResourceWithRawResponse:
        return ReferencesResourceWithRawResponse(self._integrations.references)

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

    @cached_property
    def references(self) -> AsyncReferencesResourceWithRawResponse:
        return AsyncReferencesResourceWithRawResponse(self._integrations.references)

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

    @cached_property
    def references(self) -> ReferencesResourceWithStreamingResponse:
        return ReferencesResourceWithStreamingResponse(self._integrations.references)

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

    @cached_property
    def references(self) -> AsyncReferencesResourceWithStreamingResponse:
        return AsyncReferencesResourceWithStreamingResponse(self._integrations.references)