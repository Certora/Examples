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
		CANON98:JSON{"name":"CANON98","paramSorts":[],"returnSort":{"#class":"tac.Tag.Int"},"attribute":"Ghost","cvlResultType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Mathint"},"cvlParamTypes":[],"declarationName":"CANON98"}
		I4:JSON{"name":"I4","paramSorts":[],"returnSort":{"#class":"tac.Tag.Int"},"attribute":"Ghost","cvlResultType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Mathint"},"cvlParamTypes":[],"declarationName":"CANON98"}
	}
	tacM0x20@1:bv256
	tacM0x20@3:bv256
	tacCaller@2:bv256
	tacM0x0!!44:bv256
	tacM0x0!!47:bv256
	tacM0x0!!78:bv256
	tacM0x0!!81:bv256
	tacAddress!!27:bv256
	tacAddress!!61:bv256
	CANON122!!165:bool
	tacOrigin!!129:bv256
	tacCallvalue@2:bv256
	lastReverted:bool
	lastReverted@1:bool
	lastReverted@2:bool
	lastReverted@3:bool
	tacM0x0!!179:bv256
	tacExtcodesize!!0:wordmap
	CANON28!!2:wordmap
	CANON89!!3:wordmap
	tacCalldatasize@1:bv256
	tacCalldatasize@2:bv256
	tacCalldatasize@3:bv256
	tacCalldatasize!!112:bv256
	tacM0x0@1:bv256
	tacM0x0@2:bv256
	tacM0x0@3:bv256
	tacExtcodesize:wordmap
	CANON100:int
	CANON101:int
	CANON102:int
	CANON103:int
	CANON104:bool
	CANON105:bool
	CANON106:bool
	CANON107:bv256
	CANON108:bool
	CANON109:bool
	CANON110:bv256
	CANON111:bool
	CANON112:bool
	CANON113:bool
	CANON114:int
	CANON115:int
	CANON116:int
	CANON117:bool
	CANON118:int
	CANON119:int
	CANON120:bool
	CANON122:bool
	CANON123:int
	CANON124:int
	CANON125:bool
	CANON126:bool
	CANON127:bool
	CANON128:bool
	CANON129:bool
	tacSighash!!6:bv256
	tacSighash!!7:bv256
	tacSighash!!8:bv256
	tacCalldatasize!!18:bv256
	tacCalldatasize!!52:bv256
	tacMCANON0@2:bytemap
	tacBalance:wordmap
	tacTimestamp!!139:bv256
	tacNumber@2:bv256
	tacBalance!!1:wordmap
	B9:bool
	I4:int
	R5:bv256
	B10:bool
	B11:bool
	B13:bool
	B14:bool
	B15:bool
	B19:bool
	B20:bool
	B21:bool
	B23:bool
	B24:bool
	B26:bool
	B29:bool
	B30:bool
	B31:bool
	B32:bool
	B33:bool
	B34:bool
	B35:bool
	B36:bool
	B38:bool
	B40:bool
	B42:bool
	B53:bool
	B54:bool
	B55:bool
	B57:bool
	B58:bool
	B60:bool
	B63:bool
	B64:bool
	B65:bool
	B66:bool
	B67:bool
	B68:bool
	B69:bool
	B70:bool
	B72:bool
	B74:bool
	B76:bool
	B86:bool
	B87:bool
	B88:bool
	B89:bool
	B90:bool
	B91:bool
	B92:bool
	B93:bool
	I16:int
	I17:int
	I94:int
	I95:int
	I96:int
	I97:int
	I98:int
	R12:bv256
	R22:bv256
	R25:bv256
	R28:bv256
	R37:bv256
	R39:bv256
	R41:bv256
	R43:bv256
	R45:(uninterp) skey
	R46:bv256
	R49:(uninterp) skey
	R50:bv256
	R51:bv256
	R56:bv256
	R59:bv256
	R62:bv256
	R71:bv256
	R73:bv256
	R75:bv256
	R77:bv256
	R79:(uninterp) skey
	R80:bv256
	R83:(uninterp) skey
	R84:bv256
	R85:bv256
	R99:bv256
	B101:bool
	B106:bool
	B109:bool
	B113:bool
	B114:bool
	B116:bool
	B119:bool
	B121:bool
	B124:bool
	B127:bool
	B130:bool
	B132:bool
	B135:bool
	B137:bool
	B140:bool
	B142:bool
	B145:bool
	B154:bool
	B161:bool
	B168:bool
	B171:bool
	B172:bool
	B173:bool
	B174:bool
	B175:bool
	B176:bool
	B177:bool
	B182:bool
	I100:int
	I105:int
	I110:int
	I111:int
	I115:int
	I120:int
	I126:int
	I131:int
	I136:int
	I141:int
	I144:int
	I150:int
	I159:int
	I160:int
	I162:int
	I163:int
	I166:int
	I167:int
	I183:int
	I184:int
	I185:int
	I188:int
	I189:int
	R102:bv256
	R103:bv256
	R104:bv256
	R107:bv256
	R108:bv256
	R117:bv256
	R122:bv256
	R128:bv256
	R133:bv256
	R138:bv256
	R143:bv256
	R146:bv256
	R147:bv256
	R148:bv256
	R149:bv256
	R152:bv256
	R153:bv256
	R170:bv256
	R178:bv256
	R180:(uninterp) skey
	R181:bv256
	R186:bv256
	R187:bv256
	lastHasThrown!!156:bool
	lastHasThrown!!158:bool
	lastHasThrown!!191:bool
	CANON129!!169:bool
	tacAddress@1:bv256
	tacAddress@2:bv256
	tacAddress@3:bv256
	lastReverted!!155:bool
	lastReverted!!157:bool
	lastReverted!!190:bool
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
	LCANON6@1:bool
	LCANON6@3:bool
	LCANON7@1:bv256
	LCANON7@3:bv256
	LCANON8@1:bv256
	LCANON8@3:bv256
	LCANON9@1:bool
	LCANON9@3:bool
	tacCallvalue!!123:bv256
	tacOrigin@2:bv256
	CANON10:bool
	CANON11:bool
	CANON12:int
	CANON13:int
	CANON14:int
	CANON15:int
	CANON16:bool
	CANON17:bool
	CANON18:bool
	CANON19:bv256
	CANON20:bool
	CANON21:bool
	CANON22:bv256
	CANON23:bool
	CANON24@1:bv256
	CANON24@2:bv256
	CANON24@3:bv256
	CANON25@1:bool
	CANON25@2:bool
	CANON25@3:bool
	CANON26:bool
	CANON27:bool
	CANON28:wordmap
	CANON33:int
	CANON34:int
	CANON35:int
	CANON36:int
	CANON37:int
	CANON38:int
	CANON39:int
	CANON40:int
	CANON41:int
	CANON42:int
	CANON43:int
	CANON44:int
	CANON45:int
	CANON46:int
	CANON47:bv256
	CANON48:bv256
	CANON49:int
	CANON50:bool
	CANON51:bv256
	CANON52:bv256
	CANON53:bv256
	CANON54:int
	CANON55:bool
	CANON56:bv256
	CANON57:bv256
	CANON58:bool
	CANON59:bool
	CANON60:bool
	CANON61:int
	CANON62:bool
	CANON63:bv256
	CANON64:int
	CANON65:bool
	CANON66:bv256
	CANON67:int
	CANON68:bool
	CANON69:bv256
	CANON70:int
	CANON71:bool
	CANON72:bv256
	CANON73:int
	CANON74:bool
	CANON75:bv256
	CANON76:int
	CANON77:bool
	CANON78:bv256
	CANON79:int
	CANON80:bool
	CANON81:bv256
	CANON82:bv256
	CANON83:bv256
	CANON84:bv256
	CANON85:int
	CANON86:bv256
	CANON87:bv256
	CANON88:bool
	CANON89:wordmap
	CANON92:bool
	CANON93:int
	CANON94:int
	CANON95:int
	CANON96:bv256
	CANON97:int
	CANON98:int
	CANON99:int
	LCANON10@1:bv256
	LCANON10@3:bv256
	LCANON11@1:bv256
	LCANON11@3:bv256
	LCANON12@1:bool
	LCANON12@3:bool
	LCANON13@1:bv256
	LCANON13@3:bv256
	LCANON14@1:bv256
	LCANON14@3:bv256
	LCANON15@1:bool
	LCANON15@3:bool
	LCANON16@1:bv256
	LCANON16@3:bv256
	LCANON17@1:bv256
	LCANON17@3:bv256
	LCANON18@1:bv256
	LCANON18@3:bv256
	LCANON19@1:bv256
	LCANON19@3:bv256
	LCANON20@1:bv256
	LCANON20@3:bv256
	LCANON21@1:bv256
	LCANON21@3:bv256
	LCANON22@1:bv256
	LCANON22@3:bv256
	LCANON23@1:bv256
	LCANON23@3:bv256
	LCANON24@2:bv256
	LCANON25@2:bv256
	LCANON26@2:bv256
	LCANON27@2:bv256
	LCANON28@2:bv256
	LCANON29@2:bv256
	LCANON30@2:bool
	LCANON31@2:bv256
	tacContractAtCANON0:bv256
	tacM0x20!!48:bv256
	tacM0x20!!82:bv256
	CANON120!!164:bool
	lastHasThrown:bool
	lastHasThrown@1:bool
	lastHasThrown@2:bool
	lastHasThrown@3:bool
	tacAddress!!125:bv256
	CANON0:int
	CANON1:bool
	CANON2:bool
	CANON3:bool
	CANON4:int
	CANON5:bool
	CANON6:bool
	CANON7:bool
	CANON8:bool
	CANON9:bv256
	tacCaller!!118:bv256
	tacBalance!!151:wordmap
	tacTimestamp@2:bv256
	tacSighash@1:bv256
	tacSighash@2:bv256
	tacSighash@3:bv256
	tacNumber!!134:bv256
}
Program {
	Block 0_0_0_0_0_0 Succ [0_0_0_1_0_0] {
		AssignHavocCmd tacExtcodesize!!0:0
		AssignHavocCmd tacBalance!!1:1
		AssignHavocCmd CANON12:2
		AssignHavocCmd CANON13:3
		AssignHavocCmd CANON28!!2:4
		AssignHavocCmd CANON34:5
		AssignHavocCmd CANON35:6
		AssignHavocCmd CANON36:7
		AssignHavocCmd CANON37:8
		AssignHavocCmd CANON38:9
		AssignHavocCmd CANON39:10
		AssignHavocCmd CANON40:11
		AssignHavocCmd CANON41:12
		AssignHavocCmd CANON48:13
		AssignHavocCmd CANON89!!3:14
		AssignHavocCmd R5:15
		AssignHavocCmd tacSighash!!6:16
		AssignHavocCmd tacSighash!!7:16
		AssignHavocCmd tacSighash!!8:16
		AssignExpCmd CANON0:17 0xd0e30db0
		AssignExpCmd CANON1:18 false
		AssignExpCmd CANON2:19 false
		AssignExpCmd CANON3:20 true
		AssignExpCmd CANON4:21 0x0
		AssignExpCmd CANON5:22 false
		AnnotationCmd JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Message","s":"Setup"}}
		AnnotationCmd JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Message","s":"multi contract setup"}}
		AnnotationCmd JSON{"key":{"name":"cvl.label.end","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		AnnotationCmd JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Message","s":"rule parameters setup"}}
		AnnotationCmd JSON{"key":{"name":"cvl.label.end","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		AnnotationCmd JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Message","s":"contract address vars initialized"}}
		AnnotationCmd JSON{"key":{"name":"cvl.label.end","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		AnnotationCmd JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Message","s":"setup read tracking instrumentation"}}
		AnnotationCmd JSON{"key":{"name":"cvl.label.end","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		AnnotationCmd JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Message","s":"last storage initialize"}}
		AnnotationCmd JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageGlobalChangeSnippet.StorageTakeSnapshot","lhs":{"namePrefix":"lastStorage","tag":{"#class":"tac.Tag.BlockchainState"},"callIndex":0,"meta":[{"key":{"name":"cvl.local","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true},{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"lastStorage"},{"key":{"name":"cvl.type","type":"spec.cvlast.CVLType$PureCVLType","erasureStrategy":"CallTrace"},"value":{"#class":"spec.cvlast.CVLType.PureCVLType.VMInternal.BlockchainState"}},{"key":{"name":"cvl","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true},{"key":{"name":"cvl.display","type":"java.lang.String","erasureStrategy":"CallTrace"},"value":"lastStorage"}]}}}
		AnnotationCmd JSON{"key":{"name":"cvl.label.end","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		AnnotationCmd JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Message","s":"assumptions about extcodesize"}}
		AssignExpCmd B9:23 Gt(Select(tacExtcodesize!!0:0 Apply(to_skey:bif R5:15) ) 0x0 )
		AssumeCmd B9:23
		AnnotationCmd JSON{"key":{"name":"cvl.label.end","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		AnnotationCmd JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Message","s":"assumptions about contracts' addresses"}}
		NopCmd
		AssumeExpCmd Gt(R5:15 0x0 )
		NopCmd
		AssumeExpCmd Le(R5:15 0xffffffffffffffffffffffffffffffffffffffff )
		AnnotationCmd JSON{"key":{"name":"cvl.label.end","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		AnnotationCmd JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Message","s":"assumptions about starting balances"}}
		AssignExpCmd R12:23 Select(tacBalance!!1:1 Apply(to_skey:bif R5:15) )
		NopCmd
		AssumeExpCmd Ge(R12:23 0x0 )
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
		NopCmd
		AssumeExpCmd LAnd(Le(CANON12:2 0xffffffffffffffffffffffffffffffffffffffff ) Ge(CANON12:2 0x0 ) )
		NopCmd
		AssumeExpCmd LAnd(Le(CANON13:3 0xffffffffffffffffffffffffffffffffffffffff ) Ge(CANON13:3 0x0 ) )
		AnnotationCmd:24 JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Cmd","cmd":{"cmd_type":"spec.cvlast.CVLCmd.Simple.Definition","cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/spec/ERC20.spec","start":{"line":96,"character":4},"end":{"line":96,"character":58}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Mathint"},"idL":[{"#class":"spec.cvlast.CVLLhs.Id","cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/spec/ERC20.spec","start":{"line":96,"character":4},"end":{"line":96,"character":28}},"id":"allowance_before","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":6}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Mathint"},"cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/spec/ERC20.spec","start":{"line":96,"character":4},"end":{"line":96,"character":58}}}}],"exp":{"#class":"spec.cvlast.CVLExp.ApplyExp.ContractFunction.Concrete","methodIdWithCallContext":{"#class":"spec.cvlast.ConcreteMethod","signature":{"#class":"spec.cvlast.ExternalQualifiedMethodSignature.ExternalQualifiedMethodSig","wrapped":{"#class":"spec.cvlast.QualifiedMethodSignature.QualifiedMethodSig","qualifiedMethodName":{"#class":"spec.cvlast.QualifiedFunction","host":{"name":"ERC20"},"methodId":"allowance"},"params":[{"#class":"spec.cvlast.VMParam.Named","name":"owner","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$address"}},{"#class":"spec.cvlast.VMParam.Named","name":"spender","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$address"}}],"res":[{"#class":"spec.cvlast.VMParam.Unnamed","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256}}]},"sighashInt":{"n":"dd62ed3e"}}},"args":[{"#class":"spec.cvlast.CVLExp.VariableExp","id":"holder","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":6}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"},"cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/spec/ERC20.spec","start":{"line":96,"character":4},"end":{"line":96,"character":58}}},"twoStateIndex":"NEITHER"},{"#class":"spec.cvlast.CVLExp.VariableExp","id":"spender","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":6}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"},"cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/spec/ERC20.spec","start":{"line":96,"character":4},"end":{"line":96,"character":58}}},"twoStateIndex":"NEITHER"}],"noRevert":true,"storage":{"#class":"spec.cvlast.CVLExp.VariableExp","id":"lastStorage","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":6}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.VMInternal.BlockchainState"},"cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/spec/ERC20.spec","start":{"line":96,"character":4},"end":{"line":96,"character":58}}},"twoStateIndex":"NEITHER"},"isWhole":false,"tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":6}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.VM","descriptor":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256},"context":{"#class":"spec.cvlast.typedescriptors.FromVMContext.ReturnValue"}},"cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/spec/ERC20.spec","start":{"line":96,"character":31},"end":{"line":96,"character":40}},"annotation":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.CallResolution$DirectPassing","target":{"methodSignature":{"#class":"spec.cvlast.ExternalQualifiedMethodSignature.ExternalQualifiedMethodSig","wrapped":{"#class":"spec.cvlast.QualifiedMethodSignature.QualifiedMethodSig","qualifiedMethodName":{"#class":"spec.cvlast.QualifiedFunction","host":{"name":"ERC20"},"methodId":"allowance"},"params":[{"#class":"spec.cvlast.VMParam.Named","name":"owner","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$address"}},{"#class":"spec.cvlast.VMParam.Named","name":"spender","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$address"}}],"res":[{"#class":"spec.cvlast.VMParam.Unnamed","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256}}]},"sighashInt":{"n":"dd62ed3e"}},"definitelyNonPayable":true,"annotation":{"visibility":"EXTERNAL","envFree":true,"library":false},"stateMutability":"view","tag":{"#class":"spec.cvlast.CVLImportedFunctionTag.WithMethodInfo","evmMethodInfo":{"sigHash":"dd62ed3e","name":"allowance","argTypes":[{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.address"},{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.address"}],"resultTypes":[{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256}],"stateMutability":"view","envfreeInfo":{"#class":"bridge.EnvfreeInfo.Unknown"},"isConstant":false,"paramNames":["owner","spender"],"isLibrary":false}}},"hasEnv":false}}},"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":6}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}}}}}
		AssignExpCmd:25 I16 CANON12:2
		AssignExpCmd:26 I17 CANON13:3
	}
	Block 0_0_0_1_0_0 Succ [1_0_0_0_0_0] {
		AnnotationCmd:24 JSON{"key":{"name":"call.trace.push","type":"analysis.icfg.Inliner$CallStack$PushRecord","erasureStrategy":"Canonical"},"value":"rO0ABXNyACphbmFseXNpcy5pY2ZnLklubGluZXIkQ2FsbFN0YWNrJFB1c2hSZWNvcmSX8+DCTLCH+AIAA0kACGNhbGxlZUlkTAAGY2FsbGVldAATTHZjL2RhdGEvTWV0aG9kUmVmO0wAB3N1bW1hcnl0ABVMdmMvZGF0YS9DYWxsU3VtbWFyeTt4cAAAAAFzcgARdmMuZGF0YS5NZXRob2RSZWbJlJTzzU9pGAIAA0wABGF0dHJ0ABdMc2NlbmUvTWV0aG9kQXR0cmlidXRlO0wACmNvbnRyYWN0SWR0ABZMamF2YS9tYXRoL0JpZ0ludGVnZXI7TAAHc2lnSGFzaHQAEExldm0vU2lnaGFzaEludDt4cHNyABxzY2VuZS5NZXRob2RBdHRyaWJ1dGUkQ29tbW9uNHjdebdr9XMCAAB4cgAVc2NlbmUuTWV0aG9kQXR0cmlidXRlcYg2pYWutuUCAAB4cHNyABRqYXZhLm1hdGguQmlnSW50ZWdlcoz8nx+pO/sdAwAGSQAIYml0Q291bnRJAAliaXRMZW5ndGhJABNmaXJzdE5vbnplcm9CeXRlTnVtSQAMbG93ZXN0U2V0Qml0SQAGc2lnbnVtWwAJbWFnbml0dWRldAACW0J4cgAQamF2YS5sYW5nLk51bWJlcoaslR0LlOCLAgAAeHD///////////////7////+AAAAAXVyAAJbQqzzF/gGCFTgAgAAeHAAAAAQzkYEoAAAAAAAAAAAAAAAA3hzcgAOZXZtLlNpZ2hhc2hJbnRUdcqNMXEgeAIAAUwAAW5xAH4ABnhwc3EAfgAM///////////////+/////gAAAAF1cQB+ABAAAAAE3WLtPnhw"}
		AssignHavocCmd:24 tacCalldatasize!!18:27
		NopCmd
		AssumeExpCmd Apply(add_noofl:bif 0x4 0x40)
		NopCmd
		AssumeExpCmd Apply(add_noofl:bif 0x4 0x0)
		AssignExpCmd:24 B21 LAnd(Ge(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff I16 ) Le(0x0 I16 ) )
		AssertCmd:24 B21 "sanity bounds check on cvl to vm encoding of certoraArg14071410:int failed"
		AssignExpCmd:24 R22 Apply(safe_math_narrow:bif I16)
		NopCmd
		AssumeExpCmd Apply(add_noofl:bif 0x4 0x20)
		AssignExpCmd:24 B24 LAnd(Ge(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff I17 ) Le(0x0 I17 ) )
		AssertCmd:24 B24 "sanity bounds check on cvl to vm encoding of certoraArg14111412:int failed"
		AssignExpCmd:24 R25 Apply(safe_math_narrow:bif I17)
		NopCmd
		AssumeExpCmd Eq(0x44 tacCalldatasize!!18:27 )
		LabelCmd:24 "Start procedure ERC20-allowance(address,address)"
		AnnotationCmd:24 JSON{"key":{"name":"fps.free-pointer-is-scalarized","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true}
		AssignExpCmd:24 R28:23 Select(tacExtcodesize!!0:0 Apply(to_skey:bif R5:28) )
		NopCmd
		AssumeExpCmd Gt(R28:23 0x0 )
		AnnotationCmd:24 JSON{"key":{"name":"internal.func.finder.info","type":"analysis.ip.InternalFunctionFinderReport","erasureStrategy":"Erased"},"value":"rO0ABXNyAChhbmFseXNpcy5pcC5JbnRlcm5hbEZ1bmN0aW9uRmluZGVyUmVwb3J0ian+bYn1VdACAAFMABN1bnJlc29sdmVkRnVuY3Rpb25zdAAPTGphdmEvdXRpbC9TZXQ7eHBzcgAhZGF0YXN0cnVjdHVyZXMuTGlua2VkQXJyYXlIYXNoU2V0AAAAAAAAAAEDAAJGAApsb2FkRmFjdG9yTAAJaGFzaFRhYmxldAAuTGRhdGFzdHJ1Y3R1cmVzL2FycmF5aGFzaHRhYmxlL0FycmF5SGFzaFRhYmxlO3hwdwgAAAAAQAAAAHg="}
		AnnotationCmd:24 JSON{"key":{"name":"fps.free-pointer-is-scalarized","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true}
		NopCmd
		AssumeExpCmd LNot(Lt(tacCalldatasize!!18:27 0x4 ) )
		NopCmd
		AssumeExpCmd LNot(Gt(0x70a08231 tacSighash!!6:16 ) )
		NopCmd
		AssumeExpCmd LNot(Gt(0xa9059cbb tacSighash!!6:16 ) )
		NopCmd
		AssumeExpCmd LNot(Eq(0xa9059cbb tacSighash!!6:16 ) )
		NopCmd
		AssumeExpCmd LNot(Eq(0xb2bdfa7b tacSighash!!6:16 ) )
		NopCmd
		AssumeExpCmd LNot(Eq(0xd0e30db0 tacSighash!!6:16 ) )
		NopCmd
		AssumeExpCmd Eq(0xdd62ed3e tacSighash!!6:16 )
		AssumeCmd:29 true
		AssignExpCmd:30 R37:31 Sub(tacCalldatasize!!18:27 0x4 )
		NopCmd
		AssumeExpCmd LNot(Slt(R37:31 0x40 ) )
		NopCmd
		AssumeExpCmd Le(R22 0xffffffffffffffffffffffffffffffffffffffff )
		NopCmd
		AssumeExpCmd Le(R25 0xffffffffffffffffffffffffffffffffffffffff )
		AnnotationCmd:24 JSON{"key":{"name":"internal.func.start","type":"analysis.ip.InternalFuncStartAnnotation","erasureStrategy":"CallTrace"},"value":{"id":0,"startPc":4858,"args":[{"s":{"namePrefix":"R22","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1012}]},"offset":1,"sort":"SCALAR"},{"s":{"namePrefix":"R25","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1012}]},"offset":2,"sort":"SCALAR"}],"methodSignature":{"#class":"spec.cvlast.QualifiedMethodSignature.QualifiedMethodSig","qualifiedMethodName":{"#class":"spec.cvlast.QualifiedFunction","host":{"name":"ERC20"},"methodId":"allowance"},"params":[{"#class":"spec.cvlast.VMParam.Named","name":"owner","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$address"}},{"#class":"spec.cvlast.VMParam.Named","name":"spender","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$address"}}],"res":[{"#class":"spec.cvlast.VMParam.Unnamed","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256}}]},"stackOffsetToArgPos":{"1":0,"2":1},"callSiteSrc":{"source":0,"begin":5647,"len":535,"jumpType":"ENTER","address":"ce4604a0000000000000000000000003","sourceContext":{"indexToFilepath":{"0":"contracts/ERC20.sol","1":"contracts/IERC20.sol","2":"contracts/IERC20Metadata.sol"},"sourceDir":".post_autofinders.0"}}}}
		AssignExpCmd:32 R45:33 Apply(hash_3_keccak:bif Apply(skey_basic:bif 0x40) Apply(to_skey:bif R22:34) Apply(skey_basic:bif 0x1))
		AssignExpCmd:35 R49:33 Apply(hash_3_keccak:bif Apply(skey_basic:bif 0x40) Apply(to_skey:bif R25:34) R45:36)
		AssignExpCmd:37 R50:33 Select(CANON28!!2:4 R49:38 )
		AnnotationCmd:24 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet","value":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R50","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1019}]},"displayPath":{"#class":"analysis.storage.DisplayPath.MapAccess","key":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R25","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1017}]},"keyTyp":{"#class":"tac.TACStorageType.IntegralType","typeLabel":"address","numBytes":"14","descriptor":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$address"},"lowerBound":null,"upperBound":null},"base":{"#class":"analysis.storage.DisplayPath.MapAccess","key":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R22","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1017}]},"keyTyp":{"#class":"tac.TACStorageType.IntegralType","typeLabel":"address","numBytes":"14","descriptor":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$address"},"lowerBound":null,"upperBound":null},"base":{"#class":"analysis.storage.DisplayPath.Root","name":"_allowances"}}},"storageType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256},"contractInstance":"ce4604a0000000000000000000000003","linkableStorageReadId":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet.None"}}}
		AnnotationCmd:24 JSON{"key":{"name":"internal.func.end","type":"analysis.ip.InternalFuncExitAnnotation","erasureStrategy":"Canonical"},"value":{"id":0,"rets":[{"s":{"namePrefix":"R50","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1023}]},"offset":0}],"functionLayout":{"0":{"#class":"analysis.ip.InternalFuncValueLocation.Scalar"}}}}
		AnnotationCmd:24 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.EVMFunctionReturnWrite","returnbufOffset":"0","returnValueSym":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R50","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1023}]},"callIndex":1}}
		AnnotationCmd:24 JSON{"key":{"name":"tac.return.path","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		LabelCmd:24 "End procedure ERC20-allowance(address,address)"
		AssignExpCmd:24 CANON33:39 R50:33
		AnnotationCmd:24 JSON{"key":{"name":"call.trace.pop","type":"analysis.icfg.Inliner$CallStack$PopRecord","erasureStrategy":"Canonical"},"value":"rO0ABXNyAClhbmFseXNpcy5pY2ZnLklubGluZXIkQ2FsbFN0YWNrJFBvcFJlY29yZPAPfwSLdCWJAgABSQAIY2FsbGVlSWR4cAAAAAE="}
	}
	Block 0_0_0_3_0_0 Succ [6_0_0_0_0_0] {
		AnnotationCmd:40 JSON{"key":{"name":"call.trace.push","type":"analysis.icfg.Inliner$CallStack$PushRecord","erasureStrategy":"Canonical"},"value":"rO0ABXNyACphbmFseXNpcy5pY2ZnLklubGluZXIkQ2FsbFN0YWNrJFB1c2hSZWNvcmSX8+DCTLCH+AIAA0kACGNhbGxlZUlkTAAGY2FsbGVldAATTHZjL2RhdGEvTWV0aG9kUmVmO0wAB3N1bW1hcnl0ABVMdmMvZGF0YS9DYWxsU3VtbWFyeTt4cAAAAANzcgARdmMuZGF0YS5NZXRob2RSZWbJlJTzzU9pGAIAA0wABGF0dHJ0ABdMc2NlbmUvTWV0aG9kQXR0cmlidXRlO0wACmNvbnRyYWN0SWR0ABZMamF2YS9tYXRoL0JpZ0ludGVnZXI7TAAHc2lnSGFzaHQAEExldm0vU2lnaGFzaEludDt4cHNyABxzY2VuZS5NZXRob2RBdHRyaWJ1dGUkQ29tbW9uNHjdebdr9XMCAAB4cgAVc2NlbmUuTWV0aG9kQXR0cmlidXRlcYg2pYWutuUCAAB4cHNyABRqYXZhLm1hdGguQmlnSW50ZWdlcoz8nx+pO/sdAwAGSQAIYml0Q291bnRJAAliaXRMZW5ndGhJABNmaXJzdE5vbnplcm9CeXRlTnVtSQAMbG93ZXN0U2V0Qml0SQAGc2lnbnVtWwAJbWFnbml0dWRldAACW0J4cgAQamF2YS5sYW5nLk51bWJlcoaslR0LlOCLAgAAeHD///////////////7////+AAAAAXVyAAJbQqzzF/gGCFTgAgAAeHAAAAAQzkYEoAAAAAAAAAAAAAAAA3hzcgAOZXZtLlNpZ2hhc2hJbnRUdcqNMXEgeAIAAUwAAW5xAH4ABnhwc3EAfgAM///////////////+/////gAAAAF1cQB+ABAAAAAE3WLtPnhw"}
		AssignHavocCmd:40 tacCalldatasize!!52:27
		NopCmd
		AssumeExpCmd Apply(add_noofl:bif 0x4 0x40)
		NopCmd
		AssumeExpCmd Apply(add_noofl:bif 0x4 0x0)
		AssignExpCmd:40 B55 LAnd(Ge(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff I110 ) Le(0x0 I110 ) )
		AssertCmd:40 B55 "sanity bounds check on cvl to vm encoding of certoraArg23342335:int failed"
		AssignExpCmd:40 R56 Apply(safe_math_narrow:bif I110)
		NopCmd
		AssumeExpCmd Apply(add_noofl:bif 0x4 0x20)
		AssignExpCmd:40 B58 LAnd(Ge(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff I111 ) Le(0x0 I111 ) )
		AssertCmd:40 B58 "sanity bounds check on cvl to vm encoding of certoraArg23362337:int failed"
		AssignExpCmd:40 R59 Apply(safe_math_narrow:bif I111)
		NopCmd
		AssumeExpCmd Eq(0x44 tacCalldatasize!!52:27 )
		LabelCmd:40 "Start procedure ERC20-allowance(address,address)"
		AnnotationCmd:40 JSON{"key":{"name":"fps.free-pointer-is-scalarized","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true}
		AssignExpCmd:40 R62:23 Select(tacExtcodesize!!0:0 Apply(to_skey:bif R5:28) )
		NopCmd
		AssumeExpCmd Gt(R62:23 0x0 )
		AnnotationCmd:40 JSON{"key":{"name":"internal.func.finder.info","type":"analysis.ip.InternalFunctionFinderReport","erasureStrategy":"Erased"},"value":"rO0ABXNyAChhbmFseXNpcy5pcC5JbnRlcm5hbEZ1bmN0aW9uRmluZGVyUmVwb3J0ian+bYn1VdACAAFMABN1bnJlc29sdmVkRnVuY3Rpb25zdAAPTGphdmEvdXRpbC9TZXQ7eHBzcgAhZGF0YXN0cnVjdHVyZXMuTGlua2VkQXJyYXlIYXNoU2V0AAAAAAAAAAEDAAJGAApsb2FkRmFjdG9yTAAJaGFzaFRhYmxldAAuTGRhdGFzdHJ1Y3R1cmVzL2FycmF5aGFzaHRhYmxlL0FycmF5SGFzaFRhYmxlO3hwdwgAAAAAQAAAAHg="}
		AnnotationCmd:40 JSON{"key":{"name":"fps.free-pointer-is-scalarized","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true}
		NopCmd
		AssumeExpCmd LNot(Lt(tacCalldatasize!!52:27 0x4 ) )
		NopCmd
		AssumeExpCmd LNot(Gt(0x70a08231 tacSighash!!8:16 ) )
		NopCmd
		AssumeExpCmd LNot(Gt(0xa9059cbb tacSighash!!8:16 ) )
		NopCmd
		AssumeExpCmd LNot(Eq(0xa9059cbb tacSighash!!8:16 ) )
		NopCmd
		AssumeExpCmd LNot(Eq(0xb2bdfa7b tacSighash!!8:16 ) )
		NopCmd
		AssumeExpCmd LNot(Eq(0xd0e30db0 tacSighash!!8:16 ) )
		NopCmd
		AssumeExpCmd Eq(0xdd62ed3e tacSighash!!8:16 )
		AssumeCmd:41 true
		AssignExpCmd:42 R71:31 Sub(tacCalldatasize!!52:27 0x4 )
		NopCmd
		AssumeExpCmd LNot(Slt(R71:31 0x40 ) )
		NopCmd
		AssumeExpCmd Le(R56 0xffffffffffffffffffffffffffffffffffffffff )
		NopCmd
		AssumeExpCmd Le(R59 0xffffffffffffffffffffffffffffffffffffffff )
		AnnotationCmd:40 JSON{"key":{"name":"internal.func.start","type":"analysis.ip.InternalFuncStartAnnotation","erasureStrategy":"CallTrace"},"value":{"id":1,"startPc":4858,"args":[{"s":{"namePrefix":"R56","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1012}]},"offset":1,"sort":"SCALAR"},{"s":{"namePrefix":"R59","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1012}]},"offset":2,"sort":"SCALAR"}],"methodSignature":{"#class":"spec.cvlast.QualifiedMethodSignature.QualifiedMethodSig","qualifiedMethodName":{"#class":"spec.cvlast.QualifiedFunction","host":{"name":"ERC20"},"methodId":"allowance"},"params":[{"#class":"spec.cvlast.VMParam.Named","name":"owner","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$address"}},{"#class":"spec.cvlast.VMParam.Named","name":"spender","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$address"}}],"res":[{"#class":"spec.cvlast.VMParam.Unnamed","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256}}]},"stackOffsetToArgPos":{"1":0,"2":1},"callSiteSrc":{"source":0,"begin":5647,"len":535,"jumpType":"ENTER","address":"ce4604a0000000000000000000000003","sourceContext":{"indexToFilepath":{"0":"contracts/ERC20.sol","1":"contracts/IERC20.sol","2":"contracts/IERC20Metadata.sol"},"sourceDir":".post_autofinders.0"}}}}
		AssignExpCmd:43 R79:33 Apply(hash_3_keccak:bif Apply(skey_basic:bif 0x40) Apply(to_skey:bif R56:34) Apply(skey_basic:bif 0x1))
		AssignExpCmd:44 R83:33 Apply(hash_3_keccak:bif Apply(skey_basic:bif 0x40) Apply(to_skey:bif R59:34) R79:36)
		AssignExpCmd:45 R84:33 Select(CANON28!!2:4 R83:46 )
		AnnotationCmd:40 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet","value":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R84","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1019}]},"displayPath":{"#class":"analysis.storage.DisplayPath.MapAccess","key":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R59","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1017}]},"keyTyp":{"#class":"tac.TACStorageType.IntegralType","typeLabel":"address","numBytes":"14","descriptor":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$address"},"lowerBound":null,"upperBound":null},"base":{"#class":"analysis.storage.DisplayPath.MapAccess","key":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R56","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1017}]},"keyTyp":{"#class":"tac.TACStorageType.IntegralType","typeLabel":"address","numBytes":"14","descriptor":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$address"},"lowerBound":null,"upperBound":null},"base":{"#class":"analysis.storage.DisplayPath.Root","name":"_allowances"}}},"storageType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256},"contractInstance":"ce4604a0000000000000000000000003","linkableStorageReadId":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet.None"}}}
		AnnotationCmd:40 JSON{"key":{"name":"internal.func.end","type":"analysis.ip.InternalFuncExitAnnotation","erasureStrategy":"Canonical"},"value":{"id":1,"rets":[{"s":{"namePrefix":"R84","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1023}]},"offset":0}],"functionLayout":{"0":{"#class":"analysis.ip.InternalFuncValueLocation.Scalar"}}}}
		AnnotationCmd:40 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.EVMFunctionReturnWrite","returnbufOffset":"0","returnValueSym":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R84","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1023}]},"callIndex":3}}
		AnnotationCmd:40 JSON{"key":{"name":"tac.return.path","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		LabelCmd:40 "End procedure ERC20-allowance(address,address)"
		AssignExpCmd:40 CANON114:47 R84:33
		AnnotationCmd:40 JSON{"key":{"name":"call.trace.pop","type":"analysis.icfg.Inliner$CallStack$PopRecord","erasureStrategy":"Canonical"},"value":"rO0ABXNyAClhbmFseXNpcy5pY2ZnLklubGluZXIkQ2FsbFN0YWNrJFBvcFJlY29yZPAPfwSLdCWJAgABSQAIY2FsbGVlSWR4cAAAAAM="}
	}
	Block 1_0_0_0_0_0 Succ [2_0_0_0_0_0, 3_0_0_0_0_0] {
		AssumeNotCmd:24 false
		AssumeNotCmd:24 false
		AnnotationCmd JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageGlobalChangeSnippet.StorageTakeSnapshot","lhs":{"namePrefix":"lastStorage","tag":{"#class":"tac.Tag.BlockchainState"},"callIndex":0,"meta":[{"key":{"name":"cvl.local","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true},{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"lastStorage"},{"key":{"name":"cvl.type","type":"spec.cvlast.CVLType$PureCVLType","erasureStrategy":"CallTrace"},"value":{"#class":"spec.cvlast.CVLType.PureCVLType.VMInternal.BlockchainState"}},{"key":{"name":"cvl","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true},{"key":{"name":"cvl.display","type":"java.lang.String","erasureStrategy":"CallTrace"},"value":"lastStorage"}]}}}
		AnnotationCmd:24 JSON{"key":{"name":"cvl.label.end","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		NopCmd
		AssumeExpCmd LAnd(Le(CANON34:5 0xffffffffffffffffffffffffffffffffffffffff ) Ge(CANON34:5 0x0 ) )
		NopCmd
		AssumeExpCmd LAnd(Le(CANON35:6 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff ) Ge(CANON35:6 0x0 ) )
		NopCmd
		AssumeExpCmd LAnd(Le(CANON36:7 0xffffffffffffffffffffffffffffffffffffffff ) Ge(CANON36:7 0x0 ) )
		NopCmd
		AssumeExpCmd LAnd(Le(CANON37:8 0xffffffffffffffffffffffffffffffffffffffff ) Ge(CANON37:8 0x0 ) )
		NopCmd
		AssumeExpCmd LAnd(Le(CANON38:9 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff ) Ge(CANON38:9 0x0 ) )
		NopCmd
		AssumeExpCmd LAnd(Le(CANON39:10 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff ) Ge(CANON39:10 0x0 ) )
		NopCmd
		AssumeExpCmd LAnd(Le(CANON40:11 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff ) Ge(CANON40:11 0x0 ) )
		NopCmd
		AssumeExpCmd LAnd(Le(CANON41:12 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff ) Ge(CANON41:12 0x0 ) )
		AnnotationCmd:48 JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Cmd","cmd":{"cmd_type":"spec.cvlast.CVLCmd.Simple.Apply","cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/spec/ERC20.spec","start":{"line":99,"character":4},"end":{"line":99,"character":15}},"exp":{"#class":"spec.cvlast.CVLExp.ApplyExp.ContractFunction.Symbolic","methodIdWithCallContext":{"#class":"spec.cvlast.ParametricMethod","methodId":"f","host":{"name":"ERC20"}},"args":[{"#class":"spec.cvlast.CVLExp.VariableExp","id":"e","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":6}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"env","fields":[{"fieldName":"msg","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"msg","fields":[{"fieldName":"sender","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"value","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}}]}},{"fieldName":"tx","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"tx","fields":[{"fieldName":"origin","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}}]}},{"fieldName":"block","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"block","fields":[{"fieldName":"coinbase","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"difficulty","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"gaslimit","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"number","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"timestamp","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}}]}}]},"cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/spec/ERC20.spec","start":{"line":99,"character":4},"end":{"line":99,"character":15}}},"twoStateIndex":"NEITHER"},{"#class":"spec.cvlast.CVLExp.VariableExp","id":"args","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":6}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.VMInternal.RawArgs"},"cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/spec/ERC20.spec","start":{"line":99,"character":4},"end":{"line":99,"character":15}}},"twoStateIndex":"NEITHER"}],"noRevert":true,"storage":{"#class":"spec.cvlast.CVLExp.VariableExp","id":"lastStorage","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":6}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.VMInternal.BlockchainState"},"cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/spec/ERC20.spec","start":{"line":99,"character":4},"end":{"line":99,"character":15}}},"twoStateIndex":"NEITHER"},"tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":6}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Void"},"cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/spec/ERC20.spec","start":{"line":99,"character":4},"end":{"line":99,"character":5}}}},"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":6}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}}}}}
		NopCmd
		NopCmd
		NopCmd
		NopCmd
		NopCmd
		NopCmd
		AssignExpCmd:48 B101 LAnd(Ge(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff CANON34:5 ) Le(0x0 CANON34:5 ) )
		AssertCmd:48 B101 "sanity bounds check on cvl to vm encoding of tacTmp!1836:int failed"
		AssignExpCmd:48 R102:23 Apply(safe_math_narrow:bif CANON34:5)
		AssignExpCmd:48 R104 Select(tacBalance!!1:1 Apply(to_skey:bif R102:23) )
		AssignExpCmd:48 B106 LAnd(Ge(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff CANON35:6 ) Le(0x0 CANON35:6 ) )
		AssertCmd:48 B106 "sanity bounds check on cvl to vm encoding of tacTmp!1833:int failed"
		NopCmd
		AssignExpCmd:48 B109 Ge(R104 Apply(safe_math_narrow:bif CANON35:6) )
		JumpiCmd:48 2_0_0_0_0_0 3_0_0_0_0_0 B109
	}
	Block 5_0_0_0_0_0 Succ [0_0_0_3_0_0] {
		AssumeNotCmd:48 lastReverted!!157:49
		AssumeNotCmd:48 lastHasThrown!!158:50
		AnnotationCmd JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageGlobalChangeSnippet.StorageTakeSnapshot","lhs":{"namePrefix":"lastStorage","tag":{"#class":"tac.Tag.BlockchainState"},"callIndex":0,"meta":[{"key":{"name":"cvl.local","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true},{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"lastStorage"},{"key":{"name":"cvl.type","type":"spec.cvlast.CVLType$PureCVLType","erasureStrategy":"CallTrace"},"value":{"#class":"spec.cvlast.CVLType.PureCVLType.VMInternal.BlockchainState"}},{"key":{"name":"cvl","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true},{"key":{"name":"cvl.display","type":"java.lang.String","erasureStrategy":"CallTrace"},"value":"lastStorage"}]}}}
		AnnotationCmd:48 JSON{"key":{"name":"cvl.label.end","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		AnnotationCmd:40 JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Cmd","cmd":{"cmd_type":"spec.cvlast.CVLCmd.Simple.Definition","cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/spec/ERC20.spec","start":{"line":101,"character":4},"end":{"line":101,"character":57}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Mathint"},"idL":[{"#class":"spec.cvlast.CVLLhs.Id","cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/spec/ERC20.spec","start":{"line":101,"character":4},"end":{"line":101,"character":27}},"id":"allowance_after","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":6}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Mathint"},"cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/spec/ERC20.spec","start":{"line":101,"character":4},"end":{"line":101,"character":57}}}}],"exp":{"#class":"spec.cvlast.CVLExp.ApplyExp.ContractFunction.Concrete","methodIdWithCallContext":{"#class":"spec.cvlast.ConcreteMethod","signature":{"#class":"spec.cvlast.ExternalQualifiedMethodSignature.ExternalQualifiedMethodSig","wrapped":{"#class":"spec.cvlast.QualifiedMethodSignature.QualifiedMethodSig","qualifiedMethodName":{"#class":"spec.cvlast.QualifiedFunction","host":{"name":"ERC20"},"methodId":"allowance"},"params":[{"#class":"spec.cvlast.VMParam.Named","name":"owner","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$address"}},{"#class":"spec.cvlast.VMParam.Named","name":"spender","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$address"}}],"res":[{"#class":"spec.cvlast.VMParam.Unnamed","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256}}]},"sighashInt":{"n":"dd62ed3e"}}},"args":[{"#class":"spec.cvlast.CVLExp.VariableExp","id":"holder","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":6}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"},"cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/spec/ERC20.spec","start":{"line":101,"character":4},"end":{"line":101,"character":57}}},"twoStateIndex":"NEITHER"},{"#class":"spec.cvlast.CVLExp.VariableExp","id":"spender","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":6}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"},"cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/spec/ERC20.spec","start":{"line":101,"character":4},"end":{"line":101,"character":57}}},"twoStateIndex":"NEITHER"}],"noRevert":true,"storage":{"#class":"spec.cvlast.CVLExp.VariableExp","id":"lastStorage","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":6}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.VMInternal.BlockchainState"},"cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/spec/ERC20.spec","start":{"line":101,"character":4},"end":{"line":101,"character":57}}},"twoStateIndex":"NEITHER"},"isWhole":false,"tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":6}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.VM","descriptor":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256},"context":{"#class":"spec.cvlast.typedescriptors.FromVMContext.ReturnValue"}},"cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/spec/ERC20.spec","start":{"line":101,"character":30},"end":{"line":101,"character":39}},"annotation":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.CallResolution$DirectPassing","target":{"methodSignature":{"#class":"spec.cvlast.ExternalQualifiedMethodSignature.ExternalQualifiedMethodSig","wrapped":{"#class":"spec.cvlast.QualifiedMethodSignature.QualifiedMethodSig","qualifiedMethodName":{"#class":"spec.cvlast.QualifiedFunction","host":{"name":"ERC20"},"methodId":"allowance"},"params":[{"#class":"spec.cvlast.VMParam.Named","name":"owner","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$address"}},{"#class":"spec.cvlast.VMParam.Named","name":"spender","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$address"}}],"res":[{"#class":"spec.cvlast.VMParam.Unnamed","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256}}]},"sighashInt":{"n":"dd62ed3e"}},"definitelyNonPayable":true,"annotation":{"visibility":"EXTERNAL","envFree":true,"library":false},"stateMutability":"view","tag":{"#class":"spec.cvlast.CVLImportedFunctionTag.WithMethodInfo","evmMethodInfo":{"sigHash":"dd62ed3e","name":"allowance","argTypes":[{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.address"},{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.address"}],"resultTypes":[{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256}],"stateMutability":"view","envfreeInfo":{"#class":"bridge.EnvfreeInfo.Unknown"},"isConstant":false,"paramNames":["owner","spender"],"isLibrary":false}}},"hasEnv":false}}},"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":6}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}}}}}
		AssignExpCmd:51 I110 CANON12:2
		AssignExpCmd:52 I111 CANON13:3
	}
	Block 2_0_0_0_0_0 Succ [0_0_0_2_0_0] {
		AnnotationCmd:48 JSON{"key":{"name":"call.trace.push","type":"analysis.icfg.Inliner$CallStack$PushRecord","erasureStrategy":"Canonical"},"value":"rO0ABXNyACphbmFseXNpcy5pY2ZnLklubGluZXIkQ2FsbFN0YWNrJFB1c2hSZWNvcmSX8+DCTLCH+AIAA0kACGNhbGxlZUlkTAAGY2FsbGVldAATTHZjL2RhdGEvTWV0aG9kUmVmO0wAB3N1bW1hcnl0ABVMdmMvZGF0YS9DYWxsU3VtbWFyeTt4cAAAAAJzcgARdmMuZGF0YS5NZXRob2RSZWbJlJTzzU9pGAIAA0wABGF0dHJ0ABdMc2NlbmUvTWV0aG9kQXR0cmlidXRlO0wACmNvbnRyYWN0SWR0ABZMamF2YS9tYXRoL0JpZ0ludGVnZXI7TAAHc2lnSGFzaHQAEExldm0vU2lnaGFzaEludDt4cHNyABxzY2VuZS5NZXRob2RBdHRyaWJ1dGUkQ29tbW9uNHjdebdr9XMCAAB4cgAVc2NlbmUuTWV0aG9kQXR0cmlidXRlcYg2pYWutuUCAAB4cHNyABRqYXZhLm1hdGguQmlnSW50ZWdlcoz8nx+pO/sdAwAGSQAIYml0Q291bnRJAAliaXRMZW5ndGhJABNmaXJzdE5vbnplcm9CeXRlTnVtSQAMbG93ZXN0U2V0Qml0SQAGc2lnbnVtWwAJbWFnbml0dWRldAACW0J4cgAQamF2YS5sYW5nLk51bWJlcoaslR0LlOCLAgAAeHD///////////////7////+AAAAAXVyAAJbQqzzF/gGCFTgAgAAeHAAAAAQzkYEoAAAAAAAAAAAAAAAA3hzcgAOZXZtLlNpZ2hhc2hJbnRUdcqNMXEgeAIAAUwAAW5xAH4ABnhwc3EAfgAM///////////////+/////gAAAAF1cQB+ABAAAAAE0OMNsHhw"}
		NopCmd
		AssumeExpCmd Ge(CANON48:13 0x4 )
		NopCmd
		AssumeExpCmd Ge(0x7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff CANON48:13 )
		AssignExpCmd:48 B116 LAnd(Ge(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff CANON34:5 ) Le(0x0 CANON34:5 ) )
		AssertCmd:48 B116 "sanity bounds check on cvl to vm encoding of tacTmp!1749:int failed"
		AssignExpCmd:48 R117:23 Apply(safe_math_narrow:bif CANON34:5)
		NopCmd
		AssumeExpCmd LAnd(Le(R117:53 0xffffffffffffffffffffffffffffffffffffffff ) Ge(R117:53 0x0 ) )
		AssignExpCmd:48 B121 LAnd(Ge(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff CANON35:6 ) Le(0x0 CANON35:6 ) )
		AssertCmd:48 B121 "sanity bounds check on cvl to vm encoding of tacTmp!1752:int failed"
		AssignExpCmd:48 R122:23 Apply(safe_math_narrow:bif CANON35:6)
		NopCmd
		AssumeExpCmd LAnd(Le(R122:54 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff ) Ge(R122:54 0x0 ) )
		AssignExpCmd:48 B127 LAnd(Ge(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff CANON36:7 ) Le(0x0 CANON36:7 ) )
		AssertCmd:48 B127 "sanity bounds check on cvl to vm encoding of tacTmp!1810:int failed"
		AssignExpCmd:48 R128:23 Apply(safe_math_narrow:bif CANON36:7)
		NopCmd
		AssumeExpCmd LAnd(Le(R128:55 0xffffffffffffffffffffffffffffffffffffffff ) Ge(R128:55 0x0 ) )
		AssignExpCmd:48 B132 LAnd(Ge(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff CANON40:11 ) Le(0x0 CANON40:11 ) )
		AssertCmd:48 B132 "sanity bounds check on cvl to vm encoding of tacTmp!1813:int failed"
		AssignExpCmd:48 R133:23 Apply(safe_math_narrow:bif CANON40:11)
		NopCmd
		AssumeExpCmd LAnd(Le(R133:56 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff ) Ge(R133:56 0x0 ) )
		AssignExpCmd:48 B137 LAnd(Ge(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff CANON41:12 ) Le(0x0 CANON41:12 ) )
		AssertCmd:48 B137 "sanity bounds check on cvl to vm encoding of tacTmp!1816:int failed"
		AssignExpCmd:48 R138:23 Apply(safe_math_narrow:bif CANON41:12)
		NopCmd
		AssumeExpCmd LAnd(Le(R138:57 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff ) Ge(R138:57 0x0 ) )
		AssignExpCmd:48 B142 LAnd(Ge(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff CANON35:6 ) Le(0x0 CANON35:6 ) )
		AssertCmd:48 B142 "sanity bounds check on cvl to vm encoding of tacTmp!1819:int failed"
		AssignExpCmd:48 R143:23 Apply(safe_math_narrow:bif CANON35:6)
		AssignExpCmd:48 B145 LAnd(Ge(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff CANON34:5 ) Le(0x0 CANON34:5 ) )
		AssertCmd:48 B145 "sanity bounds check on cvl to vm encoding of tacTmp!1822:int failed"
		AssignExpCmd:48 R146:23 Apply(safe_math_narrow:bif CANON34:5)
		AssignExpCmd:48 R149:23 Select(tacBalance!!1:1 Apply(to_skey:bif R146:23) )
		AssignExpCmd:58 I150:23 IntSub(R149:23 R143:23 )
		AssignExpCmd:58 tacBalance!!151:1 Store(tacBalance!!1:1 Apply(to_skey:bif R146:23) I150:23 )
		AssignExpCmd:48 R152:23 Select(tacBalance!!151:1 Apply(to_skey:bif R5:15) )
		AssignExpCmd:58 R153:23 Add(R152:23 R143:23)
		NopCmd
		AssumeExpCmd Apply(add_noofl:bif R152:23 R143:23)
		AnnotationCmd:48 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.BalanceSnippet","srcAccountInfo":{"old":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R149","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}]},"new":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"I150","tag":{"#class":"tac.Tag.Int"},"callIndex":0,"meta":[{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}]},"addr":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R146","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}]}},"trgAccountInfo":{"old":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R152","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}]},"new":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R153","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}]},"addr":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R5","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"tacContractAt"},{"key":{"name":"tac.contract.sym.addr.name","type":"java.lang.String","erasureStrategy":"Erased"},"value":"ERC20"},{"key":{"name":"tac.contract.sym.addr","type":"java.math.BigInteger","erasureStrategy":"Erased"},"value":"ce4604a0000000000000000000000003"}]}},"transferredAmount":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R143","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}]}}}
		JumpCmd 0_0_0_2_0_0
	}
	Block 3_0_0_0_0_0 Succ [5_0_0_0_0_0] {
		AssignExpCmd:48 lastReverted!!155:49 true
		AssignExpCmd:48 lastHasThrown!!156:50 false
		LabelCmd "Parallel assignment for lastReverted!!157:bool, lastHasThrown!!158:bool := lastReverted!!155:bool, lastHasThrown!!156:bool"
		AssignExpCmd lastReverted!!157:49 lastReverted!!155:49
		AssignExpCmd lastHasThrown!!158:50 lastHasThrown!!156:50
	}
	Block 6_0_0_0_0_0 Succ [] {
		AssumeNotCmd:40 false
		AssumeNotCmd:40 false
		AnnotationCmd JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageGlobalChangeSnippet.StorageTakeSnapshot","lhs":{"namePrefix":"lastStorage","tag":{"#class":"tac.Tag.BlockchainState"},"callIndex":0,"meta":[{"key":{"name":"cvl.local","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true},{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"lastStorage"},{"key":{"name":"cvl.type","type":"spec.cvlast.CVLType$PureCVLType","erasureStrategy":"CallTrace"},"value":{"#class":"spec.cvlast.CVLType.PureCVLType.VMInternal.BlockchainState"}},{"key":{"name":"cvl","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true},{"key":{"name":"cvl.display","type":"java.lang.String","erasureStrategy":"CallTrace"},"value":"lastStorage"}]}}}
		AnnotationCmd:40 JSON{"key":{"name":"cvl.label.end","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		AnnotationCmd:59 JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Cmd","cmd":{"cmd_type":"spec.cvlast.CVLCmd.Simple.Assert","cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/spec/ERC20.spec","start":{"line":103,"character":4},"end":{"line":104,"character":58}},"exp":{"#class":"spec.cvlast.CVLExp.BinaryExp.ImpliesExp","l":{"#class":"spec.cvlast.CVLExp.RelopExp.ArithRelopExp.GtExp","l":{"#class":"spec.cvlast.CVLExp.VariableExp","id":"allowance_after","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":6}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Mathint"},"cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/spec/ERC20.spec","start":{"line":103,"character":4},"end":{"line":104,"character":58}}},"twoStateIndex":"NEITHER"},"r":{"#class":"spec.cvlast.CVLExp.VariableExp","id":"allowance_before","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":6}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Mathint"},"cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/spec/ERC20.spec","start":{"line":103,"character":4},"end":{"line":104,"character":58}}},"twoStateIndex":"NEITHER"},"tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":6}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"},"cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/spec/ERC20.spec","start":{"line":103,"character":11},"end":{"line":103,"character":45}}}},"r":{"#class":"spec.cvlast.CVLExp.RelopExp.EqExp","l":{"#class":"spec.cvlast.CVLExp.FieldSelectExp","structExp":{"#class":"spec.cvlast.CVLExp.FieldSelectExp","structExp":{"#class":"spec.cvlast.CVLExp.VariableExp","id":"e","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":6}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"env","fields":[{"fieldName":"msg","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"msg","fields":[{"fieldName":"sender","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"value","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}}]}},{"fieldName":"tx","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"tx","fields":[{"fieldName":"origin","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}}]}},{"fieldName":"block","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"block","fields":[{"fieldName":"coinbase","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"difficulty","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"gaslimit","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"number","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"timestamp","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}}]}}]},"cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/spec/ERC20.spec","start":{"line":103,"character":4},"end":{"line":104,"character":58}}},"twoStateIndex":"NEITHER"},"fieldName":"msg","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":6}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"msg","fields":[{"fieldName":"sender","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"value","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}}]},"cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/spec/ERC20.spec","start":{"line":103,"character":49},"end":{"line":103,"character":50}}}},"fieldName":"sender","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":6}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"},"cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/spec/ERC20.spec","start":{"line":103,"character":49},"end":{"line":103,"character":50}}}},"r":{"#class":"spec.cvlast.CVLExp.VariableExp","id":"holder","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":6}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"},"cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/spec/ERC20.spec","start":{"line":103,"character":4},"end":{"line":104,"character":58}}},"twoStateIndex":"NEITHER"},"tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":6}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"},"cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/spec/ERC20.spec","start":{"line":103,"character":49},"end":{"line":103,"character":71}}}},"tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":6}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"},"cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/spec/ERC20.spec","start":{"line":103,"character":11},"end":{"line":103,"character":71}}}},"description":"\"approve must only change the sender's allowance\"","scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":6}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}}}}}
		AssignExpCmd:60 I159 CANON114:47
		AssignExpCmd:61 I160 CANON33:39
		AssignExpCmd:62 B161 Gt(I159 I160 )
		NopCmd
		AssignExpCmd:63 I163 CANON12:2
		AssignExpCmd:64 CANON120!!164:65 Eq(CANON34:5 I163 )
		AssignExpCmd:66 CANON122!!165:65 LOr(LNot(B161 ) CANON120!!164:65 )
		AssertCmd:67 CANON122!!165:65 "\"approve must only change the sender's allowance\""
		AnnotationCmd:59 JSON{"key":{"name":"cvl.label.end","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		AnnotationCmd:68 JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Cmd","cmd":{"cmd_type":"spec.cvlast.CVLCmd.Simple.Assert","cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/spec/ERC20.spec","start":{"line":106,"character":4},"end":{"line":108,"character":69}},"exp":{"#class":"spec.cvlast.CVLExp.BinaryExp.ImpliesExp","l":{"#class":"spec.cvlast.CVLExp.RelopExp.ArithRelopExp.GtExp","l":{"#class":"spec.cvlast.CVLExp.VariableExp","id":"allowance_after","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":6}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Mathint"},"cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/spec/ERC20.spec","start":{"line":106,"character":4},"end":{"line":108,"character":69}}},"twoStateIndex":"NEITHER"},"r":{"#class":"spec.cvlast.CVLExp.VariableExp","id":"allowance_before","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":6}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Mathint"},"cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/spec/ERC20.spec","start":{"line":106,"character":4},"end":{"line":108,"character":69}}},"twoStateIndex":"NEITHER"},"tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":6}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"},"cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/spec/ERC20.spec","start":{"line":106,"character":11},"end":{"line":106,"character":45}}}},"r":{"#class":"spec.cvlast.CVLExp.BinaryExp.LorExp","l":{"#class":"spec.cvlast.CVLExp.RelopExp.EqExp","l":{"#class":"spec.cvlast.CVLExp.FieldSelectExp","structExp":{"#class":"spec.cvlast.CVLExp.VariableExp","id":"f","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":6}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"method","fields":[{"fieldName":"selector","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":32}},{"fieldName":"isPure","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}},{"fieldName":"isView","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}},{"fieldName":"isPayable","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}},{"fieldName":"numberOfArguments","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"isFallback","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}}]},"cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/spec/ERC20.spec","start":{"line":106,"character":4},"end":{"line":108,"character":69}}},"twoStateIndex":"NEITHER"},"fieldName":"selector","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":6}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":32},"cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/spec/ERC20.spec","start":{"line":107,"character":9},"end":{"line":107,"character":10}}}},"r":{"#class":"spec.cvlast.CVLExp.FieldSelectExp","structExp":{"#class":"spec.cvlast.CVLExp.Constant.SignatureLiteralExp","function":{"#class":"spec.cvlast.QualifiedMethodSignature.QualifiedMethodSig","qualifiedMethodName":{"#class":"spec.cvlast.QualifiedFunction","host":{"name":"ERC20"},"methodId":"approve"},"params":[{"#class":"spec.cvlast.VMParam.Unnamed","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$address"}},{"#class":"spec.cvlast.VMParam.Unnamed","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256}}],"res":[]},"tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":6}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"method","fields":[{"fieldName":"selector","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":32}},{"fieldName":"isPure","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}},{"fieldName":"isView","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}},{"fieldName":"isPayable","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}},{"fieldName":"numberOfArguments","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"isFallback","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}}]},"cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/spec/ERC20.spec","start":{"line":107,"character":27},"end":{"line":107,"character":48}},"annotation":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.CVLExp$Constant$StructLit","fieldNameToEntry":{"selector":{"#class":"spec.cvlast.CVLExp.Constant.NumberLit","n":"95ea7b3","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":6}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":32},"cvlRange":{"#class":"spec.cvlast.CVLRange.Empty"}}},"isPure":{"#class":"spec.cvlast.CVLExp.Constant.BoolLit","b":"0","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":6}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"},"cvlRange":{"#class":"spec.cvlast.CVLRange.Empty"}}},"isView":{"#class":"spec.cvlast.CVLExp.Constant.BoolLit","b":"0","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":6}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"},"cvlRange":{"#class":"spec.cvlast.CVLRange.Empty"}}},"isPayable":{"#class":"spec.cvlast.CVLExp.Constant.BoolLit","b":"0","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":6}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"},"cvlRange":{"#class":"spec.cvlast.CVLRange.Empty"}}},"isFallback":{"#class":"spec.cvlast.CVLExp.Constant.BoolLit","b":"0","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":6}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"},"cvlRange":{"#class":"spec.cvlast.CVLRange.Empty"}}},"numberOfArguments":{"#class":"spec.cvlast.CVLExp.Constant.NumberLit","n":"2","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":6}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256},"cvlRange":{"#class":"spec.cvlast.CVLRange.Empty"}}}},"tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":6}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"method","fields":[{"fieldName":"selector","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":32}},{"fieldName":"isPure","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}},{"fieldName":"isView","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}},{"fieldName":"isPayable","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}},{"fieldName":"numberOfArguments","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"isFallback","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}}]},"cvlRange":{"#class":"spec.cvlast.CVLRange.Empty"}}}}},"fieldName":"selector","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":6}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":32},"cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/spec/ERC20.spec","start":{"line":107,"character":27},"end":{"line":107,"character":48}}}},"tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":6}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"},"cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/spec/ERC20.spec","start":{"line":107,"character":9},"end":{"line":107,"character":57}}}},"r":{"#class":"spec.cvlast.CVLExp.RelopExp.EqExp","l":{"#class":"spec.cvlast.CVLExp.FieldSelectExp","structExp":{"#class":"spec.cvlast.CVLExp.VariableExp","id":"f","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":6}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"method","fields":[{"fieldName":"selector","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":32}},{"fieldName":"isPure","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}},{"fieldName":"isView","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}},{"fieldName":"isPayable","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}},{"fieldName":"numberOfArguments","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"isFallback","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}}]},"cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/spec/ERC20.spec","start":{"line":106,"character":4},"end":{"line":108,"character":69}}},"twoStateIndex":"NEITHER"},"fieldName":"selector","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":6}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":32},"cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/spec/ERC20.spec","start":{"line":107,"character":61},"end":{"line":107,"character":62}}}},"r":{"#class":"spec.cvlast.CVLExp.FieldSelectExp","structExp":{"#class":"spec.cvlast.CVLExp.Constant.SignatureLiteralExp","function":{"#class":"spec.cvlast.QualifiedMethodSignature.QualifiedMethodSig","qualifiedMethodName":{"#class":"spec.cvlast.QualifiedFunction","host":{"name":"ERC20"},"methodId":"increaseAllowance"},"params":[{"#class":"spec.cvlast.VMParam.Unnamed","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$address"}},{"#class":"spec.cvlast.VMParam.Unnamed","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256}}],"res":[]},"tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":6}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"method","fields":[{"fieldName":"selector","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":32}},{"fieldName":"isPure","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}},{"fieldName":"isView","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}},{"fieldName":"isPayable","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}},{"fieldName":"numberOfArguments","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"isFallback","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}}]},"cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/spec/ERC20.spec","start":{"line":107,"character":79},"end":{"line":107,"character":110}},"annotation":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.CVLExp$Constant$StructLit","fieldNameToEntry":{"selector":{"#class":"spec.cvlast.CVLExp.Constant.NumberLit","n":"39509351","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":6}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":32},"cvlRange":{"#class":"spec.cvlast.CVLRange.Empty"}}},"isPure":{"#class":"spec.cvlast.CVLExp.Constant.BoolLit","b":"0","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":6}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"},"cvlRange":{"#class":"spec.cvlast.CVLRange.Empty"}}},"isView":{"#class":"spec.cvlast.CVLExp.Constant.BoolLit","b":"0","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":6}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"},"cvlRange":{"#class":"spec.cvlast.CVLRange.Empty"}}},"isPayable":{"#class":"spec.cvlast.CVLExp.Constant.BoolLit","b":"0","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":6}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"},"cvlRange":{"#class":"spec.cvlast.CVLRange.Empty"}}},"isFallback":{"#class":"spec.cvlast.CVLExp.Constant.BoolLit","b":"0","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":6}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"},"cvlRange":{"#class":"spec.cvlast.CVLRange.Empty"}}},"numberOfArguments":{"#class":"spec.cvlast.CVLExp.Constant.NumberLit","n":"2","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":6}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256},"cvlRange":{"#class":"spec.cvlast.CVLRange.Empty"}}}},"tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":6}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"method","fields":[{"fieldName":"selector","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":32}},{"fieldName":"isPure","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}},{"fieldName":"isView","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}},{"fieldName":"isPayable","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}},{"fieldName":"numberOfArguments","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"isFallback","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}}]},"cvlRange":{"#class":"spec.cvlast.CVLRange.Empty"}}}}},"fieldName":"selector","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":6}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":32},"cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/spec/ERC20.spec","start":{"line":107,"character":79},"end":{"line":107,"character":110}}}},"tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":6}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"},"cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/spec/ERC20.spec","start":{"line":107,"character":61},"end":{"line":107,"character":119}}}},"tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":6}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"},"cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/spec/ERC20.spec","start":{"line":107,"character":9},"end":{"line":107,"character":119}}}},"tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":6}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"},"cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/spec/ERC20.spec","start":{"line":106,"character":11},"end":{"line":107,"character":120}}}},"description":"\"only approve and increaseAllowance can increase allowances\"","scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":6}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}}}}}
		AssignExpCmd:69 I166 CANON114:47
		AssignExpCmd:70 I167 CANON33:39
		AssignExpCmd:71 B168 Gt(I166 I167 )
		AssignExpCmd:72 CANON126:65 false
		AssignExpCmd:73 CANON127:65 false
		AssignExpCmd:74 CANON128:65 false
		AssignExpCmd:75 CANON129!!169:65 LOr(LNot(B168 ) false )
		AssertCmd:76 CANON129!!169:65 "\"only approve and increaseAllowance can increase allowances\""
		AnnotationCmd:68 JSON{"key":{"name":"cvl.label.end","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
	}
	Block 0_0_0_2_0_0 Succ [4_0_0_0_0_0] {
		LabelCmd "Start procedure ERC20-deposit()"
		AnnotationCmd JSON{"key":{"name":"fps.free-pointer-is-scalarized","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true}
		AssignExpCmd lastHasThrown@2:50 false
		AssignExpCmd lastReverted@2:49 false
		AssignExpCmd R170:23 Select(tacExtcodesize!!0:0 Apply(to_skey:bif R5:28) )
		NopCmd
		AssumeExpCmd Gt(R170:23 0x0 )
		AnnotationCmd JSON{"key":{"name":"internal.func.finder.info","type":"analysis.ip.InternalFunctionFinderReport","erasureStrategy":"Erased"},"value":"rO0ABXNyAChhbmFseXNpcy5pcC5JbnRlcm5hbEZ1bmN0aW9uRmluZGVyUmVwb3J0ian+bYn1VdACAAFMABN1bnJlc29sdmVkRnVuY3Rpb25zdAAPTGphdmEvdXRpbC9TZXQ7eHBzcgAhZGF0YXN0cnVjdHVyZXMuTGlua2VkQXJyYXlIYXNoU2V0AAAAAAAAAAEDAAJGAApsb2FkRmFjdG9yTAAJaGFzaFRhYmxldAAuTGRhdGFzdHJ1Y3R1cmVzL2FycmF5aGFzaHRhYmxlL0FycmF5SGFzaFRhYmxlO3hwdwgAAAAAQAAAAHg="}
		AnnotationCmd JSON{"key":{"name":"fps.free-pointer-is-scalarized","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true}
		NopCmd
		AssumeExpCmd LNot(Lt(CANON48:13 0x4 ) )
		NopCmd
		AssumeExpCmd LNot(Gt(0x70a08231 tacSighash!!7:16 ) )
		NopCmd
		AssumeExpCmd LNot(Gt(0xa9059cbb tacSighash!!7:16 ) )
		NopCmd
		AssumeExpCmd LNot(Eq(0xa9059cbb tacSighash!!7:16 ) )
		NopCmd
		AssumeExpCmd LNot(Eq(0xb2bdfa7b tacSighash!!7:16 ) )
		NopCmd
		AssumeExpCmd Eq(0xd0e30db0 tacSighash!!7:16 )
		AssignExpCmd:77 R180:78 Apply(hash_3_keccak:bif Apply(skey_basic:bif 0x40) Apply(to_skey:bif R117:79) Apply(skey_basic:bif 0x0))
		AssignExpCmd:80 R181:81 Select(CANON89!!3:14 R180:82 )
		AnnotationCmd JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet","value":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R181","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1018}]},"displayPath":{"#class":"analysis.storage.DisplayPath.MapAccess","key":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R117","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.env.known-bit-width","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":160},{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1019}]},"keyTyp":{"#class":"tac.TACStorageType.IntegralType","typeLabel":"address","numBytes":"14","descriptor":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$address"},"lowerBound":null,"upperBound":null},"base":{"#class":"analysis.storage.DisplayPath.Root","name":"_balances"}},"storageType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256},"contractInstance":"ce4604a0000000000000000000000003","linkableStorageReadId":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet.None"}}}
		NopCmd
		AssumeExpCmd Apply(add_noofl:bif R181:81 R122:54)
		NopCmd
		NopCmd
		NopCmd
		AssignExpCmd R186:83 Apply(safe_math_narrow:bif IntAdd(Apply(safe_math_promotion:bif R181:81) Apply(safe_math_promotion:bif R122:54)))
		AnnotationCmd JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Message","s":"Apply hook Hook Sstore 0x0.0x0[key a] uint256 new_value tacS:wordmap"}}
		AssignExpCmd R187:23 Select(CANON89!!3:14 R180:82 )
		AnnotationCmd JSON{"key":{"name":"tac.inlined.hook","type":"instrumentation.transformers.HookInliner$InlinedHook","erasureStrategy":"Canonical"},"value":{"cvlPattern":{"#class":"spec.cvlast.CVLHookPattern.StoragePattern.Store","value":{"name":"new_value","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256}},"slot":{"#class":"spec.cvlast.CVLSlotPattern.MapAccess","base":{"#class":"spec.cvlast.CVLSlotPattern.Static.Named","solidityContract":{"name":"ERC20"},"name":"_balances"},"key":{"name":"a","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$address"}}},"base":"STORAGE","previousValue":{"name":"old_value","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256}}},"substitutions":{"new_value":{"#class":"vc.data.HookValue.Direct","expr":{"#class":"vc.data.TACExpr.Sym.Var","s":{"namePrefix":"R186","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1015}]},"tag":{"#class":"tac.Tag.Bit256"}}},"old_value":{"#class":"vc.data.HookValue.Direct","expr":{"#class":"vc.data.TACExpr.Sym.Var","s":{"namePrefix":"R187","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}]},"tag":{"#class":"tac.Tag.Bit256"}}},"a":{"#class":"vc.data.HookValue.Direct","expr":{"#class":"vc.data.TACExpr.Sym.Var","s":{"namePrefix":"R117","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.env.known-bit-width","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":160},{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1019}]},"tag":{"#class":"tac.Tag.Bit256"}}}}}}
		AnnotationCmd JSON{"key":{"name":"cvl.label.end","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		AnnotationCmd JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.StoreSnippet","value":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R186","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1015}]},"displayPath":{"#class":"analysis.storage.DisplayPath.MapAccess","key":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R117","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.env.known-bit-width","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":160},{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1019}]},"keyTyp":{"#class":"tac.TACStorageType.IntegralType","typeLabel":"address","numBytes":"14","descriptor":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$address"},"lowerBound":null,"upperBound":null},"base":{"#class":"analysis.storage.DisplayPath.Root","name":"_balances"}},"storageType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256},"contractInstance":"ce4604a0000000000000000000000003"}}
		AnnotationCmd JSON{"key":{"name":"tac.return.path","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		LabelCmd "End procedure ERC20-deposit()"
		AssignExpCmd lastReverted!!190:49 false
		AssignExpCmd lastHasThrown!!191:50 false
		JumpCmd 4_0_0_0_0_0
	}
	Block 4_0_0_0_0_0 Succ [5_0_0_0_0_0] {
		AnnotationCmd:48 JSON{"key":{"name":"call.trace.pop","type":"analysis.icfg.Inliner$CallStack$PopRecord","erasureStrategy":"Canonical"},"value":"rO0ABXNyAClhbmFseXNpcy5pY2ZnLklubGluZXIkQ2FsbFN0YWNrJFBvcFJlY29yZPAPfwSLdCWJAgABSQAIY2FsbGVlSWR4cAAAAAI="}
		LabelCmd "Parallel assignment for lastReverted!!157:bool, lastHasThrown!!158:bool := lastReverted!!190:bool, lastHasThrown!!191:bool"
		AssignExpCmd lastReverted!!157:49 lastReverted!!190:49
		AssignExpCmd lastHasThrown!!158:50 lastHasThrown!!191:50
	}
}
Axioms {
		CANON98
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
      "value": "holder"
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
      "value": "spender"
    }
  ],
  "4": [
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
  "5": [
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
      "value": "e.msg.sender"
    }
  ],
  "6": [
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
      "value": "e.msg.value"
    }
  ],
  "7": [
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
      "value": "e.tx.origin"
    }
  ],
  "8": [
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
      "value": "e.block.coinbase"
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
      "value": "e.block.difficulty"
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
      "value": "e.block.gaslimit"
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
      "value": "e.block.number"
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
      "value": "e.block.timestamp"
    }
  ],
  "13": [
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
      "value": "args"
    }
  ],
  "14": [
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
  "15": [
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
  "16": [
    {
      "key": {
        "name": "Tac.symbol.keyword",
        "type": "java.lang.String",
        "erasureStrategy": "Canonical"
      },
      "value": "tacSighash"
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
      "value": "f.selector"
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
      "value": "f.isPure"
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
      "value": "f.isView"
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
      "value": "f.isPayable"
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
      "value": "f.numberOfArguments"
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
      "value": "f.isFallback"
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
          "line": 96,
          "character": 4
        },
        "end": {
          "line": 96,
          "character": 58
        }
      }
    }
  ],
  "25": [
    {
      "key": {
        "name": "cvl.exp",
        "type": "spec.CVLExpToTACExprMeta",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "spec.CVLExpToTACExprMeta.NullaryCVLExp",
        "exp": {
          "#class": "spec.cvlast.CVLExp.VariableExp",
          "id": "holder",
          "tag": {
            "scope": {
              "scopeStack": [
                {
                  "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                },
                {
                  "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                  "scopeId": 6
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
              "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
            },
            "cvlRange": {
              "#class": "spec.cvlast.CVLRange.Range",
              "specFile": "certora/spec/ERC20.spec",
              "start": {
                "line": 96,
                "character": 4
              },
              "end": {
                "line": 96,
                "character": 58
              }
            }
          },
          "twoStateIndex": "NEITHER"
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
          "line": 96,
          "character": 4
        },
        "end": {
          "line": 96,
          "character": 58
        }
      }
    }
  ],
  "26": [
    {
      "key": {
        "name": "cvl.exp",
        "type": "spec.CVLExpToTACExprMeta",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "spec.CVLExpToTACExprMeta.NullaryCVLExp",
        "exp": {
          "#class": "spec.cvlast.CVLExp.VariableExp",
          "id": "spender",
          "tag": {
            "scope": {
              "scopeStack": [
                {
                  "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                },
                {
                  "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                  "scopeId": 6
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
              "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
            },
            "cvlRange": {
              "#class": "spec.cvlast.CVLRange.Range",
              "specFile": "certora/spec/ERC20.spec",
              "start": {
                "line": 96,
                "character": 4
              },
              "end": {
                "line": 96,
                "character": 58
              }
            }
          },
          "twoStateIndex": "NEITHER"
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
          "line": 96,
          "character": 4
        },
        "end": {
          "line": 96,
          "character": 58
        }
      }
    }
  ],
  "27": [
    {
      "key": {
        "name": "Tac.symbol.keyword",
        "type": "java.lang.String",
        "erasureStrategy": "Canonical"
      },
      "value": "tacCalldatasize"
    }
  ],
  "28": [
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
  "29": [
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
          "line": 96,
          "character": 4
        },
        "end": {
          "line": 96,
          "character": 58
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
        "begin": 5647,
        "len": 535,
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
  "30": [
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
          "line": 96,
          "character": 4
        },
        "end": {
          "line": 96,
          "character": 58
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
        "source": 3,
        "begin": 665,
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
  "31": [
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
      "value": 1016
    }
  ],
  "32": [
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
          "line": 96,
          "character": 4
        },
        "end": {
          "line": 96,
          "character": 58
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
        "begin": 6148,
        "len": 18,
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
  "33": [
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
      "value": 1019
    }
  ],
  "34": [
    {
      "key": {
        "name": "Tac.symbol.keyword",
        "type": "java.lang.String",
        "erasureStrategy": "Canonical"
      },
      "value": "tacM0x0"
    }
  ],
  "35": [
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
          "line": 96,
          "character": 4
        },
        "end": {
          "line": 96,
          "character": 58
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
        "begin": 6148,
        "len": 27,
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
  "36": [
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
      "value": 1019
    }
  ],
  "37": [
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
          "line": 96,
          "character": 4
        },
        "end": {
          "line": 96,
          "character": 58
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
        "begin": 6148,
        "len": 27,
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
        "name": "tac.call-graph.address-read",
        "type": "analysis.icfg.CallGraphBuilder$ContractStorageRead",
        "erasureStrategy": "Canonical"
      },
      "value": "rO0ABXNyADJhbmFseXNpcy5pY2ZnLkNhbGxHcmFwaEJ1aWxkZXIkQ29udHJhY3RTdG9yYWdlUmVhZLRpTKYiS4EFAgABSQACaWR4cAAAAAA="
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
  "38": [
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
              "namePrefix": "R25",
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
                  "value": 1017
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
                "namePrefix": "R22",
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
                    "value": 1017
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
                    "namePrefix": "R22",
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
                        "value": 1017
                      }
                    ]
                  },
                  "baseSlot": {
                    "#class": "vc.data.TACSymbol.Var.Full",
                    "namePrefix": "CANON30",
                    "tag": {
                      "#class": "tac.Tag.Bit256"
                    },
                    "callIndex": 1,
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
                    "namePrefix": "CANON29",
                    "tag": {
                      "#class": "tac.Tag.Bit256"
                    },
                    "callIndex": 1,
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
                "namePrefix": "R25",
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
                    "value": 1017
                  }
                ]
              },
              "baseSlot": {
                "#class": "vc.data.TACSymbol.Var.Full",
                "namePrefix": "CANON32",
                "tag": {
                  "#class": "tac.Tag.Bit256"
                },
                "callIndex": 1,
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
                "namePrefix": "CANON31",
                "tag": {
                  "#class": "tac.Tag.Bit256"
                },
                "callIndex": 1,
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
      "value": 1019
    }
  ],
  "39": [
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
        "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Mathint"
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
      "value": "allowance_before"
    }
  ],
  "40": [
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
          "line": 101,
          "character": 4
        },
        "end": {
          "line": 101,
          "character": 57
        }
      }
    }
  ],
  "41": [
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
          "line": 101,
          "character": 4
        },
        "end": {
          "line": 101,
          "character": 57
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
        "begin": 5647,
        "len": 535,
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
  "42": [
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
          "line": 101,
          "character": 4
        },
        "end": {
          "line": 101,
          "character": 57
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
        "source": 3,
        "begin": 665,
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
  "43": [
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
          "line": 101,
          "character": 4
        },
        "end": {
          "line": 101,
          "character": 57
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
        "begin": 6148,
        "len": 18,
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
  "44": [
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
          "line": 101,
          "character": 4
        },
        "end": {
          "line": 101,
          "character": 57
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
        "begin": 6148,
        "len": 27,
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
  "45": [
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
          "line": 101,
          "character": 4
        },
        "end": {
          "line": 101,
          "character": 57
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
        "begin": 6148,
        "len": 27,
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
        "name": "tac.call-graph.address-read",
        "type": "analysis.icfg.CallGraphBuilder$ContractStorageRead",
        "erasureStrategy": "Canonical"
      },
      "value": "rO0ABXNyADJhbmFseXNpcy5pY2ZnLkNhbGxHcmFwaEJ1aWxkZXIkQ29udHJhY3RTdG9yYWdlUmVhZLRpTKYiS4EFAgABSQACaWR4cAAAAAE="
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
  "46": [
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
              "namePrefix": "R59",
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
                  "value": 1017
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
                "namePrefix": "R56",
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
                    "value": 1017
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
                    "namePrefix": "R56",
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
                        "value": 1017
                      }
                    ]
                  },
                  "baseSlot": {
                    "#class": "vc.data.TACSymbol.Var.Full",
                    "namePrefix": "CANON30",
                    "tag": {
                      "#class": "tac.Tag.Bit256"
                    },
                    "callIndex": 3,
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
                    "namePrefix": "CANON29",
                    "tag": {
                      "#class": "tac.Tag.Bit256"
                    },
                    "callIndex": 3,
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
                "namePrefix": "R59",
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
                    "value": 1017
                  }
                ]
              },
              "baseSlot": {
                "#class": "vc.data.TACSymbol.Var.Full",
                "namePrefix": "CANON32",
                "tag": {
                  "#class": "tac.Tag.Bit256"
                },
                "callIndex": 3,
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
                "namePrefix": "CANON31",
                "tag": {
                  "#class": "tac.Tag.Bit256"
                },
                "callIndex": 3,
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
      "value": 1019
    }
  ],
  "47": [
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
        "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Mathint"
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
      "value": "allowance_after"
    }
  ],
  "48": [
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
          "line": 99,
          "character": 4
        },
        "end": {
          "line": 99,
          "character": 15
        }
      }
    }
  ],
  "49": [
    {
      "key": {
        "name": "tac.last.reverted",
        "type": "tac.MetaMap$Companion$NothingValue",
        "erasureStrategy": "Canonical"
      },
      "value": {
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
        "name": "Tac.symbol.keyword",
        "type": "java.lang.String",
        "erasureStrategy": "Canonical"
      },
      "value": "lastReverted"
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
      "value": "lastReverted"
    }
  ],
  "50": [
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
        "name": "Tac.symbol.keyword",
        "type": "java.lang.String",
        "erasureStrategy": "Canonical"
      },
      "value": "lastHasThrown"
    },
    {
      "key": {
        "name": "tac.last.has.thrown",
        "type": "tac.MetaMap$Companion$NothingValue",
        "erasureStrategy": "Canonical"
      },
      "value": {
      }
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
      "value": "lastHasThrown"
    }
  ],
  "51": [
    {
      "key": {
        "name": "cvl.exp",
        "type": "spec.CVLExpToTACExprMeta",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "spec.CVLExpToTACExprMeta.NullaryCVLExp",
        "exp": {
          "#class": "spec.cvlast.CVLExp.VariableExp",
          "id": "holder",
          "tag": {
            "scope": {
              "scopeStack": [
                {
                  "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                },
                {
                  "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                  "scopeId": 6
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
              "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
            },
            "cvlRange": {
              "#class": "spec.cvlast.CVLRange.Range",
              "specFile": "certora/spec/ERC20.spec",
              "start": {
                "line": 101,
                "character": 4
              },
              "end": {
                "line": 101,
                "character": 57
              }
            }
          },
          "twoStateIndex": "NEITHER"
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
          "line": 101,
          "character": 4
        },
        "end": {
          "line": 101,
          "character": 57
        }
      }
    }
  ],
  "52": [
    {
      "key": {
        "name": "cvl.exp",
        "type": "spec.CVLExpToTACExprMeta",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "spec.CVLExpToTACExprMeta.NullaryCVLExp",
        "exp": {
          "#class": "spec.cvlast.CVLExp.VariableExp",
          "id": "spender",
          "tag": {
            "scope": {
              "scopeStack": [
                {
                  "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                },
                {
                  "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                  "scopeId": 6
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
              "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
            },
            "cvlRange": {
              "#class": "spec.cvlast.CVLRange.Range",
              "specFile": "certora/spec/ERC20.spec",
              "start": {
                "line": 101,
                "character": 4
              },
              "end": {
                "line": 101,
                "character": 57
              }
            }
          },
          "twoStateIndex": "NEITHER"
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
          "line": 101,
          "character": 4
        },
        "end": {
          "line": 101,
          "character": 57
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
  "54": [
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
  "55": [
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
  "56": [
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
  "57": [
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
  "58": [
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
          "line": 99,
          "character": 4
        },
        "end": {
          "line": 99,
          "character": 15
        }
      }
    }
  ],
  "59": [
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
          "line": 103,
          "character": 4
        },
        "end": {
          "line": 104,
          "character": 58
        }
      }
    }
  ],
  "60": [
    {
      "key": {
        "name": "cvl.exp",
        "type": "spec.CVLExpToTACExprMeta",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "spec.CVLExpToTACExprMeta.NullaryCVLExp",
        "exp": {
          "#class": "spec.cvlast.CVLExp.VariableExp",
          "id": "allowance_after",
          "tag": {
            "scope": {
              "scopeStack": [
                {
                  "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                },
                {
                  "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                  "scopeId": 6
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
                "line": 103,
                "character": 4
              },
              "end": {
                "line": 104,
                "character": 58
              }
            }
          },
          "twoStateIndex": "NEITHER"
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
          "line": 103,
          "character": 4
        },
        "end": {
          "line": 104,
          "character": 58
        }
      }
    }
  ],
  "61": [
    {
      "key": {
        "name": "cvl.exp",
        "type": "spec.CVLExpToTACExprMeta",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "spec.CVLExpToTACExprMeta.NullaryCVLExp",
        "exp": {
          "#class": "spec.cvlast.CVLExp.VariableExp",
          "id": "allowance_before",
          "tag": {
            "scope": {
              "scopeStack": [
                {
                  "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                },
                {
                  "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                  "scopeId": 6
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
                "line": 103,
                "character": 4
              },
              "end": {
                "line": 104,
                "character": 58
              }
            }
          },
          "twoStateIndex": "NEITHER"
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
          "line": 103,
          "character": 4
        },
        "end": {
          "line": 104,
          "character": 58
        }
      }
    }
  ],
  "62": [
    {
      "key": {
        "name": "cvl.exp",
        "type": "spec.CVLExpToTACExprMeta",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "spec.CVLExpToTACExprMeta.BinaryCVLExp",
        "exp": {
          "#class": "spec.cvlast.CVLExp.RelopExp.ArithRelopExp.GtExp",
          "l": {
            "#class": "spec.cvlast.CVLExp.VariableExp",
            "id": "allowance_after",
            "tag": {
              "scope": {
                "scopeStack": [
                  {
                    "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                  },
                  {
                    "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                    "scopeId": 6
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
                  "line": 103,
                  "character": 4
                },
                "end": {
                  "line": 104,
                  "character": 58
                }
              }
            },
            "twoStateIndex": "NEITHER"
          },
          "r": {
            "#class": "spec.cvlast.CVLExp.VariableExp",
            "id": "allowance_before",
            "tag": {
              "scope": {
                "scopeStack": [
                  {
                    "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                  },
                  {
                    "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                    "scopeId": 6
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
                  "line": 103,
                  "character": 4
                },
                "end": {
                  "line": 104,
                  "character": 58
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
                  "scopeId": 6
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
                "line": 103,
                "character": 11
              },
              "end": {
                "line": 103,
                "character": 45
              }
            }
          }
        },
        "o1": {
          "out": {
            "#class": "vc.data.TACSymbol.Var.Full",
            "namePrefix": "I159",
            "tag": {
              "#class": "tac.Tag.Int"
            },
            "callIndex": 0
          },
          "exp": {
            "#class": "spec.cvlast.CVLExp.VariableExp",
            "id": "allowance_after",
            "tag": {
              "scope": {
                "scopeStack": [
                  {
                    "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                  },
                  {
                    "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                    "scopeId": 6
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
                  "line": 103,
                  "character": 4
                },
                "end": {
                  "line": 104,
                  "character": 58
                }
              }
            },
            "twoStateIndex": "NEITHER"
          }
        },
        "o2": {
          "out": {
            "#class": "vc.data.TACSymbol.Var.Full",
            "namePrefix": "I160",
            "tag": {
              "#class": "tac.Tag.Int"
            },
            "callIndex": 0
          },
          "exp": {
            "#class": "spec.cvlast.CVLExp.VariableExp",
            "id": "allowance_before",
            "tag": {
              "scope": {
                "scopeStack": [
                  {
                    "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                  },
                  {
                    "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                    "scopeId": 6
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
                  "line": 103,
                  "character": 4
                },
                "end": {
                  "line": 104,
                  "character": 58
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
          "line": 103,
          "character": 4
        },
        "end": {
          "line": 104,
          "character": 58
        }
      }
    }
  ],
  "63": [
    {
      "key": {
        "name": "cvl.exp",
        "type": "spec.CVLExpToTACExprMeta",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "spec.CVLExpToTACExprMeta.NullaryCVLExp",
        "exp": {
          "#class": "spec.cvlast.CVLExp.VariableExp",
          "id": "holder",
          "tag": {
            "scope": {
              "scopeStack": [
                {
                  "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                },
                {
                  "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                  "scopeId": 6
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
              "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
            },
            "cvlRange": {
              "#class": "spec.cvlast.CVLRange.Range",
              "specFile": "certora/spec/ERC20.spec",
              "start": {
                "line": 103,
                "character": 4
              },
              "end": {
                "line": 104,
                "character": 58
              }
            }
          },
          "twoStateIndex": "NEITHER"
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
          "line": 103,
          "character": 4
        },
        "end": {
          "line": 104,
          "character": 58
        }
      }
    }
  ],
  "64": [
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
            "#class": "spec.cvlast.CVLExp.FieldSelectExp",
            "structExp": {
              "#class": "spec.cvlast.CVLExp.FieldSelectExp",
              "structExp": {
                "#class": "spec.cvlast.CVLExp.VariableExp",
                "id": "e",
                "tag": {
                  "scope": {
                    "scopeStack": [
                      {
                        "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                      },
                      {
                        "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                        "scopeId": 6
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
                    "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
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
                  "cvlRange": {
                    "#class": "spec.cvlast.CVLRange.Range",
                    "specFile": "certora/spec/ERC20.spec",
                    "start": {
                      "line": 103,
                      "character": 4
                    },
                    "end": {
                      "line": 104,
                      "character": 58
                    }
                  }
                },
                "twoStateIndex": "NEITHER"
              },
              "fieldName": "msg",
              "tag": {
                "scope": {
                  "scopeStack": [
                    {
                      "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                    },
                    {
                      "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                      "scopeId": 6
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
                },
                "cvlRange": {
                  "#class": "spec.cvlast.CVLRange.Range",
                  "specFile": "certora/spec/ERC20.spec",
                  "start": {
                    "line": 103,
                    "character": 49
                  },
                  "end": {
                    "line": 103,
                    "character": 50
                  }
                }
              }
            },
            "fieldName": "sender",
            "tag": {
              "scope": {
                "scopeStack": [
                  {
                    "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                  },
                  {
                    "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                    "scopeId": 6
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
                "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
              },
              "cvlRange": {
                "#class": "spec.cvlast.CVLRange.Range",
                "specFile": "certora/spec/ERC20.spec",
                "start": {
                  "line": 103,
                  "character": 49
                },
                "end": {
                  "line": 103,
                  "character": 50
                }
              }
            }
          },
          "r": {
            "#class": "spec.cvlast.CVLExp.VariableExp",
            "id": "holder",
            "tag": {
              "scope": {
                "scopeStack": [
                  {
                    "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                  },
                  {
                    "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                    "scopeId": 6
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
                "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
              },
              "cvlRange": {
                "#class": "spec.cvlast.CVLRange.Range",
                "specFile": "certora/spec/ERC20.spec",
                "start": {
                  "line": 103,
                  "character": 4
                },
                "end": {
                  "line": 104,
                  "character": 58
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
                  "scopeId": 6
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
                "line": 103,
                "character": 49
              },
              "end": {
                "line": 103,
                "character": 71
              }
            }
          }
        },
        "o1": {
          "out": {
            "#class": "vc.data.TACSymbol.Var.Full",
            "namePrefix": "CANON121",
            "tag": {
              "#class": "tac.Tag.Int"
            },
            "callIndex": 0
          },
          "exp": {
            "#class": "spec.cvlast.CVLExp.FieldSelectExp",
            "structExp": {
              "#class": "spec.cvlast.CVLExp.FieldSelectExp",
              "structExp": {
                "#class": "spec.cvlast.CVLExp.VariableExp",
                "id": "e",
                "tag": {
                  "scope": {
                    "scopeStack": [
                      {
                        "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                      },
                      {
                        "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                        "scopeId": 6
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
                    "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
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
                  "cvlRange": {
                    "#class": "spec.cvlast.CVLRange.Range",
                    "specFile": "certora/spec/ERC20.spec",
                    "start": {
                      "line": 103,
                      "character": 4
                    },
                    "end": {
                      "line": 104,
                      "character": 58
                    }
                  }
                },
                "twoStateIndex": "NEITHER"
              },
              "fieldName": "msg",
              "tag": {
                "scope": {
                  "scopeStack": [
                    {
                      "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                    },
                    {
                      "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                      "scopeId": 6
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
                },
                "cvlRange": {
                  "#class": "spec.cvlast.CVLRange.Range",
                  "specFile": "certora/spec/ERC20.spec",
                  "start": {
                    "line": 103,
                    "character": 49
                  },
                  "end": {
                    "line": 103,
                    "character": 50
                  }
                }
              }
            },
            "fieldName": "sender",
            "tag": {
              "scope": {
                "scopeStack": [
                  {
                    "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                  },
                  {
                    "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                    "scopeId": 6
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
                "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
              },
              "cvlRange": {
                "#class": "spec.cvlast.CVLRange.Range",
                "specFile": "certora/spec/ERC20.spec",
                "start": {
                  "line": 103,
                  "character": 49
                },
                "end": {
                  "line": 103,
                  "character": 50
                }
              }
            }
          }
        },
        "o2": {
          "out": {
            "#class": "vc.data.TACSymbol.Var.Full",
            "namePrefix": "I163",
            "tag": {
              "#class": "tac.Tag.Int"
            },
            "callIndex": 0
          },
          "exp": {
            "#class": "spec.cvlast.CVLExp.VariableExp",
            "id": "holder",
            "tag": {
              "scope": {
                "scopeStack": [
                  {
                    "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                  },
                  {
                    "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                    "scopeId": 6
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
                "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
              },
              "cvlRange": {
                "#class": "spec.cvlast.CVLRange.Range",
                "specFile": "certora/spec/ERC20.spec",
                "start": {
                  "line": 103,
                  "character": 4
                },
                "end": {
                  "line": 104,
                  "character": 58
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
          "line": 103,
          "character": 4
        },
        "end": {
          "line": 104,
          "character": 58
        }
      }
    }
  ],
  "65": [
    {
      "key": {
        "name": "cvl",
        "type": "java.lang.Boolean",
        "erasureStrategy": "Canonical"
      },
      "value": true
    }
  ],
  "66": [
    {
      "key": {
        "name": "cvl.exp",
        "type": "spec.CVLExpToTACExprMeta",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "spec.CVLExpToTACExprMeta.BinaryCVLExp",
        "exp": {
          "#class": "spec.cvlast.CVLExp.BinaryExp.ImpliesExp",
          "l": {
            "#class": "spec.cvlast.CVLExp.RelopExp.ArithRelopExp.GtExp",
            "l": {
              "#class": "spec.cvlast.CVLExp.VariableExp",
              "id": "allowance_after",
              "tag": {
                "scope": {
                  "scopeStack": [
                    {
                      "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                    },
                    {
                      "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                      "scopeId": 6
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
                    "line": 103,
                    "character": 4
                  },
                  "end": {
                    "line": 104,
                    "character": 58
                  }
                }
              },
              "twoStateIndex": "NEITHER"
            },
            "r": {
              "#class": "spec.cvlast.CVLExp.VariableExp",
              "id": "allowance_before",
              "tag": {
                "scope": {
                  "scopeStack": [
                    {
                      "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                    },
                    {
                      "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                      "scopeId": 6
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
                    "line": 103,
                    "character": 4
                  },
                  "end": {
                    "line": 104,
                    "character": 58
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
                    "scopeId": 6
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
                  "line": 103,
                  "character": 11
                },
                "end": {
                  "line": 103,
                  "character": 45
                }
              }
            }
          },
          "r": {
            "#class": "spec.cvlast.CVLExp.RelopExp.EqExp",
            "l": {
              "#class": "spec.cvlast.CVLExp.FieldSelectExp",
              "structExp": {
                "#class": "spec.cvlast.CVLExp.FieldSelectExp",
                "structExp": {
                  "#class": "spec.cvlast.CVLExp.VariableExp",
                  "id": "e",
                  "tag": {
                    "scope": {
                      "scopeStack": [
                        {
                          "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                        },
                        {
                          "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                          "scopeId": 6
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
                      "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
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
                    "cvlRange": {
                      "#class": "spec.cvlast.CVLRange.Range",
                      "specFile": "certora/spec/ERC20.spec",
                      "start": {
                        "line": 103,
                        "character": 4
                      },
                      "end": {
                        "line": 104,
                        "character": 58
                      }
                    }
                  },
                  "twoStateIndex": "NEITHER"
                },
                "fieldName": "msg",
                "tag": {
                  "scope": {
                    "scopeStack": [
                      {
                        "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                      },
                      {
                        "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                        "scopeId": 6
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
                  },
                  "cvlRange": {
                    "#class": "spec.cvlast.CVLRange.Range",
                    "specFile": "certora/spec/ERC20.spec",
                    "start": {
                      "line": 103,
                      "character": 49
                    },
                    "end": {
                      "line": 103,
                      "character": 50
                    }
                  }
                }
              },
              "fieldName": "sender",
              "tag": {
                "scope": {
                  "scopeStack": [
                    {
                      "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                    },
                    {
                      "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                      "scopeId": 6
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
                  "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                },
                "cvlRange": {
                  "#class": "spec.cvlast.CVLRange.Range",
                  "specFile": "certora/spec/ERC20.spec",
                  "start": {
                    "line": 103,
                    "character": 49
                  },
                  "end": {
                    "line": 103,
                    "character": 50
                  }
                }
              }
            },
            "r": {
              "#class": "spec.cvlast.CVLExp.VariableExp",
              "id": "holder",
              "tag": {
                "scope": {
                  "scopeStack": [
                    {
                      "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                    },
                    {
                      "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                      "scopeId": 6
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
                  "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                },
                "cvlRange": {
                  "#class": "spec.cvlast.CVLRange.Range",
                  "specFile": "certora/spec/ERC20.spec",
                  "start": {
                    "line": 103,
                    "character": 4
                  },
                  "end": {
                    "line": 104,
                    "character": 58
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
                    "scopeId": 6
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
                  "line": 103,
                  "character": 49
                },
                "end": {
                  "line": 103,
                  "character": 71
                }
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
                  "scopeId": 6
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
                "line": 103,
                "character": 11
              },
              "end": {
                "line": 103,
                "character": 71
              }
            }
          }
        },
        "o1": {
          "out": {
            "#class": "vc.data.TACSymbol.Var.Full",
            "namePrefix": "B161",
            "tag": {
              "#class": "tac.Tag.Bool"
            },
            "callIndex": 0
          },
          "exp": {
            "#class": "spec.cvlast.CVLExp.RelopExp.ArithRelopExp.GtExp",
            "l": {
              "#class": "spec.cvlast.CVLExp.VariableExp",
              "id": "allowance_after",
              "tag": {
                "scope": {
                  "scopeStack": [
                    {
                      "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                    },
                    {
                      "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                      "scopeId": 6
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
                    "line": 103,
                    "character": 4
                  },
                  "end": {
                    "line": 104,
                    "character": 58
                  }
                }
              },
              "twoStateIndex": "NEITHER"
            },
            "r": {
              "#class": "spec.cvlast.CVLExp.VariableExp",
              "id": "allowance_before",
              "tag": {
                "scope": {
                  "scopeStack": [
                    {
                      "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                    },
                    {
                      "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                      "scopeId": 6
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
                    "line": 103,
                    "character": 4
                  },
                  "end": {
                    "line": 104,
                    "character": 58
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
                    "scopeId": 6
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
                  "line": 103,
                  "character": 11
                },
                "end": {
                  "line": 103,
                  "character": 45
                }
              }
            }
          }
        },
        "o2": {
          "out": {
            "#class": "vc.data.TACSymbol.Var.Full",
            "namePrefix": "CANON120!!164",
            "tag": {
              "#class": "tac.Tag.Bool"
            },
            "callIndex": 0,
            "meta": [
              {
                "key": {
                  "name": "cvl",
                  "type": "java.lang.Boolean",
                  "erasureStrategy": "Canonical"
                },
                "value": true
              }
            ]
          },
          "exp": {
            "#class": "spec.cvlast.CVLExp.RelopExp.EqExp",
            "l": {
              "#class": "spec.cvlast.CVLExp.FieldSelectExp",
              "structExp": {
                "#class": "spec.cvlast.CVLExp.FieldSelectExp",
                "structExp": {
                  "#class": "spec.cvlast.CVLExp.VariableExp",
                  "id": "e",
                  "tag": {
                    "scope": {
                      "scopeStack": [
                        {
                          "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                        },
                        {
                          "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                          "scopeId": 6
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
                      "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
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
                    "cvlRange": {
                      "#class": "spec.cvlast.CVLRange.Range",
                      "specFile": "certora/spec/ERC20.spec",
                      "start": {
                        "line": 103,
                        "character": 4
                      },
                      "end": {
                        "line": 104,
                        "character": 58
                      }
                    }
                  },
                  "twoStateIndex": "NEITHER"
                },
                "fieldName": "msg",
                "tag": {
                  "scope": {
                    "scopeStack": [
                      {
                        "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                      },
                      {
                        "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                        "scopeId": 6
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
                  },
                  "cvlRange": {
                    "#class": "spec.cvlast.CVLRange.Range",
                    "specFile": "certora/spec/ERC20.spec",
                    "start": {
                      "line": 103,
                      "character": 49
                    },
                    "end": {
                      "line": 103,
                      "character": 50
                    }
                  }
                }
              },
              "fieldName": "sender",
              "tag": {
                "scope": {
                  "scopeStack": [
                    {
                      "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                    },
                    {
                      "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                      "scopeId": 6
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
                  "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                },
                "cvlRange": {
                  "#class": "spec.cvlast.CVLRange.Range",
                  "specFile": "certora/spec/ERC20.spec",
                  "start": {
                    "line": 103,
                    "character": 49
                  },
                  "end": {
                    "line": 103,
                    "character": 50
                  }
                }
              }
            },
            "r": {
              "#class": "spec.cvlast.CVLExp.VariableExp",
              "id": "holder",
              "tag": {
                "scope": {
                  "scopeStack": [
                    {
                      "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                    },
                    {
                      "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                      "scopeId": 6
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
                  "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                },
                "cvlRange": {
                  "#class": "spec.cvlast.CVLRange.Range",
                  "specFile": "certora/spec/ERC20.spec",
                  "start": {
                    "line": 103,
                    "character": 4
                  },
                  "end": {
                    "line": 104,
                    "character": 58
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
                    "scopeId": 6
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
                  "line": 103,
                  "character": 49
                },
                "end": {
                  "line": 103,
                  "character": 71
                }
              }
            }
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
          "line": 103,
          "character": 4
        },
        "end": {
          "line": 104,
          "character": 58
        }
      }
    }
  ],
  "67": [
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
          "line": 103,
          "character": 4
        },
        "end": {
          "line": 104,
          "character": 58
        }
      }
    }
  ],
  "68": [
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
          "line": 106,
          "character": 4
        },
        "end": {
          "line": 108,
          "character": 69
        }
      }
    }
  ],
  "69": [
    {
      "key": {
        "name": "cvl.exp",
        "type": "spec.CVLExpToTACExprMeta",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "spec.CVLExpToTACExprMeta.NullaryCVLExp",
        "exp": {
          "#class": "spec.cvlast.CVLExp.VariableExp",
          "id": "allowance_after",
          "tag": {
            "scope": {
              "scopeStack": [
                {
                  "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                },
                {
                  "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                  "scopeId": 6
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
                "line": 106,
                "character": 4
              },
              "end": {
                "line": 108,
                "character": 69
              }
            }
          },
          "twoStateIndex": "NEITHER"
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
          "line": 106,
          "character": 4
        },
        "end": {
          "line": 108,
          "character": 69
        }
      }
    }
  ],
  "70": [
    {
      "key": {
        "name": "cvl.exp",
        "type": "spec.CVLExpToTACExprMeta",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "spec.CVLExpToTACExprMeta.NullaryCVLExp",
        "exp": {
          "#class": "spec.cvlast.CVLExp.VariableExp",
          "id": "allowance_before",
          "tag": {
            "scope": {
              "scopeStack": [
                {
                  "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                },
                {
                  "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                  "scopeId": 6
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
                "line": 106,
                "character": 4
              },
              "end": {
                "line": 108,
                "character": 69
              }
            }
          },
          "twoStateIndex": "NEITHER"
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
          "line": 106,
          "character": 4
        },
        "end": {
          "line": 108,
          "character": 69
        }
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
          "#class": "spec.cvlast.CVLExp.RelopExp.ArithRelopExp.GtExp",
          "l": {
            "#class": "spec.cvlast.CVLExp.VariableExp",
            "id": "allowance_after",
            "tag": {
              "scope": {
                "scopeStack": [
                  {
                    "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                  },
                  {
                    "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                    "scopeId": 6
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
                  "line": 106,
                  "character": 4
                },
                "end": {
                  "line": 108,
                  "character": 69
                }
              }
            },
            "twoStateIndex": "NEITHER"
          },
          "r": {
            "#class": "spec.cvlast.CVLExp.VariableExp",
            "id": "allowance_before",
            "tag": {
              "scope": {
                "scopeStack": [
                  {
                    "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                  },
                  {
                    "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                    "scopeId": 6
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
                  "line": 106,
                  "character": 4
                },
                "end": {
                  "line": 108,
                  "character": 69
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
                  "scopeId": 6
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
                "line": 106,
                "character": 11
              },
              "end": {
                "line": 106,
                "character": 45
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
            "#class": "spec.cvlast.CVLExp.VariableExp",
            "id": "allowance_after",
            "tag": {
              "scope": {
                "scopeStack": [
                  {
                    "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                  },
                  {
                    "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                    "scopeId": 6
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
                  "line": 106,
                  "character": 4
                },
                "end": {
                  "line": 108,
                  "character": 69
                }
              }
            },
            "twoStateIndex": "NEITHER"
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
            "id": "allowance_before",
            "tag": {
              "scope": {
                "scopeStack": [
                  {
                    "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                  },
                  {
                    "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                    "scopeId": 6
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
                  "line": 106,
                  "character": 4
                },
                "end": {
                  "line": 108,
                  "character": 69
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
          "line": 106,
          "character": 4
        },
        "end": {
          "line": 108,
          "character": 69
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
          "#class": "spec.cvlast.CVLExp.RelopExp.EqExp",
          "l": {
            "#class": "spec.cvlast.CVLExp.FieldSelectExp",
            "structExp": {
              "#class": "spec.cvlast.CVLExp.VariableExp",
              "id": "f",
              "tag": {
                "scope": {
                  "scopeStack": [
                    {
                      "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                    },
                    {
                      "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                      "scopeId": 6
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
                  "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
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
                "cvlRange": {
                  "#class": "spec.cvlast.CVLRange.Range",
                  "specFile": "certora/spec/ERC20.spec",
                  "start": {
                    "line": 106,
                    "character": 4
                  },
                  "end": {
                    "line": 108,
                    "character": 69
                  }
                }
              },
              "twoStateIndex": "NEITHER"
            },
            "fieldName": "selector",
            "tag": {
              "scope": {
                "scopeStack": [
                  {
                    "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                  },
                  {
                    "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                    "scopeId": 6
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
                "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                "k": 32
              },
              "cvlRange": {
                "#class": "spec.cvlast.CVLRange.Range",
                "specFile": "certora/spec/ERC20.spec",
                "start": {
                  "line": 107,
                  "character": 9
                },
                "end": {
                  "line": 107,
                  "character": 10
                }
              }
            }
          },
          "r": {
            "#class": "spec.cvlast.CVLExp.FieldSelectExp",
            "structExp": {
              "#class": "spec.cvlast.CVLExp.Constant.SignatureLiteralExp",
              "function": {
                "#class": "spec.cvlast.QualifiedMethodSignature.QualifiedMethodSig",
                "qualifiedMethodName": {
                  "#class": "spec.cvlast.QualifiedFunction",
                  "host": {
                    "name": "ERC20"
                  },
                  "methodId": "approve"
                },
                "params": [
                  {
                    "#class": "spec.cvlast.VMParam.Unnamed",
                    "vmType": {
                      "#class": "ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$address"
                    }
                  },
                  {
                    "#class": "spec.cvlast.VMParam.Unnamed",
                    "vmType": {
                      "#class": "ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK",
                      "bitwidth": 256
                    }
                  }
                ],
                "res": [
                ]
              },
              "tag": {
                "scope": {
                  "scopeStack": [
                    {
                      "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                    },
                    {
                      "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                      "scopeId": 6
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
                  "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
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
                "cvlRange": {
                  "#class": "spec.cvlast.CVLRange.Range",
                  "specFile": "certora/spec/ERC20.spec",
                  "start": {
                    "line": 107,
                    "character": 27
                  },
                  "end": {
                    "line": 107,
                    "character": 48
                  }
                },
                "annotation": {
                  "#class": "ReflectivePolymorphicSerializer::spec.cvlast.CVLExp$Constant$StructLit",
                  "fieldNameToEntry": {
                    "selector": {
                      "#class": "spec.cvlast.CVLExp.Constant.NumberLit",
                      "n": "95ea7b3",
                      "tag": {
                        "scope": {
                          "scopeStack": [
                            {
                              "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                            },
                            {
                              "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                              "scopeId": 6
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
                          "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                          "k": 32
                        },
                        "cvlRange": {
                          "#class": "spec.cvlast.CVLRange.Empty"
                        }
                      }
                    },
                    "isPure": {
                      "#class": "spec.cvlast.CVLExp.Constant.BoolLit",
                      "b": "0",
                      "tag": {
                        "scope": {
                          "scopeStack": [
                            {
                              "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                            },
                            {
                              "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                              "scopeId": 6
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
                          "#class": "spec.cvlast.CVLRange.Empty"
                        }
                      }
                    },
                    "isView": {
                      "#class": "spec.cvlast.CVLExp.Constant.BoolLit",
                      "b": "0",
                      "tag": {
                        "scope": {
                          "scopeStack": [
                            {
                              "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                            },
                            {
                              "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                              "scopeId": 6
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
                          "#class": "spec.cvlast.CVLRange.Empty"
                        }
                      }
                    },
                    "isPayable": {
                      "#class": "spec.cvlast.CVLExp.Constant.BoolLit",
                      "b": "0",
                      "tag": {
                        "scope": {
                          "scopeStack": [
                            {
                              "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                            },
                            {
                              "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                              "scopeId": 6
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
                          "#class": "spec.cvlast.CVLRange.Empty"
                        }
                      }
                    },
                    "isFallback": {
                      "#class": "spec.cvlast.CVLExp.Constant.BoolLit",
                      "b": "0",
                      "tag": {
                        "scope": {
                          "scopeStack": [
                            {
                              "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                            },
                            {
                              "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                              "scopeId": 6
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
                          "#class": "spec.cvlast.CVLRange.Empty"
                        }
                      }
                    },
                    "numberOfArguments": {
                      "#class": "spec.cvlast.CVLExp.Constant.NumberLit",
                      "n": "2",
                      "tag": {
                        "scope": {
                          "scopeStack": [
                            {
                              "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                            },
                            {
                              "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                              "scopeId": 6
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
                          "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                          "k": 256
                        },
                        "cvlRange": {
                          "#class": "spec.cvlast.CVLRange.Empty"
                        }
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
                          "scopeId": 6
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
                      "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
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
                    "cvlRange": {
                      "#class": "spec.cvlast.CVLRange.Empty"
                    }
                  }
                }
              }
            },
            "fieldName": "selector",
            "tag": {
              "scope": {
                "scopeStack": [
                  {
                    "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                  },
                  {
                    "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                    "scopeId": 6
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
                "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                "k": 32
              },
              "cvlRange": {
                "#class": "spec.cvlast.CVLRange.Range",
                "specFile": "certora/spec/ERC20.spec",
                "start": {
                  "line": 107,
                  "character": 27
                },
                "end": {
                  "line": 107,
                  "character": 48
                }
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
                  "scopeId": 6
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
                "line": 107,
                "character": 9
              },
              "end": {
                "line": 107,
                "character": 57
              }
            }
          }
        },
        "o1": {
          "out": {
            "#class": "vc.data.TACSymbol.Const",
            "value": "d0e30db0"
          },
          "exp": {
            "#class": "spec.cvlast.CVLExp.FieldSelectExp",
            "structExp": {
              "#class": "spec.cvlast.CVLExp.VariableExp",
              "id": "f",
              "tag": {
                "scope": {
                  "scopeStack": [
                    {
                      "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                    },
                    {
                      "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                      "scopeId": 6
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
                  "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
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
                "cvlRange": {
                  "#class": "spec.cvlast.CVLRange.Range",
                  "specFile": "certora/spec/ERC20.spec",
                  "start": {
                    "line": 106,
                    "character": 4
                  },
                  "end": {
                    "line": 108,
                    "character": 69
                  }
                }
              },
              "twoStateIndex": "NEITHER"
            },
            "fieldName": "selector",
            "tag": {
              "scope": {
                "scopeStack": [
                  {
                    "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                  },
                  {
                    "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                    "scopeId": 6
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
                "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                "k": 32
              },
              "cvlRange": {
                "#class": "spec.cvlast.CVLRange.Range",
                "specFile": "certora/spec/ERC20.spec",
                "start": {
                  "line": 107,
                  "character": 9
                },
                "end": {
                  "line": 107,
                  "character": 10
                }
              }
            }
          }
        },
        "o2": {
          "out": {
            "#class": "vc.data.TACSymbol.Const",
            "value": "95ea7b3"
          },
          "exp": {
            "#class": "spec.cvlast.CVLExp.FieldSelectExp",
            "structExp": {
              "#class": "spec.cvlast.CVLExp.Constant.SignatureLiteralExp",
              "function": {
                "#class": "spec.cvlast.QualifiedMethodSignature.QualifiedMethodSig",
                "qualifiedMethodName": {
                  "#class": "spec.cvlast.QualifiedFunction",
                  "host": {
                    "name": "ERC20"
                  },
                  "methodId": "approve"
                },
                "params": [
                  {
                    "#class": "spec.cvlast.VMParam.Unnamed",
                    "vmType": {
                      "#class": "ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$address"
                    }
                  },
                  {
                    "#class": "spec.cvlast.VMParam.Unnamed",
                    "vmType": {
                      "#class": "ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK",
                      "bitwidth": 256
                    }
                  }
                ],
                "res": [
                ]
              },
              "tag": {
                "scope": {
                  "scopeStack": [
                    {
                      "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                    },
                    {
                      "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                      "scopeId": 6
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
                  "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
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
                "cvlRange": {
                  "#class": "spec.cvlast.CVLRange.Range",
                  "specFile": "certora/spec/ERC20.spec",
                  "start": {
                    "line": 107,
                    "character": 27
                  },
                  "end": {
                    "line": 107,
                    "character": 48
                  }
                },
                "annotation": {
                  "#class": "ReflectivePolymorphicSerializer::spec.cvlast.CVLExp$Constant$StructLit",
                  "fieldNameToEntry": {
                    "selector": {
                      "#class": "spec.cvlast.CVLExp.Constant.NumberLit",
                      "n": "95ea7b3",
                      "tag": {
                        "scope": {
                          "scopeStack": [
                            {
                              "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                            },
                            {
                              "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                              "scopeId": 6
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
                          "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                          "k": 32
                        },
                        "cvlRange": {
                          "#class": "spec.cvlast.CVLRange.Empty"
                        }
                      }
                    },
                    "isPure": {
                      "#class": "spec.cvlast.CVLExp.Constant.BoolLit",
                      "b": "0",
                      "tag": {
                        "scope": {
                          "scopeStack": [
                            {
                              "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                            },
                            {
                              "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                              "scopeId": 6
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
                          "#class": "spec.cvlast.CVLRange.Empty"
                        }
                      }
                    },
                    "isView": {
                      "#class": "spec.cvlast.CVLExp.Constant.BoolLit",
                      "b": "0",
                      "tag": {
                        "scope": {
                          "scopeStack": [
                            {
                              "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                            },
                            {
                              "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                              "scopeId": 6
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
                          "#class": "spec.cvlast.CVLRange.Empty"
                        }
                      }
                    },
                    "isPayable": {
                      "#class": "spec.cvlast.CVLExp.Constant.BoolLit",
                      "b": "0",
                      "tag": {
                        "scope": {
                          "scopeStack": [
                            {
                              "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                            },
                            {
                              "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                              "scopeId": 6
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
                          "#class": "spec.cvlast.CVLRange.Empty"
                        }
                      }
                    },
                    "isFallback": {
                      "#class": "spec.cvlast.CVLExp.Constant.BoolLit",
                      "b": "0",
                      "tag": {
                        "scope": {
                          "scopeStack": [
                            {
                              "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                            },
                            {
                              "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                              "scopeId": 6
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
                          "#class": "spec.cvlast.CVLRange.Empty"
                        }
                      }
                    },
                    "numberOfArguments": {
                      "#class": "spec.cvlast.CVLExp.Constant.NumberLit",
                      "n": "2",
                      "tag": {
                        "scope": {
                          "scopeStack": [
                            {
                              "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                            },
                            {
                              "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                              "scopeId": 6
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
                          "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                          "k": 256
                        },
                        "cvlRange": {
                          "#class": "spec.cvlast.CVLRange.Empty"
                        }
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
                          "scopeId": 6
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
                      "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
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
                    "cvlRange": {
                      "#class": "spec.cvlast.CVLRange.Empty"
                    }
                  }
                }
              }
            },
            "fieldName": "selector",
            "tag": {
              "scope": {
                "scopeStack": [
                  {
                    "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                  },
                  {
                    "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                    "scopeId": 6
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
                "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                "k": 32
              },
              "cvlRange": {
                "#class": "spec.cvlast.CVLRange.Range",
                "specFile": "certora/spec/ERC20.spec",
                "start": {
                  "line": 107,
                  "character": 27
                },
                "end": {
                  "line": 107,
                  "character": 48
                }
              }
            }
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
          "line": 106,
          "character": 4
        },
        "end": {
          "line": 108,
          "character": 69
        }
      }
    }
  ],
  "73": [
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
            "#class": "spec.cvlast.CVLExp.FieldSelectExp",
            "structExp": {
              "#class": "spec.cvlast.CVLExp.VariableExp",
              "id": "f",
              "tag": {
                "scope": {
                  "scopeStack": [
                    {
                      "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                    },
                    {
                      "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                      "scopeId": 6
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
                  "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
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
                "cvlRange": {
                  "#class": "spec.cvlast.CVLRange.Range",
                  "specFile": "certora/spec/ERC20.spec",
                  "start": {
                    "line": 106,
                    "character": 4
                  },
                  "end": {
                    "line": 108,
                    "character": 69
                  }
                }
              },
              "twoStateIndex": "NEITHER"
            },
            "fieldName": "selector",
            "tag": {
              "scope": {
                "scopeStack": [
                  {
                    "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                  },
                  {
                    "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                    "scopeId": 6
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
                "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                "k": 32
              },
              "cvlRange": {
                "#class": "spec.cvlast.CVLRange.Range",
                "specFile": "certora/spec/ERC20.spec",
                "start": {
                  "line": 107,
                  "character": 61
                },
                "end": {
                  "line": 107,
                  "character": 62
                }
              }
            }
          },
          "r": {
            "#class": "spec.cvlast.CVLExp.FieldSelectExp",
            "structExp": {
              "#class": "spec.cvlast.CVLExp.Constant.SignatureLiteralExp",
              "function": {
                "#class": "spec.cvlast.QualifiedMethodSignature.QualifiedMethodSig",
                "qualifiedMethodName": {
                  "#class": "spec.cvlast.QualifiedFunction",
                  "host": {
                    "name": "ERC20"
                  },
                  "methodId": "increaseAllowance"
                },
                "params": [
                  {
                    "#class": "spec.cvlast.VMParam.Unnamed",
                    "vmType": {
                      "#class": "ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$address"
                    }
                  },
                  {
                    "#class": "spec.cvlast.VMParam.Unnamed",
                    "vmType": {
                      "#class": "ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK",
                      "bitwidth": 256
                    }
                  }
                ],
                "res": [
                ]
              },
              "tag": {
                "scope": {
                  "scopeStack": [
                    {
                      "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                    },
                    {
                      "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                      "scopeId": 6
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
                  "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
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
                "cvlRange": {
                  "#class": "spec.cvlast.CVLRange.Range",
                  "specFile": "certora/spec/ERC20.spec",
                  "start": {
                    "line": 107,
                    "character": 79
                  },
                  "end": {
                    "line": 107,
                    "character": 110
                  }
                },
                "annotation": {
                  "#class": "ReflectivePolymorphicSerializer::spec.cvlast.CVLExp$Constant$StructLit",
                  "fieldNameToEntry": {
                    "selector": {
                      "#class": "spec.cvlast.CVLExp.Constant.NumberLit",
                      "n": "39509351",
                      "tag": {
                        "scope": {
                          "scopeStack": [
                            {
                              "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                            },
                            {
                              "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                              "scopeId": 6
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
                          "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                          "k": 32
                        },
                        "cvlRange": {
                          "#class": "spec.cvlast.CVLRange.Empty"
                        }
                      }
                    },
                    "isPure": {
                      "#class": "spec.cvlast.CVLExp.Constant.BoolLit",
                      "b": "0",
                      "tag": {
                        "scope": {
                          "scopeStack": [
                            {
                              "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                            },
                            {
                              "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                              "scopeId": 6
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
                          "#class": "spec.cvlast.CVLRange.Empty"
                        }
                      }
                    },
                    "isView": {
                      "#class": "spec.cvlast.CVLExp.Constant.BoolLit",
                      "b": "0",
                      "tag": {
                        "scope": {
                          "scopeStack": [
                            {
                              "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                            },
                            {
                              "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                              "scopeId": 6
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
                          "#class": "spec.cvlast.CVLRange.Empty"
                        }
                      }
                    },
                    "isPayable": {
                      "#class": "spec.cvlast.CVLExp.Constant.BoolLit",
                      "b": "0",
                      "tag": {
                        "scope": {
                          "scopeStack": [
                            {
                              "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                            },
                            {
                              "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                              "scopeId": 6
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
                          "#class": "spec.cvlast.CVLRange.Empty"
                        }
                      }
                    },
                    "isFallback": {
                      "#class": "spec.cvlast.CVLExp.Constant.BoolLit",
                      "b": "0",
                      "tag": {
                        "scope": {
                          "scopeStack": [
                            {
                              "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                            },
                            {
                              "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                              "scopeId": 6
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
                          "#class": "spec.cvlast.CVLRange.Empty"
                        }
                      }
                    },
                    "numberOfArguments": {
                      "#class": "spec.cvlast.CVLExp.Constant.NumberLit",
                      "n": "2",
                      "tag": {
                        "scope": {
                          "scopeStack": [
                            {
                              "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                            },
                            {
                              "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                              "scopeId": 6
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
                          "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                          "k": 256
                        },
                        "cvlRange": {
                          "#class": "spec.cvlast.CVLRange.Empty"
                        }
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
                          "scopeId": 6
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
                      "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
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
                    "cvlRange": {
                      "#class": "spec.cvlast.CVLRange.Empty"
                    }
                  }
                }
              }
            },
            "fieldName": "selector",
            "tag": {
              "scope": {
                "scopeStack": [
                  {
                    "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                  },
                  {
                    "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                    "scopeId": 6
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
                "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                "k": 32
              },
              "cvlRange": {
                "#class": "spec.cvlast.CVLRange.Range",
                "specFile": "certora/spec/ERC20.spec",
                "start": {
                  "line": 107,
                  "character": 79
                },
                "end": {
                  "line": 107,
                  "character": 110
                }
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
                  "scopeId": 6
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
                "line": 107,
                "character": 61
              },
              "end": {
                "line": 107,
                "character": 119
              }
            }
          }
        },
        "o1": {
          "out": {
            "#class": "vc.data.TACSymbol.Const",
            "value": "d0e30db0"
          },
          "exp": {
            "#class": "spec.cvlast.CVLExp.FieldSelectExp",
            "structExp": {
              "#class": "spec.cvlast.CVLExp.VariableExp",
              "id": "f",
              "tag": {
                "scope": {
                  "scopeStack": [
                    {
                      "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                    },
                    {
                      "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                      "scopeId": 6
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
                  "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
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
                "cvlRange": {
                  "#class": "spec.cvlast.CVLRange.Range",
                  "specFile": "certora/spec/ERC20.spec",
                  "start": {
                    "line": 106,
                    "character": 4
                  },
                  "end": {
                    "line": 108,
                    "character": 69
                  }
                }
              },
              "twoStateIndex": "NEITHER"
            },
            "fieldName": "selector",
            "tag": {
              "scope": {
                "scopeStack": [
                  {
                    "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                  },
                  {
                    "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                    "scopeId": 6
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
                "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                "k": 32
              },
              "cvlRange": {
                "#class": "spec.cvlast.CVLRange.Range",
                "specFile": "certora/spec/ERC20.spec",
                "start": {
                  "line": 107,
                  "character": 61
                },
                "end": {
                  "line": 107,
                  "character": 62
                }
              }
            }
          }
        },
        "o2": {
          "out": {
            "#class": "vc.data.TACSymbol.Const",
            "value": "39509351"
          },
          "exp": {
            "#class": "spec.cvlast.CVLExp.FieldSelectExp",
            "structExp": {
              "#class": "spec.cvlast.CVLExp.Constant.SignatureLiteralExp",
              "function": {
                "#class": "spec.cvlast.QualifiedMethodSignature.QualifiedMethodSig",
                "qualifiedMethodName": {
                  "#class": "spec.cvlast.QualifiedFunction",
                  "host": {
                    "name": "ERC20"
                  },
                  "methodId": "increaseAllowance"
                },
                "params": [
                  {
                    "#class": "spec.cvlast.VMParam.Unnamed",
                    "vmType": {
                      "#class": "ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$address"
                    }
                  },
                  {
                    "#class": "spec.cvlast.VMParam.Unnamed",
                    "vmType": {
                      "#class": "ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK",
                      "bitwidth": 256
                    }
                  }
                ],
                "res": [
                ]
              },
              "tag": {
                "scope": {
                  "scopeStack": [
                    {
                      "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                    },
                    {
                      "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                      "scopeId": 6
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
                  "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
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
                "cvlRange": {
                  "#class": "spec.cvlast.CVLRange.Range",
                  "specFile": "certora/spec/ERC20.spec",
                  "start": {
                    "line": 107,
                    "character": 79
                  },
                  "end": {
                    "line": 107,
                    "character": 110
                  }
                },
                "annotation": {
                  "#class": "ReflectivePolymorphicSerializer::spec.cvlast.CVLExp$Constant$StructLit",
                  "fieldNameToEntry": {
                    "selector": {
                      "#class": "spec.cvlast.CVLExp.Constant.NumberLit",
                      "n": "39509351",
                      "tag": {
                        "scope": {
                          "scopeStack": [
                            {
                              "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                            },
                            {
                              "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                              "scopeId": 6
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
                          "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                          "k": 32
                        },
                        "cvlRange": {
                          "#class": "spec.cvlast.CVLRange.Empty"
                        }
                      }
                    },
                    "isPure": {
                      "#class": "spec.cvlast.CVLExp.Constant.BoolLit",
                      "b": "0",
                      "tag": {
                        "scope": {
                          "scopeStack": [
                            {
                              "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                            },
                            {
                              "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                              "scopeId": 6
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
                          "#class": "spec.cvlast.CVLRange.Empty"
                        }
                      }
                    },
                    "isView": {
                      "#class": "spec.cvlast.CVLExp.Constant.BoolLit",
                      "b": "0",
                      "tag": {
                        "scope": {
                          "scopeStack": [
                            {
                              "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                            },
                            {
                              "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                              "scopeId": 6
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
                          "#class": "spec.cvlast.CVLRange.Empty"
                        }
                      }
                    },
                    "isPayable": {
                      "#class": "spec.cvlast.CVLExp.Constant.BoolLit",
                      "b": "0",
                      "tag": {
                        "scope": {
                          "scopeStack": [
                            {
                              "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                            },
                            {
                              "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                              "scopeId": 6
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
                          "#class": "spec.cvlast.CVLRange.Empty"
                        }
                      }
                    },
                    "isFallback": {
                      "#class": "spec.cvlast.CVLExp.Constant.BoolLit",
                      "b": "0",
                      "tag": {
                        "scope": {
                          "scopeStack": [
                            {
                              "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                            },
                            {
                              "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                              "scopeId": 6
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
                          "#class": "spec.cvlast.CVLRange.Empty"
                        }
                      }
                    },
                    "numberOfArguments": {
                      "#class": "spec.cvlast.CVLExp.Constant.NumberLit",
                      "n": "2",
                      "tag": {
                        "scope": {
                          "scopeStack": [
                            {
                              "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                            },
                            {
                              "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                              "scopeId": 6
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
                          "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                          "k": 256
                        },
                        "cvlRange": {
                          "#class": "spec.cvlast.CVLRange.Empty"
                        }
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
                          "scopeId": 6
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
                      "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
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
                    "cvlRange": {
                      "#class": "spec.cvlast.CVLRange.Empty"
                    }
                  }
                }
              }
            },
            "fieldName": "selector",
            "tag": {
              "scope": {
                "scopeStack": [
                  {
                    "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                  },
                  {
                    "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                    "scopeId": 6
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
                "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                "k": 32
              },
              "cvlRange": {
                "#class": "spec.cvlast.CVLRange.Range",
                "specFile": "certora/spec/ERC20.spec",
                "start": {
                  "line": 107,
                  "character": 79
                },
                "end": {
                  "line": 107,
                  "character": 110
                }
              }
            }
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
          "line": 106,
          "character": 4
        },
        "end": {
          "line": 108,
          "character": 69
        }
      }
    }
  ],
  "74": [
    {
      "key": {
        "name": "cvl.exp",
        "type": "spec.CVLExpToTACExprMeta",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "spec.CVLExpToTACExprMeta.BinaryCVLExp",
        "exp": {
          "#class": "spec.cvlast.CVLExp.BinaryExp.LorExp",
          "l": {
            "#class": "spec.cvlast.CVLExp.RelopExp.EqExp",
            "l": {
              "#class": "spec.cvlast.CVLExp.FieldSelectExp",
              "structExp": {
                "#class": "spec.cvlast.CVLExp.VariableExp",
                "id": "f",
                "tag": {
                  "scope": {
                    "scopeStack": [
                      {
                        "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                      },
                      {
                        "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                        "scopeId": 6
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
                    "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
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
                  "cvlRange": {
                    "#class": "spec.cvlast.CVLRange.Range",
                    "specFile": "certora/spec/ERC20.spec",
                    "start": {
                      "line": 106,
                      "character": 4
                    },
                    "end": {
                      "line": 108,
                      "character": 69
                    }
                  }
                },
                "twoStateIndex": "NEITHER"
              },
              "fieldName": "selector",
              "tag": {
                "scope": {
                  "scopeStack": [
                    {
                      "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                    },
                    {
                      "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                      "scopeId": 6
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
                  "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                  "k": 32
                },
                "cvlRange": {
                  "#class": "spec.cvlast.CVLRange.Range",
                  "specFile": "certora/spec/ERC20.spec",
                  "start": {
                    "line": 107,
                    "character": 9
                  },
                  "end": {
                    "line": 107,
                    "character": 10
                  }
                }
              }
            },
            "r": {
              "#class": "spec.cvlast.CVLExp.FieldSelectExp",
              "structExp": {
                "#class": "spec.cvlast.CVLExp.Constant.SignatureLiteralExp",
                "function": {
                  "#class": "spec.cvlast.QualifiedMethodSignature.QualifiedMethodSig",
                  "qualifiedMethodName": {
                    "#class": "spec.cvlast.QualifiedFunction",
                    "host": {
                      "name": "ERC20"
                    },
                    "methodId": "approve"
                  },
                  "params": [
                    {
                      "#class": "spec.cvlast.VMParam.Unnamed",
                      "vmType": {
                        "#class": "ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$address"
                      }
                    },
                    {
                      "#class": "spec.cvlast.VMParam.Unnamed",
                      "vmType": {
                        "#class": "ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK",
                        "bitwidth": 256
                      }
                    }
                  ],
                  "res": [
                  ]
                },
                "tag": {
                  "scope": {
                    "scopeStack": [
                      {
                        "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                      },
                      {
                        "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                        "scopeId": 6
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
                    "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
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
                  "cvlRange": {
                    "#class": "spec.cvlast.CVLRange.Range",
                    "specFile": "certora/spec/ERC20.spec",
                    "start": {
                      "line": 107,
                      "character": 27
                    },
                    "end": {
                      "line": 107,
                      "character": 48
                    }
                  },
                  "annotation": {
                    "#class": "ReflectivePolymorphicSerializer::spec.cvlast.CVLExp$Constant$StructLit",
                    "fieldNameToEntry": {
                      "selector": {
                        "#class": "spec.cvlast.CVLExp.Constant.NumberLit",
                        "n": "95ea7b3",
                        "tag": {
                          "scope": {
                            "scopeStack": [
                              {
                                "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                              },
                              {
                                "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                                "scopeId": 6
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
                            "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                            "k": 32
                          },
                          "cvlRange": {
                            "#class": "spec.cvlast.CVLRange.Empty"
                          }
                        }
                      },
                      "isPure": {
                        "#class": "spec.cvlast.CVLExp.Constant.BoolLit",
                        "b": "0",
                        "tag": {
                          "scope": {
                            "scopeStack": [
                              {
                                "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                              },
                              {
                                "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                                "scopeId": 6
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
                            "#class": "spec.cvlast.CVLRange.Empty"
                          }
                        }
                      },
                      "isView": {
                        "#class": "spec.cvlast.CVLExp.Constant.BoolLit",
                        "b": "0",
                        "tag": {
                          "scope": {
                            "scopeStack": [
                              {
                                "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                              },
                              {
                                "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                                "scopeId": 6
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
                            "#class": "spec.cvlast.CVLRange.Empty"
                          }
                        }
                      },
                      "isPayable": {
                        "#class": "spec.cvlast.CVLExp.Constant.BoolLit",
                        "b": "0",
                        "tag": {
                          "scope": {
                            "scopeStack": [
                              {
                                "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                              },
                              {
                                "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                                "scopeId": 6
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
                            "#class": "spec.cvlast.CVLRange.Empty"
                          }
                        }
                      },
                      "isFallback": {
                        "#class": "spec.cvlast.CVLExp.Constant.BoolLit",
                        "b": "0",
                        "tag": {
                          "scope": {
                            "scopeStack": [
                              {
                                "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                              },
                              {
                                "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                                "scopeId": 6
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
                            "#class": "spec.cvlast.CVLRange.Empty"
                          }
                        }
                      },
                      "numberOfArguments": {
                        "#class": "spec.cvlast.CVLExp.Constant.NumberLit",
                        "n": "2",
                        "tag": {
                          "scope": {
                            "scopeStack": [
                              {
                                "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                              },
                              {
                                "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                                "scopeId": 6
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
                            "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                            "k": 256
                          },
                          "cvlRange": {
                            "#class": "spec.cvlast.CVLRange.Empty"
                          }
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
                            "scopeId": 6
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
                        "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
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
                      "cvlRange": {
                        "#class": "spec.cvlast.CVLRange.Empty"
                      }
                    }
                  }
                }
              },
              "fieldName": "selector",
              "tag": {
                "scope": {
                  "scopeStack": [
                    {
                      "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                    },
                    {
                      "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                      "scopeId": 6
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
                  "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                  "k": 32
                },
                "cvlRange": {
                  "#class": "spec.cvlast.CVLRange.Range",
                  "specFile": "certora/spec/ERC20.spec",
                  "start": {
                    "line": 107,
                    "character": 27
                  },
                  "end": {
                    "line": 107,
                    "character": 48
                  }
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
                    "scopeId": 6
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
                  "line": 107,
                  "character": 9
                },
                "end": {
                  "line": 107,
                  "character": 57
                }
              }
            }
          },
          "r": {
            "#class": "spec.cvlast.CVLExp.RelopExp.EqExp",
            "l": {
              "#class": "spec.cvlast.CVLExp.FieldSelectExp",
              "structExp": {
                "#class": "spec.cvlast.CVLExp.VariableExp",
                "id": "f",
                "tag": {
                  "scope": {
                    "scopeStack": [
                      {
                        "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                      },
                      {
                        "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                        "scopeId": 6
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
                    "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
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
                  "cvlRange": {
                    "#class": "spec.cvlast.CVLRange.Range",
                    "specFile": "certora/spec/ERC20.spec",
                    "start": {
                      "line": 106,
                      "character": 4
                    },
                    "end": {
                      "line": 108,
                      "character": 69
                    }
                  }
                },
                "twoStateIndex": "NEITHER"
              },
              "fieldName": "selector",
              "tag": {
                "scope": {
                  "scopeStack": [
                    {
                      "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                    },
                    {
                      "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                      "scopeId": 6
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
                  "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                  "k": 32
                },
                "cvlRange": {
                  "#class": "spec.cvlast.CVLRange.Range",
                  "specFile": "certora/spec/ERC20.spec",
                  "start": {
                    "line": 107,
                    "character": 61
                  },
                  "end": {
                    "line": 107,
                    "character": 62
                  }
                }
              }
            },
            "r": {
              "#class": "spec.cvlast.CVLExp.FieldSelectExp",
              "structExp": {
                "#class": "spec.cvlast.CVLExp.Constant.SignatureLiteralExp",
                "function": {
                  "#class": "spec.cvlast.QualifiedMethodSignature.QualifiedMethodSig",
                  "qualifiedMethodName": {
                    "#class": "spec.cvlast.QualifiedFunction",
                    "host": {
                      "name": "ERC20"
                    },
                    "methodId": "increaseAllowance"
                  },
                  "params": [
                    {
                      "#class": "spec.cvlast.VMParam.Unnamed",
                      "vmType": {
                        "#class": "ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$address"
                      }
                    },
                    {
                      "#class": "spec.cvlast.VMParam.Unnamed",
                      "vmType": {
                        "#class": "ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK",
                        "bitwidth": 256
                      }
                    }
                  ],
                  "res": [
                  ]
                },
                "tag": {
                  "scope": {
                    "scopeStack": [
                      {
                        "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                      },
                      {
                        "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                        "scopeId": 6
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
                    "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
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
                  "cvlRange": {
                    "#class": "spec.cvlast.CVLRange.Range",
                    "specFile": "certora/spec/ERC20.spec",
                    "start": {
                      "line": 107,
                      "character": 79
                    },
                    "end": {
                      "line": 107,
                      "character": 110
                    }
                  },
                  "annotation": {
                    "#class": "ReflectivePolymorphicSerializer::spec.cvlast.CVLExp$Constant$StructLit",
                    "fieldNameToEntry": {
                      "selector": {
                        "#class": "spec.cvlast.CVLExp.Constant.NumberLit",
                        "n": "39509351",
                        "tag": {
                          "scope": {
                            "scopeStack": [
                              {
                                "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                              },
                              {
                                "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                                "scopeId": 6
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
                            "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                            "k": 32
                          },
                          "cvlRange": {
                            "#class": "spec.cvlast.CVLRange.Empty"
                          }
                        }
                      },
                      "isPure": {
                        "#class": "spec.cvlast.CVLExp.Constant.BoolLit",
                        "b": "0",
                        "tag": {
                          "scope": {
                            "scopeStack": [
                              {
                                "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                              },
                              {
                                "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                                "scopeId": 6
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
                            "#class": "spec.cvlast.CVLRange.Empty"
                          }
                        }
                      },
                      "isView": {
                        "#class": "spec.cvlast.CVLExp.Constant.BoolLit",
                        "b": "0",
                        "tag": {
                          "scope": {
                            "scopeStack": [
                              {
                                "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                              },
                              {
                                "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                                "scopeId": 6
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
                            "#class": "spec.cvlast.CVLRange.Empty"
                          }
                        }
                      },
                      "isPayable": {
                        "#class": "spec.cvlast.CVLExp.Constant.BoolLit",
                        "b": "0",
                        "tag": {
                          "scope": {
                            "scopeStack": [
                              {
                                "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                              },
                              {
                                "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                                "scopeId": 6
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
                            "#class": "spec.cvlast.CVLRange.Empty"
                          }
                        }
                      },
                      "isFallback": {
                        "#class": "spec.cvlast.CVLExp.Constant.BoolLit",
                        "b": "0",
                        "tag": {
                          "scope": {
                            "scopeStack": [
                              {
                                "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                              },
                              {
                                "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                                "scopeId": 6
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
                            "#class": "spec.cvlast.CVLRange.Empty"
                          }
                        }
                      },
                      "numberOfArguments": {
                        "#class": "spec.cvlast.CVLExp.Constant.NumberLit",
                        "n": "2",
                        "tag": {
                          "scope": {
                            "scopeStack": [
                              {
                                "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                              },
                              {
                                "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                                "scopeId": 6
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
                            "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                            "k": 256
                          },
                          "cvlRange": {
                            "#class": "spec.cvlast.CVLRange.Empty"
                          }
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
                            "scopeId": 6
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
                        "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
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
                      "cvlRange": {
                        "#class": "spec.cvlast.CVLRange.Empty"
                      }
                    }
                  }
                }
              },
              "fieldName": "selector",
              "tag": {
                "scope": {
                  "scopeStack": [
                    {
                      "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                    },
                    {
                      "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                      "scopeId": 6
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
                  "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                  "k": 32
                },
                "cvlRange": {
                  "#class": "spec.cvlast.CVLRange.Range",
                  "specFile": "certora/spec/ERC20.spec",
                  "start": {
                    "line": 107,
                    "character": 79
                  },
                  "end": {
                    "line": 107,
                    "character": 110
                  }
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
                    "scopeId": 6
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
                  "line": 107,
                  "character": 61
                },
                "end": {
                  "line": 107,
                  "character": 119
                }
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
                  "scopeId": 6
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
                "line": 107,
                "character": 9
              },
              "end": {
                "line": 107,
                "character": 119
              }
            }
          }
        },
        "o1": {
          "out": {
            "#class": "vc.data.TACSymbol.Const",
            "value": "0",
            "tag": {
              "#class": "tac.Tag.Bool"
            }
          },
          "exp": {
            "#class": "spec.cvlast.CVLExp.RelopExp.EqExp",
            "l": {
              "#class": "spec.cvlast.CVLExp.FieldSelectExp",
              "structExp": {
                "#class": "spec.cvlast.CVLExp.VariableExp",
                "id": "f",
                "tag": {
                  "scope": {
                    "scopeStack": [
                      {
                        "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                      },
                      {
                        "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                        "scopeId": 6
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
                    "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
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
                  "cvlRange": {
                    "#class": "spec.cvlast.CVLRange.Range",
                    "specFile": "certora/spec/ERC20.spec",
                    "start": {
                      "line": 106,
                      "character": 4
                    },
                    "end": {
                      "line": 108,
                      "character": 69
                    }
                  }
                },
                "twoStateIndex": "NEITHER"
              },
              "fieldName": "selector",
              "tag": {
                "scope": {
                  "scopeStack": [
                    {
                      "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                    },
                    {
                      "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                      "scopeId": 6
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
                  "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                  "k": 32
                },
                "cvlRange": {
                  "#class": "spec.cvlast.CVLRange.Range",
                  "specFile": "certora/spec/ERC20.spec",
                  "start": {
                    "line": 107,
                    "character": 9
                  },
                  "end": {
                    "line": 107,
                    "character": 10
                  }
                }
              }
            },
            "r": {
              "#class": "spec.cvlast.CVLExp.FieldSelectExp",
              "structExp": {
                "#class": "spec.cvlast.CVLExp.Constant.SignatureLiteralExp",
                "function": {
                  "#class": "spec.cvlast.QualifiedMethodSignature.QualifiedMethodSig",
                  "qualifiedMethodName": {
                    "#class": "spec.cvlast.QualifiedFunction",
                    "host": {
                      "name": "ERC20"
                    },
                    "methodId": "approve"
                  },
                  "params": [
                    {
                      "#class": "spec.cvlast.VMParam.Unnamed",
                      "vmType": {
                        "#class": "ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$address"
                      }
                    },
                    {
                      "#class": "spec.cvlast.VMParam.Unnamed",
                      "vmType": {
                        "#class": "ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK",
                        "bitwidth": 256
                      }
                    }
                  ],
                  "res": [
                  ]
                },
                "tag": {
                  "scope": {
                    "scopeStack": [
                      {
                        "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                      },
                      {
                        "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                        "scopeId": 6
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
                    "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
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
                  "cvlRange": {
                    "#class": "spec.cvlast.CVLRange.Range",
                    "specFile": "certora/spec/ERC20.spec",
                    "start": {
                      "line": 107,
                      "character": 27
                    },
                    "end": {
                      "line": 107,
                      "character": 48
                    }
                  },
                  "annotation": {
                    "#class": "ReflectivePolymorphicSerializer::spec.cvlast.CVLExp$Constant$StructLit",
                    "fieldNameToEntry": {
                      "selector": {
                        "#class": "spec.cvlast.CVLExp.Constant.NumberLit",
                        "n": "95ea7b3",
                        "tag": {
                          "scope": {
                            "scopeStack": [
                              {
                                "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                              },
                              {
                                "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                                "scopeId": 6
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
                            "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                            "k": 32
                          },
                          "cvlRange": {
                            "#class": "spec.cvlast.CVLRange.Empty"
                          }
                        }
                      },
                      "isPure": {
                        "#class": "spec.cvlast.CVLExp.Constant.BoolLit",
                        "b": "0",
                        "tag": {
                          "scope": {
                            "scopeStack": [
                              {
                                "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                              },
                              {
                                "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                                "scopeId": 6
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
                            "#class": "spec.cvlast.CVLRange.Empty"
                          }
                        }
                      },
                      "isView": {
                        "#class": "spec.cvlast.CVLExp.Constant.BoolLit",
                        "b": "0",
                        "tag": {
                          "scope": {
                            "scopeStack": [
                              {
                                "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                              },
                              {
                                "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                                "scopeId": 6
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
                            "#class": "spec.cvlast.CVLRange.Empty"
                          }
                        }
                      },
                      "isPayable": {
                        "#class": "spec.cvlast.CVLExp.Constant.BoolLit",
                        "b": "0",
                        "tag": {
                          "scope": {
                            "scopeStack": [
                              {
                                "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                              },
                              {
                                "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                                "scopeId": 6
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
                            "#class": "spec.cvlast.CVLRange.Empty"
                          }
                        }
                      },
                      "isFallback": {
                        "#class": "spec.cvlast.CVLExp.Constant.BoolLit",
                        "b": "0",
                        "tag": {
                          "scope": {
                            "scopeStack": [
                              {
                                "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                              },
                              {
                                "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                                "scopeId": 6
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
                            "#class": "spec.cvlast.CVLRange.Empty"
                          }
                        }
                      },
                      "numberOfArguments": {
                        "#class": "spec.cvlast.CVLExp.Constant.NumberLit",
                        "n": "2",
                        "tag": {
                          "scope": {
                            "scopeStack": [
                              {
                                "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                              },
                              {
                                "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                                "scopeId": 6
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
                            "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                            "k": 256
                          },
                          "cvlRange": {
                            "#class": "spec.cvlast.CVLRange.Empty"
                          }
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
                            "scopeId": 6
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
                        "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
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
                      "cvlRange": {
                        "#class": "spec.cvlast.CVLRange.Empty"
                      }
                    }
                  }
                }
              },
              "fieldName": "selector",
              "tag": {
                "scope": {
                  "scopeStack": [
                    {
                      "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                    },
                    {
                      "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                      "scopeId": 6
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
                  "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                  "k": 32
                },
                "cvlRange": {
                  "#class": "spec.cvlast.CVLRange.Range",
                  "specFile": "certora/spec/ERC20.spec",
                  "start": {
                    "line": 107,
                    "character": 27
                  },
                  "end": {
                    "line": 107,
                    "character": 48
                  }
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
                    "scopeId": 6
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
                  "line": 107,
                  "character": 9
                },
                "end": {
                  "line": 107,
                  "character": 57
                }
              }
            }
          }
        },
        "o2": {
          "out": {
            "#class": "vc.data.TACSymbol.Const",
            "value": "0",
            "tag": {
              "#class": "tac.Tag.Bool"
            }
          },
          "exp": {
            "#class": "spec.cvlast.CVLExp.RelopExp.EqExp",
            "l": {
              "#class": "spec.cvlast.CVLExp.FieldSelectExp",
              "structExp": {
                "#class": "spec.cvlast.CVLExp.VariableExp",
                "id": "f",
                "tag": {
                  "scope": {
                    "scopeStack": [
                      {
                        "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                      },
                      {
                        "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                        "scopeId": 6
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
                    "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
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
                  "cvlRange": {
                    "#class": "spec.cvlast.CVLRange.Range",
                    "specFile": "certora/spec/ERC20.spec",
                    "start": {
                      "line": 106,
                      "character": 4
                    },
                    "end": {
                      "line": 108,
                      "character": 69
                    }
                  }
                },
                "twoStateIndex": "NEITHER"
              },
              "fieldName": "selector",
              "tag": {
                "scope": {
                  "scopeStack": [
                    {
                      "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                    },
                    {
                      "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                      "scopeId": 6
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
                  "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                  "k": 32
                },
                "cvlRange": {
                  "#class": "spec.cvlast.CVLRange.Range",
                  "specFile": "certora/spec/ERC20.spec",
                  "start": {
                    "line": 107,
                    "character": 61
                  },
                  "end": {
                    "line": 107,
                    "character": 62
                  }
                }
              }
            },
            "r": {
              "#class": "spec.cvlast.CVLExp.FieldSelectExp",
              "structExp": {
                "#class": "spec.cvlast.CVLExp.Constant.SignatureLiteralExp",
                "function": {
                  "#class": "spec.cvlast.QualifiedMethodSignature.QualifiedMethodSig",
                  "qualifiedMethodName": {
                    "#class": "spec.cvlast.QualifiedFunction",
                    "host": {
                      "name": "ERC20"
                    },
                    "methodId": "increaseAllowance"
                  },
                  "params": [
                    {
                      "#class": "spec.cvlast.VMParam.Unnamed",
                      "vmType": {
                        "#class": "ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$address"
                      }
                    },
                    {
                      "#class": "spec.cvlast.VMParam.Unnamed",
                      "vmType": {
                        "#class": "ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK",
                        "bitwidth": 256
                      }
                    }
                  ],
                  "res": [
                  ]
                },
                "tag": {
                  "scope": {
                    "scopeStack": [
                      {
                        "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                      },
                      {
                        "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                        "scopeId": 6
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
                    "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
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
                  "cvlRange": {
                    "#class": "spec.cvlast.CVLRange.Range",
                    "specFile": "certora/spec/ERC20.spec",
                    "start": {
                      "line": 107,
                      "character": 79
                    },
                    "end": {
                      "line": 107,
                      "character": 110
                    }
                  },
                  "annotation": {
                    "#class": "ReflectivePolymorphicSerializer::spec.cvlast.CVLExp$Constant$StructLit",
                    "fieldNameToEntry": {
                      "selector": {
                        "#class": "spec.cvlast.CVLExp.Constant.NumberLit",
                        "n": "39509351",
                        "tag": {
                          "scope": {
                            "scopeStack": [
                              {
                                "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                              },
                              {
                                "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                                "scopeId": 6
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
                            "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                            "k": 32
                          },
                          "cvlRange": {
                            "#class": "spec.cvlast.CVLRange.Empty"
                          }
                        }
                      },
                      "isPure": {
                        "#class": "spec.cvlast.CVLExp.Constant.BoolLit",
                        "b": "0",
                        "tag": {
                          "scope": {
                            "scopeStack": [
                              {
                                "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                              },
                              {
                                "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                                "scopeId": 6
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
                            "#class": "spec.cvlast.CVLRange.Empty"
                          }
                        }
                      },
                      "isView": {
                        "#class": "spec.cvlast.CVLExp.Constant.BoolLit",
                        "b": "0",
                        "tag": {
                          "scope": {
                            "scopeStack": [
                              {
                                "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                              },
                              {
                                "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                                "scopeId": 6
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
                            "#class": "spec.cvlast.CVLRange.Empty"
                          }
                        }
                      },
                      "isPayable": {
                        "#class": "spec.cvlast.CVLExp.Constant.BoolLit",
                        "b": "0",
                        "tag": {
                          "scope": {
                            "scopeStack": [
                              {
                                "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                              },
                              {
                                "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                                "scopeId": 6
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
                            "#class": "spec.cvlast.CVLRange.Empty"
                          }
                        }
                      },
                      "isFallback": {
                        "#class": "spec.cvlast.CVLExp.Constant.BoolLit",
                        "b": "0",
                        "tag": {
                          "scope": {
                            "scopeStack": [
                              {
                                "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                              },
                              {
                                "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                                "scopeId": 6
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
                            "#class": "spec.cvlast.CVLRange.Empty"
                          }
                        }
                      },
                      "numberOfArguments": {
                        "#class": "spec.cvlast.CVLExp.Constant.NumberLit",
                        "n": "2",
                        "tag": {
                          "scope": {
                            "scopeStack": [
                              {
                                "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                              },
                              {
                                "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                                "scopeId": 6
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
                            "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                            "k": 256
                          },
                          "cvlRange": {
                            "#class": "spec.cvlast.CVLRange.Empty"
                          }
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
                            "scopeId": 6
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
                        "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
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
                      "cvlRange": {
                        "#class": "spec.cvlast.CVLRange.Empty"
                      }
                    }
                  }
                }
              },
              "fieldName": "selector",
              "tag": {
                "scope": {
                  "scopeStack": [
                    {
                      "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                    },
                    {
                      "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                      "scopeId": 6
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
                  "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                  "k": 32
                },
                "cvlRange": {
                  "#class": "spec.cvlast.CVLRange.Range",
                  "specFile": "certora/spec/ERC20.spec",
                  "start": {
                    "line": 107,
                    "character": 79
                  },
                  "end": {
                    "line": 107,
                    "character": 110
                  }
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
                    "scopeId": 6
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
                  "line": 107,
                  "character": 61
                },
                "end": {
                  "line": 107,
                  "character": 119
                }
              }
            }
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
          "line": 106,
          "character": 4
        },
        "end": {
          "line": 108,
          "character": 69
        }
      }
    }
  ],
  "75": [
    {
      "key": {
        "name": "cvl.exp",
        "type": "spec.CVLExpToTACExprMeta",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "spec.CVLExpToTACExprMeta.BinaryCVLExp",
        "exp": {
          "#class": "spec.cvlast.CVLExp.BinaryExp.ImpliesExp",
          "l": {
            "#class": "spec.cvlast.CVLExp.RelopExp.ArithRelopExp.GtExp",
            "l": {
              "#class": "spec.cvlast.CVLExp.VariableExp",
              "id": "allowance_after",
              "tag": {
                "scope": {
                  "scopeStack": [
                    {
                      "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                    },
                    {
                      "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                      "scopeId": 6
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
                    "line": 106,
                    "character": 4
                  },
                  "end": {
                    "line": 108,
                    "character": 69
                  }
                }
              },
              "twoStateIndex": "NEITHER"
            },
            "r": {
              "#class": "spec.cvlast.CVLExp.VariableExp",
              "id": "allowance_before",
              "tag": {
                "scope": {
                  "scopeStack": [
                    {
                      "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                    },
                    {
                      "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                      "scopeId": 6
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
                    "line": 106,
                    "character": 4
                  },
                  "end": {
                    "line": 108,
                    "character": 69
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
                    "scopeId": 6
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
                  "line": 106,
                  "character": 11
                },
                "end": {
                  "line": 106,
                  "character": 45
                }
              }
            }
          },
          "r": {
            "#class": "spec.cvlast.CVLExp.BinaryExp.LorExp",
            "l": {
              "#class": "spec.cvlast.CVLExp.RelopExp.EqExp",
              "l": {
                "#class": "spec.cvlast.CVLExp.FieldSelectExp",
                "structExp": {
                  "#class": "spec.cvlast.CVLExp.VariableExp",
                  "id": "f",
                  "tag": {
                    "scope": {
                      "scopeStack": [
                        {
                          "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                        },
                        {
                          "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                          "scopeId": 6
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
                      "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
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
                    "cvlRange": {
                      "#class": "spec.cvlast.CVLRange.Range",
                      "specFile": "certora/spec/ERC20.spec",
                      "start": {
                        "line": 106,
                        "character": 4
                      },
                      "end": {
                        "line": 108,
                        "character": 69
                      }
                    }
                  },
                  "twoStateIndex": "NEITHER"
                },
                "fieldName": "selector",
                "tag": {
                  "scope": {
                    "scopeStack": [
                      {
                        "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                      },
                      {
                        "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                        "scopeId": 6
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
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 32
                  },
                  "cvlRange": {
                    "#class": "spec.cvlast.CVLRange.Range",
                    "specFile": "certora/spec/ERC20.spec",
                    "start": {
                      "line": 107,
                      "character": 9
                    },
                    "end": {
                      "line": 107,
                      "character": 10
                    }
                  }
                }
              },
              "r": {
                "#class": "spec.cvlast.CVLExp.FieldSelectExp",
                "structExp": {
                  "#class": "spec.cvlast.CVLExp.Constant.SignatureLiteralExp",
                  "function": {
                    "#class": "spec.cvlast.QualifiedMethodSignature.QualifiedMethodSig",
                    "qualifiedMethodName": {
                      "#class": "spec.cvlast.QualifiedFunction",
                      "host": {
                        "name": "ERC20"
                      },
                      "methodId": "approve"
                    },
                    "params": [
                      {
                        "#class": "spec.cvlast.VMParam.Unnamed",
                        "vmType": {
                          "#class": "ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$address"
                        }
                      },
                      {
                        "#class": "spec.cvlast.VMParam.Unnamed",
                        "vmType": {
                          "#class": "ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK",
                          "bitwidth": 256
                        }
                      }
                    ],
                    "res": [
                    ]
                  },
                  "tag": {
                    "scope": {
                      "scopeStack": [
                        {
                          "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                        },
                        {
                          "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                          "scopeId": 6
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
                      "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
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
                    "cvlRange": {
                      "#class": "spec.cvlast.CVLRange.Range",
                      "specFile": "certora/spec/ERC20.spec",
                      "start": {
                        "line": 107,
                        "character": 27
                      },
                      "end": {
                        "line": 107,
                        "character": 48
                      }
                    },
                    "annotation": {
                      "#class": "ReflectivePolymorphicSerializer::spec.cvlast.CVLExp$Constant$StructLit",
                      "fieldNameToEntry": {
                        "selector": {
                          "#class": "spec.cvlast.CVLExp.Constant.NumberLit",
                          "n": "95ea7b3",
                          "tag": {
                            "scope": {
                              "scopeStack": [
                                {
                                  "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                                },
                                {
                                  "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                                  "scopeId": 6
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
                              "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                              "k": 32
                            },
                            "cvlRange": {
                              "#class": "spec.cvlast.CVLRange.Empty"
                            }
                          }
                        },
                        "isPure": {
                          "#class": "spec.cvlast.CVLExp.Constant.BoolLit",
                          "b": "0",
                          "tag": {
                            "scope": {
                              "scopeStack": [
                                {
                                  "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                                },
                                {
                                  "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                                  "scopeId": 6
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
                              "#class": "spec.cvlast.CVLRange.Empty"
                            }
                          }
                        },
                        "isView": {
                          "#class": "spec.cvlast.CVLExp.Constant.BoolLit",
                          "b": "0",
                          "tag": {
                            "scope": {
                              "scopeStack": [
                                {
                                  "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                                },
                                {
                                  "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                                  "scopeId": 6
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
                              "#class": "spec.cvlast.CVLRange.Empty"
                            }
                          }
                        },
                        "isPayable": {
                          "#class": "spec.cvlast.CVLExp.Constant.BoolLit",
                          "b": "0",
                          "tag": {
                            "scope": {
                              "scopeStack": [
                                {
                                  "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                                },
                                {
                                  "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                                  "scopeId": 6
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
                              "#class": "spec.cvlast.CVLRange.Empty"
                            }
                          }
                        },
                        "isFallback": {
                          "#class": "spec.cvlast.CVLExp.Constant.BoolLit",
                          "b": "0",
                          "tag": {
                            "scope": {
                              "scopeStack": [
                                {
                                  "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                                },
                                {
                                  "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                                  "scopeId": 6
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
                              "#class": "spec.cvlast.CVLRange.Empty"
                            }
                          }
                        },
                        "numberOfArguments": {
                          "#class": "spec.cvlast.CVLExp.Constant.NumberLit",
                          "n": "2",
                          "tag": {
                            "scope": {
                              "scopeStack": [
                                {
                                  "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                                },
                                {
                                  "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                                  "scopeId": 6
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
                              "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                              "k": 256
                            },
                            "cvlRange": {
                              "#class": "spec.cvlast.CVLRange.Empty"
                            }
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
                              "scopeId": 6
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
                          "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
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
                        "cvlRange": {
                          "#class": "spec.cvlast.CVLRange.Empty"
                        }
                      }
                    }
                  }
                },
                "fieldName": "selector",
                "tag": {
                  "scope": {
                    "scopeStack": [
                      {
                        "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                      },
                      {
                        "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                        "scopeId": 6
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
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 32
                  },
                  "cvlRange": {
                    "#class": "spec.cvlast.CVLRange.Range",
                    "specFile": "certora/spec/ERC20.spec",
                    "start": {
                      "line": 107,
                      "character": 27
                    },
                    "end": {
                      "line": 107,
                      "character": 48
                    }
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
                      "scopeId": 6
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
                    "line": 107,
                    "character": 9
                  },
                  "end": {
                    "line": 107,
                    "character": 57
                  }
                }
              }
            },
            "r": {
              "#class": "spec.cvlast.CVLExp.RelopExp.EqExp",
              "l": {
                "#class": "spec.cvlast.CVLExp.FieldSelectExp",
                "structExp": {
                  "#class": "spec.cvlast.CVLExp.VariableExp",
                  "id": "f",
                  "tag": {
                    "scope": {
                      "scopeStack": [
                        {
                          "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                        },
                        {
                          "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                          "scopeId": 6
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
                      "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
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
                    "cvlRange": {
                      "#class": "spec.cvlast.CVLRange.Range",
                      "specFile": "certora/spec/ERC20.spec",
                      "start": {
                        "line": 106,
                        "character": 4
                      },
                      "end": {
                        "line": 108,
                        "character": 69
                      }
                    }
                  },
                  "twoStateIndex": "NEITHER"
                },
                "fieldName": "selector",
                "tag": {
                  "scope": {
                    "scopeStack": [
                      {
                        "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                      },
                      {
                        "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                        "scopeId": 6
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
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 32
                  },
                  "cvlRange": {
                    "#class": "spec.cvlast.CVLRange.Range",
                    "specFile": "certora/spec/ERC20.spec",
                    "start": {
                      "line": 107,
                      "character": 61
                    },
                    "end": {
                      "line": 107,
                      "character": 62
                    }
                  }
                }
              },
              "r": {
                "#class": "spec.cvlast.CVLExp.FieldSelectExp",
                "structExp": {
                  "#class": "spec.cvlast.CVLExp.Constant.SignatureLiteralExp",
                  "function": {
                    "#class": "spec.cvlast.QualifiedMethodSignature.QualifiedMethodSig",
                    "qualifiedMethodName": {
                      "#class": "spec.cvlast.QualifiedFunction",
                      "host": {
                        "name": "ERC20"
                      },
                      "methodId": "increaseAllowance"
                    },
                    "params": [
                      {
                        "#class": "spec.cvlast.VMParam.Unnamed",
                        "vmType": {
                          "#class": "ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$address"
                        }
                      },
                      {
                        "#class": "spec.cvlast.VMParam.Unnamed",
                        "vmType": {
                          "#class": "ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK",
                          "bitwidth": 256
                        }
                      }
                    ],
                    "res": [
                    ]
                  },
                  "tag": {
                    "scope": {
                      "scopeStack": [
                        {
                          "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                        },
                        {
                          "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                          "scopeId": 6
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
                      "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
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
                    "cvlRange": {
                      "#class": "spec.cvlast.CVLRange.Range",
                      "specFile": "certora/spec/ERC20.spec",
                      "start": {
                        "line": 107,
                        "character": 79
                      },
                      "end": {
                        "line": 107,
                        "character": 110
                      }
                    },
                    "annotation": {
                      "#class": "ReflectivePolymorphicSerializer::spec.cvlast.CVLExp$Constant$StructLit",
                      "fieldNameToEntry": {
                        "selector": {
                          "#class": "spec.cvlast.CVLExp.Constant.NumberLit",
                          "n": "39509351",
                          "tag": {
                            "scope": {
                              "scopeStack": [
                                {
                                  "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                                },
                                {
                                  "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                                  "scopeId": 6
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
                              "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                              "k": 32
                            },
                            "cvlRange": {
                              "#class": "spec.cvlast.CVLRange.Empty"
                            }
                          }
                        },
                        "isPure": {
                          "#class": "spec.cvlast.CVLExp.Constant.BoolLit",
                          "b": "0",
                          "tag": {
                            "scope": {
                              "scopeStack": [
                                {
                                  "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                                },
                                {
                                  "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                                  "scopeId": 6
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
                              "#class": "spec.cvlast.CVLRange.Empty"
                            }
                          }
                        },
                        "isView": {
                          "#class": "spec.cvlast.CVLExp.Constant.BoolLit",
                          "b": "0",
                          "tag": {
                            "scope": {
                              "scopeStack": [
                                {
                                  "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                                },
                                {
                                  "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                                  "scopeId": 6
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
                              "#class": "spec.cvlast.CVLRange.Empty"
                            }
                          }
                        },
                        "isPayable": {
                          "#class": "spec.cvlast.CVLExp.Constant.BoolLit",
                          "b": "0",
                          "tag": {
                            "scope": {
                              "scopeStack": [
                                {
                                  "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                                },
                                {
                                  "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                                  "scopeId": 6
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
                              "#class": "spec.cvlast.CVLRange.Empty"
                            }
                          }
                        },
                        "isFallback": {
                          "#class": "spec.cvlast.CVLExp.Constant.BoolLit",
                          "b": "0",
                          "tag": {
                            "scope": {
                              "scopeStack": [
                                {
                                  "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                                },
                                {
                                  "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                                  "scopeId": 6
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
                              "#class": "spec.cvlast.CVLRange.Empty"
                            }
                          }
                        },
                        "numberOfArguments": {
                          "#class": "spec.cvlast.CVLExp.Constant.NumberLit",
                          "n": "2",
                          "tag": {
                            "scope": {
                              "scopeStack": [
                                {
                                  "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                                },
                                {
                                  "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                                  "scopeId": 6
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
                              "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                              "k": 256
                            },
                            "cvlRange": {
                              "#class": "spec.cvlast.CVLRange.Empty"
                            }
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
                              "scopeId": 6
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
                          "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
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
                        "cvlRange": {
                          "#class": "spec.cvlast.CVLRange.Empty"
                        }
                      }
                    }
                  }
                },
                "fieldName": "selector",
                "tag": {
                  "scope": {
                    "scopeStack": [
                      {
                        "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                      },
                      {
                        "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                        "scopeId": 6
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
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 32
                  },
                  "cvlRange": {
                    "#class": "spec.cvlast.CVLRange.Range",
                    "specFile": "certora/spec/ERC20.spec",
                    "start": {
                      "line": 107,
                      "character": 79
                    },
                    "end": {
                      "line": 107,
                      "character": 110
                    }
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
                      "scopeId": 6
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
                    "line": 107,
                    "character": 61
                  },
                  "end": {
                    "line": 107,
                    "character": 119
                  }
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
                    "scopeId": 6
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
                  "line": 107,
                  "character": 9
                },
                "end": {
                  "line": 107,
                  "character": 119
                }
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
                  "scopeId": 6
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
                "line": 106,
                "character": 11
              },
              "end": {
                "line": 107,
                "character": 120
              }
            }
          }
        },
        "o1": {
          "out": {
            "#class": "vc.data.TACSymbol.Var.Full",
            "namePrefix": "B168",
            "tag": {
              "#class": "tac.Tag.Bool"
            },
            "callIndex": 0
          },
          "exp": {
            "#class": "spec.cvlast.CVLExp.RelopExp.ArithRelopExp.GtExp",
            "l": {
              "#class": "spec.cvlast.CVLExp.VariableExp",
              "id": "allowance_after",
              "tag": {
                "scope": {
                  "scopeStack": [
                    {
                      "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                    },
                    {
                      "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                      "scopeId": 6
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
                    "line": 106,
                    "character": 4
                  },
                  "end": {
                    "line": 108,
                    "character": 69
                  }
                }
              },
              "twoStateIndex": "NEITHER"
            },
            "r": {
              "#class": "spec.cvlast.CVLExp.VariableExp",
              "id": "allowance_before",
              "tag": {
                "scope": {
                  "scopeStack": [
                    {
                      "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                    },
                    {
                      "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                      "scopeId": 6
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
                    "line": 106,
                    "character": 4
                  },
                  "end": {
                    "line": 108,
                    "character": 69
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
                    "scopeId": 6
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
                  "line": 106,
                  "character": 11
                },
                "end": {
                  "line": 106,
                  "character": 45
                }
              }
            }
          }
        },
        "o2": {
          "out": {
            "#class": "vc.data.TACSymbol.Const",
            "value": "0",
            "tag": {
              "#class": "tac.Tag.Bool"
            }
          },
          "exp": {
            "#class": "spec.cvlast.CVLExp.BinaryExp.LorExp",
            "l": {
              "#class": "spec.cvlast.CVLExp.RelopExp.EqExp",
              "l": {
                "#class": "spec.cvlast.CVLExp.FieldSelectExp",
                "structExp": {
                  "#class": "spec.cvlast.CVLExp.VariableExp",
                  "id": "f",
                  "tag": {
                    "scope": {
                      "scopeStack": [
                        {
                          "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                        },
                        {
                          "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                          "scopeId": 6
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
                      "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
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
                    "cvlRange": {
                      "#class": "spec.cvlast.CVLRange.Range",
                      "specFile": "certora/spec/ERC20.spec",
                      "start": {
                        "line": 106,
                        "character": 4
                      },
                      "end": {
                        "line": 108,
                        "character": 69
                      }
                    }
                  },
                  "twoStateIndex": "NEITHER"
                },
                "fieldName": "selector",
                "tag": {
                  "scope": {
                    "scopeStack": [
                      {
                        "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                      },
                      {
                        "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                        "scopeId": 6
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
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 32
                  },
                  "cvlRange": {
                    "#class": "spec.cvlast.CVLRange.Range",
                    "specFile": "certora/spec/ERC20.spec",
                    "start": {
                      "line": 107,
                      "character": 9
                    },
                    "end": {
                      "line": 107,
                      "character": 10
                    }
                  }
                }
              },
              "r": {
                "#class": "spec.cvlast.CVLExp.FieldSelectExp",
                "structExp": {
                  "#class": "spec.cvlast.CVLExp.Constant.SignatureLiteralExp",
                  "function": {
                    "#class": "spec.cvlast.QualifiedMethodSignature.QualifiedMethodSig",
                    "qualifiedMethodName": {
                      "#class": "spec.cvlast.QualifiedFunction",
                      "host": {
                        "name": "ERC20"
                      },
                      "methodId": "approve"
                    },
                    "params": [
                      {
                        "#class": "spec.cvlast.VMParam.Unnamed",
                        "vmType": {
                          "#class": "ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$address"
                        }
                      },
                      {
                        "#class": "spec.cvlast.VMParam.Unnamed",
                        "vmType": {
                          "#class": "ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK",
                          "bitwidth": 256
                        }
                      }
                    ],
                    "res": [
                    ]
                  },
                  "tag": {
                    "scope": {
                      "scopeStack": [
                        {
                          "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                        },
                        {
                          "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                          "scopeId": 6
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
                      "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
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
                    "cvlRange": {
                      "#class": "spec.cvlast.CVLRange.Range",
                      "specFile": "certora/spec/ERC20.spec",
                      "start": {
                        "line": 107,
                        "character": 27
                      },
                      "end": {
                        "line": 107,
                        "character": 48
                      }
                    },
                    "annotation": {
                      "#class": "ReflectivePolymorphicSerializer::spec.cvlast.CVLExp$Constant$StructLit",
                      "fieldNameToEntry": {
                        "selector": {
                          "#class": "spec.cvlast.CVLExp.Constant.NumberLit",
                          "n": "95ea7b3",
                          "tag": {
                            "scope": {
                              "scopeStack": [
                                {
                                  "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                                },
                                {
                                  "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                                  "scopeId": 6
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
                              "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                              "k": 32
                            },
                            "cvlRange": {
                              "#class": "spec.cvlast.CVLRange.Empty"
                            }
                          }
                        },
                        "isPure": {
                          "#class": "spec.cvlast.CVLExp.Constant.BoolLit",
                          "b": "0",
                          "tag": {
                            "scope": {
                              "scopeStack": [
                                {
                                  "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                                },
                                {
                                  "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                                  "scopeId": 6
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
                              "#class": "spec.cvlast.CVLRange.Empty"
                            }
                          }
                        },
                        "isView": {
                          "#class": "spec.cvlast.CVLExp.Constant.BoolLit",
                          "b": "0",
                          "tag": {
                            "scope": {
                              "scopeStack": [
                                {
                                  "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                                },
                                {
                                  "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                                  "scopeId": 6
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
                              "#class": "spec.cvlast.CVLRange.Empty"
                            }
                          }
                        },
                        "isPayable": {
                          "#class": "spec.cvlast.CVLExp.Constant.BoolLit",
                          "b": "0",
                          "tag": {
                            "scope": {
                              "scopeStack": [
                                {
                                  "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                                },
                                {
                                  "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                                  "scopeId": 6
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
                              "#class": "spec.cvlast.CVLRange.Empty"
                            }
                          }
                        },
                        "isFallback": {
                          "#class": "spec.cvlast.CVLExp.Constant.BoolLit",
                          "b": "0",
                          "tag": {
                            "scope": {
                              "scopeStack": [
                                {
                                  "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                                },
                                {
                                  "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                                  "scopeId": 6
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
                              "#class": "spec.cvlast.CVLRange.Empty"
                            }
                          }
                        },
                        "numberOfArguments": {
                          "#class": "spec.cvlast.CVLExp.Constant.NumberLit",
                          "n": "2",
                          "tag": {
                            "scope": {
                              "scopeStack": [
                                {
                                  "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                                },
                                {
                                  "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                                  "scopeId": 6
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
                              "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                              "k": 256
                            },
                            "cvlRange": {
                              "#class": "spec.cvlast.CVLRange.Empty"
                            }
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
                              "scopeId": 6
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
                          "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
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
                        "cvlRange": {
                          "#class": "spec.cvlast.CVLRange.Empty"
                        }
                      }
                    }
                  }
                },
                "fieldName": "selector",
                "tag": {
                  "scope": {
                    "scopeStack": [
                      {
                        "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                      },
                      {
                        "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                        "scopeId": 6
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
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 32
                  },
                  "cvlRange": {
                    "#class": "spec.cvlast.CVLRange.Range",
                    "specFile": "certora/spec/ERC20.spec",
                    "start": {
                      "line": 107,
                      "character": 27
                    },
                    "end": {
                      "line": 107,
                      "character": 48
                    }
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
                      "scopeId": 6
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
                    "line": 107,
                    "character": 9
                  },
                  "end": {
                    "line": 107,
                    "character": 57
                  }
                }
              }
            },
            "r": {
              "#class": "spec.cvlast.CVLExp.RelopExp.EqExp",
              "l": {
                "#class": "spec.cvlast.CVLExp.FieldSelectExp",
                "structExp": {
                  "#class": "spec.cvlast.CVLExp.VariableExp",
                  "id": "f",
                  "tag": {
                    "scope": {
                      "scopeStack": [
                        {
                          "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                        },
                        {
                          "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                          "scopeId": 6
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
                      "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
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
                    "cvlRange": {
                      "#class": "spec.cvlast.CVLRange.Range",
                      "specFile": "certora/spec/ERC20.spec",
                      "start": {
                        "line": 106,
                        "character": 4
                      },
                      "end": {
                        "line": 108,
                        "character": 69
                      }
                    }
                  },
                  "twoStateIndex": "NEITHER"
                },
                "fieldName": "selector",
                "tag": {
                  "scope": {
                    "scopeStack": [
                      {
                        "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                      },
                      {
                        "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                        "scopeId": 6
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
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 32
                  },
                  "cvlRange": {
                    "#class": "spec.cvlast.CVLRange.Range",
                    "specFile": "certora/spec/ERC20.spec",
                    "start": {
                      "line": 107,
                      "character": 61
                    },
                    "end": {
                      "line": 107,
                      "character": 62
                    }
                  }
                }
              },
              "r": {
                "#class": "spec.cvlast.CVLExp.FieldSelectExp",
                "structExp": {
                  "#class": "spec.cvlast.CVLExp.Constant.SignatureLiteralExp",
                  "function": {
                    "#class": "spec.cvlast.QualifiedMethodSignature.QualifiedMethodSig",
                    "qualifiedMethodName": {
                      "#class": "spec.cvlast.QualifiedFunction",
                      "host": {
                        "name": "ERC20"
                      },
                      "methodId": "increaseAllowance"
                    },
                    "params": [
                      {
                        "#class": "spec.cvlast.VMParam.Unnamed",
                        "vmType": {
                          "#class": "ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$address"
                        }
                      },
                      {
                        "#class": "spec.cvlast.VMParam.Unnamed",
                        "vmType": {
                          "#class": "ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK",
                          "bitwidth": 256
                        }
                      }
                    ],
                    "res": [
                    ]
                  },
                  "tag": {
                    "scope": {
                      "scopeStack": [
                        {
                          "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                        },
                        {
                          "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                          "scopeId": 6
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
                      "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
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
                    "cvlRange": {
                      "#class": "spec.cvlast.CVLRange.Range",
                      "specFile": "certora/spec/ERC20.spec",
                      "start": {
                        "line": 107,
                        "character": 79
                      },
                      "end": {
                        "line": 107,
                        "character": 110
                      }
                    },
                    "annotation": {
                      "#class": "ReflectivePolymorphicSerializer::spec.cvlast.CVLExp$Constant$StructLit",
                      "fieldNameToEntry": {
                        "selector": {
                          "#class": "spec.cvlast.CVLExp.Constant.NumberLit",
                          "n": "39509351",
                          "tag": {
                            "scope": {
                              "scopeStack": [
                                {
                                  "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                                },
                                {
                                  "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                                  "scopeId": 6
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
                              "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                              "k": 32
                            },
                            "cvlRange": {
                              "#class": "spec.cvlast.CVLRange.Empty"
                            }
                          }
                        },
                        "isPure": {
                          "#class": "spec.cvlast.CVLExp.Constant.BoolLit",
                          "b": "0",
                          "tag": {
                            "scope": {
                              "scopeStack": [
                                {
                                  "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                                },
                                {
                                  "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                                  "scopeId": 6
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
                              "#class": "spec.cvlast.CVLRange.Empty"
                            }
                          }
                        },
                        "isView": {
                          "#class": "spec.cvlast.CVLExp.Constant.BoolLit",
                          "b": "0",
                          "tag": {
                            "scope": {
                              "scopeStack": [
                                {
                                  "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                                },
                                {
                                  "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                                  "scopeId": 6
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
                              "#class": "spec.cvlast.CVLRange.Empty"
                            }
                          }
                        },
                        "isPayable": {
                          "#class": "spec.cvlast.CVLExp.Constant.BoolLit",
                          "b": "0",
                          "tag": {
                            "scope": {
                              "scopeStack": [
                                {
                                  "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                                },
                                {
                                  "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                                  "scopeId": 6
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
                              "#class": "spec.cvlast.CVLRange.Empty"
                            }
                          }
                        },
                        "isFallback": {
                          "#class": "spec.cvlast.CVLExp.Constant.BoolLit",
                          "b": "0",
                          "tag": {
                            "scope": {
                              "scopeStack": [
                                {
                                  "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                                },
                                {
                                  "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                                  "scopeId": 6
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
                              "#class": "spec.cvlast.CVLRange.Empty"
                            }
                          }
                        },
                        "numberOfArguments": {
                          "#class": "spec.cvlast.CVLExp.Constant.NumberLit",
                          "n": "2",
                          "tag": {
                            "scope": {
                              "scopeStack": [
                                {
                                  "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                                },
                                {
                                  "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                                  "scopeId": 6
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
                              "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                              "k": 256
                            },
                            "cvlRange": {
                              "#class": "spec.cvlast.CVLRange.Empty"
                            }
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
                              "scopeId": 6
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
                          "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
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
                        "cvlRange": {
                          "#class": "spec.cvlast.CVLRange.Empty"
                        }
                      }
                    }
                  }
                },
                "fieldName": "selector",
                "tag": {
                  "scope": {
                    "scopeStack": [
                      {
                        "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                      },
                      {
                        "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                        "scopeId": 6
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
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 32
                  },
                  "cvlRange": {
                    "#class": "spec.cvlast.CVLRange.Range",
                    "specFile": "certora/spec/ERC20.spec",
                    "start": {
                      "line": 107,
                      "character": 79
                    },
                    "end": {
                      "line": 107,
                      "character": 110
                    }
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
                      "scopeId": 6
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
                    "line": 107,
                    "character": 61
                  },
                  "end": {
                    "line": 107,
                    "character": 119
                  }
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
                    "scopeId": 6
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
                  "line": 107,
                  "character": 9
                },
                "end": {
                  "line": 107,
                  "character": 119
                }
              }
            }
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
          "line": 106,
          "character": 4
        },
        "end": {
          "line": 108,
          "character": 69
        }
      }
    }
  ],
  "76": [
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
          "line": 106,
          "character": 4
        },
        "end": {
          "line": 108,
          "character": 69
        }
      }
    }
  ],
  "77": [
    {
      "key": {
        "name": "tac.meta",
        "type": "vc.data.TACMetaInfo",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "source": 0,
        "begin": 17760,
        "len": 21,
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
  "78": [
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
      "value": 1021
    }
  ],
  "79": [
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
  "80": [
    {
      "key": {
        "name": "tac.meta",
        "type": "vc.data.TACMetaInfo",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "source": 0,
        "begin": 17760,
        "len": 34,
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
  "81": [
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
      "value": 1018
    }
  ],
  "82": [
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
              "namePrefix": "R117",
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
                  "value": 1019
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
                "namePrefix": "R117",
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
                    "value": 1019
                  }
                ]
              },
              "baseSlot": {
                "#class": "vc.data.TACSymbol.Var.Full",
                "namePrefix": "CANON91",
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
                "namePrefix": "CANON90",
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
      "value": 1021
    }
  ],
  "83": [
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
}