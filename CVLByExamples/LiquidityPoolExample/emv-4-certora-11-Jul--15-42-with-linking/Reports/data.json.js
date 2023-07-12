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
						"ruleName": "integrityOfDeposit",
						"result": "SUCCESS",
						"time": "2",
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
						"address": "ce4604a0000000000000000000000003",
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
						"address": "ce4604a000000000000000000000000d",
						"pre_state": "{4=274184521717934524641157099916833587203}",
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
				}
			]
		}
	}