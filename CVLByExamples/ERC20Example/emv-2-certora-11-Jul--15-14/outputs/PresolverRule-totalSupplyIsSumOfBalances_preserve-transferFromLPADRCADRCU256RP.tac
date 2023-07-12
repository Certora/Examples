TACSymbolTable {
	UserDefined {
		UninterpSort skey
	}
	BuiltinFunctions {
		to_skey:JSON{"#class":"vc.data.TACBuiltInFunction.Hash.ToSkey"}
		add_noofl:JSON{"#class":"vc.data.TACBuiltInFunction.NoAddOverflowCheck"}
		safe_math_narrow:JSON{"#class":"vc.data.TACBuiltInFunction.SafeMathNarrow"}
		hash_3_keccak:JSON{"#class":"vc.data.TACBuiltInFunction.Hash.SimpleHashApplication","arity":3,"hashFamily":{"#class":"vc.data.HashFamily.Keccack"}}
		skey_basic:JSON{"#class":"vc.data.TACBuiltInFunction.Hash.Basic"}
		safe_math_promotion:JSON{"#class":"vc.data.TACBuiltInFunction.SafeMathPromotion"}
	}
	UninterpretedFunctions {
		CANON27:JSON{"name":"CANON27","paramSorts":[],"returnSort":{"#class":"tac.Tag.Int"},"attribute":"Ghost","cvlResultType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Mathint"},"cvlParamTypes":[],"declarationName":"CANON27"}
		I168:JSON{"name":"I168","paramSorts":[],"returnSort":{"#class":"tac.Tag.Int"},"attribute":"Ghost","cvlResultType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Mathint"},"cvlParamTypes":[],"declarationName":"CANON27"}
		I183:JSON{"name":"I183","paramSorts":[],"returnSort":{"#class":"tac.Tag.Int"},"attribute":"Ghost","cvlResultType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Mathint"},"cvlParamTypes":[],"declarationName":"CANON27"}
		I4:JSON{"name":"I4","paramSorts":[],"returnSort":{"#class":"tac.Tag.Int"},"attribute":"Ghost","cvlResultType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Mathint"},"cvlParamTypes":[],"declarationName":"CANON27"}
	}
	tacM0x20@2:bv256
	tacCaller@2:bv256
	tacCalldatabufCANON0@2:bv256
	tacCalldatabufCANON1@2:bv256
	tacCalldatabufCANON2@2:bv256
	tacMCANON0!!1:bytemap
	tacAddress!!27:bv256
	tacAddress!!42:bv256
	tacAddress!!79:bv256
	tacCallvalue@2:bv256
	lastReverted:bool
	lastReverted@1:bool
	lastReverted@2:bool
	lastReverted@3:bool
	tacM0x0!!129:bv256
	tacM0x0!!132:bv256
	tacM0x0!!143:bv256
	tacM0x0!!146:bv256
	tacM0x0!!154:bv256
	tacM0x0!!160:bv256
	tacM0x0!!170:bv256
	CANON24!!3:bv256
	tacExtcodesize!!0:wordmap
	CANON74!!5:wordmap
	CANON83!!6:wordmap
	tacCalldatasize@1:bv256
	tacCalldatasize@2:bv256
	tacCalldatasize@3:bv256
	tacCallvalue!!77:bv256
	tacM0x0@2:bv256
	CANON83!!163:wordmap
	tacExtcodesize:wordmap
	CANON100:bool
	CANON101:bool
	CANON102:int
	CANON103:int
	CANON104:bool
	tacSighash!!8:bv256
	tacSighash!!9:bv256
	tacCalldatasize!!24:bv256
	tacCalldatasize!!39:bv256
	tacCalldatasize!!63:bv256
	tacMCANON0@2:bytemap
	tacMCANON1@2:bytemap
	tacBalance:wordmap
	tacNumber@2:bv256
	tacBalance!!2:wordmap
	I4:int
	R7:bv256
	B11:bool
	B12:bool
	B13:bool
	B14:bool
	B15:bool
	B16:bool
	B17:bool
	B18:bool
	B19:bool
	B20:bool
	B21:bool
	B23:bool
	B25:bool
	B26:bool
	B29:bool
	B30:bool
	B31:bool
	B32:bool
	B33:bool
	B34:bool
	B35:bool
	B40:bool
	B41:bool
	B44:bool
	B45:bool
	B46:bool
	B47:bool
	B48:bool
	B49:bool
	B50:bool
	B64:bool
	B65:bool
	B70:bool
	B73:bool
	B75:bool
	B78:bool
	B81:bool
	B84:bool
	B86:bool
	B89:bool
	B91:bool
	B94:bool
	B96:bool
	B99:bool
	I38:int
	I53:int
	I54:int
	I56:int
	I57:int
	I58:int
	I59:int
	I60:int
	I69:int
	I74:int
	I80:int
	I85:int
	I90:int
	I95:int
	I98:int
	M61:bytemap
	R22:bv256
	R28:bv256
	R36:bv256
	R37:bv256
	R43:bv256
	R51:bv256
	R52:bv256
	R62:bv256
	R66:bv256
	R67:bv256
	R68:bv256
	R71:bv256
	R76:bv256
	R82:bv256
	R87:bv256
	R92:bv256
	R97:bv256
	B108:bool
	B112:bool
	B113:bool
	B114:bool
	B115:bool
	B116:bool
	B117:bool
	B118:bool
	B119:bool
	B120:bool
	B122:bool
	B124:bool
	B126:bool
	B136:bool
	B140:bool
	B141:bool
	B150:bool
	B152:bool
	B157:bool
	B173:bool
	I104:int
	I109:int
	I164:int
	I165:int
	I166:int
	I167:int
	I168:int
	I174:int
	I175:int
	I176:int
	I179:int
	I180:int
	I181:int
	I182:int
	I183:int
	R100:bv256
	R101:bv256
	R102:bv256
	R103:bv256
	R106:bv256
	R107:bv256
	R111:bv256
	R121:bv256
	R123:bv256
	R125:bv256
	R127:bv256
	R128:bv256
	R130:(uninterp) skey
	R131:bv256
	R134:(uninterp) skey
	R135:bv256
	R137:bv256
	R138:bv256
	R139:bv256
	R142:bv256
	R144:bv256
	R145:bv256
	R149:bv256
	R151:bv256
	R153:bv256
	R155:(uninterp) skey
	R156:bv256
	R158:bv256
	R159:bv256
	R161:(uninterp) skey
	R162:bv256
	R169:bv256
	R171:(uninterp) skey
	R172:bv256
	R177:bv256
	R178:bv256
	R184:bv256
	tacAddress@1:bv256
	tacAddress@2:bv256
	tacAddress@3:bv256
	LCANON0@1:bool
	LCANON0@2:bool
	LCANON0@3:bool
	LCANON1@1:bool
	LCANON1@2:bool
	LCANON1@3:bool
	LCANON2@1:bool
	LCANON2@2:bool
	LCANON2@3:bool
	LCANON3@1:bool
	LCANON3@2:bool
	LCANON3@3:bool
	LCANON4@1:bool
	LCANON4@2:bool
	LCANON4@3:bool
	LCANON5@1:bool
	LCANON5@2:bool
	LCANON5@3:bool
	LCANON6@1:bv256
	LCANON6@3:bv256
	LCANON7@1:bv256
	LCANON7@3:bv256
	LCANON8@1:bv256
	LCANON8@3:bv256
	LCANON9@2:bool
	tacMCANON0!!148:bytemap
	tacOrigin@2:bv256
	CANON10:int
	CANON11:int
	CANON12:int
	CANON13:int
	CANON14:int
	CANON15:bool
	CANON16:bool
	CANON17:bool
	CANON18:bv256
	CANON19:bool
	CANON20:bool
	CANON21:bool
	CANON22@1:bv256
	CANON22@2:bv256
	CANON22@3:bv256
	CANON23@1:bool
	CANON23@2:bool
	CANON23@3:bool
	CANON24:bv256
	CANON25:int
	CANON26:int
	CANON27:int
	CANON28:bool
	CANON30:int
	CANON31:int
	CANON32:int
	CANON33:int
	CANON34:int
	CANON35:bytemap
	CANON36:bytemap
	CANON37:bv256
	CANON38:bv256
	CANON39:bool
	CANON40:bool
	CANON41:bv256
	CANON42:bv256
	CANON43:bv256
	CANON44:int
	CANON45:bool
	CANON46:bv256
	CANON47:int
	CANON48:bool
	CANON49:bv256
	CANON50:int
	CANON51:bool
	CANON52:bv256
	CANON53:int
	CANON54:bool
	CANON55:bv256
	CANON56:int
	CANON57:bool
	CANON58:bv256
	CANON59:int
	CANON60:bool
	CANON61:bv256
	CANON62:int
	CANON63:bool
	CANON64:bv256
	CANON65:bv256
	CANON66:bv256
	CANON67:bv256
	CANON68:int
	CANON69:bv256
	CANON70:bv256
	CANON71:bool
	CANON72:bool
	CANON73:bool
	CANON74:wordmap
	CANON83:wordmap
	CANON86:bv256
	CANON89:int
	CANON90:int
	CANON91:int
	CANON92:int
	CANON95:bool
	CANON96:int
	CANON97:int
	CANON98:int
	CANON99:bv256
	LCANON10@2:bv256
	LCANON11@2:bool
	LCANON12@2:bv256
	LCANON13@2:bool
	LCANON14@2:bv256
	LCANON15@2:bv256
	LCANON16@2:bool
	LCANON17@2:bv256
	LCANON18@2:bv256
	LCANON19@2:bool
	LCANON20@2:bv256
	LCANON21@2:bv256
	LCANON22@2:bv256
	LCANON23@2:bv256
	LCANON24@2:bv256
	LCANON25@2:bv256
	LCANON26@2:bv256
	LCANON27@2:bv256
	LCANON28@2:bool
	LCANON29@2:bv256
	LCANON30@2:bv256
	LCANON31@2:bv256
	LCANON32@2:bool
	LCANON33@2:bool
	LCANON34@2:bv256
	LCANON35@2:bv256
	LCANON36@2:bv256
	LCANON37@2:bv256
	LCANON38@2:bv256
	LCANON39@2:bv256
	LCANON40@2:bv256
	LCANON41@2:bv256
	LCANON42@2:bv256
	LCANON43@2:bv256
	LCANON44@2:bv256
	LCANON45@2:bool
	LCANON46@2:bv256
	LCANON47@2:bool
	LCANON48@2:bv256
	LCANON49@2:bv256
	LCANON50@2:bv256
	LCANON51@2:bv256
	LCANON52@2:bool
	LCANON53@2:bv256
	LCANON54@2:bv256
	LCANON55@2:bv256
	LCANON56@2:bv256
	LCANON57@2:bv256
	LCANON58@2:bv256
	LCANON59@2:bv256
	LCANON60@2:bv256
	LCANON61@2:bv256
	LCANON62@2:bool
	LCANON63@2:bv256
	LCANON64@2:bv256
	LCANON65@2:bv256
	LCANON66@2:bv256
	LCANON67@2:bv256
	LCANON68@2:bv256
	LCANON69@2:bv256
	tacContractAtCANON0:bv256
	lastHasThrown:bool
	lastHasThrown@1:bool
	lastHasThrown@2:bool
	lastHasThrown@3:bool
	tacM0x20!!133:bv256
	tacM0x20!!147:bv256
	CANON104!!110:bool
	tacCaller!!72:bv256
	tacNumber!!88:bv256
	tacTimestamp!!93:bv256
	CANON0:int
	CANON1:bool
	CANON2:bool
	CANON3:bool
	CANON4:int
	CANON5:bool
	CANON6:bool
	CANON7:int
	CANON8:int
	CANON9:int
	tacBalance!!105:wordmap
	CANON28!!55:bool
	tacTimestamp@2:bv256
	tacSighash!!10:bv256
	tacSighash@1:bv256
	tacSighash@2:bv256
	tacSighash@3:bv256
	tacOrigin!!83:bv256
}
Program {
	Block 0_0_0_0_0_0 Succ [0_0_0_1_0_0] {
		AssignHavocCmd tacExtcodesize!!0:0
		AssignHavocCmd tacBalance!!2:1
		AssignHavocCmd CANON24!!3:2
		AssignHavocCmd I4
		AssignHavocCmd CANON36:3
		AssignHavocCmd CANON38:4
		AssignHavocCmd CANON74!!5:5
		AssignHavocCmd CANON83!!6:6
		AssignHavocCmd R7:7
		AssignHavocCmd tacSighash!!8:8
		AssignHavocCmd tacSighash!!9:8
		AssignHavocCmd tacSighash!!10:8
		AssignExpCmd CANON0:9 0x23b872dd
		AssignExpCmd CANON1:10 false
		AssignExpCmd CANON2:11 false
		AssignExpCmd CANON3:12 false
		AssignExpCmd CANON4:13 0x3
		AssignExpCmd CANON5:14 false
		AnnotationCmd JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Message","s":"Setup"}}
		AnnotationCmd JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Message","s":"multi contract setup"}}
		AnnotationCmd JSON{"key":{"name":"cvl.label.end","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		AnnotationCmd JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Message","s":"rule parameters setup"}}
		AssumeCmd true
		AssumeCmd true
		AssignHavocCmd CANON7:15
		AssignHavocCmd CANON8:16
		AssignHavocCmd CANON9:17
		AssignHavocCmd CANON10:18
		AssignHavocCmd CANON11:19
		AssignHavocCmd CANON12:20
		AssignHavocCmd CANON13:21
		AssignHavocCmd CANON14:22
		NopCmd
		AssumeExpCmd LAnd(Le(CANON7:15 0xffffffffffffffffffffffffffffffffffffffff ) Ge(CANON7:15 0x0 ) )
		NopCmd
		AssumeExpCmd LAnd(Le(CANON8:16 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff ) Ge(CANON8:16 0x0 ) )
		NopCmd
		AssumeExpCmd LAnd(Le(CANON9:17 0xffffffffffffffffffffffffffffffffffffffff ) Ge(CANON9:17 0x0 ) )
		NopCmd
		AssumeExpCmd LAnd(Le(CANON10:18 0xffffffffffffffffffffffffffffffffffffffff ) Ge(CANON10:18 0x0 ) )
		NopCmd
		AssumeExpCmd LAnd(Le(CANON11:19 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff ) Ge(CANON11:19 0x0 ) )
		NopCmd
		AssumeExpCmd LAnd(Le(CANON12:20 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff ) Ge(CANON12:20 0x0 ) )
		NopCmd
		AssumeExpCmd LAnd(Le(CANON13:21 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff ) Ge(CANON13:21 0x0 ) )
		NopCmd
		AssumeExpCmd LAnd(Le(CANON14:22 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff ) Ge(CANON14:22 0x0 ) )
		AnnotationCmd JSON{"key":{"name":"cvl.label.end","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		AnnotationCmd JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Message","s":"contract address vars initialized"}}
		AnnotationCmd JSON{"key":{"name":"cvl.label.end","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		AnnotationCmd JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Message","s":"setup read tracking instrumentation"}}
		AnnotationCmd JSON{"key":{"name":"cvl.label.end","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		AnnotationCmd JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Message","s":"last storage initialize"}}
		AnnotationCmd JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageGlobalChangeSnippet.StorageTakeSnapshot","lhs":{"namePrefix":"lastStorage","tag":{"#class":"tac.Tag.BlockchainState"},"callIndex":0,"meta":[{"key":{"name":"cvl.local","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true},{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"lastStorage"},{"key":{"name":"cvl.type","type":"spec.cvlast.CVLType$PureCVLType","erasureStrategy":"CallTrace"},"value":{"#class":"spec.cvlast.CVLType.PureCVLType.VMInternal.BlockchainState"}},{"key":{"name":"cvl","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true},{"key":{"name":"cvl.display","type":"java.lang.String","erasureStrategy":"CallTrace"},"value":"lastStorage"}]}}}
		AnnotationCmd JSON{"key":{"name":"cvl.label.end","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		AnnotationCmd JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Message","s":"assumptions about extcodesize"}}
		AssignExpCmd B19:23 Gt(Select(tacExtcodesize!!0:0 Apply(to_skey:bif R7:7) ) 0x0 )
		AssumeCmd B19:23
		AnnotationCmd JSON{"key":{"name":"cvl.label.end","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		AnnotationCmd JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Message","s":"assumptions about contracts' addresses"}}
		NopCmd
		AssumeExpCmd Gt(R7:7 0x0 )
		NopCmd
		AssumeExpCmd Le(R7:7 0xffffffffffffffffffffffffffffffffffffffff )
		AnnotationCmd JSON{"key":{"name":"cvl.label.end","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		AnnotationCmd JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Message","s":"assumptions about starting balances"}}
		AssignExpCmd R22:23 Select(tacBalance!!2:1 Apply(to_skey:bif R7:7) )
		NopCmd
		AssumeExpCmd Ge(R22:23 0x0 )
		AnnotationCmd JSON{"key":{"name":"cvl.label.end","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		AnnotationCmd JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Message","s":"assumptions about static addresses"}}
		AnnotationCmd JSON{"key":{"name":"cvl.label.end","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		AnnotationCmd JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Message","s":"assumptions about uniqueness of contracts' addressses"}}
		AnnotationCmd JSON{"key":{"name":"cvl.label.end","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		AnnotationCmd JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Message","s":"record starting nonces"}}
		AnnotationCmd JSON{"key":{"name":"cvl.label.end","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		AnnotationCmd JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Message","s":"cloned contracts have no balances"}}
		AnnotationCmd JSON{"key":{"name":"cvl.label.end","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		AnnotationCmd JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Message","s":"Linked immutable setup"}}
		AnnotationCmd JSON{"key":{"name":"cvl.label.end","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		AnnotationCmd JSON{"key":{"name":"cvl.label.end","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		AnnotationCmd:24 JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Message","s":"assume invariant in pre-state"}}
	}
	Block 0_0_0_1_0_0 Succ [1_0_0_0_0_0] {
		AnnotationCmd:24 JSON{"key":{"name":"call.trace.push","type":"analysis.icfg.Inliner$CallStack$PushRecord","erasureStrategy":"Canonical"},"value":"rO0ABXNyACphbmFseXNpcy5pY2ZnLklubGluZXIkQ2FsbFN0YWNrJFB1c2hSZWNvcmSX8+DCTLCH+AIAA0kACGNhbGxlZUlkTAAGY2FsbGVldAATTHZjL2RhdGEvTWV0aG9kUmVmO0wAB3N1bW1hcnl0ABVMdmMvZGF0YS9DYWxsU3VtbWFyeTt4cAAAAAFzcgARdmMuZGF0YS5NZXRob2RSZWbJlJTzzU9pGAIAA0wABGF0dHJ0ABdMc2NlbmUvTWV0aG9kQXR0cmlidXRlO0wACmNvbnRyYWN0SWR0ABZMamF2YS9tYXRoL0JpZ0ludGVnZXI7TAAHc2lnSGFzaHQAEExldm0vU2lnaGFzaEludDt4cHNyABxzY2VuZS5NZXRob2RBdHRyaWJ1dGUkQ29tbW9uNHjdebdr9XMCAAB4cgAVc2NlbmUuTWV0aG9kQXR0cmlidXRlcYg2pYWutuUCAAB4cHNyABRqYXZhLm1hdGguQmlnSW50ZWdlcoz8nx+pO/sdAwAGSQAIYml0Q291bnRJAAliaXRMZW5ndGhJABNmaXJzdE5vbnplcm9CeXRlTnVtSQAMbG93ZXN0U2V0Qml0SQAGc2lnbnVtWwAJbWFnbml0dWRldAACW0J4cgAQamF2YS5sYW5nLk51bWJlcoaslR0LlOCLAgAAeHD///////////////7////+AAAAAXVyAAJbQqzzF/gGCFTgAgAAeHAAAAAQzkYEoAAAAAAAAAAAAAAAA3hzcgAOZXZtLlNpZ2hhc2hJbnRUdcqNMXEgeAIAAUwAAW5xAH4ABnhwc3EAfgAM///////////////+/////gAAAAF1cQB+ABAAAAAEGBYN3Xhw"}
		AssignHavocCmd:24 tacCalldatasize!!24:25
		NopCmd
		AssumeExpCmd Apply(add_noofl:bif 0x4 0x0)
		NopCmd
		AssumeExpCmd Eq(0x4 tacCalldatasize!!24:25 )
		LabelCmd:24 "Start procedure ERC20-totalSupply()"
		AnnotationCmd:24 JSON{"key":{"name":"fps.free-pointer-is-scalarized","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true}
		AssignExpCmd:24 R28:23 Select(tacExtcodesize!!0:0 Apply(to_skey:bif R7:26) )
		NopCmd
		AssumeExpCmd Gt(R28:23 0x0 )
		AnnotationCmd:24 JSON{"key":{"name":"internal.func.finder.info","type":"analysis.ip.InternalFunctionFinderReport","erasureStrategy":"Erased"},"value":"rO0ABXNyAChhbmFseXNpcy5pcC5JbnRlcm5hbEZ1bmN0aW9uRmluZGVyUmVwb3J0ian+bYn1VdACAAFMABN1bnJlc29sdmVkRnVuY3Rpb25zdAAPTGphdmEvdXRpbC9TZXQ7eHBzcgAhZGF0YXN0cnVjdHVyZXMuTGlua2VkQXJyYXlIYXNoU2V0AAAAAAAAAAEDAAJGAApsb2FkRmFjdG9yTAAJaGFzaFRhYmxldAAuTGRhdGFzdHJ1Y3R1cmVzL2FycmF5aGFzaHRhYmxlL0FycmF5SGFzaFRhYmxlO3hwdwgAAAAAQAAAAHg="}
		AnnotationCmd:24 JSON{"key":{"name":"fps.free-pointer-is-scalarized","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true}
		NopCmd
		AssumeExpCmd LNot(Lt(tacCalldatasize!!24:25 0x4 ) )
		NopCmd
		AssumeExpCmd Gt(0x70a08231 tacSighash!!8:8 )
		NopCmd
		AssumeExpCmd Gt(0x2e1a7d4d tacSighash!!8:8 )
		NopCmd
		AssumeExpCmd LNot(Eq(0x6fdde03 tacSighash!!8:8 ) )
		NopCmd
		AssumeExpCmd LNot(Eq(0x95ea7b3 tacSighash!!8:8 ) )
		NopCmd
		AssumeExpCmd Eq(0x18160ddd tacSighash!!8:8 )
		AssumeCmd:27 true
		AnnotationCmd:24 JSON{"key":{"name":"internal.func.start","type":"analysis.ip.InternalFuncStartAnnotation","erasureStrategy":"CallTrace"},"value":{"id":0,"startPc":1328,"args":[],"methodSignature":{"#class":"spec.cvlast.QualifiedMethodSignature.QualifiedMethodSig","qualifiedMethodName":{"#class":"spec.cvlast.QualifiedFunction","host":{"name":"ERC20"},"methodId":"totalSupply"},"params":[],"res":[{"#class":"spec.cvlast.VMParam.Unnamed","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256}}]},"stackOffsetToArgPos":{},"callSiteSrc":{"source":0,"begin":3906,"len":364,"jumpType":"ENTER","address":"ce4604a0000000000000000000000003","sourceContext":{"indexToFilepath":{"0":"contracts/ERC20.sol","1":"contracts/IERC20.sol","2":"contracts/IERC20Metadata.sol"},"sourceDir":".post_autofinders.0"}}}}
		AnnotationCmd:24 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet","value":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"CANON24!!3","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.scalarization.sort","type":"vc.data.ScalarizationSort","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.ScalarizationSort.Split","idx":"2"}},{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.storage.bit-width","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":256},{"key":{"name":"tac.storage.pretty.paths","type":"analysis.storage.DisplayPaths","erasureStrategy":"Erased"},"value":{"paths":[{"#class":"analysis.storage.DisplayPath.Root","name":"_totalSupply"}]}},{"key":{"name":"tac.slot.type","type":"spec.cvlast.typedescriptors.EVMTypeDescriptor$EVMValueType","erasureStrategy":"Canonical"},"value":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256}},{"key":{"name":"tac.storage.non-indexed-path","type":"analysis.storage.StorageAnalysisResult$NonIndexedPath","erasureStrategy":"Canonical"},"value":{"#class":"analysis.storage.StorageAnalysisResult.NonIndexedPath.Root","slot":"2"}},{"key":{"name":"tac.storage","type":"java.math.BigInteger","erasureStrategy":"Canonical"},"value":"ce4604a0000000000000000000000003"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1021}]},"displayPath":{"#class":"analysis.storage.DisplayPath.Root","name":"_totalSupply"},"storageType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256},"contractInstance":"ce4604a0000000000000000000000003","linkableStorageReadId":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet.Id","id":0}}}
		AnnotationCmd:24 JSON{"key":{"name":"internal.func.end","type":"analysis.ip.InternalFuncExitAnnotation","erasureStrategy":"Canonical"},"value":{"id":0,"rets":[{"s":{"namePrefix":"CANON24!!3","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.scalarization.sort","type":"vc.data.ScalarizationSort","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.ScalarizationSort.Split","idx":"2"}},{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.storage.bit-width","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":256},{"key":{"name":"tac.storage.pretty.paths","type":"analysis.storage.DisplayPaths","erasureStrategy":"Erased"},"value":{"paths":[{"#class":"analysis.storage.DisplayPath.Root","name":"_totalSupply"}]}},{"key":{"name":"tac.slot.type","type":"spec.cvlast.typedescriptors.EVMTypeDescriptor$EVMValueType","erasureStrategy":"Canonical"},"value":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256}},{"key":{"name":"tac.storage.non-indexed-path","type":"analysis.storage.StorageAnalysisResult$NonIndexedPath","erasureStrategy":"Canonical"},"value":{"#class":"analysis.storage.StorageAnalysisResult.NonIndexedPath.Root","slot":"2"}},{"key":{"name":"tac.storage","type":"java.math.BigInteger","erasureStrategy":"Canonical"},"value":"ce4604a0000000000000000000000003"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1023}]},"offset":0}],"functionLayout":{"0":{"#class":"analysis.ip.InternalFuncValueLocation.Scalar"}}}}
		AnnotationCmd:24 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.EVMFunctionReturnWrite","returnbufOffset":"0","returnValueSym":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"CANON24!!3","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.scalarization.sort","type":"vc.data.ScalarizationSort","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.ScalarizationSort.Split","idx":"2"}},{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.storage.bit-width","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":256},{"key":{"name":"tac.storage.pretty.paths","type":"analysis.storage.DisplayPaths","erasureStrategy":"Erased"},"value":{"paths":[{"#class":"analysis.storage.DisplayPath.Root","name":"_totalSupply"}]}},{"key":{"name":"tac.slot.type","type":"spec.cvlast.typedescriptors.EVMTypeDescriptor$EVMValueType","erasureStrategy":"Canonical"},"value":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256}},{"key":{"name":"tac.storage.non-indexed-path","type":"analysis.storage.StorageAnalysisResult$NonIndexedPath","erasureStrategy":"Canonical"},"value":{"#class":"analysis.storage.StorageAnalysisResult.NonIndexedPath.Root","slot":"2"}},{"key":{"name":"tac.storage","type":"java.math.BigInteger","erasureStrategy":"Canonical"},"value":"ce4604a0000000000000000000000003"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1023}]},"callIndex":1}}
		AnnotationCmd:24 JSON{"key":{"name":"tac.return.path","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		LabelCmd:24 "End procedure ERC20-totalSupply()"
		NopCmd
		AnnotationCmd:24 JSON{"key":{"name":"call.trace.pop","type":"analysis.icfg.Inliner$CallStack$PopRecord","erasureStrategy":"Canonical"},"value":"rO0ABXNyAClhbmFseXNpcy5pY2ZnLklubGluZXIkQ2FsbFN0YWNrJFBvcFJlY29yZPAPfwSLdCWJAgABSQAIY2FsbGVlSWR4cAAAAAE="}
	}
	Block 0_0_0_3_0_0 Succ [3_0_0_0_0_0] {
		AnnotationCmd:24 JSON{"key":{"name":"call.trace.push","type":"analysis.icfg.Inliner$CallStack$PushRecord","erasureStrategy":"Canonical"},"value":"rO0ABXNyACphbmFseXNpcy5pY2ZnLklubGluZXIkQ2FsbFN0YWNrJFB1c2hSZWNvcmSX8+DCTLCH+AIAA0kACGNhbGxlZUlkTAAGY2FsbGVldAATTHZjL2RhdGEvTWV0aG9kUmVmO0wAB3N1bW1hcnl0ABVMdmMvZGF0YS9DYWxsU3VtbWFyeTt4cAAAAANzcgARdmMuZGF0YS5NZXRob2RSZWbJlJTzzU9pGAIAA0wABGF0dHJ0ABdMc2NlbmUvTWV0aG9kQXR0cmlidXRlO0wACmNvbnRyYWN0SWR0ABZMamF2YS9tYXRoL0JpZ0ludGVnZXI7TAAHc2lnSGFzaHQAEExldm0vU2lnaGFzaEludDt4cHNyABxzY2VuZS5NZXRob2RBdHRyaWJ1dGUkQ29tbW9uNHjdebdr9XMCAAB4cgAVc2NlbmUuTWV0aG9kQXR0cmlidXRlcYg2pYWutuUCAAB4cHNyABRqYXZhLm1hdGguQmlnSW50ZWdlcoz8nx+pO/sdAwAGSQAIYml0Q291bnRJAAliaXRMZW5ndGhJABNmaXJzdE5vbnplcm9CeXRlTnVtSQAMbG93ZXN0U2V0Qml0SQAGc2lnbnVtWwAJbWFnbml0dWRldAACW0J4cgAQamF2YS5sYW5nLk51bWJlcoaslR0LlOCLAgAAeHD///////////////7////+AAAAAXVyAAJbQqzzF/gGCFTgAgAAeHAAAAAQzkYEoAAAAAAAAAAAAAAAA3hzcgAOZXZtLlNpZ2hhc2hJbnRUdcqNMXEgeAIAAUwAAW5xAH4ABnhwc3EAfgAM///////////////+/////gAAAAF1cQB+ABAAAAAEGBYN3Xhw"}
		AssignHavocCmd:24 tacCalldatasize!!39:25
		NopCmd
		AssumeExpCmd Apply(add_noofl:bif 0x4 0x0)
		NopCmd
		AssumeExpCmd Eq(0x4 tacCalldatasize!!39:25 )
		LabelCmd:24 "Start procedure ERC20-totalSupply()"
		AnnotationCmd:24 JSON{"key":{"name":"fps.free-pointer-is-scalarized","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true}
		AssignExpCmd:24 R43:23 Select(tacExtcodesize!!0:0 Apply(to_skey:bif R7:26) )
		NopCmd
		AssumeExpCmd Gt(R43:23 0x0 )
		AnnotationCmd:24 JSON{"key":{"name":"internal.func.finder.info","type":"analysis.ip.InternalFunctionFinderReport","erasureStrategy":"Erased"},"value":"rO0ABXNyAChhbmFseXNpcy5pcC5JbnRlcm5hbEZ1bmN0aW9uRmluZGVyUmVwb3J0ian+bYn1VdACAAFMABN1bnJlc29sdmVkRnVuY3Rpb25zdAAPTGphdmEvdXRpbC9TZXQ7eHBzcgAhZGF0YXN0cnVjdHVyZXMuTGlua2VkQXJyYXlIYXNoU2V0AAAAAAAAAAEDAAJGAApsb2FkRmFjdG9yTAAJaGFzaFRhYmxldAAuTGRhdGFzdHJ1Y3R1cmVzL2FycmF5aGFzaHRhYmxlL0FycmF5SGFzaFRhYmxlO3hwdwgAAAAAQAAAAHg="}
		AnnotationCmd:24 JSON{"key":{"name":"fps.free-pointer-is-scalarized","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true}
		NopCmd
		AssumeExpCmd LNot(Lt(tacCalldatasize!!39:25 0x4 ) )
		NopCmd
		AssumeExpCmd Gt(0x70a08231 tacSighash!!10:8 )
		NopCmd
		AssumeExpCmd Gt(0x2e1a7d4d tacSighash!!10:8 )
		NopCmd
		AssumeExpCmd LNot(Eq(0x6fdde03 tacSighash!!10:8 ) )
		NopCmd
		AssumeExpCmd LNot(Eq(0x95ea7b3 tacSighash!!10:8 ) )
		NopCmd
		AssumeExpCmd Eq(0x18160ddd tacSighash!!10:8 )
		AssumeCmd:27 true
		AnnotationCmd:24 JSON{"key":{"name":"internal.func.start","type":"analysis.ip.InternalFuncStartAnnotation","erasureStrategy":"CallTrace"},"value":{"id":6,"startPc":1328,"args":[],"methodSignature":{"#class":"spec.cvlast.QualifiedMethodSignature.QualifiedMethodSig","qualifiedMethodName":{"#class":"spec.cvlast.QualifiedFunction","host":{"name":"ERC20"},"methodId":"totalSupply"},"params":[],"res":[{"#class":"spec.cvlast.VMParam.Unnamed","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256}}]},"stackOffsetToArgPos":{},"callSiteSrc":{"source":0,"begin":3906,"len":364,"jumpType":"ENTER","address":"ce4604a0000000000000000000000003","sourceContext":{"indexToFilepath":{"0":"contracts/ERC20.sol","1":"contracts/IERC20.sol","2":"contracts/IERC20Metadata.sol"},"sourceDir":".post_autofinders.0"}}}}
		AnnotationCmd:24 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet","value":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"CANON24!!3","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.scalarization.sort","type":"vc.data.ScalarizationSort","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.ScalarizationSort.Split","idx":"2"}},{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.storage.bit-width","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":256},{"key":{"name":"tac.storage.pretty.paths","type":"analysis.storage.DisplayPaths","erasureStrategy":"Erased"},"value":{"paths":[{"#class":"analysis.storage.DisplayPath.Root","name":"_totalSupply"}]}},{"key":{"name":"tac.slot.type","type":"spec.cvlast.typedescriptors.EVMTypeDescriptor$EVMValueType","erasureStrategy":"Canonical"},"value":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256}},{"key":{"name":"tac.storage.non-indexed-path","type":"analysis.storage.StorageAnalysisResult$NonIndexedPath","erasureStrategy":"Canonical"},"value":{"#class":"analysis.storage.StorageAnalysisResult.NonIndexedPath.Root","slot":"2"}},{"key":{"name":"tac.storage","type":"java.math.BigInteger","erasureStrategy":"Canonical"},"value":"ce4604a0000000000000000000000003"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1021}]},"displayPath":{"#class":"analysis.storage.DisplayPath.Root","name":"_totalSupply"},"storageType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256},"contractInstance":"ce4604a0000000000000000000000003","linkableStorageReadId":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet.Id","id":1}}}
		AnnotationCmd:24 JSON{"key":{"name":"internal.func.end","type":"analysis.ip.InternalFuncExitAnnotation","erasureStrategy":"Canonical"},"value":{"id":6,"rets":[{"s":{"namePrefix":"CANON24!!3","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.scalarization.sort","type":"vc.data.ScalarizationSort","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.ScalarizationSort.Split","idx":"2"}},{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.storage.bit-width","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":256},{"key":{"name":"tac.storage.pretty.paths","type":"analysis.storage.DisplayPaths","erasureStrategy":"Erased"},"value":{"paths":[{"#class":"analysis.storage.DisplayPath.Root","name":"_totalSupply"}]}},{"key":{"name":"tac.slot.type","type":"spec.cvlast.typedescriptors.EVMTypeDescriptor$EVMValueType","erasureStrategy":"Canonical"},"value":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256}},{"key":{"name":"tac.storage.non-indexed-path","type":"analysis.storage.StorageAnalysisResult$NonIndexedPath","erasureStrategy":"Canonical"},"value":{"#class":"analysis.storage.StorageAnalysisResult.NonIndexedPath.Root","slot":"2"}},{"key":{"name":"tac.storage","type":"java.math.BigInteger","erasureStrategy":"Canonical"},"value":"ce4604a0000000000000000000000003"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1023}]},"offset":0}],"functionLayout":{"0":{"#class":"analysis.ip.InternalFuncValueLocation.Scalar"}}}}
		AnnotationCmd:24 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.EVMFunctionReturnWrite","returnbufOffset":"0","returnValueSym":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"CANON24!!3","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.scalarization.sort","type":"vc.data.ScalarizationSort","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.ScalarizationSort.Split","idx":"2"}},{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.storage.bit-width","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":256},{"key":{"name":"tac.storage.pretty.paths","type":"analysis.storage.DisplayPaths","erasureStrategy":"Erased"},"value":{"paths":[{"#class":"analysis.storage.DisplayPath.Root","name":"_totalSupply"}]}},{"key":{"name":"tac.slot.type","type":"spec.cvlast.typedescriptors.EVMTypeDescriptor$EVMValueType","erasureStrategy":"Canonical"},"value":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256}},{"key":{"name":"tac.storage.non-indexed-path","type":"analysis.storage.StorageAnalysisResult$NonIndexedPath","erasureStrategy":"Canonical"},"value":{"#class":"analysis.storage.StorageAnalysisResult.NonIndexedPath.Root","slot":"2"}},{"key":{"name":"tac.storage","type":"java.math.BigInteger","erasureStrategy":"Canonical"},"value":"ce4604a0000000000000000000000003"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1023}]},"callIndex":3}}
		AnnotationCmd:24 JSON{"key":{"name":"tac.return.path","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		LabelCmd:24 "End procedure ERC20-totalSupply()"
		NopCmd
		AnnotationCmd:24 JSON{"key":{"name":"call.trace.pop","type":"analysis.icfg.Inliner$CallStack$PopRecord","erasureStrategy":"Canonical"},"value":"rO0ABXNyAClhbmFseXNpcy5pY2ZnLklubGluZXIkQ2FsbFN0YWNrJFBvcFJlY29yZPAPfwSLdCWJAgABSQAIY2FsbGVlSWR4cAAAAAM="}
	}
	Block 1_0_0_0_0_0 Succ [0_0_0_2_0_0] {
		AssumeNotCmd:24 false
		AssumeNotCmd:24 false
		AnnotationCmd JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageGlobalChangeSnippet.StorageTakeSnapshot","lhs":{"namePrefix":"lastStorage","tag":{"#class":"tac.Tag.BlockchainState"},"callIndex":0,"meta":[{"key":{"name":"cvl.local","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true},{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"lastStorage"},{"key":{"name":"cvl.type","type":"spec.cvlast.CVLType$PureCVLType","erasureStrategy":"CallTrace"},"value":{"#class":"spec.cvlast.CVLType.PureCVLType.VMInternal.BlockchainState"}},{"key":{"name":"cvl","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true},{"key":{"name":"cvl.display","type":"java.lang.String","erasureStrategy":"CallTrace"},"value":"lastStorage"}]}}}
		AssignExpCmd:28 CANON28!!55:29 Eq(CANON24!!3:30 I4 )
		AssumeCmd:24 CANON28!!55:29
		AnnotationCmd:24 JSON{"key":{"name":"cvl.label.end","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		AnnotationCmd:24 JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Message","s":"check effects of step taken by one of the functions"}}
		NopCmd
		NopCmd
		NopCmd
		NopCmd
		NopCmd
		NopCmd
		AssignExpCmd R62:31 CANON38:4
		AnnotationCmd:24 JSON{"key":{"name":"call.trace.push","type":"analysis.icfg.Inliner$CallStack$PushRecord","erasureStrategy":"Canonical"},"value":"rO0ABXNyACphbmFseXNpcy5pY2ZnLklubGluZXIkQ2FsbFN0YWNrJFB1c2hSZWNvcmSX8+DCTLCH+AIAA0kACGNhbGxlZUlkTAAGY2FsbGVldAATTHZjL2RhdGEvTWV0aG9kUmVmO0wAB3N1bW1hcnl0ABVMdmMvZGF0YS9DYWxsU3VtbWFyeTt4cAAAAAJzcgARdmMuZGF0YS5NZXRob2RSZWbJlJTzzU9pGAIAA0wABGF0dHJ0ABdMc2NlbmUvTWV0aG9kQXR0cmlidXRlO0wACmNvbnRyYWN0SWR0ABZMamF2YS9tYXRoL0JpZ0ludGVnZXI7TAAHc2lnSGFzaHQAEExldm0vU2lnaGFzaEludDt4cHNyABxzY2VuZS5NZXRob2RBdHRyaWJ1dGUkQ29tbW9uNHjdebdr9XMCAAB4cgAVc2NlbmUuTWV0aG9kQXR0cmlidXRlcYg2pYWutuUCAAB4cHNyABRqYXZhLm1hdGguQmlnSW50ZWdlcoz8nx+pO/sdAwAGSQAIYml0Q291bnRJAAliaXRMZW5ndGhJABNmaXJzdE5vbnplcm9CeXRlTnVtSQAMbG93ZXN0U2V0Qml0SQAGc2lnbnVtWwAJbWFnbml0dWRldAACW0J4cgAQamF2YS5sYW5nLk51bWJlcoaslR0LlOCLAgAAeHD///////////////7////+AAAAAXVyAAJbQqzzF/gGCFTgAgAAeHAAAAAQzkYEoAAAAAAAAAAAAAAAA3hzcgAOZXZtLlNpZ2hhc2hJbnRUdcqNMXEgeAIAAUwAAW5xAH4ABnhwc3EAfgAM///////////////+/////gAAAAF1cQB+ABAAAAAEI7hy3Xhw"}
		NopCmd
		AssumeExpCmd Ge(R62:32 0x64 )
		NopCmd
		AssumeExpCmd Ge(0x7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff R62:32 )
		AssignExpCmd R66:23 Select(CANON36:3 0x4 )
		AssignExpCmd tacCalldatabufCANON0@2:33 R66:23
		AssignExpCmd R67:23 Select(CANON36:3 0x24 )
		AssignExpCmd tacCalldatabufCANON1@2:34 R67:23
		AssignExpCmd R68:23 Select(CANON36:3 0x44 )
		AssignExpCmd tacCalldatabufCANON2@2:35 R68:23
		AssignExpCmd:24 B70 LAnd(Ge(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff CANON7:15 ) Le(0x0 CANON7:15 ) )
		AssertCmd:24 B70 "sanity bounds check on cvl to vm encoding of tacTmp!1491:int failed"
		AssignExpCmd:24 R71:23 Apply(safe_math_narrow:bif CANON7:15)
		NopCmd
		AssumeExpCmd LAnd(Le(R71:36 0xffffffffffffffffffffffffffffffffffffffff ) Ge(R71:36 0x0 ) )
		AssignExpCmd:24 B75 LAnd(Ge(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff CANON8:16 ) Le(0x0 CANON8:16 ) )
		AssertCmd:24 B75 "sanity bounds check on cvl to vm encoding of tacTmp!1496:int failed"
		AssignExpCmd:24 R76:23 Apply(safe_math_narrow:bif CANON8:16)
		NopCmd
		AssumeExpCmd LAnd(Le(R76:37 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff ) Ge(R76:37 0x0 ) )
		AssignExpCmd:24 B81 LAnd(Ge(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff CANON9:17 ) Le(0x0 CANON9:17 ) )
		AssertCmd:24 B81 "sanity bounds check on cvl to vm encoding of tacTmp!1500:int failed"
		AssignExpCmd:24 R82:23 Apply(safe_math_narrow:bif CANON9:17)
		NopCmd
		AssumeExpCmd LAnd(Le(R82:38 0xffffffffffffffffffffffffffffffffffffffff ) Ge(R82:38 0x0 ) )
		AssignExpCmd:24 B86 LAnd(Ge(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff CANON13:21 ) Le(0x0 CANON13:21 ) )
		AssertCmd:24 B86 "sanity bounds check on cvl to vm encoding of tacTmp!1503:int failed"
		AssignExpCmd:24 R87:23 Apply(safe_math_narrow:bif CANON13:21)
		NopCmd
		AssumeExpCmd LAnd(Le(R87:39 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff ) Ge(R87:39 0x0 ) )
		AssignExpCmd:24 B91 LAnd(Ge(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff CANON14:22 ) Le(0x0 CANON14:22 ) )
		AssertCmd:24 B91 "sanity bounds check on cvl to vm encoding of tacTmp!1506:int failed"
		AssignExpCmd:24 R92:23 Apply(safe_math_narrow:bif CANON14:22)
		NopCmd
		AssumeExpCmd LAnd(Le(R92:40 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff ) Ge(R92:40 0x0 ) )
		AssignExpCmd:24 B96 LAnd(Ge(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff CANON8:16 ) Le(0x0 CANON8:16 ) )
		AssertCmd:24 B96 "sanity bounds check on cvl to vm encoding of tacTmp!1509:int failed"
		AssignExpCmd:24 R97:23 Apply(safe_math_narrow:bif CANON8:16)
		AssignExpCmd:24 B99 LAnd(Ge(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff CANON7:15 ) Le(0x0 CANON7:15 ) )
		AssertCmd:24 B99 "sanity bounds check on cvl to vm encoding of tacTmp!1512:int failed"
		AssignExpCmd:24 R100:23 Apply(safe_math_narrow:bif CANON7:15)
		AssignExpCmd:24 R103:23 Select(tacBalance!!2:1 Apply(to_skey:bif R100:23) )
		AssignExpCmd:41 I104:23 IntSub(R103:23 R97:23 )
		AssignExpCmd:41 tacBalance!!105:1 Store(tacBalance!!2:1 Apply(to_skey:bif R100:23) I104:23 )
		AssignExpCmd:24 R106:23 Select(tacBalance!!105:1 Apply(to_skey:bif R7:7) )
		AssignExpCmd:41 R107:23 Add(R106:23 R97:23)
		NopCmd
		AssumeExpCmd Apply(add_noofl:bif R106:23 R97:23)
		AnnotationCmd:24 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.BalanceSnippet","srcAccountInfo":{"old":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R103","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}]},"new":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"I104","tag":{"#class":"tac.Tag.Int"},"callIndex":0,"meta":[{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}]},"addr":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R100","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}]}},"trgAccountInfo":{"old":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R106","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}]},"new":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R107","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}]},"addr":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R7","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"tacContractAt"},{"key":{"name":"tac.contract.sym.addr.name","type":"java.lang.String","erasureStrategy":"Erased"},"value":"ERC20"},{"key":{"name":"tac.contract.sym.addr","type":"java.math.BigInteger","erasureStrategy":"Erased"},"value":"ce4604a0000000000000000000000003"}]}},"transferredAmount":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R97","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}]}}}
		JumpCmd 0_0_0_2_0_0
	}
	Block 3_0_0_0_0_0 Succ [] {
		AssumeNotCmd:24 false
		AssumeNotCmd:24 false
		AnnotationCmd JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageGlobalChangeSnippet.StorageTakeSnapshot","lhs":{"namePrefix":"lastStorage","tag":{"#class":"tac.Tag.BlockchainState"},"callIndex":0,"meta":[{"key":{"name":"cvl.local","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true},{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"lastStorage"},{"key":{"name":"cvl.type","type":"spec.cvlast.CVLType$PureCVLType","erasureStrategy":"CallTrace"},"value":{"#class":"spec.cvlast.CVLType.PureCVLType.VMInternal.BlockchainState"}},{"key":{"name":"cvl","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true},{"key":{"name":"cvl.display","type":"java.lang.String","erasureStrategy":"CallTrace"},"value":"lastStorage"}]}}}
		AssignExpCmd:42 CANON104!!110:29 Eq(CANON24!!3:30 I183 )
		AssertCmd:43 CANON104!!110:29 "invariant violated in post-state"
		AnnotationCmd:24 JSON{"key":{"name":"cvl.label.end","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
	}
	Block 0_0_0_2_0_0 Succ [2_0_0_0_0_0] {
		LabelCmd "Start procedure ERC20-transferFrom(address,address,uint256)"
		AnnotationCmd JSON{"key":{"name":"fps.free-pointer-is-scalarized","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true}
		AssignExpCmd R111:23 Select(tacExtcodesize!!0:0 Apply(to_skey:bif R7:26) )
		NopCmd
		AssumeExpCmd Gt(R111:23 0x0 )
		AnnotationCmd JSON{"key":{"name":"internal.func.finder.info","type":"analysis.ip.InternalFunctionFinderReport","erasureStrategy":"Erased"},"value":"rO0ABXNyAChhbmFseXNpcy5pcC5JbnRlcm5hbEZ1bmN0aW9uRmluZGVyUmVwb3J0ian+bYn1VdACAAFMABN1bnJlc29sdmVkRnVuY3Rpb25zdAAPTGphdmEvdXRpbC9TZXQ7eHBzcgAhZGF0YXN0cnVjdHVyZXMuTGlua2VkQXJyYXlIYXNoU2V0AAAAAAAAAAEDAAJGAApsb2FkRmFjdG9yTAAJaGFzaFRhYmxldAAuTGRhdGFzdHJ1Y3R1cmVzL2FycmF5aGFzaHRhYmxlL0FycmF5SGFzaFRhYmxlO3hwdwgAAAAAQAAAAHg="}
		AnnotationCmd JSON{"key":{"name":"fps.free-pointer-is-scalarized","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true}
		NopCmd
		AssumeExpCmd LNot(Lt(R62:32 0x4 ) )
		NopCmd
		AssumeExpCmd Gt(0x70a08231 tacSighash!!9:8 )
		NopCmd
		AssumeExpCmd Gt(0x2e1a7d4d tacSighash!!9:8 )
		NopCmd
		AssumeExpCmd LNot(Eq(0x6fdde03 tacSighash!!9:8 ) )
		NopCmd
		AssumeExpCmd LNot(Eq(0x95ea7b3 tacSighash!!9:8 ) )
		NopCmd
		AssumeExpCmd LNot(Eq(0x18160ddd tacSighash!!9:8 ) )
		NopCmd
		AssumeExpCmd Eq(0x23b872dd tacSighash!!9:8 )
		NopCmd
		AssumeExpCmd Eq(R76:37 0x0 )
		AssignExpCmd:44 R121:45 Sub(CANON38:4 0x4 )
		NopCmd
		AssumeExpCmd LNot(Slt(R121:45 0x60 ) )
		AssignExpCmd:46 R123:47 tacCalldatabufCANON0@2:48
		NopCmd
		AssumeExpCmd Le(tacCalldatabufCANON0@2:48 0xffffffffffffffffffffffffffffffffffffffff )
		AssignExpCmd:46 R125:47 tacCalldatabufCANON1@2:49
		NopCmd
		AssumeExpCmd Le(tacCalldatabufCANON1@2:49 0xffffffffffffffffffffffffffffffffffffffff )
		AssignExpCmd:50 R127:47 tacCalldatabufCANON2@2:51
		AnnotationCmd JSON{"key":{"name":"internal.func.start","type":"analysis.ip.InternalFuncStartAnnotation","erasureStrategy":"CallTrace"},"value":{"id":1,"startPc":1450,"args":[{"s":{"namePrefix":"R123","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1011}]},"offset":1,"sort":"SCALAR"},{"s":{"namePrefix":"R125","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1011}]},"offset":2,"sort":"SCALAR"},{"s":{"namePrefix":"R127","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1011}]},"offset":3,"sort":"SCALAR"}],"methodSignature":{"#class":"spec.cvlast.QualifiedMethodSignature.QualifiedMethodSig","qualifiedMethodName":{"#class":"spec.cvlast.QualifiedFunction","host":{"name":"ERC20"},"methodId":"transferFrom"},"params":[{"#class":"spec.cvlast.VMParam.Named","name":"sender","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$address"}},{"#class":"spec.cvlast.VMParam.Named","name":"recipient","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$address"}},{"#class":"spec.cvlast.VMParam.Named","name":"amount","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256}}],"res":[{"#class":"spec.cvlast.VMParam.Unnamed","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$bool"}}]},"stackOffsetToArgPos":{"1":0,"2":1,"3":2},"callSiteSrc":{"source":0,"begin":7328,"len":851,"jumpType":"ENTER","address":"ce4604a0000000000000000000000003","sourceContext":{"indexToFilepath":{"0":"contracts/ERC20.sol","1":"contracts/IERC20.sol","2":"contracts/IERC20Metadata.sol"},"sourceDir":".post_autofinders.0"}}}}
		AssignExpCmd R128:45 tacCalldatabufCANON0@2:48
		NopCmd
		AssignExpCmd:52 R130:53 Apply(hash_3_keccak:bif Apply(skey_basic:bif 0x40) Apply(to_skey:bif tacCalldatabufCANON0@2:48) Apply(skey_basic:bif 0x1))
		AssignExpCmd:54 R134:53 Apply(hash_3_keccak:bif Apply(skey_basic:bif 0x40) Apply(to_skey:bif R71:55) R130:56)
		AssignExpCmd:57 R135:53 Select(CANON74!!5:5 R134:58 )
		AnnotationCmd JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet","value":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R135","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1017}]},"displayPath":{"#class":"analysis.storage.DisplayPath.MapAccess","key":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R71","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.env.known-bit-width","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":160},{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1015}]},"keyTyp":{"#class":"tac.TACStorageType.IntegralType","typeLabel":"address","numBytes":"14","descriptor":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$address"},"lowerBound":null,"upperBound":null},"base":{"#class":"analysis.storage.DisplayPath.MapAccess","key":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R128","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1015}]},"keyTyp":{"#class":"tac.TACStorageType.IntegralType","typeLabel":"address","numBytes":"14","descriptor":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$address"},"lowerBound":null,"upperBound":null},"base":{"#class":"analysis.storage.DisplayPath.Root","name":"_allowances"}}},"storageType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256},"contractInstance":"ce4604a0000000000000000000000003","linkableStorageReadId":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet.None"}}}
		NopCmd
		AssumeExpCmd LNot(Lt(R135:53 tacCalldatabufCANON2@2:51 ) )
		AssignExpCmd:59 R138:60 Sub(R135:53 R68:23 )
		AnnotationCmd JSON{"key":{"name":"internal.func.start","type":"analysis.ip.InternalFuncStartAnnotation","erasureStrategy":"CallTrace"},"value":{"id":2,"startPc":5140,"args":[{"s":{"namePrefix":"R123","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1011}]},"offset":1,"sort":"SCALAR"},{"s":{"namePrefix":"R71","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.env.known-bit-width","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":160},{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1015}]},"offset":2,"sort":"SCALAR"},{"s":{"namePrefix":"R138","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1014}]},"offset":3,"sort":"SCALAR"}],"methodSignature":{"#class":"spec.cvlast.QualifiedMethodSignature.QualifiedMethodSig","qualifiedMethodName":{"#class":"spec.cvlast.QualifiedFunction","host":{"name":"ERC20"},"methodId":"_approve"},"params":[{"#class":"spec.cvlast.VMParam.Named","name":"owner","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$address"}},{"#class":"spec.cvlast.VMParam.Named","name":"spender","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$address"}},{"#class":"spec.cvlast.VMParam.Named","name":"amount","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256}}],"res":[]},"stackOffsetToArgPos":{"1":0,"2":1,"3":2},"callSiteSrc":{"source":0,"begin":8038,"len":55,"jumpType":"ENTER","address":"ce4604a0000000000000000000000003","sourceContext":{"indexToFilepath":{"0":"contracts/ERC20.sol","1":"contracts/IERC20.sol","2":"contracts/IERC20Metadata.sol"},"sourceDir":".post_autofinders.0"}}}}
		AssignExpCmd R139:61 tacCalldatabufCANON0@2:48
		NopCmd
		AssumeExpCmd LNot(Eq(R139:61 0x0 ) )
		NopCmd
		AssumeExpCmd LNot(Eq(R71:36 0x0 ) )
		AssignExpCmd R142:62 tacCalldatabufCANON0@2:48
		AnnotationCmd JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.StoreSnippet","value":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R138","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1014}]},"displayPath":{"#class":"analysis.storage.DisplayPath.MapAccess","key":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R71","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.env.known-bit-width","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":160},{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1010}]},"keyTyp":{"#class":"tac.TACStorageType.IntegralType","typeLabel":"address","numBytes":"14","descriptor":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$address"},"lowerBound":null,"upperBound":null},"base":{"#class":"analysis.storage.DisplayPath.MapAccess","key":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R142","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1010}]},"keyTyp":{"#class":"tac.TACStorageType.IntegralType","typeLabel":"address","numBytes":"14","descriptor":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$address"},"lowerBound":null,"upperBound":null},"base":{"#class":"analysis.storage.DisplayPath.Root","name":"_allowances"}}},"storageType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256},"contractInstance":"ce4604a0000000000000000000000003"}}
		AnnotationCmd JSON{"key":{"name":"internal.func.end","type":"analysis.ip.InternalFuncExitAnnotation","erasureStrategy":"Canonical"},"value":{"id":2,"rets":[],"functionLayout":{}}}
		AnnotationCmd JSON{"key":{"name":"internal.func.start","type":"analysis.ip.InternalFuncStartAnnotation","erasureStrategy":"CallTrace"},"value":{"id":3,"startPc":5746,"args":[{"s":{"namePrefix":"R123","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1011}]},"offset":1,"sort":"SCALAR"},{"s":{"namePrefix":"R125","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1011}]},"offset":2,"sort":"SCALAR"},{"s":{"namePrefix":"R127","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1011}]},"offset":3,"sort":"SCALAR"}],"methodSignature":{"#class":"spec.cvlast.QualifiedMethodSignature.QualifiedMethodSig","qualifiedMethodName":{"#class":"spec.cvlast.QualifiedFunction","host":{"name":"ERC20"},"methodId":"_transfer"},"params":[{"#class":"spec.cvlast.VMParam.Named","name":"sender","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$address"}},{"#class":"spec.cvlast.VMParam.Named","name":"recipient","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$address"}},{"#class":"spec.cvlast.VMParam.Named","name":"amount","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256}}],"res":[]},"stackOffsetToArgPos":{"1":0,"2":1,"3":2},"callSiteSrc":{"source":0,"begin":8114,"len":36,"jumpType":"ENTER","address":"ce4604a0000000000000000000000003","sourceContext":{"indexToFilepath":{"0":"contracts/ERC20.sol","1":"contracts/IERC20.sol","2":"contracts/IERC20Metadata.sol"},"sourceDir":".post_autofinders.0"}}}}
		AssignExpCmd R149:61 tacCalldatabufCANON0@2:48
		NopCmd
		AssumeExpCmd LNot(Eq(R149:61 0x0 ) )
		AssignExpCmd R151:61 tacCalldatabufCANON1@2:49
		NopCmd
		AssumeExpCmd LNot(Eq(R151:61 0x0 ) )
		AnnotationCmd JSON{"key":{"name":"internal.func.start","type":"analysis.ip.InternalFuncStartAnnotation","erasureStrategy":"CallTrace"},"value":{"id":4,"startPc":6534,"args":[{"s":{"namePrefix":"R123","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1011}]},"offset":1,"sort":"SCALAR"},{"s":{"namePrefix":"R125","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1011}]},"offset":2,"sort":"SCALAR"},{"s":{"namePrefix":"R127","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1011}]},"offset":3,"sort":"SCALAR"}],"methodSignature":{"#class":"spec.cvlast.QualifiedMethodSignature.QualifiedMethodSig","qualifiedMethodName":{"#class":"spec.cvlast.QualifiedFunction","host":{"name":"ERC20"},"methodId":"_beforeTokenTransfer"},"params":[{"#class":"spec.cvlast.VMParam.Named","name":"from","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$address"}},{"#class":"spec.cvlast.VMParam.Named","name":"to","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$address"}},{"#class":"spec.cvlast.VMParam.Named","name":"amount","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256}}],"res":[]},"stackOffsetToArgPos":{"1":0,"2":1,"3":2},"callSiteSrc":{"source":0,"begin":11607,"len":47,"jumpType":"ENTER","address":"ce4604a0000000000000000000000003","sourceContext":{"indexToFilepath":{"0":"contracts/ERC20.sol","1":"contracts/IERC20.sol","2":"contracts/IERC20Metadata.sol"},"sourceDir":".post_autofinders.0"}}}}
		AnnotationCmd JSON{"key":{"name":"internal.func.end","type":"analysis.ip.InternalFuncExitAnnotation","erasureStrategy":"Canonical"},"value":{"id":4,"rets":[],"functionLayout":{}}}
		AssignExpCmd R153:62 tacCalldatabufCANON0@2:48
		NopCmd
		AssignExpCmd:63 R155:61 Apply(hash_3_keccak:bif Apply(skey_basic:bif 0x40) Apply(to_skey:bif tacCalldatabufCANON0@2:48) Apply(skey_basic:bif 0x0))
		AssignExpCmd:64 R156:61 Select(CANON83!!6:6 R155:65 )
		AnnotationCmd JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet","value":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R156","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1012}]},"displayPath":{"#class":"analysis.storage.DisplayPath.MapAccess","key":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R153","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1010}]},"keyTyp":{"#class":"tac.TACStorageType.IntegralType","typeLabel":"address","numBytes":"14","descriptor":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$address"},"lowerBound":null,"upperBound":null},"base":{"#class":"analysis.storage.DisplayPath.Root","name":"_balances"}},"storageType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256},"contractInstance":"ce4604a0000000000000000000000003","linkableStorageReadId":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet.None"}}}
		NopCmd
		AssumeExpCmd LNot(Lt(R156:61 tacCalldatabufCANON2@2:51 ) )
		AssignExpCmd:66 R158:61 Sub(R156:61 R68:23 )
		AssignExpCmd R159:67 tacCalldatabufCANON0@2:48
		NopCmd
		AssignExpCmd:68 R161:47 Apply(hash_3_keccak:bif Apply(skey_basic:bif 0x40) Apply(to_skey:bif tacCalldatabufCANON0@2:48) Apply(skey_basic:bif 0x0))
		AnnotationCmd JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Message","s":"Apply hook Hook Sstore 0x0.0x0[key a] uint256 new_value tacS:wordmap"}}
		AssignExpCmd R162:23 Select(CANON83!!6:6 R161:69 )
		AnnotationCmd JSON{"key":{"name":"tac.inlined.hook","type":"instrumentation.transformers.HookInliner$InlinedHook","erasureStrategy":"Canonical"},"value":{"cvlPattern":{"#class":"spec.cvlast.CVLHookPattern.StoragePattern.Store","value":{"name":"new_value","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256}},"slot":{"#class":"spec.cvlast.CVLSlotPattern.MapAccess","base":{"#class":"spec.cvlast.CVLSlotPattern.Static.Named","solidityContract":{"name":"ERC20"},"name":"_balances"},"key":{"name":"a","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$address"}}},"base":"STORAGE","previousValue":{"name":"old_value","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256}}},"substitutions":{"new_value":{"#class":"vc.data.HookValue.Direct","expr":{"#class":"vc.data.TACExpr.Sym.Var","s":{"namePrefix":"R158","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1012}]},"tag":{"#class":"tac.Tag.Bit256"}}},"old_value":{"#class":"vc.data.HookValue.Direct","expr":{"#class":"vc.data.TACExpr.Sym.Var","s":{"namePrefix":"R162","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}]},"tag":{"#class":"tac.Tag.Bit256"}}},"a":{"#class":"vc.data.HookValue.Direct","expr":{"#class":"vc.data.TACExpr.Sym.Var","s":{"namePrefix":"R159","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1009}]},"tag":{"#class":"tac.Tag.Bit256"}}}}}}
		AssignExpCmd:70 CANON83!!163:6 Store(CANON83!!6:6 R161:69 R158:61 )
		NopCmd
		AssignExpCmd:71 I166 IntAdd(I4 R158:61)
		NopCmd
		AssignExpCmd:72 I168 IntSub(I166 R162:23 )
		AnnotationCmd JSON{"key":{"name":"cvl.label.end","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		AnnotationCmd JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.StoreSnippet","value":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R158","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1012}]},"displayPath":{"#class":"analysis.storage.DisplayPath.MapAccess","key":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R159","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1009}]},"keyTyp":{"#class":"tac.TACStorageType.IntegralType","typeLabel":"address","numBytes":"14","descriptor":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$address"},"lowerBound":null,"upperBound":null},"base":{"#class":"analysis.storage.DisplayPath.Root","name":"_balances"}},"storageType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256},"contractInstance":"ce4604a0000000000000000000000003"}}
		AssignExpCmd R169:67 tacCalldatabufCANON1@2:49
		NopCmd
		AssignExpCmd:73 R171:47 Apply(hash_3_keccak:bif Apply(skey_basic:bif 0x40) Apply(to_skey:bif tacCalldatabufCANON1@2:49) Apply(skey_basic:bif 0x0))
		AssignExpCmd:74 R172:75 Select(CANON83!!163:6 R171:76 )
		AnnotationCmd JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet","value":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R172","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1008}]},"displayPath":{"#class":"analysis.storage.DisplayPath.MapAccess","key":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R169","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1009}]},"keyTyp":{"#class":"tac.TACStorageType.IntegralType","typeLabel":"address","numBytes":"14","descriptor":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$address"},"lowerBound":null,"upperBound":null},"base":{"#class":"analysis.storage.DisplayPath.Root","name":"_balances"}},"storageType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256},"contractInstance":"ce4604a0000000000000000000000003","linkableStorageReadId":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet.None"}}}
		NopCmd
		AssumeExpCmd Apply(add_noofl:bif R172:75 tacCalldatabufCANON2@2:51)
		AssignExpCmd I174:23 Apply(safe_math_promotion:bif R172:75)
		AssignExpCmd I175:23 Apply(safe_math_promotion:bif tacCalldatabufCANON2@2:51)
		NopCmd
		AssignExpCmd R177:77 Apply(safe_math_narrow:bif IntAdd(I174:23 I175:23))
		AnnotationCmd JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Message","s":"Apply hook Hook Sstore 0x0.0x0[key a] uint256 new_value tacS:wordmap"}}
		AssignExpCmd R178:23 Select(CANON83!!163:6 R171:76 )
		AnnotationCmd JSON{"key":{"name":"tac.inlined.hook","type":"instrumentation.transformers.HookInliner$InlinedHook","erasureStrategy":"Canonical"},"value":{"cvlPattern":{"#class":"spec.cvlast.CVLHookPattern.StoragePattern.Store","value":{"name":"new_value","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256}},"slot":{"#class":"spec.cvlast.CVLSlotPattern.MapAccess","base":{"#class":"spec.cvlast.CVLSlotPattern.Static.Named","solidityContract":{"name":"ERC20"},"name":"_balances"},"key":{"name":"a","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$address"}}},"base":"STORAGE","previousValue":{"name":"old_value","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256}}},"substitutions":{"new_value":{"#class":"vc.data.HookValue.Direct","expr":{"#class":"vc.data.TACExpr.Sym.Var","s":{"namePrefix":"R177","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1005}]},"tag":{"#class":"tac.Tag.Bit256"}}},"old_value":{"#class":"vc.data.HookValue.Direct","expr":{"#class":"vc.data.TACExpr.Sym.Var","s":{"namePrefix":"R178","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}]},"tag":{"#class":"tac.Tag.Bit256"}}},"a":{"#class":"vc.data.HookValue.Direct","expr":{"#class":"vc.data.TACExpr.Sym.Var","s":{"namePrefix":"R169","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1009}]},"tag":{"#class":"tac.Tag.Bit256"}}}}}}
		NopCmd
		AssignExpCmd:78 I181 IntAdd(I168 R177:77)
		NopCmd
		AssignExpCmd:79 I183 IntSub(I181 R178:23 )
		AnnotationCmd JSON{"key":{"name":"cvl.label.end","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		AnnotationCmd JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.StoreSnippet","value":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R177","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1005}]},"displayPath":{"#class":"analysis.storage.DisplayPath.MapAccess","key":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R169","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1009}]},"keyTyp":{"#class":"tac.TACStorageType.IntegralType","typeLabel":"address","numBytes":"14","descriptor":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$address"},"lowerBound":null,"upperBound":null},"base":{"#class":"analysis.storage.DisplayPath.Root","name":"_balances"}},"storageType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256},"contractInstance":"ce4604a0000000000000000000000003"}}
		AnnotationCmd JSON{"key":{"name":"internal.func.start","type":"analysis.ip.InternalFuncStartAnnotation","erasureStrategy":"CallTrace"},"value":{"id":5,"startPc":6686,"args":[{"s":{"namePrefix":"R123","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1011}]},"offset":1,"sort":"SCALAR"},{"s":{"namePrefix":"R125","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1011}]},"offset":2,"sort":"SCALAR"},{"s":{"namePrefix":"R127","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1011}]},"offset":3,"sort":"SCALAR"}],"methodSignature":{"#class":"spec.cvlast.QualifiedMethodSignature.QualifiedMethodSig","qualifiedMethodName":{"#class":"spec.cvlast.QualifiedFunction","host":{"name":"ERC20"},"methodId":"_afterTokenTransfer"},"params":[{"#class":"spec.cvlast.VMParam.Named","name":"from","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$address"}},{"#class":"spec.cvlast.VMParam.Named","name":"to","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$address"}},{"#class":"spec.cvlast.VMParam.Named","name":"amount","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256}}],"res":[]},"stackOffsetToArgPos":{"1":0,"2":1,"3":2},"callSiteSrc":{"source":0,"begin":12013,"len":46,"jumpType":"ENTER","address":"ce4604a0000000000000000000000003","sourceContext":{"indexToFilepath":{"0":"contracts/ERC20.sol","1":"contracts/IERC20.sol","2":"contracts/IERC20Metadata.sol"},"sourceDir":".post_autofinders.0"}}}}
		AnnotationCmd JSON{"key":{"name":"internal.func.end","type":"analysis.ip.InternalFuncExitAnnotation","erasureStrategy":"Canonical"},"value":{"id":5,"rets":[],"functionLayout":{}}}
		AnnotationCmd JSON{"key":{"name":"internal.func.end","type":"analysis.ip.InternalFuncExitAnnotation","erasureStrategy":"Canonical"},"value":{"id":3,"rets":[],"functionLayout":{}}}
		AssignExpCmd R184:80 0x1
		AnnotationCmd JSON{"key":{"name":"internal.func.end","type":"analysis.ip.InternalFuncExitAnnotation","erasureStrategy":"Canonical"},"value":{"id":1,"rets":[{"s":{"namePrefix":"R184","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1023}]},"offset":0}],"functionLayout":{"0":{"#class":"analysis.ip.InternalFuncValueLocation.Scalar"}}}}
		AnnotationCmd JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.EVMFunctionReturnWrite","returnbufOffset":"0","returnValueSym":{"#class":"vc.data.TACSymbol.Const","value":"1","tag":{"#class":"tac.Tag.Bool"}},"callIndex":2}}
		AnnotationCmd JSON{"key":{"name":"tac.return.path","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		LabelCmd "End procedure ERC20-transferFrom(address,address,uint256)"
		JumpCmd 2_0_0_0_0_0
	}
	Block 2_0_0_0_0_0 Succ [0_0_0_3_0_0] {
		AnnotationCmd:24 JSON{"key":{"name":"call.trace.pop","type":"analysis.icfg.Inliner$CallStack$PopRecord","erasureStrategy":"Canonical"},"value":"rO0ABXNyAClhbmFseXNpcy5pY2ZnLklubGluZXIkQ2FsbFN0YWNrJFBvcFJlY29yZPAPfwSLdCWJAgABSQAIY2FsbGVlSWR4cAAAAAI="}
		AssumeNotCmd:24 false
		AssumeNotCmd:24 false
		AnnotationCmd JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageGlobalChangeSnippet.StorageTakeSnapshot","lhs":{"namePrefix":"lastStorage","tag":{"#class":"tac.Tag.BlockchainState"},"callIndex":0,"meta":[{"key":{"name":"cvl.local","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true},{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"lastStorage"},{"key":{"name":"cvl.type","type":"spec.cvlast.CVLType$PureCVLType","erasureStrategy":"CallTrace"},"value":{"#class":"spec.cvlast.CVLType.PureCVLType.VMInternal.BlockchainState"}},{"key":{"name":"cvl","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true},{"key":{"name":"cvl.display","type":"java.lang.String","erasureStrategy":"CallTrace"},"value":"lastStorage"}]}}}
		AnnotationCmd:24 JSON{"key":{"name":"cvl.label.end","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		AnnotationCmd:24 JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Message","s":"assert invariant in post-state"}}
	}
}
Axioms {
		CANON27
}
Metas {
  "0": [
    {
      "key": {
        "name": "Tac.symbol.keyword",
        "type": "java.lang.String",
        "erasureStrategy": "Canonical"
      },
      "value": "tacExtcodesize"
    },
    {
      "key": {
        "name": "tac.is.extcodesize",
        "type": "tac.MetaMap$Companion$NothingValue",
        "erasureStrategy": "Canonical"
      },
      "value": {
      }
    }
  ],
  "1": [
    {
      "key": {
        "name": "Tac.symbol.keyword",
        "type": "java.lang.String",
        "erasureStrategy": "Canonical"
      },
      "value": "tacBalance"
    }
  ],
  "2": [
    {
      "key": {
        "name": "tac.scalarization.sort",
        "type": "vc.data.ScalarizationSort",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.ScalarizationSort.Split",
        "idx": "2"
      }
    },
    {
      "key": {
        "name": "tac.storage.bit-width",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 256
    },
    {
      "key": {
        "name": "tac.storage.pretty.paths",
        "type": "analysis.storage.DisplayPaths",
        "erasureStrategy": "Erased"
      },
      "value": {
        "paths": [
          {
            "#class": "analysis.storage.DisplayPath.Root",
            "name": "_totalSupply"
          }
        ]
      }
    },
    {
      "key": {
        "name": "tac.slot.type",
        "type": "spec.cvlast.typedescriptors.EVMTypeDescriptor$EVMValueType",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK",
        "bitwidth": 256
      }
    },
    {
      "key": {
        "name": "tac.storage.non-indexed-path",
        "type": "analysis.storage.StorageAnalysisResult$NonIndexedPath",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "analysis.storage.StorageAnalysisResult.NonIndexedPath.Root",
        "slot": "2"
      }
    },
    {
      "key": {
        "name": "tac.storage",
        "type": "java.math.BigInteger",
        "erasureStrategy": "Canonical"
      },
      "value": "ce4604a0000000000000000000000003"
    }
  ],
  "3": [
    {
      "key": {
        "name": "cvl.local",
        "type": "java.lang.Boolean",
        "erasureStrategy": "Canonical"
      },
      "value": true
    },
    {
      "key": {
        "name": "cvl.type",
        "type": "spec.cvlast.CVLType$PureCVLType",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "spec.cvlast.CVLType.PureCVLType.VMInternal.RawArgs"
      }
    },
    {
      "key": {
        "name": "cvl",
        "type": "java.lang.Boolean",
        "erasureStrategy": "Canonical"
      },
      "value": true
    },
    {
      "key": {
        "name": "cvl.display",
        "type": "java.lang.String",
        "erasureStrategy": "CallTrace"
      },
      "value": "invariantCalldata"
    }
  ],
  "4": [
    {
      "key": {
        "name": "cvl.local",
        "type": "java.lang.Boolean",
        "erasureStrategy": "Canonical"
      },
      "value": false
    },
    {
      "key": {
        "name": "cvl.type",
        "type": "spec.cvlast.CVLType$PureCVLType",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "spec.cvlast.CVLType.PureCVLType.VMInternal.RawArgs"
      }
    },
    {
      "key": {
        "name": "cvl",
        "type": "java.lang.Boolean",
        "erasureStrategy": "Canonical"
      },
      "value": true
    },
    {
      "key": {
        "name": "cvl.display",
        "type": "java.lang.String",
        "erasureStrategy": "CallTrace"
      },
      "value": "invariantCalldata"
    }
  ],
  "5": [
    {
      "key": {
        "name": "tac.scalarization.sort",
        "type": "vc.data.ScalarizationSort",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.ScalarizationSort.UnscalarizedBuffer"
      }
    },
    {
      "key": {
        "name": "tac.storage.bit-width",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 256
    },
    {
      "key": {
        "name": "tac.slot.type",
        "type": "spec.cvlast.typedescriptors.EVMTypeDescriptor$EVMValueType",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK",
        "bitwidth": 256
      }
    },
    {
      "key": {
        "name": "tac.storage.non-indexed-path",
        "type": "analysis.storage.StorageAnalysisResult$NonIndexedPath",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "analysis.storage.StorageAnalysisResult.NonIndexedPath.StructAccess",
        "base": {
          "#class": "analysis.storage.StorageAnalysisResult.NonIndexedPath.MapAccess",
          "base": {
            "#class": "analysis.storage.StorageAnalysisResult.NonIndexedPath.StructAccess",
            "base": {
              "#class": "analysis.storage.StorageAnalysisResult.NonIndexedPath.MapAccess",
              "base": {
                "#class": "analysis.storage.StorageAnalysisResult.NonIndexedPath.Root",
                "slot": "1"
              }
            },
            "offset": "0"
          }
        },
        "offset": "0"
      }
    },
    {
      "key": {
        "name": "tac.storage",
        "type": "java.math.BigInteger",
        "erasureStrategy": "Canonical"
      },
      "value": "ce4604a0000000000000000000000003"
    }
  ],
  "6": [
    {
      "key": {
        "name": "tac.scalarization.sort",
        "type": "vc.data.ScalarizationSort",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.ScalarizationSort.UnscalarizedBuffer"
      }
    },
    {
      "key": {
        "name": "tac.storage.bit-width",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 256
    },
    {
      "key": {
        "name": "tac.slot.type",
        "type": "spec.cvlast.typedescriptors.EVMTypeDescriptor$EVMValueType",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK",
        "bitwidth": 256
      }
    },
    {
      "key": {
        "name": "tac.storage.non-indexed-path",
        "type": "analysis.storage.StorageAnalysisResult$NonIndexedPath",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "analysis.storage.StorageAnalysisResult.NonIndexedPath.StructAccess",
        "base": {
          "#class": "analysis.storage.StorageAnalysisResult.NonIndexedPath.MapAccess",
          "base": {
            "#class": "analysis.storage.StorageAnalysisResult.NonIndexedPath.Root",
            "slot": "0"
          }
        },
        "offset": "0"
      }
    },
    {
      "key": {
        "name": "tac.storage",
        "type": "java.math.BigInteger",
        "erasureStrategy": "Canonical"
      },
      "value": "ce4604a0000000000000000000000003"
    }
  ],
  "7": [
    {
      "key": {
        "name": "Tac.symbol.keyword",
        "type": "java.lang.String",
        "erasureStrategy": "Canonical"
      },
      "value": "tacContractAt"
    },
    {
      "key": {
        "name": "tac.contract.sym.addr.name",
        "type": "java.lang.String",
        "erasureStrategy": "Erased"
      },
      "value": "ERC20"
    },
    {
      "key": {
        "name": "tac.contract.sym.addr",
        "type": "java.math.BigInteger",
        "erasureStrategy": "Erased"
      },
      "value": "ce4604a0000000000000000000000003"
    }
  ],
  "8": [
    {
      "key": {
        "name": "Tac.symbol.keyword",
        "type": "java.lang.String",
        "erasureStrategy": "Canonical"
      },
      "value": "tacSighash"
    }
  ],
  "9": [
    {
      "key": {
        "name": "cvl.struct.path",
        "type": "spec.cvlast.CVLStructPathNode",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "rootStructType": {
          "name": "method",
          "fields": [
            {
              "fieldName": "selector",
              "value": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                "k": 32
              }
            },
            {
              "fieldName": "isPure",
              "value": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
              }
            },
            {
              "fieldName": "isView",
              "value": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
              }
            },
            {
              "fieldName": "isPayable",
              "value": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
              }
            },
            {
              "fieldName": "numberOfArguments",
              "value": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                "k": 256
              }
            },
            {
              "fieldName": "isFallback",
              "value": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
              }
            }
          ]
        },
        "fields": [
          {
            "fieldName": "selector",
            "value": {
              "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
              "k": 32
            }
          }
        ]
      }
    },
    {
      "key": {
        "name": "cvl.local",
        "type": "java.lang.Boolean",
        "erasureStrategy": "Canonical"
      },
      "value": true
    },
    {
      "key": {
        "name": "cvl.type",
        "type": "spec.cvlast.CVLType$PureCVLType",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
        "k": 32
      }
    },
    {
      "key": {
        "name": "cvl",
        "type": "java.lang.Boolean",
        "erasureStrategy": "Canonical"
      },
      "value": true
    },
    {
      "key": {
        "name": "cvl.display",
        "type": "java.lang.String",
        "erasureStrategy": "CallTrace"
      },
      "value": "certoraInvF.selector"
    }
  ],
  "10": [
    {
      "key": {
        "name": "cvl.struct.path",
        "type": "spec.cvlast.CVLStructPathNode",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "rootStructType": {
          "name": "method",
          "fields": [
            {
              "fieldName": "selector",
              "value": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                "k": 32
              }
            },
            {
              "fieldName": "isPure",
              "value": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
              }
            },
            {
              "fieldName": "isView",
              "value": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
              }
            },
            {
              "fieldName": "isPayable",
              "value": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
              }
            },
            {
              "fieldName": "numberOfArguments",
              "value": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                "k": 256
              }
            },
            {
              "fieldName": "isFallback",
              "value": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
              }
            }
          ]
        },
        "fields": [
          {
            "fieldName": "isPure",
            "value": {
              "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
            }
          }
        ]
      }
    },
    {
      "key": {
        "name": "cvl.local",
        "type": "java.lang.Boolean",
        "erasureStrategy": "Canonical"
      },
      "value": true
    },
    {
      "key": {
        "name": "cvl.type",
        "type": "spec.cvlast.CVLType$PureCVLType",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
      }
    },
    {
      "key": {
        "name": "cvl",
        "type": "java.lang.Boolean",
        "erasureStrategy": "Canonical"
      },
      "value": true
    },
    {
      "key": {
        "name": "cvl.display",
        "type": "java.lang.String",
        "erasureStrategy": "CallTrace"
      },
      "value": "certoraInvF.isPure"
    }
  ],
  "11": [
    {
      "key": {
        "name": "cvl.struct.path",
        "type": "spec.cvlast.CVLStructPathNode",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "rootStructType": {
          "name": "method",
          "fields": [
            {
              "fieldName": "selector",
              "value": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                "k": 32
              }
            },
            {
              "fieldName": "isPure",
              "value": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
              }
            },
            {
              "fieldName": "isView",
              "value": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
              }
            },
            {
              "fieldName": "isPayable",
              "value": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
              }
            },
            {
              "fieldName": "numberOfArguments",
              "value": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                "k": 256
              }
            },
            {
              "fieldName": "isFallback",
              "value": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
              }
            }
          ]
        },
        "fields": [
          {
            "fieldName": "isView",
            "value": {
              "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
            }
          }
        ]
      }
    },
    {
      "key": {
        "name": "cvl.local",
        "type": "java.lang.Boolean",
        "erasureStrategy": "Canonical"
      },
      "value": true
    },
    {
      "key": {
        "name": "cvl.type",
        "type": "spec.cvlast.CVLType$PureCVLType",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
      }
    },
    {
      "key": {
        "name": "cvl",
        "type": "java.lang.Boolean",
        "erasureStrategy": "Canonical"
      },
      "value": true
    },
    {
      "key": {
        "name": "cvl.display",
        "type": "java.lang.String",
        "erasureStrategy": "CallTrace"
      },
      "value": "certoraInvF.isView"
    }
  ],
  "12": [
    {
      "key": {
        "name": "cvl.struct.path",
        "type": "spec.cvlast.CVLStructPathNode",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "rootStructType": {
          "name": "method",
          "fields": [
            {
              "fieldName": "selector",
              "value": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                "k": 32
              }
            },
            {
              "fieldName": "isPure",
              "value": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
              }
            },
            {
              "fieldName": "isView",
              "value": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
              }
            },
            {
              "fieldName": "isPayable",
              "value": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
              }
            },
            {
              "fieldName": "numberOfArguments",
              "value": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                "k": 256
              }
            },
            {
              "fieldName": "isFallback",
              "value": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
              }
            }
          ]
        },
        "fields": [
          {
            "fieldName": "isPayable",
            "value": {
              "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
            }
          }
        ]
      }
    },
    {
      "key": {
        "name": "cvl.local",
        "type": "java.lang.Boolean",
        "erasureStrategy": "Canonical"
      },
      "value": true
    },
    {
      "key": {
        "name": "cvl.type",
        "type": "spec.cvlast.CVLType$PureCVLType",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
      }
    },
    {
      "key": {
        "name": "cvl",
        "type": "java.lang.Boolean",
        "erasureStrategy": "Canonical"
      },
      "value": true
    },
    {
      "key": {
        "name": "cvl.display",
        "type": "java.lang.String",
        "erasureStrategy": "CallTrace"
      },
      "value": "certoraInvF.isPayable"
    }
  ],
  "13": [
    {
      "key": {
        "name": "cvl.struct.path",
        "type": "spec.cvlast.CVLStructPathNode",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "rootStructType": {
          "name": "method",
          "fields": [
            {
              "fieldName": "selector",
              "value": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                "k": 32
              }
            },
            {
              "fieldName": "isPure",
              "value": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
              }
            },
            {
              "fieldName": "isView",
              "value": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
              }
            },
            {
              "fieldName": "isPayable",
              "value": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
              }
            },
            {
              "fieldName": "numberOfArguments",
              "value": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                "k": 256
              }
            },
            {
              "fieldName": "isFallback",
              "value": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
              }
            }
          ]
        },
        "fields": [
          {
            "fieldName": "numberOfArguments",
            "value": {
              "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
              "k": 256
            }
          }
        ]
      }
    },
    {
      "key": {
        "name": "cvl.local",
        "type": "java.lang.Boolean",
        "erasureStrategy": "Canonical"
      },
      "value": true
    },
    {
      "key": {
        "name": "cvl.type",
        "type": "spec.cvlast.CVLType$PureCVLType",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
        "k": 256
      }
    },
    {
      "key": {
        "name": "cvl",
        "type": "java.lang.Boolean",
        "erasureStrategy": "Canonical"
      },
      "value": true
    },
    {
      "key": {
        "name": "cvl.display",
        "type": "java.lang.String",
        "erasureStrategy": "CallTrace"
      },
      "value": "certoraInvF.numberOfArguments"
    }
  ],
  "14": [
    {
      "key": {
        "name": "cvl.struct.path",
        "type": "spec.cvlast.CVLStructPathNode",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "rootStructType": {
          "name": "method",
          "fields": [
            {
              "fieldName": "selector",
              "value": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                "k": 32
              }
            },
            {
              "fieldName": "isPure",
              "value": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
              }
            },
            {
              "fieldName": "isView",
              "value": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
              }
            },
            {
              "fieldName": "isPayable",
              "value": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
              }
            },
            {
              "fieldName": "numberOfArguments",
              "value": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                "k": 256
              }
            },
            {
              "fieldName": "isFallback",
              "value": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
              }
            }
          ]
        },
        "fields": [
          {
            "fieldName": "isFallback",
            "value": {
              "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
            }
          }
        ]
      }
    },
    {
      "key": {
        "name": "cvl.local",
        "type": "java.lang.Boolean",
        "erasureStrategy": "Canonical"
      },
      "value": true
    },
    {
      "key": {
        "name": "cvl.type",
        "type": "spec.cvlast.CVLType$PureCVLType",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
      }
    },
    {
      "key": {
        "name": "cvl",
        "type": "java.lang.Boolean",
        "erasureStrategy": "Canonical"
      },
      "value": true
    },
    {
      "key": {
        "name": "cvl.display",
        "type": "java.lang.String",
        "erasureStrategy": "CallTrace"
      },
      "value": "certoraInvF.isFallback"
    }
  ],
  "15": [
    {
      "key": {
        "name": "cvl.struct.path",
        "type": "spec.cvlast.CVLStructPathNode",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "rootStructType": {
          "name": "env",
          "fields": [
            {
              "fieldName": "msg",
              "value": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
                "name": "msg",
                "fields": [
                  {
                    "fieldName": "sender",
                    "value": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                    }
                  },
                  {
                    "fieldName": "value",
                    "value": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  }
                ]
              }
            },
            {
              "fieldName": "tx",
              "value": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
                "name": "tx",
                "fields": [
                  {
                    "fieldName": "origin",
                    "value": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                    }
                  }
                ]
              }
            },
            {
              "fieldName": "block",
              "value": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
                "name": "block",
                "fields": [
                  {
                    "fieldName": "coinbase",
                    "value": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                    }
                  },
                  {
                    "fieldName": "difficulty",
                    "value": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "gaslimit",
                    "value": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "number",
                    "value": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "timestamp",
                    "value": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  }
                ]
              }
            }
          ]
        },
        "fields": [
          {
            "fieldName": "msg",
            "value": {
              "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
              "name": "msg",
              "fields": [
                {
                  "fieldName": "sender",
                  "value": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                  }
                },
                {
                  "fieldName": "value",
                  "value": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 256
                  }
                }
              ]
            }
          },
          {
            "fieldName": "sender",
            "value": {
              "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
            }
          }
        ]
      }
    },
    {
      "key": {
        "name": "cvl.local",
        "type": "java.lang.Boolean",
        "erasureStrategy": "Canonical"
      },
      "value": true
    },
    {
      "key": {
        "name": "cvl.type",
        "type": "spec.cvlast.CVLType$PureCVLType",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
      }
    },
    {
      "key": {
        "name": "cvl",
        "type": "java.lang.Boolean",
        "erasureStrategy": "Canonical"
      },
      "value": true
    },
    {
      "key": {
        "name": "cvl.display",
        "type": "java.lang.String",
        "erasureStrategy": "CallTrace"
      },
      "value": "invariantEnv.msg.sender"
    }
  ],
  "16": [
    {
      "key": {
        "name": "cvl.struct.path",
        "type": "spec.cvlast.CVLStructPathNode",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "rootStructType": {
          "name": "env",
          "fields": [
            {
              "fieldName": "msg",
              "value": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
                "name": "msg",
                "fields": [
                  {
                    "fieldName": "sender",
                    "value": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                    }
                  },
                  {
                    "fieldName": "value",
                    "value": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  }
                ]
              }
            },
            {
              "fieldName": "tx",
              "value": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
                "name": "tx",
                "fields": [
                  {
                    "fieldName": "origin",
                    "value": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                    }
                  }
                ]
              }
            },
            {
              "fieldName": "block",
              "value": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
                "name": "block",
                "fields": [
                  {
                    "fieldName": "coinbase",
                    "value": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                    }
                  },
                  {
                    "fieldName": "difficulty",
                    "value": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "gaslimit",
                    "value": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "number",
                    "value": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "timestamp",
                    "value": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  }
                ]
              }
            }
          ]
        },
        "fields": [
          {
            "fieldName": "msg",
            "value": {
              "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
              "name": "msg",
              "fields": [
                {
                  "fieldName": "sender",
                  "value": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                  }
                },
                {
                  "fieldName": "value",
                  "value": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 256
                  }
                }
              ]
            }
          },
          {
            "fieldName": "value",
            "value": {
              "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
              "k": 256
            }
          }
        ]
      }
    },
    {
      "key": {
        "name": "cvl.local",
        "type": "java.lang.Boolean",
        "erasureStrategy": "Canonical"
      },
      "value": true
    },
    {
      "key": {
        "name": "cvl.type",
        "type": "spec.cvlast.CVLType$PureCVLType",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
        "k": 256
      }
    },
    {
      "key": {
        "name": "cvl",
        "type": "java.lang.Boolean",
        "erasureStrategy": "Canonical"
      },
      "value": true
    },
    {
      "key": {
        "name": "cvl.display",
        "type": "java.lang.String",
        "erasureStrategy": "CallTrace"
      },
      "value": "invariantEnv.msg.value"
    }
  ],
  "17": [
    {
      "key": {
        "name": "cvl.struct.path",
        "type": "spec.cvlast.CVLStructPathNode",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "rootStructType": {
          "name": "env",
          "fields": [
            {
              "fieldName": "msg",
              "value": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
                "name": "msg",
                "fields": [
                  {
                    "fieldName": "sender",
                    "value": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                    }
                  },
                  {
                    "fieldName": "value",
                    "value": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  }
                ]
              }
            },
            {
              "fieldName": "tx",
              "value": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
                "name": "tx",
                "fields": [
                  {
                    "fieldName": "origin",
                    "value": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                    }
                  }
                ]
              }
            },
            {
              "fieldName": "block",
              "value": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
                "name": "block",
                "fields": [
                  {
                    "fieldName": "coinbase",
                    "value": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                    }
                  },
                  {
                    "fieldName": "difficulty",
                    "value": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "gaslimit",
                    "value": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "number",
                    "value": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "timestamp",
                    "value": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  }
                ]
              }
            }
          ]
        },
        "fields": [
          {
            "fieldName": "tx",
            "value": {
              "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
              "name": "tx",
              "fields": [
                {
                  "fieldName": "origin",
                  "value": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                  }
                }
              ]
            }
          },
          {
            "fieldName": "origin",
            "value": {
              "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
            }
          }
        ]
      }
    },
    {
      "key": {
        "name": "cvl.local",
        "type": "java.lang.Boolean",
        "erasureStrategy": "Canonical"
      },
      "value": true
    },
    {
      "key": {
        "name": "cvl.type",
        "type": "spec.cvlast.CVLType$PureCVLType",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
      }
    },
    {
      "key": {
        "name": "cvl",
        "type": "java.lang.Boolean",
        "erasureStrategy": "Canonical"
      },
      "value": true
    },
    {
      "key": {
        "name": "cvl.display",
        "type": "java.lang.String",
        "erasureStrategy": "CallTrace"
      },
      "value": "invariantEnv.tx.origin"
    }
  ],
  "18": [
    {
      "key": {
        "name": "cvl.struct.path",
        "type": "spec.cvlast.CVLStructPathNode",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "rootStructType": {
          "name": "env",
          "fields": [
            {
              "fieldName": "msg",
              "value": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
                "name": "msg",
                "fields": [
                  {
                    "fieldName": "sender",
                    "value": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                    }
                  },
                  {
                    "fieldName": "value",
                    "value": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  }
                ]
              }
            },
            {
              "fieldName": "tx",
              "value": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
                "name": "tx",
                "fields": [
                  {
                    "fieldName": "origin",
                    "value": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                    }
                  }
                ]
              }
            },
            {
              "fieldName": "block",
              "value": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
                "name": "block",
                "fields": [
                  {
                    "fieldName": "coinbase",
                    "value": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                    }
                  },
                  {
                    "fieldName": "difficulty",
                    "value": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "gaslimit",
                    "value": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "number",
                    "value": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "timestamp",
                    "value": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  }
                ]
              }
            }
          ]
        },
        "fields": [
          {
            "fieldName": "block",
            "value": {
              "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
              "name": "block",
              "fields": [
                {
                  "fieldName": "coinbase",
                  "value": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                  }
                },
                {
                  "fieldName": "difficulty",
                  "value": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 256
                  }
                },
                {
                  "fieldName": "gaslimit",
                  "value": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 256
                  }
                },
                {
                  "fieldName": "number",
                  "value": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 256
                  }
                },
                {
                  "fieldName": "timestamp",
                  "value": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 256
                  }
                }
              ]
            }
          },
          {
            "fieldName": "coinbase",
            "value": {
              "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
            }
          }
        ]
      }
    },
    {
      "key": {
        "name": "cvl.local",
        "type": "java.lang.Boolean",
        "erasureStrategy": "Canonical"
      },
      "value": true
    },
    {
      "key": {
        "name": "cvl.type",
        "type": "spec.cvlast.CVLType$PureCVLType",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
      }
    },
    {
      "key": {
        "name": "cvl",
        "type": "java.lang.Boolean",
        "erasureStrategy": "Canonical"
      },
      "value": true
    },
    {
      "key": {
        "name": "cvl.display",
        "type": "java.lang.String",
        "erasureStrategy": "CallTrace"
      },
      "value": "invariantEnv.block.coinbase"
    }
  ],
  "19": [
    {
      "key": {
        "name": "cvl.struct.path",
        "type": "spec.cvlast.CVLStructPathNode",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "rootStructType": {
          "name": "env",
          "fields": [
            {
              "fieldName": "msg",
              "value": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
                "name": "msg",
                "fields": [
                  {
                    "fieldName": "sender",
                    "value": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                    }
                  },
                  {
                    "fieldName": "value",
                    "value": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  }
                ]
              }
            },
            {
              "fieldName": "tx",
              "value": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
                "name": "tx",
                "fields": [
                  {
                    "fieldName": "origin",
                    "value": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                    }
                  }
                ]
              }
            },
            {
              "fieldName": "block",
              "value": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
                "name": "block",
                "fields": [
                  {
                    "fieldName": "coinbase",
                    "value": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                    }
                  },
                  {
                    "fieldName": "difficulty",
                    "value": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "gaslimit",
                    "value": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "number",
                    "value": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "timestamp",
                    "value": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  }
                ]
              }
            }
          ]
        },
        "fields": [
          {
            "fieldName": "block",
            "value": {
              "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
              "name": "block",
              "fields": [
                {
                  "fieldName": "coinbase",
                  "value": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                  }
                },
                {
                  "fieldName": "difficulty",
                  "value": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 256
                  }
                },
                {
                  "fieldName": "gaslimit",
                  "value": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 256
                  }
                },
                {
                  "fieldName": "number",
                  "value": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 256
                  }
                },
                {
                  "fieldName": "timestamp",
                  "value": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 256
                  }
                }
              ]
            }
          },
          {
            "fieldName": "difficulty",
            "value": {
              "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
              "k": 256
            }
          }
        ]
      }
    },
    {
      "key": {
        "name": "cvl.local",
        "type": "java.lang.Boolean",
        "erasureStrategy": "Canonical"
      },
      "value": true
    },
    {
      "key": {
        "name": "cvl.type",
        "type": "spec.cvlast.CVLType$PureCVLType",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
        "k": 256
      }
    },
    {
      "key": {
        "name": "cvl",
        "type": "java.lang.Boolean",
        "erasureStrategy": "Canonical"
      },
      "value": true
    },
    {
      "key": {
        "name": "cvl.display",
        "type": "java.lang.String",
        "erasureStrategy": "CallTrace"
      },
      "value": "invariantEnv.block.difficulty"
    }
  ],
  "20": [
    {
      "key": {
        "name": "cvl.struct.path",
        "type": "spec.cvlast.CVLStructPathNode",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "rootStructType": {
          "name": "env",
          "fields": [
            {
              "fieldName": "msg",
              "value": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
                "name": "msg",
                "fields": [
                  {
                    "fieldName": "sender",
                    "value": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                    }
                  },
                  {
                    "fieldName": "value",
                    "value": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  }
                ]
              }
            },
            {
              "fieldName": "tx",
              "value": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
                "name": "tx",
                "fields": [
                  {
                    "fieldName": "origin",
                    "value": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                    }
                  }
                ]
              }
            },
            {
              "fieldName": "block",
              "value": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
                "name": "block",
                "fields": [
                  {
                    "fieldName": "coinbase",
                    "value": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                    }
                  },
                  {
                    "fieldName": "difficulty",
                    "value": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "gaslimit",
                    "value": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "number",
                    "value": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "timestamp",
                    "value": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  }
                ]
              }
            }
          ]
        },
        "fields": [
          {
            "fieldName": "block",
            "value": {
              "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
              "name": "block",
              "fields": [
                {
                  "fieldName": "coinbase",
                  "value": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                  }
                },
                {
                  "fieldName": "difficulty",
                  "value": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 256
                  }
                },
                {
                  "fieldName": "gaslimit",
                  "value": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 256
                  }
                },
                {
                  "fieldName": "number",
                  "value": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 256
                  }
                },
                {
                  "fieldName": "timestamp",
                  "value": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 256
                  }
                }
              ]
            }
          },
          {
            "fieldName": "gaslimit",
            "value": {
              "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
              "k": 256
            }
          }
        ]
      }
    },
    {
      "key": {
        "name": "cvl.local",
        "type": "java.lang.Boolean",
        "erasureStrategy": "Canonical"
      },
      "value": true
    },
    {
      "key": {
        "name": "cvl.type",
        "type": "spec.cvlast.CVLType$PureCVLType",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
        "k": 256
      }
    },
    {
      "key": {
        "name": "cvl",
        "type": "java.lang.Boolean",
        "erasureStrategy": "Canonical"
      },
      "value": true
    },
    {
      "key": {
        "name": "cvl.display",
        "type": "java.lang.String",
        "erasureStrategy": "CallTrace"
      },
      "value": "invariantEnv.block.gaslimit"
    }
  ],
  "21": [
    {
      "key": {
        "name": "cvl.struct.path",
        "type": "spec.cvlast.CVLStructPathNode",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "rootStructType": {
          "name": "env",
          "fields": [
            {
              "fieldName": "msg",
              "value": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
                "name": "msg",
                "fields": [
                  {
                    "fieldName": "sender",
                    "value": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                    }
                  },
                  {
                    "fieldName": "value",
                    "value": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  }
                ]
              }
            },
            {
              "fieldName": "tx",
              "value": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
                "name": "tx",
                "fields": [
                  {
                    "fieldName": "origin",
                    "value": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                    }
                  }
                ]
              }
            },
            {
              "fieldName": "block",
              "value": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
                "name": "block",
                "fields": [
                  {
                    "fieldName": "coinbase",
                    "value": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                    }
                  },
                  {
                    "fieldName": "difficulty",
                    "value": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "gaslimit",
                    "value": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "number",
                    "value": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "timestamp",
                    "value": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  }
                ]
              }
            }
          ]
        },
        "fields": [
          {
            "fieldName": "block",
            "value": {
              "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
              "name": "block",
              "fields": [
                {
                  "fieldName": "coinbase",
                  "value": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                  }
                },
                {
                  "fieldName": "difficulty",
                  "value": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 256
                  }
                },
                {
                  "fieldName": "gaslimit",
                  "value": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 256
                  }
                },
                {
                  "fieldName": "number",
                  "value": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 256
                  }
                },
                {
                  "fieldName": "timestamp",
                  "value": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 256
                  }
                }
              ]
            }
          },
          {
            "fieldName": "number",
            "value": {
              "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
              "k": 256
            }
          }
        ]
      }
    },
    {
      "key": {
        "name": "cvl.local",
        "type": "java.lang.Boolean",
        "erasureStrategy": "Canonical"
      },
      "value": true
    },
    {
      "key": {
        "name": "cvl.type",
        "type": "spec.cvlast.CVLType$PureCVLType",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
        "k": 256
      }
    },
    {
      "key": {
        "name": "cvl",
        "type": "java.lang.Boolean",
        "erasureStrategy": "Canonical"
      },
      "value": true
    },
    {
      "key": {
        "name": "cvl.display",
        "type": "java.lang.String",
        "erasureStrategy": "CallTrace"
      },
      "value": "invariantEnv.block.number"
    }
  ],
  "22": [
    {
      "key": {
        "name": "cvl.struct.path",
        "type": "spec.cvlast.CVLStructPathNode",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "rootStructType": {
          "name": "env",
          "fields": [
            {
              "fieldName": "msg",
              "value": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
                "name": "msg",
                "fields": [
                  {
                    "fieldName": "sender",
                    "value": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                    }
                  },
                  {
                    "fieldName": "value",
                    "value": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  }
                ]
              }
            },
            {
              "fieldName": "tx",
              "value": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
                "name": "tx",
                "fields": [
                  {
                    "fieldName": "origin",
                    "value": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                    }
                  }
                ]
              }
            },
            {
              "fieldName": "block",
              "value": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
                "name": "block",
                "fields": [
                  {
                    "fieldName": "coinbase",
                    "value": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                    }
                  },
                  {
                    "fieldName": "difficulty",
                    "value": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "gaslimit",
                    "value": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "number",
                    "value": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "timestamp",
                    "value": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  }
                ]
              }
            }
          ]
        },
        "fields": [
          {
            "fieldName": "block",
            "value": {
              "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
              "name": "block",
              "fields": [
                {
                  "fieldName": "coinbase",
                  "value": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                  }
                },
                {
                  "fieldName": "difficulty",
                  "value": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 256
                  }
                },
                {
                  "fieldName": "gaslimit",
                  "value": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 256
                  }
                },
                {
                  "fieldName": "number",
                  "value": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 256
                  }
                },
                {
                  "fieldName": "timestamp",
                  "value": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 256
                  }
                }
              ]
            }
          },
          {
            "fieldName": "timestamp",
            "value": {
              "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
              "k": 256
            }
          }
        ]
      }
    },
    {
      "key": {
        "name": "cvl.local",
        "type": "java.lang.Boolean",
        "erasureStrategy": "Canonical"
      },
      "value": true
    },
    {
      "key": {
        "name": "cvl.type",
        "type": "spec.cvlast.CVLType$PureCVLType",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
        "k": 256
      }
    },
    {
      "key": {
        "name": "cvl",
        "type": "java.lang.Boolean",
        "erasureStrategy": "Canonical"
      },
      "value": true
    },
    {
      "key": {
        "name": "cvl.display",
        "type": "java.lang.String",
        "erasureStrategy": "CallTrace"
      },
      "value": "invariantEnv.block.timestamp"
    }
  ],
  "23": [
    {
      "key": {
        "name": "tac.is-temp-var",
        "type": "tac.MetaMap$Companion$NothingValue",
        "erasureStrategy": "Canonical"
      },
      "value": {
      }
    }
  ],
  "24": [
    {
      "key": {
        "name": "cvl.range",
        "type": "spec.cvlast.CVLRange",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "spec.cvlast.CVLRange.Range",
        "specFile": "certora/spec/ERC20.spec",
        "start": {
          "line": 140
        },
        "end": {
          "line": 141,
          "character": 49
        }
      }
    }
  ],
  "25": [
    {
      "key": {
        "name": "Tac.symbol.keyword",
        "type": "java.lang.String",
        "erasureStrategy": "Canonical"
      },
      "value": "tacCalldatasize"
    }
  ],
  "26": [
    {
      "key": {
        "name": "Tac.symbol.keyword",
        "type": "java.lang.String",
        "erasureStrategy": "Canonical"
      },
      "value": "tacAddress"
    },
    {
      "key": {
        "name": "tac.env.known-bit-width",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 160
    },
    {
      "key": {
        "name": "tac.contract.sym.addr.name",
        "type": "java.lang.String",
        "erasureStrategy": "Erased"
      },
      "value": "ERC20"
    },
    {
      "key": {
        "name": "tac.contract.sym.addr",
        "type": "java.math.BigInteger",
        "erasureStrategy": "Erased"
      },
      "value": "ce4604a0000000000000000000000003"
    }
  ],
  "27": [
    {
      "key": {
        "name": "cvl.range",
        "type": "spec.cvlast.CVLRange",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "spec.cvlast.CVLRange.Range",
        "specFile": "certora/spec/ERC20.spec",
        "start": {
          "line": 140
        },
        "end": {
          "line": 141,
          "character": 49
        }
      }
    },
    {
      "key": {
        "name": "tac.meta",
        "type": "vc.data.TACMetaInfo",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "source": 0,
        "begin": 3906,
        "len": 364,
        "jumpType": "REGULAR",
        "address": "ce4604a0000000000000000000000003",
        "sourceContext": {
          "indexToFilepath": {
            "0": "contracts/ERC20.sol",
            "1": "contracts/IERC20.sol",
            "2": "contracts/IERC20Metadata.sol"
          },
          "sourceDir": ".post_autofinders.0"
        }
      }
    }
  ],
  "28": [
    {
      "key": {
        "name": "cvl.exp",
        "type": "spec.CVLExpToTACExprMeta",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "spec.CVLExpToTACExprMeta.BinaryCVLExp",
        "exp": {
          "#class": "spec.cvlast.CVLExp.RelopExp.EqExp",
          "l": {
            "#class": "spec.cvlast.CVLExp.CastExpr",
            "toCastType": {
              "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Mathint"
            },
            "arg": {
              "#class": "spec.cvlast.CVLExp.ApplyExp.ContractFunction.Concrete",
              "methodIdWithCallContext": {
                "#class": "spec.cvlast.ConcreteMethod",
                "signature": {
                  "#class": "spec.cvlast.ExternalQualifiedMethodSignature.ExternalQualifiedMethodSig",
                  "wrapped": {
                    "#class": "spec.cvlast.QualifiedMethodSignature.QualifiedMethodSig",
                    "qualifiedMethodName": {
                      "#class": "spec.cvlast.QualifiedFunction",
                      "host": {
                        "name": "ERC20"
                      },
                      "methodId": "totalSupply"
                    },
                    "params": [
                    ],
                    "res": [
                      {
                        "#class": "spec.cvlast.VMParam.Unnamed",
                        "vmType": {
                          "#class": "ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK",
                          "bitwidth": 256
                        }
                      }
                    ]
                  },
                  "sighashInt": {
                    "n": "18160ddd"
                  }
                }
              },
              "args": [
              ],
              "noRevert": true,
              "storage": {
                "#class": "spec.cvlast.CVLExp.VariableExp",
                "id": "lastStorage",
                "tag": {
                  "scope": {
                    "scopeStack": [
                      {
                        "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                      },
                      {
                        "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                        "scopeId": 23
                      }
                    ],
                    "innerScope": {
                      "scopeStack": [
                        {
                          "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                        }
                      ],
                      "innerScope": {
                        "scopeStack": [
                        ],
                        "innerScope": null
                      }
                    }
                  },
                  "type": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.VMInternal.BlockchainState"
                  },
                  "cvlRange": {
                    "#class": "spec.cvlast.CVLRange.Range",
                    "specFile": "certora/spec/ERC20.spec",
                    "start": {
                      "line": 140
                    },
                    "end": {
                      "line": 141,
                      "character": 49
                    }
                  }
                },
                "twoStateIndex": "NEITHER"
              },
              "isWhole": false,
              "tag": {
                "scope": {
                  "scopeStack": [
                    {
                      "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                    },
                    {
                      "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                      "scopeId": 23
                    }
                  ],
                  "innerScope": {
                    "scopeStack": [
                      {
                        "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                      }
                    ],
                    "innerScope": {
                      "scopeStack": [
                      ],
                      "innerScope": null
                    }
                  }
                },
                "type": {
                  "#class": "spec.cvlast.CVLType.VM",
                  "descriptor": {
                    "#class": "ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK",
                    "bitwidth": 256
                  },
                  "context": {
                    "#class": "spec.cvlast.typedescriptors.FromVMContext.ReturnValue"
                  }
                },
                "cvlRange": {
                  "#class": "spec.cvlast.CVLRange.Range",
                  "specFile": "certora/spec/ERC20.spec",
                  "start": {
                    "line": 141,
                    "character": 15
                  },
                  "end": {
                    "line": 141,
                    "character": 26
                  }
                },
                "annotation": {
                  "#class": "ReflectivePolymorphicSerializer::spec.cvlast.CallResolution$DirectPassing",
                  "target": {
                    "methodSignature": {
                      "#class": "spec.cvlast.ExternalQualifiedMethodSignature.ExternalQualifiedMethodSig",
                      "wrapped": {
                        "#class": "spec.cvlast.QualifiedMethodSignature.QualifiedMethodSig",
                        "qualifiedMethodName": {
                          "#class": "spec.cvlast.QualifiedFunction",
                          "host": {
                            "name": "ERC20"
                          },
                          "methodId": "totalSupply"
                        },
                        "params": [
                        ],
                        "res": [
                          {
                            "#class": "spec.cvlast.VMParam.Unnamed",
                            "vmType": {
                              "#class": "ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK",
                              "bitwidth": 256
                            }
                          }
                        ]
                      },
                      "sighashInt": {
                        "n": "18160ddd"
                      }
                    },
                    "definitelyNonPayable": true,
                    "annotation": {
                      "visibility": "EXTERNAL",
                      "envFree": true,
                      "library": false
                    },
                    "stateMutability": "view",
                    "tag": {
                      "#class": "spec.cvlast.CVLImportedFunctionTag.WithMethodInfo",
                      "evmMethodInfo": {
                        "sigHash": "18160ddd",
                        "name": "totalSupply",
                        "argTypes": [
                        ],
                        "resultTypes": [
                          {
                            "#class": "spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK",
                            "bitwidth": 256
                          }
                        ],
                        "stateMutability": "view",
                        "envfreeInfo": {
                          "#class": "bridge.EnvfreeInfo.Unknown"
                        },
                        "isConstant": false,
                        "isLibrary": false
                      }
                    }
                  },
                  "hasEnv": false
                }
              }
            },
            "tag": {
              "scope": {
                "scopeStack": [
                  {
                    "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                  },
                  {
                    "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                    "scopeId": 23
                  }
                ],
                "innerScope": {
                  "scopeStack": [
                    {
                      "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                    }
                  ],
                  "innerScope": {
                    "scopeStack": [
                    ],
                    "innerScope": null
                  }
                }
              },
              "type": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Mathint"
              },
              "cvlRange": {
                "#class": "spec.cvlast.CVLRange.Range",
                "specFile": "certora/spec/ERC20.spec",
                "start": {
                  "line": 141,
                  "character": 4
                },
                "end": {
                  "line": 141,
                  "character": 28
                }
              }
            },
            "castType": "TO"
          },
          "r": {
            "#class": "spec.cvlast.CVLExp.VariableExp",
            "id": "sum_of_balances",
            "tag": {
              "scope": {
                "scopeStack": [
                  {
                    "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                  },
                  {
                    "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                    "scopeId": 23
                  }
                ],
                "innerScope": {
                  "scopeStack": [
                    {
                      "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                    }
                  ],
                  "innerScope": {
                    "scopeStack": [
                    ],
                    "innerScope": null
                  }
                }
              },
              "type": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Mathint"
              },
              "cvlRange": {
                "#class": "spec.cvlast.CVLRange.Range",
                "specFile": "certora/spec/ERC20.spec",
                "start": {
                  "line": 140
                },
                "end": {
                  "line": 141,
                  "character": 49
                }
              }
            },
            "twoStateIndex": "NEITHER"
          },
          "tag": {
            "scope": {
              "scopeStack": [
                {
                  "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                },
                {
                  "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                  "scopeId": 23
                }
              ],
              "innerScope": {
                "scopeStack": [
                  {
                    "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                  }
                ],
                "innerScope": {
                  "scopeStack": [
                  ],
                  "innerScope": null
                }
              }
            },
            "type": {
              "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
            },
            "cvlRange": {
              "#class": "spec.cvlast.CVLRange.Range",
              "specFile": "certora/spec/ERC20.spec",
              "start": {
                "line": 141,
                "character": 4
              },
              "end": {
                "line": 141,
                "character": 48
              }
            }
          }
        },
        "o1": {
          "out": {
            "#class": "vc.data.TACSymbol.Var.Full",
            "namePrefix": "CANON29",
            "tag": {
              "#class": "tac.Tag.Int"
            },
            "callIndex": 0
          },
          "exp": {
            "#class": "spec.cvlast.CVLExp.CastExpr",
            "toCastType": {
              "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Mathint"
            },
            "arg": {
              "#class": "spec.cvlast.CVLExp.ApplyExp.ContractFunction.Concrete",
              "methodIdWithCallContext": {
                "#class": "spec.cvlast.ConcreteMethod",
                "signature": {
                  "#class": "spec.cvlast.ExternalQualifiedMethodSignature.ExternalQualifiedMethodSig",
                  "wrapped": {
                    "#class": "spec.cvlast.QualifiedMethodSignature.QualifiedMethodSig",
                    "qualifiedMethodName": {
                      "#class": "spec.cvlast.QualifiedFunction",
                      "host": {
                        "name": "ERC20"
                      },
                      "methodId": "totalSupply"
                    },
                    "params": [
                    ],
                    "res": [
                      {
                        "#class": "spec.cvlast.VMParam.Unnamed",
                        "vmType": {
                          "#class": "ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK",
                          "bitwidth": 256
                        }
                      }
                    ]
                  },
                  "sighashInt": {
                    "n": "18160ddd"
                  }
                }
              },
              "args": [
              ],
              "noRevert": true,
              "storage": {
                "#class": "spec.cvlast.CVLExp.VariableExp",
                "id": "lastStorage",
                "tag": {
                  "scope": {
                    "scopeStack": [
                      {
                        "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                      },
                      {
                        "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                        "scopeId": 23
                      }
                    ],
                    "innerScope": {
                      "scopeStack": [
                        {
                          "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                        }
                      ],
                      "innerScope": {
                        "scopeStack": [
                        ],
                        "innerScope": null
                      }
                    }
                  },
                  "type": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.VMInternal.BlockchainState"
                  },
                  "cvlRange": {
                    "#class": "spec.cvlast.CVLRange.Range",
                    "specFile": "certora/spec/ERC20.spec",
                    "start": {
                      "line": 140
                    },
                    "end": {
                      "line": 141,
                      "character": 49
                    }
                  }
                },
                "twoStateIndex": "NEITHER"
              },
              "isWhole": false,
              "tag": {
                "scope": {
                  "scopeStack": [
                    {
                      "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                    },
                    {
                      "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                      "scopeId": 23
                    }
                  ],
                  "innerScope": {
                    "scopeStack": [
                      {
                        "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                      }
                    ],
                    "innerScope": {
                      "scopeStack": [
                      ],
                      "innerScope": null
                    }
                  }
                },
                "type": {
                  "#class": "spec.cvlast.CVLType.VM",
                  "descriptor": {
                    "#class": "ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK",
                    "bitwidth": 256
                  },
                  "context": {
                    "#class": "spec.cvlast.typedescriptors.FromVMContext.ReturnValue"
                  }
                },
                "cvlRange": {
                  "#class": "spec.cvlast.CVLRange.Range",
                  "specFile": "certora/spec/ERC20.spec",
                  "start": {
                    "line": 141,
                    "character": 15
                  },
                  "end": {
                    "line": 141,
                    "character": 26
                  }
                },
                "annotation": {
                  "#class": "ReflectivePolymorphicSerializer::spec.cvlast.CallResolution$DirectPassing",
                  "target": {
                    "methodSignature": {
                      "#class": "spec.cvlast.ExternalQualifiedMethodSignature.ExternalQualifiedMethodSig",
                      "wrapped": {
                        "#class": "spec.cvlast.QualifiedMethodSignature.QualifiedMethodSig",
                        "qualifiedMethodName": {
                          "#class": "spec.cvlast.QualifiedFunction",
                          "host": {
                            "name": "ERC20"
                          },
                          "methodId": "totalSupply"
                        },
                        "params": [
                        ],
                        "res": [
                          {
                            "#class": "spec.cvlast.VMParam.Unnamed",
                            "vmType": {
                              "#class": "ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK",
                              "bitwidth": 256
                            }
                          }
                        ]
                      },
                      "sighashInt": {
                        "n": "18160ddd"
                      }
                    },
                    "definitelyNonPayable": true,
                    "annotation": {
                      "visibility": "EXTERNAL",
                      "envFree": true,
                      "library": false
                    },
                    "stateMutability": "view",
                    "tag": {
                      "#class": "spec.cvlast.CVLImportedFunctionTag.WithMethodInfo",
                      "evmMethodInfo": {
                        "sigHash": "18160ddd",
                        "name": "totalSupply",
                        "argTypes": [
                        ],
                        "resultTypes": [
                          {
                            "#class": "spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK",
                            "bitwidth": 256
                          }
                        ],
                        "stateMutability": "view",
                        "envfreeInfo": {
                          "#class": "bridge.EnvfreeInfo.Unknown"
                        },
                        "isConstant": false,
                        "isLibrary": false
                      }
                    }
                  },
                  "hasEnv": false
                }
              }
            },
            "tag": {
              "scope": {
                "scopeStack": [
                  {
                    "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                  },
                  {
                    "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                    "scopeId": 23
                  }
                ],
                "innerScope": {
                  "scopeStack": [
                    {
                      "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                    }
                  ],
                  "innerScope": {
                    "scopeStack": [
                    ],
                    "innerScope": null
                  }
                }
              },
              "type": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Mathint"
              },
              "cvlRange": {
                "#class": "spec.cvlast.CVLRange.Range",
                "specFile": "certora/spec/ERC20.spec",
                "start": {
                  "line": 141,
                  "character": 4
                },
                "end": {
                  "line": 141,
                  "character": 28
                }
              }
            },
            "castType": "TO"
          }
        },
        "o2": {
          "out": {
            "#class": "vc.data.TACSymbol.Var.Full",
            "namePrefix": "I4",
            "tag": {
              "#class": "tac.Tag.Int"
            },
            "callIndex": 0
          },
          "exp": {
            "#class": "spec.cvlast.CVLExp.VariableExp",
            "id": "sum_of_balances",
            "tag": {
              "scope": {
                "scopeStack": [
                  {
                    "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                  },
                  {
                    "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                    "scopeId": 23
                  }
                ],
                "innerScope": {
                  "scopeStack": [
                    {
                      "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                    }
                  ],
                  "innerScope": {
                    "scopeStack": [
                    ],
                    "innerScope": null
                  }
                }
              },
              "type": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Mathint"
              },
              "cvlRange": {
                "#class": "spec.cvlast.CVLRange.Range",
                "specFile": "certora/spec/ERC20.spec",
                "start": {
                  "line": 140
                },
                "end": {
                  "line": 141,
                  "character": 49
                }
              }
            },
            "twoStateIndex": "NEITHER"
          }
        }
      }
    },
    {
      "key": {
        "name": "cvl.range",
        "type": "spec.cvlast.CVLRange",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "spec.cvlast.CVLRange.Range",
        "specFile": "certora/spec/ERC20.spec",
        "start": {
          "line": 140
        },
        "end": {
          "line": 141,
          "character": 49
        }
      }
    }
  ],
  "29": [
    {
      "key": {
        "name": "cvl",
        "type": "java.lang.Boolean",
        "erasureStrategy": "Canonical"
      },
      "value": true
    }
  ],
  "30": [
    {
      "key": {
        "name": "tac.scalarization.sort",
        "type": "vc.data.ScalarizationSort",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.ScalarizationSort.Split",
        "idx": "2"
      }
    },
    {
      "key": {
        "name": "Tac.symbol.keyword",
        "type": "java.lang.String",
        "erasureStrategy": "Canonical"
      },
      "value": "L"
    },
    {
      "key": {
        "name": "tac.storage.bit-width",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 256
    },
    {
      "key": {
        "name": "tac.storage.pretty.paths",
        "type": "analysis.storage.DisplayPaths",
        "erasureStrategy": "Erased"
      },
      "value": {
        "paths": [
          {
            "#class": "analysis.storage.DisplayPath.Root",
            "name": "_totalSupply"
          }
        ]
      }
    },
    {
      "key": {
        "name": "tac.slot.type",
        "type": "spec.cvlast.typedescriptors.EVMTypeDescriptor$EVMValueType",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK",
        "bitwidth": 256
      }
    },
    {
      "key": {
        "name": "tac.storage.non-indexed-path",
        "type": "analysis.storage.StorageAnalysisResult$NonIndexedPath",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "analysis.storage.StorageAnalysisResult.NonIndexedPath.Root",
        "slot": "2"
      }
    },
    {
      "key": {
        "name": "tac.storage",
        "type": "java.math.BigInteger",
        "erasureStrategy": "Canonical"
      },
      "value": "ce4604a0000000000000000000000003"
    },
    {
      "key": {
        "name": "tac.stack.height",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 1023
    }
  ],
  "31": [
    {
      "key": {
        "name": "cvl.local",
        "type": "java.lang.Boolean",
        "erasureStrategy": "Canonical"
      },
      "value": false
    }
  ],
  "32": [
    {
      "key": {
        "name": "cvl.local",
        "type": "java.lang.Boolean",
        "erasureStrategy": "Canonical"
      },
      "value": false
    },
    {
      "key": {
        "name": "Tac.symbol.keyword",
        "type": "java.lang.String",
        "erasureStrategy": "Canonical"
      },
      "value": "tacCalldatasize"
    }
  ],
  "33": [
    {
      "key": {
        "name": "tac.immutable.array",
        "type": "vc.data.ImmutableBound",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "sym": {
          "#class": "vc.data.TACSymbol.Var.Full",
          "namePrefix": "tacCalldatasize",
          "tag": {
            "#class": "tac.Tag.Bit256"
          },
          "callIndex": 0,
          "meta": [
            {
              "key": {
                "name": "Tac.symbol.keyword",
                "type": "java.lang.String",
                "erasureStrategy": "Canonical"
              },
              "value": "tacCalldatasize"
            }
          ]
        }
      }
    },
    {
      "key": {
        "name": "tac.wordmap-key",
        "type": "java.math.BigInteger",
        "erasureStrategy": "Canonical"
      },
      "value": "4"
    },
    {
      "key": {
        "name": "tac.scalarization.sort",
        "type": "vc.data.ScalarizationSort",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.ScalarizationSort.Split",
        "idx": "4"
      }
    },
    {
      "key": {
        "name": "Tac.symbol.keyword",
        "type": "java.lang.String",
        "erasureStrategy": "Canonical"
      },
      "value": "tacCalldatabuf"
    },
    {
      "key": {
        "name": "tac.storage.bit-width",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 256
    },
    {
      "key": {
        "name": "tac.calldata.offset",
        "type": "java.math.BigInteger",
        "erasureStrategy": "Canonical"
      },
      "value": "4"
    },
    {
      "key": {
        "name": "tac.is.calldata",
        "type": "tac.MetaMap$Companion$NothingValue",
        "erasureStrategy": "Canonical"
      },
      "value": {
      }
    }
  ],
  "34": [
    {
      "key": {
        "name": "tac.immutable.array",
        "type": "vc.data.ImmutableBound",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "sym": {
          "#class": "vc.data.TACSymbol.Var.Full",
          "namePrefix": "tacCalldatasize",
          "tag": {
            "#class": "tac.Tag.Bit256"
          },
          "callIndex": 0,
          "meta": [
            {
              "key": {
                "name": "Tac.symbol.keyword",
                "type": "java.lang.String",
                "erasureStrategy": "Canonical"
              },
              "value": "tacCalldatasize"
            }
          ]
        }
      }
    },
    {
      "key": {
        "name": "tac.wordmap-key",
        "type": "java.math.BigInteger",
        "erasureStrategy": "Canonical"
      },
      "value": "24"
    },
    {
      "key": {
        "name": "tac.scalarization.sort",
        "type": "vc.data.ScalarizationSort",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.ScalarizationSort.Split",
        "idx": "24"
      }
    },
    {
      "key": {
        "name": "Tac.symbol.keyword",
        "type": "java.lang.String",
        "erasureStrategy": "Canonical"
      },
      "value": "tacCalldatabuf"
    },
    {
      "key": {
        "name": "tac.storage.bit-width",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 256
    },
    {
      "key": {
        "name": "tac.calldata.offset",
        "type": "java.math.BigInteger",
        "erasureStrategy": "Canonical"
      },
      "value": "24"
    },
    {
      "key": {
        "name": "tac.is.calldata",
        "type": "tac.MetaMap$Companion$NothingValue",
        "erasureStrategy": "Canonical"
      },
      "value": {
      }
    }
  ],
  "35": [
    {
      "key": {
        "name": "tac.immutable.array",
        "type": "vc.data.ImmutableBound",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "sym": {
          "#class": "vc.data.TACSymbol.Var.Full",
          "namePrefix": "tacCalldatasize",
          "tag": {
            "#class": "tac.Tag.Bit256"
          },
          "callIndex": 0,
          "meta": [
            {
              "key": {
                "name": "Tac.symbol.keyword",
                "type": "java.lang.String",
                "erasureStrategy": "Canonical"
              },
              "value": "tacCalldatasize"
            }
          ]
        }
      }
    },
    {
      "key": {
        "name": "tac.wordmap-key",
        "type": "java.math.BigInteger",
        "erasureStrategy": "Canonical"
      },
      "value": "44"
    },
    {
      "key": {
        "name": "tac.scalarization.sort",
        "type": "vc.data.ScalarizationSort",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.ScalarizationSort.Split",
        "idx": "44"
      }
    },
    {
      "key": {
        "name": "Tac.symbol.keyword",
        "type": "java.lang.String",
        "erasureStrategy": "Canonical"
      },
      "value": "tacCalldatabuf"
    },
    {
      "key": {
        "name": "tac.storage.bit-width",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 256
    },
    {
      "key": {
        "name": "tac.calldata.offset",
        "type": "java.math.BigInteger",
        "erasureStrategy": "Canonical"
      },
      "value": "44"
    },
    {
      "key": {
        "name": "tac.is.calldata",
        "type": "tac.MetaMap$Companion$NothingValue",
        "erasureStrategy": "Canonical"
      },
      "value": {
      }
    }
  ],
  "36": [
    {
      "key": {
        "name": "Tac.symbol.keyword",
        "type": "java.lang.String",
        "erasureStrategy": "Canonical"
      },
      "value": "tacCaller"
    },
    {
      "key": {
        "name": "tac.env.known-bit-width",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 160
    },
    {
      "key": {
        "name": "tac.is-temp-var",
        "type": "tac.MetaMap$Companion$NothingValue",
        "erasureStrategy": "Canonical"
      },
      "value": {
      }
    }
  ],
  "37": [
    {
      "key": {
        "name": "Tac.symbol.keyword",
        "type": "java.lang.String",
        "erasureStrategy": "Canonical"
      },
      "value": "tacCallvalue"
    },
    {
      "key": {
        "name": "tac.is-temp-var",
        "type": "tac.MetaMap$Companion$NothingValue",
        "erasureStrategy": "Canonical"
      },
      "value": {
      }
    }
  ],
  "38": [
    {
      "key": {
        "name": "Tac.symbol.keyword",
        "type": "java.lang.String",
        "erasureStrategy": "Canonical"
      },
      "value": "tacOrigin"
    },
    {
      "key": {
        "name": "tac.env.known-bit-width",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 160
    },
    {
      "key": {
        "name": "tac.is-temp-var",
        "type": "tac.MetaMap$Companion$NothingValue",
        "erasureStrategy": "Canonical"
      },
      "value": {
      }
    }
  ],
  "39": [
    {
      "key": {
        "name": "Tac.symbol.keyword",
        "type": "java.lang.String",
        "erasureStrategy": "Canonical"
      },
      "value": "tacNumber"
    },
    {
      "key": {
        "name": "tac.is-temp-var",
        "type": "tac.MetaMap$Companion$NothingValue",
        "erasureStrategy": "Canonical"
      },
      "value": {
      }
    }
  ],
  "40": [
    {
      "key": {
        "name": "Tac.symbol.keyword",
        "type": "java.lang.String",
        "erasureStrategy": "Canonical"
      },
      "value": "tacTimestamp"
    },
    {
      "key": {
        "name": "tac.is-temp-var",
        "type": "tac.MetaMap$Companion$NothingValue",
        "erasureStrategy": "Canonical"
      },
      "value": {
      }
    }
  ],
  "41": [
    {
      "key": {
        "name": "tac.transfers.balance",
        "type": "tac.MetaMap$Companion$NothingValue",
        "erasureStrategy": "Canonical"
      },
      "value": {
      }
    },
    {
      "key": {
        "name": "cvl.range",
        "type": "spec.cvlast.CVLRange",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "spec.cvlast.CVLRange.Range",
        "specFile": "certora/spec/ERC20.spec",
        "start": {
          "line": 140
        },
        "end": {
          "line": 141,
          "character": 49
        }
      }
    }
  ],
  "42": [
    {
      "key": {
        "name": "cvl.exp",
        "type": "spec.CVLExpToTACExprMeta",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "spec.CVLExpToTACExprMeta.BinaryCVLExp",
        "exp": {
          "#class": "spec.cvlast.CVLExp.RelopExp.EqExp",
          "l": {
            "#class": "spec.cvlast.CVLExp.CastExpr",
            "toCastType": {
              "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Mathint"
            },
            "arg": {
              "#class": "spec.cvlast.CVLExp.ApplyExp.ContractFunction.Concrete",
              "methodIdWithCallContext": {
                "#class": "spec.cvlast.ConcreteMethod",
                "signature": {
                  "#class": "spec.cvlast.ExternalQualifiedMethodSignature.ExternalQualifiedMethodSig",
                  "wrapped": {
                    "#class": "spec.cvlast.QualifiedMethodSignature.QualifiedMethodSig",
                    "qualifiedMethodName": {
                      "#class": "spec.cvlast.QualifiedFunction",
                      "host": {
                        "name": "ERC20"
                      },
                      "methodId": "totalSupply"
                    },
                    "params": [
                    ],
                    "res": [
                      {
                        "#class": "spec.cvlast.VMParam.Unnamed",
                        "vmType": {
                          "#class": "ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK",
                          "bitwidth": 256
                        }
                      }
                    ]
                  },
                  "sighashInt": {
                    "n": "18160ddd"
                  }
                }
              },
              "args": [
              ],
              "noRevert": true,
              "storage": {
                "#class": "spec.cvlast.CVLExp.VariableExp",
                "id": "lastStorage",
                "tag": {
                  "scope": {
                    "scopeStack": [
                      {
                        "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                      },
                      {
                        "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                        "scopeId": 23
                      }
                    ],
                    "innerScope": {
                      "scopeStack": [
                        {
                          "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                        }
                      ],
                      "innerScope": {
                        "scopeStack": [
                        ],
                        "innerScope": null
                      }
                    }
                  },
                  "type": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.VMInternal.BlockchainState"
                  },
                  "cvlRange": {
                    "#class": "spec.cvlast.CVLRange.Range",
                    "specFile": "certora/spec/ERC20.spec",
                    "start": {
                      "line": 140
                    },
                    "end": {
                      "line": 141,
                      "character": 49
                    }
                  }
                },
                "twoStateIndex": "NEITHER"
              },
              "isWhole": false,
              "tag": {
                "scope": {
                  "scopeStack": [
                    {
                      "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                    },
                    {
                      "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                      "scopeId": 23
                    }
                  ],
                  "innerScope": {
                    "scopeStack": [
                      {
                        "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                      }
                    ],
                    "innerScope": {
                      "scopeStack": [
                      ],
                      "innerScope": null
                    }
                  }
                },
                "type": {
                  "#class": "spec.cvlast.CVLType.VM",
                  "descriptor": {
                    "#class": "ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK",
                    "bitwidth": 256
                  },
                  "context": {
                    "#class": "spec.cvlast.typedescriptors.FromVMContext.ReturnValue"
                  }
                },
                "cvlRange": {
                  "#class": "spec.cvlast.CVLRange.Range",
                  "specFile": "certora/spec/ERC20.spec",
                  "start": {
                    "line": 141,
                    "character": 15
                  },
                  "end": {
                    "line": 141,
                    "character": 26
                  }
                },
                "annotation": {
                  "#class": "ReflectivePolymorphicSerializer::spec.cvlast.CallResolution$DirectPassing",
                  "target": {
                    "methodSignature": {
                      "#class": "spec.cvlast.ExternalQualifiedMethodSignature.ExternalQualifiedMethodSig",
                      "wrapped": {
                        "#class": "spec.cvlast.QualifiedMethodSignature.QualifiedMethodSig",
                        "qualifiedMethodName": {
                          "#class": "spec.cvlast.QualifiedFunction",
                          "host": {
                            "name": "ERC20"
                          },
                          "methodId": "totalSupply"
                        },
                        "params": [
                        ],
                        "res": [
                          {
                            "#class": "spec.cvlast.VMParam.Unnamed",
                            "vmType": {
                              "#class": "ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK",
                              "bitwidth": 256
                            }
                          }
                        ]
                      },
                      "sighashInt": {
                        "n": "18160ddd"
                      }
                    },
                    "definitelyNonPayable": true,
                    "annotation": {
                      "visibility": "EXTERNAL",
                      "envFree": true,
                      "library": false
                    },
                    "stateMutability": "view",
                    "tag": {
                      "#class": "spec.cvlast.CVLImportedFunctionTag.WithMethodInfo",
                      "evmMethodInfo": {
                        "sigHash": "18160ddd",
                        "name": "totalSupply",
                        "argTypes": [
                        ],
                        "resultTypes": [
                          {
                            "#class": "spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK",
                            "bitwidth": 256
                          }
                        ],
                        "stateMutability": "view",
                        "envfreeInfo": {
                          "#class": "bridge.EnvfreeInfo.Unknown"
                        },
                        "isConstant": false,
                        "isLibrary": false
                      }
                    }
                  },
                  "hasEnv": false
                }
              }
            },
            "tag": {
              "scope": {
                "scopeStack": [
                  {
                    "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                  },
                  {
                    "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                    "scopeId": 23
                  }
                ],
                "innerScope": {
                  "scopeStack": [
                    {
                      "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                    }
                  ],
                  "innerScope": {
                    "scopeStack": [
                    ],
                    "innerScope": null
                  }
                }
              },
              "type": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Mathint"
              },
              "cvlRange": {
                "#class": "spec.cvlast.CVLRange.Range",
                "specFile": "certora/spec/ERC20.spec",
                "start": {
                  "line": 141,
                  "character": 4
                },
                "end": {
                  "line": 141,
                  "character": 28
                }
              }
            },
            "castType": "TO"
          },
          "r": {
            "#class": "spec.cvlast.CVLExp.VariableExp",
            "id": "sum_of_balances",
            "tag": {
              "scope": {
                "scopeStack": [
                  {
                    "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                  },
                  {
                    "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                    "scopeId": 23
                  }
                ],
                "innerScope": {
                  "scopeStack": [
                    {
                      "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                    }
                  ],
                  "innerScope": {
                    "scopeStack": [
                    ],
                    "innerScope": null
                  }
                }
              },
              "type": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Mathint"
              },
              "cvlRange": {
                "#class": "spec.cvlast.CVLRange.Range",
                "specFile": "certora/spec/ERC20.spec",
                "start": {
                  "line": 140
                },
                "end": {
                  "line": 141,
                  "character": 49
                }
              }
            },
            "twoStateIndex": "NEITHER"
          },
          "tag": {
            "scope": {
              "scopeStack": [
                {
                  "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                },
                {
                  "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                  "scopeId": 23
                }
              ],
              "innerScope": {
                "scopeStack": [
                  {
                    "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                  }
                ],
                "innerScope": {
                  "scopeStack": [
                  ],
                  "innerScope": null
                }
              }
            },
            "type": {
              "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
            },
            "cvlRange": {
              "#class": "spec.cvlast.CVLRange.Range",
              "specFile": "certora/spec/ERC20.spec",
              "start": {
                "line": 141,
                "character": 4
              },
              "end": {
                "line": 141,
                "character": 48
              }
            }
          }
        },
        "o1": {
          "out": {
            "#class": "vc.data.TACSymbol.Var.Full",
            "namePrefix": "CANON105",
            "tag": {
              "#class": "tac.Tag.Int"
            },
            "callIndex": 0
          },
          "exp": {
            "#class": "spec.cvlast.CVLExp.CastExpr",
            "toCastType": {
              "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Mathint"
            },
            "arg": {
              "#class": "spec.cvlast.CVLExp.ApplyExp.ContractFunction.Concrete",
              "methodIdWithCallContext": {
                "#class": "spec.cvlast.ConcreteMethod",
                "signature": {
                  "#class": "spec.cvlast.ExternalQualifiedMethodSignature.ExternalQualifiedMethodSig",
                  "wrapped": {
                    "#class": "spec.cvlast.QualifiedMethodSignature.QualifiedMethodSig",
                    "qualifiedMethodName": {
                      "#class": "spec.cvlast.QualifiedFunction",
                      "host": {
                        "name": "ERC20"
                      },
                      "methodId": "totalSupply"
                    },
                    "params": [
                    ],
                    "res": [
                      {
                        "#class": "spec.cvlast.VMParam.Unnamed",
                        "vmType": {
                          "#class": "ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK",
                          "bitwidth": 256
                        }
                      }
                    ]
                  },
                  "sighashInt": {
                    "n": "18160ddd"
                  }
                }
              },
              "args": [
              ],
              "noRevert": true,
              "storage": {
                "#class": "spec.cvlast.CVLExp.VariableExp",
                "id": "lastStorage",
                "tag": {
                  "scope": {
                    "scopeStack": [
                      {
                        "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                      },
                      {
                        "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                        "scopeId": 23
                      }
                    ],
                    "innerScope": {
                      "scopeStack": [
                        {
                          "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                        }
                      ],
                      "innerScope": {
                        "scopeStack": [
                        ],
                        "innerScope": null
                      }
                    }
                  },
                  "type": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.VMInternal.BlockchainState"
                  },
                  "cvlRange": {
                    "#class": "spec.cvlast.CVLRange.Range",
                    "specFile": "certora/spec/ERC20.spec",
                    "start": {
                      "line": 140
                    },
                    "end": {
                      "line": 141,
                      "character": 49
                    }
                  }
                },
                "twoStateIndex": "NEITHER"
              },
              "isWhole": false,
              "tag": {
                "scope": {
                  "scopeStack": [
                    {
                      "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                    },
                    {
                      "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                      "scopeId": 23
                    }
                  ],
                  "innerScope": {
                    "scopeStack": [
                      {
                        "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                      }
                    ],
                    "innerScope": {
                      "scopeStack": [
                      ],
                      "innerScope": null
                    }
                  }
                },
                "type": {
                  "#class": "spec.cvlast.CVLType.VM",
                  "descriptor": {
                    "#class": "ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK",
                    "bitwidth": 256
                  },
                  "context": {
                    "#class": "spec.cvlast.typedescriptors.FromVMContext.ReturnValue"
                  }
                },
                "cvlRange": {
                  "#class": "spec.cvlast.CVLRange.Range",
                  "specFile": "certora/spec/ERC20.spec",
                  "start": {
                    "line": 141,
                    "character": 15
                  },
                  "end": {
                    "line": 141,
                    "character": 26
                  }
                },
                "annotation": {
                  "#class": "ReflectivePolymorphicSerializer::spec.cvlast.CallResolution$DirectPassing",
                  "target": {
                    "methodSignature": {
                      "#class": "spec.cvlast.ExternalQualifiedMethodSignature.ExternalQualifiedMethodSig",
                      "wrapped": {
                        "#class": "spec.cvlast.QualifiedMethodSignature.QualifiedMethodSig",
                        "qualifiedMethodName": {
                          "#class": "spec.cvlast.QualifiedFunction",
                          "host": {
                            "name": "ERC20"
                          },
                          "methodId": "totalSupply"
                        },
                        "params": [
                        ],
                        "res": [
                          {
                            "#class": "spec.cvlast.VMParam.Unnamed",
                            "vmType": {
                              "#class": "ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK",
                              "bitwidth": 256
                            }
                          }
                        ]
                      },
                      "sighashInt": {
                        "n": "18160ddd"
                      }
                    },
                    "definitelyNonPayable": true,
                    "annotation": {
                      "visibility": "EXTERNAL",
                      "envFree": true,
                      "library": false
                    },
                    "stateMutability": "view",
                    "tag": {
                      "#class": "spec.cvlast.CVLImportedFunctionTag.WithMethodInfo",
                      "evmMethodInfo": {
                        "sigHash": "18160ddd",
                        "name": "totalSupply",
                        "argTypes": [
                        ],
                        "resultTypes": [
                          {
                            "#class": "spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK",
                            "bitwidth": 256
                          }
                        ],
                        "stateMutability": "view",
                        "envfreeInfo": {
                          "#class": "bridge.EnvfreeInfo.Unknown"
                        },
                        "isConstant": false,
                        "isLibrary": false
                      }
                    }
                  },
                  "hasEnv": false
                }
              }
            },
            "tag": {
              "scope": {
                "scopeStack": [
                  {
                    "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                  },
                  {
                    "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                    "scopeId": 23
                  }
                ],
                "innerScope": {
                  "scopeStack": [
                    {
                      "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                    }
                  ],
                  "innerScope": {
                    "scopeStack": [
                    ],
                    "innerScope": null
                  }
                }
              },
              "type": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Mathint"
              },
              "cvlRange": {
                "#class": "spec.cvlast.CVLRange.Range",
                "specFile": "certora/spec/ERC20.spec",
                "start": {
                  "line": 141,
                  "character": 4
                },
                "end": {
                  "line": 141,
                  "character": 28
                }
              }
            },
            "castType": "TO"
          }
        },
        "o2": {
          "out": {
            "#class": "vc.data.TACSymbol.Var.Full",
            "namePrefix": "I183",
            "tag": {
              "#class": "tac.Tag.Int"
            },
            "callIndex": 0
          },
          "exp": {
            "#class": "spec.cvlast.CVLExp.VariableExp",
            "id": "sum_of_balances",
            "tag": {
              "scope": {
                "scopeStack": [
                  {
                    "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                  },
                  {
                    "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                    "scopeId": 23
                  }
                ],
                "innerScope": {
                  "scopeStack": [
                    {
                      "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                    }
                  ],
                  "innerScope": {
                    "scopeStack": [
                    ],
                    "innerScope": null
                  }
                }
              },
              "type": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Mathint"
              },
              "cvlRange": {
                "#class": "spec.cvlast.CVLRange.Range",
                "specFile": "certora/spec/ERC20.spec",
                "start": {
                  "line": 140
                },
                "end": {
                  "line": 141,
                  "character": 49
                }
              }
            },
            "twoStateIndex": "NEITHER"
          }
        }
      }
    },
    {
      "key": {
        "name": "cvl.range",
        "type": "spec.cvlast.CVLRange",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "spec.cvlast.CVLRange.Range",
        "specFile": "certora/spec/ERC20.spec",
        "start": {
          "line": 140
        },
        "end": {
          "line": 141,
          "character": 49
        }
      }
    }
  ],
  "43": [
    {
      "key": {
        "name": "cvl.user.defined.assert",
        "type": "tac.MetaMap$Companion$NothingValue",
        "erasureStrategy": "Canonical"
      },
      "value": {
      }
    },
    {
      "key": {
        "name": "cvl.range",
        "type": "spec.cvlast.CVLRange",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "spec.cvlast.CVLRange.Range",
        "specFile": "certora/spec/ERC20.spec",
        "start": {
          "line": 140
        },
        "end": {
          "line": 141,
          "character": 49
        }
      }
    }
  ],
  "44": [
    {
      "key": {
        "name": "tac.meta",
        "type": "vc.data.TACMetaInfo",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "source": 3,
        "begin": 1095,
        "len": 23,
        "jumpType": "REGULAR",
        "address": "ce4604a0000000000000000000000003",
        "sourceContext": {
          "indexToFilepath": {
            "0": "contracts/ERC20.sol",
            "1": "contracts/IERC20.sol",
            "2": "contracts/IERC20Metadata.sol"
          },
          "sourceDir": ".post_autofinders.0"
        }
      }
    },
    {
      "key": {
        "name": "optimization.overflow.safe",
        "type": "tac.MetaMap$Companion$NothingValue",
        "erasureStrategy": "Canonical"
      },
      "value": {
      }
    }
  ],
  "45": [
    {
      "key": {
        "name": "Tac.symbol.keyword",
        "type": "java.lang.String",
        "erasureStrategy": "Canonical"
      },
      "value": "L"
    },
    {
      "key": {
        "name": "tac.stack.height",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 1015
    }
  ],
  "46": [
    {
      "key": {
        "name": "tac.meta",
        "type": "vc.data.TACMetaInfo",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "source": 3,
        "begin": 78,
        "len": 20,
        "jumpType": "REGULAR",
        "address": "ce4604a0000000000000000000000003",
        "sourceContext": {
          "indexToFilepath": {
            "0": "contracts/ERC20.sol",
            "1": "contracts/IERC20.sol",
            "2": "contracts/IERC20Metadata.sol"
          },
          "sourceDir": ".post_autofinders.0"
        }
      }
    }
  ],
  "47": [
    {
      "key": {
        "name": "Tac.symbol.keyword",
        "type": "java.lang.String",
        "erasureStrategy": "Canonical"
      },
      "value": "L"
    },
    {
      "key": {
        "name": "tac.stack.height",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 1011
    }
  ],
  "48": [
    {
      "key": {
        "name": "tac.immutable.array",
        "type": "vc.data.ImmutableBound",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "sym": {
          "#class": "vc.data.TACSymbol.Var.Full",
          "namePrefix": "tacCalldatasize",
          "tag": {
            "#class": "tac.Tag.Bit256"
          },
          "callIndex": 2,
          "meta": [
            {
              "key": {
                "name": "Tac.symbol.keyword",
                "type": "java.lang.String",
                "erasureStrategy": "Canonical"
              },
              "value": "tacCalldatasize"
            }
          ]
        }
      }
    },
    {
      "key": {
        "name": "tac.wordmap-key",
        "type": "java.math.BigInteger",
        "erasureStrategy": "Canonical"
      },
      "value": "4"
    },
    {
      "key": {
        "name": "tac.scalarization.sort",
        "type": "vc.data.ScalarizationSort",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.ScalarizationSort.Split",
        "idx": "4"
      }
    },
    {
      "key": {
        "name": "Tac.symbol.keyword",
        "type": "java.lang.String",
        "erasureStrategy": "Canonical"
      },
      "value": "tacCalldatabuf"
    },
    {
      "key": {
        "name": "tac.storage.bit-width",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 256
    },
    {
      "key": {
        "name": "tac.calldata.offset",
        "type": "java.math.BigInteger",
        "erasureStrategy": "Canonical"
      },
      "value": "4"
    },
    {
      "key": {
        "name": "tac.is.calldata",
        "type": "tac.MetaMap$Companion$NothingValue",
        "erasureStrategy": "Canonical"
      },
      "value": {
      }
    }
  ],
  "49": [
    {
      "key": {
        "name": "tac.immutable.array",
        "type": "vc.data.ImmutableBound",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "sym": {
          "#class": "vc.data.TACSymbol.Var.Full",
          "namePrefix": "tacCalldatasize",
          "tag": {
            "#class": "tac.Tag.Bit256"
          },
          "callIndex": 2,
          "meta": [
            {
              "key": {
                "name": "Tac.symbol.keyword",
                "type": "java.lang.String",
                "erasureStrategy": "Canonical"
              },
              "value": "tacCalldatasize"
            }
          ]
        }
      }
    },
    {
      "key": {
        "name": "tac.wordmap-key",
        "type": "java.math.BigInteger",
        "erasureStrategy": "Canonical"
      },
      "value": "24"
    },
    {
      "key": {
        "name": "tac.scalarization.sort",
        "type": "vc.data.ScalarizationSort",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.ScalarizationSort.Split",
        "idx": "24"
      }
    },
    {
      "key": {
        "name": "Tac.symbol.keyword",
        "type": "java.lang.String",
        "erasureStrategy": "Canonical"
      },
      "value": "tacCalldatabuf"
    },
    {
      "key": {
        "name": "tac.storage.bit-width",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 256
    },
    {
      "key": {
        "name": "tac.calldata.offset",
        "type": "java.math.BigInteger",
        "erasureStrategy": "Canonical"
      },
      "value": "24"
    },
    {
      "key": {
        "name": "tac.is.calldata",
        "type": "tac.MetaMap$Companion$NothingValue",
        "erasureStrategy": "Canonical"
      },
      "value": {
      }
    }
  ],
  "50": [
    {
      "key": {
        "name": "tac.meta",
        "type": "vc.data.TACMetaInfo",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "source": 3,
        "begin": 223,
        "len": 20,
        "jumpType": "REGULAR",
        "address": "ce4604a0000000000000000000000003",
        "sourceContext": {
          "indexToFilepath": {
            "0": "contracts/ERC20.sol",
            "1": "contracts/IERC20.sol",
            "2": "contracts/IERC20Metadata.sol"
          },
          "sourceDir": ".post_autofinders.0"
        }
      }
    }
  ],
  "51": [
    {
      "key": {
        "name": "tac.immutable.array",
        "type": "vc.data.ImmutableBound",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "sym": {
          "#class": "vc.data.TACSymbol.Var.Full",
          "namePrefix": "tacCalldatasize",
          "tag": {
            "#class": "tac.Tag.Bit256"
          },
          "callIndex": 2,
          "meta": [
            {
              "key": {
                "name": "Tac.symbol.keyword",
                "type": "java.lang.String",
                "erasureStrategy": "Canonical"
              },
              "value": "tacCalldatasize"
            }
          ]
        }
      }
    },
    {
      "key": {
        "name": "tac.wordmap-key",
        "type": "java.math.BigInteger",
        "erasureStrategy": "Canonical"
      },
      "value": "44"
    },
    {
      "key": {
        "name": "tac.scalarization.sort",
        "type": "vc.data.ScalarizationSort",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.ScalarizationSort.Split",
        "idx": "44"
      }
    },
    {
      "key": {
        "name": "Tac.symbol.keyword",
        "type": "java.lang.String",
        "erasureStrategy": "Canonical"
      },
      "value": "tacCalldatabuf"
    },
    {
      "key": {
        "name": "tac.storage.bit-width",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 256
    },
    {
      "key": {
        "name": "tac.calldata.offset",
        "type": "java.math.BigInteger",
        "erasureStrategy": "Canonical"
      },
      "value": "44"
    },
    {
      "key": {
        "name": "tac.is.calldata",
        "type": "tac.MetaMap$Companion$NothingValue",
        "erasureStrategy": "Canonical"
      },
      "value": {
      }
    }
  ],
  "52": [
    {
      "key": {
        "name": "tac.meta",
        "type": "vc.data.TACMetaInfo",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "source": 0,
        "begin": 7849,
        "len": 19,
        "jumpType": "REGULAR",
        "address": "ce4604a0000000000000000000000003",
        "sourceContext": {
          "indexToFilepath": {
            "0": "contracts/ERC20.sol",
            "1": "contracts/IERC20.sol",
            "2": "contracts/IERC20Metadata.sol"
          },
          "sourceDir": ".post_autofinders.0"
        }
      }
    }
  ],
  "53": [
    {
      "key": {
        "name": "Tac.symbol.keyword",
        "type": "java.lang.String",
        "erasureStrategy": "Canonical"
      },
      "value": "L"
    },
    {
      "key": {
        "name": "tac.stack.height",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 1017
    }
  ],
  "54": [
    {
      "key": {
        "name": "tac.meta",
        "type": "vc.data.TACMetaInfo",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "source": 0,
        "begin": 7849,
        "len": 31,
        "jumpType": "REGULAR",
        "address": "ce4604a0000000000000000000000003",
        "sourceContext": {
          "indexToFilepath": {
            "0": "contracts/ERC20.sol",
            "1": "contracts/IERC20.sol",
            "2": "contracts/IERC20Metadata.sol"
          },
          "sourceDir": ".post_autofinders.0"
        }
      }
    }
  ],
  "55": [
    {
      "key": {
        "name": "Tac.symbol.keyword",
        "type": "java.lang.String",
        "erasureStrategy": "Canonical"
      },
      "value": "tacM0x0"
    },
    {
      "key": {
        "name": "tac.env.known-bit-width",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 160
    },
    {
      "key": {
        "name": "tac.is-temp-var",
        "type": "tac.MetaMap$Companion$NothingValue",
        "erasureStrategy": "Canonical"
      },
      "value": {
      }
    }
  ],
  "56": [
    {
      "key": {
        "name": "Tac.symbol.keyword",
        "type": "java.lang.String",
        "erasureStrategy": "Canonical"
      },
      "value": "tacM0x20"
    },
    {
      "key": {
        "name": "tac.stack.height",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 1017
    }
  ],
  "57": [
    {
      "key": {
        "name": "tac.meta",
        "type": "vc.data.TACMetaInfo",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "source": 0,
        "begin": 7849,
        "len": 31,
        "jumpType": "REGULAR",
        "address": "ce4604a0000000000000000000000003",
        "sourceContext": {
          "indexToFilepath": {
            "0": "contracts/ERC20.sol",
            "1": "contracts/IERC20.sol",
            "2": "contracts/IERC20Metadata.sol"
          },
          "sourceDir": ".post_autofinders.0"
        }
      }
    },
    {
      "key": {
        "name": "tac.storage.node",
        "type": "analysis.storage.StorageAnalysisResult$StoragePaths",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "storagePaths": [
          {
            "#class": "analysis.storage.StorageAnalysisResult.NonIndexedPath.StructAccess",
            "base": {
              "#class": "analysis.storage.StorageAnalysisResult.NonIndexedPath.MapAccess",
              "base": {
                "#class": "analysis.storage.StorageAnalysisResult.NonIndexedPath.StructAccess",
                "base": {
                  "#class": "analysis.storage.StorageAnalysisResult.NonIndexedPath.MapAccess",
                  "base": {
                    "#class": "analysis.storage.StorageAnalysisResult.NonIndexedPath.Root",
                    "slot": "1"
                  }
                },
                "offset": "0"
              }
            },
            "offset": "0"
          }
        ]
      }
    },
    {
      "key": {
        "name": "tac.storage.access",
        "type": "tac.MetaMap$Companion$NothingValue",
        "erasureStrategy": "Canonical"
      },
      "value": {
      }
    },
    {
      "key": {
        "name": "tac.storage.printer",
        "type": "instrumentation.StoragePathAnnotation$StoragePathPrinter",
        "erasureStrategy": "Canonical"
      },
      "value": {
      }
    }
  ],
  "58": [
    {
      "key": {
        "name": "Tac.symbol.keyword",
        "type": "java.lang.String",
        "erasureStrategy": "Canonical"
      },
      "value": "L"
    },
    {
      "key": {
        "name": "tac.storage.pretty.paths",
        "type": "analysis.storage.DisplayPaths",
        "erasureStrategy": "Erased"
      },
      "value": {
        "paths": [
          {
            "#class": "analysis.storage.DisplayPath.MapAccess",
            "key": {
              "#class": "vc.data.TACSymbol.Var.Full",
              "namePrefix": "R71",
              "tag": {
                "#class": "tac.Tag.Bit256"
              },
              "callIndex": 0,
              "meta": [
                {
                  "key": {
                    "name": "Tac.symbol.keyword",
                    "type": "java.lang.String",
                    "erasureStrategy": "Canonical"
                  },
                  "value": "L"
                },
                {
                  "key": {
                    "name": "tac.env.known-bit-width",
                    "type": "java.lang.Integer",
                    "erasureStrategy": "Canonical"
                  },
                  "value": 160
                },
                {
                  "key": {
                    "name": "tac.is-temp-var",
                    "type": "tac.MetaMap$Companion$NothingValue",
                    "erasureStrategy": "Canonical"
                  },
                  "value": {
                  }
                },
                {
                  "key": {
                    "name": "tac.stack.height",
                    "type": "java.lang.Integer",
                    "erasureStrategy": "Canonical"
                  },
                  "value": 1015
                }
              ]
            },
            "keyTyp": {
              "#class": "tac.TACStorageType.IntegralType",
              "typeLabel": "address",
              "numBytes": "14",
              "descriptor": {
                "#class": "ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$address"
              },
              "lowerBound": null,
              "upperBound": null
            },
            "base": {
              "#class": "analysis.storage.DisplayPath.MapAccess",
              "key": {
                "#class": "vc.data.TACSymbol.Var.Full",
                "namePrefix": "R128",
                "tag": {
                  "#class": "tac.Tag.Bit256"
                },
                "callIndex": 0,
                "meta": [
                  {
                    "key": {
                      "name": "Tac.symbol.keyword",
                      "type": "java.lang.String",
                      "erasureStrategy": "Canonical"
                    },
                    "value": "L"
                  },
                  {
                    "key": {
                      "name": "tac.stack.height",
                      "type": "java.lang.Integer",
                      "erasureStrategy": "Canonical"
                    },
                    "value": 1015
                  }
                ]
              },
              "keyTyp": {
                "#class": "tac.TACStorageType.IntegralType",
                "typeLabel": "address",
                "numBytes": "14",
                "descriptor": {
                  "#class": "ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$address"
                },
                "lowerBound": null,
                "upperBound": null
              },
              "base": {
                "#class": "analysis.storage.DisplayPath.Root",
                "name": "_allowances"
              }
            }
          }
        ]
      }
    },
    {
      "key": {
        "name": "tac.storage.access-paths",
        "type": "analysis.storage.StorageAnalysisResult$AccessPaths",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "paths": [
          {
            "#class": "analysis.storage.StorageAnalysis.AnalysisPath.StructAccess",
            "base": {
              "#class": "analysis.storage.StorageAnalysis.AnalysisPath.MapAccess",
              "base": {
                "#class": "analysis.storage.StorageAnalysis.AnalysisPath.StructAccess",
                "base": {
                  "#class": "analysis.storage.StorageAnalysis.AnalysisPath.MapAccess",
                  "base": {
                    "#class": "analysis.storage.StorageAnalysis.AnalysisPath.Root",
                    "slot": "1"
                  },
                  "key": {
                    "#class": "vc.data.TACSymbol.Var.Full",
                    "namePrefix": "R128",
                    "tag": {
                      "#class": "tac.Tag.Bit256"
                    },
                    "callIndex": 0,
                    "meta": [
                      {
                        "key": {
                          "name": "Tac.symbol.keyword",
                          "type": "java.lang.String",
                          "erasureStrategy": "Canonical"
                        },
                        "value": "L"
                      },
                      {
                        "key": {
                          "name": "tac.stack.height",
                          "type": "java.lang.Integer",
                          "erasureStrategy": "Canonical"
                        },
                        "value": 1015
                      }
                    ]
                  },
                  "baseSlot": {
                    "#class": "vc.data.TACSymbol.Var.Full",
                    "namePrefix": "CANON76",
                    "tag": {
                      "#class": "tac.Tag.Bit256"
                    },
                    "callIndex": 2,
                    "meta": [
                      {
                        "key": {
                          "name": "tac.is-temp-var",
                          "type": "tac.MetaMap$Companion$NothingValue",
                          "erasureStrategy": "Canonical"
                        },
                        "value": {
                        }
                      }
                    ]
                  },
                  "hashResult": {
                    "#class": "vc.data.TACSymbol.Var.Full",
                    "namePrefix": "CANON75",
                    "tag": {
                      "#class": "tac.Tag.Bit256"
                    },
                    "callIndex": 2,
                    "meta": [
                      {
                        "key": {
                          "name": "tac.is-temp-var",
                          "type": "tac.MetaMap$Companion$NothingValue",
                          "erasureStrategy": "Canonical"
                        },
                        "value": {
                        }
                      }
                    ]
                  }
                },
                "offset": {
                  "#class": "analysis.storage.StorageAnalysis.Offset.Words",
                  "numWords": "0"
                }
              },
              "key": {
                "#class": "vc.data.TACSymbol.Var.Full",
                "namePrefix": "R71",
                "tag": {
                  "#class": "tac.Tag.Bit256"
                },
                "callIndex": 0,
                "meta": [
                  {
                    "key": {
                      "name": "Tac.symbol.keyword",
                      "type": "java.lang.String",
                      "erasureStrategy": "Canonical"
                    },
                    "value": "L"
                  },
                  {
                    "key": {
                      "name": "tac.env.known-bit-width",
                      "type": "java.lang.Integer",
                      "erasureStrategy": "Canonical"
                    },
                    "value": 160
                  },
                  {
                    "key": {
                      "name": "tac.is-temp-var",
                      "type": "tac.MetaMap$Companion$NothingValue",
                      "erasureStrategy": "Canonical"
                    },
                    "value": {
                    }
                  },
                  {
                    "key": {
                      "name": "tac.stack.height",
                      "type": "java.lang.Integer",
                      "erasureStrategy": "Canonical"
                    },
                    "value": 1015
                  }
                ]
              },
              "baseSlot": {
                "#class": "vc.data.TACSymbol.Var.Full",
                "namePrefix": "CANON78",
                "tag": {
                  "#class": "tac.Tag.Bit256"
                },
                "callIndex": 2,
                "meta": [
                  {
                    "key": {
                      "name": "tac.is-temp-var",
                      "type": "tac.MetaMap$Companion$NothingValue",
                      "erasureStrategy": "Canonical"
                    },
                    "value": {
                    }
                  }
                ]
              },
              "hashResult": {
                "#class": "vc.data.TACSymbol.Var.Full",
                "namePrefix": "CANON77",
                "tag": {
                  "#class": "tac.Tag.Bit256"
                },
                "callIndex": 2,
                "meta": [
                  {
                    "key": {
                      "name": "tac.is-temp-var",
                      "type": "tac.MetaMap$Companion$NothingValue",
                      "erasureStrategy": "Canonical"
                    },
                    "value": {
                    }
                  }
                ]
              }
            },
            "offset": {
              "#class": "analysis.storage.StorageAnalysis.Offset.Words",
              "numWords": "0"
            }
          }
        ]
      }
    },
    {
      "key": {
        "name": "tac.stack.height",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 1017
    }
  ],
  "59": [
    {
      "key": {
        "name": "tac.meta",
        "type": "vc.data.TACMetaInfo",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "source": 0,
        "begin": 8067,
        "len": 25,
        "jumpType": "REGULAR",
        "address": "ce4604a0000000000000000000000003",
        "sourceContext": {
          "indexToFilepath": {
            "0": "contracts/ERC20.sol",
            "1": "contracts/IERC20.sol",
            "2": "contracts/IERC20Metadata.sol"
          },
          "sourceDir": ".post_autofinders.0"
        }
      }
    },
    {
      "key": {
        "name": "optimization.overflow.safe",
        "type": "tac.MetaMap$Companion$NothingValue",
        "erasureStrategy": "Canonical"
      },
      "value": {
      }
    }
  ],
  "60": [
    {
      "key": {
        "name": "Tac.symbol.keyword",
        "type": "java.lang.String",
        "erasureStrategy": "Canonical"
      },
      "value": "L"
    },
    {
      "key": {
        "name": "tac.stack.height",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 1014
    }
  ],
  "61": [
    {
      "key": {
        "name": "Tac.symbol.keyword",
        "type": "java.lang.String",
        "erasureStrategy": "Canonical"
      },
      "value": "L"
    },
    {
      "key": {
        "name": "tac.stack.height",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 1012
    }
  ],
  "62": [
    {
      "key": {
        "name": "Tac.symbol.keyword",
        "type": "java.lang.String",
        "erasureStrategy": "Canonical"
      },
      "value": "L"
    },
    {
      "key": {
        "name": "tac.stack.height",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 1010
    }
  ],
  "63": [
    {
      "key": {
        "name": "tac.meta",
        "type": "vc.data.TACMetaInfo",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "source": 0,
        "begin": 11689,
        "len": 17,
        "jumpType": "REGULAR",
        "address": "ce4604a0000000000000000000000003",
        "sourceContext": {
          "indexToFilepath": {
            "0": "contracts/ERC20.sol",
            "1": "contracts/IERC20.sol",
            "2": "contracts/IERC20Metadata.sol"
          },
          "sourceDir": ".post_autofinders.0"
        }
      }
    }
  ],
  "64": [
    {
      "key": {
        "name": "tac.meta",
        "type": "vc.data.TACMetaInfo",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "source": 0,
        "begin": 11689,
        "len": 17,
        "jumpType": "REGULAR",
        "address": "ce4604a0000000000000000000000003",
        "sourceContext": {
          "indexToFilepath": {
            "0": "contracts/ERC20.sol",
            "1": "contracts/IERC20.sol",
            "2": "contracts/IERC20Metadata.sol"
          },
          "sourceDir": ".post_autofinders.0"
        }
      }
    },
    {
      "key": {
        "name": "tac.storage.node",
        "type": "analysis.storage.StorageAnalysisResult$StoragePaths",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "storagePaths": [
          {
            "#class": "analysis.storage.StorageAnalysisResult.NonIndexedPath.StructAccess",
            "base": {
              "#class": "analysis.storage.StorageAnalysisResult.NonIndexedPath.MapAccess",
              "base": {
                "#class": "analysis.storage.StorageAnalysisResult.NonIndexedPath.Root",
                "slot": "0"
              }
            },
            "offset": "0"
          }
        ]
      }
    },
    {
      "key": {
        "name": "tac.storage.access",
        "type": "tac.MetaMap$Companion$NothingValue",
        "erasureStrategy": "Canonical"
      },
      "value": {
      }
    },
    {
      "key": {
        "name": "tac.storage.printer",
        "type": "instrumentation.StoragePathAnnotation$StoragePathPrinter",
        "erasureStrategy": "Canonical"
      },
      "value": {
      }
    }
  ],
  "65": [
    {
      "key": {
        "name": "Tac.symbol.keyword",
        "type": "java.lang.String",
        "erasureStrategy": "Canonical"
      },
      "value": "L"
    },
    {
      "key": {
        "name": "tac.storage.pretty.paths",
        "type": "analysis.storage.DisplayPaths",
        "erasureStrategy": "Erased"
      },
      "value": {
        "paths": [
          {
            "#class": "analysis.storage.DisplayPath.MapAccess",
            "key": {
              "#class": "vc.data.TACSymbol.Var.Full",
              "namePrefix": "R153",
              "tag": {
                "#class": "tac.Tag.Bit256"
              },
              "callIndex": 0,
              "meta": [
                {
                  "key": {
                    "name": "Tac.symbol.keyword",
                    "type": "java.lang.String",
                    "erasureStrategy": "Canonical"
                  },
                  "value": "L"
                },
                {
                  "key": {
                    "name": "tac.stack.height",
                    "type": "java.lang.Integer",
                    "erasureStrategy": "Canonical"
                  },
                  "value": 1010
                }
              ]
            },
            "keyTyp": {
              "#class": "tac.TACStorageType.IntegralType",
              "typeLabel": "address",
              "numBytes": "14",
              "descriptor": {
                "#class": "ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$address"
              },
              "lowerBound": null,
              "upperBound": null
            },
            "base": {
              "#class": "analysis.storage.DisplayPath.Root",
              "name": "_balances"
            }
          }
        ]
      }
    },
    {
      "key": {
        "name": "tac.storage.access-paths",
        "type": "analysis.storage.StorageAnalysisResult$AccessPaths",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "paths": [
          {
            "#class": "analysis.storage.StorageAnalysis.AnalysisPath.StructAccess",
            "base": {
              "#class": "analysis.storage.StorageAnalysis.AnalysisPath.MapAccess",
              "base": {
                "#class": "analysis.storage.StorageAnalysis.AnalysisPath.Root",
                "slot": "0"
              },
              "key": {
                "#class": "vc.data.TACSymbol.Var.Full",
                "namePrefix": "R153",
                "tag": {
                  "#class": "tac.Tag.Bit256"
                },
                "callIndex": 0,
                "meta": [
                  {
                    "key": {
                      "name": "Tac.symbol.keyword",
                      "type": "java.lang.String",
                      "erasureStrategy": "Canonical"
                    },
                    "value": "L"
                  },
                  {
                    "key": {
                      "name": "tac.stack.height",
                      "type": "java.lang.Integer",
                      "erasureStrategy": "Canonical"
                    },
                    "value": 1010
                  }
                ]
              },
              "baseSlot": {
                "#class": "vc.data.TACSymbol.Var.Full",
                "namePrefix": "CANON85",
                "tag": {
                  "#class": "tac.Tag.Bit256"
                },
                "callIndex": 2,
                "meta": [
                  {
                    "key": {
                      "name": "tac.is-temp-var",
                      "type": "tac.MetaMap$Companion$NothingValue",
                      "erasureStrategy": "Canonical"
                    },
                    "value": {
                    }
                  }
                ]
              },
              "hashResult": {
                "#class": "vc.data.TACSymbol.Var.Full",
                "namePrefix": "CANON84",
                "tag": {
                  "#class": "tac.Tag.Bit256"
                },
                "callIndex": 2,
                "meta": [
                  {
                    "key": {
                      "name": "tac.is-temp-var",
                      "type": "tac.MetaMap$Companion$NothingValue",
                      "erasureStrategy": "Canonical"
                    },
                    "value": {
                    }
                  }
                ]
              }
            },
            "offset": {
              "#class": "analysis.storage.StorageAnalysis.Offset.Words",
              "numWords": "0"
            }
          }
        ]
      }
    },
    {
      "key": {
        "name": "tac.stack.height",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 1012
    }
  ],
  "66": [
    {
      "key": {
        "name": "tac.meta",
        "type": "vc.data.TACMetaInfo",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "source": 0,
        "begin": 11879,
        "len": 22,
        "jumpType": "REGULAR",
        "address": "ce4604a0000000000000000000000003",
        "sourceContext": {
          "indexToFilepath": {
            "0": "contracts/ERC20.sol",
            "1": "contracts/IERC20.sol",
            "2": "contracts/IERC20Metadata.sol"
          },
          "sourceDir": ".post_autofinders.0"
        }
      }
    },
    {
      "key": {
        "name": "optimization.overflow.safe",
        "type": "tac.MetaMap$Companion$NothingValue",
        "erasureStrategy": "Canonical"
      },
      "value": {
      }
    }
  ],
  "67": [
    {
      "key": {
        "name": "Tac.symbol.keyword",
        "type": "java.lang.String",
        "erasureStrategy": "Canonical"
      },
      "value": "L"
    },
    {
      "key": {
        "name": "tac.stack.height",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 1009
    }
  ],
  "68": [
    {
      "key": {
        "name": "tac.meta",
        "type": "vc.data.TACMetaInfo",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "source": 0,
        "begin": 11859,
        "len": 17,
        "jumpType": "REGULAR",
        "address": "ce4604a0000000000000000000000003",
        "sourceContext": {
          "indexToFilepath": {
            "0": "contracts/ERC20.sol",
            "1": "contracts/IERC20.sol",
            "2": "contracts/IERC20Metadata.sol"
          },
          "sourceDir": ".post_autofinders.0"
        }
      }
    }
  ],
  "69": [
    {
      "key": {
        "name": "Tac.symbol.keyword",
        "type": "java.lang.String",
        "erasureStrategy": "Canonical"
      },
      "value": "L"
    },
    {
      "key": {
        "name": "tac.storage.pretty.paths",
        "type": "analysis.storage.DisplayPaths",
        "erasureStrategy": "Erased"
      },
      "value": {
        "paths": [
          {
            "#class": "analysis.storage.DisplayPath.MapAccess",
            "key": {
              "#class": "vc.data.TACSymbol.Var.Full",
              "namePrefix": "R159",
              "tag": {
                "#class": "tac.Tag.Bit256"
              },
              "callIndex": 0,
              "meta": [
                {
                  "key": {
                    "name": "Tac.symbol.keyword",
                    "type": "java.lang.String",
                    "erasureStrategy": "Canonical"
                  },
                  "value": "L"
                },
                {
                  "key": {
                    "name": "tac.stack.height",
                    "type": "java.lang.Integer",
                    "erasureStrategy": "Canonical"
                  },
                  "value": 1009
                }
              ]
            },
            "keyTyp": {
              "#class": "tac.TACStorageType.IntegralType",
              "typeLabel": "address",
              "numBytes": "14",
              "descriptor": {
                "#class": "ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$address"
              },
              "lowerBound": null,
              "upperBound": null
            },
            "base": {
              "#class": "analysis.storage.DisplayPath.Root",
              "name": "_balances"
            }
          }
        ]
      }
    },
    {
      "key": {
        "name": "tac.storage.access-paths",
        "type": "analysis.storage.StorageAnalysisResult$AccessPaths",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "paths": [
          {
            "#class": "analysis.storage.StorageAnalysis.AnalysisPath.StructAccess",
            "base": {
              "#class": "analysis.storage.StorageAnalysis.AnalysisPath.MapAccess",
              "base": {
                "#class": "analysis.storage.StorageAnalysis.AnalysisPath.Root",
                "slot": "0"
              },
              "key": {
                "#class": "vc.data.TACSymbol.Var.Full",
                "namePrefix": "R159",
                "tag": {
                  "#class": "tac.Tag.Bit256"
                },
                "callIndex": 0,
                "meta": [
                  {
                    "key": {
                      "name": "Tac.symbol.keyword",
                      "type": "java.lang.String",
                      "erasureStrategy": "Canonical"
                    },
                    "value": "L"
                  },
                  {
                    "key": {
                      "name": "tac.stack.height",
                      "type": "java.lang.Integer",
                      "erasureStrategy": "Canonical"
                    },
                    "value": 1009
                  }
                ]
              },
              "baseSlot": {
                "#class": "vc.data.TACSymbol.Var.Full",
                "namePrefix": "CANON88",
                "tag": {
                  "#class": "tac.Tag.Bit256"
                },
                "callIndex": 2,
                "meta": [
                  {
                    "key": {
                      "name": "tac.is-temp-var",
                      "type": "tac.MetaMap$Companion$NothingValue",
                      "erasureStrategy": "Canonical"
                    },
                    "value": {
                    }
                  }
                ]
              },
              "hashResult": {
                "#class": "vc.data.TACSymbol.Var.Full",
                "namePrefix": "CANON87",
                "tag": {
                  "#class": "tac.Tag.Bit256"
                },
                "callIndex": 2,
                "meta": [
                  {
                    "key": {
                      "name": "tac.is-temp-var",
                      "type": "tac.MetaMap$Companion$NothingValue",
                      "erasureStrategy": "Canonical"
                    },
                    "value": {
                    }
                  }
                ]
              }
            },
            "offset": {
              "#class": "analysis.storage.StorageAnalysis.Offset.Words",
              "numWords": "0"
            }
          }
        ]
      }
    },
    {
      "key": {
        "name": "tac.stack.height",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 1011
    }
  ],
  "70": [
    {
      "key": {
        "name": "tac.meta",
        "type": "vc.data.TACMetaInfo",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "source": 0,
        "begin": 11859,
        "len": 42,
        "jumpType": "REGULAR",
        "address": "ce4604a0000000000000000000000003",
        "sourceContext": {
          "indexToFilepath": {
            "0": "contracts/ERC20.sol",
            "1": "contracts/IERC20.sol",
            "2": "contracts/IERC20Metadata.sol"
          },
          "sourceDir": ".post_autofinders.0"
        }
      }
    },
    {
      "key": {
        "name": "tac.storage.node",
        "type": "analysis.storage.StorageAnalysisResult$StoragePaths",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "storagePaths": [
          {
            "#class": "analysis.storage.StorageAnalysisResult.NonIndexedPath.StructAccess",
            "base": {
              "#class": "analysis.storage.StorageAnalysisResult.NonIndexedPath.MapAccess",
              "base": {
                "#class": "analysis.storage.StorageAnalysisResult.NonIndexedPath.Root",
                "slot": "0"
              }
            },
            "offset": "0"
          }
        ]
      }
    },
    {
      "key": {
        "name": "tac.storage.access",
        "type": "tac.MetaMap$Companion$NothingValue",
        "erasureStrategy": "Canonical"
      },
      "value": {
      }
    },
    {
      "key": {
        "name": "tac.storage.printer",
        "type": "instrumentation.StoragePathAnnotation$StoragePathPrinter",
        "erasureStrategy": "Canonical"
      },
      "value": {
      }
    }
  ],
  "71": [
    {
      "key": {
        "name": "cvl.exp",
        "type": "spec.CVLExpToTACExprMeta",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "spec.CVLExpToTACExprMeta.BinaryCVLExp",
        "exp": {
          "#class": "spec.cvlast.CVLExp.BinaryExp.AddExp",
          "l": {
            "#class": "spec.cvlast.CVLExp.VariableExp",
            "id": "sum_of_balances",
            "tag": {
              "scope": {
                "scopeStack": [
                  {
                    "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                  },
                  {
                    "#class": "spec.cvlast.CVLScope.Item.HookScopeItem",
                    "scopeId": 11
                  }
                ],
                "innerScope": {
                  "scopeStack": [
                    {
                      "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                    }
                  ],
                  "innerScope": {
                    "scopeStack": [
                    ],
                    "innerScope": null
                  }
                }
              },
              "type": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Mathint"
              },
              "cvlRange": {
                "#class": "spec.cvlast.CVLRange.Range",
                "specFile": "certora/spec/ERC20.spec",
                "start": {
                  "line": 136,
                  "character": 4
                },
                "end": {
                  "line": 136,
                  "character": 62
                }
              }
            },
            "twoStateIndex": "NEITHER"
          },
          "r": {
            "#class": "spec.cvlast.CVLExp.VariableExp",
            "id": "new_value",
            "tag": {
              "scope": {
                "scopeStack": [
                  {
                    "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                  },
                  {
                    "#class": "spec.cvlast.CVLScope.Item.HookScopeItem",
                    "scopeId": 11
                  }
                ],
                "innerScope": {
                  "scopeStack": [
                    {
                      "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                    }
                  ],
                  "innerScope": {
                    "scopeStack": [
                    ],
                    "innerScope": null
                  }
                }
              },
              "type": {
                "#class": "spec.cvlast.CVLType.VM",
                "descriptor": {
                  "#class": "ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK",
                  "bitwidth": 256
                },
                "context": {
                  "#class": "spec.cvlast.typedescriptors.FromVMContext.HookValue"
                }
              },
              "cvlRange": {
                "#class": "spec.cvlast.CVLRange.Range",
                "specFile": "certora/spec/ERC20.spec",
                "start": {
                  "line": 136,
                  "character": 4
                },
                "end": {
                  "line": 136,
                  "character": 62
                }
              }
            },
            "twoStateIndex": "NEITHER"
          },
          "tag": {
            "scope": {
              "scopeStack": [
                {
                  "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                },
                {
                  "#class": "spec.cvlast.CVLScope.Item.HookScopeItem",
                  "scopeId": 11
                }
              ],
              "innerScope": {
                "scopeStack": [
                  {
                    "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                  }
                ],
                "innerScope": {
                  "scopeStack": [
                  ],
                  "innerScope": null
                }
              }
            },
            "type": {
              "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Mathint"
            },
            "cvlRange": {
              "#class": "spec.cvlast.CVLRange.Range",
              "specFile": "certora/spec/ERC20.spec",
              "start": {
                "line": 136,
                "character": 22
              },
              "end": {
                "line": 136,
                "character": 49
              }
            }
          }
        },
        "o1": {
          "out": {
            "#class": "vc.data.TACSymbol.Var.Full",
            "namePrefix": "I4",
            "tag": {
              "#class": "tac.Tag.Int"
            },
            "callIndex": 0
          },
          "exp": {
            "#class": "spec.cvlast.CVLExp.VariableExp",
            "id": "sum_of_balances",
            "tag": {
              "scope": {
                "scopeStack": [
                  {
                    "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                  },
                  {
                    "#class": "spec.cvlast.CVLScope.Item.HookScopeItem",
                    "scopeId": 11
                  }
                ],
                "innerScope": {
                  "scopeStack": [
                    {
                      "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                    }
                  ],
                  "innerScope": {
                    "scopeStack": [
                    ],
                    "innerScope": null
                  }
                }
              },
              "type": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Mathint"
              },
              "cvlRange": {
                "#class": "spec.cvlast.CVLRange.Range",
                "specFile": "certora/spec/ERC20.spec",
                "start": {
                  "line": 136,
                  "character": 4
                },
                "end": {
                  "line": 136,
                  "character": 62
                }
              }
            },
            "twoStateIndex": "NEITHER"
          }
        },
        "o2": {
          "out": {
            "#class": "vc.data.TACSymbol.Var.Full",
            "namePrefix": "I165",
            "tag": {
              "#class": "tac.Tag.Int"
            },
            "callIndex": 0
          },
          "exp": {
            "#class": "spec.cvlast.CVLExp.VariableExp",
            "id": "new_value",
            "tag": {
              "scope": {
                "scopeStack": [
                  {
                    "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                  },
                  {
                    "#class": "spec.cvlast.CVLScope.Item.HookScopeItem",
                    "scopeId": 11
                  }
                ],
                "innerScope": {
                  "scopeStack": [
                    {
                      "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                    }
                  ],
                  "innerScope": {
                    "scopeStack": [
                    ],
                    "innerScope": null
                  }
                }
              },
              "type": {
                "#class": "spec.cvlast.CVLType.VM",
                "descriptor": {
                  "#class": "ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK",
                  "bitwidth": 256
                },
                "context": {
                  "#class": "spec.cvlast.typedescriptors.FromVMContext.HookValue"
                }
              },
              "cvlRange": {
                "#class": "spec.cvlast.CVLRange.Range",
                "specFile": "certora/spec/ERC20.spec",
                "start": {
                  "line": 136,
                  "character": 4
                },
                "end": {
                  "line": 136,
                  "character": 62
                }
              }
            },
            "twoStateIndex": "NEITHER"
          }
        }
      }
    },
    {
      "key": {
        "name": "cvl.range",
        "type": "spec.cvlast.CVLRange",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "spec.cvlast.CVLRange.Range",
        "specFile": "certora/spec/ERC20.spec",
        "start": {
          "line": 136,
          "character": 4
        },
        "end": {
          "line": 136,
          "character": 62
        }
      }
    }
  ],
  "72": [
    {
      "key": {
        "name": "cvl.exp",
        "type": "spec.CVLExpToTACExprMeta",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "spec.CVLExpToTACExprMeta.BinaryCVLExp",
        "exp": {
          "#class": "spec.cvlast.CVLExp.BinaryExp.SubExp",
          "l": {
            "#class": "spec.cvlast.CVLExp.BinaryExp.AddExp",
            "l": {
              "#class": "spec.cvlast.CVLExp.VariableExp",
              "id": "sum_of_balances",
              "tag": {
                "scope": {
                  "scopeStack": [
                    {
                      "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                    },
                    {
                      "#class": "spec.cvlast.CVLScope.Item.HookScopeItem",
                      "scopeId": 11
                    }
                  ],
                  "innerScope": {
                    "scopeStack": [
                      {
                        "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                      }
                    ],
                    "innerScope": {
                      "scopeStack": [
                      ],
                      "innerScope": null
                    }
                  }
                },
                "type": {
                  "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Mathint"
                },
                "cvlRange": {
                  "#class": "spec.cvlast.CVLRange.Range",
                  "specFile": "certora/spec/ERC20.spec",
                  "start": {
                    "line": 136,
                    "character": 4
                  },
                  "end": {
                    "line": 136,
                    "character": 62
                  }
                }
              },
              "twoStateIndex": "NEITHER"
            },
            "r": {
              "#class": "spec.cvlast.CVLExp.VariableExp",
              "id": "new_value",
              "tag": {
                "scope": {
                  "scopeStack": [
                    {
                      "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                    },
                    {
                      "#class": "spec.cvlast.CVLScope.Item.HookScopeItem",
                      "scopeId": 11
                    }
                  ],
                  "innerScope": {
                    "scopeStack": [
                      {
                        "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                      }
                    ],
                    "innerScope": {
                      "scopeStack": [
                      ],
                      "innerScope": null
                    }
                  }
                },
                "type": {
                  "#class": "spec.cvlast.CVLType.VM",
                  "descriptor": {
                    "#class": "ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK",
                    "bitwidth": 256
                  },
                  "context": {
                    "#class": "spec.cvlast.typedescriptors.FromVMContext.HookValue"
                  }
                },
                "cvlRange": {
                  "#class": "spec.cvlast.CVLRange.Range",
                  "specFile": "certora/spec/ERC20.spec",
                  "start": {
                    "line": 136,
                    "character": 4
                  },
                  "end": {
                    "line": 136,
                    "character": 62
                  }
                }
              },
              "twoStateIndex": "NEITHER"
            },
            "tag": {
              "scope": {
                "scopeStack": [
                  {
                    "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                  },
                  {
                    "#class": "spec.cvlast.CVLScope.Item.HookScopeItem",
                    "scopeId": 11
                  }
                ],
                "innerScope": {
                  "scopeStack": [
                    {
                      "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                    }
                  ],
                  "innerScope": {
                    "scopeStack": [
                    ],
                    "innerScope": null
                  }
                }
              },
              "type": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Mathint"
              },
              "cvlRange": {
                "#class": "spec.cvlast.CVLRange.Range",
                "specFile": "certora/spec/ERC20.spec",
                "start": {
                  "line": 136,
                  "character": 22
                },
                "end": {
                  "line": 136,
                  "character": 49
                }
              }
            }
          },
          "r": {
            "#class": "spec.cvlast.CVLExp.VariableExp",
            "id": "old_value",
            "tag": {
              "scope": {
                "scopeStack": [
                  {
                    "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                  },
                  {
                    "#class": "spec.cvlast.CVLScope.Item.HookScopeItem",
                    "scopeId": 11
                  }
                ],
                "innerScope": {
                  "scopeStack": [
                    {
                      "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                    }
                  ],
                  "innerScope": {
                    "scopeStack": [
                    ],
                    "innerScope": null
                  }
                }
              },
              "type": {
                "#class": "spec.cvlast.CVLType.VM",
                "descriptor": {
                  "#class": "ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK",
                  "bitwidth": 256
                },
                "context": {
                  "#class": "spec.cvlast.typedescriptors.FromVMContext.HookValue"
                }
              },
              "cvlRange": {
                "#class": "spec.cvlast.CVLRange.Range",
                "specFile": "certora/spec/ERC20.spec",
                "start": {
                  "line": 136,
                  "character": 4
                },
                "end": {
                  "line": 136,
                  "character": 62
                }
              }
            },
            "twoStateIndex": "NEITHER"
          },
          "tag": {
            "scope": {
              "scopeStack": [
                {
                  "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                },
                {
                  "#class": "spec.cvlast.CVLScope.Item.HookScopeItem",
                  "scopeId": 11
                }
              ],
              "innerScope": {
                "scopeStack": [
                  {
                    "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                  }
                ],
                "innerScope": {
                  "scopeStack": [
                  ],
                  "innerScope": null
                }
              }
            },
            "type": {
              "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Mathint"
            },
            "cvlRange": {
              "#class": "spec.cvlast.CVLRange.Range",
              "specFile": "certora/spec/ERC20.spec",
              "start": {
                "line": 136,
                "character": 22
              },
              "end": {
                "line": 136,
                "character": 61
              }
            }
          }
        },
        "o1": {
          "out": {
            "#class": "vc.data.TACSymbol.Var.Full",
            "namePrefix": "I166",
            "tag": {
              "#class": "tac.Tag.Int"
            },
            "callIndex": 0
          },
          "exp": {
            "#class": "spec.cvlast.CVLExp.BinaryExp.AddExp",
            "l": {
              "#class": "spec.cvlast.CVLExp.VariableExp",
              "id": "sum_of_balances",
              "tag": {
                "scope": {
                  "scopeStack": [
                    {
                      "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                    },
                    {
                      "#class": "spec.cvlast.CVLScope.Item.HookScopeItem",
                      "scopeId": 11
                    }
                  ],
                  "innerScope": {
                    "scopeStack": [
                      {
                        "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                      }
                    ],
                    "innerScope": {
                      "scopeStack": [
                      ],
                      "innerScope": null
                    }
                  }
                },
                "type": {
                  "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Mathint"
                },
                "cvlRange": {
                  "#class": "spec.cvlast.CVLRange.Range",
                  "specFile": "certora/spec/ERC20.spec",
                  "start": {
                    "line": 136,
                    "character": 4
                  },
                  "end": {
                    "line": 136,
                    "character": 62
                  }
                }
              },
              "twoStateIndex": "NEITHER"
            },
            "r": {
              "#class": "spec.cvlast.CVLExp.VariableExp",
              "id": "new_value",
              "tag": {
                "scope": {
                  "scopeStack": [
                    {
                      "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                    },
                    {
                      "#class": "spec.cvlast.CVLScope.Item.HookScopeItem",
                      "scopeId": 11
                    }
                  ],
                  "innerScope": {
                    "scopeStack": [
                      {
                        "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                      }
                    ],
                    "innerScope": {
                      "scopeStack": [
                      ],
                      "innerScope": null
                    }
                  }
                },
                "type": {
                  "#class": "spec.cvlast.CVLType.VM",
                  "descriptor": {
                    "#class": "ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK",
                    "bitwidth": 256
                  },
                  "context": {
                    "#class": "spec.cvlast.typedescriptors.FromVMContext.HookValue"
                  }
                },
                "cvlRange": {
                  "#class": "spec.cvlast.CVLRange.Range",
                  "specFile": "certora/spec/ERC20.spec",
                  "start": {
                    "line": 136,
                    "character": 4
                  },
                  "end": {
                    "line": 136,
                    "character": 62
                  }
                }
              },
              "twoStateIndex": "NEITHER"
            },
            "tag": {
              "scope": {
                "scopeStack": [
                  {
                    "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                  },
                  {
                    "#class": "spec.cvlast.CVLScope.Item.HookScopeItem",
                    "scopeId": 11
                  }
                ],
                "innerScope": {
                  "scopeStack": [
                    {
                      "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                    }
                  ],
                  "innerScope": {
                    "scopeStack": [
                    ],
                    "innerScope": null
                  }
                }
              },
              "type": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Mathint"
              },
              "cvlRange": {
                "#class": "spec.cvlast.CVLRange.Range",
                "specFile": "certora/spec/ERC20.spec",
                "start": {
                  "line": 136,
                  "character": 22
                },
                "end": {
                  "line": 136,
                  "character": 49
                }
              }
            }
          }
        },
        "o2": {
          "out": {
            "#class": "vc.data.TACSymbol.Var.Full",
            "namePrefix": "I167",
            "tag": {
              "#class": "tac.Tag.Int"
            },
            "callIndex": 0
          },
          "exp": {
            "#class": "spec.cvlast.CVLExp.VariableExp",
            "id": "old_value",
            "tag": {
              "scope": {
                "scopeStack": [
                  {
                    "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                  },
                  {
                    "#class": "spec.cvlast.CVLScope.Item.HookScopeItem",
                    "scopeId": 11
                  }
                ],
                "innerScope": {
                  "scopeStack": [
                    {
                      "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                    }
                  ],
                  "innerScope": {
                    "scopeStack": [
                    ],
                    "innerScope": null
                  }
                }
              },
              "type": {
                "#class": "spec.cvlast.CVLType.VM",
                "descriptor": {
                  "#class": "ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK",
                  "bitwidth": 256
                },
                "context": {
                  "#class": "spec.cvlast.typedescriptors.FromVMContext.HookValue"
                }
              },
              "cvlRange": {
                "#class": "spec.cvlast.CVLRange.Range",
                "specFile": "certora/spec/ERC20.spec",
                "start": {
                  "line": 136,
                  "character": 4
                },
                "end": {
                  "line": 136,
                  "character": 62
                }
              }
            },
            "twoStateIndex": "NEITHER"
          }
        }
      }
    },
    {
      "key": {
        "name": "cvl.range",
        "type": "spec.cvlast.CVLRange",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "spec.cvlast.CVLRange.Range",
        "specFile": "certora/spec/ERC20.spec",
        "start": {
          "line": 136,
          "character": 4
        },
        "end": {
          "line": 136,
          "character": 62
        }
      }
    }
  ],
  "73": [
    {
      "key": {
        "name": "tac.meta",
        "type": "vc.data.TACMetaInfo",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "source": 0,
        "begin": 11921,
        "len": 20,
        "jumpType": "REGULAR",
        "address": "ce4604a0000000000000000000000003",
        "sourceContext": {
          "indexToFilepath": {
            "0": "contracts/ERC20.sol",
            "1": "contracts/IERC20.sol",
            "2": "contracts/IERC20Metadata.sol"
          },
          "sourceDir": ".post_autofinders.0"
        }
      }
    }
  ],
  "74": [
    {
      "key": {
        "name": "tac.meta",
        "type": "vc.data.TACMetaInfo",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "source": 0,
        "begin": 11921,
        "len": 30,
        "jumpType": "REGULAR",
        "address": "ce4604a0000000000000000000000003",
        "sourceContext": {
          "indexToFilepath": {
            "0": "contracts/ERC20.sol",
            "1": "contracts/IERC20.sol",
            "2": "contracts/IERC20Metadata.sol"
          },
          "sourceDir": ".post_autofinders.0"
        }
      }
    },
    {
      "key": {
        "name": "tac.storage.node",
        "type": "analysis.storage.StorageAnalysisResult$StoragePaths",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "storagePaths": [
          {
            "#class": "analysis.storage.StorageAnalysisResult.NonIndexedPath.StructAccess",
            "base": {
              "#class": "analysis.storage.StorageAnalysisResult.NonIndexedPath.MapAccess",
              "base": {
                "#class": "analysis.storage.StorageAnalysisResult.NonIndexedPath.Root",
                "slot": "0"
              }
            },
            "offset": "0"
          }
        ]
      }
    },
    {
      "key": {
        "name": "tac.storage.access",
        "type": "tac.MetaMap$Companion$NothingValue",
        "erasureStrategy": "Canonical"
      },
      "value": {
      }
    },
    {
      "key": {
        "name": "tac.storage.printer",
        "type": "instrumentation.StoragePathAnnotation$StoragePathPrinter",
        "erasureStrategy": "Canonical"
      },
      "value": {
      }
    }
  ],
  "75": [
    {
      "key": {
        "name": "Tac.symbol.keyword",
        "type": "java.lang.String",
        "erasureStrategy": "Canonical"
      },
      "value": "L"
    },
    {
      "key": {
        "name": "tac.stack.height",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 1008
    }
  ],
  "76": [
    {
      "key": {
        "name": "Tac.symbol.keyword",
        "type": "java.lang.String",
        "erasureStrategy": "Canonical"
      },
      "value": "L"
    },
    {
      "key": {
        "name": "tac.storage.pretty.paths",
        "type": "analysis.storage.DisplayPaths",
        "erasureStrategy": "Erased"
      },
      "value": {
        "paths": [
          {
            "#class": "analysis.storage.DisplayPath.MapAccess",
            "key": {
              "#class": "vc.data.TACSymbol.Var.Full",
              "namePrefix": "R169",
              "tag": {
                "#class": "tac.Tag.Bit256"
              },
              "callIndex": 0,
              "meta": [
                {
                  "key": {
                    "name": "Tac.symbol.keyword",
                    "type": "java.lang.String",
                    "erasureStrategy": "Canonical"
                  },
                  "value": "L"
                },
                {
                  "key": {
                    "name": "tac.stack.height",
                    "type": "java.lang.Integer",
                    "erasureStrategy": "Canonical"
                  },
                  "value": 1009
                }
              ]
            },
            "keyTyp": {
              "#class": "tac.TACStorageType.IntegralType",
              "typeLabel": "address",
              "numBytes": "14",
              "descriptor": {
                "#class": "ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$address"
              },
              "lowerBound": null,
              "upperBound": null
            },
            "base": {
              "#class": "analysis.storage.DisplayPath.Root",
              "name": "_balances"
            }
          }
        ]
      }
    },
    {
      "key": {
        "name": "tac.storage.access-paths",
        "type": "analysis.storage.StorageAnalysisResult$AccessPaths",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "paths": [
          {
            "#class": "analysis.storage.StorageAnalysis.AnalysisPath.StructAccess",
            "base": {
              "#class": "analysis.storage.StorageAnalysis.AnalysisPath.MapAccess",
              "base": {
                "#class": "analysis.storage.StorageAnalysis.AnalysisPath.Root",
                "slot": "0"
              },
              "key": {
                "#class": "vc.data.TACSymbol.Var.Full",
                "namePrefix": "R169",
                "tag": {
                  "#class": "tac.Tag.Bit256"
                },
                "callIndex": 0,
                "meta": [
                  {
                    "key": {
                      "name": "Tac.symbol.keyword",
                      "type": "java.lang.String",
                      "erasureStrategy": "Canonical"
                    },
                    "value": "L"
                  },
                  {
                    "key": {
                      "name": "tac.stack.height",
                      "type": "java.lang.Integer",
                      "erasureStrategy": "Canonical"
                    },
                    "value": 1009
                  }
                ]
              },
              "baseSlot": {
                "#class": "vc.data.TACSymbol.Var.Full",
                "namePrefix": "CANON94",
                "tag": {
                  "#class": "tac.Tag.Bit256"
                },
                "callIndex": 2,
                "meta": [
                  {
                    "key": {
                      "name": "tac.is-temp-var",
                      "type": "tac.MetaMap$Companion$NothingValue",
                      "erasureStrategy": "Canonical"
                    },
                    "value": {
                    }
                  }
                ]
              },
              "hashResult": {
                "#class": "vc.data.TACSymbol.Var.Full",
                "namePrefix": "CANON93",
                "tag": {
                  "#class": "tac.Tag.Bit256"
                },
                "callIndex": 2,
                "meta": [
                  {
                    "key": {
                      "name": "tac.is-temp-var",
                      "type": "tac.MetaMap$Companion$NothingValue",
                      "erasureStrategy": "Canonical"
                    },
                    "value": {
                    }
                  }
                ]
              }
            },
            "offset": {
              "#class": "analysis.storage.StorageAnalysis.Offset.Words",
              "numWords": "0"
            }
          }
        ]
      }
    },
    {
      "key": {
        "name": "tac.stack.height",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 1011
    }
  ],
  "77": [
    {
      "key": {
        "name": "Tac.symbol.keyword",
        "type": "java.lang.String",
        "erasureStrategy": "Canonical"
      },
      "value": "L"
    },
    {
      "key": {
        "name": "tac.stack.height",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 1005
    }
  ],
  "78": [
    {
      "key": {
        "name": "cvl.exp",
        "type": "spec.CVLExpToTACExprMeta",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "spec.CVLExpToTACExprMeta.BinaryCVLExp",
        "exp": {
          "#class": "spec.cvlast.CVLExp.BinaryExp.AddExp",
          "l": {
            "#class": "spec.cvlast.CVLExp.VariableExp",
            "id": "sum_of_balances",
            "tag": {
              "scope": {
                "scopeStack": [
                  {
                    "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                  },
                  {
                    "#class": "spec.cvlast.CVLScope.Item.HookScopeItem",
                    "scopeId": 11
                  }
                ],
                "innerScope": {
                  "scopeStack": [
                    {
                      "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                    }
                  ],
                  "innerScope": {
                    "scopeStack": [
                    ],
                    "innerScope": null
                  }
                }
              },
              "type": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Mathint"
              },
              "cvlRange": {
                "#class": "spec.cvlast.CVLRange.Range",
                "specFile": "certora/spec/ERC20.spec",
                "start": {
                  "line": 136,
                  "character": 4
                },
                "end": {
                  "line": 136,
                  "character": 62
                }
              }
            },
            "twoStateIndex": "NEITHER"
          },
          "r": {
            "#class": "spec.cvlast.CVLExp.VariableExp",
            "id": "new_value",
            "tag": {
              "scope": {
                "scopeStack": [
                  {
                    "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                  },
                  {
                    "#class": "spec.cvlast.CVLScope.Item.HookScopeItem",
                    "scopeId": 11
                  }
                ],
                "innerScope": {
                  "scopeStack": [
                    {
                      "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                    }
                  ],
                  "innerScope": {
                    "scopeStack": [
                    ],
                    "innerScope": null
                  }
                }
              },
              "type": {
                "#class": "spec.cvlast.CVLType.VM",
                "descriptor": {
                  "#class": "ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK",
                  "bitwidth": 256
                },
                "context": {
                  "#class": "spec.cvlast.typedescriptors.FromVMContext.HookValue"
                }
              },
              "cvlRange": {
                "#class": "spec.cvlast.CVLRange.Range",
                "specFile": "certora/spec/ERC20.spec",
                "start": {
                  "line": 136,
                  "character": 4
                },
                "end": {
                  "line": 136,
                  "character": 62
                }
              }
            },
            "twoStateIndex": "NEITHER"
          },
          "tag": {
            "scope": {
              "scopeStack": [
                {
                  "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                },
                {
                  "#class": "spec.cvlast.CVLScope.Item.HookScopeItem",
                  "scopeId": 11
                }
              ],
              "innerScope": {
                "scopeStack": [
                  {
                    "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                  }
                ],
                "innerScope": {
                  "scopeStack": [
                  ],
                  "innerScope": null
                }
              }
            },
            "type": {
              "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Mathint"
            },
            "cvlRange": {
              "#class": "spec.cvlast.CVLRange.Range",
              "specFile": "certora/spec/ERC20.spec",
              "start": {
                "line": 136,
                "character": 22
              },
              "end": {
                "line": 136,
                "character": 49
              }
            }
          }
        },
        "o1": {
          "out": {
            "#class": "vc.data.TACSymbol.Var.Full",
            "namePrefix": "I168",
            "tag": {
              "#class": "tac.Tag.Int"
            },
            "callIndex": 0
          },
          "exp": {
            "#class": "spec.cvlast.CVLExp.VariableExp",
            "id": "sum_of_balances",
            "tag": {
              "scope": {
                "scopeStack": [
                  {
                    "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                  },
                  {
                    "#class": "spec.cvlast.CVLScope.Item.HookScopeItem",
                    "scopeId": 11
                  }
                ],
                "innerScope": {
                  "scopeStack": [
                    {
                      "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                    }
                  ],
                  "innerScope": {
                    "scopeStack": [
                    ],
                    "innerScope": null
                  }
                }
              },
              "type": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Mathint"
              },
              "cvlRange": {
                "#class": "spec.cvlast.CVLRange.Range",
                "specFile": "certora/spec/ERC20.spec",
                "start": {
                  "line": 136,
                  "character": 4
                },
                "end": {
                  "line": 136,
                  "character": 62
                }
              }
            },
            "twoStateIndex": "NEITHER"
          }
        },
        "o2": {
          "out": {
            "#class": "vc.data.TACSymbol.Var.Full",
            "namePrefix": "I180",
            "tag": {
              "#class": "tac.Tag.Int"
            },
            "callIndex": 0
          },
          "exp": {
            "#class": "spec.cvlast.CVLExp.VariableExp",
            "id": "new_value",
            "tag": {
              "scope": {
                "scopeStack": [
                  {
                    "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                  },
                  {
                    "#class": "spec.cvlast.CVLScope.Item.HookScopeItem",
                    "scopeId": 11
                  }
                ],
                "innerScope": {
                  "scopeStack": [
                    {
                      "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                    }
                  ],
                  "innerScope": {
                    "scopeStack": [
                    ],
                    "innerScope": null
                  }
                }
              },
              "type": {
                "#class": "spec.cvlast.CVLType.VM",
                "descriptor": {
                  "#class": "ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK",
                  "bitwidth": 256
                },
                "context": {
                  "#class": "spec.cvlast.typedescriptors.FromVMContext.HookValue"
                }
              },
              "cvlRange": {
                "#class": "spec.cvlast.CVLRange.Range",
                "specFile": "certora/spec/ERC20.spec",
                "start": {
                  "line": 136,
                  "character": 4
                },
                "end": {
                  "line": 136,
                  "character": 62
                }
              }
            },
            "twoStateIndex": "NEITHER"
          }
        }
      }
    },
    {
      "key": {
        "name": "cvl.range",
        "type": "spec.cvlast.CVLRange",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "spec.cvlast.CVLRange.Range",
        "specFile": "certora/spec/ERC20.spec",
        "start": {
          "line": 136,
          "character": 4
        },
        "end": {
          "line": 136,
          "character": 62
        }
      }
    }
  ],
  "79": [
    {
      "key": {
        "name": "cvl.exp",
        "type": "spec.CVLExpToTACExprMeta",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "spec.CVLExpToTACExprMeta.BinaryCVLExp",
        "exp": {
          "#class": "spec.cvlast.CVLExp.BinaryExp.SubExp",
          "l": {
            "#class": "spec.cvlast.CVLExp.BinaryExp.AddExp",
            "l": {
              "#class": "spec.cvlast.CVLExp.VariableExp",
              "id": "sum_of_balances",
              "tag": {
                "scope": {
                  "scopeStack": [
                    {
                      "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                    },
                    {
                      "#class": "spec.cvlast.CVLScope.Item.HookScopeItem",
                      "scopeId": 11
                    }
                  ],
                  "innerScope": {
                    "scopeStack": [
                      {
                        "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                      }
                    ],
                    "innerScope": {
                      "scopeStack": [
                      ],
                      "innerScope": null
                    }
                  }
                },
                "type": {
                  "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Mathint"
                },
                "cvlRange": {
                  "#class": "spec.cvlast.CVLRange.Range",
                  "specFile": "certora/spec/ERC20.spec",
                  "start": {
                    "line": 136,
                    "character": 4
                  },
                  "end": {
                    "line": 136,
                    "character": 62
                  }
                }
              },
              "twoStateIndex": "NEITHER"
            },
            "r": {
              "#class": "spec.cvlast.CVLExp.VariableExp",
              "id": "new_value",
              "tag": {
                "scope": {
                  "scopeStack": [
                    {
                      "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                    },
                    {
                      "#class": "spec.cvlast.CVLScope.Item.HookScopeItem",
                      "scopeId": 11
                    }
                  ],
                  "innerScope": {
                    "scopeStack": [
                      {
                        "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                      }
                    ],
                    "innerScope": {
                      "scopeStack": [
                      ],
                      "innerScope": null
                    }
                  }
                },
                "type": {
                  "#class": "spec.cvlast.CVLType.VM",
                  "descriptor": {
                    "#class": "ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK",
                    "bitwidth": 256
                  },
                  "context": {
                    "#class": "spec.cvlast.typedescriptors.FromVMContext.HookValue"
                  }
                },
                "cvlRange": {
                  "#class": "spec.cvlast.CVLRange.Range",
                  "specFile": "certora/spec/ERC20.spec",
                  "start": {
                    "line": 136,
                    "character": 4
                  },
                  "end": {
                    "line": 136,
                    "character": 62
                  }
                }
              },
              "twoStateIndex": "NEITHER"
            },
            "tag": {
              "scope": {
                "scopeStack": [
                  {
                    "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                  },
                  {
                    "#class": "spec.cvlast.CVLScope.Item.HookScopeItem",
                    "scopeId": 11
                  }
                ],
                "innerScope": {
                  "scopeStack": [
                    {
                      "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                    }
                  ],
                  "innerScope": {
                    "scopeStack": [
                    ],
                    "innerScope": null
                  }
                }
              },
              "type": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Mathint"
              },
              "cvlRange": {
                "#class": "spec.cvlast.CVLRange.Range",
                "specFile": "certora/spec/ERC20.spec",
                "start": {
                  "line": 136,
                  "character": 22
                },
                "end": {
                  "line": 136,
                  "character": 49
                }
              }
            }
          },
          "r": {
            "#class": "spec.cvlast.CVLExp.VariableExp",
            "id": "old_value",
            "tag": {
              "scope": {
                "scopeStack": [
                  {
                    "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                  },
                  {
                    "#class": "spec.cvlast.CVLScope.Item.HookScopeItem",
                    "scopeId": 11
                  }
                ],
                "innerScope": {
                  "scopeStack": [
                    {
                      "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                    }
                  ],
                  "innerScope": {
                    "scopeStack": [
                    ],
                    "innerScope": null
                  }
                }
              },
              "type": {
                "#class": "spec.cvlast.CVLType.VM",
                "descriptor": {
                  "#class": "ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK",
                  "bitwidth": 256
                },
                "context": {
                  "#class": "spec.cvlast.typedescriptors.FromVMContext.HookValue"
                }
              },
              "cvlRange": {
                "#class": "spec.cvlast.CVLRange.Range",
                "specFile": "certora/spec/ERC20.spec",
                "start": {
                  "line": 136,
                  "character": 4
                },
                "end": {
                  "line": 136,
                  "character": 62
                }
              }
            },
            "twoStateIndex": "NEITHER"
          },
          "tag": {
            "scope": {
              "scopeStack": [
                {
                  "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                },
                {
                  "#class": "spec.cvlast.CVLScope.Item.HookScopeItem",
                  "scopeId": 11
                }
              ],
              "innerScope": {
                "scopeStack": [
                  {
                    "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                  }
                ],
                "innerScope": {
                  "scopeStack": [
                  ],
                  "innerScope": null
                }
              }
            },
            "type": {
              "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Mathint"
            },
            "cvlRange": {
              "#class": "spec.cvlast.CVLRange.Range",
              "specFile": "certora/spec/ERC20.spec",
              "start": {
                "line": 136,
                "character": 22
              },
              "end": {
                "line": 136,
                "character": 61
              }
            }
          }
        },
        "o1": {
          "out": {
            "#class": "vc.data.TACSymbol.Var.Full",
            "namePrefix": "I181",
            "tag": {
              "#class": "tac.Tag.Int"
            },
            "callIndex": 0
          },
          "exp": {
            "#class": "spec.cvlast.CVLExp.BinaryExp.AddExp",
            "l": {
              "#class": "spec.cvlast.CVLExp.VariableExp",
              "id": "sum_of_balances",
              "tag": {
                "scope": {
                  "scopeStack": [
                    {
                      "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                    },
                    {
                      "#class": "spec.cvlast.CVLScope.Item.HookScopeItem",
                      "scopeId": 11
                    }
                  ],
                  "innerScope": {
                    "scopeStack": [
                      {
                        "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                      }
                    ],
                    "innerScope": {
                      "scopeStack": [
                      ],
                      "innerScope": null
                    }
                  }
                },
                "type": {
                  "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Mathint"
                },
                "cvlRange": {
                  "#class": "spec.cvlast.CVLRange.Range",
                  "specFile": "certora/spec/ERC20.spec",
                  "start": {
                    "line": 136,
                    "character": 4
                  },
                  "end": {
                    "line": 136,
                    "character": 62
                  }
                }
              },
              "twoStateIndex": "NEITHER"
            },
            "r": {
              "#class": "spec.cvlast.CVLExp.VariableExp",
              "id": "new_value",
              "tag": {
                "scope": {
                  "scopeStack": [
                    {
                      "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                    },
                    {
                      "#class": "spec.cvlast.CVLScope.Item.HookScopeItem",
                      "scopeId": 11
                    }
                  ],
                  "innerScope": {
                    "scopeStack": [
                      {
                        "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                      }
                    ],
                    "innerScope": {
                      "scopeStack": [
                      ],
                      "innerScope": null
                    }
                  }
                },
                "type": {
                  "#class": "spec.cvlast.CVLType.VM",
                  "descriptor": {
                    "#class": "ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK",
                    "bitwidth": 256
                  },
                  "context": {
                    "#class": "spec.cvlast.typedescriptors.FromVMContext.HookValue"
                  }
                },
                "cvlRange": {
                  "#class": "spec.cvlast.CVLRange.Range",
                  "specFile": "certora/spec/ERC20.spec",
                  "start": {
                    "line": 136,
                    "character": 4
                  },
                  "end": {
                    "line": 136,
                    "character": 62
                  }
                }
              },
              "twoStateIndex": "NEITHER"
            },
            "tag": {
              "scope": {
                "scopeStack": [
                  {
                    "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                  },
                  {
                    "#class": "spec.cvlast.CVLScope.Item.HookScopeItem",
                    "scopeId": 11
                  }
                ],
                "innerScope": {
                  "scopeStack": [
                    {
                      "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                    }
                  ],
                  "innerScope": {
                    "scopeStack": [
                    ],
                    "innerScope": null
                  }
                }
              },
              "type": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Mathint"
              },
              "cvlRange": {
                "#class": "spec.cvlast.CVLRange.Range",
                "specFile": "certora/spec/ERC20.spec",
                "start": {
                  "line": 136,
                  "character": 22
                },
                "end": {
                  "line": 136,
                  "character": 49
                }
              }
            }
          }
        },
        "o2": {
          "out": {
            "#class": "vc.data.TACSymbol.Var.Full",
            "namePrefix": "I182",
            "tag": {
              "#class": "tac.Tag.Int"
            },
            "callIndex": 0
          },
          "exp": {
            "#class": "spec.cvlast.CVLExp.VariableExp",
            "id": "old_value",
            "tag": {
              "scope": {
                "scopeStack": [
                  {
                    "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                  },
                  {
                    "#class": "spec.cvlast.CVLScope.Item.HookScopeItem",
                    "scopeId": 11
                  }
                ],
                "innerScope": {
                  "scopeStack": [
                    {
                      "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                    }
                  ],
                  "innerScope": {
                    "scopeStack": [
                    ],
                    "innerScope": null
                  }
                }
              },
              "type": {
                "#class": "spec.cvlast.CVLType.VM",
                "descriptor": {
                  "#class": "ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK",
                  "bitwidth": 256
                },
                "context": {
                  "#class": "spec.cvlast.typedescriptors.FromVMContext.HookValue"
                }
              },
              "cvlRange": {
                "#class": "spec.cvlast.CVLRange.Range",
                "specFile": "certora/spec/ERC20.spec",
                "start": {
                  "line": 136,
                  "character": 4
                },
                "end": {
                  "line": 136,
                  "character": 62
                }
              }
            },
            "twoStateIndex": "NEITHER"
          }
        }
      }
    },
    {
      "key": {
        "name": "cvl.range",
        "type": "spec.cvlast.CVLRange",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "spec.cvlast.CVLRange.Range",
        "specFile": "certora/spec/ERC20.spec",
        "start": {
          "line": 136,
          "character": 4
        },
        "end": {
          "line": 136,
          "character": 62
        }
      }
    }
  ],
  "80": [
    {
      "key": {
        "name": "Tac.symbol.keyword",
        "type": "java.lang.String",
        "erasureStrategy": "Canonical"
      },
      "value": "L"
    },
    {
      "key": {
        "name": "tac.stack.height",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 1023
    }
  ]
}