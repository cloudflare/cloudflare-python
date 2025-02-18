# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.pagination import SyncSinglePage, AsyncSinglePage
from cloudflare.types.magic_transit.pcaps import Ownership

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestOwnership:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        ownership = client.magic_transit.pcaps.ownership.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            destination_conf="s3://pcaps-bucket?region=us-east-1",
        )
        assert_matches_type(Ownership, ownership, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.magic_transit.pcaps.ownership.with_raw_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            destination_conf="s3://pcaps-bucket?region=us-east-1",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ownership = response.parse()
        assert_matches_type(Ownership, ownership, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.magic_transit.pcaps.ownership.with_streaming_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            destination_conf="s3://pcaps-bucket?region=us-east-1",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ownership = response.parse()
            assert_matches_type(Ownership, ownership, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.magic_transit.pcaps.ownership.with_raw_response.create(
                account_id="",
                destination_conf="s3://pcaps-bucket?region=us-east-1",
            )

    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        ownership = client.magic_transit.pcaps.ownership.delete(
            ownership_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert ownership is None

    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.magic_transit.pcaps.ownership.with_raw_response.delete(
            ownership_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ownership = response.parse()
        assert ownership is None

    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.magic_transit.pcaps.ownership.with_streaming_response.delete(
            ownership_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ownership = response.parse()
            assert ownership is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.magic_transit.pcaps.ownership.with_raw_response.delete(
                ownership_id="023e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ownership_id` but received ''"):
            client.magic_transit.pcaps.ownership.with_raw_response.delete(
                ownership_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        ownership = client.magic_transit.pcaps.ownership.get(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(SyncSinglePage[Ownership], ownership, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.magic_transit.pcaps.ownership.with_raw_response.get(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ownership = response.parse()
        assert_matches_type(SyncSinglePage[Ownership], ownership, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.magic_transit.pcaps.ownership.with_streaming_response.get(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ownership = response.parse()
            assert_matches_type(SyncSinglePage[Ownership], ownership, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.magic_transit.pcaps.ownership.with_raw_response.get(
                account_id="",
            )

    @parametrize
    def test_method_validate(self, client: Cloudflare) -> None:
        ownership = client.magic_transit.pcaps.ownership.validate(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            destination_conf="s3://pcaps-bucket?region=us-east-1",
            ownership_challenge="ownership-challenge-9883874ecac311ec8475433579a6bf5f.txt",
        )
        assert_matches_type(Ownership, ownership, path=["response"])

    @parametrize
    def test_raw_response_validate(self, client: Cloudflare) -> None:
        response = client.magic_transit.pcaps.ownership.with_raw_response.validate(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            destination_conf="s3://pcaps-bucket?region=us-east-1",
            ownership_challenge="ownership-challenge-9883874ecac311ec8475433579a6bf5f.txt",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ownership = response.parse()
        assert_matches_type(Ownership, ownership, path=["response"])

    @parametrize
    def test_streaming_response_validate(self, client: Cloudflare) -> None:
        with client.magic_transit.pcaps.ownership.with_streaming_response.validate(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            destination_conf="s3://pcaps-bucket?region=us-east-1",
            ownership_challenge="ownership-challenge-9883874ecac311ec8475433579a6bf5f.txt",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ownership = response.parse()
            assert_matches_type(Ownership, ownership, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_validate(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.magic_transit.pcaps.ownership.with_raw_response.validate(
                account_id="",
                destination_conf="s3://pcaps-bucket?region=us-east-1",
                ownership_challenge="ownership-challenge-9883874ecac311ec8475433579a6bf5f.txt",
            )


class TestAsyncOwnership:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        ownership = await async_client.magic_transit.pcaps.ownership.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            destination_conf="s3://pcaps-bucket?region=us-east-1",
        )
        assert_matches_type(Ownership, ownership, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.magic_transit.pcaps.ownership.with_raw_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            destination_conf="s3://pcaps-bucket?region=us-east-1",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ownership = await response.parse()
        assert_matches_type(Ownership, ownership, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.magic_transit.pcaps.ownership.with_streaming_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            destination_conf="s3://pcaps-bucket?region=us-east-1",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ownership = await response.parse()
            assert_matches_type(Ownership, ownership, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.magic_transit.pcaps.ownership.with_raw_response.create(
                account_id="",
                destination_conf="s3://pcaps-bucket?region=us-east-1",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        ownership = await async_client.magic_transit.pcaps.ownership.delete(
            ownership_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert ownership is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.magic_transit.pcaps.ownership.with_raw_response.delete(
            ownership_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ownership = await response.parse()
        assert ownership is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.magic_transit.pcaps.ownership.with_streaming_response.delete(
            ownership_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ownership = await response.parse()
            assert ownership is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.magic_transit.pcaps.ownership.with_raw_response.delete(
                ownership_id="023e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ownership_id` but received ''"):
            await async_client.magic_transit.pcaps.ownership.with_raw_response.delete(
                ownership_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        ownership = await async_client.magic_transit.pcaps.ownership.get(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(AsyncSinglePage[Ownership], ownership, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.magic_transit.pcaps.ownership.with_raw_response.get(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ownership = await response.parse()
        assert_matches_type(AsyncSinglePage[Ownership], ownership, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.magic_transit.pcaps.ownership.with_streaming_response.get(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ownership = await response.parse()
            assert_matches_type(AsyncSinglePage[Ownership], ownership, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.magic_transit.pcaps.ownership.with_raw_response.get(
                account_id="",
            )

    @parametrize
    async def test_method_validate(self, async_client: AsyncCloudflare) -> None:
        ownership = await async_client.magic_transit.pcaps.ownership.validate(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            destination_conf="s3://pcaps-bucket?region=us-east-1",
            ownership_challenge="ownership-challenge-9883874ecac311ec8475433579a6bf5f.txt",
        )
        assert_matches_type(Ownership, ownership, path=["response"])

    @parametrize
    async def test_raw_response_validate(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.magic_transit.pcaps.ownership.with_raw_response.validate(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            destination_conf="s3://pcaps-bucket?region=us-east-1",
            ownership_challenge="ownership-challenge-9883874ecac311ec8475433579a6bf5f.txt",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ownership = await response.parse()
        assert_matches_type(Ownership, ownership, path=["response"])

    @parametrize
    async def test_streaming_response_validate(self, async_client: AsyncCloudflare) -> None:
        async with async_client.magic_transit.pcaps.ownership.with_streaming_response.validate(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            destination_conf="s3://pcaps-bucket?region=us-east-1",
            ownership_challenge="ownership-challenge-9883874ecac311ec8475433579a6bf5f.txt",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ownership = await response.parse()
            assert_matches_type(Ownership, ownership, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_validate(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.magic_transit.pcaps.ownership.with_raw_response.validate(
                account_id="",
                destination_conf="s3://pcaps-bucket?region=us-east-1",
                ownership_challenge="ownership-challenge-9883874ecac311ec8475433579a6bf5f.txt",
            )
