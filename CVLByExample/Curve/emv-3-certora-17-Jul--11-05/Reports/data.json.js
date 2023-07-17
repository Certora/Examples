data = {
	"contractName": "Curve",
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
						"ruleName": "viewReentrancy",
						"result": "FAIL",
						"time": "39",
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
			"ruleName": "viewReentrancy",
			"tableBody":[
				{
					 "tableRow": {
						"funcName": "remove_liquidity(uint256,uint256[2])",
						"result": "FAIL",
						"time": "39",
						"graph_link": "Report-viewReentrancy-remove_liquidityLPU256CU256LB2RBRP-example1.html",
						"preoptimized_link": "PreoptimizedRule-viewReentrancy-remove_liquidityLPU256CU256LB2RBRP.html",
						"presimplified_link": "PresimplifiedRule-viewReentrancy-remove_liquidityLPU256CU256LB2RBRP.html",
						"prelastopt_link": "PrelastoptRule-viewReentrancy-remove_liquidityLPU256CU256LB2RBRP.html",
						"presolver_link": "PresolverRule-viewReentrancy-remove_liquidityLPU256CU256LB2RBRP.html"
					},
					 "variables": {
						"lastReverted": "false",
						"fcalldataarg": "bytemap initialized but unknown",
						"f.selector": "0x5b36389c",
						"f.isPure": "false",
						"f.isView": "false",
						"f.isPayable": "false",
						"f.numberOfArguments": "2",
						"f.isFallback": "false",
						"fenv.msg.sender": "0x18160dde",
						"fenv.msg.value": "0",
						"fenv.tx.origin": "0",
						"fenv.block.coinbase": "0xffffffffffffffffffffffffffffffffffffffff (MAX_EVM_ADDRESS)",
						"fenv.block.difficulty": "0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff (MAX_UINT256)",
						"fenv.block.gaslimit": "0",
						"fenv.block.number": "0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff (MAX_UINT256)",
						"fenv.block.timestamp": "0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff (MAX_UINT256)",
						"behaveSameAtSink_0_call0": "false",
						"Curve": "Curve (0x18160ddc)",
						"CurveTokenExample": "CurveTokenExample (0xfffffffffffffffffffffffffffffffffffffffe)",
						"ERC20": "ERC20 (0x70a08230)"
					},
					"assertMessage":[
						"Possible Read-Only Reentrancy weakness at external call site at file contracts/Curve.sol, line 168"
					],
					 "failureCauses": {
						"expr": "((!true||(!lastReverted&&(0x20==0x20)&&(((0x8ac7230489e80000*(tacCalldatabuf!!1153@49[0x4]+tacCalldatabuf!!1153@49[0x24]))/CANON106!!106)==((0x8ac7230489e80000*(tacCalldatabuf!!1649@46[0x4]+tacCalldatabuf!!1649@46[0x24]))/(CANON106!!106-tacCalldatabuf@28[0x4])))))&&(!true||(true&&(0x20==0x20)&&((CANON26!!212&lt;&lt;0xe0)==(CANON26!!212&lt;&lt;0xe0))))&&(!true||(true&&(0x20==0x20)&&(CANON22!!211==CANON22!!211)))&&(!true||(true&&(0x20==0x20)&&(CANON21!!210==CANON21!!210)))&&(!true||(true&&(0x20==0x20)&&((CANON17!!209&lt;&lt;0xe0)==(CANON17!!209&lt;&lt;0xe0))))&&(!true||(true&&(0x20==0x20)&&(CANON13!!208==CANON13!!208)))&&(!true||(true&&(0x20==0x20)&&(CANON8!!281==CANON8!!281)))&&(!true||(!lastReverted&&(0x40==0x40)&&(tacReturndata!!1375[R136]==tacReturndata!!1904[R136])))&&(!true||(!lastReverted&&(0x20==0x20)&&((tacCalldatabuf!!1455@25[0x4]+tacCalldatabuf!!1455@25[0x24])==(tacCalldatabuf!!1983@27[0x4]+tacCalldatabuf!!1983@27[0x24])))))||((!true||(!lastReverted&&(0x20==0x20)&&(((0x8ac7230489e80000*(tacCalldatabuf!!2174@42[0x4]+tacCalldatabuf!!2174@42[0x24]))/(CANON106!!106-tacCalldatabuf@28[0x4]))==((0x8ac7230489e80000*(tacCalldatabuf!!1649@46[0x4]+tacCalldatabuf!!1649@46[0x24]))/(CANON106!!106-tacCalldatabuf@28[0x4])))))&&(!true||(true&&(0x20==0x20)&&((CANON26!!212&lt;&lt;0xe0)==(CANON26!!212&lt;&lt;0xe0))))&&(!true||(true&&(0x20==0x20)&&(CANON22!!211==CANON22!!211)))&&(!true||(true&&(0x20==0x20)&&((safe_math_narrow:bif(safe_math_promotion:bif(safe_math_narrow:bif(safe_math_promotion:bif(tacCalldatabuf!!796@34[0x4])+int safe_math_promotion:bif(tacCalldatabuf!!796@34[0x24])))*int 0x8ac7230489e80000)/(CANON106!!106-tacCalldatabuf@28[0x4]))==CANON21!!210)))&&(!true||(true&&(0x20==0x20)&&((CANON17!!209&lt;&lt;0xe0)==(CANON17!!209&lt;&lt;0xe0))))&&(!true||(true&&(0x20==0x20)&&(CANON13!!208==CANON13!!208)))&&(!true||(true&&(0x20==0x20)&&(CANON8!!281==CANON8!!281)))&&(!true||(!lastReverted&&(0x40==0x40)&&(tacReturndata!!2396[R137]==tacReturndata!!1904[R137])))&&(!true||(!lastReverted&&(0x20==0x20)&&((tacCalldatabuf!!2458@26[0x4]+tacCalldatabuf!!2458@26[0x24])==(tacCalldatabuf!!1983@27[0x4]+tacCalldatabuf!!1983@27[0x24])))))"
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
									"caller": "Curve.remove_liquidity(uint256,uint256[2])",
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
						"funcName": "viewReentrancy(f=remove_liquidity(uint256,uint256[2]), fenv=*struct* fenv, fcalldataarg=unknown type)",
						"returnValue": "",
						"status": "",
						"childrenList":[
							{
								"funcName": "Storage State",
								"returnValue": "",
								"status": "",
								"childrenList":[
									{
										"funcName": "Curve",
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
												"funcName": "admin_balances[0]: 0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffc",
												"returnValue": "",
												"status": "HAVOC",
												"childrenList":[]
,
												"changed": "false"
											},
											{
												"funcName": "admin_balances[1]: 0",
												"returnValue": "",
												"status": "HAVOC",
												"childrenList":[]
,
												"changed": "false"
											},
											{
												"funcName": "coins_0: 0",
												"returnValue": "",
												"status": "HAVOC",
												"childrenList":[]
,
												"changed": "false"
											},
											{
												"funcName": "coins_1: ERC20 (0x70a08230)",
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
												"funcName": "lp_token: CurveTokenExample (0xfffffffffffffffffffffffffffffffffffffffe)",
												"returnValue": "",
												"status": "HAVOC",
												"childrenList":[]
,
												"changed": "false"
											},
											{
												"funcName": "solghost_executeFunction1: -0x100",
												"returnValue": "",
												"status": "HAVOC",
												"childrenList":[]
,
												"changed": "false"
											},
											{
												"funcName": "solghost_executeFunction2: -0x100",
												"returnValue": "",
												"status": "HAVOC",
												"childrenList":[]
,
												"changed": "false"
											},
											{
												"funcName": "solghost_return_func1: 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff (MAX_UINT256)",
												"returnValue": "",
												"status": "HAVOC",
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
									},
									{
										"funcName": "CurveTokenExample",
										"returnValue": "",
										"status": "",
										"childrenList":[
											{
												"funcName": "_balances[0x18160dde]: 0x555555555555555555555555555555555555555555555555555555555555554b",
												"returnValue": "",
												"status": "HAVOC",
												"childrenList":[]
,
												"changed": "false"
											},
											{
												"funcName": "_totalSupply: 0x555555555555555555555555555555555555555555555555555555555555514b",
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
										"funcName": "ERC20",
										"returnValue": "",
										"status": "",
										"childrenList":[
											{
												"funcName": "_balances[Curve (0x18160ddc)]: 0",
												"returnValue": "",
												"status": "HAVOC",
												"childrenList":[]
,
												"changed": "false"
											},
											{
												"funcName": "_balances[0x18160dde]: 0",
												"returnValue": "",
												"status": "HAVOC",
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
								"funcName": "Curve.get_D(xp=[], amp=0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff (MAX_UINT256))",
								"returnValue": "0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff (MAX_UINT256)",
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
										"funcName": "(internal) Curve.get_D(xp=uint256[2], amp=0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff (MAX_UINT256))",
										"returnValue": "0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff (MAX_UINT256)",
										"status": "",
										"childrenList":[
											{
												"funcName": "Storage State",
												"returnValue": "",
												"status": "",
												"childrenList":[
													{
														"funcName": "Curve",
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
																"funcName": "admin_balances[0]: 0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffc",
																"returnValue": "",
																"status": "HAVOC",
																"childrenList":[]
,
																"changed": "false"
															},
															{
																"funcName": "admin_balances[1]: 0",
																"returnValue": "",
																"status": "HAVOC",
																"childrenList":[]
,
																"changed": "false"
															},
															{
																"funcName": "coins_0: 0",
																"returnValue": "",
																"status": "HAVOC",
																"childrenList":[]
,
																"changed": "false"
															},
															{
																"funcName": "coins_1: ERC20 (0x70a08230)",
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
																"funcName": "lp_token: CurveTokenExample (0xfffffffffffffffffffffffffffffffffffffffe)",
																"returnValue": "",
																"status": "HAVOC",
																"childrenList":[]
,
																"changed": "false"
															},
															{
																"funcName": "solghost_executeFunction1: -0x100",
																"returnValue": "",
																"status": "HAVOC",
																"childrenList":[]
,
																"changed": "false"
															},
															{
																"funcName": "solghost_executeFunction2: -0x100",
																"returnValue": "",
																"status": "HAVOC",
																"childrenList":[]
,
																"changed": "false"
															},
															{
																"funcName": "solghost_return_func1: 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff (MAX_UINT256)",
																"returnValue": "",
																"status": "HAVOC",
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
													},
													{
														"funcName": "CurveTokenExample",
														"returnValue": "",
														"status": "",
														"childrenList":[
															{
																"funcName": "_balances[0x18160dde]: 0x555555555555555555555555555555555555555555555555555555555555554b",
																"returnValue": "",
																"status": "HAVOC",
																"childrenList":[]
,
																"changed": "false"
															},
															{
																"funcName": "_totalSupply: 0x555555555555555555555555555555555555555555555555555555555555514b",
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
														"funcName": "ERC20",
														"returnValue": "",
														"status": "",
														"childrenList":[
															{
																"funcName": "_balances[Curve (0x18160ddc)]: 0",
																"returnValue": "",
																"status": "HAVOC",
																"childrenList":[]
,
																"changed": "false"
															},
															{
																"funcName": "_balances[0x18160dde]: 0",
																"returnValue": "",
																"status": "HAVOC",
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
								"funcName": "Curve._balances(_value=0)",
								"returnValue": "[]",
								"status": "SUCCESS",
								"childrenList":[
									{
										"funcName": "Load from Curve.admin_balances[0]: 0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffc",
										"returnValue": "",
										"status": "",
										"childrenList":[]

									},
									{
										"funcName": "Load from Curve.admin_balances[1]: 0",
										"returnValue": "",
										"status": "",
										"childrenList":[]

									},
									{
										"funcName": "Load from Curve.coins_1: ERC20 (0x70a08230)",
										"returnValue": "",
										"status": "",
										"childrenList":[]

									},
									{
										"funcName": "ERC20.balanceOf(account=Curve (0x18160ddc))",
										"returnValue": "0",
										"status": "SUCCESS",
										"childrenList":[
											{
												"funcName": "(internal) ERC20.balanceOf(account=Curve (0x18160ddc))",
												"returnValue": "0",
												"status": "",
												"childrenList":[
													{
														"funcName": "Load from ERC20._balances[Curve (0x18160ddc)]: 0",
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
																"funcName": "Curve",
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
																		"funcName": "admin_balances[0]: 0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffc",
																		"returnValue": "",
																		"status": "HAVOC",
																		"childrenList":[]
,
																		"changed": "false"
																	},
																	{
																		"funcName": "admin_balances[1]: 0",
																		"returnValue": "",
																		"status": "HAVOC",
																		"childrenList":[]
,
																		"changed": "false"
																	},
																	{
																		"funcName": "coins_0: 0",
																		"returnValue": "",
																		"status": "HAVOC",
																		"childrenList":[]
,
																		"changed": "false"
																	},
																	{
																		"funcName": "coins_1: ERC20 (0x70a08230)",
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
																		"funcName": "lp_token: CurveTokenExample (0xfffffffffffffffffffffffffffffffffffffffe)",
																		"returnValue": "",
																		"status": "HAVOC",
																		"childrenList":[]
,
																		"changed": "false"
																	},
																	{
																		"funcName": "solghost_executeFunction1: -0x100",
																		"returnValue": "",
																		"status": "HAVOC",
																		"childrenList":[]
,
																		"changed": "false"
																	},
																	{
																		"funcName": "solghost_executeFunction2: -0x100",
																		"returnValue": "",
																		"status": "HAVOC",
																		"childrenList":[]
,
																		"changed": "false"
																	},
																	{
																		"funcName": "solghost_return_func1: 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff (MAX_UINT256)",
																		"returnValue": "",
																		"status": "HAVOC",
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
															},
															{
																"funcName": "CurveTokenExample",
																"returnValue": "",
																"status": "",
																"childrenList":[
																	{
																		"funcName": "_balances[0x18160dde]: 0x555555555555555555555555555555555555555555555555555555555555554b",
																		"returnValue": "",
																		"status": "HAVOC",
																		"childrenList":[]
,
																		"changed": "false"
																	},
																	{
																		"funcName": "_totalSupply: 0x555555555555555555555555555555555555555555555555555555555555514b",
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
																"funcName": "ERC20",
																"returnValue": "",
																"status": "",
																"childrenList":[
																	{
																		"funcName": "_balances[Curve (0x18160ddc)]: 0",
																		"returnValue": "",
																		"status": "HAVOC",
																		"childrenList":[]
,
																		"changed": "false"
																	},
																	{
																		"funcName": "_balances[0x18160dde]: 0",
																		"returnValue": "",
																		"status": "HAVOC",
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
							},
							{
								"funcName": "Curve.coins_0()",
								"returnValue": "0",
								"status": "SUCCESS",
								"childrenList":[
									{
										"funcName": "Load from Curve.coins_0: 0",
										"returnValue": "",
										"status": "",
										"childrenList":[]

									}
								]
							},
							{
								"funcName": "Curve.lp_token()",
								"returnValue": "CurveTokenExample (0xfffffffffffffffffffffffffffffffffffffffe)",
								"status": "SUCCESS",
								"childrenList":[
									{
										"funcName": "Load from Curve.lp_token: CurveTokenExample (0xfffffffffffffffffffffffffffffffffffffffe)",
										"returnValue": "",
										"status": "",
										"childrenList":[]

									}
								]
							},
							{
								"funcName": "Curve.solghost_executeFunction2()",
								"returnValue": "0xffffffff00",
								"status": "SUCCESS",
								"childrenList":[
									{
										"funcName": "Load from Curve.solghost_executeFunction2: -0x100",
										"returnValue": "",
										"status": "",
										"childrenList":[]

									}
								]
							},
							{
								"funcName": "Curve.solghost_return_func1()",
								"returnValue": "0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff (MAX_UINT256)",
								"status": "SUCCESS",
								"childrenList":[
									{
										"funcName": "Load from Curve.solghost_return_func1: 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff (MAX_UINT256)",
										"returnValue": "",
										"status": "",
										"childrenList":[]

									}
								]
							},
							{
								"funcName": "Curve.coins_1()",
								"returnValue": "ERC20 (0x70a08230)",
								"status": "SUCCESS",
								"childrenList":[
									{
										"funcName": "Load from Curve.coins_1: ERC20 (0x70a08230)",
										"returnValue": "",
										"status": "",
										"childrenList":[]

									}
								]
							},
							{
								"funcName": "Curve.solghost_executeFunction1()",
								"returnValue": "0xffffffff00",
								"status": "SUCCESS",
								"childrenList":[
									{
										"funcName": "Load from Curve.solghost_executeFunction1: -0x100",
										"returnValue": "",
										"status": "",
										"childrenList":[]

									}
								]
							},
							{
								"funcName": "Curve.getVirtualPrice()",
								"returnValue": "0",
								"status": "SUCCESS",
								"childrenList":[
									{
										"funcName": "(internal) Curve.getVirtualPrice()",
										"returnValue": "0",
										"status": "",
										"childrenList":[
											{
												"funcName": "Load from Curve.admin_balances[0]: 0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffc",
												"returnValue": "",
												"status": "",
												"childrenList":[]

											},
											{
												"funcName": "Load from Curve.admin_balances[1]: 0",
												"returnValue": "",
												"status": "",
												"childrenList":[]

											},
											{
												"funcName": "Load from Curve.coins_1: ERC20 (0x70a08230)",
												"returnValue": "",
												"status": "",
												"childrenList":[]

											},
											{
												"funcName": "ERC20.balanceOf(account=Curve (0x18160ddc))",
												"returnValue": "0",
												"status": "SUCCESS",
												"childrenList":[
													{
														"funcName": "(internal) ERC20.balanceOf(account=Curve (0x18160ddc))",
														"returnValue": "0",
														"status": "",
														"childrenList":[
															{
																"funcName": "Load from ERC20._balances[Curve (0x18160ddc)]: 0",
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
																		"funcName": "Curve",
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
																				"funcName": "admin_balances[0]: 0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffc",
																				"returnValue": "",
																				"status": "HAVOC",
																				"childrenList":[]
,
																				"changed": "false"
																			},
																			{
																				"funcName": "admin_balances[1]: 0",
																				"returnValue": "",
																				"status": "HAVOC",
																				"childrenList":[]
,
																				"changed": "false"
																			},
																			{
																				"funcName": "coins_0: 0",
																				"returnValue": "",
																				"status": "HAVOC",
																				"childrenList":[]
,
																				"changed": "false"
																			},
																			{
																				"funcName": "coins_1: ERC20 (0x70a08230)",
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
																				"funcName": "lp_token: CurveTokenExample (0xfffffffffffffffffffffffffffffffffffffffe)",
																				"returnValue": "",
																				"status": "HAVOC",
																				"childrenList":[]
,
																				"changed": "false"
																			},
																			{
																				"funcName": "solghost_executeFunction1: -0x100",
																				"returnValue": "",
																				"status": "HAVOC",
																				"childrenList":[]
,
																				"changed": "false"
																			},
																			{
																				"funcName": "solghost_executeFunction2: -0x100",
																				"returnValue": "",
																				"status": "HAVOC",
																				"childrenList":[]
,
																				"changed": "false"
																			},
																			{
																				"funcName": "solghost_return_func1: 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff (MAX_UINT256)",
																				"returnValue": "",
																				"status": "HAVOC",
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
																	},
																	{
																		"funcName": "CurveTokenExample",
																		"returnValue": "",
																		"status": "",
																		"childrenList":[
																			{
																				"funcName": "_balances[0x18160dde]: 0x555555555555555555555555555555555555555555555555555555555555554b",
																				"returnValue": "",
																				"status": "HAVOC",
																				"childrenList":[]
,
																				"changed": "false"
																			},
																			{
																				"funcName": "_totalSupply: 0x555555555555555555555555555555555555555555555555555555555555514b",
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
																		"funcName": "ERC20",
																		"returnValue": "",
																		"status": "",
																		"childrenList":[
																			{
																				"funcName": "_balances[Curve (0x18160ddc)]: 0",
																				"returnValue": "",
																				"status": "HAVOC",
																				"childrenList":[]
,
																				"changed": "false"
																			},
																			{
																				"funcName": "_balances[0x18160dde]: 0",
																				"returnValue": "",
																				"status": "HAVOC",
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
												"funcName": "(internal) Curve._A()",
												"returnValue": "0",
												"status": "",
												"childrenList":[
													{
														"funcName": "Load from Curve.future_A: 0",
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
																"funcName": "Curve",
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
																		"funcName": "admin_balances[0]: 0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffc",
																		"returnValue": "",
																		"status": "HAVOC",
																		"childrenList":[]
,
																		"changed": "false"
																	},
																	{
																		"funcName": "admin_balances[1]: 0",
																		"returnValue": "",
																		"status": "HAVOC",
																		"childrenList":[]
,
																		"changed": "false"
																	},
																	{
																		"funcName": "coins_0: 0",
																		"returnValue": "",
																		"status": "HAVOC",
																		"childrenList":[]
,
																		"changed": "false"
																	},
																	{
																		"funcName": "coins_1: ERC20 (0x70a08230)",
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
																		"funcName": "lp_token: CurveTokenExample (0xfffffffffffffffffffffffffffffffffffffffe)",
																		"returnValue": "",
																		"status": "HAVOC",
																		"childrenList":[]
,
																		"changed": "false"
																	},
																	{
																		"funcName": "solghost_executeFunction1: -0x100",
																		"returnValue": "",
																		"status": "HAVOC",
																		"childrenList":[]
,
																		"changed": "false"
																	},
																	{
																		"funcName": "solghost_executeFunction2: -0x100",
																		"returnValue": "",
																		"status": "HAVOC",
																		"childrenList":[]
,
																		"changed": "false"
																	},
																	{
																		"funcName": "solghost_return_func1: 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff (MAX_UINT256)",
																		"returnValue": "",
																		"status": "HAVOC",
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
															},
															{
																"funcName": "CurveTokenExample",
																"returnValue": "",
																"status": "",
																"childrenList":[
																	{
																		"funcName": "_balances[0x18160dde]: 0x555555555555555555555555555555555555555555555555555555555555554b",
																		"returnValue": "",
																		"status": "HAVOC",
																		"childrenList":[]
,
																		"changed": "false"
																	},
																	{
																		"funcName": "_totalSupply: 0x555555555555555555555555555555555555555555555555555555555555514b",
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
																"funcName": "ERC20",
																"returnValue": "",
																"status": "",
																"childrenList":[
																	{
																		"funcName": "_balances[Curve (0x18160ddc)]: 0",
																		"returnValue": "",
																		"status": "HAVOC",
																		"childrenList":[]
,
																		"changed": "false"
																	},
																	{
																		"funcName": "_balances[0x18160dde]: 0",
																		"returnValue": "",
																		"status": "HAVOC",
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
												"funcName": "Curve.get_D(xp=[0=3, 1=0], amp=0)",
												"returnValue": "3",
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
														"funcName": "(internal) Curve.get_D(xp=uint256[2], amp=0)",
														"returnValue": "3",
														"status": "",
														"childrenList":[
															{
																"funcName": "Storage State",
																"returnValue": "",
																"status": "",
																"childrenList":[
																	{
																		"funcName": "Curve",
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
																				"funcName": "admin_balances[0]: 0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffc",
																				"returnValue": "",
																				"status": "HAVOC",
																				"childrenList":[]
,
																				"changed": "false"
																			},
																			{
																				"funcName": "admin_balances[1]: 0",
																				"returnValue": "",
																				"status": "HAVOC",
																				"childrenList":[]
,
																				"changed": "false"
																			},
																			{
																				"funcName": "coins_0: 0",
																				"returnValue": "",
																				"status": "HAVOC",
																				"childrenList":[]
,
																				"changed": "false"
																			},
																			{
																				"funcName": "coins_1: ERC20 (0x70a08230)",
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
																				"funcName": "lp_token: CurveTokenExample (0xfffffffffffffffffffffffffffffffffffffffe)",
																				"returnValue": "",
																				"status": "HAVOC",
																				"childrenList":[]
,
																				"changed": "false"
																			},
																			{
																				"funcName": "solghost_executeFunction1: -0x100",
																				"returnValue": "",
																				"status": "HAVOC",
																				"childrenList":[]
,
																				"changed": "false"
																			},
																			{
																				"funcName": "solghost_executeFunction2: -0x100",
																				"returnValue": "",
																				"status": "HAVOC",
																				"childrenList":[]
,
																				"changed": "false"
																			},
																			{
																				"funcName": "solghost_return_func1: 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff (MAX_UINT256)",
																				"returnValue": "",
																				"status": "HAVOC",
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
																	},
																	{
																		"funcName": "CurveTokenExample",
																		"returnValue": "",
																		"status": "",
																		"childrenList":[
																			{
																				"funcName": "_balances[0x18160dde]: 0x555555555555555555555555555555555555555555555555555555555555554b",
																				"returnValue": "",
																				"status": "HAVOC",
																				"childrenList":[]
,
																				"changed": "false"
																			},
																			{
																				"funcName": "_totalSupply: 0x555555555555555555555555555555555555555555555555555555555555514b",
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
																		"funcName": "ERC20",
																		"returnValue": "",
																		"status": "",
																		"childrenList":[
																			{
																				"funcName": "_balances[Curve (0x18160ddc)]: 0",
																				"returnValue": "",
																				"status": "HAVOC",
																				"childrenList":[]
,
																				"changed": "false"
																			},
																			{
																				"funcName": "_balances[0x18160dde]: 0",
																				"returnValue": "",
																				"status": "HAVOC",
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
												"funcName": "Load from Curve.lp_token: CurveTokenExample (0xfffffffffffffffffffffffffffffffffffffffe)",
												"returnValue": "",
												"status": "",
												"childrenList":[]

											},
											{
												"funcName": "CurveTokenExample.totalSupply()",
												"returnValue": "0x555555555555555555555555555555555555555555555555555555555555514b",
												"status": "SUCCESS",
												"childrenList":[
													{
														"funcName": "(internal) CurveTokenExample.totalSupply()",
														"returnValue": "0x555555555555555555555555555555555555555555555555555555555555514b",
														"status": "",
														"childrenList":[
															{
																"funcName": "Load from CurveTokenExample._totalSupply: 0x555555555555555555555555555555555555555555555555555555555555514b",
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
																		"funcName": "Curve",
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
																				"funcName": "admin_balances[0]: 0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffc",
																				"returnValue": "",
																				"status": "HAVOC",
																				"childrenList":[]
,
																				"changed": "false"
																			},
																			{
																				"funcName": "admin_balances[1]: 0",
																				"returnValue": "",
																				"status": "HAVOC",
																				"childrenList":[]
,
																				"changed": "false"
																			},
																			{
																				"funcName": "coins_0: 0",
																				"returnValue": "",
																				"status": "HAVOC",
																				"childrenList":[]
,
																				"changed": "false"
																			},
																			{
																				"funcName": "coins_1: ERC20 (0x70a08230)",
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
																				"funcName": "lp_token: CurveTokenExample (0xfffffffffffffffffffffffffffffffffffffffe)",
																				"returnValue": "",
																				"status": "HAVOC",
																				"childrenList":[]
,
																				"changed": "false"
																			},
																			{
																				"funcName": "solghost_executeFunction1: -0x100",
																				"returnValue": "",
																				"status": "HAVOC",
																				"childrenList":[]
,
																				"changed": "false"
																			},
																			{
																				"funcName": "solghost_executeFunction2: -0x100",
																				"returnValue": "",
																				"status": "HAVOC",
																				"childrenList":[]
,
																				"changed": "false"
																			},
																			{
																				"funcName": "solghost_return_func1: 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff (MAX_UINT256)",
																				"returnValue": "",
																				"status": "HAVOC",
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
																	},
																	{
																		"funcName": "CurveTokenExample",
																		"returnValue": "",
																		"status": "",
																		"childrenList":[
																			{
																				"funcName": "_balances[0x18160dde]: 0x555555555555555555555555555555555555555555555555555555555555554b",
																				"returnValue": "",
																				"status": "HAVOC",
																				"childrenList":[]
,
																				"changed": "false"
																			},
																			{
																				"funcName": "_totalSupply: 0x555555555555555555555555555555555555555555555555555555555555514b",
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
																		"funcName": "ERC20",
																		"returnValue": "",
																		"status": "",
																		"childrenList":[
																			{
																				"funcName": "_balances[Curve (0x18160ddc)]: 0",
																				"returnValue": "",
																				"status": "HAVOC",
																				"childrenList":[]
,
																				"changed": "false"
																			},
																			{
																				"funcName": "_balances[0x18160dde]: 0",
																				"returnValue": "",
																				"status": "HAVOC",
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
													}
												]
											},
											{
												"funcName": "Storage State",
												"returnValue": "",
												"status": "",
												"childrenList":[
													{
														"funcName": "Curve",
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
																"funcName": "admin_balances[0]: 0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffc",
																"returnValue": "",
																"status": "HAVOC",
																"childrenList":[]
,
																"changed": "false"
															},
															{
																"funcName": "admin_balances[1]: 0",
																"returnValue": "",
																"status": "HAVOC",
																"childrenList":[]
,
																"changed": "false"
															},
															{
																"funcName": "coins_0: 0",
																"returnValue": "",
																"status": "HAVOC",
																"childrenList":[]
,
																"changed": "false"
															},
															{
																"funcName": "coins_1: ERC20 (0x70a08230)",
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
																"funcName": "lp_token: CurveTokenExample (0xfffffffffffffffffffffffffffffffffffffffe)",
																"returnValue": "",
																"status": "HAVOC",
																"childrenList":[]
,
																"changed": "false"
															},
															{
																"funcName": "solghost_executeFunction1: -0x100",
																"returnValue": "",
																"status": "HAVOC",
																"childrenList":[]
,
																"changed": "false"
															},
															{
																"funcName": "solghost_executeFunction2: -0x100",
																"returnValue": "",
																"status": "HAVOC",
																"childrenList":[]
,
																"changed": "false"
															},
															{
																"funcName": "solghost_return_func1: 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff (MAX_UINT256)",
																"returnValue": "",
																"status": "HAVOC",
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
													},
													{
														"funcName": "CurveTokenExample",
														"returnValue": "",
														"status": "",
														"childrenList":[
															{
																"funcName": "_balances[0x18160dde]: 0x555555555555555555555555555555555555555555555555555555555555554b",
																"returnValue": "",
																"status": "HAVOC",
																"childrenList":[]
,
																"changed": "false"
															},
															{
																"funcName": "_totalSupply: 0x555555555555555555555555555555555555555555555555555555555555514b",
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
														"funcName": "ERC20",
														"returnValue": "",
														"status": "",
														"childrenList":[
															{
																"funcName": "_balances[Curve (0x18160ddc)]: 0",
																"returnValue": "",
																"status": "HAVOC",
																"childrenList":[]
,
																"changed": "false"
															},
															{
																"funcName": "_balances[0x18160dde]: 0",
																"returnValue": "",
																"status": "HAVOC",
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
								"funcName": "Curve.f(fenv, fcalldataarg)",
								"returnValue": "",
								"status": "",
								"childrenList":[
									{
										"funcName": "Curve.remove_liquidity(_amount=0x555555555555555555555555555555555555555555555555555555555555554b, _min_amounts=[])",
										"returnValue": "[]",
										"status": "SUCCESS",
										"childrenList":[
											{
												"funcName": "sender: 0x18160dde; receiver: Curve (0x18160ddc); transferred amount: 0",
												"returnValue": "",
												"status": "TRANSFER",
												"childrenList":[
													{
														"funcName": "Load from sender.balance: 0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffc",
														"returnValue": "",
														"status": "",
														"childrenList":[]

													},
													{
														"funcName": "Store at sender.balance: 0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffc",
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
														"funcName": "Load from Curve._status: 0",
														"returnValue": "",
														"status": "",
														"childrenList":[]

													},
													{
														"funcName": "Store at Curve._status: 2",
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
																"funcName": "Curve",
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
																		"funcName": "admin_balances[0]: 0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffc",
																		"returnValue": "",
																		"status": "HAVOC",
																		"childrenList":[]
,
																		"changed": "false"
																	},
																	{
																		"funcName": "admin_balances[1]: 0",
																		"returnValue": "",
																		"status": "HAVOC",
																		"childrenList":[]
,
																		"changed": "false"
																	},
																	{
																		"funcName": "coins_0: 0",
																		"returnValue": "",
																		"status": "HAVOC",
																		"childrenList":[]
,
																		"changed": "false"
																	},
																	{
																		"funcName": "coins_1: ERC20 (0x70a08230)",
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
																		"funcName": "lp_token: CurveTokenExample (0xfffffffffffffffffffffffffffffffffffffffe)",
																		"returnValue": "",
																		"status": "HAVOC",
																		"childrenList":[]
,
																		"changed": "false"
																	},
																	{
																		"funcName": "solghost_executeFunction1: -0x100",
																		"returnValue": "",
																		"status": "HAVOC",
																		"childrenList":[]
,
																		"changed": "false"
																	},
																	{
																		"funcName": "solghost_executeFunction2: -0x100",
																		"returnValue": "",
																		"status": "HAVOC",
																		"childrenList":[]
,
																		"changed": "false"
																	},
																	{
																		"funcName": "solghost_return_func1: 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff (MAX_UINT256)",
																		"returnValue": "",
																		"status": "HAVOC",
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
															},
															{
																"funcName": "CurveTokenExample",
																"returnValue": "",
																"status": "",
																"childrenList":[
																	{
																		"funcName": "_balances[0x18160dde]: 0x555555555555555555555555555555555555555555555555555555555555554b",
																		"returnValue": "",
																		"status": "HAVOC",
																		"childrenList":[]
,
																		"changed": "false"
																	},
																	{
																		"funcName": "_totalSupply: 0x555555555555555555555555555555555555555555555555555555555555514b",
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
																"funcName": "ERC20",
																"returnValue": "",
																"status": "",
																"childrenList":[
																	{
																		"funcName": "_balances[Curve (0x18160ddc)]: 0",
																		"returnValue": "",
																		"status": "HAVOC",
																		"childrenList":[]
,
																		"changed": "false"
																	},
																	{
																		"funcName": "_balances[0x18160dde]: 0",
																		"returnValue": "",
																		"status": "HAVOC",
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
											},
											{
												"funcName": "Load from Curve.admin_balances[0]: 0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffc",
												"returnValue": "",
												"status": "",
												"childrenList":[]

											},
											{
												"funcName": "Load from Curve.admin_balances[1]: 0",
												"returnValue": "",
												"status": "",
												"childrenList":[]

											},
											{
												"funcName": "Load from Curve.coins_1: ERC20 (0x70a08230)",
												"returnValue": "",
												"status": "",
												"childrenList":[]

											},
											{
												"funcName": "ERC20.balanceOf(account=Curve (0x18160ddc))",
												"returnValue": "0",
												"status": "SUCCESS",
												"childrenList":[
													{
														"funcName": "(internal) ERC20.balanceOf(account=Curve (0x18160ddc))",
														"returnValue": "0",
														"status": "",
														"childrenList":[
															{
																"funcName": "Load from ERC20._balances[Curve (0x18160ddc)]: 0",
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
																		"funcName": "Curve",
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
																				"funcName": "admin_balances[0]: 0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffc",
																				"returnValue": "",
																				"status": "HAVOC",
																				"childrenList":[]
,
																				"changed": "false"
																			},
																			{
																				"funcName": "admin_balances[1]: 0",
																				"returnValue": "",
																				"status": "HAVOC",
																				"childrenList":[]
,
																				"changed": "false"
																			},
																			{
																				"funcName": "coins_0: 0",
																				"returnValue": "",
																				"status": "HAVOC",
																				"childrenList":[]
,
																				"changed": "false"
																			},
																			{
																				"funcName": "coins_1: ERC20 (0x70a08230)",
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
																				"funcName": "lp_token: CurveTokenExample (0xfffffffffffffffffffffffffffffffffffffffe)",
																				"returnValue": "",
																				"status": "HAVOC",
																				"childrenList":[]
,
																				"changed": "false"
																			},
																			{
																				"funcName": "solghost_executeFunction1: -0x100",
																				"returnValue": "",
																				"status": "HAVOC",
																				"childrenList":[]
,
																				"changed": "false"
																			},
																			{
																				"funcName": "solghost_executeFunction2: -0x100",
																				"returnValue": "",
																				"status": "HAVOC",
																				"childrenList":[]
,
																				"changed": "false"
																			},
																			{
																				"funcName": "solghost_return_func1: 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff (MAX_UINT256)",
																				"returnValue": "",
																				"status": "HAVOC",
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
																	},
																	{
																		"funcName": "CurveTokenExample",
																		"returnValue": "",
																		"status": "",
																		"childrenList":[
																			{
																				"funcName": "_balances[0x18160dde]: 0x555555555555555555555555555555555555555555555555555555555555554b",
																				"returnValue": "",
																				"status": "HAVOC",
																				"childrenList":[]
,
																				"changed": "false"
																			},
																			{
																				"funcName": "_totalSupply: 0x555555555555555555555555555555555555555555555555555555555555514b",
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
																		"funcName": "ERC20",
																		"returnValue": "",
																		"status": "",
																		"childrenList":[
																			{
																				"funcName": "_balances[Curve (0x18160ddc)]: 0",
																				"returnValue": "",
																				"status": "HAVOC",
																				"childrenList":[]
,
																				"changed": "false"
																			},
																			{
																				"funcName": "_balances[0x18160dde]: 0",
																				"returnValue": "",
																				"status": "HAVOC",
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
													}
												]
											},
											{
												"funcName": "Load from Curve.lp_token: CurveTokenExample (0xfffffffffffffffffffffffffffffffffffffffe)",
												"returnValue": "",
												"status": "",
												"childrenList":[]

											},
											{
												"funcName": "CurveTokenExample.totalSupply()",
												"returnValue": "0x555555555555555555555555555555555555555555555555555555555555514b",
												"status": "SUCCESS",
												"childrenList":[
													{
														"funcName": "(internal) CurveTokenExample.totalSupply()",
														"returnValue": "0x555555555555555555555555555555555555555555555555555555555555514b",
														"status": "",
														"childrenList":[
															{
																"funcName": "Load from CurveTokenExample._totalSupply: 0x555555555555555555555555555555555555555555555555555555555555514b",
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
																		"funcName": "Curve",
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
																				"funcName": "admin_balances[0]: 0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffc",
																				"returnValue": "",
																				"status": "HAVOC",
																				"childrenList":[]
,
																				"changed": "false"
																			},
																			{
																				"funcName": "admin_balances[1]: 0",
																				"returnValue": "",
																				"status": "HAVOC",
																				"childrenList":[]
,
																				"changed": "false"
																			},
																			{
																				"funcName": "coins_0: 0",
																				"returnValue": "",
																				"status": "HAVOC",
																				"childrenList":[]
,
																				"changed": "false"
																			},
																			{
																				"funcName": "coins_1: ERC20 (0x70a08230)",
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
																				"funcName": "lp_token: CurveTokenExample (0xfffffffffffffffffffffffffffffffffffffffe)",
																				"returnValue": "",
																				"status": "HAVOC",
																				"childrenList":[]
,
																				"changed": "false"
																			},
																			{
																				"funcName": "solghost_executeFunction1: -0x100",
																				"returnValue": "",
																				"status": "HAVOC",
																				"childrenList":[]
,
																				"changed": "false"
																			},
																			{
																				"funcName": "solghost_executeFunction2: -0x100",
																				"returnValue": "",
																				"status": "HAVOC",
																				"childrenList":[]
,
																				"changed": "false"
																			},
																			{
																				"funcName": "solghost_return_func1: 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff (MAX_UINT256)",
																				"returnValue": "",
																				"status": "HAVOC",
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
																	},
																	{
																		"funcName": "CurveTokenExample",
																		"returnValue": "",
																		"status": "",
																		"childrenList":[
																			{
																				"funcName": "_balances[0x18160dde]: 0x555555555555555555555555555555555555555555555555555555555555554b",
																				"returnValue": "",
																				"status": "HAVOC",
																				"childrenList":[]
,
																				"changed": "false"
																			},
																			{
																				"funcName": "_totalSupply: 0x555555555555555555555555555555555555555555555555555555555555514b",
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
																		"funcName": "ERC20",
																		"returnValue": "",
																		"status": "",
																		"childrenList":[
																			{
																				"funcName": "_balances[Curve (0x18160ddc)]: 0",
																				"returnValue": "",
																				"status": "HAVOC",
																				"childrenList":[]
,
																				"changed": "false"
																			},
																			{
																				"funcName": "_balances[0x18160dde]: 0",
																				"returnValue": "",
																				"status": "HAVOC",
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
												"funcName": "Load from Curve.lp_token: CurveTokenExample (0xfffffffffffffffffffffffffffffffffffffffe)",
												"returnValue": "",
												"status": "",
												"childrenList":[]

											},
											{
												"funcName": "CurveTokenExample.burnFrom(to=0x18160dde, value=0x555555555555555555555555555555555555555555555555555555555555554b)",
												"returnValue": "true",
												"status": "SUCCESS",
												"childrenList":[
													{
														"funcName": "(internal) ERC20._burn(account=0x18160dde, amount=0x555555555555555555555555555555555555555555555555555555555555554b)",
														"returnValue": "",
														"status": "",
														"childrenList":[
															{
																"funcName": "(internal) ERC20._update(from=0x18160dde, to=0, amount=0x555555555555555555555555555555555555555555555555555555555555554b)",
																"returnValue": "",
																"status": "",
																"childrenList":[
																	{
																		"funcName": "Load from CurveTokenExample._balances[0x18160dde]: 0x555555555555555555555555555555555555555555555555555555555555554b",
																		"returnValue": "",
																		"status": "",
																		"childrenList":[]

																	},
																	{
																		"funcName": "Store at CurveTokenExample._balances[0x18160dde]: 0",
																		"returnValue": "",
																		"status": "",
																		"childrenList":[]

																	},
																	{
																		"funcName": "Load from CurveTokenExample._totalSupply: 0x555555555555555555555555555555555555555555555555555555555555514b",
																		"returnValue": "",
																		"status": "",
																		"childrenList":[]

																	},
																	{
																		"funcName": "Store at CurveTokenExample._totalSupply: 0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffc00",
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
																				"funcName": "Curve",
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
																						"funcName": "admin_balances[0]: 0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffc",
																						"returnValue": "",
																						"status": "HAVOC",
																						"childrenList":[]
,
																						"changed": "false"
																					},
																					{
																						"funcName": "admin_balances[1]: 0",
																						"returnValue": "",
																						"status": "HAVOC",
																						"childrenList":[]
,
																						"changed": "false"
																					},
																					{
																						"funcName": "coins_0: 0",
																						"returnValue": "",
																						"status": "HAVOC",
																						"childrenList":[]
,
																						"changed": "false"
																					},
																					{
																						"funcName": "coins_1: ERC20 (0x70a08230)",
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
																						"funcName": "lp_token: CurveTokenExample (0xfffffffffffffffffffffffffffffffffffffffe)",
																						"returnValue": "",
																						"status": "HAVOC",
																						"childrenList":[]
,
																						"changed": "false"
																					},
																					{
																						"funcName": "solghost_executeFunction1: -0x100",
																						"returnValue": "",
																						"status": "HAVOC",
																						"childrenList":[]
,
																						"changed": "false"
																					},
																					{
																						"funcName": "solghost_executeFunction2: -0x100",
																						"returnValue": "",
																						"status": "HAVOC",
																						"childrenList":[]
,
																						"changed": "false"
																					},
																					{
																						"funcName": "solghost_return_func1: 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff (MAX_UINT256)",
																						"returnValue": "",
																						"status": "HAVOC",
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
																			},
																			{
																				"funcName": "CurveTokenExample",
																				"returnValue": "",
																				"status": "",
																				"childrenList":[
																					{
																						"funcName": "_balances[0x18160dde]: 0 (changed)",
																						"returnValue": "",
																						"status": "UNKNOWN",
																						"childrenList":[]
,
																						"changed": "true"
																					},
																					{
																						"funcName": "_totalSupply: 0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffc00 (changed)",
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
																				"funcName": "ERC20",
																				"returnValue": "",
																				"status": "",
																				"childrenList":[
																					{
																						"funcName": "_balances[Curve (0x18160ddc)]: 0",
																						"returnValue": "",
																						"status": "HAVOC",
																						"childrenList":[]
,
																						"changed": "false"
																					},
																					{
																						"funcName": "_balances[0x18160dde]: 0",
																						"returnValue": "",
																						"status": "HAVOC",
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
															},
															{
																"funcName": "Storage State",
																"returnValue": "",
																"status": "",
																"childrenList":[
																	{
																		"funcName": "Curve",
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
																				"funcName": "admin_balances[0]: 0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffc",
																				"returnValue": "",
																				"status": "HAVOC",
																				"childrenList":[]
,
																				"changed": "false"
																			},
																			{
																				"funcName": "admin_balances[1]: 0",
																				"returnValue": "",
																				"status": "HAVOC",
																				"childrenList":[]
,
																				"changed": "false"
																			},
																			{
																				"funcName": "coins_0: 0",
																				"returnValue": "",
																				"status": "HAVOC",
																				"childrenList":[]
,
																				"changed": "false"
																			},
																			{
																				"funcName": "coins_1: ERC20 (0x70a08230)",
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
																				"funcName": "lp_token: CurveTokenExample (0xfffffffffffffffffffffffffffffffffffffffe)",
																				"returnValue": "",
																				"status": "HAVOC",
																				"childrenList":[]
,
																				"changed": "false"
																			},
																			{
																				"funcName": "solghost_executeFunction1: -0x100",
																				"returnValue": "",
																				"status": "HAVOC",
																				"childrenList":[]
,
																				"changed": "false"
																			},
																			{
																				"funcName": "solghost_executeFunction2: -0x100",
																				"returnValue": "",
																				"status": "HAVOC",
																				"childrenList":[]
,
																				"changed": "false"
																			},
																			{
																				"funcName": "solghost_return_func1: 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff (MAX_UINT256)",
																				"returnValue": "",
																				"status": "HAVOC",
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
																	},
																	{
																		"funcName": "CurveTokenExample",
																		"returnValue": "",
																		"status": "",
																		"childrenList":[
																			{
																				"funcName": "_balances[0x18160dde]: 0",
																				"returnValue": "",
																				"status": "UNKNOWN",
																				"childrenList":[]
,
																				"changed": "false"
																			},
																			{
																				"funcName": "_totalSupply: 0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffc00",
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
																		"funcName": "ERC20",
																		"returnValue": "",
																		"status": "",
																		"childrenList":[
																			{
																				"funcName": "_balances[Curve (0x18160ddc)]: 0",
																				"returnValue": "",
																				"status": "HAVOC",
																				"childrenList":[]
,
																				"changed": "false"
																			},
																			{
																				"funcName": "_balances[0x18160dde]: 0",
																				"returnValue": "",
																				"status": "HAVOC",
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
													}
												]
											},
											{
												"funcName": "Loop at Curve.sol: line: 163: for (uint256 i;i<2;i++){",
												"returnValue": "",
												"status": "",
												"childrenList":[
													{
														"funcName": "Loop Iteration 1",
														"returnValue": "",
														"status": "",
														"childrenList":[
															{
																"funcName": "sender: Curve (0x18160ddc); receiver: 0x18160dde; transferred amount: 3",
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
																		"funcName": "Store at sender.balance: 0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffc",
																		"returnValue": "",
																		"status": "",
																		"childrenList":[]

																	},
																	{
																		"funcName": "Load from receiver.balance: 0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffc",
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
																"funcName": "/* Curve.sol: 168: */ msg.sender.call{value:value}(\"\"): UNRESOLVED Optimistic Fallback DISPATCHER summary",
																"returnValue": "",
																"status": "DISPATCHER",
																"childrenList":[
																	{
																		"funcName": "Rejected transferred funds",
																		"returnValue": "",
																		"status": "",
																		"childrenList":[]

																	}
																]
															},
															{
																"funcName": "Curve.getVirtualPrice()",
																"returnValue": "0",
																"status": "SUCCESS",
																"childrenList":[
																	{
																		"funcName": "(internal) Curve.getVirtualPrice()",
																		"returnValue": "0",
																		"status": "",
																		"childrenList":[
																			{
																				"funcName": "Load from Curve.admin_balances[0]: 0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffc",
																				"returnValue": "",
																				"status": "",
																				"childrenList":[]

																			},
																			{
																				"funcName": "Load from Curve.admin_balances[1]: 0",
																				"returnValue": "",
																				"status": "",
																				"childrenList":[]

																			},
																			{
																				"funcName": "Load from Curve.coins_1: ERC20 (0x70a08230)",
																				"returnValue": "",
																				"status": "",
																				"childrenList":[]

																			},
																			{
																				"funcName": "ERC20.balanceOf(account=Curve (0x18160ddc))",
																				"returnValue": "0",
																				"status": "SUCCESS",
																				"childrenList":[
																					{
																						"funcName": "(internal) ERC20.balanceOf(account=Curve (0x18160ddc))",
																						"returnValue": "0",
																						"status": "",
																						"childrenList":[
																							{
																								"funcName": "Load from ERC20._balances[Curve (0x18160ddc)]: 0",
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
																										"funcName": "Curve",
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
																												"funcName": "admin_balances[0]: 0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffc",
																												"returnValue": "",
																												"status": "HAVOC",
																												"childrenList":[]
,
																												"changed": "false"
																											},
																											{
																												"funcName": "admin_balances[1]: 0",
																												"returnValue": "",
																												"status": "HAVOC",
																												"childrenList":[]
,
																												"changed": "false"
																											},
																											{
																												"funcName": "coins_0: 0",
																												"returnValue": "",
																												"status": "HAVOC",
																												"childrenList":[]
,
																												"changed": "false"
																											},
																											{
																												"funcName": "coins_1: ERC20 (0x70a08230)",
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
																												"funcName": "lp_token: CurveTokenExample (0xfffffffffffffffffffffffffffffffffffffffe)",
																												"returnValue": "",
																												"status": "HAVOC",
																												"childrenList":[]
,
																												"changed": "false"
																											},
																											{
																												"funcName": "solghost_executeFunction1: -0x100",
																												"returnValue": "",
																												"status": "HAVOC",
																												"childrenList":[]
,
																												"changed": "false"
																											},
																											{
																												"funcName": "solghost_executeFunction2: -0x100",
																												"returnValue": "",
																												"status": "HAVOC",
																												"childrenList":[]
,
																												"changed": "false"
																											},
																											{
																												"funcName": "solghost_return_func1: 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff (MAX_UINT256)",
																												"returnValue": "",
																												"status": "HAVOC",
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
																									},
																									{
																										"funcName": "CurveTokenExample",
																										"returnValue": "",
																										"status": "",
																										"childrenList":[
																											{
																												"funcName": "_balances[0x18160dde]: 0",
																												"returnValue": "",
																												"status": "UNKNOWN",
																												"childrenList":[]
,
																												"changed": "false"
																											},
																											{
																												"funcName": "_totalSupply: 0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffc00",
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
																										"funcName": "ERC20",
																										"returnValue": "",
																										"status": "",
																										"childrenList":[
																											{
																												"funcName": "_balances[Curve (0x18160ddc)]: 0",
																												"returnValue": "",
																												"status": "HAVOC",
																												"childrenList":[]
,
																												"changed": "false"
																											},
																											{
																												"funcName": "_balances[0x18160dde]: 0",
																												"returnValue": "",
																												"status": "HAVOC",
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
																				"funcName": "(internal) Curve._A()",
																				"returnValue": "0",
																				"status": "",
																				"childrenList":[
																					{
																						"funcName": "Load from Curve.future_A: 0",
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
																								"funcName": "Curve",
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
																										"funcName": "admin_balances[0]: 0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffc",
																										"returnValue": "",
																										"status": "HAVOC",
																										"childrenList":[]
,
																										"changed": "false"
																									},
																									{
																										"funcName": "admin_balances[1]: 0",
																										"returnValue": "",
																										"status": "HAVOC",
																										"childrenList":[]
,
																										"changed": "false"
																									},
																									{
																										"funcName": "coins_0: 0",
																										"returnValue": "",
																										"status": "HAVOC",
																										"childrenList":[]
,
																										"changed": "false"
																									},
																									{
																										"funcName": "coins_1: ERC20 (0x70a08230)",
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
																										"funcName": "lp_token: CurveTokenExample (0xfffffffffffffffffffffffffffffffffffffffe)",
																										"returnValue": "",
																										"status": "HAVOC",
																										"childrenList":[]
,
																										"changed": "false"
																									},
																									{
																										"funcName": "solghost_executeFunction1: -0x100",
																										"returnValue": "",
																										"status": "HAVOC",
																										"childrenList":[]
,
																										"changed": "false"
																									},
																									{
																										"funcName": "solghost_executeFunction2: -0x100",
																										"returnValue": "",
																										"status": "HAVOC",
																										"childrenList":[]
,
																										"changed": "false"
																									},
																									{
																										"funcName": "solghost_return_func1: 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff (MAX_UINT256)",
																										"returnValue": "",
																										"status": "HAVOC",
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
																							},
																							{
																								"funcName": "CurveTokenExample",
																								"returnValue": "",
																								"status": "",
																								"childrenList":[
																									{
																										"funcName": "_balances[0x18160dde]: 0",
																										"returnValue": "",
																										"status": "UNKNOWN",
																										"childrenList":[]
,
																										"changed": "false"
																									},
																									{
																										"funcName": "_totalSupply: 0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffc00",
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
																								"funcName": "ERC20",
																								"returnValue": "",
																								"status": "",
																								"childrenList":[
																									{
																										"funcName": "_balances[Curve (0x18160ddc)]: 0",
																										"returnValue": "",
																										"status": "HAVOC",
																										"childrenList":[]
,
																										"changed": "false"
																									},
																									{
																										"funcName": "_balances[0x18160dde]: 0",
																										"returnValue": "",
																										"status": "HAVOC",
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
																				"funcName": "Curve.get_D(xp=[0=0, 1=0], amp=0)",
																				"returnValue": "0",
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
																						"funcName": "(internal) Curve.get_D(xp=uint256[2], amp=0)",
																						"returnValue": "0",
																						"status": "",
																						"childrenList":[
																							{
																								"funcName": "Storage State",
																								"returnValue": "",
																								"status": "",
																								"childrenList":[
																									{
																										"funcName": "Curve",
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
																												"funcName": "admin_balances[0]: 0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffc",
																												"returnValue": "",
																												"status": "HAVOC",
																												"childrenList":[]
,
																												"changed": "false"
																											},
																											{
																												"funcName": "admin_balances[1]: 0",
																												"returnValue": "",
																												"status": "HAVOC",
																												"childrenList":[]
,
																												"changed": "false"
																											},
																											{
																												"funcName": "coins_0: 0",
																												"returnValue": "",
																												"status": "HAVOC",
																												"childrenList":[]
,
																												"changed": "false"
																											},
																											{
																												"funcName": "coins_1: ERC20 (0x70a08230)",
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
																												"funcName": "lp_token: CurveTokenExample (0xfffffffffffffffffffffffffffffffffffffffe)",
																												"returnValue": "",
																												"status": "HAVOC",
																												"childrenList":[]
,
																												"changed": "false"
																											},
																											{
																												"funcName": "solghost_executeFunction1: -0x100",
																												"returnValue": "",
																												"status": "HAVOC",
																												"childrenList":[]
,
																												"changed": "false"
																											},
																											{
																												"funcName": "solghost_executeFunction2: -0x100",
																												"returnValue": "",
																												"status": "HAVOC",
																												"childrenList":[]
,
																												"changed": "false"
																											},
																											{
																												"funcName": "solghost_return_func1: 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff (MAX_UINT256)",
																												"returnValue": "",
																												"status": "HAVOC",
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
																									},
																									{
																										"funcName": "CurveTokenExample",
																										"returnValue": "",
																										"status": "",
																										"childrenList":[
																											{
																												"funcName": "_balances[0x18160dde]: 0",
																												"returnValue": "",
																												"status": "UNKNOWN",
																												"childrenList":[]
,
																												"changed": "false"
																											},
																											{
																												"funcName": "_totalSupply: 0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffc00",
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
																										"funcName": "ERC20",
																										"returnValue": "",
																										"status": "",
																										"childrenList":[
																											{
																												"funcName": "_balances[Curve (0x18160ddc)]: 0",
																												"returnValue": "",
																												"status": "HAVOC",
																												"childrenList":[]
,
																												"changed": "false"
																											},
																											{
																												"funcName": "_balances[0x18160dde]: 0",
																												"returnValue": "",
																												"status": "HAVOC",
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
																					}
																				]
																			},
																			{
																				"funcName": "Load from Curve.lp_token: CurveTokenExample (0xfffffffffffffffffffffffffffffffffffffffe)",
																				"returnValue": "",
																				"status": "",
																				"childrenList":[]

																			},
																			{
																				"funcName": "CurveTokenExample.totalSupply()",
																				"returnValue": "0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffc00",
																				"status": "SUCCESS",
																				"childrenList":[
																					{
																						"funcName": "(internal) CurveTokenExample.totalSupply()",
																						"returnValue": "0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffc00",
																						"status": "",
																						"childrenList":[
																							{
																								"funcName": "Load from CurveTokenExample._totalSupply: 0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffc00",
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
																										"funcName": "Curve",
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
																												"funcName": "admin_balances[0]: 0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffc",
																												"returnValue": "",
																												"status": "HAVOC",
																												"childrenList":[]
,
																												"changed": "false"
																											},
																											{
																												"funcName": "admin_balances[1]: 0",
																												"returnValue": "",
																												"status": "HAVOC",
																												"childrenList":[]
,
																												"changed": "false"
																											},
																											{
																												"funcName": "coins_0: 0",
																												"returnValue": "",
																												"status": "HAVOC",
																												"childrenList":[]
,
																												"changed": "false"
																											},
																											{
																												"funcName": "coins_1: ERC20 (0x70a08230)",
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
																												"funcName": "lp_token: CurveTokenExample (0xfffffffffffffffffffffffffffffffffffffffe)",
																												"returnValue": "",
																												"status": "HAVOC",
																												"childrenList":[]
,
																												"changed": "false"
																											},
																											{
																												"funcName": "solghost_executeFunction1: -0x100",
																												"returnValue": "",
																												"status": "HAVOC",
																												"childrenList":[]
,
																												"changed": "false"
																											},
																											{
																												"funcName": "solghost_executeFunction2: -0x100",
																												"returnValue": "",
																												"status": "HAVOC",
																												"childrenList":[]
,
																												"changed": "false"
																											},
																											{
																												"funcName": "solghost_return_func1: 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff (MAX_UINT256)",
																												"returnValue": "",
																												"status": "HAVOC",
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
																									},
																									{
																										"funcName": "CurveTokenExample",
																										"returnValue": "",
																										"status": "",
																										"childrenList":[
																											{
																												"funcName": "_balances[0x18160dde]: 0",
																												"returnValue": "",
																												"status": "UNKNOWN",
																												"childrenList":[]
,
																												"changed": "false"
																											},
																											{
																												"funcName": "_totalSupply: 0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffc00",
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
																										"funcName": "ERC20",
																										"returnValue": "",
																										"status": "",
																										"childrenList":[
																											{
																												"funcName": "_balances[Curve (0x18160ddc)]: 0",
																												"returnValue": "",
																												"status": "HAVOC",
																												"childrenList":[]
,
																												"changed": "false"
																											},
																											{
																												"funcName": "_balances[0x18160dde]: 0",
																												"returnValue": "",
																												"status": "HAVOC",
																												"childrenList":[]
,
																												"changed": "false"
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
																				"funcName": "Storage State",
																				"returnValue": "",
																				"status": "",
																				"childrenList":[
																					{
																						"funcName": "Curve",
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
																								"funcName": "admin_balances[0]: 0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffc",
																								"returnValue": "",
																								"status": "HAVOC",
																								"childrenList":[]
,
																								"changed": "false"
																							},
																							{
																								"funcName": "admin_balances[1]: 0",
																								"returnValue": "",
																								"status": "HAVOC",
																								"childrenList":[]
,
																								"changed": "false"
																							},
																							{
																								"funcName": "coins_0: 0",
																								"returnValue": "",
																								"status": "HAVOC",
																								"childrenList":[]
,
																								"changed": "false"
																							},
																							{
																								"funcName": "coins_1: ERC20 (0x70a08230)",
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
																								"funcName": "lp_token: CurveTokenExample (0xfffffffffffffffffffffffffffffffffffffffe)",
																								"returnValue": "",
																								"status": "HAVOC",
																								"childrenList":[]
,
																								"changed": "false"
																							},
																							{
																								"funcName": "solghost_executeFunction1: -0x100",
																								"returnValue": "",
																								"status": "HAVOC",
																								"childrenList":[]
,
																								"changed": "false"
																							},
																							{
																								"funcName": "solghost_executeFunction2: -0x100",
																								"returnValue": "",
																								"status": "HAVOC",
																								"childrenList":[]
,
																								"changed": "false"
																							},
																							{
																								"funcName": "solghost_return_func1: 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff (MAX_UINT256)",
																								"returnValue": "",
																								"status": "HAVOC",
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
																					},
																					{
																						"funcName": "CurveTokenExample",
																						"returnValue": "",
																						"status": "",
																						"childrenList":[
																							{
																								"funcName": "_balances[0x18160dde]: 0",
																								"returnValue": "",
																								"status": "UNKNOWN",
																								"childrenList":[]
,
																								"changed": "false"
																							},
																							{
																								"funcName": "_totalSupply: 0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffc00",
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
																						"funcName": "ERC20",
																						"returnValue": "",
																						"status": "",
																						"childrenList":[
																							{
																								"funcName": "_balances[Curve (0x18160ddc)]: 0",
																								"returnValue": "",
																								"status": "HAVOC",
																								"childrenList":[]
,
																								"changed": "false"
																							},
																							{
																								"funcName": "_balances[0x18160dde]: 0",
																								"returnValue": "",
																								"status": "HAVOC",
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
																	}
																]
															},
															{
																"funcName": "Curve.solghost_executeFunction1()",
																"returnValue": "0xffffffff00",
																"status": "SUCCESS",
																"childrenList":[
																	{
																		"funcName": "Load from Curve.solghost_executeFunction1: -0x100",
																		"returnValue": "",
																		"status": "",
																		"childrenList":[]

																	}
																]
															},
															{
																"funcName": "Curve.coins_1()",
																"returnValue": "ERC20 (0x70a08230)",
																"status": "SUCCESS",
																"childrenList":[
																	{
																		"funcName": "Load from Curve.coins_1: ERC20 (0x70a08230)",
																		"returnValue": "",
																		"status": "",
																		"childrenList":[]

																	}
																]
															},
															{
																"funcName": "Curve.solghost_return_func1()",
																"returnValue": "0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff (MAX_UINT256)",
																"status": "SUCCESS",
																"childrenList":[
																	{
																		"funcName": "Load from Curve.solghost_return_func1: 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff (MAX_UINT256)",
																		"returnValue": "",
																		"status": "",
																		"childrenList":[]

																	}
																]
															},
															{
																"funcName": "Curve.solghost_executeFunction2()",
																"returnValue": "0xffffffff00",
																"status": "SUCCESS",
																"childrenList":[
																	{
																		"funcName": "Load from Curve.solghost_executeFunction2: -0x100",
																		"returnValue": "",
																		"status": "",
																		"childrenList":[]

																	}
																]
															},
															{
																"funcName": "Curve.lp_token()",
																"returnValue": "CurveTokenExample (0xfffffffffffffffffffffffffffffffffffffffe)",
																"status": "SUCCESS",
																"childrenList":[
																	{
																		"funcName": "Load from Curve.lp_token: CurveTokenExample (0xfffffffffffffffffffffffffffffffffffffffe)",
																		"returnValue": "",
																		"status": "",
																		"childrenList":[]

																	}
																]
															},
															{
																"funcName": "Curve.coins_0()",
																"returnValue": "0",
																"status": "SUCCESS",
																"childrenList":[
																	{
																		"funcName": "Load from Curve.coins_0: 0",
																		"returnValue": "",
																		"status": "",
																		"childrenList":[]

																	}
																]
															},
															{
																"funcName": "Curve._balances(_value=0)",
																"returnValue": "[]",
																"status": "SUCCESS",
																"childrenList":[
																	{
																		"funcName": "Load from Curve.admin_balances[0]: 0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffc",
																		"returnValue": "",
																		"status": "",
																		"childrenList":[]

																	},
																	{
																		"funcName": "Load from Curve.admin_balances[1]: 0",
																		"returnValue": "",
																		"status": "",
																		"childrenList":[]

																	},
																	{
																		"funcName": "Load from Curve.coins_1: ERC20 (0x70a08230)",
																		"returnValue": "",
																		"status": "",
																		"childrenList":[]

																	},
																	{
																		"funcName": "ERC20.balanceOf(account=Curve (0x18160ddc))",
																		"returnValue": "0",
																		"status": "SUCCESS",
																		"childrenList":[
																			{
																				"funcName": "(internal) ERC20.balanceOf(account=Curve (0x18160ddc))",
																				"returnValue": "0",
																				"status": "",
																				"childrenList":[
																					{
																						"funcName": "Load from ERC20._balances[Curve (0x18160ddc)]: 0",
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
																								"funcName": "Curve",
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
																										"funcName": "admin_balances[0]: 0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffc",
																										"returnValue": "",
																										"status": "HAVOC",
																										"childrenList":[]
,
																										"changed": "false"
																									},
																									{
																										"funcName": "admin_balances[1]: 0",
																										"returnValue": "",
																										"status": "HAVOC",
																										"childrenList":[]
,
																										"changed": "false"
																									},
																									{
																										"funcName": "coins_0: 0",
																										"returnValue": "",
																										"status": "HAVOC",
																										"childrenList":[]
,
																										"changed": "false"
																									},
																									{
																										"funcName": "coins_1: ERC20 (0x70a08230)",
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
																										"funcName": "lp_token: CurveTokenExample (0xfffffffffffffffffffffffffffffffffffffffe)",
																										"returnValue": "",
																										"status": "HAVOC",
																										"childrenList":[]
,
																										"changed": "false"
																									},
																									{
																										"funcName": "solghost_executeFunction1: -0x100",
																										"returnValue": "",
																										"status": "HAVOC",
																										"childrenList":[]
,
																										"changed": "false"
																									},
																									{
																										"funcName": "solghost_executeFunction2: -0x100",
																										"returnValue": "",
																										"status": "HAVOC",
																										"childrenList":[]
,
																										"changed": "false"
																									},
																									{
																										"funcName": "solghost_return_func1: 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff (MAX_UINT256)",
																										"returnValue": "",
																										"status": "HAVOC",
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
																							},
																							{
																								"funcName": "CurveTokenExample",
																								"returnValue": "",
																								"status": "",
																								"childrenList":[
																									{
																										"funcName": "_balances[0x18160dde]: 0",
																										"returnValue": "",
																										"status": "UNKNOWN",
																										"childrenList":[]
,
																										"changed": "false"
																									},
																									{
																										"funcName": "_totalSupply: 0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffc00",
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
																								"funcName": "ERC20",
																								"returnValue": "",
																								"status": "",
																								"childrenList":[
																									{
																										"funcName": "_balances[Curve (0x18160ddc)]: 0",
																										"returnValue": "",
																										"status": "HAVOC",
																										"childrenList":[]
,
																										"changed": "false"
																									},
																									{
																										"funcName": "_balances[0x18160dde]: 0",
																										"returnValue": "",
																										"status": "HAVOC",
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
															},
															{
																"funcName": "Curve.get_D(xp=[], amp=0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff (MAX_UINT256))",
																"returnValue": "0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff (MAX_UINT256)",
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
																		"funcName": "(internal) Curve.get_D(xp=uint256[2], amp=0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff (MAX_UINT256))",
																		"returnValue": "0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff (MAX_UINT256)",
																		"status": "",
																		"childrenList":[
																			{
																				"funcName": "Storage State",
																				"returnValue": "",
																				"status": "",
																				"childrenList":[
																					{
																						"funcName": "Curve",
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
																								"funcName": "admin_balances[0]: 0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffc",
																								"returnValue": "",
																								"status": "HAVOC",
																								"childrenList":[]
,
																								"changed": "false"
																							},
																							{
																								"funcName": "admin_balances[1]: 0",
																								"returnValue": "",
																								"status": "HAVOC",
																								"childrenList":[]
,
																								"changed": "false"
																							},
																							{
																								"funcName": "coins_0: 0",
																								"returnValue": "",
																								"status": "HAVOC",
																								"childrenList":[]
,
																								"changed": "false"
																							},
																							{
																								"funcName": "coins_1: ERC20 (0x70a08230)",
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
																								"funcName": "lp_token: CurveTokenExample (0xfffffffffffffffffffffffffffffffffffffffe)",
																								"returnValue": "",
																								"status": "HAVOC",
																								"childrenList":[]
,
																								"changed": "false"
																							},
																							{
																								"funcName": "solghost_executeFunction1: -0x100",
																								"returnValue": "",
																								"status": "HAVOC",
																								"childrenList":[]
,
																								"changed": "false"
																							},
																							{
																								"funcName": "solghost_executeFunction2: -0x100",
																								"returnValue": "",
																								"status": "HAVOC",
																								"childrenList":[]
,
																								"changed": "false"
																							},
																							{
																								"funcName": "solghost_return_func1: 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff (MAX_UINT256)",
																								"returnValue": "",
																								"status": "HAVOC",
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
																					},
																					{
																						"funcName": "CurveTokenExample",
																						"returnValue": "",
																						"status": "",
																						"childrenList":[
																							{
																								"funcName": "_balances[0x18160dde]: 0",
																								"returnValue": "",
																								"status": "UNKNOWN",
																								"childrenList":[]
,
																								"changed": "false"
																							},
																							{
																								"funcName": "_totalSupply: 0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffc00",
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
																						"funcName": "ERC20",
																						"returnValue": "",
																						"status": "",
																						"childrenList":[
																							{
																								"funcName": "_balances[Curve (0x18160ddc)]: 0",
																								"returnValue": "",
																								"status": "HAVOC",
																								"childrenList":[]
,
																								"changed": "false"
																							},
																							{
																								"funcName": "_balances[0x18160dde]: 0",
																								"returnValue": "",
																								"status": "HAVOC",
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
																	}
																]
															},
															{
																"funcName": "sender: 0x18160dde; receiver: Curve (0x18160ddc); transferred amount: 3",
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
																		"funcName": "Store at sender.balance: 0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffc",
																		"returnValue": "",
																		"status": "",
																		"childrenList":[]

																	},
																	{
																		"funcName": "Load from receiver.balance: 0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffc",
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
																"funcName": "(internal) Curve.sample_view_functions()",
																"returnValue": "",
																"status": "",
																"childrenList":[
																	{
																		"funcName": "(internal) Curve.getVirtualPrice()",
																		"returnValue": "0",
																		"status": "",
																		"childrenList":[
																			{
																				"funcName": "Load from Curve.admin_balances[0]: 0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffc",
																				"returnValue": "",
																				"status": "",
																				"childrenList":[]

																			},
																			{
																				"funcName": "Load from Curve.admin_balances[1]: 0",
																				"returnValue": "",
																				"status": "",
																				"childrenList":[]

																			},
																			{
																				"funcName": "Load from Curve.coins_1: ERC20 (0x70a08230)",
																				"returnValue": "",
																				"status": "",
																				"childrenList":[]

																			},
																			{
																				"funcName": "ERC20.balanceOf(account=Curve (0x18160ddc))",
																				"returnValue": "0",
																				"status": "SUCCESS",
																				"childrenList":[
																					{
																						"funcName": "(internal) ERC20.balanceOf(account=Curve (0x18160ddc))",
																						"returnValue": "0",
																						"status": "",
																						"childrenList":[
																							{
																								"funcName": "Load from ERC20._balances[Curve (0x18160ddc)]: 0",
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
																										"funcName": "Curve",
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
																												"funcName": "admin_balances[0]: 0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffc",
																												"returnValue": "",
																												"status": "HAVOC",
																												"childrenList":[]
,
																												"changed": "false"
																											},
																											{
																												"funcName": "admin_balances[1]: 0",
																												"returnValue": "",
																												"status": "HAVOC",
																												"childrenList":[]
,
																												"changed": "false"
																											},
																											{
																												"funcName": "coins_0: 0",
																												"returnValue": "",
																												"status": "HAVOC",
																												"childrenList":[]
,
																												"changed": "false"
																											},
																											{
																												"funcName": "coins_1: ERC20 (0x70a08230)",
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
																												"funcName": "lp_token: CurveTokenExample (0xfffffffffffffffffffffffffffffffffffffffe)",
																												"returnValue": "",
																												"status": "HAVOC",
																												"childrenList":[]
,
																												"changed": "false"
																											},
																											{
																												"funcName": "solghost_executeFunction1: -0x100",
																												"returnValue": "",
																												"status": "HAVOC",
																												"childrenList":[]
,
																												"changed": "false"
																											},
																											{
																												"funcName": "solghost_executeFunction2: -0x100",
																												"returnValue": "",
																												"status": "HAVOC",
																												"childrenList":[]
,
																												"changed": "false"
																											},
																											{
																												"funcName": "solghost_return_func1: 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff (MAX_UINT256)",
																												"returnValue": "",
																												"status": "HAVOC",
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
																									},
																									{
																										"funcName": "CurveTokenExample",
																										"returnValue": "",
																										"status": "",
																										"childrenList":[
																											{
																												"funcName": "_balances[0x18160dde]: 0",
																												"returnValue": "",
																												"status": "UNKNOWN",
																												"childrenList":[]
,
																												"changed": "false"
																											},
																											{
																												"funcName": "_totalSupply: 0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffc00",
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
																										"funcName": "ERC20",
																										"returnValue": "",
																										"status": "",
																										"childrenList":[
																											{
																												"funcName": "_balances[Curve (0x18160ddc)]: 0",
																												"returnValue": "",
																												"status": "HAVOC",
																												"childrenList":[]
,
																												"changed": "false"
																											},
																											{
																												"funcName": "_balances[0x18160dde]: 0",
																												"returnValue": "",
																												"status": "HAVOC",
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
																			},
																			{
																				"funcName": "(internal) Curve._A()",
																				"returnValue": "0",
																				"status": "",
																				"childrenList":[
																					{
																						"funcName": "Load from Curve.future_A: 0",
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
																								"funcName": "Curve",
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
																										"funcName": "admin_balances[0]: 0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffc",
																										"returnValue": "",
																										"status": "HAVOC",
																										"childrenList":[]
,
																										"changed": "false"
																									},
																									{
																										"funcName": "admin_balances[1]: 0",
																										"returnValue": "",
																										"status": "HAVOC",
																										"childrenList":[]
,
																										"changed": "false"
																									},
																									{
																										"funcName": "coins_0: 0",
																										"returnValue": "",
																										"status": "HAVOC",
																										"childrenList":[]
,
																										"changed": "false"
																									},
																									{
																										"funcName": "coins_1: ERC20 (0x70a08230)",
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
																										"funcName": "lp_token: CurveTokenExample (0xfffffffffffffffffffffffffffffffffffffffe)",
																										"returnValue": "",
																										"status": "HAVOC",
																										"childrenList":[]
,
																										"changed": "false"
																									},
																									{
																										"funcName": "solghost_executeFunction1: -0x100",
																										"returnValue": "",
																										"status": "HAVOC",
																										"childrenList":[]
,
																										"changed": "false"
																									},
																									{
																										"funcName": "solghost_executeFunction2: -0x100",
																										"returnValue": "",
																										"status": "HAVOC",
																										"childrenList":[]
,
																										"changed": "false"
																									},
																									{
																										"funcName": "solghost_return_func1: 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff (MAX_UINT256)",
																										"returnValue": "",
																										"status": "HAVOC",
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
																							},
																							{
																								"funcName": "CurveTokenExample",
																								"returnValue": "",
																								"status": "",
																								"childrenList":[
																									{
																										"funcName": "_balances[0x18160dde]: 0",
																										"returnValue": "",
																										"status": "UNKNOWN",
																										"childrenList":[]
,
																										"changed": "false"
																									},
																									{
																										"funcName": "_totalSupply: 0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffc00",
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
																								"funcName": "ERC20",
																								"returnValue": "",
																								"status": "",
																								"childrenList":[
																									{
																										"funcName": "_balances[Curve (0x18160ddc)]: 0",
																										"returnValue": "",
																										"status": "HAVOC",
																										"childrenList":[]
,
																										"changed": "false"
																									},
																									{
																										"funcName": "_balances[0x18160dde]: 0",
																										"returnValue": "",
																										"status": "HAVOC",
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
																			},
																			{
																				"funcName": "Curve.get_D(xp=[0=3, 1=0], amp=0)",
																				"returnValue": "3",
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
																						"funcName": "(internal) Curve.get_D(xp=uint256[2], amp=0)",
																						"returnValue": "3",
																						"status": "",
																						"childrenList":[
																							{
																								"funcName": "Storage State",
																								"returnValue": "",
																								"status": "",
																								"childrenList":[
																									{
																										"funcName": "Curve",
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
																												"funcName": "admin_balances[0]: 0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffc",
																												"returnValue": "",
																												"status": "HAVOC",
																												"childrenList":[]
,
																												"changed": "false"
																											},
																											{
																												"funcName": "admin_balances[1]: 0",
																												"returnValue": "",
																												"status": "HAVOC",
																												"childrenList":[]
,
																												"changed": "false"
																											},
																											{
																												"funcName": "coins_0: 0",
																												"returnValue": "",
																												"status": "HAVOC",
																												"childrenList":[]
,
																												"changed": "false"
																											},
																											{
																												"funcName": "coins_1: ERC20 (0x70a08230)",
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
																												"funcName": "lp_token: CurveTokenExample (0xfffffffffffffffffffffffffffffffffffffffe)",
																												"returnValue": "",
																												"status": "HAVOC",
																												"childrenList":[]
,
																												"changed": "false"
																											},
																											{
																												"funcName": "solghost_executeFunction1: -0x100",
																												"returnValue": "",
																												"status": "HAVOC",
																												"childrenList":[]
,
																												"changed": "false"
																											},
																											{
																												"funcName": "solghost_executeFunction2: -0x100",
																												"returnValue": "",
																												"status": "HAVOC",
																												"childrenList":[]
,
																												"changed": "false"
																											},
																											{
																												"funcName": "solghost_return_func1: 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff (MAX_UINT256)",
																												"returnValue": "",
																												"status": "HAVOC",
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
																									},
																									{
																										"funcName": "CurveTokenExample",
																										"returnValue": "",
																										"status": "",
																										"childrenList":[
																											{
																												"funcName": "_balances[0x18160dde]: 0",
																												"returnValue": "",
																												"status": "UNKNOWN",
																												"childrenList":[]
,
																												"changed": "false"
																											},
																											{
																												"funcName": "_totalSupply: 0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffc00",
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
																										"funcName": "ERC20",
																										"returnValue": "",
																										"status": "",
																										"childrenList":[
																											{
																												"funcName": "_balances[Curve (0x18160ddc)]: 0",
																												"returnValue": "",
																												"status": "HAVOC",
																												"childrenList":[]
,
																												"changed": "false"
																											},
																											{
																												"funcName": "_balances[0x18160dde]: 0",
																												"returnValue": "",
																												"status": "HAVOC",
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
																				"funcName": "Load from Curve.lp_token: CurveTokenExample (0xfffffffffffffffffffffffffffffffffffffffe)",
																				"returnValue": "",
																				"status": "",
																				"childrenList":[]

																			},
																			{
																				"funcName": "CurveTokenExample.totalSupply()",
																				"returnValue": "0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffc00",
																				"status": "SUCCESS",
																				"childrenList":[
																					{
																						"funcName": "(internal) CurveTokenExample.totalSupply()",
																						"returnValue": "0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffc00",
																						"status": "",
																						"childrenList":[
																							{
																								"funcName": "Load from CurveTokenExample._totalSupply: 0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffc00",
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
																										"funcName": "Curve",
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
																												"funcName": "admin_balances[0]: 0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffc",
																												"returnValue": "",
																												"status": "HAVOC",
																												"childrenList":[]
,
																												"changed": "false"
																											},
																											{
																												"funcName": "admin_balances[1]: 0",
																												"returnValue": "",
																												"status": "HAVOC",
																												"childrenList":[]
,
																												"changed": "false"
																											},
																											{
																												"funcName": "coins_0: 0",
																												"returnValue": "",
																												"status": "HAVOC",
																												"childrenList":[]
,
																												"changed": "false"
																											},
																											{
																												"funcName": "coins_1: ERC20 (0x70a08230)",
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
																												"funcName": "lp_token: CurveTokenExample (0xfffffffffffffffffffffffffffffffffffffffe)",
																												"returnValue": "",
																												"status": "HAVOC",
																												"childrenList":[]
,
																												"changed": "false"
																											},
																											{
																												"funcName": "solghost_executeFunction1: -0x100",
																												"returnValue": "",
																												"status": "HAVOC",
																												"childrenList":[]
,
																												"changed": "false"
																											},
																											{
																												"funcName": "solghost_executeFunction2: -0x100",
																												"returnValue": "",
																												"status": "HAVOC",
																												"childrenList":[]
,
																												"changed": "false"
																											},
																											{
																												"funcName": "solghost_return_func1: 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff (MAX_UINT256)",
																												"returnValue": "",
																												"status": "HAVOC",
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
																									},
																									{
																										"funcName": "CurveTokenExample",
																										"returnValue": "",
																										"status": "",
																										"childrenList":[
																											{
																												"funcName": "_balances[0x18160dde]: 0",
																												"returnValue": "",
																												"status": "UNKNOWN",
																												"childrenList":[]
,
																												"changed": "false"
																											},
																											{
																												"funcName": "_totalSupply: 0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffc00",
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
																										"funcName": "ERC20",
																										"returnValue": "",
																										"status": "",
																										"childrenList":[
																											{
																												"funcName": "_balances[Curve (0x18160ddc)]: 0",
																												"returnValue": "",
																												"status": "HAVOC",
																												"childrenList":[]
,
																												"changed": "false"
																											},
																											{
																												"funcName": "_balances[0x18160dde]: 0",
																												"returnValue": "",
																												"status": "HAVOC",
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
																					}
																				]
																			},
																			{
																				"funcName": "Storage State",
																				"returnValue": "",
																				"status": "",
																				"childrenList":[
																					{
																						"funcName": "Curve",
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
																								"funcName": "admin_balances[0]: 0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffc",
																								"returnValue": "",
																								"status": "HAVOC",
																								"childrenList":[]
,
																								"changed": "false"
																							},
																							{
																								"funcName": "admin_balances[1]: 0",
																								"returnValue": "",
																								"status": "HAVOC",
																								"childrenList":[]
,
																								"changed": "false"
																							},
																							{
																								"funcName": "coins_0: 0",
																								"returnValue": "",
																								"status": "HAVOC",
																								"childrenList":[]
,
																								"changed": "false"
																							},
																							{
																								"funcName": "coins_1: ERC20 (0x70a08230)",
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
																								"funcName": "lp_token: CurveTokenExample (0xfffffffffffffffffffffffffffffffffffffffe)",
																								"returnValue": "",
																								"status": "HAVOC",
																								"childrenList":[]
,
																								"changed": "false"
																							},
																							{
																								"funcName": "solghost_executeFunction1: -0x100",
																								"returnValue": "",
																								"status": "HAVOC",
																								"childrenList":[]
,
																								"changed": "false"
																							},
																							{
																								"funcName": "solghost_executeFunction2: -0x100",
																								"returnValue": "",
																								"status": "HAVOC",
																								"childrenList":[]
,
																								"changed": "false"
																							},
																							{
																								"funcName": "solghost_return_func1: 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff (MAX_UINT256)",
																								"returnValue": "",
																								"status": "HAVOC",
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
																					},
																					{
																						"funcName": "CurveTokenExample",
																						"returnValue": "",
																						"status": "",
																						"childrenList":[
																							{
																								"funcName": "_balances[0x18160dde]: 0",
																								"returnValue": "",
																								"status": "UNKNOWN",
																								"childrenList":[]
,
																								"changed": "false"
																							},
																							{
																								"funcName": "_totalSupply: 0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffc00",
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
																						"funcName": "ERC20",
																						"returnValue": "",
																						"status": "",
																						"childrenList":[
																							{
																								"funcName": "_balances[Curve (0x18160ddc)]: 0",
																								"returnValue": "",
																								"status": "HAVOC",
																								"childrenList":[]
,
																								"changed": "false"
																							},
																							{
																								"funcName": "_balances[0x18160dde]: 0",
																								"returnValue": "",
																								"status": "HAVOC",
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
																	},
																	{
																		"funcName": "Store at Curve.solghost_return_func1: 0",
																		"returnValue": "",
																		"status": "",
																		"childrenList":[]

																	},
																	{
																		"funcName": "Store at Curve.solghost_trigger_check: true",
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
																				"funcName": "Curve",
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
																						"funcName": "admin_balances[0]: 0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffc",
																						"returnValue": "",
																						"status": "HAVOC",
																						"childrenList":[]
,
																						"changed": "false"
																					},
																					{
																						"funcName": "admin_balances[1]: 0",
																						"returnValue": "",
																						"status": "HAVOC",
																						"childrenList":[]
,
																						"changed": "false"
																					},
																					{
																						"funcName": "coins_0: 0",
																						"returnValue": "",
																						"status": "HAVOC",
																						"childrenList":[]
,
																						"changed": "false"
																					},
																					{
																						"funcName": "coins_1: ERC20 (0x70a08230)",
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
																						"funcName": "lp_token: CurveTokenExample (0xfffffffffffffffffffffffffffffffffffffffe)",
																						"returnValue": "",
																						"status": "HAVOC",
																						"childrenList":[]
,
																						"changed": "false"
																					},
																					{
																						"funcName": "solghost_executeFunction1: -0x100",
																						"returnValue": "",
																						"status": "HAVOC",
																						"childrenList":[]
,
																						"changed": "false"
																					},
																					{
																						"funcName": "solghost_executeFunction2: -0x100",
																						"returnValue": "",
																						"status": "HAVOC",
																						"childrenList":[]
,
																						"changed": "false"
																					},
																					{
																						"funcName": "solghost_return_func1: 0 (changed)",
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
																			},
																			{
																				"funcName": "CurveTokenExample",
																				"returnValue": "",
																				"status": "",
																				"childrenList":[
																					{
																						"funcName": "_balances[0x18160dde]: 0",
																						"returnValue": "",
																						"status": "UNKNOWN",
																						"childrenList":[]
,
																						"changed": "false"
																					},
																					{
																						"funcName": "_totalSupply: 0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffc00",
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
																				"funcName": "ERC20",
																				"returnValue": "",
																				"status": "",
																				"childrenList":[
																					{
																						"funcName": "_balances[Curve (0x18160ddc)]: 0",
																						"returnValue": "",
																						"status": "HAVOC",
																						"childrenList":[]
,
																						"changed": "false"
																					},
																					{
																						"funcName": "_balances[0x18160dde]: 0",
																						"returnValue": "",
																						"status": "HAVOC",
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
														"funcName": "Loop Iteration 2",
														"returnValue": "",
														"status": "",
														"childrenList":[
															{
																"funcName": "Load from Curve.coins_1: ERC20 (0x70a08230)",
																"returnValue": "",
																"status": "",
																"childrenList":[]

															},
															{
																"funcName": "ERC20.transfer(to=0x18160dde, amount=0)",
																"returnValue": "true",
																"status": "SUCCESS",
																"childrenList":[
																	{
																		"funcName": "(internal) ERC20.transfer(to=0x18160dde, amount=0)",
																		"returnValue": "true",
																		"status": "",
																		"childrenList":[
																			{
																				"funcName": "(internal) Context._msgSender()",
																				"returnValue": "Curve (0x18160ddc)",
																				"status": "",
																				"childrenList":[
																					{
																						"funcName": "Storage State",
																						"returnValue": "",
																						"status": "",
																						"childrenList":[
																							{
																								"funcName": "Curve",
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
																										"funcName": "admin_balances[0]: 0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffc",
																										"returnValue": "",
																										"status": "HAVOC",
																										"childrenList":[]
,
																										"changed": "false"
																									},
																									{
																										"funcName": "admin_balances[1]: 0",
																										"returnValue": "",
																										"status": "HAVOC",
																										"childrenList":[]
,
																										"changed": "false"
																									},
																									{
																										"funcName": "coins_0: 0",
																										"returnValue": "",
																										"status": "HAVOC",
																										"childrenList":[]
,
																										"changed": "false"
																									},
																									{
																										"funcName": "coins_1: ERC20 (0x70a08230)",
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
																										"funcName": "lp_token: CurveTokenExample (0xfffffffffffffffffffffffffffffffffffffffe)",
																										"returnValue": "",
																										"status": "HAVOC",
																										"childrenList":[]
,
																										"changed": "false"
																									},
																									{
																										"funcName": "solghost_executeFunction1: -0x100",
																										"returnValue": "",
																										"status": "HAVOC",
																										"childrenList":[]
,
																										"changed": "false"
																									},
																									{
																										"funcName": "solghost_executeFunction2: -0x100",
																										"returnValue": "",
																										"status": "HAVOC",
																										"childrenList":[]
,
																										"changed": "false"
																									},
																									{
																										"funcName": "solghost_return_func1: 0",
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
																							},
																							{
																								"funcName": "CurveTokenExample",
																								"returnValue": "",
																								"status": "",
																								"childrenList":[
																									{
																										"funcName": "_balances[0x18160dde]: 0",
																										"returnValue": "",
																										"status": "UNKNOWN",
																										"childrenList":[]
,
																										"changed": "false"
																									},
																									{
																										"funcName": "_totalSupply: 0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffc00",
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
																								"funcName": "ERC20",
																								"returnValue": "",
																								"status": "",
																								"childrenList":[
																									{
																										"funcName": "_balances[Curve (0x18160ddc)]: 0",
																										"returnValue": "",
																										"status": "HAVOC",
																										"childrenList":[]
,
																										"changed": "false"
																									},
																									{
																										"funcName": "_balances[0x18160dde]: 0",
																										"returnValue": "",
																										"status": "HAVOC",
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
																			},
																			{
																				"funcName": "(internal) ERC20._transfer(from=Curve (0x18160ddc), to=0x18160dde, amount=0)",
																				"returnValue": "",
																				"status": "",
																				"childrenList":[
																					{
																						"funcName": "(internal) ERC20._update(from=Curve (0x18160ddc), to=0x18160dde, amount=0)",
																						"returnValue": "",
																						"status": "",
																						"childrenList":[
																							{
																								"funcName": "Load from ERC20._balances[Curve (0x18160ddc)]: 0",
																								"returnValue": "",
																								"status": "",
																								"childrenList":[]

																							},
																							{
																								"funcName": "Store at ERC20._balances[Curve (0x18160ddc)]: 0",
																								"returnValue": "",
																								"status": "",
																								"childrenList":[]

																							},
																							{
																								"funcName": "Load from ERC20._balances[0x18160dde]: 0",
																								"returnValue": "",
																								"status": "",
																								"childrenList":[]

																							},
																							{
																								"funcName": "Store at ERC20._balances[0x18160dde]: 0",
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
																										"funcName": "Curve",
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
																												"funcName": "admin_balances[0]: 0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffc",
																												"returnValue": "",
																												"status": "HAVOC",
																												"childrenList":[]
,
																												"changed": "false"
																											},
																											{
																												"funcName": "admin_balances[1]: 0",
																												"returnValue": "",
																												"status": "HAVOC",
																												"childrenList":[]
,
																												"changed": "false"
																											},
																											{
																												"funcName": "coins_0: 0",
																												"returnValue": "",
																												"status": "HAVOC",
																												"childrenList":[]
,
																												"changed": "false"
																											},
																											{
																												"funcName": "coins_1: ERC20 (0x70a08230)",
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
																												"funcName": "lp_token: CurveTokenExample (0xfffffffffffffffffffffffffffffffffffffffe)",
																												"returnValue": "",
																												"status": "HAVOC",
																												"childrenList":[]
,
																												"changed": "false"
																											},
																											{
																												"funcName": "solghost_executeFunction1: -0x100",
																												"returnValue": "",
																												"status": "HAVOC",
																												"childrenList":[]
,
																												"changed": "false"
																											},
																											{
																												"funcName": "solghost_executeFunction2: -0x100",
																												"returnValue": "",
																												"status": "HAVOC",
																												"childrenList":[]
,
																												"changed": "false"
																											},
																											{
																												"funcName": "solghost_return_func1: 0",
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
																									},
																									{
																										"funcName": "CurveTokenExample",
																										"returnValue": "",
																										"status": "",
																										"childrenList":[
																											{
																												"funcName": "_balances[0x18160dde]: 0",
																												"returnValue": "",
																												"status": "UNKNOWN",
																												"childrenList":[]
,
																												"changed": "false"
																											},
																											{
																												"funcName": "_totalSupply: 0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffc00",
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
																										"funcName": "ERC20",
																										"returnValue": "",
																										"status": "",
																										"childrenList":[
																											{
																												"funcName": "_balances[Curve (0x18160ddc)]: 0 (changed)",
																												"returnValue": "",
																												"status": "UNKNOWN",
																												"childrenList":[]
,
																												"changed": "true"
																											},
																											{
																												"funcName": "_balances[0x18160dde]: 0 (changed)",
																												"returnValue": "",
																												"status": "UNKNOWN",
																												"childrenList":[]
,
																												"changed": "true"
																											}
																										],
																										"storageId": "null"
																									}
																								],
																								"storageId": "28"
																							}
																						]
																					},
																					{
																						"funcName": "Storage State",
																						"returnValue": "",
																						"status": "",
																						"childrenList":[
																							{
																								"funcName": "Curve",
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
																										"funcName": "admin_balances[0]: 0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffc",
																										"returnValue": "",
																										"status": "HAVOC",
																										"childrenList":[]
,
																										"changed": "false"
																									},
																									{
																										"funcName": "admin_balances[1]: 0",
																										"returnValue": "",
																										"status": "HAVOC",
																										"childrenList":[]
,
																										"changed": "false"
																									},
																									{
																										"funcName": "coins_0: 0",
																										"returnValue": "",
																										"status": "HAVOC",
																										"childrenList":[]
,
																										"changed": "false"
																									},
																									{
																										"funcName": "coins_1: ERC20 (0x70a08230)",
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
																										"funcName": "lp_token: CurveTokenExample (0xfffffffffffffffffffffffffffffffffffffffe)",
																										"returnValue": "",
																										"status": "HAVOC",
																										"childrenList":[]
,
																										"changed": "false"
																									},
																									{
																										"funcName": "solghost_executeFunction1: -0x100",
																										"returnValue": "",
																										"status": "HAVOC",
																										"childrenList":[]
,
																										"changed": "false"
																									},
																									{
																										"funcName": "solghost_executeFunction2: -0x100",
																										"returnValue": "",
																										"status": "HAVOC",
																										"childrenList":[]
,
																										"changed": "false"
																									},
																									{
																										"funcName": "solghost_return_func1: 0",
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
																							},
																							{
																								"funcName": "CurveTokenExample",
																								"returnValue": "",
																								"status": "",
																								"childrenList":[
																									{
																										"funcName": "_balances[0x18160dde]: 0",
																										"returnValue": "",
																										"status": "UNKNOWN",
																										"childrenList":[]
,
																										"changed": "false"
																									},
																									{
																										"funcName": "_totalSupply: 0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffc00",
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
																								"funcName": "ERC20",
																								"returnValue": "",
																								"status": "",
																								"childrenList":[
																									{
																										"funcName": "_balances[Curve (0x18160ddc)]: 0",
																										"returnValue": "",
																										"status": "UNKNOWN",
																										"childrenList":[]
,
																										"changed": "false"
																									},
																									{
																										"funcName": "_balances[0x18160dde]: 0",
																										"returnValue": "",
																										"status": "UNKNOWN",
																										"childrenList":[]
,
																										"changed": "false"
																									}
																								],
																								"storageId": "null"
																							}
																						],
																						"storageId": "29"
																					}
																				]
																			},
																			{
																				"funcName": "Storage State",
																				"returnValue": "",
																				"status": "",
																				"childrenList":[
																					{
																						"funcName": "Curve",
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
																								"funcName": "admin_balances[0]: 0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffc",
																								"returnValue": "",
																								"status": "HAVOC",
																								"childrenList":[]
,
																								"changed": "false"
																							},
																							{
																								"funcName": "admin_balances[1]: 0",
																								"returnValue": "",
																								"status": "HAVOC",
																								"childrenList":[]
,
																								"changed": "false"
																							},
																							{
																								"funcName": "coins_0: 0",
																								"returnValue": "",
																								"status": "HAVOC",
																								"childrenList":[]
,
																								"changed": "false"
																							},
																							{
																								"funcName": "coins_1: ERC20 (0x70a08230)",
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
																								"funcName": "lp_token: CurveTokenExample (0xfffffffffffffffffffffffffffffffffffffffe)",
																								"returnValue": "",
																								"status": "HAVOC",
																								"childrenList":[]
,
																								"changed": "false"
																							},
																							{
																								"funcName": "solghost_executeFunction1: -0x100",
																								"returnValue": "",
																								"status": "HAVOC",
																								"childrenList":[]
,
																								"changed": "false"
																							},
																							{
																								"funcName": "solghost_executeFunction2: -0x100",
																								"returnValue": "",
																								"status": "HAVOC",
																								"childrenList":[]
,
																								"changed": "false"
																							},
																							{
																								"funcName": "solghost_return_func1: 0",
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
																					},
																					{
																						"funcName": "CurveTokenExample",
																						"returnValue": "",
																						"status": "",
																						"childrenList":[
																							{
																								"funcName": "_balances[0x18160dde]: 0",
																								"returnValue": "",
																								"status": "UNKNOWN",
																								"childrenList":[]
,
																								"changed": "false"
																							},
																							{
																								"funcName": "_totalSupply: 0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffc00",
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
																						"funcName": "ERC20",
																						"returnValue": "",
																						"status": "",
																						"childrenList":[
																							{
																								"funcName": "_balances[Curve (0x18160ddc)]: 0",
																								"returnValue": "",
																								"status": "UNKNOWN",
																								"childrenList":[]
,
																								"changed": "false"
																							},
																							{
																								"funcName": "_balances[0x18160dde]: 0",
																								"returnValue": "",
																								"status": "UNKNOWN",
																								"childrenList":[]
,
																								"changed": "false"
																							}
																						],
																						"storageId": "null"
																					}
																				],
																				"storageId": "30"
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
														"funcName": "Store at Curve._status: 1",
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
																"funcName": "Curve",
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
																		"funcName": "admin_balances[0]: 0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffc",
																		"returnValue": "",
																		"status": "HAVOC",
																		"childrenList":[]
,
																		"changed": "false"
																	},
																	{
																		"funcName": "admin_balances[1]: 0",
																		"returnValue": "",
																		"status": "HAVOC",
																		"childrenList":[]
,
																		"changed": "false"
																	},
																	{
																		"funcName": "coins_0: 0",
																		"returnValue": "",
																		"status": "HAVOC",
																		"childrenList":[]
,
																		"changed": "false"
																	},
																	{
																		"funcName": "coins_1: ERC20 (0x70a08230)",
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
																		"funcName": "lp_token: CurveTokenExample (0xfffffffffffffffffffffffffffffffffffffffe)",
																		"returnValue": "",
																		"status": "HAVOC",
																		"childrenList":[]
,
																		"changed": "false"
																	},
																	{
																		"funcName": "solghost_executeFunction1: -0x100",
																		"returnValue": "",
																		"status": "HAVOC",
																		"childrenList":[]
,
																		"changed": "false"
																	},
																	{
																		"funcName": "solghost_executeFunction2: -0x100",
																		"returnValue": "",
																		"status": "HAVOC",
																		"childrenList":[]
,
																		"changed": "false"
																	},
																	{
																		"funcName": "solghost_return_func1: 0",
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
															},
															{
																"funcName": "CurveTokenExample",
																"returnValue": "",
																"status": "",
																"childrenList":[
																	{
																		"funcName": "_balances[0x18160dde]: 0",
																		"returnValue": "",
																		"status": "UNKNOWN",
																		"childrenList":[]
,
																		"changed": "false"
																	},
																	{
																		"funcName": "_totalSupply: 0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffc00",
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
																"funcName": "ERC20",
																"returnValue": "",
																"status": "",
																"childrenList":[
																	{
																		"funcName": "_balances[Curve (0x18160ddc)]: 0",
																		"returnValue": "",
																		"status": "UNKNOWN",
																		"childrenList":[]
,
																		"changed": "false"
																	},
																	{
																		"funcName": "_balances[0x18160dde]: 0",
																		"returnValue": "",
																		"status": "UNKNOWN",
																		"childrenList":[]
,
																		"changed": "false"
																	}
																],
																"storageId": "null"
															}
														],
														"storageId": "31"
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
								"funcName": "Curve.getVirtualPrice()",
								"returnValue": "0",
								"status": "SUCCESS",
								"childrenList":[
									{
										"funcName": "(internal) Curve.getVirtualPrice()",
										"returnValue": "0",
										"status": "",
										"childrenList":[
											{
												"funcName": "Load from Curve.admin_balances[0]: 0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffc",
												"returnValue": "",
												"status": "",
												"childrenList":[]

											},
											{
												"funcName": "Load from Curve.admin_balances[1]: 0",
												"returnValue": "",
												"status": "",
												"childrenList":[]

											},
											{
												"funcName": "Load from Curve.coins_1: ERC20 (0x70a08230)",
												"returnValue": "",
												"status": "",
												"childrenList":[]

											},
											{
												"funcName": "ERC20.balanceOf(account=Curve (0x18160ddc))",
												"returnValue": "0",
												"status": "SUCCESS",
												"childrenList":[
													{
														"funcName": "(internal) ERC20.balanceOf(account=Curve (0x18160ddc))",
														"returnValue": "0",
														"status": "",
														"childrenList":[
															{
																"funcName": "Load from ERC20._balances[Curve (0x18160ddc)]: 0",
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
																		"funcName": "Curve",
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
																				"funcName": "admin_balances[0]: 0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffc",
																				"returnValue": "",
																				"status": "HAVOC",
																				"childrenList":[]
,
																				"changed": "false"
																			},
																			{
																				"funcName": "admin_balances[1]: 0",
																				"returnValue": "",
																				"status": "HAVOC",
																				"childrenList":[]
,
																				"changed": "false"
																			},
																			{
																				"funcName": "coins_0: 0",
																				"returnValue": "",
																				"status": "HAVOC",
																				"childrenList":[]
,
																				"changed": "false"
																			},
																			{
																				"funcName": "coins_1: ERC20 (0x70a08230)",
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
																				"funcName": "lp_token: CurveTokenExample (0xfffffffffffffffffffffffffffffffffffffffe)",
																				"returnValue": "",
																				"status": "HAVOC",
																				"childrenList":[]
,
																				"changed": "false"
																			},
																			{
																				"funcName": "solghost_executeFunction1: -0x100",
																				"returnValue": "",
																				"status": "HAVOC",
																				"childrenList":[]
,
																				"changed": "false"
																			},
																			{
																				"funcName": "solghost_executeFunction2: -0x100",
																				"returnValue": "",
																				"status": "HAVOC",
																				"childrenList":[]
,
																				"changed": "false"
																			},
																			{
																				"funcName": "solghost_return_func1: 0",
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
																	},
																	{
																		"funcName": "CurveTokenExample",
																		"returnValue": "",
																		"status": "",
																		"childrenList":[
																			{
																				"funcName": "_balances[0x18160dde]: 0",
																				"returnValue": "",
																				"status": "UNKNOWN",
																				"childrenList":[]
,
																				"changed": "false"
																			},
																			{
																				"funcName": "_totalSupply: 0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffc00",
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
																		"funcName": "ERC20",
																		"returnValue": "",
																		"status": "",
																		"childrenList":[
																			{
																				"funcName": "_balances[Curve (0x18160ddc)]: 0",
																				"returnValue": "",
																				"status": "UNKNOWN",
																				"childrenList":[]
,
																				"changed": "false"
																			},
																			{
																				"funcName": "_balances[0x18160dde]: 0",
																				"returnValue": "",
																				"status": "UNKNOWN",
																				"childrenList":[]
,
																				"changed": "false"
																			}
																		],
																		"storageId": "null"
																	}
																],
																"storageId": "32"
															}
														]
													}
												]
											},
											{
												"funcName": "(internal) Curve._A()",
												"returnValue": "0",
												"status": "",
												"childrenList":[
													{
														"funcName": "Load from Curve.future_A: 0",
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
																"funcName": "Curve",
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
																		"funcName": "admin_balances[0]: 0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffc",
																		"returnValue": "",
																		"status": "HAVOC",
																		"childrenList":[]
,
																		"changed": "false"
																	},
																	{
																		"funcName": "admin_balances[1]: 0",
																		"returnValue": "",
																		"status": "HAVOC",
																		"childrenList":[]
,
																		"changed": "false"
																	},
																	{
																		"funcName": "coins_0: 0",
																		"returnValue": "",
																		"status": "HAVOC",
																		"childrenList":[]
,
																		"changed": "false"
																	},
																	{
																		"funcName": "coins_1: ERC20 (0x70a08230)",
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
																		"funcName": "lp_token: CurveTokenExample (0xfffffffffffffffffffffffffffffffffffffffe)",
																		"returnValue": "",
																		"status": "HAVOC",
																		"childrenList":[]
,
																		"changed": "false"
																	},
																	{
																		"funcName": "solghost_executeFunction1: -0x100",
																		"returnValue": "",
																		"status": "HAVOC",
																		"childrenList":[]
,
																		"changed": "false"
																	},
																	{
																		"funcName": "solghost_executeFunction2: -0x100",
																		"returnValue": "",
																		"status": "HAVOC",
																		"childrenList":[]
,
																		"changed": "false"
																	},
																	{
																		"funcName": "solghost_return_func1: 0",
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
															},
															{
																"funcName": "CurveTokenExample",
																"returnValue": "",
																"status": "",
																"childrenList":[
																	{
																		"funcName": "_balances[0x18160dde]: 0",
																		"returnValue": "",
																		"status": "UNKNOWN",
																		"childrenList":[]
,
																		"changed": "false"
																	},
																	{
																		"funcName": "_totalSupply: 0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffc00",
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
																"funcName": "ERC20",
																"returnValue": "",
																"status": "",
																"childrenList":[
																	{
																		"funcName": "_balances[Curve (0x18160ddc)]: 0",
																		"returnValue": "",
																		"status": "UNKNOWN",
																		"childrenList":[]
,
																		"changed": "false"
																	},
																	{
																		"funcName": "_balances[0x18160dde]: 0",
																		"returnValue": "",
																		"status": "UNKNOWN",
																		"childrenList":[]
,
																		"changed": "false"
																	}
																],
																"storageId": "null"
															}
														],
														"storageId": "33"
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
												"funcName": "Curve.get_D(xp=[0=3, 1=0], amp=0)",
												"returnValue": "3",
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
														"funcName": "(internal) Curve.get_D(xp=uint256[2], amp=0)",
														"returnValue": "3",
														"status": "",
														"childrenList":[
															{
																"funcName": "Storage State",
																"returnValue": "",
																"status": "",
																"childrenList":[
																	{
																		"funcName": "Curve",
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
																				"funcName": "admin_balances[0]: 0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffc",
																				"returnValue": "",
																				"status": "HAVOC",
																				"childrenList":[]
,
																				"changed": "false"
																			},
																			{
																				"funcName": "admin_balances[1]: 0",
																				"returnValue": "",
																				"status": "HAVOC",
																				"childrenList":[]
,
																				"changed": "false"
																			},
																			{
																				"funcName": "coins_0: 0",
																				"returnValue": "",
																				"status": "HAVOC",
																				"childrenList":[]
,
																				"changed": "false"
																			},
																			{
																				"funcName": "coins_1: ERC20 (0x70a08230)",
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
																				"funcName": "lp_token: CurveTokenExample (0xfffffffffffffffffffffffffffffffffffffffe)",
																				"returnValue": "",
																				"status": "HAVOC",
																				"childrenList":[]
,
																				"changed": "false"
																			},
																			{
																				"funcName": "solghost_executeFunction1: -0x100",
																				"returnValue": "",
																				"status": "HAVOC",
																				"childrenList":[]
,
																				"changed": "false"
																			},
																			{
																				"funcName": "solghost_executeFunction2: -0x100",
																				"returnValue": "",
																				"status": "HAVOC",
																				"childrenList":[]
,
																				"changed": "false"
																			},
																			{
																				"funcName": "solghost_return_func1: 0",
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
																	},
																	{
																		"funcName": "CurveTokenExample",
																		"returnValue": "",
																		"status": "",
																		"childrenList":[
																			{
																				"funcName": "_balances[0x18160dde]: 0",
																				"returnValue": "",
																				"status": "UNKNOWN",
																				"childrenList":[]
,
																				"changed": "false"
																			},
																			{
																				"funcName": "_totalSupply: 0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffc00",
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
																		"funcName": "ERC20",
																		"returnValue": "",
																		"status": "",
																		"childrenList":[
																			{
																				"funcName": "_balances[Curve (0x18160ddc)]: 0",
																				"returnValue": "",
																				"status": "UNKNOWN",
																				"childrenList":[]
,
																				"changed": "false"
																			},
																			{
																				"funcName": "_balances[0x18160dde]: 0",
																				"returnValue": "",
																				"status": "UNKNOWN",
																				"childrenList":[]
,
																				"changed": "false"
																			}
																		],
																		"storageId": "null"
																	}
																],
																"storageId": "34"
															}
														]
													}
												]
											},
											{
												"funcName": "Load from Curve.lp_token: CurveTokenExample (0xfffffffffffffffffffffffffffffffffffffffe)",
												"returnValue": "",
												"status": "",
												"childrenList":[]

											},
											{
												"funcName": "CurveTokenExample.totalSupply()",
												"returnValue": "0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffc00",
												"status": "SUCCESS",
												"childrenList":[
													{
														"funcName": "(internal) CurveTokenExample.totalSupply()",
														"returnValue": "0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffc00",
														"status": "",
														"childrenList":[
															{
																"funcName": "Load from CurveTokenExample._totalSupply: 0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffc00",
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
																		"funcName": "Curve",
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
																				"funcName": "admin_balances[0]: 0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffc",
																				"returnValue": "",
																				"status": "HAVOC",
																				"childrenList":[]
,
																				"changed": "false"
																			},
																			{
																				"funcName": "admin_balances[1]: 0",
																				"returnValue": "",
																				"status": "HAVOC",
																				"childrenList":[]
,
																				"changed": "false"
																			},
																			{
																				"funcName": "coins_0: 0",
																				"returnValue": "",
																				"status": "HAVOC",
																				"childrenList":[]
,
																				"changed": "false"
																			},
																			{
																				"funcName": "coins_1: ERC20 (0x70a08230)",
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
																				"funcName": "lp_token: CurveTokenExample (0xfffffffffffffffffffffffffffffffffffffffe)",
																				"returnValue": "",
																				"status": "HAVOC",
																				"childrenList":[]
,
																				"changed": "false"
																			},
																			{
																				"funcName": "solghost_executeFunction1: -0x100",
																				"returnValue": "",
																				"status": "HAVOC",
																				"childrenList":[]
,
																				"changed": "false"
																			},
																			{
																				"funcName": "solghost_executeFunction2: -0x100",
																				"returnValue": "",
																				"status": "HAVOC",
																				"childrenList":[]
,
																				"changed": "false"
																			},
																			{
																				"funcName": "solghost_return_func1: 0",
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
																	},
																	{
																		"funcName": "CurveTokenExample",
																		"returnValue": "",
																		"status": "",
																		"childrenList":[
																			{
																				"funcName": "_balances[0x18160dde]: 0",
																				"returnValue": "",
																				"status": "UNKNOWN",
																				"childrenList":[]
,
																				"changed": "false"
																			},
																			{
																				"funcName": "_totalSupply: 0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffc00",
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
																		"funcName": "ERC20",
																		"returnValue": "",
																		"status": "",
																		"childrenList":[
																			{
																				"funcName": "_balances[Curve (0x18160ddc)]: 0",
																				"returnValue": "",
																				"status": "UNKNOWN",
																				"childrenList":[]
,
																				"changed": "false"
																			},
																			{
																				"funcName": "_balances[0x18160dde]: 0",
																				"returnValue": "",
																				"status": "UNKNOWN",
																				"childrenList":[]
,
																				"changed": "false"
																			}
																		],
																		"storageId": "null"
																	}
																],
																"storageId": "35"
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
														"funcName": "Curve",
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
																"funcName": "admin_balances[0]: 0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffc",
																"returnValue": "",
																"status": "HAVOC",
																"childrenList":[]
,
																"changed": "false"
															},
															{
																"funcName": "admin_balances[1]: 0",
																"returnValue": "",
																"status": "HAVOC",
																"childrenList":[]
,
																"changed": "false"
															},
															{
																"funcName": "coins_0: 0",
																"returnValue": "",
																"status": "HAVOC",
																"childrenList":[]
,
																"changed": "false"
															},
															{
																"funcName": "coins_1: ERC20 (0x70a08230)",
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
																"funcName": "lp_token: CurveTokenExample (0xfffffffffffffffffffffffffffffffffffffffe)",
																"returnValue": "",
																"status": "HAVOC",
																"childrenList":[]
,
																"changed": "false"
															},
															{
																"funcName": "solghost_executeFunction1: -0x100",
																"returnValue": "",
																"status": "HAVOC",
																"childrenList":[]
,
																"changed": "false"
															},
															{
																"funcName": "solghost_executeFunction2: -0x100",
																"returnValue": "",
																"status": "HAVOC",
																"childrenList":[]
,
																"changed": "false"
															},
															{
																"funcName": "solghost_return_func1: 0",
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
													},
													{
														"funcName": "CurveTokenExample",
														"returnValue": "",
														"status": "",
														"childrenList":[
															{
																"funcName": "_balances[0x18160dde]: 0",
																"returnValue": "",
																"status": "UNKNOWN",
																"childrenList":[]
,
																"changed": "false"
															},
															{
																"funcName": "_totalSupply: 0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffc00",
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
														"funcName": "ERC20",
														"returnValue": "",
														"status": "",
														"childrenList":[
															{
																"funcName": "_balances[Curve (0x18160ddc)]: 0",
																"returnValue": "",
																"status": "UNKNOWN",
																"childrenList":[]
,
																"changed": "false"
															},
															{
																"funcName": "_balances[0x18160dde]: 0",
																"returnValue": "",
																"status": "UNKNOWN",
																"childrenList":[]
,
																"changed": "false"
															}
														],
														"storageId": "null"
													}
												],
												"storageId": "36"
											}
										]
									}
								]
							},
							{
								"funcName": "Curve.solghost_executeFunction1()",
								"returnValue": "0xffffffff00",
								"status": "SUCCESS",
								"childrenList":[
									{
										"funcName": "Load from Curve.solghost_executeFunction1: -0x100",
										"returnValue": "",
										"status": "",
										"childrenList":[]

									}
								]
							},
							{
								"funcName": "Curve.coins_1()",
								"returnValue": "ERC20 (0x70a08230)",
								"status": "SUCCESS",
								"childrenList":[
									{
										"funcName": "Load from Curve.coins_1: ERC20 (0x70a08230)",
										"returnValue": "",
										"status": "",
										"childrenList":[]

									}
								]
							},
							{
								"funcName": "Curve.solghost_return_func1()",
								"returnValue": "0",
								"status": "SUCCESS",
								"childrenList":[
									{
										"funcName": "Load from Curve.solghost_return_func1: 0",
										"returnValue": "",
										"status": "",
										"childrenList":[]

									}
								]
							},
							{
								"funcName": "Curve.solghost_executeFunction2()",
								"returnValue": "0xffffffff00",
								"status": "SUCCESS",
								"childrenList":[
									{
										"funcName": "Load from Curve.solghost_executeFunction2: -0x100",
										"returnValue": "",
										"status": "",
										"childrenList":[]

									}
								]
							},
							{
								"funcName": "Curve.lp_token()",
								"returnValue": "CurveTokenExample (0xfffffffffffffffffffffffffffffffffffffffe)",
								"status": "SUCCESS",
								"childrenList":[
									{
										"funcName": "Load from Curve.lp_token: CurveTokenExample (0xfffffffffffffffffffffffffffffffffffffffe)",
										"returnValue": "",
										"status": "",
										"childrenList":[]

									}
								]
							},
							{
								"funcName": "Curve.coins_0()",
								"returnValue": "0",
								"status": "SUCCESS",
								"childrenList":[
									{
										"funcName": "Load from Curve.coins_0: 0",
										"returnValue": "",
										"status": "",
										"childrenList":[]

									}
								]
							},
							{
								"funcName": "Curve._balances(_value=0)",
								"returnValue": "[]",
								"status": "SUCCESS",
								"childrenList":[
									{
										"funcName": "Load from Curve.admin_balances[0]: 0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffc",
										"returnValue": "",
										"status": "",
										"childrenList":[]

									},
									{
										"funcName": "Load from Curve.admin_balances[1]: 0",
										"returnValue": "",
										"status": "",
										"childrenList":[]

									},
									{
										"funcName": "Load from Curve.coins_1: ERC20 (0x70a08230)",
										"returnValue": "",
										"status": "",
										"childrenList":[]

									},
									{
										"funcName": "ERC20.balanceOf(account=Curve (0x18160ddc))",
										"returnValue": "0",
										"status": "SUCCESS",
										"childrenList":[
											{
												"funcName": "(internal) ERC20.balanceOf(account=Curve (0x18160ddc))",
												"returnValue": "0",
												"status": "",
												"childrenList":[
													{
														"funcName": "Load from ERC20._balances[Curve (0x18160ddc)]: 0",
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
																"funcName": "Curve",
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
																		"funcName": "admin_balances[0]: 0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffc",
																		"returnValue": "",
																		"status": "HAVOC",
																		"childrenList":[]
,
																		"changed": "false"
																	},
																	{
																		"funcName": "admin_balances[1]: 0",
																		"returnValue": "",
																		"status": "HAVOC",
																		"childrenList":[]
,
																		"changed": "false"
																	},
																	{
																		"funcName": "coins_0: 0",
																		"returnValue": "",
																		"status": "HAVOC",
																		"childrenList":[]
,
																		"changed": "false"
																	},
																	{
																		"funcName": "coins_1: ERC20 (0x70a08230)",
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
																		"funcName": "lp_token: CurveTokenExample (0xfffffffffffffffffffffffffffffffffffffffe)",
																		"returnValue": "",
																		"status": "HAVOC",
																		"childrenList":[]
,
																		"changed": "false"
																	},
																	{
																		"funcName": "solghost_executeFunction1: -0x100",
																		"returnValue": "",
																		"status": "HAVOC",
																		"childrenList":[]
,
																		"changed": "false"
																	},
																	{
																		"funcName": "solghost_executeFunction2: -0x100",
																		"returnValue": "",
																		"status": "HAVOC",
																		"childrenList":[]
,
																		"changed": "false"
																	},
																	{
																		"funcName": "solghost_return_func1: 0",
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
															},
															{
																"funcName": "CurveTokenExample",
																"returnValue": "",
																"status": "",
																"childrenList":[
																	{
																		"funcName": "_balances[0x18160dde]: 0",
																		"returnValue": "",
																		"status": "UNKNOWN",
																		"childrenList":[]
,
																		"changed": "false"
																	},
																	{
																		"funcName": "_totalSupply: 0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffc00",
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
																"funcName": "ERC20",
																"returnValue": "",
																"status": "",
																"childrenList":[
																	{
																		"funcName": "_balances[Curve (0x18160ddc)]: 0",
																		"returnValue": "",
																		"status": "UNKNOWN",
																		"childrenList":[]
,
																		"changed": "false"
																	},
																	{
																		"funcName": "_balances[0x18160dde]: 0",
																		"returnValue": "",
																		"status": "UNKNOWN",
																		"childrenList":[]
,
																		"changed": "false"
																	}
																],
																"storageId": "null"
															}
														],
														"storageId": "37"
													}
												]
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
							},
							{
								"funcName": "Curve.get_D(xp=[], amp=0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff (MAX_UINT256))",
								"returnValue": "0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff (MAX_UINT256)",
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
										"funcName": "(internal) Curve.get_D(xp=uint256[2], amp=0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff (MAX_UINT256))",
										"returnValue": "0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff (MAX_UINT256)",
										"status": "",
										"childrenList":[
											{
												"funcName": "Storage State",
												"returnValue": "",
												"status": "",
												"childrenList":[
													{
														"funcName": "Curve",
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
																"funcName": "admin_balances[0]: 0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffc",
																"returnValue": "",
																"status": "HAVOC",
																"childrenList":[]
,
																"changed": "false"
															},
															{
																"funcName": "admin_balances[1]: 0",
																"returnValue": "",
																"status": "HAVOC",
																"childrenList":[]
,
																"changed": "false"
															},
															{
																"funcName": "coins_0: 0",
																"returnValue": "",
																"status": "HAVOC",
																"childrenList":[]
,
																"changed": "false"
															},
															{
																"funcName": "coins_1: ERC20 (0x70a08230)",
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
																"funcName": "lp_token: CurveTokenExample (0xfffffffffffffffffffffffffffffffffffffffe)",
																"returnValue": "",
																"status": "HAVOC",
																"childrenList":[]
,
																"changed": "false"
															},
															{
																"funcName": "solghost_executeFunction1: -0x100",
																"returnValue": "",
																"status": "HAVOC",
																"childrenList":[]
,
																"changed": "false"
															},
															{
																"funcName": "solghost_executeFunction2: -0x100",
																"returnValue": "",
																"status": "HAVOC",
																"childrenList":[]
,
																"changed": "false"
															},
															{
																"funcName": "solghost_return_func1: 0",
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
													},
													{
														"funcName": "CurveTokenExample",
														"returnValue": "",
														"status": "",
														"childrenList":[
															{
																"funcName": "_balances[0x18160dde]: 0",
																"returnValue": "",
																"status": "UNKNOWN",
																"childrenList":[]
,
																"changed": "false"
															},
															{
																"funcName": "_totalSupply: 0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffc00",
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
														"funcName": "ERC20",
														"returnValue": "",
														"status": "",
														"childrenList":[
															{
																"funcName": "_balances[Curve (0x18160ddc)]: 0",
																"returnValue": "",
																"status": "UNKNOWN",
																"childrenList":[]
,
																"changed": "false"
															},
															{
																"funcName": "_balances[0x18160dde]: 0",
																"returnValue": "",
																"status": "UNKNOWN",
																"childrenList":[]
,
																"changed": "false"
															}
														],
														"storageId": "null"
													}
												],
												"storageId": "38"
											}
										]
									}
								]
							},
							{
								"funcName": "Possible view reentrancy weakness",
								"returnValue": "",
								"status": "",
								"childrenList":[]

							}
						]
					}
				}
,				{
					 "tableRow": {
						"funcName": "func1_caller()",
						"result": "SUCCESS",
						"time": "0",
						"graph_link": "",
						"preoptimized_link": "PreoptimizedRule-viewReentrancy-func1_callerLPRP.html",
						"presimplified_link": "PresimplifiedRule-viewReentrancy-func1_callerLPRP.html",
						"prelastopt_link": "PrelastoptRule-viewReentrancy-func1_callerLPRP.html",
						"presolver_link": "PresolverRule-viewReentrancy-func1_callerLPRP.html"
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
						"address": "ce4604a000000000000000000000001e",
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
						"address": "ce4604a0000000000000000000000027",
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
						"name": "Curve",
						"address": "ce4604a000000000000000000000000c",
						"pre_state": "{11=274184521717934524641157099916833587239, 12=274184521717934524641157099916833587230}",
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