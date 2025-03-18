# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare._utils import parse_datetime
from cloudflare.types.radar.as112 import (
    TimeseriesGroupEdnsResponse,
    TimeseriesGroupDNSSECResponse,
    TimeseriesGroupProtocolResponse,
    TimeseriesGroupIPVersionResponse,
    TimeseriesGroupQueryTypeResponse,
    TimeseriesGroupResponseCodesResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTimeseriesGroups:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_dnssec(self, client: Cloudflare) -> None:
        timeseries_group = client.radar.as112.timeseries_groups.dnssec()
        assert_matches_type(TimeseriesGroupDNSSECResponse, timeseries_group, path=["response"])

    @parametrize
    def test_method_dnssec_with_all_params(self, client: Cloudflare) -> None:
        timeseries_group = client.radar.as112.timeseries_groups.dnssec(
            agg_interval="15m",
            asn=["string"],
            continent=["string"],
            date_end=[parse_datetime("2019-12-27T18:11:19.117Z")],
            date_range=["7d"],
            date_start=[parse_datetime("2019-12-27T18:11:19.117Z")],
            format="JSON",
            location=["string"],
            name=["main_series"],
            protocol="UDP",
            query_type="A",
            response_code="NOERROR",
        )
        assert_matches_type(TimeseriesGroupDNSSECResponse, timeseries_group, path=["response"])

    @parametrize
    def test_raw_response_dnssec(self, client: Cloudflare) -> None:
        response = client.radar.as112.timeseries_groups.with_raw_response.dnssec()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        timeseries_group = response.parse()
        assert_matches_type(TimeseriesGroupDNSSECResponse, timeseries_group, path=["response"])

    @parametrize
    def test_streaming_response_dnssec(self, client: Cloudflare) -> None:
        with client.radar.as112.timeseries_groups.with_streaming_response.dnssec() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            timeseries_group = response.parse()
            assert_matches_type(TimeseriesGroupDNSSECResponse, timeseries_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_edns(self, client: Cloudflare) -> None:
        timeseries_group = client.radar.as112.timeseries_groups.edns()
        assert_matches_type(TimeseriesGroupEdnsResponse, timeseries_group, path=["response"])

    @parametrize
    def test_method_edns_with_all_params(self, client: Cloudflare) -> None:
        timeseries_group = client.radar.as112.timeseries_groups.edns(
            agg_interval="15m",
            asn=["string"],
            continent=["string"],
            date_end=[parse_datetime("2019-12-27T18:11:19.117Z")],
            date_range=["7d"],
            date_start=[parse_datetime("2019-12-27T18:11:19.117Z")],
            format="JSON",
            location=["string"],
            name=["main_series"],
            protocol="UDP",
            query_type="A",
            response_code="NOERROR",
        )
        assert_matches_type(TimeseriesGroupEdnsResponse, timeseries_group, path=["response"])

    @parametrize
    def test_raw_response_edns(self, client: Cloudflare) -> None:
        response = client.radar.as112.timeseries_groups.with_raw_response.edns()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        timeseries_group = response.parse()
        assert_matches_type(TimeseriesGroupEdnsResponse, timeseries_group, path=["response"])

    @parametrize
    def test_streaming_response_edns(self, client: Cloudflare) -> None:
        with client.radar.as112.timeseries_groups.with_streaming_response.edns() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            timeseries_group = response.parse()
            assert_matches_type(TimeseriesGroupEdnsResponse, timeseries_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_ip_version(self, client: Cloudflare) -> None:
        timeseries_group = client.radar.as112.timeseries_groups.ip_version()
        assert_matches_type(TimeseriesGroupIPVersionResponse, timeseries_group, path=["response"])

    @parametrize
    def test_method_ip_version_with_all_params(self, client: Cloudflare) -> None:
        timeseries_group = client.radar.as112.timeseries_groups.ip_version(
            agg_interval="15m",
            asn=["string"],
            continent=["string"],
            date_end=[parse_datetime("2019-12-27T18:11:19.117Z")],
            date_range=["7d"],
            date_start=[parse_datetime("2019-12-27T18:11:19.117Z")],
            format="JSON",
            location=["string"],
            name=["main_series"],
            protocol="UDP",
            query_type="A",
            response_code="NOERROR",
        )
        assert_matches_type(TimeseriesGroupIPVersionResponse, timeseries_group, path=["response"])

    @parametrize
    def test_raw_response_ip_version(self, client: Cloudflare) -> None:
        response = client.radar.as112.timeseries_groups.with_raw_response.ip_version()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        timeseries_group = response.parse()
        assert_matches_type(TimeseriesGroupIPVersionResponse, timeseries_group, path=["response"])

    @parametrize
    def test_streaming_response_ip_version(self, client: Cloudflare) -> None:
        with client.radar.as112.timeseries_groups.with_streaming_response.ip_version() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            timeseries_group = response.parse()
            assert_matches_type(TimeseriesGroupIPVersionResponse, timeseries_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_protocol(self, client: Cloudflare) -> None:
        timeseries_group = client.radar.as112.timeseries_groups.protocol()
        assert_matches_type(TimeseriesGroupProtocolResponse, timeseries_group, path=["response"])

    @parametrize
    def test_method_protocol_with_all_params(self, client: Cloudflare) -> None:
        timeseries_group = client.radar.as112.timeseries_groups.protocol(
            agg_interval="15m",
            asn=["string"],
            continent=["string"],
            date_end=[parse_datetime("2019-12-27T18:11:19.117Z")],
            date_range=["7d"],
            date_start=[parse_datetime("2019-12-27T18:11:19.117Z")],
            format="JSON",
            location=["string"],
            name=["main_series"],
            query_type="A",
            response_code="NOERROR",
        )
        assert_matches_type(TimeseriesGroupProtocolResponse, timeseries_group, path=["response"])

    @parametrize
    def test_raw_response_protocol(self, client: Cloudflare) -> None:
        response = client.radar.as112.timeseries_groups.with_raw_response.protocol()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        timeseries_group = response.parse()
        assert_matches_type(TimeseriesGroupProtocolResponse, timeseries_group, path=["response"])

    @parametrize
    def test_streaming_response_protocol(self, client: Cloudflare) -> None:
        with client.radar.as112.timeseries_groups.with_streaming_response.protocol() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            timeseries_group = response.parse()
            assert_matches_type(TimeseriesGroupProtocolResponse, timeseries_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_query_type(self, client: Cloudflare) -> None:
        timeseries_group = client.radar.as112.timeseries_groups.query_type()
        assert_matches_type(TimeseriesGroupQueryTypeResponse, timeseries_group, path=["response"])

    @parametrize
    def test_method_query_type_with_all_params(self, client: Cloudflare) -> None:
        timeseries_group = client.radar.as112.timeseries_groups.query_type(
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
            protocol="UDP",
            response_code="NOERROR",
        )
        assert_matches_type(TimeseriesGroupQueryTypeResponse, timeseries_group, path=["response"])

    @parametrize
    def test_raw_response_query_type(self, client: Cloudflare) -> None:
        response = client.radar.as112.timeseries_groups.with_raw_response.query_type()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        timeseries_group = response.parse()
        assert_matches_type(TimeseriesGroupQueryTypeResponse, timeseries_group, path=["response"])

    @parametrize
    def test_streaming_response_query_type(self, client: Cloudflare) -> None:
        with client.radar.as112.timeseries_groups.with_streaming_response.query_type() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            timeseries_group = response.parse()
            assert_matches_type(TimeseriesGroupQueryTypeResponse, timeseries_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_response_codes(self, client: Cloudflare) -> None:
        timeseries_group = client.radar.as112.timeseries_groups.response_codes()
        assert_matches_type(TimeseriesGroupResponseCodesResponse, timeseries_group, path=["response"])

    @parametrize
    def test_method_response_codes_with_all_params(self, client: Cloudflare) -> None:
        timeseries_group = client.radar.as112.timeseries_groups.response_codes(
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
            protocol="UDP",
            query_type="A",
        )
        assert_matches_type(TimeseriesGroupResponseCodesResponse, timeseries_group, path=["response"])

    @parametrize
    def test_raw_response_response_codes(self, client: Cloudflare) -> None:
        response = client.radar.as112.timeseries_groups.with_raw_response.response_codes()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        timeseries_group = response.parse()
        assert_matches_type(TimeseriesGroupResponseCodesResponse, timeseries_group, path=["response"])

    @parametrize
    def test_streaming_response_response_codes(self, client: Cloudflare) -> None:
        with client.radar.as112.timeseries_groups.with_streaming_response.response_codes() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            timeseries_group = response.parse()
            assert_matches_type(TimeseriesGroupResponseCodesResponse, timeseries_group, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncTimeseriesGroups:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_dnssec(self, async_client: AsyncCloudflare) -> None:
        timeseries_group = await async_client.radar.as112.timeseries_groups.dnssec()
        assert_matches_type(TimeseriesGroupDNSSECResponse, timeseries_group, path=["response"])

    @parametrize
    async def test_method_dnssec_with_all_params(self, async_client: AsyncCloudflare) -> None:
        timeseries_group = await async_client.radar.as112.timeseries_groups.dnssec(
            agg_interval="15m",
            asn=["string"],
            continent=["string"],
            date_end=[parse_datetime("2019-12-27T18:11:19.117Z")],
            date_range=["7d"],
            date_start=[parse_datetime("2019-12-27T18:11:19.117Z")],
            format="JSON",
            location=["string"],
            name=["main_series"],
            protocol="UDP",
            query_type="A",
            response_code="NOERROR",
        )
        assert_matches_type(TimeseriesGroupDNSSECResponse, timeseries_group, path=["response"])

    @parametrize
    async def test_raw_response_dnssec(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.radar.as112.timeseries_groups.with_raw_response.dnssec()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        timeseries_group = await response.parse()
        assert_matches_type(TimeseriesGroupDNSSECResponse, timeseries_group, path=["response"])

    @parametrize
    async def test_streaming_response_dnssec(self, async_client: AsyncCloudflare) -> None:
        async with async_client.radar.as112.timeseries_groups.with_streaming_response.dnssec() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            timeseries_group = await response.parse()
            assert_matches_type(TimeseriesGroupDNSSECResponse, timeseries_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_edns(self, async_client: AsyncCloudflare) -> None:
        timeseries_group = await async_client.radar.as112.timeseries_groups.edns()
        assert_matches_type(TimeseriesGroupEdnsResponse, timeseries_group, path=["response"])

    @parametrize
    async def test_method_edns_with_all_params(self, async_client: AsyncCloudflare) -> None:
        timeseries_group = await async_client.radar.as112.timeseries_groups.edns(
            agg_interval="15m",
            asn=["string"],
            continent=["string"],
            date_end=[parse_datetime("2019-12-27T18:11:19.117Z")],
            date_range=["7d"],
            date_start=[parse_datetime("2019-12-27T18:11:19.117Z")],
            format="JSON",
            location=["string"],
            name=["main_series"],
            protocol="UDP",
            query_type="A",
            response_code="NOERROR",
        )
        assert_matches_type(TimeseriesGroupEdnsResponse, timeseries_group, path=["response"])

    @parametrize
    async def test_raw_response_edns(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.radar.as112.timeseries_groups.with_raw_response.edns()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        timeseries_group = await response.parse()
        assert_matches_type(TimeseriesGroupEdnsResponse, timeseries_group, path=["response"])

    @parametrize
    async def test_streaming_response_edns(self, async_client: AsyncCloudflare) -> None:
        async with async_client.radar.as112.timeseries_groups.with_streaming_response.edns() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            timeseries_group = await response.parse()
            assert_matches_type(TimeseriesGroupEdnsResponse, timeseries_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_ip_version(self, async_client: AsyncCloudflare) -> None:
        timeseries_group = await async_client.radar.as112.timeseries_groups.ip_version()
        assert_matches_type(TimeseriesGroupIPVersionResponse, timeseries_group, path=["response"])

    @parametrize
    async def test_method_ip_version_with_all_params(self, async_client: AsyncCloudflare) -> None:
        timeseries_group = await async_client.radar.as112.timeseries_groups.ip_version(
            agg_interval="15m",
            asn=["string"],
            continent=["string"],
            date_end=[parse_datetime("2019-12-27T18:11:19.117Z")],
            date_range=["7d"],
            date_start=[parse_datetime("2019-12-27T18:11:19.117Z")],
            format="JSON",
            location=["string"],
            name=["main_series"],
            protocol="UDP",
            query_type="A",
            response_code="NOERROR",
        )
        assert_matches_type(TimeseriesGroupIPVersionResponse, timeseries_group, path=["response"])

    @parametrize
    async def test_raw_response_ip_version(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.radar.as112.timeseries_groups.with_raw_response.ip_version()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        timeseries_group = await response.parse()
        assert_matches_type(TimeseriesGroupIPVersionResponse, timeseries_group, path=["response"])

    @parametrize
    async def test_streaming_response_ip_version(self, async_client: AsyncCloudflare) -> None:
        async with async_client.radar.as112.timeseries_groups.with_streaming_response.ip_version() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            timeseries_group = await response.parse()
            assert_matches_type(TimeseriesGroupIPVersionResponse, timeseries_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_protocol(self, async_client: AsyncCloudflare) -> None:
        timeseries_group = await async_client.radar.as112.timeseries_groups.protocol()
        assert_matches_type(TimeseriesGroupProtocolResponse, timeseries_group, path=["response"])

    @parametrize
    async def test_method_protocol_with_all_params(self, async_client: AsyncCloudflare) -> None:
        timeseries_group = await async_client.radar.as112.timeseries_groups.protocol(
            agg_interval="15m",
            asn=["string"],
            continent=["string"],
            date_end=[parse_datetime("2019-12-27T18:11:19.117Z")],
            date_range=["7d"],
            date_start=[parse_datetime("2019-12-27T18:11:19.117Z")],
            format="JSON",
            location=["string"],
            name=["main_series"],
            query_type="A",
            response_code="NOERROR",
        )
        assert_matches_type(TimeseriesGroupProtocolResponse, timeseries_group, path=["response"])

    @parametrize
    async def test_raw_response_protocol(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.radar.as112.timeseries_groups.with_raw_response.protocol()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        timeseries_group = await response.parse()
        assert_matches_type(TimeseriesGroupProtocolResponse, timeseries_group, path=["response"])

    @parametrize
    async def test_streaming_response_protocol(self, async_client: AsyncCloudflare) -> None:
        async with async_client.radar.as112.timeseries_groups.with_streaming_response.protocol() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            timeseries_group = await response.parse()
            assert_matches_type(TimeseriesGroupProtocolResponse, timeseries_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_query_type(self, async_client: AsyncCloudflare) -> None:
        timeseries_group = await async_client.radar.as112.timeseries_groups.query_type()
        assert_matches_type(TimeseriesGroupQueryTypeResponse, timeseries_group, path=["response"])

    @parametrize
    async def test_method_query_type_with_all_params(self, async_client: AsyncCloudflare) -> None:
        timeseries_group = await async_client.radar.as112.timeseries_groups.query_type(
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
            protocol="UDP",
            response_code="NOERROR",
        )
        assert_matches_type(TimeseriesGroupQueryTypeResponse, timeseries_group, path=["response"])

    @parametrize
    async def test_raw_response_query_type(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.radar.as112.timeseries_groups.with_raw_response.query_type()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        timeseries_group = await response.parse()
        assert_matches_type(TimeseriesGroupQueryTypeResponse, timeseries_group, path=["response"])

    @parametrize
    async def test_streaming_response_query_type(self, async_client: AsyncCloudflare) -> None:
        async with async_client.radar.as112.timeseries_groups.with_streaming_response.query_type() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            timeseries_group = await response.parse()
            assert_matches_type(TimeseriesGroupQueryTypeResponse, timeseries_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_response_codes(self, async_client: AsyncCloudflare) -> None:
        timeseries_group = await async_client.radar.as112.timeseries_groups.response_codes()
        assert_matches_type(TimeseriesGroupResponseCodesResponse, timeseries_group, path=["response"])

    @parametrize
    async def test_method_response_codes_with_all_params(self, async_client: AsyncCloudflare) -> None:
        timeseries_group = await async_client.radar.as112.timeseries_groups.response_codes(
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
            protocol="UDP",
            query_type="A",
        )
        assert_matches_type(TimeseriesGroupResponseCodesResponse, timeseries_group, path=["response"])

    @parametrize
    async def test_raw_response_response_codes(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.radar.as112.timeseries_groups.with_raw_response.response_codes()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        timeseries_group = await response.parse()
        assert_matches_type(TimeseriesGroupResponseCodesResponse, timeseries_group, path=["response"])

    @parametrize
    async def test_streaming_response_response_codes(self, async_client: AsyncCloudflare) -> None:
        async with async_client.radar.as112.timeseries_groups.with_streaming_response.response_codes() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            timeseries_group = await response.parse()
            assert_matches_type(TimeseriesGroupResponseCodesResponse, timeseries_group, path=["response"])

        assert cast(Any, response.is_closed) is True
