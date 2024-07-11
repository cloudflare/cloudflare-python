# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.stream import Caption

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestLanguage:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        language = client.stream.captions.language.create(
            language="tr",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            identifier="ea95132c15732412d22c1476fa83f27a",
        )
        assert_matches_type(Optional[Caption], language, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.stream.captions.language.with_raw_response.create(
            language="tr",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            identifier="ea95132c15732412d22c1476fa83f27a",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        language = response.parse()
        assert_matches_type(Optional[Caption], language, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.stream.captions.language.with_streaming_response.create(
            language="tr",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            identifier="ea95132c15732412d22c1476fa83f27a",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            language = response.parse()
            assert_matches_type(Optional[Caption], language, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.stream.captions.language.with_raw_response.create(
                language="tr",
                account_id="",
                identifier="ea95132c15732412d22c1476fa83f27a",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identifier` but received ''"):
            client.stream.captions.language.with_raw_response.create(
                language="tr",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                identifier="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `language` but received ''"):
            client.stream.captions.language.with_raw_response.create(
                language="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                identifier="ea95132c15732412d22c1476fa83f27a",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        language = client.stream.captions.language.update(
            language="tr",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            identifier="ea95132c15732412d22c1476fa83f27a",
            file="@/Users/kyle/Desktop/tr.vtt",
        )
        assert_matches_type(Optional[Caption], language, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.stream.captions.language.with_raw_response.update(
            language="tr",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            identifier="ea95132c15732412d22c1476fa83f27a",
            file="@/Users/kyle/Desktop/tr.vtt",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        language = response.parse()
        assert_matches_type(Optional[Caption], language, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.stream.captions.language.with_streaming_response.update(
            language="tr",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            identifier="ea95132c15732412d22c1476fa83f27a",
            file="@/Users/kyle/Desktop/tr.vtt",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            language = response.parse()
            assert_matches_type(Optional[Caption], language, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.stream.captions.language.with_raw_response.update(
                language="tr",
                account_id="",
                identifier="ea95132c15732412d22c1476fa83f27a",
                file="@/Users/kyle/Desktop/tr.vtt",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identifier` but received ''"):
            client.stream.captions.language.with_raw_response.update(
                language="tr",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                identifier="",
                file="@/Users/kyle/Desktop/tr.vtt",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `language` but received ''"):
            client.stream.captions.language.with_raw_response.update(
                language="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                identifier="ea95132c15732412d22c1476fa83f27a",
                file="@/Users/kyle/Desktop/tr.vtt",
            )

    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        language = client.stream.captions.language.delete(
            language="tr",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            identifier="ea95132c15732412d22c1476fa83f27a",
        )
        assert_matches_type(str, language, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.stream.captions.language.with_raw_response.delete(
            language="tr",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            identifier="ea95132c15732412d22c1476fa83f27a",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        language = response.parse()
        assert_matches_type(str, language, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.stream.captions.language.with_streaming_response.delete(
            language="tr",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            identifier="ea95132c15732412d22c1476fa83f27a",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            language = response.parse()
            assert_matches_type(str, language, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.stream.captions.language.with_raw_response.delete(
                language="tr",
                account_id="",
                identifier="ea95132c15732412d22c1476fa83f27a",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identifier` but received ''"):
            client.stream.captions.language.with_raw_response.delete(
                language="tr",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                identifier="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `language` but received ''"):
            client.stream.captions.language.with_raw_response.delete(
                language="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                identifier="ea95132c15732412d22c1476fa83f27a",
            )

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        language = client.stream.captions.language.get(
            language="tr",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            identifier="ea95132c15732412d22c1476fa83f27a",
        )
        assert_matches_type(Optional[Caption], language, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.stream.captions.language.with_raw_response.get(
            language="tr",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            identifier="ea95132c15732412d22c1476fa83f27a",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        language = response.parse()
        assert_matches_type(Optional[Caption], language, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.stream.captions.language.with_streaming_response.get(
            language="tr",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            identifier="ea95132c15732412d22c1476fa83f27a",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            language = response.parse()
            assert_matches_type(Optional[Caption], language, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.stream.captions.language.with_raw_response.get(
                language="tr",
                account_id="",
                identifier="ea95132c15732412d22c1476fa83f27a",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identifier` but received ''"):
            client.stream.captions.language.with_raw_response.get(
                language="tr",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                identifier="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `language` but received ''"):
            client.stream.captions.language.with_raw_response.get(
                language="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                identifier="ea95132c15732412d22c1476fa83f27a",
            )


class TestAsyncLanguage:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        language = await async_client.stream.captions.language.create(
            language="tr",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            identifier="ea95132c15732412d22c1476fa83f27a",
        )
        assert_matches_type(Optional[Caption], language, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.stream.captions.language.with_raw_response.create(
            language="tr",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            identifier="ea95132c15732412d22c1476fa83f27a",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        language = await response.parse()
        assert_matches_type(Optional[Caption], language, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.stream.captions.language.with_streaming_response.create(
            language="tr",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            identifier="ea95132c15732412d22c1476fa83f27a",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            language = await response.parse()
            assert_matches_type(Optional[Caption], language, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.stream.captions.language.with_raw_response.create(
                language="tr",
                account_id="",
                identifier="ea95132c15732412d22c1476fa83f27a",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identifier` but received ''"):
            await async_client.stream.captions.language.with_raw_response.create(
                language="tr",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                identifier="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `language` but received ''"):
            await async_client.stream.captions.language.with_raw_response.create(
                language="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                identifier="ea95132c15732412d22c1476fa83f27a",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        language = await async_client.stream.captions.language.update(
            language="tr",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            identifier="ea95132c15732412d22c1476fa83f27a",
            file="@/Users/kyle/Desktop/tr.vtt",
        )
        assert_matches_type(Optional[Caption], language, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.stream.captions.language.with_raw_response.update(
            language="tr",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            identifier="ea95132c15732412d22c1476fa83f27a",
            file="@/Users/kyle/Desktop/tr.vtt",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        language = await response.parse()
        assert_matches_type(Optional[Caption], language, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.stream.captions.language.with_streaming_response.update(
            language="tr",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            identifier="ea95132c15732412d22c1476fa83f27a",
            file="@/Users/kyle/Desktop/tr.vtt",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            language = await response.parse()
            assert_matches_type(Optional[Caption], language, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.stream.captions.language.with_raw_response.update(
                language="tr",
                account_id="",
                identifier="ea95132c15732412d22c1476fa83f27a",
                file="@/Users/kyle/Desktop/tr.vtt",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identifier` but received ''"):
            await async_client.stream.captions.language.with_raw_response.update(
                language="tr",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                identifier="",
                file="@/Users/kyle/Desktop/tr.vtt",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `language` but received ''"):
            await async_client.stream.captions.language.with_raw_response.update(
                language="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                identifier="ea95132c15732412d22c1476fa83f27a",
                file="@/Users/kyle/Desktop/tr.vtt",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        language = await async_client.stream.captions.language.delete(
            language="tr",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            identifier="ea95132c15732412d22c1476fa83f27a",
        )
        assert_matches_type(str, language, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.stream.captions.language.with_raw_response.delete(
            language="tr",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            identifier="ea95132c15732412d22c1476fa83f27a",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        language = await response.parse()
        assert_matches_type(str, language, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.stream.captions.language.with_streaming_response.delete(
            language="tr",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            identifier="ea95132c15732412d22c1476fa83f27a",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            language = await response.parse()
            assert_matches_type(str, language, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.stream.captions.language.with_raw_response.delete(
                language="tr",
                account_id="",
                identifier="ea95132c15732412d22c1476fa83f27a",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identifier` but received ''"):
            await async_client.stream.captions.language.with_raw_response.delete(
                language="tr",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                identifier="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `language` but received ''"):
            await async_client.stream.captions.language.with_raw_response.delete(
                language="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                identifier="ea95132c15732412d22c1476fa83f27a",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        language = await async_client.stream.captions.language.get(
            language="tr",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            identifier="ea95132c15732412d22c1476fa83f27a",
        )
        assert_matches_type(Optional[Caption], language, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.stream.captions.language.with_raw_response.get(
            language="tr",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            identifier="ea95132c15732412d22c1476fa83f27a",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        language = await response.parse()
        assert_matches_type(Optional[Caption], language, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.stream.captions.language.with_streaming_response.get(
            language="tr",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            identifier="ea95132c15732412d22c1476fa83f27a",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            language = await response.parse()
            assert_matches_type(Optional[Caption], language, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.stream.captions.language.with_raw_response.get(
                language="tr",
                account_id="",
                identifier="ea95132c15732412d22c1476fa83f27a",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identifier` but received ''"):
            await async_client.stream.captions.language.with_raw_response.get(
                language="tr",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                identifier="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `language` but received ''"):
            await async_client.stream.captions.language.with_raw_response.get(
                language="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                identifier="ea95132c15732412d22c1476fa83f27a",
            )
