# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Optional, Any, cast

from cloudflare.types.settings import NELUpdateResponse, NELGetResponse

import os
import pytest
import httpx
from typing_extensions import get_args
from typing import Optional
from respx import MockRouter
from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.settings import nel_update_params

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestNEL:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        nel = client.settings.nel.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            value={
                "id": "nel",
                "value": {},
            },
        )
        assert_matches_type(Optional[NELUpdateResponse], nel, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update_with_all_params(self, client: Cloudflare) -> None:
        nel = client.settings.nel.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            value={
                "id": "nel",
                "value": {"enabled": False},
            },
        )
        assert_matches_type(Optional[NELUpdateResponse], nel, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.settings.nel.with_raw_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            value={
                "id": "nel",
                "value": {},
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        nel = response.parse()
        assert_matches_type(Optional[NELUpdateResponse], nel, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.settings.nel.with_streaming_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            value={
                "id": "nel",
                "value": {},
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            nel = response.parse()
            assert_matches_type(Optional[NELUpdateResponse], nel, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.settings.nel.with_raw_response.update(
                "",
                value={
                    "id": "nel",
                    "value": {},
                },
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        nel = client.settings.nel.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[NELGetResponse], nel, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.settings.nel.with_raw_response.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        nel = response.parse()
        assert_matches_type(Optional[NELGetResponse], nel, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.settings.nel.with_streaming_response.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            nel = response.parse()
            assert_matches_type(Optional[NELGetResponse], nel, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.settings.nel.with_raw_response.get(
                "",
            )


class TestAsyncNEL:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        nel = await async_client.settings.nel.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            value={
                "id": "nel",
                "value": {},
            },
        )
        assert_matches_type(Optional[NELUpdateResponse], nel, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncCloudflare) -> None:
        nel = await async_client.settings.nel.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            value={
                "id": "nel",
                "value": {"enabled": False},
            },
        )
        assert_matches_type(Optional[NELUpdateResponse], nel, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.settings.nel.with_raw_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            value={
                "id": "nel",
                "value": {},
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        nel = await response.parse()
        assert_matches_type(Optional[NELUpdateResponse], nel, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.settings.nel.with_streaming_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            value={
                "id": "nel",
                "value": {},
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            nel = await response.parse()
            assert_matches_type(Optional[NELUpdateResponse], nel, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.settings.nel.with_raw_response.update(
                "",
                value={
                    "id": "nel",
                    "value": {},
                },
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        nel = await async_client.settings.nel.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[NELGetResponse], nel, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.settings.nel.with_raw_response.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        nel = await response.parse()
        assert_matches_type(Optional[NELGetResponse], nel, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.settings.nel.with_streaming_response.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            nel = await response.parse()
            assert_matches_type(Optional[NELGetResponse], nel, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.settings.nel.with_raw_response.get(
                "",
            )
