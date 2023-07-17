data = {
	"contractName": "curve",
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
						"ruleName": "no_read_only_reentrancy",
						"result": "FAIL",
						"time": "504",
						"graph_link": "",
						"preoptimized_link": "",
						"presimplified_link": "",
						"prelastopt_link": "",
						"presolver_link": ""
					},
					"isMultiRule": true
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
			"ruleName": "no_read_only_reentrancy",
			"tableBody":[
				{
					 "tableRow": {
						"funcName": "remove_liquidity(uint256,uint256[2])",
						"result": "FAIL",
						"time": "485",
						"graph_link": "Report-no_read_only_reentrancy-remove_liquidityLPU256CU256LB2RBRP-example1.html",
						"preoptimized_link": "PreoptimizedRule-no_read_only_reentrancy-remove_liquidityLPU256CU256LB2RBRP.html",
						"presimplified_link": "PresimplifiedRule-no_read_only_reentrancy-remove_liquidityLPU256CU256LB2RBRP.html",
						"prelastopt_link": "PrelastoptRule-no_read_only_reentrancy-remove_liquidityLPU256CU256LB2RBRP.html",
						"presolver_link": "PresolverRule-no_read_only_reentrancy-remove_liquidityLPU256CU256LB2RBRP.html"
					},
					 "variables": {
						"data": "bytemap initialized but unknown",
						"e.msg.sender": "ERC20 (0x270e)",
						"e.msg.value": "0",
						"e.tx.origin": "0x401",
						"e.block.coinbase": "0x404",
						"e.block.difficulty": "0",
						"e.block.gaslimit": "0",
						"e.block.number": "0",
						"e.block.timestamp": "0",
						"e_external.msg.sender": "identity (0xffff)",
						"e_external.msg.value": "0",
						"e_external.tx.origin": "0x402",
						"e_external.block.coinbase": "0x403",
						"e_external.block.difficulty": "0",
						"e_external.block.gaslimit": "0",
						"e_external.block.number": "0",
						"e_external.block.timestamp": "0",
						"f.selector": "0x5b36389c",
						"f.isPure": "false",
						"f.isView": "false",
						"f.isPayable": "false",
						"f.numberOfArguments": "2",
						"f.isFallback": "false",
						"CurveTokenExample": "CurveTokenExample (0x270d)",
						"ERC20": "ERC20 (0x270e)",
						"identity": "identity (0xffff)"
					},
					"assertMessage":[

					],
					 "failureCauses": {
						"expr": "!(B61&&(((safe_math_narrow:bif(safe_math_promotion:bif(safe_math_narrow:bif(safe_math_promotion:bif(tacCalldatabuf!!1151@11[0x4])+int safe_math_promotion:bif(tacCalldatabuf!!1151@11[0x24])))*int 0x8ac7230489e80000)/(CANON124!!19-tacCalldatabuf@5[0x4]))==I62)||((safe_math_narrow:bif(safe_math_promotion:bif(safe_math_narrow:bif(safe_math_promotion:bif(tacCalldatabuf!!1151@11[0x4])+int safe_math_promotion:bif(tacCalldatabuf!!1151@11[0x24])))*int 0x8ac7230489e80000)/(CANON124!!19-tacCalldatabuf@5[0x4]))==I37)))"
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
							{
								 "tableRow": {
									"caller": "curve.remove_liquidity(uint256,uint256[2])",
									"callee": "[?].[?]",
									"summmary": "Optimistic Fallback DISPATCHER",
									"comments":[
										{
											"alternative explicit fallbacks": "There are no contracts with custom fallback() function implementation"
										},
										{
											"callee resolution": "both callee contract and sighash are unresolved"
										},
										{
											"summary application reason": "summarized as instructed by command-line flag -optimisticFallback"
										}
									]
								}
							}
						]
					},
					 "callTrace": {
						"funcName": "no_read_only_reentrancy(f=remove_liquidity(uint256,uint256[2]))",
						"returnValue": "",
						"status": "",
						"childrenList":[
							{
								"funcName": "Storage State",
								"returnValue": "",
								"status": "",
								"childrenList":[
									{
										"funcName": "ERC20",
										"returnValue": "",
										"status": "",
										"childrenList":[
											{
												"funcName": "_balances[ERC20 (0x270e)]: 10",
												"returnValue": "",
												"status": "HAVOC",
												"childrenList":[]
,
												"changed": "false"
											},
											{
												"funcName": "_balances[identity (0xffff)]: 0xcd98cb94f23b4265",
												"returnValue": "",
												"status": "HAVOC",
												"childrenList":[]
,
												"changed": "false"
											}
										],
										"storageId": "null"
									},
									{
										"funcName": "CurveTokenExample",
										"returnValue": "",
										"status": "",
										"childrenList":[
											{
												"funcName": "_balances[ERC20 (0x270e)]: 0x802c23c97dc928ced4c55c9cd9397b4",
												"returnValue": "",
												"status": "HAVOC",
												"childrenList":[]
,
												"changed": "false"
											},
											{
												"funcName": "_totalSupply: 0x802c23c97dc928d32afe74c128797b4",
												"returnValue": "",
												"status": "HAVOC",
												"childrenList":[]
,
												"changed": "false"
											}
										],
										"storageId": "null"
									},
									{
										"funcName": "curve",
										"returnValue": "",
										"status": "",
										"childrenList":[
											{
												"funcName": "_status: 0",
												"returnValue": "",
												"status": "HAVOC",
												"childrenList":[]
,
												"changed": "false"
											},
											{
												"funcName": "admin_balances[0]: 0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffd",
												"returnValue": "",
												"status": "HAVOC",
												"childrenList":[]
,
												"changed": "false"
											},
											{
												"funcName": "admin_balances[1]: 3",
												"returnValue": "",
												"status": "HAVOC",
												"childrenList":[]
,
												"changed": "false"
											},
											{
												"funcName": "coins_1: ERC20 (0x270e)",
												"returnValue": "",
												"status": "HAVOC",
												"childrenList":[]
,
												"changed": "false"
											},
											{
												"funcName": "future_A: 0",
												"returnValue": "",
												"status": "HAVOC",
												"childrenList":[]
,
												"changed": "false"
											},
											{
												"funcName": "lp_token: CurveTokenExample (0x270d)",
												"returnValue": "",
												"status": "HAVOC",
												"childrenList":[]
,
												"changed": "false"
											},
											{
												"funcName": "solghost_return_func1: *",
												"returnValue": "",
												"status": "DONT CARE",
												"childrenList":[]
,
												"changed": "false"
											},
											{
												"funcName": "solghost_trigger_check: *",
												"returnValue": "",
												"status": "DONT CARE",
												"childrenList":[]
,
												"changed": "false"
											}
										],
										"storageId": "null"
									}
								],
								"storageId": "1"
							},
							{
								"funcName": "Setup",
								"returnValue": "",
								"status": "",
								"childrenList":[
									{
										"funcName": "multi contract setup",
										"returnValue": "",
										"status": "",
										"childrenList":[]

									},
									{
										"funcName": "rule parameters setup",
										"returnValue": "",
										"status": "",
										"childrenList":[]

									},
									{
										"funcName": "contract address vars initialized",
										"returnValue": "",
										"status": "",
										"childrenList":[]

									},
									{
										"funcName": "setup read tracking instrumentation",
										"returnValue": "",
										"status": "",
										"childrenList":[]

									},
									{
										"funcName": "last storage initialize",
										"returnValue": "",
										"status": "",
										"childrenList":[]

									},
									{
										"funcName": "assumptions about extcodesize",
										"returnValue": "",
										"status": "",
										"childrenList":[]

									},
									{
										"funcName": "assumptions about contracts' addresses",
										"returnValue": "",
										"status": "",
										"childrenList":[]

									},
									{
										"funcName": "assumptions about starting balances",
										"returnValue": "",
										"status": "",
										"childrenList":[]

									},
									{
										"funcName": "assumptions about static addresses",
										"returnValue": "",
										"status": "",
										"childrenList":[]

									},
									{
										"funcName": "assumptions about uniqueness of contracts' addressses",
										"returnValue": "",
										"status": "",
										"childrenList":[]

									},
									{
										"funcName": "record starting nonces",
										"returnValue": "",
										"status": "",
										"childrenList":[]

									},
									{
										"funcName": "cloned contracts have no balances",
										"returnValue": "",
										"status": "",
										"childrenList":[]

									},
									{
										"funcName": "Linked immutable setup",
										"returnValue": "",
										"status": "",
										"childrenList":[]

									}
								]
							},
							{
								"funcName": "require cond",
								"returnValue": "",
								"status": "",
								"childrenList":[]

							},
							{
								"funcName": "require before_func1 == curve.getVirtualPrice(e_external)",
								"returnValue": "",
								"status": "",
								"childrenList":[
									{
										"funcName": "curve.getVirtualPrice()",
										"returnValue": "13",
										"status": "SUCCESS",
										"childrenList":[
											{
												"funcName": "sender: identity (0xffff); receiver: identity (0xffff); transferred amount: 0",
												"returnValue": "",
												"status": "TRANSFER",
												"childrenList":[
													{
														"funcName": "Load from sender.balance: 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff (MAX_UINT256)",
														"returnValue": "",
														"status": "",
														"childrenList":[]

													},
													{
														"funcName": "Store at sender.balance: 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff (MAX_UINT256)",
														"returnValue": "",
														"status": "",
														"childrenList":[]

													},
													{
														"funcName": "Load from receiver.balance: 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff (MAX_UINT256)",
														"returnValue": "",
														"status": "",
														"childrenList":[]

													},
													{
														"funcName": "Store at receiver.balance: 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff (MAX_UINT256)",
														"returnValue": "",
														"status": "",
														"childrenList":[]

													}
												]
											},
											{
												"funcName": "(internal) curve.getVirtualPrice()",
												"returnValue": "13",
												"status": "",
												"childrenList":[
													{
														"funcName": "Load from curve.admin_balances[0]: 0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffd",
														"returnValue": "",
														"status": "",
														"childrenList":[]

													},
													{
														"funcName": "Load from curve.admin_balances[1]: 3",
														"returnValue": "",
														"status": "",
														"childrenList":[]

													},
													{
														"funcName": "Load from curve.coins_1: ERC20 (0x270e)",
														"returnValue": "",
														"status": "",
														"childrenList":[]

													},
													{
														"funcName": "ERC20.balanceOf(account=identity (0xffff))",
														"returnValue": "0xcd98cb94f23b4265",
														"status": "SUCCESS",
														"childrenList":[
															{
																"funcName": "(internal) ERC20.balanceOf(account=identity (0xffff))",
																"returnValue": "0xcd98cb94f23b4265",
																"status": "",
																"childrenList":[
																	{
																		"funcName": "Load from ERC20._balances[identity (0xffff)]: 0xcd98cb94f23b4265",
																		"returnValue": "",
																		"status": "",
																		"childrenList":[]

																	},
																	{
																		"funcName": "Storage State",
																		"returnValue": "",
																		"status": "",
																		"childrenList":[
																			{
																				"funcName": "ERC20",
																				"returnValue": "",
																				"status": "",
																				"childrenList":[
																					{
																						"funcName": "_balances[ERC20 (0x270e)]: 10",
																						"returnValue": "",
																						"status": "HAVOC",
																						"childrenList":[]
,
																						"changed": "false"
																					},
																					{
																						"funcName": "_balances[identity (0xffff)]: 0xcd98cb94f23b4265",
																						"returnValue": "",
																						"status": "HAVOC",
																						"childrenList":[]
,
																						"changed": "false"
																					}
																				],
																				"storageId": "null"
																			},
																			{
																				"funcName": "CurveTokenExample",
																				"returnValue": "",
																				"status": "",
																				"childrenList":[
																					{
																						"funcName": "_balances[ERC20 (0x270e)]: 0x802c23c97dc928ced4c55c9cd9397b4",
																						"returnValue": "",
																						"status": "HAVOC",
																						"childrenList":[]
,
																						"changed": "false"
																					},
																					{
																						"funcName": "_totalSupply: 0x802c23c97dc928d32afe74c128797b4",
																						"returnValue": "",
																						"status": "HAVOC",
																						"childrenList":[]
,
																						"changed": "false"
																					}
																				],
																				"storageId": "null"
																			},
																			{
																				"funcName": "curve",
																				"returnValue": "",
																				"status": "",
																				"childrenList":[
																					{
																						"funcName": "_status: 0",
																						"returnValue": "",
																						"status": "HAVOC",
																						"childrenList":[]
,
																						"changed": "false"
																					},
																					{
																						"funcName": "admin_balances[0]: 0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffd",
																						"returnValue": "",
																						"status": "HAVOC",
																						"childrenList":[]
,
																						"changed": "false"
																					},
																					{
																						"funcName": "admin_balances[1]: 3",
																						"returnValue": "",
																						"status": "HAVOC",
																						"childrenList":[]
,
																						"changed": "false"
																					},
																					{
																						"funcName": "coins_1: ERC20 (0x270e)",
																						"returnValue": "",
																						"status": "HAVOC",
																						"childrenList":[]
,
																						"changed": "false"
																					},
																					{
																						"funcName": "future_A: 0",
																						"returnValue": "",
																						"status": "HAVOC",
																						"childrenList":[]
,
																						"changed": "false"
																					},
																					{
																						"funcName": "lp_token: CurveTokenExample (0x270d)",
																						"returnValue": "",
																						"status": "HAVOC",
																						"childrenList":[]
,
																						"changed": "false"
																					},
																					{
																						"funcName": "solghost_return_func1: *",
																						"returnValue": "",
																						"status": "DONT CARE",
																						"childrenList":[]
,
																						"changed": "false"
																					},
																					{
																						"funcName": "solghost_trigger_check: *",
																						"returnValue": "",
																						"status": "DONT CARE",
																						"childrenList":[]
,
																						"changed": "false"
																					}
																				],
																				"storageId": "null"
																			}
																		],
																		"storageId": "2"
																	}
																]
															}
														]
													},
													{
														"funcName": "(internal) curve._A()",
														"returnValue": "0",
														"status": "",
														"childrenList":[
															{
																"funcName": "Load from curve.future_A: 0",
																"returnValue": "",
																"status": "",
																"childrenList":[]

															},
															{
																"funcName": "Storage State",
																"returnValue": "",
																"status": "",
																"childrenList":[
																	{
																		"funcName": "ERC20",
																		"returnValue": "",
																		"status": "",
																		"childrenList":[
																			{
																				"funcName": "_balances[ERC20 (0x270e)]: 10",
																				"returnValue": "",
																				"status": "HAVOC",
																				"childrenList":[]
,
																				"changed": "false"
																			},
																			{
																				"funcName": "_balances[identity (0xffff)]: 0xcd98cb94f23b4265",
																				"returnValue": "",
																				"status": "HAVOC",
																				"childrenList":[]
,
																				"changed": "false"
																			}
																		],
																		"storageId": "null"
																	},
																	{
																		"funcName": "CurveTokenExample",
																		"returnValue": "",
																		"status": "",
																		"childrenList":[
																			{
																				"funcName": "_balances[ERC20 (0x270e)]: 0x802c23c97dc928ced4c55c9cd9397b4",
																				"returnValue": "",
																				"status": "HAVOC",
																				"childrenList":[]
,
																				"changed": "false"
																			},
																			{
																				"funcName": "_totalSupply: 0x802c23c97dc928d32afe74c128797b4",
																				"returnValue": "",
																				"status": "HAVOC",
																				"childrenList":[]
,
																				"changed": "false"
																			}
																		],
																		"storageId": "null"
																	},
																	{
																		"funcName": "curve",
																		"returnValue": "",
																		"status": "",
																		"childrenList":[
																			{
																				"funcName": "_status: 0",
																				"returnValue": "",
																				"status": "HAVOC",
																				"childrenList":[]
,
																				"changed": "false"
																			},
																			{
																				"funcName": "admin_balances[0]: 0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffd",
																				"returnValue": "",
																				"status": "HAVOC",
																				"childrenList":[]
,
																				"changed": "false"
																			},
																			{
																				"funcName": "admin_balances[1]: 3",
																				"returnValue": "",
																				"status": "HAVOC",
																				"childrenList":[]
,
																				"changed": "false"
																			},
																			{
																				"funcName": "coins_1: ERC20 (0x270e)",
																				"returnValue": "",
																				"status": "HAVOC",
																				"childrenList":[]
,
																				"changed": "false"
																			},
																			{
																				"funcName": "future_A: 0",
																				"returnValue": "",
																				"status": "HAVOC",
																				"childrenList":[]
,
																				"changed": "false"
																			},
																			{
																				"funcName": "lp_token: CurveTokenExample (0x270d)",
																				"returnValue": "",
																				"status": "HAVOC",
																				"childrenList":[]
,
																				"changed": "false"
																			},
																			{
																				"funcName": "solghost_return_func1: *",
																				"returnValue": "",
																				"status": "DONT CARE",
																				"childrenList":[]
,
																				"changed": "false"
																			},
																			{
																				"funcName": "solghost_trigger_check: *",
																				"returnValue": "",
																				"status": "DONT CARE",
																				"childrenList":[]
,
																				"changed": "false"
																			}
																		],
																		"storageId": "null"
																	}
																],
																"storageId": "3"
															}
														]
													},
													{
														"funcName": "unknown loop source code",
														"returnValue": "",
														"status": "",
														"childrenList":[
															{
																"funcName": "Loop Iteration 1",
																"returnValue": "",
																"status": "",
																"childrenList":[]

															},
															{
																"funcName": "Loop Iteration 2",
																"returnValue": "",
																"status": "",
																"childrenList":[]

															}
														]
													},
													{
														"funcName": "curve.get_D(xp=[0=2, 1=0xcd98cb94f23b4262], amp=0)",
														"returnValue": "0xcd98cb94f23b4264",
														"status": "SUCCESS",
														"childrenList":[
															{
																"funcName": "unknown loop source code",
																"returnValue": "",
																"status": "",
																"childrenList":[
																	{
																		"funcName": "Loop Iteration 1",
																		"returnValue": "",
																		"status": "",
																		"childrenList":[]

																	},
																	{
																		"funcName": "Loop Iteration 2",
																		"returnValue": "",
																		"status": "",
																		"childrenList":[]

																	}
																]
															},
															{
																"funcName": "(internal) curve.get_D(xp=uint256[2], amp=0)",
																"returnValue": "0xcd98cb94f23b4264",
																"status": "",
																"childrenList":[
																	{
																		"funcName": "Storage State",
																		"returnValue": "",
																		"status": "",
																		"childrenList":[
																			{
																				"funcName": "ERC20",
																				"returnValue": "",
																				"status": "",
																				"childrenList":[
																					{
																						"funcName": "_balances[ERC20 (0x270e)]: 10",
																						"returnValue": "",
																						"status": "HAVOC",
																						"childrenList":[]
,
																						"changed": "false"
																					},
																					{
																						"funcName": "_balances[identity (0xffff)]: 0xcd98cb94f23b4265",
																						"returnValue": "",
																						"status": "HAVOC",
																						"childrenList":[]
,
																						"changed": "false"
																					}
																				],
																				"storageId": "null"
																			},
																			{
																				"funcName": "CurveTokenExample",
																				"returnValue": "",
																				"status": "",
																				"childrenList":[
																					{
																						"funcName": "_balances[ERC20 (0x270e)]: 0x802c23c97dc928ced4c55c9cd9397b4",
																						"returnValue": "",
																						"status": "HAVOC",
																						"childrenList":[]
,
																						"changed": "false"
																					},
																					{
																						"funcName": "_totalSupply: 0x802c23c97dc928d32afe74c128797b4",
																						"returnValue": "",
																						"status": "HAVOC",
																						"childrenList":[]
,
																						"changed": "false"
																					}
																				],
																				"storageId": "null"
																			},
																			{
																				"funcName": "curve",
																				"returnValue": "",
																				"status": "",
																				"childrenList":[
																					{
																						"funcName": "_status: 0",
																						"returnValue": "",
																						"status": "HAVOC",
																						"childrenList":[]
,
																						"changed": "false"
																					},
																					{
																						"funcName": "admin_balances[0]: 0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffd",
																						"returnValue": "",
																						"status": "HAVOC",
																						"childrenList":[]
,
																						"changed": "false"
																					},
																					{
																						"funcName": "admin_balances[1]: 3",
																						"returnValue": "",
																						"status": "HAVOC",
																						"childrenList":[]
,
																						"changed": "false"
																					},
																					{
																						"funcName": "coins_1: ERC20 (0x270e)",
																						"returnValue": "",
																						"status": "HAVOC",
																						"childrenList":[]
,
																						"changed": "false"
																					},
																					{
																						"funcName": "future_A: 0",
																						"returnValue": "",
																						"status": "HAVOC",
																						"childrenList":[]
,
																						"changed": "false"
																					},
																					{
																						"funcName": "lp_token: CurveTokenExample (0x270d)",
																						"returnValue": "",
																						"status": "HAVOC",
																						"childrenList":[]
,
																						"changed": "false"
																					},
																					{
																						"funcName": "solghost_return_func1: *",
																						"returnValue": "",
																						"status": "DONT CARE",
																						"childrenList":[]
,
																						"changed": "false"
																					},
																					{
																						"funcName": "solghost_trigger_check: *",
																						"returnValue": "",
																						"status": "DONT CARE",
																						"childrenList":[]
,
																						"changed": "false"
																					}
																				],
																				"storageId": "null"
																			}
																		],
																		"storageId": "4"
																	}
																]
															}
														]
													},
													{
														"funcName": "Load from curve.lp_token: CurveTokenExample (0x270d)",
														"returnValue": "",
														"status": "",
														"childrenList":[]

													},
													{
														"funcName": "CurveTokenExample.totalSupply()",
														"returnValue": "0x802c23c97dc928d32afe74c128797b4",
														"status": "SUCCESS",
														"childrenList":[
															{
																"funcName": "(internal) CurveTokenExample.totalSupply()",
																"returnValue": "0x802c23c97dc928d32afe74c128797b4",
																"status": "",
																"childrenList":[
																	{
																		"funcName": "Load from CurveTokenExample._totalSupply: 0x802c23c97dc928d32afe74c128797b4",
																		"returnValue": "",
																		"status": "",
																		"childrenList":[]

																	},
																	{
																		"funcName": "Storage State",
																		"returnValue": "",
																		"status": "",
																		"childrenList":[
																			{
																				"funcName": "ERC20",
																				"returnValue": "",
																				"status": "",
																				"childrenList":[
																					{
																						"funcName": "_balances[ERC20 (0x270e)]: 10",
																						"returnValue": "",
																						"status": "HAVOC",
																						"childrenList":[]
,
																						"changed": "false"
																					},
																					{
																						"funcName": "_balances[identity (0xffff)]: 0xcd98cb94f23b4265",
																						"returnValue": "",
																						"status": "HAVOC",
																						"childrenList":[]
,
																						"changed": "false"
																					}
																				],
																				"storageId": "null"
																			},
																			{
																				"funcName": "CurveTokenExample",
																				"returnValue": "",
																				"status": "",
																				"childrenList":[
																					{
																						"funcName": "_balances[ERC20 (0x270e)]: 0x802c23c97dc928ced4c55c9cd9397b4",
																						"returnValue": "",
																						"status": "HAVOC",
																						"childrenList":[]
,
																						"changed": "false"
																					},
																					{
																						"funcName": "_totalSupply: 0x802c23c97dc928d32afe74c128797b4",
																						"returnValue": "",
																						"status": "HAVOC",
																						"childrenList":[]
,
																						"changed": "false"
																					}
																				],
																				"storageId": "null"
																			},
																			{
																				"funcName": "curve",
																				"returnValue": "",
																				"status": "",
																				"childrenList":[
																					{
																						"funcName": "_status: 0",
																						"returnValue": "",
																						"status": "HAVOC",
																						"childrenList":[]
,
																						"changed": "false"
																					},
																					{
																						"funcName": "admin_balances[0]: 0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffd",
																						"returnValue": "",
																						"status": "HAVOC",
																						"childrenList":[]
,
																						"changed": "false"
																					},
																					{
																						"funcName": "admin_balances[1]: 3",
																						"returnValue": "",
																						"status": "HAVOC",
																						"childrenList":[]
,
																						"changed": "false"
																					},
																					{
																						"funcName": "coins_1: ERC20 (0x270e)",
																						"returnValue": "",
																						"status": "HAVOC",
																						"childrenList":[]
,
																						"changed": "false"
																					},
																					{
																						"funcName": "future_A: 0",
																						"returnValue": "",
																						"status": "HAVOC",
																						"childrenList":[]
,
																						"changed": "false"
																					},
																					{
																						"funcName": "lp_token: CurveTokenExample (0x270d)",
																						"returnValue": "",
																						"status": "HAVOC",
																						"childrenList":[]
,
																						"changed": "false"
																					},
																					{
																						"funcName": "solghost_return_func1: *",
																						"returnValue": "",
																						"status": "DONT CARE",
																						"childrenList":[]
,
																						"changed": "false"
																					},
																					{
																						"funcName": "solghost_trigger_check: *",
																						"returnValue": "",
																						"status": "DONT CARE",
																						"childrenList":[]
,
																						"changed": "false"
																					}
																				],
																				"storageId": "null"
																			}
																		],
																		"storageId": "5"
																	}
																]
															}
														]
													},
													{
														"funcName": "Storage State",
														"returnValue": "",
														"status": "",
														"childrenList":[
															{
																"funcName": "ERC20",
																"returnValue": "",
																"status": "",
																"childrenList":[
																	{
																		"funcName": "_balances[ERC20 (0x270e)]: 10",
																		"returnValue": "",
																		"status": "HAVOC",
																		"childrenList":[]
,
																		"changed": "false"
																	},
																	{
																		"funcName": "_balances[identity (0xffff)]: 0xcd98cb94f23b4265",
																		"returnValue": "",
																		"status": "HAVOC",
																		"childrenList":[]
,
																		"changed": "false"
																	}
																],
																"storageId": "null"
															},
															{
																"funcName": "CurveTokenExample",
																"returnValue": "",
																"status": "",
																"childrenList":[
																	{
																		"funcName": "_balances[ERC20 (0x270e)]: 0x802c23c97dc928ced4c55c9cd9397b4",
																		"returnValue": "",
																		"status": "HAVOC",
																		"childrenList":[]
,
																		"changed": "false"
																	},
																	{
																		"funcName": "_totalSupply: 0x802c23c97dc928d32afe74c128797b4",
																		"returnValue": "",
																		"status": "HAVOC",
																		"childrenList":[]
,
																		"changed": "false"
																	}
																],
																"storageId": "null"
															},
															{
																"funcName": "curve",
																"returnValue": "",
																"status": "",
																"childrenList":[
																	{
																		"funcName": "_status: 0",
																		"returnValue": "",
																		"status": "HAVOC",
																		"childrenList":[]
,
																		"changed": "false"
																	},
																	{
																		"funcName": "admin_balances[0]: 0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffd",
																		"returnValue": "",
																		"status": "HAVOC",
																		"childrenList":[]
,
																		"changed": "false"
																	},
																	{
																		"funcName": "admin_balances[1]: 3",
																		"returnValue": "",
																		"status": "HAVOC",
																		"childrenList":[]
,
																		"changed": "false"
																	},
																	{
																		"funcName": "coins_1: ERC20 (0x270e)",
																		"returnValue": "",
																		"status": "HAVOC",
																		"childrenList":[]
,
																		"changed": "false"
																	},
																	{
																		"funcName": "future_A: 0",
																		"returnValue": "",
																		"status": "HAVOC",
																		"childrenList":[]
,
																		"changed": "false"
																	},
																	{
																		"funcName": "lp_token: CurveTokenExample (0x270d)",
																		"returnValue": "",
																		"status": "HAVOC",
																		"childrenList":[]
,
																		"changed": "false"
																	},
																	{
																		"funcName": "solghost_return_func1: *",
																		"returnValue": "",
																		"status": "DONT CARE",
																		"childrenList":[]
,
																		"changed": "false"
																	},
																	{
																		"funcName": "solghost_trigger_check: *",
																		"returnValue": "",
																		"status": "DONT CARE",
																		"childrenList":[]
,
																		"changed": "false"
																	}
																],
																"storageId": "null"
															}
														],
														"storageId": "6"
													}
												]
											}
										]
									},
									{
										"funcName": "before_func1 == curve.getVirtualPrice(e_external)",
										"returnValue": "true",
										"status": "",
										"childrenList":[
											{
												"funcName": "before_func1",
												"returnValue": "13",
												"status": "",
												"childrenList":[]

											},
											{
												"funcName": "curve.getVirtualPrice(e_external)",
												"returnValue": "*",
												"status": "",
												"childrenList":[]

											}
										]
									}
								]
							},
							{
								"funcName": "curve.f(e, data)",
								"returnValue": "",
								"status": "",
								"childrenList":[
									{
										"funcName": "curve.remove_liquidity(_amount=0x802c23c97dc928ced4c55c9cd9397b3, _min_amounts=[])",
										"returnValue": "[]",
										"status": "SUCCESS",
										"childrenList":[
											{
												"funcName": "sender: ERC20 (0x270e); receiver: identity (0xffff); transferred amount: 0",
												"returnValue": "",
												"status": "TRANSFER",
												"childrenList":[
													{
														"funcName": "Load from sender.balance: 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff (MAX_UINT256)",
														"returnValue": "",
														"status": "",
														"childrenList":[]

													},
													{
														"funcName": "Store at sender.balance: 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff (MAX_UINT256)",
														"returnValue": "",
														"status": "",
														"childrenList":[]

													},
													{
														"funcName": "Load from receiver.balance: 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff (MAX_UINT256)",
														"returnValue": "",
														"status": "",
														"childrenList":[]

													},
													{
														"funcName": "Store at receiver.balance: 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff (MAX_UINT256)",
														"returnValue": "",
														"status": "",
														"childrenList":[]

													}
												]
											},
											{
												"funcName": "unknown loop source code",
												"returnValue": "",
												"status": "",
												"childrenList":[
													{
														"funcName": "Loop Iteration 1",
														"returnValue": "",
														"status": "",
														"childrenList":[]

													},
													{
														"funcName": "Loop Iteration 2",
														"returnValue": "",
														"status": "",
														"childrenList":[]

													}
												]
											},
											{
												"funcName": "(internal) ReentrancyGuard._nonReentrantBefore()",
												"returnValue": "",
												"status": "",
												"childrenList":[
													{
														"funcName": "Load from curve._status: 0",
														"returnValue": "",
														"status": "",
														"childrenList":[]

													},
													{
														"funcName": "Store at curve._status: 2",
														"returnValue": "",
														"status": "",
														"childrenList":[]

													},
													{
														"funcName": "Storage State",
														"returnValue": "",
														"status": "",
														"childrenList":[
															{
																"funcName": "ERC20",
																"returnValue": "",
																"status": "",
																"childrenList":[
																	{
																		"funcName": "_balances[ERC20 (0x270e)]: 10",
																		"returnValue": "",
																		"status": "HAVOC",
																		"childrenList":[]
,
																		"changed": "false"
																	},
																	{
																		"funcName": "_balances[identity (0xffff)]: 0xcd98cb94f23b4265",
																		"returnValue": "",
																		"status": "HAVOC",
																		"childrenList":[]
,
																		"changed": "false"
																	}
																],
																"storageId": "null"
															},
															{
																"funcName": "CurveTokenExample",
																"returnValue": "",
																"status": "",
																"childrenList":[
																	{
																		"funcName": "_balances[ERC20 (0x270e)]: 0x802c23c97dc928ced4c55c9cd9397b4",
																		"returnValue": "",
																		"status": "HAVOC",
																		"childrenList":[]
,
																		"changed": "false"
																	},
																	{
																		"funcName": "_totalSupply: 0x802c23c97dc928d32afe74c128797b4",
																		"returnValue": "",
																		"status": "HAVOC",
																		"childrenList":[]
,
																		"changed": "false"
																	}
																],
																"storageId": "null"
															},
															{
																"funcName": "curve",
																"returnValue": "",
																"status": "",
																"childrenList":[
																	{
																		"funcName": "_status: 2 (changed)",
																		"returnValue": "",
																		"status": "CONCRETE",
																		"childrenList":[]
,
																		"changed": "true"
																	},
																	{
																		"funcName": "admin_balances[0]: 0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffd",
																		"returnValue": "",
																		"status": "HAVOC",
																		"childrenList":[]
,
																		"changed": "false"
																	},
																	{
																		"funcName": "admin_balances[1]: 3",
																		"returnValue": "",
																		"status": "HAVOC",
																		"childrenList":[]
,
																		"changed": "false"
																	},
																	{
																		"funcName": "coins_1: ERC20 (0x270e)",
																		"returnValue": "",
																		"status": "HAVOC",
																		"childrenList":[]
,
																		"changed": "false"
																	},
																	{
																		"funcName": "future_A: 0",
																		"returnValue": "",
																		"status": "HAVOC",
																		"childrenList":[]
,
																		"changed": "false"
																	},
																	{
																		"funcName": "lp_token: CurveTokenExample (0x270d)",
																		"returnValue": "",
																		"status": "HAVOC",
																		"childrenList":[]
,
																		"changed": "false"
																	},
																	{
																		"funcName": "solghost_return_func1: *",
																		"returnValue": "",
																		"status": "DONT CARE",
																		"childrenList":[]
,
																		"changed": "false"
																	},
																	{
																		"funcName": "solghost_trigger_check: *",
																		"returnValue": "",
																		"status": "DONT CARE",
																		"childrenList":[]
,
																		"changed": "false"
																	}
																],
																"storageId": "null"
															}
														],
														"storageId": "7"
													}
												]
											},
											{
												"funcName": "Load from curve.admin_balances[0]: 0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffd",
												"returnValue": "",
												"status": "",
												"childrenList":[]

											},
											{
												"funcName": "Load from curve.admin_balances[1]: 3",
												"returnValue": "",
												"status": "",
												"childrenList":[]

											},
											{
												"funcName": "Load from curve.coins_1: ERC20 (0x270e)",
												"returnValue": "",
												"status": "",
												"childrenList":[]

											},
											{
												"funcName": "ERC20.balanceOf(account=identity (0xffff))",
												"returnValue": "0xcd98cb94f23b4265",
												"status": "SUCCESS",
												"childrenList":[
													{
														"funcName": "(internal) ERC20.balanceOf(account=identity (0xffff))",
														"returnValue": "0xcd98cb94f23b4265",
														"status": "",
														"childrenList":[
															{
																"funcName": "Load from ERC20._balances[identity (0xffff)]: 0xcd98cb94f23b4265",
																"returnValue": "",
																"status": "",
																"childrenList":[]

															},
															{
																"funcName": "Storage State",
																"returnValue": "",
																"status": "",
																"childrenList":[
																	{
																		"funcName": "ERC20",
																		"returnValue": "",
																		"status": "",
																		"childrenList":[
																			{
																				"funcName": "_balances[ERC20 (0x270e)]: 10",
																				"returnValue": "",
																				"status": "HAVOC",
																				"childrenList":[]
,
																				"changed": "false"
																			},
																			{
																				"funcName": "_balances[identity (0xffff)]: 0xcd98cb94f23b4265",
																				"returnValue": "",
																				"status": "HAVOC",
																				"childrenList":[]
,
																				"changed": "false"
																			}
																		],
																		"storageId": "null"
																	},
																	{
																		"funcName": "CurveTokenExample",
																		"returnValue": "",
																		"status": "",
																		"childrenList":[
																			{
																				"funcName": "_balances[ERC20 (0x270e)]: 0x802c23c97dc928ced4c55c9cd9397b4",
																				"returnValue": "",
																				"status": "HAVOC",
																				"childrenList":[]
,
																				"changed": "false"
																			},
																			{
																				"funcName": "_totalSupply: 0x802c23c97dc928d32afe74c128797b4",
																				"returnValue": "",
																				"status": "HAVOC",
																				"childrenList":[]
,
																				"changed": "false"
																			}
																		],
																		"storageId": "null"
																	},
																	{
																		"funcName": "curve",
																		"returnValue": "",
																		"status": "",
																		"childrenList":[
																			{
																				"funcName": "_status: 2",
																				"returnValue": "",
																				"status": "CONCRETE",
																				"childrenList":[]
,
																				"changed": "false"
																			},
																			{
																				"funcName": "admin_balances[0]: 0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffd",
																				"returnValue": "",
																				"status": "HAVOC",
																				"childrenList":[]
,
																				"changed": "false"
																			},
																			{
																				"funcName": "admin_balances[1]: 3",
																				"returnValue": "",
																				"status": "HAVOC",
																				"childrenList":[]
,
																				"changed": "false"
																			},
																			{
																				"funcName": "coins_1: ERC20 (0x270e)",
																				"returnValue": "",
																				"status": "HAVOC",
																				"childrenList":[]
,
																				"changed": "false"
																			},
																			{
																				"funcName": "future_A: 0",
																				"returnValue": "",
																				"status": "HAVOC",
																				"childrenList":[]
,
																				"changed": "false"
																			},
																			{
																				"funcName": "lp_token: CurveTokenExample (0x270d)",
																				"returnValue": "",
																				"status": "HAVOC",
																				"childrenList":[]
,
																				"changed": "false"
																			},
																			{
																				"funcName": "solghost_return_func1: *",
																				"returnValue": "",
																				"status": "DONT CARE",
																				"childrenList":[]
,
																				"changed": "false"
																			},
																			{
																				"funcName": "solghost_trigger_check: *",
																				"returnValue": "",
																				"status": "DONT CARE",
																				"childrenList":[]
,
																				"changed": "false"
																			}
																		],
																		"storageId": "null"
																	}
																],
																"storageId": "8"
															}
														]
													}
												]
											},
											{
												"funcName": "Load from curve.lp_token: CurveTokenExample (0x270d)",
												"returnValue": "",
												"status": "",
												"childrenList":[]

											},
											{
												"funcName": "CurveTokenExample.totalSupply()",
												"returnValue": "0x802c23c97dc928d32afe74c128797b4",
												"status": "SUCCESS",
												"childrenList":[
													{
														"funcName": "(internal) CurveTokenExample.totalSupply()",
														"returnValue": "0x802c23c97dc928d32afe74c128797b4",
														"status": "",
														"childrenList":[
															{
																"funcName": "Load from CurveTokenExample._totalSupply: 0x802c23c97dc928d32afe74c128797b4",
																"returnValue": "",
																"status": "",
																"childrenList":[]

															},
															{
																"funcName": "Storage State",
																"returnValue": "",
																"status": "",
																"childrenList":[
																	{
																		"funcName": "ERC20",
																		"returnValue": "",
																		"status": "",
																		"childrenList":[
																			{
																				"funcName": "_balances[ERC20 (0x270e)]: 10",
																				"returnValue": "",
																				"status": "HAVOC",
																				"childrenList":[]
,
																				"changed": "false"
																			},
																			{
																				"funcName": "_balances[identity (0xffff)]: 0xcd98cb94f23b4265",
																				"returnValue": "",
																				"status": "HAVOC",
																				"childrenList":[]
,
																				"changed": "false"
																			}
																		],
																		"storageId": "null"
																	},
																	{
																		"funcName": "CurveTokenExample",
																		"returnValue": "",
																		"status": "",
																		"childrenList":[
																			{
																				"funcName": "_balances[ERC20 (0x270e)]: 0x802c23c97dc928ced4c55c9cd9397b4",
																				"returnValue": "",
																				"status": "HAVOC",
																				"childrenList":[]
,
																				"changed": "false"
																			},
																			{
																				"funcName": "_totalSupply: 0x802c23c97dc928d32afe74c128797b4",
																				"returnValue": "",
																				"status": "HAVOC",
																				"childrenList":[]
,
																				"changed": "false"
																			}
																		],
																		"storageId": "null"
																	},
																	{
																		"funcName": "curve",
																		"returnValue": "",
																		"status": "",
																		"childrenList":[
																			{
																				"funcName": "_status: 2",
																				"returnValue": "",
																				"status": "CONCRETE",
																				"childrenList":[]
,
																				"changed": "false"
																			},
																			{
																				"funcName": "admin_balances[0]: 0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffd",
																				"returnValue": "",
																				"status": "HAVOC",
																				"childrenList":[]
,
																				"changed": "false"
																			},
																			{
																				"funcName": "admin_balances[1]: 3",
																				"returnValue": "",
																				"status": "HAVOC",
																				"childrenList":[]
,
																				"changed": "false"
																			},
																			{
																				"funcName": "coins_1: ERC20 (0x270e)",
																				"returnValue": "",
																				"status": "HAVOC",
																				"childrenList":[]
,
																				"changed": "false"
																			},
																			{
																				"funcName": "future_A: 0",
																				"returnValue": "",
																				"status": "HAVOC",
																				"childrenList":[]
,
																				"changed": "false"
																			},
																			{
																				"funcName": "lp_token: CurveTokenExample (0x270d)",
																				"returnValue": "",
																				"status": "HAVOC",
																				"childrenList":[]
,
																				"changed": "false"
																			},
																			{
																				"funcName": "solghost_return_func1: *",
																				"returnValue": "",
																				"status": "DONT CARE",
																				"childrenList":[]
,
																				"changed": "false"
																			},
																			{
																				"funcName": "solghost_trigger_check: *",
																				"returnValue": "",
																				"status": "DONT CARE",
																				"childrenList":[]
,
																				"changed": "false"
																			}
																		],
																		"storageId": "null"
																	}
																],
																"storageId": "9"
															}
														]
													}
												]
											},
											{
												"funcName": "Load from curve.lp_token: CurveTokenExample (0x270d)",
												"returnValue": "",
												"status": "",
												"childrenList":[]

											},
											{
												"funcName": "CurveTokenExample.burnFrom(to=ERC20 (0x270e), value=0x802c23c97dc928ced4c55c9cd9397b3)",
												"returnValue": "true",
												"status": "SUCCESS",
												"childrenList":[
													{
														"funcName": "(internal) ERC20._burn(account=ERC20 (0x270e), amount=0x802c23c97dc928ced4c55c9cd9397b3)",
														"returnValue": "",
														"status": "",
														"childrenList":[
															{
																"funcName": "(internal) ERC20._update(from=ERC20 (0x270e), to=0, amount=0x802c23c97dc928ced4c55c9cd9397b3)",
																"returnValue": "",
																"status": "",
																"childrenList":[
																	{
																		"funcName": "Load from CurveTokenExample._balances[ERC20 (0x270e)]: 0x802c23c97dc928ced4c55c9cd9397b4",
																		"returnValue": "",
																		"status": "",
																		"childrenList":[]

																	},
																	{
																		"funcName": "Store at CurveTokenExample._balances[ERC20 (0x270e)]: 1",
																		"returnValue": "",
																		"status": "",
																		"childrenList":[]

																	},
																	{
																		"funcName": "Load from CurveTokenExample._totalSupply: 0x802c23c97dc928d32afe74c128797b4",
																		"returnValue": "",
																		"status": "",
																		"childrenList":[]

																	},
																	{
																		"funcName": "Store at CurveTokenExample._totalSupply: 0x4563918244f40001",
																		"returnValue": "",
																		"status": "",
																		"childrenList":[]

																	},
																	{
																		"funcName": "Storage State",
																		"returnValue": "",
																		"status": "",
																		"childrenList":[
																			{
																				"funcName": "ERC20",
																				"returnValue": "",
																				"status": "",
																				"childrenList":[
																					{
																						"funcName": "_balances[ERC20 (0x270e)]: 10",
																						"returnValue": "",
																						"status": "HAVOC",
																						"childrenList":[]
,
																						"changed": "false"
																					},
																					{
																						"funcName": "_balances[identity (0xffff)]: 0xcd98cb94f23b4265",
																						"returnValue": "",
																						"status": "HAVOC",
																						"childrenList":[]
,
																						"changed": "false"
																					}
																				],
																				"storageId": "null"
																			},
																			{
																				"funcName": "CurveTokenExample",
																				"returnValue": "",
																				"status": "",
																				"childrenList":[
																					{
																						"funcName": "_balances[ERC20 (0x270e)]: 1 (changed)",
																						"returnValue": "",
																						"status": "HAVOC DEPENDENT",
																						"childrenList":[]
,
																						"changed": "true"
																					},
																					{
																						"funcName": "_totalSupply: 0x4563918244f40001 (changed)",
																						"returnValue": "",
																						"status": "HAVOC DEPENDENT",
																						"childrenList":[]
,
																						"changed": "true"
																					}
																				],
																				"storageId": "null"
																			},
																			{
																				"funcName": "curve",
																				"returnValue": "",
																				"status": "",
																				"childrenList":[
																					{
																						"funcName": "_status: 2",
																						"returnValue": "",
																						"status": "CONCRETE",
																						"childrenList":[]
,
																						"changed": "false"
																					},
																					{
																						"funcName": "admin_balances[0]: 0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffd",
																						"returnValue": "",
																						"status": "HAVOC",
																						"childrenList":[]
,
																						"changed": "false"
																					},
																					{
																						"funcName": "admin_balances[1]: 3",
																						"returnValue": "",
																						"status": "HAVOC",
																						"childrenList":[]
,
																						"changed": "false"
																					},
																					{
																						"funcName": "coins_1: ERC20 (0x270e)",
																						"returnValue": "",
																						"status": "HAVOC",
																						"childrenList":[]
,
																						"changed": "false"
																					},
																					{
																						"funcName": "future_A: 0",
																						"returnValue": "",
																						"status": "HAVOC",
																						"childrenList":[]
,
																						"changed": "false"
																					},
																					{
																						"funcName": "lp_token: CurveTokenExample (0x270d)",
																						"returnValue": "",
																						"status": "HAVOC",
																						"childrenList":[]
,
																						"changed": "false"
																					},
																					{
																						"funcName": "solghost_return_func1: *",
																						"returnValue": "",
																						"status": "DONT CARE",
																						"childrenList":[]
,
																						"changed": "false"
																					},
																					{
																						"funcName": "solghost_trigger_check: *",
																						"returnValue": "",
																						"status": "DONT CARE",
																						"childrenList":[]
,
																						"changed": "false"
																					}
																				],
																				"storageId": "null"
																			}
																		],
																		"storageId": "10"
																	}
																]
															},
															{
																"funcName": "Storage State",
																"returnValue": "",
																"status": "",
																"childrenList":[
																	{
																		"funcName": "ERC20",
																		"returnValue": "",
																		"status": "",
																		"childrenList":[
																			{
																				"funcName": "_balances[ERC20 (0x270e)]: 10",
																				"returnValue": "",
																				"status": "HAVOC",
																				"childrenList":[]
,
																				"changed": "false"
																			},
																			{
																				"funcName": "_balances[identity (0xffff)]: 0xcd98cb94f23b4265",
																				"returnValue": "",
																				"status": "HAVOC",
																				"childrenList":[]
,
																				"changed": "false"
																			}
																		],
																		"storageId": "null"
																	},
																	{
																		"funcName": "CurveTokenExample",
																		"returnValue": "",
																		"status": "",
																		"childrenList":[
																			{
																				"funcName": "_balances[ERC20 (0x270e)]: 1",
																				"returnValue": "",
																				"status": "HAVOC DEPENDENT",
																				"childrenList":[]
,
																				"changed": "false"
																			},
																			{
																				"funcName": "_totalSupply: 0x4563918244f40001",
																				"returnValue": "",
																				"status": "HAVOC DEPENDENT",
																				"childrenList":[]
,
																				"changed": "false"
																			}
																		],
																		"storageId": "null"
																	},
																	{
																		"funcName": "curve",
																		"returnValue": "",
																		"status": "",
																		"childrenList":[
																			{
																				"funcName": "_status: 2",
																				"returnValue": "",
																				"status": "CONCRETE",
																				"childrenList":[]
,
																				"changed": "false"
																			},
																			{
																				"funcName": "admin_balances[0]: 0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffd",
																				"returnValue": "",
																				"status": "HAVOC",
																				"childrenList":[]
,
																				"changed": "false"
																			},
																			{
																				"funcName": "admin_balances[1]: 3",
																				"returnValue": "",
																				"status": "HAVOC",
																				"childrenList":[]
,
																				"changed": "false"
																			},
																			{
																				"funcName": "coins_1: ERC20 (0x270e)",
																				"returnValue": "",
																				"status": "HAVOC",
																				"childrenList":[]
,
																				"changed": "false"
																			},
																			{
																				"funcName": "future_A: 0",
																				"returnValue": "",
																				"status": "HAVOC",
																				"childrenList":[]
,
																				"changed": "false"
																			},
																			{
																				"funcName": "lp_token: CurveTokenExample (0x270d)",
																				"returnValue": "",
																				"status": "HAVOC",
																				"childrenList":[]
,
																				"changed": "false"
																			},
																			{
																				"funcName": "solghost_return_func1: *",
																				"returnValue": "",
																				"status": "DONT CARE",
																				"childrenList":[]
,
																				"changed": "false"
																			},
																			{
																				"funcName": "solghost_trigger_check: *",
																				"returnValue": "",
																				"status": "DONT CARE",
																				"childrenList":[]
,
																				"changed": "false"
																			}
																		],
																		"storageId": "null"
																	}
																],
																"storageId": "11"
															}
														]
													}
												]
											},
											{
												"funcName": "Loop at curve.sol: line: 180: for (uint256 i;i<2;i++){",
												"returnValue": "",
												"status": "",
												"childrenList":[
													{
														"funcName": "Loop Iteration 1",
														"returnValue": "",
														"status": "",
														"childrenList":[
															{
																"funcName": "(internal) curve.sample_view_functions()",
																"returnValue": "",
																"status": "",
																"childrenList":[
																	{
																		"funcName": "(internal) curve.getVirtualPrice()",
																		"returnValue": "0x19b319729e47684c2",
																		"status": "",
																		"childrenList":[
																			{
																				"funcName": "Load from curve.admin_balances[0]: 0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffd",
																				"returnValue": "",
																				"status": "",
																				"childrenList":[]

																			},
																			{
																				"funcName": "Load from curve.admin_balances[1]: 3",
																				"returnValue": "",
																				"status": "",
																				"childrenList":[]

																			},
																			{
																				"funcName": "Load from curve.coins_1: ERC20 (0x270e)",
																				"returnValue": "",
																				"status": "",
																				"childrenList":[]

																			},
																			{
																				"funcName": "ERC20.balanceOf(account=identity (0xffff))",
																				"returnValue": "0xcd98cb94f23b4265",
																				"status": "SUCCESS",
																				"childrenList":[
																					{
																						"funcName": "(internal) ERC20.balanceOf(account=identity (0xffff))",
																						"returnValue": "0xcd98cb94f23b4265",
																						"status": "",
																						"childrenList":[
																							{
																								"funcName": "Load from ERC20._balances[identity (0xffff)]: 0xcd98cb94f23b4265",
																								"returnValue": "",
																								"status": "",
																								"childrenList":[]

																							},
																							{
																								"funcName": "Storage State",
																								"returnValue": "",
																								"status": "",
																								"childrenList":[
																									{
																										"funcName": "ERC20",
																										"returnValue": "",
																										"status": "",
																										"childrenList":[
																											{
																												"funcName": "_balances[ERC20 (0x270e)]: 10",
																												"returnValue": "",
																												"status": "HAVOC",
																												"childrenList":[]
,
																												"changed": "false"
																											},
																											{
																												"funcName": "_balances[identity (0xffff)]: 0xcd98cb94f23b4265",
																												"returnValue": "",
																												"status": "HAVOC",
																												"childrenList":[]
,
																												"changed": "false"
																											}
																										],
																										"storageId": "null"
																									},
																									{
																										"funcName": "CurveTokenExample",
																										"returnValue": "",
																										"status": "",
																										"childrenList":[
																											{
																												"funcName": "_balances[ERC20 (0x270e)]: 1",
																												"returnValue": "",
																												"status": "HAVOC DEPENDENT",
																												"childrenList":[]
,
																												"changed": "false"
																											},
																											{
																												"funcName": "_totalSupply: 0x4563918244f40001",
																												"returnValue": "",
																												"status": "HAVOC DEPENDENT",
																												"childrenList":[]
,
																												"changed": "false"
																											}
																										],
																										"storageId": "null"
																									},
																									{
																										"funcName": "curve",
																										"returnValue": "",
																										"status": "",
																										"childrenList":[
																											{
																												"funcName": "_status: 2",
																												"returnValue": "",
																												"status": "CONCRETE",
																												"childrenList":[]
,
																												"changed": "false"
																											},
																											{
																												"funcName": "admin_balances[0]: 0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffd",
																												"returnValue": "",
																												"status": "HAVOC",
																												"childrenList":[]
,
																												"changed": "false"
																											},
																											{
																												"funcName": "admin_balances[1]: 3",
																												"returnValue": "",
																												"status": "HAVOC",
																												"childrenList":[]
,
																												"changed": "false"
																											},
																											{
																												"funcName": "coins_1: ERC20 (0x270e)",
																												"returnValue": "",
																												"status": "HAVOC",
																												"childrenList":[]
,
																												"changed": "false"
																											},
																											{
																												"funcName": "future_A: 0",
																												"returnValue": "",
																												"status": "HAVOC",
																												"childrenList":[]
,
																												"changed": "false"
																											},
																											{
																												"funcName": "lp_token: CurveTokenExample (0x270d)",
																												"returnValue": "",
																												"status": "HAVOC",
																												"childrenList":[]
,
																												"changed": "false"
																											},
																											{
																												"funcName": "solghost_return_func1: *",
																												"returnValue": "",
																												"status": "DONT CARE",
																												"childrenList":[]
,
																												"changed": "false"
																											},
																											{
																												"funcName": "solghost_trigger_check: *",
																												"returnValue": "",
																												"status": "DONT CARE",
																												"childrenList":[]
,
																												"changed": "false"
																											}
																										],
																										"storageId": "null"
																									}
																								],
																								"storageId": "12"
																							}
																						]
																					}
																				]
																			},
																			{
																				"funcName": "(internal) curve._A()",
																				"returnValue": "0",
																				"status": "",
																				"childrenList":[
																					{
																						"funcName": "Load from curve.future_A: 0",
																						"returnValue": "",
																						"status": "",
																						"childrenList":[]

																					},
																					{
																						"funcName": "Storage State",
																						"returnValue": "",
																						"status": "",
																						"childrenList":[
																							{
																								"funcName": "ERC20",
																								"returnValue": "",
																								"status": "",
																								"childrenList":[
																									{
																										"funcName": "_balances[ERC20 (0x270e)]: 10",
																										"returnValue": "",
																										"status": "HAVOC",
																										"childrenList":[]
,
																										"changed": "false"
																									},
																									{
																										"funcName": "_balances[identity (0xffff)]: 0xcd98cb94f23b4265",
																										"returnValue": "",
																										"status": "HAVOC",
																										"childrenList":[]
,
																										"changed": "false"
																									}
																								],
																								"storageId": "null"
																							},
																							{
																								"funcName": "CurveTokenExample",
																								"returnValue": "",
																								"status": "",
																								"childrenList":[
																									{
																										"funcName": "_balances[ERC20 (0x270e)]: 1",
																										"returnValue": "",
																										"status": "HAVOC DEPENDENT",
																										"childrenList":[]
,
																										"changed": "false"
																									},
																									{
																										"funcName": "_totalSupply: 0x4563918244f40001",
																										"returnValue": "",
																										"status": "HAVOC DEPENDENT",
																										"childrenList":[]
,
																										"changed": "false"
																									}
																								],
																								"storageId": "null"
																							},
																							{
																								"funcName": "curve",
																								"returnValue": "",
																								"status": "",
																								"childrenList":[
																									{
																										"funcName": "_status: 2",
																										"returnValue": "",
																										"status": "CONCRETE",
																										"childrenList":[]
,
																										"changed": "false"
																									},
																									{
																										"funcName": "admin_balances[0]: 0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffd",
																										"returnValue": "",
																										"status": "HAVOC",
																										"childrenList":[]
,
																										"changed": "false"
																									},
																									{
																										"funcName": "admin_balances[1]: 3",
																										"returnValue": "",
																										"status": "HAVOC",
																										"childrenList":[]
,
																										"changed": "false"
																									},
																									{
																										"funcName": "coins_1: ERC20 (0x270e)",
																										"returnValue": "",
																										"status": "HAVOC",
																										"childrenList":[]
,
																										"changed": "false"
																									},
																									{
																										"funcName": "future_A: 0",
																										"returnValue": "",
																										"status": "HAVOC",
																										"childrenList":[]
,
																										"changed": "false"
																									},
																									{
																										"funcName": "lp_token: CurveTokenExample (0x270d)",
																										"returnValue": "",
																										"status": "HAVOC",
																										"childrenList":[]
,
																										"changed": "false"
																									},
																									{
																										"funcName": "solghost_return_func1: *",
																										"returnValue": "",
																										"status": "DONT CARE",
																										"childrenList":[]
,
																										"changed": "false"
																									},
																									{
																										"funcName": "solghost_trigger_check: *",
																										"returnValue": "",
																										"status": "DONT CARE",
																										"childrenList":[]
,
																										"changed": "false"
																									}
																								],
																								"storageId": "null"
																							}
																						],
																						"storageId": "13"
																					}
																				]
																			},
																			{
																				"funcName": "unknown loop source code",
																				"returnValue": "",
																				"status": "",
																				"childrenList":[
																					{
																						"funcName": "Loop Iteration 1",
																						"returnValue": "",
																						"status": "",
																						"childrenList":[]

																					},
																					{
																						"funcName": "Loop Iteration 2",
																						"returnValue": "",
																						"status": "",
																						"childrenList":[]

																					}
																				]
																			},
																			{
																				"funcName": "curve.get_D(xp=[0=2, 1=0xcd98cb94f23b4262], amp=0)",
																				"returnValue": "0xcd98cb94f23b4264",
																				"status": "SUCCESS",
																				"childrenList":[
																					{
																						"funcName": "unknown loop source code",
																						"returnValue": "",
																						"status": "",
																						"childrenList":[
																							{
																								"funcName": "Loop Iteration 1",
																								"returnValue": "",
																								"status": "",
																								"childrenList":[]

																							},
																							{
																								"funcName": "Loop Iteration 2",
																								"returnValue": "",
																								"status": "",
																								"childrenList":[]

																							}
																						]
																					},
																					{
																						"funcName": "(internal) curve.get_D(xp=uint256[2], amp=0)",
																						"returnValue": "0xcd98cb94f23b4264",
																						"status": "",
																						"childrenList":[
																							{
																								"funcName": "Storage State",
																								"returnValue": "",
																								"status": "",
																								"childrenList":[
																									{
																										"funcName": "ERC20",
																										"returnValue": "",
																										"status": "",
																										"childrenList":[
																											{
																												"funcName": "_balances[ERC20 (0x270e)]: 10",
																												"returnValue": "",
																												"status": "HAVOC",
																												"childrenList":[]
,
																												"changed": "false"
																											},
																											{
																												"funcName": "_balances[identity (0xffff)]: 0xcd98cb94f23b4265",
																												"returnValue": "",
																												"status": "HAVOC",
																												"childrenList":[]
,
																												"changed": "false"
																											}
																										],
																										"storageId": "null"
																									},
																									{
																										"funcName": "CurveTokenExample",
																										"returnValue": "",
																										"status": "",
																										"childrenList":[
																											{
																												"funcName": "_balances[ERC20 (0x270e)]: 1",
																												"returnValue": "",
																												"status": "HAVOC DEPENDENT",
																												"childrenList":[]
,
																												"changed": "false"
																											},
																											{
																												"funcName": "_totalSupply: 0x4563918244f40001",
																												"returnValue": "",
																												"status": "HAVOC DEPENDENT",
																												"childrenList":[]
,
																												"changed": "false"
																											}
																										],
																										"storageId": "null"
																									},
																									{
																										"funcName": "curve",
																										"returnValue": "",
																										"status": "",
																										"childrenList":[
																											{
																												"funcName": "_status: 2",
																												"returnValue": "",
																												"status": "CONCRETE",
																												"childrenList":[]
,
																												"changed": "false"
																											},
																											{
																												"funcName": "admin_balances[0]: 0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffd",
																												"returnValue": "",
																												"status": "HAVOC",
																												"childrenList":[]
,
																												"changed": "false"
																											},
																											{
																												"funcName": "admin_balances[1]: 3",
																												"returnValue": "",
																												"status": "HAVOC",
																												"childrenList":[]
,
																												"changed": "false"
																											},
																											{
																												"funcName": "coins_1: ERC20 (0x270e)",
																												"returnValue": "",
																												"status": "HAVOC",
																												"childrenList":[]
,
																												"changed": "false"
																											},
																											{
																												"funcName": "future_A: 0",
																												"returnValue": "",
																												"status": "HAVOC",
																												"childrenList":[]
,
																												"changed": "false"
																											},
																											{
																												"funcName": "lp_token: CurveTokenExample (0x270d)",
																												"returnValue": "",
																												"status": "HAVOC",
																												"childrenList":[]
,
																												"changed": "false"
																											},
																											{
																												"funcName": "solghost_return_func1: *",
																												"returnValue": "",
																												"status": "DONT CARE",
																												"childrenList":[]
,
																												"changed": "false"
																											},
																											{
																												"funcName": "solghost_trigger_check: *",
																												"returnValue": "",
																												"status": "DONT CARE",
																												"childrenList":[]
,
																												"changed": "false"
																											}
																										],
																										"storageId": "null"
																									}
																								],
																								"storageId": "14"
																							}
																						]
																					}
																				]
																			},
																			{
																				"funcName": "Load from curve.lp_token: CurveTokenExample (0x270d)",
																				"returnValue": "",
																				"status": "",
																				"childrenList":[]

																			},
																			{
																				"funcName": "CurveTokenExample.totalSupply()",
																				"returnValue": "0x4563918244f40001",
																				"status": "SUCCESS",
																				"childrenList":[
																					{
																						"funcName": "(internal) CurveTokenExample.totalSupply()",
																						"returnValue": "0x4563918244f40001",
																						"status": "",
																						"childrenList":[
																							{
																								"funcName": "Load from CurveTokenExample._totalSupply: 0x4563918244f40001",
																								"returnValue": "",
																								"status": "",
																								"childrenList":[]

																							},
																							{
																								"funcName": "Storage State",
																								"returnValue": "",
																								"status": "",
																								"childrenList":[
																									{
																										"funcName": "ERC20",
																										"returnValue": "",
																										"status": "",
																										"childrenList":[
																											{
																												"funcName": "_balances[ERC20 (0x270e)]: 10",
																												"returnValue": "",
																												"status": "HAVOC",
																												"childrenList":[]
,
																												"changed": "false"
																											},
																											{
																												"funcName": "_balances[identity (0xffff)]: 0xcd98cb94f23b4265",
																												"returnValue": "",
																												"status": "HAVOC",
																												"childrenList":[]
,
																												"changed": "false"
																											}
																										],
																										"storageId": "null"
																									},
																									{
																										"funcName": "CurveTokenExample",
																										"returnValue": "",
																										"status": "",
																										"childrenList":[
																											{
																												"funcName": "_balances[ERC20 (0x270e)]: 1",
																												"returnValue": "",
																												"status": "HAVOC DEPENDENT",
																												"childrenList":[]
,
																												"changed": "false"
																											},
																											{
																												"funcName": "_totalSupply: 0x4563918244f40001",
																												"returnValue": "",
																												"status": "HAVOC DEPENDENT",
																												"childrenList":[]
,
																												"changed": "false"
																											}
																										],
																										"storageId": "null"
																									},
																									{
																										"funcName": "curve",
																										"returnValue": "",
																										"status": "",
																										"childrenList":[
																											{
																												"funcName": "_status: 2",
																												"returnValue": "",
																												"status": "CONCRETE",
																												"childrenList":[]
,
																												"changed": "false"
																											},
																											{
																												"funcName": "admin_balances[0]: 0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffd",
																												"returnValue": "",
																												"status": "HAVOC",
																												"childrenList":[]
,
																												"changed": "false"
																											},
																											{
																												"funcName": "admin_balances[1]: 3",
																												"returnValue": "",
																												"status": "HAVOC",
																												"childrenList":[]
,
																												"changed": "false"
																											},
																											{
																												"funcName": "coins_1: ERC20 (0x270e)",
																												"returnValue": "",
																												"status": "HAVOC",
																												"childrenList":[]
,
																												"changed": "false"
																											},
																											{
																												"funcName": "future_A: 0",
																												"returnValue": "",
																												"status": "HAVOC",
																												"childrenList":[]
,
																												"changed": "false"
																											},
																											{
																												"funcName": "lp_token: CurveTokenExample (0x270d)",
																												"returnValue": "",
																												"status": "HAVOC",
																												"childrenList":[]
,
																												"changed": "false"
																											},
																											{
																												"funcName": "solghost_return_func1: *",
																												"returnValue": "",
																												"status": "DONT CARE",
																												"childrenList":[]
,
																												"changed": "false"
																											},
																											{
																												"funcName": "solghost_trigger_check: *",
																												"returnValue": "",
																												"status": "DONT CARE",
																												"childrenList":[]
,
																												"changed": "false"
																											}
																										],
																										"storageId": "null"
																									}
																								],
																								"storageId": "15"
																							}
																						]
																					}
																				]
																			},
																			{
																				"funcName": "Storage State",
																				"returnValue": "",
																				"status": "",
																				"childrenList":[
																					{
																						"funcName": "ERC20",
																						"returnValue": "",
																						"status": "",
																						"childrenList":[
																							{
																								"funcName": "_balances[ERC20 (0x270e)]: 10",
																								"returnValue": "",
																								"status": "HAVOC",
																								"childrenList":[]
,
																								"changed": "false"
																							},
																							{
																								"funcName": "_balances[identity (0xffff)]: 0xcd98cb94f23b4265",
																								"returnValue": "",
																								"status": "HAVOC",
																								"childrenList":[]
,
																								"changed": "false"
																							}
																						],
																						"storageId": "null"
																					},
																					{
																						"funcName": "CurveTokenExample",
																						"returnValue": "",
																						"status": "",
																						"childrenList":[
																							{
																								"funcName": "_balances[ERC20 (0x270e)]: 1",
																								"returnValue": "",
																								"status": "HAVOC DEPENDENT",
																								"childrenList":[]
,
																								"changed": "false"
																							},
																							{
																								"funcName": "_totalSupply: 0x4563918244f40001",
																								"returnValue": "",
																								"status": "HAVOC DEPENDENT",
																								"childrenList":[]
,
																								"changed": "false"
																							}
																						],
																						"storageId": "null"
																					},
																					{
																						"funcName": "curve",
																						"returnValue": "",
																						"status": "",
																						"childrenList":[
																							{
																								"funcName": "_status: 2",
																								"returnValue": "",
																								"status": "CONCRETE",
																								"childrenList":[]
,
																								"changed": "false"
																							},
																							{
																								"funcName": "admin_balances[0]: 0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffd",
																								"returnValue": "",
																								"status": "HAVOC",
																								"childrenList":[]
,
																								"changed": "false"
																							},
																							{
																								"funcName": "admin_balances[1]: 3",
																								"returnValue": "",
																								"status": "HAVOC",
																								"childrenList":[]
,
																								"changed": "false"
																							},
																							{
																								"funcName": "coins_1: ERC20 (0x270e)",
																								"returnValue": "",
																								"status": "HAVOC",
																								"childrenList":[]
,
																								"changed": "false"
																							},
																							{
																								"funcName": "future_A: 0",
																								"returnValue": "",
																								"status": "HAVOC",
																								"childrenList":[]
,
																								"changed": "false"
																							},
																							{
																								"funcName": "lp_token: CurveTokenExample (0x270d)",
																								"returnValue": "",
																								"status": "HAVOC",
																								"childrenList":[]
,
																								"changed": "false"
																							},
																							{
																								"funcName": "solghost_return_func1: *",
																								"returnValue": "",
																								"status": "DONT CARE",
																								"childrenList":[]
,
																								"changed": "false"
																							},
																							{
																								"funcName": "solghost_trigger_check: *",
																								"returnValue": "",
																								"status": "DONT CARE",
																								"childrenList":[]
,
																								"changed": "false"
																							}
																						],
																						"storageId": "null"
																					}
																				],
																				"storageId": "16"
																			}
																		]
																	},
																	{
																		"funcName": "Apply hook store curve.solghost_return_func1 := newValue (old: oldValue)",
																		"returnValue": "",
																		"status": "",
																		"childrenList":[
																			{
																				"funcName": "With parameters:",
																				"returnValue": "",
																				"status": "",
																				"childrenList":[
																					{
																						"funcName": "newValue = 0x19b319729e47684c2",
																						"returnValue": "",
																						"status": "",
																						"childrenList":[]

																					},
																					{
																						"funcName": "oldValue = 0x0",
																						"returnValue": "",
																						"status": "",
																						"childrenList":[]

																					}
																				]
																			}
																		]
																	},
																	{
																		"funcName": "Store at curve.solghost_return_func1: 0x19b319729e47684c2",
																		"returnValue": "",
																		"status": "",
																		"childrenList":[]

																	},
																	{
																		"funcName": "Apply hook store curve.solghost_trigger_check := newValue (old: oldValue)",
																		"returnValue": "",
																		"status": "",
																		"childrenList":[
																			{
																				"funcName": "With parameters:",
																				"returnValue": "",
																				"status": "",
																				"childrenList":[
																					{
																						"funcName": "newValue = 0x1",
																						"returnValue": "",
																						"status": "",
																						"childrenList":[]

																					},
																					{
																						"funcName": "oldValue = 0x0",
																						"returnValue": "",
																						"status": "",
																						"childrenList":[]

																					}
																				]
																			}
																		]
																	},
																	{
																		"funcName": "Store at curve.solghost_trigger_check: true",
																		"returnValue": "",
																		"status": "",
																		"childrenList":[]

																	},
																	{
																		"funcName": "Storage State",
																		"returnValue": "",
																		"status": "",
																		"childrenList":[
																			{
																				"funcName": "ERC20",
																				"returnValue": "",
																				"status": "",
																				"childrenList":[
																					{
																						"funcName": "_balances[ERC20 (0x270e)]: 10",
																						"returnValue": "",
																						"status": "HAVOC",
																						"childrenList":[]
,
																						"changed": "false"
																					},
																					{
																						"funcName": "_balances[identity (0xffff)]: 0xcd98cb94f23b4265",
																						"returnValue": "",
																						"status": "HAVOC",
																						"childrenList":[]
,
																						"changed": "false"
																					}
																				],
																				"storageId": "null"
																			},
																			{
																				"funcName": "CurveTokenExample",
																				"returnValue": "",
																				"status": "",
																				"childrenList":[
																					{
																						"funcName": "_balances[ERC20 (0x270e)]: 1",
																						"returnValue": "",
																						"status": "HAVOC DEPENDENT",
																						"childrenList":[]
,
																						"changed": "false"
																					},
																					{
																						"funcName": "_totalSupply: 0x4563918244f40001",
																						"returnValue": "",
																						"status": "HAVOC DEPENDENT",
																						"childrenList":[]
,
																						"changed": "false"
																					}
																				],
																				"storageId": "null"
																			},
																			{
																				"funcName": "curve",
																				"returnValue": "",
																				"status": "",
																				"childrenList":[
																					{
																						"funcName": "_status: 2",
																						"returnValue": "",
																						"status": "CONCRETE",
																						"childrenList":[]
,
																						"changed": "false"
																					},
																					{
																						"funcName": "admin_balances[0]: 0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffd",
																						"returnValue": "",
																						"status": "HAVOC",
																						"childrenList":[]
,
																						"changed": "false"
																					},
																					{
																						"funcName": "admin_balances[1]: 3",
																						"returnValue": "",
																						"status": "HAVOC",
																						"childrenList":[]
,
																						"changed": "false"
																					},
																					{
																						"funcName": "coins_1: ERC20 (0x270e)",
																						"returnValue": "",
																						"status": "HAVOC",
																						"childrenList":[]
,
																						"changed": "false"
																					},
																					{
																						"funcName": "future_A: 0",
																						"returnValue": "",
																						"status": "HAVOC",
																						"childrenList":[]
,
																						"changed": "false"
																					},
																					{
																						"funcName": "lp_token: CurveTokenExample (0x270d)",
																						"returnValue": "",
																						"status": "HAVOC",
																						"childrenList":[]
,
																						"changed": "false"
																					},
																					{
																						"funcName": "solghost_return_func1: 0x19b319729e47684c2 (changed)",
																						"returnValue": "",
																						"status": "UNKNOWN",
																						"childrenList":[]
,
																						"changed": "true"
																					},
																					{
																						"funcName": "solghost_trigger_check: true (changed)",
																						"returnValue": "",
																						"status": "CONCRETE",
																						"childrenList":[]
,
																						"changed": "true"
																					}
																				],
																				"storageId": "null"
																			}
																		],
																		"storageId": "17"
																	}
																]
															}
														]
													},
													{
														"funcName": "Loop Iteration 2",
														"returnValue": "",
														"status": "",
														"childrenList":[
															{
																"funcName": "Load from curve.coins_1: ERC20 (0x270e)",
																"returnValue": "",
																"status": "",
																"childrenList":[]

															},
															{
																"funcName": "ERC20.transfer(to=ERC20 (0x270e), amount=0xcd98cb94f23b425b)",
																"returnValue": "true",
																"status": "SUCCESS",
																"childrenList":[
																	{
																		"funcName": "(internal) ERC20.transfer(to=ERC20 (0x270e), amount=0xcd98cb94f23b425b)",
																		"returnValue": "true",
																		"status": "",
																		"childrenList":[
																			{
																				"funcName": "(internal) Context._msgSender()",
																				"returnValue": "identity (0xffff)",
																				"status": "",
																				"childrenList":[
																					{
																						"funcName": "Storage State",
																						"returnValue": "",
																						"status": "",
																						"childrenList":[
																							{
																								"funcName": "ERC20",
																								"returnValue": "",
																								"status": "",
																								"childrenList":[
																									{
																										"funcName": "_balances[ERC20 (0x270e)]: 10",
																										"returnValue": "",
																										"status": "HAVOC",
																										"childrenList":[]
,
																										"changed": "false"
																									},
																									{
																										"funcName": "_balances[identity (0xffff)]: 0xcd98cb94f23b4265",
																										"returnValue": "",
																										"status": "HAVOC",
																										"childrenList":[]
,
																										"changed": "false"
																									}
																								],
																								"storageId": "null"
																							},
																							{
																								"funcName": "CurveTokenExample",
																								"returnValue": "",
																								"status": "",
																								"childrenList":[
																									{
																										"funcName": "_balances[ERC20 (0x270e)]: 1",
																										"returnValue": "",
																										"status": "HAVOC DEPENDENT",
																										"childrenList":[]
,
																										"changed": "false"
																									},
																									{
																										"funcName": "_totalSupply: 0x4563918244f40001",
																										"returnValue": "",
																										"status": "HAVOC DEPENDENT",
																										"childrenList":[]
,
																										"changed": "false"
																									}
																								],
																								"storageId": "null"
																							},
																							{
																								"funcName": "curve",
																								"returnValue": "",
																								"status": "",
																								"childrenList":[
																									{
																										"funcName": "_status: 2",
																										"returnValue": "",
																										"status": "CONCRETE",
																										"childrenList":[]
,
																										"changed": "false"
																									},
																									{
																										"funcName": "admin_balances[0]: 0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffd",
																										"returnValue": "",
																										"status": "HAVOC",
																										"childrenList":[]
,
																										"changed": "false"
																									},
																									{
																										"funcName": "admin_balances[1]: 3",
																										"returnValue": "",
																										"status": "HAVOC",
																										"childrenList":[]
,
																										"changed": "false"
																									},
																									{
																										"funcName": "coins_1: ERC20 (0x270e)",
																										"returnValue": "",
																										"status": "HAVOC",
																										"childrenList":[]
,
																										"changed": "false"
																									},
																									{
																										"funcName": "future_A: 0",
																										"returnValue": "",
																										"status": "HAVOC",
																										"childrenList":[]
,
																										"changed": "false"
																									},
																									{
																										"funcName": "lp_token: CurveTokenExample (0x270d)",
																										"returnValue": "",
																										"status": "HAVOC",
																										"childrenList":[]
,
																										"changed": "false"
																									},
																									{
																										"funcName": "solghost_return_func1: 0x19b319729e47684c2",
																										"returnValue": "",
																										"status": "UNKNOWN",
																										"childrenList":[]
,
																										"changed": "false"
																									},
																									{
																										"funcName": "solghost_trigger_check: true",
																										"returnValue": "",
																										"status": "CONCRETE",
																										"childrenList":[]
,
																										"changed": "false"
																									}
																								],
																								"storageId": "null"
																							}
																						],
																						"storageId": "18"
																					}
																				]
																			},
																			{
																				"funcName": "(internal) ERC20._transfer(from=identity (0xffff), to=ERC20 (0x270e), amount=0xcd98cb94f23b425b)",
																				"returnValue": "",
																				"status": "",
																				"childrenList":[
																					{
																						"funcName": "(internal) ERC20._update(from=identity (0xffff), to=ERC20 (0x270e), amount=0xcd98cb94f23b425b)",
																						"returnValue": "",
																						"status": "",
																						"childrenList":[
																							{
																								"funcName": "Load from ERC20._balances[identity (0xffff)]: 0xcd98cb94f23b4265",
																								"returnValue": "",
																								"status": "",
																								"childrenList":[]

																							},
																							{
																								"funcName": "Store at ERC20._balances[identity (0xffff)]: 10",
																								"returnValue": "",
																								"status": "",
																								"childrenList":[]

																							},
																							{
																								"funcName": "Load from ERC20._balances[ERC20 (0x270e)]: 10",
																								"returnValue": "",
																								"status": "",
																								"childrenList":[]

																							},
																							{
																								"funcName": "Store at ERC20._balances[ERC20 (0x270e)]: 0xcd98cb94f23b4265",
																								"returnValue": "",
																								"status": "",
																								"childrenList":[]

																							},
																							{
																								"funcName": "Storage State",
																								"returnValue": "",
																								"status": "",
																								"childrenList":[
																									{
																										"funcName": "ERC20",
																										"returnValue": "",
																										"status": "",
																										"childrenList":[
																											{
																												"funcName": "_balances[ERC20 (0x270e)]: 0xcd98cb94f23b4265 (changed)",
																												"returnValue": "",
																												"status": "HAVOC DEPENDENT",
																												"childrenList":[]
,
																												"changed": "true"
																											},
																											{
																												"funcName": "_balances[identity (0xffff)]: 10 (changed)",
																												"returnValue": "",
																												"status": "HAVOC DEPENDENT",
																												"childrenList":[]
,
																												"changed": "true"
																											}
																										],
																										"storageId": "null"
																									},
																									{
																										"funcName": "CurveTokenExample",
																										"returnValue": "",
																										"status": "",
																										"childrenList":[
																											{
																												"funcName": "_balances[ERC20 (0x270e)]: 1",
																												"returnValue": "",
																												"status": "HAVOC DEPENDENT",
																												"childrenList":[]
,
																												"changed": "false"
																											},
																											{
																												"funcName": "_totalSupply: 0x4563918244f40001",
																												"returnValue": "",
																												"status": "HAVOC DEPENDENT",
																												"childrenList":[]
,
																												"changed": "false"
																											}
																										],
																										"storageId": "null"
																									},
																									{
																										"funcName": "curve",
																										"returnValue": "",
																										"status": "",
																										"childrenList":[
																											{
																												"funcName": "_status: 2",
																												"returnValue": "",
																												"status": "CONCRETE",
																												"childrenList":[]
,
																												"changed": "false"
																											},
																											{
																												"funcName": "admin_balances[0]: 0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffd",
																												"returnValue": "",
																												"status": "HAVOC",
																												"childrenList":[]
,
																												"changed": "false"
																											},
																											{
																												"funcName": "admin_balances[1]: 3",
																												"returnValue": "",
																												"status": "HAVOC",
																												"childrenList":[]
,
																												"changed": "false"
																											},
																											{
																												"funcName": "coins_1: ERC20 (0x270e)",
																												"returnValue": "",
																												"status": "HAVOC",
																												"childrenList":[]
,
																												"changed": "false"
																											},
																											{
																												"funcName": "future_A: 0",
																												"returnValue": "",
																												"status": "HAVOC",
																												"childrenList":[]
,
																												"changed": "false"
																											},
																											{
																												"funcName": "lp_token: CurveTokenExample (0x270d)",
																												"returnValue": "",
																												"status": "HAVOC",
																												"childrenList":[]
,
																												"changed": "false"
																											},
																											{
																												"funcName": "solghost_return_func1: 0x19b319729e47684c2",
																												"returnValue": "",
																												"status": "UNKNOWN",
																												"childrenList":[]
,
																												"changed": "false"
																											},
																											{
																												"funcName": "solghost_trigger_check: true",
																												"returnValue": "",
																												"status": "CONCRETE",
																												"childrenList":[]
,
																												"changed": "false"
																											}
																										],
																										"storageId": "null"
																									}
																								],
																								"storageId": "19"
																							}
																						]
																					},
																					{
																						"funcName": "Storage State",
																						"returnValue": "",
																						"status": "",
																						"childrenList":[
																							{
																								"funcName": "ERC20",
																								"returnValue": "",
																								"status": "",
																								"childrenList":[
																									{
																										"funcName": "_balances[ERC20 (0x270e)]: 0xcd98cb94f23b4265",
																										"returnValue": "",
																										"status": "HAVOC DEPENDENT",
																										"childrenList":[]
,
																										"changed": "false"
																									},
																									{
																										"funcName": "_balances[identity (0xffff)]: 10",
																										"returnValue": "",
																										"status": "HAVOC DEPENDENT",
																										"childrenList":[]
,
																										"changed": "false"
																									}
																								],
																								"storageId": "null"
																							},
																							{
																								"funcName": "CurveTokenExample",
																								"returnValue": "",
																								"status": "",
																								"childrenList":[
																									{
																										"funcName": "_balances[ERC20 (0x270e)]: 1",
																										"returnValue": "",
																										"status": "HAVOC DEPENDENT",
																										"childrenList":[]
,
																										"changed": "false"
																									},
																									{
																										"funcName": "_totalSupply: 0x4563918244f40001",
																										"returnValue": "",
																										"status": "HAVOC DEPENDENT",
																										"childrenList":[]
,
																										"changed": "false"
																									}
																								],
																								"storageId": "null"
																							},
																							{
																								"funcName": "curve",
																								"returnValue": "",
																								"status": "",
																								"childrenList":[
																									{
																										"funcName": "_status: 2",
																										"returnValue": "",
																										"status": "CONCRETE",
																										"childrenList":[]
,
																										"changed": "false"
																									},
																									{
																										"funcName": "admin_balances[0]: 0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffd",
																										"returnValue": "",
																										"status": "HAVOC",
																										"childrenList":[]
,
																										"changed": "false"
																									},
																									{
																										"funcName": "admin_balances[1]: 3",
																										"returnValue": "",
																										"status": "HAVOC",
																										"childrenList":[]
,
																										"changed": "false"
																									},
																									{
																										"funcName": "coins_1: ERC20 (0x270e)",
																										"returnValue": "",
																										"status": "HAVOC",
																										"childrenList":[]
,
																										"changed": "false"
																									},
																									{
																										"funcName": "future_A: 0",
																										"returnValue": "",
																										"status": "HAVOC",
																										"childrenList":[]
,
																										"changed": "false"
																									},
																									{
																										"funcName": "lp_token: CurveTokenExample (0x270d)",
																										"returnValue": "",
																										"status": "HAVOC",
																										"childrenList":[]
,
																										"changed": "false"
																									},
																									{
																										"funcName": "solghost_return_func1: 0x19b319729e47684c2",
																										"returnValue": "",
																										"status": "UNKNOWN",
																										"childrenList":[]
,
																										"changed": "false"
																									},
																									{
																										"funcName": "solghost_trigger_check: true",
																										"returnValue": "",
																										"status": "CONCRETE",
																										"childrenList":[]
,
																										"changed": "false"
																									}
																								],
																								"storageId": "null"
																							}
																						],
																						"storageId": "20"
																					}
																				]
																			},
																			{
																				"funcName": "Storage State",
																				"returnValue": "",
																				"status": "",
																				"childrenList":[
																					{
																						"funcName": "ERC20",
																						"returnValue": "",
																						"status": "",
																						"childrenList":[
																							{
																								"funcName": "_balances[ERC20 (0x270e)]: 0xcd98cb94f23b4265",
																								"returnValue": "",
																								"status": "HAVOC DEPENDENT",
																								"childrenList":[]
,
																								"changed": "false"
																							},
																							{
																								"funcName": "_balances[identity (0xffff)]: 10",
																								"returnValue": "",
																								"status": "HAVOC DEPENDENT",
																								"childrenList":[]
,
																								"changed": "false"
																							}
																						],
																						"storageId": "null"
																					},
																					{
																						"funcName": "CurveTokenExample",
																						"returnValue": "",
																						"status": "",
																						"childrenList":[
																							{
																								"funcName": "_balances[ERC20 (0x270e)]: 1",
																								"returnValue": "",
																								"status": "HAVOC DEPENDENT",
																								"childrenList":[]
,
																								"changed": "false"
																							},
																							{
																								"funcName": "_totalSupply: 0x4563918244f40001",
																								"returnValue": "",
																								"status": "HAVOC DEPENDENT",
																								"childrenList":[]
,
																								"changed": "false"
																							}
																						],
																						"storageId": "null"
																					},
																					{
																						"funcName": "curve",
																						"returnValue": "",
																						"status": "",
																						"childrenList":[
																							{
																								"funcName": "_status: 2",
																								"returnValue": "",
																								"status": "CONCRETE",
																								"childrenList":[]
,
																								"changed": "false"
																							},
																							{
																								"funcName": "admin_balances[0]: 0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffd",
																								"returnValue": "",
																								"status": "HAVOC",
																								"childrenList":[]
,
																								"changed": "false"
																							},
																							{
																								"funcName": "admin_balances[1]: 3",
																								"returnValue": "",
																								"status": "HAVOC",
																								"childrenList":[]
,
																								"changed": "false"
																							},
																							{
																								"funcName": "coins_1: ERC20 (0x270e)",
																								"returnValue": "",
																								"status": "HAVOC",
																								"childrenList":[]
,
																								"changed": "false"
																							},
																							{
																								"funcName": "future_A: 0",
																								"returnValue": "",
																								"status": "HAVOC",
																								"childrenList":[]
,
																								"changed": "false"
																							},
																							{
																								"funcName": "lp_token: CurveTokenExample (0x270d)",
																								"returnValue": "",
																								"status": "HAVOC",
																								"childrenList":[]
,
																								"changed": "false"
																							},
																							{
																								"funcName": "solghost_return_func1: 0x19b319729e47684c2",
																								"returnValue": "",
																								"status": "UNKNOWN",
																								"childrenList":[]
,
																								"changed": "false"
																							},
																							{
																								"funcName": "solghost_trigger_check: true",
																								"returnValue": "",
																								"status": "CONCRETE",
																								"childrenList":[]
,
																								"changed": "false"
																							}
																						],
																						"storageId": "null"
																					}
																				],
																				"storageId": "21"
																			}
																		]
																	}
																]
															}
														]
													}
												]
											},
											{
												"funcName": "(internal) ReentrancyGuard._nonReentrantAfter()",
												"returnValue": "",
												"status": "",
												"childrenList":[
													{
														"funcName": "Store at curve._status: 1",
														"returnValue": "",
														"status": "",
														"childrenList":[]

													},
													{
														"funcName": "Storage State",
														"returnValue": "",
														"status": "",
														"childrenList":[
															{
																"funcName": "ERC20",
																"returnValue": "",
																"status": "",
																"childrenList":[
																	{
																		"funcName": "_balances[ERC20 (0x270e)]: 0xcd98cb94f23b4265",
																		"returnValue": "",
																		"status": "HAVOC DEPENDENT",
																		"childrenList":[]
,
																		"changed": "false"
																	},
																	{
																		"funcName": "_balances[identity (0xffff)]: 10",
																		"returnValue": "",
																		"status": "HAVOC DEPENDENT",
																		"childrenList":[]
,
																		"changed": "false"
																	}
																],
																"storageId": "null"
															},
															{
																"funcName": "CurveTokenExample",
																"returnValue": "",
																"status": "",
																"childrenList":[
																	{
																		"funcName": "_balances[ERC20 (0x270e)]: 1",
																		"returnValue": "",
																		"status": "HAVOC DEPENDENT",
																		"childrenList":[]
,
																		"changed": "false"
																	},
																	{
																		"funcName": "_totalSupply: 0x4563918244f40001",
																		"returnValue": "",
																		"status": "HAVOC DEPENDENT",
																		"childrenList":[]
,
																		"changed": "false"
																	}
																],
																"storageId": "null"
															},
															{
																"funcName": "curve",
																"returnValue": "",
																"status": "",
																"childrenList":[
																	{
																		"funcName": "_status: 1 (changed)",
																		"returnValue": "",
																		"status": "CONCRETE",
																		"childrenList":[]
,
																		"changed": "true"
																	},
																	{
																		"funcName": "admin_balances[0]: 0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffd",
																		"returnValue": "",
																		"status": "HAVOC",
																		"childrenList":[]
,
																		"changed": "false"
																	},
																	{
																		"funcName": "admin_balances[1]: 3",
																		"returnValue": "",
																		"status": "HAVOC",
																		"childrenList":[]
,
																		"changed": "false"
																	},
																	{
																		"funcName": "coins_1: ERC20 (0x270e)",
																		"returnValue": "",
																		"status": "HAVOC",
																		"childrenList":[]
,
																		"changed": "false"
																	},
																	{
																		"funcName": "future_A: 0",
																		"returnValue": "",
																		"status": "HAVOC",
																		"childrenList":[]
,
																		"changed": "false"
																	},
																	{
																		"funcName": "lp_token: CurveTokenExample (0x270d)",
																		"returnValue": "",
																		"status": "HAVOC",
																		"childrenList":[]
,
																		"changed": "false"
																	},
																	{
																		"funcName": "solghost_return_func1: 0x19b319729e47684c2",
																		"returnValue": "",
																		"status": "UNKNOWN",
																		"childrenList":[]
,
																		"changed": "false"
																	},
																	{
																		"funcName": "solghost_trigger_check: true",
																		"returnValue": "",
																		"status": "CONCRETE",
																		"childrenList":[]
,
																		"changed": "false"
																	}
																],
																"storageId": "null"
															}
														],
														"storageId": "22"
													}
												]
											},
											{
												"funcName": "unknown loop source code",
												"returnValue": "",
												"status": "",
												"childrenList":[
													{
														"funcName": "Loop Iteration 1",
														"returnValue": "",
														"status": "",
														"childrenList":[]

													},
													{
														"funcName": "Loop Iteration 2",
														"returnValue": "",
														"status": "",
														"childrenList":[]

													}
												]
											}
										]
									}
								]
							},
							{
								"funcName": "require after_func1 == curve.getVirtualPrice(e_external)",
								"returnValue": "",
								"status": "",
								"childrenList":[
									{
										"funcName": "curve.getVirtualPrice()",
										"returnValue": "17",
										"status": "SUCCESS",
										"childrenList":[
											{
												"funcName": "sender: identity (0xffff); receiver: identity (0xffff); transferred amount: 0",
												"returnValue": "",
												"status": "TRANSFER",
												"childrenList":[
													{
														"funcName": "Load from sender.balance: 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff (MAX_UINT256)",
														"returnValue": "",
														"status": "",
														"childrenList":[]

													},
													{
														"funcName": "Store at sender.balance: 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff (MAX_UINT256)",
														"returnValue": "",
														"status": "",
														"childrenList":[]

													},
													{
														"funcName": "Load from receiver.balance: 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff (MAX_UINT256)",
														"returnValue": "",
														"status": "",
														"childrenList":[]

													},
													{
														"funcName": "Store at receiver.balance: 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff (MAX_UINT256)",
														"returnValue": "",
														"status": "",
														"childrenList":[]

													}
												]
											},
											{
												"funcName": "(internal) curve.getVirtualPrice()",
												"returnValue": "17",
												"status": "",
												"childrenList":[
													{
														"funcName": "Load from curve.admin_balances[0]: 0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffd",
														"returnValue": "",
														"status": "",
														"childrenList":[]

													},
													{
														"funcName": "Load from curve.admin_balances[1]: 3",
														"returnValue": "",
														"status": "",
														"childrenList":[]

													},
													{
														"funcName": "Load from curve.coins_1: ERC20 (0x270e)",
														"returnValue": "",
														"status": "",
														"childrenList":[]

													},
													{
														"funcName": "ERC20.balanceOf(account=identity (0xffff))",
														"returnValue": "10",
														"status": "SUCCESS",
														"childrenList":[
															{
																"funcName": "(internal) ERC20.balanceOf(account=identity (0xffff))",
																"returnValue": "10",
																"status": "",
																"childrenList":[
																	{
																		"funcName": "Load from ERC20._balances[identity (0xffff)]: 10",
																		"returnValue": "",
																		"status": "",
																		"childrenList":[]

																	},
																	{
																		"funcName": "Storage State",
																		"returnValue": "",
																		"status": "",
																		"childrenList":[
																			{
																				"funcName": "ERC20",
																				"returnValue": "",
																				"status": "",
																				"childrenList":[
																					{
																						"funcName": "_balances[ERC20 (0x270e)]: 0xcd98cb94f23b4265",
																						"returnValue": "",
																						"status": "HAVOC DEPENDENT",
																						"childrenList":[]
,
																						"changed": "false"
																					},
																					{
																						"funcName": "_balances[identity (0xffff)]: 10",
																						"returnValue": "",
																						"status": "HAVOC DEPENDENT",
																						"childrenList":[]
,
																						"changed": "false"
																					}
																				],
																				"storageId": "null"
																			},
																			{
																				"funcName": "CurveTokenExample",
																				"returnValue": "",
																				"status": "",
																				"childrenList":[
																					{
																						"funcName": "_balances[ERC20 (0x270e)]: 1",
																						"returnValue": "",
																						"status": "HAVOC DEPENDENT",
																						"childrenList":[]
,
																						"changed": "false"
																					},
																					{
																						"funcName": "_totalSupply: 0x4563918244f40001",
																						"returnValue": "",
																						"status": "HAVOC DEPENDENT",
																						"childrenList":[]
,
																						"changed": "false"
																					}
																				],
																				"storageId": "null"
																			},
																			{
																				"funcName": "curve",
																				"returnValue": "",
																				"status": "",
																				"childrenList":[
																					{
																						"funcName": "_status: 1",
																						"returnValue": "",
																						"status": "CONCRETE",
																						"childrenList":[]
,
																						"changed": "false"
																					},
																					{
																						"funcName": "admin_balances[0]: 0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffd",
																						"returnValue": "",
																						"status": "HAVOC",
																						"childrenList":[]
,
																						"changed": "false"
																					},
																					{
																						"funcName": "admin_balances[1]: 3",
																						"returnValue": "",
																						"status": "HAVOC",
																						"childrenList":[]
,
																						"changed": "false"
																					},
																					{
																						"funcName": "coins_1: ERC20 (0x270e)",
																						"returnValue": "",
																						"status": "HAVOC",
																						"childrenList":[]
,
																						"changed": "false"
																					},
																					{
																						"funcName": "future_A: 0",
																						"returnValue": "",
																						"status": "HAVOC",
																						"childrenList":[]
,
																						"changed": "false"
																					},
																					{
																						"funcName": "lp_token: CurveTokenExample (0x270d)",
																						"returnValue": "",
																						"status": "HAVOC",
																						"childrenList":[]
,
																						"changed": "false"
																					},
																					{
																						"funcName": "solghost_return_func1: 0x19b319729e47684c2",
																						"returnValue": "",
																						"status": "UNKNOWN",
																						"childrenList":[]
,
																						"changed": "false"
																					},
																					{
																						"funcName": "solghost_trigger_check: true",
																						"returnValue": "",
																						"status": "CONCRETE",
																						"childrenList":[]
,
																						"changed": "false"
																					}
																				],
																				"storageId": "null"
																			}
																		],
																		"storageId": "23"
																	}
																]
															}
														]
													},
													{
														"funcName": "(internal) curve._A()",
														"returnValue": "0",
														"status": "",
														"childrenList":[
															{
																"funcName": "Load from curve.future_A: 0",
																"returnValue": "",
																"status": "",
																"childrenList":[]

															},
															{
																"funcName": "Storage State",
																"returnValue": "",
																"status": "",
																"childrenList":[
																	{
																		"funcName": "ERC20",
																		"returnValue": "",
																		"status": "",
																		"childrenList":[
																			{
																				"funcName": "_balances[ERC20 (0x270e)]: 0xcd98cb94f23b4265",
																				"returnValue": "",
																				"status": "HAVOC DEPENDENT",
																				"childrenList":[]
,
																				"changed": "false"
																			},
																			{
																				"funcName": "_balances[identity (0xffff)]: 10",
																				"returnValue": "",
																				"status": "HAVOC DEPENDENT",
																				"childrenList":[]
,
																				"changed": "false"
																			}
																		],
																		"storageId": "null"
																	},
																	{
																		"funcName": "CurveTokenExample",
																		"returnValue": "",
																		"status": "",
																		"childrenList":[
																			{
																				"funcName": "_balances[ERC20 (0x270e)]: 1",
																				"returnValue": "",
																				"status": "HAVOC DEPENDENT",
																				"childrenList":[]
,
																				"changed": "false"
																			},
																			{
																				"funcName": "_totalSupply: 0x4563918244f40001",
																				"returnValue": "",
																				"status": "HAVOC DEPENDENT",
																				"childrenList":[]
,
																				"changed": "false"
																			}
																		],
																		"storageId": "null"
																	},
																	{
																		"funcName": "curve",
																		"returnValue": "",
																		"status": "",
																		"childrenList":[
																			{
																				"funcName": "_status: 1",
																				"returnValue": "",
																				"status": "CONCRETE",
																				"childrenList":[]
,
																				"changed": "false"
																			},
																			{
																				"funcName": "admin_balances[0]: 0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffd",
																				"returnValue": "",
																				"status": "HAVOC",
																				"childrenList":[]
,
																				"changed": "false"
																			},
																			{
																				"funcName": "admin_balances[1]: 3",
																				"returnValue": "",
																				"status": "HAVOC",
																				"childrenList":[]
,
																				"changed": "false"
																			},
																			{
																				"funcName": "coins_1: ERC20 (0x270e)",
																				"returnValue": "",
																				"status": "HAVOC",
																				"childrenList":[]
,
																				"changed": "false"
																			},
																			{
																				"funcName": "future_A: 0",
																				"returnValue": "",
																				"status": "HAVOC",
																				"childrenList":[]
,
																				"changed": "false"
																			},
																			{
																				"funcName": "lp_token: CurveTokenExample (0x270d)",
																				"returnValue": "",
																				"status": "HAVOC",
																				"childrenList":[]
,
																				"changed": "false"
																			},
																			{
																				"funcName": "solghost_return_func1: 0x19b319729e47684c2",
																				"returnValue": "",
																				"status": "UNKNOWN",
																				"childrenList":[]
,
																				"changed": "false"
																			},
																			{
																				"funcName": "solghost_trigger_check: true",
																				"returnValue": "",
																				"status": "CONCRETE",
																				"childrenList":[]
,
																				"changed": "false"
																			}
																		],
																		"storageId": "null"
																	}
																],
																"storageId": "24"
															}
														]
													},
													{
														"funcName": "unknown loop source code",
														"returnValue": "",
														"status": "",
														"childrenList":[
															{
																"funcName": "Loop Iteration 1",
																"returnValue": "",
																"status": "",
																"childrenList":[]

															},
															{
																"funcName": "Loop Iteration 2",
																"returnValue": "",
																"status": "",
																"childrenList":[]

															}
														]
													},
													{
														"funcName": "curve.get_D(xp=[0=2, 1=7], amp=0)",
														"returnValue": "9",
														"status": "SUCCESS",
														"childrenList":[
															{
																"funcName": "unknown loop source code",
																"returnValue": "",
																"status": "",
																"childrenList":[
																	{
																		"funcName": "Loop Iteration 1",
																		"returnValue": "",
																		"status": "",
																		"childrenList":[]

																	},
																	{
																		"funcName": "Loop Iteration 2",
																		"returnValue": "",
																		"status": "",
																		"childrenList":[]

																	}
																]
															},
															{
																"funcName": "(internal) curve.get_D(xp=uint256[2], amp=0)",
																"returnValue": "9",
																"status": "",
																"childrenList":[
																	{
																		"funcName": "Storage State",
																		"returnValue": "",
																		"status": "",
																		"childrenList":[
																			{
																				"funcName": "ERC20",
																				"returnValue": "",
																				"status": "",
																				"childrenList":[
																					{
																						"funcName": "_balances[ERC20 (0x270e)]: 0xcd98cb94f23b4265",
																						"returnValue": "",
																						"status": "HAVOC DEPENDENT",
																						"childrenList":[]
,
																						"changed": "false"
																					},
																					{
																						"funcName": "_balances[identity (0xffff)]: 10",
																						"returnValue": "",
																						"status": "HAVOC DEPENDENT",
																						"childrenList":[]
,
																						"changed": "false"
																					}
																				],
																				"storageId": "null"
																			},
																			{
																				"funcName": "CurveTokenExample",
																				"returnValue": "",
																				"status": "",
																				"childrenList":[
																					{
																						"funcName": "_balances[ERC20 (0x270e)]: 1",
																						"returnValue": "",
																						"status": "HAVOC DEPENDENT",
																						"childrenList":[]
,
																						"changed": "false"
																					},
																					{
																						"funcName": "_totalSupply: 0x4563918244f40001",
																						"returnValue": "",
																						"status": "HAVOC DEPENDENT",
																						"childrenList":[]
,
																						"changed": "false"
																					}
																				],
																				"storageId": "null"
																			},
																			{
																				"funcName": "curve",
																				"returnValue": "",
																				"status": "",
																				"childrenList":[
																					{
																						"funcName": "_status: 1",
																						"returnValue": "",
																						"status": "CONCRETE",
																						"childrenList":[]
,
																						"changed": "false"
																					},
																					{
																						"funcName": "admin_balances[0]: 0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffd",
																						"returnValue": "",
																						"status": "HAVOC",
																						"childrenList":[]
,
																						"changed": "false"
																					},
																					{
																						"funcName": "admin_balances[1]: 3",
																						"returnValue": "",
																						"status": "HAVOC",
																						"childrenList":[]
,
																						"changed": "false"
																					},
																					{
																						"funcName": "coins_1: ERC20 (0x270e)",
																						"returnValue": "",
																						"status": "HAVOC",
																						"childrenList":[]
,
																						"changed": "false"
																					},
																					{
																						"funcName": "future_A: 0",
																						"returnValue": "",
																						"status": "HAVOC",
																						"childrenList":[]
,
																						"changed": "false"
																					},
																					{
																						"funcName": "lp_token: CurveTokenExample (0x270d)",
																						"returnValue": "",
																						"status": "HAVOC",
																						"childrenList":[]
,
																						"changed": "false"
																					},
																					{
																						"funcName": "solghost_return_func1: 0x19b319729e47684c2",
																						"returnValue": "",
																						"status": "UNKNOWN",
																						"childrenList":[]
,
																						"changed": "false"
																					},
																					{
																						"funcName": "solghost_trigger_check: true",
																						"returnValue": "",
																						"status": "CONCRETE",
																						"childrenList":[]
,
																						"changed": "false"
																					}
																				],
																				"storageId": "null"
																			}
																		],
																		"storageId": "25"
																	}
																]
															}
														]
													},
													{
														"funcName": "Load from curve.lp_token: CurveTokenExample (0x270d)",
														"returnValue": "",
														"status": "",
														"childrenList":[]

													},
													{
														"funcName": "CurveTokenExample.totalSupply()",
														"returnValue": "0x4563918244f40001",
														"status": "SUCCESS",
														"childrenList":[
															{
																"funcName": "(internal) CurveTokenExample.totalSupply()",
																"returnValue": "0x4563918244f40001",
																"status": "",
																"childrenList":[
																	{
																		"funcName": "Load from CurveTokenExample._totalSupply: 0x4563918244f40001",
																		"returnValue": "",
																		"status": "",
																		"childrenList":[]

																	},
																	{
																		"funcName": "Storage State",
																		"returnValue": "",
																		"status": "",
																		"childrenList":[
																			{
																				"funcName": "ERC20",
																				"returnValue": "",
																				"status": "",
																				"childrenList":[
																					{
																						"funcName": "_balances[ERC20 (0x270e)]: 0xcd98cb94f23b4265",
																						"returnValue": "",
																						"status": "HAVOC DEPENDENT",
																						"childrenList":[]
,
																						"changed": "false"
																					},
																					{
																						"funcName": "_balances[identity (0xffff)]: 10",
																						"returnValue": "",
																						"status": "HAVOC DEPENDENT",
																						"childrenList":[]
,
																						"changed": "false"
																					}
																				],
																				"storageId": "null"
																			},
																			{
																				"funcName": "CurveTokenExample",
																				"returnValue": "",
																				"status": "",
																				"childrenList":[
																					{
																						"funcName": "_balances[ERC20 (0x270e)]: 1",
																						"returnValue": "",
																						"status": "HAVOC DEPENDENT",
																						"childrenList":[]
,
																						"changed": "false"
																					},
																					{
																						"funcName": "_totalSupply: 0x4563918244f40001",
																						"returnValue": "",
																						"status": "HAVOC DEPENDENT",
																						"childrenList":[]
,
																						"changed": "false"
																					}
																				],
																				"storageId": "null"
																			},
																			{
																				"funcName": "curve",
																				"returnValue": "",
																				"status": "",
																				"childrenList":[
																					{
																						"funcName": "_status: 1",
																						"returnValue": "",
																						"status": "CONCRETE",
																						"childrenList":[]
,
																						"changed": "false"
																					},
																					{
																						"funcName": "admin_balances[0]: 0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffd",
																						"returnValue": "",
																						"status": "HAVOC",
																						"childrenList":[]
,
																						"changed": "false"
																					},
																					{
																						"funcName": "admin_balances[1]: 3",
																						"returnValue": "",
																						"status": "HAVOC",
																						"childrenList":[]
,
																						"changed": "false"
																					},
																					{
																						"funcName": "coins_1: ERC20 (0x270e)",
																						"returnValue": "",
																						"status": "HAVOC",
																						"childrenList":[]
,
																						"changed": "false"
																					},
																					{
																						"funcName": "future_A: 0",
																						"returnValue": "",
																						"status": "HAVOC",
																						"childrenList":[]
,
																						"changed": "false"
																					},
																					{
																						"funcName": "lp_token: CurveTokenExample (0x270d)",
																						"returnValue": "",
																						"status": "HAVOC",
																						"childrenList":[]
,
																						"changed": "false"
																					},
																					{
																						"funcName": "solghost_return_func1: 0x19b319729e47684c2",
																						"returnValue": "",
																						"status": "UNKNOWN",
																						"childrenList":[]
,
																						"changed": "false"
																					},
																					{
																						"funcName": "solghost_trigger_check: true",
																						"returnValue": "",
																						"status": "CONCRETE",
																						"childrenList":[]
,
																						"changed": "false"
																					}
																				],
																				"storageId": "null"
																			}
																		],
																		"storageId": "26"
																	}
																]
															}
														]
													},
													{
														"funcName": "Storage State",
														"returnValue": "",
														"status": "",
														"childrenList":[
															{
																"funcName": "ERC20",
																"returnValue": "",
																"status": "",
																"childrenList":[
																	{
																		"funcName": "_balances[ERC20 (0x270e)]: 0xcd98cb94f23b4265",
																		"returnValue": "",
																		"status": "HAVOC DEPENDENT",
																		"childrenList":[]
,
																		"changed": "false"
																	},
																	{
																		"funcName": "_balances[identity (0xffff)]: 10",
																		"returnValue": "",
																		"status": "HAVOC DEPENDENT",
																		"childrenList":[]
,
																		"changed": "false"
																	}
																],
																"storageId": "null"
															},
															{
																"funcName": "CurveTokenExample",
																"returnValue": "",
																"status": "",
																"childrenList":[
																	{
																		"funcName": "_balances[ERC20 (0x270e)]: 1",
																		"returnValue": "",
																		"status": "HAVOC DEPENDENT",
																		"childrenList":[]
,
																		"changed": "false"
																	},
																	{
																		"funcName": "_totalSupply: 0x4563918244f40001",
																		"returnValue": "",
																		"status": "HAVOC DEPENDENT",
																		"childrenList":[]
,
																		"changed": "false"
																	}
																],
																"storageId": "null"
															},
															{
																"funcName": "curve",
																"returnValue": "",
																"status": "",
																"childrenList":[
																	{
																		"funcName": "_status: 1",
																		"returnValue": "",
																		"status": "CONCRETE",
																		"childrenList":[]
,
																		"changed": "false"
																	},
																	{
																		"funcName": "admin_balances[0]: 0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffd",
																		"returnValue": "",
																		"status": "HAVOC",
																		"childrenList":[]
,
																		"changed": "false"
																	},
																	{
																		"funcName": "admin_balances[1]: 3",
																		"returnValue": "",
																		"status": "HAVOC",
																		"childrenList":[]
,
																		"changed": "false"
																	},
																	{
																		"funcName": "coins_1: ERC20 (0x270e)",
																		"returnValue": "",
																		"status": "HAVOC",
																		"childrenList":[]
,
																		"changed": "false"
																	},
																	{
																		"funcName": "future_A: 0",
																		"returnValue": "",
																		"status": "HAVOC",
																		"childrenList":[]
,
																		"changed": "false"
																	},
																	{
																		"funcName": "lp_token: CurveTokenExample (0x270d)",
																		"returnValue": "",
																		"status": "HAVOC",
																		"childrenList":[]
,
																		"changed": "false"
																	},
																	{
																		"funcName": "solghost_return_func1: 0x19b319729e47684c2",
																		"returnValue": "",
																		"status": "UNKNOWN",
																		"childrenList":[]
,
																		"changed": "false"
																	},
																	{
																		"funcName": "solghost_trigger_check: true",
																		"returnValue": "",
																		"status": "CONCRETE",
																		"childrenList":[]
,
																		"changed": "false"
																	}
																],
																"storageId": "null"
															}
														],
														"storageId": "27"
													}
												]
											}
										]
									},
									{
										"funcName": "after_func1 == curve.getVirtualPrice(e_external)",
										"returnValue": "true",
										"status": "",
										"childrenList":[
											{
												"funcName": "after_func1",
												"returnValue": "17",
												"status": "",
												"childrenList":[]

											},
											{
												"funcName": "curve.getVirtualPrice(e_external)",
												"returnValue": "*",
												"status": "",
												"childrenList":[]

											}
										]
									}
								]
							},
							{
								"funcName": "assert cond",
								"returnValue": "",
								"status": "",
								"childrenList":[
									{
										"funcName": "Storage State",
										"returnValue": "",
										"status": "",
										"childrenList":[
											{
												"funcName": "ERC20",
												"returnValue": "",
												"status": "",
												"childrenList":[
													{
														"funcName": "_balances[ERC20 (0x270e)]: 0xcd98cb94f23b4265",
														"returnValue": "",
														"status": "HAVOC DEPENDENT",
														"childrenList":[]
,
														"changed": "false"
													},
													{
														"funcName": "_balances[identity (0xffff)]: 10",
														"returnValue": "",
														"status": "HAVOC DEPENDENT",
														"childrenList":[]
,
														"changed": "false"
													}
												],
												"storageId": "null"
											},
											{
												"funcName": "CurveTokenExample",
												"returnValue": "",
												"status": "",
												"childrenList":[
													{
														"funcName": "_balances[ERC20 (0x270e)]: 1",
														"returnValue": "",
														"status": "HAVOC DEPENDENT",
														"childrenList":[]
,
														"changed": "false"
													},
													{
														"funcName": "_totalSupply: 0x4563918244f40001",
														"returnValue": "",
														"status": "HAVOC DEPENDENT",
														"childrenList":[]
,
														"changed": "false"
													}
												],
												"storageId": "null"
											},
											{
												"funcName": "curve",
												"returnValue": "",
												"status": "",
												"childrenList":[
													{
														"funcName": "_status: 1",
														"returnValue": "",
														"status": "CONCRETE",
														"childrenList":[]
,
														"changed": "false"
													},
													{
														"funcName": "admin_balances[0]: 0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffd",
														"returnValue": "",
														"status": "HAVOC",
														"childrenList":[]
,
														"changed": "false"
													},
													{
														"funcName": "admin_balances[1]: 3",
														"returnValue": "",
														"status": "HAVOC",
														"childrenList":[]
,
														"changed": "false"
													},
													{
														"funcName": "coins_1: ERC20 (0x270e)",
														"returnValue": "",
														"status": "HAVOC",
														"childrenList":[]
,
														"changed": "false"
													},
													{
														"funcName": "future_A: 0",
														"returnValue": "",
														"status": "HAVOC",
														"childrenList":[]
,
														"changed": "false"
													},
													{
														"funcName": "lp_token: CurveTokenExample (0x270d)",
														"returnValue": "",
														"status": "HAVOC",
														"childrenList":[]
,
														"changed": "false"
													},
													{
														"funcName": "solghost_return_func1: 0x19b319729e47684c2",
														"returnValue": "",
														"status": "UNKNOWN",
														"childrenList":[]
,
														"changed": "false"
													},
													{
														"funcName": "solghost_trigger_check: true",
														"returnValue": "",
														"status": "CONCRETE",
														"childrenList":[]
,
														"changed": "false"
													}
												],
												"storageId": "null"
											}
										],
										"storageId": "28"
									}
								]
							}
						]
					}
				}
,				{
					 "tableRow": {
						"funcName": "_balances(uint256)",
						"result": "SUCCESS",
						"time": "2",
						"graph_link": "",
						"preoptimized_link": "PreoptimizedRule-no_read_only_reentrancy-_balancesLPU256RP.html",
						"presimplified_link": "PresimplifiedRule-no_read_only_reentrancy-_balancesLPU256RP.html",
						"prelastopt_link": "PrelastoptRule-no_read_only_reentrancy-_balancesLPU256RP.html",
						"presolver_link": "PresolverRule-no_read_only_reentrancy-_balancesLPU256RP.html"
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
						"funcName": "coins_0()",
						"result": "SUCCESS",
						"time": "2",
						"graph_link": "",
						"preoptimized_link": "PreoptimizedRule-no_read_only_reentrancy-coins_0LPRP.html",
						"presimplified_link": "PresimplifiedRule-no_read_only_reentrancy-coins_0LPRP.html",
						"prelastopt_link": "PrelastoptRule-no_read_only_reentrancy-coins_0LPRP.html",
						"presolver_link": "PresolverRule-no_read_only_reentrancy-coins_0LPRP.html"
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
						"funcName": "coins_1()",
						"result": "SUCCESS",
						"time": "2",
						"graph_link": "",
						"preoptimized_link": "PreoptimizedRule-no_read_only_reentrancy-coins_1LPRP.html",
						"presimplified_link": "PresimplifiedRule-no_read_only_reentrancy-coins_1LPRP.html",
						"prelastopt_link": "PrelastoptRule-no_read_only_reentrancy-coins_1LPRP.html",
						"presolver_link": "PresolverRule-no_read_only_reentrancy-coins_1LPRP.html"
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
						"funcName": "func1_caller()",
						"result": "SUCCESS",
						"time": "1",
						"graph_link": "",
						"preoptimized_link": "PreoptimizedRule-no_read_only_reentrancy-func1_callerLPRP.html",
						"presimplified_link": "PresimplifiedRule-no_read_only_reentrancy-func1_callerLPRP.html",
						"prelastopt_link": "PrelastoptRule-no_read_only_reentrancy-func1_callerLPRP.html",
						"presolver_link": "PresolverRule-no_read_only_reentrancy-func1_callerLPRP.html"
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
						"funcName": "getVirtualPrice()",
						"result": "SUCCESS",
						"time": "0",
						"graph_link": "",
						"preoptimized_link": "PreoptimizedRule-no_read_only_reentrancy-getVirtualPriceLPRP.html",
						"presimplified_link": "PresimplifiedRule-no_read_only_reentrancy-getVirtualPriceLPRP.html",
						"prelastopt_link": "PrelastoptRule-no_read_only_reentrancy-getVirtualPriceLPRP.html",
						"presolver_link": "PresolverRule-no_read_only_reentrancy-getVirtualPriceLPRP.html"
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
						"funcName": "get_D(uint256[2],uint256)",
						"result": "SUCCESS",
						"time": "3",
						"graph_link": "",
						"preoptimized_link": "PreoptimizedRule-no_read_only_reentrancy-get_DLPU256LB2RBCU256RP.html",
						"presimplified_link": "PresimplifiedRule-no_read_only_reentrancy-get_DLPU256LB2RBCU256RP.html",
						"prelastopt_link": "PrelastoptRule-no_read_only_reentrancy-get_DLPU256LB2RBCU256RP.html",
						"presolver_link": "PresolverRule-no_read_only_reentrancy-get_DLPU256LB2RBCU256RP.html"
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
						"funcName": "lp_token()",
						"result": "SUCCESS",
						"time": "3",
						"graph_link": "",
						"preoptimized_link": "PreoptimizedRule-no_read_only_reentrancy-lp_tokenLPRP.html",
						"presimplified_link": "PresimplifiedRule-no_read_only_reentrancy-lp_tokenLPRP.html",
						"prelastopt_link": "PrelastoptRule-no_read_only_reentrancy-lp_tokenLPRP.html",
						"presolver_link": "PresolverRule-no_read_only_reentrancy-lp_tokenLPRP.html"
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
						"funcName": "solghost_executeFunction1()",
						"result": "SUCCESS",
						"time": "1",
						"graph_link": "",
						"preoptimized_link": "PreoptimizedRule-no_read_only_reentrancy-solghost_executeFunction1LPRP.html",
						"presimplified_link": "PresimplifiedRule-no_read_only_reentrancy-solghost_executeFunction1LPRP.html",
						"prelastopt_link": "PrelastoptRule-no_read_only_reentrancy-solghost_executeFunction1LPRP.html",
						"presolver_link": "PresolverRule-no_read_only_reentrancy-solghost_executeFunction1LPRP.html"
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
						"funcName": "solghost_executeFunction2()",
						"result": "SUCCESS",
						"time": "3",
						"graph_link": "",
						"preoptimized_link": "PreoptimizedRule-no_read_only_reentrancy-solghost_executeFunction2LPRP.html",
						"presimplified_link": "PresimplifiedRule-no_read_only_reentrancy-solghost_executeFunction2LPRP.html",
						"prelastopt_link": "PrelastoptRule-no_read_only_reentrancy-solghost_executeFunction2LPRP.html",
						"presolver_link": "PresolverRule-no_read_only_reentrancy-solghost_executeFunction2LPRP.html"
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
						"funcName": "solghost_return_func1()",
						"result": "SUCCESS",
						"time": "2",
						"graph_link": "",
						"preoptimized_link": "PreoptimizedRule-no_read_only_reentrancy-solghost_return_func1LPRP.html",
						"presimplified_link": "PresimplifiedRule-no_read_only_reentrancy-solghost_return_func1LPRP.html",
						"prelastopt_link": "PrelastoptRule-no_read_only_reentrancy-solghost_return_func1LPRP.html",
						"presolver_link": "PresolverRule-no_read_only_reentrancy-solghost_return_func1LPRP.html"
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
						"name": "CurveTokenExample",
						"address": "ce4604a0000000000000000000000014",
						"pre_state": "{}",
						"methodsNames":[
							"constructor()",
							"constructor(string,string)",
							"symbol()",
							"name()",
							"decimals()",
							"transferFrom(address,address,uint256)",
							"burnFrom(address,uint256)",
							"balanceOf(address)",
							"increaseAllowance(address,uint256)",
							"approve(address,uint256)",
							"decreaseAllowance(address,uint256)",
							"mint(address,uint256)",
							"transfer(address,uint256)",
							"totalSupply()",
							"allowance(address,address)"
						]
					}
				},
				{
					 "tableRow": {
						"name": "ERC20",
						"address": "ce4604a0000000000000000000000004",
						"pre_state": "{}",
						"methodsNames":[
							"constructor(string,string)",
							"symbol()",
							"name()",
							"decimals()",
							"transferFrom(address,address,uint256)",
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
						"name": "curve",
						"address": "ce4604a0000000000000000000000017",
						"pre_state": "{11=274184521717934524641157099916833587204, 12=274184521717934524641157099916833587220}",
						"methodsNames":[
							"constructor(address,address)",
							"coins_1()",
							"solghost_executeFunction2()",
							"solghost_return_func1()",
							"lp_token()",
							"_balances(uint256)",
							"coins_0()",
							"get_D(uint256[2],uint256)",
							"solghost_executeFunction1()",
							"func1_caller()",
							"getVirtualPrice()",
							"remove_liquidity(uint256,uint256[2])"
						]
					}
				}
			]
		}
	}