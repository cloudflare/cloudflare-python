# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from cloudflare import Cloudflare, AsyncCloudflare

from cloudflare.types.radar.attacks.layer7.top import AseOriginResponse

from typing import Any, cast

import os
import pytest
import httpx
from typing_extensions import get_args
from typing import Optional
from respx import MockRouter
from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.radar.attacks.layer7.top import ase_origin_params
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


class TestAses:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_origin(self, client: Cloudflare) -> None:
        ase = client.radar.attacks.layer7.top.ases.origin()
        assert_matches_type(AseOriginResponse, ase, path=["response"])

    @parametrize
    def test_method_origin_with_all_params(self, client: Cloudflare) -> None:
        ase = client.radar.attacks.layer7.top.ases.origin(
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
            http_method=["GET", "POST", "DELETE"],
            http_version=["HTTPv1", "HTTPv2", "HTTPv3"],
            ip_version=["IPv4", "IPv6"],
            limit=5,
            location=["string", "string", "string"],
            mitigation_product=["DDOS", "WAF", "BOT_MANAGEMENT"],
            name=["string", "string", "string"],
        )
        assert_matches_type(AseOriginResponse, ase, path=["response"])

    @parametrize
    def test_raw_response_origin(self, client: Cloudflare) -> None:
        response = client.radar.attacks.layer7.top.ases.with_raw_response.origin()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ase = response.parse()
        assert_matches_type(AseOriginResponse, ase, path=["response"])

    @parametrize
    def test_streaming_response_origin(self, client: Cloudflare) -> None:
        with client.radar.attacks.layer7.top.ases.with_streaming_response.origin() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ase = response.parse()
            assert_matches_type(AseOriginResponse, ase, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAses:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_origin(self, async_client: AsyncCloudflare) -> None:
        ase = await async_client.radar.attacks.layer7.top.ases.origin()
        assert_matches_type(AseOriginResponse, ase, path=["response"])

    @parametrize
    async def test_method_origin_with_all_params(self, async_client: AsyncCloudflare) -> None:
        ase = await async_client.radar.attacks.layer7.top.ases.origin(
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
            http_method=["GET", "POST", "DELETE"],
            http_version=["HTTPv1", "HTTPv2", "HTTPv3"],
            ip_version=["IPv4", "IPv6"],
            limit=5,
            location=["string", "string", "string"],
            mitigation_product=["DDOS", "WAF", "BOT_MANAGEMENT"],
            name=["string", "string", "string"],
        )
        assert_matches_type(AseOriginResponse, ase, path=["response"])

    @parametrize
    async def test_raw_response_origin(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.radar.attacks.layer7.top.ases.with_raw_response.origin()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ase = await response.parse()
        assert_matches_type(AseOriginResponse, ase, path=["response"])

    @parametrize
    async def test_streaming_response_origin(self, async_client: AsyncCloudflare) -> None:
        async with async_client.radar.attacks.layer7.top.ases.with_streaming_response.origin() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ase = await response.parse()
            assert_matches_type(AseOriginResponse, ase, path=["response"])

        assert cast(Any, response.is_closed) is True
