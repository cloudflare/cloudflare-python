# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.ai_gateway import (
    BillingUsageHistoryResponse,
    BillingCreditBalanceResponse,
    BillingInvoiceHistoryResponse,
    BillingInvoicePreviewResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBilling:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="HTTP 404 error from prism -- route not in spec")
    @parametrize
    def test_method_credit_balance(self, client: Cloudflare) -> None:
        billing = client.ai_gateway.billing.credit_balance(
            account_id="account_id",
        )
        assert_matches_type(BillingCreditBalanceResponse, billing, path=["response"])

    @pytest.mark.skip(reason="HTTP 404 error from prism -- route not in spec")
    @parametrize
    def test_raw_response_credit_balance(self, client: Cloudflare) -> None:
        response = client.ai_gateway.billing.with_raw_response.credit_balance(
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        billing = response.parse()
        assert_matches_type(BillingCreditBalanceResponse, billing, path=["response"])

    @pytest.mark.skip(reason="HTTP 404 error from prism -- route not in spec")
    @parametrize
    def test_streaming_response_credit_balance(self, client: Cloudflare) -> None:
        with client.ai_gateway.billing.with_streaming_response.credit_balance(
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            billing = response.parse()
            assert_matches_type(BillingCreditBalanceResponse, billing, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="HTTP 404 error from prism -- route not in spec")
    @parametrize
    def test_path_params_credit_balance(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.ai_gateway.billing.with_raw_response.credit_balance(
                account_id="",
            )

    @parametrize
    def test_method_invoice_history(self, client: Cloudflare) -> None:
        billing = client.ai_gateway.billing.invoice_history(
            account_id="account_id",
        )
        assert_matches_type(BillingInvoiceHistoryResponse, billing, path=["response"])

    @parametrize
    def test_method_invoice_history_with_all_params(self, client: Cloudflare) -> None:
        billing = client.ai_gateway.billing.invoice_history(
            account_id="account_id",
            type="all",
        )
        assert_matches_type(BillingInvoiceHistoryResponse, billing, path=["response"])

    @parametrize
    def test_raw_response_invoice_history(self, client: Cloudflare) -> None:
        response = client.ai_gateway.billing.with_raw_response.invoice_history(
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        billing = response.parse()
        assert_matches_type(BillingInvoiceHistoryResponse, billing, path=["response"])

    @parametrize
    def test_streaming_response_invoice_history(self, client: Cloudflare) -> None:
        with client.ai_gateway.billing.with_streaming_response.invoice_history(
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            billing = response.parse()
            assert_matches_type(BillingInvoiceHistoryResponse, billing, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_invoice_history(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.ai_gateway.billing.with_raw_response.invoice_history(
                account_id="",
            )

    @parametrize
    def test_method_invoice_preview(self, client: Cloudflare) -> None:
        billing = client.ai_gateway.billing.invoice_preview(
            account_id="account_id",
        )
        assert_matches_type(BillingInvoicePreviewResponse, billing, path=["response"])

    @parametrize
    def test_raw_response_invoice_preview(self, client: Cloudflare) -> None:
        response = client.ai_gateway.billing.with_raw_response.invoice_preview(
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        billing = response.parse()
        assert_matches_type(BillingInvoicePreviewResponse, billing, path=["response"])

    @parametrize
    def test_streaming_response_invoice_preview(self, client: Cloudflare) -> None:
        with client.ai_gateway.billing.with_streaming_response.invoice_preview(
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            billing = response.parse()
            assert_matches_type(BillingInvoicePreviewResponse, billing, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_invoice_preview(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.ai_gateway.billing.with_raw_response.invoice_preview(
                account_id="",
            )

    @parametrize
    def test_method_usage_history(self, client: Cloudflare) -> None:
        billing = client.ai_gateway.billing.usage_history(
            account_id="account_id",
            value_grouping_window="day",
        )
        assert_matches_type(BillingUsageHistoryResponse, billing, path=["response"])

    @parametrize
    def test_method_usage_history_with_all_params(self, client: Cloudflare) -> None:
        billing = client.ai_gateway.billing.usage_history(
            account_id="account_id",
            value_grouping_window="day",
            end_time=1700086400000,
            start_time=1700000000000,
        )
        assert_matches_type(BillingUsageHistoryResponse, billing, path=["response"])

    @parametrize
    def test_raw_response_usage_history(self, client: Cloudflare) -> None:
        response = client.ai_gateway.billing.with_raw_response.usage_history(
            account_id="account_id",
            value_grouping_window="day",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        billing = response.parse()
        assert_matches_type(BillingUsageHistoryResponse, billing, path=["response"])

    @parametrize
    def test_streaming_response_usage_history(self, client: Cloudflare) -> None:
        with client.ai_gateway.billing.with_streaming_response.usage_history(
            account_id="account_id",
            value_grouping_window="day",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            billing = response.parse()
            assert_matches_type(BillingUsageHistoryResponse, billing, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_usage_history(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.ai_gateway.billing.with_raw_response.usage_history(
                account_id="",
                value_grouping_window="day",
            )


class TestAsyncBilling:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="HTTP 404 error from prism -- route not in spec")
    @parametrize
    async def test_method_credit_balance(self, async_client: AsyncCloudflare) -> None:
        billing = await async_client.ai_gateway.billing.credit_balance(
            account_id="account_id",
        )
        assert_matches_type(BillingCreditBalanceResponse, billing, path=["response"])

    @pytest.mark.skip(reason="HTTP 404 error from prism -- route not in spec")
    @parametrize
    async def test_raw_response_credit_balance(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.ai_gateway.billing.with_raw_response.credit_balance(
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        billing = await response.parse()
        assert_matches_type(BillingCreditBalanceResponse, billing, path=["response"])

    @pytest.mark.skip(reason="HTTP 404 error from prism -- route not in spec")
    @parametrize
    async def test_streaming_response_credit_balance(self, async_client: AsyncCloudflare) -> None:
        async with async_client.ai_gateway.billing.with_streaming_response.credit_balance(
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            billing = await response.parse()
            assert_matches_type(BillingCreditBalanceResponse, billing, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="HTTP 404 error from prism -- route not in spec")
    @parametrize
    async def test_path_params_credit_balance(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.ai_gateway.billing.with_raw_response.credit_balance(
                account_id="",
            )

    @parametrize
    async def test_method_invoice_history(self, async_client: AsyncCloudflare) -> None:
        billing = await async_client.ai_gateway.billing.invoice_history(
            account_id="account_id",
        )
        assert_matches_type(BillingInvoiceHistoryResponse, billing, path=["response"])

    @parametrize
    async def test_method_invoice_history_with_all_params(self, async_client: AsyncCloudflare) -> None:
        billing = await async_client.ai_gateway.billing.invoice_history(
            account_id="account_id",
            type="all",
        )
        assert_matches_type(BillingInvoiceHistoryResponse, billing, path=["response"])

    @parametrize
    async def test_raw_response_invoice_history(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.ai_gateway.billing.with_raw_response.invoice_history(
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        billing = await response.parse()
        assert_matches_type(BillingInvoiceHistoryResponse, billing, path=["response"])

    @parametrize
    async def test_streaming_response_invoice_history(self, async_client: AsyncCloudflare) -> None:
        async with async_client.ai_gateway.billing.with_streaming_response.invoice_history(
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            billing = await response.parse()
            assert_matches_type(BillingInvoiceHistoryResponse, billing, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_invoice_history(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.ai_gateway.billing.with_raw_response.invoice_history(
                account_id="",
            )

    @parametrize
    async def test_method_invoice_preview(self, async_client: AsyncCloudflare) -> None:
        billing = await async_client.ai_gateway.billing.invoice_preview(
            account_id="account_id",
        )
        assert_matches_type(BillingInvoicePreviewResponse, billing, path=["response"])

    @parametrize
    async def test_raw_response_invoice_preview(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.ai_gateway.billing.with_raw_response.invoice_preview(
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        billing = await response.parse()
        assert_matches_type(BillingInvoicePreviewResponse, billing, path=["response"])

    @parametrize
    async def test_streaming_response_invoice_preview(self, async_client: AsyncCloudflare) -> None:
        async with async_client.ai_gateway.billing.with_streaming_response.invoice_preview(
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            billing = await response.parse()
            assert_matches_type(BillingInvoicePreviewResponse, billing, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_invoice_preview(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.ai_gateway.billing.with_raw_response.invoice_preview(
                account_id="",
            )

    @parametrize
    async def test_method_usage_history(self, async_client: AsyncCloudflare) -> None:
        billing = await async_client.ai_gateway.billing.usage_history(
            account_id="account_id",
            value_grouping_window="day",
        )
        assert_matches_type(BillingUsageHistoryResponse, billing, path=["response"])

    @parametrize
    async def test_method_usage_history_with_all_params(self, async_client: AsyncCloudflare) -> None:
        billing = await async_client.ai_gateway.billing.usage_history(
            account_id="account_id",
            value_grouping_window="day",
            end_time=1700086400000,
            start_time=1700000000000,
        )
        assert_matches_type(BillingUsageHistoryResponse, billing, path=["response"])

    @parametrize
    async def test_raw_response_usage_history(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.ai_gateway.billing.with_raw_response.usage_history(
            account_id="account_id",
            value_grouping_window="day",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        billing = await response.parse()
        assert_matches_type(BillingUsageHistoryResponse, billing, path=["response"])

    @parametrize
    async def test_streaming_response_usage_history(self, async_client: AsyncCloudflare) -> None:
        async with async_client.ai_gateway.billing.with_streaming_response.usage_history(
            account_id="account_id",
            value_grouping_window="day",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            billing = await response.parse()
            assert_matches_type(BillingUsageHistoryResponse, billing, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_usage_history(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.ai_gateway.billing.with_raw_response.usage_history(
                account_id="",
                value_grouping_window="day",
            )
