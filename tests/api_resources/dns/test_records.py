# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.dns import (
    RecordGetResponse,
    RecordEditResponse,
    RecordListResponse,
    RecordScanResponse,
    RecordCreateResponse,
    RecordDeleteResponse,
    RecordImportResponse,
    RecordUpdateResponse,
)
from cloudflare.pagination import SyncV4PagePaginationArray, AsyncV4PagePaginationArray

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRecords:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        record = client.dns.records.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="URI",
        )
        assert_matches_type(RecordCreateResponse, record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create_with_all_params(self, client: Cloudflare) -> None:
        record = client.dns.records.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="URI",
            comment="Domain verification record",
            content={},
            data={
                "flags": {},
                "tag": "issue",
                "value": 'alpn="h3,h2" ipv4hint="127.0.0.1" ipv6hint="::1"',
                "algorithm": 2,
                "certificate": "string",
                "key_tag": 1,
                "type": 1,
                "protocol": 3,
                "public_key": "string",
                "digest": "string",
                "digest_type": 1,
                "priority": 1,
                "target": ".",
                "altitude": 0,
                "lat_degrees": 37,
                "lat_direction": "N",
                "lat_minutes": 46,
                "lat_seconds": 46,
                "long_degrees": 122,
                "long_direction": "W",
                "long_minutes": 23,
                "long_seconds": 35,
                "precision_horz": 0,
                "precision_vert": 0,
                "size": 100,
                "order": 100,
                "preference": 10,
                "regex": "string",
                "replacement": "string",
                "service": "_sip",
                "matching_type": 1,
                "selector": 0,
                "usage": 0,
                "name": "example.com",
                "port": 8806,
                "proto": "_tcp",
                "weight": 20,
                "fingerprint": "string",
                "content": "http://example.com/example.html",
            },
            meta={
                "auto_added": True,
                "source": "primary",
            },
            priority=10,
            proxied=False,
            tags=["owner:dns-team", "owner:dns-team", "owner:dns-team"],
            ttl=3600,
        )
        assert_matches_type(RecordCreateResponse, record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.dns.records.with_raw_response.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="URI",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        record = response.parse()
        assert_matches_type(RecordCreateResponse, record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.dns.records.with_streaming_response.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="URI",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            record = response.parse()
            assert_matches_type(RecordCreateResponse, record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.dns.records.with_raw_response.create(
                zone_id="",
                name="example.com",
                type="URI",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        record = client.dns.records.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="URI",
        )
        assert_matches_type(RecordUpdateResponse, record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update_with_all_params(self, client: Cloudflare) -> None:
        record = client.dns.records.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="URI",
            comment="Domain verification record",
            content={},
            data={
                "flags": {},
                "tag": "issue",
                "value": 'alpn="h3,h2" ipv4hint="127.0.0.1" ipv6hint="::1"',
                "algorithm": 2,
                "certificate": "string",
                "key_tag": 1,
                "type": 1,
                "protocol": 3,
                "public_key": "string",
                "digest": "string",
                "digest_type": 1,
                "priority": 1,
                "target": ".",
                "altitude": 0,
                "lat_degrees": 37,
                "lat_direction": "N",
                "lat_minutes": 46,
                "lat_seconds": 46,
                "long_degrees": 122,
                "long_direction": "W",
                "long_minutes": 23,
                "long_seconds": 35,
                "precision_horz": 0,
                "precision_vert": 0,
                "size": 100,
                "order": 100,
                "preference": 10,
                "regex": "string",
                "replacement": "string",
                "service": "_sip",
                "matching_type": 1,
                "selector": 0,
                "usage": 0,
                "name": "example.com",
                "port": 8806,
                "proto": "_tcp",
                "weight": 20,
                "fingerprint": "string",
                "content": "http://example.com/example.html",
            },
            meta={
                "auto_added": True,
                "source": "primary",
            },
            priority=10,
            proxied=False,
            tags=["owner:dns-team", "owner:dns-team", "owner:dns-team"],
            ttl=3600,
        )
        assert_matches_type(RecordUpdateResponse, record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.dns.records.with_raw_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="URI",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        record = response.parse()
        assert_matches_type(RecordUpdateResponse, record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.dns.records.with_streaming_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="URI",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            record = response.parse()
            assert_matches_type(RecordUpdateResponse, record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.dns.records.with_raw_response.update(
                "023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
                name="example.com",
                type="URI",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_record_id` but received ''"):
            client.dns.records.with_raw_response.update(
                "",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                name="example.com",
                type="URI",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        record = client.dns.records.list(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(SyncV4PagePaginationArray[RecordListResponse], record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list_with_all_params(self, client: Cloudflare) -> None:
        record = client.dns.records.list(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            comment={
                "present": "string",
                "absent": "string",
                "exact": "Hello, world",
                "contains": "ello, worl",
                "startswith": "Hello, w",
                "endswith": "o, world",
            },
            content="127.0.0.1",
            direction="asc",
            match="any",
            name="example.com",
            order="type",
            page=1,
            per_page=5,
            proxied=False,
            search="www.cloudflare.com",
            tag={
                "present": "important",
                "absent": "important",
                "exact": "greeting:Hello, world",
                "contains": "greeting:ello, worl",
                "startswith": "greeting:Hello, w",
                "endswith": "greeting:o, world",
            },
            tag_match="any",
            type="A",
        )
        assert_matches_type(SyncV4PagePaginationArray[RecordListResponse], record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.dns.records.with_raw_response.list(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        record = response.parse()
        assert_matches_type(SyncV4PagePaginationArray[RecordListResponse], record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.dns.records.with_streaming_response.list(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            record = response.parse()
            assert_matches_type(SyncV4PagePaginationArray[RecordListResponse], record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.dns.records.with_raw_response.list(
                zone_id="",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        record = client.dns.records.delete(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[RecordDeleteResponse], record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.dns.records.with_raw_response.delete(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        record = response.parse()
        assert_matches_type(Optional[RecordDeleteResponse], record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.dns.records.with_streaming_response.delete(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            record = response.parse()
            assert_matches_type(Optional[RecordDeleteResponse], record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.dns.records.with_raw_response.delete(
                "023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_record_id` but received ''"):
            client.dns.records.with_raw_response.delete(
                "",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_edit(self, client: Cloudflare) -> None:
        record = client.dns.records.edit(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="URI",
        )
        assert_matches_type(RecordEditResponse, record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_edit_with_all_params(self, client: Cloudflare) -> None:
        record = client.dns.records.edit(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="URI",
            comment="Domain verification record",
            content={},
            data={
                "flags": {},
                "tag": "issue",
                "value": 'alpn="h3,h2" ipv4hint="127.0.0.1" ipv6hint="::1"',
                "algorithm": 2,
                "certificate": "string",
                "key_tag": 1,
                "type": 1,
                "protocol": 3,
                "public_key": "string",
                "digest": "string",
                "digest_type": 1,
                "priority": 1,
                "target": ".",
                "altitude": 0,
                "lat_degrees": 37,
                "lat_direction": "N",
                "lat_minutes": 46,
                "lat_seconds": 46,
                "long_degrees": 122,
                "long_direction": "W",
                "long_minutes": 23,
                "long_seconds": 35,
                "precision_horz": 0,
                "precision_vert": 0,
                "size": 100,
                "order": 100,
                "preference": 10,
                "regex": "string",
                "replacement": "string",
                "service": "_sip",
                "matching_type": 1,
                "selector": 0,
                "usage": 0,
                "name": "example.com",
                "port": 8806,
                "proto": "_tcp",
                "weight": 20,
                "fingerprint": "string",
                "content": "http://example.com/example.html",
            },
            meta={
                "auto_added": True,
                "source": "primary",
            },
            priority=10,
            proxied=False,
            tags=["owner:dns-team", "owner:dns-team", "owner:dns-team"],
            ttl=3600,
        )
        assert_matches_type(RecordEditResponse, record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_edit(self, client: Cloudflare) -> None:
        response = client.dns.records.with_raw_response.edit(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="URI",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        record = response.parse()
        assert_matches_type(RecordEditResponse, record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_edit(self, client: Cloudflare) -> None:
        with client.dns.records.with_streaming_response.edit(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="URI",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            record = response.parse()
            assert_matches_type(RecordEditResponse, record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_edit(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.dns.records.with_raw_response.edit(
                "023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
                name="example.com",
                type="URI",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_record_id` but received ''"):
            client.dns.records.with_raw_response.edit(
                "",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                name="example.com",
                type="URI",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_export(self, client: Cloudflare) -> None:
        record = client.dns.records.export(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(str, record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_export(self, client: Cloudflare) -> None:
        response = client.dns.records.with_raw_response.export(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        record = response.parse()
        assert_matches_type(str, record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_export(self, client: Cloudflare) -> None:
        with client.dns.records.with_streaming_response.export(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            record = response.parse()
            assert_matches_type(str, record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_export(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.dns.records.with_raw_response.export(
                zone_id="",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        record = client.dns.records.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(RecordGetResponse, record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.dns.records.with_raw_response.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        record = response.parse()
        assert_matches_type(RecordGetResponse, record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.dns.records.with_streaming_response.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            record = response.parse()
            assert_matches_type(RecordGetResponse, record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.dns.records.with_raw_response.get(
                "023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_record_id` but received ''"):
            client.dns.records.with_raw_response.get(
                "",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_import(self, client: Cloudflare) -> None:
        record = client.dns.records.import_(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            file="www.example.com. 300 IN  A 127.0.0.1",
        )
        assert_matches_type(RecordImportResponse, record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_import_with_all_params(self, client: Cloudflare) -> None:
        record = client.dns.records.import_(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            file="www.example.com. 300 IN  A 127.0.0.1",
            proxied="true",
        )
        assert_matches_type(RecordImportResponse, record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_import(self, client: Cloudflare) -> None:
        response = client.dns.records.with_raw_response.import_(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            file="www.example.com. 300 IN  A 127.0.0.1",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        record = response.parse()
        assert_matches_type(RecordImportResponse, record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_import(self, client: Cloudflare) -> None:
        with client.dns.records.with_streaming_response.import_(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            file="www.example.com. 300 IN  A 127.0.0.1",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            record = response.parse()
            assert_matches_type(RecordImportResponse, record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_import(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.dns.records.with_raw_response.import_(
                zone_id="",
                file="www.example.com. 300 IN  A 127.0.0.1",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_scan(self, client: Cloudflare) -> None:
        record = client.dns.records.scan(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(RecordScanResponse, record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_scan(self, client: Cloudflare) -> None:
        response = client.dns.records.with_raw_response.scan(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        record = response.parse()
        assert_matches_type(RecordScanResponse, record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_scan(self, client: Cloudflare) -> None:
        with client.dns.records.with_streaming_response.scan(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            record = response.parse()
            assert_matches_type(RecordScanResponse, record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_scan(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.dns.records.with_raw_response.scan(
                zone_id="",
            )


class TestAsyncRecords:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="URI",
        )
        assert_matches_type(RecordCreateResponse, record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="URI",
            comment="Domain verification record",
            content={},
            data={
                "flags": {},
                "tag": "issue",
                "value": 'alpn="h3,h2" ipv4hint="127.0.0.1" ipv6hint="::1"',
                "algorithm": 2,
                "certificate": "string",
                "key_tag": 1,
                "type": 1,
                "protocol": 3,
                "public_key": "string",
                "digest": "string",
                "digest_type": 1,
                "priority": 1,
                "target": ".",
                "altitude": 0,
                "lat_degrees": 37,
                "lat_direction": "N",
                "lat_minutes": 46,
                "lat_seconds": 46,
                "long_degrees": 122,
                "long_direction": "W",
                "long_minutes": 23,
                "long_seconds": 35,
                "precision_horz": 0,
                "precision_vert": 0,
                "size": 100,
                "order": 100,
                "preference": 10,
                "regex": "string",
                "replacement": "string",
                "service": "_sip",
                "matching_type": 1,
                "selector": 0,
                "usage": 0,
                "name": "example.com",
                "port": 8806,
                "proto": "_tcp",
                "weight": 20,
                "fingerprint": "string",
                "content": "http://example.com/example.html",
            },
            meta={
                "auto_added": True,
                "source": "primary",
            },
            priority=10,
            proxied=False,
            tags=["owner:dns-team", "owner:dns-team", "owner:dns-team"],
            ttl=3600,
        )
        assert_matches_type(RecordCreateResponse, record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dns.records.with_raw_response.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="URI",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        record = await response.parse()
        assert_matches_type(RecordCreateResponse, record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.dns.records.with_streaming_response.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="URI",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            record = await response.parse()
            assert_matches_type(RecordCreateResponse, record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.dns.records.with_raw_response.create(
                zone_id="",
                name="example.com",
                type="URI",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="URI",
        )
        assert_matches_type(RecordUpdateResponse, record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="URI",
            comment="Domain verification record",
            content={},
            data={
                "flags": {},
                "tag": "issue",
                "value": 'alpn="h3,h2" ipv4hint="127.0.0.1" ipv6hint="::1"',
                "algorithm": 2,
                "certificate": "string",
                "key_tag": 1,
                "type": 1,
                "protocol": 3,
                "public_key": "string",
                "digest": "string",
                "digest_type": 1,
                "priority": 1,
                "target": ".",
                "altitude": 0,
                "lat_degrees": 37,
                "lat_direction": "N",
                "lat_minutes": 46,
                "lat_seconds": 46,
                "long_degrees": 122,
                "long_direction": "W",
                "long_minutes": 23,
                "long_seconds": 35,
                "precision_horz": 0,
                "precision_vert": 0,
                "size": 100,
                "order": 100,
                "preference": 10,
                "regex": "string",
                "replacement": "string",
                "service": "_sip",
                "matching_type": 1,
                "selector": 0,
                "usage": 0,
                "name": "example.com",
                "port": 8806,
                "proto": "_tcp",
                "weight": 20,
                "fingerprint": "string",
                "content": "http://example.com/example.html",
            },
            meta={
                "auto_added": True,
                "source": "primary",
            },
            priority=10,
            proxied=False,
            tags=["owner:dns-team", "owner:dns-team", "owner:dns-team"],
            ttl=3600,
        )
        assert_matches_type(RecordUpdateResponse, record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dns.records.with_raw_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="URI",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        record = await response.parse()
        assert_matches_type(RecordUpdateResponse, record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.dns.records.with_streaming_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="URI",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            record = await response.parse()
            assert_matches_type(RecordUpdateResponse, record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.dns.records.with_raw_response.update(
                "023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
                name="example.com",
                type="URI",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_record_id` but received ''"):
            await async_client.dns.records.with_raw_response.update(
                "",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                name="example.com",
                type="URI",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.list(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(AsyncV4PagePaginationArray[RecordListResponse], record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.list(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            comment={
                "present": "string",
                "absent": "string",
                "exact": "Hello, world",
                "contains": "ello, worl",
                "startswith": "Hello, w",
                "endswith": "o, world",
            },
            content="127.0.0.1",
            direction="asc",
            match="any",
            name="example.com",
            order="type",
            page=1,
            per_page=5,
            proxied=False,
            search="www.cloudflare.com",
            tag={
                "present": "important",
                "absent": "important",
                "exact": "greeting:Hello, world",
                "contains": "greeting:ello, worl",
                "startswith": "greeting:Hello, w",
                "endswith": "greeting:o, world",
            },
            tag_match="any",
            type="A",
        )
        assert_matches_type(AsyncV4PagePaginationArray[RecordListResponse], record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dns.records.with_raw_response.list(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        record = await response.parse()
        assert_matches_type(AsyncV4PagePaginationArray[RecordListResponse], record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.dns.records.with_streaming_response.list(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            record = await response.parse()
            assert_matches_type(AsyncV4PagePaginationArray[RecordListResponse], record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.dns.records.with_raw_response.list(
                zone_id="",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.delete(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[RecordDeleteResponse], record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dns.records.with_raw_response.delete(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        record = await response.parse()
        assert_matches_type(Optional[RecordDeleteResponse], record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.dns.records.with_streaming_response.delete(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            record = await response.parse()
            assert_matches_type(Optional[RecordDeleteResponse], record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.dns.records.with_raw_response.delete(
                "023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_record_id` but received ''"):
            await async_client.dns.records.with_raw_response.delete(
                "",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_edit(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.edit(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="URI",
        )
        assert_matches_type(RecordEditResponse, record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_edit_with_all_params(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.edit(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="URI",
            comment="Domain verification record",
            content={},
            data={
                "flags": {},
                "tag": "issue",
                "value": 'alpn="h3,h2" ipv4hint="127.0.0.1" ipv6hint="::1"',
                "algorithm": 2,
                "certificate": "string",
                "key_tag": 1,
                "type": 1,
                "protocol": 3,
                "public_key": "string",
                "digest": "string",
                "digest_type": 1,
                "priority": 1,
                "target": ".",
                "altitude": 0,
                "lat_degrees": 37,
                "lat_direction": "N",
                "lat_minutes": 46,
                "lat_seconds": 46,
                "long_degrees": 122,
                "long_direction": "W",
                "long_minutes": 23,
                "long_seconds": 35,
                "precision_horz": 0,
                "precision_vert": 0,
                "size": 100,
                "order": 100,
                "preference": 10,
                "regex": "string",
                "replacement": "string",
                "service": "_sip",
                "matching_type": 1,
                "selector": 0,
                "usage": 0,
                "name": "example.com",
                "port": 8806,
                "proto": "_tcp",
                "weight": 20,
                "fingerprint": "string",
                "content": "http://example.com/example.html",
            },
            meta={
                "auto_added": True,
                "source": "primary",
            },
            priority=10,
            proxied=False,
            tags=["owner:dns-team", "owner:dns-team", "owner:dns-team"],
            ttl=3600,
        )
        assert_matches_type(RecordEditResponse, record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_edit(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dns.records.with_raw_response.edit(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="URI",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        record = await response.parse()
        assert_matches_type(RecordEditResponse, record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_edit(self, async_client: AsyncCloudflare) -> None:
        async with async_client.dns.records.with_streaming_response.edit(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="URI",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            record = await response.parse()
            assert_matches_type(RecordEditResponse, record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_edit(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.dns.records.with_raw_response.edit(
                "023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
                name="example.com",
                type="URI",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_record_id` but received ''"):
            await async_client.dns.records.with_raw_response.edit(
                "",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                name="example.com",
                type="URI",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_export(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.export(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(str, record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_export(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dns.records.with_raw_response.export(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        record = await response.parse()
        assert_matches_type(str, record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_export(self, async_client: AsyncCloudflare) -> None:
        async with async_client.dns.records.with_streaming_response.export(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            record = await response.parse()
            assert_matches_type(str, record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_export(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.dns.records.with_raw_response.export(
                zone_id="",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(RecordGetResponse, record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dns.records.with_raw_response.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        record = await response.parse()
        assert_matches_type(RecordGetResponse, record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.dns.records.with_streaming_response.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            record = await response.parse()
            assert_matches_type(RecordGetResponse, record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.dns.records.with_raw_response.get(
                "023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_record_id` but received ''"):
            await async_client.dns.records.with_raw_response.get(
                "",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_import(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.import_(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            file="www.example.com. 300 IN  A 127.0.0.1",
        )
        assert_matches_type(RecordImportResponse, record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_import_with_all_params(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.import_(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            file="www.example.com. 300 IN  A 127.0.0.1",
            proxied="true",
        )
        assert_matches_type(RecordImportResponse, record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_import(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dns.records.with_raw_response.import_(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            file="www.example.com. 300 IN  A 127.0.0.1",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        record = await response.parse()
        assert_matches_type(RecordImportResponse, record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_import(self, async_client: AsyncCloudflare) -> None:
        async with async_client.dns.records.with_streaming_response.import_(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            file="www.example.com. 300 IN  A 127.0.0.1",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            record = await response.parse()
            assert_matches_type(RecordImportResponse, record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_import(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.dns.records.with_raw_response.import_(
                zone_id="",
                file="www.example.com. 300 IN  A 127.0.0.1",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_scan(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.scan(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(RecordScanResponse, record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_scan(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dns.records.with_raw_response.scan(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        record = await response.parse()
        assert_matches_type(RecordScanResponse, record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_scan(self, async_client: AsyncCloudflare) -> None:
        async with async_client.dns.records.with_streaming_response.scan(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            record = await response.parse()
            assert_matches_type(RecordScanResponse, record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_scan(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.dns.records.with_raw_response.scan(
                zone_id="",
            )
