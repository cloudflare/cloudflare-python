# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare._utils import parse_datetime
from cloudflare.types.radar.as112 import (
    TopEdnsResponse,
    TopDNSSECResponse,
    TopIPVersionResponse,
    TopLocationsResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTop:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_dnssec(self, client: Cloudflare) -> None:
        top = client.radar.as112.top.dnssec(
            dnssec="SUPPORTED",
        )
        assert_matches_type(TopDNSSECResponse, top, path=["response"])

    @parametrize
    def test_method_dnssec_with_all_params(self, client: Cloudflare) -> None:
        top = client.radar.as112.top.dnssec(
            dnssec="SUPPORTED",
            asn=["string"],
            continent=["string"],
            date_end=[parse_datetime("2019-12-27T18:11:19.117Z")],
            date_range=["7d"],
            date_start=[parse_datetime("2019-12-27T18:11:19.117Z")],
            format="JSON",
            limit=5,
            location=["string"],
            name=["main_series"],
        )
        assert_matches_type(TopDNSSECResponse, top, path=["response"])

    @parametrize
    def test_raw_response_dnssec(self, client: Cloudflare) -> None:
        response = client.radar.as112.top.with_raw_response.dnssec(
            dnssec="SUPPORTED",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        top = response.parse()
        assert_matches_type(TopDNSSECResponse, top, path=["response"])

    @parametrize
    def test_streaming_response_dnssec(self, client: Cloudflare) -> None:
        with client.radar.as112.top.with_streaming_response.dnssec(
            dnssec="SUPPORTED",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            top = response.parse()
            assert_matches_type(TopDNSSECResponse, top, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_edns(self, client: Cloudflare) -> None:
        top = client.radar.as112.top.edns(
            edns="SUPPORTED",
        )
        assert_matches_type(TopEdnsResponse, top, path=["response"])

    @parametrize
    def test_method_edns_with_all_params(self, client: Cloudflare) -> None:
        top = client.radar.as112.top.edns(
            edns="SUPPORTED",
            asn=["string"],
            continent=["string"],
            date_end=[parse_datetime("2019-12-27T18:11:19.117Z")],
            date_range=["7d"],
            date_start=[parse_datetime("2019-12-27T18:11:19.117Z")],
            format="JSON",
            limit=5,
            location=["string"],
            name=["main_series"],
        )
        assert_matches_type(TopEdnsResponse, top, path=["response"])

    @parametrize
    def test_raw_response_edns(self, client: Cloudflare) -> None:
        response = client.radar.as112.top.with_raw_response.edns(
            edns="SUPPORTED",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        top = response.parse()
        assert_matches_type(TopEdnsResponse, top, path=["response"])

    @parametrize
    def test_streaming_response_edns(self, client: Cloudflare) -> None:
        with client.radar.as112.top.with_streaming_response.edns(
            edns="SUPPORTED",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            top = response.parse()
            assert_matches_type(TopEdnsResponse, top, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_ip_version(self, client: Cloudflare) -> None:
        top = client.radar.as112.top.ip_version(
            ip_version="IPv4",
        )
        assert_matches_type(TopIPVersionResponse, top, path=["response"])

    @parametrize
    def test_method_ip_version_with_all_params(self, client: Cloudflare) -> None:
        top = client.radar.as112.top.ip_version(
            ip_version="IPv4",
            asn=["string"],
            continent=["string"],
            date_end=[parse_datetime("2019-12-27T18:11:19.117Z")],
            date_range=["7d"],
            date_start=[parse_datetime("2019-12-27T18:11:19.117Z")],
            format="JSON",
            limit=5,
            location=["string"],
            name=["main_series"],
        )
        assert_matches_type(TopIPVersionResponse, top, path=["response"])

    @parametrize
    def test_raw_response_ip_version(self, client: Cloudflare) -> None:
        response = client.radar.as112.top.with_raw_response.ip_version(
            ip_version="IPv4",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        top = response.parse()
        assert_matches_type(TopIPVersionResponse, top, path=["response"])

    @parametrize
    def test_streaming_response_ip_version(self, client: Cloudflare) -> None:
        with client.radar.as112.top.with_streaming_response.ip_version(
            ip_version="IPv4",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            top = response.parse()
            assert_matches_type(TopIPVersionResponse, top, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_locations(self, client: Cloudflare) -> None:
        top = client.radar.as112.top.locations()
        assert_matches_type(TopLocationsResponse, top, path=["response"])

    @parametrize
    def test_method_locations_with_all_params(self, client: Cloudflare) -> None:
        top = client.radar.as112.top.locations(
            asn=["string"],
            continent=["string"],
            date_end=[parse_datetime("2019-12-27T18:11:19.117Z")],
            date_range=["7d"],
            date_start=[parse_datetime("2019-12-27T18:11:19.117Z")],
            format="JSON",
            limit=5,
            location=["string"],
            name=["main_series"],
        )
        assert_matches_type(TopLocationsResponse, top, path=["response"])

    @parametrize
    def test_raw_response_locations(self, client: Cloudflare) -> None:
        response = client.radar.as112.top.with_raw_response.locations()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        top = response.parse()
        assert_matches_type(TopLocationsResponse, top, path=["response"])

    @parametrize
    def test_streaming_response_locations(self, client: Cloudflare) -> None:
        with client.radar.as112.top.with_streaming_response.locations() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            top = response.parse()
            assert_matches_type(TopLocationsResponse, top, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncTop:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_dnssec(self, async_client: AsyncCloudflare) -> None:
        top = await async_client.radar.as112.top.dnssec(
            dnssec="SUPPORTED",
        )
        assert_matches_type(TopDNSSECResponse, top, path=["response"])

    @parametrize
    async def test_method_dnssec_with_all_params(self, async_client: AsyncCloudflare) -> None:
        top = await async_client.radar.as112.top.dnssec(
            dnssec="SUPPORTED",
            asn=["string"],
            continent=["string"],
            date_end=[parse_datetime("2019-12-27T18:11:19.117Z")],
            date_range=["7d"],
            date_start=[parse_datetime("2019-12-27T18:11:19.117Z")],
            format="JSON",
            limit=5,
            location=["string"],
            name=["main_series"],
        )
        assert_matches_type(TopDNSSECResponse, top, path=["response"])

    @parametrize
    async def test_raw_response_dnssec(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.radar.as112.top.with_raw_response.dnssec(
            dnssec="SUPPORTED",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        top = await response.parse()
        assert_matches_type(TopDNSSECResponse, top, path=["response"])

    @parametrize
    async def test_streaming_response_dnssec(self, async_client: AsyncCloudflare) -> None:
        async with async_client.radar.as112.top.with_streaming_response.dnssec(
            dnssec="SUPPORTED",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            top = await response.parse()
            assert_matches_type(TopDNSSECResponse, top, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_edns(self, async_client: AsyncCloudflare) -> None:
        top = await async_client.radar.as112.top.edns(
            edns="SUPPORTED",
        )
        assert_matches_type(TopEdnsResponse, top, path=["response"])

    @parametrize
    async def test_method_edns_with_all_params(self, async_client: AsyncCloudflare) -> None:
        top = await async_client.radar.as112.top.edns(
            edns="SUPPORTED",
            asn=["string"],
            continent=["string"],
            date_end=[parse_datetime("2019-12-27T18:11:19.117Z")],
            date_range=["7d"],
            date_start=[parse_datetime("2019-12-27T18:11:19.117Z")],
            format="JSON",
            limit=5,
            location=["string"],
            name=["main_series"],
        )
        assert_matches_type(TopEdnsResponse, top, path=["response"])

    @parametrize
    async def test_raw_response_edns(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.radar.as112.top.with_raw_response.edns(
            edns="SUPPORTED",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        top = await response.parse()
        assert_matches_type(TopEdnsResponse, top, path=["response"])

    @parametrize
    async def test_streaming_response_edns(self, async_client: AsyncCloudflare) -> None:
        async with async_client.radar.as112.top.with_streaming_response.edns(
            edns="SUPPORTED",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            top = await response.parse()
            assert_matches_type(TopEdnsResponse, top, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_ip_version(self, async_client: AsyncCloudflare) -> None:
        top = await async_client.radar.as112.top.ip_version(
            ip_version="IPv4",
        )
        assert_matches_type(TopIPVersionResponse, top, path=["response"])

    @parametrize
    async def test_method_ip_version_with_all_params(self, async_client: AsyncCloudflare) -> None:
        top = await async_client.radar.as112.top.ip_version(
            ip_version="IPv4",
            asn=["string"],
            continent=["string"],
            date_end=[parse_datetime("2019-12-27T18:11:19.117Z")],
            date_range=["7d"],
            date_start=[parse_datetime("2019-12-27T18:11:19.117Z")],
            format="JSON",
            limit=5,
            location=["string"],
            name=["main_series"],
        )
        assert_matches_type(TopIPVersionResponse, top, path=["response"])

    @parametrize
    async def test_raw_response_ip_version(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.radar.as112.top.with_raw_response.ip_version(
            ip_version="IPv4",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        top = await response.parse()
        assert_matches_type(TopIPVersionResponse, top, path=["response"])

    @parametrize
    async def test_streaming_response_ip_version(self, async_client: AsyncCloudflare) -> None:
        async with async_client.radar.as112.top.with_streaming_response.ip_version(
            ip_version="IPv4",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            top = await response.parse()
            assert_matches_type(TopIPVersionResponse, top, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_locations(self, async_client: AsyncCloudflare) -> None:
        top = await async_client.radar.as112.top.locations()
        assert_matches_type(TopLocationsResponse, top, path=["response"])

    @parametrize
    async def test_method_locations_with_all_params(self, async_client: AsyncCloudflare) -> None:
        top = await async_client.radar.as112.top.locations(
            asn=["string"],
            continent=["string"],
            date_end=[parse_datetime("2019-12-27T18:11:19.117Z")],
            date_range=["7d"],
            date_start=[parse_datetime("2019-12-27T18:11:19.117Z")],
            format="JSON",
            limit=5,
            location=["string"],
            name=["main_series"],
        )
        assert_matches_type(TopLocationsResponse, top, path=["response"])

    @parametrize
    async def test_raw_response_locations(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.radar.as112.top.with_raw_response.locations()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        top = await response.parse()
        assert_matches_type(TopLocationsResponse, top, path=["response"])

    @parametrize
    async def test_streaming_response_locations(self, async_client: AsyncCloudflare) -> None:
        async with async_client.radar.as112.top.with_streaming_response.locations() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            top = await response.parse()
            assert_matches_type(TopLocationsResponse, top, path=["response"])

        assert cast(Any, response.is_closed) is True
