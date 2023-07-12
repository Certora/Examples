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
		CANON123:JSON{"name":"CANON123","paramSorts":[],"returnSort":{"#class":"tac.Tag.Int"},"attribute":"Ghost","cvlResultType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Mathint"},"cvlParamTypes":[],"declarationName":"CANON123"}
	}
	tacM0x20@4:bv256
	tacCaller@4:bv256
	tacCalldatabufCANON0@4:bv256
	tacCalldatabufCANON1@4:bv256
	tacMCANON0!!1:bytemap
	tacM0x0!!48:bv256
	tacM0x0!!71:bv256
	tacAddress!!36:bv256
	tacAddress!!59:bv256
	tacAddress!!79:bv256
	tacAddress!!97:bv256
	tacOrigin!!182:bv256
	tacCallvalue@4:bv256
	lastReverted:bool
	lastReverted@1:bool
	lastReverted@2:bool
	lastReverted@3:bool
	lastReverted@4:bool
	lastReverted@5:bool
	lastReverted@6:bool
	lastReverted@7:bool
	tacM0x0!!109:bv256
	tacM0x0!!132:bv256
	tacM0x0!!228:bv256
	tacM0x0!!231:bv256
	tacM0x0!!242:bv256
	tacM0x0!!245:bv256
	tacExtcodesize!!0:wordmap
	CANON31!!3:wordmap
	CANON46!!4:bv256
	CANON92!!5:wordmap
	tacCalldatasize@1:bv256
	tacCalldatasize@2:bv256
	tacCalldatasize@3:bv256
	tacCalldatasize@4:bv256
	tacCalldatasize@5:bv256
	tacCalldatasize@6:bv256
	tacCalldatasize@7:bv256
	tacCalldatasize!!114:bv256
	tacCalldatasize!!137:bv256
	tacCalldatasize!!163:bv256
	tacM0x0@1:bv256
	tacM0x0@2:bv256
	tacM0x0@4:bv256
	tacM0x0@5:bv256
	tacM0x0@6:bv256
	tacExtcodesize:wordmap
	CANON101:int
	CANON102:bool
	CANON103:bool
	CANON104:bool
	CANON105:bv256
	CANON106:bool
	CANON107:bool
	CANON108:int
	CANON109:int
	CANON110:bool
	CANON111:bool
	CANON112:bool
	CANON113:bv256
	CANON114:bool
	CANON115:bool
	CANON116:int
	CANON117:int
	CANON118:bool
	CANON119:bool
	CANON120:int
	CANON121:int
	CANON122:bool
	CANON123:int
	tacSighash!!7:bv256
	tacSighash!!8:bv256
	tacSighash!!9:bv256
	tacCalldatasize!!30:bv256
	tacCalldatasize!!53:bv256
	tacCalldatasize!!76:bv256
	tacCalldatasize!!91:bv256
	tacMCANON0@4:bytemap
	tacMCANON1@4:bytemap
	tacBalance:wordmap
	tacTimestamp!!192:bv256
	tacNumber@4:bv256
	tacBalance!!2:wordmap
	R6:bv256
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
	B26:bool
	B28:bool
	B31:bool
	B32:bool
	B33:bool
	B35:bool
	B38:bool
	B39:bool
	B40:bool
	B41:bool
	B42:bool
	B44:bool
	B46:bool
	B54:bool
	B55:bool
	B56:bool
	B58:bool
	B61:bool
	B62:bool
	B63:bool
	B64:bool
	B65:bool
	B67:bool
	B69:bool
	B77:bool
	B78:bool
	B81:bool
	B82:bool
	B83:bool
	B84:bool
	B85:bool
	B86:bool
	B87:bool
	B92:bool
	B93:bool
	B94:bool
	B96:bool
	B99:bool
	I29:int
	I52:int
	I75:int
	I90:int
	R27:bv256
	R34:bv256
	R37:bv256
	R43:bv256
	R45:bv256
	R47:bv256
	R49:(uninterp) skey
	R50:bv256
	R51:bv256
	R57:bv256
	R60:bv256
	R66:bv256
	R68:bv256
	R70:bv256
	R72:(uninterp) skey
	R73:bv256
	R74:bv256
	R80:bv256
	R88:bv256
	R89:bv256
	R95:bv256
	R98:bv256
	B100:bool
	B101:bool
	B102:bool
	B103:bool
	B105:bool
	B107:bool
	B115:bool
	B116:bool
	B117:bool
	B119:bool
	B122:bool
	B123:bool
	B124:bool
	B125:bool
	B126:bool
	B128:bool
	B130:bool
	B138:bool
	B139:bool
	B142:bool
	B143:bool
	B144:bool
	B145:bool
	B146:bool
	B147:bool
	B148:bool
	B155:bool
	B164:bool
	B165:bool
	B169:bool
	B172:bool
	B174:bool
	B177:bool
	B180:bool
	B183:bool
	B185:bool
	B188:bool
	B190:bool
	B193:bool
	B195:bool
	B198:bool
	B207:bool
	B211:bool
	B213:bool
	B214:bool
	B215:bool
	B216:bool
	B217:bool
	B218:bool
	B219:bool
	B220:bool
	B221:bool
	B223:bool
	B225:bool
	B235:bool
	B238:bool
	B240:bool
	I113:int
	I136:int
	I151:int
	I152:int
	I153:int
	I154:int
	I156:int
	I157:int
	I158:int
	I159:int
	I160:int
	I168:int
	I173:int
	I179:int
	I184:int
	I189:int
	I194:int
	I197:int
	I203:int
	I208:int
	I209:int
	I210:int
	I248:int
	M161:bytemap
	R104:bv256
	R106:bv256
	R108:bv256
	R110:(uninterp) skey
	R111:bv256
	R112:bv256
	R118:bv256
	R121:bv256
	R127:bv256
	R129:bv256
	R131:bv256
	R133:(uninterp) skey
	R134:bv256
	R135:bv256
	R141:bv256
	R149:bv256
	R150:bv256
	R162:bv256
	R166:bv256
	R167:bv256
	R170:bv256
	R175:bv256
	R181:bv256
	R186:bv256
	R191:bv256
	R196:bv256
	R199:bv256
	R200:bv256
	R201:bv256
	R202:bv256
	R205:bv256
	R206:bv256
	R212:bv256
	R222:bv256
	R224:bv256
	R226:bv256
	R227:bv256
	R229:(uninterp) skey
	R230:bv256
	R233:(uninterp) skey
	R234:bv256
	R236:bv256
	R237:bv256
	R239:bv256
	R241:bv256
	R243:bv256
	R244:bv256
	R247:bv256
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
	LCANON2@4:bool
	LCANON2@5:bool
	LCANON2@6:bool
	LCANON3@1:bool
	LCANON3@2:bool
	LCANON3@4:bool
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
	tacCallvalue!!176:bv256
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
	CANON92:wordmap
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
	LCANON15@7:bool
	LCANON16@3:bool
	LCANON16@7:bool
	LCANON17@3:bool
	LCANON17@7:bool
	LCANON18@3:bool
	LCANON18@7:bool
	LCANON19@3:bv256
	LCANON19@7:bv256
	LCANON20@3:bv256
	LCANON20@7:bv256
	LCANON21@3:bv256
	LCANON21@7:bv256
	LCANON22@4:bool
	LCANON23@4:bool
	LCANON24@4:bool
	LCANON25@4:bv256
	LCANON26@4:bool
	LCANON27@4:bv256
	LCANON28@4:bool
	LCANON29@4:bv256
	LCANON30@4:bv256
	LCANON31@4:bool
	LCANON32@4:bv256
	LCANON33@4:bv256
	LCANON34@4:bv256
	LCANON35@4:bv256
	LCANON36@4:bv256
	LCANON37@4:bv256
	LCANON38@4:bv256
	LCANON39@4:bv256
	LCANON40@4:bool
	LCANON41@4:bv256
	LCANON42@4:bv256
	LCANON43@4:bool
	LCANON44@4:bv256
	LCANON45@4:bool
	LCANON46@4:bv256
	LCANON47@4:bv256
	LCANON48@4:bv256
	LCANON49@4:bv256
	LCANON50@4:bv256
	LCANON51@4:bv256
	LCANON52@4:bv256
	LCANON53@4:bv256
	LCANON54@4:bv256
	LCANON55@4:bv256
	LCANON56@4:bv256
	tacContractAtCANON0:bv256
	lastHasThrown:bool
	lastHasThrown@1:bool
	lastHasThrown@2:bool
	lastHasThrown@3:bool
	lastHasThrown@4:bool
	lastHasThrown@5:bool
	lastHasThrown@6:bool
	lastHasThrown@7:bool
	tacM0x20!!232:bv256
	tacM0x20!!246:bv256
	tacAddress!!120:bv256
	tacAddress!!140:bv256
	tacAddress!!178:bv256
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
	tacCaller!!171:bv256
	tacBalance!!204:wordmap
	tacTimestamp@4:bv256
	tacSighash!!10:bv256
	tacSighash!!11:bv256
	tacSighash!!12:bv256
	tacSighash!!13:bv256
	tacSighash@1:bv256
	tacSighash@2:bv256
	tacSighash@3:bv256
	tacSighash@4:bv256
	tacSighash@5:bv256
	tacSighash@6:bv256
	tacSighash@7:bv256
	tacNumber!!187:bv256
}
Program {
	Block 0_0_0_0_0_0 Succ [0_0_0_1_0_0] {
		AssignHavocCmd tacExtcodesize!!0:0
		AssignHavocCmd tacBalance!!2:1
		AssignHavocCmd CANON31!!3:2
		AssignHavocCmd CANON46!!4:3
		AssignHavocCmd CANON56:4
		AssignHavocCmd CANON58:5
		AssignHavocCmd CANON92!!5:6
		AssignHavocCmd R6:7
		AssignHavocCmd tacSighash!!7:8
		AssignHavocCmd tacSighash!!8:8
		AssignHavocCmd tacSighash!!9:8
		AssignHavocCmd tacSighash!!10:8
		AssignHavocCmd tacSighash!!11:8
		AssignHavocCmd tacSighash!!12:8
		AssignHavocCmd tacSighash!!13:8
		AssignExpCmd CANON0:9 0xa457c2d7
		AssignExpCmd CANON1:10 false
		AssignExpCmd CANON2:11 false
		AssignExpCmd CANON3:12 false
		AssignExpCmd CANON4:13 0x2
		AssignExpCmd CANON5:14 false
		AnnotationCmd JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Message","s":"Setup"}}
		AnnotationCmd JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Message","s":"multi contract setup"}}
		AnnotationCmd JSON{"key":{"name":"cvl.label.end","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		AnnotationCmd JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Message","s":"rule parameters setup"}}
		AssignHavocCmd CANON6:15
		NopCmd
		AssumeExpCmd LAnd(Le(CANON6:15 0xffffffffffffffffffffffffffffffffffffffff ) Ge(CANON6:15 0x0 ) )
		AssignHavocCmd CANON8:16
		NopCmd
		AssumeExpCmd LAnd(Le(CANON8:16 0xffffffffffffffffffffffffffffffffffffffff ) Ge(CANON8:16 0x0 ) )
		AssumeCmd true
		AssumeCmd true
		AssignHavocCmd CANON9:17
		AssignHavocCmd CANON10:18
		AssignHavocCmd CANON11:19
		AssignHavocCmd CANON12:20
		AssignHavocCmd CANON13:21
		AssignHavocCmd CANON14:22
		AssignHavocCmd CANON15:23
		AssignHavocCmd CANON16:24
		NopCmd
		AssumeExpCmd LAnd(Le(CANON9:17 0xffffffffffffffffffffffffffffffffffffffff ) Ge(CANON9:17 0x0 ) )
		NopCmd
		AssumeExpCmd LAnd(Le(CANON10:18 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff ) Ge(CANON10:18 0x0 ) )
		NopCmd
		AssumeExpCmd LAnd(Le(CANON11:19 0xffffffffffffffffffffffffffffffffffffffff ) Ge(CANON11:19 0x0 ) )
		NopCmd
		AssumeExpCmd LAnd(Le(CANON12:20 0xffffffffffffffffffffffffffffffffffffffff ) Ge(CANON12:20 0x0 ) )
		NopCmd
		AssumeExpCmd LAnd(Le(CANON13:21 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff ) Ge(CANON13:21 0x0 ) )
		NopCmd
		AssumeExpCmd LAnd(Le(CANON14:22 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff ) Ge(CANON14:22 0x0 ) )
		NopCmd
		AssumeExpCmd LAnd(Le(CANON15:23 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff ) Ge(CANON15:23 0x0 ) )
		NopCmd
		AssumeExpCmd LAnd(Le(CANON16:24 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff ) Ge(CANON16:24 0x0 ) )
		AnnotationCmd JSON{"key":{"name":"cvl.label.end","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		AnnotationCmd JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Message","s":"contract address vars initialized"}}
		AnnotationCmd JSON{"key":{"name":"cvl.label.end","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		AnnotationCmd JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Message","s":"setup read tracking instrumentation"}}
		AnnotationCmd JSON{"key":{"name":"cvl.label.end","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		AnnotationCmd JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Message","s":"last storage initialize"}}
		AnnotationCmd JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageGlobalChangeSnippet.StorageTakeSnapshot","lhs":{"namePrefix":"lastStorage","tag":{"#class":"tac.Tag.BlockchainState"},"callIndex":0,"meta":[{"key":{"name":"cvl.local","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true},{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"lastStorage"},{"key":{"name":"cvl.type","type":"spec.cvlast.CVLType$PureCVLType","erasureStrategy":"CallTrace"},"value":{"#class":"spec.cvlast.CVLType.PureCVLType.VMInternal.BlockchainState"}},{"key":{"name":"cvl","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true},{"key":{"name":"cvl.display","type":"java.lang.String","erasureStrategy":"CallTrace"},"value":"lastStorage"}]}}}
		AnnotationCmd JSON{"key":{"name":"cvl.label.end","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		AnnotationCmd JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Message","s":"assumptions about extcodesize"}}
		AssignExpCmd B24:25 Gt(Select(tacExtcodesize!!0:0 Apply(to_skey:bif R6:7) ) 0x0 )
		AssumeCmd B24:25
		AnnotationCmd JSON{"key":{"name":"cvl.label.end","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		AnnotationCmd JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Message","s":"assumptions about contracts' addresses"}}
		NopCmd
		AssumeExpCmd Gt(R6:7 0x0 )
		NopCmd
		AssumeExpCmd Le(R6:7 0xffffffffffffffffffffffffffffffffffffffff )
		AnnotationCmd JSON{"key":{"name":"cvl.label.end","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		AnnotationCmd JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Message","s":"assumptions about starting balances"}}
		AssignExpCmd R27:25 Select(tacBalance!!2:1 Apply(to_skey:bif R6:7) )
		NopCmd
		AssumeExpCmd Ge(R27:25 0x0 )
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
		AnnotationCmd:26 JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Message","s":"assume invariant in pre-state"}}
		AssignExpCmd:27 I29 CANON6:15
	}
	Block 0_0_0_1_0_0 Succ [1_0_0_0_0_0] {
		AnnotationCmd:26 JSON{"key":{"name":"call.trace.push","type":"analysis.icfg.Inliner$CallStack$PushRecord","erasureStrategy":"Canonical"},"value":"rO0ABXNyACphbmFseXNpcy5pY2ZnLklubGluZXIkQ2FsbFN0YWNrJFB1c2hSZWNvcmSX8+DCTLCH+AIAA0kACGNhbGxlZUlkTAAGY2FsbGVldAATTHZjL2RhdGEvTWV0aG9kUmVmO0wAB3N1bW1hcnl0ABVMdmMvZGF0YS9DYWxsU3VtbWFyeTt4cAAAAAFzcgARdmMuZGF0YS5NZXRob2RSZWbJlJTzzU9pGAIAA0wABGF0dHJ0ABdMc2NlbmUvTWV0aG9kQXR0cmlidXRlO0wACmNvbnRyYWN0SWR0ABZMamF2YS9tYXRoL0JpZ0ludGVnZXI7TAAHc2lnSGFzaHQAEExldm0vU2lnaGFzaEludDt4cHNyABxzY2VuZS5NZXRob2RBdHRyaWJ1dGUkQ29tbW9uNHjdebdr9XMCAAB4cgAVc2NlbmUuTWV0aG9kQXR0cmlidXRlcYg2pYWutuUCAAB4cHNyABRqYXZhLm1hdGguQmlnSW50ZWdlcoz8nx+pO/sdAwAGSQAIYml0Q291bnRJAAliaXRMZW5ndGhJABNmaXJzdE5vbnplcm9CeXRlTnVtSQAMbG93ZXN0U2V0Qml0SQAGc2lnbnVtWwAJbWFnbml0dWRldAACW0J4cgAQamF2YS5sYW5nLk51bWJlcoaslR0LlOCLAgAAeHD///////////////7////+AAAAAXVyAAJbQqzzF/gGCFTgAgAAeHAAAAAQzkYEoAAAAAAAAAAAAAAAA3hzcgAOZXZtLlNpZ2hhc2hJbnRUdcqNMXEgeAIAAUwAAW5xAH4ABnhwc3EAfgAM///////////////+/////gAAAAF1cQB+ABAAAAAEcKCCMXhw"}
		AssignHavocCmd:26 tacCalldatasize!!30:28
		NopCmd
		AssumeExpCmd Apply(add_noofl:bif 0x4 0x20)
		NopCmd
		AssumeExpCmd Apply(add_noofl:bif 0x4 0x0)
		AssignExpCmd:26 B33 LAnd(Ge(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff I29 ) Le(0x0 I29 ) )
		AssertCmd:26 B33 "sanity bounds check on cvl to vm encoding of certoraArg29792980:int failed"
		AssignExpCmd:26 R34 Apply(safe_math_narrow:bif I29)
		NopCmd
		AssumeExpCmd Eq(0x24 tacCalldatasize!!30:28 )
		LabelCmd:26 "Start procedure ERC20-balanceOf(address)"
		AnnotationCmd:26 JSON{"key":{"name":"fps.free-pointer-is-scalarized","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true}
		AssignExpCmd:26 R37:25 Select(tacExtcodesize!!0:0 Apply(to_skey:bif R6:29) )
		NopCmd
		AssumeExpCmd Gt(R37:25 0x0 )
		AnnotationCmd:26 JSON{"key":{"name":"internal.func.finder.info","type":"analysis.ip.InternalFunctionFinderReport","erasureStrategy":"Erased"},"value":"rO0ABXNyAChhbmFseXNpcy5pcC5JbnRlcm5hbEZ1bmN0aW9uRmluZGVyUmVwb3J0ian+bYn1VdACAAFMABN1bnJlc29sdmVkRnVuY3Rpb25zdAAPTGphdmEvdXRpbC9TZXQ7eHBzcgAhZGF0YXN0cnVjdHVyZXMuTGlua2VkQXJyYXlIYXNoU2V0AAAAAAAAAAEDAAJGAApsb2FkRmFjdG9yTAAJaGFzaFRhYmxldAAuTGRhdGFzdHJ1Y3R1cmVzL2FycmF5aGFzaHRhYmxlL0FycmF5SGFzaFRhYmxlO3hwdwgAAAAAQAAAAHg="}
		AnnotationCmd:26 JSON{"key":{"name":"fps.free-pointer-is-scalarized","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true}
		NopCmd
		AssumeExpCmd LNot(Lt(tacCalldatasize!!30:28 0x4 ) )
		NopCmd
		AssumeExpCmd LNot(Gt(0x70a08231 tacSighash!!7:8 ) )
		NopCmd
		AssumeExpCmd Gt(0xa9059cbb tacSighash!!7:8 )
		NopCmd
		AssumeExpCmd Eq(0x70a08231 tacSighash!!7:8 )
		AssumeCmd:30 true
		AssignExpCmd:31 R43:32 Sub(tacCalldatasize!!30:28 0x4 )
		NopCmd
		AssumeExpCmd LNot(Slt(R43:32 0x20 ) )
		NopCmd
		AssumeExpCmd Le(R34 0xffffffffffffffffffffffffffffffffffffffff )
		AnnotationCmd:26 JSON{"key":{"name":"internal.func.start","type":"analysis.ip.InternalFuncStartAnnotation","erasureStrategy":"CallTrace"},"value":{"id":0,"startPc":3130,"args":[{"s":{"namePrefix":"R34","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1013}]},"offset":1,"sort":"SCALAR"}],"methodSignature":{"#class":"spec.cvlast.QualifiedMethodSignature.QualifiedMethodSig","qualifiedMethodName":{"#class":"spec.cvlast.QualifiedFunction","host":{"name":"ERC20"},"methodId":"balanceOf"},"params":[{"#class":"spec.cvlast.VMParam.Named","name":"account","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$address"}}],"res":[{"#class":"spec.cvlast.VMParam.Unnamed","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256}}]},"stackOffsetToArgPos":{"1":0},"callSiteSrc":{"source":0,"begin":4328,"len":511,"jumpType":"ENTER","address":"ce4604a0000000000000000000000003","sourceContext":{"indexToFilepath":{"0":"contracts/ERC20.sol","1":"contracts/IERC20.sol","2":"contracts/IERC20Metadata.sol"},"sourceDir":".post_autofinders.0"}}}}
		AssignExpCmd:33 R49:34 Apply(hash_3_keccak:bif Apply(skey_basic:bif 0x40) Apply(to_skey:bif R34:35) Apply(skey_basic:bif 0x0))
		AssignExpCmd:36 R50:34 Select(CANON31!!3:2 R49:37 )
		AnnotationCmd:26 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet","value":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R50","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1020}]},"displayPath":{"#class":"analysis.storage.DisplayPath.MapAccess","key":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R34","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1018}]},"keyTyp":{"#class":"tac.TACStorageType.IntegralType","typeLabel":"address","numBytes":"14","descriptor":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$address"},"lowerBound":null,"upperBound":null},"base":{"#class":"analysis.storage.DisplayPath.Root","name":"_balances"}},"storageType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256},"contractInstance":"ce4604a0000000000000000000000003","linkableStorageReadId":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet.None"}}}
		AnnotationCmd:26 JSON{"key":{"name":"internal.func.end","type":"analysis.ip.InternalFuncExitAnnotation","erasureStrategy":"Canonical"},"value":{"id":0,"rets":[{"s":{"namePrefix":"R50","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1023}]},"offset":0}],"functionLayout":{"0":{"#class":"analysis.ip.InternalFuncValueLocation.Scalar"}}}}
		AnnotationCmd:26 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.EVMFunctionReturnWrite","returnbufOffset":"0","returnValueSym":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R50","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1023}]},"callIndex":1}}
		AnnotationCmd:26 JSON{"key":{"name":"tac.return.path","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		LabelCmd:26 "End procedure ERC20-balanceOf(address)"
		NopCmd
		AnnotationCmd:26 JSON{"key":{"name":"call.trace.pop","type":"analysis.icfg.Inliner$CallStack$PopRecord","erasureStrategy":"Canonical"},"value":"rO0ABXNyAClhbmFseXNpcy5pY2ZnLklubGluZXIkQ2FsbFN0YWNrJFBvcFJlY29yZPAPfwSLdCWJAgABSQAIY2FsbGVlSWR4cAAAAAE="}
	}
	Block 0_0_0_2_0_0 Succ [2_0_0_0_0_0] {
		AnnotationCmd:26 JSON{"key":{"name":"call.trace.push","type":"analysis.icfg.Inliner$CallStack$PushRecord","erasureStrategy":"Canonical"},"value":"rO0ABXNyACphbmFseXNpcy5pY2ZnLklubGluZXIkQ2FsbFN0YWNrJFB1c2hSZWNvcmSX8+DCTLCH+AIAA0kACGNhbGxlZUlkTAAGY2FsbGVldAATTHZjL2RhdGEvTWV0aG9kUmVmO0wAB3N1bW1hcnl0ABVMdmMvZGF0YS9DYWxsU3VtbWFyeTt4cAAAAAJzcgARdmMuZGF0YS5NZXRob2RSZWbJlJTzzU9pGAIAA0wABGF0dHJ0ABdMc2NlbmUvTWV0aG9kQXR0cmlidXRlO0wACmNvbnRyYWN0SWR0ABZMamF2YS9tYXRoL0JpZ0ludGVnZXI7TAAHc2lnSGFzaHQAEExldm0vU2lnaGFzaEludDt4cHNyABxzY2VuZS5NZXRob2RBdHRyaWJ1dGUkQ29tbW9uNHjdebdr9XMCAAB4cgAVc2NlbmUuTWV0aG9kQXR0cmlidXRlcYg2pYWutuUCAAB4cHNyABRqYXZhLm1hdGguQmlnSW50ZWdlcoz8nx+pO/sdAwAGSQAIYml0Q291bnRJAAliaXRMZW5ndGhJABNmaXJzdE5vbnplcm9CeXRlTnVtSQAMbG93ZXN0U2V0Qml0SQAGc2lnbnVtWwAJbWFnbml0dWRldAACW0J4cgAQamF2YS5sYW5nLk51bWJlcoaslR0LlOCLAgAAeHD///////////////7////+AAAAAXVyAAJbQqzzF/gGCFTgAgAAeHAAAAAQzkYEoAAAAAAAAAAAAAAAA3hzcgAOZXZtLlNpZ2hhc2hJbnRUdcqNMXEgeAIAAUwAAW5xAH4ABnhwc3EAfgAM///////////////+/////gAAAAF1cQB+ABAAAAAEcKCCMXhw"}
		AssignHavocCmd:26 tacCalldatasize!!53:28
		NopCmd
		AssumeExpCmd Apply(add_noofl:bif 0x4 0x20)
		NopCmd
		AssumeExpCmd Apply(add_noofl:bif 0x4 0x0)
		AssignExpCmd:26 B56 LAnd(Ge(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff I152 ) Le(0x0 I152 ) )
		AssertCmd:26 B56 "sanity bounds check on cvl to vm encoding of certoraArg29922993:int failed"
		AssignExpCmd:26 R57 Apply(safe_math_narrow:bif I152)
		NopCmd
		AssumeExpCmd Eq(0x24 tacCalldatasize!!53:28 )
		LabelCmd:26 "Start procedure ERC20-balanceOf(address)"
		AnnotationCmd:26 JSON{"key":{"name":"fps.free-pointer-is-scalarized","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true}
		AssignExpCmd:26 R60:25 Select(tacExtcodesize!!0:0 Apply(to_skey:bif R6:29) )
		NopCmd
		AssumeExpCmd Gt(R60:25 0x0 )
		AnnotationCmd:26 JSON{"key":{"name":"internal.func.finder.info","type":"analysis.ip.InternalFunctionFinderReport","erasureStrategy":"Erased"},"value":"rO0ABXNyAChhbmFseXNpcy5pcC5JbnRlcm5hbEZ1bmN0aW9uRmluZGVyUmVwb3J0ian+bYn1VdACAAFMABN1bnJlc29sdmVkRnVuY3Rpb25zdAAPTGphdmEvdXRpbC9TZXQ7eHBzcgAhZGF0YXN0cnVjdHVyZXMuTGlua2VkQXJyYXlIYXNoU2V0AAAAAAAAAAEDAAJGAApsb2FkRmFjdG9yTAAJaGFzaFRhYmxldAAuTGRhdGFzdHJ1Y3R1cmVzL2FycmF5aGFzaHRhYmxlL0FycmF5SGFzaFRhYmxlO3hwdwgAAAAAQAAAAHg="}
		AnnotationCmd:26 JSON{"key":{"name":"fps.free-pointer-is-scalarized","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true}
		NopCmd
		AssumeExpCmd LNot(Lt(tacCalldatasize!!53:28 0x4 ) )
		NopCmd
		AssumeExpCmd LNot(Gt(0x70a08231 tacSighash!!8:8 ) )
		NopCmd
		AssumeExpCmd Gt(0xa9059cbb tacSighash!!8:8 )
		NopCmd
		AssumeExpCmd Eq(0x70a08231 tacSighash!!8:8 )
		AssumeCmd:30 true
		AssignExpCmd:31 R66:32 Sub(tacCalldatasize!!53:28 0x4 )
		NopCmd
		AssumeExpCmd LNot(Slt(R66:32 0x20 ) )
		NopCmd
		AssumeExpCmd Le(R57 0xffffffffffffffffffffffffffffffffffffffff )
		AnnotationCmd:26 JSON{"key":{"name":"internal.func.start","type":"analysis.ip.InternalFuncStartAnnotation","erasureStrategy":"CallTrace"},"value":{"id":1,"startPc":3130,"args":[{"s":{"namePrefix":"R57","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1013}]},"offset":1,"sort":"SCALAR"}],"methodSignature":{"#class":"spec.cvlast.QualifiedMethodSignature.QualifiedMethodSig","qualifiedMethodName":{"#class":"spec.cvlast.QualifiedFunction","host":{"name":"ERC20"},"methodId":"balanceOf"},"params":[{"#class":"spec.cvlast.VMParam.Named","name":"account","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$address"}}],"res":[{"#class":"spec.cvlast.VMParam.Unnamed","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256}}]},"stackOffsetToArgPos":{"1":0},"callSiteSrc":{"source":0,"begin":4328,"len":511,"jumpType":"ENTER","address":"ce4604a0000000000000000000000003","sourceContext":{"indexToFilepath":{"0":"contracts/ERC20.sol","1":"contracts/IERC20.sol","2":"contracts/IERC20Metadata.sol"},"sourceDir":".post_autofinders.0"}}}}
		AssignExpCmd:33 R72:34 Apply(hash_3_keccak:bif Apply(skey_basic:bif 0x40) Apply(to_skey:bif R57:35) Apply(skey_basic:bif 0x0))
		AssignExpCmd:38 R73:34 Select(CANON31!!3:2 R72:39 )
		AnnotationCmd:26 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet","value":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R73","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1020}]},"displayPath":{"#class":"analysis.storage.DisplayPath.MapAccess","key":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R57","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1018}]},"keyTyp":{"#class":"tac.TACStorageType.IntegralType","typeLabel":"address","numBytes":"14","descriptor":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$address"},"lowerBound":null,"upperBound":null},"base":{"#class":"analysis.storage.DisplayPath.Root","name":"_balances"}},"storageType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256},"contractInstance":"ce4604a0000000000000000000000003","linkableStorageReadId":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet.None"}}}
		AnnotationCmd:26 JSON{"key":{"name":"internal.func.end","type":"analysis.ip.InternalFuncExitAnnotation","erasureStrategy":"Canonical"},"value":{"id":1,"rets":[{"s":{"namePrefix":"R73","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1023}]},"offset":0}],"functionLayout":{"0":{"#class":"analysis.ip.InternalFuncValueLocation.Scalar"}}}}
		AnnotationCmd:26 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.EVMFunctionReturnWrite","returnbufOffset":"0","returnValueSym":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R73","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1023}]},"callIndex":2}}
		AnnotationCmd:26 JSON{"key":{"name":"tac.return.path","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		LabelCmd:26 "End procedure ERC20-balanceOf(address)"
		NopCmd
		AnnotationCmd:26 JSON{"key":{"name":"call.trace.pop","type":"analysis.icfg.Inliner$CallStack$PopRecord","erasureStrategy":"Canonical"},"value":"rO0ABXNyAClhbmFseXNpcy5pY2ZnLklubGluZXIkQ2FsbFN0YWNrJFBvcFJlY29yZPAPfwSLdCWJAgABSQAIY2FsbGVlSWR4cAAAAAI="}
	}
	Block 0_0_0_3_0_0 Succ [3_0_0_0_0_0] {
		AnnotationCmd:26 JSON{"key":{"name":"call.trace.push","type":"analysis.icfg.Inliner$CallStack$PushRecord","erasureStrategy":"Canonical"},"value":"rO0ABXNyACphbmFseXNpcy5pY2ZnLklubGluZXIkQ2FsbFN0YWNrJFB1c2hSZWNvcmSX8+DCTLCH+AIAA0kACGNhbGxlZUlkTAAGY2FsbGVldAATTHZjL2RhdGEvTWV0aG9kUmVmO0wAB3N1bW1hcnl0ABVMdmMvZGF0YS9DYWxsU3VtbWFyeTt4cAAAAANzcgARdmMuZGF0YS5NZXRob2RSZWbJlJTzzU9pGAIAA0wABGF0dHJ0ABdMc2NlbmUvTWV0aG9kQXR0cmlidXRlO0wACmNvbnRyYWN0SWR0ABZMamF2YS9tYXRoL0JpZ0ludGVnZXI7TAAHc2lnSGFzaHQAEExldm0vU2lnaGFzaEludDt4cHNyABxzY2VuZS5NZXRob2RBdHRyaWJ1dGUkQ29tbW9uNHjdebdr9XMCAAB4cgAVc2NlbmUuTWV0aG9kQXR0cmlidXRlcYg2pYWutuUCAAB4cHNyABRqYXZhLm1hdGguQmlnSW50ZWdlcoz8nx+pO/sdAwAGSQAIYml0Q291bnRJAAliaXRMZW5ndGhJABNmaXJzdE5vbnplcm9CeXRlTnVtSQAMbG93ZXN0U2V0Qml0SQAGc2lnbnVtWwAJbWFnbml0dWRldAACW0J4cgAQamF2YS5sYW5nLk51bWJlcoaslR0LlOCLAgAAeHD///////////////7////+AAAAAXVyAAJbQqzzF/gGCFTgAgAAeHAAAAAQzkYEoAAAAAAAAAAAAAAAA3hzcgAOZXZtLlNpZ2hhc2hJbnRUdcqNMXEgeAIAAUwAAW5xAH4ABnhwc3EAfgAM///////////////+/////gAAAAF1cQB+ABAAAAAEGBYN3Xhw"}
		AssignHavocCmd:26 tacCalldatasize!!76:28
		NopCmd
		AssumeExpCmd Apply(add_noofl:bif 0x4 0x0)
		NopCmd
		AssumeExpCmd Eq(0x4 tacCalldatasize!!76:28 )
		LabelCmd:26 "Start procedure ERC20-totalSupply()"
		AnnotationCmd:26 JSON{"key":{"name":"fps.free-pointer-is-scalarized","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true}
		AssignExpCmd:26 R80:25 Select(tacExtcodesize!!0:0 Apply(to_skey:bif R6:29) )
		NopCmd
		AssumeExpCmd Gt(R80:25 0x0 )
		AnnotationCmd:26 JSON{"key":{"name":"internal.func.finder.info","type":"analysis.ip.InternalFunctionFinderReport","erasureStrategy":"Erased"},"value":"rO0ABXNyAChhbmFseXNpcy5pcC5JbnRlcm5hbEZ1bmN0aW9uRmluZGVyUmVwb3J0ian+bYn1VdACAAFMABN1bnJlc29sdmVkRnVuY3Rpb25zdAAPTGphdmEvdXRpbC9TZXQ7eHBzcgAhZGF0YXN0cnVjdHVyZXMuTGlua2VkQXJyYXlIYXNoU2V0AAAAAAAAAAEDAAJGAApsb2FkRmFjdG9yTAAJaGFzaFRhYmxldAAuTGRhdGFzdHJ1Y3R1cmVzL2FycmF5aGFzaHRhYmxlL0FycmF5SGFzaFRhYmxlO3hwdwgAAAAAQAAAAHg="}
		AnnotationCmd:26 JSON{"key":{"name":"fps.free-pointer-is-scalarized","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true}
		NopCmd
		AssumeExpCmd LNot(Lt(tacCalldatasize!!76:28 0x4 ) )
		NopCmd
		AssumeExpCmd Gt(0x70a08231 tacSighash!!9:8 )
		NopCmd
		AssumeExpCmd Gt(0x2e1a7d4d tacSighash!!9:8 )
		NopCmd
		AssumeExpCmd LNot(Eq(0x6fdde03 tacSighash!!9:8 ) )
		NopCmd
		AssumeExpCmd LNot(Eq(0x95ea7b3 tacSighash!!9:8 ) )
		NopCmd
		AssumeExpCmd Eq(0x18160ddd tacSighash!!9:8 )
		AssumeCmd:40 true
		AnnotationCmd:26 JSON{"key":{"name":"internal.func.start","type":"analysis.ip.InternalFuncStartAnnotation","erasureStrategy":"CallTrace"},"value":{"id":2,"startPc":1328,"args":[],"methodSignature":{"#class":"spec.cvlast.QualifiedMethodSignature.QualifiedMethodSig","qualifiedMethodName":{"#class":"spec.cvlast.QualifiedFunction","host":{"name":"ERC20"},"methodId":"totalSupply"},"params":[],"res":[{"#class":"spec.cvlast.VMParam.Unnamed","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256}}]},"stackOffsetToArgPos":{},"callSiteSrc":{"source":0,"begin":3906,"len":364,"jumpType":"ENTER","address":"ce4604a0000000000000000000000003","sourceContext":{"indexToFilepath":{"0":"contracts/ERC20.sol","1":"contracts/IERC20.sol","2":"contracts/IERC20Metadata.sol"},"sourceDir":".post_autofinders.0"}}}}
		AnnotationCmd:26 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet","value":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"CANON46!!4","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.scalarization.sort","type":"vc.data.ScalarizationSort","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.ScalarizationSort.Split","idx":"2"}},{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.storage.bit-width","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":256},{"key":{"name":"tac.storage.pretty.paths","type":"analysis.storage.DisplayPaths","erasureStrategy":"Erased"},"value":{"paths":[{"#class":"analysis.storage.DisplayPath.Root","name":"_totalSupply"}]}},{"key":{"name":"tac.slot.type","type":"spec.cvlast.typedescriptors.EVMTypeDescriptor$EVMValueType","erasureStrategy":"Canonical"},"value":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256}},{"key":{"name":"tac.storage.non-indexed-path","type":"analysis.storage.StorageAnalysisResult$NonIndexedPath","erasureStrategy":"Canonical"},"value":{"#class":"analysis.storage.StorageAnalysisResult.NonIndexedPath.Root","slot":"2"}},{"key":{"name":"tac.storage","type":"java.math.BigInteger","erasureStrategy":"Canonical"},"value":"ce4604a0000000000000000000000003"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1021}]},"displayPath":{"#class":"analysis.storage.DisplayPath.Root","name":"_totalSupply"},"storageType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256},"contractInstance":"ce4604a0000000000000000000000003","linkableStorageReadId":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet.Id","id":2}}}
		AnnotationCmd:26 JSON{"key":{"name":"internal.func.end","type":"analysis.ip.InternalFuncExitAnnotation","erasureStrategy":"Canonical"},"value":{"id":2,"rets":[{"s":{"namePrefix":"CANON46!!4","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.scalarization.sort","type":"vc.data.ScalarizationSort","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.ScalarizationSort.Split","idx":"2"}},{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.storage.bit-width","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":256},{"key":{"name":"tac.storage.pretty.paths","type":"analysis.storage.DisplayPaths","erasureStrategy":"Erased"},"value":{"paths":[{"#class":"analysis.storage.DisplayPath.Root","name":"_totalSupply"}]}},{"key":{"name":"tac.slot.type","type":"spec.cvlast.typedescriptors.EVMTypeDescriptor$EVMValueType","erasureStrategy":"Canonical"},"value":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256}},{"key":{"name":"tac.storage.non-indexed-path","type":"analysis.storage.StorageAnalysisResult$NonIndexedPath","erasureStrategy":"Canonical"},"value":{"#class":"analysis.storage.StorageAnalysisResult.NonIndexedPath.Root","slot":"2"}},{"key":{"name":"tac.storage","type":"java.math.BigInteger","erasureStrategy":"Canonical"},"value":"ce4604a0000000000000000000000003"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1023}]},"offset":0}],"functionLayout":{"0":{"#class":"analysis.ip.InternalFuncValueLocation.Scalar"}}}}
		AnnotationCmd:26 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.EVMFunctionReturnWrite","returnbufOffset":"0","returnValueSym":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"CANON46!!4","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.scalarization.sort","type":"vc.data.ScalarizationSort","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.ScalarizationSort.Split","idx":"2"}},{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.storage.bit-width","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":256},{"key":{"name":"tac.storage.pretty.paths","type":"analysis.storage.DisplayPaths","erasureStrategy":"Erased"},"value":{"paths":[{"#class":"analysis.storage.DisplayPath.Root","name":"_totalSupply"}]}},{"key":{"name":"tac.slot.type","type":"spec.cvlast.typedescriptors.EVMTypeDescriptor$EVMValueType","erasureStrategy":"Canonical"},"value":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256}},{"key":{"name":"tac.storage.non-indexed-path","type":"analysis.storage.StorageAnalysisResult$NonIndexedPath","erasureStrategy":"Canonical"},"value":{"#class":"analysis.storage.StorageAnalysisResult.NonIndexedPath.Root","slot":"2"}},{"key":{"name":"tac.storage","type":"java.math.BigInteger","erasureStrategy":"Canonical"},"value":"ce4604a0000000000000000000000003"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1023}]},"callIndex":3}}
		AnnotationCmd:26 JSON{"key":{"name":"tac.return.path","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		LabelCmd:26 "End procedure ERC20-totalSupply()"
		NopCmd
		AnnotationCmd:26 JSON{"key":{"name":"call.trace.pop","type":"analysis.icfg.Inliner$CallStack$PopRecord","erasureStrategy":"Canonical"},"value":"rO0ABXNyAClhbmFseXNpcy5pY2ZnLklubGluZXIkQ2FsbFN0YWNrJFBvcFJlY29yZPAPfwSLdCWJAgABSQAIY2FsbGVlSWR4cAAAAAM="}
	}
	Block 0_0_0_5_0_0 Succ [5_0_0_0_0_0] {
		AnnotationCmd:26 JSON{"key":{"name":"call.trace.push","type":"analysis.icfg.Inliner$CallStack$PushRecord","erasureStrategy":"Canonical"},"value":"rO0ABXNyACphbmFseXNpcy5pY2ZnLklubGluZXIkQ2FsbFN0YWNrJFB1c2hSZWNvcmSX8+DCTLCH+AIAA0kACGNhbGxlZUlkTAAGY2FsbGVldAATTHZjL2RhdGEvTWV0aG9kUmVmO0wAB3N1bW1hcnl0ABVMdmMvZGF0YS9DYWxsU3VtbWFyeTt4cAAAAAVzcgARdmMuZGF0YS5NZXRob2RSZWbJlJTzzU9pGAIAA0wABGF0dHJ0ABdMc2NlbmUvTWV0aG9kQXR0cmlidXRlO0wACmNvbnRyYWN0SWR0ABZMamF2YS9tYXRoL0JpZ0ludGVnZXI7TAAHc2lnSGFzaHQAEExldm0vU2lnaGFzaEludDt4cHNyABxzY2VuZS5NZXRob2RBdHRyaWJ1dGUkQ29tbW9uNHjdebdr9XMCAAB4cgAVc2NlbmUuTWV0aG9kQXR0cmlidXRlcYg2pYWutuUCAAB4cHNyABRqYXZhLm1hdGguQmlnSW50ZWdlcoz8nx+pO/sdAwAGSQAIYml0Q291bnRJAAliaXRMZW5ndGhJABNmaXJzdE5vbnplcm9CeXRlTnVtSQAMbG93ZXN0U2V0Qml0SQAGc2lnbnVtWwAJbWFnbml0dWRldAACW0J4cgAQamF2YS5sYW5nLk51bWJlcoaslR0LlOCLAgAAeHD///////////////7////+AAAAAXVyAAJbQqzzF/gGCFTgAgAAeHAAAAAQzkYEoAAAAAAAAAAAAAAAA3hzcgAOZXZtLlNpZ2hhc2hJbnRUdcqNMXEgeAIAAUwAAW5xAH4ABnhwc3EAfgAM///////////////+/////gAAAAF1cQB+ABAAAAAEcKCCMXhw"}
		AssignHavocCmd:26 tacCalldatasize!!91:28
		NopCmd
		AssumeExpCmd Apply(add_noofl:bif 0x4 0x20)
		NopCmd
		AssumeExpCmd Apply(add_noofl:bif 0x4 0x0)
		AssignExpCmd:26 B94 LAnd(Ge(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff I248 ) Le(0x0 I248 ) )
		AssertCmd:26 B94 "sanity bounds check on cvl to vm encoding of certoraArg32753276:int failed"
		AssignExpCmd:26 R95 Apply(safe_math_narrow:bif I248)
		NopCmd
		AssumeExpCmd Eq(0x24 tacCalldatasize!!91:28 )
		LabelCmd:26 "Start procedure ERC20-balanceOf(address)"
		AnnotationCmd:26 JSON{"key":{"name":"fps.free-pointer-is-scalarized","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true}
		AssignExpCmd:26 R98:25 Select(tacExtcodesize!!0:0 Apply(to_skey:bif R6:29) )
		NopCmd
		AssumeExpCmd Gt(R98:25 0x0 )
		AnnotationCmd:26 JSON{"key":{"name":"internal.func.finder.info","type":"analysis.ip.InternalFunctionFinderReport","erasureStrategy":"Erased"},"value":"rO0ABXNyAChhbmFseXNpcy5pcC5JbnRlcm5hbEZ1bmN0aW9uRmluZGVyUmVwb3J0ian+bYn1VdACAAFMABN1bnJlc29sdmVkRnVuY3Rpb25zdAAPTGphdmEvdXRpbC9TZXQ7eHBzcgAhZGF0YXN0cnVjdHVyZXMuTGlua2VkQXJyYXlIYXNoU2V0AAAAAAAAAAEDAAJGAApsb2FkRmFjdG9yTAAJaGFzaFRhYmxldAAuTGRhdGFzdHJ1Y3R1cmVzL2FycmF5aGFzaHRhYmxlL0FycmF5SGFzaFRhYmxlO3hwdwgAAAAAQAAAAHg="}
		AnnotationCmd:26 JSON{"key":{"name":"fps.free-pointer-is-scalarized","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true}
		NopCmd
		AssumeExpCmd LNot(Lt(tacCalldatasize!!91:28 0x4 ) )
		NopCmd
		AssumeExpCmd LNot(Gt(0x70a08231 tacSighash!!11:8 ) )
		NopCmd
		AssumeExpCmd Gt(0xa9059cbb tacSighash!!11:8 )
		NopCmd
		AssumeExpCmd Eq(0x70a08231 tacSighash!!11:8 )
		AssumeCmd:30 true
		AssignExpCmd:31 R104:32 Sub(tacCalldatasize!!91:28 0x4 )
		NopCmd
		AssumeExpCmd LNot(Slt(R104:32 0x20 ) )
		NopCmd
		AssumeExpCmd Le(R95 0xffffffffffffffffffffffffffffffffffffffff )
		AnnotationCmd:26 JSON{"key":{"name":"internal.func.start","type":"analysis.ip.InternalFuncStartAnnotation","erasureStrategy":"CallTrace"},"value":{"id":5,"startPc":3130,"args":[{"s":{"namePrefix":"R95","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1013}]},"offset":1,"sort":"SCALAR"}],"methodSignature":{"#class":"spec.cvlast.QualifiedMethodSignature.QualifiedMethodSig","qualifiedMethodName":{"#class":"spec.cvlast.QualifiedFunction","host":{"name":"ERC20"},"methodId":"balanceOf"},"params":[{"#class":"spec.cvlast.VMParam.Named","name":"account","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$address"}}],"res":[{"#class":"spec.cvlast.VMParam.Unnamed","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256}}]},"stackOffsetToArgPos":{"1":0},"callSiteSrc":{"source":0,"begin":4328,"len":511,"jumpType":"ENTER","address":"ce4604a0000000000000000000000003","sourceContext":{"indexToFilepath":{"0":"contracts/ERC20.sol","1":"contracts/IERC20.sol","2":"contracts/IERC20Metadata.sol"},"sourceDir":".post_autofinders.0"}}}}
		AssignExpCmd:33 R110:34 Apply(hash_3_keccak:bif Apply(skey_basic:bif 0x40) Apply(to_skey:bif R95:35) Apply(skey_basic:bif 0x0))
		AssignExpCmd:41 R111:34 Select(CANON31!!3:2 R110:42 )
		AnnotationCmd:26 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet","value":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R111","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1020}]},"displayPath":{"#class":"analysis.storage.DisplayPath.MapAccess","key":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R95","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1018}]},"keyTyp":{"#class":"tac.TACStorageType.IntegralType","typeLabel":"address","numBytes":"14","descriptor":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$address"},"lowerBound":null,"upperBound":null},"base":{"#class":"analysis.storage.DisplayPath.Root","name":"_balances"}},"storageType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256},"contractInstance":"ce4604a0000000000000000000000003","linkableStorageReadId":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet.None"}}}
		AnnotationCmd:26 JSON{"key":{"name":"internal.func.end","type":"analysis.ip.InternalFuncExitAnnotation","erasureStrategy":"Canonical"},"value":{"id":5,"rets":[{"s":{"namePrefix":"R111","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1023}]},"offset":0}],"functionLayout":{"0":{"#class":"analysis.ip.InternalFuncValueLocation.Scalar"}}}}
		AnnotationCmd:26 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.EVMFunctionReturnWrite","returnbufOffset":"0","returnValueSym":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R111","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1023}]},"callIndex":5}}
		AnnotationCmd:26 JSON{"key":{"name":"tac.return.path","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		LabelCmd:26 "End procedure ERC20-balanceOf(address)"
		NopCmd
		AnnotationCmd:26 JSON{"key":{"name":"call.trace.pop","type":"analysis.icfg.Inliner$CallStack$PopRecord","erasureStrategy":"Canonical"},"value":"rO0ABXNyAClhbmFseXNpcy5pY2ZnLklubGluZXIkQ2FsbFN0YWNrJFBvcFJlY29yZPAPfwSLdCWJAgABSQAIY2FsbGVlSWR4cAAAAAU="}
	}
	Block 0_0_0_6_0_0 Succ [6_0_0_0_0_0] {
		AnnotationCmd:26 JSON{"key":{"name":"call.trace.push","type":"analysis.icfg.Inliner$CallStack$PushRecord","erasureStrategy":"Canonical"},"value":"rO0ABXNyACphbmFseXNpcy5pY2ZnLklubGluZXIkQ2FsbFN0YWNrJFB1c2hSZWNvcmSX8+DCTLCH+AIAA0kACGNhbGxlZUlkTAAGY2FsbGVldAATTHZjL2RhdGEvTWV0aG9kUmVmO0wAB3N1bW1hcnl0ABVMdmMvZGF0YS9DYWxsU3VtbWFyeTt4cAAAAAZzcgARdmMuZGF0YS5NZXRob2RSZWbJlJTzzU9pGAIAA0wABGF0dHJ0ABdMc2NlbmUvTWV0aG9kQXR0cmlidXRlO0wACmNvbnRyYWN0SWR0ABZMamF2YS9tYXRoL0JpZ0ludGVnZXI7TAAHc2lnSGFzaHQAEExldm0vU2lnaGFzaEludDt4cHNyABxzY2VuZS5NZXRob2RBdHRyaWJ1dGUkQ29tbW9uNHjdebdr9XMCAAB4cgAVc2NlbmUuTWV0aG9kQXR0cmlidXRlcYg2pYWutuUCAAB4cHNyABRqYXZhLm1hdGguQmlnSW50ZWdlcoz8nx+pO/sdAwAGSQAIYml0Q291bnRJAAliaXRMZW5ndGhJABNmaXJzdE5vbnplcm9CeXRlTnVtSQAMbG93ZXN0U2V0Qml0SQAGc2lnbnVtWwAJbWFnbml0dWRldAACW0J4cgAQamF2YS5sYW5nLk51bWJlcoaslR0LlOCLAgAAeHD///////////////7////+AAAAAXVyAAJbQqzzF/gGCFTgAgAAeHAAAAAQzkYEoAAAAAAAAAAAAAAAA3hzcgAOZXZtLlNpZ2hhc2hJbnRUdcqNMXEgeAIAAUwAAW5xAH4ABnhwc3EAfgAM///////////////+/////gAAAAF1cQB+ABAAAAAEcKCCMXhw"}
		AssignHavocCmd:26 tacCalldatasize!!114:28
		NopCmd
		AssumeExpCmd Apply(add_noofl:bif 0x4 0x20)
		NopCmd
		AssumeExpCmd Apply(add_noofl:bif 0x4 0x0)
		AssignExpCmd:26 B117 LAnd(Ge(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff I208 ) Le(0x0 I208 ) )
		AssertCmd:26 B117 "sanity bounds check on cvl to vm encoding of certoraArg33223323:int failed"
		AssignExpCmd:26 R118 Apply(safe_math_narrow:bif I208)
		NopCmd
		AssumeExpCmd Eq(0x24 tacCalldatasize!!114:28 )
		LabelCmd:26 "Start procedure ERC20-balanceOf(address)"
		AnnotationCmd:26 JSON{"key":{"name":"fps.free-pointer-is-scalarized","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true}
		AssignExpCmd:26 R121:25 Select(tacExtcodesize!!0:0 Apply(to_skey:bif R6:29) )
		NopCmd
		AssumeExpCmd Gt(R121:25 0x0 )
		AnnotationCmd:26 JSON{"key":{"name":"internal.func.finder.info","type":"analysis.ip.InternalFunctionFinderReport","erasureStrategy":"Erased"},"value":"rO0ABXNyAChhbmFseXNpcy5pcC5JbnRlcm5hbEZ1bmN0aW9uRmluZGVyUmVwb3J0ian+bYn1VdACAAFMABN1bnJlc29sdmVkRnVuY3Rpb25zdAAPTGphdmEvdXRpbC9TZXQ7eHBzcgAhZGF0YXN0cnVjdHVyZXMuTGlua2VkQXJyYXlIYXNoU2V0AAAAAAAAAAEDAAJGAApsb2FkRmFjdG9yTAAJaGFzaFRhYmxldAAuTGRhdGFzdHJ1Y3R1cmVzL2FycmF5aGFzaHRhYmxlL0FycmF5SGFzaFRhYmxlO3hwdwgAAAAAQAAAAHg="}
		AnnotationCmd:26 JSON{"key":{"name":"fps.free-pointer-is-scalarized","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true}
		NopCmd
		AssumeExpCmd LNot(Lt(tacCalldatasize!!114:28 0x4 ) )
		NopCmd
		AssumeExpCmd LNot(Gt(0x70a08231 tacSighash!!12:8 ) )
		NopCmd
		AssumeExpCmd Gt(0xa9059cbb tacSighash!!12:8 )
		NopCmd
		AssumeExpCmd Eq(0x70a08231 tacSighash!!12:8 )
		AssumeCmd:30 true
		AssignExpCmd:31 R127:32 Sub(tacCalldatasize!!114:28 0x4 )
		NopCmd
		AssumeExpCmd LNot(Slt(R127:32 0x20 ) )
		NopCmd
		AssumeExpCmd Le(R118 0xffffffffffffffffffffffffffffffffffffffff )
		AnnotationCmd:26 JSON{"key":{"name":"internal.func.start","type":"analysis.ip.InternalFuncStartAnnotation","erasureStrategy":"CallTrace"},"value":{"id":6,"startPc":3130,"args":[{"s":{"namePrefix":"R118","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1013}]},"offset":1,"sort":"SCALAR"}],"methodSignature":{"#class":"spec.cvlast.QualifiedMethodSignature.QualifiedMethodSig","qualifiedMethodName":{"#class":"spec.cvlast.QualifiedFunction","host":{"name":"ERC20"},"methodId":"balanceOf"},"params":[{"#class":"spec.cvlast.VMParam.Named","name":"account","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$address"}}],"res":[{"#class":"spec.cvlast.VMParam.Unnamed","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256}}]},"stackOffsetToArgPos":{"1":0},"callSiteSrc":{"source":0,"begin":4328,"len":511,"jumpType":"ENTER","address":"ce4604a0000000000000000000000003","sourceContext":{"indexToFilepath":{"0":"contracts/ERC20.sol","1":"contracts/IERC20.sol","2":"contracts/IERC20Metadata.sol"},"sourceDir":".post_autofinders.0"}}}}
		AssignExpCmd:33 R133:34 Apply(hash_3_keccak:bif Apply(skey_basic:bif 0x40) Apply(to_skey:bif R118:35) Apply(skey_basic:bif 0x0))
		AssignExpCmd:43 R134:34 Select(CANON31!!3:2 R133:44 )
		AnnotationCmd:26 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet","value":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R134","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1020}]},"displayPath":{"#class":"analysis.storage.DisplayPath.MapAccess","key":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R118","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1018}]},"keyTyp":{"#class":"tac.TACStorageType.IntegralType","typeLabel":"address","numBytes":"14","descriptor":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$address"},"lowerBound":null,"upperBound":null},"base":{"#class":"analysis.storage.DisplayPath.Root","name":"_balances"}},"storageType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256},"contractInstance":"ce4604a0000000000000000000000003","linkableStorageReadId":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet.None"}}}
		AnnotationCmd:26 JSON{"key":{"name":"internal.func.end","type":"analysis.ip.InternalFuncExitAnnotation","erasureStrategy":"Canonical"},"value":{"id":6,"rets":[{"s":{"namePrefix":"R134","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1023}]},"offset":0}],"functionLayout":{"0":{"#class":"analysis.ip.InternalFuncValueLocation.Scalar"}}}}
		AnnotationCmd:26 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.EVMFunctionReturnWrite","returnbufOffset":"0","returnValueSym":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R134","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1023}]},"callIndex":6}}
		AnnotationCmd:26 JSON{"key":{"name":"tac.return.path","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		LabelCmd:26 "End procedure ERC20-balanceOf(address)"
		NopCmd
		AnnotationCmd:26 JSON{"key":{"name":"call.trace.pop","type":"analysis.icfg.Inliner$CallStack$PopRecord","erasureStrategy":"Canonical"},"value":"rO0ABXNyAClhbmFseXNpcy5pY2ZnLklubGluZXIkQ2FsbFN0YWNrJFBvcFJlY29yZPAPfwSLdCWJAgABSQAIY2FsbGVlSWR4cAAAAAY="}
	}
	Block 0_0_0_7_0_0 Succ [7_0_0_0_0_0] {
		AnnotationCmd:26 JSON{"key":{"name":"call.trace.push","type":"analysis.icfg.Inliner$CallStack$PushRecord","erasureStrategy":"Canonical"},"value":"rO0ABXNyACphbmFseXNpcy5pY2ZnLklubGluZXIkQ2FsbFN0YWNrJFB1c2hSZWNvcmSX8+DCTLCH+AIAA0kACGNhbGxlZUlkTAAGY2FsbGVldAATTHZjL2RhdGEvTWV0aG9kUmVmO0wAB3N1bW1hcnl0ABVMdmMvZGF0YS9DYWxsU3VtbWFyeTt4cAAAAAdzcgARdmMuZGF0YS5NZXRob2RSZWbJlJTzzU9pGAIAA0wABGF0dHJ0ABdMc2NlbmUvTWV0aG9kQXR0cmlidXRlO0wACmNvbnRyYWN0SWR0ABZMamF2YS9tYXRoL0JpZ0ludGVnZXI7TAAHc2lnSGFzaHQAEExldm0vU2lnaGFzaEludDt4cHNyABxzY2VuZS5NZXRob2RBdHRyaWJ1dGUkQ29tbW9uNHjdebdr9XMCAAB4cgAVc2NlbmUuTWV0aG9kQXR0cmlidXRlcYg2pYWutuUCAAB4cHNyABRqYXZhLm1hdGguQmlnSW50ZWdlcoz8nx+pO/sdAwAGSQAIYml0Q291bnRJAAliaXRMZW5ndGhJABNmaXJzdE5vbnplcm9CeXRlTnVtSQAMbG93ZXN0U2V0Qml0SQAGc2lnbnVtWwAJbWFnbml0dWRldAACW0J4cgAQamF2YS5sYW5nLk51bWJlcoaslR0LlOCLAgAAeHD///////////////7////+AAAAAXVyAAJbQqzzF/gGCFTgAgAAeHAAAAAQzkYEoAAAAAAAAAAAAAAAA3hzcgAOZXZtLlNpZ2hhc2hJbnRUdcqNMXEgeAIAAUwAAW5xAH4ABnhwc3EAfgAM///////////////+/////gAAAAF1cQB+ABAAAAAEGBYN3Xhw"}
		AssignHavocCmd:26 tacCalldatasize!!137:28
		NopCmd
		AssumeExpCmd Apply(add_noofl:bif 0x4 0x0)
		NopCmd
		AssumeExpCmd Eq(0x4 tacCalldatasize!!137:28 )
		LabelCmd:26 "Start procedure ERC20-totalSupply()"
		AnnotationCmd:26 JSON{"key":{"name":"fps.free-pointer-is-scalarized","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true}
		AssignExpCmd:26 R141:25 Select(tacExtcodesize!!0:0 Apply(to_skey:bif R6:29) )
		NopCmd
		AssumeExpCmd Gt(R141:25 0x0 )
		AnnotationCmd:26 JSON{"key":{"name":"internal.func.finder.info","type":"analysis.ip.InternalFunctionFinderReport","erasureStrategy":"Erased"},"value":"rO0ABXNyAChhbmFseXNpcy5pcC5JbnRlcm5hbEZ1bmN0aW9uRmluZGVyUmVwb3J0ian+bYn1VdACAAFMABN1bnJlc29sdmVkRnVuY3Rpb25zdAAPTGphdmEvdXRpbC9TZXQ7eHBzcgAhZGF0YXN0cnVjdHVyZXMuTGlua2VkQXJyYXlIYXNoU2V0AAAAAAAAAAEDAAJGAApsb2FkRmFjdG9yTAAJaGFzaFRhYmxldAAuTGRhdGFzdHJ1Y3R1cmVzL2FycmF5aGFzaHRhYmxlL0FycmF5SGFzaFRhYmxlO3hwdwgAAAAAQAAAAHg="}
		AnnotationCmd:26 JSON{"key":{"name":"fps.free-pointer-is-scalarized","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true}
		NopCmd
		AssumeExpCmd LNot(Lt(tacCalldatasize!!137:28 0x4 ) )
		NopCmd
		AssumeExpCmd Gt(0x70a08231 tacSighash!!13:8 )
		NopCmd
		AssumeExpCmd Gt(0x2e1a7d4d tacSighash!!13:8 )
		NopCmd
		AssumeExpCmd LNot(Eq(0x6fdde03 tacSighash!!13:8 ) )
		NopCmd
		AssumeExpCmd LNot(Eq(0x95ea7b3 tacSighash!!13:8 ) )
		NopCmd
		AssumeExpCmd Eq(0x18160ddd tacSighash!!13:8 )
		AssumeCmd:40 true
		AnnotationCmd:26 JSON{"key":{"name":"internal.func.start","type":"analysis.ip.InternalFuncStartAnnotation","erasureStrategy":"CallTrace"},"value":{"id":7,"startPc":1328,"args":[],"methodSignature":{"#class":"spec.cvlast.QualifiedMethodSignature.QualifiedMethodSig","qualifiedMethodName":{"#class":"spec.cvlast.QualifiedFunction","host":{"name":"ERC20"},"methodId":"totalSupply"},"params":[],"res":[{"#class":"spec.cvlast.VMParam.Unnamed","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256}}]},"stackOffsetToArgPos":{},"callSiteSrc":{"source":0,"begin":3906,"len":364,"jumpType":"ENTER","address":"ce4604a0000000000000000000000003","sourceContext":{"indexToFilepath":{"0":"contracts/ERC20.sol","1":"contracts/IERC20.sol","2":"contracts/IERC20Metadata.sol"},"sourceDir":".post_autofinders.0"}}}}
		AnnotationCmd:26 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet","value":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"CANON46!!4","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.scalarization.sort","type":"vc.data.ScalarizationSort","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.ScalarizationSort.Split","idx":"2"}},{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.storage.bit-width","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":256},{"key":{"name":"tac.storage.pretty.paths","type":"analysis.storage.DisplayPaths","erasureStrategy":"Erased"},"value":{"paths":[{"#class":"analysis.storage.DisplayPath.Root","name":"_totalSupply"}]}},{"key":{"name":"tac.slot.type","type":"spec.cvlast.typedescriptors.EVMTypeDescriptor$EVMValueType","erasureStrategy":"Canonical"},"value":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256}},{"key":{"name":"tac.storage.non-indexed-path","type":"analysis.storage.StorageAnalysisResult$NonIndexedPath","erasureStrategy":"Canonical"},"value":{"#class":"analysis.storage.StorageAnalysisResult.NonIndexedPath.Root","slot":"2"}},{"key":{"name":"tac.storage","type":"java.math.BigInteger","erasureStrategy":"Canonical"},"value":"ce4604a0000000000000000000000003"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1021}]},"displayPath":{"#class":"analysis.storage.DisplayPath.Root","name":"_totalSupply"},"storageType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256},"contractInstance":"ce4604a0000000000000000000000003","linkableStorageReadId":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet.Id","id":5}}}
		AnnotationCmd:26 JSON{"key":{"name":"internal.func.end","type":"analysis.ip.InternalFuncExitAnnotation","erasureStrategy":"Canonical"},"value":{"id":7,"rets":[{"s":{"namePrefix":"CANON46!!4","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.scalarization.sort","type":"vc.data.ScalarizationSort","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.ScalarizationSort.Split","idx":"2"}},{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.storage.bit-width","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":256},{"key":{"name":"tac.storage.pretty.paths","type":"analysis.storage.DisplayPaths","erasureStrategy":"Erased"},"value":{"paths":[{"#class":"analysis.storage.DisplayPath.Root","name":"_totalSupply"}]}},{"key":{"name":"tac.slot.type","type":"spec.cvlast.typedescriptors.EVMTypeDescriptor$EVMValueType","erasureStrategy":"Canonical"},"value":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256}},{"key":{"name":"tac.storage.non-indexed-path","type":"analysis.storage.StorageAnalysisResult$NonIndexedPath","erasureStrategy":"Canonical"},"value":{"#class":"analysis.storage.StorageAnalysisResult.NonIndexedPath.Root","slot":"2"}},{"key":{"name":"tac.storage","type":"java.math.BigInteger","erasureStrategy":"Canonical"},"value":"ce4604a0000000000000000000000003"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1023}]},"offset":0}],"functionLayout":{"0":{"#class":"analysis.ip.InternalFuncValueLocation.Scalar"}}}}
		AnnotationCmd:26 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.EVMFunctionReturnWrite","returnbufOffset":"0","returnValueSym":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"CANON46!!4","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.scalarization.sort","type":"vc.data.ScalarizationSort","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.ScalarizationSort.Split","idx":"2"}},{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.storage.bit-width","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":256},{"key":{"name":"tac.storage.pretty.paths","type":"analysis.storage.DisplayPaths","erasureStrategy":"Erased"},"value":{"paths":[{"#class":"analysis.storage.DisplayPath.Root","name":"_totalSupply"}]}},{"key":{"name":"tac.slot.type","type":"spec.cvlast.typedescriptors.EVMTypeDescriptor$EVMValueType","erasureStrategy":"Canonical"},"value":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256}},{"key":{"name":"tac.storage.non-indexed-path","type":"analysis.storage.StorageAnalysisResult$NonIndexedPath","erasureStrategy":"Canonical"},"value":{"#class":"analysis.storage.StorageAnalysisResult.NonIndexedPath.Root","slot":"2"}},{"key":{"name":"tac.storage","type":"java.math.BigInteger","erasureStrategy":"Canonical"},"value":"ce4604a0000000000000000000000003"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1023}]},"callIndex":7}}
		AnnotationCmd:26 JSON{"key":{"name":"tac.return.path","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		LabelCmd:26 "End procedure ERC20-totalSupply()"
		NopCmd
		AnnotationCmd:26 JSON{"key":{"name":"call.trace.pop","type":"analysis.icfg.Inliner$CallStack$PopRecord","erasureStrategy":"Canonical"},"value":"rO0ABXNyAClhbmFseXNpcy5pY2ZnLklubGluZXIkQ2FsbFN0YWNrJFBvcFJlY29yZPAPfwSLdCWJAgABSQAIY2FsbGVlSWR4cAAAAAc="}
	}
	Block 1_0_0_0_0_0 Succ [0_0_0_2_0_0] {
		AssumeNotCmd:26 false
		AssumeNotCmd:26 false
		AnnotationCmd JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageGlobalChangeSnippet.StorageTakeSnapshot","lhs":{"namePrefix":"lastStorage","tag":{"#class":"tac.Tag.BlockchainState"},"callIndex":0,"meta":[{"key":{"name":"cvl.local","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true},{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"lastStorage"},{"key":{"name":"cvl.type","type":"spec.cvlast.CVLType$PureCVLType","erasureStrategy":"CallTrace"},"value":{"#class":"spec.cvlast.CVLType.PureCVLType.VMInternal.BlockchainState"}},{"key":{"name":"cvl","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true},{"key":{"name":"cvl.display","type":"java.lang.String","erasureStrategy":"CallTrace"},"value":"lastStorage"}]}}}
		AssignExpCmd:45 I152 CANON8:16
	}
	Block 2_0_0_0_0_0 Succ [0_0_0_3_0_0] {
		AssumeNotCmd:26 false
		AssumeNotCmd:26 false
		AnnotationCmd JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageGlobalChangeSnippet.StorageTakeSnapshot","lhs":{"namePrefix":"lastStorage","tag":{"#class":"tac.Tag.BlockchainState"},"callIndex":0,"meta":[{"key":{"name":"cvl.local","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true},{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"lastStorage"},{"key":{"name":"cvl.type","type":"spec.cvlast.CVLType$PureCVLType","erasureStrategy":"CallTrace"},"value":{"#class":"spec.cvlast.CVLType.PureCVLType.VMInternal.BlockchainState"}},{"key":{"name":"cvl","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true},{"key":{"name":"cvl.display","type":"java.lang.String","erasureStrategy":"CallTrace"},"value":"lastStorage"}]}}}
		AssignExpCmd:46 I153 IntAdd(R50:34 R73:34)
	}
	Block 3_0_0_0_0_0 Succ [0_0_0_4_0_0] {
		AssumeNotCmd:26 false
		AssumeNotCmd:26 false
		AnnotationCmd JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageGlobalChangeSnippet.StorageTakeSnapshot","lhs":{"namePrefix":"lastStorage","tag":{"#class":"tac.Tag.BlockchainState"},"callIndex":0,"meta":[{"key":{"name":"cvl.local","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true},{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"lastStorage"},{"key":{"name":"cvl.type","type":"spec.cvlast.CVLType$PureCVLType","erasureStrategy":"CallTrace"},"value":{"#class":"spec.cvlast.CVLType.PureCVLType.VMInternal.BlockchainState"}},{"key":{"name":"cvl","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true},{"key":{"name":"cvl.display","type":"java.lang.String","erasureStrategy":"CallTrace"},"value":"lastStorage"}]}}}
		AssignExpCmd:47 B155 Le(I153 CANON46!!4:48 )
		AssumeCmd:26 B155
		AnnotationCmd:26 JSON{"key":{"name":"cvl.label.end","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		AnnotationCmd:26 JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Message","s":"check effects of step taken by one of the functions"}}
		NopCmd
		NopCmd
		NopCmd
		NopCmd
		NopCmd
		NopCmd
		NopCmd
		AnnotationCmd:26 JSON{"key":{"name":"call.trace.push","type":"analysis.icfg.Inliner$CallStack$PushRecord","erasureStrategy":"Canonical"},"value":"rO0ABXNyACphbmFseXNpcy5pY2ZnLklubGluZXIkQ2FsbFN0YWNrJFB1c2hSZWNvcmSX8+DCTLCH+AIAA0kACGNhbGxlZUlkTAAGY2FsbGVldAATTHZjL2RhdGEvTWV0aG9kUmVmO0wAB3N1bW1hcnl0ABVMdmMvZGF0YS9DYWxsU3VtbWFyeTt4cAAAAARzcgARdmMuZGF0YS5NZXRob2RSZWbJlJTzzU9pGAIAA0wABGF0dHJ0ABdMc2NlbmUvTWV0aG9kQXR0cmlidXRlO0wACmNvbnRyYWN0SWR0ABZMamF2YS9tYXRoL0JpZ0ludGVnZXI7TAAHc2lnSGFzaHQAEExldm0vU2lnaGFzaEludDt4cHNyABxzY2VuZS5NZXRob2RBdHRyaWJ1dGUkQ29tbW9uNHjdebdr9XMCAAB4cgAVc2NlbmUuTWV0aG9kQXR0cmlidXRlcYg2pYWutuUCAAB4cHNyABRqYXZhLm1hdGguQmlnSW50ZWdlcoz8nx+pO/sdAwAGSQAIYml0Q291bnRJAAliaXRMZW5ndGhJABNmaXJzdE5vbnplcm9CeXRlTnVtSQAMbG93ZXN0U2V0Qml0SQAGc2lnbnVtWwAJbWFnbml0dWRldAACW0J4cgAQamF2YS5sYW5nLk51bWJlcoaslR0LlOCLAgAAeHD///////////////7////+AAAAAXVyAAJbQqzzF/gGCFTgAgAAeHAAAAAQzkYEoAAAAAAAAAAAAAAAA3hzcgAOZXZtLlNpZ2hhc2hJbnRUdcqNMXEgeAIAAUwAAW5xAH4ABnhwc3EAfgAM///////////////+/////gAAAAF1cQB+ABAAAAAEpFfC13hw"}
		NopCmd
		AssumeExpCmd Ge(CANON58:5 0x44 )
		NopCmd
		AssumeExpCmd Ge(0x7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff CANON58:5 )
		AssignExpCmd R166:25 Select(CANON56:4 0x4 )
		AssignExpCmd tacCalldatabufCANON0@4:49 R166:25
		AssignExpCmd R167:25 Select(CANON56:4 0x24 )
		AssignExpCmd tacCalldatabufCANON1@4:50 R167:25
		AssignExpCmd:26 B169 LAnd(Ge(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff CANON9:17 ) Le(0x0 CANON9:17 ) )
		AssertCmd:26 B169 "sanity bounds check on cvl to vm encoding of tacTmp!3130:int failed"
		AssignExpCmd:26 R170:25 Apply(safe_math_narrow:bif CANON9:17)
		NopCmd
		AssumeExpCmd LAnd(Le(R170:51 0xffffffffffffffffffffffffffffffffffffffff ) Ge(R170:51 0x0 ) )
		AssignExpCmd:26 B174 LAnd(Ge(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff CANON10:18 ) Le(0x0 CANON10:18 ) )
		AssertCmd:26 B174 "sanity bounds check on cvl to vm encoding of tacTmp!3133:int failed"
		AssignExpCmd:26 R175:25 Apply(safe_math_narrow:bif CANON10:18)
		NopCmd
		AssumeExpCmd LAnd(Le(R175:52 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff ) Ge(R175:52 0x0 ) )
		AssignExpCmd:26 B180 LAnd(Ge(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff CANON11:19 ) Le(0x0 CANON11:19 ) )
		AssertCmd:26 B180 "sanity bounds check on cvl to vm encoding of tacTmp!3137:int failed"
		AssignExpCmd:26 R181:25 Apply(safe_math_narrow:bif CANON11:19)
		NopCmd
		AssumeExpCmd LAnd(Le(R181:53 0xffffffffffffffffffffffffffffffffffffffff ) Ge(R181:53 0x0 ) )
		AssignExpCmd:26 B185 LAnd(Ge(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff CANON15:23 ) Le(0x0 CANON15:23 ) )
		AssertCmd:26 B185 "sanity bounds check on cvl to vm encoding of tacTmp!3140:int failed"
		AssignExpCmd:26 R186:25 Apply(safe_math_narrow:bif CANON15:23)
		NopCmd
		AssumeExpCmd LAnd(Le(R186:54 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff ) Ge(R186:54 0x0 ) )
		AssignExpCmd:26 B190 LAnd(Ge(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff CANON16:24 ) Le(0x0 CANON16:24 ) )
		AssertCmd:26 B190 "sanity bounds check on cvl to vm encoding of tacTmp!3143:int failed"
		AssignExpCmd:26 R191:25 Apply(safe_math_narrow:bif CANON16:24)
		NopCmd
		AssumeExpCmd LAnd(Le(R191:55 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff ) Ge(R191:55 0x0 ) )
		AssignExpCmd:26 B195 LAnd(Ge(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff CANON10:18 ) Le(0x0 CANON10:18 ) )
		AssertCmd:26 B195 "sanity bounds check on cvl to vm encoding of tacTmp!3146:int failed"
		AssignExpCmd:26 R196:25 Apply(safe_math_narrow:bif CANON10:18)
		AssignExpCmd:26 B198 LAnd(Ge(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff CANON9:17 ) Le(0x0 CANON9:17 ) )
		AssertCmd:26 B198 "sanity bounds check on cvl to vm encoding of tacTmp!3149:int failed"
		AssignExpCmd:26 R199:25 Apply(safe_math_narrow:bif CANON9:17)
		AssignExpCmd:26 R202:25 Select(tacBalance!!2:1 Apply(to_skey:bif R199:25) )
		AssignExpCmd:56 I203:25 IntSub(R202:25 R196:25 )
		AssignExpCmd:56 tacBalance!!204:1 Store(tacBalance!!2:1 Apply(to_skey:bif R199:25) I203:25 )
		AssignExpCmd:26 R205:25 Select(tacBalance!!204:1 Apply(to_skey:bif R6:7) )
		AssignExpCmd:56 R206:25 Add(R205:25 R196:25)
		NopCmd
		AssumeExpCmd Apply(add_noofl:bif R205:25 R196:25)
		AnnotationCmd:26 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.BalanceSnippet","srcAccountInfo":{"old":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R202","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}]},"new":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"I203","tag":{"#class":"tac.Tag.Int"},"callIndex":0,"meta":[{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}]},"addr":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R199","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}]}},"trgAccountInfo":{"old":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R205","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}]},"new":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R206","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}]},"addr":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R6","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"tacContractAt"},{"key":{"name":"tac.contract.sym.addr.name","type":"java.lang.String","erasureStrategy":"Erased"},"value":"ERC20"},{"key":{"name":"tac.contract.sym.addr","type":"java.math.BigInteger","erasureStrategy":"Erased"},"value":"ce4604a0000000000000000000000003"}]}},"transferredAmount":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R196","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}]}}}
		JumpCmd 0_0_0_4_0_0
	}
	Block 5_0_0_0_0_0 Succ [0_0_0_6_0_0] {
		AssumeNotCmd:26 false
		AssumeNotCmd:26 false
		AnnotationCmd JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageGlobalChangeSnippet.StorageTakeSnapshot","lhs":{"namePrefix":"lastStorage","tag":{"#class":"tac.Tag.BlockchainState"},"callIndex":0,"meta":[{"key":{"name":"cvl.local","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true},{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"lastStorage"},{"key":{"name":"cvl.type","type":"spec.cvlast.CVLType$PureCVLType","erasureStrategy":"CallTrace"},"value":{"#class":"spec.cvlast.CVLType.PureCVLType.VMInternal.BlockchainState"}},{"key":{"name":"cvl","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true},{"key":{"name":"cvl.display","type":"java.lang.String","erasureStrategy":"CallTrace"},"value":"lastStorage"}]}}}
		AssignExpCmd:45 I208 CANON8:16
	}
	Block 6_0_0_0_0_0 Succ [0_0_0_7_0_0] {
		AssumeNotCmd:26 false
		AssumeNotCmd:26 false
		AnnotationCmd JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageGlobalChangeSnippet.StorageTakeSnapshot","lhs":{"namePrefix":"lastStorage","tag":{"#class":"tac.Tag.BlockchainState"},"callIndex":0,"meta":[{"key":{"name":"cvl.local","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true},{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"lastStorage"},{"key":{"name":"cvl.type","type":"spec.cvlast.CVLType$PureCVLType","erasureStrategy":"CallTrace"},"value":{"#class":"spec.cvlast.CVLType.PureCVLType.VMInternal.BlockchainState"}},{"key":{"name":"cvl","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true},{"key":{"name":"cvl.display","type":"java.lang.String","erasureStrategy":"CallTrace"},"value":"lastStorage"}]}}}
		AssignExpCmd:57 I209 IntAdd(R111:34 R134:34)
	}
	Block 7_0_0_0_0_0 Succ [] {
		AssumeNotCmd:26 false
		AssumeNotCmd:26 false
		AnnotationCmd JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageGlobalChangeSnippet.StorageTakeSnapshot","lhs":{"namePrefix":"lastStorage","tag":{"#class":"tac.Tag.BlockchainState"},"callIndex":0,"meta":[{"key":{"name":"cvl.local","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true},{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"lastStorage"},{"key":{"name":"cvl.type","type":"spec.cvlast.CVLType$PureCVLType","erasureStrategy":"CallTrace"},"value":{"#class":"spec.cvlast.CVLType.PureCVLType.VMInternal.BlockchainState"}},{"key":{"name":"cvl","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true},{"key":{"name":"cvl.display","type":"java.lang.String","erasureStrategy":"CallTrace"},"value":"lastStorage"}]}}}
		AssignExpCmd:58 B211 Le(I209 CANON46!!4:48 )
		AssertCmd:59 B211 "invariant violated in post-state"
		AnnotationCmd:26 JSON{"key":{"name":"cvl.label.end","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
	}
	Block 0_0_0_4_0_0 Succ [4_0_0_0_0_0] {
		LabelCmd "Start procedure ERC20-decreaseAllowance(address,uint256)"
		AnnotationCmd JSON{"key":{"name":"fps.free-pointer-is-scalarized","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true}
		AssignExpCmd R212:25 Select(tacExtcodesize!!0:0 Apply(to_skey:bif R6:29) )
		NopCmd
		AssumeExpCmd Gt(R212:25 0x0 )
		AnnotationCmd JSON{"key":{"name":"internal.func.finder.info","type":"analysis.ip.InternalFunctionFinderReport","erasureStrategy":"Erased"},"value":"rO0ABXNyAChhbmFseXNpcy5pcC5JbnRlcm5hbEZ1bmN0aW9uRmluZGVyUmVwb3J0ian+bYn1VdACAAFMABN1bnJlc29sdmVkRnVuY3Rpb25zdAAPTGphdmEvdXRpbC9TZXQ7eHBzcgAhZGF0YXN0cnVjdHVyZXMuTGlua2VkQXJyYXlIYXNoU2V0AAAAAAAAAAEDAAJGAApsb2FkRmFjdG9yTAAJaGFzaFRhYmxldAAuTGRhdGFzdHJ1Y3R1cmVzL2FycmF5aGFzaHRhYmxlL0FycmF5SGFzaFRhYmxlO3hwdwgAAAAAQAAAAHg="}
		AnnotationCmd JSON{"key":{"name":"fps.free-pointer-is-scalarized","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true}
		NopCmd
		AssumeExpCmd LNot(Lt(CANON58:5 0x4 ) )
		NopCmd
		AssumeExpCmd LNot(Gt(0x70a08231 tacSighash!!10:8 ) )
		NopCmd
		AssumeExpCmd Gt(0xa9059cbb tacSighash!!10:8 )
		NopCmd
		AssumeExpCmd LNot(Eq(0x70a08231 tacSighash!!10:8 ) )
		NopCmd
		AssumeExpCmd LNot(Eq(0x95d89b41 tacSighash!!10:8 ) )
		NopCmd
		AssumeExpCmd LNot(Eq(0x9dc29fac tacSighash!!10:8 ) )
		NopCmd
		AssumeExpCmd Eq(0xa457c2d7 tacSighash!!10:8 )
		NopCmd
		AssumeExpCmd Eq(R175:52 0x0 )
		AssignExpCmd:60 R222:61 Sub(CANON58:5 0x4 )
		NopCmd
		AssumeExpCmd LNot(Slt(R222:61 0x40 ) )
		AssignExpCmd:62 R224:63 tacCalldatabufCANON0@4:64
		NopCmd
		AssumeExpCmd Le(R166:25 0xffffffffffffffffffffffffffffffffffffffff )
		AssignExpCmd:65 R226:63 tacCalldatabufCANON1@4:66
		AnnotationCmd JSON{"key":{"name":"internal.func.start","type":"analysis.ip.InternalFuncStartAnnotation","erasureStrategy":"CallTrace"},"value":{"id":3,"startPc":4194,"args":[{"s":{"namePrefix":"R224","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1012}]},"offset":1,"sort":"SCALAR"},{"s":{"namePrefix":"R226","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1012}]},"offset":2,"sort":"SCALAR"}],"methodSignature":{"#class":"spec.cvlast.QualifiedMethodSignature.QualifiedMethodSig","qualifiedMethodName":{"#class":"spec.cvlast.QualifiedFunction","host":{"name":"ERC20"},"methodId":"decreaseAllowance"},"params":[{"#class":"spec.cvlast.VMParam.Named","name":"spender","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$address"}},{"#class":"spec.cvlast.VMParam.Named","name":"subtractedValue","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256}}],"res":[{"#class":"spec.cvlast.VMParam.Unnamed","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$bool"}}]},"stackOffsetToArgPos":{"1":0,"2":1},"callSiteSrc":{"source":0,"begin":9689,"len":813,"jumpType":"ENTER","address":"ce4604a0000000000000000000000003","sourceContext":{"indexToFilepath":{"0":"contracts/ERC20.sol","1":"contracts/IERC20.sol","2":"contracts/IERC20Metadata.sol"},"sourceDir":".post_autofinders.0"}}}}
		AssignExpCmd:67 R229:68 Apply(hash_3_keccak:bif Apply(skey_basic:bif 0x40) Apply(to_skey:bif R170:69) Apply(skey_basic:bif 0x1))
		AssignExpCmd R230:61 tacCalldatabufCANON0@4:64
		NopCmd
		AssignExpCmd:70 R233:68 Apply(hash_3_keccak:bif Apply(skey_basic:bif 0x40) Apply(to_skey:bif R166:25) R229:71)
		AssignExpCmd:72 R234:68 Select(CANON92!!5:6 R233:73 )
		AnnotationCmd JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet","value":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R234","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1018}]},"displayPath":{"#class":"analysis.storage.DisplayPath.MapAccess","key":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R230","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1016}]},"keyTyp":{"#class":"tac.TACStorageType.IntegralType","typeLabel":"address","numBytes":"14","descriptor":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$address"},"lowerBound":null,"upperBound":null},"base":{"#class":"analysis.storage.DisplayPath.MapAccess","key":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R170","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.env.known-bit-width","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":160},{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1016}]},"keyTyp":{"#class":"tac.TACStorageType.IntegralType","typeLabel":"address","numBytes":"14","descriptor":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$address"},"lowerBound":null,"upperBound":null},"base":{"#class":"analysis.storage.DisplayPath.Root","name":"_allowances"}}},"storageType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256},"contractInstance":"ce4604a0000000000000000000000003","linkableStorageReadId":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet.None"}}}
		NopCmd
		AssumeExpCmd LNot(Lt(R234:68 R167:25 ) )
		AssignExpCmd:74 R237:75 Sub(R234:68 R167:25 )
		AnnotationCmd JSON{"key":{"name":"internal.func.start","type":"analysis.ip.InternalFuncStartAnnotation","erasureStrategy":"CallTrace"},"value":{"id":4,"startPc":5140,"args":[{"s":{"namePrefix":"R170","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.env.known-bit-width","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":160},{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1017}]},"offset":1,"sort":"SCALAR"},{"s":{"namePrefix":"R224","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1012}]},"offset":2,"sort":"SCALAR"},{"s":{"namePrefix":"R237","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1015}]},"offset":3,"sort":"SCALAR"}],"methodSignature":{"#class":"spec.cvlast.QualifiedMethodSignature.QualifiedMethodSig","qualifiedMethodName":{"#class":"spec.cvlast.QualifiedFunction","host":{"name":"ERC20"},"methodId":"_approve"},"params":[{"#class":"spec.cvlast.VMParam.Named","name":"owner","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$address"}},{"#class":"spec.cvlast.VMParam.Named","name":"spender","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$address"}},{"#class":"spec.cvlast.VMParam.Named","name":"amount","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256}}],"res":[]},"stackOffsetToArgPos":{"1":0,"2":1,"3":2},"callSiteSrc":{"source":0,"begin":10398,"len":65,"jumpType":"ENTER","address":"ce4604a0000000000000000000000003","sourceContext":{"indexToFilepath":{"0":"contracts/ERC20.sol","1":"contracts/IERC20.sol","2":"contracts/IERC20Metadata.sol"},"sourceDir":".post_autofinders.0"}}}}
		NopCmd
		AssumeExpCmd LNot(Eq(R170:51 0x0 ) )
		NopCmd
		NopCmd
		AssumeExpCmd LNot(Eq(R166:25 0x0 ) )
		AssignExpCmd R244:76 tacCalldatabufCANON0@4:64
		AnnotationCmd JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.StoreSnippet","value":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R237","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1015}]},"displayPath":{"#class":"analysis.storage.DisplayPath.MapAccess","key":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R244","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1011}]},"keyTyp":{"#class":"tac.TACStorageType.IntegralType","typeLabel":"address","numBytes":"14","descriptor":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$address"},"lowerBound":null,"upperBound":null},"base":{"#class":"analysis.storage.DisplayPath.MapAccess","key":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R170","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.env.known-bit-width","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":160},{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1011}]},"keyTyp":{"#class":"tac.TACStorageType.IntegralType","typeLabel":"address","numBytes":"14","descriptor":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$address"},"lowerBound":null,"upperBound":null},"base":{"#class":"analysis.storage.DisplayPath.Root","name":"_allowances"}}},"storageType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256},"contractInstance":"ce4604a0000000000000000000000003"}}
		AnnotationCmd JSON{"key":{"name":"internal.func.end","type":"analysis.ip.InternalFuncExitAnnotation","erasureStrategy":"Canonical"},"value":{"id":4,"rets":[],"functionLayout":{}}}
		AssignExpCmd R247:77 0x1
		AnnotationCmd JSON{"key":{"name":"internal.func.end","type":"analysis.ip.InternalFuncExitAnnotation","erasureStrategy":"Canonical"},"value":{"id":3,"rets":[{"s":{"namePrefix":"R247","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1023}]},"offset":0}],"functionLayout":{"0":{"#class":"analysis.ip.InternalFuncValueLocation.Scalar"}}}}
		AnnotationCmd JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.EVMFunctionReturnWrite","returnbufOffset":"0","returnValueSym":{"#class":"vc.data.TACSymbol.Const","value":"1","tag":{"#class":"tac.Tag.Bool"}},"callIndex":4}}
		AnnotationCmd JSON{"key":{"name":"tac.return.path","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		LabelCmd "End procedure ERC20-decreaseAllowance(address,uint256)"
		JumpCmd 4_0_0_0_0_0
	}
	Block 4_0_0_0_0_0 Succ [0_0_0_5_0_0] {
		AnnotationCmd:26 JSON{"key":{"name":"call.trace.pop","type":"analysis.icfg.Inliner$CallStack$PopRecord","erasureStrategy":"Canonical"},"value":"rO0ABXNyAClhbmFseXNpcy5pY2ZnLklubGluZXIkQ2FsbFN0YWNrJFBvcFJlY29yZPAPfwSLdCWJAgABSQAIY2FsbGVlSWR4cAAAAAQ="}
		AssumeNotCmd:26 false
		AssumeNotCmd:26 false
		AnnotationCmd JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageGlobalChangeSnippet.StorageTakeSnapshot","lhs":{"namePrefix":"lastStorage","tag":{"#class":"tac.Tag.BlockchainState"},"callIndex":0,"meta":[{"key":{"name":"cvl.local","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true},{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"lastStorage"},{"key":{"name":"cvl.type","type":"spec.cvlast.CVLType$PureCVLType","erasureStrategy":"CallTrace"},"value":{"#class":"spec.cvlast.CVLType.PureCVLType.VMInternal.BlockchainState"}},{"key":{"name":"cvl","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true},{"key":{"name":"cvl.display","type":"java.lang.String","erasureStrategy":"CallTrace"},"value":"lastStorage"}]}}}
		AnnotationCmd:26 JSON{"key":{"name":"cvl.label.end","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		AnnotationCmd:26 JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Message","s":"assert invariant in post-state"}}
		AssignExpCmd:27 I248 CANON6:15
	}
}
Axioms {
		CANON123
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
  "16": [
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
  "24": [
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
      "value": 1017
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
      "value": 1020
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
  "37": [
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
              "namePrefix": "R34",
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
                "namePrefix": "R34",
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
              "namePrefix": "R95",
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
                "namePrefix": "R95",
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
  "44": [
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
              "namePrefix": "R118",
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
                "namePrefix": "R118",
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
  "45": [
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
            "namePrefix": "I52",
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
            "namePrefix": "I75",
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
            "namePrefix": "I153",
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
            "namePrefix": "I90",
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
  "48": [
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
  "50": [
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
  "51": [
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
  "52": [
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
  "53": [
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
  "54": [
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
  "55": [
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
  "56": [
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
            "namePrefix": "I113",
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
            "namePrefix": "I136",
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
            "namePrefix": "I209",
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
            "namePrefix": "I151",
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
  "59": [
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
  "60": [
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
      "value": 1016
    }
  ],
  "62": [
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
  "63": [
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
  "64": [
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
  "65": [
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
  "66": [
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
  "67": [
    {
      "key": {
        "name": "tac.meta",
        "type": "vc.data.TACMetaInfo",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "source": 0,
        "begin": 10203,
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
      "value": 1018
    }
  ],
  "69": [
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
  "70": [
    {
      "key": {
        "name": "tac.meta",
        "type": "vc.data.TACMetaInfo",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "source": 0,
        "begin": 10203,
        "len": 32,
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
      "value": "tacM0x20"
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
  "72": [
    {
      "key": {
        "name": "tac.meta",
        "type": "vc.data.TACMetaInfo",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "source": 0,
        "begin": 10203,
        "len": 32,
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
              "namePrefix": "R230",
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
                  "value": 1016
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
                "namePrefix": "R170",
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
                    "value": 1016
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
                    "namePrefix": "R170",
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
                        "value": 1016
                      }
                    ]
                  },
                  "baseSlot": {
                    "#class": "vc.data.TACSymbol.Var.Full",
                    "namePrefix": "CANON94",
                    "tag": {
                      "#class": "tac.Tag.Bit256"
                    },
                    "callIndex": 4,
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
                    "callIndex": 4,
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
                "namePrefix": "R230",
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
                    "value": 1016
                  }
                ]
              },
              "baseSlot": {
                "#class": "vc.data.TACSymbol.Var.Full",
                "namePrefix": "CANON96",
                "tag": {
                  "#class": "tac.Tag.Bit256"
                },
                "callIndex": 4,
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
                "namePrefix": "CANON95",
                "tag": {
                  "#class": "tac.Tag.Bit256"
                },
                "callIndex": 4,
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
      "value": 1018
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
        "begin": 10428,
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
        "name": "optimization.overflow.safe",
        "type": "tac.MetaMap$Companion$NothingValue",
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
      "value": 1015
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
      "value": 1023
    }
  ]
}