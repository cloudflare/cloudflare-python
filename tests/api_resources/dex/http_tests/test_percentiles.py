# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.dex.http_tests import PercentileListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPercentiles:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        percentile = client.dex.http_tests.percentiles.list(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="01a7362d577a6c3019a474fd6f485823",
            time_end="2023-09-20T17:00:00Z",
            time_start="2023-09-20T17:00:00Z",
        )
        assert_matches_type(PercentileListResponse, percentile, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list_with_all_params(self, client: Cloudflare) -> None:
        percentile = client.dex.http_tests.percentiles.list(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="01a7362d577a6c3019a474fd6f485823",
            time_end="2023-09-20T17:00:00Z",
            time_start="2023-09-20T17:00:00Z",
            colo="string",
            device_id=["string", "string", "string"],
        )
        assert_matches_type(PercentileListResponse, percentile, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.dex.http_tests.percentiles.with_raw_response.list(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="01a7362d577a6c3019a474fd6f485823",
            time_end="2023-09-20T17:00:00Z",
            time_start="2023-09-20T17:00:00Z",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        percentile = response.parse()
        assert_matches_type(PercentileListResponse, percentile, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.dex.http_tests.percentiles.with_streaming_response.list(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="01a7362d577a6c3019a474fd6f485823",
            time_end="2023-09-20T17:00:00Z",
            time_start="2023-09-20T17:00:00Z",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            percentile = response.parse()
            assert_matches_type(PercentileListResponse, percentile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.dex.http_tests.percentiles.with_raw_response.list(
                "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_id="",
                time_end="2023-09-20T17:00:00Z",
                time_start="2023-09-20T17:00:00Z",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `test_id` but received ''"):
            client.dex.http_tests.percentiles.with_raw_response.list(
                "",
                account_id="01a7362d577a6c3019a474fd6f485823",
                time_end="2023-09-20T17:00:00Z",
                time_start="2023-09-20T17:00:00Z",
            )


class TestAsyncPercentiles:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        percentile = await async_client.dex.http_tests.percentiles.list(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="01a7362d577a6c3019a474fd6f485823",
            time_end="2023-09-20T17:00:00Z",
            time_start="2023-09-20T17:00:00Z",
        )
        assert_matches_type(PercentileListResponse, percentile, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCloudflare) -> None:
        percentile = await async_client.dex.http_tests.percentiles.list(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="01a7362d577a6c3019a474fd6f485823",
            time_end="2023-09-20T17:00:00Z",
            time_start="2023-09-20T17:00:00Z",
            colo="string",
            device_id=["string", "string", "string"],
        )
        assert_matches_type(PercentileListResponse, percentile, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dex.http_tests.percentiles.with_raw_response.list(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="01a7362d577a6c3019a474fd6f485823",
            time_end="2023-09-20T17:00:00Z",
            time_start="2023-09-20T17:00:00Z",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        percentile = await response.parse()
        assert_matches_type(PercentileListResponse, percentile, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.dex.http_tests.percentiles.with_streaming_response.list(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="01a7362d577a6c3019a474fd6f485823",
            time_end="2023-09-20T17:00:00Z",
            time_start="2023-09-20T17:00:00Z",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            percentile = await response.parse()
            assert_matches_type(PercentileListResponse, percentile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.dex.http_tests.percentiles.with_raw_response.list(
                "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_id="",
                time_end="2023-09-20T17:00:00Z",
                time_start="2023-09-20T17:00:00Z",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `test_id` but received ''"):
            await async_client.dex.http_tests.percentiles.with_raw_response.list(
                "",
                account_id="01a7362d577a6c3019a474fd6f485823",
                time_end="2023-09-20T17:00:00Z",
                time_start="2023-09-20T17:00:00Z",
            )
