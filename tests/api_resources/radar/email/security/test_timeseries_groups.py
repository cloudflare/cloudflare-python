# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare._utils import parse_datetime
from cloudflare.types.radar.email.security import (
    TimeseriesGroupARCResponse,
    TimeseriesGroupDKIMResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTimeseriesGroups:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_arc(self, client: Cloudflare) -> None:
        timeseries_group = client.radar.email.security.timeseries_groups.arc()
        assert_matches_type(TimeseriesGroupARCResponse, timeseries_group, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_arc_with_all_params(self, client: Cloudflare) -> None:
        timeseries_group = client.radar.email.security.timeseries_groups.arc(
            agg_interval="1h",
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
            location=["string", "string", "string"],
            name=["string", "string", "string"],
            spf=["PASS", "NONE", "FAIL"],
        )
        assert_matches_type(TimeseriesGroupARCResponse, timeseries_group, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_arc(self, client: Cloudflare) -> None:
        response = client.radar.email.security.timeseries_groups.with_raw_response.arc()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        timeseries_group = response.parse()
        assert_matches_type(TimeseriesGroupARCResponse, timeseries_group, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_arc(self, client: Cloudflare) -> None:
        with client.radar.email.security.timeseries_groups.with_streaming_response.arc() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            timeseries_group = response.parse()
            assert_matches_type(TimeseriesGroupARCResponse, timeseries_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_dkim(self, client: Cloudflare) -> None:
        timeseries_group = client.radar.email.security.timeseries_groups.dkim()
        assert_matches_type(TimeseriesGroupDKIMResponse, timeseries_group, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_dkim_with_all_params(self, client: Cloudflare) -> None:
        timeseries_group = client.radar.email.security.timeseries_groups.dkim(
            agg_interval="1h",
            arc=["PASS", "NONE", "FAIL"],
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
            dmarc=["PASS", "NONE", "FAIL"],
            format="JSON",
            location=["string", "string", "string"],
            name=["string", "string", "string"],
            spf=["PASS", "NONE", "FAIL"],
        )
        assert_matches_type(TimeseriesGroupDKIMResponse, timeseries_group, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_dkim(self, client: Cloudflare) -> None:
        response = client.radar.email.security.timeseries_groups.with_raw_response.dkim()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        timeseries_group = response.parse()
        assert_matches_type(TimeseriesGroupDKIMResponse, timeseries_group, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_dkim(self, client: Cloudflare) -> None:
        with client.radar.email.security.timeseries_groups.with_streaming_response.dkim() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            timeseries_group = response.parse()
            assert_matches_type(TimeseriesGroupDKIMResponse, timeseries_group, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncTimeseriesGroups:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_arc(self, async_client: AsyncCloudflare) -> None:
        timeseries_group = await async_client.radar.email.security.timeseries_groups.arc()
        assert_matches_type(TimeseriesGroupARCResponse, timeseries_group, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_arc_with_all_params(self, async_client: AsyncCloudflare) -> None:
        timeseries_group = await async_client.radar.email.security.timeseries_groups.arc(
            agg_interval="1h",
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
            location=["string", "string", "string"],
            name=["string", "string", "string"],
            spf=["PASS", "NONE", "FAIL"],
        )
        assert_matches_type(TimeseriesGroupARCResponse, timeseries_group, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_arc(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.radar.email.security.timeseries_groups.with_raw_response.arc()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        timeseries_group = await response.parse()
        assert_matches_type(TimeseriesGroupARCResponse, timeseries_group, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_arc(self, async_client: AsyncCloudflare) -> None:
        async with async_client.radar.email.security.timeseries_groups.with_streaming_response.arc() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            timeseries_group = await response.parse()
            assert_matches_type(TimeseriesGroupARCResponse, timeseries_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_dkim(self, async_client: AsyncCloudflare) -> None:
        timeseries_group = await async_client.radar.email.security.timeseries_groups.dkim()
        assert_matches_type(TimeseriesGroupDKIMResponse, timeseries_group, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_dkim_with_all_params(self, async_client: AsyncCloudflare) -> None:
        timeseries_group = await async_client.radar.email.security.timeseries_groups.dkim(
            agg_interval="1h",
            arc=["PASS", "NONE", "FAIL"],
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
            dmarc=["PASS", "NONE", "FAIL"],
            format="JSON",
            location=["string", "string", "string"],
            name=["string", "string", "string"],
            spf=["PASS", "NONE", "FAIL"],
        )
        assert_matches_type(TimeseriesGroupDKIMResponse, timeseries_group, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_dkim(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.radar.email.security.timeseries_groups.with_raw_response.dkim()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        timeseries_group = await response.parse()
        assert_matches_type(TimeseriesGroupDKIMResponse, timeseries_group, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_dkim(self, async_client: AsyncCloudflare) -> None:
        async with async_client.radar.email.security.timeseries_groups.with_streaming_response.dkim() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            timeseries_group = await response.parse()
            assert_matches_type(TimeseriesGroupDKIMResponse, timeseries_group, path=["response"])

        assert cast(Any, response.is_closed) is True
