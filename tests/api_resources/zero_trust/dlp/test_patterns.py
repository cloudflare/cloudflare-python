# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.zero_trust.dlp import PatternValidateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPatterns:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_validate(self, client: Cloudflare) -> None:
        pattern = client.zero_trust.dlp.patterns.validate(
            account_id="account_id",
            regex="regex",
        )
        assert_matches_type(Optional[PatternValidateResponse], pattern, path=["response"])

    @parametrize
    def test_method_validate_with_all_params(self, client: Cloudflare) -> None:
        pattern = client.zero_trust.dlp.patterns.validate(
            account_id="account_id",
            regex="regex",
            max_match_bytes=0,
        )
        assert_matches_type(Optional[PatternValidateResponse], pattern, path=["response"])

    @parametrize
    def test_raw_response_validate(self, client: Cloudflare) -> None:
        response = client.zero_trust.dlp.patterns.with_raw_response.validate(
            account_id="account_id",
            regex="regex",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pattern = response.parse()
        assert_matches_type(Optional[PatternValidateResponse], pattern, path=["response"])

    @parametrize
    def test_streaming_response_validate(self, client: Cloudflare) -> None:
        with client.zero_trust.dlp.patterns.with_streaming_response.validate(
            account_id="account_id",
            regex="regex",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pattern = response.parse()
            assert_matches_type(Optional[PatternValidateResponse], pattern, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_validate(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.dlp.patterns.with_raw_response.validate(
                account_id="",
                regex="regex",
            )


class TestAsyncPatterns:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_validate(self, async_client: AsyncCloudflare) -> None:
        pattern = await async_client.zero_trust.dlp.patterns.validate(
            account_id="account_id",
            regex="regex",
        )
        assert_matches_type(Optional[PatternValidateResponse], pattern, path=["response"])

    @parametrize
    async def test_method_validate_with_all_params(self, async_client: AsyncCloudflare) -> None:
        pattern = await async_client.zero_trust.dlp.patterns.validate(
            account_id="account_id",
            regex="regex",
            max_match_bytes=0,
        )
        assert_matches_type(Optional[PatternValidateResponse], pattern, path=["response"])

    @parametrize
    async def test_raw_response_validate(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.dlp.patterns.with_raw_response.validate(
            account_id="account_id",
            regex="regex",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pattern = await response.parse()
        assert_matches_type(Optional[PatternValidateResponse], pattern, path=["response"])

    @parametrize
    async def test_streaming_response_validate(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.dlp.patterns.with_streaming_response.validate(
            account_id="account_id",
            regex="regex",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pattern = await response.parse()
            assert_matches_type(Optional[PatternValidateResponse], pattern, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_validate(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.dlp.patterns.with_raw_response.validate(
                account_id="",
                regex="regex",
            )
