# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, Type, cast
from typing_extensions import Literal

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    maybe_transform,
    strip_not_given,
    async_maybe_transform,
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
from ...pagination import SyncSinglePage, AsyncSinglePage
from ..._base_client import AsyncPaginator, make_request_options
from ...types.magic_cloud_networking import (
    cloud_integration_get_params,
    cloud_integration_edit_params,
    cloud_integration_list_params,
    cloud_integration_create_params,
    cloud_integration_update_params,
    cloud_integration_discover_params,
)
from ...types.magic_cloud_networking.cloud_integration_get_response import CloudIntegrationGetResponse
from ...types.magic_cloud_networking.cloud_integration_edit_response import CloudIntegrationEditResponse
from ...types.magic_cloud_networking.cloud_integration_list_response import CloudIntegrationListResponse
from ...types.magic_cloud_networking.cloud_integration_create_response import CloudIntegrationCreateResponse
from ...types.magic_cloud_networking.cloud_integration_delete_response import CloudIntegrationDeleteResponse
from ...types.magic_cloud_networking.cloud_integration_update_response import CloudIntegrationUpdateResponse
from ...types.magic_cloud_networking.cloud_integration_discover_response import CloudIntegrationDiscoverResponse
from ...types.magic_cloud_networking.cloud_integration_discover_all_response import CloudIntegrationDiscoverAllResponse
from ...types.magic_cloud_networking.cloud_integration_initial_setup_response import (
    CloudIntegrationInitialSetupResponse,
)

__all__ = ["CloudIntegrationsResource", "AsyncCloudIntegrationsResource"]


class CloudIntegrationsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CloudIntegrationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return CloudIntegrationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CloudIntegrationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return CloudIntegrationsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        account_id: str,
        cloud_type: Literal["AWS", "AZURE", "GOOGLE", "CLOUDFLARE"],
        friendly_name: str,
        description: str | NotGiven = NOT_GIVEN,
        forwarded: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CloudIntegrationCreateResponse:
        """
        Create a new Cloud Integration (Closed Beta)

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        extra_headers = {**strip_not_given({"forwarded": forwarded}), **(extra_headers or {})}
        return self._post(
            f"/accounts/{account_id}/magic/cloud/providers",
            body=maybe_transform(
                {
                    "cloud_type": cloud_type,
                    "friendly_name": friendly_name,
                    "description": description,
                },
                cloud_integration_create_params.CloudIntegrationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[CloudIntegrationCreateResponse]._unwrapper,
            ),
            cast_to=cast(Type[CloudIntegrationCreateResponse], ResultWrapper[CloudIntegrationCreateResponse]),
        )

    def update(
        self,
        provider_id: str,
        *,
        account_id: str,
        aws_arn: str | NotGiven = NOT_GIVEN,
        azure_subscription_id: str | NotGiven = NOT_GIVEN,
        azure_tenant_id: str | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        friendly_name: str | NotGiven = NOT_GIVEN,
        gcp_project_id: str | NotGiven = NOT_GIVEN,
        gcp_service_account_email: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CloudIntegrationUpdateResponse:
        """
        Update a Cloud Integration (Closed Beta)

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not provider_id:
            raise ValueError(f"Expected a non-empty value for `provider_id` but received {provider_id!r}")
        return self._put(
            f"/accounts/{account_id}/magic/cloud/providers/{provider_id}",
            body=maybe_transform(
                {
                    "aws_arn": aws_arn,
                    "azure_subscription_id": azure_subscription_id,
                    "azure_tenant_id": azure_tenant_id,
                    "description": description,
                    "friendly_name": friendly_name,
                    "gcp_project_id": gcp_project_id,
                    "gcp_service_account_email": gcp_service_account_email,
                },
                cloud_integration_update_params.CloudIntegrationUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[CloudIntegrationUpdateResponse]._unwrapper,
            ),
            cast_to=cast(Type[CloudIntegrationUpdateResponse], ResultWrapper[CloudIntegrationUpdateResponse]),
        )

    def list(
        self,
        *,
        account_id: str,
        cloudflare: bool | NotGiven = NOT_GIVEN,
        desc: bool | NotGiven = NOT_GIVEN,
        order_by: str | NotGiven = NOT_GIVEN,
        status: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncSinglePage[CloudIntegrationListResponse]:
        """
        List Cloud Integrations (Closed Beta)

        Args:
          order_by: one of ["updated_at", "id", "cloud_type", "name"]

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/magic/cloud/providers",
            page=SyncSinglePage[CloudIntegrationListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cloudflare": cloudflare,
                        "desc": desc,
                        "order_by": order_by,
                        "status": status,
                    },
                    cloud_integration_list_params.CloudIntegrationListParams,
                ),
            ),
            model=CloudIntegrationListResponse,
        )

    def delete(
        self,
        provider_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CloudIntegrationDeleteResponse:
        """
        Delete a Cloud Integration (Closed Beta)

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not provider_id:
            raise ValueError(f"Expected a non-empty value for `provider_id` but received {provider_id!r}")
        return self._delete(
            f"/accounts/{account_id}/magic/cloud/providers/{provider_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[CloudIntegrationDeleteResponse]._unwrapper,
            ),
            cast_to=cast(Type[CloudIntegrationDeleteResponse], ResultWrapper[CloudIntegrationDeleteResponse]),
        )

    def discover(
        self,
        provider_id: str,
        *,
        account_id: str,
        v2: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CloudIntegrationDiscoverResponse:
        """
        Run discovery for a Cloud Integration (Closed Beta)

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not provider_id:
            raise ValueError(f"Expected a non-empty value for `provider_id` but received {provider_id!r}")
        return self._post(
            f"/accounts/{account_id}/magic/cloud/providers/{provider_id}/discover",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"v2": v2}, cloud_integration_discover_params.CloudIntegrationDiscoverParams),
            ),
            cast_to=CloudIntegrationDiscoverResponse,
        )

    def discover_all(
        self,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CloudIntegrationDiscoverAllResponse:
        """
        Run discovery for all Cloud Integrations in an account (Closed Beta)

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._post(
            f"/accounts/{account_id}/magic/cloud/providers/discover",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CloudIntegrationDiscoverAllResponse,
        )

    def edit(
        self,
        provider_id: str,
        *,
        account_id: str,
        aws_arn: str | NotGiven = NOT_GIVEN,
        azure_subscription_id: str | NotGiven = NOT_GIVEN,
        azure_tenant_id: str | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        friendly_name: str | NotGiven = NOT_GIVEN,
        gcp_project_id: str | NotGiven = NOT_GIVEN,
        gcp_service_account_email: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CloudIntegrationEditResponse:
        """
        Update a Cloud Integration (Closed Beta)

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not provider_id:
            raise ValueError(f"Expected a non-empty value for `provider_id` but received {provider_id!r}")
        return self._patch(
            f"/accounts/{account_id}/magic/cloud/providers/{provider_id}",
            body=maybe_transform(
                {
                    "aws_arn": aws_arn,
                    "azure_subscription_id": azure_subscription_id,
                    "azure_tenant_id": azure_tenant_id,
                    "description": description,
                    "friendly_name": friendly_name,
                    "gcp_project_id": gcp_project_id,
                    "gcp_service_account_email": gcp_service_account_email,
                },
                cloud_integration_edit_params.CloudIntegrationEditParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[CloudIntegrationEditResponse]._unwrapper,
            ),
            cast_to=cast(Type[CloudIntegrationEditResponse], ResultWrapper[CloudIntegrationEditResponse]),
        )

    def get(
        self,
        provider_id: str,
        *,
        account_id: str,
        status: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CloudIntegrationGetResponse:
        """
        Read a Cloud Integration (Closed Beta)

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not provider_id:
            raise ValueError(f"Expected a non-empty value for `provider_id` but received {provider_id!r}")
        return self._get(
            f"/accounts/{account_id}/magic/cloud/providers/{provider_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"status": status}, cloud_integration_get_params.CloudIntegrationGetParams),
                post_parser=ResultWrapper[CloudIntegrationGetResponse]._unwrapper,
            ),
            cast_to=cast(Type[CloudIntegrationGetResponse], ResultWrapper[CloudIntegrationGetResponse]),
        )

    def initial_setup(
        self,
        provider_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CloudIntegrationInitialSetupResponse:
        """
        Get initial configuration to complete Cloud Integration setup (Closed Beta)

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not provider_id:
            raise ValueError(f"Expected a non-empty value for `provider_id` but received {provider_id!r}")
        return cast(
            CloudIntegrationInitialSetupResponse,
            self._get(
                f"/accounts/{account_id}/magic/cloud/providers/{provider_id}/initial_setup",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper[CloudIntegrationInitialSetupResponse]._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[CloudIntegrationInitialSetupResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class AsyncCloudIntegrationsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCloudIntegrationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCloudIntegrationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCloudIntegrationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncCloudIntegrationsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_id: str,
        cloud_type: Literal["AWS", "AZURE", "GOOGLE", "CLOUDFLARE"],
        friendly_name: str,
        description: str | NotGiven = NOT_GIVEN,
        forwarded: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CloudIntegrationCreateResponse:
        """
        Create a new Cloud Integration (Closed Beta)

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        extra_headers = {**strip_not_given({"forwarded": forwarded}), **(extra_headers or {})}
        return await self._post(
            f"/accounts/{account_id}/magic/cloud/providers",
            body=await async_maybe_transform(
                {
                    "cloud_type": cloud_type,
                    "friendly_name": friendly_name,
                    "description": description,
                },
                cloud_integration_create_params.CloudIntegrationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[CloudIntegrationCreateResponse]._unwrapper,
            ),
            cast_to=cast(Type[CloudIntegrationCreateResponse], ResultWrapper[CloudIntegrationCreateResponse]),
        )

    async def update(
        self,
        provider_id: str,
        *,
        account_id: str,
        aws_arn: str | NotGiven = NOT_GIVEN,
        azure_subscription_id: str | NotGiven = NOT_GIVEN,
        azure_tenant_id: str | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        friendly_name: str | NotGiven = NOT_GIVEN,
        gcp_project_id: str | NotGiven = NOT_GIVEN,
        gcp_service_account_email: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CloudIntegrationUpdateResponse:
        """
        Update a Cloud Integration (Closed Beta)

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not provider_id:
            raise ValueError(f"Expected a non-empty value for `provider_id` but received {provider_id!r}")
        return await self._put(
            f"/accounts/{account_id}/magic/cloud/providers/{provider_id}",
            body=await async_maybe_transform(
                {
                    "aws_arn": aws_arn,
                    "azure_subscription_id": azure_subscription_id,
                    "azure_tenant_id": azure_tenant_id,
                    "description": description,
                    "friendly_name": friendly_name,
                    "gcp_project_id": gcp_project_id,
                    "gcp_service_account_email": gcp_service_account_email,
                },
                cloud_integration_update_params.CloudIntegrationUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[CloudIntegrationUpdateResponse]._unwrapper,
            ),
            cast_to=cast(Type[CloudIntegrationUpdateResponse], ResultWrapper[CloudIntegrationUpdateResponse]),
        )

    def list(
        self,
        *,
        account_id: str,
        cloudflare: bool | NotGiven = NOT_GIVEN,
        desc: bool | NotGiven = NOT_GIVEN,
        order_by: str | NotGiven = NOT_GIVEN,
        status: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[CloudIntegrationListResponse, AsyncSinglePage[CloudIntegrationListResponse]]:
        """
        List Cloud Integrations (Closed Beta)

        Args:
          order_by: one of ["updated_at", "id", "cloud_type", "name"]

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/magic/cloud/providers",
            page=AsyncSinglePage[CloudIntegrationListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cloudflare": cloudflare,
                        "desc": desc,
                        "order_by": order_by,
                        "status": status,
                    },
                    cloud_integration_list_params.CloudIntegrationListParams,
                ),
            ),
            model=CloudIntegrationListResponse,
        )

    async def delete(
        self,
        provider_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CloudIntegrationDeleteResponse:
        """
        Delete a Cloud Integration (Closed Beta)

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not provider_id:
            raise ValueError(f"Expected a non-empty value for `provider_id` but received {provider_id!r}")
        return await self._delete(
            f"/accounts/{account_id}/magic/cloud/providers/{provider_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[CloudIntegrationDeleteResponse]._unwrapper,
            ),
            cast_to=cast(Type[CloudIntegrationDeleteResponse], ResultWrapper[CloudIntegrationDeleteResponse]),
        )

    async def discover(
        self,
        provider_id: str,
        *,
        account_id: str,
        v2: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CloudIntegrationDiscoverResponse:
        """
        Run discovery for a Cloud Integration (Closed Beta)

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not provider_id:
            raise ValueError(f"Expected a non-empty value for `provider_id` but received {provider_id!r}")
        return await self._post(
            f"/accounts/{account_id}/magic/cloud/providers/{provider_id}/discover",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"v2": v2}, cloud_integration_discover_params.CloudIntegrationDiscoverParams
                ),
            ),
            cast_to=CloudIntegrationDiscoverResponse,
        )

    async def discover_all(
        self,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CloudIntegrationDiscoverAllResponse:
        """
        Run discovery for all Cloud Integrations in an account (Closed Beta)

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._post(
            f"/accounts/{account_id}/magic/cloud/providers/discover",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CloudIntegrationDiscoverAllResponse,
        )

    async def edit(
        self,
        provider_id: str,
        *,
        account_id: str,
        aws_arn: str | NotGiven = NOT_GIVEN,
        azure_subscription_id: str | NotGiven = NOT_GIVEN,
        azure_tenant_id: str | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        friendly_name: str | NotGiven = NOT_GIVEN,
        gcp_project_id: str | NotGiven = NOT_GIVEN,
        gcp_service_account_email: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CloudIntegrationEditResponse:
        """
        Update a Cloud Integration (Closed Beta)

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not provider_id:
            raise ValueError(f"Expected a non-empty value for `provider_id` but received {provider_id!r}")
        return await self._patch(
            f"/accounts/{account_id}/magic/cloud/providers/{provider_id}",
            body=await async_maybe_transform(
                {
                    "aws_arn": aws_arn,
                    "azure_subscription_id": azure_subscription_id,
                    "azure_tenant_id": azure_tenant_id,
                    "description": description,
                    "friendly_name": friendly_name,
                    "gcp_project_id": gcp_project_id,
                    "gcp_service_account_email": gcp_service_account_email,
                },
                cloud_integration_edit_params.CloudIntegrationEditParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[CloudIntegrationEditResponse]._unwrapper,
            ),
            cast_to=cast(Type[CloudIntegrationEditResponse], ResultWrapper[CloudIntegrationEditResponse]),
        )

    async def get(
        self,
        provider_id: str,
        *,
        account_id: str,
        status: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CloudIntegrationGetResponse:
        """
        Read a Cloud Integration (Closed Beta)

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not provider_id:
            raise ValueError(f"Expected a non-empty value for `provider_id` but received {provider_id!r}")
        return await self._get(
            f"/accounts/{account_id}/magic/cloud/providers/{provider_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"status": status}, cloud_integration_get_params.CloudIntegrationGetParams
                ),
                post_parser=ResultWrapper[CloudIntegrationGetResponse]._unwrapper,
            ),
            cast_to=cast(Type[CloudIntegrationGetResponse], ResultWrapper[CloudIntegrationGetResponse]),
        )

    async def initial_setup(
        self,
        provider_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CloudIntegrationInitialSetupResponse:
        """
        Get initial configuration to complete Cloud Integration setup (Closed Beta)

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not provider_id:
            raise ValueError(f"Expected a non-empty value for `provider_id` but received {provider_id!r}")
        return cast(
            CloudIntegrationInitialSetupResponse,
            await self._get(
                f"/accounts/{account_id}/magic/cloud/providers/{provider_id}/initial_setup",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper[CloudIntegrationInitialSetupResponse]._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[CloudIntegrationInitialSetupResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class CloudIntegrationsResourceWithRawResponse:
    def __init__(self, cloud_integrations: CloudIntegrationsResource) -> None:
        self._cloud_integrations = cloud_integrations

        self.create = to_raw_response_wrapper(
            cloud_integrations.create,
        )
        self.update = to_raw_response_wrapper(
            cloud_integrations.update,
        )
        self.list = to_raw_response_wrapper(
            cloud_integrations.list,
        )
        self.delete = to_raw_response_wrapper(
            cloud_integrations.delete,
        )
        self.discover = to_raw_response_wrapper(
            cloud_integrations.discover,
        )
        self.discover_all = to_raw_response_wrapper(
            cloud_integrations.discover_all,
        )
        self.edit = to_raw_response_wrapper(
            cloud_integrations.edit,
        )
        self.get = to_raw_response_wrapper(
            cloud_integrations.get,
        )
        self.initial_setup = to_raw_response_wrapper(
            cloud_integrations.initial_setup,
        )


class AsyncCloudIntegrationsResourceWithRawResponse:
    def __init__(self, cloud_integrations: AsyncCloudIntegrationsResource) -> None:
        self._cloud_integrations = cloud_integrations

        self.create = async_to_raw_response_wrapper(
            cloud_integrations.create,
        )
        self.update = async_to_raw_response_wrapper(
            cloud_integrations.update,
        )
        self.list = async_to_raw_response_wrapper(
            cloud_integrations.list,
        )
        self.delete = async_to_raw_response_wrapper(
            cloud_integrations.delete,
        )
        self.discover = async_to_raw_response_wrapper(
            cloud_integrations.discover,
        )
        self.discover_all = async_to_raw_response_wrapper(
            cloud_integrations.discover_all,
        )
        self.edit = async_to_raw_response_wrapper(
            cloud_integrations.edit,
        )
        self.get = async_to_raw_response_wrapper(
            cloud_integrations.get,
        )
        self.initial_setup = async_to_raw_response_wrapper(
            cloud_integrations.initial_setup,
        )


class CloudIntegrationsResourceWithStreamingResponse:
    def __init__(self, cloud_integrations: CloudIntegrationsResource) -> None:
        self._cloud_integrations = cloud_integrations

        self.create = to_streamed_response_wrapper(
            cloud_integrations.create,
        )
        self.update = to_streamed_response_wrapper(
            cloud_integrations.update,
        )
        self.list = to_streamed_response_wrapper(
            cloud_integrations.list,
        )
        self.delete = to_streamed_response_wrapper(
            cloud_integrations.delete,
        )
        self.discover = to_streamed_response_wrapper(
            cloud_integrations.discover,
        )
        self.discover_all = to_streamed_response_wrapper(
            cloud_integrations.discover_all,
        )
        self.edit = to_streamed_response_wrapper(
            cloud_integrations.edit,
        )
        self.get = to_streamed_response_wrapper(
            cloud_integrations.get,
        )
        self.initial_setup = to_streamed_response_wrapper(
            cloud_integrations.initial_setup,
        )


class AsyncCloudIntegrationsResourceWithStreamingResponse:
    def __init__(self, cloud_integrations: AsyncCloudIntegrationsResource) -> None:
        self._cloud_integrations = cloud_integrations

        self.create = async_to_streamed_response_wrapper(
            cloud_integrations.create,
        )
        self.update = async_to_streamed_response_wrapper(
            cloud_integrations.update,
        )
        self.list = async_to_streamed_response_wrapper(
            cloud_integrations.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            cloud_integrations.delete,
        )
        self.discover = async_to_streamed_response_wrapper(
            cloud_integrations.discover,
        )
        self.discover_all = async_to_streamed_response_wrapper(
            cloud_integrations.discover_all,
        )
        self.edit = async_to_streamed_response_wrapper(
            cloud_integrations.edit,
        )
        self.get = async_to_streamed_response_wrapper(
            cloud_integrations.get,
        )
        self.initial_setup = async_to_streamed_response_wrapper(
            cloud_integrations.initial_setup,
        )
