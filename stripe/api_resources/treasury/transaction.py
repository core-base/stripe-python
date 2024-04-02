# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec

from stripe.api_resources.abstract import ListableAPIResource


class Transaction(ListableAPIResource):
    """
    Transactions represent changes to a [FinancialAccount's](https://stripe.com/docs/api#financial_accounts) balance.
    """

    OBJECT_NAME = "treasury.transaction"
