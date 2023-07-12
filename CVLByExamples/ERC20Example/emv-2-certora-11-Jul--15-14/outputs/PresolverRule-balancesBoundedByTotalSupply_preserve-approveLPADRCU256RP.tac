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
		CANON119:JSON{"name":"CANON119","paramSorts":[],"returnSort":{"#class":"tac.Tag.Int"},"attribute":"Ghost","cvlResultType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Mathint"},"cvlParamTypes":[],"declarationName":"CANON119"}
	}
	tacM0x20@4:bv256
	tacCaller@4:bv256
	tacCalldatabufCANON0@4:bv256
	tacCalldatabufCANON1@4:bv256
	tacMCANON0!!1:bytemap
	tacM0x0!!47:bv256
	tacM0x0!!70:bv256
	tacAddress!!35:bv256
	tacAddress!!58:bv256
	tacAddress!!78:bv256
	tacAddress!!96:bv256
	tacOrigin!!181:bv256
	tacCallvalue@4:bv256
	lastReverted:bool
	lastReverted@1:bool
	lastReverted@2:bool
	lastReverted@3:bool
	lastReverted@4:bool
	lastReverted@5:bool
	lastReverted@6:bool
	lastReverted@7:bool
	tacM0x0!!108:bv256
	tacM0x0!!131:bv256
	tacM0x0!!229:bv256
	tacM0x0!!232:bv256
	tacExtcodesize!!0:wordmap
	CANON31!!3:wordmap
	CANON46!!4:bv256
	tacCalldatasize@1:bv256
	tacCalldatasize@2:bv256
	tacCalldatasize@3:bv256
	tacCalldatasize@4:bv256
	tacCalldatasize@5:bv256
	tacCalldatasize@6:bv256
	tacCalldatasize@7:bv256
	tacCalldatasize!!113:bv256
	tacCalldatasize!!136:bv256
	tacCalldatasize!!162:bv256
	tacM0x0@1:bv256
	tacM0x0@2:bv256
	tacM0x0@4:bv256
	tacM0x0@5:bv256
	tacM0x0@6:bv256
	tacExtcodesize:wordmap
	CANON100:bool
	CANON101:bv256
	CANON102:bool
	CANON103:bool
	CANON104:int
	CANON105:int
	CANON106:bool
	CANON107:bool
	CANON108:bool
	CANON109:bv256
	CANON110:bool
	CANON111:bool
	CANON112:int
	CANON113:int
	CANON114:bool
	CANON115:bool
	CANON116:int
	CANON117:int
	CANON118:bool
	CANON119:int
	tacSighash!!6:bv256
	tacSighash!!7:bv256
	tacSighash!!8:bv256
	tacSighash!!9:bv256
	tacCalldatasize!!29:bv256
	tacCalldatasize!!52:bv256
	tacCalldatasize!!75:bv256
	tacCalldatasize!!90:bv256
	tacMCANON0@4:bytemap
	tacMCANON1@4:bytemap
	tacBalance:wordmap
	tacTimestamp!!191:bv256
	tacNumber@4:bv256
	tacBalance!!2:wordmap
	R5:bv256
	B13:bool
	B14:bool
	B15:bool
	B16:bool
	B17:bool
	B18:bool
	B19:bool
	B20:bool
	B21:bool
	B22:bool
	B23:bool
	B24:bool
	B25:bool
	B27:bool
	B30:bool
	B31:bool
	B32:bool
	B34:bool
	B37:bool
	B38:bool
	B39:bool
	B40:bool
	B41:bool
	B43:bool
	B45:bool
	B53:bool
	B54:bool
	B55:bool
	B57:bool
	B60:bool
	B61:bool
	B62:bool
	B63:bool
	B64:bool
	B66:bool
	B68:bool
	B76:bool
	B77:bool
	B80:bool
	B81:bool
	B82:bool
	B83:bool
	B84:bool
	B85:bool
	B86:bool
	B91:bool
	B92:bool
	B93:bool
	B95:bool
	B98:bool
	B99:bool
	I28:int
	I51:int
	I74:int
	I89:int
	R26:bv256
	R33:bv256
	R36:bv256
	R42:bv256
	R44:bv256
	R46:bv256
	R48:(uninterp) skey
	R49:bv256
	R50:bv256
	R56:bv256
	R59:bv256
	R65:bv256
	R67:bv256
	R69:bv256
	R71:(uninterp) skey
	R72:bv256
	R73:bv256
	R79:bv256
	R87:bv256
	R88:bv256
	R94:bv256
	R97:bv256
	B100:bool
	B101:bool
	B102:bool
	B104:bool
	B106:bool
	B114:bool
	B115:bool
	B116:bool
	B118:bool
	B121:bool
	B122:bool
	B123:bool
	B124:bool
	B125:bool
	B127:bool
	B129:bool
	B137:bool
	B138:bool
	B141:bool
	B142:bool
	B143:bool
	B144:bool
	B145:bool
	B146:bool
	B147:bool
	B154:bool
	B163:bool
	B164:bool
	B168:bool
	B171:bool
	B173:bool
	B176:bool
	B179:bool
	B182:bool
	B184:bool
	B187:bool
	B189:bool
	B192:bool
	B194:bool
	B197:bool
	B206:bool
	B210:bool
	B212:bool
	B213:bool
	B214:bool
	B215:bool
	B216:bool
	B217:bool
	B218:bool
	B220:bool
	B222:bool
	B225:bool
	B227:bool
	I112:int
	I135:int
	I150:int
	I151:int
	I152:int
	I153:int
	I155:int
	I156:int
	I157:int
	I158:int
	I159:int
	I167:int
	I172:int
	I178:int
	I183:int
	I188:int
	I193:int
	I196:int
	I202:int
	I207:int
	I208:int
	I209:int
	I235:int
	M160:bytemap
	R103:bv256
	R105:bv256
	R107:bv256
	R109:(uninterp) skey
	R110:bv256
	R111:bv256
	R117:bv256
	R120:bv256
	R126:bv256
	R128:bv256
	R130:bv256
	R132:(uninterp) skey
	R133:bv256
	R134:bv256
	R140:bv256
	R148:bv256
	R149:bv256
	R161:bv256
	R165:bv256
	R166:bv256
	R169:bv256
	R174:bv256
	R180:bv256
	R185:bv256
	R190:bv256
	R195:bv256
	R198:bv256
	R199:bv256
	R200:bv256
	R201:bv256
	R204:bv256
	R205:bv256
	R211:bv256
	R219:bv256
	R221:bv256
	R223:bv256
	R224:bv256
	R226:bv256
	R228:bv256
	R230:bv256
	R231:bv256
	R234:bv256
	tacAddress@1:bv256
	tacAddress@2:bv256
	tacAddress@3:bv256
	tacAddress@4:bv256
	tacAddress@5:bv256
	tacAddress@6:bv256
	tacAddress@7:bv256
	LCANON0@1:bool
	LCANON0@2:bool
	LCANON0@3:bool
	LCANON0@4:bool
	LCANON0@5:bool
	LCANON0@6:bool
	LCANON0@7:bool
	LCANON1@1:bool
	LCANON1@2:bool
	LCANON1@3:bool
	LCANON1@4:bool
	LCANON1@5:bool
	LCANON1@6:bool
	LCANON1@7:bool
	LCANON2@1:bool
	LCANON2@2:bool
	LCANON2@5:bool
	LCANON2@6:bool
	LCANON3@1:bool
	LCANON3@2:bool
	LCANON3@5:bool
	LCANON3@6:bool
	LCANON4@1:bv256
	LCANON4@2:bv256
	LCANON4@5:bv256
	LCANON4@6:bv256
	LCANON5@1:bv256
	LCANON5@2:bv256
	LCANON5@5:bv256
	LCANON5@6:bv256
	LCANON6@1:bool
	LCANON6@2:bool
	LCANON6@5:bool
	LCANON6@6:bool
	LCANON7@1:bv256
	LCANON7@2:bv256
	LCANON7@5:bv256
	LCANON7@6:bv256
	LCANON8@1:bv256
	LCANON8@2:bv256
	LCANON8@5:bv256
	LCANON8@6:bv256
	LCANON9@1:bool
	LCANON9@2:bool
	LCANON9@5:bool
	LCANON9@6:bool
	tacCallvalue!!175:bv256
	tacOrigin@4:bv256
	CANON10:int
	CANON11:int
	CANON12:int
	CANON13:int
	CANON14:int
	CANON15:int
	CANON16:int
	CANON17:bool
	CANON18:bool
	CANON19:bool
	CANON20:bv256
	CANON21:bool
	CANON22:int
	CANON23:bool
	CANON24:bool
	CANON25:bool
	CANON26:bv256
	CANON27:bool
	CANON28@1:bv256
	CANON28@2:bv256
	CANON28@3:bv256
	CANON28@4:bv256
	CANON28@5:bv256
	CANON28@6:bv256
	CANON28@7:bv256
	CANON29@1:bool
	CANON29@2:bool
	CANON29@3:bool
	CANON29@4:bool
	CANON29@5:bool
	CANON29@6:bool
	CANON29@7:bool
	CANON30:bool
	CANON31:wordmap
	CANON34:int
	CANON35:int
	CANON36:bool
	CANON37:bool
	CANON38:bool
	CANON39:bv256
	CANON40:bool
	CANON41:bool
	CANON42:int
	CANON43:int
	CANON44:bool
	CANON45:bool
	CANON46:bv256
	CANON47:int
	CANON48:int
	CANON49:bool
	CANON50:int
	CANON51:int
	CANON52:int
	CANON53:int
	CANON54:int
	CANON55:bytemap
	CANON56:bytemap
	CANON57:bv256
	CANON58:bv256
	CANON59:bool
	CANON60:bool
	CANON61:bv256
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
	CANON75:int
	CANON76:bool
	CANON77:bv256
	CANON78:int
	CANON79:bool
	CANON80:bv256
	CANON81:int
	CANON82:bool
	CANON83:bv256
	CANON84:bv256
	CANON85:bv256
	CANON86:bv256
	CANON87:int
	CANON88:bv256
	CANON89:bv256
	CANON90:bool
	CANON91:bool
	CANON96:wordmap
	CANON97:int
	CANON98:bool
	CANON99:bool
	LCANON10@1:bv256
	LCANON10@2:bv256
	LCANON10@5:bv256
	LCANON10@6:bv256
	LCANON11@1:bv256
	LCANON11@2:bv256
	LCANON11@5:bv256
	LCANON11@6:bv256
	LCANON12@1:bv256
	LCANON12@2:bv256
	LCANON12@5:bv256
	LCANON12@6:bv256
	LCANON13@1:bv256
	LCANON13@2:bv256
	LCANON13@5:bv256
	LCANON13@6:bv256
	LCANON14@1:bv256
	LCANON14@2:bv256
	LCANON14@5:bv256
	LCANON14@6:bv256
	LCANON15@3:bool
	LCANON15@4:bool
	LCANON15@7:bool
	LCANON16@3:bool
	LCANON16@4:bool
	LCANON16@7:bool
	LCANON17@3:bool
	LCANON17@4:bool
	LCANON17@7:bool
	LCANON18@3:bool
	LCANON18@7:bool
	LCANON19@3:bv256
	LCANON19@7:bv256
	LCANON20@3:bv256
	LCANON20@7:bv256
	LCANON21@3:bv256
	LCANON21@7:bv256
	LCANON22@4:bv256
	LCANON23@4:bool
	LCANON24@4:bv256
	LCANON25@4:bool
	LCANON26@4:bv256
	LCANON27@4:bv256
	LCANON28@4:bool
	LCANON29@4:bv256
	LCANON30@4:bv256
	LCANON31@4:bool
	LCANON32@4:bv256
	LCANON33@4:bool
	LCANON34@4:bv256
	LCANON35@4:bv256
	LCANON36@4:bv256
	LCANON37@4:bv256
	LCANON38@4:bv256
	LCANON39@4:bv256
	LCANON40@4:bv256
	LCANON41@4:bv256
	LCANON42@4:bv256
	LCANON43@4:bv256
	LCANON44@4:bv256
	tacContractAtCANON0:bv256
	lastHasThrown:bool
	lastHasThrown@1:bool
	lastHasThrown@2:bool
	lastHasThrown@3:bool
	lastHasThrown@4:bool
	lastHasThrown@5:bool
	lastHasThrown@6:bool
	lastHasThrown@7:bool
	tacM0x20!!233:bv256
	tacAddress!!119:bv256
	tacAddress!!139:bv256
	tacAddress!!177:bv256
	CANON0:int
	CANON1:bool
	CANON2:bool
	CANON3:bool
	CANON4:int
	CANON5:bool
	CANON6:int
	CANON7:bool
	CANON8:int
	CANON9:int
	tacCaller!!170:bv256
	tacBalance!!203:wordmap
	tacTimestamp@4:bv256
	tacSighash!!10:bv256
	tacSighash!!11:bv256
	tacSighash!!12:bv256
	tacSighash@1:bv256
	tacSighash@2:bv256
	tacSighash@3:bv256
	tacSighash@4:bv256
	tacSighash@5:bv256
	tacSighash@6:bv256
	tacSighash@7:bv256
	tacNumber!!186:bv256
}
Program {
	Block 0_0_0_0_0_0 Succ [0_0_0_1_0_0] {
		AssignHavocCmd tacExtcodesize!!0:0
		AssignHavocCmd tacBalance!!2:1
		AssignHavocCmd CANON31!!3:2
		AssignHavocCmd CANON46!!4:3
		AssignHavocCmd CANON56:4
		AssignHavocCmd CANON58:5
		AssignHavocCmd R5:6
		AssignHavocCmd tacSighash!!6:7
		AssignHavocCmd tacSighash!!7:7
		AssignHavocCmd tacSighash!!8:7
		AssignHavocCmd tacSighash!!9:7
		AssignHavocCmd tacSighash!!10:7
		AssignHavocCmd tacSighash!!11:7
		AssignHavocCmd tacSighash!!12:7
		AssignExpCmd CANON0:8 0x95ea7b3
		AssignExpCmd CANON1:9 false
		AssignExpCmd CANON2:10 false
		AssignExpCmd CANON3:11 false
		AssignExpCmd CANON4:12 0x2
		AssignExpCmd CANON5:13 false
		AnnotationCmd JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Message","s":"Setup"}}
		AnnotationCmd JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Message","s":"multi contract setup"}}
		AnnotationCmd JSON{"key":{"name":"cvl.label.end","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		AnnotationCmd JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Message","s":"rule parameters setup"}}
		AssignHavocCmd CANON6:14
		NopCmd
		AssumeExpCmd LAnd(Le(CANON6:14 0xffffffffffffffffffffffffffffffffffffffff ) Ge(CANON6:14 0x0 ) )
		AssignHavocCmd CANON8:15
		NopCmd
		AssumeExpCmd LAnd(Le(CANON8:15 0xffffffffffffffffffffffffffffffffffffffff ) Ge(CANON8:15 0x0 ) )
		AssumeCmd true
		AssumeCmd true
		AssignHavocCmd CANON9:16
		AssignHavocCmd CANON10:17
		AssignHavocCmd CANON11:18
		AssignHavocCmd CANON12:19
		AssignHavocCmd CANON13:20
		AssignHavocCmd CANON14:21
		AssignHavocCmd CANON15:22
		AssignHavocCmd CANON16:23
		NopCmd
		AssumeExpCmd LAnd(Le(CANON9:16 0xffffffffffffffffffffffffffffffffffffffff ) Ge(CANON9:16 0x0 ) )
		NopCmd
		AssumeExpCmd LAnd(Le(CANON10:17 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff ) Ge(CANON10:17 0x0 ) )
		NopCmd
		AssumeExpCmd LAnd(Le(CANON11:18 0xffffffffffffffffffffffffffffffffffffffff ) Ge(CANON11:18 0x0 ) )
		NopCmd
		AssumeExpCmd LAnd(Le(CANON12:19 0xffffffffffffffffffffffffffffffffffffffff ) Ge(CANON12:19 0x0 ) )
		NopCmd
		AssumeExpCmd LAnd(Le(CANON13:20 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff ) Ge(CANON13:20 0x0 ) )
		NopCmd
		AssumeExpCmd LAnd(Le(CANON14:21 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff ) Ge(CANON14:21 0x0 ) )
		NopCmd
		AssumeExpCmd LAnd(Le(CANON15:22 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff ) Ge(CANON15:22 0x0 ) )
		NopCmd
		AssumeExpCmd LAnd(Le(CANON16:23 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff ) Ge(CANON16:23 0x0 ) )
		AnnotationCmd JSON{"key":{"name":"cvl.label.end","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		AnnotationCmd JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Message","s":"contract address vars initialized"}}
		AnnotationCmd JSON{"key":{"name":"cvl.label.end","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		AnnotationCmd JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Message","s":"setup read tracking instrumentation"}}
		AnnotationCmd JSON{"key":{"name":"cvl.label.end","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		AnnotationCmd JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Message","s":"last storage initialize"}}
		AnnotationCmd JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageGlobalChangeSnippet.StorageTakeSnapshot","lhs":{"namePrefix":"lastStorage","tag":{"#class":"tac.Tag.BlockchainState"},"callIndex":0,"meta":[{"key":{"name":"cvl.local","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true},{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"lastStorage"},{"key":{"name":"cvl.type","type":"spec.cvlast.CVLType$PureCVLType","erasureStrategy":"CallTrace"},"value":{"#class":"spec.cvlast.CVLType.PureCVLType.VMInternal.BlockchainState"}},{"key":{"name":"cvl","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true},{"key":{"name":"cvl.display","type":"java.lang.String","erasureStrategy":"CallTrace"},"value":"lastStorage"}]}}}
		AnnotationCmd JSON{"key":{"name":"cvl.label.end","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		AnnotationCmd JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Message","s":"assumptions about extcodesize"}}
		AssignExpCmd B23:24 Gt(Select(tacExtcodesize!!0:0 Apply(to_skey:bif R5:6) ) 0x0 )
		AssumeCmd B23:24
		AnnotationCmd JSON{"key":{"name":"cvl.label.end","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		AnnotationCmd JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Message","s":"assumptions about contracts' addresses"}}
		NopCmd
		AssumeExpCmd Gt(R5:6 0x0 )
		NopCmd
		AssumeExpCmd Le(R5:6 0xffffffffffffffffffffffffffffffffffffffff )
		AnnotationCmd JSON{"key":{"name":"cvl.label.end","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		AnnotationCmd JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Message","s":"assumptions about starting balances"}}
		AssignExpCmd R26:24 Select(tacBalance!!2:1 Apply(to_skey:bif R5:6) )
		NopCmd
		AssumeExpCmd Ge(R26:24 0x0 )
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
		AnnotationCmd:25 JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Message","s":"assume invariant in pre-state"}}
		AssignExpCmd:26 I28 CANON6:14
	}
	Block 0_0_0_1_0_0 Succ [1_0_0_0_0_0] {
		AnnotationCmd:25 JSON{"key":{"name":"call.trace.push","type":"analysis.icfg.Inliner$CallStack$PushRecord","erasureStrategy":"Canonical"},"value":"rO0ABXNyACphbmFseXNpcy5pY2ZnLklubGluZXIkQ2FsbFN0YWNrJFB1c2hSZWNvcmSX8+DCTLCH+AIAA0kACGNhbGxlZUlkTAAGY2FsbGVldAATTHZjL2RhdGEvTWV0aG9kUmVmO0wAB3N1bW1hcnl0ABVMdmMvZGF0YS9DYWxsU3VtbWFyeTt4cAAAAAFzcgARdmMuZGF0YS5NZXRob2RSZWbJlJTzzU9pGAIAA0wABGF0dHJ0ABdMc2NlbmUvTWV0aG9kQXR0cmlidXRlO0wACmNvbnRyYWN0SWR0ABZMamF2YS9tYXRoL0JpZ0ludGVnZXI7TAAHc2lnSGFzaHQAEExldm0vU2lnaGFzaEludDt4cHNyABxzY2VuZS5NZXRob2RBdHRyaWJ1dGUkQ29tbW9uNHjdebdr9XMCAAB4cgAVc2NlbmUuTWV0aG9kQXR0cmlidXRlcYg2pYWutuUCAAB4cHNyABRqYXZhLm1hdGguQmlnSW50ZWdlcoz8nx+pO/sdAwAGSQAIYml0Q291bnRJAAliaXRMZW5ndGhJABNmaXJzdE5vbnplcm9CeXRlTnVtSQAMbG93ZXN0U2V0Qml0SQAGc2lnbnVtWwAJbWFnbml0dWRldAACW0J4cgAQamF2YS5sYW5nLk51bWJlcoaslR0LlOCLAgAAeHD///////////////7////+AAAAAXVyAAJbQqzzF/gGCFTgAgAAeHAAAAAQzkYEoAAAAAAAAAAAAAAAA3hzcgAOZXZtLlNpZ2hhc2hJbnRUdcqNMXEgeAIAAUwAAW5xAH4ABnhwc3EAfgAM///////////////+/////gAAAAF1cQB+ABAAAAAEcKCCMXhw"}
		AssignHavocCmd:25 tacCalldatasize!!29:27
		NopCmd
		AssumeExpCmd Apply(add_noofl:bif 0x4 0x20)
		NopCmd
		AssumeExpCmd Apply(add_noofl:bif 0x4 0x0)
		AssignExpCmd:25 B32 LAnd(Ge(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff I28 ) Le(0x0 I28 ) )
		AssertCmd:25 B32 "sanity bounds check on cvl to vm encoding of certoraArg29792980:int failed"
		AssignExpCmd:25 R33 Apply(safe_math_narrow:bif I28)
		NopCmd
		AssumeExpCmd Eq(0x24 tacCalldatasize!!29:27 )
		LabelCmd:25 "Start procedure ERC20-balanceOf(address)"
		AnnotationCmd:25 JSON{"key":{"name":"fps.free-pointer-is-scalarized","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true}
		AssignExpCmd:25 R36:24 Select(tacExtcodesize!!0:0 Apply(to_skey:bif R5:28) )
		NopCmd
		AssumeExpCmd Gt(R36:24 0x0 )
		AnnotationCmd:25 JSON{"key":{"name":"internal.func.finder.info","type":"analysis.ip.InternalFunctionFinderReport","erasureStrategy":"Erased"},"value":"rO0ABXNyAChhbmFseXNpcy5pcC5JbnRlcm5hbEZ1bmN0aW9uRmluZGVyUmVwb3J0ian+bYn1VdACAAFMABN1bnJlc29sdmVkRnVuY3Rpb25zdAAPTGphdmEvdXRpbC9TZXQ7eHBzcgAhZGF0YXN0cnVjdHVyZXMuTGlua2VkQXJyYXlIYXNoU2V0AAAAAAAAAAEDAAJGAApsb2FkRmFjdG9yTAAJaGFzaFRhYmxldAAuTGRhdGFzdHJ1Y3R1cmVzL2FycmF5aGFzaHRhYmxlL0FycmF5SGFzaFRhYmxlO3hwdwgAAAAAQAAAAHg="}
		AnnotationCmd:25 JSON{"key":{"name":"fps.free-pointer-is-scalarized","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true}
		NopCmd
		AssumeExpCmd LNot(Lt(tacCalldatasize!!29:27 0x4 ) )
		NopCmd
		AssumeExpCmd LNot(Gt(0x70a08231 tacSighash!!6:7 ) )
		NopCmd
		AssumeExpCmd Gt(0xa9059cbb tacSighash!!6:7 )
		NopCmd
		AssumeExpCmd Eq(0x70a08231 tacSighash!!6:7 )
		AssumeCmd:29 true
		AssignExpCmd:30 R42:31 Sub(tacCalldatasize!!29:27 0x4 )
		NopCmd
		AssumeExpCmd LNot(Slt(R42:31 0x20 ) )
		NopCmd
		AssumeExpCmd Le(R33 0xffffffffffffffffffffffffffffffffffffffff )
		AnnotationCmd:25 JSON{"key":{"name":"internal.func.start","type":"analysis.ip.InternalFuncStartAnnotation","erasureStrategy":"CallTrace"},"value":{"id":0,"startPc":3130,"args":[{"s":{"namePrefix":"R33","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1013}]},"offset":1,"sort":"SCALAR"}],"methodSignature":{"#class":"spec.cvlast.QualifiedMethodSignature.QualifiedMethodSig","qualifiedMethodName":{"#class":"spec.cvlast.QualifiedFunction","host":{"name":"ERC20"},"methodId":"balanceOf"},"params":[{"#class":"spec.cvlast.VMParam.Named","name":"account","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$address"}}],"res":[{"#class":"spec.cvlast.VMParam.Unnamed","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256}}]},"stackOffsetToArgPos":{"1":0},"callSiteSrc":{"source":0,"begin":4328,"len":511,"jumpType":"ENTER","address":"ce4604a0000000000000000000000003","sourceContext":{"indexToFilepath":{"0":"contracts/ERC20.sol","1":"contracts/IERC20.sol","2":"contracts/IERC20Metadata.sol"},"sourceDir":".post_autofinders.0"}}}}
		AssignExpCmd:32 R48:33 Apply(hash_3_keccak:bif Apply(skey_basic:bif 0x40) Apply(to_skey:bif R33:34) Apply(skey_basic:bif 0x0))
		AssignExpCmd:35 R49:33 Select(CANON31!!3:2 R48:36 )
		AnnotationCmd:25 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet","value":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R49","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1020}]},"displayPath":{"#class":"analysis.storage.DisplayPath.MapAccess","key":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R33","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1018}]},"keyTyp":{"#class":"tac.TACStorageType.IntegralType","typeLabel":"address","numBytes":"14","descriptor":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$address"},"lowerBound":null,"upperBound":null},"base":{"#class":"analysis.storage.DisplayPath.Root","name":"_balances"}},"storageType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256},"contractInstance":"ce4604a0000000000000000000000003","linkableStorageReadId":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet.None"}}}
		AnnotationCmd:25 JSON{"key":{"name":"internal.func.end","type":"analysis.ip.InternalFuncExitAnnotation","erasureStrategy":"Canonical"},"value":{"id":0,"rets":[{"s":{"namePrefix":"R49","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1023}]},"offset":0}],"functionLayout":{"0":{"#class":"analysis.ip.InternalFuncValueLocation.Scalar"}}}}
		AnnotationCmd:25 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.EVMFunctionReturnWrite","returnbufOffset":"0","returnValueSym":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R49","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1023}]},"callIndex":1}}
		AnnotationCmd:25 JSON{"key":{"name":"tac.return.path","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		LabelCmd:25 "End procedure ERC20-balanceOf(address)"
		NopCmd
		AnnotationCmd:25 JSON{"key":{"name":"call.trace.pop","type":"analysis.icfg.Inliner$CallStack$PopRecord","erasureStrategy":"Canonical"},"value":"rO0ABXNyAClhbmFseXNpcy5pY2ZnLklubGluZXIkQ2FsbFN0YWNrJFBvcFJlY29yZPAPfwSLdCWJAgABSQAIY2FsbGVlSWR4cAAAAAE="}
	}
	Block 0_0_0_2_0_0 Succ [2_0_0_0_0_0] {
		AnnotationCmd:25 JSON{"key":{"name":"call.trace.push","type":"analysis.icfg.Inliner$CallStack$PushRecord","erasureStrategy":"Canonical"},"value":"rO0ABXNyACphbmFseXNpcy5pY2ZnLklubGluZXIkQ2FsbFN0YWNrJFB1c2hSZWNvcmSX8+DCTLCH+AIAA0kACGNhbGxlZUlkTAAGY2FsbGVldAATTHZjL2RhdGEvTWV0aG9kUmVmO0wAB3N1bW1hcnl0ABVMdmMvZGF0YS9DYWxsU3VtbWFyeTt4cAAAAAJzcgARdmMuZGF0YS5NZXRob2RSZWbJlJTzzU9pGAIAA0wABGF0dHJ0ABdMc2NlbmUvTWV0aG9kQXR0cmlidXRlO0wACmNvbnRyYWN0SWR0ABZMamF2YS9tYXRoL0JpZ0ludGVnZXI7TAAHc2lnSGFzaHQAEExldm0vU2lnaGFzaEludDt4cHNyABxzY2VuZS5NZXRob2RBdHRyaWJ1dGUkQ29tbW9uNHjdebdr9XMCAAB4cgAVc2NlbmUuTWV0aG9kQXR0cmlidXRlcYg2pYWutuUCAAB4cHNyABRqYXZhLm1hdGguQmlnSW50ZWdlcoz8nx+pO/sdAwAGSQAIYml0Q291bnRJAAliaXRMZW5ndGhJABNmaXJzdE5vbnplcm9CeXRlTnVtSQAMbG93ZXN0U2V0Qml0SQAGc2lnbnVtWwAJbWFnbml0dWRldAACW0J4cgAQamF2YS5sYW5nLk51bWJlcoaslR0LlOCLAgAAeHD///////////////7////+AAAAAXVyAAJbQqzzF/gGCFTgAgAAeHAAAAAQzkYEoAAAAAAAAAAAAAAAA3hzcgAOZXZtLlNpZ2hhc2hJbnRUdcqNMXEgeAIAAUwAAW5xAH4ABnhwc3EAfgAM///////////////+/////gAAAAF1cQB+ABAAAAAEcKCCMXhw"}
		AssignHavocCmd:25 tacCalldatasize!!52:27
		NopCmd
		AssumeExpCmd Apply(add_noofl:bif 0x4 0x20)
		NopCmd
		AssumeExpCmd Apply(add_noofl:bif 0x4 0x0)
		AssignExpCmd:25 B55 LAnd(Ge(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff I151 ) Le(0x0 I151 ) )
		AssertCmd:25 B55 "sanity bounds check on cvl to vm encoding of certoraArg29922993:int failed"
		AssignExpCmd:25 R56 Apply(safe_math_narrow:bif I151)
		NopCmd
		AssumeExpCmd Eq(0x24 tacCalldatasize!!52:27 )
		LabelCmd:25 "Start procedure ERC20-balanceOf(address)"
		AnnotationCmd:25 JSON{"key":{"name":"fps.free-pointer-is-scalarized","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true}
		AssignExpCmd:25 R59:24 Select(tacExtcodesize!!0:0 Apply(to_skey:bif R5:28) )
		NopCmd
		AssumeExpCmd Gt(R59:24 0x0 )
		AnnotationCmd:25 JSON{"key":{"name":"internal.func.finder.info","type":"analysis.ip.InternalFunctionFinderReport","erasureStrategy":"Erased"},"value":"rO0ABXNyAChhbmFseXNpcy5pcC5JbnRlcm5hbEZ1bmN0aW9uRmluZGVyUmVwb3J0ian+bYn1VdACAAFMABN1bnJlc29sdmVkRnVuY3Rpb25zdAAPTGphdmEvdXRpbC9TZXQ7eHBzcgAhZGF0YXN0cnVjdHVyZXMuTGlua2VkQXJyYXlIYXNoU2V0AAAAAAAAAAEDAAJGAApsb2FkRmFjdG9yTAAJaGFzaFRhYmxldAAuTGRhdGFzdHJ1Y3R1cmVzL2FycmF5aGFzaHRhYmxlL0FycmF5SGFzaFRhYmxlO3hwdwgAAAAAQAAAAHg="}
		AnnotationCmd:25 JSON{"key":{"name":"fps.free-pointer-is-scalarized","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true}
		NopCmd
		AssumeExpCmd LNot(Lt(tacCalldatasize!!52:27 0x4 ) )
		NopCmd
		AssumeExpCmd LNot(Gt(0x70a08231 tacSighash!!7:7 ) )
		NopCmd
		AssumeExpCmd Gt(0xa9059cbb tacSighash!!7:7 )
		NopCmd
		AssumeExpCmd Eq(0x70a08231 tacSighash!!7:7 )
		AssumeCmd:29 true
		AssignExpCmd:30 R65:31 Sub(tacCalldatasize!!52:27 0x4 )
		NopCmd
		AssumeExpCmd LNot(Slt(R65:31 0x20 ) )
		NopCmd
		AssumeExpCmd Le(R56 0xffffffffffffffffffffffffffffffffffffffff )
		AnnotationCmd:25 JSON{"key":{"name":"internal.func.start","type":"analysis.ip.InternalFuncStartAnnotation","erasureStrategy":"CallTrace"},"value":{"id":1,"startPc":3130,"args":[{"s":{"namePrefix":"R56","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1013}]},"offset":1,"sort":"SCALAR"}],"methodSignature":{"#class":"spec.cvlast.QualifiedMethodSignature.QualifiedMethodSig","qualifiedMethodName":{"#class":"spec.cvlast.QualifiedFunction","host":{"name":"ERC20"},"methodId":"balanceOf"},"params":[{"#class":"spec.cvlast.VMParam.Named","name":"account","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$address"}}],"res":[{"#class":"spec.cvlast.VMParam.Unnamed","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256}}]},"stackOffsetToArgPos":{"1":0},"callSiteSrc":{"source":0,"begin":4328,"len":511,"jumpType":"ENTER","address":"ce4604a0000000000000000000000003","sourceContext":{"indexToFilepath":{"0":"contracts/ERC20.sol","1":"contracts/IERC20.sol","2":"contracts/IERC20Metadata.sol"},"sourceDir":".post_autofinders.0"}}}}
		AssignExpCmd:32 R71:33 Apply(hash_3_keccak:bif Apply(skey_basic:bif 0x40) Apply(to_skey:bif R56:34) Apply(skey_basic:bif 0x0))
		AssignExpCmd:37 R72:33 Select(CANON31!!3:2 R71:38 )
		AnnotationCmd:25 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet","value":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R72","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1020}]},"displayPath":{"#class":"analysis.storage.DisplayPath.MapAccess","key":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R56","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1018}]},"keyTyp":{"#class":"tac.TACStorageType.IntegralType","typeLabel":"address","numBytes":"14","descriptor":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$address"},"lowerBound":null,"upperBound":null},"base":{"#class":"analysis.storage.DisplayPath.Root","name":"_balances"}},"storageType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256},"contractInstance":"ce4604a0000000000000000000000003","linkableStorageReadId":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet.None"}}}
		AnnotationCmd:25 JSON{"key":{"name":"internal.func.end","type":"analysis.ip.InternalFuncExitAnnotation","erasureStrategy":"Canonical"},"value":{"id":1,"rets":[{"s":{"namePrefix":"R72","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1023}]},"offset":0}],"functionLayout":{"0":{"#class":"analysis.ip.InternalFuncValueLocation.Scalar"}}}}
		AnnotationCmd:25 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.EVMFunctionReturnWrite","returnbufOffset":"0","returnValueSym":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R72","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1023}]},"callIndex":2}}
		AnnotationCmd:25 JSON{"key":{"name":"tac.return.path","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		LabelCmd:25 "End procedure ERC20-balanceOf(address)"
		NopCmd
		AnnotationCmd:25 JSON{"key":{"name":"call.trace.pop","type":"analysis.icfg.Inliner$CallStack$PopRecord","erasureStrategy":"Canonical"},"value":"rO0ABXNyAClhbmFseXNpcy5pY2ZnLklubGluZXIkQ2FsbFN0YWNrJFBvcFJlY29yZPAPfwSLdCWJAgABSQAIY2FsbGVlSWR4cAAAAAI="}
	}
	Block 0_0_0_3_0_0 Succ [3_0_0_0_0_0] {
		AnnotationCmd:25 JSON{"key":{"name":"call.trace.push","type":"analysis.icfg.Inliner$CallStack$PushRecord","erasureStrategy":"Canonical"},"value":"rO0ABXNyACphbmFseXNpcy5pY2ZnLklubGluZXIkQ2FsbFN0YWNrJFB1c2hSZWNvcmSX8+DCTLCH+AIAA0kACGNhbGxlZUlkTAAGY2FsbGVldAATTHZjL2RhdGEvTWV0aG9kUmVmO0wAB3N1bW1hcnl0ABVMdmMvZGF0YS9DYWxsU3VtbWFyeTt4cAAAAANzcgARdmMuZGF0YS5NZXRob2RSZWbJlJTzzU9pGAIAA0wABGF0dHJ0ABdMc2NlbmUvTWV0aG9kQXR0cmlidXRlO0wACmNvbnRyYWN0SWR0ABZMamF2YS9tYXRoL0JpZ0ludGVnZXI7TAAHc2lnSGFzaHQAEExldm0vU2lnaGFzaEludDt4cHNyABxzY2VuZS5NZXRob2RBdHRyaWJ1dGUkQ29tbW9uNHjdebdr9XMCAAB4cgAVc2NlbmUuTWV0aG9kQXR0cmlidXRlcYg2pYWutuUCAAB4cHNyABRqYXZhLm1hdGguQmlnSW50ZWdlcoz8nx+pO/sdAwAGSQAIYml0Q291bnRJAAliaXRMZW5ndGhJABNmaXJzdE5vbnplcm9CeXRlTnVtSQAMbG93ZXN0U2V0Qml0SQAGc2lnbnVtWwAJbWFnbml0dWRldAACW0J4cgAQamF2YS5sYW5nLk51bWJlcoaslR0LlOCLAgAAeHD///////////////7////+AAAAAXVyAAJbQqzzF/gGCFTgAgAAeHAAAAAQzkYEoAAAAAAAAAAAAAAAA3hzcgAOZXZtLlNpZ2hhc2hJbnRUdcqNMXEgeAIAAUwAAW5xAH4ABnhwc3EAfgAM///////////////+/////gAAAAF1cQB+ABAAAAAEGBYN3Xhw"}
		AssignHavocCmd:25 tacCalldatasize!!75:27
		NopCmd
		AssumeExpCmd Apply(add_noofl:bif 0x4 0x0)
		NopCmd
		AssumeExpCmd Eq(0x4 tacCalldatasize!!75:27 )
		LabelCmd:25 "Start procedure ERC20-totalSupply()"
		AnnotationCmd:25 JSON{"key":{"name":"fps.free-pointer-is-scalarized","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true}
		AssignExpCmd:25 R79:24 Select(tacExtcodesize!!0:0 Apply(to_skey:bif R5:28) )
		NopCmd
		AssumeExpCmd Gt(R79:24 0x0 )
		AnnotationCmd:25 JSON{"key":{"name":"internal.func.finder.info","type":"analysis.ip.InternalFunctionFinderReport","erasureStrategy":"Erased"},"value":"rO0ABXNyAChhbmFseXNpcy5pcC5JbnRlcm5hbEZ1bmN0aW9uRmluZGVyUmVwb3J0ian+bYn1VdACAAFMABN1bnJlc29sdmVkRnVuY3Rpb25zdAAPTGphdmEvdXRpbC9TZXQ7eHBzcgAhZGF0YXN0cnVjdHVyZXMuTGlua2VkQXJyYXlIYXNoU2V0AAAAAAAAAAEDAAJGAApsb2FkRmFjdG9yTAAJaGFzaFRhYmxldAAuTGRhdGFzdHJ1Y3R1cmVzL2FycmF5aGFzaHRhYmxlL0FycmF5SGFzaFRhYmxlO3hwdwgAAAAAQAAAAHg="}
		AnnotationCmd:25 JSON{"key":{"name":"fps.free-pointer-is-scalarized","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true}
		NopCmd
		AssumeExpCmd LNot(Lt(tacCalldatasize!!75:27 0x4 ) )
		NopCmd
		AssumeExpCmd Gt(0x70a08231 tacSighash!!8:7 )
		NopCmd
		AssumeExpCmd Gt(0x2e1a7d4d tacSighash!!8:7 )
		NopCmd
		AssumeExpCmd LNot(Eq(0x6fdde03 tacSighash!!8:7 ) )
		NopCmd
		AssumeExpCmd LNot(Eq(0x95ea7b3 tacSighash!!8:7 ) )
		NopCmd
		AssumeExpCmd Eq(0x18160ddd tacSighash!!8:7 )
		AssumeCmd:39 true
		AnnotationCmd:25 JSON{"key":{"name":"internal.func.start","type":"analysis.ip.InternalFuncStartAnnotation","erasureStrategy":"CallTrace"},"value":{"id":2,"startPc":1328,"args":[],"methodSignature":{"#class":"spec.cvlast.QualifiedMethodSignature.QualifiedMethodSig","qualifiedMethodName":{"#class":"spec.cvlast.QualifiedFunction","host":{"name":"ERC20"},"methodId":"totalSupply"},"params":[],"res":[{"#class":"spec.cvlast.VMParam.Unnamed","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256}}]},"stackOffsetToArgPos":{},"callSiteSrc":{"source":0,"begin":3906,"len":364,"jumpType":"ENTER","address":"ce4604a0000000000000000000000003","sourceContext":{"indexToFilepath":{"0":"contracts/ERC20.sol","1":"contracts/IERC20.sol","2":"contracts/IERC20Metadata.sol"},"sourceDir":".post_autofinders.0"}}}}
		AnnotationCmd:25 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet","value":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"CANON46!!4","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.scalarization.sort","type":"vc.data.ScalarizationSort","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.ScalarizationSort.Split","idx":"2"}},{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.storage.bit-width","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":256},{"key":{"name":"tac.storage.pretty.paths","type":"analysis.storage.DisplayPaths","erasureStrategy":"Erased"},"value":{"paths":[{"#class":"analysis.storage.DisplayPath.Root","name":"_totalSupply"}]}},{"key":{"name":"tac.slot.type","type":"spec.cvlast.typedescriptors.EVMTypeDescriptor$EVMValueType","erasureStrategy":"Canonical"},"value":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256}},{"key":{"name":"tac.storage.non-indexed-path","type":"analysis.storage.StorageAnalysisResult$NonIndexedPath","erasureStrategy":"Canonical"},"value":{"#class":"analysis.storage.StorageAnalysisResult.NonIndexedPath.Root","slot":"2"}},{"key":{"name":"tac.storage","type":"java.math.BigInteger","erasureStrategy":"Canonical"},"value":"ce4604a0000000000000000000000003"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1021}]},"displayPath":{"#class":"analysis.storage.DisplayPath.Root","name":"_totalSupply"},"storageType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256},"contractInstance":"ce4604a0000000000000000000000003","linkableStorageReadId":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet.Id","id":2}}}
		AnnotationCmd:25 JSON{"key":{"name":"internal.func.end","type":"analysis.ip.InternalFuncExitAnnotation","erasureStrategy":"Canonical"},"value":{"id":2,"rets":[{"s":{"namePrefix":"CANON46!!4","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.scalarization.sort","type":"vc.data.ScalarizationSort","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.ScalarizationSort.Split","idx":"2"}},{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.storage.bit-width","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":256},{"key":{"name":"tac.storage.pretty.paths","type":"analysis.storage.DisplayPaths","erasureStrategy":"Erased"},"value":{"paths":[{"#class":"analysis.storage.DisplayPath.Root","name":"_totalSupply"}]}},{"key":{"name":"tac.slot.type","type":"spec.cvlast.typedescriptors.EVMTypeDescriptor$EVMValueType","erasureStrategy":"Canonical"},"value":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256}},{"key":{"name":"tac.storage.non-indexed-path","type":"analysis.storage.StorageAnalysisResult$NonIndexedPath","erasureStrategy":"Canonical"},"value":{"#class":"analysis.storage.StorageAnalysisResult.NonIndexedPath.Root","slot":"2"}},{"key":{"name":"tac.storage","type":"java.math.BigInteger","erasureStrategy":"Canonical"},"value":"ce4604a0000000000000000000000003"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1023}]},"offset":0}],"functionLayout":{"0":{"#class":"analysis.ip.InternalFuncValueLocation.Scalar"}}}}
		AnnotationCmd:25 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.EVMFunctionReturnWrite","returnbufOffset":"0","returnValueSym":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"CANON46!!4","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.scalarization.sort","type":"vc.data.ScalarizationSort","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.ScalarizationSort.Split","idx":"2"}},{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.storage.bit-width","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":256},{"key":{"name":"tac.storage.pretty.paths","type":"analysis.storage.DisplayPaths","erasureStrategy":"Erased"},"value":{"paths":[{"#class":"analysis.storage.DisplayPath.Root","name":"_totalSupply"}]}},{"key":{"name":"tac.slot.type","type":"spec.cvlast.typedescriptors.EVMTypeDescriptor$EVMValueType","erasureStrategy":"Canonical"},"value":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256}},{"key":{"name":"tac.storage.non-indexed-path","type":"analysis.storage.StorageAnalysisResult$NonIndexedPath","erasureStrategy":"Canonical"},"value":{"#class":"analysis.storage.StorageAnalysisResult.NonIndexedPath.Root","slot":"2"}},{"key":{"name":"tac.storage","type":"java.math.BigInteger","erasureStrategy":"Canonical"},"value":"ce4604a0000000000000000000000003"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1023}]},"callIndex":3}}
		AnnotationCmd:25 JSON{"key":{"name":"tac.return.path","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		LabelCmd:25 "End procedure ERC20-totalSupply()"
		NopCmd
		AnnotationCmd:25 JSON{"key":{"name":"call.trace.pop","type":"analysis.icfg.Inliner$CallStack$PopRecord","erasureStrategy":"Canonical"},"value":"rO0ABXNyAClhbmFseXNpcy5pY2ZnLklubGluZXIkQ2FsbFN0YWNrJFBvcFJlY29yZPAPfwSLdCWJAgABSQAIY2FsbGVlSWR4cAAAAAM="}
	}
	Block 0_0_0_5_0_0 Succ [5_0_0_0_0_0] {
		AnnotationCmd:25 JSON{"key":{"name":"call.trace.push","type":"analysis.icfg.Inliner$CallStack$PushRecord","erasureStrategy":"Canonical"},"value":"rO0ABXNyACphbmFseXNpcy5pY2ZnLklubGluZXIkQ2FsbFN0YWNrJFB1c2hSZWNvcmSX8+DCTLCH+AIAA0kACGNhbGxlZUlkTAAGY2FsbGVldAATTHZjL2RhdGEvTWV0aG9kUmVmO0wAB3N1bW1hcnl0ABVMdmMvZGF0YS9DYWxsU3VtbWFyeTt4cAAAAAVzcgARdmMuZGF0YS5NZXRob2RSZWbJlJTzzU9pGAIAA0wABGF0dHJ0ABdMc2NlbmUvTWV0aG9kQXR0cmlidXRlO0wACmNvbnRyYWN0SWR0ABZMamF2YS9tYXRoL0JpZ0ludGVnZXI7TAAHc2lnSGFzaHQAEExldm0vU2lnaGFzaEludDt4cHNyABxzY2VuZS5NZXRob2RBdHRyaWJ1dGUkQ29tbW9uNHjdebdr9XMCAAB4cgAVc2NlbmUuTWV0aG9kQXR0cmlidXRlcYg2pYWutuUCAAB4cHNyABRqYXZhLm1hdGguQmlnSW50ZWdlcoz8nx+pO/sdAwAGSQAIYml0Q291bnRJAAliaXRMZW5ndGhJABNmaXJzdE5vbnplcm9CeXRlTnVtSQAMbG93ZXN0U2V0Qml0SQAGc2lnbnVtWwAJbWFnbml0dWRldAACW0J4cgAQamF2YS5sYW5nLk51bWJlcoaslR0LlOCLAgAAeHD///////////////7////+AAAAAXVyAAJbQqzzF/gGCFTgAgAAeHAAAAAQzkYEoAAAAAAAAAAAAAAAA3hzcgAOZXZtLlNpZ2hhc2hJbnRUdcqNMXEgeAIAAUwAAW5xAH4ABnhwc3EAfgAM///////////////+/////gAAAAF1cQB+ABAAAAAEcKCCMXhw"}
		AssignHavocCmd:25 tacCalldatasize!!90:27
		NopCmd
		AssumeExpCmd Apply(add_noofl:bif 0x4 0x20)
		NopCmd
		AssumeExpCmd Apply(add_noofl:bif 0x4 0x0)
		AssignExpCmd:25 B93 LAnd(Ge(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff I235 ) Le(0x0 I235 ) )
		AssertCmd:25 B93 "sanity bounds check on cvl to vm encoding of certoraArg32753276:int failed"
		AssignExpCmd:25 R94 Apply(safe_math_narrow:bif I235)
		NopCmd
		AssumeExpCmd Eq(0x24 tacCalldatasize!!90:27 )
		LabelCmd:25 "Start procedure ERC20-balanceOf(address)"
		AnnotationCmd:25 JSON{"key":{"name":"fps.free-pointer-is-scalarized","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true}
		AssignExpCmd:25 R97:24 Select(tacExtcodesize!!0:0 Apply(to_skey:bif R5:28) )
		NopCmd
		AssumeExpCmd Gt(R97:24 0x0 )
		AnnotationCmd:25 JSON{"key":{"name":"internal.func.finder.info","type":"analysis.ip.InternalFunctionFinderReport","erasureStrategy":"Erased"},"value":"rO0ABXNyAChhbmFseXNpcy5pcC5JbnRlcm5hbEZ1bmN0aW9uRmluZGVyUmVwb3J0ian+bYn1VdACAAFMABN1bnJlc29sdmVkRnVuY3Rpb25zdAAPTGphdmEvdXRpbC9TZXQ7eHBzcgAhZGF0YXN0cnVjdHVyZXMuTGlua2VkQXJyYXlIYXNoU2V0AAAAAAAAAAEDAAJGAApsb2FkRmFjdG9yTAAJaGFzaFRhYmxldAAuTGRhdGFzdHJ1Y3R1cmVzL2FycmF5aGFzaHRhYmxlL0FycmF5SGFzaFRhYmxlO3hwdwgAAAAAQAAAAHg="}
		AnnotationCmd:25 JSON{"key":{"name":"fps.free-pointer-is-scalarized","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true}
		NopCmd
		AssumeExpCmd LNot(Lt(tacCalldatasize!!90:27 0x4 ) )
		NopCmd
		AssumeExpCmd LNot(Gt(0x70a08231 tacSighash!!10:7 ) )
		NopCmd
		AssumeExpCmd Gt(0xa9059cbb tacSighash!!10:7 )
		NopCmd
		AssumeExpCmd Eq(0x70a08231 tacSighash!!10:7 )
		AssumeCmd:29 true
		AssignExpCmd:30 R103:31 Sub(tacCalldatasize!!90:27 0x4 )
		NopCmd
		AssumeExpCmd LNot(Slt(R103:31 0x20 ) )
		NopCmd
		AssumeExpCmd Le(R94 0xffffffffffffffffffffffffffffffffffffffff )
		AnnotationCmd:25 JSON{"key":{"name":"internal.func.start","type":"analysis.ip.InternalFuncStartAnnotation","erasureStrategy":"CallTrace"},"value":{"id":5,"startPc":3130,"args":[{"s":{"namePrefix":"R94","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1013}]},"offset":1,"sort":"SCALAR"}],"methodSignature":{"#class":"spec.cvlast.QualifiedMethodSignature.QualifiedMethodSig","qualifiedMethodName":{"#class":"spec.cvlast.QualifiedFunction","host":{"name":"ERC20"},"methodId":"balanceOf"},"params":[{"#class":"spec.cvlast.VMParam.Named","name":"account","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$address"}}],"res":[{"#class":"spec.cvlast.VMParam.Unnamed","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256}}]},"stackOffsetToArgPos":{"1":0},"callSiteSrc":{"source":0,"begin":4328,"len":511,"jumpType":"ENTER","address":"ce4604a0000000000000000000000003","sourceContext":{"indexToFilepath":{"0":"contracts/ERC20.sol","1":"contracts/IERC20.sol","2":"contracts/IERC20Metadata.sol"},"sourceDir":".post_autofinders.0"}}}}
		AssignExpCmd:32 R109:33 Apply(hash_3_keccak:bif Apply(skey_basic:bif 0x40) Apply(to_skey:bif R94:34) Apply(skey_basic:bif 0x0))
		AssignExpCmd:40 R110:33 Select(CANON31!!3:2 R109:41 )
		AnnotationCmd:25 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet","value":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R110","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1020}]},"displayPath":{"#class":"analysis.storage.DisplayPath.MapAccess","key":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R94","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1018}]},"keyTyp":{"#class":"tac.TACStorageType.IntegralType","typeLabel":"address","numBytes":"14","descriptor":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$address"},"lowerBound":null,"upperBound":null},"base":{"#class":"analysis.storage.DisplayPath.Root","name":"_balances"}},"storageType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256},"contractInstance":"ce4604a0000000000000000000000003","linkableStorageReadId":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet.None"}}}
		AnnotationCmd:25 JSON{"key":{"name":"internal.func.end","type":"analysis.ip.InternalFuncExitAnnotation","erasureStrategy":"Canonical"},"value":{"id":5,"rets":[{"s":{"namePrefix":"R110","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1023}]},"offset":0}],"functionLayout":{"0":{"#class":"analysis.ip.InternalFuncValueLocation.Scalar"}}}}
		AnnotationCmd:25 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.EVMFunctionReturnWrite","returnbufOffset":"0","returnValueSym":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R110","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1023}]},"callIndex":5}}
		AnnotationCmd:25 JSON{"key":{"name":"tac.return.path","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		LabelCmd:25 "End procedure ERC20-balanceOf(address)"
		NopCmd
		AnnotationCmd:25 JSON{"key":{"name":"call.trace.pop","type":"analysis.icfg.Inliner$CallStack$PopRecord","erasureStrategy":"Canonical"},"value":"rO0ABXNyAClhbmFseXNpcy5pY2ZnLklubGluZXIkQ2FsbFN0YWNrJFBvcFJlY29yZPAPfwSLdCWJAgABSQAIY2FsbGVlSWR4cAAAAAU="}
	}
	Block 0_0_0_6_0_0 Succ [6_0_0_0_0_0] {
		AnnotationCmd:25 JSON{"key":{"name":"call.trace.push","type":"analysis.icfg.Inliner$CallStack$PushRecord","erasureStrategy":"Canonical"},"value":"rO0ABXNyACphbmFseXNpcy5pY2ZnLklubGluZXIkQ2FsbFN0YWNrJFB1c2hSZWNvcmSX8+DCTLCH+AIAA0kACGNhbGxlZUlkTAAGY2FsbGVldAATTHZjL2RhdGEvTWV0aG9kUmVmO0wAB3N1bW1hcnl0ABVMdmMvZGF0YS9DYWxsU3VtbWFyeTt4cAAAAAZzcgARdmMuZGF0YS5NZXRob2RSZWbJlJTzzU9pGAIAA0wABGF0dHJ0ABdMc2NlbmUvTWV0aG9kQXR0cmlidXRlO0wACmNvbnRyYWN0SWR0ABZMamF2YS9tYXRoL0JpZ0ludGVnZXI7TAAHc2lnSGFzaHQAEExldm0vU2lnaGFzaEludDt4cHNyABxzY2VuZS5NZXRob2RBdHRyaWJ1dGUkQ29tbW9uNHjdebdr9XMCAAB4cgAVc2NlbmUuTWV0aG9kQXR0cmlidXRlcYg2pYWutuUCAAB4cHNyABRqYXZhLm1hdGguQmlnSW50ZWdlcoz8nx+pO/sdAwAGSQAIYml0Q291bnRJAAliaXRMZW5ndGhJABNmaXJzdE5vbnplcm9CeXRlTnVtSQAMbG93ZXN0U2V0Qml0SQAGc2lnbnVtWwAJbWFnbml0dWRldAACW0J4cgAQamF2YS5sYW5nLk51bWJlcoaslR0LlOCLAgAAeHD///////////////7////+AAAAAXVyAAJbQqzzF/gGCFTgAgAAeHAAAAAQzkYEoAAAAAAAAAAAAAAAA3hzcgAOZXZtLlNpZ2hhc2hJbnRUdcqNMXEgeAIAAUwAAW5xAH4ABnhwc3EAfgAM///////////////+/////gAAAAF1cQB+ABAAAAAEcKCCMXhw"}
		AssignHavocCmd:25 tacCalldatasize!!113:27
		NopCmd
		AssumeExpCmd Apply(add_noofl:bif 0x4 0x20)
		NopCmd
		AssumeExpCmd Apply(add_noofl:bif 0x4 0x0)
		AssignExpCmd:25 B116 LAnd(Ge(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff I207 ) Le(0x0 I207 ) )
		AssertCmd:25 B116 "sanity bounds check on cvl to vm encoding of certoraArg33223323:int failed"
		AssignExpCmd:25 R117 Apply(safe_math_narrow:bif I207)
		NopCmd
		AssumeExpCmd Eq(0x24 tacCalldatasize!!113:27 )
		LabelCmd:25 "Start procedure ERC20-balanceOf(address)"
		AnnotationCmd:25 JSON{"key":{"name":"fps.free-pointer-is-scalarized","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true}
		AssignExpCmd:25 R120:24 Select(tacExtcodesize!!0:0 Apply(to_skey:bif R5:28) )
		NopCmd
		AssumeExpCmd Gt(R120:24 0x0 )
		AnnotationCmd:25 JSON{"key":{"name":"internal.func.finder.info","type":"analysis.ip.InternalFunctionFinderReport","erasureStrategy":"Erased"},"value":"rO0ABXNyAChhbmFseXNpcy5pcC5JbnRlcm5hbEZ1bmN0aW9uRmluZGVyUmVwb3J0ian+bYn1VdACAAFMABN1bnJlc29sdmVkRnVuY3Rpb25zdAAPTGphdmEvdXRpbC9TZXQ7eHBzcgAhZGF0YXN0cnVjdHVyZXMuTGlua2VkQXJyYXlIYXNoU2V0AAAAAAAAAAEDAAJGAApsb2FkRmFjdG9yTAAJaGFzaFRhYmxldAAuTGRhdGFzdHJ1Y3R1cmVzL2FycmF5aGFzaHRhYmxlL0FycmF5SGFzaFRhYmxlO3hwdwgAAAAAQAAAAHg="}
		AnnotationCmd:25 JSON{"key":{"name":"fps.free-pointer-is-scalarized","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true}
		NopCmd
		AssumeExpCmd LNot(Lt(tacCalldatasize!!113:27 0x4 ) )
		NopCmd
		AssumeExpCmd LNot(Gt(0x70a08231 tacSighash!!11:7 ) )
		NopCmd
		AssumeExpCmd Gt(0xa9059cbb tacSighash!!11:7 )
		NopCmd
		AssumeExpCmd Eq(0x70a08231 tacSighash!!11:7 )
		AssumeCmd:29 true
		AssignExpCmd:30 R126:31 Sub(tacCalldatasize!!113:27 0x4 )
		NopCmd
		AssumeExpCmd LNot(Slt(R126:31 0x20 ) )
		NopCmd
		AssumeExpCmd Le(R117 0xffffffffffffffffffffffffffffffffffffffff )
		AnnotationCmd:25 JSON{"key":{"name":"internal.func.start","type":"analysis.ip.InternalFuncStartAnnotation","erasureStrategy":"CallTrace"},"value":{"id":6,"startPc":3130,"args":[{"s":{"namePrefix":"R117","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1013}]},"offset":1,"sort":"SCALAR"}],"methodSignature":{"#class":"spec.cvlast.QualifiedMethodSignature.QualifiedMethodSig","qualifiedMethodName":{"#class":"spec.cvlast.QualifiedFunction","host":{"name":"ERC20"},"methodId":"balanceOf"},"params":[{"#class":"spec.cvlast.VMParam.Named","name":"account","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$address"}}],"res":[{"#class":"spec.cvlast.VMParam.Unnamed","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256}}]},"stackOffsetToArgPos":{"1":0},"callSiteSrc":{"source":0,"begin":4328,"len":511,"jumpType":"ENTER","address":"ce4604a0000000000000000000000003","sourceContext":{"indexToFilepath":{"0":"contracts/ERC20.sol","1":"contracts/IERC20.sol","2":"contracts/IERC20Metadata.sol"},"sourceDir":".post_autofinders.0"}}}}
		AssignExpCmd:32 R132:33 Apply(hash_3_keccak:bif Apply(skey_basic:bif 0x40) Apply(to_skey:bif R117:34) Apply(skey_basic:bif 0x0))
		AssignExpCmd:42 R133:33 Select(CANON31!!3:2 R132:43 )
		AnnotationCmd:25 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet","value":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R133","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1020}]},"displayPath":{"#class":"analysis.storage.DisplayPath.MapAccess","key":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R117","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1018}]},"keyTyp":{"#class":"tac.TACStorageType.IntegralType","typeLabel":"address","numBytes":"14","descriptor":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$address"},"lowerBound":null,"upperBound":null},"base":{"#class":"analysis.storage.DisplayPath.Root","name":"_balances"}},"storageType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256},"contractInstance":"ce4604a0000000000000000000000003","linkableStorageReadId":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet.None"}}}
		AnnotationCmd:25 JSON{"key":{"name":"internal.func.end","type":"analysis.ip.InternalFuncExitAnnotation","erasureStrategy":"Canonical"},"value":{"id":6,"rets":[{"s":{"namePrefix":"R133","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1023}]},"offset":0}],"functionLayout":{"0":{"#class":"analysis.ip.InternalFuncValueLocation.Scalar"}}}}
		AnnotationCmd:25 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.EVMFunctionReturnWrite","returnbufOffset":"0","returnValueSym":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R133","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1023}]},"callIndex":6}}
		AnnotationCmd:25 JSON{"key":{"name":"tac.return.path","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		LabelCmd:25 "End procedure ERC20-balanceOf(address)"
		NopCmd
		AnnotationCmd:25 JSON{"key":{"name":"call.trace.pop","type":"analysis.icfg.Inliner$CallStack$PopRecord","erasureStrategy":"Canonical"},"value":"rO0ABXNyAClhbmFseXNpcy5pY2ZnLklubGluZXIkQ2FsbFN0YWNrJFBvcFJlY29yZPAPfwSLdCWJAgABSQAIY2FsbGVlSWR4cAAAAAY="}
	}
	Block 0_0_0_7_0_0 Succ [7_0_0_0_0_0] {
		AnnotationCmd:25 JSON{"key":{"name":"call.trace.push","type":"analysis.icfg.Inliner$CallStack$PushRecord","erasureStrategy":"Canonical"},"value":"rO0ABXNyACphbmFseXNpcy5pY2ZnLklubGluZXIkQ2FsbFN0YWNrJFB1c2hSZWNvcmSX8+DCTLCH+AIAA0kACGNhbGxlZUlkTAAGY2FsbGVldAATTHZjL2RhdGEvTWV0aG9kUmVmO0wAB3N1bW1hcnl0ABVMdmMvZGF0YS9DYWxsU3VtbWFyeTt4cAAAAAdzcgARdmMuZGF0YS5NZXRob2RSZWbJlJTzzU9pGAIAA0wABGF0dHJ0ABdMc2NlbmUvTWV0aG9kQXR0cmlidXRlO0wACmNvbnRyYWN0SWR0ABZMamF2YS9tYXRoL0JpZ0ludGVnZXI7TAAHc2lnSGFzaHQAEExldm0vU2lnaGFzaEludDt4cHNyABxzY2VuZS5NZXRob2RBdHRyaWJ1dGUkQ29tbW9uNHjdebdr9XMCAAB4cgAVc2NlbmUuTWV0aG9kQXR0cmlidXRlcYg2pYWutuUCAAB4cHNyABRqYXZhLm1hdGguQmlnSW50ZWdlcoz8nx+pO/sdAwAGSQAIYml0Q291bnRJAAliaXRMZW5ndGhJABNmaXJzdE5vbnplcm9CeXRlTnVtSQAMbG93ZXN0U2V0Qml0SQAGc2lnbnVtWwAJbWFnbml0dWRldAACW0J4cgAQamF2YS5sYW5nLk51bWJlcoaslR0LlOCLAgAAeHD///////////////7////+AAAAAXVyAAJbQqzzF/gGCFTgAgAAeHAAAAAQzkYEoAAAAAAAAAAAAAAAA3hzcgAOZXZtLlNpZ2hhc2hJbnRUdcqNMXEgeAIAAUwAAW5xAH4ABnhwc3EAfgAM///////////////+/////gAAAAF1cQB+ABAAAAAEGBYN3Xhw"}
		AssignHavocCmd:25 tacCalldatasize!!136:27
		NopCmd
		AssumeExpCmd Apply(add_noofl:bif 0x4 0x0)
		NopCmd
		AssumeExpCmd Eq(0x4 tacCalldatasize!!136:27 )
		LabelCmd:25 "Start procedure ERC20-totalSupply()"
		AnnotationCmd:25 JSON{"key":{"name":"fps.free-pointer-is-scalarized","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true}
		AssignExpCmd:25 R140:24 Select(tacExtcodesize!!0:0 Apply(to_skey:bif R5:28) )
		NopCmd
		AssumeExpCmd Gt(R140:24 0x0 )
		AnnotationCmd:25 JSON{"key":{"name":"internal.func.finder.info","type":"analysis.ip.InternalFunctionFinderReport","erasureStrategy":"Erased"},"value":"rO0ABXNyAChhbmFseXNpcy5pcC5JbnRlcm5hbEZ1bmN0aW9uRmluZGVyUmVwb3J0ian+bYn1VdACAAFMABN1bnJlc29sdmVkRnVuY3Rpb25zdAAPTGphdmEvdXRpbC9TZXQ7eHBzcgAhZGF0YXN0cnVjdHVyZXMuTGlua2VkQXJyYXlIYXNoU2V0AAAAAAAAAAEDAAJGAApsb2FkRmFjdG9yTAAJaGFzaFRhYmxldAAuTGRhdGFzdHJ1Y3R1cmVzL2FycmF5aGFzaHRhYmxlL0FycmF5SGFzaFRhYmxlO3hwdwgAAAAAQAAAAHg="}
		AnnotationCmd:25 JSON{"key":{"name":"fps.free-pointer-is-scalarized","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true}
		NopCmd
		AssumeExpCmd LNot(Lt(tacCalldatasize!!136:27 0x4 ) )
		NopCmd
		AssumeExpCmd Gt(0x70a08231 tacSighash!!12:7 )
		NopCmd
		AssumeExpCmd Gt(0x2e1a7d4d tacSighash!!12:7 )
		NopCmd
		AssumeExpCmd LNot(Eq(0x6fdde03 tacSighash!!12:7 ) )
		NopCmd
		AssumeExpCmd LNot(Eq(0x95ea7b3 tacSighash!!12:7 ) )
		NopCmd
		AssumeExpCmd Eq(0x18160ddd tacSighash!!12:7 )
		AssumeCmd:39 true
		AnnotationCmd:25 JSON{"key":{"name":"internal.func.start","type":"analysis.ip.InternalFuncStartAnnotation","erasureStrategy":"CallTrace"},"value":{"id":7,"startPc":1328,"args":[],"methodSignature":{"#class":"spec.cvlast.QualifiedMethodSignature.QualifiedMethodSig","qualifiedMethodName":{"#class":"spec.cvlast.QualifiedFunction","host":{"name":"ERC20"},"methodId":"totalSupply"},"params":[],"res":[{"#class":"spec.cvlast.VMParam.Unnamed","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256}}]},"stackOffsetToArgPos":{},"callSiteSrc":{"source":0,"begin":3906,"len":364,"jumpType":"ENTER","address":"ce4604a0000000000000000000000003","sourceContext":{"indexToFilepath":{"0":"contracts/ERC20.sol","1":"contracts/IERC20.sol","2":"contracts/IERC20Metadata.sol"},"sourceDir":".post_autofinders.0"}}}}
		AnnotationCmd:25 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet","value":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"CANON46!!4","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.scalarization.sort","type":"vc.data.ScalarizationSort","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.ScalarizationSort.Split","idx":"2"}},{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.storage.bit-width","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":256},{"key":{"name":"tac.storage.pretty.paths","type":"analysis.storage.DisplayPaths","erasureStrategy":"Erased"},"value":{"paths":[{"#class":"analysis.storage.DisplayPath.Root","name":"_totalSupply"}]}},{"key":{"name":"tac.slot.type","type":"spec.cvlast.typedescriptors.EVMTypeDescriptor$EVMValueType","erasureStrategy":"Canonical"},"value":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256}},{"key":{"name":"tac.storage.non-indexed-path","type":"analysis.storage.StorageAnalysisResult$NonIndexedPath","erasureStrategy":"Canonical"},"value":{"#class":"analysis.storage.StorageAnalysisResult.NonIndexedPath.Root","slot":"2"}},{"key":{"name":"tac.storage","type":"java.math.BigInteger","erasureStrategy":"Canonical"},"value":"ce4604a0000000000000000000000003"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1021}]},"displayPath":{"#class":"analysis.storage.DisplayPath.Root","name":"_totalSupply"},"storageType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256},"contractInstance":"ce4604a0000000000000000000000003","linkableStorageReadId":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet.Id","id":5}}}
		AnnotationCmd:25 JSON{"key":{"name":"internal.func.end","type":"analysis.ip.InternalFuncExitAnnotation","erasureStrategy":"Canonical"},"value":{"id":7,"rets":[{"s":{"namePrefix":"CANON46!!4","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.scalarization.sort","type":"vc.data.ScalarizationSort","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.ScalarizationSort.Split","idx":"2"}},{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.storage.bit-width","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":256},{"key":{"name":"tac.storage.pretty.paths","type":"analysis.storage.DisplayPaths","erasureStrategy":"Erased"},"value":{"paths":[{"#class":"analysis.storage.DisplayPath.Root","name":"_totalSupply"}]}},{"key":{"name":"tac.slot.type","type":"spec.cvlast.typedescriptors.EVMTypeDescriptor$EVMValueType","erasureStrategy":"Canonical"},"value":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256}},{"key":{"name":"tac.storage.non-indexed-path","type":"analysis.storage.StorageAnalysisResult$NonIndexedPath","erasureStrategy":"Canonical"},"value":{"#class":"analysis.storage.StorageAnalysisResult.NonIndexedPath.Root","slot":"2"}},{"key":{"name":"tac.storage","type":"java.math.BigInteger","erasureStrategy":"Canonical"},"value":"ce4604a0000000000000000000000003"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1023}]},"offset":0}],"functionLayout":{"0":{"#class":"analysis.ip.InternalFuncValueLocation.Scalar"}}}}
		AnnotationCmd:25 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.EVMFunctionReturnWrite","returnbufOffset":"0","returnValueSym":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"CANON46!!4","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.scalarization.sort","type":"vc.data.ScalarizationSort","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.ScalarizationSort.Split","idx":"2"}},{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.storage.bit-width","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":256},{"key":{"name":"tac.storage.pretty.paths","type":"analysis.storage.DisplayPaths","erasureStrategy":"Erased"},"value":{"paths":[{"#class":"analysis.storage.DisplayPath.Root","name":"_totalSupply"}]}},{"key":{"name":"tac.slot.type","type":"spec.cvlast.typedescriptors.EVMTypeDescriptor$EVMValueType","erasureStrategy":"Canonical"},"value":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256}},{"key":{"name":"tac.storage.non-indexed-path","type":"analysis.storage.StorageAnalysisResult$NonIndexedPath","erasureStrategy":"Canonical"},"value":{"#class":"analysis.storage.StorageAnalysisResult.NonIndexedPath.Root","slot":"2"}},{"key":{"name":"tac.storage","type":"java.math.BigInteger","erasureStrategy":"Canonical"},"value":"ce4604a0000000000000000000000003"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1023}]},"callIndex":7}}
		AnnotationCmd:25 JSON{"key":{"name":"tac.return.path","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		LabelCmd:25 "End procedure ERC20-totalSupply()"
		NopCmd
		AnnotationCmd:25 JSON{"key":{"name":"call.trace.pop","type":"analysis.icfg.Inliner$CallStack$PopRecord","erasureStrategy":"Canonical"},"value":"rO0ABXNyAClhbmFseXNpcy5pY2ZnLklubGluZXIkQ2FsbFN0YWNrJFBvcFJlY29yZPAPfwSLdCWJAgABSQAIY2FsbGVlSWR4cAAAAAc="}
	}
	Block 1_0_0_0_0_0 Succ [0_0_0_2_0_0] {
		AssumeNotCmd:25 false
		AssumeNotCmd:25 false
		AnnotationCmd JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageGlobalChangeSnippet.StorageTakeSnapshot","lhs":{"namePrefix":"lastStorage","tag":{"#class":"tac.Tag.BlockchainState"},"callIndex":0,"meta":[{"key":{"name":"cvl.local","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true},{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"lastStorage"},{"key":{"name":"cvl.type","type":"spec.cvlast.CVLType$PureCVLType","erasureStrategy":"CallTrace"},"value":{"#class":"spec.cvlast.CVLType.PureCVLType.VMInternal.BlockchainState"}},{"key":{"name":"cvl","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true},{"key":{"name":"cvl.display","type":"java.lang.String","erasureStrategy":"CallTrace"},"value":"lastStorage"}]}}}
		AssignExpCmd:44 I151 CANON8:15
	}
	Block 2_0_0_0_0_0 Succ [0_0_0_3_0_0] {
		AssumeNotCmd:25 false
		AssumeNotCmd:25 false
		AnnotationCmd JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageGlobalChangeSnippet.StorageTakeSnapshot","lhs":{"namePrefix":"lastStorage","tag":{"#class":"tac.Tag.BlockchainState"},"callIndex":0,"meta":[{"key":{"name":"cvl.local","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true},{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"lastStorage"},{"key":{"name":"cvl.type","type":"spec.cvlast.CVLType$PureCVLType","erasureStrategy":"CallTrace"},"value":{"#class":"spec.cvlast.CVLType.PureCVLType.VMInternal.BlockchainState"}},{"key":{"name":"cvl","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true},{"key":{"name":"cvl.display","type":"java.lang.String","erasureStrategy":"CallTrace"},"value":"lastStorage"}]}}}
		AssignExpCmd:45 I152 IntAdd(R49:33 R72:33)
	}
	Block 3_0_0_0_0_0 Succ [0_0_0_4_0_0] {
		AssumeNotCmd:25 false
		AssumeNotCmd:25 false
		AnnotationCmd JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageGlobalChangeSnippet.StorageTakeSnapshot","lhs":{"namePrefix":"lastStorage","tag":{"#class":"tac.Tag.BlockchainState"},"callIndex":0,"meta":[{"key":{"name":"cvl.local","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true},{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"lastStorage"},{"key":{"name":"cvl.type","type":"spec.cvlast.CVLType$PureCVLType","erasureStrategy":"CallTrace"},"value":{"#class":"spec.cvlast.CVLType.PureCVLType.VMInternal.BlockchainState"}},{"key":{"name":"cvl","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true},{"key":{"name":"cvl.display","type":"java.lang.String","erasureStrategy":"CallTrace"},"value":"lastStorage"}]}}}
		AssignExpCmd:46 B154 Le(I152 CANON46!!4:47 )
		AssumeCmd:25 B154
		AnnotationCmd:25 JSON{"key":{"name":"cvl.label.end","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		AnnotationCmd:25 JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Message","s":"check effects of step taken by one of the functions"}}
		NopCmd
		NopCmd
		NopCmd
		NopCmd
		NopCmd
		NopCmd
		NopCmd
		AnnotationCmd:25 JSON{"key":{"name":"call.trace.push","type":"analysis.icfg.Inliner$CallStack$PushRecord","erasureStrategy":"Canonical"},"value":"rO0ABXNyACphbmFseXNpcy5pY2ZnLklubGluZXIkQ2FsbFN0YWNrJFB1c2hSZWNvcmSX8+DCTLCH+AIAA0kACGNhbGxlZUlkTAAGY2FsbGVldAATTHZjL2RhdGEvTWV0aG9kUmVmO0wAB3N1bW1hcnl0ABVMdmMvZGF0YS9DYWxsU3VtbWFyeTt4cAAAAARzcgARdmMuZGF0YS5NZXRob2RSZWbJlJTzzU9pGAIAA0wABGF0dHJ0ABdMc2NlbmUvTWV0aG9kQXR0cmlidXRlO0wACmNvbnRyYWN0SWR0ABZMamF2YS9tYXRoL0JpZ0ludGVnZXI7TAAHc2lnSGFzaHQAEExldm0vU2lnaGFzaEludDt4cHNyABxzY2VuZS5NZXRob2RBdHRyaWJ1dGUkQ29tbW9uNHjdebdr9XMCAAB4cgAVc2NlbmUuTWV0aG9kQXR0cmlidXRlcYg2pYWutuUCAAB4cHNyABRqYXZhLm1hdGguQmlnSW50ZWdlcoz8nx+pO/sdAwAGSQAIYml0Q291bnRJAAliaXRMZW5ndGhJABNmaXJzdE5vbnplcm9CeXRlTnVtSQAMbG93ZXN0U2V0Qml0SQAGc2lnbnVtWwAJbWFnbml0dWRldAACW0J4cgAQamF2YS5sYW5nLk51bWJlcoaslR0LlOCLAgAAeHD///////////////7////+AAAAAXVyAAJbQqzzF/gGCFTgAgAAeHAAAAAQzkYEoAAAAAAAAAAAAAAAA3hzcgAOZXZtLlNpZ2hhc2hJbnRUdcqNMXEgeAIAAUwAAW5xAH4ABnhwc3EAfgAM///////////////+/////gAAAAF1cQB+ABAAAAAECV6ns3hw"}
		NopCmd
		AssumeExpCmd Ge(CANON58:5 0x44 )
		NopCmd
		AssumeExpCmd Ge(0x7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff CANON58:5 )
		AssignExpCmd R165:24 Select(CANON56:4 0x4 )
		AssignExpCmd tacCalldatabufCANON0@4:48 R165:24
		AssignExpCmd R166:24 Select(CANON56:4 0x24 )
		AssignExpCmd tacCalldatabufCANON1@4:49 R166:24
		AssignExpCmd:25 B168 LAnd(Ge(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff CANON9:16 ) Le(0x0 CANON9:16 ) )
		AssertCmd:25 B168 "sanity bounds check on cvl to vm encoding of tacTmp!3089:int failed"
		AssignExpCmd:25 R169:24 Apply(safe_math_narrow:bif CANON9:16)
		NopCmd
		AssumeExpCmd LAnd(Le(R169:50 0xffffffffffffffffffffffffffffffffffffffff ) Ge(R169:50 0x0 ) )
		AssignExpCmd:25 B173 LAnd(Ge(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff CANON10:17 ) Le(0x0 CANON10:17 ) )
		AssertCmd:25 B173 "sanity bounds check on cvl to vm encoding of tacTmp!3092:int failed"
		AssignExpCmd:25 R174:24 Apply(safe_math_narrow:bif CANON10:17)
		NopCmd
		AssumeExpCmd LAnd(Le(R174:51 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff ) Ge(R174:51 0x0 ) )
		AssignExpCmd:25 B179 LAnd(Ge(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff CANON11:18 ) Le(0x0 CANON11:18 ) )
		AssertCmd:25 B179 "sanity bounds check on cvl to vm encoding of tacTmp!3096:int failed"
		AssignExpCmd:25 R180:24 Apply(safe_math_narrow:bif CANON11:18)
		NopCmd
		AssumeExpCmd LAnd(Le(R180:52 0xffffffffffffffffffffffffffffffffffffffff ) Ge(R180:52 0x0 ) )
		AssignExpCmd:25 B184 LAnd(Ge(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff CANON15:22 ) Le(0x0 CANON15:22 ) )
		AssertCmd:25 B184 "sanity bounds check on cvl to vm encoding of tacTmp!3101:int failed"
		AssignExpCmd:25 R185:24 Apply(safe_math_narrow:bif CANON15:22)
		NopCmd
		AssumeExpCmd LAnd(Le(R185:53 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff ) Ge(R185:53 0x0 ) )
		AssignExpCmd:25 B189 LAnd(Ge(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff CANON16:23 ) Le(0x0 CANON16:23 ) )
		AssertCmd:25 B189 "sanity bounds check on cvl to vm encoding of tacTmp!3104:int failed"
		AssignExpCmd:25 R190:24 Apply(safe_math_narrow:bif CANON16:23)
		NopCmd
		AssumeExpCmd LAnd(Le(R190:54 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff ) Ge(R190:54 0x0 ) )
		AssignExpCmd:25 B194 LAnd(Ge(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff CANON10:17 ) Le(0x0 CANON10:17 ) )
		AssertCmd:25 B194 "sanity bounds check on cvl to vm encoding of tacTmp!3120:int failed"
		AssignExpCmd:25 R195:24 Apply(safe_math_narrow:bif CANON10:17)
		AssignExpCmd:25 B197 LAnd(Ge(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff CANON9:16 ) Le(0x0 CANON9:16 ) )
		AssertCmd:25 B197 "sanity bounds check on cvl to vm encoding of tacTmp!3123:int failed"
		AssignExpCmd:25 R198:24 Apply(safe_math_narrow:bif CANON9:16)
		AssignExpCmd:25 R201:24 Select(tacBalance!!2:1 Apply(to_skey:bif R198:24) )
		AssignExpCmd:55 I202:24 IntSub(R201:24 R195:24 )
		AssignExpCmd:55 tacBalance!!203:1 Store(tacBalance!!2:1 Apply(to_skey:bif R198:24) I202:24 )
		AssignExpCmd:25 R204:24 Select(tacBalance!!203:1 Apply(to_skey:bif R5:6) )
		AssignExpCmd:55 R205:24 Add(R204:24 R195:24)
		NopCmd
		AssumeExpCmd Apply(add_noofl:bif R204:24 R195:24)
		AnnotationCmd:25 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.BalanceSnippet","srcAccountInfo":{"old":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R201","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}]},"new":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"I202","tag":{"#class":"tac.Tag.Int"},"callIndex":0,"meta":[{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}]},"addr":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R198","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}]}},"trgAccountInfo":{"old":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R204","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}]},"new":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R205","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}]},"addr":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R5","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"tacContractAt"},{"key":{"name":"tac.contract.sym.addr.name","type":"java.lang.String","erasureStrategy":"Erased"},"value":"ERC20"},{"key":{"name":"tac.contract.sym.addr","type":"java.math.BigInteger","erasureStrategy":"Erased"},"value":"ce4604a0000000000000000000000003"}]}},"transferredAmount":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R195","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}]}}}
		JumpCmd 0_0_0_4_0_0
	}
	Block 5_0_0_0_0_0 Succ [0_0_0_6_0_0] {
		AssumeNotCmd:25 false
		AssumeNotCmd:25 false
		AnnotationCmd JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageGlobalChangeSnippet.StorageTakeSnapshot","lhs":{"namePrefix":"lastStorage","tag":{"#class":"tac.Tag.BlockchainState"},"callIndex":0,"meta":[{"key":{"name":"cvl.local","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true},{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"lastStorage"},{"key":{"name":"cvl.type","type":"spec.cvlast.CVLType$PureCVLType","erasureStrategy":"CallTrace"},"value":{"#class":"spec.cvlast.CVLType.PureCVLType.VMInternal.BlockchainState"}},{"key":{"name":"cvl","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true},{"key":{"name":"cvl.display","type":"java.lang.String","erasureStrategy":"CallTrace"},"value":"lastStorage"}]}}}
		AssignExpCmd:44 I207 CANON8:15
	}
	Block 6_0_0_0_0_0 Succ [0_0_0_7_0_0] {
		AssumeNotCmd:25 false
		AssumeNotCmd:25 false
		AnnotationCmd JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageGlobalChangeSnippet.StorageTakeSnapshot","lhs":{"namePrefix":"lastStorage","tag":{"#class":"tac.Tag.BlockchainState"},"callIndex":0,"meta":[{"key":{"name":"cvl.local","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true},{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"lastStorage"},{"key":{"name":"cvl.type","type":"spec.cvlast.CVLType$PureCVLType","erasureStrategy":"CallTrace"},"value":{"#class":"spec.cvlast.CVLType.PureCVLType.VMInternal.BlockchainState"}},{"key":{"name":"cvl","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true},{"key":{"name":"cvl.display","type":"java.lang.String","erasureStrategy":"CallTrace"},"value":"lastStorage"}]}}}
		AssignExpCmd:56 I208 IntAdd(R110:33 R133:33)
	}
	Block 7_0_0_0_0_0 Succ [] {
		AssumeNotCmd:25 false
		AssumeNotCmd:25 false
		AnnotationCmd JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageGlobalChangeSnippet.StorageTakeSnapshot","lhs":{"namePrefix":"lastStorage","tag":{"#class":"tac.Tag.BlockchainState"},"callIndex":0,"meta":[{"key":{"name":"cvl.local","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true},{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"lastStorage"},{"key":{"name":"cvl.type","type":"spec.cvlast.CVLType$PureCVLType","erasureStrategy":"CallTrace"},"value":{"#class":"spec.cvlast.CVLType.PureCVLType.VMInternal.BlockchainState"}},{"key":{"name":"cvl","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true},{"key":{"name":"cvl.display","type":"java.lang.String","erasureStrategy":"CallTrace"},"value":"lastStorage"}]}}}
		AssignExpCmd:57 B210 Le(I208 CANON46!!4:47 )
		AssertCmd:58 B210 "invariant violated in post-state"
		AnnotationCmd:25 JSON{"key":{"name":"cvl.label.end","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
	}
	Block 0_0_0_4_0_0 Succ [4_0_0_0_0_0] {
		LabelCmd "Start procedure ERC20-approve(address,uint256)"
		AnnotationCmd JSON{"key":{"name":"fps.free-pointer-is-scalarized","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true}
		AssignExpCmd R211:24 Select(tacExtcodesize!!0:0 Apply(to_skey:bif R5:28) )
		NopCmd
		AssumeExpCmd Gt(R211:24 0x0 )
		AnnotationCmd JSON{"key":{"name":"internal.func.finder.info","type":"analysis.ip.InternalFunctionFinderReport","erasureStrategy":"Erased"},"value":"rO0ABXNyAChhbmFseXNpcy5pcC5JbnRlcm5hbEZ1bmN0aW9uRmluZGVyUmVwb3J0ian+bYn1VdACAAFMABN1bnJlc29sdmVkRnVuY3Rpb25zdAAPTGphdmEvdXRpbC9TZXQ7eHBzcgAhZGF0YXN0cnVjdHVyZXMuTGlua2VkQXJyYXlIYXNoU2V0AAAAAAAAAAEDAAJGAApsb2FkRmFjdG9yTAAJaGFzaFRhYmxldAAuTGRhdGFzdHJ1Y3R1cmVzL2FycmF5aGFzaHRhYmxlL0FycmF5SGFzaFRhYmxlO3hwdwgAAAAAQAAAAHg="}
		AnnotationCmd JSON{"key":{"name":"fps.free-pointer-is-scalarized","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true}
		NopCmd
		AssumeExpCmd LNot(Lt(CANON58:5 0x4 ) )
		NopCmd
		AssumeExpCmd Gt(0x70a08231 tacSighash!!9:7 )
		NopCmd
		AssumeExpCmd Gt(0x2e1a7d4d tacSighash!!9:7 )
		NopCmd
		AssumeExpCmd LNot(Eq(0x6fdde03 tacSighash!!9:7 ) )
		NopCmd
		AssumeExpCmd Eq(0x95ea7b3 tacSighash!!9:7 )
		NopCmd
		AssumeExpCmd Eq(R174:51 0x0 )
		AssignExpCmd:59 R219:60 Sub(CANON58:5 0x4 )
		NopCmd
		AssumeExpCmd LNot(Slt(R219:60 0x40 ) )
		AssignExpCmd:61 R221:62 tacCalldatabufCANON0@4:63
		NopCmd
		AssumeExpCmd Le(R165:24 0xffffffffffffffffffffffffffffffffffffffff )
		AssignExpCmd:64 R223:62 tacCalldatabufCANON1@4:65
		AnnotationCmd JSON{"key":{"name":"internal.func.start","type":"analysis.ip.InternalFuncStartAnnotation","erasureStrategy":"CallTrace"},"value":{"id":3,"startPc":1158,"args":[{"s":{"namePrefix":"R221","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1012}]},"offset":1,"sort":"SCALAR"},{"s":{"namePrefix":"R223","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1012}]},"offset":2,"sort":"SCALAR"}],"methodSignature":{"#class":"spec.cvlast.QualifiedMethodSignature.QualifiedMethodSig","qualifiedMethodName":{"#class":"spec.cvlast.QualifiedFunction","host":{"name":"ERC20"},"methodId":"approve"},"params":[{"#class":"spec.cvlast.VMParam.Named","name":"spender","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$address"}},{"#class":"spec.cvlast.VMParam.Named","name":"amount","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256}}],"res":[{"#class":"spec.cvlast.VMParam.Unnamed","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$bool"}}]},"stackOffsetToArgPos":{"1":0,"2":1},"callSiteSrc":{"source":0,"begin":6320,"len":541,"jumpType":"ENTER","address":"ce4604a0000000000000000000000003","sourceContext":{"indexToFilepath":{"0":"contracts/ERC20.sol","1":"contracts/IERC20.sol","2":"contracts/IERC20Metadata.sol"},"sourceDir":".post_autofinders.0"}}}}
		AnnotationCmd JSON{"key":{"name":"internal.func.start","type":"analysis.ip.InternalFuncStartAnnotation","erasureStrategy":"CallTrace"},"value":{"id":4,"startPc":5140,"args":[{"s":{"namePrefix":"R169","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.env.known-bit-width","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":160},{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1018}]},"offset":1,"sort":"SCALAR"},{"s":{"namePrefix":"R221","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1012}]},"offset":2,"sort":"SCALAR"},{"s":{"namePrefix":"R223","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1012}]},"offset":3,"sort":"SCALAR"}],"methodSignature":{"#class":"spec.cvlast.QualifiedMethodSignature.QualifiedMethodSig","qualifiedMethodName":{"#class":"spec.cvlast.QualifiedFunction","host":{"name":"ERC20"},"methodId":"_approve"},"params":[{"#class":"spec.cvlast.VMParam.Named","name":"owner","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$address"}},{"#class":"spec.cvlast.VMParam.Named","name":"spender","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$address"}},{"#class":"spec.cvlast.VMParam.Named","name":"amount","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256}}],"res":[]},"stackOffsetToArgPos":{"1":0,"2":1,"3":2},"callSiteSrc":{"source":0,"begin":6796,"len":37,"jumpType":"ENTER","address":"ce4604a0000000000000000000000003","sourceContext":{"indexToFilepath":{"0":"contracts/ERC20.sol","1":"contracts/IERC20.sol","2":"contracts/IERC20Metadata.sol"},"sourceDir":".post_autofinders.0"}}}}
		NopCmd
		AssumeExpCmd LNot(Eq(R169:50 0x0 ) )
		NopCmd
		NopCmd
		AssumeExpCmd LNot(Eq(R165:24 0x0 ) )
		AssignExpCmd R231:62 tacCalldatabufCANON0@4:63
		AnnotationCmd JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.StoreSnippet","value":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R223","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1012}]},"displayPath":{"#class":"analysis.storage.DisplayPath.MapAccess","key":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R231","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1012}]},"keyTyp":{"#class":"tac.TACStorageType.IntegralType","typeLabel":"address","numBytes":"14","descriptor":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$address"},"lowerBound":null,"upperBound":null},"base":{"#class":"analysis.storage.DisplayPath.MapAccess","key":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R169","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.env.known-bit-width","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":160},{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1012}]},"keyTyp":{"#class":"tac.TACStorageType.IntegralType","typeLabel":"address","numBytes":"14","descriptor":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$address"},"lowerBound":null,"upperBound":null},"base":{"#class":"analysis.storage.DisplayPath.Root","name":"_allowances"}}},"storageType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256},"contractInstance":"ce4604a0000000000000000000000003"}}
		AnnotationCmd JSON{"key":{"name":"internal.func.end","type":"analysis.ip.InternalFuncExitAnnotation","erasureStrategy":"Canonical"},"value":{"id":4,"rets":[],"functionLayout":{}}}
		AssignExpCmd R234:66 0x1
		AnnotationCmd JSON{"key":{"name":"internal.func.end","type":"analysis.ip.InternalFuncExitAnnotation","erasureStrategy":"Canonical"},"value":{"id":3,"rets":[{"s":{"namePrefix":"R234","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1023}]},"offset":0}],"functionLayout":{"0":{"#class":"analysis.ip.InternalFuncValueLocation.Scalar"}}}}
		AnnotationCmd JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.EVMFunctionReturnWrite","returnbufOffset":"0","returnValueSym":{"#class":"vc.data.TACSymbol.Const","value":"1","tag":{"#class":"tac.Tag.Bool"}},"callIndex":4}}
		AnnotationCmd JSON{"key":{"name":"tac.return.path","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		LabelCmd "End procedure ERC20-approve(address,uint256)"
		JumpCmd 4_0_0_0_0_0
	}
	Block 4_0_0_0_0_0 Succ [0_0_0_5_0_0] {
		AnnotationCmd:25 JSON{"key":{"name":"call.trace.pop","type":"analysis.icfg.Inliner$CallStack$PopRecord","erasureStrategy":"Canonical"},"value":"rO0ABXNyAClhbmFseXNpcy5pY2ZnLklubGluZXIkQ2FsbFN0YWNrJFBvcFJlY29yZPAPfwSLdCWJAgABSQAIY2FsbGVlSWR4cAAAAAQ="}
		AssumeNotCmd:25 false
		AssumeNotCmd:25 false
		AnnotationCmd JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageGlobalChangeSnippet.StorageTakeSnapshot","lhs":{"namePrefix":"lastStorage","tag":{"#class":"tac.Tag.BlockchainState"},"callIndex":0,"meta":[{"key":{"name":"cvl.local","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true},{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"lastStorage"},{"key":{"name":"cvl.type","type":"spec.cvlast.CVLType$PureCVLType","erasureStrategy":"CallTrace"},"value":{"#class":"spec.cvlast.CVLType.PureCVLType.VMInternal.BlockchainState"}},{"key":{"name":"cvl","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true},{"key":{"name":"cvl.display","type":"java.lang.String","erasureStrategy":"CallTrace"},"value":"lastStorage"}]}}}
		AnnotationCmd:25 JSON{"key":{"name":"cvl.label.end","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		AnnotationCmd:25 JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Message","s":"assert invariant in post-state"}}
		AssignExpCmd:26 I235 CANON6:14
	}
}
Axioms {
		CANON119
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
  "3": [
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
  "6": [
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
  "7": [
    {
      "key": {
        "name": "Tac.symbol.keyword",
        "type": "java.lang.String",
        "erasureStrategy": "Canonical"
      },
      "value": "tacSighash"
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
      "value": "alice"
    }
  ],
  "15": [
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
      "value": "bob"
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
  "23": [
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
          "line": 114
        },
        "end": {
          "line": 126,
          "character": 1
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
          "id": "alice",
          "tag": {
            "scope": {
              "scopeStack": [
                {
                  "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                },
                {
                  "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                  "scopeId": 12
                }
              ],
              "innerScope": {
                "scopeStack": [
                  {
                    "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                  }
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
                "line": 114
              },
              "end": {
                "line": 126,
                "character": 1
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
          "line": 114
        },
        "end": {
          "line": 126,
          "character": 1
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
          "line": 114
        },
        "end": {
          "line": 126,
          "character": 1
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
          "line": 114
        },
        "end": {
          "line": 126,
          "character": 1
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
      "value": 1017
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
          "line": 114
        },
        "end": {
          "line": 126,
          "character": 1
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
      "value": 1020
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
          "line": 114
        },
        "end": {
          "line": 126,
          "character": 1
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
  "36": [
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
              "namePrefix": "R33",
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
                "namePrefix": "R33",
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
                "namePrefix": "CANON33",
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
          "line": 114
        },
        "end": {
          "line": 126,
          "character": 1
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
                    "value": 1018
                  }
                ]
              },
              "baseSlot": {
                "#class": "vc.data.TACSymbol.Var.Full",
                "namePrefix": "CANON33",
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
                "namePrefix": "CANON32",
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
          "line": 114
        },
        "end": {
          "line": 126,
          "character": 1
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
          "line": 114
        },
        "end": {
          "line": 126,
          "character": 1
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
      "value": "rO0ABXNyADJhbmFseXNpcy5pY2ZnLkNhbGxHcmFwaEJ1aWxkZXIkQ29udHJhY3RTdG9yYWdlUmVhZLRpTKYiS4EFAgABSQACaWR4cAAAAAM="
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
  "41": [
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
              "namePrefix": "R94",
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
                "namePrefix": "R94",
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
                "namePrefix": "CANON33",
                "tag": {
                  "#class": "tac.Tag.Bit256"
                },
                "callIndex": 5,
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
                "namePrefix": "CANON32",
                "tag": {
                  "#class": "tac.Tag.Bit256"
                },
                "callIndex": 5,
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
          "line": 114
        },
        "end": {
          "line": 126,
          "character": 1
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
      "value": "rO0ABXNyADJhbmFseXNpcy5pY2ZnLkNhbGxHcmFwaEJ1aWxkZXIkQ29udHJhY3RTdG9yYWdlUmVhZLRpTKYiS4EFAgABSQACaWR4cAAAAAQ="
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
  "43": [
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
                "namePrefix": "CANON33",
                "tag": {
                  "#class": "tac.Tag.Bit256"
                },
                "callIndex": 6,
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
                "namePrefix": "CANON32",
                "tag": {
                  "#class": "tac.Tag.Bit256"
                },
                "callIndex": 6,
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
          "id": "bob",
          "tag": {
            "scope": {
              "scopeStack": [
                {
                  "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                },
                {
                  "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                  "scopeId": 12
                }
              ],
              "innerScope": {
                "scopeStack": [
                  {
                    "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                  }
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
                "line": 114
              },
              "end": {
                "line": 126,
                "character": 1
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
          "line": 114
        },
        "end": {
          "line": 126,
          "character": 1
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
                "id": "alice",
                "tag": {
                  "scope": {
                    "scopeStack": [
                      {
                        "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                      },
                      {
                        "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                        "scopeId": 12
                      }
                    ],
                    "innerScope": {
                      "scopeStack": [
                        {
                          "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                        }
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
                      "line": 114
                    },
                    "end": {
                      "line": 126,
                      "character": 1
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
                      "scopeId": 12
                    }
                  ],
                  "innerScope": {
                    "scopeStack": [
                      {
                        "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                      }
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
                    "line": 114
                  },
                  "end": {
                    "line": 126,
                    "character": 1
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
                    "scopeId": 12
                  }
                ],
                "innerScope": {
                  "scopeStack": [
                    {
                      "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                    }
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
                  "line": 115,
                  "character": 4
                },
                "end": {
                  "line": 115,
                  "character": 13
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
                "id": "bob",
                "tag": {
                  "scope": {
                    "scopeStack": [
                      {
                        "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                      },
                      {
                        "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                        "scopeId": 12
                      }
                    ],
                    "innerScope": {
                      "scopeStack": [
                        {
                          "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                        }
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
                      "line": 114
                    },
                    "end": {
                      "line": 126,
                      "character": 1
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
                      "scopeId": 12
                    }
                  ],
                  "innerScope": {
                    "scopeStack": [
                      {
                        "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                      }
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
                    "line": 114
                  },
                  "end": {
                    "line": 126,
                    "character": 1
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
                    "scopeId": 12
                  }
                ],
                "innerScope": {
                  "scopeStack": [
                    {
                      "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                    }
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
                  "line": 115,
                  "character": 23
                },
                "end": {
                  "line": 115,
                  "character": 32
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
          "tag": {
            "scope": {
              "scopeStack": [
                {
                  "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                },
                {
                  "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                  "scopeId": 12
                }
              ],
              "innerScope": {
                "scopeStack": [
                  {
                    "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                  }
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
                "line": 115,
                "character": 4
              },
              "end": {
                "line": 115,
                "character": 37
              }
            }
          }
        },
        "o1": {
          "out": {
            "#class": "vc.data.TACSymbol.Var.Full",
            "namePrefix": "I51",
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
                "id": "alice",
                "tag": {
                  "scope": {
                    "scopeStack": [
                      {
                        "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                      },
                      {
                        "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                        "scopeId": 12
                      }
                    ],
                    "innerScope": {
                      "scopeStack": [
                        {
                          "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                        }
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
                      "line": 114
                    },
                    "end": {
                      "line": 126,
                      "character": 1
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
                      "scopeId": 12
                    }
                  ],
                  "innerScope": {
                    "scopeStack": [
                      {
                        "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                      }
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
                    "line": 114
                  },
                  "end": {
                    "line": 126,
                    "character": 1
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
                    "scopeId": 12
                  }
                ],
                "innerScope": {
                  "scopeStack": [
                    {
                      "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                    }
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
                  "line": 115,
                  "character": 4
                },
                "end": {
                  "line": 115,
                  "character": 13
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
            "namePrefix": "I74",
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
                "id": "bob",
                "tag": {
                  "scope": {
                    "scopeStack": [
                      {
                        "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                      },
                      {
                        "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                        "scopeId": 12
                      }
                    ],
                    "innerScope": {
                      "scopeStack": [
                        {
                          "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                        }
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
                      "line": 114
                    },
                    "end": {
                      "line": 126,
                      "character": 1
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
                      "scopeId": 12
                    }
                  ],
                  "innerScope": {
                    "scopeStack": [
                      {
                        "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                      }
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
                    "line": 114
                  },
                  "end": {
                    "line": 126,
                    "character": 1
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
                    "scopeId": 12
                  }
                ],
                "innerScope": {
                  "scopeStack": [
                    {
                      "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                    }
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
                  "line": 115,
                  "character": 23
                },
                "end": {
                  "line": 115,
                  "character": 32
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
          "line": 114
        },
        "end": {
          "line": 126,
          "character": 1
        }
      }
    }
  ],
  "46": [
    {
      "key": {
        "name": "cvl.exp",
        "type": "spec.CVLExpToTACExprMeta",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "spec.CVLExpToTACExprMeta.BinaryCVLExp",
        "exp": {
          "#class": "spec.cvlast.CVLExp.RelopExp.ArithRelopExp.LeExp",
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
                  "id": "alice",
                  "tag": {
                    "scope": {
                      "scopeStack": [
                        {
                          "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                        },
                        {
                          "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                          "scopeId": 12
                        }
                      ],
                      "innerScope": {
                        "scopeStack": [
                          {
                            "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                          }
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
                        "line": 114
                      },
                      "end": {
                        "line": 126,
                        "character": 1
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
                        "scopeId": 12
                      }
                    ],
                    "innerScope": {
                      "scopeStack": [
                        {
                          "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                        }
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
                      "line": 114
                    },
                    "end": {
                      "line": 126,
                      "character": 1
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
                      "scopeId": 12
                    }
                  ],
                  "innerScope": {
                    "scopeStack": [
                      {
                        "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                      }
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
                    "line": 115,
                    "character": 4
                  },
                  "end": {
                    "line": 115,
                    "character": 13
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
                  "id": "bob",
                  "tag": {
                    "scope": {
                      "scopeStack": [
                        {
                          "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                        },
                        {
                          "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                          "scopeId": 12
                        }
                      ],
                      "innerScope": {
                        "scopeStack": [
                          {
                            "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                          }
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
                        "line": 114
                      },
                      "end": {
                        "line": 126,
                        "character": 1
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
                        "scopeId": 12
                      }
                    ],
                    "innerScope": {
                      "scopeStack": [
                        {
                          "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                        }
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
                      "line": 114
                    },
                    "end": {
                      "line": 126,
                      "character": 1
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
                      "scopeId": 12
                    }
                  ],
                  "innerScope": {
                    "scopeStack": [
                      {
                        "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                      }
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
                    "line": 115,
                    "character": 23
                  },
                  "end": {
                    "line": 115,
                    "character": 32
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
            "tag": {
              "scope": {
                "scopeStack": [
                  {
                    "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                  },
                  {
                    "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                    "scopeId": 12
                  }
                ],
                "innerScope": {
                  "scopeStack": [
                    {
                      "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                    }
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
                  "line": 115,
                  "character": 4
                },
                "end": {
                  "line": 115,
                  "character": 37
                }
              }
            }
          },
          "r": {
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
                        "scopeId": 12
                      }
                    ],
                    "innerScope": {
                      "scopeStack": [
                        {
                          "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                        }
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
                      "line": 114
                    },
                    "end": {
                      "line": 126,
                      "character": 1
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
                      "scopeId": 12
                    }
                  ],
                  "innerScope": {
                    "scopeStack": [
                      {
                        "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                      }
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
                    "line": 115,
                    "character": 52
                  },
                  "end": {
                    "line": 115,
                    "character": 63
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
                    "scopeId": 12
                  }
                ],
                "innerScope": {
                  "scopeStack": [
                    {
                      "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                    }
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
                  "line": 115,
                  "character": 41
                },
                "end": {
                  "line": 115,
                  "character": 65
                }
              }
            },
            "castType": "TO"
          },
          "tag": {
            "scope": {
              "scopeStack": [
                {
                  "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                },
                {
                  "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                  "scopeId": 12
                }
              ],
              "innerScope": {
                "scopeStack": [
                  {
                    "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                  }
                ],
                "innerScope": {
                  "scopeStack": [
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
                "line": 115,
                "character": 4
              },
              "end": {
                "line": 115,
                "character": 66
              }
            }
          }
        },
        "o1": {
          "out": {
            "#class": "vc.data.TACSymbol.Var.Full",
            "namePrefix": "I152",
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
                  "id": "alice",
                  "tag": {
                    "scope": {
                      "scopeStack": [
                        {
                          "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                        },
                        {
                          "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                          "scopeId": 12
                        }
                      ],
                      "innerScope": {
                        "scopeStack": [
                          {
                            "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                          }
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
                        "line": 114
                      },
                      "end": {
                        "line": 126,
                        "character": 1
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
                        "scopeId": 12
                      }
                    ],
                    "innerScope": {
                      "scopeStack": [
                        {
                          "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                        }
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
                      "line": 114
                    },
                    "end": {
                      "line": 126,
                      "character": 1
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
                      "scopeId": 12
                    }
                  ],
                  "innerScope": {
                    "scopeStack": [
                      {
                        "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                      }
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
                    "line": 115,
                    "character": 4
                  },
                  "end": {
                    "line": 115,
                    "character": 13
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
                  "id": "bob",
                  "tag": {
                    "scope": {
                      "scopeStack": [
                        {
                          "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                        },
                        {
                          "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                          "scopeId": 12
                        }
                      ],
                      "innerScope": {
                        "scopeStack": [
                          {
                            "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                          }
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
                        "line": 114
                      },
                      "end": {
                        "line": 126,
                        "character": 1
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
                        "scopeId": 12
                      }
                    ],
                    "innerScope": {
                      "scopeStack": [
                        {
                          "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                        }
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
                      "line": 114
                    },
                    "end": {
                      "line": 126,
                      "character": 1
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
                      "scopeId": 12
                    }
                  ],
                  "innerScope": {
                    "scopeStack": [
                      {
                        "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                      }
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
                    "line": 115,
                    "character": 23
                  },
                  "end": {
                    "line": 115,
                    "character": 32
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
            "tag": {
              "scope": {
                "scopeStack": [
                  {
                    "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                  },
                  {
                    "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                    "scopeId": 12
                  }
                ],
                "innerScope": {
                  "scopeStack": [
                    {
                      "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                    }
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
                  "line": 115,
                  "character": 4
                },
                "end": {
                  "line": 115,
                  "character": 37
                }
              }
            }
          }
        },
        "o2": {
          "out": {
            "#class": "vc.data.TACSymbol.Var.Full",
            "namePrefix": "I89",
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
                        "scopeId": 12
                      }
                    ],
                    "innerScope": {
                      "scopeStack": [
                        {
                          "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                        }
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
                      "line": 114
                    },
                    "end": {
                      "line": 126,
                      "character": 1
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
                      "scopeId": 12
                    }
                  ],
                  "innerScope": {
                    "scopeStack": [
                      {
                        "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                      }
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
                    "line": 115,
                    "character": 52
                  },
                  "end": {
                    "line": 115,
                    "character": 63
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
                    "scopeId": 12
                  }
                ],
                "innerScope": {
                  "scopeStack": [
                    {
                      "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                    }
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
                  "line": 115,
                  "character": 41
                },
                "end": {
                  "line": 115,
                  "character": 65
                }
              }
            },
            "castType": "TO"
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
          "line": 114
        },
        "end": {
          "line": 126,
          "character": 1
        }
      }
    }
  ],
  "47": [
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
  "50": [
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
  "51": [
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
  "52": [
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
  "53": [
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
  "54": [
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
  "55": [
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
          "line": 114
        },
        "end": {
          "line": 126,
          "character": 1
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
                "id": "alice",
                "tag": {
                  "scope": {
                    "scopeStack": [
                      {
                        "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                      },
                      {
                        "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                        "scopeId": 12
                      }
                    ],
                    "innerScope": {
                      "scopeStack": [
                        {
                          "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                        }
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
                      "line": 114
                    },
                    "end": {
                      "line": 126,
                      "character": 1
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
                      "scopeId": 12
                    }
                  ],
                  "innerScope": {
                    "scopeStack": [
                      {
                        "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                      }
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
                    "line": 114
                  },
                  "end": {
                    "line": 126,
                    "character": 1
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
                    "scopeId": 12
                  }
                ],
                "innerScope": {
                  "scopeStack": [
                    {
                      "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                    }
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
                  "line": 115,
                  "character": 4
                },
                "end": {
                  "line": 115,
                  "character": 13
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
                "id": "bob",
                "tag": {
                  "scope": {
                    "scopeStack": [
                      {
                        "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                      },
                      {
                        "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                        "scopeId": 12
                      }
                    ],
                    "innerScope": {
                      "scopeStack": [
                        {
                          "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                        }
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
                      "line": 114
                    },
                    "end": {
                      "line": 126,
                      "character": 1
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
                      "scopeId": 12
                    }
                  ],
                  "innerScope": {
                    "scopeStack": [
                      {
                        "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                      }
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
                    "line": 114
                  },
                  "end": {
                    "line": 126,
                    "character": 1
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
                    "scopeId": 12
                  }
                ],
                "innerScope": {
                  "scopeStack": [
                    {
                      "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                    }
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
                  "line": 115,
                  "character": 23
                },
                "end": {
                  "line": 115,
                  "character": 32
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
          "tag": {
            "scope": {
              "scopeStack": [
                {
                  "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                },
                {
                  "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                  "scopeId": 12
                }
              ],
              "innerScope": {
                "scopeStack": [
                  {
                    "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                  }
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
                "line": 115,
                "character": 4
              },
              "end": {
                "line": 115,
                "character": 37
              }
            }
          }
        },
        "o1": {
          "out": {
            "#class": "vc.data.TACSymbol.Var.Full",
            "namePrefix": "I112",
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
                "id": "alice",
                "tag": {
                  "scope": {
                    "scopeStack": [
                      {
                        "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                      },
                      {
                        "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                        "scopeId": 12
                      }
                    ],
                    "innerScope": {
                      "scopeStack": [
                        {
                          "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                        }
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
                      "line": 114
                    },
                    "end": {
                      "line": 126,
                      "character": 1
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
                      "scopeId": 12
                    }
                  ],
                  "innerScope": {
                    "scopeStack": [
                      {
                        "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                      }
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
                    "line": 114
                  },
                  "end": {
                    "line": 126,
                    "character": 1
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
                    "scopeId": 12
                  }
                ],
                "innerScope": {
                  "scopeStack": [
                    {
                      "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                    }
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
                  "line": 115,
                  "character": 4
                },
                "end": {
                  "line": 115,
                  "character": 13
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
            "namePrefix": "I135",
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
                "id": "bob",
                "tag": {
                  "scope": {
                    "scopeStack": [
                      {
                        "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                      },
                      {
                        "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                        "scopeId": 12
                      }
                    ],
                    "innerScope": {
                      "scopeStack": [
                        {
                          "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                        }
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
                      "line": 114
                    },
                    "end": {
                      "line": 126,
                      "character": 1
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
                      "scopeId": 12
                    }
                  ],
                  "innerScope": {
                    "scopeStack": [
                      {
                        "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                      }
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
                    "line": 114
                  },
                  "end": {
                    "line": 126,
                    "character": 1
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
                    "scopeId": 12
                  }
                ],
                "innerScope": {
                  "scopeStack": [
                    {
                      "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                    }
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
                  "line": 115,
                  "character": 23
                },
                "end": {
                  "line": 115,
                  "character": 32
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
          "line": 114
        },
        "end": {
          "line": 126,
          "character": 1
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
        "#class": "spec.CVLExpToTACExprMeta.BinaryCVLExp",
        "exp": {
          "#class": "spec.cvlast.CVLExp.RelopExp.ArithRelopExp.LeExp",
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
                  "id": "alice",
                  "tag": {
                    "scope": {
                      "scopeStack": [
                        {
                          "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                        },
                        {
                          "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                          "scopeId": 12
                        }
                      ],
                      "innerScope": {
                        "scopeStack": [
                          {
                            "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                          }
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
                        "line": 114
                      },
                      "end": {
                        "line": 126,
                        "character": 1
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
                        "scopeId": 12
                      }
                    ],
                    "innerScope": {
                      "scopeStack": [
                        {
                          "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                        }
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
                      "line": 114
                    },
                    "end": {
                      "line": 126,
                      "character": 1
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
                      "scopeId": 12
                    }
                  ],
                  "innerScope": {
                    "scopeStack": [
                      {
                        "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                      }
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
                    "line": 115,
                    "character": 4
                  },
                  "end": {
                    "line": 115,
                    "character": 13
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
                  "id": "bob",
                  "tag": {
                    "scope": {
                      "scopeStack": [
                        {
                          "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                        },
                        {
                          "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                          "scopeId": 12
                        }
                      ],
                      "innerScope": {
                        "scopeStack": [
                          {
                            "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                          }
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
                        "line": 114
                      },
                      "end": {
                        "line": 126,
                        "character": 1
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
                        "scopeId": 12
                      }
                    ],
                    "innerScope": {
                      "scopeStack": [
                        {
                          "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                        }
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
                      "line": 114
                    },
                    "end": {
                      "line": 126,
                      "character": 1
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
                      "scopeId": 12
                    }
                  ],
                  "innerScope": {
                    "scopeStack": [
                      {
                        "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                      }
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
                    "line": 115,
                    "character": 23
                  },
                  "end": {
                    "line": 115,
                    "character": 32
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
            "tag": {
              "scope": {
                "scopeStack": [
                  {
                    "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                  },
                  {
                    "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                    "scopeId": 12
                  }
                ],
                "innerScope": {
                  "scopeStack": [
                    {
                      "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                    }
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
                  "line": 115,
                  "character": 4
                },
                "end": {
                  "line": 115,
                  "character": 37
                }
              }
            }
          },
          "r": {
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
                        "scopeId": 12
                      }
                    ],
                    "innerScope": {
                      "scopeStack": [
                        {
                          "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                        }
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
                      "line": 114
                    },
                    "end": {
                      "line": 126,
                      "character": 1
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
                      "scopeId": 12
                    }
                  ],
                  "innerScope": {
                    "scopeStack": [
                      {
                        "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                      }
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
                    "line": 115,
                    "character": 52
                  },
                  "end": {
                    "line": 115,
                    "character": 63
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
                    "scopeId": 12
                  }
                ],
                "innerScope": {
                  "scopeStack": [
                    {
                      "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                    }
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
                  "line": 115,
                  "character": 41
                },
                "end": {
                  "line": 115,
                  "character": 65
                }
              }
            },
            "castType": "TO"
          },
          "tag": {
            "scope": {
              "scopeStack": [
                {
                  "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                },
                {
                  "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                  "scopeId": 12
                }
              ],
              "innerScope": {
                "scopeStack": [
                  {
                    "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                  }
                ],
                "innerScope": {
                  "scopeStack": [
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
                "line": 115,
                "character": 4
              },
              "end": {
                "line": 115,
                "character": 66
              }
            }
          }
        },
        "o1": {
          "out": {
            "#class": "vc.data.TACSymbol.Var.Full",
            "namePrefix": "I208",
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
                  "id": "alice",
                  "tag": {
                    "scope": {
                      "scopeStack": [
                        {
                          "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                        },
                        {
                          "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                          "scopeId": 12
                        }
                      ],
                      "innerScope": {
                        "scopeStack": [
                          {
                            "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                          }
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
                        "line": 114
                      },
                      "end": {
                        "line": 126,
                        "character": 1
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
                        "scopeId": 12
                      }
                    ],
                    "innerScope": {
                      "scopeStack": [
                        {
                          "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                        }
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
                      "line": 114
                    },
                    "end": {
                      "line": 126,
                      "character": 1
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
                      "scopeId": 12
                    }
                  ],
                  "innerScope": {
                    "scopeStack": [
                      {
                        "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                      }
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
                    "line": 115,
                    "character": 4
                  },
                  "end": {
                    "line": 115,
                    "character": 13
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
                  "id": "bob",
                  "tag": {
                    "scope": {
                      "scopeStack": [
                        {
                          "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                        },
                        {
                          "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                          "scopeId": 12
                        }
                      ],
                      "innerScope": {
                        "scopeStack": [
                          {
                            "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                          }
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
                        "line": 114
                      },
                      "end": {
                        "line": 126,
                        "character": 1
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
                        "scopeId": 12
                      }
                    ],
                    "innerScope": {
                      "scopeStack": [
                        {
                          "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                        }
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
                      "line": 114
                    },
                    "end": {
                      "line": 126,
                      "character": 1
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
                      "scopeId": 12
                    }
                  ],
                  "innerScope": {
                    "scopeStack": [
                      {
                        "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                      }
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
                    "line": 115,
                    "character": 23
                  },
                  "end": {
                    "line": 115,
                    "character": 32
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
            "tag": {
              "scope": {
                "scopeStack": [
                  {
                    "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                  },
                  {
                    "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                    "scopeId": 12
                  }
                ],
                "innerScope": {
                  "scopeStack": [
                    {
                      "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                    }
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
                  "line": 115,
                  "character": 4
                },
                "end": {
                  "line": 115,
                  "character": 37
                }
              }
            }
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
                        "scopeId": 12
                      }
                    ],
                    "innerScope": {
                      "scopeStack": [
                        {
                          "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                        }
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
                      "line": 114
                    },
                    "end": {
                      "line": 126,
                      "character": 1
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
                      "scopeId": 12
                    }
                  ],
                  "innerScope": {
                    "scopeStack": [
                      {
                        "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                      }
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
                    "line": 115,
                    "character": 52
                  },
                  "end": {
                    "line": 115,
                    "character": 63
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
                    "scopeId": 12
                  }
                ],
                "innerScope": {
                  "scopeStack": [
                    {
                      "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                    }
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
                  "line": 115,
                  "character": 41
                },
                "end": {
                  "line": 115,
                  "character": 65
                }
              }
            },
            "castType": "TO"
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
          "line": 114
        },
        "end": {
          "line": 126,
          "character": 1
        }
      }
    }
  ],
  "58": [
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
          "line": 114
        },
        "end": {
          "line": 126,
          "character": 1
        }
      }
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
      "value": 1016
    }
  ],
  "61": [
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
      "value": 1012
    }
  ],
  "63": [
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
          "callIndex": 4,
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
  "64": [
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
  "65": [
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
          "callIndex": 4,
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
  "66": [
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