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
	}
	UninterpretedFunctions {
		CANON115:JSON{"name":"CANON115","paramSorts":[],"returnSort":{"#class":"tac.Tag.Int"},"attribute":"Ghost","cvlResultType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Mathint"},"cvlParamTypes":[],"declarationName":"CANON115"}
	}
	tacM0x20@1:bv256
	tacM0x20@3:bv256
	tacCaller@2:bv256
	tacCalldatabufCANON0@2:bv256
	tacM0x0!!43:bv256
	tacM0x0!!46:bv256
	tacM0x0!!77:bv256
	tacM0x0!!80:bv256
	tacAddress!!26:bv256
	tacAddress!!60:bv256
	tacOrigin!!118:bv256
	CANON114!!154:bool
	tacCallvalue@2:bv256
	lastReverted:bool
	lastReverted@1:bool
	lastReverted@2:bool
	lastReverted@3:bool
	tacM0x0!!167:bv256
	tacExtcodesize!!0:wordmap
	CANON28!!2:wordmap
	CANON83!!3:wordmap
	tacCalldatasize@1:bv256
	tacCalldatasize@2:bv256
	tacCalldatasize@3:bv256
	tacCalldatasize!!100:bv256
	tacM0x0@1:bv256
	tacM0x0@2:bv256
	tacM0x0@3:bv256
	tacExtcodesize:wordmap
	CANON100:int
	CANON101:int
	CANON102:bool
	CANON103:int
	CANON104:int
	CANON105:bool
	CANON107:bool
	CANON108:int
	CANON109:int
	CANON110:bool
	CANON111:bool
	CANON112:bool
	CANON113:bool
	CANON114:bool
	CANON115:int
	CANON107!!150:bool
	tacSighash!!5:bv256
	tacSighash!!6:bv256
	tacSighash!!7:bv256
	tacCalldatasize!!17:bv256
	tacCalldatasize!!51:bv256
	tacBalance:wordmap
	tacTimestamp!!128:bv256
	tacNumber@2:bv256
	tacBalance!!1:wordmap
	B8:bool
	B9:bool
	R4:bv256
	B10:bool
	B12:bool
	B13:bool
	B14:bool
	B18:bool
	B19:bool
	B20:bool
	B22:bool
	B23:bool
	B25:bool
	B28:bool
	B29:bool
	B30:bool
	B31:bool
	B32:bool
	B33:bool
	B34:bool
	B35:bool
	B37:bool
	B39:bool
	B41:bool
	B52:bool
	B53:bool
	B54:bool
	B56:bool
	B57:bool
	B59:bool
	B62:bool
	B63:bool
	B64:bool
	B65:bool
	B66:bool
	B67:bool
	B68:bool
	B69:bool
	B71:bool
	B73:bool
	B75:bool
	B85:bool
	B86:bool
	B87:bool
	B88:bool
	B89:bool
	B90:bool
	B91:bool
	B92:bool
	I15:int
	I16:int
	I93:int
	I94:int
	I95:int
	I96:int
	I97:int
	M98:bytemap
	R11:bv256
	R21:bv256
	R24:bv256
	R27:bv256
	R36:bv256
	R38:bv256
	R40:bv256
	R42:bv256
	R44:(uninterp) skey
	R45:bv256
	R48:(uninterp) skey
	R49:bv256
	R50:bv256
	R55:bv256
	R58:bv256
	R61:bv256
	R70:bv256
	R72:bv256
	R74:bv256
	R76:bv256
	R78:(uninterp) skey
	R79:bv256
	R82:(uninterp) skey
	R83:bv256
	R84:bv256
	R99:bv256
	B101:bool
	B102:bool
	B105:bool
	B108:bool
	B110:bool
	B113:bool
	B116:bool
	B119:bool
	B121:bool
	B124:bool
	B126:bool
	B129:bool
	B131:bool
	B134:bool
	B143:bool
	B146:bool
	B153:bool
	B156:bool
	B157:bool
	B158:bool
	B159:bool
	B160:bool
	B161:bool
	B163:bool
	B165:bool
	I104:int
	I109:int
	I115:int
	I120:int
	I125:int
	I130:int
	I133:int
	I139:int
	I144:int
	I145:int
	I147:int
	I148:int
	I151:int
	I152:int
	I171:int
	I172:int
	R103:bv256
	R106:bv256
	R111:bv256
	R117:bv256
	R122:bv256
	R127:bv256
	R132:bv256
	R135:bv256
	R136:bv256
	R137:bv256
	R138:bv256
	R141:bv256
	R142:bv256
	R155:bv256
	R162:bv256
	R164:bv256
	R166:bv256
	R168:(uninterp) skey
	R169:bv256
	R170:bv256
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
	LCANON3@3:bool
	LCANON4@1:bool
	LCANON4@3:bool
	LCANON5@1:bool
	LCANON5@3:bool
	LCANON6@1:bool
	LCANON6@3:bool
	LCANON7@1:bv256
	LCANON7@3:bv256
	LCANON8@1:bv256
	LCANON8@3:bv256
	LCANON9@1:bool
	LCANON9@3:bool
	tacCallvalue!!112:bv256
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
	CANON47:bytemap
	CANON48:bytemap
	CANON49:bv256
	CANON50:bv256
	CANON51:bool
	CANON52:bool
	CANON53:bv256
	CANON54:int
	CANON55:bool
	CANON56:bv256
	CANON57:int
	CANON58:bool
	CANON59:bv256
	CANON60:int
	CANON61:bool
	CANON62:bv256
	CANON63:int
	CANON64:bool
	CANON65:bv256
	CANON66:int
	CANON67:bool
	CANON68:bv256
	CANON69:int
	CANON70:bool
	CANON71:bv256
	CANON72:int
	CANON73:bool
	CANON74:bv256
	CANON75:bv256
	CANON76:bv256
	CANON77:bv256
	CANON78:int
	CANON79:bv256
	CANON80:bv256
	CANON81:bool
	CANON82:bool
	CANON83:wordmap
	CANON86@2:bv256
	CANON87:int
	CANON88:int
	CANON89:bool
	CANON90:bool
	CANON91:bool
	CANON92:bv256
	CANON93:bool
	CANON94:bool
	CANON95:bv256
	CANON96:bool
	CANON97:bool
	CANON98:bool
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
	LCANON24@2:bool
	LCANON25@2:bv256
	LCANON26@2:bool
	LCANON27@2:bv256
	LCANON28@2:bool
	LCANON29@2:bv256
	LCANON30@2:bv256
	LCANON31@2:bool
	LCANON32@2:bv256
	LCANON33@2:bv256
	LCANON34@2:bv256
	LCANON35@2:bv256
	LCANON36@2:bv256
	tacContractAtCANON0:bv256
	tacM0x20!!47:bv256
	tacM0x20!!81:bv256
	lastHasThrown:bool
	lastHasThrown@1:bool
	lastHasThrown@2:bool
	lastHasThrown@3:bool
	tacAddress!!114:bv256
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
	tacCaller!!107:bv256
	tacBalance!!140:wordmap
	CANON105!!149:bool
	tacTimestamp@2:bv256
	tacSighash@1:bv256
	tacSighash@2:bv256
	tacSighash@3:bv256
	tacNumber!!123:bv256
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
		AssignHavocCmd CANON50:14
		AssignHavocCmd CANON83!!3:15
		AssignHavocCmd R4:16
		AssignHavocCmd tacSighash!!5:17
		AssignHavocCmd tacSighash!!6:17
		AssignHavocCmd tacSighash!!7:17
		AssignExpCmd CANON0:18 0x70a08231
		AssignExpCmd CANON1:19 false
		AssignExpCmd CANON2:20 true
		AssignExpCmd CANON3:21 false
		AssignExpCmd CANON4:22 0x1
		AssignExpCmd CANON5:23 false
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
		AssignExpCmd B8:24 Gt(Select(tacExtcodesize!!0:0 Apply(to_skey:bif R4:16) ) 0x0 )
		AssumeCmd B8:24
		AnnotationCmd JSON{"key":{"name":"cvl.label.end","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		AnnotationCmd JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Message","s":"assumptions about contracts' addresses"}}
		NopCmd
		AssumeExpCmd Gt(R4:16 0x0 )
		NopCmd
		AssumeExpCmd Le(R4:16 0xffffffffffffffffffffffffffffffffffffffff )
		AnnotationCmd JSON{"key":{"name":"cvl.label.end","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		AnnotationCmd JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Message","s":"assumptions about starting balances"}}
		AssignExpCmd R11:24 Select(tacBalance!!1:1 Apply(to_skey:bif R4:16) )
		NopCmd
		AssumeExpCmd Ge(R11:24 0x0 )
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
		AnnotationCmd:25 JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Cmd","cmd":{"cmd_type":"spec.cvlast.CVLCmd.Simple.Definition","cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/spec/ERC20.spec","start":{"line":96,"character":4},"end":{"line":96,"character":58}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Mathint"},"idL":[{"#class":"spec.cvlast.CVLLhs.Id","cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/spec/ERC20.spec","start":{"line":96,"character":4},"end":{"line":96,"character":28}},"id":"allowance_before","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":6}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Mathint"},"cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/spec/ERC20.spec","start":{"line":96,"character":4},"end":{"line":96,"character":58}}}}],"exp":{"#class":"spec.cvlast.CVLExp.ApplyExp.ContractFunction.Concrete","methodIdWithCallContext":{"#class":"spec.cvlast.ConcreteMethod","signature":{"#class":"spec.cvlast.ExternalQualifiedMethodSignature.ExternalQualifiedMethodSig","wrapped":{"#class":"spec.cvlast.QualifiedMethodSignature.QualifiedMethodSig","qualifiedMethodName":{"#class":"spec.cvlast.QualifiedFunction","host":{"name":"ERC20"},"methodId":"allowance"},"params":[{"#class":"spec.cvlast.VMParam.Named","name":"owner","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$address"}},{"#class":"spec.cvlast.VMParam.Named","name":"spender","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$address"}}],"res":[{"#class":"spec.cvlast.VMParam.Unnamed","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256}}]},"sighashInt":{"n":"dd62ed3e"}}},"args":[{"#class":"spec.cvlast.CVLExp.VariableExp","id":"holder","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":6}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"},"cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/spec/ERC20.spec","start":{"line":96,"character":4},"end":{"line":96,"character":58}}},"twoStateIndex":"NEITHER"},{"#class":"spec.cvlast.CVLExp.VariableExp","id":"spender","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":6}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"},"cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/spec/ERC20.spec","start":{"line":96,"character":4},"end":{"line":96,"character":58}}},"twoStateIndex":"NEITHER"}],"noRevert":true,"storage":{"#class":"spec.cvlast.CVLExp.VariableExp","id":"lastStorage","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":6}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.VMInternal.BlockchainState"},"cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/spec/ERC20.spec","start":{"line":96,"character":4},"end":{"line":96,"character":58}}},"twoStateIndex":"NEITHER"},"isWhole":false,"tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":6}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.VM","descriptor":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256},"context":{"#class":"spec.cvlast.typedescriptors.FromVMContext.ReturnValue"}},"cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/spec/ERC20.spec","start":{"line":96,"character":31},"end":{"line":96,"character":40}},"annotation":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.CallResolution$DirectPassing","target":{"methodSignature":{"#class":"spec.cvlast.ExternalQualifiedMethodSignature.ExternalQualifiedMethodSig","wrapped":{"#class":"spec.cvlast.QualifiedMethodSignature.QualifiedMethodSig","qualifiedMethodName":{"#class":"spec.cvlast.QualifiedFunction","host":{"name":"ERC20"},"methodId":"allowance"},"params":[{"#class":"spec.cvlast.VMParam.Named","name":"owner","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$address"}},{"#class":"spec.cvlast.VMParam.Named","name":"spender","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$address"}}],"res":[{"#class":"spec.cvlast.VMParam.Unnamed","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256}}]},"sighashInt":{"n":"dd62ed3e"}},"definitelyNonPayable":true,"annotation":{"visibility":"EXTERNAL","envFree":true,"library":false},"stateMutability":"view","tag":{"#class":"spec.cvlast.CVLImportedFunctionTag.WithMethodInfo","evmMethodInfo":{"sigHash":"dd62ed3e","name":"allowance","argTypes":[{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.address"},{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.address"}],"resultTypes":[{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256}],"stateMutability":"view","envfreeInfo":{"#class":"bridge.EnvfreeInfo.Unknown"},"isConstant":false,"paramNames":["owner","spender"],"isLibrary":false}}},"hasEnv":false}}},"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":6}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}}}}}
		AssignExpCmd:26 I15 CANON12:2
		AssignExpCmd:27 I16 CANON13:3
	}
	Block 0_0_0_1_0_0 Succ [1_0_0_0_0_0] {
		AnnotationCmd:25 JSON{"key":{"name":"call.trace.push","type":"analysis.icfg.Inliner$CallStack$PushRecord","erasureStrategy":"Canonical"},"value":"rO0ABXNyACphbmFseXNpcy5pY2ZnLklubGluZXIkQ2FsbFN0YWNrJFB1c2hSZWNvcmSX8+DCTLCH+AIAA0kACGNhbGxlZUlkTAAGY2FsbGVldAATTHZjL2RhdGEvTWV0aG9kUmVmO0wAB3N1bW1hcnl0ABVMdmMvZGF0YS9DYWxsU3VtbWFyeTt4cAAAAAFzcgARdmMuZGF0YS5NZXRob2RSZWbJlJTzzU9pGAIAA0wABGF0dHJ0ABdMc2NlbmUvTWV0aG9kQXR0cmlidXRlO0wACmNvbnRyYWN0SWR0ABZMamF2YS9tYXRoL0JpZ0ludGVnZXI7TAAHc2lnSGFzaHQAEExldm0vU2lnaGFzaEludDt4cHNyABxzY2VuZS5NZXRob2RBdHRyaWJ1dGUkQ29tbW9uNHjdebdr9XMCAAB4cgAVc2NlbmUuTWV0aG9kQXR0cmlidXRlcYg2pYWutuUCAAB4cHNyABRqYXZhLm1hdGguQmlnSW50ZWdlcoz8nx+pO/sdAwAGSQAIYml0Q291bnRJAAliaXRMZW5ndGhJABNmaXJzdE5vbnplcm9CeXRlTnVtSQAMbG93ZXN0U2V0Qml0SQAGc2lnbnVtWwAJbWFnbml0dWRldAACW0J4cgAQamF2YS5sYW5nLk51bWJlcoaslR0LlOCLAgAAeHD///////////////7////+AAAAAXVyAAJbQqzzF/gGCFTgAgAAeHAAAAAQzkYEoAAAAAAAAAAAAAAAA3hzcgAOZXZtLlNpZ2hhc2hJbnRUdcqNMXEgeAIAAUwAAW5xAH4ABnhwc3EAfgAM///////////////+/////gAAAAF1cQB+ABAAAAAE3WLtPnhw"}
		AssignHavocCmd:25 tacCalldatasize!!17:28
		NopCmd
		AssumeExpCmd Apply(add_noofl:bif 0x4 0x40)
		NopCmd
		AssumeExpCmd Apply(add_noofl:bif 0x4 0x0)
		AssignExpCmd:25 B20 LAnd(Ge(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff I15 ) Le(0x0 I15 ) )
		AssertCmd:25 B20 "sanity bounds check on cvl to vm encoding of certoraArg14071410:int failed"
		AssignExpCmd:25 R21 Apply(safe_math_narrow:bif I15)
		NopCmd
		AssumeExpCmd Apply(add_noofl:bif 0x4 0x20)
		AssignExpCmd:25 B23 LAnd(Ge(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff I16 ) Le(0x0 I16 ) )
		AssertCmd:25 B23 "sanity bounds check on cvl to vm encoding of certoraArg14111412:int failed"
		AssignExpCmd:25 R24 Apply(safe_math_narrow:bif I16)
		NopCmd
		AssumeExpCmd Eq(0x44 tacCalldatasize!!17:28 )
		LabelCmd:25 "Start procedure ERC20-allowance(address,address)"
		AnnotationCmd:25 JSON{"key":{"name":"fps.free-pointer-is-scalarized","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true}
		AssignExpCmd:25 R27:24 Select(tacExtcodesize!!0:0 Apply(to_skey:bif R4:29) )
		NopCmd
		AssumeExpCmd Gt(R27:24 0x0 )
		AnnotationCmd:25 JSON{"key":{"name":"internal.func.finder.info","type":"analysis.ip.InternalFunctionFinderReport","erasureStrategy":"Erased"},"value":"rO0ABXNyAChhbmFseXNpcy5pcC5JbnRlcm5hbEZ1bmN0aW9uRmluZGVyUmVwb3J0ian+bYn1VdACAAFMABN1bnJlc29sdmVkRnVuY3Rpb25zdAAPTGphdmEvdXRpbC9TZXQ7eHBzcgAhZGF0YXN0cnVjdHVyZXMuTGlua2VkQXJyYXlIYXNoU2V0AAAAAAAAAAEDAAJGAApsb2FkRmFjdG9yTAAJaGFzaFRhYmxldAAuTGRhdGFzdHJ1Y3R1cmVzL2FycmF5aGFzaHRhYmxlL0FycmF5SGFzaFRhYmxlO3hwdwgAAAAAQAAAAHg="}
		AnnotationCmd:25 JSON{"key":{"name":"fps.free-pointer-is-scalarized","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true}
		NopCmd
		AssumeExpCmd LNot(Lt(tacCalldatasize!!17:28 0x4 ) )
		NopCmd
		AssumeExpCmd LNot(Gt(0x70a08231 tacSighash!!5:17 ) )
		NopCmd
		AssumeExpCmd LNot(Gt(0xa9059cbb tacSighash!!5:17 ) )
		NopCmd
		AssumeExpCmd LNot(Eq(0xa9059cbb tacSighash!!5:17 ) )
		NopCmd
		AssumeExpCmd LNot(Eq(0xb2bdfa7b tacSighash!!5:17 ) )
		NopCmd
		AssumeExpCmd LNot(Eq(0xd0e30db0 tacSighash!!5:17 ) )
		NopCmd
		AssumeExpCmd Eq(0xdd62ed3e tacSighash!!5:17 )
		AssumeCmd:30 true
		AssignExpCmd:31 R36:32 Sub(tacCalldatasize!!17:28 0x4 )
		NopCmd
		AssumeExpCmd LNot(Slt(R36:32 0x40 ) )
		NopCmd
		AssumeExpCmd Le(R21 0xffffffffffffffffffffffffffffffffffffffff )
		NopCmd
		AssumeExpCmd Le(R24 0xffffffffffffffffffffffffffffffffffffffff )
		AnnotationCmd:25 JSON{"key":{"name":"internal.func.start","type":"analysis.ip.InternalFuncStartAnnotation","erasureStrategy":"CallTrace"},"value":{"id":0,"startPc":4858,"args":[{"s":{"namePrefix":"R21","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1012}]},"offset":1,"sort":"SCALAR"},{"s":{"namePrefix":"R24","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1012}]},"offset":2,"sort":"SCALAR"}],"methodSignature":{"#class":"spec.cvlast.QualifiedMethodSignature.QualifiedMethodSig","qualifiedMethodName":{"#class":"spec.cvlast.QualifiedFunction","host":{"name":"ERC20"},"methodId":"allowance"},"params":[{"#class":"spec.cvlast.VMParam.Named","name":"owner","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$address"}},{"#class":"spec.cvlast.VMParam.Named","name":"spender","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$address"}}],"res":[{"#class":"spec.cvlast.VMParam.Unnamed","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256}}]},"stackOffsetToArgPos":{"1":0,"2":1},"callSiteSrc":{"source":0,"begin":5647,"len":535,"jumpType":"ENTER","address":"ce4604a0000000000000000000000003","sourceContext":{"indexToFilepath":{"0":"contracts/ERC20.sol","1":"contracts/IERC20.sol","2":"contracts/IERC20Metadata.sol"},"sourceDir":".post_autofinders.0"}}}}
		AssignExpCmd:33 R44:34 Apply(hash_3_keccak:bif Apply(skey_basic:bif 0x40) Apply(to_skey:bif R21:35) Apply(skey_basic:bif 0x1))
		AssignExpCmd:36 R48:34 Apply(hash_3_keccak:bif Apply(skey_basic:bif 0x40) Apply(to_skey:bif R24:35) R44:37)
		AssignExpCmd:38 R49:34 Select(CANON28!!2:4 R48:39 )
		AnnotationCmd:25 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet","value":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R49","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1019}]},"displayPath":{"#class":"analysis.storage.DisplayPath.MapAccess","key":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R24","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1017}]},"keyTyp":{"#class":"tac.TACStorageType.IntegralType","typeLabel":"address","numBytes":"14","descriptor":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$address"},"lowerBound":null,"upperBound":null},"base":{"#class":"analysis.storage.DisplayPath.MapAccess","key":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R21","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1017}]},"keyTyp":{"#class":"tac.TACStorageType.IntegralType","typeLabel":"address","numBytes":"14","descriptor":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$address"},"lowerBound":null,"upperBound":null},"base":{"#class":"analysis.storage.DisplayPath.Root","name":"_allowances"}}},"storageType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256},"contractInstance":"ce4604a0000000000000000000000003","linkableStorageReadId":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet.None"}}}
		AnnotationCmd:25 JSON{"key":{"name":"internal.func.end","type":"analysis.ip.InternalFuncExitAnnotation","erasureStrategy":"Canonical"},"value":{"id":0,"rets":[{"s":{"namePrefix":"R49","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1023}]},"offset":0}],"functionLayout":{"0":{"#class":"analysis.ip.InternalFuncValueLocation.Scalar"}}}}
		AnnotationCmd:25 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.EVMFunctionReturnWrite","returnbufOffset":"0","returnValueSym":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R49","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1023}]},"callIndex":1}}
		AnnotationCmd:25 JSON{"key":{"name":"tac.return.path","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		LabelCmd:25 "End procedure ERC20-allowance(address,address)"
		AssignExpCmd:25 CANON33:40 R49:34
		AnnotationCmd:25 JSON{"key":{"name":"call.trace.pop","type":"analysis.icfg.Inliner$CallStack$PopRecord","erasureStrategy":"Canonical"},"value":"rO0ABXNyAClhbmFseXNpcy5pY2ZnLklubGluZXIkQ2FsbFN0YWNrJFBvcFJlY29yZPAPfwSLdCWJAgABSQAIY2FsbGVlSWR4cAAAAAE="}
	}
	Block 0_0_0_3_0_0 Succ [3_0_0_0_0_0] {
		AnnotationCmd:41 JSON{"key":{"name":"call.trace.push","type":"analysis.icfg.Inliner$CallStack$PushRecord","erasureStrategy":"Canonical"},"value":"rO0ABXNyACphbmFseXNpcy5pY2ZnLklubGluZXIkQ2FsbFN0YWNrJFB1c2hSZWNvcmSX8+DCTLCH+AIAA0kACGNhbGxlZUlkTAAGY2FsbGVldAATTHZjL2RhdGEvTWV0aG9kUmVmO0wAB3N1bW1hcnl0ABVMdmMvZGF0YS9DYWxsU3VtbWFyeTt4cAAAAANzcgARdmMuZGF0YS5NZXRob2RSZWbJlJTzzU9pGAIAA0wABGF0dHJ0ABdMc2NlbmUvTWV0aG9kQXR0cmlidXRlO0wACmNvbnRyYWN0SWR0ABZMamF2YS9tYXRoL0JpZ0ludGVnZXI7TAAHc2lnSGFzaHQAEExldm0vU2lnaGFzaEludDt4cHNyABxzY2VuZS5NZXRob2RBdHRyaWJ1dGUkQ29tbW9uNHjdebdr9XMCAAB4cgAVc2NlbmUuTWV0aG9kQXR0cmlidXRlcYg2pYWutuUCAAB4cHNyABRqYXZhLm1hdGguQmlnSW50ZWdlcoz8nx+pO/sdAwAGSQAIYml0Q291bnRJAAliaXRMZW5ndGhJABNmaXJzdE5vbnplcm9CeXRlTnVtSQAMbG93ZXN0U2V0Qml0SQAGc2lnbnVtWwAJbWFnbml0dWRldAACW0J4cgAQamF2YS5sYW5nLk51bWJlcoaslR0LlOCLAgAAeHD///////////////7////+AAAAAXVyAAJbQqzzF/gGCFTgAgAAeHAAAAAQzkYEoAAAAAAAAAAAAAAAA3hzcgAOZXZtLlNpZ2hhc2hJbnRUdcqNMXEgeAIAAUwAAW5xAH4ABnhwc3EAfgAM///////////////+/////gAAAAF1cQB+ABAAAAAE3WLtPnhw"}
		AssignHavocCmd:41 tacCalldatasize!!51:28
		NopCmd
		AssumeExpCmd Apply(add_noofl:bif 0x4 0x40)
		NopCmd
		AssumeExpCmd Apply(add_noofl:bif 0x4 0x0)
		AssignExpCmd:41 B54 LAnd(Ge(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff I171 ) Le(0x0 I171 ) )
		AssertCmd:41 B54 "sanity bounds check on cvl to vm encoding of certoraArg23342335:int failed"
		AssignExpCmd:41 R55 Apply(safe_math_narrow:bif I171)
		NopCmd
		AssumeExpCmd Apply(add_noofl:bif 0x4 0x20)
		AssignExpCmd:41 B57 LAnd(Ge(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff I172 ) Le(0x0 I172 ) )
		AssertCmd:41 B57 "sanity bounds check on cvl to vm encoding of certoraArg23362337:int failed"
		AssignExpCmd:41 R58 Apply(safe_math_narrow:bif I172)
		NopCmd
		AssumeExpCmd Eq(0x44 tacCalldatasize!!51:28 )
		LabelCmd:41 "Start procedure ERC20-allowance(address,address)"
		AnnotationCmd:41 JSON{"key":{"name":"fps.free-pointer-is-scalarized","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true}
		AssignExpCmd:41 R61:24 Select(tacExtcodesize!!0:0 Apply(to_skey:bif R4:29) )
		NopCmd
		AssumeExpCmd Gt(R61:24 0x0 )
		AnnotationCmd:41 JSON{"key":{"name":"internal.func.finder.info","type":"analysis.ip.InternalFunctionFinderReport","erasureStrategy":"Erased"},"value":"rO0ABXNyAChhbmFseXNpcy5pcC5JbnRlcm5hbEZ1bmN0aW9uRmluZGVyUmVwb3J0ian+bYn1VdACAAFMABN1bnJlc29sdmVkRnVuY3Rpb25zdAAPTGphdmEvdXRpbC9TZXQ7eHBzcgAhZGF0YXN0cnVjdHVyZXMuTGlua2VkQXJyYXlIYXNoU2V0AAAAAAAAAAEDAAJGAApsb2FkRmFjdG9yTAAJaGFzaFRhYmxldAAuTGRhdGFzdHJ1Y3R1cmVzL2FycmF5aGFzaHRhYmxlL0FycmF5SGFzaFRhYmxlO3hwdwgAAAAAQAAAAHg="}
		AnnotationCmd:41 JSON{"key":{"name":"fps.free-pointer-is-scalarized","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true}
		NopCmd
		AssumeExpCmd LNot(Lt(tacCalldatasize!!51:28 0x4 ) )
		NopCmd
		AssumeExpCmd LNot(Gt(0x70a08231 tacSighash!!7:17 ) )
		NopCmd
		AssumeExpCmd LNot(Gt(0xa9059cbb tacSighash!!7:17 ) )
		NopCmd
		AssumeExpCmd LNot(Eq(0xa9059cbb tacSighash!!7:17 ) )
		NopCmd
		AssumeExpCmd LNot(Eq(0xb2bdfa7b tacSighash!!7:17 ) )
		NopCmd
		AssumeExpCmd LNot(Eq(0xd0e30db0 tacSighash!!7:17 ) )
		NopCmd
		AssumeExpCmd Eq(0xdd62ed3e tacSighash!!7:17 )
		AssumeCmd:42 true
		AssignExpCmd:43 R70:32 Sub(tacCalldatasize!!51:28 0x4 )
		NopCmd
		AssumeExpCmd LNot(Slt(R70:32 0x40 ) )
		NopCmd
		AssumeExpCmd Le(R55 0xffffffffffffffffffffffffffffffffffffffff )
		NopCmd
		AssumeExpCmd Le(R58 0xffffffffffffffffffffffffffffffffffffffff )
		AnnotationCmd:41 JSON{"key":{"name":"internal.func.start","type":"analysis.ip.InternalFuncStartAnnotation","erasureStrategy":"CallTrace"},"value":{"id":2,"startPc":4858,"args":[{"s":{"namePrefix":"R55","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1012}]},"offset":1,"sort":"SCALAR"},{"s":{"namePrefix":"R58","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1012}]},"offset":2,"sort":"SCALAR"}],"methodSignature":{"#class":"spec.cvlast.QualifiedMethodSignature.QualifiedMethodSig","qualifiedMethodName":{"#class":"spec.cvlast.QualifiedFunction","host":{"name":"ERC20"},"methodId":"allowance"},"params":[{"#class":"spec.cvlast.VMParam.Named","name":"owner","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$address"}},{"#class":"spec.cvlast.VMParam.Named","name":"spender","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$address"}}],"res":[{"#class":"spec.cvlast.VMParam.Unnamed","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256}}]},"stackOffsetToArgPos":{"1":0,"2":1},"callSiteSrc":{"source":0,"begin":5647,"len":535,"jumpType":"ENTER","address":"ce4604a0000000000000000000000003","sourceContext":{"indexToFilepath":{"0":"contracts/ERC20.sol","1":"contracts/IERC20.sol","2":"contracts/IERC20Metadata.sol"},"sourceDir":".post_autofinders.0"}}}}
		AssignExpCmd:44 R78:34 Apply(hash_3_keccak:bif Apply(skey_basic:bif 0x40) Apply(to_skey:bif R55:35) Apply(skey_basic:bif 0x1))
		AssignExpCmd:45 R82:34 Apply(hash_3_keccak:bif Apply(skey_basic:bif 0x40) Apply(to_skey:bif R58:35) R78:37)
		AssignExpCmd:46 R83:34 Select(CANON28!!2:4 R82:47 )
		AnnotationCmd:41 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet","value":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R83","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1019}]},"displayPath":{"#class":"analysis.storage.DisplayPath.MapAccess","key":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R58","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1017}]},"keyTyp":{"#class":"tac.TACStorageType.IntegralType","typeLabel":"address","numBytes":"14","descriptor":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$address"},"lowerBound":null,"upperBound":null},"base":{"#class":"analysis.storage.DisplayPath.MapAccess","key":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R55","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1017}]},"keyTyp":{"#class":"tac.TACStorageType.IntegralType","typeLabel":"address","numBytes":"14","descriptor":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$address"},"lowerBound":null,"upperBound":null},"base":{"#class":"analysis.storage.DisplayPath.Root","name":"_allowances"}}},"storageType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256},"contractInstance":"ce4604a0000000000000000000000003","linkableStorageReadId":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet.None"}}}
		AnnotationCmd:41 JSON{"key":{"name":"internal.func.end","type":"analysis.ip.InternalFuncExitAnnotation","erasureStrategy":"Canonical"},"value":{"id":2,"rets":[{"s":{"namePrefix":"R83","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1023}]},"offset":0}],"functionLayout":{"0":{"#class":"analysis.ip.InternalFuncValueLocation.Scalar"}}}}
		AnnotationCmd:41 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.EVMFunctionReturnWrite","returnbufOffset":"0","returnValueSym":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R83","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1023}]},"callIndex":3}}
		AnnotationCmd:41 JSON{"key":{"name":"tac.return.path","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		LabelCmd:41 "End procedure ERC20-allowance(address,address)"
		AssignExpCmd:41 CANON99:48 R83:34
		AnnotationCmd:41 JSON{"key":{"name":"call.trace.pop","type":"analysis.icfg.Inliner$CallStack$PopRecord","erasureStrategy":"Canonical"},"value":"rO0ABXNyAClhbmFseXNpcy5pY2ZnLklubGluZXIkQ2FsbFN0YWNrJFBvcFJlY29yZPAPfwSLdCWJAgABSQAIY2FsbGVlSWR4cAAAAAM="}
	}
	Block 1_0_0_0_0_0 Succ [0_0_0_2_0_0] {
		AssumeNotCmd:25 false
		AssumeNotCmd:25 false
		AnnotationCmd JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageGlobalChangeSnippet.StorageTakeSnapshot","lhs":{"namePrefix":"lastStorage","tag":{"#class":"tac.Tag.BlockchainState"},"callIndex":0,"meta":[{"key":{"name":"cvl.local","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true},{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"lastStorage"},{"key":{"name":"cvl.type","type":"spec.cvlast.CVLType$PureCVLType","erasureStrategy":"CallTrace"},"value":{"#class":"spec.cvlast.CVLType.PureCVLType.VMInternal.BlockchainState"}},{"key":{"name":"cvl","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true},{"key":{"name":"cvl.display","type":"java.lang.String","erasureStrategy":"CallTrace"},"value":"lastStorage"}]}}}
		AnnotationCmd:25 JSON{"key":{"name":"cvl.label.end","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
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
		AnnotationCmd:49 JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Cmd","cmd":{"cmd_type":"spec.cvlast.CVLCmd.Simple.Apply","cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/spec/ERC20.spec","start":{"line":99,"character":4},"end":{"line":99,"character":15}},"exp":{"#class":"spec.cvlast.CVLExp.ApplyExp.ContractFunction.Symbolic","methodIdWithCallContext":{"#class":"spec.cvlast.ParametricMethod","methodId":"f","host":{"name":"ERC20"}},"args":[{"#class":"spec.cvlast.CVLExp.VariableExp","id":"e","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":6}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"env","fields":[{"fieldName":"msg","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"msg","fields":[{"fieldName":"sender","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"value","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}}]}},{"fieldName":"tx","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"tx","fields":[{"fieldName":"origin","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}}]}},{"fieldName":"block","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"block","fields":[{"fieldName":"coinbase","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"difficulty","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"gaslimit","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"number","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"timestamp","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}}]}}]},"cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/spec/ERC20.spec","start":{"line":99,"character":4},"end":{"line":99,"character":15}}},"twoStateIndex":"NEITHER"},{"#class":"spec.cvlast.CVLExp.VariableExp","id":"args","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":6}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.VMInternal.RawArgs"},"cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/spec/ERC20.spec","start":{"line":99,"character":4},"end":{"line":99,"character":15}}},"twoStateIndex":"NEITHER"}],"noRevert":true,"storage":{"#class":"spec.cvlast.CVLExp.VariableExp","id":"lastStorage","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":6}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.VMInternal.BlockchainState"},"cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/spec/ERC20.spec","start":{"line":99,"character":4},"end":{"line":99,"character":15}}},"twoStateIndex":"NEITHER"},"tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":6}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Void"},"cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/spec/ERC20.spec","start":{"line":99,"character":4},"end":{"line":99,"character":5}}}},"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":6}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}}}}}
		NopCmd
		NopCmd
		NopCmd
		NopCmd
		NopCmd
		NopCmd
		AssignExpCmd R99:50 CANON50:14
		AnnotationCmd:49 JSON{"key":{"name":"call.trace.push","type":"analysis.icfg.Inliner$CallStack$PushRecord","erasureStrategy":"Canonical"},"value":"rO0ABXNyACphbmFseXNpcy5pY2ZnLklubGluZXIkQ2FsbFN0YWNrJFB1c2hSZWNvcmSX8+DCTLCH+AIAA0kACGNhbGxlZUlkTAAGY2FsbGVldAATTHZjL2RhdGEvTWV0aG9kUmVmO0wAB3N1bW1hcnl0ABVMdmMvZGF0YS9DYWxsU3VtbWFyeTt4cAAAAAJzcgARdmMuZGF0YS5NZXRob2RSZWbJlJTzzU9pGAIAA0wABGF0dHJ0ABdMc2NlbmUvTWV0aG9kQXR0cmlidXRlO0wACmNvbnRyYWN0SWR0ABZMamF2YS9tYXRoL0JpZ0ludGVnZXI7TAAHc2lnSGFzaHQAEExldm0vU2lnaGFzaEludDt4cHNyABxzY2VuZS5NZXRob2RBdHRyaWJ1dGUkQ29tbW9uNHjdebdr9XMCAAB4cgAVc2NlbmUuTWV0aG9kQXR0cmlidXRlcYg2pYWutuUCAAB4cHNyABRqYXZhLm1hdGguQmlnSW50ZWdlcoz8nx+pO/sdAwAGSQAIYml0Q291bnRJAAliaXRMZW5ndGhJABNmaXJzdE5vbnplcm9CeXRlTnVtSQAMbG93ZXN0U2V0Qml0SQAGc2lnbnVtWwAJbWFnbml0dWRldAACW0J4cgAQamF2YS5sYW5nLk51bWJlcoaslR0LlOCLAgAAeHD///////////////7////+AAAAAXVyAAJbQqzzF/gGCFTgAgAAeHAAAAAQzkYEoAAAAAAAAAAAAAAAA3hzcgAOZXZtLlNpZ2hhc2hJbnRUdcqNMXEgeAIAAUwAAW5xAH4ABnhwc3EAfgAM///////////////+/////gAAAAF1cQB+ABAAAAAEcKCCMXhw"}
		NopCmd
		AssumeExpCmd Ge(R99:51 0x24 )
		NopCmd
		AssumeExpCmd Ge(0x7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff R99:51 )
		AssignExpCmd R103:24 Select(CANON48:13 0x4 )
		AssignExpCmd tacCalldatabufCANON0@2:52 R103:24
		AssignExpCmd:49 B105 LAnd(Ge(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff CANON34:5 ) Le(0x0 CANON34:5 ) )
		AssertCmd:49 B105 "sanity bounds check on cvl to vm encoding of tacTmp!1519:int failed"
		AssignExpCmd:49 R106:24 Apply(safe_math_narrow:bif CANON34:5)
		NopCmd
		AssumeExpCmd LAnd(Le(R106:53 0xffffffffffffffffffffffffffffffffffffffff ) Ge(R106:53 0x0 ) )
		AssignExpCmd:49 B110 LAnd(Ge(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff CANON35:6 ) Le(0x0 CANON35:6 ) )
		AssertCmd:49 B110 "sanity bounds check on cvl to vm encoding of tacTmp!1522:int failed"
		AssignExpCmd:49 R111:24 Apply(safe_math_narrow:bif CANON35:6)
		NopCmd
		AssumeExpCmd LAnd(Le(R111:54 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff ) Ge(R111:54 0x0 ) )
		AssignExpCmd:49 B116 LAnd(Ge(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff CANON36:7 ) Le(0x0 CANON36:7 ) )
		AssertCmd:49 B116 "sanity bounds check on cvl to vm encoding of tacTmp!1526:int failed"
		AssignExpCmd:49 R117:24 Apply(safe_math_narrow:bif CANON36:7)
		NopCmd
		AssumeExpCmd LAnd(Le(R117:55 0xffffffffffffffffffffffffffffffffffffffff ) Ge(R117:55 0x0 ) )
		AssignExpCmd:49 B121 LAnd(Ge(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff CANON40:11 ) Le(0x0 CANON40:11 ) )
		AssertCmd:49 B121 "sanity bounds check on cvl to vm encoding of tacTmp!1529:int failed"
		AssignExpCmd:49 R122:24 Apply(safe_math_narrow:bif CANON40:11)
		NopCmd
		AssumeExpCmd LAnd(Le(R122:56 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff ) Ge(R122:56 0x0 ) )
		AssignExpCmd:49 B126 LAnd(Ge(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff CANON41:12 ) Le(0x0 CANON41:12 ) )
		AssertCmd:49 B126 "sanity bounds check on cvl to vm encoding of tacTmp!1532:int failed"
		AssignExpCmd:49 R127:24 Apply(safe_math_narrow:bif CANON41:12)
		NopCmd
		AssumeExpCmd LAnd(Le(R127:57 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff ) Ge(R127:57 0x0 ) )
		AssignExpCmd:49 B131 LAnd(Ge(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff CANON35:6 ) Le(0x0 CANON35:6 ) )
		AssertCmd:49 B131 "sanity bounds check on cvl to vm encoding of tacTmp!1535:int failed"
		AssignExpCmd:49 R132:24 Apply(safe_math_narrow:bif CANON35:6)
		AssignExpCmd:49 B134 LAnd(Ge(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff CANON34:5 ) Le(0x0 CANON34:5 ) )
		AssertCmd:49 B134 "sanity bounds check on cvl to vm encoding of tacTmp!1538:int failed"
		AssignExpCmd:49 R135:24 Apply(safe_math_narrow:bif CANON34:5)
		AssignExpCmd:49 R138:24 Select(tacBalance!!1:1 Apply(to_skey:bif R135:24) )
		AssignExpCmd:58 I139:24 IntSub(R138:24 R132:24 )
		AssignExpCmd:58 tacBalance!!140:1 Store(tacBalance!!1:1 Apply(to_skey:bif R135:24) I139:24 )
		AssignExpCmd:49 R141:24 Select(tacBalance!!140:1 Apply(to_skey:bif R4:16) )
		AssignExpCmd:58 R142:24 Add(R141:24 R132:24)
		NopCmd
		AssumeExpCmd Apply(add_noofl:bif R141:24 R132:24)
		AnnotationCmd:49 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.BalanceSnippet","srcAccountInfo":{"old":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R138","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}]},"new":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"I139","tag":{"#class":"tac.Tag.Int"},"callIndex":0,"meta":[{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}]},"addr":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R135","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}]}},"trgAccountInfo":{"old":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R141","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}]},"new":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R142","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}]},"addr":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R4","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"tacContractAt"},{"key":{"name":"tac.contract.sym.addr.name","type":"java.lang.String","erasureStrategy":"Erased"},"value":"ERC20"},{"key":{"name":"tac.contract.sym.addr","type":"java.math.BigInteger","erasureStrategy":"Erased"},"value":"ce4604a0000000000000000000000003"}]}},"transferredAmount":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R132","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}]}}}
		JumpCmd 0_0_0_2_0_0
	}
	Block 3_0_0_0_0_0 Succ [] {
		AssumeNotCmd:41 false
		AssumeNotCmd:41 false
		AnnotationCmd JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageGlobalChangeSnippet.StorageTakeSnapshot","lhs":{"namePrefix":"lastStorage","tag":{"#class":"tac.Tag.BlockchainState"},"callIndex":0,"meta":[{"key":{"name":"cvl.local","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true},{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"lastStorage"},{"key":{"name":"cvl.type","type":"spec.cvlast.CVLType$PureCVLType","erasureStrategy":"CallTrace"},"value":{"#class":"spec.cvlast.CVLType.PureCVLType.VMInternal.BlockchainState"}},{"key":{"name":"cvl","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true},{"key":{"name":"cvl.display","type":"java.lang.String","erasureStrategy":"CallTrace"},"value":"lastStorage"}]}}}
		AnnotationCmd:41 JSON{"key":{"name":"cvl.label.end","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		AnnotationCmd:59 JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Cmd","cmd":{"cmd_type":"spec.cvlast.CVLCmd.Simple.Assert","cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/spec/ERC20.spec","start":{"line":103,"character":4},"end":{"line":104,"character":58}},"exp":{"#class":"spec.cvlast.CVLExp.BinaryExp.ImpliesExp","l":{"#class":"spec.cvlast.CVLExp.RelopExp.ArithRelopExp.GtExp","l":{"#class":"spec.cvlast.CVLExp.VariableExp","id":"allowance_after","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":6}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Mathint"},"cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/spec/ERC20.spec","start":{"line":103,"character":4},"end":{"line":104,"character":58}}},"twoStateIndex":"NEITHER"},"r":{"#class":"spec.cvlast.CVLExp.VariableExp","id":"allowance_before","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":6}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Mathint"},"cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/spec/ERC20.spec","start":{"line":103,"character":4},"end":{"line":104,"character":58}}},"twoStateIndex":"NEITHER"},"tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":6}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"},"cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/spec/ERC20.spec","start":{"line":103,"character":11},"end":{"line":103,"character":45}}}},"r":{"#class":"spec.cvlast.CVLExp.RelopExp.EqExp","l":{"#class":"spec.cvlast.CVLExp.FieldSelectExp","structExp":{"#class":"spec.cvlast.CVLExp.FieldSelectExp","structExp":{"#class":"spec.cvlast.CVLExp.VariableExp","id":"e","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":6}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"env","fields":[{"fieldName":"msg","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"msg","fields":[{"fieldName":"sender","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"value","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}}]}},{"fieldName":"tx","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"tx","fields":[{"fieldName":"origin","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}}]}},{"fieldName":"block","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"block","fields":[{"fieldName":"coinbase","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"difficulty","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"gaslimit","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"number","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"timestamp","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}}]}}]},"cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/spec/ERC20.spec","start":{"line":103,"character":4},"end":{"line":104,"character":58}}},"twoStateIndex":"NEITHER"},"fieldName":"msg","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":6}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"msg","fields":[{"fieldName":"sender","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"value","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}}]},"cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/spec/ERC20.spec","start":{"line":103,"character":49},"end":{"line":103,"character":50}}}},"fieldName":"sender","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":6}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"},"cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/spec/ERC20.spec","start":{"line":103,"character":49},"end":{"line":103,"character":50}}}},"r":{"#class":"spec.cvlast.CVLExp.VariableExp","id":"holder","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":6}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"},"cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/spec/ERC20.spec","start":{"line":103,"character":4},"end":{"line":104,"character":58}}},"twoStateIndex":"NEITHER"},"tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":6}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"},"cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/spec/ERC20.spec","start":{"line":103,"character":49},"end":{"line":103,"character":71}}}},"tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":6}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"},"cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/spec/ERC20.spec","start":{"line":103,"character":11},"end":{"line":103,"character":71}}}},"description":"\"approve must only change the sender's allowance\"","scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":6}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}}}}}
		AssignExpCmd:60 I144 CANON99:48
		AssignExpCmd:61 I145 CANON33:40
		AssignExpCmd:62 B146 Gt(I144 I145 )
		NopCmd
		AssignExpCmd:63 I148 CANON12:2
		AssignExpCmd:64 CANON105!!149:65 Eq(CANON34:5 I148 )
		AssignExpCmd:66 CANON107!!150:65 LOr(LNot(B146 ) CANON105!!149:65 )
		AssertCmd:67 CANON107!!150:65 "\"approve must only change the sender's allowance\""
		AnnotationCmd:59 JSON{"key":{"name":"cvl.label.end","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		AnnotationCmd:68 JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Cmd","cmd":{"cmd_type":"spec.cvlast.CVLCmd.Simple.Assert","cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/spec/ERC20.spec","start":{"line":106,"character":4},"end":{"line":108,"character":69}},"exp":{"#class":"spec.cvlast.CVLExp.BinaryExp.ImpliesExp","l":{"#class":"spec.cvlast.CVLExp.RelopExp.ArithRelopExp.GtExp","l":{"#class":"spec.cvlast.CVLExp.VariableExp","id":"allowance_after","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":6}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Mathint"},"cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/spec/ERC20.spec","start":{"line":106,"character":4},"end":{"line":108,"character":69}}},"twoStateIndex":"NEITHER"},"r":{"#class":"spec.cvlast.CVLExp.VariableExp","id":"allowance_before","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":6}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Mathint"},"cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/spec/ERC20.spec","start":{"line":106,"character":4},"end":{"line":108,"character":69}}},"twoStateIndex":"NEITHER"},"tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":6}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"},"cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/spec/ERC20.spec","start":{"line":106,"character":11},"end":{"line":106,"character":45}}}},"r":{"#class":"spec.cvlast.CVLExp.BinaryExp.LorExp","l":{"#class":"spec.cvlast.CVLExp.RelopExp.EqExp","l":{"#class":"spec.cvlast.CVLExp.FieldSelectExp","structExp":{"#class":"spec.cvlast.CVLExp.VariableExp","id":"f","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":6}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"method","fields":[{"fieldName":"selector","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":32}},{"fieldName":"isPure","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}},{"fieldName":"isView","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}},{"fieldName":"isPayable","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}},{"fieldName":"numberOfArguments","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"isFallback","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}}]},"cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/spec/ERC20.spec","start":{"line":106,"character":4},"end":{"line":108,"character":69}}},"twoStateIndex":"NEITHER"},"fieldName":"selector","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":6}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":32},"cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/spec/ERC20.spec","start":{"line":107,"character":9},"end":{"line":107,"character":10}}}},"r":{"#class":"spec.cvlast.CVLExp.FieldSelectExp","structExp":{"#class":"spec.cvlast.CVLExp.Constant.SignatureLiteralExp","function":{"#class":"spec.cvlast.QualifiedMethodSignature.QualifiedMethodSig","qualifiedMethodName":{"#class":"spec.cvlast.QualifiedFunction","host":{"name":"ERC20"},"methodId":"approve"},"params":[{"#class":"spec.cvlast.VMParam.Unnamed","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$address"}},{"#class":"spec.cvlast.VMParam.Unnamed","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256}}],"res":[]},"tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":6}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"method","fields":[{"fieldName":"selector","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":32}},{"fieldName":"isPure","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}},{"fieldName":"isView","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}},{"fieldName":"isPayable","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}},{"fieldName":"numberOfArguments","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"isFallback","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}}]},"cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/spec/ERC20.spec","start":{"line":107,"character":27},"end":{"line":107,"character":48}},"annotation":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.CVLExp$Constant$StructLit","fieldNameToEntry":{"selector":{"#class":"spec.cvlast.CVLExp.Constant.NumberLit","n":"95ea7b3","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":6}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":32},"cvlRange":{"#class":"spec.cvlast.CVLRange.Empty"}}},"isPure":{"#class":"spec.cvlast.CVLExp.Constant.BoolLit","b":"0","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":6}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"},"cvlRange":{"#class":"spec.cvlast.CVLRange.Empty"}}},"isView":{"#class":"spec.cvlast.CVLExp.Constant.BoolLit","b":"0","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":6}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"},"cvlRange":{"#class":"spec.cvlast.CVLRange.Empty"}}},"isPayable":{"#class":"spec.cvlast.CVLExp.Constant.BoolLit","b":"0","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":6}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"},"cvlRange":{"#class":"spec.cvlast.CVLRange.Empty"}}},"isFallback":{"#class":"spec.cvlast.CVLExp.Constant.BoolLit","b":"0","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":6}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"},"cvlRange":{"#class":"spec.cvlast.CVLRange.Empty"}}},"numberOfArguments":{"#class":"spec.cvlast.CVLExp.Constant.NumberLit","n":"2","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":6}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256},"cvlRange":{"#class":"spec.cvlast.CVLRange.Empty"}}}},"tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":6}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"method","fields":[{"fieldName":"selector","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":32}},{"fieldName":"isPure","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}},{"fieldName":"isView","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}},{"fieldName":"isPayable","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}},{"fieldName":"numberOfArguments","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"isFallback","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}}]},"cvlRange":{"#class":"spec.cvlast.CVLRange.Empty"}}}}},"fieldName":"selector","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":6}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":32},"cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/spec/ERC20.spec","start":{"line":107,"character":27},"end":{"line":107,"character":48}}}},"tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":6}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"},"cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/spec/ERC20.spec","start":{"line":107,"character":9},"end":{"line":107,"character":57}}}},"r":{"#class":"spec.cvlast.CVLExp.RelopExp.EqExp","l":{"#class":"spec.cvlast.CVLExp.FieldSelectExp","structExp":{"#class":"spec.cvlast.CVLExp.VariableExp","id":"f","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":6}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"method","fields":[{"fieldName":"selector","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":32}},{"fieldName":"isPure","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}},{"fieldName":"isView","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}},{"fieldName":"isPayable","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}},{"fieldName":"numberOfArguments","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"isFallback","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}}]},"cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/spec/ERC20.spec","start":{"line":106,"character":4},"end":{"line":108,"character":69}}},"twoStateIndex":"NEITHER"},"fieldName":"selector","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":6}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":32},"cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/spec/ERC20.spec","start":{"line":107,"character":61},"end":{"line":107,"character":62}}}},"r":{"#class":"spec.cvlast.CVLExp.FieldSelectExp","structExp":{"#class":"spec.cvlast.CVLExp.Constant.SignatureLiteralExp","function":{"#class":"spec.cvlast.QualifiedMethodSignature.QualifiedMethodSig","qualifiedMethodName":{"#class":"spec.cvlast.QualifiedFunction","host":{"name":"ERC20"},"methodId":"increaseAllowance"},"params":[{"#class":"spec.cvlast.VMParam.Unnamed","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$address"}},{"#class":"spec.cvlast.VMParam.Unnamed","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256}}],"res":[]},"tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":6}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"method","fields":[{"fieldName":"selector","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":32}},{"fieldName":"isPure","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}},{"fieldName":"isView","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}},{"fieldName":"isPayable","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}},{"fieldName":"numberOfArguments","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"isFallback","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}}]},"cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/spec/ERC20.spec","start":{"line":107,"character":79},"end":{"line":107,"character":110}},"annotation":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.CVLExp$Constant$StructLit","fieldNameToEntry":{"selector":{"#class":"spec.cvlast.CVLExp.Constant.NumberLit","n":"39509351","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":6}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":32},"cvlRange":{"#class":"spec.cvlast.CVLRange.Empty"}}},"isPure":{"#class":"spec.cvlast.CVLExp.Constant.BoolLit","b":"0","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":6}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"},"cvlRange":{"#class":"spec.cvlast.CVLRange.Empty"}}},"isView":{"#class":"spec.cvlast.CVLExp.Constant.BoolLit","b":"0","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":6}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"},"cvlRange":{"#class":"spec.cvlast.CVLRange.Empty"}}},"isPayable":{"#class":"spec.cvlast.CVLExp.Constant.BoolLit","b":"0","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":6}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"},"cvlRange":{"#class":"spec.cvlast.CVLRange.Empty"}}},"isFallback":{"#class":"spec.cvlast.CVLExp.Constant.BoolLit","b":"0","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":6}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"},"cvlRange":{"#class":"spec.cvlast.CVLRange.Empty"}}},"numberOfArguments":{"#class":"spec.cvlast.CVLExp.Constant.NumberLit","n":"2","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":6}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256},"cvlRange":{"#class":"spec.cvlast.CVLRange.Empty"}}}},"tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":6}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"method","fields":[{"fieldName":"selector","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":32}},{"fieldName":"isPure","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}},{"fieldName":"isView","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}},{"fieldName":"isPayable","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}},{"fieldName":"numberOfArguments","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"isFallback","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}}]},"cvlRange":{"#class":"spec.cvlast.CVLRange.Empty"}}}}},"fieldName":"selector","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":6}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":32},"cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/spec/ERC20.spec","start":{"line":107,"character":79},"end":{"line":107,"character":110}}}},"tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":6}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"},"cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/spec/ERC20.spec","start":{"line":107,"character":61},"end":{"line":107,"character":119}}}},"tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":6}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"},"cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/spec/ERC20.spec","start":{"line":107,"character":9},"end":{"line":107,"character":119}}}},"tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":6}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"},"cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/spec/ERC20.spec","start":{"line":106,"character":11},"end":{"line":107,"character":120}}}},"description":"\"only approve and increaseAllowance can increase allowances\"","scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":6}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}}}}}
		AssignExpCmd:69 I151 CANON99:48
		AssignExpCmd:70 I152 CANON33:40
		AssignExpCmd:71 B153 Gt(I151 I152 )
		AssignExpCmd:72 CANON111:65 false
		AssignExpCmd:73 CANON112:65 false
		AssignExpCmd:74 CANON113:65 false
		AssignExpCmd:75 CANON114!!154:65 LOr(LNot(B153 ) false )
		AssertCmd:76 CANON114!!154:65 "\"only approve and increaseAllowance can increase allowances\""
		AnnotationCmd:68 JSON{"key":{"name":"cvl.label.end","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
	}
	Block 0_0_0_2_0_0 Succ [2_0_0_0_0_0] {
		LabelCmd "Start procedure ERC20-balanceOf(address)"
		AnnotationCmd JSON{"key":{"name":"fps.free-pointer-is-scalarized","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true}
		AssignExpCmd R155:24 Select(tacExtcodesize!!0:0 Apply(to_skey:bif R4:29) )
		NopCmd
		AssumeExpCmd Gt(R155:24 0x0 )
		AnnotationCmd JSON{"key":{"name":"internal.func.finder.info","type":"analysis.ip.InternalFunctionFinderReport","erasureStrategy":"Erased"},"value":"rO0ABXNyAChhbmFseXNpcy5pcC5JbnRlcm5hbEZ1bmN0aW9uRmluZGVyUmVwb3J0ian+bYn1VdACAAFMABN1bnJlc29sdmVkRnVuY3Rpb25zdAAPTGphdmEvdXRpbC9TZXQ7eHBzcgAhZGF0YXN0cnVjdHVyZXMuTGlua2VkQXJyYXlIYXNoU2V0AAAAAAAAAAEDAAJGAApsb2FkRmFjdG9yTAAJaGFzaFRhYmxldAAuTGRhdGFzdHJ1Y3R1cmVzL2FycmF5aGFzaHRhYmxlL0FycmF5SGFzaFRhYmxlO3hwdwgAAAAAQAAAAHg="}
		AnnotationCmd JSON{"key":{"name":"fps.free-pointer-is-scalarized","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true}
		NopCmd
		AssumeExpCmd LNot(Lt(R99:51 0x4 ) )
		NopCmd
		AssumeExpCmd LNot(Gt(0x70a08231 tacSighash!!6:17 ) )
		NopCmd
		AssumeExpCmd Gt(0xa9059cbb tacSighash!!6:17 )
		NopCmd
		AssumeExpCmd Eq(0x70a08231 tacSighash!!6:17 )
		NopCmd
		AssumeExpCmd Eq(R111:54 0x0 )
		AssignExpCmd:77 R162:78 Sub(CANON50:14 0x4 )
		NopCmd
		AssumeExpCmd LNot(Slt(R162:78 0x20 ) )
		AssignExpCmd:79 R164:80 tacCalldatabufCANON0@2:81
		NopCmd
		AssumeExpCmd Le(tacCalldatabufCANON0@2:81 0xffffffffffffffffffffffffffffffffffffffff )
		AnnotationCmd JSON{"key":{"name":"internal.func.start","type":"analysis.ip.InternalFuncStartAnnotation","erasureStrategy":"CallTrace"},"value":{"id":1,"startPc":3130,"args":[{"s":{"namePrefix":"R164","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1013}]},"offset":1,"sort":"SCALAR"}],"methodSignature":{"#class":"spec.cvlast.QualifiedMethodSignature.QualifiedMethodSig","qualifiedMethodName":{"#class":"spec.cvlast.QualifiedFunction","host":{"name":"ERC20"},"methodId":"balanceOf"},"params":[{"#class":"spec.cvlast.VMParam.Named","name":"account","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$address"}}],"res":[{"#class":"spec.cvlast.VMParam.Unnamed","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256}}]},"stackOffsetToArgPos":{"1":0},"callSiteSrc":{"source":0,"begin":4328,"len":511,"jumpType":"ENTER","address":"ce4604a0000000000000000000000003","sourceContext":{"indexToFilepath":{"0":"contracts/ERC20.sol","1":"contracts/IERC20.sol","2":"contracts/IERC20Metadata.sol"},"sourceDir":".post_autofinders.0"}}}}
		AssignExpCmd R166:82 tacCalldatabufCANON0@2:81
		NopCmd
		AssignExpCmd:83 R168:84 Apply(hash_3_keccak:bif Apply(skey_basic:bif 0x40) Apply(to_skey:bif tacCalldatabufCANON0@2:81) Apply(skey_basic:bif 0x0))
		AssignExpCmd:85 R169:84 Select(CANON83!!3:15 R168:86 )
		AnnotationCmd JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet","value":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R169","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1020}]},"displayPath":{"#class":"analysis.storage.DisplayPath.MapAccess","key":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R166","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1018}]},"keyTyp":{"#class":"tac.TACStorageType.IntegralType","typeLabel":"address","numBytes":"14","descriptor":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$address"},"lowerBound":null,"upperBound":null},"base":{"#class":"analysis.storage.DisplayPath.Root","name":"_balances"}},"storageType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256},"contractInstance":"ce4604a0000000000000000000000003","linkableStorageReadId":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet.None"}}}
		AnnotationCmd JSON{"key":{"name":"internal.func.end","type":"analysis.ip.InternalFuncExitAnnotation","erasureStrategy":"Canonical"},"value":{"id":1,"rets":[{"s":{"namePrefix":"R169","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1023}]},"offset":0}],"functionLayout":{"0":{"#class":"analysis.ip.InternalFuncValueLocation.Scalar"}}}}
		AnnotationCmd JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.EVMFunctionReturnWrite","returnbufOffset":"0","returnValueSym":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R169","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1023}]},"callIndex":2}}
		AnnotationCmd JSON{"key":{"name":"tac.return.path","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		LabelCmd "End procedure ERC20-balanceOf(address)"
		JumpCmd 2_0_0_0_0_0
	}
	Block 2_0_0_0_0_0 Succ [0_0_0_3_0_0] {
		AnnotationCmd:49 JSON{"key":{"name":"call.trace.pop","type":"analysis.icfg.Inliner$CallStack$PopRecord","erasureStrategy":"Canonical"},"value":"rO0ABXNyAClhbmFseXNpcy5pY2ZnLklubGluZXIkQ2FsbFN0YWNrJFBvcFJlY29yZPAPfwSLdCWJAgABSQAIY2FsbGVlSWR4cAAAAAI="}
		AssumeNotCmd:49 false
		AssumeNotCmd:49 false
		AnnotationCmd JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageGlobalChangeSnippet.StorageTakeSnapshot","lhs":{"namePrefix":"lastStorage","tag":{"#class":"tac.Tag.BlockchainState"},"callIndex":0,"meta":[{"key":{"name":"cvl.local","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true},{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"lastStorage"},{"key":{"name":"cvl.type","type":"spec.cvlast.CVLType$PureCVLType","erasureStrategy":"CallTrace"},"value":{"#class":"spec.cvlast.CVLType.PureCVLType.VMInternal.BlockchainState"}},{"key":{"name":"cvl","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true},{"key":{"name":"cvl.display","type":"java.lang.String","erasureStrategy":"CallTrace"},"value":"lastStorage"}]}}}
		AnnotationCmd:49 JSON{"key":{"name":"cvl.label.end","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		AnnotationCmd:41 JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Cmd","cmd":{"cmd_type":"spec.cvlast.CVLCmd.Simple.Definition","cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/spec/ERC20.spec","start":{"line":101,"character":4},"end":{"line":101,"character":57}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Mathint"},"idL":[{"#class":"spec.cvlast.CVLLhs.Id","cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/spec/ERC20.spec","start":{"line":101,"character":4},"end":{"line":101,"character":27}},"id":"allowance_after","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":6}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Mathint"},"cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/spec/ERC20.spec","start":{"line":101,"character":4},"end":{"line":101,"character":57}}}}],"exp":{"#class":"spec.cvlast.CVLExp.ApplyExp.ContractFunction.Concrete","methodIdWithCallContext":{"#class":"spec.cvlast.ConcreteMethod","signature":{"#class":"spec.cvlast.ExternalQualifiedMethodSignature.ExternalQualifiedMethodSig","wrapped":{"#class":"spec.cvlast.QualifiedMethodSignature.QualifiedMethodSig","qualifiedMethodName":{"#class":"spec.cvlast.QualifiedFunction","host":{"name":"ERC20"},"methodId":"allowance"},"params":[{"#class":"spec.cvlast.VMParam.Named","name":"owner","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$address"}},{"#class":"spec.cvlast.VMParam.Named","name":"spender","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$address"}}],"res":[{"#class":"spec.cvlast.VMParam.Unnamed","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256}}]},"sighashInt":{"n":"dd62ed3e"}}},"args":[{"#class":"spec.cvlast.CVLExp.VariableExp","id":"holder","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":6}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"},"cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/spec/ERC20.spec","start":{"line":101,"character":4},"end":{"line":101,"character":57}}},"twoStateIndex":"NEITHER"},{"#class":"spec.cvlast.CVLExp.VariableExp","id":"spender","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":6}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"},"cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/spec/ERC20.spec","start":{"line":101,"character":4},"end":{"line":101,"character":57}}},"twoStateIndex":"NEITHER"}],"noRevert":true,"storage":{"#class":"spec.cvlast.CVLExp.VariableExp","id":"lastStorage","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":6}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.VMInternal.BlockchainState"},"cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/spec/ERC20.spec","start":{"line":101,"character":4},"end":{"line":101,"character":57}}},"twoStateIndex":"NEITHER"},"isWhole":false,"tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":6}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.VM","descriptor":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256},"context":{"#class":"spec.cvlast.typedescriptors.FromVMContext.ReturnValue"}},"cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/spec/ERC20.spec","start":{"line":101,"character":30},"end":{"line":101,"character":39}},"annotation":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.CallResolution$DirectPassing","target":{"methodSignature":{"#class":"spec.cvlast.ExternalQualifiedMethodSignature.ExternalQualifiedMethodSig","wrapped":{"#class":"spec.cvlast.QualifiedMethodSignature.QualifiedMethodSig","qualifiedMethodName":{"#class":"spec.cvlast.QualifiedFunction","host":{"name":"ERC20"},"methodId":"allowance"},"params":[{"#class":"spec.cvlast.VMParam.Named","name":"owner","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$address"}},{"#class":"spec.cvlast.VMParam.Named","name":"spender","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$address"}}],"res":[{"#class":"spec.cvlast.VMParam.Unnamed","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256}}]},"sighashInt":{"n":"dd62ed3e"}},"definitelyNonPayable":true,"annotation":{"visibility":"EXTERNAL","envFree":true,"library":false},"stateMutability":"view","tag":{"#class":"spec.cvlast.CVLImportedFunctionTag.WithMethodInfo","evmMethodInfo":{"sigHash":"dd62ed3e","name":"allowance","argTypes":[{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.address"},{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.address"}],"resultTypes":[{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256}],"stateMutability":"view","envfreeInfo":{"#class":"bridge.EnvfreeInfo.Unknown"},"isConstant":false,"paramNames":["owner","spender"],"isLibrary":false}}},"hasEnv":false}}},"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":6}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}}}}}
		AssignExpCmd:87 I171 CANON12:2
		AssignExpCmd:88 I172 CANON13:3
	}
}
Axioms {
		CANON115
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
      "value": "args"
    }
  ],
  "14": [
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
  "15": [
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
  "16": [
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
  "17": [
    {
      "key": {
        "name": "Tac.symbol.keyword",
        "type": "java.lang.String",
        "erasureStrategy": "Canonical"
      },
      "value": "tacSighash"
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
  "23": [
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
  "24": [
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
  "25": [
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
  "27": [
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
  "28": [
    {
      "key": {
        "name": "Tac.symbol.keyword",
        "type": "java.lang.String",
        "erasureStrategy": "Canonical"
      },
      "value": "tacCalldatasize"
    }
  ],
  "29": [
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
  "31": [
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
  "32": [
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
  "33": [
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
  "34": [
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
  "35": [
    {
      "key": {
        "name": "Tac.symbol.keyword",
        "type": "java.lang.String",
        "erasureStrategy": "Canonical"
      },
      "value": "tacM0x0"
    }
  ],
  "36": [
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
  "37": [
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
  "38": [
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
  "39": [
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
              "namePrefix": "R24",
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
                "namePrefix": "R21",
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
                    "namePrefix": "R21",
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
                "namePrefix": "R24",
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
  "40": [
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
    }
  ],
  "46": [
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
      "value": "rO0ABXNyADJhbmFseXNpcy5pY2ZnLkNhbGxHcmFwaEJ1aWxkZXIkQ29udHJhY3RTdG9yYWdlUmVhZLRpTKYiS4EFAgABSQACaWR4cAAAAAI="
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
              "namePrefix": "R58",
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
                "namePrefix": "R55",
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
                    "namePrefix": "R55",
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
                "namePrefix": "R58",
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
  "48": [
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
  "49": [
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
  "50": [
    {
      "key": {
        "name": "cvl.local",
        "type": "java.lang.Boolean",
        "erasureStrategy": "Canonical"
      },
      "value": false
    }
  ],
  "51": [
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
  "52": [
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
            "namePrefix": "I144",
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
            "namePrefix": "I145",
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
            "namePrefix": "CANON106",
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
            "namePrefix": "I148",
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
            "namePrefix": "B146",
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
            "namePrefix": "CANON105!!149",
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
            "namePrefix": "I151",
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
            "namePrefix": "I152",
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
            "value": "70a08231"
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
            "value": "70a08231"
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
            "namePrefix": "B153",
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
        "source": 3,
        "begin": 380,
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
      "value": 1017
    }
  ],
  "79": [
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
      "value": 1013
    }
  ],
  "81": [
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
        "name": "tac.stack.height",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 1018
    }
  ],
  "83": [
    {
      "key": {
        "name": "tac.meta",
        "type": "vc.data.TACMetaInfo",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "source": 0,
        "begin": 4814,
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
  "84": [
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
      "value": 1020
    }
  ],
  "85": [
    {
      "key": {
        "name": "tac.meta",
        "type": "vc.data.TACMetaInfo",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "source": 0,
        "begin": 4814,
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
  "86": [
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
              "namePrefix": "R166",
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
                  "value": 1018
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
                "namePrefix": "R166",
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
                    "value": 1018
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
      "value": 1020
    }
  ],
  "87": [
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
  "88": [
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
  ]
}