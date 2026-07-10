# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Optional, cast
from typing_extensions import Literal

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
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
    sending_domain_restriction_edit_params,
    sending_domain_restriction_list_params,
    sending_domain_restriction_create_params,
)
from ....types.email_security.settings.sending_domain_restriction_get_response import (
    SendingDomainRestrictionGetResponse,
)
from ....types.email_security.settings.sending_domain_restriction_edit_response import (
    SendingDomainRestrictionEditResponse,
)
from ....types.email_security.settings.sending_domain_restriction_list_response import (
    SendingDomainRestrictionListResponse,
)
from ....types.email_security.settings.sending_domain_restriction_create_response import (
    SendingDomainRestrictionCreateResponse,
)
from ....types.email_security.settings.sending_domain_restriction_delete_response import (
    SendingDomainRestrictionDeleteResponse,
)

__all__ = ["SendingDomainRestrictionsResource", "AsyncSendingDomainRestrictionsResource"]


class SendingDomainRestrictionsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SendingDomainRestrictionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return SendingDomainRestrictionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SendingDomainRestrictionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return SendingDomainRestrictionsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        account_id: str,
        domain: str,
        exclude: SequenceNotStr[str],
        comments: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[SendingDomainRestrictionCreateResponse]:
        """
        Creates a new sending domain restriction to enforce TLS requirements for a
        domain. Emails without TLS from this domain will be dropped unless the subdomain
        is in the exclude list.

        Args:
          account_id: Identifier.

          domain: Domain that requires TLS enforcement.

          exclude: Excluded subdomains that are exempt from TLS requirements.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._post(
            path_template(
                "/accounts/{account_id}/email-security/settings/sending_domain_restrictions", account_id=account_id
            ),
            body=maybe_transform(
                {
                    "domain": domain,
                    "exclude": exclude,
                    "comments": comments,
                },
                sending_domain_restriction_create_params.SendingDomainRestrictionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[SendingDomainRestrictionCreateResponse]]._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[SendingDomainRestrictionCreateResponse]],
                ResultWrapper[SendingDomainRestrictionCreateResponse],
            ),
        )

    def list(
        self,
        *,
        account_id: str,
        direction: Literal["asc", "desc"] | Omit = omit,
        order: Literal["domain", "created_at"] | Omit = omit,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        search: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncV4PagePaginationArray[SendingDomainRestrictionListResponse]:
        """Returns a paginated list of sending domain restrictions.

        These restrictions
        enforce TLS requirements for emails from specific domains. Mail without TLS from
        restricted domains will be dropped unless the subdomain is in the exclude list.
        Supports sorting and searching.

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
                "/accounts/{account_id}/email-security/settings/sending_domain_restrictions", account_id=account_id
            ),
            page=SyncV4PagePaginationArray[SendingDomainRestrictionListResponse],
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
                    sending_domain_restriction_list_params.SendingDomainRestrictionListParams,
                ),
            ),
            model=SendingDomainRestrictionListResponse,
        )

    def delete(
        self,
        sending_domain_restriction_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[SendingDomainRestrictionDeleteResponse]:
        """Removes a sending domain restriction.

        After deletion, TLS will no longer be
        enforced for emails from this domain.

        Args:
          account_id: Identifier.

          sending_domain_restriction_id: Sending domain restriction identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not sending_domain_restriction_id:
            raise ValueError(
                f"Expected a non-empty value for `sending_domain_restriction_id` but received {sending_domain_restriction_id!r}"
            )
        return self._delete(
            path_template(
                "/accounts/{account_id}/email-security/settings/sending_domain_restrictions/{sending_domain_restriction_id}",
                account_id=account_id,
                sending_domain_restriction_id=sending_domain_restriction_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[SendingDomainRestrictionDeleteResponse]]._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[SendingDomainRestrictionDeleteResponse]],
                ResultWrapper[SendingDomainRestrictionDeleteResponse],
            ),
        )

    def edit(
        self,
        sending_domain_restriction_id: str,
        *,
        account_id: str,
        comments: Optional[str] | Omit = omit,
        domain: str | Omit = omit,
        exclude: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[SendingDomainRestrictionEditResponse]:
        """Updates an existing sending domain restriction.

        Only provided fields will be
        modified. Changes affect which domains require TLS and which subdomains are
        excluded.

        Args:
          account_id: Identifier.

          sending_domain_restriction_id: Sending domain restriction identifier.

          domain: Domain that requires TLS enforcement.

          exclude: Excluded subdomains that are exempt from TLS requirements.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not sending_domain_restriction_id:
            raise ValueError(
                f"Expected a non-empty value for `sending_domain_restriction_id` but received {sending_domain_restriction_id!r}"
            )
        return self._patch(
            path_template(
                "/accounts/{account_id}/email-security/settings/sending_domain_restrictions/{sending_domain_restriction_id}",
                account_id=account_id,
                sending_domain_restriction_id=sending_domain_restriction_id,
            ),
            body=maybe_transform(
                {
                    "comments": comments,
                    "domain": domain,
                    "exclude": exclude,
                },
                sending_domain_restriction_edit_params.SendingDomainRestrictionEditParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[SendingDomainRestrictionEditResponse]]._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[SendingDomainRestrictionEditResponse]],
                ResultWrapper[SendingDomainRestrictionEditResponse],
            ),
        )

    def get(
        self,
        sending_domain_restriction_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[SendingDomainRestrictionGetResponse]:
        """
        Retrieves details for a specific sending domain restriction including the domain
        requiring TLS and any excluded subdomains exempt from the TLS requirement.

        Args:
          account_id: Identifier.

          sending_domain_restriction_id: Sending domain restriction identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not sending_domain_restriction_id:
            raise ValueError(
                f"Expected a non-empty value for `sending_domain_restriction_id` but received {sending_domain_restriction_id!r}"
            )
        return self._get(
            path_template(
                "/accounts/{account_id}/email-security/settings/sending_domain_restrictions/{sending_domain_restriction_id}",
                account_id=account_id,
                sending_domain_restriction_id=sending_domain_restriction_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[SendingDomainRestrictionGetResponse]]._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[SendingDomainRestrictionGetResponse]], ResultWrapper[SendingDomainRestrictionGetResponse]
            ),
        )


class AsyncSendingDomainRestrictionsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSendingDomainRestrictionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSendingDomainRestrictionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSendingDomainRestrictionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncSendingDomainRestrictionsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_id: str,
        domain: str,
        exclude: SequenceNotStr[str],
        comments: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[SendingDomainRestrictionCreateResponse]:
        """
        Creates a new sending domain restriction to enforce TLS requirements for a
        domain. Emails without TLS from this domain will be dropped unless the subdomain
        is in the exclude list.

        Args:
          account_id: Identifier.

          domain: Domain that requires TLS enforcement.

          exclude: Excluded subdomains that are exempt from TLS requirements.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._post(
            path_template(
                "/accounts/{account_id}/email-security/settings/sending_domain_restrictions", account_id=account_id
            ),
            body=await async_maybe_transform(
                {
                    "domain": domain,
                    "exclude": exclude,
                    "comments": comments,
                },
                sending_domain_restriction_create_params.SendingDomainRestrictionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[SendingDomainRestrictionCreateResponse]]._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[SendingDomainRestrictionCreateResponse]],
                ResultWrapper[SendingDomainRestrictionCreateResponse],
            ),
        )

    def list(
        self,
        *,
        account_id: str,
        direction: Literal["asc", "desc"] | Omit = omit,
        order: Literal["domain", "created_at"] | Omit = omit,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        search: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[
        SendingDomainRestrictionListResponse, AsyncV4PagePaginationArray[SendingDomainRestrictionListResponse]
    ]:
        """Returns a paginated list of sending domain restrictions.

        These restrictions
        enforce TLS requirements for emails from specific domains. Mail without TLS from
        restricted domains will be dropped unless the subdomain is in the exclude list.
        Supports sorting and searching.

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
                "/accounts/{account_id}/email-security/settings/sending_domain_restrictions", account_id=account_id
            ),
            page=AsyncV4PagePaginationArray[SendingDomainRestrictionListResponse],
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
                    sending_domain_restriction_list_params.SendingDomainRestrictionListParams,
                ),
            ),
            model=SendingDomainRestrictionListResponse,
        )

    async def delete(
        self,
        sending_domain_restriction_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[SendingDomainRestrictionDeleteResponse]:
        """Removes a sending domain restriction.

        After deletion, TLS will no longer be
        enforced for emails from this domain.

        Args:
          account_id: Identifier.

          sending_domain_restriction_id: Sending domain restriction identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not sending_domain_restriction_id:
            raise ValueError(
                f"Expected a non-empty value for `sending_domain_restriction_id` but received {sending_domain_restriction_id!r}"
            )
        return await self._delete(
            path_template(
                "/accounts/{account_id}/email-security/settings/sending_domain_restrictions/{sending_domain_restriction_id}",
                account_id=account_id,
                sending_domain_restriction_id=sending_domain_restriction_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[SendingDomainRestrictionDeleteResponse]]._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[SendingDomainRestrictionDeleteResponse]],
                ResultWrapper[SendingDomainRestrictionDeleteResponse],
            ),
        )

    async def edit(
        self,
        sending_domain_restriction_id: str,
        *,
        account_id: str,
        comments: Optional[str] | Omit = omit,
        domain: str | Omit = omit,
        exclude: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[SendingDomainRestrictionEditResponse]:
        """Updates an existing sending domain restriction.

        Only provided fields will be
        modified. Changes affect which domains require TLS and which subdomains are
        excluded.

        Args:
          account_id: Identifier.

          sending_domain_restriction_id: Sending domain restriction identifier.

          domain: Domain that requires TLS enforcement.

          exclude: Excluded subdomains that are exempt from TLS requirements.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not sending_domain_restriction_id:
            raise ValueError(
                f"Expected a non-empty value for `sending_domain_restriction_id` but received {sending_domain_restriction_id!r}"
            )
        return await self._patch(
            path_template(
                "/accounts/{account_id}/email-security/settings/sending_domain_restrictions/{sending_domain_restriction_id}",
                account_id=account_id,
                sending_domain_restriction_id=sending_domain_restriction_id,
            ),
            body=await async_maybe_transform(
                {
                    "comments": comments,
                    "domain": domain,
                    "exclude": exclude,
                },
                sending_domain_restriction_edit_params.SendingDomainRestrictionEditParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[SendingDomainRestrictionEditResponse]]._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[SendingDomainRestrictionEditResponse]],
                ResultWrapper[SendingDomainRestrictionEditResponse],
            ),
        )

    async def get(
        self,
        sending_domain_restriction_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[SendingDomainRestrictionGetResponse]:
        """
        Retrieves details for a specific sending domain restriction including the domain
        requiring TLS and any excluded subdomains exempt from the TLS requirement.

        Args:
          account_id: Identifier.

          sending_domain_restriction_id: Sending domain restriction identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not sending_domain_restriction_id:
            raise ValueError(
                f"Expected a non-empty value for `sending_domain_restriction_id` but received {sending_domain_restriction_id!r}"
            )
        return await self._get(
            path_template(
                "/accounts/{account_id}/email-security/settings/sending_domain_restrictions/{sending_domain_restriction_id}",
                account_id=account_id,
                sending_domain_restriction_id=sending_domain_restriction_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[SendingDomainRestrictionGetResponse]]._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[SendingDomainRestrictionGetResponse]], ResultWrapper[SendingDomainRestrictionGetResponse]
            ),
        )


