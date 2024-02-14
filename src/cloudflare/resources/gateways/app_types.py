# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Type, Optional, cast

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._wrappers import ResultWrapper
from ..._base_client import (
    make_request_options,
)
from ...types.gateways import (
    AppTypeZeroTrustGatewayApplicationAndApplicationTypeMappingsListApplicationAndApplicationTypeMappingsResponse,
)

__all__ = ["AppTypes", "AsyncAppTypes"]


class AppTypes(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AppTypesWithRawResponse:
        return AppTypesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AppTypesWithStreamingResponse:
        return AppTypesWithStreamingResponse(self)

    def zero_trust_gateway_application_and_application_type_mappings_list_application_and_application_type_mappings(
        self,
        account_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[
        AppTypeZeroTrustGatewayApplicationAndApplicationTypeMappingsListApplicationAndApplicationTypeMappingsResponse
    ]:
        """
        Fetches all application and application type mappings.

        Args:
          account_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get(
            f"/accounts/{account_id}/gateway/app_types",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[
                    Optional[
                        AppTypeZeroTrustGatewayApplicationAndApplicationTypeMappingsListApplicationAndApplicationTypeMappingsResponse
                    ]
                ],
                ResultWrapper[
                    AppTypeZeroTrustGatewayApplicationAndApplicationTypeMappingsListApplicationAndApplicationTypeMappingsResponse
                ],
            ),
        )


class AsyncAppTypes(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAppTypesWithRawResponse:
        return AsyncAppTypesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAppTypesWithStreamingResponse:
        return AsyncAppTypesWithStreamingResponse(self)

    async def zero_trust_gateway_application_and_application_type_mappings_list_application_and_application_type_mappings(
        self,
        account_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[
        AppTypeZeroTrustGatewayApplicationAndApplicationTypeMappingsListApplicationAndApplicationTypeMappingsResponse
    ]:
        """
        Fetches all application and application type mappings.

        Args:
          account_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._get(
            f"/accounts/{account_id}/gateway/app_types",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[
                    Optional[
                        AppTypeZeroTrustGatewayApplicationAndApplicationTypeMappingsListApplicationAndApplicationTypeMappingsResponse
                    ]
                ],
                ResultWrapper[
                    AppTypeZeroTrustGatewayApplicationAndApplicationTypeMappingsListApplicationAndApplicationTypeMappingsResponse
                ],
            ),
        )


class AppTypesWithRawResponse:
    def __init__(self, app_types: AppTypes) -> None:
        self._app_types = app_types

        self.zero_trust_gateway_application_and_application_type_mappings_list_application_and_application_type_mappings = to_raw_response_wrapper(
            app_types.zero_trust_gateway_application_and_application_type_mappings_list_application_and_application_type_mappings,
        )


class AsyncAppTypesWithRawResponse:
    def __init__(self, app_types: AsyncAppTypes) -> None:
        self._app_types = app_types

        self.zero_trust_gateway_application_and_application_type_mappings_list_application_and_application_type_mappings = async_to_raw_response_wrapper(
            app_types.zero_trust_gateway_application_and_application_type_mappings_list_application_and_application_type_mappings,
        )


class AppTypesWithStreamingResponse:
    def __init__(self, app_types: AppTypes) -> None:
        self._app_types = app_types

        self.zero_trust_gateway_application_and_application_type_mappings_list_application_and_application_type_mappings = to_streamed_response_wrapper(
            app_types.zero_trust_gateway_application_and_application_type_mappings_list_application_and_application_type_mappings,
        )


class AsyncAppTypesWithStreamingResponse:
    def __init__(self, app_types: AsyncAppTypes) -> None:
        self._app_types = app_types

        self.zero_trust_gateway_application_and_application_type_mappings_list_application_and_application_type_mappings = async_to_streamed_response_wrapper(
            app_types.zero_trust_gateway_application_and_application_type_mappings_list_application_and_application_type_mappings,
        )
