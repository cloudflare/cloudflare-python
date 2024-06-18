# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.zero_trust.dlp import Dataset
from cloudflare.types.zero_trust.dlp.datasets import NewVersion

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestUpload:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        upload = client.zero_trust.dlp.datasets.upload.create(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="string",
        )
        assert_matches_type(Optional[NewVersion], upload, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.zero_trust.dlp.datasets.upload.with_raw_response.create(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        upload = response.parse()
        assert_matches_type(Optional[NewVersion], upload, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.zero_trust.dlp.datasets.upload.with_streaming_response.create(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            upload = response.parse()
            assert_matches_type(Optional[NewVersion], upload, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.dlp.datasets.upload.with_raw_response.create(
                "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dataset_id` but received ''"):
            client.zero_trust.dlp.datasets.upload.with_raw_response.create(
                "",
                account_id="string",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_edit(self, client: Cloudflare) -> None:
        upload = client.zero_trust.dlp.datasets.upload.edit(
            0,
            account_id="string",
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            body="string",
        )
        assert_matches_type(Optional[Dataset], upload, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_edit(self, client: Cloudflare) -> None:
        response = client.zero_trust.dlp.datasets.upload.with_raw_response.edit(
            0,
            account_id="string",
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            body="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        upload = response.parse()
        assert_matches_type(Optional[Dataset], upload, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_edit(self, client: Cloudflare) -> None:
        with client.zero_trust.dlp.datasets.upload.with_streaming_response.edit(
            0,
            account_id="string",
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            body="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            upload = response.parse()
            assert_matches_type(Optional[Dataset], upload, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_edit(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.dlp.datasets.upload.with_raw_response.edit(
                0,
                account_id="",
                dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                body="string",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dataset_id` but received ''"):
            client.zero_trust.dlp.datasets.upload.with_raw_response.edit(
                0,
                account_id="string",
                dataset_id="",
                body="string",
            )


class TestAsyncUpload:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        upload = await async_client.zero_trust.dlp.datasets.upload.create(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="string",
        )
        assert_matches_type(Optional[NewVersion], upload, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.dlp.datasets.upload.with_raw_response.create(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        upload = await response.parse()
        assert_matches_type(Optional[NewVersion], upload, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.dlp.datasets.upload.with_streaming_response.create(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            upload = await response.parse()
            assert_matches_type(Optional[NewVersion], upload, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.dlp.datasets.upload.with_raw_response.create(
                "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dataset_id` but received ''"):
            await async_client.zero_trust.dlp.datasets.upload.with_raw_response.create(
                "",
                account_id="string",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_edit(self, async_client: AsyncCloudflare) -> None:
        upload = await async_client.zero_trust.dlp.datasets.upload.edit(
            0,
            account_id="string",
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            body="string",
        )
        assert_matches_type(Optional[Dataset], upload, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_edit(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.dlp.datasets.upload.with_raw_response.edit(
            0,
            account_id="string",
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            body="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        upload = await response.parse()
        assert_matches_type(Optional[Dataset], upload, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_edit(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.dlp.datasets.upload.with_streaming_response.edit(
            0,
            account_id="string",
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            body="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            upload = await response.parse()
            assert_matches_type(Optional[Dataset], upload, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_edit(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.dlp.datasets.upload.with_raw_response.edit(
                0,
                account_id="",
                dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                body="string",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dataset_id` but received ''"):
            await async_client.zero_trust.dlp.datasets.upload.with_raw_response.edit(
                0,
                account_id="string",
                dataset_id="",
                body="string",
            )
