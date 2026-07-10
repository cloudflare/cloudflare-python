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
    trusted_domain_edit_params,
    trusted_domain_list_params,
    trusted_domain_create_params,
)
from ....types.email_security.settings.trusted_domain_get_response import TrustedDomainGetResponse
from ....types.email_security.settings.trusted_domain_edit_response import TrustedDomainEditResponse
from ....types.email_security.settings.trusted_domain_list_response import TrustedDomainListResponse
from ....types.email_security.settings.trusted_domain_create_response import TrustedDomainCreateResponse
from ....types.email_security.settings.trusted_domain_delete_response import TrustedDomainDeleteResponse

__all__ = ["TrustedDomainsResource", "AsyncTrustedDomainsResource"]


class TrustedDomainsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TrustedDomainsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return TrustedDomainsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TrustedDomainsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return TrustedDomainsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        account_id: str,
        is_recent: bool,
        is_regex: bool,
        is_similarity: bool,
        pattern: str,
        comments: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[TrustedDomainCreateResponse]:
        """Creates a new trusted domain pattern.

        Use for partner domains or approved
        senders that should bypass recent domain registration and similarity checks.
        Configure whether it prevents recent domain or spoof dispositions.

        Args:
          account_id: Identifier.

          is_recent: Select to prevent recently registered domains from triggering a Suspicious or
              Malicious disposition.

          is_similarity: Select for partner or other approved domains that have similar spelling to your
              connected domains. Prevents listed domains from triggering a Spoof disposition.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._post(
            path_template("/accounts/{account_id}/email-security/settings/trusted_domains", account_id=account_id),
            body=maybe_transform(
                {
                    "is_recent": is_recent,
                    "is_regex": is_regex,
                    "is_similarity": is_similarity,
                    "pattern": pattern,
                    "comments": comments,
                },
                trusted_domain_create_params.TrustedDomainCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[TrustedDomainCreateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[TrustedDomainCreateResponse]], ResultWrapper[TrustedDomainCreateResponse]),
        )

    def list(
        self,
        *,
        account_id: str,
        direction: Literal["asc", "desc"] | Omit = omit,
        is_recent: bool | Omit = omit,
        is_similarity: bool | Omit = omit,
        order: Literal["pattern", "created_at"] | Omit = omit,
        page: int | Omit = omit,
        pattern: str | Omit = omit,
        per_page: int | Omit = omit,
        search: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncV4PagePaginationArray[TrustedDomainListResponse]:
        """Returns a paginated list of trusted domain patterns.

        Trusted domains prevent
        false positives for recently registered domains and lookalike domain detections.
        Patterns can use regular expressions for flexible matching.

        Args:
          account_id: Identifier.

          direction: The sorting direction.

          is_recent: Filter to show only recently registered domains that are trusted to prevent
              triggering Suspicious or Malicious dispositions.

          is_similarity: Filter to show only proximity domains (partner or approved domains with similar
              spelling to connected domains) that prevent Spoof dispositions.

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
            path_template("/accounts/{account_id}/email-security/settings/trusted_domains", account_id=account_id),
            page=SyncV4PagePaginationArray[TrustedDomainListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "direction": direction,
                        "is_recent": is_recent,
                        "is_similarity": is_similarity,
                        "order": order,
                        "page": page,
                        "pattern": pattern,
                        "per_page": per_page,
                        "search": search,
                    },
                    trusted_domain_list_params.TrustedDomainListParams,
                ),
            ),
            model=TrustedDomainListResponse,
        )

    def delete(
        self,
        trusted_domain_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[TrustedDomainDeleteResponse]:
        """Removes a trusted domain pattern.

        After deletion, emails from this domain will
        be subject to normal recent domain and similarity checks.

        Args:
          account_id: Identifier.

          trusted_domain_id: Trusted domain identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not trusted_domain_id:
            raise ValueError(f"Expected a non-empty value for `trusted_domain_id` but received {trusted_domain_id!r}")
        return self._delete(
            path_template(
                "/accounts/{account_id}/email-security/settings/trusted_domains/{trusted_domain_id}",
                account_id=account_id,
                trusted_domain_id=trusted_domain_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[TrustedDomainDeleteResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[TrustedDomainDeleteResponse]], ResultWrapper[TrustedDomainDeleteResponse]),
        )

    def edit(
        self,
        trusted_domain_id: str,
        *,
        account_id: str,
        comments: Optional[str] | Omit = omit,
        is_recent: bool | Omit = omit,
        is_regex: bool | Omit = omit,
        is_similarity: bool | Omit = omit,
        pattern: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[TrustedDomainEditResponse]:
        """Updates an existing trusted domain pattern.

        Only provided fields will be
        modified. Changes take effect for new emails matching the pattern.

        Args:
          account_id: Identifier.

          trusted_domain_id: Trusted domain identifier

          is_recent: Select to prevent recently registered domains from triggering a Suspicious or
              Malicious disposition.

          is_similarity: Select for partner or other approved domains that have similar spelling to your
              connected domains. Prevents listed domains from triggering a Spoof disposition.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not trusted_domain_id:
            raise ValueError(f"Expected a non-empty value for `trusted_domain_id` but received {trusted_domain_id!r}")
        return self._patch(
            path_template(
                "/accounts/{account_id}/email-security/settings/trusted_domains/{trusted_domain_id}",
                account_id=account_id,
                trusted_domain_id=trusted_domain_id,
            ),
            body=maybe_transform(
                {
                    "comments": comments,
                    "is_recent": is_recent,
                    "is_regex": is_regex,
                    "is_similarity": is_similarity,
                    "pattern": pattern,
                },
                trusted_domain_edit_params.TrustedDomainEditParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[TrustedDomainEditResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[TrustedDomainEditResponse]], ResultWrapper[TrustedDomainEditResponse]),
        )

    def get(
        self,
        trusted_domain_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[TrustedDomainGetResponse]:
        """
        Retrieves details for a specific trusted domain pattern including its pattern
        value, whether it uses regex matching, and which detection types it affects.

        Args:
          account_id: Identifier.

          trusted_domain_id: Trusted domain identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not trusted_domain_id:
            raise ValueError(f"Expected a non-empty value for `trusted_domain_id` but received {trusted_domain_id!r}")
        return self._get(
            path_template(
                "/accounts/{account_id}/email-security/settings/trusted_domains/{trusted_domain_id}",
                account_id=account_id,
                trusted_domain_id=trusted_domain_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[TrustedDomainGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[TrustedDomainGetResponse]], ResultWrapper[TrustedDomainGetResponse]),
        )


class AsyncTrustedDomainsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTrustedDomainsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTrustedDomainsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTrustedDomainsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncTrustedDomainsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_id: str,
        is_recent: bool,
        is_regex: bool,
        is_similarity: bool,
        pattern: str,
        comments: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[TrustedDomainCreateResponse]:
        """Creates a new trusted domain pattern.

        Use for partner domains or approved
        senders that should bypass recent domain registration and similarity checks.
        Configure whether it prevents recent domain or spoof dispositions.

        Args:
          account_id: Identifier.

          is_recent: Select to prevent recently registered domains from triggering a Suspicious or
              Malicious disposition.

          is_similarity: Select for partner or other approved domains that have similar spelling to your
              connected domains. Prevents listed domains from triggering a Spoof disposition.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._post(
            path_template("/accounts/{account_id}/email-security/settings/trusted_domains", account_id=account_id),
            body=await async_maybe_transform(
                {
                    "is_recent": is_recent,
                    "is_regex": is_regex,
                    "is_similarity": is_similarity,
                    "pattern": pattern,
                    "comments": comments,
                },
                trusted_domain_create_params.TrustedDomainCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[TrustedDomainCreateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[TrustedDomainCreateResponse]], ResultWrapper[TrustedDomainCreateResponse]),
        )

    def list(
        self,
        *,
        account_id: str,
        direction: Literal["asc", "desc"] | Omit = omit,
        is_recent: bool | Omit = omit,
        is_similarity: bool | Omit = omit,
        order: Literal["pattern", "created_at"] | Omit = omit,
        page: int | Omit = omit,
        pattern: str | Omit = omit,
        per_page: int | Omit = omit,
        search: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[TrustedDomainListResponse, AsyncV4PagePaginationArray[TrustedDomainListResponse]]:
        """Returns a paginated list of trusted domain patterns.

        Trusted domains prevent
        false positives for recently registered domains and lookalike domain detections.
        Patterns can use regular expressions for flexible matching.

        Args:
          account_id: Identifier.

          direction: The sorting direction.

          is_recent: Filter to show only recently registered domains that are trusted to prevent
              triggering Suspicious or Malicious dispositions.

          is_similarity: Filter to show only proximity domains (partner or approved domains with similar
              spelling to connected domains) that prevent Spoof dispositions.

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
            path_template("/accounts/{account_id}/email-security/settings/trusted_domains", account_id=account_id),
            page=AsyncV4PagePaginationArray[TrustedDomainListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "direction": direction,
                        "is_recent": is_recent,
                        "is_similarity": is_similarity,
                        "order": order,
                        "page": page,
                        "pattern": pattern,
                        "per_page": per_page,
                        "search": search,
                    },
                    trusted_domain_list_params.TrustedDomainListParams,
                ),
            ),
            model=TrustedDomainListResponse,
        )

    async def delete(
        self,
        trusted_domain_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[TrustedDomainDeleteResponse]:
        """Removes a trusted domain pattern.

        After deletion, emails from this domain will
        be subject to normal recent domain and similarity checks.

        Args:
          account_id: Identifier.

          trusted_domain_id: Trusted domain identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not trusted_domain_id:
            raise ValueError(f"Expected a non-empty value for `trusted_domain_id` but received {trusted_domain_id!r}")
        return await self._delete(
            path_template(
                "/accounts/{account_id}/email-security/settings/trusted_domains/{trusted_domain_id}",
                account_id=account_id,
                trusted_domain_id=trusted_domain_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[TrustedDomainDeleteResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[TrustedDomainDeleteResponse]], ResultWrapper[TrustedDomainDeleteResponse]),
        )

    async def edit(
        self,
        trusted_domain_id: str,
        *,
        account_id: str,
        comments: Optional[str] | Omit = omit,
        is_recent: bool | Omit = omit,
        is_regex: bool | Omit = omit,
        is_similarity: bool | Omit = omit,
        pattern: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[TrustedDomainEditResponse]:
        """Updates an existing trusted domain pattern.

        Only provided fields will be
        modified. Changes take effect for new emails matching the pattern.

        Args:
          account_id: Identifier.

          trusted_domain_id: Trusted domain identifier

          is_recent: Select to prevent recently registered domains from triggering a Suspicious or
              Malicious disposition.

          is_similarity: Select for partner or other approved domains that have similar spelling to your
              connected domains. Prevents listed domains from triggering a Spoof disposition.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not trusted_domain_id:
            raise ValueError(f"Expected a non-empty value for `trusted_domain_id` but received {trusted_domain_id!r}")
        return await self._patch(
            path_template(
                "/accounts/{account_id}/email-security/settings/trusted_domains/{trusted_domain_id}",
                account_id=account_id,
                trusted_domain_id=trusted_domain_id,
            ),
            body=await async_maybe_transform(
                {
                    "comments": comments,
                    "is_recent": is_recent,
                    "is_regex": is_regex,
                    "is_similarity": is_similarity,
                    "pattern": pattern,
                },
                trusted_domain_edit_params.TrustedDomainEditParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[TrustedDomainEditResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[TrustedDomainEditResponse]], ResultWrapper[TrustedDomainEditResponse]),
        )

    async def get(
        self,
        trusted_domain_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[TrustedDomainGetResponse]:
        """
        Retrieves details for a specific trusted domain pattern including its pattern
        value, whether it uses regex matching, and which detection types it affects.

        Args:
          account_id: Identifier.

          trusted_domain_id: Trusted domain identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not trusted_domain_id:
            raise ValueError(f"Expected a non-empty value for `trusted_domain_id` but received {trusted_domain_id!r}")
        return await self._get(
            path_template(
                "/accounts/{account_id}/email-security/settings/trusted_domains/{trusted_domain_id}",
                account_id=account_id,
                trusted_domain_id=trusted_domain_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[TrustedDomainGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[TrustedDomainGetResponse]], ResultWrapper[TrustedDomainGetResponse]),
        )


class TrustedDomainsResourceWithRawResponse:
    def __init__(self, trusted_domains: TrustedDomainsResource) -> None:
        self._trusted_domains = trusted_domains

        self.create = to_raw_response_wrapper(
            trusted_domains.create,
        )
        self.list = to_raw_response_wrapper(
            trusted_domains.list,
        )
        self.delete = to_raw_response_wrapper(
            trusted_domains.delete,
        )
        self.edit = to_raw_response_wrapper(
            trusted_domains.edit,
        )
        self.get = to_raw_response_wrapper(
            trusted_domains.get,
        )


class AsyncTrustedDomainsResourceWithRawResponse:
    def __init__(self, trusted_domains: AsyncTrustedDomainsResource) -> None:
        self._trusted_domains = trusted_domains

        self.create = async_to_raw_response_wrapper(
            trusted_domains.create,
        )
        self.list = async_to_raw_response_wrapper(
            trusted_domains.list,
        )
        self.delete = async_to_raw_response_wrapper(
            trusted_domains.delete,
        )
        self.edit = async_to_raw_response_wrapper(
            trusted_domains.edit,
        )
        self.get = async_to_raw_response_wrapper(
            trusted_domains.get,
        )


class TrustedDomainsResourceWithStreamingResponse:
    def __init__(self, trusted_domains: TrustedDomainsResource) -> None:
        self._trusted_domains = trusted_domains

        self.create = to_streamed_response_wrapper(
            trusted_domains.create,
        )
        self.list = to_streamed_response_wrapper(
            trusted_domains.list,
        )
        self.delete = to_streamed_response_wrapper(
            trusted_domains.delete,
        )
        self.edit = to_streamed_response_wrapper(
            trusted_domains.edit,
        )
        self.get = to_streamed_response_wrapper(
            trusted_domains.get,
        )


class AsyncTrustedDomainsResourceWithStreamingResponse:
    def __init__(self, trusted_domains: AsyncTrustedDomainsResource) -> None:
        self._trusted_domains = trusted_domains

        self.create = async_to_streamed_response_wrapper(
            trusted_domains.create,
        )
        self.list = async_to_streamed_response_wrapper(
            trusted_domains.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            trusted_domains.delete,
        )
        self.edit = async_to_streamed_response_wrapper(
            trusted_domains.edit,
        )
        self.get = async_to_streamed_response_wrapper(
            trusted_domains.get,
        )
