# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Optional, cast
from typing_extensions import Literal, overload

import httpx

from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import required_args, maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._wrappers import ResultWrapper
from ..pagination import SyncV4PagePagination, AsyncV4PagePagination
from .._base_client import AsyncPaginator, make_request_options
from ..types.abuse_reports import abuse_report_list_params, abuse_report_create_params
from ..types.abuse_reports.abuse_report_get_response import AbuseReportGetResponse
from ..types.abuse_reports.abuse_report_list_response import AbuseReportListResponse
from ..types.abuse_reports.abuse_report_create_response import AbuseReportCreateResponse

__all__ = ["AbuseReportsResource", "AsyncAbuseReportsResource"]


class AbuseReportsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AbuseReportsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AbuseReportsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AbuseReportsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AbuseReportsResourceWithStreamingResponse(self)

    @overload
    def create(
        self,
        report_param: str,
        *,
        account_id: str,
        act: Literal["abuse_dmca"],
        address1: str,
        agent_name: str,
        agree: Literal[1],
        city: str,
        country: str,
        email: str,
        email2: str,
        host_notification: Literal["send"],
        name: str,
        original_work: str,
        owner_notification: Literal["send"],
        signature: str,
        state: str,
        urls: str,
        comments: str | Omit = omit,
        company: str | Omit = omit,
        reported_country: str | Omit = omit,
        reported_user_agent: str | Omit = omit,
        tele: str | Omit = omit,
        title: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> str:
        """
        Submit the Abuse Report of a particular type

        Args:
          report_param: The report type for submitted reports.

          act: The report type for submitted reports.

          address1: Text not exceeding 100 characters. This field may be released by Cloudflare to
              third parties such as the Lumen Database (https://lumendatabase.org/).

          agent_name: The name of the copyright holder. Text not exceeding 60 characters. This field
              may be released by Cloudflare to third parties such as the Lumen Database
              (https://lumendatabase.org/).

          agree: Can be `0` for false or `1` for true. Must be value: 1 for DMCA reports

          city: Text not exceeding 255 characters. This field may be released by Cloudflare to
              third parties such as the Lumen Database (https://lumendatabase.org/).

          country: Text not exceeding 255 characters. This field may be released by Cloudflare to
              third parties such as the Lumen Database (https://lumendatabase.org/).

          email: A valid email of the abuse reporter. This field may be released by Cloudflare to
              third parties such as the Lumen Database (https://lumendatabase.org/).

          email2: Should match the value provided in `email`

          host_notification: Notification type based on the abuse type. NOTE: Copyright (DMCA) and Trademark
              reports cannot be anonymous.

          name: Text not exceeding 255 characters. This field may be released by Cloudflare to
              third parties such as the Lumen Database (https://lumendatabase.org/).

          original_work: Text not exceeding 255 characters. This field may be released by Cloudflare to
              third parties such as the Lumen Database (https://lumendatabase.org/).

          owner_notification: Notification type based on the abuse type. NOTE: Copyright (DMCA) and Trademark
              reports cannot be anonymous.

          signature: Required for DMCA reports, should be same as Name. An affirmation that all
              information in the report is true and accurate while agreeing to the policies of
              Cloudflare's abuse reports

          state: Text not exceeding 255 characters. This field may be released by Cloudflare to
              third parties such as the Lumen Database (https://lumendatabase.org/).

          urls: A list of valid URLs separated by ‘\n’ (new line character). The list of the
              URLs should not exceed 250 URLs. All URLs should have the same hostname. Each
              URL should be unique. This field may be released by Cloudflare to third parties
              such as the Lumen Database (https://lumendatabase.org/).

          comments: Any additional comments about the infringement not exceeding 2000 characters

          company: Text not exceeding 100 characters. This field may be released by Cloudflare to
              third parties such as the Lumen Database (https://lumendatabase.org/).

          reported_country: Text containing 2 characters

          reported_user_agent: Text not exceeding 255 characters

          tele: Text not exceeding 20 characters. This field may be released by Cloudflare to
              third parties such as the Lumen Database (https://lumendatabase.org/).

          title: Text not exceeding 255 characters

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        report_param: str,
        *,
        account_id: str,
        act: Literal["abuse_trademark"],
        email: str,
        email2: str,
        host_notification: Literal["send"],
        justification: str,
        name: str,
        owner_notification: Literal["send"],
        trademark_number: str,
        trademark_office: str,
        trademark_symbol: str,
        urls: str,
        comments: str | Omit = omit,
        company: str | Omit = omit,
        reported_country: str | Omit = omit,
        reported_user_agent: str | Omit = omit,
        tele: str | Omit = omit,
        title: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> str:
        """
        Submit the Abuse Report of a particular type

        Args:
          report_param: The report type for submitted reports.

          act: The report type for submitted reports.

          email: A valid email of the abuse reporter. This field may be released by Cloudflare to
              third parties such as the Lumen Database (https://lumendatabase.org/).

          email2: Should match the value provided in `email`

          host_notification: Notification type based on the abuse type. NOTE: Copyright (DMCA) and Trademark
              reports cannot be anonymous.

          justification: A detailed description of the infringement, including any necessary access
              details and the exact steps needed to view the content, not exceeding 5000
              characters.

          name: Text not exceeding 255 characters. This field may be released by Cloudflare to
              third parties such as the Lumen Database (https://lumendatabase.org/).

          owner_notification: Notification type based on the abuse type. NOTE: Copyright (DMCA) and Trademark
              reports cannot be anonymous.

          trademark_number: Text not exceeding 1000 characters

          trademark_office: Text not exceeding 1000 characters

          trademark_symbol: Text not exceeding 1000 characters

          urls: A list of valid URLs separated by ‘\n’ (new line character). The list of the
              URLs should not exceed 250 URLs. All URLs should have the same hostname. Each
              URL should be unique. This field may be released by Cloudflare to third parties
              such as the Lumen Database (https://lumendatabase.org/).

          comments: Any additional comments about the infringement not exceeding 2000 characters

          company: Text not exceeding 100 characters. This field may be released by Cloudflare to
              third parties such as the Lumen Database (https://lumendatabase.org/).

          reported_country: Text containing 2 characters

          reported_user_agent: Text not exceeding 255 characters

          tele: Text not exceeding 20 characters. This field may be released by Cloudflare to
              third parties such as the Lumen Database (https://lumendatabase.org/).

          title: Text not exceeding 255 characters

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        report_param: str,
        *,
        account_id: str,
        act: Literal["abuse_general"],
        email: str,
        email2: str,
        host_notification: Literal["send", "send-anon"],
        justification: str,
        name: str,
        owner_notification: Literal["send", "send-anon", "none"],
        urls: str,
        comments: str | Omit = omit,
        company: str | Omit = omit,
        destination_ips: str | Omit = omit,
        ports_protocols: str | Omit = omit,
        reported_country: str | Omit = omit,
        reported_user_agent: str | Omit = omit,
        source_ips: str | Omit = omit,
        tele: str | Omit = omit,
        title: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> str:
        """
        Submit the Abuse Report of a particular type

        Args:
          report_param: The report type for submitted reports.

          act: The report type for submitted reports.

          email: A valid email of the abuse reporter. This field may be released by Cloudflare to
              third parties such as the Lumen Database (https://lumendatabase.org/).

          email2: Should match the value provided in `email`

          host_notification: Notification type based on the abuse type. NOTE: Copyright (DMCA) and Trademark
              reports cannot be anonymous.

          justification: A detailed description of the infringement, including any necessary access
              details and the exact steps needed to view the content, not exceeding 5000
              characters.

          name: Text not exceeding 255 characters. This field may be released by Cloudflare to
              third parties such as the Lumen Database (https://lumendatabase.org/).

          owner_notification: Notification type based on the abuse type. NOTE: Copyright (DMCA) and Trademark
              reports cannot be anonymous.

          urls: A list of valid URLs separated by ‘\n’ (new line character). The list of the
              URLs should not exceed 250 URLs. All URLs should have the same hostname. Each
              URL should be unique. This field may be released by Cloudflare to third parties
              such as the Lumen Database (https://lumendatabase.org/).

          comments: Any additional comments about the infringement not exceeding 2000 characters

          company: Text not exceeding 100 characters. This field may be released by Cloudflare to
              third parties such as the Lumen Database (https://lumendatabase.org/).

          destination_ips: A list of IP addresses separated by ‘\n’ (new line character). The list of
              destination IPs should not exceed 30 IP addresses. Each one of the IP addresses
              ought to be unique.

          ports_protocols: A comma separated list of ports and protocols e.g. 80/TCP, 22/UDP. The total
              size of the field should not exceed 2000 characters. Each individual
              port/protocol should not exceed 100 characters. The list should not have more
              than 30 unique ports and protocols.

          reported_country: Text containing 2 characters

          reported_user_agent: Text not exceeding 255 characters

          source_ips: A list of IP addresses separated by ‘\n’ (new line character). The list of
              source IPs should not exceed 30 IP addresses. Each one of the IP addresses ought
              to be unique.

          tele: Text not exceeding 20 characters. This field may be released by Cloudflare to
              third parties such as the Lumen Database (https://lumendatabase.org/).

          title: Text not exceeding 255 characters

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        report_param: str,
        *,
        account_id: str,
        act: Literal["abuse_phishing"],
        email: str,
        email2: str,
        host_notification: Literal["send", "send-anon"],
        justification: str,
        name: str,
        owner_notification: Literal["send", "send-anon"],
        urls: str,
        comments: str | Omit = omit,
        company: str | Omit = omit,
        original_work: str | Omit = omit,
        reported_country: str | Omit = omit,
        reported_user_agent: str | Omit = omit,
        tele: str | Omit = omit,
        title: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> str:
        """
        Submit the Abuse Report of a particular type

        Args:
          report_param: The report type for submitted reports.

          act: The report type for submitted reports.

          email: A valid email of the abuse reporter. This field may be released by Cloudflare to
              third parties such as the Lumen Database (https://lumendatabase.org/).

          email2: Should match the value provided in `email`

          host_notification: Notification type based on the abuse type. NOTE: Copyright (DMCA) and Trademark
              reports cannot be anonymous.

          justification: A detailed description of the infringement, including any necessary access
              details and the exact steps needed to view the content, not exceeding 5000
              characters.

          name: Text not exceeding 255 characters. This field may be released by Cloudflare to
              third parties such as the Lumen Database (https://lumendatabase.org/).

          owner_notification: Notification type based on the abuse type. NOTE: Copyright (DMCA) and Trademark
              reports cannot be anonymous.

          urls: A list of valid URLs separated by ‘\n’ (new line character). The list of the
              URLs should not exceed 250 URLs. All URLs should have the same hostname. Each
              URL should be unique. This field may be released by Cloudflare to third parties
              such as the Lumen Database (https://lumendatabase.org/).

          comments: Any additional comments about the infringement not exceeding 2000 characters

          company: Text not exceeding 100 characters. This field may be released by Cloudflare to
              third parties such as the Lumen Database (https://lumendatabase.org/).

          original_work: Text not exceeding 255 characters. This field may be released by Cloudflare to
              third parties such as the Lumen Database (https://lumendatabase.org/).

          reported_country: Text containing 2 characters

          reported_user_agent: Text not exceeding 255 characters

          tele: Text not exceeding 20 characters. This field may be released by Cloudflare to
              third parties such as the Lumen Database (https://lumendatabase.org/).

          title: Text not exceeding 255 characters

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        report_param: str,
        *,
        account_id: str,
        act: Literal["abuse_children"],
        email: str,
        email2: str,
        host_notification: Literal["send", "send-anon"],
        justification: str,
        name: str,
        ncmec_notification: Literal["send", "send-anon"],
        owner_notification: Literal["send", "send-anon", "none"],
        urls: str,
        comments: str | Omit = omit,
        company: str | Omit = omit,
        country: str | Omit = omit,
        reported_country: str | Omit = omit,
        reported_user_agent: str | Omit = omit,
        tele: str | Omit = omit,
        title: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> str:
        """
        Submit the Abuse Report of a particular type

        Args:
          report_param: The report type for submitted reports.

          act: The report type for submitted reports.

          email: A valid email of the abuse reporter. This field may be released by Cloudflare to
              third parties such as the Lumen Database (https://lumendatabase.org/).

          email2: Should match the value provided in `email`

          host_notification: Notification type based on the abuse type. NOTE: Copyright (DMCA) and Trademark
              reports cannot be anonymous.

          justification: A detailed description of the infringement, including any necessary access
              details and the exact steps needed to view the content, not exceeding 5000
              characters.

          name: Text not exceeding 255 characters. This field may be released by Cloudflare to
              third parties such as the Lumen Database (https://lumendatabase.org/).

          ncmec_notification: Notification type based on the abuse type. NOTE: Copyright (DMCA) and Trademark
              reports cannot be anonymous.

          owner_notification: Notification type based on the abuse type. NOTE: Copyright (DMCA) and Trademark
              reports cannot be anonymous.

          urls: A list of valid URLs separated by ‘\n’ (new line character). The list of the
              URLs should not exceed 250 URLs. All URLs should have the same hostname. Each
              URL should be unique. This field may be released by Cloudflare to third parties
              such as the Lumen Database (https://lumendatabase.org/).

          comments: Any additional comments about the infringement not exceeding 2000 characters

          company: Text not exceeding 100 characters. This field may be released by Cloudflare to
              third parties such as the Lumen Database (https://lumendatabase.org/).

          country: Text not exceeding 255 characters. This field may be released by Cloudflare to
              third parties such as the Lumen Database (https://lumendatabase.org/).

          reported_country: Text containing 2 characters

          reported_user_agent: Text not exceeding 255 characters

          tele: Text not exceeding 20 characters. This field may be released by Cloudflare to
              third parties such as the Lumen Database (https://lumendatabase.org/).

          title: Text not exceeding 255 characters

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        report_param: str,
        *,
        account_id: str,
        act: Literal["abuse_threat"],
        email: str,
        email2: str,
        host_notification: Literal["send", "send-anon"],
        justification: str,
        name: str,
        owner_notification: Literal["send", "send-anon"],
        urls: str,
        comments: str | Omit = omit,
        company: str | Omit = omit,
        reported_country: str | Omit = omit,
        reported_user_agent: str | Omit = omit,
        tele: str | Omit = omit,
        title: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> str:
        """
        Submit the Abuse Report of a particular type

        Args:
          report_param: The report type for submitted reports.

          act: The report type for submitted reports.

          email: A valid email of the abuse reporter. This field may be released by Cloudflare to
              third parties such as the Lumen Database (https://lumendatabase.org/).

          email2: Should match the value provided in `email`

          host_notification: Notification type based on the abuse type. NOTE: Copyright (DMCA) and Trademark
              reports cannot be anonymous.

          justification: A detailed description of the infringement, including any necessary access
              details and the exact steps needed to view the content, not exceeding 5000
              characters.

          name: Text not exceeding 255 characters. This field may be released by Cloudflare to
              third parties such as the Lumen Database (https://lumendatabase.org/).

          owner_notification: Notification type based on the abuse type. NOTE: Copyright (DMCA) and Trademark
              reports cannot be anonymous.

          urls: A list of valid URLs separated by ‘\n’ (new line character). The list of the
              URLs should not exceed 250 URLs. All URLs should have the same hostname. Each
              URL should be unique. This field may be released by Cloudflare to third parties
              such as the Lumen Database (https://lumendatabase.org/).

          comments: Any additional comments about the infringement not exceeding 2000 characters

          company: Text not exceeding 100 characters. This field may be released by Cloudflare to
              third parties such as the Lumen Database (https://lumendatabase.org/).

          reported_country: Text containing 2 characters

          reported_user_agent: Text not exceeding 255 characters

          tele: Text not exceeding 20 characters. This field may be released by Cloudflare to
              third parties such as the Lumen Database (https://lumendatabase.org/).

          title: Text not exceeding 255 characters

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        report_param: str,
        *,
        account_id: str,
        act: Literal["abuse_registrar_whois"],
        email: str,
        email2: str,
        name: str,
        owner_notification: Literal["send", "send-anon", "none"],
        urls: str,
        comments: str | Omit = omit,
        company: str | Omit = omit,
        reported_country: str | Omit = omit,
        reported_user_agent: str | Omit = omit,
        tele: str | Omit = omit,
        title: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> str:
        """
        Submit the Abuse Report of a particular type

        Args:
          report_param: The report type for submitted reports.

          act: The report type for submitted reports.

          email: A valid email of the abuse reporter. This field may be released by Cloudflare to
              third parties such as the Lumen Database (https://lumendatabase.org/).

          email2: Should match the value provided in `email`

          name: Text not exceeding 255 characters. This field may be released by Cloudflare to
              third parties such as the Lumen Database (https://lumendatabase.org/).

          owner_notification: Notification type based on the abuse type. NOTE: Copyright (DMCA) and Trademark
              reports cannot be anonymous.

          urls: A list of valid URLs separated by ‘\n’ (new line character). The list of the
              URLs should not exceed 250 URLs. All URLs should have the same hostname. Each
              URL should be unique. This field may be released by Cloudflare to third parties
              such as the Lumen Database (https://lumendatabase.org/).

          comments: Any additional comments about the infringement not exceeding 2000 characters

          company: Text not exceeding 100 characters. This field may be released by Cloudflare to
              third parties such as the Lumen Database (https://lumendatabase.org/).

          reported_country: Text containing 2 characters

          reported_user_agent: Text not exceeding 255 characters

          tele: Text not exceeding 20 characters. This field may be released by Cloudflare to
              third parties such as the Lumen Database (https://lumendatabase.org/).

          title: Text not exceeding 255 characters

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        report_param: str,
        *,
        account_id: str,
        act: Literal["abuse_ncsei"],
        email: str,
        email2: str,
        host_notification: Literal["send", "send-anon"],
        name: str,
        ncsei_subject_representation: bool,
        owner_notification: Literal["send", "send-anon", "none"],
        urls: str,
        comments: str | Omit = omit,
        company: str | Omit = omit,
        country: str | Omit = omit,
        reported_country: str | Omit = omit,
        reported_user_agent: str | Omit = omit,
        tele: str | Omit = omit,
        title: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> str:
        """
        Submit the Abuse Report of a particular type

        Args:
          report_param: The report type for submitted reports.

          act: The report type for submitted reports.

          email: A valid email of the abuse reporter. This field may be released by Cloudflare to
              third parties such as the Lumen Database (https://lumendatabase.org/).

          email2: Should match the value provided in `email`

          host_notification: Notification type based on the abuse type. NOTE: Copyright (DMCA) and Trademark
              reports cannot be anonymous.

          name: Text not exceeding 255 characters. This field may be released by Cloudflare to
              third parties such as the Lumen Database (https://lumendatabase.org/).

          ncsei_subject_representation: If the submitter is the target of NCSEI in the URLs of the abuse report.

          owner_notification: Notification type based on the abuse type. NOTE: Copyright (DMCA) and Trademark
              reports cannot be anonymous.

          urls: A list of valid URLs separated by ‘\n’ (new line character). The list of the
              URLs should not exceed 250 URLs. All URLs should have the same hostname. Each
              URL should be unique. This field may be released by Cloudflare to third parties
              such as the Lumen Database (https://lumendatabase.org/).

          comments: Any additional comments about the infringement not exceeding 2000 characters

          company: Text not exceeding 100 characters. This field may be released by Cloudflare to
              third parties such as the Lumen Database (https://lumendatabase.org/).

          country: Text not exceeding 255 characters. This field may be released by Cloudflare to
              third parties such as the Lumen Database (https://lumendatabase.org/).

          reported_country: Text containing 2 characters

          reported_user_agent: Text not exceeding 255 characters

          tele: Text not exceeding 20 characters. This field may be released by Cloudflare to
              third parties such as the Lumen Database (https://lumendatabase.org/).

          title: Text not exceeding 255 characters

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(
        [
            "account_id",
            "act",
            "address1",
            "agent_name",
            "agree",
            "city",
            "country",
            "email",
            "email2",
            "host_notification",
            "name",
            "original_work",
            "owner_notification",
            "signature",
            "state",
            "urls",
        ],
        [
            "account_id",
            "act",
            "email",
            "email2",
            "host_notification",
            "justification",
            "name",
            "owner_notification",
            "trademark_number",
            "trademark_office",
            "trademark_symbol",
            "urls",
        ],
        [
            "account_id",
            "act",
            "email",
            "email2",
            "host_notification",
            "justification",
            "name",
            "owner_notification",
            "urls",
        ],
        [
            "account_id",
            "act",
            "email",
            "email2",
            "host_notification",
            "justification",
            "name",
            "ncmec_notification",
            "owner_notification",
            "urls",
        ],
        ["account_id", "act", "email", "email2", "name", "owner_notification", "urls"],
        [
            "account_id",
            "act",
            "email",
            "email2",
            "host_notification",
            "name",
            "ncsei_subject_representation",
            "owner_notification",
            "urls",
        ],
    )
    def create(
        self,
        report_param: str,
        *,
        account_id: str,
        act: Literal["abuse_dmca"]
        | Literal["abuse_trademark"]
        | Literal["abuse_general"]
        | Literal["abuse_phishing"]
        | Literal["abuse_children"]
        | Literal["abuse_threat"]
        | Literal["abuse_registrar_whois"]
        | Literal["abuse_ncsei"],
        address1: str | Omit = omit,
        agent_name: str | Omit = omit,
        agree: Literal[1] | Omit = omit,
        city: str | Omit = omit,
        country: str | Omit = omit,
        email: str,
        email2: str,
        host_notification: Literal["send"] | Literal["send", "send-anon"] | Omit = omit,
        name: str,
        original_work: str | Omit = omit,
        owner_notification: Literal["send"] | Literal["send", "send-anon", "none"] | Literal["send", "send-anon"],
        signature: str | Omit = omit,
        state: str | Omit = omit,
        urls: str,
        comments: str | Omit = omit,
        company: str | Omit = omit,
        reported_country: str | Omit = omit,
        reported_user_agent: str | Omit = omit,
        tele: str | Omit = omit,
        title: str | Omit = omit,
        justification: str | Omit = omit,
        trademark_number: str | Omit = omit,
        trademark_office: str | Omit = omit,
        trademark_symbol: str | Omit = omit,
        destination_ips: str | Omit = omit,
        ports_protocols: str | Omit = omit,
        source_ips: str | Omit = omit,
        ncmec_notification: Literal["send", "send-anon"] | Omit = omit,
        ncsei_subject_representation: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> str:
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not report_param:
            raise ValueError(f"Expected a non-empty value for `report_param` but received {report_param!r}")
        return self._post(
            f"/accounts/{account_id}/abuse-reports/{report_param}",
            body=maybe_transform(
                {
                    "act": act,
                    "address1": address1,
                    "agent_name": agent_name,
                    "agree": agree,
                    "city": city,
                    "country": country,
                    "email": email,
                    "email2": email2,
                    "host_notification": host_notification,
                    "name": name,
                    "original_work": original_work,
                    "owner_notification": owner_notification,
                    "signature": signature,
                    "state": state,
                    "urls": urls,
                    "comments": comments,
                    "company": company,
                    "reported_country": reported_country,
                    "reported_user_agent": reported_user_agent,
                    "tele": tele,
                    "title": title,
                    "justification": justification,
                    "trademark_number": trademark_number,
                    "trademark_office": trademark_office,
                    "trademark_symbol": trademark_symbol,
                    "destination_ips": destination_ips,
                    "ports_protocols": ports_protocols,
                    "source_ips": source_ips,
                    "ncmec_notification": ncmec_notification,
                    "ncsei_subject_representation": ncsei_subject_representation,
                },
                abuse_report_create_params.AbuseReportCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[AbuseReportCreateResponse]._unwrapper,
            ),
            cast_to=cast(Type[str], ResultWrapper[str]),
        )

    def list(
        self,
        *,
        account_id: str,
        created_after: str | Omit = omit,
        created_before: str | Omit = omit,
        domain: str | Omit = omit,
        mitigation_status: Literal["pending", "active", "in_review", "cancelled", "removed"] | Omit = omit,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        sort: str | Omit = omit,
        status: Literal["accepted", "in_review"] | Omit = omit,
        type: Literal["PHISH", "GEN", "THREAT", "DMCA", "EMER", "TM", "REG_WHO", "NCSEI", "NETWORK"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncV4PagePagination[Optional[AbuseReportListResponse]]:
        """
        List the abuse reports for a given account

        Args:
          created_after: Returns reports created after the specified date

          created_before: Returns reports created before the specified date

          domain: Filter by domain name related to the abuse report

          mitigation_status: Filter reports that have any mitigations in the given status.

          page: Where in pagination to start listing abuse reports

          per_page: How many abuse reports per page to list

          sort: A property to sort by, followed by the order (id, cdate, domain, type, status)

          status: Filter by the status of the report.

          type: Filter by the type of the report.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/abuse-reports",
            page=SyncV4PagePagination[Optional[AbuseReportListResponse]],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "created_after": created_after,
                        "created_before": created_before,
                        "domain": domain,
                        "mitigation_status": mitigation_status,
                        "page": page,
                        "per_page": per_page,
                        "sort": sort,
                        "status": status,
                        "type": type,
                    },
                    abuse_report_list_params.AbuseReportListParams,
                ),
            ),
            model=AbuseReportListResponse,
        )

    def get(
        self,
        report_param: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AbuseReportGetResponse:
        """
        Retrieve the details of an abuse report.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not report_param:
            raise ValueError(f"Expected a non-empty value for `report_param` but received {report_param!r}")
        return self._get(
            f"/accounts/{account_id}/abuse-reports/{report_param}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[AbuseReportGetResponse]._unwrapper,
            ),
            cast_to=cast(Type[AbuseReportGetResponse], ResultWrapper[AbuseReportGetResponse]),
        )


class AsyncAbuseReportsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAbuseReportsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAbuseReportsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAbuseReportsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncAbuseReportsResourceWithStreamingResponse(self)

    @overload
    async def create(
        self,
        report_param: str,
        *,
        account_id: str,
        act: Literal["abuse_dmca"],
        address1: str,
        agent_name: str,
        agree: Literal[1],
        city: str,
        country: str,
        email: str,
        email2: str,
        host_notification: Literal["send"],
        name: str,
        original_work: str,
        owner_notification: Literal["send"],
        signature: str,
        state: str,
        urls: str,
        comments: str | Omit = omit,
        company: str | Omit = omit,
        reported_country: str | Omit = omit,
        reported_user_agent: str | Omit = omit,
        tele: str | Omit = omit,
        title: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> str:
        """
        Submit the Abuse Report of a particular type

        Args:
          report_param: The report type for submitted reports.

          act: The report type for submitted reports.

          address1: Text not exceeding 100 characters. This field may be released by Cloudflare to
              third parties such as the Lumen Database (https://lumendatabase.org/).

          agent_name: The name of the copyright holder. Text not exceeding 60 characters. This field
              may be released by Cloudflare to third parties such as the Lumen Database
              (https://lumendatabase.org/).

          agree: Can be `0` for false or `1` for true. Must be value: 1 for DMCA reports

          city: Text not exceeding 255 characters. This field may be released by Cloudflare to
              third parties such as the Lumen Database (https://lumendatabase.org/).

          country: Text not exceeding 255 characters. This field may be released by Cloudflare to
              third parties such as the Lumen Database (https://lumendatabase.org/).

          email: A valid email of the abuse reporter. This field may be released by Cloudflare to
              third parties such as the Lumen Database (https://lumendatabase.org/).

          email2: Should match the value provided in `email`

          host_notification: Notification type based on the abuse type. NOTE: Copyright (DMCA) and Trademark
              reports cannot be anonymous.

          name: Text not exceeding 255 characters. This field may be released by Cloudflare to
              third parties such as the Lumen Database (https://lumendatabase.org/).

          original_work: Text not exceeding 255 characters. This field may be released by Cloudflare to
              third parties such as the Lumen Database (https://lumendatabase.org/).

          owner_notification: Notification type based on the abuse type. NOTE: Copyright (DMCA) and Trademark
              reports cannot be anonymous.

          signature: Required for DMCA reports, should be same as Name. An affirmation that all
              information in the report is true and accurate while agreeing to the policies of
              Cloudflare's abuse reports

          state: Text not exceeding 255 characters. This field may be released by Cloudflare to
              third parties such as the Lumen Database (https://lumendatabase.org/).

          urls: A list of valid URLs separated by ‘\n’ (new line character). The list of the
              URLs should not exceed 250 URLs. All URLs should have the same hostname. Each
              URL should be unique. This field may be released by Cloudflare to third parties
              such as the Lumen Database (https://lumendatabase.org/).

          comments: Any additional comments about the infringement not exceeding 2000 characters

          company: Text not exceeding 100 characters. This field may be released by Cloudflare to
              third parties such as the Lumen Database (https://lumendatabase.org/).

          reported_country: Text containing 2 characters

          reported_user_agent: Text not exceeding 255 characters

          tele: Text not exceeding 20 characters. This field may be released by Cloudflare to
              third parties such as the Lumen Database (https://lumendatabase.org/).

          title: Text not exceeding 255 characters

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        report_param: str,
        *,
        account_id: str,
        act: Literal["abuse_trademark"],
        email: str,
        email2: str,
        host_notification: Literal["send"],
        justification: str,
        name: str,
        owner_notification: Literal["send"],
        trademark_number: str,
        trademark_office: str,
        trademark_symbol: str,
        urls: str,
        comments: str | Omit = omit,
        company: str | Omit = omit,
        reported_country: str | Omit = omit,
        reported_user_agent: str | Omit = omit,
        tele: str | Omit = omit,
        title: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> str:
        """
        Submit the Abuse Report of a particular type

        Args:
          report_param: The report type for submitted reports.

          act: The report type for submitted reports.

          email: A valid email of the abuse reporter. This field may be released by Cloudflare to
              third parties such as the Lumen Database (https://lumendatabase.org/).

          email2: Should match the value provided in `email`

          host_notification: Notification type based on the abuse type. NOTE: Copyright (DMCA) and Trademark
              reports cannot be anonymous.

          justification: A detailed description of the infringement, including any necessary access
              details and the exact steps needed to view the content, not exceeding 5000
              characters.

          name: Text not exceeding 255 characters. This field may be released by Cloudflare to
              third parties such as the Lumen Database (https://lumendatabase.org/).

          owner_notification: Notification type based on the abuse type. NOTE: Copyright (DMCA) and Trademark
              reports cannot be anonymous.

          trademark_number: Text not exceeding 1000 characters

          trademark_office: Text not exceeding 1000 characters

          trademark_symbol: Text not exceeding 1000 characters

          urls: A list of valid URLs separated by ‘\n’ (new line character). The list of the
              URLs should not exceed 250 URLs. All URLs should have the same hostname. Each
              URL should be unique. This field may be released by Cloudflare to third parties
              such as the Lumen Database (https://lumendatabase.org/).

          comments: Any additional comments about the infringement not exceeding 2000 characters

          company: Text not exceeding 100 characters. This field may be released by Cloudflare to
              third parties such as the Lumen Database (https://lumendatabase.org/).

          reported_country: Text containing 2 characters

          reported_user_agent: Text not exceeding 255 characters

          tele: Text not exceeding 20 characters. This field may be released by Cloudflare to
              third parties such as the Lumen Database (https://lumendatabase.org/).

          title: Text not exceeding 255 characters

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        report_param: str,
        *,
        account_id: str,
        act: Literal["abuse_general"],
        email: str,
        email2: str,
        host_notification: Literal["send", "send-anon"],
        justification: str,
        name: str,
        owner_notification: Literal["send", "send-anon", "none"],
        urls: str,
        comments: str | Omit = omit,
        company: str | Omit = omit,
        destination_ips: str | Omit = omit,
        ports_protocols: str | Omit = omit,
        reported_country: str | Omit = omit,
        reported_user_agent: str | Omit = omit,
        source_ips: str | Omit = omit,
        tele: str | Omit = omit,
        title: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> str:
        """
        Submit the Abuse Report of a particular type

        Args:
          report_param: The report type for submitted reports.

          act: The report type for submitted reports.

          email: A valid email of the abuse reporter. This field may be released by Cloudflare to
              third parties such as the Lumen Database (https://lumendatabase.org/).

          email2: Should match the value provided in `email`

          host_notification: Notification type based on the abuse type. NOTE: Copyright (DMCA) and Trademark
              reports cannot be anonymous.

          justification: A detailed description of the infringement, including any necessary access
              details and the exact steps needed to view the content, not exceeding 5000
              characters.

          name: Text not exceeding 255 characters. This field may be released by Cloudflare to
              third parties such as the Lumen Database (https://lumendatabase.org/).

          owner_notification: Notification type based on the abuse type. NOTE: Copyright (DMCA) and Trademark
              reports cannot be anonymous.

          urls: A list of valid URLs separated by ‘\n’ (new line character). The list of the
              URLs should not exceed 250 URLs. All URLs should have the same hostname. Each
              URL should be unique. This field may be released by Cloudflare to third parties
              such as the Lumen Database (https://lumendatabase.org/).

          comments: Any additional comments about the infringement not exceeding 2000 characters

          company: Text not exceeding 100 characters. This field may be released by Cloudflare to
              third parties such as the Lumen Database (https://lumendatabase.org/).

          destination_ips: A list of IP addresses separated by ‘\n’ (new line character). The list of
              destination IPs should not exceed 30 IP addresses. Each one of the IP addresses
              ought to be unique.

          ports_protocols: A comma separated list of ports and protocols e.g. 80/TCP, 22/UDP. The total
              size of the field should not exceed 2000 characters. Each individual
              port/protocol should not exceed 100 characters. The list should not have more
              than 30 unique ports and protocols.

          reported_country: Text containing 2 characters

          reported_user_agent: Text not exceeding 255 characters

          source_ips: A list of IP addresses separated by ‘\n’ (new line character). The list of
              source IPs should not exceed 30 IP addresses. Each one of the IP addresses ought
              to be unique.

          tele: Text not exceeding 20 characters. This field may be released by Cloudflare to
              third parties such as the Lumen Database (https://lumendatabase.org/).

          title: Text not exceeding 255 characters

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        report_param: str,
        *,
        account_id: str,
        act: Literal["abuse_phishing"],
        email: str,
        email2: str,
        host_notification: Literal["send", "send-anon"],
        justification: str,
        name: str,
        owner_notification: Literal["send", "send-anon"],
        urls: str,
        comments: str | Omit = omit,
        company: str | Omit = omit,
        original_work: str | Omit = omit,
        reported_country: str | Omit = omit,
        reported_user_agent: str | Omit = omit,
        tele: str | Omit = omit,
        title: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> str:
        """
        Submit the Abuse Report of a particular type

        Args:
          report_param: The report type for submitted reports.

          act: The report type for submitted reports.

          email: A valid email of the abuse reporter. This field may be released by Cloudflare to
              third parties such as the Lumen Database (https://lumendatabase.org/).

          email2: Should match the value provided in `email`

          host_notification: Notification type based on the abuse type. NOTE: Copyright (DMCA) and Trademark
              reports cannot be anonymous.

          justification: A detailed description of the infringement, including any necessary access
              details and the exact steps needed to view the content, not exceeding 5000
              characters.

          name: Text not exceeding 255 characters. This field may be released by Cloudflare to
              third parties such as the Lumen Database (https://lumendatabase.org/).

          owner_notification: Notification type based on the abuse type. NOTE: Copyright (DMCA) and Trademark
              reports cannot be anonymous.

          urls: A list of valid URLs separated by ‘\n’ (new line character). The list of the
              URLs should not exceed 250 URLs. All URLs should have the same hostname. Each
              URL should be unique. This field may be released by Cloudflare to third parties
              such as the Lumen Database (https://lumendatabase.org/).

          comments: Any additional comments about the infringement not exceeding 2000 characters

          company: Text not exceeding 100 characters. This field may be released by Cloudflare to
              third parties such as the Lumen Database (https://lumendatabase.org/).

          original_work: Text not exceeding 255 characters. This field may be released by Cloudflare to
              third parties such as the Lumen Database (https://lumendatabase.org/).

          reported_country: Text containing 2 characters

          reported_user_agent: Text not exceeding 255 characters

          tele: Text not exceeding 20 characters. This field may be released by Cloudflare to
              third parties such as the Lumen Database (https://lumendatabase.org/).

          title: Text not exceeding 255 characters

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        report_param: str,
        *,
        account_id: str,
        act: Literal["abuse_children"],
        email: str,
        email2: str,
        host_notification: Literal["send", "send-anon"],
        justification: str,
        name: str,
        ncmec_notification: Literal["send", "send-anon"],
        owner_notification: Literal["send", "send-anon", "none"],
        urls: str,
        comments: str | Omit = omit,
        company: str | Omit = omit,
        country: str | Omit = omit,
        reported_country: str | Omit = omit,
        reported_user_agent: str | Omit = omit,
        tele: str | Omit = omit,
        title: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> str:
        """
        Submit the Abuse Report of a particular type

        Args:
          report_param: The report type for submitted reports.

          act: The report type for submitted reports.

          email: A valid email of the abuse reporter. This field may be released by Cloudflare to
              third parties such as the Lumen Database (https://lumendatabase.org/).

          email2: Should match the value provided in `email`

          host_notification: Notification type based on the abuse type. NOTE: Copyright (DMCA) and Trademark
              reports cannot be anonymous.

          justification: A detailed description of the infringement, including any necessary access
              details and the exact steps needed to view the content, not exceeding 5000
              characters.

          name: Text not exceeding 255 characters. This field may be released by Cloudflare to
              third parties such as the Lumen Database (https://lumendatabase.org/).

          ncmec_notification: Notification type based on the abuse type. NOTE: Copyright (DMCA) and Trademark
              reports cannot be anonymous.

          owner_notification: Notification type based on the abuse type. NOTE: Copyright (DMCA) and Trademark
              reports cannot be anonymous.

          urls: A list of valid URLs separated by ‘\n’ (new line character). The list of the
              URLs should not exceed 250 URLs. All URLs should have the same hostname. Each
              URL should be unique. This field may be released by Cloudflare to third parties
              such as the Lumen Database (https://lumendatabase.org/).

          comments: Any additional comments about the infringement not exceeding 2000 characters

          company: Text not exceeding 100 characters. This field may be released by Cloudflare to
              third parties such as the Lumen Database (https://lumendatabase.org/).

          country: Text not exceeding 255 characters. This field may be released by Cloudflare to
              third parties such as the Lumen Database (https://lumendatabase.org/).

          reported_country: Text containing 2 characters

          reported_user_agent: Text not exceeding 255 characters

          tele: Text not exceeding 20 characters. This field may be released by Cloudflare to
              third parties such as the Lumen Database (https://lumendatabase.org/).

          title: Text not exceeding 255 characters

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        report_param: str,
        *,
        account_id: str,
        act: Literal["abuse_threat"],
        email: str,
        email2: str,
        host_notification: Literal["send", "send-anon"],
        justification: str,
        name: str,
        owner_notification: Literal["send", "send-anon"],
        urls: str,
        comments: str | Omit = omit,
        company: str | Omit = omit,
        reported_country: str | Omit = omit,
        reported_user_agent: str | Omit = omit,
        tele: str | Omit = omit,
        title: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> str:
        """
        Submit the Abuse Report of a particular type

        Args:
          report_param: The report type for submitted reports.

          act: The report type for submitted reports.

          email: A valid email of the abuse reporter. This field may be released by Cloudflare to
              third parties such as the Lumen Database (https://lumendatabase.org/).

          email2: Should match the value provided in `email`

          host_notification: Notification type based on the abuse type. NOTE: Copyright (DMCA) and Trademark
              reports cannot be anonymous.

          justification: A detailed description of the infringement, including any necessary access
              details and the exact steps needed to view the content, not exceeding 5000
              characters.

          name: Text not exceeding 255 characters. This field may be released by Cloudflare to
              third parties such as the Lumen Database (https://lumendatabase.org/).

          owner_notification: Notification type based on the abuse type. NOTE: Copyright (DMCA) and Trademark
              reports cannot be anonymous.

          urls: A list of valid URLs separated by ‘\n’ (new line character). The list of the
              URLs should not exceed 250 URLs. All URLs should have the same hostname. Each
              URL should be unique. This field may be released by Cloudflare to third parties
              such as the Lumen Database (https://lumendatabase.org/).

          comments: Any additional comments about the infringement not exceeding 2000 characters

          company: Text not exceeding 100 characters. This field may be released by Cloudflare to
              third parties such as the Lumen Database (https://lumendatabase.org/).

          reported_country: Text containing 2 characters

          reported_user_agent: Text not exceeding 255 characters

          tele: Text not exceeding 20 characters. This field may be released by Cloudflare to
              third parties such as the Lumen Database (https://lumendatabase.org/).

          title: Text not exceeding 255 characters

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        report_param: str,
        *,
        account_id: str,
        act: Literal["abuse_registrar_whois"],
        email: str,
        email2: str,
        name: str,
        owner_notification: Literal["send", "send-anon", "none"],
        urls: str,
        comments: str | Omit = omit,
        company: str | Omit = omit,
        reported_country: str | Omit = omit,
        reported_user_agent: str | Omit = omit,
        tele: str | Omit = omit,
        title: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> str:
        """
        Submit the Abuse Report of a particular type

        Args:
          report_param: The report type for submitted reports.

          act: The report type for submitted reports.

          email: A valid email of the abuse reporter. This field may be released by Cloudflare to
              third parties such as the Lumen Database (https://lumendatabase.org/).

          email2: Should match the value provided in `email`

          name: Text not exceeding 255 characters. This field may be released by Cloudflare to
              third parties such as the Lumen Database (https://lumendatabase.org/).

          owner_notification: Notification type based on the abuse type. NOTE: Copyright (DMCA) and Trademark
              reports cannot be anonymous.

          urls: A list of valid URLs separated by ‘\n’ (new line character). The list of the
              URLs should not exceed 250 URLs. All URLs should have the same hostname. Each
              URL should be unique. This field may be released by Cloudflare to third parties
              such as the Lumen Database (https://lumendatabase.org/).

          comments: Any additional comments about the infringement not exceeding 2000 characters

          company: Text not exceeding 100 characters. This field may be released by Cloudflare to
              third parties such as the Lumen Database (https://lumendatabase.org/).

          reported_country: Text containing 2 characters

          reported_user_agent: Text not exceeding 255 characters

          tele: Text not exceeding 20 characters. This field may be released by Cloudflare to
              third parties such as the Lumen Database (https://lumendatabase.org/).

          title: Text not exceeding 255 characters

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        report_param: str,
        *,
        account_id: str,
        act: Literal["abuse_ncsei"],
        email: str,
        email2: str,
        host_notification: Literal["send", "send-anon"],
        name: str,
        ncsei_subject_representation: bool,
        owner_notification: Literal["send", "send-anon", "none"],
        urls: str,
        comments: str | Omit = omit,
        company: str | Omit = omit,
        country: str | Omit = omit,
        reported_country: str | Omit = omit,
        reported_user_agent: str | Omit = omit,
        tele: str | Omit = omit,
        title: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> str:
        """
        Submit the Abuse Report of a particular type

        Args:
          report_param: The report type for submitted reports.

          act: The report type for submitted reports.

          email: A valid email of the abuse reporter. This field may be released by Cloudflare to
              third parties such as the Lumen Database (https://lumendatabase.org/).

          email2: Should match the value provided in `email`

          host_notification: Notification type based on the abuse type. NOTE: Copyright (DMCA) and Trademark
              reports cannot be anonymous.

          name: Text not exceeding 255 characters. This field may be released by Cloudflare to
              third parties such as the Lumen Database (https://lumendatabase.org/).

          ncsei_subject_representation: If the submitter is the target of NCSEI in the URLs of the abuse report.

          owner_notification: Notification type based on the abuse type. NOTE: Copyright (DMCA) and Trademark
              reports cannot be anonymous.

          urls: A list of valid URLs separated by ‘\n’ (new line character). The list of the
              URLs should not exceed 250 URLs. All URLs should have the same hostname. Each
              URL should be unique. This field may be released by Cloudflare to third parties
              such as the Lumen Database (https://lumendatabase.org/).

          comments: Any additional comments about the infringement not exceeding 2000 characters

          company: Text not exceeding 100 characters. This field may be released by Cloudflare to
              third parties such as the Lumen Database (https://lumendatabase.org/).

          country: Text not exceeding 255 characters. This field may be released by Cloudflare to
              third parties such as the Lumen Database (https://lumendatabase.org/).

          reported_country: Text containing 2 characters

          reported_user_agent: Text not exceeding 255 characters

          tele: Text not exceeding 20 characters. This field may be released by Cloudflare to
              third parties such as the Lumen Database (https://lumendatabase.org/).

          title: Text not exceeding 255 characters

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(
        [
            "account_id",
            "act",
            "address1",
            "agent_name",
            "agree",
            "city",
            "country",
            "email",
            "email2",
            "host_notification",
            "name",
            "original_work",
            "owner_notification",
            "signature",
            "state",
            "urls",
        ],
        [
            "account_id",
            "act",
            "email",
            "email2",
            "host_notification",
            "justification",
            "name",
            "owner_notification",
            "trademark_number",
            "trademark_office",
            "trademark_symbol",
            "urls",
        ],
        [
            "account_id",
            "act",
            "email",
            "email2",
            "host_notification",
            "justification",
            "name",
            "owner_notification",
            "urls",
        ],
        [
            "account_id",
            "act",
            "email",
            "email2",
            "host_notification",
            "justification",
            "name",
            "ncmec_notification",
            "owner_notification",
            "urls",
        ],
        ["account_id", "act", "email", "email2", "name", "owner_notification", "urls"],
        [
            "account_id",
            "act",
            "email",
            "email2",
            "host_notification",
            "name",
            "ncsei_subject_representation",
            "owner_notification",
            "urls",
        ],
    )
    async def create(
        self,
        report_param: str,
        *,
        account_id: str,
        act: Literal["abuse_dmca"]
        | Literal["abuse_trademark"]
        | Literal["abuse_general"]
        | Literal["abuse_phishing"]
        | Literal["abuse_children"]
        | Literal["abuse_threat"]
        | Literal["abuse_registrar_whois"]
        | Literal["abuse_ncsei"],
        address1: str | Omit = omit,
        agent_name: str | Omit = omit,
        agree: Literal[1] | Omit = omit,
        city: str | Omit = omit,
        country: str | Omit = omit,
        email: str,
        email2: str,
        host_notification: Literal["send"] | Literal["send", "send-anon"] | Omit = omit,
        name: str,
        original_work: str | Omit = omit,
        owner_notification: Literal["send"] | Literal["send", "send-anon", "none"] | Literal["send", "send-anon"],
        signature: str | Omit = omit,
        state: str | Omit = omit,
        urls: str,
        comments: str | Omit = omit,
        company: str | Omit = omit,
        reported_country: str | Omit = omit,
        reported_user_agent: str | Omit = omit,
        tele: str | Omit = omit,
        title: str | Omit = omit,
        justification: str | Omit = omit,
        trademark_number: str | Omit = omit,
        trademark_office: str | Omit = omit,
        trademark_symbol: str | Omit = omit,
        destination_ips: str | Omit = omit,
        ports_protocols: str | Omit = omit,
        source_ips: str | Omit = omit,
        ncmec_notification: Literal["send", "send-anon"] | Omit = omit,
        ncsei_subject_representation: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> str:
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not report_param:
            raise ValueError(f"Expected a non-empty value for `report_param` but received {report_param!r}")
        return await self._post(
            f"/accounts/{account_id}/abuse-reports/{report_param}",
            body=await async_maybe_transform(
                {
                    "act": act,
                    "address1": address1,
                    "agent_name": agent_name,
                    "agree": agree,
                    "city": city,
                    "country": country,
                    "email": email,
                    "email2": email2,
                    "host_notification": host_notification,
                    "name": name,
                    "original_work": original_work,
                    "owner_notification": owner_notification,
                    "signature": signature,
                    "state": state,
                    "urls": urls,
                    "comments": comments,
                    "company": company,
                    "reported_country": reported_country,
                    "reported_user_agent": reported_user_agent,
                    "tele": tele,
                    "title": title,
                    "justification": justification,
                    "trademark_number": trademark_number,
                    "trademark_office": trademark_office,
                    "trademark_symbol": trademark_symbol,
                    "destination_ips": destination_ips,
                    "ports_protocols": ports_protocols,
                    "source_ips": source_ips,
                    "ncmec_notification": ncmec_notification,
                    "ncsei_subject_representation": ncsei_subject_representation,
                },
                abuse_report_create_params.AbuseReportCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[AbuseReportCreateResponse]._unwrapper,
            ),
            cast_to=cast(Type[str], ResultWrapper[str]),
        )

    def list(
        self,
        *,
        account_id: str,
        created_after: str | Omit = omit,
        created_before: str | Omit = omit,
        domain: str | Omit = omit,
        mitigation_status: Literal["pending", "active", "in_review", "cancelled", "removed"] | Omit = omit,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        sort: str | Omit = omit,
        status: Literal["accepted", "in_review"] | Omit = omit,
        type: Literal["PHISH", "GEN", "THREAT", "DMCA", "EMER", "TM", "REG_WHO", "NCSEI", "NETWORK"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[Optional[AbuseReportListResponse], AsyncV4PagePagination[Optional[AbuseReportListResponse]]]:
        """
        List the abuse reports for a given account

        Args:
          created_after: Returns reports created after the specified date

          created_before: Returns reports created before the specified date

          domain: Filter by domain name related to the abuse report

          mitigation_status: Filter reports that have any mitigations in the given status.

          page: Where in pagination to start listing abuse reports

          per_page: How many abuse reports per page to list

          sort: A property to sort by, followed by the order (id, cdate, domain, type, status)

          status: Filter by the status of the report.

          type: Filter by the type of the report.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/abuse-reports",
            page=AsyncV4PagePagination[Optional[AbuseReportListResponse]],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "created_after": created_after,
                        "created_before": created_before,
                        "domain": domain,
                        "mitigation_status": mitigation_status,
                        "page": page,
                        "per_page": per_page,
                        "sort": sort,
                        "status": status,
                        "type": type,
                    },
                    abuse_report_list_params.AbuseReportListParams,
                ),
            ),
            model=AbuseReportListResponse,
        )

    async def get(
        self,
        report_param: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AbuseReportGetResponse:
        """
        Retrieve the details of an abuse report.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not report_param:
            raise ValueError(f"Expected a non-empty value for `report_param` but received {report_param!r}")
        return await self._get(
            f"/accounts/{account_id}/abuse-reports/{report_param}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[AbuseReportGetResponse]._unwrapper,
            ),
            cast_to=cast(Type[AbuseReportGetResponse], ResultWrapper[AbuseReportGetResponse]),
        )


class AbuseReportsResourceWithRawResponse:
    def __init__(self, abuse_reports: AbuseReportsResource) -> None:
        self._abuse_reports = abuse_reports

        self.create = to_raw_response_wrapper(
            abuse_reports.create,
        )
        self.list = to_raw_response_wrapper(
            abuse_reports.list,
        )
        self.get = to_raw_response_wrapper(
            abuse_reports.get,
        )


class AsyncAbuseReportsResourceWithRawResponse:
    def __init__(self, abuse_reports: AsyncAbuseReportsResource) -> None:
        self._abuse_reports = abuse_reports

        self.create = async_to_raw_response_wrapper(
            abuse_reports.create,
        )
        self.list = async_to_raw_response_wrapper(
            abuse_reports.list,
        )
        self.get = async_to_raw_response_wrapper(
            abuse_reports.get,
        )


class AbuseReportsResourceWithStreamingResponse:
    def __init__(self, abuse_reports: AbuseReportsResource) -> None:
        self._abuse_reports = abuse_reports

        self.create = to_streamed_response_wrapper(
            abuse_reports.create,
        )
        self.list = to_streamed_response_wrapper(
            abuse_reports.list,
        )
        self.get = to_streamed_response_wrapper(
            abuse_reports.get,
        )


class AsyncAbuseReportsResourceWithStreamingResponse:
    def __init__(self, abuse_reports: AsyncAbuseReportsResource) -> None:
        self._abuse_reports = abuse_reports

        self.create = async_to_streamed_response_wrapper(
            abuse_reports.create,
        )
        self.list = async_to_streamed_response_wrapper(
            abuse_reports.list,
        )
        self.get = async_to_streamed_response_wrapper(
            abuse_reports.get,
        )
