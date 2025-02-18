# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, List, Type, Iterable, Optional, cast
from typing_extensions import Literal, overload

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
    record_batch_params,
    record_create_params,
    record_import_params,
    record_update_params,
)
from ...pagination import SyncV4PagePaginationArray, AsyncV4PagePaginationArray
from ..._base_client import AsyncPaginator, make_request_options
from ...types.dns.ttl_param import TTLParam
from ...types.dns.record_tags import RecordTags
from ...types.dns.record_param import RecordParam
from ...types.dns.batch_put_param import BatchPutParam
from ...types.dns.record_response import RecordResponse
from ...types.dns.batch_patch_param import BatchPatchParam
from ...types.shared.sort_direction import SortDirection
from ...types.dns.record_scan_response import RecordScanResponse
from ...types.dns.record_batch_response import RecordBatchResponse
from ...types.dns.record_delete_response import RecordDeleteResponse
from ...types.dns.record_import_response import RecordImportResponse

__all__ = ["RecordsResource", "AsyncRecordsResource"]


class RecordsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RecordsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return RecordsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RecordsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return RecordsResourceWithStreamingResponse(self)

    @overload
    def create(
        self,
        *,
        zone_id: str,
        comment: str | NotGiven = NOT_GIVEN,
        content: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        proxied: bool | NotGiven = NOT_GIVEN,
        settings: record_create_params.ARecordSettings | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        type: Literal["A"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[RecordResponse]:
        """
        Create a new DNS record for a zone.

        Notes:

        - A/AAAA records cannot exist on the same name as CNAME records.
        - NS records cannot exist on the same name as any other record type.
        - Domain names are always represented in Punycode, even if Unicode characters
          were used when creating the record.

        Args:
          zone_id: Identifier

          comment: Comments or notes about the DNS record. This field has no effect on DNS
              responses.

          content: A valid IPv4 address.

          name: DNS record name (or @ for the zone apex) in Punycode.

          proxied: Whether the record is receiving the performance and security benefits of
              Cloudflare.

          settings: Settings for the DNS record.

          tags: Custom tags for the DNS record. This field has no effect on DNS responses.

          ttl: Time To Live (TTL) of the DNS record in seconds. Setting to 1 means 'automatic'.
              Value must be between 60 and 86400, with the minimum reduced to 30 for
              Enterprise zones.

          type: Record type.

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
        comment: str | NotGiven = NOT_GIVEN,
        content: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        proxied: bool | NotGiven = NOT_GIVEN,
        settings: record_create_params.AAAARecordSettings | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        type: Literal["AAAA"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[RecordResponse]:
        """
        Create a new DNS record for a zone.

        Notes:

        - A/AAAA records cannot exist on the same name as CNAME records.
        - NS records cannot exist on the same name as any other record type.
        - Domain names are always represented in Punycode, even if Unicode characters
          were used when creating the record.

        Args:
          zone_id: Identifier

          comment: Comments or notes about the DNS record. This field has no effect on DNS
              responses.

          content: A valid IPv6 address.

          name: DNS record name (or @ for the zone apex) in Punycode.

          proxied: Whether the record is receiving the performance and security benefits of
              Cloudflare.

          settings: Settings for the DNS record.

          tags: Custom tags for the DNS record. This field has no effect on DNS responses.

          ttl: Time To Live (TTL) of the DNS record in seconds. Setting to 1 means 'automatic'.
              Value must be between 60 and 86400, with the minimum reduced to 30 for
              Enterprise zones.

          type: Record type.

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
        comment: str | NotGiven = NOT_GIVEN,
        data: record_create_params.CAARecordData | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        proxied: bool | NotGiven = NOT_GIVEN,
        settings: record_create_params.CAARecordSettings | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        type: Literal["CAA"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[RecordResponse]:
        """
        Create a new DNS record for a zone.

        Notes:

        - A/AAAA records cannot exist on the same name as CNAME records.
        - NS records cannot exist on the same name as any other record type.
        - Domain names are always represented in Punycode, even if Unicode characters
          were used when creating the record.

        Args:
          zone_id: Identifier

          comment: Comments or notes about the DNS record. This field has no effect on DNS
              responses.

          data: Components of a CAA record.

          name: DNS record name (or @ for the zone apex) in Punycode.

          proxied: Whether the record is receiving the performance and security benefits of
              Cloudflare.

          settings: Settings for the DNS record.

          tags: Custom tags for the DNS record. This field has no effect on DNS responses.

          ttl: Time To Live (TTL) of the DNS record in seconds. Setting to 1 means 'automatic'.
              Value must be between 60 and 86400, with the minimum reduced to 30 for
              Enterprise zones.

          type: Record type.

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
        comment: str | NotGiven = NOT_GIVEN,
        data: record_create_params.CERTRecordData | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        proxied: bool | NotGiven = NOT_GIVEN,
        settings: record_create_params.CERTRecordSettings | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        type: Literal["CERT"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[RecordResponse]:
        """
        Create a new DNS record for a zone.

        Notes:

        - A/AAAA records cannot exist on the same name as CNAME records.
        - NS records cannot exist on the same name as any other record type.
        - Domain names are always represented in Punycode, even if Unicode characters
          were used when creating the record.

        Args:
          zone_id: Identifier

          comment: Comments or notes about the DNS record. This field has no effect on DNS
              responses.

          data: Components of a CERT record.

          name: DNS record name (or @ for the zone apex) in Punycode.

          proxied: Whether the record is receiving the performance and security benefits of
              Cloudflare.

          settings: Settings for the DNS record.

          tags: Custom tags for the DNS record. This field has no effect on DNS responses.

          ttl: Time To Live (TTL) of the DNS record in seconds. Setting to 1 means 'automatic'.
              Value must be between 60 and 86400, with the minimum reduced to 30 for
              Enterprise zones.

          type: Record type.

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
        comment: str | NotGiven = NOT_GIVEN,
        content: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        proxied: bool | NotGiven = NOT_GIVEN,
        settings: record_create_params.CNAMERecordSettings | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        type: Literal["CNAME"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[RecordResponse]:
        """
        Create a new DNS record for a zone.

        Notes:

        - A/AAAA records cannot exist on the same name as CNAME records.
        - NS records cannot exist on the same name as any other record type.
        - Domain names are always represented in Punycode, even if Unicode characters
          were used when creating the record.

        Args:
          zone_id: Identifier

          comment: Comments or notes about the DNS record. This field has no effect on DNS
              responses.

          content: A valid hostname. Must not match the record's name.

          name: DNS record name (or @ for the zone apex) in Punycode.

          proxied: Whether the record is receiving the performance and security benefits of
              Cloudflare.

          settings: Settings for the DNS record.

          tags: Custom tags for the DNS record. This field has no effect on DNS responses.

          ttl: Time To Live (TTL) of the DNS record in seconds. Setting to 1 means 'automatic'.
              Value must be between 60 and 86400, with the minimum reduced to 30 for
              Enterprise zones.

          type: Record type.

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
        comment: str | NotGiven = NOT_GIVEN,
        data: record_create_params.DNSKEYRecordData | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        proxied: bool | NotGiven = NOT_GIVEN,
        settings: record_create_params.DNSKEYRecordSettings | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        type: Literal["DNSKEY"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[RecordResponse]:
        """
        Create a new DNS record for a zone.

        Notes:

        - A/AAAA records cannot exist on the same name as CNAME records.
        - NS records cannot exist on the same name as any other record type.
        - Domain names are always represented in Punycode, even if Unicode characters
          were used when creating the record.

        Args:
          zone_id: Identifier

          comment: Comments or notes about the DNS record. This field has no effect on DNS
              responses.

          data: Components of a DNSKEY record.

          name: DNS record name (or @ for the zone apex) in Punycode.

          proxied: Whether the record is receiving the performance and security benefits of
              Cloudflare.

          settings: Settings for the DNS record.

          tags: Custom tags for the DNS record. This field has no effect on DNS responses.

          ttl: Time To Live (TTL) of the DNS record in seconds. Setting to 1 means 'automatic'.
              Value must be between 60 and 86400, with the minimum reduced to 30 for
              Enterprise zones.

          type: Record type.

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
        comment: str | NotGiven = NOT_GIVEN,
        data: record_create_params.DSRecordData | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        proxied: bool | NotGiven = NOT_GIVEN,
        settings: record_create_params.DSRecordSettings | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        type: Literal["DS"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[RecordResponse]:
        """
        Create a new DNS record for a zone.

        Notes:

        - A/AAAA records cannot exist on the same name as CNAME records.
        - NS records cannot exist on the same name as any other record type.
        - Domain names are always represented in Punycode, even if Unicode characters
          were used when creating the record.

        Args:
          zone_id: Identifier

          comment: Comments or notes about the DNS record. This field has no effect on DNS
              responses.

          data: Components of a DS record.

          name: DNS record name (or @ for the zone apex) in Punycode.

          proxied: Whether the record is receiving the performance and security benefits of
              Cloudflare.

          settings: Settings for the DNS record.

          tags: Custom tags for the DNS record. This field has no effect on DNS responses.

          ttl: Time To Live (TTL) of the DNS record in seconds. Setting to 1 means 'automatic'.
              Value must be between 60 and 86400, with the minimum reduced to 30 for
              Enterprise zones.

          type: Record type.

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
        comment: str | NotGiven = NOT_GIVEN,
        data: record_create_params.HTTPSRecordData | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        proxied: bool | NotGiven = NOT_GIVEN,
        settings: record_create_params.HTTPSRecordSettings | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        type: Literal["HTTPS"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[RecordResponse]:
        """
        Create a new DNS record for a zone.

        Notes:

        - A/AAAA records cannot exist on the same name as CNAME records.
        - NS records cannot exist on the same name as any other record type.
        - Domain names are always represented in Punycode, even if Unicode characters
          were used when creating the record.

        Args:
          zone_id: Identifier

          comment: Comments or notes about the DNS record. This field has no effect on DNS
              responses.

          data: Components of a HTTPS record.

          name: DNS record name (or @ for the zone apex) in Punycode.

          proxied: Whether the record is receiving the performance and security benefits of
              Cloudflare.

          settings: Settings for the DNS record.

          tags: Custom tags for the DNS record. This field has no effect on DNS responses.

          ttl: Time To Live (TTL) of the DNS record in seconds. Setting to 1 means 'automatic'.
              Value must be between 60 and 86400, with the minimum reduced to 30 for
              Enterprise zones.

          type: Record type.

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
        comment: str | NotGiven = NOT_GIVEN,
        data: record_create_params.LOCRecordData | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        proxied: bool | NotGiven = NOT_GIVEN,
        settings: record_create_params.LOCRecordSettings | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        type: Literal["LOC"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[RecordResponse]:
        """
        Create a new DNS record for a zone.

        Notes:

        - A/AAAA records cannot exist on the same name as CNAME records.
        - NS records cannot exist on the same name as any other record type.
        - Domain names are always represented in Punycode, even if Unicode characters
          were used when creating the record.

        Args:
          zone_id: Identifier

          comment: Comments or notes about the DNS record. This field has no effect on DNS
              responses.

          data: Components of a LOC record.

          name: DNS record name (or @ for the zone apex) in Punycode.

          proxied: Whether the record is receiving the performance and security benefits of
              Cloudflare.

          settings: Settings for the DNS record.

          tags: Custom tags for the DNS record. This field has no effect on DNS responses.

          ttl: Time To Live (TTL) of the DNS record in seconds. Setting to 1 means 'automatic'.
              Value must be between 60 and 86400, with the minimum reduced to 30 for
              Enterprise zones.

          type: Record type.

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
        comment: str | NotGiven = NOT_GIVEN,
        content: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        priority: float | NotGiven = NOT_GIVEN,
        proxied: bool | NotGiven = NOT_GIVEN,
        settings: record_create_params.MXRecordSettings | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        type: Literal["MX"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[RecordResponse]:
        """
        Create a new DNS record for a zone.

        Notes:

        - A/AAAA records cannot exist on the same name as CNAME records.
        - NS records cannot exist on the same name as any other record type.
        - Domain names are always represented in Punycode, even if Unicode characters
          were used when creating the record.

        Args:
          zone_id: Identifier

          comment: Comments or notes about the DNS record. This field has no effect on DNS
              responses.

          content: A valid mail server hostname.

          name: DNS record name (or @ for the zone apex) in Punycode.

          priority: Required for MX, SRV and URI records; unused by other record types. Records with
              lower priorities are preferred.

          proxied: Whether the record is receiving the performance and security benefits of
              Cloudflare.

          settings: Settings for the DNS record.

          tags: Custom tags for the DNS record. This field has no effect on DNS responses.

          ttl: Time To Live (TTL) of the DNS record in seconds. Setting to 1 means 'automatic'.
              Value must be between 60 and 86400, with the minimum reduced to 30 for
              Enterprise zones.

          type: Record type.

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
        comment: str | NotGiven = NOT_GIVEN,
        data: record_create_params.NAPTRRecordData | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        proxied: bool | NotGiven = NOT_GIVEN,
        settings: record_create_params.NAPTRRecordSettings | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        type: Literal["NAPTR"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[RecordResponse]:
        """
        Create a new DNS record for a zone.

        Notes:

        - A/AAAA records cannot exist on the same name as CNAME records.
        - NS records cannot exist on the same name as any other record type.
        - Domain names are always represented in Punycode, even if Unicode characters
          were used when creating the record.

        Args:
          zone_id: Identifier

          comment: Comments or notes about the DNS record. This field has no effect on DNS
              responses.

          data: Components of a NAPTR record.

          name: DNS record name (or @ for the zone apex) in Punycode.

          proxied: Whether the record is receiving the performance and security benefits of
              Cloudflare.

          settings: Settings for the DNS record.

          tags: Custom tags for the DNS record. This field has no effect on DNS responses.

          ttl: Time To Live (TTL) of the DNS record in seconds. Setting to 1 means 'automatic'.
              Value must be between 60 and 86400, with the minimum reduced to 30 for
              Enterprise zones.

          type: Record type.

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
        comment: str | NotGiven = NOT_GIVEN,
        content: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        proxied: bool | NotGiven = NOT_GIVEN,
        settings: record_create_params.NSRecordSettings | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        type: Literal["NS"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[RecordResponse]:
        """
        Create a new DNS record for a zone.

        Notes:

        - A/AAAA records cannot exist on the same name as CNAME records.
        - NS records cannot exist on the same name as any other record type.
        - Domain names are always represented in Punycode, even if Unicode characters
          were used when creating the record.

        Args:
          zone_id: Identifier

          comment: Comments or notes about the DNS record. This field has no effect on DNS
              responses.

          content: A valid name server host name.

          name: DNS record name (or @ for the zone apex) in Punycode.

          proxied: Whether the record is receiving the performance and security benefits of
              Cloudflare.

          settings: Settings for the DNS record.

          tags: Custom tags for the DNS record. This field has no effect on DNS responses.

          ttl: Time To Live (TTL) of the DNS record in seconds. Setting to 1 means 'automatic'.
              Value must be between 60 and 86400, with the minimum reduced to 30 for
              Enterprise zones.

          type: Record type.

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
        comment: str | NotGiven = NOT_GIVEN,
        content: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        proxied: bool | NotGiven = NOT_GIVEN,
        settings: record_create_params.DNSRecordsOpenpgpkeyRecordSettings | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        type: Literal["OPENPGPKEY"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[RecordResponse]:
        """
        Create a new DNS record for a zone.

        Notes:

        - A/AAAA records cannot exist on the same name as CNAME records.
        - NS records cannot exist on the same name as any other record type.
        - Domain names are always represented in Punycode, even if Unicode characters
          were used when creating the record.

        Args:
          zone_id: Identifier

          comment: Comments or notes about the DNS record. This field has no effect on DNS
              responses.

          content: A single Base64-encoded OpenPGP Transferable Public Key (RFC 4880 Section 11.1)

          name: DNS record name (or @ for the zone apex) in Punycode.

          proxied: Whether the record is receiving the performance and security benefits of
              Cloudflare.

          settings: Settings for the DNS record.

          tags: Custom tags for the DNS record. This field has no effect on DNS responses.

          ttl: Time To Live (TTL) of the DNS record in seconds. Setting to 1 means 'automatic'.
              Value must be between 60 and 86400, with the minimum reduced to 30 for
              Enterprise zones.

          type: Record type.

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
        comment: str | NotGiven = NOT_GIVEN,
        content: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        proxied: bool | NotGiven = NOT_GIVEN,
        settings: record_create_params.PTRRecordSettings | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        type: Literal["PTR"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[RecordResponse]:
        """
        Create a new DNS record for a zone.

        Notes:

        - A/AAAA records cannot exist on the same name as CNAME records.
        - NS records cannot exist on the same name as any other record type.
        - Domain names are always represented in Punycode, even if Unicode characters
          were used when creating the record.

        Args:
          zone_id: Identifier

          comment: Comments or notes about the DNS record. This field has no effect on DNS
              responses.

          content: Domain name pointing to the address.

          name: DNS record name (or @ for the zone apex) in Punycode.

          proxied: Whether the record is receiving the performance and security benefits of
              Cloudflare.

          settings: Settings for the DNS record.

          tags: Custom tags for the DNS record. This field has no effect on DNS responses.

          ttl: Time To Live (TTL) of the DNS record in seconds. Setting to 1 means 'automatic'.
              Value must be between 60 and 86400, with the minimum reduced to 30 for
              Enterprise zones.

          type: Record type.

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
        comment: str | NotGiven = NOT_GIVEN,
        data: record_create_params.SMIMEARecordData | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        proxied: bool | NotGiven = NOT_GIVEN,
        settings: record_create_params.SMIMEARecordSettings | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        type: Literal["SMIMEA"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[RecordResponse]:
        """
        Create a new DNS record for a zone.

        Notes:

        - A/AAAA records cannot exist on the same name as CNAME records.
        - NS records cannot exist on the same name as any other record type.
        - Domain names are always represented in Punycode, even if Unicode characters
          were used when creating the record.

        Args:
          zone_id: Identifier

          comment: Comments or notes about the DNS record. This field has no effect on DNS
              responses.

          data: Components of a SMIMEA record.

          name: DNS record name (or @ for the zone apex) in Punycode.

          proxied: Whether the record is receiving the performance and security benefits of
              Cloudflare.

          settings: Settings for the DNS record.

          tags: Custom tags for the DNS record. This field has no effect on DNS responses.

          ttl: Time To Live (TTL) of the DNS record in seconds. Setting to 1 means 'automatic'.
              Value must be between 60 and 86400, with the minimum reduced to 30 for
              Enterprise zones.

          type: Record type.

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
        comment: str | NotGiven = NOT_GIVEN,
        data: record_create_params.SRVRecordData | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        proxied: bool | NotGiven = NOT_GIVEN,
        settings: record_create_params.SRVRecordSettings | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        type: Literal["SRV"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[RecordResponse]:
        """
        Create a new DNS record for a zone.

        Notes:

        - A/AAAA records cannot exist on the same name as CNAME records.
        - NS records cannot exist on the same name as any other record type.
        - Domain names are always represented in Punycode, even if Unicode characters
          were used when creating the record.

        Args:
          zone_id: Identifier

          comment: Comments or notes about the DNS record. This field has no effect on DNS
              responses.

          data: Components of a SRV record.

          name: DNS record name (or @ for the zone apex) in Punycode.

          proxied: Whether the record is receiving the performance and security benefits of
              Cloudflare.

          settings: Settings for the DNS record.

          tags: Custom tags for the DNS record. This field has no effect on DNS responses.

          ttl: Time To Live (TTL) of the DNS record in seconds. Setting to 1 means 'automatic'.
              Value must be between 60 and 86400, with the minimum reduced to 30 for
              Enterprise zones.

          type: Record type.

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
        comment: str | NotGiven = NOT_GIVEN,
        data: record_create_params.SSHFPRecordData | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        proxied: bool | NotGiven = NOT_GIVEN,
        settings: record_create_params.SSHFPRecordSettings | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        type: Literal["SSHFP"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[RecordResponse]:
        """
        Create a new DNS record for a zone.

        Notes:

        - A/AAAA records cannot exist on the same name as CNAME records.
        - NS records cannot exist on the same name as any other record type.
        - Domain names are always represented in Punycode, even if Unicode characters
          were used when creating the record.

        Args:
          zone_id: Identifier

          comment: Comments or notes about the DNS record. This field has no effect on DNS
              responses.

          data: Components of a SSHFP record.

          name: DNS record name (or @ for the zone apex) in Punycode.

          proxied: Whether the record is receiving the performance and security benefits of
              Cloudflare.

          settings: Settings for the DNS record.

          tags: Custom tags for the DNS record. This field has no effect on DNS responses.

          ttl: Time To Live (TTL) of the DNS record in seconds. Setting to 1 means 'automatic'.
              Value must be between 60 and 86400, with the minimum reduced to 30 for
              Enterprise zones.

          type: Record type.

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
        comment: str | NotGiven = NOT_GIVEN,
        data: record_create_params.SVCBRecordData | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        proxied: bool | NotGiven = NOT_GIVEN,
        settings: record_create_params.SVCBRecordSettings | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        type: Literal["SVCB"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[RecordResponse]:
        """
        Create a new DNS record for a zone.

        Notes:

        - A/AAAA records cannot exist on the same name as CNAME records.
        - NS records cannot exist on the same name as any other record type.
        - Domain names are always represented in Punycode, even if Unicode characters
          were used when creating the record.

        Args:
          zone_id: Identifier

          comment: Comments or notes about the DNS record. This field has no effect on DNS
              responses.

          data: Components of a SVCB record.

          name: DNS record name (or @ for the zone apex) in Punycode.

          proxied: Whether the record is receiving the performance and security benefits of
              Cloudflare.

          settings: Settings for the DNS record.

          tags: Custom tags for the DNS record. This field has no effect on DNS responses.

          ttl: Time To Live (TTL) of the DNS record in seconds. Setting to 1 means 'automatic'.
              Value must be between 60 and 86400, with the minimum reduced to 30 for
              Enterprise zones.

          type: Record type.

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
        comment: str | NotGiven = NOT_GIVEN,
        data: record_create_params.TLSARecordData | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        proxied: bool | NotGiven = NOT_GIVEN,
        settings: record_create_params.TLSARecordSettings | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        type: Literal["TLSA"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[RecordResponse]:
        """
        Create a new DNS record for a zone.

        Notes:

        - A/AAAA records cannot exist on the same name as CNAME records.
        - NS records cannot exist on the same name as any other record type.
        - Domain names are always represented in Punycode, even if Unicode characters
          were used when creating the record.

        Args:
          zone_id: Identifier

          comment: Comments or notes about the DNS record. This field has no effect on DNS
              responses.

          data: Components of a TLSA record.

          name: DNS record name (or @ for the zone apex) in Punycode.

          proxied: Whether the record is receiving the performance and security benefits of
              Cloudflare.

          settings: Settings for the DNS record.

          tags: Custom tags for the DNS record. This field has no effect on DNS responses.

          ttl: Time To Live (TTL) of the DNS record in seconds. Setting to 1 means 'automatic'.
              Value must be between 60 and 86400, with the minimum reduced to 30 for
              Enterprise zones.

          type: Record type.

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
        comment: str | NotGiven = NOT_GIVEN,
        content: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        proxied: bool | NotGiven = NOT_GIVEN,
        settings: record_create_params.TXTRecordSettings | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        type: Literal["TXT"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[RecordResponse]:
        """
        Create a new DNS record for a zone.

        Notes:

        - A/AAAA records cannot exist on the same name as CNAME records.
        - NS records cannot exist on the same name as any other record type.
        - Domain names are always represented in Punycode, even if Unicode characters
          were used when creating the record.

        Args:
          zone_id: Identifier

          comment: Comments or notes about the DNS record. This field has no effect on DNS
              responses.

          content: Text content for the record. The content must consist of quoted "character
              strings" (RFC 1035), each with a length of up to 255 bytes. Strings exceeding
              this allowed maximum length are automatically split.

              Learn more at
              <https://www.cloudflare.com/learning/dns/dns-records/dns-txt-record/>.

          name: DNS record name (or @ for the zone apex) in Punycode.

          proxied: Whether the record is receiving the performance and security benefits of
              Cloudflare.

          settings: Settings for the DNS record.

          tags: Custom tags for the DNS record. This field has no effect on DNS responses.

          ttl: Time To Live (TTL) of the DNS record in seconds. Setting to 1 means 'automatic'.
              Value must be between 60 and 86400, with the minimum reduced to 30 for
              Enterprise zones.

          type: Record type.

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
        comment: str | NotGiven = NOT_GIVEN,
        data: record_create_params.URIRecordData | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        priority: float | NotGiven = NOT_GIVEN,
        proxied: bool | NotGiven = NOT_GIVEN,
        settings: record_create_params.URIRecordSettings | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        type: Literal["URI"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[RecordResponse]:
        """
        Create a new DNS record for a zone.

        Notes:

        - A/AAAA records cannot exist on the same name as CNAME records.
        - NS records cannot exist on the same name as any other record type.
        - Domain names are always represented in Punycode, even if Unicode characters
          were used when creating the record.

        Args:
          zone_id: Identifier

          comment: Comments or notes about the DNS record. This field has no effect on DNS
              responses.

          data: Components of a URI record.

          name: DNS record name (or @ for the zone apex) in Punycode.

          priority: Required for MX, SRV and URI records; unused by other record types. Records with
              lower priorities are preferred.

          proxied: Whether the record is receiving the performance and security benefits of
              Cloudflare.

          settings: Settings for the DNS record.

          tags: Custom tags for the DNS record. This field has no effect on DNS responses.

          ttl: Time To Live (TTL) of the DNS record in seconds. Setting to 1 means 'automatic'.
              Value must be between 60 and 86400, with the minimum reduced to 30 for
              Enterprise zones.

          type: Record type.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["zone_id"])
    def create(
        self,
        *,
        zone_id: str,
        comment: str | NotGiven = NOT_GIVEN,
        content: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        proxied: bool | NotGiven = NOT_GIVEN,
        settings: record_create_params.ARecordSettings
        | record_create_params.CNAMERecordSettings
        | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
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
        | Literal["URI"]
        | NotGiven = NOT_GIVEN,
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
    ) -> Optional[RecordResponse]:
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return cast(
            Optional[RecordResponse],
            self._post(
                f"/zones/{zone_id}/dns_records",
                body=maybe_transform(
                    {
                        "comment": comment,
                        "content": content,
                        "name": name,
                        "proxied": proxied,
                        "settings": settings,
                        "tags": tags,
                        "ttl": ttl,
                        "type": type,
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
                    post_parser=ResultWrapper[Optional[RecordResponse]]._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[RecordResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    @overload
    def update(
        self,
        dns_record_id: str,
        *,
        zone_id: str,
        comment: str | NotGiven = NOT_GIVEN,
        content: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        proxied: bool | NotGiven = NOT_GIVEN,
        settings: record_update_params.ARecordSettings | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        type: Literal["A"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[RecordResponse]:
        """
        Overwrite an existing DNS record.

        Notes:

        - A/AAAA records cannot exist on the same name as CNAME records.
        - NS records cannot exist on the same name as any other record type.
        - Domain names are always represented in Punycode, even if Unicode characters
          were used when creating the record.

        Args:
          zone_id: Identifier

          dns_record_id: Identifier

          comment: Comments or notes about the DNS record. This field has no effect on DNS
              responses.

          content: A valid IPv4 address.

          name: DNS record name (or @ for the zone apex) in Punycode.

          proxied: Whether the record is receiving the performance and security benefits of
              Cloudflare.

          settings: Settings for the DNS record.

          tags: Custom tags for the DNS record. This field has no effect on DNS responses.

          ttl: Time To Live (TTL) of the DNS record in seconds. Setting to 1 means 'automatic'.
              Value must be between 60 and 86400, with the minimum reduced to 30 for
              Enterprise zones.

          type: Record type.

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
        comment: str | NotGiven = NOT_GIVEN,
        content: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        proxied: bool | NotGiven = NOT_GIVEN,
        settings: record_update_params.AAAARecordSettings | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        type: Literal["AAAA"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[RecordResponse]:
        """
        Overwrite an existing DNS record.

        Notes:

        - A/AAAA records cannot exist on the same name as CNAME records.
        - NS records cannot exist on the same name as any other record type.
        - Domain names are always represented in Punycode, even if Unicode characters
          were used when creating the record.

        Args:
          zone_id: Identifier

          dns_record_id: Identifier

          comment: Comments or notes about the DNS record. This field has no effect on DNS
              responses.

          content: A valid IPv6 address.

          name: DNS record name (or @ for the zone apex) in Punycode.

          proxied: Whether the record is receiving the performance and security benefits of
              Cloudflare.

          settings: Settings for the DNS record.

          tags: Custom tags for the DNS record. This field has no effect on DNS responses.

          ttl: Time To Live (TTL) of the DNS record in seconds. Setting to 1 means 'automatic'.
              Value must be between 60 and 86400, with the minimum reduced to 30 for
              Enterprise zones.

          type: Record type.

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
        comment: str | NotGiven = NOT_GIVEN,
        data: record_update_params.CAARecordData | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        proxied: bool | NotGiven = NOT_GIVEN,
        settings: record_update_params.CAARecordSettings | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        type: Literal["CAA"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[RecordResponse]:
        """
        Overwrite an existing DNS record.

        Notes:

        - A/AAAA records cannot exist on the same name as CNAME records.
        - NS records cannot exist on the same name as any other record type.
        - Domain names are always represented in Punycode, even if Unicode characters
          were used when creating the record.

        Args:
          zone_id: Identifier

          dns_record_id: Identifier

          comment: Comments or notes about the DNS record. This field has no effect on DNS
              responses.

          data: Components of a CAA record.

          name: DNS record name (or @ for the zone apex) in Punycode.

          proxied: Whether the record is receiving the performance and security benefits of
              Cloudflare.

          settings: Settings for the DNS record.

          tags: Custom tags for the DNS record. This field has no effect on DNS responses.

          ttl: Time To Live (TTL) of the DNS record in seconds. Setting to 1 means 'automatic'.
              Value must be between 60 and 86400, with the minimum reduced to 30 for
              Enterprise zones.

          type: Record type.

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
        comment: str | NotGiven = NOT_GIVEN,
        data: record_update_params.CERTRecordData | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        proxied: bool | NotGiven = NOT_GIVEN,
        settings: record_update_params.CERTRecordSettings | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        type: Literal["CERT"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[RecordResponse]:
        """
        Overwrite an existing DNS record.

        Notes:

        - A/AAAA records cannot exist on the same name as CNAME records.
        - NS records cannot exist on the same name as any other record type.
        - Domain names are always represented in Punycode, even if Unicode characters
          were used when creating the record.

        Args:
          zone_id: Identifier

          dns_record_id: Identifier

          comment: Comments or notes about the DNS record. This field has no effect on DNS
              responses.

          data: Components of a CERT record.

          name: DNS record name (or @ for the zone apex) in Punycode.

          proxied: Whether the record is receiving the performance and security benefits of
              Cloudflare.

          settings: Settings for the DNS record.

          tags: Custom tags for the DNS record. This field has no effect on DNS responses.

          ttl: Time To Live (TTL) of the DNS record in seconds. Setting to 1 means 'automatic'.
              Value must be between 60 and 86400, with the minimum reduced to 30 for
              Enterprise zones.

          type: Record type.

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
        comment: str | NotGiven = NOT_GIVEN,
        content: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        proxied: bool | NotGiven = NOT_GIVEN,
        settings: record_update_params.CNAMERecordSettings | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        type: Literal["CNAME"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[RecordResponse]:
        """
        Overwrite an existing DNS record.

        Notes:

        - A/AAAA records cannot exist on the same name as CNAME records.
        - NS records cannot exist on the same name as any other record type.
        - Domain names are always represented in Punycode, even if Unicode characters
          were used when creating the record.

        Args:
          zone_id: Identifier

          dns_record_id: Identifier

          comment: Comments or notes about the DNS record. This field has no effect on DNS
              responses.

          content: A valid hostname. Must not match the record's name.

          name: DNS record name (or @ for the zone apex) in Punycode.

          proxied: Whether the record is receiving the performance and security benefits of
              Cloudflare.

          settings: Settings for the DNS record.

          tags: Custom tags for the DNS record. This field has no effect on DNS responses.

          ttl: Time To Live (TTL) of the DNS record in seconds. Setting to 1 means 'automatic'.
              Value must be between 60 and 86400, with the minimum reduced to 30 for
              Enterprise zones.

          type: Record type.

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
        comment: str | NotGiven = NOT_GIVEN,
        data: record_update_params.DNSKEYRecordData | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        proxied: bool | NotGiven = NOT_GIVEN,
        settings: record_update_params.DNSKEYRecordSettings | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        type: Literal["DNSKEY"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[RecordResponse]:
        """
        Overwrite an existing DNS record.

        Notes:

        - A/AAAA records cannot exist on the same name as CNAME records.
        - NS records cannot exist on the same name as any other record type.
        - Domain names are always represented in Punycode, even if Unicode characters
          were used when creating the record.

        Args:
          zone_id: Identifier

          dns_record_id: Identifier

          comment: Comments or notes about the DNS record. This field has no effect on DNS
              responses.

          data: Components of a DNSKEY record.

          name: DNS record name (or @ for the zone apex) in Punycode.

          proxied: Whether the record is receiving the performance and security benefits of
              Cloudflare.

          settings: Settings for the DNS record.

          tags: Custom tags for the DNS record. This field has no effect on DNS responses.

          ttl: Time To Live (TTL) of the DNS record in seconds. Setting to 1 means 'automatic'.
              Value must be between 60 and 86400, with the minimum reduced to 30 for
              Enterprise zones.

          type: Record type.

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
        comment: str | NotGiven = NOT_GIVEN,
        data: record_update_params.DSRecordData | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        proxied: bool | NotGiven = NOT_GIVEN,
        settings: record_update_params.DSRecordSettings | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        type: Literal["DS"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[RecordResponse]:
        """
        Overwrite an existing DNS record.

        Notes:

        - A/AAAA records cannot exist on the same name as CNAME records.
        - NS records cannot exist on the same name as any other record type.
        - Domain names are always represented in Punycode, even if Unicode characters
          were used when creating the record.

        Args:
          zone_id: Identifier

          dns_record_id: Identifier

          comment: Comments or notes about the DNS record. This field has no effect on DNS
              responses.

          data: Components of a DS record.

          name: DNS record name (or @ for the zone apex) in Punycode.

          proxied: Whether the record is receiving the performance and security benefits of
              Cloudflare.

          settings: Settings for the DNS record.

          tags: Custom tags for the DNS record. This field has no effect on DNS responses.

          ttl: Time To Live (TTL) of the DNS record in seconds. Setting to 1 means 'automatic'.
              Value must be between 60 and 86400, with the minimum reduced to 30 for
              Enterprise zones.

          type: Record type.

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
        comment: str | NotGiven = NOT_GIVEN,
        data: record_update_params.HTTPSRecordData | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        proxied: bool | NotGiven = NOT_GIVEN,
        settings: record_update_params.HTTPSRecordSettings | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        type: Literal["HTTPS"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[RecordResponse]:
        """
        Overwrite an existing DNS record.

        Notes:

        - A/AAAA records cannot exist on the same name as CNAME records.
        - NS records cannot exist on the same name as any other record type.
        - Domain names are always represented in Punycode, even if Unicode characters
          were used when creating the record.

        Args:
          zone_id: Identifier

          dns_record_id: Identifier

          comment: Comments or notes about the DNS record. This field has no effect on DNS
              responses.

          data: Components of a HTTPS record.

          name: DNS record name (or @ for the zone apex) in Punycode.

          proxied: Whether the record is receiving the performance and security benefits of
              Cloudflare.

          settings: Settings for the DNS record.

          tags: Custom tags for the DNS record. This field has no effect on DNS responses.

          ttl: Time To Live (TTL) of the DNS record in seconds. Setting to 1 means 'automatic'.
              Value must be between 60 and 86400, with the minimum reduced to 30 for
              Enterprise zones.

          type: Record type.

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
        comment: str | NotGiven = NOT_GIVEN,
        data: record_update_params.LOCRecordData | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        proxied: bool | NotGiven = NOT_GIVEN,
        settings: record_update_params.LOCRecordSettings | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        type: Literal["LOC"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[RecordResponse]:
        """
        Overwrite an existing DNS record.

        Notes:

        - A/AAAA records cannot exist on the same name as CNAME records.
        - NS records cannot exist on the same name as any other record type.
        - Domain names are always represented in Punycode, even if Unicode characters
          were used when creating the record.

        Args:
          zone_id: Identifier

          dns_record_id: Identifier

          comment: Comments or notes about the DNS record. This field has no effect on DNS
              responses.

          data: Components of a LOC record.

          name: DNS record name (or @ for the zone apex) in Punycode.

          proxied: Whether the record is receiving the performance and security benefits of
              Cloudflare.

          settings: Settings for the DNS record.

          tags: Custom tags for the DNS record. This field has no effect on DNS responses.

          ttl: Time To Live (TTL) of the DNS record in seconds. Setting to 1 means 'automatic'.
              Value must be between 60 and 86400, with the minimum reduced to 30 for
              Enterprise zones.

          type: Record type.

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
        comment: str | NotGiven = NOT_GIVEN,
        content: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        priority: float | NotGiven = NOT_GIVEN,
        proxied: bool | NotGiven = NOT_GIVEN,
        settings: record_update_params.MXRecordSettings | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        type: Literal["MX"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[RecordResponse]:
        """
        Overwrite an existing DNS record.

        Notes:

        - A/AAAA records cannot exist on the same name as CNAME records.
        - NS records cannot exist on the same name as any other record type.
        - Domain names are always represented in Punycode, even if Unicode characters
          were used when creating the record.

        Args:
          zone_id: Identifier

          dns_record_id: Identifier

          comment: Comments or notes about the DNS record. This field has no effect on DNS
              responses.

          content: A valid mail server hostname.

          name: DNS record name (or @ for the zone apex) in Punycode.

          priority: Required for MX, SRV and URI records; unused by other record types. Records with
              lower priorities are preferred.

          proxied: Whether the record is receiving the performance and security benefits of
              Cloudflare.

          settings: Settings for the DNS record.

          tags: Custom tags for the DNS record. This field has no effect on DNS responses.

          ttl: Time To Live (TTL) of the DNS record in seconds. Setting to 1 means 'automatic'.
              Value must be between 60 and 86400, with the minimum reduced to 30 for
              Enterprise zones.

          type: Record type.

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
        comment: str | NotGiven = NOT_GIVEN,
        data: record_update_params.NAPTRRecordData | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        proxied: bool | NotGiven = NOT_GIVEN,
        settings: record_update_params.NAPTRRecordSettings | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        type: Literal["NAPTR"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[RecordResponse]:
        """
        Overwrite an existing DNS record.

        Notes:

        - A/AAAA records cannot exist on the same name as CNAME records.
        - NS records cannot exist on the same name as any other record type.
        - Domain names are always represented in Punycode, even if Unicode characters
          were used when creating the record.

        Args:
          zone_id: Identifier

          dns_record_id: Identifier

          comment: Comments or notes about the DNS record. This field has no effect on DNS
              responses.

          data: Components of a NAPTR record.

          name: DNS record name (or @ for the zone apex) in Punycode.

          proxied: Whether the record is receiving the performance and security benefits of
              Cloudflare.

          settings: Settings for the DNS record.

          tags: Custom tags for the DNS record. This field has no effect on DNS responses.

          ttl: Time To Live (TTL) of the DNS record in seconds. Setting to 1 means 'automatic'.
              Value must be between 60 and 86400, with the minimum reduced to 30 for
              Enterprise zones.

          type: Record type.

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
        comment: str | NotGiven = NOT_GIVEN,
        content: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        proxied: bool | NotGiven = NOT_GIVEN,
        settings: record_update_params.NSRecordSettings | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        type: Literal["NS"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[RecordResponse]:
        """
        Overwrite an existing DNS record.

        Notes:

        - A/AAAA records cannot exist on the same name as CNAME records.
        - NS records cannot exist on the same name as any other record type.
        - Domain names are always represented in Punycode, even if Unicode characters
          were used when creating the record.

        Args:
          zone_id: Identifier

          dns_record_id: Identifier

          comment: Comments or notes about the DNS record. This field has no effect on DNS
              responses.

          content: A valid name server host name.

          name: DNS record name (or @ for the zone apex) in Punycode.

          proxied: Whether the record is receiving the performance and security benefits of
              Cloudflare.

          settings: Settings for the DNS record.

          tags: Custom tags for the DNS record. This field has no effect on DNS responses.

          ttl: Time To Live (TTL) of the DNS record in seconds. Setting to 1 means 'automatic'.
              Value must be between 60 and 86400, with the minimum reduced to 30 for
              Enterprise zones.

          type: Record type.

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
        comment: str | NotGiven = NOT_GIVEN,
        content: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        proxied: bool | NotGiven = NOT_GIVEN,
        settings: record_update_params.DNSRecordsOpenpgpkeyRecordSettings | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        type: Literal["OPENPGPKEY"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[RecordResponse]:
        """
        Overwrite an existing DNS record.

        Notes:

        - A/AAAA records cannot exist on the same name as CNAME records.
        - NS records cannot exist on the same name as any other record type.
        - Domain names are always represented in Punycode, even if Unicode characters
          were used when creating the record.

        Args:
          zone_id: Identifier

          dns_record_id: Identifier

          comment: Comments or notes about the DNS record. This field has no effect on DNS
              responses.

          content: A single Base64-encoded OpenPGP Transferable Public Key (RFC 4880 Section 11.1)

          name: DNS record name (or @ for the zone apex) in Punycode.

          proxied: Whether the record is receiving the performance and security benefits of
              Cloudflare.

          settings: Settings for the DNS record.

          tags: Custom tags for the DNS record. This field has no effect on DNS responses.

          ttl: Time To Live (TTL) of the DNS record in seconds. Setting to 1 means 'automatic'.
              Value must be between 60 and 86400, with the minimum reduced to 30 for
              Enterprise zones.

          type: Record type.

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
        comment: str | NotGiven = NOT_GIVEN,
        content: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        proxied: bool | NotGiven = NOT_GIVEN,
        settings: record_update_params.PTRRecordSettings | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        type: Literal["PTR"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[RecordResponse]:
        """
        Overwrite an existing DNS record.

        Notes:

        - A/AAAA records cannot exist on the same name as CNAME records.
        - NS records cannot exist on the same name as any other record type.
        - Domain names are always represented in Punycode, even if Unicode characters
          were used when creating the record.

        Args:
          zone_id: Identifier

          dns_record_id: Identifier

          comment: Comments or notes about the DNS record. This field has no effect on DNS
              responses.

          content: Domain name pointing to the address.

          name: DNS record name (or @ for the zone apex) in Punycode.

          proxied: Whether the record is receiving the performance and security benefits of
              Cloudflare.

          settings: Settings for the DNS record.

          tags: Custom tags for the DNS record. This field has no effect on DNS responses.

          ttl: Time To Live (TTL) of the DNS record in seconds. Setting to 1 means 'automatic'.
              Value must be between 60 and 86400, with the minimum reduced to 30 for
              Enterprise zones.

          type: Record type.

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
        comment: str | NotGiven = NOT_GIVEN,
        data: record_update_params.SMIMEARecordData | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        proxied: bool | NotGiven = NOT_GIVEN,
        settings: record_update_params.SMIMEARecordSettings | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        type: Literal["SMIMEA"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[RecordResponse]:
        """
        Overwrite an existing DNS record.

        Notes:

        - A/AAAA records cannot exist on the same name as CNAME records.
        - NS records cannot exist on the same name as any other record type.
        - Domain names are always represented in Punycode, even if Unicode characters
          were used when creating the record.

        Args:
          zone_id: Identifier

          dns_record_id: Identifier

          comment: Comments or notes about the DNS record. This field has no effect on DNS
              responses.

          data: Components of a SMIMEA record.

          name: DNS record name (or @ for the zone apex) in Punycode.

          proxied: Whether the record is receiving the performance and security benefits of
              Cloudflare.

          settings: Settings for the DNS record.

          tags: Custom tags for the DNS record. This field has no effect on DNS responses.

          ttl: Time To Live (TTL) of the DNS record in seconds. Setting to 1 means 'automatic'.
              Value must be between 60 and 86400, with the minimum reduced to 30 for
              Enterprise zones.

          type: Record type.

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
        comment: str | NotGiven = NOT_GIVEN,
        data: record_update_params.SRVRecordData | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        proxied: bool | NotGiven = NOT_GIVEN,
        settings: record_update_params.SRVRecordSettings | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        type: Literal["SRV"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[RecordResponse]:
        """
        Overwrite an existing DNS record.

        Notes:

        - A/AAAA records cannot exist on the same name as CNAME records.
        - NS records cannot exist on the same name as any other record type.
        - Domain names are always represented in Punycode, even if Unicode characters
          were used when creating the record.

        Args:
          zone_id: Identifier

          dns_record_id: Identifier

          comment: Comments or notes about the DNS record. This field has no effect on DNS
              responses.

          data: Components of a SRV record.

          name: DNS record name (or @ for the zone apex) in Punycode.

          proxied: Whether the record is receiving the performance and security benefits of
              Cloudflare.

          settings: Settings for the DNS record.

          tags: Custom tags for the DNS record. This field has no effect on DNS responses.

          ttl: Time To Live (TTL) of the DNS record in seconds. Setting to 1 means 'automatic'.
              Value must be between 60 and 86400, with the minimum reduced to 30 for
              Enterprise zones.

          type: Record type.

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
        comment: str | NotGiven = NOT_GIVEN,
        data: record_update_params.SSHFPRecordData | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        proxied: bool | NotGiven = NOT_GIVEN,
        settings: record_update_params.SSHFPRecordSettings | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        type: Literal["SSHFP"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[RecordResponse]:
        """
        Overwrite an existing DNS record.

        Notes:

        - A/AAAA records cannot exist on the same name as CNAME records.
        - NS records cannot exist on the same name as any other record type.
        - Domain names are always represented in Punycode, even if Unicode characters
          were used when creating the record.

        Args:
          zone_id: Identifier

          dns_record_id: Identifier

          comment: Comments or notes about the DNS record. This field has no effect on DNS
              responses.

          data: Components of a SSHFP record.

          name: DNS record name (or @ for the zone apex) in Punycode.

          proxied: Whether the record is receiving the performance and security benefits of
              Cloudflare.

          settings: Settings for the DNS record.

          tags: Custom tags for the DNS record. This field has no effect on DNS responses.

          ttl: Time To Live (TTL) of the DNS record in seconds. Setting to 1 means 'automatic'.
              Value must be between 60 and 86400, with the minimum reduced to 30 for
              Enterprise zones.

          type: Record type.

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
        comment: str | NotGiven = NOT_GIVEN,
        data: record_update_params.SVCBRecordData | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        proxied: bool | NotGiven = NOT_GIVEN,
        settings: record_update_params.SVCBRecordSettings | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        type: Literal["SVCB"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[RecordResponse]:
        """
        Overwrite an existing DNS record.

        Notes:

        - A/AAAA records cannot exist on the same name as CNAME records.
        - NS records cannot exist on the same name as any other record type.
        - Domain names are always represented in Punycode, even if Unicode characters
          were used when creating the record.

        Args:
          zone_id: Identifier

          dns_record_id: Identifier

          comment: Comments or notes about the DNS record. This field has no effect on DNS
              responses.

          data: Components of a SVCB record.

          name: DNS record name (or @ for the zone apex) in Punycode.

          proxied: Whether the record is receiving the performance and security benefits of
              Cloudflare.

          settings: Settings for the DNS record.

          tags: Custom tags for the DNS record. This field has no effect on DNS responses.

          ttl: Time To Live (TTL) of the DNS record in seconds. Setting to 1 means 'automatic'.
              Value must be between 60 and 86400, with the minimum reduced to 30 for
              Enterprise zones.

          type: Record type.

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
        comment: str | NotGiven = NOT_GIVEN,
        data: record_update_params.TLSARecordData | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        proxied: bool | NotGiven = NOT_GIVEN,
        settings: record_update_params.TLSARecordSettings | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        type: Literal["TLSA"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[RecordResponse]:
        """
        Overwrite an existing DNS record.

        Notes:

        - A/AAAA records cannot exist on the same name as CNAME records.
        - NS records cannot exist on the same name as any other record type.
        - Domain names are always represented in Punycode, even if Unicode characters
          were used when creating the record.

        Args:
          zone_id: Identifier

          dns_record_id: Identifier

          comment: Comments or notes about the DNS record. This field has no effect on DNS
              responses.

          data: Components of a TLSA record.

          name: DNS record name (or @ for the zone apex) in Punycode.

          proxied: Whether the record is receiving the performance and security benefits of
              Cloudflare.

          settings: Settings for the DNS record.

          tags: Custom tags for the DNS record. This field has no effect on DNS responses.

          ttl: Time To Live (TTL) of the DNS record in seconds. Setting to 1 means 'automatic'.
              Value must be between 60 and 86400, with the minimum reduced to 30 for
              Enterprise zones.

          type: Record type.

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
        comment: str | NotGiven = NOT_GIVEN,
        content: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        proxied: bool | NotGiven = NOT_GIVEN,
        settings: record_update_params.TXTRecordSettings | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        type: Literal["TXT"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[RecordResponse]:
        """
        Overwrite an existing DNS record.

        Notes:

        - A/AAAA records cannot exist on the same name as CNAME records.
        - NS records cannot exist on the same name as any other record type.
        - Domain names are always represented in Punycode, even if Unicode characters
          were used when creating the record.

        Args:
          zone_id: Identifier

          dns_record_id: Identifier

          comment: Comments or notes about the DNS record. This field has no effect on DNS
              responses.

          content: Text content for the record. The content must consist of quoted "character
              strings" (RFC 1035), each with a length of up to 255 bytes. Strings exceeding
              this allowed maximum length are automatically split.

              Learn more at
              <https://www.cloudflare.com/learning/dns/dns-records/dns-txt-record/>.

          name: DNS record name (or @ for the zone apex) in Punycode.

          proxied: Whether the record is receiving the performance and security benefits of
              Cloudflare.

          settings: Settings for the DNS record.

          tags: Custom tags for the DNS record. This field has no effect on DNS responses.

          ttl: Time To Live (TTL) of the DNS record in seconds. Setting to 1 means 'automatic'.
              Value must be between 60 and 86400, with the minimum reduced to 30 for
              Enterprise zones.

          type: Record type.

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
        comment: str | NotGiven = NOT_GIVEN,
        data: record_update_params.URIRecordData | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        priority: float | NotGiven = NOT_GIVEN,
        proxied: bool | NotGiven = NOT_GIVEN,
        settings: record_update_params.URIRecordSettings | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        type: Literal["URI"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[RecordResponse]:
        """
        Overwrite an existing DNS record.

        Notes:

        - A/AAAA records cannot exist on the same name as CNAME records.
        - NS records cannot exist on the same name as any other record type.
        - Domain names are always represented in Punycode, even if Unicode characters
          were used when creating the record.

        Args:
          zone_id: Identifier

          dns_record_id: Identifier

          comment: Comments or notes about the DNS record. This field has no effect on DNS
              responses.

          data: Components of a URI record.

          name: DNS record name (or @ for the zone apex) in Punycode.

          priority: Required for MX, SRV and URI records; unused by other record types. Records with
              lower priorities are preferred.

          proxied: Whether the record is receiving the performance and security benefits of
              Cloudflare.

          settings: Settings for the DNS record.

          tags: Custom tags for the DNS record. This field has no effect on DNS responses.

          ttl: Time To Live (TTL) of the DNS record in seconds. Setting to 1 means 'automatic'.
              Value must be between 60 and 86400, with the minimum reduced to 30 for
              Enterprise zones.

          type: Record type.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["zone_id"])
    def update(
        self,
        dns_record_id: str,
        *,
        zone_id: str,
        comment: str | NotGiven = NOT_GIVEN,
        content: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        proxied: bool | NotGiven = NOT_GIVEN,
        settings: record_update_params.ARecordSettings
        | record_update_params.CNAMERecordSettings
        | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
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
        | Literal["URI"]
        | NotGiven = NOT_GIVEN,
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
    ) -> Optional[RecordResponse]:
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not dns_record_id:
            raise ValueError(f"Expected a non-empty value for `dns_record_id` but received {dns_record_id!r}")
        return cast(
            Optional[RecordResponse],
            self._put(
                f"/zones/{zone_id}/dns_records/{dns_record_id}",
                body=maybe_transform(
                    {
                        "comment": comment,
                        "content": content,
                        "name": name,
                        "proxied": proxied,
                        "settings": settings,
                        "tags": tags,
                        "ttl": ttl,
                        "type": type,
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
                    post_parser=ResultWrapper[Optional[RecordResponse]]._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[RecordResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def list(
        self,
        *,
        zone_id: str,
        comment: record_list_params.Comment | NotGiven = NOT_GIVEN,
        content: record_list_params.Content | NotGiven = NOT_GIVEN,
        direction: SortDirection | NotGiven = NOT_GIVEN,
        match: Literal["any", "all"] | NotGiven = NOT_GIVEN,
        name: record_list_params.Name | NotGiven = NOT_GIVEN,
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
    ) -> SyncV4PagePaginationArray[RecordResponse]:
        """
        List, search, sort, and filter a zones' DNS records.

        Args:
          zone_id: Identifier

          direction: Direction to order DNS records in.

          match: Whether to match all search requirements or at least one (any). If set to `all`,
              acts like a logical AND between filters. If set to `any`, acts like a logical OR
              instead. Note that the interaction between tag filters is controlled by the
              `tag-match` parameter instead.

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
            page=SyncV4PagePaginationArray[RecordResponse],
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
            model=cast(Any, RecordResponse),  # Union types cannot be passed in as arguments in the type system
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

    def batch(
        self,
        *,
        zone_id: str,
        deletes: Iterable[record_batch_params.Delete] | NotGiven = NOT_GIVEN,
        patches: Iterable[BatchPatchParam] | NotGiven = NOT_GIVEN,
        posts: Iterable[RecordParam] | NotGiven = NOT_GIVEN,
        puts: Iterable[BatchPutParam] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[RecordBatchResponse]:
        """
        Send a Batch of DNS Record API calls to be executed together.

        Notes:

        - Although Cloudflare will execute the batched operations in a single database
          transaction, Cloudflare's distributed KV store must treat each record change
          as a single key-value pair. This means that the propagation of changes is not
          atomic. See
          [the documentation](https://developers.cloudflare.com/dns/manage-dns-records/how-to/batch-record-changes/ "Batch DNS records")
          for more information.
        - The operations you specify within the /batch request body are always executed
          in the following order:

          - Deletes
          - Patches
          - Puts
          - Posts

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
            f"/zones/{zone_id}/dns_records/batch",
            body=maybe_transform(
                {
                    "deletes": deletes,
                    "patches": patches,
                    "posts": posts,
                    "puts": puts,
                },
                record_batch_params.RecordBatchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[RecordBatchResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[RecordBatchResponse]], ResultWrapper[RecordBatchResponse]),
        )

    @overload
    def edit(
        self,
        dns_record_id: str,
        *,
        zone_id: str,
        comment: str | NotGiven = NOT_GIVEN,
        content: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        proxied: bool | NotGiven = NOT_GIVEN,
        settings: record_edit_params.ARecordSettings | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        type: Literal["A"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[RecordResponse]:
        """
        Update an existing DNS record.

        Notes:

        - A/AAAA records cannot exist on the same name as CNAME records.
        - NS records cannot exist on the same name as any other record type.
        - Domain names are always represented in Punycode, even if Unicode characters
          were used when creating the record.

        Args:
          zone_id: Identifier

          dns_record_id: Identifier

          comment: Comments or notes about the DNS record. This field has no effect on DNS
              responses.

          content: A valid IPv4 address.

          name: DNS record name (or @ for the zone apex) in Punycode.

          proxied: Whether the record is receiving the performance and security benefits of
              Cloudflare.

          settings: Settings for the DNS record.

          tags: Custom tags for the DNS record. This field has no effect on DNS responses.

          ttl: Time To Live (TTL) of the DNS record in seconds. Setting to 1 means 'automatic'.
              Value must be between 60 and 86400, with the minimum reduced to 30 for
              Enterprise zones.

          type: Record type.

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
        comment: str | NotGiven = NOT_GIVEN,
        content: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        proxied: bool | NotGiven = NOT_GIVEN,
        settings: record_edit_params.AAAARecordSettings | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        type: Literal["AAAA"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[RecordResponse]:
        """
        Update an existing DNS record.

        Notes:

        - A/AAAA records cannot exist on the same name as CNAME records.
        - NS records cannot exist on the same name as any other record type.
        - Domain names are always represented in Punycode, even if Unicode characters
          were used when creating the record.

        Args:
          zone_id: Identifier

          dns_record_id: Identifier

          comment: Comments or notes about the DNS record. This field has no effect on DNS
              responses.

          content: A valid IPv6 address.

          name: DNS record name (or @ for the zone apex) in Punycode.

          proxied: Whether the record is receiving the performance and security benefits of
              Cloudflare.

          settings: Settings for the DNS record.

          tags: Custom tags for the DNS record. This field has no effect on DNS responses.

          ttl: Time To Live (TTL) of the DNS record in seconds. Setting to 1 means 'automatic'.
              Value must be between 60 and 86400, with the minimum reduced to 30 for
              Enterprise zones.

          type: Record type.

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
        comment: str | NotGiven = NOT_GIVEN,
        data: record_edit_params.CAARecordData | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        proxied: bool | NotGiven = NOT_GIVEN,
        settings: record_edit_params.CAARecordSettings | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        type: Literal["CAA"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[RecordResponse]:
        """
        Update an existing DNS record.

        Notes:

        - A/AAAA records cannot exist on the same name as CNAME records.
        - NS records cannot exist on the same name as any other record type.
        - Domain names are always represented in Punycode, even if Unicode characters
          were used when creating the record.

        Args:
          zone_id: Identifier

          dns_record_id: Identifier

          comment: Comments or notes about the DNS record. This field has no effect on DNS
              responses.

          data: Components of a CAA record.

          name: DNS record name (or @ for the zone apex) in Punycode.

          proxied: Whether the record is receiving the performance and security benefits of
              Cloudflare.

          settings: Settings for the DNS record.

          tags: Custom tags for the DNS record. This field has no effect on DNS responses.

          ttl: Time To Live (TTL) of the DNS record in seconds. Setting to 1 means 'automatic'.
              Value must be between 60 and 86400, with the minimum reduced to 30 for
              Enterprise zones.

          type: Record type.

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
        comment: str | NotGiven = NOT_GIVEN,
        data: record_edit_params.CERTRecordData | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        proxied: bool | NotGiven = NOT_GIVEN,
        settings: record_edit_params.CERTRecordSettings | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        type: Literal["CERT"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[RecordResponse]:
        """
        Update an existing DNS record.

        Notes:

        - A/AAAA records cannot exist on the same name as CNAME records.
        - NS records cannot exist on the same name as any other record type.
        - Domain names are always represented in Punycode, even if Unicode characters
          were used when creating the record.

        Args:
          zone_id: Identifier

          dns_record_id: Identifier

          comment: Comments or notes about the DNS record. This field has no effect on DNS
              responses.

          data: Components of a CERT record.

          name: DNS record name (or @ for the zone apex) in Punycode.

          proxied: Whether the record is receiving the performance and security benefits of
              Cloudflare.

          settings: Settings for the DNS record.

          tags: Custom tags for the DNS record. This field has no effect on DNS responses.

          ttl: Time To Live (TTL) of the DNS record in seconds. Setting to 1 means 'automatic'.
              Value must be between 60 and 86400, with the minimum reduced to 30 for
              Enterprise zones.

          type: Record type.

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
        comment: str | NotGiven = NOT_GIVEN,
        content: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        proxied: bool | NotGiven = NOT_GIVEN,
        settings: record_edit_params.CNAMERecordSettings | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        type: Literal["CNAME"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[RecordResponse]:
        """
        Update an existing DNS record.

        Notes:

        - A/AAAA records cannot exist on the same name as CNAME records.
        - NS records cannot exist on the same name as any other record type.
        - Domain names are always represented in Punycode, even if Unicode characters
          were used when creating the record.

        Args:
          zone_id: Identifier

          dns_record_id: Identifier

          comment: Comments or notes about the DNS record. This field has no effect on DNS
              responses.

          content: A valid hostname. Must not match the record's name.

          name: DNS record name (or @ for the zone apex) in Punycode.

          proxied: Whether the record is receiving the performance and security benefits of
              Cloudflare.

          settings: Settings for the DNS record.

          tags: Custom tags for the DNS record. This field has no effect on DNS responses.

          ttl: Time To Live (TTL) of the DNS record in seconds. Setting to 1 means 'automatic'.
              Value must be between 60 and 86400, with the minimum reduced to 30 for
              Enterprise zones.

          type: Record type.

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
        comment: str | NotGiven = NOT_GIVEN,
        data: record_edit_params.DNSKEYRecordData | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        proxied: bool | NotGiven = NOT_GIVEN,
        settings: record_edit_params.DNSKEYRecordSettings | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        type: Literal["DNSKEY"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[RecordResponse]:
        """
        Update an existing DNS record.

        Notes:

        - A/AAAA records cannot exist on the same name as CNAME records.
        - NS records cannot exist on the same name as any other record type.
        - Domain names are always represented in Punycode, even if Unicode characters
          were used when creating the record.

        Args:
          zone_id: Identifier

          dns_record_id: Identifier

          comment: Comments or notes about the DNS record. This field has no effect on DNS
              responses.

          data: Components of a DNSKEY record.

          name: DNS record name (or @ for the zone apex) in Punycode.

          proxied: Whether the record is receiving the performance and security benefits of
              Cloudflare.

          settings: Settings for the DNS record.

          tags: Custom tags for the DNS record. This field has no effect on DNS responses.

          ttl: Time To Live (TTL) of the DNS record in seconds. Setting to 1 means 'automatic'.
              Value must be between 60 and 86400, with the minimum reduced to 30 for
              Enterprise zones.

          type: Record type.

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
        comment: str | NotGiven = NOT_GIVEN,
        data: record_edit_params.DSRecordData | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        proxied: bool | NotGiven = NOT_GIVEN,
        settings: record_edit_params.DSRecordSettings | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        type: Literal["DS"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[RecordResponse]:
        """
        Update an existing DNS record.

        Notes:

        - A/AAAA records cannot exist on the same name as CNAME records.
        - NS records cannot exist on the same name as any other record type.
        - Domain names are always represented in Punycode, even if Unicode characters
          were used when creating the record.

        Args:
          zone_id: Identifier

          dns_record_id: Identifier

          comment: Comments or notes about the DNS record. This field has no effect on DNS
              responses.

          data: Components of a DS record.

          name: DNS record name (or @ for the zone apex) in Punycode.

          proxied: Whether the record is receiving the performance and security benefits of
              Cloudflare.

          settings: Settings for the DNS record.

          tags: Custom tags for the DNS record. This field has no effect on DNS responses.

          ttl: Time To Live (TTL) of the DNS record in seconds. Setting to 1 means 'automatic'.
              Value must be between 60 and 86400, with the minimum reduced to 30 for
              Enterprise zones.

          type: Record type.

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
        comment: str | NotGiven = NOT_GIVEN,
        data: record_edit_params.HTTPSRecordData | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        proxied: bool | NotGiven = NOT_GIVEN,
        settings: record_edit_params.HTTPSRecordSettings | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        type: Literal["HTTPS"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[RecordResponse]:
        """
        Update an existing DNS record.

        Notes:

        - A/AAAA records cannot exist on the same name as CNAME records.
        - NS records cannot exist on the same name as any other record type.
        - Domain names are always represented in Punycode, even if Unicode characters
          were used when creating the record.

        Args:
          zone_id: Identifier

          dns_record_id: Identifier

          comment: Comments or notes about the DNS record. This field has no effect on DNS
              responses.

          data: Components of a HTTPS record.

          name: DNS record name (or @ for the zone apex) in Punycode.

          proxied: Whether the record is receiving the performance and security benefits of
              Cloudflare.

          settings: Settings for the DNS record.

          tags: Custom tags for the DNS record. This field has no effect on DNS responses.

          ttl: Time To Live (TTL) of the DNS record in seconds. Setting to 1 means 'automatic'.
              Value must be between 60 and 86400, with the minimum reduced to 30 for
              Enterprise zones.

          type: Record type.

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
        comment: str | NotGiven = NOT_GIVEN,
        data: record_edit_params.LOCRecordData | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        proxied: bool | NotGiven = NOT_GIVEN,
        settings: record_edit_params.LOCRecordSettings | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        type: Literal["LOC"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[RecordResponse]:
        """
        Update an existing DNS record.

        Notes:

        - A/AAAA records cannot exist on the same name as CNAME records.
        - NS records cannot exist on the same name as any other record type.
        - Domain names are always represented in Punycode, even if Unicode characters
          were used when creating the record.

        Args:
          zone_id: Identifier

          dns_record_id: Identifier

          comment: Comments or notes about the DNS record. This field has no effect on DNS
              responses.

          data: Components of a LOC record.

          name: DNS record name (or @ for the zone apex) in Punycode.

          proxied: Whether the record is receiving the performance and security benefits of
              Cloudflare.

          settings: Settings for the DNS record.

          tags: Custom tags for the DNS record. This field has no effect on DNS responses.

          ttl: Time To Live (TTL) of the DNS record in seconds. Setting to 1 means 'automatic'.
              Value must be between 60 and 86400, with the minimum reduced to 30 for
              Enterprise zones.

          type: Record type.

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
        comment: str | NotGiven = NOT_GIVEN,
        content: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        priority: float | NotGiven = NOT_GIVEN,
        proxied: bool | NotGiven = NOT_GIVEN,
        settings: record_edit_params.MXRecordSettings | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        type: Literal["MX"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[RecordResponse]:
        """
        Update an existing DNS record.

        Notes:

        - A/AAAA records cannot exist on the same name as CNAME records.
        - NS records cannot exist on the same name as any other record type.
        - Domain names are always represented in Punycode, even if Unicode characters
          were used when creating the record.

        Args:
          zone_id: Identifier

          dns_record_id: Identifier

          comment: Comments or notes about the DNS record. This field has no effect on DNS
              responses.

          content: A valid mail server hostname.

          name: DNS record name (or @ for the zone apex) in Punycode.

          priority: Required for MX, SRV and URI records; unused by other record types. Records with
              lower priorities are preferred.

          proxied: Whether the record is receiving the performance and security benefits of
              Cloudflare.

          settings: Settings for the DNS record.

          tags: Custom tags for the DNS record. This field has no effect on DNS responses.

          ttl: Time To Live (TTL) of the DNS record in seconds. Setting to 1 means 'automatic'.
              Value must be between 60 and 86400, with the minimum reduced to 30 for
              Enterprise zones.

          type: Record type.

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
        comment: str | NotGiven = NOT_GIVEN,
        data: record_edit_params.NAPTRRecordData | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        proxied: bool | NotGiven = NOT_GIVEN,
        settings: record_edit_params.NAPTRRecordSettings | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        type: Literal["NAPTR"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[RecordResponse]:
        """
        Update an existing DNS record.

        Notes:

        - A/AAAA records cannot exist on the same name as CNAME records.
        - NS records cannot exist on the same name as any other record type.
        - Domain names are always represented in Punycode, even if Unicode characters
          were used when creating the record.

        Args:
          zone_id: Identifier

          dns_record_id: Identifier

          comment: Comments or notes about the DNS record. This field has no effect on DNS
              responses.

          data: Components of a NAPTR record.

          name: DNS record name (or @ for the zone apex) in Punycode.

          proxied: Whether the record is receiving the performance and security benefits of
              Cloudflare.

          settings: Settings for the DNS record.

          tags: Custom tags for the DNS record. This field has no effect on DNS responses.

          ttl: Time To Live (TTL) of the DNS record in seconds. Setting to 1 means 'automatic'.
              Value must be between 60 and 86400, with the minimum reduced to 30 for
              Enterprise zones.

          type: Record type.

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
        comment: str | NotGiven = NOT_GIVEN,
        content: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        proxied: bool | NotGiven = NOT_GIVEN,
        settings: record_edit_params.NSRecordSettings | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        type: Literal["NS"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[RecordResponse]:
        """
        Update an existing DNS record.

        Notes:

        - A/AAAA records cannot exist on the same name as CNAME records.
        - NS records cannot exist on the same name as any other record type.
        - Domain names are always represented in Punycode, even if Unicode characters
          were used when creating the record.

        Args:
          zone_id: Identifier

          dns_record_id: Identifier

          comment: Comments or notes about the DNS record. This field has no effect on DNS
              responses.

          content: A valid name server host name.

          name: DNS record name (or @ for the zone apex) in Punycode.

          proxied: Whether the record is receiving the performance and security benefits of
              Cloudflare.

          settings: Settings for the DNS record.

          tags: Custom tags for the DNS record. This field has no effect on DNS responses.

          ttl: Time To Live (TTL) of the DNS record in seconds. Setting to 1 means 'automatic'.
              Value must be between 60 and 86400, with the minimum reduced to 30 for
              Enterprise zones.

          type: Record type.

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
        comment: str | NotGiven = NOT_GIVEN,
        content: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        proxied: bool | NotGiven = NOT_GIVEN,
        settings: record_edit_params.DNSRecordsOpenpgpkeyRecordSettings | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        type: Literal["OPENPGPKEY"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[RecordResponse]:
        """
        Update an existing DNS record.

        Notes:

        - A/AAAA records cannot exist on the same name as CNAME records.
        - NS records cannot exist on the same name as any other record type.
        - Domain names are always represented in Punycode, even if Unicode characters
          were used when creating the record.

        Args:
          zone_id: Identifier

          dns_record_id: Identifier

          comment: Comments or notes about the DNS record. This field has no effect on DNS
              responses.

          content: A single Base64-encoded OpenPGP Transferable Public Key (RFC 4880 Section 11.1)

          name: DNS record name (or @ for the zone apex) in Punycode.

          proxied: Whether the record is receiving the performance and security benefits of
              Cloudflare.

          settings: Settings for the DNS record.

          tags: Custom tags for the DNS record. This field has no effect on DNS responses.

          ttl: Time To Live (TTL) of the DNS record in seconds. Setting to 1 means 'automatic'.
              Value must be between 60 and 86400, with the minimum reduced to 30 for
              Enterprise zones.

          type: Record type.

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
        comment: str | NotGiven = NOT_GIVEN,
        content: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        proxied: bool | NotGiven = NOT_GIVEN,
        settings: record_edit_params.PTRRecordSettings | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        type: Literal["PTR"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[RecordResponse]:
        """
        Update an existing DNS record.

        Notes:

        - A/AAAA records cannot exist on the same name as CNAME records.
        - NS records cannot exist on the same name as any other record type.
        - Domain names are always represented in Punycode, even if Unicode characters
          were used when creating the record.

        Args:
          zone_id: Identifier

          dns_record_id: Identifier

          comment: Comments or notes about the DNS record. This field has no effect on DNS
              responses.

          content: Domain name pointing to the address.

          name: DNS record name (or @ for the zone apex) in Punycode.

          proxied: Whether the record is receiving the performance and security benefits of
              Cloudflare.

          settings: Settings for the DNS record.

          tags: Custom tags for the DNS record. This field has no effect on DNS responses.

          ttl: Time To Live (TTL) of the DNS record in seconds. Setting to 1 means 'automatic'.
              Value must be between 60 and 86400, with the minimum reduced to 30 for
              Enterprise zones.

          type: Record type.

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
        comment: str | NotGiven = NOT_GIVEN,
        data: record_edit_params.SMIMEARecordData | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        proxied: bool | NotGiven = NOT_GIVEN,
        settings: record_edit_params.SMIMEARecordSettings | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        type: Literal["SMIMEA"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[RecordResponse]:
        """
        Update an existing DNS record.

        Notes:

        - A/AAAA records cannot exist on the same name as CNAME records.
        - NS records cannot exist on the same name as any other record type.
        - Domain names are always represented in Punycode, even if Unicode characters
          were used when creating the record.

        Args:
          zone_id: Identifier

          dns_record_id: Identifier

          comment: Comments or notes about the DNS record. This field has no effect on DNS
              responses.

          data: Components of a SMIMEA record.

          name: DNS record name (or @ for the zone apex) in Punycode.

          proxied: Whether the record is receiving the performance and security benefits of
              Cloudflare.

          settings: Settings for the DNS record.

          tags: Custom tags for the DNS record. This field has no effect on DNS responses.

          ttl: Time To Live (TTL) of the DNS record in seconds. Setting to 1 means 'automatic'.
              Value must be between 60 and 86400, with the minimum reduced to 30 for
              Enterprise zones.

          type: Record type.

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
        comment: str | NotGiven = NOT_GIVEN,
        data: record_edit_params.SRVRecordData | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        proxied: bool | NotGiven = NOT_GIVEN,
        settings: record_edit_params.SRVRecordSettings | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        type: Literal["SRV"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[RecordResponse]:
        """
        Update an existing DNS record.

        Notes:

        - A/AAAA records cannot exist on the same name as CNAME records.
        - NS records cannot exist on the same name as any other record type.
        - Domain names are always represented in Punycode, even if Unicode characters
          were used when creating the record.

        Args:
          zone_id: Identifier

          dns_record_id: Identifier

          comment: Comments or notes about the DNS record. This field has no effect on DNS
              responses.

          data: Components of a SRV record.

          name: DNS record name (or @ for the zone apex) in Punycode.

          proxied: Whether the record is receiving the performance and security benefits of
              Cloudflare.

          settings: Settings for the DNS record.

          tags: Custom tags for the DNS record. This field has no effect on DNS responses.

          ttl: Time To Live (TTL) of the DNS record in seconds. Setting to 1 means 'automatic'.
              Value must be between 60 and 86400, with the minimum reduced to 30 for
              Enterprise zones.

          type: Record type.

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
        comment: str | NotGiven = NOT_GIVEN,
        data: record_edit_params.SSHFPRecordData | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        proxied: bool | NotGiven = NOT_GIVEN,
        settings: record_edit_params.SSHFPRecordSettings | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        type: Literal["SSHFP"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[RecordResponse]:
        """
        Update an existing DNS record.

        Notes:

        - A/AAAA records cannot exist on the same name as CNAME records.
        - NS records cannot exist on the same name as any other record type.
        - Domain names are always represented in Punycode, even if Unicode characters
          were used when creating the record.

        Args:
          zone_id: Identifier

          dns_record_id: Identifier

          comment: Comments or notes about the DNS record. This field has no effect on DNS
              responses.

          data: Components of a SSHFP record.

          name: DNS record name (or @ for the zone apex) in Punycode.

          proxied: Whether the record is receiving the performance and security benefits of
              Cloudflare.

          settings: Settings for the DNS record.

          tags: Custom tags for the DNS record. This field has no effect on DNS responses.

          ttl: Time To Live (TTL) of the DNS record in seconds. Setting to 1 means 'automatic'.
              Value must be between 60 and 86400, with the minimum reduced to 30 for
              Enterprise zones.

          type: Record type.

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
        comment: str | NotGiven = NOT_GIVEN,
        data: record_edit_params.SVCBRecordData | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        proxied: bool | NotGiven = NOT_GIVEN,
        settings: record_edit_params.SVCBRecordSettings | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        type: Literal["SVCB"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[RecordResponse]:
        """
        Update an existing DNS record.

        Notes:

        - A/AAAA records cannot exist on the same name as CNAME records.
        - NS records cannot exist on the same name as any other record type.
        - Domain names are always represented in Punycode, even if Unicode characters
          were used when creating the record.

        Args:
          zone_id: Identifier

          dns_record_id: Identifier

          comment: Comments or notes about the DNS record. This field has no effect on DNS
              responses.

          data: Components of a SVCB record.

          name: DNS record name (or @ for the zone apex) in Punycode.

          proxied: Whether the record is receiving the performance and security benefits of
              Cloudflare.

          settings: Settings for the DNS record.

          tags: Custom tags for the DNS record. This field has no effect on DNS responses.

          ttl: Time To Live (TTL) of the DNS record in seconds. Setting to 1 means 'automatic'.
              Value must be between 60 and 86400, with the minimum reduced to 30 for
              Enterprise zones.

          type: Record type.

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
        comment: str | NotGiven = NOT_GIVEN,
        data: record_edit_params.TLSARecordData | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        proxied: bool | NotGiven = NOT_GIVEN,
        settings: record_edit_params.TLSARecordSettings | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        type: Literal["TLSA"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[RecordResponse]:
        """
        Update an existing DNS record.

        Notes:

        - A/AAAA records cannot exist on the same name as CNAME records.
        - NS records cannot exist on the same name as any other record type.
        - Domain names are always represented in Punycode, even if Unicode characters
          were used when creating the record.

        Args:
          zone_id: Identifier

          dns_record_id: Identifier

          comment: Comments or notes about the DNS record. This field has no effect on DNS
              responses.

          data: Components of a TLSA record.

          name: DNS record name (or @ for the zone apex) in Punycode.

          proxied: Whether the record is receiving the performance and security benefits of
              Cloudflare.

          settings: Settings for the DNS record.

          tags: Custom tags for the DNS record. This field has no effect on DNS responses.

          ttl: Time To Live (TTL) of the DNS record in seconds. Setting to 1 means 'automatic'.
              Value must be between 60 and 86400, with the minimum reduced to 30 for
              Enterprise zones.

          type: Record type.

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
        comment: str | NotGiven = NOT_GIVEN,
        content: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        proxied: bool | NotGiven = NOT_GIVEN,
        settings: record_edit_params.TXTRecordSettings | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        type: Literal["TXT"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[RecordResponse]:
        """
        Update an existing DNS record.

        Notes:

        - A/AAAA records cannot exist on the same name as CNAME records.
        - NS records cannot exist on the same name as any other record type.
        - Domain names are always represented in Punycode, even if Unicode characters
          were used when creating the record.

        Args:
          zone_id: Identifier

          dns_record_id: Identifier

          comment: Comments or notes about the DNS record. This field has no effect on DNS
              responses.

          content: Text content for the record. The content must consist of quoted "character
              strings" (RFC 1035), each with a length of up to 255 bytes. Strings exceeding
              this allowed maximum length are automatically split.

              Learn more at
              <https://www.cloudflare.com/learning/dns/dns-records/dns-txt-record/>.

          name: DNS record name (or @ for the zone apex) in Punycode.

          proxied: Whether the record is receiving the performance and security benefits of
              Cloudflare.

          settings: Settings for the DNS record.

          tags: Custom tags for the DNS record. This field has no effect on DNS responses.

          ttl: Time To Live (TTL) of the DNS record in seconds. Setting to 1 means 'automatic'.
              Value must be between 60 and 86400, with the minimum reduced to 30 for
              Enterprise zones.

          type: Record type.

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
        comment: str | NotGiven = NOT_GIVEN,
        data: record_edit_params.URIRecordData | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        priority: float | NotGiven = NOT_GIVEN,
        proxied: bool | NotGiven = NOT_GIVEN,
        settings: record_edit_params.URIRecordSettings | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        type: Literal["URI"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[RecordResponse]:
        """
        Update an existing DNS record.

        Notes:

        - A/AAAA records cannot exist on the same name as CNAME records.
        - NS records cannot exist on the same name as any other record type.
        - Domain names are always represented in Punycode, even if Unicode characters
          were used when creating the record.

        Args:
          zone_id: Identifier

          dns_record_id: Identifier

          comment: Comments or notes about the DNS record. This field has no effect on DNS
              responses.

          data: Components of a URI record.

          name: DNS record name (or @ for the zone apex) in Punycode.

          priority: Required for MX, SRV and URI records; unused by other record types. Records with
              lower priorities are preferred.

          proxied: Whether the record is receiving the performance and security benefits of
              Cloudflare.

          settings: Settings for the DNS record.

          tags: Custom tags for the DNS record. This field has no effect on DNS responses.

          ttl: Time To Live (TTL) of the DNS record in seconds. Setting to 1 means 'automatic'.
              Value must be between 60 and 86400, with the minimum reduced to 30 for
              Enterprise zones.

          type: Record type.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["zone_id"])
    def edit(
        self,
        dns_record_id: str,
        *,
        zone_id: str,
        comment: str | NotGiven = NOT_GIVEN,
        content: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        proxied: bool | NotGiven = NOT_GIVEN,
        settings: record_edit_params.ARecordSettings | record_edit_params.CNAMERecordSettings | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
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
        | Literal["URI"]
        | NotGiven = NOT_GIVEN,
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
    ) -> Optional[RecordResponse]:
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not dns_record_id:
            raise ValueError(f"Expected a non-empty value for `dns_record_id` but received {dns_record_id!r}")
        return cast(
            Optional[RecordResponse],
            self._patch(
                f"/zones/{zone_id}/dns_records/{dns_record_id}",
                body=maybe_transform(
                    {
                        "comment": comment,
                        "content": content,
                        "name": name,
                        "proxied": proxied,
                        "settings": settings,
                        "tags": tags,
                        "ttl": ttl,
                        "type": type,
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
                    post_parser=ResultWrapper[Optional[RecordResponse]]._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[RecordResponse]
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
    ) -> Optional[RecordResponse]:
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
            Optional[RecordResponse],
            self._get(
                f"/zones/{zone_id}/dns_records/{dns_record_id}",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper[Optional[RecordResponse]]._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[RecordResponse]
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
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRecordsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRecordsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncRecordsResourceWithStreamingResponse(self)

    @overload
    async def create(
        self,
        *,
        zone_id: str,
        comment: str | NotGiven = NOT_GIVEN,
        content: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        proxied: bool | NotGiven = NOT_GIVEN,
        settings: record_create_params.ARecordSettings | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        type: Literal["A"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[RecordResponse]:
        """
        Create a new DNS record for a zone.

        Notes:

        - A/AAAA records cannot exist on the same name as CNAME records.
        - NS records cannot exist on the same name as any other record type.
        - Domain names are always represented in Punycode, even if Unicode characters
          were used when creating the record.

        Args:
          zone_id: Identifier

          comment: Comments or notes about the DNS record. This field has no effect on DNS
              responses.

          content: A valid IPv4 address.

          name: DNS record name (or @ for the zone apex) in Punycode.

          proxied: Whether the record is receiving the performance and security benefits of
              Cloudflare.

          settings: Settings for the DNS record.

          tags: Custom tags for the DNS record. This field has no effect on DNS responses.

          ttl: Time To Live (TTL) of the DNS record in seconds. Setting to 1 means 'automatic'.
              Value must be between 60 and 86400, with the minimum reduced to 30 for
              Enterprise zones.

          type: Record type.

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
        comment: str | NotGiven = NOT_GIVEN,
        content: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        proxied: bool | NotGiven = NOT_GIVEN,
        settings: record_create_params.AAAARecordSettings | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        type: Literal["AAAA"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[RecordResponse]:
        """
        Create a new DNS record for a zone.

        Notes:

        - A/AAAA records cannot exist on the same name as CNAME records.
        - NS records cannot exist on the same name as any other record type.
        - Domain names are always represented in Punycode, even if Unicode characters
          were used when creating the record.

        Args:
          zone_id: Identifier

          comment: Comments or notes about the DNS record. This field has no effect on DNS
              responses.

          content: A valid IPv6 address.

          name: DNS record name (or @ for the zone apex) in Punycode.

          proxied: Whether the record is receiving the performance and security benefits of
              Cloudflare.

          settings: Settings for the DNS record.

          tags: Custom tags for the DNS record. This field has no effect on DNS responses.

          ttl: Time To Live (TTL) of the DNS record in seconds. Setting to 1 means 'automatic'.
              Value must be between 60 and 86400, with the minimum reduced to 30 for
              Enterprise zones.

          type: Record type.

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
        comment: str | NotGiven = NOT_GIVEN,
        data: record_create_params.CAARecordData | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        proxied: bool | NotGiven = NOT_GIVEN,
        settings: record_create_params.CAARecordSettings | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        type: Literal["CAA"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[RecordResponse]:
        """
        Create a new DNS record for a zone.

        Notes:

        - A/AAAA records cannot exist on the same name as CNAME records.
        - NS records cannot exist on the same name as any other record type.
        - Domain names are always represented in Punycode, even if Unicode characters
          were used when creating the record.

        Args:
          zone_id: Identifier

          comment: Comments or notes about the DNS record. This field has no effect on DNS
              responses.

          data: Components of a CAA record.

          name: DNS record name (or @ for the zone apex) in Punycode.

          proxied: Whether the record is receiving the performance and security benefits of
              Cloudflare.

          settings: Settings for the DNS record.

          tags: Custom tags for the DNS record. This field has no effect on DNS responses.

          ttl: Time To Live (TTL) of the DNS record in seconds. Setting to 1 means 'automatic'.
              Value must be between 60 and 86400, with the minimum reduced to 30 for
              Enterprise zones.

          type: Record type.

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
        comment: str | NotGiven = NOT_GIVEN,
        data: record_create_params.CERTRecordData | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        proxied: bool | NotGiven = NOT_GIVEN,
        settings: record_create_params.CERTRecordSettings | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        type: Literal["CERT"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[RecordResponse]:
        """
        Create a new DNS record for a zone.

        Notes:

        - A/AAAA records cannot exist on the same name as CNAME records.
        - NS records cannot exist on the same name as any other record type.
        - Domain names are always represented in Punycode, even if Unicode characters
          were used when creating the record.

        Args:
          zone_id: Identifier

          comment: Comments or notes about the DNS record. This field has no effect on DNS
              responses.

          data: Components of a CERT record.

          name: DNS record name (or @ for the zone apex) in Punycode.

          proxied: Whether the record is receiving the performance and security benefits of
              Cloudflare.

          settings: Settings for the DNS record.

          tags: Custom tags for the DNS record. This field has no effect on DNS responses.

          ttl: Time To Live (TTL) of the DNS record in seconds. Setting to 1 means 'automatic'.
              Value must be between 60 and 86400, with the minimum reduced to 30 for
              Enterprise zones.

          type: Record type.

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
        comment: str | NotGiven = NOT_GIVEN,
        content: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        proxied: bool | NotGiven = NOT_GIVEN,
        settings: record_create_params.CNAMERecordSettings | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        type: Literal["CNAME"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[RecordResponse]:
        """
        Create a new DNS record for a zone.

        Notes:

        - A/AAAA records cannot exist on the same name as CNAME records.
        - NS records cannot exist on the same name as any other record type.
        - Domain names are always represented in Punycode, even if Unicode characters
          were used when creating the record.

        Args:
          zone_id: Identifier

          comment: Comments or notes about the DNS record. This field has no effect on DNS
              responses.

          content: A valid hostname. Must not match the record's name.

          name: DNS record name (or @ for the zone apex) in Punycode.

          proxied: Whether the record is receiving the performance and security benefits of
              Cloudflare.

          settings: Settings for the DNS record.

          tags: Custom tags for the DNS record. This field has no effect on DNS responses.

          ttl: Time To Live (TTL) of the DNS record in seconds. Setting to 1 means 'automatic'.
              Value must be between 60 and 86400, with the minimum reduced to 30 for
              Enterprise zones.

          type: Record type.

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
        comment: str | NotGiven = NOT_GIVEN,
        data: record_create_params.DNSKEYRecordData | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        proxied: bool | NotGiven = NOT_GIVEN,
        settings: record_create_params.DNSKEYRecordSettings | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        type: Literal["DNSKEY"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[RecordResponse]:
        """
        Create a new DNS record for a zone.

        Notes:

        - A/AAAA records cannot exist on the same name as CNAME records.
        - NS records cannot exist on the same name as any other record type.
        - Domain names are always represented in Punycode, even if Unicode characters
          were used when creating the record.

        Args:
          zone_id: Identifier

          comment: Comments or notes about the DNS record. This field has no effect on DNS
              responses.

          data: Components of a DNSKEY record.

          name: DNS record name (or @ for the zone apex) in Punycode.

          proxied: Whether the record is receiving the performance and security benefits of
              Cloudflare.

          settings: Settings for the DNS record.

          tags: Custom tags for the DNS record. This field has no effect on DNS responses.

          ttl: Time To Live (TTL) of the DNS record in seconds. Setting to 1 means 'automatic'.
              Value must be between 60 and 86400, with the minimum reduced to 30 for
              Enterprise zones.

          type: Record type.

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
        comment: str | NotGiven = NOT_GIVEN,
        data: record_create_params.DSRecordData | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        proxied: bool | NotGiven = NOT_GIVEN,
        settings: record_create_params.DSRecordSettings | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        type: Literal["DS"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[RecordResponse]:
        """
        Create a new DNS record for a zone.

        Notes:

        - A/AAAA records cannot exist on the same name as CNAME records.
        - NS records cannot exist on the same name as any other record type.
        - Domain names are always represented in Punycode, even if Unicode characters
          were used when creating the record.

        Args:
          zone_id: Identifier

          comment: Comments or notes about the DNS record. This field has no effect on DNS
              responses.

          data: Components of a DS record.

          name: DNS record name (or @ for the zone apex) in Punycode.

          proxied: Whether the record is receiving the performance and security benefits of
              Cloudflare.

          settings: Settings for the DNS record.

          tags: Custom tags for the DNS record. This field has no effect on DNS responses.

          ttl: Time To Live (TTL) of the DNS record in seconds. Setting to 1 means 'automatic'.
              Value must be between 60 and 86400, with the minimum reduced to 30 for
              Enterprise zones.

          type: Record type.

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
        comment: str | NotGiven = NOT_GIVEN,
        data: record_create_params.HTTPSRecordData | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        proxied: bool | NotGiven = NOT_GIVEN,
        settings: record_create_params.HTTPSRecordSettings | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        type: Literal["HTTPS"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[RecordResponse]:
        """
        Create a new DNS record for a zone.

        Notes:

        - A/AAAA records cannot exist on the same name as CNAME records.
        - NS records cannot exist on the same name as any other record type.
        - Domain names are always represented in Punycode, even if Unicode characters
          were used when creating the record.

        Args:
          zone_id: Identifier

          comment: Comments or notes about the DNS record. This field has no effect on DNS
              responses.

          data: Components of a HTTPS record.

          name: DNS record name (or @ for the zone apex) in Punycode.

          proxied: Whether the record is receiving the performance and security benefits of
              Cloudflare.

          settings: Settings for the DNS record.

          tags: Custom tags for the DNS record. This field has no effect on DNS responses.

          ttl: Time To Live (TTL) of the DNS record in seconds. Setting to 1 means 'automatic'.
              Value must be between 60 and 86400, with the minimum reduced to 30 for
              Enterprise zones.

          type: Record type.

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
        comment: str | NotGiven = NOT_GIVEN,
        data: record_create_params.LOCRecordData | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        proxied: bool | NotGiven = NOT_GIVEN,
        settings: record_create_params.LOCRecordSettings | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        type: Literal["LOC"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[RecordResponse]:
        """
        Create a new DNS record for a zone.

        Notes:

        - A/AAAA records cannot exist on the same name as CNAME records.
        - NS records cannot exist on the same name as any other record type.
        - Domain names are always represented in Punycode, even if Unicode characters
          were used when creating the record.

        Args:
          zone_id: Identifier

          comment: Comments or notes about the DNS record. This field has no effect on DNS
              responses.

          data: Components of a LOC record.

          name: DNS record name (or @ for the zone apex) in Punycode.

          proxied: Whether the record is receiving the performance and security benefits of
              Cloudflare.

          settings: Settings for the DNS record.

          tags: Custom tags for the DNS record. This field has no effect on DNS responses.

          ttl: Time To Live (TTL) of the DNS record in seconds. Setting to 1 means 'automatic'.
              Value must be between 60 and 86400, with the minimum reduced to 30 for
              Enterprise zones.

          type: Record type.

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
        comment: str | NotGiven = NOT_GIVEN,
        content: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        priority: float | NotGiven = NOT_GIVEN,
        proxied: bool | NotGiven = NOT_GIVEN,
        settings: record_create_params.MXRecordSettings | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        type: Literal["MX"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[RecordResponse]:
        """
        Create a new DNS record for a zone.

        Notes:

        - A/AAAA records cannot exist on the same name as CNAME records.
        - NS records cannot exist on the same name as any other record type.
        - Domain names are always represented in Punycode, even if Unicode characters
          were used when creating the record.

        Args:
          zone_id: Identifier

          comment: Comments or notes about the DNS record. This field has no effect on DNS
              responses.

          content: A valid mail server hostname.

          name: DNS record name (or @ for the zone apex) in Punycode.

          priority: Required for MX, SRV and URI records; unused by other record types. Records with
              lower priorities are preferred.

          proxied: Whether the record is receiving the performance and security benefits of
              Cloudflare.

          settings: Settings for the DNS record.

          tags: Custom tags for the DNS record. This field has no effect on DNS responses.

          ttl: Time To Live (TTL) of the DNS record in seconds. Setting to 1 means 'automatic'.
              Value must be between 60 and 86400, with the minimum reduced to 30 for
              Enterprise zones.

          type: Record type.

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
        comment: str | NotGiven = NOT_GIVEN,
        data: record_create_params.NAPTRRecordData | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        proxied: bool | NotGiven = NOT_GIVEN,
        settings: record_create_params.NAPTRRecordSettings | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        type: Literal["NAPTR"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[RecordResponse]:
        """
        Create a new DNS record for a zone.

        Notes:

        - A/AAAA records cannot exist on the same name as CNAME records.
        - NS records cannot exist on the same name as any other record type.
        - Domain names are always represented in Punycode, even if Unicode characters
          were used when creating the record.

        Args:
          zone_id: Identifier

          comment: Comments or notes about the DNS record. This field has no effect on DNS
              responses.

          data: Components of a NAPTR record.

          name: DNS record name (or @ for the zone apex) in Punycode.

          proxied: Whether the record is receiving the performance and security benefits of
              Cloudflare.

          settings: Settings for the DNS record.

          tags: Custom tags for the DNS record. This field has no effect on DNS responses.

          ttl: Time To Live (TTL) of the DNS record in seconds. Setting to 1 means 'automatic'.
              Value must be between 60 and 86400, with the minimum reduced to 30 for
              Enterprise zones.

          type: Record type.

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
        comment: str | NotGiven = NOT_GIVEN,
        content: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        proxied: bool | NotGiven = NOT_GIVEN,
        settings: record_create_params.NSRecordSettings | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        type: Literal["NS"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[RecordResponse]:
        """
        Create a new DNS record for a zone.

        Notes:

        - A/AAAA records cannot exist on the same name as CNAME records.
        - NS records cannot exist on the same name as any other record type.
        - Domain names are always represented in Punycode, even if Unicode characters
          were used when creating the record.

        Args:
          zone_id: Identifier

          comment: Comments or notes about the DNS record. This field has no effect on DNS
              responses.

          content: A valid name server host name.

          name: DNS record name (or @ for the zone apex) in Punycode.

          proxied: Whether the record is receiving the performance and security benefits of
              Cloudflare.

          settings: Settings for the DNS record.

          tags: Custom tags for the DNS record. This field has no effect on DNS responses.

          ttl: Time To Live (TTL) of the DNS record in seconds. Setting to 1 means 'automatic'.
              Value must be between 60 and 86400, with the minimum reduced to 30 for
              Enterprise zones.

          type: Record type.

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
        comment: str | NotGiven = NOT_GIVEN,
        content: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        proxied: bool | NotGiven = NOT_GIVEN,
        settings: record_create_params.DNSRecordsOpenpgpkeyRecordSettings | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        type: Literal["OPENPGPKEY"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[RecordResponse]:
        """
        Create a new DNS record for a zone.

        Notes:

        - A/AAAA records cannot exist on the same name as CNAME records.
        - NS records cannot exist on the same name as any other record type.
        - Domain names are always represented in Punycode, even if Unicode characters
          were used when creating the record.

        Args:
          zone_id: Identifier

          comment: Comments or notes about the DNS record. This field has no effect on DNS
              responses.

          content: A single Base64-encoded OpenPGP Transferable Public Key (RFC 4880 Section 11.1)

          name: DNS record name (or @ for the zone apex) in Punycode.

          proxied: Whether the record is receiving the performance and security benefits of
              Cloudflare.

          settings: Settings for the DNS record.

          tags: Custom tags for the DNS record. This field has no effect on DNS responses.

          ttl: Time To Live (TTL) of the DNS record in seconds. Setting to 1 means 'automatic'.
              Value must be between 60 and 86400, with the minimum reduced to 30 for
              Enterprise zones.

          type: Record type.

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
        comment: str | NotGiven = NOT_GIVEN,
        content: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        proxied: bool | NotGiven = NOT_GIVEN,
        settings: record_create_params.PTRRecordSettings | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        type: Literal["PTR"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[RecordResponse]:
        """
        Create a new DNS record for a zone.

        Notes:

        - A/AAAA records cannot exist on the same name as CNAME records.
        - NS records cannot exist on the same name as any other record type.
        - Domain names are always represented in Punycode, even if Unicode characters
          were used when creating the record.

        Args:
          zone_id: Identifier

          comment: Comments or notes about the DNS record. This field has no effect on DNS
              responses.

          content: Domain name pointing to the address.

          name: DNS record name (or @ for the zone apex) in Punycode.

          proxied: Whether the record is receiving the performance and security benefits of
              Cloudflare.

          settings: Settings for the DNS record.

          tags: Custom tags for the DNS record. This field has no effect on DNS responses.

          ttl: Time To Live (TTL) of the DNS record in seconds. Setting to 1 means 'automatic'.
              Value must be between 60 and 86400, with the minimum reduced to 30 for
              Enterprise zones.

          type: Record type.

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
        comment: str | NotGiven = NOT_GIVEN,
        data: record_create_params.SMIMEARecordData | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        proxied: bool | NotGiven = NOT_GIVEN,
        settings: record_create_params.SMIMEARecordSettings | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        type: Literal["SMIMEA"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[RecordResponse]:
        """
        Create a new DNS record for a zone.

        Notes:

        - A/AAAA records cannot exist on the same name as CNAME records.
        - NS records cannot exist on the same name as any other record type.
        - Domain names are always represented in Punycode, even if Unicode characters
          were used when creating the record.

        Args:
          zone_id: Identifier

          comment: Comments or notes about the DNS record. This field has no effect on DNS
              responses.

          data: Components of a SMIMEA record.

          name: DNS record name (or @ for the zone apex) in Punycode.

          proxied: Whether the record is receiving the performance and security benefits of
              Cloudflare.

          settings: Settings for the DNS record.

          tags: Custom tags for the DNS record. This field has no effect on DNS responses.

          ttl: Time To Live (TTL) of the DNS record in seconds. Setting to 1 means 'automatic'.
              Value must be between 60 and 86400, with the minimum reduced to 30 for
              Enterprise zones.

          type: Record type.

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
        comment: str | NotGiven = NOT_GIVEN,
        data: record_create_params.SRVRecordData | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        proxied: bool | NotGiven = NOT_GIVEN,
        settings: record_create_params.SRVRecordSettings | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        type: Literal["SRV"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[RecordResponse]:
        """
        Create a new DNS record for a zone.

        Notes:

        - A/AAAA records cannot exist on the same name as CNAME records.
        - NS records cannot exist on the same name as any other record type.
        - Domain names are always represented in Punycode, even if Unicode characters
          were used when creating the record.

        Args:
          zone_id: Identifier

          comment: Comments or notes about the DNS record. This field has no effect on DNS
              responses.

          data: Components of a SRV record.

          name: DNS record name (or @ for the zone apex) in Punycode.

          proxied: Whether the record is receiving the performance and security benefits of
              Cloudflare.

          settings: Settings for the DNS record.

          tags: Custom tags for the DNS record. This field has no effect on DNS responses.

          ttl: Time To Live (TTL) of the DNS record in seconds. Setting to 1 means 'automatic'.
              Value must be between 60 and 86400, with the minimum reduced to 30 for
              Enterprise zones.

          type: Record type.

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
        comment: str | NotGiven = NOT_GIVEN,
        data: record_create_params.SSHFPRecordData | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        proxied: bool | NotGiven = NOT_GIVEN,
        settings: record_create_params.SSHFPRecordSettings | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        type: Literal["SSHFP"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[RecordResponse]:
        """
        Create a new DNS record for a zone.

        Notes:

        - A/AAAA records cannot exist on the same name as CNAME records.
        - NS records cannot exist on the same name as any other record type.
        - Domain names are always represented in Punycode, even if Unicode characters
          were used when creating the record.

        Args:
          zone_id: Identifier

          comment: Comments or notes about the DNS record. This field has no effect on DNS
              responses.

          data: Components of a SSHFP record.

          name: DNS record name (or @ for the zone apex) in Punycode.

          proxied: Whether the record is receiving the performance and security benefits of
              Cloudflare.

          settings: Settings for the DNS record.

          tags: Custom tags for the DNS record. This field has no effect on DNS responses.

          ttl: Time To Live (TTL) of the DNS record in seconds. Setting to 1 means 'automatic'.
              Value must be between 60 and 86400, with the minimum reduced to 30 for
              Enterprise zones.

          type: Record type.

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
        comment: str | NotGiven = NOT_GIVEN,
        data: record_create_params.SVCBRecordData | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        proxied: bool | NotGiven = NOT_GIVEN,
        settings: record_create_params.SVCBRecordSettings | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        type: Literal["SVCB"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[RecordResponse]:
        """
        Create a new DNS record for a zone.

        Notes:

        - A/AAAA records cannot exist on the same name as CNAME records.
        - NS records cannot exist on the same name as any other record type.
        - Domain names are always represented in Punycode, even if Unicode characters
          were used when creating the record.

        Args:
          zone_id: Identifier

          comment: Comments or notes about the DNS record. This field has no effect on DNS
              responses.

          data: Components of a SVCB record.

          name: DNS record name (or @ for the zone apex) in Punycode.

          proxied: Whether the record is receiving the performance and security benefits of
              Cloudflare.

          settings: Settings for the DNS record.

          tags: Custom tags for the DNS record. This field has no effect on DNS responses.

          ttl: Time To Live (TTL) of the DNS record in seconds. Setting to 1 means 'automatic'.
              Value must be between 60 and 86400, with the minimum reduced to 30 for
              Enterprise zones.

          type: Record type.

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
        comment: str | NotGiven = NOT_GIVEN,
        data: record_create_params.TLSARecordData | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        proxied: bool | NotGiven = NOT_GIVEN,
        settings: record_create_params.TLSARecordSettings | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        type: Literal["TLSA"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[RecordResponse]:
        """
        Create a new DNS record for a zone.

        Notes:

        - A/AAAA records cannot exist on the same name as CNAME records.
        - NS records cannot exist on the same name as any other record type.
        - Domain names are always represented in Punycode, even if Unicode characters
          were used when creating the record.

        Args:
          zone_id: Identifier

          comment: Comments or notes about the DNS record. This field has no effect on DNS
              responses.

          data: Components of a TLSA record.

          name: DNS record name (or @ for the zone apex) in Punycode.

          proxied: Whether the record is receiving the performance and security benefits of
              Cloudflare.

          settings: Settings for the DNS record.

          tags: Custom tags for the DNS record. This field has no effect on DNS responses.

          ttl: Time To Live (TTL) of the DNS record in seconds. Setting to 1 means 'automatic'.
              Value must be between 60 and 86400, with the minimum reduced to 30 for
              Enterprise zones.

          type: Record type.

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
        comment: str | NotGiven = NOT_GIVEN,
        content: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        proxied: bool | NotGiven = NOT_GIVEN,
        settings: record_create_params.TXTRecordSettings | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        type: Literal["TXT"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[RecordResponse]:
        """
        Create a new DNS record for a zone.

        Notes:

        - A/AAAA records cannot exist on the same name as CNAME records.
        - NS records cannot exist on the same name as any other record type.
        - Domain names are always represented in Punycode, even if Unicode characters
          were used when creating the record.

        Args:
          zone_id: Identifier

          comment: Comments or notes about the DNS record. This field has no effect on DNS
              responses.

          content: Text content for the record. The content must consist of quoted "character
              strings" (RFC 1035), each with a length of up to 255 bytes. Strings exceeding
              this allowed maximum length are automatically split.

              Learn more at
              <https://www.cloudflare.com/learning/dns/dns-records/dns-txt-record/>.

          name: DNS record name (or @ for the zone apex) in Punycode.

          proxied: Whether the record is receiving the performance and security benefits of
              Cloudflare.

          settings: Settings for the DNS record.

          tags: Custom tags for the DNS record. This field has no effect on DNS responses.

          ttl: Time To Live (TTL) of the DNS record in seconds. Setting to 1 means 'automatic'.
              Value must be between 60 and 86400, with the minimum reduced to 30 for
              Enterprise zones.

          type: Record type.

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
        comment: str | NotGiven = NOT_GIVEN,
        data: record_create_params.URIRecordData | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        priority: float | NotGiven = NOT_GIVEN,
        proxied: bool | NotGiven = NOT_GIVEN,
        settings: record_create_params.URIRecordSettings | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        type: Literal["URI"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[RecordResponse]:
        """
        Create a new DNS record for a zone.

        Notes:

        - A/AAAA records cannot exist on the same name as CNAME records.
        - NS records cannot exist on the same name as any other record type.
        - Domain names are always represented in Punycode, even if Unicode characters
          were used when creating the record.

        Args:
          zone_id: Identifier

          comment: Comments or notes about the DNS record. This field has no effect on DNS
              responses.

          data: Components of a URI record.

          name: DNS record name (or @ for the zone apex) in Punycode.

          priority: Required for MX, SRV and URI records; unused by other record types. Records with
              lower priorities are preferred.

          proxied: Whether the record is receiving the performance and security benefits of
              Cloudflare.

          settings: Settings for the DNS record.

          tags: Custom tags for the DNS record. This field has no effect on DNS responses.

          ttl: Time To Live (TTL) of the DNS record in seconds. Setting to 1 means 'automatic'.
              Value must be between 60 and 86400, with the minimum reduced to 30 for
              Enterprise zones.

          type: Record type.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["zone_id"])
    async def create(
        self,
        *,
        zone_id: str,
        comment: str | NotGiven = NOT_GIVEN,
        content: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        proxied: bool | NotGiven = NOT_GIVEN,
        settings: record_create_params.ARecordSettings
        | record_create_params.CNAMERecordSettings
        | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
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
        | Literal["URI"]
        | NotGiven = NOT_GIVEN,
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
    ) -> Optional[RecordResponse]:
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return cast(
            Optional[RecordResponse],
            await self._post(
                f"/zones/{zone_id}/dns_records",
                body=await async_maybe_transform(
                    {
                        "comment": comment,
                        "content": content,
                        "name": name,
                        "proxied": proxied,
                        "settings": settings,
                        "tags": tags,
                        "ttl": ttl,
                        "type": type,
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
                    post_parser=ResultWrapper[Optional[RecordResponse]]._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[RecordResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    @overload
    async def update(
        self,
        dns_record_id: str,
        *,
        zone_id: str,
        comment: str | NotGiven = NOT_GIVEN,
        content: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        proxied: bool | NotGiven = NOT_GIVEN,
        settings: record_update_params.ARecordSettings | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        type: Literal["A"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[RecordResponse]:
        """
        Overwrite an existing DNS record.

        Notes:

        - A/AAAA records cannot exist on the same name as CNAME records.
        - NS records cannot exist on the same name as any other record type.
        - Domain names are always represented in Punycode, even if Unicode characters
          were used when creating the record.

        Args:
          zone_id: Identifier

          dns_record_id: Identifier

          comment: Comments or notes about the DNS record. This field has no effect on DNS
              responses.

          content: A valid IPv4 address.

          name: DNS record name (or @ for the zone apex) in Punycode.

          proxied: Whether the record is receiving the performance and security benefits of
              Cloudflare.

          settings: Settings for the DNS record.

          tags: Custom tags for the DNS record. This field has no effect on DNS responses.

          ttl: Time To Live (TTL) of the DNS record in seconds. Setting to 1 means 'automatic'.
              Value must be between 60 and 86400, with the minimum reduced to 30 for
              Enterprise zones.

          type: Record type.

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
        comment: str | NotGiven = NOT_GIVEN,
        content: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        proxied: bool | NotGiven = NOT_GIVEN,
        settings: record_update_params.AAAARecordSettings | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        type: Literal["AAAA"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[RecordResponse]:
        """
        Overwrite an existing DNS record.

        Notes:

        - A/AAAA records cannot exist on the same name as CNAME records.
        - NS records cannot exist on the same name as any other record type.
        - Domain names are always represented in Punycode, even if Unicode characters
          were used when creating the record.

        Args:
          zone_id: Identifier

          dns_record_id: Identifier

          comment: Comments or notes about the DNS record. This field has no effect on DNS
              responses.

          content: A valid IPv6 address.

          name: DNS record name (or @ for the zone apex) in Punycode.

          proxied: Whether the record is receiving the performance and security benefits of
              Cloudflare.

          settings: Settings for the DNS record.

          tags: Custom tags for the DNS record. This field has no effect on DNS responses.

          ttl: Time To Live (TTL) of the DNS record in seconds. Setting to 1 means 'automatic'.
              Value must be between 60 and 86400, with the minimum reduced to 30 for
              Enterprise zones.

          type: Record type.

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
        comment: str | NotGiven = NOT_GIVEN,
        data: record_update_params.CAARecordData | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        proxied: bool | NotGiven = NOT_GIVEN,
        settings: record_update_params.CAARecordSettings | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        type: Literal["CAA"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[RecordResponse]:
        """
        Overwrite an existing DNS record.

        Notes:

        - A/AAAA records cannot exist on the same name as CNAME records.
        - NS records cannot exist on the same name as any other record type.
        - Domain names are always represented in Punycode, even if Unicode characters
          were used when creating the record.

        Args:
          zone_id: Identifier

          dns_record_id: Identifier

          comment: Comments or notes about the DNS record. This field has no effect on DNS
              responses.

          data: Components of a CAA record.

          name: DNS record name (or @ for the zone apex) in Punycode.

          proxied: Whether the record is receiving the performance and security benefits of
              Cloudflare.

          settings: Settings for the DNS record.

          tags: Custom tags for the DNS record. This field has no effect on DNS responses.

          ttl: Time To Live (TTL) of the DNS record in seconds. Setting to 1 means 'automatic'.
              Value must be between 60 and 86400, with the minimum reduced to 30 for
              Enterprise zones.

          type: Record type.

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
        comment: str | NotGiven = NOT_GIVEN,
        data: record_update_params.CERTRecordData | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        proxied: bool | NotGiven = NOT_GIVEN,
        settings: record_update_params.CERTRecordSettings | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        type: Literal["CERT"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[RecordResponse]:
        """
        Overwrite an existing DNS record.

        Notes:

        - A/AAAA records cannot exist on the same name as CNAME records.
        - NS records cannot exist on the same name as any other record type.
        - Domain names are always represented in Punycode, even if Unicode characters
          were used when creating the record.

        Args:
          zone_id: Identifier

          dns_record_id: Identifier

          comment: Comments or notes about the DNS record. This field has no effect on DNS
              responses.

          data: Components of a CERT record.

          name: DNS record name (or @ for the zone apex) in Punycode.

          proxied: Whether the record is receiving the performance and security benefits of
              Cloudflare.

          settings: Settings for the DNS record.

          tags: Custom tags for the DNS record. This field has no effect on DNS responses.

          ttl: Time To Live (TTL) of the DNS record in seconds. Setting to 1 means 'automatic'.
              Value must be between 60 and 86400, with the minimum reduced to 30 for
              Enterprise zones.

          type: Record type.

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
        comment: str | NotGiven = NOT_GIVEN,
        content: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        proxied: bool | NotGiven = NOT_GIVEN,
        settings: record_update_params.CNAMERecordSettings | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        type: Literal["CNAME"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[RecordResponse]:
        """
        Overwrite an existing DNS record.

        Notes:

        - A/AAAA records cannot exist on the same name as CNAME records.
        - NS records cannot exist on the same name as any other record type.
        - Domain names are always represented in Punycode, even if Unicode characters
          were used when creating the record.

        Args:
          zone_id: Identifier

          dns_record_id: Identifier

          comment: Comments or notes about the DNS record. This field has no effect on DNS
              responses.

          content: A valid hostname. Must not match the record's name.

          name: DNS record name (or @ for the zone apex) in Punycode.

          proxied: Whether the record is receiving the performance and security benefits of
              Cloudflare.

          settings: Settings for the DNS record.

          tags: Custom tags for the DNS record. This field has no effect on DNS responses.

          ttl: Time To Live (TTL) of the DNS record in seconds. Setting to 1 means 'automatic'.
              Value must be between 60 and 86400, with the minimum reduced to 30 for
              Enterprise zones.

          type: Record type.

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
        comment: str | NotGiven = NOT_GIVEN,
        data: record_update_params.DNSKEYRecordData | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        proxied: bool | NotGiven = NOT_GIVEN,
        settings: record_update_params.DNSKEYRecordSettings | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        type: Literal["DNSKEY"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[RecordResponse]:
        """
        Overwrite an existing DNS record.

        Notes:

        - A/AAAA records cannot exist on the same name as CNAME records.
        - NS records cannot exist on the same name as any other record type.
        - Domain names are always represented in Punycode, even if Unicode characters
          were used when creating the record.

        Args:
          zone_id: Identifier

          dns_record_id: Identifier

          comment: Comments or notes about the DNS record. This field has no effect on DNS
              responses.

          data: Components of a DNSKEY record.

          name: DNS record name (or @ for the zone apex) in Punycode.

          proxied: Whether the record is receiving the performance and security benefits of
              Cloudflare.

          settings: Settings for the DNS record.

          tags: Custom tags for the DNS record. This field has no effect on DNS responses.

          ttl: Time To Live (TTL) of the DNS record in seconds. Setting to 1 means 'automatic'.
              Value must be between 60 and 86400, with the minimum reduced to 30 for
              Enterprise zones.

          type: Record type.

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
        comment: str | NotGiven = NOT_GIVEN,
        data: record_update_params.DSRecordData | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        proxied: bool | NotGiven = NOT_GIVEN,
        settings: record_update_params.DSRecordSettings | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        type: Literal["DS"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[RecordResponse]:
        """
        Overwrite an existing DNS record.

        Notes:

        - A/AAAA records cannot exist on the same name as CNAME records.
        - NS records cannot exist on the same name as any other record type.
        - Domain names are always represented in Punycode, even if Unicode characters
          were used when creating the record.

        Args:
          zone_id: Identifier

          dns_record_id: Identifier

          comment: Comments or notes about the DNS record. This field has no effect on DNS
              responses.

          data: Components of a DS record.

          name: DNS record name (or @ for the zone apex) in Punycode.

          proxied: Whether the record is receiving the performance and security benefits of
              Cloudflare.

          settings: Settings for the DNS record.

          tags: Custom tags for the DNS record. This field has no effect on DNS responses.

          ttl: Time To Live (TTL) of the DNS record in seconds. Setting to 1 means 'automatic'.
              Value must be between 60 and 86400, with the minimum reduced to 30 for
              Enterprise zones.

          type: Record type.

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
        comment: str | NotGiven = NOT_GIVEN,
        data: record_update_params.HTTPSRecordData | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        proxied: bool | NotGiven = NOT_GIVEN,
        settings: record_update_params.HTTPSRecordSettings | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        type: Literal["HTTPS"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[RecordResponse]:
        """
        Overwrite an existing DNS record.

        Notes:

        - A/AAAA records cannot exist on the same name as CNAME records.
        - NS records cannot exist on the same name as any other record type.
        - Domain names are always represented in Punycode, even if Unicode characters
          were used when creating the record.

        Args:
          zone_id: Identifier

          dns_record_id: Identifier

          comment: Comments or notes about the DNS record. This field has no effect on DNS
              responses.

          data: Components of a HTTPS record.

          name: DNS record name (or @ for the zone apex) in Punycode.

          proxied: Whether the record is receiving the performance and security benefits of
              Cloudflare.

          settings: Settings for the DNS record.

          tags: Custom tags for the DNS record. This field has no effect on DNS responses.

          ttl: Time To Live (TTL) of the DNS record in seconds. Setting to 1 means 'automatic'.
              Value must be between 60 and 86400, with the minimum reduced to 30 for
              Enterprise zones.

          type: Record type.

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
        comment: str | NotGiven = NOT_GIVEN,
        data: record_update_params.LOCRecordData | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        proxied: bool | NotGiven = NOT_GIVEN,
        settings: record_update_params.LOCRecordSettings | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        type: Literal["LOC"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[RecordResponse]:
        """
        Overwrite an existing DNS record.

        Notes:

        - A/AAAA records cannot exist on the same name as CNAME records.
        - NS records cannot exist on the same name as any other record type.
        - Domain names are always represented in Punycode, even if Unicode characters
          were used when creating the record.

        Args:
          zone_id: Identifier

          dns_record_id: Identifier

          comment: Comments or notes about the DNS record. This field has no effect on DNS
              responses.

          data: Components of a LOC record.

          name: DNS record name (or @ for the zone apex) in Punycode.

          proxied: Whether the record is receiving the performance and security benefits of
              Cloudflare.

          settings: Settings for the DNS record.

          tags: Custom tags for the DNS record. This field has no effect on DNS responses.

          ttl: Time To Live (TTL) of the DNS record in seconds. Setting to 1 means 'automatic'.
              Value must be between 60 and 86400, with the minimum reduced to 30 for
              Enterprise zones.

          type: Record type.

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
        comment: str | NotGiven = NOT_GIVEN,
        content: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        priority: float | NotGiven = NOT_GIVEN,
        proxied: bool | NotGiven = NOT_GIVEN,
        settings: record_update_params.MXRecordSettings | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        type: Literal["MX"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[RecordResponse]:
        """
        Overwrite an existing DNS record.

        Notes:

        - A/AAAA records cannot exist on the same name as CNAME records.
        - NS records cannot exist on the same name as any other record type.
        - Domain names are always represented in Punycode, even if Unicode characters
          were used when creating the record.

        Args:
          zone_id: Identifier

          dns_record_id: Identifier

          comment: Comments or notes about the DNS record. This field has no effect on DNS
              responses.

          content: A valid mail server hostname.

          name: DNS record name (or @ for the zone apex) in Punycode.

          priority: Required for MX, SRV and URI records; unused by other record types. Records with
              lower priorities are preferred.

          proxied: Whether the record is receiving the performance and security benefits of
              Cloudflare.

          settings: Settings for the DNS record.

          tags: Custom tags for the DNS record. This field has no effect on DNS responses.

          ttl: Time To Live (TTL) of the DNS record in seconds. Setting to 1 means 'automatic'.
              Value must be between 60 and 86400, with the minimum reduced to 30 for
              Enterprise zones.

          type: Record type.

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
        comment: str | NotGiven = NOT_GIVEN,
        data: record_update_params.NAPTRRecordData | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        proxied: bool | NotGiven = NOT_GIVEN,
        settings: record_update_params.NAPTRRecordSettings | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        type: Literal["NAPTR"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[RecordResponse]:
        """
        Overwrite an existing DNS record.

        Notes:

        - A/AAAA records cannot exist on the same name as CNAME records.
        - NS records cannot exist on the same name as any other record type.
        - Domain names are always represented in Punycode, even if Unicode characters
          were used when creating the record.

        Args:
          zone_id: Identifier

          dns_record_id: Identifier

          comment: Comments or notes about the DNS record. This field has no effect on DNS
              responses.

          data: Components of a NAPTR record.

          name: DNS record name (or @ for the zone apex) in Punycode.

          proxied: Whether the record is receiving the performance and security benefits of
              Cloudflare.

          settings: Settings for the DNS record.

          tags: Custom tags for the DNS record. This field has no effect on DNS responses.

          ttl: Time To Live (TTL) of the DNS record in seconds. Setting to 1 means 'automatic'.
              Value must be between 60 and 86400, with the minimum reduced to 30 for
              Enterprise zones.

          type: Record type.

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
        comment: str | NotGiven = NOT_GIVEN,
        content: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        proxied: bool | NotGiven = NOT_GIVEN,
        settings: record_update_params.NSRecordSettings | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        type: Literal["NS"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[RecordResponse]:
        """
        Overwrite an existing DNS record.

        Notes:

        - A/AAAA records cannot exist on the same name as CNAME records.
        - NS records cannot exist on the same name as any other record type.
        - Domain names are always represented in Punycode, even if Unicode characters
          were used when creating the record.

        Args:
          zone_id: Identifier

          dns_record_id: Identifier

          comment: Comments or notes about the DNS record. This field has no effect on DNS
              responses.

          content: A valid name server host name.

          name: DNS record name (or @ for the zone apex) in Punycode.

          proxied: Whether the record is receiving the performance and security benefits of
              Cloudflare.

          settings: Settings for the DNS record.

          tags: Custom tags for the DNS record. This field has no effect on DNS responses.

          ttl: Time To Live (TTL) of the DNS record in seconds. Setting to 1 means 'automatic'.
              Value must be between 60 and 86400, with the minimum reduced to 30 for
              Enterprise zones.

          type: Record type.

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
        comment: str | NotGiven = NOT_GIVEN,
        content: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        proxied: bool | NotGiven = NOT_GIVEN,
        settings: record_update_params.DNSRecordsOpenpgpkeyRecordSettings | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        type: Literal["OPENPGPKEY"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[RecordResponse]:
        """
        Overwrite an existing DNS record.

        Notes:

        - A/AAAA records cannot exist on the same name as CNAME records.
        - NS records cannot exist on the same name as any other record type.
        - Domain names are always represented in Punycode, even if Unicode characters
          were used when creating the record.

        Args:
          zone_id: Identifier

          dns_record_id: Identifier

          comment: Comments or notes about the DNS record. This field has no effect on DNS
              responses.

          content: A single Base64-encoded OpenPGP Transferable Public Key (RFC 4880 Section 11.1)

          name: DNS record name (or @ for the zone apex) in Punycode.

          proxied: Whether the record is receiving the performance and security benefits of
              Cloudflare.

          settings: Settings for the DNS record.

          tags: Custom tags for the DNS record. This field has no effect on DNS responses.

          ttl: Time To Live (TTL) of the DNS record in seconds. Setting to 1 means 'automatic'.
              Value must be between 60 and 86400, with the minimum reduced to 30 for
              Enterprise zones.

          type: Record type.

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
        comment: str | NotGiven = NOT_GIVEN,
        content: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        proxied: bool | NotGiven = NOT_GIVEN,
        settings: record_update_params.PTRRecordSettings | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        type: Literal["PTR"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[RecordResponse]:
        """
        Overwrite an existing DNS record.

        Notes:

        - A/AAAA records cannot exist on the same name as CNAME records.
        - NS records cannot exist on the same name as any other record type.
        - Domain names are always represented in Punycode, even if Unicode characters
          were used when creating the record.

        Args:
          zone_id: Identifier

          dns_record_id: Identifier

          comment: Comments or notes about the DNS record. This field has no effect on DNS
              responses.

          content: Domain name pointing to the address.

          name: DNS record name (or @ for the zone apex) in Punycode.

          proxied: Whether the record is receiving the performance and security benefits of
              Cloudflare.

          settings: Settings for the DNS record.

          tags: Custom tags for the DNS record. This field has no effect on DNS responses.

          ttl: Time To Live (TTL) of the DNS record in seconds. Setting to 1 means 'automatic'.
              Value must be between 60 and 86400, with the minimum reduced to 30 for
              Enterprise zones.

          type: Record type.

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
        comment: str | NotGiven = NOT_GIVEN,
        data: record_update_params.SMIMEARecordData | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        proxied: bool | NotGiven = NOT_GIVEN,
        settings: record_update_params.SMIMEARecordSettings | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        type: Literal["SMIMEA"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[RecordResponse]:
        """
        Overwrite an existing DNS record.

        Notes:

        - A/AAAA records cannot exist on the same name as CNAME records.
        - NS records cannot exist on the same name as any other record type.
        - Domain names are always represented in Punycode, even if Unicode characters
          were used when creating the record.

        Args:
          zone_id: Identifier

          dns_record_id: Identifier

          comment: Comments or notes about the DNS record. This field has no effect on DNS
              responses.

          data: Components of a SMIMEA record.

          name: DNS record name (or @ for the zone apex) in Punycode.

          proxied: Whether the record is receiving the performance and security benefits of
              Cloudflare.

          settings: Settings for the DNS record.

          tags: Custom tags for the DNS record. This field has no effect on DNS responses.

          ttl: Time To Live (TTL) of the DNS record in seconds. Setting to 1 means 'automatic'.
              Value must be between 60 and 86400, with the minimum reduced to 30 for
              Enterprise zones.

          type: Record type.

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
        comment: str | NotGiven = NOT_GIVEN,
        data: record_update_params.SRVRecordData | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        proxied: bool | NotGiven = NOT_GIVEN,
        settings: record_update_params.SRVRecordSettings | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        type: Literal["SRV"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[RecordResponse]:
        """
        Overwrite an existing DNS record.

        Notes:

        - A/AAAA records cannot exist on the same name as CNAME records.
        - NS records cannot exist on the same name as any other record type.
        - Domain names are always represented in Punycode, even if Unicode characters
          were used when creating the record.

        Args:
          zone_id: Identifier

          dns_record_id: Identifier

          comment: Comments or notes about the DNS record. This field has no effect on DNS
              responses.

          data: Components of a SRV record.

          name: DNS record name (or @ for the zone apex) in Punycode.

          proxied: Whether the record is receiving the performance and security benefits of
              Cloudflare.

          settings: Settings for the DNS record.

          tags: Custom tags for the DNS record. This field has no effect on DNS responses.

          ttl: Time To Live (TTL) of the DNS record in seconds. Setting to 1 means 'automatic'.
              Value must be between 60 and 86400, with the minimum reduced to 30 for
              Enterprise zones.

          type: Record type.

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
        comment: str | NotGiven = NOT_GIVEN,
        data: record_update_params.SSHFPRecordData | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        proxied: bool | NotGiven = NOT_GIVEN,
        settings: record_update_params.SSHFPRecordSettings | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        type: Literal["SSHFP"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[RecordResponse]:
        """
        Overwrite an existing DNS record.

        Notes:

        - A/AAAA records cannot exist on the same name as CNAME records.
        - NS records cannot exist on the same name as any other record type.
        - Domain names are always represented in Punycode, even if Unicode characters
          were used when creating the record.

        Args:
          zone_id: Identifier

          dns_record_id: Identifier

          comment: Comments or notes about the DNS record. This field has no effect on DNS
              responses.

          data: Components of a SSHFP record.

          name: DNS record name (or @ for the zone apex) in Punycode.

          proxied: Whether the record is receiving the performance and security benefits of
              Cloudflare.

          settings: Settings for the DNS record.

          tags: Custom tags for the DNS record. This field has no effect on DNS responses.

          ttl: Time To Live (TTL) of the DNS record in seconds. Setting to 1 means 'automatic'.
              Value must be between 60 and 86400, with the minimum reduced to 30 for
              Enterprise zones.

          type: Record type.

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
        comment: str | NotGiven = NOT_GIVEN,
        data: record_update_params.SVCBRecordData | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        proxied: bool | NotGiven = NOT_GIVEN,
        settings: record_update_params.SVCBRecordSettings | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        type: Literal["SVCB"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[RecordResponse]:
        """
        Overwrite an existing DNS record.

        Notes:

        - A/AAAA records cannot exist on the same name as CNAME records.
        - NS records cannot exist on the same name as any other record type.
        - Domain names are always represented in Punycode, even if Unicode characters
          were used when creating the record.

        Args:
          zone_id: Identifier

          dns_record_id: Identifier

          comment: Comments or notes about the DNS record. This field has no effect on DNS
              responses.

          data: Components of a SVCB record.

          name: DNS record name (or @ for the zone apex) in Punycode.

          proxied: Whether the record is receiving the performance and security benefits of
              Cloudflare.

          settings: Settings for the DNS record.

          tags: Custom tags for the DNS record. This field has no effect on DNS responses.

          ttl: Time To Live (TTL) of the DNS record in seconds. Setting to 1 means 'automatic'.
              Value must be between 60 and 86400, with the minimum reduced to 30 for
              Enterprise zones.

          type: Record type.

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
        comment: str | NotGiven = NOT_GIVEN,
        data: record_update_params.TLSARecordData | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        proxied: bool | NotGiven = NOT_GIVEN,
        settings: record_update_params.TLSARecordSettings | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        type: Literal["TLSA"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[RecordResponse]:
        """
        Overwrite an existing DNS record.

        Notes:

        - A/AAAA records cannot exist on the same name as CNAME records.
        - NS records cannot exist on the same name as any other record type.
        - Domain names are always represented in Punycode, even if Unicode characters
          were used when creating the record.

        Args:
          zone_id: Identifier

          dns_record_id: Identifier

          comment: Comments or notes about the DNS record. This field has no effect on DNS
              responses.

          data: Components of a TLSA record.

          name: DNS record name (or @ for the zone apex) in Punycode.

          proxied: Whether the record is receiving the performance and security benefits of
              Cloudflare.

          settings: Settings for the DNS record.

          tags: Custom tags for the DNS record. This field has no effect on DNS responses.

          ttl: Time To Live (TTL) of the DNS record in seconds. Setting to 1 means 'automatic'.
              Value must be between 60 and 86400, with the minimum reduced to 30 for
              Enterprise zones.

          type: Record type.

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
        comment: str | NotGiven = NOT_GIVEN,
        content: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        proxied: bool | NotGiven = NOT_GIVEN,
        settings: record_update_params.TXTRecordSettings | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        type: Literal["TXT"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[RecordResponse]:
        """
        Overwrite an existing DNS record.

        Notes:

        - A/AAAA records cannot exist on the same name as CNAME records.
        - NS records cannot exist on the same name as any other record type.
        - Domain names are always represented in Punycode, even if Unicode characters
          were used when creating the record.

        Args:
          zone_id: Identifier

          dns_record_id: Identifier

          comment: Comments or notes about the DNS record. This field has no effect on DNS
              responses.

          content: Text content for the record. The content must consist of quoted "character
              strings" (RFC 1035), each with a length of up to 255 bytes. Strings exceeding
              this allowed maximum length are automatically split.

              Learn more at
              <https://www.cloudflare.com/learning/dns/dns-records/dns-txt-record/>.

          name: DNS record name (or @ for the zone apex) in Punycode.

          proxied: Whether the record is receiving the performance and security benefits of
              Cloudflare.

          settings: Settings for the DNS record.

          tags: Custom tags for the DNS record. This field has no effect on DNS responses.

          ttl: Time To Live (TTL) of the DNS record in seconds. Setting to 1 means 'automatic'.
              Value must be between 60 and 86400, with the minimum reduced to 30 for
              Enterprise zones.

          type: Record type.

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
        comment: str | NotGiven = NOT_GIVEN,
        data: record_update_params.URIRecordData | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        priority: float | NotGiven = NOT_GIVEN,
        proxied: bool | NotGiven = NOT_GIVEN,
        settings: record_update_params.URIRecordSettings | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        type: Literal["URI"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[RecordResponse]:
        """
        Overwrite an existing DNS record.

        Notes:

        - A/AAAA records cannot exist on the same name as CNAME records.
        - NS records cannot exist on the same name as any other record type.
        - Domain names are always represented in Punycode, even if Unicode characters
          were used when creating the record.

        Args:
          zone_id: Identifier

          dns_record_id: Identifier

          comment: Comments or notes about the DNS record. This field has no effect on DNS
              responses.

          data: Components of a URI record.

          name: DNS record name (or @ for the zone apex) in Punycode.

          priority: Required for MX, SRV and URI records; unused by other record types. Records with
              lower priorities are preferred.

          proxied: Whether the record is receiving the performance and security benefits of
              Cloudflare.

          settings: Settings for the DNS record.

          tags: Custom tags for the DNS record. This field has no effect on DNS responses.

          ttl: Time To Live (TTL) of the DNS record in seconds. Setting to 1 means 'automatic'.
              Value must be between 60 and 86400, with the minimum reduced to 30 for
              Enterprise zones.

          type: Record type.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["zone_id"])
    async def update(
        self,
        dns_record_id: str,
        *,
        zone_id: str,
        comment: str | NotGiven = NOT_GIVEN,
        content: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        proxied: bool | NotGiven = NOT_GIVEN,
        settings: record_update_params.ARecordSettings
        | record_update_params.CNAMERecordSettings
        | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
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
        | Literal["URI"]
        | NotGiven = NOT_GIVEN,
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
    ) -> Optional[RecordResponse]:
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not dns_record_id:
            raise ValueError(f"Expected a non-empty value for `dns_record_id` but received {dns_record_id!r}")
        return cast(
            Optional[RecordResponse],
            await self._put(
                f"/zones/{zone_id}/dns_records/{dns_record_id}",
                body=await async_maybe_transform(
                    {
                        "comment": comment,
                        "content": content,
                        "name": name,
                        "proxied": proxied,
                        "settings": settings,
                        "tags": tags,
                        "ttl": ttl,
                        "type": type,
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
                    post_parser=ResultWrapper[Optional[RecordResponse]]._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[RecordResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def list(
        self,
        *,
        zone_id: str,
        comment: record_list_params.Comment | NotGiven = NOT_GIVEN,
        content: record_list_params.Content | NotGiven = NOT_GIVEN,
        direction: SortDirection | NotGiven = NOT_GIVEN,
        match: Literal["any", "all"] | NotGiven = NOT_GIVEN,
        name: record_list_params.Name | NotGiven = NOT_GIVEN,
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
    ) -> AsyncPaginator[RecordResponse, AsyncV4PagePaginationArray[RecordResponse]]:
        """
        List, search, sort, and filter a zones' DNS records.

        Args:
          zone_id: Identifier

          direction: Direction to order DNS records in.

          match: Whether to match all search requirements or at least one (any). If set to `all`,
              acts like a logical AND between filters. If set to `any`, acts like a logical OR
              instead. Note that the interaction between tag filters is controlled by the
              `tag-match` parameter instead.

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
            page=AsyncV4PagePaginationArray[RecordResponse],
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
            model=cast(Any, RecordResponse),  # Union types cannot be passed in as arguments in the type system
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

    async def batch(
        self,
        *,
        zone_id: str,
        deletes: Iterable[record_batch_params.Delete] | NotGiven = NOT_GIVEN,
        patches: Iterable[BatchPatchParam] | NotGiven = NOT_GIVEN,
        posts: Iterable[RecordParam] | NotGiven = NOT_GIVEN,
        puts: Iterable[BatchPutParam] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[RecordBatchResponse]:
        """
        Send a Batch of DNS Record API calls to be executed together.

        Notes:

        - Although Cloudflare will execute the batched operations in a single database
          transaction, Cloudflare's distributed KV store must treat each record change
          as a single key-value pair. This means that the propagation of changes is not
          atomic. See
          [the documentation](https://developers.cloudflare.com/dns/manage-dns-records/how-to/batch-record-changes/ "Batch DNS records")
          for more information.
        - The operations you specify within the /batch request body are always executed
          in the following order:

          - Deletes
          - Patches
          - Puts
          - Posts

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
            f"/zones/{zone_id}/dns_records/batch",
            body=await async_maybe_transform(
                {
                    "deletes": deletes,
                    "patches": patches,
                    "posts": posts,
                    "puts": puts,
                },
                record_batch_params.RecordBatchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[RecordBatchResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[RecordBatchResponse]], ResultWrapper[RecordBatchResponse]),
        )

    @overload
    async def edit(
        self,
        dns_record_id: str,
        *,
        zone_id: str,
        comment: str | NotGiven = NOT_GIVEN,
        content: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        proxied: bool | NotGiven = NOT_GIVEN,
        settings: record_edit_params.ARecordSettings | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        type: Literal["A"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[RecordResponse]:
        """
        Update an existing DNS record.

        Notes:

        - A/AAAA records cannot exist on the same name as CNAME records.
        - NS records cannot exist on the same name as any other record type.
        - Domain names are always represented in Punycode, even if Unicode characters
          were used when creating the record.

        Args:
          zone_id: Identifier

          dns_record_id: Identifier

          comment: Comments or notes about the DNS record. This field has no effect on DNS
              responses.

          content: A valid IPv4 address.

          name: DNS record name (or @ for the zone apex) in Punycode.

          proxied: Whether the record is receiving the performance and security benefits of
              Cloudflare.

          settings: Settings for the DNS record.

          tags: Custom tags for the DNS record. This field has no effect on DNS responses.

          ttl: Time To Live (TTL) of the DNS record in seconds. Setting to 1 means 'automatic'.
              Value must be between 60 and 86400, with the minimum reduced to 30 for
              Enterprise zones.

          type: Record type.

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
        comment: str | NotGiven = NOT_GIVEN,
        content: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        proxied: bool | NotGiven = NOT_GIVEN,
        settings: record_edit_params.AAAARecordSettings | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        type: Literal["AAAA"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[RecordResponse]:
        """
        Update an existing DNS record.

        Notes:

        - A/AAAA records cannot exist on the same name as CNAME records.
        - NS records cannot exist on the same name as any other record type.
        - Domain names are always represented in Punycode, even if Unicode characters
          were used when creating the record.

        Args:
          zone_id: Identifier

          dns_record_id: Identifier

          comment: Comments or notes about the DNS record. This field has no effect on DNS
              responses.

          content: A valid IPv6 address.

          name: DNS record name (or @ for the zone apex) in Punycode.

          proxied: Whether the record is receiving the performance and security benefits of
              Cloudflare.

          settings: Settings for the DNS record.

          tags: Custom tags for the DNS record. This field has no effect on DNS responses.

          ttl: Time To Live (TTL) of the DNS record in seconds. Setting to 1 means 'automatic'.
              Value must be between 60 and 86400, with the minimum reduced to 30 for
              Enterprise zones.

          type: Record type.

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
        comment: str | NotGiven = NOT_GIVEN,
        data: record_edit_params.CAARecordData | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        proxied: bool | NotGiven = NOT_GIVEN,
        settings: record_edit_params.CAARecordSettings | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        type: Literal["CAA"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[RecordResponse]:
        """
        Update an existing DNS record.

        Notes:

        - A/AAAA records cannot exist on the same name as CNAME records.
        - NS records cannot exist on the same name as any other record type.
        - Domain names are always represented in Punycode, even if Unicode characters
          were used when creating the record.

        Args:
          zone_id: Identifier

          dns_record_id: Identifier

          comment: Comments or notes about the DNS record. This field has no effect on DNS
              responses.

          data: Components of a CAA record.

          name: DNS record name (or @ for the zone apex) in Punycode.

          proxied: Whether the record is receiving the performance and security benefits of
              Cloudflare.

          settings: Settings for the DNS record.

          tags: Custom tags for the DNS record. This field has no effect on DNS responses.

          ttl: Time To Live (TTL) of the DNS record in seconds. Setting to 1 means 'automatic'.
              Value must be between 60 and 86400, with the minimum reduced to 30 for
              Enterprise zones.

          type: Record type.

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
        comment: str | NotGiven = NOT_GIVEN,
        data: record_edit_params.CERTRecordData | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        proxied: bool | NotGiven = NOT_GIVEN,
        settings: record_edit_params.CERTRecordSettings | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        type: Literal["CERT"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[RecordResponse]:
        """
        Update an existing DNS record.

        Notes:

        - A/AAAA records cannot exist on the same name as CNAME records.
        - NS records cannot exist on the same name as any other record type.
        - Domain names are always represented in Punycode, even if Unicode characters
          were used when creating the record.

        Args:
          zone_id: Identifier

          dns_record_id: Identifier

          comment: Comments or notes about the DNS record. This field has no effect on DNS
              responses.

          data: Components of a CERT record.

          name: DNS record name (or @ for the zone apex) in Punycode.

          proxied: Whether the record is receiving the performance and security benefits of
              Cloudflare.

          settings: Settings for the DNS record.

          tags: Custom tags for the DNS record. This field has no effect on DNS responses.

          ttl: Time To Live (TTL) of the DNS record in seconds. Setting to 1 means 'automatic'.
              Value must be between 60 and 86400, with the minimum reduced to 30 for
              Enterprise zones.

          type: Record type.

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
        comment: str | NotGiven = NOT_GIVEN,
        content: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        proxied: bool | NotGiven = NOT_GIVEN,
        settings: record_edit_params.CNAMERecordSettings | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        type: Literal["CNAME"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[RecordResponse]:
        """
        Update an existing DNS record.

        Notes:

        - A/AAAA records cannot exist on the same name as CNAME records.
        - NS records cannot exist on the same name as any other record type.
        - Domain names are always represented in Punycode, even if Unicode characters
          were used when creating the record.

        Args:
          zone_id: Identifier

          dns_record_id: Identifier

          comment: Comments or notes about the DNS record. This field has no effect on DNS
              responses.

          content: A valid hostname. Must not match the record's name.

          name: DNS record name (or @ for the zone apex) in Punycode.

          proxied: Whether the record is receiving the performance and security benefits of
              Cloudflare.

          settings: Settings for the DNS record.

          tags: Custom tags for the DNS record. This field has no effect on DNS responses.

          ttl: Time To Live (TTL) of the DNS record in seconds. Setting to 1 means 'automatic'.
              Value must be between 60 and 86400, with the minimum reduced to 30 for
              Enterprise zones.

          type: Record type.

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
        comment: str | NotGiven = NOT_GIVEN,
        data: record_edit_params.DNSKEYRecordData | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        proxied: bool | NotGiven = NOT_GIVEN,
        settings: record_edit_params.DNSKEYRecordSettings | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        type: Literal["DNSKEY"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[RecordResponse]:
        """
        Update an existing DNS record.

        Notes:

        - A/AAAA records cannot exist on the same name as CNAME records.
        - NS records cannot exist on the same name as any other record type.
        - Domain names are always represented in Punycode, even if Unicode characters
          were used when creating the record.

        Args:
          zone_id: Identifier

          dns_record_id: Identifier

          comment: Comments or notes about the DNS record. This field has no effect on DNS
              responses.

          data: Components of a DNSKEY record.

          name: DNS record name (or @ for the zone apex) in Punycode.

          proxied: Whether the record is receiving the performance and security benefits of
              Cloudflare.

          settings: Settings for the DNS record.

          tags: Custom tags for the DNS record. This field has no effect on DNS responses.

          ttl: Time To Live (TTL) of the DNS record in seconds. Setting to 1 means 'automatic'.
              Value must be between 60 and 86400, with the minimum reduced to 30 for
              Enterprise zones.

          type: Record type.

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
        comment: str | NotGiven = NOT_GIVEN,
        data: record_edit_params.DSRecordData | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        proxied: bool | NotGiven = NOT_GIVEN,
        settings: record_edit_params.DSRecordSettings | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        type: Literal["DS"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[RecordResponse]:
        """
        Update an existing DNS record.

        Notes:

        - A/AAAA records cannot exist on the same name as CNAME records.
        - NS records cannot exist on the same name as any other record type.
        - Domain names are always represented in Punycode, even if Unicode characters
          were used when creating the record.

        Args:
          zone_id: Identifier

          dns_record_id: Identifier

          comment: Comments or notes about the DNS record. This field has no effect on DNS
              responses.

          data: Components of a DS record.

          name: DNS record name (or @ for the zone apex) in Punycode.

          proxied: Whether the record is receiving the performance and security benefits of
              Cloudflare.

          settings: Settings for the DNS record.

          tags: Custom tags for the DNS record. This field has no effect on DNS responses.

          ttl: Time To Live (TTL) of the DNS record in seconds. Setting to 1 means 'automatic'.
              Value must be between 60 and 86400, with the minimum reduced to 30 for
              Enterprise zones.

          type: Record type.

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
        comment: str | NotGiven = NOT_GIVEN,
        data: record_edit_params.HTTPSRecordData | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        proxied: bool | NotGiven = NOT_GIVEN,
        settings: record_edit_params.HTTPSRecordSettings | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        type: Literal["HTTPS"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[RecordResponse]:
        """
        Update an existing DNS record.

        Notes:

        - A/AAAA records cannot exist on the same name as CNAME records.
        - NS records cannot exist on the same name as any other record type.
        - Domain names are always represented in Punycode, even if Unicode characters
          were used when creating the record.

        Args:
          zone_id: Identifier

          dns_record_id: Identifier

          comment: Comments or notes about the DNS record. This field has no effect on DNS
              responses.

          data: Components of a HTTPS record.

          name: DNS record name (or @ for the zone apex) in Punycode.

          proxied: Whether the record is receiving the performance and security benefits of
              Cloudflare.

          settings: Settings for the DNS record.

          tags: Custom tags for the DNS record. This field has no effect on DNS responses.

          ttl: Time To Live (TTL) of the DNS record in seconds. Setting to 1 means 'automatic'.
              Value must be between 60 and 86400, with the minimum reduced to 30 for
              Enterprise zones.

          type: Record type.

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
        comment: str | NotGiven = NOT_GIVEN,
        data: record_edit_params.LOCRecordData | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        proxied: bool | NotGiven = NOT_GIVEN,
        settings: record_edit_params.LOCRecordSettings | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        type: Literal["LOC"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[RecordResponse]:
        """
        Update an existing DNS record.

        Notes:

        - A/AAAA records cannot exist on the same name as CNAME records.
        - NS records cannot exist on the same name as any other record type.
        - Domain names are always represented in Punycode, even if Unicode characters
          were used when creating the record.

        Args:
          zone_id: Identifier

          dns_record_id: Identifier

          comment: Comments or notes about the DNS record. This field has no effect on DNS
              responses.

          data: Components of a LOC record.

          name: DNS record name (or @ for the zone apex) in Punycode.

          proxied: Whether the record is receiving the performance and security benefits of
              Cloudflare.

          settings: Settings for the DNS record.

          tags: Custom tags for the DNS record. This field has no effect on DNS responses.

          ttl: Time To Live (TTL) of the DNS record in seconds. Setting to 1 means 'automatic'.
              Value must be between 60 and 86400, with the minimum reduced to 30 for
              Enterprise zones.

          type: Record type.

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
        comment: str | NotGiven = NOT_GIVEN,
        content: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        priority: float | NotGiven = NOT_GIVEN,
        proxied: bool | NotGiven = NOT_GIVEN,
        settings: record_edit_params.MXRecordSettings | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        type: Literal["MX"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[RecordResponse]:
        """
        Update an existing DNS record.

        Notes:

        - A/AAAA records cannot exist on the same name as CNAME records.
        - NS records cannot exist on the same name as any other record type.
        - Domain names are always represented in Punycode, even if Unicode characters
          were used when creating the record.

        Args:
          zone_id: Identifier

          dns_record_id: Identifier

          comment: Comments or notes about the DNS record. This field has no effect on DNS
              responses.

          content: A valid mail server hostname.

          name: DNS record name (or @ for the zone apex) in Punycode.

          priority: Required for MX, SRV and URI records; unused by other record types. Records with
              lower priorities are preferred.

          proxied: Whether the record is receiving the performance and security benefits of
              Cloudflare.

          settings: Settings for the DNS record.

          tags: Custom tags for the DNS record. This field has no effect on DNS responses.

          ttl: Time To Live (TTL) of the DNS record in seconds. Setting to 1 means 'automatic'.
              Value must be between 60 and 86400, with the minimum reduced to 30 for
              Enterprise zones.

          type: Record type.

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
        comment: str | NotGiven = NOT_GIVEN,
        data: record_edit_params.NAPTRRecordData | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        proxied: bool | NotGiven = NOT_GIVEN,
        settings: record_edit_params.NAPTRRecordSettings | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        type: Literal["NAPTR"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[RecordResponse]:
        """
        Update an existing DNS record.

        Notes:

        - A/AAAA records cannot exist on the same name as CNAME records.
        - NS records cannot exist on the same name as any other record type.
        - Domain names are always represented in Punycode, even if Unicode characters
          were used when creating the record.

        Args:
          zone_id: Identifier

          dns_record_id: Identifier

          comment: Comments or notes about the DNS record. This field has no effect on DNS
              responses.

          data: Components of a NAPTR record.

          name: DNS record name (or @ for the zone apex) in Punycode.

          proxied: Whether the record is receiving the performance and security benefits of
              Cloudflare.

          settings: Settings for the DNS record.

          tags: Custom tags for the DNS record. This field has no effect on DNS responses.

          ttl: Time To Live (TTL) of the DNS record in seconds. Setting to 1 means 'automatic'.
              Value must be between 60 and 86400, with the minimum reduced to 30 for
              Enterprise zones.

          type: Record type.

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
        comment: str | NotGiven = NOT_GIVEN,
        content: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        proxied: bool | NotGiven = NOT_GIVEN,
        settings: record_edit_params.NSRecordSettings | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        type: Literal["NS"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[RecordResponse]:
        """
        Update an existing DNS record.

        Notes:

        - A/AAAA records cannot exist on the same name as CNAME records.
        - NS records cannot exist on the same name as any other record type.
        - Domain names are always represented in Punycode, even if Unicode characters
          were used when creating the record.

        Args:
          zone_id: Identifier

          dns_record_id: Identifier

          comment: Comments or notes about the DNS record. This field has no effect on DNS
              responses.

          content: A valid name server host name.

          name: DNS record name (or @ for the zone apex) in Punycode.

          proxied: Whether the record is receiving the performance and security benefits of
              Cloudflare.

          settings: Settings for the DNS record.

          tags: Custom tags for the DNS record. This field has no effect on DNS responses.

          ttl: Time To Live (TTL) of the DNS record in seconds. Setting to 1 means 'automatic'.
              Value must be between 60 and 86400, with the minimum reduced to 30 for
              Enterprise zones.

          type: Record type.

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
        comment: str | NotGiven = NOT_GIVEN,
        content: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        proxied: bool | NotGiven = NOT_GIVEN,
        settings: record_edit_params.DNSRecordsOpenpgpkeyRecordSettings | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        type: Literal["OPENPGPKEY"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[RecordResponse]:
        """
        Update an existing DNS record.

        Notes:

        - A/AAAA records cannot exist on the same name as CNAME records.
        - NS records cannot exist on the same name as any other record type.
        - Domain names are always represented in Punycode, even if Unicode characters
          were used when creating the record.

        Args:
          zone_id: Identifier

          dns_record_id: Identifier

          comment: Comments or notes about the DNS record. This field has no effect on DNS
              responses.

          content: A single Base64-encoded OpenPGP Transferable Public Key (RFC 4880 Section 11.1)

          name: DNS record name (or @ for the zone apex) in Punycode.

          proxied: Whether the record is receiving the performance and security benefits of
              Cloudflare.

          settings: Settings for the DNS record.

          tags: Custom tags for the DNS record. This field has no effect on DNS responses.

          ttl: Time To Live (TTL) of the DNS record in seconds. Setting to 1 means 'automatic'.
              Value must be between 60 and 86400, with the minimum reduced to 30 for
              Enterprise zones.

          type: Record type.

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
        comment: str | NotGiven = NOT_GIVEN,
        content: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        proxied: bool | NotGiven = NOT_GIVEN,
        settings: record_edit_params.PTRRecordSettings | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        type: Literal["PTR"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[RecordResponse]:
        """
        Update an existing DNS record.

        Notes:

        - A/AAAA records cannot exist on the same name as CNAME records.
        - NS records cannot exist on the same name as any other record type.
        - Domain names are always represented in Punycode, even if Unicode characters
          were used when creating the record.

        Args:
          zone_id: Identifier

          dns_record_id: Identifier

          comment: Comments or notes about the DNS record. This field has no effect on DNS
              responses.

          content: Domain name pointing to the address.

          name: DNS record name (or @ for the zone apex) in Punycode.

          proxied: Whether the record is receiving the performance and security benefits of
              Cloudflare.

          settings: Settings for the DNS record.

          tags: Custom tags for the DNS record. This field has no effect on DNS responses.

          ttl: Time To Live (TTL) of the DNS record in seconds. Setting to 1 means 'automatic'.
              Value must be between 60 and 86400, with the minimum reduced to 30 for
              Enterprise zones.

          type: Record type.

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
        comment: str | NotGiven = NOT_GIVEN,
        data: record_edit_params.SMIMEARecordData | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        proxied: bool | NotGiven = NOT_GIVEN,
        settings: record_edit_params.SMIMEARecordSettings | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        type: Literal["SMIMEA"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[RecordResponse]:
        """
        Update an existing DNS record.

        Notes:

        - A/AAAA records cannot exist on the same name as CNAME records.
        - NS records cannot exist on the same name as any other record type.
        - Domain names are always represented in Punycode, even if Unicode characters
          were used when creating the record.

        Args:
          zone_id: Identifier

          dns_record_id: Identifier

          comment: Comments or notes about the DNS record. This field has no effect on DNS
              responses.

          data: Components of a SMIMEA record.

          name: DNS record name (or @ for the zone apex) in Punycode.

          proxied: Whether the record is receiving the performance and security benefits of
              Cloudflare.

          settings: Settings for the DNS record.

          tags: Custom tags for the DNS record. This field has no effect on DNS responses.

          ttl: Time To Live (TTL) of the DNS record in seconds. Setting to 1 means 'automatic'.
              Value must be between 60 and 86400, with the minimum reduced to 30 for
              Enterprise zones.

          type: Record type.

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
        comment: str | NotGiven = NOT_GIVEN,
        data: record_edit_params.SRVRecordData | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        proxied: bool | NotGiven = NOT_GIVEN,
        settings: record_edit_params.SRVRecordSettings | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        type: Literal["SRV"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[RecordResponse]:
        """
        Update an existing DNS record.

        Notes:

        - A/AAAA records cannot exist on the same name as CNAME records.
        - NS records cannot exist on the same name as any other record type.
        - Domain names are always represented in Punycode, even if Unicode characters
          were used when creating the record.

        Args:
          zone_id: Identifier

          dns_record_id: Identifier

          comment: Comments or notes about the DNS record. This field has no effect on DNS
              responses.

          data: Components of a SRV record.

          name: DNS record name (or @ for the zone apex) in Punycode.

          proxied: Whether the record is receiving the performance and security benefits of
              Cloudflare.

          settings: Settings for the DNS record.

          tags: Custom tags for the DNS record. This field has no effect on DNS responses.

          ttl: Time To Live (TTL) of the DNS record in seconds. Setting to 1 means 'automatic'.
              Value must be between 60 and 86400, with the minimum reduced to 30 for
              Enterprise zones.

          type: Record type.

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
        comment: str | NotGiven = NOT_GIVEN,
        data: record_edit_params.SSHFPRecordData | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        proxied: bool | NotGiven = NOT_GIVEN,
        settings: record_edit_params.SSHFPRecordSettings | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        type: Literal["SSHFP"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[RecordResponse]:
        """
        Update an existing DNS record.

        Notes:

        - A/AAAA records cannot exist on the same name as CNAME records.
        - NS records cannot exist on the same name as any other record type.
        - Domain names are always represented in Punycode, even if Unicode characters
          were used when creating the record.

        Args:
          zone_id: Identifier

          dns_record_id: Identifier

          comment: Comments or notes about the DNS record. This field has no effect on DNS
              responses.

          data: Components of a SSHFP record.

          name: DNS record name (or @ for the zone apex) in Punycode.

          proxied: Whether the record is receiving the performance and security benefits of
              Cloudflare.

          settings: Settings for the DNS record.

          tags: Custom tags for the DNS record. This field has no effect on DNS responses.

          ttl: Time To Live (TTL) of the DNS record in seconds. Setting to 1 means 'automatic'.
              Value must be between 60 and 86400, with the minimum reduced to 30 for
              Enterprise zones.

          type: Record type.

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
        comment: str | NotGiven = NOT_GIVEN,
        data: record_edit_params.SVCBRecordData | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        proxied: bool | NotGiven = NOT_GIVEN,
        settings: record_edit_params.SVCBRecordSettings | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        type: Literal["SVCB"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[RecordResponse]:
        """
        Update an existing DNS record.

        Notes:

        - A/AAAA records cannot exist on the same name as CNAME records.
        - NS records cannot exist on the same name as any other record type.
        - Domain names are always represented in Punycode, even if Unicode characters
          were used when creating the record.

        Args:
          zone_id: Identifier

          dns_record_id: Identifier

          comment: Comments or notes about the DNS record. This field has no effect on DNS
              responses.

          data: Components of a SVCB record.

          name: DNS record name (or @ for the zone apex) in Punycode.

          proxied: Whether the record is receiving the performance and security benefits of
              Cloudflare.

          settings: Settings for the DNS record.

          tags: Custom tags for the DNS record. This field has no effect on DNS responses.

          ttl: Time To Live (TTL) of the DNS record in seconds. Setting to 1 means 'automatic'.
              Value must be between 60 and 86400, with the minimum reduced to 30 for
              Enterprise zones.

          type: Record type.

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
        comment: str | NotGiven = NOT_GIVEN,
        data: record_edit_params.TLSARecordData | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        proxied: bool | NotGiven = NOT_GIVEN,
        settings: record_edit_params.TLSARecordSettings | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        type: Literal["TLSA"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[RecordResponse]:
        """
        Update an existing DNS record.

        Notes:

        - A/AAAA records cannot exist on the same name as CNAME records.
        - NS records cannot exist on the same name as any other record type.
        - Domain names are always represented in Punycode, even if Unicode characters
          were used when creating the record.

        Args:
          zone_id: Identifier

          dns_record_id: Identifier

          comment: Comments or notes about the DNS record. This field has no effect on DNS
              responses.

          data: Components of a TLSA record.

          name: DNS record name (or @ for the zone apex) in Punycode.

          proxied: Whether the record is receiving the performance and security benefits of
              Cloudflare.

          settings: Settings for the DNS record.

          tags: Custom tags for the DNS record. This field has no effect on DNS responses.

          ttl: Time To Live (TTL) of the DNS record in seconds. Setting to 1 means 'automatic'.
              Value must be between 60 and 86400, with the minimum reduced to 30 for
              Enterprise zones.

          type: Record type.

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
        comment: str | NotGiven = NOT_GIVEN,
        content: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        proxied: bool | NotGiven = NOT_GIVEN,
        settings: record_edit_params.TXTRecordSettings | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        type: Literal["TXT"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[RecordResponse]:
        """
        Update an existing DNS record.

        Notes:

        - A/AAAA records cannot exist on the same name as CNAME records.
        - NS records cannot exist on the same name as any other record type.
        - Domain names are always represented in Punycode, even if Unicode characters
          were used when creating the record.

        Args:
          zone_id: Identifier

          dns_record_id: Identifier

          comment: Comments or notes about the DNS record. This field has no effect on DNS
              responses.

          content: Text content for the record. The content must consist of quoted "character
              strings" (RFC 1035), each with a length of up to 255 bytes. Strings exceeding
              this allowed maximum length are automatically split.

              Learn more at
              <https://www.cloudflare.com/learning/dns/dns-records/dns-txt-record/>.

          name: DNS record name (or @ for the zone apex) in Punycode.

          proxied: Whether the record is receiving the performance and security benefits of
              Cloudflare.

          settings: Settings for the DNS record.

          tags: Custom tags for the DNS record. This field has no effect on DNS responses.

          ttl: Time To Live (TTL) of the DNS record in seconds. Setting to 1 means 'automatic'.
              Value must be between 60 and 86400, with the minimum reduced to 30 for
              Enterprise zones.

          type: Record type.

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
        comment: str | NotGiven = NOT_GIVEN,
        data: record_edit_params.URIRecordData | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        priority: float | NotGiven = NOT_GIVEN,
        proxied: bool | NotGiven = NOT_GIVEN,
        settings: record_edit_params.URIRecordSettings | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
        type: Literal["URI"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[RecordResponse]:
        """
        Update an existing DNS record.

        Notes:

        - A/AAAA records cannot exist on the same name as CNAME records.
        - NS records cannot exist on the same name as any other record type.
        - Domain names are always represented in Punycode, even if Unicode characters
          were used when creating the record.

        Args:
          zone_id: Identifier

          dns_record_id: Identifier

          comment: Comments or notes about the DNS record. This field has no effect on DNS
              responses.

          data: Components of a URI record.

          name: DNS record name (or @ for the zone apex) in Punycode.

          priority: Required for MX, SRV and URI records; unused by other record types. Records with
              lower priorities are preferred.

          proxied: Whether the record is receiving the performance and security benefits of
              Cloudflare.

          settings: Settings for the DNS record.

          tags: Custom tags for the DNS record. This field has no effect on DNS responses.

          ttl: Time To Live (TTL) of the DNS record in seconds. Setting to 1 means 'automatic'.
              Value must be between 60 and 86400, with the minimum reduced to 30 for
              Enterprise zones.

          type: Record type.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["zone_id"])
    async def edit(
        self,
        dns_record_id: str,
        *,
        zone_id: str,
        comment: str | NotGiven = NOT_GIVEN,
        content: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        proxied: bool | NotGiven = NOT_GIVEN,
        settings: record_edit_params.ARecordSettings | record_edit_params.CNAMERecordSettings | NotGiven = NOT_GIVEN,
        tags: List[RecordTags] | NotGiven = NOT_GIVEN,
        ttl: TTLParam | NotGiven = NOT_GIVEN,
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
        | Literal["URI"]
        | NotGiven = NOT_GIVEN,
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
    ) -> Optional[RecordResponse]:
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not dns_record_id:
            raise ValueError(f"Expected a non-empty value for `dns_record_id` but received {dns_record_id!r}")
        return cast(
            Optional[RecordResponse],
            await self._patch(
                f"/zones/{zone_id}/dns_records/{dns_record_id}",
                body=await async_maybe_transform(
                    {
                        "comment": comment,
                        "content": content,
                        "name": name,
                        "proxied": proxied,
                        "settings": settings,
                        "tags": tags,
                        "ttl": ttl,
                        "type": type,
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
                    post_parser=ResultWrapper[Optional[RecordResponse]]._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[RecordResponse]
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
    ) -> Optional[RecordResponse]:
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
            Optional[RecordResponse],
            await self._get(
                f"/zones/{zone_id}/dns_records/{dns_record_id}",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper[Optional[RecordResponse]]._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[RecordResponse]
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
        self.batch = to_raw_response_wrapper(
            records.batch,
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
        self.batch = async_to_raw_response_wrapper(
            records.batch,
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
        self.batch = to_streamed_response_wrapper(
            records.batch,
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
        self.batch = async_to_streamed_response_wrapper(
            records.batch,
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
