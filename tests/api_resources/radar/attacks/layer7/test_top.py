# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from cloudflare import Cloudflare, AsyncCloudflare

from cloudflare.types.radar.attacks.layer7 import TopAttacksResponse, TopIndustryResponse, TopVerticalResponse

from typing import Any, cast

import os
import pytest
import httpx
from typing_extensions import get_args
from typing import Optional
from respx import MockRouter
from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.radar.attacks.layer7 import top_attacks_params
from cloudflare.types.radar.attacks.layer7 import top_industry_params
from cloudflare.types.radar.attacks.layer7 import top_vertical_params
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

class TestTop:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=['loose', 'strict'])


    @parametrize
    def test_method_attacks(self, client: Cloudflare) -> None:
        top = client.radar.attacks.layer7.top.attacks()
        assert_matches_type(TopAttacksResponse, top, path=['response'])

    @parametrize
    def test_method_attacks_with_all_params(self, client: Cloudflare) -> None:
        top = client.radar.attacks.layer7.top.attacks(
            asn=["string", "string", "string"],
            continent=["string", "string", "string"],
            date_end=[parse_datetime("2019-12-27T18:11:19.117Z"), parse_datetime("2019-12-27T18:11:19.117Z"), parse_datetime("2019-12-27T18:11:19.117Z")],
            date_range=["7d", "7d", "7d"],
            date_start=[parse_datetime("2019-12-27T18:11:19.117Z"), parse_datetime("2019-12-27T18:11:19.117Z"), parse_datetime("2019-12-27T18:11:19.117Z")],
            format="JSON",
            http_method=["GET", "POST", "DELETE"],
            http_version=["HTTPv1", "HTTPv2", "HTTPv3"],
            ip_version=["IPv4", "IPv6"],
            limit=5,
            limit_direction="ORIGIN",
            limit_per_location=10,
            location=["string", "string", "string"],
            magnitude="AFFECTED_ZONES",
            mitigation_product=["DDOS", "WAF", "BOT_MANAGEMENT"],
            name=["string", "string", "string"],
            normalization="PERCENTAGE",
        )
        assert_matches_type(TopAttacksResponse, top, path=['response'])

    @parametrize
    def test_raw_response_attacks(self, client: Cloudflare) -> None:

        response = client.radar.attacks.layer7.top.with_raw_response.attacks()

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        top = response.parse()
        assert_matches_type(TopAttacksResponse, top, path=['response'])

    @parametrize
    def test_streaming_response_attacks(self, client: Cloudflare) -> None:
        with client.radar.attacks.layer7.top.with_streaming_response.attacks() as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            top = response.parse()
            assert_matches_type(TopAttacksResponse, top, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_industry(self, client: Cloudflare) -> None:
        top = client.radar.attacks.layer7.top.industry()
        assert_matches_type(TopIndustryResponse, top, path=['response'])

    @parametrize
    def test_method_industry_with_all_params(self, client: Cloudflare) -> None:
        top = client.radar.attacks.layer7.top.industry(
            asn=["string", "string", "string"],
            continent=["string", "string", "string"],
            date_end=[parse_datetime("2019-12-27T18:11:19.117Z"), parse_datetime("2019-12-27T18:11:19.117Z"), parse_datetime("2019-12-27T18:11:19.117Z")],
            date_range=["7d", "7d", "7d"],
            date_start=[parse_datetime("2019-12-27T18:11:19.117Z"), parse_datetime("2019-12-27T18:11:19.117Z"), parse_datetime("2019-12-27T18:11:19.117Z")],
            format="JSON",
            http_method=["GET", "POST", "DELETE"],
            http_version=["HTTPv1", "HTTPv2", "HTTPv3"],
            ip_version=["IPv4", "IPv6"],
            limit=5,
            location=["string", "string", "string"],
            mitigation_product=["DDOS", "WAF", "BOT_MANAGEMENT"],
            name=["string", "string", "string"],
        )
        assert_matches_type(TopIndustryResponse, top, path=['response'])

    @parametrize
    def test_raw_response_industry(self, client: Cloudflare) -> None:

        response = client.radar.attacks.layer7.top.with_raw_response.industry()

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        top = response.parse()
        assert_matches_type(TopIndustryResponse, top, path=['response'])

    @parametrize
    def test_streaming_response_industry(self, client: Cloudflare) -> None:
        with client.radar.attacks.layer7.top.with_streaming_response.industry() as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            top = response.parse()
            assert_matches_type(TopIndustryResponse, top, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_vertical(self, client: Cloudflare) -> None:
        top = client.radar.attacks.layer7.top.vertical()
        assert_matches_type(TopVerticalResponse, top, path=['response'])

    @parametrize
    def test_method_vertical_with_all_params(self, client: Cloudflare) -> None:
        top = client.radar.attacks.layer7.top.vertical(
            asn=["string", "string", "string"],
            continent=["string", "string", "string"],
            date_end=[parse_datetime("2019-12-27T18:11:19.117Z"), parse_datetime("2019-12-27T18:11:19.117Z"), parse_datetime("2019-12-27T18:11:19.117Z")],
            date_range=["7d", "7d", "7d"],
            date_start=[parse_datetime("2019-12-27T18:11:19.117Z"), parse_datetime("2019-12-27T18:11:19.117Z"), parse_datetime("2019-12-27T18:11:19.117Z")],
            format="JSON",
            http_method=["GET", "POST", "DELETE"],
            http_version=["HTTPv1", "HTTPv2", "HTTPv3"],
            ip_version=["IPv4", "IPv6"],
            limit=5,
            location=["string", "string", "string"],
            mitigation_product=["DDOS", "WAF", "BOT_MANAGEMENT"],
            name=["string", "string", "string"],
        )
        assert_matches_type(TopVerticalResponse, top, path=['response'])

    @parametrize
    def test_raw_response_vertical(self, client: Cloudflare) -> None:

        response = client.radar.attacks.layer7.top.with_raw_response.vertical()

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        top = response.parse()
        assert_matches_type(TopVerticalResponse, top, path=['response'])

    @parametrize
    def test_streaming_response_vertical(self, client: Cloudflare) -> None:
        with client.radar.attacks.layer7.top.with_streaming_response.vertical() as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            top = response.parse()
            assert_matches_type(TopVerticalResponse, top, path=['response'])

        assert cast(Any, response.is_closed) is True
class TestAsyncTop:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=['loose', 'strict'])


    @parametrize
    async def test_method_attacks(self, async_client: AsyncCloudflare) -> None:
        top = await async_client.radar.attacks.layer7.top.attacks()
        assert_matches_type(TopAttacksResponse, top, path=['response'])

    @parametrize
    async def test_method_attacks_with_all_params(self, async_client: AsyncCloudflare) -> None:
        top = await async_client.radar.attacks.layer7.top.attacks(
            asn=["string", "string", "string"],
            continent=["string", "string", "string"],
            date_end=[parse_datetime("2019-12-27T18:11:19.117Z"), parse_datetime("2019-12-27T18:11:19.117Z"), parse_datetime("2019-12-27T18:11:19.117Z")],
            date_range=["7d", "7d", "7d"],
            date_start=[parse_datetime("2019-12-27T18:11:19.117Z"), parse_datetime("2019-12-27T18:11:19.117Z"), parse_datetime("2019-12-27T18:11:19.117Z")],
            format="JSON",
            http_method=["GET", "POST", "DELETE"],
            http_version=["HTTPv1", "HTTPv2", "HTTPv3"],
            ip_version=["IPv4", "IPv6"],
            limit=5,
            limit_direction="ORIGIN",
            limit_per_location=10,
            location=["string", "string", "string"],
            magnitude="AFFECTED_ZONES",
            mitigation_product=["DDOS", "WAF", "BOT_MANAGEMENT"],
            name=["string", "string", "string"],
            normalization="PERCENTAGE",
        )
        assert_matches_type(TopAttacksResponse, top, path=['response'])

    @parametrize
    async def test_raw_response_attacks(self, async_client: AsyncCloudflare) -> None:

        response = await async_client.radar.attacks.layer7.top.with_raw_response.attacks()

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        top = await response.parse()
        assert_matches_type(TopAttacksResponse, top, path=['response'])

    @parametrize
    async def test_streaming_response_attacks(self, async_client: AsyncCloudflare) -> None:
        async with async_client.radar.attacks.layer7.top.with_streaming_response.attacks() as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            top = await response.parse()
            assert_matches_type(TopAttacksResponse, top, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_industry(self, async_client: AsyncCloudflare) -> None:
        top = await async_client.radar.attacks.layer7.top.industry()
        assert_matches_type(TopIndustryResponse, top, path=['response'])

    @parametrize
    async def test_method_industry_with_all_params(self, async_client: AsyncCloudflare) -> None:
        top = await async_client.radar.attacks.layer7.top.industry(
            asn=["string", "string", "string"],
            continent=["string", "string", "string"],
            date_end=[parse_datetime("2019-12-27T18:11:19.117Z"), parse_datetime("2019-12-27T18:11:19.117Z"), parse_datetime("2019-12-27T18:11:19.117Z")],
            date_range=["7d", "7d", "7d"],
            date_start=[parse_datetime("2019-12-27T18:11:19.117Z"), parse_datetime("2019-12-27T18:11:19.117Z"), parse_datetime("2019-12-27T18:11:19.117Z")],
            format="JSON",
            http_method=["GET", "POST", "DELETE"],
            http_version=["HTTPv1", "HTTPv2", "HTTPv3"],
            ip_version=["IPv4", "IPv6"],
            limit=5,
            location=["string", "string", "string"],
            mitigation_product=["DDOS", "WAF", "BOT_MANAGEMENT"],
            name=["string", "string", "string"],
        )
        assert_matches_type(TopIndustryResponse, top, path=['response'])

    @parametrize
    async def test_raw_response_industry(self, async_client: AsyncCloudflare) -> None:

        response = await async_client.radar.attacks.layer7.top.with_raw_response.industry()

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        top = await response.parse()
        assert_matches_type(TopIndustryResponse, top, path=['response'])

    @parametrize
    async def test_streaming_response_industry(self, async_client: AsyncCloudflare) -> None:
        async with async_client.radar.attacks.layer7.top.with_streaming_response.industry() as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            top = await response.parse()
            assert_matches_type(TopIndustryResponse, top, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_vertical(self, async_client: AsyncCloudflare) -> None:
        top = await async_client.radar.attacks.layer7.top.vertical()
        assert_matches_type(TopVerticalResponse, top, path=['response'])

    @parametrize
    async def test_method_vertical_with_all_params(self, async_client: AsyncCloudflare) -> None:
        top = await async_client.radar.attacks.layer7.top.vertical(
            asn=["string", "string", "string"],
            continent=["string", "string", "string"],
            date_end=[parse_datetime("2019-12-27T18:11:19.117Z"), parse_datetime("2019-12-27T18:11:19.117Z"), parse_datetime("2019-12-27T18:11:19.117Z")],
            date_range=["7d", "7d", "7d"],
            date_start=[parse_datetime("2019-12-27T18:11:19.117Z"), parse_datetime("2019-12-27T18:11:19.117Z"), parse_datetime("2019-12-27T18:11:19.117Z")],
            format="JSON",
            http_method=["GET", "POST", "DELETE"],
            http_version=["HTTPv1", "HTTPv2", "HTTPv3"],
            ip_version=["IPv4", "IPv6"],
            limit=5,
            location=["string", "string", "string"],
            mitigation_product=["DDOS", "WAF", "BOT_MANAGEMENT"],
            name=["string", "string", "string"],
        )
        assert_matches_type(TopVerticalResponse, top, path=['response'])

    @parametrize
    async def test_raw_response_vertical(self, async_client: AsyncCloudflare) -> None:

        response = await async_client.radar.attacks.layer7.top.with_raw_response.vertical()

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        top = await response.parse()
        assert_matches_type(TopVerticalResponse, top, path=['response'])

    @parametrize
    async def test_streaming_response_vertical(self, async_client: AsyncCloudflare) -> None:
        async with async_client.radar.attacks.layer7.top.with_streaming_response.vertical() as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            top = await response.parse()
            assert_matches_type(TopVerticalResponse, top, path=['response'])

        assert cast(Any, response.is_closed) is True