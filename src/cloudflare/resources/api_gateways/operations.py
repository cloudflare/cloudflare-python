# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from ..._compat import cached_property

from ...types.api_gateways import (
    OperationUpdateResponse,
    OperationListResponse,
    OperationDeleteResponse,
    OperationAPIShieldEndpointManagementAddOperationsToAZoneResponse,
    OperationAPIShieldEndpointManagementGetInformationAboutAllOperationsOnAZoneResponse,
    OperationGetResponse,
    operation_api_shield_endpoint_management_add_operations_to_a_zone_params,
)

from typing import Type, Optional, List, Iterable

from typing_extensions import Literal

from ..._response import (
    to_raw_response_wrapper,
    async_to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_streamed_response_wrapper,
)

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ..._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ..._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._base_client import (
    SyncAPIClient,
    AsyncAPIClient,
    _merge_mappings,
    AsyncPaginator,
    make_request_options,
    HttpxBinaryResponseContent,
)
from ...types import shared_params
from ...types.api_gateways import operation_update_params
from ...types.api_gateways import operation_list_params
from ...types.api_gateways import operation_api_shield_endpoint_management_add_operations_to_a_zone_params
from ...types.api_gateways import (
    operation_api_shield_endpoint_management_get_information_about_all_operations_on_a_zone_params,
)
from ...types.api_gateways import operation_get_params
from ..._wrappers import ResultWrapper
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast

__all__ = ["Operations", "AsyncOperations"]


