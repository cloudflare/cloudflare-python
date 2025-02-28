# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare._utils import parse_datetime
from cloudflare.types.radar.dns import (
    SummaryDNSSECResponse,
    SummaryCacheHitResponse,
    SummaryProtocolResponse,
    SummaryDNSSECE2EResponse,
    SummaryIPVersionResponse,
    SummaryQueryTypeResponse,
    SummaryDNSSECAwareResponse,
    SummaryResponseTTLResponse,
    SummaryResponseCodeResponse,
    SummaryMatchingAnswerResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSummary:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_cache_hit(self, client: Cloudflare) -> None:
        summary = client.radar.dns.summary.cache_hit()
        assert_matches_type(SummaryCacheHitResponse, summary, path=["response"])

    @parametrize
    def test_method_cache_hit_with_all_params(self, client: Cloudflare) -> None:
        summary = client.radar.dns.summary.cache_hit(
            asn=["string"],
            continent=["string"],
            date_end=[parse_datetime("2019-12-27T18:11:19.117Z")],
            date_range=["7d"],
            date_start=[parse_datetime("2019-12-27T18:11:19.117Z")],
            format="JSON",
            location=["string"],
            name=["main_series"],
            nodata=True,
            protocol="UDP",
            query_type="A",
            response_code="NOERROR",
            tld=["string"],
        )
        assert_matches_type(SummaryCacheHitResponse, summary, path=["response"])

    @parametrize
    def test_raw_response_cache_hit(self, client: Cloudflare) -> None:
        response = client.radar.dns.summary.with_raw_response.cache_hit()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        summary = response.parse()
        assert_matches_type(SummaryCacheHitResponse, summary, path=["response"])

    @parametrize
    def test_streaming_response_cache_hit(self, client: Cloudflare) -> None:
        with client.radar.dns.summary.with_streaming_response.cache_hit() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            summary = response.parse()
            assert_matches_type(SummaryCacheHitResponse, summary, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_dnssec(self, client: Cloudflare) -> None:
        summary = client.radar.dns.summary.dnssec()
        assert_matches_type(SummaryDNSSECResponse, summary, path=["response"])

    @parametrize
    def test_method_dnssec_with_all_params(self, client: Cloudflare) -> None:
        summary = client.radar.dns.summary.dnssec(
            asn=["string"],
            continent=["string"],
            date_end=[parse_datetime("2019-12-27T18:11:19.117Z")],
            date_range=["7d"],
            date_start=[parse_datetime("2019-12-27T18:11:19.117Z")],
            format="JSON",
            location=["string"],
            name=["main_series"],
            nodata=True,
            protocol="UDP",
            query_type="A",
            response_code="NOERROR",
            tld=["string"],
        )
        assert_matches_type(SummaryDNSSECResponse, summary, path=["response"])

    @parametrize
    def test_raw_response_dnssec(self, client: Cloudflare) -> None:
        response = client.radar.dns.summary.with_raw_response.dnssec()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        summary = response.parse()
        assert_matches_type(SummaryDNSSECResponse, summary, path=["response"])

    @parametrize
    def test_streaming_response_dnssec(self, client: Cloudflare) -> None:
        with client.radar.dns.summary.with_streaming_response.dnssec() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            summary = response.parse()
            assert_matches_type(SummaryDNSSECResponse, summary, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_dnssec_aware(self, client: Cloudflare) -> None:
        summary = client.radar.dns.summary.dnssec_aware()
        assert_matches_type(SummaryDNSSECAwareResponse, summary, path=["response"])

    @parametrize
    def test_method_dnssec_aware_with_all_params(self, client: Cloudflare) -> None:
        summary = client.radar.dns.summary.dnssec_aware(
            asn=["string"],
            continent=["string"],
            date_end=[parse_datetime("2019-12-27T18:11:19.117Z")],
            date_range=["7d"],
            date_start=[parse_datetime("2019-12-27T18:11:19.117Z")],
            format="JSON",
            location=["string"],
            name=["main_series"],
            nodata=True,
            protocol="UDP",
            query_type="A",
            response_code="NOERROR",
            tld=["string"],
        )
        assert_matches_type(SummaryDNSSECAwareResponse, summary, path=["response"])

    @parametrize
    def test_raw_response_dnssec_aware(self, client: Cloudflare) -> None:
        response = client.radar.dns.summary.with_raw_response.dnssec_aware()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        summary = response.parse()
        assert_matches_type(SummaryDNSSECAwareResponse, summary, path=["response"])

    @parametrize
    def test_streaming_response_dnssec_aware(self, client: Cloudflare) -> None:
        with client.radar.dns.summary.with_streaming_response.dnssec_aware() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            summary = response.parse()
            assert_matches_type(SummaryDNSSECAwareResponse, summary, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_dnssec_e2e(self, client: Cloudflare) -> None:
        summary = client.radar.dns.summary.dnssec_e2e()
        assert_matches_type(SummaryDNSSECE2EResponse, summary, path=["response"])

    @parametrize
    def test_method_dnssec_e2e_with_all_params(self, client: Cloudflare) -> None:
        summary = client.radar.dns.summary.dnssec_e2e(
            asn=["string"],
            continent=["string"],
            date_end=[parse_datetime("2019-12-27T18:11:19.117Z")],
            date_range=["7d"],
            date_start=[parse_datetime("2019-12-27T18:11:19.117Z")],
            format="JSON",
            location=["string"],
            name=["main_series"],
            nodata=True,
            protocol="UDP",
            query_type="A",
            response_code="NOERROR",
            tld=["string"],
        )
        assert_matches_type(SummaryDNSSECE2EResponse, summary, path=["response"])

    @parametrize
    def test_raw_response_dnssec_e2e(self, client: Cloudflare) -> None:
        response = client.radar.dns.summary.with_raw_response.dnssec_e2e()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        summary = response.parse()
        assert_matches_type(SummaryDNSSECE2EResponse, summary, path=["response"])

    @parametrize
    def test_streaming_response_dnssec_e2e(self, client: Cloudflare) -> None:
        with client.radar.dns.summary.with_streaming_response.dnssec_e2e() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            summary = response.parse()
            assert_matches_type(SummaryDNSSECE2EResponse, summary, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_ip_version(self, client: Cloudflare) -> None:
        summary = client.radar.dns.summary.ip_version()
        assert_matches_type(SummaryIPVersionResponse, summary, path=["response"])

    @parametrize
    def test_method_ip_version_with_all_params(self, client: Cloudflare) -> None:
        summary = client.radar.dns.summary.ip_version(
            asn=["string"],
            continent=["string"],
            date_end=[parse_datetime("2019-12-27T18:11:19.117Z")],
            date_range=["7d"],
            date_start=[parse_datetime("2019-12-27T18:11:19.117Z")],
            format="JSON",
            location=["string"],
            name=["main_series"],
            nodata=True,
            protocol="UDP",
            query_type="A",
            response_code="NOERROR",
            tld=["string"],
        )
        assert_matches_type(SummaryIPVersionResponse, summary, path=["response"])

    @parametrize
    def test_raw_response_ip_version(self, client: Cloudflare) -> None:
        response = client.radar.dns.summary.with_raw_response.ip_version()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        summary = response.parse()
        assert_matches_type(SummaryIPVersionResponse, summary, path=["response"])

    @parametrize
    def test_streaming_response_ip_version(self, client: Cloudflare) -> None:
        with client.radar.dns.summary.with_streaming_response.ip_version() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            summary = response.parse()
            assert_matches_type(SummaryIPVersionResponse, summary, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_matching_answer(self, client: Cloudflare) -> None:
        summary = client.radar.dns.summary.matching_answer()
        assert_matches_type(SummaryMatchingAnswerResponse, summary, path=["response"])

    @parametrize
    def test_method_matching_answer_with_all_params(self, client: Cloudflare) -> None:
        summary = client.radar.dns.summary.matching_answer(
            asn=["string"],
            continent=["string"],
            date_end=[parse_datetime("2019-12-27T18:11:19.117Z")],
            date_range=["7d"],
            date_start=[parse_datetime("2019-12-27T18:11:19.117Z")],
            format="JSON",
            location=["string"],
            name=["main_series"],
            nodata=True,
            protocol="UDP",
            query_type="A",
            response_code="NOERROR",
            tld=["string"],
        )
        assert_matches_type(SummaryMatchingAnswerResponse, summary, path=["response"])

    @parametrize
    def test_raw_response_matching_answer(self, client: Cloudflare) -> None:
        response = client.radar.dns.summary.with_raw_response.matching_answer()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        summary = response.parse()
        assert_matches_type(SummaryMatchingAnswerResponse, summary, path=["response"])

    @parametrize
    def test_streaming_response_matching_answer(self, client: Cloudflare) -> None:
        with client.radar.dns.summary.with_streaming_response.matching_answer() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            summary = response.parse()
            assert_matches_type(SummaryMatchingAnswerResponse, summary, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_protocol(self, client: Cloudflare) -> None:
        summary = client.radar.dns.summary.protocol()
        assert_matches_type(SummaryProtocolResponse, summary, path=["response"])

    @parametrize
    def test_method_protocol_with_all_params(self, client: Cloudflare) -> None:
        summary = client.radar.dns.summary.protocol(
            asn=["string"],
            continent=["string"],
            date_end=[parse_datetime("2019-12-27T18:11:19.117Z")],
            date_range=["7d"],
            date_start=[parse_datetime("2019-12-27T18:11:19.117Z")],
            format="JSON",
            location=["string"],
            name=["main_series"],
            nodata=True,
            query_type="A",
            response_code="NOERROR",
            tld=["string"],
        )
        assert_matches_type(SummaryProtocolResponse, summary, path=["response"])

    @parametrize
    def test_raw_response_protocol(self, client: Cloudflare) -> None:
        response = client.radar.dns.summary.with_raw_response.protocol()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        summary = response.parse()
        assert_matches_type(SummaryProtocolResponse, summary, path=["response"])

    @parametrize
    def test_streaming_response_protocol(self, client: Cloudflare) -> None:
        with client.radar.dns.summary.with_streaming_response.protocol() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            summary = response.parse()
            assert_matches_type(SummaryProtocolResponse, summary, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_query_type(self, client: Cloudflare) -> None:
        summary = client.radar.dns.summary.query_type()
        assert_matches_type(SummaryQueryTypeResponse, summary, path=["response"])

    @parametrize
    def test_method_query_type_with_all_params(self, client: Cloudflare) -> None:
        summary = client.radar.dns.summary.query_type(
            asn=["string"],
            continent=["string"],
            date_end=[parse_datetime("2019-12-27T18:11:19.117Z")],
            date_range=["7d"],
            date_start=[parse_datetime("2019-12-27T18:11:19.117Z")],
            format="JSON",
            limit_per_group=10,
            location=["string"],
            name=["main_series"],
            nodata=True,
            protocol="UDP",
            response_code="NOERROR",
            tld=["string"],
        )
        assert_matches_type(SummaryQueryTypeResponse, summary, path=["response"])

    @parametrize
    def test_raw_response_query_type(self, client: Cloudflare) -> None:
        response = client.radar.dns.summary.with_raw_response.query_type()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        summary = response.parse()
        assert_matches_type(SummaryQueryTypeResponse, summary, path=["response"])

    @parametrize
    def test_streaming_response_query_type(self, client: Cloudflare) -> None:
        with client.radar.dns.summary.with_streaming_response.query_type() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            summary = response.parse()
            assert_matches_type(SummaryQueryTypeResponse, summary, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_response_code(self, client: Cloudflare) -> None:
        summary = client.radar.dns.summary.response_code()
        assert_matches_type(SummaryResponseCodeResponse, summary, path=["response"])

    @parametrize
    def test_method_response_code_with_all_params(self, client: Cloudflare) -> None:
        summary = client.radar.dns.summary.response_code(
            asn=["string"],
            continent=["string"],
            date_end=[parse_datetime("2019-12-27T18:11:19.117Z")],
            date_range=["7d"],
            date_start=[parse_datetime("2019-12-27T18:11:19.117Z")],
            format="JSON",
            limit_per_group=10,
            location=["string"],
            name=["main_series"],
            nodata=True,
            protocol="UDP",
            query_type="A",
            tld=["string"],
        )
        assert_matches_type(SummaryResponseCodeResponse, summary, path=["response"])

    @parametrize
    def test_raw_response_response_code(self, client: Cloudflare) -> None:
        response = client.radar.dns.summary.with_raw_response.response_code()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        summary = response.parse()
        assert_matches_type(SummaryResponseCodeResponse, summary, path=["response"])

    @parametrize
    def test_streaming_response_response_code(self, client: Cloudflare) -> None:
        with client.radar.dns.summary.with_streaming_response.response_code() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            summary = response.parse()
            assert_matches_type(SummaryResponseCodeResponse, summary, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_response_ttl(self, client: Cloudflare) -> None:
        summary = client.radar.dns.summary.response_ttl()
        assert_matches_type(SummaryResponseTTLResponse, summary, path=["response"])

    @parametrize
    def test_method_response_ttl_with_all_params(self, client: Cloudflare) -> None:
        summary = client.radar.dns.summary.response_ttl(
            asn=["string"],
            continent=["string"],
            date_end=[parse_datetime("2019-12-27T18:11:19.117Z")],
            date_range=["7d"],
            date_start=[parse_datetime("2019-12-27T18:11:19.117Z")],
            format="JSON",
            location=["string"],
            name=["main_series"],
            nodata=True,
            protocol="UDP",
            query_type="A",
            response_code="NOERROR",
            tld=["string"],
        )
        assert_matches_type(SummaryResponseTTLResponse, summary, path=["response"])

    @parametrize
    def test_raw_response_response_ttl(self, client: Cloudflare) -> None:
        response = client.radar.dns.summary.with_raw_response.response_ttl()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        summary = response.parse()
        assert_matches_type(SummaryResponseTTLResponse, summary, path=["response"])

    @parametrize
    def test_streaming_response_response_ttl(self, client: Cloudflare) -> None:
        with client.radar.dns.summary.with_streaming_response.response_ttl() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            summary = response.parse()
            assert_matches_type(SummaryResponseTTLResponse, summary, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncSummary:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_cache_hit(self, async_client: AsyncCloudflare) -> None:
        summary = await async_client.radar.dns.summary.cache_hit()
        assert_matches_type(SummaryCacheHitResponse, summary, path=["response"])

    @parametrize
    async def test_method_cache_hit_with_all_params(self, async_client: AsyncCloudflare) -> None:
        summary = await async_client.radar.dns.summary.cache_hit(
            asn=["string"],
            continent=["string"],
            date_end=[parse_datetime("2019-12-27T18:11:19.117Z")],
            date_range=["7d"],
            date_start=[parse_datetime("2019-12-27T18:11:19.117Z")],
            format="JSON",
            location=["string"],
            name=["main_series"],
            nodata=True,
            protocol="UDP",
            query_type="A",
            response_code="NOERROR",
            tld=["string"],
        )
        assert_matches_type(SummaryCacheHitResponse, summary, path=["response"])

    @parametrize
    async def test_raw_response_cache_hit(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.radar.dns.summary.with_raw_response.cache_hit()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        summary = await response.parse()
        assert_matches_type(SummaryCacheHitResponse, summary, path=["response"])

    @parametrize
    async def test_streaming_response_cache_hit(self, async_client: AsyncCloudflare) -> None:
        async with async_client.radar.dns.summary.with_streaming_response.cache_hit() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            summary = await response.parse()
            assert_matches_type(SummaryCacheHitResponse, summary, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_dnssec(self, async_client: AsyncCloudflare) -> None:
        summary = await async_client.radar.dns.summary.dnssec()
        assert_matches_type(SummaryDNSSECResponse, summary, path=["response"])

    @parametrize
    async def test_method_dnssec_with_all_params(self, async_client: AsyncCloudflare) -> None:
        summary = await async_client.radar.dns.summary.dnssec(
            asn=["string"],
            continent=["string"],
            date_end=[parse_datetime("2019-12-27T18:11:19.117Z")],
            date_range=["7d"],
            date_start=[parse_datetime("2019-12-27T18:11:19.117Z")],
            format="JSON",
            location=["string"],
            name=["main_series"],
            nodata=True,
            protocol="UDP",
            query_type="A",
            response_code="NOERROR",
            tld=["string"],
        )
        assert_matches_type(SummaryDNSSECResponse, summary, path=["response"])

    @parametrize
    async def test_raw_response_dnssec(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.radar.dns.summary.with_raw_response.dnssec()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        summary = await response.parse()
        assert_matches_type(SummaryDNSSECResponse, summary, path=["response"])

    @parametrize
    async def test_streaming_response_dnssec(self, async_client: AsyncCloudflare) -> None:
        async with async_client.radar.dns.summary.with_streaming_response.dnssec() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            summary = await response.parse()
            assert_matches_type(SummaryDNSSECResponse, summary, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_dnssec_aware(self, async_client: AsyncCloudflare) -> None:
        summary = await async_client.radar.dns.summary.dnssec_aware()
        assert_matches_type(SummaryDNSSECAwareResponse, summary, path=["response"])

    @parametrize
    async def test_method_dnssec_aware_with_all_params(self, async_client: AsyncCloudflare) -> None:
        summary = await async_client.radar.dns.summary.dnssec_aware(
            asn=["string"],
            continent=["string"],
            date_end=[parse_datetime("2019-12-27T18:11:19.117Z")],
            date_range=["7d"],
            date_start=[parse_datetime("2019-12-27T18:11:19.117Z")],
            format="JSON",
            location=["string"],
            name=["main_series"],
            nodata=True,
            protocol="UDP",
            query_type="A",
            response_code="NOERROR",
            tld=["string"],
        )
        assert_matches_type(SummaryDNSSECAwareResponse, summary, path=["response"])

    @parametrize
    async def test_raw_response_dnssec_aware(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.radar.dns.summary.with_raw_response.dnssec_aware()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        summary = await response.parse()
        assert_matches_type(SummaryDNSSECAwareResponse, summary, path=["response"])

    @parametrize
    async def test_streaming_response_dnssec_aware(self, async_client: AsyncCloudflare) -> None:
        async with async_client.radar.dns.summary.with_streaming_response.dnssec_aware() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            summary = await response.parse()
            assert_matches_type(SummaryDNSSECAwareResponse, summary, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_dnssec_e2e(self, async_client: AsyncCloudflare) -> None:
        summary = await async_client.radar.dns.summary.dnssec_e2e()
        assert_matches_type(SummaryDNSSECE2EResponse, summary, path=["response"])

    @parametrize
    async def test_method_dnssec_e2e_with_all_params(self, async_client: AsyncCloudflare) -> None:
        summary = await async_client.radar.dns.summary.dnssec_e2e(
            asn=["string"],
            continent=["string"],
            date_end=[parse_datetime("2019-12-27T18:11:19.117Z")],
            date_range=["7d"],
            date_start=[parse_datetime("2019-12-27T18:11:19.117Z")],
            format="JSON",
            location=["string"],
            name=["main_series"],
            nodata=True,
            protocol="UDP",
            query_type="A",
            response_code="NOERROR",
            tld=["string"],
        )
        assert_matches_type(SummaryDNSSECE2EResponse, summary, path=["response"])

    @parametrize
    async def test_raw_response_dnssec_e2e(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.radar.dns.summary.with_raw_response.dnssec_e2e()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        summary = await response.parse()
        assert_matches_type(SummaryDNSSECE2EResponse, summary, path=["response"])

    @parametrize
    async def test_streaming_response_dnssec_e2e(self, async_client: AsyncCloudflare) -> None:
        async with async_client.radar.dns.summary.with_streaming_response.dnssec_e2e() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            summary = await response.parse()
            assert_matches_type(SummaryDNSSECE2EResponse, summary, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_ip_version(self, async_client: AsyncCloudflare) -> None:
        summary = await async_client.radar.dns.summary.ip_version()
        assert_matches_type(SummaryIPVersionResponse, summary, path=["response"])

    @parametrize
    async def test_method_ip_version_with_all_params(self, async_client: AsyncCloudflare) -> None:
        summary = await async_client.radar.dns.summary.ip_version(
            asn=["string"],
            continent=["string"],
            date_end=[parse_datetime("2019-12-27T18:11:19.117Z")],
            date_range=["7d"],
            date_start=[parse_datetime("2019-12-27T18:11:19.117Z")],
            format="JSON",
            location=["string"],
            name=["main_series"],
            nodata=True,
            protocol="UDP",
            query_type="A",
            response_code="NOERROR",
            tld=["string"],
        )
        assert_matches_type(SummaryIPVersionResponse, summary, path=["response"])

    @parametrize
    async def test_raw_response_ip_version(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.radar.dns.summary.with_raw_response.ip_version()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        summary = await response.parse()
        assert_matches_type(SummaryIPVersionResponse, summary, path=["response"])

    @parametrize
    async def test_streaming_response_ip_version(self, async_client: AsyncCloudflare) -> None:
        async with async_client.radar.dns.summary.with_streaming_response.ip_version() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            summary = await response.parse()
            assert_matches_type(SummaryIPVersionResponse, summary, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_matching_answer(self, async_client: AsyncCloudflare) -> None:
        summary = await async_client.radar.dns.summary.matching_answer()
        assert_matches_type(SummaryMatchingAnswerResponse, summary, path=["response"])

    @parametrize
    async def test_method_matching_answer_with_all_params(self, async_client: AsyncCloudflare) -> None:
        summary = await async_client.radar.dns.summary.matching_answer(
            asn=["string"],
            continent=["string"],
            date_end=[parse_datetime("2019-12-27T18:11:19.117Z")],
            date_range=["7d"],
            date_start=[parse_datetime("2019-12-27T18:11:19.117Z")],
            format="JSON",
            location=["string"],
            name=["main_series"],
            nodata=True,
            protocol="UDP",
            query_type="A",
            response_code="NOERROR",
            tld=["string"],
        )
        assert_matches_type(SummaryMatchingAnswerResponse, summary, path=["response"])

    @parametrize
    async def test_raw_response_matching_answer(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.radar.dns.summary.with_raw_response.matching_answer()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        summary = await response.parse()
        assert_matches_type(SummaryMatchingAnswerResponse, summary, path=["response"])

    @parametrize
    async def test_streaming_response_matching_answer(self, async_client: AsyncCloudflare) -> None:
        async with async_client.radar.dns.summary.with_streaming_response.matching_answer() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            summary = await response.parse()
            assert_matches_type(SummaryMatchingAnswerResponse, summary, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_protocol(self, async_client: AsyncCloudflare) -> None:
        summary = await async_client.radar.dns.summary.protocol()
        assert_matches_type(SummaryProtocolResponse, summary, path=["response"])

    @parametrize
    async def test_method_protocol_with_all_params(self, async_client: AsyncCloudflare) -> None:
        summary = await async_client.radar.dns.summary.protocol(
            asn=["string"],
            continent=["string"],
            date_end=[parse_datetime("2019-12-27T18:11:19.117Z")],
            date_range=["7d"],
            date_start=[parse_datetime("2019-12-27T18:11:19.117Z")],
            format="JSON",
            location=["string"],
            name=["main_series"],
            nodata=True,
            query_type="A",
            response_code="NOERROR",
            tld=["string"],
        )
        assert_matches_type(SummaryProtocolResponse, summary, path=["response"])

    @parametrize
    async def test_raw_response_protocol(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.radar.dns.summary.with_raw_response.protocol()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        summary = await response.parse()
        assert_matches_type(SummaryProtocolResponse, summary, path=["response"])

    @parametrize
    async def test_streaming_response_protocol(self, async_client: AsyncCloudflare) -> None:
        async with async_client.radar.dns.summary.with_streaming_response.protocol() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            summary = await response.parse()
            assert_matches_type(SummaryProtocolResponse, summary, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_query_type(self, async_client: AsyncCloudflare) -> None:
        summary = await async_client.radar.dns.summary.query_type()
        assert_matches_type(SummaryQueryTypeResponse, summary, path=["response"])

    @parametrize
    async def test_method_query_type_with_all_params(self, async_client: AsyncCloudflare) -> None:
        summary = await async_client.radar.dns.summary.query_type(
            asn=["string"],
            continent=["string"],
            date_end=[parse_datetime("2019-12-27T18:11:19.117Z")],
            date_range=["7d"],
            date_start=[parse_datetime("2019-12-27T18:11:19.117Z")],
            format="JSON",
            limit_per_group=10,
            location=["string"],
            name=["main_series"],
            nodata=True,
            protocol="UDP",
            response_code="NOERROR",
            tld=["string"],
        )
        assert_matches_type(SummaryQueryTypeResponse, summary, path=["response"])

    @parametrize
    async def test_raw_response_query_type(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.radar.dns.summary.with_raw_response.query_type()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        summary = await response.parse()
        assert_matches_type(SummaryQueryTypeResponse, summary, path=["response"])

    @parametrize
    async def test_streaming_response_query_type(self, async_client: AsyncCloudflare) -> None:
        async with async_client.radar.dns.summary.with_streaming_response.query_type() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            summary = await response.parse()
            assert_matches_type(SummaryQueryTypeResponse, summary, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_response_code(self, async_client: AsyncCloudflare) -> None:
        summary = await async_client.radar.dns.summary.response_code()
        assert_matches_type(SummaryResponseCodeResponse, summary, path=["response"])

    @parametrize
    async def test_method_response_code_with_all_params(self, async_client: AsyncCloudflare) -> None:
        summary = await async_client.radar.dns.summary.response_code(
            asn=["string"],
            continent=["string"],
            date_end=[parse_datetime("2019-12-27T18:11:19.117Z")],
            date_range=["7d"],
            date_start=[parse_datetime("2019-12-27T18:11:19.117Z")],
            format="JSON",
            limit_per_group=10,
            location=["string"],
            name=["main_series"],
            nodata=True,
            protocol="UDP",
            query_type="A",
            tld=["string"],
        )
        assert_matches_type(SummaryResponseCodeResponse, summary, path=["response"])

    @parametrize
    async def test_raw_response_response_code(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.radar.dns.summary.with_raw_response.response_code()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        summary = await response.parse()
        assert_matches_type(SummaryResponseCodeResponse, summary, path=["response"])

    @parametrize
    async def test_streaming_response_response_code(self, async_client: AsyncCloudflare) -> None:
        async with async_client.radar.dns.summary.with_streaming_response.response_code() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            summary = await response.parse()
            assert_matches_type(SummaryResponseCodeResponse, summary, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_response_ttl(self, async_client: AsyncCloudflare) -> None:
        summary = await async_client.radar.dns.summary.response_ttl()
        assert_matches_type(SummaryResponseTTLResponse, summary, path=["response"])

    @parametrize
    async def test_method_response_ttl_with_all_params(self, async_client: AsyncCloudflare) -> None:
        summary = await async_client.radar.dns.summary.response_ttl(
            asn=["string"],
            continent=["string"],
            date_end=[parse_datetime("2019-12-27T18:11:19.117Z")],
            date_range=["7d"],
            date_start=[parse_datetime("2019-12-27T18:11:19.117Z")],
            format="JSON",
            location=["string"],
            name=["main_series"],
            nodata=True,
            protocol="UDP",
            query_type="A",
            response_code="NOERROR",
            tld=["string"],
        )
        assert_matches_type(SummaryResponseTTLResponse, summary, path=["response"])

    @parametrize
    async def test_raw_response_response_ttl(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.radar.dns.summary.with_raw_response.response_ttl()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        summary = await response.parse()
        assert_matches_type(SummaryResponseTTLResponse, summary, path=["response"])

    @parametrize
    async def test_streaming_response_response_ttl(self, async_client: AsyncCloudflare) -> None:
        async with async_client.radar.dns.summary.with_streaming_response.response_ttl() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            summary = await response.parse()
            assert_matches_type(SummaryResponseTTLResponse, summary, path=["response"])

        assert cast(Any, response.is_closed) is True
