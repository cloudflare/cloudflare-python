# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Optional, cast
from typing_extensions import Literal

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ...._utils import path_template, maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._wrappers import ResultWrapper
from ....pagination import SyncV4PagePaginationArray, AsyncV4PagePaginationArray
from ...._base_client import AsyncPaginator, make_request_options
from ....types.email_security.settings import (
    impersonation_registry_edit_params,
    impersonation_registry_list_params,
    impersonation_registry_create_params,
)
from ....types.email_security.settings.impersonation_registry_get_response import ImpersonationRegistryGetResponse
from ....types.email_security.settings.impersonation_registry_edit_response import ImpersonationRegistryEditResponse
from ....types.email_security.settings.impersonation_registry_list_response import ImpersonationRegistryListResponse
from ....types.email_security.settings.impersonation_registry_create_response import ImpersonationRegistryCreateResponse
from ....types.email_security.settings.impersonation_registry_delete_response import ImpersonationRegistryDeleteResponse

__all__ = ["ImpersonationRegistryResource", "AsyncImpersonationRegistryResource"]


class ImpersonationRegistryResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ImpersonationRegistryResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return ImpersonationRegistryResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ImpersonationRegistryResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return ImpersonationRegistryResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        account_id: str,
        email: str,
        is_email_regex: bool,
        name: str,
        comments: Optional[str] | Omit = omit,
        directory_id: Optional[int] | Omit = omit,
        directory_node_id: Optional[int] | Omit = omit,
        external_directory_node_id: Optional[str] | Omit = omit,
        provenance: Literal["A1S_INTERNAL", "SNOOPY-CASB_OFFICE_365", "SNOOPY-OFFICE_365", "SNOOPY-GOOGLE_DIRECTORY"]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[ImpersonationRegistryCreateResponse]:
        """
        Creates a new entry in the impersonation registry to protect against
        impersonation. Emails attempting to impersonate this identity will be flagged.
        Supports regex patterns for flexible email matching.

        Args:
          account_id: Identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._post(
            path_template(
                "/accounts/{account_id}/email-security/settings/impersonation_registry", account_id=account_id
            ),
            body=maybe_transform(
                {
                    "email": email,
                    "is_email_regex": is_email_regex,
                    "name": name,
                    "comments": comments,
                    "directory_id": directory_id,
                    "directory_node_id": directory_node_id,
                    "external_directory_node_id": external_directory_node_id,
                    "provenance": provenance,
                },
                impersonation_registry_create_params.ImpersonationRegistryCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[ImpersonationRegistryCreateResponse]]._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[ImpersonationRegistryCreateResponse]], ResultWrapper[ImpersonationRegistryCreateResponse]
            ),
        )

    def list(
        self,
        *,
        account_id: str,
        direction: Literal["asc", "desc"] | Omit = omit,
        order: Literal["name", "email", "created_at"] | Omit = omit,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        provenance: Literal["A1S_INTERNAL", "SNOOPY-CASB_OFFICE_365", "SNOOPY-OFFICE_365", "SNOOPY-GOOGLE_DIRECTORY"]
        | Omit = omit,
        search: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncV4PagePaginationArray[ImpersonationRegistryListResponse]:
        """
        Returns a paginated list of protected identities in the impersonation registry.
        These entries define identities and email addresses to protect from
        impersonation attacks. Can be manually added or automatically synced from
        directory integrations.

        Args:
          account_id: Identifier.

          direction: The sorting direction.

          order: Field to sort by.

          page: Current page within paginated list of results.

          per_page: The number of results per page. Maximum value is 1000.

          search: Search term for filtering records. Behavior may change.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            path_template(
                "/accounts/{account_id}/email-security/settings/impersonation_registry", account_id=account_id
            ),
            page=SyncV4PagePaginationArray[ImpersonationRegistryListResponse],
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
                        "provenance": provenance,
                        "search": search,
                    },
                    impersonation_registry_list_params.ImpersonationRegistryListParams,
                ),
            ),
            model=ImpersonationRegistryListResponse,
        )

    def delete(
        self,
        impersonation_registry_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[ImpersonationRegistryDeleteResponse]:
        """Removes an entry from the impersonation registry.

        After deletion, this identity
        will no longer be protected from impersonation.

        Args:
          account_id: Identifier.

          impersonation_registry_id: Impersonation registry entry identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not impersonation_registry_id:
            raise ValueError(
                f"Expected a non-empty value for `impersonation_registry_id` but received {impersonation_registry_id!r}"
            )
        return self._delete(
            path_template(
                "/accounts/{account_id}/email-security/settings/impersonation_registry/{impersonation_registry_id}",
                account_id=account_id,
                impersonation_registry_id=impersonation_registry_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[ImpersonationRegistryDeleteResponse]]._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[ImpersonationRegistryDeleteResponse]], ResultWrapper[ImpersonationRegistryDeleteResponse]
            ),
        )

    def edit(
        self,
        impersonation_registry_id: str,
        *,
        account_id: str,
        comments: Optional[str] | Omit = omit,
        directory_id: Optional[int] | Omit = omit,
        directory_node_id: Optional[int] | Omit = omit,
        email: str | Omit = omit,
        external_directory_node_id: Optional[str] | Omit = omit,
        is_email_regex: bool | Omit = omit,
        name: str | Omit = omit,
        provenance: Literal["A1S_INTERNAL", "SNOOPY-CASB_OFFICE_365", "SNOOPY-OFFICE_365", "SNOOPY-GOOGLE_DIRECTORY"]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[ImpersonationRegistryEditResponse]:
        """Updates an existing impersonation registry entry.

        Only provided fields will be
        modified. Directory-synced entries can't be updated.

        Args:
          account_id: Identifier.

          impersonation_registry_id: Impersonation registry entry identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not impersonation_registry_id:
            raise ValueError(
                f"Expected a non-empty value for `impersonation_registry_id` but received {impersonation_registry_id!r}"
            )
        return self._patch(
            path_template(
                "/accounts/{account_id}/email-security/settings/impersonation_registry/{impersonation_registry_id}",
                account_id=account_id,
                impersonation_registry_id=impersonation_registry_id,
            ),
            body=maybe_transform(
                {
                    "comments": comments,
                    "directory_id": directory_id,
                    "directory_node_id": directory_node_id,
                    "email": email,
                    "external_directory_node_id": external_directory_node_id,
                    "is_email_regex": is_email_regex,
                    "name": name,
                    "provenance": provenance,
                },
                impersonation_registry_edit_params.ImpersonationRegistryEditParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[ImpersonationRegistryEditResponse]]._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[ImpersonationRegistryEditResponse]], ResultWrapper[ImpersonationRegistryEditResponse]
            ),
        )

    def get(
        self,
        impersonation_registry_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[ImpersonationRegistryGetResponse]:
        """
        Retrieves details for a specific impersonation registry entry including the
        protected identity, email pattern, and synchronization source if
        directory-synced.

        Args:
          account_id: Identifier.

          impersonation_registry_id: Impersonation registry entry identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not impersonation_registry_id:
            raise ValueError(
                f"Expected a non-empty value for `impersonation_registry_id` but received {impersonation_registry_id!r}"
            )
        return self._get(
            path_template(
                "/accounts/{account_id}/email-security/settings/impersonation_registry/{impersonation_registry_id}",
                account_id=account_id,
                impersonation_registry_id=impersonation_registry_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[ImpersonationRegistryGetResponse]]._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[ImpersonationRegistryGetResponse]], ResultWrapper[ImpersonationRegistryGetResponse]
            ),
        )


class AsyncImpersonationRegistryResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncImpersonationRegistryResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncImpersonationRegistryResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncImpersonationRegistryResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncImpersonationRegistryResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_id: str,
        email: str,
        is_email_regex: bool,
        name: str,
        comments: Optional[str] | Omit = omit,
        directory_id: Optional[int] | Omit = omit,
        directory_node_id: Optional[int] | Omit = omit,
        external_directory_node_id: Optional[str] | Omit = omit,
        provenance: Literal["A1S_INTERNAL", "SNOOPY-CASB_OFFICE_365", "SNOOPY-OFFICE_365", "SNOOPY-GOOGLE_DIRECTORY"]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[ImpersonationRegistryCreateResponse]:
        """
        Creates a new entry in the impersonation registry to protect against
        impersonation. Emails attempting to impersonate this identity will be flagged.
        Supports regex patterns for flexible email matching.

        Args:
          account_id: Identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._post(
            path_template(
                "/accounts/{account_id}/email-security/settings/impersonation_registry", account_id=account_id
            ),
            body=await async_maybe_transform(
                {
                    "email": email,
                    "is_email_regex": is_email_regex,
                    "name": name,
                    "comments": comments,
                    "directory_id": directory_id,
                    "directory_node_id": directory_node_id,
                    "external_directory_node_id": external_directory_node_id,
                    "provenance": provenance,
                },
                impersonation_registry_create_params.ImpersonationRegistryCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[ImpersonationRegistryCreateResponse]]._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[ImpersonationRegistryCreateResponse]], ResultWrapper[ImpersonationRegistryCreateResponse]
            ),
        )

    def list(
        self,
        *,
        account_id: str,
        direction: Literal["asc", "desc"] | Omit = omit,
        order: Literal["name", "email", "created_at"] | Omit = omit,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        provenance: Literal["A1S_INTERNAL", "SNOOPY-CASB_OFFICE_365", "SNOOPY-OFFICE_365", "SNOOPY-GOOGLE_DIRECTORY"]
        | Omit = omit,
        search: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[
        ImpersonationRegistryListResponse, AsyncV4PagePaginationArray[ImpersonationRegistryListResponse]
    ]:
        """
        Returns a paginated list of protected identities in the impersonation registry.
        These entries define identities and email addresses to protect from
        impersonation attacks. Can be manually added or automatically synced from
        directory integrations.

        Args:
          account_id: Identifier.

          direction: The sorting direction.

          order: Field to sort by.

          page: Current page within paginated list of results.

          per_page: The number of results per page. Maximum value is 1000.

          search: Search term for filtering records. Behavior may change.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            path_template(
                "/accounts/{account_id}/email-security/settings/impersonation_registry", account_id=account_id
            ),
            page=AsyncV4PagePaginationArray[ImpersonationRegistryListResponse],
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
                        "provenance": provenance,
                        "search": search,
                    },
                    impersonation_registry_list_params.ImpersonationRegistryListParams,
                ),
            ),
            model=ImpersonationRegistryListResponse,
        )

    async def delete(
        self,
        impersonation_registry_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[ImpersonationRegistryDeleteResponse]:
        """Removes an entry from the impersonation registry.

        After deletion, this identity
        will no longer be protected from impersonation.

        Args:
          account_id: Identifier.

          impersonation_registry_id: Impersonation registry entry identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not impersonation_registry_id:
            raise ValueError(
                f"Expected a non-empty value for `impersonation_registry_id` but received {impersonation_registry_id!r}"
            )
        return await self._delete(
            path_template(
                "/accounts/{account_id}/email-security/settings/impersonation_registry/{impersonation_registry_id}",
                account_id=account_id,
                impersonation_registry_id=impersonation_registry_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[ImpersonationRegistryDeleteResponse]]._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[ImpersonationRegistryDeleteResponse]], ResultWrapper[ImpersonationRegistryDeleteResponse]
            ),
        )

    async def edit(
        self,
        impersonation_registry_id: str,
        *,
        account_id: str,
        comments: Optional[str] | Omit = omit,
        directory_id: Optional[int] | Omit = omit,
        directory_node_id: Optional[int] | Omit = omit,
        email: str | Omit = omit,
        external_directory_node_id: Optional[str] | Omit = omit,
        is_email_regex: bool | Omit = omit,
        name: str | Omit = omit,
        provenance: Literal["A1S_INTERNAL", "SNOOPY-CASB_OFFICE_365", "SNOOPY-OFFICE_365", "SNOOPY-GOOGLE_DIRECTORY"]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[ImpersonationRegistryEditResponse]:
        """Updates an existing impersonation registry entry.

        Only provided fields will be
        modified. Directory-synced entries can't be updated.

        Args:
          account_id: Identifier.

          impersonation_registry_id: Impersonation registry entry identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not impersonation_registry_id:
            raise ValueError(
                f"Expected a non-empty value for `impersonation_registry_id` but received {impersonation_registry_id!r}"
            )
        return await self._patch(
            path_template(
                "/accounts/{account_id}/email-security/settings/impersonation_registry/{impersonation_registry_id}",
                account_id=account_id,
                impersonation_registry_id=impersonation_registry_id,
            ),
            body=await async_maybe_transform(
                {
                    "comments": comments,
                    "directory_id": directory_id,
                    "directory_node_id": directory_node_id,
                    "email": email,
                    "external_directory_node_id": external_directory_node_id,
                    "is_email_regex": is_email_regex,
                    "name": name,
                    "provenance": provenance,
                },
                impersonation_registry_edit_params.ImpersonationRegistryEditParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[ImpersonationRegistryEditResponse]]._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[ImpersonationRegistryEditResponse]], ResultWrapper[ImpersonationRegistryEditResponse]
            ),
        )

    async def get(
        self,
        impersonation_registry_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[ImpersonationRegistryGetResponse]:
        """
        Retrieves details for a specific impersonation registry entry including the
        protected identity, email pattern, and synchronization source if
        directory-synced.

        Args:
          account_id: Identifier.

          impersonation_registry_id: Impersonation registry entry identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not impersonation_registry_id:
            raise ValueError(
                f"Expected a non-empty value for `impersonation_registry_id` but received {impersonation_registry_id!r}"
            )
        return await self._get(
            path_template(
                "/accounts/{account_id}/email-security/settings/impersonation_registry/{impersonation_registry_id}",
                account_id=account_id,
                impersonation_registry_id=impersonation_registry_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[ImpersonationRegistryGetResponse]]._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[ImpersonationRegistryGetResponse]], ResultWrapper[ImpersonationRegistryGetResponse]
            ),
        )


