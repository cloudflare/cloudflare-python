# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare._utils import parse_datetime
from cloudflare.types.radar import (
    DNSSummaryV2Response,
    DNSTimeseriesResponse,
    DNSTimeseriesGroupsV2Response,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDNS:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_summary_v2(self, client: Cloudflare) -> None:
        dns = client.radar.dns.summary_v2(
            dimension="IP_VERSION",
        )
        assert_matches_type(DNSSummaryV2Response, dns, path=["response"])

    @parametrize
    def test_method_summary_v2_with_all_params(self, client: Cloudflare) -> None:
        dns = client.radar.dns.summary_v2(
            dimension="IP_VERSION",
            asn=["string"],
            cache_hit=[True],
            continent=["string"],
            date_end=[parse_datetime("2019-12-27T18:11:19.117Z")],
            date_range=["7d"],
            date_start=[parse_datetime("2019-12-27T18:11:19.117Z")],
            dnssec=["INVALID"],
            dnssec_aware=["SUPPORTED"],
            dnssec_e2e=[True],
            format="JSON",
            ip_version=["IPv4"],
            limit_per_group=10,
            location=["string"],
            matching_answer=[True],
            name=["main_series"],
            nodata=[True],
            protocol=["UDP"],
            query_type=["A"],
            response_code=["NOERROR"],
            response_ttl=["LTE_1M"],
            tld=["com"],
        )
        assert_matches_type(DNSSummaryV2Response, dns, path=["response"])

    @parametrize
    def test_raw_response_summary_v2(self, client: Cloudflare) -> None:
        response = client.radar.dns.with_raw_response.summary_v2(
            dimension="IP_VERSION",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dns = response.parse()
        assert_matches_type(DNSSummaryV2Response, dns, path=["response"])

    @parametrize
    def test_streaming_response_summary_v2(self, client: Cloudflare) -> None:
        with client.radar.dns.with_streaming_response.summary_v2(
            dimension="IP_VERSION",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dns = response.parse()
            assert_matches_type(DNSSummaryV2Response, dns, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_timeseries(self, client: Cloudflare) -> None:
        dns = client.radar.dns.timeseries()
        assert_matches_type(DNSTimeseriesResponse, dns, path=["response"])

    @parametrize
    def test_method_timeseries_with_all_params(self, client: Cloudflare) -> None:
        dns = client.radar.dns.timeseries(
            agg_interval="1h",
            asn=["string"],
            cache_hit=[True],
            continent=["string"],
            date_end=[parse_datetime("2019-12-27T18:11:19.117Z")],
            date_range=["7d"],
            date_start=[parse_datetime("2019-12-27T18:11:19.117Z")],
            dnssec=["INVALID"],
            dnssec_aware=["SUPPORTED"],
            dnssec_e2e=[True],
            format="JSON",
            ip_version=["IPv4"],
            location=["string"],
            matching_answer=[True],
            name=["main_series"],
            nodata=[True],
            protocol=["UDP"],
            query_type=["A"],
            response_code=["NOERROR"],
            response_ttl=["LTE_1M"],
            tld=["com"],
        )
        assert_matches_type(DNSTimeseriesResponse, dns, path=["response"])

    @parametrize
    def test_raw_response_timeseries(self, client: Cloudflare) -> None:
        response = client.radar.dns.with_raw_response.timeseries()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dns = response.parse()
        assert_matches_type(DNSTimeseriesResponse, dns, path=["response"])

    @parametrize
    def test_streaming_response_timeseries(self, client: Cloudflare) -> None:
        with client.radar.dns.with_streaming_response.timeseries() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dns = response.parse()
            assert_matches_type(DNSTimeseriesResponse, dns, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_timeseries_groups_v2(self, client: Cloudflare) -> None:
        dns = client.radar.dns.timeseries_groups_v2(
            dimension="IP_VERSION",
        )
        assert_matches_type(DNSTimeseriesGroupsV2Response, dns, path=["response"])

    @parametrize
    def test_method_timeseries_groups_v2_with_all_params(self, client: Cloudflare) -> None:
        dns = client.radar.dns.timeseries_groups_v2(
            dimension="IP_VERSION",
            agg_interval="1h",
            asn=["string"],
            cache_hit=[True],
            continent=["string"],
            date_end=[parse_datetime("2019-12-27T18:11:19.117Z")],
            date_range=["7d"],
            date_start=[parse_datetime("2019-12-27T18:11:19.117Z")],
            dnssec=["INVALID"],
            dnssec_aware=["SUPPORTED"],
            dnssec_e2e=[True],
            format="JSON",
            ip_version=["IPv4"],
            limit_per_group=10,
            location=["string"],
            matching_answer=[True],
            name=["main_series"],
            nodata=[True],
            normalization="PERCENTAGE",
            protocol=["UDP"],
            query_type=["A"],
            response_code=["NOERROR"],
            response_ttl=["LTE_1M"],
            tld=["com"],
        )
        assert_matches_type(DNSTimeseriesGroupsV2Response, dns, path=["response"])

    @parametrize
    def test_raw_response_timeseries_groups_v2(self, client: Cloudflare) -> None:
        response = client.radar.dns.with_raw_response.timeseries_groups_v2(
            dimension="IP_VERSION",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dns = response.parse()
        assert_matches_type(DNSTimeseriesGroupsV2Response, dns, path=["response"])

    @parametrize
    def test_streaming_response_timeseries_groups_v2(self, client: Cloudflare) -> None:
        with client.radar.dns.with_streaming_response.timeseries_groups_v2(
            dimension="IP_VERSION",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dns = response.parse()
            assert_matches_type(DNSTimeseriesGroupsV2Response, dns, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncDNS:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_summary_v2(self, async_client: AsyncCloudflare) -> None:
        dns = await async_client.radar.dns.summary_v2(
            dimension="IP_VERSION",
        )
        assert_matches_type(DNSSummaryV2Response, dns, path=["response"])

    @parametrize
    async def test_method_summary_v2_with_all_params(self, async_client: AsyncCloudflare) -> None:
        dns = await async_client.radar.dns.summary_v2(
            dimension="IP_VERSION",
            asn=["string"],
            cache_hit=[True],
            continent=["string"],
            date_end=[parse_datetime("2019-12-27T18:11:19.117Z")],
            date_range=["7d"],
            date_start=[parse_datetime("2019-12-27T18:11:19.117Z")],
            dnssec=["INVALID"],
            dnssec_aware=["SUPPORTED"],
            dnssec_e2e=[True],
            format="JSON",
            ip_version=["IPv4"],
            limit_per_group=10,
            location=["string"],
            matching_answer=[True],
            name=["main_series"],
            nodata=[True],
            protocol=["UDP"],
            query_type=["A"],
            response_code=["NOERROR"],
            response_ttl=["LTE_1M"],
            tld=["com"],
        )
        assert_matches_type(DNSSummaryV2Response, dns, path=["response"])

    @parametrize
    async def test_raw_response_summary_v2(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.radar.dns.with_raw_response.summary_v2(
            dimension="IP_VERSION",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dns = await response.parse()
        assert_matches_type(DNSSummaryV2Response, dns, path=["response"])

    @parametrize
    async def test_streaming_response_summary_v2(self, async_client: AsyncCloudflare) -> None:
        async with async_client.radar.dns.with_streaming_response.summary_v2(
            dimension="IP_VERSION",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dns = await response.parse()
            assert_matches_type(DNSSummaryV2Response, dns, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_timeseries(self, async_client: AsyncCloudflare) -> None:
        dns = await async_client.radar.dns.timeseries()
        assert_matches_type(DNSTimeseriesResponse, dns, path=["response"])

    @parametrize
    async def test_method_timeseries_with_all_params(self, async_client: AsyncCloudflare) -> None:
        dns = await async_client.radar.dns.timeseries(
            agg_interval="1h",
            asn=["string"],
            cache_hit=[True],
            continent=["string"],
            date_end=[parse_datetime("2019-12-27T18:11:19.117Z")],
            date_range=["7d"],
            date_start=[parse_datetime("2019-12-27T18:11:19.117Z")],
            dnssec=["INVALID"],
            dnssec_aware=["SUPPORTED"],
            dnssec_e2e=[True],
            format="JSON",
            ip_version=["IPv4"],
            location=["string"],
            matching_answer=[True],
            name=["main_series"],
            nodata=[True],
            protocol=["UDP"],
            query_type=["A"],
            response_code=["NOERROR"],
            response_ttl=["LTE_1M"],
            tld=["com"],
        )
        assert_matches_type(DNSTimeseriesResponse, dns, path=["response"])

    @parametrize
    async def test_raw_response_timeseries(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.radar.dns.with_raw_response.timeseries()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dns = await response.parse()
        assert_matches_type(DNSTimeseriesResponse, dns, path=["response"])

    @parametrize
    async def test_streaming_response_timeseries(self, async_client: AsyncCloudflare) -> None:
        async with async_client.radar.dns.with_streaming_response.timeseries() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dns = await response.parse()
            assert_matches_type(DNSTimeseriesResponse, dns, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_timeseries_groups_v2(self, async_client: AsyncCloudflare) -> None:
        dns = await async_client.radar.dns.timeseries_groups_v2(
            dimension="IP_VERSION",
        )
        assert_matches_type(DNSTimeseriesGroupsV2Response, dns, path=["response"])

    @parametrize
    async def test_method_timeseries_groups_v2_with_all_params(self, async_client: AsyncCloudflare) -> None:
        dns = await async_client.radar.dns.timeseries_groups_v2(
            dimension="IP_VERSION",
            agg_interval="1h",
            asn=["string"],
            cache_hit=[True],
            continent=["string"],
            date_end=[parse_datetime("2019-12-27T18:11:19.117Z")],
            date_range=["7d"],
            date_start=[parse_datetime("2019-12-27T18:11:19.117Z")],
            dnssec=["INVALID"],
            dnssec_aware=["SUPPORTED"],
            dnssec_e2e=[True],
            format="JSON",
            ip_version=["IPv4"],
            limit_per_group=10,
            location=["string"],
            matching_answer=[True],
            name=["main_series"],
            nodata=[True],
            normalization="PERCENTAGE",
            protocol=["UDP"],
            query_type=["A"],
            response_code=["NOERROR"],
            response_ttl=["LTE_1M"],
            tld=["com"],
        )
        assert_matches_type(DNSTimeseriesGroupsV2Response, dns, path=["response"])

    @parametrize
    async def test_raw_response_timeseries_groups_v2(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.radar.dns.with_raw_response.timeseries_groups_v2(
            dimension="IP_VERSION",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dns = await response.parse()
        assert_matches_type(DNSTimeseriesGroupsV2Response, dns, path=["response"])

    @parametrize
    async def test_streaming_response_timeseries_groups_v2(self, async_client: AsyncCloudflare) -> None:
        async with async_client.radar.dns.with_streaming_response.timeseries_groups_v2(
            dimension="IP_VERSION",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dns = await response.parse()
            assert_matches_type(DNSTimeseriesGroupsV2Response, dns, path=["response"])

        assert cast(Any, response.is_closed) is True
