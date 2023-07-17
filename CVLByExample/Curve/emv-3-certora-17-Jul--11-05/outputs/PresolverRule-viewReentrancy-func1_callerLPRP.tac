TACSymbolTable {
	UserDefined {
		UninterpSort skey
	}
	BuiltinFunctions {
		to_skey:JSON{"#class":"vc.data.TACBuiltInFunction.Hash.ToSkey"}
		safe_math_narrow:JSON{"#class":"vc.data.TACBuiltInFunction.SafeMathNarrow"}
		add_noofl:JSON{"#class":"vc.data.TACBuiltInFunction.NoAddOverflowCheck"}
		skey_basic:JSON{"#class":"vc.data.TACBuiltInFunction.Hash.Basic"}
		hash_3_keccak:JSON{"#class":"vc.data.TACBuiltInFunction.Hash.SimpleHashApplication","arity":3,"hashFamily":{"#class":"vc.data.HashFamily.Keccack"}}
		safe_math_promotion:JSON{"#class":"vc.data.TACBuiltInFunction.SafeMathPromotion"}
		mul_noofl:JSON{"#class":"vc.data.TACBuiltInFunction.NoMulOverflowCheck"}
	}
	UninterpretedFunctions {
	}
	tacM0x40@1:bv256
	tacNonce:wordmap
	tacCaller@1:bv256
	tacMCANON2!!123:bytemap
	tacMCANON2!!125:bytemap
	tacMCANON2!!150:bytemap
	tacMCANON2!!184:bytemap
	tacMCANON2!!198:bytemap
	tacMCANON2!!205:bytemap
	tacMCANON2!!207:bytemap
	tacMCANON2!!209:bytemap
	tacMCANON2!!211:bytemap
	tacMCANON2!!237:bytemap
	tacCalldatabufCANON0@2:bv256
	tacCalldatabufCANON0@4:bv256
	tacCalldatabufCANON1@2:bv256
	tacMCANON1!!4:bytemap
	tacMCANON2!!5:bytemap
	tacMCANON3!!6:bytemap
	tacOrigNonceCANON0:wordmap
	tacOrigNonceCANON1:wordmap
	CANON85!!13:wordmap
	tacAddress!!72:bv256
	tacCallvalue@1:bv256
	lastReverted:bool
	lastReverted@1:bool
	lastReverted@2:bool
	lastReverted@3:bool
	lastReverted@4:bool
	tacM0x0!!145:bv256
	tacExtcodesize!!3:wordmap
	CANON26!!9:bv256
	tacCalldatasize@1:bv256
	tacCalldatasize@2:bv256
	tacCalldatasize@3:bv256
	tacCalldatasize@4:bv256
	tacReturndata@1:bytemap
	tacReturnsize@1:bv256
	tacMCANON3!!170:bytemap
	tacMCANON3!!172:bytemap
	tacCallvalue!!70:bv256
	CANON94!!14:bv256
	tacM0x0@2:bv256
	tacRC@1:bv256
	tacExtcodesize:wordmap
	CANON100:bool
	CANON101:bool
	CANON104@1:bv256
	CANON104@2:bv256
	CANON104@3:bv256
	CANON104@4:bv256
	CANON105@1:bv256
	CANON106@1:bv256
	CANON107:bool
	CANON108:bool
	CANON109:bool
	CANON110:bool
	CANON111:bool
	CANON112:bool
	CANON113:int
	CANON114:int
	CANON115:int
	CANON116@1:bool
	CANON117@1:bool
	CANON118@1:bool
	CANON119@1:bv256
	CANON120:bool
	CANON121:int
	CANON122:int
	CANON123:int
	CANON124@1:bool
	tacCalldatasize!!57:bv256
	tacMCANON0@1:bytemap
	tacMCANON1@1:bytemap
	tacMCANON2@1:bytemap
	tacMCANON3@3:bytemap
	tacMCANON0havocme21883@1:bytemap
	tacBalance:wordmap
	tacBalance!!98:wordmap
	tacNumber@1:bv256
	tacBalance!!7:wordmap
	tacCalldatabuf@1:bytemap
	tacCalldatabuf@3:bytemap
	B22:bool
	B23:bool
	B24:bool
	B25:bool
	B26:bool
	B27:bool
	B28:bool
	B29:bool
	B30:bool
	B31:bool
	B32:bool
	B33:bool
	B34:bool
	B35:bool
	B36:bool
	B37:bool
	B38:bool
	B40:bool
	B42:bool
	B44:bool
	B45:bool
	B46:bool
	B47:bool
	B48:bool
	B49:bool
	B60:bool
	B61:bool
	B63:bool
	B66:bool
	B68:bool
	B71:bool
	B74:bool
	B77:bool
	B79:bool
	B82:bool
	B84:bool
	B87:bool
	B89:bool
	B92:bool
	I50:int
	I51:int
	I52:int
	I53:int
	I54:int
	I62:int
	I67:int
	I73:int
	I78:int
	I83:int
	I88:int
	I91:int
	I97:int
	M55:bytemap
	M58:bytemap
	R15:bv256
	R16:bv256
	R17:bv256
	R39:bv256
	R41:bv256
	R43:bv256
	R56:bv256
	R59:bv256
	R64:bv256
	R69:bv256
	R75:bv256
	R80:bv256
	R85:bv256
	R90:bv256
	R93:bv256
	R94:bv256
	R95:bv256
	R96:bv256
	R99:bv256
	B101:bool
	B104:bool
	B105:bool
	B106:bool
	B107:bool
	B108:bool
	B109:bool
	B110:bool
	B114:bool
	B119:bool
	B120:bool
	B121:bool
	B130:bool
	B131:bool
	B133:bool
	B134:bool
	B135:bool
	B136:bool
	B137:bool
	B139:bool
	B140:bool
	B142:bool
	B143:bool
	B152:bool
	B153:bool
	B156:bool
	B157:bool
	B158:bool
	B159:bool
	B162:bool
	B163:bool
	B164:bool
	B165:bool
	B167:bool
	B168:bool
	B177:bool
	B186:bool
	B187:bool
	B189:bool
	B190:bool
	B191:bool
	B192:bool
	B193:bool
	B194:bool
	B200:bool
	B218:bool
	B220:bool
	B221:bool
	B223:bool
	B227:bool
	B233:bool
	B234:bool
	B235:bool
	I178:int
	I179:int
	I180:int
	I224:int
	I225:int
	R100:bv256
	R103:bv256
	R111:bv256
	R112:bv256
	R113:bv256
	R115:bv256
	R117:bv256
	R118:bv256
	R122:bv256
	R124:bv256
	R126:bv256
	R127:bv256
	R132:bv256
	R138:bv256
	R141:bv256
	R144:bv256
	R146:(uninterp) skey
	R147:bv256
	R148:bv256
	R155:bv256
	R160:bv256
	R161:bv256
	R166:bv256
	R169:bv256
	R171:bv256
	R173:bv256
	R174:bv256
	R175:bv256
	R176:bv256
	R181:bv256
	R182:bv256
	R188:bv256
	R195:bv256
	R196:bv256
	R199:bv256
	R201:bv256
	R203:bv256
	R204:bv256
	R206:bv256
	R208:bv256
	R210:bv256
	R212:bv256
	R213:bv256
	R214:bv256
	R216:bv256
	R217:bv256
	R219:bv256
	R222:bv256
	R226:bv256
	R228:bv256
	R229:bv256
	R230:bv256
	R231:bv256
	R232:bv256
	R236:bv256
	R238:bv256
	R239:bv256
	tacOrigSCANON0:wordmap
	tacOrigSCANON1:wordmap
	tacOrigSCANON2:bv256
	tacOrigSCANON3:bv256
	tacOrigSCANON4:bv256
	tacOrigSCANON5:wordmap
	tacOrigSCANON6:wordmap
	tacOrigSCANON7:wordmap
	tacOrigSCANON8:wordmap
	tacOrigSCANON9:wordmap
	tacAddress@1:bv256
	tacAddress@2:bv256
	tacAddress@3:bv256
	tacAddress@4:bv256
	tacOrigBalanceCANON0:wordmap
	tacOrigBalanceCANON1:wordmap
	LCANON0@1:bv256
	LCANON0@2:bv256
	LCANON0@3:bv256
	LCANON0@4:bv256
	LCANON1@1:bool
	LCANON2@1:bool
	LCANON2@2:bool
	LCANON2@3:bool
	LCANON2@4:bool
	LCANON3@1:bool
	LCANON3@2:bool
	LCANON3@3:bool
	LCANON3@4:bool
	LCANON4@1:bool
	LCANON4@3:bool
	LCANON5@1:bool
	LCANON6@1:bool
	LCANON6@4:bool
	LCANON7@1:bv256
	LCANON8@1:bv256
	LCANON9@1:bv256
	tacOrigin@1:bv256
	tacCalldatabuf!!8@3:bytemap
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
	CANON20:bv256
	CANON21:bool
	CANON22:bv256
	CANON23:bool
	CANON24:bool
	CANON25:bool
	CANON26:bv256
	CANON27:bv256
	CANON28:int
	CANON29:int
	CANON30:int
	CANON31:int
	CANON32:int
	CANON33:bytemap
	CANON34:bytemap
	CANON35:bv256
	CANON36:bv256
	CANON37:bytemap
	CANON39:bv256
	CANON40:bool
	CANON41:bool
	CANON42:int
	CANON43:bool
	CANON44:bv256
	CANON45:int
	CANON46:bool
	CANON47:bv256
	CANON48:int
	CANON49:bool
	CANON50:bv256
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
	CANON63:bv256
	CANON64:bv256
	CANON65:bv256
	CANON66:int
	CANON67:bv256
	CANON68:bv256
	CANON69:bool
	CANON70@1:bv256
	CANON70@2:bv256
	CANON70@3:bv256
	CANON70@4:bv256
	CANON71@1:bool
	CANON71@2:bool
	CANON71@3:bool
	CANON71@4:bool
	CANON72:wordmap
	CANON73@1:bool
	CANON74@1:bool
	CANON75@1:bool
	CANON76@1:bv256
	CANON77@1:bv256
	CANON78:wordmap
	CANON79:bv256
	CANON80:bv256
	CANON81:bv256
	CANON82:wordmap
	CANON83:wordmap
	CANON84:wordmap
	CANON85:wordmap
	CANON86:wordmap
	CANON87:wordmap
	CANON88:bv256
	CANON89:bv256
	CANON90:bv256
	CANON91:wordmap
	CANON92:bv256
	CANON93:bv256
	CANON94:bv256
	CANON95:bv256
	CANON96:bv256
	CANON97:bv256
	CANON98:bv256
	CANON99@1:bool
	LCANON10@1:bv256
	LCANON11@1:bv256
	LCANON12@1:bool
	LCANON13@1:bv256
	LCANON14@1:bv256
	LCANON15@1:bv256
	LCANON16@1:bv256
	LCANON17@1:bv256
	LCANON18@1:bv256
	LCANON19@1:bv256
	LCANON20@1:bv256
	LCANON21@2:bool
	LCANON22@2:bool
	LCANON23@2:bv256
	LCANON24@2:bool
	LCANON25@2:bv256
	LCANON26@2:bool
	LCANON27@2:bv256
	LCANON27@4:bv256
	LCANON28@2:bv256
	LCANON29@2:bv256
	LCANON30@2:bv256
	LCANON31@1:bool
	LCANON32@1:bv256
	LCANON33@1:bv256
	LCANON34@1:bv256
	LCANON35@1:bool
	LCANON36@1:bv256
	LCANON37@1:bool
	LCANON38@1:bv256
	LCANON39@1:bv256
	LCANON40@1:bv256
	LCANON41@1:bv256
	LCANON42@1:bv256
	LCANON43@1:bv256
	LCANON44@1:bv256
	LCANON45@1:bv256
	LCANON46@1:bv256
	LCANON47@1:bv256
	LCANON48@1:bv256
	LCANON49@3:bv256
	LCANON50@3:bv256
	LCANON51@3:bool
	LCANON52@3:bool
	LCANON53@3:bv256
	LCANON54@3:bool
	LCANON55@3:bv256
	LCANON56@3:bool
	LCANON57@3:bool
	LCANON58@3:bv256
	LCANON59@3:bv256
	LCANON60@3:bv256
	LCANON61@3:bv256
	LCANON62@3:bv256
	LCANON63@3:bool
	LCANON64@3:bv256
	LCANON65@3:bv256
	LCANON66@1:bool
	LCANON67@1:bv256
	LCANON68@1:bv256
	LCANON69@1:bv256
	LCANON70@1:bv256
	LCANON71@1:bool
	LCANON72@1:bv256
	LCANON73@1:bv256
	LCANON74@1:bv256
	LCANON75@1:bv256
	LCANON76@1:bv256
	LCANON77@1:bv256
	LCANON78@1:bv256
	LCANON79@4:bool
	LCANON80@4:bool
	LCANON81@4:bv256
	LCANON82@1:bv256
	LCANON83@1:bv256
	LCANON84@1:bv256
	LCANON85@1:bv256
	LCANON86@1:bool
	LCANON87@1:bv256
	LCANON88@1:bool
	LCANON89@1:bool
	LCANON90@1:bv256
	LCANON91@1:bv256
	LCANON92@1:bool
	LCANON93@1:bv256
	LCANON94@1:bv256
	LCANON95@1:bv256
	LCANON96@1:bv256
	tacContractAtCANON0:bv256
	tacContractAtCANON1:bv256
	tacContractAtCANON2:bv256
	lastHasThrown:bool
	lastHasThrown@1:bool
	lastHasThrown@2:bool
	lastHasThrown@3:bool
	lastHasThrown@4:bool
	tacOrigSCANON10:wordmap
	tacOrigSCANON11:wordmap
	tacOrigSCANON12:bv256
	tacOrigSCANON13:bv256
	tacOrigSCANON14:bv256
	tacOrigSCANON15:wordmap
	tacOrigSCANON16:wordmap
	tacOrigSCANON17:wordmap
	tacOrigSCANON18:bv256
	tacOrigSCANON19:bv256
	tacOrigSCANON20:bv256
	tacOrigSCANON21:bv256
	tacOrigSCANON22:bv256
	tacOrigSCANON23:bv256
	tacOrigSCANON24:bv256
	tacOrigSCANON25:bv256
	tacOrigSCANON26:bv256
	tacOrigSCANON27:wordmap
	tacOrigSCANON28:wordmap
	tacOrigSCANON29:bv256
	tacOrigSCANON30:bv256
	tacOrigSCANON31:bv256
	tacOrigSCANON32:wordmap
	tacOrigSCANON33:wordmap
	tacOrigSCANON34:wordmap
	tacOrigSCANON35:wordmap
	tacOrigSCANON36:wordmap
	tacOrigSCANON37:wordmap
	tacOrigSCANON38:wordmap
	tacOrigSCANON39:bv256
	tacOrigSCANON40:bv256
	tacOrigSCANON41:bv256
	tacOrigSCANON42:wordmap
	tacOrigSCANON43:wordmap
	tacOrigSCANON44:wordmap
	tacOrigSCANON45:bv256
	tacOrigSCANON46:bv256
	tacOrigSCANON47:bv256
	tacOrigSCANON48:bv256
	tacOrigSCANON49:bv256
	tacOrigSCANON50:bv256
	tacOrigSCANON51:bv256
	tacOrigSCANON52:bv256
	tacOrigSCANON53:bv256
	tacCaller!!65:bv256
	tacNumber!!81:bv256
	tacAddress!!129:bv256
	tacAddress!!151:bv256
	tacAddress!!185:bv256
	tacReturndata!!128:bytemap
	tacReturndata!!149:bytemap
	tacReturndata!!183:bytemap
	tacReturndata!!197:bytemap
	tacReturndata!!215:bytemap
	tacReturndata!!240:bytemap
	tacTimestamp!!86:bv256
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
	tacCalldatabuf!!154@3:bytemap
	tacSCANON0:wordmap
	tacSCANON1:wordmap
	tacSCANON2:wordmap
	tacCalldatasize!!0:bv256
	tacCalldatasize!!1:bv256
	tacCalldatasize!!2:bv256
	tacMCANON1!!116:bytemap
	tacMCANON1!!202:bytemap
	CANON72!!11:wordmap
	CANON27!!10:bv256
	tacBalance!!102:wordmap
	CANON79!!12:bv256
	tacTimestamp@1:bv256
	tacSighash!!18:bv256
	tacSighash!!19:bv256
	tacSighash!!20:bv256
	tacSighash!!21:bv256
	tacSighash@1:bv256
	tacSighash@2:bv256
	tacSighash@3:bv256
	tacSighash@4:bv256
	tacOrigin!!76:bv256
}
Program {
	Block 0_0_0_0_0_0 Succ [0_0_0_1_0_0] {
		AssignHavocCmd tacCalldatabufCANON0@2:0
		AssignHavocCmd tacCalldatabufCANON0@4:0
		AssignHavocCmd tacCalldatasize!!0:1
		AssignHavocCmd tacCalldatasize!!1:1
		AssignHavocCmd tacCalldatasize!!2:1
		AssignHavocCmd tacExtcodesize!!3:2
		AssignExpCmd tacMCANON1!!4:3 ByteMapDefinition(i.21885:bv256 -> 0x0 )
		AssignExpCmd tacMCANON2!!5:4 ByteMapDefinition(i.21886:bv256 -> 0x0 )
		AssignExpCmd tacMCANON3!!6:5 ByteMapDefinition(i.21887:bv256 -> 0x0 )
		AssignHavocCmd tacBalance!!7:6
		AssignExpCmd tacCalldatabuf!!8@3:7 ByteMapDefinition(i.21888:bv256 -> Ite(Lt(i.21888 tacCalldatasize!!1:1 ) Unconstrained(bv256) 0x0 ) )
		AssignHavocCmd CANON26!!9:8
		AssignHavocCmd CANON27!!10:9
		AssignHavocCmd CANON34:10
		AssignHavocCmd CANON36:11
		AssignHavocCmd CANON72!!11:12
		AssignHavocCmd CANON79!!12:13
		AssignHavocCmd CANON85!!13:14
		AssignHavocCmd CANON94!!14:15
		AssignHavocCmd R15:16
		AssignHavocCmd R16:17
		AssignHavocCmd R17:18
		AssignHavocCmd tacSighash!!18:19
		AssignHavocCmd tacSighash!!19:19
		AssignHavocCmd tacSighash!!20:19
		AssignHavocCmd tacSighash!!21:19
		AssignExpCmd CANON0:20 0x421b78d9
		AnnotationCmd JSON{"key":{"name":"PlaceholderData","type":"rules.genericrulecheckers.helpers.InstrumentationPlaceholderCommandsManager$Companion$PlaceholderData","erasureStrategy":"Canonical"},"value":{"index":0,"loc":{"#class":"rules.genericrulecheckers.helpers.InstrumentationPlaceholderCommandsManager.PlaceholdersLocation.After","ptr":{"block":{"#class":"tac.BlockIdentifier","origStartPc":0,"stkTop":0,"decompCopy":0,"calleeIdx":0,"topOfStackValue":0,"freshCopy":0},"pos":0},"amount":2},"managerId":2}}
		AnnotationCmd JSON{"key":{"name":"PlaceholderData","type":"rules.genericrulecheckers.helpers.InstrumentationPlaceholderCommandsManager$Companion$PlaceholderData","erasureStrategy":"Canonical"},"value":{"index":1,"loc":{"#class":"rules.genericrulecheckers.helpers.InstrumentationPlaceholderCommandsManager.PlaceholdersLocation.After","ptr":{"block":{"#class":"tac.BlockIdentifier","origStartPc":0,"stkTop":0,"decompCopy":0,"calleeIdx":0,"topOfStackValue":0,"freshCopy":0},"pos":0},"amount":2},"managerId":2}}
		AssignExpCmd CANON1:21 false
		AssignExpCmd CANON2:22 false
		AssignExpCmd CANON3:23 false
		AssignExpCmd CANON4:24 0x0
		AssignExpCmd CANON5:25 false
		AnnotationCmd JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Message","s":"Setup"}}
		AnnotationCmd JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Message","s":"multi contract setup"}}
		AnnotationCmd JSON{"key":{"name":"cvl.label.end","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		AnnotationCmd JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Message","s":"rule parameters setup"}}
		AssumeCmd true
		AssumeCmd true
		AssignHavocCmd CANON7:26
		AssignHavocCmd CANON8:27
		AssignHavocCmd CANON9:28
		AssignHavocCmd CANON10:29
		AssignHavocCmd CANON11:30
		AssignHavocCmd CANON12:31
		AssignHavocCmd CANON13:32
		AssignHavocCmd CANON14:33
		NopCmd
		AssumeExpCmd LAnd(Le(CANON7:26 0xffffffffffffffffffffffffffffffffffffffff ) Ge(CANON7:26 0x0 ) )
		NopCmd
		AssumeExpCmd LAnd(Le(CANON8:27 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff ) Ge(CANON8:27 0x0 ) )
		NopCmd
		AssumeExpCmd LAnd(Le(CANON9:28 0xffffffffffffffffffffffffffffffffffffffff ) Ge(CANON9:28 0x0 ) )
		NopCmd
		AssumeExpCmd LAnd(Le(CANON10:29 0xffffffffffffffffffffffffffffffffffffffff ) Ge(CANON10:29 0x0 ) )
		NopCmd
		AssumeExpCmd LAnd(Le(CANON11:30 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff ) Ge(CANON11:30 0x0 ) )
		NopCmd
		AssumeExpCmd LAnd(Le(CANON12:31 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff ) Ge(CANON12:31 0x0 ) )
		NopCmd
		AssumeExpCmd LAnd(Le(CANON13:32 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff ) Ge(CANON13:32 0x0 ) )
		NopCmd
		AssumeExpCmd LAnd(Le(CANON14:33 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff ) Ge(CANON14:33 0x0 ) )
		AnnotationCmd JSON{"key":{"name":"cvl.label.end","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		AnnotationCmd JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Message","s":"contract address vars initialized"}}
		AnnotationCmd JSON{"key":{"name":"cvl.label.end","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		AnnotationCmd JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Message","s":"setup read tracking instrumentation"}}
		AnnotationCmd JSON{"key":{"name":"cvl.label.end","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		AnnotationCmd JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Message","s":"last storage initialize"}}
		AnnotationCmd JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageGlobalChangeSnippet.StorageTakeSnapshot","lhs":{"namePrefix":"lastStorage","tag":{"#class":"tac.Tag.BlockchainState"},"callIndex":0,"meta":[{"key":{"name":"cvl.local","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true},{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"lastStorage"},{"key":{"name":"cvl.type","type":"spec.cvlast.CVLType$PureCVLType","erasureStrategy":"CallTrace"},"value":{"#class":"spec.cvlast.CVLType.PureCVLType.VMInternal.BlockchainState"}},{"key":{"name":"cvl","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true},{"key":{"name":"cvl.display","type":"java.lang.String","erasureStrategy":"CallTrace"},"value":"lastStorage"}]}}}
		AnnotationCmd JSON{"key":{"name":"cvl.label.end","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		AnnotationCmd JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Message","s":"assumptions about extcodesize"}}
		AssignExpCmd B30:34 Gt(Select(tacExtcodesize!!3:2 Apply(to_skey:bif R15:16) ) 0x0 )
		AssumeCmd B30:34
		AssignExpCmd B31:34 Gt(Select(tacExtcodesize!!3:2 Apply(to_skey:bif R16:17) ) 0x0 )
		AssumeCmd B31:34
		AssignExpCmd B32:34 Gt(Select(tacExtcodesize!!3:2 Apply(to_skey:bif R17:18) ) 0x0 )
		AssumeCmd B32:34
		AnnotationCmd JSON{"key":{"name":"cvl.label.end","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		AnnotationCmd JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Message","s":"assumptions about contracts' addresses"}}
		NopCmd
		AssumeExpCmd Gt(R15:16 0x0 )
		NopCmd
		AssumeExpCmd Le(R15:16 0xffffffffffffffffffffffffffffffffffffffff )
		NopCmd
		AssumeExpCmd Gt(R16:17 0x0 )
		NopCmd
		AssumeExpCmd Le(R16:17 0xffffffffffffffffffffffffffffffffffffffff )
		NopCmd
		AssumeExpCmd Gt(R17:18 0x0 )
		NopCmd
		AssumeExpCmd Le(R17:18 0xffffffffffffffffffffffffffffffffffffffff )
		AnnotationCmd JSON{"key":{"name":"cvl.label.end","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		AnnotationCmd JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Message","s":"assumptions about starting balances"}}
		AssignExpCmd R39:34 Select(tacBalance!!7:6 Apply(to_skey:bif R15:16) )
		NopCmd
		AssumeExpCmd Ge(R39:34 0x0 )
		AssignExpCmd R41:34 Select(tacBalance!!7:6 Apply(to_skey:bif R16:17) )
		NopCmd
		AssumeExpCmd Ge(R41:34 0x0 )
		AssignExpCmd R43:34 Select(tacBalance!!7:6 Apply(to_skey:bif R17:18) )
		NopCmd
		AssumeExpCmd Ge(R43:34 0x0 )
		AnnotationCmd JSON{"key":{"name":"cvl.label.end","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		AnnotationCmd JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Message","s":"assumptions about static addresses"}}
		AnnotationCmd JSON{"key":{"name":"cvl.label.end","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		AnnotationCmd JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Message","s":"assumptions about uniqueness of contracts' addressses"}}
		NopCmd
		AssumeExpCmd LNot(Eq(R15:16 R16:17 ) )
		NopCmd
		AssumeExpCmd LNot(Eq(R15:16 R17:18 ) )
		NopCmd
		AssumeExpCmd LNot(Eq(R16:17 R17:18 ) )
		AnnotationCmd JSON{"key":{"name":"cvl.label.end","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		NopCmd
		AssumeExpCmd Eq(CANON26!!9:8 R16:17 )
		NopCmd
		AssumeExpCmd Eq(CANON27!!10:9 R15:16 )
		AnnotationCmd JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Message","s":"record starting nonces"}}
		AnnotationCmd JSON{"key":{"name":"cvl.label.end","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		AnnotationCmd JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Message","s":"cloned contracts have no balances"}}
		AnnotationCmd JSON{"key":{"name":"cvl.label.end","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		AnnotationCmd JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Message","s":"Linked immutable setup"}}
		AnnotationCmd JSON{"key":{"name":"cvl.label.end","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		AnnotationCmd JSON{"key":{"name":"cvl.label.end","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		AnnotationCmd:35 JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Cmd","cmd":{"cmd_type":"spec.cvlast.CVLCmd.Simple.Apply","cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/specs/BuiltinViewReentrancy.spec","end":{"character":32}},"exp":{"#class":"spec.cvlast.CVLExp.ApplyExp.ContractFunction.Symbolic","methodIdWithCallContext":{"#class":"spec.cvlast.ParametricMethod","methodId":"f","host":{"name":"Curve"}},"args":[{"#class":"spec.cvlast.CVLExp.VariableExp","id":"fenv","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":0}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"env","fields":[{"fieldName":"msg","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"msg","fields":[{"fieldName":"sender","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"value","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}}]}},{"fieldName":"tx","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"tx","fields":[{"fieldName":"origin","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}}]}},{"fieldName":"block","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"block","fields":[{"fieldName":"coinbase","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"difficulty","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"gaslimit","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"number","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"timestamp","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}}]}}]},"cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/specs/BuiltinViewReentrancy.spec","end":{"character":32}}},"twoStateIndex":"NEITHER"},{"#class":"spec.cvlast.CVLExp.VariableExp","id":"fcalldataarg","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":0}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.VMInternal.RawArgs"},"cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/specs/BuiltinViewReentrancy.spec","end":{"character":32}}},"twoStateIndex":"NEITHER"}],"noRevert":true,"storage":{"#class":"spec.cvlast.CVLExp.VariableExp","id":"lastStorage","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":0}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.VMInternal.BlockchainState"},"cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/specs/BuiltinViewReentrancy.spec","end":{"character":32}}},"twoStateIndex":"NEITHER"},"tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":0}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Void"},"cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/specs/BuiltinViewReentrancy.spec","end":{"character":32}}}},"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":0}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}}}}}
		NopCmd
		NopCmd
		NopCmd
		NopCmd
		NopCmd
		NopCmd
		NopCmd
		AnnotationCmd:35 JSON{"key":{"name":"call.trace.push","type":"analysis.icfg.Inliner$CallStack$PushRecord","erasureStrategy":"Canonical"},"value":"rO0ABXNyACphbmFseXNpcy5pY2ZnLklubGluZXIkQ2FsbFN0YWNrJFB1c2hSZWNvcmSX8+DCTLCH+AIAA0kACGNhbGxlZUlkTAAGY2FsbGVldAATTHZjL2RhdGEvTWV0aG9kUmVmO0wAB3N1bW1hcnl0ABVMdmMvZGF0YS9DYWxsU3VtbWFyeTt4cAAAAAFzcgARdmMuZGF0YS5NZXRob2RSZWbJlJTzzU9pGAIAA0wABGF0dHJ0ABdMc2NlbmUvTWV0aG9kQXR0cmlidXRlO0wACmNvbnRyYWN0SWR0ABZMamF2YS9tYXRoL0JpZ0ludGVnZXI7TAAHc2lnSGFzaHQAEExldm0vU2lnaGFzaEludDt4cHNyABxzY2VuZS5NZXRob2RBdHRyaWJ1dGUkQ29tbW9uNHjdebdr9XMCAAB4cgAVc2NlbmUuTWV0aG9kQXR0cmlidXRlcYg2pYWutuUCAAB4cHNyABRqYXZhLm1hdGguQmlnSW50ZWdlcoz8nx+pO/sdAwAGSQAIYml0Q291bnRJAAliaXRMZW5ndGhJABNmaXJzdE5vbnplcm9CeXRlTnVtSQAMbG93ZXN0U2V0Qml0SQAGc2lnbnVtWwAJbWFnbml0dWRldAACW0J4cgAQamF2YS5sYW5nLk51bWJlcoaslR0LlOCLAgAAeHD///////////////7////+AAAAAXVyAAJbQqzzF/gGCFTgAgAAeHAAAAAQzkYEoAAAAAAAAAAAAAAADHhzcgAOZXZtLlNpZ2hhc2hJbnRUdcqNMXEgeAIAAUwAAW5xAH4ABnhwc3EAfgAM///////////////+/////gAAAAF1cQB+ABAAAAAEQht42Xhw"}
		AssignExpCmd:35 M58:34 ByteMapDefinition(CANON38:bv256 -> Ite(Lt(CANON38:34 CANON36:11 ) Unconstrained(bv256) 0x0 ) )
		AssignExpCmd tacCalldatabuf@1:36 LongStore(M58:34 0x0 CANON34:10 0x0 CANON36:11 )
		NopCmd
		AssumeExpCmd Ge(CANON36:11 0x4 )
		NopCmd
		AssumeExpCmd Ge(0x7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff CANON36:11 )
		AssignExpCmd:35 B63 LAnd(Ge(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff CANON7:26 ) Le(0x0 CANON7:26 ) )
		AssertCmd:35 B63 "sanity bounds check on cvl to vm encoding of tacTmp!4752:int failed"
		AssignExpCmd:35 R64:34 Apply(safe_math_narrow:bif CANON7:26)
		NopCmd
		AssumeExpCmd LAnd(Le(R64:37 0xffffffffffffffffffffffffffffffffffffffff ) Ge(R64:37 0x0 ) )
		AssignExpCmd:35 B68 LAnd(Ge(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff CANON8:27 ) Le(0x0 CANON8:27 ) )
		AssertCmd:35 B68 "sanity bounds check on cvl to vm encoding of tacTmp!4755:int failed"
		AssignExpCmd:35 R69:34 Apply(safe_math_narrow:bif CANON8:27)
		NopCmd
		AssumeExpCmd LAnd(Le(R69:38 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff ) Ge(R69:38 0x0 ) )
		AssignExpCmd:35 B74 LAnd(Ge(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff CANON9:28 ) Le(0x0 CANON9:28 ) )
		AssertCmd:35 B74 "sanity bounds check on cvl to vm encoding of tacTmp!4759:int failed"
		AssignExpCmd:35 R75:34 Apply(safe_math_narrow:bif CANON9:28)
		NopCmd
		AssumeExpCmd LAnd(Le(R75:39 0xffffffffffffffffffffffffffffffffffffffff ) Ge(R75:39 0x0 ) )
		AssignExpCmd:35 B79 LAnd(Ge(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff CANON13:32 ) Le(0x0 CANON13:32 ) )
		AssertCmd:35 B79 "sanity bounds check on cvl to vm encoding of tacTmp!4762:int failed"
		AssignExpCmd:35 R80:34 Apply(safe_math_narrow:bif CANON13:32)
		NopCmd
		AssumeExpCmd LAnd(Le(R80:40 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff ) Ge(R80:40 0x0 ) )
		AssignExpCmd:35 B84 LAnd(Ge(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff CANON14:33 ) Le(0x0 CANON14:33 ) )
		AssertCmd:35 B84 "sanity bounds check on cvl to vm encoding of tacTmp!4765:int failed"
		AssignExpCmd:35 R85:34 Apply(safe_math_narrow:bif CANON14:33)
		NopCmd
		AssumeExpCmd LAnd(Le(R85:41 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff ) Ge(R85:41 0x0 ) )
		AssignExpCmd:35 B89 LAnd(Ge(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff CANON8:27 ) Le(0x0 CANON8:27 ) )
		AssertCmd:35 B89 "sanity bounds check on cvl to vm encoding of tacTmp!4768:int failed"
		AssignExpCmd:35 R90:34 Apply(safe_math_narrow:bif CANON8:27)
		AssignExpCmd:35 B92 LAnd(Ge(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff CANON7:26 ) Le(0x0 CANON7:26 ) )
		AssertCmd:35 B92 "sanity bounds check on cvl to vm encoding of tacTmp!4771:int failed"
		AssignExpCmd:35 R93:34 Apply(safe_math_narrow:bif CANON7:26)
		AssignExpCmd:35 R96:34 Select(tacBalance!!7:6 Apply(to_skey:bif R93:34) )
		AssignExpCmd:42 I97:34 IntSub(R96:34 R90:34 )
		AssignExpCmd:42 tacBalance!!98:6 Store(tacBalance!!7:6 Apply(to_skey:bif R93:34) I97:34 )
		AssignExpCmd:35 R99:34 Select(tacBalance!!98:6 Apply(to_skey:bif R17:18) )
		AssignExpCmd:42 R100:34 Add(R99:34 R90:34)
		NopCmd
		AssumeExpCmd Apply(add_noofl:bif R99:34 R90:34)
		AssignExpCmd:42 tacBalance!!102:6 Store(tacBalance!!98:6 Apply(to_skey:bif R17:18) R100:34 )
		AnnotationCmd:35 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.BalanceSnippet","srcAccountInfo":{"old":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R96","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}]},"new":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"I97","tag":{"#class":"tac.Tag.Int"},"callIndex":0,"meta":[{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}]},"addr":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R93","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}]}},"trgAccountInfo":{"old":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R99","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}]},"new":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R100","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}]},"addr":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R17","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"tacContractAt"},{"key":{"name":"tac.contract.sym.addr.name","type":"java.lang.String","erasureStrategy":"Erased"},"value":"Curve"},{"key":{"name":"tac.contract.sym.addr","type":"java.math.BigInteger","erasureStrategy":"Erased"},"value":"ce4604a000000000000000000000000c"}]}},"transferredAmount":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R90","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}]}}}
		JumpCmd 0_0_0_1_0_0
	}
	Block 0_0_0_1_0_0 Succ [0_0_0_2_0_0] {
		LabelCmd "Start procedure Curve-func1_caller()"
		AnnotationCmd JSON{"key":{"name":"fps.free-pointer-is-scalarized","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true}
		AssignExpCmd R103:34 Select(tacExtcodesize!!3:2 Apply(to_skey:bif R17:43) )
		NopCmd
		AssumeExpCmd Gt(R103:34 0x0 )
		AnnotationCmd JSON{"key":{"name":"internal.func.finder.info","type":"analysis.ip.InternalFunctionFinderReport","erasureStrategy":"Erased"},"value":"rO0ABXNyAChhbmFseXNpcy5pcC5JbnRlcm5hbEZ1bmN0aW9uRmluZGVyUmVwb3J0ian+bYn1VdACAAFMABN1bnJlc29sdmVkRnVuY3Rpb25zdAAPTGphdmEvdXRpbC9TZXQ7eHBzcgAhZGF0YXN0cnVjdHVyZXMuTGlua2VkQXJyYXlIYXNoU2V0AAAAAAAAAAEDAAJGAApsb2FkRmFjdG9yTAAJaGFzaFRhYmxldAAuTGRhdGFzdHJ1Y3R1cmVzL2FycmF5aGFzaHRhYmxlL0FycmF5SGFzaFRhYmxlO3hwdwgAAAAAQAAAAHg="}
		AnnotationCmd JSON{"key":{"name":"fps.free-pointer-is-scalarized","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true}
		NopCmd
		AssumeExpCmd Eq(R69:38 0x0 )
		NopCmd
		AssumeExpCmd LNot(Lt(CANON36:11 0x4 ) )
		NopCmd
		AssumeExpCmd Gt(0x82c63066 tacSighash!!18:19 )
		NopCmd
		AssumeExpCmd LNot(Eq(0x3842f776 tacSighash!!18:19 ) )
		NopCmd
		AssumeExpCmd LNot(Eq(0x3d24a36b tacSighash!!18:19 ) )
		NopCmd
		AssumeExpCmd Eq(0x421b78d9 tacSighash!!18:19 )
		AnnotationCmd JSON{"key":{"name":"internal.func.start","type":"analysis.ip.InternalFuncStartAnnotation","erasureStrategy":"CallTrace"},"value":{"id":0,"startPc":1664,"args":[],"methodSignature":{"#class":"spec.cvlast.QualifiedMethodSignature.QualifiedMethodSig","qualifiedMethodName":{"#class":"spec.cvlast.QualifiedFunction","host":{"name":"Curve"},"methodId":"func1_caller"},"params":[],"res":[{"#class":"spec.cvlast.VMParam.Unnamed","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256}}]},"stackOffsetToArgPos":{},"callSiteSrc":{"source":1,"begin":984,"len":351,"jumpType":"ENTER","address":"ce4604a000000000000000000000000c","sourceContext":{"indexToFilepath":{"0":"contracts/Context.sol","1":"contracts/Curve.sol","2":"contracts/CurveToken.sol","3":"contracts/CurveTokenExample.sol","4":"contracts/ERC20.sol","5":"contracts/IERC20.sol","6":"contracts/IERC20Metadata.sol","7":"contracts/ReentrancyGuard.sol"},"sourceDir":".post_autofinders.0"}}}}
		AnnotationCmd JSON{"key":{"name":"internal.func.start","type":"analysis.ip.InternalFuncStartAnnotation","erasureStrategy":"CallTrace"},"value":{"id":1,"startPc":2909,"args":[],"methodSignature":{"#class":"spec.cvlast.QualifiedMethodSignature.QualifiedMethodSig","qualifiedMethodName":{"#class":"spec.cvlast.QualifiedFunction","host":{"name":"Curve"},"methodId":"getVirtualPrice"},"params":[],"res":[{"#class":"spec.cvlast.VMParam.Unnamed","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256}}]},"stackOffsetToArgPos":{},"callSiteSrc":{"source":1,"begin":1311,"len":17,"jumpType":"ENTER","address":"ce4604a000000000000000000000000c","sourceContext":{"indexToFilepath":{"0":"contracts/Context.sol","1":"contracts/Curve.sol","2":"contracts/CurveToken.sol","3":"contracts/CurveTokenExample.sol","4":"contracts/ERC20.sol","5":"contracts/IERC20.sol","6":"contracts/IERC20Metadata.sol","7":"contracts/ReentrancyGuard.sol"},"sourceDir":".post_autofinders.0"}}}}
		AnnotationCmd JSON{"key":{"name":"pta.end-allocation","type":"analysis.alloc.AllocationAnalysis$AbstractLocation","erasureStrategy":"Erased"},"value":{"prevFPWriteIdx":0,"nextFPWriteCmd":{"block":{"#class":"tac.BlockIdentifier","origStartPc":16,"stkTop":1024,"decompCopy":0,"calleeIdx":0,"topOfStackValue":2,"freshCopy":0},"pos":34},"sort":{"#class":"analysis.alloc.AllocationAnalysis.Alloc.ConstBlock","sz":"40"}}}
		AssignExpCmd:44 R112:45 Select(CANON72!!11:12 Apply(skey_basic:bif 0x8) )
		AnnotationCmd JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet","value":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R112","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1010}]},"displayPath":{"#class":"analysis.storage.DisplayPath.ArrayAccess","index":{"#class":"vc.data.TACSymbol.Const","value":"0"},"base":{"#class":"analysis.storage.DisplayPath.Root","name":"admin_balances"}},"storageType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256},"contractInstance":"ce4604a000000000000000000000000c","linkableStorageReadId":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet.None"}}}
		AssignExpCmd:46 R113:47 Select(tacBalance!!102:6 Apply(to_skey:bif R17:43) )
		NopCmd
		AssumeExpCmd LNot(Lt(R113:47 R112:45 ) )
		AssignExpCmd:48 R115:49 Sub(R113:47 R112:45 )
		AssignExpCmd:50 tacMCANON1!!116:3 Store(tacMCANON1!!4:3 0xc0 R115:49 )
		AssignExpCmd:51 R117:52 Select(CANON72!!11:12 Apply(skey_basic:bif 0x9) )
		AnnotationCmd JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet","value":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R117","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1011}]},"displayPath":{"#class":"analysis.storage.DisplayPath.ArrayAccess","index":{"#class":"vc.data.TACSymbol.Const","value":"1"},"base":{"#class":"analysis.storage.DisplayPath.Root","name":"admin_balances"}},"storageType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256},"contractInstance":"ce4604a000000000000000000000000c","linkableStorageReadId":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet.None"}}}
		AssignExpCmd B119:34 Le(CANON26!!9:53 0xffffffffffffffffffffffffffffffffffffffff )
		AssignExpCmd B120:34 Ge(CANON26!!9:53 0x0 )
		NopCmd
		AssumeExpCmd LAnd(B119:34 B120:34 )
		AnnotationCmd JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet","value":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"CANON26!!9","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.scalarization.sort","type":"vc.data.ScalarizationSort","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.ScalarizationSort.Packed","packedStart":{"#class":"vc.data.ScalarizationSort.Split","idx":"b"},"start":0}},{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.storage.bit-width","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":160},{"key":{"name":"tac.storage.pretty.paths","type":"analysis.storage.DisplayPaths","erasureStrategy":"Erased"},"value":{"paths":[{"#class":"analysis.storage.DisplayPath.Root","name":"coins_1"}]}},{"key":{"name":"tac.slot.type","type":"spec.cvlast.typedescriptors.EVMTypeDescriptor$EVMValueType","erasureStrategy":"Canonical"},"value":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.address"}},{"key":{"name":"tac.storage.non-indexed-path","type":"analysis.storage.StorageAnalysisResult$NonIndexedPath","erasureStrategy":"Canonical"},"value":{"#class":"analysis.storage.StorageAnalysisResult.NonIndexedPath.Root","slot":"b"}},{"key":{"name":"tac.storage","type":"java.math.BigInteger","erasureStrategy":"Canonical"},"value":"ce4604a000000000000000000000000c"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1009}]},"displayPath":{"#class":"analysis.storage.DisplayPath.Root","name":"coins_1"},"storageType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.address"},"contractInstance":"ce4604a000000000000000000000000c","linkableStorageReadId":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet.Id","id":0}}}
		AnnotationCmd JSON{"key":{"name":"init.reorder.fence","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		AssignExpCmd:54 tacMCANON2!!123:4 Store(tacMCANON2!!5:4 0x100 0x70a0823100000000000000000000000000000000000000000000000000000000 )
		AssignExpCmd:55 tacMCANON2!!125:4 Store(tacMCANON2!!123:4 0x104 R17:43 )
		AssignExpCmd:54 R126:56 0x100
		AssignHavocCmd:54 R127:57
		AssignHavocCmd tacReturndata!!128:58
		JumpCmd 0_0_0_2_0_0
	}
	Block 4_0_0_0_0_0 Succ [] {
		AnnotationCmd:35 JSON{"key":{"name":"call.trace.pop","type":"analysis.icfg.Inliner$CallStack$PopRecord","erasureStrategy":"Canonical"},"value":"rO0ABXNyAClhbmFseXNpcy5pY2ZnLklubGluZXIkQ2FsbFN0YWNrJFBvcFJlY29yZPAPfwSLdCWJAgABSQAIY2FsbGVlSWR4cAAAAAE="}
		AssumeNotCmd:35 false
		AssumeNotCmd:35 false
		AnnotationCmd JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageGlobalChangeSnippet.StorageTakeSnapshot","lhs":{"namePrefix":"lastStorage","tag":{"#class":"tac.Tag.BlockchainState"},"callIndex":0,"meta":[{"key":{"name":"cvl.local","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true},{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"lastStorage"},{"key":{"name":"cvl.type","type":"spec.cvlast.CVLType$PureCVLType","erasureStrategy":"CallTrace"},"value":{"#class":"spec.cvlast.CVLType.PureCVLType.VMInternal.BlockchainState"}},{"key":{"name":"cvl","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true},{"key":{"name":"cvl.display","type":"java.lang.String","erasureStrategy":"CallTrace"},"value":"lastStorage"}]}}}
		AnnotationCmd:35 JSON{"key":{"name":"cvl.label.end","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		AnnotationCmd JSON{"key":{"name":"PlaceholderData","type":"rules.genericrulecheckers.helpers.InstrumentationPlaceholderCommandsManager$Companion$PlaceholderData","erasureStrategy":"Canonical"},"value":{"index":0,"loc":{"#class":"rules.genericrulecheckers.helpers.InstrumentationPlaceholderCommandsManager.PlaceholdersLocation.Before","ptr":{"block":{"#class":"tac.BlockIdentifier","origStartPc":58,"stkTop":0,"decompCopy":0,"calleeIdx":0,"topOfStackValue":0,"freshCopy":0},"pos":0},"amount":1},"managerId":2}}
	}
	Block 0_0_0_2_0_0 Succ [1_0_0_1_0_0] {
		AnnotationCmd JSON{"key":{"name":"call.trace.push","type":"analysis.icfg.Inliner$CallStack$PushRecord","erasureStrategy":"Canonical"},"value":"rO0ABXNyACphbmFseXNpcy5pY2ZnLklubGluZXIkQ2FsbFN0YWNrJFB1c2hSZWNvcmSX8+DCTLCH+AIAA0kACGNhbGxlZUlkTAAGY2FsbGVldAATTHZjL2RhdGEvTWV0aG9kUmVmO0wAB3N1bW1hcnl0ABVMdmMvZGF0YS9DYWxsU3VtbWFyeTt4cAAAAAJzcgARdmMuZGF0YS5NZXRob2RSZWbJlJTzzU9pGAIAA0wABGF0dHJ0ABdMc2NlbmUvTWV0aG9kQXR0cmlidXRlO0wACmNvbnRyYWN0SWR0ABZMamF2YS9tYXRoL0JpZ0ludGVnZXI7TAAHc2lnSGFzaHQAEExldm0vU2lnaGFzaEludDt4cHNyABxzY2VuZS5NZXRob2RBdHRyaWJ1dGUkQ29tbW9uNHjdebdr9XMCAAB4cgAVc2NlbmUuTWV0aG9kQXR0cmlidXRlcYg2pYWutuUCAAB4cHNyABRqYXZhLm1hdGguQmlnSW50ZWdlcoz8nx+pO/sdAwAGSQAIYml0Q291bnRJAAliaXRMZW5ndGhJABNmaXJzdE5vbnplcm9CeXRlTnVtSQAMbG93ZXN0U2V0Qml0SQAGc2lnbnVtWwAJbWFnbml0dWRldAACW0J4cgAQamF2YS5sYW5nLk51bWJlcoaslR0LlOCLAgAAeHD///////////////7////+AAAAAXVyAAJbQqzzF/gGCFTgAgAAeHAAAAAQzkYEoAAAAAAAAAAAAAAAJ3hzcgAOZXZtLlNpZ2hhc2hJbnRUdcqNMXEgeAIAAUwAAW5xAH4ABnhwc3EAfgAM///////////////+/////gAAAAF1cQB+ABAAAAAEcKCCMXhzcgATdmMuZGF0YS5DYWxsU3VtbWFyeZQcmw5vl+FdAgAQSQAJc3VtbWFyeUlkTAAOY2FsbENvbnZlbnRpb250ACZMaW5zdHJ1bWVudGF0aW9uL2NhbGxzL0NhbGxDb252ZW50aW9uO0wACmNhbGxUYXJnZXR0ABpMYW5hbHlzaXMvaWNmZy9DYWxsVGFyZ2V0O0wACGNhbGxUeXBldAAVTHZjL2RhdGEvVEFDQ2FsbFR5cGU7TAAPY2Fubm90QmVJbmxpbmVkdAAtTGFuYWx5c2lzL2ljZmcvSW5saW5lciRJbGxlZ2FsSW5saW5pbmdSZWFzb247TAAGZ2FzVmFydAATTHZjL2RhdGEvVEFDU3ltYm9sO0wABmluQmFzZXEAfgAbTAAIaW5PZmZzZXRxAH4AG0wABmluU2l6ZXEAfgAbTAAMb3JpZ0NhbGxjb3JldAAgTHZjL2RhdGEvVEFDQ21kJFNpbXBsZSRDYWxsQ29yZTtMAAdvdXRCYXNlcQB+ABtMAAlvdXRPZmZzZXRxAH4AG0wAB291dFNpemVxAH4AG0wADXNpZ1Jlc29sdXRpb250AA9MamF2YS91dGlsL1NldDtMAAV0b1ZhcnEAfgAbTAAIdmFsdWVWYXJxAH4AG3hwAAAAAHNyACRpbnN0cnVtZW50YXRpb24uY2FsbHMuQ2FsbENvbnZlbnRpb25HtO1ulL788QIAA0kACGNhbGxlcklkTAAFaW5wdXR0ABlMYW5hbHlzaXMvaWNmZy9DYWxsSW5wdXQ7TAAGcmF3T3V0dAAiTGluc3RydW1lbnRhdGlvbi9jYWxscy9DYWxsT3V0cHV0O3hwAAAAAHNyABdhbmFseXNpcy5pY2ZnLkNhbGxJbnB1dJjJD1MhNUxQAgAHTAAHYmFzZVZhcnQAGUx2Yy9kYXRhL1RBQ0V4cHIkU3ltJFZhcjtMABBlbmNvZGVkQXJndW1lbnRzdAAjTGFuYWx5c2lzL2ljZmcvQUJJQXJndW1lbnRFbmNvZGluZztMABNpbnB1dFNpemVMb3dlckJvdW5kcQB+AAZMAAZvZmZzZXR0ABVMdmMvZGF0YS9UQUNFeHByJFN5bTtMABRyYW5nZVRvRGVjb21wb3NlZEFyZ3QAD0xqYXZhL3V0aWwvTWFwO0wAEHNpbXBsaWZpZWRPZmZzZXR0ABtMdmMvZGF0YS9UQUNFeHByJFN5bSRDb25zdDtMAARzaXplcQB+ACZ4cHNyABd2Yy5kYXRhLlRBQ0V4cHIkU3ltJFZhcskrg43eGgPnAgACTAABc3QAF0x2Yy9kYXRhL1RBQ1N5bWJvbCRWYXI7TAADdGFndAAJTHRhYy9UYWc7eHIAE3ZjLmRhdGEuVEFDRXhwciRTeW2iVj0S4YSNUAIAAHhyAA92Yy5kYXRhLlRBQ0V4cHJYhGlUu/v+yAIAAHhwc3IANnZjLmRhdGEuVEFDU3ltYm9sJFZhciRXaXRoRGVmYXVsdENhbGxJbmRleCRXaXRoQnl0ZU1hcJ7+oHF4CHAAAgACTAAEbWV0YXQALUxrb3RsaW54L2NvbGxlY3Rpb25zL2ltbXV0YWJsZS9QZXJzaXN0ZW50TWFwO0wACm5hbWVQcmVmaXh0ABJMamF2YS9sYW5nL1N0cmluZzt4cgAVdmMuZGF0YS5UQUNTeW1ib2wkVmFyCYrCGVl9SXYCAAB4cgARdmMuZGF0YS5UQUNTeW1ib2zd3Run/CoWswIAAHhwc3IAJmRhdGFzdHJ1Y3R1cmVzLnRyZWFwLkhhc2hUcmVhcE1hcCROb2Rlf2t9acJIPnQCAANMAANrZXl0ABJMamF2YS9sYW5nL09iamVjdDtMAARuZXh0dAA1TGRhdGFzdHJ1Y3R1cmVzL3RyZWFwL0hhc2hUcmVhcE1hcCRNb3JlS2V5VmFsdWVQYWlycztMAAV2YWx1ZXEAfgA3eHIAIWRhdGFzdHJ1Y3R1cmVzLnRyZWFwLkhhc2hUcmVhcE1hcPMJ/2vt3boKAgAAeHIAHWRhdGFzdHJ1Y3R1cmVzLnRyZWFwLlRyZWFwTWFw46LAyn3v5moCAAB4cgAaZGF0YXN0cnVjdHVyZXMudHJlYXAuVHJlYXA88f21zZwbdQIAAkwABGxlZnR0ABxMZGF0YXN0cnVjdHVyZXMvdHJlYXAvVHJlYXA7TAAFcmlnaHRxAH4APHhwcHNxAH4ANnBzcQB+ADZwcHNyAAt0YWMuTWV0YUtleVF/W3MiCfIZAgADTAAPZXJhc3VyZVN0cmF0ZWd5dAAdTHRhYy9NZXRhS2V5JEVyYXN1cmVTdHJhdGVneTtMAARuYW1lcQB+ADJMAAN0eXB0ABFMamF2YS9sYW5nL0NsYXNzO3hwfnIAG3RhYy5NZXRhS2V5JEVyYXN1cmVTdHJhdGVneQAAAAAAAAAAEgAAeHIADmphdmEubGFuZy5FbnVtAAAAAAAAAAASAAB4cHQACUNhbm9uaWNhbHQAF3RhYy5tZW1vcnkucGFydGl0aW9uLWlkdnIAEWphdmEubGFuZy5JbnRlZ2VyEuKgpPeBhzgCAAFJAAV2YWx1ZXhxAH4ADnBzcQB+AEkAAAACc3EAfgBAcQB+AEZ0ABJUYWMuc3ltYm9sLmtleXdvcmR2cgAQamF2YS5sYW5nLlN0cmluZ6DwpDh6O7NCAgAAeHBwdAAEdGFjTXNxAH4AQHEAfgBGdAANdGFjLmlzLm1lbW9yeXZyACJ0YWMuTWV0YU1hcCRDb21wYW5pb24kTm90aGluZ1ZhbHVl8nsHH85ykpUCAAB4cHBzcQB+AFN0AA90YWNNQ0FOT04yISExMjVzcgAPdGFjLlRhZyRCeXRlTWFwNb/Ry6GDRgkCAAB4cgALdGFjLlRhZyRNYXABJytzDV3P/QIAAHhyAAd0YWMuVGFnLk9V3gn2xngCAAB4cHBzcQB+AAz///////////////7////+AAAAAXVxAH4AEAAAAAEkeHNxAH4AKnNyADV2Yy5kYXRhLlRBQ1N5bWJvbCRWYXIkV2l0aERlZmF1bHRDYWxsSW5kZXgkV2l0aEJpdDI1NnqsyEgq0drPAgACTAAEbWV0YXEAfgAxTAAKbmFtZVByZWZpeHEAfgAyeHEAfgAzc3EAfgA2c3EAfgA2cHBxAH4ATHB0AAFMcHNxAH4AQHEAfgBGdAAQdGFjLnN0YWNrLmhlaWdodHEAfgBKcHNxAH4ASQAAA+50AARSMTI2c3IADnRhYy5UYWckQml0MjU2IyLQT+LlKkgCAAB4cQB+AFlzcgARamF2YS51dGlsLkhhc2hNYXAFB9rBwxZg0QMAAkYACmxvYWRGYWN0b3JJAAl0aHJlc2hvbGR4cD9AAAAAAAADdwgAAAAEAAAAAnNyAB5hbmFseXNpcy5pY2ZnLlNjcmF0Y2hCeXRlUmFuZ2XBTLaPpUzj2gIAAkwABGZyb21xAH4ABkwAAnRvcQB+AAZ4cHNxAH4ADP///////////////v////4AAAAAdXEAfgAQAAAAAHhzcQB+AAz///////////////7////+AAAAAXVxAH4AEAAAAAEDeHNyAC1hbmFseXNpcy5pY2ZnLkRlY29tcG9zZWRDYWxsSW5wdXRBcmckQ29uc3RhbnSFavLdQafqPQIAA0wAAWN0ABlMdmMvZGF0YS9UQUNTeW1ib2wkQ29uc3Q7TAARY29udHJhY3RSZWZlcmVuY2V0AC9MYW5hbHlzaXMvaWNmZy9DYWxsR3JhcGhCdWlsZGVyJENhbGxlZENvbnRyYWN0O0wADHNjcmF0Y2hSYW5nZXQAIExhbmFseXNpcy9pY2ZnL1NjcmF0Y2hCeXRlUmFuZ2U7eHIAJGFuYWx5c2lzLmljZmcuRGVjb21wb3NlZENhbGxJbnB1dEFyZ82Nwhnirh8hAgAAeHBzcgAXdmMuZGF0YS5UQUNTeW1ib2wkQ29uc3QmHp5/l8IUcAIAAkwAA3RhZ3EAfgAsTAAFdmFsdWVxAH4ABnhxAH4ANHEAfgBoc3EAfgAM///////////////+/////gAAAAF1cQB+ABAAAAAgcKCCMQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAB4cHEAfgBsc3EAfgBrc3EAfgAM///////////////+/////gAAAAF1cQB+ABAAAAABBHhzcQB+AAz///////////////7////+AAAAAXVxAH4AEAAAAAEjeHNyAC1hbmFseXNpcy5pY2ZnLkRlY29tcG9zZWRDYWxsSW5wdXRBcmckVmFyaWFibGWV3y80jneopQIAA0wAEWNvbnRyYWN0UmVmZXJlbmNlcQB+AHNMAAxzY3JhdGNoUmFuZ2VxAH4AdEwAAXZxAH4AK3hxAH4AdXNyAERhbmFseXNpcy5pY2ZnLkNhbGxHcmFwaEJ1aWxkZXIkQ2FsbGVkQ29udHJhY3QkRnVsbHlSZXNvbHZlZCRTZWxmTGlua++8l8Aq7q6zAgABTAAKY29udHJhY3RJZHEAfgAGeHIAO2FuYWx5c2lzLmljZmcuQ2FsbEdyYXBoQnVpbGRlciRDYWxsZWRDb250cmFjdCRGdWxseVJlc29sdmVkotnIkxMAs6QCAAB4cgAtYW5hbHlzaXMuaWNmZy5DYWxsR3JhcGhCdWlsZGVyJENhbGxlZENvbnRyYWN00wt1rN/LodcCAAB4cHNxAH4ADP///////////////v////4AAAABdXEAfgAQAAAAEM5GBKAAAAAAAAAAAAAAAAx4cQB+AHtzcQB+AF5zcQB+ADZwc3EAfgA2c3EAfgA2c3EAfgA2cHBxAH4ATHB0AAp0YWNBZGRyZXNzc3EAfgA2cHBzcQB+AEB+cQB+AER0AAZFcmFzZWR0ABp0YWMuY29udHJhY3Quc3ltLmFkZHIubmFtZXEAfgBPcHQABUN1cnZlc3EAfgBAcQB+AEZ0ABd0YWMuZW52Lmtub3duLWJpdC13aWR0aHEAfgBKcHNxAH4ASQAAAKBwc3EAfgBAcQB+AJB0ABV0YWMuY29udHJhY3Quc3ltLmFkZHJ2cQB+AAxwcQB+AIZzcQB+AEBxAH4ARnQAGHRhYy5kZWNvbXAtaW5zY2FsYXIuc29ydHZyAB10YWMuRGVjb21wb3NlZElucHV0U2NhbGFyU29ydCeGMd9jMFQFAgAAeHBwc3IAJHRhYy5EZWNvbXBvc2VkSW5wdXRTY2FsYXJTb3J0JFNpbXBsZXkHVfqoCbJbAgABTAAKYnl0ZU9mZnNldHEAfgAGeHEAfgCccQB+AHx0AANSMTd4cHNxAH4AKnNyABp2Yy5kYXRhLlRBQ1N5bWJvbCRWYXIkRnVsbBPmPQsuB0CVAgAESQAJY2FsbEluZGV4TAAEbWV0YXEAfgAxTAAKbmFtZVByZWZpeHEAfgAyTAADdGFncQB+ACx4cQB+ADMAAAABc3EAfgA2c3EAfgA2cHBxAH4ATHBxAH4AYnBxAH4AY3BzcQB+AEkAAAPtdAAITENBTk9OMTlxAH4AaHEAfgBoc3IAIGluc3RydW1lbnRhdGlvbi5jYWxscy5DYWxsT3V0cHV0wsWbN8G9nHsCAANMAARiYXNlcQB+ACtMAAZvZmZzZXR0ABFMdmMvZGF0YS9UQUNFeHByO0wABHNpemVxAH4AqXhwc3EAfgAwc3EAfgA2cHNxAH4ANnBzcQB+ADZwcHEAfgBDcHEAfgBLcQB+AExwcQB+AFBxAH4AUXBxAH4AVXEAfgBWc3EAfgAqc3EAfgBec3EAfgA2c3EAfgA2cHBxAH4ATHBxAH4AYnBxAH4AY3BzcQB+AEkAAAPucQB+AGZxAH4AaHNyABl2Yy5kYXRhLlRBQ0V4cHIkU3ltJENvbnN0U0iv8zJB2nYCAAJMAAFzcQB+AHJMAAN0YWdxAH4ALHhxAH4ALXNxAH4Ad3EAfgBoc3EAfgAM///////////////+/////gAAAAF1cQB+ABAAAAABIHhxAH4AaHNyAB5hbmFseXNpcy5pY2ZnLkNhbGxUYXJnZXQkVmFsaWS5phn2PatV+gIAAUwABmNhbGxlZXEAfgBzeHIAGGFuYWx5c2lzLmljZmcuQ2FsbFRhcmdldEbdPSx8dj4lAgAAeHBzcgBHYW5hbHlzaXMuaWNmZy5DYWxsR3JhcGhCdWlsZGVyJENhbGxlZENvbnRyYWN0JEZ1bGx5UmVzb2x2ZWQkU3RvcmFnZUxpbmvSgQnS0FaL1QIAAkkADXN0b3JhZ2VSZWFkSWRMAApjb250cmFjdElkcQB+AAZ4cQB+AIMAAAAkcQB+AA9+cgATdmMuZGF0YS5UQUNDYWxsVHlwZQAAAAAAAAAAEgAAeHEAfgBFdAAGU1RBVElDcHNxAH4AXnNxAH4ANnNxAH4ANnBwcQB+AExwcQB+AGJwcQB+AGNwc3EAfgBJAAAD6nQABFIxMjdzcQB+ADBzcQB+ADZwc3EAfgA2cHNxAH4ANnBwcQB+AENwcQB+AEtxAH4ATHBxAH4AUHEAfgBRcHEAfgBVcQB+AFZzcQB+AF5zcQB+ADZzcQB+ADZwcHEAfgBMcHEAfgBicHEAfgBjcHEAfgBlcQB+AGZzcQB+AHdxAH4AaHEAfgBbc3IAHnZjLmRhdGEuVEFDQ21kJFNpbXBsZSRDYWxsQ29yZaEphUcEgWZ6AgALTAAIY2FsbFR5cGVxAH4AGUwAA2dhc3EAfgAbTAAGaW5CYXNlcQB+ACtMAAhpbk9mZnNldHEAfgAbTAAGaW5TaXplcQB+ABtMAARtZXRhcQB+ADFMAAdvdXRCYXNlcQB+ACtMAAlvdXRPZmZzZXRxAH4AG0wAB291dFNpemVxAH4AG0wAAnRvcQB+ABtMAAV2YWx1ZXEAfgAbeHIAFXZjLmRhdGEuVEFDQ21kJFNpbXBsZe0m1iUxBnXSAgAAeHIAE3ZjLmRhdGEuVEFDQ21kJFNwZWMbq/EA+MEDvgIAAHhyAA52Yy5kYXRhLlRBQ0NtZFTLD4g8OR/wAgAAeHBxAH4Av3NxAH4AXnNxAH4ANnNxAH4ANnBwcQB+AExwcQB+AGJwcQB+AGNwcQB+AMRxAH4AxXNxAH4AMHNxAH4ANnBzcQB+ADZwc3EAfgA2cHBxAH4AQ3BxAH4AS3EAfgBMcHEAfgBQcQB+AFFwcQB+AFVxAH4AVnNxAH4AXnNxAH4ANnNxAH4ANnBwcQB+AExwcQB+AGJwcQB+AGNwcQB+AGVxAH4AZnNxAH4AogAAAAFzcQB+ADZzcQB+ADZwcHEAfgBMcHEAfgBicHEAfgBjcHEAfgCmcQB+AKdxAH4AaHNxAH4ANnBwc3EAfgBAfnEAfgBEdAAJQ2FsbFRyYWNldAAIdGFjLm1ldGF2cgATdmMuZGF0YS5UQUNNZXRhSW5mbzVgTP2lS6hxAgAGSQAFYmVnaW5JAANsZW5JAAZzb3VyY2VMAAdhZGRyZXNzcQB+AAZMAAhqdW1wVHlwZXQAE0xjb21waWxlci9KdW1wVHlwZTtMAA1zb3VyY2VDb250ZXh0dAAYTGNvbXBpbGVyL1NvdXJjZUNvbnRleHQ7eHBwc3EAfgDlAAAXHwAAACcAAAABcQB+AIZ+cgARY29tcGlsZXIuSnVtcFR5cGUAAAAAAAAAABIAAHhxAH4ARXQAB1JFR1VMQVJzcgAWY29tcGlsZXIuU291cmNlQ29udGV4dIzLW+lAXNoTAgACTAAPaW5kZXhUb0ZpbGVwYXRocQB+ACdMAAlzb3VyY2VEaXJxAH4AMnhwc3EAfgBpP0AAAAAAAAx3CAAAABAAAAAIc3EAfgBJAAAAAHQAFWNvbnRyYWN0cy9Db250ZXh0LnNvbHNxAH4ASQAAAAF0ABNjb250cmFjdHMvQ3VydmUuc29scQB+AEt0ABhjb250cmFjdHMvQ3VydmVUb2tlbi5zb2xzcQB+AEkAAAADdAAfY29udHJhY3RzL0N1cnZlVG9rZW5FeGFtcGxlLnNvbHNxAH4ASQAAAAR0ABNjb250cmFjdHMvRVJDMjAuc29sc3EAfgBJAAAABXQAFGNvbnRyYWN0cy9JRVJDMjAuc29sc3EAfgBJAAAABnQAHGNvbnRyYWN0cy9JRVJDMjBNZXRhZGF0YS5zb2xzcQB+AEkAAAAHdAAdY29udHJhY3RzL1JlZW50cmFuY3lHdWFyZC5zb2x4dAATLnBvc3RfYXV0b2ZpbmRlcnMuMHNxAH4AMHNxAH4ANnBzcQB+ADZwc3EAfgA2cHBxAH4AQ3BxAH4AS3EAfgBMcHEAfgBQcQB+AFFwcQB+AFVxAH4AVnNxAH4AXnNxAH4ANnNxAH4ANnBwcQB+AExwcQB+AGJwcQB+AGNwcQB+ALNxAH4AZnEAfgC2c3EAfgBec3EAfgA2c3EAfgA2c3EAfgA2c3EAfgA2cHNxAH4ANnBwcQB+AExwcQB+AGJzcQB+AEBxAH4ARnQAFnRhYy5zY2FsYXJpemF0aW9uLnNvcnR2cgAZdmMuZGF0YS5TY2FsYXJpemF0aW9uU29ydDDOcJ3kaA0mAgAAeHBwc3IAIHZjLmRhdGEuU2NhbGFyaXphdGlvblNvcnQkUGFja2VkLkWtEpOI5PcCAAJJAAVzdGFydEwAC3BhY2tlZFN0YXJ0dAAbTHZjL2RhdGEvU2NhbGFyaXphdGlvblNvcnQ7eHEAfgEPAAAAAHNyAB92Yy5kYXRhLlNjYWxhcml6YXRpb25Tb3J0JFNwbGl0VP9Zp/HHsgUCAAFMAANpZHhxAH4ABnhxAH4BD3NxAH4ADP///////////////v////4AAAABdXEAfgAQAAAAAQt4c3EAfgA2cHNxAH4ANnBzcQB+ADZwcHNxAH4AQHEAfgBGdAAcdGFjLnN0b3JhZ2Uubm9uLWluZGV4ZWQtcGF0aHZyADVhbmFseXNpcy5zdG9yYWdlLlN0b3JhZ2VBbmFseXNpc1Jlc3VsdCROb25JbmRleGVkUGF0aAjBoEuh+j9FAgAAeHBwc3IAOmFuYWx5c2lzLnN0b3JhZ2UuU3RvcmFnZUFuYWx5c2lzUmVzdWx0JE5vbkluZGV4ZWRQYXRoJFJvb3S/N/XYpeoK/wIAAUwABHNsb3RxAH4ABnhxAH4BHXEAfgEWc3EAfgBAcQB+AEZ0AA10YWMuc2xvdC50eXBldnIAOnNwZWMuY3ZsYXN0LnR5cGVkZXNjcmlwdG9ycy5FVk1UeXBlRGVzY3JpcHRvciRFVk1WYWx1ZVR5cGXGia8Cuuq4JQIAAHhyAC1zcGVjLmN2bGFzdC50eXBlZGVzY3JpcHRvcnMuRVZNVHlwZURlc2NyaXB0b3LIUanxPMJqHQIAAHhwcHNyADVzcGVjLmN2bGFzdC50eXBlZGVzY3JpcHRvcnMuRVZNVHlwZURlc2NyaXB0b3IkYWRkcmVzc3r4ZfRvl6ApAgAAeHIARHNwZWMuY3ZsYXN0LnR5cGVkZXNjcmlwdG9ycy5FVk1UeXBlRGVzY3JpcHRvciRFVk1Jc29tb3JwaGljVmFsdWVUeXBl93WYkW4QoQ8CAAB4cQB+ASNzcQB+AEBxAH4AkHQAGHRhYy5zdG9yYWdlLnByZXR0eS5wYXRoc3ZyAB1hbmFseXNpcy5zdG9yYWdlLkRpc3BsYXlQYXRoc/dES7fD9VEWAgABTAAFcGF0aHNxAH4AHXhwcHNxAH4BK3NyABdqYXZhLnV0aWwuTGlua2VkSGFzaFNldNhs11qV3SoeAgAAeHIAEWphdmEudXRpbC5IYXNoU2V0ukSFlZa4tzQDAAB4cHcMAAAAED9AAAAAAAABc3IAIWFuYWx5c2lzLnN0b3JhZ2UuRGlzcGxheVBhdGgkUm9vdNNzoL2Z0DxyAgACTAAEYmFzZXQAHkxhbmFseXNpcy9zdG9yYWdlL0Rpc3BsYXlQYXRoO0wABG5hbWVxAH4AMnhyABxhbmFseXNpcy5zdG9yYWdlLkRpc3BsYXlQYXRoT0Bj6lbSIAUCAAB4cHB0AAdjb2luc18xeHNxAH4AQHEAfgBGdAAVdGFjLnN0b3JhZ2UuYml0LXdpZHRocQB+AEpwc3EAfgBJAAAAoHBzcQB+AEBxAH4ARnQAC3RhYy5zdG9yYWdlcQB+AJlwcQB+AIZwcQB+AGNwc3EAfgBJAAAD8nQACkNBTk9OMjYhITlzcQB+AHdxAH4AaHEAfgBtc3EAfgAwc3EAfgA2cHNxAH4ANnBzcQB+ADZwcHEAfgBDcHEAfgBLcQB+AExwcQB+AFBxAH4AUXBxAH4AVXEAfgBWc3EAfgBec3EAfgA2c3EAfgA2cHBxAH4ATHBxAH4AYnBxAH4AY3BxAH4As3EAfgBmcQB+ALZzcgAiamF2YS51dGlsLkNvbGxlY3Rpb25zJFNpbmdsZXRvblNldCxSQZgpwLG/AgABTAAHZWxlbWVudHEAfgA3eHBxAH4AFHNxAH4AXnNxAH4ANnNxAH4ANnNxAH4ANnNxAH4ANnBzcQB+ADZwcHEAfgBMcHEAfgBicQB+AQ1wcQB+ARNzcQB+ADZwc3EAfgA2cHNxAH4ANnBwcQB+ARtwcQB+ASBxAH4BIXBxAH4BKHEAfgEpcHNxAH4BK3NxAH4BLncMAAAAED9AAAAAAAABcQB+ATR4cQB+ATZwcQB+AThwcQB+ATlwcQB+AIZwcQB+AGNwcQB+ATtxAH4BPHNxAH4Ad3EAfgBocQB+AG0="}
		AnnotationCmd JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageGlobalChangeSnippet.StorageBackupPoint","calleeTxId":2}}
		NopCmd
		AssumeExpCmd LAnd(Eq(tacCalldatasize!!0:1 0x24 ) Eq(tacCalldatasize!!0:1 0x24 ) )
		NopCmd
		AssumeExpCmd Eq(tacCalldatabufCANON0@2:0 0x70a0823100000000000000000000000000000000000000000000000000000000 )
		AssignExpCmd tacCalldatabufCANON1@2:59 R17:60
		LabelCmd "Start procedure ERC20-balanceOf(address)"
		AnnotationCmd JSON{"key":{"name":"fps.free-pointer-is-scalarized","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true}
		AssignExpCmd R132:34 Select(tacExtcodesize!!3:2 Apply(to_skey:bif R16:61) )
		NopCmd
		AssumeExpCmd Gt(R132:34 0x0 )
		AnnotationCmd JSON{"key":{"name":"internal.func.finder.info","type":"analysis.ip.InternalFunctionFinderReport","erasureStrategy":"Erased"},"value":"rO0ABXNyAChhbmFseXNpcy5pcC5JbnRlcm5hbEZ1bmN0aW9uRmluZGVyUmVwb3J0ian+bYn1VdACAAFMABN1bnJlc29sdmVkRnVuY3Rpb25zdAAPTGphdmEvdXRpbC9TZXQ7eHBzcgAhZGF0YXN0cnVjdHVyZXMuTGlua2VkQXJyYXlIYXNoU2V0AAAAAAAAAAEDAAJGAApsb2FkRmFjdG9yTAAJaGFzaFRhYmxldAAuTGRhdGFzdHJ1Y3R1cmVzL2FycmF5aGFzaHRhYmxlL0FycmF5SGFzaFRhYmxlO3hwdwgAAAAAQAAAAHg="}
		AnnotationCmd JSON{"key":{"name":"fps.free-pointer-is-scalarized","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true}
		NopCmd
		AssumeExpCmd LNot(Lt(tacCalldatasize!!0:1 0x4 ) )
		NopCmd
		AssumeExpCmd LNot(Gt(0x39509351 tacSighash!!19:19 ) )
		NopCmd
		AssumeExpCmd LNot(Eq(0x39509351 tacSighash!!19:19 ) )
		NopCmd
		AssumeExpCmd Eq(0x70a08231 tacSighash!!19:19 )
		AssignExpCmd:62 R138:63 Sub(tacCalldatasize!!0:1 0x4 )
		AssignExpCmd B139:64 Slt(R138:63 0x20 )
		NopCmd
		AssumeExpCmd LNot(B139:64 )
		AssignExpCmd:65 R141:66 tacCalldatabufCANON1@2:67
		NopCmd
		AssumeExpCmd Eq(R17:60 R17:60 )
		AnnotationCmd JSON{"key":{"name":"internal.func.start","type":"analysis.ip.InternalFuncStartAnnotation","erasureStrategy":"CallTrace"},"value":{"id":2,"startPc":1712,"args":[{"s":{"namePrefix":"R141","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1013}]},"offset":1,"sort":"SCALAR"}],"methodSignature":{"#class":"spec.cvlast.QualifiedMethodSignature.QualifiedMethodSig","qualifiedMethodName":{"#class":"spec.cvlast.QualifiedFunction","host":{"name":"ERC20"},"methodId":"balanceOf"},"params":[{"#class":"spec.cvlast.VMParam.Named","name":"account","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$address"}}],"res":[{"#class":"spec.cvlast.VMParam.Unnamed","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256}}]},"stackOffsetToArgPos":{"1":0},"callSiteSrc":{"source":1,"begin":4376,"len":467,"jumpType":"ENTER","address":"ce4604a0000000000000000000000027","sourceContext":{"indexToFilepath":{"0":"contracts/Context.sol","1":"contracts/ERC20.sol","2":"contracts/IERC20.sol","3":"contracts/IERC20Metadata.sol"},"sourceDir":".post_autofinders.2"}}}}
		AssignExpCmd:68 R146:69 Apply(hash_3_keccak:bif Apply(skey_basic:bif 0x40) Apply(to_skey:bif R17:60) Apply(skey_basic:bif 0x0))
		AssignExpCmd:70 R147:69 Select(CANON85!!13:14 R146:71 )
		AnnotationCmd JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet","value":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R147","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1020}]},"displayPath":{"#class":"analysis.storage.DisplayPath.MapAccess","key":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R141","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1018}]},"keyTyp":{"#class":"tac.TACStorageType.IntegralType","typeLabel":"address","numBytes":"14","descriptor":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$address"},"lowerBound":null,"upperBound":null},"base":{"#class":"analysis.storage.DisplayPath.Root","name":"_balances"}},"storageType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256},"contractInstance":"ce4604a0000000000000000000000027","linkableStorageReadId":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet.None"}}}
		AnnotationCmd JSON{"key":{"name":"internal.func.end","type":"analysis.ip.InternalFuncExitAnnotation","erasureStrategy":"Canonical"},"value":{"id":2,"rets":[{"s":{"namePrefix":"R147","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1023}]},"offset":0}],"functionLayout":{"0":{"#class":"analysis.ip.InternalFuncValueLocation.Scalar"}}}}
		AnnotationCmd JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.EVMFunctionReturnWrite","returnbufOffset":"0","returnValueSym":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R147","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1023}]},"callIndex":2}}
		AnnotationCmd JSON{"key":{"name":"tac.return.path","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		LabelCmd "End procedure ERC20-balanceOf(address)"
		AssignExpCmd tacReturndata!!149:58 Store(tacReturndata!!128:58 0x0 R147:69 )
		AssignExpCmd tacMCANON2!!150:4 Store(tacMCANON2!!125:4 0x100 R147:69 )
		AnnotationCmd JSON{"key":{"name":"call.trace.pop","type":"analysis.icfg.Inliner$CallStack$PopRecord","erasureStrategy":"Canonical"},"value":"rO0ABXNyAClhbmFseXNpcy5pY2ZnLklubGluZXIkQ2FsbFN0YWNrJFBvcFJlY29yZPAPfwSLdCWJAgABSQAIY2FsbGVlSWR4cAAAAAI="}
		JumpCmd 1_0_0_1_0_0
	}
	Block 0_0_0_3_0_0 Succ [2_0_0_1_0_0] {
		AnnotationCmd JSON{"key":{"name":"call.trace.push","type":"analysis.icfg.Inliner$CallStack$PushRecord","erasureStrategy":"Canonical"},"value":"rO0ABXNyACphbmFseXNpcy5pY2ZnLklubGluZXIkQ2FsbFN0YWNrJFB1c2hSZWNvcmSX8+DCTLCH+AIAA0kACGNhbGxlZUlkTAAGY2FsbGVldAATTHZjL2RhdGEvTWV0aG9kUmVmO0wAB3N1bW1hcnl0ABVMdmMvZGF0YS9DYWxsU3VtbWFyeTt4cAAAAANzcgARdmMuZGF0YS5NZXRob2RSZWbJlJTzzU9pGAIAA0wABGF0dHJ0ABdMc2NlbmUvTWV0aG9kQXR0cmlidXRlO0wACmNvbnRyYWN0SWR0ABZMamF2YS9tYXRoL0JpZ0ludGVnZXI7TAAHc2lnSGFzaHQAEExldm0vU2lnaGFzaEludDt4cHNyABxzY2VuZS5NZXRob2RBdHRyaWJ1dGUkQ29tbW9uNHjdebdr9XMCAAB4cgAVc2NlbmUuTWV0aG9kQXR0cmlidXRlcYg2pYWutuUCAAB4cHNyABRqYXZhLm1hdGguQmlnSW50ZWdlcoz8nx+pO/sdAwAGSQAIYml0Q291bnRJAAliaXRMZW5ndGhJABNmaXJzdE5vbnplcm9CeXRlTnVtSQAMbG93ZXN0U2V0Qml0SQAGc2lnbnVtWwAJbWFnbml0dWRldAACW0J4cgAQamF2YS5sYW5nLk51bWJlcoaslR0LlOCLAgAAeHD///////////////7////+AAAAAXVyAAJbQqzzF/gGCFTgAgAAeHAAAAAQzkYEoAAAAAAAAAAAAAAADHhzcgAOZXZtLlNpZ2hhc2hJbnRUdcqNMXEgeAIAAUwAAW5xAH4ABnhwc3EAfgAM///////////////+/////gAAAAF1cQB+ABAAAAAEOEL3dnhzcgATdmMuZGF0YS5DYWxsU3VtbWFyeZQcmw5vl+FdAgAQSQAJc3VtbWFyeUlkTAAOY2FsbENvbnZlbnRpb250ACZMaW5zdHJ1bWVudGF0aW9uL2NhbGxzL0NhbGxDb252ZW50aW9uO0wACmNhbGxUYXJnZXR0ABpMYW5hbHlzaXMvaWNmZy9DYWxsVGFyZ2V0O0wACGNhbGxUeXBldAAVTHZjL2RhdGEvVEFDQ2FsbFR5cGU7TAAPY2Fubm90QmVJbmxpbmVkdAAtTGFuYWx5c2lzL2ljZmcvSW5saW5lciRJbGxlZ2FsSW5saW5pbmdSZWFzb247TAAGZ2FzVmFydAATTHZjL2RhdGEvVEFDU3ltYm9sO0wABmluQmFzZXEAfgAbTAAIaW5PZmZzZXRxAH4AG0wABmluU2l6ZXEAfgAbTAAMb3JpZ0NhbGxjb3JldAAgTHZjL2RhdGEvVEFDQ21kJFNpbXBsZSRDYWxsQ29yZTtMAAdvdXRCYXNlcQB+ABtMAAlvdXRPZmZzZXRxAH4AG0wAB291dFNpemVxAH4AG0wADXNpZ1Jlc29sdXRpb250AA9MamF2YS91dGlsL1NldDtMAAV0b1ZhcnEAfgAbTAAIdmFsdWVWYXJxAH4AG3hwAAAAAXNyACRpbnN0cnVtZW50YXRpb24uY2FsbHMuQ2FsbENvbnZlbnRpb25HtO1ulL788QIAA0kACGNhbGxlcklkTAAFaW5wdXR0ABlMYW5hbHlzaXMvaWNmZy9DYWxsSW5wdXQ7TAAGcmF3T3V0dAAiTGluc3RydW1lbnRhdGlvbi9jYWxscy9DYWxsT3V0cHV0O3hwAAAAAHNyABdhbmFseXNpcy5pY2ZnLkNhbGxJbnB1dJjJD1MhNUxQAgAHTAAHYmFzZVZhcnQAGUx2Yy9kYXRhL1RBQ0V4cHIkU3ltJFZhcjtMABBlbmNvZGVkQXJndW1lbnRzdAAjTGFuYWx5c2lzL2ljZmcvQUJJQXJndW1lbnRFbmNvZGluZztMABNpbnB1dFNpemVMb3dlckJvdW5kcQB+AAZMAAZvZmZzZXR0ABVMdmMvZGF0YS9UQUNFeHByJFN5bTtMABRyYW5nZVRvRGVjb21wb3NlZEFyZ3QAD0xqYXZhL3V0aWwvTWFwO0wAEHNpbXBsaWZpZWRPZmZzZXR0ABtMdmMvZGF0YS9UQUNFeHByJFN5bSRDb25zdDtMAARzaXplcQB+ACZ4cHNyABd2Yy5kYXRhLlRBQ0V4cHIkU3ltJFZhcskrg43eGgPnAgACTAABc3QAF0x2Yy9kYXRhL1RBQ1N5bWJvbCRWYXI7TAADdGFndAAJTHRhYy9UYWc7eHIAE3ZjLmRhdGEuVEFDRXhwciRTeW2iVj0S4YSNUAIAAHhyAA92Yy5kYXRhLlRBQ0V4cHJYhGlUu/v+yAIAAHhwc3IANnZjLmRhdGEuVEFDU3ltYm9sJFZhciRXaXRoRGVmYXVsdENhbGxJbmRleCRXaXRoQnl0ZU1hcJ7+oHF4CHAAAgACTAAEbWV0YXQALUxrb3RsaW54L2NvbGxlY3Rpb25zL2ltbXV0YWJsZS9QZXJzaXN0ZW50TWFwO0wACm5hbWVQcmVmaXh0ABJMamF2YS9sYW5nL1N0cmluZzt4cgAVdmMuZGF0YS5UQUNTeW1ib2wkVmFyCYrCGVl9SXYCAAB4cgARdmMuZGF0YS5UQUNTeW1ib2zd3Run/CoWswIAAHhwc3IAJmRhdGFzdHJ1Y3R1cmVzLnRyZWFwLkhhc2hUcmVhcE1hcCROb2Rlf2t9acJIPnQCAANMAANrZXl0ABJMamF2YS9sYW5nL09iamVjdDtMAARuZXh0dAA1TGRhdGFzdHJ1Y3R1cmVzL3RyZWFwL0hhc2hUcmVhcE1hcCRNb3JlS2V5VmFsdWVQYWlycztMAAV2YWx1ZXEAfgA3eHIAIWRhdGFzdHJ1Y3R1cmVzLnRyZWFwLkhhc2hUcmVhcE1hcPMJ/2vt3boKAgAAeHIAHWRhdGFzdHJ1Y3R1cmVzLnRyZWFwLlRyZWFwTWFw46LAyn3v5moCAAB4cgAaZGF0YXN0cnVjdHVyZXMudHJlYXAuVHJlYXA88f21zZwbdQIAAkwABGxlZnR0ABxMZGF0YXN0cnVjdHVyZXMvdHJlYXAvVHJlYXA7TAAFcmlnaHRxAH4APHhwcHNxAH4ANnBzcQB+ADZwcHNyAAt0YWMuTWV0YUtleVF/W3MiCfIZAgADTAAPZXJhc3VyZVN0cmF0ZWd5dAAdTHRhYy9NZXRhS2V5JEVyYXN1cmVTdHJhdGVneTtMAARuYW1lcQB+ADJMAAN0eXB0ABFMamF2YS9sYW5nL0NsYXNzO3hwfnIAG3RhYy5NZXRhS2V5JEVyYXN1cmVTdHJhdGVneQAAAAAAAAAAEgAAeHIADmphdmEubGFuZy5FbnVtAAAAAAAAAAASAAB4cHQACUNhbm9uaWNhbHQAF3RhYy5tZW1vcnkucGFydGl0aW9uLWlkdnIAEWphdmEubGFuZy5JbnRlZ2VyEuKgpPeBhzgCAAFJAAV2YWx1ZXhxAH4ADnBzcQB+AEkAAAACc3EAfgBAcQB+AEZ0ABJUYWMuc3ltYm9sLmtleXdvcmR2cgAQamF2YS5sYW5nLlN0cmluZ6DwpDh6O7NCAgAAeHBwdAAEdGFjTXNxAH4AQHEAfgBGdAANdGFjLmlzLm1lbW9yeXZyACJ0YWMuTWV0YU1hcCRDb21wYW5pb24kTm90aGluZ1ZhbHVl8nsHH85ykpUCAAB4cHBzcQB+AFN0AA90YWNNQ0FOT04yISEyMTFzcgAPdGFjLlRhZyRCeXRlTWFwNb/Ry6GDRgkCAAB4cgALdGFjLlRhZyRNYXABJytzDV3P/QIAAHhyAAd0YWMuVGFnLk9V3gn2xngCAAB4cHBzcQB+AAz///////////////7////+AAAAAXVxAH4AEAAAAAFkeHNxAH4AKnNyADV2Yy5kYXRhLlRBQ1N5bWJvbCRWYXIkV2l0aERlZmF1bHRDYWxsSW5kZXgkV2l0aEJpdDI1NnqsyEgq0drPAgACTAAEbWV0YXEAfgAxTAAKbmFtZVByZWZpeHEAfgAyeHEAfgAzc3EAfgA2c3EAfgA2cHBxAH4ATHB0AAFMcHNxAH4AQHEAfgBGdAAQdGFjLnN0YWNrLmhlaWdodHEAfgBKcHNxAH4ASQAAA/Z0AARSMjEyc3IADnRhYy5UYWckQml0MjU2IyLQT+LlKkgCAAB4cQB+AFlzcgARamF2YS51dGlsLkhhc2hNYXAFB9rBwxZg0QMAAkYACmxvYWRGYWN0b3JJAAl0aHJlc2hvbGR4cD9AAAAAAAADdwgAAAAEAAAAAnNyAB5hbmFseXNpcy5pY2ZnLlNjcmF0Y2hCeXRlUmFuZ2XBTLaPpUzj2gIAAkwABGZyb21xAH4ABkwAAnRvcQB+AAZ4cHNxAH4ADP///////////////v////4AAAAAdXEAfgAQAAAAAHhzcQB+AAz///////////////7////+AAAAAXVxAH4AEAAAAAEDeHNyAC1hbmFseXNpcy5pY2ZnLkRlY29tcG9zZWRDYWxsSW5wdXRBcmckQ29uc3RhbnSFavLdQafqPQIAA0wAAWN0ABlMdmMvZGF0YS9UQUNTeW1ib2wkQ29uc3Q7TAARY29udHJhY3RSZWZlcmVuY2V0AC9MYW5hbHlzaXMvaWNmZy9DYWxsR3JhcGhCdWlsZGVyJENhbGxlZENvbnRyYWN0O0wADHNjcmF0Y2hSYW5nZXQAIExhbmFseXNpcy9pY2ZnL1NjcmF0Y2hCeXRlUmFuZ2U7eHIAJGFuYWx5c2lzLmljZmcuRGVjb21wb3NlZENhbGxJbnB1dEFyZ82Nwhnirh8hAgAAeHBzcgAXdmMuZGF0YS5UQUNTeW1ib2wkQ29uc3QmHp5/l8IUcAIAAkwAA3RhZ3EAfgAsTAAFdmFsdWVxAH4ABnhxAH4ANHEAfgBoc3EAfgAM///////////////+/////gAAAAF1cQB+ABAAAAAgOEL3dgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAB4cHEAfgBsc3EAfgBrc3EAfgAM///////////////+/////gAAAAF1cQB+ABAAAAABRHhzcQB+AAz///////////////7////+AAAAAXVxAH4AEAAAAAFjeHNyAC1hbmFseXNpcy5pY2ZnLkRlY29tcG9zZWRDYWxsSW5wdXRBcmckVmFyaWFibGWV3y80jneopQIAA0wAEWNvbnRyYWN0UmVmZXJlbmNlcQB+AHNMAAxzY3JhdGNoUmFuZ2VxAH4AdEwAAXZxAH4AK3hxAH4AdXNyADxhbmFseXNpcy5pY2ZnLkNhbGxHcmFwaEJ1aWxkZXIkQ2FsbGVkQ29udHJhY3QkVW5yZXNvbHZlZFJlYWRDhKJZ0RDzoAIAAUkADXN0b3JhZ2VSZWFkSWR4cgAtYW5hbHlzaXMuaWNmZy5DYWxsR3JhcGhCdWlsZGVyJENhbGxlZENvbnRyYWN00wt1rN/LodcCAAB4cAAAAAJxAH4Ae3NxAH4AXnNxAH4ANnNxAH4ANnBzcQB+ADZzcQB+ADZzcQB+ADZwc3EAfgA2cHBxAH4ATHBxAH4AYnNxAH4AQHEAfgBGdAAWdGFjLnNjYWxhcml6YXRpb24uc29ydHZyABl2Yy5kYXRhLlNjYWxhcml6YXRpb25Tb3J0MM5wneRoDSYCAAB4cHBzcgAfdmMuZGF0YS5TY2FsYXJpemF0aW9uU29ydCRTcGxpdFT/Wafxx7IFAgABTAADaWR4cQB+AAZ4cQB+AI5zcQB+AAz///////////////7////+AAAAAXVxAH4AEAAAAAEFeHNxAH4ANnBzcQB+ADZwc3EAfgA2cHBzcQB+AEBxAH4ARnQAHHRhYy5zdG9yYWdlLm5vbi1pbmRleGVkLXBhdGh2cgA1YW5hbHlzaXMuc3RvcmFnZS5TdG9yYWdlQW5hbHlzaXNSZXN1bHQkTm9uSW5kZXhlZFBhdGgIwaBLofo/RQIAAHhwcHNyADphbmFseXNpcy5zdG9yYWdlLlN0b3JhZ2VBbmFseXNpc1Jlc3VsdCROb25JbmRleGVkUGF0aCRSb290vzf12KXqCv8CAAFMAARzbG90cQB+AAZ4cQB+AJlxAH4AknNxAH4AQHEAfgBGdAANdGFjLnNsb3QudHlwZXZyADpzcGVjLmN2bGFzdC50eXBlZGVzY3JpcHRvcnMuRVZNVHlwZURlc2NyaXB0b3IkRVZNVmFsdWVUeXBlxomvArrquCUCAAB4cgAtc3BlYy5jdmxhc3QudHlwZWRlc2NyaXB0b3JzLkVWTVR5cGVEZXNjcmlwdG9yyFGp8TzCah0CAAB4cHBzcgAzc3BlYy5jdmxhc3QudHlwZWRlc2NyaXB0b3JzLkVWTVR5cGVEZXNjcmlwdG9yJFVJbnRL+xQfR/Nlf8ACAAFJAAhiaXR3aWR0aHhyAERzcGVjLmN2bGFzdC50eXBlZGVzY3JpcHRvcnMuRVZNVHlwZURlc2NyaXB0b3IkRVZNSXNvbW9ycGhpY1ZhbHVlVHlwZfd1mJFuEKEPAgAAeHEAfgCfAAABAHNxAH4AQH5xAH4ARHQABkVyYXNlZHQAGHRhYy5zdG9yYWdlLnByZXR0eS5wYXRoc3ZyAB1hbmFseXNpcy5zdG9yYWdlLkRpc3BsYXlQYXRoc/dES7fD9VEWAgABTAAFcGF0aHNxAH4AHXhwcHNxAH4AqXNyABdqYXZhLnV0aWwuTGlua2VkSGFzaFNldNhs11qV3SoeAgAAeHIAEWphdmEudXRpbC5IYXNoU2V0ukSFlZa4tzQDAAB4cHcMAAAAED9AAAAAAAABc3IAIWFuYWx5c2lzLnN0b3JhZ2UuRGlzcGxheVBhdGgkUm9vdNNzoL2Z0DxyAgACTAAEYmFzZXQAHkxhbmFseXNpcy9zdG9yYWdlL0Rpc3BsYXlQYXRoO0wABG5hbWVxAH4AMnhyABxhbmFseXNpcy5zdG9yYWdlLkRpc3BsYXlQYXRoT0Bj6lbSIAUCAAB4cHB0AAhmdXR1cmVfQXhzcQB+AEBxAH4ARnQAFXRhYy5zdG9yYWdlLmJpdC13aWR0aHEAfgBKcHNxAH4ASQAAAQBwc3EAfgBAcQB+AEZ0AAt0YWMuc3RvcmFnZXZxAH4ADHBxAH4AD3NxAH4AQHEAfgBGdAAYdGFjLmRlY29tcC1p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"}
		AnnotationCmd JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageGlobalChangeSnippet.StorageBackupPoint","calleeTxId":3}}
		NopCmd
		AssumeExpCmd LAnd(Eq(tacCalldatasize!!1:1 0x64 ) Eq(tacCalldatasize!!1:1 0x64 ) )
		AssignExpCmd B153:34 Eq(Select(tacCalldatabuf!!8@3:72 0x0 ) 0x3842f77600000000000000000000000000000000000000000000000000000000 )
		AssumeCmd B153:34
		AssignExpCmd tacCalldatabuf!!154@3:7 LongStore(tacCalldatabuf!!8@3:72 0x4 tacMCANON2!!211:4 0x124 Sub(0x64 0x4 ) )
		LabelCmd "Start procedure Curve-get_D(uint256[2],uint256)"
		AnnotationCmd JSON{"key":{"name":"fps.free-pointer-is-scalarized","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true}
		AssignExpCmd R155:34 Select(tacExtcodesize!!3:2 Apply(to_skey:bif R17:43) )
		NopCmd
		AssumeExpCmd Gt(R155:34 0x0 )
		AnnotationCmd JSON{"key":{"name":"internal.func.finder.info","type":"analysis.ip.InternalFunctionFinderReport","erasureStrategy":"Erased"},"value":"rO0ABXNyAChhbmFseXNpcy5pcC5JbnRlcm5hbEZ1bmN0aW9uRmluZGVyUmVwb3J0ian+bYn1VdACAAFMABN1bnJlc29sdmVkRnVuY3Rpb25zdAAPTGphdmEvdXRpbC9TZXQ7eHBzcgAhZGF0YXN0cnVjdHVyZXMuTGlua2VkQXJyYXlIYXNoU2V0AAAAAAAAAAEDAAJGAApsb2FkRmFjdG9yTAAJaGFzaFRhYmxldAAuTGRhdGFzdHJ1Y3R1cmVzL2FycmF5aGFzaHRhYmxlL0FycmF5SGFzaFRhYmxlO3hwdwgAAAAAQAAAAHg="}
		AnnotationCmd JSON{"key":{"name":"fps.free-pointer-is-scalarized","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true}
		NopCmd
		AssumeExpCmd LNot(Lt(tacCalldatasize!!1:1 0x4 ) )
		NopCmd
		AssumeExpCmd Gt(0x82c63066 tacSighash!!20:19 )
		NopCmd
		AssumeExpCmd Eq(0x3842f776 tacSighash!!20:19 )
		AssignExpCmd:73 R161:74 Sub(tacCalldatasize!!1:1 0x4 )
		AssignExpCmd B162:63 Slt(R161:74 0x60 )
		NopCmd
		AssumeExpCmd LNot(B162:63 )
		NopCmd
		AssumeExpCmd Slt(0x23 tacCalldatasize!!1:75 )
		AssignExpCmd:76 R166:77 0x80
		AssumeCmd:78 true
		AssignExpCmd B167:79 Gt(0x44 tacCalldatasize!!1:75 )
		NopCmd
		AssumeExpCmd LNot(B167:79 )
		AnnotationCmd JSON{"key":{"name":"dsa.assign.start","type":"java.lang.String","erasureStrategy":"Erased"},"value":"4280_1005_0_0_0_0 -> 4282_1004_0_0_0_0"}
		LabelCmd "Parallel assignment for R3573:bv256, R3574:bv256 := R2326:bv256, R3653:bv256"
		AnnotationCmd JSON{"key":{"name":"dsa.assign.end","type":"java.lang.String","erasureStrategy":"Erased"},"value":"4280_1005_0_0_0_0 -> 4282_1004_0_0_0_0"}
		AnnotationCmd JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.LoopSnippet.StartLoopSnippet","loopIndex":1,"loopSource":"unknown loop source code"}}
		AnnotationCmd JSON{"key":{"name":"start_loop.cmd","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		AnnotationCmd JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.LoopSnippet.StartIter","iteration":1}}
		AssignExpCmd:80 R169:81 Select(tacCalldatabuf!!154@3:72 0x4 )
		AssignExpCmd:82 tacMCANON3!!170:5 Store(tacMCANON3!!6:5 0x80 R169:81 )
		AnnotationCmd JSON{"key":{"name":"dsa.assign.start","type":"java.lang.String","erasureStrategy":"Erased"},"value":"4301_1002_0_0_0_0 -> 4282_1004_0_0_0_0"}
		LabelCmd "Parallel assignment for R3573:bv256, R3574:bv256 := R3566:bv256, R3570:bv256"
		AnnotationCmd JSON{"key":{"name":"dsa.assign.end","type":"java.lang.String","erasureStrategy":"Erased"},"value":"4301_1002_0_0_0_0 -> 4282_1004_0_0_0_0"}
		AnnotationCmd JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.LoopSnippet.EndIter","iteration":1}}
		AnnotationCmd JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.LoopSnippet.StartIter","iteration":2}}
		AssignExpCmd:80 R171:81 Select(tacCalldatabuf!!154@3:72 0x24 )
		AssignExpCmd:82 tacMCANON3!!172:5 Store(tacMCANON3!!170:5 0xa0 R171:81 )
		AnnotationCmd JSON{"key":{"name":"dsa.assign.start","type":"java.lang.String","erasureStrategy":"Erased"},"value":"4301_1002_0_0_0_0 -> 4282_1004_0_0_0_0"}
		LabelCmd "Parallel assignment for R3573:bv256, R3574:bv256 := R3566:bv256, R3570:bv256"
		AnnotationCmd JSON{"key":{"name":"dsa.assign.end","type":"java.lang.String","erasureStrategy":"Erased"},"value":"4301_1002_0_0_0_0 -> 4282_1004_0_0_0_0"}
		AnnotationCmd JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.LoopSnippet.EndIter","iteration":2}}
		AnnotationCmd JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.LoopSnippet.EndLoopSnippet","loopId":1}}
		AnnotationCmd JSON{"key":{"name":"end_loop.cmd","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		AnnotationCmd JSON{"key":{"name":"pta.end-allocation","type":"analysis.alloc.AllocationAnalysis$AbstractLocation","erasureStrategy":"Erased"},"value":{"prevFPWriteIdx":0,"nextFPWriteCmd":{"block":{"#class":"tac.BlockIdentifier","origStartPc":4102,"stkTop":1000,"decompCopy":0,"calleeIdx":0,"topOfStackValue":0,"freshCopy":0},"pos":1},"sort":{"#class":"analysis.alloc.AllocationAnalysis.Alloc.ConstBlock","sz":"40"}}}
		AssignExpCmd:80 R173:83 Select(tacCalldatabuf!!154@3:72 0x44 )
		AnnotationCmd JSON{"key":{"name":"internal.func.start","type":"analysis.ip.InternalFuncStartAnnotation","erasureStrategy":"CallTrace"},"value":{"id":4,"startPc":558,"args":[{"s":{"namePrefix":"R166","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1001}]},"offset":1,"sort":"SCALAR"},{"s":{"namePrefix":"R173","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1012}]},"offset":2,"sort":"SCALAR"}],"methodSignature":{"#class":"spec.cvlast.QualifiedMethodSignature.QualifiedMethodSig","qualifiedMethodName":{"#class":"spec.cvlast.QualifiedFunction","host":{"name":"Curve"},"methodId":"get_D"},"params":[{"#class":"spec.cvlast.VMParam.Named","name":"xp","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$StaticArrayDescriptor","location":"memory","elementType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256},"numElements":"2"}},{"#class":"spec.cvlast.VMParam.Named","name":"amp","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256}}],"res":[{"#class":"spec.cvlast.VMParam.Unnamed","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256}}]},"stackOffsetToArgPos":{"1":0,"2":1},"callSiteSrc":{"source":1,"begin":2956,"len":1542,"jumpType":"ENTER","address":"ce4604a000000000000000000000000c","sourceContext":{"indexToFilepath":{"0":"contracts/Context.sol","1":"contracts/Curve.sol","2":"contracts/CurveToken.sol","3":"contracts/CurveTokenExample.sol","4":"contracts/ERC20.sol","5":"contracts/IERC20.sol","6":"contracts/IERC20Metadata.sol","7":"contracts/ReentrancyGuard.sol"},"sourceDir":".post_autofinders.0"}}}}
		AssignExpCmd:84 R174:63 Select(tacMCANON3!!172:5 0xa0 )
		AssignExpCmd:85 R175:74 Select(tacMCANON3!!172:5 0x80 )
		NopCmd
		AssumeExpCmd Apply(add_noofl:bif R175:74 R174:63)
		NopCmd
		NopCmd
		NopCmd
		AssignExpCmd R181:66 Apply(safe_math_narrow:bif IntAdd(Apply(safe_math_promotion:bif R175:74) Apply(safe_math_promotion:bif R174:63)))
		AnnotationCmd JSON{"key":{"name":"internal.func.end","type":"analysis.ip.InternalFuncExitAnnotation","erasureStrategy":"Canonical"},"value":{"id":4,"rets":[{"s":{"namePrefix":"R181","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1023}]},"offset":0}],"functionLayout":{"0":{"#class":"analysis.ip.InternalFuncValueLocation.Scalar"}}}}
		AnnotationCmd JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.EVMFunctionReturnWrite","returnbufOffset":"0","returnValueSym":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R181","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1023}]},"callIndex":3}}
		AnnotationCmd JSON{"key":{"name":"tac.return.path","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		LabelCmd "End procedure Curve-get_D(uint256[2],uint256)"
		AssignExpCmd tacReturndata!!183:58 Store(tacReturndata!!215:58 0x0 R181:66 )
		AssignExpCmd tacMCANON2!!184:4 Store(tacMCANON2!!211:4 0x120 R181:66 )
		AnnotationCmd JSON{"key":{"name":"call.trace.pop","type":"analysis.icfg.Inliner$CallStack$PopRecord","erasureStrategy":"Canonical"},"value":"rO0ABXNyAClhbmFseXNpcy5pY2ZnLklubGluZXIkQ2FsbFN0YWNrJFBvcFJlY29yZPAPfwSLdCWJAgABSQAIY2FsbGVlSWR4cAAAAAM="}
		JumpCmd 2_0_0_1_0_0
	}
	Block 0_0_0_4_0_0 Succ [3_0_0_1_0_0] {
		AnnotationCmd JSON{"key":{"name":"call.trace.push","type":"analysis.icfg.Inliner$CallStack$PushRecord","erasureStrategy":"Canonical"},"value":"rO0ABXNyACphbmFseXNpcy5pY2ZnLklubGluZXIkQ2FsbFN0YWNrJFB1c2hSZWNvcmSX8+DCTLCH+AIAA0kACGNhbGxlZUlkTAAGY2FsbGVldAATTHZjL2RhdGEvTWV0aG9kUmVmO0wAB3N1bW1hcnl0ABVMdmMvZGF0YS9DYWxsU3VtbWFyeTt4cAAAAARzcgARdmMuZGF0YS5NZXRob2RSZWbJlJTzzU9pGAIAA0wABGF0dHJ0ABdMc2NlbmUvTWV0aG9kQXR0cmlidXRlO0wACmNvbnRyYWN0SWR0ABZMamF2YS9tYXRoL0JpZ0ludGVnZXI7TAAHc2lnSGFzaHQAEExldm0vU2lnaGFzaEludDt4cHNyABxzY2VuZS5NZXRob2RBdHRyaWJ1dGUkQ29tbW9uNHjdebdr9XMCAAB4cgAVc2NlbmUuTWV0aG9kQXR0cmlidXRlcYg2pYWutuUCAAB4cHNyABRqYXZhLm1hdGguQmlnSW50ZWdlcoz8nx+pO/sdAwAGSQAIYml0Q291bnRJAAliaXRMZW5ndGhJABNmaXJzdE5vbnplcm9CeXRlTnVtSQAMbG93ZXN0U2V0Qml0SQAGc2lnbnVtWwAJbWFnbml0dWRldAACW0J4cgAQamF2YS5sYW5nLk51bWJlcoaslR0LlOCLAgAAeHD///////////////7////+AAAAAXVyAAJbQqzzF/gGCFTgAgAAeHAAAAAQzkYEoAAAAAAAAAAAAAAAHnhzcgAOZXZtLlNpZ2hhc2hJbnRUdcqNMXEgeAIAAUwAAW5xAH4ABnhwc3EAfgAM///////////////+/////gAAAAF1cQB+ABAAAAAEGBYN3XhzcgATdmMuZGF0YS5DYWxsU3VtbWFyeZQcmw5vl+FdAgAQSQAJc3VtbWFyeUlkTAAOY2FsbENvbnZlbnRpb250ACZMaW5zdHJ1bWVudGF0aW9uL2NhbGxzL0NhbGxDb252ZW50aW9uO0wACmNhbGxUYXJnZXR0ABpMYW5hbHlzaXMvaWNmZy9DYWxsVGFyZ2V0O0wACGNhbGxUeXBldAAVTHZjL2RhdGEvVEFDQ2FsbFR5cGU7TAAPY2Fubm90QmVJbmxpbmVkdAAtTGFuYWx5c2lzL2ljZmcvSW5saW5lciRJbGxlZ2FsSW5saW5pbmdSZWFzb247TAAGZ2FzVmFydAATTHZjL2RhdGEvVEFDU3ltYm9sO0wABmluQmFzZXEAfgAbTAAIaW5PZmZzZXRxAH4AG0wABmluU2l6ZXEAfgAbTAAMb3JpZ0NhbGxjb3JldAAgTHZjL2RhdGEvVEFDQ21kJFNpbXBsZSRDYWxsQ29yZTtMAAdvdXRCYXNlcQB+ABtMAAlvdXRPZmZzZXRxAH4AG0wAB291dFNpemVxAH4AG0wADXNpZ1Jlc29sdXRpb250AA9MamF2YS91dGlsL1NldDtMAAV0b1ZhcnEAfgAbTAAIdmFsdWVWYXJxAH4AG3hwAAAAAnNyACRpbnN0cnVtZW50YXRpb24uY2FsbHMuQ2FsbENvbnZlbnRpb25HtO1ulL788QIAA0kACGNhbGxlcklkTAAFaW5wdXR0ABlMYW5hbHlzaXMvaWNmZy9DYWxsSW5wdXQ7TAAGcmF3T3V0dAAiTGluc3RydW1lbnRhdGlvbi9jYWxscy9DYWxsT3V0cHV0O3hwAAAAAHNyABdhbmFseXNpcy5pY2ZnLkNhbGxJbnB1dJjJD1MhNUxQAgAHTAAHYmFzZVZhcnQAGUx2Yy9kYXRhL1RBQ0V4cHIkU3ltJFZhcjtMABBlbmNvZGVkQXJndW1lbnRzdAAjTGFuYWx5c2lzL2ljZmcvQUJJQXJndW1lbnRFbmNvZGluZztMABNpbnB1dFNpemVMb3dlckJvdW5kcQB+AAZMAAZvZmZzZXR0ABVMdmMvZGF0YS9UQUNFeHByJFN5bTtMABRyYW5nZVRvRGVjb21wb3NlZEFyZ3QAD0xqYXZhL3V0aWwvTWFwO0wAEHNpbXBsaWZpZWRPZmZzZXR0ABtMdmMvZGF0YS9UQUNFeHByJFN5bSRDb25zdDtMAARzaXplcQB+ACZ4cHNyABd2Yy5kYXRhLlRBQ0V4cHIkU3ltJFZhcskrg43eGgPnAgACTAABc3QAF0x2Yy9kYXRhL1RBQ1N5bWJvbCRWYXI7TAADdGFndAAJTHRhYy9UYWc7eHIAE3ZjLmRhdGEuVEFDRXhwciRTeW2iVj0S4YSNUAIAAHhyAA92Yy5kYXRhLlRBQ0V4cHJYhGlUu/v+yAIAAHhwc3IANnZjLmRhdGEuVEFDU3ltYm9sJFZhciRXaXRoRGVmYXVsdENhbGxJbmRleCRXaXRoQnl0ZU1hcJ7+oHF4CHAAAgACTAAEbWV0YXQALUxrb3RsaW54L2NvbGxlY3Rpb25zL2ltbXV0YWJsZS9QZXJzaXN0ZW50TWFwO0wACm5hbWVQcmVmaXh0ABJMamF2YS9sYW5nL1N0cmluZzt4cgAVdmMuZGF0YS5UQUNTeW1ib2wkVmFyCYrCGVl9SXYCAAB4cgARdmMuZGF0YS5UQUNTeW1ib2zd3Run/CoWswIAAHhwc3IAJmRhdGFzdHJ1Y3R1cmVzLnRyZWFwLkhhc2hUcmVhcE1hcCROb2Rlf2t9acJIPnQCAANMAANrZXl0ABJMamF2YS9sYW5nL09iamVjdDtMAARuZXh0dAA1TGRhdGFzdHJ1Y3R1cmVzL3RyZWFwL0hhc2hUcmVhcE1hcCRNb3JlS2V5VmFsdWVQYWlycztMAAV2YWx1ZXEAfgA3eHIAIWRhdGFzdHJ1Y3R1cmVzLnRyZWFwLkhhc2hUcmVhcE1hcPMJ/2vt3boKAgAAeHIAHWRhdGFzdHJ1Y3R1cmVzLnRyZWFwLlRyZWFwTWFw46LAyn3v5moCAAB4cgAaZGF0YXN0cnVjdHVyZXMudHJlYXAuVHJlYXA88f21zZwbdQIAAkwABGxlZnR0ABxMZGF0YXN0cnVjdHVyZXMvdHJlYXAvVHJlYXA7TAAFcmlnaHRxAH4APHhwcHNxAH4ANnBzcQB+ADZwcHNyAAt0YWMuTWV0YUtleVF/W3MiCfIZAgADTAAPZXJhc3VyZVN0cmF0ZWd5dAAdTHRhYy9NZXRhS2V5JEVyYXN1cmVTdHJhdGVneTtMAARuYW1lcQB+ADJMAAN0eXB0ABFMamF2YS9sYW5nL0NsYXNzO3hwfnIAG3RhYy5NZXRhS2V5JEVyYXN1cmVTdHJhdGVneQAAAAAAAAAAEgAAeHIADmphdmEubGFuZy5FbnVtAAAAAAAAAAASAAB4cHQACUNhbm9uaWNhbHQAF3RhYy5tZW1vcnkucGFydGl0aW9uLWlkdnIAEWphdmEubGFuZy5JbnRlZ2VyEuKgpPeBhzgCAAFJAAV2YWx1ZXhxAH4ADnBzcQB+AEkAAAACc3EAfgBAcQB+AEZ0ABJUYWMuc3ltYm9sLmtleXdvcmR2cgAQamF2YS5sYW5nLlN0cmluZ6DwpDh6O7NCAgAAeHBwdAAEdGFjTXNxAH4AQHEAfgBGdAANdGFjLmlzLm1lbW9yeXZyACJ0YWMuTWV0YU1hcCRDb21wYW5pb24kTm90aGluZ1ZhbHVl8nsHH85ykpUCAAB4cHBzcQB+AFN0AA90YWNNQ0FOT04yISEyMzdzcgAPdGFjLlRhZyRCeXRlTWFwNb/Ry6GDRgkCAAB4cgALdGFjLlRhZyRNYXABJytzDV3P/QIAAHhyAAd0YWMuVGFnLk9V3gn2xngCAAB4cHBzcQB+AAz///////////////7////+AAAAAXVxAH4AEAAAAAEEeHNxAH4AKnNyADV2Yy5kYXRhLlRBQ1N5bWJvbCRWYXIkV2l0aERlZmF1bHRDYWxsSW5kZXgkV2l0aEJpdDI1NnqsyEgq0drPAgACTAAEbWV0YXEAfgAxTAAKbmFtZVByZWZpeHEAfgAyeHEAfgAzc3EAfgA2c3EAfgA2cHBxAH4ATHB0AAFMcHNxAH4AQHEAfgBGdAAQdGFjLnN0YWNrLmhlaWdodHEAfgBKcHNxAH4ASQAAA/V0AARSMjM4c3IADnRhYy5UYWckQml0MjU2IyLQT+LlKkgCAAB4cQB+AFlzcgARamF2YS51dGlsLkhhc2hNYXAFB9rBwxZg0QMAAkYACmxvYWRGYWN0b3JJAAl0aHJlc2hvbGR4cD9AAAAAAAABdwgAAAACAAAAAXNyAB5hbmFseXNpcy5pY2ZnLlNjcmF0Y2hCeXRlUmFuZ2XBTLaPpUzj2gIAAkwABGZyb21xAH4ABkwAAnRvcQB+AAZ4cHNxAH4ADP///////////////v////4AAAAAdXEAfgAQAAAAAHhzcQB+AAz///////////////7////+AAAAAXVxAH4AEAAAAAEDeHNyAC1hbmFseXNpcy5pY2ZnLkRlY29tcG9zZWRDYWxsSW5wdXRBcmckQ29uc3RhbnSFavLdQafqPQIAA0wAAWN0ABlMdmMvZGF0YS9UQUNTeW1ib2wkQ29uc3Q7TAARY29udHJhY3RSZWZlcmVuY2V0AC9MYW5hbHlzaXMvaWNmZy9DYWxsR3JhcGhCdWlsZGVyJENhbGxlZENvbnRyYWN0O0wADHNjcmF0Y2hSYW5nZXQAIExhbmFseXNpcy9pY2ZnL1NjcmF0Y2hCeXRlUmFuZ2U7eHIAJGFuYWx5c2lzLmljZmcuRGVjb21wb3NlZENhbGxJbnB1dEFy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AH4ATHBxAH4AYnNxAH4AQHEAfgBGdAAWdGFjLnNjYWxhcml6YXRpb24uc29ydHZyABl2Yy5kYXRhLlNjYWxhcml6YXRpb25Tb3J0MM5wneRoDSYCAAB4cHBzcgAgdmMuZGF0YS5TY2FsYXJpemF0aW9uU29ydCRQYWNrZWQuRa0Sk4jk9wIAAkkABXN0YXJ0TAALcGFja2VkU3RhcnR0ABtMdmMvZGF0YS9TY2FsYXJpemF0aW9uU29ydDt4cQB+AO0AAAAAc3IAH3ZjLmRhdGEuU2NhbGFyaXphdGlvblNvcnQkU3BsaXRU/1mn8ceyBQIAAUwAA2lkeHEAfgAGeHEAfgDtc3EAfgAM///////////////+/////gAAAAF1cQB+ABAAAAABDHhzcQB+ADZwc3EAfgA2cHNxAH4ANnBwc3EAfgBAcQB+AEZ0ABx0YWMuc3RvcmFnZS5ub24taW5kZXhlZC1wYXRodnIANWFuYWx5c2lzLnN0b3JhZ2UuU3RvcmFnZUFuYWx5c2lzUmVzdWx0JE5vbkluZGV4ZWRQYXRoCMGgS6H6P0UCAAB4cHBzcgA6YW5hbHlzaXMuc3RvcmFnZS5TdG9yYWdlQW5hbHlzaXNSZXN1bHQkTm9uSW5kZXhlZFBhdGgkUm9vdL839dil6gr/AgABTAAEc2xvdHEAfgAGeHEAfgD7cQB+APRzcQB+AEBxAH4ARnQADXRhYy5zbG90LnR5cGV2cgA6c3BlYy5jdmxhc3QudHlwZWRlc2NyaXB0b3JzLkVWTVR5cGVEZXNjcmlwdG9yJEVWTVZhbHVlVHlwZcaJrwK66rglAgAAeHIALXNwZWMuY3ZsYXN0LnR5cGVkZXNjcmlwdG9ycy5FVk1UeXBlRGVzY3JpcHRvcshRqfE8wmodAgAAeHBwc3IANXNwZWMuY3ZsYXN0LnR5cGVkZXNjcmlwdG9ycy5FVk1UeXBlRGVzY3JpcHRvciRhZGRyZXNzevhl9G+XoCkCAAB4cgBEc3BlYy5jdmxhc3QudHlwZWRlc2NyaXB0b3JzLkVWTVR5cGVEZXNjcmlwdG9yJEVWTUlzb21vcnBoaWNWYWx1ZVR5cGX3dZiRbhChDwIAAHhxAH4BAXNxAH4AQH5xAH4ARHQABkVyYXNlZHQAGHRhYy5zdG9yYWdlLnByZXR0eS5wYXRoc3ZyAB1hbmFseXNpcy5zdG9yYWdlLkRpc3BsYXlQYXRoc/dES7fD9VEWAgABTAAFcGF0aHNxAH4AHXhwcHNxAH4BC3NyABdqYXZhLnV0aWwuTGlua2VkSGFzaFNldNhs11qV3SoeAgAAeHIAEWphdmEudXRpbC5IYXNoU2V0ukSFlZa4tzQDAAB4cHcMAAAAED9AAAAAAAABc3IAIWFuYWx5c2lzLnN0b3JhZ2UuRGlzcGxheVBhdGgkUm9vdNNzoL2Z0DxyAgACTAAEYmFzZXQAHkxhbmFseXNpcy9zdG9yYWdlL0Rpc3BsYXlQYXRoO0wABG5hbWVxAH4AMnhyABxhbmFseXNpcy5zdG9yYWdlLkRpc3BsYXlQYXRoT0Bj6lbSIAUCAAB4cHB0AAhscF90b2tlbnhzcQB+AEBxAH4ARnQAFXRhYy5zdG9yYWdlLmJpdC13aWR0aHEAfgBKcHNxAH4ASQAAAKBwc3EAfgBAcQB+AEZ0AAt0YWMuc3RvcmFnZXZxAH4ADHBxAH4AxnBxAH4AY3BzcQB+AEkAAAP5dAALQ0FOT04yNyEhMTBzcQB+AHdxAH4AaHEAfgBtc3EAfgAwc3EAfgA2cHNxAH4ANnBzcQB+ADZwcHEAfgBDcHEAfgBLcQB+AExwcQB+AFBxAH4AUXBxAH4AVXEAfgBWc3EAfgBec3EAfgA2c3EAfgA2cHBxAH4ATHBxAH4AYnBxAH4AY3BxAH4AjXEAfgBmcQB+AJBzcgAiamF2YS51dGlsLkNvbGxlY3Rpb25zJFNpbmdsZXRvblNldCxSQZgpwLG/AgABTAAHZWxlbWVudHEAfgA3eHBxAH4AFHNxAH4AXnNxAH4ANnNxAH4ANnNxAH4ANnNxAH4ANnBzcQB+ADZwcHEAfgBMcHEAfgBicQB+AOtwcQB+APFzcQB+ADZwc3EAfgA2cHNxAH4ANnBwcQB+APlwcQB+AP5xAH4A/3BxAH4BBnEAfgEHcHNxAH4BC3NxAH4BDncMAAAAED9AAAAAAAABcQB+ARR4cQB+ARZwcQB+ARhwcQB+ARlwcQB+AMZwcQB+AGNwcQB+ARxxAH4BHXNxAH4Ad3EAfgBocQB+AG0="}
		AnnotationCmd JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageGlobalChangeSnippet.StorageBackupPoint","calleeTxId":4}}
		NopCmd
		AssumeExpCmd LAnd(Eq(tacCalldatasize!!2:1 0x4 ) Eq(tacCalldatasize!!2:1 0x4 ) )
		NopCmd
		AssumeExpCmd Eq(tacCalldatabufCANON0@4:0 0x18160ddd00000000000000000000000000000000000000000000000000000000 )
		LabelCmd "Start procedure CurveTokenExample-totalSupply()"
		AnnotationCmd JSON{"key":{"name":"fps.free-pointer-is-scalarized","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true}
		AssignExpCmd R188:34 Select(tacExtcodesize!!3:2 Apply(to_skey:bif R15:86) )
		NopCmd
		AssumeExpCmd Gt(R188:34 0x0 )
		AnnotationCmd JSON{"key":{"name":"internal.func.finder.info","type":"analysis.ip.InternalFunctionFinderReport","erasureStrategy":"Erased"},"value":"rO0ABXNyAChhbmFseXNpcy5pcC5JbnRlcm5hbEZ1bmN0aW9uRmluZGVyUmVwb3J0ian+bYn1VdACAAFMABN1bnJlc29sdmVkRnVuY3Rpb25zdAAPTGphdmEvdXRpbC9TZXQ7eHBzcgAhZGF0YXN0cnVjdHVyZXMuTGlua2VkQXJyYXlIYXNoU2V0AAAAAAAAAAEDAAJGAApsb2FkRmFjdG9yTAAJaGFzaFRhYmxldAAuTGRhdGFzdHJ1Y3R1cmVzL2FycmF5aGFzaHRhYmxlL0FycmF5SGFzaFRhYmxlO3hwdwgAAAAAQAAAAHg="}
		AnnotationCmd JSON{"key":{"name":"fps.free-pointer-is-scalarized","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true}
		NopCmd
		AssumeExpCmd LNot(Lt(tacCalldatasize!!2:1 0x4 ) )
		NopCmd
		AssumeExpCmd Gt(0x40c10f19 tacSighash!!21:19 )
		NopCmd
		AssumeExpCmd LNot(Eq(0x6fdde03 tacSighash!!21:19 ) )
		NopCmd
		AssumeExpCmd LNot(Eq(0x95ea7b3 tacSighash!!21:19 ) )
		NopCmd
		AssumeExpCmd Eq(0x18160ddd tacSighash!!21:19 )
		AnnotationCmd JSON{"key":{"name":"internal.func.start","type":"analysis.ip.InternalFuncStartAnnotation","erasureStrategy":"CallTrace"},"value":{"id":5,"startPc":1205,"args":[],"methodSignature":{"#class":"spec.cvlast.QualifiedMethodSignature.QualifiedMethodSig","qualifiedMethodName":{"#class":"spec.cvlast.QualifiedFunction","host":{"name":"CurveTokenExample"},"methodId":"totalSupply"},"params":[],"res":[{"#class":"spec.cvlast.VMParam.Unnamed","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256}}]},"stackOffsetToArgPos":{},"callSiteSrc":{"source":3,"begin":3954,"len":364,"jumpType":"ENTER","address":"ce4604a000000000000000000000001e","sourceContext":{"indexToFilepath":{"0":"contracts/Context.sol","1":"contracts/CurveToken.sol","2":"contracts/CurveTokenExample.sol","3":"contracts/ERC20.sol","4":"contracts/IERC20.sol","5":"contracts/IERC20Metadata.sol"},"sourceDir":".post_autofinders.1"}}}}
		AnnotationCmd JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet","value":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"CANON79!!12","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.scalarization.sort","type":"vc.data.ScalarizationSort","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.ScalarizationSort.Split","idx":"2"}},{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.storage.bit-width","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":256},{"key":{"name":"tac.storage.pretty.paths","type":"analysis.storage.DisplayPaths","erasureStrategy":"Erased"},"value":{"paths":[{"#class":"analysis.storage.DisplayPath.Root","name":"_totalSupply"}]}},{"key":{"name":"tac.slot.type","type":"spec.cvlast.typedescriptors.EVMTypeDescriptor$EVMValueType","erasureStrategy":"Canonical"},"value":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256}},{"key":{"name":"tac.storage.non-indexed-path","type":"analysis.storage.StorageAnalysisResult$NonIndexedPath","erasureStrategy":"Canonical"},"value":{"#class":"analysis.storage.StorageAnalysisResult.NonIndexedPath.Root","slot":"2"}},{"key":{"name":"tac.storage","type":"java.math.BigInteger","erasureStrategy":"Canonical"},"value":"ce4604a000000000000000000000001e"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1021}]},"displayPath":{"#class":"analysis.storage.DisplayPath.Root","name":"_totalSupply"},"storageType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256},"contractInstance":"ce4604a000000000000000000000001e","linkableStorageReadId":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet.Id","id":4}}}
		AnnotationCmd JSON{"key":{"name":"internal.func.end","type":"analysis.ip.InternalFuncExitAnnotation","erasureStrategy":"Canonical"},"value":{"id":5,"rets":[{"s":{"namePrefix":"CANON79!!12","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.scalarization.sort","type":"vc.data.ScalarizationSort","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.ScalarizationSort.Split","idx":"2"}},{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.storage.bit-width","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":256},{"key":{"name":"tac.storage.pretty.paths","type":"analysis.storage.DisplayPaths","erasureStrategy":"Erased"},"value":{"paths":[{"#class":"analysis.storage.DisplayPath.Root","name":"_totalSupply"}]}},{"key":{"name":"tac.slot.type","type":"spec.cvlast.typedescriptors.EVMTypeDescriptor$EVMValueType","erasureStrategy":"Canonical"},"value":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256}},{"key":{"name":"tac.storage.non-indexed-path","type":"analysis.storage.StorageAnalysisResult$NonIndexedPath","erasureStrategy":"Canonical"},"value":{"#class":"analysis.storage.StorageAnalysisResult.NonIndexedPath.Root","slot":"2"}},{"key":{"name":"tac.storage","type":"java.math.BigInteger","erasureStrategy":"Canonical"},"value":"ce4604a000000000000000000000001e"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1023}]},"offset":0}],"functionLayout":{"0":{"#class":"analysis.ip.InternalFuncValueLocation.Scalar"}}}}
		AnnotationCmd JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.EVMFunctionReturnWrite","returnbufOffset":"0","returnValueSym":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"CANON79!!12","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.scalarization.sort","type":"vc.data.ScalarizationSort","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.ScalarizationSort.Split","idx":"2"}},{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.storage.bit-width","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":256},{"key":{"name":"tac.storage.pretty.paths","type":"analysis.storage.DisplayPaths","erasureStrategy":"Erased"},"value":{"paths":[{"#class":"analysis.storage.DisplayPath.Root","name":"_totalSupply"}]}},{"key":{"name":"tac.slot.type","type":"spec.cvlast.typedescriptors.EVMTypeDescriptor$EVMValueType","erasureStrategy":"Canonical"},"value":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256}},{"key":{"name":"tac.storage.non-indexed-path","type":"analysis.storage.StorageAnalysisResult$NonIndexedPath","erasureStrategy":"Canonical"},"value":{"#class":"analysis.storage.StorageAnalysisResult.NonIndexedPath.Root","slot":"2"}},{"key":{"name":"tac.storage","type":"java.math.BigInteger","erasureStrategy":"Canonical"},"value":"ce4604a000000000000000000000001e"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1023}]},"callIndex":4}}
		AnnotationCmd JSON{"key":{"name":"tac.return.path","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		LabelCmd "End procedure CurveTokenExample-totalSupply()"
		AssignExpCmd tacReturndata!!197:58 Store(tacReturndata!!240:58 0x0 CANON79!!12:87 )
		AssignExpCmd tacMCANON2!!198:4 Store(tacMCANON2!!237:4 0x140 CANON79!!12:87 )
		AnnotationCmd JSON{"key":{"name":"call.trace.pop","type":"analysis.icfg.Inliner$CallStack$PopRecord","erasureStrategy":"Canonical"},"value":"rO0ABXNyAClhbmFseXNpcy5pY2ZnLklubGluZXIkQ2FsbFN0YWNrJFBvcFJlY29yZPAPfwSLdCWJAgABSQAIY2FsbGVlSWR4cAAAAAQ="}
		JumpCmd 3_0_0_1_0_0
	}
	Block 1_0_0_1_0_0 Succ [0_0_0_3_0_0] {
		AssumeNotCmd:54 false
		AnnotationCmd JSON{"key":{"name":"pta.fake-return.start","type":"analysis.CmdPointer","erasureStrategy":"Erased"},"value":{"block":{"#class":"tac.BlockIdentifier","origStartPc":1608,"stkTop":1007,"decompCopy":0,"calleeIdx":0,"topOfStackValue":2,"freshCopy":0},"pos":1}}
		AnnotationCmd JSON{"key":{"name":"pta.fake-return.end","type":"analysis.CmdPointer","erasureStrategy":"Erased"},"value":{"block":{"#class":"tac.BlockIdentifier","origStartPc":1608,"stkTop":1007,"decompCopy":0,"calleeIdx":0,"topOfStackValue":2,"freshCopy":0},"pos":6}}
		AssumeNotCmd:88 false
		AssignExpCmd:89 R199:77 Select(tacMCANON2!!150:4 0x100 )
		NopCmd
		AssumeExpCmd LNot(Lt(R199:77 R117:52 ) )
		AssignExpCmd:90 R201:49 Sub(R199:77 R117:52 )
		AssignExpCmd:50 tacMCANON1!!202:3 Store(tacMCANON1!!116:3 0xe0 R201:49 )
		AnnotationCmd JSON{"key":{"name":"pta.end-allocation","type":"analysis.alloc.AllocationAnalysis$AbstractLocation","erasureStrategy":"Erased"},"value":{"prevFPWriteIdx":1,"nextFPWriteCmd":{"block":{"#class":"tac.BlockIdentifier","origStartPc":16,"stkTop":1024,"decompCopy":0,"calleeIdx":0,"topOfStackValue":2,"freshCopy":0},"pos":44},"sort":{"#class":"analysis.alloc.AllocationAnalysis.Alloc.ConstBlock","sz":"40"}}}
		AnnotationCmd JSON{"key":{"name":"internal.func.start","type":"analysis.ip.InternalFuncStartAnnotation","erasureStrategy":"CallTrace"},"value":{"id":3,"startPc":3822,"args":[],"methodSignature":{"#class":"spec.cvlast.QualifiedMethodSignature.QualifiedMethodSig","qualifiedMethodName":{"#class":"spec.cvlast.QualifiedFunction","host":{"name":"Curve"},"methodId":"_A"},"params":[],"res":[{"#class":"spec.cvlast.VMParam.Unnamed","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256}}]},"stackOffsetToArgPos":{},"callSiteSrc":{"source":1,"begin":6351,"len":4,"jumpType":"ENTER","address":"ce4604a000000000000000000000000c","sourceContext":{"indexToFilepath":{"0":"contracts/Context.sol","1":"contracts/Curve.sol","2":"contracts/CurveToken.sol","3":"contracts/CurveTokenExample.sol","4":"contracts/ERC20.sol","5":"contracts/IERC20.sol","6":"contracts/IERC20Metadata.sol","7":"contracts/ReentrancyGuard.sol"},"sourceDir":".post_autofinders.0"}}}}
		AnnotationCmd JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet","value":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"CANON94!!14","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.scalarization.sort","type":"vc.data.ScalarizationSort","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.ScalarizationSort.Split","idx":"5"}},{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.storage.bit-width","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":256},{"key":{"name":"tac.storage.pretty.paths","type":"analysis.storage.DisplayPaths","erasureStrategy":"Erased"},"value":{"paths":[{"#class":"analysis.storage.DisplayPath.Root","name":"future_A"}]}},{"key":{"name":"tac.slot.type","type":"spec.cvlast.typedescriptors.EVMTypeDescriptor$EVMValueType","erasureStrategy":"Canonical"},"value":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256}},{"key":{"name":"tac.storage.non-indexed-path","type":"analysis.storage.StorageAnalysisResult$NonIndexedPath","erasureStrategy":"Canonical"},"value":{"#class":"analysis.storage.StorageAnalysisResult.NonIndexedPath.Root","slot":"5"}},{"key":{"name":"tac.storage","type":"java.math.BigInteger","erasureStrategy":"Canonical"},"value":"ce4604a000000000000000000000000c"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1013}]},"displayPath":{"#class":"analysis.storage.DisplayPath.Root","name":"future_A"},"storageType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256},"contractInstance":"ce4604a000000000000000000000000c","linkableStorageReadId":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet.Id","id":2}}}
		AnnotationCmd JSON{"key":{"name":"internal.func.end","type":"analysis.ip.InternalFuncExitAnnotation","erasureStrategy":"Canonical"},"value":{"id":3,"rets":[{"s":{"namePrefix":"CANON94!!14","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.scalarization.sort","type":"vc.data.ScalarizationSort","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.ScalarizationSort.Split","idx":"5"}},{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.storage.bit-width","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":256},{"key":{"name":"tac.storage.pretty.paths","type":"analysis.storage.DisplayPaths","erasureStrategy":"Erased"},"value":{"paths":[{"#class":"analysis.storage.DisplayPath.Root","name":"future_A"}]}},{"key":{"name":"tac.slot.type","type":"spec.cvlast.typedescriptors.EVMTypeDescriptor$EVMValueType","erasureStrategy":"Canonical"},"value":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256}},{"key":{"name":"tac.storage.non-indexed-path","type":"analysis.storage.StorageAnalysisResult$NonIndexedPath","erasureStrategy":"Canonical"},"value":{"#class":"analysis.storage.StorageAnalysisResult.NonIndexedPath.Root","slot":"5"}},{"key":{"name":"tac.storage","type":"java.math.BigInteger","erasureStrategy":"Canonical"},"value":"ce4604a000000000000000000000000c"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1015}]},"offset":0}],"functionLayout":{"0":{"#class":"analysis.ip.InternalFuncValueLocation.Scalar"}}}}
		AssignExpCmd:91 tacMCANON2!!205:4 Store(tacMCANON2!!150:4 0x120 0x3842f77600000000000000000000000000000000000000000000000000000000 )
		AnnotationCmd JSON{"key":{"name":"dsa.assign.start","type":"java.lang.String","erasureStrategy":"Erased"},"value":"4639_1007_0_0_0_0 -> 4643_1005_0_0_0_0"}
		LabelCmd "Parallel assignment for R4170:bv256, R4207:bv256, B4208:bool, R4209:bv256 := R6282:bv256, R365:bv256, B4072:bool, R4073:bv256"
		AnnotationCmd JSON{"key":{"name":"dsa.assign.end","type":"java.lang.String","erasureStrategy":"Erased"},"value":"4639_1007_0_0_0_0 -> 4643_1005_0_0_0_0"}
		AnnotationCmd JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.LoopSnippet.StartLoopSnippet","loopIndex":0,"loopSource":"unknown loop source code"}}
		AnnotationCmd JSON{"key":{"name":"start_loop.cmd","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		AnnotationCmd JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.LoopSnippet.StartIter","iteration":1}}
		AssignExpCmd:92 R206:79 Select(tacMCANON1!!202:3 0xc0 )
		AssignExpCmd:93 tacMCANON2!!207:4 Store(tacMCANON2!!205:4 0x124 R206:79 )
		AnnotationCmd JSON{"key":{"name":"dsa.assign.start","type":"java.lang.String","erasureStrategy":"Erased"},"value":"4674_1003_0_0_0_0 -> 4643_1005_0_0_0_0"}
		LabelCmd "Parallel assignment for R4170:bv256, R4207:bv256, B4208:bool, R4209:bv256 := R3940:bv256, R3983:bv256, B4205:bool, R4202:bv256"
		AnnotationCmd JSON{"key":{"name":"dsa.assign.end","type":"java.lang.String","erasureStrategy":"Erased"},"value":"4674_1003_0_0_0_0 -> 4643_1005_0_0_0_0"}
		AnnotationCmd JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.LoopSnippet.EndIter","iteration":1}}
		AnnotationCmd JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.LoopSnippet.StartIter","iteration":2}}
		AssignExpCmd:92 R208:79 Select(tacMCANON1!!202:3 0xe0 )
		AssignExpCmd:93 tacMCANON2!!209:4 Store(tacMCANON2!!207:4 0x144 R208:79 )
		AnnotationCmd JSON{"key":{"name":"dsa.assign.start","type":"java.lang.String","erasureStrategy":"Erased"},"value":"4674_1003_0_0_0_0 -> 4643_1005_0_0_0_0"}
		LabelCmd "Parallel assignment for R4170:bv256, R4207:bv256, B4208:bool, R4209:bv256 := R3940:bv256, R3983:bv256, B4205:bool, R4202:bv256"
		AnnotationCmd JSON{"key":{"name":"dsa.assign.end","type":"java.lang.String","erasureStrategy":"Erased"},"value":"4674_1003_0_0_0_0 -> 4643_1005_0_0_0_0"}
		AnnotationCmd JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.LoopSnippet.EndIter","iteration":2}}
		AnnotationCmd JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.LoopSnippet.EndLoopSnippet","loopId":0}}
		AnnotationCmd JSON{"key":{"name":"end_loop.cmd","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		AssignExpCmd:94 tacMCANON2!!211:4 Store(tacMCANON2!!209:4 0x164 CANON94!!14:95 )
		AssignExpCmd:91 R212:96 0x120
		NopCmd
		AssignHavocCmd:91 R214:45
		AssignHavocCmd tacReturndata!!215:58
		JumpCmd 0_0_0_3_0_0
	}
	Block 3_0_0_1_0_0 Succ [4_0_0_0_0_0] {
		AssumeNotCmd:97 false
		AnnotationCmd JSON{"key":{"name":"pta.fake-return.start","type":"analysis.CmdPointer","erasureStrategy":"Erased"},"value":{"block":{"#class":"tac.BlockIdentifier","origStartPc":3278,"stkTop":1014,"decompCopy":0,"calleeIdx":0,"topOfStackValue":2,"freshCopy":0},"pos":1}}
		AnnotationCmd JSON{"key":{"name":"pta.fake-return.end","type":"analysis.CmdPointer","erasureStrategy":"Erased"},"value":{"block":{"#class":"tac.BlockIdentifier","origStartPc":3278,"stkTop":1014,"decompCopy":0,"calleeIdx":0,"topOfStackValue":2,"freshCopy":0},"pos":6}}
		AssumeNotCmd:88 false
		AssignExpCmd:89 R216:98 Select(tacMCANON2!!198:4 0x140 )
		NopCmd
		AssumeExpCmd Apply(mul_noofl:bif R231:47 0x8ac7230489e80000)
		NopCmd
		AssignExpCmd:99 I225:34 IntMul(Apply(safe_math_promotion:bif R231:47) 0x8ac7230489e80000)
		NopCmd
		NopCmd
		AssumeExpCmd Gt(R216:98 0x0 )
		AssignExpCmd:100 R228:66 Div(Apply(safe_math_narrow:bif I225:34) R216:98 )
		AnnotationCmd JSON{"key":{"name":"internal.func.end","type":"analysis.ip.InternalFuncExitAnnotation","erasureStrategy":"Canonical"},"value":{"id":1,"rets":[{"s":{"namePrefix":"R228","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1021}]},"offset":0}],"functionLayout":{"0":{"#class":"analysis.ip.InternalFuncValueLocation.Scalar"}}}}
		AnnotationCmd JSON{"key":{"name":"internal.func.end","type":"analysis.ip.InternalFuncExitAnnotation","erasureStrategy":"Canonical"},"value":{"id":0,"rets":[{"s":{"namePrefix":"R228","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1023}]},"offset":0}],"functionLayout":{"0":{"#class":"analysis.ip.InternalFuncValueLocation.Scalar"}}}}
		AnnotationCmd JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.EVMFunctionReturnWrite","returnbufOffset":"0","returnValueSym":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R228","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1023}]},"callIndex":1}}
		AnnotationCmd JSON{"key":{"name":"tac.return.path","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		LabelCmd "End procedure Curve-func1_caller()"
		AssignExpCmd lastReverted:101 false
		JumpCmd 4_0_0_0_0_0
	}
	Block 2_0_0_1_0_0 Succ [0_0_0_4_0_0] {
		AssumeNotCmd:91 false
		AnnotationCmd JSON{"key":{"name":"pta.fake-return.start","type":"analysis.CmdPointer","erasureStrategy":"Erased"},"value":{"block":{"#class":"tac.BlockIdentifier","origStartPc":3129,"stkTop":1015,"decompCopy":0,"calleeIdx":0,"topOfStackValue":2,"freshCopy":0},"pos":1}}
		AnnotationCmd JSON{"key":{"name":"pta.fake-return.end","type":"analysis.CmdPointer","erasureStrategy":"Erased"},"value":{"block":{"#class":"tac.BlockIdentifier","origStartPc":3129,"stkTop":1015,"decompCopy":0,"calleeIdx":0,"topOfStackValue":2,"freshCopy":0},"pos":6}}
		AssumeNotCmd:88 false
		AssignExpCmd:89 R231:47 Select(tacMCANON2!!184:4 0x120 )
		AssignExpCmd B233:34 Le(CANON27!!10:102 0xffffffffffffffffffffffffffffffffffffffff )
		AssignExpCmd B234:34 Ge(CANON27!!10:102 0x0 )
		NopCmd
		AssumeExpCmd LAnd(B233:34 B234:34 )
		AnnotationCmd JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet","value":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"CANON27!!10","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.scalarization.sort","type":"vc.data.ScalarizationSort","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.ScalarizationSort.Packed","packedStart":{"#class":"vc.data.ScalarizationSort.Split","idx":"c"},"start":0}},{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.storage.bit-width","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":160},{"key":{"name":"tac.storage.pretty.paths","type":"analysis.storage.DisplayPaths","erasureStrategy":"Erased"},"value":{"paths":[{"#class":"analysis.storage.DisplayPath.Root","name":"lp_token"}]}},{"key":{"name":"tac.slot.type","type":"spec.cvlast.typedescriptors.EVMTypeDescriptor$EVMValueType","erasureStrategy":"Canonical"},"value":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.address"}},{"key":{"name":"tac.storage.non-indexed-path","type":"analysis.storage.StorageAnalysisResult$NonIndexedPath","erasureStrategy":"Canonical"},"value":{"#class":"analysis.storage.StorageAnalysisResult.NonIndexedPath.Root","slot":"c"}},{"key":{"name":"tac.storage","type":"java.math.BigInteger","erasureStrategy":"Canonical"},"value":"ce4604a000000000000000000000000c"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1016}]},"displayPath":{"#class":"analysis.storage.DisplayPath.Root","name":"lp_token"},"storageType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.address"},"contractInstance":"ce4604a000000000000000000000000c","linkableStorageReadId":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet.Id","id":3}}}
		AnnotationCmd JSON{"key":{"name":"init.reorder.fence","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		AssignExpCmd:97 tacMCANON2!!237:4 Store(tacMCANON2!!184:4 0x140 0x18160ddd00000000000000000000000000000000000000000000000000000000 )
		AssignExpCmd:97 R238:66 0x140
		AssignHavocCmd:97 R239:47
		AssignHavocCmd tacReturndata!!240:58
		JumpCmd 0_0_0_4_0_0
	}
}
Axioms {
}
Metas {
  "0": [
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
          "callIndex": 1,
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
      "value": "0"
    },
    {
      "key": {
        "name": "tac.scalarization.sort",
        "type": "vc.data.ScalarizationSort",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.ScalarizationSort.Split",
        "idx": "0"
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
      "value": "0"
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
  "1": [
    {
      "key": {
        "name": "Tac.symbol.keyword",
        "type": "java.lang.String",
        "erasureStrategy": "Canonical"
      },
      "value": "tacCalldatasize"
    }
  ],
  "2": [
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
  "3": [
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
  "4": [
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
      "value": 2
    }
  ],
  "5": [
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
      "value": 3
    }
  ],
  "6": [
    {
      "key": {
        "name": "Tac.symbol.keyword",
        "type": "java.lang.String",
        "erasureStrategy": "Canonical"
      },
      "value": "tacBalance"
    }
  ],
  "7": [
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
        "name": "Tac.symbol.keyword",
        "type": "java.lang.String",
        "erasureStrategy": "Canonical"
      },
      "value": "tacCalldatabuf"
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
  "8": [
    {
      "key": {
        "name": "tac.scalarization.sort",
        "type": "vc.data.ScalarizationSort",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.ScalarizationSort.Packed",
        "packedStart": {
          "#class": "vc.data.ScalarizationSort.Split",
          "idx": "b"
        },
        "start": 0
      }
    },
    {
      "key": {
        "name": "tac.storage.bit-width",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 160
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
            "name": "coins_1"
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
        "#class": "spec.cvlast.typedescriptors.EVMTypeDescriptor.address"
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
        "slot": "b"
      }
    },
    {
      "key": {
        "name": "tac.storage",
        "type": "java.math.BigInteger",
        "erasureStrategy": "Canonical"
      },
      "value": "ce4604a000000000000000000000000c"
    }
  ],
  "9": [
    {
      "key": {
        "name": "tac.scalarization.sort",
        "type": "vc.data.ScalarizationSort",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.ScalarizationSort.Packed",
        "packedStart": {
          "#class": "vc.data.ScalarizationSort.Split",
          "idx": "c"
        },
        "start": 0
      }
    },
    {
      "key": {
        "name": "tac.storage.bit-width",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 160
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
            "name": "lp_token"
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
        "#class": "spec.cvlast.typedescriptors.EVMTypeDescriptor.address"
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
        "slot": "c"
      }
    },
    {
      "key": {
        "name": "tac.storage",
        "type": "java.math.BigInteger",
        "erasureStrategy": "Canonical"
      },
      "value": "ce4604a000000000000000000000000c"
    }
  ],
  "10": [
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
      "value": "fcalldataarg"
    }
  ],
  "11": [
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
      "value": "fcalldataarg"
    }
  ],
  "12": [
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
          "#class": "analysis.storage.StorageAnalysisResult.NonIndexedPath.StaticArrayAccess",
          "base": {
            "#class": "analysis.storage.StorageAnalysisResult.NonIndexedPath.Root",
            "slot": "8"
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
      "value": "ce4604a000000000000000000000000c"
    }
  ],
  "13": [
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
      "value": "ce4604a000000000000000000000001e"
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
      "value": "ce4604a0000000000000000000000027"
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
        "#class": "vc.data.ScalarizationSort.Split",
        "idx": "5"
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
            "name": "future_A"
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
        "slot": "5"
      }
    },
    {
      "key": {
        "name": "tac.storage",
        "type": "java.math.BigInteger",
        "erasureStrategy": "Canonical"
      },
      "value": "ce4604a000000000000000000000000c"
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
      "value": "CurveTokenExample"
    },
    {
      "key": {
        "name": "tac.contract.sym.addr",
        "type": "java.math.BigInteger",
        "erasureStrategy": "Erased"
      },
      "value": "ce4604a000000000000000000000001e"
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
      "value": "ce4604a0000000000000000000000027"
    }
  ],
  "18": [
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
      "value": "Curve"
    },
    {
      "key": {
        "name": "tac.contract.sym.addr",
        "type": "java.math.BigInteger",
        "erasureStrategy": "Erased"
      },
      "value": "ce4604a000000000000000000000000c"
    }
  ],
  "19": [
    {
      "key": {
        "name": "Tac.symbol.keyword",
        "type": "java.lang.String",
        "erasureStrategy": "Canonical"
      },
      "value": "tacSighash"
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
  "25": [
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
  "26": [
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
      "value": "fenv.msg.sender"
    }
  ],
  "27": [
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
      "value": "fenv.msg.value"
    }
  ],
  "28": [
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
      "value": "fenv.tx.origin"
    }
  ],
  "29": [
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
      "value": "fenv.block.coinbase"
    }
  ],
  "30": [
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
      "value": "fenv.block.difficulty"
    }
  ],
  "31": [
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
      "value": "fenv.block.gaslimit"
    }
  ],
  "32": [
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
      "value": "fenv.block.number"
    }
  ],
  "33": [
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
      "value": "fenv.block.timestamp"
    }
  ],
  "34": [
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
  "35": [
    {
      "key": {
        "name": "cvl.range",
        "type": "spec.cvlast.CVLRange",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "spec.cvlast.CVLRange.Range",
        "specFile": "certora/specs/BuiltinViewReentrancy.spec",
        "end": {
          "character": 32
        }
      }
    }
  ],
  "36": [
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
          "callIndex": 1,
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
        "name": "Tac.symbol.keyword",
        "type": "java.lang.String",
        "erasureStrategy": "Canonical"
      },
      "value": "tacCalldatabuf"
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
  "37": [
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
  "38": [
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
  "39": [
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
  "40": [
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
  "41": [
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
  "42": [
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
        "specFile": "certora/specs/BuiltinViewReentrancy.spec",
        "end": {
          "character": 32
        }
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
      "value": "Curve"
    },
    {
      "key": {
        "name": "tac.contract.sym.addr",
        "type": "java.math.BigInteger",
        "erasureStrategy": "Erased"
      },
      "value": "ce4604a000000000000000000000000c"
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
        "source": 1,
        "begin": 5879,
        "len": 17,
        "jumpType": "REGULAR",
        "address": "ce4604a000000000000000000000000c",
        "sourceContext": {
          "indexToFilepath": {
            "0": "contracts/Context.sol",
            "1": "contracts/Curve.sol",
            "2": "contracts/CurveToken.sol",
            "3": "contracts/CurveTokenExample.sol",
            "4": "contracts/ERC20.sol",
            "5": "contracts/IERC20.sol",
            "6": "contracts/IERC20Metadata.sol",
            "7": "contracts/ReentrancyGuard.sol"
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
              "#class": "analysis.storage.StorageAnalysisResult.NonIndexedPath.StaticArrayAccess",
              "base": {
                "#class": "analysis.storage.StorageAnalysisResult.NonIndexedPath.Root",
                "slot": "8"
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
      "value": 1010
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
        "source": 1,
        "begin": 5855,
        "len": 21,
        "jumpType": "REGULAR",
        "address": "ce4604a000000000000000000000000c",
        "sourceContext": {
          "indexToFilepath": {
            "0": "contracts/Context.sol",
            "1": "contracts/Curve.sol",
            "2": "contracts/CurveToken.sol",
            "3": "contracts/CurveTokenExample.sol",
            "4": "contracts/ERC20.sol",
            "5": "contracts/IERC20.sol",
            "6": "contracts/IERC20Metadata.sol",
            "7": "contracts/ReentrancyGuard.sol"
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
      "value": 1009
    }
  ],
  "48": [
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
  "49": [
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
  "50": [
    {
      "key": {
        "name": "tac.meta",
        "type": "vc.data.TACMetaInfo",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "source": 1,
        "begin": 5834,
        "len": 145,
        "jumpType": "REGULAR",
        "address": "ce4604a000000000000000000000000c",
        "sourceContext": {
          "indexToFilepath": {
            "0": "contracts/Context.sol",
            "1": "contracts/Curve.sol",
            "2": "contracts/CurveToken.sol",
            "3": "contracts/CurveTokenExample.sol",
            "4": "contracts/ERC20.sol",
            "5": "contracts/IERC20.sol",
            "6": "contracts/IERC20Metadata.sol",
            "7": "contracts/ReentrancyGuard.sol"
          },
          "sourceDir": ".post_autofinders.0"
        }
      }
    }
  ],
  "51": [
    {
      "key": {
        "name": "tac.meta",
        "type": "vc.data.TACMetaInfo",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "source": 1,
        "begin": 5961,
        "len": 17,
        "jumpType": "REGULAR",
        "address": "ce4604a000000000000000000000000c",
        "sourceContext": {
          "indexToFilepath": {
            "0": "contracts/Context.sol",
            "1": "contracts/Curve.sol",
            "2": "contracts/CurveToken.sol",
            "3": "contracts/CurveTokenExample.sol",
            "4": "contracts/ERC20.sol",
            "5": "contracts/IERC20.sol",
            "6": "contracts/IERC20Metadata.sol",
            "7": "contracts/ReentrancyGuard.sol"
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
              "#class": "analysis.storage.StorageAnalysisResult.NonIndexedPath.StaticArrayAccess",
              "base": {
                "#class": "analysis.storage.StorageAnalysisResult.NonIndexedPath.Root",
                "slot": "8"
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
  "52": [
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
  "53": [
    {
      "key": {
        "name": "tac.scalarization.sort",
        "type": "vc.data.ScalarizationSort",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.ScalarizationSort.Packed",
        "packedStart": {
          "#class": "vc.data.ScalarizationSort.Split",
          "idx": "b"
        },
        "start": 0
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
      "value": 160
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
            "name": "coins_1"
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
        "#class": "spec.cvlast.typedescriptors.EVMTypeDescriptor.address"
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
        "slot": "b"
      }
    },
    {
      "key": {
        "name": "tac.storage",
        "type": "java.math.BigInteger",
        "erasureStrategy": "Canonical"
      },
      "value": "ce4604a000000000000000000000000c"
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
  "54": [
    {
      "key": {
        "name": "tac.meta",
        "type": "vc.data.TACMetaInfo",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "source": 1,
        "begin": 5919,
        "len": 39,
        "jumpType": "REGULAR",
        "address": "ce4604a000000000000000000000000c",
        "sourceContext": {
          "indexToFilepath": {
            "0": "contracts/Context.sol",
            "1": "contracts/Curve.sol",
            "2": "contracts/CurveToken.sol",
            "3": "contracts/CurveTokenExample.sol",
            "4": "contracts/ERC20.sol",
            "5": "contracts/IERC20.sol",
            "6": "contracts/IERC20Metadata.sol",
            "7": "contracts/ReentrancyGuard.sol"
          },
          "sourceDir": ".post_autofinders.0"
        }
      }
    }
  ],
  "55": [
    {
      "key": {
        "name": "tac.meta",
        "type": "vc.data.TACMetaInfo",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "source": 8,
        "begin": 6816,
        "len": 37,
        "jumpType": "REGULAR",
        "address": "ce4604a000000000000000000000000c",
        "sourceContext": {
          "indexToFilepath": {
            "0": "contracts/Context.sol",
            "1": "contracts/Curve.sol",
            "2": "contracts/CurveToken.sol",
            "3": "contracts/CurveTokenExample.sol",
            "4": "contracts/ERC20.sol",
            "5": "contracts/IERC20.sol",
            "6": "contracts/IERC20Metadata.sol",
            "7": "contracts/ReentrancyGuard.sol"
          },
          "sourceDir": ".post_autofinders.0"
        }
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
      "value": "L"
    },
    {
      "key": {
        "name": "tac.stack.height",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 1006
    }
  ],
  "57": [
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
      "value": 1002
    }
  ],
  "58": [
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
  "59": [
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
          "callIndex": 1,
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
  "60": [
    {
      "key": {
        "name": "tac.decomp-inscalar.sort",
        "type": "tac.DecomposedInputScalarSort",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "tac.DecomposedInputScalarSort.Simple",
        "byteOffset": "4"
      }
    },
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
      "value": "Curve"
    },
    {
      "key": {
        "name": "tac.contract.sym.addr",
        "type": "java.math.BigInteger",
        "erasureStrategy": "Erased"
      },
      "value": "ce4604a000000000000000000000000c"
    }
  ],
  "61": [
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
      "value": "ce4604a0000000000000000000000027"
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
        "source": 4,
        "begin": 4984,
        "len": 23,
        "jumpType": "REGULAR",
        "address": "ce4604a0000000000000000000000027",
        "sourceContext": {
          "indexToFilepath": {
            "0": "contracts/Context.sol",
            "1": "contracts/ERC20.sol",
            "2": "contracts/IERC20.sol",
            "3": "contracts/IERC20Metadata.sol"
          },
          "sourceDir": ".post_autofinders.2"
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
      "value": 1017
    }
  ],
  "64": [
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
  "65": [
    {
      "key": {
        "name": "tac.meta",
        "type": "vc.data.TACMetaInfo",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "source": 4,
        "begin": 2157,
        "len": 20,
        "jumpType": "REGULAR",
        "address": "ce4604a0000000000000000000000027",
        "sourceContext": {
          "indexToFilepath": {
            "0": "contracts/Context.sol",
            "1": "contracts/ERC20.sol",
            "2": "contracts/IERC20.sol",
            "3": "contracts/IERC20Metadata.sol"
          },
          "sourceDir": ".post_autofinders.2"
        }
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
      "value": 1013
    }
  ],
  "67": [
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
  "68": [
    {
      "key": {
        "name": "tac.meta",
        "type": "vc.data.TACMetaInfo",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "source": 1,
        "begin": 4818,
        "len": 18,
        "jumpType": "REGULAR",
        "address": "ce4604a0000000000000000000000027",
        "sourceContext": {
          "indexToFilepath": {
            "0": "contracts/Context.sol",
            "1": "contracts/ERC20.sol",
            "2": "contracts/IERC20.sol",
            "3": "contracts/IERC20Metadata.sol"
          },
          "sourceDir": ".post_autofinders.2"
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
        "name": "tac.stack.height",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 1020
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
        "source": 1,
        "begin": 4818,
        "len": 18,
        "jumpType": "REGULAR",
        "address": "ce4604a0000000000000000000000027",
        "sourceContext": {
          "indexToFilepath": {
            "0": "contracts/Context.sol",
            "1": "contracts/ERC20.sol",
            "2": "contracts/IERC20.sol",
            "3": "contracts/IERC20Metadata.sol"
          },
          "sourceDir": ".post_autofinders.2"
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
              "namePrefix": "R141",
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
                "namePrefix": "R141",
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
                "namePrefix": "CANON103",
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
                "namePrefix": "CANON102",
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
          "namePrefix": "tacCalldatasize!!1",
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
        "name": "Tac.symbol.keyword",
        "type": "java.lang.String",
        "erasureStrategy": "Canonical"
      },
      "value": "tacCalldatabuf"
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
        "name": "tac.meta",
        "type": "vc.data.TACMetaInfo",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "source": 8,
        "begin": 3060,
        "len": 23,
        "jumpType": "REGULAR",
        "address": "ce4604a000000000000000000000000c",
        "sourceContext": {
          "indexToFilepath": {
            "0": "contracts/Context.sol",
            "1": "contracts/Curve.sol",
            "2": "contracts/CurveToken.sol",
            "3": "contracts/CurveTokenExample.sol",
            "4": "contracts/ERC20.sol",
            "5": "contracts/IERC20.sol",
            "6": "contracts/IERC20Metadata.sol",
            "7": "contracts/ReentrancyGuard.sol"
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
      "value": 1016
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
      "value": 1021
    }
  ],
  "76": [
    {
      "key": {
        "name": "tac.meta",
        "type": "vc.data.TACMetaInfo",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "source": 8,
        "begin": 67,
        "len": 9,
        "jumpType": "REGULAR",
        "address": "ce4604a000000000000000000000000c",
        "sourceContext": {
          "indexToFilepath": {
            "0": "contracts/Context.sol",
            "1": "contracts/Curve.sol",
            "2": "contracts/CurveToken.sol",
            "3": "contracts/CurveTokenExample.sol",
            "4": "contracts/ERC20.sol",
            "5": "contracts/IERC20.sol",
            "6": "contracts/IERC20Metadata.sol",
            "7": "contracts/ReentrancyGuard.sol"
          },
          "sourceDir": ".post_autofinders.0"
        }
      }
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
      "value": 1001
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
        "source": 8,
        "begin": 907,
        "len": 88,
        "jumpType": "REGULAR",
        "address": "ce4604a000000000000000000000000c",
        "sourceContext": {
          "indexToFilepath": {
            "0": "contracts/Context.sol",
            "1": "contracts/Curve.sol",
            "2": "contracts/CurveToken.sol",
            "3": "contracts/CurveTokenExample.sol",
            "4": "contracts/ERC20.sol",
            "5": "contracts/IERC20.sol",
            "6": "contracts/IERC20Metadata.sol",
            "7": "contracts/ReentrancyGuard.sol"
          },
          "sourceDir": ".post_autofinders.0"
        }
      }
    },
    {
      "key": {
        "name": "optimization.pruning.branch",
        "type": "analysis.controlflow.InfeasibleBranchPruning$BranchCondition",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "conditionVar": {
          "namePrefix": "LCANON56",
          "tag": {
            "#class": "tac.Tag.Bool"
          },
          "callIndex": 3,
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
              "value": 999
            }
          ]
        },
        "takenBranch": true
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
      "value": 1004
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
        "source": 8,
        "begin": 1833,
        "len": 20,
        "jumpType": "REGULAR",
        "address": "ce4604a000000000000000000000000c",
        "sourceContext": {
          "indexToFilepath": {
            "0": "contracts/Context.sol",
            "1": "contracts/Curve.sol",
            "2": "contracts/CurveToken.sol",
            "3": "contracts/CurveTokenExample.sol",
            "4": "contracts/ERC20.sol",
            "5": "contracts/IERC20.sol",
            "6": "contracts/IERC20Metadata.sol",
            "7": "contracts/ReentrancyGuard.sol"
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
      "value": 998
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
        "source": 8,
        "begin": 2468,
        "len": 50,
        "jumpType": "REGULAR",
        "address": "ce4604a000000000000000000000000c",
        "sourceContext": {
          "indexToFilepath": {
            "0": "contracts/Context.sol",
            "1": "contracts/Curve.sol",
            "2": "contracts/CurveToken.sol",
            "3": "contracts/CurveTokenExample.sol",
            "4": "contracts/ERC20.sol",
            "5": "contracts/IERC20.sol",
            "6": "contracts/IERC20Metadata.sol",
            "7": "contracts/ReentrancyGuard.sol"
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
      "value": 1012
    }
  ],
  "84": [
    {
      "key": {
        "name": "tac.meta",
        "type": "vc.data.TACMetaInfo",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "source": 1,
        "begin": 3683,
        "len": 5,
        "jumpType": "REGULAR",
        "address": "ce4604a000000000000000000000000c",
        "sourceContext": {
          "indexToFilepath": {
            "0": "contracts/Context.sol",
            "1": "contracts/Curve.sol",
            "2": "contracts/CurveToken.sol",
            "3": "contracts/CurveTokenExample.sol",
            "4": "contracts/ERC20.sol",
            "5": "contracts/IERC20.sol",
            "6": "contracts/IERC20Metadata.sol",
            "7": "contracts/ReentrancyGuard.sol"
          },
          "sourceDir": ".post_autofinders.0"
        }
      }
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
        "source": 1,
        "begin": 3675,
        "len": 5,
        "jumpType": "REGULAR",
        "address": "ce4604a000000000000000000000000c",
        "sourceContext": {
          "indexToFilepath": {
            "0": "contracts/Context.sol",
            "1": "contracts/Curve.sol",
            "2": "contracts/CurveToken.sol",
            "3": "contracts/CurveTokenExample.sol",
            "4": "contracts/ERC20.sol",
            "5": "contracts/IERC20.sol",
            "6": "contracts/IERC20Metadata.sol",
            "7": "contracts/ReentrancyGuard.sol"
          },
          "sourceDir": ".post_autofinders.0"
        }
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
      "value": "CurveTokenExample"
    },
    {
      "key": {
        "name": "tac.contract.sym.addr",
        "type": "java.math.BigInteger",
        "erasureStrategy": "Erased"
      },
      "value": "ce4604a000000000000000000000001e"
    }
  ],
  "87": [
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
      "value": "ce4604a000000000000000000000001e"
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
  "88": [
    {
      "key": {
        "name": "tac.meta",
        "type": "vc.data.TACMetaInfo",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "source": 8,
        "begin": 9679,
        "len": 119,
        "jumpType": "REGULAR",
        "address": "ce4604a000000000000000000000000c",
        "sourceContext": {
          "indexToFilepath": {
            "0": "contracts/Context.sol",
            "1": "contracts/Curve.sol",
            "2": "contracts/CurveToken.sol",
            "3": "contracts/CurveTokenExample.sol",
            "4": "contracts/ERC20.sol",
            "5": "contracts/IERC20.sol",
            "6": "contracts/IERC20Metadata.sol",
            "7": "contracts/ReentrancyGuard.sol"
          },
          "sourceDir": ".post_autofinders.0"
        }
      }
    }
  ],
  "89": [
    {
      "key": {
        "name": "tac.meta",
        "type": "vc.data.TACMetaInfo",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "source": 8,
        "begin": 9525,
        "len": 13,
        "jumpType": "REGULAR",
        "address": "ce4604a000000000000000000000000c",
        "sourceContext": {
          "indexToFilepath": {
            "0": "contracts/Context.sol",
            "1": "contracts/Curve.sol",
            "2": "contracts/CurveToken.sol",
            "3": "contracts/CurveTokenExample.sol",
            "4": "contracts/ERC20.sol",
            "5": "contracts/IERC20.sol",
            "6": "contracts/IERC20Metadata.sol",
            "7": "contracts/ReentrancyGuard.sol"
          },
          "sourceDir": ".post_autofinders.0"
        }
      }
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
        "source": 8,
        "begin": 9422,
        "len": 9,
        "jumpType": "REGULAR",
        "address": "ce4604a000000000000000000000000c",
        "sourceContext": {
          "indexToFilepath": {
            "0": "contracts/Context.sol",
            "1": "contracts/Curve.sol",
            "2": "contracts/CurveToken.sol",
            "3": "contracts/CurveTokenExample.sol",
            "4": "contracts/ERC20.sol",
            "5": "contracts/IERC20.sol",
            "6": "contracts/IERC20Metadata.sol",
            "7": "contracts/ReentrancyGuard.sol"
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
  "91": [
    {
      "key": {
        "name": "tac.meta",
        "type": "vc.data.TACMetaInfo",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "source": 1,
        "begin": 6327,
        "len": 29,
        "jumpType": "REGULAR",
        "address": "ce4604a000000000000000000000000c",
        "sourceContext": {
          "indexToFilepath": {
            "0": "contracts/Context.sol",
            "1": "contracts/Curve.sol",
            "2": "contracts/CurveToken.sol",
            "3": "contracts/CurveTokenExample.sol",
            "4": "contracts/ERC20.sol",
            "5": "contracts/IERC20.sol",
            "6": "contracts/IERC20Metadata.sol",
            "7": "contracts/ReentrancyGuard.sol"
          },
          "sourceDir": ".post_autofinders.0"
        }
      }
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
        "source": 8,
        "begin": 5461,
        "len": 13,
        "jumpType": "REGULAR",
        "address": "ce4604a000000000000000000000000c",
        "sourceContext": {
          "indexToFilepath": {
            "0": "contracts/Context.sol",
            "1": "contracts/Curve.sol",
            "2": "contracts/CurveToken.sol",
            "3": "contracts/CurveTokenExample.sol",
            "4": "contracts/ERC20.sol",
            "5": "contracts/IERC20.sol",
            "6": "contracts/IERC20Metadata.sol",
            "7": "contracts/ReentrancyGuard.sol"
          },
          "sourceDir": ".post_autofinders.0"
        }
      }
    }
  ],
  "93": [
    {
      "key": {
        "name": "tac.meta",
        "type": "vc.data.TACMetaInfo",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "source": 8,
        "begin": 4578,
        "len": 37,
        "jumpType": "REGULAR",
        "address": "ce4604a000000000000000000000000c",
        "sourceContext": {
          "indexToFilepath": {
            "0": "contracts/Context.sol",
            "1": "contracts/Curve.sol",
            "2": "contracts/CurveToken.sol",
            "3": "contracts/CurveTokenExample.sol",
            "4": "contracts/ERC20.sol",
            "5": "contracts/IERC20.sol",
            "6": "contracts/IERC20Metadata.sol",
            "7": "contracts/ReentrancyGuard.sol"
          },
          "sourceDir": ".post_autofinders.0"
        }
      }
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
        "source": 8,
        "begin": 3538,
        "len": 37,
        "jumpType": "REGULAR",
        "address": "ce4604a000000000000000000000000c",
        "sourceContext": {
          "indexToFilepath": {
            "0": "contracts/Context.sol",
            "1": "contracts/Curve.sol",
            "2": "contracts/CurveToken.sol",
            "3": "contracts/CurveTokenExample.sol",
            "4": "contracts/ERC20.sol",
            "5": "contracts/IERC20.sol",
            "6": "contracts/IERC20Metadata.sol",
            "7": "contracts/ReentrancyGuard.sol"
          },
          "sourceDir": ".post_autofinders.0"
        }
      }
    }
  ],
  "95": [
    {
      "key": {
        "name": "tac.scalarization.sort",
        "type": "vc.data.ScalarizationSort",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.ScalarizationSort.Split",
        "idx": "5"
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
            "name": "future_A"
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
        "slot": "5"
      }
    },
    {
      "key": {
        "name": "tac.storage",
        "type": "java.math.BigInteger",
        "erasureStrategy": "Canonical"
      },
      "value": "ce4604a000000000000000000000000c"
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
      "value": 1014
    }
  ],
  "97": [
    {
      "key": {
        "name": "tac.meta",
        "type": "vc.data.TACMetaInfo",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "source": 1,
        "begin": 6388,
        "len": 29,
        "jumpType": "REGULAR",
        "address": "ce4604a000000000000000000000000c",
        "sourceContext": {
          "indexToFilepath": {
            "0": "contracts/Context.sol",
            "1": "contracts/Curve.sol",
            "2": "contracts/CurveToken.sol",
            "3": "contracts/CurveTokenExample.sol",
            "4": "contracts/ERC20.sol",
            "5": "contracts/IERC20.sol",
            "6": "contracts/IERC20Metadata.sol",
            "7": "contracts/ReentrancyGuard.sol"
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
      "value": 1008
    }
  ],
  "99": [
    {
      "key": {
        "name": "tac.meta",
        "type": "vc.data.TACMetaInfo",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "source": 8,
        "begin": 8848,
        "len": 9,
        "jumpType": "REGULAR",
        "address": "ce4604a000000000000000000000000c",
        "sourceContext": {
          "indexToFilepath": {
            "0": "contracts/Context.sol",
            "1": "contracts/Curve.sol",
            "2": "contracts/CurveToken.sol",
            "3": "contracts/CurveTokenExample.sol",
            "4": "contracts/ERC20.sol",
            "5": "contracts/IERC20.sol",
            "6": "contracts/IERC20Metadata.sol",
            "7": "contracts/ReentrancyGuard.sol"
          },
          "sourceDir": ".post_autofinders.0"
        }
      }
    }
  ],
  "100": [
    {
      "key": {
        "name": "tac.meta",
        "type": "vc.data.TACMetaInfo",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "source": 8,
        "begin": 9225,
        "len": 9,
        "jumpType": "REGULAR",
        "address": "ce4604a000000000000000000000000c",
        "sourceContext": {
          "indexToFilepath": {
            "0": "contracts/Context.sol",
            "1": "contracts/Curve.sol",
            "2": "contracts/CurveToken.sol",
            "3": "contracts/CurveTokenExample.sol",
            "4": "contracts/ERC20.sol",
            "5": "contracts/IERC20.sol",
            "6": "contracts/IERC20Metadata.sol",
            "7": "contracts/ReentrancyGuard.sol"
          },
          "sourceDir": ".post_autofinders.0"
        }
      }
    }
  ],
  "101": [
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
  "102": [
    {
      "key": {
        "name": "tac.scalarization.sort",
        "type": "vc.data.ScalarizationSort",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.ScalarizationSort.Packed",
        "packedStart": {
          "#class": "vc.data.ScalarizationSort.Split",
          "idx": "c"
        },
        "start": 0
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
      "value": 160
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
            "name": "lp_token"
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
        "#class": "spec.cvlast.typedescriptors.EVMTypeDescriptor.address"
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
        "slot": "c"
      }
    },
    {
      "key": {
        "name": "tac.storage",
        "type": "java.math.BigInteger",
        "erasureStrategy": "Canonical"
      },
      "value": "ce4604a000000000000000000000000c"
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
}