# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Optional, Any, cast

from cloudflare.types.logpush.ownerships import ValidatePostAccountsAccountIdentifierLogpushOwnershipValidateResponse

import os
import pytest
import httpx
from typing_extensions import get_args
from typing import Optional
from respx import MockRouter
from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.logpush.ownerships import (
    validate_post_accounts_account_identifier_logpush_ownership_validate_params,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestValidates:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_post_accounts_account_identifier_logpush_ownership_validate(self, client: Cloudflare) -> None:
        validate = client.logpush.ownerships.validates.post_accounts_account_identifier_logpush_ownership_validate(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_or_zone="string",
            destination_conf="s3://mybucket/logs?region=us-west-2",
            ownership_challenge="00000000000000000000",
        )
        assert_matches_type(
            Optional[ValidatePostAccountsAccountIdentifierLogpushOwnershipValidateResponse], validate, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_post_accounts_account_identifier_logpush_ownership_validate(self, client: Cloudflare) -> None:
        response = client.logpush.ownerships.validates.with_raw_response.post_accounts_account_identifier_logpush_ownership_validate(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_or_zone="string",
            destination_conf="s3://mybucket/logs?region=us-west-2",
            ownership_challenge="00000000000000000000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        validate = response.parse()
        assert_matches_type(
            Optional[ValidatePostAccountsAccountIdentifierLogpushOwnershipValidateResponse], validate, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_post_accounts_account_identifier_logpush_ownership_validate(
        self, client: Cloudflare
    ) -> None:
        with client.logpush.ownerships.validates.with_streaming_response.post_accounts_account_identifier_logpush_ownership_validate(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_or_zone="string",
            destination_conf="s3://mybucket/logs?region=us-west-2",
            ownership_challenge="00000000000000000000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            validate = response.parse()
            assert_matches_type(
                Optional[ValidatePostAccountsAccountIdentifierLogpushOwnershipValidateResponse],
                validate,
                path=["response"],
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_post_accounts_account_identifier_logpush_ownership_validate(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone` but received ''"):
            client.logpush.ownerships.validates.with_raw_response.post_accounts_account_identifier_logpush_ownership_validate(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_or_zone="",
                destination_conf="s3://mybucket/logs?region=us-west-2",
                ownership_challenge="00000000000000000000",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone_id` but received ''"):
            client.logpush.ownerships.validates.with_raw_response.post_accounts_account_identifier_logpush_ownership_validate(
                "",
                account_or_zone="string",
                destination_conf="s3://mybucket/logs?region=us-west-2",
                ownership_challenge="00000000000000000000",
            )


class TestAsyncValidates:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_post_accounts_account_identifier_logpush_ownership_validate(
        self, async_client: AsyncCloudflare
    ) -> None:
        validate = (
            await async_client.logpush.ownerships.validates.post_accounts_account_identifier_logpush_ownership_validate(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_or_zone="string",
                destination_conf="s3://mybucket/logs?region=us-west-2",
                ownership_challenge="00000000000000000000",
            )
        )
        assert_matches_type(
            Optional[ValidatePostAccountsAccountIdentifierLogpushOwnershipValidateResponse], validate, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_post_accounts_account_identifier_logpush_ownership_validate(
        self, async_client: AsyncCloudflare
    ) -> None:
        response = await async_client.logpush.ownerships.validates.with_raw_response.post_accounts_account_identifier_logpush_ownership_validate(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_or_zone="string",
            destination_conf="s3://mybucket/logs?region=us-west-2",
            ownership_challenge="00000000000000000000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        validate = await response.parse()
        assert_matches_type(
            Optional[ValidatePostAccountsAccountIdentifierLogpushOwnershipValidateResponse], validate, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_post_accounts_account_identifier_logpush_ownership_validate(
        self, async_client: AsyncCloudflare
    ) -> None:
        async with async_client.logpush.ownerships.validates.with_streaming_response.post_accounts_account_identifier_logpush_ownership_validate(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_or_zone="string",
            destination_conf="s3://mybucket/logs?region=us-west-2",
            ownership_challenge="00000000000000000000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            validate = await response.parse()
            assert_matches_type(
                Optional[ValidatePostAccountsAccountIdentifierLogpushOwnershipValidateResponse],
                validate,
                path=["response"],
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_post_accounts_account_identifier_logpush_ownership_validate(
        self, async_client: AsyncCloudflare
    ) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone` but received ''"):
            await async_client.logpush.ownerships.validates.with_raw_response.post_accounts_account_identifier_logpush_ownership_validate(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_or_zone="",
                destination_conf="s3://mybucket/logs?region=us-west-2",
                ownership_challenge="00000000000000000000",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone_id` but received ''"):
            await async_client.logpush.ownerships.validates.with_raw_response.post_accounts_account_identifier_logpush_ownership_validate(
                "",
                account_or_zone="string",
                destination_conf="s3://mybucket/logs?region=us-west-2",
                ownership_challenge="00000000000000000000",
            )
