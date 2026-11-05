# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, cast

import httpx

from .usage import (
    UsageResource,
    AsyncUsageResource,
    UsageResourceWithRawResponse,
    AsyncUsageResourceWithRawResponse,
    UsageResourceWithStreamingResponse,
    AsyncUsageResourceWithStreamingResponse,
)
from .credits import (
    CreditsResource,
    AsyncCreditsResource,
    CreditsResourceWithRawResponse,
    AsyncCreditsResourceWithRawResponse,
    CreditsResourceWithStreamingResponse,
    AsyncCreditsResourceWithStreamingResponse,
)
from .history import (
    HistoryResource,
    AsyncHistoryResource,
    HistoryResourceWithRawResponse,
    AsyncHistoryResourceWithRawResponse,
    HistoryResourceWithStreamingResponse,
    AsyncHistoryResourceWithStreamingResponse,
)
from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from .bad_debt import (
    BadDebtResource,
    AsyncBadDebtResource,
    BadDebtResourceWithRawResponse,
    AsyncBadDebtResourceWithRawResponse,
    BadDebtResourceWithStreamingResponse,
    AsyncBadDebtResourceWithStreamingResponse,
)
from ..._compat import cached_property
from .rate_plans import (
    RatePlansResource,
    AsyncRatePlansResource,
    RatePlansResourceWithRawResponse,
    AsyncRatePlansResourceWithRawResponse,
    RatePlansResourceWithStreamingResponse,
    AsyncRatePlansResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._wrappers import ResultWrapper
from ..._base_client import make_request_options
from .unpaid_invoice import (
    UnpaidInvoiceResource,
    AsyncUnpaidInvoiceResource,
    UnpaidInvoiceResourceWithRawResponse,
    AsyncUnpaidInvoiceResourceWithRawResponse,
    UnpaidInvoiceResourceWithStreamingResponse,
    AsyncUnpaidInvoiceResourceWithStreamingResponse,
)
from ...types.billing import billing_address_validation_params
from .profiles.profiles import (
    ProfilesResource,
    AsyncProfilesResource,
    ProfilesResourceWithRawResponse,
    AsyncProfilesResourceWithRawResponse,
    ProfilesResourceWithStreamingResponse,
    AsyncProfilesResourceWithStreamingResponse,
)
from .spend_policies.spend_policies import (
    SpendPoliciesResource,
    AsyncSpendPoliciesResource,
    SpendPoliciesResourceWithRawResponse,
    AsyncSpendPoliciesResourceWithRawResponse,
    SpendPoliciesResourceWithStreamingResponse,
    AsyncSpendPoliciesResourceWithStreamingResponse,
)
from ...types.billing.billing_address_validation_response import BillingAddressValidationResponse

__all__ = ["BillingResource", "AsyncBillingResource"]


class BillingResource(SyncAPIResource):
    @cached_property
    def spend_policies(self) -> SpendPoliciesResource:
        return SpendPoliciesResource(self._client)

    @cached_property
    def profiles(self) -> ProfilesResource:
        return ProfilesResource(self._client)

    @cached_property
    def usage(self) -> UsageResource:
        return UsageResource(self._client)

    @cached_property
    def credits(self) -> CreditsResource:
        return CreditsResource(self._client)

    @cached_property
    def history(self) -> HistoryResource:
        return HistoryResource(self._client)

    @cached_property
    def bad_debt(self) -> BadDebtResource:
        return BadDebtResource(self._client)

    @cached_property
    def unpaid_invoice(self) -> UnpaidInvoiceResource:
        return UnpaidInvoiceResource(self._client)

    @cached_property
    def rate_plans(self) -> RatePlansResource:
        return RatePlansResource(self._client)

    @cached_property
    def with_raw_response(self) -> BillingResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return BillingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BillingResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return BillingResourceWithStreamingResponse(self)

    def address_validation(
        self,
        *,
        address: str | Omit = omit,
        address2: str | Omit = omit,
        city: str | Omit = omit,
        country: str | Omit = omit,
        state: str | Omit = omit,
        zipcode: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BillingAddressValidationResponse:
        """
        Validates a billing address and returns validated address suggestions.
        Authentication is not enforced to support pre-signup address validation flows,
        so credentials are accepted but not required.

        Args:
          address: Address line 1.

          address2: Address line 2.

          city: City.

          country: Country code.

          state: State or province.

          zipcode: Postal or zip code.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/billing/address-validation",
            body=maybe_transform(
                {
                    "address": address,
                    "address2": address2,
                    "city": city,
                    "country": country,
                    "state": state,
                    "zipcode": zipcode,
                },
                billing_address_validation_params.BillingAddressValidationParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[BillingAddressValidationResponse]._unwrapper,
            ),
            cast_to=cast(Type[BillingAddressValidationResponse], ResultWrapper[BillingAddressValidationResponse]),
        )


class AsyncBillingResource(AsyncAPIResource):
    @cached_property
    def spend_policies(self) -> AsyncSpendPoliciesResource:
        return AsyncSpendPoliciesResource(self._client)

    @cached_property
    def profiles(self) -> AsyncProfilesResource:
        return AsyncProfilesResource(self._client)

    @cached_property
    def usage(self) -> AsyncUsageResource:
        return AsyncUsageResource(self._client)

    @cached_property
    def credits(self) -> AsyncCreditsResource:
        return AsyncCreditsResource(self._client)

    @cached_property
    def history(self) -> AsyncHistoryResource:
        return AsyncHistoryResource(self._client)

    @cached_property
    def bad_debt(self) -> AsyncBadDebtResource:
        return AsyncBadDebtResource(self._client)

    @cached_property
    def unpaid_invoice(self) -> AsyncUnpaidInvoiceResource:
        return AsyncUnpaidInvoiceResource(self._client)

    @cached_property
    def rate_plans(self) -> AsyncRatePlansResource:
        return AsyncRatePlansResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncBillingResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncBillingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBillingResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncBillingResourceWithStreamingResponse(self)

    async def address_validation(
        self,
        *,
        address: str | Omit = omit,
        address2: str | Omit = omit,
        city: str | Omit = omit,
        country: str | Omit = omit,
        state: str | Omit = omit,
        zipcode: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BillingAddressValidationResponse:
        """
        Validates a billing address and returns validated address suggestions.
        Authentication is not enforced to support pre-signup address validation flows,
        so credentials are accepted but not required.

        Args:
          address: Address line 1.

          address2: Address line 2.

          city: City.

          country: Country code.

          state: State or province.

          zipcode: Postal or zip code.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/billing/address-validation",
            body=await async_maybe_transform(
                {
                    "address": address,
                    "address2": address2,
                    "city": city,
                    "country": country,
                    "state": state,
                    "zipcode": zipcode,
                },
                billing_address_validation_params.BillingAddressValidationParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[BillingAddressValidationResponse]._unwrapper,
            ),
            cast_to=cast(Type[BillingAddressValidationResponse], ResultWrapper[BillingAddressValidationResponse]),
        )


class BillingResourceWithRawResponse:
    def __init__(self, billing: BillingResource) -> None:
        self._billing = billing

        self.address_validation = to_raw_response_wrapper(
            billing.address_validation,
        )

    @cached_property
    def spend_policies(self) -> SpendPoliciesResourceWithRawResponse:
        return SpendPoliciesResourceWithRawResponse(self._billing.spend_policies)

    @cached_property
    def profiles(self) -> ProfilesResourceWithRawResponse:
        return ProfilesResourceWithRawResponse(self._billing.profiles)

    @cached_property
    def usage(self) -> UsageResourceWithRawResponse:
        return UsageResourceWithRawResponse(self._billing.usage)

    @cached_property
    def credits(self) -> CreditsResourceWithRawResponse:
        return CreditsResourceWithRawResponse(self._billing.credits)

    @cached_property
    def history(self) -> HistoryResourceWithRawResponse:
        return HistoryResourceWithRawResponse(self._billing.history)

    @cached_property
    def bad_debt(self) -> BadDebtResourceWithRawResponse:
        return BadDebtResourceWithRawResponse(self._billing.bad_debt)

    @cached_property
    def unpaid_invoice(self) -> UnpaidInvoiceResourceWithRawResponse:
        return UnpaidInvoiceResourceWithRawResponse(self._billing.unpaid_invoice)

    @cached_property
    def rate_plans(self) -> RatePlansResourceWithRawResponse:
        return RatePlansResourceWithRawResponse(self._billing.rate_plans)


class AsyncBillingResourceWithRawResponse:
    def __init__(self, billing: AsyncBillingResource) -> None:
        self._billing = billing

        self.address_validation = async_to_raw_response_wrapper(
            billing.address_validation,
        )

    @cached_property
    def spend_policies(self) -> AsyncSpendPoliciesResourceWithRawResponse:
        return AsyncSpendPoliciesResourceWithRawResponse(self._billing.spend_policies)

    @cached_property
    def profiles(self) -> AsyncProfilesResourceWithRawResponse:
        return AsyncProfilesResourceWithRawResponse(self._billing.profiles)

    @cached_property
    def usage(self) -> AsyncUsageResourceWithRawResponse:
        return AsyncUsageResourceWithRawResponse(self._billing.usage)

    @cached_property
    def credits(self) -> AsyncCreditsResourceWithRawResponse:
        return AsyncCreditsResourceWithRawResponse(self._billing.credits)

    @cached_property
    def history(self) -> AsyncHistoryResourceWithRawResponse:
        return AsyncHistoryResourceWithRawResponse(self._billing.history)

    @cached_property
    def bad_debt(self) -> AsyncBadDebtResourceWithRawResponse:
        return AsyncBadDebtResourceWithRawResponse(self._billing.bad_debt)

    @cached_property
    def unpaid_invoice(self) -> AsyncUnpaidInvoiceResourceWithRawResponse:
        return AsyncUnpaidInvoiceResourceWithRawResponse(self._billing.unpaid_invoice)

    @cached_property
    def rate_plans(self) -> AsyncRatePlansResourceWithRawResponse:
        return AsyncRatePlansResourceWithRawResponse(self._billing.rate_plans)


class BillingResourceWithStreamingResponse:
    def __init__(self, billing: BillingResource) -> None:
        self._billing = billing

        self.address_validation = to_streamed_response_wrapper(
            billing.address_validation,
        )

    @cached_property
    def spend_policies(self) -> SpendPoliciesResourceWithStreamingResponse:
        return SpendPoliciesResourceWithStreamingResponse(self._billing.spend_policies)

    @cached_property
    def profiles(self) -> ProfilesResourceWithStreamingResponse:
        return ProfilesResourceWithStreamingResponse(self._billing.profiles)

    @cached_property
    def usage(self) -> UsageResourceWithStreamingResponse:
        return UsageResourceWithStreamingResponse(self._billing.usage)

    @cached_property
    def credits(self) -> CreditsResourceWithStreamingResponse:
        return CreditsResourceWithStreamingResponse(self._billing.credits)

    @cached_property
    def history(self) -> HistoryResourceWithStreamingResponse:
        return HistoryResourceWithStreamingResponse(self._billing.history)

    @cached_property
    def bad_debt(self) -> BadDebtResourceWithStreamingResponse:
        return BadDebtResourceWithStreamingResponse(self._billing.bad_debt)

    @cached_property
    def unpaid_invoice(self) -> UnpaidInvoiceResourceWithStreamingResponse:
        return UnpaidInvoiceResourceWithStreamingResponse(self._billing.unpaid_invoice)

    @cached_property
    def rate_plans(self) -> RatePlansResourceWithStreamingResponse:
        return RatePlansResourceWithStreamingResponse(self._billing.rate_plans)


class AsyncBillingResourceWithStreamingResponse:
    def __init__(self, billing: AsyncBillingResource) -> None:
        self._billing = billing

        self.address_validation = async_to_streamed_response_wrapper(
            billing.address_validation,
        )

    @cached_property
    def spend_policies(self) -> AsyncSpendPoliciesResourceWithStreamingResponse:
        return AsyncSpendPoliciesResourceWithStreamingResponse(self._billing.spend_policies)

    @cached_property
    def profiles(self) -> AsyncProfilesResourceWithStreamingResponse:
        return AsyncProfilesResourceWithStreamingResponse(self._billing.profiles)

    @cached_property
    def usage(self) -> AsyncUsageResourceWithStreamingResponse:
        return AsyncUsageResourceWithStreamingResponse(self._billing.usage)

    @cached_property
    def credits(self) -> AsyncCreditsResourceWithStreamingResponse:
        return AsyncCreditsResourceWithStreamingResponse(self._billing.credits)

    @cached_property
    def history(self) -> AsyncHistoryResourceWithStreamingResponse:
        return AsyncHistoryResourceWithStreamingResponse(self._billing.history)

    @cached_property
    def bad_debt(self) -> AsyncBadDebtResourceWithStreamingResponse:
        return AsyncBadDebtResourceWithStreamingResponse(self._billing.bad_debt)

    @cached_property
    def unpaid_invoice(self) -> AsyncUnpaidInvoiceResourceWithStreamingResponse:
        return AsyncUnpaidInvoiceResourceWithStreamingResponse(self._billing.unpaid_invoice)

    @cached_property
    def rate_plans(self) -> AsyncRatePlansResourceWithStreamingResponse:
        return AsyncRatePlansResourceWithStreamingResponse(self._billing.rate_plans)