class SendingDomainRestrictionsResourceWithRawResponse:
    def __init__(self, sending_domain_restrictions: SendingDomainRestrictionsResource) -> None:
        self._sending_domain_restrictions = sending_domain_restrictions

        self.create = to_raw_response_wrapper(
            sending_domain_restrictions.create,
        )
        self.list = to_raw_response_wrapper(
            sending_domain_restrictions.list,
        )
        self.delete = to_raw_response_wrapper(
            sending_domain_restrictions.delete,
        )
        self.edit = to_raw_response_wrapper(
            sending_domain_restrictions.edit,
        )
        self.get = to_raw_response_wrapper(
            sending_domain_restrictions.get,
        )


class AsyncSendingDomainRestrictionsResourceWithRawResponse:
    def __init__(self, sending_domain_restrictions: AsyncSendingDomainRestrictionsResource) -> None:
        self._sending_domain_restrictions = sending_domain_restrictions

        self.create = async_to_raw_response_wrapper(
            sending_domain_restrictions.create,
        )
        self.list = async_to_raw_response_wrapper(
            sending_domain_restrictions.list,
        )
        self.delete = async_to_raw_response_wrapper(
            sending_domain_restrictions.delete,
        )
        self.edit = async_to_raw_response_wrapper(
            sending_domain_restrictions.edit,
        )
        self.get = async_to_raw_response_wrapper(
            sending_domain_restrictions.get,
        )


