# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare._utils import parse_datetime
from cloudflare.types.radar import (
    CtSummaryResponse,
    CtTimeseriesResponse,
    CtTimeseriesGroupsResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCt:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_summary(self, client: Cloudflare) -> None:
        ct = client.radar.ct.summary(
            dimension="CA",
        )
        assert_matches_type(CtSummaryResponse, ct, path=["response"])

    @parametrize
    def test_method_summary_with_all_params(self, client: Cloudflare) -> None:
        ct = client.radar.ct.summary(
            dimension="CA",
            ca=["string"],
            ca_owner=["string"],
            date_end=[parse_datetime("2019-12-27T18:11:19.117Z")],
            date_range=["7d"],
            date_start=[parse_datetime("2019-12-27T18:11:19.117Z")],
            duration=["LTE_3D"],
            entry_type=["PRECERTIFICATE"],
            expiration_status=["EXPIRED"],
            format="JSON",
            has_ips=[True],
            has_wildcards=[True],
            limit_per_group=10,
            log=["string"],
            log_api=["RFC6962"],
            log_operator=["string"],
            name=["main_series"],
            normalization="RAW_VALUES",
            public_key_algorithm=["DSA"],
            signature_algorithm=["DSA_SHA_1"],
            tld=["string"],
            unique_entries=["true"],
            validation_level=["DOMAIN"],
        )
        assert_matches_type(CtSummaryResponse, ct, path=["response"])

    @parametrize
    def test_raw_response_summary(self, client: Cloudflare) -> None:
        response = client.radar.ct.with_raw_response.summary(
            dimension="CA",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ct = response.parse()
        assert_matches_type(CtSummaryResponse, ct, path=["response"])

    @parametrize
    def test_streaming_response_summary(self, client: Cloudflare) -> None:
        with client.radar.ct.with_streaming_response.summary(
            dimension="CA",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ct = response.parse()
            assert_matches_type(CtSummaryResponse, ct, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_timeseries(self, client: Cloudflare) -> None:
        ct = client.radar.ct.timeseries()
        assert_matches_type(CtTimeseriesResponse, ct, path=["response"])

    @parametrize
    def test_method_timeseries_with_all_params(self, client: Cloudflare) -> None:
        ct = client.radar.ct.timeseries(
            agg_interval="1h",
            ca=["string"],
            ca_owner=["string"],
            date_end=[parse_datetime("2019-12-27T18:11:19.117Z")],
            date_range=["7d"],
            date_start=[parse_datetime("2019-12-27T18:11:19.117Z")],
            duration=["LTE_3D"],
            entry_type=["PRECERTIFICATE"],
            expiration_status=["EXPIRED"],
            format="JSON",
            has_ips=[True],
            has_wildcards=[True],
            log=["string"],
            log_api=["RFC6962"],
            log_operator=["string"],
            name=["main_series"],
            public_key_algorithm=["DSA"],
            signature_algorithm=["DSA_SHA_1"],
            tld=["string"],
            unique_entries=["true"],
            validation_level=["DOMAIN"],
        )
        assert_matches_type(CtTimeseriesResponse, ct, path=["response"])

    @parametrize
    def test_raw_response_timeseries(self, client: Cloudflare) -> None:
        response = client.radar.ct.with_raw_response.timeseries()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ct = response.parse()
        assert_matches_type(CtTimeseriesResponse, ct, path=["response"])

    @parametrize
    def test_streaming_response_timeseries(self, client: Cloudflare) -> None:
        with client.radar.ct.with_streaming_response.timeseries() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ct = response.parse()
            assert_matches_type(CtTimeseriesResponse, ct, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_timeseries_groups(self, client: Cloudflare) -> None:
        ct = client.radar.ct.timeseries_groups(
            dimension="CA",
        )
        assert_matches_type(CtTimeseriesGroupsResponse, ct, path=["response"])

    @parametrize
    def test_method_timeseries_groups_with_all_params(self, client: Cloudflare) -> None:
        ct = client.radar.ct.timeseries_groups(
            dimension="CA",
            agg_interval="1h",
            ca=["string"],
            ca_owner=["string"],
            date_end=[parse_datetime("2019-12-27T18:11:19.117Z")],
            date_range=["7d"],
            date_start=[parse_datetime("2019-12-27T18:11:19.117Z")],
            duration=["LTE_3D"],
            entry_type=["PRECERTIFICATE"],
            expiration_status=["EXPIRED"],
            format="JSON",
            has_ips=[True],
            has_wildcards=[True],
            limit_per_group=10,
            log=["string"],
            log_api=["RFC6962"],
            log_operator=["string"],
            name=["main_series"],
            normalization="RAW_VALUES",
            public_key_algorithm=["DSA"],
            signature_algorithm=["DSA_SHA_1"],
            tld=["string"],
            unique_entries=["true"],
            validation_level=["DOMAIN"],
        )
        assert_matches_type(CtTimeseriesGroupsResponse, ct, path=["response"])

    @parametrize
    def test_raw_response_timeseries_groups(self, client: Cloudflare) -> None:
        response = client.radar.ct.with_raw_response.timeseries_groups(
            dimension="CA",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ct = response.parse()
        assert_matches_type(CtTimeseriesGroupsResponse, ct, path=["response"])

    @parametrize
    def test_streaming_response_timeseries_groups(self, client: Cloudflare) -> None:
        with client.radar.ct.with_streaming_response.timeseries_groups(
            dimension="CA",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ct = response.parse()
            assert_matches_type(CtTimeseriesGroupsResponse, ct, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncCt:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_summary(self, async_client: AsyncCloudflare) -> None:
        ct = await async_client.radar.ct.summary(
            dimension="CA",
        )
        assert_matches_type(CtSummaryResponse, ct, path=["response"])

    @parametrize
    async def test_method_summary_with_all_params(self, async_client: AsyncCloudflare) -> None:
        ct = await async_client.radar.ct.summary(
            dimension="CA",
            ca=["string"],
            ca_owner=["string"],
            date_end=[parse_datetime("2019-12-27T18:11:19.117Z")],
            date_range=["7d"],
            date_start=[parse_datetime("2019-12-27T18:11:19.117Z")],
            duration=["LTE_3D"],
            entry_type=["PRECERTIFICATE"],
            expiration_status=["EXPIRED"],
            format="JSON",
            has_ips=[True],
            has_wildcards=[True],
            limit_per_group=10,
            log=["string"],
            log_api=["RFC6962"],
            log_operator=["string"],
            name=["main_series"],
            normalization="RAW_VALUES",
            public_key_algorithm=["DSA"],
            signature_algorithm=["DSA_SHA_1"],
            tld=["string"],
            unique_entries=["true"],
            validation_level=["DOMAIN"],
        )
        assert_matches_type(CtSummaryResponse, ct, path=["response"])

    @parametrize
    async def test_raw_response_summary(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.radar.ct.with_raw_response.summary(
            dimension="CA",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ct = await response.parse()
        assert_matches_type(CtSummaryResponse, ct, path=["response"])

    @parametrize
    async def test_streaming_response_summary(self, async_client: AsyncCloudflare) -> None:
        async with async_client.radar.ct.with_streaming_response.summary(
            dimension="CA",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ct = await response.parse()
            assert_matches_type(CtSummaryResponse, ct, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_timeseries(self, async_client: AsyncCloudflare) -> None:
        ct = await async_client.radar.ct.timeseries()
        assert_matches_type(CtTimeseriesResponse, ct, path=["response"])

    @parametrize
    async def test_method_timeseries_with_all_params(self, async_client: AsyncCloudflare) -> None:
        ct = await async_client.radar.ct.timeseries(
            agg_interval="1h",
            ca=["string"],
            ca_owner=["string"],
            date_end=[parse_datetime("2019-12-27T18:11:19.117Z")],
            date_range=["7d"],
            date_start=[parse_datetime("2019-12-27T18:11:19.117Z")],
            duration=["LTE_3D"],
            entry_type=["PRECERTIFICATE"],
            expiration_status=["EXPIRED"],
            format="JSON",
            has_ips=[True],
            has_wildcards=[True],
            log=["string"],
            log_api=["RFC6962"],
            log_operator=["string"],
            name=["main_series"],
            public_key_algorithm=["DSA"],
            signature_algorithm=["DSA_SHA_1"],
            tld=["string"],
            unique_entries=["true"],
            validation_level=["DOMAIN"],
        )
        assert_matches_type(CtTimeseriesResponse, ct, path=["response"])

    @parametrize
    async def test_raw_response_timeseries(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.radar.ct.with_raw_response.timeseries()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ct = await response.parse()
        assert_matches_type(CtTimeseriesResponse, ct, path=["response"])

    @parametrize
    async def test_streaming_response_timeseries(self, async_client: AsyncCloudflare) -> None:
        async with async_client.radar.ct.with_streaming_response.timeseries() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ct = await response.parse()
            assert_matches_type(CtTimeseriesResponse, ct, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_timeseries_groups(self, async_client: AsyncCloudflare) -> None:
        ct = await async_client.radar.ct.timeseries_groups(
            dimension="CA",
        )
        assert_matches_type(CtTimeseriesGroupsResponse, ct, path=["response"])

    @parametrize
    async def test_method_timeseries_groups_with_all_params(self, async_client: AsyncCloudflare) -> None:
        ct = await async_client.radar.ct.timeseries_groups(
            dimension="CA",
            agg_interval="1h",
            ca=["string"],
            ca_owner=["string"],
            date_end=[parse_datetime("2019-12-27T18:11:19.117Z")],
            date_range=["7d"],
            date_start=[parse_datetime("2019-12-27T18:11:19.117Z")],
            duration=["LTE_3D"],
            entry_type=["PRECERTIFICATE"],
            expiration_status=["EXPIRED"],
            format="JSON",
            has_ips=[True],
            has_wildcards=[True],
            limit_per_group=10,
            log=["string"],
            log_api=["RFC6962"],
            log_operator=["string"],
            name=["main_series"],
            normalization="RAW_VALUES",
            public_key_algorithm=["DSA"],
            signature_algorithm=["DSA_SHA_1"],
            tld=["string"],
            unique_entries=["true"],
            validation_level=["DOMAIN"],
        )
        assert_matches_type(CtTimeseriesGroupsResponse, ct, path=["response"])

    @parametrize
    async def test_raw_response_timeseries_groups(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.radar.ct.with_raw_response.timeseries_groups(
            dimension="CA",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ct = await response.parse()
        assert_matches_type(CtTimeseriesGroupsResponse, ct, path=["response"])

    @parametrize
    async def test_streaming_response_timeseries_groups(self, async_client: AsyncCloudflare) -> None:
        async with async_client.radar.ct.with_streaming_response.timeseries_groups(
            dimension="CA",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ct = await response.parse()
            assert_matches_type(CtTimeseriesGroupsResponse, ct, path=["response"])

        assert cast(Any, response.is_closed) is True
