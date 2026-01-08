# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.realtime_kit import AppGetResponse, AppPostResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestApps:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        app = client.realtime_kit.apps.get(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(AppGetResponse, app, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.realtime_kit.apps.with_raw_response.get(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        app = response.parse()
        assert_matches_type(AppGetResponse, app, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.realtime_kit.apps.with_streaming_response.get(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            app = response.parse()
            assert_matches_type(AppGetResponse, app, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.realtime_kit.apps.with_raw_response.get(
                account_id="",
            )

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    def test_method_post(self, client: Cloudflare) -> None:
        app = client.realtime_kit.apps.post(
            account_id="account_id",
            name="name",
        )
        assert_matches_type(AppPostResponse, app, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    def test_raw_response_post(self, client: Cloudflare) -> None:
        response = client.realtime_kit.apps.with_raw_response.post(
            account_id="account_id",
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        app = response.parse()
        assert_matches_type(AppPostResponse, app, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    def test_streaming_response_post(self, client: Cloudflare) -> None:
        with client.realtime_kit.apps.with_streaming_response.post(
            account_id="account_id",
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            app = response.parse()
            assert_matches_type(AppPostResponse, app, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    def test_path_params_post(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.realtime_kit.apps.with_raw_response.post(
                account_id="",
                name="name",
            )


class TestAsyncApps:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        app = await async_client.realtime_kit.apps.get(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(AppGetResponse, app, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.realtime_kit.apps.with_raw_response.get(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        app = await response.parse()
        assert_matches_type(AppGetResponse, app, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.realtime_kit.apps.with_streaming_response.get(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            app = await response.parse()
            assert_matches_type(AppGetResponse, app, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.realtime_kit.apps.with_raw_response.get(
                account_id="",
            )

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    async def test_method_post(self, async_client: AsyncCloudflare) -> None:
        app = await async_client.realtime_kit.apps.post(
            account_id="account_id",
            name="name",
        )
        assert_matches_type(AppPostResponse, app, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    async def test_raw_response_post(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.realtime_kit.apps.with_raw_response.post(
            account_id="account_id",
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        app = await response.parse()
        assert_matches_type(AppPostResponse, app, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    async def test_streaming_response_post(self, async_client: AsyncCloudflare) -> None:
        async with async_client.realtime_kit.apps.with_streaming_response.post(
            account_id="account_id",
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            app = await response.parse()
            assert_matches_type(AppPostResponse, app, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    async def test_path_params_post(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.realtime_kit.apps.with_raw_response.post(
                account_id="",
                name="name",
            )
