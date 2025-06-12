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
            name="example.com",
            type="A",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_create_with_all_params_overload_1(self, client: Cloudflare) -> None:
        record = client.dns.records.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="A",
            comment="Domain verification record",
            content="198.51.100.4",
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_create_overload_1(self, client: Cloudflare) -> None:
        response = client.dns.records.with_raw_response.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="A",
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
            name="example.com",
            type="A",
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
                name="example.com",
                type="A",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_create_overload_2(self, client: Cloudflare) -> None:
        record = client.dns.records.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="AAAA",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_create_with_all_params_overload_2(self, client: Cloudflare) -> None:
        record = client.dns.records.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="AAAA",
            comment="Domain verification record",
            content="2400:cb00:2049::1",
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_create_overload_2(self, client: Cloudflare) -> None:
        response = client.dns.records.with_raw_response.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="AAAA",
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
            name="example.com",
            type="AAAA",
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
                name="example.com",
                type="AAAA",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_create_overload_3(self, client: Cloudflare) -> None:
        record = client.dns.records.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="CNAME",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_create_with_all_params_overload_3(self, client: Cloudflare) -> None:
        record = client.dns.records.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="CNAME",
            comment="Domain verification record",
            content="content",
            proxied=True,
            settings={
                "flatten_cname": True,
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_create_overload_3(self, client: Cloudflare) -> None:
        response = client.dns.records.with_raw_response.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="CNAME",
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
            name="example.com",
            type="CNAME",
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
                name="example.com",
                type="CNAME",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_create_overload_4(self, client: Cloudflare) -> None:
        record = client.dns.records.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="MX",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_create_with_all_params_overload_4(self, client: Cloudflare) -> None:
        record = client.dns.records.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="MX",
            comment="Domain verification record",
            content="mx.example.com",
            priority=10,
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_create_overload_4(self, client: Cloudflare) -> None:
        response = client.dns.records.with_raw_response.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="MX",
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
            name="example.com",
            type="MX",
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
                name="example.com",
                type="MX",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_create_overload_5(self, client: Cloudflare) -> None:
        record = client.dns.records.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="NS",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_create_with_all_params_overload_5(self, client: Cloudflare) -> None:
        record = client.dns.records.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="NS",
            comment="Domain verification record",
            content="ns1.example.com",
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_create_overload_5(self, client: Cloudflare) -> None:
        response = client.dns.records.with_raw_response.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="NS",
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
            name="example.com",
            type="NS",
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
                name="example.com",
                type="NS",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_create_overload_6(self, client: Cloudflare) -> None:
        record = client.dns.records.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="OPENPGPKEY",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_create_with_all_params_overload_6(self, client: Cloudflare) -> None:
        record = client.dns.records.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="OPENPGPKEY",
            comment="Domain verification record",
            content="content",
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_create_overload_6(self, client: Cloudflare) -> None:
        response = client.dns.records.with_raw_response.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="OPENPGPKEY",
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
            name="example.com",
            type="OPENPGPKEY",
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
                name="example.com",
                type="OPENPGPKEY",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_create_overload_7(self, client: Cloudflare) -> None:
        record = client.dns.records.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="PTR",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_create_with_all_params_overload_7(self, client: Cloudflare) -> None:
        record = client.dns.records.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="PTR",
            comment="Domain verification record",
            content="example.com",
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_create_overload_7(self, client: Cloudflare) -> None:
        response = client.dns.records.with_raw_response.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="PTR",
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
            name="example.com",
            type="PTR",
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
                name="example.com",
                type="PTR",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_create_overload_8(self, client: Cloudflare) -> None:
        record = client.dns.records.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="TXT",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_create_with_all_params_overload_8(self, client: Cloudflare) -> None:
        record = client.dns.records.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="TXT",
            comment="Domain verification record",
            content='"v=spf1 include:example.com -all"',
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_create_overload_8(self, client: Cloudflare) -> None:
        response = client.dns.records.with_raw_response.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="TXT",
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
            name="example.com",
            type="TXT",
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
                name="example.com",
                type="TXT",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_create_overload_9(self, client: Cloudflare) -> None:
        record = client.dns.records.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="CAA",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_create_with_all_params_overload_9(self, client: Cloudflare) -> None:
        record = client.dns.records.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="CAA",
            comment="Domain verification record",
            data={
                "flags": 1,
                "tag": "issue",
                "value": "value",
            },
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_create_overload_9(self, client: Cloudflare) -> None:
        response = client.dns.records.with_raw_response.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="CAA",
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
            name="example.com",
            type="CAA",
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
                name="example.com",
                type="CAA",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_create_overload_10(self, client: Cloudflare) -> None:
        record = client.dns.records.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="CERT",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_create_with_all_params_overload_10(self, client: Cloudflare) -> None:
        record = client.dns.records.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="CERT",
            comment="Domain verification record",
            data={
                "algorithm": 8,
                "certificate": "certificate",
                "key_tag": 1,
                "type": 9,
            },
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_create_overload_10(self, client: Cloudflare) -> None:
        response = client.dns.records.with_raw_response.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="CERT",
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
            name="example.com",
            type="CERT",
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
                name="example.com",
                type="CERT",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_create_overload_11(self, client: Cloudflare) -> None:
        record = client.dns.records.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="DNSKEY",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_create_with_all_params_overload_11(self, client: Cloudflare) -> None:
        record = client.dns.records.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="DNSKEY",
            comment="Domain verification record",
            data={
                "algorithm": 5,
                "flags": 1,
                "protocol": 3,
                "public_key": "public_key",
            },
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_create_overload_11(self, client: Cloudflare) -> None:
        response = client.dns.records.with_raw_response.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="DNSKEY",
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
            name="example.com",
            type="DNSKEY",
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
                name="example.com",
                type="DNSKEY",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_create_overload_12(self, client: Cloudflare) -> None:
        record = client.dns.records.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="DS",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_create_with_all_params_overload_12(self, client: Cloudflare) -> None:
        record = client.dns.records.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="DS",
            comment="Domain verification record",
            data={
                "algorithm": 3,
                "digest": "digest",
                "digest_type": 1,
                "key_tag": 1,
            },
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_create_overload_12(self, client: Cloudflare) -> None:
        response = client.dns.records.with_raw_response.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="DS",
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
            name="example.com",
            type="DS",
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
                name="example.com",
                type="DS",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_create_overload_13(self, client: Cloudflare) -> None:
        record = client.dns.records.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="HTTPS",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_create_with_all_params_overload_13(self, client: Cloudflare) -> None:
        record = client.dns.records.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="HTTPS",
            comment="Domain verification record",
            data={
                "priority": 1,
                "target": ".",
                "value": 'alpn="h3,h2" ipv4hint="127.0.0.1" ipv6hint="::1"',
            },
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_create_overload_13(self, client: Cloudflare) -> None:
        response = client.dns.records.with_raw_response.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="HTTPS",
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
            name="example.com",
            type="HTTPS",
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
                name="example.com",
                type="HTTPS",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_create_overload_14(self, client: Cloudflare) -> None:
        record = client.dns.records.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="LOC",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_create_with_all_params_overload_14(self, client: Cloudflare) -> None:
        record = client.dns.records.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="LOC",
            comment="Domain verification record",
            data={
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
            },
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_create_overload_14(self, client: Cloudflare) -> None:
        response = client.dns.records.with_raw_response.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="LOC",
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
            name="example.com",
            type="LOC",
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
                name="example.com",
                type="LOC",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_create_overload_15(self, client: Cloudflare) -> None:
        record = client.dns.records.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="NAPTR",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_create_with_all_params_overload_15(self, client: Cloudflare) -> None:
        record = client.dns.records.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="NAPTR",
            comment="Domain verification record",
            data={
                "flags": "flags",
                "order": 100,
                "preference": 10,
                "regex": "regex",
                "replacement": "replacement",
                "service": "service",
            },
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_create_overload_15(self, client: Cloudflare) -> None:
        response = client.dns.records.with_raw_response.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="NAPTR",
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
            name="example.com",
            type="NAPTR",
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
                name="example.com",
                type="NAPTR",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_create_overload_16(self, client: Cloudflare) -> None:
        record = client.dns.records.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="SMIMEA",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_create_with_all_params_overload_16(self, client: Cloudflare) -> None:
        record = client.dns.records.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="SMIMEA",
            comment="Domain verification record",
            data={
                "certificate": "certificate",
                "matching_type": 0,
                "selector": 0,
                "usage": 3,
            },
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_create_overload_16(self, client: Cloudflare) -> None:
        response = client.dns.records.with_raw_response.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="SMIMEA",
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
            name="example.com",
            type="SMIMEA",
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
                name="example.com",
                type="SMIMEA",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_create_overload_17(self, client: Cloudflare) -> None:
        record = client.dns.records.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="SRV",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_create_with_all_params_overload_17(self, client: Cloudflare) -> None:
        record = client.dns.records.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="SRV",
            comment="Domain verification record",
            data={
                "port": 8806,
                "priority": 10,
                "target": "example.com",
                "weight": 5,
            },
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_create_overload_17(self, client: Cloudflare) -> None:
        response = client.dns.records.with_raw_response.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="SRV",
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
            name="example.com",
            type="SRV",
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
                name="example.com",
                type="SRV",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_create_overload_18(self, client: Cloudflare) -> None:
        record = client.dns.records.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="SSHFP",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_create_with_all_params_overload_18(self, client: Cloudflare) -> None:
        record = client.dns.records.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="SSHFP",
            comment="Domain verification record",
            data={
                "algorithm": 2,
                "fingerprint": "fingerprint",
                "type": 1,
            },
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_create_overload_18(self, client: Cloudflare) -> None:
        response = client.dns.records.with_raw_response.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="SSHFP",
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
            name="example.com",
            type="SSHFP",
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
                name="example.com",
                type="SSHFP",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_create_overload_19(self, client: Cloudflare) -> None:
        record = client.dns.records.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="SVCB",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_create_with_all_params_overload_19(self, client: Cloudflare) -> None:
        record = client.dns.records.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="SVCB",
            comment="Domain verification record",
            data={
                "priority": 1,
                "target": ".",
                "value": 'alpn="h3,h2" ipv4hint="127.0.0.1" ipv6hint="::1"',
            },
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_create_overload_19(self, client: Cloudflare) -> None:
        response = client.dns.records.with_raw_response.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="SVCB",
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
            name="example.com",
            type="SVCB",
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
                name="example.com",
                type="SVCB",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_create_overload_20(self, client: Cloudflare) -> None:
        record = client.dns.records.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="TLSA",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_create_with_all_params_overload_20(self, client: Cloudflare) -> None:
        record = client.dns.records.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="TLSA",
            comment="Domain verification record",
            data={
                "certificate": "certificate",
                "matching_type": 1,
                "selector": 0,
                "usage": 0,
            },
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_create_overload_20(self, client: Cloudflare) -> None:
        response = client.dns.records.with_raw_response.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="TLSA",
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
            name="example.com",
            type="TLSA",
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
                name="example.com",
                type="TLSA",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_create_overload_21(self, client: Cloudflare) -> None:
        record = client.dns.records.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="URI",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_create_with_all_params_overload_21(self, client: Cloudflare) -> None:
        record = client.dns.records.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="URI",
            comment="Domain verification record",
            data={
                "target": "http://example.com/example.html",
                "weight": 20,
            },
            priority=10,
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_create_overload_21(self, client: Cloudflare) -> None:
        response = client.dns.records.with_raw_response.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="URI",
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
            name="example.com",
            type="URI",
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
                name="example.com",
                type="URI",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_update_overload_1(self, client: Cloudflare) -> None:
        record = client.dns.records.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="A",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_update_with_all_params_overload_1(self, client: Cloudflare) -> None:
        record = client.dns.records.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="A",
            comment="Domain verification record",
            content="198.51.100.4",
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_update_overload_1(self, client: Cloudflare) -> None:
        response = client.dns.records.with_raw_response.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="A",
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
            name="example.com",
            type="A",
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
                name="example.com",
                type="A",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_record_id` but received ''"):
            client.dns.records.with_raw_response.update(
                dns_record_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                name="example.com",
                type="A",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_update_overload_2(self, client: Cloudflare) -> None:
        record = client.dns.records.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="AAAA",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_update_with_all_params_overload_2(self, client: Cloudflare) -> None:
        record = client.dns.records.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="AAAA",
            comment="Domain verification record",
            content="2400:cb00:2049::1",
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_update_overload_2(self, client: Cloudflare) -> None:
        response = client.dns.records.with_raw_response.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="AAAA",
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
            name="example.com",
            type="AAAA",
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
                name="example.com",
                type="AAAA",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_record_id` but received ''"):
            client.dns.records.with_raw_response.update(
                dns_record_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                name="example.com",
                type="AAAA",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_update_overload_3(self, client: Cloudflare) -> None:
        record = client.dns.records.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="CNAME",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_update_with_all_params_overload_3(self, client: Cloudflare) -> None:
        record = client.dns.records.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="CNAME",
            comment="Domain verification record",
            content="content",
            proxied=True,
            settings={
                "flatten_cname": True,
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_update_overload_3(self, client: Cloudflare) -> None:
        response = client.dns.records.with_raw_response.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="CNAME",
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
            name="example.com",
            type="CNAME",
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
                name="example.com",
                type="CNAME",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_record_id` but received ''"):
            client.dns.records.with_raw_response.update(
                dns_record_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                name="example.com",
                type="CNAME",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_update_overload_4(self, client: Cloudflare) -> None:
        record = client.dns.records.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="MX",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_update_with_all_params_overload_4(self, client: Cloudflare) -> None:
        record = client.dns.records.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="MX",
            comment="Domain verification record",
            content="mx.example.com",
            priority=10,
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_update_overload_4(self, client: Cloudflare) -> None:
        response = client.dns.records.with_raw_response.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="MX",
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
            name="example.com",
            type="MX",
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
                name="example.com",
                type="MX",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_record_id` but received ''"):
            client.dns.records.with_raw_response.update(
                dns_record_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                name="example.com",
                type="MX",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_update_overload_5(self, client: Cloudflare) -> None:
        record = client.dns.records.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="NS",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_update_with_all_params_overload_5(self, client: Cloudflare) -> None:
        record = client.dns.records.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="NS",
            comment="Domain verification record",
            content="ns1.example.com",
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_update_overload_5(self, client: Cloudflare) -> None:
        response = client.dns.records.with_raw_response.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="NS",
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
            name="example.com",
            type="NS",
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
                name="example.com",
                type="NS",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_record_id` but received ''"):
            client.dns.records.with_raw_response.update(
                dns_record_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                name="example.com",
                type="NS",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_update_overload_6(self, client: Cloudflare) -> None:
        record = client.dns.records.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="OPENPGPKEY",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_update_with_all_params_overload_6(self, client: Cloudflare) -> None:
        record = client.dns.records.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="OPENPGPKEY",
            comment="Domain verification record",
            content="content",
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_update_overload_6(self, client: Cloudflare) -> None:
        response = client.dns.records.with_raw_response.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="OPENPGPKEY",
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
            name="example.com",
            type="OPENPGPKEY",
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
                name="example.com",
                type="OPENPGPKEY",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_record_id` but received ''"):
            client.dns.records.with_raw_response.update(
                dns_record_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                name="example.com",
                type="OPENPGPKEY",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_update_overload_7(self, client: Cloudflare) -> None:
        record = client.dns.records.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="PTR",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_update_with_all_params_overload_7(self, client: Cloudflare) -> None:
        record = client.dns.records.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="PTR",
            comment="Domain verification record",
            content="example.com",
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_update_overload_7(self, client: Cloudflare) -> None:
        response = client.dns.records.with_raw_response.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="PTR",
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
            name="example.com",
            type="PTR",
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
                name="example.com",
                type="PTR",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_record_id` but received ''"):
            client.dns.records.with_raw_response.update(
                dns_record_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                name="example.com",
                type="PTR",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_update_overload_8(self, client: Cloudflare) -> None:
        record = client.dns.records.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="TXT",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_update_with_all_params_overload_8(self, client: Cloudflare) -> None:
        record = client.dns.records.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="TXT",
            comment="Domain verification record",
            content='"v=spf1 include:example.com -all"',
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_update_overload_8(self, client: Cloudflare) -> None:
        response = client.dns.records.with_raw_response.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="TXT",
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
            name="example.com",
            type="TXT",
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
                name="example.com",
                type="TXT",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_record_id` but received ''"):
            client.dns.records.with_raw_response.update(
                dns_record_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                name="example.com",
                type="TXT",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_update_overload_9(self, client: Cloudflare) -> None:
        record = client.dns.records.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="CAA",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_update_with_all_params_overload_9(self, client: Cloudflare) -> None:
        record = client.dns.records.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="CAA",
            comment="Domain verification record",
            data={
                "flags": 1,
                "tag": "issue",
                "value": "value",
            },
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_update_overload_9(self, client: Cloudflare) -> None:
        response = client.dns.records.with_raw_response.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="CAA",
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
            name="example.com",
            type="CAA",
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
                name="example.com",
                type="CAA",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_record_id` but received ''"):
            client.dns.records.with_raw_response.update(
                dns_record_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                name="example.com",
                type="CAA",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_update_overload_10(self, client: Cloudflare) -> None:
        record = client.dns.records.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="CERT",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_update_with_all_params_overload_10(self, client: Cloudflare) -> None:
        record = client.dns.records.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="CERT",
            comment="Domain verification record",
            data={
                "algorithm": 8,
                "certificate": "certificate",
                "key_tag": 1,
                "type": 9,
            },
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_update_overload_10(self, client: Cloudflare) -> None:
        response = client.dns.records.with_raw_response.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="CERT",
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
            name="example.com",
            type="CERT",
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
                name="example.com",
                type="CERT",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_record_id` but received ''"):
            client.dns.records.with_raw_response.update(
                dns_record_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                name="example.com",
                type="CERT",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_update_overload_11(self, client: Cloudflare) -> None:
        record = client.dns.records.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="DNSKEY",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_update_with_all_params_overload_11(self, client: Cloudflare) -> None:
        record = client.dns.records.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="DNSKEY",
            comment="Domain verification record",
            data={
                "algorithm": 5,
                "flags": 1,
                "protocol": 3,
                "public_key": "public_key",
            },
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_update_overload_11(self, client: Cloudflare) -> None:
        response = client.dns.records.with_raw_response.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="DNSKEY",
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
            name="example.com",
            type="DNSKEY",
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
                name="example.com",
                type="DNSKEY",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_record_id` but received ''"):
            client.dns.records.with_raw_response.update(
                dns_record_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                name="example.com",
                type="DNSKEY",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_update_overload_12(self, client: Cloudflare) -> None:
        record = client.dns.records.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="DS",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_update_with_all_params_overload_12(self, client: Cloudflare) -> None:
        record = client.dns.records.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="DS",
            comment="Domain verification record",
            data={
                "algorithm": 3,
                "digest": "digest",
                "digest_type": 1,
                "key_tag": 1,
            },
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_update_overload_12(self, client: Cloudflare) -> None:
        response = client.dns.records.with_raw_response.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="DS",
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
            name="example.com",
            type="DS",
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
                name="example.com",
                type="DS",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_record_id` but received ''"):
            client.dns.records.with_raw_response.update(
                dns_record_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                name="example.com",
                type="DS",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_update_overload_13(self, client: Cloudflare) -> None:
        record = client.dns.records.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="HTTPS",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_update_with_all_params_overload_13(self, client: Cloudflare) -> None:
        record = client.dns.records.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="HTTPS",
            comment="Domain verification record",
            data={
                "priority": 1,
                "target": ".",
                "value": 'alpn="h3,h2" ipv4hint="127.0.0.1" ipv6hint="::1"',
            },
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_update_overload_13(self, client: Cloudflare) -> None:
        response = client.dns.records.with_raw_response.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="HTTPS",
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
            name="example.com",
            type="HTTPS",
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
                name="example.com",
                type="HTTPS",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_record_id` but received ''"):
            client.dns.records.with_raw_response.update(
                dns_record_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                name="example.com",
                type="HTTPS",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_update_overload_14(self, client: Cloudflare) -> None:
        record = client.dns.records.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="LOC",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_update_with_all_params_overload_14(self, client: Cloudflare) -> None:
        record = client.dns.records.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="LOC",
            comment="Domain verification record",
            data={
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
            },
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_update_overload_14(self, client: Cloudflare) -> None:
        response = client.dns.records.with_raw_response.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="LOC",
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
            name="example.com",
            type="LOC",
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
                name="example.com",
                type="LOC",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_record_id` but received ''"):
            client.dns.records.with_raw_response.update(
                dns_record_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                name="example.com",
                type="LOC",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_update_overload_15(self, client: Cloudflare) -> None:
        record = client.dns.records.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="NAPTR",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_update_with_all_params_overload_15(self, client: Cloudflare) -> None:
        record = client.dns.records.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="NAPTR",
            comment="Domain verification record",
            data={
                "flags": "flags",
                "order": 100,
                "preference": 10,
                "regex": "regex",
                "replacement": "replacement",
                "service": "service",
            },
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_update_overload_15(self, client: Cloudflare) -> None:
        response = client.dns.records.with_raw_response.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="NAPTR",
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
            name="example.com",
            type="NAPTR",
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
                name="example.com",
                type="NAPTR",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_record_id` but received ''"):
            client.dns.records.with_raw_response.update(
                dns_record_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                name="example.com",
                type="NAPTR",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_update_overload_16(self, client: Cloudflare) -> None:
        record = client.dns.records.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="SMIMEA",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_update_with_all_params_overload_16(self, client: Cloudflare) -> None:
        record = client.dns.records.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="SMIMEA",
            comment="Domain verification record",
            data={
                "certificate": "certificate",
                "matching_type": 0,
                "selector": 0,
                "usage": 3,
            },
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_update_overload_16(self, client: Cloudflare) -> None:
        response = client.dns.records.with_raw_response.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="SMIMEA",
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
            name="example.com",
            type="SMIMEA",
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
                name="example.com",
                type="SMIMEA",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_record_id` but received ''"):
            client.dns.records.with_raw_response.update(
                dns_record_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                name="example.com",
                type="SMIMEA",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_update_overload_17(self, client: Cloudflare) -> None:
        record = client.dns.records.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="SRV",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_update_with_all_params_overload_17(self, client: Cloudflare) -> None:
        record = client.dns.records.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="SRV",
            comment="Domain verification record",
            data={
                "port": 8806,
                "priority": 10,
                "target": "example.com",
                "weight": 5,
            },
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_update_overload_17(self, client: Cloudflare) -> None:
        response = client.dns.records.with_raw_response.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="SRV",
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
            name="example.com",
            type="SRV",
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
                name="example.com",
                type="SRV",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_record_id` but received ''"):
            client.dns.records.with_raw_response.update(
                dns_record_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                name="example.com",
                type="SRV",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_update_overload_18(self, client: Cloudflare) -> None:
        record = client.dns.records.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="SSHFP",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_update_with_all_params_overload_18(self, client: Cloudflare) -> None:
        record = client.dns.records.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="SSHFP",
            comment="Domain verification record",
            data={
                "algorithm": 2,
                "fingerprint": "fingerprint",
                "type": 1,
            },
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_update_overload_18(self, client: Cloudflare) -> None:
        response = client.dns.records.with_raw_response.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="SSHFP",
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
            name="example.com",
            type="SSHFP",
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
                name="example.com",
                type="SSHFP",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_record_id` but received ''"):
            client.dns.records.with_raw_response.update(
                dns_record_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                name="example.com",
                type="SSHFP",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_update_overload_19(self, client: Cloudflare) -> None:
        record = client.dns.records.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="SVCB",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_update_with_all_params_overload_19(self, client: Cloudflare) -> None:
        record = client.dns.records.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="SVCB",
            comment="Domain verification record",
            data={
                "priority": 1,
                "target": ".",
                "value": 'alpn="h3,h2" ipv4hint="127.0.0.1" ipv6hint="::1"',
            },
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_update_overload_19(self, client: Cloudflare) -> None:
        response = client.dns.records.with_raw_response.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="SVCB",
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
            name="example.com",
            type="SVCB",
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
                name="example.com",
                type="SVCB",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_record_id` but received ''"):
            client.dns.records.with_raw_response.update(
                dns_record_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                name="example.com",
                type="SVCB",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_update_overload_20(self, client: Cloudflare) -> None:
        record = client.dns.records.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="TLSA",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_update_with_all_params_overload_20(self, client: Cloudflare) -> None:
        record = client.dns.records.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="TLSA",
            comment="Domain verification record",
            data={
                "certificate": "certificate",
                "matching_type": 1,
                "selector": 0,
                "usage": 0,
            },
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_update_overload_20(self, client: Cloudflare) -> None:
        response = client.dns.records.with_raw_response.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="TLSA",
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
            name="example.com",
            type="TLSA",
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
                name="example.com",
                type="TLSA",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_record_id` but received ''"):
            client.dns.records.with_raw_response.update(
                dns_record_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                name="example.com",
                type="TLSA",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_update_overload_21(self, client: Cloudflare) -> None:
        record = client.dns.records.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="URI",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_update_with_all_params_overload_21(self, client: Cloudflare) -> None:
        record = client.dns.records.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="URI",
            comment="Domain verification record",
            data={
                "target": "http://example.com/example.html",
                "weight": 20,
            },
            priority=10,
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_update_overload_21(self, client: Cloudflare) -> None:
        response = client.dns.records.with_raw_response.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="URI",
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
            name="example.com",
            type="URI",
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
                name="example.com",
                type="URI",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_record_id` but received ''"):
            client.dns.records.with_raw_response.update(
                dns_record_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                name="example.com",
                type="URI",
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
                    "name": "example.com",
                    "type": "A",
                    "comment": "Domain verification record",
                    "content": "198.51.100.4",
                    "proxied": True,
                    "settings": {
                        "ipv4_only": True,
                        "ipv6_only": True,
                    },
                    "tags": ["owner:dns-team"],
                    "ttl": 3600,
                    "id": "023e105f4ecef8ad9ca31a8372d0c353",
                }
            ],
            posts=[
                {
                    "name": "example.com",
                    "type": "A",
                    "comment": "Domain verification record",
                    "content": "198.51.100.4",
                    "proxied": True,
                    "settings": {
                        "ipv4_only": True,
                        "ipv6_only": True,
                    },
                    "tags": ["owner:dns-team"],
                    "ttl": 3600,
                }
            ],
            puts=[
                {
                    "name": "example.com",
                    "type": "A",
                    "comment": "Domain verification record",
                    "content": "198.51.100.4",
                    "proxied": True,
                    "settings": {
                        "ipv4_only": True,
                        "ipv6_only": True,
                    },
                    "tags": ["owner:dns-team"],
                    "ttl": 3600,
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
            name="example.com",
            type="A",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_edit_with_all_params_overload_1(self, client: Cloudflare) -> None:
        record = client.dns.records.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="A",
            comment="Domain verification record",
            content="198.51.100.4",
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_edit_overload_1(self, client: Cloudflare) -> None:
        response = client.dns.records.with_raw_response.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="A",
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
            name="example.com",
            type="A",
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
                name="example.com",
                type="A",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_record_id` but received ''"):
            client.dns.records.with_raw_response.edit(
                dns_record_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                name="example.com",
                type="A",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_edit_overload_2(self, client: Cloudflare) -> None:
        record = client.dns.records.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="AAAA",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_edit_with_all_params_overload_2(self, client: Cloudflare) -> None:
        record = client.dns.records.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="AAAA",
            comment="Domain verification record",
            content="2400:cb00:2049::1",
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_edit_overload_2(self, client: Cloudflare) -> None:
        response = client.dns.records.with_raw_response.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="AAAA",
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
            name="example.com",
            type="AAAA",
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
                name="example.com",
                type="AAAA",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_record_id` but received ''"):
            client.dns.records.with_raw_response.edit(
                dns_record_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                name="example.com",
                type="AAAA",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_edit_overload_3(self, client: Cloudflare) -> None:
        record = client.dns.records.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="CNAME",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_edit_with_all_params_overload_3(self, client: Cloudflare) -> None:
        record = client.dns.records.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="CNAME",
            comment="Domain verification record",
            content="content",
            proxied=True,
            settings={
                "flatten_cname": True,
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_edit_overload_3(self, client: Cloudflare) -> None:
        response = client.dns.records.with_raw_response.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="CNAME",
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
            name="example.com",
            type="CNAME",
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
                name="example.com",
                type="CNAME",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_record_id` but received ''"):
            client.dns.records.with_raw_response.edit(
                dns_record_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                name="example.com",
                type="CNAME",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_edit_overload_4(self, client: Cloudflare) -> None:
        record = client.dns.records.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="MX",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_edit_with_all_params_overload_4(self, client: Cloudflare) -> None:
        record = client.dns.records.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="MX",
            comment="Domain verification record",
            content="mx.example.com",
            priority=10,
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_edit_overload_4(self, client: Cloudflare) -> None:
        response = client.dns.records.with_raw_response.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="MX",
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
            name="example.com",
            type="MX",
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
                name="example.com",
                type="MX",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_record_id` but received ''"):
            client.dns.records.with_raw_response.edit(
                dns_record_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                name="example.com",
                type="MX",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_edit_overload_5(self, client: Cloudflare) -> None:
        record = client.dns.records.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="NS",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_edit_with_all_params_overload_5(self, client: Cloudflare) -> None:
        record = client.dns.records.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="NS",
            comment="Domain verification record",
            content="ns1.example.com",
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_edit_overload_5(self, client: Cloudflare) -> None:
        response = client.dns.records.with_raw_response.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="NS",
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
            name="example.com",
            type="NS",
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
                name="example.com",
                type="NS",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_record_id` but received ''"):
            client.dns.records.with_raw_response.edit(
                dns_record_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                name="example.com",
                type="NS",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_edit_overload_6(self, client: Cloudflare) -> None:
        record = client.dns.records.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="OPENPGPKEY",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_edit_with_all_params_overload_6(self, client: Cloudflare) -> None:
        record = client.dns.records.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="OPENPGPKEY",
            comment="Domain verification record",
            content="content",
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_edit_overload_6(self, client: Cloudflare) -> None:
        response = client.dns.records.with_raw_response.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="OPENPGPKEY",
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
            name="example.com",
            type="OPENPGPKEY",
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
                name="example.com",
                type="OPENPGPKEY",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_record_id` but received ''"):
            client.dns.records.with_raw_response.edit(
                dns_record_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                name="example.com",
                type="OPENPGPKEY",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_edit_overload_7(self, client: Cloudflare) -> None:
        record = client.dns.records.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="PTR",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_edit_with_all_params_overload_7(self, client: Cloudflare) -> None:
        record = client.dns.records.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="PTR",
            comment="Domain verification record",
            content="example.com",
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_edit_overload_7(self, client: Cloudflare) -> None:
        response = client.dns.records.with_raw_response.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="PTR",
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
            name="example.com",
            type="PTR",
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
                name="example.com",
                type="PTR",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_record_id` but received ''"):
            client.dns.records.with_raw_response.edit(
                dns_record_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                name="example.com",
                type="PTR",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_edit_overload_8(self, client: Cloudflare) -> None:
        record = client.dns.records.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="TXT",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_edit_with_all_params_overload_8(self, client: Cloudflare) -> None:
        record = client.dns.records.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="TXT",
            comment="Domain verification record",
            content='"v=spf1 include:example.com -all"',
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_edit_overload_8(self, client: Cloudflare) -> None:
        response = client.dns.records.with_raw_response.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="TXT",
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
            name="example.com",
            type="TXT",
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
                name="example.com",
                type="TXT",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_record_id` but received ''"):
            client.dns.records.with_raw_response.edit(
                dns_record_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                name="example.com",
                type="TXT",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_edit_overload_9(self, client: Cloudflare) -> None:
        record = client.dns.records.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="CAA",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_edit_with_all_params_overload_9(self, client: Cloudflare) -> None:
        record = client.dns.records.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="CAA",
            comment="Domain verification record",
            data={
                "flags": 1,
                "tag": "issue",
                "value": "value",
            },
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_edit_overload_9(self, client: Cloudflare) -> None:
        response = client.dns.records.with_raw_response.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="CAA",
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
            name="example.com",
            type="CAA",
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
                name="example.com",
                type="CAA",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_record_id` but received ''"):
            client.dns.records.with_raw_response.edit(
                dns_record_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                name="example.com",
                type="CAA",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_edit_overload_10(self, client: Cloudflare) -> None:
        record = client.dns.records.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="CERT",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_edit_with_all_params_overload_10(self, client: Cloudflare) -> None:
        record = client.dns.records.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="CERT",
            comment="Domain verification record",
            data={
                "algorithm": 8,
                "certificate": "certificate",
                "key_tag": 1,
                "type": 9,
            },
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_edit_overload_10(self, client: Cloudflare) -> None:
        response = client.dns.records.with_raw_response.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="CERT",
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
            name="example.com",
            type="CERT",
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
                name="example.com",
                type="CERT",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_record_id` but received ''"):
            client.dns.records.with_raw_response.edit(
                dns_record_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                name="example.com",
                type="CERT",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_edit_overload_11(self, client: Cloudflare) -> None:
        record = client.dns.records.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="DNSKEY",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_edit_with_all_params_overload_11(self, client: Cloudflare) -> None:
        record = client.dns.records.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="DNSKEY",
            comment="Domain verification record",
            data={
                "algorithm": 5,
                "flags": 1,
                "protocol": 3,
                "public_key": "public_key",
            },
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_edit_overload_11(self, client: Cloudflare) -> None:
        response = client.dns.records.with_raw_response.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="DNSKEY",
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
            name="example.com",
            type="DNSKEY",
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
                name="example.com",
                type="DNSKEY",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_record_id` but received ''"):
            client.dns.records.with_raw_response.edit(
                dns_record_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                name="example.com",
                type="DNSKEY",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_edit_overload_12(self, client: Cloudflare) -> None:
        record = client.dns.records.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="DS",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_edit_with_all_params_overload_12(self, client: Cloudflare) -> None:
        record = client.dns.records.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="DS",
            comment="Domain verification record",
            data={
                "algorithm": 3,
                "digest": "digest",
                "digest_type": 1,
                "key_tag": 1,
            },
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_edit_overload_12(self, client: Cloudflare) -> None:
        response = client.dns.records.with_raw_response.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="DS",
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
            name="example.com",
            type="DS",
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
                name="example.com",
                type="DS",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_record_id` but received ''"):
            client.dns.records.with_raw_response.edit(
                dns_record_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                name="example.com",
                type="DS",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_edit_overload_13(self, client: Cloudflare) -> None:
        record = client.dns.records.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="HTTPS",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_edit_with_all_params_overload_13(self, client: Cloudflare) -> None:
        record = client.dns.records.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="HTTPS",
            comment="Domain verification record",
            data={
                "priority": 1,
                "target": ".",
                "value": 'alpn="h3,h2" ipv4hint="127.0.0.1" ipv6hint="::1"',
            },
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_edit_overload_13(self, client: Cloudflare) -> None:
        response = client.dns.records.with_raw_response.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="HTTPS",
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
            name="example.com",
            type="HTTPS",
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
                name="example.com",
                type="HTTPS",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_record_id` but received ''"):
            client.dns.records.with_raw_response.edit(
                dns_record_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                name="example.com",
                type="HTTPS",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_edit_overload_14(self, client: Cloudflare) -> None:
        record = client.dns.records.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="LOC",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_edit_with_all_params_overload_14(self, client: Cloudflare) -> None:
        record = client.dns.records.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="LOC",
            comment="Domain verification record",
            data={
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
            },
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_edit_overload_14(self, client: Cloudflare) -> None:
        response = client.dns.records.with_raw_response.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="LOC",
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
            name="example.com",
            type="LOC",
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
                name="example.com",
                type="LOC",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_record_id` but received ''"):
            client.dns.records.with_raw_response.edit(
                dns_record_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                name="example.com",
                type="LOC",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_edit_overload_15(self, client: Cloudflare) -> None:
        record = client.dns.records.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="NAPTR",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_edit_with_all_params_overload_15(self, client: Cloudflare) -> None:
        record = client.dns.records.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="NAPTR",
            comment="Domain verification record",
            data={
                "flags": "flags",
                "order": 100,
                "preference": 10,
                "regex": "regex",
                "replacement": "replacement",
                "service": "service",
            },
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_edit_overload_15(self, client: Cloudflare) -> None:
        response = client.dns.records.with_raw_response.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="NAPTR",
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
            name="example.com",
            type="NAPTR",
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
                name="example.com",
                type="NAPTR",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_record_id` but received ''"):
            client.dns.records.with_raw_response.edit(
                dns_record_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                name="example.com",
                type="NAPTR",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_edit_overload_16(self, client: Cloudflare) -> None:
        record = client.dns.records.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="SMIMEA",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_edit_with_all_params_overload_16(self, client: Cloudflare) -> None:
        record = client.dns.records.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="SMIMEA",
            comment="Domain verification record",
            data={
                "certificate": "certificate",
                "matching_type": 0,
                "selector": 0,
                "usage": 3,
            },
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_edit_overload_16(self, client: Cloudflare) -> None:
        response = client.dns.records.with_raw_response.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="SMIMEA",
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
            name="example.com",
            type="SMIMEA",
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
                name="example.com",
                type="SMIMEA",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_record_id` but received ''"):
            client.dns.records.with_raw_response.edit(
                dns_record_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                name="example.com",
                type="SMIMEA",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_edit_overload_17(self, client: Cloudflare) -> None:
        record = client.dns.records.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="SRV",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_edit_with_all_params_overload_17(self, client: Cloudflare) -> None:
        record = client.dns.records.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="SRV",
            comment="Domain verification record",
            data={
                "port": 8806,
                "priority": 10,
                "target": "example.com",
                "weight": 5,
            },
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_edit_overload_17(self, client: Cloudflare) -> None:
        response = client.dns.records.with_raw_response.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="SRV",
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
            name="example.com",
            type="SRV",
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
                name="example.com",
                type="SRV",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_record_id` but received ''"):
            client.dns.records.with_raw_response.edit(
                dns_record_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                name="example.com",
                type="SRV",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_edit_overload_18(self, client: Cloudflare) -> None:
        record = client.dns.records.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="SSHFP",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_edit_with_all_params_overload_18(self, client: Cloudflare) -> None:
        record = client.dns.records.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="SSHFP",
            comment="Domain verification record",
            data={
                "algorithm": 2,
                "fingerprint": "fingerprint",
                "type": 1,
            },
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_edit_overload_18(self, client: Cloudflare) -> None:
        response = client.dns.records.with_raw_response.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="SSHFP",
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
            name="example.com",
            type="SSHFP",
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
                name="example.com",
                type="SSHFP",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_record_id` but received ''"):
            client.dns.records.with_raw_response.edit(
                dns_record_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                name="example.com",
                type="SSHFP",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_edit_overload_19(self, client: Cloudflare) -> None:
        record = client.dns.records.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="SVCB",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_edit_with_all_params_overload_19(self, client: Cloudflare) -> None:
        record = client.dns.records.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="SVCB",
            comment="Domain verification record",
            data={
                "priority": 1,
                "target": ".",
                "value": 'alpn="h3,h2" ipv4hint="127.0.0.1" ipv6hint="::1"',
            },
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_edit_overload_19(self, client: Cloudflare) -> None:
        response = client.dns.records.with_raw_response.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="SVCB",
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
            name="example.com",
            type="SVCB",
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
                name="example.com",
                type="SVCB",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_record_id` but received ''"):
            client.dns.records.with_raw_response.edit(
                dns_record_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                name="example.com",
                type="SVCB",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_edit_overload_20(self, client: Cloudflare) -> None:
        record = client.dns.records.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="TLSA",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_edit_with_all_params_overload_20(self, client: Cloudflare) -> None:
        record = client.dns.records.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="TLSA",
            comment="Domain verification record",
            data={
                "certificate": "certificate",
                "matching_type": 1,
                "selector": 0,
                "usage": 0,
            },
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_edit_overload_20(self, client: Cloudflare) -> None:
        response = client.dns.records.with_raw_response.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="TLSA",
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
            name="example.com",
            type="TLSA",
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
                name="example.com",
                type="TLSA",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_record_id` but received ''"):
            client.dns.records.with_raw_response.edit(
                dns_record_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                name="example.com",
                type="TLSA",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_edit_overload_21(self, client: Cloudflare) -> None:
        record = client.dns.records.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="URI",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_edit_with_all_params_overload_21(self, client: Cloudflare) -> None:
        record = client.dns.records.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="URI",
            comment="Domain verification record",
            data={
                "target": "http://example.com/example.html",
                "weight": 20,
            },
            priority=10,
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_edit_overload_21(self, client: Cloudflare) -> None:
        response = client.dns.records.with_raw_response.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="URI",
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
            name="example.com",
            type="URI",
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
                name="example.com",
                type="URI",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_record_id` but received ''"):
            client.dns.records.with_raw_response.edit(
                dns_record_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                name="example.com",
                type="URI",
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
            name="example.com",
            type="A",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_create_with_all_params_overload_1(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="A",
            comment="Domain verification record",
            content="198.51.100.4",
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_create_overload_1(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dns.records.with_raw_response.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="A",
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
            name="example.com",
            type="A",
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
                name="example.com",
                type="A",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_create_overload_2(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="AAAA",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_create_with_all_params_overload_2(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="AAAA",
            comment="Domain verification record",
            content="2400:cb00:2049::1",
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_create_overload_2(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dns.records.with_raw_response.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="AAAA",
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
            name="example.com",
            type="AAAA",
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
                name="example.com",
                type="AAAA",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_create_overload_3(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="CNAME",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_create_with_all_params_overload_3(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="CNAME",
            comment="Domain verification record",
            content="content",
            proxied=True,
            settings={
                "flatten_cname": True,
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_create_overload_3(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dns.records.with_raw_response.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="CNAME",
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
            name="example.com",
            type="CNAME",
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
                name="example.com",
                type="CNAME",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_create_overload_4(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="MX",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_create_with_all_params_overload_4(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="MX",
            comment="Domain verification record",
            content="mx.example.com",
            priority=10,
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_create_overload_4(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dns.records.with_raw_response.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="MX",
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
            name="example.com",
            type="MX",
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
                name="example.com",
                type="MX",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_create_overload_5(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="NS",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_create_with_all_params_overload_5(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="NS",
            comment="Domain verification record",
            content="ns1.example.com",
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_create_overload_5(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dns.records.with_raw_response.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="NS",
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
            name="example.com",
            type="NS",
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
                name="example.com",
                type="NS",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_create_overload_6(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="OPENPGPKEY",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_create_with_all_params_overload_6(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="OPENPGPKEY",
            comment="Domain verification record",
            content="content",
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_create_overload_6(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dns.records.with_raw_response.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="OPENPGPKEY",
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
            name="example.com",
            type="OPENPGPKEY",
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
                name="example.com",
                type="OPENPGPKEY",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_create_overload_7(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="PTR",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_create_with_all_params_overload_7(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="PTR",
            comment="Domain verification record",
            content="example.com",
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_create_overload_7(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dns.records.with_raw_response.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="PTR",
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
            name="example.com",
            type="PTR",
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
                name="example.com",
                type="PTR",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_create_overload_8(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="TXT",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_create_with_all_params_overload_8(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="TXT",
            comment="Domain verification record",
            content='"v=spf1 include:example.com -all"',
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_create_overload_8(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dns.records.with_raw_response.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="TXT",
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
            name="example.com",
            type="TXT",
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
                name="example.com",
                type="TXT",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_create_overload_9(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="CAA",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_create_with_all_params_overload_9(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="CAA",
            comment="Domain verification record",
            data={
                "flags": 1,
                "tag": "issue",
                "value": "value",
            },
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_create_overload_9(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dns.records.with_raw_response.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="CAA",
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
            name="example.com",
            type="CAA",
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
                name="example.com",
                type="CAA",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_create_overload_10(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="CERT",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_create_with_all_params_overload_10(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="CERT",
            comment="Domain verification record",
            data={
                "algorithm": 8,
                "certificate": "certificate",
                "key_tag": 1,
                "type": 9,
            },
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_create_overload_10(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dns.records.with_raw_response.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="CERT",
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
            name="example.com",
            type="CERT",
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
                name="example.com",
                type="CERT",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_create_overload_11(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="DNSKEY",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_create_with_all_params_overload_11(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="DNSKEY",
            comment="Domain verification record",
            data={
                "algorithm": 5,
                "flags": 1,
                "protocol": 3,
                "public_key": "public_key",
            },
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_create_overload_11(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dns.records.with_raw_response.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="DNSKEY",
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
            name="example.com",
            type="DNSKEY",
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
                name="example.com",
                type="DNSKEY",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_create_overload_12(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="DS",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_create_with_all_params_overload_12(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="DS",
            comment="Domain verification record",
            data={
                "algorithm": 3,
                "digest": "digest",
                "digest_type": 1,
                "key_tag": 1,
            },
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_create_overload_12(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dns.records.with_raw_response.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="DS",
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
            name="example.com",
            type="DS",
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
                name="example.com",
                type="DS",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_create_overload_13(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="HTTPS",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_create_with_all_params_overload_13(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="HTTPS",
            comment="Domain verification record",
            data={
                "priority": 1,
                "target": ".",
                "value": 'alpn="h3,h2" ipv4hint="127.0.0.1" ipv6hint="::1"',
            },
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_create_overload_13(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dns.records.with_raw_response.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="HTTPS",
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
            name="example.com",
            type="HTTPS",
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
                name="example.com",
                type="HTTPS",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_create_overload_14(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="LOC",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_create_with_all_params_overload_14(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="LOC",
            comment="Domain verification record",
            data={
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
            },
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_create_overload_14(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dns.records.with_raw_response.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="LOC",
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
            name="example.com",
            type="LOC",
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
                name="example.com",
                type="LOC",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_create_overload_15(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="NAPTR",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_create_with_all_params_overload_15(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="NAPTR",
            comment="Domain verification record",
            data={
                "flags": "flags",
                "order": 100,
                "preference": 10,
                "regex": "regex",
                "replacement": "replacement",
                "service": "service",
            },
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_create_overload_15(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dns.records.with_raw_response.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="NAPTR",
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
            name="example.com",
            type="NAPTR",
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
                name="example.com",
                type="NAPTR",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_create_overload_16(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="SMIMEA",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_create_with_all_params_overload_16(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="SMIMEA",
            comment="Domain verification record",
            data={
                "certificate": "certificate",
                "matching_type": 0,
                "selector": 0,
                "usage": 3,
            },
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_create_overload_16(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dns.records.with_raw_response.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="SMIMEA",
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
            name="example.com",
            type="SMIMEA",
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
                name="example.com",
                type="SMIMEA",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_create_overload_17(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="SRV",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_create_with_all_params_overload_17(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="SRV",
            comment="Domain verification record",
            data={
                "port": 8806,
                "priority": 10,
                "target": "example.com",
                "weight": 5,
            },
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_create_overload_17(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dns.records.with_raw_response.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="SRV",
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
            name="example.com",
            type="SRV",
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
                name="example.com",
                type="SRV",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_create_overload_18(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="SSHFP",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_create_with_all_params_overload_18(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="SSHFP",
            comment="Domain verification record",
            data={
                "algorithm": 2,
                "fingerprint": "fingerprint",
                "type": 1,
            },
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_create_overload_18(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dns.records.with_raw_response.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="SSHFP",
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
            name="example.com",
            type="SSHFP",
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
                name="example.com",
                type="SSHFP",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_create_overload_19(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="SVCB",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_create_with_all_params_overload_19(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="SVCB",
            comment="Domain verification record",
            data={
                "priority": 1,
                "target": ".",
                "value": 'alpn="h3,h2" ipv4hint="127.0.0.1" ipv6hint="::1"',
            },
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_create_overload_19(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dns.records.with_raw_response.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="SVCB",
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
            name="example.com",
            type="SVCB",
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
                name="example.com",
                type="SVCB",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_create_overload_20(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="TLSA",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_create_with_all_params_overload_20(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="TLSA",
            comment="Domain verification record",
            data={
                "certificate": "certificate",
                "matching_type": 1,
                "selector": 0,
                "usage": 0,
            },
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_create_overload_20(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dns.records.with_raw_response.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="TLSA",
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
            name="example.com",
            type="TLSA",
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
                name="example.com",
                type="TLSA",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_create_overload_21(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="URI",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_create_with_all_params_overload_21(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="URI",
            comment="Domain verification record",
            data={
                "target": "http://example.com/example.html",
                "weight": 20,
            },
            priority=10,
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_create_overload_21(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dns.records.with_raw_response.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="URI",
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
            name="example.com",
            type="URI",
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
                name="example.com",
                type="URI",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_update_overload_1(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="A",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_update_with_all_params_overload_1(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="A",
            comment="Domain verification record",
            content="198.51.100.4",
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_update_overload_1(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dns.records.with_raw_response.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="A",
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
            name="example.com",
            type="A",
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
                name="example.com",
                type="A",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_record_id` but received ''"):
            await async_client.dns.records.with_raw_response.update(
                dns_record_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                name="example.com",
                type="A",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_update_overload_2(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="AAAA",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_update_with_all_params_overload_2(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="AAAA",
            comment="Domain verification record",
            content="2400:cb00:2049::1",
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_update_overload_2(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dns.records.with_raw_response.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="AAAA",
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
            name="example.com",
            type="AAAA",
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
                name="example.com",
                type="AAAA",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_record_id` but received ''"):
            await async_client.dns.records.with_raw_response.update(
                dns_record_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                name="example.com",
                type="AAAA",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_update_overload_3(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="CNAME",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_update_with_all_params_overload_3(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="CNAME",
            comment="Domain verification record",
            content="content",
            proxied=True,
            settings={
                "flatten_cname": True,
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_update_overload_3(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dns.records.with_raw_response.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="CNAME",
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
            name="example.com",
            type="CNAME",
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
                name="example.com",
                type="CNAME",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_record_id` but received ''"):
            await async_client.dns.records.with_raw_response.update(
                dns_record_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                name="example.com",
                type="CNAME",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_update_overload_4(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="MX",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_update_with_all_params_overload_4(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="MX",
            comment="Domain verification record",
            content="mx.example.com",
            priority=10,
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_update_overload_4(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dns.records.with_raw_response.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="MX",
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
            name="example.com",
            type="MX",
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
                name="example.com",
                type="MX",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_record_id` but received ''"):
            await async_client.dns.records.with_raw_response.update(
                dns_record_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                name="example.com",
                type="MX",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_update_overload_5(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="NS",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_update_with_all_params_overload_5(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="NS",
            comment="Domain verification record",
            content="ns1.example.com",
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_update_overload_5(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dns.records.with_raw_response.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="NS",
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
            name="example.com",
            type="NS",
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
                name="example.com",
                type="NS",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_record_id` but received ''"):
            await async_client.dns.records.with_raw_response.update(
                dns_record_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                name="example.com",
                type="NS",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_update_overload_6(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="OPENPGPKEY",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_update_with_all_params_overload_6(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="OPENPGPKEY",
            comment="Domain verification record",
            content="content",
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_update_overload_6(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dns.records.with_raw_response.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="OPENPGPKEY",
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
            name="example.com",
            type="OPENPGPKEY",
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
                name="example.com",
                type="OPENPGPKEY",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_record_id` but received ''"):
            await async_client.dns.records.with_raw_response.update(
                dns_record_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                name="example.com",
                type="OPENPGPKEY",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_update_overload_7(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="PTR",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_update_with_all_params_overload_7(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="PTR",
            comment="Domain verification record",
            content="example.com",
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_update_overload_7(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dns.records.with_raw_response.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="PTR",
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
            name="example.com",
            type="PTR",
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
                name="example.com",
                type="PTR",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_record_id` but received ''"):
            await async_client.dns.records.with_raw_response.update(
                dns_record_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                name="example.com",
                type="PTR",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_update_overload_8(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="TXT",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_update_with_all_params_overload_8(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="TXT",
            comment="Domain verification record",
            content='"v=spf1 include:example.com -all"',
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_update_overload_8(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dns.records.with_raw_response.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="TXT",
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
            name="example.com",
            type="TXT",
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
                name="example.com",
                type="TXT",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_record_id` but received ''"):
            await async_client.dns.records.with_raw_response.update(
                dns_record_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                name="example.com",
                type="TXT",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_update_overload_9(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="CAA",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_update_with_all_params_overload_9(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="CAA",
            comment="Domain verification record",
            data={
                "flags": 1,
                "tag": "issue",
                "value": "value",
            },
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_update_overload_9(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dns.records.with_raw_response.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="CAA",
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
            name="example.com",
            type="CAA",
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
                name="example.com",
                type="CAA",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_record_id` but received ''"):
            await async_client.dns.records.with_raw_response.update(
                dns_record_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                name="example.com",
                type="CAA",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_update_overload_10(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="CERT",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_update_with_all_params_overload_10(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="CERT",
            comment="Domain verification record",
            data={
                "algorithm": 8,
                "certificate": "certificate",
                "key_tag": 1,
                "type": 9,
            },
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_update_overload_10(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dns.records.with_raw_response.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="CERT",
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
            name="example.com",
            type="CERT",
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
                name="example.com",
                type="CERT",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_record_id` but received ''"):
            await async_client.dns.records.with_raw_response.update(
                dns_record_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                name="example.com",
                type="CERT",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_update_overload_11(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="DNSKEY",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_update_with_all_params_overload_11(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="DNSKEY",
            comment="Domain verification record",
            data={
                "algorithm": 5,
                "flags": 1,
                "protocol": 3,
                "public_key": "public_key",
            },
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_update_overload_11(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dns.records.with_raw_response.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="DNSKEY",
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
            name="example.com",
            type="DNSKEY",
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
                name="example.com",
                type="DNSKEY",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_record_id` but received ''"):
            await async_client.dns.records.with_raw_response.update(
                dns_record_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                name="example.com",
                type="DNSKEY",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_update_overload_12(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="DS",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_update_with_all_params_overload_12(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="DS",
            comment="Domain verification record",
            data={
                "algorithm": 3,
                "digest": "digest",
                "digest_type": 1,
                "key_tag": 1,
            },
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_update_overload_12(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dns.records.with_raw_response.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="DS",
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
            name="example.com",
            type="DS",
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
                name="example.com",
                type="DS",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_record_id` but received ''"):
            await async_client.dns.records.with_raw_response.update(
                dns_record_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                name="example.com",
                type="DS",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_update_overload_13(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="HTTPS",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_update_with_all_params_overload_13(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="HTTPS",
            comment="Domain verification record",
            data={
                "priority": 1,
                "target": ".",
                "value": 'alpn="h3,h2" ipv4hint="127.0.0.1" ipv6hint="::1"',
            },
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_update_overload_13(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dns.records.with_raw_response.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="HTTPS",
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
            name="example.com",
            type="HTTPS",
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
                name="example.com",
                type="HTTPS",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_record_id` but received ''"):
            await async_client.dns.records.with_raw_response.update(
                dns_record_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                name="example.com",
                type="HTTPS",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_update_overload_14(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="LOC",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_update_with_all_params_overload_14(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="LOC",
            comment="Domain verification record",
            data={
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
            },
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_update_overload_14(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dns.records.with_raw_response.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="LOC",
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
            name="example.com",
            type="LOC",
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
                name="example.com",
                type="LOC",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_record_id` but received ''"):
            await async_client.dns.records.with_raw_response.update(
                dns_record_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                name="example.com",
                type="LOC",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_update_overload_15(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="NAPTR",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_update_with_all_params_overload_15(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="NAPTR",
            comment="Domain verification record",
            data={
                "flags": "flags",
                "order": 100,
                "preference": 10,
                "regex": "regex",
                "replacement": "replacement",
                "service": "service",
            },
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_update_overload_15(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dns.records.with_raw_response.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="NAPTR",
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
            name="example.com",
            type="NAPTR",
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
                name="example.com",
                type="NAPTR",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_record_id` but received ''"):
            await async_client.dns.records.with_raw_response.update(
                dns_record_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                name="example.com",
                type="NAPTR",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_update_overload_16(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="SMIMEA",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_update_with_all_params_overload_16(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="SMIMEA",
            comment="Domain verification record",
            data={
                "certificate": "certificate",
                "matching_type": 0,
                "selector": 0,
                "usage": 3,
            },
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_update_overload_16(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dns.records.with_raw_response.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="SMIMEA",
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
            name="example.com",
            type="SMIMEA",
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
                name="example.com",
                type="SMIMEA",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_record_id` but received ''"):
            await async_client.dns.records.with_raw_response.update(
                dns_record_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                name="example.com",
                type="SMIMEA",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_update_overload_17(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="SRV",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_update_with_all_params_overload_17(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="SRV",
            comment="Domain verification record",
            data={
                "port": 8806,
                "priority": 10,
                "target": "example.com",
                "weight": 5,
            },
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_update_overload_17(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dns.records.with_raw_response.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="SRV",
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
            name="example.com",
            type="SRV",
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
                name="example.com",
                type="SRV",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_record_id` but received ''"):
            await async_client.dns.records.with_raw_response.update(
                dns_record_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                name="example.com",
                type="SRV",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_update_overload_18(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="SSHFP",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_update_with_all_params_overload_18(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="SSHFP",
            comment="Domain verification record",
            data={
                "algorithm": 2,
                "fingerprint": "fingerprint",
                "type": 1,
            },
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_update_overload_18(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dns.records.with_raw_response.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="SSHFP",
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
            name="example.com",
            type="SSHFP",
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
                name="example.com",
                type="SSHFP",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_record_id` but received ''"):
            await async_client.dns.records.with_raw_response.update(
                dns_record_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                name="example.com",
                type="SSHFP",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_update_overload_19(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="SVCB",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_update_with_all_params_overload_19(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="SVCB",
            comment="Domain verification record",
            data={
                "priority": 1,
                "target": ".",
                "value": 'alpn="h3,h2" ipv4hint="127.0.0.1" ipv6hint="::1"',
            },
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_update_overload_19(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dns.records.with_raw_response.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="SVCB",
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
            name="example.com",
            type="SVCB",
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
                name="example.com",
                type="SVCB",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_record_id` but received ''"):
            await async_client.dns.records.with_raw_response.update(
                dns_record_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                name="example.com",
                type="SVCB",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_update_overload_20(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="TLSA",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_update_with_all_params_overload_20(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="TLSA",
            comment="Domain verification record",
            data={
                "certificate": "certificate",
                "matching_type": 1,
                "selector": 0,
                "usage": 0,
            },
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_update_overload_20(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dns.records.with_raw_response.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="TLSA",
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
            name="example.com",
            type="TLSA",
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
                name="example.com",
                type="TLSA",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_record_id` but received ''"):
            await async_client.dns.records.with_raw_response.update(
                dns_record_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                name="example.com",
                type="TLSA",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_update_overload_21(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="URI",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_update_with_all_params_overload_21(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="URI",
            comment="Domain verification record",
            data={
                "target": "http://example.com/example.html",
                "weight": 20,
            },
            priority=10,
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_update_overload_21(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dns.records.with_raw_response.update(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="URI",
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
            name="example.com",
            type="URI",
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
                name="example.com",
                type="URI",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_record_id` but received ''"):
            await async_client.dns.records.with_raw_response.update(
                dns_record_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                name="example.com",
                type="URI",
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
                    "name": "example.com",
                    "type": "A",
                    "comment": "Domain verification record",
                    "content": "198.51.100.4",
                    "proxied": True,
                    "settings": {
                        "ipv4_only": True,
                        "ipv6_only": True,
                    },
                    "tags": ["owner:dns-team"],
                    "ttl": 3600,
                    "id": "023e105f4ecef8ad9ca31a8372d0c353",
                }
            ],
            posts=[
                {
                    "name": "example.com",
                    "type": "A",
                    "comment": "Domain verification record",
                    "content": "198.51.100.4",
                    "proxied": True,
                    "settings": {
                        "ipv4_only": True,
                        "ipv6_only": True,
                    },
                    "tags": ["owner:dns-team"],
                    "ttl": 3600,
                }
            ],
            puts=[
                {
                    "name": "example.com",
                    "type": "A",
                    "comment": "Domain verification record",
                    "content": "198.51.100.4",
                    "proxied": True,
                    "settings": {
                        "ipv4_only": True,
                        "ipv6_only": True,
                    },
                    "tags": ["owner:dns-team"],
                    "ttl": 3600,
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
            name="example.com",
            type="A",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_edit_with_all_params_overload_1(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="A",
            comment="Domain verification record",
            content="198.51.100.4",
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_edit_overload_1(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dns.records.with_raw_response.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="A",
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
            name="example.com",
            type="A",
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
                name="example.com",
                type="A",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_record_id` but received ''"):
            await async_client.dns.records.with_raw_response.edit(
                dns_record_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                name="example.com",
                type="A",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_edit_overload_2(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="AAAA",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_edit_with_all_params_overload_2(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="AAAA",
            comment="Domain verification record",
            content="2400:cb00:2049::1",
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_edit_overload_2(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dns.records.with_raw_response.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="AAAA",
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
            name="example.com",
            type="AAAA",
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
                name="example.com",
                type="AAAA",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_record_id` but received ''"):
            await async_client.dns.records.with_raw_response.edit(
                dns_record_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                name="example.com",
                type="AAAA",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_edit_overload_3(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="CNAME",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_edit_with_all_params_overload_3(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="CNAME",
            comment="Domain verification record",
            content="content",
            proxied=True,
            settings={
                "flatten_cname": True,
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_edit_overload_3(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dns.records.with_raw_response.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="CNAME",
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
            name="example.com",
            type="CNAME",
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
                name="example.com",
                type="CNAME",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_record_id` but received ''"):
            await async_client.dns.records.with_raw_response.edit(
                dns_record_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                name="example.com",
                type="CNAME",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_edit_overload_4(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="MX",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_edit_with_all_params_overload_4(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="MX",
            comment="Domain verification record",
            content="mx.example.com",
            priority=10,
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_edit_overload_4(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dns.records.with_raw_response.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="MX",
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
            name="example.com",
            type="MX",
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
                name="example.com",
                type="MX",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_record_id` but received ''"):
            await async_client.dns.records.with_raw_response.edit(
                dns_record_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                name="example.com",
                type="MX",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_edit_overload_5(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="NS",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_edit_with_all_params_overload_5(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="NS",
            comment="Domain verification record",
            content="ns1.example.com",
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_edit_overload_5(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dns.records.with_raw_response.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="NS",
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
            name="example.com",
            type="NS",
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
                name="example.com",
                type="NS",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_record_id` but received ''"):
            await async_client.dns.records.with_raw_response.edit(
                dns_record_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                name="example.com",
                type="NS",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_edit_overload_6(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="OPENPGPKEY",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_edit_with_all_params_overload_6(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="OPENPGPKEY",
            comment="Domain verification record",
            content="content",
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_edit_overload_6(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dns.records.with_raw_response.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="OPENPGPKEY",
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
            name="example.com",
            type="OPENPGPKEY",
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
                name="example.com",
                type="OPENPGPKEY",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_record_id` but received ''"):
            await async_client.dns.records.with_raw_response.edit(
                dns_record_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                name="example.com",
                type="OPENPGPKEY",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_edit_overload_7(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="PTR",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_edit_with_all_params_overload_7(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="PTR",
            comment="Domain verification record",
            content="example.com",
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_edit_overload_7(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dns.records.with_raw_response.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="PTR",
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
            name="example.com",
            type="PTR",
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
                name="example.com",
                type="PTR",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_record_id` but received ''"):
            await async_client.dns.records.with_raw_response.edit(
                dns_record_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                name="example.com",
                type="PTR",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_edit_overload_8(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="TXT",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_edit_with_all_params_overload_8(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="TXT",
            comment="Domain verification record",
            content='"v=spf1 include:example.com -all"',
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_edit_overload_8(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dns.records.with_raw_response.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="TXT",
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
            name="example.com",
            type="TXT",
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
                name="example.com",
                type="TXT",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_record_id` but received ''"):
            await async_client.dns.records.with_raw_response.edit(
                dns_record_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                name="example.com",
                type="TXT",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_edit_overload_9(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="CAA",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_edit_with_all_params_overload_9(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="CAA",
            comment="Domain verification record",
            data={
                "flags": 1,
                "tag": "issue",
                "value": "value",
            },
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_edit_overload_9(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dns.records.with_raw_response.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="CAA",
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
            name="example.com",
            type="CAA",
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
                name="example.com",
                type="CAA",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_record_id` but received ''"):
            await async_client.dns.records.with_raw_response.edit(
                dns_record_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                name="example.com",
                type="CAA",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_edit_overload_10(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="CERT",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_edit_with_all_params_overload_10(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="CERT",
            comment="Domain verification record",
            data={
                "algorithm": 8,
                "certificate": "certificate",
                "key_tag": 1,
                "type": 9,
            },
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_edit_overload_10(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dns.records.with_raw_response.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="CERT",
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
            name="example.com",
            type="CERT",
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
                name="example.com",
                type="CERT",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_record_id` but received ''"):
            await async_client.dns.records.with_raw_response.edit(
                dns_record_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                name="example.com",
                type="CERT",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_edit_overload_11(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="DNSKEY",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_edit_with_all_params_overload_11(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="DNSKEY",
            comment="Domain verification record",
            data={
                "algorithm": 5,
                "flags": 1,
                "protocol": 3,
                "public_key": "public_key",
            },
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_edit_overload_11(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dns.records.with_raw_response.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="DNSKEY",
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
            name="example.com",
            type="DNSKEY",
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
                name="example.com",
                type="DNSKEY",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_record_id` but received ''"):
            await async_client.dns.records.with_raw_response.edit(
                dns_record_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                name="example.com",
                type="DNSKEY",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_edit_overload_12(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="DS",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_edit_with_all_params_overload_12(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="DS",
            comment="Domain verification record",
            data={
                "algorithm": 3,
                "digest": "digest",
                "digest_type": 1,
                "key_tag": 1,
            },
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_edit_overload_12(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dns.records.with_raw_response.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="DS",
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
            name="example.com",
            type="DS",
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
                name="example.com",
                type="DS",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_record_id` but received ''"):
            await async_client.dns.records.with_raw_response.edit(
                dns_record_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                name="example.com",
                type="DS",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_edit_overload_13(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="HTTPS",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_edit_with_all_params_overload_13(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="HTTPS",
            comment="Domain verification record",
            data={
                "priority": 1,
                "target": ".",
                "value": 'alpn="h3,h2" ipv4hint="127.0.0.1" ipv6hint="::1"',
            },
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_edit_overload_13(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dns.records.with_raw_response.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="HTTPS",
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
            name="example.com",
            type="HTTPS",
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
                name="example.com",
                type="HTTPS",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_record_id` but received ''"):
            await async_client.dns.records.with_raw_response.edit(
                dns_record_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                name="example.com",
                type="HTTPS",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_edit_overload_14(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="LOC",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_edit_with_all_params_overload_14(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="LOC",
            comment="Domain verification record",
            data={
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
            },
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_edit_overload_14(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dns.records.with_raw_response.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="LOC",
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
            name="example.com",
            type="LOC",
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
                name="example.com",
                type="LOC",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_record_id` but received ''"):
            await async_client.dns.records.with_raw_response.edit(
                dns_record_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                name="example.com",
                type="LOC",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_edit_overload_15(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="NAPTR",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_edit_with_all_params_overload_15(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="NAPTR",
            comment="Domain verification record",
            data={
                "flags": "flags",
                "order": 100,
                "preference": 10,
                "regex": "regex",
                "replacement": "replacement",
                "service": "service",
            },
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_edit_overload_15(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dns.records.with_raw_response.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="NAPTR",
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
            name="example.com",
            type="NAPTR",
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
                name="example.com",
                type="NAPTR",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_record_id` but received ''"):
            await async_client.dns.records.with_raw_response.edit(
                dns_record_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                name="example.com",
                type="NAPTR",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_edit_overload_16(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="SMIMEA",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_edit_with_all_params_overload_16(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="SMIMEA",
            comment="Domain verification record",
            data={
                "certificate": "certificate",
                "matching_type": 0,
                "selector": 0,
                "usage": 3,
            },
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_edit_overload_16(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dns.records.with_raw_response.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="SMIMEA",
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
            name="example.com",
            type="SMIMEA",
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
                name="example.com",
                type="SMIMEA",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_record_id` but received ''"):
            await async_client.dns.records.with_raw_response.edit(
                dns_record_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                name="example.com",
                type="SMIMEA",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_edit_overload_17(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="SRV",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_edit_with_all_params_overload_17(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="SRV",
            comment="Domain verification record",
            data={
                "port": 8806,
                "priority": 10,
                "target": "example.com",
                "weight": 5,
            },
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_edit_overload_17(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dns.records.with_raw_response.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="SRV",
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
            name="example.com",
            type="SRV",
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
                name="example.com",
                type="SRV",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_record_id` but received ''"):
            await async_client.dns.records.with_raw_response.edit(
                dns_record_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                name="example.com",
                type="SRV",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_edit_overload_18(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="SSHFP",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_edit_with_all_params_overload_18(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="SSHFP",
            comment="Domain verification record",
            data={
                "algorithm": 2,
                "fingerprint": "fingerprint",
                "type": 1,
            },
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_edit_overload_18(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dns.records.with_raw_response.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="SSHFP",
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
            name="example.com",
            type="SSHFP",
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
                name="example.com",
                type="SSHFP",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_record_id` but received ''"):
            await async_client.dns.records.with_raw_response.edit(
                dns_record_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                name="example.com",
                type="SSHFP",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_edit_overload_19(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="SVCB",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_edit_with_all_params_overload_19(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="SVCB",
            comment="Domain verification record",
            data={
                "priority": 1,
                "target": ".",
                "value": 'alpn="h3,h2" ipv4hint="127.0.0.1" ipv6hint="::1"',
            },
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_edit_overload_19(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dns.records.with_raw_response.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="SVCB",
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
            name="example.com",
            type="SVCB",
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
                name="example.com",
                type="SVCB",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_record_id` but received ''"):
            await async_client.dns.records.with_raw_response.edit(
                dns_record_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                name="example.com",
                type="SVCB",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_edit_overload_20(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="TLSA",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_edit_with_all_params_overload_20(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="TLSA",
            comment="Domain verification record",
            data={
                "certificate": "certificate",
                "matching_type": 1,
                "selector": 0,
                "usage": 0,
            },
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_edit_overload_20(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dns.records.with_raw_response.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="TLSA",
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
            name="example.com",
            type="TLSA",
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
                name="example.com",
                type="TLSA",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_record_id` but received ''"):
            await async_client.dns.records.with_raw_response.edit(
                dns_record_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                name="example.com",
                type="TLSA",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_edit_overload_21(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="URI",
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_edit_with_all_params_overload_21(self, async_client: AsyncCloudflare) -> None:
        record = await async_client.dns.records.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="URI",
            comment="Domain verification record",
            data={
                "target": "http://example.com/example.html",
                "weight": 20,
            },
            priority=10,
            proxied=True,
            settings={
                "ipv4_only": True,
                "ipv6_only": True,
            },
            tags=["owner:dns-team"],
            ttl=3600,
        )
        assert_matches_type(Optional[RecordResponse], record, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_edit_overload_21(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dns.records.with_raw_response.edit(
            dns_record_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="example.com",
            type="URI",
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
            name="example.com",
            type="URI",
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
                name="example.com",
                type="URI",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_record_id` but received ''"):
            await async_client.dns.records.with_raw_response.edit(
                dns_record_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                name="example.com",
                type="URI",
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
