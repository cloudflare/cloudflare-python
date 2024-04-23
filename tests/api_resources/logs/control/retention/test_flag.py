# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.logs.control.retention.flag_get_response import FlagGetResponse
from cloudflare.types.logs.control.retention.flag_create_response import FlagCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFlag:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        flag = client.logs.control.retention.flag.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            flag=True,
        )
        assert_matches_type(FlagCreateResponse, flag, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.logs.control.retention.flag.with_raw_response.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            flag=True,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        flag = response.parse()
        assert_matches_type(FlagCreateResponse, flag, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.logs.control.retention.flag.with_streaming_response.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            flag=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            flag = response.parse()
            assert_matches_type(FlagCreateResponse, flag, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_identifier` but received ''"):
            client.logs.control.retention.flag.with_raw_response.create(
                "",
                flag=True,
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        flag = client.logs.control.retention.flag.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(FlagGetResponse, flag, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.logs.control.retention.flag.with_raw_response.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        flag = response.parse()
        assert_matches_type(FlagGetResponse, flag, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.logs.control.retention.flag.with_streaming_response.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            flag = response.parse()
            assert_matches_type(FlagGetResponse, flag, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_identifier` but received ''"):
            client.logs.control.retention.flag.with_raw_response.get(
                "",
            )


class TestAsyncFlag:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        flag = await async_client.logs.control.retention.flag.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            flag=True,
        )
        assert_matches_type(FlagCreateResponse, flag, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.logs.control.retention.flag.with_raw_response.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            flag=True,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        flag = await response.parse()
        assert_matches_type(FlagCreateResponse, flag, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.logs.control.retention.flag.with_streaming_response.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            flag=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            flag = await response.parse()
            assert_matches_type(FlagCreateResponse, flag, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_identifier` but received ''"):
            await async_client.logs.control.retention.flag.with_raw_response.create(
                "",
                flag=True,
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        flag = await async_client.logs.control.retention.flag.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(FlagGetResponse, flag, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.logs.control.retention.flag.with_raw_response.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        flag = await response.parse()
        assert_matches_type(FlagGetResponse, flag, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.logs.control.retention.flag.with_streaming_response.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            flag = await response.parse()
            assert_matches_type(FlagGetResponse, flag, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_identifier` but received ''"):
            await async_client.logs.control.retention.flag.with_raw_response.get(
                "",
            )
