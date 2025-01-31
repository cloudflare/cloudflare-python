# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.pagination import SyncSinglePage, AsyncSinglePage
from cloudflare.types.zero_trust.access import (
    ServiceToken,
    ServiceTokenCreateResponse,
    ServiceTokenRotateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestServiceTokens:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        service_token = client.zero_trust.access.service_tokens.create(
            name="CI/CD token",
            account_id="account_id",
        )
        assert_matches_type(Optional[ServiceTokenCreateResponse], service_token, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_create_with_all_params(self, client: Cloudflare) -> None:
        service_token = client.zero_trust.access.service_tokens.create(
            name="CI/CD token",
            account_id="account_id",
            duration="60m",
        )
        assert_matches_type(Optional[ServiceTokenCreateResponse], service_token, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.zero_trust.access.service_tokens.with_raw_response.create(
            name="CI/CD token",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        service_token = response.parse()
        assert_matches_type(Optional[ServiceTokenCreateResponse], service_token, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.zero_trust.access.service_tokens.with_streaming_response.create(
            name="CI/CD token",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            service_token = response.parse()
            assert_matches_type(Optional[ServiceTokenCreateResponse], service_token, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.zero_trust.access.service_tokens.with_raw_response.create(
                name="CI/CD token",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.zero_trust.access.service_tokens.with_raw_response.create(
                name="CI/CD token",
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        service_token = client.zero_trust.access.service_tokens.update(
            service_token_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="account_id",
        )
        assert_matches_type(Optional[ServiceToken], service_token, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_update_with_all_params(self, client: Cloudflare) -> None:
        service_token = client.zero_trust.access.service_tokens.update(
            service_token_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="account_id",
            duration="60m",
            name="CI/CD token",
        )
        assert_matches_type(Optional[ServiceToken], service_token, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.zero_trust.access.service_tokens.with_raw_response.update(
            service_token_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        service_token = response.parse()
        assert_matches_type(Optional[ServiceToken], service_token, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.zero_trust.access.service_tokens.with_streaming_response.update(
            service_token_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            service_token = response.parse()
            assert_matches_type(Optional[ServiceToken], service_token, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `service_token_id` but received ''"):
            client.zero_trust.access.service_tokens.with_raw_response.update(
                service_token_id="",
                account_id="account_id",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.zero_trust.access.service_tokens.with_raw_response.update(
                service_token_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.zero_trust.access.service_tokens.with_raw_response.update(
                service_token_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        service_token = client.zero_trust.access.service_tokens.list(
            account_id="account_id",
        )
        assert_matches_type(SyncSinglePage[ServiceToken], service_token, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_list_with_all_params(self, client: Cloudflare) -> None:
        service_token = client.zero_trust.access.service_tokens.list(
            account_id="account_id",
            name="name",
            search="search",
        )
        assert_matches_type(SyncSinglePage[ServiceToken], service_token, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.zero_trust.access.service_tokens.with_raw_response.list(
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        service_token = response.parse()
        assert_matches_type(SyncSinglePage[ServiceToken], service_token, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.zero_trust.access.service_tokens.with_streaming_response.list(
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            service_token = response.parse()
            assert_matches_type(SyncSinglePage[ServiceToken], service_token, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.zero_trust.access.service_tokens.with_raw_response.list(
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.zero_trust.access.service_tokens.with_raw_response.list(
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        service_token = client.zero_trust.access.service_tokens.delete(
            service_token_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="account_id",
        )
        assert_matches_type(Optional[ServiceToken], service_token, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_delete_with_all_params(self, client: Cloudflare) -> None:
        service_token = client.zero_trust.access.service_tokens.delete(
            service_token_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="account_id",
        )
        assert_matches_type(Optional[ServiceToken], service_token, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.zero_trust.access.service_tokens.with_raw_response.delete(
            service_token_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        service_token = response.parse()
        assert_matches_type(Optional[ServiceToken], service_token, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.zero_trust.access.service_tokens.with_streaming_response.delete(
            service_token_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            service_token = response.parse()
            assert_matches_type(Optional[ServiceToken], service_token, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `service_token_id` but received ''"):
            client.zero_trust.access.service_tokens.with_raw_response.delete(
                service_token_id="",
                account_id="account_id",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.zero_trust.access.service_tokens.with_raw_response.delete(
                service_token_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.zero_trust.access.service_tokens.with_raw_response.delete(
                service_token_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        service_token = client.zero_trust.access.service_tokens.get(
            service_token_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="account_id",
        )
        assert_matches_type(Optional[ServiceToken], service_token, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_get_with_all_params(self, client: Cloudflare) -> None:
        service_token = client.zero_trust.access.service_tokens.get(
            service_token_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="account_id",
        )
        assert_matches_type(Optional[ServiceToken], service_token, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.zero_trust.access.service_tokens.with_raw_response.get(
            service_token_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        service_token = response.parse()
        assert_matches_type(Optional[ServiceToken], service_token, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.zero_trust.access.service_tokens.with_streaming_response.get(
            service_token_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            service_token = response.parse()
            assert_matches_type(Optional[ServiceToken], service_token, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `service_token_id` but received ''"):
            client.zero_trust.access.service_tokens.with_raw_response.get(
                service_token_id="",
                account_id="account_id",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.zero_trust.access.service_tokens.with_raw_response.get(
                service_token_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.zero_trust.access.service_tokens.with_raw_response.get(
                service_token_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_id="account_id",
            )

    @parametrize
    def test_method_refresh(self, client: Cloudflare) -> None:
        service_token = client.zero_trust.access.service_tokens.refresh(
            service_token_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[ServiceToken], service_token, path=["response"])

    @parametrize
    def test_raw_response_refresh(self, client: Cloudflare) -> None:
        response = client.zero_trust.access.service_tokens.with_raw_response.refresh(
            service_token_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        service_token = response.parse()
        assert_matches_type(Optional[ServiceToken], service_token, path=["response"])

    @parametrize
    def test_streaming_response_refresh(self, client: Cloudflare) -> None:
        with client.zero_trust.access.service_tokens.with_streaming_response.refresh(
            service_token_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            service_token = response.parse()
            assert_matches_type(Optional[ServiceToken], service_token, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_refresh(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.access.service_tokens.with_raw_response.refresh(
                service_token_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `service_token_id` but received ''"):
            client.zero_trust.access.service_tokens.with_raw_response.refresh(
                service_token_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    def test_method_rotate(self, client: Cloudflare) -> None:
        service_token = client.zero_trust.access.service_tokens.rotate(
            service_token_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[ServiceTokenRotateResponse], service_token, path=["response"])

    @parametrize
    def test_raw_response_rotate(self, client: Cloudflare) -> None:
        response = client.zero_trust.access.service_tokens.with_raw_response.rotate(
            service_token_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        service_token = response.parse()
        assert_matches_type(Optional[ServiceTokenRotateResponse], service_token, path=["response"])

    @parametrize
    def test_streaming_response_rotate(self, client: Cloudflare) -> None:
        with client.zero_trust.access.service_tokens.with_streaming_response.rotate(
            service_token_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            service_token = response.parse()
            assert_matches_type(Optional[ServiceTokenRotateResponse], service_token, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_rotate(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.access.service_tokens.with_raw_response.rotate(
                service_token_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `service_token_id` but received ''"):
            client.zero_trust.access.service_tokens.with_raw_response.rotate(
                service_token_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )


class TestAsyncServiceTokens:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        service_token = await async_client.zero_trust.access.service_tokens.create(
            name="CI/CD token",
            account_id="account_id",
        )
        assert_matches_type(Optional[ServiceTokenCreateResponse], service_token, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCloudflare) -> None:
        service_token = await async_client.zero_trust.access.service_tokens.create(
            name="CI/CD token",
            account_id="account_id",
            duration="60m",
        )
        assert_matches_type(Optional[ServiceTokenCreateResponse], service_token, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.access.service_tokens.with_raw_response.create(
            name="CI/CD token",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        service_token = await response.parse()
        assert_matches_type(Optional[ServiceTokenCreateResponse], service_token, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.access.service_tokens.with_streaming_response.create(
            name="CI/CD token",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            service_token = await response.parse()
            assert_matches_type(Optional[ServiceTokenCreateResponse], service_token, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.zero_trust.access.service_tokens.with_raw_response.create(
                name="CI/CD token",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.zero_trust.access.service_tokens.with_raw_response.create(
                name="CI/CD token",
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        service_token = await async_client.zero_trust.access.service_tokens.update(
            service_token_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="account_id",
        )
        assert_matches_type(Optional[ServiceToken], service_token, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncCloudflare) -> None:
        service_token = await async_client.zero_trust.access.service_tokens.update(
            service_token_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="account_id",
            duration="60m",
            name="CI/CD token",
        )
        assert_matches_type(Optional[ServiceToken], service_token, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.access.service_tokens.with_raw_response.update(
            service_token_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        service_token = await response.parse()
        assert_matches_type(Optional[ServiceToken], service_token, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.access.service_tokens.with_streaming_response.update(
            service_token_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            service_token = await response.parse()
            assert_matches_type(Optional[ServiceToken], service_token, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `service_token_id` but received ''"):
            await async_client.zero_trust.access.service_tokens.with_raw_response.update(
                service_token_id="",
                account_id="account_id",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.zero_trust.access.service_tokens.with_raw_response.update(
                service_token_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.zero_trust.access.service_tokens.with_raw_response.update(
                service_token_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        service_token = await async_client.zero_trust.access.service_tokens.list(
            account_id="account_id",
        )
        assert_matches_type(AsyncSinglePage[ServiceToken], service_token, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCloudflare) -> None:
        service_token = await async_client.zero_trust.access.service_tokens.list(
            account_id="account_id",
            name="name",
            search="search",
        )
        assert_matches_type(AsyncSinglePage[ServiceToken], service_token, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.access.service_tokens.with_raw_response.list(
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        service_token = await response.parse()
        assert_matches_type(AsyncSinglePage[ServiceToken], service_token, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.access.service_tokens.with_streaming_response.list(
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            service_token = await response.parse()
            assert_matches_type(AsyncSinglePage[ServiceToken], service_token, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.zero_trust.access.service_tokens.with_raw_response.list(
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.zero_trust.access.service_tokens.with_raw_response.list(
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        service_token = await async_client.zero_trust.access.service_tokens.delete(
            service_token_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="account_id",
        )
        assert_matches_type(Optional[ServiceToken], service_token, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncCloudflare) -> None:
        service_token = await async_client.zero_trust.access.service_tokens.delete(
            service_token_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="account_id",
        )
        assert_matches_type(Optional[ServiceToken], service_token, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.access.service_tokens.with_raw_response.delete(
            service_token_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        service_token = await response.parse()
        assert_matches_type(Optional[ServiceToken], service_token, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.access.service_tokens.with_streaming_response.delete(
            service_token_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            service_token = await response.parse()
            assert_matches_type(Optional[ServiceToken], service_token, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `service_token_id` but received ''"):
            await async_client.zero_trust.access.service_tokens.with_raw_response.delete(
                service_token_id="",
                account_id="account_id",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.zero_trust.access.service_tokens.with_raw_response.delete(
                service_token_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.zero_trust.access.service_tokens.with_raw_response.delete(
                service_token_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        service_token = await async_client.zero_trust.access.service_tokens.get(
            service_token_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="account_id",
        )
        assert_matches_type(Optional[ServiceToken], service_token, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncCloudflare) -> None:
        service_token = await async_client.zero_trust.access.service_tokens.get(
            service_token_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="account_id",
        )
        assert_matches_type(Optional[ServiceToken], service_token, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.access.service_tokens.with_raw_response.get(
            service_token_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        service_token = await response.parse()
        assert_matches_type(Optional[ServiceToken], service_token, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.access.service_tokens.with_streaming_response.get(
            service_token_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            service_token = await response.parse()
            assert_matches_type(Optional[ServiceToken], service_token, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `service_token_id` but received ''"):
            await async_client.zero_trust.access.service_tokens.with_raw_response.get(
                service_token_id="",
                account_id="account_id",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.zero_trust.access.service_tokens.with_raw_response.get(
                service_token_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.zero_trust.access.service_tokens.with_raw_response.get(
                service_token_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_id="account_id",
            )

    @parametrize
    async def test_method_refresh(self, async_client: AsyncCloudflare) -> None:
        service_token = await async_client.zero_trust.access.service_tokens.refresh(
            service_token_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[ServiceToken], service_token, path=["response"])

    @parametrize
    async def test_raw_response_refresh(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.access.service_tokens.with_raw_response.refresh(
            service_token_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        service_token = await response.parse()
        assert_matches_type(Optional[ServiceToken], service_token, path=["response"])

    @parametrize
    async def test_streaming_response_refresh(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.access.service_tokens.with_streaming_response.refresh(
            service_token_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            service_token = await response.parse()
            assert_matches_type(Optional[ServiceToken], service_token, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_refresh(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.access.service_tokens.with_raw_response.refresh(
                service_token_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `service_token_id` but received ''"):
            await async_client.zero_trust.access.service_tokens.with_raw_response.refresh(
                service_token_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    async def test_method_rotate(self, async_client: AsyncCloudflare) -> None:
        service_token = await async_client.zero_trust.access.service_tokens.rotate(
            service_token_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[ServiceTokenRotateResponse], service_token, path=["response"])

    @parametrize
    async def test_raw_response_rotate(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.access.service_tokens.with_raw_response.rotate(
            service_token_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        service_token = await response.parse()
        assert_matches_type(Optional[ServiceTokenRotateResponse], service_token, path=["response"])

    @parametrize
    async def test_streaming_response_rotate(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.access.service_tokens.with_streaming_response.rotate(
            service_token_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            service_token = await response.parse()
            assert_matches_type(Optional[ServiceTokenRotateResponse], service_token, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_rotate(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.access.service_tokens.with_raw_response.rotate(
                service_token_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `service_token_id` but received ''"):
            await async_client.zero_trust.access.service_tokens.with_raw_response.rotate(
                service_token_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )
