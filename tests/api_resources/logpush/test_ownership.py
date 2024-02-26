# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.logpush import (
    OwnershipCreateResponse,
    OwnershipValidateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestOwnership:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        ownership = client.logpush.ownership.create(
            account_id="string",
            zone_id="string",
            destination_conf="s3://mybucket/logs?region=us-west-2",
        )
        assert_matches_type(Optional[OwnershipCreateResponse], ownership, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.logpush.ownership.with_raw_response.create(
            account_id="string",
            zone_id="string",
            destination_conf="s3://mybucket/logs?region=us-west-2",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ownership = response.parse()
        assert_matches_type(Optional[OwnershipCreateResponse], ownership, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.logpush.ownership.with_streaming_response.create(
            account_id="string",
            zone_id="string",
            destination_conf="s3://mybucket/logs?region=us-west-2",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ownership = response.parse()
            assert_matches_type(Optional[OwnershipCreateResponse], ownership, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.logpush.ownership.with_raw_response.create(
                account_id="",
                zone_id="string",
                destination_conf="s3://mybucket/logs?region=us-west-2",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.logpush.ownership.with_raw_response.create(
                account_id="string",
                zone_id="",
                destination_conf="s3://mybucket/logs?region=us-west-2",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_validate(self, client: Cloudflare) -> None:
        ownership = client.logpush.ownership.validate(
            account_id="string",
            zone_id="string",
            destination_conf="s3://mybucket/logs?region=us-west-2",
            ownership_challenge="00000000000000000000",
        )
        assert_matches_type(Optional[OwnershipValidateResponse], ownership, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_validate(self, client: Cloudflare) -> None:
        response = client.logpush.ownership.with_raw_response.validate(
            account_id="string",
            zone_id="string",
            destination_conf="s3://mybucket/logs?region=us-west-2",
            ownership_challenge="00000000000000000000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ownership = response.parse()
        assert_matches_type(Optional[OwnershipValidateResponse], ownership, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_validate(self, client: Cloudflare) -> None:
        with client.logpush.ownership.with_streaming_response.validate(
            account_id="string",
            zone_id="string",
            destination_conf="s3://mybucket/logs?region=us-west-2",
            ownership_challenge="00000000000000000000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ownership = response.parse()
            assert_matches_type(Optional[OwnershipValidateResponse], ownership, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_validate(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.logpush.ownership.with_raw_response.validate(
                account_id="",
                zone_id="string",
                destination_conf="s3://mybucket/logs?region=us-west-2",
                ownership_challenge="00000000000000000000",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.logpush.ownership.with_raw_response.validate(
                account_id="string",
                zone_id="",
                destination_conf="s3://mybucket/logs?region=us-west-2",
                ownership_challenge="00000000000000000000",
            )


class TestAsyncOwnership:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        ownership = await async_client.logpush.ownership.create(
            account_id="string",
            zone_id="string",
            destination_conf="s3://mybucket/logs?region=us-west-2",
        )
        assert_matches_type(Optional[OwnershipCreateResponse], ownership, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.logpush.ownership.with_raw_response.create(
            account_id="string",
            zone_id="string",
            destination_conf="s3://mybucket/logs?region=us-west-2",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ownership = await response.parse()
        assert_matches_type(Optional[OwnershipCreateResponse], ownership, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.logpush.ownership.with_streaming_response.create(
            account_id="string",
            zone_id="string",
            destination_conf="s3://mybucket/logs?region=us-west-2",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ownership = await response.parse()
            assert_matches_type(Optional[OwnershipCreateResponse], ownership, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.logpush.ownership.with_raw_response.create(
                account_id="",
                zone_id="string",
                destination_conf="s3://mybucket/logs?region=us-west-2",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.logpush.ownership.with_raw_response.create(
                account_id="string",
                zone_id="",
                destination_conf="s3://mybucket/logs?region=us-west-2",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_validate(self, async_client: AsyncCloudflare) -> None:
        ownership = await async_client.logpush.ownership.validate(
            account_id="string",
            zone_id="string",
            destination_conf="s3://mybucket/logs?region=us-west-2",
            ownership_challenge="00000000000000000000",
        )
        assert_matches_type(Optional[OwnershipValidateResponse], ownership, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_validate(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.logpush.ownership.with_raw_response.validate(
            account_id="string",
            zone_id="string",
            destination_conf="s3://mybucket/logs?region=us-west-2",
            ownership_challenge="00000000000000000000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ownership = await response.parse()
        assert_matches_type(Optional[OwnershipValidateResponse], ownership, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_validate(self, async_client: AsyncCloudflare) -> None:
        async with async_client.logpush.ownership.with_streaming_response.validate(
            account_id="string",
            zone_id="string",
            destination_conf="s3://mybucket/logs?region=us-west-2",
            ownership_challenge="00000000000000000000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ownership = await response.parse()
            assert_matches_type(Optional[OwnershipValidateResponse], ownership, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_validate(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.logpush.ownership.with_raw_response.validate(
                account_id="",
                zone_id="string",
                destination_conf="s3://mybucket/logs?region=us-west-2",
                ownership_challenge="00000000000000000000",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.logpush.ownership.with_raw_response.validate(
                account_id="string",
                zone_id="",
                destination_conf="s3://mybucket/logs?region=us-west-2",
                ownership_challenge="00000000000000000000",
            )
