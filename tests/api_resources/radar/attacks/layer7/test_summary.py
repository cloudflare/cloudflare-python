# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare._utils import parse_datetime
from cloudflare.types.radar.attacks.layer7 import (
    SummaryIPVersionResponse,
    SummaryHTTPMethodResponse,
    SummaryHTTPVersionResponse,
    SummaryManagedRulesResponse,
    SummaryMitigationProductResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSummary:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_http_method(self, client: Cloudflare) -> None:
        summary = client.radar.attacks.layer7.summary.http_method()
        assert_matches_type(SummaryHTTPMethodResponse, summary, path=["response"])

    @parametrize
    def test_method_http_method_with_all_params(self, client: Cloudflare) -> None:
        summary = client.radar.attacks.layer7.summary.http_method(
            asn=["string"],
            continent=["string"],
            date_end=[parse_datetime("2019-12-27T18:11:19.117Z")],
            date_range=["7d"],
            date_start=[parse_datetime("2019-12-27T18:11:19.117Z")],
            format="JSON",
            http_version=["HTTPv1"],
            ip_version=["IPv4"],
            limit_per_group=10,
            location=["string"],
            mitigation_product=["DDOS"],
            name=["main_series"],
        )
        assert_matches_type(SummaryHTTPMethodResponse, summary, path=["response"])

    @parametrize
    def test_raw_response_http_method(self, client: Cloudflare) -> None:
        response = client.radar.attacks.layer7.summary.with_raw_response.http_method()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        summary = response.parse()
        assert_matches_type(SummaryHTTPMethodResponse, summary, path=["response"])

    @parametrize
    def test_streaming_response_http_method(self, client: Cloudflare) -> None:
        with client.radar.attacks.layer7.summary.with_streaming_response.http_method() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            summary = response.parse()
            assert_matches_type(SummaryHTTPMethodResponse, summary, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_http_version(self, client: Cloudflare) -> None:
        summary = client.radar.attacks.layer7.summary.http_version()
        assert_matches_type(SummaryHTTPVersionResponse, summary, path=["response"])

    @parametrize
    def test_method_http_version_with_all_params(self, client: Cloudflare) -> None:
        summary = client.radar.attacks.layer7.summary.http_version(
            asn=["string"],
            continent=["string"],
            date_end=[parse_datetime("2019-12-27T18:11:19.117Z")],
            date_range=["7d"],
            date_start=[parse_datetime("2019-12-27T18:11:19.117Z")],
            format="JSON",
            http_method=["GET"],
            ip_version=["IPv4"],
            location=["string"],
            mitigation_product=["DDOS"],
            name=["main_series"],
        )
        assert_matches_type(SummaryHTTPVersionResponse, summary, path=["response"])

    @parametrize
    def test_raw_response_http_version(self, client: Cloudflare) -> None:
        response = client.radar.attacks.layer7.summary.with_raw_response.http_version()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        summary = response.parse()
        assert_matches_type(SummaryHTTPVersionResponse, summary, path=["response"])

    @parametrize
    def test_streaming_response_http_version(self, client: Cloudflare) -> None:
        with client.radar.attacks.layer7.summary.with_streaming_response.http_version() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            summary = response.parse()
            assert_matches_type(SummaryHTTPVersionResponse, summary, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_ip_version(self, client: Cloudflare) -> None:
        summary = client.radar.attacks.layer7.summary.ip_version()
        assert_matches_type(SummaryIPVersionResponse, summary, path=["response"])

    @parametrize
    def test_method_ip_version_with_all_params(self, client: Cloudflare) -> None:
        summary = client.radar.attacks.layer7.summary.ip_version(
            asn=["string"],
            continent=["string"],
            date_end=[parse_datetime("2019-12-27T18:11:19.117Z")],
            date_range=["7d"],
            date_start=[parse_datetime("2019-12-27T18:11:19.117Z")],
            format="JSON",
            http_method=["GET"],
            http_version=["HTTPv1"],
            location=["string"],
            mitigation_product=["DDOS"],
            name=["main_series"],
        )
        assert_matches_type(SummaryIPVersionResponse, summary, path=["response"])

    @parametrize
    def test_raw_response_ip_version(self, client: Cloudflare) -> None:
        response = client.radar.attacks.layer7.summary.with_raw_response.ip_version()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        summary = response.parse()
        assert_matches_type(SummaryIPVersionResponse, summary, path=["response"])

    @parametrize
    def test_streaming_response_ip_version(self, client: Cloudflare) -> None:
        with client.radar.attacks.layer7.summary.with_streaming_response.ip_version() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            summary = response.parse()
            assert_matches_type(SummaryIPVersionResponse, summary, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_managed_rules(self, client: Cloudflare) -> None:
        summary = client.radar.attacks.layer7.summary.managed_rules()
        assert_matches_type(SummaryManagedRulesResponse, summary, path=["response"])

    @parametrize
    def test_method_managed_rules_with_all_params(self, client: Cloudflare) -> None:
        summary = client.radar.attacks.layer7.summary.managed_rules(
            asn=["string"],
            continent=["string"],
            date_end=[parse_datetime("2019-12-27T18:11:19.117Z")],
            date_range=["7d"],
            date_start=[parse_datetime("2019-12-27T18:11:19.117Z")],
            format="JSON",
            http_method=["GET"],
            http_version=["HTTPv1"],
            ip_version=["IPv4"],
            limit_per_group=10,
            location=["string"],
            mitigation_product=["DDOS"],
            name=["main_series"],
        )
        assert_matches_type(SummaryManagedRulesResponse, summary, path=["response"])

    @parametrize
    def test_raw_response_managed_rules(self, client: Cloudflare) -> None:
        response = client.radar.attacks.layer7.summary.with_raw_response.managed_rules()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        summary = response.parse()
        assert_matches_type(SummaryManagedRulesResponse, summary, path=["response"])

    @parametrize
    def test_streaming_response_managed_rules(self, client: Cloudflare) -> None:
        with client.radar.attacks.layer7.summary.with_streaming_response.managed_rules() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            summary = response.parse()
            assert_matches_type(SummaryManagedRulesResponse, summary, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_mitigation_product(self, client: Cloudflare) -> None:
        summary = client.radar.attacks.layer7.summary.mitigation_product()
        assert_matches_type(SummaryMitigationProductResponse, summary, path=["response"])

    @parametrize
    def test_method_mitigation_product_with_all_params(self, client: Cloudflare) -> None:
        summary = client.radar.attacks.layer7.summary.mitigation_product(
            asn=["string"],
            continent=["string"],
            date_end=[parse_datetime("2019-12-27T18:11:19.117Z")],
            date_range=["7d"],
            date_start=[parse_datetime("2019-12-27T18:11:19.117Z")],
            format="JSON",
            http_method=["GET"],
            http_version=["HTTPv1"],
            ip_version=["IPv4"],
            limit_per_group=10,
            location=["string"],
            name=["main_series"],
        )
        assert_matches_type(SummaryMitigationProductResponse, summary, path=["response"])

    @parametrize
    def test_raw_response_mitigation_product(self, client: Cloudflare) -> None:
        response = client.radar.attacks.layer7.summary.with_raw_response.mitigation_product()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        summary = response.parse()
        assert_matches_type(SummaryMitigationProductResponse, summary, path=["response"])

    @parametrize
    def test_streaming_response_mitigation_product(self, client: Cloudflare) -> None:
        with client.radar.attacks.layer7.summary.with_streaming_response.mitigation_product() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            summary = response.parse()
            assert_matches_type(SummaryMitigationProductResponse, summary, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncSummary:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_http_method(self, async_client: AsyncCloudflare) -> None:
        summary = await async_client.radar.attacks.layer7.summary.http_method()
        assert_matches_type(SummaryHTTPMethodResponse, summary, path=["response"])

    @parametrize
    async def test_method_http_method_with_all_params(self, async_client: AsyncCloudflare) -> None:
        summary = await async_client.radar.attacks.layer7.summary.http_method(
            asn=["string"],
            continent=["string"],
            date_end=[parse_datetime("2019-12-27T18:11:19.117Z")],
            date_range=["7d"],
            date_start=[parse_datetime("2019-12-27T18:11:19.117Z")],
            format="JSON",
            http_version=["HTTPv1"],
            ip_version=["IPv4"],
            limit_per_group=10,
            location=["string"],
            mitigation_product=["DDOS"],
            name=["main_series"],
        )
        assert_matches_type(SummaryHTTPMethodResponse, summary, path=["response"])

    @parametrize
    async def test_raw_response_http_method(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.radar.attacks.layer7.summary.with_raw_response.http_method()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        summary = await response.parse()
        assert_matches_type(SummaryHTTPMethodResponse, summary, path=["response"])

    @parametrize
    async def test_streaming_response_http_method(self, async_client: AsyncCloudflare) -> None:
        async with async_client.radar.attacks.layer7.summary.with_streaming_response.http_method() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            summary = await response.parse()
            assert_matches_type(SummaryHTTPMethodResponse, summary, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_http_version(self, async_client: AsyncCloudflare) -> None:
        summary = await async_client.radar.attacks.layer7.summary.http_version()
        assert_matches_type(SummaryHTTPVersionResponse, summary, path=["response"])

    @parametrize
    async def test_method_http_version_with_all_params(self, async_client: AsyncCloudflare) -> None:
        summary = await async_client.radar.attacks.layer7.summary.http_version(
            asn=["string"],
            continent=["string"],
            date_end=[parse_datetime("2019-12-27T18:11:19.117Z")],
            date_range=["7d"],
            date_start=[parse_datetime("2019-12-27T18:11:19.117Z")],
            format="JSON",
            http_method=["GET"],
            ip_version=["IPv4"],
            location=["string"],
            mitigation_product=["DDOS"],
            name=["main_series"],
        )
        assert_matches_type(SummaryHTTPVersionResponse, summary, path=["response"])

    @parametrize
    async def test_raw_response_http_version(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.radar.attacks.layer7.summary.with_raw_response.http_version()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        summary = await response.parse()
        assert_matches_type(SummaryHTTPVersionResponse, summary, path=["response"])

    @parametrize
    async def test_streaming_response_http_version(self, async_client: AsyncCloudflare) -> None:
        async with async_client.radar.attacks.layer7.summary.with_streaming_response.http_version() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            summary = await response.parse()
            assert_matches_type(SummaryHTTPVersionResponse, summary, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_ip_version(self, async_client: AsyncCloudflare) -> None:
        summary = await async_client.radar.attacks.layer7.summary.ip_version()
        assert_matches_type(SummaryIPVersionResponse, summary, path=["response"])

    @parametrize
    async def test_method_ip_version_with_all_params(self, async_client: AsyncCloudflare) -> None:
        summary = await async_client.radar.attacks.layer7.summary.ip_version(
            asn=["string"],
            continent=["string"],
            date_end=[parse_datetime("2019-12-27T18:11:19.117Z")],
            date_range=["7d"],
            date_start=[parse_datetime("2019-12-27T18:11:19.117Z")],
            format="JSON",
            http_method=["GET"],
            http_version=["HTTPv1"],
            location=["string"],
            mitigation_product=["DDOS"],
            name=["main_series"],
        )
        assert_matches_type(SummaryIPVersionResponse, summary, path=["response"])

    @parametrize
    async def test_raw_response_ip_version(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.radar.attacks.layer7.summary.with_raw_response.ip_version()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        summary = await response.parse()
        assert_matches_type(SummaryIPVersionResponse, summary, path=["response"])

    @parametrize
    async def test_streaming_response_ip_version(self, async_client: AsyncCloudflare) -> None:
        async with async_client.radar.attacks.layer7.summary.with_streaming_response.ip_version() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            summary = await response.parse()
            assert_matches_type(SummaryIPVersionResponse, summary, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_managed_rules(self, async_client: AsyncCloudflare) -> None:
        summary = await async_client.radar.attacks.layer7.summary.managed_rules()
        assert_matches_type(SummaryManagedRulesResponse, summary, path=["response"])

    @parametrize
    async def test_method_managed_rules_with_all_params(self, async_client: AsyncCloudflare) -> None:
        summary = await async_client.radar.attacks.layer7.summary.managed_rules(
            asn=["string"],
            continent=["string"],
            date_end=[parse_datetime("2019-12-27T18:11:19.117Z")],
            date_range=["7d"],
            date_start=[parse_datetime("2019-12-27T18:11:19.117Z")],
            format="JSON",
            http_method=["GET"],
            http_version=["HTTPv1"],
            ip_version=["IPv4"],
            limit_per_group=10,
            location=["string"],
            mitigation_product=["DDOS"],
            name=["main_series"],
        )
        assert_matches_type(SummaryManagedRulesResponse, summary, path=["response"])

    @parametrize
    async def test_raw_response_managed_rules(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.radar.attacks.layer7.summary.with_raw_response.managed_rules()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        summary = await response.parse()
        assert_matches_type(SummaryManagedRulesResponse, summary, path=["response"])

    @parametrize
    async def test_streaming_response_managed_rules(self, async_client: AsyncCloudflare) -> None:
        async with async_client.radar.attacks.layer7.summary.with_streaming_response.managed_rules() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            summary = await response.parse()
            assert_matches_type(SummaryManagedRulesResponse, summary, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_mitigation_product(self, async_client: AsyncCloudflare) -> None:
        summary = await async_client.radar.attacks.layer7.summary.mitigation_product()
        assert_matches_type(SummaryMitigationProductResponse, summary, path=["response"])

    @parametrize
    async def test_method_mitigation_product_with_all_params(self, async_client: AsyncCloudflare) -> None:
        summary = await async_client.radar.attacks.layer7.summary.mitigation_product(
            asn=["string"],
            continent=["string"],
            date_end=[parse_datetime("2019-12-27T18:11:19.117Z")],
            date_range=["7d"],
            date_start=[parse_datetime("2019-12-27T18:11:19.117Z")],
            format="JSON",
            http_method=["GET"],
            http_version=["HTTPv1"],
            ip_version=["IPv4"],
            limit_per_group=10,
            location=["string"],
            name=["main_series"],
        )
        assert_matches_type(SummaryMitigationProductResponse, summary, path=["response"])

    @parametrize
    async def test_raw_response_mitigation_product(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.radar.attacks.layer7.summary.with_raw_response.mitigation_product()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        summary = await response.parse()
        assert_matches_type(SummaryMitigationProductResponse, summary, path=["response"])

    @parametrize
    async def test_streaming_response_mitigation_product(self, async_client: AsyncCloudflare) -> None:
        async with async_client.radar.attacks.layer7.summary.with_streaming_response.mitigation_product() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            summary = await response.parse()
            assert_matches_type(SummaryMitigationProductResponse, summary, path=["response"])

        assert cast(Any, response.is_closed) is True
