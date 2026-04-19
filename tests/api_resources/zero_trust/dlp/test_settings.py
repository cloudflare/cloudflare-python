# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.zero_trust.dlp import DLPSettings

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSettings:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        setting = client.zero_trust.dlp.settings.update(
            account_id="account_id",
        )
        assert_matches_type(Optional[DLPSettings], setting, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Cloudflare) -> None:
        setting = client.zero_trust.dlp.settings.update(
            account_id="account_id",
            ai_context_analysis=True,
            ocr=True,
            payload_logging={
                "masking_level": "full",
                "public_key": "public_key",
            },
        )
        assert_matches_type(Optional[DLPSettings], setting, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.zero_trust.dlp.settings.with_raw_response.update(
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = response.parse()
        assert_matches_type(Optional[DLPSettings], setting, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.zero_trust.dlp.settings.with_streaming_response.update(
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = response.parse()
            assert_matches_type(Optional[DLPSettings], setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.dlp.settings.with_raw_response.update(
                account_id="",
            )

    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        setting = client.zero_trust.dlp.settings.delete(
            account_id="account_id",
        )
        assert_matches_type(Optional[DLPSettings], setting, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.zero_trust.dlp.settings.with_raw_response.delete(
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = response.parse()
        assert_matches_type(Optional[DLPSettings], setting, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.zero_trust.dlp.settings.with_streaming_response.delete(
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = response.parse()
            assert_matches_type(Optional[DLPSettings], setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.dlp.settings.with_raw_response.delete(
                account_id="",
            )

    @parametrize
    def test_method_edit(self, client: Cloudflare) -> None:
        setting = client.zero_trust.dlp.settings.edit(
            account_id="account_id",
        )
        assert_matches_type(Optional[DLPSettings], setting, path=["response"])

    @parametrize
    def test_method_edit_with_all_params(self, client: Cloudflare) -> None:
        setting = client.zero_trust.dlp.settings.edit(
            account_id="account_id",
            ai_context_analysis=True,
            ocr=True,
            payload_logging={
                "masking_level": "full",
                "public_key": "public_key",
            },
        )
        assert_matches_type(Optional[DLPSettings], setting, path=["response"])

    @parametrize
    def test_raw_response_edit(self, client: Cloudflare) -> None:
        response = client.zero_trust.dlp.settings.with_raw_response.edit(
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = response.parse()
        assert_matches_type(Optional[DLPSettings], setting, path=["response"])

    @parametrize
    def test_streaming_response_edit(self, client: Cloudflare) -> None:
        with client.zero_trust.dlp.settings.with_streaming_response.edit(
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = response.parse()
            assert_matches_type(Optional[DLPSettings], setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_edit(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.dlp.settings.with_raw_response.edit(
                account_id="",
            )

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        setting = client.zero_trust.dlp.settings.get(
            account_id="account_id",
        )
        assert_matches_type(Optional[DLPSettings], setting, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.zero_trust.dlp.settings.with_raw_response.get(
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = response.parse()
        assert_matches_type(Optional[DLPSettings], setting, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.zero_trust.dlp.settings.with_streaming_response.get(
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = response.parse()
            assert_matches_type(Optional[DLPSettings], setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.dlp.settings.with_raw_response.get(
                account_id="",
            )


class TestAsyncSettings:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        setting = await async_client.zero_trust.dlp.settings.update(
            account_id="account_id",
        )
        assert_matches_type(Optional[DLPSettings], setting, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncCloudflare) -> None:
        setting = await async_client.zero_trust.dlp.settings.update(
            account_id="account_id",
            ai_context_analysis=True,
            ocr=True,
            payload_logging={
                "masking_level": "full",
                "public_key": "public_key",
            },
        )
        assert_matches_type(Optional[DLPSettings], setting, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.dlp.settings.with_raw_response.update(
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = await response.parse()
        assert_matches_type(Optional[DLPSettings], setting, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.dlp.settings.with_streaming_response.update(
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = await response.parse()
            assert_matches_type(Optional[DLPSettings], setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.dlp.settings.with_raw_response.update(
                account_id="",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        setting = await async_client.zero_trust.dlp.settings.delete(
            account_id="account_id",
        )
        assert_matches_type(Optional[DLPSettings], setting, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.dlp.settings.with_raw_response.delete(
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = await response.parse()
        assert_matches_type(Optional[DLPSettings], setting, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.dlp.settings.with_streaming_response.delete(
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = await response.parse()
            assert_matches_type(Optional[DLPSettings], setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.dlp.settings.with_raw_response.delete(
                account_id="",
            )

    @parametrize
    async def test_method_edit(self, async_client: AsyncCloudflare) -> None:
        setting = await async_client.zero_trust.dlp.settings.edit(
            account_id="account_id",
        )
        assert_matches_type(Optional[DLPSettings], setting, path=["response"])

    @parametrize
    async def test_method_edit_with_all_params(self, async_client: AsyncCloudflare) -> None:
        setting = await async_client.zero_trust.dlp.settings.edit(
            account_id="account_id",
            ai_context_analysis=True,
            ocr=True,
            payload_logging={
                "masking_level": "full",
                "public_key": "public_key",
            },
        )
        assert_matches_type(Optional[DLPSettings], setting, path=["response"])

    @parametrize
    async def test_raw_response_edit(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.dlp.settings.with_raw_response.edit(
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = await response.parse()
        assert_matches_type(Optional[DLPSettings], setting, path=["response"])

    @parametrize
    async def test_streaming_response_edit(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.dlp.settings.with_streaming_response.edit(
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = await response.parse()
            assert_matches_type(Optional[DLPSettings], setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_edit(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.dlp.settings.with_raw_response.edit(
                account_id="",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        setting = await async_client.zero_trust.dlp.settings.get(
            account_id="account_id",
        )
        assert_matches_type(Optional[DLPSettings], setting, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.dlp.settings.with_raw_response.get(
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = await response.parse()
        assert_matches_type(Optional[DLPSettings], setting, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.dlp.settings.with_streaming_response.get(
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = await response.parse()
            assert_matches_type(Optional[DLPSettings], setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.dlp.settings.with_raw_response.get(
                account_id="",
            )
