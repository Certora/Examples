data = {
	"contractName": "Pool",
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
						"ruleName": "flashLoanIncreasesBalance",
						"result": "FAIL",
						"time": "3",
						"graph_link": "Report-flashLoanIncreasesBalance-example1.html",
						"preoptimized_link": "PreoptimizedRule-flashLoanIncreasesBalance.html",
						"presimplified_link": "PresimplifiedRule-flashLoanIncreasesBalance.html",
						"prelastopt_link": "PrelastoptRule-flashLoanIncreasesBalance.html",
						"presolver_link": "PresolverRule-flashLoanIncreasesBalance.html"
					},
					"isMultiRule": false,
					 "variables": {
						"receiver": "TransferReceiver (0xfffe)",
						"amount": "3",
						"e.msg.sender": "0xffff",
						"e.msg.value": "0",
						"e.tx.origin": "0x401",
						"e.block.coinbase": "0x402",
						"e.block.difficulty": "10",
						"e.block.gaslimit": "9",
						"e.block.number": "6",
						"e.block.timestamp": "2",
						"balance_before": "8",
						"lastHasThrown": "false",
						"lastReverted": "false",
						"balance_after": "4",
						"Pool": "Pool (15)",
						"identity": "identity (0xffffffffffffffffffffffffffffffffffffffff (MAX_EVM_ADDRESS))",
						"TransferReceiver": "TransferReceiver (0xfffe)",
						"TrivialReceiver": "TrivialReceiver (0x95ea7b3)"
					},
					"assertMessage":[
						"flash loans must not decrease the contract's underlying balance"
					],
					 "failureCauses": {
						"expr": "!(balance_after&gt;=balance_before)"
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
									"caller": "Pool.flashLoan(address,uint256)",
									"callee": "[?].executeOperation(uint256, uint256, address)",
									"summmary": "DISPATCHER(optimistic = true)",
									"comments":[
										{
											"alternative callees": "[TransferReceiver | TrivialReceiver]"
										},
										{
											"callee resolution": "callee contract unresolved; callee sighash resolved"
										},
										{
											"summary application reason": "declared at flashLoan_dispatcher.spec:29:70 to apply only to calls without available callee implementation"
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
					},
					 "callTrace": {
						"funcName": "flashLoanIncreasesBalance",
						"returnValue": "",
						"status": "",
						"childrenList":[
							{
								"funcName": "Storage State",
								"returnValue": "",
								"status": "",
								"childrenList":[
									{
										"funcName": "TransferReceiver",
										"returnValue": "",
										"status": "",
										"childrenList":[
											{
												"funcName": "pool: Pool (15)",
												"returnValue": "",
												"status": "HAVOC",
												"childrenList":[]
,
												"changed": "false"
											},
											{
												"funcName": "transfer_amount: 5",
												"returnValue": "",
												"status": "HAVOC",
												"childrenList":[]
,
												"changed": "false"
											},
											{
												"funcName": "underlying: identity (0xffffffffffffffffffffffffffffffffffffffff (MAX_EVM_ADDRESS))",
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
										"funcName": "Asset",
										"returnValue": "",
										"status": "",
										"childrenList":[
											{
												"funcName": "_allowance[Pool (15)][Pool (15)]: 7",
												"returnValue": "",
												"status": "HAVOC",
												"childrenList":[]
,
												"changed": "false"
											},
											{
												"funcName": "_allowance[Pool (15)][TransferReceiver (0xfffe)]: 5",
												"returnValue": "",
												"status": "HAVOC",
												"childrenList":[]
,
												"changed": "false"
											},
											{
												"funcName": "_allowance[0xffff][Pool (15)]: 4",
												"returnValue": "",
												"status": "HAVOC",
												"childrenList":[]
,
												"changed": "false"
											},
											{
												"funcName": "_balanceOf[Pool (15)]: 8",
												"returnValue": "",
												"status": "HAVOC",
												"childrenList":[]
,
												"changed": "false"
											},
											{
												"funcName": "_balanceOf[TransferReceiver (0xfffe)]: 0",
												"returnValue": "",
												"status": "HAVOC",
												"childrenList":[]
,
												"changed": "false"
											},
											{
												"funcName": "_balanceOf[0xffff]: 1",
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
										"funcName": "Pool",
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
												"funcName": "asset: identity (0xffffffffffffffffffffffffffffffffffffffff (MAX_EVM_ADDRESS))",
												"returnValue": "",
												"status": "HAVOC",
												"childrenList":[]
,
												"changed": "false"
											},
											{
												"funcName": "feeRate: 0xd06",
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
								"funcName": "require e.msg.sender != currentContract",
								"returnValue": "",
								"status": "",
								"childrenList":[
									{
										"funcName": "e.msg.sender != currentContract",
										"returnValue": "true",
										"status": "",
										"childrenList":[
											{
												"funcName": "e.msg.sender == currentContract",
												"returnValue": "false",
												"status": "",
												"childrenList":[
													{
														"funcName": "e.msg.sender",
														"returnValue": "*",
														"status": "",
														"childrenList":[]

													},
													{
														"funcName": "currentContract",
														"returnValue": "*",
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
								"funcName": "balance_before = Asset.balanceOf(account=currentContract)",
								"returnValue": "",
								"status": "",
								"childrenList":[
									{
										"funcName": "Asset.balanceOf(account=X)",
										"returnValue": "8",
										"status": "SUCCESS",
										"childrenList":[
											{
												"funcName": "(internal) Asset.balanceOf(account=Pool (15))",
												"returnValue": "8",
												"status": "",
												"childrenList":[
													{
														"funcName": "Load from Asset._balanceOf[Pool (15)]: 8",
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
																"funcName": "TransferReceiver",
																"returnValue": "",
																"status": "",
																"childrenList":[
																	{
																		"funcName": "pool: Pool (15)",
																		"returnValue": "",
																		"status": "HAVOC",
																		"childrenList":[]
,
																		"changed": "false"
																	},
																	{
																		"funcName": "transfer_amount: 5",
																		"returnValue": "",
																		"status": "HAVOC",
																		"childrenList":[]
,
																		"changed": "false"
																	},
																	{
																		"funcName": "underlying: identity (0xffffffffffffffffffffffffffffffffffffffff (MAX_EVM_ADDRESS))",
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
																"funcName": "Asset",
																"returnValue": "",
																"status": "",
																"childrenList":[
																	{
																		"funcName": "_allowance[Pool (15)][Pool (15)]: 7",
																		"returnValue": "",
																		"status": "HAVOC",
																		"childrenList":[]
,
																		"changed": "false"
																	},
																	{
																		"funcName": "_allowance[Pool (15)][TransferReceiver (0xfffe)]: 5",
																		"returnValue": "",
																		"status": "HAVOC",
																		"childrenList":[]
,
																		"changed": "false"
																	},
																	{
																		"funcName": "_allowance[0xffff][Pool (15)]: 4",
																		"returnValue": "",
																		"status": "HAVOC",
																		"childrenList":[]
,
																		"changed": "false"
																	},
																	{
																		"funcName": "_balanceOf[Pool (15)]: 8",
																		"returnValue": "",
																		"status": "HAVOC",
																		"childrenList":[]
,
																		"changed": "false"
																	},
																	{
																		"funcName": "_balanceOf[TransferReceiver (0xfffe)]: 0",
																		"returnValue": "",
																		"status": "HAVOC",
																		"childrenList":[]
,
																		"changed": "false"
																	},
																	{
																		"funcName": "_balanceOf[0xffff]: 1",
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
																"funcName": "Pool",
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
																		"funcName": "asset: identity (0xffffffffffffffffffffffffffffffffffffffff (MAX_EVM_ADDRESS))",
																		"returnValue": "",
																		"status": "HAVOC",
																		"childrenList":[]
,
																		"changed": "false"
																	},
																	{
																		"funcName": "feeRate: 0xd06",
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
									}
								]
							},
							{
								"funcName": "Pool.flashLoan(e, receiver, amount)",
								"returnValue": "",
								"status": "",
								"childrenList":[
									{
										"funcName": "Pool.flashLoan(receiverAddress=X, amount=X)",
										"returnValue": "",
										"status": "SUCCESS",
										"childrenList":[
											{
												"funcName": "sender: 0xffff; receiver: Pool (15); transferred amount: 0",
												"returnValue": "",
												"status": "TRANSFER",
												"childrenList":[
													{
														"funcName": "Load from sender.balance: 0",
														"returnValue": "",
														"status": "",
														"childrenList":[]

													},
													{
														"funcName": "Store at sender.balance: 0",
														"returnValue": "",
														"status": "",
														"childrenList":[]

													},
													{
														"funcName": "Load from receiver.balance: 0",
														"returnValue": "",
														"status": "",
														"childrenList":[]

													},
													{
														"funcName": "Store at receiver.balance: 0",
														"returnValue": "",
														"status": "",
														"childrenList":[]

													}
												]
											},
											{
												"funcName": "(internal) Pool.flashLoan(receiverAddress=TransferReceiver (0xfffe), amount=3)",
												"returnValue": "",
												"status": "",
												"childrenList":[
													{
														"funcName": "Load from Pool._status: 0",
														"returnValue": "",
														"status": "",
														"childrenList":[]

													},
													{
														"funcName": "Store at Pool._status: 2",
														"returnValue": "",
														"status": "",
														"childrenList":[]

													},
													{
														"funcName": "(internal) Pool.calcPremium(amount=3)",
														"returnValue": "1",
														"status": "",
														"childrenList":[
															{
																"funcName": "Load from Pool.feeRate: 0xd06",
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
																		"funcName": "TransferReceiver",
																		"returnValue": "",
																		"status": "",
																		"childrenList":[
																			{
																				"funcName": "pool: Pool (15)",
																				"returnValue": "",
																				"status": "HAVOC",
																				"childrenList":[]
,
																				"changed": "false"
																			},
																			{
																				"funcName": "transfer_amount: 5",
																				"returnValue": "",
																				"status": "HAVOC",
																				"childrenList":[]
,
																				"changed": "false"
																			},
																			{
																				"funcName": "underlying: identity (0xffffffffffffffffffffffffffffffffffffffff (MAX_EVM_ADDRESS))",
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
																		"funcName": "Asset",
																		"returnValue": "",
																		"status": "",
																		"childrenList":[
																			{
																				"funcName": "_allowance[Pool (15)][Pool (15)]: 7",
																				"returnValue": "",
																				"status": "HAVOC",
																				"childrenList":[]
,
																				"changed": "false"
																			},
																			{
																				"funcName": "_allowance[Pool (15)][TransferReceiver (0xfffe)]: 5",
																				"returnValue": "",
																				"status": "HAVOC",
																				"childrenList":[]
,
																				"changed": "false"
																			},
																			{
																				"funcName": "_allowance[0xffff][Pool (15)]: 4",
																				"returnValue": "",
																				"status": "HAVOC",
																				"childrenList":[]
,
																				"changed": "false"
																			},
																			{
																				"funcName": "_balanceOf[Pool (15)]: 8",
																				"returnValue": "",
																				"status": "HAVOC",
																				"childrenList":[]
,
																				"changed": "false"
																			},
																			{
																				"funcName": "_balanceOf[TransferReceiver (0xfffe)]: 0",
																				"returnValue": "",
																				"status": "HAVOC",
																				"childrenList":[]
,
																				"changed": "false"
																			},
																			{
																				"funcName": "_balanceOf[0xffff]: 1",
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
																		"funcName": "Pool",
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
																				"funcName": "asset: identity (0xffffffffffffffffffffffffffffffffffffffff (MAX_EVM_ADDRESS))",
																				"returnValue": "",
																				"status": "HAVOC",
																				"childrenList":[]
,
																				"changed": "false"
																			},
																			{
																				"funcName": "feeRate: 0xd06",
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
													},
													{
														"funcName": "Load from Pool.asset: identity (0xffffffffffffffffffffffffffffffffffffffff (MAX_EVM_ADDRESS))",
														"returnValue": "",
														"status": "",
														"childrenList":[]

													},
													{
														"funcName": "Asset.transferFrom(from=Pool (15), recipient=0xffff, amount=3)",
														"returnValue": "true",
														"status": "SUCCESS",
														"childrenList":[
															{
																"funcName": "Load from Asset._allowance[Pool (15)][Pool (15)]: 7",
																"returnValue": "",
																"status": "",
																"childrenList":[]

															},
															{
																"funcName": "Load from Asset._allowance[Pool (15)][Pool (15)]: 7",
																"returnValue": "",
																"status": "",
																"childrenList":[]

															},
															{
																"funcName": "Store at Asset._allowance[Pool (15)][Pool (15)]: 4",
																"returnValue": "",
																"status": "",
																"childrenList":[]

															},
															{
																"funcName": "Load from Asset._balanceOf[Pool (15)]: 8",
																"returnValue": "",
																"status": "",
																"childrenList":[]

															},
															{
																"funcName": "Store at Asset._balanceOf[Pool (15)]: 5",
																"returnValue": "",
																"status": "",
																"childrenList":[]

															},
															{
																"funcName": "Load from Asset._balanceOf[0xffff]: 1",
																"returnValue": "",
																"status": "",
																"childrenList":[]

															},
															{
																"funcName": "Store at Asset._balanceOf[0xffff]: 4",
																"returnValue": "",
																"status": "",
																"childrenList":[]

															}
														]
													},
													{
														"funcName": "executeOperation(uint256,uint256,address): UNRESOLVED DISPATCHER(optimistic = true) summary @ flashLoan_dispatcher.spec:29:70",
														"returnValue": "",
														"status": "DISPATCHER",
														"childrenList":[
															{
																"funcName": "TransferReceiver.executeOperation(amount=3, premium=1, initiator=0xffff)",
																"returnValue": "true",
																"status": "SUCCESS",
																"childrenList":[
																	{
																		"funcName": "Load from TransferReceiver.underlying: identity (0xffffffffffffffffffffffffffffffffffffffff (MAX_EVM_ADDRESS))",
																		"returnValue": "",
																		"status": "",
																		"childrenList":[]

																	},
																	{
																		"funcName": "Load from TransferReceiver.pool: Pool (15)",
																		"returnValue": "",
																		"status": "",
																		"childrenList":[]

																	},
																	{
																		"funcName": "Load from TransferReceiver.transfer_amount: 5",
																		"returnValue": "",
																		"status": "",
																		"childrenList":[]

																	},
																	{
																		"funcName": "Asset.transferFrom(from=Pool (15), recipient=TransferReceiver (0xfffe), amount=5)",
																		"returnValue": "true",
																		"status": "SUCCESS",
																		"childrenList":[
																			{
																				"funcName": "Load from Asset._allowance[Pool (15)][TransferReceiver (0xfffe)]: 5",
																				"returnValue": "",
																				"status": "",
																				"childrenList":[]

																			},
																			{
																				"funcName": "Load from Asset._allowance[Pool (15)][TransferReceiver (0xfffe)]: 5",
																				"returnValue": "",
																				"status": "",
																				"childrenList":[]

																			},
																			{
																				"funcName": "Store at Asset._allowance[Pool (15)][TransferReceiver (0xfffe)]: 0",
																				"returnValue": "",
																				"status": "",
																				"childrenList":[]

																			},
																			{
																				"funcName": "Load from Asset._balanceOf[Pool (15)]: 5",
																				"returnValue": "",
																				"status": "",
																				"childrenList":[]

																			},
																			{
																				"funcName": "Store at Asset._balanceOf[Pool (15)]: 0",
																				"returnValue": "",
																				"status": "",
																				"childrenList":[]

																			},
																			{
																				"funcName": "Load from Asset._balanceOf[TransferReceiver (0xfffe)]: 0",
																				"returnValue": "",
																				"status": "",
																				"childrenList":[]

																			},
																			{
																				"funcName": "Store at Asset._balanceOf[TransferReceiver (0xfffe)]: 5",
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
														"funcName": "Load from Pool.asset: identity (0xffffffffffffffffffffffffffffffffffffffff (MAX_EVM_ADDRESS))",
														"returnValue": "",
														"status": "",
														"childrenList":[]

													},
													{
														"funcName": "Asset.transferFrom(from=0xffff, recipient=Pool (15), amount=4)",
														"returnValue": "true",
														"status": "SUCCESS",
														"childrenList":[
															{
																"funcName": "Load from Asset._allowance[0xffff][Pool (15)]: 4",
																"returnValue": "",
																"status": "",
																"childrenList":[]

															},
															{
																"funcName": "Load from Asset._allowance[0xffff][Pool (15)]: 4",
																"returnValue": "",
																"status": "",
																"childrenList":[]

															},
															{
																"funcName": "Store at Asset._allowance[0xffff][Pool (15)]: 0",
																"returnValue": "",
																"status": "",
																"childrenList":[]

															},
															{
																"funcName": "Load from Asset._balanceOf[0xffff]: 4",
																"returnValue": "",
																"status": "",
																"childrenList":[]

															},
															{
																"funcName": "Store at Asset._balanceOf[0xffff]: 0",
																"returnValue": "",
																"status": "",
																"childrenList":[]

															},
															{
																"funcName": "Load from Asset._balanceOf[Pool (15)]: 0",
																"returnValue": "",
																"status": "",
																"childrenList":[]

															},
															{
																"funcName": "Store at Asset._balanceOf[Pool (15)]: 4",
																"returnValue": "",
																"status": "",
																"childrenList":[]

															}
														]
													},
													{
														"funcName": "Store at Pool._status: 1",
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
																"funcName": "TransferReceiver",
																"returnValue": "",
																"status": "",
																"childrenList":[
																	{
																		"funcName": "pool: Pool (15)",
																		"returnValue": "",
																		"status": "HAVOC",
																		"childrenList":[]
,
																		"changed": "false"
																	},
																	{
																		"funcName": "transfer_amount: 5",
																		"returnValue": "",
																		"status": "HAVOC",
																		"childrenList":[]
,
																		"changed": "false"
																	},
																	{
																		"funcName": "underlying: identity (0xffffffffffffffffffffffffffffffffffffffff (MAX_EVM_ADDRESS))",
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
																"funcName": "Asset",
																"returnValue": "",
																"status": "",
																"childrenList":[
																	{
																		"funcName": "_allowance[Pool (15)][Pool (15)]: 4 (changed)",
																		"returnValue": "",
																		"status": "HAVOC DEPENDENT",
																		"childrenList":[]
,
																		"changed": "true"
																	},
																	{
																		"funcName": "_allowance[Pool (15)][TransferReceiver (0xfffe)]: 0 (changed)",
																		"returnValue": "",
																		"status": "HAVOC DEPENDENT",
																		"childrenList":[]
,
																		"changed": "true"
																	},
																	{
																		"funcName": "_allowance[0xffff][Pool (15)]: 0 (changed)",
																		"returnValue": "",
																		"status": "UNKNOWN",
																		"childrenList":[]
,
																		"changed": "true"
																	},
																	{
																		"funcName": "_balanceOf[Pool (15)]: 4 (changed)",
																		"returnValue": "",
																		"status": "UNKNOWN",
																		"childrenList":[]
,
																		"changed": "true"
																	},
																	{
																		"funcName": "_balanceOf[TransferReceiver (0xfffe)]: 5 (changed)",
																		"returnValue": "",
																		"status": "HAVOC DEPENDENT",
																		"childrenList":[]
,
																		"changed": "true"
																	},
																	{
																		"funcName": "_balanceOf[0xffff]: 0 (changed)",
																		"returnValue": "",
																		"status": "UNKNOWN",
																		"childrenList":[]
,
																		"changed": "true"
																	}
																],
																"storageId": "null"
															},
															{
																"funcName": "Pool",
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
																		"funcName": "asset: identity (0xffffffffffffffffffffffffffffffffffffffff (MAX_EVM_ADDRESS))",
																		"returnValue": "",
																		"status": "HAVOC",
																		"childrenList":[]
,
																		"changed": "false"
																	},
																	{
																		"funcName": "feeRate: 0xd06",
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
									}
								]
							},
							{
								"funcName": "balance_after = Asset.balanceOf(account=currentContract)",
								"returnValue": "",
								"status": "",
								"childrenList":[
									{
										"funcName": "Asset.balanceOf(account=X)",
										"returnValue": "4",
										"status": "SUCCESS",
										"childrenList":[
											{
												"funcName": "(internal) Asset.balanceOf(account=Pool (15))",
												"returnValue": "4",
												"status": "",
												"childrenList":[
													{
														"funcName": "Load from Asset._balanceOf[Pool (15)]: 4",
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
																"funcName": "TransferReceiver",
																"returnValue": "",
																"status": "",
																"childrenList":[
																	{
																		"funcName": "pool: Pool (15)",
																		"returnValue": "",
																		"status": "HAVOC",
																		"childrenList":[]
,
																		"changed": "false"
																	},
																	{
																		"funcName": "transfer_amount: 5",
																		"returnValue": "",
																		"status": "HAVOC",
																		"childrenList":[]
,
																		"changed": "false"
																	},
																	{
																		"funcName": "underlying: identity (0xffffffffffffffffffffffffffffffffffffffff (MAX_EVM_ADDRESS))",
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
																"funcName": "Asset",
																"returnValue": "",
																"status": "",
																"childrenList":[
																	{
																		"funcName": "_allowance[Pool (15)][Pool (15)]: 4",
																		"returnValue": "",
																		"status": "HAVOC DEPENDENT",
																		"childrenList":[]
,
																		"changed": "false"
																	},
																	{
																		"funcName": "_allowance[Pool (15)][TransferReceiver (0xfffe)]: 0",
																		"returnValue": "",
																		"status": "HAVOC DEPENDENT",
																		"childrenList":[]
,
																		"changed": "false"
																	},
																	{
																		"funcName": "_allowance[0xffff][Pool (15)]: 0",
																		"returnValue": "",
																		"status": "UNKNOWN",
																		"childrenList":[]
,
																		"changed": "false"
																	},
																	{
																		"funcName": "_balanceOf[Pool (15)]: 4",
																		"returnValue": "",
																		"status": "UNKNOWN",
																		"childrenList":[]
,
																		"changed": "false"
																	},
																	{
																		"funcName": "_balanceOf[TransferReceiver (0xfffe)]: 5",
																		"returnValue": "",
																		"status": "HAVOC DEPENDENT",
																		"childrenList":[]
,
																		"changed": "false"
																	},
																	{
																		"funcName": "_balanceOf[0xffff]: 0",
																		"returnValue": "",
																		"status": "UNKNOWN",
																		"childrenList":[]
,
																		"changed": "false"
																	}
																],
																"storageId": "null"
															},
															{
																"funcName": "Pool",
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
																		"funcName": "asset: identity (0xffffffffffffffffffffffffffffffffffffffff (MAX_EVM_ADDRESS))",
																		"returnValue": "",
																		"status": "HAVOC",
																		"childrenList":[]
,
																		"changed": "false"
																	},
																	{
																		"funcName": "feeRate: 0xd06",
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
											}
										]
									}
								]
							},
							{
								"funcName": "assert balance_after >= balance_before",
								"returnValue": "",
								"status": "",
								"childrenList":[
									{
										"funcName": "balance_after >= balance_before",
										"returnValue": "false",
										"status": "",
										"childrenList":[
											{
												"funcName": "balance_after",
												"returnValue": "4",
												"status": "",
												"childrenList":[]

											},
											{
												"funcName": "balance_before",
												"returnValue": "8",
												"status": "",
												"childrenList":[]

											}
										]
									},
									{
										"funcName": "Storage State",
										"returnValue": "",
										"status": "",
										"childrenList":[
											{
												"funcName": "TransferReceiver",
												"returnValue": "",
												"status": "",
												"childrenList":[
													{
														"funcName": "pool: Pool (15)",
														"returnValue": "",
														"status": "HAVOC",
														"childrenList":[]
,
														"changed": "false"
													},
													{
														"funcName": "transfer_amount: 5",
														"returnValue": "",
														"status": "HAVOC",
														"childrenList":[]
,
														"changed": "false"
													},
													{
														"funcName": "underlying: identity (0xffffffffffffffffffffffffffffffffffffffff (MAX_EVM_ADDRESS))",
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
												"funcName": "Asset",
												"returnValue": "",
												"status": "",
												"childrenList":[
													{
														"funcName": "_allowance[Pool (15)][Pool (15)]: 4",
														"returnValue": "",
														"status": "HAVOC DEPENDENT",
														"childrenList":[]
,
														"changed": "false"
													},
													{
														"funcName": "_allowance[Pool (15)][TransferReceiver (0xfffe)]: 0",
														"returnValue": "",
														"status": "HAVOC DEPENDENT",
														"childrenList":[]
,
														"changed": "false"
													},
													{
														"funcName": "_allowance[0xffff][Pool (15)]: 0",
														"returnValue": "",
														"status": "UNKNOWN",
														"childrenList":[]
,
														"changed": "false"
													},
													{
														"funcName": "_balanceOf[Pool (15)]: 4",
														"returnValue": "",
														"status": "UNKNOWN",
														"childrenList":[]
,
														"changed": "false"
													},
													{
														"funcName": "_balanceOf[TransferReceiver (0xfffe)]: 5",
														"returnValue": "",
														"status": "HAVOC DEPENDENT",
														"childrenList":[]
,
														"changed": "false"
													},
													{
														"funcName": "_balanceOf[0xffff]: 0",
														"returnValue": "",
														"status": "UNKNOWN",
														"childrenList":[]
,
														"changed": "false"
													}
												],
												"storageId": "null"
											},
											{
												"funcName": "Pool",
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
														"funcName": "asset: identity (0xffffffffffffffffffffffffffffffffffffffff (MAX_EVM_ADDRESS))",
														"returnValue": "",
														"status": "HAVOC",
														"childrenList":[]
,
														"changed": "false"
													},
													{
														"funcName": "feeRate: 0xd06",
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
					}
				},
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
						"funcName": "Asset.balanceOf(address)",
						"result": "SUCCESS",
						"time": "0",
						"graph_link": "",
						"preoptimized_link": "PreoptimizedRule-envfreeFuncsStaticCheck-Asset.balanceOfLPADRRP.html",
						"presimplified_link": "PresimplifiedRule-envfreeFuncsStaticCheck-Asset.balanceOfLPADRRP.html",
						"prelastopt_link": "PrelastoptRule-envfreeFuncsStaticCheck-Asset.balanceOfLPADRRP.html",
						"presolver_link": "PresolverRule-envfreeFuncsStaticCheck-Asset.balanceOfLPADRRP.html"
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
						"address": "ce4604a000000000000000000000000d",
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
						"name": "Pool",
						"address": "ce4604a0000000000000000000000017",
						"pre_state": "{4=274184521717934524641157099916833587213}",
						"methodsNames":[
							"deposit(uint256)",
							"calcPremium(uint256)",
							"transferFrom(address,address,uint256)",
							"withdraw(uint256)",
							"amountToShares(uint256)",
							"asset()",
							"transfer(address,uint256)",
							"balanceOf(address)",
							"approve(address,uint256)",
							"assetBalance()",
							"feeRate()",
							"sharesToAmount(uint256)",
							"flashLoan(address,uint256)",
							"totalSupply()",
							"allowance(address,address)"
						]
					}
				},
				{
					 "tableRow": {
						"name": "TransferReceiver",
						"address": "ce4604a0000000000000000000000003",
						"pre_state": "{0=274184521717934524641157099916833587213}",
						"methodsNames":[
							"executeOperation(uint256,uint256,address)"
						]
					}
				},
				{
					 "tableRow": {
						"name": "TrivialReceiver",
						"address": "ce4604a0000000000000000000000008",
						"pre_state": "{}",
						"methodsNames":[
							"executeOperation(uint256,uint256,address)"
						]
					}
				}
			]
		}
	}