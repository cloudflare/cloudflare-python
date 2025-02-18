# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.zero_trust.dlp.datasets.versions import EntryCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEntries:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        entry = client.zero_trust.dlp.datasets.versions.entries.create(
            entry_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            version=0,
            body=b"raw file contents",
        )
        assert_matches_type(Optional[EntryCreateResponse], entry, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.zero_trust.dlp.datasets.versions.entries.with_raw_response.create(
            entry_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            version=0,
            body=b"raw file contents",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entry = response.parse()
        assert_matches_type(Optional[EntryCreateResponse], entry, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.zero_trust.dlp.datasets.versions.entries.with_streaming_response.create(
            entry_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            version=0,
            body=b"raw file contents",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entry = response.parse()
            assert_matches_type(Optional[EntryCreateResponse], entry, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.dlp.datasets.versions.entries.with_raw_response.create(
                entry_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
                dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                version=0,
                body=b"raw file contents",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dataset_id` but received ''"):
            client.zero_trust.dlp.datasets.versions.entries.with_raw_response.create(
                entry_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="account_id",
                dataset_id="",
                version=0,
                body=b"raw file contents",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `entry_id` but received ''"):
            client.zero_trust.dlp.datasets.versions.entries.with_raw_response.create(
                entry_id="",
                account_id="account_id",
                dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                version=0,
                body=b"raw file contents",
            )


class TestAsyncEntries:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        entry = await async_client.zero_trust.dlp.datasets.versions.entries.create(
            entry_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            version=0,
            body=b"raw file contents",
        )
        assert_matches_type(Optional[EntryCreateResponse], entry, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.dlp.datasets.versions.entries.with_raw_response.create(
            entry_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            version=0,
            body=b"raw file contents",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entry = await response.parse()
        assert_matches_type(Optional[EntryCreateResponse], entry, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.dlp.datasets.versions.entries.with_streaming_response.create(
            entry_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            version=0,
            body=b"raw file contents",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entry = await response.parse()
            assert_matches_type(Optional[EntryCreateResponse], entry, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.dlp.datasets.versions.entries.with_raw_response.create(
                entry_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
                dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                version=0,
                body=b"raw file contents",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dataset_id` but received ''"):
            await async_client.zero_trust.dlp.datasets.versions.entries.with_raw_response.create(
                entry_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="account_id",
                dataset_id="",
                version=0,
                body=b"raw file contents",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `entry_id` but received ''"):
            await async_client.zero_trust.dlp.datasets.versions.entries.with_raw_response.create(
                entry_id="",
                account_id="account_id",
                dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                version=0,
                body=b"raw file contents",
            )
