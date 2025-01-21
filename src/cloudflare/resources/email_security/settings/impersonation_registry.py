# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Optional, cast
from typing_extensions import Literal

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import (
    maybe_transform,
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
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ImpersonationRegistryCreateResponse:
        """
        Create an entry in impersonation registry

        Args:
          account_id: Account Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._post(
            f"/accounts/{account_id}/email-security/settings/impersonation_registry",
            body=maybe_transform(
                {
                    "email": email,
                    "is_email_regex": is_email_regex,
                    "name": name,
                },
                impersonation_registry_create_params.ImpersonationRegistryCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[ImpersonationRegistryCreateResponse]._unwrapper,
            ),
            cast_to=cast(Type[ImpersonationRegistryCreateResponse], ResultWrapper[ImpersonationRegistryCreateResponse]),
        )

    def list(
        self,
        *,
        account_id: str,
        direction: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
        order: Literal["name", "email", "created_at"] | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        provenance: Literal["A1S_INTERNAL", "SNOOPY-CASB_OFFICE_365", "SNOOPY-OFFICE_365", "SNOOPY-GOOGLE_DIRECTORY"]
        | NotGiven = NOT_GIVEN,
        search: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncV4PagePaginationArray[ImpersonationRegistryListResponse]:
        """
        Lists, searches, and sorts entries in the impersonation registry.

        Args:
          account_id: Account Identifier

          direction: The sorting direction.

          order: The field to sort by.

          page: The page number of paginated results.

          per_page: The number of results per page.

          search: Allows searching in multiple properties of a record simultaneously. This
              parameter is intended for human users, not automation. Its exact behavior is
              intentionally left unspecified and is subject to change in the future.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/email-security/settings/impersonation_registry",
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
        display_name_id: int,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ImpersonationRegistryDeleteResponse:
        """
        Delete an entry from impersonation registry

        Args:
          account_id: Account Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._delete(
            f"/accounts/{account_id}/email-security/settings/impersonation_registry/{display_name_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[ImpersonationRegistryDeleteResponse]._unwrapper,
            ),
            cast_to=cast(Type[ImpersonationRegistryDeleteResponse], ResultWrapper[ImpersonationRegistryDeleteResponse]),
        )

    def edit(
        self,
        display_name_id: int,
        *,
        account_id: str,
        email: Optional[str] | NotGiven = NOT_GIVEN,
        is_email_regex: Optional[bool] | NotGiven = NOT_GIVEN,
        name: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ImpersonationRegistryEditResponse:
        """
        Update an entry in impersonation registry

        Args:
          account_id: Account Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._patch(
            f"/accounts/{account_id}/email-security/settings/impersonation_registry/{display_name_id}",
            body=maybe_transform(
                {
                    "email": email,
                    "is_email_regex": is_email_regex,
                    "name": name,
                },
                impersonation_registry_edit_params.ImpersonationRegistryEditParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[ImpersonationRegistryEditResponse]._unwrapper,
            ),
            cast_to=cast(Type[ImpersonationRegistryEditResponse], ResultWrapper[ImpersonationRegistryEditResponse]),
        )

    def get(
        self,
        display_name_id: int,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ImpersonationRegistryGetResponse:
        """
        Get an entry in impersonation registry

        Args:
          account_id: Account Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get(
            f"/accounts/{account_id}/email-security/settings/impersonation_registry/{display_name_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[ImpersonationRegistryGetResponse]._unwrapper,
            ),
            cast_to=cast(Type[ImpersonationRegistryGetResponse], ResultWrapper[ImpersonationRegistryGetResponse]),
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
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ImpersonationRegistryCreateResponse:
        """
        Create an entry in impersonation registry

        Args:
          account_id: Account Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._post(
            f"/accounts/{account_id}/email-security/settings/impersonation_registry",
            body=await async_maybe_transform(
                {
                    "email": email,
                    "is_email_regex": is_email_regex,
                    "name": name,
                },
                impersonation_registry_create_params.ImpersonationRegistryCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[ImpersonationRegistryCreateResponse]._unwrapper,
            ),
            cast_to=cast(Type[ImpersonationRegistryCreateResponse], ResultWrapper[ImpersonationRegistryCreateResponse]),
        )

    def list(
        self,
        *,
        account_id: str,
        direction: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
        order: Literal["name", "email", "created_at"] | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        provenance: Literal["A1S_INTERNAL", "SNOOPY-CASB_OFFICE_365", "SNOOPY-OFFICE_365", "SNOOPY-GOOGLE_DIRECTORY"]
        | NotGiven = NOT_GIVEN,
        search: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[
        ImpersonationRegistryListResponse, AsyncV4PagePaginationArray[ImpersonationRegistryListResponse]
    ]:
        """
        Lists, searches, and sorts entries in the impersonation registry.

        Args:
          account_id: Account Identifier

          direction: The sorting direction.

          order: The field to sort by.

          page: The page number of paginated results.

          per_page: The number of results per page.

          search: Allows searching in multiple properties of a record simultaneously. This
              parameter is intended for human users, not automation. Its exact behavior is
              intentionally left unspecified and is subject to change in the future.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/email-security/settings/impersonation_registry",
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
        display_name_id: int,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ImpersonationRegistryDeleteResponse:
        """
        Delete an entry from impersonation registry

        Args:
          account_id: Account Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._delete(
            f"/accounts/{account_id}/email-security/settings/impersonation_registry/{display_name_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[ImpersonationRegistryDeleteResponse]._unwrapper,
            ),
            cast_to=cast(Type[ImpersonationRegistryDeleteResponse], ResultWrapper[ImpersonationRegistryDeleteResponse]),
        )

    async def edit(
        self,
        display_name_id: int,
        *,
        account_id: str,
        email: Optional[str] | NotGiven = NOT_GIVEN,
        is_email_regex: Optional[bool] | NotGiven = NOT_GIVEN,
        name: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ImpersonationRegistryEditResponse:
        """
        Update an entry in impersonation registry

        Args:
          account_id: Account Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._patch(
            f"/accounts/{account_id}/email-security/settings/impersonation_registry/{display_name_id}",
            body=await async_maybe_transform(
                {
                    "email": email,
                    "is_email_regex": is_email_regex,
                    "name": name,
                },
                impersonation_registry_edit_params.ImpersonationRegistryEditParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[ImpersonationRegistryEditResponse]._unwrapper,
            ),
            cast_to=cast(Type[ImpersonationRegistryEditResponse], ResultWrapper[ImpersonationRegistryEditResponse]),
        )

    async def get(
        self,
        display_name_id: int,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ImpersonationRegistryGetResponse:
        """
        Get an entry in impersonation registry

        Args:
          account_id: Account Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._get(
            f"/accounts/{account_id}/email-security/settings/impersonation_registry/{display_name_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[ImpersonationRegistryGetResponse]._unwrapper,
            ),
            cast_to=cast(Type[ImpersonationRegistryGetResponse], ResultWrapper[ImpersonationRegistryGetResponse]),
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
