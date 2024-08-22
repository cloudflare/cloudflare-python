# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from cloudflare import Cloudflare, AsyncCloudflare

from cloudflare.types.radar.attacks.layer3.top import LocationOriginResponse, LocationTargetResponse

from typing import Any, cast

import os
import pytest
import httpx
from typing_extensions import get_args
from typing import Optional
from respx import MockRouter
from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.radar.attacks.layer3.top import location_origin_params
from cloudflare.types.radar.attacks.layer3.top import location_target_params
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

class TestLocations:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=['loose', 'strict'])


    @parametrize
    def test_method_origin(self, client: Cloudflare) -> None:
        location = client.radar.attacks.layer3.top.locations.origin()
        assert_matches_type(LocationOriginResponse, location, path=['response'])

    @parametrize
    def test_method_origin_with_all_params(self, client: Cloudflare) -> None:
        location = client.radar.attacks.layer3.top.locations.origin(
            continent=["string", "string", "string"],
            date_end=[parse_datetime("2019-12-27T18:11:19.117Z"), parse_datetime("2019-12-27T18:11:19.117Z"), parse_datetime("2019-12-27T18:11:19.117Z")],
            date_range=["7d", "7d", "7d"],
            date_start=[parse_datetime("2019-12-27T18:11:19.117Z"), parse_datetime("2019-12-27T18:11:19.117Z"), parse_datetime("2019-12-27T18:11:19.117Z")],
            format="JSON",
            ip_version=["IPv4", "IPv6"],
            limit=5,
            location=["string", "string", "string"],
            name=["string", "string", "string"],
            protocol=["UDP", "TCP", "ICMP"],
        )
        assert_matches_type(LocationOriginResponse, location, path=['response'])

    @parametrize
    def test_raw_response_origin(self, client: Cloudflare) -> None:

        response = client.radar.attacks.layer3.top.locations.with_raw_response.origin()

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        location = response.parse()
        assert_matches_type(LocationOriginResponse, location, path=['response'])

    @parametrize
    def test_streaming_response_origin(self, client: Cloudflare) -> None:
        with client.radar.attacks.layer3.top.locations.with_streaming_response.origin() as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            location = response.parse()
            assert_matches_type(LocationOriginResponse, location, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_target(self, client: Cloudflare) -> None:
        location = client.radar.attacks.layer3.top.locations.target()
        assert_matches_type(LocationTargetResponse, location, path=['response'])

    @parametrize
    def test_method_target_with_all_params(self, client: Cloudflare) -> None:
        location = client.radar.attacks.layer3.top.locations.target(
            continent=["string", "string", "string"],
            date_end=[parse_datetime("2019-12-27T18:11:19.117Z"), parse_datetime("2019-12-27T18:11:19.117Z"), parse_datetime("2019-12-27T18:11:19.117Z")],
            date_range=["7d", "7d", "7d"],
            date_start=[parse_datetime("2019-12-27T18:11:19.117Z"), parse_datetime("2019-12-27T18:11:19.117Z"), parse_datetime("2019-12-27T18:11:19.117Z")],
            format="JSON",
            ip_version=["IPv4", "IPv6"],
            limit=5,
            location=["string", "string", "string"],
            name=["string", "string", "string"],
            protocol=["UDP", "TCP", "ICMP"],
        )
        assert_matches_type(LocationTargetResponse, location, path=['response'])

    @parametrize
    def test_raw_response_target(self, client: Cloudflare) -> None:

        response = client.radar.attacks.layer3.top.locations.with_raw_response.target()

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        location = response.parse()
        assert_matches_type(LocationTargetResponse, location, path=['response'])

    @parametrize
    def test_streaming_response_target(self, client: Cloudflare) -> None:
        with client.radar.attacks.layer3.top.locations.with_streaming_response.target() as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            location = response.parse()
            assert_matches_type(LocationTargetResponse, location, path=['response'])

        assert cast(Any, response.is_closed) is True
class TestAsyncLocations:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=['loose', 'strict'])


    @parametrize
    async def test_method_origin(self, async_client: AsyncCloudflare) -> None:
        location = await async_client.radar.attacks.layer3.top.locations.origin()
        assert_matches_type(LocationOriginResponse, location, path=['response'])

    @parametrize
    async def test_method_origin_with_all_params(self, async_client: AsyncCloudflare) -> None:
        location = await async_client.radar.attacks.layer3.top.locations.origin(
            continent=["string", "string", "string"],
            date_end=[parse_datetime("2019-12-27T18:11:19.117Z"), parse_datetime("2019-12-27T18:11:19.117Z"), parse_datetime("2019-12-27T18:11:19.117Z")],
            date_range=["7d", "7d", "7d"],
            date_start=[parse_datetime("2019-12-27T18:11:19.117Z"), parse_datetime("2019-12-27T18:11:19.117Z"), parse_datetime("2019-12-27T18:11:19.117Z")],
            format="JSON",
            ip_version=["IPv4", "IPv6"],
            limit=5,
            location=["string", "string", "string"],
            name=["string", "string", "string"],
            protocol=["UDP", "TCP", "ICMP"],
        )
        assert_matches_type(LocationOriginResponse, location, path=['response'])

    @parametrize
    async def test_raw_response_origin(self, async_client: AsyncCloudflare) -> None:

        response = await async_client.radar.attacks.layer3.top.locations.with_raw_response.origin()

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        location = await response.parse()
        assert_matches_type(LocationOriginResponse, location, path=['response'])

    @parametrize
    async def test_streaming_response_origin(self, async_client: AsyncCloudflare) -> None:
        async with async_client.radar.attacks.layer3.top.locations.with_streaming_response.origin() as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            location = await response.parse()
            assert_matches_type(LocationOriginResponse, location, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_target(self, async_client: AsyncCloudflare) -> None:
        location = await async_client.radar.attacks.layer3.top.locations.target()
        assert_matches_type(LocationTargetResponse, location, path=['response'])

    @parametrize
    async def test_method_target_with_all_params(self, async_client: AsyncCloudflare) -> None:
        location = await async_client.radar.attacks.layer3.top.locations.target(
            continent=["string", "string", "string"],
            date_end=[parse_datetime("2019-12-27T18:11:19.117Z"), parse_datetime("2019-12-27T18:11:19.117Z"), parse_datetime("2019-12-27T18:11:19.117Z")],
            date_range=["7d", "7d", "7d"],
            date_start=[parse_datetime("2019-12-27T18:11:19.117Z"), parse_datetime("2019-12-27T18:11:19.117Z"), parse_datetime("2019-12-27T18:11:19.117Z")],
            format="JSON",
            ip_version=["IPv4", "IPv6"],
            limit=5,
            location=["string", "string", "string"],
            name=["string", "string", "string"],
            protocol=["UDP", "TCP", "ICMP"],
        )
        assert_matches_type(LocationTargetResponse, location, path=['response'])

    @parametrize
    async def test_raw_response_target(self, async_client: AsyncCloudflare) -> None:

        response = await async_client.radar.attacks.layer3.top.locations.with_raw_response.target()

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        location = await response.parse()
        assert_matches_type(LocationTargetResponse, location, path=['response'])

    @parametrize
    async def test_streaming_response_target(self, async_client: AsyncCloudflare) -> None:
        async with async_client.radar.attacks.layer3.top.locations.with_streaming_response.target() as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            location = await response.parse()
            assert_matches_type(LocationTargetResponse, location, path=['response'])

        assert cast(Any, response.is_closed) is True