# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.email_security.investigate import PreviewGetResponse, PreviewCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPreview:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        preview = client.email_security.investigate.preview.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            postfix_id="4Njp3P0STMz2c02Q",
        )
        assert_matches_type(PreviewCreateResponse, preview, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.email_security.investigate.preview.with_raw_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            postfix_id="4Njp3P0STMz2c02Q",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        preview = response.parse()
        assert_matches_type(PreviewCreateResponse, preview, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.email_security.investigate.preview.with_streaming_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            postfix_id="4Njp3P0STMz2c02Q",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            preview = response.parse()
            assert_matches_type(PreviewCreateResponse, preview, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.email_security.investigate.preview.with_raw_response.create(
                account_id="",
                postfix_id="4Njp3P0STMz2c02Q",
            )

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        preview = client.email_security.investigate.preview.get(
            postfix_id="4Njp3P0STMz2c02Q",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(PreviewGetResponse, preview, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.email_security.investigate.preview.with_raw_response.get(
            postfix_id="4Njp3P0STMz2c02Q",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        preview = response.parse()
        assert_matches_type(PreviewGetResponse, preview, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.email_security.investigate.preview.with_streaming_response.get(
            postfix_id="4Njp3P0STMz2c02Q",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            preview = response.parse()
            assert_matches_type(PreviewGetResponse, preview, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.email_security.investigate.preview.with_raw_response.get(
                postfix_id="4Njp3P0STMz2c02Q",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `postfix_id` but received ''"):
            client.email_security.investigate.preview.with_raw_response.get(
                postfix_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )


class TestAsyncPreview:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        preview = await async_client.email_security.investigate.preview.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            postfix_id="4Njp3P0STMz2c02Q",
        )
        assert_matches_type(PreviewCreateResponse, preview, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.email_security.investigate.preview.with_raw_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            postfix_id="4Njp3P0STMz2c02Q",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        preview = await response.parse()
        assert_matches_type(PreviewCreateResponse, preview, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.email_security.investigate.preview.with_streaming_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            postfix_id="4Njp3P0STMz2c02Q",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            preview = await response.parse()
            assert_matches_type(PreviewCreateResponse, preview, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.email_security.investigate.preview.with_raw_response.create(
                account_id="",
                postfix_id="4Njp3P0STMz2c02Q",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        preview = await async_client.email_security.investigate.preview.get(
            postfix_id="4Njp3P0STMz2c02Q",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(PreviewGetResponse, preview, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.email_security.investigate.preview.with_raw_response.get(
            postfix_id="4Njp3P0STMz2c02Q",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        preview = await response.parse()
        assert_matches_type(PreviewGetResponse, preview, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.email_security.investigate.preview.with_streaming_response.get(
            postfix_id="4Njp3P0STMz2c02Q",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            preview = await response.parse()
            assert_matches_type(PreviewGetResponse, preview, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.email_security.investigate.preview.with_raw_response.get(
                postfix_id="4Njp3P0STMz2c02Q",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `postfix_id` but received ''"):
            await async_client.email_security.investigate.preview.with_raw_response.get(
                postfix_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )
