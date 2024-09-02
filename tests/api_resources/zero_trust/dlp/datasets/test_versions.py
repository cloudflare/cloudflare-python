# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from cloudflare import Cloudflare, AsyncCloudflare

from typing import Optional, Any, cast

from cloudflare.types.zero_trust.dlp.datasets import VersionCreateResponse

import os
import pytest
import httpx
from typing_extensions import get_args
from typing import Optional
from respx import MockRouter
from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.zero_trust.dlp.datasets import version_create_params

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestVersions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        version = client.zero_trust.dlp.datasets.versions.create(
            version=0,
            account_id="account_id",
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            body=[
                {"entry_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"},
                {"entry_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"},
                {"entry_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"},
            ],
        )
        assert_matches_type(Optional[VersionCreateResponse], version, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.zero_trust.dlp.datasets.versions.with_raw_response.create(
            version=0,
            account_id="account_id",
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            body=[
                {"entry_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"},
                {"entry_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"},
                {"entry_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"},
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        version = response.parse()
        assert_matches_type(Optional[VersionCreateResponse], version, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.zero_trust.dlp.datasets.versions.with_streaming_response.create(
            version=0,
            account_id="account_id",
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            body=[
                {"entry_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"},
                {"entry_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"},
                {"entry_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"},
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            version = response.parse()
            assert_matches_type(Optional[VersionCreateResponse], version, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.dlp.datasets.versions.with_raw_response.create(
                version=0,
                account_id="",
                dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                body=[
                    {"entry_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"},
                    {"entry_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"},
                    {"entry_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"},
                ],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dataset_id` but received ''"):
            client.zero_trust.dlp.datasets.versions.with_raw_response.create(
                version=0,
                account_id="account_id",
                dataset_id="",
                body=[
                    {"entry_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"},
                    {"entry_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"},
                    {"entry_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"},
                ],
            )


class TestAsyncVersions:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        version = await async_client.zero_trust.dlp.datasets.versions.create(
            version=0,
            account_id="account_id",
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            body=[
                {"entry_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"},
                {"entry_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"},
                {"entry_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"},
            ],
        )
        assert_matches_type(Optional[VersionCreateResponse], version, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.dlp.datasets.versions.with_raw_response.create(
            version=0,
            account_id="account_id",
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            body=[
                {"entry_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"},
                {"entry_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"},
                {"entry_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"},
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        version = await response.parse()
        assert_matches_type(Optional[VersionCreateResponse], version, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.dlp.datasets.versions.with_streaming_response.create(
            version=0,
            account_id="account_id",
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            body=[
                {"entry_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"},
                {"entry_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"},
                {"entry_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"},
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            version = await response.parse()
            assert_matches_type(Optional[VersionCreateResponse], version, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.dlp.datasets.versions.with_raw_response.create(
                version=0,
                account_id="",
                dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                body=[
                    {"entry_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"},
                    {"entry_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"},
                    {"entry_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"},
                ],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dataset_id` but received ''"):
            await async_client.zero_trust.dlp.datasets.versions.with_raw_response.create(
                version=0,
                account_id="account_id",
                dataset_id="",
                body=[
                    {"entry_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"},
                    {"entry_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"},
                    {"entry_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"},
                ],
            )