class Operations(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> OperationsWithRawResponse:
        return OperationsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OperationsWithStreamingResponse:
        return OperationsWithStreamingResponse(self)

    def update(
        self,
        operation_id: str,
        *,
        zone_id: str,
        state: Literal["review", "ignored"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OperationUpdateResponse:
        """
        Update the `state` on a discovered operation

        Args:
          zone_id: Identifier

          operation_id: UUID identifier

          state: Mark state of operation in API Discovery

              - `review` - Mark operation as for review
              - `ignored` - Mark operation as ignored

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not operation_id:
            raise ValueError(f"Expected a non-empty value for `operation_id` but received {operation_id!r}")
        return self._patch(
            f"/zones/{zone_id}/api_gateway/discovery/operations/{operation_id}",
            body=maybe_transform({"state": state}, operation_update_params.OperationUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[OperationUpdateResponse], ResultWrapper[OperationUpdateResponse]),
        )

    def list(
        self,
        zone_id: str,
        *,
        diff: bool | NotGiven = NOT_GIVEN,
        direction: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
        endpoint: str | NotGiven = NOT_GIVEN,
        host: List[str] | NotGiven = NOT_GIVEN,
        method: List[str] | NotGiven = NOT_GIVEN,
        order: Literal["host", "method", "endpoint", "traffic_stats.requests", "traffic_stats.last_updated"]
        | NotGiven = NOT_GIVEN,
        origin: Literal["ML", "SessionIdentifier"] | NotGiven = NOT_GIVEN,
        page: object | NotGiven = NOT_GIVEN,
        per_page: object | NotGiven = NOT_GIVEN,
        state: Literal["review", "saved", "ignored"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[OperationListResponse]:
        """
        Retrieve the most up to date view of discovered operations

        Args:
          zone_id: Identifier

          diff: When `true`, only return API Discovery results that are not saved into API
              Shield Endpoint Management

          direction: Direction to order results.

          endpoint: Filter results to only include endpoints containing this pattern.

          host: Filter results to only include the specified hosts.

          method: Filter results to only include the specified HTTP methods.

          order: Field to order by

          origin: Filter results to only include discovery results sourced from a particular
              discovery engine

              - `ML` - Discovered operations that were sourced using ML API Discovery
              - `SessionIdentifier` - Discovered operations that were sourced using Session
                Identifier API Discovery

          page: Page number of paginated results.

          per_page: Maximum number of results per page.

          state: Filter results to only include discovery results in a particular state. States
              are as follows

              - `review` - Discovered operations that are not saved into API Shield Endpoint
                Management
              - `saved` - Discovered operations that are already saved into API Shield
                Endpoint Management
              - `ignored` - Discovered operations that have been marked as ignored

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._get(
            f"/zones/{zone_id}/api_gateway/discovery/operations",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "diff": diff,
                        "direction": direction,
                        "endpoint": endpoint,
                        "host": host,
                        "method": method,
                        "order": order,
                        "origin": origin,
                        "page": page,
                        "per_page": per_page,
                        "state": state,
                    },
                    operation_list_params.OperationListParams,
                ),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[OperationListResponse]], ResultWrapper[OperationListResponse]),
        )

    def delete(
        self,
        operation_id: str,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OperationDeleteResponse:
        """
        Delete an operation

        Args:
          zone_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not operation_id:
            raise ValueError(f"Expected a non-empty value for `operation_id` but received {operation_id!r}")
        return cast(
            OperationDeleteResponse,
            self._delete(
                f"/zones/{zone_id}/api_gateway/operations/{operation_id}",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[OperationDeleteResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def api_shield_endpoint_management_add_operations_to_a_zone(
        self,
        zone_id: str,
        *,
        body: Iterable[operation_api_shield_endpoint_management_add_operations_to_a_zone_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[OperationAPIShieldEndpointManagementAddOperationsToAZoneResponse]:
        """Add one or more operations to a zone.

        Endpoints can contain path variables.
        Host, method, endpoint will be normalized to a canoncial form when creating an
        operation and must be unique on the zone. Inserting an operation that matches an
        existing one will return the record of the already existing operation and update
        its last_updated date.

        Args:
          zone_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._post(
            f"/zones/{zone_id}/api_gateway/operations",
            body=maybe_transform(
                body,
                operation_api_shield_endpoint_management_add_operations_to_a_zone_params.OperationAPIShieldEndpointManagementAddOperationsToAZoneParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[OperationAPIShieldEndpointManagementAddOperationsToAZoneResponse]],
                ResultWrapper[OperationAPIShieldEndpointManagementAddOperationsToAZoneResponse],
            ),
        )

    def api_shield_endpoint_management_get_information_about_all_operations_on_a_zone(
        self,
        zone_id: str,
        *,
        direction: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
        endpoint: str | NotGiven = NOT_GIVEN,
        feature: List[Literal["thresholds", "parameter_schemas", "schema_info"]] | NotGiven = NOT_GIVEN,
        host: List[str] | NotGiven = NOT_GIVEN,
        method: List[str] | NotGiven = NOT_GIVEN,
        order: Literal["method", "host", "endpoint", "thresholds.$key"] | NotGiven = NOT_GIVEN,
        page: object | NotGiven = NOT_GIVEN,
        per_page: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[OperationAPIShieldEndpointManagementGetInformationAboutAllOperationsOnAZoneResponse]:
        """
        Retrieve information about all operations on a zone

        Args:
          zone_id: Identifier

          direction: Direction to order results.

          endpoint: Filter results to only include endpoints containing this pattern.

          feature: Add feature(s) to the results. The feature name that is given here corresponds
              to the resulting feature object. Have a look at the top-level object description
              for more details on the specific meaning.

          host: Filter results to only include the specified hosts.

          method: Filter results to only include the specified HTTP methods.

          order: Field to order by. When requesting a feature, the feature keys are available for
              ordering as well, e.g., `thresholds.suggested_threshold`.

          page: Page number of paginated results.

          per_page: Number of results to return per page

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._get(
            f"/zones/{zone_id}/api_gateway/operations",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "direction": direction,
                        "endpoint": endpoint,
                        "feature": feature,
                        "host": host,
                        "method": method,
                        "order": order,
                        "page": page,
                        "per_page": per_page,
                    },
                    operation_api_shield_endpoint_management_get_information_about_all_operations_on_a_zone_params.OperationAPIShieldEndpointManagementGetInformationAboutAllOperationsOnAZoneParams,
                ),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[OperationAPIShieldEndpointManagementGetInformationAboutAllOperationsOnAZoneResponse]],
                ResultWrapper[OperationAPIShieldEndpointManagementGetInformationAboutAllOperationsOnAZoneResponse],
            ),
        )

    def get(
        self,
        operation_id: str,
        *,
        zone_id: str,
        feature: List[Literal["thresholds", "parameter_schemas", "schema_info"]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OperationGetResponse:
        """
        Retrieve information about an operation

        Args:
          zone_id: Identifier

          feature: Add feature(s) to the results. The feature name that is given here corresponds
              to the resulting feature object. Have a look at the top-level object description
              for more details on the specific meaning.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not operation_id:
            raise ValueError(f"Expected a non-empty value for `operation_id` but received {operation_id!r}")
        return self._get(
            f"/zones/{zone_id}/api_gateway/operations/{operation_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"feature": feature}, operation_get_params.OperationGetParams),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[OperationGetResponse], ResultWrapper[OperationGetResponse]),
        )


class AsyncOperations(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncOperationsWithRawResponse:
        return AsyncOperationsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOperationsWithStreamingResponse:
        return AsyncOperationsWithStreamingResponse(self)

    async def update(
        self,
        operation_id: str,
        *,
        zone_id: str,
        state: Literal["review", "ignored"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OperationUpdateResponse:
        """
        Update the `state` on a discovered operation

        Args:
          zone_id: Identifier

          operation_id: UUID identifier

          state: Mark state of operation in API Discovery

              - `review` - Mark operation as for review
              - `ignored` - Mark operation as ignored

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not operation_id:
            raise ValueError(f"Expected a non-empty value for `operation_id` but received {operation_id!r}")
        return await self._patch(
            f"/zones/{zone_id}/api_gateway/discovery/operations/{operation_id}",
            body=maybe_transform({"state": state}, operation_update_params.OperationUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[OperationUpdateResponse], ResultWrapper[OperationUpdateResponse]),
        )

    async def list(
        self,
        zone_id: str,
        *,
        diff: bool | NotGiven = NOT_GIVEN,
        direction: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
        endpoint: str | NotGiven = NOT_GIVEN,
        host: List[str] | NotGiven = NOT_GIVEN,
        method: List[str] | NotGiven = NOT_GIVEN,
        order: Literal["host", "method", "endpoint", "traffic_stats.requests", "traffic_stats.last_updated"]
        | NotGiven = NOT_GIVEN,
        origin: Literal["ML", "SessionIdentifier"] | NotGiven = NOT_GIVEN,
        page: object | NotGiven = NOT_GIVEN,
        per_page: object | NotGiven = NOT_GIVEN,
        state: Literal["review", "saved", "ignored"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[OperationListResponse]:
        """
        Retrieve the most up to date view of discovered operations

        Args:
          zone_id: Identifier

          diff: When `true`, only return API Discovery results that are not saved into API
              Shield Endpoint Management

          direction: Direction to order results.

          endpoint: Filter results to only include endpoints containing this pattern.

          host: Filter results to only include the specified hosts.

          method: Filter results to only include the specified HTTP methods.

          order: Field to order by

          origin: Filter results to only include discovery results sourced from a particular
              discovery engine

              - `ML` - Discovered operations that were sourced using ML API Discovery
              - `SessionIdentifier` - Discovered operations that were sourced using Session
                Identifier API Discovery

          page: Page number of paginated results.

          per_page: Maximum number of results per page.

          state: Filter results to only include discovery results in a particular state. States
              are as follows

              - `review` - Discovered operations that are not saved into API Shield Endpoint
                Management
              - `saved` - Discovered operations that are already saved into API Shield
                Endpoint Management
              - `ignored` - Discovered operations that have been marked as ignored

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._get(
            f"/zones/{zone_id}/api_gateway/discovery/operations",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "diff": diff,
                        "direction": direction,
                        "endpoint": endpoint,
                        "host": host,
                        "method": method,
                        "order": order,
                        "origin": origin,
                        "page": page,
                        "per_page": per_page,
                        "state": state,
                    },
                    operation_list_params.OperationListParams,
                ),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[OperationListResponse]], ResultWrapper[OperationListResponse]),
        )

    async def delete(
        self,
        operation_id: str,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OperationDeleteResponse:
        """
        Delete an operation

        Args:
          zone_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not operation_id:
            raise ValueError(f"Expected a non-empty value for `operation_id` but received {operation_id!r}")
        return cast(
            OperationDeleteResponse,
            await self._delete(
                f"/zones/{zone_id}/api_gateway/operations/{operation_id}",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[OperationDeleteResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def api_shield_endpoint_management_add_operations_to_a_zone(
        self,
        zone_id: str,
        *,
        body: Iterable[operation_api_shield_endpoint_management_add_operations_to_a_zone_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[OperationAPIShieldEndpointManagementAddOperationsToAZoneResponse]:
        """Add one or more operations to a zone.

        Endpoints can contain path variables.
        Host, method, endpoint will be normalized to a canoncial form when creating an
        operation and must be unique on the zone. Inserting an operation that matches an
        existing one will return the record of the already existing operation and update
        its last_updated date.

        Args:
          zone_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._post(
            f"/zones/{zone_id}/api_gateway/operations",
            body=maybe_transform(
                body,
                operation_api_shield_endpoint_management_add_operations_to_a_zone_params.OperationAPIShieldEndpointManagementAddOperationsToAZoneParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[OperationAPIShieldEndpointManagementAddOperationsToAZoneResponse]],
                ResultWrapper[OperationAPIShieldEndpointManagementAddOperationsToAZoneResponse],
            ),
        )

    async def api_shield_endpoint_management_get_information_about_all_operations_on_a_zone(
        self,
        zone_id: str,
        *,
        direction: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
        endpoint: str | NotGiven = NOT_GIVEN,
        feature: List[Literal["thresholds", "parameter_schemas", "schema_info"]] | NotGiven = NOT_GIVEN,
        host: List[str] | NotGiven = NOT_GIVEN,
        method: List[str] | NotGiven = NOT_GIVEN,
        order: Literal["method", "host", "endpoint", "thresholds.$key"] | NotGiven = NOT_GIVEN,
        page: object | NotGiven = NOT_GIVEN,
        per_page: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[OperationAPIShieldEndpointManagementGetInformationAboutAllOperationsOnAZoneResponse]:
        """
        Retrieve information about all operations on a zone

        Args:
          zone_id: Identifier

          direction: Direction to order results.

          endpoint: Filter results to only include endpoints containing this pattern.

          feature: Add feature(s) to the results. The feature name that is given here corresponds
              to the resulting feature object. Have a look at the top-level object description
              for more details on the specific meaning.

          host: Filter results to only include the specified hosts.

          method: Filter results to only include the specified HTTP methods.

          order: Field to order by. When requesting a feature, the feature keys are available for
              ordering as well, e.g., `thresholds.suggested_threshold`.

          page: Page number of paginated results.

          per_page: Number of results to return per page

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._get(
            f"/zones/{zone_id}/api_gateway/operations",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "direction": direction,
                        "endpoint": endpoint,
                        "feature": feature,
                        "host": host,
                        "method": method,
                        "order": order,
                        "page": page,
                        "per_page": per_page,
                    },
                    operation_api_shield_endpoint_management_get_information_about_all_operations_on_a_zone_params.OperationAPIShieldEndpointManagementGetInformationAboutAllOperationsOnAZoneParams,
                ),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[OperationAPIShieldEndpointManagementGetInformationAboutAllOperationsOnAZoneResponse]],
                ResultWrapper[OperationAPIShieldEndpointManagementGetInformationAboutAllOperationsOnAZoneResponse],
            ),
        )

    async def get(
        self,
        operation_id: str,
        *,
        zone_id: str,
        feature: List[Literal["thresholds", "parameter_schemas", "schema_info"]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OperationGetResponse:
        """
        Retrieve information about an operation

        Args:
          zone_id: Identifier

          feature: Add feature(s) to the results. The feature name that is given here corresponds
              to the resulting feature object. Have a look at the top-level object description
              for more details on the specific meaning.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not operation_id:
            raise ValueError(f"Expected a non-empty value for `operation_id` but received {operation_id!r}")
        return await self._get(
            f"/zones/{zone_id}/api_gateway/operations/{operation_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"feature": feature}, operation_get_params.OperationGetParams),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[OperationGetResponse], ResultWrapper[OperationGetResponse]),
        )


class OperationsWithRawResponse:
    def __init__(self, operations: Operations) -> None:
        self._operations = operations

        self.update = to_raw_response_wrapper(
            operations.update,
        )
        self.list = to_raw_response_wrapper(
            operations.list,
        )
        self.delete = to_raw_response_wrapper(
            operations.delete,
        )
        self.api_shield_endpoint_management_add_operations_to_a_zone = to_raw_response_wrapper(
            operations.api_shield_endpoint_management_add_operations_to_a_zone,
        )
        self.api_shield_endpoint_management_get_information_about_all_operations_on_a_zone = to_raw_response_wrapper(
            operations.api_shield_endpoint_management_get_information_about_all_operations_on_a_zone,
        )
        self.get = to_raw_response_wrapper(
            operations.get,
        )


class AsyncOperationsWithRawResponse:
    def __init__(self, operations: AsyncOperations) -> None:
        self._operations = operations

        self.update = async_to_raw_response_wrapper(
            operations.update,
        )
        self.list = async_to_raw_response_wrapper(
            operations.list,
        )
        self.delete = async_to_raw_response_wrapper(
            operations.delete,
        )
        self.api_shield_endpoint_management_add_operations_to_a_zone = async_to_raw_response_wrapper(
            operations.api_shield_endpoint_management_add_operations_to_a_zone,
        )
        self.api_shield_endpoint_management_get_information_about_all_operations_on_a_zone = (
            async_to_raw_response_wrapper(
                operations.api_shield_endpoint_management_get_information_about_all_operations_on_a_zone,
            )
        )
        self.get = async_to_raw_response_wrapper(
            operations.get,
        )


class OperationsWithStreamingResponse:
    def __init__(self, operations: Operations) -> None:
        self._operations = operations

        self.update = to_streamed_response_wrapper(
            operations.update,
        )
        self.list = to_streamed_response_wrapper(
            operations.list,
        )
        self.delete = to_streamed_response_wrapper(
            operations.delete,
        )
        self.api_shield_endpoint_management_add_operations_to_a_zone = to_streamed_response_wrapper(
            operations.api_shield_endpoint_management_add_operations_to_a_zone,
        )
        self.api_shield_endpoint_management_get_information_about_all_operations_on_a_zone = (
            to_streamed_response_wrapper(
                operations.api_shield_endpoint_management_get_information_about_all_operations_on_a_zone,
            )
        )
        self.get = to_streamed_response_wrapper(
            operations.get,
        )


class AsyncOperationsWithStreamingResponse:
    def __init__(self, operations: AsyncOperations) -> None:
        self._operations = operations

        self.update = async_to_streamed_response_wrapper(
            operations.update,
        )
        self.list = async_to_streamed_response_wrapper(
            operations.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            operations.delete,
        )
        self.api_shield_endpoint_management_add_operations_to_a_zone = async_to_streamed_response_wrapper(
            operations.api_shield_endpoint_management_add_operations_to_a_zone,
        )
        self.api_shield_endpoint_management_get_information_about_all_operations_on_a_zone = (
            async_to_streamed_response_wrapper(
                operations.api_shield_endpoint_management_get_information_about_all_operations_on_a_zone,
            )
        )
        self.get = async_to_streamed_response_wrapper(
            operations.get,
        )
