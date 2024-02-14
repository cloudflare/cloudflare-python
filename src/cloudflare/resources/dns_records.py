# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from .._compat import cached_property

from typing_extensions import Literal

from typing import List, Union, Type, Optional

from ..types import (
    DNSRecordCreateResponse,
    DNSRecordUpdateResponse,
    DNSRecordListResponse,
    DNSRecordDeleteResponse,
    DNSRecordExportResponse,
    DNSRecordGetResponse,
    DNSRecordImportResponse,
    DNSRecordScanResponse,
    dns_record_create_params,
    dns_record_update_params,
    dns_record_list_params,
)

from .._response import (
    to_raw_response_wrapper,
    async_to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_streamed_response_wrapper,
)

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from .._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from .._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from .._resource import SyncAPIResource, AsyncAPIResource
from .._base_client import (
    SyncAPIClient,
    AsyncAPIClient,
    _merge_mappings,
    AsyncPaginator,
    make_request_options,
    HttpxBinaryResponseContent,
)
from ..types import shared_params
from ..types import dns_record_create_params
from ..types import dns_record_update_params
from ..types import dns_record_list_params
from ..types import dns_record_import_params
from .._wrappers import ResultWrapper
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast

__all__ = ["DNSRecords", "AsyncDNSRecords"]


