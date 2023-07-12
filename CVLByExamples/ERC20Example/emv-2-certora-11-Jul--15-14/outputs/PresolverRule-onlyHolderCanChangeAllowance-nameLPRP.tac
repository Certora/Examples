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
		CANON107:JSON{"name":"CANON107","paramSorts":[],"returnSort":{"#class":"tac.Tag.Int"},"attribute":"Ghost","cvlResultType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Mathint"},"cvlParamTypes":[],"declarationName":"CANON107"}
	}
	tacM0x20@1:bv256
	tacM0x20@3:bv256
	tacM0x40@2:bv256
	tacCaller@2:bv256
	tacM0x0!!43:bv256
	tacM0x0!!46:bv256
	tacM0x0!!77:bv256
	tacM0x0!!80:bv256
	tacAddress!!26:bv256
	tacAddress!!60:bv256
	tacOrigin!!116:bv256
	tacCallvalue@2:bv256
	CANON106!!152:bool
	lastReverted:bool
	lastReverted@1:bool
	lastReverted@2:bool
	lastReverted@3:bool
	tacExtcodesize!!0:wordmap
	CANON28!!3:wordmap
	tacCalldatasize@1:bv256
	tacCalldatasize@2:bv256
	tacCalldatasize@3:bv256
	tacM!!2:bytemap
	tacM0x0@1:bv256
	tacM0x0@3:bv256
	tacExtcodesize:wordmap
	CANON100:int
	CANON101:int
	CANON102:bool
	CANON103:bool
	CANON104:bool
	CANON105:bool
	CANON106:bool
	CANON107:int
	tacSighash!!5:bv256
	tacSighash!!6:bv256
	tacSighash!!7:bv256
	tacCalldatasize!!17:bv256
	tacCalldatasize!!51:bv256
	tacCalldatasize!!99:bv256
	tacBalance:wordmap
	tacTimestamp!!126:bv256
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
	R98:bv256
	B100:bool
	B101:bool
	B103:bool
	B106:bool
	B108:bool
	B111:bool
	B114:bool
	B117:bool
	B119:bool
	B122:bool
	B124:bool
	B127:bool
	B129:bool
	B132:bool
	B141:bool
	B144:bool
	B151:bool
	B154:bool
	B155:bool
	B156:bool
	B157:bool
	B158:bool
	B159:bool
	B166:bool
	B171:bool
	B172:bool
	B174:bool
	B180:bool
	B184:bool
	B188:bool
	I102:int
	I107:int
	I113:int
	I118:int
	I123:int
	I128:int
	I131:int
	I137:int
	I142:int
	I143:int
	I145:int
	I146:int
	I149:int
	I150:int
	I175:int
	I176:int
	R104:bv256
	R109:bv256
	R115:bv256
	R120:bv256
	R125:bv256
	R130:bv256
	R133:bv256
	R134:bv256
	R135:bv256
	R136:bv256
	R139:bv256
	R140:bv256
	R153:bv256
	R161:bv256
	R163:bv256
	R165:bv256
	R167:bv256
	R168:bv256
	R169:bv256
	R170:bv256
	R173:bv256
	R177:bv256
	R179:bv256
	R181:bv256
	R183:bv256
	R185:bv256
	R187:bv256
	CANON97!!147:bool
	tacM@2:bytemap
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
	tacCallvalue!!110:bv256
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
	CANON49:bool
	CANON50:bool
	CANON51:int
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
	CANON72:bv256
	CANON73:bv256
	CANON74:bv256
	CANON75:int
	CANON76:bv256
	CANON77:bv256
	CANON78:bool
	CANON79:int
	CANON80:int
	CANON81:bool
	CANON82:bool
	CANON83:bool
	CANON84:bv256
	CANON85:bool
	CANON86:bool
	CANON87:bv256
	CANON88:bool
	CANON89:bool
	CANON90:bool
	CANON91:int
	CANON92:int
	CANON93:int
	CANON94:bool
	CANON95:int
	CANON96:int
	CANON97:bool
	CANON99:bool
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
	LCANON25@2:bool
	LCANON26@2:bv256
	LCANON27@2:bool
	LCANON28@2:bv256
	LCANON29@2:bv256
	LCANON30@2:bv256
	LCANON31@2:bv256
	LCANON32@2:bv256
	LCANON33@2:bool
	LCANON34@2:bv256
	LCANON35@2:bool
	LCANON36@2:bv256
	LCANON37@2:bv256
	LCANON38@2:bv256
	LCANON39@2:bv256
	LCANON40@2:bv256
	tacM!!160:bytemap
	tacM!!162:bytemap
	tacM!!164:bytemap
	tacM!!178:bytemap
	tacM!!182:bytemap
	tacM!!186:bytemap
	tacContractAtCANON0:bv256
	tacM0x20!!47:bv256
	tacM0x20!!81:bv256
	lastHasThrown:bool
	lastHasThrown@1:bool
	lastHasThrown@2:bool
	lastHasThrown@3:bool
	tacAddress!!112:bv256
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
	tacCaller!!105:bv256
	tacBalance!!138:wordmap
	tacTimestamp@2:bv256
	CANON99!!148:bool
	tacSighash@1:bv256
	tacSighash@2:bv256
	tacSighash@3:bv256
	tacNumber!!121:bv256
}
Program {
	Block 0_0_0_0_0_0 Succ [0_0_0_1_0_0] {
		AssignHavocCmd tacExtcodesize!!0:0
		AssignHavocCmd tacBalance!!1:1
		AssignExpCmd tacM!!2:2 ByteMapDefinition(i.3758:bv256 -> 0x0 )
		AssignHavocCmd CANON12:3
		AssignHavocCmd CANON13:4
		AssignHavocCmd CANON28!!3:5
		AssignHavocCmd CANON34:6
		AssignHavocCmd CANON35:7
		AssignHavocCmd CANON36:8
		AssignHavocCmd CANON37:9
		AssignHavocCmd CANON38:10
		AssignHavocCmd CANON39:11
		AssignHavocCmd CANON40:12
		AssignHavocCmd CANON41:13
		AssignHavocCmd CANON48:14
		AssignHavocCmd R4:15
		AssignHavocCmd tacSighash!!5:16
		AssignHavocCmd tacSighash!!6:16
		AssignHavocCmd tacSighash!!7:16
		AssignExpCmd CANON0:17 0x6fdde03
		AssignExpCmd CANON1:18 false
		AssignExpCmd CANON2:19 true
		AssignExpCmd CANON3:20 false
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
		AssignExpCmd B8:23 Gt(Select(tacExtcodesize!!0:0 Apply(to_skey:bif R4:15) ) 0x0 )
		AssumeCmd B8:23
		AnnotationCmd JSON{"key":{"name":"cvl.label.end","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		AnnotationCmd JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Message","s":"assumptions about contracts' addresses"}}
		NopCmd
		AssumeExpCmd Gt(R4:15 0x0 )
		NopCmd
		AssumeExpCmd Le(R4:15 0xffffffffffffffffffffffffffffffffffffffff )
		AnnotationCmd JSON{"key":{"name":"cvl.label.end","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		AnnotationCmd JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Message","s":"assumptions about starting balances"}}
		AssignExpCmd R11:23 Select(tacBalance!!1:1 Apply(to_skey:bif R4:15) )
		NopCmd
		AssumeExpCmd Ge(R11:23 0x0 )
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
		AssumeExpCmd LAnd(Le(CANON12:3 0xffffffffffffffffffffffffffffffffffffffff ) Ge(CANON12:3 0x0 ) )
		NopCmd
		AssumeExpCmd LAnd(Le(CANON13:4 0xffffffffffffffffffffffffffffffffffffffff ) Ge(CANON13:4 0x0 ) )
		AnnotationCmd:24 JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Cmd","cmd":{"cmd_type":"spec.cvlast.CVLCmd.Simple.Definition","cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/spec/ERC20.spec","start":{"line":96,"character":4},"end":{"line":96,"character":58}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Mathint"},"idL":[{"#class":"spec.cvlast.CVLLhs.Id","cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/spec/ERC20.spec","start":{"line":96,"character":4},"end":{"line":96,"character":28}},"id":"allowance_before","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":6}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Mathint"},"cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/spec/ERC20.spec","start":{"line":96,"character":4},"end":{"line":96,"character":58}}}}],"exp":{"#class":"spec.cvlast.CVLExp.ApplyExp.ContractFunction.Concrete","methodIdWithCallContext":{"#class":"spec.cvlast.ConcreteMethod","signature":{"#class":"spec.cvlast.ExternalQualifiedMethodSignature.ExternalQualifiedMethodSig","wrapped":{"#class":"spec.cvlast.QualifiedMethodSignature.QualifiedMethodSig","qualifiedMethodName":{"#class":"spec.cvlast.QualifiedFunction","host":{"name":"ERC20"},"methodId":"allowance"},"params":[{"#class":"spec.cvlast.VMParam.Named","name":"owner","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$address"}},{"#class":"spec.cvlast.VMParam.Named","name":"spender","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$address"}}],"res":[{"#class":"spec.cvlast.VMParam.Unnamed","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256}}]},"sighashInt":{"n":"dd62ed3e"}}},"args":[{"#class":"spec.cvlast.CVLExp.VariableExp","id":"holder","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":6}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"},"cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/spec/ERC20.spec","start":{"line":96,"character":4},"end":{"line":96,"character":58}}},"twoStateIndex":"NEITHER"},{"#class":"spec.cvlast.CVLExp.VariableExp","id":"spender","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":6}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"},"cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/spec/ERC20.spec","start":{"line":96,"character":4},"end":{"line":96,"character":58}}},"twoStateIndex":"NEITHER"}],"noRevert":true,"storage":{"#class":"spec.cvlast.CVLExp.VariableExp","id":"lastStorage","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":6}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.VMInternal.BlockchainState"},"cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/spec/ERC20.spec","start":{"line":96,"character":4},"end":{"line":96,"character":58}}},"twoStateIndex":"NEITHER"},"isWhole":false,"tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":6}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.VM","descriptor":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256},"context":{"#class":"spec.cvlast.typedescriptors.FromVMContext.ReturnValue"}},"cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/spec/ERC20.spec","start":{"line":96,"character":31},"end":{"line":96,"character":40}},"annotation":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.CallResolution$DirectPassing","target":{"methodSignature":{"#class":"spec.cvlast.ExternalQualifiedMethodSignature.ExternalQualifiedMethodSig","wrapped":{"#class":"spec.cvlast.QualifiedMethodSignature.QualifiedMethodSig","qualifiedMethodName":{"#class":"spec.cvlast.QualifiedFunction","host":{"name":"ERC20"},"methodId":"allowance"},"params":[{"#class":"spec.cvlast.VMParam.Named","name":"owner","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$address"}},{"#class":"spec.cvlast.VMParam.Named","name":"spender","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$address"}}],"res":[{"#class":"spec.cvlast.VMParam.Unnamed","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256}}]},"sighashInt":{"n":"dd62ed3e"}},"definitelyNonPayable":true,"annotation":{"visibility":"EXTERNAL","envFree":true,"library":false},"stateMutability":"view","tag":{"#class":"spec.cvlast.CVLImportedFunctionTag.WithMethodInfo","evmMethodInfo":{"sigHash":"dd62ed3e","name":"allowance","argTypes":[{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.address"},{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.address"}],"resultTypes":[{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256}],"stateMutability":"view","envfreeInfo":{"#class":"bridge.EnvfreeInfo.Unknown"},"isConstant":false,"paramNames":["owner","spender"],"isLibrary":false}}},"hasEnv":false}}},"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":6}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}}}}}
		AssignExpCmd:25 I15 CANON12:3
		AssignExpCmd:26 I16 CANON13:4
	}
	Block 0_0_0_1_0_0 Succ [1_0_0_0_0_0] {
		AnnotationCmd:24 JSON{"key":{"name":"call.trace.push","type":"analysis.icfg.Inliner$CallStack$PushRecord","erasureStrategy":"Canonical"},"value":"rO0ABXNyACphbmFseXNpcy5pY2ZnLklubGluZXIkQ2FsbFN0YWNrJFB1c2hSZWNvcmSX8+DCTLCH+AIAA0kACGNhbGxlZUlkTAAGY2FsbGVldAATTHZjL2RhdGEvTWV0aG9kUmVmO0wAB3N1bW1hcnl0ABVMdmMvZGF0YS9DYWxsU3VtbWFyeTt4cAAAAAFzcgARdmMuZGF0YS5NZXRob2RSZWbJlJTzzU9pGAIAA0wABGF0dHJ0ABdMc2NlbmUvTWV0aG9kQXR0cmlidXRlO0wACmNvbnRyYWN0SWR0ABZMamF2YS9tYXRoL0JpZ0ludGVnZXI7TAAHc2lnSGFzaHQAEExldm0vU2lnaGFzaEludDt4cHNyABxzY2VuZS5NZXRob2RBdHRyaWJ1dGUkQ29tbW9uNHjdebdr9XMCAAB4cgAVc2NlbmUuTWV0aG9kQXR0cmlidXRlcYg2pYWutuUCAAB4cHNyABRqYXZhLm1hdGguQmlnSW50ZWdlcoz8nx+pO/sdAwAGSQAIYml0Q291bnRJAAliaXRMZW5ndGhJABNmaXJzdE5vbnplcm9CeXRlTnVtSQAMbG93ZXN0U2V0Qml0SQAGc2lnbnVtWwAJbWFnbml0dWRldAACW0J4cgAQamF2YS5sYW5nLk51bWJlcoaslR0LlOCLAgAAeHD///////////////7////+AAAAAXVyAAJbQqzzF/gGCFTgAgAAeHAAAAAQzkYEoAAAAAAAAAAAAAAAA3hzcgAOZXZtLlNpZ2hhc2hJbnRUdcqNMXEgeAIAAUwAAW5xAH4ABnhwc3EAfgAM///////////////+/////gAAAAF1cQB+ABAAAAAE3WLtPnhw"}
		AssignHavocCmd:24 tacCalldatasize!!17:27
		NopCmd
		AssumeExpCmd Apply(add_noofl:bif 0x4 0x40)
		NopCmd
		AssumeExpCmd Apply(add_noofl:bif 0x4 0x0)
		AssignExpCmd:24 B20 LAnd(Ge(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff I15 ) Le(0x0 I15 ) )
		AssertCmd:24 B20 "sanity bounds check on cvl to vm encoding of certoraArg14071410:int failed"
		AssignExpCmd:24 R21 Apply(safe_math_narrow:bif I15)
		NopCmd
		AssumeExpCmd Apply(add_noofl:bif 0x4 0x20)
		AssignExpCmd:24 B23 LAnd(Ge(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff I16 ) Le(0x0 I16 ) )
		AssertCmd:24 B23 "sanity bounds check on cvl to vm encoding of certoraArg14111412:int failed"
		AssignExpCmd:24 R24 Apply(safe_math_narrow:bif I16)
		NopCmd
		AssumeExpCmd Eq(0x44 tacCalldatasize!!17:27 )
		LabelCmd:24 "Start procedure ERC20-allowance(address,address)"
		AnnotationCmd:24 JSON{"key":{"name":"fps.free-pointer-is-scalarized","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true}
		AssignExpCmd:24 R27:23 Select(tacExtcodesize!!0:0 Apply(to_skey:bif R4:28) )
		NopCmd
		AssumeExpCmd Gt(R27:23 0x0 )
		AnnotationCmd:24 JSON{"key":{"name":"internal.func.finder.info","type":"analysis.ip.InternalFunctionFinderReport","erasureStrategy":"Erased"},"value":"rO0ABXNyAChhbmFseXNpcy5pcC5JbnRlcm5hbEZ1bmN0aW9uRmluZGVyUmVwb3J0ian+bYn1VdACAAFMABN1bnJlc29sdmVkRnVuY3Rpb25zdAAPTGphdmEvdXRpbC9TZXQ7eHBzcgAhZGF0YXN0cnVjdHVyZXMuTGlua2VkQXJyYXlIYXNoU2V0AAAAAAAAAAEDAAJGAApsb2FkRmFjdG9yTAAJaGFzaFRhYmxldAAuTGRhdGFzdHJ1Y3R1cmVzL2FycmF5aGFzaHRhYmxlL0FycmF5SGFzaFRhYmxlO3hwdwgAAAAAQAAAAHg="}
		AnnotationCmd:24 JSON{"key":{"name":"fps.free-pointer-is-scalarized","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true}
		NopCmd
		AssumeExpCmd LNot(Lt(tacCalldatasize!!17:27 0x4 ) )
		NopCmd
		AssumeExpCmd LNot(Gt(0x70a08231 tacSighash!!5:16 ) )
		NopCmd
		AssumeExpCmd LNot(Gt(0xa9059cbb tacSighash!!5:16 ) )
		NopCmd
		AssumeExpCmd LNot(Eq(0xa9059cbb tacSighash!!5:16 ) )
		NopCmd
		AssumeExpCmd LNot(Eq(0xb2bdfa7b tacSighash!!5:16 ) )
		NopCmd
		AssumeExpCmd LNot(Eq(0xd0e30db0 tacSighash!!5:16 ) )
		NopCmd
		AssumeExpCmd Eq(0xdd62ed3e tacSighash!!5:16 )
		AssumeCmd:29 true
		AssignExpCmd:30 R36:31 Sub(tacCalldatasize!!17:27 0x4 )
		NopCmd
		AssumeExpCmd LNot(Slt(R36:31 0x40 ) )
		NopCmd
		AssumeExpCmd Le(R21 0xffffffffffffffffffffffffffffffffffffffff )
		NopCmd
		AssumeExpCmd Le(R24 0xffffffffffffffffffffffffffffffffffffffff )
		AnnotationCmd:24 JSON{"key":{"name":"internal.func.start","type":"analysis.ip.InternalFuncStartAnnotation","erasureStrategy":"CallTrace"},"value":{"id":0,"startPc":4858,"args":[{"s":{"namePrefix":"R21","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1012}]},"offset":1,"sort":"SCALAR"},{"s":{"namePrefix":"R24","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1012}]},"offset":2,"sort":"SCALAR"}],"methodSignature":{"#class":"spec.cvlast.QualifiedMethodSignature.QualifiedMethodSig","qualifiedMethodName":{"#class":"spec.cvlast.QualifiedFunction","host":{"name":"ERC20"},"methodId":"allowance"},"params":[{"#class":"spec.cvlast.VMParam.Named","name":"owner","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$address"}},{"#class":"spec.cvlast.VMParam.Named","name":"spender","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$address"}}],"res":[{"#class":"spec.cvlast.VMParam.Unnamed","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256}}]},"stackOffsetToArgPos":{"1":0,"2":1},"callSiteSrc":{"source":0,"begin":5647,"len":535,"jumpType":"ENTER","address":"ce4604a0000000000000000000000003","sourceContext":{"indexToFilepath":{"0":"contracts/ERC20.sol","1":"contracts/IERC20.sol","2":"contracts/IERC20Metadata.sol"},"sourceDir":".post_autofinders.0"}}}}
		AssignExpCmd:32 R44:33 Apply(hash_3_keccak:bif Apply(skey_basic:bif 0x40) Apply(to_skey:bif R21:34) Apply(skey_basic:bif 0x1))
		AssignExpCmd:35 R48:33 Apply(hash_3_keccak:bif Apply(skey_basic:bif 0x40) Apply(to_skey:bif R24:34) R44:36)
		AssignExpCmd:37 R49:33 Select(CANON28!!3:5 R48:38 )
		AnnotationCmd:24 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet","value":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R49","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1019}]},"displayPath":{"#class":"analysis.storage.DisplayPath.MapAccess","key":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R24","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1017}]},"keyTyp":{"#class":"tac.TACStorageType.IntegralType","typeLabel":"address","numBytes":"14","descriptor":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$address"},"lowerBound":null,"upperBound":null},"base":{"#class":"analysis.storage.DisplayPath.MapAccess","key":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R21","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1017}]},"keyTyp":{"#class":"tac.TACStorageType.IntegralType","typeLabel":"address","numBytes":"14","descriptor":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$address"},"lowerBound":null,"upperBound":null},"base":{"#class":"analysis.storage.DisplayPath.Root","name":"_allowances"}}},"storageType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256},"contractInstance":"ce4604a0000000000000000000000003","linkableStorageReadId":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet.None"}}}
		AnnotationCmd:24 JSON{"key":{"name":"internal.func.end","type":"analysis.ip.InternalFuncExitAnnotation","erasureStrategy":"Canonical"},"value":{"id":0,"rets":[{"s":{"namePrefix":"R49","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1023}]},"offset":0}],"functionLayout":{"0":{"#class":"analysis.ip.InternalFuncValueLocation.Scalar"}}}}
		AnnotationCmd:24 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.EVMFunctionReturnWrite","returnbufOffset":"0","returnValueSym":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R49","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1023}]},"callIndex":1}}
		AnnotationCmd:24 JSON{"key":{"name":"tac.return.path","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		LabelCmd:24 "End procedure ERC20-allowance(address,address)"
		AssignExpCmd:24 CANON33:39 R49:33
		AnnotationCmd:24 JSON{"key":{"name":"call.trace.pop","type":"analysis.icfg.Inliner$CallStack$PopRecord","erasureStrategy":"Canonical"},"value":"rO0ABXNyAClhbmFseXNpcy5pY2ZnLklubGluZXIkQ2FsbFN0YWNrJFBvcFJlY29yZPAPfwSLdCWJAgABSQAIY2FsbGVlSWR4cAAAAAE="}
	}
	Block 0_0_0_3_0_0 Succ [3_0_0_0_0_0] {
		AnnotationCmd:40 JSON{"key":{"name":"call.trace.push","type":"analysis.icfg.Inliner$CallStack$PushRecord","erasureStrategy":"Canonical"},"value":"rO0ABXNyACphbmFseXNpcy5pY2ZnLklubGluZXIkQ2FsbFN0YWNrJFB1c2hSZWNvcmSX8+DCTLCH+AIAA0kACGNhbGxlZUlkTAAGY2FsbGVldAATTHZjL2RhdGEvTWV0aG9kUmVmO0wAB3N1bW1hcnl0ABVMdmMvZGF0YS9DYWxsU3VtbWFyeTt4cAAAAANzcgARdmMuZGF0YS5NZXRob2RSZWbJlJTzzU9pGAIAA0wABGF0dHJ0ABdMc2NlbmUvTWV0aG9kQXR0cmlidXRlO0wACmNvbnRyYWN0SWR0ABZMamF2YS9tYXRoL0JpZ0ludGVnZXI7TAAHc2lnSGFzaHQAEExldm0vU2lnaGFzaEludDt4cHNyABxzY2VuZS5NZXRob2RBdHRyaWJ1dGUkQ29tbW9uNHjdebdr9XMCAAB4cgAVc2NlbmUuTWV0aG9kQXR0cmlidXRlcYg2pYWutuUCAAB4cHNyABRqYXZhLm1hdGguQmlnSW50ZWdlcoz8nx+pO/sdAwAGSQAIYml0Q291bnRJAAliaXRMZW5ndGhJABNmaXJzdE5vbnplcm9CeXRlTnVtSQAMbG93ZXN0U2V0Qml0SQAGc2lnbnVtWwAJbWFnbml0dWRldAACW0J4cgAQamF2YS5sYW5nLk51bWJlcoaslR0LlOCLAgAAeHD///////////////7////+AAAAAXVyAAJbQqzzF/gGCFTgAgAAeHAAAAAQzkYEoAAAAAAAAAAAAAAAA3hzcgAOZXZtLlNpZ2hhc2hJbnRUdcqNMXEgeAIAAUwAAW5xAH4ABnhwc3EAfgAM///////////////+/////gAAAAF1cQB+ABAAAAAE3WLtPnhw"}
		AssignHavocCmd:40 tacCalldatasize!!51:27
		NopCmd
		AssumeExpCmd Apply(add_noofl:bif 0x4 0x40)
		NopCmd
		AssumeExpCmd Apply(add_noofl:bif 0x4 0x0)
		AssignExpCmd:40 B54 LAnd(Ge(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff I175 ) Le(0x0 I175 ) )
		AssertCmd:40 B54 "sanity bounds check on cvl to vm encoding of certoraArg23342335:int failed"
		AssignExpCmd:40 R55 Apply(safe_math_narrow:bif I175)
		NopCmd
		AssumeExpCmd Apply(add_noofl:bif 0x4 0x20)
		AssignExpCmd:40 B57 LAnd(Ge(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff I176 ) Le(0x0 I176 ) )
		AssertCmd:40 B57 "sanity bounds check on cvl to vm encoding of certoraArg23362337:int failed"
		AssignExpCmd:40 R58 Apply(safe_math_narrow:bif I176)
		NopCmd
		AssumeExpCmd Eq(0x44 tacCalldatasize!!51:27 )
		LabelCmd:40 "Start procedure ERC20-allowance(address,address)"
		AnnotationCmd:40 JSON{"key":{"name":"fps.free-pointer-is-scalarized","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true}
		AssignExpCmd:40 R61:23 Select(tacExtcodesize!!0:0 Apply(to_skey:bif R4:28) )
		NopCmd
		AssumeExpCmd Gt(R61:23 0x0 )
		AnnotationCmd:40 JSON{"key":{"name":"internal.func.finder.info","type":"analysis.ip.InternalFunctionFinderReport","erasureStrategy":"Erased"},"value":"rO0ABXNyAChhbmFseXNpcy5pcC5JbnRlcm5hbEZ1bmN0aW9uRmluZGVyUmVwb3J0ian+bYn1VdACAAFMABN1bnJlc29sdmVkRnVuY3Rpb25zdAAPTGphdmEvdXRpbC9TZXQ7eHBzcgAhZGF0YXN0cnVjdHVyZXMuTGlua2VkQXJyYXlIYXNoU2V0AAAAAAAAAAEDAAJGAApsb2FkRmFjdG9yTAAJaGFzaFRhYmxldAAuTGRhdGFzdHJ1Y3R1cmVzL2FycmF5aGFzaHRhYmxlL0FycmF5SGFzaFRhYmxlO3hwdwgAAAAAQAAAAHg="}
		AnnotationCmd:40 JSON{"key":{"name":"fps.free-pointer-is-scalarized","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true}
		NopCmd
		AssumeExpCmd LNot(Lt(tacCalldatasize!!51:27 0x4 ) )
		NopCmd
		AssumeExpCmd LNot(Gt(0x70a08231 tacSighash!!7:16 ) )
		NopCmd
		AssumeExpCmd LNot(Gt(0xa9059cbb tacSighash!!7:16 ) )
		NopCmd
		AssumeExpCmd LNot(Eq(0xa9059cbb tacSighash!!7:16 ) )
		NopCmd
		AssumeExpCmd LNot(Eq(0xb2bdfa7b tacSighash!!7:16 ) )
		NopCmd
		AssumeExpCmd LNot(Eq(0xd0e30db0 tacSighash!!7:16 ) )
		NopCmd
		AssumeExpCmd Eq(0xdd62ed3e tacSighash!!7:16 )
		AssumeCmd:41 true
		AssignExpCmd:42 R70:31 Sub(tacCalldatasize!!51:27 0x4 )
		NopCmd
		AssumeExpCmd LNot(Slt(R70:31 0x40 ) )
		NopCmd
		AssumeExpCmd Le(R55 0xffffffffffffffffffffffffffffffffffffffff )
		NopCmd
		AssumeExpCmd Le(R58 0xffffffffffffffffffffffffffffffffffffffff )
		AnnotationCmd:40 JSON{"key":{"name":"internal.func.start","type":"analysis.ip.InternalFuncStartAnnotation","erasureStrategy":"CallTrace"},"value":{"id":2,"startPc":4858,"args":[{"s":{"namePrefix":"R55","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1012}]},"offset":1,"sort":"SCALAR"},{"s":{"namePrefix":"R58","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1012}]},"offset":2,"sort":"SCALAR"}],"methodSignature":{"#class":"spec.cvlast.QualifiedMethodSignature.QualifiedMethodSig","qualifiedMethodName":{"#class":"spec.cvlast.QualifiedFunction","host":{"name":"ERC20"},"methodId":"allowance"},"params":[{"#class":"spec.cvlast.VMParam.Named","name":"owner","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$address"}},{"#class":"spec.cvlast.VMParam.Named","name":"spender","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$address"}}],"res":[{"#class":"spec.cvlast.VMParam.Unnamed","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256}}]},"stackOffsetToArgPos":{"1":0,"2":1},"callSiteSrc":{"source":0,"begin":5647,"len":535,"jumpType":"ENTER","address":"ce4604a0000000000000000000000003","sourceContext":{"indexToFilepath":{"0":"contracts/ERC20.sol","1":"contracts/IERC20.sol","2":"contracts/IERC20Metadata.sol"},"sourceDir":".post_autofinders.0"}}}}
		AssignExpCmd:43 R78:33 Apply(hash_3_keccak:bif Apply(skey_basic:bif 0x40) Apply(to_skey:bif R55:34) Apply(skey_basic:bif 0x1))
		AssignExpCmd:44 R82:33 Apply(hash_3_keccak:bif Apply(skey_basic:bif 0x40) Apply(to_skey:bif R58:34) R78:36)
		AssignExpCmd:45 R83:33 Select(CANON28!!3:5 R82:46 )
		AnnotationCmd:40 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet","value":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R83","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1019}]},"displayPath":{"#class":"analysis.storage.DisplayPath.MapAccess","key":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R58","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1017}]},"keyTyp":{"#class":"tac.TACStorageType.IntegralType","typeLabel":"address","numBytes":"14","descriptor":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$address"},"lowerBound":null,"upperBound":null},"base":{"#class":"analysis.storage.DisplayPath.MapAccess","key":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R55","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1017}]},"keyTyp":{"#class":"tac.TACStorageType.IntegralType","typeLabel":"address","numBytes":"14","descriptor":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$address"},"lowerBound":null,"upperBound":null},"base":{"#class":"analysis.storage.DisplayPath.Root","name":"_allowances"}}},"storageType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256},"contractInstance":"ce4604a0000000000000000000000003","linkableStorageReadId":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet.None"}}}
		AnnotationCmd:40 JSON{"key":{"name":"internal.func.end","type":"analysis.ip.InternalFuncExitAnnotation","erasureStrategy":"Canonical"},"value":{"id":2,"rets":[{"s":{"namePrefix":"R83","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1023}]},"offset":0}],"functionLayout":{"0":{"#class":"analysis.ip.InternalFuncValueLocation.Scalar"}}}}
		AnnotationCmd:40 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.EVMFunctionReturnWrite","returnbufOffset":"0","returnValueSym":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R83","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1023}]},"callIndex":3}}
		AnnotationCmd:40 JSON{"key":{"name":"tac.return.path","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		LabelCmd:40 "End procedure ERC20-allowance(address,address)"
		AssignExpCmd:40 CANON91:47 R83:33
		AnnotationCmd:40 JSON{"key":{"name":"call.trace.pop","type":"analysis.icfg.Inliner$CallStack$PopRecord","erasureStrategy":"Canonical"},"value":"rO0ABXNyAClhbmFseXNpcy5pY2ZnLklubGluZXIkQ2FsbFN0YWNrJFBvcFJlY29yZPAPfwSLdCWJAgABSQAIY2FsbGVlSWR4cAAAAAM="}
	}
	Block 1_0_0_0_0_0 Succ [0_0_0_2_0_0] {
		AssumeNotCmd:24 false
		AssumeNotCmd:24 false
		AnnotationCmd JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageGlobalChangeSnippet.StorageTakeSnapshot","lhs":{"namePrefix":"lastStorage","tag":{"#class":"tac.Tag.BlockchainState"},"callIndex":0,"meta":[{"key":{"name":"cvl.local","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true},{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"lastStorage"},{"key":{"name":"cvl.type","type":"spec.cvlast.CVLType$PureCVLType","erasureStrategy":"CallTrace"},"value":{"#class":"spec.cvlast.CVLType.PureCVLType.VMInternal.BlockchainState"}},{"key":{"name":"cvl","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true},{"key":{"name":"cvl.display","type":"java.lang.String","erasureStrategy":"CallTrace"},"value":"lastStorage"}]}}}
		AnnotationCmd:24 JSON{"key":{"name":"cvl.label.end","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		NopCmd
		AssumeExpCmd LAnd(Le(CANON34:6 0xffffffffffffffffffffffffffffffffffffffff ) Ge(CANON34:6 0x0 ) )
		NopCmd
		AssumeExpCmd LAnd(Le(CANON35:7 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff ) Ge(CANON35:7 0x0 ) )
		NopCmd
		AssumeExpCmd LAnd(Le(CANON36:8 0xffffffffffffffffffffffffffffffffffffffff ) Ge(CANON36:8 0x0 ) )
		NopCmd
		AssumeExpCmd LAnd(Le(CANON37:9 0xffffffffffffffffffffffffffffffffffffffff ) Ge(CANON37:9 0x0 ) )
		NopCmd
		AssumeExpCmd LAnd(Le(CANON38:10 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff ) Ge(CANON38:10 0x0 ) )
		NopCmd
		AssumeExpCmd LAnd(Le(CANON39:11 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff ) Ge(CANON39:11 0x0 ) )
		NopCmd
		AssumeExpCmd LAnd(Le(CANON40:12 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff ) Ge(CANON40:12 0x0 ) )
		NopCmd
		AssumeExpCmd LAnd(Le(CANON41:13 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff ) Ge(CANON41:13 0x0 ) )
		AnnotationCmd:48 JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Cmd","cmd":{"cmd_type":"spec.cvlast.CVLCmd.Simple.Apply","cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/spec/ERC20.spec","start":{"line":99,"character":4},"end":{"line":99,"character":15}},"exp":{"#class":"spec.cvlast.CVLExp.ApplyExp.ContractFunction.Symbolic","methodIdWithCallContext":{"#class":"spec.cvlast.ParametricMethod","methodId":"f","host":{"name":"ERC20"}},"args":[{"#class":"spec.cvlast.CVLExp.VariableExp","id":"e","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":6}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"env","fields":[{"fieldName":"msg","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"msg","fields":[{"fieldName":"sender","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"value","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}}]}},{"fieldName":"tx","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"tx","fields":[{"fieldName":"origin","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}}]}},{"fieldName":"block","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"block","fields":[{"fieldName":"coinbase","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"difficulty","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"gaslimit","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"number","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"timestamp","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}}]}}]},"cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/spec/ERC20.spec","start":{"line":99,"character":4},"end":{"line":99,"character":15}}},"twoStateIndex":"NEITHER"},{"#class":"spec.cvlast.CVLExp.VariableExp","id":"args","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":6}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.VMInternal.RawArgs"},"cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/spec/ERC20.spec","start":{"line":99,"character":4},"end":{"line":99,"character":15}}},"twoStateIndex":"NEITHER"}],"noRevert":true,"storage":{"#class":"spec.cvlast.CVLExp.VariableExp","id":"lastStorage","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":6}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.VMInternal.BlockchainState"},"cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/spec/ERC20.spec","start":{"line":99,"character":4},"end":{"line":99,"character":15}}},"twoStateIndex":"NEITHER"},"tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":6}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Void"},"cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/spec/ERC20.spec","start":{"line":99,"character":4},"end":{"line":99,"character":5}}}},"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":6}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}}}}}
		NopCmd
		NopCmd
		NopCmd
		NopCmd
		NopCmd
		NopCmd
		AnnotationCmd:48 JSON{"key":{"name":"call.trace.push","type":"analysis.icfg.Inliner$CallStack$PushRecord","erasureStrategy":"Canonical"},"value":"rO0ABXNyACphbmFseXNpcy5pY2ZnLklubGluZXIkQ2FsbFN0YWNrJFB1c2hSZWNvcmSX8+DCTLCH+AIAA0kACGNhbGxlZUlkTAAGY2FsbGVldAATTHZjL2RhdGEvTWV0aG9kUmVmO0wAB3N1bW1hcnl0ABVMdmMvZGF0YS9DYWxsU3VtbWFyeTt4cAAAAAJzcgARdmMuZGF0YS5NZXRob2RSZWbJlJTzzU9pGAIAA0wABGF0dHJ0ABdMc2NlbmUvTWV0aG9kQXR0cmlidXRlO0wACmNvbnRyYWN0SWR0ABZMamF2YS9tYXRoL0JpZ0ludGVnZXI7TAAHc2lnSGFzaHQAEExldm0vU2lnaGFzaEludDt4cHNyABxzY2VuZS5NZXRob2RBdHRyaWJ1dGUkQ29tbW9uNHjdebdr9XMCAAB4cgAVc2NlbmUuTWV0aG9kQXR0cmlidXRlcYg2pYWutuUCAAB4cHNyABRqYXZhLm1hdGguQmlnSW50ZWdlcoz8nx+pO/sdAwAGSQAIYml0Q291bnRJAAliaXRMZW5ndGhJABNmaXJzdE5vbnplcm9CeXRlTnVtSQAMbG93ZXN0U2V0Qml0SQAGc2lnbnVtWwAJbWFnbml0dWRldAACW0J4cgAQamF2YS5sYW5nLk51bWJlcoaslR0LlOCLAgAAeHD///////////////7////+AAAAAXVyAAJbQqzzF/gGCFTgAgAAeHAAAAAQzkYEoAAAAAAAAAAAAAAAA3hzcgAOZXZtLlNpZ2hhc2hJbnRUdcqNMXEgeAIAAUwAAW5xAH4ABnhwc3EAfgAM///////////////+/////gAAAAF1cQB+ABAAAAAEBv3eA3hw"}
		NopCmd
		AssumeExpCmd Ge(CANON48:14 0x4 )
		NopCmd
		AssumeExpCmd Ge(0x7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff CANON48:14 )
		AssignExpCmd:48 B103 LAnd(Ge(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff CANON34:6 ) Le(0x0 CANON34:6 ) )
		AssertCmd:48 B103 "sanity bounds check on cvl to vm encoding of tacTmp!1683:int failed"
		AssignExpCmd:48 R104:23 Apply(safe_math_narrow:bif CANON34:6)
		NopCmd
		AssumeExpCmd LAnd(Le(R104:49 0xffffffffffffffffffffffffffffffffffffffff ) Ge(R104:49 0x0 ) )
		AssignExpCmd:48 B108 LAnd(Ge(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff CANON35:7 ) Le(0x0 CANON35:7 ) )
		AssertCmd:48 B108 "sanity bounds check on cvl to vm encoding of tacTmp!1686:int failed"
		AssignExpCmd:48 R109:23 Apply(safe_math_narrow:bif CANON35:7)
		NopCmd
		AssumeExpCmd LAnd(Le(R109:50 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff ) Ge(R109:50 0x0 ) )
		AssignExpCmd:48 B114 LAnd(Ge(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff CANON36:8 ) Le(0x0 CANON36:8 ) )
		AssertCmd:48 B114 "sanity bounds check on cvl to vm encoding of tacTmp!1690:int failed"
		AssignExpCmd:48 R115:23 Apply(safe_math_narrow:bif CANON36:8)
		NopCmd
		AssumeExpCmd LAnd(Le(R115:51 0xffffffffffffffffffffffffffffffffffffffff ) Ge(R115:51 0x0 ) )
		AssignExpCmd:48 B119 LAnd(Ge(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff CANON40:12 ) Le(0x0 CANON40:12 ) )
		AssertCmd:48 B119 "sanity bounds check on cvl to vm encoding of tacTmp!1693:int failed"
		AssignExpCmd:48 R120:23 Apply(safe_math_narrow:bif CANON40:12)
		NopCmd
		AssumeExpCmd LAnd(Le(R120:52 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff ) Ge(R120:52 0x0 ) )
		AssignExpCmd:48 B124 LAnd(Ge(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff CANON41:13 ) Le(0x0 CANON41:13 ) )
		AssertCmd:48 B124 "sanity bounds check on cvl to vm encoding of tacTmp!1696:int failed"
		AssignExpCmd:48 R125:23 Apply(safe_math_narrow:bif CANON41:13)
		NopCmd
		AssumeExpCmd LAnd(Le(R125:53 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff ) Ge(R125:53 0x0 ) )
		AssignExpCmd:48 B129 LAnd(Ge(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff CANON35:7 ) Le(0x0 CANON35:7 ) )
		AssertCmd:48 B129 "sanity bounds check on cvl to vm encoding of tacTmp!1699:int failed"
		AssignExpCmd:48 R130:23 Apply(safe_math_narrow:bif CANON35:7)
		AssignExpCmd:48 B132 LAnd(Ge(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff CANON34:6 ) Le(0x0 CANON34:6 ) )
		AssertCmd:48 B132 "sanity bounds check on cvl to vm encoding of tacTmp!1702:int failed"
		AssignExpCmd:48 R133:23 Apply(safe_math_narrow:bif CANON34:6)
		AssignExpCmd:48 R136:23 Select(tacBalance!!1:1 Apply(to_skey:bif R133:23) )
		AssignExpCmd:54 I137:23 IntSub(R136:23 R130:23 )
		AssignExpCmd:54 tacBalance!!138:1 Store(tacBalance!!1:1 Apply(to_skey:bif R133:23) I137:23 )
		AssignExpCmd:48 R139:23 Select(tacBalance!!138:1 Apply(to_skey:bif R4:15) )
		AssignExpCmd:54 R140:23 Add(R139:23 R130:23)
		NopCmd
		AssumeExpCmd Apply(add_noofl:bif R139:23 R130:23)
		AnnotationCmd:48 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.BalanceSnippet","srcAccountInfo":{"old":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R136","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}]},"new":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"I137","tag":{"#class":"tac.Tag.Int"},"callIndex":0,"meta":[{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}]},"addr":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R133","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}]}},"trgAccountInfo":{"old":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R139","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}]},"new":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R140","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}]},"addr":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R4","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"tacContractAt"},{"key":{"name":"tac.contract.sym.addr.name","type":"java.lang.String","erasureStrategy":"Erased"},"value":"ERC20"},{"key":{"name":"tac.contract.sym.addr","type":"java.math.BigInteger","erasureStrategy":"Erased"},"value":"ce4604a0000000000000000000000003"}]}},"transferredAmount":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R130","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}]}}}
		JumpCmd 0_0_0_2_0_0
	}
	Block 3_0_0_0_0_0 Succ [] {
		AssumeNotCmd:40 false
		AssumeNotCmd:40 false
		AnnotationCmd JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageGlobalChangeSnippet.StorageTakeSnapshot","lhs":{"namePrefix":"lastStorage","tag":{"#class":"tac.Tag.BlockchainState"},"callIndex":0,"meta":[{"key":{"name":"cvl.local","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true},{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"lastStorage"},{"key":{"name":"cvl.type","type":"spec.cvlast.CVLType$PureCVLType","erasureStrategy":"CallTrace"},"value":{"#class":"spec.cvlast.CVLType.PureCVLType.VMInternal.BlockchainState"}},{"key":{"name":"cvl","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true},{"key":{"name":"cvl.display","type":"java.lang.String","erasureStrategy":"CallTrace"},"value":"lastStorage"}]}}}
		AnnotationCmd:40 JSON{"key":{"name":"cvl.label.end","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		AnnotationCmd:55 JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Cmd","cmd":{"cmd_type":"spec.cvlast.CVLCmd.Simple.Assert","cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/spec/ERC20.spec","start":{"line":103,"character":4},"end":{"line":104,"character":58}},"exp":{"#class":"spec.cvlast.CVLExp.BinaryExp.ImpliesExp","l":{"#class":"spec.cvlast.CVLExp.RelopExp.ArithRelopExp.GtExp","l":{"#class":"spec.cvlast.CVLExp.VariableExp","id":"allowance_after","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":6}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Mathint"},"cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/spec/ERC20.spec","start":{"line":103,"character":4},"end":{"line":104,"character":58}}},"twoStateIndex":"NEITHER"},"r":{"#class":"spec.cvlast.CVLExp.VariableExp","id":"allowance_before","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":6}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Mathint"},"cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/spec/ERC20.spec","start":{"line":103,"character":4},"end":{"line":104,"character":58}}},"twoStateIndex":"NEITHER"},"tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":6}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"},"cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/spec/ERC20.spec","start":{"line":103,"character":11},"end":{"line":103,"character":45}}}},"r":{"#class":"spec.cvlast.CVLExp.RelopExp.EqExp","l":{"#class":"spec.cvlast.CVLExp.FieldSelectExp","structExp":{"#class":"spec.cvlast.CVLExp.FieldSelectExp","structExp":{"#class":"spec.cvlast.CVLExp.VariableExp","id":"e","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":6}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"env","fields":[{"fieldName":"msg","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"msg","fields":[{"fieldName":"sender","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"value","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}}]}},{"fieldName":"tx","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"tx","fields":[{"fieldName":"origin","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}}]}},{"fieldName":"block","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"block","fields":[{"fieldName":"coinbase","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"difficulty","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"gaslimit","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"number","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"timestamp","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}}]}}]},"cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/spec/ERC20.spec","start":{"line":103,"character":4},"end":{"line":104,"character":58}}},"twoStateIndex":"NEITHER"},"fieldName":"msg","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":6}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"msg","fields":[{"fieldName":"sender","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"value","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}}]},"cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/spec/ERC20.spec","start":{"line":103,"character":49},"end":{"line":103,"character":50}}}},"fieldName":"sender","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":6}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"},"cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/spec/ERC20.spec","start":{"line":103,"character":49},"end":{"line":103,"character":50}}}},"r":{"#class":"spec.cvlast.CVLExp.VariableExp","id":"holder","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":6}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"},"cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/spec/ERC20.spec","start":{"line":103,"character":4},"end":{"line":104,"character":58}}},"twoStateIndex":"NEITHER"},"tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":6}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"},"cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/spec/ERC20.spec","start":{"line":103,"character":49},"end":{"line":103,"character":71}}}},"tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":6}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"},"cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/spec/ERC20.spec","start":{"line":103,"character":11},"end":{"line":103,"character":71}}}},"description":"\"approve must only change the sender's allowance\"","scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":6}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}}}}}
		AssignExpCmd:56 I142 CANON91:47
		AssignExpCmd:57 I143 CANON33:39
		AssignExpCmd:58 B144 Gt(I142 I143 )
		NopCmd
		AssignExpCmd:59 I146 CANON12:3
		AssignExpCmd:60 CANON97!!147:61 Eq(CANON34:6 I146 )
		AssignExpCmd:62 CANON99!!148:61 LOr(LNot(B144 ) CANON97!!147:61 )
		AssertCmd:63 CANON99!!148:61 "\"approve must only change the sender's allowance\""
		AnnotationCmd:55 JSON{"key":{"name":"cvl.label.end","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		AnnotationCmd:64 JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Cmd","cmd":{"cmd_type":"spec.cvlast.CVLCmd.Simple.Assert","cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/spec/ERC20.spec","start":{"line":106,"character":4},"end":{"line":108,"character":69}},"exp":{"#class":"spec.cvlast.CVLExp.BinaryExp.ImpliesExp","l":{"#class":"spec.cvlast.CVLExp.RelopExp.ArithRelopExp.GtExp","l":{"#class":"spec.cvlast.CVLExp.VariableExp","id":"allowance_after","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":6}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Mathint"},"cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/spec/ERC20.spec","start":{"line":106,"character":4},"end":{"line":108,"character":69}}},"twoStateIndex":"NEITHER"},"r":{"#class":"spec.cvlast.CVLExp.VariableExp","id":"allowance_before","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":6}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Mathint"},"cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/spec/ERC20.spec","start":{"line":106,"character":4},"end":{"line":108,"character":69}}},"twoStateIndex":"NEITHER"},"tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":6}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"},"cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/spec/ERC20.spec","start":{"line":106,"character":11},"end":{"line":106,"character":45}}}},"r":{"#class":"spec.cvlast.CVLExp.BinaryExp.LorExp","l":{"#class":"spec.cvlast.CVLExp.RelopExp.EqExp","l":{"#class":"spec.cvlast.CVLExp.FieldSelectExp","structExp":{"#class":"spec.cvlast.CVLExp.VariableExp","id":"f","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":6}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"method","fields":[{"fieldName":"selector","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":32}},{"fieldName":"isPure","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}},{"fieldName":"isView","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}},{"fieldName":"isPayable","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}},{"fieldName":"numberOfArguments","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"isFallback","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}}]},"cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/spec/ERC20.spec","start":{"line":106,"character":4},"end":{"line":108,"character":69}}},"twoStateIndex":"NEITHER"},"fieldName":"selector","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":6}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":32},"cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/spec/ERC20.spec","start":{"line":107,"character":9},"end":{"line":107,"character":10}}}},"r":{"#class":"spec.cvlast.CVLExp.FieldSelectExp","structExp":{"#class":"spec.cvlast.CVLExp.Constant.SignatureLiteralExp","function":{"#class":"spec.cvlast.QualifiedMethodSignature.QualifiedMethodSig","qualifiedMethodName":{"#class":"spec.cvlast.QualifiedFunction","host":{"name":"ERC20"},"methodId":"approve"},"params":[{"#class":"spec.cvlast.VMParam.Unnamed","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$address"}},{"#class":"spec.cvlast.VMParam.Unnamed","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256}}],"res":[]},"tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":6}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"method","fields":[{"fieldName":"selector","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":32}},{"fieldName":"isPure","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}},{"fieldName":"isView","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}},{"fieldName":"isPayable","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}},{"fieldName":"numberOfArguments","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"isFallback","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}}]},"cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/spec/ERC20.spec","start":{"line":107,"character":27},"end":{"line":107,"character":48}},"annotation":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.CVLExp$Constant$StructLit","fieldNameToEntry":{"selector":{"#class":"spec.cvlast.CVLExp.Constant.NumberLit","n":"95ea7b3","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":6}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":32},"cvlRange":{"#class":"spec.cvlast.CVLRange.Empty"}}},"isPure":{"#class":"spec.cvlast.CVLExp.Constant.BoolLit","b":"0","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":6}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"},"cvlRange":{"#class":"spec.cvlast.CVLRange.Empty"}}},"isView":{"#class":"spec.cvlast.CVLExp.Constant.BoolLit","b":"0","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":6}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"},"cvlRange":{"#class":"spec.cvlast.CVLRange.Empty"}}},"isPayable":{"#class":"spec.cvlast.CVLExp.Constant.BoolLit","b":"0","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":6}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"},"cvlRange":{"#class":"spec.cvlast.CVLRange.Empty"}}},"isFallback":{"#class":"spec.cvlast.CVLExp.Constant.BoolLit","b":"0","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":6}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"},"cvlRange":{"#class":"spec.cvlast.CVLRange.Empty"}}},"numberOfArguments":{"#class":"spec.cvlast.CVLExp.Constant.NumberLit","n":"2","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":6}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256},"cvlRange":{"#class":"spec.cvlast.CVLRange.Empty"}}}},"tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":6}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"method","fields":[{"fieldName":"selector","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":32}},{"fieldName":"isPure","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}},{"fieldName":"isView","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}},{"fieldName":"isPayable","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}},{"fieldName":"numberOfArguments","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"isFallback","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}}]},"cvlRange":{"#class":"spec.cvlast.CVLRange.Empty"}}}}},"fieldName":"selector","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":6}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":32},"cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/spec/ERC20.spec","start":{"line":107,"character":27},"end":{"line":107,"character":48}}}},"tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":6}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"},"cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/spec/ERC20.spec","start":{"line":107,"character":9},"end":{"line":107,"character":57}}}},"r":{"#class":"spec.cvlast.CVLExp.RelopExp.EqExp","l":{"#class":"spec.cvlast.CVLExp.FieldSelectExp","structExp":{"#class":"spec.cvlast.CVLExp.VariableExp","id":"f","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":6}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"method","fields":[{"fieldName":"selector","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":32}},{"fieldName":"isPure","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}},{"fieldName":"isView","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}},{"fieldName":"isPayable","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}},{"fieldName":"numberOfArguments","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"isFallback","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}}]},"cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/spec/ERC20.spec","start":{"line":106,"character":4},"end":{"line":108,"character":69}}},"twoStateIndex":"NEITHER"},"fieldName":"selector","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":6}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":32},"cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/spec/ERC20.spec","start":{"line":107,"character":61},"end":{"line":107,"character":62}}}},"r":{"#class":"spec.cvlast.CVLExp.FieldSelectExp","structExp":{"#class":"spec.cvlast.CVLExp.Constant.SignatureLiteralExp","function":{"#class":"spec.cvlast.QualifiedMethodSignature.QualifiedMethodSig","qualifiedMethodName":{"#class":"spec.cvlast.QualifiedFunction","host":{"name":"ERC20"},"methodId":"increaseAllowance"},"params":[{"#class":"spec.cvlast.VMParam.Unnamed","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$address"}},{"#class":"spec.cvlast.VMParam.Unnamed","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256}}],"res":[]},"tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":6}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"method","fields":[{"fieldName":"selector","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":32}},{"fieldName":"isPure","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}},{"fieldName":"isView","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}},{"fieldName":"isPayable","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}},{"fieldName":"numberOfArguments","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"isFallback","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}}]},"cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/spec/ERC20.spec","start":{"line":107,"character":79},"end":{"line":107,"character":110}},"annotation":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.CVLExp$Constant$StructLit","fieldNameToEntry":{"selector":{"#class":"spec.cvlast.CVLExp.Constant.NumberLit","n":"39509351","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":6}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":32},"cvlRange":{"#class":"spec.cvlast.CVLRange.Empty"}}},"isPure":{"#class":"spec.cvlast.CVLExp.Constant.BoolLit","b":"0","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":6}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"},"cvlRange":{"#class":"spec.cvlast.CVLRange.Empty"}}},"isView":{"#class":"spec.cvlast.CVLExp.Constant.BoolLit","b":"0","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":6}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"},"cvlRange":{"#class":"spec.cvlast.CVLRange.Empty"}}},"isPayable":{"#class":"spec.cvlast.CVLExp.Constant.BoolLit","b":"0","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":6}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"},"cvlRange":{"#class":"spec.cvlast.CVLRange.Empty"}}},"isFallback":{"#class":"spec.cvlast.CVLExp.Constant.BoolLit","b":"0","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":6}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"},"cvlRange":{"#class":"spec.cvlast.CVLRange.Empty"}}},"numberOfArguments":{"#class":"spec.cvlast.CVLExp.Constant.NumberLit","n":"2","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":6}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256},"cvlRange":{"#class":"spec.cvlast.CVLRange.Empty"}}}},"tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":6}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"method","fields":[{"fieldName":"selector","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":32}},{"fieldName":"isPure","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}},{"fieldName":"isView","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}},{"fieldName":"isPayable","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}},{"fieldName":"numberOfArguments","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"isFallback","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}}]},"cvlRange":{"#class":"spec.cvlast.CVLRange.Empty"}}}}},"fieldName":"selector","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":6}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":32},"cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/spec/ERC20.spec","start":{"line":107,"character":79},"end":{"line":107,"character":110}}}},"tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":6}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"},"cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/spec/ERC20.spec","start":{"line":107,"character":61},"end":{"line":107,"character":119}}}},"tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":6}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"},"cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/spec/ERC20.spec","start":{"line":107,"character":9},"end":{"line":107,"character":119}}}},"tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":6}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"},"cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/spec/ERC20.spec","start":{"line":106,"character":11},"end":{"line":107,"character":120}}}},"description":"\"only approve and increaseAllowance can increase allowances\"","scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":6}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}}}}}
		AssignExpCmd:65 I149 CANON91:47
		AssignExpCmd:66 I150 CANON33:39
		AssignExpCmd:67 B151 Gt(I149 I150 )
		AssignExpCmd:68 CANON103:61 false
		AssignExpCmd:69 CANON104:61 false
		AssignExpCmd:70 CANON105:61 false
		AssignExpCmd:71 CANON106!!152:61 LOr(LNot(B151 ) false )
		AssertCmd:72 CANON106!!152:61 "\"only approve and increaseAllowance can increase allowances\""
		AnnotationCmd:64 JSON{"key":{"name":"cvl.label.end","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
	}
	Block 0_0_0_2_0_0 Succ [9043_1010_0_2_0_2, 0_0_0_2_0_268] {
		LabelCmd "Start procedure ERC20-name()"
		AnnotationCmd JSON{"key":{"name":"fps.free-pointer-is-scalarized","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true}
		AssignExpCmd R153:23 Select(tacExtcodesize!!0:0 Apply(to_skey:bif R4:28) )
		NopCmd
		AssumeExpCmd Gt(R153:23 0x0 )
		AnnotationCmd JSON{"key":{"name":"internal.func.finder.info","type":"analysis.ip.InternalFunctionFinderReport","erasureStrategy":"Erased"},"value":"rO0ABXNyAChhbmFseXNpcy5pcC5JbnRlcm5hbEZ1bmN0aW9uRmluZGVyUmVwb3J0ian+bYn1VdACAAFMABN1bnJlc29sdmVkRnVuY3Rpb25zdAAPTGphdmEvdXRpbC9TZXQ7eHBzcgAhZGF0YXN0cnVjdHVyZXMuTGlua2VkQXJyYXlIYXNoU2V0AAAAAAAAAAEDAAJGAApsb2FkRmFjdG9yTAAJaGFzaFRhYmxldAAuTGRhdGFzdHJ1Y3R1cmVzL2FycmF5aGFzaHRhYmxlL0FycmF5SGFzaFRhYmxlO3hwdwgAAAAAQAAAAHg="}
		AnnotationCmd JSON{"key":{"name":"fps.free-pointer-is-scalarized","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true}
		NopCmd
		AssumeExpCmd LNot(Lt(CANON48:14 0x4 ) )
		NopCmd
		AssumeExpCmd Gt(0x70a08231 tacSighash!!6:16 )
		NopCmd
		AssumeExpCmd Gt(0x2e1a7d4d tacSighash!!6:16 )
		NopCmd
		AssumeExpCmd Eq(0x6fdde03 tacSighash!!6:16 )
		NopCmd
		AssumeExpCmd Eq(R109:50 0x0 )
		AnnotationCmd JSON{"key":{"name":"internal.func.start","type":"analysis.ip.InternalFuncStartAnnotation","erasureStrategy":"CallTrace"},"value":{"id":1,"startPc":1023,"args":[],"methodSignature":{"#class":"spec.cvlast.QualifiedMethodSignature.QualifiedMethodSig","qualifiedMethodName":{"#class":"spec.cvlast.QualifiedFunction","host":{"name":"ERC20"},"methodId":"name"},"params":[],"res":[{"#class":"spec.cvlast.VMParam.Unnamed","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$StringType","location":"memory"}}]},"stackOffsetToArgPos":{},"callSiteSrc":{"source":0,"begin":2052,"len":353,"jumpType":"ENTER","address":"ce4604a0000000000000000000000003","sourceContext":{"indexToFilepath":{"0":"contracts/ERC20.sol","1":"contracts/IERC20.sol","2":"contracts/IERC20Metadata.sol"},"sourceDir":".post_autofinders.0"}}}}
		AssignExpCmd:73 tacM!!160:2 Store(tacM!!2:2 0x80 0x0 )
		AnnotationCmd JSON{"key":{"name":"pta.end-allocation","type":"analysis.alloc.AllocationAnalysis$AbstractLocation","erasureStrategy":"Erased"},"value":{"prevFPWriteIdx":0,"nextFPWriteCmd":{"block":{"#class":"tac.BlockIdentifier","origStartPc":260,"stkTop":1023,"decompCopy":0,"calleeIdx":0,"topOfStackValue":2,"freshCopy":0},"pos":8},"sort":{"#class":"analysis.alloc.AllocationAnalysis.Alloc.ConstBlock","sz":"20"}}}
		AssignExpCmd R161:74 0x80
		AnnotationCmd JSON{"key":{"name":"internal.func.end","type":"analysis.ip.InternalFuncExitAnnotation","erasureStrategy":"Canonical"},"value":{"id":1,"rets":[{"s":{"namePrefix":"R161","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1023}]},"offset":0}],"functionLayout":{"0":{"#class":"analysis.ip.InternalFuncValueLocation.Struct","memorySegments":{"0":{"namePrefix":"tacM!!160","tag":{"#class":"tac.Tag.ByteMap"},"callIndex":0,"meta":[{"key":{"name":"tac.is.memory","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}},{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"tacM"},{"key":{"name":"tac.memory.partition-id","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":0}]}}}}}}
		AssignExpCmd:75 tacM!!162:76 Store(tacM!!160:2 0xa0 0x20 )
		AnnotationCmd JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.EVMFunctionReturnWrite","returnbufOffset":"0","returnValueSym":{"#class":"vc.data.TACSymbol.Const","value":"20"},"callIndex":2}}
		AssignExpCmd:77 R163:78 Select(tacM!!162:76 0x80 )
		AnnotationCmd JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.EVMFunctionReturnWrite","returnbufOffset":"20","returnValueSym":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R163","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1012}]},"callIndex":2}}
		AnnotationCmd JSON{"key":{"name":"dsa.assign.start","type":"java.lang.String","erasureStrategy":"Erased"},"value":"9031_1011_0_0_0_0 -> 9034_1010_0_0_0_0"}
		LabelCmd "Parallel assignment for B5169:bool, R5170:bv256 := B5128:bool, R5129:bv256"
		NopCmd
		AnnotationCmd JSON{"key":{"name":"dsa.assign.end","type":"java.lang.String","erasureStrategy":"Erased"},"value":"9031_1011_0_0_0_0 -> 9034_1010_0_0_0_0"}
		AnnotationCmd JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.LoopSnippet.CopyLoop"}}
		AnnotationCmd JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.LoopSnippet.StartLoopSnippet","loopIndex":0,"loopSource":"unknown loop source code"}}
		AnnotationCmd JSON{"key":{"name":"start_loop.cmd","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		AssignExpCmd B166:79 Lt(0x0 R163:78 )
		JumpiCmd:80 9043_1010_0_2_0_2 0_0_0_2_0_268 B166:79
	}
	Block 9076_1010_0_2_0_0 Succ [2_0_0_0_0_0] {
		AnnotationCmd JSON{"key":{"name":"tac.return.path","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		LabelCmd "End procedure ERC20-name()"
		JumpCmd 2_0_0_0_0_0
	}
	Block 9043_1010_0_2_0_0 Succ [9061_1010_0_2_0_0] {
		AnnotationCmd JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.LoopSnippet.StartIter","iteration":4}}
		AnnotationCmd JSON{"key":{"name":"dsa.assign.start","type":"java.lang.String","erasureStrategy":"Erased"},"value":"9043_1010_0_0_0_0 -> 9034_1010_0_0_0_0"}
		LabelCmd "Parallel assignment for B5169:bool, R5170:bv256 := B5167:bool, R5164:bv256"
		NopCmd
		AnnotationCmd JSON{"key":{"name":"dsa.assign.end","type":"java.lang.String","erasureStrategy":"Erased"},"value":"9043_1010_0_0_0_0 -> 9034_1010_0_0_0_0"}
		AnnotationCmd JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.LoopSnippet.EndIter","iteration":4}}
		NopCmd
		AssignExpCmd B172:79 LNot(Lt(0x80 R163:78 ) )
		AnnotationCmd JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.LoopSnippet.AssertUnwindCond","assertCond":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"B172","tag":{"#class":"tac.Tag.Bool"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1009}]},"msg":"Unwinding condition in a loop"}}
		AssertCmd B172:79 "Unwinding condition in a loop"
		AnnotationCmd JSON{"key":{"name":"snippet.cmd.scope.end","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		LabelCmd "Parallel assignment for R173:bv256 := R170:bv256"
		AssignExpCmd R173:81 0x80
	}
	Block 9061_1010_0_2_0_0 Succ [9070_1010_0_2_0_0, 9076_1010_0_2_0_0] {
		AnnotationCmd JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.LoopSnippet.EndLoopSnippet","loopId":0}}
		AnnotationCmd JSON{"key":{"name":"end_loop.cmd","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		AssignExpCmd B174:79 Gt(R173:81 R163:78 )
		JumpiCmd:82 9070_1010_0_2_0_0 9076_1010_0_2_0_0 B174:79
	}
	Block 9070_1010_0_2_0_0 Succ [9076_1010_0_2_0_0] {
		JumpCmd 9076_1010_0_2_0_0
	}
	Block 2_0_0_0_0_0 Succ [0_0_0_3_0_0] {
		AnnotationCmd:48 JSON{"key":{"name":"call.trace.pop","type":"analysis.icfg.Inliner$CallStack$PopRecord","erasureStrategy":"Canonical"},"value":"rO0ABXNyAClhbmFseXNpcy5pY2ZnLklubGluZXIkQ2FsbFN0YWNrJFBvcFJlY29yZPAPfwSLdCWJAgABSQAIY2FsbGVlSWR4cAAAAAI="}
		AssumeNotCmd:48 false
		AssumeNotCmd:48 false
		AnnotationCmd JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageGlobalChangeSnippet.StorageTakeSnapshot","lhs":{"namePrefix":"lastStorage","tag":{"#class":"tac.Tag.BlockchainState"},"callIndex":0,"meta":[{"key":{"name":"cvl.local","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true},{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"lastStorage"},{"key":{"name":"cvl.type","type":"spec.cvlast.CVLType$PureCVLType","erasureStrategy":"CallTrace"},"value":{"#class":"spec.cvlast.CVLType.PureCVLType.VMInternal.BlockchainState"}},{"key":{"name":"cvl","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true},{"key":{"name":"cvl.display","type":"java.lang.String","erasureStrategy":"CallTrace"},"value":"lastStorage"}]}}}
		AnnotationCmd:48 JSON{"key":{"name":"cvl.label.end","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		AnnotationCmd:40 JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Cmd","cmd":{"cmd_type":"spec.cvlast.CVLCmd.Simple.Definition","cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/spec/ERC20.spec","start":{"line":101,"character":4},"end":{"line":101,"character":57}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Mathint"},"idL":[{"#class":"spec.cvlast.CVLLhs.Id","cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/spec/ERC20.spec","start":{"line":101,"character":4},"end":{"line":101,"character":27}},"id":"allowance_after","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":6}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Mathint"},"cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/spec/ERC20.spec","start":{"line":101,"character":4},"end":{"line":101,"character":57}}}}],"exp":{"#class":"spec.cvlast.CVLExp.ApplyExp.ContractFunction.Concrete","methodIdWithCallContext":{"#class":"spec.cvlast.ConcreteMethod","signature":{"#class":"spec.cvlast.ExternalQualifiedMethodSignature.ExternalQualifiedMethodSig","wrapped":{"#class":"spec.cvlast.QualifiedMethodSignature.QualifiedMethodSig","qualifiedMethodName":{"#class":"spec.cvlast.QualifiedFunction","host":{"name":"ERC20"},"methodId":"allowance"},"params":[{"#class":"spec.cvlast.VMParam.Named","name":"owner","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$address"}},{"#class":"spec.cvlast.VMParam.Named","name":"spender","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$address"}}],"res":[{"#class":"spec.cvlast.VMParam.Unnamed","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256}}]},"sighashInt":{"n":"dd62ed3e"}}},"args":[{"#class":"spec.cvlast.CVLExp.VariableExp","id":"holder","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":6}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"},"cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/spec/ERC20.spec","start":{"line":101,"character":4},"end":{"line":101,"character":57}}},"twoStateIndex":"NEITHER"},{"#class":"spec.cvlast.CVLExp.VariableExp","id":"spender","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":6}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"},"cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/spec/ERC20.spec","start":{"line":101,"character":4},"end":{"line":101,"character":57}}},"twoStateIndex":"NEITHER"}],"noRevert":true,"storage":{"#class":"spec.cvlast.CVLExp.VariableExp","id":"lastStorage","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":6}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.VMInternal.BlockchainState"},"cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/spec/ERC20.spec","start":{"line":101,"character":4},"end":{"line":101,"character":57}}},"twoStateIndex":"NEITHER"},"isWhole":false,"tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":6}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.VM","descriptor":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256},"context":{"#class":"spec.cvlast.typedescriptors.FromVMContext.ReturnValue"}},"cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/spec/ERC20.spec","start":{"line":101,"character":30},"end":{"line":101,"character":39}},"annotation":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.CallResolution$DirectPassing","target":{"methodSignature":{"#class":"spec.cvlast.ExternalQualifiedMethodSignature.ExternalQualifiedMethodSig","wrapped":{"#class":"spec.cvlast.QualifiedMethodSignature.QualifiedMethodSig","qualifiedMethodName":{"#class":"spec.cvlast.QualifiedFunction","host":{"name":"ERC20"},"methodId":"allowance"},"params":[{"#class":"spec.cvlast.VMParam.Named","name":"owner","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$address"}},{"#class":"spec.cvlast.VMParam.Named","name":"spender","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$address"}}],"res":[{"#class":"spec.cvlast.VMParam.Unnamed","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256}}]},"sighashInt":{"n":"dd62ed3e"}},"definitelyNonPayable":true,"annotation":{"visibility":"EXTERNAL","envFree":true,"library":false},"stateMutability":"view","tag":{"#class":"spec.cvlast.CVLImportedFunctionTag.WithMethodInfo","evmMethodInfo":{"sigHash":"dd62ed3e","name":"allowance","argTypes":[{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.address"},{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.address"}],"resultTypes":[{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256}],"stateMutability":"view","envfreeInfo":{"#class":"bridge.EnvfreeInfo.Unknown"},"isConstant":false,"paramNames":["owner","spender"],"isLibrary":false}}},"hasEnv":false}}},"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":6}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}}}}}
		AssignExpCmd:83 I175 CANON12:3
		AssignExpCmd:84 I176 CANON13:4
	}
	Block 9043_1010_0_2_0_2 Succ [9043_1010_0_2_0_4, 9043_1010_0_2_0_269] {
		AnnotationCmd JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.LoopSnippet.StartIter","iteration":1}}
		AnnotationCmd JSON{"key":{"name":"dsa.assign.start","type":"java.lang.String","erasureStrategy":"Erased"},"value":"9043_1010_0_0_0_0 -> 9034_1010_0_0_0_0"}
		LabelCmd "Parallel assignment for B5169:bool, R5170:bv256 := B5167:bool, R5164:bv256"
		NopCmd
		AnnotationCmd JSON{"key":{"name":"dsa.assign.end","type":"java.lang.String","erasureStrategy":"Erased"},"value":"9043_1010_0_0_0_0 -> 9034_1010_0_0_0_0"}
		AnnotationCmd JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.LoopSnippet.EndIter","iteration":1}}
		AssignExpCmd B180:79 Lt(0x20 R163:78 )
		JumpiCmd:80 9043_1010_0_2_0_4 9043_1010_0_2_0_269 B180:79
	}
	Block 9043_1010_0_2_0_6 Succ [9043_1010_0_2_0_0, 9043_1010_0_2_0_271] {
		AnnotationCmd JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.LoopSnippet.StartIter","iteration":3}}
		AnnotationCmd JSON{"key":{"name":"dsa.assign.start","type":"java.lang.String","erasureStrategy":"Erased"},"value":"9043_1010_0_0_0_0 -> 9034_1010_0_0_0_0"}
		LabelCmd "Parallel assignment for B5169:bool, R5170:bv256 := B5167:bool, R5164:bv256"
		NopCmd
		AnnotationCmd JSON{"key":{"name":"dsa.assign.end","type":"java.lang.String","erasureStrategy":"Erased"},"value":"9043_1010_0_0_0_0 -> 9034_1010_0_0_0_0"}
		AnnotationCmd JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.LoopSnippet.EndIter","iteration":3}}
		AssignExpCmd B184:79 Lt(0x60 R163:78 )
		JumpiCmd:80 9043_1010_0_2_0_0 9043_1010_0_2_0_271 B184:79
	}
	Block 9043_1010_0_2_0_4 Succ [9043_1010_0_2_0_6, 9043_1010_0_2_0_270] {
		AnnotationCmd JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.LoopSnippet.StartIter","iteration":2}}
		AnnotationCmd JSON{"key":{"name":"dsa.assign.start","type":"java.lang.String","erasureStrategy":"Erased"},"value":"9043_1010_0_0_0_0 -> 9034_1010_0_0_0_0"}
		LabelCmd "Parallel assignment for B5169:bool, R5170:bv256 := B5167:bool, R5164:bv256"
		NopCmd
		AnnotationCmd JSON{"key":{"name":"dsa.assign.end","type":"java.lang.String","erasureStrategy":"Erased"},"value":"9043_1010_0_0_0_0 -> 9034_1010_0_0_0_0"}
		AnnotationCmd JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.LoopSnippet.EndIter","iteration":2}}
		AssignExpCmd B188:79 Lt(0x40 R163:78 )
		JumpiCmd:80 9043_1010_0_2_0_6 9043_1010_0_2_0_270 B188:79
	}
	Block 0_0_0_2_0_268 Succ [9061_1010_0_2_0_0] {
		LabelCmd "Parallel assignment for R173:bv256 := R165:bv256"
		AssignExpCmd R173:81 0x0
	}
	Block 9043_1010_0_2_0_269 Succ [9061_1010_0_2_0_0] {
		LabelCmd "Parallel assignment for R173:bv256 := R179:bv256"
		AssignExpCmd R173:81 0x20
	}
	Block 9043_1010_0_2_0_270 Succ [9061_1010_0_2_0_0] {
		LabelCmd "Parallel assignment for R173:bv256 := R187:bv256"
		AssignExpCmd R173:81 0x40
	}
	Block 9043_1010_0_2_0_271 Succ [9061_1010_0_2_0_0] {
		LabelCmd "Parallel assignment for R173:bv256 := R183:bv256"
		AssignExpCmd R173:81 0x60
	}
}
Axioms {
		CANON107
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
        "name": "tac.is.memory",
        "type": "tac.MetaMap$Companion$NothingValue",
        "erasureStrategy": "Canonical"
      },
      "value": {
      }
    },
    {
      "key": {
        "name": "Tac.symbol.keyword",
        "type": "java.lang.String",
        "erasureStrategy": "Canonical"
      },
      "value": "tacM"
    },
    {
      "key": {
        "name": "tac.memory.partition-id",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 0
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
      "value": "holder"
    }
  ],
  "4": [
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
  "13": [
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
  "50": [
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
  "51": [
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
  "52": [
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
  "53": [
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
  "54": [
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
  "55": [
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
  "56": [
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
  "57": [
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
  "58": [
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
            "namePrefix": "I142",
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
            "namePrefix": "I143",
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
  "59": [
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
  "60": [
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
            "namePrefix": "CANON98",
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
            "namePrefix": "I146",
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
  "61": [
    {
      "key": {
        "name": "cvl",
        "type": "java.lang.Boolean",
        "erasureStrategy": "Canonical"
      },
      "value": true
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
            "namePrefix": "B144",
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
            "namePrefix": "CANON97!!147",
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
  "63": [
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
  "64": [
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
  "65": [
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
  "66": [
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
  "67": [
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
            "namePrefix": "I149",
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
            "namePrefix": "I150",
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
  "68": [
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
            "value": "6fdde03"
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
  "69": [
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
            "value": "6fdde03"
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
  "70": [
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
            "namePrefix": "B151",
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
  "72": [
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
  "73": [
    {
      "key": {
        "name": "tac.meta",
        "type": "vc.data.TACMetaInfo",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "source": 0,
        "begin": 2389,
        "len": 9,
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
  ],
  "75": [
    {
      "key": {
        "name": "tac.meta",
        "type": "vc.data.TACMetaInfo",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "source": 3,
        "begin": 8065,
        "len": 47,
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
        "name": "tac.return.write",
        "type": "analysis.icfg.ExtCallSummarization$CallSummaryReturnWriteInfo",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "summaryId": 0,
        "offset": "0"
      }
    }
  ],
  "76": [
    {
      "key": {
        "name": "tac.is.memory",
        "type": "tac.MetaMap$Companion$NothingValue",
        "erasureStrategy": "Canonical"
      },
      "value": {
      }
    },
    {
      "key": {
        "name": "Tac.symbol.keyword",
        "type": "java.lang.String",
        "erasureStrategy": "Canonical"
      },
      "value": "tacM"
    },
    {
      "key": {
        "name": "tac.memory.partition-id",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 1
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
        "begin": 12998,
        "len": 12,
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
      "value": 1012
    }
  ],
  "79": [
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
  "80": [
    {
      "key": {
        "name": "tac.meta",
        "type": "vc.data.TACMetaInfo",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "source": 3,
        "begin": 14442,
        "len": 113,
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
      "value": 1010
    }
  ],
  "82": [
    {
      "key": {
        "name": "tac.meta",
        "type": "vc.data.TACMetaInfo",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "source": 3,
        "begin": 14564,
        "len": 2,
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
  "83": [
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
  "84": [
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