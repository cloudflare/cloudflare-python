# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from cloudflare.types import (
    URLNormalizationURLNormalizationGetURLNormalizationSettingsResponse,
    URLNormalizationURLNormalizationUpdateURLNormalizationSettingsResponse,
)

from typing import Any, cast

import os
import pytest
import httpx
from typing_extensions import get_args
from typing import Optional
from respx import MockRouter
from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types import url_normalization_url_normalization_update_url_normalization_settings_params

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestURLNormalizations:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_url_normalization_get_url_normalization_settings(self, client: Cloudflare) -> None:
        url_normalization = client.url_normalizations.url_normalization_get_url_normalization_settings(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(
            URLNormalizationURLNormalizationGetURLNormalizationSettingsResponse, url_normalization, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_url_normalization_get_url_normalization_settings(self, client: Cloudflare) -> None:
        response = client.url_normalizations.with_raw_response.url_normalization_get_url_normalization_settings(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        url_normalization = response.parse()
        assert_matches_type(
            URLNormalizationURLNormalizationGetURLNormalizationSettingsResponse, url_normalization, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_url_normalization_get_url_normalization_settings(self, client: Cloudflare) -> None:
        with client.url_normalizations.with_streaming_response.url_normalization_get_url_normalization_settings(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            url_normalization = response.parse()
            assert_matches_type(
                URLNormalizationURLNormalizationGetURLNormalizationSettingsResponse,
                url_normalization,
                path=["response"],
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_url_normalization_get_url_normalization_settings(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.url_normalizations.with_raw_response.url_normalization_get_url_normalization_settings(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_url_normalization_update_url_normalization_settings(self, client: Cloudflare) -> None:
        url_normalization = client.url_normalizations.url_normalization_update_url_normalization_settings(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(
            URLNormalizationURLNormalizationUpdateURLNormalizationSettingsResponse, url_normalization, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    def test_method_url_normalization_update_url_normalization_settings_with_all_params(
        self, client: Cloudflare
    ) -> None:
        url_normalization = client.url_normalizations.url_normalization_update_url_normalization_settings(
            "023e105f4ecef8ad9ca31a8372d0c353",
            scope="incoming",
            type="cloudflare",
        )
        assert_matches_type(
            URLNormalizationURLNormalizationUpdateURLNormalizationSettingsResponse, url_normalization, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_url_normalization_update_url_normalization_settings(self, client: Cloudflare) -> None:
        response = client.url_normalizations.with_raw_response.url_normalization_update_url_normalization_settings(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        url_normalization = response.parse()
        assert_matches_type(
            URLNormalizationURLNormalizationUpdateURLNormalizationSettingsResponse, url_normalization, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_url_normalization_update_url_normalization_settings(self, client: Cloudflare) -> None:
        with client.url_normalizations.with_streaming_response.url_normalization_update_url_normalization_settings(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            url_normalization = response.parse()
            assert_matches_type(
                URLNormalizationURLNormalizationUpdateURLNormalizationSettingsResponse,
                url_normalization,
                path=["response"],
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_url_normalization_update_url_normalization_settings(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.url_normalizations.with_raw_response.url_normalization_update_url_normalization_settings(
                "",
            )


class TestAsyncURLNormalizations:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_url_normalization_get_url_normalization_settings(self, async_client: AsyncCloudflare) -> None:
        url_normalization = await async_client.url_normalizations.url_normalization_get_url_normalization_settings(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(
            URLNormalizationURLNormalizationGetURLNormalizationSettingsResponse, url_normalization, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_url_normalization_get_url_normalization_settings(
        self, async_client: AsyncCloudflare
    ) -> None:
        response = (
            await async_client.url_normalizations.with_raw_response.url_normalization_get_url_normalization_settings(
                "023e105f4ecef8ad9ca31a8372d0c353",
            )
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        url_normalization = await response.parse()
        assert_matches_type(
            URLNormalizationURLNormalizationGetURLNormalizationSettingsResponse, url_normalization, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_url_normalization_get_url_normalization_settings(
        self, async_client: AsyncCloudflare
    ) -> None:
        async with async_client.url_normalizations.with_streaming_response.url_normalization_get_url_normalization_settings(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            url_normalization = await response.parse()
            assert_matches_type(
                URLNormalizationURLNormalizationGetURLNormalizationSettingsResponse,
                url_normalization,
                path=["response"],
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_url_normalization_get_url_normalization_settings(
        self, async_client: AsyncCloudflare
    ) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.url_normalizations.with_raw_response.url_normalization_get_url_normalization_settings(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_url_normalization_update_url_normalization_settings(
        self, async_client: AsyncCloudflare
    ) -> None:
        url_normalization = await async_client.url_normalizations.url_normalization_update_url_normalization_settings(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(
            URLNormalizationURLNormalizationUpdateURLNormalizationSettingsResponse, url_normalization, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    async def test_method_url_normalization_update_url_normalization_settings_with_all_params(
        self, async_client: AsyncCloudflare
    ) -> None:
        url_normalization = await async_client.url_normalizations.url_normalization_update_url_normalization_settings(
            "023e105f4ecef8ad9ca31a8372d0c353",
            scope="incoming",
            type="cloudflare",
        )
        assert_matches_type(
            URLNormalizationURLNormalizationUpdateURLNormalizationSettingsResponse, url_normalization, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_url_normalization_update_url_normalization_settings(
        self, async_client: AsyncCloudflare
    ) -> None:
        response = (
            await async_client.url_normalizations.with_raw_response.url_normalization_update_url_normalization_settings(
                "023e105f4ecef8ad9ca31a8372d0c353",
            )
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        url_normalization = await response.parse()
        assert_matches_type(
            URLNormalizationURLNormalizationUpdateURLNormalizationSettingsResponse, url_normalization, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_url_normalization_update_url_normalization_settings(
        self, async_client: AsyncCloudflare
    ) -> None:
        async with async_client.url_normalizations.with_streaming_response.url_normalization_update_url_normalization_settings(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            url_normalization = await response.parse()
            assert_matches_type(
                URLNormalizationURLNormalizationUpdateURLNormalizationSettingsResponse,
                url_normalization,
                path=["response"],
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_url_normalization_update_url_normalization_settings(
        self, async_client: AsyncCloudflare
    ) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.url_normalizations.with_raw_response.url_normalization_update_url_normalization_settings(
                "",
            )
