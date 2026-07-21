# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.cloudforce_one.threat_events.indicators import (
    ByDatasetGetResponse,
    ByDatasetListResponse,
)

# pyright: reportDeprecated=false

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestByDataset:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            by_dataset = client.cloudforce_one.threat_events.indicators.by_dataset.list(
                dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="account_id",
            )

        assert_matches_type(ByDatasetListResponse, by_dataset, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Cloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            by_dataset = client.cloudforce_one.threat_events.indicators.by_dataset.list(
                dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="account_id",
                indicator_type="indicatorType",
                name="name",
                page=0,
                page_size=0,
                related_event=["string"],
            )

        assert_matches_type(ByDatasetListResponse, by_dataset, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            response = client.cloudforce_one.threat_events.indicators.by_dataset.with_raw_response.list(
                dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="account_id",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        by_dataset = response.parse()
        assert_matches_type(ByDatasetListResponse, by_dataset, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            with client.cloudforce_one.threat_events.indicators.by_dataset.with_streaming_response.list(
                dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="account_id",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                by_dataset = response.parse()
                assert_matches_type(ByDatasetListResponse, by_dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
                client.cloudforce_one.threat_events.indicators.by_dataset.with_raw_response.list(
                    dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    account_id="",
                )

            with pytest.raises(ValueError, match=r"Expected a non-empty value for `dataset_id` but received ''"):
                client.cloudforce_one.threat_events.indicators.by_dataset.with_raw_response.list(
                    dataset_id="",
                    account_id="account_id",
                )

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        by_dataset = client.cloudforce_one.threat_events.indicators.by_dataset.get(
            indicator_id="indicator_id",
            account_id="account_id",
            dataset_id="dataset_id",
        )
        assert_matches_type(ByDatasetGetResponse, by_dataset, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.cloudforce_one.threat_events.indicators.by_dataset.with_raw_response.get(
            indicator_id="indicator_id",
            account_id="account_id",
            dataset_id="dataset_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        by_dataset = response.parse()
        assert_matches_type(ByDatasetGetResponse, by_dataset, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.cloudforce_one.threat_events.indicators.by_dataset.with_streaming_response.get(
            indicator_id="indicator_id",
            account_id="account_id",
            dataset_id="dataset_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            by_dataset = response.parse()
            assert_matches_type(ByDatasetGetResponse, by_dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.cloudforce_one.threat_events.indicators.by_dataset.with_raw_response.get(
                indicator_id="indicator_id",
                account_id="",
                dataset_id="dataset_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dataset_id` but received ''"):
            client.cloudforce_one.threat_events.indicators.by_dataset.with_raw_response.get(
                indicator_id="indicator_id",
                account_id="account_id",
                dataset_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `indicator_id` but received ''"):
            client.cloudforce_one.threat_events.indicators.by_dataset.with_raw_response.get(
                indicator_id="",
                account_id="account_id",
                dataset_id="dataset_id",
            )


class TestAsyncByDataset:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            by_dataset = await async_client.cloudforce_one.threat_events.indicators.by_dataset.list(
                dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="account_id",
            )

        assert_matches_type(ByDatasetListResponse, by_dataset, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            by_dataset = await async_client.cloudforce_one.threat_events.indicators.by_dataset.list(
                dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="account_id",
                indicator_type="indicatorType",
                name="name",
                page=0,
                page_size=0,
                related_event=["string"],
            )

        assert_matches_type(ByDatasetListResponse, by_dataset, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            response = await async_client.cloudforce_one.threat_events.indicators.by_dataset.with_raw_response.list(
                dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="account_id",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        by_dataset = await response.parse()
        assert_matches_type(ByDatasetListResponse, by_dataset, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            async with async_client.cloudforce_one.threat_events.indicators.by_dataset.with_streaming_response.list(
                dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="account_id",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                by_dataset = await response.parse()
                assert_matches_type(ByDatasetListResponse, by_dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
                await async_client.cloudforce_one.threat_events.indicators.by_dataset.with_raw_response.list(
                    dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    account_id="",
                )

            with pytest.raises(ValueError, match=r"Expected a non-empty value for `dataset_id` but received ''"):
                await async_client.cloudforce_one.threat_events.indicators.by_dataset.with_raw_response.list(
                    dataset_id="",
                    account_id="account_id",
                )

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        by_dataset = await async_client.cloudforce_one.threat_events.indicators.by_dataset.get(
            indicator_id="indicator_id",
            account_id="account_id",
            dataset_id="dataset_id",
        )
        assert_matches_type(ByDatasetGetResponse, by_dataset, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.cloudforce_one.threat_events.indicators.by_dataset.with_raw_response.get(
            indicator_id="indicator_id",
            account_id="account_id",
            dataset_id="dataset_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        by_dataset = await response.parse()
        assert_matches_type(ByDatasetGetResponse, by_dataset, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.cloudforce_one.threat_events.indicators.by_dataset.with_streaming_response.get(
            indicator_id="indicator_id",
            account_id="account_id",
            dataset_id="dataset_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            by_dataset = await response.parse()
            assert_matches_type(ByDatasetGetResponse, by_dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.cloudforce_one.threat_events.indicators.by_dataset.with_raw_response.get(
                indicator_id="indicator_id",
                account_id="",
                dataset_id="dataset_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dataset_id` but received ''"):
            await async_client.cloudforce_one.threat_events.indicators.by_dataset.with_raw_response.get(
                indicator_id="indicator_id",
                account_id="account_id",
                dataset_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `indicator_id` but received ''"):
            await async_client.cloudforce_one.threat_events.indicators.by_dataset.with_raw_response.get(
                indicator_id="",
                account_id="account_id",
                dataset_id="dataset_id",
            )
