# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.shared import UnnamedSchemaRef8d6a37a1e4190f86652802244d29525f

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestReceived:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        received = client.logs.received.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
            end="2018-05-20T10:01:00Z",
        )
        assert_matches_type(UnnamedSchemaRef8d6a37a1e4190f86652802244d29525f, received, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_get_with_all_params(self, client: Cloudflare) -> None:
        received = client.logs.received.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
            end="2018-05-20T10:01:00Z",
            count=1,
            fields="ClientIP,RayID,EdgeStartTimestamp",
            sample=0.1,
            start="2018-05-20T10:00:00Z",
            timestamps="unixnano",
        )
        assert_matches_type(UnnamedSchemaRef8d6a37a1e4190f86652802244d29525f, received, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.logs.received.with_raw_response.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
            end="2018-05-20T10:01:00Z",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        received = response.parse()
        assert_matches_type(UnnamedSchemaRef8d6a37a1e4190f86652802244d29525f, received, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.logs.received.with_streaming_response.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
            end="2018-05-20T10:01:00Z",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            received = response.parse()
            assert_matches_type(UnnamedSchemaRef8d6a37a1e4190f86652802244d29525f, received, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_identifier` but received ''"):
            client.logs.received.with_raw_response.get(
                "",
                end="2018-05-20T10:01:00Z",
            )


class TestAsyncReceived:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        received = await async_client.logs.received.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
            end="2018-05-20T10:01:00Z",
        )
        assert_matches_type(UnnamedSchemaRef8d6a37a1e4190f86652802244d29525f, received, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncCloudflare) -> None:
        received = await async_client.logs.received.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
            end="2018-05-20T10:01:00Z",
            count=1,
            fields="ClientIP,RayID,EdgeStartTimestamp",
            sample=0.1,
            start="2018-05-20T10:00:00Z",
            timestamps="unixnano",
        )
        assert_matches_type(UnnamedSchemaRef8d6a37a1e4190f86652802244d29525f, received, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.logs.received.with_raw_response.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
            end="2018-05-20T10:01:00Z",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        received = await response.parse()
        assert_matches_type(UnnamedSchemaRef8d6a37a1e4190f86652802244d29525f, received, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.logs.received.with_streaming_response.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
            end="2018-05-20T10:01:00Z",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            received = await response.parse()
            assert_matches_type(UnnamedSchemaRef8d6a37a1e4190f86652802244d29525f, received, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_identifier` but received ''"):
            await async_client.logs.received.with_raw_response.get(
                "",
                end="2018-05-20T10:01:00Z",
            )
