data = {
	"contractName": "BallGame",
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
						"ruleName": "playerTwoNeverWins",
						"result": "FAIL",
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
						"ruleName": "playerTwoNeverWins_instate",
						"result": "SUCCESS",
						"time": "0",
						"graph_link": "",
						"preoptimized_link": "PreoptimizedRule-playerTwoNeverWins_instate.html",
						"presimplified_link": "PresimplifiedRule-playerTwoNeverWins_instate.html",
						"prelastopt_link": "PrelastoptRule-playerTwoNeverWins_instate.html",
						"presolver_link": "PresolverRule-playerTwoNeverWins_instate.html"
					},
					"isMultiRule": false,
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
						"funcName": "ballPosition()",
						"result": "SUCCESS",
						"time": "0",
						"graph_link": "",
						"preoptimized_link": "PreoptimizedRule-envfreeFuncsStaticCheck-ballPositionLPRP.html",
						"presimplified_link": "PresimplifiedRule-envfreeFuncsStaticCheck-ballPositionLPRP.html",
						"prelastopt_link": "PrelastoptRule-envfreeFuncsStaticCheck-ballPositionLPRP.html",
						"presolver_link": "PresolverRule-envfreeFuncsStaticCheck-ballPositionLPRP.html"
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
						"funcName": "pass()",
						"result": "SUCCESS",
						"time": "0",
						"graph_link": "",
						"preoptimized_link": "PreoptimizedRule-envfreeFuncsStaticCheck-passLPRP.html",
						"presimplified_link": "PresimplifiedRule-envfreeFuncsStaticCheck-passLPRP.html",
						"prelastopt_link": "PrelastoptRule-envfreeFuncsStaticCheck-passLPRP.html",
						"presolver_link": "PresolverRule-envfreeFuncsStaticCheck-passLPRP.html"
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
					"ruleName": "playerTwoNeverWins_preserve",
					"tableBody":[
						{
							 "tableRow": {
								"funcName": "pass()",
								"result": "FAIL",
								"time": "0",
								"graph_link": "Report-playerTwoNeverWins_preserve-passLPRP-example1.html",
								"preoptimized_link": "PreoptimizedRule-playerTwoNeverWins_preserve-passLPRP.html",
								"presimplified_link": "PresimplifiedRule-playerTwoNeverWins_preserve-passLPRP.html",
								"prelastopt_link": "PrelastoptRule-playerTwoNeverWins_preserve-passLPRP.html",
								"presolver_link": "PresolverRule-playerTwoNeverWins_preserve-passLPRP.html"
							},
							 "variables": {
								"certoraInvF.selector": "0xa7a1ed72",
								"certoraInvF.isPure": "false",
								"certoraInvF.isView": "false",
								"certoraInvF.isPayable": "false",
								"certoraInvF.numberOfArguments": "0",
								"certoraInvF.isFallback": "false",
								"invariantEnv.msg.sender": "BallGame (0x2712)",
								"invariantEnv.msg.value": "0",
								"invariantEnv.tx.origin": "0x401",
								"invariantEnv.block.coinbase": "0x402",
								"invariantEnv.block.difficulty": "8",
								"invariantEnv.block.gaslimit": "7",
								"invariantEnv.block.number": "6",
								"invariantEnv.block.timestamp": "3",
								"lastHasThrown": "false",
								"lastReverted": "false",
								"BallGame": "BallGame (0x2712)",
								"ecrecover": "ecrecover (0x2711)",
								"sha256": "sha256 (0x4538)",
								"identity": "identity (0x2be5)"
							},
							"assertMessage":[
								"invariant violated in post-state"
							],
							 "failureCauses": {
								"expr": "0x2==0x2"
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
							},
							 "callTrace": {
								"funcName": "playerTwoNeverWins_preserve(certoraInvF=pass(), invariantCalldata=unknown type, invariantEnv=*struct* invariantEnv)",
								"returnValue": "",
								"status": "",
								"childrenList":[
									{
										"funcName": "Storage State",
										"returnValue": "",
										"status": "",
										"childrenList":[
											{
												"funcName": "BallGame",
												"returnValue": "",
												"status": "",
												"childrenList":[
													{
														"funcName": "ballPosition: 0",
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
										"funcName": "assume invariant in pre-state",
										"returnValue": "",
										"status": "",
										"childrenList":[
											{
												"funcName": "BallGame.ballPosition()",
												"returnValue": "0",
												"status": "SUCCESS",
												"childrenList":[
													{
														"funcName": "Load from BallGame.ballPosition: 0",
														"returnValue": "",
														"status": "",
														"childrenList":[]

													}
												]
											},
											{
												"funcName": "BallGame.ballPosition() != 2",
												"returnValue": "true",
												"status": "",
												"childrenList":[
													{
														"funcName": "BallGame.ballPosition() == 2",
														"returnValue": "false",
														"status": "",
														"childrenList":[
															{
																"funcName": "BallGame.ballPosition()",
																"returnValue": "*",
																"status": "",
																"childrenList":[]

															},
															{
																"funcName": "2",
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
										"funcName": "check effects of step taken by one of the functions",
										"returnValue": "",
										"status": "",
										"childrenList":[
											{
												"funcName": "BallGame.pass()",
												"returnValue": "",
												"status": "SUCCESS",
												"childrenList":[
													{
														"funcName": "sender: BallGame (0x2712); receiver: BallGame (0x2712); transferred amount: 0",
														"returnValue": "",
														"status": "TRANSFER",
														"childrenList":[
															{
																"funcName": "Load from sender.balance: 0x985",
																"returnValue": "",
																"status": "",
																"childrenList":[]

															},
															{
																"funcName": "Store at sender.balance: 0x985",
																"returnValue": "",
																"status": "",
																"childrenList":[]

															},
															{
																"funcName": "Load from receiver.balance: 0x985",
																"returnValue": "",
																"status": "",
																"childrenList":[]

															},
															{
																"funcName": "Store at receiver.balance: 0x985",
																"returnValue": "",
																"status": "",
																"childrenList":[]

															}
														]
													},
													{
														"funcName": "Load from BallGame.ballPosition: 0",
														"returnValue": "",
														"status": "",
														"childrenList":[]

													},
													{
														"funcName": "Load from BallGame.ballPosition: 0",
														"returnValue": "",
														"status": "",
														"childrenList":[]

													},
													{
														"funcName": "Store at BallGame.ballPosition: 2",
														"returnValue": "",
														"status": "",
														"childrenList":[]

													}
												]
											}
										]
									},
									{
										"funcName": "assert invariant in post-state",
										"returnValue": "",
										"status": "",
										"childrenList":[
											{
												"funcName": "BallGame.ballPosition()",
												"returnValue": "2",
												"status": "SUCCESS",
												"childrenList":[
													{
														"funcName": "Load from BallGame.ballPosition: 2",
														"returnValue": "",
														"status": "",
														"childrenList":[]

													}
												]
											},
											{
												"funcName": "BallGame.ballPosition() != 2",
												"returnValue": "false",
												"status": "",
												"childrenList":[
													{
														"funcName": "BallGame.ballPosition() == 2",
														"returnValue": "true",
														"status": "",
														"childrenList":[
															{
																"funcName": "BallGame.ballPosition()",
																"returnValue": "*",
																"status": "",
																"childrenList":[]

															},
															{
																"funcName": "2",
																"returnValue": "",
																"status": "",
																"childrenList":[]

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
														"funcName": "BallGame",
														"returnValue": "",
														"status": "",
														"childrenList":[
															{
																"funcName": "ballPosition: 2 (changed)",
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
												"storageId": "2"
											}
										]
									}
								]
							}
						}
					]

				},
		{
			"ruleName": "playerTwoNeverWins",
			"tableBody":[
				{
					 "tableRow": {
						"funcName": "playerTwoNeverWins_skipped_preserve_ballPosition()",
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
						"funcName": "playerTwoNeverWins_preserve",
						"result": "FAIL",
						"time": "0",
						"graph_link": "",
						"preoptimized_link": "",
						"presimplified_link": "",
						"prelastopt_link": "",
						"presolver_link": ""
					},
					"isMultiAssert": true
				}
,				{
					 "tableRow": {
						"funcName": "playerTwoNeverWins_instate",
						"result": "SUCCESS",
						"time": "0",
						"graph_link": "",
						"preoptimized_link": "PreoptimizedRule-playerTwoNeverWins_instate.html",
						"presimplified_link": "PresimplifiedRule-playerTwoNeverWins_instate.html",
						"prelastopt_link": "PrelastoptRule-playerTwoNeverWins_instate.html",
						"presolver_link": "PresolverRule-playerTwoNeverWins_instate.html"
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
						"name": "BallGame",
						"address": "ce4604a0000000000000000000000001",
						"pre_state": "{}",
						"methodsNames":[
							"constructor()",
							"ballPosition()",
							"pass()"
						]
					}
				}
			]
		}
	}