class SendingDomainRestrictionsResourceWithStreamingResponse:
    def __init__(self, sending_domain_restrictions: SendingDomainRestrictionsResource) -> None:
        self._sending_domain_restrictions = sending_domain_restrictions

        self.create = to_streamed_response_wrapper(
            sending_domain_restrictions.create,
        )
        self.list = to_streamed_response_wrapper(
            sending_domain_restrictions.list,
        )
        self.delete = to_streamed_response_wrapper(
            sending_domain_restrictions.delete,
        )
        self.edit = to_streamed_response_wrapper(
            sending_domain_restrictions.edit,
        )
        self.get = to_streamed_response_wrapper(
            sending_domain_restrictions.get,
        )


class AsyncSendingDomainRestrictionsResourceWithStreamingResponse:
    def __init__(self, sending_domain_restrictions: AsyncSendingDomainRestrictionsResource) -> None:
        self._sending_domain_restrictions = sending_domain_restrictions

        self.create = async_to_streamed_response_wrapper(
            sending_domain_restrictions.create,
        )
        self.list = async_to_streamed_response_wrapper(
            sending_domain_restrictions.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            sending_domain_restrictions.delete,
        )
        self.edit = async_to_streamed_response_wrapper(
            sending_domain_restrictions.edit,
        )
        self.get = async_to_streamed_response_wrapper(
            sending_domain_restrictions.get,
        )
