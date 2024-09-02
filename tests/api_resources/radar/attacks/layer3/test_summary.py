# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from cloudflare import Cloudflare, AsyncCloudflare

from cloudflare.types.radar.attacks.layer3 import (
    SummaryBitrateResponse,
    SummaryDurationResponse,
    SummaryGetResponse,
    SummaryIPVersionResponse,
    SummaryProtocolResponse,
    SummaryVectorResponse,
)

from typing import Any, cast

import os
import pytest
import httpx
from typing_extensions import get_args
from typing import Optional
from respx import MockRouter
from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.radar.attacks.layer3 import summary_bitrate_params
from cloudflare.types.radar.attacks.layer3 import summary_duration_params
from cloudflare.types.radar.attacks.layer3 import summary_get_params
from cloudflare.types.radar.attacks.layer3 import summary_ip_version_params
from cloudflare.types.radar.attacks.layer3 import summary_protocol_params
from cloudflare.types.radar.attacks.layer3 import summary_vector_params
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime

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
            continent=["string", "string", "string"],
            date_end=[
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
            ],
            date_range=["7d", "7d", "7d"],
            date_start=[
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
            ],
            direction="ORIGIN",
            format="JSON",
            ip_version=["IPv4", "IPv6"],
            location=["string", "string", "string"],
            name=["string", "string", "string"],
            protocol=["UDP", "TCP", "ICMP"],
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
            continent=["string", "string", "string"],
            date_end=[
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
            ],
            date_range=["7d", "7d", "7d"],
            date_start=[
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
            ],
            direction="ORIGIN",
            format="JSON",
            ip_version=["IPv4", "IPv6"],
            location=["string", "string", "string"],
            name=["string", "string", "string"],
            protocol=["UDP", "TCP", "ICMP"],
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
    def test_method_get(self, client: Cloudflare) -> None:
        summary = client.radar.attacks.layer3.summary.get()
        assert_matches_type(SummaryGetResponse, summary, path=["response"])

    @parametrize
    def test_method_get_with_all_params(self, client: Cloudflare) -> None:
        summary = client.radar.attacks.layer3.summary.get(
            asn=["string", "string", "string"],
            continent=["string", "string", "string"],
            date_end=[
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
            ],
            date_range=["7d", "7d", "7d"],
            date_start=[
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
            ],
            format="JSON",
            location=["string", "string", "string"],
            name=["string", "string", "string"],
        )
        assert_matches_type(SummaryGetResponse, summary, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.radar.attacks.layer3.summary.with_raw_response.get()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        summary = response.parse()
        assert_matches_type(SummaryGetResponse, summary, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.radar.attacks.layer3.summary.with_streaming_response.get() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            summary = response.parse()
            assert_matches_type(SummaryGetResponse, summary, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_ip_version(self, client: Cloudflare) -> None:
        summary = client.radar.attacks.layer3.summary.ip_version()
        assert_matches_type(SummaryIPVersionResponse, summary, path=["response"])

    @parametrize
    def test_method_ip_version_with_all_params(self, client: Cloudflare) -> None:
        summary = client.radar.attacks.layer3.summary.ip_version(
            continent=["string", "string", "string"],
            date_end=[
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
            ],
            date_range=["7d", "7d", "7d"],
            date_start=[
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
            ],
            direction="ORIGIN",
            format="JSON",
            location=["string", "string", "string"],
            name=["string", "string", "string"],
            protocol=["UDP", "TCP", "ICMP"],
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
            continent=["string", "string", "string"],
            date_end=[
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
            ],
            date_range=["7d", "7d", "7d"],
            date_start=[
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
            ],
            direction="ORIGIN",
            format="JSON",
            ip_version=["IPv4", "IPv6"],
            location=["string", "string", "string"],
            name=["string", "string", "string"],
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
            continent=["string", "string", "string"],
            date_end=[
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
            ],
            date_range=["7d", "7d", "7d"],
            date_start=[
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
            ],
            direction="ORIGIN",
            format="JSON",
            ip_version=["IPv4", "IPv6"],
            location=["string", "string", "string"],
            name=["string", "string", "string"],
            protocol=["UDP", "TCP", "ICMP"],
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
            continent=["string", "string", "string"],
            date_end=[
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
            ],
            date_range=["7d", "7d", "7d"],
            date_start=[
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
            ],
            direction="ORIGIN",
            format="JSON",
            ip_version=["IPv4", "IPv6"],
            location=["string", "string", "string"],
            name=["string", "string", "string"],
            protocol=["UDP", "TCP", "ICMP"],
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
            continent=["string", "string", "string"],
            date_end=[
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
            ],
            date_range=["7d", "7d", "7d"],
            date_start=[
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
            ],
            direction="ORIGIN",
            format="JSON",
            ip_version=["IPv4", "IPv6"],
            location=["string", "string", "string"],
            name=["string", "string", "string"],
            protocol=["UDP", "TCP", "ICMP"],
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
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        summary = await async_client.radar.attacks.layer3.summary.get()
        assert_matches_type(SummaryGetResponse, summary, path=["response"])

    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncCloudflare) -> None:
        summary = await async_client.radar.attacks.layer3.summary.get(
            asn=["string", "string", "string"],
            continent=["string", "string", "string"],
            date_end=[
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
            ],
            date_range=["7d", "7d", "7d"],
            date_start=[
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
            ],
            format="JSON",
            location=["string", "string", "string"],
            name=["string", "string", "string"],
        )
        assert_matches_type(SummaryGetResponse, summary, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.radar.attacks.layer3.summary.with_raw_response.get()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        summary = await response.parse()
        assert_matches_type(SummaryGetResponse, summary, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.radar.attacks.layer3.summary.with_streaming_response.get() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            summary = await response.parse()
            assert_matches_type(SummaryGetResponse, summary, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_ip_version(self, async_client: AsyncCloudflare) -> None:
        summary = await async_client.radar.attacks.layer3.summary.ip_version()
        assert_matches_type(SummaryIPVersionResponse, summary, path=["response"])

    @parametrize
    async def test_method_ip_version_with_all_params(self, async_client: AsyncCloudflare) -> None:
        summary = await async_client.radar.attacks.layer3.summary.ip_version(
            continent=["string", "string", "string"],
            date_end=[
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
            ],
            date_range=["7d", "7d", "7d"],
            date_start=[
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
            ],
            direction="ORIGIN",
            format="JSON",
            location=["string", "string", "string"],
            name=["string", "string", "string"],
            protocol=["UDP", "TCP", "ICMP"],
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
            continent=["string", "string", "string"],
            date_end=[
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
            ],
            date_range=["7d", "7d", "7d"],
            date_start=[
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
            ],
            direction="ORIGIN",
            format="JSON",
            ip_version=["IPv4", "IPv6"],
            location=["string", "string", "string"],
            name=["string", "string", "string"],
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
            continent=["string", "string", "string"],
            date_end=[
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
            ],
            date_range=["7d", "7d", "7d"],
            date_start=[
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
            ],
            direction="ORIGIN",
            format="JSON",
            ip_version=["IPv4", "IPv6"],
            location=["string", "string", "string"],
            name=["string", "string", "string"],
            protocol=["UDP", "TCP", "ICMP"],
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
