#!/bin/bash

echo "UT test start ..."
python3 -m unittest test_api_signature.TestApi
python3 -m unittest test_apply_loan.TestApplyLoan
python3 -m unittest test_cancel_open_orders.TestCancelOpenOrders
python3 -m unittest test_cancel_order.TestCancelOrder
python3 -m unittest test_cancel_withdraw.TestCancelWithdraw
python3 -m unittest test_create_order.TestCreateOrder
python3 -m unittest test_error_response.TestErrorResponse
python3 -m unittest test_etf_swap.TestEtfSwap
python3 -m unittest test_get_24h_trade_statistics.TestGet24HTradeStatistics
python3 -m unittest test_get_balance.TestGetBalance
python3 -m unittest test_get_best_quote.TestGetBestQuote
python3 -m unittest test_get_candlestick.TestGetCandlestick
python3 -m unittest test_get_currencies.TestGetCurrencies
python3 -m unittest test_get_deposit_history.TestGetDepositHistory
python3 -m unittest test_get_etf_candlestick.TestGetETFCandlestick
python3 -m unittest test_get_etf_swap_config.TestGetEtfSwapConfig
python3 -m unittest test_get_etf_swap_history.TestGetEtfSwapHistory
python3 -m unittest test_get_historical_trade.TestGetHistoricalTrade
python3 -m unittest test_get_history_orders.TestGetHistoryOrders
python3 -m unittest test_get_loan_history.TestGetLoanHistory
python3 -m unittest test_get_margin_balance_detail.TestGetMarginBalanceDetail
python3 -m unittest test_get_match_result_by_order_id.TestGetMatchResultByOrderId
python3 -m unittest test_get_match_result_by_request.TestGetMatchResultByRequest
python3 -m unittest test_get_open_orders.TestGetOpenOrders
python3 -m unittest test_get_order.TestGetOrders
python3 -m unittest test_get_price_depth.TestGetPriceDepth
python3 -m unittest test_get_specify_account.TestGetSpecifyAccount
python3 -m unittest test_get_symbols.TestGetSymbols
python3 -m unittest test_get_withdraw_history.TestGetWithdrawHistory
python3 -m unittest test_repay_loan.TestRepayLoan
python3 -m unittest test_subscribe_account_event.TestSubscribeAccountEvent
python3 -m unittest test_subscribe_candlestick_event.TestSubscribeCandlestickEvent
python3 -m unittest test_subscribe_order_update_event.TestSubscribeOrderUpdateEvent
python3 -m unittest test_subscribe_price_depth_event.TestSubscribePriceDepthEvent
python3 -m unittest test_subscribe_trade_event.TestSubscribeTradeEvent
python3 -m unittest test_subscribe_trade_statistics.TestSubscribeTradeStatistics
python3 -m unittest test_transfer.TestTransfer
python3 -m unittest test_transfer_master.TestTransferMaster
python3 -m unittest test_withdraw.TestWithdraw
echo "UT test end ..."