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
		CANON89:JSON{"name":"CANON89","paramSorts":[],"returnSort":{"#class":"tac.Tag.Int"},"attribute":"Ghost","cvlResultType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Mathint"},"cvlParamTypes":[],"declarationName":"CANON89"}
		I5:JSON{"name":"I5","paramSorts":[],"returnSort":{"#class":"tac.Tag.Int"},"attribute":"Ghost","cvlResultType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Mathint"},"cvlParamTypes":[],"declarationName":"CANON89"}
	}
	tacM0x20@1:bv256
	tacM0x20@3:bv256
	tacCaller@2:bv256
	tacCalldatabufCANON0@2:bv256
	tacMCANON0!!1:bytemap
	tacM0x0!!45:bv256
	tacM0x0!!48:bv256
	tacM0x0!!79:bv256
	tacM0x0!!82:bv256
	tacAddress!!28:bv256
	tacAddress!!62:bv256
	tacOrigin!!120:bv256
	tacCallvalue@2:bv256
	CANON135!!153:bool
	lastReverted:bool
	lastReverted@1:bool
	lastReverted@2:bool
	lastReverted@3:bool
	tacM0x0!!169:bv256
	tacM0x0!!174:bv256
	tacExtcodesize!!0:wordmap
	CANON28!!3:wordmap
	tacRC!!210:bv256
	CANON82!!4:wordmap
	tacCalldatasize@1:bv256
	tacCalldatasize@2:bv256
	tacCalldatasize@3:bv256
	tacReturndata@2:bytemap
	tacReturnsize@2:bv256
	tacCalldatasize!!102:bv256
	tacMCANON2havocme3782@2:bytemap
	tacCond:bool
	tacCond@2:bool
	tacM0x0@1:bv256
	tacM0x0@2:bv256
	tacM0x0@3:bv256
	tacRC@2:bv256
	ReachabilityCertora2_0_0_2_0_0:bool
	tacExtcodesize:wordmap
	CANON100@2:bool
	CANON101@2:bv256
	CANON102:bool
	CANON103:bv256
	CANON104:bv256
	CANON105:bool
	CANON106:bool
	CANON107@2:bool
	CANON108@2:bv256
	CANON109@2:bv256
	CANON110@2:int
	CANON111@2:bv256
	CANON112@2:bv256
	CANON113@2:bool
	CANON114@2:bool
	CANON115:int
	CANON116:int
	CANON117:bool
	CANON118:bool
	CANON119:bool
	CANON120:bv256
	CANON121:bool
	CANON122:bool
	CANON123:bv256
	CANON124:bool
	CANON125:bool
	CANON126:bool
	CANON127:int
	CANON128:int
	CANON129:int
	CANON130:bool
	CANON131:int
	CANON132:int
	CANON133:bool
	CANON135:bool
	CANON136:int
	CANON137:int
	CANON138:bool
	CANON139:bool
	CANON140:bool
	CANON141:bool
	CANON142:bool
	tacSighash!!7:bv256
	tacSighash!!8:bv256
	tacSighash!!9:bv256
	tacCalldatasize!!19:bv256
	tacCalldatasize!!53:bv256
	tacMCANON0havocme3783@2:bytemap
	tacMCANON0@2:bytemap
	tacMCANON1@2:bytemap
	tacMCANON2@2:bytemap
	tacBalance:wordmap
	tacTimestamp!!130:bv256
	tacNumber@2:bv256
	tacBalance!!2:wordmap
	I5:int
	R6:bv256
	B10:bool
	B11:bool
	B12:bool
	B14:bool
	B15:bool
	B16:bool
	B20:bool
	B21:bool
	B22:bool
	B24:bool
	B25:bool
	B27:bool
	B30:bool
	B31:bool
	B32:bool
	B33:bool
	B34:bool
	B35:bool
	B36:bool
	B37:bool
	B39:bool
	B41:bool
	B43:bool
	B54:bool
	B55:bool
	B56:bool
	B58:bool
	B59:bool
	B61:bool
	B64:bool
	B65:bool
	B66:bool
	B67:bool
	B68:bool
	B69:bool
	B70:bool
	B71:bool
	B73:bool
	B75:bool
	B77:bool
	B87:bool
	B88:bool
	B89:bool
	B90:bool
	B91:bool
	B92:bool
	B93:bool
	B94:bool
	I17:int
	I18:int
	I95:int
	I96:int
	I97:int
	I98:int
	I99:int
	R13:bv256
	R23:bv256
	R26:bv256
	R29:bv256
	R38:bv256
	R40:bv256
	R42:bv256
	R44:bv256
	R46:(uninterp) skey
	R47:bv256
	R50:(uninterp) skey
	R51:bv256
	R52:bv256
	R57:bv256
	R60:bv256
	R63:bv256
	R72:bv256
	R74:bv256
	R76:bv256
	R78:bv256
	R80:(uninterp) skey
	R81:bv256
	R84:(uninterp) skey
	R85:bv256
	R86:bv256
	B103:bool
	B104:bool
	B107:bool
	B110:bool
	B112:bool
	B115:bool
	B118:bool
	B121:bool
	B123:bool
	B126:bool
	B128:bool
	B131:bool
	B133:bool
	B136:bool
	B145:bool
	B149:bool
	B156:bool
	B159:bool
	B160:bool
	B161:bool
	B162:bool
	B163:bool
	B164:bool
	B166:bool
	B172:bool
	B177:bool
	B186:bool
	B188:bool
	B190:bool
	B197:bool
	B206:bool
	B217:bool
	B221:bool
	B222:bool
	B226:bool
	B227:bool
	I106:int
	I111:int
	I117:int
	I122:int
	I127:int
	I132:int
	I135:int
	I141:int
	I147:int
	I148:int
	I150:int
	I151:int
	I154:int
	I155:int
	I180:int
	I181:int
	I193:int
	I202:int
	I218:int
	I219:int
	M100:bytemap
	R101:bv256
	R105:bv256
	R108:bv256
	R113:bv256
	R119:bv256
	R124:bv256
	R129:bv256
	R134:bv256
	R137:bv256
	R138:bv256
	R139:bv256
	R140:bv256
	R143:bv256
	R144:bv256
	R158:bv256
	R165:bv256
	R167:bv256
	R168:bv256
	R170:(uninterp) skey
	R171:bv256
	R173:bv256
	R175:(uninterp) skey
	R176:bv256
	R178:bv256
	R179:bv256
	R182:bv256
	R183:bv256
	R184:bv256
	R185:bv256
	R187:bv256
	R191:bv256
	R192:bv256
	R195:bv256
	R196:bv256
	R198:bv256
	R199:bv256
	R200:bv256
	R201:bv256
	R204:bv256
	R205:bv256
	R213:bv256
	R216:bv256
	R220:bv256
	R223:bv256
	R224:bv256
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
	tacCallvalue!!114:bv256
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
	CANON82:wordmap
	CANON87:bv256
	CANON88:int
	CANON89:int
	CANON90:int
	CANON91:int
	CANON92:int
	CANON93@2:bv256
	CANON94@2:bv256
	CANON95@2:bv256
	CANON96@2:bv256
	CANON97@2:int
	CANON98@2:bv256
	CANON99@2:bv256
	tacCondCANON0@2:bool
	tacCondCANON1@2:bool
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
	LCANON29@2:bool
	LCANON30@2:bv256
	LCANON31@2:bv256
	LCANON32@2:bv256
	LCANON33@2:bv256
	LCANON34@2:bv256
	LCANON35@2:bool
	LCANON36@2:bv256
	LCANON37@2:bv256
	LCANON38@2:bv256
	LCANON39@2:bv256
	LCANON40@2:bool
	LCANON41@2:bv256
	LCANON42@2:bv256
	LCANON43@2:bv256
	LCANON44@2:bv256
	LCANON45@2:bv256
	LCANON46@2:bv256
	LCANON47@2:bv256
	LCANON48@2:bv256
	LCANON49@2:bool
	LCANON50@2:bv256
	tacContractAtCANON0:bv256
	tacM0x20!!49:bv256
	tacM0x20!!83:bv256
	lastHasThrown:bool
	lastHasThrown@1:bool
	lastHasThrown@2:bool
	lastHasThrown@3:bool
	CANON133!!152:bool
	tacAddress!!116:bv256
	tacReturndata!!208:bytemap
	tacReturndata!!215:bytemap
	ReachabilityCertora2029_1018_0_2_0_3:bool
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
	tacCond!!189:bool
	tacCond!!211:bool
	tacCaller!!109:bv256
	tacBalance!!142:wordmap
	tacBalance!!146:wordmap
	tacBalance!!194:wordmap
	tacBalance!!203:wordmap
	tacBalance!!207:wordmap
	tacBalance!!225:wordmap
	tacBalance!!228:wordmap
	tacTimestamp@2:bv256
	CANON142!!157:bool
	tacSighash@1:bv256
	tacSighash@2:bv256
	tacSighash@3:bv256
	tacNumber!!125:bv256
	tacReturnsize!!209:bv256
	tacReturnsize!!212:bv256
	tacReturnsize!!214:bv256
}
Program {
	Block 0_0_0_0_0_0 Succ [0_0_0_1_0_0] {
		AssignHavocCmd tacExtcodesize!!0:0
		AssignExpCmd tacMCANON0!!1:1 ByteMapDefinition(i.3785:bv256 -> 0x0 )
		AssignHavocCmd tacBalance!!2:2
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
		AssignHavocCmd CANON50:15
		AssignHavocCmd CANON82!!4:16
		AssignHavocCmd R6:17
		AssignHavocCmd tacSighash!!7:18
		AssignHavocCmd tacSighash!!8:18
		AssignHavocCmd tacSighash!!9:18
		AssignExpCmd CANON0:19 0x2e1a7d4d
		AssignExpCmd CANON1:20 false
		AssignExpCmd CANON2:21 false
		AssignExpCmd CANON3:22 false
		AssignExpCmd CANON4:23 0x1
		AssignExpCmd CANON5:24 false
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
		AssignExpCmd B10:25 Gt(Select(tacExtcodesize!!0:0 Apply(to_skey:bif R6:17) ) 0x0 )
		AssumeCmd B10:25
		AnnotationCmd JSON{"key":{"name":"cvl.label.end","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		AnnotationCmd JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Message","s":"assumptions about contracts' addresses"}}
		NopCmd
		AssumeExpCmd Gt(R6:17 0x0 )
		NopCmd
		AssumeExpCmd Le(R6:17 0xffffffffffffffffffffffffffffffffffffffff )
		AnnotationCmd JSON{"key":{"name":"cvl.label.end","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		AnnotationCmd JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Message","s":"assumptions about starting balances"}}
		AssignExpCmd R13:25 Select(tacBalance!!2:2 Apply(to_skey:bif R6:17) )
		NopCmd
		AssumeExpCmd Ge(R13:25 0x0 )
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
		AnnotationCmd:26 JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Cmd","cmd":{"cmd_type":"spec.cvlast.CVLCmd.Simple.Definition","cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/spec/ERC20.spec","start":{"line":96,"character":4},"end":{"line":96,"character":58}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Mathint"},"idL":[{"#class":"spec.cvlast.CVLLhs.Id","cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/spec/ERC20.spec","start":{"line":96,"character":4},"end":{"line":96,"character":28}},"id":"allowance_before","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":6}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Mathint"},"cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/spec/ERC20.spec","start":{"line":96,"character":4},"end":{"line":96,"character":58}}}}],"exp":{"#class":"spec.cvlast.CVLExp.ApplyExp.ContractFunction.Concrete","methodIdWithCallContext":{"#class":"spec.cvlast.ConcreteMethod","signature":{"#class":"spec.cvlast.ExternalQualifiedMethodSignature.ExternalQualifiedMethodSig","wrapped":{"#class":"spec.cvlast.QualifiedMethodSignature.QualifiedMethodSig","qualifiedMethodName":{"#class":"spec.cvlast.QualifiedFunction","host":{"name":"ERC20"},"methodId":"allowance"},"params":[{"#class":"spec.cvlast.VMParam.Named","name":"owner","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$address"}},{"#class":"spec.cvlast.VMParam.Named","name":"spender","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$address"}}],"res":[{"#class":"spec.cvlast.VMParam.Unnamed","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256}}]},"sighashInt":{"n":"dd62ed3e"}}},"args":[{"#class":"spec.cvlast.CVLExp.VariableExp","id":"holder","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":6}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"},"cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/spec/ERC20.spec","start":{"line":96,"character":4},"end":{"line":96,"character":58}}},"twoStateIndex":"NEITHER"},{"#class":"spec.cvlast.CVLExp.VariableExp","id":"spender","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":6}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"},"cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/spec/ERC20.spec","start":{"line":96,"character":4},"end":{"line":96,"character":58}}},"twoStateIndex":"NEITHER"}],"noRevert":true,"storage":{"#class":"spec.cvlast.CVLExp.VariableExp","id":"lastStorage","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":6}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.VMInternal.BlockchainState"},"cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/spec/ERC20.spec","start":{"line":96,"character":4},"end":{"line":96,"character":58}}},"twoStateIndex":"NEITHER"},"isWhole":false,"tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":6}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.VM","descriptor":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256},"context":{"#class":"spec.cvlast.typedescriptors.FromVMContext.ReturnValue"}},"cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/spec/ERC20.spec","start":{"line":96,"character":31},"end":{"line":96,"character":40}},"annotation":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.CallResolution$DirectPassing","target":{"methodSignature":{"#class":"spec.cvlast.ExternalQualifiedMethodSignature.ExternalQualifiedMethodSig","wrapped":{"#class":"spec.cvlast.QualifiedMethodSignature.QualifiedMethodSig","qualifiedMethodName":{"#class":"spec.cvlast.QualifiedFunction","host":{"name":"ERC20"},"methodId":"allowance"},"params":[{"#class":"spec.cvlast.VMParam.Named","name":"owner","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$address"}},{"#class":"spec.cvlast.VMParam.Named","name":"spender","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$address"}}],"res":[{"#class":"spec.cvlast.VMParam.Unnamed","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256}}]},"sighashInt":{"n":"dd62ed3e"}},"definitelyNonPayable":true,"annotation":{"visibility":"EXTERNAL","envFree":true,"library":false},"stateMutability":"view","tag":{"#class":"spec.cvlast.CVLImportedFunctionTag.WithMethodInfo","evmMethodInfo":{"sigHash":"dd62ed3e","name":"allowance","argTypes":[{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.address"},{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.address"}],"resultTypes":[{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256}],"stateMutability":"view","envfreeInfo":{"#class":"bridge.EnvfreeInfo.Unknown"},"isConstant":false,"paramNames":["owner","spender"],"isLibrary":false}}},"hasEnv":false}}},"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":6}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}}}}}
		AssignExpCmd:27 I17 CANON12:3
		AssignExpCmd:28 I18 CANON13:4
	}
	Block 0_0_0_1_0_0 Succ [1_0_0_0_0_0] {
		AnnotationCmd:26 JSON{"key":{"name":"call.trace.push","type":"analysis.icfg.Inliner$CallStack$PushRecord","erasureStrategy":"Canonical"},"value":"rO0ABXNyACphbmFseXNpcy5pY2ZnLklubGluZXIkQ2FsbFN0YWNrJFB1c2hSZWNvcmSX8+DCTLCH+AIAA0kACGNhbGxlZUlkTAAGY2FsbGVldAATTHZjL2RhdGEvTWV0aG9kUmVmO0wAB3N1bW1hcnl0ABVMdmMvZGF0YS9DYWxsU3VtbWFyeTt4cAAAAAFzcgARdmMuZGF0YS5NZXRob2RSZWbJlJTzzU9pGAIAA0wABGF0dHJ0ABdMc2NlbmUvTWV0aG9kQXR0cmlidXRlO0wACmNvbnRyYWN0SWR0ABZMamF2YS9tYXRoL0JpZ0ludGVnZXI7TAAHc2lnSGFzaHQAEExldm0vU2lnaGFzaEludDt4cHNyABxzY2VuZS5NZXRob2RBdHRyaWJ1dGUkQ29tbW9uNHjdebdr9XMCAAB4cgAVc2NlbmUuTWV0aG9kQXR0cmlidXRlcYg2pYWutuUCAAB4cHNyABRqYXZhLm1hdGguQmlnSW50ZWdlcoz8nx+pO/sdAwAGSQAIYml0Q291bnRJAAliaXRMZW5ndGhJABNmaXJzdE5vbnplcm9CeXRlTnVtSQAMbG93ZXN0U2V0Qml0SQAGc2lnbnVtWwAJbWFnbml0dWRldAACW0J4cgAQamF2YS5sYW5nLk51bWJlcoaslR0LlOCLAgAAeHD///////////////7////+AAAAAXVyAAJbQqzzF/gGCFTgAgAAeHAAAAAQzkYEoAAAAAAAAAAAAAAAA3hzcgAOZXZtLlNpZ2hhc2hJbnRUdcqNMXEgeAIAAUwAAW5xAH4ABnhwc3EAfgAM///////////////+/////gAAAAF1cQB+ABAAAAAE3WLtPnhw"}
		AssignHavocCmd:26 tacCalldatasize!!19:29
		NopCmd
		AssumeExpCmd Apply(add_noofl:bif 0x4 0x40)
		NopCmd
		AssumeExpCmd Apply(add_noofl:bif 0x4 0x0)
		AssignExpCmd:26 B22 LAnd(Ge(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff I17 ) Le(0x0 I17 ) )
		AssertCmd:26 B22 "sanity bounds check on cvl to vm encoding of certoraArg14071410:int failed"
		AssignExpCmd:26 R23 Apply(safe_math_narrow:bif I17)
		NopCmd
		AssumeExpCmd Apply(add_noofl:bif 0x4 0x20)
		AssignExpCmd:26 B25 LAnd(Ge(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff I18 ) Le(0x0 I18 ) )
		AssertCmd:26 B25 "sanity bounds check on cvl to vm encoding of certoraArg14111412:int failed"
		AssignExpCmd:26 R26 Apply(safe_math_narrow:bif I18)
		NopCmd
		AssumeExpCmd Eq(0x44 tacCalldatasize!!19:29 )
		LabelCmd:26 "Start procedure ERC20-allowance(address,address)"
		AnnotationCmd:26 JSON{"key":{"name":"fps.free-pointer-is-scalarized","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true}
		AssignExpCmd:26 R29:25 Select(tacExtcodesize!!0:0 Apply(to_skey:bif R6:30) )
		NopCmd
		AssumeExpCmd Gt(R29:25 0x0 )
		AnnotationCmd:26 JSON{"key":{"name":"internal.func.finder.info","type":"analysis.ip.InternalFunctionFinderReport","erasureStrategy":"Erased"},"value":"rO0ABXNyAChhbmFseXNpcy5pcC5JbnRlcm5hbEZ1bmN0aW9uRmluZGVyUmVwb3J0ian+bYn1VdACAAFMABN1bnJlc29sdmVkRnVuY3Rpb25zdAAPTGphdmEvdXRpbC9TZXQ7eHBzcgAhZGF0YXN0cnVjdHVyZXMuTGlua2VkQXJyYXlIYXNoU2V0AAAAAAAAAAEDAAJGAApsb2FkRmFjdG9yTAAJaGFzaFRhYmxldAAuTGRhdGFzdHJ1Y3R1cmVzL2FycmF5aGFzaHRhYmxlL0FycmF5SGFzaFRhYmxlO3hwdwgAAAAAQAAAAHg="}
		AnnotationCmd:26 JSON{"key":{"name":"fps.free-pointer-is-scalarized","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true}
		NopCmd
		AssumeExpCmd LNot(Lt(tacCalldatasize!!19:29 0x4 ) )
		NopCmd
		AssumeExpCmd LNot(Gt(0x70a08231 tacSighash!!7:18 ) )
		NopCmd
		AssumeExpCmd LNot(Gt(0xa9059cbb tacSighash!!7:18 ) )
		NopCmd
		AssumeExpCmd LNot(Eq(0xa9059cbb tacSighash!!7:18 ) )
		NopCmd
		AssumeExpCmd LNot(Eq(0xb2bdfa7b tacSighash!!7:18 ) )
		NopCmd
		AssumeExpCmd LNot(Eq(0xd0e30db0 tacSighash!!7:18 ) )
		NopCmd
		AssumeExpCmd Eq(0xdd62ed3e tacSighash!!7:18 )
		AssumeCmd:31 true
		AssignExpCmd:32 R38:33 Sub(tacCalldatasize!!19:29 0x4 )
		NopCmd
		AssumeExpCmd LNot(Slt(R38:33 0x40 ) )
		NopCmd
		AssumeExpCmd Le(R23 0xffffffffffffffffffffffffffffffffffffffff )
		NopCmd
		AssumeExpCmd Le(R26 0xffffffffffffffffffffffffffffffffffffffff )
		AnnotationCmd:26 JSON{"key":{"name":"internal.func.start","type":"analysis.ip.InternalFuncStartAnnotation","erasureStrategy":"CallTrace"},"value":{"id":0,"startPc":4858,"args":[{"s":{"namePrefix":"R23","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1012}]},"offset":1,"sort":"SCALAR"},{"s":{"namePrefix":"R26","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1012}]},"offset":2,"sort":"SCALAR"}],"methodSignature":{"#class":"spec.cvlast.QualifiedMethodSignature.QualifiedMethodSig","qualifiedMethodName":{"#class":"spec.cvlast.QualifiedFunction","host":{"name":"ERC20"},"methodId":"allowance"},"params":[{"#class":"spec.cvlast.VMParam.Named","name":"owner","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$address"}},{"#class":"spec.cvlast.VMParam.Named","name":"spender","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$address"}}],"res":[{"#class":"spec.cvlast.VMParam.Unnamed","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256}}]},"stackOffsetToArgPos":{"1":0,"2":1},"callSiteSrc":{"source":0,"begin":5647,"len":535,"jumpType":"ENTER","address":"ce4604a0000000000000000000000003","sourceContext":{"indexToFilepath":{"0":"contracts/ERC20.sol","1":"contracts/IERC20.sol","2":"contracts/IERC20Metadata.sol"},"sourceDir":".post_autofinders.0"}}}}
		AssignExpCmd:34 R46:35 Apply(hash_3_keccak:bif Apply(skey_basic:bif 0x40) Apply(to_skey:bif R23:36) Apply(skey_basic:bif 0x1))
		AssignExpCmd:37 R50:35 Apply(hash_3_keccak:bif Apply(skey_basic:bif 0x40) Apply(to_skey:bif R26:36) R46:38)
		AssignExpCmd:39 R51:35 Select(CANON28!!3:5 R50:40 )
		AnnotationCmd:26 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet","value":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R51","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1019}]},"displayPath":{"#class":"analysis.storage.DisplayPath.MapAccess","key":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R26","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1017}]},"keyTyp":{"#class":"tac.TACStorageType.IntegralType","typeLabel":"address","numBytes":"14","descriptor":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$address"},"lowerBound":null,"upperBound":null},"base":{"#class":"analysis.storage.DisplayPath.MapAccess","key":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R23","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1017}]},"keyTyp":{"#class":"tac.TACStorageType.IntegralType","typeLabel":"address","numBytes":"14","descriptor":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$address"},"lowerBound":null,"upperBound":null},"base":{"#class":"analysis.storage.DisplayPath.Root","name":"_allowances"}}},"storageType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256},"contractInstance":"ce4604a0000000000000000000000003","linkableStorageReadId":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet.None"}}}
		AnnotationCmd:26 JSON{"key":{"name":"internal.func.end","type":"analysis.ip.InternalFuncExitAnnotation","erasureStrategy":"Canonical"},"value":{"id":0,"rets":[{"s":{"namePrefix":"R51","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1023}]},"offset":0}],"functionLayout":{"0":{"#class":"analysis.ip.InternalFuncValueLocation.Scalar"}}}}
		AnnotationCmd:26 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.EVMFunctionReturnWrite","returnbufOffset":"0","returnValueSym":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R51","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1023}]},"callIndex":1}}
		AnnotationCmd:26 JSON{"key":{"name":"tac.return.path","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		LabelCmd:26 "End procedure ERC20-allowance(address,address)"
		AssignExpCmd:26 CANON33:41 R51:35
		AnnotationCmd:26 JSON{"key":{"name":"call.trace.pop","type":"analysis.icfg.Inliner$CallStack$PopRecord","erasureStrategy":"Canonical"},"value":"rO0ABXNyAClhbmFseXNpcy5pY2ZnLklubGluZXIkQ2FsbFN0YWNrJFBvcFJlY29yZPAPfwSLdCWJAgABSQAIY2FsbGVlSWR4cAAAAAE="}
	}
	Block 0_0_0_3_0_0 Succ [4_0_0_0_0_0] {
		AnnotationCmd:42 JSON{"key":{"name":"call.trace.push","type":"analysis.icfg.Inliner$CallStack$PushRecord","erasureStrategy":"Canonical"},"value":"rO0ABXNyACphbmFseXNpcy5pY2ZnLklubGluZXIkQ2FsbFN0YWNrJFB1c2hSZWNvcmSX8+DCTLCH+AIAA0kACGNhbGxlZUlkTAAGY2FsbGVldAATTHZjL2RhdGEvTWV0aG9kUmVmO0wAB3N1bW1hcnl0ABVMdmMvZGF0YS9DYWxsU3VtbWFyeTt4cAAAAANzcgARdmMuZGF0YS5NZXRob2RSZWbJlJTzzU9pGAIAA0wABGF0dHJ0ABdMc2NlbmUvTWV0aG9kQXR0cmlidXRlO0wACmNvbnRyYWN0SWR0ABZMamF2YS9tYXRoL0JpZ0ludGVnZXI7TAAHc2lnSGFzaHQAEExldm0vU2lnaGFzaEludDt4cHNyABxzY2VuZS5NZXRob2RBdHRyaWJ1dGUkQ29tbW9uNHjdebdr9XMCAAB4cgAVc2NlbmUuTWV0aG9kQXR0cmlidXRlcYg2pYWutuUCAAB4cHNyABRqYXZhLm1hdGguQmlnSW50ZWdlcoz8nx+pO/sdAwAGSQAIYml0Q291bnRJAAliaXRMZW5ndGhJABNmaXJzdE5vbnplcm9CeXRlTnVtSQAMbG93ZXN0U2V0Qml0SQAGc2lnbnVtWwAJbWFnbml0dWRldAACW0J4cgAQamF2YS5sYW5nLk51bWJlcoaslR0LlOCLAgAAeHD///////////////7////+AAAAAXVyAAJbQqzzF/gGCFTgAgAAeHAAAAAQzkYEoAAAAAAAAAAAAAAAA3hzcgAOZXZtLlNpZ2hhc2hJbnRUdcqNMXEgeAIAAUwAAW5xAH4ABnhwc3EAfgAM///////////////+/////gAAAAF1cQB+ABAAAAAE3WLtPnhw"}
		AssignHavocCmd:42 tacCalldatasize!!53:29
		NopCmd
		AssumeExpCmd Apply(add_noofl:bif 0x4 0x40)
		NopCmd
		AssumeExpCmd Apply(add_noofl:bif 0x4 0x0)
		AssignExpCmd:42 B56 LAnd(Ge(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff I218 ) Le(0x0 I218 ) )
		AssertCmd:42 B56 "sanity bounds check on cvl to vm encoding of certoraArg23342335:int failed"
		AssignExpCmd:42 R57 Apply(safe_math_narrow:bif I218)
		NopCmd
		AssumeExpCmd Apply(add_noofl:bif 0x4 0x20)
		AssignExpCmd:42 B59 LAnd(Ge(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff I219 ) Le(0x0 I219 ) )
		AssertCmd:42 B59 "sanity bounds check on cvl to vm encoding of certoraArg23362337:int failed"
		AssignExpCmd:42 R60 Apply(safe_math_narrow:bif I219)
		NopCmd
		AssumeExpCmd Eq(0x44 tacCalldatasize!!53:29 )
		LabelCmd:42 "Start procedure ERC20-allowance(address,address)"
		AnnotationCmd:42 JSON{"key":{"name":"fps.free-pointer-is-scalarized","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true}
		AssignExpCmd:42 R63:25 Select(tacExtcodesize!!0:0 Apply(to_skey:bif R6:30) )
		NopCmd
		AssumeExpCmd Gt(R63:25 0x0 )
		AnnotationCmd:42 JSON{"key":{"name":"internal.func.finder.info","type":"analysis.ip.InternalFunctionFinderReport","erasureStrategy":"Erased"},"value":"rO0ABXNyAChhbmFseXNpcy5pcC5JbnRlcm5hbEZ1bmN0aW9uRmluZGVyUmVwb3J0ian+bYn1VdACAAFMABN1bnJlc29sdmVkRnVuY3Rpb25zdAAPTGphdmEvdXRpbC9TZXQ7eHBzcgAhZGF0YXN0cnVjdHVyZXMuTGlua2VkQXJyYXlIYXNoU2V0AAAAAAAAAAEDAAJGAApsb2FkRmFjdG9yTAAJaGFzaFRhYmxldAAuTGRhdGFzdHJ1Y3R1cmVzL2FycmF5aGFzaHRhYmxlL0FycmF5SGFzaFRhYmxlO3hwdwgAAAAAQAAAAHg="}
		AnnotationCmd:42 JSON{"key":{"name":"fps.free-pointer-is-scalarized","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true}
		NopCmd
		AssumeExpCmd LNot(Lt(tacCalldatasize!!53:29 0x4 ) )
		NopCmd
		AssumeExpCmd LNot(Gt(0x70a08231 tacSighash!!9:18 ) )
		NopCmd
		AssumeExpCmd LNot(Gt(0xa9059cbb tacSighash!!9:18 ) )
		NopCmd
		AssumeExpCmd LNot(Eq(0xa9059cbb tacSighash!!9:18 ) )
		NopCmd
		AssumeExpCmd LNot(Eq(0xb2bdfa7b tacSighash!!9:18 ) )
		NopCmd
		AssumeExpCmd LNot(Eq(0xd0e30db0 tacSighash!!9:18 ) )
		NopCmd
		AssumeExpCmd Eq(0xdd62ed3e tacSighash!!9:18 )
		AssumeCmd:43 true
		AssignExpCmd:44 R72:33 Sub(tacCalldatasize!!53:29 0x4 )
		NopCmd
		AssumeExpCmd LNot(Slt(R72:33 0x40 ) )
		NopCmd
		AssumeExpCmd Le(R57 0xffffffffffffffffffffffffffffffffffffffff )
		NopCmd
		AssumeExpCmd Le(R60 0xffffffffffffffffffffffffffffffffffffffff )
		AnnotationCmd:42 JSON{"key":{"name":"internal.func.start","type":"analysis.ip.InternalFuncStartAnnotation","erasureStrategy":"CallTrace"},"value":{"id":1,"startPc":4858,"args":[{"s":{"namePrefix":"R57","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1012}]},"offset":1,"sort":"SCALAR"},{"s":{"namePrefix":"R60","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1012}]},"offset":2,"sort":"SCALAR"}],"methodSignature":{"#class":"spec.cvlast.QualifiedMethodSignature.QualifiedMethodSig","qualifiedMethodName":{"#class":"spec.cvlast.QualifiedFunction","host":{"name":"ERC20"},"methodId":"allowance"},"params":[{"#class":"spec.cvlast.VMParam.Named","name":"owner","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$address"}},{"#class":"spec.cvlast.VMParam.Named","name":"spender","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$address"}}],"res":[{"#class":"spec.cvlast.VMParam.Unnamed","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256}}]},"stackOffsetToArgPos":{"1":0,"2":1},"callSiteSrc":{"source":0,"begin":5647,"len":535,"jumpType":"ENTER","address":"ce4604a0000000000000000000000003","sourceContext":{"indexToFilepath":{"0":"contracts/ERC20.sol","1":"contracts/IERC20.sol","2":"contracts/IERC20Metadata.sol"},"sourceDir":".post_autofinders.0"}}}}
		AssignExpCmd:45 R80:35 Apply(hash_3_keccak:bif Apply(skey_basic:bif 0x40) Apply(to_skey:bif R57:36) Apply(skey_basic:bif 0x1))
		AssignExpCmd:46 R84:35 Apply(hash_3_keccak:bif Apply(skey_basic:bif 0x40) Apply(to_skey:bif R60:36) R80:38)
		AssignExpCmd:47 R85:35 Select(CANON28!!3:5 R84:48 )
		AnnotationCmd:42 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet","value":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R85","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1019}]},"displayPath":{"#class":"analysis.storage.DisplayPath.MapAccess","key":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R60","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1017}]},"keyTyp":{"#class":"tac.TACStorageType.IntegralType","typeLabel":"address","numBytes":"14","descriptor":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$address"},"lowerBound":null,"upperBound":null},"base":{"#class":"analysis.storage.DisplayPath.MapAccess","key":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R57","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1017}]},"keyTyp":{"#class":"tac.TACStorageType.IntegralType","typeLabel":"address","numBytes":"14","descriptor":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$address"},"lowerBound":null,"upperBound":null},"base":{"#class":"analysis.storage.DisplayPath.Root","name":"_allowances"}}},"storageType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256},"contractInstance":"ce4604a0000000000000000000000003","linkableStorageReadId":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet.None"}}}
		AnnotationCmd:42 JSON{"key":{"name":"internal.func.end","type":"analysis.ip.InternalFuncExitAnnotation","erasureStrategy":"Canonical"},"value":{"id":1,"rets":[{"s":{"namePrefix":"R85","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1023}]},"offset":0}],"functionLayout":{"0":{"#class":"analysis.ip.InternalFuncValueLocation.Scalar"}}}}
		AnnotationCmd:42 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.EVMFunctionReturnWrite","returnbufOffset":"0","returnValueSym":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R85","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1023}]},"callIndex":3}}
		AnnotationCmd:42 JSON{"key":{"name":"tac.return.path","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		LabelCmd:42 "End procedure ERC20-allowance(address,address)"
		AssignExpCmd:42 CANON127:49 R85:35
		AnnotationCmd:42 JSON{"key":{"name":"call.trace.pop","type":"analysis.icfg.Inliner$CallStack$PopRecord","erasureStrategy":"Canonical"},"value":"rO0ABXNyAClhbmFseXNpcy5pY2ZnLklubGluZXIkQ2FsbFN0YWNrJFBvcFJlY29yZPAPfwSLdCWJAgABSQAIY2FsbGVlSWR4cAAAAAM="}
	}
	Block 1_0_0_0_0_0 Succ [0_0_0_2_0_0] {
		AssumeNotCmd:26 false
		AssumeNotCmd:26 false
		AnnotationCmd JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageGlobalChangeSnippet.StorageTakeSnapshot","lhs":{"namePrefix":"lastStorage","tag":{"#class":"tac.Tag.BlockchainState"},"callIndex":0,"meta":[{"key":{"name":"cvl.local","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true},{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"lastStorage"},{"key":{"name":"cvl.type","type":"spec.cvlast.CVLType$PureCVLType","erasureStrategy":"CallTrace"},"value":{"#class":"spec.cvlast.CVLType.PureCVLType.VMInternal.BlockchainState"}},{"key":{"name":"cvl","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true},{"key":{"name":"cvl.display","type":"java.lang.String","erasureStrategy":"CallTrace"},"value":"lastStorage"}]}}}
		AnnotationCmd:26 JSON{"key":{"name":"cvl.label.end","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
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
		AnnotationCmd:50 JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Cmd","cmd":{"cmd_type":"spec.cvlast.CVLCmd.Simple.Apply","cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/spec/ERC20.spec","start":{"line":99,"character":4},"end":{"line":99,"character":15}},"exp":{"#class":"spec.cvlast.CVLExp.ApplyExp.ContractFunction.Symbolic","methodIdWithCallContext":{"#class":"spec.cvlast.ParametricMethod","methodId":"f","host":{"name":"ERC20"}},"args":[{"#class":"spec.cvlast.CVLExp.VariableExp","id":"e","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":6}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"env","fields":[{"fieldName":"msg","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"msg","fields":[{"fieldName":"sender","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"value","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}}]}},{"fieldName":"tx","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"tx","fields":[{"fieldName":"origin","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}}]}},{"fieldName":"block","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"block","fields":[{"fieldName":"coinbase","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"difficulty","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"gaslimit","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"number","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"timestamp","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}}]}}]},"cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/spec/ERC20.spec","start":{"line":99,"character":4},"end":{"line":99,"character":15}}},"twoStateIndex":"NEITHER"},{"#class":"spec.cvlast.CVLExp.VariableExp","id":"args","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":6}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.VMInternal.RawArgs"},"cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/spec/ERC20.spec","start":{"line":99,"character":4},"end":{"line":99,"character":15}}},"twoStateIndex":"NEITHER"}],"noRevert":true,"storage":{"#class":"spec.cvlast.CVLExp.VariableExp","id":"lastStorage","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":6}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.VMInternal.BlockchainState"},"cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/spec/ERC20.spec","start":{"line":99,"character":4},"end":{"line":99,"character":15}}},"twoStateIndex":"NEITHER"},"tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":6}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Void"},"cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/spec/ERC20.spec","start":{"line":99,"character":4},"end":{"line":99,"character":5}}}},"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":6}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}}}}}
		NopCmd
		NopCmd
		NopCmd
		NopCmd
		NopCmd
		NopCmd
		NopCmd
		AnnotationCmd:50 JSON{"key":{"name":"call.trace.push","type":"analysis.icfg.Inliner$CallStack$PushRecord","erasureStrategy":"Canonical"},"value":"rO0ABXNyACphbmFseXNpcy5pY2ZnLklubGluZXIkQ2FsbFN0YWNrJFB1c2hSZWNvcmSX8+DCTLCH+AIAA0kACGNhbGxlZUlkTAAGY2FsbGVldAATTHZjL2RhdGEvTWV0aG9kUmVmO0wAB3N1bW1hcnl0ABVMdmMvZGF0YS9DYWxsU3VtbWFyeTt4cAAAAAJzcgARdmMuZGF0YS5NZXRob2RSZWbJlJTzzU9pGAIAA0wABGF0dHJ0ABdMc2NlbmUvTWV0aG9kQXR0cmlidXRlO0wACmNvbnRyYWN0SWR0ABZMamF2YS9tYXRoL0JpZ0ludGVnZXI7TAAHc2lnSGFzaHQAEExldm0vU2lnaGFzaEludDt4cHNyABxzY2VuZS5NZXRob2RBdHRyaWJ1dGUkQ29tbW9uNHjdebdr9XMCAAB4cgAVc2NlbmUuTWV0aG9kQXR0cmlidXRlcYg2pYWutuUCAAB4cHNyABRqYXZhLm1hdGguQmlnSW50ZWdlcoz8nx+pO/sdAwAGSQAIYml0Q291bnRJAAliaXRMZW5ndGhJABNmaXJzdE5vbnplcm9CeXRlTnVtSQAMbG93ZXN0U2V0Qml0SQAGc2lnbnVtWwAJbWFnbml0dWRldAACW0J4cgAQamF2YS5sYW5nLk51bWJlcoaslR0LlOCLAgAAeHD///////////////7////+AAAAAXVyAAJbQqzzF/gGCFTgAgAAeHAAAAAQzkYEoAAAAAAAAAAAAAAAA3hzcgAOZXZtLlNpZ2hhc2hJbnRUdcqNMXEgeAIAAUwAAW5xAH4ABnhwc3EAfgAM///////////////+/////gAAAAF1cQB+ABAAAAAELhp9TXhw"}
		NopCmd
		AssumeExpCmd Ge(CANON50:15 0x24 )
		NopCmd
		AssumeExpCmd Ge(0x7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff CANON50:15 )
		AssignExpCmd R105:25 Select(CANON48:14 0x4 )
		AssignExpCmd tacCalldatabufCANON0@2:51 R105:25
		AssignExpCmd:50 B107 LAnd(Ge(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff CANON34:6 ) Le(0x0 CANON34:6 ) )
		AssertCmd:50 B107 "sanity bounds check on cvl to vm encoding of tacTmp!2029:int failed"
		AssignExpCmd:50 R108:25 Apply(safe_math_narrow:bif CANON34:6)
		NopCmd
		AssumeExpCmd LAnd(Le(R108:52 0xffffffffffffffffffffffffffffffffffffffff ) Ge(R108:52 0x0 ) )
		AssignExpCmd:50 B112 LAnd(Ge(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff CANON35:7 ) Le(0x0 CANON35:7 ) )
		AssertCmd:50 B112 "sanity bounds check on cvl to vm encoding of tacTmp!2032:int failed"
		AssignExpCmd:50 R113:25 Apply(safe_math_narrow:bif CANON35:7)
		NopCmd
		AssumeExpCmd LAnd(Le(R113:53 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff ) Ge(R113:53 0x0 ) )
		AssignExpCmd:50 B118 LAnd(Ge(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff CANON36:8 ) Le(0x0 CANON36:8 ) )
		AssertCmd:50 B118 "sanity bounds check on cvl to vm encoding of tacTmp!2036:int failed"
		AssignExpCmd:50 R119:25 Apply(safe_math_narrow:bif CANON36:8)
		NopCmd
		AssumeExpCmd LAnd(Le(R119:54 0xffffffffffffffffffffffffffffffffffffffff ) Ge(R119:54 0x0 ) )
		AssignExpCmd:50 B123 LAnd(Ge(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff CANON40:12 ) Le(0x0 CANON40:12 ) )
		AssertCmd:50 B123 "sanity bounds check on cvl to vm encoding of tacTmp!2039:int failed"
		AssignExpCmd:50 R124:25 Apply(safe_math_narrow:bif CANON40:12)
		NopCmd
		AssumeExpCmd LAnd(Le(R124:55 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff ) Ge(R124:55 0x0 ) )
		AssignExpCmd:50 B128 LAnd(Ge(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff CANON41:13 ) Le(0x0 CANON41:13 ) )
		AssertCmd:50 B128 "sanity bounds check on cvl to vm encoding of tacTmp!2042:int failed"
		AssignExpCmd:50 R129:25 Apply(safe_math_narrow:bif CANON41:13)
		NopCmd
		AssumeExpCmd LAnd(Le(R129:56 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff ) Ge(R129:56 0x0 ) )
		AssignExpCmd:50 B133 LAnd(Ge(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff CANON35:7 ) Le(0x0 CANON35:7 ) )
		AssertCmd:50 B133 "sanity bounds check on cvl to vm encoding of tacTmp!2045:int failed"
		AssignExpCmd:50 R134:25 Apply(safe_math_narrow:bif CANON35:7)
		AssignExpCmd:50 B136 LAnd(Ge(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff CANON34:6 ) Le(0x0 CANON34:6 ) )
		AssertCmd:50 B136 "sanity bounds check on cvl to vm encoding of tacTmp!2051:int failed"
		AssignExpCmd:50 R137:25 Apply(safe_math_narrow:bif CANON34:6)
		AssignExpCmd:50 R140:25 Select(tacBalance!!2:2 Apply(to_skey:bif R137:25) )
		AssignExpCmd:57 I141:25 IntSub(R140:25 R134:25 )
		AssignExpCmd:57 tacBalance!!142:2 Store(tacBalance!!2:2 Apply(to_skey:bif R137:25) I141:25 )
		AssignExpCmd:50 R143:25 Select(tacBalance!!142:2 Apply(to_skey:bif R6:17) )
		AssignExpCmd:57 R144:25 Add(R143:25 R134:25)
		NopCmd
		AssumeExpCmd Apply(add_noofl:bif R143:25 R134:25)
		AssignExpCmd:57 tacBalance!!146:2 Store(tacBalance!!142:2 Apply(to_skey:bif R6:17) R144:25 )
		AnnotationCmd:50 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.BalanceSnippet","srcAccountInfo":{"old":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R140","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}]},"new":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"I141","tag":{"#class":"tac.Tag.Int"},"callIndex":0,"meta":[{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}]},"addr":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R137","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}]}},"trgAccountInfo":{"old":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R143","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}]},"new":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R144","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}]},"addr":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R6","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"tacContractAt"},{"key":{"name":"tac.contract.sym.addr.name","type":"java.lang.String","erasureStrategy":"Erased"},"value":"ERC20"},{"key":{"name":"tac.contract.sym.addr","type":"java.math.BigInteger","erasureStrategy":"Erased"},"value":"ce4604a0000000000000000000000003"}]}},"transferredAmount":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R134","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}]}}}
		JumpCmd 0_0_0_2_0_0
	}
	Block 4_0_0_0_0_0 Succ [] {
		AssumeNotCmd:42 false
		AssumeNotCmd:42 false
		AnnotationCmd JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageGlobalChangeSnippet.StorageTakeSnapshot","lhs":{"namePrefix":"lastStorage","tag":{"#class":"tac.Tag.BlockchainState"},"callIndex":0,"meta":[{"key":{"name":"cvl.local","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true},{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"lastStorage"},{"key":{"name":"cvl.type","type":"spec.cvlast.CVLType$PureCVLType","erasureStrategy":"CallTrace"},"value":{"#class":"spec.cvlast.CVLType.PureCVLType.VMInternal.BlockchainState"}},{"key":{"name":"cvl","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true},{"key":{"name":"cvl.display","type":"java.lang.String","erasureStrategy":"CallTrace"},"value":"lastStorage"}]}}}
		AnnotationCmd:42 JSON{"key":{"name":"cvl.label.end","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		AnnotationCmd:58 JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Cmd","cmd":{"cmd_type":"spec.cvlast.CVLCmd.Simple.Assert","cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/spec/ERC20.spec","start":{"line":103,"character":4},"end":{"line":104,"character":58}},"exp":{"#class":"spec.cvlast.CVLExp.BinaryExp.ImpliesExp","l":{"#class":"spec.cvlast.CVLExp.RelopExp.ArithRelopExp.GtExp","l":{"#class":"spec.cvlast.CVLExp.VariableExp","id":"allowance_after","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":6}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Mathint"},"cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/spec/ERC20.spec","start":{"line":103,"character":4},"end":{"line":104,"character":58}}},"twoStateIndex":"NEITHER"},"r":{"#class":"spec.cvlast.CVLExp.VariableExp","id":"allowance_before","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":6}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Mathint"},"cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/spec/ERC20.spec","start":{"line":103,"character":4},"end":{"line":104,"character":58}}},"twoStateIndex":"NEITHER"},"tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":6}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"},"cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/spec/ERC20.spec","start":{"line":103,"character":11},"end":{"line":103,"character":45}}}},"r":{"#class":"spec.cvlast.CVLExp.RelopExp.EqExp","l":{"#class":"spec.cvlast.CVLExp.FieldSelectExp","structExp":{"#class":"spec.cvlast.CVLExp.FieldSelectExp","structExp":{"#class":"spec.cvlast.CVLExp.VariableExp","id":"e","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":6}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"env","fields":[{"fieldName":"msg","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"msg","fields":[{"fieldName":"sender","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"value","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}}]}},{"fieldName":"tx","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"tx","fields":[{"fieldName":"origin","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}}]}},{"fieldName":"block","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"block","fields":[{"fieldName":"coinbase","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"difficulty","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"gaslimit","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"number","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"timestamp","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}}]}}]},"cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/spec/ERC20.spec","start":{"line":103,"character":4},"end":{"line":104,"character":58}}},"twoStateIndex":"NEITHER"},"fieldName":"msg","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":6}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"msg","fields":[{"fieldName":"sender","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"value","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}}]},"cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/spec/ERC20.spec","start":{"line":103,"character":49},"end":{"line":103,"character":50}}}},"fieldName":"sender","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":6}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"},"cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/spec/ERC20.spec","start":{"line":103,"character":49},"end":{"line":103,"character":50}}}},"r":{"#class":"spec.cvlast.CVLExp.VariableExp","id":"holder","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":6}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"},"cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/spec/ERC20.spec","start":{"line":103,"character":4},"end":{"line":104,"character":58}}},"twoStateIndex":"NEITHER"},"tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":6}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"},"cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/spec/ERC20.spec","start":{"line":103,"character":49},"end":{"line":103,"character":71}}}},"tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":6}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"},"cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/spec/ERC20.spec","start":{"line":103,"character":11},"end":{"line":103,"character":71}}}},"description":"\"approve must only change the sender's allowance\"","scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":6}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}}}}}
		AssignExpCmd:59 I147 CANON127:49
		AssignExpCmd:60 I148 CANON33:41
		AssignExpCmd:61 B149 Gt(I147 I148 )
		NopCmd
		AssignExpCmd:62 I151 CANON12:3
		AssignExpCmd:63 CANON133!!152:64 Eq(CANON34:6 I151 )
		AssignExpCmd:65 CANON135!!153:64 LOr(LNot(B149 ) CANON133!!152:64 )
		AssertCmd:66 CANON135!!153:64 "\"approve must only change the sender's allowance\""
		AnnotationCmd:58 JSON{"key":{"name":"cvl.label.end","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		AnnotationCmd:67 JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Cmd","cmd":{"cmd_type":"spec.cvlast.CVLCmd.Simple.Assert","cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/spec/ERC20.spec","start":{"line":106,"character":4},"end":{"line":108,"character":69}},"exp":{"#class":"spec.cvlast.CVLExp.BinaryExp.ImpliesExp","l":{"#class":"spec.cvlast.CVLExp.RelopExp.ArithRelopExp.GtExp","l":{"#class":"spec.cvlast.CVLExp.VariableExp","id":"allowance_after","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":6}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Mathint"},"cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/spec/ERC20.spec","start":{"line":106,"character":4},"end":{"line":108,"character":69}}},"twoStateIndex":"NEITHER"},"r":{"#class":"spec.cvlast.CVLExp.VariableExp","id":"allowance_before","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":6}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Mathint"},"cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/spec/ERC20.spec","start":{"line":106,"character":4},"end":{"line":108,"character":69}}},"twoStateIndex":"NEITHER"},"tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":6}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"},"cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/spec/ERC20.spec","start":{"line":106,"character":11},"end":{"line":106,"character":45}}}},"r":{"#class":"spec.cvlast.CVLExp.BinaryExp.LorExp","l":{"#class":"spec.cvlast.CVLExp.RelopExp.EqExp","l":{"#class":"spec.cvlast.CVLExp.FieldSelectExp","structExp":{"#class":"spec.cvlast.CVLExp.VariableExp","id":"f","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":6}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"method","fields":[{"fieldName":"selector","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":32}},{"fieldName":"isPure","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}},{"fieldName":"isView","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}},{"fieldName":"isPayable","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}},{"fieldName":"numberOfArguments","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"isFallback","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}}]},"cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/spec/ERC20.spec","start":{"line":106,"character":4},"end":{"line":108,"character":69}}},"twoStateIndex":"NEITHER"},"fieldName":"selector","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":6}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":32},"cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/spec/ERC20.spec","start":{"line":107,"character":9},"end":{"line":107,"character":10}}}},"r":{"#class":"spec.cvlast.CVLExp.FieldSelectExp","structExp":{"#class":"spec.cvlast.CVLExp.Constant.SignatureLiteralExp","function":{"#class":"spec.cvlast.QualifiedMethodSignature.QualifiedMethodSig","qualifiedMethodName":{"#class":"spec.cvlast.QualifiedFunction","host":{"name":"ERC20"},"methodId":"approve"},"params":[{"#class":"spec.cvlast.VMParam.Unnamed","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$address"}},{"#class":"spec.cvlast.VMParam.Unnamed","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256}}],"res":[]},"tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":6}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"method","fields":[{"fieldName":"selector","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":32}},{"fieldName":"isPure","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}},{"fieldName":"isView","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}},{"fieldName":"isPayable","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}},{"fieldName":"numberOfArguments","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"isFallback","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}}]},"cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/spec/ERC20.spec","start":{"line":107,"character":27},"end":{"line":107,"character":48}},"annotation":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.CVLExp$Constant$StructLit","fieldNameToEntry":{"selector":{"#class":"spec.cvlast.CVLExp.Constant.NumberLit","n":"95ea7b3","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":6}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":32},"cvlRange":{"#class":"spec.cvlast.CVLRange.Empty"}}},"isPure":{"#class":"spec.cvlast.CVLExp.Constant.BoolLit","b":"0","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":6}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"},"cvlRange":{"#class":"spec.cvlast.CVLRange.Empty"}}},"isView":{"#class":"spec.cvlast.CVLExp.Constant.BoolLit","b":"0","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":6}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"},"cvlRange":{"#class":"spec.cvlast.CVLRange.Empty"}}},"isPayable":{"#class":"spec.cvlast.CVLExp.Constant.BoolLit","b":"0","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":6}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"},"cvlRange":{"#class":"spec.cvlast.CVLRange.Empty"}}},"isFallback":{"#class":"spec.cvlast.CVLExp.Constant.BoolLit","b":"0","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":6}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"},"cvlRange":{"#class":"spec.cvlast.CVLRange.Empty"}}},"numberOfArguments":{"#class":"spec.cvlast.CVLExp.Constant.NumberLit","n":"2","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":6}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256},"cvlRange":{"#class":"spec.cvlast.CVLRange.Empty"}}}},"tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":6}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"method","fields":[{"fieldName":"selector","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":32}},{"fieldName":"isPure","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}},{"fieldName":"isView","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}},{"fieldName":"isPayable","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}},{"fieldName":"numberOfArguments","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"isFallback","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}}]},"cvlRange":{"#class":"spec.cvlast.CVLRange.Empty"}}}}},"fieldName":"selector","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":6}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":32},"cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/spec/ERC20.spec","start":{"line":107,"character":27},"end":{"line":107,"character":48}}}},"tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":6}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"},"cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/spec/ERC20.spec","start":{"line":107,"character":9},"end":{"line":107,"character":57}}}},"r":{"#class":"spec.cvlast.CVLExp.RelopExp.EqExp","l":{"#class":"spec.cvlast.CVLExp.FieldSelectExp","structExp":{"#class":"spec.cvlast.CVLExp.VariableExp","id":"f","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":6}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"method","fields":[{"fieldName":"selector","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":32}},{"fieldName":"isPure","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}},{"fieldName":"isView","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}},{"fieldName":"isPayable","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}},{"fieldName":"numberOfArguments","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"isFallback","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}}]},"cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/spec/ERC20.spec","start":{"line":106,"character":4},"end":{"line":108,"character":69}}},"twoStateIndex":"NEITHER"},"fieldName":"selector","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":6}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":32},"cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/spec/ERC20.spec","start":{"line":107,"character":61},"end":{"line":107,"character":62}}}},"r":{"#class":"spec.cvlast.CVLExp.FieldSelectExp","structExp":{"#class":"spec.cvlast.CVLExp.Constant.SignatureLiteralExp","function":{"#class":"spec.cvlast.QualifiedMethodSignature.QualifiedMethodSig","qualifiedMethodName":{"#class":"spec.cvlast.QualifiedFunction","host":{"name":"ERC20"},"methodId":"increaseAllowance"},"params":[{"#class":"spec.cvlast.VMParam.Unnamed","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$address"}},{"#class":"spec.cvlast.VMParam.Unnamed","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256}}],"res":[]},"tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":6}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"method","fields":[{"fieldName":"selector","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":32}},{"fieldName":"isPure","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}},{"fieldName":"isView","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}},{"fieldName":"isPayable","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}},{"fieldName":"numberOfArguments","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"isFallback","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}}]},"cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/spec/ERC20.spec","start":{"line":107,"character":79},"end":{"line":107,"character":110}},"annotation":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.CVLExp$Constant$StructLit","fieldNameToEntry":{"selector":{"#class":"spec.cvlast.CVLExp.Constant.NumberLit","n":"39509351","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":6}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":32},"cvlRange":{"#class":"spec.cvlast.CVLRange.Empty"}}},"isPure":{"#class":"spec.cvlast.CVLExp.Constant.BoolLit","b":"0","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":6}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"},"cvlRange":{"#class":"spec.cvlast.CVLRange.Empty"}}},"isView":{"#class":"spec.cvlast.CVLExp.Constant.BoolLit","b":"0","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":6}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"},"cvlRange":{"#class":"spec.cvlast.CVLRange.Empty"}}},"isPayable":{"#class":"spec.cvlast.CVLExp.Constant.BoolLit","b":"0","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":6}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"},"cvlRange":{"#class":"spec.cvlast.CVLRange.Empty"}}},"isFallback":{"#class":"spec.cvlast.CVLExp.Constant.BoolLit","b":"0","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":6}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"},"cvlRange":{"#class":"spec.cvlast.CVLRange.Empty"}}},"numberOfArguments":{"#class":"spec.cvlast.CVLExp.Constant.NumberLit","n":"2","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":6}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256},"cvlRange":{"#class":"spec.cvlast.CVLRange.Empty"}}}},"tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":6}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"method","fields":[{"fieldName":"selector","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":32}},{"fieldName":"isPure","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}},{"fieldName":"isView","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}},{"fieldName":"isPayable","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}},{"fieldName":"numberOfArguments","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"isFallback","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}}]},"cvlRange":{"#class":"spec.cvlast.CVLRange.Empty"}}}}},"fieldName":"selector","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":6}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":32},"cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/spec/ERC20.spec","start":{"line":107,"character":79},"end":{"line":107,"character":110}}}},"tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":6}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"},"cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/spec/ERC20.spec","start":{"line":107,"character":61},"end":{"line":107,"character":119}}}},"tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":6}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"},"cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/spec/ERC20.spec","start":{"line":107,"character":9},"end":{"line":107,"character":119}}}},"tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":6}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"},"cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/spec/ERC20.spec","start":{"line":106,"character":11},"end":{"line":107,"character":120}}}},"description":"\"only approve and increaseAllowance can increase allowances\"","scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":6}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}}}}}
		AssignExpCmd:68 I154 CANON127:49
		AssignExpCmd:69 I155 CANON33:41
		AssignExpCmd:70 B156 Gt(I154 I155 )
		AssignExpCmd:71 CANON139:64 false
		AssignExpCmd:72 CANON140:64 false
		AssignExpCmd:73 CANON141:64 false
		AssignExpCmd:74 CANON142!!157:64 LOr(LNot(B156 ) false )
		AssertCmd:75 CANON142!!157:64 "\"only approve and increaseAllowance can increase allowances\""
		AnnotationCmd:67 JSON{"key":{"name":"cvl.label.end","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
	}
	Block 0_0_0_2_0_0 Succ [2029_1018_0_2_0_1, 2029_1018_0_2_0_2] {
		LabelCmd "Start procedure ERC20-withdraw(uint256)"
		AnnotationCmd JSON{"key":{"name":"fps.free-pointer-is-scalarized","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true}
		AssignExpCmd lastHasThrown@2:76 false
		AssignExpCmd lastReverted@2:77 false
		AssignExpCmd R158:25 Select(tacExtcodesize!!0:0 Apply(to_skey:bif R6:30) )
		NopCmd
		AssumeExpCmd Gt(R158:25 0x0 )
		AnnotationCmd JSON{"key":{"name":"internal.func.finder.info","type":"analysis.ip.InternalFunctionFinderReport","erasureStrategy":"Erased"},"value":"rO0ABXNyAChhbmFseXNpcy5pcC5JbnRlcm5hbEZ1bmN0aW9uRmluZGVyUmVwb3J0ian+bYn1VdACAAFMABN1bnJlc29sdmVkRnVuY3Rpb25zdAAPTGphdmEvdXRpbC9TZXQ7eHBzcgAhZGF0YXN0cnVjdHVyZXMuTGlua2VkQXJyYXlIYXNoU2V0AAAAAAAAAAEDAAJGAApsb2FkRmFjdG9yTAAJaGFzaFRhYmxldAAuTGRhdGFzdHJ1Y3R1cmVzL2FycmF5aGFzaHRhYmxlL0FycmF5SGFzaFRhYmxlO3hwdwgAAAAAQAAAAHg="}
		AnnotationCmd JSON{"key":{"name":"fps.free-pointer-is-scalarized","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true}
		NopCmd
		AssumeExpCmd LNot(Lt(CANON50:15 0x4 ) )
		NopCmd
		AssumeExpCmd Gt(0x70a08231 tacSighash!!8:18 )
		NopCmd
		AssumeExpCmd LNot(Gt(0x2e1a7d4d tacSighash!!8:18 ) )
		NopCmd
		AssumeExpCmd Eq(0x2e1a7d4d tacSighash!!8:18 )
		NopCmd
		AssumeExpCmd Eq(R113:53 0x0 )
		AssignExpCmd:78 R165:79 Sub(CANON50:15 0x4 )
		NopCmd
		AssumeExpCmd LNot(Slt(R165:79 0x20 ) )
		AssignExpCmd:80 R167:81 tacCalldatabufCANON0@2:82
		AssignExpCmd:83 R170:84 Apply(hash_3_keccak:bif Apply(skey_basic:bif 0x40) Apply(to_skey:bif R108:85) Apply(skey_basic:bif 0x0))
		AssignExpCmd:86 R171:84 Select(CANON82!!4:16 R170:87 )
		AnnotationCmd JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet","value":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R171","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1021}]},"displayPath":{"#class":"analysis.storage.DisplayPath.MapAccess","key":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R108","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.env.known-bit-width","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":160},{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1019}]},"keyTyp":{"#class":"tac.TACStorageType.IntegralType","typeLabel":"address","numBytes":"14","descriptor":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$address"},"lowerBound":null,"upperBound":null},"base":{"#class":"analysis.storage.DisplayPath.Root","name":"_balances"}},"storageType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256},"contractInstance":"ce4604a0000000000000000000000003","linkableStorageReadId":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet.None"}}}
		NopCmd
		AssumeExpCmd LNot(Gt(R105:25 R171:84 ) )
		AssignExpCmd:88 R175:89 Apply(hash_3_keccak:bif Apply(skey_basic:bif 0x40) Apply(to_skey:bif R108:85) Apply(skey_basic:bif 0x0))
		AssignExpCmd:90 R176:79 Select(CANON82!!4:16 R175:91 )
		AnnotationCmd JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet","value":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R176","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1017}]},"displayPath":{"#class":"analysis.storage.DisplayPath.MapAccess","key":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R108","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.env.known-bit-width","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":160},{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1018}]},"keyTyp":{"#class":"tac.TACStorageType.IntegralType","typeLabel":"address","numBytes":"14","descriptor":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$address"},"lowerBound":null,"upperBound":null},"base":{"#class":"analysis.storage.DisplayPath.Root","name":"_balances"}},"storageType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256},"contractInstance":"ce4604a0000000000000000000000003","linkableStorageReadId":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet.None"}}}
		NopCmd
		AssumeExpCmd LNot(Lt(R176:79 R105:25 ) )
		AssignExpCmd:92 R178:93 Sub(R176:79 R105:25 )
		AnnotationCmd JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Message","s":"Apply hook Hook Sstore 0x0.0x0[key a] uint256 new_value tacS:wordmap"}}
		AssignExpCmd R179:25 Select(CANON82!!4:16 R175:91 )
		AnnotationCmd JSON{"key":{"name":"tac.inlined.hook","type":"instrumentation.transformers.HookInliner$InlinedHook","erasureStrategy":"Canonical"},"value":{"cvlPattern":{"#class":"spec.cvlast.CVLHookPattern.StoragePattern.Store","value":{"name":"new_value","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256}},"slot":{"#class":"spec.cvlast.CVLSlotPattern.MapAccess","base":{"#class":"spec.cvlast.CVLSlotPattern.Static.Named","solidityContract":{"name":"ERC20"},"name":"_balances"},"key":{"name":"a","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$address"}}},"base":"STORAGE","previousValue":{"name":"old_value","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256}}},"substitutions":{"new_value":{"#class":"vc.data.HookValue.Direct","expr":{"#class":"vc.data.TACExpr.Sym.Var","s":{"namePrefix":"R178","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1014}]},"tag":{"#class":"tac.Tag.Bit256"}}},"old_value":{"#class":"vc.data.HookValue.Direct","expr":{"#class":"vc.data.TACExpr.Sym.Var","s":{"namePrefix":"R179","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}]},"tag":{"#class":"tac.Tag.Bit256"}}},"a":{"#class":"vc.data.HookValue.Direct","expr":{"#class":"vc.data.TACExpr.Sym.Var","s":{"namePrefix":"R108","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.env.known-bit-width","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":160},{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1018}]},"tag":{"#class":"tac.Tag.Bit256"}}}}}}
		AnnotationCmd JSON{"key":{"name":"cvl.label.end","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		AnnotationCmd JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.StoreSnippet","value":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R178","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1014}]},"displayPath":{"#class":"analysis.storage.DisplayPath.MapAccess","key":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R108","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.env.known-bit-width","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":160},{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1018}]},"keyTyp":{"#class":"tac.TACStorageType.IntegralType","typeLabel":"address","numBytes":"14","descriptor":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$address"},"lowerBound":null,"upperBound":null},"base":{"#class":"analysis.storage.DisplayPath.Root","name":"_balances"}},"storageType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256},"contractInstance":"ce4604a0000000000000000000000003"}}
		AssignExpCmd:94 R183:33 0x80
		AssignHavocCmd:94 R184:95
		AssignExpCmd R185:25 Select(tacBalance!!146:2 Apply(to_skey:bif R6:30) )
		AssignExpCmd B186:96 Ge(R185:25 R105:25 )
		AssignExpCmd R187:25 Select(tacBalance!!146:2 Apply(to_skey:bif R108:97) )
		AssignExpCmd B188:96 Apply(add_noofl:bif R187:25 R105:25)
		AssignExpCmd tacCond!!189:96 LAnd(B186:96 B188:96 )
		JumpiCmd 2029_1018_0_2_0_1 2029_1018_0_2_0_2 tacCond!!189:96
	}
	Block 2029_1018_0_2_0_7 Succ [2090_1018_0_2_0_0, 2057_1018_0_2_0_0] {
		AssignExpCmd B190:79 Eq(tacReturnsize!!212:98 0x0 )
		JumpiCmd:94 2090_1018_0_2_0_0 2057_1018_0_2_0_0 B190:79
	}
	Block 2057_1018_0_2_0_0 Succ [2095_1018_0_2_0_0] {
		AnnotationCmd JSON{"key":{"name":"pta.end-allocation","type":"analysis.alloc.AllocationAnalysis$AbstractLocation","erasureStrategy":"Erased"},"value":{"prevFPWriteIdx":0,"nextFPWriteCmd":{"block":{"#class":"tac.BlockIdentifier","origStartPc":2057,"stkTop":1018,"decompCopy":0,"calleeIdx":0,"topOfStackValue":0,"freshCopy":0},"pos":5},"sort":{"#class":"analysis.alloc.AllocationAnalysis.Alloc.DynamicBlock","eSz":"1","elemSym":{"first":{"block":{"#class":"tac.BlockIdentifier","origStartPc":2057,"stkTop":1018,"decompCopy":0,"calleeIdx":0,"topOfStackValue":0,"freshCopy":0},"pos":2},"second":{"namePrefix":"LCANON51","tag":{"#class":"tac.Tag.Bit256"},"callIndex":2,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1015}]}}}}}
		JumpCmd:94 2095_1018_0_2_0_0
	}
	Block 2090_1018_0_2_0_0 Succ [2095_1018_0_2_0_0] {
		JumpCmd 2095_1018_0_2_0_0
	}
	Block 2029_1018_0_2_0_5 Succ [2029_1018_0_2_0_7] {
		AssignExpCmd R191:25 Ite(Eq(tacRC!!210:99 0x0 ) R105:25 0x0 )
		AssignExpCmd R192:25 Select(tacBalance!!228:2 Apply(to_skey:bif R108:97) )
		AssignExpCmd:100 I193:25 IntSub(R192:25 R191:25 )
		AssignExpCmd:100 tacBalance!!194:2 Store(tacBalance!!228:2 Apply(to_skey:bif R108:97) I193:25 )
		AssignExpCmd R195:25 Select(tacBalance!!194:2 Apply(to_skey:bif R6:101) )
		AssignExpCmd:100 R196:25 Add(R195:25 R191:25)
		NopCmd
		AssumeExpCmd Apply(add_noofl:bif R195:25 R191:25)
		AnnotationCmd JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.BalanceSnippet","srcAccountInfo":{"old":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R192","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}]},"new":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"I193","tag":{"#class":"tac.Tag.Int"},"callIndex":0,"meta":[{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}]},"addr":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R108","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.env.known-bit-width","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":160},{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1020}]}},"trgAccountInfo":{"old":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R195","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}]},"new":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R196","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}]},"addr":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R6","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"tacAddress"},{"key":{"name":"tac.env.known-bit-width","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":160},{"key":{"name":"tac.contract.sym.addr.name","type":"java.lang.String","erasureStrategy":"Erased"},"value":"ERC20"},{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}},{"key":{"name":"tac.contract.sym.addr","type":"java.math.BigInteger","erasureStrategy":"Erased"},"value":"ce4604a0000000000000000000000003"}]}},"transferredAmount":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R191","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}]}}}
		AnnotationCmd JSON{"key":{"name":"dsa.assign.start","type":"java.lang.String","erasureStrategy":"Erased"},"value":"2029_1018_0_0_0_2 -> 2029_1018_0_0_0_1"}
		LabelCmd "Parallel assignment for B804:bool, B805:bool, R806:bv256 := B791:bool, B801:bool, R802:bv256"
		AnnotationCmd JSON{"key":{"name":"dsa.assign.end","type":"java.lang.String","erasureStrategy":"Erased"},"value":"2029_1018_0_0_0_2 -> 2029_1018_0_0_0_1"}
		LabelCmd "Parallel assignment for R199:bv256, tacReturnsize!!212:bv256 := tacRC!!210:bv256, tacReturnsize!!209:bv256"
		AssignExpCmd R199:79 tacRC!!210:79
		AssignExpCmd tacReturnsize!!212:98 tacReturnsize!!209:98
	}
	Block 2029_1018_0_2_0_1 Succ [2_0_0_2_0_0, 2029_1018_0_2_0_3] {
		AssignExpCmd R201:25 Select(tacBalance!!146:2 Apply(to_skey:bif R6:101) )
		AssignExpCmd:100 I202:25 IntSub(R201:25 R105:25 )
		AssignExpCmd:100 tacBalance!!203:2 Store(tacBalance!!146:2 Apply(to_skey:bif R6:101) I202:25 )
		AssignExpCmd R204:25 Select(tacBalance!!203:2 Apply(to_skey:bif R108:97) )
		AssignExpCmd:100 R205:25 Add(R204:25 R105:25)
		NopCmd
		AssumeExpCmd Apply(add_noofl:bif R204:25 tacCalldatabufCANON0@2:82)
		AssignExpCmd:100 tacBalance!!207:2 Store(tacBalance!!203:2 Apply(to_skey:bif R108:97) R205:25 )
		AnnotationCmd JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.BalanceSnippet","srcAccountInfo":{"old":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R201","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}]},"new":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"I202","tag":{"#class":"tac.Tag.Int"},"callIndex":0,"meta":[{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}]},"addr":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R6","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"tacAddress"},{"key":{"name":"tac.env.known-bit-width","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":160},{"key":{"name":"tac.contract.sym.addr.name","type":"java.lang.String","erasureStrategy":"Erased"},"value":"ERC20"},{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}},{"key":{"name":"tac.contract.sym.addr","type":"java.math.BigInteger","erasureStrategy":"Erased"},"value":"ce4604a0000000000000000000000003"}]}},"trgAccountInfo":{"old":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R204","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}]},"new":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R205","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}]},"addr":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R108","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.env.known-bit-width","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":160},{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1020}]}},"transferredAmount":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R167","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1013}]}}}
		AssignHavocCmd tacReturndata!!208:102
		AssignHavocCmd tacReturnsize!!209:98
		AssignHavocCmd tacRC!!210:99
		AssignExpCmd tacCond!!211:96 Gt(tacRC!!210:99 0x0 )
		JumpiCmd 2_0_0_2_0_0 2029_1018_0_2_0_3 tacCond!!211:96
	}
	Block 2029_1018_0_2_0_6 Succ [2029_1018_0_2_0_7] {
		AnnotationCmd JSON{"key":{"name":"dsa.assign.start","type":"java.lang.String","erasureStrategy":"Erased"},"value":"2029_1018_0_0_0_3 -> 2029_1018_0_0_0_1"}
		LabelCmd "Parallel assignment for B804:bool, B805:bool, R806:bv256 := B791:bool, B801:bool, R802:bv256"
		AnnotationCmd JSON{"key":{"name":"dsa.assign.end","type":"java.lang.String","erasureStrategy":"Erased"},"value":"2029_1018_0_0_0_3 -> 2029_1018_0_0_0_1"}
		LabelCmd "Parallel assignment for R199:bv256, tacReturnsize!!212:bv256 := tacRC!!210:bv256, tacReturnsize!!209:bv256"
		AssignExpCmd R199:79 tacRC!!210:79
		AssignExpCmd tacReturnsize!!212:98 tacReturnsize!!209:98
	}
	Block 2029_1018_0_2_0_2 Succ [2029_1018_0_2_0_7] {
		NopCmd
		AssignExpCmd tacReturndata!!215:102 ByteMapDefinition(CANON143:bv256 -> 0x0 )
		AnnotationCmd JSON{"key":{"name":"dsa.assign.start","type":"java.lang.String","erasureStrategy":"Erased"},"value":"2029_1018_0_0_0_4 -> 2029_1018_0_0_0_1"}
		LabelCmd "Parallel assignment for B804:bool, B805:bool, R806:bv256 := B811:bool, B808:bool, R809:bv256"
		NopCmd
		AnnotationCmd JSON{"key":{"name":"dsa.assign.end","type":"java.lang.String","erasureStrategy":"Erased"},"value":"2029_1018_0_0_0_4 -> 2029_1018_0_0_0_1"}
		LabelCmd "Parallel assignment for R199:bv256, tacReturnsize!!212:bv256 := R216:bv256, tacReturnsize!!214:bv256"
		AssignExpCmd R199:79 0x0
		AssignExpCmd tacReturnsize!!212:98 0x0
	}
	Block 2095_1018_0_2_0_0 Succ [3_0_0_0_0_0] {
		NopCmd
		AssumeExpCmd Gt(R199:79 0x0 )
		AnnotationCmd JSON{"key":{"name":"tac.return.path","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		LabelCmd "End procedure ERC20-withdraw(uint256)"
		JumpCmd 3_0_0_0_0_0
	}
	Block 3_0_0_0_0_0 Succ [0_0_0_3_0_0] {
		AnnotationCmd:50 JSON{"key":{"name":"call.trace.pop","type":"analysis.icfg.Inliner$CallStack$PopRecord","erasureStrategy":"Canonical"},"value":"rO0ABXNyAClhbmFseXNpcy5pY2ZnLklubGluZXIkQ2FsbFN0YWNrJFBvcFJlY29yZPAPfwSLdCWJAgABSQAIY2FsbGVlSWR4cAAAAAI="}
		AssumeNotCmd:50 false
		AssumeNotCmd:50 false
		AnnotationCmd JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageGlobalChangeSnippet.StorageTakeSnapshot","lhs":{"namePrefix":"lastStorage","tag":{"#class":"tac.Tag.BlockchainState"},"callIndex":0,"meta":[{"key":{"name":"cvl.local","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true},{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"lastStorage"},{"key":{"name":"cvl.type","type":"spec.cvlast.CVLType$PureCVLType","erasureStrategy":"CallTrace"},"value":{"#class":"spec.cvlast.CVLType.PureCVLType.VMInternal.BlockchainState"}},{"key":{"name":"cvl","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true},{"key":{"name":"cvl.display","type":"java.lang.String","erasureStrategy":"CallTrace"},"value":"lastStorage"}]}}}
		AnnotationCmd:50 JSON{"key":{"name":"cvl.label.end","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		AnnotationCmd:42 JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Cmd","cmd":{"cmd_type":"spec.cvlast.CVLCmd.Simple.Definition","cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/spec/ERC20.spec","start":{"line":101,"character":4},"end":{"line":101,"character":57}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Mathint"},"idL":[{"#class":"spec.cvlast.CVLLhs.Id","cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/spec/ERC20.spec","start":{"line":101,"character":4},"end":{"line":101,"character":27}},"id":"allowance_after","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":6}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Mathint"},"cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/spec/ERC20.spec","start":{"line":101,"character":4},"end":{"line":101,"character":57}}}}],"exp":{"#class":"spec.cvlast.CVLExp.ApplyExp.ContractFunction.Concrete","methodIdWithCallContext":{"#class":"spec.cvlast.ConcreteMethod","signature":{"#class":"spec.cvlast.ExternalQualifiedMethodSignature.ExternalQualifiedMethodSig","wrapped":{"#class":"spec.cvlast.QualifiedMethodSignature.QualifiedMethodSig","qualifiedMethodName":{"#class":"spec.cvlast.QualifiedFunction","host":{"name":"ERC20"},"methodId":"allowance"},"params":[{"#class":"spec.cvlast.VMParam.Named","name":"owner","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$address"}},{"#class":"spec.cvlast.VMParam.Named","name":"spender","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$address"}}],"res":[{"#class":"spec.cvlast.VMParam.Unnamed","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256}}]},"sighashInt":{"n":"dd62ed3e"}}},"args":[{"#class":"spec.cvlast.CVLExp.VariableExp","id":"holder","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":6}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"},"cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/spec/ERC20.spec","start":{"line":101,"character":4},"end":{"line":101,"character":57}}},"twoStateIndex":"NEITHER"},{"#class":"spec.cvlast.CVLExp.VariableExp","id":"spender","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":6}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"},"cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/spec/ERC20.spec","start":{"line":101,"character":4},"end":{"line":101,"character":57}}},"twoStateIndex":"NEITHER"}],"noRevert":true,"storage":{"#class":"spec.cvlast.CVLExp.VariableExp","id":"lastStorage","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":6}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.VMInternal.BlockchainState"},"cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/spec/ERC20.spec","start":{"line":101,"character":4},"end":{"line":101,"character":57}}},"twoStateIndex":"NEITHER"},"isWhole":false,"tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":6}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.VM","descriptor":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256},"context":{"#class":"spec.cvlast.typedescriptors.FromVMContext.ReturnValue"}},"cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/spec/ERC20.spec","start":{"line":101,"character":30},"end":{"line":101,"character":39}},"annotation":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.CallResolution$DirectPassing","target":{"methodSignature":{"#class":"spec.cvlast.ExternalQualifiedMethodSignature.ExternalQualifiedMethodSig","wrapped":{"#class":"spec.cvlast.QualifiedMethodSignature.QualifiedMethodSig","qualifiedMethodName":{"#class":"spec.cvlast.QualifiedFunction","host":{"name":"ERC20"},"methodId":"allowance"},"params":[{"#class":"spec.cvlast.VMParam.Named","name":"owner","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$address"}},{"#class":"spec.cvlast.VMParam.Named","name":"spender","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$address"}}],"res":[{"#class":"spec.cvlast.VMParam.Unnamed","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256}}]},"sighashInt":{"n":"dd62ed3e"}},"definitelyNonPayable":true,"annotation":{"visibility":"EXTERNAL","envFree":true,"library":false},"stateMutability":"view","tag":{"#class":"spec.cvlast.CVLImportedFunctionTag.WithMethodInfo","evmMethodInfo":{"sigHash":"dd62ed3e","name":"allowance","argTypes":[{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.address"},{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.address"}],"resultTypes":[{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256}],"stateMutability":"view","envfreeInfo":{"#class":"bridge.EnvfreeInfo.Unknown"},"isConstant":false,"paramNames":["owner","spender"],"isLibrary":false}}},"hasEnv":false}}},"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":6}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}}}}}
		AssignExpCmd:103 I218 CANON12:3
		AssignExpCmd:104 I219 CANON13:4
	}
	Block 2029_1018_0_2_0_4 Succ [2029_1018_0_2_0_5, 2029_1018_0_2_0_6] {
		AssignHavocCmd ReachabilityCertora2029_1018_0_2_0_3:105
		AssignHavocCmd ReachabilityCertora2_0_0_2_0_0:106
		AssignExpCmd tacBalance!!228:2 Ite(ReachabilityCertora2_0_0_2_0_0:106 tacBalance!!225:2 tacBalance!!207:2 )
		AssignExpCmd B221:25 Eq(tacRC!!210:99 0x0 )
		JumpiCmd 2029_1018_0_2_0_5 2029_1018_0_2_0_6 B221:25
	}
	Block 2029_1018_0_2_0_3 Succ [2029_1018_0_2_0_4] {
		LabelCmd "Parallel assignment for tacBalance!!228:wordmap := tacBalance!!207:wordmap"
	}
	Block 2_0_0_2_0_0 Succ [2029_1018_0_2_0_4] {
		AnnotationCmd JSON{"key":{"name":"call.trace.external.summary.start","type":"analysis.icfg.SummaryStack$SummaryStart$External","erasureStrategy":"CallTrace"},"value":"rO0ABXNyADBhbmFseXNpcy5pY2ZnLlN1bW1hcnlTdGFjayRTdW1tYXJ5U3RhcnQkRXh0ZXJuYWxjtfa80obNOgIABUwACGNhbGxOb2RldAAVTHZjL2RhdGEvQ2FsbFN1bW1hcnk7TAAXY2FsbFJlc29sdXRpb25UYWJsZUluZm90ADZMcmVwb3J0L2NhbGxyZXNvbHV0aW9uL0NhbGxSZXNvbHV0aW9uVGFibGVTdW1tYXJ5SW5mbztMAAtjYWxsU2l0ZVNyY3QAFUx2Yy9kYXRhL1RBQ01ldGFJbmZvO0wAB3N1bW1hcnl0AB1Mc3BlYy9jdmxhc3QvU3BlY0NhbGxTdW1tYXJ5O0wAB3N1cHBvcnR0AA9MamF2YS91dGlsL1NldDt4cgAnYW5hbHlzaXMuaWNmZy5TdW1tYXJ5U3RhY2skU3VtbWFyeVN0YXJ0yFuGy+NGxUICAAB4cHNyABN2Yy5kYXRhLkNhbGxTdW1tYXJ5lBybDm+X4V0CABBJAAlzdW1tYXJ5SWRMAA5jYWxsQ29udmVudGlvbnQAJkxpbnN0cnVtZW50YXRpb24vY2FsbHMvQ2FsbENvbnZlbnRpb247TAAKY2FsbFRhcmdldHQAGkxhbmFseXNpcy9pY2ZnL0NhbGxUYXJnZXQ7TAAIY2FsbFR5cGV0ABVMdmMvZGF0YS9UQUNDYWxsVHlwZTtMAA9jYW5ub3RCZUlubGluZWR0AC1MYW5hbHlzaXMvaWNmZy9JbmxpbmVyJElsbGVnYWxJbmxpbmluZ1JlYXNvbjtMAAZnYXNWYXJ0ABNMdmMvZGF0YS9UQUNTeW1ib2w7TAAGaW5CYXNlcQB+AA1MAAhpbk9mZnNldHEAfgANTAAGaW5TaXplcQB+AA1MAAxvcmlnQ2FsbGNvcmV0ACBMdmMvZGF0YS9UQUNDbWQkU2ltcGxlJENhbGxDb3JlO0wAB291dEJhc2VxAH4ADUwACW91dE9mZnNldHEAfgANTAAHb3V0U2l6ZXEAfgANTAANc2lnUmVzb2x1dGlvbnEAfgAFTAAFdG9WYXJxAH4ADUwACHZhbHVlVmFycQB+AA14cAAAAABzcgAkaW5zdHJ1bWVudGF0aW9uLmNhbGxzLkNhbGxDb252ZW50aW9uR7TtbpS+/PECAANJAAhjYWxsZXJJZEwABWlucHV0dAAZTGFuYWx5c2lzL2ljZmcvQ2FsbElucHV0O0wABnJhd091dHQAIkxpbnN0cnVtZW50YXRpb24vY2FsbHMvQ2FsbE91dHB1dDt4cAAAAABzcgAXYW5hbHlzaXMuaWNmZy5DYWxsSW5wdXSYyQ9TITVMUAIAB0wAB2Jhc2VWYXJ0ABlMdmMvZGF0YS9UQUNFeHByJFN5bSRWYXI7TAAQZW5jb2RlZEFyZ3VtZW50c3QAI0xhbmFseXNpcy9pY2ZnL0FCSUFyZ3VtZW50RW5jb2Rpbmc7TAATaW5wdXRTaXplTG93ZXJCb3VuZHQAFkxqYXZhL21hdGgvQmlnSW50ZWdlcjtMAAZvZmZzZXR0ABVMdmMvZGF0YS9UQUNFeHByJFN5bTtMABRyYW5nZVRvRGVjb21wb3NlZEFyZ3QAD0xqYXZhL3V0aWwvTWFwO0wAEHNpbXBsaWZpZWRPZmZzZXR0ABtMdmMvZGF0YS9UQUNFeHByJFN5bSRDb25zdDtMAARzaXplcQB+ABh4cHNyABd2Yy5kYXRhLlRBQ0V4cHIkU3ltJFZhcskrg43eGgPnAgACTAABc3QAF0x2Yy9kYXRhL1RBQ1N5bWJvbCRWYXI7TAADdGFndAAJTHRhYy9UYWc7eHIAE3ZjLmRhdGEuVEFDRXhwciRTeW2iVj0S4YSNUAIAAHhyAA92Yy5kYXRhLlRBQ0V4cHJYhGlUu/v+yAIAAHhwc3IANnZjLmRhdGEuVEFDU3ltYm9sJFZhciRXaXRoRGVmYXVsdENhbGxJbmRleCRXaXRoQnl0ZU1hcJ7+oHF4CHAAAgACTAAEbWV0YXQALUxrb3RsaW54L2NvbGxlY3Rpb25zL2ltbXV0YWJsZS9QZXJzaXN0ZW50TWFwO0wACm5hbWVQcmVmaXh0ABJMamF2YS9sYW5nL1N0cmluZzt4cgAVdmMuZGF0YS5UQUNTeW1ib2wkVmFyCYrCGVl9SXYCAAB4cgARdmMuZGF0YS5UQUNTeW1ib2zd3Run/CoWswIAAHhwc3IAJmRhdGFzdHJ1Y3R1cmVzLnRyZWFwLkhhc2hUcmVhcE1hcCROb2Rlf2t9acJIPnQCAANMAANrZXl0ABJMamF2YS9sYW5nL09iamVjdDtMAARuZXh0dAA1TGRhdGFzdHJ1Y3R1cmVzL3RyZWFwL0hhc2hUcmVhcE1hcCRNb3JlS2V5VmFsdWVQYWlycztMAAV2YWx1ZXEAfgApeHIAIWRhdGFzdHJ1Y3R1cmVzLnRyZWFwLkhhc2hUcmVhcE1hcPMJ/2vt3boKAgAAeHIAHWRhdGFzdHJ1Y3R1cmVzLnRyZWFwLlRyZWFwTWFw46LAyn3v5moCAAB4cgAaZGF0YXN0cnVjdHVyZXMudHJlYXAuVHJlYXA88f21zZwbdQIAAkwABGxlZnR0ABxMZGF0YXN0cnVjdHVyZXMvdHJlYXAvVHJlYXA7TAAFcmlnaHRxAH4ALnhwcHNxAH4AKHBzcQB+AChwcHNyAAt0YWMuTWV0YUtleVF/W3MiCfIZAgADTAAPZXJhc3VyZVN0cmF0ZWd5dAAdTHRhYy9NZXRhS2V5JEVyYXN1cmVTdHJhdGVneTtMAARuYW1lcQB+ACRMAAN0eXB0ABFMamF2YS9sYW5nL0NsYXNzO3hwfnIAG3RhYy5NZXRhS2V5JEVyYXN1cmVTdHJhdGVneQAAAAAAAAAAEgAAeHIADmphdmEubGFuZy5FbnVtAAAAAAAAAAASAAB4cHQACUNhbm9uaWNhbHQAF3RhYy5tZW1vcnkucGFydGl0aW9uLWlkdnIAEWphdmEubGFuZy5JbnRlZ2VyEuKgpPeBhzgCAAFJAAV2YWx1ZXhyABBqYXZhLmxhbmcuTnVtYmVyhqyVHQuU4IsCAAB4cHBzcQB+ADsAAAAAc3EAfgAycQB+ADh0ABJUYWMuc3ltYm9sLmtleXdvcmR2cgAQamF2YS5sYW5nLlN0cmluZ6DwpDh6O7NCAgAAeHBwdAAEdGFjTXNxAH4AMnEAfgA4dAANdGFjLmlzLm1lbW9yeXZyACJ0YWMuTWV0YU1hcCRDb21wYW5pb24kTm90aGluZ1ZhbHVl8nsHH85ykpUCAAB4cHBzcQB+AEZ0AA10YWNNQ0FOT04wISExc3IAD3RhYy5UYWckQnl0ZU1hcDW/0cuhg0YJAgAAeHIAC3RhYy5UYWckTWFwAScrcw1dz/0CAAB4cgAHdGFjLlRhZy5PVd4J9sZ4AgAAeHBwcHNxAH4AHHNyADV2Yy5kYXRhLlRBQ1N5bWJvbCRWYXIkV2l0aERlZmF1bHRDYWxsSW5kZXgkV2l0aEJpdDI1NnqsyEgq0drPAgACTAAEbWV0YXEAfgAjTAAKbmFtZVByZWZpeHEAfgAkeHEAfgAlc3EAfgAoc3EAfgAocHBxAH4AP3B0AAFMcHNxAH4AMnEAfgA4dAAQdGFjLnN0YWNrLmhlaWdodHEAfgA9cHNxAH4AOwAAA/h0AARSMTgzc3IADnRhYy5UYWckQml0MjU2IyLQT+LlKkgCAAB4cQB+AExzcgARamF2YS51dGlsLkhhc2hNYXAFB9rBwxZg0QMAAkYACmxvYWRGYWN0b3JJAAl0aHJlc2hvbGR4cD9AAAAAAAAAdwgAAAAQAAAAAHhwc3IAGXZjLmRhdGEuVEFDRXhwciRTeW0kQ29uc3RTSK/zMkHadgIAAkwAAXN0ABlMdmMvZGF0YS9UQUNTeW1ib2wkQ29uc3Q7TAADdGFncQB+AB54cQB+AB9zcgAXdmMuZGF0YS5UQUNTeW1ib2wkQ29uc3QmHp5/l8IUcAIAAkwAA3RhZ3EAfgAeTAAFdmFsdWVxAH4AF3hxAH4AJnEAfgBZc3IAFGphdmEubWF0aC5CaWdJbnRlZ2VyjPyfH6k7+x0DAAZJAAhiaXRDb3VudEkACWJpdExlbmd0aEkAE2ZpcnN0Tm9uemVyb0J5dGVOdW1JAAxsb3dlc3RTZXRCaXRJAAZzaWdudW1bAAltYWduaXR1ZGV0AAJbQnhxAH4APP///////////////v////4AAAAAdXIAAltCrPMX+AYIVOACAAB4cAAAAAB4cQB+AFlzcgAgaW5zdHJ1bWVudGF0aW9uLmNhbGxzLkNhbGxPdXRwdXTCxZs3wb2cewIAA0wABGJhc2VxAH4AHUwABm9mZnNldHQAEUx2Yy9kYXRhL1RBQ0V4cHI7TAAEc2l6ZXEAfgBneHBzcQB+ACJzcQB+AChwc3EAfgAocHNxAH4AKHBwcQB+ADVwcQB+AD5xAH4AP3BxAH4AQ3EAfgBEcHEAfgBIcQB+AElzcQB+ABxzcQB+AE9zcQB+AChzcQB+AChwcHEAfgA/cHEAfgBTcHEAfgBUcHNxAH4AOwAAA/hxAH4AV3EAfgBZc3EAfgBcc3EAfgBfcQB+AFlxAH4AY3EAfgBZc3IAHWFuYWx5c2lzLmljZmcuQ2FsbFRhcmdldCROb25lVWDROet1Mg4CAAB4cgAYYW5hbHlzaXMuaWNmZy5DYWxsVGFyZ2V0Rt09LHx2PiUCAAB4cH5yABN2Yy5kYXRhLlRBQ0NhbGxUeXBlAAAAAAAAAAASAAB4cQB+ADd0AAxSRUdVTEFSX0NBTExwc3EAfgBPc3EAfgAoc3EAfgAocHBxAH4AP3BxAH4AU3BxAH4AVHBzcQB+ADsAAAPzdAAEUjE4NHNxAH4AInNxAH4AKHBzcQB+AChwc3EAfgAocHBxAH4ANXBxAH4APnEAfgA/cHEAfgBDcQB+AERwcQB+AEhxAH4ASXNxAH4AT3NxAH4AKHNxAH4AKHBwcQB+AD9wcQB+AFNwcQB+AFRwcQB+AFZxAH4AV3EAfgBgc3IAHnZjLmRhdGEuVEFDQ21kJFNpbXBsZSRDYWxsQ29yZaEphUcEgWZ6AgALTAAIY2FsbFR5cGVxAH4AC0wAA2dhc3EAfgANTAAGaW5CYXNlcQB+AB1MAAhpbk9mZnNldHEAfgANTAAGaW5TaXplcQB+AA1MAARtZXRhcQB+ACNMAAdvdXRCYXNlcQB+AB1MAAlvdXRPZmZzZXRxAH4ADUwAB291dFNpemVxAH4ADUwAAnRvcQB+AA1MAAV2YWx1ZXEAfgANeHIAFXZjLmRhdGEuVEFDQ21kJFNpbXBsZe0m1iUxBnXSAgAAeHIAE3ZjLmRhdGEuVEFDQ21kJFNwZWMbq/EA+MEDvgIAAHhyAA52Yy5kYXRhLlRBQ0NtZFTLD4g8OR/wAgAAeHBxAH4AeHNxAH4AT3NxAH4AKHNxAH4AKHBwcQB+AD9wcQB+AFNwcQB+AFRwcQB+AH1xAH4AfnNxAH4AInNxAH4AKHBzcQB+AChwc3EAfgAocHBxAH4ANXBxAH4APnEAfgA/cHEAfgBDcQB+AERwcQB+AEhxAH4ASXNxAH4AT3NxAH4AKHNxAH4AKHBwcQB+AD9wcQB+AFNwcQB+AFRwcQB+AFZxAH4AV3NyABp2Yy5kYXRhLlRBQ1N5bWJvbCRWYXIkRnVsbBPmPQsuB0CVAgAESQAJY2FsbEluZGV4TAAEbWV0YXEAfgAjTAAKbmFtZVByZWZpeHEAfgAkTAADdGFncQB+AB54cQB+ACUAAAACc3EAfgAoc3EAfgAocHBxAH4AP3BxAH4AU3BxAH4AVHBzcQB+ADsAAAP3dAAITENBTk9ONDVxAH4AWXNxAH4AKHBwc3EAfgAyfnEAfgA2dAAJQ2FsbFRyYWNldAAIdGFjLm1ldGF2cgATdmMuZGF0YS5UQUNNZXRhSW5mbzVgTP2lS6hxAgAGSQAFYmVnaW5JAANsZW5JAAZzb3VyY2VMAAdhZGRyZXNzcQB+ABdMAAhqdW1wVHlwZXQAE0xjb21waWxlci9KdW1wVHlwZTtMAA1zb3VyY2VDb250ZXh0dAAYTGNvbXBpbGVyL1NvdXJjZUNvbnRleHQ7eHBwc3EAfgCgAABGMgAAACIAAAAAc3EAfgBh///////////////+/////gAAAAF1cQB+AGQAAAAQzkYEoAAAAAAAAAAAAAAAA3h+cgARY29tcGlsZXIuSnVtcFR5cGUAAAAAAAAAABIAAHhxAH4AN3QAB1JFR1VMQVJzcgAWY29tcGlsZXIuU291cmNlQ29udGV4dIzLW+lAXNoTAgACTAAPaW5kZXhUb0ZpbGVwYXRocQB+ABlMAAlzb3VyY2VEaXJxAH4AJHhwc3EAfgBaP0AAAAAAAAZ3CAAAAAgAAAADcQB+AD50ABNjb250cmFjdHMvRVJDMjAuc29sc3EAfgA7AAAAAXQAFGNvbnRyYWN0cy9JRVJDMjAuc29sc3EAfgA7AAAAAnQAHGNvbnRyYWN0cy9JRVJDMjBNZXRhZGF0YS5zb2x4dAATLnBvc3RfYXV0b2ZpbmRlcnMuMHNxAH4AInNxAH4AKHBzcQB+AChwc3EAfgAocHBxAH4ANXBxAH4APnEAfgA/cHEAfgBDcQB+AERwcQB+AEhxAH4ASXNxAH4AT3NxAH4AKHNxAH4AKHBwcQB+AD9wcQB+AFNwcQB+AFRwcQB+AHFxAH4AV3EAfgBzc3EAfgBPc3EAfgAoc3EAfgAoc3EAfgAocHBxAH4AP3BxAH4AU3NxAH4AKHBwc3EAfgAycQB+ADh0AA90YWMuaXMtdGVtcC12YXJxAH4AR3BxAH4ASHNxAH4AMnEAfgA4dAAXdGFjLmVudi5rbm93bi1iaXQtd2lkdGhxAH4APXBzcQB+ADsAAACgcHEAfgBUcHNxAH4AOwAAA/x0AARSMTA4c3EAfgBPc3EAfgAoc3EAfgAocHBxAH4AP3BxAH4AU3BxAH4AVHBzcQB+ADsAAAP1dAAEUjE2N3NxAH4AInNxAH4AKHBzcQB+AChwc3EAfgAocHBxAH4ANXBxAH4APnEAfgA/cHEAfgBDcQB+AERwcQB+AEhxAH4ASXNxAH4AT3NxAH4AKHNxAH4AKHBwcQB+AD9wcQB+AFNwcQB+AFRwcQB+AHFxAH4AV3EAfgBzc3IAG2tvdGxpbi5jb2xsZWN0aW9ucy5FbXB0eVNldC9GsBV21+L0AgAAeHBzcQB+AE9zcQB+AChzcQB+AChzcQB+AChwcHEAfgA/cHEAfgBTc3EAfgAocHBxAH4Av3BxAH4ASHEAfgDBcHEAfgDDcHEAfgBUcHEAfgDEcQB+AMVzcQB+AE9zcQB+AChzcQB+AChwcHEAfgA/cHEAfgBTcHEAfgBUcHEAfgDJcQB+AMpzcgBNcmVwb3J0LmNhbGxyZXNvbHV0aW9uLkNhbGxSZXNvbHV0aW9uVGFibGVTdW1tYXJ5SW5mbyRIYXZvY0luZm8kVW5yZXNvbHZlZENhbGybf2YyS18sawIAAUwACWhhdm9jVHlwZXQAIUxhbmFseXNpcy9pY2ZnL0hhdm9jZXIkSGF2b2NUeXBlO3hyAD5yZXBvcnQuY2FsbHJlc29sdXRpb24uQ2FsbFJlc29sdXRpb25UYWJsZVN1bW1hcnlJbmZvJEhhdm9jSW5mb2jNPQ8aqLW0AgAAeHIANHJlcG9ydC5jYWxscmVzb2x1dGlvbi5DYWxsUmVzb2x1dGlvblRhYmxlU3VtbWFyeUluZm/6oMji4aK8IQIAAUwADWluZm8kZGVsZWdhdGV0AA1Ma290bGluL0xhenk7eHBzcgAaa290bGluLkluaXRpYWxpemVkTGF6eUltcGx7x3/xICqBjQIAAUwABXZhbHVlcQB+ACl4cHNyAClrb3RsaW4uY29sbGVjdGlvbnMuYnVpbGRlcnMuU2VyaWFsaXplZE1hcAAAAAAAAAAADAAAeHB3BQAAAAADdAAac3VtbWFyeSBhcHBsaWNhdGlvbiByZWFzb250ACJjaG9zZW4gYXV0b21hdGljYWxseSBieSB0aGUgUHJvdmVydAALaGF2b2Mgc2NvcGV0AD1hbGwgY29udHJhY3RzIGV4Y2VwdCBFUkMyMCAoY2U0NjA0YTAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDMpdAALaGF2b2MgY2F1c2V0AD9UaGUgUHJvdmVyIGNvdWxkIG5vdCByZXNvbHZlIHRoZSBjYWxsZWUsIHRodXMsIGhhdm9jJ2QgdGhlIGNhbGx4c3IAKWFuYWx5c2lzLmljZmcuSGF2b2NlciRIYXZvY1R5cGUkQWxsRXhjZXB0IFr0XgikebsCAAFMAB1leGNsdWRlQWRkcmVzc0FuZENvbnRyYWN0TmFtZXEAfgAZeHIAH2FuYWx5c2lzLmljZmcuSGF2b2NlciRIYXZvY1R5cGWvwEl7loDZSwIAAHhwc3IAImphdmEudXRpbC5Db2xsZWN0aW9ucyRTaW5nbGV0b25NYXCfIwmRcX9rkQIAAkwAAWtxAH4AKUwAAXZxAH4AKXhwcQB+AKV0AAVFUkMyMHEAfgCkc3IALXNwZWMuY3ZsYXN0LlNwZWNDYWxsU3VtbWFyeSRIYXZvY1N1bW1hcnkkQXV0b7oQrzUhSMsMAgACWgAKdW5yZXNvbHZlZEwACGN2bFJhbmdldAAWTHNwZWMvY3ZsYXN0L0NWTFJhbmdlO3hyAChzcGVjLmN2bGFzdC5TcGVjQ2FsbFN1bW1hcnkkSGF2b2NTdW1tYXJ5RCyf9c4q4JQCAAB4cgAsc3BlYy5jdmxhc3QuU3BlY0NhbGxTdW1tYXJ5JEV4cHJlc3NpYmxlSW5DVkwEHG3pUuDAOwIAAHhyABtzcGVjLmN2bGFzdC5TcGVjQ2FsbFN1bW1hcnlgoWZBNKEcxwIAAHhwAXNyABpzcGVjLmN2bGFzdC5DVkxSYW5nZSRFbXB0eZ6SnnCSUeq+AgABTAAHY29tbWVudHEAfgAkeHIAFHNwZWMuY3ZsYXN0LkNWTFJhbmdlQnbt/uRv8nICAAB4cHQAAHNyABdqYXZhLnV0aWwuTGlua2VkSGFzaFNldNhs11qV3SoeAgAAeHIAEWphdmEudXRpbC5IYXNoU2V0ukSFlZa4tzQDAAB4cHcMAAAAED9AAAAAAAAFcQB+ANRxAH4A2XEAfgB6cQB+AINxAH4Af3g="}
		NopCmd
		AssumeExpCmd Lt(tacReturnsize!!209:98 0x100000000 )
		AssignExpCmd R223:25 Select(tacBalance!!207:2 Apply(to_skey:bif R6:17) )
		AssignExpCmd R224:25 Select(tacBalance!!207:2 Apply(to_skey:bif R108:97) )
		AssignHavocCmd tacBalance!!225:2
		AssignExpCmd B226:25 Le(R223:25 Select(tacBalance!!225:2 Apply(to_skey:bif R6:17) ) )
		AssumeCmd B226:25
		AssignExpCmd B227:25 Eq(R224:25 Select(tacBalance!!225:2 Apply(to_skey:bif R108:97) ) )
		AssumeCmd B227:25
		AnnotationCmd JSON{"key":{"name":"call.trace.external.summary.end","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		LabelCmd "Inline Summary(summaryType=UNRESOLVED AUTO summary @ unknownLocation)"
		LabelCmd "Parallel assignment for tacBalance!!228:wordmap := tacBalance!!225:wordmap"
	}
}
Axioms {
		CANON89
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
  "2": [
    {
      "key": {
        "name": "Tac.symbol.keyword",
        "type": "java.lang.String",
        "erasureStrategy": "Canonical"
      },
      "value": "tacBalance"
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
  "15": [
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
  "16": [
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
  "17": [
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
  "18": [
    {
      "key": {
        "name": "Tac.symbol.keyword",
        "type": "java.lang.String",
        "erasureStrategy": "Canonical"
      },
      "value": "tacSighash"
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
  "24": [
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
  "25": [
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
  "26": [
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
  "28": [
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
  "29": [
    {
      "key": {
        "name": "Tac.symbol.keyword",
        "type": "java.lang.String",
        "erasureStrategy": "Canonical"
      },
      "value": "tacCalldatasize"
    }
  ],
  "30": [
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
      "value": 1016
    }
  ],
  "34": [
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
  "35": [
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
  "36": [
    {
      "key": {
        "name": "Tac.symbol.keyword",
        "type": "java.lang.String",
        "erasureStrategy": "Canonical"
      },
      "value": "tacM0x0"
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
    }
  ],
  "38": [
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
  "39": [
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
  "40": [
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
              "namePrefix": "R26",
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
                "namePrefix": "R23",
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
                    "namePrefix": "R23",
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
                "namePrefix": "R26",
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
  "41": [
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
    }
  ],
  "47": [
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
  "48": [
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
              "namePrefix": "R60",
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
                "namePrefix": "R57",
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
                    "namePrefix": "R57",
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
                "namePrefix": "R60",
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
  "49": [
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
  "50": [
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
  "52": [
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
  "53": [
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
  "54": [
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
  "55": [
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
  "56": [
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
  "57": [
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
  "58": [
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
  "61": [
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
            "namePrefix": "I147",
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
            "namePrefix": "I148",
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
  "62": [
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
  "63": [
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
            "namePrefix": "CANON134",
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
            "namePrefix": "I151",
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
  "64": [
    {
      "key": {
        "name": "cvl",
        "type": "java.lang.Boolean",
        "erasureStrategy": "Canonical"
      },
      "value": true
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
            "namePrefix": "B149",
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
            "namePrefix": "CANON133!!152",
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
  "66": [
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
            "namePrefix": "I154",
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
            "namePrefix": "I155",
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
            "value": "2e1a7d4d"
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
            "value": "2e1a7d4d"
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
            "namePrefix": "B156",
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
  "75": [
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
  "76": [
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
  "77": [
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
  "78": [
    {
      "key": {
        "name": "tac.meta",
        "type": "vc.data.TACMetaInfo",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "source": 3,
        "begin": 2032,
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
      "value": 1017
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
      "value": 1013
    }
  ],
  "82": [
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
  "83": [
    {
      "key": {
        "name": "tac.meta",
        "type": "vc.data.TACMetaInfo",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "source": 0,
        "begin": 17878,
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
      "value": 1021
    }
  ],
  "85": [
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
  "86": [
    {
      "key": {
        "name": "tac.meta",
        "type": "vc.data.TACMetaInfo",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "source": 0,
        "begin": 17878,
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
              "namePrefix": "R108",
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
                "namePrefix": "R108",
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
              },
              "hashResult": {
                "#class": "vc.data.TACSymbol.Var.Full",
                "namePrefix": "CANON83",
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
  "88": [
    {
      "key": {
        "name": "tac.meta",
        "type": "vc.data.TACMetaInfo",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "source": 0,
        "begin": 17910,
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
  "89": [
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
  "90": [
    {
      "key": {
        "name": "tac.meta",
        "type": "vc.data.TACMetaInfo",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "source": 0,
        "begin": 17910,
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
              "namePrefix": "R108",
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
                "namePrefix": "R108",
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
                    "value": 1018
                  }
                ]
              },
              "baseSlot": {
                "#class": "vc.data.TACSymbol.Var.Full",
                "namePrefix": "CANON86",
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
  "92": [
    {
      "key": {
        "name": "tac.meta",
        "type": "vc.data.TACMetaInfo",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "source": 3,
        "begin": 13838,
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
      "value": 1014
    }
  ],
  "94": [
    {
      "key": {
        "name": "tac.meta",
        "type": "vc.data.TACMetaInfo",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "source": 0,
        "begin": 17970,
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
    }
  ],
  "95": [
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
  "96": [
    {
      "key": {
        "name": "Tac.symbol.keyword",
        "type": "java.lang.String",
        "erasureStrategy": "Canonical"
      },
      "value": "tacCond"
    }
  ],
  "97": [
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
      "value": 1020
    }
  ],
  "98": [
    {
      "key": {
        "name": "Tac.symbol.keyword",
        "type": "java.lang.String",
        "erasureStrategy": "Canonical"
      },
      "value": "tacReturnsize"
    }
  ],
  "99": [
    {
      "key": {
        "name": "Tac.symbol.keyword",
        "type": "java.lang.String",
        "erasureStrategy": "Canonical"
      },
      "value": "tacRC"
    }
  ],
  "100": [
    {
      "key": {
        "name": "tac.transfers.balance",
        "type": "tac.MetaMap$Companion$NothingValue",
        "erasureStrategy": "Canonical"
      },
      "value": {
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
        "name": "tac.is-temp-var",
        "type": "tac.MetaMap$Companion$NothingValue",
        "erasureStrategy": "Canonical"
      },
      "value": {
      }
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
  "102": [
    {
      "key": {
        "name": "Tac.symbol.keyword",
        "type": "java.lang.String",
        "erasureStrategy": "Canonical"
      },
      "value": "tacReturndata"
    },
    {
      "key": {
        "name": "tac.is.returndata",
        "type": "tac.MetaMap$Companion$NothingValue",
        "erasureStrategy": "Canonical"
      },
      "value": {
      }
    }
  ],
  "103": [
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
  "104": [
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
  "105": [
    {
      "key": {
        "name": "ReachVar",
        "type": "tac.NBId",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "tac.BlockIdentifier",
        "origStartPc": 2029,
        "stkTop": 1018,
        "decompCopy": 0,
        "calleeIdx": 2,
        "topOfStackValue": 0,
        "freshCopy": 3
      }
    }
  ],
  "106": [
    {
      "key": {
        "name": "ReachVar",
        "type": "tac.NBId",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "tac.BlockIdentifier",
        "origStartPc": 2,
        "stkTop": 0,
        "decompCopy": 0,
        "calleeIdx": 2,
        "topOfStackValue": 0,
        "freshCopy": 0
      }
    }
  ]
}