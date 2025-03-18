# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare._utils import parse_datetime
from cloudflare.types.radar.dns import (
    TimeseriesGroupDNSSECResponse,
    TimeseriesGroupCacheHitResponse,
    TimeseriesGroupProtocolResponse,
    TimeseriesGroupDNSSECE2EResponse,
    TimeseriesGroupIPVersionResponse,
    TimeseriesGroupQueryTypeResponse,
    TimeseriesGroupDNSSECAwareResponse,
    TimeseriesGroupResponseTTLResponse,
    TimeseriesGroupResponseCodeResponse,
    TimeseriesGroupMatchingAnswerResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTimeseriesGroups:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_cache_hit(self, client: Cloudflare) -> None:
        timeseries_group = client.radar.dns.timeseries_groups.cache_hit()
        assert_matches_type(TimeseriesGroupCacheHitResponse, timeseries_group, path=["response"])

    @parametrize
    def test_method_cache_hit_with_all_params(self, client: Cloudflare) -> None:
        timeseries_group = client.radar.dns.timeseries_groups.cache_hit(
            agg_interval="15m",
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
        assert_matches_type(TimeseriesGroupCacheHitResponse, timeseries_group, path=["response"])

    @parametrize
    def test_raw_response_cache_hit(self, client: Cloudflare) -> None:
        response = client.radar.dns.timeseries_groups.with_raw_response.cache_hit()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        timeseries_group = response.parse()
        assert_matches_type(TimeseriesGroupCacheHitResponse, timeseries_group, path=["response"])

    @parametrize
    def test_streaming_response_cache_hit(self, client: Cloudflare) -> None:
        with client.radar.dns.timeseries_groups.with_streaming_response.cache_hit() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            timeseries_group = response.parse()
            assert_matches_type(TimeseriesGroupCacheHitResponse, timeseries_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_dnssec(self, client: Cloudflare) -> None:
        timeseries_group = client.radar.dns.timeseries_groups.dnssec()
        assert_matches_type(TimeseriesGroupDNSSECResponse, timeseries_group, path=["response"])

    @parametrize
    def test_method_dnssec_with_all_params(self, client: Cloudflare) -> None:
        timeseries_group = client.radar.dns.timeseries_groups.dnssec(
            agg_interval="15m",
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
        assert_matches_type(TimeseriesGroupDNSSECResponse, timeseries_group, path=["response"])

    @parametrize
    def test_raw_response_dnssec(self, client: Cloudflare) -> None:
        response = client.radar.dns.timeseries_groups.with_raw_response.dnssec()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        timeseries_group = response.parse()
        assert_matches_type(TimeseriesGroupDNSSECResponse, timeseries_group, path=["response"])

    @parametrize
    def test_streaming_response_dnssec(self, client: Cloudflare) -> None:
        with client.radar.dns.timeseries_groups.with_streaming_response.dnssec() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            timeseries_group = response.parse()
            assert_matches_type(TimeseriesGroupDNSSECResponse, timeseries_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_dnssec_aware(self, client: Cloudflare) -> None:
        timeseries_group = client.radar.dns.timeseries_groups.dnssec_aware()
        assert_matches_type(TimeseriesGroupDNSSECAwareResponse, timeseries_group, path=["response"])

    @parametrize
    def test_method_dnssec_aware_with_all_params(self, client: Cloudflare) -> None:
        timeseries_group = client.radar.dns.timeseries_groups.dnssec_aware(
            agg_interval="15m",
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
        assert_matches_type(TimeseriesGroupDNSSECAwareResponse, timeseries_group, path=["response"])

    @parametrize
    def test_raw_response_dnssec_aware(self, client: Cloudflare) -> None:
        response = client.radar.dns.timeseries_groups.with_raw_response.dnssec_aware()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        timeseries_group = response.parse()
        assert_matches_type(TimeseriesGroupDNSSECAwareResponse, timeseries_group, path=["response"])

    @parametrize
    def test_streaming_response_dnssec_aware(self, client: Cloudflare) -> None:
        with client.radar.dns.timeseries_groups.with_streaming_response.dnssec_aware() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            timeseries_group = response.parse()
            assert_matches_type(TimeseriesGroupDNSSECAwareResponse, timeseries_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_dnssec_e2e(self, client: Cloudflare) -> None:
        timeseries_group = client.radar.dns.timeseries_groups.dnssec_e2e()
        assert_matches_type(TimeseriesGroupDNSSECE2EResponse, timeseries_group, path=["response"])

    @parametrize
    def test_method_dnssec_e2e_with_all_params(self, client: Cloudflare) -> None:
        timeseries_group = client.radar.dns.timeseries_groups.dnssec_e2e(
            agg_interval="15m",
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
        assert_matches_type(TimeseriesGroupDNSSECE2EResponse, timeseries_group, path=["response"])

    @parametrize
    def test_raw_response_dnssec_e2e(self, client: Cloudflare) -> None:
        response = client.radar.dns.timeseries_groups.with_raw_response.dnssec_e2e()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        timeseries_group = response.parse()
        assert_matches_type(TimeseriesGroupDNSSECE2EResponse, timeseries_group, path=["response"])

    @parametrize
    def test_streaming_response_dnssec_e2e(self, client: Cloudflare) -> None:
        with client.radar.dns.timeseries_groups.with_streaming_response.dnssec_e2e() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            timeseries_group = response.parse()
            assert_matches_type(TimeseriesGroupDNSSECE2EResponse, timeseries_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_ip_version(self, client: Cloudflare) -> None:
        timeseries_group = client.radar.dns.timeseries_groups.ip_version()
        assert_matches_type(TimeseriesGroupIPVersionResponse, timeseries_group, path=["response"])

    @parametrize
    def test_method_ip_version_with_all_params(self, client: Cloudflare) -> None:
        timeseries_group = client.radar.dns.timeseries_groups.ip_version(
            agg_interval="15m",
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
        assert_matches_type(TimeseriesGroupIPVersionResponse, timeseries_group, path=["response"])

    @parametrize
    def test_raw_response_ip_version(self, client: Cloudflare) -> None:
        response = client.radar.dns.timeseries_groups.with_raw_response.ip_version()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        timeseries_group = response.parse()
        assert_matches_type(TimeseriesGroupIPVersionResponse, timeseries_group, path=["response"])

    @parametrize
    def test_streaming_response_ip_version(self, client: Cloudflare) -> None:
        with client.radar.dns.timeseries_groups.with_streaming_response.ip_version() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            timeseries_group = response.parse()
            assert_matches_type(TimeseriesGroupIPVersionResponse, timeseries_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_matching_answer(self, client: Cloudflare) -> None:
        timeseries_group = client.radar.dns.timeseries_groups.matching_answer()
        assert_matches_type(TimeseriesGroupMatchingAnswerResponse, timeseries_group, path=["response"])

    @parametrize
    def test_method_matching_answer_with_all_params(self, client: Cloudflare) -> None:
        timeseries_group = client.radar.dns.timeseries_groups.matching_answer(
            agg_interval="15m",
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
        assert_matches_type(TimeseriesGroupMatchingAnswerResponse, timeseries_group, path=["response"])

    @parametrize
    def test_raw_response_matching_answer(self, client: Cloudflare) -> None:
        response = client.radar.dns.timeseries_groups.with_raw_response.matching_answer()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        timeseries_group = response.parse()
        assert_matches_type(TimeseriesGroupMatchingAnswerResponse, timeseries_group, path=["response"])

    @parametrize
    def test_streaming_response_matching_answer(self, client: Cloudflare) -> None:
        with client.radar.dns.timeseries_groups.with_streaming_response.matching_answer() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            timeseries_group = response.parse()
            assert_matches_type(TimeseriesGroupMatchingAnswerResponse, timeseries_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_protocol(self, client: Cloudflare) -> None:
        timeseries_group = client.radar.dns.timeseries_groups.protocol()
        assert_matches_type(TimeseriesGroupProtocolResponse, timeseries_group, path=["response"])

    @parametrize
    def test_method_protocol_with_all_params(self, client: Cloudflare) -> None:
        timeseries_group = client.radar.dns.timeseries_groups.protocol(
            agg_interval="15m",
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
        assert_matches_type(TimeseriesGroupProtocolResponse, timeseries_group, path=["response"])

    @parametrize
    def test_raw_response_protocol(self, client: Cloudflare) -> None:
        response = client.radar.dns.timeseries_groups.with_raw_response.protocol()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        timeseries_group = response.parse()
        assert_matches_type(TimeseriesGroupProtocolResponse, timeseries_group, path=["response"])

    @parametrize
    def test_streaming_response_protocol(self, client: Cloudflare) -> None:
        with client.radar.dns.timeseries_groups.with_streaming_response.protocol() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            timeseries_group = response.parse()
            assert_matches_type(TimeseriesGroupProtocolResponse, timeseries_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_query_type(self, client: Cloudflare) -> None:
        timeseries_group = client.radar.dns.timeseries_groups.query_type()
        assert_matches_type(TimeseriesGroupQueryTypeResponse, timeseries_group, path=["response"])

    @parametrize
    def test_method_query_type_with_all_params(self, client: Cloudflare) -> None:
        timeseries_group = client.radar.dns.timeseries_groups.query_type(
            agg_interval="15m",
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
        assert_matches_type(TimeseriesGroupQueryTypeResponse, timeseries_group, path=["response"])

    @parametrize
    def test_raw_response_query_type(self, client: Cloudflare) -> None:
        response = client.radar.dns.timeseries_groups.with_raw_response.query_type()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        timeseries_group = response.parse()
        assert_matches_type(TimeseriesGroupQueryTypeResponse, timeseries_group, path=["response"])

    @parametrize
    def test_streaming_response_query_type(self, client: Cloudflare) -> None:
        with client.radar.dns.timeseries_groups.with_streaming_response.query_type() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            timeseries_group = response.parse()
            assert_matches_type(TimeseriesGroupQueryTypeResponse, timeseries_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_response_code(self, client: Cloudflare) -> None:
        timeseries_group = client.radar.dns.timeseries_groups.response_code()
        assert_matches_type(TimeseriesGroupResponseCodeResponse, timeseries_group, path=["response"])

    @parametrize
    def test_method_response_code_with_all_params(self, client: Cloudflare) -> None:
        timeseries_group = client.radar.dns.timeseries_groups.response_code(
            agg_interval="15m",
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
        assert_matches_type(TimeseriesGroupResponseCodeResponse, timeseries_group, path=["response"])

    @parametrize
    def test_raw_response_response_code(self, client: Cloudflare) -> None:
        response = client.radar.dns.timeseries_groups.with_raw_response.response_code()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        timeseries_group = response.parse()
        assert_matches_type(TimeseriesGroupResponseCodeResponse, timeseries_group, path=["response"])

    @parametrize
    def test_streaming_response_response_code(self, client: Cloudflare) -> None:
        with client.radar.dns.timeseries_groups.with_streaming_response.response_code() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            timeseries_group = response.parse()
            assert_matches_type(TimeseriesGroupResponseCodeResponse, timeseries_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_response_ttl(self, client: Cloudflare) -> None:
        timeseries_group = client.radar.dns.timeseries_groups.response_ttl()
        assert_matches_type(TimeseriesGroupResponseTTLResponse, timeseries_group, path=["response"])

    @parametrize
    def test_method_response_ttl_with_all_params(self, client: Cloudflare) -> None:
        timeseries_group = client.radar.dns.timeseries_groups.response_ttl(
            agg_interval="15m",
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
        assert_matches_type(TimeseriesGroupResponseTTLResponse, timeseries_group, path=["response"])

    @parametrize
    def test_raw_response_response_ttl(self, client: Cloudflare) -> None:
        response = client.radar.dns.timeseries_groups.with_raw_response.response_ttl()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        timeseries_group = response.parse()
        assert_matches_type(TimeseriesGroupResponseTTLResponse, timeseries_group, path=["response"])

    @parametrize
    def test_streaming_response_response_ttl(self, client: Cloudflare) -> None:
        with client.radar.dns.timeseries_groups.with_streaming_response.response_ttl() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            timeseries_group = response.parse()
            assert_matches_type(TimeseriesGroupResponseTTLResponse, timeseries_group, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncTimeseriesGroups:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_cache_hit(self, async_client: AsyncCloudflare) -> None:
        timeseries_group = await async_client.radar.dns.timeseries_groups.cache_hit()
        assert_matches_type(TimeseriesGroupCacheHitResponse, timeseries_group, path=["response"])

    @parametrize
    async def test_method_cache_hit_with_all_params(self, async_client: AsyncCloudflare) -> None:
        timeseries_group = await async_client.radar.dns.timeseries_groups.cache_hit(
            agg_interval="15m",
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
        assert_matches_type(TimeseriesGroupCacheHitResponse, timeseries_group, path=["response"])

    @parametrize
    async def test_raw_response_cache_hit(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.radar.dns.timeseries_groups.with_raw_response.cache_hit()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        timeseries_group = await response.parse()
        assert_matches_type(TimeseriesGroupCacheHitResponse, timeseries_group, path=["response"])

    @parametrize
    async def test_streaming_response_cache_hit(self, async_client: AsyncCloudflare) -> None:
        async with async_client.radar.dns.timeseries_groups.with_streaming_response.cache_hit() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            timeseries_group = await response.parse()
            assert_matches_type(TimeseriesGroupCacheHitResponse, timeseries_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_dnssec(self, async_client: AsyncCloudflare) -> None:
        timeseries_group = await async_client.radar.dns.timeseries_groups.dnssec()
        assert_matches_type(TimeseriesGroupDNSSECResponse, timeseries_group, path=["response"])

    @parametrize
    async def test_method_dnssec_with_all_params(self, async_client: AsyncCloudflare) -> None:
        timeseries_group = await async_client.radar.dns.timeseries_groups.dnssec(
            agg_interval="15m",
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
        assert_matches_type(TimeseriesGroupDNSSECResponse, timeseries_group, path=["response"])

    @parametrize
    async def test_raw_response_dnssec(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.radar.dns.timeseries_groups.with_raw_response.dnssec()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        timeseries_group = await response.parse()
        assert_matches_type(TimeseriesGroupDNSSECResponse, timeseries_group, path=["response"])

    @parametrize
    async def test_streaming_response_dnssec(self, async_client: AsyncCloudflare) -> None:
        async with async_client.radar.dns.timeseries_groups.with_streaming_response.dnssec() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            timeseries_group = await response.parse()
            assert_matches_type(TimeseriesGroupDNSSECResponse, timeseries_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_dnssec_aware(self, async_client: AsyncCloudflare) -> None:
        timeseries_group = await async_client.radar.dns.timeseries_groups.dnssec_aware()
        assert_matches_type(TimeseriesGroupDNSSECAwareResponse, timeseries_group, path=["response"])

    @parametrize
    async def test_method_dnssec_aware_with_all_params(self, async_client: AsyncCloudflare) -> None:
        timeseries_group = await async_client.radar.dns.timeseries_groups.dnssec_aware(
            agg_interval="15m",
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
        assert_matches_type(TimeseriesGroupDNSSECAwareResponse, timeseries_group, path=["response"])

    @parametrize
    async def test_raw_response_dnssec_aware(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.radar.dns.timeseries_groups.with_raw_response.dnssec_aware()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        timeseries_group = await response.parse()
        assert_matches_type(TimeseriesGroupDNSSECAwareResponse, timeseries_group, path=["response"])

    @parametrize
    async def test_streaming_response_dnssec_aware(self, async_client: AsyncCloudflare) -> None:
        async with async_client.radar.dns.timeseries_groups.with_streaming_response.dnssec_aware() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            timeseries_group = await response.parse()
            assert_matches_type(TimeseriesGroupDNSSECAwareResponse, timeseries_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_dnssec_e2e(self, async_client: AsyncCloudflare) -> None:
        timeseries_group = await async_client.radar.dns.timeseries_groups.dnssec_e2e()
        assert_matches_type(TimeseriesGroupDNSSECE2EResponse, timeseries_group, path=["response"])

    @parametrize
    async def test_method_dnssec_e2e_with_all_params(self, async_client: AsyncCloudflare) -> None:
        timeseries_group = await async_client.radar.dns.timeseries_groups.dnssec_e2e(
            agg_interval="15m",
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
        assert_matches_type(TimeseriesGroupDNSSECE2EResponse, timeseries_group, path=["response"])

    @parametrize
    async def test_raw_response_dnssec_e2e(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.radar.dns.timeseries_groups.with_raw_response.dnssec_e2e()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        timeseries_group = await response.parse()
        assert_matches_type(TimeseriesGroupDNSSECE2EResponse, timeseries_group, path=["response"])

    @parametrize
    async def test_streaming_response_dnssec_e2e(self, async_client: AsyncCloudflare) -> None:
        async with async_client.radar.dns.timeseries_groups.with_streaming_response.dnssec_e2e() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            timeseries_group = await response.parse()
            assert_matches_type(TimeseriesGroupDNSSECE2EResponse, timeseries_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_ip_version(self, async_client: AsyncCloudflare) -> None:
        timeseries_group = await async_client.radar.dns.timeseries_groups.ip_version()
        assert_matches_type(TimeseriesGroupIPVersionResponse, timeseries_group, path=["response"])

    @parametrize
    async def test_method_ip_version_with_all_params(self, async_client: AsyncCloudflare) -> None:
        timeseries_group = await async_client.radar.dns.timeseries_groups.ip_version(
            agg_interval="15m",
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
        assert_matches_type(TimeseriesGroupIPVersionResponse, timeseries_group, path=["response"])

    @parametrize
    async def test_raw_response_ip_version(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.radar.dns.timeseries_groups.with_raw_response.ip_version()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        timeseries_group = await response.parse()
        assert_matches_type(TimeseriesGroupIPVersionResponse, timeseries_group, path=["response"])

    @parametrize
    async def test_streaming_response_ip_version(self, async_client: AsyncCloudflare) -> None:
        async with async_client.radar.dns.timeseries_groups.with_streaming_response.ip_version() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            timeseries_group = await response.parse()
            assert_matches_type(TimeseriesGroupIPVersionResponse, timeseries_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_matching_answer(self, async_client: AsyncCloudflare) -> None:
        timeseries_group = await async_client.radar.dns.timeseries_groups.matching_answer()
        assert_matches_type(TimeseriesGroupMatchingAnswerResponse, timeseries_group, path=["response"])

    @parametrize
    async def test_method_matching_answer_with_all_params(self, async_client: AsyncCloudflare) -> None:
        timeseries_group = await async_client.radar.dns.timeseries_groups.matching_answer(
            agg_interval="15m",
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
        assert_matches_type(TimeseriesGroupMatchingAnswerResponse, timeseries_group, path=["response"])

    @parametrize
    async def test_raw_response_matching_answer(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.radar.dns.timeseries_groups.with_raw_response.matching_answer()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        timeseries_group = await response.parse()
        assert_matches_type(TimeseriesGroupMatchingAnswerResponse, timeseries_group, path=["response"])

    @parametrize
    async def test_streaming_response_matching_answer(self, async_client: AsyncCloudflare) -> None:
        async with async_client.radar.dns.timeseries_groups.with_streaming_response.matching_answer() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            timeseries_group = await response.parse()
            assert_matches_type(TimeseriesGroupMatchingAnswerResponse, timeseries_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_protocol(self, async_client: AsyncCloudflare) -> None:
        timeseries_group = await async_client.radar.dns.timeseries_groups.protocol()
        assert_matches_type(TimeseriesGroupProtocolResponse, timeseries_group, path=["response"])

    @parametrize
    async def test_method_protocol_with_all_params(self, async_client: AsyncCloudflare) -> None:
        timeseries_group = await async_client.radar.dns.timeseries_groups.protocol(
            agg_interval="15m",
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
        assert_matches_type(TimeseriesGroupProtocolResponse, timeseries_group, path=["response"])

    @parametrize
    async def test_raw_response_protocol(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.radar.dns.timeseries_groups.with_raw_response.protocol()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        timeseries_group = await response.parse()
        assert_matches_type(TimeseriesGroupProtocolResponse, timeseries_group, path=["response"])

    @parametrize
    async def test_streaming_response_protocol(self, async_client: AsyncCloudflare) -> None:
        async with async_client.radar.dns.timeseries_groups.with_streaming_response.protocol() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            timeseries_group = await response.parse()
            assert_matches_type(TimeseriesGroupProtocolResponse, timeseries_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_query_type(self, async_client: AsyncCloudflare) -> None:
        timeseries_group = await async_client.radar.dns.timeseries_groups.query_type()
        assert_matches_type(TimeseriesGroupQueryTypeResponse, timeseries_group, path=["response"])

    @parametrize
    async def test_method_query_type_with_all_params(self, async_client: AsyncCloudflare) -> None:
        timeseries_group = await async_client.radar.dns.timeseries_groups.query_type(
            agg_interval="15m",
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
        assert_matches_type(TimeseriesGroupQueryTypeResponse, timeseries_group, path=["response"])

    @parametrize
    async def test_raw_response_query_type(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.radar.dns.timeseries_groups.with_raw_response.query_type()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        timeseries_group = await response.parse()
        assert_matches_type(TimeseriesGroupQueryTypeResponse, timeseries_group, path=["response"])

    @parametrize
    async def test_streaming_response_query_type(self, async_client: AsyncCloudflare) -> None:
        async with async_client.radar.dns.timeseries_groups.with_streaming_response.query_type() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            timeseries_group = await response.parse()
            assert_matches_type(TimeseriesGroupQueryTypeResponse, timeseries_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_response_code(self, async_client: AsyncCloudflare) -> None:
        timeseries_group = await async_client.radar.dns.timeseries_groups.response_code()
        assert_matches_type(TimeseriesGroupResponseCodeResponse, timeseries_group, path=["response"])

    @parametrize
    async def test_method_response_code_with_all_params(self, async_client: AsyncCloudflare) -> None:
        timeseries_group = await async_client.radar.dns.timeseries_groups.response_code(
            agg_interval="15m",
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
        assert_matches_type(TimeseriesGroupResponseCodeResponse, timeseries_group, path=["response"])

    @parametrize
    async def test_raw_response_response_code(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.radar.dns.timeseries_groups.with_raw_response.response_code()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        timeseries_group = await response.parse()
        assert_matches_type(TimeseriesGroupResponseCodeResponse, timeseries_group, path=["response"])

    @parametrize
    async def test_streaming_response_response_code(self, async_client: AsyncCloudflare) -> None:
        async with async_client.radar.dns.timeseries_groups.with_streaming_response.response_code() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            timeseries_group = await response.parse()
            assert_matches_type(TimeseriesGroupResponseCodeResponse, timeseries_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_response_ttl(self, async_client: AsyncCloudflare) -> None:
        timeseries_group = await async_client.radar.dns.timeseries_groups.response_ttl()
        assert_matches_type(TimeseriesGroupResponseTTLResponse, timeseries_group, path=["response"])

    @parametrize
    async def test_method_response_ttl_with_all_params(self, async_client: AsyncCloudflare) -> None:
        timeseries_group = await async_client.radar.dns.timeseries_groups.response_ttl(
            agg_interval="15m",
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
        assert_matches_type(TimeseriesGroupResponseTTLResponse, timeseries_group, path=["response"])

    @parametrize
    async def test_raw_response_response_ttl(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.radar.dns.timeseries_groups.with_raw_response.response_ttl()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        timeseries_group = await response.parse()
        assert_matches_type(TimeseriesGroupResponseTTLResponse, timeseries_group, path=["response"])

    @parametrize
    async def test_streaming_response_response_ttl(self, async_client: AsyncCloudflare) -> None:
        async with async_client.radar.dns.timeseries_groups.with_streaming_response.response_ttl() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            timeseries_group = await response.parse()
            assert_matches_type(TimeseriesGroupResponseTTLResponse, timeseries_group, path=["response"])

        assert cast(Any, response.is_closed) is True