class DNSRecords(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DNSRecordsWithRawResponse:
        return DNSRecordsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DNSRecordsWithStreamingResponse:
        return DNSRecordsWithStreamingResponse(self)

    @overload
    def create(
        self,
        zone_id: str,
        *,
        content: str,
        name: str,
        type: Literal["A"],
        comment: str | NotGiven = NOT_GIVEN,
        proxied: bool | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        ttl: Union[float, Literal[1]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DNSRecordCreateResponse:
        """
        Create a new DNS record for a zone.

        Notes:

        - A/AAAA records cannot exist on the same name as CNAME records.
        - NS records cannot exist on the same name as any other record type.
        - Domain names are always represented in Punycode, even if Unicode characters
          were used when creating the record.

        Args:
          zone_id: Identifier

          content: A valid IPv4 address.

          name: DNS record name (or @ for the zone apex) in Punycode.

          type: Record type.

          comment: Comments or notes about the DNS record. This field has no effect on DNS
              responses.

          proxied: Whether the record is receiving the performance and security benefits of
              Cloudflare.

          tags: Custom tags for the DNS record. This field has no effect on DNS responses.

          ttl: Time To Live (TTL) of the DNS record in seconds. Setting to 1 means 'automatic'.
              Value must be between 60 and 86400, with the minimum reduced to 30 for
              Enterprise zones.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        zone_id: str,
        *,
        content: str,
        name: str,
        type: Literal["AAAA"],
        comment: str | NotGiven = NOT_GIVEN,
        proxied: bool | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        ttl: Union[float, Literal[1]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DNSRecordCreateResponse:
        """
        Create a new DNS record for a zone.

        Notes:

        - A/AAAA records cannot exist on the same name as CNAME records.
        - NS records cannot exist on the same name as any other record type.
        - Domain names are always represented in Punycode, even if Unicode characters
          were used when creating the record.

        Args:
          zone_id: Identifier

          content: A valid IPv6 address.

          name: DNS record name (or @ for the zone apex) in Punycode.

          type: Record type.

          comment: Comments or notes about the DNS record. This field has no effect on DNS
              responses.

          proxied: Whether the record is receiving the performance and security benefits of
              Cloudflare.

          tags: Custom tags for the DNS record. This field has no effect on DNS responses.

          ttl: Time To Live (TTL) of the DNS record in seconds. Setting to 1 means 'automatic'.
              Value must be between 60 and 86400, with the minimum reduced to 30 for
              Enterprise zones.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        zone_id: str,
        *,
        data: dns_record_create_params.DNSRecordsCaaRecordData,
        name: str,
        type: Literal["CAA"],
        comment: str | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        ttl: Union[float, Literal[1]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DNSRecordCreateResponse:
        """
        Create a new DNS record for a zone.

        Notes:

        - A/AAAA records cannot exist on the same name as CNAME records.
        - NS records cannot exist on the same name as any other record type.
        - Domain names are always represented in Punycode, even if Unicode characters
          were used when creating the record.

        Args:
          zone_id: Identifier

          data: Components of a CAA record.

          name: DNS record name (or @ for the zone apex) in Punycode.

          type: Record type.

          comment: Comments or notes about the DNS record. This field has no effect on DNS
              responses.

          tags: Custom tags for the DNS record. This field has no effect on DNS responses.

          ttl: Time To Live (TTL) of the DNS record in seconds. Setting to 1 means 'automatic'.
              Value must be between 60 and 86400, with the minimum reduced to 30 for
              Enterprise zones.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        zone_id: str,
        *,
        data: dns_record_create_params.DNSRecordsCertRecordData,
        name: str,
        type: Literal["CERT"],
        comment: str | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        ttl: Union[float, Literal[1]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DNSRecordCreateResponse:
        """
        Create a new DNS record for a zone.

        Notes:

        - A/AAAA records cannot exist on the same name as CNAME records.
        - NS records cannot exist on the same name as any other record type.
        - Domain names are always represented in Punycode, even if Unicode characters
          were used when creating the record.

        Args:
          zone_id: Identifier

          data: Components of a CERT record.

          name: DNS record name (or @ for the zone apex) in Punycode.

          type: Record type.

          comment: Comments or notes about the DNS record. This field has no effect on DNS
              responses.

          tags: Custom tags for the DNS record. This field has no effect on DNS responses.

          ttl: Time To Live (TTL) of the DNS record in seconds. Setting to 1 means 'automatic'.
              Value must be between 60 and 86400, with the minimum reduced to 30 for
              Enterprise zones.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        zone_id: str,
        *,
        content: object,
        name: str,
        type: Literal["CNAME"],
        comment: str | NotGiven = NOT_GIVEN,
        proxied: bool | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        ttl: Union[float, Literal[1]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DNSRecordCreateResponse:
        """
        Create a new DNS record for a zone.

        Notes:

        - A/AAAA records cannot exist on the same name as CNAME records.
        - NS records cannot exist on the same name as any other record type.
        - Domain names are always represented in Punycode, even if Unicode characters
          were used when creating the record.

        Args:
          zone_id: Identifier

          content: A valid hostname. Must not match the record's name.

          name: DNS record name (or @ for the zone apex) in Punycode.

          type: Record type.

          comment: Comments or notes about the DNS record. This field has no effect on DNS
              responses.

          proxied: Whether the record is receiving the performance and security benefits of
              Cloudflare.

          tags: Custom tags for the DNS record. This field has no effect on DNS responses.

          ttl: Time To Live (TTL) of the DNS record in seconds. Setting to 1 means 'automatic'.
              Value must be between 60 and 86400, with the minimum reduced to 30 for
              Enterprise zones.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        zone_id: str,
        *,
        data: dns_record_create_params.DNSRecordsDnskeyRecordData,
        name: str,
        type: Literal["DNSKEY"],
        comment: str | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        ttl: Union[float, Literal[1]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DNSRecordCreateResponse:
        """
        Create a new DNS record for a zone.

        Notes:

        - A/AAAA records cannot exist on the same name as CNAME records.
        - NS records cannot exist on the same name as any other record type.
        - Domain names are always represented in Punycode, even if Unicode characters
          were used when creating the record.

        Args:
          zone_id: Identifier

          data: Components of a DNSKEY record.

          name: DNS record name (or @ for the zone apex) in Punycode.

          type: Record type.

          comment: Comments or notes about the DNS record. This field has no effect on DNS
              responses.

          tags: Custom tags for the DNS record. This field has no effect on DNS responses.

          ttl: Time To Live (TTL) of the DNS record in seconds. Setting to 1 means 'automatic'.
              Value must be between 60 and 86400, with the minimum reduced to 30 for
              Enterprise zones.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        zone_id: str,
        *,
        data: dns_record_create_params.DNSRecordsDsRecordData,
        name: str,
        type: Literal["DS"],
        comment: str | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        ttl: Union[float, Literal[1]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DNSRecordCreateResponse:
        """
        Create a new DNS record for a zone.

        Notes:

        - A/AAAA records cannot exist on the same name as CNAME records.
        - NS records cannot exist on the same name as any other record type.
        - Domain names are always represented in Punycode, even if Unicode characters
          were used when creating the record.

        Args:
          zone_id: Identifier

          data: Components of a DS record.

          name: DNS record name (or @ for the zone apex) in Punycode.

          type: Record type.

          comment: Comments or notes about the DNS record. This field has no effect on DNS
              responses.

          tags: Custom tags for the DNS record. This field has no effect on DNS responses.

          ttl: Time To Live (TTL) of the DNS record in seconds. Setting to 1 means 'automatic'.
              Value must be between 60 and 86400, with the minimum reduced to 30 for
              Enterprise zones.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        zone_id: str,
        *,
        data: dns_record_create_params.DNSRecordsHTTPsRecordData,
        name: str,
        type: Literal["HTTPS"],
        comment: str | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        ttl: Union[float, Literal[1]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DNSRecordCreateResponse:
        """
        Create a new DNS record for a zone.

        Notes:

        - A/AAAA records cannot exist on the same name as CNAME records.
        - NS records cannot exist on the same name as any other record type.
        - Domain names are always represented in Punycode, even if Unicode characters
          were used when creating the record.

        Args:
          zone_id: Identifier

          data: Components of a HTTPS record.

          name: DNS record name (or @ for the zone apex) in Punycode.

          type: Record type.

          comment: Comments or notes about the DNS record. This field has no effect on DNS
              responses.

          tags: Custom tags for the DNS record. This field has no effect on DNS responses.

          ttl: Time To Live (TTL) of the DNS record in seconds. Setting to 1 means 'automatic'.
              Value must be between 60 and 86400, with the minimum reduced to 30 for
              Enterprise zones.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        zone_id: str,
        *,
        data: dns_record_create_params.DNSRecordsLocRecordData,
        name: str,
        type: Literal["LOC"],
        comment: str | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        ttl: Union[float, Literal[1]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DNSRecordCreateResponse:
        """
        Create a new DNS record for a zone.

        Notes:

        - A/AAAA records cannot exist on the same name as CNAME records.
        - NS records cannot exist on the same name as any other record type.
        - Domain names are always represented in Punycode, even if Unicode characters
          were used when creating the record.

        Args:
          zone_id: Identifier

          data: Components of a LOC record.

          name: DNS record name (or @ for the zone apex) in Punycode.

          type: Record type.

          comment: Comments or notes about the DNS record. This field has no effect on DNS
              responses.

          tags: Custom tags for the DNS record. This field has no effect on DNS responses.

          ttl: Time To Live (TTL) of the DNS record in seconds. Setting to 1 means 'automatic'.
              Value must be between 60 and 86400, with the minimum reduced to 30 for
              Enterprise zones.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        zone_id: str,
        *,
        content: str,
        name: str,
        priority: float,
        type: Literal["MX"],
        comment: str | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        ttl: Union[float, Literal[1]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DNSRecordCreateResponse:
        """
        Create a new DNS record for a zone.

        Notes:

        - A/AAAA records cannot exist on the same name as CNAME records.
        - NS records cannot exist on the same name as any other record type.
        - Domain names are always represented in Punycode, even if Unicode characters
          were used when creating the record.

        Args:
          zone_id: Identifier

          content: A valid mail server hostname.

          name: DNS record name (or @ for the zone apex) in Punycode.

          priority: Required for MX, SRV and URI records; unused by other record types. Records with
              lower priorities are preferred.

          type: Record type.

          comment: Comments or notes about the DNS record. This field has no effect on DNS
              responses.

          tags: Custom tags for the DNS record. This field has no effect on DNS responses.

          ttl: Time To Live (TTL) of the DNS record in seconds. Setting to 1 means 'automatic'.
              Value must be between 60 and 86400, with the minimum reduced to 30 for
              Enterprise zones.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        zone_id: str,
        *,
        data: dns_record_create_params.DNSRecordsNaptrRecordData,
        name: str,
        type: Literal["NAPTR"],
        comment: str | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        ttl: Union[float, Literal[1]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DNSRecordCreateResponse:
        """
        Create a new DNS record for a zone.

        Notes:

        - A/AAAA records cannot exist on the same name as CNAME records.
        - NS records cannot exist on the same name as any other record type.
        - Domain names are always represented in Punycode, even if Unicode characters
          were used when creating the record.

        Args:
          zone_id: Identifier

          data: Components of a NAPTR record.

          name: DNS record name (or @ for the zone apex) in Punycode.

          type: Record type.

          comment: Comments or notes about the DNS record. This field has no effect on DNS
              responses.

          tags: Custom tags for the DNS record. This field has no effect on DNS responses.

          ttl: Time To Live (TTL) of the DNS record in seconds. Setting to 1 means 'automatic'.
              Value must be between 60 and 86400, with the minimum reduced to 30 for
              Enterprise zones.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        zone_id: str,
        *,
        content: object,
        name: str,
        type: Literal["NS"],
        comment: str | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        ttl: Union[float, Literal[1]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DNSRecordCreateResponse:
        """
        Create a new DNS record for a zone.

        Notes:

        - A/AAAA records cannot exist on the same name as CNAME records.
        - NS records cannot exist on the same name as any other record type.
        - Domain names are always represented in Punycode, even if Unicode characters
          were used when creating the record.

        Args:
          zone_id: Identifier

          content: A valid name server host name.

          name: DNS record name (or @ for the zone apex) in Punycode.

          type: Record type.

          comment: Comments or notes about the DNS record. This field has no effect on DNS
              responses.

          tags: Custom tags for the DNS record. This field has no effect on DNS responses.

          ttl: Time To Live (TTL) of the DNS record in seconds. Setting to 1 means 'automatic'.
              Value must be between 60 and 86400, with the minimum reduced to 30 for
              Enterprise zones.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        zone_id: str,
        *,
        content: str,
        name: str,
        type: Literal["PTR"],
        comment: str | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        ttl: Union[float, Literal[1]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DNSRecordCreateResponse:
        """
        Create a new DNS record for a zone.

        Notes:

        - A/AAAA records cannot exist on the same name as CNAME records.
        - NS records cannot exist on the same name as any other record type.
        - Domain names are always represented in Punycode, even if Unicode characters
          were used when creating the record.

        Args:
          zone_id: Identifier

          content: Domain name pointing to the address.

          name: DNS record name (or @ for the zone apex) in Punycode.

          type: Record type.

          comment: Comments or notes about the DNS record. This field has no effect on DNS
              responses.

          tags: Custom tags for the DNS record. This field has no effect on DNS responses.

          ttl: Time To Live (TTL) of the DNS record in seconds. Setting to 1 means 'automatic'.
              Value must be between 60 and 86400, with the minimum reduced to 30 for
              Enterprise zones.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        zone_id: str,
        *,
        data: dns_record_create_params.DNSRecordsSmimeaRecordData,
        name: str,
        type: Literal["SMIMEA"],
        comment: str | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        ttl: Union[float, Literal[1]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DNSRecordCreateResponse:
        """
        Create a new DNS record for a zone.

        Notes:

        - A/AAAA records cannot exist on the same name as CNAME records.
        - NS records cannot exist on the same name as any other record type.
        - Domain names are always represented in Punycode, even if Unicode characters
          were used when creating the record.

        Args:
          zone_id: Identifier

          data: Components of a SMIMEA record.

          name: DNS record name (or @ for the zone apex) in Punycode.

          type: Record type.

          comment: Comments or notes about the DNS record. This field has no effect on DNS
              responses.

          tags: Custom tags for the DNS record. This field has no effect on DNS responses.

          ttl: Time To Live (TTL) of the DNS record in seconds. Setting to 1 means 'automatic'.
              Value must be between 60 and 86400, with the minimum reduced to 30 for
              Enterprise zones.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        zone_id: str,
        *,
        data: dns_record_create_params.DNSRecordsSrvRecordData,
        name: str,
        type: Literal["SRV"],
        comment: str | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        ttl: Union[float, Literal[1]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DNSRecordCreateResponse:
        """
        Create a new DNS record for a zone.

        Notes:

        - A/AAAA records cannot exist on the same name as CNAME records.
        - NS records cannot exist on the same name as any other record type.
        - Domain names are always represented in Punycode, even if Unicode characters
          were used when creating the record.

        Args:
          zone_id: Identifier

          data: Components of a SRV record.

          name: DNS record name (or @ for the zone apex) in Punycode. For SRV records, the first
              label is normally a service and the second a protocol name, each starting with
              an underscore.

          type: Record type.

          comment: Comments or notes about the DNS record. This field has no effect on DNS
              responses.

          tags: Custom tags for the DNS record. This field has no effect on DNS responses.

          ttl: Time To Live (TTL) of the DNS record in seconds. Setting to 1 means 'automatic'.
              Value must be between 60 and 86400, with the minimum reduced to 30 for
              Enterprise zones.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        zone_id: str,
        *,
        data: dns_record_create_params.DNSRecordsSshfpRecordData,
        name: str,
        type: Literal["SSHFP"],
        comment: str | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        ttl: Union[float, Literal[1]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DNSRecordCreateResponse:
        """
        Create a new DNS record for a zone.

        Notes:

        - A/AAAA records cannot exist on the same name as CNAME records.
        - NS records cannot exist on the same name as any other record type.
        - Domain names are always represented in Punycode, even if Unicode characters
          were used when creating the record.

        Args:
          zone_id: Identifier

          data: Components of a SSHFP record.

          name: DNS record name (or @ for the zone apex) in Punycode.

          type: Record type.

          comment: Comments or notes about the DNS record. This field has no effect on DNS
              responses.

          tags: Custom tags for the DNS record. This field has no effect on DNS responses.

          ttl: Time To Live (TTL) of the DNS record in seconds. Setting to 1 means 'automatic'.
              Value must be between 60 and 86400, with the minimum reduced to 30 for
              Enterprise zones.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        zone_id: str,
        *,
        data: dns_record_create_params.DNSRecordsSvcbRecordData,
        name: str,
        type: Literal["SVCB"],
        comment: str | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        ttl: Union[float, Literal[1]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DNSRecordCreateResponse:
        """
        Create a new DNS record for a zone.

        Notes:

        - A/AAAA records cannot exist on the same name as CNAME records.
        - NS records cannot exist on the same name as any other record type.
        - Domain names are always represented in Punycode, even if Unicode characters
          were used when creating the record.

        Args:
          zone_id: Identifier

          data: Components of a SVCB record.

          name: DNS record name (or @ for the zone apex) in Punycode.

          type: Record type.

          comment: Comments or notes about the DNS record. This field has no effect on DNS
              responses.

          tags: Custom tags for the DNS record. This field has no effect on DNS responses.

          ttl: Time To Live (TTL) of the DNS record in seconds. Setting to 1 means 'automatic'.
              Value must be between 60 and 86400, with the minimum reduced to 30 for
              Enterprise zones.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        zone_id: str,
        *,
        data: dns_record_create_params.DNSRecordsTlsaRecordData,
        name: str,
        type: Literal["TLSA"],
        comment: str | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        ttl: Union[float, Literal[1]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DNSRecordCreateResponse:
        """
        Create a new DNS record for a zone.

        Notes:

        - A/AAAA records cannot exist on the same name as CNAME records.
        - NS records cannot exist on the same name as any other record type.
        - Domain names are always represented in Punycode, even if Unicode characters
          were used when creating the record.

        Args:
          zone_id: Identifier

          data: Components of a TLSA record.

          name: DNS record name (or @ for the zone apex) in Punycode.

          type: Record type.

          comment: Comments or notes about the DNS record. This field has no effect on DNS
              responses.

          tags: Custom tags for the DNS record. This field has no effect on DNS responses.

          ttl: Time To Live (TTL) of the DNS record in seconds. Setting to 1 means 'automatic'.
              Value must be between 60 and 86400, with the minimum reduced to 30 for
              Enterprise zones.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        zone_id: str,
        *,
        content: str,
        name: str,
        type: Literal["TXT"],
        comment: str | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        ttl: Union[float, Literal[1]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DNSRecordCreateResponse:
        """
        Create a new DNS record for a zone.

        Notes:

        - A/AAAA records cannot exist on the same name as CNAME records.
        - NS records cannot exist on the same name as any other record type.
        - Domain names are always represented in Punycode, even if Unicode characters
          were used when creating the record.

        Args:
          zone_id: Identifier

          content: Text content for the record.

          name: DNS record name (or @ for the zone apex) in Punycode.

          type: Record type.

          comment: Comments or notes about the DNS record. This field has no effect on DNS
              responses.

          tags: Custom tags for the DNS record. This field has no effect on DNS responses.

          ttl: Time To Live (TTL) of the DNS record in seconds. Setting to 1 means 'automatic'.
              Value must be between 60 and 86400, with the minimum reduced to 30 for
              Enterprise zones.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        zone_id: str,
        *,
        data: dns_record_create_params.DNSRecordsUriRecordData,
        name: str,
        priority: float,
        type: Literal["URI"],
        comment: str | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        ttl: Union[float, Literal[1]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DNSRecordCreateResponse:
        """
        Create a new DNS record for a zone.

        Notes:

        - A/AAAA records cannot exist on the same name as CNAME records.
        - NS records cannot exist on the same name as any other record type.
        - Domain names are always represented in Punycode, even if Unicode characters
          were used when creating the record.

        Args:
          zone_id: Identifier

          data: Components of a URI record.

          name: DNS record name (or @ for the zone apex) in Punycode.

          priority: Required for MX, SRV and URI records; unused by other record types. Records with
              lower priorities are preferred.

          type: Record type.

          comment: Comments or notes about the DNS record. This field has no effect on DNS
              responses.

          tags: Custom tags for the DNS record. This field has no effect on DNS responses.

          ttl: Time To Live (TTL) of the DNS record in seconds. Setting to 1 means 'automatic'.
              Value must be between 60 and 86400, with the minimum reduced to 30 for
              Enterprise zones.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(
        ["content", "name", "type"],
        ["content", "name", "type"],
        ["data", "name", "type"],
        ["data", "name", "type"],
        ["content", "name", "type"],
        ["data", "name", "type"],
        ["data", "name", "type"],
        ["data", "name", "type"],
        ["data", "name", "type"],
        ["content", "name", "priority", "type"],
        ["data", "name", "type"],
        ["content", "name", "type"],
        ["content", "name", "type"],
        ["data", "name", "type"],
        ["data", "name", "type"],
        ["data", "name", "type"],
        ["data", "name", "type"],
        ["data", "name", "type"],
        ["content", "name", "type"],
        ["data", "name", "priority", "type"],
    )
    def create(
        self,
        zone_id: str,
        *,
        content: str | object | NotGiven = NOT_GIVEN,
        name: str,
        type: Literal["A"]
        | Literal["AAAA"]
        | Literal["CAA"]
        | Literal["CERT"]
        | Literal["CNAME"]
        | Literal["DNSKEY"]
        | Literal["DS"]
        | Literal["HTTPS"]
        | Literal["LOC"]
        | Literal["MX"]
        | Literal["NAPTR"]
        | Literal["NS"]
        | Literal["PTR"]
        | Literal["SMIMEA"]
        | Literal["SRV"]
        | Literal["SSHFP"]
        | Literal["SVCB"]
        | Literal["TLSA"]
        | Literal["TXT"]
        | Literal["URI"],
        comment: str | NotGiven = NOT_GIVEN,
        proxied: bool | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        ttl: Union[float, Literal[1]] | NotGiven = NOT_GIVEN,
        data: dns_record_create_params.DNSRecordsCaaRecordData
        | dns_record_create_params.DNSRecordsCertRecordData
        | dns_record_create_params.DNSRecordsDnskeyRecordData
        | dns_record_create_params.DNSRecordsDsRecordData
        | dns_record_create_params.DNSRecordsHTTPsRecordData
        | dns_record_create_params.DNSRecordsLocRecordData
        | dns_record_create_params.DNSRecordsNaptrRecordData
        | dns_record_create_params.DNSRecordsSmimeaRecordData
        | dns_record_create_params.DNSRecordsSrvRecordData
        | dns_record_create_params.DNSRecordsSshfpRecordData
        | dns_record_create_params.DNSRecordsUriRecordData
        | NotGiven = NOT_GIVEN,
        priority: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DNSRecordCreateResponse:
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return cast(
            DNSRecordCreateResponse,
            self._post(
                f"/zones/{zone_id}/dns_records",
                body=maybe_transform(
                    {
                        "content": content,
                        "name": name,
                        "type": type,
                        "comment": comment,
                        "proxied": proxied,
                        "tags": tags,
                        "ttl": ttl,
                        "data": data,
                        "priority": priority,
                    },
                    dns_record_create_params.DNSRecordCreateParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[DNSRecordCreateResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    @overload
    def update(
        self,
        dns_record_id: str,
        *,
        zone_id: str,
        content: str,
        name: str,
        type: Literal["A"],
        comment: str | NotGiven = NOT_GIVEN,
        proxied: bool | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        ttl: Union[float, Literal[1]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DNSRecordUpdateResponse:
        """Overwrite an existing DNS record.

        Notes:

        - A/AAAA records cannot exist on the same name as CNAME records.
        - NS records cannot exist on the same name as any other record type.
        - Domain names are always represented in Punycode, even if Unicode characters
          were used when creating the record.

        Args:
          zone_id: Identifier

          dns_record_id: Identifier

          content: A valid IPv4 address.

          name: DNS record name (or @ for the zone apex) in Punycode.

          type: Record type.

          comment: Comments or notes about the DNS record. This field has no effect on DNS
              responses.

          proxied: Whether the record is receiving the performance and security benefits of
              Cloudflare.

          tags: Custom tags for the DNS record. This field has no effect on DNS responses.

          ttl: Time To Live (TTL) of the DNS record in seconds. Setting to 1 means 'automatic'.
              Value must be between 60 and 86400, with the minimum reduced to 30 for
              Enterprise zones.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def update(
        self,
        dns_record_id: str,
        *,
        zone_id: str,
        content: str,
        name: str,
        type: Literal["AAAA"],
        comment: str | NotGiven = NOT_GIVEN,
        proxied: bool | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        ttl: Union[float, Literal[1]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DNSRecordUpdateResponse:
        """Overwrite an existing DNS record.

        Notes:

        - A/AAAA records cannot exist on the same name as CNAME records.
        - NS records cannot exist on the same name as any other record type.
        - Domain names are always represented in Punycode, even if Unicode characters
          were used when creating the record.

        Args:
          zone_id: Identifier

          dns_record_id: Identifier

          content: A valid IPv6 address.

          name: DNS record name (or @ for the zone apex) in Punycode.

          type: Record type.

          comment: Comments or notes about the DNS record. This field has no effect on DNS
              responses.

          proxied: Whether the record is receiving the performance and security benefits of
              Cloudflare.

          tags: Custom tags for the DNS record. This field has no effect on DNS responses.

          ttl: Time To Live (TTL) of the DNS record in seconds. Setting to 1 means 'automatic'.
              Value must be between 60 and 86400, with the minimum reduced to 30 for
              Enterprise zones.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def update(
        self,
        dns_record_id: str,
        *,
        zone_id: str,
        data: dns_record_update_params.DNSRecordsCaaRecordData,
        name: str,
        type: Literal["CAA"],
        comment: str | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        ttl: Union[float, Literal[1]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DNSRecordUpdateResponse:
        """Overwrite an existing DNS record.

        Notes:

        - A/AAAA records cannot exist on the same name as CNAME records.
        - NS records cannot exist on the same name as any other record type.
        - Domain names are always represented in Punycode, even if Unicode characters
          were used when creating the record.

        Args:
          zone_id: Identifier

          dns_record_id: Identifier

          data: Components of a CAA record.

          name: DNS record name (or @ for the zone apex) in Punycode.

          type: Record type.

          comment: Comments or notes about the DNS record. This field has no effect on DNS
              responses.

          tags: Custom tags for the DNS record. This field has no effect on DNS responses.

          ttl: Time To Live (TTL) of the DNS record in seconds. Setting to 1 means 'automatic'.
              Value must be between 60 and 86400, with the minimum reduced to 30 for
              Enterprise zones.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def update(
        self,
        dns_record_id: str,
        *,
        zone_id: str,
        data: dns_record_update_params.DNSRecordsCertRecordData,
        name: str,
        type: Literal["CERT"],
        comment: str | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        ttl: Union[float, Literal[1]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DNSRecordUpdateResponse:
        """Overwrite an existing DNS record.

        Notes:

        - A/AAAA records cannot exist on the same name as CNAME records.
        - NS records cannot exist on the same name as any other record type.
        - Domain names are always represented in Punycode, even if Unicode characters
          were used when creating the record.

        Args:
          zone_id: Identifier

          dns_record_id: Identifier

          data: Components of a CERT record.

          name: DNS record name (or @ for the zone apex) in Punycode.

          type: Record type.

          comment: Comments or notes about the DNS record. This field has no effect on DNS
              responses.

          tags: Custom tags for the DNS record. This field has no effect on DNS responses.

          ttl: Time To Live (TTL) of the DNS record in seconds. Setting to 1 means 'automatic'.
              Value must be between 60 and 86400, with the minimum reduced to 30 for
              Enterprise zones.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def update(
        self,
        dns_record_id: str,
        *,
        zone_id: str,
        content: object,
        name: str,
        type: Literal["CNAME"],
        comment: str | NotGiven = NOT_GIVEN,
        proxied: bool | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        ttl: Union[float, Literal[1]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DNSRecordUpdateResponse:
        """Overwrite an existing DNS record.

        Notes:

        - A/AAAA records cannot exist on the same name as CNAME records.
        - NS records cannot exist on the same name as any other record type.
        - Domain names are always represented in Punycode, even if Unicode characters
          were used when creating the record.

        Args:
          zone_id: Identifier

          dns_record_id: Identifier

          content: A valid hostname. Must not match the record's name.

          name: DNS record name (or @ for the zone apex) in Punycode.

          type: Record type.

          comment: Comments or notes about the DNS record. This field has no effect on DNS
              responses.

          proxied: Whether the record is receiving the performance and security benefits of
              Cloudflare.

          tags: Custom tags for the DNS record. This field has no effect on DNS responses.

          ttl: Time To Live (TTL) of the DNS record in seconds. Setting to 1 means 'automatic'.
              Value must be between 60 and 86400, with the minimum reduced to 30 for
              Enterprise zones.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def update(
        self,
        dns_record_id: str,
        *,
        zone_id: str,
        data: dns_record_update_params.DNSRecordsDnskeyRecordData,
        name: str,
        type: Literal["DNSKEY"],
        comment: str | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        ttl: Union[float, Literal[1]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DNSRecordUpdateResponse:
        """Overwrite an existing DNS record.

        Notes:

        - A/AAAA records cannot exist on the same name as CNAME records.
        - NS records cannot exist on the same name as any other record type.
        - Domain names are always represented in Punycode, even if Unicode characters
          were used when creating the record.

        Args:
          zone_id: Identifier

          dns_record_id: Identifier

          data: Components of a DNSKEY record.

          name: DNS record name (or @ for the zone apex) in Punycode.

          type: Record type.

          comment: Comments or notes about the DNS record. This field has no effect on DNS
              responses.

          tags: Custom tags for the DNS record. This field has no effect on DNS responses.

          ttl: Time To Live (TTL) of the DNS record in seconds. Setting to 1 means 'automatic'.
              Value must be between 60 and 86400, with the minimum reduced to 30 for
              Enterprise zones.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def update(
        self,
        dns_record_id: str,
        *,
        zone_id: str,
        data: dns_record_update_params.DNSRecordsDsRecordData,
        name: str,
        type: Literal["DS"],
        comment: str | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        ttl: Union[float, Literal[1]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DNSRecordUpdateResponse:
        """Overwrite an existing DNS record.

        Notes:

        - A/AAAA records cannot exist on the same name as CNAME records.
        - NS records cannot exist on the same name as any other record type.
        - Domain names are always represented in Punycode, even if Unicode characters
          were used when creating the record.

        Args:
          zone_id: Identifier

          dns_record_id: Identifier

          data: Components of a DS record.

          name: DNS record name (or @ for the zone apex) in Punycode.

          type: Record type.

          comment: Comments or notes about the DNS record. This field has no effect on DNS
              responses.

          tags: Custom tags for the DNS record. This field has no effect on DNS responses.

          ttl: Time To Live (TTL) of the DNS record in seconds. Setting to 1 means 'automatic'.
              Value must be between 60 and 86400, with the minimum reduced to 30 for
              Enterprise zones.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def update(
        self,
        dns_record_id: str,
        *,
        zone_id: str,
        data: dns_record_update_params.DNSRecordsHTTPsRecordData,
        name: str,
        type: Literal["HTTPS"],
        comment: str | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        ttl: Union[float, Literal[1]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DNSRecordUpdateResponse:
        """Overwrite an existing DNS record.

        Notes:

        - A/AAAA records cannot exist on the same name as CNAME records.
        - NS records cannot exist on the same name as any other record type.
        - Domain names are always represented in Punycode, even if Unicode characters
          were used when creating the record.

        Args:
          zone_id: Identifier

          dns_record_id: Identifier

          data: Components of a HTTPS record.

          name: DNS record name (or @ for the zone apex) in Punycode.

          type: Record type.

          comment: Comments or notes about the DNS record. This field has no effect on DNS
              responses.

          tags: Custom tags for the DNS record. This field has no effect on DNS responses.

          ttl: Time To Live (TTL) of the DNS record in seconds. Setting to 1 means 'automatic'.
              Value must be between 60 and 86400, with the minimum reduced to 30 for
              Enterprise zones.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def update(
        self,
        dns_record_id: str,
        *,
        zone_id: str,
        data: dns_record_update_params.DNSRecordsLocRecordData,
        name: str,
        type: Literal["LOC"],
        comment: str | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        ttl: Union[float, Literal[1]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DNSRecordUpdateResponse:
        """Overwrite an existing DNS record.

        Notes:

        - A/AAAA records cannot exist on the same name as CNAME records.
        - NS records cannot exist on the same name as any other record type.
        - Domain names are always represented in Punycode, even if Unicode characters
          were used when creating the record.

        Args:
          zone_id: Identifier

          dns_record_id: Identifier

          data: Components of a LOC record.

          name: DNS record name (or @ for the zone apex) in Punycode.

          type: Record type.

          comment: Comments or notes about the DNS record. This field has no effect on DNS
              responses.

          tags: Custom tags for the DNS record. This field has no effect on DNS responses.

          ttl: Time To Live (TTL) of the DNS record in seconds. Setting to 1 means 'automatic'.
              Value must be between 60 and 86400, with the minimum reduced to 30 for
              Enterprise zones.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def update(
        self,
        dns_record_id: str,
        *,
        zone_id: str,
        content: str,
        name: str,
        priority: float,
        type: Literal["MX"],
        comment: str | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        ttl: Union[float, Literal[1]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DNSRecordUpdateResponse:
        """Overwrite an existing DNS record.

        Notes:

        - A/AAAA records cannot exist on the same name as CNAME records.
        - NS records cannot exist on the same name as any other record type.
        - Domain names are always represented in Punycode, even if Unicode characters
          were used when creating the record.

        Args:
          zone_id: Identifier

          dns_record_id: Identifier

          content: A valid mail server hostname.

          name: DNS record name (or @ for the zone apex) in Punycode.

          priority: Required for MX, SRV and URI records; unused by other record types. Records with
              lower priorities are preferred.

          type: Record type.

          comment: Comments or notes about the DNS record. This field has no effect on DNS
              responses.

          tags: Custom tags for the DNS record. This field has no effect on DNS responses.

          ttl: Time To Live (TTL) of the DNS record in seconds. Setting to 1 means 'automatic'.
              Value must be between 60 and 86400, with the minimum reduced to 30 for
              Enterprise zones.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def update(
        self,
        dns_record_id: str,
        *,
        zone_id: str,
        data: dns_record_update_params.DNSRecordsNaptrRecordData,
        name: str,
        type: Literal["NAPTR"],
        comment: str | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        ttl: Union[float, Literal[1]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DNSRecordUpdateResponse:
        """Overwrite an existing DNS record.

        Notes:

        - A/AAAA records cannot exist on the same name as CNAME records.
        - NS records cannot exist on the same name as any other record type.
        - Domain names are always represented in Punycode, even if Unicode characters
          were used when creating the record.

        Args:
          zone_id: Identifier

          dns_record_id: Identifier

          data: Components of a NAPTR record.

          name: DNS record name (or @ for the zone apex) in Punycode.

          type: Record type.

          comment: Comments or notes about the DNS record. This field has no effect on DNS
              responses.

          tags: Custom tags for the DNS record. This field has no effect on DNS responses.

          ttl: Time To Live (TTL) of the DNS record in seconds. Setting to 1 means 'automatic'.
              Value must be between 60 and 86400, with the minimum reduced to 30 for
              Enterprise zones.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def update(
        self,
        dns_record_id: str,
        *,
        zone_id: str,
        content: object,
        name: str,
        type: Literal["NS"],
        comment: str | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        ttl: Union[float, Literal[1]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DNSRecordUpdateResponse:
        """Overwrite an existing DNS record.

        Notes:

        - A/AAAA records cannot exist on the same name as CNAME records.
        - NS records cannot exist on the same name as any other record type.
        - Domain names are always represented in Punycode, even if Unicode characters
          were used when creating the record.

        Args:
          zone_id: Identifier

          dns_record_id: Identifier

          content: A valid name server host name.

          name: DNS record name (or @ for the zone apex) in Punycode.

          type: Record type.

          comment: Comments or notes about the DNS record. This field has no effect on DNS
              responses.

          tags: Custom tags for the DNS record. This field has no effect on DNS responses.

          ttl: Time To Live (TTL) of the DNS record in seconds. Setting to 1 means 'automatic'.
              Value must be between 60 and 86400, with the minimum reduced to 30 for
              Enterprise zones.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def update(
        self,
        dns_record_id: str,
        *,
        zone_id: str,
        content: str,
        name: str,
        type: Literal["PTR"],
        comment: str | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        ttl: Union[float, Literal[1]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DNSRecordUpdateResponse:
        """Overwrite an existing DNS record.

        Notes:

        - A/AAAA records cannot exist on the same name as CNAME records.
        - NS records cannot exist on the same name as any other record type.
        - Domain names are always represented in Punycode, even if Unicode characters
          were used when creating the record.

        Args:
          zone_id: Identifier

          dns_record_id: Identifier

          content: Domain name pointing to the address.

          name: DNS record name (or @ for the zone apex) in Punycode.

          type: Record type.

          comment: Comments or notes about the DNS record. This field has no effect on DNS
              responses.

          tags: Custom tags for the DNS record. This field has no effect on DNS responses.

          ttl: Time To Live (TTL) of the DNS record in seconds. Setting to 1 means 'automatic'.
              Value must be between 60 and 86400, with the minimum reduced to 30 for
              Enterprise zones.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def update(
        self,
        dns_record_id: str,
        *,
        zone_id: str,
        data: dns_record_update_params.DNSRecordsSmimeaRecordData,
        name: str,
        type: Literal["SMIMEA"],
        comment: str | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        ttl: Union[float, Literal[1]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DNSRecordUpdateResponse:
        """Overwrite an existing DNS record.

        Notes:

        - A/AAAA records cannot exist on the same name as CNAME records.
        - NS records cannot exist on the same name as any other record type.
        - Domain names are always represented in Punycode, even if Unicode characters
          were used when creating the record.

        Args:
          zone_id: Identifier

          dns_record_id: Identifier

          data: Components of a SMIMEA record.

          name: DNS record name (or @ for the zone apex) in Punycode.

          type: Record type.

          comment: Comments or notes about the DNS record. This field has no effect on DNS
              responses.

          tags: Custom tags for the DNS record. This field has no effect on DNS responses.

          ttl: Time To Live (TTL) of the DNS record in seconds. Setting to 1 means 'automatic'.
              Value must be between 60 and 86400, with the minimum reduced to 30 for
              Enterprise zones.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def update(
        self,
        dns_record_id: str,
        *,
        zone_id: str,
        data: dns_record_update_params.DNSRecordsSrvRecordData,
        name: str,
        type: Literal["SRV"],
        comment: str | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        ttl: Union[float, Literal[1]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DNSRecordUpdateResponse:
        """Overwrite an existing DNS record.

        Notes:

        - A/AAAA records cannot exist on the same name as CNAME records.
        - NS records cannot exist on the same name as any other record type.
        - Domain names are always represented in Punycode, even if Unicode characters
          were used when creating the record.

        Args:
          zone_id: Identifier

          dns_record_id: Identifier

          data: Components of a SRV record.

          name: DNS record name (or @ for the zone apex) in Punycode. For SRV records, the first
              label is normally a service and the second a protocol name, each starting with
              an underscore.

          type: Record type.

          comment: Comments or notes about the DNS record. This field has no effect on DNS
              responses.

          tags: Custom tags for the DNS record. This field has no effect on DNS responses.

          ttl: Time To Live (TTL) of the DNS record in seconds. Setting to 1 means 'automatic'.
              Value must be between 60 and 86400, with the minimum reduced to 30 for
              Enterprise zones.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def update(
        self,
        dns_record_id: str,
        *,
        zone_id: str,
        data: dns_record_update_params.DNSRecordsSshfpRecordData,
        name: str,
        type: Literal["SSHFP"],
        comment: str | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        ttl: Union[float, Literal[1]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DNSRecordUpdateResponse:
        """Overwrite an existing DNS record.

        Notes:

        - A/AAAA records cannot exist on the same name as CNAME records.
        - NS records cannot exist on the same name as any other record type.
        - Domain names are always represented in Punycode, even if Unicode characters
          were used when creating the record.

        Args:
          zone_id: Identifier

          dns_record_id: Identifier

          data: Components of a SSHFP record.

          name: DNS record name (or @ for the zone apex) in Punycode.

          type: Record type.

          comment: Comments or notes about the DNS record. This field has no effect on DNS
              responses.

          tags: Custom tags for the DNS record. This field has no effect on DNS responses.

          ttl: Time To Live (TTL) of the DNS record in seconds. Setting to 1 means 'automatic'.
              Value must be between 60 and 86400, with the minimum reduced to 30 for
              Enterprise zones.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def update(
        self,
        dns_record_id: str,
        *,
        zone_id: str,
        data: dns_record_update_params.DNSRecordsSvcbRecordData,
        name: str,
        type: Literal["SVCB"],
        comment: str | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        ttl: Union[float, Literal[1]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DNSRecordUpdateResponse:
        """Overwrite an existing DNS record.

        Notes:

        - A/AAAA records cannot exist on the same name as CNAME records.
        - NS records cannot exist on the same name as any other record type.
        - Domain names are always represented in Punycode, even if Unicode characters
          were used when creating the record.

        Args:
          zone_id: Identifier

          dns_record_id: Identifier

          data: Components of a SVCB record.

          name: DNS record name (or @ for the zone apex) in Punycode.

          type: Record type.

          comment: Comments or notes about the DNS record. This field has no effect on DNS
              responses.

          tags: Custom tags for the DNS record. This field has no effect on DNS responses.

          ttl: Time To Live (TTL) of the DNS record in seconds. Setting to 1 means 'automatic'.
              Value must be between 60 and 86400, with the minimum reduced to 30 for
              Enterprise zones.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def update(
        self,
        dns_record_id: str,
        *,
        zone_id: str,
        data: dns_record_update_params.DNSRecordsTlsaRecordData,
        name: str,
        type: Literal["TLSA"],
        comment: str | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        ttl: Union[float, Literal[1]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DNSRecordUpdateResponse:
        """Overwrite an existing DNS record.

        Notes:

        - A/AAAA records cannot exist on the same name as CNAME records.
        - NS records cannot exist on the same name as any other record type.
        - Domain names are always represented in Punycode, even if Unicode characters
          were used when creating the record.

        Args:
          zone_id: Identifier

          dns_record_id: Identifier

          data: Components of a TLSA record.

          name: DNS record name (or @ for the zone apex) in Punycode.

          type: Record type.

          comment: Comments or notes about the DNS record. This field has no effect on DNS
              responses.

          tags: Custom tags for the DNS record. This field has no effect on DNS responses.

          ttl: Time To Live (TTL) of the DNS record in seconds. Setting to 1 means 'automatic'.
              Value must be between 60 and 86400, with the minimum reduced to 30 for
              Enterprise zones.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def update(
        self,
        dns_record_id: str,
        *,
        zone_id: str,
        content: str,
        name: str,
        type: Literal["TXT"],
        comment: str | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        ttl: Union[float, Literal[1]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DNSRecordUpdateResponse:
        """Overwrite an existing DNS record.

        Notes:

        - A/AAAA records cannot exist on the same name as CNAME records.
        - NS records cannot exist on the same name as any other record type.
        - Domain names are always represented in Punycode, even if Unicode characters
          were used when creating the record.

        Args:
          zone_id: Identifier

          dns_record_id: Identifier

          content: Text content for the record.

          name: DNS record name (or @ for the zone apex) in Punycode.

          type: Record type.

          comment: Comments or notes about the DNS record. This field has no effect on DNS
              responses.

          tags: Custom tags for the DNS record. This field has no effect on DNS responses.

          ttl: Time To Live (TTL) of the DNS record in seconds. Setting to 1 means 'automatic'.
              Value must be between 60 and 86400, with the minimum reduced to 30 for
              Enterprise zones.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def update(
        self,
        dns_record_id: str,
        *,
        zone_id: str,
        data: dns_record_update_params.DNSRecordsUriRecordData,
        name: str,
        priority: float,
        type: Literal["URI"],
        comment: str | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        ttl: Union[float, Literal[1]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DNSRecordUpdateResponse:
        """Overwrite an existing DNS record.

        Notes:

        - A/AAAA records cannot exist on the same name as CNAME records.
        - NS records cannot exist on the same name as any other record type.
        - Domain names are always represented in Punycode, even if Unicode characters
          were used when creating the record.

        Args:
          zone_id: Identifier

          dns_record_id: Identifier

          data: Components of a URI record.

          name: DNS record name (or @ for the zone apex) in Punycode.

          priority: Required for MX, SRV and URI records; unused by other record types. Records with
              lower priorities are preferred.

          type: Record type.

          comment: Comments or notes about the DNS record. This field has no effect on DNS
              responses.

          tags: Custom tags for the DNS record. This field has no effect on DNS responses.

          ttl: Time To Live (TTL) of the DNS record in seconds. Setting to 1 means 'automatic'.
              Value must be between 60 and 86400, with the minimum reduced to 30 for
              Enterprise zones.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(
        ["zone_id", "content", "name", "type"],
        ["zone_id", "content", "name", "type"],
        ["zone_id", "data", "name", "type"],
        ["zone_id", "data", "name", "type"],
        ["zone_id", "content", "name", "type"],
        ["zone_id", "data", "name", "type"],
        ["zone_id", "data", "name", "type"],
        ["zone_id", "data", "name", "type"],
        ["zone_id", "data", "name", "type"],
        ["zone_id", "content", "name", "priority", "type"],
        ["zone_id", "data", "name", "type"],
        ["zone_id", "content", "name", "type"],
        ["zone_id", "content", "name", "type"],
        ["zone_id", "data", "name", "type"],
        ["zone_id", "data", "name", "type"],
        ["zone_id", "data", "name", "type"],
        ["zone_id", "data", "name", "type"],
        ["zone_id", "data", "name", "type"],
        ["zone_id", "content", "name", "type"],
        ["zone_id", "data", "name", "priority", "type"],
    )
    def update(
        self,
        dns_record_id: str,
        *,
        zone_id: str,
        content: str | object | NotGiven = NOT_GIVEN,
        name: str,
        type: Literal["A"]
        | Literal["AAAA"]
        | Literal["CAA"]
        | Literal["CERT"]
        | Literal["CNAME"]
        | Literal["DNSKEY"]
        | Literal["DS"]
        | Literal["HTTPS"]
        | Literal["LOC"]
        | Literal["MX"]
        | Literal["NAPTR"]
        | Literal["NS"]
        | Literal["PTR"]
        | Literal["SMIMEA"]
        | Literal["SRV"]
        | Literal["SSHFP"]
        | Literal["SVCB"]
        | Literal["TLSA"]
        | Literal["TXT"]
        | Literal["URI"],
        comment: str | NotGiven = NOT_GIVEN,
        proxied: bool | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        ttl: Union[float, Literal[1]] | NotGiven = NOT_GIVEN,
        data: dns_record_update_params.DNSRecordsCaaRecordData
        | dns_record_update_params.DNSRecordsCertRecordData
        | dns_record_update_params.DNSRecordsDnskeyRecordData
        | dns_record_update_params.DNSRecordsDsRecordData
        | dns_record_update_params.DNSRecordsHTTPsRecordData
        | dns_record_update_params.DNSRecordsLocRecordData
        | dns_record_update_params.DNSRecordsNaptrRecordData
        | dns_record_update_params.DNSRecordsSmimeaRecordData
        | dns_record_update_params.DNSRecordsSrvRecordData
        | dns_record_update_params.DNSRecordsSshfpRecordData
        | dns_record_update_params.DNSRecordsUriRecordData
        | NotGiven = NOT_GIVEN,
        priority: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DNSRecordUpdateResponse:
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not dns_record_id:
            raise ValueError(f"Expected a non-empty value for `dns_record_id` but received {dns_record_id!r}")
        return cast(
            DNSRecordUpdateResponse,
            self._put(
                f"/zones/{zone_id}/dns_records/{dns_record_id}",
                body=maybe_transform(
                    {
                        "content": content,
                        "name": name,
                        "type": type,
                        "comment": comment,
                        "proxied": proxied,
                        "tags": tags,
                        "ttl": ttl,
                        "data": data,
                        "priority": priority,
                    },
                    dns_record_update_params.DNSRecordUpdateParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[DNSRecordUpdateResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def list(
        self,
        zone_id: str,
        *,
        comment: dns_record_list_params.Comment | NotGiven = NOT_GIVEN,
        content: str | NotGiven = NOT_GIVEN,
        direction: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
        match: Literal["any", "all"] | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        order: Literal["type", "name", "content", "ttl", "proxied"] | NotGiven = NOT_GIVEN,
        page: float | NotGiven = NOT_GIVEN,
        per_page: float | NotGiven = NOT_GIVEN,
        proxied: bool | NotGiven = NOT_GIVEN,
        search: str | NotGiven = NOT_GIVEN,
        tag: dns_record_list_params.Tag | NotGiven = NOT_GIVEN,
        tag_match: Literal["any", "all"] | NotGiven = NOT_GIVEN,
        type: Literal[
            "A",
            "AAAA",
            "CAA",
            "CERT",
            "CNAME",
            "DNSKEY",
            "DS",
            "HTTPS",
            "LOC",
            "MX",
            "NAPTR",
            "NS",
            "PTR",
            "SMIMEA",
            "SRV",
            "SSHFP",
            "SVCB",
            "TLSA",
            "TXT",
            "URI",
        ]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[DNSRecordListResponse]:
        """
        List, search, sort, and filter a zones' DNS records.

        Args:
          zone_id: Identifier

          content: DNS record content.

          direction: Direction to order DNS records in.

          match: Whether to match all search requirements or at least one (any). If set to `all`,
              acts like a logical AND between filters. If set to `any`, acts like a logical OR
              instead. Note that the interaction between tag filters is controlled by the
              `tag-match` parameter instead.

          name: DNS record name (or @ for the zone apex) in Punycode.

          order: Field to order DNS records by.

          page: Page number of paginated results.

          per_page: Number of DNS records per page.

          proxied: Whether the record is receiving the performance and security benefits of
              Cloudflare.

          search: Allows searching in multiple properties of a DNS record simultaneously. This
              parameter is intended for human users, not automation. Its exact behavior is
              intentionally left unspecified and is subject to change in the future. This
              parameter works independently of the `match` setting. For automated searches,
              please use the other available parameters.

          tag_match: Whether to match all tag search requirements or at least one (any). If set to
              `all`, acts like a logical AND between tag filters. If set to `any`, acts like a
              logical OR instead. Note that the regular `match` parameter is still used to
              combine the resulting condition with other filters that aren't related to tags.

          type: Record type.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._get(
            f"/zones/{zone_id}/dns_records",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "comment": comment,
                        "content": content,
                        "direction": direction,
                        "match": match,
                        "name": name,
                        "order": order,
                        "page": page,
                        "per_page": per_page,
                        "proxied": proxied,
                        "search": search,
                        "tag": tag,
                        "tag_match": tag_match,
                        "type": type,
                    },
                    dns_record_list_params.DNSRecordListParams,
                ),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[DNSRecordListResponse]], ResultWrapper[DNSRecordListResponse]),
        )

    def delete(
        self,
        dns_record_id: str,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[DNSRecordDeleteResponse]:
        """
        Delete DNS Record

        Args:
          zone_id: Identifier

          dns_record_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not dns_record_id:
            raise ValueError(f"Expected a non-empty value for `dns_record_id` but received {dns_record_id!r}")
        return self._delete(
            f"/zones/{zone_id}/dns_records/{dns_record_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[DNSRecordDeleteResponse]], ResultWrapper[DNSRecordDeleteResponse]),
        )

    def export(
        self,
        zone_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> str:
        """
        You can export your
        [BIND config](https://en.wikipedia.org/wiki/Zone_file "Zone file") through this
        endpoint.

        See
        [the documentation](https://developers.cloudflare.com/dns/manage-dns-records/how-to/import-and-export/ "Import and export records")
        for more information.

        Args:
          zone_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        extra_headers = {"Accept": "text/plain", **(extra_headers or {})}
        return self._get(
            f"/zones/{zone_id}/dns_records/export",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )

    def get(
        self,
        dns_record_id: str,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DNSRecordGetResponse:
        """
        DNS Record Details

        Args:
          zone_id: Identifier

          dns_record_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not dns_record_id:
            raise ValueError(f"Expected a non-empty value for `dns_record_id` but received {dns_record_id!r}")
        return cast(
            DNSRecordGetResponse,
            self._get(
                f"/zones/{zone_id}/dns_records/{dns_record_id}",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[DNSRecordGetResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def import_(
        self,
        zone_id: str,
        *,
        file: str,
        proxied: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DNSRecordImportResponse:
        """
        You can upload your
        [BIND config](https://en.wikipedia.org/wiki/Zone_file "Zone file") through this
        endpoint. It assumes that cURL is called from a location with bind_config.txt
        (valid BIND config) present.

        See
        [the documentation](https://developers.cloudflare.com/dns/manage-dns-records/how-to/import-and-export/ "Import and export records")
        for more information.

        Args:
          zone_id: Identifier

          file: BIND config to import.

              **Tip:** When using cURL, a file can be uploaded using
              `--form 'file=@bind_config.txt'`.

          proxied: Whether or not proxiable records should receive the performance and security
              benefits of Cloudflare.

              The value should be either `true` or `false`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._post(
            f"/zones/{zone_id}/dns_records/import",
            body=maybe_transform(
                {
                    "file": file,
                    "proxied": proxied,
                },
                dns_record_import_params.DNSRecordImportParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[DNSRecordImportResponse], ResultWrapper[DNSRecordImportResponse]),
        )

    def scan(
        self,
        zone_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DNSRecordScanResponse:
        """
        Scan for common DNS records on your domain and automatically add them to your
        zone. Useful if you haven't updated your nameservers yet.

        Args:
          zone_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._post(
            f"/zones/{zone_id}/dns_records/scan",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[DNSRecordScanResponse], ResultWrapper[DNSRecordScanResponse]),
        )


class AsyncDNSRecords(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDNSRecordsWithRawResponse:
        return AsyncDNSRecordsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDNSRecordsWithStreamingResponse:
        return AsyncDNSRecordsWithStreamingResponse(self)

    @overload
    async def create(
        self,
        zone_id: str,
        *,
        content: str,
        name: str,
        type: Literal["A"],
        comment: str | NotGiven = NOT_GIVEN,
        proxied: bool | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        ttl: Union[float, Literal[1]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DNSRecordCreateResponse:
        """
        Create a new DNS record for a zone.

        Notes:

        - A/AAAA records cannot exist on the same name as CNAME records.
        - NS records cannot exist on the same name as any other record type.
        - Domain names are always represented in Punycode, even if Unicode characters
          were used when creating the record.

        Args:
          zone_id: Identifier

          content: A valid IPv4 address.

          name: DNS record name (or @ for the zone apex) in Punycode.

          type: Record type.

          comment: Comments or notes about the DNS record. This field has no effect on DNS
              responses.

          proxied: Whether the record is receiving the performance and security benefits of
              Cloudflare.

          tags: Custom tags for the DNS record. This field has no effect on DNS responses.

          ttl: Time To Live (TTL) of the DNS record in seconds. Setting to 1 means 'automatic'.
              Value must be between 60 and 86400, with the minimum reduced to 30 for
              Enterprise zones.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        zone_id: str,
        *,
        content: str,
        name: str,
        type: Literal["AAAA"],
        comment: str | NotGiven = NOT_GIVEN,
        proxied: bool | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        ttl: Union[float, Literal[1]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DNSRecordCreateResponse:
        """
        Create a new DNS record for a zone.

        Notes:

        - A/AAAA records cannot exist on the same name as CNAME records.
        - NS records cannot exist on the same name as any other record type.
        - Domain names are always represented in Punycode, even if Unicode characters
          were used when creating the record.

        Args:
          zone_id: Identifier

          content: A valid IPv6 address.

          name: DNS record name (or @ for the zone apex) in Punycode.

          type: Record type.

          comment: Comments or notes about the DNS record. This field has no effect on DNS
              responses.

          proxied: Whether the record is receiving the performance and security benefits of
              Cloudflare.

          tags: Custom tags for the DNS record. This field has no effect on DNS responses.

          ttl: Time To Live (TTL) of the DNS record in seconds. Setting to 1 means 'automatic'.
              Value must be between 60 and 86400, with the minimum reduced to 30 for
              Enterprise zones.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        zone_id: str,
        *,
        data: dns_record_create_params.DNSRecordsCaaRecordData,
        name: str,
        type: Literal["CAA"],
        comment: str | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        ttl: Union[float, Literal[1]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DNSRecordCreateResponse:
        """
        Create a new DNS record for a zone.

        Notes:

        - A/AAAA records cannot exist on the same name as CNAME records.
        - NS records cannot exist on the same name as any other record type.
        - Domain names are always represented in Punycode, even if Unicode characters
          were used when creating the record.

        Args:
          zone_id: Identifier

          data: Components of a CAA record.

          name: DNS record name (or @ for the zone apex) in Punycode.

          type: Record type.

          comment: Comments or notes about the DNS record. This field has no effect on DNS
              responses.

          tags: Custom tags for the DNS record. This field has no effect on DNS responses.

          ttl: Time To Live (TTL) of the DNS record in seconds. Setting to 1 means 'automatic'.
              Value must be between 60 and 86400, with the minimum reduced to 30 for
              Enterprise zones.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        zone_id: str,
        *,
        data: dns_record_create_params.DNSRecordsCertRecordData,
        name: str,
        type: Literal["CERT"],
        comment: str | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        ttl: Union[float, Literal[1]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DNSRecordCreateResponse:
        """
        Create a new DNS record for a zone.

        Notes:

        - A/AAAA records cannot exist on the same name as CNAME records.
        - NS records cannot exist on the same name as any other record type.
        - Domain names are always represented in Punycode, even if Unicode characters
          were used when creating the record.

        Args:
          zone_id: Identifier

          data: Components of a CERT record.

          name: DNS record name (or @ for the zone apex) in Punycode.

          type: Record type.

          comment: Comments or notes about the DNS record. This field has no effect on DNS
              responses.

          tags: Custom tags for the DNS record. This field has no effect on DNS responses.

          ttl: Time To Live (TTL) of the DNS record in seconds. Setting to 1 means 'automatic'.
              Value must be between 60 and 86400, with the minimum reduced to 30 for
              Enterprise zones.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        zone_id: str,
        *,
        content: object,
        name: str,
        type: Literal["CNAME"],
        comment: str | NotGiven = NOT_GIVEN,
        proxied: bool | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        ttl: Union[float, Literal[1]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DNSRecordCreateResponse:
        """
        Create a new DNS record for a zone.

        Notes:

        - A/AAAA records cannot exist on the same name as CNAME records.
        - NS records cannot exist on the same name as any other record type.
        - Domain names are always represented in Punycode, even if Unicode characters
          were used when creating the record.

        Args:
          zone_id: Identifier

          content: A valid hostname. Must not match the record's name.

          name: DNS record name (or @ for the zone apex) in Punycode.

          type: Record type.

          comment: Comments or notes about the DNS record. This field has no effect on DNS
              responses.

          proxied: Whether the record is receiving the performance and security benefits of
              Cloudflare.

          tags: Custom tags for the DNS record. This field has no effect on DNS responses.

          ttl: Time To Live (TTL) of the DNS record in seconds. Setting to 1 means 'automatic'.
              Value must be between 60 and 86400, with the minimum reduced to 30 for
              Enterprise zones.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        zone_id: str,
        *,
        data: dns_record_create_params.DNSRecordsDnskeyRecordData,
        name: str,
        type: Literal["DNSKEY"],
        comment: str | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        ttl: Union[float, Literal[1]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DNSRecordCreateResponse:
        """
        Create a new DNS record for a zone.

        Notes:

        - A/AAAA records cannot exist on the same name as CNAME records.
        - NS records cannot exist on the same name as any other record type.
        - Domain names are always represented in Punycode, even if Unicode characters
          were used when creating the record.

        Args:
          zone_id: Identifier

          data: Components of a DNSKEY record.

          name: DNS record name (or @ for the zone apex) in Punycode.

          type: Record type.

          comment: Comments or notes about the DNS record. This field has no effect on DNS
              responses.

          tags: Custom tags for the DNS record. This field has no effect on DNS responses.

          ttl: Time To Live (TTL) of the DNS record in seconds. Setting to 1 means 'automatic'.
              Value must be between 60 and 86400, with the minimum reduced to 30 for
              Enterprise zones.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        zone_id: str,
        *,
        data: dns_record_create_params.DNSRecordsDsRecordData,
        name: str,
        type: Literal["DS"],
        comment: str | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        ttl: Union[float, Literal[1]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DNSRecordCreateResponse:
        """
        Create a new DNS record for a zone.

        Notes:

        - A/AAAA records cannot exist on the same name as CNAME records.
        - NS records cannot exist on the same name as any other record type.
        - Domain names are always represented in Punycode, even if Unicode characters
          were used when creating the record.

        Args:
          zone_id: Identifier

          data: Components of a DS record.

          name: DNS record name (or @ for the zone apex) in Punycode.

          type: Record type.

          comment: Comments or notes about the DNS record. This field has no effect on DNS
              responses.

          tags: Custom tags for the DNS record. This field has no effect on DNS responses.

          ttl: Time To Live (TTL) of the DNS record in seconds. Setting to 1 means 'automatic'.
              Value must be between 60 and 86400, with the minimum reduced to 30 for
              Enterprise zones.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        zone_id: str,
        *,
        data: dns_record_create_params.DNSRecordsHTTPsRecordData,
        name: str,
        type: Literal["HTTPS"],
        comment: str | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        ttl: Union[float, Literal[1]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DNSRecordCreateResponse:
        """
        Create a new DNS record for a zone.

        Notes:

        - A/AAAA records cannot exist on the same name as CNAME records.
        - NS records cannot exist on the same name as any other record type.
        - Domain names are always represented in Punycode, even if Unicode characters
          were used when creating the record.

        Args:
          zone_id: Identifier

          data: Components of a HTTPS record.

          name: DNS record name (or @ for the zone apex) in Punycode.

          type: Record type.

          comment: Comments or notes about the DNS record. This field has no effect on DNS
              responses.

          tags: Custom tags for the DNS record. This field has no effect on DNS responses.

          ttl: Time To Live (TTL) of the DNS record in seconds. Setting to 1 means 'automatic'.
              Value must be between 60 and 86400, with the minimum reduced to 30 for
              Enterprise zones.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        zone_id: str,
        *,
        data: dns_record_create_params.DNSRecordsLocRecordData,
        name: str,
        type: Literal["LOC"],
        comment: str | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        ttl: Union[float, Literal[1]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DNSRecordCreateResponse:
        """
        Create a new DNS record for a zone.

        Notes:

        - A/AAAA records cannot exist on the same name as CNAME records.
        - NS records cannot exist on the same name as any other record type.
        - Domain names are always represented in Punycode, even if Unicode characters
          were used when creating the record.

        Args:
          zone_id: Identifier

          data: Components of a LOC record.

          name: DNS record name (or @ for the zone apex) in Punycode.

          type: Record type.

          comment: Comments or notes about the DNS record. This field has no effect on DNS
              responses.

          tags: Custom tags for the DNS record. This field has no effect on DNS responses.

          ttl: Time To Live (TTL) of the DNS record in seconds. Setting to 1 means 'automatic'.
              Value must be between 60 and 86400, with the minimum reduced to 30 for
              Enterprise zones.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        zone_id: str,
        *,
        content: str,
        name: str,
        priority: float,
        type: Literal["MX"],
        comment: str | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        ttl: Union[float, Literal[1]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DNSRecordCreateResponse:
        """
        Create a new DNS record for a zone.

        Notes:

        - A/AAAA records cannot exist on the same name as CNAME records.
        - NS records cannot exist on the same name as any other record type.
        - Domain names are always represented in Punycode, even if Unicode characters
          were used when creating the record.

        Args:
          zone_id: Identifier

          content: A valid mail server hostname.

          name: DNS record name (or @ for the zone apex) in Punycode.

          priority: Required for MX, SRV and URI records; unused by other record types. Records with
              lower priorities are preferred.

          type: Record type.

          comment: Comments or notes about the DNS record. This field has no effect on DNS
              responses.

          tags: Custom tags for the DNS record. This field has no effect on DNS responses.

          ttl: Time To Live (TTL) of the DNS record in seconds. Setting to 1 means 'automatic'.
              Value must be between 60 and 86400, with the minimum reduced to 30 for
              Enterprise zones.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        zone_id: str,
        *,
        data: dns_record_create_params.DNSRecordsNaptrRecordData,
        name: str,
        type: Literal["NAPTR"],
        comment: str | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        ttl: Union[float, Literal[1]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DNSRecordCreateResponse:
        """
        Create a new DNS record for a zone.

        Notes:

        - A/AAAA records cannot exist on the same name as CNAME records.
        - NS records cannot exist on the same name as any other record type.
        - Domain names are always represented in Punycode, even if Unicode characters
          were used when creating the record.

        Args:
          zone_id: Identifier

          data: Components of a NAPTR record.

          name: DNS record name (or @ for the zone apex) in Punycode.

          type: Record type.

          comment: Comments or notes about the DNS record. This field has no effect on DNS
              responses.

          tags: Custom tags for the DNS record. This field has no effect on DNS responses.

          ttl: Time To Live (TTL) of the DNS record in seconds. Setting to 1 means 'automatic'.
              Value must be between 60 and 86400, with the minimum reduced to 30 for
              Enterprise zones.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        zone_id: str,
        *,
        content: object,
        name: str,
        type: Literal["NS"],
        comment: str | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        ttl: Union[float, Literal[1]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DNSRecordCreateResponse:
        """
        Create a new DNS record for a zone.

        Notes:

        - A/AAAA records cannot exist on the same name as CNAME records.
        - NS records cannot exist on the same name as any other record type.
        - Domain names are always represented in Punycode, even if Unicode characters
          were used when creating the record.

        Args:
          zone_id: Identifier

          content: A valid name server host name.

          name: DNS record name (or @ for the zone apex) in Punycode.

          type: Record type.

          comment: Comments or notes about the DNS record. This field has no effect on DNS
              responses.

          tags: Custom tags for the DNS record. This field has no effect on DNS responses.

          ttl: Time To Live (TTL) of the DNS record in seconds. Setting to 1 means 'automatic'.
              Value must be between 60 and 86400, with the minimum reduced to 30 for
              Enterprise zones.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        zone_id: str,
        *,
        content: str,
        name: str,
        type: Literal["PTR"],
        comment: str | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        ttl: Union[float, Literal[1]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DNSRecordCreateResponse:
        """
        Create a new DNS record for a zone.

        Notes:

        - A/AAAA records cannot exist on the same name as CNAME records.
        - NS records cannot exist on the same name as any other record type.
        - Domain names are always represented in Punycode, even if Unicode characters
          were used when creating the record.

        Args:
          zone_id: Identifier

          content: Domain name pointing to the address.

          name: DNS record name (or @ for the zone apex) in Punycode.

          type: Record type.

          comment: Comments or notes about the DNS record. This field has no effect on DNS
              responses.

          tags: Custom tags for the DNS record. This field has no effect on DNS responses.

          ttl: Time To Live (TTL) of the DNS record in seconds. Setting to 1 means 'automatic'.
              Value must be between 60 and 86400, with the minimum reduced to 30 for
              Enterprise zones.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        zone_id: str,
        *,
        data: dns_record_create_params.DNSRecordsSmimeaRecordData,
        name: str,
        type: Literal["SMIMEA"],
        comment: str | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        ttl: Union[float, Literal[1]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DNSRecordCreateResponse:
        """
        Create a new DNS record for a zone.

        Notes:

        - A/AAAA records cannot exist on the same name as CNAME records.
        - NS records cannot exist on the same name as any other record type.
        - Domain names are always represented in Punycode, even if Unicode characters
          were used when creating the record.

        Args:
          zone_id: Identifier

          data: Components of a SMIMEA record.

          name: DNS record name (or @ for the zone apex) in Punycode.

          type: Record type.

          comment: Comments or notes about the DNS record. This field has no effect on DNS
              responses.

          tags: Custom tags for the DNS record. This field has no effect on DNS responses.

          ttl: Time To Live (TTL) of the DNS record in seconds. Setting to 1 means 'automatic'.
              Value must be between 60 and 86400, with the minimum reduced to 30 for
              Enterprise zones.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        zone_id: str,
        *,
        data: dns_record_create_params.DNSRecordsSrvRecordData,
        name: str,
        type: Literal["SRV"],
        comment: str | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        ttl: Union[float, Literal[1]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DNSRecordCreateResponse:
        """
        Create a new DNS record for a zone.

        Notes:

        - A/AAAA records cannot exist on the same name as CNAME records.
        - NS records cannot exist on the same name as any other record type.
        - Domain names are always represented in Punycode, even if Unicode characters
          were used when creating the record.

        Args:
          zone_id: Identifier

          data: Components of a SRV record.

          name: DNS record name (or @ for the zone apex) in Punycode. For SRV records, the first
              label is normally a service and the second a protocol name, each starting with
              an underscore.

          type: Record type.

          comment: Comments or notes about the DNS record. This field has no effect on DNS
              responses.

          tags: Custom tags for the DNS record. This field has no effect on DNS responses.

          ttl: Time To Live (TTL) of the DNS record in seconds. Setting to 1 means 'automatic'.
              Value must be between 60 and 86400, with the minimum reduced to 30 for
              Enterprise zones.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        zone_id: str,
        *,
        data: dns_record_create_params.DNSRecordsSshfpRecordData,
        name: str,
        type: Literal["SSHFP"],
        comment: str | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        ttl: Union[float, Literal[1]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DNSRecordCreateResponse:
        """
        Create a new DNS record for a zone.

        Notes:

        - A/AAAA records cannot exist on the same name as CNAME records.
        - NS records cannot exist on the same name as any other record type.
        - Domain names are always represented in Punycode, even if Unicode characters
          were used when creating the record.

        Args:
          zone_id: Identifier

          data: Components of a SSHFP record.

          name: DNS record name (or @ for the zone apex) in Punycode.

          type: Record type.

          comment: Comments or notes about the DNS record. This field has no effect on DNS
              responses.

          tags: Custom tags for the DNS record. This field has no effect on DNS responses.

          ttl: Time To Live (TTL) of the DNS record in seconds. Setting to 1 means 'automatic'.
              Value must be between 60 and 86400, with the minimum reduced to 30 for
              Enterprise zones.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        zone_id: str,
        *,
        data: dns_record_create_params.DNSRecordsSvcbRecordData,
        name: str,
        type: Literal["SVCB"],
        comment: str | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        ttl: Union[float, Literal[1]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DNSRecordCreateResponse:
        """
        Create a new DNS record for a zone.

        Notes:

        - A/AAAA records cannot exist on the same name as CNAME records.
        - NS records cannot exist on the same name as any other record type.
        - Domain names are always represented in Punycode, even if Unicode characters
          were used when creating the record.

        Args:
          zone_id: Identifier

          data: Components of a SVCB record.

          name: DNS record name (or @ for the zone apex) in Punycode.

          type: Record type.

          comment: Comments or notes about the DNS record. This field has no effect on DNS
              responses.

          tags: Custom tags for the DNS record. This field has no effect on DNS responses.

          ttl: Time To Live (TTL) of the DNS record in seconds. Setting to 1 means 'automatic'.
              Value must be between 60 and 86400, with the minimum reduced to 30 for
              Enterprise zones.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        zone_id: str,
        *,
        data: dns_record_create_params.DNSRecordsTlsaRecordData,
        name: str,
        type: Literal["TLSA"],
        comment: str | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        ttl: Union[float, Literal[1]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DNSRecordCreateResponse:
        """
        Create a new DNS record for a zone.

        Notes:

        - A/AAAA records cannot exist on the same name as CNAME records.
        - NS records cannot exist on the same name as any other record type.
        - Domain names are always represented in Punycode, even if Unicode characters
          were used when creating the record.

        Args:
          zone_id: Identifier

          data: Components of a TLSA record.

          name: DNS record name (or @ for the zone apex) in Punycode.

          type: Record type.

          comment: Comments or notes about the DNS record. This field has no effect on DNS
              responses.

          tags: Custom tags for the DNS record. This field has no effect on DNS responses.

          ttl: Time To Live (TTL) of the DNS record in seconds. Setting to 1 means 'automatic'.
              Value must be between 60 and 86400, with the minimum reduced to 30 for
              Enterprise zones.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        zone_id: str,
        *,
        content: str,
        name: str,
        type: Literal["TXT"],
        comment: str | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        ttl: Union[float, Literal[1]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DNSRecordCreateResponse:
        """
        Create a new DNS record for a zone.

        Notes:

        - A/AAAA records cannot exist on the same name as CNAME records.
        - NS records cannot exist on the same name as any other record type.
        - Domain names are always represented in Punycode, even if Unicode characters
          were used when creating the record.

        Args:
          zone_id: Identifier

          content: Text content for the record.

          name: DNS record name (or @ for the zone apex) in Punycode.

          type: Record type.

          comment: Comments or notes about the DNS record. This field has no effect on DNS
              responses.

          tags: Custom tags for the DNS record. This field has no effect on DNS responses.

          ttl: Time To Live (TTL) of the DNS record in seconds. Setting to 1 means 'automatic'.
              Value must be between 60 and 86400, with the minimum reduced to 30 for
              Enterprise zones.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        zone_id: str,
        *,
        data: dns_record_create_params.DNSRecordsUriRecordData,
        name: str,
        priority: float,
        type: Literal["URI"],
        comment: str | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        ttl: Union[float, Literal[1]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DNSRecordCreateResponse:
        """
        Create a new DNS record for a zone.

        Notes:

        - A/AAAA records cannot exist on the same name as CNAME records.
        - NS records cannot exist on the same name as any other record type.
        - Domain names are always represented in Punycode, even if Unicode characters
          were used when creating the record.

        Args:
          zone_id: Identifier

          data: Components of a URI record.

          name: DNS record name (or @ for the zone apex) in Punycode.

          priority: Required for MX, SRV and URI records; unused by other record types. Records with
              lower priorities are preferred.

          type: Record type.

          comment: Comments or notes about the DNS record. This field has no effect on DNS
              responses.

          tags: Custom tags for the DNS record. This field has no effect on DNS responses.

          ttl: Time To Live (TTL) of the DNS record in seconds. Setting to 1 means 'automatic'.
              Value must be between 60 and 86400, with the minimum reduced to 30 for
              Enterprise zones.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(
        ["content", "name", "type"],
        ["content", "name", "type"],
        ["data", "name", "type"],
        ["data", "name", "type"],
        ["content", "name", "type"],
        ["data", "name", "type"],
        ["data", "name", "type"],
        ["data", "name", "type"],
        ["data", "name", "type"],
        ["content", "name", "priority", "type"],
        ["data", "name", "type"],
        ["content", "name", "type"],
        ["content", "name", "type"],
        ["data", "name", "type"],
        ["data", "name", "type"],
        ["data", "name", "type"],
        ["data", "name", "type"],
        ["data", "name", "type"],
        ["content", "name", "type"],
        ["data", "name", "priority", "type"],
    )
    async def create(
        self,
        zone_id: str,
        *,
        content: str | object | NotGiven = NOT_GIVEN,
        name: str,
        type: Literal["A"]
        | Literal["AAAA"]
        | Literal["CAA"]
        | Literal["CERT"]
        | Literal["CNAME"]
        | Literal["DNSKEY"]
        | Literal["DS"]
        | Literal["HTTPS"]
        | Literal["LOC"]
        | Literal["MX"]
        | Literal["NAPTR"]
        | Literal["NS"]
        | Literal["PTR"]
        | Literal["SMIMEA"]
        | Literal["SRV"]
        | Literal["SSHFP"]
        | Literal["SVCB"]
        | Literal["TLSA"]
        | Literal["TXT"]
        | Literal["URI"],
        comment: str | NotGiven = NOT_GIVEN,
        proxied: bool | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        ttl: Union[float, Literal[1]] | NotGiven = NOT_GIVEN,
        data: dns_record_create_params.DNSRecordsCaaRecordData
        | dns_record_create_params.DNSRecordsCertRecordData
        | dns_record_create_params.DNSRecordsDnskeyRecordData
        | dns_record_create_params.DNSRecordsDsRecordData
        | dns_record_create_params.DNSRecordsHTTPsRecordData
        | dns_record_create_params.DNSRecordsLocRecordData
        | dns_record_create_params.DNSRecordsNaptrRecordData
        | dns_record_create_params.DNSRecordsSmimeaRecordData
        | dns_record_create_params.DNSRecordsSrvRecordData
        | dns_record_create_params.DNSRecordsSshfpRecordData
        | dns_record_create_params.DNSRecordsUriRecordData
        | NotGiven = NOT_GIVEN,
        priority: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DNSRecordCreateResponse:
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return cast(
            DNSRecordCreateResponse,
            await self._post(
                f"/zones/{zone_id}/dns_records",
                body=maybe_transform(
                    {
                        "content": content,
                        "name": name,
                        "type": type,
                        "comment": comment,
                        "proxied": proxied,
                        "tags": tags,
                        "ttl": ttl,
                        "data": data,
                        "priority": priority,
                    },
                    dns_record_create_params.DNSRecordCreateParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[DNSRecordCreateResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    @overload
    async def update(
        self,
        dns_record_id: str,
        *,
        zone_id: str,
        content: str,
        name: str,
        type: Literal["A"],
        comment: str | NotGiven = NOT_GIVEN,
        proxied: bool | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        ttl: Union[float, Literal[1]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DNSRecordUpdateResponse:
        """Overwrite an existing DNS record.

        Notes:

        - A/AAAA records cannot exist on the same name as CNAME records.
        - NS records cannot exist on the same name as any other record type.
        - Domain names are always represented in Punycode, even if Unicode characters
          were used when creating the record.

        Args:
          zone_id: Identifier

          dns_record_id: Identifier

          content: A valid IPv4 address.

          name: DNS record name (or @ for the zone apex) in Punycode.

          type: Record type.

          comment: Comments or notes about the DNS record. This field has no effect on DNS
              responses.

          proxied: Whether the record is receiving the performance and security benefits of
              Cloudflare.

          tags: Custom tags for the DNS record. This field has no effect on DNS responses.

          ttl: Time To Live (TTL) of the DNS record in seconds. Setting to 1 means 'automatic'.
              Value must be between 60 and 86400, with the minimum reduced to 30 for
              Enterprise zones.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def update(
        self,
        dns_record_id: str,
        *,
        zone_id: str,
        content: str,
        name: str,
        type: Literal["AAAA"],
        comment: str | NotGiven = NOT_GIVEN,
        proxied: bool | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        ttl: Union[float, Literal[1]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DNSRecordUpdateResponse:
        """Overwrite an existing DNS record.

        Notes:

        - A/AAAA records cannot exist on the same name as CNAME records.
        - NS records cannot exist on the same name as any other record type.
        - Domain names are always represented in Punycode, even if Unicode characters
          were used when creating the record.

        Args:
          zone_id: Identifier

          dns_record_id: Identifier

          content: A valid IPv6 address.

          name: DNS record name (or @ for the zone apex) in Punycode.

          type: Record type.

          comment: Comments or notes about the DNS record. This field has no effect on DNS
              responses.

          proxied: Whether the record is receiving the performance and security benefits of
              Cloudflare.

          tags: Custom tags for the DNS record. This field has no effect on DNS responses.

          ttl: Time To Live (TTL) of the DNS record in seconds. Setting to 1 means 'automatic'.
              Value must be between 60 and 86400, with the minimum reduced to 30 for
              Enterprise zones.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def update(
        self,
        dns_record_id: str,
        *,
        zone_id: str,
        data: dns_record_update_params.DNSRecordsCaaRecordData,
        name: str,
        type: Literal["CAA"],
        comment: str | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        ttl: Union[float, Literal[1]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DNSRecordUpdateResponse:
        """Overwrite an existing DNS record.

        Notes:

        - A/AAAA records cannot exist on the same name as CNAME records.
        - NS records cannot exist on the same name as any other record type.
        - Domain names are always represented in Punycode, even if Unicode characters
          were used when creating the record.

        Args:
          zone_id: Identifier

          dns_record_id: Identifier

          data: Components of a CAA record.

          name: DNS record name (or @ for the zone apex) in Punycode.

          type: Record type.

          comment: Comments or notes about the DNS record. This field has no effect on DNS
              responses.

          tags: Custom tags for the DNS record. This field has no effect on DNS responses.

          ttl: Time To Live (TTL) of the DNS record in seconds. Setting to 1 means 'automatic'.
              Value must be between 60 and 86400, with the minimum reduced to 30 for
              Enterprise zones.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def update(
        self,
        dns_record_id: str,
        *,
        zone_id: str,
        data: dns_record_update_params.DNSRecordsCertRecordData,
        name: str,
        type: Literal["CERT"],
        comment: str | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        ttl: Union[float, Literal[1]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DNSRecordUpdateResponse:
        """Overwrite an existing DNS record.

        Notes:

        - A/AAAA records cannot exist on the same name as CNAME records.
        - NS records cannot exist on the same name as any other record type.
        - Domain names are always represented in Punycode, even if Unicode characters
          were used when creating the record.

        Args:
          zone_id: Identifier

          dns_record_id: Identifier

          data: Components of a CERT record.

          name: DNS record name (or @ for the zone apex) in Punycode.

          type: Record type.

          comment: Comments or notes about the DNS record. This field has no effect on DNS
              responses.

          tags: Custom tags for the DNS record. This field has no effect on DNS responses.

          ttl: Time To Live (TTL) of the DNS record in seconds. Setting to 1 means 'automatic'.
              Value must be between 60 and 86400, with the minimum reduced to 30 for
              Enterprise zones.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def update(
        self,
        dns_record_id: str,
        *,
        zone_id: str,
        content: object,
        name: str,
        type: Literal["CNAME"],
        comment: str | NotGiven = NOT_GIVEN,
        proxied: bool | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        ttl: Union[float, Literal[1]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DNSRecordUpdateResponse:
        """Overwrite an existing DNS record.

        Notes:

        - A/AAAA records cannot exist on the same name as CNAME records.
        - NS records cannot exist on the same name as any other record type.
        - Domain names are always represented in Punycode, even if Unicode characters
          were used when creating the record.

        Args:
          zone_id: Identifier

          dns_record_id: Identifier

          content: A valid hostname. Must not match the record's name.

          name: DNS record name (or @ for the zone apex) in Punycode.

          type: Record type.

          comment: Comments or notes about the DNS record. This field has no effect on DNS
              responses.

          proxied: Whether the record is receiving the performance and security benefits of
              Cloudflare.

          tags: Custom tags for the DNS record. This field has no effect on DNS responses.

          ttl: Time To Live (TTL) of the DNS record in seconds. Setting to 1 means 'automatic'.
              Value must be between 60 and 86400, with the minimum reduced to 30 for
              Enterprise zones.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def update(
        self,
        dns_record_id: str,
        *,
        zone_id: str,
        data: dns_record_update_params.DNSRecordsDnskeyRecordData,
        name: str,
        type: Literal["DNSKEY"],
        comment: str | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        ttl: Union[float, Literal[1]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DNSRecordUpdateResponse:
        """Overwrite an existing DNS record.

        Notes:

        - A/AAAA records cannot exist on the same name as CNAME records.
        - NS records cannot exist on the same name as any other record type.
        - Domain names are always represented in Punycode, even if Unicode characters
          were used when creating the record.

        Args:
          zone_id: Identifier

          dns_record_id: Identifier

          data: Components of a DNSKEY record.

          name: DNS record name (or @ for the zone apex) in Punycode.

          type: Record type.

          comment: Comments or notes about the DNS record. This field has no effect on DNS
              responses.

          tags: Custom tags for the DNS record. This field has no effect on DNS responses.

          ttl: Time To Live (TTL) of the DNS record in seconds. Setting to 1 means 'automatic'.
              Value must be between 60 and 86400, with the minimum reduced to 30 for
              Enterprise zones.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def update(
        self,
        dns_record_id: str,
        *,
        zone_id: str,
        data: dns_record_update_params.DNSRecordsDsRecordData,
        name: str,
        type: Literal["DS"],
        comment: str | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        ttl: Union[float, Literal[1]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DNSRecordUpdateResponse:
        """Overwrite an existing DNS record.

        Notes:

        - A/AAAA records cannot exist on the same name as CNAME records.
        - NS records cannot exist on the same name as any other record type.
        - Domain names are always represented in Punycode, even if Unicode characters
          were used when creating the record.

        Args:
          zone_id: Identifier

          dns_record_id: Identifier

          data: Components of a DS record.

          name: DNS record name (or @ for the zone apex) in Punycode.

          type: Record type.

          comment: Comments or notes about the DNS record. This field has no effect on DNS
              responses.

          tags: Custom tags for the DNS record. This field has no effect on DNS responses.

          ttl: Time To Live (TTL) of the DNS record in seconds. Setting to 1 means 'automatic'.
              Value must be between 60 and 86400, with the minimum reduced to 30 for
              Enterprise zones.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def update(
        self,
        dns_record_id: str,
        *,
        zone_id: str,
        data: dns_record_update_params.DNSRecordsHTTPsRecordData,
        name: str,
        type: Literal["HTTPS"],
        comment: str | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        ttl: Union[float, Literal[1]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DNSRecordUpdateResponse:
        """Overwrite an existing DNS record.

        Notes:

        - A/AAAA records cannot exist on the same name as CNAME records.
        - NS records cannot exist on the same name as any other record type.
        - Domain names are always represented in Punycode, even if Unicode characters
          were used when creating the record.

        Args:
          zone_id: Identifier

          dns_record_id: Identifier

          data: Components of a HTTPS record.

          name: DNS record name (or @ for the zone apex) in Punycode.

          type: Record type.

          comment: Comments or notes about the DNS record. This field has no effect on DNS
              responses.

          tags: Custom tags for the DNS record. This field has no effect on DNS responses.

          ttl: Time To Live (TTL) of the DNS record in seconds. Setting to 1 means 'automatic'.
              Value must be between 60 and 86400, with the minimum reduced to 30 for
              Enterprise zones.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def update(
        self,
        dns_record_id: str,
        *,
        zone_id: str,
        data: dns_record_update_params.DNSRecordsLocRecordData,
        name: str,
        type: Literal["LOC"],
        comment: str | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        ttl: Union[float, Literal[1]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DNSRecordUpdateResponse:
        """Overwrite an existing DNS record.

        Notes:

        - A/AAAA records cannot exist on the same name as CNAME records.
        - NS records cannot exist on the same name as any other record type.
        - Domain names are always represented in Punycode, even if Unicode characters
          were used when creating the record.

        Args:
          zone_id: Identifier

          dns_record_id: Identifier

          data: Components of a LOC record.

          name: DNS record name (or @ for the zone apex) in Punycode.

          type: Record type.

          comment: Comments or notes about the DNS record. This field has no effect on DNS
              responses.

          tags: Custom tags for the DNS record. This field has no effect on DNS responses.

          ttl: Time To Live (TTL) of the DNS record in seconds. Setting to 1 means 'automatic'.
              Value must be between 60 and 86400, with the minimum reduced to 30 for
              Enterprise zones.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def update(
        self,
        dns_record_id: str,
        *,
        zone_id: str,
        content: str,
        name: str,
        priority: float,
        type: Literal["MX"],
        comment: str | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        ttl: Union[float, Literal[1]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DNSRecordUpdateResponse:
        """Overwrite an existing DNS record.

        Notes:

        - A/AAAA records cannot exist on the same name as CNAME records.
        - NS records cannot exist on the same name as any other record type.
        - Domain names are always represented in Punycode, even if Unicode characters
          were used when creating the record.

        Args:
          zone_id: Identifier

          dns_record_id: Identifier

          content: A valid mail server hostname.

          name: DNS record name (or @ for the zone apex) in Punycode.

          priority: Required for MX, SRV and URI records; unused by other record types. Records with
              lower priorities are preferred.

          type: Record type.

          comment: Comments or notes about the DNS record. This field has no effect on DNS
              responses.

          tags: Custom tags for the DNS record. This field has no effect on DNS responses.

          ttl: Time To Live (TTL) of the DNS record in seconds. Setting to 1 means 'automatic'.
              Value must be between 60 and 86400, with the minimum reduced to 30 for
              Enterprise zones.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def update(
        self,
        dns_record_id: str,
        *,
        zone_id: str,
        data: dns_record_update_params.DNSRecordsNaptrRecordData,
        name: str,
        type: Literal["NAPTR"],
        comment: str | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        ttl: Union[float, Literal[1]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DNSRecordUpdateResponse:
        """Overwrite an existing DNS record.

        Notes:

        - A/AAAA records cannot exist on the same name as CNAME records.
        - NS records cannot exist on the same name as any other record type.
        - Domain names are always represented in Punycode, even if Unicode characters
          were used when creating the record.

        Args:
          zone_id: Identifier

          dns_record_id: Identifier

          data: Components of a NAPTR record.

          name: DNS record name (or @ for the zone apex) in Punycode.

          type: Record type.

          comment: Comments or notes about the DNS record. This field has no effect on DNS
              responses.

          tags: Custom tags for the DNS record. This field has no effect on DNS responses.

          ttl: Time To Live (TTL) of the DNS record in seconds. Setting to 1 means 'automatic'.
              Value must be between 60 and 86400, with the minimum reduced to 30 for
              Enterprise zones.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def update(
        self,
        dns_record_id: str,
        *,
        zone_id: str,
        content: object,
        name: str,
        type: Literal["NS"],
        comment: str | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        ttl: Union[float, Literal[1]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DNSRecordUpdateResponse:
        """Overwrite an existing DNS record.

        Notes:

        - A/AAAA records cannot exist on the same name as CNAME records.
        - NS records cannot exist on the same name as any other record type.
        - Domain names are always represented in Punycode, even if Unicode characters
          were used when creating the record.

        Args:
          zone_id: Identifier

          dns_record_id: Identifier

          content: A valid name server host name.

          name: DNS record name (or @ for the zone apex) in Punycode.

          type: Record type.

          comment: Comments or notes about the DNS record. This field has no effect on DNS
              responses.

          tags: Custom tags for the DNS record. This field has no effect on DNS responses.

          ttl: Time To Live (TTL) of the DNS record in seconds. Setting to 1 means 'automatic'.
              Value must be between 60 and 86400, with the minimum reduced to 30 for
              Enterprise zones.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def update(
        self,
        dns_record_id: str,
        *,
        zone_id: str,
        content: str,
        name: str,
        type: Literal["PTR"],
        comment: str | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        ttl: Union[float, Literal[1]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DNSRecordUpdateResponse:
        """Overwrite an existing DNS record.

        Notes:

        - A/AAAA records cannot exist on the same name as CNAME records.
        - NS records cannot exist on the same name as any other record type.
        - Domain names are always represented in Punycode, even if Unicode characters
          were used when creating the record.

        Args:
          zone_id: Identifier

          dns_record_id: Identifier

          content: Domain name pointing to the address.

          name: DNS record name (or @ for the zone apex) in Punycode.

          type: Record type.

          comment: Comments or notes about the DNS record. This field has no effect on DNS
              responses.

          tags: Custom tags for the DNS record. This field has no effect on DNS responses.

          ttl: Time To Live (TTL) of the DNS record in seconds. Setting to 1 means 'automatic'.
              Value must be between 60 and 86400, with the minimum reduced to 30 for
              Enterprise zones.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def update(
        self,
        dns_record_id: str,
        *,
        zone_id: str,
        data: dns_record_update_params.DNSRecordsSmimeaRecordData,
        name: str,
        type: Literal["SMIMEA"],
        comment: str | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        ttl: Union[float, Literal[1]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DNSRecordUpdateResponse:
        """Overwrite an existing DNS record.

        Notes:

        - A/AAAA records cannot exist on the same name as CNAME records.
        - NS records cannot exist on the same name as any other record type.
        - Domain names are always represented in Punycode, even if Unicode characters
          were used when creating the record.

        Args:
          zone_id: Identifier

          dns_record_id: Identifier

          data: Components of a SMIMEA record.

          name: DNS record name (or @ for the zone apex) in Punycode.

          type: Record type.

          comment: Comments or notes about the DNS record. This field has no effect on DNS
              responses.

          tags: Custom tags for the DNS record. This field has no effect on DNS responses.

          ttl: Time To Live (TTL) of the DNS record in seconds. Setting to 1 means 'automatic'.
              Value must be between 60 and 86400, with the minimum reduced to 30 for
              Enterprise zones.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def update(
        self,
        dns_record_id: str,
        *,
        zone_id: str,
        data: dns_record_update_params.DNSRecordsSrvRecordData,
        name: str,
        type: Literal["SRV"],
        comment: str | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        ttl: Union[float, Literal[1]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DNSRecordUpdateResponse:
        """Overwrite an existing DNS record.

        Notes:

        - A/AAAA records cannot exist on the same name as CNAME records.
        - NS records cannot exist on the same name as any other record type.
        - Domain names are always represented in Punycode, even if Unicode characters
          were used when creating the record.

        Args:
          zone_id: Identifier

          dns_record_id: Identifier

          data: Components of a SRV record.

          name: DNS record name (or @ for the zone apex) in Punycode. For SRV records, the first
              label is normally a service and the second a protocol name, each starting with
              an underscore.

          type: Record type.

          comment: Comments or notes about the DNS record. This field has no effect on DNS
              responses.

          tags: Custom tags for the DNS record. This field has no effect on DNS responses.

          ttl: Time To Live (TTL) of the DNS record in seconds. Setting to 1 means 'automatic'.
              Value must be between 60 and 86400, with the minimum reduced to 30 for
              Enterprise zones.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def update(
        self,
        dns_record_id: str,
        *,
        zone_id: str,
        data: dns_record_update_params.DNSRecordsSshfpRecordData,
        name: str,
        type: Literal["SSHFP"],
        comment: str | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        ttl: Union[float, Literal[1]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DNSRecordUpdateResponse:
        """Overwrite an existing DNS record.

        Notes:

        - A/AAAA records cannot exist on the same name as CNAME records.
        - NS records cannot exist on the same name as any other record type.
        - Domain names are always represented in Punycode, even if Unicode characters
          were used when creating the record.

        Args:
          zone_id: Identifier

          dns_record_id: Identifier

          data: Components of a SSHFP record.

          name: DNS record name (or @ for the zone apex) in Punycode.

          type: Record type.

          comment: Comments or notes about the DNS record. This field has no effect on DNS
              responses.

          tags: Custom tags for the DNS record. This field has no effect on DNS responses.

          ttl: Time To Live (TTL) of the DNS record in seconds. Setting to 1 means 'automatic'.
              Value must be between 60 and 86400, with the minimum reduced to 30 for
              Enterprise zones.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def update(
        self,
        dns_record_id: str,
        *,
        zone_id: str,
        data: dns_record_update_params.DNSRecordsSvcbRecordData,
        name: str,
        type: Literal["SVCB"],
        comment: str | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        ttl: Union[float, Literal[1]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DNSRecordUpdateResponse:
        """Overwrite an existing DNS record.

        Notes:

        - A/AAAA records cannot exist on the same name as CNAME records.
        - NS records cannot exist on the same name as any other record type.
        - Domain names are always represented in Punycode, even if Unicode characters
          were used when creating the record.

        Args:
          zone_id: Identifier

          dns_record_id: Identifier

          data: Components of a SVCB record.

          name: DNS record name (or @ for the zone apex) in Punycode.

          type: Record type.

          comment: Comments or notes about the DNS record. This field has no effect on DNS
              responses.

          tags: Custom tags for the DNS record. This field has no effect on DNS responses.

          ttl: Time To Live (TTL) of the DNS record in seconds. Setting to 1 means 'automatic'.
              Value must be between 60 and 86400, with the minimum reduced to 30 for
              Enterprise zones.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def update(
        self,
        dns_record_id: str,
        *,
        zone_id: str,
        data: dns_record_update_params.DNSRecordsTlsaRecordData,
        name: str,
        type: Literal["TLSA"],
        comment: str | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        ttl: Union[float, Literal[1]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DNSRecordUpdateResponse:
        """Overwrite an existing DNS record.

        Notes:

        - A/AAAA records cannot exist on the same name as CNAME records.
        - NS records cannot exist on the same name as any other record type.
        - Domain names are always represented in Punycode, even if Unicode characters
          were used when creating the record.

        Args:
          zone_id: Identifier

          dns_record_id: Identifier

          data: Components of a TLSA record.

          name: DNS record name (or @ for the zone apex) in Punycode.

          type: Record type.

          comment: Comments or notes about the DNS record. This field has no effect on DNS
              responses.

          tags: Custom tags for the DNS record. This field has no effect on DNS responses.

          ttl: Time To Live (TTL) of the DNS record in seconds. Setting to 1 means 'automatic'.
              Value must be between 60 and 86400, with the minimum reduced to 30 for
              Enterprise zones.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def update(
        self,
        dns_record_id: str,
        *,
        zone_id: str,
        content: str,
        name: str,
        type: Literal["TXT"],
        comment: str | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        ttl: Union[float, Literal[1]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DNSRecordUpdateResponse:
        """Overwrite an existing DNS record.

        Notes:

        - A/AAAA records cannot exist on the same name as CNAME records.
        - NS records cannot exist on the same name as any other record type.
        - Domain names are always represented in Punycode, even if Unicode characters
          were used when creating the record.

        Args:
          zone_id: Identifier

          dns_record_id: Identifier

          content: Text content for the record.

          name: DNS record name (or @ for the zone apex) in Punycode.

          type: Record type.

          comment: Comments or notes about the DNS record. This field has no effect on DNS
              responses.

          tags: Custom tags for the DNS record. This field has no effect on DNS responses.

          ttl: Time To Live (TTL) of the DNS record in seconds. Setting to 1 means 'automatic'.
              Value must be between 60 and 86400, with the minimum reduced to 30 for
              Enterprise zones.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def update(
        self,
        dns_record_id: str,
        *,
        zone_id: str,
        data: dns_record_update_params.DNSRecordsUriRecordData,
        name: str,
        priority: float,
        type: Literal["URI"],
        comment: str | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        ttl: Union[float, Literal[1]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DNSRecordUpdateResponse:
        """Overwrite an existing DNS record.

        Notes:

        - A/AAAA records cannot exist on the same name as CNAME records.
        - NS records cannot exist on the same name as any other record type.
        - Domain names are always represented in Punycode, even if Unicode characters
          were used when creating the record.

        Args:
          zone_id: Identifier

          dns_record_id: Identifier

          data: Components of a URI record.

          name: DNS record name (or @ for the zone apex) in Punycode.

          priority: Required for MX, SRV and URI records; unused by other record types. Records with
              lower priorities are preferred.

          type: Record type.

          comment: Comments or notes about the DNS record. This field has no effect on DNS
              responses.

          tags: Custom tags for the DNS record. This field has no effect on DNS responses.

          ttl: Time To Live (TTL) of the DNS record in seconds. Setting to 1 means 'automatic'.
              Value must be between 60 and 86400, with the minimum reduced to 30 for
              Enterprise zones.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(
        ["zone_id", "content", "name", "type"],
        ["zone_id", "content", "name", "type"],
        ["zone_id", "data", "name", "type"],
        ["zone_id", "data", "name", "type"],
        ["zone_id", "content", "name", "type"],
        ["zone_id", "data", "name", "type"],
        ["zone_id", "data", "name", "type"],
        ["zone_id", "data", "name", "type"],
        ["zone_id", "data", "name", "type"],
        ["zone_id", "content", "name", "priority", "type"],
        ["zone_id", "data", "name", "type"],
        ["zone_id", "content", "name", "type"],
        ["zone_id", "content", "name", "type"],
        ["zone_id", "data", "name", "type"],
        ["zone_id", "data", "name", "type"],
        ["zone_id", "data", "name", "type"],
        ["zone_id", "data", "name", "type"],
        ["zone_id", "data", "name", "type"],
        ["zone_id", "content", "name", "type"],
        ["zone_id", "data", "name", "priority", "type"],
    )
    async def update(
        self,
        dns_record_id: str,
        *,
        zone_id: str,
        content: str | object | NotGiven = NOT_GIVEN,
        name: str,
        type: Literal["A"]
        | Literal["AAAA"]
        | Literal["CAA"]
        | Literal["CERT"]
        | Literal["CNAME"]
        | Literal["DNSKEY"]
        | Literal["DS"]
        | Literal["HTTPS"]
        | Literal["LOC"]
        | Literal["MX"]
        | Literal["NAPTR"]
        | Literal["NS"]
        | Literal["PTR"]
        | Literal["SMIMEA"]
        | Literal["SRV"]
        | Literal["SSHFP"]
        | Literal["SVCB"]
        | Literal["TLSA"]
        | Literal["TXT"]
        | Literal["URI"],
        comment: str | NotGiven = NOT_GIVEN,
        proxied: bool | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        ttl: Union[float, Literal[1]] | NotGiven = NOT_GIVEN,
        data: dns_record_update_params.DNSRecordsCaaRecordData
        | dns_record_update_params.DNSRecordsCertRecordData
        | dns_record_update_params.DNSRecordsDnskeyRecordData
        | dns_record_update_params.DNSRecordsDsRecordData
        | dns_record_update_params.DNSRecordsHTTPsRecordData
        | dns_record_update_params.DNSRecordsLocRecordData
        | dns_record_update_params.DNSRecordsNaptrRecordData
        | dns_record_update_params.DNSRecordsSmimeaRecordData
        | dns_record_update_params.DNSRecordsSrvRecordData
        | dns_record_update_params.DNSRecordsSshfpRecordData
        | dns_record_update_params.DNSRecordsUriRecordData
        | NotGiven = NOT_GIVEN,
        priority: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DNSRecordUpdateResponse:
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not dns_record_id:
            raise ValueError(f"Expected a non-empty value for `dns_record_id` but received {dns_record_id!r}")
        return cast(
            DNSRecordUpdateResponse,
            await self._put(
                f"/zones/{zone_id}/dns_records/{dns_record_id}",
                body=maybe_transform(
                    {
                        "content": content,
                        "name": name,
                        "type": type,
                        "comment": comment,
                        "proxied": proxied,
                        "tags": tags,
                        "ttl": ttl,
                        "data": data,
                        "priority": priority,
                    },
                    dns_record_update_params.DNSRecordUpdateParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[DNSRecordUpdateResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def list(
        self,
        zone_id: str,
        *,
        comment: dns_record_list_params.Comment | NotGiven = NOT_GIVEN,
        content: str | NotGiven = NOT_GIVEN,
        direction: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
        match: Literal["any", "all"] | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        order: Literal["type", "name", "content", "ttl", "proxied"] | NotGiven = NOT_GIVEN,
        page: float | NotGiven = NOT_GIVEN,
        per_page: float | NotGiven = NOT_GIVEN,
        proxied: bool | NotGiven = NOT_GIVEN,
        search: str | NotGiven = NOT_GIVEN,
        tag: dns_record_list_params.Tag | NotGiven = NOT_GIVEN,
        tag_match: Literal["any", "all"] | NotGiven = NOT_GIVEN,
        type: Literal[
            "A",
            "AAAA",
            "CAA",
            "CERT",
            "CNAME",
            "DNSKEY",
            "DS",
            "HTTPS",
            "LOC",
            "MX",
            "NAPTR",
            "NS",
            "PTR",
            "SMIMEA",
            "SRV",
            "SSHFP",
            "SVCB",
            "TLSA",
            "TXT",
            "URI",
        ]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[DNSRecordListResponse]:
        """
        List, search, sort, and filter a zones' DNS records.

        Args:
          zone_id: Identifier

          content: DNS record content.

          direction: Direction to order DNS records in.

          match: Whether to match all search requirements or at least one (any). If set to `all`,
              acts like a logical AND between filters. If set to `any`, acts like a logical OR
              instead. Note that the interaction between tag filters is controlled by the
              `tag-match` parameter instead.

          name: DNS record name (or @ for the zone apex) in Punycode.

          order: Field to order DNS records by.

          page: Page number of paginated results.

          per_page: Number of DNS records per page.

          proxied: Whether the record is receiving the performance and security benefits of
              Cloudflare.

          search: Allows searching in multiple properties of a DNS record simultaneously. This
              parameter is intended for human users, not automation. Its exact behavior is
              intentionally left unspecified and is subject to change in the future. This
              parameter works independently of the `match` setting. For automated searches,
              please use the other available parameters.

          tag_match: Whether to match all tag search requirements or at least one (any). If set to
              `all`, acts like a logical AND between tag filters. If set to `any`, acts like a
              logical OR instead. Note that the regular `match` parameter is still used to
              combine the resulting condition with other filters that aren't related to tags.

          type: Record type.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._get(
            f"/zones/{zone_id}/dns_records",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "comment": comment,
                        "content": content,
                        "direction": direction,
                        "match": match,
                        "name": name,
                        "order": order,
                        "page": page,
                        "per_page": per_page,
                        "proxied": proxied,
                        "search": search,
                        "tag": tag,
                        "tag_match": tag_match,
                        "type": type,
                    },
                    dns_record_list_params.DNSRecordListParams,
                ),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[DNSRecordListResponse]], ResultWrapper[DNSRecordListResponse]),
        )

    async def delete(
        self,
        dns_record_id: str,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[DNSRecordDeleteResponse]:
        """
        Delete DNS Record

        Args:
          zone_id: Identifier

          dns_record_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not dns_record_id:
            raise ValueError(f"Expected a non-empty value for `dns_record_id` but received {dns_record_id!r}")
        return await self._delete(
            f"/zones/{zone_id}/dns_records/{dns_record_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[DNSRecordDeleteResponse]], ResultWrapper[DNSRecordDeleteResponse]),
        )

    async def export(
        self,
        zone_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> str:
        """
        You can export your
        [BIND config](https://en.wikipedia.org/wiki/Zone_file "Zone file") through this
        endpoint.

        See
        [the documentation](https://developers.cloudflare.com/dns/manage-dns-records/how-to/import-and-export/ "Import and export records")
        for more information.

        Args:
          zone_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        extra_headers = {"Accept": "text/plain", **(extra_headers or {})}
        return await self._get(
            f"/zones/{zone_id}/dns_records/export",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )

    async def get(
        self,
        dns_record_id: str,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DNSRecordGetResponse:
        """
        DNS Record Details

        Args:
          zone_id: Identifier

          dns_record_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not dns_record_id:
            raise ValueError(f"Expected a non-empty value for `dns_record_id` but received {dns_record_id!r}")
        return cast(
            DNSRecordGetResponse,
            await self._get(
                f"/zones/{zone_id}/dns_records/{dns_record_id}",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[DNSRecordGetResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def import_(
        self,
        zone_id: str,
        *,
        file: str,
        proxied: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DNSRecordImportResponse:
        """
        You can upload your
        [BIND config](https://en.wikipedia.org/wiki/Zone_file "Zone file") through this
        endpoint. It assumes that cURL is called from a location with bind_config.txt
        (valid BIND config) present.

        See
        [the documentation](https://developers.cloudflare.com/dns/manage-dns-records/how-to/import-and-export/ "Import and export records")
        for more information.

        Args:
          zone_id: Identifier

          file: BIND config to import.

              **Tip:** When using cURL, a file can be uploaded using
              `--form 'file=@bind_config.txt'`.

          proxied: Whether or not proxiable records should receive the performance and security
              benefits of Cloudflare.

              The value should be either `true` or `false`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._post(
            f"/zones/{zone_id}/dns_records/import",
            body=maybe_transform(
                {
                    "file": file,
                    "proxied": proxied,
                },
                dns_record_import_params.DNSRecordImportParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[DNSRecordImportResponse], ResultWrapper[DNSRecordImportResponse]),
        )

    async def scan(
        self,
        zone_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DNSRecordScanResponse:
        """
        Scan for common DNS records on your domain and automatically add them to your
        zone. Useful if you haven't updated your nameservers yet.

        Args:
          zone_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._post(
            f"/zones/{zone_id}/dns_records/scan",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[DNSRecordScanResponse], ResultWrapper[DNSRecordScanResponse]),
        )


class DNSRecordsWithRawResponse:
    def __init__(self, dns_records: DNSRecords) -> None:
        self._dns_records = dns_records

        self.create = to_raw_response_wrapper(
            dns_records.create,
        )
        self.update = to_raw_response_wrapper(
            dns_records.update,
        )
        self.list = to_raw_response_wrapper(
            dns_records.list,
        )
        self.delete = to_raw_response_wrapper(
            dns_records.delete,
        )
        self.export = to_raw_response_wrapper(
            dns_records.export,
        )
        self.get = to_raw_response_wrapper(
            dns_records.get,
        )
        self.import_ = to_raw_response_wrapper(
            dns_records.import_,
        )
        self.scan = to_raw_response_wrapper(
            dns_records.scan,
        )


class AsyncDNSRecordsWithRawResponse:
    def __init__(self, dns_records: AsyncDNSRecords) -> None:
        self._dns_records = dns_records

        self.create = async_to_raw_response_wrapper(
            dns_records.create,
        )
        self.update = async_to_raw_response_wrapper(
            dns_records.update,
        )
        self.list = async_to_raw_response_wrapper(
            dns_records.list,
        )
        self.delete = async_to_raw_response_wrapper(
            dns_records.delete,
        )
        self.export = async_to_raw_response_wrapper(
            dns_records.export,
        )
        self.get = async_to_raw_response_wrapper(
            dns_records.get,
        )
        self.import_ = async_to_raw_response_wrapper(
            dns_records.import_,
        )
        self.scan = async_to_raw_response_wrapper(
            dns_records.scan,
        )


class DNSRecordsWithStreamingResponse:
    def __init__(self, dns_records: DNSRecords) -> None:
        self._dns_records = dns_records

        self.create = to_streamed_response_wrapper(
            dns_records.create,
        )
        self.update = to_streamed_response_wrapper(
            dns_records.update,
        )
        self.list = to_streamed_response_wrapper(
            dns_records.list,
        )
        self.delete = to_streamed_response_wrapper(
            dns_records.delete,
        )
        self.export = to_streamed_response_wrapper(
            dns_records.export,
        )
        self.get = to_streamed_response_wrapper(
            dns_records.get,
        )
        self.import_ = to_streamed_response_wrapper(
            dns_records.import_,
        )
        self.scan = to_streamed_response_wrapper(
            dns_records.scan,
        )


class AsyncDNSRecordsWithStreamingResponse:
    def __init__(self, dns_records: AsyncDNSRecords) -> None:
        self._dns_records = dns_records

        self.create = async_to_streamed_response_wrapper(
            dns_records.create,
        )
        self.update = async_to_streamed_response_wrapper(
            dns_records.update,
        )
        self.list = async_to_streamed_response_wrapper(
            dns_records.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            dns_records.delete,
        )
        self.export = async_to_streamed_response_wrapper(
            dns_records.export,
        )
        self.get = async_to_streamed_response_wrapper(
            dns_records.get,
        )
        self.import_ = async_to_streamed_response_wrapper(
            dns_records.import_,
        )
        self.scan = async_to_streamed_response_wrapper(
            dns_records.scan,
        )
