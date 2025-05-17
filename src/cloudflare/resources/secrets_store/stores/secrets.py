# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Type, Iterable, Optional, cast
from typing_extensions import Literal

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._wrappers import ResultWrapper
from ....pagination import SyncSinglePage, AsyncSinglePage, SyncV4PagePaginationArray, AsyncV4PagePaginationArray
from ...._base_client import AsyncPaginator, make_request_options
from ....types.secrets_store.stores import (
    secret_edit_params,
    secret_list_params,
    secret_create_params,
    secret_duplicate_params,
)
from ....types.secrets_store.stores.secret_get_response import SecretGetResponse
from ....types.secrets_store.stores.secret_edit_response import SecretEditResponse
from ....types.secrets_store.stores.secret_list_response import SecretListResponse
from ....types.secrets_store.stores.secret_create_response import SecretCreateResponse
from ....types.secrets_store.stores.secret_delete_response import SecretDeleteResponse
from ....types.secrets_store.stores.secret_duplicate_response import SecretDuplicateResponse
from ....types.secrets_store.stores.secret_bulk_delete_response import SecretBulkDeleteResponse

__all__ = ["SecretsResource", "AsyncSecretsResource"]


class SecretsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SecretsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return SecretsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SecretsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return SecretsResourceWithStreamingResponse(self)

    def create(
        self,
        store_id: str,
        *,
        account_id: str,
        body: Iterable[secret_create_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncSinglePage[SecretCreateResponse]:
        """
        Creates a secret in the account

        Args:
          account_id: Account Identifier

          store_id: Store Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not store_id:
            raise ValueError(f"Expected a non-empty value for `store_id` but received {store_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/secrets_store/stores/{store_id}/secrets",
            page=SyncSinglePage[SecretCreateResponse],
            body=maybe_transform(body, Iterable[secret_create_params.Body]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=SecretCreateResponse,
            method="post",
        )

    def list(
        self,
        store_id: str,
        *,
        account_id: str,
        direction: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
        order: Literal["name", "comment", "created", "modified", "status"] | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        search: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncV4PagePaginationArray[SecretListResponse]:
        """
        Lists all store secrets

        Args:
          account_id: Account Identifier

          store_id: Store Identifier

          direction: Direction to sort objects

          order: Order secrets by values in the given field

          page: Page number

          per_page: Number of objects to return per page

          search: Search secrets using a filter string, filtering across name and comment

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not store_id:
            raise ValueError(f"Expected a non-empty value for `store_id` but received {store_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/secrets_store/stores/{store_id}/secrets",
            page=SyncV4PagePaginationArray[SecretListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "direction": direction,
                        "order": order,
                        "page": page,
                        "per_page": per_page,
                        "search": search,
                    },
                    secret_list_params.SecretListParams,
                ),
            ),
            model=SecretListResponse,
        )

    def delete(
        self,
        secret_id: str,
        *,
        account_id: str,
        store_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[SecretDeleteResponse]:
        """
        Deletes a single secret

        Args:
          account_id: Account Identifier

          store_id: Store Identifier

          secret_id: Secret identifier tag.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not store_id:
            raise ValueError(f"Expected a non-empty value for `store_id` but received {store_id!r}")
        if not secret_id:
            raise ValueError(f"Expected a non-empty value for `secret_id` but received {secret_id!r}")
        return self._delete(
            f"/accounts/{account_id}/secrets_store/stores/{store_id}/secrets/{secret_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[SecretDeleteResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[SecretDeleteResponse]], ResultWrapper[SecretDeleteResponse]),
        )

    def bulk_delete(
        self,
        store_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncSinglePage[SecretBulkDeleteResponse]:
        """
        Deletes one or more secrets

        Args:
          account_id: Account Identifier

          store_id: Store Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not store_id:
            raise ValueError(f"Expected a non-empty value for `store_id` but received {store_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/secrets_store/stores/{store_id}/secrets",
            page=SyncSinglePage[SecretBulkDeleteResponse],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=SecretBulkDeleteResponse,
            method="delete",
        )

    def duplicate(
        self,
        secret_id: str,
        *,
        account_id: str,
        store_id: str,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[SecretDuplicateResponse]:
        """
        Duplicates the secret, keeping the value

        Args:
          account_id: Account Identifier

          store_id: Store Identifier

          secret_id: Secret identifier tag.

          name: The name of the secret

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not store_id:
            raise ValueError(f"Expected a non-empty value for `store_id` but received {store_id!r}")
        if not secret_id:
            raise ValueError(f"Expected a non-empty value for `secret_id` but received {secret_id!r}")
        return self._post(
            f"/accounts/{account_id}/secrets_store/stores/{store_id}/secrets/{secret_id}/duplicate",
            body=maybe_transform({"name": name}, secret_duplicate_params.SecretDuplicateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[SecretDuplicateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[SecretDuplicateResponse]], ResultWrapper[SecretDuplicateResponse]),
        )

    def edit(
        self,
        secret_id: str,
        *,
        account_id: str,
        store_id: str,
        name: str,
        scopes: List[str] | NotGiven = NOT_GIVEN,
        value: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[SecretEditResponse]:
        """
        Updates a single secret

        Args:
          account_id: Account Identifier

          store_id: Store Identifier

          secret_id: Secret identifier tag.

          name: The name of the secret

          scopes: The list of services that can use this secret.

          value: The value of the secret. Note that this is 'write only' - no API reponse will
              provide this value, it is only used to create/modify secrets.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not store_id:
            raise ValueError(f"Expected a non-empty value for `store_id` but received {store_id!r}")
        if not secret_id:
            raise ValueError(f"Expected a non-empty value for `secret_id` but received {secret_id!r}")
        return self._patch(
            f"/accounts/{account_id}/secrets_store/stores/{store_id}/secrets/{secret_id}",
            body=maybe_transform(
                {
                    "name": name,
                    "scopes": scopes,
                    "value": value,
                },
                secret_edit_params.SecretEditParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[SecretEditResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[SecretEditResponse]], ResultWrapper[SecretEditResponse]),
        )

    def get(
        self,
        secret_id: str,
        *,
        account_id: str,
        store_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[SecretGetResponse]:
        """
        Returns details of a single secret

        Args:
          account_id: Account Identifier

          store_id: Store Identifier

          secret_id: Secret identifier tag.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not store_id:
            raise ValueError(f"Expected a non-empty value for `store_id` but received {store_id!r}")
        if not secret_id:
            raise ValueError(f"Expected a non-empty value for `secret_id` but received {secret_id!r}")
        return self._get(
            f"/accounts/{account_id}/secrets_store/stores/{store_id}/secrets/{secret_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[SecretGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[SecretGetResponse]], ResultWrapper[SecretGetResponse]),
        )


class AsyncSecretsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSecretsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSecretsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSecretsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncSecretsResourceWithStreamingResponse(self)

    def create(
        self,
        store_id: str,
        *,
        account_id: str,
        body: Iterable[secret_create_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[SecretCreateResponse, AsyncSinglePage[SecretCreateResponse]]:
        """
        Creates a secret in the account

        Args:
          account_id: Account Identifier

          store_id: Store Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not store_id:
            raise ValueError(f"Expected a non-empty value for `store_id` but received {store_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/secrets_store/stores/{store_id}/secrets",
            page=AsyncSinglePage[SecretCreateResponse],
            body=maybe_transform(body, Iterable[secret_create_params.Body]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=SecretCreateResponse,
            method="post",
        )

    def list(
        self,
        store_id: str,
        *,
        account_id: str,
        direction: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
        order: Literal["name", "comment", "created", "modified", "status"] | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        search: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[SecretListResponse, AsyncV4PagePaginationArray[SecretListResponse]]:
        """
        Lists all store secrets

        Args:
          account_id: Account Identifier

          store_id: Store Identifier

          direction: Direction to sort objects

          order: Order secrets by values in the given field

          page: Page number

          per_page: Number of objects to return per page

          search: Search secrets using a filter string, filtering across name and comment

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not store_id:
            raise ValueError(f"Expected a non-empty value for `store_id` but received {store_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/secrets_store/stores/{store_id}/secrets",
            page=AsyncV4PagePaginationArray[SecretListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "direction": direction,
                        "order": order,
                        "page": page,
                        "per_page": per_page,
                        "search": search,
                    },
                    secret_list_params.SecretListParams,
                ),
            ),
            model=SecretListResponse,
        )

    async def delete(
        self,
        secret_id: str,
        *,
        account_id: str,
        store_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[SecretDeleteResponse]:
        """
        Deletes a single secret

        Args:
          account_id: Account Identifier

          store_id: Store Identifier

          secret_id: Secret identifier tag.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not store_id:
            raise ValueError(f"Expected a non-empty value for `store_id` but received {store_id!r}")
        if not secret_id:
            raise ValueError(f"Expected a non-empty value for `secret_id` but received {secret_id!r}")
        return await self._delete(
            f"/accounts/{account_id}/secrets_store/stores/{store_id}/secrets/{secret_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[SecretDeleteResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[SecretDeleteResponse]], ResultWrapper[SecretDeleteResponse]),
        )

    def bulk_delete(
        self,
        store_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[SecretBulkDeleteResponse, AsyncSinglePage[SecretBulkDeleteResponse]]:
        """
        Deletes one or more secrets

        Args:
          account_id: Account Identifier

          store_id: Store Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not store_id:
            raise ValueError(f"Expected a non-empty value for `store_id` but received {store_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/secrets_store/stores/{store_id}/secrets",
            page=AsyncSinglePage[SecretBulkDeleteResponse],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=SecretBulkDeleteResponse,
            method="delete",
        )

    async def duplicate(
        self,
        secret_id: str,
        *,
        account_id: str,
        store_id: str,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[SecretDuplicateResponse]:
        """
        Duplicates the secret, keeping the value

        Args:
          account_id: Account Identifier

          store_id: Store Identifier

          secret_id: Secret identifier tag.

          name: The name of the secret

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not store_id:
            raise ValueError(f"Expected a non-empty value for `store_id` but received {store_id!r}")
        if not secret_id:
            raise ValueError(f"Expected a non-empty value for `secret_id` but received {secret_id!r}")
        return await self._post(
            f"/accounts/{account_id}/secrets_store/stores/{store_id}/secrets/{secret_id}/duplicate",
            body=await async_maybe_transform({"name": name}, secret_duplicate_params.SecretDuplicateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[SecretDuplicateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[SecretDuplicateResponse]], ResultWrapper[SecretDuplicateResponse]),
        )

    async def edit(
        self,
        secret_id: str,
        *,
        account_id: str,
        store_id: str,
        name: str,
        scopes: List[str] | NotGiven = NOT_GIVEN,
        value: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[SecretEditResponse]:
        """
        Updates a single secret

        Args:
          account_id: Account Identifier

          store_id: Store Identifier

          secret_id: Secret identifier tag.

          name: The name of the secret

          scopes: The list of services that can use this secret.

          value: The value of the secret. Note that this is 'write only' - no API reponse will
              provide this value, it is only used to create/modify secrets.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not store_id:
            raise ValueError(f"Expected a non-empty value for `store_id` but received {store_id!r}")
        if not secret_id:
            raise ValueError(f"Expected a non-empty value for `secret_id` but received {secret_id!r}")
        return await self._patch(
            f"/accounts/{account_id}/secrets_store/stores/{store_id}/secrets/{secret_id}",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "scopes": scopes,
                    "value": value,
                },
                secret_edit_params.SecretEditParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[SecretEditResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[SecretEditResponse]], ResultWrapper[SecretEditResponse]),
        )

    async def get(
        self,
        secret_id: str,
        *,
        account_id: str,
        store_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[SecretGetResponse]:
        """
        Returns details of a single secret

        Args:
          account_id: Account Identifier

          store_id: Store Identifier

          secret_id: Secret identifier tag.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not store_id:
            raise ValueError(f"Expected a non-empty value for `store_id` but received {store_id!r}")
        if not secret_id:
            raise ValueError(f"Expected a non-empty value for `secret_id` but received {secret_id!r}")
        return await self._get(
            f"/accounts/{account_id}/secrets_store/stores/{store_id}/secrets/{secret_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[SecretGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[SecretGetResponse]], ResultWrapper[SecretGetResponse]),
        )


class SecretsResourceWithRawResponse:
    def __init__(self, secrets: SecretsResource) -> None:
        self._secrets = secrets

        self.create = to_raw_response_wrapper(
            secrets.create,
        )
        self.list = to_raw_response_wrapper(
            secrets.list,
        )
        self.delete = to_raw_response_wrapper(
            secrets.delete,
        )
        self.bulk_delete = to_raw_response_wrapper(
            secrets.bulk_delete,
        )
        self.duplicate = to_raw_response_wrapper(
            secrets.duplicate,
        )
        self.edit = to_raw_response_wrapper(
            secrets.edit,
        )
        self.get = to_raw_response_wrapper(
            secrets.get,
        )


class AsyncSecretsResourceWithRawResponse:
    def __init__(self, secrets: AsyncSecretsResource) -> None:
        self._secrets = secrets

        self.create = async_to_raw_response_wrapper(
            secrets.create,
        )
        self.list = async_to_raw_response_wrapper(
            secrets.list,
        )
        self.delete = async_to_raw_response_wrapper(
            secrets.delete,
        )
        self.bulk_delete = async_to_raw_response_wrapper(
            secrets.bulk_delete,
        )
        self.duplicate = async_to_raw_response_wrapper(
            secrets.duplicate,
        )
        self.edit = async_to_raw_response_wrapper(
            secrets.edit,
        )
        self.get = async_to_raw_response_wrapper(
            secrets.get,
        )


class SecretsResourceWithStreamingResponse:
    def __init__(self, secrets: SecretsResource) -> None:
        self._secrets = secrets

        self.create = to_streamed_response_wrapper(
            secrets.create,
        )
        self.list = to_streamed_response_wrapper(
            secrets.list,
        )
        self.delete = to_streamed_response_wrapper(
            secrets.delete,
        )
        self.bulk_delete = to_streamed_response_wrapper(
            secrets.bulk_delete,
        )
        self.duplicate = to_streamed_response_wrapper(
            secrets.duplicate,
        )
        self.edit = to_streamed_response_wrapper(
            secrets.edit,
        )
        self.get = to_streamed_response_wrapper(
            secrets.get,
        )


class AsyncSecretsResourceWithStreamingResponse:
    def __init__(self, secrets: AsyncSecretsResource) -> None:
        self._secrets = secrets

        self.create = async_to_streamed_response_wrapper(
            secrets.create,
        )
        self.list = async_to_streamed_response_wrapper(
            secrets.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            secrets.delete,
        )
        self.bulk_delete = async_to_streamed_response_wrapper(
            secrets.bulk_delete,
        )
        self.duplicate = async_to_streamed_response_wrapper(
            secrets.duplicate,
        )
        self.edit = async_to_streamed_response_wrapper(
            secrets.edit,
        )
        self.get = async_to_streamed_response_wrapper(
            secrets.get,
        )