class ImpersonationRegistryResourceWithRawResponse:
    def __init__(self, impersonation_registry: ImpersonationRegistryResource) -> None:
        self._impersonation_registry = impersonation_registry

        self.create = to_raw_response_wrapper(
            impersonation_registry.create,
        )
        self.list = to_raw_response_wrapper(
            impersonation_registry.list,
        )
        self.delete = to_raw_response_wrapper(
            impersonation_registry.delete,
        )
        self.edit = to_raw_response_wrapper(
            impersonation_registry.edit,
        )
        self.get = to_raw_response_wrapper(
            impersonation_registry.get,
        )


class AsyncImpersonationRegistryResourceWithRawResponse:
    def __init__(self, impersonation_registry: AsyncImpersonationRegistryResource) -> None:
        self._impersonation_registry = impersonation_registry

        self.create = async_to_raw_response_wrapper(
            impersonation_registry.create,
        )
        self.list = async_to_raw_response_wrapper(
            impersonation_registry.list,
        )
        self.delete = async_to_raw_response_wrapper(
            impersonation_registry.delete,
        )
        self.edit = async_to_raw_response_wrapper(
            impersonation_registry.edit,
        )
        self.get = async_to_raw_response_wrapper(
            impersonation_registry.get,
        )


class ImpersonationRegistryResourceWithStreamingResponse:
    def __init__(self, impersonation_registry: ImpersonationRegistryResource) -> None:
        self._impersonation_registry = impersonation_registry

        self.create = to_streamed_response_wrapper(
            impersonation_registry.create,
        )
        self.list = to_streamed_response_wrapper(
            impersonation_registry.list,
        )
        self.delete = to_streamed_response_wrapper(
            impersonation_registry.delete,
        )
        self.edit = to_streamed_response_wrapper(
            impersonation_registry.edit,
        )
        self.get = to_streamed_response_wrapper(
            impersonation_registry.get,
        )


class AsyncImpersonationRegistryResourceWithStreamingResponse:
    def __init__(self, impersonation_registry: AsyncImpersonationRegistryResource) -> None:
        self._impersonation_registry = impersonation_registry

        self.create = async_to_streamed_response_wrapper(
            impersonation_registry.create,
        )
        self.list = async_to_streamed_response_wrapper(
            impersonation_registry.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            impersonation_registry.delete,
        )
        self.edit = async_to_streamed_response_wrapper(
            impersonation_registry.edit,
        )
        self.get = async_to_streamed_response_wrapper(
            impersonation_registry.get,
        )
