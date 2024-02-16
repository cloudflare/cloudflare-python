# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.logpush.validates import (
    OriginPostAccountsAccountIdentifierLogpushValidateOriginResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestOrigins:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_post_accounts_account_identifier_logpush_validate_origin(self, client: Cloudflare) -> None:
        origin = client.logpush.validates.origins.post_accounts_account_identifier_logpush_validate_origin(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_or_zone="string",
            logpull_options="fields=RayID,ClientIP,EdgeStartTimestamp&timestamps=rfc3339",
        )
        assert_matches_type(
            Optional[OriginPostAccountsAccountIdentifierLogpushValidateOriginResponse], origin, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_post_accounts_account_identifier_logpush_validate_origin(self, client: Cloudflare) -> None:
        response = (
            client.logpush.validates.origins.with_raw_response.post_accounts_account_identifier_logpush_validate_origin(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_or_zone="string",
                logpull_options="fields=RayID,ClientIP,EdgeStartTimestamp&timestamps=rfc3339",
            )
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        origin = response.parse()
        assert_matches_type(
            Optional[OriginPostAccountsAccountIdentifierLogpushValidateOriginResponse], origin, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_post_accounts_account_identifier_logpush_validate_origin(
        self, client: Cloudflare
    ) -> None:
        with client.logpush.validates.origins.with_streaming_response.post_accounts_account_identifier_logpush_validate_origin(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_or_zone="string",
            logpull_options="fields=RayID,ClientIP,EdgeStartTimestamp&timestamps=rfc3339",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            origin = response.parse()
            assert_matches_type(
                Optional[OriginPostAccountsAccountIdentifierLogpushValidateOriginResponse], origin, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_post_accounts_account_identifier_logpush_validate_origin(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone` but received ''"):
            client.logpush.validates.origins.with_raw_response.post_accounts_account_identifier_logpush_validate_origin(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_or_zone="",
                logpull_options="fields=RayID,ClientIP,EdgeStartTimestamp&timestamps=rfc3339",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone_id` but received ''"):
            client.logpush.validates.origins.with_raw_response.post_accounts_account_identifier_logpush_validate_origin(
                "",
                account_or_zone="string",
                logpull_options="fields=RayID,ClientIP,EdgeStartTimestamp&timestamps=rfc3339",
            )


class TestAsyncOrigins:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_post_accounts_account_identifier_logpush_validate_origin(
        self, async_client: AsyncCloudflare
    ) -> None:
        origin = await async_client.logpush.validates.origins.post_accounts_account_identifier_logpush_validate_origin(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_or_zone="string",
            logpull_options="fields=RayID,ClientIP,EdgeStartTimestamp&timestamps=rfc3339",
        )
        assert_matches_type(
            Optional[OriginPostAccountsAccountIdentifierLogpushValidateOriginResponse], origin, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_post_accounts_account_identifier_logpush_validate_origin(
        self, async_client: AsyncCloudflare
    ) -> None:
        response = await async_client.logpush.validates.origins.with_raw_response.post_accounts_account_identifier_logpush_validate_origin(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_or_zone="string",
            logpull_options="fields=RayID,ClientIP,EdgeStartTimestamp&timestamps=rfc3339",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        origin = await response.parse()
        assert_matches_type(
            Optional[OriginPostAccountsAccountIdentifierLogpushValidateOriginResponse], origin, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_post_accounts_account_identifier_logpush_validate_origin(
        self, async_client: AsyncCloudflare
    ) -> None:
        async with async_client.logpush.validates.origins.with_streaming_response.post_accounts_account_identifier_logpush_validate_origin(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_or_zone="string",
            logpull_options="fields=RayID,ClientIP,EdgeStartTimestamp&timestamps=rfc3339",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            origin = await response.parse()
            assert_matches_type(
                Optional[OriginPostAccountsAccountIdentifierLogpushValidateOriginResponse], origin, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_post_accounts_account_identifier_logpush_validate_origin(
        self, async_client: AsyncCloudflare
    ) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone` but received ''"):
            await async_client.logpush.validates.origins.with_raw_response.post_accounts_account_identifier_logpush_validate_origin(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_or_zone="",
                logpull_options="fields=RayID,ClientIP,EdgeStartTimestamp&timestamps=rfc3339",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone_id` but received ''"):
            await async_client.logpush.validates.origins.with_raw_response.post_accounts_account_identifier_logpush_validate_origin(
                "",
                account_or_zone="string",
                logpull_options="fields=RayID,ClientIP,EdgeStartTimestamp&timestamps=rfc3339",
            )
