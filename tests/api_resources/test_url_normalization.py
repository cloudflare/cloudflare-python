# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.url_normalization import (
    URLNormalizationGetResponse,
    URLNormalizationUpdateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestURLNormalization:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="TODO: investigate unauthorized HTTP response")
    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        url_normalization = client.url_normalization.update(
            zone_id="9f1839b6152d298aca64c4e906b6d074",
            scope="incoming",
            type="cloudflare",
        )
        assert_matches_type(URLNormalizationUpdateResponse, url_normalization, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate unauthorized HTTP response")
    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.url_normalization.with_raw_response.update(
            zone_id="9f1839b6152d298aca64c4e906b6d074",
            scope="incoming",
            type="cloudflare",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        url_normalization = response.parse()
        assert_matches_type(URLNormalizationUpdateResponse, url_normalization, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate unauthorized HTTP response")
    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.url_normalization.with_streaming_response.update(
            zone_id="9f1839b6152d298aca64c4e906b6d074",
            scope="incoming",
            type="cloudflare",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            url_normalization = response.parse()
            assert_matches_type(URLNormalizationUpdateResponse, url_normalization, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate unauthorized HTTP response")
    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.url_normalization.with_raw_response.update(
                zone_id="",
                scope="incoming",
                type="cloudflare",
            )

    @pytest.mark.skip(reason="TODO: investigate unauthorized HTTP response")
    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        url_normalization = client.url_normalization.delete(
            zone_id="9f1839b6152d298aca64c4e906b6d074",
        )
        assert url_normalization is None

    @pytest.mark.skip(reason="TODO: investigate unauthorized HTTP response")
    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.url_normalization.with_raw_response.delete(
            zone_id="9f1839b6152d298aca64c4e906b6d074",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        url_normalization = response.parse()
        assert url_normalization is None

    @pytest.mark.skip(reason="TODO: investigate unauthorized HTTP response")
    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.url_normalization.with_streaming_response.delete(
            zone_id="9f1839b6152d298aca64c4e906b6d074",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            url_normalization = response.parse()
            assert url_normalization is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate unauthorized HTTP response")
    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.url_normalization.with_raw_response.delete(
                zone_id="",
            )

    @pytest.mark.skip(reason="TODO: investigate unauthorized HTTP response")
    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        url_normalization = client.url_normalization.get(
            zone_id="9f1839b6152d298aca64c4e906b6d074",
        )
        assert_matches_type(URLNormalizationGetResponse, url_normalization, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate unauthorized HTTP response")
    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.url_normalization.with_raw_response.get(
            zone_id="9f1839b6152d298aca64c4e906b6d074",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        url_normalization = response.parse()
        assert_matches_type(URLNormalizationGetResponse, url_normalization, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate unauthorized HTTP response")
    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.url_normalization.with_streaming_response.get(
            zone_id="9f1839b6152d298aca64c4e906b6d074",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            url_normalization = response.parse()
            assert_matches_type(URLNormalizationGetResponse, url_normalization, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate unauthorized HTTP response")
    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.url_normalization.with_raw_response.get(
                zone_id="",
            )


class TestAsyncURLNormalization:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="TODO: investigate unauthorized HTTP response")
    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        url_normalization = await async_client.url_normalization.update(
            zone_id="9f1839b6152d298aca64c4e906b6d074",
            scope="incoming",
            type="cloudflare",
        )
        assert_matches_type(URLNormalizationUpdateResponse, url_normalization, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate unauthorized HTTP response")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.url_normalization.with_raw_response.update(
            zone_id="9f1839b6152d298aca64c4e906b6d074",
            scope="incoming",
            type="cloudflare",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        url_normalization = await response.parse()
        assert_matches_type(URLNormalizationUpdateResponse, url_normalization, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate unauthorized HTTP response")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.url_normalization.with_streaming_response.update(
            zone_id="9f1839b6152d298aca64c4e906b6d074",
            scope="incoming",
            type="cloudflare",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            url_normalization = await response.parse()
            assert_matches_type(URLNormalizationUpdateResponse, url_normalization, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate unauthorized HTTP response")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.url_normalization.with_raw_response.update(
                zone_id="",
                scope="incoming",
                type="cloudflare",
            )

    @pytest.mark.skip(reason="TODO: investigate unauthorized HTTP response")
    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        url_normalization = await async_client.url_normalization.delete(
            zone_id="9f1839b6152d298aca64c4e906b6d074",
        )
        assert url_normalization is None

    @pytest.mark.skip(reason="TODO: investigate unauthorized HTTP response")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.url_normalization.with_raw_response.delete(
            zone_id="9f1839b6152d298aca64c4e906b6d074",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        url_normalization = await response.parse()
        assert url_normalization is None

    @pytest.mark.skip(reason="TODO: investigate unauthorized HTTP response")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.url_normalization.with_streaming_response.delete(
            zone_id="9f1839b6152d298aca64c4e906b6d074",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            url_normalization = await response.parse()
            assert url_normalization is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate unauthorized HTTP response")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.url_normalization.with_raw_response.delete(
                zone_id="",
            )

    @pytest.mark.skip(reason="TODO: investigate unauthorized HTTP response")
    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        url_normalization = await async_client.url_normalization.get(
            zone_id="9f1839b6152d298aca64c4e906b6d074",
        )
        assert_matches_type(URLNormalizationGetResponse, url_normalization, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate unauthorized HTTP response")
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.url_normalization.with_raw_response.get(
            zone_id="9f1839b6152d298aca64c4e906b6d074",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        url_normalization = await response.parse()
        assert_matches_type(URLNormalizationGetResponse, url_normalization, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate unauthorized HTTP response")
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.url_normalization.with_streaming_response.get(
            zone_id="9f1839b6152d298aca64c4e906b6d074",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            url_normalization = await response.parse()
            assert_matches_type(URLNormalizationGetResponse, url_normalization, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate unauthorized HTTP response")
    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.url_normalization.with_raw_response.get(
                zone_id="",
            )
