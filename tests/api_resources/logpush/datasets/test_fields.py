# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFields:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        field = client.logpush.datasets.fields.get(
            dataset_id="gateway_dns",
            account_id="account_id",
        )
        assert_matches_type(object, field, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_get_with_all_params(self, client: Cloudflare) -> None:
        field = client.logpush.datasets.fields.get(
            dataset_id="gateway_dns",
            account_id="account_id",
        )
        assert_matches_type(object, field, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.logpush.datasets.fields.with_raw_response.get(
            dataset_id="gateway_dns",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        field = response.parse()
        assert_matches_type(object, field, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.logpush.datasets.fields.with_streaming_response.get(
            dataset_id="gateway_dns",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            field = response.parse()
            assert_matches_type(object, field, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dataset_id` but received ''"):
            client.logpush.datasets.fields.with_raw_response.get(
                dataset_id="",
                account_id="account_id",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.logpush.datasets.fields.with_raw_response.get(
                dataset_id="gateway_dns",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.logpush.datasets.fields.with_raw_response.get(
                dataset_id="gateway_dns",
                account_id="account_id",
            )


class TestAsyncFields:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        field = await async_client.logpush.datasets.fields.get(
            dataset_id="gateway_dns",
            account_id="account_id",
        )
        assert_matches_type(object, field, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncCloudflare) -> None:
        field = await async_client.logpush.datasets.fields.get(
            dataset_id="gateway_dns",
            account_id="account_id",
        )
        assert_matches_type(object, field, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.logpush.datasets.fields.with_raw_response.get(
            dataset_id="gateway_dns",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        field = await response.parse()
        assert_matches_type(object, field, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.logpush.datasets.fields.with_streaming_response.get(
            dataset_id="gateway_dns",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            field = await response.parse()
            assert_matches_type(object, field, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dataset_id` but received ''"):
            await async_client.logpush.datasets.fields.with_raw_response.get(
                dataset_id="",
                account_id="account_id",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.logpush.datasets.fields.with_raw_response.get(
                dataset_id="gateway_dns",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.logpush.datasets.fields.with_raw_response.get(
                dataset_id="gateway_dns",
                account_id="account_id",
            )
