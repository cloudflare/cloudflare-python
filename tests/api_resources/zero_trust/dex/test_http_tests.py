# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.zero_trust.dex import HTTPDetails

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestHTTPTests:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        http_test = client.zero_trust.dex.http_tests.get(
            test_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="01a7362d577a6c3019a474fd6f485823",
            from_="1689520412000",
            interval="minute",
            to="1689606812000",
        )
        assert_matches_type(Optional[HTTPDetails], http_test, path=["response"])

    @parametrize
    def test_method_get_with_all_params(self, client: Cloudflare) -> None:
        http_test = client.zero_trust.dex.http_tests.get(
            test_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="01a7362d577a6c3019a474fd6f485823",
            from_="1689520412000",
            interval="minute",
            to="1689606812000",
            colo="colo",
            device_id=["string"],
        )
        assert_matches_type(Optional[HTTPDetails], http_test, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.zero_trust.dex.http_tests.with_raw_response.get(
            test_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="01a7362d577a6c3019a474fd6f485823",
            from_="1689520412000",
            interval="minute",
            to="1689606812000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        http_test = response.parse()
        assert_matches_type(Optional[HTTPDetails], http_test, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.zero_trust.dex.http_tests.with_streaming_response.get(
            test_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="01a7362d577a6c3019a474fd6f485823",
            from_="1689520412000",
            interval="minute",
            to="1689606812000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            http_test = response.parse()
            assert_matches_type(Optional[HTTPDetails], http_test, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.dex.http_tests.with_raw_response.get(
                test_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_id="",
                from_="1689520412000",
                interval="minute",
                to="1689606812000",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `test_id` but received ''"):
            client.zero_trust.dex.http_tests.with_raw_response.get(
                test_id="",
                account_id="01a7362d577a6c3019a474fd6f485823",
                from_="1689520412000",
                interval="minute",
                to="1689606812000",
            )


class TestAsyncHTTPTests:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        http_test = await async_client.zero_trust.dex.http_tests.get(
            test_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="01a7362d577a6c3019a474fd6f485823",
            from_="1689520412000",
            interval="minute",
            to="1689606812000",
        )
        assert_matches_type(Optional[HTTPDetails], http_test, path=["response"])

    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncCloudflare) -> None:
        http_test = await async_client.zero_trust.dex.http_tests.get(
            test_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="01a7362d577a6c3019a474fd6f485823",
            from_="1689520412000",
            interval="minute",
            to="1689606812000",
            colo="colo",
            device_id=["string"],
        )
        assert_matches_type(Optional[HTTPDetails], http_test, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.dex.http_tests.with_raw_response.get(
            test_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="01a7362d577a6c3019a474fd6f485823",
            from_="1689520412000",
            interval="minute",
            to="1689606812000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        http_test = await response.parse()
        assert_matches_type(Optional[HTTPDetails], http_test, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.dex.http_tests.with_streaming_response.get(
            test_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="01a7362d577a6c3019a474fd6f485823",
            from_="1689520412000",
            interval="minute",
            to="1689606812000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            http_test = await response.parse()
            assert_matches_type(Optional[HTTPDetails], http_test, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.dex.http_tests.with_raw_response.get(
                test_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_id="",
                from_="1689520412000",
                interval="minute",
                to="1689606812000",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `test_id` but received ''"):
            await async_client.zero_trust.dex.http_tests.with_raw_response.get(
                test_id="",
                account_id="01a7362d577a6c3019a474fd6f485823",
                from_="1689520412000",
                interval="minute",
                to="1689606812000",
            )
