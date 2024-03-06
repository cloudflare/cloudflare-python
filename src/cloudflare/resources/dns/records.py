# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Any, List, Type, Union, Optional, cast
from typing_extensions import Literal

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
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
    RecordGetResponse,
    RecordEditResponse,
    RecordListResponse,
    RecordScanResponse,
    RecordCreateResponse,
    RecordDeleteResponse,
    RecordImportResponse,
    RecordUpdateResponse,
    record_edit_params,
    record_list_params,
    record_create_params,
    record_import_params,
    record_update_params,
)
from ...pagination import SyncV4PagePaginationArray, AsyncV4PagePaginationArray
from ..._base_client import (
    AsyncPaginator,
    make_request_options,
)

__all__ = ["Records", "AsyncRecords"]


class Records(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RecordsWithRawResponse:
        return RecordsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RecordsWithStreamingResponse:
        return RecordsWithStreamingResponse(self)

    def create(
        self,
        *,
        zone_id: str,
        name: str,
        type: Literal["URI"],
        comment: str | NotGiven = NOT_GIVEN,
        data: record_create_params.Data | NotGiven = NOT_GIVEN,
        meta: record_create_params.Meta | NotGiven = NOT_GIVEN,
        priority: float | NotGiven = NOT_GIVEN,
        proxied: bool | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        ttl: Union[float, Literal[1]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RecordCreateResponse:
        """
        Create a new DNS record for a zone.

        Notes:

        - A/AAAA records cannot exist on the same name as CNAME records.
        - NS records cannot exist on the same name as any other record type.
        - Domain names are always represented in Punycode, even if Unicode characters
          were used when creating the record.

        Args:
          zone_id: Identifier

          name: DNS record name (or @ for the zone apex) in Punycode.

          type: Record type.

          comment: Comments or notes about the DNS record. This field has no effect on DNS
              responses.

          priority: Required for MX, SRV and URI records; unused by other record types. Records with
              lower priorities are preferred.

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
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return cast(
            RecordCreateResponse,
            self._post(
                f"/zones/{zone_id}/dns_records",
                body=maybe_transform(
                    {
                        "name": name,
                        "type": type,
                        "comment": comment,
                        "data": data,
                        "meta": meta,
                        "priority": priority,
                        "proxied": proxied,
                        "tags": tags,
                        "ttl": ttl,
                    },
                    record_create_params.RecordCreateParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[RecordCreateResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def update(
        self,
        dns_record_id: str,
        *,
        zone_id: str,
        name: str,
        type: Literal["URI"],
        comment: str | NotGiven = NOT_GIVEN,
        data: record_update_params.Data | NotGiven = NOT_GIVEN,
        meta: record_update_params.Meta | NotGiven = NOT_GIVEN,
        priority: float | NotGiven = NOT_GIVEN,
        proxied: bool | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        ttl: Union[float, Literal[1]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RecordUpdateResponse:
        """Overwrite an existing DNS record.

        Notes:

        - A/AAAA records cannot exist on the same name as CNAME records.
        - NS records cannot exist on the same name as any other record type.
        - Domain names are always represented in Punycode, even if Unicode characters
          were used when creating the record.

        Args:
          zone_id: Identifier

          dns_record_id: Identifier

          name: DNS record name (or @ for the zone apex) in Punycode.

          type: Record type.

          comment: Comments or notes about the DNS record. This field has no effect on DNS
              responses.

          priority: Required for MX, SRV and URI records; unused by other record types. Records with
              lower priorities are preferred.

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
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not dns_record_id:
            raise ValueError(f"Expected a non-empty value for `dns_record_id` but received {dns_record_id!r}")
        return cast(
            RecordUpdateResponse,
            self._put(
                f"/zones/{zone_id}/dns_records/{dns_record_id}",
                body=maybe_transform(
                    {
                        "name": name,
                        "type": type,
                        "comment": comment,
                        "data": data,
                        "meta": meta,
                        "priority": priority,
                        "proxied": proxied,
                        "tags": tags,
                        "ttl": ttl,
                    },
                    record_update_params.RecordUpdateParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[RecordUpdateResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def list(
        self,
        *,
        zone_id: str,
        comment: record_list_params.Comment | NotGiven = NOT_GIVEN,
        content: str | NotGiven = NOT_GIVEN,
        direction: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
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
    ) -> SyncV4PagePaginationArray[RecordListResponse]:
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
            page=SyncV4PagePaginationArray[RecordListResponse],
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
            model=cast(Any, RecordListResponse),  # Union types cannot be passed in as arguments in the type system
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
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[RecordDeleteResponse]], ResultWrapper[RecordDeleteResponse]),
        )

    def edit(
        self,
        dns_record_id: str,
        *,
        zone_id: str,
        name: str,
        type: Literal["URI"],
        comment: str | NotGiven = NOT_GIVEN,
        data: record_edit_params.Data | NotGiven = NOT_GIVEN,
        meta: record_edit_params.Meta | NotGiven = NOT_GIVEN,
        priority: float | NotGiven = NOT_GIVEN,
        proxied: bool | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        ttl: Union[float, Literal[1]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RecordEditResponse:
        """Update an existing DNS record.

        Notes:

        - A/AAAA records cannot exist on the same name as CNAME records.
        - NS records cannot exist on the same name as any other record type.
        - Domain names are always represented in Punycode, even if Unicode characters
          were used when creating the record.

        Args:
          zone_id: Identifier

          dns_record_id: Identifier

          name: DNS record name (or @ for the zone apex) in Punycode.

          type: Record type.

          comment: Comments or notes about the DNS record. This field has no effect on DNS
              responses.

          priority: Required for MX, SRV and URI records; unused by other record types. Records with
              lower priorities are preferred.

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
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not dns_record_id:
            raise ValueError(f"Expected a non-empty value for `dns_record_id` but received {dns_record_id!r}")
        return cast(
            RecordEditResponse,
            self._patch(
                f"/zones/{zone_id}/dns_records/{dns_record_id}",
                body=maybe_transform(
                    {
                        "name": name,
                        "type": type,
                        "comment": comment,
                        "data": data,
                        "meta": meta,
                        "priority": priority,
                        "proxied": proxied,
                        "tags": tags,
                        "ttl": ttl,
                    },
                    record_edit_params.RecordEditParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[RecordEditResponse]
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
    ) -> RecordGetResponse:
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
            RecordGetResponse,
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
                    Any, ResultWrapper[RecordGetResponse]
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
    ) -> RecordImportResponse:
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
                record_import_params.RecordImportParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[RecordImportResponse], ResultWrapper[RecordImportResponse]),
        )

    def scan(
        self,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RecordScanResponse:
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
            cast_to=cast(Type[RecordScanResponse], ResultWrapper[RecordScanResponse]),
        )


class AsyncRecords(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRecordsWithRawResponse:
        return AsyncRecordsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRecordsWithStreamingResponse:
        return AsyncRecordsWithStreamingResponse(self)

    async def create(
        self,
        *,
        zone_id: str,
        name: str,
        type: Literal["URI"],
        comment: str | NotGiven = NOT_GIVEN,
        data: record_create_params.Data | NotGiven = NOT_GIVEN,
        meta: record_create_params.Meta | NotGiven = NOT_GIVEN,
        priority: float | NotGiven = NOT_GIVEN,
        proxied: bool | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        ttl: Union[float, Literal[1]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RecordCreateResponse:
        """
        Create a new DNS record for a zone.

        Notes:

        - A/AAAA records cannot exist on the same name as CNAME records.
        - NS records cannot exist on the same name as any other record type.
        - Domain names are always represented in Punycode, even if Unicode characters
          were used when creating the record.

        Args:
          zone_id: Identifier

          name: DNS record name (or @ for the zone apex) in Punycode.

          type: Record type.

          comment: Comments or notes about the DNS record. This field has no effect on DNS
              responses.

          priority: Required for MX, SRV and URI records; unused by other record types. Records with
              lower priorities are preferred.

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
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return cast(
            RecordCreateResponse,
            await self._post(
                f"/zones/{zone_id}/dns_records",
                body=await async_maybe_transform(
                    {
                        "name": name,
                        "type": type,
                        "comment": comment,
                        "data": data,
                        "meta": meta,
                        "priority": priority,
                        "proxied": proxied,
                        "tags": tags,
                        "ttl": ttl,
                    },
                    record_create_params.RecordCreateParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[RecordCreateResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def update(
        self,
        dns_record_id: str,
        *,
        zone_id: str,
        name: str,
        type: Literal["URI"],
        comment: str | NotGiven = NOT_GIVEN,
        data: record_update_params.Data | NotGiven = NOT_GIVEN,
        meta: record_update_params.Meta | NotGiven = NOT_GIVEN,
        priority: float | NotGiven = NOT_GIVEN,
        proxied: bool | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        ttl: Union[float, Literal[1]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RecordUpdateResponse:
        """Overwrite an existing DNS record.

        Notes:

        - A/AAAA records cannot exist on the same name as CNAME records.
        - NS records cannot exist on the same name as any other record type.
        - Domain names are always represented in Punycode, even if Unicode characters
          were used when creating the record.

        Args:
          zone_id: Identifier

          dns_record_id: Identifier

          name: DNS record name (or @ for the zone apex) in Punycode.

          type: Record type.

          comment: Comments or notes about the DNS record. This field has no effect on DNS
              responses.

          priority: Required for MX, SRV and URI records; unused by other record types. Records with
              lower priorities are preferred.

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
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not dns_record_id:
            raise ValueError(f"Expected a non-empty value for `dns_record_id` but received {dns_record_id!r}")
        return cast(
            RecordUpdateResponse,
            await self._put(
                f"/zones/{zone_id}/dns_records/{dns_record_id}",
                body=await async_maybe_transform(
                    {
                        "name": name,
                        "type": type,
                        "comment": comment,
                        "data": data,
                        "meta": meta,
                        "priority": priority,
                        "proxied": proxied,
                        "tags": tags,
                        "ttl": ttl,
                    },
                    record_update_params.RecordUpdateParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[RecordUpdateResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def list(
        self,
        *,
        zone_id: str,
        comment: record_list_params.Comment | NotGiven = NOT_GIVEN,
        content: str | NotGiven = NOT_GIVEN,
        direction: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
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
    ) -> AsyncPaginator[RecordListResponse, AsyncV4PagePaginationArray[RecordListResponse]]:
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
            page=AsyncV4PagePaginationArray[RecordListResponse],
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
            model=cast(Any, RecordListResponse),  # Union types cannot be passed in as arguments in the type system
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
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[RecordDeleteResponse]], ResultWrapper[RecordDeleteResponse]),
        )

    async def edit(
        self,
        dns_record_id: str,
        *,
        zone_id: str,
        name: str,
        type: Literal["URI"],
        comment: str | NotGiven = NOT_GIVEN,
        data: record_edit_params.Data | NotGiven = NOT_GIVEN,
        meta: record_edit_params.Meta | NotGiven = NOT_GIVEN,
        priority: float | NotGiven = NOT_GIVEN,
        proxied: bool | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        ttl: Union[float, Literal[1]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RecordEditResponse:
        """Update an existing DNS record.

        Notes:

        - A/AAAA records cannot exist on the same name as CNAME records.
        - NS records cannot exist on the same name as any other record type.
        - Domain names are always represented in Punycode, even if Unicode characters
          were used when creating the record.

        Args:
          zone_id: Identifier

          dns_record_id: Identifier

          name: DNS record name (or @ for the zone apex) in Punycode.

          type: Record type.

          comment: Comments or notes about the DNS record. This field has no effect on DNS
              responses.

          priority: Required for MX, SRV and URI records; unused by other record types. Records with
              lower priorities are preferred.

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
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not dns_record_id:
            raise ValueError(f"Expected a non-empty value for `dns_record_id` but received {dns_record_id!r}")
        return cast(
            RecordEditResponse,
            await self._patch(
                f"/zones/{zone_id}/dns_records/{dns_record_id}",
                body=await async_maybe_transform(
                    {
                        "name": name,
                        "type": type,
                        "comment": comment,
                        "data": data,
                        "meta": meta,
                        "priority": priority,
                        "proxied": proxied,
                        "tags": tags,
                        "ttl": ttl,
                    },
                    record_edit_params.RecordEditParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[RecordEditResponse]
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
    ) -> RecordGetResponse:
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
            RecordGetResponse,
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
                    Any, ResultWrapper[RecordGetResponse]
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
    ) -> RecordImportResponse:
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
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[RecordImportResponse], ResultWrapper[RecordImportResponse]),
        )

    async def scan(
        self,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RecordScanResponse:
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
            cast_to=cast(Type[RecordScanResponse], ResultWrapper[RecordScanResponse]),
        )


class RecordsWithRawResponse:
    def __init__(self, records: Records) -> None:
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


class AsyncRecordsWithRawResponse:
    def __init__(self, records: AsyncRecords) -> None:
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


class RecordsWithStreamingResponse:
    def __init__(self, records: Records) -> None:
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


class AsyncRecordsWithStreamingResponse:
    def __init__(self, records: AsyncRecords) -> None:
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
