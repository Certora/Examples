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
		CANON71:JSON{"name":"CANON71","paramSorts":[],"returnSort":{"#class":"tac.Tag.Int"},"attribute":"Ghost","cvlResultType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Mathint"},"cvlParamTypes":[],"declarationName":"CANON71"}
		I187:JSON{"name":"I187","paramSorts":[],"returnSort":{"#class":"tac.Tag.Int"},"attribute":"Ghost","cvlResultType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Mathint"},"cvlParamTypes":[],"declarationName":"CANON71"}
		I8:JSON{"name":"I8","paramSorts":[],"returnSort":{"#class":"tac.Tag.Int"},"attribute":"Ghost","cvlResultType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Mathint"},"cvlParamTypes":[],"declarationName":"CANON71"}
	}
	tacCaller@3:bv256
	tacCalldatabufCANON0@3:bv256
	tacCalldatabufCANON1@3:bv256
	tacMCANON0!!1:bytemap
	tacMCANON1!!2:bytemap
	tacM0x0!!49:bv256
	tacM0x0!!72:bv256
	tacAddress!!37:bv256
	tacAddress!!60:bv256
	tacAddress!!96:bv256
	tacOrigin!!100:bv256
	tacCallvalue@3:bv256
	lastReverted:bool
	lastReverted@1:bool
	lastReverted@2:bool
	lastReverted@3:bool
	tacM0x0!!169:bv256
	tacM0x0!!179:bv256
	tacM0x0!!190:bv256
	tacExtcodesize!!0:wordmap
	CANON26!!4:wordmap
	tacSCANON0!!10:wordmap
	CANON62!!5:bv256
	CANON64!!6:wordmap
	CANON67!!7:bv256
	tacCalldatasize@1:bv256
	tacCalldatasize@2:bv256
	tacCalldatasize@3:bv256
	CANON33!!136:bool
	tacCallvalue!!94:bv256
	tacM0x0@1:bv256
	tacM0x0@2:bv256
	tacM0x0@3:bv256
	CANON110!!155:bool
	tacExtcodesize:wordmap
	CANON100:bv256
	CANON101:bv256
	CANON102:bv256
	CANON103:bv256
	CANON104:int
	CANON105:bv256
	CANON106:bv256
	CANON107:bool
	CANON108:bool
	CANON109:bool
	CANON110:bool
	CANON113:bv256
	CANON116:int
	CANON117:int
	CANON118:int
	CANON119:int
	CANON122:bv256
	tacCalldatasize!!31:bv256
	tacCalldatasize!!54:bv256
	tacCalldatasize!!77:bv256
	tacMCANON0@3:bytemap
	tacMCANON1@3:bytemap
	tacMCANON2@3:bytemap
	tacBalance:wordmap
	tacTimestamp!!110:bv256
	tacNumber@3:bv256
	tacBalance!!3:wordmap
	CANON26!!182:wordmap
	CANON47!!142:bool
	I8:int
	R9:bv256
	B14:bool
	B15:bool
	B16:bool
	B18:bool
	B19:bool
	B20:bool
	B21:bool
	B22:bool
	B23:bool
	B24:bool
	B25:bool
	B26:bool
	B27:bool
	B28:bool
	B32:bool
	B33:bool
	B34:bool
	B36:bool
	B39:bool
	B40:bool
	B41:bool
	B42:bool
	B43:bool
	B45:bool
	B47:bool
	B55:bool
	B56:bool
	B57:bool
	B59:bool
	B62:bool
	B63:bool
	B64:bool
	B65:bool
	B66:bool
	B68:bool
	B70:bool
	B78:bool
	B79:bool
	B80:bool
	B82:bool
	B83:bool
	B85:bool
	B87:bool
	B90:bool
	B92:bool
	B95:bool
	B98:bool
	I29:int
	I30:int
	I53:int
	I76:int
	I86:int
	I91:int
	I97:int
	R17:bv256
	R35:bv256
	R38:bv256
	R44:bv256
	R46:bv256
	R48:bv256
	R50:(uninterp) skey
	R51:bv256
	R52:bv256
	R58:bv256
	R61:bv256
	R67:bv256
	R69:bv256
	R71:bv256
	R73:(uninterp) skey
	R74:bv256
	R75:bv256
	R81:bv256
	R84:bv256
	R88:bv256
	R93:bv256
	R99:bv256
	B101:bool
	B103:bool
	B106:bool
	B108:bool
	B111:bool
	B113:bool
	B116:bool
	B125:bool
	B127:bool
	B128:bool
	B129:bool
	B130:bool
	B131:bool
	B132:bool
	B134:bool
	B140:bool
	B143:bool
	B146:bool
	B154:bool
	B156:bool
	B158:bool
	B163:bool
	B172:bool
	B194:bool
	B197:bool
	B209:bool
	I102:int
	I107:int
	I112:int
	I115:int
	I121:int
	I133:int
	I135:int
	I137:int
	I138:int
	I139:int
	I141:int
	I144:int
	I147:int
	I148:int
	I149:int
	I150:int
	I151:int
	I152:int
	I153:int
	I183:int
	I184:int
	I185:int
	I186:int
	I187:int
	I200:int
	I201:int
	R104:bv256
	R109:bv256
	R114:bv256
	R117:bv256
	R118:bv256
	R119:bv256
	R120:bv256
	R123:bv256
	R124:bv256
	R126:bv256
	R157:bv256
	R162:bv256
	R168:bv256
	R170:(uninterp) skey
	R171:bv256
	R177:bv256
	R178:bv256
	R180:(uninterp) skey
	R181:bv256
	R188:bv256
	R189:bv256
	R191:(uninterp) skey
	R192:bv256
	R193:bv256
	R195:bv256
	R196:bv256
	R198:bv256
	R199:bv256
	R202:bv256
	R207:bv256
	R208:bv256
	lastHasThrown!!204:bool
	lastHasThrown!!206:bool
	lastHasThrown!!211:bool
	tacAddress@1:bv256
	tacAddress@2:bv256
	tacAddress@3:bv256
	lastReverted!!203:bool
	lastReverted!!205:bool
	lastReverted!!210:bool
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
	LCANON4@1:bv256
	LCANON4@2:bv256
	LCANON5@1:bv256
	LCANON5@2:bv256
	LCANON6@1:bool
	LCANON6@2:bool
	LCANON7@1:bv256
	LCANON7@2:bv256
	LCANON8@1:bv256
	LCANON8@2:bv256
	LCANON9@1:bool
	LCANON9@2:bool
	tacMCANON0!!159:bytemap
	tacMCANON0!!160:bytemap
	tacMCANON0!!161:bytemap
	tacMCANON0!!164:bytemap
	tacMCANON0!!165:bytemap
	tacMCANON0!!166:bytemap
	tacMCANON0!!167:bytemap
	tacMCANON0!!173:bytemap
	tacMCANON0!!174:bytemap
	tacMCANON0!!175:bytemap
	tacMCANON0!!176:bytemap
	tacOrigin@3:bv256
	CANON10:int
	CANON11:int
	CANON12:int
	CANON13:int
	CANON14:int
	CANON15:int
	CANON16:int
	CANON17:int
	CANON18:bool
	CANON19:bool
	CANON20:bool
	CANON21:bv256
	CANON22:bool
	CANON23@1:bv256
	CANON23@2:bv256
	CANON23@3:bv256
	CANON24@1:bool
	CANON24@2:bool
	CANON24@3:bool
	CANON25:bool
	CANON26:wordmap
	CANON29:int
	CANON30:int
	CANON31:bool
	CANON32:int
	CANON33:bool
	CANON35:int
	CANON36:bool
	CANON37:bool
	CANON38:bool
	CANON39:bv256
	CANON40:bool
	CANON41:bool
	CANON42:int
	CANON43:int
	CANON44:int
	CANON45:bool
	CANON46:int
	CANON47:bool
	CANON49:bool
	CANON50:int
	CANON51:bool
	CANON52:bool
	CANON53:int
	CANON54:int
	CANON55:int
	CANON56:int
	CANON57:int
	CANON58:int
	CANON59:int
	CANON60:wordmap
	CANON61:bv256
	CANON62:bv256
	CANON63:wordmap
	CANON64:wordmap
	CANON65:wordmap
	CANON66:bv256
	CANON67:bv256
	CANON68:wordmap
	CANON70:int
	CANON71:int
	CANON72:bool
	CANON73:bool
	CANON74:bool
	CANON75:bv256
	CANON76:bool
	CANON77:bool
	CANON78:bv256
	CANON79:bool
	CANON80:int
	CANON81:bool
	CANON82:bv256
	CANON83:int
	CANON84:bool
	CANON85:bv256
	CANON86:int
	CANON87:bool
	CANON88:bv256
	CANON89:int
	CANON90:bool
	CANON91:bv256
	CANON92:int
	CANON93:bool
	CANON94:bv256
	CANON95:int
	CANON96:bool
	CANON97:bv256
	CANON98:int
	CANON99:bool
	CANON51!!145:bool
	LCANON10@1:bv256
	LCANON10@2:bv256
	LCANON11@1:bv256
	LCANON11@2:bv256
	LCANON12@1:bv256
	LCANON12@2:bv256
	LCANON13@1:bv256
	LCANON13@2:bv256
	LCANON14@1:bv256
	LCANON14@2:bv256
	LCANON15@3:bool
	LCANON16@3:bv256
	LCANON17@3:bool
	LCANON18@3:bv256
	LCANON19@3:bool
	LCANON20@3:bv256
	LCANON21@3:bv256
	LCANON22@3:bv256
	LCANON23@3:bv256
	LCANON24@3:bool
	LCANON25@3:bv256
	LCANON26@3:bv256
	LCANON27@3:bool
	LCANON28@3:bv256
	LCANON29@3:bv256
	LCANON30@3:bv256
	LCANON31@3:bool
	LCANON32@3:bv256
	LCANON33@3:bv256
	LCANON34@3:bv256
	LCANON35@3:bv256
	LCANON36@3:bv256
	LCANON37@3:bool
	LCANON38@3:bv256
	LCANON39@3:bv256
	LCANON40@3:bv256
	LCANON41@3:bv256
	LCANON42@3:bv256
	LCANON43@3:bv256
	LCANON44@3:bv256
	LCANON45@3:bv256
	LCANON46@3:bv256
	LCANON47@3:bv256
	LCANON48@3:bool
	LCANON49@3:bv256
	LCANON50@3:bv256
	LCANON51@3:bv256
	LCANON52@3:bv256
	LCANON53@3:bv256
	LCANON54@3:bv256
	LCANON55@3:bv256
	LCANON56@3:bv256
	LCANON57@3:bv256
	LCANON58@3:bv256
	LCANON59@3:bv256
	LCANON60@3:bv256
	LCANON61@3:bv256
	tacContractAtCANON0:bv256
	lastHasThrown:bool
	lastHasThrown@1:bool
	lastHasThrown@2:bool
	lastHasThrown@3:bool
	tacCaller!!89:bv256
	CANON0:bool
	CANON1:bool
	CANON2:bool
	CANON3:bv256
	CANON4:bool
	CANON5:bool
	CANON6:int
	CANON7:int
	CANON8:int
	CANON9:int
	tacSCANON0:wordmap
	tacBalance!!122:wordmap
	tacTimestamp@3:bv256
	tacSighash!!11:bv256
	tacSighash!!12:bv256
	tacSighash!!13:bv256
	tacSighash@1:bv256
	tacSighash@2:bv256
	tacSighash@3:bv256
	tacNumber!!105:bv256
}
Program {
	Block 0_0_0_0_0_0 Succ [0_0_0_1_0_0] {
		AssignHavocCmd tacExtcodesize!!0:0
		AssignHavocCmd tacBalance!!3:1
		AssignHavocCmd CANON10:2
		AssignHavocCmd CANON11:3
		AssignHavocCmd CANON12:4
		AssignHavocCmd CANON13:5
		AssignHavocCmd CANON14:6
		AssignHavocCmd CANON15:7
		AssignHavocCmd CANON26!!4:8
		AssignHavocCmd R9:9
		AssignHavocCmd CANON6:10
		AssignHavocCmd CANON7:11
		AssignHavocCmd CANON8:12
		AssignHavocCmd CANON9:13
		AssignHavocCmd tacSighash!!11:14
		AssignHavocCmd tacSighash!!12:14
		AssignHavocCmd tacSighash!!13:14
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
		AssignExpCmd B14:15 Gt(Select(tacExtcodesize!!0:0 Apply(to_skey:bif R9:9) ) 0x0 )
		AssumeCmd B14:15
		AnnotationCmd JSON{"key":{"name":"cvl.label.end","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		AnnotationCmd JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Message","s":"assumptions about contracts' addresses"}}
		NopCmd
		AssumeExpCmd Gt(R9:9 0x0 )
		NopCmd
		AssumeExpCmd Le(R9:9 0xffffffffffffffffffffffffffffffffffffffff )
		AnnotationCmd JSON{"key":{"name":"cvl.label.end","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		AnnotationCmd JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Message","s":"assumptions about starting balances"}}
		AssignExpCmd R17:15 Select(tacBalance!!3:1 Apply(to_skey:bif R9:9) )
		NopCmd
		AssumeExpCmd Ge(R17:15 0x0 )
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
		AssumeExpCmd LAnd(Le(CANON6:10 0xffffffffffffffffffffffffffffffffffffffff ) Ge(CANON6:10 0x0 ) )
		NopCmd
		AssumeExpCmd LAnd(Le(CANON7:11 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff ) Ge(CANON7:11 0x0 ) )
		NopCmd
		AssumeExpCmd LAnd(Le(CANON8:12 0xffffffffffffffffffffffffffffffffffffffff ) Ge(CANON8:12 0x0 ) )
		NopCmd
		AssumeExpCmd LAnd(Le(CANON9:13 0xffffffffffffffffffffffffffffffffffffffff ) Ge(CANON9:13 0x0 ) )
		NopCmd
		AssumeExpCmd LAnd(Le(CANON10:2 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff ) Ge(CANON10:2 0x0 ) )
		NopCmd
		AssumeExpCmd LAnd(Le(CANON11:3 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff ) Ge(CANON11:3 0x0 ) )
		NopCmd
		AssumeExpCmd LAnd(Le(CANON12:4 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff ) Ge(CANON12:4 0x0 ) )
		NopCmd
		AssumeExpCmd LAnd(Le(CANON13:5 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff ) Ge(CANON13:5 0x0 ) )
		NopCmd
		AssumeExpCmd LAnd(Le(CANON14:6 0xffffffffffffffffffffffffffffffffffffffff ) Ge(CANON14:6 0x0 ) )
		NopCmd
		AssumeExpCmd LAnd(Le(CANON15:7 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff ) Ge(CANON15:7 0x0 ) )
		AnnotationCmd:16 JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Cmd","cmd":{"cmd_type":"spec.cvlast.CVLCmd.Simple.AssumeCmd.Assume","cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/spec/ERC20.spec","start":{"line":64,"character":4},"end":{"line":64,"character":45}},"exp":{"#class":"spec.cvlast.CVLExp.RelopExp.ArithRelopExp.GtExp","l":{"#class":"spec.cvlast.CVLExp.ApplyExp.ContractFunction.Concrete","methodIdWithCallContext":{"#class":"spec.cvlast.ConcreteMethod","signature":{"#class":"spec.cvlast.ExternalQualifiedMethodSignature.ExternalQualifiedMethodSig","wrapped":{"#class":"spec.cvlast.QualifiedMethodSignature.QualifiedMethodSig","qualifiedMethodName":{"#class":"spec.cvlast.QualifiedFunction","host":{"name":"ERC20"},"methodId":"balanceOf"},"params":[{"#class":"spec.cvlast.VMParam.Named","name":"account","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$address"}}],"res":[{"#class":"spec.cvlast.VMParam.Unnamed","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256}}]},"sighashInt":{"n":"70a08231"}}},"args":[{"#class":"spec.cvlast.CVLExp.FieldSelectExp","structExp":{"#class":"spec.cvlast.CVLExp.FieldSelectExp","structExp":{"#class":"spec.cvlast.CVLExp.VariableExp","id":"e","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":2}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"env","fields":[{"fieldName":"msg","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"msg","fields":[{"fieldName":"sender","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"value","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}}]}},{"fieldName":"tx","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"tx","fields":[{"fieldName":"origin","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}}]}},{"fieldName":"block","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"block","fields":[{"fieldName":"coinbase","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"difficulty","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"gaslimit","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"number","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"timestamp","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}}]}}]},"cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/spec/ERC20.spec","start":{"line":64,"character":4},"end":{"line":64,"character":45}}},"twoStateIndex":"NEITHER"},"fieldName":"msg","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":2}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"msg","fields":[{"fieldName":"sender","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"value","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}}]},"cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/spec/ERC20.spec","start":{"line":64,"character":22},"end":{"line":64,"character":23}}}},"fieldName":"sender","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":2}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"},"cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/spec/ERC20.spec","start":{"line":64,"character":22},"end":{"line":64,"character":23}}}}],"noRevert":true,"storage":{"#class":"spec.cvlast.CVLExp.VariableExp","id":"lastStorage","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":2}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.VMInternal.BlockchainState"},"cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/spec/ERC20.spec","start":{"line":64,"character":4},"end":{"line":64,"character":45}}},"twoStateIndex":"NEITHER"},"isWhole":false,"tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":2}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.VM","descriptor":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256},"context":{"#class":"spec.cvlast.typedescriptors.FromVMContext.ReturnValue"}},"cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/spec/ERC20.spec","start":{"line":64,"character":12},"end":{"line":64,"character":21}},"annotation":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.CallResolution$DirectPassing","target":{"methodSignature":{"#class":"spec.cvlast.ExternalQualifiedMethodSignature.ExternalQualifiedMethodSig","wrapped":{"#class":"spec.cvlast.QualifiedMethodSignature.QualifiedMethodSig","qualifiedMethodName":{"#class":"spec.cvlast.QualifiedFunction","host":{"name":"ERC20"},"methodId":"balanceOf"},"params":[{"#class":"spec.cvlast.VMParam.Named","name":"account","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$address"}}],"res":[{"#class":"spec.cvlast.VMParam.Unnamed","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256}}]},"sighashInt":{"n":"70a08231"}},"definitelyNonPayable":true,"annotation":{"visibility":"EXTERNAL","envFree":true,"library":false},"stateMutability":"view","tag":{"#class":"spec.cvlast.CVLImportedFunctionTag.WithMethodInfo","evmMethodInfo":{"sigHash":"70a08231","name":"balanceOf","argTypes":[{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.address"}],"resultTypes":[{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256}],"stateMutability":"view","envfreeInfo":{"#class":"bridge.EnvfreeInfo.Unknown"},"isConstant":false,"paramNames":["account"],"isLibrary":false}}},"hasEnv":false}}},"r":{"#class":"spec.cvlast.CVLExp.VariableExp","id":"amount","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":2}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256},"cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/spec/ERC20.spec","start":{"line":64,"character":4},"end":{"line":64,"character":45}}},"twoStateIndex":"NEITHER"},"tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":2}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"},"cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/spec/ERC20.spec","start":{"line":64,"character":12},"end":{"line":64,"character":44}}}},"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":2}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}}}}}
		NopCmd
	}
	Block 0_0_0_1_0_0 Succ [1_0_0_0_0_0] {
		AnnotationCmd:16 JSON{"key":{"name":"call.trace.push","type":"analysis.icfg.Inliner$CallStack$PushRecord","erasureStrategy":"Canonical"},"value":"rO0ABXNyACphbmFseXNpcy5pY2ZnLklubGluZXIkQ2FsbFN0YWNrJFB1c2hSZWNvcmSX8+DCTLCH+AIAA0kACGNhbGxlZUlkTAAGY2FsbGVldAATTHZjL2RhdGEvTWV0aG9kUmVmO0wAB3N1bW1hcnl0ABVMdmMvZGF0YS9DYWxsU3VtbWFyeTt4cAAAAAFzcgARdmMuZGF0YS5NZXRob2RSZWbJlJTzzU9pGAIAA0wABGF0dHJ0ABdMc2NlbmUvTWV0aG9kQXR0cmlidXRlO0wACmNvbnRyYWN0SWR0ABZMamF2YS9tYXRoL0JpZ0ludGVnZXI7TAAHc2lnSGFzaHQAEExldm0vU2lnaGFzaEludDt4cHNyABxzY2VuZS5NZXRob2RBdHRyaWJ1dGUkQ29tbW9uNHjdebdr9XMCAAB4cgAVc2NlbmUuTWV0aG9kQXR0cmlidXRlcYg2pYWutuUCAAB4cHNyABRqYXZhLm1hdGguQmlnSW50ZWdlcoz8nx+pO/sdAwAGSQAIYml0Q291bnRJAAliaXRMZW5ndGhJABNmaXJzdE5vbnplcm9CeXRlTnVtSQAMbG93ZXN0U2V0Qml0SQAGc2lnbnVtWwAJbWFnbml0dWRldAACW0J4cgAQamF2YS5sYW5nLk51bWJlcoaslR0LlOCLAgAAeHD///////////////7////+AAAAAXVyAAJbQqzzF/gGCFTgAgAAeHAAAAAQzkYEoAAAAAAAAAAAAAAAA3hzcgAOZXZtLlNpZ2hhc2hJbnRUdcqNMXEgeAIAAUwAAW5xAH4ABnhwc3EAfgAM///////////////+/////gAAAAF1cQB+ABAAAAAEcKCCMXhw"}
		AssignHavocCmd:16 tacCalldatasize!!31:17
		NopCmd
		AssumeExpCmd Apply(add_noofl:bif 0x4 0x20)
		NopCmd
		AssumeExpCmd Apply(add_noofl:bif 0x4 0x0)
		AssignExpCmd:16 B34 LAnd(Ge(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff CANON6:10 ) Le(0x0 CANON6:10 ) )
		AssertCmd:16 B34 "sanity bounds check on cvl to vm encoding of certoraArg25392540:int failed"
		AssignExpCmd:16 R35 Apply(safe_math_narrow:bif CANON6:10)
		NopCmd
		AssumeExpCmd Eq(0x24 tacCalldatasize!!31:17 )
		LabelCmd:16 "Start procedure ERC20-balanceOf(address)"
		AnnotationCmd:16 JSON{"key":{"name":"fps.free-pointer-is-scalarized","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true}
		AssignExpCmd:16 R38:15 Select(tacExtcodesize!!0:0 Apply(to_skey:bif R9:18) )
		NopCmd
		AssumeExpCmd Gt(R38:15 0x0 )
		AnnotationCmd:16 JSON{"key":{"name":"internal.func.finder.info","type":"analysis.ip.InternalFunctionFinderReport","erasureStrategy":"Erased"},"value":"rO0ABXNyAChhbmFseXNpcy5pcC5JbnRlcm5hbEZ1bmN0aW9uRmluZGVyUmVwb3J0ian+bYn1VdACAAFMABN1bnJlc29sdmVkRnVuY3Rpb25zdAAPTGphdmEvdXRpbC9TZXQ7eHBzcgAhZGF0YXN0cnVjdHVyZXMuTGlua2VkQXJyYXlIYXNoU2V0AAAAAAAAAAEDAAJGAApsb2FkRmFjdG9yTAAJaGFzaFRhYmxldAAuTGRhdGFzdHJ1Y3R1cmVzL2FycmF5aGFzaHRhYmxlL0FycmF5SGFzaFRhYmxlO3hwdwgAAAAAQAAAAHg="}
		AnnotationCmd:16 JSON{"key":{"name":"fps.free-pointer-is-scalarized","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true}
		NopCmd
		AssumeExpCmd LNot(Lt(tacCalldatasize!!31:17 0x4 ) )
		NopCmd
		AssumeExpCmd LNot(Gt(0x70a08231 tacSighash!!11:14 ) )
		NopCmd
		AssumeExpCmd Gt(0xa9059cbb tacSighash!!11:14 )
		NopCmd
		AssumeExpCmd Eq(0x70a08231 tacSighash!!11:14 )
		AssumeCmd:19 true
		AssignExpCmd:20 R44:21 Sub(tacCalldatasize!!31:17 0x4 )
		NopCmd
		AssumeExpCmd LNot(Slt(R44:21 0x20 ) )
		NopCmd
		AssumeExpCmd Le(R35 0xffffffffffffffffffffffffffffffffffffffff )
		AnnotationCmd:16 JSON{"key":{"name":"internal.func.start","type":"analysis.ip.InternalFuncStartAnnotation","erasureStrategy":"CallTrace"},"value":{"id":0,"startPc":3130,"args":[{"s":{"namePrefix":"R35","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1013}]},"offset":1,"sort":"SCALAR"}],"methodSignature":{"#class":"spec.cvlast.QualifiedMethodSignature.QualifiedMethodSig","qualifiedMethodName":{"#class":"spec.cvlast.QualifiedFunction","host":{"name":"ERC20"},"methodId":"balanceOf"},"params":[{"#class":"spec.cvlast.VMParam.Named","name":"account","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$address"}}],"res":[{"#class":"spec.cvlast.VMParam.Unnamed","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256}}]},"stackOffsetToArgPos":{"1":0},"callSiteSrc":{"source":0,"begin":4328,"len":511,"jumpType":"ENTER","address":"ce4604a0000000000000000000000003","sourceContext":{"indexToFilepath":{"0":"contracts/ERC20.sol","1":"contracts/IERC20.sol","2":"contracts/IERC20Metadata.sol"},"sourceDir":".post_autofinders.0"}}}}
		AssignExpCmd:22 R50:23 Apply(hash_3_keccak:bif Apply(skey_basic:bif 0x40) Apply(to_skey:bif R35:24) Apply(skey_basic:bif 0x0))
		AssignExpCmd:25 R51:23 Select(CANON26!!4:8 R50:26 )
		AnnotationCmd:16 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet","value":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R51","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1020}]},"displayPath":{"#class":"analysis.storage.DisplayPath.MapAccess","key":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R35","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1018}]},"keyTyp":{"#class":"tac.TACStorageType.IntegralType","typeLabel":"address","numBytes":"14","descriptor":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$address"},"lowerBound":null,"upperBound":null},"base":{"#class":"analysis.storage.DisplayPath.Root","name":"_balances"}},"storageType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256},"contractInstance":"ce4604a0000000000000000000000003","linkableStorageReadId":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet.None"}}}
		AnnotationCmd:16 JSON{"key":{"name":"internal.func.end","type":"analysis.ip.InternalFuncExitAnnotation","erasureStrategy":"Canonical"},"value":{"id":0,"rets":[{"s":{"namePrefix":"R51","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1023}]},"offset":0}],"functionLayout":{"0":{"#class":"analysis.ip.InternalFuncValueLocation.Scalar"}}}}
		AnnotationCmd:16 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.EVMFunctionReturnWrite","returnbufOffset":"0","returnValueSym":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R51","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1023}]},"callIndex":1}}
		AnnotationCmd:16 JSON{"key":{"name":"tac.return.path","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		LabelCmd:16 "End procedure ERC20-balanceOf(address)"
		NopCmd
		AnnotationCmd:16 JSON{"key":{"name":"call.trace.pop","type":"analysis.icfg.Inliner$CallStack$PopRecord","erasureStrategy":"Canonical"},"value":"rO0ABXNyAClhbmFseXNpcy5pY2ZnLklubGluZXIkQ2FsbFN0YWNrJFBvcFJlY29yZPAPfwSLdCWJAgABSQAIY2FsbGVlSWR4cAAAAAE="}
	}
	Block 0_0_0_2_0_0 Succ [2_0_0_0_0_0] {
		AnnotationCmd:27 JSON{"key":{"name":"call.trace.push","type":"analysis.icfg.Inliner$CallStack$PushRecord","erasureStrategy":"Canonical"},"value":"rO0ABXNyACphbmFseXNpcy5pY2ZnLklubGluZXIkQ2FsbFN0YWNrJFB1c2hSZWNvcmSX8+DCTLCH+AIAA0kACGNhbGxlZUlkTAAGY2FsbGVldAATTHZjL2RhdGEvTWV0aG9kUmVmO0wAB3N1bW1hcnl0ABVMdmMvZGF0YS9DYWxsU3VtbWFyeTt4cAAAAAJzcgARdmMuZGF0YS5NZXRob2RSZWbJlJTzzU9pGAIAA0wABGF0dHJ0ABdMc2NlbmUvTWV0aG9kQXR0cmlidXRlO0wACmNvbnRyYWN0SWR0ABZMamF2YS9tYXRoL0JpZ0ludGVnZXI7TAAHc2lnSGFzaHQAEExldm0vU2lnaGFzaEludDt4cHNyABxzY2VuZS5NZXRob2RBdHRyaWJ1dGUkQ29tbW9uNHjdebdr9XMCAAB4cgAVc2NlbmUuTWV0aG9kQXR0cmlidXRlcYg2pYWutuUCAAB4cHNyABRqYXZhLm1hdGguQmlnSW50ZWdlcoz8nx+pO/sdAwAGSQAIYml0Q291bnRJAAliaXRMZW5ndGhJABNmaXJzdE5vbnplcm9CeXRlTnVtSQAMbG93ZXN0U2V0Qml0SQAGc2lnbnVtWwAJbWFnbml0dWRldAACW0J4cgAQamF2YS5sYW5nLk51bWJlcoaslR0LlOCLAgAAeHD///////////////7////+AAAAAXVyAAJbQqzzF/gGCFTgAgAAeHAAAAAQzkYEoAAAAAAAAAAAAAAAA3hzcgAOZXZtLlNpZ2hhc2hJbnRUdcqNMXEgeAIAAUwAAW5xAH4ABnhwc3EAfgAM///////////////+/////gAAAAF1cQB+ABAAAAAEcKCCMXhw"}
		AssignHavocCmd:27 tacCalldatasize!!54:17
		NopCmd
		AssumeExpCmd Apply(add_noofl:bif 0x4 0x20)
		NopCmd
		AssumeExpCmd Apply(add_noofl:bif 0x4 0x0)
		AssignExpCmd:27 B57 LAnd(Ge(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff I137 ) Le(0x0 I137 ) )
		AssertCmd:27 B57 "sanity bounds check on cvl to vm encoding of certoraArg25832584:int failed"
		AssignExpCmd:27 R58 Apply(safe_math_narrow:bif I137)
		NopCmd
		AssumeExpCmd Eq(0x24 tacCalldatasize!!54:17 )
		LabelCmd:27 "Start procedure ERC20-balanceOf(address)"
		AnnotationCmd:27 JSON{"key":{"name":"fps.free-pointer-is-scalarized","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true}
		AssignExpCmd:27 R61:15 Select(tacExtcodesize!!0:0 Apply(to_skey:bif R9:18) )
		NopCmd
		AssumeExpCmd Gt(R61:15 0x0 )
		AnnotationCmd:27 JSON{"key":{"name":"internal.func.finder.info","type":"analysis.ip.InternalFunctionFinderReport","erasureStrategy":"Erased"},"value":"rO0ABXNyAChhbmFseXNpcy5pcC5JbnRlcm5hbEZ1bmN0aW9uRmluZGVyUmVwb3J0ian+bYn1VdACAAFMABN1bnJlc29sdmVkRnVuY3Rpb25zdAAPTGphdmEvdXRpbC9TZXQ7eHBzcgAhZGF0YXN0cnVjdHVyZXMuTGlua2VkQXJyYXlIYXNoU2V0AAAAAAAAAAEDAAJGAApsb2FkRmFjdG9yTAAJaGFzaFRhYmxldAAuTGRhdGFzdHJ1Y3R1cmVzL2FycmF5aGFzaHRhYmxlL0FycmF5SGFzaFRhYmxlO3hwdwgAAAAAQAAAAHg="}
		AnnotationCmd:27 JSON{"key":{"name":"fps.free-pointer-is-scalarized","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true}
		NopCmd
		AssumeExpCmd LNot(Lt(tacCalldatasize!!54:17 0x4 ) )
		NopCmd
		AssumeExpCmd LNot(Gt(0x70a08231 tacSighash!!12:14 ) )
		NopCmd
		AssumeExpCmd Gt(0xa9059cbb tacSighash!!12:14 )
		NopCmd
		AssumeExpCmd Eq(0x70a08231 tacSighash!!12:14 )
		AssumeCmd:28 true
		AssignExpCmd:29 R67:21 Sub(tacCalldatasize!!54:17 0x4 )
		NopCmd
		AssumeExpCmd LNot(Slt(R67:21 0x20 ) )
		NopCmd
		AssumeExpCmd Le(R58 0xffffffffffffffffffffffffffffffffffffffff )
		AnnotationCmd:27 JSON{"key":{"name":"internal.func.start","type":"analysis.ip.InternalFuncStartAnnotation","erasureStrategy":"CallTrace"},"value":{"id":1,"startPc":3130,"args":[{"s":{"namePrefix":"R58","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1013}]},"offset":1,"sort":"SCALAR"}],"methodSignature":{"#class":"spec.cvlast.QualifiedMethodSignature.QualifiedMethodSig","qualifiedMethodName":{"#class":"spec.cvlast.QualifiedFunction","host":{"name":"ERC20"},"methodId":"balanceOf"},"params":[{"#class":"spec.cvlast.VMParam.Named","name":"account","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$address"}}],"res":[{"#class":"spec.cvlast.VMParam.Unnamed","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256}}]},"stackOffsetToArgPos":{"1":0},"callSiteSrc":{"source":0,"begin":4328,"len":511,"jumpType":"ENTER","address":"ce4604a0000000000000000000000003","sourceContext":{"indexToFilepath":{"0":"contracts/ERC20.sol","1":"contracts/IERC20.sol","2":"contracts/IERC20Metadata.sol"},"sourceDir":".post_autofinders.0"}}}}
		AssignExpCmd:30 R73:23 Apply(hash_3_keccak:bif Apply(skey_basic:bif 0x40) Apply(to_skey:bif R58:24) Apply(skey_basic:bif 0x0))
		AssignExpCmd:31 R74:23 Select(CANON26!!4:8 R73:32 )
		AnnotationCmd:27 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet","value":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R74","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1020}]},"displayPath":{"#class":"analysis.storage.DisplayPath.MapAccess","key":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R58","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1018}]},"keyTyp":{"#class":"tac.TACStorageType.IntegralType","typeLabel":"address","numBytes":"14","descriptor":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$address"},"lowerBound":null,"upperBound":null},"base":{"#class":"analysis.storage.DisplayPath.Root","name":"_balances"}},"storageType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256},"contractInstance":"ce4604a0000000000000000000000003","linkableStorageReadId":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet.None"}}}
		AnnotationCmd:27 JSON{"key":{"name":"internal.func.end","type":"analysis.ip.InternalFuncExitAnnotation","erasureStrategy":"Canonical"},"value":{"id":1,"rets":[{"s":{"namePrefix":"R74","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1023}]},"offset":0}],"functionLayout":{"0":{"#class":"analysis.ip.InternalFuncValueLocation.Scalar"}}}}
		AnnotationCmd:27 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.EVMFunctionReturnWrite","returnbufOffset":"0","returnValueSym":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R74","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1023}]},"callIndex":2}}
		AnnotationCmd:27 JSON{"key":{"name":"tac.return.path","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		LabelCmd:27 "End procedure ERC20-balanceOf(address)"
		NopCmd
		AnnotationCmd:27 JSON{"key":{"name":"call.trace.pop","type":"analysis.icfg.Inliner$CallStack$PopRecord","erasureStrategy":"Canonical"},"value":"rO0ABXNyAClhbmFseXNpcy5pY2ZnLklubGluZXIkQ2FsbFN0YWNrJFBvcFJlY29yZPAPfwSLdCWJAgABSQAIY2FsbGVlSWR4cAAAAAI="}
	}
	Block 0_0_0_3_0_0 Succ [860_1023_0_3_2_0, 3_0_0_3_0_123] {
		AnnotationCmd JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageGlobalChangeSnippet.StorageTakeSnapshot","lhs":{"namePrefix":"CANON69","tag":{"#class":"tac.Tag.BlockchainState"},"callIndex":0}}}
		AnnotationCmd:33 JSON{"key":{"name":"call.trace.push","type":"analysis.icfg.Inliner$CallStack$PushRecord","erasureStrategy":"Canonical"},"value":"rO0ABXNyACphbmFseXNpcy5pY2ZnLklubGluZXIkQ2FsbFN0YWNrJFB1c2hSZWNvcmSX8+DCTLCH+AIAA0kACGNhbGxlZUlkTAAGY2FsbGVldAATTHZjL2RhdGEvTWV0aG9kUmVmO0wAB3N1bW1hcnl0ABVMdmMvZGF0YS9DYWxsU3VtbWFyeTt4cAAAAANzcgARdmMuZGF0YS5NZXRob2RSZWbJlJTzzU9pGAIAA0wABGF0dHJ0ABdMc2NlbmUvTWV0aG9kQXR0cmlidXRlO0wACmNvbnRyYWN0SWR0ABZMamF2YS9tYXRoL0JpZ0ludGVnZXI7TAAHc2lnSGFzaHQAEExldm0vU2lnaGFzaEludDt4cHNyABxzY2VuZS5NZXRob2RBdHRyaWJ1dGUkQ29tbW9uNHjdebdr9XMCAAB4cgAVc2NlbmUuTWV0aG9kQXR0cmlidXRlcYg2pYWutuUCAAB4cHNyABRqYXZhLm1hdGguQmlnSW50ZWdlcoz8nx+pO/sdAwAGSQAIYml0Q291bnRJAAliaXRMZW5ndGhJABNmaXJzdE5vbnplcm9CeXRlTnVtSQAMbG93ZXN0U2V0Qml0SQAGc2lnbnVtWwAJbWFnbml0dWRldAACW0J4cgAQamF2YS5sYW5nLk51bWJlcoaslR0LlOCLAgAAeHD///////////////7////+AAAAAXVyAAJbQqzzF/gGCFTgAgAAeHAAAAAQzkYEoAAAAAAAAAAAAAAAA3hzcgAOZXZtLlNpZ2hhc2hJbnRUdcqNMXEgeAIAAUwAAW5xAH4ABnhwc3EAfgAM///////////////+/////gAAAAF1cQB+ABAAAAAEqQWcu3hw"}
		AssignHavocCmd:33 tacCalldatasize!!77:17
		NopCmd
		AssumeExpCmd Apply(add_noofl:bif 0x4 0x40)
		NopCmd
		AssumeExpCmd Apply(add_noofl:bif 0x4 0x0)
		AssignExpCmd:33 B80 LAnd(Ge(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff I152 ) Le(0x0 I152 ) )
		AssertCmd:33 B80 "sanity bounds check on cvl to vm encoding of certoraArg26232624:int failed"
		AssignExpCmd:33 R81 Apply(safe_math_narrow:bif I152)
		AssignExpCmd:33 tacCalldatabufCANON0@3:34 R81
		NopCmd
		AssumeExpCmd Apply(add_noofl:bif 0x4 0x20)
		AssignExpCmd:33 B83 LAnd(Ge(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff I153 ) Le(0x0 I153 ) )
		AssertCmd:33 B83 "sanity bounds check on cvl to vm encoding of certoraArg26252626:int failed"
		AssignExpCmd:33 R84 Apply(safe_math_narrow:bif I153)
		AssignExpCmd:33 tacCalldatabufCANON1@3:35 R84
		NopCmd
		AssumeExpCmd Eq(0x44 tacCalldatasize!!77:17 )
		AssignExpCmd:33 B87 LAnd(Ge(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff CANON6:10 ) Le(0x0 CANON6:10 ) )
		AssertCmd:33 B87 "sanity bounds check on cvl to vm encoding of tacTmp!2634:int failed"
		AssignExpCmd:33 R88:15 Apply(safe_math_narrow:bif CANON6:10)
		NopCmd
		AssumeExpCmd LAnd(Le(R88:36 0xffffffffffffffffffffffffffffffffffffffff ) Ge(R88:36 0x0 ) )
		AssignExpCmd:33 B92 LAnd(Ge(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff CANON7:11 ) Le(0x0 CANON7:11 ) )
		AssertCmd:33 B92 "sanity bounds check on cvl to vm encoding of tacTmp!2637:int failed"
		AssignExpCmd:33 R93:15 Apply(safe_math_narrow:bif CANON7:11)
		NopCmd
		AssumeExpCmd LAnd(Le(R93:37 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff ) Ge(R93:37 0x0 ) )
		AssignExpCmd:33 B98 LAnd(Ge(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff CANON8:12 ) Le(0x0 CANON8:12 ) )
		AssertCmd:33 B98 "sanity bounds check on cvl to vm encoding of tacTmp!2641:int failed"
		AssignExpCmd:33 R99:15 Apply(safe_math_narrow:bif CANON8:12)
		NopCmd
		AssumeExpCmd LAnd(Le(R99:38 0xffffffffffffffffffffffffffffffffffffffff ) Ge(R99:38 0x0 ) )
		AssignExpCmd:33 B103 LAnd(Ge(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff CANON12:4 ) Le(0x0 CANON12:4 ) )
		AssertCmd:33 B103 "sanity bounds check on cvl to vm encoding of tacTmp!2644:int failed"
		AssignExpCmd:33 R104:15 Apply(safe_math_narrow:bif CANON12:4)
		NopCmd
		AssumeExpCmd LAnd(Le(R104:39 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff ) Ge(R104:39 0x0 ) )
		AssignExpCmd:33 B108 LAnd(Ge(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff CANON13:5 ) Le(0x0 CANON13:5 ) )
		AssertCmd:33 B108 "sanity bounds check on cvl to vm encoding of tacTmp!2647:int failed"
		AssignExpCmd:33 R109:15 Apply(safe_math_narrow:bif CANON13:5)
		NopCmd
		AssumeExpCmd LAnd(Le(R109:40 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff ) Ge(R109:40 0x0 ) )
		AssignExpCmd:33 B113 LAnd(Ge(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff CANON7:11 ) Le(0x0 CANON7:11 ) )
		AssertCmd:33 B113 "sanity bounds check on cvl to vm encoding of tacTmp!2650:int failed"
		AssignExpCmd:33 R114:15 Apply(safe_math_narrow:bif CANON7:11)
		AssignExpCmd:33 B116 LAnd(Ge(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff CANON6:10 ) Le(0x0 CANON6:10 ) )
		AssertCmd:33 B116 "sanity bounds check on cvl to vm encoding of tacTmp!2653:int failed"
		AssignExpCmd:33 R117:15 Apply(safe_math_narrow:bif CANON6:10)
		AssignExpCmd:33 R120:15 Select(tacBalance!!3:1 Apply(to_skey:bif R117:15) )
		AssignExpCmd:41 I121:15 IntSub(R120:15 R114:15 )
		AssignExpCmd:41 tacBalance!!122:1 Store(tacBalance!!3:1 Apply(to_skey:bif R117:15) I121:15 )
		AssignExpCmd:33 R123:15 Select(tacBalance!!122:1 Apply(to_skey:bif R9:9) )
		AssignExpCmd:41 R124:15 Add(R123:15 R114:15)
		NopCmd
		AssumeExpCmd Apply(add_noofl:bif R123:15 R114:15)
		AnnotationCmd:33 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.BalanceSnippet","srcAccountInfo":{"old":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R120","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}]},"new":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"I121","tag":{"#class":"tac.Tag.Int"},"callIndex":0,"meta":[{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}]},"addr":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R117","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}]}},"trgAccountInfo":{"old":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R123","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}]},"new":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R124","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}]},"addr":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R9","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"tacContractAt"},{"key":{"name":"tac.contract.sym.addr.name","type":"java.lang.String","erasureStrategy":"Erased"},"value":"ERC20"},{"key":{"name":"tac.contract.sym.addr","type":"java.math.BigInteger","erasureStrategy":"Erased"},"value":"ce4604a0000000000000000000000003"}]}},"transferredAmount":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R114","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}]}}}
		LabelCmd:33 "Start procedure ERC20-transfer(address,uint256)"
		AnnotationCmd:33 JSON{"key":{"name":"fps.free-pointer-is-scalarized","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true}
		AssignExpCmd:33 R126:15 Select(tacExtcodesize!!0:0 Apply(to_skey:bif R9:18) )
		NopCmd
		AssumeExpCmd Gt(R126:15 0x0 )
		AnnotationCmd:33 JSON{"key":{"name":"internal.func.finder.info","type":"analysis.ip.InternalFunctionFinderReport","erasureStrategy":"Erased"},"value":"rO0ABXNyAChhbmFseXNpcy5pcC5JbnRlcm5hbEZ1bmN0aW9uRmluZGVyUmVwb3J0ian+bYn1VdACAAFMABN1bnJlc29sdmVkRnVuY3Rpb25zdAAPTGphdmEvdXRpbC9TZXQ7eHBzcgAhZGF0YXN0cnVjdHVyZXMuTGlua2VkQXJyYXlIYXNoU2V0AAAAAAAAAAEDAAJGAApsb2FkRmFjdG9yTAAJaGFzaFRhYmxldAAuTGRhdGFzdHJ1Y3R1cmVzL2FycmF5aGFzaHRhYmxlL0FycmF5SGFzaFRhYmxlO3hwdwgAAAAAQAAAAHg="}
		AnnotationCmd:33 JSON{"key":{"name":"fps.free-pointer-is-scalarized","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true}
		NopCmd
		AssumeExpCmd LNot(Lt(tacCalldatasize!!77:17 0x4 ) )
		NopCmd
		AssumeExpCmd LNot(Gt(0x70a08231 tacSighash!!13:14 ) )
		NopCmd
		AssumeExpCmd LNot(Gt(0xa9059cbb tacSighash!!13:14 ) )
		NopCmd
		AssumeExpCmd Eq(0xa9059cbb tacSighash!!13:14 )
		AssignExpCmd:33 B132:42 Eq(R93:15 0x0 )
		JumpiCmd:43 860_1023_0_3_2_0 3_0_0_3_0_123 B132:42
	}
	Block 1_0_0_0_0_0 Succ [0_0_0_2_0_0] {
		AssumeNotCmd:16 false
		AssumeNotCmd:16 false
		AnnotationCmd JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageGlobalChangeSnippet.StorageTakeSnapshot","lhs":{"namePrefix":"lastStorage","tag":{"#class":"tac.Tag.BlockchainState"},"callIndex":0,"meta":[{"key":{"name":"cvl.local","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true},{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"lastStorage"},{"key":{"name":"cvl.type","type":"spec.cvlast.CVLType$PureCVLType","erasureStrategy":"CallTrace"},"value":{"#class":"spec.cvlast.CVLType.PureCVLType.VMInternal.BlockchainState"}},{"key":{"name":"cvl","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true},{"key":{"name":"cvl.display","type":"java.lang.String","erasureStrategy":"CallTrace"},"value":"lastStorage"}]}}}
		AssignExpCmd:44 I133 CANON15:7
		AssignExpCmd:45 B134 Gt(R51:23 I133 )
		AssumeCmd:16 B134
		AnnotationCmd:16 JSON{"key":{"name":"cvl.label.end","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		AnnotationCmd:46 JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Cmd","cmd":{"cmd_type":"spec.cvlast.CVLCmd.Simple.AssumeCmd.Assume","cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/spec/ERC20.spec","start":{"line":65,"character":4},"end":{"line":65,"character":29}},"exp":{"#class":"spec.cvlast.CVLExp.RelopExp.EqExp","l":{"#class":"spec.cvlast.CVLExp.FieldSelectExp","structExp":{"#class":"spec.cvlast.CVLExp.FieldSelectExp","structExp":{"#class":"spec.cvlast.CVLExp.VariableExp","id":"e","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":2}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"env","fields":[{"fieldName":"msg","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"msg","fields":[{"fieldName":"sender","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"value","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}}]}},{"fieldName":"tx","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"tx","fields":[{"fieldName":"origin","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}}]}},{"fieldName":"block","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"block","fields":[{"fieldName":"coinbase","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"difficulty","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"gaslimit","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"number","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"timestamp","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}}]}}]},"cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/spec/ERC20.spec","start":{"line":65,"character":4},"end":{"line":65,"character":29}}},"twoStateIndex":"NEITHER"},"fieldName":"msg","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":2}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"msg","fields":[{"fieldName":"sender","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"value","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}}]},"cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/spec/ERC20.spec","start":{"line":65,"character":12},"end":{"line":65,"character":13}}}},"fieldName":"value","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":2}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256},"cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/spec/ERC20.spec","start":{"line":65,"character":12},"end":{"line":65,"character":13}}}},"r":{"#class":"spec.cvlast.CVLExp.Constant.NumberLit","n":"0","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":2}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.NumberLiteral","n":"0"},"cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/spec/ERC20.spec","start":{"line":65,"character":27},"end":{"line":65,"character":28}}}},"tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":2}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"},"cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/spec/ERC20.spec","start":{"line":65,"character":12},"end":{"line":65,"character":28}}}},"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":2}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}}}}}
		NopCmd
		AssignExpCmd:47 CANON33!!136:48 Eq(CANON7:11 0x0 )
		AssumeCmd:46 CANON33!!136:48
		AnnotationCmd:46 JSON{"key":{"name":"cvl.label.end","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		AnnotationCmd:27 JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Cmd","cmd":{"cmd_type":"spec.cvlast.CVLCmd.Simple.AssumeCmd.Assume","cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/spec/ERC20.spec","start":{"line":66,"character":4},"end":{"line":66,"character":53}},"exp":{"#class":"spec.cvlast.CVLExp.RelopExp.ArithRelopExp.LtExp","l":{"#class":"spec.cvlast.CVLExp.BinaryExp.AddExp","l":{"#class":"spec.cvlast.CVLExp.ApplyExp.ContractFunction.Concrete","methodIdWithCallContext":{"#class":"spec.cvlast.ConcreteMethod","signature":{"#class":"spec.cvlast.ExternalQualifiedMethodSignature.ExternalQualifiedMethodSig","wrapped":{"#class":"spec.cvlast.QualifiedMethodSignature.QualifiedMethodSig","qualifiedMethodName":{"#class":"spec.cvlast.QualifiedFunction","host":{"name":"ERC20"},"methodId":"balanceOf"},"params":[{"#class":"spec.cvlast.VMParam.Named","name":"account","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$address"}}],"res":[{"#class":"spec.cvlast.VMParam.Unnamed","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256}}]},"sighashInt":{"n":"70a08231"}}},"args":[{"#class":"spec.cvlast.CVLExp.VariableExp","id":"recipient","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":2}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"},"cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/spec/ERC20.spec","start":{"line":66,"character":4},"end":{"line":66,"character":53}}},"twoStateIndex":"NEITHER"}],"noRevert":true,"storage":{"#class":"spec.cvlast.CVLExp.VariableExp","id":"lastStorage","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":2}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.VMInternal.BlockchainState"},"cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/spec/ERC20.spec","start":{"line":66,"character":4},"end":{"line":66,"character":53}}},"twoStateIndex":"NEITHER"},"isWhole":false,"tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":2}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.VM","descriptor":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256},"context":{"#class":"spec.cvlast.typedescriptors.FromVMContext.ReturnValue"}},"cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/spec/ERC20.spec","start":{"line":66,"character":12},"end":{"line":66,"character":21}},"annotation":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.CallResolution$DirectPassing","target":{"methodSignature":{"#class":"spec.cvlast.ExternalQualifiedMethodSignature.ExternalQualifiedMethodSig","wrapped":{"#class":"spec.cvlast.QualifiedMethodSignature.QualifiedMethodSig","qualifiedMethodName":{"#class":"spec.cvlast.QualifiedFunction","host":{"name":"ERC20"},"methodId":"balanceOf"},"params":[{"#class":"spec.cvlast.VMParam.Named","name":"account","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$address"}}],"res":[{"#class":"spec.cvlast.VMParam.Unnamed","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256}}]},"sighashInt":{"n":"70a08231"}},"definitelyNonPayable":true,"annotation":{"visibility":"EXTERNAL","envFree":true,"library":false},"stateMutability":"view","tag":{"#class":"spec.cvlast.CVLImportedFunctionTag.WithMethodInfo","evmMethodInfo":{"sigHash":"70a08231","name":"balanceOf","argTypes":[{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.address"}],"resultTypes":[{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256}],"stateMutability":"view","envfreeInfo":{"#class":"bridge.EnvfreeInfo.Unknown"},"isConstant":false,"paramNames":["account"],"isLibrary":false}}},"hasEnv":false}}},"r":{"#class":"spec.cvlast.CVLExp.VariableExp","id":"amount","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":2}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256},"cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/spec/ERC20.spec","start":{"line":66,"character":4},"end":{"line":66,"character":53}}},"twoStateIndex":"NEITHER"},"tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":2}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Mathint"},"cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/spec/ERC20.spec","start":{"line":66,"character":12},"end":{"line":66,"character":41}}}},"r":{"#class":"spec.cvlast.CVLExp.Constant.NumberLit","n":"ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":2}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.NumberLiteral","n":"ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff"},"cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/spec/ERC20.spec","start":{"line":66,"character":44},"end":{"line":66,"character":52}}}},"tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":2}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"},"cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/spec/ERC20.spec","start":{"line":66,"character":12},"end":{"line":66,"character":52}}}},"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":2}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}}}}}
		AssignExpCmd:49 I137 CANON14:6
	}
	Block 2_0_0_0_0_0 Succ [0_0_0_3_0_0] {
		AssumeNotCmd:27 false
		AssumeNotCmd:27 false
		AnnotationCmd JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageGlobalChangeSnippet.StorageTakeSnapshot","lhs":{"namePrefix":"lastStorage","tag":{"#class":"tac.Tag.BlockchainState"},"callIndex":0,"meta":[{"key":{"name":"cvl.local","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true},{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"lastStorage"},{"key":{"name":"cvl.type","type":"spec.cvlast.CVLType$PureCVLType","erasureStrategy":"CallTrace"},"value":{"#class":"spec.cvlast.CVLType.PureCVLType.VMInternal.BlockchainState"}},{"key":{"name":"cvl","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true},{"key":{"name":"cvl.display","type":"java.lang.String","erasureStrategy":"CallTrace"},"value":"lastStorage"}]}}}
		AssignExpCmd:50 I138 CANON15:7
		AssignExpCmd:51 I139 IntAdd(R74:23 I138)
		AssignExpCmd:52 B140 Lt(I139 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff )
		AssumeCmd:27 B140
		AnnotationCmd:27 JSON{"key":{"name":"cvl.label.end","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		AnnotationCmd:53 JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Cmd","cmd":{"cmd_type":"spec.cvlast.CVLCmd.Simple.AssumeCmd.Assume","cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/spec/ERC20.spec","start":{"line":67,"character":4},"end":{"line":67,"character":30}},"exp":{"#class":"spec.cvlast.CVLExp.RelopExp.NeExp","l":{"#class":"spec.cvlast.CVLExp.FieldSelectExp","structExp":{"#class":"spec.cvlast.CVLExp.FieldSelectExp","structExp":{"#class":"spec.cvlast.CVLExp.VariableExp","id":"e","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":2}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"env","fields":[{"fieldName":"msg","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"msg","fields":[{"fieldName":"sender","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"value","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}}]}},{"fieldName":"tx","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"tx","fields":[{"fieldName":"origin","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}}]}},{"fieldName":"block","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"block","fields":[{"fieldName":"coinbase","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"difficulty","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"gaslimit","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"number","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"timestamp","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}}]}}]},"cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/spec/ERC20.spec","start":{"line":67,"character":4},"end":{"line":67,"character":30}}},"twoStateIndex":"NEITHER"},"fieldName":"msg","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":2}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"msg","fields":[{"fieldName":"sender","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"value","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}}]},"cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/spec/ERC20.spec","start":{"line":67,"character":12},"end":{"line":67,"character":13}}}},"fieldName":"sender","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":2}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"},"cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/spec/ERC20.spec","start":{"line":67,"character":12},"end":{"line":67,"character":13}}}},"r":{"#class":"spec.cvlast.CVLExp.Constant.NumberLit","n":"0","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":2}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.NumberLiteral","n":"0"},"cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/spec/ERC20.spec","start":{"line":67,"character":28},"end":{"line":67,"character":29}}}},"tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":2}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"},"cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/spec/ERC20.spec","start":{"line":67,"character":12},"end":{"line":67,"character":29}}}},"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":2}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}}}}}
		NopCmd
		AssignExpCmd:54 CANON47!!142:48 Eq(CANON6:10 0x0 )
		AssignExpCmd:55 B143 LNot(CANON47!!142:48 )
		AssumeCmd:53 B143
		AnnotationCmd:53 JSON{"key":{"name":"cvl.label.end","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		AnnotationCmd:56 JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Cmd","cmd":{"cmd_type":"spec.cvlast.CVLCmd.Simple.AssumeCmd.Assume","cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/spec/ERC20.spec","start":{"line":68,"character":4},"end":{"line":68,"character":27}},"exp":{"#class":"spec.cvlast.CVLExp.RelopExp.NeExp","l":{"#class":"spec.cvlast.CVLExp.VariableExp","id":"recipient","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":2}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"},"cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/spec/ERC20.spec","start":{"line":68,"character":4},"end":{"line":68,"character":27}}},"twoStateIndex":"NEITHER"},"r":{"#class":"spec.cvlast.CVLExp.Constant.NumberLit","n":"0","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":2}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.NumberLiteral","n":"0"},"cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/spec/ERC20.spec","start":{"line":68,"character":25},"end":{"line":68,"character":26}}}},"tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":2}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"},"cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/spec/ERC20.spec","start":{"line":68,"character":12},"end":{"line":68,"character":26}}}},"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":2}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}}}}}
		AssignExpCmd:57 I144 CANON14:6
		AssignExpCmd:58 CANON51!!145:48 Eq(I144 0x0 )
		AssignExpCmd:59 B146 LNot(CANON51!!145:48 )
		AssumeCmd:56 B146
		AnnotationCmd:56 JSON{"key":{"name":"cvl.label.end","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		AnnotationCmd:33 JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Cmd","cmd":{"cmd_type":"spec.cvlast.CVLCmd.Simple.Apply","cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/spec/ERC20.spec","start":{"line":70,"character":4},"end":{"line":70,"character":46}},"exp":{"#class":"spec.cvlast.CVLExp.ApplyExp.ContractFunction.Concrete","methodIdWithCallContext":{"#class":"spec.cvlast.ConcreteMethod","signature":{"#class":"spec.cvlast.ExternalQualifiedMethodSignature.ExternalQualifiedMethodSig","wrapped":{"#class":"spec.cvlast.QualifiedMethodSignature.QualifiedMethodSig","qualifiedMethodName":{"#class":"spec.cvlast.QualifiedFunction","host":{"name":"ERC20"},"methodId":"transfer"},"params":[{"#class":"spec.cvlast.VMParam.Named","name":"recipient","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$address"}},{"#class":"spec.cvlast.VMParam.Named","name":"amount","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256}}],"res":[{"#class":"spec.cvlast.VMParam.Unnamed","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$bool"}}]},"sighashInt":{"n":"a9059cbb"}}},"args":[{"#class":"spec.cvlast.CVLExp.VariableExp","id":"e","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":2}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"env","fields":[{"fieldName":"msg","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"msg","fields":[{"fieldName":"sender","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"value","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}}]}},{"fieldName":"tx","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"tx","fields":[{"fieldName":"origin","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}}]}},{"fieldName":"block","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"block","fields":[{"fieldName":"coinbase","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"difficulty","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"gaslimit","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"number","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"timestamp","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}}]}}]},"cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/spec/ERC20.spec","start":{"line":70,"character":4},"end":{"line":70,"character":46}}},"twoStateIndex":"NEITHER"},{"#class":"spec.cvlast.CVLExp.VariableExp","id":"recipient","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":2}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"},"cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/spec/ERC20.spec","start":{"line":70,"character":4},"end":{"line":70,"character":46}}},"twoStateIndex":"NEITHER"},{"#class":"spec.cvlast.CVLExp.VariableExp","id":"amount","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":2}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256},"cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/spec/ERC20.spec","start":{"line":70,"character":4},"end":{"line":70,"character":46}}},"twoStateIndex":"NEITHER"}],"noRevert":false,"storage":{"#class":"spec.cvlast.CVLExp.VariableExp","id":"lastStorage","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":2}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.VMInternal.BlockchainState"},"cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/spec/ERC20.spec","start":{"line":70,"character":4},"end":{"line":70,"character":46}}},"twoStateIndex":"NEITHER"},"isWhole":false,"tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":2}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.VM","descriptor":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$bool"},"context":{"#class":"spec.cvlast.typedescriptors.FromVMContext.ReturnValue"}},"cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/spec/ERC20.spec","start":{"line":70,"character":4},"end":{"line":70,"character":12}},"annotation":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.CallResolution$DirectPassing","target":{"methodSignature":{"#class":"spec.cvlast.ExternalQualifiedMethodSignature.ExternalQualifiedMethodSig","wrapped":{"#class":"spec.cvlast.QualifiedMethodSignature.QualifiedMethodSig","qualifiedMethodName":{"#class":"spec.cvlast.QualifiedFunction","host":{"name":"ERC20"},"methodId":"transfer"},"params":[{"#class":"spec.cvlast.VMParam.Named","name":"recipient","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$address"}},{"#class":"spec.cvlast.VMParam.Named","name":"amount","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256}}],"res":[{"#class":"spec.cvlast.VMParam.Unnamed","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$bool"}}]},"sighashInt":{"n":"a9059cbb"}},"definitelyNonPayable":true,"annotation":{"visibility":"EXTERNAL","envFree":false,"library":false},"stateMutability":"nonpayable","tag":{"#class":"spec.cvlast.CVLImportedFunctionTag.WithMethodInfo","evmMethodInfo":{"sigHash":"a9059cbb","name":"transfer","argTypes":[{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.address"},{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256}],"resultTypes":[{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.bool"}],"stateMutability":"nonpayable","envfreeInfo":{"#class":"bridge.EnvfreeInfo.Unknown"},"isConstant":false,"paramNames":["recipient","amount"],"isLibrary":false}}},"hasEnv":true}}},"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":2}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}}}}}
		NopCmd
		NopCmd
		NopCmd
		NopCmd
		NopCmd
		AssignExpCmd:60 I152 CANON14:6
		AssignExpCmd:61 I153 CANON15:7
	}
	Block 6_0_0_0_0_0 Succ [] {
		AnnotationCmd JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageGlobalChangeSnippet.StorageTakeSnapshot","lhs":{"namePrefix":"lastStorage","tag":{"#class":"tac.Tag.BlockchainState"},"callIndex":0,"meta":[{"key":{"name":"cvl.local","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true},{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"lastStorage"},{"key":{"name":"cvl.type","type":"spec.cvlast.CVLType$PureCVLType","erasureStrategy":"CallTrace"},"value":{"#class":"spec.cvlast.CVLType.PureCVLType.VMInternal.BlockchainState"}},{"key":{"name":"cvl","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true},{"key":{"name":"cvl.display","type":"java.lang.String","erasureStrategy":"CallTrace"},"value":"lastStorage"}]}}}
		AnnotationCmd:33 JSON{"key":{"name":"cvl.label.end","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		AnnotationCmd:62 JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Cmd","cmd":{"cmd_type":"spec.cvlast.CVLCmd.Simple.Assert","cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/spec/ERC20.spec","start":{"line":71,"character":4},"end":{"line":71,"character":25}},"exp":{"#class":"spec.cvlast.CVLExp.UnaryExp.LNotExp","e":{"#class":"spec.cvlast.CVLExp.VariableExp","id":"lastReverted","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":2}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"},"cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/spec/ERC20.spec","start":{"line":71,"character":4},"end":{"line":71,"character":25}}},"twoStateIndex":"NEITHER"},"tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":2}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"},"cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/spec/ERC20.spec","start":{"line":71,"character":11},"end":{"line":71,"character":24}}}},"description":"","scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":2}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}}}}}
		AssignExpCmd:63 CANON110!!155:48 LNot(lastReverted!!205:64 )
		AssertCmd:65 CANON110!!155:48 ""
		AnnotationCmd:62 JSON{"key":{"name":"cvl.label.end","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
	}
	Block 4_0_0_0_0_0 Succ [6_0_0_0_0_0] {
		AnnotationCmd JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageGlobalChangeSnippet.StorageRestoreSnapshot","name":{"namePrefix":"CANON69","tag":{"#class":"tac.Tag.BlockchainState"},"callIndex":0}}}
		JumpCmd:33 6_0_0_0_0_0
	}
	Block 5_0_0_0_0_0 Succ [6_0_0_0_0_0] {
		JumpCmd:33 6_0_0_0_0_0
	}
	Block 3_0_0_0_0_0 Succ [4_0_0_0_0_0, 5_0_0_0_0_0] {
		AssignExpCmd:33 B156 LOr(lastReverted!!205:64 lastHasThrown!!206:66 )
		JumpiCmd:33 4_0_0_0_0_0 5_0_0_0_0_0 B156
	}
	Block 860_1023_0_3_2_0 Succ [3_0_0_3_0_123, 7079_1018_0_3_2_0] {
		AssignExpCmd:67 R157:68 Sub(tacCalldatasize!!77:17 0x4 )
		AssignExpCmd:33 B158:21 Slt(R157:68 0x40 )
		JumpiCmd:69 3_0_0_3_0_123 7079_1018_0_3_2_0 B158:21
	}
	Block 5947_1016_0_3_0_0 Succ [3_0_0_3_0_123] {
		AnnotationCmd:33 JSON{"key":{"name":"init.reorder.fence","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
	}
	Block 6005_1016_0_3_0_0 Succ [6059_1016_0_3_0_0, 6117_1016_0_3_0_0] {
		AssignExpCmd:70 R162:71 BWAnd(0xffffffffffffffffffffffffffffffffffffffff tacCalldatabufCANON0@3:72 )
		AssignExpCmd:33 B163:73 Eq(R162:71 0x0 )
		JumpiCmd:74 6059_1016_0_3_0_0 6117_1016_0_3_0_0 B163:73
	}
	Block 6059_1016_0_3_0_0 Succ [3_0_0_3_0_123] {
		AnnotationCmd:33 JSON{"key":{"name":"init.reorder.fence","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
	}
	Block 6117_1016_0_3_0_0 Succ [6204_1015_0_3_0_0, 6262_1015_0_3_0_0] {
		AnnotationCmd:33 JSON{"key":{"name":"internal.func.start","type":"analysis.ip.InternalFuncStartAnnotation","erasureStrategy":"CallTrace"},"value":{"id":4,"startPc":6534,"args":[{"s":{"namePrefix":"R88","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.env.known-bit-width","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":160},{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1018}]},"offset":1,"sort":"SCALAR"},{"s":{"namePrefix":"R195","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1012}]},"offset":2,"sort":"SCALAR"},{"s":{"namePrefix":"R207","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1012}]},"offset":3,"sort":"SCALAR"}],"methodSignature":{"#class":"spec.cvlast.QualifiedMethodSignature.QualifiedMethodSig","qualifiedMethodName":{"#class":"spec.cvlast.QualifiedFunction","host":{"name":"ERC20"},"methodId":"_beforeTokenTransfer"},"params":[{"#class":"spec.cvlast.VMParam.Named","name":"from","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$address"}},{"#class":"spec.cvlast.VMParam.Named","name":"to","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$address"}},{"#class":"spec.cvlast.VMParam.Named","name":"amount","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256}}],"res":[]},"stackOffsetToArgPos":{"1":0,"2":1,"3":2},"callSiteSrc":{"source":0,"begin":11607,"len":47,"jumpType":"ENTER","address":"ce4604a0000000000000000000000003","sourceContext":{"indexToFilepath":{"0":"contracts/ERC20.sol","1":"contracts/IERC20.sol","2":"contracts/IERC20Metadata.sol"},"sourceDir":".post_autofinders.0"}}}}
		AnnotationCmd:33 JSON{"key":{"name":"internal.func.end","type":"analysis.ip.InternalFuncExitAnnotation","erasureStrategy":"Canonical"},"value":{"id":4,"rets":[],"functionLayout":{}}}
		AssignExpCmd:75 R170:71 Apply(hash_3_keccak:bif Apply(skey_basic:bif 0x40) Apply(to_skey:bif R88:76) Apply(skey_basic:bif 0x0))
		AssignExpCmd:77 R171:71 Select(CANON26!!4:8 R170:78 )
		AnnotationCmd:33 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet","value":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R171","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1014}]},"displayPath":{"#class":"analysis.storage.DisplayPath.MapAccess","key":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R88","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.env.known-bit-width","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":160},{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1012}]},"keyTyp":{"#class":"tac.TACStorageType.IntegralType","typeLabel":"address","numBytes":"14","descriptor":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$address"},"lowerBound":null,"upperBound":null},"base":{"#class":"analysis.storage.DisplayPath.Root","name":"_balances"}},"storageType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256},"contractInstance":"ce4604a0000000000000000000000003","linkableStorageReadId":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet.None"}}}
		AssignExpCmd:33 B172:71 Lt(R171:71 tacCalldatabufCANON1@3:79 )
		JumpiCmd:80 6204_1015_0_3_0_0 6262_1015_0_3_0_0 B172:71
	}
	Block 6204_1015_0_3_0_0 Succ [3_0_0_3_0_123] {
		AnnotationCmd:33 JSON{"key":{"name":"init.reorder.fence","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
	}
	Block 6262_1015_0_3_0_0 Succ [8875_1008_0_3_0_0, 8883_1008_0_3_0_0] {
		AssignExpCmd:81 R177:71 Sub(R171:71 tacCalldatabufCANON1@3:79 )
		AssignExpCmd:82 R180:83 Apply(hash_3_keccak:bif Apply(skey_basic:bif 0x40) Apply(to_skey:bif R88:76) Apply(skey_basic:bif 0x0))
		AnnotationCmd JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Message","s":"Apply hook Hook Sstore 0x0.0x0[key a] uint256 new_value tacS:wordmap"}}
		AssignExpCmd R181:15 Select(CANON26!!4:8 R180:84 )
		AnnotationCmd JSON{"key":{"name":"tac.inlined.hook","type":"instrumentation.transformers.HookInliner$InlinedHook","erasureStrategy":"Canonical"},"value":{"cvlPattern":{"#class":"spec.cvlast.CVLHookPattern.StoragePattern.Store","value":{"name":"new_value","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256}},"slot":{"#class":"spec.cvlast.CVLSlotPattern.MapAccess","base":{"#class":"spec.cvlast.CVLSlotPattern.Static.Named","solidityContract":{"name":"ERC20"},"name":"_balances"},"key":{"name":"a","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$address"}}},"base":"STORAGE","previousValue":{"name":"old_value","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256}}},"substitutions":{"new_value":{"#class":"vc.data.HookValue.Direct","expr":{"#class":"vc.data.TACExpr.Sym.Var","s":{"namePrefix":"R177","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1014}]},"tag":{"#class":"tac.Tag.Bit256"}}},"old_value":{"#class":"vc.data.HookValue.Direct","expr":{"#class":"vc.data.TACExpr.Sym.Var","s":{"namePrefix":"R181","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}]},"tag":{"#class":"tac.Tag.Bit256"}}},"a":{"#class":"vc.data.HookValue.Direct","expr":{"#class":"vc.data.TACExpr.Sym.Var","s":{"namePrefix":"R88","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.env.known-bit-width","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":160},{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1011}]},"tag":{"#class":"tac.Tag.Bit256"}}}}}}
		AssignExpCmd:85 CANON26!!182:8 Store(CANON26!!4:8 R180:84 R177:71 )
		AnnotationCmd JSON{"key":{"name":"cvl.label.end","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		AnnotationCmd:33 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.StoreSnippet","value":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R177","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1014}]},"displayPath":{"#class":"analysis.storage.DisplayPath.MapAccess","key":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R88","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.env.known-bit-width","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":160},{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1011}]},"keyTyp":{"#class":"tac.TACStorageType.IntegralType","typeLabel":"address","numBytes":"14","descriptor":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$address"},"lowerBound":null,"upperBound":null},"base":{"#class":"analysis.storage.DisplayPath.Root","name":"_balances"}},"storageType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256},"contractInstance":"ce4604a0000000000000000000000003"}}
		AssignExpCmd:86 R188:87 BWAnd(0xffffffffffffffffffffffffffffffffffffffff tacCalldatabufCANON0@3:72 )
		AssignExpCmd:86 R191:83 Apply(hash_3_keccak:bif Apply(skey_basic:bif 0x40) Apply(to_skey:bif R188:88) Apply(skey_basic:bif 0x0))
		AssignExpCmd:89 R192:90 Select(CANON26!!182:8 R191:91 )
		AnnotationCmd:33 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet","value":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R192","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1010}]},"displayPath":{"#class":"analysis.storage.DisplayPath.MapAccess","key":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R188","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1011}]},"keyTyp":{"#class":"tac.TACStorageType.IntegralType","typeLabel":"address","numBytes":"14","descriptor":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$address"},"lowerBound":null,"upperBound":null},"base":{"#class":"analysis.storage.DisplayPath.Root","name":"_balances"}},"storageType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256},"contractInstance":"ce4604a0000000000000000000000003","linkableStorageReadId":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet.None"}}}
		AssignExpCmd:92 R193:93 Sub(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff tacCalldatabufCANON1@3:79 )
		AssignExpCmd:33 B194:93 Gt(R192:90 R193:93 )
		JumpiCmd:94 8875_1008_0_3_0_0 8883_1008_0_3_0_0 B194:93
	}
	Block 7079_1018_0_3_2_0 Succ [9166_1011_0_3_0_0, 3_0_0_3_0_123] {
		AssignExpCmd:95 R195:96 tacCalldatabufCANON0@3:72
		AssignExpCmd:97 R196:98 BWAnd(R81 0xffffffffffffffffffffffffffffffffffffffff )
		AssignExpCmd:33 B197:90 Eq(R81 R196:98 )
		JumpiCmd:99 9166_1011_0_3_0_0 3_0_0_3_0_123 B197:90
	}
	Block 8875_1008_0_3_0_0 Succ [3_0_0_3_0_123] {
		NopCmd
	}
	Block 8883_1008_0_3_0_0 Succ [3_0_0_0_0_0] {
		AssignExpCmd:100 R198:93 Add(R192:90 tacCalldatabufCANON1@3:79)
		AnnotationCmd JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Message","s":"Apply hook Hook Sstore 0x0.0x0[key a] uint256 new_value tacS:wordmap"}}
		AssignExpCmd R199:15 Select(CANON26!!182:8 R191:91 )
		AnnotationCmd JSON{"key":{"name":"tac.inlined.hook","type":"instrumentation.transformers.HookInliner$InlinedHook","erasureStrategy":"Canonical"},"value":{"cvlPattern":{"#class":"spec.cvlast.CVLHookPattern.StoragePattern.Store","value":{"name":"new_value","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256}},"slot":{"#class":"spec.cvlast.CVLSlotPattern.MapAccess","base":{"#class":"spec.cvlast.CVLSlotPattern.Static.Named","solidityContract":{"name":"ERC20"},"name":"_balances"},"key":{"name":"a","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$address"}}},"base":"STORAGE","previousValue":{"name":"old_value","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256}}},"substitutions":{"new_value":{"#class":"vc.data.HookValue.Direct","expr":{"#class":"vc.data.TACExpr.Sym.Var","s":{"namePrefix":"R198","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1007}]},"tag":{"#class":"tac.Tag.Bit256"}}},"old_value":{"#class":"vc.data.HookValue.Direct","expr":{"#class":"vc.data.TACExpr.Sym.Var","s":{"namePrefix":"R199","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}]},"tag":{"#class":"tac.Tag.Bit256"}}},"a":{"#class":"vc.data.HookValue.Direct","expr":{"#class":"vc.data.TACExpr.Sym.Var","s":{"namePrefix":"R188","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1011}]},"tag":{"#class":"tac.Tag.Bit256"}}}}}}
		AnnotationCmd JSON{"key":{"name":"cvl.label.end","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		AnnotationCmd:33 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.StoreSnippet","value":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R198","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1007}]},"displayPath":{"#class":"analysis.storage.DisplayPath.MapAccess","key":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R188","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1011}]},"keyTyp":{"#class":"tac.TACStorageType.IntegralType","typeLabel":"address","numBytes":"14","descriptor":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$address"},"lowerBound":null,"upperBound":null},"base":{"#class":"analysis.storage.DisplayPath.Root","name":"_balances"}},"storageType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256},"contractInstance":"ce4604a0000000000000000000000003"}}
		AnnotationCmd:33 JSON{"key":{"name":"internal.func.start","type":"analysis.ip.InternalFuncStartAnnotation","erasureStrategy":"CallTrace"},"value":{"id":5,"startPc":6686,"args":[{"s":{"namePrefix":"R88","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.env.known-bit-width","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":160},{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1018}]},"offset":1,"sort":"SCALAR"},{"s":{"namePrefix":"R195","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1012}]},"offset":2,"sort":"SCALAR"},{"s":{"namePrefix":"R207","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1012}]},"offset":3,"sort":"SCALAR"}],"methodSignature":{"#class":"spec.cvlast.QualifiedMethodSignature.QualifiedMethodSig","qualifiedMethodName":{"#class":"spec.cvlast.QualifiedFunction","host":{"name":"ERC20"},"methodId":"_afterTokenTransfer"},"params":[{"#class":"spec.cvlast.VMParam.Named","name":"from","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$address"}},{"#class":"spec.cvlast.VMParam.Named","name":"to","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$address"}},{"#class":"spec.cvlast.VMParam.Named","name":"amount","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256}}],"res":[]},"stackOffsetToArgPos":{"1":0,"2":1,"3":2},"callSiteSrc":{"source":0,"begin":12013,"len":46,"jumpType":"ENTER","address":"ce4604a0000000000000000000000003","sourceContext":{"indexToFilepath":{"0":"contracts/ERC20.sol","1":"contracts/IERC20.sol","2":"contracts/IERC20Metadata.sol"},"sourceDir":".post_autofinders.0"}}}}
		AnnotationCmd:33 JSON{"key":{"name":"internal.func.end","type":"analysis.ip.InternalFuncExitAnnotation","erasureStrategy":"Canonical"},"value":{"id":5,"rets":[],"functionLayout":{}}}
		AnnotationCmd:33 JSON{"key":{"name":"internal.func.end","type":"analysis.ip.InternalFuncExitAnnotation","erasureStrategy":"Canonical"},"value":{"id":3,"rets":[],"functionLayout":{}}}
		AssignExpCmd:33 R202:101 0x1
		AnnotationCmd:33 JSON{"key":{"name":"internal.func.end","type":"analysis.ip.InternalFuncExitAnnotation","erasureStrategy":"Canonical"},"value":{"id":2,"rets":[{"s":{"namePrefix":"R202","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1023}]},"offset":0}],"functionLayout":{"0":{"#class":"analysis.ip.InternalFuncValueLocation.Scalar"}}}}
		AnnotationCmd:33 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.EVMFunctionReturnWrite","returnbufOffset":"0","returnValueSym":{"#class":"vc.data.TACSymbol.Const","value":"1","tag":{"#class":"tac.Tag.Bool"}},"callIndex":3}}
		AnnotationCmd:33 JSON{"key":{"name":"tac.return.path","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		LabelCmd:33 "End procedure ERC20-transfer(address,uint256)"
		AssignExpCmd:33 lastReverted!!203:64 false
		AssignExpCmd:33 lastHasThrown!!204:66 false
		AnnotationCmd:33 JSON{"key":{"name":"call.trace.pop","type":"analysis.icfg.Inliner$CallStack$PopRecord","erasureStrategy":"Canonical"},"value":"rO0ABXNyAClhbmFseXNpcy5pY2ZnLklubGluZXIkQ2FsbFN0YWNrJFBvcFJlY29yZPAPfwSLdCWJAgABSQAIY2FsbGVlSWR4cAAAAAM="}
		LabelCmd "Parallel assignment for lastReverted!!205:bool, lastHasThrown!!206:bool := lastReverted!!203:bool, lastHasThrown!!204:bool"
		AssignExpCmd lastReverted!!205:64 lastReverted!!203:64
		AssignExpCmd lastHasThrown!!206:66 lastHasThrown!!204:66
	}
	Block 9166_1011_0_3_0_0 Succ [5947_1016_0_3_0_0, 6005_1016_0_3_0_0] {
		AssignExpCmd:102 R207:96 tacCalldatabufCANON1@3:79
		AnnotationCmd:33 JSON{"key":{"name":"internal.func.start","type":"analysis.ip.InternalFuncStartAnnotation","erasureStrategy":"CallTrace"},"value":{"id":2,"startPc":4563,"args":[{"s":{"namePrefix":"R195","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1012}]},"offset":1,"sort":"SCALAR"},{"s":{"namePrefix":"R207","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1012}]},"offset":2,"sort":"SCALAR"}],"methodSignature":{"#class":"spec.cvlast.QualifiedMethodSignature.QualifiedMethodSig","qualifiedMethodName":{"#class":"spec.cvlast.QualifiedFunction","host":{"name":"ERC20"},"methodId":"transfer"},"params":[{"#class":"spec.cvlast.VMParam.Named","name":"recipient","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$address"}},{"#class":"spec.cvlast.VMParam.Named","name":"amount","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256}}],"res":[{"#class":"spec.cvlast.VMParam.Unnamed","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$bool"}}]},"stackOffsetToArgPos":{"1":0,"2":1},"callSiteSrc":{"source":0,"begin":5042,"len":547,"jumpType":"ENTER","address":"ce4604a0000000000000000000000003","sourceContext":{"indexToFilepath":{"0":"contracts/ERC20.sol","1":"contracts/IERC20.sol","2":"contracts/IERC20Metadata.sol"},"sourceDir":".post_autofinders.0"}}}}
		AnnotationCmd:33 JSON{"key":{"name":"internal.func.start","type":"analysis.ip.InternalFuncStartAnnotation","erasureStrategy":"CallTrace"},"value":{"id":3,"startPc":5746,"args":[{"s":{"namePrefix":"R88","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.env.known-bit-width","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":160},{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1018}]},"offset":1,"sort":"SCALAR"},{"s":{"namePrefix":"R195","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1012}]},"offset":2,"sort":"SCALAR"},{"s":{"namePrefix":"R207","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1012}]},"offset":3,"sort":"SCALAR"}],"methodSignature":{"#class":"spec.cvlast.QualifiedMethodSignature.QualifiedMethodSig","qualifiedMethodName":{"#class":"spec.cvlast.QualifiedFunction","host":{"name":"ERC20"},"methodId":"_transfer"},"params":[{"#class":"spec.cvlast.VMParam.Named","name":"sender","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$address"}},{"#class":"spec.cvlast.VMParam.Named","name":"recipient","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$address"}},{"#class":"spec.cvlast.VMParam.Named","name":"amount","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256}}],"res":[]},"stackOffsetToArgPos":{"1":0,"2":1,"3":2},"callSiteSrc":{"source":0,"begin":5521,"len":40,"jumpType":"ENTER","address":"ce4604a0000000000000000000000003","sourceContext":{"indexToFilepath":{"0":"contracts/ERC20.sol","1":"contracts/IERC20.sol","2":"contracts/IERC20Metadata.sol"},"sourceDir":".post_autofinders.0"}}}}
		AssignExpCmd:33 B209:73 Eq(R88:36 0x0 )
		JumpiCmd:103 5947_1016_0_3_0_0 6005_1016_0_3_0_0 B209:73
	}
	Block 3_0_0_3_0_123 Succ [3_0_0_0_0_0] {
		AnnotationCmd JSON{"key":{"name":"tac.revert.path","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		LabelCmd "End procedure ERC20-transfer(address,uint256)"
		AssignExpCmd lastReverted!!210:64 true
		AssignExpCmd lastHasThrown!!211:66 false
		AnnotationCmd JSON{"key":{"name":"call.trace.pop","type":"analysis.icfg.Inliner$CallStack$PopRecord","erasureStrategy":"Canonical"},"value":"rO0ABXNyAClhbmFseXNpcy5pY2ZnLklubGluZXIkQ2FsbFN0YWNrJFBvcFJlY29yZPAPfwSLdCWJAgABSQAIY2FsbGVlSWR4cAAAAAM="}
		LabelCmd "Parallel assignment for lastReverted!!205:bool, lastHasThrown!!206:bool := lastReverted!!210:bool, lastHasThrown!!211:bool"
		AssignExpCmd lastReverted!!205:64 lastReverted!!210:64
		AssignExpCmd lastHasThrown!!206:66 lastHasThrown!!211:66
	}
}
Axioms {
		CANON71
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
  "3": [
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
  "4": [
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
  "6": [
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
      "value": "recipient"
    }
  ],
  "7": [
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
      "value": "amount"
    }
  ],
  "8": [
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
  "9": [
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
  "14": [
    {
      "key": {
        "name": "Tac.symbol.keyword",
        "type": "java.lang.String",
        "erasureStrategy": "Canonical"
      },
      "value": "tacSighash"
    }
  ],
  "15": [
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
  "16": [
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
          "line": 64,
          "character": 4
        },
        "end": {
          "line": 64,
          "character": 45
        }
      }
    }
  ],
  "17": [
    {
      "key": {
        "name": "Tac.symbol.keyword",
        "type": "java.lang.String",
        "erasureStrategy": "Canonical"
      },
      "value": "tacCalldatasize"
    }
  ],
  "18": [
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
  "19": [
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
          "line": 64,
          "character": 4
        },
        "end": {
          "line": 64,
          "character": 45
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
        "begin": 4328,
        "len": 511,
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
  "20": [
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
          "line": 64,
          "character": 4
        },
        "end": {
          "line": 64,
          "character": 45
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
  "21": [
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
  "22": [
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
          "line": 64,
          "character": 4
        },
        "end": {
          "line": 64,
          "character": 45
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
  "23": [
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
  "24": [
    {
      "key": {
        "name": "Tac.symbol.keyword",
        "type": "java.lang.String",
        "erasureStrategy": "Canonical"
      },
      "value": "tacM0x0"
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
          "line": 64,
          "character": 4
        },
        "end": {
          "line": 64,
          "character": 45
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
  "26": [
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
              "namePrefix": "R35",
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
                "namePrefix": "R35",
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
                "namePrefix": "CANON28",
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
                "namePrefix": "CANON27",
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
      "value": 1020
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
          "line": 66,
          "character": 4
        },
        "end": {
          "line": 66,
          "character": 53
        }
      }
    }
  ],
  "28": [
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
          "line": 66,
          "character": 4
        },
        "end": {
          "line": 66,
          "character": 53
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
        "begin": 4328,
        "len": 511,
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
          "line": 66,
          "character": 4
        },
        "end": {
          "line": 66,
          "character": 53
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
          "line": 66,
          "character": 4
        },
        "end": {
          "line": 66,
          "character": 53
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
          "line": 66,
          "character": 4
        },
        "end": {
          "line": 66,
          "character": 53
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
                    "value": 1018
                  }
                ]
              },
              "baseSlot": {
                "#class": "vc.data.TACSymbol.Var.Full",
                "namePrefix": "CANON28",
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
                "namePrefix": "CANON27",
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
          "line": 70,
          "character": 4
        },
        "end": {
          "line": 70,
          "character": 46
        }
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
          "line": 70,
          "character": 4
        },
        "end": {
          "line": 70,
          "character": 46
        }
      }
    }
  ],
  "42": [
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
      "value": 1022
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
          "line": 70,
          "character": 4
        },
        "end": {
          "line": 70,
          "character": 46
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
        "begin": 5042,
        "len": 547,
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
        "name": "cvl.exp",
        "type": "spec.CVLExpToTACExprMeta",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "spec.CVLExpToTACExprMeta.NullaryCVLExp",
        "exp": {
          "#class": "spec.cvlast.CVLExp.VariableExp",
          "id": "amount",
          "tag": {
            "scope": {
              "scopeStack": [
                {
                  "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                },
                {
                  "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                  "scopeId": 2
                }
              ],
              "innerScope": {
                "scopeStack": [
                  {
                    "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                  }
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
              "#class": "spec.cvlast.CVLRange.Range",
              "specFile": "certora/spec/ERC20.spec",
              "start": {
                "line": 64,
                "character": 4
              },
              "end": {
                "line": 64,
                "character": 45
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
          "line": 64,
          "character": 4
        },
        "end": {
          "line": 64,
          "character": 45
        }
      }
    }
  ],
  "45": [
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
                    "methodId": "balanceOf"
                  },
                  "params": [
                    {
                      "#class": "spec.cvlast.VMParam.Named",
                      "name": "account",
                      "vmType": {
                        "#class": "ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$address"
                      }
                    }
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
                  "n": "70a08231"
                }
              }
            },
            "args": [
              {
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
                            "scopeId": 2
                          }
                        ],
                        "innerScope": {
                          "scopeStack": [
                            {
                              "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                            }
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
                          "line": 64,
                          "character": 4
                        },
                        "end": {
                          "line": 64,
                          "character": 45
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
                          "scopeId": 2
                        }
                      ],
                      "innerScope": {
                        "scopeStack": [
                          {
                            "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                          }
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
                        "line": 64,
                        "character": 22
                      },
                      "end": {
                        "line": 64,
                        "character": 23
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
                        "scopeId": 2
                      }
                    ],
                    "innerScope": {
                      "scopeStack": [
                        {
                          "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                        }
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
                      "line": 64,
                      "character": 22
                    },
                    "end": {
                      "line": 64,
                      "character": 23
                    }
                  }
                }
              }
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
                      "scopeId": 2
                    }
                  ],
                  "innerScope": {
                    "scopeStack": [
                      {
                        "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                      }
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
                    "line": 64,
                    "character": 4
                  },
                  "end": {
                    "line": 64,
                    "character": 45
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
                    "scopeId": 2
                  }
                ],
                "innerScope": {
                  "scopeStack": [
                    {
                      "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                    }
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
                  "line": 64,
                  "character": 12
                },
                "end": {
                  "line": 64,
                  "character": 21
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
                        "methodId": "balanceOf"
                      },
                      "params": [
                        {
                          "#class": "spec.cvlast.VMParam.Named",
                          "name": "account",
                          "vmType": {
                            "#class": "ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$address"
                          }
                        }
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
                      "n": "70a08231"
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
                      "sigHash": "70a08231",
                      "name": "balanceOf",
                      "argTypes": [
                        {
                          "#class": "spec.cvlast.typedescriptors.EVMTypeDescriptor.address"
                        }
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
                      "paramNames": [
                        "account"
                      ],
                      "isLibrary": false
                    }
                  }
                },
                "hasEnv": false
              }
            }
          },
          "r": {
            "#class": "spec.cvlast.CVLExp.VariableExp",
            "id": "amount",
            "tag": {
              "scope": {
                "scopeStack": [
                  {
                    "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                  },
                  {
                    "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                    "scopeId": 2
                  }
                ],
                "innerScope": {
                  "scopeStack": [
                    {
                      "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                    }
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
                "#class": "spec.cvlast.CVLRange.Range",
                "specFile": "certora/spec/ERC20.spec",
                "start": {
                  "line": 64,
                  "character": 4
                },
                "end": {
                  "line": 64,
                  "character": 45
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
                  "scopeId": 2
                }
              ],
              "innerScope": {
                "scopeStack": [
                  {
                    "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                  }
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
                "line": 64,
                "character": 12
              },
              "end": {
                "line": 64,
                "character": 44
              }
            }
          }
        },
        "o1": {
          "out": {
            "#class": "vc.data.TACSymbol.Var.Full",
            "namePrefix": "I53",
            "tag": {
              "#class": "tac.Tag.Int"
            },
            "callIndex": 0
          },
          "exp": {
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
                    "methodId": "balanceOf"
                  },
                  "params": [
                    {
                      "#class": "spec.cvlast.VMParam.Named",
                      "name": "account",
                      "vmType": {
                        "#class": "ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$address"
                      }
                    }
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
                  "n": "70a08231"
                }
              }
            },
            "args": [
              {
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
                            "scopeId": 2
                          }
                        ],
                        "innerScope": {
                          "scopeStack": [
                            {
                              "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                            }
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
                          "line": 64,
                          "character": 4
                        },
                        "end": {
                          "line": 64,
                          "character": 45
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
                          "scopeId": 2
                        }
                      ],
                      "innerScope": {
                        "scopeStack": [
                          {
                            "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                          }
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
                        "line": 64,
                        "character": 22
                      },
                      "end": {
                        "line": 64,
                        "character": 23
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
                        "scopeId": 2
                      }
                    ],
                    "innerScope": {
                      "scopeStack": [
                        {
                          "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                        }
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
                      "line": 64,
                      "character": 22
                    },
                    "end": {
                      "line": 64,
                      "character": 23
                    }
                  }
                }
              }
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
                      "scopeId": 2
                    }
                  ],
                  "innerScope": {
                    "scopeStack": [
                      {
                        "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                      }
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
                    "line": 64,
                    "character": 4
                  },
                  "end": {
                    "line": 64,
                    "character": 45
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
                    "scopeId": 2
                  }
                ],
                "innerScope": {
                  "scopeStack": [
                    {
                      "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                    }
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
                  "line": 64,
                  "character": 12
                },
                "end": {
                  "line": 64,
                  "character": 21
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
                        "methodId": "balanceOf"
                      },
                      "params": [
                        {
                          "#class": "spec.cvlast.VMParam.Named",
                          "name": "account",
                          "vmType": {
                            "#class": "ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$address"
                          }
                        }
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
                      "n": "70a08231"
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
                      "sigHash": "70a08231",
                      "name": "balanceOf",
                      "argTypes": [
                        {
                          "#class": "spec.cvlast.typedescriptors.EVMTypeDescriptor.address"
                        }
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
                      "paramNames": [
                        "account"
                      ],
                      "isLibrary": false
                    }
                  }
                },
                "hasEnv": false
              }
            }
          }
        },
        "o2": {
          "out": {
            "#class": "vc.data.TACSymbol.Var.Full",
            "namePrefix": "I133",
            "tag": {
              "#class": "tac.Tag.Int"
            },
            "callIndex": 0
          },
          "exp": {
            "#class": "spec.cvlast.CVLExp.VariableExp",
            "id": "amount",
            "tag": {
              "scope": {
                "scopeStack": [
                  {
                    "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                  },
                  {
                    "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                    "scopeId": 2
                  }
                ],
                "innerScope": {
                  "scopeStack": [
                    {
                      "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                    }
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
                "#class": "spec.cvlast.CVLRange.Range",
                "specFile": "certora/spec/ERC20.spec",
                "start": {
                  "line": 64,
                  "character": 4
                },
                "end": {
                  "line": 64,
                  "character": 45
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
          "line": 64,
          "character": 4
        },
        "end": {
          "line": 64,
          "character": 45
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
          "line": 65,
          "character": 4
        },
        "end": {
          "line": 65,
          "character": 29
        }
      }
    }
  ],
  "47": [
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
                        "scopeId": 2
                      }
                    ],
                    "innerScope": {
                      "scopeStack": [
                        {
                          "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                        }
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
                      "line": 65,
                      "character": 4
                    },
                    "end": {
                      "line": 65,
                      "character": 29
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
                      "scopeId": 2
                    }
                  ],
                  "innerScope": {
                    "scopeStack": [
                      {
                        "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                      }
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
                    "line": 65,
                    "character": 12
                  },
                  "end": {
                    "line": 65,
                    "character": 13
                  }
                }
              }
            },
            "fieldName": "value",
            "tag": {
              "scope": {
                "scopeStack": [
                  {
                    "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                  },
                  {
                    "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                    "scopeId": 2
                  }
                ],
                "innerScope": {
                  "scopeStack": [
                    {
                      "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                    }
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
                "#class": "spec.cvlast.CVLRange.Range",
                "specFile": "certora/spec/ERC20.spec",
                "start": {
                  "line": 65,
                  "character": 12
                },
                "end": {
                  "line": 65,
                  "character": 13
                }
              }
            }
          },
          "r": {
            "#class": "spec.cvlast.CVLExp.Constant.NumberLit",
            "n": "0",
            "tag": {
              "scope": {
                "scopeStack": [
                  {
                    "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                  },
                  {
                    "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                    "scopeId": 2
                  }
                ],
                "innerScope": {
                  "scopeStack": [
                    {
                      "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                    }
                  ],
                  "innerScope": {
                    "scopeStack": [
                    ],
                    "innerScope": null
                  }
                }
              },
              "type": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.NumberLiteral",
                "n": "0"
              },
              "cvlRange": {
                "#class": "spec.cvlast.CVLRange.Range",
                "specFile": "certora/spec/ERC20.spec",
                "start": {
                  "line": 65,
                  "character": 27
                },
                "end": {
                  "line": 65,
                  "character": 28
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
                  "scopeId": 2
                }
              ],
              "innerScope": {
                "scopeStack": [
                  {
                    "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                  }
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
                "line": 65,
                "character": 12
              },
              "end": {
                "line": 65,
                "character": 28
              }
            }
          }
        },
        "o1": {
          "out": {
            "#class": "vc.data.TACSymbol.Var.Full",
            "namePrefix": "CANON34",
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
                        "scopeId": 2
                      }
                    ],
                    "innerScope": {
                      "scopeStack": [
                        {
                          "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                        }
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
                      "line": 65,
                      "character": 4
                    },
                    "end": {
                      "line": 65,
                      "character": 29
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
                      "scopeId": 2
                    }
                  ],
                  "innerScope": {
                    "scopeStack": [
                      {
                        "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                      }
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
                    "line": 65,
                    "character": 12
                  },
                  "end": {
                    "line": 65,
                    "character": 13
                  }
                }
              }
            },
            "fieldName": "value",
            "tag": {
              "scope": {
                "scopeStack": [
                  {
                    "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                  },
                  {
                    "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                    "scopeId": 2
                  }
                ],
                "innerScope": {
                  "scopeStack": [
                    {
                      "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                    }
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
                "#class": "spec.cvlast.CVLRange.Range",
                "specFile": "certora/spec/ERC20.spec",
                "start": {
                  "line": 65,
                  "character": 12
                },
                "end": {
                  "line": 65,
                  "character": 13
                }
              }
            }
          }
        },
        "o2": {
          "out": {
            "#class": "vc.data.TACSymbol.Const",
            "value": "0"
          },
          "exp": {
            "#class": "spec.cvlast.CVLExp.Constant.NumberLit",
            "n": "0",
            "tag": {
              "scope": {
                "scopeStack": [
                  {
                    "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                  },
                  {
                    "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                    "scopeId": 2
                  }
                ],
                "innerScope": {
                  "scopeStack": [
                    {
                      "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                    }
                  ],
                  "innerScope": {
                    "scopeStack": [
                    ],
                    "innerScope": null
                  }
                }
              },
              "type": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.NumberLiteral",
                "n": "0"
              },
              "cvlRange": {
                "#class": "spec.cvlast.CVLRange.Range",
                "specFile": "certora/spec/ERC20.spec",
                "start": {
                  "line": 65,
                  "character": 27
                },
                "end": {
                  "line": 65,
                  "character": 28
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
          "line": 65,
          "character": 4
        },
        "end": {
          "line": 65,
          "character": 29
        }
      }
    }
  ],
  "48": [
    {
      "key": {
        "name": "cvl",
        "type": "java.lang.Boolean",
        "erasureStrategy": "Canonical"
      },
      "value": true
    }
  ],
  "49": [
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
          "id": "recipient",
          "tag": {
            "scope": {
              "scopeStack": [
                {
                  "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                },
                {
                  "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                  "scopeId": 2
                }
              ],
              "innerScope": {
                "scopeStack": [
                  {
                    "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                  }
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
                "line": 66,
                "character": 4
              },
              "end": {
                "line": 66,
                "character": 53
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
          "line": 66,
          "character": 4
        },
        "end": {
          "line": 66,
          "character": 53
        }
      }
    }
  ],
  "50": [
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
          "id": "amount",
          "tag": {
            "scope": {
              "scopeStack": [
                {
                  "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                },
                {
                  "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                  "scopeId": 2
                }
              ],
              "innerScope": {
                "scopeStack": [
                  {
                    "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                  }
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
              "#class": "spec.cvlast.CVLRange.Range",
              "specFile": "certora/spec/ERC20.spec",
              "start": {
                "line": 66,
                "character": 4
              },
              "end": {
                "line": 66,
                "character": 53
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
          "line": 66,
          "character": 4
        },
        "end": {
          "line": 66,
          "character": 53
        }
      }
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
        "#class": "spec.CVLExpToTACExprMeta.BinaryCVLExp",
        "exp": {
          "#class": "spec.cvlast.CVLExp.BinaryExp.AddExp",
          "l": {
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
                    "methodId": "balanceOf"
                  },
                  "params": [
                    {
                      "#class": "spec.cvlast.VMParam.Named",
                      "name": "account",
                      "vmType": {
                        "#class": "ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$address"
                      }
                    }
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
                  "n": "70a08231"
                }
              }
            },
            "args": [
              {
                "#class": "spec.cvlast.CVLExp.VariableExp",
                "id": "recipient",
                "tag": {
                  "scope": {
                    "scopeStack": [
                      {
                        "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                      },
                      {
                        "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                        "scopeId": 2
                      }
                    ],
                    "innerScope": {
                      "scopeStack": [
                        {
                          "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                        }
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
                      "line": 66,
                      "character": 4
                    },
                    "end": {
                      "line": 66,
                      "character": 53
                    }
                  }
                },
                "twoStateIndex": "NEITHER"
              }
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
                      "scopeId": 2
                    }
                  ],
                  "innerScope": {
                    "scopeStack": [
                      {
                        "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                      }
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
                    "line": 66,
                    "character": 4
                  },
                  "end": {
                    "line": 66,
                    "character": 53
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
                    "scopeId": 2
                  }
                ],
                "innerScope": {
                  "scopeStack": [
                    {
                      "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                    }
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
                  "line": 66,
                  "character": 12
                },
                "end": {
                  "line": 66,
                  "character": 21
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
                        "methodId": "balanceOf"
                      },
                      "params": [
                        {
                          "#class": "spec.cvlast.VMParam.Named",
                          "name": "account",
                          "vmType": {
                            "#class": "ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$address"
                          }
                        }
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
                      "n": "70a08231"
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
                      "sigHash": "70a08231",
                      "name": "balanceOf",
                      "argTypes": [
                        {
                          "#class": "spec.cvlast.typedescriptors.EVMTypeDescriptor.address"
                        }
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
                      "paramNames": [
                        "account"
                      ],
                      "isLibrary": false
                    }
                  }
                },
                "hasEnv": false
              }
            }
          },
          "r": {
            "#class": "spec.cvlast.CVLExp.VariableExp",
            "id": "amount",
            "tag": {
              "scope": {
                "scopeStack": [
                  {
                    "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                  },
                  {
                    "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                    "scopeId": 2
                  }
                ],
                "innerScope": {
                  "scopeStack": [
                    {
                      "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                    }
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
                "#class": "spec.cvlast.CVLRange.Range",
                "specFile": "certora/spec/ERC20.spec",
                "start": {
                  "line": 66,
                  "character": 4
                },
                "end": {
                  "line": 66,
                  "character": 53
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
                  "scopeId": 2
                }
              ],
              "innerScope": {
                "scopeStack": [
                  {
                    "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                  }
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
                "line": 66,
                "character": 12
              },
              "end": {
                "line": 66,
                "character": 41
              }
            }
          }
        },
        "o1": {
          "out": {
            "#class": "vc.data.TACSymbol.Var.Full",
            "namePrefix": "I76",
            "tag": {
              "#class": "tac.Tag.Int"
            },
            "callIndex": 0
          },
          "exp": {
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
                    "methodId": "balanceOf"
                  },
                  "params": [
                    {
                      "#class": "spec.cvlast.VMParam.Named",
                      "name": "account",
                      "vmType": {
                        "#class": "ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$address"
                      }
                    }
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
                  "n": "70a08231"
                }
              }
            },
            "args": [
              {
                "#class": "spec.cvlast.CVLExp.VariableExp",
                "id": "recipient",
                "tag": {
                  "scope": {
                    "scopeStack": [
                      {
                        "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                      },
                      {
                        "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                        "scopeId": 2
                      }
                    ],
                    "innerScope": {
                      "scopeStack": [
                        {
                          "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                        }
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
                      "line": 66,
                      "character": 4
                    },
                    "end": {
                      "line": 66,
                      "character": 53
                    }
                  }
                },
                "twoStateIndex": "NEITHER"
              }
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
                      "scopeId": 2
                    }
                  ],
                  "innerScope": {
                    "scopeStack": [
                      {
                        "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                      }
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
                    "line": 66,
                    "character": 4
                  },
                  "end": {
                    "line": 66,
                    "character": 53
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
                    "scopeId": 2
                  }
                ],
                "innerScope": {
                  "scopeStack": [
                    {
                      "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                    }
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
                  "line": 66,
                  "character": 12
                },
                "end": {
                  "line": 66,
                  "character": 21
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
                        "methodId": "balanceOf"
                      },
                      "params": [
                        {
                          "#class": "spec.cvlast.VMParam.Named",
                          "name": "account",
                          "vmType": {
                            "#class": "ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$address"
                          }
                        }
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
                      "n": "70a08231"
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
                      "sigHash": "70a08231",
                      "name": "balanceOf",
                      "argTypes": [
                        {
                          "#class": "spec.cvlast.typedescriptors.EVMTypeDescriptor.address"
                        }
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
                      "paramNames": [
                        "account"
                      ],
                      "isLibrary": false
                    }
                  }
                },
                "hasEnv": false
              }
            }
          }
        },
        "o2": {
          "out": {
            "#class": "vc.data.TACSymbol.Var.Full",
            "namePrefix": "I138",
            "tag": {
              "#class": "tac.Tag.Int"
            },
            "callIndex": 0
          },
          "exp": {
            "#class": "spec.cvlast.CVLExp.VariableExp",
            "id": "amount",
            "tag": {
              "scope": {
                "scopeStack": [
                  {
                    "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                  },
                  {
                    "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                    "scopeId": 2
                  }
                ],
                "innerScope": {
                  "scopeStack": [
                    {
                      "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                    }
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
                "#class": "spec.cvlast.CVLRange.Range",
                "specFile": "certora/spec/ERC20.spec",
                "start": {
                  "line": 66,
                  "character": 4
                },
                "end": {
                  "line": 66,
                  "character": 53
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
          "line": 66,
          "character": 4
        },
        "end": {
          "line": 66,
          "character": 53
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
        "#class": "spec.CVLExpToTACExprMeta.BinaryCVLExp",
        "exp": {
          "#class": "spec.cvlast.CVLExp.RelopExp.ArithRelopExp.LtExp",
          "l": {
            "#class": "spec.cvlast.CVLExp.BinaryExp.AddExp",
            "l": {
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
                      "methodId": "balanceOf"
                    },
                    "params": [
                      {
                        "#class": "spec.cvlast.VMParam.Named",
                        "name": "account",
                        "vmType": {
                          "#class": "ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$address"
                        }
                      }
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
                    "n": "70a08231"
                  }
                }
              },
              "args": [
                {
                  "#class": "spec.cvlast.CVLExp.VariableExp",
                  "id": "recipient",
                  "tag": {
                    "scope": {
                      "scopeStack": [
                        {
                          "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                        },
                        {
                          "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                          "scopeId": 2
                        }
                      ],
                      "innerScope": {
                        "scopeStack": [
                          {
                            "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                          }
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
                        "line": 66,
                        "character": 4
                      },
                      "end": {
                        "line": 66,
                        "character": 53
                      }
                    }
                  },
                  "twoStateIndex": "NEITHER"
                }
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
                        "scopeId": 2
                      }
                    ],
                    "innerScope": {
                      "scopeStack": [
                        {
                          "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                        }
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
                      "line": 66,
                      "character": 4
                    },
                    "end": {
                      "line": 66,
                      "character": 53
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
                      "scopeId": 2
                    }
                  ],
                  "innerScope": {
                    "scopeStack": [
                      {
                        "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                      }
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
                    "line": 66,
                    "character": 12
                  },
                  "end": {
                    "line": 66,
                    "character": 21
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
                          "methodId": "balanceOf"
                        },
                        "params": [
                          {
                            "#class": "spec.cvlast.VMParam.Named",
                            "name": "account",
                            "vmType": {
                              "#class": "ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$address"
                            }
                          }
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
                        "n": "70a08231"
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
                        "sigHash": "70a08231",
                        "name": "balanceOf",
                        "argTypes": [
                          {
                            "#class": "spec.cvlast.typedescriptors.EVMTypeDescriptor.address"
                          }
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
                        "paramNames": [
                          "account"
                        ],
                        "isLibrary": false
                      }
                    }
                  },
                  "hasEnv": false
                }
              }
            },
            "r": {
              "#class": "spec.cvlast.CVLExp.VariableExp",
              "id": "amount",
              "tag": {
                "scope": {
                  "scopeStack": [
                    {
                      "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                    },
                    {
                      "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                      "scopeId": 2
                    }
                  ],
                  "innerScope": {
                    "scopeStack": [
                      {
                        "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                      }
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
                  "#class": "spec.cvlast.CVLRange.Range",
                  "specFile": "certora/spec/ERC20.spec",
                  "start": {
                    "line": 66,
                    "character": 4
                  },
                  "end": {
                    "line": 66,
                    "character": 53
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
                    "scopeId": 2
                  }
                ],
                "innerScope": {
                  "scopeStack": [
                    {
                      "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                    }
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
                  "line": 66,
                  "character": 12
                },
                "end": {
                  "line": 66,
                  "character": 41
                }
              }
            }
          },
          "r": {
            "#class": "spec.cvlast.CVLExp.Constant.NumberLit",
            "n": "ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff",
            "tag": {
              "scope": {
                "scopeStack": [
                  {
                    "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                  },
                  {
                    "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                    "scopeId": 2
                  }
                ],
                "innerScope": {
                  "scopeStack": [
                    {
                      "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                    }
                  ],
                  "innerScope": {
                    "scopeStack": [
                    ],
                    "innerScope": null
                  }
                }
              },
              "type": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.NumberLiteral",
                "n": "ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff"
              },
              "cvlRange": {
                "#class": "spec.cvlast.CVLRange.Range",
                "specFile": "certora/spec/ERC20.spec",
                "start": {
                  "line": 66,
                  "character": 44
                },
                "end": {
                  "line": 66,
                  "character": 52
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
                  "scopeId": 2
                }
              ],
              "innerScope": {
                "scopeStack": [
                  {
                    "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                  }
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
                "line": 66,
                "character": 12
              },
              "end": {
                "line": 66,
                "character": 52
              }
            }
          }
        },
        "o1": {
          "out": {
            "#class": "vc.data.TACSymbol.Var.Full",
            "namePrefix": "I139",
            "tag": {
              "#class": "tac.Tag.Int"
            },
            "callIndex": 0
          },
          "exp": {
            "#class": "spec.cvlast.CVLExp.BinaryExp.AddExp",
            "l": {
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
                      "methodId": "balanceOf"
                    },
                    "params": [
                      {
                        "#class": "spec.cvlast.VMParam.Named",
                        "name": "account",
                        "vmType": {
                          "#class": "ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$address"
                        }
                      }
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
                    "n": "70a08231"
                  }
                }
              },
              "args": [
                {
                  "#class": "spec.cvlast.CVLExp.VariableExp",
                  "id": "recipient",
                  "tag": {
                    "scope": {
                      "scopeStack": [
                        {
                          "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                        },
                        {
                          "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                          "scopeId": 2
                        }
                      ],
                      "innerScope": {
                        "scopeStack": [
                          {
                            "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                          }
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
                        "line": 66,
                        "character": 4
                      },
                      "end": {
                        "line": 66,
                        "character": 53
                      }
                    }
                  },
                  "twoStateIndex": "NEITHER"
                }
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
                        "scopeId": 2
                      }
                    ],
                    "innerScope": {
                      "scopeStack": [
                        {
                          "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                        }
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
                      "line": 66,
                      "character": 4
                    },
                    "end": {
                      "line": 66,
                      "character": 53
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
                      "scopeId": 2
                    }
                  ],
                  "innerScope": {
                    "scopeStack": [
                      {
                        "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                      }
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
                    "line": 66,
                    "character": 12
                  },
                  "end": {
                    "line": 66,
                    "character": 21
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
                          "methodId": "balanceOf"
                        },
                        "params": [
                          {
                            "#class": "spec.cvlast.VMParam.Named",
                            "name": "account",
                            "vmType": {
                              "#class": "ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$address"
                            }
                          }
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
                        "n": "70a08231"
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
                        "sigHash": "70a08231",
                        "name": "balanceOf",
                        "argTypes": [
                          {
                            "#class": "spec.cvlast.typedescriptors.EVMTypeDescriptor.address"
                          }
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
                        "paramNames": [
                          "account"
                        ],
                        "isLibrary": false
                      }
                    }
                  },
                  "hasEnv": false
                }
              }
            },
            "r": {
              "#class": "spec.cvlast.CVLExp.VariableExp",
              "id": "amount",
              "tag": {
                "scope": {
                  "scopeStack": [
                    {
                      "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                    },
                    {
                      "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                      "scopeId": 2
                    }
                  ],
                  "innerScope": {
                    "scopeStack": [
                      {
                        "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                      }
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
                  "#class": "spec.cvlast.CVLRange.Range",
                  "specFile": "certora/spec/ERC20.spec",
                  "start": {
                    "line": 66,
                    "character": 4
                  },
                  "end": {
                    "line": 66,
                    "character": 53
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
                    "scopeId": 2
                  }
                ],
                "innerScope": {
                  "scopeStack": [
                    {
                      "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                    }
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
                  "line": 66,
                  "character": 12
                },
                "end": {
                  "line": 66,
                  "character": 41
                }
              }
            }
          }
        },
        "o2": {
          "out": {
            "#class": "vc.data.TACSymbol.Const",
            "value": "ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff"
          },
          "exp": {
            "#class": "spec.cvlast.CVLExp.Constant.NumberLit",
            "n": "ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff",
            "tag": {
              "scope": {
                "scopeStack": [
                  {
                    "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                  },
                  {
                    "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                    "scopeId": 2
                  }
                ],
                "innerScope": {
                  "scopeStack": [
                    {
                      "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                    }
                  ],
                  "innerScope": {
                    "scopeStack": [
                    ],
                    "innerScope": null
                  }
                }
              },
              "type": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.NumberLiteral",
                "n": "ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff"
              },
              "cvlRange": {
                "#class": "spec.cvlast.CVLRange.Range",
                "specFile": "certora/spec/ERC20.spec",
                "start": {
                  "line": 66,
                  "character": 44
                },
                "end": {
                  "line": 66,
                  "character": 52
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
          "line": 66,
          "character": 4
        },
        "end": {
          "line": 66,
          "character": 53
        }
      }
    }
  ],
  "53": [
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
          "line": 67,
          "character": 4
        },
        "end": {
          "line": 67,
          "character": 30
        }
      }
    }
  ],
  "54": [
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
                        "scopeId": 2
                      }
                    ],
                    "innerScope": {
                      "scopeStack": [
                        {
                          "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                        }
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
                      "line": 67,
                      "character": 4
                    },
                    "end": {
                      "line": 67,
                      "character": 30
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
                      "scopeId": 2
                    }
                  ],
                  "innerScope": {
                    "scopeStack": [
                      {
                        "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                      }
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
                    "line": 67,
                    "character": 12
                  },
                  "end": {
                    "line": 67,
                    "character": 13
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
                    "scopeId": 2
                  }
                ],
                "innerScope": {
                  "scopeStack": [
                    {
                      "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                    }
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
                  "line": 67,
                  "character": 12
                },
                "end": {
                  "line": 67,
                  "character": 13
                }
              }
            }
          },
          "r": {
            "#class": "spec.cvlast.CVLExp.Constant.NumberLit",
            "n": "0",
            "tag": {
              "scope": {
                "scopeStack": [
                  {
                    "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                  },
                  {
                    "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                    "scopeId": 2
                  }
                ],
                "innerScope": {
                  "scopeStack": [
                    {
                      "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                    }
                  ],
                  "innerScope": {
                    "scopeStack": [
                    ],
                    "innerScope": null
                  }
                }
              },
              "type": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.NumberLiteral",
                "n": "0"
              },
              "cvlRange": {
                "#class": "spec.cvlast.CVLRange.Range",
                "specFile": "certora/spec/ERC20.spec",
                "start": {
                  "line": 67,
                  "character": 28
                },
                "end": {
                  "line": 67,
                  "character": 29
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
                  "scopeId": 2
                }
              ],
              "innerScope": {
                "scopeStack": [
                  {
                    "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                  }
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
                "line": 67,
                "character": 12
              },
              "end": {
                "line": 67,
                "character": 29
              }
            }
          }
        },
        "o1": {
          "out": {
            "#class": "vc.data.TACSymbol.Var.Full",
            "namePrefix": "CANON48",
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
                        "scopeId": 2
                      }
                    ],
                    "innerScope": {
                      "scopeStack": [
                        {
                          "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                        }
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
                      "line": 67,
                      "character": 4
                    },
                    "end": {
                      "line": 67,
                      "character": 30
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
                      "scopeId": 2
                    }
                  ],
                  "innerScope": {
                    "scopeStack": [
                      {
                        "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                      }
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
                    "line": 67,
                    "character": 12
                  },
                  "end": {
                    "line": 67,
                    "character": 13
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
                    "scopeId": 2
                  }
                ],
                "innerScope": {
                  "scopeStack": [
                    {
                      "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                    }
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
                  "line": 67,
                  "character": 12
                },
                "end": {
                  "line": 67,
                  "character": 13
                }
              }
            }
          }
        },
        "o2": {
          "out": {
            "#class": "vc.data.TACSymbol.Const",
            "value": "0"
          },
          "exp": {
            "#class": "spec.cvlast.CVLExp.Constant.NumberLit",
            "n": "0",
            "tag": {
              "scope": {
                "scopeStack": [
                  {
                    "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                  },
                  {
                    "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                    "scopeId": 2
                  }
                ],
                "innerScope": {
                  "scopeStack": [
                    {
                      "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                    }
                  ],
                  "innerScope": {
                    "scopeStack": [
                    ],
                    "innerScope": null
                  }
                }
              },
              "type": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.NumberLiteral",
                "n": "0"
              },
              "cvlRange": {
                "#class": "spec.cvlast.CVLRange.Range",
                "specFile": "certora/spec/ERC20.spec",
                "start": {
                  "line": 67,
                  "character": 28
                },
                "end": {
                  "line": 67,
                  "character": 29
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
          "line": 67,
          "character": 4
        },
        "end": {
          "line": 67,
          "character": 30
        }
      }
    }
  ],
  "55": [
    {
      "key": {
        "name": "cvl.exp",
        "type": "spec.CVLExpToTACExprMeta",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "spec.CVLExpToTACExprMeta.UnaryCVLExp",
        "exp": {
          "#class": "spec.cvlast.CVLExp.RelopExp.NeExp",
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
                        "scopeId": 2
                      }
                    ],
                    "innerScope": {
                      "scopeStack": [
                        {
                          "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                        }
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
                      "line": 67,
                      "character": 4
                    },
                    "end": {
                      "line": 67,
                      "character": 30
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
                      "scopeId": 2
                    }
                  ],
                  "innerScope": {
                    "scopeStack": [
                      {
                        "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                      }
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
                    "line": 67,
                    "character": 12
                  },
                  "end": {
                    "line": 67,
                    "character": 13
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
                    "scopeId": 2
                  }
                ],
                "innerScope": {
                  "scopeStack": [
                    {
                      "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                    }
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
                  "line": 67,
                  "character": 12
                },
                "end": {
                  "line": 67,
                  "character": 13
                }
              }
            }
          },
          "r": {
            "#class": "spec.cvlast.CVLExp.Constant.NumberLit",
            "n": "0",
            "tag": {
              "scope": {
                "scopeStack": [
                  {
                    "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                  },
                  {
                    "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                    "scopeId": 2
                  }
                ],
                "innerScope": {
                  "scopeStack": [
                    {
                      "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                    }
                  ],
                  "innerScope": {
                    "scopeStack": [
                    ],
                    "innerScope": null
                  }
                }
              },
              "type": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.NumberLiteral",
                "n": "0"
              },
              "cvlRange": {
                "#class": "spec.cvlast.CVLRange.Range",
                "specFile": "certora/spec/ERC20.spec",
                "start": {
                  "line": 67,
                  "character": 28
                },
                "end": {
                  "line": 67,
                  "character": 29
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
                  "scopeId": 2
                }
              ],
              "innerScope": {
                "scopeStack": [
                  {
                    "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                  }
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
                "line": 67,
                "character": 12
              },
              "end": {
                "line": 67,
                "character": 29
              }
            }
          }
        },
        "o": {
          "out": {
            "#class": "vc.data.TACSymbol.Var.Full",
            "namePrefix": "CANON47!!142",
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
                          "scopeId": 2
                        }
                      ],
                      "innerScope": {
                        "scopeStack": [
                          {
                            "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                          }
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
                        "line": 67,
                        "character": 4
                      },
                      "end": {
                        "line": 67,
                        "character": 30
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
                        "scopeId": 2
                      }
                    ],
                    "innerScope": {
                      "scopeStack": [
                        {
                          "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                        }
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
                      "line": 67,
                      "character": 12
                    },
                    "end": {
                      "line": 67,
                      "character": 13
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
                      "scopeId": 2
                    }
                  ],
                  "innerScope": {
                    "scopeStack": [
                      {
                        "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                      }
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
                    "line": 67,
                    "character": 12
                  },
                  "end": {
                    "line": 67,
                    "character": 13
                  }
                }
              }
            },
            "r": {
              "#class": "spec.cvlast.CVLExp.Constant.NumberLit",
              "n": "0",
              "tag": {
                "scope": {
                  "scopeStack": [
                    {
                      "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                    },
                    {
                      "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                      "scopeId": 2
                    }
                  ],
                  "innerScope": {
                    "scopeStack": [
                      {
                        "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                      }
                    ],
                    "innerScope": {
                      "scopeStack": [
                      ],
                      "innerScope": null
                    }
                  }
                },
                "type": {
                  "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.NumberLiteral",
                  "n": "0"
                },
                "cvlRange": {
                  "#class": "spec.cvlast.CVLRange.Range",
                  "specFile": "certora/spec/ERC20.spec",
                  "start": {
                    "line": 67,
                    "character": 28
                  },
                  "end": {
                    "line": 67,
                    "character": 29
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
                    "scopeId": 2
                  }
                ],
                "innerScope": {
                  "scopeStack": [
                    {
                      "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                    }
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
                  "line": 67,
                  "character": 12
                },
                "end": {
                  "line": 67,
                  "character": 29
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
          "line": 67,
          "character": 4
        },
        "end": {
          "line": 67,
          "character": 30
        }
      }
    }
  ],
  "56": [
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
          "line": 68,
          "character": 4
        },
        "end": {
          "line": 68,
          "character": 27
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
          "id": "recipient",
          "tag": {
            "scope": {
              "scopeStack": [
                {
                  "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                },
                {
                  "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                  "scopeId": 2
                }
              ],
              "innerScope": {
                "scopeStack": [
                  {
                    "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                  }
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
                "line": 68,
                "character": 4
              },
              "end": {
                "line": 68,
                "character": 27
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
          "line": 68,
          "character": 4
        },
        "end": {
          "line": 68,
          "character": 27
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
          "#class": "spec.cvlast.CVLExp.RelopExp.EqExp",
          "l": {
            "#class": "spec.cvlast.CVLExp.VariableExp",
            "id": "recipient",
            "tag": {
              "scope": {
                "scopeStack": [
                  {
                    "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                  },
                  {
                    "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                    "scopeId": 2
                  }
                ],
                "innerScope": {
                  "scopeStack": [
                    {
                      "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                    }
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
                  "line": 68,
                  "character": 4
                },
                "end": {
                  "line": 68,
                  "character": 27
                }
              }
            },
            "twoStateIndex": "NEITHER"
          },
          "r": {
            "#class": "spec.cvlast.CVLExp.Constant.NumberLit",
            "n": "0",
            "tag": {
              "scope": {
                "scopeStack": [
                  {
                    "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                  },
                  {
                    "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                    "scopeId": 2
                  }
                ],
                "innerScope": {
                  "scopeStack": [
                    {
                      "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                    }
                  ],
                  "innerScope": {
                    "scopeStack": [
                    ],
                    "innerScope": null
                  }
                }
              },
              "type": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.NumberLiteral",
                "n": "0"
              },
              "cvlRange": {
                "#class": "spec.cvlast.CVLRange.Range",
                "specFile": "certora/spec/ERC20.spec",
                "start": {
                  "line": 68,
                  "character": 25
                },
                "end": {
                  "line": 68,
                  "character": 26
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
                  "scopeId": 2
                }
              ],
              "innerScope": {
                "scopeStack": [
                  {
                    "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                  }
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
                "line": 68,
                "character": 12
              },
              "end": {
                "line": 68,
                "character": 26
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
            "id": "recipient",
            "tag": {
              "scope": {
                "scopeStack": [
                  {
                    "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                  },
                  {
                    "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                    "scopeId": 2
                  }
                ],
                "innerScope": {
                  "scopeStack": [
                    {
                      "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                    }
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
                  "line": 68,
                  "character": 4
                },
                "end": {
                  "line": 68,
                  "character": 27
                }
              }
            },
            "twoStateIndex": "NEITHER"
          }
        },
        "o2": {
          "out": {
            "#class": "vc.data.TACSymbol.Const",
            "value": "0"
          },
          "exp": {
            "#class": "spec.cvlast.CVLExp.Constant.NumberLit",
            "n": "0",
            "tag": {
              "scope": {
                "scopeStack": [
                  {
                    "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                  },
                  {
                    "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                    "scopeId": 2
                  }
                ],
                "innerScope": {
                  "scopeStack": [
                    {
                      "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                    }
                  ],
                  "innerScope": {
                    "scopeStack": [
                    ],
                    "innerScope": null
                  }
                }
              },
              "type": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.NumberLiteral",
                "n": "0"
              },
              "cvlRange": {
                "#class": "spec.cvlast.CVLRange.Range",
                "specFile": "certora/spec/ERC20.spec",
                "start": {
                  "line": 68,
                  "character": 25
                },
                "end": {
                  "line": 68,
                  "character": 26
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
          "line": 68,
          "character": 4
        },
        "end": {
          "line": 68,
          "character": 27
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
        "#class": "spec.CVLExpToTACExprMeta.UnaryCVLExp",
        "exp": {
          "#class": "spec.cvlast.CVLExp.RelopExp.NeExp",
          "l": {
            "#class": "spec.cvlast.CVLExp.VariableExp",
            "id": "recipient",
            "tag": {
              "scope": {
                "scopeStack": [
                  {
                    "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                  },
                  {
                    "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                    "scopeId": 2
                  }
                ],
                "innerScope": {
                  "scopeStack": [
                    {
                      "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                    }
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
                  "line": 68,
                  "character": 4
                },
                "end": {
                  "line": 68,
                  "character": 27
                }
              }
            },
            "twoStateIndex": "NEITHER"
          },
          "r": {
            "#class": "spec.cvlast.CVLExp.Constant.NumberLit",
            "n": "0",
            "tag": {
              "scope": {
                "scopeStack": [
                  {
                    "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                  },
                  {
                    "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                    "scopeId": 2
                  }
                ],
                "innerScope": {
                  "scopeStack": [
                    {
                      "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                    }
                  ],
                  "innerScope": {
                    "scopeStack": [
                    ],
                    "innerScope": null
                  }
                }
              },
              "type": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.NumberLiteral",
                "n": "0"
              },
              "cvlRange": {
                "#class": "spec.cvlast.CVLRange.Range",
                "specFile": "certora/spec/ERC20.spec",
                "start": {
                  "line": 68,
                  "character": 25
                },
                "end": {
                  "line": 68,
                  "character": 26
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
                  "scopeId": 2
                }
              ],
              "innerScope": {
                "scopeStack": [
                  {
                    "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                  }
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
                "line": 68,
                "character": 12
              },
              "end": {
                "line": 68,
                "character": 26
              }
            }
          }
        },
        "o": {
          "out": {
            "#class": "vc.data.TACSymbol.Var.Full",
            "namePrefix": "CANON51!!145",
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
              "#class": "spec.cvlast.CVLExp.VariableExp",
              "id": "recipient",
              "tag": {
                "scope": {
                  "scopeStack": [
                    {
                      "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                    },
                    {
                      "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                      "scopeId": 2
                    }
                  ],
                  "innerScope": {
                    "scopeStack": [
                      {
                        "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                      }
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
                    "line": 68,
                    "character": 4
                  },
                  "end": {
                    "line": 68,
                    "character": 27
                  }
                }
              },
              "twoStateIndex": "NEITHER"
            },
            "r": {
              "#class": "spec.cvlast.CVLExp.Constant.NumberLit",
              "n": "0",
              "tag": {
                "scope": {
                  "scopeStack": [
                    {
                      "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                    },
                    {
                      "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                      "scopeId": 2
                    }
                  ],
                  "innerScope": {
                    "scopeStack": [
                      {
                        "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                      }
                    ],
                    "innerScope": {
                      "scopeStack": [
                      ],
                      "innerScope": null
                    }
                  }
                },
                "type": {
                  "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.NumberLiteral",
                  "n": "0"
                },
                "cvlRange": {
                  "#class": "spec.cvlast.CVLRange.Range",
                  "specFile": "certora/spec/ERC20.spec",
                  "start": {
                    "line": 68,
                    "character": 25
                  },
                  "end": {
                    "line": 68,
                    "character": 26
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
                    "scopeId": 2
                  }
                ],
                "innerScope": {
                  "scopeStack": [
                    {
                      "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                    }
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
                  "line": 68,
                  "character": 12
                },
                "end": {
                  "line": 68,
                  "character": 26
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
          "line": 68,
          "character": 4
        },
        "end": {
          "line": 68,
          "character": 27
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
          "id": "recipient",
          "tag": {
            "scope": {
              "scopeStack": [
                {
                  "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                },
                {
                  "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                  "scopeId": 2
                }
              ],
              "innerScope": {
                "scopeStack": [
                  {
                    "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                  }
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
                "line": 70,
                "character": 4
              },
              "end": {
                "line": 70,
                "character": 46
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
          "line": 70,
          "character": 4
        },
        "end": {
          "line": 70,
          "character": 46
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
          "id": "amount",
          "tag": {
            "scope": {
              "scopeStack": [
                {
                  "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                },
                {
                  "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                  "scopeId": 2
                }
              ],
              "innerScope": {
                "scopeStack": [
                  {
                    "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                  }
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
              "#class": "spec.cvlast.CVLRange.Range",
              "specFile": "certora/spec/ERC20.spec",
              "start": {
                "line": 70,
                "character": 4
              },
              "end": {
                "line": 70,
                "character": 46
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
          "line": 70,
          "character": 4
        },
        "end": {
          "line": 70,
          "character": 46
        }
      }
    }
  ],
  "62": [
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
          "line": 71,
          "character": 4
        },
        "end": {
          "line": 71,
          "character": 25
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
        "#class": "spec.CVLExpToTACExprMeta.UnaryCVLExp",
        "exp": {
          "#class": "spec.cvlast.CVLExp.UnaryExp.LNotExp",
          "e": {
            "#class": "spec.cvlast.CVLExp.VariableExp",
            "id": "lastReverted",
            "tag": {
              "scope": {
                "scopeStack": [
                  {
                    "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                  },
                  {
                    "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                    "scopeId": 2
                  }
                ],
                "innerScope": {
                  "scopeStack": [
                    {
                      "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                    }
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
                  "line": 71,
                  "character": 4
                },
                "end": {
                  "line": 71,
                  "character": 25
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
                  "scopeId": 2
                }
              ],
              "innerScope": {
                "scopeStack": [
                  {
                    "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                  }
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
                "line": 71,
                "character": 11
              },
              "end": {
                "line": 71,
                "character": 24
              }
            }
          }
        },
        "o": {
          "out": {
            "#class": "vc.data.TACSymbol.Var.Full",
            "namePrefix": "lastReverted!!205",
            "tag": {
              "#class": "tac.Tag.Bool"
            },
            "callIndex": 0,
            "meta": [
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
            ]
          },
          "exp": {
            "#class": "spec.cvlast.CVLExp.VariableExp",
            "id": "lastReverted",
            "tag": {
              "scope": {
                "scopeStack": [
                  {
                    "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                  },
                  {
                    "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                    "scopeId": 2
                  }
                ],
                "innerScope": {
                  "scopeStack": [
                    {
                      "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                    }
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
                  "line": 71,
                  "character": 4
                },
                "end": {
                  "line": 71,
                  "character": 25
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
          "line": 71,
          "character": 4
        },
        "end": {
          "line": 71,
          "character": 25
        }
      }
    }
  ],
  "64": [
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
  "65": [
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
          "line": 71,
          "character": 4
        },
        "end": {
          "line": 71,
          "character": 25
        }
      }
    }
  ],
  "66": [
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
  "67": [
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
          "line": 70,
          "character": 4
        },
        "end": {
          "line": 70,
          "character": 46
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
        "begin": 1636,
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
  "68": [
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
  "69": [
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
          "line": 70,
          "character": 4
        },
        "end": {
          "line": 70,
          "character": 46
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
        "begin": 1629,
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
  "70": [
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
          "line": 70,
          "character": 4
        },
        "end": {
          "line": 70,
          "character": 46
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
        "begin": 11533,
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
    }
  ],
  "71": [
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
  "72": [
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
          "callIndex": 3,
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
  "73": [
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
  "74": [
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
          "line": 70,
          "character": 4
        },
        "end": {
          "line": 70,
          "character": 46
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
        "begin": 11525,
        "len": 71,
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
  "75": [
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
          "line": 70,
          "character": 4
        },
        "end": {
          "line": 70,
          "character": 46
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
  "76": [
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
  "77": [
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
          "line": 70,
          "character": 4
        },
        "end": {
          "line": 70,
          "character": 46
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
              "namePrefix": "R88",
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
                  "value": 1012
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
                "namePrefix": "R88",
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
                    "value": 1012
                  }
                ]
              },
              "baseSlot": {
                "#class": "vc.data.TACSymbol.Var.Full",
                "namePrefix": "CANON112",
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
                "namePrefix": "CANON111",
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
      "value": 1014
    }
  ],
  "79": [
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
          "callIndex": 3,
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
  "80": [
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
          "line": 70,
          "character": 4
        },
        "end": {
          "line": 70,
          "character": 46
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
        "begin": 11716,
        "len": 108,
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
        "name": "cvl.range",
        "type": "spec.cvlast.CVLRange",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "spec.cvlast.CVLRange.Range",
        "specFile": "certora/spec/ERC20.spec",
        "start": {
          "line": 70,
          "character": 4
        },
        "end": {
          "line": 70,
          "character": 46
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
  "82": [
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
          "line": 70,
          "character": 4
        },
        "end": {
          "line": 70,
          "character": 46
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
      "value": 1013
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
              "namePrefix": "R88",
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
                  "value": 1011
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
                "namePrefix": "R88",
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
                    "value": 1011
                  }
                ]
              },
              "baseSlot": {
                "#class": "vc.data.TACSymbol.Var.Full",
                "namePrefix": "CANON115",
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
                "namePrefix": "CANON114",
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
      "value": 1013
    }
  ],
  "85": [
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
          "line": 70,
          "character": 4
        },
        "end": {
          "line": 70,
          "character": 46
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
  "86": [
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
          "line": 70,
          "character": 4
        },
        "end": {
          "line": 70,
          "character": 46
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
  "87": [
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
  "88": [
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
        "name": "tac.stack.height",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 1011
    }
  ],
  "89": [
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
          "line": 70,
          "character": 4
        },
        "end": {
          "line": 70,
          "character": 46
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
  "90": [
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
  "91": [
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
              "namePrefix": "R188",
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
                  "value": 1011
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
                "namePrefix": "R188",
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
                    "value": 1011
                  }
                ]
              },
              "baseSlot": {
                "#class": "vc.data.TACSymbol.Var.Full",
                "namePrefix": "CANON121",
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
                "namePrefix": "CANON120",
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
      "value": 1013
    }
  ],
  "92": [
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
          "line": 70,
          "character": 4
        },
        "end": {
          "line": 70,
          "character": 46
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
        "begin": 13526,
        "len": 74,
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
  "93": [
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
      "value": 1007
    }
  ],
  "94": [
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
          "line": 70,
          "character": 4
        },
        "end": {
          "line": 70,
          "character": 46
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
        "begin": 13517,
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
  "95": [
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
          "line": 70,
          "character": 4
        },
        "end": {
          "line": 70,
          "character": 46
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
  "96": [
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
  "97": [
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
          "line": 70,
          "character": 4
        },
        "end": {
          "line": 70,
          "character": 46
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
        "begin": 14123,
        "len": 54,
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
  "98": [
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
      "value": 1004
    }
  ],
  "99": [
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
          "line": 70,
          "character": 4
        },
        "end": {
          "line": 70,
          "character": 46
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
        "begin": 15024,
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
  "100": [
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
          "line": 70,
          "character": 4
        },
        "end": {
          "line": 70,
          "character": 46
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
        "begin": 13641,
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
  "101": [
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
  "102": [
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
          "line": 70,
          "character": 4
        },
        "end": {
          "line": 70,
          "character": 46
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
  "103": [
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
          "line": 70,
          "character": 4
        },
        "end": {
          "line": 70,
          "character": 46
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
        "begin": 11445,
        "len": 70,
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
  ]
}