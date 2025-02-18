# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.logpush import (
    OwnershipValidation,
    OwnershipCreateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestOwnership:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        ownership = client.logpush.ownership.create(
            destination_conf="s3://mybucket/logs?region=us-west-2",
            account_id="account_id",
        )
        assert_matches_type(Optional[OwnershipCreateResponse], ownership, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_create_with_all_params(self, client: Cloudflare) -> None:
        ownership = client.logpush.ownership.create(
            destination_conf="s3://mybucket/logs?region=us-west-2",
            account_id="account_id",
        )
        assert_matches_type(Optional[OwnershipCreateResponse], ownership, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.logpush.ownership.with_raw_response.create(
            destination_conf="s3://mybucket/logs?region=us-west-2",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ownership = response.parse()
        assert_matches_type(Optional[OwnershipCreateResponse], ownership, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.logpush.ownership.with_streaming_response.create(
            destination_conf="s3://mybucket/logs?region=us-west-2",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ownership = response.parse()
            assert_matches_type(Optional[OwnershipCreateResponse], ownership, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.logpush.ownership.with_raw_response.create(
                destination_conf="s3://mybucket/logs?region=us-west-2",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.logpush.ownership.with_raw_response.create(
                destination_conf="s3://mybucket/logs?region=us-west-2",
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_validate(self, client: Cloudflare) -> None:
        ownership = client.logpush.ownership.validate(
            destination_conf="s3://mybucket/logs?region=us-west-2",
            ownership_challenge="00000000000000000000",
            account_id="account_id",
        )
        assert_matches_type(Optional[OwnershipValidation], ownership, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_validate_with_all_params(self, client: Cloudflare) -> None:
        ownership = client.logpush.ownership.validate(
            destination_conf="s3://mybucket/logs?region=us-west-2",
            ownership_challenge="00000000000000000000",
            account_id="account_id",
        )
        assert_matches_type(Optional[OwnershipValidation], ownership, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_validate(self, client: Cloudflare) -> None:
        response = client.logpush.ownership.with_raw_response.validate(
            destination_conf="s3://mybucket/logs?region=us-west-2",
            ownership_challenge="00000000000000000000",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ownership = response.parse()
        assert_matches_type(Optional[OwnershipValidation], ownership, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_validate(self, client: Cloudflare) -> None:
        with client.logpush.ownership.with_streaming_response.validate(
            destination_conf="s3://mybucket/logs?region=us-west-2",
            ownership_challenge="00000000000000000000",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ownership = response.parse()
            assert_matches_type(Optional[OwnershipValidation], ownership, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_validate(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.logpush.ownership.with_raw_response.validate(
                destination_conf="s3://mybucket/logs?region=us-west-2",
                ownership_challenge="00000000000000000000",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.logpush.ownership.with_raw_response.validate(
                destination_conf="s3://mybucket/logs?region=us-west-2",
                ownership_challenge="00000000000000000000",
                account_id="account_id",
            )


class TestAsyncOwnership:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        ownership = await async_client.logpush.ownership.create(
            destination_conf="s3://mybucket/logs?region=us-west-2",
            account_id="account_id",
        )
        assert_matches_type(Optional[OwnershipCreateResponse], ownership, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCloudflare) -> None:
        ownership = await async_client.logpush.ownership.create(
            destination_conf="s3://mybucket/logs?region=us-west-2",
            account_id="account_id",
        )
        assert_matches_type(Optional[OwnershipCreateResponse], ownership, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.logpush.ownership.with_raw_response.create(
            destination_conf="s3://mybucket/logs?region=us-west-2",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ownership = await response.parse()
        assert_matches_type(Optional[OwnershipCreateResponse], ownership, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.logpush.ownership.with_streaming_response.create(
            destination_conf="s3://mybucket/logs?region=us-west-2",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ownership = await response.parse()
            assert_matches_type(Optional[OwnershipCreateResponse], ownership, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.logpush.ownership.with_raw_response.create(
                destination_conf="s3://mybucket/logs?region=us-west-2",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.logpush.ownership.with_raw_response.create(
                destination_conf="s3://mybucket/logs?region=us-west-2",
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_validate(self, async_client: AsyncCloudflare) -> None:
        ownership = await async_client.logpush.ownership.validate(
            destination_conf="s3://mybucket/logs?region=us-west-2",
            ownership_challenge="00000000000000000000",
            account_id="account_id",
        )
        assert_matches_type(Optional[OwnershipValidation], ownership, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_validate_with_all_params(self, async_client: AsyncCloudflare) -> None:
        ownership = await async_client.logpush.ownership.validate(
            destination_conf="s3://mybucket/logs?region=us-west-2",
            ownership_challenge="00000000000000000000",
            account_id="account_id",
        )
        assert_matches_type(Optional[OwnershipValidation], ownership, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_validate(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.logpush.ownership.with_raw_response.validate(
            destination_conf="s3://mybucket/logs?region=us-west-2",
            ownership_challenge="00000000000000000000",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ownership = await response.parse()
        assert_matches_type(Optional[OwnershipValidation], ownership, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_validate(self, async_client: AsyncCloudflare) -> None:
        async with async_client.logpush.ownership.with_streaming_response.validate(
            destination_conf="s3://mybucket/logs?region=us-west-2",
            ownership_challenge="00000000000000000000",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ownership = await response.parse()
            assert_matches_type(Optional[OwnershipValidation], ownership, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_validate(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.logpush.ownership.with_raw_response.validate(
                destination_conf="s3://mybucket/logs?region=us-west-2",
                ownership_challenge="00000000000000000000",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.logpush.ownership.with_raw_response.validate(
                destination_conf="s3://mybucket/logs?region=us-west-2",
                ownership_challenge="00000000000000000000",
                account_id="account_id",
            )
