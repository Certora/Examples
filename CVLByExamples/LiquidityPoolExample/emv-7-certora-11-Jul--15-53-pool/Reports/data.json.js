data = {
	"contractName": "PoolHarness",
		 "main_table": {
			"tableHeader":[
				"Test name",
				"Result",
				"Time(sec)",
				"Dump"
			],
			"contractResult":[
				{
					 "tableRow": {
						"ruleName": "envfreeFuncsStaticCheck",
						"result": "SUCCESS",
						"time": "0",
						"graph_link": "",
						"preoptimized_link": "",
						"presimplified_link": "",
						"prelastopt_link": "",
						"presolver_link": ""
					},
					"isMultiRule": true
				},
				{
					 "tableRow": {
						"ruleName": "flashLoanIncreasesBalance",
						"result": "SUCCESS",
						"time": "233",
						"graph_link": "",
						"preoptimized_link": "PreoptimizedRule-flashLoanIncreasesBalance.html",
						"presimplified_link": "PresimplifiedRule-flashLoanIncreasesBalance.html",
						"prelastopt_link": "PrelastoptRule-flashLoanIncreasesBalance.html",
						"presolver_link": "PresolverRule-flashLoanIncreasesBalance.html"
					},
					"isMultiRule": false,
					 "callResolutionTable": {
						"tableHeader":[
							"Caller",
							"Callee",
							"Summary"
						],
						"callResolution":[
							{
								 "tableRow": {
									"caller": "PoolHarness.underlyingAllowance(address)",
									"callee": "[?].allowance(address, address)",
									"summmary": "DISPATCHER(optimistic = true)",
									"comments":[
										{
											"alternative callees": "[Asset | DummyERC20A | DummyERC20B | DummyERC20Impl | DummyWeth | ERC20Basic | FTT | PoolHarness | SushiToken | USDC | USDT]"
										},
										{
											"callee resolution": "callee contract unresolved; callee sighash resolved"
										},
										{
											"callee resolution hint (1)": "To resolve the call, try '--link PoolHarness:asset=[Asset | DummyERC20A | DummyERC20B | DummyERC20Impl | DummyWeth | ERC20Basic | FTT | PoolHarness | SushiToken | USDC | USDT]'"
										},
										{
											"summary application reason": "declared at erc20.spec:19:66 to apply only to calls without available callee implementation"
										}
									]
								}
							},
							{
								 "tableRow": {
									"caller": "PoolHarness.underlyingBalance()",
									"callee": "[?].balanceOf(address)",
									"summmary": "DISPATCHER(optimistic = true)",
									"comments":[
										{
											"alternative callees": "[Asset | DummyERC20A | DummyERC20B | DummyERC20Impl | DummyWeth | ERC20Basic | FTT | PoolHarness | SushiToken | USDC | USDT]"
										},
										{
											"callee resolution": "callee contract unresolved; callee sighash resolved"
										},
										{
											"callee resolution hint (1)": "To resolve the call, try '--link PoolHarness:asset=[Asset | DummyERC20A | DummyERC20B | DummyERC20Impl | DummyWeth | ERC20Basic | FTT | PoolHarness | SushiToken | USDC | USDT]'"
										},
										{
											"summary application reason": "declared at erc20.spec:18:66 to apply only to calls without available callee implementation"
										}
									]
								}
							},
							{
								 "tableRow": {
									"caller": "PoolHarness.flashLoan(address,uint256)",
									"callee": "[?].transferFrom(address, address, uint256)",
									"summmary": "DISPATCHER(optimistic = true)",
									"comments":[
										{
											"alternative callees": "[Asset | DummyERC20A | DummyERC20B | DummyERC20Impl | DummyWeth | ERC20Basic | FTT | PoolHarness | SushiToken | USDC | USDT]"
										},
										{
											"callee resolution": "callee contract unresolved; callee sighash resolved"
										},
										{
											"callee resolution hint (1)": "To resolve the call, try '--link PoolHarness:asset=[Asset | DummyERC20A | DummyERC20B | DummyERC20Impl | DummyWeth | ERC20Basic | FTT | PoolHarness | SushiToken | USDC | USDT]'"
										},
										{
											"summary application reason": "declared at erc20.spec:22:66 to apply only to calls without available callee implementation"
										}
									]
								}
							},
							{
								 "tableRow": {
									"caller": "PoolHarness.flashLoan(address,uint256)",
									"callee": "[?].executeOperation(uint256, uint256, address)",
									"summmary": "DISPATCHER(optimistic = true)",
									"comments":[
										{
											"alternative callees": "[FlexibleReceiver | TransferReceiver | TrivialReceiver]"
										},
										{
											"callee resolution": "callee contract unresolved; callee sighash resolved"
										},
										{
											"summary application reason": "declared at pool.spec:16:70 to apply only to calls without available callee implementation"
										}
									]
								}
							},
							{
								 "tableRow": {
									"caller": "FlexibleReceiver.executeOperation(uint256,uint256,address)",
									"callee": "[?].approve(address, uint256)",
									"summmary": "DISPATCHER(optimistic = true)",
									"comments":[
										{
											"alternative callees": "[Asset | DummyERC20A | DummyERC20B | DummyERC20Impl | DummyWeth | ERC20Basic | FTT | PoolHarness | SushiToken | USDC | USDT]"
										},
										{
											"callee resolution": "callee contract unresolved; callee sighash resolved"
										},
										{
											"callee resolution hint (1)": "To resolve the call, try '--link FlexibleReceiver:token=[Asset | DummyERC20A | DummyERC20B | DummyERC20Impl | DummyWeth | ERC20Basic | FTT | PoolHarness | SushiToken | USDC | USDT]'"
										},
										{
											"summary application reason": "declared at erc20.spec:20:66 to apply only to calls without available callee implementation"
										}
									]
								}
							},
							{
								 "tableRow": {
									"caller": "FlexibleReceiver.executeOperation(uint256,uint256,address)",
									"callee": "[?].transfer(address, uint256)",
									"summmary": "DISPATCHER(optimistic = true)",
									"comments":[
										{
											"alternative callees": "[Asset | DummyERC20A | DummyERC20B | DummyERC20Impl | DummyWeth | ERC20Basic | FTT | PoolHarness | SushiToken | USDC | USDT]"
										},
										{
											"callee resolution": "callee contract unresolved; callee sighash resolved"
										},
										{
											"callee resolution hint (1)": "To resolve the call, try '--link FlexibleReceiver:token=[Asset | DummyERC20A | DummyERC20B | DummyERC20Impl | DummyWeth | ERC20Basic | FTT | PoolHarness | SushiToken | USDC | USDT]'"
										},
										{
											"summary application reason": "declared at erc20.spec:21:66 to apply only to calls without available callee implementation"
										}
									]
								}
							},
							{
								 "tableRow": {
									"caller": "FlexibleReceiver.executeOperation(uint256,uint256,address)",
									"callee": "[?].withdraw(uint256)",
									"summmary": "DISPATCHER(optimistic = true)",
									"comments":[
										{
											"alternative callees": "[DummyWeth | PoolHarness]"
										},
										{
											"callee resolution": "callee contract unresolved; callee sighash resolved"
										},
										{
											"callee resolution hint (1)": "To resolve the call, try '--link FlexibleReceiver:token=[DummyWeth | PoolHarness]'"
										},
										{
											"summary application reason": "declared at pool.spec:12:46 to apply only to calls without available callee implementation"
										}
									]
								}
							},
							{
								 "tableRow": {
									"caller": "FlexibleReceiver.executeOperation(uint256,uint256,address)",
									"callee": "[?].transferFrom(address, address, uint256)",
									"summmary": "DISPATCHER(optimistic = true)",
									"comments":[
										{
											"alternative callees": "[Asset | DummyERC20A | DummyERC20B | DummyERC20Impl | DummyWeth | ERC20Basic | FTT | PoolHarness | SushiToken | USDC | USDT]"
										},
										{
											"callee resolution": "callee contract unresolved; callee sighash resolved"
										},
										{
											"callee resolution hint (1)": "To resolve the call, try '--link FlexibleReceiver:token=[Asset | DummyERC20A | DummyERC20B | DummyERC20Impl | DummyWeth | ERC20Basic | FTT | PoolHarness | SushiToken | USDC | USDT]'"
										},
										{
											"summary application reason": "declared at erc20.spec:22:66 to apply only to calls without available callee implementation"
										}
									]
								}
							},
							{
								 "tableRow": {
									"caller": "FlexibleReceiver.executeOperation(uint256,uint256,address)",
									"callee": "[?].deposit(uint256)",
									"summmary": "DISPATCHER(optimistic = true)",
									"comments":[
										{
											"alternative callees": "[PoolHarness]"
										},
										{
											"callee resolution": "callee contract unresolved; callee sighash resolved"
										},
										{
											"callee resolution hint (1)": "To resolve the call, try '--link FlexibleReceiver:token=[PoolHarness]'"
										},
										{
											"summary application reason": "declared at pool.spec:11:46 to apply only to calls without available callee implementation"
										}
									]
								}
							},
							{
								 "tableRow": {
									"caller": "TransferReceiver.executeOperation(uint256,uint256,address)",
									"callee": "[?].transferFrom(address, address, uint256)",
									"summmary": "DISPATCHER(optimistic = true)",
									"comments":[
										{
											"alternative callees": "[Asset | DummyERC20A | DummyERC20B | DummyERC20Impl | DummyWeth | ERC20Basic | FTT | PoolHarness | SushiToken | USDC | USDT]"
										},
										{
											"callee resolution": "callee contract unresolved; callee sighash resolved"
										},
										{
											"callee resolution hint (1)": "To resolve the call, try '--link TransferReceiver:underlying=[Asset | DummyERC20A | DummyERC20B | DummyERC20Impl | DummyWeth | ERC20Basic | FTT | PoolHarness | SushiToken | USDC | USDT]'"
										},
										{
											"summary application reason": "declared at erc20.spec:22:66 to apply only to calls without available callee implementation"
										}
									]
								}
							},
							{
								 "tableRow": {
									"caller": "PoolHarness.flashLoan(address,uint256)",
									"callee": "[?].transferFrom(address, address, uint256)",
									"summmary": "DISPATCHER(optimistic = true)",
									"comments":[
										{
											"alternative callees": "[Asset | DummyERC20A | DummyERC20B | DummyERC20Impl | DummyWeth | ERC20Basic | FTT | PoolHarness | SushiToken | USDC | USDT]"
										},
										{
											"callee resolution": "callee contract unresolved; callee sighash resolved"
										},
										{
											"callee resolution hint (1)": "To resolve the call, try '--link PoolHarness:asset=[Asset | DummyERC20A | DummyERC20B | DummyERC20Impl | DummyWeth | ERC20Basic | FTT | PoolHarness | SushiToken | USDC | USDT]'"
										},
										{
											"summary application reason": "declared at erc20.spec:22:66 to apply only to calls without available callee implementation"
										}
									]
								}
							}
						]
					},
					 "callResolutionWarningsTable": {
						"tableHeader":[
							"Caller",
							"Callee",
							"Summary"
						],
						"callResolutionWarnings":[

						]
					}
				},
				{
					 "tableRow": {
						"ruleName": "integrityOfDeposit",
						"result": "SUCCESS",
						"time": "11",
						"graph_link": "",
						"preoptimized_link": "PreoptimizedRule-integrityOfDeposit.html",
						"presimplified_link": "PresimplifiedRule-integrityOfDeposit.html",
						"prelastopt_link": "PrelastoptRule-integrityOfDeposit.html",
						"presolver_link": "PresolverRule-integrityOfDeposit.html"
					},
					"isMultiRule": false,
					 "callResolutionTable": {
						"tableHeader":[
							"Caller",
							"Callee",
							"Summary"
						],
						"callResolution":[
							{
								 "tableRow": {
									"caller": "PoolHarness.underlyingBalance()",
									"callee": "[?].balanceOf(address)",
									"summmary": "DISPATCHER(optimistic = true)",
									"comments":[
										{
											"alternative callees": "[Asset | DummyERC20A | DummyERC20B | DummyERC20Impl | DummyWeth | ERC20Basic | FTT | PoolHarness | SushiToken | USDC | USDT]"
										},
										{
											"callee resolution": "callee contract unresolved; callee sighash resolved"
										},
										{
											"callee resolution hint (1)": "To resolve the call, try '--link PoolHarness:asset=[Asset | DummyERC20A | DummyERC20B | DummyERC20Impl | DummyWeth | ERC20Basic | FTT | PoolHarness | SushiToken | USDC | USDT]'"
										},
										{
											"summary application reason": "declared at erc20.spec:18:66 to apply only to calls without available callee implementation"
										}
									]
								}
							},
							{
								 "tableRow": {
									"caller": "PoolHarness.underlyingAllowance(address)",
									"callee": "[?].allowance(address, address)",
									"summmary": "DISPATCHER(optimistic = true)",
									"comments":[
										{
											"alternative callees": "[Asset | DummyERC20A | DummyERC20B | DummyERC20Impl | DummyWeth | ERC20Basic | FTT | PoolHarness | SushiToken | USDC | USDT]"
										},
										{
											"callee resolution": "callee contract unresolved; callee sighash resolved"
										},
										{
											"callee resolution hint (1)": "To resolve the call, try '--link PoolHarness:asset=[Asset | DummyERC20A | DummyERC20B | DummyERC20Impl | DummyWeth | ERC20Basic | FTT | PoolHarness | SushiToken | USDC | USDT]'"
										},
										{
											"summary application reason": "declared at erc20.spec:19:66 to apply only to calls without available callee implementation"
										}
									]
								}
							},
							{
								 "tableRow": {
									"caller": "PoolHarness.deposit(uint256)",
									"callee": "[?].balanceOf(address)",
									"summmary": "DISPATCHER(optimistic = true)",
									"comments":[
										{
											"alternative callees": "[Asset | DummyERC20A | DummyERC20B | DummyERC20Impl | DummyWeth | ERC20Basic | FTT | PoolHarness | SushiToken | USDC | USDT]"
										},
										{
											"callee resolution": "callee contract unresolved; callee sighash resolved"
										},
										{
											"callee resolution hint (1)": "To resolve the call, try '--link PoolHarness:asset=[Asset | DummyERC20A | DummyERC20B | DummyERC20Impl | DummyWeth | ERC20Basic | FTT | PoolHarness | SushiToken | USDC | USDT]'"
										},
										{
											"summary application reason": "declared at erc20.spec:18:66 to apply only to calls without available callee implementation"
										}
									]
								}
							},
							{
								 "tableRow": {
									"caller": "PoolHarness.deposit(uint256)",
									"callee": "[?].balanceOf(address)",
									"summmary": "DISPATCHER(optimistic = true)",
									"comments":[
										{
											"alternative callees": "[Asset | DummyERC20A | DummyERC20B | DummyERC20Impl | DummyWeth | ERC20Basic | FTT | PoolHarness | SushiToken | USDC | USDT]"
										},
										{
											"callee resolution": "callee contract unresolved; callee sighash resolved"
										},
										{
											"callee resolution hint (1)": "To resolve the call, try '--link PoolHarness:asset=[Asset | DummyERC20A | DummyERC20B | DummyERC20Impl | DummyWeth | ERC20Basic | FTT | PoolHarness | SushiToken | USDC | USDT]'"
										},
										{
											"summary application reason": "declared at erc20.spec:18:66 to apply only to calls without available callee implementation"
										}
									]
								}
							},
							{
								 "tableRow": {
									"caller": "PoolHarness.deposit(uint256)",
									"callee": "[?].transferFrom(address, address, uint256)",
									"summmary": "DISPATCHER(optimistic = true)",
									"comments":[
										{
											"alternative callees": "[Asset | DummyERC20A | DummyERC20B | DummyERC20Impl | DummyWeth | ERC20Basic | FTT | PoolHarness | SushiToken | USDC | USDT]"
										},
										{
											"callee resolution": "callee contract unresolved; callee sighash resolved"
										},
										{
											"callee resolution hint (1)": "To resolve the call, try '--link PoolHarness:asset=[Asset | DummyERC20A | DummyERC20B | DummyERC20Impl | DummyWeth | ERC20Basic | FTT | PoolHarness | SushiToken | USDC | USDT]'"
										},
										{
											"summary application reason": "declared at erc20.spec:22:66 to apply only to calls without available callee implementation"
										}
									]
								}
							}
						]
					},
					 "callResolutionWarningsTable": {
						"tableHeader":[
							"Caller",
							"Callee",
							"Summary"
						],
						"callResolutionWarnings":[

						]
					}
				},
				{
					 "tableRow": {
						"ruleName": "noAllowance",
						"result": "SUCCESS",
						"time": "198",
						"graph_link": "",
						"preoptimized_link": "",
						"presimplified_link": "",
						"prelastopt_link": "",
						"presolver_link": ""
					},
					"isMultiRule": true
				},
				{
					 "tableRow": {
						"ruleName": "noAllowance_instate",
						"result": "SUCCESS",
						"time": "16",
						"graph_link": "",
						"preoptimized_link": "PreoptimizedRule-noAllowance_instate.html",
						"presimplified_link": "PresimplifiedRule-noAllowance_instate.html",
						"prelastopt_link": "PrelastoptRule-noAllowance_instate.html",
						"presolver_link": "PresolverRule-noAllowance_instate.html"
					},
					"isMultiRule": false,
					 "callResolutionTable": {
						"tableHeader":[
							"Caller",
							"Callee",
							"Summary"
						],
						"callResolution":[
							{
								 "tableRow": {
									"caller": "PoolHarness.underlyingAllowance(address)",
									"callee": "[?].allowance(address, address)",
									"summmary": "DISPATCHER(optimistic = true)",
									"comments":[
										{
											"alternative callees": "[Asset | DummyERC20A | DummyERC20B | DummyERC20Impl | DummyWeth | ERC20Basic | FTT | PoolHarness | SushiToken | USDC | USDT]"
										},
										{
											"callee resolution": "callee contract unresolved; callee sighash resolved"
										},
										{
											"callee resolution hint (1)": "To resolve the call, try '--link PoolHarness:asset=[Asset | DummyERC20A | DummyERC20B | DummyERC20Impl | DummyWeth | ERC20Basic | FTT | PoolHarness | SushiToken | USDC | USDT]'"
										},
										{
											"summary application reason": "declared at erc20.spec:19:66 to apply only to calls without available callee implementation"
										}
									]
								}
							}
						]
					},
					 "callResolutionWarningsTable": {
						"tableHeader":[
							"Caller",
							"Callee",
							"Summary"
						],
						"callResolutionWarnings":[

						]
					}
				}
			]

		},
		 "sub_tables": {
			"tableHeader":[
				"Function name",
				"Result",
				"Time(secs)",
				"Dump"
			],
			"functionResults":[
		{
			"ruleName": "envfreeFuncsStaticCheck",
			"tableBody":[
				{
					 "tableRow": {
						"funcName": "asset()",
						"result": "SUCCESS",
						"time": "0",
						"graph_link": "",
						"preoptimized_link": "PreoptimizedRule-envfreeFuncsStaticCheck-assetLPRP.html",
						"presimplified_link": "PresimplifiedRule-envfreeFuncsStaticCheck-assetLPRP.html",
						"prelastopt_link": "PrelastoptRule-envfreeFuncsStaticCheck-assetLPRP.html",
						"presolver_link": "PresolverRule-envfreeFuncsStaticCheck-assetLPRP.html"
					},
					 "callResolutionTable": {
						"tableHeader":[
							"Caller",
							"Callee",
							"Summary"
						],
						"callResolution":[

						]
					},
					 "callResolutionWarningsTable": {
						"tableHeader":[
							"Caller",
							"Callee",
							"Summary"
						],
						"callResolutionWarnings":[

						]
					}
				}
,				{
					 "tableRow": {
						"funcName": "balanceOf(address)",
						"result": "SUCCESS",
						"time": "0",
						"graph_link": "",
						"preoptimized_link": "PreoptimizedRule-envfreeFuncsStaticCheck-balanceOfLPADRRP.html",
						"presimplified_link": "PresimplifiedRule-envfreeFuncsStaticCheck-balanceOfLPADRRP.html",
						"prelastopt_link": "PrelastoptRule-envfreeFuncsStaticCheck-balanceOfLPADRRP.html",
						"presolver_link": "PresolverRule-envfreeFuncsStaticCheck-balanceOfLPADRRP.html"
					},
					 "callResolutionTable": {
						"tableHeader":[
							"Caller",
							"Callee",
							"Summary"
						],
						"callResolution":[

						]
					},
					 "callResolutionWarningsTable": {
						"tableHeader":[
							"Caller",
							"Callee",
							"Summary"
						],
						"callResolutionWarnings":[

						]
					}
				}
,				{
					 "tableRow": {
						"funcName": "totalSupply()",
						"result": "SUCCESS",
						"time": "0",
						"graph_link": "",
						"preoptimized_link": "PreoptimizedRule-envfreeFuncsStaticCheck-totalSupplyLPRP.html",
						"presimplified_link": "PresimplifiedRule-envfreeFuncsStaticCheck-totalSupplyLPRP.html",
						"prelastopt_link": "PrelastoptRule-envfreeFuncsStaticCheck-totalSupplyLPRP.html",
						"presolver_link": "PresolverRule-envfreeFuncsStaticCheck-totalSupplyLPRP.html"
					},
					 "callResolutionTable": {
						"tableHeader":[
							"Caller",
							"Callee",
							"Summary"
						],
						"callResolution":[

						]
					},
					 "callResolutionWarningsTable": {
						"tableHeader":[
							"Caller",
							"Callee",
							"Summary"
						],
						"callResolutionWarnings":[

						]
					}
				}
,				{
					 "tableRow": {
						"funcName": "underlyingAllowance(address)",
						"result": "SUCCESS",
						"time": "0",
						"graph_link": "",
						"preoptimized_link": "PreoptimizedRule-envfreeFuncsStaticCheck-underlyingAllowanceLPADRRP.html",
						"presimplified_link": "PresimplifiedRule-envfreeFuncsStaticCheck-underlyingAllowanceLPADRRP.html",
						"prelastopt_link": "PrelastoptRule-envfreeFuncsStaticCheck-underlyingAllowanceLPADRRP.html",
						"presolver_link": "PresolverRule-envfreeFuncsStaticCheck-underlyingAllowanceLPADRRP.html"
					},
					 "callResolutionTable": {
						"tableHeader":[
							"Caller",
							"Callee",
							"Summary"
						],
						"callResolution":[

						]
					},
					 "callResolutionWarningsTable": {
						"tableHeader":[
							"Caller",
							"Callee",
							"Summary"
						],
						"callResolutionWarnings":[

						]
					}
				}
,				{
					 "tableRow": {
						"funcName": "underlyingBalance()",
						"result": "SUCCESS",
						"time": "0",
						"graph_link": "",
						"preoptimized_link": "PreoptimizedRule-envfreeFuncsStaticCheck-underlyingBalanceLPRP.html",
						"presimplified_link": "PresimplifiedRule-envfreeFuncsStaticCheck-underlyingBalanceLPRP.html",
						"prelastopt_link": "PrelastoptRule-envfreeFuncsStaticCheck-underlyingBalanceLPRP.html",
						"presolver_link": "PresolverRule-envfreeFuncsStaticCheck-underlyingBalanceLPRP.html"
					},
					 "callResolutionTable": {
						"tableHeader":[
							"Caller",
							"Callee",
							"Summary"
						],
						"callResolution":[

						]
					},
					 "callResolutionWarningsTable": {
						"tableHeader":[
							"Caller",
							"Callee",
							"Summary"
						],
						"callResolutionWarnings":[

						]
					}
				}
			]

		},
				{
					"ruleName": "noAllowance_preserve",
					"tableBody":[
						{
							 "tableRow": {
								"funcName": "approve(address,uint256)",
								"result": "SUCCESS",
								"time": "18",
								"graph_link": "",
								"preoptimized_link": "PreoptimizedRule-noAllowance_preserve-approveLPADRCU256RP.html",
								"presimplified_link": "PresimplifiedRule-noAllowance_preserve-approveLPADRCU256RP.html",
								"prelastopt_link": "PrelastoptRule-noAllowance_preserve-approveLPADRCU256RP.html",
								"presolver_link": "PresolverRule-noAllowance_preserve-approveLPADRCU256RP.html"
							},
							 "callResolutionTable": {
								"tableHeader":[
									"Caller",
									"Callee",
									"Summary"
								],
								"callResolution":[
									{
										 "tableRow": {
											"caller": "PoolHarness.underlyingAllowance(address)",
											"callee": "[?].allowance(address, address)",
											"summmary": "DISPATCHER(optimistic = true)",
											"comments":[
												{
													"alternative callees": "[Asset | DummyERC20A | DummyERC20B | DummyERC20Impl | DummyWeth | ERC20Basic | FTT | PoolHarness | SushiToken | USDC | USDT]"
												},
												{
													"callee resolution": "callee contract unresolved; callee sighash resolved"
												},
												{
													"callee resolution hint (1)": "To resolve the call, try '--link PoolHarness:asset=[Asset | DummyERC20A | DummyERC20B | DummyERC20Impl | DummyWeth | ERC20Basic | FTT | PoolHarness | SushiToken | USDC | USDT]'"
												},
												{
													"summary application reason": "declared at erc20.spec:19:66 to apply only to calls without available callee implementation"
												}
											]
										}
									}
								]
							},
							 "callResolutionWarningsTable": {
								"tableHeader":[
									"Caller",
									"Callee",
									"Summary"
								],
								"callResolutionWarnings":[

								]
							}
						}
,						{
							 "tableRow": {
								"funcName": "deposit(uint256)",
								"result": "SUCCESS",
								"time": "9",
								"graph_link": "",
								"preoptimized_link": "PreoptimizedRule-noAllowance_preserve-depositLPU256RP.html",
								"presimplified_link": "PresimplifiedRule-noAllowance_preserve-depositLPU256RP.html",
								"prelastopt_link": "PrelastoptRule-noAllowance_preserve-depositLPU256RP.html",
								"presolver_link": "PresolverRule-noAllowance_preserve-depositLPU256RP.html"
							},
							 "callResolutionTable": {
								"tableHeader":[
									"Caller",
									"Callee",
									"Summary"
								],
								"callResolution":[
									{
										 "tableRow": {
											"caller": "PoolHarness.underlyingAllowance(address)",
											"callee": "[?].allowance(address, address)",
											"summmary": "DISPATCHER(optimistic = true)",
											"comments":[
												{
													"alternative callees": "[Asset | DummyERC20A | DummyERC20B | DummyERC20Impl | DummyWeth | ERC20Basic | FTT | PoolHarness | SushiToken | USDC | USDT]"
												},
												{
													"callee resolution": "callee contract unresolved; callee sighash resolved"
												},
												{
													"callee resolution hint (1)": "To resolve the call, try '--link PoolHarness:asset=[Asset | DummyERC20A | DummyERC20B | DummyERC20Impl | DummyWeth | ERC20Basic | FTT | PoolHarness | SushiToken | USDC | USDT]'"
												},
												{
													"summary application reason": "declared at erc20.spec:19:66 to apply only to calls without available callee implementation"
												}
											]
										}
									},
									{
										 "tableRow": {
											"caller": "PoolHarness.deposit(uint256)",
											"callee": "[?].balanceOf(address)",
											"summmary": "DISPATCHER(optimistic = true)",
											"comments":[
												{
													"alternative callees": "[Asset | DummyERC20A | DummyERC20B | DummyERC20Impl | DummyWeth | ERC20Basic | FTT | PoolHarness | SushiToken | USDC | USDT]"
												},
												{
													"callee resolution": "callee contract unresolved; callee sighash resolved"
												},
												{
													"callee resolution hint (1)": "To resolve the call, try '--link PoolHarness:asset=[Asset | DummyERC20A | DummyERC20B | DummyERC20Impl | DummyWeth | ERC20Basic | FTT | PoolHarness | SushiToken | USDC | USDT]'"
												},
												{
													"summary application reason": "declared at erc20.spec:18:66 to apply only to calls without available callee implementation"
												}
											]
										}
									},
									{
										 "tableRow": {
											"caller": "PoolHarness.deposit(uint256)",
											"callee": "[?].balanceOf(address)",
											"summmary": "DISPATCHER(optimistic = true)",
											"comments":[
												{
													"alternative callees": "[Asset | DummyERC20A | DummyERC20B | DummyERC20Impl | DummyWeth | ERC20Basic | FTT | PoolHarness | SushiToken | USDC | USDT]"
												},
												{
													"callee resolution": "callee contract unresolved; callee sighash resolved"
												},
												{
													"callee resolution hint (1)": "To resolve the call, try '--link PoolHarness:asset=[Asset | DummyERC20A | DummyERC20B | DummyERC20Impl | DummyWeth | ERC20Basic | FTT | PoolHarness | SushiToken | USDC | USDT]'"
												},
												{
													"summary application reason": "declared at erc20.spec:18:66 to apply only to calls without available callee implementation"
												}
											]
										}
									},
									{
										 "tableRow": {
											"caller": "PoolHarness.deposit(uint256)",
											"callee": "[?].transferFrom(address, address, uint256)",
											"summmary": "DISPATCHER(optimistic = true)",
											"comments":[
												{
													"alternative callees": "[Asset | DummyERC20A | DummyERC20B | DummyERC20Impl | DummyWeth | ERC20Basic | FTT | PoolHarness | SushiToken | USDC | USDT]"
												},
												{
													"callee resolution": "callee contract unresolved; callee sighash resolved"
												},
												{
													"callee resolution hint (1)": "To resolve the call, try '--link PoolHarness:asset=[Asset | DummyERC20A | DummyERC20B | DummyERC20Impl | DummyWeth | ERC20Basic | FTT | PoolHarness | SushiToken | USDC | USDT]'"
												},
												{
													"summary application reason": "declared at erc20.spec:22:66 to apply only to calls without available callee implementation"
												}
											]
										}
									}
								]
							},
							 "callResolutionWarningsTable": {
								"tableHeader":[
									"Caller",
									"Callee",
									"Summary"
								],
								"callResolutionWarnings":[

								]
							}
						}
,						{
							 "tableRow": {
								"funcName": "flashLoan(address,uint256)",
								"result": "SUCCESS",
								"time": "89",
								"graph_link": "",
								"preoptimized_link": "PreoptimizedRule-noAllowance_preserve-flashLoanLPADRCU256RP.html",
								"presimplified_link": "PresimplifiedRule-noAllowance_preserve-flashLoanLPADRCU256RP.html",
								"prelastopt_link": "PrelastoptRule-noAllowance_preserve-flashLoanLPADRCU256RP.html",
								"presolver_link": "PresolverRule-noAllowance_preserve-flashLoanLPADRCU256RP.html"
							},
							 "callResolutionTable": {
								"tableHeader":[
									"Caller",
									"Callee",
									"Summary"
								],
								"callResolution":[
									{
										 "tableRow": {
											"caller": "PoolHarness.underlyingAllowance(address)",
											"callee": "[?].allowance(address, address)",
											"summmary": "DISPATCHER(optimistic = true)",
											"comments":[
												{
													"alternative callees": "[Asset | DummyERC20A | DummyERC20B | DummyERC20Impl | DummyWeth | ERC20Basic | FTT | PoolHarness | SushiToken | USDC | USDT]"
												},
												{
													"callee resolution": "callee contract unresolved; callee sighash resolved"
												},
												{
													"callee resolution hint (1)": "To resolve the call, try '--link PoolHarness:asset=[Asset | DummyERC20A | DummyERC20B | DummyERC20Impl | DummyWeth | ERC20Basic | FTT | PoolHarness | SushiToken | USDC | USDT]'"
												},
												{
													"summary application reason": "declared at erc20.spec:19:66 to apply only to calls without available callee implementation"
												}
											]
										}
									},
									{
										 "tableRow": {
											"caller": "PoolHarness.flashLoan(address,uint256)",
											"callee": "[?].transferFrom(address, address, uint256)",
											"summmary": "DISPATCHER(optimistic = true)",
											"comments":[
												{
													"alternative callees": "[Asset | DummyERC20A | DummyERC20B | DummyERC20Impl | DummyWeth | ERC20Basic | FTT | PoolHarness | SushiToken | USDC | USDT]"
												},
												{
													"callee resolution": "callee contract unresolved; callee sighash resolved"
												},
												{
													"callee resolution hint (1)": "To resolve the call, try '--link PoolHarness:asset=[Asset | DummyERC20A | DummyERC20B | DummyERC20Impl | DummyWeth | ERC20Basic | FTT | PoolHarness | SushiToken | USDC | USDT]'"
												},
												{
													"summary application reason": "declared at erc20.spec:22:66 to apply only to calls without available callee implementation"
												}
											]
										}
									},
									{
										 "tableRow": {
											"caller": "PoolHarness.flashLoan(address,uint256)",
											"callee": "[?].executeOperation(uint256, uint256, address)",
											"summmary": "DISPATCHER(optimistic = true)",
											"comments":[
												{
													"alternative callees": "[FlexibleReceiver | TransferReceiver | TrivialReceiver]"
												},
												{
													"callee resolution": "callee contract unresolved; callee sighash resolved"
												},
												{
													"summary application reason": "declared at pool.spec:16:70 to apply only to calls without available callee implementation"
												}
											]
										}
									},
									{
										 "tableRow": {
											"caller": "FlexibleReceiver.executeOperation(uint256,uint256,address)",
											"callee": "[?].approve(address, uint256)",
											"summmary": "DISPATCHER(optimistic = true)",
											"comments":[
												{
													"alternative callees": "[Asset | DummyERC20A | DummyERC20B | DummyERC20Impl | DummyWeth | ERC20Basic | FTT | PoolHarness | SushiToken | USDC | USDT]"
												},
												{
													"callee resolution": "callee contract unresolved; callee sighash resolved"
												},
												{
													"callee resolution hint (1)": "To resolve the call, try '--link FlexibleReceiver:token=[Asset | DummyERC20A | DummyERC20B | DummyERC20Impl | DummyWeth | ERC20Basic | FTT | PoolHarness | SushiToken | USDC | USDT]'"
												},
												{
													"summary application reason": "declared at erc20.spec:20:66 to apply only to calls without available callee implementation"
												}
											]
										}
									},
									{
										 "tableRow": {
											"caller": "FlexibleReceiver.executeOperation(uint256,uint256,address)",
											"callee": "[?].transfer(address, uint256)",
											"summmary": "DISPATCHER(optimistic = true)",
											"comments":[
												{
													"alternative callees": "[Asset | DummyERC20A | DummyERC20B | DummyERC20Impl | DummyWeth | ERC20Basic | FTT | PoolHarness | SushiToken | USDC | USDT]"
												},
												{
													"callee resolution": "callee contract unresolved; callee sighash resolved"
												},
												{
													"callee resolution hint (1)": "To resolve the call, try '--link FlexibleReceiver:token=[Asset | DummyERC20A | DummyERC20B | DummyERC20Impl | DummyWeth | ERC20Basic | FTT | PoolHarness | SushiToken | USDC | USDT]'"
												},
												{
													"summary application reason": "declared at erc20.spec:21:66 to apply only to calls without available callee implementation"
												}
											]
										}
									},
									{
										 "tableRow": {
											"caller": "FlexibleReceiver.executeOperation(uint256,uint256,address)",
											"callee": "[?].withdraw(uint256)",
											"summmary": "DISPATCHER(optimistic = true)",
											"comments":[
												{
													"alternative callees": "[DummyWeth | PoolHarness]"
												},
												{
													"callee resolution": "callee contract unresolved; callee sighash resolved"
												},
												{
													"callee resolution hint (1)": "To resolve the call, try '--link FlexibleReceiver:token=[DummyWeth | PoolHarness]'"
												},
												{
													"summary application reason": "declared at pool.spec:12:46 to apply only to calls without available callee implementation"
												}
											]
										}
									},
									{
										 "tableRow": {
											"caller": "FlexibleReceiver.executeOperation(uint256,uint256,address)",
											"callee": "[?].transferFrom(address, address, uint256)",
											"summmary": "DISPATCHER(optimistic = true)",
											"comments":[
												{
													"alternative callees": "[Asset | DummyERC20A | DummyERC20B | DummyERC20Impl | DummyWeth | ERC20Basic | FTT | PoolHarness | SushiToken | USDC | USDT]"
												},
												{
													"callee resolution": "callee contract unresolved; callee sighash resolved"
												},
												{
													"callee resolution hint (1)": "To resolve the call, try '--link FlexibleReceiver:token=[Asset | DummyERC20A | DummyERC20B | DummyERC20Impl | DummyWeth | ERC20Basic | FTT | PoolHarness | SushiToken | USDC | USDT]'"
												},
												{
													"summary application reason": "declared at erc20.spec:22:66 to apply only to calls without available callee implementation"
												}
											]
										}
									},
									{
										 "tableRow": {
											"caller": "FlexibleReceiver.executeOperation(uint256,uint256,address)",
											"callee": "[?].deposit(uint256)",
											"summmary": "DISPATCHER(optimistic = true)",
											"comments":[
												{
													"alternative callees": "[PoolHarness]"
												},
												{
													"callee resolution": "callee contract unresolved; callee sighash resolved"
												},
												{
													"callee resolution hint (1)": "To resolve the call, try '--link FlexibleReceiver:token=[PoolHarness]'"
												},
												{
													"summary application reason": "declared at pool.spec:11:46 to apply only to calls without available callee implementation"
												}
											]
										}
									},
									{
										 "tableRow": {
											"caller": "TransferReceiver.executeOperation(uint256,uint256,address)",
											"callee": "[?].transferFrom(address, address, uint256)",
											"summmary": "DISPATCHER(optimistic = true)",
											"comments":[
												{
													"alternative callees": "[Asset | DummyERC20A | DummyERC20B | DummyERC20Impl | DummyWeth | ERC20Basic | FTT | PoolHarness | SushiToken | USDC | USDT]"
												},
												{
													"callee resolution": "callee contract unresolved; callee sighash resolved"
												},
												{
													"callee resolution hint (1)": "To resolve the call, try '--link TransferReceiver:underlying=[Asset | DummyERC20A | DummyERC20B | DummyERC20Impl | DummyWeth | ERC20Basic | FTT | PoolHarness | SushiToken | USDC | USDT]'"
												},
												{
													"summary application reason": "declared at erc20.spec:22:66 to apply only to calls without available callee implementation"
												}
											]
										}
									},
									{
										 "tableRow": {
											"caller": "PoolHarness.flashLoan(address,uint256)",
											"callee": "[?].transferFrom(address, address, uint256)",
											"summmary": "DISPATCHER(optimistic = true)",
											"comments":[
												{
													"alternative callees": "[Asset | DummyERC20A | DummyERC20B | DummyERC20Impl | DummyWeth | ERC20Basic | FTT | PoolHarness | SushiToken | USDC | USDT]"
												},
												{
													"callee resolution": "callee contract unresolved; callee sighash resolved"
												},
												{
													"callee resolution hint (1)": "To resolve the call, try '--link PoolHarness:asset=[Asset | DummyERC20A | DummyERC20B | DummyERC20Impl | DummyWeth | ERC20Basic | FTT | PoolHarness | SushiToken | USDC | USDT]'"
												},
												{
													"summary application reason": "declared at erc20.spec:22:66 to apply only to calls without available callee implementation"
												}
											]
										}
									}
								]
							},
							 "callResolutionWarningsTable": {
								"tableHeader":[
									"Caller",
									"Callee",
									"Summary"
								],
								"callResolutionWarnings":[

								]
							}
						}
,						{
							 "tableRow": {
								"funcName": "transfer(address,uint256)",
								"result": "SUCCESS",
								"time": "16",
								"graph_link": "",
								"preoptimized_link": "PreoptimizedRule-noAllowance_preserve-transferLPADRCU256RP.html",
								"presimplified_link": "PresimplifiedRule-noAllowance_preserve-transferLPADRCU256RP.html",
								"prelastopt_link": "PrelastoptRule-noAllowance_preserve-transferLPADRCU256RP.html",
								"presolver_link": "PresolverRule-noAllowance_preserve-transferLPADRCU256RP.html"
							},
							 "callResolutionTable": {
								"tableHeader":[
									"Caller",
									"Callee",
									"Summary"
								],
								"callResolution":[
									{
										 "tableRow": {
											"caller": "PoolHarness.underlyingAllowance(address)",
											"callee": "[?].allowance(address, address)",
											"summmary": "DISPATCHER(optimistic = true)",
											"comments":[
												{
													"alternative callees": "[Asset | DummyERC20A | DummyERC20B | DummyERC20Impl | DummyWeth | ERC20Basic | FTT | PoolHarness | SushiToken | USDC | USDT]"
												},
												{
													"callee resolution": "callee contract unresolved; callee sighash resolved"
												},
												{
													"callee resolution hint (1)": "To resolve the call, try '--link PoolHarness:asset=[Asset | DummyERC20A | DummyERC20B | DummyERC20Impl | DummyWeth | ERC20Basic | FTT | PoolHarness | SushiToken | USDC | USDT]'"
												},
												{
													"summary application reason": "declared at erc20.spec:19:66 to apply only to calls without available callee implementation"
												}
											]
										}
									}
								]
							},
							 "callResolutionWarningsTable": {
								"tableHeader":[
									"Caller",
									"Callee",
									"Summary"
								],
								"callResolutionWarnings":[

								]
							}
						}
,						{
							 "tableRow": {
								"funcName": "transferFrom(address,address,uint256)",
								"result": "SUCCESS",
								"time": "7",
								"graph_link": "",
								"preoptimized_link": "PreoptimizedRule-noAllowance_preserve-transferFromLPADRCADRCU256RP.html",
								"presimplified_link": "PresimplifiedRule-noAllowance_preserve-transferFromLPADRCADRCU256RP.html",
								"prelastopt_link": "PrelastoptRule-noAllowance_preserve-transferFromLPADRCADRCU256RP.html",
								"presolver_link": "PresolverRule-noAllowance_preserve-transferFromLPADRCADRCU256RP.html"
							},
							 "callResolutionTable": {
								"tableHeader":[
									"Caller",
									"Callee",
									"Summary"
								],
								"callResolution":[
									{
										 "tableRow": {
											"caller": "PoolHarness.underlyingAllowance(address)",
											"callee": "[?].allowance(address, address)",
											"summmary": "DISPATCHER(optimistic = true)",
											"comments":[
												{
													"alternative callees": "[Asset | DummyERC20A | DummyERC20B | DummyERC20Impl | DummyWeth | ERC20Basic | FTT | PoolHarness | SushiToken | USDC | USDT]"
												},
												{
													"callee resolution": "callee contract unresolved; callee sighash resolved"
												},
												{
													"callee resolution hint (1)": "To resolve the call, try '--link PoolHarness:asset=[Asset | DummyERC20A | DummyERC20B | DummyERC20Impl | DummyWeth | ERC20Basic | FTT | PoolHarness | SushiToken | USDC | USDT]'"
												},
												{
													"summary application reason": "declared at erc20.spec:19:66 to apply only to calls without available callee implementation"
												}
											]
										}
									}
								]
							},
							 "callResolutionWarningsTable": {
								"tableHeader":[
									"Caller",
									"Callee",
									"Summary"
								],
								"callResolutionWarnings":[

								]
							}
						}
,						{
							 "tableRow": {
								"funcName": "underlyingAllowance(address)",
								"result": "SUCCESS",
								"time": "18",
								"graph_link": "",
								"preoptimized_link": "PreoptimizedRule-noAllowance_preserve-underlyingAllowanceLPADRRP.html",
								"presimplified_link": "PresimplifiedRule-noAllowance_preserve-underlyingAllowanceLPADRRP.html",
								"prelastopt_link": "PrelastoptRule-noAllowance_preserve-underlyingAllowanceLPADRRP.html",
								"presolver_link": "PresolverRule-noAllowance_preserve-underlyingAllowanceLPADRRP.html"
							},
							 "callResolutionTable": {
								"tableHeader":[
									"Caller",
									"Callee",
									"Summary"
								],
								"callResolution":[
									{
										 "tableRow": {
											"caller": "PoolHarness.underlyingAllowance(address)",
											"callee": "[?].allowance(address, address)",
											"summmary": "DISPATCHER(optimistic = true)",
											"comments":[
												{
													"alternative callees": "[Asset | DummyERC20A | DummyERC20B | DummyERC20Impl | DummyWeth | ERC20Basic | FTT | PoolHarness | SushiToken | USDC | USDT]"
												},
												{
													"callee resolution": "callee contract unresolved; callee sighash resolved"
												},
												{
													"callee resolution hint (1)": "To resolve the call, try '--link PoolHarness:asset=[Asset | DummyERC20A | DummyERC20B | DummyERC20Impl | DummyWeth | ERC20Basic | FTT | PoolHarness | SushiToken | USDC | USDT]'"
												},
												{
													"summary application reason": "declared at erc20.spec:19:66 to apply only to calls without available callee implementation"
												}
											]
										}
									}
								]
							},
							 "callResolutionWarningsTable": {
								"tableHeader":[
									"Caller",
									"Callee",
									"Summary"
								],
								"callResolutionWarnings":[

								]
							}
						}
,						{
							 "tableRow": {
								"funcName": "underlyingBalance()",
								"result": "SUCCESS",
								"time": "10",
								"graph_link": "",
								"preoptimized_link": "PreoptimizedRule-noAllowance_preserve-underlyingBalanceLPRP.html",
								"presimplified_link": "PresimplifiedRule-noAllowance_preserve-underlyingBalanceLPRP.html",
								"prelastopt_link": "PrelastoptRule-noAllowance_preserve-underlyingBalanceLPRP.html",
								"presolver_link": "PresolverRule-noAllowance_preserve-underlyingBalanceLPRP.html"
							},
							 "callResolutionTable": {
								"tableHeader":[
									"Caller",
									"Callee",
									"Summary"
								],
								"callResolution":[
									{
										 "tableRow": {
											"caller": "PoolHarness.underlyingAllowance(address)",
											"callee": "[?].allowance(address, address)",
											"summmary": "DISPATCHER(optimistic = true)",
											"comments":[
												{
													"alternative callees": "[Asset | DummyERC20A | DummyERC20B | DummyERC20Impl | DummyWeth | ERC20Basic | FTT | PoolHarness | SushiToken | USDC | USDT]"
												},
												{
													"callee resolution": "callee contract unresolved; callee sighash resolved"
												},
												{
													"callee resolution hint (1)": "To resolve the call, try '--link PoolHarness:asset=[Asset | DummyERC20A | DummyERC20B | DummyERC20Impl | DummyWeth | ERC20Basic | FTT | PoolHarness | SushiToken | USDC | USDT]'"
												},
												{
													"summary application reason": "declared at erc20.spec:19:66 to apply only to calls without available callee implementation"
												}
											]
										}
									},
									{
										 "tableRow": {
											"caller": "PoolHarness.underlyingBalance()",
											"callee": "[?].balanceOf(address)",
											"summmary": "DISPATCHER(optimistic = true)",
											"comments":[
												{
													"alternative callees": "[Asset | DummyERC20A | DummyERC20B | DummyERC20Impl | DummyWeth | ERC20Basic | FTT | PoolHarness | SushiToken | USDC | USDT]"
												},
												{
													"callee resolution": "callee contract unresolved; callee sighash resolved"
												},
												{
													"callee resolution hint (1)": "To resolve the call, try '--link PoolHarness:asset=[Asset | DummyERC20A | DummyERC20B | DummyERC20Impl | DummyWeth | ERC20Basic | FTT | PoolHarness | SushiToken | USDC | USDT]'"
												},
												{
													"summary application reason": "declared at erc20.spec:18:66 to apply only to calls without available callee implementation"
												}
											]
										}
									}
								]
							},
							 "callResolutionWarningsTable": {
								"tableHeader":[
									"Caller",
									"Callee",
									"Summary"
								],
								"callResolutionWarnings":[

								]
							}
						}
,						{
							 "tableRow": {
								"funcName": "withdraw(uint256)",
								"result": "SUCCESS",
								"time": "15",
								"graph_link": "",
								"preoptimized_link": "PreoptimizedRule-noAllowance_preserve-withdrawLPU256RP.html",
								"presimplified_link": "PresimplifiedRule-noAllowance_preserve-withdrawLPU256RP.html",
								"prelastopt_link": "PrelastoptRule-noAllowance_preserve-withdrawLPU256RP.html",
								"presolver_link": "PresolverRule-noAllowance_preserve-withdrawLPU256RP.html"
							},
							 "callResolutionTable": {
								"tableHeader":[
									"Caller",
									"Callee",
									"Summary"
								],
								"callResolution":[
									{
										 "tableRow": {
											"caller": "PoolHarness.underlyingAllowance(address)",
											"callee": "[?].allowance(address, address)",
											"summmary": "DISPATCHER(optimistic = true)",
											"comments":[
												{
													"alternative callees": "[Asset | DummyERC20A | DummyERC20B | DummyERC20Impl | DummyWeth | ERC20Basic | FTT | PoolHarness | SushiToken | USDC | USDT]"
												},
												{
													"callee resolution": "callee contract unresolved; callee sighash resolved"
												},
												{
													"callee resolution hint (1)": "To resolve the call, try '--link PoolHarness:asset=[Asset | DummyERC20A | DummyERC20B | DummyERC20Impl | DummyWeth | ERC20Basic | FTT | PoolHarness | SushiToken | USDC | USDT]'"
												},
												{
													"summary application reason": "declared at erc20.spec:19:66 to apply only to calls without available callee implementation"
												}
											]
										}
									},
									{
										 "tableRow": {
											"caller": "PoolHarness.withdraw(uint256)",
											"callee": "[?].balanceOf(address)",
											"summmary": "DISPATCHER(optimistic = true)",
											"comments":[
												{
													"alternative callees": "[Asset | DummyERC20A | DummyERC20B | DummyERC20Impl | DummyWeth | ERC20Basic | FTT | PoolHarness | SushiToken | USDC | USDT]"
												},
												{
													"callee resolution": "callee contract unresolved; callee sighash resolved"
												},
												{
													"callee resolution hint (1)": "To resolve the call, try '--link PoolHarness:asset=[Asset | DummyERC20A | DummyERC20B | DummyERC20Impl | DummyWeth | ERC20Basic | FTT | PoolHarness | SushiToken | USDC | USDT]'"
												},
												{
													"summary application reason": "declared at erc20.spec:18:66 to apply only to calls without available callee implementation"
												}
											]
										}
									},
									{
										 "tableRow": {
											"caller": "PoolHarness.withdraw(uint256)",
											"callee": "[?].balanceOf(address)",
											"summmary": "DISPATCHER(optimistic = true)",
											"comments":[
												{
													"alternative callees": "[Asset | DummyERC20A | DummyERC20B | DummyERC20Impl | DummyWeth | ERC20Basic | FTT | PoolHarness | SushiToken | USDC | USDT]"
												},
												{
													"callee resolution": "callee contract unresolved; callee sighash resolved"
												},
												{
													"callee resolution hint (1)": "To resolve the call, try '--link PoolHarness:asset=[Asset | DummyERC20A | DummyERC20B | DummyERC20Impl | DummyWeth | ERC20Basic | FTT | PoolHarness | SushiToken | USDC | USDT]'"
												},
												{
													"summary application reason": "declared at erc20.spec:18:66 to apply only to calls without available callee implementation"
												}
											]
										}
									},
									{
										 "tableRow": {
											"caller": "PoolHarness.withdraw(uint256)",
											"callee": "[?].transferFrom(address, address, uint256)",
											"summmary": "DISPATCHER(optimistic = true)",
											"comments":[
												{
													"alternative callees": "[Asset | DummyERC20A | DummyERC20B | DummyERC20Impl | DummyWeth | ERC20Basic | FTT | PoolHarness | SushiToken | USDC | USDT]"
												},
												{
													"callee resolution": "callee contract unresolved; callee sighash resolved"
												},
												{
													"callee resolution hint (1)": "To resolve the call, try '--link PoolHarness:asset=[Asset | DummyERC20A | DummyERC20B | DummyERC20Impl | DummyWeth | ERC20Basic | FTT | PoolHarness | SushiToken | USDC | USDT]'"
												},
												{
													"summary application reason": "declared at erc20.spec:22:66 to apply only to calls without available callee implementation"
												}
											]
										}
									}
								]
							},
							 "callResolutionWarningsTable": {
								"tableHeader":[
									"Caller",
									"Callee",
									"Summary"
								],
								"callResolutionWarnings":[

								]
							}
						}
					]

				},
		{
			"ruleName": "noAllowance",
			"tableBody":[
				{
					 "tableRow": {
						"funcName": "noAllowance_skipped_preserve_allowance(address,address)",
						"result": "SKIPPED",
						"time": "?",
						"graph_link": "",
						"preoptimized_link": "",
						"presimplified_link": "",
						"prelastopt_link": "",
						"presolver_link": ""
					}
				}
,				{
					 "tableRow": {
						"funcName": "noAllowance_skipped_preserve_amountToShares(uint256)",
						"result": "SKIPPED",
						"time": "?",
						"graph_link": "",
						"preoptimized_link": "",
						"presimplified_link": "",
						"prelastopt_link": "",
						"presolver_link": ""
					}
				}
,				{
					 "tableRow": {
						"funcName": "noAllowance_skipped_preserve_asset()",
						"result": "SKIPPED",
						"time": "?",
						"graph_link": "",
						"preoptimized_link": "",
						"presimplified_link": "",
						"prelastopt_link": "",
						"presolver_link": ""
					}
				}
,				{
					 "tableRow": {
						"funcName": "noAllowance_skipped_preserve_assetBalance()",
						"result": "SKIPPED",
						"time": "?",
						"graph_link": "",
						"preoptimized_link": "",
						"presimplified_link": "",
						"prelastopt_link": "",
						"presolver_link": ""
					}
				}
,				{
					 "tableRow": {
						"funcName": "noAllowance_skipped_preserve_balanceOf(address)",
						"result": "SKIPPED",
						"time": "?",
						"graph_link": "",
						"preoptimized_link": "",
						"presimplified_link": "",
						"prelastopt_link": "",
						"presolver_link": ""
					}
				}
,				{
					 "tableRow": {
						"funcName": "noAllowance_skipped_preserve_calcPremium(uint256)",
						"result": "SKIPPED",
						"time": "?",
						"graph_link": "",
						"preoptimized_link": "",
						"presimplified_link": "",
						"prelastopt_link": "",
						"presolver_link": ""
					}
				}
,				{
					 "tableRow": {
						"funcName": "noAllowance_skipped_preserve_feeRate()",
						"result": "SKIPPED",
						"time": "?",
						"graph_link": "",
						"preoptimized_link": "",
						"presimplified_link": "",
						"prelastopt_link": "",
						"presolver_link": ""
					}
				}
,				{
					 "tableRow": {
						"funcName": "noAllowance_skipped_preserve_sharesToAmount(uint256)",
						"result": "SKIPPED",
						"time": "?",
						"graph_link": "",
						"preoptimized_link": "",
						"presimplified_link": "",
						"prelastopt_link": "",
						"presolver_link": ""
					}
				}
,				{
					 "tableRow": {
						"funcName": "noAllowance_skipped_preserve_totalSupply()",
						"result": "SKIPPED",
						"time": "?",
						"graph_link": "",
						"preoptimized_link": "",
						"presimplified_link": "",
						"prelastopt_link": "",
						"presolver_link": ""
					}
				}
,				{
					 "tableRow": {
						"funcName": "noAllowance_instate",
						"result": "SUCCESS",
						"time": "16",
						"graph_link": "",
						"preoptimized_link": "PreoptimizedRule-noAllowance_instate.html",
						"presimplified_link": "PresimplifiedRule-noAllowance_instate.html",
						"prelastopt_link": "PrelastoptRule-noAllowance_instate.html",
						"presolver_link": "PresolverRule-noAllowance_instate.html"
					},
					 "callResolutionTable": {
						"tableHeader":[
							"Caller",
							"Callee",
							"Summary"
						],
						"callResolution":[
							{
								 "tableRow": {
									"caller": "PoolHarness.underlyingAllowance(address)",
									"callee": "[?].allowance(address, address)",
									"summmary": "DISPATCHER(optimistic = true)",
									"comments":[
										{
											"alternative callees": "[Asset | DummyERC20A | DummyERC20B | DummyERC20Impl | DummyWeth | ERC20Basic | FTT | PoolHarness | SushiToken | USDC | USDT]"
										},
										{
											"callee resolution": "callee contract unresolved; callee sighash resolved"
										},
										{
											"callee resolution hint (1)": "To resolve the call, try '--link PoolHarness:asset=[Asset | DummyERC20A | DummyERC20B | DummyERC20Impl | DummyWeth | ERC20Basic | FTT | PoolHarness | SushiToken | USDC | USDT]'"
										},
										{
											"summary application reason": "declared at erc20.spec:19:66 to apply only to calls without available callee implementation"
										}
									]
								}
							}
						]
					},
					 "callResolutionWarningsTable": {
						"tableHeader":[
							"Caller",
							"Callee",
							"Summary"
						],
						"callResolutionWarnings":[

						]
					}
				}
,				{
					 "tableRow": {
						"funcName": "noAllowance_preserve",
						"result": "SUCCESS",
						"time": "182",
						"graph_link": "",
						"preoptimized_link": "",
						"presimplified_link": "",
						"prelastopt_link": "",
						"presolver_link": ""
					},
					"isMultiAssert": true
				}
			]

		}
			]

		},
		 "assert_tables": {
			"tableHeader":[
				"Assertions",
				"Result",
				"Time(secs)",
				"Dump"
			],
			"functionResults":[

			]

		},
		 "availableContractsTable": {
			"sectionName": "Available contracts",
			"tableHeader":[
				"Name",
				"Address",
				"Pre-state",
				"Methods"
			],
			"contractResult":[
				{
					 "tableRow": {
						"name": "Asset",
						"address": "ce4604a0000000000000000000000085",
						"pre_state": "{}",
						"methodsNames":[
							"transferFrom(address,address,uint256)",
							"balanceOf(address)",
							"approve(address,uint256)",
							"transfer(address,uint256)",
							"totalSupply()",
							"allowance(address,address)"
						]
					}
				},
				{
					 "tableRow": {
						"name": "DummyERC20A",
						"address": "ce4604a0000000000000000000000020",
						"pre_state": "{}",
						"methodsNames":[
							"myAddress()",
							"symbol()",
							"name()",
							"decimals()",
							"transferFrom(address,address,uint256)",
							"balanceOf(address)",
							"approve(address,uint256)",
							"transfer(address,uint256)",
							"totalSupply()",
							"allowance(address,address)"
						]
					}
				},
				{
					 "tableRow": {
						"name": "DummyERC20B",
						"address": "ce4604a0000000000000000000000024",
						"pre_state": "{}",
						"methodsNames":[
							"myAddress()",
							"symbol()",
							"name()",
							"decimals()",
							"transferFrom(address,address,uint256)",
							"balanceOf(address)",
							"approve(address,uint256)",
							"transfer(address,uint256)",
							"totalSupply()",
							"allowance(address,address)"
						]
					}
				},
				{
					 "tableRow": {
						"name": "DummyERC20Impl",
						"address": "ce4604a0000000000000000000000027",
						"pre_state": "{}",
						"methodsNames":[
							"myAddress()",
							"symbol()",
							"name()",
							"decimals()",
							"transferFrom(address,address,uint256)",
							"balanceOf(address)",
							"approve(address,uint256)",
							"transfer(address,uint256)",
							"totalSupply()",
							"allowance(address,address)"
						]
					}
				},
				{
					 "tableRow": {
						"name": "DummyWeth",
						"address": "ce4604a0000000000000000000000029",
						"pre_state": "{}",
						"methodsNames":[
							"myAddress()",
							"symbol()",
							"name()",
							"decimals()",
							"transferFrom(address,address,uint256)",
							"withdraw(uint256)",
							"deposit()",
							"balanceOf(address)",
							"approve(address,uint256)",
							"transfer(address,uint256)",
							"totalSupply()",
							"allowance(address,address)"
						]
					}
				},
				{
					 "tableRow": {
						"name": "ERC20Basic",
						"address": "ce4604a000000000000000000000002c",
						"pre_state": "{}",
						"methodsNames":[
							"constructor()",
							"symbol()",
							"name()",
							"decimals()",
							"transferFrom(address,address,uint256)",
							"balanceOf(address)",
							"approve(address,uint256)",
							"transfer(address,uint256)",
							"totalSupply()",
							"allowance(address,address)"
						]
					}
				},
				{
					 "tableRow": {
						"name": "FTT",
						"address": "ce4604a0000000000000000000000037",
						"pre_state": "{}",
						"methodsNames":[
							"constructor()",
							"symbol()",
							"name()",
							"decimals()",
							"transferFrom(address,address,uint256)",
							"burn(uint256)",
							"burnFrom(address,uint256)",
							"balanceOf(address)",
							"increaseAllowance(address,uint256)",
							"approve(address,uint256)",
							"decreaseAllowance(address,uint256)",
							"transfer(address,uint256)",
							"totalSupply()",
							"allowance(address,address)"
						]
					}
				},
				{
					 "tableRow": {
						"name": "FlexibleReceiver",
						"address": "ce4604a0000000000000000000000005",
						"pre_state": "{}",
						"methodsNames":[
							"executeOperation(uint256,uint256,address)"
						]
					}
				},
				{
					 "tableRow": {
						"name": "PoolHarness",
						"address": "ce4604a000000000000000000000000f",
						"pre_state": "{}",
						"methodsNames":[
							"deposit(uint256)",
							"calcPremium(uint256)",
							"transferFrom(address,address,uint256)",
							"withdraw(uint256)",
							"amountToShares(uint256)",
							"asset()",
							"transfer(address,uint256)",
							"underlyingAllowance(address)",
							"balanceOf(address)",
							"approve(address,uint256)",
							"assetBalance()",
							"feeRate()",
							"sharesToAmount(uint256)",
							"underlyingBalance()",
							"totalSupply()",
							"allowance(address,address)",
							"flashLoan(address,uint256)"
						]
					}
				},
				{
					 "tableRow": {
						"name": "SushiToken",
						"address": "ce4604a0000000000000000000000047",
						"pre_state": "{}",
						"methodsNames":[
							"nonces(address)",
							"constructor(string,string)",
							"constructor()",
							"name()",
							"transferOwnership(address)",
							"mint(address,uint256)",
							"delegates(address)",
							"delegateBySig(address,uint256,uint256,uint8,bytes32,bytes32)",
							"renounceOwnership()",
							"balanceOf(address)",
							"approve(address,uint256)",
							"transfer(address,uint256)",
							"allowance(address,address)",
							"symbol()",
							"numCheckpoints(address)",
							"increaseAllowance(address,uint256)",
							"getCurrentVotes(address)",
							"checkpoints(address,uint32)",
							"decreaseAllowance(address,uint256)",
							"owner()",
							"DELEGATION_TYPEHASH()",
							"delegate(address)",
							"totalSupply()",
							"transferFrom(address,address,uint256)",
							"getPriorVotes(address,uint256)",
							"decimals()",
							"DOMAIN_TYPEHASH()"
						]
					}
				},
				{
					 "tableRow": {
						"name": "TransferReceiver",
						"address": "ce4604a0000000000000000000000017",
						"pre_state": "{}",
						"methodsNames":[
							"executeOperation(uint256,uint256,address)"
						]
					}
				},
				{
					 "tableRow": {
						"name": "TrivialReceiver",
						"address": "ce4604a000000000000000000000001c",
						"pre_state": "{}",
						"methodsNames":[
							"executeOperation(uint256,uint256,address)"
						]
					}
				},
				{
					 "tableRow": {
						"name": "USDC",
						"address": "ce4604a000000000000000000000006d",
						"pre_state": "{}",
						"methodsNames":[
							"nonces(address)",
							"constructor()",
							"authorizationState(address,bytes32)",
							"name()",
							"rescuer()",
							"CANCEL_AUTHORIZATION_TYPEHASH()",
							"isBlacklisted(address)",
							"initializeV2_1(address)",
							"transferOwnership(address)",
							"rescueERC20(Contract IERC20,address,uint256)",
							"transferWithAuthorization(address,address,uint256,uint256,uint256,bytes32,uint8,bytes32,bytes32)",
							"currency()",
							"DOMAIN_SEPARATOR()",
							"mint(address,uint256)",
							"isMinter(address)",
							"PERMIT_TYPEHASH()",
							"updateBlacklister(address)",
							"initialize(string,string,string,uint8,address,address,address,address)",
							"blacklister()",
							"balanceOf(address)",
							"approve(address,uint256)",
							"masterMinter()",
							"unpause()",
							"transfer(address,uint256)",
							"updatePauser(address)",
							"paused()",
							"allowance(address,address)",
							"symbol()",
							"RECEIVE_WITH_AUTHORIZATION_TYPEHASH()",
							"minterAllowance(address)",
							"updateRescuer(address)",
							"receiveWithAuthorization(address,address,uint256,uint256,uint256,bytes32,uint8,bytes32,bytes32)",
							"permit(address,address,uint256,uint256,uint8,bytes32,bytes32)",
							"version()",
							"increaseAllowance(address,uint256)",
							"removeMinter(address)",
							"configureMinter(address,uint256)",
							"decreaseAllowance(address,uint256)",
							"pause()",
							"owner()",
							"totalSupply()",
							"transferFrom(address,address,uint256)",
							"balances(address)",
							"initializeV2(string)",
							"updateMasterMinter(address)",
							"blacklist(address)",
							"decimals()",
							"TRANSFER_WITH_AUTHORIZATION_TYPEHASH()",
							"burn(uint256)",
							"unBlacklist(address)",
							"pauser()",
							"cancelAuthorization(address,bytes32,uint8,bytes32,bytes32)"
						]
					}
				},
				{
					 "tableRow": {
						"name": "USDT",
						"address": "ce4604a0000000000000000000000080",
						"pre_state": "{}",
						"methodsNames":[
							"constructor(uint256,string,string,uint256)",
							"constructor()",
							"name()",
							"transferOwnership(address)",
							"deprecate(address)",
							"maximumFee()",
							"deprecated()",
							"MAX_UINT()",
							"destroyBlackFunds(address)",
							"balanceOf(address)",
							"approve(address,uint256)",
							"unpause()",
							"paused()",
							"transfer(address,uint256)",
							"allowance(address,address)",
							"upgradedAddress()",
							"getBlackListStatus(address)",
							"symbol()",
							"addBlackList(address)",
							"removeBlackList(address)",
							"pause()",
							"owner()",
							"totalSupply()",
							"transferFrom(address,address,uint256)",
							"isBlackListed(address)",
							"balances(address)",
							"allowed(address,address)",
							"issue(uint256)",
							"decimals()",
							"getOwner()",
							"_totalSupply()",
							"basisPointsRate()",
							"redeem(uint256)",
							"setParams(uint256,uint256)"
						]
					}
				}
			]
		}
	}