# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.dns import (
    RecordResponse,
    RecordScanResponse,
    RecordBatchResponse,
    RecordDeleteResponse,
    RecordImportResponse,
)
from cloudflare.pagination import SyncV4PagePaginationArray, AsyncV4PagePaginationArray

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRecords:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_create_overload_1(self, client: Cloudflare) -> None:
        record = client.dns.records.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_create_with_all_params_overload_1(self, client: Cloudflare) -> None:
        record = client.dns.records.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            comment="Domain verification record",
            content="198.51.100.4",
            name="example.com",
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
            type="A",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_create_overload_1(self, client: Cloudflare) -> None:
        response = client.dns.records.with_raw_response.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        record = response.parse()
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_create_overload_1(self, client: Cloudflare) -> None:
        with client.dns.records.with_streaming_response.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            record = response.parse()
            assert_matches_type(Optional[RecordResponse], record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_create_overload_1(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.dns.records.with_raw_response.create(
                zone_id="",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_create_overload_2(self, client: Cloudflare) -> None:
        record = client.dns.records.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_create_with_all_params_overload_2(self, client: Cloudflare) -> None:
        record = client.dns.records.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            comment="Domain verification record",
            content="2400:cb00:2049::1",
            name="example.com",
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
            type="AAAA",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_create_overload_2(self, client: Cloudflare) -> None:
        response = client.dns.records.with_raw_response.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        record = response.parse()
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_create_overload_2(self, client: Cloudflare) -> None:
        with client.dns.records.with_streaming_response.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            record = response.parse()
            assert_matches_type(Optional[RecordResponse], record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_create_overload_2(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.dns.records.with_raw_response.create(
                zone_id="",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_create_overload_3(self, client: Cloudflare) -> None:
        record = client.dns.records.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_create_with_all_params_overload_3(self, client: Cloudflare) -> None:
        record = client.dns.records.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            comment="Domain verification record",
            data={
                "flags": 1,
                "tag": "issue",
                "value": "value",
            },
            name="example.com",
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
            type="CAA",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_create_overload_3(self, client: Cloudflare) -> None:
        response = client.dns.records.with_raw_response.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        record = response.parse()
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_create_overload_3(self, client: Cloudflare) -> None:
        with client.dns.records.with_streaming_response.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            record = response.parse()
            assert_matches_type(Optional[RecordResponse], record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_create_overload_3(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.dns.records.with_raw_response.create(
                zone_id="",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_create_overload_4(self, client: Cloudflare) -> None:
        record = client.dns.records.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_create_with_all_params_overload_4(self, client: Cloudflare) -> None:
        record = client.dns.records.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            comment="Domain verification record",
            data={
                "algorithm": 8,
                "certificate": "certificate",
                "key_tag": 1,
                "type": 9,
            },
            name="example.com",
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
            type="CERT",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_create_overload_4(self, client: Cloudflare) -> None:
        response = client.dns.records.with_raw_response.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        record = response.parse()
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_create_overload_4(self, client: Cloudflare) -> None:
        with client.dns.records.with_streaming_response.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            record = response.parse()
            assert_matches_type(Optional[RecordResponse], record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_create_overload_4(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.dns.records.with_raw_response.create(
                zone_id="",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_create_overload_5(self, client: Cloudflare) -> None:
        record = client.dns.records.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_create_with_all_params_overload_5(self, client: Cloudflare) -> None:
        record = client.dns.records.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            comment="Domain verification record",
            content="content",
            name="example.com",
            proxied=True,
            settings={
                "flatten_cname": True,
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
            type="CNAME",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_create_overload_5(self, client: Cloudflare) -> None:
        response = client.dns.records.with_raw_response.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        record = response.parse()
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_create_overload_5(self, client: Cloudflare) -> None:
        with client.dns.records.with_streaming_response.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            record = response.parse()
            assert_matches_type(Optional[RecordResponse], record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_create_overload_5(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.dns.records.with_raw_response.create(
                zone_id="",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_create_overload_6(self, client: Cloudflare) -> None:
        record = client.dns.records.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_create_with_all_params_overload_6(self, client: Cloudflare) -> None:
        record = client.dns.records.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            comment="Domain verification record",
            data={
                "algorithm": 5,
                "flags": 1,
                "protocol": 3,
                "public_key": "public_key",
            },
            name="example.com",
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
            type="DNSKEY",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_create_overload_6(self, client: Cloudflare) -> None:
        response = client.dns.records.with_raw_response.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        record = response.parse()
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_create_overload_6(self, client: Cloudflare) -> None:
        with client.dns.records.with_streaming_response.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            record = response.parse()
            assert_matches_type(Optional[RecordResponse], record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_create_overload_6(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.dns.records.with_raw_response.create(
                zone_id="",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_create_overload_7(self, client: Cloudflare) -> None:
        record = client.dns.records.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_create_with_all_params_overload_7(self, client: Cloudflare) -> None:
        record = client.dns.records.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            comment="Domain verification record",
            data={
                "algorithm": 3,
                "digest": "digest",
                "digest_type": 1,
                "key_tag": 1,
            },
            name="example.com",
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
            type="DS",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_create_overload_7(self, client: Cloudflare) -> None:
        response = client.dns.records.with_raw_response.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        record = response.parse()
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_create_overload_7(self, client: Cloudflare) -> None:
        with client.dns.records.with_streaming_response.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            record = response.parse()
            assert_matches_type(Optional[RecordResponse], record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_create_overload_7(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.dns.records.with_raw_response.create(
                zone_id="",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_create_overload_8(self, client: Cloudflare) -> None:
        record = client.dns.records.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_create_with_all_params_overload_8(self, client: Cloudflare) -> None:
        record = client.dns.records.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            comment="Domain verification record",
            data={
                "priority": 1,
                "target": ".",
                "value": 'alpn="h3,h2" ipv4hint="127.0.0.1" ipv6hint="::1"',
            },
            name="example.com",
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
            type="HTTPS",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_create_overload_8(self, client: Cloudflare) -> None:
        response = client.dns.records.with_raw_response.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        record = response.parse()
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_create_overload_8(self, client: Cloudflare) -> None:
        with client.dns.records.with_streaming_response.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            record = response.parse()
            assert_matches_type(Optional[RecordResponse], record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_create_overload_8(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.dns.records.with_raw_response.create(
                zone_id="",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_create_overload_9(self, client: Cloudflare) -> None:
        record = client.dns.records.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_create_with_all_params_overload_9(self, client: Cloudflare) -> None:
        record = client.dns.records.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            comment="Domain verification record",
            data={
                "altitude": 0,
                "lat_degrees": 37,
                "lat_direction": "N",
                "lat_minutes": 46,
                "lat_seconds": 46,
                "long_degrees": 122,
                "long_direction": "E",
                "long_minutes": 23,
                "long_seconds": 35,
                "precision_horz": 0,
                "precision_vert": 0,
                "size": 100,
            },
            name="example.com",
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
            type="LOC",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_create_overload_9(self, client: Cloudflare) -> None:
        response = client.dns.records.with_raw_response.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        record = response.parse()
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_create_overload_9(self, client: Cloudflare) -> None:
        with client.dns.records.with_streaming_response.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            record = response.parse()
            assert_matches_type(Optional[RecordResponse], record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_create_overload_9(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.dns.records.with_raw_response.create(
                zone_id="",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_create_overload_10(self, client: Cloudflare) -> None:
        record = client.dns.records.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_create_with_all_params_overload_10(self, client: Cloudflare) -> None:
        record = client.dns.records.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            comment="Domain verification record",
            content="mx.example.com",
            name="example.com",
            priority=10,
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
            type="MX",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_create_overload_10(self, client: Cloudflare) -> None:
        response = client.dns.records.with_raw_response.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        record = response.parse()
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_create_overload_10(self, client: Cloudflare) -> None:
        with client.dns.records.with_streaming_response.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            record = response.parse()
            assert_matches_type(Optional[RecordResponse], record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_create_overload_10(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.dns.records.with_raw_response.create(
                zone_id="",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_create_overload_11(self, client: Cloudflare) -> None:
        record = client.dns.records.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_create_with_all_params_overload_11(self, client: Cloudflare) -> None:
        record = client.dns.records.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            comment="Domain verification record",
            data={
                "flags": "flags",
                "order": 100,
                "preference": 10,
                "regex": "regex",
                "replacement": "replacement",
                "service": "service",
            },
            name="example.com",
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
            type="NAPTR",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_create_overload_11(self, client: Cloudflare) -> None:
        response = client.dns.records.with_raw_response.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        record = response.parse()
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_create_overload_11(self, client: Cloudflare) -> None:
        with client.dns.records.with_streaming_response.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            record = response.parse()
            assert_matches_type(Optional[RecordResponse], record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_create_overload_11(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.dns.records.with_raw_response.create(
                zone_id="",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_create_overload_12(self, client: Cloudflare) -> None:
        record = client.dns.records.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_create_with_all_params_overload_12(self, client: Cloudflare) -> None:
        record = client.dns.records.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            comment="Domain verification record",
            content="ns1.example.com",
            name="example.com",
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
            type="NS",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_create_overload_12(self, client: Cloudflare) -> None:
        response = client.dns.records.with_raw_response.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        record = response.parse()
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_create_overload_12(self, client: Cloudflare) -> None:
        with client.dns.records.with_streaming_response.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            record = response.parse()
            assert_matches_type(Optional[RecordResponse], record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_create_overload_12(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.dns.records.with_raw_response.create(
                zone_id="",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_create_overload_13(self, client: Cloudflare) -> None:
        record = client.dns.records.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_create_with_all_params_overload_13(self, client: Cloudflare) -> None:
        record = client.dns.records.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            comment="Domain verification record",
            content="content",
            name="example.com",
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
            type="OPENPGPKEY",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_create_overload_13(self, client: Cloudflare) -> None:
        response = client.dns.records.with_raw_response.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        record = response.parse()
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_create_overload_13(self, client: Cloudflare) -> None:
        with client.dns.records.with_streaming_response.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            record = response.parse()
            assert_matches_type(Optional[RecordResponse], record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_create_overload_13(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.dns.records.with_raw_response.create(
                zone_id="",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_create_overload_14(self, client: Cloudflare) -> None:
        record = client.dns.records.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_create_with_all_params_overload_14(self, client: Cloudflare) -> None:
        record = client.dns.records.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            comment="Domain verification record",
            content="example.com",
            name="example.com",
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
            type="PTR",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_create_overload_14(self, client: Cloudflare) -> None:
        response = client.dns.records.with_raw_response.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        record = response.parse()
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_create_overload_14(self, client: Cloudflare) -> None:
        with client.dns.records.with_streaming_response.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            record = response.parse()
            assert_matches_type(Optional[RecordResponse], record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_create_overload_14(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.dns.records.with_raw_response.create(
                zone_id="",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_create_overload_15(self, client: Cloudflare) -> None:
        record = client.dns.records.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_create_with_all_params_overload_15(self, client: Cloudflare) -> None:
        record = client.dns.records.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            comment="Domain verification record",
            data={
                "certificate": "certificate",
                "matching_type": 0,
                "selector": 0,
                "usage": 3,
            },
            name="example.com",
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
            type="SMIMEA",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_create_overload_15(self, client: Cloudflare) -> None:
        response = client.dns.records.with_raw_response.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        record = response.parse()
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_create_overload_15(self, client: Cloudflare) -> None:
        with client.dns.records.with_streaming_response.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            record = response.parse()
            assert_matches_type(Optional[RecordResponse], record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_create_overload_15(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.dns.records.with_raw_response.create(
                zone_id="",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_create_overload_16(self, client: Cloudflare) -> None:
        record = client.dns.records.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_create_with_all_params_overload_16(self, client: Cloudflare) -> None:
        record = client.dns.records.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            comment="Domain verification record",
            data={
                "port": 8806,
                "priority": 10,
                "target": "example.com",
                "weight": 5,
            },
            name="example.com",
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
            type="SRV",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_create_overload_16(self, client: Cloudflare) -> None:
        response = client.dns.records.with_raw_response.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        record = response.parse()
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_create_overload_16(self, client: Cloudflare) -> None:
        with client.dns.records.with_streaming_response.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            record = response.parse()
            assert_matches_type(Optional[RecordResponse], record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_create_overload_16(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.dns.records.with_raw_response.create(
                zone_id="",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_create_overload_17(self, client: Cloudflare) -> None:
        record = client.dns.records.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_create_with_all_params_overload_17(self, client: Cloudflare) -> None:
        record = client.dns.records.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            comment="Domain verification record",
            data={
                "algorithm": 2,
                "fingerprint": "fingerprint",
                "type": 1,
            },
            name="example.com",
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
            type="SSHFP",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_create_overload_17(self, client: Cloudflare) -> None:
        response = client.dns.records.with_raw_response.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        record = response.parse()
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_create_overload_17(self, client: Cloudflare) -> None:
        with client.dns.records.with_streaming_response.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            record = response.parse()
            assert_matches_type(Optional[RecordResponse], record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_create_overload_17(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.dns.records.with_raw_response.create(
                zone_id="",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_create_overload_18(self, client: Cloudflare) -> None:
        record = client.dns.records.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_create_with_all_params_overload_18(self, client: Cloudflare) -> None:
        record = client.dns.records.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            comment="Domain verification record",
            data={
                "priority": 1,
                "target": ".",
                "value": 'alpn="h3,h2" ipv4hint="127.0.0.1" ipv6hint="::1"',
            },
            name="example.com",
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
            type="SVCB",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_create_overload_18(self, client: Cloudflare) -> None:
        response = client.dns.records.with_raw_response.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        record = response.parse()
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_create_overload_18(self, client: Cloudflare) -> None:
        with client.dns.records.with_streaming_response.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            record = response.parse()
            assert_matches_type(Optional[RecordResponse], record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_create_overload_18(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.dns.records.with_raw_response.create(
                zone_id="",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_create_overload_19(self, client: Cloudflare) -> None:
        record = client.dns.records.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_create_with_all_params_overload_19(self, client: Cloudflare) -> None:
        record = client.dns.records.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            comment="Domain verification record",
            data={
                "certificate": "certificate",
                "matching_type": 1,
                "selector": 0,
                "usage": 0,
            },
            name="example.com",
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
            type="TLSA",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_create_overload_19(self, client: Cloudflare) -> None:
        response = client.dns.records.with_raw_response.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        record = response.parse()
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_create_overload_19(self, client: Cloudflare) -> None:
        with client.dns.records.with_streaming_response.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            record = response.parse()
            assert_matches_type(Optional[RecordResponse], record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_create_overload_19(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.dns.records.with_raw_response.create(
                zone_id="",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_create_overload_20(self, client: Cloudflare) -> None:
        record = client.dns.records.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_create_with_all_params_overload_20(self, client: Cloudflare) -> None:
        record = client.dns.records.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            comment="Domain verification record",
            content='"v=spf1 include:example.com -all"',
            name="example.com",
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
            type="TXT",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_create_overload_20(self, client: Cloudflare) -> None:
        response = client.dns.records.with_raw_response.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        record = response.parse()
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_create_overload_20(self, client: Cloudflare) -> None:
        with client.dns.records.with_streaming_response.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            record = response.parse()
            assert_matches_type(Optional[RecordResponse], record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_create_overload_20(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.dns.records.with_raw_response.create(
                zone_id="",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_create_overload_21(self, client: Cloudflare) -> None:
        record = client.dns.records.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_create_with_all_params_overload_21(self, client: Cloudflare) -> None:
        record = client.dns.records.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            comment="Domain verification record",
            data={
                "target": "http://example.com/example.html",
                "weight": 20,
            },
            name="example.com",
            priority=10,
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
            type="URI",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_create_overload_21(self, client: Cloudflare) -> None:
        response = client.dns.records.with_raw_response.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        record = response.parse()
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_create_overload_21(self, client: Cloudflare) -> None:
        with client.dns.records.with_streaming_response.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            record = response.parse()
            assert_matches_type(Optional[RecordResponse], record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_create_overload_21(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.dns.records.with_raw_response.create(
                zone_id="",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_update_overload_1(self, client: Cloudflare) -> None:
        record = client.dns.records.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_update_with_all_params_overload_1(self, client: Cloudflare) -> None:
        record = client.dns.records.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            comment="Domain verification record",
            content="198.51.100.4",
            name="example.com",
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
            type="A",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_update_overload_1(self, client: Cloudflare) -> None:
        response = client.dns.records.with_raw_response.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        record = response.parse()
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_update_overload_1(self, client: Cloudflare) -> None:
        with client.dns.records.with_streaming_response.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            record = response.parse()
            assert_matches_type(Optional[RecordResponse], record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_update_overload_1(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.dns.records.with_raw_response.update(
                dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_record_id` but received ''"):
            client.dns.records.with_raw_response.update(
                dns_record_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_update_overload_2(self, client: Cloudflare) -> None:
        record = client.dns.records.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_update_with_all_params_overload_2(self, client: Cloudflare) -> None:
        record = client.dns.records.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            comment="Domain verification record",
            content="2400:cb00:2049::1",
            name="example.com",
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
            type="AAAA",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_update_overload_2(self, client: Cloudflare) -> None:
        response = client.dns.records.with_raw_response.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        record = response.parse()
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_update_overload_2(self, client: Cloudflare) -> None:
        with client.dns.records.with_streaming_response.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            record = response.parse()
            assert_matches_type(Optional[RecordResponse], record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_update_overload_2(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.dns.records.with_raw_response.update(
                dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_record_id` but received ''"):
            client.dns.records.with_raw_response.update(
                dns_record_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_update_overload_3(self, client: Cloudflare) -> None:
        record = client.dns.records.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_update_with_all_params_overload_3(self, client: Cloudflare) -> None:
        record = client.dns.records.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            comment="Domain verification record",
            data={
                "flags": 1,
                "tag": "issue",
                "value": "value",
            },
            name="example.com",
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
            type="CAA",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_update_overload_3(self, client: Cloudflare) -> None:
        response = client.dns.records.with_raw_response.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        record = response.parse()
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_update_overload_3(self, client: Cloudflare) -> None:
        with client.dns.records.with_streaming_response.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            record = response.parse()
            assert_matches_type(Optional[RecordResponse], record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_update_overload_3(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.dns.records.with_raw_response.update(
                dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_record_id` but received ''"):
            client.dns.records.with_raw_response.update(
                dns_record_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_update_overload_4(self, client: Cloudflare) -> None:
        record = client.dns.records.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_update_with_all_params_overload_4(self, client: Cloudflare) -> None:
        record = client.dns.records.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            comment="Domain verification record",
            data={
                "algorithm": 8,
                "certificate": "certificate",
                "key_tag": 1,
                "type": 9,
            },
            name="example.com",
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
            type="CERT",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_update_overload_4(self, client: Cloudflare) -> None:
        response = client.dns.records.with_raw_response.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        record = response.parse()
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_update_overload_4(self, client: Cloudflare) -> None:
        with client.dns.records.with_streaming_response.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            record = response.parse()
            assert_matches_type(Optional[RecordResponse], record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_update_overload_4(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.dns.records.with_raw_response.update(
                dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_record_id` but received ''"):
            client.dns.records.with_raw_response.update(
                dns_record_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_update_overload_5(self, client: Cloudflare) -> None:
        record = client.dns.records.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_update_with_all_params_overload_5(self, client: Cloudflare) -> None:
        record = client.dns.records.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            comment="Domain verification record",
            content="content",
            name="example.com",
            proxied=True,
            settings={
                "flatten_cname": True,
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
            type="CNAME",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_update_overload_5(self, client: Cloudflare) -> None:
        response = client.dns.records.with_raw_response.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        record = response.parse()
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_update_overload_5(self, client: Cloudflare) -> None:
        with client.dns.records.with_streaming_response.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            record = response.parse()
            assert_matches_type(Optional[RecordResponse], record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_update_overload_5(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.dns.records.with_raw_response.update(
                dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_record_id` but received ''"):
            client.dns.records.with_raw_response.update(
                dns_record_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_update_overload_6(self, client: Cloudflare) -> None:
        record = client.dns.records.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_update_with_all_params_overload_6(self, client: Cloudflare) -> None:
        record = client.dns.records.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            comment="Domain verification record",
            data={
                "algorithm": 5,
                "flags": 1,
                "protocol": 3,
                "public_key": "public_key",
            },
            name="example.com",
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
            type="DNSKEY",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_update_overload_6(self, client: Cloudflare) -> None:
        response = client.dns.records.with_raw_response.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        record = response.parse()
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_update_overload_6(self, client: Cloudflare) -> None:
        with client.dns.records.with_streaming_response.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            record = response.parse()
            assert_matches_type(Optional[RecordResponse], record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_update_overload_6(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.dns.records.with_raw_response.update(
                dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_record_id` but received ''"):
            client.dns.records.with_raw_response.update(
                dns_record_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_update_overload_7(self, client: Cloudflare) -> None:
        record = client.dns.records.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_update_with_all_params_overload_7(self, client: Cloudflare) -> None:
        record = client.dns.records.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            comment="Domain verification record",
            data={
                "algorithm": 3,
                "digest": "digest",
                "digest_type": 1,
                "key_tag": 1,
            },
            name="example.com",
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
            type="DS",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_update_overload_7(self, client: Cloudflare) -> None:
        response = client.dns.records.with_raw_response.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        record = response.parse()
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_update_overload_7(self, client: Cloudflare) -> None:
        with client.dns.records.with_streaming_response.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            record = response.parse()
            assert_matches_type(Optional[RecordResponse], record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_update_overload_7(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.dns.records.with_raw_response.update(
                dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_record_id` but received ''"):
            client.dns.records.with_raw_response.update(
                dns_record_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_update_overload_8(self, client: Cloudflare) -> None:
        record = client.dns.records.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_update_with_all_params_overload_8(self, client: Cloudflare) -> None:
        record = client.dns.records.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            comment="Domain verification record",
            data={
                "priority": 1,
                "target": ".",
                "value": 'alpn="h3,h2" ipv4hint="127.0.0.1" ipv6hint="::1"',
            },
            name="example.com",
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
            type="HTTPS",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_update_overload_8(self, client: Cloudflare) -> None:
        response = client.dns.records.with_raw_response.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        record = response.parse()
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_update_overload_8(self, client: Cloudflare) -> None:
        with client.dns.records.with_streaming_response.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            record = response.parse()
            assert_matches_type(Optional[RecordResponse], record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_update_overload_8(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.dns.records.with_raw_response.update(
                dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_record_id` but received ''"):
            client.dns.records.with_raw_response.update(
                dns_record_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_update_overload_9(self, client: Cloudflare) -> None:
        record = client.dns.records.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_update_with_all_params_overload_9(self, client: Cloudflare) -> None:
        record = client.dns.records.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            comment="Domain verification record",
            data={
                "altitude": 0,
                "lat_degrees": 37,
                "lat_direction": "N",
                "lat_minutes": 46,
                "lat_seconds": 46,
                "long_degrees": 122,
                "long_direction": "E",
                "long_minutes": 23,
                "long_seconds": 35,
                "precision_horz": 0,
                "precision_vert": 0,
                "size": 100,
            },
            name="example.com",
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
            type="LOC",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_update_overload_9(self, client: Cloudflare) -> None:
        response = client.dns.records.with_raw_response.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        record = response.parse()
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_update_overload_9(self, client: Cloudflare) -> None:
        with client.dns.records.with_streaming_response.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            record = response.parse()
            assert_matches_type(Optional[RecordResponse], record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_update_overload_9(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.dns.records.with_raw_response.update(
                dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_record_id` but received ''"):
            client.dns.records.with_raw_response.update(
                dns_record_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_update_overload_10(self, client: Cloudflare) -> None:
        record = client.dns.records.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_update_with_all_params_overload_10(self, client: Cloudflare) -> None:
        record = client.dns.records.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            comment="Domain verification record",
            content="mx.example.com",
            name="example.com",
            priority=10,
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
            type="MX",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_update_overload_10(self, client: Cloudflare) -> None:
        response = client.dns.records.with_raw_response.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        record = response.parse()
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_update_overload_10(self, client: Cloudflare) -> None:
        with client.dns.records.with_streaming_response.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            record = response.parse()
            assert_matches_type(Optional[RecordResponse], record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_update_overload_10(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.dns.records.with_raw_response.update(
                dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_record_id` but received ''"):
            client.dns.records.with_raw_response.update(
                dns_record_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_update_overload_11(self, client: Cloudflare) -> None:
        record = client.dns.records.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_update_with_all_params_overload_11(self, client: Cloudflare) -> None:
        record = client.dns.records.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            comment="Domain verification record",
            data={
                "flags": "flags",
                "order": 100,
                "preference": 10,
                "regex": "regex",
                "replacement": "replacement",
                "service": "service",
            },
            name="example.com",
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
            type="NAPTR",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_update_overload_11(self, client: Cloudflare) -> None:
        response = client.dns.records.with_raw_response.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        record = response.parse()
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_update_overload_11(self, client: Cloudflare) -> None:
        with client.dns.records.with_streaming_response.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            record = response.parse()
            assert_matches_type(Optional[RecordResponse], record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_update_overload_11(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.dns.records.with_raw_response.update(
                dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_record_id` but received ''"):
            client.dns.records.with_raw_response.update(
                dns_record_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_update_overload_12(self, client: Cloudflare) -> None:
        record = client.dns.records.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_update_with_all_params_overload_12(self, client: Cloudflare) -> None:
        record = client.dns.records.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            comment="Domain verification record",
            content="ns1.example.com",
            name="example.com",
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
            type="NS",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_update_overload_12(self, client: Cloudflare) -> None:
        response = client.dns.records.with_raw_response.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        record = response.parse()
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_update_overload_12(self, client: Cloudflare) -> None:
        with client.dns.records.with_streaming_response.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            record = response.parse()
            assert_matches_type(Optional[RecordResponse], record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_update_overload_12(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.dns.records.with_raw_response.update(
                dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_record_id` but received ''"):
            client.dns.records.with_raw_response.update(
                dns_record_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_update_overload_13(self, client: Cloudflare) -> None:
        record = client.dns.records.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_update_with_all_params_overload_13(self, client: Cloudflare) -> None:
        record = client.dns.records.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            comment="Domain verification record",
            content="content",
            name="example.com",
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
            type="OPENPGPKEY",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_update_overload_13(self, client: Cloudflare) -> None:
        response = client.dns.records.with_raw_response.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        record = response.parse()
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_update_overload_13(self, client: Cloudflare) -> None:
        with client.dns.records.with_streaming_response.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            record = response.parse()
            assert_matches_type(Optional[RecordResponse], record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_update_overload_13(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.dns.records.with_raw_response.update(
                dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_record_id` but received ''"):
            client.dns.records.with_raw_response.update(
                dns_record_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_update_overload_14(self, client: Cloudflare) -> None:
        record = client.dns.records.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_update_with_all_params_overload_14(self, client: Cloudflare) -> None:
        record = client.dns.records.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            comment="Domain verification record",
            content="example.com",
            name="example.com",
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
            type="PTR",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_update_overload_14(self, client: Cloudflare) -> None:
        response = client.dns.records.with_raw_response.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        record = response.parse()
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_update_overload_14(self, client: Cloudflare) -> None:
        with client.dns.records.with_streaming_response.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            record = response.parse()
            assert_matches_type(Optional[RecordResponse], record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_update_overload_14(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.dns.records.with_raw_response.update(
                dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_record_id` but received ''"):
            client.dns.records.with_raw_response.update(
                dns_record_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_update_overload_15(self, client: Cloudflare) -> None:
        record = client.dns.records.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_update_with_all_params_overload_15(self, client: Cloudflare) -> None:
        record = client.dns.records.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            comment="Domain verification record",
            data={
                "certificate": "certificate",
                "matching_type": 0,
                "selector": 0,
                "usage": 3,
            },
            name="example.com",
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
            type="SMIMEA",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_update_overload_15(self, client: Cloudflare) -> None:
        response = client.dns.records.with_raw_response.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        record = response.parse()
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_update_overload_15(self, client: Cloudflare) -> None:
        with client.dns.records.with_streaming_response.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            record = response.parse()
            assert_matches_type(Optional[RecordResponse], record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_update_overload_15(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.dns.records.with_raw_response.update(
                dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_record_id` but received ''"):
            client.dns.records.with_raw_response.update(
                dns_record_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_update_overload_16(self, client: Cloudflare) -> None:
        record = client.dns.records.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_update_with_all_params_overload_16(self, client: Cloudflare) -> None:
        record = client.dns.records.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            comment="Domain verification record",
            data={
                "port": 8806,
                "priority": 10,
                "target": "example.com",
                "weight": 5,
            },
            name="example.com",
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
            type="SRV",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_update_overload_16(self, client: Cloudflare) -> None:
        response = client.dns.records.with_raw_response.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        record = response.parse()
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_update_overload_16(self, client: Cloudflare) -> None:
        with client.dns.records.with_streaming_response.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            record = response.parse()
            assert_matches_type(Optional[RecordResponse], record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_update_overload_16(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.dns.records.with_raw_response.update(
                dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_record_id` but received ''"):
            client.dns.records.with_raw_response.update(
                dns_record_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_update_overload_17(self, client: Cloudflare) -> None:
        record = client.dns.records.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_update_with_all_params_overload_17(self, client: Cloudflare) -> None:
        record = client.dns.records.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            comment="Domain verification record",
            data={
                "algorithm": 2,
                "fingerprint": "fingerprint",
                "type": 1,
            },
            name="example.com",
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
            type="SSHFP",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_update_overload_17(self, client: Cloudflare) -> None:
        response = client.dns.records.with_raw_response.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        record = response.parse()
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_update_overload_17(self, client: Cloudflare) -> None:
        with client.dns.records.with_streaming_response.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            record = response.parse()
            assert_matches_type(Optional[RecordResponse], record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_update_overload_17(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.dns.records.with_raw_response.update(
                dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_record_id` but received ''"):
            client.dns.records.with_raw_response.update(
                dns_record_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_update_overload_18(self, client: Cloudflare) -> None:
        record = client.dns.records.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_update_with_all_params_overload_18(self, client: Cloudflare) -> None:
        record = client.dns.records.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            comment="Domain verification record",
            data={
                "priority": 1,
                "target": ".",
                "value": 'alpn="h3,h2" ipv4hint="127.0.0.1" ipv6hint="::1"',
            },
            name="example.com",
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
            type="SVCB",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_update_overload_18(self, client: Cloudflare) -> None:
        response = client.dns.records.with_raw_response.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        record = response.parse()
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_update_overload_18(self, client: Cloudflare) -> None:
        with client.dns.records.with_streaming_response.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            record = response.parse()
            assert_matches_type(Optional[RecordResponse], record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_update_overload_18(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.dns.records.with_raw_response.update(
                dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_record_id` but received ''"):
            client.dns.records.with_raw_response.update(
                dns_record_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_update_overload_19(self, client: Cloudflare) -> None:
        record = client.dns.records.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_update_with_all_params_overload_19(self, client: Cloudflare) -> None:
        record = client.dns.records.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            comment="Domain verification record",
            data={
                "certificate": "certificate",
                "matching_type": 1,
                "selector": 0,
                "usage": 0,
            },
            name="example.com",
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
            type="TLSA",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_update_overload_19(self, client: Cloudflare) -> None:
        response = client.dns.records.with_raw_response.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        record = response.parse()
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_update_overload_19(self, client: Cloudflare) -> None:
        with client.dns.records.with_streaming_response.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            record = response.parse()
            assert_matches_type(Optional[RecordResponse], record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_update_overload_19(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.dns.records.with_raw_response.update(
                dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_record_id` but received ''"):
            client.dns.records.with_raw_response.update(
                dns_record_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_update_overload_20(self, client: Cloudflare) -> None:
        record = client.dns.records.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_update_with_all_params_overload_20(self, client: Cloudflare) -> None:
        record = client.dns.records.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            comment="Domain verification record",
            content='"v=spf1 include:example.com -all"',
            name="example.com",
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
            type="TXT",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_update_overload_20(self, client: Cloudflare) -> None:
        response = client.dns.records.with_raw_response.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        record = response.parse()
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_update_overload_20(self, client: Cloudflare) -> None:
        with client.dns.records.with_streaming_response.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            record = response.parse()
            assert_matches_type(Optional[RecordResponse], record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_update_overload_20(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.dns.records.with_raw_response.update(
                dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_record_id` but received ''"):
            client.dns.records.with_raw_response.update(
                dns_record_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_update_overload_21(self, client: Cloudflare) -> None:
        record = client.dns.records.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_update_with_all_params_overload_21(self, client: Cloudflare) -> None:
        record = client.dns.records.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            comment="Domain verification record",
            data={
                "target": "http://example.com/example.html",
                "weight": 20,
            },
            name="example.com",
            priority=10,
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
            type="URI",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_update_overload_21(self, client: Cloudflare) -> None:
        response = client.dns.records.with_raw_response.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        record = response.parse()
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_update_overload_21(self, client: Cloudflare) -> None:
        with client.dns.records.with_streaming_response.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            record = response.parse()
            assert_matches_type(Optional[RecordResponse], record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_update_overload_21(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.dns.records.with_raw_response.update(
                dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_record_id` but received ''"):
            client.dns.records.with_raw_response.update(
                dns_record_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip(reason="mock server returns invalid data")
    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        record = client.dns.records.list(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(SyncV4PagePaginationArray[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="mock server returns invalid data")
    @parametrize
    def test_method_list_with_all_params(self, client: Cloudflare) -> None:
        record = client.dns.records.list(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            comment={
                "absent": "absent",
                "contains": "ello, worl",
                "endswith": "o, world",
                "exact": "Hello, world",
                "present": "present",
                "startswith": "Hello, w",
            },
            content={
                "contains": "7.0.0.",
                "endswith": ".0.1",
                "exact": "127.0.0.1",
                "startswith": "127.0.",
            },
            direction="asc",
            match="any",
            name={
                "contains": "w.example.",
                "endswith": ".example.com",
                "exact": "www.example.com",
                "startswith": "www.example",
            },
            order="type",
            page=1,
            per_page=5,
            proxied=True,
            search="www.cloudflare.com",
            tag={
                "absent": "important",
                "contains": "greeting:ello, worl",
                "endswith": "greeting:o, world",
                "exact": "greeting:Hello, world",
                "present": "important",
                "startswith": "greeting:Hello, w",
            },
            tag_match="any",
            type="A",
        )
        assert_matches_type(SyncV4PagePaginationArray[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="mock server returns invalid data")
    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.dns.records.with_raw_response.list(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        record = response.parse()
        assert_matches_type(SyncV4PagePaginationArray[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="mock server returns invalid data")
    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.dns.records.with_streaming_response.list(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            record = response.parse()
            assert_matches_type(SyncV4PagePaginationArray[RecordResponse], record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="mock server returns invalid data")
    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.dns.records.with_raw_response.list(
                zone_id="",
            )

    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        record = client.dns.records.delete(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[RecordDeleteResponse], record, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.dns.records.with_raw_response.delete(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        record = response.parse()
        assert_matches_type(Optional[RecordDeleteResponse], record, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.dns.records.with_streaming_response.delete(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            record = response.parse()
            assert_matches_type(Optional[RecordDeleteResponse], record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.dns.records.with_raw_response.delete(
                dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_record_id` but received ''"):
            client.dns.records.with_raw_response.delete(
                dns_record_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip(reason="TODO: investigate auth errors on test suite")
    @parametrize
    def test_method_batch(self, client: Cloudflare) -> None:
        record = client.dns.records.batch(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[RecordBatchResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate auth errors on test suite")
    @parametrize
    def test_method_batch_with_all_params(self, client: Cloudflare) -> None:
        record = client.dns.records.batch(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            deletes=[{"id": "023e105f4ecef8ad9ca31a8372d0c353"}],
            patches=[
                {
                    "comment": "Domain verification record",
                    "content": "198.51.100.4",
                    "name": "example.com",
                    "proxied": True,
                    "settings": {
                        "ipv4_only": True,
                        "ipv6_only": True,
                    },
                    "tags": ["owner:dns-team"],
                    "ttl": 3600,
                    "type": "A",
                    "id": "023e105f4ecef8ad9ca31a8372d0c353",
                }
            ],
            posts=[
                {
                    "comment": "Domain verification record",
                    "content": "198.51.100.4",
                    "name": "example.com",
                    "proxied": True,
                    "settings": {
                        "ipv4_only": True,
                        "ipv6_only": True,
                    },
                    "tags": ["owner:dns-team"],
                    "ttl": 3600,
                    "type": "A",
                }
            ],
            puts=[
                {
                    "comment": "Domain verification record",
                    "content": "198.51.100.4",
                    "name": "example.com",
                    "proxied": True,
                    "settings": {
                        "ipv4_only": True,
                        "ipv6_only": True,
                    },
                    "tags": ["owner:dns-team"],
                    "ttl": 3600,
                    "type": "A",
                    "id": "023e105f4ecef8ad9ca31a8372d0c353",
                }
            ],
        )
        assert_matches_type(Optional[RecordBatchResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate auth errors on test suite")
    @parametrize
    def test_raw_response_batch(self, client: Cloudflare) -> None:
        response = client.dns.records.with_raw_response.batch(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        record = response.parse()
        assert_matches_type(Optional[RecordBatchResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate auth errors on test suite")
    @parametrize
    def test_streaming_response_batch(self, client: Cloudflare) -> None:
        with client.dns.records.with_streaming_response.batch(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            record = response.parse()
            assert_matches_type(Optional[RecordBatchResponse], record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate auth errors on test suite")
    @parametrize
    def test_path_params_batch(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.dns.records.with_raw_response.batch(
                zone_id="",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_edit_overload_1(self, client: Cloudflare) -> None:
        record = client.dns.records.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_edit_with_all_params_overload_1(self, client: Cloudflare) -> None:
        record = client.dns.records.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            comment="Domain verification record",
            content="198.51.100.4",
            name="example.com",
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
            type="A",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_edit_overload_1(self, client: Cloudflare) -> None:
        response = client.dns.records.with_raw_response.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        record = response.parse()
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_edit_overload_1(self, client: Cloudflare) -> None:
        with client.dns.records.with_streaming_response.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            record = response.parse()
            assert_matches_type(Optional[RecordResponse], record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_edit_overload_1(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.dns.records.with_raw_response.edit(
                dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_record_id` but received ''"):
            client.dns.records.with_raw_response.edit(
                dns_record_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_edit_overload_2(self, client: Cloudflare) -> None:
        record = client.dns.records.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_edit_with_all_params_overload_2(self, client: Cloudflare) -> None:
        record = client.dns.records.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            comment="Domain verification record",
            content="2400:cb00:2049::1",
            name="example.com",
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
            type="AAAA",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_edit_overload_2(self, client: Cloudflare) -> None:
        response = client.dns.records.with_raw_response.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        record = response.parse()
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_edit_overload_2(self, client: Cloudflare) -> None:
        with client.dns.records.with_streaming_response.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            record = response.parse()
            assert_matches_type(Optional[RecordResponse], record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_edit_overload_2(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.dns.records.with_raw_response.edit(
                dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_record_id` but received ''"):
            client.dns.records.with_raw_response.edit(
                dns_record_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_edit_overload_3(self, client: Cloudflare) -> None:
        record = client.dns.records.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_edit_with_all_params_overload_3(self, client: Cloudflare) -> None:
        record = client.dns.records.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            comment="Domain verification record",
            data={
                "flags": 1,
                "tag": "issue",
                "value": "value",
            },
            name="example.com",
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
            type="CAA",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_edit_overload_3(self, client: Cloudflare) -> None:
        response = client.dns.records.with_raw_response.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        record = response.parse()
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_edit_overload_3(self, client: Cloudflare) -> None:
        with client.dns.records.with_streaming_response.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            record = response.parse()
            assert_matches_type(Optional[RecordResponse], record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_edit_overload_3(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.dns.records.with_raw_response.edit(
                dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_record_id` but received ''"):
            client.dns.records.with_raw_response.edit(
                dns_record_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_edit_overload_4(self, client: Cloudflare) -> None:
        record = client.dns.records.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_edit_with_all_params_overload_4(self, client: Cloudflare) -> None:
        record = client.dns.records.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            comment="Domain verification record",
            data={
                "algorithm": 8,
                "certificate": "certificate",
                "key_tag": 1,
                "type": 9,
            },
            name="example.com",
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
            type="CERT",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_edit_overload_4(self, client: Cloudflare) -> None:
        response = client.dns.records.with_raw_response.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        record = response.parse()
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_edit_overload_4(self, client: Cloudflare) -> None:
        with client.dns.records.with_streaming_response.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            record = response.parse()
            assert_matches_type(Optional[RecordResponse], record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_edit_overload_4(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.dns.records.with_raw_response.edit(
                dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_record_id` but received ''"):
            client.dns.records.with_raw_response.edit(
                dns_record_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_edit_overload_5(self, client: Cloudflare) -> None:
        record = client.dns.records.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_edit_with_all_params_overload_5(self, client: Cloudflare) -> None:
        record = client.dns.records.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            comment="Domain verification record",
            content="content",
            name="example.com",
            proxied=True,
            settings={
                "flatten_cname": True,
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
            type="CNAME",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_edit_overload_5(self, client: Cloudflare) -> None:
        response = client.dns.records.with_raw_response.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        record = response.parse()
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_edit_overload_5(self, client: Cloudflare) -> None:
        with client.dns.records.with_streaming_response.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            record = response.parse()
            assert_matches_type(Optional[RecordResponse], record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_edit_overload_5(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.dns.records.with_raw_response.edit(
                dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_record_id` but received ''"):
            client.dns.records.with_raw_response.edit(
                dns_record_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_edit_overload_6(self, client: Cloudflare) -> None:
        record = client.dns.records.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_edit_with_all_params_overload_6(self, client: Cloudflare) -> None:
        record = client.dns.records.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            comment="Domain verification record",
            data={
                "algorithm": 5,
                "flags": 1,
                "protocol": 3,
                "public_key": "public_key",
            },
            name="example.com",
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
            type="DNSKEY",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_edit_overload_6(self, client: Cloudflare) -> None:
        response = client.dns.records.with_raw_response.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        record = response.parse()
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_edit_overload_6(self, client: Cloudflare) -> None:
        with client.dns.records.with_streaming_response.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            record = response.parse()
            assert_matches_type(Optional[RecordResponse], record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_edit_overload_6(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.dns.records.with_raw_response.edit(
                dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_record_id` but received ''"):
            client.dns.records.with_raw_response.edit(
                dns_record_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_edit_overload_7(self, client: Cloudflare) -> None:
        record = client.dns.records.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_edit_with_all_params_overload_7(self, client: Cloudflare) -> None:
        record = client.dns.records.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            comment="Domain verification record",
            data={
                "algorithm": 3,
                "digest": "digest",
                "digest_type": 1,
                "key_tag": 1,
            },
            name="example.com",
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
            type="DS",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_edit_overload_7(self, client: Cloudflare) -> None:
        response = client.dns.records.with_raw_response.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        record = response.parse()
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_edit_overload_7(self, client: Cloudflare) -> None:
        with client.dns.records.with_streaming_response.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            record = response.parse()
            assert_matches_type(Optional[RecordResponse], record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_edit_overload_7(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.dns.records.with_raw_response.edit(
                dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_record_id` but received ''"):
            client.dns.records.with_raw_response.edit(
                dns_record_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_edit_overload_8(self, client: Cloudflare) -> None:
        record = client.dns.records.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_edit_with_all_params_overload_8(self, client: Cloudflare) -> None:
        record = client.dns.records.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            comment="Domain verification record",
            data={
                "priority": 1,
                "target": ".",
                "value": 'alpn="h3,h2" ipv4hint="127.0.0.1" ipv6hint="::1"',
            },
            name="example.com",
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
            type="HTTPS",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_edit_overload_8(self, client: Cloudflare) -> None:
        response = client.dns.records.with_raw_response.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        record = response.parse()
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_edit_overload_8(self, client: Cloudflare) -> None:
        with client.dns.records.with_streaming_response.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            record = response.parse()
            assert_matches_type(Optional[RecordResponse], record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_edit_overload_8(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.dns.records.with_raw_response.edit(
                dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_record_id` but received ''"):
            client.dns.records.with_raw_response.edit(
                dns_record_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_edit_overload_9(self, client: Cloudflare) -> None:
        record = client.dns.records.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_edit_with_all_params_overload_9(self, client: Cloudflare) -> None:
        record = client.dns.records.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            comment="Domain verification record",
            data={
                "altitude": 0,
                "lat_degrees": 37,
                "lat_direction": "N",
                "lat_minutes": 46,
                "lat_seconds": 46,
                "long_degrees": 122,
                "long_direction": "E",
                "long_minutes": 23,
                "long_seconds": 35,
                "precision_horz": 0,
                "precision_vert": 0,
                "size": 100,
            },
            name="example.com",
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
            type="LOC",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_edit_overload_9(self, client: Cloudflare) -> None:
        response = client.dns.records.with_raw_response.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        record = response.parse()
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_edit_overload_9(self, client: Cloudflare) -> None:
        with client.dns.records.with_streaming_response.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            record = response.parse()
            assert_matches_type(Optional[RecordResponse], record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_edit_overload_9(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.dns.records.with_raw_response.edit(
                dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_record_id` but received ''"):
            client.dns.records.with_raw_response.edit(
                dns_record_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_edit_overload_10(self, client: Cloudflare) -> None:
        record = client.dns.records.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_edit_with_all_params_overload_10(self, client: Cloudflare) -> None:
        record = client.dns.records.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            comment="Domain verification record",
            content="mx.example.com",
            name="example.com",
            priority=10,
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
            type="MX",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_edit_overload_10(self, client: Cloudflare) -> None:
        response = client.dns.records.with_raw_response.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        record = response.parse()
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_edit_overload_10(self, client: Cloudflare) -> None:
        with client.dns.records.with_streaming_response.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            record = response.parse()
            assert_matches_type(Optional[RecordResponse], record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_edit_overload_10(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.dns.records.with_raw_response.edit(
                dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_record_id` but received ''"):
            client.dns.records.with_raw_response.edit(
                dns_record_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_edit_overload_11(self, client: Cloudflare) -> None:
        record = client.dns.records.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_edit_with_all_params_overload_11(self, client: Cloudflare) -> None:
        record = client.dns.records.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            comment="Domain verification record",
            data={
                "flags": "flags",
                "order": 100,
                "preference": 10,
                "regex": "regex",
                "replacement": "replacement",
                "service": "service",
            },
            name="example.com",
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
            type="NAPTR",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_edit_overload_11(self, client: Cloudflare) -> None:
        response = client.dns.records.with_raw_response.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        record = response.parse()
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_edit_overload_11(self, client: Cloudflare) -> None:
        with client.dns.records.with_streaming_response.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            record = response.parse()
            assert_matches_type(Optional[RecordResponse], record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_edit_overload_11(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.dns.records.with_raw_response.edit(
                dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_record_id` but received ''"):
            client.dns.records.with_raw_response.edit(
                dns_record_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_edit_overload_12(self, client: Cloudflare) -> None:
        record = client.dns.records.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_edit_with_all_params_overload_12(self, client: Cloudflare) -> None:
        record = client.dns.records.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            comment="Domain verification record",
            content="ns1.example.com",
            name="example.com",
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
            type="NS",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_edit_overload_12(self, client: Cloudflare) -> None:
        response = client.dns.records.with_raw_response.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        record = response.parse()
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_edit_overload_12(self, client: Cloudflare) -> None:
        with client.dns.records.with_streaming_response.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            record = response.parse()
            assert_matches_type(Optional[RecordResponse], record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_edit_overload_12(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.dns.records.with_raw_response.edit(
                dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_record_id` but received ''"):
            client.dns.records.with_raw_response.edit(
                dns_record_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_edit_overload_13(self, client: Cloudflare) -> None:
        record = client.dns.records.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_edit_with_all_params_overload_13(self, client: Cloudflare) -> None:
        record = client.dns.records.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            comment="Domain verification record",
            content="content",
            name="example.com",
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
            type="OPENPGPKEY",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_edit_overload_13(self, client: Cloudflare) -> None:
        response = client.dns.records.with_raw_response.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        record = response.parse()
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_edit_overload_13(self, client: Cloudflare) -> None:
        with client.dns.records.with_streaming_response.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            record = response.parse()
            assert_matches_type(Optional[RecordResponse], record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_edit_overload_13(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.dns.records.with_raw_response.edit(
                dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_record_id` but received ''"):
            client.dns.records.with_raw_response.edit(
                dns_record_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_edit_overload_14(self, client: Cloudflare) -> None:
        record = client.dns.records.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_edit_with_all_params_overload_14(self, client: Cloudflare) -> None:
        record = client.dns.records.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            comment="Domain verification record",
            content="example.com",
            name="example.com",
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
            type="PTR",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_edit_overload_14(self, client: Cloudflare) -> None:
        response = client.dns.records.with_raw_response.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        record = response.parse()
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_edit_overload_14(self, client: Cloudflare) -> None:
        with client.dns.records.with_streaming_response.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            record = response.parse()
            assert_matches_type(Optional[RecordResponse], record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_edit_overload_14(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.dns.records.with_raw_response.edit(
                dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_record_id` but received ''"):
            client.dns.records.with_raw_response.edit(
                dns_record_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_edit_overload_15(self, client: Cloudflare) -> None:
        record = client.dns.records.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_edit_with_all_params_overload_15(self, client: Cloudflare) -> None:
        record = client.dns.records.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            comment="Domain verification record",
            data={
                "certificate": "certificate",
                "matching_type": 0,
                "selector": 0,
                "usage": 3,
            },
            name="example.com",
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
            type="SMIMEA",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_edit_overload_15(self, client: Cloudflare) -> None:
        response = client.dns.records.with_raw_response.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        record = response.parse()
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_edit_overload_15(self, client: Cloudflare) -> None:
        with client.dns.records.with_streaming_response.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            record = response.parse()
            assert_matches_type(Optional[RecordResponse], record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_edit_overload_15(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.dns.records.with_raw_response.edit(
                dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_record_id` but received ''"):
            client.dns.records.with_raw_response.edit(
                dns_record_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_edit_overload_16(self, client: Cloudflare) -> None:
        record = client.dns.records.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_edit_with_all_params_overload_16(self, client: Cloudflare) -> None:
        record = client.dns.records.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            comment="Domain verification record",
            data={
                "port": 8806,
                "priority": 10,
                "target": "example.com",
                "weight": 5,
            },
            name="example.com",
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
            type="SRV",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_edit_overload_16(self, client: Cloudflare) -> None:
        response = client.dns.records.with_raw_response.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        record = response.parse()
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_edit_overload_16(self, client: Cloudflare) -> None:
        with client.dns.records.with_streaming_response.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            record = response.parse()
            assert_matches_type(Optional[RecordResponse], record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_edit_overload_16(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.dns.records.with_raw_response.edit(
                dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_record_id` but received ''"):
            client.dns.records.with_raw_response.edit(
                dns_record_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_edit_overload_17(self, client: Cloudflare) -> None:
        record = client.dns.records.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_edit_with_all_params_overload_17(self, client: Cloudflare) -> None:
        record = client.dns.records.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            comment="Domain verification record",
            data={
                "algorithm": 2,
                "fingerprint": "fingerprint",
                "type": 1,
            },
            name="example.com",
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
            type="SSHFP",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_edit_overload_17(self, client: Cloudflare) -> None:
        response = client.dns.records.with_raw_response.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        record = response.parse()
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_edit_overload_17(self, client: Cloudflare) -> None:
        with client.dns.records.with_streaming_response.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            record = response.parse()
            assert_matches_type(Optional[RecordResponse], record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_edit_overload_17(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.dns.records.with_raw_response.edit(
                dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_record_id` but received ''"):
            client.dns.records.with_raw_response.edit(
                dns_record_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_edit_overload_18(self, client: Cloudflare) -> None:
        record = client.dns.records.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_edit_with_all_params_overload_18(self, client: Cloudflare) -> None:
        record = client.dns.records.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            comment="Domain verification record",
            data={
                "priority": 1,
                "target": ".",
                "value": 'alpn="h3,h2" ipv4hint="127.0.0.1" ipv6hint="::1"',
            },
            name="example.com",
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
            type="SVCB",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_edit_overload_18(self, client: Cloudflare) -> None:
        response = client.dns.records.with_raw_response.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        record = response.parse()
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_edit_overload_18(self, client: Cloudflare) -> None:
        with client.dns.records.with_streaming_response.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            record = response.parse()
            assert_matches_type(Optional[RecordResponse], record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_edit_overload_18(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.dns.records.with_raw_response.edit(
                dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_record_id` but received ''"):
            client.dns.records.with_raw_response.edit(
                dns_record_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_edit_overload_19(self, client: Cloudflare) -> None:
        record = client.dns.records.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_edit_with_all_params_overload_19(self, client: Cloudflare) -> None:
        record = client.dns.records.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            comment="Domain verification record",
            data={
                "certificate": "certificate",
                "matching_type": 1,
                "selector": 0,
                "usage": 0,
            },
            name="example.com",
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
            type="TLSA",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_edit_overload_19(self, client: Cloudflare) -> None:
        response = client.dns.records.with_raw_response.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        record = response.parse()
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_edit_overload_19(self, client: Cloudflare) -> None:
        with client.dns.records.with_streaming_response.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            record = response.parse()
            assert_matches_type(Optional[RecordResponse], record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_edit_overload_19(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.dns.records.with_raw_response.edit(
                dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_record_id` but received ''"):
            client.dns.records.with_raw_response.edit(
                dns_record_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_edit_overload_20(self, client: Cloudflare) -> None:
        record = client.dns.records.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_edit_with_all_params_overload_20(self, client: Cloudflare) -> None:
        record = client.dns.records.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            comment="Domain verification record",
            content='"v=spf1 include:example.com -all"',
            name="example.com",
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
            type="TXT",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_edit_overload_20(self, client: Cloudflare) -> None:
        response = client.dns.records.with_raw_response.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        record = response.parse()
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_edit_overload_20(self, client: Cloudflare) -> None:
        with client.dns.records.with_streaming_response.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            record = response.parse()
            assert_matches_type(Optional[RecordResponse], record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_edit_overload_20(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.dns.records.with_raw_response.edit(
                dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_record_id` but received ''"):
            client.dns.records.with_raw_response.edit(
                dns_record_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_edit_overload_21(self, client: Cloudflare) -> None:
        record = client.dns.records.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_edit_with_all_params_overload_21(self, client: Cloudflare) -> None:
        record = client.dns.records.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            comment="Domain verification record",
            data={
                "target": "http://example.com/example.html",
                "weight": 20,
            },
            name="example.com",
            priority=10,
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
            type="URI",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_edit_overload_21(self, client: Cloudflare) -> None:
        response = client.dns.records.with_raw_response.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        record = response.parse()
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_edit_overload_21(self, client: Cloudflare) -> None:
        with client.dns.records.with_streaming_response.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            record = response.parse()
            assert_matches_type(Optional[RecordResponse], record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_edit_overload_21(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.dns.records.with_raw_response.edit(
                dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_record_id` but received ''"):
            client.dns.records.with_raw_response.edit(
                dns_record_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    def test_method_export(self, client: Cloudflare) -> None:
        record = client.dns.records.export(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(str, record, path=["response"])

    @parametrize
    def test_raw_response_export(self, client: Cloudflare) -> None:
        response = client.dns.records.with_raw_response.export(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        record = response.parse()
        assert_matches_type(str, record, path=["response"])

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

    @parametrize
    def test_path_params_export(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.dns.records.with_raw_response.export(
                zone_id="",
            )

    @pytest.mark.skip(reason="mock server returns invalid data")
    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        record = client.dns.records.get(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="mock server returns invalid data")
    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.dns.records.with_raw_response.get(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        record = response.parse()
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="mock server returns invalid data")
    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.dns.records.with_streaming_response.get(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            record = response.parse()
            assert_matches_type(Optional[RecordResponse], record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="mock server returns invalid data")
    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.dns.records.with_raw_response.get(
                dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_record_id` but received ''"):
            client.dns.records.with_raw_response.get(
                dns_record_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_import(self, client: Cloudflare) -> None:
        record = client.dns.records.import_(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            file="www.example.com. 300 IN  A 127.0.0.1",
        )
        assert_matches_type(Optional[RecordImportResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_import_with_all_params(self, client: Cloudflare) -> None:
        record = client.dns.records.import_(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            file="www.example.com. 300 IN  A 127.0.0.1",
            proxied="true",
        )
        assert_matches_type(Optional[RecordImportResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_import(self, client: Cloudflare) -> None:
        response = client.dns.records.with_raw_response.import_(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            file="www.example.com. 300 IN  A 127.0.0.1",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        record = response.parse()
        assert_matches_type(Optional[RecordImportResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_import(self, client: Cloudflare) -> None:
        with client.dns.records.with_streaming_response.import_(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            file="www.example.com. 300 IN  A 127.0.0.1",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            record = response.parse()
            assert_matches_type(Optional[RecordImportResponse], record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_import(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.dns.records.with_raw_response.import_(
                zone_id="",
                file="www.example.com. 300 IN  A 127.0.0.1",
            )

    @parametrize
    def test_method_scan(self, client: Cloudflare) -> None:
        record = client.dns.records.scan(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        )
        assert_matches_type(Optional[RecordScanResponse], record, path=["response"])

    @parametrize
    def test_raw_response_scan(self, client: Cloudflare) -> None:
        response = client.dns.records.with_raw_response.scan(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        record = response.parse()
        assert_matches_type(Optional[RecordScanResponse], record, path=["response"])

    @parametrize
    def test_streaming_response_scan(self, client: Cloudflare) -> None:
        with client.dns.records.with_streaming_response.scan(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            record = response.parse()
            assert_matches_type(Optional[RecordScanResponse], record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_scan(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.dns.records.with_raw_response.scan(
                zone_id="",
                body={},
            )


class TestAsyncRecords:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_create_overload_1(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_create_with_all_params_overload_1(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            comment="Domain verification record",
            content="198.51.100.4",
            name="example.com",
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
            type="A",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_create_overload_1(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dns.records.with_raw_response.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        record = await response.parse()
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_create_overload_1(self, async_client: AsyncCloudflare) -> None:
        async with async_client.dns.records.with_streaming_response.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            record = await response.parse()
            assert_matches_type(Optional[RecordResponse], record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_create_overload_1(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.dns.records.with_raw_response.create(
                zone_id="",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_create_overload_2(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_create_with_all_params_overload_2(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            comment="Domain verification record",
            content="2400:cb00:2049::1",
            name="example.com",
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
            type="AAAA",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_create_overload_2(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dns.records.with_raw_response.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        record = await response.parse()
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_create_overload_2(self, async_client: AsyncCloudflare) -> None:
        async with async_client.dns.records.with_streaming_response.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            record = await response.parse()
            assert_matches_type(Optional[RecordResponse], record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_create_overload_2(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.dns.records.with_raw_response.create(
                zone_id="",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_create_overload_3(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_create_with_all_params_overload_3(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            comment="Domain verification record",
            data={
                "flags": 1,
                "tag": "issue",
                "value": "value",
            },
            name="example.com",
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
            type="CAA",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_create_overload_3(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dns.records.with_raw_response.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        record = await response.parse()
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_create_overload_3(self, async_client: AsyncCloudflare) -> None:
        async with async_client.dns.records.with_streaming_response.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            record = await response.parse()
            assert_matches_type(Optional[RecordResponse], record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_create_overload_3(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.dns.records.with_raw_response.create(
                zone_id="",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_create_overload_4(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_create_with_all_params_overload_4(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            comment="Domain verification record",
            data={
                "algorithm": 8,
                "certificate": "certificate",
                "key_tag": 1,
                "type": 9,
            },
            name="example.com",
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
            type="CERT",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_create_overload_4(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dns.records.with_raw_response.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        record = await response.parse()
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_create_overload_4(self, async_client: AsyncCloudflare) -> None:
        async with async_client.dns.records.with_streaming_response.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            record = await response.parse()
            assert_matches_type(Optional[RecordResponse], record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_create_overload_4(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.dns.records.with_raw_response.create(
                zone_id="",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_create_overload_5(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_create_with_all_params_overload_5(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            comment="Domain verification record",
            content="content",
            name="example.com",
            proxied=True,
            settings={
                "flatten_cname": True,
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
            type="CNAME",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_create_overload_5(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dns.records.with_raw_response.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        record = await response.parse()
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_create_overload_5(self, async_client: AsyncCloudflare) -> None:
        async with async_client.dns.records.with_streaming_response.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            record = await response.parse()
            assert_matches_type(Optional[RecordResponse], record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_create_overload_5(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.dns.records.with_raw_response.create(
                zone_id="",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_create_overload_6(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_create_with_all_params_overload_6(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            comment="Domain verification record",
            data={
                "algorithm": 5,
                "flags": 1,
                "protocol": 3,
                "public_key": "public_key",
            },
            name="example.com",
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
            type="DNSKEY",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_create_overload_6(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dns.records.with_raw_response.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        record = await response.parse()
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_create_overload_6(self, async_client: AsyncCloudflare) -> None:
        async with async_client.dns.records.with_streaming_response.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            record = await response.parse()
            assert_matches_type(Optional[RecordResponse], record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_create_overload_6(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.dns.records.with_raw_response.create(
                zone_id="",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_create_overload_7(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_create_with_all_params_overload_7(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            comment="Domain verification record",
            data={
                "algorithm": 3,
                "digest": "digest",
                "digest_type": 1,
                "key_tag": 1,
            },
            name="example.com",
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
            type="DS",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_create_overload_7(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dns.records.with_raw_response.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        record = await response.parse()
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_create_overload_7(self, async_client: AsyncCloudflare) -> None:
        async with async_client.dns.records.with_streaming_response.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            record = await response.parse()
            assert_matches_type(Optional[RecordResponse], record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_create_overload_7(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.dns.records.with_raw_response.create(
                zone_id="",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_create_overload_8(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_create_with_all_params_overload_8(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            comment="Domain verification record",
            data={
                "priority": 1,
                "target": ".",
                "value": 'alpn="h3,h2" ipv4hint="127.0.0.1" ipv6hint="::1"',
            },
            name="example.com",
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
            type="HTTPS",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_create_overload_8(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dns.records.with_raw_response.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        record = await response.parse()
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_create_overload_8(self, async_client: AsyncCloudflare) -> None:
        async with async_client.dns.records.with_streaming_response.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            record = await response.parse()
            assert_matches_type(Optional[RecordResponse], record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_create_overload_8(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.dns.records.with_raw_response.create(
                zone_id="",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_create_overload_9(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_create_with_all_params_overload_9(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            comment="Domain verification record",
            data={
                "altitude": 0,
                "lat_degrees": 37,
                "lat_direction": "N",
                "lat_minutes": 46,
                "lat_seconds": 46,
                "long_degrees": 122,
                "long_direction": "E",
                "long_minutes": 23,
                "long_seconds": 35,
                "precision_horz": 0,
                "precision_vert": 0,
                "size": 100,
            },
            name="example.com",
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
            type="LOC",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_create_overload_9(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dns.records.with_raw_response.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        record = await response.parse()
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_create_overload_9(self, async_client: AsyncCloudflare) -> None:
        async with async_client.dns.records.with_streaming_response.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            record = await response.parse()
            assert_matches_type(Optional[RecordResponse], record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_create_overload_9(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.dns.records.with_raw_response.create(
                zone_id="",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_create_overload_10(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_create_with_all_params_overload_10(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            comment="Domain verification record",
            content="mx.example.com",
            name="example.com",
            priority=10,
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
            type="MX",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_create_overload_10(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dns.records.with_raw_response.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        record = await response.parse()
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_create_overload_10(self, async_client: AsyncCloudflare) -> None:
        async with async_client.dns.records.with_streaming_response.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            record = await response.parse()
            assert_matches_type(Optional[RecordResponse], record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_create_overload_10(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.dns.records.with_raw_response.create(
                zone_id="",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_create_overload_11(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_create_with_all_params_overload_11(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            comment="Domain verification record",
            data={
                "flags": "flags",
                "order": 100,
                "preference": 10,
                "regex": "regex",
                "replacement": "replacement",
                "service": "service",
            },
            name="example.com",
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
            type="NAPTR",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_create_overload_11(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dns.records.with_raw_response.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        record = await response.parse()
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_create_overload_11(self, async_client: AsyncCloudflare) -> None:
        async with async_client.dns.records.with_streaming_response.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            record = await response.parse()
            assert_matches_type(Optional[RecordResponse], record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_create_overload_11(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.dns.records.with_raw_response.create(
                zone_id="",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_create_overload_12(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_create_with_all_params_overload_12(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            comment="Domain verification record",
            content="ns1.example.com",
            name="example.com",
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
            type="NS",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_create_overload_12(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dns.records.with_raw_response.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        record = await response.parse()
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_create_overload_12(self, async_client: AsyncCloudflare) -> None:
        async with async_client.dns.records.with_streaming_response.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            record = await response.parse()
            assert_matches_type(Optional[RecordResponse], record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_create_overload_12(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.dns.records.with_raw_response.create(
                zone_id="",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_create_overload_13(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_create_with_all_params_overload_13(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            comment="Domain verification record",
            content="content",
            name="example.com",
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
            type="OPENPGPKEY",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_create_overload_13(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dns.records.with_raw_response.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        record = await response.parse()
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_create_overload_13(self, async_client: AsyncCloudflare) -> None:
        async with async_client.dns.records.with_streaming_response.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            record = await response.parse()
            assert_matches_type(Optional[RecordResponse], record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_create_overload_13(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.dns.records.with_raw_response.create(
                zone_id="",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_create_overload_14(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_create_with_all_params_overload_14(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            comment="Domain verification record",
            content="example.com",
            name="example.com",
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
            type="PTR",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_create_overload_14(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dns.records.with_raw_response.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        record = await response.parse()
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_create_overload_14(self, async_client: AsyncCloudflare) -> None:
        async with async_client.dns.records.with_streaming_response.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            record = await response.parse()
            assert_matches_type(Optional[RecordResponse], record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_create_overload_14(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.dns.records.with_raw_response.create(
                zone_id="",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_create_overload_15(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_create_with_all_params_overload_15(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            comment="Domain verification record",
            data={
                "certificate": "certificate",
                "matching_type": 0,
                "selector": 0,
                "usage": 3,
            },
            name="example.com",
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
            type="SMIMEA",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_create_overload_15(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dns.records.with_raw_response.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        record = await response.parse()
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_create_overload_15(self, async_client: AsyncCloudflare) -> None:
        async with async_client.dns.records.with_streaming_response.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            record = await response.parse()
            assert_matches_type(Optional[RecordResponse], record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_create_overload_15(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.dns.records.with_raw_response.create(
                zone_id="",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_create_overload_16(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_create_with_all_params_overload_16(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            comment="Domain verification record",
            data={
                "port": 8806,
                "priority": 10,
                "target": "example.com",
                "weight": 5,
            },
            name="example.com",
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
            type="SRV",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_create_overload_16(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dns.records.with_raw_response.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        record = await response.parse()
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_create_overload_16(self, async_client: AsyncCloudflare) -> None:
        async with async_client.dns.records.with_streaming_response.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            record = await response.parse()
            assert_matches_type(Optional[RecordResponse], record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_create_overload_16(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.dns.records.with_raw_response.create(
                zone_id="",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_create_overload_17(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_create_with_all_params_overload_17(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            comment="Domain verification record",
            data={
                "algorithm": 2,
                "fingerprint": "fingerprint",
                "type": 1,
            },
            name="example.com",
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
            type="SSHFP",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_create_overload_17(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dns.records.with_raw_response.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        record = await response.parse()
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_create_overload_17(self, async_client: AsyncCloudflare) -> None:
        async with async_client.dns.records.with_streaming_response.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            record = await response.parse()
            assert_matches_type(Optional[RecordResponse], record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_create_overload_17(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.dns.records.with_raw_response.create(
                zone_id="",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_create_overload_18(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_create_with_all_params_overload_18(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            comment="Domain verification record",
            data={
                "priority": 1,
                "target": ".",
                "value": 'alpn="h3,h2" ipv4hint="127.0.0.1" ipv6hint="::1"',
            },
            name="example.com",
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
            type="SVCB",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_create_overload_18(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dns.records.with_raw_response.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        record = await response.parse()
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_create_overload_18(self, async_client: AsyncCloudflare) -> None:
        async with async_client.dns.records.with_streaming_response.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            record = await response.parse()
            assert_matches_type(Optional[RecordResponse], record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_create_overload_18(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.dns.records.with_raw_response.create(
                zone_id="",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_create_overload_19(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_create_with_all_params_overload_19(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            comment="Domain verification record",
            data={
                "certificate": "certificate",
                "matching_type": 1,
                "selector": 0,
                "usage": 0,
            },
            name="example.com",
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
            type="TLSA",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_create_overload_19(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dns.records.with_raw_response.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        record = await response.parse()
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_create_overload_19(self, async_client: AsyncCloudflare) -> None:
        async with async_client.dns.records.with_streaming_response.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            record = await response.parse()
            assert_matches_type(Optional[RecordResponse], record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_create_overload_19(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.dns.records.with_raw_response.create(
                zone_id="",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_create_overload_20(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_create_with_all_params_overload_20(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            comment="Domain verification record",
            content='"v=spf1 include:example.com -all"',
            name="example.com",
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
            type="TXT",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_create_overload_20(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dns.records.with_raw_response.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        record = await response.parse()
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_create_overload_20(self, async_client: AsyncCloudflare) -> None:
        async with async_client.dns.records.with_streaming_response.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            record = await response.parse()
            assert_matches_type(Optional[RecordResponse], record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_create_overload_20(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.dns.records.with_raw_response.create(
                zone_id="",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_create_overload_21(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_create_with_all_params_overload_21(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            comment="Domain verification record",
            data={
                "target": "http://example.com/example.html",
                "weight": 20,
            },
            name="example.com",
            priority=10,
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
            type="URI",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_create_overload_21(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dns.records.with_raw_response.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        record = await response.parse()
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_create_overload_21(self, async_client: AsyncCloudflare) -> None:
        async with async_client.dns.records.with_streaming_response.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            record = await response.parse()
            assert_matches_type(Optional[RecordResponse], record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_create_overload_21(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.dns.records.with_raw_response.create(
                zone_id="",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_update_overload_1(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_update_with_all_params_overload_1(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            comment="Domain verification record",
            content="198.51.100.4",
            name="example.com",
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
            type="A",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_update_overload_1(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dns.records.with_raw_response.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        record = await response.parse()
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_update_overload_1(self, async_client: AsyncCloudflare) -> None:
        async with async_client.dns.records.with_streaming_response.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            record = await response.parse()
            assert_matches_type(Optional[RecordResponse], record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_update_overload_1(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.dns.records.with_raw_response.update(
                dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_record_id` but received ''"):
            await async_client.dns.records.with_raw_response.update(
                dns_record_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_update_overload_2(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_update_with_all_params_overload_2(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            comment="Domain verification record",
            content="2400:cb00:2049::1",
            name="example.com",
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
            type="AAAA",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_update_overload_2(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dns.records.with_raw_response.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        record = await response.parse()
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_update_overload_2(self, async_client: AsyncCloudflare) -> None:
        async with async_client.dns.records.with_streaming_response.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            record = await response.parse()
            assert_matches_type(Optional[RecordResponse], record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_update_overload_2(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.dns.records.with_raw_response.update(
                dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_record_id` but received ''"):
            await async_client.dns.records.with_raw_response.update(
                dns_record_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_update_overload_3(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_update_with_all_params_overload_3(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            comment="Domain verification record",
            data={
                "flags": 1,
                "tag": "issue",
                "value": "value",
            },
            name="example.com",
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
            type="CAA",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_update_overload_3(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dns.records.with_raw_response.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        record = await response.parse()
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_update_overload_3(self, async_client: AsyncCloudflare) -> None:
        async with async_client.dns.records.with_streaming_response.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            record = await response.parse()
            assert_matches_type(Optional[RecordResponse], record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_update_overload_3(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.dns.records.with_raw_response.update(
                dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_record_id` but received ''"):
            await async_client.dns.records.with_raw_response.update(
                dns_record_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_update_overload_4(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_update_with_all_params_overload_4(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            comment="Domain verification record",
            data={
                "algorithm": 8,
                "certificate": "certificate",
                "key_tag": 1,
                "type": 9,
            },
            name="example.com",
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
            type="CERT",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_update_overload_4(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dns.records.with_raw_response.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        record = await response.parse()
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_update_overload_4(self, async_client: AsyncCloudflare) -> None:
        async with async_client.dns.records.with_streaming_response.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            record = await response.parse()
            assert_matches_type(Optional[RecordResponse], record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_update_overload_4(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.dns.records.with_raw_response.update(
                dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_record_id` but received ''"):
            await async_client.dns.records.with_raw_response.update(
                dns_record_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_update_overload_5(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_update_with_all_params_overload_5(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            comment="Domain verification record",
            content="content",
            name="example.com",
            proxied=True,
            settings={
                "flatten_cname": True,
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
            type="CNAME",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_update_overload_5(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dns.records.with_raw_response.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        record = await response.parse()
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_update_overload_5(self, async_client: AsyncCloudflare) -> None:
        async with async_client.dns.records.with_streaming_response.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            record = await response.parse()
            assert_matches_type(Optional[RecordResponse], record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_update_overload_5(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.dns.records.with_raw_response.update(
                dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_record_id` but received ''"):
            await async_client.dns.records.with_raw_response.update(
                dns_record_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_update_overload_6(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_update_with_all_params_overload_6(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            comment="Domain verification record",
            data={
                "algorithm": 5,
                "flags": 1,
                "protocol": 3,
                "public_key": "public_key",
            },
            name="example.com",
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
            type="DNSKEY",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_update_overload_6(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dns.records.with_raw_response.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        record = await response.parse()
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_update_overload_6(self, async_client: AsyncCloudflare) -> None:
        async with async_client.dns.records.with_streaming_response.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            record = await response.parse()
            assert_matches_type(Optional[RecordResponse], record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_update_overload_6(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.dns.records.with_raw_response.update(
                dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_record_id` but received ''"):
            await async_client.dns.records.with_raw_response.update(
                dns_record_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_update_overload_7(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_update_with_all_params_overload_7(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            comment="Domain verification record",
            data={
                "algorithm": 3,
                "digest": "digest",
                "digest_type": 1,
                "key_tag": 1,
            },
            name="example.com",
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
            type="DS",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_update_overload_7(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dns.records.with_raw_response.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        record = await response.parse()
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_update_overload_7(self, async_client: AsyncCloudflare) -> None:
        async with async_client.dns.records.with_streaming_response.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            record = await response.parse()
            assert_matches_type(Optional[RecordResponse], record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_update_overload_7(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.dns.records.with_raw_response.update(
                dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_record_id` but received ''"):
            await async_client.dns.records.with_raw_response.update(
                dns_record_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_update_overload_8(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_update_with_all_params_overload_8(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            comment="Domain verification record",
            data={
                "priority": 1,
                "target": ".",
                "value": 'alpn="h3,h2" ipv4hint="127.0.0.1" ipv6hint="::1"',
            },
            name="example.com",
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
            type="HTTPS",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_update_overload_8(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dns.records.with_raw_response.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        record = await response.parse()
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_update_overload_8(self, async_client: AsyncCloudflare) -> None:
        async with async_client.dns.records.with_streaming_response.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            record = await response.parse()
            assert_matches_type(Optional[RecordResponse], record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_update_overload_8(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.dns.records.with_raw_response.update(
                dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_record_id` but received ''"):
            await async_client.dns.records.with_raw_response.update(
                dns_record_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_update_overload_9(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_update_with_all_params_overload_9(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            comment="Domain verification record",
            data={
                "altitude": 0,
                "lat_degrees": 37,
                "lat_direction": "N",
                "lat_minutes": 46,
                "lat_seconds": 46,
                "long_degrees": 122,
                "long_direction": "E",
                "long_minutes": 23,
                "long_seconds": 35,
                "precision_horz": 0,
                "precision_vert": 0,
                "size": 100,
            },
            name="example.com",
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
            type="LOC",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_update_overload_9(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dns.records.with_raw_response.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        record = await response.parse()
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_update_overload_9(self, async_client: AsyncCloudflare) -> None:
        async with async_client.dns.records.with_streaming_response.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            record = await response.parse()
            assert_matches_type(Optional[RecordResponse], record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_update_overload_9(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.dns.records.with_raw_response.update(
                dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_record_id` but received ''"):
            await async_client.dns.records.with_raw_response.update(
                dns_record_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_update_overload_10(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_update_with_all_params_overload_10(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            comment="Domain verification record",
            content="mx.example.com",
            name="example.com",
            priority=10,
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
            type="MX",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_update_overload_10(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dns.records.with_raw_response.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        record = await response.parse()
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_update_overload_10(self, async_client: AsyncCloudflare) -> None:
        async with async_client.dns.records.with_streaming_response.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            record = await response.parse()
            assert_matches_type(Optional[RecordResponse], record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_update_overload_10(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.dns.records.with_raw_response.update(
                dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_record_id` but received ''"):
            await async_client.dns.records.with_raw_response.update(
                dns_record_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_update_overload_11(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_update_with_all_params_overload_11(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            comment="Domain verification record",
            data={
                "flags": "flags",
                "order": 100,
                "preference": 10,
                "regex": "regex",
                "replacement": "replacement",
                "service": "service",
            },
            name="example.com",
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
            type="NAPTR",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_update_overload_11(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dns.records.with_raw_response.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        record = await response.parse()
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_update_overload_11(self, async_client: AsyncCloudflare) -> None:
        async with async_client.dns.records.with_streaming_response.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            record = await response.parse()
            assert_matches_type(Optional[RecordResponse], record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_update_overload_11(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.dns.records.with_raw_response.update(
                dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_record_id` but received ''"):
            await async_client.dns.records.with_raw_response.update(
                dns_record_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_update_overload_12(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_update_with_all_params_overload_12(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            comment="Domain verification record",
            content="ns1.example.com",
            name="example.com",
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
            type="NS",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_update_overload_12(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dns.records.with_raw_response.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        record = await response.parse()
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_update_overload_12(self, async_client: AsyncCloudflare) -> None:
        async with async_client.dns.records.with_streaming_response.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            record = await response.parse()
            assert_matches_type(Optional[RecordResponse], record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_update_overload_12(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.dns.records.with_raw_response.update(
                dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_record_id` but received ''"):
            await async_client.dns.records.with_raw_response.update(
                dns_record_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_update_overload_13(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_update_with_all_params_overload_13(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            comment="Domain verification record",
            content="content",
            name="example.com",
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
            type="OPENPGPKEY",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_update_overload_13(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dns.records.with_raw_response.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        record = await response.parse()
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_update_overload_13(self, async_client: AsyncCloudflare) -> None:
        async with async_client.dns.records.with_streaming_response.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            record = await response.parse()
            assert_matches_type(Optional[RecordResponse], record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_update_overload_13(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.dns.records.with_raw_response.update(
                dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_record_id` but received ''"):
            await async_client.dns.records.with_raw_response.update(
                dns_record_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_update_overload_14(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_update_with_all_params_overload_14(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            comment="Domain verification record",
            content="example.com",
            name="example.com",
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
            type="PTR",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_update_overload_14(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dns.records.with_raw_response.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        record = await response.parse()
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_update_overload_14(self, async_client: AsyncCloudflare) -> None:
        async with async_client.dns.records.with_streaming_response.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            record = await response.parse()
            assert_matches_type(Optional[RecordResponse], record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_update_overload_14(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.dns.records.with_raw_response.update(
                dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_record_id` but received ''"):
            await async_client.dns.records.with_raw_response.update(
                dns_record_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_update_overload_15(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_update_with_all_params_overload_15(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            comment="Domain verification record",
            data={
                "certificate": "certificate",
                "matching_type": 0,
                "selector": 0,
                "usage": 3,
            },
            name="example.com",
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
            type="SMIMEA",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_update_overload_15(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dns.records.with_raw_response.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        record = await response.parse()
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_update_overload_15(self, async_client: AsyncCloudflare) -> None:
        async with async_client.dns.records.with_streaming_response.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            record = await response.parse()
            assert_matches_type(Optional[RecordResponse], record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_update_overload_15(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.dns.records.with_raw_response.update(
                dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_record_id` but received ''"):
            await async_client.dns.records.with_raw_response.update(
                dns_record_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_update_overload_16(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_update_with_all_params_overload_16(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            comment="Domain verification record",
            data={
                "port": 8806,
                "priority": 10,
                "target": "example.com",
                "weight": 5,
            },
            name="example.com",
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
            type="SRV",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_update_overload_16(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dns.records.with_raw_response.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        record = await response.parse()
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_update_overload_16(self, async_client: AsyncCloudflare) -> None:
        async with async_client.dns.records.with_streaming_response.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            record = await response.parse()
            assert_matches_type(Optional[RecordResponse], record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_update_overload_16(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.dns.records.with_raw_response.update(
                dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_record_id` but received ''"):
            await async_client.dns.records.with_raw_response.update(
                dns_record_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_update_overload_17(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_update_with_all_params_overload_17(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            comment="Domain verification record",
            data={
                "algorithm": 2,
                "fingerprint": "fingerprint",
                "type": 1,
            },
            name="example.com",
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
            type="SSHFP",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_update_overload_17(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dns.records.with_raw_response.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        record = await response.parse()
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_update_overload_17(self, async_client: AsyncCloudflare) -> None:
        async with async_client.dns.records.with_streaming_response.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            record = await response.parse()
            assert_matches_type(Optional[RecordResponse], record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_update_overload_17(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.dns.records.with_raw_response.update(
                dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_record_id` but received ''"):
            await async_client.dns.records.with_raw_response.update(
                dns_record_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_update_overload_18(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_update_with_all_params_overload_18(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            comment="Domain verification record",
            data={
                "priority": 1,
                "target": ".",
                "value": 'alpn="h3,h2" ipv4hint="127.0.0.1" ipv6hint="::1"',
            },
            name="example.com",
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
            type="SVCB",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_update_overload_18(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dns.records.with_raw_response.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        record = await response.parse()
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_update_overload_18(self, async_client: AsyncCloudflare) -> None:
        async with async_client.dns.records.with_streaming_response.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            record = await response.parse()
            assert_matches_type(Optional[RecordResponse], record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_update_overload_18(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.dns.records.with_raw_response.update(
                dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_record_id` but received ''"):
            await async_client.dns.records.with_raw_response.update(
                dns_record_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_update_overload_19(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_update_with_all_params_overload_19(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            comment="Domain verification record",
            data={
                "certificate": "certificate",
                "matching_type": 1,
                "selector": 0,
                "usage": 0,
            },
            name="example.com",
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
            type="TLSA",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_update_overload_19(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dns.records.with_raw_response.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        record = await response.parse()
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_update_overload_19(self, async_client: AsyncCloudflare) -> None:
        async with async_client.dns.records.with_streaming_response.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            record = await response.parse()
            assert_matches_type(Optional[RecordResponse], record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_update_overload_19(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.dns.records.with_raw_response.update(
                dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_record_id` but received ''"):
            await async_client.dns.records.with_raw_response.update(
                dns_record_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_update_overload_20(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_update_with_all_params_overload_20(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            comment="Domain verification record",
            content='"v=spf1 include:example.com -all"',
            name="example.com",
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
            type="TXT",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_update_overload_20(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dns.records.with_raw_response.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        record = await response.parse()
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_update_overload_20(self, async_client: AsyncCloudflare) -> None:
        async with async_client.dns.records.with_streaming_response.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            record = await response.parse()
            assert_matches_type(Optional[RecordResponse], record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_update_overload_20(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.dns.records.with_raw_response.update(
                dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_record_id` but received ''"):
            await async_client.dns.records.with_raw_response.update(
                dns_record_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_update_overload_21(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_update_with_all_params_overload_21(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            comment="Domain verification record",
            data={
                "target": "http://example.com/example.html",
                "weight": 20,
            },
            name="example.com",
            priority=10,
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
            type="URI",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_update_overload_21(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dns.records.with_raw_response.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        record = await response.parse()
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_update_overload_21(self, async_client: AsyncCloudflare) -> None:
        async with async_client.dns.records.with_streaming_response.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            record = await response.parse()
            assert_matches_type(Optional[RecordResponse], record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_update_overload_21(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.dns.records.with_raw_response.update(
                dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_record_id` but received ''"):
            await async_client.dns.records.with_raw_response.update(
                dns_record_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip(reason="mock server returns invalid data")
    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.list(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(AsyncV4PagePaginationArray[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="mock server returns invalid data")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.list(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            comment={
                "absent": "absent",
                "contains": "ello, worl",
                "endswith": "o, world",
                "exact": "Hello, world",
                "present": "present",
                "startswith": "Hello, w",
            },
            content={
                "contains": "7.0.0.",
                "endswith": ".0.1",
                "exact": "127.0.0.1",
                "startswith": "127.0.",
            },
            direction="asc",
            match="any",
            name={
                "contains": "w.example.",
                "endswith": ".example.com",
                "exact": "www.example.com",
                "startswith": "www.example",
            },
            order="type",
            page=1,
            per_page=5,
            proxied=True,
            search="www.cloudflare.com",
            tag={
                "absent": "important",
                "contains": "greeting:ello, worl",
                "endswith": "greeting:o, world",
                "exact": "greeting:Hello, world",
                "present": "important",
                "startswith": "greeting:Hello, w",
            },
            tag_match="any",
            type="A",
        )
        assert_matches_type(AsyncV4PagePaginationArray[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="mock server returns invalid data")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dns.records.with_raw_response.list(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        record = await response.parse()
        assert_matches_type(AsyncV4PagePaginationArray[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="mock server returns invalid data")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.dns.records.with_streaming_response.list(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            record = await response.parse()
            assert_matches_type(AsyncV4PagePaginationArray[RecordResponse], record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="mock server returns invalid data")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.dns.records.with_raw_response.list(
                zone_id="",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.delete(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[RecordDeleteResponse], record, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dns.records.with_raw_response.delete(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        record = await response.parse()
        assert_matches_type(Optional[RecordDeleteResponse], record, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.dns.records.with_streaming_response.delete(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            record = await response.parse()
            assert_matches_type(Optional[RecordDeleteResponse], record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.dns.records.with_raw_response.delete(
                dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_record_id` but received ''"):
            await async_client.dns.records.with_raw_response.delete(
                dns_record_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip(reason="TODO: investigate auth errors on test suite")
    @parametrize
    async def test_method_batch(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.batch(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[RecordBatchResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate auth errors on test suite")
    @parametrize
    async def test_method_batch_with_all_params(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.batch(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            deletes=[{"id": "023e105f4ecef8ad9ca31a8372d0c353"}],
            patches=[
                {
                    "comment": "Domain verification record",
                    "content": "198.51.100.4",
                    "name": "example.com",
                    "proxied": True,
                    "settings": {
                        "ipv4_only": True,
                        "ipv6_only": True,
                    },
                    "tags": ["owner:dns-team"],
                    "ttl": 3600,
                    "type": "A",
                    "id": "023e105f4ecef8ad9ca31a8372d0c353",
                }
            ],
            posts=[
                {
                    "comment": "Domain verification record",
                    "content": "198.51.100.4",
                    "name": "example.com",
                    "proxied": True,
                    "settings": {
                        "ipv4_only": True,
                        "ipv6_only": True,
                    },
                    "tags": ["owner:dns-team"],
                    "ttl": 3600,
                    "type": "A",
                }
            ],
            puts=[
                {
                    "comment": "Domain verification record",
                    "content": "198.51.100.4",
                    "name": "example.com",
                    "proxied": True,
                    "settings": {
                        "ipv4_only": True,
                        "ipv6_only": True,
                    },
                    "tags": ["owner:dns-team"],
                    "ttl": 3600,
                    "type": "A",
                    "id": "023e105f4ecef8ad9ca31a8372d0c353",
                }
            ],
        )
        assert_matches_type(Optional[RecordBatchResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate auth errors on test suite")
    @parametrize
    async def test_raw_response_batch(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dns.records.with_raw_response.batch(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        record = await response.parse()
        assert_matches_type(Optional[RecordBatchResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate auth errors on test suite")
    @parametrize
    async def test_streaming_response_batch(self, async_client: AsyncCloudflare) -> None:
        async with async_client.dns.records.with_streaming_response.batch(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            record = await response.parse()
            assert_matches_type(Optional[RecordBatchResponse], record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate auth errors on test suite")
    @parametrize
    async def test_path_params_batch(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.dns.records.with_raw_response.batch(
                zone_id="",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_edit_overload_1(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_edit_with_all_params_overload_1(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            comment="Domain verification record",
            content="198.51.100.4",
            name="example.com",
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
            type="A",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_edit_overload_1(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dns.records.with_raw_response.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        record = await response.parse()
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_edit_overload_1(self, async_client: AsyncCloudflare) -> None:
        async with async_client.dns.records.with_streaming_response.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            record = await response.parse()
            assert_matches_type(Optional[RecordResponse], record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_edit_overload_1(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.dns.records.with_raw_response.edit(
                dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_record_id` but received ''"):
            await async_client.dns.records.with_raw_response.edit(
                dns_record_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_edit_overload_2(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_edit_with_all_params_overload_2(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            comment="Domain verification record",
            content="2400:cb00:2049::1",
            name="example.com",
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
            type="AAAA",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_edit_overload_2(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dns.records.with_raw_response.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        record = await response.parse()
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_edit_overload_2(self, async_client: AsyncCloudflare) -> None:
        async with async_client.dns.records.with_streaming_response.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            record = await response.parse()
            assert_matches_type(Optional[RecordResponse], record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_edit_overload_2(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.dns.records.with_raw_response.edit(
                dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_record_id` but received ''"):
            await async_client.dns.records.with_raw_response.edit(
                dns_record_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_edit_overload_3(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_edit_with_all_params_overload_3(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            comment="Domain verification record",
            data={
                "flags": 1,
                "tag": "issue",
                "value": "value",
            },
            name="example.com",
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
            type="CAA",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_edit_overload_3(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dns.records.with_raw_response.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        record = await response.parse()
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_edit_overload_3(self, async_client: AsyncCloudflare) -> None:
        async with async_client.dns.records.with_streaming_response.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            record = await response.parse()
            assert_matches_type(Optional[RecordResponse], record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_edit_overload_3(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.dns.records.with_raw_response.edit(
                dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_record_id` but received ''"):
            await async_client.dns.records.with_raw_response.edit(
                dns_record_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_edit_overload_4(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_edit_with_all_params_overload_4(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            comment="Domain verification record",
            data={
                "algorithm": 8,
                "certificate": "certificate",
                "key_tag": 1,
                "type": 9,
            },
            name="example.com",
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
            type="CERT",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_edit_overload_4(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dns.records.with_raw_response.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        record = await response.parse()
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_edit_overload_4(self, async_client: AsyncCloudflare) -> None:
        async with async_client.dns.records.with_streaming_response.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            record = await response.parse()
            assert_matches_type(Optional[RecordResponse], record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_edit_overload_4(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.dns.records.with_raw_response.edit(
                dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_record_id` but received ''"):
            await async_client.dns.records.with_raw_response.edit(
                dns_record_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_edit_overload_5(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_edit_with_all_params_overload_5(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            comment="Domain verification record",
            content="content",
            name="example.com",
            proxied=True,
            settings={
                "flatten_cname": True,
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
            type="CNAME",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_edit_overload_5(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dns.records.with_raw_response.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        record = await response.parse()
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_edit_overload_5(self, async_client: AsyncCloudflare) -> None:
        async with async_client.dns.records.with_streaming_response.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            record = await response.parse()
            assert_matches_type(Optional[RecordResponse], record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_edit_overload_5(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.dns.records.with_raw_response.edit(
                dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_record_id` but received ''"):
            await async_client.dns.records.with_raw_response.edit(
                dns_record_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_edit_overload_6(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_edit_with_all_params_overload_6(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            comment="Domain verification record",
            data={
                "algorithm": 5,
                "flags": 1,
                "protocol": 3,
                "public_key": "public_key",
            },
            name="example.com",
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
            type="DNSKEY",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_edit_overload_6(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dns.records.with_raw_response.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        record = await response.parse()
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_edit_overload_6(self, async_client: AsyncCloudflare) -> None:
        async with async_client.dns.records.with_streaming_response.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            record = await response.parse()
            assert_matches_type(Optional[RecordResponse], record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_edit_overload_6(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.dns.records.with_raw_response.edit(
                dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_record_id` but received ''"):
            await async_client.dns.records.with_raw_response.edit(
                dns_record_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_edit_overload_7(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_edit_with_all_params_overload_7(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            comment="Domain verification record",
            data={
                "algorithm": 3,
                "digest": "digest",
                "digest_type": 1,
                "key_tag": 1,
            },
            name="example.com",
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
            type="DS",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_edit_overload_7(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dns.records.with_raw_response.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        record = await response.parse()
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_edit_overload_7(self, async_client: AsyncCloudflare) -> None:
        async with async_client.dns.records.with_streaming_response.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            record = await response.parse()
            assert_matches_type(Optional[RecordResponse], record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_edit_overload_7(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.dns.records.with_raw_response.edit(
                dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_record_id` but received ''"):
            await async_client.dns.records.with_raw_response.edit(
                dns_record_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_edit_overload_8(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_edit_with_all_params_overload_8(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            comment="Domain verification record",
            data={
                "priority": 1,
                "target": ".",
                "value": 'alpn="h3,h2" ipv4hint="127.0.0.1" ipv6hint="::1"',
            },
            name="example.com",
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
            type="HTTPS",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_edit_overload_8(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dns.records.with_raw_response.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        record = await response.parse()
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_edit_overload_8(self, async_client: AsyncCloudflare) -> None:
        async with async_client.dns.records.with_streaming_response.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            record = await response.parse()
            assert_matches_type(Optional[RecordResponse], record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_edit_overload_8(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.dns.records.with_raw_response.edit(
                dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_record_id` but received ''"):
            await async_client.dns.records.with_raw_response.edit(
                dns_record_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_edit_overload_9(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_edit_with_all_params_overload_9(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            comment="Domain verification record",
            data={
                "altitude": 0,
                "lat_degrees": 37,
                "lat_direction": "N",
                "lat_minutes": 46,
                "lat_seconds": 46,
                "long_degrees": 122,
                "long_direction": "E",
                "long_minutes": 23,
                "long_seconds": 35,
                "precision_horz": 0,
                "precision_vert": 0,
                "size": 100,
            },
            name="example.com",
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
            type="LOC",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_edit_overload_9(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dns.records.with_raw_response.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        record = await response.parse()
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_edit_overload_9(self, async_client: AsyncCloudflare) -> None:
        async with async_client.dns.records.with_streaming_response.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            record = await response.parse()
            assert_matches_type(Optional[RecordResponse], record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_edit_overload_9(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.dns.records.with_raw_response.edit(
                dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_record_id` but received ''"):
            await async_client.dns.records.with_raw_response.edit(
                dns_record_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_edit_overload_10(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_edit_with_all_params_overload_10(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            comment="Domain verification record",
            content="mx.example.com",
            name="example.com",
            priority=10,
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
            type="MX",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_edit_overload_10(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dns.records.with_raw_response.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        record = await response.parse()
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_edit_overload_10(self, async_client: AsyncCloudflare) -> None:
        async with async_client.dns.records.with_streaming_response.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            record = await response.parse()
            assert_matches_type(Optional[RecordResponse], record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_edit_overload_10(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.dns.records.with_raw_response.edit(
                dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_record_id` but received ''"):
            await async_client.dns.records.with_raw_response.edit(
                dns_record_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_edit_overload_11(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_edit_with_all_params_overload_11(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            comment="Domain verification record",
            data={
                "flags": "flags",
                "order": 100,
                "preference": 10,
                "regex": "regex",
                "replacement": "replacement",
                "service": "service",
            },
            name="example.com",
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
            type="NAPTR",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_edit_overload_11(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dns.records.with_raw_response.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        record = await response.parse()
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_edit_overload_11(self, async_client: AsyncCloudflare) -> None:
        async with async_client.dns.records.with_streaming_response.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            record = await response.parse()
            assert_matches_type(Optional[RecordResponse], record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_edit_overload_11(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.dns.records.with_raw_response.edit(
                dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_record_id` but received ''"):
            await async_client.dns.records.with_raw_response.edit(
                dns_record_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_edit_overload_12(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_edit_with_all_params_overload_12(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            comment="Domain verification record",
            content="ns1.example.com",
            name="example.com",
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
            type="NS",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_edit_overload_12(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dns.records.with_raw_response.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        record = await response.parse()
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_edit_overload_12(self, async_client: AsyncCloudflare) -> None:
        async with async_client.dns.records.with_streaming_response.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            record = await response.parse()
            assert_matches_type(Optional[RecordResponse], record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_edit_overload_12(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.dns.records.with_raw_response.edit(
                dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_record_id` but received ''"):
            await async_client.dns.records.with_raw_response.edit(
                dns_record_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_edit_overload_13(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_edit_with_all_params_overload_13(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            comment="Domain verification record",
            content="content",
            name="example.com",
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
            type="OPENPGPKEY",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_edit_overload_13(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dns.records.with_raw_response.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        record = await response.parse()
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_edit_overload_13(self, async_client: AsyncCloudflare) -> None:
        async with async_client.dns.records.with_streaming_response.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            record = await response.parse()
            assert_matches_type(Optional[RecordResponse], record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_edit_overload_13(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.dns.records.with_raw_response.edit(
                dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_record_id` but received ''"):
            await async_client.dns.records.with_raw_response.edit(
                dns_record_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_edit_overload_14(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_edit_with_all_params_overload_14(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            comment="Domain verification record",
            content="example.com",
            name="example.com",
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
            type="PTR",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_edit_overload_14(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dns.records.with_raw_response.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        record = await response.parse()
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_edit_overload_14(self, async_client: AsyncCloudflare) -> None:
        async with async_client.dns.records.with_streaming_response.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            record = await response.parse()
            assert_matches_type(Optional[RecordResponse], record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_edit_overload_14(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.dns.records.with_raw_response.edit(
                dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_record_id` but received ''"):
            await async_client.dns.records.with_raw_response.edit(
                dns_record_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_edit_overload_15(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_edit_with_all_params_overload_15(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            comment="Domain verification record",
            data={
                "certificate": "certificate",
                "matching_type": 0,
                "selector": 0,
                "usage": 3,
            },
            name="example.com",
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
            type="SMIMEA",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_edit_overload_15(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dns.records.with_raw_response.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        record = await response.parse()
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_edit_overload_15(self, async_client: AsyncCloudflare) -> None:
        async with async_client.dns.records.with_streaming_response.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            record = await response.parse()
            assert_matches_type(Optional[RecordResponse], record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_edit_overload_15(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.dns.records.with_raw_response.edit(
                dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_record_id` but received ''"):
            await async_client.dns.records.with_raw_response.edit(
                dns_record_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_edit_overload_16(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_edit_with_all_params_overload_16(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            comment="Domain verification record",
            data={
                "port": 8806,
                "priority": 10,
                "target": "example.com",
                "weight": 5,
            },
            name="example.com",
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
            type="SRV",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_edit_overload_16(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dns.records.with_raw_response.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        record = await response.parse()
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_edit_overload_16(self, async_client: AsyncCloudflare) -> None:
        async with async_client.dns.records.with_streaming_response.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            record = await response.parse()
            assert_matches_type(Optional[RecordResponse], record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_edit_overload_16(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.dns.records.with_raw_response.edit(
                dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_record_id` but received ''"):
            await async_client.dns.records.with_raw_response.edit(
                dns_record_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_edit_overload_17(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_edit_with_all_params_overload_17(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            comment="Domain verification record",
            data={
                "algorithm": 2,
                "fingerprint": "fingerprint",
                "type": 1,
            },
            name="example.com",
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
            type="SSHFP",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_edit_overload_17(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dns.records.with_raw_response.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        record = await response.parse()
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_edit_overload_17(self, async_client: AsyncCloudflare) -> None:
        async with async_client.dns.records.with_streaming_response.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            record = await response.parse()
            assert_matches_type(Optional[RecordResponse], record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_edit_overload_17(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.dns.records.with_raw_response.edit(
                dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_record_id` but received ''"):
            await async_client.dns.records.with_raw_response.edit(
                dns_record_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_edit_overload_18(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_edit_with_all_params_overload_18(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            comment="Domain verification record",
            data={
                "priority": 1,
                "target": ".",
                "value": 'alpn="h3,h2" ipv4hint="127.0.0.1" ipv6hint="::1"',
            },
            name="example.com",
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
            type="SVCB",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_edit_overload_18(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dns.records.with_raw_response.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        record = await response.parse()
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_edit_overload_18(self, async_client: AsyncCloudflare) -> None:
        async with async_client.dns.records.with_streaming_response.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            record = await response.parse()
            assert_matches_type(Optional[RecordResponse], record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_edit_overload_18(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.dns.records.with_raw_response.edit(
                dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_record_id` but received ''"):
            await async_client.dns.records.with_raw_response.edit(
                dns_record_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_edit_overload_19(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_edit_with_all_params_overload_19(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            comment="Domain verification record",
            data={
                "certificate": "certificate",
                "matching_type": 1,
                "selector": 0,
                "usage": 0,
            },
            name="example.com",
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
            type="TLSA",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_edit_overload_19(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dns.records.with_raw_response.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        record = await response.parse()
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_edit_overload_19(self, async_client: AsyncCloudflare) -> None:
        async with async_client.dns.records.with_streaming_response.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            record = await response.parse()
            assert_matches_type(Optional[RecordResponse], record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_edit_overload_19(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.dns.records.with_raw_response.edit(
                dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_record_id` but received ''"):
            await async_client.dns.records.with_raw_response.edit(
                dns_record_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_edit_overload_20(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_edit_with_all_params_overload_20(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            comment="Domain verification record",
            content='"v=spf1 include:example.com -all"',
            name="example.com",
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
            type="TXT",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_edit_overload_20(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dns.records.with_raw_response.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        record = await response.parse()
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_edit_overload_20(self, async_client: AsyncCloudflare) -> None:
        async with async_client.dns.records.with_streaming_response.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            record = await response.parse()
            assert_matches_type(Optional[RecordResponse], record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_edit_overload_20(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.dns.records.with_raw_response.edit(
                dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_record_id` but received ''"):
            await async_client.dns.records.with_raw_response.edit(
                dns_record_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_edit_overload_21(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_edit_with_all_params_overload_21(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            comment="Domain verification record",
            data={
                "target": "http://example.com/example.html",
                "weight": 20,
            },
            name="example.com",
            priority=10,
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
            type="URI",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_edit_overload_21(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dns.records.with_raw_response.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        record = await response.parse()
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_edit_overload_21(self, async_client: AsyncCloudflare) -> None:
        async with async_client.dns.records.with_streaming_response.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            record = await response.parse()
            assert_matches_type(Optional[RecordResponse], record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_edit_overload_21(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.dns.records.with_raw_response.edit(
                dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_record_id` but received ''"):
            await async_client.dns.records.with_raw_response.edit(
                dns_record_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    async def test_method_export(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.export(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(str, record, path=["response"])

    @parametrize
    async def test_raw_response_export(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dns.records.with_raw_response.export(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        record = await response.parse()
        assert_matches_type(str, record, path=["response"])

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

    @parametrize
    async def test_path_params_export(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.dns.records.with_raw_response.export(
                zone_id="",
            )

    @pytest.mark.skip(reason="mock server returns invalid data")
    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.get(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="mock server returns invalid data")
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dns.records.with_raw_response.get(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        record = await response.parse()
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="mock server returns invalid data")
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.dns.records.with_streaming_response.get(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            record = await response.parse()
            assert_matches_type(Optional[RecordResponse], record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="mock server returns invalid data")
    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.dns.records.with_raw_response.get(
                dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_record_id` but received ''"):
            await async_client.dns.records.with_raw_response.get(
                dns_record_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_import(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.import_(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            file="www.example.com. 300 IN  A 127.0.0.1",
        )
        assert_matches_type(Optional[RecordImportResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_import_with_all_params(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.import_(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            file="www.example.com. 300 IN  A 127.0.0.1",
            proxied="true",
        )
        assert_matches_type(Optional[RecordImportResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_import(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dns.records.with_raw_response.import_(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            file="www.example.com. 300 IN  A 127.0.0.1",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        record = await response.parse()
        assert_matches_type(Optional[RecordImportResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_import(self, async_client: AsyncCloudflare) -> None:
        async with async_client.dns.records.with_streaming_response.import_(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            file="www.example.com. 300 IN  A 127.0.0.1",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            record = await response.parse()
            assert_matches_type(Optional[RecordImportResponse], record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_import(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.dns.records.with_raw_response.import_(
                zone_id="",
                file="www.example.com. 300 IN  A 127.0.0.1",
            )

    @parametrize
    async def test_method_scan(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.scan(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        )
        assert_matches_type(Optional[RecordScanResponse], record, path=["response"])

    @parametrize
    async def test_raw_response_scan(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dns.records.with_raw_response.scan(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        record = await response.parse()
        assert_matches_type(Optional[RecordScanResponse], record, path=["response"])

    @parametrize
    async def test_streaming_response_scan(self, async_client: AsyncCloudflare) -> None:
        async with async_client.dns.records.with_streaming_response.scan(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            record = await response.parse()
            assert_matches_type(Optional[RecordScanResponse], record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_scan(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.dns.records.with_raw_response.scan(
                zone_id="",
                body={},
            )
