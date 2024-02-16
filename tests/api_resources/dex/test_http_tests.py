# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from cloudflare.types.dex import HTTPTestGetResponse

from typing import Any, cast

import os
import pytest
import httpx
from typing_extensions import get_args
from typing import Optional
from respx import MockRouter
from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.dex import http_test_get_params

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestHTTPTests:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        http_test = client.dex.http_tests.get(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="01a7362d577a6c3019a474fd6f485823",
            interval="minute",
            time_end="string",
            time_start="string",
        )
        assert_matches_type(HTTPTestGetResponse, http_test, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_get_with_all_params(self, client: Cloudflare) -> None:
        http_test = client.dex.http_tests.get(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="01a7362d577a6c3019a474fd6f485823",
            interval="minute",
            time_end="string",
            time_start="string",
            colo="string",
            device_id=["string", "string", "string"],
        )
        assert_matches_type(HTTPTestGetResponse, http_test, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.dex.http_tests.with_raw_response.get(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="01a7362d577a6c3019a474fd6f485823",
            interval="minute",
            time_end="string",
            time_start="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        http_test = response.parse()
        assert_matches_type(HTTPTestGetResponse, http_test, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.dex.http_tests.with_streaming_response.get(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="01a7362d577a6c3019a474fd6f485823",
            interval="minute",
            time_end="string",
            time_start="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            http_test = response.parse()
            assert_matches_type(HTTPTestGetResponse, http_test, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.dex.http_tests.with_raw_response.get(
                "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_id="",
                interval="minute",
                time_end="string",
                time_start="string",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `test_id` but received ''"):
            client.dex.http_tests.with_raw_response.get(
                "",
                account_id="01a7362d577a6c3019a474fd6f485823",
                interval="minute",
                time_end="string",
                time_start="string",
            )


class TestAsyncHTTPTests:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        http_test = await async_client.dex.http_tests.get(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="01a7362d577a6c3019a474fd6f485823",
            interval="minute",
            time_end="string",
            time_start="string",
        )
        assert_matches_type(HTTPTestGetResponse, http_test, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncCloudflare) -> None:
        http_test = await async_client.dex.http_tests.get(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="01a7362d577a6c3019a474fd6f485823",
            interval="minute",
            time_end="string",
            time_start="string",
            colo="string",
            device_id=["string", "string", "string"],
        )
        assert_matches_type(HTTPTestGetResponse, http_test, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dex.http_tests.with_raw_response.get(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="01a7362d577a6c3019a474fd6f485823",
            interval="minute",
            time_end="string",
            time_start="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        http_test = await response.parse()
        assert_matches_type(HTTPTestGetResponse, http_test, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.dex.http_tests.with_streaming_response.get(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="01a7362d577a6c3019a474fd6f485823",
            interval="minute",
            time_end="string",
            time_start="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            http_test = await response.parse()
            assert_matches_type(HTTPTestGetResponse, http_test, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.dex.http_tests.with_raw_response.get(
                "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_id="",
                interval="minute",
                time_end="string",
                time_start="string",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `test_id` but received ''"):
            await async_client.dex.http_tests.with_raw_response.get(
                "",
                account_id="01a7362d577a6c3019a474fd6f485823",
                interval="minute",
                time_end="string",
                time_start="string",
            )
