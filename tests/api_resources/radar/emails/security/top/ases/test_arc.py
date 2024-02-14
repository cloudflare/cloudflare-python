# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from cloudflare.types.radar.emails.security.top.ases import ArcGetResponse

from typing import Any, cast

import os
import pytest
import httpx
from typing_extensions import get_args
from typing import Optional
from respx import MockRouter
from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.radar.emails.security.top.ases import arc_get_params
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


class TestArc:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        arc = client.radar.emails.security.top.ases.arc.get(
            "PASS",
        )
        assert_matches_type(ArcGetResponse, arc, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_get_with_all_params(self, client: Cloudflare) -> None:
        arc = client.radar.emails.security.top.ases.arc.get(
            "PASS",
            asn=["string", "string", "string"],
            date_end=[
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
            ],
            date_range=["1d", "2d", "7d"],
            date_start=[
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
            ],
            dkim=["PASS", "NONE", "FAIL"],
            dmarc=["PASS", "NONE", "FAIL"],
            format="JSON",
            limit=5,
            location=["string", "string", "string"],
            name=["string", "string", "string"],
            spf=["PASS", "NONE", "FAIL"],
        )
        assert_matches_type(ArcGetResponse, arc, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.radar.emails.security.top.ases.arc.with_raw_response.get(
            "PASS",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        arc = response.parse()
        assert_matches_type(ArcGetResponse, arc, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.radar.emails.security.top.ases.arc.with_streaming_response.get(
            "PASS",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            arc = response.parse()
            assert_matches_type(ArcGetResponse, arc, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncArc:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        arc = await async_client.radar.emails.security.top.ases.arc.get(
            "PASS",
        )
        assert_matches_type(ArcGetResponse, arc, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncCloudflare) -> None:
        arc = await async_client.radar.emails.security.top.ases.arc.get(
            "PASS",
            asn=["string", "string", "string"],
            date_end=[
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
            ],
            date_range=["1d", "2d", "7d"],
            date_start=[
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
            ],
            dkim=["PASS", "NONE", "FAIL"],
            dmarc=["PASS", "NONE", "FAIL"],
            format="JSON",
            limit=5,
            location=["string", "string", "string"],
            name=["string", "string", "string"],
            spf=["PASS", "NONE", "FAIL"],
        )
        assert_matches_type(ArcGetResponse, arc, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.radar.emails.security.top.ases.arc.with_raw_response.get(
            "PASS",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        arc = await response.parse()
        assert_matches_type(ArcGetResponse, arc, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.radar.emails.security.top.ases.arc.with_streaming_response.get(
            "PASS",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            arc = await response.parse()
            assert_matches_type(ArcGetResponse, arc, path=["response"])

        assert cast(Any, response.is_closed) is True
