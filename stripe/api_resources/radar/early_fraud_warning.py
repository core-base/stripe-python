# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec

from stripe.api_resources.abstract import ListableAPIResource


class EarlyFraudWarning(ListableAPIResource):
    """
    An early fraud warning indicates that the card issuer has notified us that a
    charge may be fraudulent.

    Related guide: [Early fraud warnings](https://stripe.com/docs/disputes/measuring#early-fraud-warnings)
    """

    OBJECT_NAME = "radar.early_fraud_warning"
