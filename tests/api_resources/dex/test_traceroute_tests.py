# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from cloudflare.types.dex import (
    TracerouteTestGetResponse,
    TracerouteTestNetworkPathResponse,
    TracerouteTestPercentilesResponse,
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
from cloudflare.types.dex import traceroute_test_get_params
from cloudflare.types.dex import traceroute_test_network_path_params
from cloudflare.types.dex import traceroute_test_percentiles_params

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTracerouteTests:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        traceroute_test = client.dex.traceroute_tests.get(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="01a7362d577a6c3019a474fd6f485823",
            interval="minute",
            time_end="1689606812000",
            time_start="1689520412000",
        )
        assert_matches_type(TracerouteTestGetResponse, traceroute_test, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_get_with_all_params(self, client: Cloudflare) -> None:
        traceroute_test = client.dex.traceroute_tests.get(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="01a7362d577a6c3019a474fd6f485823",
            interval="minute",
            time_end="1689606812000",
            time_start="1689520412000",
            colo="string",
            device_id=["string", "string", "string"],
        )
        assert_matches_type(TracerouteTestGetResponse, traceroute_test, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.dex.traceroute_tests.with_raw_response.get(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="01a7362d577a6c3019a474fd6f485823",
            interval="minute",
            time_end="1689606812000",
            time_start="1689520412000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        traceroute_test = response.parse()
        assert_matches_type(TracerouteTestGetResponse, traceroute_test, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.dex.traceroute_tests.with_streaming_response.get(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="01a7362d577a6c3019a474fd6f485823",
            interval="minute",
            time_end="1689606812000",
            time_start="1689520412000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            traceroute_test = response.parse()
            assert_matches_type(TracerouteTestGetResponse, traceroute_test, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.dex.traceroute_tests.with_raw_response.get(
                "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_id="",
                interval="minute",
                time_end="1689606812000",
                time_start="1689520412000",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `test_id` but received ''"):
            client.dex.traceroute_tests.with_raw_response.get(
                "",
                account_id="01a7362d577a6c3019a474fd6f485823",
                interval="minute",
                time_end="1689606812000",
                time_start="1689520412000",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_network_path(self, client: Cloudflare) -> None:
        traceroute_test = client.dex.traceroute_tests.network_path(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="01a7362d577a6c3019a474fd6f485823",
            device_id="string",
            interval="minute",
            time_end="1689606812000",
            time_start="1689520412000",
        )
        assert_matches_type(TracerouteTestNetworkPathResponse, traceroute_test, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_network_path(self, client: Cloudflare) -> None:
        response = client.dex.traceroute_tests.with_raw_response.network_path(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="01a7362d577a6c3019a474fd6f485823",
            device_id="string",
            interval="minute",
            time_end="1689606812000",
            time_start="1689520412000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        traceroute_test = response.parse()
        assert_matches_type(TracerouteTestNetworkPathResponse, traceroute_test, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_network_path(self, client: Cloudflare) -> None:
        with client.dex.traceroute_tests.with_streaming_response.network_path(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="01a7362d577a6c3019a474fd6f485823",
            device_id="string",
            interval="minute",
            time_end="1689606812000",
            time_start="1689520412000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            traceroute_test = response.parse()
            assert_matches_type(TracerouteTestNetworkPathResponse, traceroute_test, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_network_path(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.dex.traceroute_tests.with_raw_response.network_path(
                "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_id="",
                device_id="string",
                interval="minute",
                time_end="1689606812000",
                time_start="1689520412000",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `test_id` but received ''"):
            client.dex.traceroute_tests.with_raw_response.network_path(
                "",
                account_id="01a7362d577a6c3019a474fd6f485823",
                device_id="string",
                interval="minute",
                time_end="1689606812000",
                time_start="1689520412000",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_percentiles(self, client: Cloudflare) -> None:
        traceroute_test = client.dex.traceroute_tests.percentiles(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="01a7362d577a6c3019a474fd6f485823",
            time_end="2023-09-20T17:00:00Z",
            time_start="2023-09-20T17:00:00Z",
        )
        assert_matches_type(TracerouteTestPercentilesResponse, traceroute_test, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_percentiles_with_all_params(self, client: Cloudflare) -> None:
        traceroute_test = client.dex.traceroute_tests.percentiles(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="01a7362d577a6c3019a474fd6f485823",
            time_end="2023-09-20T17:00:00Z",
            time_start="2023-09-20T17:00:00Z",
            colo="string",
            device_id=["string", "string", "string"],
        )
        assert_matches_type(TracerouteTestPercentilesResponse, traceroute_test, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_percentiles(self, client: Cloudflare) -> None:
        response = client.dex.traceroute_tests.with_raw_response.percentiles(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="01a7362d577a6c3019a474fd6f485823",
            time_end="2023-09-20T17:00:00Z",
            time_start="2023-09-20T17:00:00Z",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        traceroute_test = response.parse()
        assert_matches_type(TracerouteTestPercentilesResponse, traceroute_test, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_percentiles(self, client: Cloudflare) -> None:
        with client.dex.traceroute_tests.with_streaming_response.percentiles(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="01a7362d577a6c3019a474fd6f485823",
            time_end="2023-09-20T17:00:00Z",
            time_start="2023-09-20T17:00:00Z",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            traceroute_test = response.parse()
            assert_matches_type(TracerouteTestPercentilesResponse, traceroute_test, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_percentiles(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.dex.traceroute_tests.with_raw_response.percentiles(
                "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_id="",
                time_end="2023-09-20T17:00:00Z",
                time_start="2023-09-20T17:00:00Z",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `test_id` but received ''"):
            client.dex.traceroute_tests.with_raw_response.percentiles(
                "",
                account_id="01a7362d577a6c3019a474fd6f485823",
                time_end="2023-09-20T17:00:00Z",
                time_start="2023-09-20T17:00:00Z",
            )


class TestAsyncTracerouteTests:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        traceroute_test = await async_client.dex.traceroute_tests.get(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="01a7362d577a6c3019a474fd6f485823",
            interval="minute",
            time_end="1689606812000",
            time_start="1689520412000",
        )
        assert_matches_type(TracerouteTestGetResponse, traceroute_test, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncCloudflare) -> None:
        traceroute_test = await async_client.dex.traceroute_tests.get(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="01a7362d577a6c3019a474fd6f485823",
            interval="minute",
            time_end="1689606812000",
            time_start="1689520412000",
            colo="string",
            device_id=["string", "string", "string"],
        )
        assert_matches_type(TracerouteTestGetResponse, traceroute_test, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dex.traceroute_tests.with_raw_response.get(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="01a7362d577a6c3019a474fd6f485823",
            interval="minute",
            time_end="1689606812000",
            time_start="1689520412000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        traceroute_test = await response.parse()
        assert_matches_type(TracerouteTestGetResponse, traceroute_test, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.dex.traceroute_tests.with_streaming_response.get(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="01a7362d577a6c3019a474fd6f485823",
            interval="minute",
            time_end="1689606812000",
            time_start="1689520412000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            traceroute_test = await response.parse()
            assert_matches_type(TracerouteTestGetResponse, traceroute_test, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.dex.traceroute_tests.with_raw_response.get(
                "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_id="",
                interval="minute",
                time_end="1689606812000",
                time_start="1689520412000",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `test_id` but received ''"):
            await async_client.dex.traceroute_tests.with_raw_response.get(
                "",
                account_id="01a7362d577a6c3019a474fd6f485823",
                interval="minute",
                time_end="1689606812000",
                time_start="1689520412000",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_network_path(self, async_client: AsyncCloudflare) -> None:
        traceroute_test = await async_client.dex.traceroute_tests.network_path(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="01a7362d577a6c3019a474fd6f485823",
            device_id="string",
            interval="minute",
            time_end="1689606812000",
            time_start="1689520412000",
        )
        assert_matches_type(TracerouteTestNetworkPathResponse, traceroute_test, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_network_path(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dex.traceroute_tests.with_raw_response.network_path(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="01a7362d577a6c3019a474fd6f485823",
            device_id="string",
            interval="minute",
            time_end="1689606812000",
            time_start="1689520412000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        traceroute_test = await response.parse()
        assert_matches_type(TracerouteTestNetworkPathResponse, traceroute_test, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_network_path(self, async_client: AsyncCloudflare) -> None:
        async with async_client.dex.traceroute_tests.with_streaming_response.network_path(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="01a7362d577a6c3019a474fd6f485823",
            device_id="string",
            interval="minute",
            time_end="1689606812000",
            time_start="1689520412000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            traceroute_test = await response.parse()
            assert_matches_type(TracerouteTestNetworkPathResponse, traceroute_test, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_network_path(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.dex.traceroute_tests.with_raw_response.network_path(
                "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_id="",
                device_id="string",
                interval="minute",
                time_end="1689606812000",
                time_start="1689520412000",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `test_id` but received ''"):
            await async_client.dex.traceroute_tests.with_raw_response.network_path(
                "",
                account_id="01a7362d577a6c3019a474fd6f485823",
                device_id="string",
                interval="minute",
                time_end="1689606812000",
                time_start="1689520412000",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_percentiles(self, async_client: AsyncCloudflare) -> None:
        traceroute_test = await async_client.dex.traceroute_tests.percentiles(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="01a7362d577a6c3019a474fd6f485823",
            time_end="2023-09-20T17:00:00Z",
            time_start="2023-09-20T17:00:00Z",
        )
        assert_matches_type(TracerouteTestPercentilesResponse, traceroute_test, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_percentiles_with_all_params(self, async_client: AsyncCloudflare) -> None:
        traceroute_test = await async_client.dex.traceroute_tests.percentiles(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="01a7362d577a6c3019a474fd6f485823",
            time_end="2023-09-20T17:00:00Z",
            time_start="2023-09-20T17:00:00Z",
            colo="string",
            device_id=["string", "string", "string"],
        )
        assert_matches_type(TracerouteTestPercentilesResponse, traceroute_test, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_percentiles(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dex.traceroute_tests.with_raw_response.percentiles(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="01a7362d577a6c3019a474fd6f485823",
            time_end="2023-09-20T17:00:00Z",
            time_start="2023-09-20T17:00:00Z",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        traceroute_test = await response.parse()
        assert_matches_type(TracerouteTestPercentilesResponse, traceroute_test, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_percentiles(self, async_client: AsyncCloudflare) -> None:
        async with async_client.dex.traceroute_tests.with_streaming_response.percentiles(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="01a7362d577a6c3019a474fd6f485823",
            time_end="2023-09-20T17:00:00Z",
            time_start="2023-09-20T17:00:00Z",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            traceroute_test = await response.parse()
            assert_matches_type(TracerouteTestPercentilesResponse, traceroute_test, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_percentiles(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.dex.traceroute_tests.with_raw_response.percentiles(
                "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_id="",
                time_end="2023-09-20T17:00:00Z",
                time_start="2023-09-20T17:00:00Z",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `test_id` but received ''"):
            await async_client.dex.traceroute_tests.with_raw_response.percentiles(
                "",
                account_id="01a7362d577a6c3019a474fd6f485823",
                time_end="2023-09-20T17:00:00Z",
                time_start="2023-09-20T17:00:00Z",
            )
