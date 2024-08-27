# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, List, Type, Optional, cast, overload
from typing_extensions import Literal

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    required_args,
    maybe_transform,
    async_maybe_transform,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._wrappers import ResultWrapper
from ...types.dns import (
    record_edit_params,
    record_list_params,
    record_scan_params,
    record_create_params,
    record_import_params,
    record_update_params,
)
from ...pagination import SyncV4PagePaginationArray, AsyncV4PagePaginationArray
from ..._base_client import AsyncPaginator, make_request_options
from ...types.dns.record import Record
from ...types.dns.ttl_param import TTLParam
from ...types.dns.record_tags import RecordTags
from ...types.shared.sort_direction import SortDirection
from ...types.dns.record_scan_response import RecordScanResponse
from ...types.dns.record_delete_response import RecordDeleteResponse
from ...types.dns.record_import_response import RecordImportResponse

__all__ = ["RecordsResource", "AsyncRecordsResource"]


class RecordsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RecordsResourceWithRawResponse:
        return RecordsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RecordsResourceWithStreamingResponse:
        return RecordsResourceWithStreamingResponse(self)

    @overload
    def create(
        self,
        *,
        zone_id: str,
        content: str,
        name: str,
        type: Literal["A"],
        id: str | NotGiven = NOT_GIVEN,
        comment: str | NotGiven = NOT_GIVEN,
        proxied: bool | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Record]:
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

          id: Identifier

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
        *,
        zone_id: str,
        content: str,
        name: str,
        type: Literal["AAAA"],
        id: str | NotGiven = NOT_GIVEN,
        comment: str | NotGiven = NOT_GIVEN,
        proxied: bool | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Record]:
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

          id: Identifier

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
        *,
        zone_id: str,
        data: record_create_params.CAARecordData,
        name: str,
        type: Literal["CAA"],
        id: str | NotGiven = NOT_GIVEN,
        comment: str | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Record]:
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

          id: Identifier

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
        *,
        zone_id: str,
        data: record_create_params.CERTRecordData,
        name: str,
        type: Literal["CERT"],
        id: str | NotGiven = NOT_GIVEN,
        comment: str | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Record]:
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

          id: Identifier

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
        *,
        zone_id: str,
        content: str,
        name: str,
        type: Literal["CNAME"],
        id: str | NotGiven = NOT_GIVEN,
        comment: str | NotGiven = NOT_GIVEN,
        proxied: bool | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Record]:
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

          id: Identifier

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
        *,
        zone_id: str,
        data: record_create_params.DNSKEYRecordData,
        name: str,
        type: Literal["DNSKEY"],
        id: str | NotGiven = NOT_GIVEN,
        comment: str | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Record]:
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

          id: Identifier

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
        *,
        zone_id: str,
        data: record_create_params.DSRecordData,
        name: str,
        type: Literal["DS"],
        id: str | NotGiven = NOT_GIVEN,
        comment: str | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Record]:
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

          id: Identifier

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
        *,
        zone_id: str,
        data: record_create_params.HTTPSRecordData,
        name: str,
        type: Literal["HTTPS"],
        id: str | NotGiven = NOT_GIVEN,
        comment: str | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Record]:
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

          id: Identifier

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
        *,
        zone_id: str,
        data: record_create_params.LOCRecordData,
        name: str,
        type: Literal["LOC"],
        id: str | NotGiven = NOT_GIVEN,
        comment: str | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Record]:
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

          id: Identifier

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
        *,
        zone_id: str,
        content: str,
        name: str,
        priority: float,
        type: Literal["MX"],
        id: str | NotGiven = NOT_GIVEN,
        comment: str | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Record]:
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

          id: Identifier

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
        *,
        zone_id: str,
        data: record_create_params.NAPTRRecordData,
        name: str,
        type: Literal["NAPTR"],
        id: str | NotGiven = NOT_GIVEN,
        comment: str | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Record]:
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

          id: Identifier

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
        *,
        zone_id: str,
        content: str,
        name: str,
        type: Literal["NS"],
        id: str | NotGiven = NOT_GIVEN,
        comment: str | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Record]:
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

          id: Identifier

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
        *,
        zone_id: str,
        content: str,
        name: str,
        type: Literal["OPENPGPKEY"],
        id: str | NotGiven = NOT_GIVEN,
        comment: str | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Record]:
        """
        Create a new DNS record for a zone.

        Notes:

        - A/AAAA records cannot exist on the same name as CNAME records.
        - NS records cannot exist on the same name as any other record type.
        - Domain names are always represented in Punycode, even if Unicode characters
          were used when creating the record.

        Args:
          zone_id: Identifier

          content: A single Base64-encoded OpenPGP Transferable Public Key (RFC 4880 Section 11.1)

          name: DNS record name (or @ for the zone apex) in Punycode.

          type: Record type.

          id: Identifier

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
        *,
        zone_id: str,
        content: str,
        name: str,
        type: Literal["PTR"],
        id: str | NotGiven = NOT_GIVEN,
        comment: str | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Record]:
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

          id: Identifier

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
        *,
        zone_id: str,
        data: record_create_params.SMIMEARecordData,
        name: str,
        type: Literal["SMIMEA"],
        id: str | NotGiven = NOT_GIVEN,
        comment: str | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Record]:
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

          id: Identifier

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
        *,
        zone_id: str,
        data: record_create_params.SRVRecordData,
        name: str,
        type: Literal["SRV"],
        id: str | NotGiven = NOT_GIVEN,
        comment: str | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Record]:
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

          id: Identifier

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
        *,
        zone_id: str,
        data: record_create_params.SSHFPRecordData,
        name: str,
        type: Literal["SSHFP"],
        id: str | NotGiven = NOT_GIVEN,
        comment: str | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Record]:
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

          id: Identifier

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
        *,
        zone_id: str,
        data: record_create_params.SVCBRecordData,
        name: str,
        type: Literal["SVCB"],
        id: str | NotGiven = NOT_GIVEN,
        comment: str | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Record]:
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

          id: Identifier

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
        *,
        zone_id: str,
        data: record_create_params.TLSARecordData,
        name: str,
        type: Literal["TLSA"],
        id: str | NotGiven = NOT_GIVEN,
        comment: str | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Record]:
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

          id: Identifier

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
        *,
        zone_id: str,
        content: str,
        name: str,
        type: Literal["TXT"],
        id: str | NotGiven = NOT_GIVEN,
        comment: str | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Record]:
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

          id: Identifier

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
        *,
        zone_id: str,
        data: record_create_params.URIRecordData,
        name: str,
        priority: float,
        type: Literal["URI"],
        id: str | NotGiven = NOT_GIVEN,
        comment: str | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Record]:
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

          id: Identifier

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
        ["zone_id", "data", "name", "type"],
        ["zone_id", "content", "name", "priority", "type"],
        ["zone_id", "data", "name", "priority", "type"],
    )
    def create(
        self,
        *,
        zone_id: str,
        content: str | NotGiven = NOT_GIVEN,
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
        | Literal["OPENPGPKEY"]
        | Literal["PTR"]
        | Literal["SMIMEA"]
        | Literal["SRV"]
        | Literal["SSHFP"]
        | Literal["SVCB"]
        | Literal["TLSA"]
        | Literal["TXT"]
        | Literal["URI"],
        id: str | NotGiven = NOT_GIVEN,
        comment: str | NotGiven = NOT_GIVEN,
        proxied: bool | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        data: record_create_params.CAARecordData
        | record_create_params.CERTRecordData
        | record_create_params.DNSKEYRecordData
        | record_create_params.DSRecordData
        | record_create_params.HTTPSRecordData
        | record_create_params.LOCRecordData
        | record_create_params.NAPTRRecordData
        | record_create_params.SMIMEARecordData
        | record_create_params.SRVRecordData
        | record_create_params.SSHFPRecordData
        | record_create_params.URIRecordData
        | NotGiven = NOT_GIVEN,
        priority: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Record]:
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return cast(
            Optional[Record],
            self._post(
                f"/zones/{zone_id}/dns_records",
                body=maybe_transform(
                    {
                        "content": content,
                        "name": name,
                        "type": type,
                        "id": id,
                        "comment": comment,
                        "proxied": proxied,
                        "tags": tags,
                        "ttl": ttl,
                        "data": data,
                        "priority": priority,
                    },
                    record_create_params.RecordCreateParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper[Optional[Record]]._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[Record]
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
        id: str | NotGiven = NOT_GIVEN,
        comment: str | NotGiven = NOT_GIVEN,
        proxied: bool | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Record]:
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

          id: Identifier

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
        id: str | NotGiven = NOT_GIVEN,
        comment: str | NotGiven = NOT_GIVEN,
        proxied: bool | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Record]:
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

          id: Identifier

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
        data: record_update_params.CAARecordData,
        name: str,
        type: Literal["CAA"],
        id: str | NotGiven = NOT_GIVEN,
        comment: str | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Record]:
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

          id: Identifier

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
        data: record_update_params.CERTRecordData,
        name: str,
        type: Literal["CERT"],
        id: str | NotGiven = NOT_GIVEN,
        comment: str | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Record]:
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

          id: Identifier

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
        type: Literal["CNAME"],
        id: str | NotGiven = NOT_GIVEN,
        comment: str | NotGiven = NOT_GIVEN,
        proxied: bool | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Record]:
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

          id: Identifier

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
        data: record_update_params.DNSKEYRecordData,
        name: str,
        type: Literal["DNSKEY"],
        id: str | NotGiven = NOT_GIVEN,
        comment: str | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Record]:
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

          id: Identifier

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
        data: record_update_params.DSRecordData,
        name: str,
        type: Literal["DS"],
        id: str | NotGiven = NOT_GIVEN,
        comment: str | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Record]:
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

          id: Identifier

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
        data: record_update_params.HTTPSRecordData,
        name: str,
        type: Literal["HTTPS"],
        id: str | NotGiven = NOT_GIVEN,
        comment: str | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Record]:
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

          id: Identifier

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
        data: record_update_params.LOCRecordData,
        name: str,
        type: Literal["LOC"],
        id: str | NotGiven = NOT_GIVEN,
        comment: str | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Record]:
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

          id: Identifier

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
        id: str | NotGiven = NOT_GIVEN,
        comment: str | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Record]:
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

          id: Identifier

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
        data: record_update_params.NAPTRRecordData,
        name: str,
        type: Literal["NAPTR"],
        id: str | NotGiven = NOT_GIVEN,
        comment: str | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Record]:
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

          id: Identifier

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
        type: Literal["NS"],
        id: str | NotGiven = NOT_GIVEN,
        comment: str | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Record]:
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

          id: Identifier

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
        type: Literal["OPENPGPKEY"],
        id: str | NotGiven = NOT_GIVEN,
        comment: str | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Record]:
        """Overwrite an existing DNS record.

        Notes:

        - A/AAAA records cannot exist on the same name as CNAME records.
        - NS records cannot exist on the same name as any other record type.
        - Domain names are always represented in Punycode, even if Unicode characters
          were used when creating the record.

        Args:
          zone_id: Identifier

          dns_record_id: Identifier

          content: A single Base64-encoded OpenPGP Transferable Public Key (RFC 4880 Section 11.1)

          name: DNS record name (or @ for the zone apex) in Punycode.

          type: Record type.

          id: Identifier

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
        id: str | NotGiven = NOT_GIVEN,
        comment: str | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Record]:
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

          id: Identifier

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
        data: record_update_params.SMIMEARecordData,
        name: str,
        type: Literal["SMIMEA"],
        id: str | NotGiven = NOT_GIVEN,
        comment: str | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Record]:
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

          id: Identifier

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
        data: record_update_params.SRVRecordData,
        name: str,
        type: Literal["SRV"],
        id: str | NotGiven = NOT_GIVEN,
        comment: str | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Record]:
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

          id: Identifier

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
        data: record_update_params.SSHFPRecordData,
        name: str,
        type: Literal["SSHFP"],
        id: str | NotGiven = NOT_GIVEN,
        comment: str | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Record]:
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

          id: Identifier

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
        data: record_update_params.SVCBRecordData,
        name: str,
        type: Literal["SVCB"],
        id: str | NotGiven = NOT_GIVEN,
        comment: str | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Record]:
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

          id: Identifier

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
        data: record_update_params.TLSARecordData,
        name: str,
        type: Literal["TLSA"],
        id: str | NotGiven = NOT_GIVEN,
        comment: str | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Record]:
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

          id: Identifier

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
        id: str | NotGiven = NOT_GIVEN,
        comment: str | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Record]:
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

          id: Identifier

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
        data: record_update_params.URIRecordData,
        name: str,
        priority: float,
        type: Literal["URI"],
        id: str | NotGiven = NOT_GIVEN,
        comment: str | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Record]:
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

          id: Identifier

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
        ["zone_id", "data", "name", "type"],
        ["zone_id", "content", "name", "priority", "type"],
        ["zone_id", "data", "name", "priority", "type"],
    )
    def update(
        self,
        dns_record_id: str,
        *,
        zone_id: str,
        content: str | NotGiven = NOT_GIVEN,
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
        | Literal["OPENPGPKEY"]
        | Literal["PTR"]
        | Literal["SMIMEA"]
        | Literal["SRV"]
        | Literal["SSHFP"]
        | Literal["SVCB"]
        | Literal["TLSA"]
        | Literal["TXT"]
        | Literal["URI"],
        id: str | NotGiven = NOT_GIVEN,
        comment: str | NotGiven = NOT_GIVEN,
        proxied: bool | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        data: record_update_params.CAARecordData
        | record_update_params.CERTRecordData
        | record_update_params.DNSKEYRecordData
        | record_update_params.DSRecordData
        | record_update_params.HTTPSRecordData
        | record_update_params.LOCRecordData
        | record_update_params.NAPTRRecordData
        | record_update_params.SMIMEARecordData
        | record_update_params.SRVRecordData
        | record_update_params.SSHFPRecordData
        | record_update_params.URIRecordData
        | NotGiven = NOT_GIVEN,
        priority: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Record]:
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not dns_record_id:
            raise ValueError(f"Expected a non-empty value for `dns_record_id` but received {dns_record_id!r}")
        return cast(
            Optional[Record],
            self._put(
                f"/zones/{zone_id}/dns_records/{dns_record_id}",
                body=maybe_transform(
                    {
                        "content": content,
                        "name": name,
                        "type": type,
                        "id": id,
                        "comment": comment,
                        "proxied": proxied,
                        "tags": tags,
                        "ttl": ttl,
                        "data": data,
                        "priority": priority,
                    },
                    record_update_params.RecordUpdateParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper[Optional[Record]]._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[Record]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def list(
        self,
        *,
        zone_id: str,
        comment: record_list_params.Comment | NotGiven = NOT_GIVEN,
        content: str | NotGiven = NOT_GIVEN,
        direction: SortDirection | NotGiven = NOT_GIVEN,
        match: Literal["any", "all"] | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        order: Literal["type", "name", "content", "ttl", "proxied"] | NotGiven = NOT_GIVEN,
        page: float | NotGiven = NOT_GIVEN,
        per_page: float | NotGiven = NOT_GIVEN,
        proxied: bool | NotGiven = NOT_GIVEN,
        search: str | NotGiven = NOT_GIVEN,
        tag: record_list_params.Tag | NotGiven = NOT_GIVEN,
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
            "OPENPGPKEY",
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
    ) -> SyncV4PagePaginationArray[Record]:
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
        return self._get_api_list(
            f"/zones/{zone_id}/dns_records",
            page=SyncV4PagePaginationArray[Record],
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
                    record_list_params.RecordListParams,
                ),
            ),
            model=cast(Any, Record),  # Union types cannot be passed in as arguments in the type system
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
    ) -> Optional[RecordDeleteResponse]:
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
                post_parser=ResultWrapper[Optional[RecordDeleteResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[RecordDeleteResponse]], ResultWrapper[RecordDeleteResponse]),
        )

    @overload
    def edit(
        self,
        dns_record_id: str,
        *,
        zone_id: str,
        content: str,
        name: str,
        type: Literal["A"],
        id: str | NotGiven = NOT_GIVEN,
        comment: str | NotGiven = NOT_GIVEN,
        proxied: bool | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Record]:
        """Update an existing DNS record.

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

          id: Identifier

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
    def edit(
        self,
        dns_record_id: str,
        *,
        zone_id: str,
        content: str,
        name: str,
        type: Literal["AAAA"],
        id: str | NotGiven = NOT_GIVEN,
        comment: str | NotGiven = NOT_GIVEN,
        proxied: bool | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Record]:
        """Update an existing DNS record.

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

          id: Identifier

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
    def edit(
        self,
        dns_record_id: str,
        *,
        zone_id: str,
        data: record_edit_params.CAARecordData,
        name: str,
        type: Literal["CAA"],
        id: str | NotGiven = NOT_GIVEN,
        comment: str | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Record]:
        """Update an existing DNS record.

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

          id: Identifier

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
    def edit(
        self,
        dns_record_id: str,
        *,
        zone_id: str,
        data: record_edit_params.CERTRecordData,
        name: str,
        type: Literal["CERT"],
        id: str | NotGiven = NOT_GIVEN,
        comment: str | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Record]:
        """Update an existing DNS record.

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

          id: Identifier

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
    def edit(
        self,
        dns_record_id: str,
        *,
        zone_id: str,
        content: str,
        name: str,
        type: Literal["CNAME"],
        id: str | NotGiven = NOT_GIVEN,
        comment: str | NotGiven = NOT_GIVEN,
        proxied: bool | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Record]:
        """Update an existing DNS record.

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

          id: Identifier

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
    def edit(
        self,
        dns_record_id: str,
        *,
        zone_id: str,
        data: record_edit_params.DNSKEYRecordData,
        name: str,
        type: Literal["DNSKEY"],
        id: str | NotGiven = NOT_GIVEN,
        comment: str | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Record]:
        """Update an existing DNS record.

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

          id: Identifier

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
    def edit(
        self,
        dns_record_id: str,
        *,
        zone_id: str,
        data: record_edit_params.DSRecordData,
        name: str,
        type: Literal["DS"],
        id: str | NotGiven = NOT_GIVEN,
        comment: str | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Record]:
        """Update an existing DNS record.

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

          id: Identifier

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
    def edit(
        self,
        dns_record_id: str,
        *,
        zone_id: str,
        data: record_edit_params.HTTPSRecordData,
        name: str,
        type: Literal["HTTPS"],
        id: str | NotGiven = NOT_GIVEN,
        comment: str | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Record]:
        """Update an existing DNS record.

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

          id: Identifier

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
    def edit(
        self,
        dns_record_id: str,
        *,
        zone_id: str,
        data: record_edit_params.LOCRecordData,
        name: str,
        type: Literal["LOC"],
        id: str | NotGiven = NOT_GIVEN,
        comment: str | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Record]:
        """Update an existing DNS record.

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

          id: Identifier

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
    def edit(
        self,
        dns_record_id: str,
        *,
        zone_id: str,
        content: str,
        name: str,
        priority: float,
        type: Literal["MX"],
        id: str | NotGiven = NOT_GIVEN,
        comment: str | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Record]:
        """Update an existing DNS record.

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

          id: Identifier

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
    def edit(
        self,
        dns_record_id: str,
        *,
        zone_id: str,
        data: record_edit_params.NAPTRRecordData,
        name: str,
        type: Literal["NAPTR"],
        id: str | NotGiven = NOT_GIVEN,
        comment: str | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Record]:
        """Update an existing DNS record.

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

          id: Identifier

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
    def edit(
        self,
        dns_record_id: str,
        *,
        zone_id: str,
        content: str,
        name: str,
        type: Literal["NS"],
        id: str | NotGiven = NOT_GIVEN,
        comment: str | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Record]:
        """Update an existing DNS record.

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

          id: Identifier

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
    def edit(
        self,
        dns_record_id: str,
        *,
        zone_id: str,
        content: str,
        name: str,
        type: Literal["OPENPGPKEY"],
        id: str | NotGiven = NOT_GIVEN,
        comment: str | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Record]:
        """Update an existing DNS record.

        Notes:

        - A/AAAA records cannot exist on the same name as CNAME records.
        - NS records cannot exist on the same name as any other record type.
        - Domain names are always represented in Punycode, even if Unicode characters
          were used when creating the record.

        Args:
          zone_id: Identifier

          dns_record_id: Identifier

          content: A single Base64-encoded OpenPGP Transferable Public Key (RFC 4880 Section 11.1)

          name: DNS record name (or @ for the zone apex) in Punycode.

          type: Record type.

          id: Identifier

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
    def edit(
        self,
        dns_record_id: str,
        *,
        zone_id: str,
        content: str,
        name: str,
        type: Literal["PTR"],
        id: str | NotGiven = NOT_GIVEN,
        comment: str | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Record]:
        """Update an existing DNS record.

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

          id: Identifier

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
    def edit(
        self,
        dns_record_id: str,
        *,
        zone_id: str,
        data: record_edit_params.SMIMEARecordData,
        name: str,
        type: Literal["SMIMEA"],
        id: str | NotGiven = NOT_GIVEN,
        comment: str | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Record]:
        """Update an existing DNS record.

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

          id: Identifier

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
    def edit(
        self,
        dns_record_id: str,
        *,
        zone_id: str,
        data: record_edit_params.SRVRecordData,
        name: str,
        type: Literal["SRV"],
        id: str | NotGiven = NOT_GIVEN,
        comment: str | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Record]:
        """Update an existing DNS record.

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

          id: Identifier

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
    def edit(
        self,
        dns_record_id: str,
        *,
        zone_id: str,
        data: record_edit_params.SSHFPRecordData,
        name: str,
        type: Literal["SSHFP"],
        id: str | NotGiven = NOT_GIVEN,
        comment: str | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Record]:
        """Update an existing DNS record.

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

          id: Identifier

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
    def edit(
        self,
        dns_record_id: str,
        *,
        zone_id: str,
        data: record_edit_params.SVCBRecordData,
        name: str,
        type: Literal["SVCB"],
        id: str | NotGiven = NOT_GIVEN,
        comment: str | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Record]:
        """Update an existing DNS record.

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

          id: Identifier

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
    def edit(
        self,
        dns_record_id: str,
        *,
        zone_id: str,
        data: record_edit_params.TLSARecordData,
        name: str,
        type: Literal["TLSA"],
        id: str | NotGiven = NOT_GIVEN,
        comment: str | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Record]:
        """Update an existing DNS record.

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

          id: Identifier

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
    def edit(
        self,
        dns_record_id: str,
        *,
        zone_id: str,
        content: str,
        name: str,
        type: Literal["TXT"],
        id: str | NotGiven = NOT_GIVEN,
        comment: str | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Record]:
        """Update an existing DNS record.

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

          id: Identifier

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
    def edit(
        self,
        dns_record_id: str,
        *,
        zone_id: str,
        data: record_edit_params.URIRecordData,
        name: str,
        priority: float,
        type: Literal["URI"],
        id: str | NotGiven = NOT_GIVEN,
        comment: str | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Record]:
        """Update an existing DNS record.

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

          id: Identifier

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
        ["zone_id", "data", "name", "type"],
        ["zone_id", "content", "name", "priority", "type"],
        ["zone_id", "data", "name", "priority", "type"],
    )
    def edit(
        self,
        dns_record_id: str,
        *,
        zone_id: str,
        content: str | NotGiven = NOT_GIVEN,
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
        | Literal["OPENPGPKEY"]
        | Literal["PTR"]
        | Literal["SMIMEA"]
        | Literal["SRV"]
        | Literal["SSHFP"]
        | Literal["SVCB"]
        | Literal["TLSA"]
        | Literal["TXT"]
        | Literal["URI"],
        id: str | NotGiven = NOT_GIVEN,
        comment: str | NotGiven = NOT_GIVEN,
        proxied: bool | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        data: record_edit_params.CAARecordData
        | record_edit_params.CERTRecordData
        | record_edit_params.DNSKEYRecordData
        | record_edit_params.DSRecordData
        | record_edit_params.HTTPSRecordData
        | record_edit_params.LOCRecordData
        | record_edit_params.NAPTRRecordData
        | record_edit_params.SMIMEARecordData
        | record_edit_params.SRVRecordData
        | record_edit_params.SSHFPRecordData
        | record_edit_params.URIRecordData
        | NotGiven = NOT_GIVEN,
        priority: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Record]:
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not dns_record_id:
            raise ValueError(f"Expected a non-empty value for `dns_record_id` but received {dns_record_id!r}")
        return cast(
            Optional[Record],
            self._patch(
                f"/zones/{zone_id}/dns_records/{dns_record_id}",
                body=maybe_transform(
                    {
                        "content": content,
                        "name": name,
                        "type": type,
                        "id": id,
                        "comment": comment,
                        "proxied": proxied,
                        "tags": tags,
                        "ttl": ttl,
                        "data": data,
                        "priority": priority,
                    },
                    record_edit_params.RecordEditParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper[Optional[Record]]._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[Record]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def export(
        self,
        *,
        zone_id: str,
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
    ) -> Optional[Record]:
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
            Optional[Record],
            self._get(
                f"/zones/{zone_id}/dns_records/{dns_record_id}",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper[Optional[Record]]._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[Record]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def import_(
        self,
        *,
        zone_id: str,
        file: str,
        proxied: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[RecordImportResponse]:
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
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return self._post(
            f"/zones/{zone_id}/dns_records/import",
            body=maybe_transform(
                {
                    "file": file,
                    "proxied": proxied,
                },
                record_import_params.RecordImportParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[RecordImportResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[RecordImportResponse]], ResultWrapper[RecordImportResponse]),
        )

    def scan(
        self,
        *,
        zone_id: str,
        body: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[RecordScanResponse]:
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
            body=maybe_transform(body, record_scan_params.RecordScanParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[RecordScanResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[RecordScanResponse]], ResultWrapper[RecordScanResponse]),
        )


class AsyncRecordsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRecordsResourceWithRawResponse:
        return AsyncRecordsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRecordsResourceWithStreamingResponse:
        return AsyncRecordsResourceWithStreamingResponse(self)

    @overload
    async def create(
        self,
        *,
        zone_id: str,
        content: str,
        name: str,
        type: Literal["A"],
        id: str | NotGiven = NOT_GIVEN,
        comment: str | NotGiven = NOT_GIVEN,
        proxied: bool | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Record]:
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

          id: Identifier

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
        *,
        zone_id: str,
        content: str,
        name: str,
        type: Literal["AAAA"],
        id: str | NotGiven = NOT_GIVEN,
        comment: str | NotGiven = NOT_GIVEN,
        proxied: bool | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Record]:
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

          id: Identifier

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
        *,
        zone_id: str,
        data: record_create_params.CAARecordData,
        name: str,
        type: Literal["CAA"],
        id: str | NotGiven = NOT_GIVEN,
        comment: str | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Record]:
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

          id: Identifier

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
        *,
        zone_id: str,
        data: record_create_params.CERTRecordData,
        name: str,
        type: Literal["CERT"],
        id: str | NotGiven = NOT_GIVEN,
        comment: str | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Record]:
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

          id: Identifier

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
        *,
        zone_id: str,
        content: str,
        name: str,
        type: Literal["CNAME"],
        id: str | NotGiven = NOT_GIVEN,
        comment: str | NotGiven = NOT_GIVEN,
        proxied: bool | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Record]:
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

          id: Identifier

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
        *,
        zone_id: str,
        data: record_create_params.DNSKEYRecordData,
        name: str,
        type: Literal["DNSKEY"],
        id: str | NotGiven = NOT_GIVEN,
        comment: str | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Record]:
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

          id: Identifier

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
        *,
        zone_id: str,
        data: record_create_params.DSRecordData,
        name: str,
        type: Literal["DS"],
        id: str | NotGiven = NOT_GIVEN,
        comment: str | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Record]:
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

          id: Identifier

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
        *,
        zone_id: str,
        data: record_create_params.HTTPSRecordData,
        name: str,
        type: Literal["HTTPS"],
        id: str | NotGiven = NOT_GIVEN,
        comment: str | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Record]:
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

          id: Identifier

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
        *,
        zone_id: str,
        data: record_create_params.LOCRecordData,
        name: str,
        type: Literal["LOC"],
        id: str | NotGiven = NOT_GIVEN,
        comment: str | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Record]:
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

          id: Identifier

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
        *,
        zone_id: str,
        content: str,
        name: str,
        priority: float,
        type: Literal["MX"],
        id: str | NotGiven = NOT_GIVEN,
        comment: str | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Record]:
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

          id: Identifier

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
        *,
        zone_id: str,
        data: record_create_params.NAPTRRecordData,
        name: str,
        type: Literal["NAPTR"],
        id: str | NotGiven = NOT_GIVEN,
        comment: str | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Record]:
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

          id: Identifier

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
        *,
        zone_id: str,
        content: str,
        name: str,
        type: Literal["NS"],
        id: str | NotGiven = NOT_GIVEN,
        comment: str | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Record]:
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

          id: Identifier

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
        *,
        zone_id: str,
        content: str,
        name: str,
        type: Literal["OPENPGPKEY"],
        id: str | NotGiven = NOT_GIVEN,
        comment: str | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Record]:
        """
        Create a new DNS record for a zone.

        Notes:

        - A/AAAA records cannot exist on the same name as CNAME records.
        - NS records cannot exist on the same name as any other record type.
        - Domain names are always represented in Punycode, even if Unicode characters
          were used when creating the record.

        Args:
          zone_id: Identifier

          content: A single Base64-encoded OpenPGP Transferable Public Key (RFC 4880 Section 11.1)

          name: DNS record name (or @ for the zone apex) in Punycode.

          type: Record type.

          id: Identifier

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
        *,
        zone_id: str,
        content: str,
        name: str,
        type: Literal["PTR"],
        id: str | NotGiven = NOT_GIVEN,
        comment: str | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Record]:
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

          id: Identifier

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
        *,
        zone_id: str,
        data: record_create_params.SMIMEARecordData,
        name: str,
        type: Literal["SMIMEA"],
        id: str | NotGiven = NOT_GIVEN,
        comment: str | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Record]:
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

          id: Identifier

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
        *,
        zone_id: str,
        data: record_create_params.SRVRecordData,
        name: str,
        type: Literal["SRV"],
        id: str | NotGiven = NOT_GIVEN,
        comment: str | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Record]:
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

          id: Identifier

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
        *,
        zone_id: str,
        data: record_create_params.SSHFPRecordData,
        name: str,
        type: Literal["SSHFP"],
        id: str | NotGiven = NOT_GIVEN,
        comment: str | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Record]:
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

          id: Identifier

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
        *,
        zone_id: str,
        data: record_create_params.SVCBRecordData,
        name: str,
        type: Literal["SVCB"],
        id: str | NotGiven = NOT_GIVEN,
        comment: str | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Record]:
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

          id: Identifier

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
        *,
        zone_id: str,
        data: record_create_params.TLSARecordData,
        name: str,
        type: Literal["TLSA"],
        id: str | NotGiven = NOT_GIVEN,
        comment: str | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Record]:
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

          id: Identifier

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
        *,
        zone_id: str,
        content: str,
        name: str,
        type: Literal["TXT"],
        id: str | NotGiven = NOT_GIVEN,
        comment: str | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Record]:
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

          id: Identifier

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
        *,
        zone_id: str,
        data: record_create_params.URIRecordData,
        name: str,
        priority: float,
        type: Literal["URI"],
        id: str | NotGiven = NOT_GIVEN,
        comment: str | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Record]:
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

          id: Identifier

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
        ["zone_id", "data", "name", "type"],
        ["zone_id", "content", "name", "priority", "type"],
        ["zone_id", "data", "name", "priority", "type"],
    )
    async def create(
        self,
        *,
        zone_id: str,
        content: str | NotGiven = NOT_GIVEN,
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
        | Literal["OPENPGPKEY"]
        | Literal["PTR"]
        | Literal["SMIMEA"]
        | Literal["SRV"]
        | Literal["SSHFP"]
        | Literal["SVCB"]
        | Literal["TLSA"]
        | Literal["TXT"]
        | Literal["URI"],
        id: str | NotGiven = NOT_GIVEN,
        comment: str | NotGiven = NOT_GIVEN,
        proxied: bool | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        data: record_create_params.CAARecordData
        | record_create_params.CERTRecordData
        | record_create_params.DNSKEYRecordData
        | record_create_params.DSRecordData
        | record_create_params.HTTPSRecordData
        | record_create_params.LOCRecordData
        | record_create_params.NAPTRRecordData
        | record_create_params.SMIMEARecordData
        | record_create_params.SRVRecordData
        | record_create_params.SSHFPRecordData
        | record_create_params.URIRecordData
        | NotGiven = NOT_GIVEN,
        priority: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Record]:
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return cast(
            Optional[Record],
            await self._post(
                f"/zones/{zone_id}/dns_records",
                body=await async_maybe_transform(
                    {
                        "content": content,
                        "name": name,
                        "type": type,
                        "id": id,
                        "comment": comment,
                        "proxied": proxied,
                        "tags": tags,
                        "ttl": ttl,
                        "data": data,
                        "priority": priority,
                    },
                    record_create_params.RecordCreateParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper[Optional[Record]]._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[Record]
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
        id: str | NotGiven = NOT_GIVEN,
        comment: str | NotGiven = NOT_GIVEN,
        proxied: bool | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Record]:
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

          id: Identifier

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
        id: str | NotGiven = NOT_GIVEN,
        comment: str | NotGiven = NOT_GIVEN,
        proxied: bool | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Record]:
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

          id: Identifier

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
        data: record_update_params.CAARecordData,
        name: str,
        type: Literal["CAA"],
        id: str | NotGiven = NOT_GIVEN,
        comment: str | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Record]:
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

          id: Identifier

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
        data: record_update_params.CERTRecordData,
        name: str,
        type: Literal["CERT"],
        id: str | NotGiven = NOT_GIVEN,
        comment: str | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Record]:
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

          id: Identifier

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
        type: Literal["CNAME"],
        id: str | NotGiven = NOT_GIVEN,
        comment: str | NotGiven = NOT_GIVEN,
        proxied: bool | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Record]:
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

          id: Identifier

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
        data: record_update_params.DNSKEYRecordData,
        name: str,
        type: Literal["DNSKEY"],
        id: str | NotGiven = NOT_GIVEN,
        comment: str | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Record]:
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

          id: Identifier

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
        data: record_update_params.DSRecordData,
        name: str,
        type: Literal["DS"],
        id: str | NotGiven = NOT_GIVEN,
        comment: str | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Record]:
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

          id: Identifier

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
        data: record_update_params.HTTPSRecordData,
        name: str,
        type: Literal["HTTPS"],
        id: str | NotGiven = NOT_GIVEN,
        comment: str | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Record]:
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

          id: Identifier

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
        data: record_update_params.LOCRecordData,
        name: str,
        type: Literal["LOC"],
        id: str | NotGiven = NOT_GIVEN,
        comment: str | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Record]:
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

          id: Identifier

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
        id: str | NotGiven = NOT_GIVEN,
        comment: str | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Record]:
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

          id: Identifier

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
        data: record_update_params.NAPTRRecordData,
        name: str,
        type: Literal["NAPTR"],
        id: str | NotGiven = NOT_GIVEN,
        comment: str | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Record]:
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

          id: Identifier

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
        type: Literal["NS"],
        id: str | NotGiven = NOT_GIVEN,
        comment: str | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Record]:
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

          id: Identifier

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
        type: Literal["OPENPGPKEY"],
        id: str | NotGiven = NOT_GIVEN,
        comment: str | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Record]:
        """Overwrite an existing DNS record.

        Notes:

        - A/AAAA records cannot exist on the same name as CNAME records.
        - NS records cannot exist on the same name as any other record type.
        - Domain names are always represented in Punycode, even if Unicode characters
          were used when creating the record.

        Args:
          zone_id: Identifier

          dns_record_id: Identifier

          content: A single Base64-encoded OpenPGP Transferable Public Key (RFC 4880 Section 11.1)

          name: DNS record name (or @ for the zone apex) in Punycode.

          type: Record type.

          id: Identifier

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
        id: str | NotGiven = NOT_GIVEN,
        comment: str | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Record]:
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

          id: Identifier

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
        data: record_update_params.SMIMEARecordData,
        name: str,
        type: Literal["SMIMEA"],
        id: str | NotGiven = NOT_GIVEN,
        comment: str | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Record]:
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

          id: Identifier

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
        data: record_update_params.SRVRecordData,
        name: str,
        type: Literal["SRV"],
        id: str | NotGiven = NOT_GIVEN,
        comment: str | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Record]:
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

          id: Identifier

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
        data: record_update_params.SSHFPRecordData,
        name: str,
        type: Literal["SSHFP"],
        id: str | NotGiven = NOT_GIVEN,
        comment: str | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Record]:
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

          id: Identifier

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
        data: record_update_params.SVCBRecordData,
        name: str,
        type: Literal["SVCB"],
        id: str | NotGiven = NOT_GIVEN,
        comment: str | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Record]:
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

          id: Identifier

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
        data: record_update_params.TLSARecordData,
        name: str,
        type: Literal["TLSA"],
        id: str | NotGiven = NOT_GIVEN,
        comment: str | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Record]:
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

          id: Identifier

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
        id: str | NotGiven = NOT_GIVEN,
        comment: str | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Record]:
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

          id: Identifier

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
        data: record_update_params.URIRecordData,
        name: str,
        priority: float,
        type: Literal["URI"],
        id: str | NotGiven = NOT_GIVEN,
        comment: str | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Record]:
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

          id: Identifier

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
        ["zone_id", "data", "name", "type"],
        ["zone_id", "content", "name", "priority", "type"],
        ["zone_id", "data", "name", "priority", "type"],
    )
    async def update(
        self,
        dns_record_id: str,
        *,
        zone_id: str,
        content: str | NotGiven = NOT_GIVEN,
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
        | Literal["OPENPGPKEY"]
        | Literal["PTR"]
        | Literal["SMIMEA"]
        | Literal["SRV"]
        | Literal["SSHFP"]
        | Literal["SVCB"]
        | Literal["TLSA"]
        | Literal["TXT"]
        | Literal["URI"],
        id: str | NotGiven = NOT_GIVEN,
        comment: str | NotGiven = NOT_GIVEN,
        proxied: bool | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        data: record_update_params.CAARecordData
        | record_update_params.CERTRecordData
        | record_update_params.DNSKEYRecordData
        | record_update_params.DSRecordData
        | record_update_params.HTTPSRecordData
        | record_update_params.LOCRecordData
        | record_update_params.NAPTRRecordData
        | record_update_params.SMIMEARecordData
        | record_update_params.SRVRecordData
        | record_update_params.SSHFPRecordData
        | record_update_params.URIRecordData
        | NotGiven = NOT_GIVEN,
        priority: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Record]:
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not dns_record_id:
            raise ValueError(f"Expected a non-empty value for `dns_record_id` but received {dns_record_id!r}")
        return cast(
            Optional[Record],
            await self._put(
                f"/zones/{zone_id}/dns_records/{dns_record_id}",
                body=await async_maybe_transform(
                    {
                        "content": content,
                        "name": name,
                        "type": type,
                        "id": id,
                        "comment": comment,
                        "proxied": proxied,
                        "tags": tags,
                        "ttl": ttl,
                        "data": data,
                        "priority": priority,
                    },
                    record_update_params.RecordUpdateParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper[Optional[Record]]._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[Record]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def list(
        self,
        *,
        zone_id: str,
        comment: record_list_params.Comment | NotGiven = NOT_GIVEN,
        content: str | NotGiven = NOT_GIVEN,
        direction: SortDirection | NotGiven = NOT_GIVEN,
        match: Literal["any", "all"] | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        order: Literal["type", "name", "content", "ttl", "proxied"] | NotGiven = NOT_GIVEN,
        page: float | NotGiven = NOT_GIVEN,
        per_page: float | NotGiven = NOT_GIVEN,
        proxied: bool | NotGiven = NOT_GIVEN,
        search: str | NotGiven = NOT_GIVEN,
        tag: record_list_params.Tag | NotGiven = NOT_GIVEN,
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
            "OPENPGPKEY",
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
    ) -> AsyncPaginator[Record, AsyncV4PagePaginationArray[Record]]:
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
        return self._get_api_list(
            f"/zones/{zone_id}/dns_records",
            page=AsyncV4PagePaginationArray[Record],
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
                    record_list_params.RecordListParams,
                ),
            ),
            model=cast(Any, Record),  # Union types cannot be passed in as arguments in the type system
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
    ) -> Optional[RecordDeleteResponse]:
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
                post_parser=ResultWrapper[Optional[RecordDeleteResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[RecordDeleteResponse]], ResultWrapper[RecordDeleteResponse]),
        )

    @overload
    async def edit(
        self,
        dns_record_id: str,
        *,
        zone_id: str,
        content: str,
        name: str,
        type: Literal["A"],
        id: str | NotGiven = NOT_GIVEN,
        comment: str | NotGiven = NOT_GIVEN,
        proxied: bool | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Record]:
        """Update an existing DNS record.

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

          id: Identifier

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
    async def edit(
        self,
        dns_record_id: str,
        *,
        zone_id: str,
        content: str,
        name: str,
        type: Literal["AAAA"],
        id: str | NotGiven = NOT_GIVEN,
        comment: str | NotGiven = NOT_GIVEN,
        proxied: bool | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Record]:
        """Update an existing DNS record.

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

          id: Identifier

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
    async def edit(
        self,
        dns_record_id: str,
        *,
        zone_id: str,
        data: record_edit_params.CAARecordData,
        name: str,
        type: Literal["CAA"],
        id: str | NotGiven = NOT_GIVEN,
        comment: str | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Record]:
        """Update an existing DNS record.

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

          id: Identifier

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
    async def edit(
        self,
        dns_record_id: str,
        *,
        zone_id: str,
        data: record_edit_params.CERTRecordData,
        name: str,
        type: Literal["CERT"],
        id: str | NotGiven = NOT_GIVEN,
        comment: str | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Record]:
        """Update an existing DNS record.

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

          id: Identifier

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
    async def edit(
        self,
        dns_record_id: str,
        *,
        zone_id: str,
        content: str,
        name: str,
        type: Literal["CNAME"],
        id: str | NotGiven = NOT_GIVEN,
        comment: str | NotGiven = NOT_GIVEN,
        proxied: bool | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Record]:
        """Update an existing DNS record.

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

          id: Identifier

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
    async def edit(
        self,
        dns_record_id: str,
        *,
        zone_id: str,
        data: record_edit_params.DNSKEYRecordData,
        name: str,
        type: Literal["DNSKEY"],
        id: str | NotGiven = NOT_GIVEN,
        comment: str | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Record]:
        """Update an existing DNS record.

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

          id: Identifier

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
    async def edit(
        self,
        dns_record_id: str,
        *,
        zone_id: str,
        data: record_edit_params.DSRecordData,
        name: str,
        type: Literal["DS"],
        id: str | NotGiven = NOT_GIVEN,
        comment: str | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Record]:
        """Update an existing DNS record.

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

          id: Identifier

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
    async def edit(
        self,
        dns_record_id: str,
        *,
        zone_id: str,
        data: record_edit_params.HTTPSRecordData,
        name: str,
        type: Literal["HTTPS"],
        id: str | NotGiven = NOT_GIVEN,
        comment: str | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Record]:
        """Update an existing DNS record.

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

          id: Identifier

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
    async def edit(
        self,
        dns_record_id: str,
        *,
        zone_id: str,
        data: record_edit_params.LOCRecordData,
        name: str,
        type: Literal["LOC"],
        id: str | NotGiven = NOT_GIVEN,
        comment: str | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Record]:
        """Update an existing DNS record.

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

          id: Identifier

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
    async def edit(
        self,
        dns_record_id: str,
        *,
        zone_id: str,
        content: str,
        name: str,
        priority: float,
        type: Literal["MX"],
        id: str | NotGiven = NOT_GIVEN,
        comment: str | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Record]:
        """Update an existing DNS record.

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

          id: Identifier

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
    async def edit(
        self,
        dns_record_id: str,
        *,
        zone_id: str,
        data: record_edit_params.NAPTRRecordData,
        name: str,
        type: Literal["NAPTR"],
        id: str | NotGiven = NOT_GIVEN,
        comment: str | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Record]:
        """Update an existing DNS record.

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

          id: Identifier

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
    async def edit(
        self,
        dns_record_id: str,
        *,
        zone_id: str,
        content: str,
        name: str,
        type: Literal["NS"],
        id: str | NotGiven = NOT_GIVEN,
        comment: str | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Record]:
        """Update an existing DNS record.

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

          id: Identifier

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
    async def edit(
        self,
        dns_record_id: str,
        *,
        zone_id: str,
        content: str,
        name: str,
        type: Literal["OPENPGPKEY"],
        id: str | NotGiven = NOT_GIVEN,
        comment: str | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Record]:
        """Update an existing DNS record.

        Notes:

        - A/AAAA records cannot exist on the same name as CNAME records.
        - NS records cannot exist on the same name as any other record type.
        - Domain names are always represented in Punycode, even if Unicode characters
          were used when creating the record.

        Args:
          zone_id: Identifier

          dns_record_id: Identifier

          content: A single Base64-encoded OpenPGP Transferable Public Key (RFC 4880 Section 11.1)

          name: DNS record name (or @ for the zone apex) in Punycode.

          type: Record type.

          id: Identifier

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
    async def edit(
        self,
        dns_record_id: str,
        *,
        zone_id: str,
        content: str,
        name: str,
        type: Literal["PTR"],
        id: str | NotGiven = NOT_GIVEN,
        comment: str | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Record]:
        """Update an existing DNS record.

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

          id: Identifier

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
    async def edit(
        self,
        dns_record_id: str,
        *,
        zone_id: str,
        data: record_edit_params.SMIMEARecordData,
        name: str,
        type: Literal["SMIMEA"],
        id: str | NotGiven = NOT_GIVEN,
        comment: str | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Record]:
        """Update an existing DNS record.

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

          id: Identifier

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
    async def edit(
        self,
        dns_record_id: str,
        *,
        zone_id: str,
        data: record_edit_params.SRVRecordData,
        name: str,
        type: Literal["SRV"],
        id: str | NotGiven = NOT_GIVEN,
        comment: str | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Record]:
        """Update an existing DNS record.

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

          id: Identifier

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
    async def edit(
        self,
        dns_record_id: str,
        *,
        zone_id: str,
        data: record_edit_params.SSHFPRecordData,
        name: str,
        type: Literal["SSHFP"],
        id: str | NotGiven = NOT_GIVEN,
        comment: str | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Record]:
        """Update an existing DNS record.

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

          id: Identifier

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
    async def edit(
        self,
        dns_record_id: str,
        *,
        zone_id: str,
        data: record_edit_params.SVCBRecordData,
        name: str,
        type: Literal["SVCB"],
        id: str | NotGiven = NOT_GIVEN,
        comment: str | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Record]:
        """Update an existing DNS record.

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

          id: Identifier

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
    async def edit(
        self,
        dns_record_id: str,
        *,
        zone_id: str,
        data: record_edit_params.TLSARecordData,
        name: str,
        type: Literal["TLSA"],
        id: str | NotGiven = NOT_GIVEN,
        comment: str | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Record]:
        """Update an existing DNS record.

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

          id: Identifier

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
    async def edit(
        self,
        dns_record_id: str,
        *,
        zone_id: str,
        content: str,
        name: str,
        type: Literal["TXT"],
        id: str | NotGiven = NOT_GIVEN,
        comment: str | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Record]:
        """Update an existing DNS record.

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

          id: Identifier

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
    async def edit(
        self,
        dns_record_id: str,
        *,
        zone_id: str,
        data: record_edit_params.URIRecordData,
        name: str,
        priority: float,
        type: Literal["URI"],
        id: str | NotGiven = NOT_GIVEN,
        comment: str | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Record]:
        """Update an existing DNS record.

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

          id: Identifier

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
        ["zone_id", "data", "name", "type"],
        ["zone_id", "content", "name", "priority", "type"],
        ["zone_id", "data", "name", "priority", "type"],
    )
    async def edit(
        self,
        dns_record_id: str,
        *,
        zone_id: str,
        content: str | NotGiven = NOT_GIVEN,
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
        | Literal["OPENPGPKEY"]
        | Literal["PTR"]
        | Literal["SMIMEA"]
        | Literal["SRV"]
        | Literal["SSHFP"]
        | Literal["SVCB"]
        | Literal["TLSA"]
        | Literal["TXT"]
        | Literal["URI"],
        id: str | NotGiven = NOT_GIVEN,
        comment: str | NotGiven = NOT_GIVEN,
        proxied: bool | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        data: record_edit_params.CAARecordData
        | record_edit_params.CERTRecordData
        | record_edit_params.DNSKEYRecordData
        | record_edit_params.DSRecordData
        | record_edit_params.HTTPSRecordData
        | record_edit_params.LOCRecordData
        | record_edit_params.NAPTRRecordData
        | record_edit_params.SMIMEARecordData
        | record_edit_params.SRVRecordData
        | record_edit_params.SSHFPRecordData
        | record_edit_params.URIRecordData
        | NotGiven = NOT_GIVEN,
        priority: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Record]:
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not dns_record_id:
            raise ValueError(f"Expected a non-empty value for `dns_record_id` but received {dns_record_id!r}")
        return cast(
            Optional[Record],
            await self._patch(
                f"/zones/{zone_id}/dns_records/{dns_record_id}",
                body=await async_maybe_transform(
                    {
                        "content": content,
                        "name": name,
                        "type": type,
                        "id": id,
                        "comment": comment,
                        "proxied": proxied,
                        "tags": tags,
                        "ttl": ttl,
                        "data": data,
                        "priority": priority,
                    },
                    record_edit_params.RecordEditParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper[Optional[Record]]._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[Record]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def export(
        self,
        *,
        zone_id: str,
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
    ) -> Optional[Record]:
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
            Optional[Record],
            await self._get(
                f"/zones/{zone_id}/dns_records/{dns_record_id}",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper[Optional[Record]]._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[Record]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def import_(
        self,
        *,
        zone_id: str,
        file: str,
        proxied: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[RecordImportResponse]:
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
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return await self._post(
            f"/zones/{zone_id}/dns_records/import",
            body=await async_maybe_transform(
                {
                    "file": file,
                    "proxied": proxied,
                },
                record_import_params.RecordImportParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[RecordImportResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[RecordImportResponse]], ResultWrapper[RecordImportResponse]),
        )

    async def scan(
        self,
        *,
        zone_id: str,
        body: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[RecordScanResponse]:
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
            body=await async_maybe_transform(body, record_scan_params.RecordScanParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[RecordScanResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[RecordScanResponse]], ResultWrapper[RecordScanResponse]),
        )


class RecordsResourceWithRawResponse:
    def __init__(self, records: RecordsResource) -> None:
        self._records = records

        self.create = to_raw_response_wrapper(
            records.create,
        )
        self.update = to_raw_response_wrapper(
            records.update,
        )
        self.list = to_raw_response_wrapper(
            records.list,
        )
        self.delete = to_raw_response_wrapper(
            records.delete,
        )
        self.edit = to_raw_response_wrapper(
            records.edit,
        )
        self.export = to_raw_response_wrapper(
            records.export,
        )
        self.get = to_raw_response_wrapper(
            records.get,
        )
        self.import_ = to_raw_response_wrapper(
            records.import_,
        )
        self.scan = to_raw_response_wrapper(
            records.scan,
        )


class AsyncRecordsResourceWithRawResponse:
    def __init__(self, records: AsyncRecordsResource) -> None:
        self._records = records

        self.create = async_to_raw_response_wrapper(
            records.create,
        )
        self.update = async_to_raw_response_wrapper(
            records.update,
        )
        self.list = async_to_raw_response_wrapper(
            records.list,
        )
        self.delete = async_to_raw_response_wrapper(
            records.delete,
        )
        self.edit = async_to_raw_response_wrapper(
            records.edit,
        )
        self.export = async_to_raw_response_wrapper(
            records.export,
        )
        self.get = async_to_raw_response_wrapper(
            records.get,
        )
        self.import_ = async_to_raw_response_wrapper(
            records.import_,
        )
        self.scan = async_to_raw_response_wrapper(
            records.scan,
        )


class RecordsResourceWithStreamingResponse:
    def __init__(self, records: RecordsResource) -> None:
        self._records = records

        self.create = to_streamed_response_wrapper(
            records.create,
        )
        self.update = to_streamed_response_wrapper(
            records.update,
        )
        self.list = to_streamed_response_wrapper(
            records.list,
        )
        self.delete = to_streamed_response_wrapper(
            records.delete,
        )
        self.edit = to_streamed_response_wrapper(
            records.edit,
        )
        self.export = to_streamed_response_wrapper(
            records.export,
        )
        self.get = to_streamed_response_wrapper(
            records.get,
        )
        self.import_ = to_streamed_response_wrapper(
            records.import_,
        )
        self.scan = to_streamed_response_wrapper(
            records.scan,
        )


class AsyncRecordsResourceWithStreamingResponse:
    def __init__(self, records: AsyncRecordsResource) -> None:
        self._records = records

        self.create = async_to_streamed_response_wrapper(
            records.create,
        )
        self.update = async_to_streamed_response_wrapper(
            records.update,
        )
        self.list = async_to_streamed_response_wrapper(
            records.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            records.delete,
        )
        self.edit = async_to_streamed_response_wrapper(
            records.edit,
        )
        self.export = async_to_streamed_response_wrapper(
            records.export,
        )
        self.get = async_to_streamed_response_wrapper(
            records.get,
        )
        self.import_ = async_to_streamed_response_wrapper(
            records.import_,
        )
        self.scan = async_to_streamed_response_wrapper(
            records.scan,
        )
