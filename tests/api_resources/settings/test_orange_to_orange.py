# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.settings import (
    OrangeToOrangeGetResponse,
    OrangeToOrangeUpdateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestOrangeToOrange:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        orange_to_orange = client.settings.orange_to_orange.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            value={
                "id": "orange_to_orange",
                "value": "on",
            },
        )
        assert_matches_type(Optional[OrangeToOrangeUpdateResponse], orange_to_orange, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update_with_all_params(self, client: Cloudflare) -> None:
        orange_to_orange = client.settings.orange_to_orange.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            value={
                "id": "orange_to_orange",
                "value": "on",
            },
        )
        assert_matches_type(Optional[OrangeToOrangeUpdateResponse], orange_to_orange, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.settings.orange_to_orange.with_raw_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            value={
                "id": "orange_to_orange",
                "value": "on",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        orange_to_orange = response.parse()
        assert_matches_type(Optional[OrangeToOrangeUpdateResponse], orange_to_orange, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.settings.orange_to_orange.with_streaming_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            value={
                "id": "orange_to_orange",
                "value": "on",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            orange_to_orange = response.parse()
            assert_matches_type(Optional[OrangeToOrangeUpdateResponse], orange_to_orange, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.settings.orange_to_orange.with_raw_response.update(
                "",
                value={
                    "id": "orange_to_orange",
                    "value": "on",
                },
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        orange_to_orange = client.settings.orange_to_orange.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[OrangeToOrangeGetResponse], orange_to_orange, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.settings.orange_to_orange.with_raw_response.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        orange_to_orange = response.parse()
        assert_matches_type(Optional[OrangeToOrangeGetResponse], orange_to_orange, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.settings.orange_to_orange.with_streaming_response.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            orange_to_orange = response.parse()
            assert_matches_type(Optional[OrangeToOrangeGetResponse], orange_to_orange, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.settings.orange_to_orange.with_raw_response.get(
                "",
            )


class TestAsyncOrangeToOrange:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        orange_to_orange = await async_client.settings.orange_to_orange.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            value={
                "id": "orange_to_orange",
                "value": "on",
            },
        )
        assert_matches_type(Optional[OrangeToOrangeUpdateResponse], orange_to_orange, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncCloudflare) -> None:
        orange_to_orange = await async_client.settings.orange_to_orange.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            value={
                "id": "orange_to_orange",
                "value": "on",
            },
        )
        assert_matches_type(Optional[OrangeToOrangeUpdateResponse], orange_to_orange, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.settings.orange_to_orange.with_raw_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            value={
                "id": "orange_to_orange",
                "value": "on",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        orange_to_orange = await response.parse()
        assert_matches_type(Optional[OrangeToOrangeUpdateResponse], orange_to_orange, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.settings.orange_to_orange.with_streaming_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            value={
                "id": "orange_to_orange",
                "value": "on",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            orange_to_orange = await response.parse()
            assert_matches_type(Optional[OrangeToOrangeUpdateResponse], orange_to_orange, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.settings.orange_to_orange.with_raw_response.update(
                "",
                value={
                    "id": "orange_to_orange",
                    "value": "on",
                },
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        orange_to_orange = await async_client.settings.orange_to_orange.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[OrangeToOrangeGetResponse], orange_to_orange, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.settings.orange_to_orange.with_raw_response.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        orange_to_orange = await response.parse()
        assert_matches_type(Optional[OrangeToOrangeGetResponse], orange_to_orange, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.settings.orange_to_orange.with_streaming_response.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            orange_to_orange = await response.parse()
            assert_matches_type(Optional[OrangeToOrangeGetResponse], orange_to_orange, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.settings.orange_to_orange.with_raw_response.get(
                "",
            )
