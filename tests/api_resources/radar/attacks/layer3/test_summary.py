# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare._utils import parse_datetime
from cloudflare.types.radar.attacks.layer3 import (
    SummaryVectorResponse,
    SummaryBitrateResponse,
    SummaryDurationResponse,
    SummaryProtocolResponse,
    SummaryIPVersionResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSummary:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_bitrate(self, client: Cloudflare) -> None:
        summary = client.radar.attacks.layer3.summary.bitrate()
        assert_matches_type(SummaryBitrateResponse, summary, path=["response"])

    @parametrize
    def test_method_bitrate_with_all_params(self, client: Cloudflare) -> None:
        summary = client.radar.attacks.layer3.summary.bitrate(
            continent=["string"],
            date_end=[parse_datetime("2019-12-27T18:11:19.117Z")],
            date_range=["7d"],
            date_start=[parse_datetime("2019-12-27T18:11:19.117Z")],
            direction="ORIGIN",
            format="JSON",
            ip_version=["IPv4"],
            location=["string"],
            name=["main_series"],
            protocol=["UDP"],
        )
        assert_matches_type(SummaryBitrateResponse, summary, path=["response"])

    @parametrize
    def test_raw_response_bitrate(self, client: Cloudflare) -> None:
        response = client.radar.attacks.layer3.summary.with_raw_response.bitrate()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        summary = response.parse()
        assert_matches_type(SummaryBitrateResponse, summary, path=["response"])

    @parametrize
    def test_streaming_response_bitrate(self, client: Cloudflare) -> None:
        with client.radar.attacks.layer3.summary.with_streaming_response.bitrate() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            summary = response.parse()
            assert_matches_type(SummaryBitrateResponse, summary, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_duration(self, client: Cloudflare) -> None:
        summary = client.radar.attacks.layer3.summary.duration()
        assert_matches_type(SummaryDurationResponse, summary, path=["response"])

    @parametrize
    def test_method_duration_with_all_params(self, client: Cloudflare) -> None:
        summary = client.radar.attacks.layer3.summary.duration(
            continent=["string"],
            date_end=[parse_datetime("2019-12-27T18:11:19.117Z")],
            date_range=["7d"],
            date_start=[parse_datetime("2019-12-27T18:11:19.117Z")],
            direction="ORIGIN",
            format="JSON",
            ip_version=["IPv4"],
            location=["string"],
            name=["main_series"],
            protocol=["UDP"],
        )
        assert_matches_type(SummaryDurationResponse, summary, path=["response"])

    @parametrize
    def test_raw_response_duration(self, client: Cloudflare) -> None:
        response = client.radar.attacks.layer3.summary.with_raw_response.duration()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        summary = response.parse()
        assert_matches_type(SummaryDurationResponse, summary, path=["response"])

    @parametrize
    def test_streaming_response_duration(self, client: Cloudflare) -> None:
        with client.radar.attacks.layer3.summary.with_streaming_response.duration() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            summary = response.parse()
            assert_matches_type(SummaryDurationResponse, summary, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_ip_version(self, client: Cloudflare) -> None:
        summary = client.radar.attacks.layer3.summary.ip_version()
        assert_matches_type(SummaryIPVersionResponse, summary, path=["response"])

    @parametrize
    def test_method_ip_version_with_all_params(self, client: Cloudflare) -> None:
        summary = client.radar.attacks.layer3.summary.ip_version(
            continent=["string"],
            date_end=[parse_datetime("2019-12-27T18:11:19.117Z")],
            date_range=["7d"],
            date_start=[parse_datetime("2019-12-27T18:11:19.117Z")],
            direction="ORIGIN",
            format="JSON",
            location=["string"],
            name=["main_series"],
            protocol=["UDP"],
        )
        assert_matches_type(SummaryIPVersionResponse, summary, path=["response"])

    @parametrize
    def test_raw_response_ip_version(self, client: Cloudflare) -> None:
        response = client.radar.attacks.layer3.summary.with_raw_response.ip_version()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        summary = response.parse()
        assert_matches_type(SummaryIPVersionResponse, summary, path=["response"])

    @parametrize
    def test_streaming_response_ip_version(self, client: Cloudflare) -> None:
        with client.radar.attacks.layer3.summary.with_streaming_response.ip_version() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            summary = response.parse()
            assert_matches_type(SummaryIPVersionResponse, summary, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_protocol(self, client: Cloudflare) -> None:
        summary = client.radar.attacks.layer3.summary.protocol()
        assert_matches_type(SummaryProtocolResponse, summary, path=["response"])

    @parametrize
    def test_method_protocol_with_all_params(self, client: Cloudflare) -> None:
        summary = client.radar.attacks.layer3.summary.protocol(
            continent=["string"],
            date_end=[parse_datetime("2019-12-27T18:11:19.117Z")],
            date_range=["7d"],
            date_start=[parse_datetime("2019-12-27T18:11:19.117Z")],
            direction="ORIGIN",
            format="JSON",
            ip_version=["IPv4"],
            location=["string"],
            name=["main_series"],
        )
        assert_matches_type(SummaryProtocolResponse, summary, path=["response"])

    @parametrize
    def test_raw_response_protocol(self, client: Cloudflare) -> None:
        response = client.radar.attacks.layer3.summary.with_raw_response.protocol()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        summary = response.parse()
        assert_matches_type(SummaryProtocolResponse, summary, path=["response"])

    @parametrize
    def test_streaming_response_protocol(self, client: Cloudflare) -> None:
        with client.radar.attacks.layer3.summary.with_streaming_response.protocol() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            summary = response.parse()
            assert_matches_type(SummaryProtocolResponse, summary, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_vector(self, client: Cloudflare) -> None:
        summary = client.radar.attacks.layer3.summary.vector()
        assert_matches_type(SummaryVectorResponse, summary, path=["response"])

    @parametrize
    def test_method_vector_with_all_params(self, client: Cloudflare) -> None:
        summary = client.radar.attacks.layer3.summary.vector(
            continent=["string"],
            date_end=[parse_datetime("2019-12-27T18:11:19.117Z")],
            date_range=["7d"],
            date_start=[parse_datetime("2019-12-27T18:11:19.117Z")],
            direction="ORIGIN",
            format="JSON",
            ip_version=["IPv4"],
            limit_per_group=10,
            location=["string"],
            name=["main_series"],
            protocol=["UDP"],
        )
        assert_matches_type(SummaryVectorResponse, summary, path=["response"])

    @parametrize
    def test_raw_response_vector(self, client: Cloudflare) -> None:
        response = client.radar.attacks.layer3.summary.with_raw_response.vector()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        summary = response.parse()
        assert_matches_type(SummaryVectorResponse, summary, path=["response"])

    @parametrize
    def test_streaming_response_vector(self, client: Cloudflare) -> None:
        with client.radar.attacks.layer3.summary.with_streaming_response.vector() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            summary = response.parse()
            assert_matches_type(SummaryVectorResponse, summary, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncSummary:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_bitrate(self, async_client: AsyncCloudflare) -> None:
        summary = await async_client.radar.attacks.layer3.summary.bitrate()
        assert_matches_type(SummaryBitrateResponse, summary, path=["response"])

    @parametrize
    async def test_method_bitrate_with_all_params(self, async_client: AsyncCloudflare) -> None:
        summary = await async_client.radar.attacks.layer3.summary.bitrate(
            continent=["string"],
            date_end=[parse_datetime("2019-12-27T18:11:19.117Z")],
            date_range=["7d"],
            date_start=[parse_datetime("2019-12-27T18:11:19.117Z")],
            direction="ORIGIN",
            format="JSON",
            ip_version=["IPv4"],
            location=["string"],
            name=["main_series"],
            protocol=["UDP"],
        )
        assert_matches_type(SummaryBitrateResponse, summary, path=["response"])

    @parametrize
    async def test_raw_response_bitrate(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.radar.attacks.layer3.summary.with_raw_response.bitrate()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        summary = await response.parse()
        assert_matches_type(SummaryBitrateResponse, summary, path=["response"])

    @parametrize
    async def test_streaming_response_bitrate(self, async_client: AsyncCloudflare) -> None:
        async with async_client.radar.attacks.layer3.summary.with_streaming_response.bitrate() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            summary = await response.parse()
            assert_matches_type(SummaryBitrateResponse, summary, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_duration(self, async_client: AsyncCloudflare) -> None:
        summary = await async_client.radar.attacks.layer3.summary.duration()
        assert_matches_type(SummaryDurationResponse, summary, path=["response"])

    @parametrize
    async def test_method_duration_with_all_params(self, async_client: AsyncCloudflare) -> None:
        summary = await async_client.radar.attacks.layer3.summary.duration(
            continent=["string"],
            date_end=[parse_datetime("2019-12-27T18:11:19.117Z")],
            date_range=["7d"],
            date_start=[parse_datetime("2019-12-27T18:11:19.117Z")],
            direction="ORIGIN",
            format="JSON",
            ip_version=["IPv4"],
            location=["string"],
            name=["main_series"],
            protocol=["UDP"],
        )
        assert_matches_type(SummaryDurationResponse, summary, path=["response"])

    @parametrize
    async def test_raw_response_duration(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.radar.attacks.layer3.summary.with_raw_response.duration()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        summary = await response.parse()
        assert_matches_type(SummaryDurationResponse, summary, path=["response"])

    @parametrize
    async def test_streaming_response_duration(self, async_client: AsyncCloudflare) -> None:
        async with async_client.radar.attacks.layer3.summary.with_streaming_response.duration() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            summary = await response.parse()
            assert_matches_type(SummaryDurationResponse, summary, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_ip_version(self, async_client: AsyncCloudflare) -> None:
        summary = await async_client.radar.attacks.layer3.summary.ip_version()
        assert_matches_type(SummaryIPVersionResponse, summary, path=["response"])

    @parametrize
    async def test_method_ip_version_with_all_params(self, async_client: AsyncCloudflare) -> None:
        summary = await async_client.radar.attacks.layer3.summary.ip_version(
            continent=["string"],
            date_end=[parse_datetime("2019-12-27T18:11:19.117Z")],
            date_range=["7d"],
            date_start=[parse_datetime("2019-12-27T18:11:19.117Z")],
            direction="ORIGIN",
            format="JSON",
            location=["string"],
            name=["main_series"],
            protocol=["UDP"],
        )
        assert_matches_type(SummaryIPVersionResponse, summary, path=["response"])

    @parametrize
    async def test_raw_response_ip_version(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.radar.attacks.layer3.summary.with_raw_response.ip_version()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        summary = await response.parse()
        assert_matches_type(SummaryIPVersionResponse, summary, path=["response"])

    @parametrize
    async def test_streaming_response_ip_version(self, async_client: AsyncCloudflare) -> None:
        async with async_client.radar.attacks.layer3.summary.with_streaming_response.ip_version() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            summary = await response.parse()
            assert_matches_type(SummaryIPVersionResponse, summary, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_protocol(self, async_client: AsyncCloudflare) -> None:
        summary = await async_client.radar.attacks.layer3.summary.protocol()
        assert_matches_type(SummaryProtocolResponse, summary, path=["response"])

    @parametrize
    async def test_method_protocol_with_all_params(self, async_client: AsyncCloudflare) -> None:
        summary = await async_client.radar.attacks.layer3.summary.protocol(
            continent=["string"],
            date_end=[parse_datetime("2019-12-27T18:11:19.117Z")],
            date_range=["7d"],
            date_start=[parse_datetime("2019-12-27T18:11:19.117Z")],
            direction="ORIGIN",
            format="JSON",
            ip_version=["IPv4"],
            location=["string"],
            name=["main_series"],
        )
        assert_matches_type(SummaryProtocolResponse, summary, path=["response"])

    @parametrize
    async def test_raw_response_protocol(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.radar.attacks.layer3.summary.with_raw_response.protocol()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        summary = await response.parse()
        assert_matches_type(SummaryProtocolResponse, summary, path=["response"])

    @parametrize
    async def test_streaming_response_protocol(self, async_client: AsyncCloudflare) -> None:
        async with async_client.radar.attacks.layer3.summary.with_streaming_response.protocol() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            summary = await response.parse()
            assert_matches_type(SummaryProtocolResponse, summary, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_vector(self, async_client: AsyncCloudflare) -> None:
        summary = await async_client.radar.attacks.layer3.summary.vector()
        assert_matches_type(SummaryVectorResponse, summary, path=["response"])

    @parametrize
    async def test_method_vector_with_all_params(self, async_client: AsyncCloudflare) -> None:
        summary = await async_client.radar.attacks.layer3.summary.vector(
            continent=["string"],
            date_end=[parse_datetime("2019-12-27T18:11:19.117Z")],
            date_range=["7d"],
            date_start=[parse_datetime("2019-12-27T18:11:19.117Z")],
            direction="ORIGIN",
            format="JSON",
            ip_version=["IPv4"],
            limit_per_group=10,
            location=["string"],
            name=["main_series"],
            protocol=["UDP"],
        )
        assert_matches_type(SummaryVectorResponse, summary, path=["response"])

    @parametrize
    async def test_raw_response_vector(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.radar.attacks.layer3.summary.with_raw_response.vector()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        summary = await response.parse()
        assert_matches_type(SummaryVectorResponse, summary, path=["response"])

    @parametrize
    async def test_streaming_response_vector(self, async_client: AsyncCloudflare) -> None:
        async with async_client.radar.attacks.layer3.summary.with_streaming_response.vector() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            summary = await response.parse()
            assert_matches_type(SummaryVectorResponse, summary, path=["response"])

        assert cast(Any, response.is_closed) is True
