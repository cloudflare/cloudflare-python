# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.logpush.validates.destinations import (
    ExistDeleteAccountsAccountIdentifierLogpushValidateDestinationExistsResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestExists:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_delete_accounts_account_identifier_logpush_validate_destination_exists(
        self, client: Cloudflare
    ) -> None:
        exist = client.logpush.validates.destinations.exists.delete_accounts_account_identifier_logpush_validate_destination_exists(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_or_zone="string",
            destination_conf="s3://mybucket/logs?region=us-west-2",
        )
        assert_matches_type(
            Optional[ExistDeleteAccountsAccountIdentifierLogpushValidateDestinationExistsResponse],
            exist,
            path=["response"],
        )

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete_accounts_account_identifier_logpush_validate_destination_exists(
        self, client: Cloudflare
    ) -> None:
        response = client.logpush.validates.destinations.exists.with_raw_response.delete_accounts_account_identifier_logpush_validate_destination_exists(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_or_zone="string",
            destination_conf="s3://mybucket/logs?region=us-west-2",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        exist = response.parse()
        assert_matches_type(
            Optional[ExistDeleteAccountsAccountIdentifierLogpushValidateDestinationExistsResponse],
            exist,
            path=["response"],
        )

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete_accounts_account_identifier_logpush_validate_destination_exists(
        self, client: Cloudflare
    ) -> None:
        with client.logpush.validates.destinations.exists.with_streaming_response.delete_accounts_account_identifier_logpush_validate_destination_exists(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_or_zone="string",
            destination_conf="s3://mybucket/logs?region=us-west-2",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            exist = response.parse()
            assert_matches_type(
                Optional[ExistDeleteAccountsAccountIdentifierLogpushValidateDestinationExistsResponse],
                exist,
                path=["response"],
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_delete_accounts_account_identifier_logpush_validate_destination_exists(
        self, client: Cloudflare
    ) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone` but received ''"):
            client.logpush.validates.destinations.exists.with_raw_response.delete_accounts_account_identifier_logpush_validate_destination_exists(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_or_zone="",
                destination_conf="s3://mybucket/logs?region=us-west-2",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone_id` but received ''"):
            client.logpush.validates.destinations.exists.with_raw_response.delete_accounts_account_identifier_logpush_validate_destination_exists(
                "",
                account_or_zone="string",
                destination_conf="s3://mybucket/logs?region=us-west-2",
            )


class TestAsyncExists:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete_accounts_account_identifier_logpush_validate_destination_exists(
        self, async_client: AsyncCloudflare
    ) -> None:
        exist = await async_client.logpush.validates.destinations.exists.delete_accounts_account_identifier_logpush_validate_destination_exists(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_or_zone="string",
            destination_conf="s3://mybucket/logs?region=us-west-2",
        )
        assert_matches_type(
            Optional[ExistDeleteAccountsAccountIdentifierLogpushValidateDestinationExistsResponse],
            exist,
            path=["response"],
        )

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete_accounts_account_identifier_logpush_validate_destination_exists(
        self, async_client: AsyncCloudflare
    ) -> None:
        response = await async_client.logpush.validates.destinations.exists.with_raw_response.delete_accounts_account_identifier_logpush_validate_destination_exists(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_or_zone="string",
            destination_conf="s3://mybucket/logs?region=us-west-2",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        exist = await response.parse()
        assert_matches_type(
            Optional[ExistDeleteAccountsAccountIdentifierLogpushValidateDestinationExistsResponse],
            exist,
            path=["response"],
        )

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete_accounts_account_identifier_logpush_validate_destination_exists(
        self, async_client: AsyncCloudflare
    ) -> None:
        async with async_client.logpush.validates.destinations.exists.with_streaming_response.delete_accounts_account_identifier_logpush_validate_destination_exists(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_or_zone="string",
            destination_conf="s3://mybucket/logs?region=us-west-2",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            exist = await response.parse()
            assert_matches_type(
                Optional[ExistDeleteAccountsAccountIdentifierLogpushValidateDestinationExistsResponse],
                exist,
                path=["response"],
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_delete_accounts_account_identifier_logpush_validate_destination_exists(
        self, async_client: AsyncCloudflare
    ) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone` but received ''"):
            await async_client.logpush.validates.destinations.exists.with_raw_response.delete_accounts_account_identifier_logpush_validate_destination_exists(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_or_zone="",
                destination_conf="s3://mybucket/logs?region=us-west-2",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone_id` but received ''"):
            await async_client.logpush.validates.destinations.exists.with_raw_response.delete_accounts_account_identifier_logpush_validate_destination_exists(
                "",
                account_or_zone="string",
                destination_conf="s3://mybucket/logs?region=us-west-2",
            )
