# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Optional, cast

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._wrappers import ResultWrapper
from ...types.acm import custom_trust_store_list_params, custom_trust_store_create_params
from ...pagination import SyncV4PagePaginationArray, AsyncV4PagePaginationArray
from ..._base_client import AsyncPaginator, make_request_options
from ...types.acm.custom_trust_store import CustomTrustStore
from ...types.acm.custom_trust_store_delete_response import CustomTrustStoreDeleteResponse

__all__ = ["CustomTrustStoreResource", "AsyncCustomTrustStoreResource"]


class CustomTrustStoreResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CustomTrustStoreResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return CustomTrustStoreResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CustomTrustStoreResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return CustomTrustStoreResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        zone_id: str | None = None,
        certificate: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[CustomTrustStore]:
        """
        Add Custom Origin Trust Store for a Zone.

        Args:
          zone_id: Identifier.

          certificate: The zone's SSL certificate or certificate and the intermediate(s).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if zone_id is None:
            zone_id = self._client._get_zone_id_path_param()
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._post(
            path_template("/zones/{zone_id}/acm/custom_trust_store", zone_id=zone_id),
            body=maybe_transform(
                {"certificate": certificate}, custom_trust_store_create_params.CustomTrustStoreCreateParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[CustomTrustStore]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[CustomTrustStore]], ResultWrapper[CustomTrustStore]),
        )

    def list(
        self,
        *,
        zone_id: str | None = None,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        page: float | Omit = omit,
        per_page: float | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncV4PagePaginationArray[CustomTrustStore]:
        """
        Get Custom Origin Trust Store for a Zone.

        Args:
          zone_id: Identifier.

          limit: Limit to the number of records returned.

          offset: Offset the results

          page: Page number of paginated results.

          per_page: Number of records per page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if zone_id is None:
            zone_id = self._client._get_zone_id_path_param()
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._get_api_list(
            path_template("/zones/{zone_id}/acm/custom_trust_store", zone_id=zone_id),
            page=SyncV4PagePaginationArray[CustomTrustStore],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "offset": offset,
                        "page": page,
                        "per_page": per_page,
                    },
                    custom_trust_store_list_params.CustomTrustStoreListParams,
                ),
            ),
            model=CustomTrustStore,
        )

    def delete(
        self,
        custom_origin_trust_store_id: str,
        *,
        zone_id: str | None = None,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[CustomTrustStoreDeleteResponse]:
        """Removes a CA certificate from the custom origin trust store.

        Origins using
        certificates signed by this CA will no longer be trusted.

        Args:
          zone_id: Identifier.

          custom_origin_trust_store_id: Identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if zone_id is None:
            zone_id = self._client._get_zone_id_path_param()
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not custom_origin_trust_store_id:
            raise ValueError(
                f"Expected a non-empty value for `custom_origin_trust_store_id` but received {custom_origin_trust_store_id!r}"
            )
        return self._delete(
            path_template(
                "/zones/{zone_id}/acm/custom_trust_store/{custom_origin_trust_store_id}",
                zone_id=zone_id,
                custom_origin_trust_store_id=custom_origin_trust_store_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[CustomTrustStoreDeleteResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[CustomTrustStoreDeleteResponse]], ResultWrapper[CustomTrustStoreDeleteResponse]),
        )

    def get(
        self,
        custom_origin_trust_store_id: str,
        *,
        zone_id: str | None = None,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[CustomTrustStore]:
        """
        Retrieves details about a specific certificate in the custom origin trust store,
        including expiration and subject information.

        Args:
          zone_id: Identifier.

          custom_origin_trust_store_id: Identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if zone_id is None:
            zone_id = self._client._get_zone_id_path_param()
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not custom_origin_trust_store_id:
            raise ValueError(
                f"Expected a non-empty value for `custom_origin_trust_store_id` but received {custom_origin_trust_store_id!r}"
            )
        return self._get(
            path_template(
                "/zones/{zone_id}/acm/custom_trust_store/{custom_origin_trust_store_id}",
                zone_id=zone_id,
                custom_origin_trust_store_id=custom_origin_trust_store_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[CustomTrustStore]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[CustomTrustStore]], ResultWrapper[CustomTrustStore]),
        )


class AsyncCustomTrustStoreResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCustomTrustStoreResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCustomTrustStoreResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCustomTrustStoreResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncCustomTrustStoreResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        zone_id: str | None = None,
        certificate: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[CustomTrustStore]:
        """
        Add Custom Origin Trust Store for a Zone.

        Args:
          zone_id: Identifier.

          certificate: The zone's SSL certificate or certificate and the intermediate(s).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if zone_id is None:
            zone_id = self._client._get_zone_id_path_param()
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._post(
            path_template("/zones/{zone_id}/acm/custom_trust_store", zone_id=zone_id),
            body=await async_maybe_transform(
                {"certificate": certificate}, custom_trust_store_create_params.CustomTrustStoreCreateParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[CustomTrustStore]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[CustomTrustStore]], ResultWrapper[CustomTrustStore]),
        )

    def list(
        self,
        *,
        zone_id: str | None = None,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        page: float | Omit = omit,
        per_page: float | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[CustomTrustStore, AsyncV4PagePaginationArray[CustomTrustStore]]:
        """
        Get Custom Origin Trust Store for a Zone.

        Args:
          zone_id: Identifier.

          limit: Limit to the number of records returned.

          offset: Offset the results

          page: Page number of paginated results.

          per_page: Number of records per page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if zone_id is None:
            zone_id = self._client._get_zone_id_path_param()
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._get_api_list(
            path_template("/zones/{zone_id}/acm/custom_trust_store", zone_id=zone_id),
            page=AsyncV4PagePaginationArray[CustomTrustStore],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "offset": offset,
                        "page": page,
                        "per_page": per_page,
                    },
                    custom_trust_store_list_params.CustomTrustStoreListParams,
                ),
            ),
            model=CustomTrustStore,
        )

    async def delete(
        self,
        custom_origin_trust_store_id: str,
        *,
        zone_id: str | None = None,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[CustomTrustStoreDeleteResponse]:
        """Removes a CA certificate from the custom origin trust store.

        Origins using
        certificates signed by this CA will no longer be trusted.

        Args:
          zone_id: Identifier.

          custom_origin_trust_store_id: Identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if zone_id is None:
            zone_id = self._client._get_zone_id_path_param()
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not custom_origin_trust_store_id:
            raise ValueError(
                f"Expected a non-empty value for `custom_origin_trust_store_id` but received {custom_origin_trust_store_id!r}"
            )
        return await self._delete(
            path_template(
                "/zones/{zone_id}/acm/custom_trust_store/{custom_origin_trust_store_id}",
                zone_id=zone_id,
                custom_origin_trust_store_id=custom_origin_trust_store_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[CustomTrustStoreDeleteResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[CustomTrustStoreDeleteResponse]], ResultWrapper[CustomTrustStoreDeleteResponse]),
        )

    async def get(
        self,
        custom_origin_trust_store_id: str,
        *,
        zone_id: str | None = None,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[CustomTrustStore]:
        """
        Retrieves details about a specific certificate in the custom origin trust store,
        including expiration and subject information.

        Args:
          zone_id: Identifier.

          custom_origin_trust_store_id: Identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if zone_id is None:
            zone_id = self._client._get_zone_id_path_param()
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not custom_origin_trust_store_id:
            raise ValueError(
                f"Expected a non-empty value for `custom_origin_trust_store_id` but received {custom_origin_trust_store_id!r}"
            )
        return await self._get(
            path_template(
                "/zones/{zone_id}/acm/custom_trust_store/{custom_origin_trust_store_id}",
                zone_id=zone_id,
                custom_origin_trust_store_id=custom_origin_trust_store_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[CustomTrustStore]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[CustomTrustStore]], ResultWrapper[CustomTrustStore]),
        )


class CustomTrustStoreResourceWithRawResponse:
    def __init__(self, custom_trust_store: CustomTrustStoreResource) -> None:
        self._custom_trust_store = custom_trust_store

        self.create = to_raw_response_wrapper(
            custom_trust_store.create,
        )
        self.list = to_raw_response_wrapper(
            custom_trust_store.list,
        )
        self.delete = to_raw_response_wrapper(
            custom_trust_store.delete,
        )
        self.get = to_raw_response_wrapper(
            custom_trust_store.get,
        )


class AsyncCustomTrustStoreResourceWithRawResponse:
    def __init__(self, custom_trust_store: AsyncCustomTrustStoreResource) -> None:
        self._custom_trust_store = custom_trust_store

        self.create = async_to_raw_response_wrapper(
            custom_trust_store.create,
        )
        self.list = async_to_raw_response_wrapper(
            custom_trust_store.list,
        )
        self.delete = async_to_raw_response_wrapper(
            custom_trust_store.delete,
        )
        self.get = async_to_raw_response_wrapper(
            custom_trust_store.get,
        )


class CustomTrustStoreResourceWithStreamingResponse:
    def __init__(self, custom_trust_store: CustomTrustStoreResource) -> None:
        self._custom_trust_store = custom_trust_store

        self.create = to_streamed_response_wrapper(
            custom_trust_store.create,
        )
        self.list = to_streamed_response_wrapper(
            custom_trust_store.list,
        )
        self.delete = to_streamed_response_wrapper(
            custom_trust_store.delete,
        )
        self.get = to_streamed_response_wrapper(
            custom_trust_store.get,
        )


class AsyncCustomTrustStoreResourceWithStreamingResponse:
    def __init__(self, custom_trust_store: AsyncCustomTrustStoreResource) -> None:
        self._custom_trust_store = custom_trust_store

        self.create = async_to_streamed_response_wrapper(
            custom_trust_store.create,
        )
        self.list = async_to_streamed_response_wrapper(
            custom_trust_store.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            custom_trust_store.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            custom_trust_store.get,
        )
