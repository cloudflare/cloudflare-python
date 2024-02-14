# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from cloudflare.types.dlps.profiles import PredefinedUpdateResponse, PredefinedGetResponse

from typing import Any, cast

import os
import pytest
import httpx
from typing_extensions import get_args
from typing import Optional
from respx import MockRouter
from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.dlps.profiles import predefined_update_params

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPredefineds:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        predefined = client.dlps.profiles.predefineds.update(
            "384e129d-25bd-403c-8019-bc19eb7a8a5f",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(PredefinedUpdateResponse, predefined, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update_with_all_params(self, client: Cloudflare) -> None:
        predefined = client.dlps.profiles.predefineds.update(
            "384e129d-25bd-403c-8019-bc19eb7a8a5f",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            allowed_match_count=5,
            entries=[{"enabled": True}, {"enabled": True}, {"enabled": True}],
        )
        assert_matches_type(PredefinedUpdateResponse, predefined, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.dlps.profiles.predefineds.with_raw_response.update(
            "384e129d-25bd-403c-8019-bc19eb7a8a5f",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        predefined = response.parse()
        assert_matches_type(PredefinedUpdateResponse, predefined, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.dlps.profiles.predefineds.with_streaming_response.update(
            "384e129d-25bd-403c-8019-bc19eb7a8a5f",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            predefined = response.parse()
            assert_matches_type(PredefinedUpdateResponse, predefined, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.dlps.profiles.predefineds.with_raw_response.update(
                "384e129d-25bd-403c-8019-bc19eb7a8a5f",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `profile_id` but received ''"):
            client.dlps.profiles.predefineds.with_raw_response.update(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        predefined = client.dlps.profiles.predefineds.get(
            "384e129d-25bd-403c-8019-bc19eb7a8a5f",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(PredefinedGetResponse, predefined, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.dlps.profiles.predefineds.with_raw_response.get(
            "384e129d-25bd-403c-8019-bc19eb7a8a5f",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        predefined = response.parse()
        assert_matches_type(PredefinedGetResponse, predefined, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.dlps.profiles.predefineds.with_streaming_response.get(
            "384e129d-25bd-403c-8019-bc19eb7a8a5f",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            predefined = response.parse()
            assert_matches_type(PredefinedGetResponse, predefined, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.dlps.profiles.predefineds.with_raw_response.get(
                "384e129d-25bd-403c-8019-bc19eb7a8a5f",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `profile_id` but received ''"):
            client.dlps.profiles.predefineds.with_raw_response.get(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )


class TestAsyncPredefineds:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        predefined = await async_client.dlps.profiles.predefineds.update(
            "384e129d-25bd-403c-8019-bc19eb7a8a5f",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(PredefinedUpdateResponse, predefined, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncCloudflare) -> None:
        predefined = await async_client.dlps.profiles.predefineds.update(
            "384e129d-25bd-403c-8019-bc19eb7a8a5f",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            allowed_match_count=5,
            entries=[{"enabled": True}, {"enabled": True}, {"enabled": True}],
        )
        assert_matches_type(PredefinedUpdateResponse, predefined, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dlps.profiles.predefineds.with_raw_response.update(
            "384e129d-25bd-403c-8019-bc19eb7a8a5f",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        predefined = await response.parse()
        assert_matches_type(PredefinedUpdateResponse, predefined, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.dlps.profiles.predefineds.with_streaming_response.update(
            "384e129d-25bd-403c-8019-bc19eb7a8a5f",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            predefined = await response.parse()
            assert_matches_type(PredefinedUpdateResponse, predefined, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.dlps.profiles.predefineds.with_raw_response.update(
                "384e129d-25bd-403c-8019-bc19eb7a8a5f",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `profile_id` but received ''"):
            await async_client.dlps.profiles.predefineds.with_raw_response.update(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        predefined = await async_client.dlps.profiles.predefineds.get(
            "384e129d-25bd-403c-8019-bc19eb7a8a5f",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(PredefinedGetResponse, predefined, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dlps.profiles.predefineds.with_raw_response.get(
            "384e129d-25bd-403c-8019-bc19eb7a8a5f",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        predefined = await response.parse()
        assert_matches_type(PredefinedGetResponse, predefined, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.dlps.profiles.predefineds.with_streaming_response.get(
            "384e129d-25bd-403c-8019-bc19eb7a8a5f",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            predefined = await response.parse()
            assert_matches_type(PredefinedGetResponse, predefined, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.dlps.profiles.predefineds.with_raw_response.get(
                "384e129d-25bd-403c-8019-bc19eb7a8a5f",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `profile_id` but received ''"):
            await async_client.dlps.profiles.predefineds.with_raw_response.get(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )
