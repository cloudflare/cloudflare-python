# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, cast
from typing_extensions import Literal

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import (
    maybe_transform,
    strip_not_given,
    async_maybe_transform,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._wrappers import ResultWrapper
from ....pagination import SyncSinglePage, AsyncSinglePage
from ...._base_client import AsyncPaginator, make_request_options
from .prebuilt_policies import (
    PrebuiltPoliciesResource,
    AsyncPrebuiltPoliciesResource,
    PrebuiltPoliciesResourceWithRawResponse,
    AsyncPrebuiltPoliciesResourceWithRawResponse,
    PrebuiltPoliciesResourceWithStreamingResponse,
    AsyncPrebuiltPoliciesResourceWithStreamingResponse,
)
from ....types.magic_cloud_networking import (
    catalog_sync_edit_params,
    catalog_sync_create_params,
    catalog_sync_delete_params,
    catalog_sync_update_params,
)
from ....types.magic_cloud_networking.catalog_sync_get_response import CatalogSyncGetResponse
from ....types.magic_cloud_networking.catalog_sync_edit_response import CatalogSyncEditResponse
from ....types.magic_cloud_networking.catalog_sync_list_response import CatalogSyncListResponse
from ....types.magic_cloud_networking.catalog_sync_create_response import CatalogSyncCreateResponse
from ....types.magic_cloud_networking.catalog_sync_delete_response import CatalogSyncDeleteResponse
from ....types.magic_cloud_networking.catalog_sync_update_response import CatalogSyncUpdateResponse
from ....types.magic_cloud_networking.catalog_sync_refresh_response import CatalogSyncRefreshResponse

__all__ = ["CatalogSyncsResource", "AsyncCatalogSyncsResource"]


class CatalogSyncsResource(SyncAPIResource):
    @cached_property
    def prebuilt_policies(self) -> PrebuiltPoliciesResource:
        return PrebuiltPoliciesResource(self._client)

    @cached_property
    def with_raw_response(self) -> CatalogSyncsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return CatalogSyncsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CatalogSyncsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return CatalogSyncsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        account_id: str,
        destination_type: Literal["NONE", "ZERO_TRUST_LIST"],
        name: str,
        update_mode: Literal["AUTO", "MANUAL"],
        description: str | NotGiven = NOT_GIVEN,
        policy: str | NotGiven = NOT_GIVEN,
        forwarded: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CatalogSyncCreateResponse:
        """
        Create a new Catalog Sync (Closed Beta)

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
            f"/accounts/{account_id}/magic/cloud/catalog-syncs",
            body=maybe_transform(
                {
                    "destination_type": destination_type,
                    "name": name,
                    "update_mode": update_mode,
                    "description": description,
                    "policy": policy,
                },
                catalog_sync_create_params.CatalogSyncCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[CatalogSyncCreateResponse]._unwrapper,
            ),
            cast_to=cast(Type[CatalogSyncCreateResponse], ResultWrapper[CatalogSyncCreateResponse]),
        )

    def update(
        self,
        sync_id: str,
        *,
        account_id: str,
        description: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        policy: str | NotGiven = NOT_GIVEN,
        update_mode: Literal["AUTO", "MANUAL"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CatalogSyncUpdateResponse:
        """
        Update a Catalog Sync (Closed Beta)

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not sync_id:
            raise ValueError(f"Expected a non-empty value for `sync_id` but received {sync_id!r}")
        return self._put(
            f"/accounts/{account_id}/magic/cloud/catalog-syncs/{sync_id}",
            body=maybe_transform(
                {
                    "description": description,
                    "name": name,
                    "policy": policy,
                    "update_mode": update_mode,
                },
                catalog_sync_update_params.CatalogSyncUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[CatalogSyncUpdateResponse]._unwrapper,
            ),
            cast_to=cast(Type[CatalogSyncUpdateResponse], ResultWrapper[CatalogSyncUpdateResponse]),
        )

    def list(
        self,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncSinglePage[CatalogSyncListResponse]:
        """
        List Catalog Syncs (Closed Beta)

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/magic/cloud/catalog-syncs",
            page=SyncSinglePage[CatalogSyncListResponse],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=CatalogSyncListResponse,
        )

    def delete(
        self,
        sync_id: str,
        *,
        account_id: str,
        delete_destination: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CatalogSyncDeleteResponse:
        """
        Delete a Catalog Sync (Closed Beta)

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not sync_id:
            raise ValueError(f"Expected a non-empty value for `sync_id` but received {sync_id!r}")
        return self._delete(
            f"/accounts/{account_id}/magic/cloud/catalog-syncs/{sync_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"delete_destination": delete_destination}, catalog_sync_delete_params.CatalogSyncDeleteParams
                ),
                post_parser=ResultWrapper[CatalogSyncDeleteResponse]._unwrapper,
            ),
            cast_to=cast(Type[CatalogSyncDeleteResponse], ResultWrapper[CatalogSyncDeleteResponse]),
        )

    def edit(
        self,
        sync_id: str,
        *,
        account_id: str,
        description: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        policy: str | NotGiven = NOT_GIVEN,
        update_mode: Literal["AUTO", "MANUAL"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CatalogSyncEditResponse:
        """
        Update a Catalog Sync (Closed Beta)

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not sync_id:
            raise ValueError(f"Expected a non-empty value for `sync_id` but received {sync_id!r}")
        return self._patch(
            f"/accounts/{account_id}/magic/cloud/catalog-syncs/{sync_id}",
            body=maybe_transform(
                {
                    "description": description,
                    "name": name,
                    "policy": policy,
                    "update_mode": update_mode,
                },
                catalog_sync_edit_params.CatalogSyncEditParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[CatalogSyncEditResponse]._unwrapper,
            ),
            cast_to=cast(Type[CatalogSyncEditResponse], ResultWrapper[CatalogSyncEditResponse]),
        )

    def get(
        self,
        sync_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CatalogSyncGetResponse:
        """
        Read a Catalog Sync (Closed Beta)

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not sync_id:
            raise ValueError(f"Expected a non-empty value for `sync_id` but received {sync_id!r}")
        return self._get(
            f"/accounts/{account_id}/magic/cloud/catalog-syncs/{sync_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[CatalogSyncGetResponse]._unwrapper,
            ),
            cast_to=cast(Type[CatalogSyncGetResponse], ResultWrapper[CatalogSyncGetResponse]),
        )

    def refresh(
        self,
        sync_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> str:
        """
        Refresh a Catalog Sync's destination by running the sync policy against latest
        resource catalog (Closed Beta)

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not sync_id:
            raise ValueError(f"Expected a non-empty value for `sync_id` but received {sync_id!r}")
        return self._post(
            f"/accounts/{account_id}/magic/cloud/catalog-syncs/{sync_id}/refresh",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[CatalogSyncRefreshResponse]._unwrapper,
            ),
            cast_to=cast(Type[str], ResultWrapper[str]),
        )


class AsyncCatalogSyncsResource(AsyncAPIResource):
    @cached_property
    def prebuilt_policies(self) -> AsyncPrebuiltPoliciesResource:
        return AsyncPrebuiltPoliciesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncCatalogSyncsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCatalogSyncsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCatalogSyncsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncCatalogSyncsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_id: str,
        destination_type: Literal["NONE", "ZERO_TRUST_LIST"],
        name: str,
        update_mode: Literal["AUTO", "MANUAL"],
        description: str | NotGiven = NOT_GIVEN,
        policy: str | NotGiven = NOT_GIVEN,
        forwarded: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CatalogSyncCreateResponse:
        """
        Create a new Catalog Sync (Closed Beta)

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
            f"/accounts/{account_id}/magic/cloud/catalog-syncs",
            body=await async_maybe_transform(
                {
                    "destination_type": destination_type,
                    "name": name,
                    "update_mode": update_mode,
                    "description": description,
                    "policy": policy,
                },
                catalog_sync_create_params.CatalogSyncCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[CatalogSyncCreateResponse]._unwrapper,
            ),
            cast_to=cast(Type[CatalogSyncCreateResponse], ResultWrapper[CatalogSyncCreateResponse]),
        )

    async def update(
        self,
        sync_id: str,
        *,
        account_id: str,
        description: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        policy: str | NotGiven = NOT_GIVEN,
        update_mode: Literal["AUTO", "MANUAL"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CatalogSyncUpdateResponse:
        """
        Update a Catalog Sync (Closed Beta)

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not sync_id:
            raise ValueError(f"Expected a non-empty value for `sync_id` but received {sync_id!r}")
        return await self._put(
            f"/accounts/{account_id}/magic/cloud/catalog-syncs/{sync_id}",
            body=await async_maybe_transform(
                {
                    "description": description,
                    "name": name,
                    "policy": policy,
                    "update_mode": update_mode,
                },
                catalog_sync_update_params.CatalogSyncUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[CatalogSyncUpdateResponse]._unwrapper,
            ),
            cast_to=cast(Type[CatalogSyncUpdateResponse], ResultWrapper[CatalogSyncUpdateResponse]),
        )

    def list(
        self,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[CatalogSyncListResponse, AsyncSinglePage[CatalogSyncListResponse]]:
        """
        List Catalog Syncs (Closed Beta)

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/magic/cloud/catalog-syncs",
            page=AsyncSinglePage[CatalogSyncListResponse],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=CatalogSyncListResponse,
        )

    async def delete(
        self,
        sync_id: str,
        *,
        account_id: str,
        delete_destination: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CatalogSyncDeleteResponse:
        """
        Delete a Catalog Sync (Closed Beta)

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not sync_id:
            raise ValueError(f"Expected a non-empty value for `sync_id` but received {sync_id!r}")
        return await self._delete(
            f"/accounts/{account_id}/magic/cloud/catalog-syncs/{sync_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"delete_destination": delete_destination}, catalog_sync_delete_params.CatalogSyncDeleteParams
                ),
                post_parser=ResultWrapper[CatalogSyncDeleteResponse]._unwrapper,
            ),
            cast_to=cast(Type[CatalogSyncDeleteResponse], ResultWrapper[CatalogSyncDeleteResponse]),
        )

    async def edit(
        self,
        sync_id: str,
        *,
        account_id: str,
        description: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        policy: str | NotGiven = NOT_GIVEN,
        update_mode: Literal["AUTO", "MANUAL"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CatalogSyncEditResponse:
        """
        Update a Catalog Sync (Closed Beta)

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not sync_id:
            raise ValueError(f"Expected a non-empty value for `sync_id` but received {sync_id!r}")
        return await self._patch(
            f"/accounts/{account_id}/magic/cloud/catalog-syncs/{sync_id}",
            body=await async_maybe_transform(
                {
                    "description": description,
                    "name": name,
                    "policy": policy,
                    "update_mode": update_mode,
                },
                catalog_sync_edit_params.CatalogSyncEditParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[CatalogSyncEditResponse]._unwrapper,
            ),
            cast_to=cast(Type[CatalogSyncEditResponse], ResultWrapper[CatalogSyncEditResponse]),
        )

    async def get(
        self,
        sync_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CatalogSyncGetResponse:
        """
        Read a Catalog Sync (Closed Beta)

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not sync_id:
            raise ValueError(f"Expected a non-empty value for `sync_id` but received {sync_id!r}")
        return await self._get(
            f"/accounts/{account_id}/magic/cloud/catalog-syncs/{sync_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[CatalogSyncGetResponse]._unwrapper,
            ),
            cast_to=cast(Type[CatalogSyncGetResponse], ResultWrapper[CatalogSyncGetResponse]),
        )

    async def refresh(
        self,
        sync_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> str:
        """
        Refresh a Catalog Sync's destination by running the sync policy against latest
        resource catalog (Closed Beta)

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not sync_id:
            raise ValueError(f"Expected a non-empty value for `sync_id` but received {sync_id!r}")
        return await self._post(
            f"/accounts/{account_id}/magic/cloud/catalog-syncs/{sync_id}/refresh",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[CatalogSyncRefreshResponse]._unwrapper,
            ),
            cast_to=cast(Type[str], ResultWrapper[str]),
        )


class CatalogSyncsResourceWithRawResponse:
    def __init__(self, catalog_syncs: CatalogSyncsResource) -> None:
        self._catalog_syncs = catalog_syncs

        self.create = to_raw_response_wrapper(
            catalog_syncs.create,
        )
        self.update = to_raw_response_wrapper(
            catalog_syncs.update,
        )
        self.list = to_raw_response_wrapper(
            catalog_syncs.list,
        )
        self.delete = to_raw_response_wrapper(
            catalog_syncs.delete,
        )
        self.edit = to_raw_response_wrapper(
            catalog_syncs.edit,
        )
        self.get = to_raw_response_wrapper(
            catalog_syncs.get,
        )
        self.refresh = to_raw_response_wrapper(
            catalog_syncs.refresh,
        )

    @cached_property
    def prebuilt_policies(self) -> PrebuiltPoliciesResourceWithRawResponse:
        return PrebuiltPoliciesResourceWithRawResponse(self._catalog_syncs.prebuilt_policies)


class AsyncCatalogSyncsResourceWithRawResponse:
    def __init__(self, catalog_syncs: AsyncCatalogSyncsResource) -> None:
        self._catalog_syncs = catalog_syncs

        self.create = async_to_raw_response_wrapper(
            catalog_syncs.create,
        )
        self.update = async_to_raw_response_wrapper(
            catalog_syncs.update,
        )
        self.list = async_to_raw_response_wrapper(
            catalog_syncs.list,
        )
        self.delete = async_to_raw_response_wrapper(
            catalog_syncs.delete,
        )
        self.edit = async_to_raw_response_wrapper(
            catalog_syncs.edit,
        )
        self.get = async_to_raw_response_wrapper(
            catalog_syncs.get,
        )
        self.refresh = async_to_raw_response_wrapper(
            catalog_syncs.refresh,
        )

    @cached_property
    def prebuilt_policies(self) -> AsyncPrebuiltPoliciesResourceWithRawResponse:
        return AsyncPrebuiltPoliciesResourceWithRawResponse(self._catalog_syncs.prebuilt_policies)


class CatalogSyncsResourceWithStreamingResponse:
    def __init__(self, catalog_syncs: CatalogSyncsResource) -> None:
        self._catalog_syncs = catalog_syncs

        self.create = to_streamed_response_wrapper(
            catalog_syncs.create,
        )
        self.update = to_streamed_response_wrapper(
            catalog_syncs.update,
        )
        self.list = to_streamed_response_wrapper(
            catalog_syncs.list,
        )
        self.delete = to_streamed_response_wrapper(
            catalog_syncs.delete,
        )
        self.edit = to_streamed_response_wrapper(
            catalog_syncs.edit,
        )
        self.get = to_streamed_response_wrapper(
            catalog_syncs.get,
        )
        self.refresh = to_streamed_response_wrapper(
            catalog_syncs.refresh,
        )

    @cached_property
    def prebuilt_policies(self) -> PrebuiltPoliciesResourceWithStreamingResponse:
        return PrebuiltPoliciesResourceWithStreamingResponse(self._catalog_syncs.prebuilt_policies)


class AsyncCatalogSyncsResourceWithStreamingResponse:
    def __init__(self, catalog_syncs: AsyncCatalogSyncsResource) -> None:
        self._catalog_syncs = catalog_syncs

        self.create = async_to_streamed_response_wrapper(
            catalog_syncs.create,
        )
        self.update = async_to_streamed_response_wrapper(
            catalog_syncs.update,
        )
        self.list = async_to_streamed_response_wrapper(
            catalog_syncs.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            catalog_syncs.delete,
        )
        self.edit = async_to_streamed_response_wrapper(
            catalog_syncs.edit,
        )
        self.get = async_to_streamed_response_wrapper(
            catalog_syncs.get,
        )
        self.refresh = async_to_streamed_response_wrapper(
            catalog_syncs.refresh,
        )

    @cached_property
    def prebuilt_policies(self) -> AsyncPrebuiltPoliciesResourceWithStreamingResponse:
        return AsyncPrebuiltPoliciesResourceWithStreamingResponse(self._catalog_syncs.prebuilt_policies)
