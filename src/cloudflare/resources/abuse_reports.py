# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, cast
from typing_extensions import Literal, overload

import httpx

from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import (
    required_args,
    maybe_transform,
    async_maybe_transform,
)
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._wrappers import ResultWrapper
from .._base_client import make_request_options
from ..types.abuse_reports import abuse_report_create_params
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
        report_type: Literal[
            "abuse_dmca",
            "abuse_trademark",
            "abuse_general",
            "abuse_phishing",
            "abuse_children",
            "abuse_threat",
            "abuse_registrar_whois",
            "abuse_ncsei",
        ],
        *,
        account_id: str,
        address1: str,
        agent_name: str,
        agree: Literal[0, 1],
        city: str,
        country: str,
        host_notification: Literal["send", "send-anon", "none"],
        original_work: str,
        owner_notification: Literal["send", "send-anon", "none"],
        signature: str,
        state: str,
        act: Literal[
            "abuse_dmca",
            "abuse_trademark",
            "abuse_general",
            "abuse_phishing",
            "abuse_children",
            "abuse_threat",
            "abuse_registrar_whois",
            "abuse_ncsei",
        ]
        | NotGiven = NOT_GIVEN,
        comments: str | NotGiven = NOT_GIVEN,
        company: str | NotGiven = NOT_GIVEN,
        destination_ips: str | NotGiven = NOT_GIVEN,
        email: str | NotGiven = NOT_GIVEN,
        email2: str | NotGiven = NOT_GIVEN,
        justification: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        ncmec_notification: Literal["send", "send-anon", "none"] | NotGiven = NOT_GIVEN,
        ncsei_subject_representation: bool | NotGiven = NOT_GIVEN,
        ports_protocols: str | NotGiven = NOT_GIVEN,
        source_ips: str | NotGiven = NOT_GIVEN,
        tele: str | NotGiven = NOT_GIVEN,
        title: str | NotGiven = NOT_GIVEN,
        trademark_number: str | NotGiven = NOT_GIVEN,
        trademark_office: str | NotGiven = NOT_GIVEN,
        trademark_symbol: str | NotGiven = NOT_GIVEN,
        urls: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> str:
        """
        Submit the Abuse Report of a particular type

        Args:
          report_type: The abuse report type

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

          host_notification: Notification type based on the abuse type. NOTE: Copyright (DMCA) and Trademark
              reports cannot be anonymous.

          original_work: Text not exceeding 255 characters. This field may be released by Cloudflare to
              third parties such as the Lumen Database (https://lumendatabase.org/).

          owner_notification: Notification type based on the abuse type. NOTE: Copyright (DMCA) and Trademark
              reports cannot be anonymous.

          signature: Required for DMCA reports, should be same as Name. An affirmation that all
              information in the report is true and accurate while agreeing to the policies of
              Cloudflare's abuse reports

          state: Text not exceeding 255 characters. This field may be released by Cloudflare to
              third parties such as the Lumen Database (https://lumendatabase.org/).

          act: The abuse report type

          comments: Any additional comments about the infringement not exceeding 2000 characters

          company: Text not exceeding 100 characters. This field may be released by Cloudflare to
              third parties such as the Lumen Database (https://lumendatabase.org/).

          destination_ips: A list of IP addresses separated by ‘ ’ (new line character). The list of
              destination IPs should not exceed 30 IP addresses. Each one of the IP addresses
              ought to be unique

          email: A valid email of the abuse reporter. This field may be released by Cloudflare to
              third parties such as the Lumen Database (https://lumendatabase.org/).

          email2: Should match the value provided in `email`

          justification: A detailed description of the infringement, including any necessary access
              details and the exact steps needed to view the content, not exceeding 5000
              characters

          name: Text not exceeding 255 characters. This field may be released by Cloudflare to
              third parties such as the Lumen Database (https://lumendatabase.org/).

          ncmec_notification: Notification type based on the abuse type. NOTE: Copyright (DMCA) and Trademark
              reports cannot be anonymous.

          ncsei_subject_representation: If the submitter is the target of NCSEI in the URLs of the abuse report.

          ports_protocols: A comma separated list of ports and protocols e.g. 80/TCP, 22/UDP. The total
              size of the field should not exceed 2000 characters. Each individual
              port/protocol should not exceed 100 characters. The list should not have more
              than 30 unique ports and protocols.

          source_ips: A list of IP addresses separated by ‘ ’ (new line character). The list of source
              IPs should not exceed 30 IP addresses. Each one of the IP addresses ought to be
              unique

          tele: Text not exceeding 20 characters. This field may be released by Cloudflare to
              third parties such as the Lumen Database (https://lumendatabase.org/).

          title: Text not exceeding 255 characters

          trademark_number: Text not exceeding 1000 characters

          trademark_office: Text not exceeding 1000 characters

          trademark_symbol: Text not exceeding 1000 characters

          urls: A list of valid URLs separated by ‘ ’ (new line character). The list of the URLs
              should not exceed 250 URLs. All URLs should have the same hostname. Each URL
              should be unique. This field may be released by Cloudflare to third parties such
              as the Lumen Database (https://lumendatabase.org/).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        report_type: Literal[
            "abuse_dmca",
            "abuse_trademark",
            "abuse_general",
            "abuse_phishing",
            "abuse_children",
            "abuse_threat",
            "abuse_registrar_whois",
            "abuse_ncsei",
        ],
        *,
        account_id: str,
        host_notification: Literal["send", "send-anon", "none"],
        justification: str,
        owner_notification: Literal["send", "send-anon", "none"],
        trademark_number: str,
        trademark_office: str,
        trademark_symbol: str,
        act: Literal[
            "abuse_dmca",
            "abuse_trademark",
            "abuse_general",
            "abuse_phishing",
            "abuse_children",
            "abuse_threat",
            "abuse_registrar_whois",
            "abuse_ncsei",
        ]
        | NotGiven = NOT_GIVEN,
        address1: str | NotGiven = NOT_GIVEN,
        agent_name: str | NotGiven = NOT_GIVEN,
        agree: Literal[0, 1] | NotGiven = NOT_GIVEN,
        city: str | NotGiven = NOT_GIVEN,
        comments: str | NotGiven = NOT_GIVEN,
        company: str | NotGiven = NOT_GIVEN,
        country: str | NotGiven = NOT_GIVEN,
        destination_ips: str | NotGiven = NOT_GIVEN,
        email: str | NotGiven = NOT_GIVEN,
        email2: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        ncmec_notification: Literal["send", "send-anon", "none"] | NotGiven = NOT_GIVEN,
        ncsei_subject_representation: bool | NotGiven = NOT_GIVEN,
        original_work: str | NotGiven = NOT_GIVEN,
        ports_protocols: str | NotGiven = NOT_GIVEN,
        signature: str | NotGiven = NOT_GIVEN,
        source_ips: str | NotGiven = NOT_GIVEN,
        state: str | NotGiven = NOT_GIVEN,
        tele: str | NotGiven = NOT_GIVEN,
        title: str | NotGiven = NOT_GIVEN,
        urls: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> str:
        """
        Submit the Abuse Report of a particular type

        Args:
          report_type: The abuse report type

          host_notification: Notification type based on the abuse type. NOTE: Copyright (DMCA) and Trademark
              reports cannot be anonymous.

          justification: A detailed description of the infringement, including any necessary access
              details and the exact steps needed to view the content, not exceeding 5000
              characters

          owner_notification: Notification type based on the abuse type. NOTE: Copyright (DMCA) and Trademark
              reports cannot be anonymous.

          trademark_number: Text not exceeding 1000 characters

          trademark_office: Text not exceeding 1000 characters

          trademark_symbol: Text not exceeding 1000 characters

          act: The abuse report type

          address1: Text not exceeding 100 characters. This field may be released by Cloudflare to
              third parties such as the Lumen Database (https://lumendatabase.org/).

          agent_name: The name of the copyright holder. Text not exceeding 60 characters. This field
              may be released by Cloudflare to third parties such as the Lumen Database
              (https://lumendatabase.org/).

          agree: Can be `0` for false or `1` for true. Must be value: 1 for DMCA reports

          city: Text not exceeding 255 characters. This field may be released by Cloudflare to
              third parties such as the Lumen Database (https://lumendatabase.org/).

          comments: Any additional comments about the infringement not exceeding 2000 characters

          company: Text not exceeding 100 characters. This field may be released by Cloudflare to
              third parties such as the Lumen Database (https://lumendatabase.org/).

          country: Text not exceeding 255 characters. This field may be released by Cloudflare to
              third parties such as the Lumen Database (https://lumendatabase.org/).

          destination_ips: A list of IP addresses separated by ‘ ’ (new line character). The list of
              destination IPs should not exceed 30 IP addresses. Each one of the IP addresses
              ought to be unique

          email: A valid email of the abuse reporter. This field may be released by Cloudflare to
              third parties such as the Lumen Database (https://lumendatabase.org/).

          email2: Should match the value provided in `email`

          name: Text not exceeding 255 characters. This field may be released by Cloudflare to
              third parties such as the Lumen Database (https://lumendatabase.org/).

          ncmec_notification: Notification type based on the abuse type. NOTE: Copyright (DMCA) and Trademark
              reports cannot be anonymous.

          ncsei_subject_representation: If the submitter is the target of NCSEI in the URLs of the abuse report.

          original_work: Text not exceeding 255 characters. This field may be released by Cloudflare to
              third parties such as the Lumen Database (https://lumendatabase.org/).

          ports_protocols: A comma separated list of ports and protocols e.g. 80/TCP, 22/UDP. The total
              size of the field should not exceed 2000 characters. Each individual
              port/protocol should not exceed 100 characters. The list should not have more
              than 30 unique ports and protocols.

          signature: Required for DMCA reports, should be same as Name. An affirmation that all
              information in the report is true and accurate while agreeing to the policies of
              Cloudflare's abuse reports

          source_ips: A list of IP addresses separated by ‘ ’ (new line character). The list of source
              IPs should not exceed 30 IP addresses. Each one of the IP addresses ought to be
              unique

          state: Text not exceeding 255 characters. This field may be released by Cloudflare to
              third parties such as the Lumen Database (https://lumendatabase.org/).

          tele: Text not exceeding 20 characters. This field may be released by Cloudflare to
              third parties such as the Lumen Database (https://lumendatabase.org/).

          title: Text not exceeding 255 characters

          urls: A list of valid URLs separated by ‘ ’ (new line character). The list of the URLs
              should not exceed 250 URLs. All URLs should have the same hostname. Each URL
              should be unique. This field may be released by Cloudflare to third parties such
              as the Lumen Database (https://lumendatabase.org/).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        report_type: Literal[
            "abuse_dmca",
            "abuse_trademark",
            "abuse_general",
            "abuse_phishing",
            "abuse_children",
            "abuse_threat",
            "abuse_registrar_whois",
            "abuse_ncsei",
        ],
        *,
        account_id: str,
        host_notification: Literal["send", "send-anon", "none"],
        justification: str,
        owner_notification: Literal["send", "send-anon", "none"],
        act: Literal[
            "abuse_dmca",
            "abuse_trademark",
            "abuse_general",
            "abuse_phishing",
            "abuse_children",
            "abuse_threat",
            "abuse_registrar_whois",
            "abuse_ncsei",
        ]
        | NotGiven = NOT_GIVEN,
        address1: str | NotGiven = NOT_GIVEN,
        agent_name: str | NotGiven = NOT_GIVEN,
        agree: Literal[0, 1] | NotGiven = NOT_GIVEN,
        city: str | NotGiven = NOT_GIVEN,
        comments: str | NotGiven = NOT_GIVEN,
        company: str | NotGiven = NOT_GIVEN,
        country: str | NotGiven = NOT_GIVEN,
        destination_ips: str | NotGiven = NOT_GIVEN,
        email: str | NotGiven = NOT_GIVEN,
        email2: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        ncmec_notification: Literal["send", "send-anon", "none"] | NotGiven = NOT_GIVEN,
        ncsei_subject_representation: bool | NotGiven = NOT_GIVEN,
        original_work: str | NotGiven = NOT_GIVEN,
        ports_protocols: str | NotGiven = NOT_GIVEN,
        signature: str | NotGiven = NOT_GIVEN,
        source_ips: str | NotGiven = NOT_GIVEN,
        state: str | NotGiven = NOT_GIVEN,
        tele: str | NotGiven = NOT_GIVEN,
        title: str | NotGiven = NOT_GIVEN,
        trademark_number: str | NotGiven = NOT_GIVEN,
        trademark_office: str | NotGiven = NOT_GIVEN,
        trademark_symbol: str | NotGiven = NOT_GIVEN,
        urls: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> str:
        """
        Submit the Abuse Report of a particular type

        Args:
          report_type: The abuse report type

          host_notification: Notification type based on the abuse type. NOTE: Copyright (DMCA) and Trademark
              reports cannot be anonymous.

          justification: A detailed description of the infringement, including any necessary access
              details and the exact steps needed to view the content, not exceeding 5000
              characters

          owner_notification: Notification type based on the abuse type. NOTE: Copyright (DMCA) and Trademark
              reports cannot be anonymous.

          act: The abuse report type

          address1: Text not exceeding 100 characters. This field may be released by Cloudflare to
              third parties such as the Lumen Database (https://lumendatabase.org/).

          agent_name: The name of the copyright holder. Text not exceeding 60 characters. This field
              may be released by Cloudflare to third parties such as the Lumen Database
              (https://lumendatabase.org/).

          agree: Can be `0` for false or `1` for true. Must be value: 1 for DMCA reports

          city: Text not exceeding 255 characters. This field may be released by Cloudflare to
              third parties such as the Lumen Database (https://lumendatabase.org/).

          comments: Any additional comments about the infringement not exceeding 2000 characters

          company: Text not exceeding 100 characters. This field may be released by Cloudflare to
              third parties such as the Lumen Database (https://lumendatabase.org/).

          country: Text not exceeding 255 characters. This field may be released by Cloudflare to
              third parties such as the Lumen Database (https://lumendatabase.org/).

          destination_ips: A list of IP addresses separated by ‘ ’ (new line character). The list of
              destination IPs should not exceed 30 IP addresses. Each one of the IP addresses
              ought to be unique

          email: A valid email of the abuse reporter. This field may be released by Cloudflare to
              third parties such as the Lumen Database (https://lumendatabase.org/).

          email2: Should match the value provided in `email`

          name: Text not exceeding 255 characters. This field may be released by Cloudflare to
              third parties such as the Lumen Database (https://lumendatabase.org/).

          ncmec_notification: Notification type based on the abuse type. NOTE: Copyright (DMCA) and Trademark
              reports cannot be anonymous.

          ncsei_subject_representation: If the submitter is the target of NCSEI in the URLs of the abuse report.

          original_work: Text not exceeding 255 characters. This field may be released by Cloudflare to
              third parties such as the Lumen Database (https://lumendatabase.org/).

          ports_protocols: A comma separated list of ports and protocols e.g. 80/TCP, 22/UDP. The total
              size of the field should not exceed 2000 characters. Each individual
              port/protocol should not exceed 100 characters. The list should not have more
              than 30 unique ports and protocols.

          signature: Required for DMCA reports, should be same as Name. An affirmation that all
              information in the report is true and accurate while agreeing to the policies of
              Cloudflare's abuse reports

          source_ips: A list of IP addresses separated by ‘ ’ (new line character). The list of source
              IPs should not exceed 30 IP addresses. Each one of the IP addresses ought to be
              unique

          state: Text not exceeding 255 characters. This field may be released by Cloudflare to
              third parties such as the Lumen Database (https://lumendatabase.org/).

          tele: Text not exceeding 20 characters. This field may be released by Cloudflare to
              third parties such as the Lumen Database (https://lumendatabase.org/).

          title: Text not exceeding 255 characters

          trademark_number: Text not exceeding 1000 characters

          trademark_office: Text not exceeding 1000 characters

          trademark_symbol: Text not exceeding 1000 characters

          urls: A list of valid URLs separated by ‘ ’ (new line character). The list of the URLs
              should not exceed 250 URLs. All URLs should have the same hostname. Each URL
              should be unique. This field may be released by Cloudflare to third parties such
              as the Lumen Database (https://lumendatabase.org/).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        report_type: Literal[
            "abuse_dmca",
            "abuse_trademark",
            "abuse_general",
            "abuse_phishing",
            "abuse_children",
            "abuse_threat",
            "abuse_registrar_whois",
            "abuse_ncsei",
        ],
        *,
        account_id: str,
        host_notification: Literal["send", "send-anon", "none"],
        justification: str,
        owner_notification: Literal["send", "send-anon", "none"],
        act: Literal[
            "abuse_dmca",
            "abuse_trademark",
            "abuse_general",
            "abuse_phishing",
            "abuse_children",
            "abuse_threat",
            "abuse_registrar_whois",
            "abuse_ncsei",
        ]
        | NotGiven = NOT_GIVEN,
        address1: str | NotGiven = NOT_GIVEN,
        agent_name: str | NotGiven = NOT_GIVEN,
        agree: Literal[0, 1] | NotGiven = NOT_GIVEN,
        city: str | NotGiven = NOT_GIVEN,
        comments: str | NotGiven = NOT_GIVEN,
        company: str | NotGiven = NOT_GIVEN,
        country: str | NotGiven = NOT_GIVEN,
        destination_ips: str | NotGiven = NOT_GIVEN,
        email: str | NotGiven = NOT_GIVEN,
        email2: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        ncmec_notification: Literal["send", "send-anon", "none"] | NotGiven = NOT_GIVEN,
        ncsei_subject_representation: bool | NotGiven = NOT_GIVEN,
        original_work: str | NotGiven = NOT_GIVEN,
        ports_protocols: str | NotGiven = NOT_GIVEN,
        signature: str | NotGiven = NOT_GIVEN,
        source_ips: str | NotGiven = NOT_GIVEN,
        state: str | NotGiven = NOT_GIVEN,
        tele: str | NotGiven = NOT_GIVEN,
        title: str | NotGiven = NOT_GIVEN,
        trademark_number: str | NotGiven = NOT_GIVEN,
        trademark_office: str | NotGiven = NOT_GIVEN,
        trademark_symbol: str | NotGiven = NOT_GIVEN,
        urls: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> str:
        """
        Submit the Abuse Report of a particular type

        Args:
          report_type: The abuse report type

          host_notification: Notification type based on the abuse type. NOTE: Copyright (DMCA) and Trademark
              reports cannot be anonymous.

          justification: A detailed description of the infringement, including any necessary access
              details and the exact steps needed to view the content, not exceeding 5000
              characters

          owner_notification: Notification type based on the abuse type. NOTE: Copyright (DMCA) and Trademark
              reports cannot be anonymous.

          act: The abuse report type

          address1: Text not exceeding 100 characters. This field may be released by Cloudflare to
              third parties such as the Lumen Database (https://lumendatabase.org/).

          agent_name: The name of the copyright holder. Text not exceeding 60 characters. This field
              may be released by Cloudflare to third parties such as the Lumen Database
              (https://lumendatabase.org/).

          agree: Can be `0` for false or `1` for true. Must be value: 1 for DMCA reports

          city: Text not exceeding 255 characters. This field may be released by Cloudflare to
              third parties such as the Lumen Database (https://lumendatabase.org/).

          comments: Any additional comments about the infringement not exceeding 2000 characters

          company: Text not exceeding 100 characters. This field may be released by Cloudflare to
              third parties such as the Lumen Database (https://lumendatabase.org/).

          country: Text not exceeding 255 characters. This field may be released by Cloudflare to
              third parties such as the Lumen Database (https://lumendatabase.org/).

          destination_ips: A list of IP addresses separated by ‘ ’ (new line character). The list of
              destination IPs should not exceed 30 IP addresses. Each one of the IP addresses
              ought to be unique

          email: A valid email of the abuse reporter. This field may be released by Cloudflare to
              third parties such as the Lumen Database (https://lumendatabase.org/).

          email2: Should match the value provided in `email`

          name: Text not exceeding 255 characters. This field may be released by Cloudflare to
              third parties such as the Lumen Database (https://lumendatabase.org/).

          ncmec_notification: Notification type based on the abuse type. NOTE: Copyright (DMCA) and Trademark
              reports cannot be anonymous.

          ncsei_subject_representation: If the submitter is the target of NCSEI in the URLs of the abuse report.

          original_work: Text not exceeding 255 characters. This field may be released by Cloudflare to
              third parties such as the Lumen Database (https://lumendatabase.org/).

          ports_protocols: A comma separated list of ports and protocols e.g. 80/TCP, 22/UDP. The total
              size of the field should not exceed 2000 characters. Each individual
              port/protocol should not exceed 100 characters. The list should not have more
              than 30 unique ports and protocols.

          signature: Required for DMCA reports, should be same as Name. An affirmation that all
              information in the report is true and accurate while agreeing to the policies of
              Cloudflare's abuse reports

          source_ips: A list of IP addresses separated by ‘ ’ (new line character). The list of source
              IPs should not exceed 30 IP addresses. Each one of the IP addresses ought to be
              unique

          state: Text not exceeding 255 characters. This field may be released by Cloudflare to
              third parties such as the Lumen Database (https://lumendatabase.org/).

          tele: Text not exceeding 20 characters. This field may be released by Cloudflare to
              third parties such as the Lumen Database (https://lumendatabase.org/).

          title: Text not exceeding 255 characters

          trademark_number: Text not exceeding 1000 characters

          trademark_office: Text not exceeding 1000 characters

          trademark_symbol: Text not exceeding 1000 characters

          urls: A list of valid URLs separated by ‘ ’ (new line character). The list of the URLs
              should not exceed 250 URLs. All URLs should have the same hostname. Each URL
              should be unique. This field may be released by Cloudflare to third parties such
              as the Lumen Database (https://lumendatabase.org/).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        report_type: Literal[
            "abuse_dmca",
            "abuse_trademark",
            "abuse_general",
            "abuse_phishing",
            "abuse_children",
            "abuse_threat",
            "abuse_registrar_whois",
            "abuse_ncsei",
        ],
        *,
        account_id: str,
        host_notification: Literal["send", "send-anon", "none"],
        justification: str,
        ncmec_notification: Literal["send", "send-anon", "none"],
        owner_notification: Literal["send", "send-anon", "none"],
        act: Literal[
            "abuse_dmca",
            "abuse_trademark",
            "abuse_general",
            "abuse_phishing",
            "abuse_children",
            "abuse_threat",
            "abuse_registrar_whois",
            "abuse_ncsei",
        ]
        | NotGiven = NOT_GIVEN,
        address1: str | NotGiven = NOT_GIVEN,
        agent_name: str | NotGiven = NOT_GIVEN,
        agree: Literal[0, 1] | NotGiven = NOT_GIVEN,
        city: str | NotGiven = NOT_GIVEN,
        comments: str | NotGiven = NOT_GIVEN,
        company: str | NotGiven = NOT_GIVEN,
        country: str | NotGiven = NOT_GIVEN,
        destination_ips: str | NotGiven = NOT_GIVEN,
        email: str | NotGiven = NOT_GIVEN,
        email2: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        ncsei_subject_representation: bool | NotGiven = NOT_GIVEN,
        original_work: str | NotGiven = NOT_GIVEN,
        ports_protocols: str | NotGiven = NOT_GIVEN,
        signature: str | NotGiven = NOT_GIVEN,
        source_ips: str | NotGiven = NOT_GIVEN,
        state: str | NotGiven = NOT_GIVEN,
        tele: str | NotGiven = NOT_GIVEN,
        title: str | NotGiven = NOT_GIVEN,
        trademark_number: str | NotGiven = NOT_GIVEN,
        trademark_office: str | NotGiven = NOT_GIVEN,
        trademark_symbol: str | NotGiven = NOT_GIVEN,
        urls: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> str:
        """
        Submit the Abuse Report of a particular type

        Args:
          report_type: The abuse report type

          host_notification: Notification type based on the abuse type. NOTE: Copyright (DMCA) and Trademark
              reports cannot be anonymous.

          justification: A detailed description of the infringement, including any necessary access
              details and the exact steps needed to view the content, not exceeding 5000
              characters

          ncmec_notification: Notification type based on the abuse type. NOTE: Copyright (DMCA) and Trademark
              reports cannot be anonymous.

          owner_notification: Notification type based on the abuse type. NOTE: Copyright (DMCA) and Trademark
              reports cannot be anonymous.

          act: The abuse report type

          address1: Text not exceeding 100 characters. This field may be released by Cloudflare to
              third parties such as the Lumen Database (https://lumendatabase.org/).

          agent_name: The name of the copyright holder. Text not exceeding 60 characters. This field
              may be released by Cloudflare to third parties such as the Lumen Database
              (https://lumendatabase.org/).

          agree: Can be `0` for false or `1` for true. Must be value: 1 for DMCA reports

          city: Text not exceeding 255 characters. This field may be released by Cloudflare to
              third parties such as the Lumen Database (https://lumendatabase.org/).

          comments: Any additional comments about the infringement not exceeding 2000 characters

          company: Text not exceeding 100 characters. This field may be released by Cloudflare to
              third parties such as the Lumen Database (https://lumendatabase.org/).

          country: Text not exceeding 255 characters. This field may be released by Cloudflare to
              third parties such as the Lumen Database (https://lumendatabase.org/).

          destination_ips: A list of IP addresses separated by ‘ ’ (new line character). The list of
              destination IPs should not exceed 30 IP addresses. Each one of the IP addresses
              ought to be unique

          email: A valid email of the abuse reporter. This field may be released by Cloudflare to
              third parties such as the Lumen Database (https://lumendatabase.org/).

          email2: Should match the value provided in `email`

          name: Text not exceeding 255 characters. This field may be released by Cloudflare to
              third parties such as the Lumen Database (https://lumendatabase.org/).

          ncsei_subject_representation: If the submitter is the target of NCSEI in the URLs of the abuse report.

          original_work: Text not exceeding 255 characters. This field may be released by Cloudflare to
              third parties such as the Lumen Database (https://lumendatabase.org/).

          ports_protocols: A comma separated list of ports and protocols e.g. 80/TCP, 22/UDP. The total
              size of the field should not exceed 2000 characters. Each individual
              port/protocol should not exceed 100 characters. The list should not have more
              than 30 unique ports and protocols.

          signature: Required for DMCA reports, should be same as Name. An affirmation that all
              information in the report is true and accurate while agreeing to the policies of
              Cloudflare's abuse reports

          source_ips: A list of IP addresses separated by ‘ ’ (new line character). The list of source
              IPs should not exceed 30 IP addresses. Each one of the IP addresses ought to be
              unique

          state: Text not exceeding 255 characters. This field may be released by Cloudflare to
              third parties such as the Lumen Database (https://lumendatabase.org/).

          tele: Text not exceeding 20 characters. This field may be released by Cloudflare to
              third parties such as the Lumen Database (https://lumendatabase.org/).

          title: Text not exceeding 255 characters

          trademark_number: Text not exceeding 1000 characters

          trademark_office: Text not exceeding 1000 characters

          trademark_symbol: Text not exceeding 1000 characters

          urls: A list of valid URLs separated by ‘ ’ (new line character). The list of the URLs
              should not exceed 250 URLs. All URLs should have the same hostname. Each URL
              should be unique. This field may be released by Cloudflare to third parties such
              as the Lumen Database (https://lumendatabase.org/).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        report_type: Literal[
            "abuse_dmca",
            "abuse_trademark",
            "abuse_general",
            "abuse_phishing",
            "abuse_children",
            "abuse_threat",
            "abuse_registrar_whois",
            "abuse_ncsei",
        ],
        *,
        account_id: str,
        host_notification: Literal["send", "send-anon", "none"],
        justification: str,
        owner_notification: Literal["send", "send-anon", "none"],
        act: Literal[
            "abuse_dmca",
            "abuse_trademark",
            "abuse_general",
            "abuse_phishing",
            "abuse_children",
            "abuse_threat",
            "abuse_registrar_whois",
            "abuse_ncsei",
        ]
        | NotGiven = NOT_GIVEN,
        address1: str | NotGiven = NOT_GIVEN,
        agent_name: str | NotGiven = NOT_GIVEN,
        agree: Literal[0, 1] | NotGiven = NOT_GIVEN,
        city: str | NotGiven = NOT_GIVEN,
        comments: str | NotGiven = NOT_GIVEN,
        company: str | NotGiven = NOT_GIVEN,
        country: str | NotGiven = NOT_GIVEN,
        destination_ips: str | NotGiven = NOT_GIVEN,
        email: str | NotGiven = NOT_GIVEN,
        email2: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        ncmec_notification: Literal["send", "send-anon", "none"] | NotGiven = NOT_GIVEN,
        ncsei_subject_representation: bool | NotGiven = NOT_GIVEN,
        original_work: str | NotGiven = NOT_GIVEN,
        ports_protocols: str | NotGiven = NOT_GIVEN,
        signature: str | NotGiven = NOT_GIVEN,
        source_ips: str | NotGiven = NOT_GIVEN,
        state: str | NotGiven = NOT_GIVEN,
        tele: str | NotGiven = NOT_GIVEN,
        title: str | NotGiven = NOT_GIVEN,
        trademark_number: str | NotGiven = NOT_GIVEN,
        trademark_office: str | NotGiven = NOT_GIVEN,
        trademark_symbol: str | NotGiven = NOT_GIVEN,
        urls: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> str:
        """
        Submit the Abuse Report of a particular type

        Args:
          report_type: The abuse report type

          host_notification: Notification type based on the abuse type. NOTE: Copyright (DMCA) and Trademark
              reports cannot be anonymous.

          justification: A detailed description of the infringement, including any necessary access
              details and the exact steps needed to view the content, not exceeding 5000
              characters

          owner_notification: Notification type based on the abuse type. NOTE: Copyright (DMCA) and Trademark
              reports cannot be anonymous.

          act: The abuse report type

          address1: Text not exceeding 100 characters. This field may be released by Cloudflare to
              third parties such as the Lumen Database (https://lumendatabase.org/).

          agent_name: The name of the copyright holder. Text not exceeding 60 characters. This field
              may be released by Cloudflare to third parties such as the Lumen Database
              (https://lumendatabase.org/).

          agree: Can be `0` for false or `1` for true. Must be value: 1 for DMCA reports

          city: Text not exceeding 255 characters. This field may be released by Cloudflare to
              third parties such as the Lumen Database (https://lumendatabase.org/).

          comments: Any additional comments about the infringement not exceeding 2000 characters

          company: Text not exceeding 100 characters. This field may be released by Cloudflare to
              third parties such as the Lumen Database (https://lumendatabase.org/).

          country: Text not exceeding 255 characters. This field may be released by Cloudflare to
              third parties such as the Lumen Database (https://lumendatabase.org/).

          destination_ips: A list of IP addresses separated by ‘ ’ (new line character). The list of
              destination IPs should not exceed 30 IP addresses. Each one of the IP addresses
              ought to be unique

          email: A valid email of the abuse reporter. This field may be released by Cloudflare to
              third parties such as the Lumen Database (https://lumendatabase.org/).

          email2: Should match the value provided in `email`

          name: Text not exceeding 255 characters. This field may be released by Cloudflare to
              third parties such as the Lumen Database (https://lumendatabase.org/).

          ncmec_notification: Notification type based on the abuse type. NOTE: Copyright (DMCA) and Trademark
              reports cannot be anonymous.

          ncsei_subject_representation: If the submitter is the target of NCSEI in the URLs of the abuse report.

          original_work: Text not exceeding 255 characters. This field may be released by Cloudflare to
              third parties such as the Lumen Database (https://lumendatabase.org/).

          ports_protocols: A comma separated list of ports and protocols e.g. 80/TCP, 22/UDP. The total
              size of the field should not exceed 2000 characters. Each individual
              port/protocol should not exceed 100 characters. The list should not have more
              than 30 unique ports and protocols.

          signature: Required for DMCA reports, should be same as Name. An affirmation that all
              information in the report is true and accurate while agreeing to the policies of
              Cloudflare's abuse reports

          source_ips: A list of IP addresses separated by ‘ ’ (new line character). The list of source
              IPs should not exceed 30 IP addresses. Each one of the IP addresses ought to be
              unique

          state: Text not exceeding 255 characters. This field may be released by Cloudflare to
              third parties such as the Lumen Database (https://lumendatabase.org/).

          tele: Text not exceeding 20 characters. This field may be released by Cloudflare to
              third parties such as the Lumen Database (https://lumendatabase.org/).

          title: Text not exceeding 255 characters

          trademark_number: Text not exceeding 1000 characters

          trademark_office: Text not exceeding 1000 characters

          trademark_symbol: Text not exceeding 1000 characters

          urls: A list of valid URLs separated by ‘ ’ (new line character). The list of the URLs
              should not exceed 250 URLs. All URLs should have the same hostname. Each URL
              should be unique. This field may be released by Cloudflare to third parties such
              as the Lumen Database (https://lumendatabase.org/).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        report_type: Literal[
            "abuse_dmca",
            "abuse_trademark",
            "abuse_general",
            "abuse_phishing",
            "abuse_children",
            "abuse_threat",
            "abuse_registrar_whois",
            "abuse_ncsei",
        ],
        *,
        account_id: str,
        owner_notification: Literal["send", "send-anon", "none"],
        act: Literal[
            "abuse_dmca",
            "abuse_trademark",
            "abuse_general",
            "abuse_phishing",
            "abuse_children",
            "abuse_threat",
            "abuse_registrar_whois",
            "abuse_ncsei",
        ]
        | NotGiven = NOT_GIVEN,
        address1: str | NotGiven = NOT_GIVEN,
        agent_name: str | NotGiven = NOT_GIVEN,
        agree: Literal[0, 1] | NotGiven = NOT_GIVEN,
        city: str | NotGiven = NOT_GIVEN,
        comments: str | NotGiven = NOT_GIVEN,
        company: str | NotGiven = NOT_GIVEN,
        country: str | NotGiven = NOT_GIVEN,
        destination_ips: str | NotGiven = NOT_GIVEN,
        email: str | NotGiven = NOT_GIVEN,
        email2: str | NotGiven = NOT_GIVEN,
        host_notification: Literal["send", "send-anon", "none"] | NotGiven = NOT_GIVEN,
        justification: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        ncmec_notification: Literal["send", "send-anon", "none"] | NotGiven = NOT_GIVEN,
        ncsei_subject_representation: bool | NotGiven = NOT_GIVEN,
        original_work: str | NotGiven = NOT_GIVEN,
        ports_protocols: str | NotGiven = NOT_GIVEN,
        signature: str | NotGiven = NOT_GIVEN,
        source_ips: str | NotGiven = NOT_GIVEN,
        state: str | NotGiven = NOT_GIVEN,
        tele: str | NotGiven = NOT_GIVEN,
        title: str | NotGiven = NOT_GIVEN,
        trademark_number: str | NotGiven = NOT_GIVEN,
        trademark_office: str | NotGiven = NOT_GIVEN,
        trademark_symbol: str | NotGiven = NOT_GIVEN,
        urls: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> str:
        """
        Submit the Abuse Report of a particular type

        Args:
          report_type: The abuse report type

          owner_notification: Notification type based on the abuse type. NOTE: Copyright (DMCA) and Trademark
              reports cannot be anonymous.

          act: The abuse report type

          address1: Text not exceeding 100 characters. This field may be released by Cloudflare to
              third parties such as the Lumen Database (https://lumendatabase.org/).

          agent_name: The name of the copyright holder. Text not exceeding 60 characters. This field
              may be released by Cloudflare to third parties such as the Lumen Database
              (https://lumendatabase.org/).

          agree: Can be `0` for false or `1` for true. Must be value: 1 for DMCA reports

          city: Text not exceeding 255 characters. This field may be released by Cloudflare to
              third parties such as the Lumen Database (https://lumendatabase.org/).

          comments: Any additional comments about the infringement not exceeding 2000 characters

          company: Text not exceeding 100 characters. This field may be released by Cloudflare to
              third parties such as the Lumen Database (https://lumendatabase.org/).

          country: Text not exceeding 255 characters. This field may be released by Cloudflare to
              third parties such as the Lumen Database (https://lumendatabase.org/).

          destination_ips: A list of IP addresses separated by ‘ ’ (new line character). The list of
              destination IPs should not exceed 30 IP addresses. Each one of the IP addresses
              ought to be unique

          email: A valid email of the abuse reporter. This field may be released by Cloudflare to
              third parties such as the Lumen Database (https://lumendatabase.org/).

          email2: Should match the value provided in `email`

          host_notification: Notification type based on the abuse type. NOTE: Copyright (DMCA) and Trademark
              reports cannot be anonymous.

          justification: A detailed description of the infringement, including any necessary access
              details and the exact steps needed to view the content, not exceeding 5000
              characters

          name: Text not exceeding 255 characters. This field may be released by Cloudflare to
              third parties such as the Lumen Database (https://lumendatabase.org/).

          ncmec_notification: Notification type based on the abuse type. NOTE: Copyright (DMCA) and Trademark
              reports cannot be anonymous.

          ncsei_subject_representation: If the submitter is the target of NCSEI in the URLs of the abuse report.

          original_work: Text not exceeding 255 characters. This field may be released by Cloudflare to
              third parties such as the Lumen Database (https://lumendatabase.org/).

          ports_protocols: A comma separated list of ports and protocols e.g. 80/TCP, 22/UDP. The total
              size of the field should not exceed 2000 characters. Each individual
              port/protocol should not exceed 100 characters. The list should not have more
              than 30 unique ports and protocols.

          signature: Required for DMCA reports, should be same as Name. An affirmation that all
              information in the report is true and accurate while agreeing to the policies of
              Cloudflare's abuse reports

          source_ips: A list of IP addresses separated by ‘ ’ (new line character). The list of source
              IPs should not exceed 30 IP addresses. Each one of the IP addresses ought to be
              unique

          state: Text not exceeding 255 characters. This field may be released by Cloudflare to
              third parties such as the Lumen Database (https://lumendatabase.org/).

          tele: Text not exceeding 20 characters. This field may be released by Cloudflare to
              third parties such as the Lumen Database (https://lumendatabase.org/).

          title: Text not exceeding 255 characters

          trademark_number: Text not exceeding 1000 characters

          trademark_office: Text not exceeding 1000 characters

          trademark_symbol: Text not exceeding 1000 characters

          urls: A list of valid URLs separated by ‘ ’ (new line character). The list of the URLs
              should not exceed 250 URLs. All URLs should have the same hostname. Each URL
              should be unique. This field may be released by Cloudflare to third parties such
              as the Lumen Database (https://lumendatabase.org/).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        report_type: Literal[
            "abuse_dmca",
            "abuse_trademark",
            "abuse_general",
            "abuse_phishing",
            "abuse_children",
            "abuse_threat",
            "abuse_registrar_whois",
            "abuse_ncsei",
        ],
        *,
        account_id: str,
        host_notification: Literal["send", "send-anon", "none"],
        ncsei_subject_representation: bool,
        owner_notification: Literal["send", "send-anon", "none"],
        act: Literal[
            "abuse_dmca",
            "abuse_trademark",
            "abuse_general",
            "abuse_phishing",
            "abuse_children",
            "abuse_threat",
            "abuse_registrar_whois",
            "abuse_ncsei",
        ]
        | NotGiven = NOT_GIVEN,
        address1: str | NotGiven = NOT_GIVEN,
        agent_name: str | NotGiven = NOT_GIVEN,
        agree: Literal[0, 1] | NotGiven = NOT_GIVEN,
        city: str | NotGiven = NOT_GIVEN,
        comments: str | NotGiven = NOT_GIVEN,
        company: str | NotGiven = NOT_GIVEN,
        country: str | NotGiven = NOT_GIVEN,
        destination_ips: str | NotGiven = NOT_GIVEN,
        email: str | NotGiven = NOT_GIVEN,
        email2: str | NotGiven = NOT_GIVEN,
        justification: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        ncmec_notification: Literal["send", "send-anon", "none"] | NotGiven = NOT_GIVEN,
        original_work: str | NotGiven = NOT_GIVEN,
        ports_protocols: str | NotGiven = NOT_GIVEN,
        signature: str | NotGiven = NOT_GIVEN,
        source_ips: str | NotGiven = NOT_GIVEN,
        state: str | NotGiven = NOT_GIVEN,
        tele: str | NotGiven = NOT_GIVEN,
        title: str | NotGiven = NOT_GIVEN,
        trademark_number: str | NotGiven = NOT_GIVEN,
        trademark_office: str | NotGiven = NOT_GIVEN,
        trademark_symbol: str | NotGiven = NOT_GIVEN,
        urls: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> str:
        """
        Submit the Abuse Report of a particular type

        Args:
          report_type: The abuse report type

          host_notification: Notification type based on the abuse type. NOTE: Copyright (DMCA) and Trademark
              reports cannot be anonymous.

          ncsei_subject_representation: If the submitter is the target of NCSEI in the URLs of the abuse report.

          owner_notification: Notification type based on the abuse type. NOTE: Copyright (DMCA) and Trademark
              reports cannot be anonymous.

          act: The abuse report type

          address1: Text not exceeding 100 characters. This field may be released by Cloudflare to
              third parties such as the Lumen Database (https://lumendatabase.org/).

          agent_name: The name of the copyright holder. Text not exceeding 60 characters. This field
              may be released by Cloudflare to third parties such as the Lumen Database
              (https://lumendatabase.org/).

          agree: Can be `0` for false or `1` for true. Must be value: 1 for DMCA reports

          city: Text not exceeding 255 characters. This field may be released by Cloudflare to
              third parties such as the Lumen Database (https://lumendatabase.org/).

          comments: Any additional comments about the infringement not exceeding 2000 characters

          company: Text not exceeding 100 characters. This field may be released by Cloudflare to
              third parties such as the Lumen Database (https://lumendatabase.org/).

          country: Text not exceeding 255 characters. This field may be released by Cloudflare to
              third parties such as the Lumen Database (https://lumendatabase.org/).

          destination_ips: A list of IP addresses separated by ‘ ’ (new line character). The list of
              destination IPs should not exceed 30 IP addresses. Each one of the IP addresses
              ought to be unique

          email: A valid email of the abuse reporter. This field may be released by Cloudflare to
              third parties such as the Lumen Database (https://lumendatabase.org/).

          email2: Should match the value provided in `email`

          justification: A detailed description of the infringement, including any necessary access
              details and the exact steps needed to view the content, not exceeding 5000
              characters

          name: Text not exceeding 255 characters. This field may be released by Cloudflare to
              third parties such as the Lumen Database (https://lumendatabase.org/).

          ncmec_notification: Notification type based on the abuse type. NOTE: Copyright (DMCA) and Trademark
              reports cannot be anonymous.

          original_work: Text not exceeding 255 characters. This field may be released by Cloudflare to
              third parties such as the Lumen Database (https://lumendatabase.org/).

          ports_protocols: A comma separated list of ports and protocols e.g. 80/TCP, 22/UDP. The total
              size of the field should not exceed 2000 characters. Each individual
              port/protocol should not exceed 100 characters. The list should not have more
              than 30 unique ports and protocols.

          signature: Required for DMCA reports, should be same as Name. An affirmation that all
              information in the report is true and accurate while agreeing to the policies of
              Cloudflare's abuse reports

          source_ips: A list of IP addresses separated by ‘ ’ (new line character). The list of source
              IPs should not exceed 30 IP addresses. Each one of the IP addresses ought to be
              unique

          state: Text not exceeding 255 characters. This field may be released by Cloudflare to
              third parties such as the Lumen Database (https://lumendatabase.org/).

          tele: Text not exceeding 20 characters. This field may be released by Cloudflare to
              third parties such as the Lumen Database (https://lumendatabase.org/).

          title: Text not exceeding 255 characters

          trademark_number: Text not exceeding 1000 characters

          trademark_office: Text not exceeding 1000 characters

          trademark_symbol: Text not exceeding 1000 characters

          urls: A list of valid URLs separated by ‘ ’ (new line character). The list of the URLs
              should not exceed 250 URLs. All URLs should have the same hostname. Each URL
              should be unique. This field may be released by Cloudflare to third parties such
              as the Lumen Database (https://lumendatabase.org/).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(
        [
            "account_id",
            "address1",
            "agent_name",
            "agree",
            "city",
            "country",
            "host_notification",
            "original_work",
            "owner_notification",
            "signature",
            "state",
        ],
        [
            "account_id",
            "host_notification",
            "justification",
            "owner_notification",
            "trademark_number",
            "trademark_office",
            "trademark_symbol",
        ],
        ["account_id", "host_notification", "justification", "owner_notification"],
        ["account_id", "host_notification", "justification", "ncmec_notification", "owner_notification"],
        ["account_id", "owner_notification"],
        ["account_id", "host_notification", "ncsei_subject_representation", "owner_notification"],
    )
    def create(
        self,
        report_type: Literal[
            "abuse_dmca",
            "abuse_trademark",
            "abuse_general",
            "abuse_phishing",
            "abuse_children",
            "abuse_threat",
            "abuse_registrar_whois",
            "abuse_ncsei",
        ],
        *,
        account_id: str,
        address1: str | NotGiven = NOT_GIVEN,
        agent_name: str | NotGiven = NOT_GIVEN,
        agree: Literal[0, 1] | NotGiven = NOT_GIVEN,
        city: str | NotGiven = NOT_GIVEN,
        country: str | NotGiven = NOT_GIVEN,
        host_notification: Literal["send", "send-anon", "none"] | NotGiven = NOT_GIVEN,
        original_work: str | NotGiven = NOT_GIVEN,
        owner_notification: Literal["send", "send-anon", "none"],
        signature: str | NotGiven = NOT_GIVEN,
        state: str | NotGiven = NOT_GIVEN,
        act: Literal[
            "abuse_dmca",
            "abuse_trademark",
            "abuse_general",
            "abuse_phishing",
            "abuse_children",
            "abuse_threat",
            "abuse_registrar_whois",
            "abuse_ncsei",
        ]
        | NotGiven = NOT_GIVEN,
        comments: str | NotGiven = NOT_GIVEN,
        company: str | NotGiven = NOT_GIVEN,
        destination_ips: str | NotGiven = NOT_GIVEN,
        email: str | NotGiven = NOT_GIVEN,
        email2: str | NotGiven = NOT_GIVEN,
        justification: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        ncmec_notification: Literal["send", "send-anon", "none"] | NotGiven = NOT_GIVEN,
        ncsei_subject_representation: bool | NotGiven = NOT_GIVEN,
        ports_protocols: str | NotGiven = NOT_GIVEN,
        source_ips: str | NotGiven = NOT_GIVEN,
        tele: str | NotGiven = NOT_GIVEN,
        title: str | NotGiven = NOT_GIVEN,
        trademark_number: str | NotGiven = NOT_GIVEN,
        trademark_office: str | NotGiven = NOT_GIVEN,
        trademark_symbol: str | NotGiven = NOT_GIVEN,
        urls: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> str:
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not report_type:
            raise ValueError(f"Expected a non-empty value for `report_type` but received {report_type!r}")
        return self._post(
            f"/accounts/{account_id}/abuse-reports/{report_type}",
            body=maybe_transform(
                {
                    "address1": address1,
                    "agent_name": agent_name,
                    "agree": agree,
                    "city": city,
                    "country": country,
                    "host_notification": host_notification,
                    "original_work": original_work,
                    "owner_notification": owner_notification,
                    "signature": signature,
                    "state": state,
                    "act": act,
                    "comments": comments,
                    "company": company,
                    "destination_ips": destination_ips,
                    "email": email,
                    "email2": email2,
                    "justification": justification,
                    "name": name,
                    "ncmec_notification": ncmec_notification,
                    "ncsei_subject_representation": ncsei_subject_representation,
                    "ports_protocols": ports_protocols,
                    "source_ips": source_ips,
                    "tele": tele,
                    "title": title,
                    "trademark_number": trademark_number,
                    "trademark_office": trademark_office,
                    "trademark_symbol": trademark_symbol,
                    "urls": urls,
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
        report_type: Literal[
            "abuse_dmca",
            "abuse_trademark",
            "abuse_general",
            "abuse_phishing",
            "abuse_children",
            "abuse_threat",
            "abuse_registrar_whois",
            "abuse_ncsei",
        ],
        *,
        account_id: str,
        address1: str,
        agent_name: str,
        agree: Literal[0, 1],
        city: str,
        country: str,
        host_notification: Literal["send", "send-anon", "none"],
        original_work: str,
        owner_notification: Literal["send", "send-anon", "none"],
        signature: str,
        state: str,
        act: Literal[
            "abuse_dmca",
            "abuse_trademark",
            "abuse_general",
            "abuse_phishing",
            "abuse_children",
            "abuse_threat",
            "abuse_registrar_whois",
            "abuse_ncsei",
        ]
        | NotGiven = NOT_GIVEN,
        comments: str | NotGiven = NOT_GIVEN,
        company: str | NotGiven = NOT_GIVEN,
        destination_ips: str | NotGiven = NOT_GIVEN,
        email: str | NotGiven = NOT_GIVEN,
        email2: str | NotGiven = NOT_GIVEN,
        justification: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        ncmec_notification: Literal["send", "send-anon", "none"] | NotGiven = NOT_GIVEN,
        ncsei_subject_representation: bool | NotGiven = NOT_GIVEN,
        ports_protocols: str | NotGiven = NOT_GIVEN,
        source_ips: str | NotGiven = NOT_GIVEN,
        tele: str | NotGiven = NOT_GIVEN,
        title: str | NotGiven = NOT_GIVEN,
        trademark_number: str | NotGiven = NOT_GIVEN,
        trademark_office: str | NotGiven = NOT_GIVEN,
        trademark_symbol: str | NotGiven = NOT_GIVEN,
        urls: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> str:
        """
        Submit the Abuse Report of a particular type

        Args:
          report_type: The abuse report type

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

          host_notification: Notification type based on the abuse type. NOTE: Copyright (DMCA) and Trademark
              reports cannot be anonymous.

          original_work: Text not exceeding 255 characters. This field may be released by Cloudflare to
              third parties such as the Lumen Database (https://lumendatabase.org/).

          owner_notification: Notification type based on the abuse type. NOTE: Copyright (DMCA) and Trademark
              reports cannot be anonymous.

          signature: Required for DMCA reports, should be same as Name. An affirmation that all
              information in the report is true and accurate while agreeing to the policies of
              Cloudflare's abuse reports

          state: Text not exceeding 255 characters. This field may be released by Cloudflare to
              third parties such as the Lumen Database (https://lumendatabase.org/).

          act: The abuse report type

          comments: Any additional comments about the infringement not exceeding 2000 characters

          company: Text not exceeding 100 characters. This field may be released by Cloudflare to
              third parties such as the Lumen Database (https://lumendatabase.org/).

          destination_ips: A list of IP addresses separated by ‘ ’ (new line character). The list of
              destination IPs should not exceed 30 IP addresses. Each one of the IP addresses
              ought to be unique

          email: A valid email of the abuse reporter. This field may be released by Cloudflare to
              third parties such as the Lumen Database (https://lumendatabase.org/).

          email2: Should match the value provided in `email`

          justification: A detailed description of the infringement, including any necessary access
              details and the exact steps needed to view the content, not exceeding 5000
              characters

          name: Text not exceeding 255 characters. This field may be released by Cloudflare to
              third parties such as the Lumen Database (https://lumendatabase.org/).

          ncmec_notification: Notification type based on the abuse type. NOTE: Copyright (DMCA) and Trademark
              reports cannot be anonymous.

          ncsei_subject_representation: If the submitter is the target of NCSEI in the URLs of the abuse report.

          ports_protocols: A comma separated list of ports and protocols e.g. 80/TCP, 22/UDP. The total
              size of the field should not exceed 2000 characters. Each individual
              port/protocol should not exceed 100 characters. The list should not have more
              than 30 unique ports and protocols.

          source_ips: A list of IP addresses separated by ‘ ’ (new line character). The list of source
              IPs should not exceed 30 IP addresses. Each one of the IP addresses ought to be
              unique

          tele: Text not exceeding 20 characters. This field may be released by Cloudflare to
              third parties such as the Lumen Database (https://lumendatabase.org/).

          title: Text not exceeding 255 characters

          trademark_number: Text not exceeding 1000 characters

          trademark_office: Text not exceeding 1000 characters

          trademark_symbol: Text not exceeding 1000 characters

          urls: A list of valid URLs separated by ‘ ’ (new line character). The list of the URLs
              should not exceed 250 URLs. All URLs should have the same hostname. Each URL
              should be unique. This field may be released by Cloudflare to third parties such
              as the Lumen Database (https://lumendatabase.org/).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        report_type: Literal[
            "abuse_dmca",
            "abuse_trademark",
            "abuse_general",
            "abuse_phishing",
            "abuse_children",
            "abuse_threat",
            "abuse_registrar_whois",
            "abuse_ncsei",
        ],
        *,
        account_id: str,
        host_notification: Literal["send", "send-anon", "none"],
        justification: str,
        owner_notification: Literal["send", "send-anon", "none"],
        trademark_number: str,
        trademark_office: str,
        trademark_symbol: str,
        act: Literal[
            "abuse_dmca",
            "abuse_trademark",
            "abuse_general",
            "abuse_phishing",
            "abuse_children",
            "abuse_threat",
            "abuse_registrar_whois",
            "abuse_ncsei",
        ]
        | NotGiven = NOT_GIVEN,
        address1: str | NotGiven = NOT_GIVEN,
        agent_name: str | NotGiven = NOT_GIVEN,
        agree: Literal[0, 1] | NotGiven = NOT_GIVEN,
        city: str | NotGiven = NOT_GIVEN,
        comments: str | NotGiven = NOT_GIVEN,
        company: str | NotGiven = NOT_GIVEN,
        country: str | NotGiven = NOT_GIVEN,
        destination_ips: str | NotGiven = NOT_GIVEN,
        email: str | NotGiven = NOT_GIVEN,
        email2: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        ncmec_notification: Literal["send", "send-anon", "none"] | NotGiven = NOT_GIVEN,
        ncsei_subject_representation: bool | NotGiven = NOT_GIVEN,
        original_work: str | NotGiven = NOT_GIVEN,
        ports_protocols: str | NotGiven = NOT_GIVEN,
        signature: str | NotGiven = NOT_GIVEN,
        source_ips: str | NotGiven = NOT_GIVEN,
        state: str | NotGiven = NOT_GIVEN,
        tele: str | NotGiven = NOT_GIVEN,
        title: str | NotGiven = NOT_GIVEN,
        urls: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> str:
        """
        Submit the Abuse Report of a particular type

        Args:
          report_type: The abuse report type

          host_notification: Notification type based on the abuse type. NOTE: Copyright (DMCA) and Trademark
              reports cannot be anonymous.

          justification: A detailed description of the infringement, including any necessary access
              details and the exact steps needed to view the content, not exceeding 5000
              characters

          owner_notification: Notification type based on the abuse type. NOTE: Copyright (DMCA) and Trademark
              reports cannot be anonymous.

          trademark_number: Text not exceeding 1000 characters

          trademark_office: Text not exceeding 1000 characters

          trademark_symbol: Text not exceeding 1000 characters

          act: The abuse report type

          address1: Text not exceeding 100 characters. This field may be released by Cloudflare to
              third parties such as the Lumen Database (https://lumendatabase.org/).

          agent_name: The name of the copyright holder. Text not exceeding 60 characters. This field
              may be released by Cloudflare to third parties such as the Lumen Database
              (https://lumendatabase.org/).

          agree: Can be `0` for false or `1` for true. Must be value: 1 for DMCA reports

          city: Text not exceeding 255 characters. This field may be released by Cloudflare to
              third parties such as the Lumen Database (https://lumendatabase.org/).

          comments: Any additional comments about the infringement not exceeding 2000 characters

          company: Text not exceeding 100 characters. This field may be released by Cloudflare to
              third parties such as the Lumen Database (https://lumendatabase.org/).

          country: Text not exceeding 255 characters. This field may be released by Cloudflare to
              third parties such as the Lumen Database (https://lumendatabase.org/).

          destination_ips: A list of IP addresses separated by ‘ ’ (new line character). The list of
              destination IPs should not exceed 30 IP addresses. Each one of the IP addresses
              ought to be unique

          email: A valid email of the abuse reporter. This field may be released by Cloudflare to
              third parties such as the Lumen Database (https://lumendatabase.org/).

          email2: Should match the value provided in `email`

          name: Text not exceeding 255 characters. This field may be released by Cloudflare to
              third parties such as the Lumen Database (https://lumendatabase.org/).

          ncmec_notification: Notification type based on the abuse type. NOTE: Copyright (DMCA) and Trademark
              reports cannot be anonymous.

          ncsei_subject_representation: If the submitter is the target of NCSEI in the URLs of the abuse report.

          original_work: Text not exceeding 255 characters. This field may be released by Cloudflare to
              third parties such as the Lumen Database (https://lumendatabase.org/).

          ports_protocols: A comma separated list of ports and protocols e.g. 80/TCP, 22/UDP. The total
              size of the field should not exceed 2000 characters. Each individual
              port/protocol should not exceed 100 characters. The list should not have more
              than 30 unique ports and protocols.

          signature: Required for DMCA reports, should be same as Name. An affirmation that all
              information in the report is true and accurate while agreeing to the policies of
              Cloudflare's abuse reports

          source_ips: A list of IP addresses separated by ‘ ’ (new line character). The list of source
              IPs should not exceed 30 IP addresses. Each one of the IP addresses ought to be
              unique

          state: Text not exceeding 255 characters. This field may be released by Cloudflare to
              third parties such as the Lumen Database (https://lumendatabase.org/).

          tele: Text not exceeding 20 characters. This field may be released by Cloudflare to
              third parties such as the Lumen Database (https://lumendatabase.org/).

          title: Text not exceeding 255 characters

          urls: A list of valid URLs separated by ‘ ’ (new line character). The list of the URLs
              should not exceed 250 URLs. All URLs should have the same hostname. Each URL
              should be unique. This field may be released by Cloudflare to third parties such
              as the Lumen Database (https://lumendatabase.org/).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        report_type: Literal[
            "abuse_dmca",
            "abuse_trademark",
            "abuse_general",
            "abuse_phishing",
            "abuse_children",
            "abuse_threat",
            "abuse_registrar_whois",
            "abuse_ncsei",
        ],
        *,
        account_id: str,
        host_notification: Literal["send", "send-anon", "none"],
        justification: str,
        owner_notification: Literal["send", "send-anon", "none"],
        act: Literal[
            "abuse_dmca",
            "abuse_trademark",
            "abuse_general",
            "abuse_phishing",
            "abuse_children",
            "abuse_threat",
            "abuse_registrar_whois",
            "abuse_ncsei",
        ]
        | NotGiven = NOT_GIVEN,
        address1: str | NotGiven = NOT_GIVEN,
        agent_name: str | NotGiven = NOT_GIVEN,
        agree: Literal[0, 1] | NotGiven = NOT_GIVEN,
        city: str | NotGiven = NOT_GIVEN,
        comments: str | NotGiven = NOT_GIVEN,
        company: str | NotGiven = NOT_GIVEN,
        country: str | NotGiven = NOT_GIVEN,
        destination_ips: str | NotGiven = NOT_GIVEN,
        email: str | NotGiven = NOT_GIVEN,
        email2: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        ncmec_notification: Literal["send", "send-anon", "none"] | NotGiven = NOT_GIVEN,
        ncsei_subject_representation: bool | NotGiven = NOT_GIVEN,
        original_work: str | NotGiven = NOT_GIVEN,
        ports_protocols: str | NotGiven = NOT_GIVEN,
        signature: str | NotGiven = NOT_GIVEN,
        source_ips: str | NotGiven = NOT_GIVEN,
        state: str | NotGiven = NOT_GIVEN,
        tele: str | NotGiven = NOT_GIVEN,
        title: str | NotGiven = NOT_GIVEN,
        trademark_number: str | NotGiven = NOT_GIVEN,
        trademark_office: str | NotGiven = NOT_GIVEN,
        trademark_symbol: str | NotGiven = NOT_GIVEN,
        urls: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> str:
        """
        Submit the Abuse Report of a particular type

        Args:
          report_type: The abuse report type

          host_notification: Notification type based on the abuse type. NOTE: Copyright (DMCA) and Trademark
              reports cannot be anonymous.

          justification: A detailed description of the infringement, including any necessary access
              details and the exact steps needed to view the content, not exceeding 5000
              characters

          owner_notification: Notification type based on the abuse type. NOTE: Copyright (DMCA) and Trademark
              reports cannot be anonymous.

          act: The abuse report type

          address1: Text not exceeding 100 characters. This field may be released by Cloudflare to
              third parties such as the Lumen Database (https://lumendatabase.org/).

          agent_name: The name of the copyright holder. Text not exceeding 60 characters. This field
              may be released by Cloudflare to third parties such as the Lumen Database
              (https://lumendatabase.org/).

          agree: Can be `0` for false or `1` for true. Must be value: 1 for DMCA reports

          city: Text not exceeding 255 characters. This field may be released by Cloudflare to
              third parties such as the Lumen Database (https://lumendatabase.org/).

          comments: Any additional comments about the infringement not exceeding 2000 characters

          company: Text not exceeding 100 characters. This field may be released by Cloudflare to
              third parties such as the Lumen Database (https://lumendatabase.org/).

          country: Text not exceeding 255 characters. This field may be released by Cloudflare to
              third parties such as the Lumen Database (https://lumendatabase.org/).

          destination_ips: A list of IP addresses separated by ‘ ’ (new line character). The list of
              destination IPs should not exceed 30 IP addresses. Each one of the IP addresses
              ought to be unique

          email: A valid email of the abuse reporter. This field may be released by Cloudflare to
              third parties such as the Lumen Database (https://lumendatabase.org/).

          email2: Should match the value provided in `email`

          name: Text not exceeding 255 characters. This field may be released by Cloudflare to
              third parties such as the Lumen Database (https://lumendatabase.org/).

          ncmec_notification: Notification type based on the abuse type. NOTE: Copyright (DMCA) and Trademark
              reports cannot be anonymous.

          ncsei_subject_representation: If the submitter is the target of NCSEI in the URLs of the abuse report.

          original_work: Text not exceeding 255 characters. This field may be released by Cloudflare to
              third parties such as the Lumen Database (https://lumendatabase.org/).

          ports_protocols: A comma separated list of ports and protocols e.g. 80/TCP, 22/UDP. The total
              size of the field should not exceed 2000 characters. Each individual
              port/protocol should not exceed 100 characters. The list should not have more
              than 30 unique ports and protocols.

          signature: Required for DMCA reports, should be same as Name. An affirmation that all
              information in the report is true and accurate while agreeing to the policies of
              Cloudflare's abuse reports

          source_ips: A list of IP addresses separated by ‘ ’ (new line character). The list of source
              IPs should not exceed 30 IP addresses. Each one of the IP addresses ought to be
              unique

          state: Text not exceeding 255 characters. This field may be released by Cloudflare to
              third parties such as the Lumen Database (https://lumendatabase.org/).

          tele: Text not exceeding 20 characters. This field may be released by Cloudflare to
              third parties such as the Lumen Database (https://lumendatabase.org/).

          title: Text not exceeding 255 characters

          trademark_number: Text not exceeding 1000 characters

          trademark_office: Text not exceeding 1000 characters

          trademark_symbol: Text not exceeding 1000 characters

          urls: A list of valid URLs separated by ‘ ’ (new line character). The list of the URLs
              should not exceed 250 URLs. All URLs should have the same hostname. Each URL
              should be unique. This field may be released by Cloudflare to third parties such
              as the Lumen Database (https://lumendatabase.org/).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        report_type: Literal[
            "abuse_dmca",
            "abuse_trademark",
            "abuse_general",
            "abuse_phishing",
            "abuse_children",
            "abuse_threat",
            "abuse_registrar_whois",
            "abuse_ncsei",
        ],
        *,
        account_id: str,
        host_notification: Literal["send", "send-anon", "none"],
        justification: str,
        owner_notification: Literal["send", "send-anon", "none"],
        act: Literal[
            "abuse_dmca",
            "abuse_trademark",
            "abuse_general",
            "abuse_phishing",
            "abuse_children",
            "abuse_threat",
            "abuse_registrar_whois",
            "abuse_ncsei",
        ]
        | NotGiven = NOT_GIVEN,
        address1: str | NotGiven = NOT_GIVEN,
        agent_name: str | NotGiven = NOT_GIVEN,
        agree: Literal[0, 1] | NotGiven = NOT_GIVEN,
        city: str | NotGiven = NOT_GIVEN,
        comments: str | NotGiven = NOT_GIVEN,
        company: str | NotGiven = NOT_GIVEN,
        country: str | NotGiven = NOT_GIVEN,
        destination_ips: str | NotGiven = NOT_GIVEN,
        email: str | NotGiven = NOT_GIVEN,
        email2: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        ncmec_notification: Literal["send", "send-anon", "none"] | NotGiven = NOT_GIVEN,
        ncsei_subject_representation: bool | NotGiven = NOT_GIVEN,
        original_work: str | NotGiven = NOT_GIVEN,
        ports_protocols: str | NotGiven = NOT_GIVEN,
        signature: str | NotGiven = NOT_GIVEN,
        source_ips: str | NotGiven = NOT_GIVEN,
        state: str | NotGiven = NOT_GIVEN,
        tele: str | NotGiven = NOT_GIVEN,
        title: str | NotGiven = NOT_GIVEN,
        trademark_number: str | NotGiven = NOT_GIVEN,
        trademark_office: str | NotGiven = NOT_GIVEN,
        trademark_symbol: str | NotGiven = NOT_GIVEN,
        urls: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> str:
        """
        Submit the Abuse Report of a particular type

        Args:
          report_type: The abuse report type

          host_notification: Notification type based on the abuse type. NOTE: Copyright (DMCA) and Trademark
              reports cannot be anonymous.

          justification: A detailed description of the infringement, including any necessary access
              details and the exact steps needed to view the content, not exceeding 5000
              characters

          owner_notification: Notification type based on the abuse type. NOTE: Copyright (DMCA) and Trademark
              reports cannot be anonymous.

          act: The abuse report type

          address1: Text not exceeding 100 characters. This field may be released by Cloudflare to
              third parties such as the Lumen Database (https://lumendatabase.org/).

          agent_name: The name of the copyright holder. Text not exceeding 60 characters. This field
              may be released by Cloudflare to third parties such as the Lumen Database
              (https://lumendatabase.org/).

          agree: Can be `0` for false or `1` for true. Must be value: 1 for DMCA reports

          city: Text not exceeding 255 characters. This field may be released by Cloudflare to
              third parties such as the Lumen Database (https://lumendatabase.org/).

          comments: Any additional comments about the infringement not exceeding 2000 characters

          company: Text not exceeding 100 characters. This field may be released by Cloudflare to
              third parties such as the Lumen Database (https://lumendatabase.org/).

          country: Text not exceeding 255 characters. This field may be released by Cloudflare to
              third parties such as the Lumen Database (https://lumendatabase.org/).

          destination_ips: A list of IP addresses separated by ‘ ’ (new line character). The list of
              destination IPs should not exceed 30 IP addresses. Each one of the IP addresses
              ought to be unique

          email: A valid email of the abuse reporter. This field may be released by Cloudflare to
              third parties such as the Lumen Database (https://lumendatabase.org/).

          email2: Should match the value provided in `email`

          name: Text not exceeding 255 characters. This field may be released by Cloudflare to
              third parties such as the Lumen Database (https://lumendatabase.org/).

          ncmec_notification: Notification type based on the abuse type. NOTE: Copyright (DMCA) and Trademark
              reports cannot be anonymous.

          ncsei_subject_representation: If the submitter is the target of NCSEI in the URLs of the abuse report.

          original_work: Text not exceeding 255 characters. This field may be released by Cloudflare to
              third parties such as the Lumen Database (https://lumendatabase.org/).

          ports_protocols: A comma separated list of ports and protocols e.g. 80/TCP, 22/UDP. The total
              size of the field should not exceed 2000 characters. Each individual
              port/protocol should not exceed 100 characters. The list should not have more
              than 30 unique ports and protocols.

          signature: Required for DMCA reports, should be same as Name. An affirmation that all
              information in the report is true and accurate while agreeing to the policies of
              Cloudflare's abuse reports

          source_ips: A list of IP addresses separated by ‘ ’ (new line character). The list of source
              IPs should not exceed 30 IP addresses. Each one of the IP addresses ought to be
              unique

          state: Text not exceeding 255 characters. This field may be released by Cloudflare to
              third parties such as the Lumen Database (https://lumendatabase.org/).

          tele: Text not exceeding 20 characters. This field may be released by Cloudflare to
              third parties such as the Lumen Database (https://lumendatabase.org/).

          title: Text not exceeding 255 characters

          trademark_number: Text not exceeding 1000 characters

          trademark_office: Text not exceeding 1000 characters

          trademark_symbol: Text not exceeding 1000 characters

          urls: A list of valid URLs separated by ‘ ’ (new line character). The list of the URLs
              should not exceed 250 URLs. All URLs should have the same hostname. Each URL
              should be unique. This field may be released by Cloudflare to third parties such
              as the Lumen Database (https://lumendatabase.org/).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        report_type: Literal[
            "abuse_dmca",
            "abuse_trademark",
            "abuse_general",
            "abuse_phishing",
            "abuse_children",
            "abuse_threat",
            "abuse_registrar_whois",
            "abuse_ncsei",
        ],
        *,
        account_id: str,
        host_notification: Literal["send", "send-anon", "none"],
        justification: str,
        ncmec_notification: Literal["send", "send-anon", "none"],
        owner_notification: Literal["send", "send-anon", "none"],
        act: Literal[
            "abuse_dmca",
            "abuse_trademark",
            "abuse_general",
            "abuse_phishing",
            "abuse_children",
            "abuse_threat",
            "abuse_registrar_whois",
            "abuse_ncsei",
        ]
        | NotGiven = NOT_GIVEN,
        address1: str | NotGiven = NOT_GIVEN,
        agent_name: str | NotGiven = NOT_GIVEN,
        agree: Literal[0, 1] | NotGiven = NOT_GIVEN,
        city: str | NotGiven = NOT_GIVEN,
        comments: str | NotGiven = NOT_GIVEN,
        company: str | NotGiven = NOT_GIVEN,
        country: str | NotGiven = NOT_GIVEN,
        destination_ips: str | NotGiven = NOT_GIVEN,
        email: str | NotGiven = NOT_GIVEN,
        email2: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        ncsei_subject_representation: bool | NotGiven = NOT_GIVEN,
        original_work: str | NotGiven = NOT_GIVEN,
        ports_protocols: str | NotGiven = NOT_GIVEN,
        signature: str | NotGiven = NOT_GIVEN,
        source_ips: str | NotGiven = NOT_GIVEN,
        state: str | NotGiven = NOT_GIVEN,
        tele: str | NotGiven = NOT_GIVEN,
        title: str | NotGiven = NOT_GIVEN,
        trademark_number: str | NotGiven = NOT_GIVEN,
        trademark_office: str | NotGiven = NOT_GIVEN,
        trademark_symbol: str | NotGiven = NOT_GIVEN,
        urls: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> str:
        """
        Submit the Abuse Report of a particular type

        Args:
          report_type: The abuse report type

          host_notification: Notification type based on the abuse type. NOTE: Copyright (DMCA) and Trademark
              reports cannot be anonymous.

          justification: A detailed description of the infringement, including any necessary access
              details and the exact steps needed to view the content, not exceeding 5000
              characters

          ncmec_notification: Notification type based on the abuse type. NOTE: Copyright (DMCA) and Trademark
              reports cannot be anonymous.

          owner_notification: Notification type based on the abuse type. NOTE: Copyright (DMCA) and Trademark
              reports cannot be anonymous.

          act: The abuse report type

          address1: Text not exceeding 100 characters. This field may be released by Cloudflare to
              third parties such as the Lumen Database (https://lumendatabase.org/).

          agent_name: The name of the copyright holder. Text not exceeding 60 characters. This field
              may be released by Cloudflare to third parties such as the Lumen Database
              (https://lumendatabase.org/).

          agree: Can be `0` for false or `1` for true. Must be value: 1 for DMCA reports

          city: Text not exceeding 255 characters. This field may be released by Cloudflare to
              third parties such as the Lumen Database (https://lumendatabase.org/).

          comments: Any additional comments about the infringement not exceeding 2000 characters

          company: Text not exceeding 100 characters. This field may be released by Cloudflare to
              third parties such as the Lumen Database (https://lumendatabase.org/).

          country: Text not exceeding 255 characters. This field may be released by Cloudflare to
              third parties such as the Lumen Database (https://lumendatabase.org/).

          destination_ips: A list of IP addresses separated by ‘ ’ (new line character). The list of
              destination IPs should not exceed 30 IP addresses. Each one of the IP addresses
              ought to be unique

          email: A valid email of the abuse reporter. This field may be released by Cloudflare to
              third parties such as the Lumen Database (https://lumendatabase.org/).

          email2: Should match the value provided in `email`

          name: Text not exceeding 255 characters. This field may be released by Cloudflare to
              third parties such as the Lumen Database (https://lumendatabase.org/).

          ncsei_subject_representation: If the submitter is the target of NCSEI in the URLs of the abuse report.

          original_work: Text not exceeding 255 characters. This field may be released by Cloudflare to
              third parties such as the Lumen Database (https://lumendatabase.org/).

          ports_protocols: A comma separated list of ports and protocols e.g. 80/TCP, 22/UDP. The total
              size of the field should not exceed 2000 characters. Each individual
              port/protocol should not exceed 100 characters. The list should not have more
              than 30 unique ports and protocols.

          signature: Required for DMCA reports, should be same as Name. An affirmation that all
              information in the report is true and accurate while agreeing to the policies of
              Cloudflare's abuse reports

          source_ips: A list of IP addresses separated by ‘ ’ (new line character). The list of source
              IPs should not exceed 30 IP addresses. Each one of the IP addresses ought to be
              unique

          state: Text not exceeding 255 characters. This field may be released by Cloudflare to
              third parties such as the Lumen Database (https://lumendatabase.org/).

          tele: Text not exceeding 20 characters. This field may be released by Cloudflare to
              third parties such as the Lumen Database (https://lumendatabase.org/).

          title: Text not exceeding 255 characters

          trademark_number: Text not exceeding 1000 characters

          trademark_office: Text not exceeding 1000 characters

          trademark_symbol: Text not exceeding 1000 characters

          urls: A list of valid URLs separated by ‘ ’ (new line character). The list of the URLs
              should not exceed 250 URLs. All URLs should have the same hostname. Each URL
              should be unique. This field may be released by Cloudflare to third parties such
              as the Lumen Database (https://lumendatabase.org/).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        report_type: Literal[
            "abuse_dmca",
            "abuse_trademark",
            "abuse_general",
            "abuse_phishing",
            "abuse_children",
            "abuse_threat",
            "abuse_registrar_whois",
            "abuse_ncsei",
        ],
        *,
        account_id: str,
        host_notification: Literal["send", "send-anon", "none"],
        justification: str,
        owner_notification: Literal["send", "send-anon", "none"],
        act: Literal[
            "abuse_dmca",
            "abuse_trademark",
            "abuse_general",
            "abuse_phishing",
            "abuse_children",
            "abuse_threat",
            "abuse_registrar_whois",
            "abuse_ncsei",
        ]
        | NotGiven = NOT_GIVEN,
        address1: str | NotGiven = NOT_GIVEN,
        agent_name: str | NotGiven = NOT_GIVEN,
        agree: Literal[0, 1] | NotGiven = NOT_GIVEN,
        city: str | NotGiven = NOT_GIVEN,
        comments: str | NotGiven = NOT_GIVEN,
        company: str | NotGiven = NOT_GIVEN,
        country: str | NotGiven = NOT_GIVEN,
        destination_ips: str | NotGiven = NOT_GIVEN,
        email: str | NotGiven = NOT_GIVEN,
        email2: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        ncmec_notification: Literal["send", "send-anon", "none"] | NotGiven = NOT_GIVEN,
        ncsei_subject_representation: bool | NotGiven = NOT_GIVEN,
        original_work: str | NotGiven = NOT_GIVEN,
        ports_protocols: str | NotGiven = NOT_GIVEN,
        signature: str | NotGiven = NOT_GIVEN,
        source_ips: str | NotGiven = NOT_GIVEN,
        state: str | NotGiven = NOT_GIVEN,
        tele: str | NotGiven = NOT_GIVEN,
        title: str | NotGiven = NOT_GIVEN,
        trademark_number: str | NotGiven = NOT_GIVEN,
        trademark_office: str | NotGiven = NOT_GIVEN,
        trademark_symbol: str | NotGiven = NOT_GIVEN,
        urls: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> str:
        """
        Submit the Abuse Report of a particular type

        Args:
          report_type: The abuse report type

          host_notification: Notification type based on the abuse type. NOTE: Copyright (DMCA) and Trademark
              reports cannot be anonymous.

          justification: A detailed description of the infringement, including any necessary access
              details and the exact steps needed to view the content, not exceeding 5000
              characters

          owner_notification: Notification type based on the abuse type. NOTE: Copyright (DMCA) and Trademark
              reports cannot be anonymous.

          act: The abuse report type

          address1: Text not exceeding 100 characters. This field may be released by Cloudflare to
              third parties such as the Lumen Database (https://lumendatabase.org/).

          agent_name: The name of the copyright holder. Text not exceeding 60 characters. This field
              may be released by Cloudflare to third parties such as the Lumen Database
              (https://lumendatabase.org/).

          agree: Can be `0` for false or `1` for true. Must be value: 1 for DMCA reports

          city: Text not exceeding 255 characters. This field may be released by Cloudflare to
              third parties such as the Lumen Database (https://lumendatabase.org/).

          comments: Any additional comments about the infringement not exceeding 2000 characters

          company: Text not exceeding 100 characters. This field may be released by Cloudflare to
              third parties such as the Lumen Database (https://lumendatabase.org/).

          country: Text not exceeding 255 characters. This field may be released by Cloudflare to
              third parties such as the Lumen Database (https://lumendatabase.org/).

          destination_ips: A list of IP addresses separated by ‘ ’ (new line character). The list of
              destination IPs should not exceed 30 IP addresses. Each one of the IP addresses
              ought to be unique

          email: A valid email of the abuse reporter. This field may be released by Cloudflare to
              third parties such as the Lumen Database (https://lumendatabase.org/).

          email2: Should match the value provided in `email`

          name: Text not exceeding 255 characters. This field may be released by Cloudflare to
              third parties such as the Lumen Database (https://lumendatabase.org/).

          ncmec_notification: Notification type based on the abuse type. NOTE: Copyright (DMCA) and Trademark
              reports cannot be anonymous.

          ncsei_subject_representation: If the submitter is the target of NCSEI in the URLs of the abuse report.

          original_work: Text not exceeding 255 characters. This field may be released by Cloudflare to
              third parties such as the Lumen Database (https://lumendatabase.org/).

          ports_protocols: A comma separated list of ports and protocols e.g. 80/TCP, 22/UDP. The total
              size of the field should not exceed 2000 characters. Each individual
              port/protocol should not exceed 100 characters. The list should not have more
              than 30 unique ports and protocols.

          signature: Required for DMCA reports, should be same as Name. An affirmation that all
              information in the report is true and accurate while agreeing to the policies of
              Cloudflare's abuse reports

          source_ips: A list of IP addresses separated by ‘ ’ (new line character). The list of source
              IPs should not exceed 30 IP addresses. Each one of the IP addresses ought to be
              unique

          state: Text not exceeding 255 characters. This field may be released by Cloudflare to
              third parties such as the Lumen Database (https://lumendatabase.org/).

          tele: Text not exceeding 20 characters. This field may be released by Cloudflare to
              third parties such as the Lumen Database (https://lumendatabase.org/).

          title: Text not exceeding 255 characters

          trademark_number: Text not exceeding 1000 characters

          trademark_office: Text not exceeding 1000 characters

          trademark_symbol: Text not exceeding 1000 characters

          urls: A list of valid URLs separated by ‘ ’ (new line character). The list of the URLs
              should not exceed 250 URLs. All URLs should have the same hostname. Each URL
              should be unique. This field may be released by Cloudflare to third parties such
              as the Lumen Database (https://lumendatabase.org/).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        report_type: Literal[
            "abuse_dmca",
            "abuse_trademark",
            "abuse_general",
            "abuse_phishing",
            "abuse_children",
            "abuse_threat",
            "abuse_registrar_whois",
            "abuse_ncsei",
        ],
        *,
        account_id: str,
        owner_notification: Literal["send", "send-anon", "none"],
        act: Literal[
            "abuse_dmca",
            "abuse_trademark",
            "abuse_general",
            "abuse_phishing",
            "abuse_children",
            "abuse_threat",
            "abuse_registrar_whois",
            "abuse_ncsei",
        ]
        | NotGiven = NOT_GIVEN,
        address1: str | NotGiven = NOT_GIVEN,
        agent_name: str | NotGiven = NOT_GIVEN,
        agree: Literal[0, 1] | NotGiven = NOT_GIVEN,
        city: str | NotGiven = NOT_GIVEN,
        comments: str | NotGiven = NOT_GIVEN,
        company: str | NotGiven = NOT_GIVEN,
        country: str | NotGiven = NOT_GIVEN,
        destination_ips: str | NotGiven = NOT_GIVEN,
        email: str | NotGiven = NOT_GIVEN,
        email2: str | NotGiven = NOT_GIVEN,
        host_notification: Literal["send", "send-anon", "none"] | NotGiven = NOT_GIVEN,
        justification: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        ncmec_notification: Literal["send", "send-anon", "none"] | NotGiven = NOT_GIVEN,
        ncsei_subject_representation: bool | NotGiven = NOT_GIVEN,
        original_work: str | NotGiven = NOT_GIVEN,
        ports_protocols: str | NotGiven = NOT_GIVEN,
        signature: str | NotGiven = NOT_GIVEN,
        source_ips: str | NotGiven = NOT_GIVEN,
        state: str | NotGiven = NOT_GIVEN,
        tele: str | NotGiven = NOT_GIVEN,
        title: str | NotGiven = NOT_GIVEN,
        trademark_number: str | NotGiven = NOT_GIVEN,
        trademark_office: str | NotGiven = NOT_GIVEN,
        trademark_symbol: str | NotGiven = NOT_GIVEN,
        urls: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> str:
        """
        Submit the Abuse Report of a particular type

        Args:
          report_type: The abuse report type

          owner_notification: Notification type based on the abuse type. NOTE: Copyright (DMCA) and Trademark
              reports cannot be anonymous.

          act: The abuse report type

          address1: Text not exceeding 100 characters. This field may be released by Cloudflare to
              third parties such as the Lumen Database (https://lumendatabase.org/).

          agent_name: The name of the copyright holder. Text not exceeding 60 characters. This field
              may be released by Cloudflare to third parties such as the Lumen Database
              (https://lumendatabase.org/).

          agree: Can be `0` for false or `1` for true. Must be value: 1 for DMCA reports

          city: Text not exceeding 255 characters. This field may be released by Cloudflare to
              third parties such as the Lumen Database (https://lumendatabase.org/).

          comments: Any additional comments about the infringement not exceeding 2000 characters

          company: Text not exceeding 100 characters. This field may be released by Cloudflare to
              third parties such as the Lumen Database (https://lumendatabase.org/).

          country: Text not exceeding 255 characters. This field may be released by Cloudflare to
              third parties such as the Lumen Database (https://lumendatabase.org/).

          destination_ips: A list of IP addresses separated by ‘ ’ (new line character). The list of
              destination IPs should not exceed 30 IP addresses. Each one of the IP addresses
              ought to be unique

          email: A valid email of the abuse reporter. This field may be released by Cloudflare to
              third parties such as the Lumen Database (https://lumendatabase.org/).

          email2: Should match the value provided in `email`

          host_notification: Notification type based on the abuse type. NOTE: Copyright (DMCA) and Trademark
              reports cannot be anonymous.

          justification: A detailed description of the infringement, including any necessary access
              details and the exact steps needed to view the content, not exceeding 5000
              characters

          name: Text not exceeding 255 characters. This field may be released by Cloudflare to
              third parties such as the Lumen Database (https://lumendatabase.org/).

          ncmec_notification: Notification type based on the abuse type. NOTE: Copyright (DMCA) and Trademark
              reports cannot be anonymous.

          ncsei_subject_representation: If the submitter is the target of NCSEI in the URLs of the abuse report.

          original_work: Text not exceeding 255 characters. This field may be released by Cloudflare to
              third parties such as the Lumen Database (https://lumendatabase.org/).

          ports_protocols: A comma separated list of ports and protocols e.g. 80/TCP, 22/UDP. The total
              size of the field should not exceed 2000 characters. Each individual
              port/protocol should not exceed 100 characters. The list should not have more
              than 30 unique ports and protocols.

          signature: Required for DMCA reports, should be same as Name. An affirmation that all
              information in the report is true and accurate while agreeing to the policies of
              Cloudflare's abuse reports

          source_ips: A list of IP addresses separated by ‘ ’ (new line character). The list of source
              IPs should not exceed 30 IP addresses. Each one of the IP addresses ought to be
              unique

          state: Text not exceeding 255 characters. This field may be released by Cloudflare to
              third parties such as the Lumen Database (https://lumendatabase.org/).

          tele: Text not exceeding 20 characters. This field may be released by Cloudflare to
              third parties such as the Lumen Database (https://lumendatabase.org/).

          title: Text not exceeding 255 characters

          trademark_number: Text not exceeding 1000 characters

          trademark_office: Text not exceeding 1000 characters

          trademark_symbol: Text not exceeding 1000 characters

          urls: A list of valid URLs separated by ‘ ’ (new line character). The list of the URLs
              should not exceed 250 URLs. All URLs should have the same hostname. Each URL
              should be unique. This field may be released by Cloudflare to third parties such
              as the Lumen Database (https://lumendatabase.org/).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        report_type: Literal[
            "abuse_dmca",
            "abuse_trademark",
            "abuse_general",
            "abuse_phishing",
            "abuse_children",
            "abuse_threat",
            "abuse_registrar_whois",
            "abuse_ncsei",
        ],
        *,
        account_id: str,
        host_notification: Literal["send", "send-anon", "none"],
        ncsei_subject_representation: bool,
        owner_notification: Literal["send", "send-anon", "none"],
        act: Literal[
            "abuse_dmca",
            "abuse_trademark",
            "abuse_general",
            "abuse_phishing",
            "abuse_children",
            "abuse_threat",
            "abuse_registrar_whois",
            "abuse_ncsei",
        ]
        | NotGiven = NOT_GIVEN,
        address1: str | NotGiven = NOT_GIVEN,
        agent_name: str | NotGiven = NOT_GIVEN,
        agree: Literal[0, 1] | NotGiven = NOT_GIVEN,
        city: str | NotGiven = NOT_GIVEN,
        comments: str | NotGiven = NOT_GIVEN,
        company: str | NotGiven = NOT_GIVEN,
        country: str | NotGiven = NOT_GIVEN,
        destination_ips: str | NotGiven = NOT_GIVEN,
        email: str | NotGiven = NOT_GIVEN,
        email2: str | NotGiven = NOT_GIVEN,
        justification: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        ncmec_notification: Literal["send", "send-anon", "none"] | NotGiven = NOT_GIVEN,
        original_work: str | NotGiven = NOT_GIVEN,
        ports_protocols: str | NotGiven = NOT_GIVEN,
        signature: str | NotGiven = NOT_GIVEN,
        source_ips: str | NotGiven = NOT_GIVEN,
        state: str | NotGiven = NOT_GIVEN,
        tele: str | NotGiven = NOT_GIVEN,
        title: str | NotGiven = NOT_GIVEN,
        trademark_number: str | NotGiven = NOT_GIVEN,
        trademark_office: str | NotGiven = NOT_GIVEN,
        trademark_symbol: str | NotGiven = NOT_GIVEN,
        urls: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> str:
        """
        Submit the Abuse Report of a particular type

        Args:
          report_type: The abuse report type

          host_notification: Notification type based on the abuse type. NOTE: Copyright (DMCA) and Trademark
              reports cannot be anonymous.

          ncsei_subject_representation: If the submitter is the target of NCSEI in the URLs of the abuse report.

          owner_notification: Notification type based on the abuse type. NOTE: Copyright (DMCA) and Trademark
              reports cannot be anonymous.

          act: The abuse report type

          address1: Text not exceeding 100 characters. This field may be released by Cloudflare to
              third parties such as the Lumen Database (https://lumendatabase.org/).

          agent_name: The name of the copyright holder. Text not exceeding 60 characters. This field
              may be released by Cloudflare to third parties such as the Lumen Database
              (https://lumendatabase.org/).

          agree: Can be `0` for false or `1` for true. Must be value: 1 for DMCA reports

          city: Text not exceeding 255 characters. This field may be released by Cloudflare to
              third parties such as the Lumen Database (https://lumendatabase.org/).

          comments: Any additional comments about the infringement not exceeding 2000 characters

          company: Text not exceeding 100 characters. This field may be released by Cloudflare to
              third parties such as the Lumen Database (https://lumendatabase.org/).

          country: Text not exceeding 255 characters. This field may be released by Cloudflare to
              third parties such as the Lumen Database (https://lumendatabase.org/).

          destination_ips: A list of IP addresses separated by ‘ ’ (new line character). The list of
              destination IPs should not exceed 30 IP addresses. Each one of the IP addresses
              ought to be unique

          email: A valid email of the abuse reporter. This field may be released by Cloudflare to
              third parties such as the Lumen Database (https://lumendatabase.org/).

          email2: Should match the value provided in `email`

          justification: A detailed description of the infringement, including any necessary access
              details and the exact steps needed to view the content, not exceeding 5000
              characters

          name: Text not exceeding 255 characters. This field may be released by Cloudflare to
              third parties such as the Lumen Database (https://lumendatabase.org/).

          ncmec_notification: Notification type based on the abuse type. NOTE: Copyright (DMCA) and Trademark
              reports cannot be anonymous.

          original_work: Text not exceeding 255 characters. This field may be released by Cloudflare to
              third parties such as the Lumen Database (https://lumendatabase.org/).

          ports_protocols: A comma separated list of ports and protocols e.g. 80/TCP, 22/UDP. The total
              size of the field should not exceed 2000 characters. Each individual
              port/protocol should not exceed 100 characters. The list should not have more
              than 30 unique ports and protocols.

          signature: Required for DMCA reports, should be same as Name. An affirmation that all
              information in the report is true and accurate while agreeing to the policies of
              Cloudflare's abuse reports

          source_ips: A list of IP addresses separated by ‘ ’ (new line character). The list of source
              IPs should not exceed 30 IP addresses. Each one of the IP addresses ought to be
              unique

          state: Text not exceeding 255 characters. This field may be released by Cloudflare to
              third parties such as the Lumen Database (https://lumendatabase.org/).

          tele: Text not exceeding 20 characters. This field may be released by Cloudflare to
              third parties such as the Lumen Database (https://lumendatabase.org/).

          title: Text not exceeding 255 characters

          trademark_number: Text not exceeding 1000 characters

          trademark_office: Text not exceeding 1000 characters

          trademark_symbol: Text not exceeding 1000 characters

          urls: A list of valid URLs separated by ‘ ’ (new line character). The list of the URLs
              should not exceed 250 URLs. All URLs should have the same hostname. Each URL
              should be unique. This field may be released by Cloudflare to third parties such
              as the Lumen Database (https://lumendatabase.org/).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(
        [
            "account_id",
            "address1",
            "agent_name",
            "agree",
            "city",
            "country",
            "host_notification",
            "original_work",
            "owner_notification",
            "signature",
            "state",
        ],
        [
            "account_id",
            "host_notification",
            "justification",
            "owner_notification",
            "trademark_number",
            "trademark_office",
            "trademark_symbol",
        ],
        ["account_id", "host_notification", "justification", "owner_notification"],
        ["account_id", "host_notification", "justification", "ncmec_notification", "owner_notification"],
        ["account_id", "owner_notification"],
        ["account_id", "host_notification", "ncsei_subject_representation", "owner_notification"],
    )
    async def create(
        self,
        report_type: Literal[
            "abuse_dmca",
            "abuse_trademark",
            "abuse_general",
            "abuse_phishing",
            "abuse_children",
            "abuse_threat",
            "abuse_registrar_whois",
            "abuse_ncsei",
        ],
        *,
        account_id: str,
        address1: str | NotGiven = NOT_GIVEN,
        agent_name: str | NotGiven = NOT_GIVEN,
        agree: Literal[0, 1] | NotGiven = NOT_GIVEN,
        city: str | NotGiven = NOT_GIVEN,
        country: str | NotGiven = NOT_GIVEN,
        host_notification: Literal["send", "send-anon", "none"] | NotGiven = NOT_GIVEN,
        original_work: str | NotGiven = NOT_GIVEN,
        owner_notification: Literal["send", "send-anon", "none"],
        signature: str | NotGiven = NOT_GIVEN,
        state: str | NotGiven = NOT_GIVEN,
        act: Literal[
            "abuse_dmca",
            "abuse_trademark",
            "abuse_general",
            "abuse_phishing",
            "abuse_children",
            "abuse_threat",
            "abuse_registrar_whois",
            "abuse_ncsei",
        ]
        | NotGiven = NOT_GIVEN,
        comments: str | NotGiven = NOT_GIVEN,
        company: str | NotGiven = NOT_GIVEN,
        destination_ips: str | NotGiven = NOT_GIVEN,
        email: str | NotGiven = NOT_GIVEN,
        email2: str | NotGiven = NOT_GIVEN,
        justification: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        ncmec_notification: Literal["send", "send-anon", "none"] | NotGiven = NOT_GIVEN,
        ncsei_subject_representation: bool | NotGiven = NOT_GIVEN,
        ports_protocols: str | NotGiven = NOT_GIVEN,
        source_ips: str | NotGiven = NOT_GIVEN,
        tele: str | NotGiven = NOT_GIVEN,
        title: str | NotGiven = NOT_GIVEN,
        trademark_number: str | NotGiven = NOT_GIVEN,
        trademark_office: str | NotGiven = NOT_GIVEN,
        trademark_symbol: str | NotGiven = NOT_GIVEN,
        urls: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> str:
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not report_type:
            raise ValueError(f"Expected a non-empty value for `report_type` but received {report_type!r}")
        return await self._post(
            f"/accounts/{account_id}/abuse-reports/{report_type}",
            body=await async_maybe_transform(
                {
                    "address1": address1,
                    "agent_name": agent_name,
                    "agree": agree,
                    "city": city,
                    "country": country,
                    "host_notification": host_notification,
                    "original_work": original_work,
                    "owner_notification": owner_notification,
                    "signature": signature,
                    "state": state,
                    "act": act,
                    "comments": comments,
                    "company": company,
                    "destination_ips": destination_ips,
                    "email": email,
                    "email2": email2,
                    "justification": justification,
                    "name": name,
                    "ncmec_notification": ncmec_notification,
                    "ncsei_subject_representation": ncsei_subject_representation,
                    "ports_protocols": ports_protocols,
                    "source_ips": source_ips,
                    "tele": tele,
                    "title": title,
                    "trademark_number": trademark_number,
                    "trademark_office": trademark_office,
                    "trademark_symbol": trademark_symbol,
                    "urls": urls,
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


class AbuseReportsResourceWithRawResponse:
    def __init__(self, abuse_reports: AbuseReportsResource) -> None:
        self._abuse_reports = abuse_reports

        self.create = to_raw_response_wrapper(
            abuse_reports.create,
        )


class AsyncAbuseReportsResourceWithRawResponse:
    def __init__(self, abuse_reports: AsyncAbuseReportsResource) -> None:
        self._abuse_reports = abuse_reports

        self.create = async_to_raw_response_wrapper(
            abuse_reports.create,
        )


class AbuseReportsResourceWithStreamingResponse:
    def __init__(self, abuse_reports: AbuseReportsResource) -> None:
        self._abuse_reports = abuse_reports

        self.create = to_streamed_response_wrapper(
            abuse_reports.create,
        )


class AsyncAbuseReportsResourceWithStreamingResponse:
    def __init__(self, abuse_reports: AsyncAbuseReportsResource) -> None:
        self._abuse_reports = abuse_reports

        self.create = async_to_streamed_response_wrapper(
            abuse_reports.create,
        )
