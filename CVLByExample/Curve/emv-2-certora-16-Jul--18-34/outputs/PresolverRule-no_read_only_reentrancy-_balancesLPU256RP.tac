TACSymbolTable {
	UserDefined {
		UninterpSort skey
	}
	BuiltinFunctions {
		to_skey:JSON{"#class":"vc.data.TACBuiltInFunction.Hash.ToSkey"}
		add_noofl:JSON{"#class":"vc.data.TACBuiltInFunction.NoAddOverflowCheck"}
		safe_math_narrow:JSON{"#class":"vc.data.TACBuiltInFunction.SafeMathNarrow"}
		skey_basic:JSON{"#class":"vc.data.TACBuiltInFunction.Hash.Basic"}
		hash_3_keccak:JSON{"#class":"vc.data.TACBuiltInFunction.Hash.SimpleHashApplication","arity":3,"hashFamily":{"#class":"vc.data.HashFamily.Keccack"}}
		safe_math_promotion:JSON{"#class":"vc.data.TACBuiltInFunction.SafeMathPromotion"}
		mul_noofl:JSON{"#class":"vc.data.TACBuiltInFunction.NoMulOverflowCheck"}
	}
	UninterpretedFunctions {
		B22:JSON{"name":"B22","paramSorts":[],"returnSort":{"#class":"tac.Tag.Bool"},"attribute":"Ghost","cvlResultType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"},"cvlParamTypes":[],"declarationName":"CANON37"}
		CANON105:JSON{"name":"CANON105","paramSorts":[],"returnSort":{"#class":"tac.Tag.Int"},"attribute":"Ghost","cvlResultType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256},"cvlParamTypes":[],"declarationName":"CANON105"}
		CANON109:JSON{"name":"CANON109","paramSorts":[],"returnSort":{"#class":"tac.Tag.Int"},"attribute":"Ghost","cvlResultType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256},"cvlParamTypes":[],"declarationName":"CANON109"}
		CANON37:JSON{"name":"CANON37","paramSorts":[],"returnSort":{"#class":"tac.Tag.Bool"},"attribute":"Ghost","cvlResultType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"},"cvlParamTypes":[],"declarationName":"CANON37"}
		CANON39:JSON{"name":"CANON39","paramSorts":[],"returnSort":{"#class":"tac.Tag.Int"},"attribute":"Ghost","cvlResultType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256},"cvlParamTypes":[],"declarationName":"CANON39"}
		I23:JSON{"name":"I23","paramSorts":[],"returnSort":{"#class":"tac.Tag.Int"},"attribute":"Ghost","cvlResultType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256},"cvlParamTypes":[],"declarationName":"CANON39"}
		I8:JSON{"name":"I8","paramSorts":[],"returnSort":{"#class":"tac.Tag.Int"},"attribute":"Ghost","cvlResultType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256},"cvlParamTypes":[],"declarationName":"CANON105"}
	}
	tacM0x40@1:bv256
	tacM0x40@7:bv256
	tacMCANON1!!10:bytemap
	tacMCANON2!!11:bytemap
	tacMCANON2!!12:bytemap
	tacMCANON3!!13:bytemap
	tacMCANON3!!14:bytemap
	tacNonce:wordmap
	tacMCANON5!!15:bytemap
	tacCaller@1:bv256
	tacCaller@5:bv256
	tacCaller@7:bv256
	tacMCANON2!!151:bytemap
	tacMCANON2!!153:bytemap
	tacMCANON2!!178:bytemap
	tacMCANON2!!212:bytemap
	tacMCANON2!!226:bytemap
	tacMCANON2!!294:bytemap
	tacMCANON2!!296:bytemap
	tacMCANON2!!321:bytemap
	tacMCANON2!!355:bytemap
	tacMCANON2!!369:bytemap
	tacMCANON2!!376:bytemap
	tacMCANON2!!378:bytemap
	tacMCANON2!!380:bytemap
	tacMCANON2!!382:bytemap
	tacMCANON2!!393:bytemap
	tacMCANON2!!395:bytemap
	tacMCANON2!!397:bytemap
	tacMCANON2!!399:bytemap
	tacMCANON2!!440:bytemap
	tacMCANON2!!450:bytemap
	tacCalldatabufCANON0@2:bv256
	tacCalldatabufCANON0@4:bv256
	tacCalldatabufCANON0@6:bv256
	tacCalldatabufCANON0@8:bv256
	tacCalldatabufCANON0@10:bv256
	tacCalldatabufCANON1@2:bv256
	tacCalldatabufCANON1@6:bv256
	tacCalldatabufCANON1@8:bv256
	tacMCANON6!!16:bytemap
	tacMCANON1!!9:bytemap
	tacOrigNonceCANON0:wordmap
	tacOrigNonceCANON1:wordmap
	tacOrigNonceCANON2:wordmap
	CANON87!!25:bv256
	tacAddress!!97:bv256
	tacMCANON4havocme5358@5:bytemap
	tacOrigin!!101:bv256
	tacOrigin!!244:bv256
	tacOrigin!!481:bv256
	tacCallvalue@1:bv256
	tacCallvalue@5:bv256
	tacCallvalue@7:bv256
	lastReverted:bool
	lastReverted@1:bool
	lastReverted@2:bool
	lastReverted@3:bool
	lastReverted@4:bool
	lastReverted@5:bool
	lastReverted@6:bool
	lastReverted@7:bool
	lastReverted@8:bool
	lastReverted@9:bool
	lastReverted@10:bool
	tacM0x0!!173:bv256
	tacM0x0!!316:bv256
	tacM0x0!!555:bv256
	tacExtcodesize!!7:wordmap
	tacCalldatasize@1:bv256
	tacCalldatasize@2:bv256
	tacCalldatasize@3:bv256
	tacCalldatasize@4:bv256
	tacCalldatasize@5:bv256
	tacCalldatasize@6:bv256
	tacCalldatasize@7:bv256
	tacCalldatasize@8:bv256
	tacCalldatasize@9:bv256
	tacCalldatasize@10:bv256
	tacReturndata@1:bytemap
	tacReturndata@5:bytemap
	tacReturndata@7:bytemap
	tacReturnsize@1:bv256
	tacReturnsize@5:bv256
	tacReturnsize@7:bv256
	tacCalldatasize!!227:bv256
	tacCalldatasize!!462:bv256
	tacMCANON3!!198:bytemap
	tacMCANON3!!200:bytemap
	tacMCANON3!!341:bytemap
	tacMCANON3!!343:bytemap
	tacCallvalue!!95:bv256
	CANON93!!26:wordmap
	tacCalldatabuf!!18@3:bytemap
	tacCalldatabuf!!19@9:bytemap
	tacM0x0@2:bv256
	tacM0x0@6:bv256
	tacM0x0@8:bv256
	tacRC@1:bv256
	tacRC@5:bv256
	tacRC@7:bv256
	CANON241!!508:bool
	CANON99!!27:bv256
	tacExtcodesize:wordmap
	CANON100:bv256
	CANON101:bv256
	CANON102:bv256
	CANON103:bv256
	CANON104:int
	CANON105:int
	CANON106:int
	CANON107:bool
	CANON108:int
	CANON109:int
	CANON110@1:bool
	CANON110@5:bool
	CANON110@7:bool
	CANON111:bool
	CANON112:bool
	CANON115@2:bv256
	CANON115@3:bv256
	CANON115@4:bv256
	CANON115@6:bv256
	CANON115@8:bv256
	CANON115@9:bv256
	CANON115@10:bv256
	CANON116@1:bv256
	CANON116@7:bv256
	CANON117@1:bv256
	CANON117@7:bv256
	CANON118:int
	CANON119:int
	CANON120:bool
	CANON121:int
	CANON122:bool
	CANON123:bool
	CANON124:bool
	CANON125:bool
	CANON126:bool
	CANON127:bool
	CANON128:int
	CANON129:int
	CANON130:int
	CANON131@1:bool
	CANON131@7:bool
	CANON132@1:bool
	CANON132@7:bool
	CANON133@1:bool
	CANON133@7:bool
	CANON134@1:bv256
	CANON134@7:bv256
	CANON135:bool
	CANON136:int
	CANON137:int
	CANON138:int
	CANON139@1:bool
	CANON139@7:bool
	CANON140:int
	CANON141:bool
	CANON142:int
	CANON143:int
	CANON144:int
	CANON145:int
	CANON146:int
	CANON147:bytemap
	CANON148:bytemap
	CANON149:bv256
	CANON150:bv256
	CANON151:bytemap
	CANON153:bv256
	CANON154:bool
	CANON155:bool
	CANON156:int
	CANON157:bool
	CANON158:bv256
	CANON159:int
	CANON160:bool
	CANON161:bv256
	CANON162:int
	CANON163:bool
	CANON164:bv256
	CANON165:int
	CANON166:bool
	CANON167:bv256
	CANON168:int
	CANON169:bool
	CANON170:bv256
	CANON171:int
	CANON172:bool
	CANON173:bv256
	CANON174:int
	CANON175:bool
	CANON176:bv256
	CANON177@5:bool
	CANON178@5:bool
	CANON179@5:bool
	CANON180@5:bv256
	CANON181@5:bv256
	CANON182:int
	CANON183:int
	CANON184:bool
	CANON185:int
	CANON186:bool
	CANON187:bool
	CANON188:int
	CANON189:int
	CANON190:int
	CANON191:int
	CANON192:int
	CANON193:int
	CANON194:bool
	CANON195:bool
	CANON196:int
	CANON197:bool
	CANON198:bv256
	CANON199:int
	CANON200:bool
	CANON201:bv256
	CANON202:int
	CANON203:bool
	CANON204:bv256
	CANON205:int
	CANON206:bool
	CANON207:bv256
	CANON208:int
	CANON209:bool
	CANON210:bv256
	CANON211:int
	CANON212:bool
	CANON213:bv256
	CANON214:int
	CANON215:bool
	CANON216:bv256
	CANON217:int
	CANON218:int
	CANON219:bool
	CANON220:int
	CANON221:bool
	CANON222:bool
	CANON223:int
	CANON224:int
	CANON225:bool
	CANON226:int
	CANON227:bool
	CANON228:bool
	CANON229:bool
	CANON230:bool
	CANON231:bool
	CANON232:bool
	CANON233:int
	CANON234:int
	CANON235:int
	CANON236:bool
	CANON237:int
	CANON238:int
	CANON239:int
	CANON240:int
	CANON241:bool
	CANON242:bool
	tacCalldatasize!!84:bv256
	tacMCANON0havocme5356@1:bytemap
	tacMCANON0havocme5357@7:bytemap
	tacMCANON0@1:bytemap
	tacMCANON0@7:bytemap
	tacMCANON1@1:bytemap
	tacMCANON1@7:bytemap
	tacMCANON2@1:bytemap
	tacMCANON2@7:bytemap
	tacMCANON3@3:bytemap
	tacMCANON3@9:bytemap
	tacMCANON4@5:bytemap
	tacMCANON5@5:bytemap
	tacMCANON6@5:bytemap
	tacBalance:wordmap
	tacTimestamp!!111:bv256
	tacTimestamp!!254:bv256
	tacTimestamp!!491:bv256
	tacBalance!!17:wordmap
	tacNumber@1:bv256
	tacNumber@5:bv256
	tacNumber@7:bv256
	tacCalldatabuf@1:bytemap
	tacCalldatabuf@3:bytemap
	tacCalldatabuf@5:bytemap
	tacCalldatabuf@7:bytemap
	tacCalldatabuf@9:bytemap
	I8:int
	B22:bool
	B41:bool
	B42:bool
	B43:bool
	B44:bool
	B45:bool
	B46:bool
	B47:bool
	B48:bool
	B49:bool
	B51:bool
	B53:bool
	B55:bool
	B56:bool
	B57:bool
	B58:bool
	B59:bool
	B60:bool
	B61:bool
	B62:bool
	B63:bool
	B64:bool
	B65:bool
	B66:bool
	B67:bool
	B68:bool
	B69:bool
	B70:bool
	B71:bool
	B72:bool
	B73:bool
	B74:bool
	B75:bool
	B76:bool
	B77:bool
	B85:bool
	B86:bool
	B88:bool
	B91:bool
	B93:bool
	B96:bool
	B99:bool
	I23:int
	I78:int
	I79:int
	I80:int
	I81:int
	I82:int
	I83:int
	I87:int
	I92:int
	I98:int
	R28:bv256
	R29:bv256
	R30:bv256
	R50:bv256
	R52:bv256
	R54:bv256
	R89:bv256
	R94:bv256
	B102:bool
	B104:bool
	B107:bool
	B109:bool
	B112:bool
	B114:bool
	B117:bool
	B126:bool
	B129:bool
	B130:bool
	B131:bool
	B132:bool
	B133:bool
	B134:bool
	B135:bool
	B136:bool
	B137:bool
	B138:bool
	B142:bool
	B147:bool
	B148:bool
	B149:bool
	B158:bool
	B159:bool
	B161:bool
	B162:bool
	B163:bool
	B164:bool
	B165:bool
	B167:bool
	B168:bool
	B170:bool
	B171:bool
	B180:bool
	B181:bool
	B184:bool
	B185:bool
	B186:bool
	B187:bool
	B190:bool
	B191:bool
	B192:bool
	B193:bool
	B195:bool
	B196:bool
	B205:bool
	B214:bool
	B215:bool
	B217:bool
	B218:bool
	B219:bool
	B220:bool
	B221:bool
	B222:bool
	B228:bool
	B229:bool
	B231:bool
	B234:bool
	B236:bool
	B239:bool
	B242:bool
	B245:bool
	B247:bool
	B250:bool
	B252:bool
	B255:bool
	B257:bool
	B260:bool
	B269:bool
	B272:bool
	B273:bool
	B274:bool
	B275:bool
	B276:bool
	B277:bool
	B278:bool
	B279:bool
	B280:bool
	B281:bool
	B285:bool
	B290:bool
	B291:bool
	B292:bool
	B301:bool
	B302:bool
	B304:bool
	B305:bool
	B306:bool
	B307:bool
	B308:bool
	B310:bool
	B311:bool
	B313:bool
	B314:bool
	B323:bool
	B324:bool
	B327:bool
	B328:bool
	B329:bool
	B330:bool
	B333:bool
	B334:bool
	B335:bool
	B336:bool
	B338:bool
	B339:bool
	B348:bool
	B357:bool
	B358:bool
	B360:bool
	B361:bool
	B362:bool
	B363:bool
	B364:bool
	B365:bool
	B371:bool
	B388:bool
	B406:bool
	B408:bool
	B409:bool
	B411:bool
	B415:bool
	B421:bool
	B423:bool
	B424:bool
	B426:bool
	B430:bool
	B436:bool
	B437:bool
	B438:bool
	B446:bool
	B447:bool
	B448:bool
	B465:bool
	B466:bool
	B468:bool
	B471:bool
	B473:bool
	B476:bool
	B479:bool
	B482:bool
	B484:bool
	B487:bool
	B489:bool
	B492:bool
	B494:bool
	B497:bool
	B506:bool
	B509:bool
	B511:bool
	B512:bool
	B513:bool
	B514:bool
	B515:bool
	B516:bool
	B518:bool
	B522:bool
	B524:bool
	B529:bool
	B530:bool
	B531:bool
	B540:bool
	B541:bool
	B543:bool
	B544:bool
	B545:bool
	B546:bool
	B547:bool
	B549:bool
	B550:bool
	B552:bool
	B553:bool
	B567:bool
	I103:int
	I108:int
	I113:int
	I116:int
	I122:int
	I206:int
	I207:int
	I208:int
	I230:int
	I235:int
	I241:int
	I246:int
	I251:int
	I256:int
	I259:int
	I265:int
	I349:int
	I350:int
	I351:int
	I412:int
	I413:int
	I418:int
	I427:int
	I428:int
	I433:int
	I455:int
	I456:int
	I457:int
	I458:int
	I459:int
	I467:int
	I472:int
	I478:int
	I483:int
	I488:int
	I493:int
	I496:int
	I502:int
	I560:int
	I561:int
	I562:int
	I563:int
	I564:int
	I565:int
	M460:bytemap
	M463:bytemap
	R100:bv256
	R105:bv256
	R110:bv256
	R115:bv256
	R118:bv256
	R119:bv256
	R120:bv256
	R121:bv256
	R124:bv256
	R125:bv256
	R128:bv256
	R139:bv256
	R140:bv256
	R141:bv256
	R143:bv256
	R145:bv256
	R146:bv256
	R150:bv256
	R152:bv256
	R154:bv256
	R155:bv256
	R160:bv256
	R166:bv256
	R169:bv256
	R172:bv256
	R174:(uninterp) skey
	R175:bv256
	R176:bv256
	R183:bv256
	R188:bv256
	R189:bv256
	R194:bv256
	R197:bv256
	R199:bv256
	R201:bv256
	R202:bv256
	R203:bv256
	R204:bv256
	R209:bv256
	R210:bv256
	R216:bv256
	R223:bv256
	R224:bv256
	R232:bv256
	R237:bv256
	R243:bv256
	R248:bv256
	R253:bv256
	R258:bv256
	R261:bv256
	R262:bv256
	R263:bv256
	R264:bv256
	R267:bv256
	R268:bv256
	R271:bv256
	R282:bv256
	R283:bv256
	R284:bv256
	R286:bv256
	R288:bv256
	R289:bv256
	R293:bv256
	R295:bv256
	R297:bv256
	R298:bv256
	R303:bv256
	R309:bv256
	R312:bv256
	R315:bv256
	R317:(uninterp) skey
	R318:bv256
	R319:bv256
	R326:bv256
	R331:bv256
	R332:bv256
	R337:bv256
	R340:bv256
	R342:bv256
	R344:bv256
	R345:bv256
	R346:bv256
	R347:bv256
	R352:bv256
	R353:bv256
	R359:bv256
	R366:bv256
	R367:bv256
	R370:bv256
	R372:bv256
	R374:bv256
	R375:bv256
	R377:bv256
	R379:bv256
	R381:bv256
	R383:bv256
	R384:bv256
	R385:bv256
	R387:bv256
	R389:bv256
	R391:bv256
	R392:bv256
	R394:bv256
	R396:bv256
	R398:bv256
	R400:bv256
	R401:bv256
	R402:bv256
	R404:bv256
	R405:bv256
	R407:bv256
	R410:bv256
	R414:bv256
	R416:bv256
	R417:bv256
	R419:bv256
	R420:bv256
	R422:bv256
	R425:bv256
	R429:bv256
	R431:bv256
	R432:bv256
	R434:bv256
	R435:bv256
	R439:bv256
	R441:bv256
	R442:bv256
	R444:bv256
	R445:bv256
	R449:bv256
	R451:bv256
	R452:bv256
	R461:bv256
	R464:bv256
	R469:bv256
	R474:bv256
	R480:bv256
	R485:bv256
	R490:bv256
	R495:bv256
	R498:bv256
	R499:bv256
	R500:bv256
	R501:bv256
	R504:bv256
	R505:bv256
	R510:bv256
	R517:bv256
	R519:bv256
	R520:bv256
	R521:bv256
	R523:bv256
	R525:bv256
	R527:bv256
	R528:bv256
	R532:bv256
	R534:bv256
	R536:bv256
	R537:bv256
	R542:bv256
	R548:bv256
	R551:bv256
	R554:bv256
	R556:(uninterp) skey
	R557:bv256
	R558:bv256
	R566:bv256
	R568:bv256
	R570:bv256
	tacOrigSCANON0:wordmap
	tacOrigSCANON1:wordmap
	tacOrigSCANON2:wordmap
	tacOrigSCANON3:wordmap
	tacOrigSCANON4:wordmap
	tacOrigSCANON5:bv256
	tacOrigSCANON6:bv256
	tacOrigSCANON7:bv256
	tacOrigSCANON8:wordmap
	tacOrigSCANON9:wordmap
	tacAddress@1:bv256
	tacAddress@2:bv256
	tacAddress@3:bv256
	tacAddress@4:bv256
	tacAddress@5:bv256
	tacAddress@6:bv256
	tacAddress@7:bv256
	tacAddress@8:bv256
	tacAddress@9:bv256
	tacAddress@10:bv256
	tacOrigBalanceCANON0:wordmap
	tacOrigBalanceCANON1:wordmap
	tacOrigBalanceCANON2:wordmap
	LCANON0@1:bv256
	LCANON0@2:bv256
	LCANON0@3:bv256
	LCANON0@4:bv256
	LCANON0@5:bv256
	LCANON0@6:bv256
	LCANON0@7:bv256
	LCANON0@8:bv256
	LCANON0@9:bv256
	LCANON0@10:bv256
	LCANON1@1:bool
	LCANON1@5:bool
	LCANON1@7:bool
	LCANON2@1:bool
	LCANON2@2:bool
	LCANON2@3:bool
	LCANON2@4:bool
	LCANON2@5:bool
	LCANON2@6:bool
	LCANON2@7:bool
	LCANON2@8:bool
	LCANON2@9:bool
	LCANON2@10:bool
	LCANON3@1:bool
	LCANON3@2:bool
	LCANON3@3:bool
	LCANON3@4:bool
	LCANON3@5:bool
	LCANON3@6:bool
	LCANON3@7:bool
	LCANON3@8:bool
	LCANON3@9:bool
	LCANON3@10:bool
	LCANON4@1:bool
	LCANON4@2:bool
	LCANON4@6:bool
	LCANON4@7:bool
	LCANON4@8:bool
	LCANON5@1:bool
	LCANON5@2:bool
	LCANON5@6:bool
	LCANON5@7:bool
	LCANON5@8:bool
	LCANON6@1:bool
	LCANON6@7:bool
	LCANON7@1:bool
	LCANON7@7:bool
	LCANON8@1:bool
	LCANON8@7:bool
	LCANON9@1:bool
	LCANON9@7:bool
	tacCallvalue!!238:bv256
	tacCallvalue!!475:bv256
	tacOrigin@1:bv256
	tacOrigin@5:bv256
	tacOrigin@7:bv256
	CANON10:bv256
	CANON11:bool
	CANON12:bv256
	CANON13:bool
	CANON14:bv256
	CANON15:bool
	CANON16:bool
	CANON17:bool
	CANON18:bv256
	CANON19:bv256
	CANON20:int
	CANON21:int
	CANON22:int
	CANON23:int
	CANON24:int
	CANON25:int
	CANON26:int
	CANON27:int
	CANON28:int
	CANON29:int
	CANON30:int
	CANON31:int
	CANON32:int
	CANON33:int
	CANON34:int
	CANON35:int
	CANON36:bool
	CANON37:bool
	CANON38:int
	CANON39:int
	CANON40:int
	CANON41:int
	CANON42:int
	CANON43:int
	CANON44:int
	CANON45:bool
	CANON46:bool
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
	CANON65:int
	CANON66:bool
	CANON67:bv256
	CANON68:bv256
	CANON69:bv256
	CANON70:bv256
	CANON71:int
	CANON72:bv256
	CANON73:bv256
	CANON74:bool
	CANON75@1:bv256
	CANON75@2:bv256
	CANON75@3:bv256
	CANON75@4:bv256
	CANON75@5:bv256
	CANON75@6:bv256
	CANON75@7:bv256
	CANON75@8:bv256
	CANON75@9:bv256
	CANON75@10:bv256
	CANON76@1:bool
	CANON76@2:bool
	CANON76@3:bool
	CANON76@4:bool
	CANON76@5:bool
	CANON76@6:bool
	CANON76@7:bool
	CANON76@8:bool
	CANON76@9:bool
	CANON76@10:bool
	CANON77:wordmap
	CANON78@1:bool
	CANON78@7:bool
	CANON79@1:bool
	CANON79@7:bool
	CANON80@1:bool
	CANON80@7:bool
	CANON81@1:bv256
	CANON81@7:bv256
	CANON82@1:bv256
	CANON82@7:bv256
	CANON83:wordmap
	CANON84:wordmap
	CANON85:wordmap
	CANON86:wordmap
	CANON87:bv256
	CANON88:bv256
	CANON89:bv256
	CANON90:wordmap
	CANON91:wordmap
	CANON92:wordmap
	CANON93:wordmap
	CANON94:bv256
	CANON95:bv256
	CANON96:bv256
	CANON97:bv256
	CANON98:bv256
	CANON99:bv256
	CANON18!!20:bv256
	CANON19!!21:bv256
	LCANON10@1:bv256
	LCANON10@7:bv256
	LCANON11@1:bv256
	LCANON11@7:bv256
	LCANON12@1:bv256
	LCANON12@7:bv256
	LCANON13@1:bv256
	LCANON13@7:bv256
	LCANON14@1:bv256
	LCANON14@7:bv256
	LCANON15@1:bool
	LCANON15@7:bool
	LCANON16@1:bv256
	LCANON16@7:bv256
	LCANON17@1:bv256
	LCANON17@7:bv256
	LCANON18@1:bv256
	LCANON18@7:bv256
	LCANON19@1:bv256
	LCANON19@7:bv256
	LCANON20@1:bv256
	LCANON20@7:bv256
	LCANON21@1:bv256
	LCANON21@7:bv256
	LCANON22@1:bv256
	LCANON22@7:bv256
	LCANON23@1:bv256
	LCANON23@7:bv256
	LCANON24@2:bv256
	LCANON24@6:bv256
	LCANON24@8:bv256
	LCANON25@2:bool
	LCANON25@6:bool
	LCANON25@8:bool
	LCANON26@2:bv256
	LCANON26@6:bv256
	LCANON26@8:bv256
	LCANON27@2:bool
	LCANON27@6:bool
	LCANON27@8:bool
	LCANON28@2:bv256
	LCANON28@4:bv256
	LCANON28@6:bv256
	LCANON28@8:bv256
	LCANON28@10:bv256
	LCANON29@2:bv256
	LCANON29@6:bv256
	LCANON29@8:bv256
	LCANON30@2:bv256
	LCANON30@6:bv256
	LCANON30@8:bv256
	LCANON31@2:bv256
	LCANON31@6:bv256
	LCANON31@8:bv256
	LCANON32@1:bool
	LCANON32@7:bool
	LCANON33@1:bv256
	LCANON33@7:bv256
	LCANON34@1:bv256
	LCANON34@7:bv256
	LCANON35@1:bv256
	LCANON35@7:bv256
	LCANON36@1:bool
	LCANON36@7:bool
	LCANON37@1:bv256
	LCANON37@7:bv256
	LCANON38@1:bool
	LCANON38@7:bool
	LCANON39@1:bv256
	LCANON39@7:bv256
	LCANON40@1:bv256
	LCANON40@7:bv256
	LCANON41@1:bv256
	LCANON41@7:bv256
	LCANON42@1:bv256
	LCANON42@7:bv256
	LCANON43@1:bv256
	LCANON43@7:bv256
	LCANON44@1:bv256
	LCANON44@7:bv256
	LCANON45@1:bv256
	LCANON45@7:bv256
	LCANON46@1:bv256
	LCANON46@7:bv256
	LCANON47@1:bv256
	LCANON47@7:bv256
	LCANON48@1:bv256
	LCANON48@7:bv256
	LCANON49@1:bv256
	LCANON49@7:bv256
	LCANON50@3:bool
	LCANON50@5:bool
	LCANON50@9:bool
	LCANON51@3:bv256
	LCANON51@9:bv256
	LCANON52@3:bv256
	LCANON52@9:bv256
	LCANON53@3:bool
	LCANON53@9:bool
	LCANON54@3:bool
	LCANON54@9:bool
	LCANON55@3:bv256
	LCANON55@9:bv256
	LCANON56@3:bool
	LCANON56@9:bool
	LCANON57@3:bv256
	LCANON57@9:bv256
	LCANON58@3:bool
	LCANON58@9:bool
	LCANON59@3:bool
	LCANON59@9:bool
	LCANON60@3:bv256
	LCANON60@9:bv256
	LCANON61@3:bv256
	LCANON61@9:bv256
	LCANON62@3:bv256
	LCANON62@9:bv256
	LCANON63@3:bv256
	LCANON63@9:bv256
	LCANON64@3:bv256
	LCANON64@9:bv256
	LCANON65@3:bool
	LCANON65@9:bool
	LCANON66@3:bv256
	LCANON66@9:bv256
	LCANON67@3:bv256
	LCANON67@9:bv256
	LCANON68@1:bool
	LCANON68@7:bool
	LCANON69@1:bv256
	LCANON69@7:bv256
	LCANON70@1:bv256
	LCANON70@7:bv256
	LCANON71@1:bv256
	LCANON71@7:bv256
	LCANON72@1:bv256
	LCANON72@7:bv256
	LCANON73@1:bool
	LCANON73@7:bool
	LCANON74@1:bv256
	LCANON74@7:bv256
	LCANON75@1:bv256
	LCANON75@7:bv256
	LCANON76@1:bv256
	LCANON76@7:bv256
	LCANON77@1:bv256
	LCANON77@7:bv256
	LCANON78@1:bv256
	LCANON78@7:bv256
	LCANON79@1:bv256
	LCANON79@7:bv256
	LCANON80@1:bv256
	LCANON80@7:bv256
	LCANON81@4:bool
	LCANON81@10:bool
	LCANON82@4:bool
	LCANON82@10:bool
	LCANON83@4:bool
	LCANON83@10:bool
	LCANON84@4:bv256
	LCANON84@10:bv256
	LCANON85@1:bv256
	LCANON85@7:bv256
	LCANON86@1:bv256
	LCANON86@7:bv256
	LCANON87@1:bv256
	LCANON87@7:bv256
	LCANON88@1:bv256
	LCANON88@7:bv256
	LCANON89@1:bool
	LCANON89@7:bool
	LCANON90@1:bv256
	LCANON90@7:bv256
	LCANON91@1:bool
	LCANON91@7:bool
	LCANON92@1:bool
	LCANON92@7:bool
	LCANON93@1:bv256
	LCANON93@7:bv256
	LCANON94@1:bv256
	LCANON94@7:bv256
	LCANON95@1:bool
	LCANON95@7:bool
	LCANON96@1:bv256
	LCANON96@7:bv256
	LCANON97@1:bv256
	LCANON97@7:bv256
	LCANON98@1:bv256
	LCANON98@7:bv256
	LCANON99@5:bool
	tacMCANON5!!526:bytemap
	tacMCANON5!!569:bytemap
	tacContractAtCANON0:bv256
	tacContractAtCANON1:bv256
	tacContractAtCANON2:bv256
	lastHasThrown:bool
	lastHasThrown@1:bool
	lastHasThrown@2:bool
	lastHasThrown@3:bool
	lastHasThrown@4:bool
	lastHasThrown@5:bool
	lastHasThrown@6:bool
	lastHasThrown@7:bool
	lastHasThrown@8:bool
	lastHasThrown@9:bool
	lastHasThrown@10:bool
	tacOrigSCANON10:wordmap
	tacOrigSCANON11:wordmap
	tacOrigSCANON12:wordmap
	tacOrigSCANON13:bv256
	tacOrigSCANON14:bv256
	tacOrigSCANON15:bv256
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
	tacOrigSCANON29:wordmap
	tacOrigSCANON30:wordmap
	tacOrigSCANON31:wordmap
	tacOrigSCANON32:bv256
	tacOrigSCANON33:bv256
	tacOrigSCANON34:bv256
	tacOrigSCANON35:wordmap
	tacOrigSCANON36:wordmap
	tacOrigSCANON37:wordmap
	tacOrigSCANON38:wordmap
	tacOrigSCANON39:wordmap
	tacOrigSCANON40:bv256
	tacOrigSCANON41:bv256
	tacOrigSCANON42:bv256
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
	tacOrigSCANON54:wordmap
	tacOrigSCANON55:wordmap
	tacOrigSCANON56:wordmap
	tacOrigSCANON57:wordmap
	tacOrigSCANON58:wordmap
	tacOrigSCANON59:bv256
	tacOrigSCANON60:bv256
	tacOrigSCANON61:bv256
	tacOrigSCANON62:wordmap
	tacOrigSCANON63:wordmap
	tacOrigSCANON64:wordmap
	tacOrigSCANON65:wordmap
	tacOrigSCANON66:wordmap
	tacOrigSCANON67:bv256
	tacOrigSCANON68:bv256
	tacOrigSCANON69:bv256
	tacOrigSCANON70:wordmap
	tacOrigSCANON71:wordmap
	tacOrigSCANON72:bv256
	tacOrigSCANON73:bv256
	tacOrigSCANON74:bv256
	tacOrigSCANON75:bv256
	tacOrigSCANON76:bv256
	tacOrigSCANON77:bv256
	tacOrigSCANON78:bv256
	tacOrigSCANON79:bv256
	tacOrigSCANON80:bv256
	CANON141!!454:bool
	tacCaller!!90:bv256
	tacAddress!!157:bv256
	tacAddress!!179:bv256
	tacAddress!!213:bv256
	tacAddress!!240:bv256
	tacAddress!!300:bv256
	tacAddress!!322:bv256
	tacAddress!!356:bv256
	tacAddress!!477:bv256
	tacAddress!!539:bv256
	tacReturndata!!156:bytemap
	tacReturndata!!177:bytemap
	tacReturndata!!211:bytemap
	tacReturndata!!225:bytemap
	tacReturndata!!299:bytemap
	tacReturndata!!320:bytemap
	tacReturndata!!354:bytemap
	tacReturndata!!368:bytemap
	tacReturndata!!386:bytemap
	tacReturndata!!403:bytemap
	tacReturndata!!443:bytemap
	tacReturndata!!453:bytemap
	tacReturndata!!538:bytemap
	CANON0:int
	CANON1:bool
	CANON2:bool
	CANON3:bool
	CANON4:int
	CANON5:bool
	CANON6:bool
	CANON7:bool
	CANON8:bool
	CANON9:bool
	tacCalldatabuf!!182@3:bytemap
	tacCalldatabuf!!325@9:bytemap
	tacSCANON0:wordmap
	tacSCANON1:wordmap
	tacSCANON2:wordmap
	tacCaller!!233:bv256
	tacCaller!!470:bv256
	tacCalldatasize!!0:bv256
	tacCalldatasize!!1:bv256
	tacCalldatasize!!2:bv256
	tacCalldatasize!!3:bv256
	tacCalldatasize!!4:bv256
	tacCalldatasize!!5:bv256
	tacCalldatasize!!6:bv256
	tacMCANON1!!144:bytemap
	tacMCANON1!!287:bytemap
	tacMCANON1!!373:bytemap
	tacMCANON1!!390:bytemap
	LCANON100@5:bv256
	LCANON101@5:bool
	LCANON102@5:bv256
	LCANON103@5:bv256
	LCANON104@5:bv256
	LCANON105@5:bv256
	LCANON106@5:bool
	LCANON107@5:bv256
	LCANON108@5:bool
	LCANON109@5:bv256
	LCANON110@5:bv256
	LCANON111@5:bv256
	LCANON112@5:bv256
	LCANON113@5:bv256
	LCANON114@5:bv256
	LCANON115@5:bv256
	LCANON116@5:bv256
	LCANON117@5:bool
	LCANON118@5:bv256
	LCANON119@5:bv256
	LCANON120@5:bv256
	LCANON121@5:bool
	LCANON122@5:bv256
	LCANON123@5:bool
	LCANON124@5:bv256
	LCANON125@5:bv256
	LCANON126@5:bv256
	LCANON127@5:bv256
	LCANON128@5:bv256
	LCANON129@5:bv256
	tacBalance!!123:wordmap
	tacBalance!!127:wordmap
	tacBalance!!266:wordmap
	tacBalance!!270:wordmap
	tacBalance!!503:wordmap
	tacBalance!!507:wordmap
	tacMCANON6!!533:bytemap
	tacMCANON6!!535:bytemap
	tacMCANON6!!559:bytemap
	CANON77!!24:wordmap
	tacTimestamp@1:bv256
	tacTimestamp@5:bv256
	tacTimestamp@7:bv256
	tacSighash!!31:bv256
	tacSighash!!32:bv256
	tacSighash!!33:bv256
	tacSighash!!34:bv256
	tacSighash!!35:bv256
	tacSighash!!36:bv256
	tacSighash!!37:bv256
	tacSighash!!38:bv256
	tacSighash!!39:bv256
	tacSighash!!40:bv256
	tacSighash@1:bv256
	tacSighash@2:bv256
	tacSighash@3:bv256
	tacSighash@4:bv256
	tacSighash@5:bv256
	tacSighash@6:bv256
	tacSighash@7:bv256
	tacSighash@8:bv256
	tacSighash@9:bv256
	tacSighash@10:bv256
	tacNumber!!106:bv256
	tacNumber!!249:bv256
	tacNumber!!486:bv256
}
Program {
	Block 0_0_0_0_0_0 Succ [0_0_0_1_0_0] {
		AssignHavocCmd tacCalldatabufCANON0@2:0
		AssignHavocCmd tacCalldatabufCANON0@4:0
		AssignHavocCmd tacCalldatabufCANON0@6:1
		AssignHavocCmd tacCalldatabufCANON0@8:2
		AssignHavocCmd tacCalldatabufCANON0@10:2
		AssignHavocCmd tacCalldatasize!!0:3
		AssignHavocCmd tacCalldatasize!!1:3
		AssignHavocCmd tacCalldatasize!!2:3
		AssignHavocCmd tacCalldatasize!!3:3
		AssignHavocCmd tacCalldatasize!!4:3
		AssignHavocCmd tacCalldatasize!!5:3
		AssignHavocCmd tacCalldatasize!!6:3
		AssignHavocCmd tacExtcodesize!!7:4
		AssignHavocCmd I8
		AssignHavocCmd CANON148:5
		AssignHavocCmd CANON150:6
		AssignExpCmd tacMCANON1!!9:7 ByteMapDefinition(i.5394:bv256 -> 0x0 )
		AssignExpCmd tacMCANON1!!10:8 ByteMapDefinition(i.5395:bv256 -> 0x0 )
		AssignExpCmd tacMCANON2!!11:9 ByteMapDefinition(i.5396:bv256 -> 0x0 )
		AssignExpCmd tacMCANON2!!12:10 ByteMapDefinition(i.5397:bv256 -> 0x0 )
		AssignExpCmd tacMCANON3!!13:11 ByteMapDefinition(i.5398:bv256 -> 0x0 )
		AssignExpCmd tacMCANON3!!14:12 ByteMapDefinition(i.5399:bv256 -> 0x0 )
		AssignExpCmd tacMCANON6!!16:13 ByteMapDefinition(i.5400:bv256 -> 0x0 )
		AssignHavocCmd tacBalance!!17:14
		AssignExpCmd tacCalldatabuf@1:15 ByteMapDefinition(i.5401:bv256 -> Ite(Lt(i.5401 tacCalldatasize@1:3 ) Unconstrained(bv256) 0x0 ) )
		AssignExpCmd tacCalldatabuf!!18@3:16 ByteMapDefinition(i.5402:bv256 -> Ite(Lt(i.5402 tacCalldatasize!!1:3 ) Unconstrained(bv256) 0x0 ) )
		AssignExpCmd tacCalldatabuf@7:17 ByteMapDefinition(i.5403:bv256 -> Ite(Lt(i.5403 tacCalldatasize@7:3 ) Unconstrained(bv256) 0x0 ) )
		AssignExpCmd tacCalldatabuf!!19@9:18 ByteMapDefinition(i.5404:bv256 -> Ite(Lt(i.5404 tacCalldatasize!!5:3 ) Unconstrained(bv256) 0x0 ) )
		AssignHavocCmd CANON18!!20:19
		AssignHavocCmd CANON19!!21:20
		AssignHavocCmd CANON20:21
		AssignHavocCmd CANON21:22
		AssignHavocCmd CANON22:23
		AssignHavocCmd CANON23:24
		AssignHavocCmd CANON24:25
		AssignHavocCmd CANON25:26
		AssignHavocCmd CANON26:27
		AssignHavocCmd CANON27:28
		AssignHavocCmd CANON28:29
		AssignHavocCmd CANON29:30
		AssignHavocCmd CANON30:31
		AssignHavocCmd CANON31:32
		AssignHavocCmd CANON32:33
		AssignHavocCmd CANON33:34
		AssignHavocCmd CANON34:35
		AssignHavocCmd CANON35:36
		AssignHavocCmd B22
		AssignHavocCmd I23
		AssignHavocCmd CANON77!!24:37
		AssignHavocCmd CANON87!!25:38
		AssignHavocCmd CANON93!!26:39
		AssignHavocCmd CANON99!!27:40
		AssignHavocCmd R28:41
		AssignHavocCmd R29:42
		AssignHavocCmd R30:43
		AssignHavocCmd tacSighash!!31:44
		AssignHavocCmd tacSighash!!32:44
		AssignHavocCmd tacSighash!!33:44
		AssignHavocCmd tacSighash!!34:44
		AssignHavocCmd tacSighash!!35:44
		AssignHavocCmd tacSighash!!36:44
		AssignHavocCmd tacSighash!!37:44
		AssignHavocCmd tacSighash!!38:44
		AssignHavocCmd tacSighash!!39:44
		AssignHavocCmd tacSighash!!40:44
		AssignExpCmd CANON0:45 0x3d24a36b
		AssignExpCmd CANON1:46 false
		AssignExpCmd CANON2:47 true
		AssignExpCmd CANON3:48 false
		AssignExpCmd CANON4:49 0x1
		AssignExpCmd CANON5:50 false
		AnnotationCmd JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Message","s":"Setup"}}
		AnnotationCmd JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Message","s":"multi contract setup"}}
		AnnotationCmd JSON{"key":{"name":"cvl.label.end","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		AnnotationCmd JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Message","s":"rule parameters setup"}}
		AssumeCmd true
		AssumeCmd true
		AnnotationCmd JSON{"key":{"name":"cvl.label.end","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		AnnotationCmd JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Message","s":"contract address vars initialized"}}
		AnnotationCmd JSON{"key":{"name":"cvl.label.end","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		AnnotationCmd JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Message","s":"setup read tracking instrumentation"}}
		AnnotationCmd JSON{"key":{"name":"cvl.label.end","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		AnnotationCmd JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Message","s":"last storage initialize"}}
		AnnotationCmd JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageGlobalChangeSnippet.StorageTakeSnapshot","lhs":{"namePrefix":"lastStorage","tag":{"#class":"tac.Tag.BlockchainState"},"callIndex":0,"meta":[{"key":{"name":"cvl.local","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true},{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"lastStorage"},{"key":{"name":"cvl.type","type":"spec.cvlast.CVLType$PureCVLType","erasureStrategy":"CallTrace"},"value":{"#class":"spec.cvlast.CVLType.PureCVLType.VMInternal.BlockchainState"}},{"key":{"name":"cvl","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true},{"key":{"name":"cvl.display","type":"java.lang.String","erasureStrategy":"CallTrace"},"value":"lastStorage"}]}}}
		AnnotationCmd JSON{"key":{"name":"cvl.label.end","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		AnnotationCmd JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Message","s":"assumptions about extcodesize"}}
		AssignExpCmd B41:51 Gt(Select(tacExtcodesize!!7:4 Apply(to_skey:bif R28:41) ) 0x0 )
		AssumeCmd B41:51
		AssignExpCmd B42:51 Gt(Select(tacExtcodesize!!7:4 Apply(to_skey:bif R29:42) ) 0x0 )
		AssumeCmd B42:51
		AssignExpCmd B43:51 Gt(Select(tacExtcodesize!!7:4 Apply(to_skey:bif R30:43) ) 0x0 )
		AssumeCmd B43:51
		AnnotationCmd JSON{"key":{"name":"cvl.label.end","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		AnnotationCmd JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Message","s":"assumptions about contracts' addresses"}}
		NopCmd
		AssumeExpCmd Gt(R28:41 0x0 )
		NopCmd
		AssumeExpCmd Le(R28:41 0xffffffffffffffffffffffffffffffffffffffff )
		NopCmd
		AssumeExpCmd Gt(R29:42 0x0 )
		NopCmd
		AssumeExpCmd Le(R29:42 0xffffffffffffffffffffffffffffffffffffffff )
		NopCmd
		AssumeExpCmd Gt(R30:43 0x0 )
		NopCmd
		AssumeExpCmd Le(R30:43 0xffffffffffffffffffffffffffffffffffffffff )
		AnnotationCmd JSON{"key":{"name":"cvl.label.end","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		AnnotationCmd JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Message","s":"assumptions about starting balances"}}
		AssignExpCmd R50:51 Select(tacBalance!!17:14 Apply(to_skey:bif R28:41) )
		NopCmd
		AssumeExpCmd Ge(R50:51 0x0 )
		AssignExpCmd R52:51 Select(tacBalance!!17:14 Apply(to_skey:bif R29:42) )
		NopCmd
		AssumeExpCmd Ge(R52:51 0x0 )
		AssignExpCmd R54:51 Select(tacBalance!!17:14 Apply(to_skey:bif R30:43) )
		NopCmd
		AssumeExpCmd Ge(R54:51 0x0 )
		AnnotationCmd JSON{"key":{"name":"cvl.label.end","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		AnnotationCmd JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Message","s":"assumptions about static addresses"}}
		AnnotationCmd JSON{"key":{"name":"cvl.label.end","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		AnnotationCmd JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Message","s":"assumptions about uniqueness of contracts' addressses"}}
		NopCmd
		AssumeExpCmd LNot(Eq(R28:41 R29:42 ) )
		NopCmd
		AssumeExpCmd LNot(Eq(R28:41 R30:43 ) )
		NopCmd
		AssumeExpCmd LNot(Eq(R29:42 R30:43 ) )
		AnnotationCmd JSON{"key":{"name":"cvl.label.end","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		NopCmd
		AssumeExpCmd Eq(CANON18!!20:19 R29:42 )
		NopCmd
		AssumeExpCmd Eq(CANON19!!21:20 R28:41 )
		AnnotationCmd JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Message","s":"record starting nonces"}}
		AnnotationCmd JSON{"key":{"name":"cvl.label.end","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		AnnotationCmd JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Message","s":"cloned contracts have no balances"}}
		AnnotationCmd JSON{"key":{"name":"cvl.label.end","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		AnnotationCmd JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Message","s":"Linked immutable setup"}}
		AnnotationCmd JSON{"key":{"name":"cvl.label.end","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		AnnotationCmd JSON{"key":{"name":"cvl.label.end","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		NopCmd
		AssumeExpCmd LAnd(Le(CANON20:21 0xffffffffffffffffffffffffffffffffffffffff ) Ge(CANON20:21 0x0 ) )
		NopCmd
		AssumeExpCmd LAnd(Le(CANON21:22 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff ) Ge(CANON21:22 0x0 ) )
		NopCmd
		AssumeExpCmd LAnd(Le(CANON22:23 0xffffffffffffffffffffffffffffffffffffffff ) Ge(CANON22:23 0x0 ) )
		NopCmd
		AssumeExpCmd LAnd(Le(CANON23:24 0xffffffffffffffffffffffffffffffffffffffff ) Ge(CANON23:24 0x0 ) )
		NopCmd
		AssumeExpCmd LAnd(Le(CANON24:25 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff ) Ge(CANON24:25 0x0 ) )
		NopCmd
		AssumeExpCmd LAnd(Le(CANON25:26 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff ) Ge(CANON25:26 0x0 ) )
		NopCmd
		AssumeExpCmd LAnd(Le(CANON26:27 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff ) Ge(CANON26:27 0x0 ) )
		NopCmd
		AssumeExpCmd LAnd(Le(CANON27:28 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff ) Ge(CANON27:28 0x0 ) )
		NopCmd
		AssumeExpCmd LAnd(Le(CANON28:29 0xffffffffffffffffffffffffffffffffffffffff ) Ge(CANON28:29 0x0 ) )
		NopCmd
		AssumeExpCmd LAnd(Le(CANON29:30 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff ) Ge(CANON29:30 0x0 ) )
		NopCmd
		AssumeExpCmd LAnd(Le(CANON30:31 0xffffffffffffffffffffffffffffffffffffffff ) Ge(CANON30:31 0x0 ) )
		NopCmd
		AssumeExpCmd LAnd(Le(CANON31:32 0xffffffffffffffffffffffffffffffffffffffff ) Ge(CANON31:32 0x0 ) )
		NopCmd
		AssumeExpCmd LAnd(Le(CANON32:33 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff ) Ge(CANON32:33 0x0 ) )
		NopCmd
		AssumeExpCmd LAnd(Le(CANON33:34 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff ) Ge(CANON33:34 0x0 ) )
		NopCmd
		AssumeExpCmd LAnd(Le(CANON34:35 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff ) Ge(CANON34:35 0x0 ) )
		NopCmd
		AssumeExpCmd LAnd(Le(CANON35:36 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff ) Ge(CANON35:36 0x0 ) )
		AnnotationCmd:52 JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Cmd","cmd":{"cmd_type":"spec.cvlast.CVLCmd.Simple.AssumeCmd.Assume","cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/specs/ViewReentrancy.spec","start":{"line":25,"character":4},"end":{"line":25,"character":17}},"exp":{"#class":"spec.cvlast.CVLExp.VariableExp","id":"cond","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":0}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"},"cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/specs/ViewReentrancy.spec","start":{"line":25,"character":4},"end":{"line":25,"character":17}}},"twoStateIndex":"NEITHER"},"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":0}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}}}}}
		AssumeCmd:52 B22
		AnnotationCmd:52 JSON{"key":{"name":"cvl.label.end","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		AnnotationCmd:53 JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Cmd","cmd":{"cmd_type":"spec.cvlast.CVLCmd.Simple.AssumeCmd.Assume","cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/specs/ViewReentrancy.spec","start":{"line":26,"character":4},"end":{"line":26,"character":56}},"exp":{"#class":"spec.cvlast.CVLExp.RelopExp.EqExp","l":{"#class":"spec.cvlast.CVLExp.VariableExp","id":"before_func1","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":0}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256},"cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/specs/ViewReentrancy.spec","start":{"line":26,"character":4},"end":{"line":26,"character":56}}},"twoStateIndex":"NEITHER"},"r":{"#class":"spec.cvlast.CVLExp.ApplyExp.ContractFunction.Concrete","methodIdWithCallContext":{"#class":"spec.cvlast.ConcreteMethod","signature":{"#class":"spec.cvlast.ExternalQualifiedMethodSignature.ExternalQualifiedMethodSig","wrapped":{"#class":"spec.cvlast.QualifiedMethodSignature.QualifiedMethodSig","qualifiedMethodName":{"#class":"spec.cvlast.QualifiedFunction","host":{"name":"curve"},"methodId":"getVirtualPrice"},"params":[],"res":[{"#class":"spec.cvlast.VMParam.Unnamed","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256}}]},"sighashInt":{"n":"e25aa5fa"}}},"args":[{"#class":"spec.cvlast.CVLExp.VariableExp","id":"e_external","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":0}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"env","fields":[{"fieldName":"msg","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"msg","fields":[{"fieldName":"sender","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"value","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}}]}},{"fieldName":"tx","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"tx","fields":[{"fieldName":"origin","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}}]}},{"fieldName":"block","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"block","fields":[{"fieldName":"coinbase","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"difficulty","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"gaslimit","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"number","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"timestamp","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}}]}}]},"cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/specs/ViewReentrancy.spec","start":{"line":26,"character":4},"end":{"line":26,"character":56}}},"twoStateIndex":"NEITHER"}],"noRevert":true,"storage":{"#class":"spec.cvlast.CVLExp.VariableExp","id":"lastStorage","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":0}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.VMInternal.BlockchainState"},"cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/specs/ViewReentrancy.spec","start":{"line":26,"character":4},"end":{"line":26,"character":56}}},"twoStateIndex":"NEITHER"},"isWhole":false,"tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":0}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.VM","descriptor":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256},"context":{"#class":"spec.cvlast.typedescriptors.FromVMContext.ReturnValue"}},"cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/specs/ViewReentrancy.spec","start":{"line":26,"character":28},"end":{"line":26,"character":43}},"annotation":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.CallResolution$DirectPassing","target":{"methodSignature":{"#class":"spec.cvlast.ExternalQualifiedMethodSignature.ExternalQualifiedMethodSig","wrapped":{"#class":"spec.cvlast.QualifiedMethodSignature.QualifiedMethodSig","qualifiedMethodName":{"#class":"spec.cvlast.QualifiedFunction","host":{"name":"curve"},"methodId":"getVirtualPrice"},"params":[],"res":[{"#class":"spec.cvlast.VMParam.Unnamed","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256}}]},"sighashInt":{"n":"e25aa5fa"}},"definitelyNonPayable":true,"annotation":{"visibility":"EXTERNAL","envFree":false,"library":false},"stateMutability":"view","tag":{"#class":"spec.cvlast.CVLImportedFunctionTag.WithMethodInfo","evmMethodInfo":{"sigHash":"e25aa5fa","name":"getVirtualPrice","argTypes":[],"resultTypes":[{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256}],"stateMutability":"view","envfreeInfo":{"#class":"bridge.EnvfreeInfo.Unknown"},"isConstant":false,"isLibrary":false}}},"hasEnv":true}}},"tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":0}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"},"cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/specs/ViewReentrancy.spec","start":{"line":26,"character":12},"end":{"line":26,"character":55}}}},"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":0}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}}}}}
		NopCmd
		NopCmd
		NopCmd
		NopCmd
		NopCmd
	}
	Block 0_0_0_1_0_0 Succ [0_0_0_2_0_0] {
		AnnotationCmd:53 JSON{"key":{"name":"call.trace.push","type":"analysis.icfg.Inliner$CallStack$PushRecord","erasureStrategy":"Canonical"},"value":"rO0ABXNyACphbmFseXNpcy5pY2ZnLklubGluZXIkQ2FsbFN0YWNrJFB1c2hSZWNvcmSX8+DCTLCH+AIAA0kACGNhbGxlZUlkTAAGY2FsbGVldAATTHZjL2RhdGEvTWV0aG9kUmVmO0wAB3N1bW1hcnl0ABVMdmMvZGF0YS9DYWxsU3VtbWFyeTt4cAAAAAFzcgARdmMuZGF0YS5NZXRob2RSZWbJlJTzzU9pGAIAA0wABGF0dHJ0ABdMc2NlbmUvTWV0aG9kQXR0cmlidXRlO0wACmNvbnRyYWN0SWR0ABZMamF2YS9tYXRoL0JpZ0ludGVnZXI7TAAHc2lnSGFzaHQAEExldm0vU2lnaGFzaEludDt4cHNyABxzY2VuZS5NZXRob2RBdHRyaWJ1dGUkQ29tbW9uNHjdebdr9XMCAAB4cgAVc2NlbmUuTWV0aG9kQXR0cmlidXRlcYg2pYWutuUCAAB4cHNyABRqYXZhLm1hdGguQmlnSW50ZWdlcoz8nx+pO/sdAwAGSQAIYml0Q291bnRJAAliaXRMZW5ndGhJABNmaXJzdE5vbnplcm9CeXRlTnVtSQAMbG93ZXN0U2V0Qml0SQAGc2lnbnVtWwAJbWFnbml0dWRldAACW0J4cgAQamF2YS5sYW5nLk51bWJlcoaslR0LlOCLAgAAeHD///////////////7////+AAAAAXVyAAJbQqzzF/gGCFTgAgAAeHAAAAAQzkYEoAAAAAAAAAAAAAAAKHhzcgAOZXZtLlNpZ2hhc2hJbnRUdcqNMXEgeAIAAUwAAW5xAH4ABnhwc3EAfgAM///////////////+/////gAAAAF1cQB+ABAAAAAE4lql+nhw"}
		AssignHavocCmd:53 tacCalldatasize!!84:3
		NopCmd
		AssumeExpCmd Apply(add_noofl:bif 0x4 0x0)
		NopCmd
		AssumeExpCmd Eq(0x4 tacCalldatasize!!84:3 )
		AssignExpCmd:53 B88 LAnd(Ge(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff CANON28:29 ) Le(0x0 CANON28:29 ) )
		AssertCmd:53 B88 "sanity bounds check on cvl to vm encoding of tacTmp!4760:int failed"
		AssignExpCmd:53 R89:51 Apply(safe_math_narrow:bif CANON28:29)
		NopCmd
		AssumeExpCmd LAnd(Le(R89:54 0xffffffffffffffffffffffffffffffffffffffff ) Ge(R89:54 0x0 ) )
		AssignExpCmd:53 B93 LAnd(Ge(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff CANON29:30 ) Le(0x0 CANON29:30 ) )
		AssertCmd:53 B93 "sanity bounds check on cvl to vm encoding of tacTmp!4763:int failed"
		AssignExpCmd:53 R94:51 Apply(safe_math_narrow:bif CANON29:30)
		NopCmd
		AssumeExpCmd LAnd(Le(R94:55 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff ) Ge(R94:55 0x0 ) )
		AssignExpCmd:53 B99 LAnd(Ge(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff CANON30:31 ) Le(0x0 CANON30:31 ) )
		AssertCmd:53 B99 "sanity bounds check on cvl to vm encoding of tacTmp!4767:int failed"
		AssignExpCmd:53 R100:51 Apply(safe_math_narrow:bif CANON30:31)
		NopCmd
		AssumeExpCmd LAnd(Le(R100:56 0xffffffffffffffffffffffffffffffffffffffff ) Ge(R100:56 0x0 ) )
		AssignExpCmd:53 B104 LAnd(Ge(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff CANON34:35 ) Le(0x0 CANON34:35 ) )
		AssertCmd:53 B104 "sanity bounds check on cvl to vm encoding of tacTmp!4770:int failed"
		AssignExpCmd:53 R105:51 Apply(safe_math_narrow:bif CANON34:35)
		NopCmd
		AssumeExpCmd LAnd(Le(R105:57 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff ) Ge(R105:57 0x0 ) )
		AssignExpCmd:53 B109 LAnd(Ge(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff CANON35:36 ) Le(0x0 CANON35:36 ) )
		AssertCmd:53 B109 "sanity bounds check on cvl to vm encoding of tacTmp!4773:int failed"
		AssignExpCmd:53 R110:51 Apply(safe_math_narrow:bif CANON35:36)
		NopCmd
		AssumeExpCmd LAnd(Le(R110:58 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff ) Ge(R110:58 0x0 ) )
		AssignExpCmd:53 B114 LAnd(Ge(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff CANON29:30 ) Le(0x0 CANON29:30 ) )
		AssertCmd:53 B114 "sanity bounds check on cvl to vm encoding of tacTmp!4776:int failed"
		AssignExpCmd:53 R115:51 Apply(safe_math_narrow:bif CANON29:30)
		AssignExpCmd:53 B117 LAnd(Ge(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff CANON28:29 ) Le(0x0 CANON28:29 ) )
		AssertCmd:53 B117 "sanity bounds check on cvl to vm encoding of tacTmp!4779:int failed"
		AssignExpCmd:53 R118:51 Apply(safe_math_narrow:bif CANON28:29)
		AssignExpCmd:53 R121:51 Select(tacBalance!!17:14 Apply(to_skey:bif R118:51) )
		AssignExpCmd:59 I122:51 IntSub(R121:51 R115:51 )
		AssignExpCmd:59 tacBalance!!123:14 Store(tacBalance!!17:14 Apply(to_skey:bif R118:51) I122:51 )
		AssignExpCmd:53 R124:51 Select(tacBalance!!123:14 Apply(to_skey:bif R30:43) )
		AssignExpCmd:59 R125:51 Add(R124:51 R115:51)
		NopCmd
		AssumeExpCmd Apply(add_noofl:bif R124:51 R115:51)
		AssignExpCmd:59 tacBalance!!127:14 Store(tacBalance!!123:14 Apply(to_skey:bif R30:43) R125:51 )
		AnnotationCmd:53 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.BalanceSnippet","srcAccountInfo":{"old":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R121","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}]},"new":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"I122","tag":{"#class":"tac.Tag.Int"},"callIndex":0,"meta":[{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}]},"addr":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R118","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}]}},"trgAccountInfo":{"old":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R124","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}]},"new":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R125","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}]},"addr":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R30","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"tacContractAt"},{"key":{"name":"tac.contract.sym.addr.name","type":"java.lang.String","erasureStrategy":"Erased"},"value":"curve"},{"key":{"name":"tac.contract.sym.addr","type":"java.math.BigInteger","erasureStrategy":"Erased"},"value":"ce4604a0000000000000000000000028"}]}},"transferredAmount":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R115","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}]}}}
		LabelCmd:53 "Start procedure curve-getVirtualPrice()"
		AnnotationCmd:53 JSON{"key":{"name":"fps.free-pointer-is-scalarized","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true}
		AssignExpCmd:53 R128:51 Select(tacExtcodesize!!7:4 Apply(to_skey:bif R30:60) )
		NopCmd
		AssumeExpCmd Gt(R128:51 0x0 )
		AnnotationCmd:53 JSON{"key":{"name":"internal.func.finder.info","type":"analysis.ip.InternalFunctionFinderReport","erasureStrategy":"Erased"},"value":"rO0ABXNyAChhbmFseXNpcy5pcC5JbnRlcm5hbEZ1bmN0aW9uRmluZGVyUmVwb3J0ian+bYn1VdACAAFMABN1bnJlc29sdmVkRnVuY3Rpb25zdAAPTGphdmEvdXRpbC9TZXQ7eHBzcgAhZGF0YXN0cnVjdHVyZXMuTGlua2VkQXJyYXlIYXNoU2V0AAAAAAAAAAEDAAJGAApsb2FkRmFjdG9yTAAJaGFzaFRhYmxldAAuTGRhdGFzdHJ1Y3R1cmVzL2FycmF5aGFzaHRhYmxlL0FycmF5SGFzaFRhYmxlO3hwdwgAAAAAQAAAAHg="}
		AnnotationCmd:53 JSON{"key":{"name":"fps.free-pointer-is-scalarized","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true}
		NopCmd
		AssumeExpCmd Eq(R94:51 0x0 )
		NopCmd
		AssumeExpCmd LNot(Lt(tacCalldatasize!!84:3 0x4 ) )
		NopCmd
		AssumeExpCmd LNot(Gt(0x82c63066 tacSighash!!31:44 ) )
		NopCmd
		AssumeExpCmd LNot(Eq(0x82c63066 tacSighash!!31:44 ) )
		NopCmd
		AssumeExpCmd LNot(Eq(0x89295a45 tacSighash!!31:44 ) )
		NopCmd
		AssumeExpCmd LNot(Eq(0x9d1e1f25 tacSighash!!31:44 ) )
		NopCmd
		AssumeExpCmd LNot(Eq(0xac8c9059 tacSighash!!31:44 ) )
		NopCmd
		AssumeExpCmd LNot(Eq(0xd802e4f7 tacSighash!!31:44 ) )
		NopCmd
		AssumeExpCmd Eq(0xe25aa5fa tacSighash!!31:44 )
		AnnotationCmd:53 JSON{"key":{"name":"internal.func.start","type":"analysis.ip.InternalFuncStartAnnotation","erasureStrategy":"CallTrace"},"value":{"id":0,"startPc":2909,"args":[],"methodSignature":{"#class":"spec.cvlast.QualifiedMethodSignature.QualifiedMethodSig","qualifiedMethodName":{"#class":"spec.cvlast.QualifiedFunction","host":{"name":"curve"},"methodId":"getVirtualPrice"},"params":[],"res":[{"#class":"spec.cvlast.VMParam.Unnamed","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256}}]},"stackOffsetToArgPos":{},"callSiteSrc":{"source":7,"begin":5992,"len":476,"jumpType":"ENTER","address":"ce4604a0000000000000000000000028","sourceContext":{"indexToFilepath":{"0":"contracts/Context.sol","1":"contracts/CurveToken.sol","2":"contracts/CurveTokenExample.sol","3":"contracts/ERC20.sol","4":"contracts/IERC20.sol","5":"contracts/IERC20Metadata.sol","6":"contracts/ReentrancyGuard.sol","7":"contracts/curve.sol"},"sourceDir":".post_autofinders.2"}}}}
		AnnotationCmd:53 JSON{"key":{"name":"pta.end-allocation","type":"analysis.alloc.AllocationAnalysis$AbstractLocation","erasureStrategy":"Erased"},"value":{"prevFPWriteIdx":0,"nextFPWriteCmd":{"block":{"#class":"tac.BlockIdentifier","origStartPc":16,"stkTop":1024,"decompCopy":0,"calleeIdx":0,"topOfStackValue":2,"freshCopy":0},"pos":34},"sort":{"#class":"analysis.alloc.AllocationAnalysis.Alloc.ConstBlock","sz":"40"}}}
		AssignExpCmd:61 R140:62 Select(CANON77!!24:37 Apply(skey_basic:bif 0x8) )
		AnnotationCmd:53 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet","value":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R140","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1012}]},"displayPath":{"#class":"analysis.storage.DisplayPath.ArrayAccess","index":{"#class":"vc.data.TACSymbol.Const","value":"0"},"base":{"#class":"analysis.storage.DisplayPath.Root","name":"admin_balances"}},"storageType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256},"contractInstance":"ce4604a0000000000000000000000028","linkableStorageReadId":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet.None"}}}
		AssignExpCmd:63 R141:64 Select(tacBalance!!127:14 Apply(to_skey:bif R30:60) )
		NopCmd
		AssumeExpCmd LNot(Lt(R141:64 R140:62 ) )
		AssignExpCmd:65 R143:66 Sub(R141:64 R140:62 )
		AssignExpCmd:67 tacMCANON1!!144:7 Store(tacMCANON1!!9:7 0xc0 R143:66 )
		AssignExpCmd:68 R145:69 Select(CANON77!!24:37 Apply(skey_basic:bif 0x9) )
		AnnotationCmd:53 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet","value":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R145","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1013}]},"displayPath":{"#class":"analysis.storage.DisplayPath.ArrayAccess","index":{"#class":"vc.data.TACSymbol.Const","value":"1"},"base":{"#class":"analysis.storage.DisplayPath.Root","name":"admin_balances"}},"storageType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256},"contractInstance":"ce4604a0000000000000000000000028","linkableStorageReadId":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet.None"}}}
		AssignExpCmd:53 B147:51 Le(CANON18!!20:70 0xffffffffffffffffffffffffffffffffffffffff )
		AssignExpCmd:53 B148:51 Ge(CANON18!!20:70 0x0 )
		NopCmd
		AssumeExpCmd LAnd(B147:51 B148:51 )
		AnnotationCmd:53 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet","value":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"CANON18!!20","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.scalarization.sort","type":"vc.data.ScalarizationSort","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.ScalarizationSort.Packed","packedStart":{"#class":"vc.data.ScalarizationSort.Split","idx":"b"},"start":0}},{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.storage.bit-width","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":160},{"key":{"name":"tac.storage.pretty.paths","type":"analysis.storage.DisplayPaths","erasureStrategy":"Erased"},"value":{"paths":[{"#class":"analysis.storage.DisplayPath.Root","name":"coins_1"}]}},{"key":{"name":"tac.slot.type","type":"spec.cvlast.typedescriptors.EVMTypeDescriptor$EVMValueType","erasureStrategy":"Canonical"},"value":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.address"}},{"key":{"name":"tac.storage.non-indexed-path","type":"analysis.storage.StorageAnalysisResult$NonIndexedPath","erasureStrategy":"Canonical"},"value":{"#class":"analysis.storage.StorageAnalysisResult.NonIndexedPath.Root","slot":"b"}},{"key":{"name":"tac.storage","type":"java.math.BigInteger","erasureStrategy":"Canonical"},"value":"ce4604a0000000000000000000000028"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1011}]},"displayPath":{"#class":"analysis.storage.DisplayPath.Root","name":"coins_1"},"storageType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.address"},"contractInstance":"ce4604a0000000000000000000000028","linkableStorageReadId":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet.Id","id":0}}}
		AnnotationCmd:53 JSON{"key":{"name":"init.reorder.fence","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		AssignExpCmd:71 tacMCANON2!!151:9 Store(tacMCANON2!!11:9 0x100 0x70a0823100000000000000000000000000000000000000000000000000000000 )
		AssignExpCmd:72 tacMCANON2!!153:9 Store(tacMCANON2!!151:9 0x104 R30:43 )
		AssignExpCmd:71 R154:73 0x100
		AssignHavocCmd:71 R155:74
		AssignHavocCmd:53 tacReturndata!!156:75
		JumpCmd:53 0_0_0_2_0_0
	}
	Block 0_0_0_2_0_0 Succ [1_0_0_1_0_0] {
		AnnotationCmd:53 JSON{"key":{"name":"call.trace.push","type":"analysis.icfg.Inliner$CallStack$PushRecord","erasureStrategy":"Canonical"},"value":"rO0ABXNyACphbmFseXNpcy5pY2ZnLklubGluZXIkQ2FsbFN0YWNrJFB1c2hSZWNvcmSX8+DCTLCH+AIAA0kACGNhbGxlZUlkTAAGY2FsbGVldAATTHZjL2RhdGEvTWV0aG9kUmVmO0wAB3N1bW1hcnl0ABVMdmMvZGF0YS9DYWxsU3VtbWFyeTt4cAAAAAJzcgARdmMuZGF0YS5NZXRob2RSZWbJlJTzzU9pGAIAA0wABGF0dHJ0ABdMc2NlbmUvTWV0aG9kQXR0cmlidXRlO0wACmNvbnRyYWN0SWR0ABZMamF2YS9tYXRoL0JpZ0ludGVnZXI7TAAHc2lnSGFzaHQAEExldm0vU2lnaGFzaEludDt4cHNyABxzY2VuZS5NZXRob2RBdHRyaWJ1dGUkQ29tbW9uNHjdebdr9XMCAAB4cgAVc2NlbmUuTWV0aG9kQXR0cmlidXRlcYg2pYWutuUCAAB4cHNyABRqYXZhLm1hdGguQmlnSW50ZWdlcoz8nx+pO/sdAwAGSQAIYml0Q291bnRJAAliaXRMZW5ndGhJABNmaXJzdE5vbnplcm9CeXRlTnVtSQAMbG93ZXN0U2V0Qml0SQAGc2lnbnVtWwAJbWFnbml0dWRldAACW0J4cgAQamF2YS5sYW5nLk51bWJlcoaslR0LlOCLAgAAeHD///////////////7////+AAAAAXVyAAJbQqzzF/gGCFTgAgAAeHAAAAAQzkYEoAAAAAAAAAAAAAAAEXhzcgAOZXZtLlNpZ2hhc2hJbnRUdcqNMXEgeAIAAUwAAW5xAH4ABnhwc3EAfgAM///////////////+/////gAAAAF1cQB+ABAAAAAEcKCCMXhzcgATdmMuZGF0YS5DYWxsU3VtbWFyeZQcmw5vl+FdAgAQSQAJc3VtbWFyeUlkTAAOY2FsbENvbnZlbnRpb250ACZMaW5zdHJ1bWVudGF0aW9uL2NhbGxzL0NhbGxDb252ZW50aW9uO0wACmNhbGxUYXJnZXR0ABpMYW5hbHlzaXMvaWNmZy9DYWxsVGFyZ2V0O0wACGNhbGxUeXBldAAVTHZjL2RhdGEvVEFDQ2FsbFR5cGU7TAAPY2Fubm90QmVJbmxpbmVkdAAtTGFuYWx5c2lzL2ljZmcvSW5saW5lciRJbGxlZ2FsSW5saW5pbmdSZWFzb247TAAGZ2FzVmFydAATTHZjL2RhdGEvVEFDU3ltYm9sO0wABmluQmFzZXEAfgAbTAAIaW5PZmZzZXRxAH4AG0wABmluU2l6ZXEAfgAbTAAMb3JpZ0NhbGxjb3JldAAgTHZjL2RhdGEvVEFDQ21kJFNpbXBsZSRDYWxsQ29yZTtMAAdvdXRCYXNlcQB+ABtMAAlvdXRPZmZzZXRxAH4AG0wAB291dFNpemVxAH4AG0wADXNpZ1Jlc29sdXRpb250AA9MamF2YS91dGlsL1NldDtMAAV0b1ZhcnEAfgAbTAAIdmFsdWVWYXJxAH4AG3hwAAAAAHNyACRpbnN0cnVtZW50YXRpb24uY2FsbHMuQ2FsbENvbnZlbnRpb25HtO1ulL788QIAA0kACGNhbGxlcklkTAAFaW5wdXR0ABlMYW5hbHlzaXMvaWNmZy9DYWxsSW5wdXQ7TAAGcmF3T3V0dAAiTGluc3RydW1lbnRhdGlvbi9jYWxscy9DYWxsT3V0cHV0O3hwAAAAAHNyABdhbmFseXNpcy5pY2ZnLkNhbGxJbnB1dJjJD1MhNUxQAgAHTAAHYmFzZVZhcnQAGUx2Yy9kYXRhL1RBQ0V4cHIkU3ltJFZhcjtMABBlbmNvZGVkQXJndW1lbnRzdAAjTGFuYWx5c2lzL2ljZmcvQUJJQXJndW1lbnRFbmNvZGluZztMABNpbnB1dFNpemVMb3dlckJvdW5kcQB+AAZMAAZvZmZzZXR0ABVMdmMvZGF0YS9UQUNFeHByJFN5bTtMABRyYW5nZVRvRGVjb21wb3NlZEFyZ3QAD0xqYXZhL3V0aWwvTWFwO0wAEHNpbXBsaWZpZWRPZmZzZXR0ABtMdmMvZGF0YS9UQUNFeHByJFN5bSRDb25zdDtMAARzaXplcQB+ACZ4cHNyABd2Yy5kYXRhLlRBQ0V4cHIkU3ltJFZhcskrg43eGgPnAgACTAABc3QAF0x2Yy9kYXRhL1RBQ1N5bWJvbCRWYXI7TAADdGFndAAJTHRhYy9UYWc7eHIAE3ZjLmRhdGEuVEFDRXhwciRTeW2iVj0S4YSNUAIAAHhyAA92Yy5kYXRhLlRBQ0V4cHJYhGlUu/v+yAIAAHhwc3IANnZjLmRhdGEuVEFDU3ltYm9sJFZhciRXaXRoRGVmYXVsdENhbGxJbmRleCRXaXRoQnl0ZU1hcJ7+oHF4CHAAAgACTAAEbWV0YXQALUxrb3RsaW54L2NvbGxlY3Rpb25zL2ltbXV0YWJsZS9QZXJzaXN0ZW50TWFwO0wACm5hbWVQcmVmaXh0ABJMamF2YS9sYW5nL1N0cmluZzt4cgAVdmMuZGF0YS5UQUNTeW1ib2wkVmFyCYrCGVl9SXYCAAB4cgARdmMuZGF0YS5UQUNTeW1ib2zd3Run/CoWswIAAHhwc3IAJmRhdGFzdHJ1Y3R1cmVzLnRyZWFwLkhhc2hUcmVhcE1hcCROb2Rlf2t9acJIPnQCAANMAANrZXl0ABJMamF2YS9sYW5nL09iamVjdDtMAARuZXh0dAA1TGRhdGFzdHJ1Y3R1cmVzL3RyZWFwL0hhc2hUcmVhcE1hcCRNb3JlS2V5VmFsdWVQYWlycztMAAV2YWx1ZXEAfgA3eHIAIWRhdGFzdHJ1Y3R1cmVzLnRyZWFwLkhhc2hUcmVhcE1hcPMJ/2vt3boKAgAAeHIAHWRhdGFzdHJ1Y3R1cmVzLnRyZWFwLlRyZWFwTWFw46LAyn3v5moCAAB4cgAaZGF0YXN0cnVjdHVyZXMudHJlYXAuVHJlYXA88f21zZwbdQIAAkwABGxlZnR0ABxMZGF0YXN0cnVjdHVyZXMvdHJlYXAvVHJlYXA7TAAFcmlnaHRxAH4APHhwcHNxAH4ANnBzcQB+ADZwcHNyAAt0YWMuTWV0YUtleVF/W3MiCfIZAgADTAAPZXJhc3VyZVN0cmF0ZWd5dAAdTHRhYy9NZXRhS2V5JEVyYXN1cmVTdHJhdGVneTtMAARuYW1lcQB+ADJMAAN0eXB0ABFMamF2YS9sYW5nL0NsYXNzO3hwfnIAG3RhYy5NZXRhS2V5JEVyYXN1cmVTdHJhdGVneQAAAAAAAAAAEgAAeHIADmphdmEubGFuZy5FbnVtAAAAAAAAAAASAAB4cHQACUNhbm9uaWNhbHQAF3RhYy5tZW1vcnkucGFydGl0aW9uLWlkdnIAEWphdmEubGFuZy5JbnRlZ2VyEuKgpPeBhzgCAAFJAAV2YWx1ZXhxAH4ADnBzcQB+AEkAAAACc3EAfgBAcQB+AEZ0ABJUYWMuc3ltYm9sLmtleXdvcmR2cgAQamF2YS5sYW5nLlN0cmluZ6DwpDh6O7NCAgAAeHBwdAAEdGFjTXNxAH4AQHEAfgBGdAANdGFjLmlzLm1lbW9yeXZyACJ0YWMuTWV0YU1hcCRDb21wYW5pb24kTm90aGluZ1ZhbHVl8nsHH85ykpUCAAB4cHBzcQB+AFN0AA90YWNNQ0FOT04yISExNTNzcgAPdGFjLlRhZyRCeXRlTWFwNb/Ry6GDRgkCAAB4cgALdGFjLlRhZyRNYXABJytzDV3P/QIAAHhyAAd0YWMuVGFnLk9V3gn2xngCAAB4cHBzcQB+AAz///////////////7////+AAAAAXVxAH4AEAAAAAEkeHNxAH4AKnNyADV2Yy5kYXRhLlRBQ1N5bWJvbCRWYXIkV2l0aERlZmF1bHRDYWxsSW5kZXgkV2l0aEJpdDI1NnqsyEgq0drPAgACTAAEbWV0YXEAfgAxTAAKbmFtZVByZWZpeHEAfgAyeHEAfgAzc3EAfgA2c3EAfgA2cHBxAH4ATHB0AAFMcHNxAH4AQHEAfgBGdAAQdGFjLnN0YWNrLmhlaWdodHEAfgBKcHNxAH4ASQAAA/B0AARSMTU0c3IADnRhYy5UYWckQml0MjU2IyLQT+LlKkgCAAB4cQB+AFlzcgARamF2YS51dGlsLkhhc2hNYXAFB9rBwxZg0QMAAkYACmxvYWRGYWN0b3JJAAl0aHJlc2hvbGR4cD9AAAAAAAADdwgAAAAEAAAAAnNyAB5hbmFseXNpcy5pY2ZnLlNjcmF0Y2hCeXRlUmFuZ2XBTLaPpUzj2gIAAkwABGZyb21xAH4ABkwAAnRvcQB+AAZ4cHNxAH4ADP///////////////v////4AAAAAdXEAfgAQAAAAAHhzcQB+AAz///////////////7////+AAAAAXVxAH4AEAAAAAEDeHNyAC1hbmFseXNpcy5pY2ZnLkRlY29tcG9zZWRDYWxsSW5wdXRBcmckQ29uc3RhbnSFavLdQafqPQIAA0wAAWN0ABlMdmMvZGF0YS9UQUNTeW1ib2wkQ29uc3Q7TAARY29udHJhY3RSZWZlcmVuY2V0AC9MYW5hbHlzaXMvaWNmZy9DYWxsR3JhcGhCdWlsZGVyJENhbGxlZENvbnRyYWN0O0wADHNjcmF0Y2hSYW5nZXQAIExhbmFseXNpcy9pY2ZnL1NjcmF0Y2hCeXRlUmFuZ2U7eHIAJGFuYWx5c2lzLmljZmcuRGVjb21wb3NlZENhbGxJbnB1dEFy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ZUNvbnRleHQ7eHBwc3EAfgDhAAAXHwAAACcAAAAHcQB+AIZ+cgARY29tcGlsZXIuSnVtcFR5cGUAAAAAAAAAABIAAHhxAH4ARXQAB1JFR1VMQVJzcgAWY29tcGlsZXIuU291cmNlQ29udGV4dIzLW+lAXNoTAgACTAAPaW5kZXhUb0ZpbGVwYXRocQB+ACdMAAlzb3VyY2VEaXJxAH4AMnhwc3EAfgBpP0AAAAAAAAx3CAAAABAAAAAIc3EAfgBJAAAAAHQAFWNvbnRyYWN0cy9Db250ZXh0LnNvbHNxAH4ASQAAAAF0ABhjb250cmFjdHMvQ3VydmVUb2tlbi5zb2xxAH4AS3QAH2NvbnRyYWN0cy9DdXJ2ZVRva2VuRXhhbXBsZS5zb2xzcQB+AEkAAAADdAATY29udHJhY3RzL0VSQzIwLnNvbHNxAH4ASQAAAAR0ABRjb250cmFjdHMvSUVSQzIwLnNvbHNxAH4ASQAAAAV0ABxjb250cmFjdHMvSUVSQzIwTWV0YWRhdGEuc29sc3EAfgBJAAAABnQAHWNvbnRyYWN0cy9SZWVudHJhbmN5R3VhcmQuc29sc3EAfgBJAAAAB3QAE2NvbnRyYWN0cy9jdXJ2ZS5zb2x4dAATLnBvc3RfYXV0b2ZpbmRlcnMuMnNxAH4AMHNxAH4ANnBzcQB+ADZwc3EAfgA2cHBxAH4AQ3BxAH4AS3EAfgBMcHEAfgBQcQB+AFFwcQB+AFVxAH4AVnNxAH4AXnNxAH4ANnNxAH4ANnBwcQB+AExwcQB+AGJwcQB+AGNwcQB+AK9xAH4AZnEAfgCyc3EAfgBec3EAfgA2c3EAfgA2c3EAfgA2c3EAfgA2cHNxAH4ANnBwcQB+AExwcQB+AGJzcQB+AEBxAH4ARnQAFnRhYy5zY2FsYXJpemF0aW9uLnNvcnR2cgAZdmMuZGF0YS5TY2FsYXJpemF0aW9uU29ydDDOcJ3kaA0mAgAAeHBwc3IAIHZjLmRhdGEuU2NhbGFyaXphdGlvblNvcnQkUGFja2VkLkWtEpOI5PcCAAJJAAVzdGFydEwAC3BhY2tlZFN0YXJ0dAAbTHZjL2RhdGEvU2NhbGFyaXphdGlvblNvcnQ7eHEAfgELAAAAAHNyAB92Yy5kYXRhLlNjYWxhcml6YXRpb25Tb3J0JFNwbGl0VP9Zp/HHsgUCAAFMAANpZHhxAH4ABnhxAH4BC3NxAH4ADP///////////////v////4AAAABdXEAfgAQAAAAAQt4c3EAfgA2cHNxAH4ANnBzcQB+ADZwcHNxAH4AQHEAfgBGdAAcdGFjLnN0b3JhZ2Uubm9uLWluZGV4ZWQtcGF0aHZyADVhbmFseXNpcy5zdG9yYWdlLlN0b3JhZ2VBbmFseXNpc1Jlc3VsdCROb25JbmRleGVkUGF0aAjBoEuh+j9FAgAAeHBwc3IAOmFuYWx5c2lzLnN0b3JhZ2UuU3RvcmFnZUFuYWx5c2lzUmVzdWx0JE5vbkluZGV4ZWRQYXRoJFJvb3S/N/XYpeoK/wIAAUwABHNsb3RxAH4ABnhxAH4BGXEAfgESc3EAfgBAcQB+AEZ0AA10YWMuc2xvdC50eXBldnIAOnNwZWMuY3ZsYXN0LnR5cGVkZXNjcmlwdG9ycy5FVk1UeXBlRGVzY3JpcHRvciRFVk1WYWx1ZVR5cGXGia8Cuuq4JQIAAHhyAC1zcGVjLmN2bGFzdC50eXBlZGVzY3JpcHRvcnMuRVZNVHlwZURlc2NyaXB0b3LIUanxPMJqHQIAAHhwcHNyADVzcGVjLmN2bGFzdC50eXBlZGVzY3JpcHRvcnMuRVZNVHlwZURlc2NyaXB0b3IkYWRkcmVzc3r4ZfRvl6ApAgAAeHIARHNwZWMuY3ZsYXN0LnR5cGVkZXNjcmlwdG9ycy5FVk1UeXBlRGVzY3JpcHRvciRFVk1Jc29tb3JwaGljVmFsdWVUeXBl93WYkW4QoQ8CAAB4cQB+AR9zcQB+AEBxAH4Aj3QAGHRhYy5zdG9yYWdlLnByZXR0eS5wYXRoc3ZyAB1hbmFseXNpcy5zdG9yYWdlLkRpc3BsYXlQYXRoc/dES7fD9VEWAgABTAAFcGF0aHNxAH4AHXhwcHNxAH4BJ3NyABdqYXZhLnV0aWwuTGlua2VkSGFzaFNldNhs11qV3SoeAgAAeHIAEWphdmEudXRpbC5IYXNoU2V0ukSFlZa4tzQDAAB4cHcMAAAAED9AAAAAAAABc3IAIWFuYWx5c2lzLnN0b3JhZ2UuRGlzcGxheVBhdGgkUm9vdNNzoL2Z0DxyAgACTAAEYmFzZXQAHkxhbmFseXNpcy9zdG9yYWdlL0Rpc3BsYXlQYXRoO0wABG5hbWVxAH4AMnhyABxhbmFseXNpcy5zdG9yYWdlLkRpc3BsYXlQYXRoT0Bj6lbSIAUCAAB4cHB0AAdjb2luc18xeHNxAH4AQHEAfgBGdAAVdGFjLnN0b3JhZ2UuYml0LXdpZHRocQB+AEpwc3EAfgBJAAAAoHBzcQB+AEBxAH4ARnQAC3RhYy5zdG9yYWdlcQB+AJVwcQB+AIZwcQB+AGNwc3EAfgBJAAAD9HQAC0NBTk9OMTghITIwc3EAfgB3cQB+AGhxAH4AbXNxAH4AMHNxAH4ANnBzcQB+ADZwc3EAfgA2cHBxAH4AQ3BxAH4AS3EAfgBMcHEAfgBQcQB+AFFwcQB+AFVxAH4AVnNxAH4AXnNxAH4ANnNxAH4ANnBwcQB+AExwcQB+AGJwcQB+AGNwcQB+AK9xAH4AZnEAfgCyc3IAImphdmEudXRpbC5Db2xsZWN0aW9ucyRTaW5nbGV0b25TZXQsUkGYKcCxvwIAAUwAB2VsZW1lbnRxAH4AN3hwcQB+ABRzcQB+AF5zcQB+ADZzcQB+ADZzcQB+ADZzcQB+ADZwc3EAfgA2cHBxAH4ATHBxAH4AYnEAfgEJcHEAfgEPc3EAfgA2cHNxAH4ANnBzcQB+ADZwcHEAfgEXcHEAfgEccQB+AR1wcQB+ASRxAH4BJXBzcQB+ASdzcQB+ASp3DAAAABA/QAAAAAAAAXEAfgEweHEAfgEycHEAfgE0cHEAfgE1cHEAfgCGcHEAfgBjcHEAfgE3cQB+AThzcQB+AHdxAH4AaHEAfgBt"}
		AnnotationCmd:53 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageGlobalChangeSnippet.StorageBackupPoint","calleeTxId":2}}
		NopCmd
		AssumeExpCmd LAnd(Eq(tacCalldatasize!!0:3 0x24 ) Eq(tacCalldatasize!!0:3 0x24 ) )
		NopCmd
		AssumeExpCmd Eq(tacCalldatabufCANON0@2:0 0x70a0823100000000000000000000000000000000000000000000000000000000 )
		AssignExpCmd:53 tacCalldatabufCANON1@2:76 R30:77
		LabelCmd:53 "Start procedure ERC20-balanceOf(address)"
		AnnotationCmd:53 JSON{"key":{"name":"fps.free-pointer-is-scalarized","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true}
		AssignExpCmd:53 R160:51 Select(tacExtcodesize!!7:4 Apply(to_skey:bif R29:78) )
		NopCmd
		AssumeExpCmd Gt(R160:51 0x0 )
		AnnotationCmd:53 JSON{"key":{"name":"internal.func.finder.info","type":"analysis.ip.InternalFunctionFinderReport","erasureStrategy":"Erased"},"value":"rO0ABXNyAChhbmFseXNpcy5pcC5JbnRlcm5hbEZ1bmN0aW9uRmluZGVyUmVwb3J0ian+bYn1VdACAAFMABN1bnJlc29sdmVkRnVuY3Rpb25zdAAPTGphdmEvdXRpbC9TZXQ7eHBzcgAhZGF0YXN0cnVjdHVyZXMuTGlua2VkQXJyYXlIYXNoU2V0AAAAAAAAAAEDAAJGAApsb2FkRmFjdG9yTAAJaGFzaFRhYmxldAAuTGRhdGFzdHJ1Y3R1cmVzL2FycmF5aGFzaHRhYmxlL0FycmF5SGFzaFRhYmxlO3hwdwgAAAAAQAAAAHg="}
		AnnotationCmd:53 JSON{"key":{"name":"fps.free-pointer-is-scalarized","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true}
		NopCmd
		AssumeExpCmd LNot(Lt(tacCalldatasize!!0:3 0x4 ) )
		NopCmd
		AssumeExpCmd LNot(Gt(0x39509351 tacSighash!!32:44 ) )
		NopCmd
		AssumeExpCmd LNot(Eq(0x39509351 tacSighash!!32:44 ) )
		NopCmd
		AssumeExpCmd Eq(0x70a08231 tacSighash!!32:44 )
		AssignExpCmd:79 R166:80 Sub(tacCalldatasize!!0:3 0x4 )
		AssignExpCmd:53 B167:81 Slt(R166:80 0x20 )
		NopCmd
		AssumeExpCmd LNot(B167:81 )
		AssignExpCmd:82 R169:69 tacCalldatabufCANON1@2:83
		NopCmd
		AssumeExpCmd Eq(tacCalldatabufCANON1@2:83 tacCalldatabufCANON1@2:83 )
		AnnotationCmd:53 JSON{"key":{"name":"internal.func.start","type":"analysis.ip.InternalFuncStartAnnotation","erasureStrategy":"CallTrace"},"value":{"id":1,"startPc":1712,"args":[{"s":{"namePrefix":"R169","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1013}]},"offset":1,"sort":"SCALAR"}],"methodSignature":{"#class":"spec.cvlast.QualifiedMethodSignature.QualifiedMethodSig","qualifiedMethodName":{"#class":"spec.cvlast.QualifiedFunction","host":{"name":"ERC20"},"methodId":"balanceOf"},"params":[{"#class":"spec.cvlast.VMParam.Named","name":"account","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$address"}}],"res":[{"#class":"spec.cvlast.VMParam.Unnamed","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256}}]},"stackOffsetToArgPos":{"1":0},"callSiteSrc":{"source":1,"begin":4376,"len":467,"jumpType":"ENTER","address":"ce4604a0000000000000000000000011","sourceContext":{"indexToFilepath":{"0":"contracts/Context.sol","1":"contracts/ERC20.sol","2":"contracts/IERC20.sol","3":"contracts/IERC20Metadata.sol"},"sourceDir":".post_autofinders.1"}}}}
		AssignExpCmd:84 R174:85 Apply(hash_3_keccak:bif Apply(skey_basic:bif 0x40) Apply(to_skey:bif tacCalldatabufCANON1@2:83) Apply(skey_basic:bif 0x0))
		AssignExpCmd:86 R175:85 Select(CANON93!!26:39 R174:87 )
		AnnotationCmd:53 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet","value":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R175","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1020}]},"displayPath":{"#class":"analysis.storage.DisplayPath.MapAccess","key":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R169","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1018}]},"keyTyp":{"#class":"tac.TACStorageType.IntegralType","typeLabel":"address","numBytes":"14","descriptor":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$address"},"lowerBound":null,"upperBound":null},"base":{"#class":"analysis.storage.DisplayPath.Root","name":"_balances"}},"storageType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256},"contractInstance":"ce4604a0000000000000000000000011","linkableStorageReadId":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet.None"}}}
		AnnotationCmd:53 JSON{"key":{"name":"internal.func.end","type":"analysis.ip.InternalFuncExitAnnotation","erasureStrategy":"Canonical"},"value":{"id":1,"rets":[{"s":{"namePrefix":"R175","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1023}]},"offset":0}],"functionLayout":{"0":{"#class":"analysis.ip.InternalFuncValueLocation.Scalar"}}}}
		AnnotationCmd:53 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.EVMFunctionReturnWrite","returnbufOffset":"0","returnValueSym":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R175","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1023}]},"callIndex":2}}
		AnnotationCmd:53 JSON{"key":{"name":"tac.return.path","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		LabelCmd:53 "End procedure ERC20-balanceOf(address)"
		AssignExpCmd:53 tacReturndata!!177:75 Store(tacReturndata!!156:75 0x0 R175:85 )
		AssignExpCmd:53 tacMCANON2!!178:9 Store(tacMCANON2!!153:9 0x100 R175:85 )
		AnnotationCmd:53 JSON{"key":{"name":"call.trace.pop","type":"analysis.icfg.Inliner$CallStack$PopRecord","erasureStrategy":"Canonical"},"value":"rO0ABXNyAClhbmFseXNpcy5pY2ZnLklubGluZXIkQ2FsbFN0YWNrJFBvcFJlY29yZPAPfwSLdCWJAgABSQAIY2FsbGVlSWR4cAAAAAI="}
		JumpCmd:53 1_0_0_1_0_0
	}
	Block 0_0_0_3_0_0 Succ [2_0_0_1_0_0] {
		AnnotationCmd:53 JSON{"key":{"name":"call.trace.push","type":"analysis.icfg.Inliner$CallStack$PushRecord","erasureStrategy":"Canonical"},"value":"rO0ABXNyACphbmFseXNpcy5pY2ZnLklubGluZXIkQ2FsbFN0YWNrJFB1c2hSZWNvcmSX8+DCTLCH+AIAA0kACGNhbGxlZUlkTAAGY2FsbGVldAATTHZjL2RhdGEvTWV0aG9kUmVmO0wAB3N1bW1hcnl0ABVMdmMvZGF0YS9DYWxsU3VtbWFyeTt4cAAAAANzcgARdmMuZGF0YS5NZXRob2RSZWbJlJTzzU9pGAIAA0wABGF0dHJ0ABdMc2NlbmUvTWV0aG9kQXR0cmlidXRlO0wACmNvbnRyYWN0SWR0ABZMamF2YS9tYXRoL0JpZ0ludGVnZXI7TAAHc2lnSGFzaHQAEExldm0vU2lnaGFzaEludDt4cHNyABxzY2VuZS5NZXRob2RBdHRyaWJ1dGUkQ29tbW9uNHjdebdr9XMCAAB4cgAVc2NlbmUuTWV0aG9kQXR0cmlidXRlcYg2pYWutuUCAAB4cHNyABRqYXZhLm1hdGguQmlnSW50ZWdlcoz8nx+pO/sdAwAGSQAIYml0Q291bnRJAAliaXRMZW5ndGhJABNmaXJzdE5vbnplcm9CeXRlTnVtSQAMbG93ZXN0U2V0Qml0SQAGc2lnbnVtWwAJbWFnbml0dWRldAACW0J4cgAQamF2YS5sYW5nLk51bWJlcoaslR0LlOCLAgAAeHD///////////////7////+AAAAAXVyAAJbQqzzF/gGCFTgAgAAeHAAAAAQzkYEoAAAAAAAAAAAAAAAKHhzcgAOZXZtLlNpZ2hhc2hJbnRUdcqNMXEgeAIAAUwAAW5xAH4ABnhwc3EAfgAM///////////////+/////gAAAAF1cQB+ABAAAAAEOEL3dnhzcgATdmMuZGF0YS5DYWxsU3VtbWFyeZQcmw5vl+FdAgAQSQAJc3VtbWFyeUlkTAAOY2FsbENvbnZlbnRpb250ACZMaW5zdHJ1bWVudGF0aW9uL2NhbGxzL0NhbGxDb252ZW50aW9uO0wACmNhbGxUYXJnZXR0ABpMYW5hbHlzaXMvaWNmZy9DYWxsVGFyZ2V0O0wACGNhbGxUeXBldAAVTHZjL2RhdGEvVEFDQ2FsbFR5cGU7TAAPY2Fubm90QmVJbmxpbmVkdAAtTGFuYWx5c2lzL2ljZmcvSW5saW5lciRJbGxlZ2FsSW5saW5pbmdSZWFzb247TAAGZ2FzVmFydAATTHZjL2RhdGEvVEFDU3ltYm9sO0wABmluQmFzZXEAfgAbTAAIaW5PZmZzZXRxAH4AG0wABmluU2l6ZXEAfgAbTAAMb3JpZ0NhbGxjb3JldAAgTHZjL2RhdGEvVEFDQ21kJFNpbXBsZSRDYWxsQ29yZTtMAAdvdXRCYXNlcQB+ABtMAAlvdXRPZmZzZXRxAH4AG0wAB291dFNpemVxAH4AG0wADXNpZ1Jlc29sdXRpb250AA9MamF2YS91dGlsL1NldDtMAAV0b1ZhcnEAfgAbTAAIdmFsdWVWYXJxAH4AG3hwAAAAAXNyACRpbnN0cnVtZW50YXRpb24uY2FsbHMuQ2FsbENvbnZlbnRpb25HtO1ulL788QIAA0kACGNhbGxlcklkTAAFaW5wdXR0ABlMYW5hbHlzaXMvaWNmZy9DYWxsSW5wdXQ7TAAGcmF3T3V0dAAiTGluc3RydW1lbnRhdGlvbi9jYWxscy9DYWxsT3V0cHV0O3hwAAAAAHNyABdhbmFseXNpcy5pY2ZnLkNhbGxJbnB1dJjJD1MhNUxQAgAHTAAHYmFzZVZhcnQAGUx2Yy9kYXRhL1RBQ0V4cHIkU3ltJFZhcjtMABBlbmNvZGVkQXJndW1lbnRzdAAjTGFuYWx5c2lzL2ljZmcvQUJJQXJndW1lbnRFbmNvZGluZztMABNpbnB1dFNpemVMb3dlckJvdW5kcQB+AAZMAAZvZmZzZXR0ABVMdmMvZGF0YS9UQUNFeHByJFN5bTtMABRyYW5nZVRvRGVjb21wb3NlZEFyZ3QAD0xqYXZhL3V0aWwvTWFwO0wAEHNpbXBsaWZpZWRPZmZzZXR0ABtMdmMvZGF0YS9UQUNFeHByJFN5bSRDb25zdDtMAARzaXplcQB+ACZ4cHNyABd2Yy5kYXRhLlRBQ0V4cHIkU3ltJFZhcskrg43eGgPnAgACTAABc3QAF0x2Yy9kYXRhL1RBQ1N5bWJvbCRWYXI7TAADdGFndAAJTHRhYy9UYWc7eHIAE3ZjLmRhdGEuVEFDRXhwciRTeW2iVj0S4YSNUAIAAHhyAA92Yy5kYXRhLlRBQ0V4cHJYhGlUu/v+yAIAAHhwc3IANnZjLmRhdGEuVEFDU3ltYm9sJFZhciRXaXRoRGVmYXVsdENhbGxJbmRleCRXaXRoQnl0ZU1hcJ7+oHF4CHAAAgACTAAEbWV0YXQALUxrb3RsaW54L2NvbGxlY3Rpb25zL2ltbXV0YWJsZS9QZXJzaXN0ZW50TWFwO0wACm5hbWVQcmVmaXh0ABJMamF2YS9sYW5nL1N0cmluZzt4cgAVdmMuZGF0YS5UQUNTeW1ib2wkVmFyCYrCGVl9SXYCAAB4cgARdmMuZGF0YS5UQUNTeW1ib2zd3Run/CoWswIAAHhwc3IAJmRhdGFzdHJ1Y3R1cmVzLnRyZWFwLkhhc2hUcmVhcE1hcCROb2Rlf2t9acJIPnQCAANMAANrZXl0ABJMamF2YS9sYW5nL09iamVjdDtMAARuZXh0dAA1TGRhdGFzdHJ1Y3R1cmVzL3RyZWFwL0hhc2hUcmVhcE1hcCRNb3JlS2V5VmFsdWVQYWlycztMAAV2YWx1ZXEAfgA3eHIAIWRhdGFzdHJ1Y3R1cmVzLnRyZWFwLkhhc2hUcmVhcE1hcPMJ/2vt3boKAgAAeHIAHWRhdGFzdHJ1Y3R1cmVzLnRyZWFwLlRyZWFwTWFw46LAyn3v5moCAAB4cgAaZGF0YXN0cnVjdHVyZXMudHJlYXAuVHJlYXA88f21zZwbdQIAAkwABGxlZnR0ABxMZGF0YXN0cnVjdHVyZXMvdHJlYXAvVHJlYXA7TAAFcmlnaHRxAH4APHhwcHNxAH4ANnBzcQB+ADZwcHNyAAt0YWMuTWV0YUtleVF/W3MiCfIZAgADTAAPZXJhc3VyZVN0cmF0ZWd5dAAdTHRhYy9NZXRhS2V5JEVyYXN1cmVTdHJhdGVneTtMAARuYW1lcQB+ADJMAAN0eXB0ABFMamF2YS9sYW5nL0NsYXNzO3hwfnIAG3RhYy5NZXRhS2V5JEVyYXN1cmVTdHJhdGVneQAAAAAAAAAAEgAAeHIADmphdmEubGFuZy5FbnVtAAAAAAAAAAASAAB4cHQACUNhbm9uaWNhbHQAF3RhYy5tZW1vcnkucGFydGl0aW9uLWlkdnIAEWphdmEubGFuZy5JbnRlZ2VyEuKgpPeBhzgCAAFJAAV2YWx1ZXhxAH4ADnBzcQB+AEkAAAACc3EAfgBAcQB+AEZ0ABJUYWMuc3ltYm9sLmtleXdvcmR2cgAQamF2YS5sYW5nLlN0cmluZ6DwpDh6O7NCAgAAeHBwdAAEdGFjTXNxAH4AQHEAfgBGdAANdGFjLmlzLm1lbW9yeXZyACJ0YWMuTWV0YU1hcCRDb21wYW5pb24kTm90aGluZ1ZhbHVl8nsHH85ykpUCAAB4cHBzcQB+AFN0AA90YWNNQ0FOT04yISEzODJzcgAPdGFjLlRhZyRCeXRlTWFwNb/Ry6GDRgkCAAB4cgALdGFjLlRhZyRNYXABJytzDV3P/QIAAHhyAAd0YWMuVGFnLk9V3gn2xngCAAB4cHBzcQB+AAz///////////////7////+AAAAAXVxAH4AEAAAAAFkeHNxAH4AKnNyADV2Yy5kYXRhLlRBQ1N5bWJvbCRWYXIkV2l0aERlZmF1bHRDYWxsSW5kZXgkV2l0aEJpdDI1NnqsyEgq0drPAgACTAAEbWV0YXEAfgAxTAAKbmFtZVByZWZpeHEAfgAyeHEAfgAzc3EAfgA2c3EAfgA2cHBxAH4ATHB0AAFMcHNxAH4AQHEAfgBGdAAQdGFjLnN0YWNrLmhlaWdodHEAfgBKcHNxAH4ASQAAA/h0AARSMzgzc3IADnRhYy5UYWckQml0MjU2IyLQT+LlKkgCAAB4cQB+AFlzcgARamF2YS51dGlsLkhhc2hNYXAFB9rBwxZg0QMAAkYACmxvYWRGYWN0b3JJAAl0aHJlc2hvbGR4cD9AAAAAAAADdwgAAAAEAAAAAnNyAB5hbmFseXNpcy5pY2ZnLlNjcmF0Y2hCeXRlUmFuZ2XBTLaPpUzj2gIAAkwABGZyb21xAH4ABkwAAnRvcQB+AAZ4cHNxAH4ADP///////////////v////4AAAAAdXEAfgAQAAAAAHhzcQB+AAz///////////////7////+AAAAAXVxAH4AEAAAAAEDeHNyAC1hbmFseXNpcy5pY2ZnLkRlY29tcG9zZWRDYWxsSW5wdXRBcmckQ29uc3RhbnSFavLdQafqPQIAA0wAAWN0ABlMdmMvZGF0YS9UQUNTeW1ib2wkQ29uc3Q7TAARY29udHJhY3RSZWZlcmVuY2V0AC9MYW5hbHlzaXMvaWNmZy9DYWxsR3JhcGhCdWlsZGVyJENhbGxlZENvbnRyYWN0O0wADHNjcmF0Y2hSYW5nZXQAIExhbmFseXNpcy9pY2ZnL1NjcmF0Y2hCeXRlUmFuZ2U7eHIAJGFuYWx5c2lzLmljZmcuRGVjb21wb3NlZENhbGxJbnB1dEFyZ82Nwhnirh8hAgAAeHBzcgAXdmMuZGF0YS5UQUNTeW1ib2wkQ29uc3QmHp5/l8IUcAIAAkwAA3RhZ3EAfgAsTAAFdmFsdWVxAH4ABnhxAH4ANHEAfgBoc3EAfgAM///////////////+/////gAAAAF1cQB+ABAAAAAgOEL3dgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAB4cHEAfgBsc3EAfgBrc3EAfgAM///////////////+/////gAAAAF1cQB+ABAAAAABRHhzcQB+AAz///////////////7////+AAAAAXVxAH4AEAAAAAFjeHNyAC1hbmFseXNpcy5pY2ZnLkRlY29tcG9zZWRDYWxsSW5wdXRBcmckVmFyaWFibGWV3y80jneopQIAA0wAEWNvbnRyYWN0UmVmZXJlbmNlcQB+AHNMAAxzY3JhdGNoUmFuZ2VxAH4AdEwAAXZxAH4AK3hxAH4AdXNyADxhbmFseXNpcy5pY2ZnLkNhbGxHcmFwaEJ1aWxkZXIkQ2FsbGVkQ29udHJhY3QkVW5yZXNvbHZlZFJlYWRDhKJZ0RDzoAIAAUkADXN0b3JhZ2VSZWFkSWR4cgAtYW5hbHlzaXMuaWNmZy5DYWxsR3JhcGhCdWlsZGVyJENhbGxlZENvbnRyYWN00wt1rN/LodcCAAB4cAAAAAJxAH4Ae3NxAH4AXnNxAH4ANnNxAH4ANnBzcQB+ADZzcQB+ADZzcQB+ADZwc3EAfgA2cHBxAH4ATHBxAH4AYnNxAH4AQHEAfgBGdAAWdGFjLnNjYWxhcml6YXRpb24uc29ydHZyABl2Yy5kYXRhLlNjYWxhcml6YXRpb25Tb3J0MM5wneRoDSYCAAB4cHBzcgAfdmMuZGF0YS5TY2FsYXJpemF0aW9uU29ydCRTcGxpdFT/Wafxx7IFAgABTAADaWR4cQB+AAZ4cQB+AI5zcQB+AAz///////////////7////+AAAAAXVxAH4AEAAAAAEFeHNxAH4ANnBzcQB+ADZwc3EAfgA2cHBzcQB+AEBxAH4ARnQAHHRhYy5zdG9yYWdlLm5vbi1pbmRleGVkLXBhdGh2cgA1YW5hbHlzaXMuc3RvcmFnZS5TdG9yYWdlQW5hbHlzaXNSZXN1bHQkTm9uSW5kZXhlZFBhdGgIwaBLofo/RQIAAHhwcHNyADphbmFseXNpcy5zdG9yYWdlLlN0b3JhZ2VBbmFseXNpc1Jlc3VsdCROb25JbmRleGVkUGF0aCRSb290vzf12KXqCv8CAAFMAARzbG90cQB+AAZ4cQB+AJlxAH4AknNxAH4AQHEAfgBGdAANdGFjLnNsb3QudHlwZXZyADpzcGVjLmN2bGFzdC50eXBlZGVzY3JpcHRvcnMuRVZNVHlwZURlc2NyaXB0b3IkRVZNVmFsdWVUeXBlxomvArrquCUCAAB4cgAtc3BlYy5jdmxhc3QudHlwZWRlc2NyaXB0b3JzLkVWTVR5cGVEZXNjcmlwdG9yyFGp8TzCah0CAAB4cHBzcgAzc3BlYy5jdmxhc3QudHlwZWRlc2NyaXB0b3JzLkVWTVR5cGVEZXNjcmlwdG9yJFVJbnRL+xQfR/Nlf8ACAAFJAAhiaXR3aWR0aHhyAERzcGVjLmN2bGFzdC50eXBlZGVzY3JpcHRvcnMuRVZNVHlwZURlc2NyaXB0b3IkRVZNSXNvbW9ycGhpY1ZhbHVlVHlwZfd1mJFuEKEPAgAAeHEAfgCfAAABAHNxAH4AQH5xAH4ARHQABkVyYXNlZHQAGHRhYy5zdG9yYWdlLnByZXR0eS5wYXRoc3ZyAB1hbmFseXNpcy5zdG9yYWdlLkRpc3BsYXlQYXRoc/dES7fD9VEWAgABTAAFcGF0aHNxAH4AHXhwcHNxAH4AqXNyABdqYXZhLnV0aWwuTGlua2VkSGFzaFNldNhs11qV3SoeAgAAeHIAEWphdmEudXRpbC5IYXNoU2V0ukSFlZa4tzQDAAB4cHcMAAAAED9AAAAAAAABc3IAIWFuYWx5c2lzLnN0b3JhZ2UuRGlzcGxheVBhdGgkUm9vdNNzoL2Z0DxyAgACTAAEYmFzZXQAHkxhbmFseXNpcy9zdG9yYWdlL0Rpc3BsYXlQYXRoO0wABG5hbWVxAH4AMnhyABxhbmFseXNpcy5zdG9yYWdlLkRpc3BsYXlQYXRoT0Bj6lbSIAUCAAB4cHB0AAhmdXR1cmVfQXhzcQB+AEBxAH4ARnQAFXRhYy5zdG9yYWdlLmJpdC13aWR0aHEAfgBKcHNxAH4ASQAAAQBwc3EAfgBAcQB+AEZ0AAt0YWMuc3RvcmFnZXZxAH4ADHBxAH4AD3NxAH4AQHEAfgBGdAAYdGFjLmRlY29tcC1p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"}
		AnnotationCmd:53 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageGlobalChangeSnippet.StorageBackupPoint","calleeTxId":3}}
		NopCmd
		AssumeExpCmd LAnd(Eq(tacCalldatasize!!1:3 0x64 ) Eq(tacCalldatasize!!1:3 0x64 ) )
		AssignExpCmd:53 B181:51 Eq(Select(tacCalldatabuf!!18@3:88 0x0 ) 0x3842f77600000000000000000000000000000000000000000000000000000000 )
		AssumeCmd:53 B181:51
		AssignExpCmd:53 tacCalldatabuf!!182@3:16 LongStore(tacCalldatabuf!!18@3:88 0x4 tacMCANON2!!382:9 0x124 Sub(0x64 0x4 ) )
		LabelCmd:53 "Start procedure curve-get_D(uint256[2],uint256)"
		AnnotationCmd:53 JSON{"key":{"name":"fps.free-pointer-is-scalarized","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true}
		AssignExpCmd:53 R183:51 Select(tacExtcodesize!!7:4 Apply(to_skey:bif R30:60) )
		NopCmd
		AssumeExpCmd Gt(R183:51 0x0 )
		AnnotationCmd:53 JSON{"key":{"name":"internal.func.finder.info","type":"analysis.ip.InternalFunctionFinderReport","erasureStrategy":"Erased"},"value":"rO0ABXNyAChhbmFseXNpcy5pcC5JbnRlcm5hbEZ1bmN0aW9uRmluZGVyUmVwb3J0ian+bYn1VdACAAFMABN1bnJlc29sdmVkRnVuY3Rpb25zdAAPTGphdmEvdXRpbC9TZXQ7eHBzcgAhZGF0YXN0cnVjdHVyZXMuTGlua2VkQXJyYXlIYXNoU2V0AAAAAAAAAAEDAAJGAApsb2FkRmFjdG9yTAAJaGFzaFRhYmxldAAuTGRhdGFzdHJ1Y3R1cmVzL2FycmF5aGFzaHRhYmxlL0FycmF5SGFzaFRhYmxlO3hwdwgAAAAAQAAAAHg="}
		AnnotationCmd:53 JSON{"key":{"name":"fps.free-pointer-is-scalarized","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true}
		NopCmd
		AssumeExpCmd LNot(Lt(tacCalldatasize!!1:3 0x4 ) )
		NopCmd
		AssumeExpCmd Gt(0x82c63066 tacSighash!!33:44 )
		NopCmd
		AssumeExpCmd Eq(0x3842f776 tacSighash!!33:44 )
		AssignExpCmd:89 R189:90 Sub(tacCalldatasize!!1:3 0x4 )
		AssignExpCmd:53 B190:80 Slt(R189:90 0x60 )
		NopCmd
		AssumeExpCmd LNot(B190:80 )
		NopCmd
		AssumeExpCmd Slt(0x23 tacCalldatasize!!1:91 )
		AssignExpCmd:92 R194:93 0x80
		AssumeCmd:94 true
		AssignExpCmd:53 B195:74 Gt(0x44 tacCalldatasize!!1:91 )
		NopCmd
		AssumeExpCmd LNot(B195:74 )
		AnnotationCmd:53 JSON{"key":{"name":"dsa.assign.start","type":"java.lang.String","erasureStrategy":"Erased"},"value":"4280_1005_0_0_0_0 -> 4282_1004_0_0_0_0"}
		LabelCmd:53 "Parallel assignment for R3573:bv256, R3574:bv256 := R2326:bv256, R3653:bv256"
		AnnotationCmd:53 JSON{"key":{"name":"dsa.assign.end","type":"java.lang.String","erasureStrategy":"Erased"},"value":"4280_1005_0_0_0_0 -> 4282_1004_0_0_0_0"}
		AnnotationCmd:53 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.LoopSnippet.StartLoopSnippet","loopIndex":1,"loopSource":"unknown loop source code"}}
		AnnotationCmd:53 JSON{"key":{"name":"start_loop.cmd","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		AnnotationCmd:53 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.LoopSnippet.StartIter","iteration":1}}
		AssignExpCmd:95 R197:96 Select(tacCalldatabuf!!182@3:88 0x4 )
		AssignExpCmd:97 tacMCANON3!!198:11 Store(tacMCANON3!!13:11 0x80 R197:96 )
		AnnotationCmd:53 JSON{"key":{"name":"dsa.assign.start","type":"java.lang.String","erasureStrategy":"Erased"},"value":"4301_1002_0_0_0_0 -> 4282_1004_0_0_0_0"}
		LabelCmd:53 "Parallel assignment for R3573:bv256, R3574:bv256 := R3566:bv256, R3570:bv256"
		AnnotationCmd:53 JSON{"key":{"name":"dsa.assign.end","type":"java.lang.String","erasureStrategy":"Erased"},"value":"4301_1002_0_0_0_0 -> 4282_1004_0_0_0_0"}
		AnnotationCmd:53 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.LoopSnippet.EndIter","iteration":1}}
		AnnotationCmd:53 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.LoopSnippet.StartIter","iteration":2}}
		AssignExpCmd:95 R199:96 Select(tacCalldatabuf!!182@3:88 0x24 )
		AssignExpCmd:97 tacMCANON3!!200:11 Store(tacMCANON3!!198:11 0xa0 R199:96 )
		AnnotationCmd:53 JSON{"key":{"name":"dsa.assign.start","type":"java.lang.String","erasureStrategy":"Erased"},"value":"4301_1002_0_0_0_0 -> 4282_1004_0_0_0_0"}
		LabelCmd:53 "Parallel assignment for R3573:bv256, R3574:bv256 := R3566:bv256, R3570:bv256"
		AnnotationCmd:53 JSON{"key":{"name":"dsa.assign.end","type":"java.lang.String","erasureStrategy":"Erased"},"value":"4301_1002_0_0_0_0 -> 4282_1004_0_0_0_0"}
		AnnotationCmd:53 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.LoopSnippet.EndIter","iteration":2}}
		AnnotationCmd:53 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.LoopSnippet.EndLoopSnippet","loopId":1}}
		AnnotationCmd:53 JSON{"key":{"name":"end_loop.cmd","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		AnnotationCmd:53 JSON{"key":{"name":"pta.end-allocation","type":"analysis.alloc.AllocationAnalysis$AbstractLocation","erasureStrategy":"Erased"},"value":{"prevFPWriteIdx":0,"nextFPWriteCmd":{"block":{"#class":"tac.BlockIdentifier","origStartPc":4102,"stkTop":1000,"decompCopy":0,"calleeIdx":0,"topOfStackValue":0,"freshCopy":0},"pos":1},"sort":{"#class":"analysis.alloc.AllocationAnalysis.Alloc.ConstBlock","sz":"40"}}}
		AssignExpCmd:95 R201:62 Select(tacCalldatabuf!!182@3:88 0x44 )
		AnnotationCmd:53 JSON{"key":{"name":"internal.func.start","type":"analysis.ip.InternalFuncStartAnnotation","erasureStrategy":"CallTrace"},"value":{"id":3,"startPc":558,"args":[{"s":{"namePrefix":"R194","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1001}]},"offset":1,"sort":"SCALAR"},{"s":{"namePrefix":"R201","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1012}]},"offset":2,"sort":"SCALAR"}],"methodSignature":{"#class":"spec.cvlast.QualifiedMethodSignature.QualifiedMethodSig","qualifiedMethodName":{"#class":"spec.cvlast.QualifiedFunction","host":{"name":"curve"},"methodId":"get_D"},"params":[{"#class":"spec.cvlast.VMParam.Named","name":"xp","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$StaticArrayDescriptor","location":"memory","elementType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256},"numElements":"2"}},{"#class":"spec.cvlast.VMParam.Named","name":"amp","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256}}],"res":[{"#class":"spec.cvlast.VMParam.Unnamed","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256}}]},"stackOffsetToArgPos":{"1":0,"2":1},"callSiteSrc":{"source":7,"begin":2956,"len":1542,"jumpType":"ENTER","address":"ce4604a0000000000000000000000028","sourceContext":{"indexToFilepath":{"0":"contracts/Context.sol","1":"contracts/CurveToken.sol","2":"contracts/CurveTokenExample.sol","3":"contracts/ERC20.sol","4":"contracts/IERC20.sol","5":"contracts/IERC20Metadata.sol","6":"contracts/ReentrancyGuard.sol","7":"contracts/curve.sol"},"sourceDir":".post_autofinders.2"}}}}
		AssignExpCmd:98 R202:80 Select(tacMCANON3!!200:11 0xa0 )
		AssignExpCmd:99 R203:90 Select(tacMCANON3!!200:11 0x80 )
		NopCmd
		AssumeExpCmd Apply(add_noofl:bif R203:90 R202:80)
		AssignExpCmd I206:51 Apply(safe_math_promotion:bif R203:90)
		AssignExpCmd I207:51 Apply(safe_math_promotion:bif R202:80)
		NopCmd
		AssignExpCmd R209:69 Apply(safe_math_narrow:bif IntAdd(I206:51 I207:51))
		AnnotationCmd:53 JSON{"key":{"name":"internal.func.end","type":"analysis.ip.InternalFuncExitAnnotation","erasureStrategy":"Canonical"},"value":{"id":3,"rets":[{"s":{"namePrefix":"R209","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1023}]},"offset":0}],"functionLayout":{"0":{"#class":"analysis.ip.InternalFuncValueLocation.Scalar"}}}}
		AnnotationCmd:53 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.EVMFunctionReturnWrite","returnbufOffset":"0","returnValueSym":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R209","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1023}]},"callIndex":3}}
		AnnotationCmd:53 JSON{"key":{"name":"tac.return.path","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		LabelCmd:53 "End procedure curve-get_D(uint256[2],uint256)"
		AssignExpCmd:53 tacReturndata!!211:75 Store(tacReturndata!!386:75 0x0 R209:69 )
		AssignExpCmd:53 tacMCANON2!!212:9 Store(tacMCANON2!!382:9 0x120 R209:69 )
		AnnotationCmd:53 JSON{"key":{"name":"call.trace.pop","type":"analysis.icfg.Inliner$CallStack$PopRecord","erasureStrategy":"Canonical"},"value":"rO0ABXNyAClhbmFseXNpcy5pY2ZnLklubGluZXIkQ2FsbFN0YWNrJFBvcFJlY29yZPAPfwSLdCWJAgABSQAIY2FsbGVlSWR4cAAAAAM="}
		JumpCmd:53 2_0_0_1_0_0
	}
	Block 0_0_0_4_0_0 Succ [3_0_0_1_0_0] {
		AnnotationCmd:53 JSON{"key":{"name":"call.trace.push","type":"analysis.icfg.Inliner$CallStack$PushRecord","erasureStrategy":"Canonical"},"value":"rO0ABXNyACphbmFseXNpcy5pY2ZnLklubGluZXIkQ2FsbFN0YWNrJFB1c2hSZWNvcmSX8+DCTLCH+AIAA0kACGNhbGxlZUlkTAAGY2FsbGVldAATTHZjL2RhdGEvTWV0aG9kUmVmO0wAB3N1bW1hcnl0ABVMdmMvZGF0YS9DYWxsU3VtbWFyeTt4cAAAAARzcgARdmMuZGF0YS5NZXRob2RSZWbJlJTzzU9pGAIAA0wABGF0dHJ0ABdMc2NlbmUvTWV0aG9kQXR0cmlidXRlO0wACmNvbnRyYWN0SWR0ABZMamF2YS9tYXRoL0JpZ0ludGVnZXI7TAAHc2lnSGFzaHQAEExldm0vU2lnaGFzaEludDt4cHNyABxzY2VuZS5NZXRob2RBdHRyaWJ1dGUkQ29tbW9uNHjdebdr9XMCAAB4cgAVc2NlbmUuTWV0aG9kQXR0cmlidXRlcYg2pYWutuUCAAB4cHNyABRqYXZhLm1hdGguQmlnSW50ZWdlcoz8nx+pO/sdAwAGSQAIYml0Q291bnRJAAliaXRMZW5ndGhJABNmaXJzdE5vbnplcm9CeXRlTnVtSQAMbG93ZXN0U2V0Qml0SQAGc2lnbnVtWwAJbWFnbml0dWRldAACW0J4cgAQamF2YS5sYW5nLk51bWJlcoaslR0LlOCLAgAAeHD///////////////7////+AAAAAXVyAAJbQqzzF/gGCFTgAgAAeHAAAAAQzkYEoAAAAAAAAAAAAAAACHhzcgAOZXZtLlNpZ2hhc2hJbnRUdcqNMXEgeAIAAUwAAW5xAH4ABnhwc3EAfgAM///////////////+/////gAAAAF1cQB+ABAAAAAEGBYN3XhzcgATdmMuZGF0YS5DYWxsU3VtbWFyeZQcmw5vl+FdAgAQSQAJc3VtbWFyeUlkTAAOY2FsbENvbnZlbnRpb250ACZMaW5zdHJ1bWVudGF0aW9uL2NhbGxzL0NhbGxDb252ZW50aW9uO0wACmNhbGxUYXJnZXR0ABpMYW5hbHlzaXMvaWNmZy9DYWxsVGFyZ2V0O0wACGNhbGxUeXBldAAVTHZjL2RhdGEvVEFDQ2FsbFR5cGU7TAAPY2Fubm90QmVJbmxpbmVkdAAtTGFuYWx5c2lzL2ljZmcvSW5saW5lciRJbGxlZ2FsSW5saW5pbmdSZWFzb247TAAGZ2FzVmFydAATTHZjL2RhdGEvVEFDU3ltYm9sO0wABmluQmFzZXEAfgAbTAAIaW5PZmZzZXRxAH4AG0wABmluU2l6ZXEAfgAbTAAMb3JpZ0NhbGxjb3JldAAgTHZjL2RhdGEvVEFDQ21kJFNpbXBsZSRDYWxsQ29yZTtMAAdvdXRCYXNlcQB+ABtMAAlvdXRPZmZzZXRxAH4AG0wAB291dFNpemVxAH4AG0wADXNpZ1Jlc29sdXRpb250AA9MamF2YS91dGlsL1NldDtMAAV0b1ZhcnEAfgAbTAAIdmFsdWVWYXJxAH4AG3hwAAAAAnNyACRpbnN0cnVtZW50YXRpb24uY2FsbHMuQ2FsbENvbnZlbnRpb25HtO1ulL788QIAA0kACGNhbGxlcklkTAAFaW5wdXR0ABlMYW5hbHlzaXMvaWNmZy9DYWxsSW5wdXQ7TAAGcmF3T3V0dAAiTGluc3RydW1lbnRhdGlvbi9jYWxscy9DYWxsT3V0cHV0O3hwAAAAAHNyABdhbmFseXNpcy5pY2ZnLkNhbGxJbnB1dJjJD1MhNUxQAgAHTAAHYmFzZVZhcnQAGUx2Yy9kYXRhL1RBQ0V4cHIkU3ltJFZhcjtMABBlbmNvZGVkQXJndW1lbnRzdAAjTGFuYWx5c2lzL2ljZmcvQUJJQXJndW1lbnRFbmNvZGluZztMABNpbnB1dFNpemVMb3dlckJvdW5kcQB+AAZMAAZvZmZzZXR0ABVMdmMvZGF0YS9UQUNFeHByJFN5bTtMABRyYW5nZVRvRGVjb21wb3NlZEFyZ3QAD0xqYXZhL3V0aWwvTWFwO0wAEHNpbXBsaWZpZWRPZmZzZXR0ABtMdmMvZGF0YS9UQUNFeHByJFN5bSRDb25zdDtMAARzaXplcQB+ACZ4cHNyABd2Yy5kYXRhLlRBQ0V4cHIkU3ltJFZhcskrg43eGgPnAgACTAABc3QAF0x2Yy9kYXRhL1RBQ1N5bWJvbCRWYXI7TAADdGFndAAJTHRhYy9UYWc7eHIAE3ZjLmRhdGEuVEFDRXhwciRTeW2iVj0S4YSNUAIAAHhyAA92Yy5kYXRhLlRBQ0V4cHJYhGlUu/v+yAIAAHhwc3IANnZjLmRhdGEuVEFDU3ltYm9sJFZhciRXaXRoRGVmYXVsdENhbGxJbmRleCRXaXRoQnl0ZU1hcJ7+oHF4CHAAAgACTAAEbWV0YXQALUxrb3RsaW54L2NvbGxlY3Rpb25zL2ltbXV0YWJsZS9QZXJzaXN0ZW50TWFwO0wACm5hbWVQcmVmaXh0ABJMamF2YS9sYW5nL1N0cmluZzt4cgAVdmMuZGF0YS5UQUNTeW1ib2wkVmFyCYrCGVl9SXYCAAB4cgARdmMuZGF0YS5UQUNTeW1ib2zd3Run/CoWswIAAHhwc3IAJmRhdGFzdHJ1Y3R1cmVzLnRyZWFwLkhhc2hUcmVhcE1hcCROb2Rlf2t9acJIPnQCAANMAANrZXl0ABJMamF2YS9sYW5nL09iamVjdDtMAARuZXh0dAA1TGRhdGFzdHJ1Y3R1cmVzL3RyZWFwL0hhc2hUcmVhcE1hcCRNb3JlS2V5VmFsdWVQYWlycztMAAV2YWx1ZXEAfgA3eHIAIWRhdGFzdHJ1Y3R1cmVzLnRyZWFwLkhhc2hUcmVhcE1hcPMJ/2vt3boKAgAAeHIAHWRhdGFzdHJ1Y3R1cmVzLnRyZWFwLlRyZWFwTWFw46LAyn3v5moCAAB4cgAaZGF0YXN0cnVjdHVyZXMudHJlYXAuVHJlYXA88f21zZwbdQIAAkwABGxlZnR0ABxMZGF0YXN0cnVjdHVyZXMvdHJlYXAvVHJlYXA7TAAFcmlnaHRxAH4APHhwcHNxAH4ANnBzcQB+ADZwcHNyAAt0YWMuTWV0YUtleVF/W3MiCfIZAgADTAAPZXJhc3VyZVN0cmF0ZWd5dAAdTHRhYy9NZXRhS2V5JEVyYXN1cmVTdHJhdGVneTtMAARuYW1lcQB+ADJMAAN0eXB0ABFMamF2YS9sYW5nL0NsYXNzO3hwfnIAG3RhYy5NZXRhS2V5JEVyYXN1cmVTdHJhdGVneQAAAAAAAAAAEgAAeHIADmphdmEubGFuZy5FbnVtAAAAAAAAAAASAAB4cHQACUNhbm9uaWNhbHQAF3RhYy5tZW1vcnkucGFydGl0aW9uLWlkdnIAEWphdmEubGFuZy5JbnRlZ2VyEuKgpPeBhzgCAAFJAAV2YWx1ZXhxAH4ADnBzcQB+AEkAAAACc3EAfgBAcQB+AEZ0ABJUYWMuc3ltYm9sLmtleXdvcmR2cgAQamF2YS5sYW5nLlN0cmluZ6DwpDh6O7NCAgAAeHBwdAAEdGFjTXNxAH4AQHEAfgBGdAANdGFjLmlzLm1lbW9yeXZyACJ0YWMuTWV0YU1hcCRDb21wYW5pb24kTm90aGluZ1ZhbHVl8nsHH85ykpUCAAB4cHBzcQB+AFN0AA90YWNNQ0FOT04yISE0NDBzcgAPdGFjLlRhZyRCeXRlTWFwNb/Ry6GDRgkCAAB4cgALdGFjLlRhZyRNYXABJytzDV3P/QIAAHhyAAd0YWMuVGFnLk9V3gn2xngCAAB4cHBzcQB+AAz///////////////7////+AAAAAXVxAH4AEAAAAAEEeHNxAH4AKnNyADV2Yy5kYXRhLlRBQ1N5bWJvbCRWYXIkV2l0aERlZmF1bHRDYWxsSW5kZXgkV2l0aEJpdDI1NnqsyEgq0drPAgACTAAEbWV0YXEAfgAxTAAKbmFtZVByZWZpeHEAfgAyeHEAfgAzc3EAfgA2c3EAfgA2cHBxAH4ATHB0AAFMcHNxAH4AQHEAfgBGdAAQdGFjLnN0YWNrLmhlaWdodHEAfgBKcHNxAH4ASQAAA/d0AARSNDQxc3IADnRhYy5UYWckQml0MjU2IyLQT+LlKkgCAAB4cQB+AFlzcgARamF2YS51dGlsLkhhc2hNYXAFB9rBwxZg0QMAAkYACmxvYWRGYWN0b3JJAAl0aHJlc2hvbGR4cD9AAAAAAAABdwgAAAACAAAAAXNyAB5hbmFseXNpcy5pY2ZnLlNjcmF0Y2hCeXRlUmFuZ2XBTLaPpUzj2gIAAkwABGZyb21xAH4ABkwAAnRvcQB+AAZ4cHNxAH4ADP///////////////v////4AAAAAdXEAfgAQAAAAAHhzcQB+AAz///////////////7////+AAAAAXVxAH4AEAAAAAEDeHNyAC1hbmFseXNpcy5pY2ZnLkRlY29tcG9zZWRDYWxsSW5wdXRBcmckQ29uc3RhbnSFavLdQafqPQIAA0wAAWN0ABlMdmMvZGF0YS9UQUNTeW1ib2wkQ29uc3Q7TAARY29udHJhY3RSZWZlcmVuY2V0AC9MYW5hbHlzaXMvaWNmZy9DYWxsR3JhcGhCdWlsZGVyJENhbGxlZENvbnRyYWN0O0wADHNjcmF0Y2hSYW5nZXQAIExhbmFseXNpcy9pY2ZnL1NjcmF0Y2hCeXRlUmFuZ2U7eHIAJGFuYWx5c2lzLmljZmcuRGVjb21wb3NlZENhbGxJbnB1dEFy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AH4ATHBxAH4AYnNxAH4AQHEAfgBGdAAWdGFjLnNjYWxhcml6YXRpb24uc29ydHZyABl2Yy5kYXRhLlNjYWxhcml6YXRpb25Tb3J0MM5wneRoDSYCAAB4cHBzcgAgdmMuZGF0YS5TY2FsYXJpemF0aW9uU29ydCRQYWNrZWQuRa0Sk4jk9wIAAkkABXN0YXJ0TAALcGFja2VkU3RhcnR0ABtMdmMvZGF0YS9TY2FsYXJpemF0aW9uU29ydDt4cQB+AO0AAAAAc3IAH3ZjLmRhdGEuU2NhbGFyaXphdGlvblNvcnQkU3BsaXRU/1mn8ceyBQIAAUwAA2lkeHEAfgAGeHEAfgDtc3EAfgAM///////////////+/////gAAAAF1cQB+ABAAAAABDHhzcQB+ADZwc3EAfgA2cHNxAH4ANnBwc3EAfgBAcQB+AEZ0ABx0YWMuc3RvcmFnZS5ub24taW5kZXhlZC1wYXRodnIANWFuYWx5c2lzLnN0b3JhZ2UuU3RvcmFnZUFuYWx5c2lzUmVzdWx0JE5vbkluZGV4ZWRQYXRoCMGgS6H6P0UCAAB4cHBzcgA6YW5hbHlzaXMuc3RvcmFnZS5TdG9yYWdlQW5hbHlzaXNSZXN1bHQkTm9uSW5kZXhlZFBhdGgkUm9vdL839dil6gr/AgABTAAEc2xvdHEAfgAGeHEAfgD7cQB+APRzcQB+AEBxAH4ARnQADXRhYy5zbG90LnR5cGV2cgA6c3BlYy5jdmxhc3QudHlwZWRlc2NyaXB0b3JzLkVWTVR5cGVEZXNjcmlwdG9yJEVWTVZhbHVlVHlwZcaJrwK66rglAgAAeHIALXNwZWMuY3ZsYXN0LnR5cGVkZXNjcmlwdG9ycy5FVk1UeXBlRGVzY3JpcHRvcshRqfE8wmodAgAAeHBwc3IANXNwZWMuY3ZsYXN0LnR5cGVkZXNjcmlwdG9ycy5FVk1UeXBlRGVzY3JpcHRvciRhZGRyZXNzevhl9G+XoCkCAAB4cgBEc3BlYy5jdmxhc3QudHlwZWRlc2NyaXB0b3JzLkVWTVR5cGVEZXNjcmlwdG9yJEVWTUlzb21vcnBoaWNWYWx1ZVR5cGX3dZiRbhChDwIAAHhxAH4BAXNxAH4AQH5xAH4ARHQABkVyYXNlZHQAGHRhYy5zdG9yYWdlLnByZXR0eS5wYXRoc3ZyAB1hbmFseXNpcy5zdG9yYWdlLkRpc3BsYXlQYXRoc/dES7fD9VEWAgABTAAFcGF0aHNxAH4AHXhwcHNxAH4BC3NyABdqYXZhLnV0aWwuTGlua2VkSGFzaFNldNhs11qV3SoeAgAAeHIAEWphdmEudXRpbC5IYXNoU2V0ukSFlZa4tzQDAAB4cHcMAAAAED9AAAAAAAABc3IAIWFuYWx5c2lzLnN0b3JhZ2UuRGlzcGxheVBhdGgkUm9vdNNzoL2Z0DxyAgACTAAEYmFzZXQAHkxhbmFseXNpcy9zdG9yYWdlL0Rpc3BsYXlQYXRoO0wABG5hbWVxAH4AMnhyABxhbmFseXNpcy5zdG9yYWdlLkRpc3BsYXlQYXRoT0Bj6lbSIAUCAAB4cHB0AAhscF90b2tlbnhzcQB+AEBxAH4ARnQAFXRhYy5zdG9yYWdlLmJpdC13aWR0aHEAfgBKcHNxAH4ASQAAAKBwc3EAfgBAcQB+AEZ0AAt0YWMuc3RvcmFnZXZxAH4ADHBxAH4AxnBxAH4AY3BzcQB+AEkAAAP7dAALQ0FOT04xOSEhMjFzcQB+AHdxAH4AaHEAfgBtc3EAfgAwc3EAfgA2cHNxAH4ANnBzcQB+ADZwcHEAfgBDcHEAfgBLcQB+AExwcQB+AFBxAH4AUXBxAH4AVXEAfgBWc3EAfgBec3EAfgA2c3EAfgA2cHBxAH4ATHBxAH4AYnBxAH4AY3BxAH4AjXEAfgBmcQB+AJBzcgAiamF2YS51dGlsLkNvbGxlY3Rpb25zJFNpbmdsZXRvblNldCxSQZgpwLG/AgABTAAHZWxlbWVudHEAfgA3eHBxAH4AFHNxAH4AXnNxAH4ANnNxAH4ANnNxAH4ANnNxAH4ANnBzcQB+ADZwcHEAfgBMcHEAfgBicQB+AOtwcQB+APFzcQB+ADZwc3EAfgA2cHNxAH4ANnBwcQB+APlwcQB+AP5xAH4A/3BxAH4BBnEAfgEHcHNxAH4BC3NxAH4BDncMAAAAED9AAAAAAAABcQB+ARR4cQB+ARZwcQB+ARhwcQB+ARlwcQB+AMZwcQB+AGNwcQB+ARxxAH4BHXNxAH4Ad3EAfgBocQB+AG0="}
		AnnotationCmd:53 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageGlobalChangeSnippet.StorageBackupPoint","calleeTxId":4}}
		NopCmd
		AssumeExpCmd LAnd(Eq(tacCalldatasize!!2:3 0x4 ) Eq(tacCalldatasize!!2:3 0x4 ) )
		NopCmd
		AssumeExpCmd Eq(tacCalldatabufCANON0@4:0 0x18160ddd00000000000000000000000000000000000000000000000000000000 )
		LabelCmd:53 "Start procedure CurveTokenExample-totalSupply()"
		AnnotationCmd:53 JSON{"key":{"name":"fps.free-pointer-is-scalarized","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true}
		AssignExpCmd:53 R216:51 Select(tacExtcodesize!!7:4 Apply(to_skey:bif R28:100) )
		NopCmd
		AssumeExpCmd Gt(R216:51 0x0 )
		AnnotationCmd:53 JSON{"key":{"name":"internal.func.finder.info","type":"analysis.ip.InternalFunctionFinderReport","erasureStrategy":"Erased"},"value":"rO0ABXNyAChhbmFseXNpcy5pcC5JbnRlcm5hbEZ1bmN0aW9uRmluZGVyUmVwb3J0ian+bYn1VdACAAFMABN1bnJlc29sdmVkRnVuY3Rpb25zdAAPTGphdmEvdXRpbC9TZXQ7eHBzcgAhZGF0YXN0cnVjdHVyZXMuTGlua2VkQXJyYXlIYXNoU2V0AAAAAAAAAAEDAAJGAApsb2FkRmFjdG9yTAAJaGFzaFRhYmxldAAuTGRhdGFzdHJ1Y3R1cmVzL2FycmF5aGFzaHRhYmxlL0FycmF5SGFzaFRhYmxlO3hwdwgAAAAAQAAAAHg="}
		AnnotationCmd:53 JSON{"key":{"name":"fps.free-pointer-is-scalarized","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true}
		NopCmd
		AssumeExpCmd LNot(Lt(tacCalldatasize!!2:3 0x4 ) )
		NopCmd
		AssumeExpCmd Gt(0x40c10f19 tacSighash!!34:44 )
		NopCmd
		AssumeExpCmd LNot(Eq(0x6fdde03 tacSighash!!34:44 ) )
		NopCmd
		AssumeExpCmd LNot(Eq(0x95ea7b3 tacSighash!!34:44 ) )
		NopCmd
		AssumeExpCmd Eq(0x18160ddd tacSighash!!34:44 )
		AnnotationCmd:53 JSON{"key":{"name":"internal.func.start","type":"analysis.ip.InternalFuncStartAnnotation","erasureStrategy":"CallTrace"},"value":{"id":4,"startPc":1205,"args":[],"methodSignature":{"#class":"spec.cvlast.QualifiedMethodSignature.QualifiedMethodSig","qualifiedMethodName":{"#class":"spec.cvlast.QualifiedFunction","host":{"name":"CurveTokenExample"},"methodId":"totalSupply"},"params":[],"res":[{"#class":"spec.cvlast.VMParam.Unnamed","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256}}]},"stackOffsetToArgPos":{},"callSiteSrc":{"source":3,"begin":3954,"len":364,"jumpType":"ENTER","address":"ce4604a0000000000000000000000008","sourceContext":{"indexToFilepath":{"0":"contracts/Context.sol","1":"contracts/CurveToken.sol","2":"contracts/CurveTokenExample.sol","3":"contracts/ERC20.sol","4":"contracts/IERC20.sol","5":"contracts/IERC20Metadata.sol"},"sourceDir":".post_autofinders.0"}}}}
		AnnotationCmd:53 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet","value":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"CANON87!!25","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.scalarization.sort","type":"vc.data.ScalarizationSort","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.ScalarizationSort.Split","idx":"2"}},{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.storage.bit-width","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":256},{"key":{"name":"tac.storage.pretty.paths","type":"analysis.storage.DisplayPaths","erasureStrategy":"Erased"},"value":{"paths":[{"#class":"analysis.storage.DisplayPath.Root","name":"_totalSupply"}]}},{"key":{"name":"tac.slot.type","type":"spec.cvlast.typedescriptors.EVMTypeDescriptor$EVMValueType","erasureStrategy":"Canonical"},"value":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256}},{"key":{"name":"tac.storage.non-indexed-path","type":"analysis.storage.StorageAnalysisResult$NonIndexedPath","erasureStrategy":"Canonical"},"value":{"#class":"analysis.storage.StorageAnalysisResult.NonIndexedPath.Root","slot":"2"}},{"key":{"name":"tac.storage","type":"java.math.BigInteger","erasureStrategy":"Canonical"},"value":"ce4604a0000000000000000000000008"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1021}]},"displayPath":{"#class":"analysis.storage.DisplayPath.Root","name":"_totalSupply"},"storageType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256},"contractInstance":"ce4604a0000000000000000000000008","linkableStorageReadId":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet.Id","id":4}}}
		AnnotationCmd:53 JSON{"key":{"name":"internal.func.end","type":"analysis.ip.InternalFuncExitAnnotation","erasureStrategy":"Canonical"},"value":{"id":4,"rets":[{"s":{"namePrefix":"CANON87!!25","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.scalarization.sort","type":"vc.data.ScalarizationSort","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.ScalarizationSort.Split","idx":"2"}},{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.storage.bit-width","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":256},{"key":{"name":"tac.storage.pretty.paths","type":"analysis.storage.DisplayPaths","erasureStrategy":"Erased"},"value":{"paths":[{"#class":"analysis.storage.DisplayPath.Root","name":"_totalSupply"}]}},{"key":{"name":"tac.slot.type","type":"spec.cvlast.typedescriptors.EVMTypeDescriptor$EVMValueType","erasureStrategy":"Canonical"},"value":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256}},{"key":{"name":"tac.storage.non-indexed-path","type":"analysis.storage.StorageAnalysisResult$NonIndexedPath","erasureStrategy":"Canonical"},"value":{"#class":"analysis.storage.StorageAnalysisResult.NonIndexedPath.Root","slot":"2"}},{"key":{"name":"tac.storage","type":"java.math.BigInteger","erasureStrategy":"Canonical"},"value":"ce4604a0000000000000000000000008"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1023}]},"offset":0}],"functionLayout":{"0":{"#class":"analysis.ip.InternalFuncValueLocation.Scalar"}}}}
		AnnotationCmd:53 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.EVMFunctionReturnWrite","returnbufOffset":"0","returnValueSym":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"CANON87!!25","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.scalarization.sort","type":"vc.data.ScalarizationSort","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.ScalarizationSort.Split","idx":"2"}},{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.storage.bit-width","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":256},{"key":{"name":"tac.storage.pretty.paths","type":"analysis.storage.DisplayPaths","erasureStrategy":"Erased"},"value":{"paths":[{"#class":"analysis.storage.DisplayPath.Root","name":"_totalSupply"}]}},{"key":{"name":"tac.slot.type","type":"spec.cvlast.typedescriptors.EVMTypeDescriptor$EVMValueType","erasureStrategy":"Canonical"},"value":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256}},{"key":{"name":"tac.storage.non-indexed-path","type":"analysis.storage.StorageAnalysisResult$NonIndexedPath","erasureStrategy":"Canonical"},"value":{"#class":"analysis.storage.StorageAnalysisResult.NonIndexedPath.Root","slot":"2"}},{"key":{"name":"tac.storage","type":"java.math.BigInteger","erasureStrategy":"Canonical"},"value":"ce4604a0000000000000000000000008"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1023}]},"callIndex":4}}
		AnnotationCmd:53 JSON{"key":{"name":"tac.return.path","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		LabelCmd:53 "End procedure CurveTokenExample-totalSupply()"
		AssignExpCmd:53 tacReturndata!!225:75 Store(tacReturndata!!443:75 0x0 CANON87!!25:101 )
		AssignExpCmd:53 tacMCANON2!!226:9 Store(tacMCANON2!!440:9 0x140 CANON87!!25:101 )
		AnnotationCmd:53 JSON{"key":{"name":"call.trace.pop","type":"analysis.icfg.Inliner$CallStack$PopRecord","erasureStrategy":"Canonical"},"value":"rO0ABXNyAClhbmFseXNpcy5pY2ZnLklubGluZXIkQ2FsbFN0YWNrJFBvcFJlY29yZPAPfwSLdCWJAgABSQAIY2FsbGVlSWR4cAAAAAQ="}
		JumpCmd:53 3_0_0_1_0_0
	}
	Block 0_0_0_7_0_0 Succ [0_0_0_8_0_0] {
		AnnotationCmd:102 JSON{"key":{"name":"call.trace.push","type":"analysis.icfg.Inliner$CallStack$PushRecord","erasureStrategy":"Canonical"},"value":"rO0ABXNyACphbmFseXNpcy5pY2ZnLklubGluZXIkQ2FsbFN0YWNrJFB1c2hSZWNvcmSX8+DCTLCH+AIAA0kACGNhbGxlZUlkTAAGY2FsbGVldAATTHZjL2RhdGEvTWV0aG9kUmVmO0wAB3N1bW1hcnl0ABVMdmMvZGF0YS9DYWxsU3VtbWFyeTt4cAAAAAdzcgARdmMuZGF0YS5NZXRob2RSZWbJlJTzzU9pGAIAA0wABGF0dHJ0ABdMc2NlbmUvTWV0aG9kQXR0cmlidXRlO0wACmNvbnRyYWN0SWR0ABZMamF2YS9tYXRoL0JpZ0ludGVnZXI7TAAHc2lnSGFzaHQAEExldm0vU2lnaGFzaEludDt4cHNyABxzY2VuZS5NZXRob2RBdHRyaWJ1dGUkQ29tbW9uNHjdebdr9XMCAAB4cgAVc2NlbmUuTWV0aG9kQXR0cmlidXRlcYg2pYWutuUCAAB4cHNyABRqYXZhLm1hdGguQmlnSW50ZWdlcoz8nx+pO/sdAwAGSQAIYml0Q291bnRJAAliaXRMZW5ndGhJABNmaXJzdE5vbnplcm9CeXRlTnVtSQAMbG93ZXN0U2V0Qml0SQAGc2lnbnVtWwAJbWFnbml0dWRldAACW0J4cgAQamF2YS5sYW5nLk51bWJlcoaslR0LlOCLAgAAeHD///////////////7////+AAAAAXVyAAJbQqzzF/gGCFTgAgAAeHAAAAAQzkYEoAAAAAAAAAAAAAAAKHhzcgAOZXZtLlNpZ2hhc2hJbnRUdcqNMXEgeAIAAUwAAW5xAH4ABnhwc3EAfgAM///////////////+/////gAAAAF1cQB+ABAAAAAE4lql+nhw"}
		AssignHavocCmd:102 tacCalldatasize!!227:3
		NopCmd
		AssumeExpCmd Apply(add_noofl:bif 0x4 0x0)
		NopCmd
		AssumeExpCmd Eq(0x4 tacCalldatasize!!227:3 )
		AssignExpCmd:102 B231 LAnd(Ge(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff CANON28:29 ) Le(0x0 CANON28:29 ) )
		AssertCmd:102 B231 "sanity bounds check on cvl to vm encoding of tacTmp!5085:int failed"
		AssignExpCmd:102 R232:51 Apply(safe_math_narrow:bif CANON28:29)
		NopCmd
		AssumeExpCmd LAnd(Le(R232:54 0xffffffffffffffffffffffffffffffffffffffff ) Ge(R232:54 0x0 ) )
		AssignExpCmd:102 B236 LAnd(Ge(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff CANON29:30 ) Le(0x0 CANON29:30 ) )
		AssertCmd:102 B236 "sanity bounds check on cvl to vm encoding of tacTmp!5088:int failed"
		AssignExpCmd:102 R237:51 Apply(safe_math_narrow:bif CANON29:30)
		NopCmd
		AssumeExpCmd LAnd(Le(R237:55 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff ) Ge(R237:55 0x0 ) )
		AssignExpCmd:102 B242 LAnd(Ge(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff CANON30:31 ) Le(0x0 CANON30:31 ) )
		AssertCmd:102 B242 "sanity bounds check on cvl to vm encoding of tacTmp!5092:int failed"
		AssignExpCmd:102 R243:51 Apply(safe_math_narrow:bif CANON30:31)
		NopCmd
		AssumeExpCmd LAnd(Le(R243:56 0xffffffffffffffffffffffffffffffffffffffff ) Ge(R243:56 0x0 ) )
		AssignExpCmd:102 B247 LAnd(Ge(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff CANON34:35 ) Le(0x0 CANON34:35 ) )
		AssertCmd:102 B247 "sanity bounds check on cvl to vm encoding of tacTmp!5095:int failed"
		AssignExpCmd:102 R248:51 Apply(safe_math_narrow:bif CANON34:35)
		NopCmd
		AssumeExpCmd LAnd(Le(R248:57 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff ) Ge(R248:57 0x0 ) )
		AssignExpCmd:102 B252 LAnd(Ge(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff CANON35:36 ) Le(0x0 CANON35:36 ) )
		AssertCmd:102 B252 "sanity bounds check on cvl to vm encoding of tacTmp!5098:int failed"
		AssignExpCmd:102 R253:51 Apply(safe_math_narrow:bif CANON35:36)
		NopCmd
		AssumeExpCmd LAnd(Le(R253:58 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff ) Ge(R253:58 0x0 ) )
		AssignExpCmd:102 B257 LAnd(Ge(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff CANON29:30 ) Le(0x0 CANON29:30 ) )
		AssertCmd:102 B257 "sanity bounds check on cvl to vm encoding of tacTmp!5101:int failed"
		AssignExpCmd:102 R258:51 Apply(safe_math_narrow:bif CANON29:30)
		AssignExpCmd:102 B260 LAnd(Ge(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff CANON28:29 ) Le(0x0 CANON28:29 ) )
		AssertCmd:102 B260 "sanity bounds check on cvl to vm encoding of tacTmp!5104:int failed"
		AssignExpCmd:102 R261:51 Apply(safe_math_narrow:bif CANON28:29)
		AssignExpCmd:102 R264:51 Select(tacBalance!!507:14 Apply(to_skey:bif R261:51) )
		AssignExpCmd:103 I265:51 IntSub(R264:51 R258:51 )
		AssignExpCmd:103 tacBalance!!266:14 Store(tacBalance!!507:14 Apply(to_skey:bif R261:51) I265:51 )
		AssignExpCmd:102 R267:51 Select(tacBalance!!266:14 Apply(to_skey:bif R30:43) )
		AssignExpCmd:103 R268:51 Add(R267:51 R258:51)
		NopCmd
		AssumeExpCmd Apply(add_noofl:bif R267:51 R258:51)
		AssignExpCmd:103 tacBalance!!270:14 Store(tacBalance!!266:14 Apply(to_skey:bif R30:43) R268:51 )
		AnnotationCmd:102 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.BalanceSnippet","srcAccountInfo":{"old":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R264","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}]},"new":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"I265","tag":{"#class":"tac.Tag.Int"},"callIndex":0,"meta":[{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}]},"addr":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R261","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}]}},"trgAccountInfo":{"old":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R267","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}]},"new":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R268","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}]},"addr":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R30","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"tacContractAt"},{"key":{"name":"tac.contract.sym.addr.name","type":"java.lang.String","erasureStrategy":"Erased"},"value":"curve"},{"key":{"name":"tac.contract.sym.addr","type":"java.math.BigInteger","erasureStrategy":"Erased"},"value":"ce4604a0000000000000000000000028"}]}},"transferredAmount":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R258","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}]}}}
		LabelCmd:102 "Start procedure curve-getVirtualPrice()"
		AnnotationCmd:102 JSON{"key":{"name":"fps.free-pointer-is-scalarized","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true}
		AssignExpCmd:102 R271:51 Select(tacExtcodesize!!7:4 Apply(to_skey:bif R30:60) )
		NopCmd
		AssumeExpCmd Gt(R271:51 0x0 )
		AnnotationCmd:102 JSON{"key":{"name":"internal.func.finder.info","type":"analysis.ip.InternalFunctionFinderReport","erasureStrategy":"Erased"},"value":"rO0ABXNyAChhbmFseXNpcy5pcC5JbnRlcm5hbEZ1bmN0aW9uRmluZGVyUmVwb3J0ian+bYn1VdACAAFMABN1bnJlc29sdmVkRnVuY3Rpb25zdAAPTGphdmEvdXRpbC9TZXQ7eHBzcgAhZGF0YXN0cnVjdHVyZXMuTGlua2VkQXJyYXlIYXNoU2V0AAAAAAAAAAEDAAJGAApsb2FkRmFjdG9yTAAJaGFzaFRhYmxldAAuTGRhdGFzdHJ1Y3R1cmVzL2FycmF5aGFzaHRhYmxlL0FycmF5SGFzaFRhYmxlO3hwdwgAAAAAQAAAAHg="}
		AnnotationCmd:102 JSON{"key":{"name":"fps.free-pointer-is-scalarized","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true}
		NopCmd
		AssumeExpCmd Eq(R237:51 0x0 )
		NopCmd
		AssumeExpCmd LNot(Lt(tacCalldatasize!!227:3 0x4 ) )
		NopCmd
		AssumeExpCmd LNot(Gt(0x82c63066 tacSighash!!37:44 ) )
		NopCmd
		AssumeExpCmd LNot(Eq(0x82c63066 tacSighash!!37:44 ) )
		NopCmd
		AssumeExpCmd LNot(Eq(0x89295a45 tacSighash!!37:44 ) )
		NopCmd
		AssumeExpCmd LNot(Eq(0x9d1e1f25 tacSighash!!37:44 ) )
		NopCmd
		AssumeExpCmd LNot(Eq(0xac8c9059 tacSighash!!37:44 ) )
		NopCmd
		AssumeExpCmd LNot(Eq(0xd802e4f7 tacSighash!!37:44 ) )
		NopCmd
		AssumeExpCmd Eq(0xe25aa5fa tacSighash!!37:44 )
		AnnotationCmd:102 JSON{"key":{"name":"internal.func.start","type":"analysis.ip.InternalFuncStartAnnotation","erasureStrategy":"CallTrace"},"value":{"id":6,"startPc":2909,"args":[],"methodSignature":{"#class":"spec.cvlast.QualifiedMethodSignature.QualifiedMethodSig","qualifiedMethodName":{"#class":"spec.cvlast.QualifiedFunction","host":{"name":"curve"},"methodId":"getVirtualPrice"},"params":[],"res":[{"#class":"spec.cvlast.VMParam.Unnamed","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256}}]},"stackOffsetToArgPos":{},"callSiteSrc":{"source":7,"begin":5992,"len":476,"jumpType":"ENTER","address":"ce4604a0000000000000000000000028","sourceContext":{"indexToFilepath":{"0":"contracts/Context.sol","1":"contracts/CurveToken.sol","2":"contracts/CurveTokenExample.sol","3":"contracts/ERC20.sol","4":"contracts/IERC20.sol","5":"contracts/IERC20Metadata.sol","6":"contracts/ReentrancyGuard.sol","7":"contracts/curve.sol"},"sourceDir":".post_autofinders.2"}}}}
		AnnotationCmd:102 JSON{"key":{"name":"pta.end-allocation","type":"analysis.alloc.AllocationAnalysis$AbstractLocation","erasureStrategy":"Erased"},"value":{"prevFPWriteIdx":0,"nextFPWriteCmd":{"block":{"#class":"tac.BlockIdentifier","origStartPc":16,"stkTop":1024,"decompCopy":0,"calleeIdx":0,"topOfStackValue":2,"freshCopy":0},"pos":34},"sort":{"#class":"analysis.alloc.AllocationAnalysis.Alloc.ConstBlock","sz":"40"}}}
		AssignExpCmd:104 R283:62 Select(CANON77!!24:37 Apply(skey_basic:bif 0x8) )
		AnnotationCmd:102 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet","value":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R283","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1012}]},"displayPath":{"#class":"analysis.storage.DisplayPath.ArrayAccess","index":{"#class":"vc.data.TACSymbol.Const","value":"0"},"base":{"#class":"analysis.storage.DisplayPath.Root","name":"admin_balances"}},"storageType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256},"contractInstance":"ce4604a0000000000000000000000028","linkableStorageReadId":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet.None"}}}
		AssignExpCmd:105 R284:64 Select(tacBalance!!270:14 Apply(to_skey:bif R30:60) )
		NopCmd
		AssumeExpCmd LNot(Lt(R284:64 R283:62 ) )
		AssignExpCmd:106 R286:66 Sub(R284:64 R283:62 )
		AssignExpCmd:107 tacMCANON1!!287:8 Store(tacMCANON1!!10:8 0xc0 R286:66 )
		AssignExpCmd:108 R288:69 Select(CANON77!!24:37 Apply(skey_basic:bif 0x9) )
		AnnotationCmd:102 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet","value":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R288","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1013}]},"displayPath":{"#class":"analysis.storage.DisplayPath.ArrayAccess","index":{"#class":"vc.data.TACSymbol.Const","value":"1"},"base":{"#class":"analysis.storage.DisplayPath.Root","name":"admin_balances"}},"storageType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256},"contractInstance":"ce4604a0000000000000000000000028","linkableStorageReadId":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet.None"}}}
		AssignExpCmd:102 B290:51 Le(CANON18!!20:70 0xffffffffffffffffffffffffffffffffffffffff )
		AssignExpCmd:102 B291:51 Ge(CANON18!!20:70 0x0 )
		NopCmd
		AssumeExpCmd LAnd(B290:51 B291:51 )
		AnnotationCmd:102 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet","value":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"CANON18!!20","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.scalarization.sort","type":"vc.data.ScalarizationSort","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.ScalarizationSort.Packed","packedStart":{"#class":"vc.data.ScalarizationSort.Split","idx":"b"},"start":0}},{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.storage.bit-width","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":160},{"key":{"name":"tac.storage.pretty.paths","type":"analysis.storage.DisplayPaths","erasureStrategy":"Erased"},"value":{"paths":[{"#class":"analysis.storage.DisplayPath.Root","name":"coins_1"}]}},{"key":{"name":"tac.slot.type","type":"spec.cvlast.typedescriptors.EVMTypeDescriptor$EVMValueType","erasureStrategy":"Canonical"},"value":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.address"}},{"key":{"name":"tac.storage.non-indexed-path","type":"analysis.storage.StorageAnalysisResult$NonIndexedPath","erasureStrategy":"Canonical"},"value":{"#class":"analysis.storage.StorageAnalysisResult.NonIndexedPath.Root","slot":"b"}},{"key":{"name":"tac.storage","type":"java.math.BigInteger","erasureStrategy":"Canonical"},"value":"ce4604a0000000000000000000000028"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1011}]},"displayPath":{"#class":"analysis.storage.DisplayPath.Root","name":"coins_1"},"storageType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.address"},"contractInstance":"ce4604a0000000000000000000000028","linkableStorageReadId":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet.Id","id":7}}}
		AnnotationCmd:102 JSON{"key":{"name":"init.reorder.fence","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		AssignExpCmd:109 tacMCANON2!!294:10 Store(tacMCANON2!!12:10 0x100 0x70a0823100000000000000000000000000000000000000000000000000000000 )
		AssignExpCmd:110 tacMCANON2!!296:10 Store(tacMCANON2!!294:10 0x104 R30:43 )
		AssignExpCmd:109 R297:73 0x100
		AssignHavocCmd:109 R298:74
		AssignHavocCmd:102 tacReturndata!!299:75
		JumpCmd:102 0_0_0_8_0_0
	}
	Block 0_0_0_8_0_0 Succ [1_0_0_7_0_0] {
		AnnotationCmd:102 JSON{"key":{"name":"call.trace.push","type":"analysis.icfg.Inliner$CallStack$PushRecord","erasureStrategy":"Canonical"},"value":"rO0ABXNyACphbmFseXNpcy5pY2ZnLklubGluZXIkQ2FsbFN0YWNrJFB1c2hSZWNvcmSX8+DCTLCH+AIAA0kACGNhbGxlZUlkTAAGY2FsbGVldAATTHZjL2RhdGEvTWV0aG9kUmVmO0wAB3N1bW1hcnl0ABVMdmMvZGF0YS9DYWxsU3VtbWFyeTt4cAAAAAhzcgARdmMuZGF0YS5NZXRob2RSZWbJlJTzzU9pGAIAA0wABGF0dHJ0ABdMc2NlbmUvTWV0aG9kQXR0cmlidXRlO0wACmNvbnRyYWN0SWR0ABZMamF2YS9tYXRoL0JpZ0ludGVnZXI7TAAHc2lnSGFzaHQAEExldm0vU2lnaGFzaEludDt4cHNyABxzY2VuZS5NZXRob2RBdHRyaWJ1dGUkQ29tbW9uNHjdebdr9XMCAAB4cgAVc2NlbmUuTWV0aG9kQXR0cmlidXRlcYg2pYWutuUCAAB4cHNyABRqYXZhLm1hdGguQmlnSW50ZWdlcoz8nx+pO/sdAwAGSQAIYml0Q291bnRJAAliaXRMZW5ndGhJABNmaXJzdE5vbnplcm9CeXRlTnVtSQAMbG93ZXN0U2V0Qml0SQAGc2lnbnVtWwAJbWFnbml0dWRldAACW0J4cgAQamF2YS5sYW5nLk51bWJlcoaslR0LlOCLAgAAeHD///////////////7////+AAAAAXVyAAJbQqzzF/gGCFTgAgAAeHAAAAAQzkYEoAAAAAAAAAAAAAAAEXhzcgAOZXZtLlNpZ2hhc2hJbnRUdcqNMXEgeAIAAUwAAW5xAH4ABnhwc3EAfgAM///////////////+/////gAAAAF1cQB+ABAAAAAEcKCCMXhzcgATdmMuZGF0YS5DYWxsU3VtbWFyeZQcmw5vl+FdAgAQSQAJc3VtbWFyeUlkTAAOY2FsbENvbnZlbnRpb250ACZMaW5zdHJ1bWVudGF0aW9uL2NhbGxzL0NhbGxDb252ZW50aW9uO0wACmNhbGxUYXJnZXR0ABpMYW5hbHlzaXMvaWNmZy9DYWxsVGFyZ2V0O0wACGNhbGxUeXBldAAVTHZjL2RhdGEvVEFDQ2FsbFR5cGU7TAAPY2Fubm90QmVJbmxpbmVkdAAtTGFuYWx5c2lzL2ljZmcvSW5saW5lciRJbGxlZ2FsSW5saW5pbmdSZWFzb247TAAGZ2FzVmFydAATTHZjL2RhdGEvVEFDU3ltYm9sO0wABmluQmFzZXEAfgAbTAAIaW5PZmZzZXRxAH4AG0wABmluU2l6ZXEAfgAbTAAMb3JpZ0NhbGxjb3JldAAgTHZjL2RhdGEvVEFDQ21kJFNpbXBsZSRDYWxsQ29yZTtMAAdvdXRCYXNlcQB+ABtMAAlvdXRPZmZzZXRxAH4AG0wAB291dFNpemVxAH4AG0wADXNpZ1Jlc29sdXRpb250AA9MamF2YS91dGlsL1NldDtMAAV0b1ZhcnEAfgAbTAAIdmFsdWVWYXJxAH4AG3hwAAAABHNyACRpbnN0cnVtZW50YXRpb24uY2FsbHMuQ2FsbENvbnZlbnRpb25HtO1ulL788QIAA0kACGNhbGxlcklkTAAFaW5wdXR0ABlMYW5hbHlzaXMvaWNmZy9DYWxsSW5wdXQ7TAAGcmF3T3V0dAAiTGluc3RydW1lbnRhdGlvbi9jYWxscy9DYWxsT3V0cHV0O3hwAAAAAHNyABdhbmFseXNpcy5pY2ZnLkNhbGxJbnB1dJjJD1MhNUxQAgAHTAAHYmFzZVZhcnQAGUx2Yy9kYXRhL1RBQ0V4cHIkU3ltJFZhcjtMABBlbmNvZGVkQXJndW1lbnRzdAAjTGFuYWx5c2lzL2ljZmcvQUJJQXJndW1lbnRFbmNvZGluZztMABNpbnB1dFNpemVMb3dlckJvdW5kcQB+AAZMAAZvZmZzZXR0ABVMdmMvZGF0YS9UQUNFeHByJFN5bTtMABRyYW5nZVRvRGVjb21wb3NlZEFyZ3QAD0xqYXZhL3V0aWwvTWFwO0wAEHNpbXBsaWZpZWRPZmZzZXR0ABtMdmMvZGF0YS9UQUNFeHByJFN5bSRDb25zdDtMAARzaXplcQB+ACZ4cHNyABd2Yy5kYXRhLlRBQ0V4cHIkU3ltJFZhcskrg43eGgPnAgACTAABc3QAF0x2Yy9kYXRhL1RBQ1N5bWJvbCRWYXI7TAADdGFndAAJTHRhYy9UYWc7eHIAE3ZjLmRhdGEuVEFDRXhwciRTeW2iVj0S4YSNUAIAAHhyAA92Yy5kYXRhLlRBQ0V4cHJYhGlUu/v+yAIAAHhwc3IANnZjLmRhdGEuVEFDU3ltYm9sJFZhciRXaXRoRGVmYXVsdENhbGxJbmRleCRXaXRoQnl0ZU1hcJ7+oHF4CHAAAgACTAAEbWV0YXQALUxrb3RsaW54L2NvbGxlY3Rpb25zL2ltbXV0YWJsZS9QZXJzaXN0ZW50TWFwO0wACm5hbWVQcmVmaXh0ABJMamF2YS9sYW5nL1N0cmluZzt4cgAVdmMuZGF0YS5UQUNTeW1ib2wkVmFyCYrCGVl9SXYCAAB4cgARdmMuZGF0YS5UQUNTeW1ib2zd3Run/CoWswIAAHhwc3IAJmRhdGFzdHJ1Y3R1cmVzLnRyZWFwLkhhc2hUcmVhcE1hcCROb2Rlf2t9acJIPnQCAANMAANrZXl0ABJMamF2YS9sYW5nL09iamVjdDtMAARuZXh0dAA1TGRhdGFzdHJ1Y3R1cmVzL3RyZWFwL0hhc2hUcmVhcE1hcCRNb3JlS2V5VmFsdWVQYWlycztMAAV2YWx1ZXEAfgA3eHIAIWRhdGFzdHJ1Y3R1cmVzLnRyZWFwLkhhc2hUcmVhcE1hcPMJ/2vt3boKAgAAeHIAHWRhdGFzdHJ1Y3R1cmVzLnRyZWFwLlRyZWFwTWFw46LAyn3v5moCAAB4cgAaZGF0YXN0cnVjdHVyZXMudHJlYXAuVHJlYXA88f21zZwbdQIAAkwABGxlZnR0ABxMZGF0YXN0cnVjdHVyZXMvdHJlYXAvVHJlYXA7TAAFcmlnaHRxAH4APHhwcHNxAH4ANnBzcQB+ADZwcHNyAAt0YWMuTWV0YUtleVF/W3MiCfIZAgADTAAPZXJhc3VyZVN0cmF0ZWd5dAAdTHRhYy9NZXRhS2V5JEVyYXN1cmVTdHJhdGVneTtMAARuYW1lcQB+ADJMAAN0eXB0ABFMamF2YS9sYW5nL0NsYXNzO3hwfnIAG3RhYy5NZXRhS2V5JEVyYXN1cmVTdHJhdGVneQAAAAAAAAAAEgAAeHIADmphdmEubGFuZy5FbnVtAAAAAAAAAAASAAB4cHQACUNhbm9uaWNhbHQAF3RhYy5tZW1vcnkucGFydGl0aW9uLWlkdnIAEWphdmEubGFuZy5JbnRlZ2VyEuKgpPeBhzgCAAFJAAV2YWx1ZXhxAH4ADnBzcQB+AEkAAAAJc3EAfgBAcQB+AEZ0ABJUYWMuc3ltYm9sLmtleXdvcmR2cgAQamF2YS5sYW5nLlN0cmluZ6DwpDh6O7NCAgAAeHBwdAAEdGFjTXNxAH4AQHEAfgBGdAANdGFjLmlzLm1lbW9yeXZyACJ0YWMuTWV0YU1hcCRDb21wYW5pb24kTm90aGluZ1ZhbHVl8nsHH85ykpUCAAB4cHBzcQB+AFN0AA90YWNNQ0FOT04yISEyOTZzcgAPdGFjLlRhZyRCeXRlTWFwNb/Ry6GDRgkCAAB4cgALdGFjLlRhZyRNYXABJytzDV3P/QIAAHhyAAd0YWMuVGFnLk9V3gn2xngCAAB4cHBzcQB+AAz///////////////7////+AAAAAXVxAH4AEAAAAAEkeHNxAH4AKnNyADV2Yy5kYXRhLlRBQ1N5bWJvbCRWYXIkV2l0aERlZmF1bHRDYWxsSW5kZXgkV2l0aEJpdDI1NnqsyEgq0drPAgACTAAEbWV0YXEAfgAxTAAKbmFtZVByZWZpeHEAfgAyeHEAfgAzc3EAfgA2c3EAfgA2cHBxAH4ATHB0AAFMcHNxAH4AQHEAfgBGdAAQdGFjLnN0YWNrLmhlaWdodHEAfgBKcHNxAH4ASQAAA/B0AARSMjk3c3IADnRhYy5UYWckQml0MjU2IyLQT+LlKkgCAAB4cQB+AFlzcgARamF2YS51dGlsLkhhc2hNYXAFB9rBwxZg0QMAAkYACmxvYWRGYWN0b3JJAAl0aHJlc2hvbGR4cD9AAAAAAAADdwgAAAAEAAAAAnNyAB5hbmFseXNpcy5pY2ZnLlNjcmF0Y2hCeXRlUmFuZ2XBTLaPpUzj2gIAAkwABGZyb21xAH4ABkwAAnRvcQB+AAZ4cHNxAH4ADP///////////////v////4AAAAAdXEAfgAQAAAAAHhzcQB+AAz///////////////7////+AAAAAXVxAH4AEAAAAAEDeHNyAC1hbmFseXNpcy5pY2ZnLkRlY29tcG9zZWRDYWxsSW5wdXRBcmckQ29uc3RhbnSFavLdQafqPQIAA0wAAWN0ABlMdmMvZGF0YS9UQUNTeW1ib2wkQ29uc3Q7TAARY29udHJhY3RSZWZlcmVuY2V0AC9MYW5hbHlzaXMvaWNmZy9DYWxsR3JhcGhCdWlsZGVyJENhbGxlZENvbnRyYWN0O0wADHNjcmF0Y2hSYW5nZXQAIExhbmFseXNpcy9pY2ZnL1NjcmF0Y2hCeXRlUmFuZ2U7eHIAJGFuYWx5c2lzLmljZmcuRGVjb21wb3NlZENhbGxJbnB1dEFy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ZUNvbnRleHQ7eHBwc3EAfgDhAAAXHwAAACcAAAAHcQB+AIZ+cgARY29tcGlsZXIuSnVtcFR5cGUAAAAAAAAAABIAAHhxAH4ARXQAB1JFR1VMQVJzcgAWY29tcGlsZXIuU291cmNlQ29udGV4dIzLW+lAXNoTAgACTAAPaW5kZXhUb0ZpbGVwYXRocQB+ACdMAAlzb3VyY2VEaXJxAH4AMnhwc3EAfgBpP0AAAAAAAAx3CAAAABAAAAAIc3EAfgBJAAAAAHQAFWNvbnRyYWN0cy9Db250ZXh0LnNvbHNxAH4ASQAAAAF0ABhjb250cmFjdHMvQ3VydmVUb2tlbi5zb2xzcQB+AEkAAAACdAAfY29udHJhY3RzL0N1cnZlVG9rZW5FeGFtcGxlLnNvbHNxAH4ASQAAAAN0ABNjb250cmFjdHMvRVJDMjAuc29sc3EAfgBJAAAABHQAFGNvbnRyYWN0cy9JRVJDMjAuc29sc3EAfgBJAAAABXQAHGNvbnRyYWN0cy9JRVJDMjBNZXRhZGF0YS5zb2xzcQB+AEkAAAAGdAAdY29udHJhY3RzL1JlZW50cmFuY3lHdWFyZC5zb2xzcQB+AEkAAAAHdAATY29udHJhY3RzL2N1cnZlLnNvbHh0ABMucG9zdF9hdXRvZmluZGVycy4yc3EAfgAwc3EAfgA2cHNxAH4ANnBzcQB+ADZwcHEAfgBDcHEAfgBLcQB+AExwcQB+AFBxAH4AUXBxAH4AVXEAfgBWc3EAfgBec3EAfgA2c3EAfgA2cHBxAH4ATHBxAH4AYnBxAH4AY3BxAH4Ar3EAfgBmcQB+ALJzcQB+AF5zcQB+ADZzcQB+ADZzcQB+ADZzcQB+ADZwc3EAfgA2cHBxAH4ATHBxAH4AYnNxAH4AQHEAfgBGdAAWdGFjLnNjYWxhcml6YXRpb24uc29ydHZyABl2Yy5kYXRhLlNjYWxhcml6YXRpb25Tb3J0MM5wneRoDSYCAAB4cHBzcgAgdmMuZGF0YS5TY2FsYXJpemF0aW9uU29ydCRQYWNrZWQuRa0Sk4jk9wIAAkkABXN0YXJ0TAALcGFja2VkU3RhcnR0ABtMdmMvZGF0YS9TY2FsYXJpemF0aW9uU29ydDt4cQB+AQwAAAAAc3IAH3ZjLmRhdGEuU2NhbGFyaXphdGlvblNvcnQkU3BsaXRU/1mn8ceyBQIAAUwAA2lkeHEAfgAGeHEAfgEMc3EAfgAM///////////////+/////gAAAAF1cQB+ABAAAAABC3hzcQB+ADZwc3EAfgA2cHNxAH4ANnBwc3EAfgBAcQB+AEZ0ABx0YWMuc3RvcmFnZS5ub24taW5kZXhlZC1wYXRodnIANWFuYWx5c2lzLnN0b3JhZ2UuU3RvcmFnZUFuYWx5c2lzUmVzdWx0JE5vbkluZGV4ZWRQYXRoCMGgS6H6P0UCAAB4cHBzcgA6YW5hbHlzaXMuc3RvcmFnZS5TdG9yYWdlQW5hbHlzaXNSZXN1bHQkTm9uSW5kZXhlZFBhdGgkUm9vdL839dil6gr/AgABTAAEc2xvdHEAfgAGeHEAfgEacQB+ARNzcQB+AEBxAH4ARnQADXRhYy5zbG90LnR5cGV2cgA6c3BlYy5jdmxhc3QudHlwZWRlc2NyaXB0b3JzLkVWTVR5cGVEZXNjcmlwdG9yJEVWTVZhbHVlVHlwZcaJrwK66rglAgAAeHIALXNwZWMuY3ZsYXN0LnR5cGVkZXNjcmlwdG9ycy5FVk1UeXBlRGVzY3JpcHRvcshRqfE8wmodAgAAeHBwc3IANXNwZWMuY3ZsYXN0LnR5cGVkZXNjcmlwdG9ycy5FVk1UeXBlRGVzY3JpcHRvciRhZGRyZXNzevhl9G+XoCkCAAB4cgBEc3BlYy5jdmxhc3QudHlwZWRlc2NyaXB0b3JzLkVWTVR5cGVEZXNjcmlwdG9yJEVWTUlzb21vcnBoaWNWYWx1ZVR5cGX3dZiRbhChDwIAAHhxAH4BIHNxAH4AQHEAfgCPdAAYdGFjLnN0b3JhZ2UucHJldHR5LnBhdGhzdnIAHWFuYWx5c2lzLnN0b3JhZ2UuRGlzcGxheVBhdGhz90RLt8P1URYCAAFMAAVwYXRoc3EAfgAdeHBwc3EAfgEoc3IAF2phdmEudXRpbC5MaW5rZWRIYXNoU2V02GzXWpXdKh4CAAB4cgARamF2YS51dGlsLkhhc2hTZXS6RIWVlri3NAMAAHhwdwwAAAAQP0AAAAAAAAFzcgAhYW5hbHlzaXMuc3RvcmFnZS5EaXNwbGF5UGF0aCRSb29003OgvZnQPHICAAJMAARiYXNldAAeTGFuYWx5c2lzL3N0b3JhZ2UvRGlzcGxheVBhdGg7TAAEbmFtZXEAfgAyeHIAHGFuYWx5c2lzLnN0b3JhZ2UuRGlzcGxheVBhdGhPQGPqVtIgBQIAAHhwcHQAB2NvaW5zXzF4c3EAfgBAcQB+AEZ0ABV0YWMuc3RvcmFnZS5iaXQtd2lkdGhxAH4ASnBzcQB+AEkAAACgcHNxAH4AQHEAfgBGdAALdGFjLnN0b3JhZ2VxAH4AlXBxAH4AhnBxAH4AY3BzcQB+AEkAAAP0dAALQ0FOT04xOCEhMjBzcQB+AHdxAH4AaHEAfgBtc3EAfgAwc3EAfgA2cHNxAH4ANnBzcQB+ADZwcHEAfgBDcHEAfgBLcQB+AExwcQB+AFBxAH4AUXBxAH4AVXEAfgBWc3EAfgBec3EAfgA2c3EAfgA2cHBxAH4ATHBxAH4AYnBxAH4AY3BxAH4Ar3EAfgBmcQB+ALJzcgAiamF2YS51dGlsLkNvbGxlY3Rpb25zJFNpbmdsZXRvblNldCxSQZgpwLG/AgABTAAHZWxlbWVudHEAfgA3eHBxAH4AFHNxAH4AXnNxAH4ANnNxAH4ANnNxAH4ANnNxAH4ANnBzcQB+ADZwcHEAfgBMcHEAfgBicQB+AQpwcQB+ARBzcQB+ADZwc3EAfgA2cHNxAH4ANnBwcQB+ARhwcQB+AR1xAH4BHnBxAH4BJXEAfgEmcHNxAH4BKHNxAH4BK3cMAAAAED9AAAAAAAABcQB+ATF4cQB+ATNwcQB+ATVwcQB+ATZwcQB+AIZwcQB+AGNwcQB+AThxAH4BOXNxAH4Ad3EAfgBocQB+AG0="}
		AnnotationCmd:102 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageGlobalChangeSnippet.StorageBackupPoint","calleeTxId":8}}
		NopCmd
		AssumeExpCmd LAnd(Eq(tacCalldatasize!!4:3 0x24 ) Eq(tacCalldatasize!!4:3 0x24 ) )
		NopCmd
		AssumeExpCmd Eq(tacCalldatabufCANON0@8:2 0x70a0823100000000000000000000000000000000000000000000000000000000 )
		AssignExpCmd:102 tacCalldatabufCANON1@8:111 R30:77
		LabelCmd:102 "Start procedure ERC20-balanceOf(address)"
		AnnotationCmd:102 JSON{"key":{"name":"fps.free-pointer-is-scalarized","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true}
		AssignExpCmd:102 R303:51 Select(tacExtcodesize!!7:4 Apply(to_skey:bif R29:78) )
		NopCmd
		AssumeExpCmd Gt(R303:51 0x0 )
		AnnotationCmd:102 JSON{"key":{"name":"internal.func.finder.info","type":"analysis.ip.InternalFunctionFinderReport","erasureStrategy":"Erased"},"value":"rO0ABXNyAChhbmFseXNpcy5pcC5JbnRlcm5hbEZ1bmN0aW9uRmluZGVyUmVwb3J0ian+bYn1VdACAAFMABN1bnJlc29sdmVkRnVuY3Rpb25zdAAPTGphdmEvdXRpbC9TZXQ7eHBzcgAhZGF0YXN0cnVjdHVyZXMuTGlua2VkQXJyYXlIYXNoU2V0AAAAAAAAAAEDAAJGAApsb2FkRmFjdG9yTAAJaGFzaFRhYmxldAAuTGRhdGFzdHJ1Y3R1cmVzL2FycmF5aGFzaHRhYmxlL0FycmF5SGFzaFRhYmxlO3hwdwgAAAAAQAAAAHg="}
		AnnotationCmd:102 JSON{"key":{"name":"fps.free-pointer-is-scalarized","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true}
		NopCmd
		AssumeExpCmd LNot(Lt(tacCalldatasize!!4:3 0x4 ) )
		NopCmd
		AssumeExpCmd LNot(Gt(0x39509351 tacSighash!!38:44 ) )
		NopCmd
		AssumeExpCmd LNot(Eq(0x39509351 tacSighash!!38:44 ) )
		NopCmd
		AssumeExpCmd Eq(0x70a08231 tacSighash!!38:44 )
		AssignExpCmd:112 R309:80 Sub(tacCalldatasize!!4:3 0x4 )
		AssignExpCmd:102 B310:81 Slt(R309:80 0x20 )
		NopCmd
		AssumeExpCmd LNot(B310:81 )
		AssignExpCmd:113 R312:69 tacCalldatabufCANON1@8:114
		NopCmd
		AssumeExpCmd Eq(tacCalldatabufCANON1@8:114 tacCalldatabufCANON1@8:114 )
		AnnotationCmd:102 JSON{"key":{"name":"internal.func.start","type":"analysis.ip.InternalFuncStartAnnotation","erasureStrategy":"CallTrace"},"value":{"id":7,"startPc":1712,"args":[{"s":{"namePrefix":"R312","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1013}]},"offset":1,"sort":"SCALAR"}],"methodSignature":{"#class":"spec.cvlast.QualifiedMethodSignature.QualifiedMethodSig","qualifiedMethodName":{"#class":"spec.cvlast.QualifiedFunction","host":{"name":"ERC20"},"methodId":"balanceOf"},"params":[{"#class":"spec.cvlast.VMParam.Named","name":"account","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$address"}}],"res":[{"#class":"spec.cvlast.VMParam.Unnamed","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256}}]},"stackOffsetToArgPos":{"1":0},"callSiteSrc":{"source":1,"begin":4376,"len":467,"jumpType":"ENTER","address":"ce4604a0000000000000000000000011","sourceContext":{"indexToFilepath":{"0":"contracts/Context.sol","1":"contracts/ERC20.sol","2":"contracts/IERC20.sol","3":"contracts/IERC20Metadata.sol"},"sourceDir":".post_autofinders.1"}}}}
		AssignExpCmd:115 R317:85 Apply(hash_3_keccak:bif Apply(skey_basic:bif 0x40) Apply(to_skey:bif tacCalldatabufCANON1@8:114) Apply(skey_basic:bif 0x0))
		AssignExpCmd:116 R318:85 Select(CANON93!!26:39 R317:117 )
		AnnotationCmd:102 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet","value":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R318","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1020}]},"displayPath":{"#class":"analysis.storage.DisplayPath.MapAccess","key":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R312","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1018}]},"keyTyp":{"#class":"tac.TACStorageType.IntegralType","typeLabel":"address","numBytes":"14","descriptor":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$address"},"lowerBound":null,"upperBound":null},"base":{"#class":"analysis.storage.DisplayPath.Root","name":"_balances"}},"storageType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256},"contractInstance":"ce4604a0000000000000000000000011","linkableStorageReadId":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet.None"}}}
		AnnotationCmd:102 JSON{"key":{"name":"internal.func.end","type":"analysis.ip.InternalFuncExitAnnotation","erasureStrategy":"Canonical"},"value":{"id":7,"rets":[{"s":{"namePrefix":"R318","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1023}]},"offset":0}],"functionLayout":{"0":{"#class":"analysis.ip.InternalFuncValueLocation.Scalar"}}}}
		AnnotationCmd:102 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.EVMFunctionReturnWrite","returnbufOffset":"0","returnValueSym":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R318","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1023}]},"callIndex":8}}
		AnnotationCmd:102 JSON{"key":{"name":"tac.return.path","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		LabelCmd:102 "End procedure ERC20-balanceOf(address)"
		AssignExpCmd:102 tacReturndata!!320:75 Store(tacReturndata!!299:75 0x0 R318:85 )
		AssignExpCmd:102 tacMCANON2!!321:10 Store(tacMCANON2!!296:10 0x100 R318:85 )
		AnnotationCmd:102 JSON{"key":{"name":"call.trace.pop","type":"analysis.icfg.Inliner$CallStack$PopRecord","erasureStrategy":"Canonical"},"value":"rO0ABXNyAClhbmFseXNpcy5pY2ZnLklubGluZXIkQ2FsbFN0YWNrJFBvcFJlY29yZPAPfwSLdCWJAgABSQAIY2FsbGVlSWR4cAAAAAg="}
		JumpCmd:102 1_0_0_7_0_0
	}
	Block 0_0_0_9_0_0 Succ [2_0_0_7_0_0] {
		AnnotationCmd:102 JSON{"key":{"name":"call.trace.push","type":"analysis.icfg.Inliner$CallStack$PushRecord","erasureStrategy":"Canonical"},"value":"rO0ABXNyACphbmFseXNpcy5pY2ZnLklubGluZXIkQ2FsbFN0YWNrJFB1c2hSZWNvcmSX8+DCTLCH+AIAA0kACGNhbGxlZUlkTAAGY2FsbGVldAATTHZjL2RhdGEvTWV0aG9kUmVmO0wAB3N1bW1hcnl0ABVMdmMvZGF0YS9DYWxsU3VtbWFyeTt4cAAAAAlzcgARdmMuZGF0YS5NZXRob2RSZWbJlJTzzU9pGAIAA0wABGF0dHJ0ABdMc2NlbmUvTWV0aG9kQXR0cmlidXRlO0wACmNvbnRyYWN0SWR0ABZMamF2YS9tYXRoL0JpZ0ludGVnZXI7TAAHc2lnSGFzaHQAEExldm0vU2lnaGFzaEludDt4cHNyABxzY2VuZS5NZXRob2RBdHRyaWJ1dGUkQ29tbW9uNHjdebdr9XMCAAB4cgAVc2NlbmUuTWV0aG9kQXR0cmlidXRlcYg2pYWutuUCAAB4cHNyABRqYXZhLm1hdGguQmlnSW50ZWdlcoz8nx+pO/sdAwAGSQAIYml0Q291bnRJAAliaXRMZW5ndGhJABNmaXJzdE5vbnplcm9CeXRlTnVtSQAMbG93ZXN0U2V0Qml0SQAGc2lnbnVtWwAJbWFnbml0dWRldAACW0J4cgAQamF2YS5sYW5nLk51bWJlcoaslR0LlOCLAgAAeHD///////////////7////+AAAAAXVyAAJbQqzzF/gGCFTgAgAAeHAAAAAQzkYEoAAAAAAAAAAAAAAAKHhzcgAOZXZtLlNpZ2hhc2hJbnRUdcqNMXEgeAIAAUwAAW5xAH4ABnhwc3EAfgAM///////////////+/////gAAAAF1cQB+ABAAAAAEOEL3dnhzcgATdmMuZGF0YS5DYWxsU3VtbWFyeZQcmw5vl+FdAgAQSQAJc3VtbWFyeUlkTAAOY2FsbENvbnZlbnRpb250ACZMaW5zdHJ1bWVudGF0aW9uL2NhbGxzL0NhbGxDb252ZW50aW9uO0wACmNhbGxUYXJnZXR0ABpMYW5hbHlzaXMvaWNmZy9DYWxsVGFyZ2V0O0wACGNhbGxUeXBldAAVTHZjL2RhdGEvVEFDQ2FsbFR5cGU7TAAPY2Fubm90QmVJbmxpbmVkdAAtTGFuYWx5c2lzL2ljZmcvSW5saW5lciRJbGxlZ2FsSW5saW5pbmdSZWFzb247TAAGZ2FzVmFydAATTHZjL2RhdGEvVEFDU3ltYm9sO0wABmluQmFzZXEAfgAbTAAIaW5PZmZzZXRxAH4AG0wABmluU2l6ZXEAfgAbTAAMb3JpZ0NhbGxjb3JldAAgTHZjL2RhdGEvVEFDQ21kJFNpbXBsZSRDYWxsQ29yZTtMAAdvdXRCYXNlcQB+ABtMAAlvdXRPZmZzZXRxAH4AG0wAB291dFNpemVxAH4AG0wADXNpZ1Jlc29sdXRpb250AA9MamF2YS91dGlsL1NldDtMAAV0b1ZhcnEAfgAbTAAIdmFsdWVWYXJxAH4AG3hwAAAABXNyACRpbnN0cnVtZW50YXRpb24uY2FsbHMuQ2FsbENvbnZlbnRpb25HtO1ulL788QIAA0kACGNhbGxlcklkTAAFaW5wdXR0ABlMYW5hbHlzaXMvaWNmZy9DYWxsSW5wdXQ7TAAGcmF3T3V0dAAiTGluc3RydW1lbnRhdGlvbi9jYWxscy9DYWxsT3V0cHV0O3hwAAAAAHNyABdhbmFseXNpcy5pY2ZnLkNhbGxJbnB1dJjJD1MhNUxQAgAHTAAHYmFzZVZhcnQAGUx2Yy9kYXRhL1RBQ0V4cHIkU3ltJFZhcjtMABBlbmNvZGVkQXJndW1lbnRzdAAjTGFuYWx5c2lzL2ljZmcvQUJJQXJndW1lbnRFbmNvZGluZztMABNpbnB1dFNpemVMb3dlckJvdW5kcQB+AAZMAAZvZmZzZXR0ABVMdmMvZGF0YS9UQUNFeHByJFN5bTtMABRyYW5nZVRvRGVjb21wb3NlZEFyZ3QAD0xqYXZhL3V0aWwvTWFwO0wAEHNpbXBsaWZpZWRPZmZzZXR0ABtMdmMvZGF0YS9UQUNFeHByJFN5bSRDb25zdDtMAARzaXplcQB+ACZ4cHNyABd2Yy5kYXRhLlRBQ0V4cHIkU3ltJFZhcskrg43eGgPnAgACTAABc3QAF0x2Yy9kYXRhL1RBQ1N5bWJvbCRWYXI7TAADdGFndAAJTHRhYy9UYWc7eHIAE3ZjLmRhdGEuVEFDRXhwciRTeW2iVj0S4YSNUAIAAHhyAA92Yy5kYXRhLlRBQ0V4cHJYhGlUu/v+yAIAAHhwc3IANnZjLmRhdGEuVEFDU3ltYm9sJFZhciRXaXRoRGVmYXVsdENhbGxJbmRleCRXaXRoQnl0ZU1hcJ7+oHF4CHAAAgACTAAEbWV0YXQALUxrb3RsaW54L2NvbGxlY3Rpb25zL2ltbXV0YWJsZS9QZXJzaXN0ZW50TWFwO0wACm5hbWVQcmVmaXh0ABJMamF2YS9sYW5nL1N0cmluZzt4cgAVdmMuZGF0YS5UQUNTeW1ib2wkVmFyCYrCGVl9SXYCAAB4cgARdmMuZGF0YS5UQUNTeW1ib2zd3Run/CoWswIAAHhwc3IAJmRhdGFzdHJ1Y3R1cmVzLnRyZWFwLkhhc2hUcmVhcE1hcCROb2Rlf2t9acJIPnQCAANMAANrZXl0ABJMamF2YS9sYW5nL09iamVjdDtMAARuZXh0dAA1TGRhdGFzdHJ1Y3R1cmVzL3RyZWFwL0hhc2hUcmVhcE1hcCRNb3JlS2V5VmFsdWVQYWlycztMAAV2YWx1ZXEAfgA3eHIAIWRhdGFzdHJ1Y3R1cmVzLnRyZWFwLkhhc2hUcmVhcE1hcPMJ/2vt3boKAgAAeHIAHWRhdGFzdHJ1Y3R1cmVzLnRyZWFwLlRyZWFwTWFw46LAyn3v5moCAAB4cgAaZGF0YXN0cnVjdHVyZXMudHJlYXAuVHJlYXA88f21zZwbdQIAAkwABGxlZnR0ABxMZGF0YXN0cnVjdHVyZXMvdHJlYXAvVHJlYXA7TAAFcmlnaHRxAH4APHhwcHNxAH4ANnBzcQB+ADZwcHNyAAt0YWMuTWV0YUtleVF/W3MiCfIZAgADTAAPZXJhc3VyZVN0cmF0ZWd5dAAdTHRhYy9NZXRhS2V5JEVyYXN1cmVTdHJhdGVneTtMAARuYW1lcQB+ADJMAAN0eXB0ABFMamF2YS9sYW5nL0NsYXNzO3hwfnIAG3RhYy5NZXRhS2V5JEVyYXN1cmVTdHJhdGVneQAAAAAAAAAAEgAAeHIADmphdmEubGFuZy5FbnVtAAAAAAAAAAASAAB4cHQACUNhbm9uaWNhbHQAF3RhYy5tZW1vcnkucGFydGl0aW9uLWlkdnIAEWphdmEubGFuZy5JbnRlZ2VyEuKgpPeBhzgCAAFJAAV2YWx1ZXhxAH4ADnBzcQB+AEkAAAAJc3EAfgBAcQB+AEZ0ABJUYWMuc3ltYm9sLmtleXdvcmR2cgAQamF2YS5sYW5nLlN0cmluZ6DwpDh6O7NCAgAAeHBwdAAEdGFjTXNxAH4AQHEAfgBGdAANdGFjLmlzLm1lbW9yeXZyACJ0YWMuTWV0YU1hcCRDb21wYW5pb24kTm90aGluZ1ZhbHVl8nsHH85ykpUCAAB4cHBzcQB+AFN0AA90YWNNQ0FOT04yISEzOTlzcgAPdGFjLlRhZyRCeXRlTWFwNb/Ry6GDRgkCAAB4cgALdGFjLlRhZyRNYXABJytzDV3P/QIAAHhyAAd0YWMuVGFnLk9V3gn2xngCAAB4cHBzcQB+AAz///////////////7////+AAAAAXVxAH4AEAAAAAFkeHNxAH4AKnNyADV2Yy5kYXRhLlRBQ1N5bWJvbCRWYXIkV2l0aERlZmF1bHRDYWxsSW5kZXgkV2l0aEJpdDI1NnqsyEgq0drPAgACTAAEbWV0YXEAfgAxTAAKbmFtZVByZWZpeHEAfgAyeHEAfgAzc3EAfgA2c3EAfgA2cHBxAH4ATHB0AAFMcHNxAH4AQHEAfgBGdAAQdGFjLnN0YWNrLmhlaWdodHEAfgBKcHNxAH4ASQAAA/h0AARSNDAwc3IADnRhYy5UYWckQml0MjU2IyLQT+LlKkgCAAB4cQB+AFlzcgARamF2YS51dGlsLkhhc2hNYXAFB9rBwxZg0QMAAkYACmxvYWRGYWN0b3JJAAl0aHJlc2hvbGR4cD9AAAAAAAADdwgAAAAEAAAAAnNyAB5hbmFseXNpcy5pY2ZnLlNjcmF0Y2hCeXRlUmFuZ2XBTLaPpUzj2gIAAkwABGZyb21xAH4ABkwAAnRvcQB+AAZ4cHNxAH4ADP///////////////v////4AAAAAdXEAfgAQAAAAAHhzcQB+AAz///////////////7////+AAAAAXVxAH4AEAAAAAEDeHNyAC1hbmFseXNpcy5pY2ZnLkRlY29tcG9zZWRDYWxsSW5wdXRBcmckQ29uc3RhbnSFavLdQafqPQIAA0wAAWN0ABlMdmMvZGF0YS9UQUNTeW1ib2wkQ29uc3Q7TAARY29udHJhY3RSZWZlcmVuY2V0AC9MYW5hbHlzaXMvaWNmZy9DYWxsR3JhcGhCdWlsZGVyJENhbGxlZENvbnRyYWN0O0wADHNjcmF0Y2hSYW5nZXQAIExhbmFseXNpcy9pY2ZnL1NjcmF0Y2hCeXRlUmFuZ2U7eHIAJGFuYWx5c2lzLmljZmcuRGVjb21wb3NlZENhbGxJbnB1dEFyZ82Nwhnirh8hAgAAeHBzcgAXdmMuZGF0YS5UQUNTeW1ib2wkQ29uc3QmHp5/l8IUcAIAAkwAA3RhZ3EAfgAsTAAFdmFsdWVxAH4ABnhxAH4ANHEAfgBoc3EAfgAM///////////////+/////gAAAAF1cQB+ABAAAAAgOEL3dgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAB4cHEAfgBsc3EAfgBrc3EAfgAM///////////////+/////gAAAAF1cQB+ABAAAAABRHhzcQB+AAz///////////////7////+AAAAAXVxAH4AEAAAAAFjeHNyAC1hbmFseXNpcy5pY2ZnLkRlY29tcG9zZWRDYWxsSW5wdXRBcmckVmFyaWFibGWV3y80jneopQIAA0wAEWNvbnRyYWN0UmVmZXJlbmNlcQB+AHNMAAxzY3JhdGNoUmFuZ2VxAH4AdEwAAXZxAH4AK3hxAH4AdXNyADxhbmFseXNpcy5pY2ZnLkNhbGxHcmFwaEJ1aWxkZXIkQ2FsbGVkQ29udHJhY3QkVW5yZXNvbHZlZFJlYWRDhKJZ0RDzoAIAAUkADXN0b3JhZ2VSZWFkSWR4cgAtYW5hbHlzaXMuaWNmZy5DYWxsR3JhcGhCdWlsZGVyJENhbGxlZENvbnRyYWN00wt1rN/LodcCAAB4cAAAAAlxAH4Ae3NxAH4AXnNxAH4ANnNxAH4ANnBzcQB+ADZzcQB+ADZzcQB+ADZwc3EAfgA2cHBxAH4ATHBxAH4AYnNxAH4AQHEAfgBGdAAWdGFjLnNjYWxhcml6YXRpb24uc29ydHZyABl2Yy5kYXRhLlNjYWxhcml6YXRpb25Tb3J0MM5wneRoDSYCAAB4cHBzcgAfdmMuZGF0YS5TY2FsYXJpemF0aW9uU29ydCRTcGxpdFT/Wafxx7IFAgABTAADaWR4cQB+AAZ4cQB+AI5zcQB+AAz///////////////7////+AAAAAXVxAH4AEAAAAAEFeHNxAH4ANnBzcQB+ADZwc3EAfgA2cHBzcQB+AEBxAH4ARnQAHHRhYy5zdG9yYWdlLm5vbi1pbmRleGVkLXBhdGh2cgA1YW5hbHlzaXMuc3RvcmFnZS5TdG9yYWdlQW5hbHlzaXNSZXN1bHQkTm9uSW5kZXhlZFBhdGgIwaBLofo/RQIAAHhwcHNyADphbmFseXNpcy5zdG9yYWdlLlN0b3JhZ2VBbmFseXNpc1Jlc3VsdCROb25JbmRleGVkUGF0aCRSb290vzf12KXqCv8CAAFMAARzbG90cQB+AAZ4cQB+AJlxAH4AknNxAH4AQHEAfgBGdAANdGFjLnNsb3QudHlwZXZyADpzcGVjLmN2bGFzdC50eXBlZGVzY3JpcHRvcnMuRVZNVHlwZURlc2NyaXB0b3IkRVZNVmFsdWVUeXBlxomvArrquCUCAAB4cgAtc3BlYy5jdmxhc3QudHlwZWRlc2NyaXB0b3JzLkVWTVR5cGVEZXNjcmlwdG9yyFGp8TzCah0CAAB4cHBzcgAzc3BlYy5jdmxhc3QudHlwZWRlc2NyaXB0b3JzLkVWTVR5cGVEZXNjcmlwdG9yJFVJbnRL+xQfR/Nlf8ACAAFJAAhiaXR3aWR0aHhyAERzcGVjLmN2bGFzdC50eXBlZGVzY3JpcHRvcnMuRVZNVHlwZURlc2NyaXB0b3IkRVZNSXNvbW9ycGhpY1ZhbHVlVHlwZfd1mJFuEKEPAgAAeHEAfgCfAAABAHNxAH4AQH5xAH4ARHQABkVyYXNlZHQAGHRhYy5zdG9yYWdlLnByZXR0eS5wYXRoc3ZyAB1hbmFseXNpcy5zdG9yYWdlLkRpc3BsYXlQYXRoc/dES7fD9VEWAgABTAAFcGF0aHNxAH4AHXhwcHNxAH4AqXNyABdqYXZhLnV0aWwuTGlua2VkSGFzaFNldNhs11qV3SoeAgAAeHIAEWphdmEudXRpbC5IYXNoU2V0ukSFlZa4tzQDAAB4cHcMAAAAED9AAAAAAAABc3IAIWFuYWx5c2lzLnN0b3JhZ2UuRGlzcGxheVBhdGgkUm9vdNNzoL2Z0DxyAgACTAAEYmFzZXQAHkxhbmFseXNpcy9zdG9yYWdlL0Rpc3BsYXlQYXRoO0wABG5hbWVxAH4AMnhyABxhbmFseXNpcy5zdG9yYWdlLkRpc3BsYXlQYXRoT0Bj6lbSIAUCAAB4cHB0AAhmdXR1cmVfQXhzcQB+AEBxAH4ARnQAFXRhYy5zdG9yYWdlLmJpdC13aWR0aHEAfgBKcHNxAH4ASQAAAQBwc3EAfgBAcQB+AEZ0AAt0YWMuc3RvcmFnZXZxAH4ADHBxAH4AD3NxAH4AQHEAfgBGdAAYdGFjLmRlY29tcC1p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"}
		AnnotationCmd:102 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageGlobalChangeSnippet.StorageBackupPoint","calleeTxId":9}}
		NopCmd
		AssumeExpCmd LAnd(Eq(tacCalldatasize!!5:3 0x64 ) Eq(tacCalldatasize!!5:3 0x64 ) )
		AssignExpCmd:102 B324:51 Eq(Select(tacCalldatabuf!!19@9:118 0x0 ) 0x3842f77600000000000000000000000000000000000000000000000000000000 )
		AssumeCmd:102 B324:51
		AssignExpCmd:102 tacCalldatabuf!!325@9:18 LongStore(tacCalldatabuf!!19@9:118 0x4 tacMCANON2!!399:10 0x124 Sub(0x64 0x4 ) )
		LabelCmd:102 "Start procedure curve-get_D(uint256[2],uint256)"
		AnnotationCmd:102 JSON{"key":{"name":"fps.free-pointer-is-scalarized","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true}
		AssignExpCmd:102 R326:51 Select(tacExtcodesize!!7:4 Apply(to_skey:bif R30:60) )
		NopCmd
		AssumeExpCmd Gt(R326:51 0x0 )
		AnnotationCmd:102 JSON{"key":{"name":"internal.func.finder.info","type":"analysis.ip.InternalFunctionFinderReport","erasureStrategy":"Erased"},"value":"rO0ABXNyAChhbmFseXNpcy5pcC5JbnRlcm5hbEZ1bmN0aW9uRmluZGVyUmVwb3J0ian+bYn1VdACAAFMABN1bnJlc29sdmVkRnVuY3Rpb25zdAAPTGphdmEvdXRpbC9TZXQ7eHBzcgAhZGF0YXN0cnVjdHVyZXMuTGlua2VkQXJyYXlIYXNoU2V0AAAAAAAAAAEDAAJGAApsb2FkRmFjdG9yTAAJaGFzaFRhYmxldAAuTGRhdGFzdHJ1Y3R1cmVzL2FycmF5aGFzaHRhYmxlL0FycmF5SGFzaFRhYmxlO3hwdwgAAAAAQAAAAHg="}
		AnnotationCmd:102 JSON{"key":{"name":"fps.free-pointer-is-scalarized","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true}
		NopCmd
		AssumeExpCmd LNot(Lt(tacCalldatasize!!5:3 0x4 ) )
		NopCmd
		AssumeExpCmd Gt(0x82c63066 tacSighash!!39:44 )
		NopCmd
		AssumeExpCmd Eq(0x3842f776 tacSighash!!39:44 )
		AssignExpCmd:119 R332:90 Sub(tacCalldatasize!!5:3 0x4 )
		AssignExpCmd:102 B333:80 Slt(R332:90 0x60 )
		NopCmd
		AssumeExpCmd LNot(B333:80 )
		NopCmd
		AssumeExpCmd Slt(0x23 tacCalldatasize!!5:91 )
		AssignExpCmd:120 R337:93 0x80
		AssumeCmd:121 true
		AssignExpCmd:102 B338:74 Gt(0x44 tacCalldatasize!!5:91 )
		NopCmd
		AssumeExpCmd LNot(B338:74 )
		AnnotationCmd:102 JSON{"key":{"name":"dsa.assign.start","type":"java.lang.String","erasureStrategy":"Erased"},"value":"4280_1005_0_0_0_0 -> 4282_1004_0_0_0_0"}
		LabelCmd:102 "Parallel assignment for R3573:bv256, R3574:bv256 := R2326:bv256, R3653:bv256"
		AnnotationCmd:102 JSON{"key":{"name":"dsa.assign.end","type":"java.lang.String","erasureStrategy":"Erased"},"value":"4280_1005_0_0_0_0 -> 4282_1004_0_0_0_0"}
		AnnotationCmd:102 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.LoopSnippet.StartLoopSnippet","loopIndex":4,"loopSource":"unknown loop source code"}}
		AnnotationCmd:102 JSON{"key":{"name":"start_loop.cmd","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		AnnotationCmd:102 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.LoopSnippet.StartIter","iteration":1}}
		AssignExpCmd:122 R340:96 Select(tacCalldatabuf!!325@9:118 0x4 )
		AssignExpCmd:123 tacMCANON3!!341:12 Store(tacMCANON3!!14:12 0x80 R340:96 )
		AnnotationCmd:102 JSON{"key":{"name":"dsa.assign.start","type":"java.lang.String","erasureStrategy":"Erased"},"value":"4301_1002_0_0_0_0 -> 4282_1004_0_0_0_0"}
		LabelCmd:102 "Parallel assignment for R3573:bv256, R3574:bv256 := R3566:bv256, R3570:bv256"
		AnnotationCmd:102 JSON{"key":{"name":"dsa.assign.end","type":"java.lang.String","erasureStrategy":"Erased"},"value":"4301_1002_0_0_0_0 -> 4282_1004_0_0_0_0"}
		AnnotationCmd:102 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.LoopSnippet.EndIter","iteration":1}}
		AnnotationCmd:102 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.LoopSnippet.StartIter","iteration":2}}
		AssignExpCmd:122 R342:96 Select(tacCalldatabuf!!325@9:118 0x24 )
		AssignExpCmd:123 tacMCANON3!!343:12 Store(tacMCANON3!!341:12 0xa0 R342:96 )
		AnnotationCmd:102 JSON{"key":{"name":"dsa.assign.start","type":"java.lang.String","erasureStrategy":"Erased"},"value":"4301_1002_0_0_0_0 -> 4282_1004_0_0_0_0"}
		LabelCmd:102 "Parallel assignment for R3573:bv256, R3574:bv256 := R3566:bv256, R3570:bv256"
		AnnotationCmd:102 JSON{"key":{"name":"dsa.assign.end","type":"java.lang.String","erasureStrategy":"Erased"},"value":"4301_1002_0_0_0_0 -> 4282_1004_0_0_0_0"}
		AnnotationCmd:102 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.LoopSnippet.EndIter","iteration":2}}
		AnnotationCmd:102 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.LoopSnippet.EndLoopSnippet","loopId":4}}
		AnnotationCmd:102 JSON{"key":{"name":"end_loop.cmd","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		AnnotationCmd:102 JSON{"key":{"name":"pta.end-allocation","type":"analysis.alloc.AllocationAnalysis$AbstractLocation","erasureStrategy":"Erased"},"value":{"prevFPWriteIdx":0,"nextFPWriteCmd":{"block":{"#class":"tac.BlockIdentifier","origStartPc":4102,"stkTop":1000,"decompCopy":0,"calleeIdx":0,"topOfStackValue":0,"freshCopy":0},"pos":1},"sort":{"#class":"analysis.alloc.AllocationAnalysis.Alloc.ConstBlock","sz":"40"}}}
		AssignExpCmd:122 R344:62 Select(tacCalldatabuf!!325@9:118 0x44 )
		AnnotationCmd:102 JSON{"key":{"name":"internal.func.start","type":"analysis.ip.InternalFuncStartAnnotation","erasureStrategy":"CallTrace"},"value":{"id":9,"startPc":558,"args":[{"s":{"namePrefix":"R337","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1001}]},"offset":1,"sort":"SCALAR"},{"s":{"namePrefix":"R344","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1012}]},"offset":2,"sort":"SCALAR"}],"methodSignature":{"#class":"spec.cvlast.QualifiedMethodSignature.QualifiedMethodSig","qualifiedMethodName":{"#class":"spec.cvlast.QualifiedFunction","host":{"name":"curve"},"methodId":"get_D"},"params":[{"#class":"spec.cvlast.VMParam.Named","name":"xp","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$StaticArrayDescriptor","location":"memory","elementType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256},"numElements":"2"}},{"#class":"spec.cvlast.VMParam.Named","name":"amp","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256}}],"res":[{"#class":"spec.cvlast.VMParam.Unnamed","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256}}]},"stackOffsetToArgPos":{"1":0,"2":1},"callSiteSrc":{"source":7,"begin":2956,"len":1542,"jumpType":"ENTER","address":"ce4604a0000000000000000000000028","sourceContext":{"indexToFilepath":{"0":"contracts/Context.sol","1":"contracts/CurveToken.sol","2":"contracts/CurveTokenExample.sol","3":"contracts/ERC20.sol","4":"contracts/IERC20.sol","5":"contracts/IERC20Metadata.sol","6":"contracts/ReentrancyGuard.sol","7":"contracts/curve.sol"},"sourceDir":".post_autofinders.2"}}}}
		AssignExpCmd:124 R345:80 Select(tacMCANON3!!343:12 0xa0 )
		AssignExpCmd:125 R346:90 Select(tacMCANON3!!343:12 0x80 )
		NopCmd
		AssumeExpCmd Apply(add_noofl:bif R346:90 R345:80)
		AssignExpCmd I349:51 Apply(safe_math_promotion:bif R346:90)
		AssignExpCmd I350:51 Apply(safe_math_promotion:bif R345:80)
		NopCmd
		AssignExpCmd R352:69 Apply(safe_math_narrow:bif IntAdd(I349:51 I350:51))
		AnnotationCmd:102 JSON{"key":{"name":"internal.func.end","type":"analysis.ip.InternalFuncExitAnnotation","erasureStrategy":"Canonical"},"value":{"id":9,"rets":[{"s":{"namePrefix":"R352","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1023}]},"offset":0}],"functionLayout":{"0":{"#class":"analysis.ip.InternalFuncValueLocation.Scalar"}}}}
		AnnotationCmd:102 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.EVMFunctionReturnWrite","returnbufOffset":"0","returnValueSym":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R352","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1023}]},"callIndex":9}}
		AnnotationCmd:102 JSON{"key":{"name":"tac.return.path","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		LabelCmd:102 "End procedure curve-get_D(uint256[2],uint256)"
		AssignExpCmd:102 tacReturndata!!354:75 Store(tacReturndata!!403:75 0x0 R352:69 )
		AssignExpCmd:102 tacMCANON2!!355:10 Store(tacMCANON2!!399:10 0x120 R352:69 )
		AnnotationCmd:102 JSON{"key":{"name":"call.trace.pop","type":"analysis.icfg.Inliner$CallStack$PopRecord","erasureStrategy":"Canonical"},"value":"rO0ABXNyAClhbmFseXNpcy5pY2ZnLklubGluZXIkQ2FsbFN0YWNrJFBvcFJlY29yZPAPfwSLdCWJAgABSQAIY2FsbGVlSWR4cAAAAAk="}
		JumpCmd:102 2_0_0_7_0_0
	}
	Block 0_0_0_10_0_0 Succ [3_0_0_7_0_0] {
		AnnotationCmd:102 JSON{"key":{"name":"call.trace.push","type":"analysis.icfg.Inliner$CallStack$PushRecord","erasureStrategy":"Canonical"},"value":"rO0ABXNyACphbmFseXNpcy5pY2ZnLklubGluZXIkQ2FsbFN0YWNrJFB1c2hSZWNvcmSX8+DCTLCH+AIAA0kACGNhbGxlZUlkTAAGY2FsbGVldAATTHZjL2RhdGEvTWV0aG9kUmVmO0wAB3N1bW1hcnl0ABVMdmMvZGF0YS9DYWxsU3VtbWFyeTt4cAAAAApzcgARdmMuZGF0YS5NZXRob2RSZWbJlJTzzU9pGAIAA0wABGF0dHJ0ABdMc2NlbmUvTWV0aG9kQXR0cmlidXRlO0wACmNvbnRyYWN0SWR0ABZMamF2YS9tYXRoL0JpZ0ludGVnZXI7TAAHc2lnSGFzaHQAEExldm0vU2lnaGFzaEludDt4cHNyABxzY2VuZS5NZXRob2RBdHRyaWJ1dGUkQ29tbW9uNHjdebdr9XMCAAB4cgAVc2NlbmUuTWV0aG9kQXR0cmlidXRlcYg2pYWutuUCAAB4cHNyABRqYXZhLm1hdGguQmlnSW50ZWdlcoz8nx+pO/sdAwAGSQAIYml0Q291bnRJAAliaXRMZW5ndGhJABNmaXJzdE5vbnplcm9CeXRlTnVtSQAMbG93ZXN0U2V0Qml0SQAGc2lnbnVtWwAJbWFnbml0dWRldAACW0J4cgAQamF2YS5sYW5nLk51bWJlcoaslR0LlOCLAgAAeHD///////////////7////+AAAAAXVyAAJbQqzzF/gGCFTgAgAAeHAAAAAQzkYEoAAAAAAAAAAAAAAACHhzcgAOZXZtLlNpZ2hhc2hJbnRUdcqNMXEgeAIAAUwAAW5xAH4ABnhwc3EAfgAM///////////////+/////gAAAAF1cQB+ABAAAAAEGBYN3XhzcgATdmMuZGF0YS5DYWxsU3VtbWFyeZQcmw5vl+FdAgAQSQAJc3VtbWFyeUlkTAAOY2FsbENvbnZlbnRpb250ACZMaW5zdHJ1bWVudGF0aW9uL2NhbGxzL0NhbGxDb252ZW50aW9uO0wACmNhbGxUYXJnZXR0ABpMYW5hbHlzaXMvaWNmZy9DYWxsVGFyZ2V0O0wACGNhbGxUeXBldAAVTHZjL2RhdGEvVEFDQ2FsbFR5cGU7TAAPY2Fubm90QmVJbmxpbmVkdAAtTGFuYWx5c2lzL2ljZmcvSW5saW5lciRJbGxlZ2FsSW5saW5pbmdSZWFzb247TAAGZ2FzVmFydAATTHZjL2RhdGEvVEFDU3ltYm9sO0wABmluQmFzZXEAfgAbTAAIaW5PZmZzZXRxAH4AG0wABmluU2l6ZXEAfgAbTAAMb3JpZ0NhbGxjb3JldAAgTHZjL2RhdGEvVEFDQ21kJFNpbXBsZSRDYWxsQ29yZTtMAAdvdXRCYXNlcQB+ABtMAAlvdXRPZmZzZXRxAH4AG0wAB291dFNpemVxAH4AG0wADXNpZ1Jlc29sdXRpb250AA9MamF2YS91dGlsL1NldDtMAAV0b1ZhcnEAfgAbTAAIdmFsdWVWYXJxAH4AG3hwAAAABnNyACRpbnN0cnVtZW50YXRpb24uY2FsbHMuQ2FsbENvbnZlbnRpb25HtO1ulL788QIAA0kACGNhbGxlcklkTAAFaW5wdXR0ABlMYW5hbHlzaXMvaWNmZy9DYWxsSW5wdXQ7TAAGcmF3T3V0dAAiTGluc3RydW1lbnRhdGlvbi9jYWxscy9DYWxsT3V0cHV0O3hwAAAAAHNyABdhbmFseXNpcy5pY2ZnLkNhbGxJbnB1dJjJD1MhNUxQAgAHTAAHYmFzZVZhcnQAGUx2Yy9kYXRhL1RBQ0V4cHIkU3ltJFZhcjtMABBlbmNvZGVkQXJndW1lbnRzdAAjTGFuYWx5c2lzL2ljZmcvQUJJQXJndW1lbnRFbmNvZGluZztMABNpbnB1dFNpemVMb3dlckJvdW5kcQB+AAZMAAZvZmZzZXR0ABVMdmMvZGF0YS9UQUNFeHByJFN5bTtMABRyYW5nZVRvRGVjb21wb3NlZEFyZ3QAD0xqYXZhL3V0aWwvTWFwO0wAEHNpbXBsaWZpZWRPZmZzZXR0ABtMdmMvZGF0YS9UQUNFeHByJFN5bSRDb25zdDtMAARzaXplcQB+ACZ4cHNyABd2Yy5kYXRhLlRBQ0V4cHIkU3ltJFZhcskrg43eGgPnAgACTAABc3QAF0x2Yy9kYXRhL1RBQ1N5bWJvbCRWYXI7TAADdGFndAAJTHRhYy9UYWc7eHIAE3ZjLmRhdGEuVEFDRXhwciRTeW2iVj0S4YSNUAIAAHhyAA92Yy5kYXRhLlRBQ0V4cHJYhGlUu/v+yAIAAHhwc3IANnZjLmRhdGEuVEFDU3ltYm9sJFZhciRXaXRoRGVmYXVsdENhbGxJbmRleCRXaXRoQnl0ZU1hcJ7+oHF4CHAAAgACTAAEbWV0YXQALUxrb3RsaW54L2NvbGxlY3Rpb25zL2ltbXV0YWJsZS9QZXJzaXN0ZW50TWFwO0wACm5hbWVQcmVmaXh0ABJMamF2YS9sYW5nL1N0cmluZzt4cgAVdmMuZGF0YS5UQUNTeW1ib2wkVmFyCYrCGVl9SXYCAAB4cgARdmMuZGF0YS5UQUNTeW1ib2zd3Run/CoWswIAAHhwc3IAJmRhdGFzdHJ1Y3R1cmVzLnRyZWFwLkhhc2hUcmVhcE1hcCROb2Rlf2t9acJIPnQCAANMAANrZXl0ABJMamF2YS9sYW5nL09iamVjdDtMAARuZXh0dAA1TGRhdGFzdHJ1Y3R1cmVzL3RyZWFwL0hhc2hUcmVhcE1hcCRNb3JlS2V5VmFsdWVQYWlycztMAAV2YWx1ZXEAfgA3eHIAIWRhdGFzdHJ1Y3R1cmVzLnRyZWFwLkhhc2hUcmVhcE1hcPMJ/2vt3boKAgAAeHIAHWRhdGFzdHJ1Y3R1cmVzLnRyZWFwLlRyZWFwTWFw46LAyn3v5moCAAB4cgAaZGF0YXN0cnVjdHVyZXMudHJlYXAuVHJlYXA88f21zZwbdQIAAkwABGxlZnR0ABxMZGF0YXN0cnVjdHVyZXMvdHJlYXAvVHJlYXA7TAAFcmlnaHRxAH4APHhwcHNxAH4ANnBzcQB+ADZwcHNyAAt0YWMuTWV0YUtleVF/W3MiCfIZAgADTAAPZXJhc3VyZVN0cmF0ZWd5dAAdTHRhYy9NZXRhS2V5JEVyYXN1cmVTdHJhdGVneTtMAARuYW1lcQB+ADJMAAN0eXB0ABFMamF2YS9sYW5nL0NsYXNzO3hwfnIAG3RhYy5NZXRhS2V5JEVyYXN1cmVTdHJhdGVneQAAAAAAAAAAEgAAeHIADmphdmEubGFuZy5FbnVtAAAAAAAAAAASAAB4cHQACUNhbm9uaWNhbHQAF3RhYy5tZW1vcnkucGFydGl0aW9uLWlkdnIAEWphdmEubGFuZy5JbnRlZ2VyEuKgpPeBhzgCAAFJAAV2YWx1ZXhxAH4ADnBzcQB+AEkAAAAJc3EAfgBAcQB+AEZ0ABJUYWMuc3ltYm9sLmtleXdvcmR2cgAQamF2YS5sYW5nLlN0cmluZ6DwpDh6O7NCAgAAeHBwdAAEdGFjTXNxAH4AQHEAfgBGdAANdGFjLmlzLm1lbW9yeXZyACJ0YWMuTWV0YU1hcCRDb21wYW5pb24kTm90aGluZ1ZhbHVl8nsHH85ykpUCAAB4cHBzcQB+AFN0AA90YWNNQ0FOT04yISE0NTBzcgAPdGFjLlRhZyRCeXRlTWFwNb/Ry6GDRgkCAAB4cgALdGFjLlRhZyRNYXABJytzDV3P/QIAAHhyAAd0YWMuVGFnLk9V3gn2xngCAAB4cHBzcQB+AAz///////////////7////+AAAAAXVxAH4AEAAAAAEEeHNxAH4AKnNyADV2Yy5kYXRhLlRBQ1N5bWJvbCRWYXIkV2l0aERlZmF1bHRDYWxsSW5kZXgkV2l0aEJpdDI1NnqsyEgq0drPAgACTAAEbWV0YXEAfgAxTAAKbmFtZVByZWZpeHEAfgAyeHEAfgAzc3EAfgA2c3EAfgA2cHBxAH4ATHB0AAFMcHNxAH4AQHEAfgBGdAAQdGFjLnN0YWNrLmhlaWdodHEAfgBKcHNxAH4ASQAAA/d0AARSNDUxc3IADnRhYy5UYWckQml0MjU2IyLQT+LlKkgCAAB4cQB+AFlzcgARamF2YS51dGlsLkhhc2hNYXAFB9rBwxZg0QMAAkYACmxvYWRGYWN0b3JJAAl0aHJlc2hvbGR4cD9AAAAAAAABdwgAAAACAAAAAXNyAB5hbmFseXNpcy5pY2ZnLlNjcmF0Y2hCeXRlUmFuZ2XBTLaPpUzj2gIAAkwABGZyb21xAH4ABkwAAnRvcQB+AAZ4cHNxAH4ADP///////////////v////4AAAAAdXEAfgAQAAAAAHhzcQB+AAz///////////////7////+AAAAAXVxAH4AEAAAAAEDeHNyAC1hbmFseXNpcy5pY2ZnLkRlY29tcG9zZWRDYWxsSW5wdXRBcmckQ29uc3RhbnSFavLdQafqPQIAA0wAAWN0ABlMdmMvZGF0YS9UQUNTeW1ib2wkQ29uc3Q7TAARY29udHJhY3RSZWZlcmVuY2V0AC9MYW5hbHlzaXMvaWNmZy9DYWxsR3JhcGhCdWlsZGVyJENhbGxlZENvbnRyYWN0O0wADHNjcmF0Y2hSYW5nZXQAIExhbmFseXNpcy9pY2ZnL1NjcmF0Y2hCeXRlUmFuZ2U7eHIAJGFuYWx5c2lzLmljZmcuRGVjb21wb3NlZENhbGxJbnB1dEFy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ADZwcHEAfgBMcHEAfgBic3EAfgBAcQB+AEZ0ABZ0YWMuc2NhbGFyaXphdGlvbi5zb3J0dnIAGXZjLmRhdGEuU2NhbGFyaXphdGlvblNvcnQwznCd5GgNJgIAAHhwcHNyACB2Yy5kYXRhLlNjYWxhcml6YXRpb25Tb3J0JFBhY2tlZC5FrRKTiOT3AgACSQAFc3RhcnRMAAtwYWNrZWRTdGFydHQAG0x2Yy9kYXRhL1NjYWxhcml6YXRpb25Tb3J0O3hxAH4A7gAAAABzcgAfdmMuZGF0YS5TY2FsYXJpemF0aW9uU29ydCRTcGxpdFT/Wafxx7IFAgABTAADaWR4cQB+AAZ4cQB+AO5zcQB+AAz///////////////7////+AAAAAXVxAH4AEAAAAAEMeHNxAH4ANnBzcQB+ADZwc3EAfgA2cHBzcQB+AEBxAH4ARnQAHHRhYy5zdG9yYWdlLm5vbi1pbmRleGVkLXBhdGh2cgA1YW5hbHlzaXMuc3RvcmFnZS5TdG9yYWdlQW5hbHlzaXNSZXN1bHQkTm9uSW5kZXhlZFBhdGgIwaBLofo/RQIAAHhwcHNyADphbmFseXNpcy5zdG9yYWdlLlN0b3JhZ2VBbmFseXNpc1Jlc3VsdCROb25JbmRleGVkUGF0aCRSb290vzf12KXqCv8CAAFMAARzbG90cQB+AAZ4cQB+APxxAH4A9XNxAH4AQHEAfgBGdAANdGFjLnNsb3QudHlwZXZyADpzcGVjLmN2bGFzdC50eXBlZGVzY3JpcHRvcnMuRVZNVHlwZURlc2NyaXB0b3IkRVZNVmFsdWVUeXBlxomvArrquCUCAAB4cgAtc3BlYy5jdmxhc3QudHlwZWRlc2NyaXB0b3JzLkVWTVR5cGVEZXNjcmlwdG9yyFGp8TzCah0CAAB4cHBzcgA1c3BlYy5jdmxhc3QudHlwZWRlc2NyaXB0b3JzLkVWTVR5cGVEZXNjcmlwdG9yJGFkZHJlc3N6+GX0b5egKQIAAHhyAERzcGVjLmN2bGFzdC50eXBlZGVzY3JpcHRvcnMuRVZNVHlwZURlc2NyaXB0b3IkRVZNSXNvbW9ycGhpY1ZhbHVlVHlwZfd1mJFuEKEPAgAAeHEAfgECc3EAfgBAfnEAfgBEdAAGRXJhc2VkdAAYdGFjLnN0b3JhZ2UucHJldHR5LnBhdGhzdnIAHWFuYWx5c2lzLnN0b3JhZ2UuRGlzcGxheVBhdGhz90RLt8P1URYCAAFMAAVwYXRoc3EAfgAdeHBwc3EAfgEMc3IAF2phdmEudXRpbC5MaW5rZWRIYXNoU2V02GzXWpXdKh4CAAB4cgARamF2YS51dGlsLkhhc2hTZXS6RIWVlri3NAMAAHhwdwwAAAAQP0AAAAAAAAFzcgAhYW5hbHlzaXMuc3RvcmFnZS5EaXNwbGF5UGF0aCRSb29003OgvZnQPHICAAJMAARiYXNldAAeTGFuYWx5c2lzL3N0b3JhZ2UvRGlzcGxheVBhdGg7TAAEbmFtZXEAfgAyeHIAHGFuYWx5c2lzLnN0b3JhZ2UuRGlzcGxheVBhdGhPQGPqVtIgBQIAAHhwcHQACGxwX3Rva2VueHNxAH4AQHEAfgBGdAAVdGFjLnN0b3JhZ2UuYml0LXdpZHRocQB+AEpwc3EAfgBJAAAAoHBzcQB+AEBxAH4ARnQAC3RhYy5zdG9yYWdldnEAfgAMcHEAfgDGcHEAfgBjcHNxAH4ASQAAA/t0AAtDQU5PTjE5ISEyMXNxAH4Ad3EAfgBocQB+AG1zcQB+ADBzcQB+ADZwc3EAfgA2cHNxAH4ANnBwcQB+AENwcQB+AEtxAH4ATHBxAH4AUHEAfgBRcHEAfgBVcQB+AFZzcQB+AF5zcQB+ADZzcQB+ADZwcHEAfgBMcHEAfgBicHEAfgBjcHEAfgCNcQB+AGZxAH4AkHNyACJqYXZhLnV0aWwuQ29sbGVjdGlvbnMkU2luZ2xldG9uU2V0LFJBmCnAsb8CAAFMAAdlbGVtZW50cQB+ADd4cHEAfgAUc3EAfgBec3EAfgA2c3EAfgA2c3EAfgA2c3EAfgA2cHNxAH4ANnBwcQB+AExwcQB+AGJxAH4A7HBxAH4A8nNxAH4ANnBzcQB+ADZwc3EAfgA2cHBxAH4A+nBxAH4A/3EAfgEAcHEAfgEHcQB+AQhwc3EAfgEMc3EAfgEPdwwAAAAQP0AAAAAAAAFxAH4BFXhxAH4BF3BxAH4BGXBxAH4BGnBxAH4AxnBxAH4AY3BxAH4BHXEAfgEec3EAfgB3cQB+AGhxAH4AbQ=="}
		AnnotationCmd:102 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageGlobalChangeSnippet.StorageBackupPoint","calleeTxId":10}}
		NopCmd
		AssumeExpCmd LAnd(Eq(tacCalldatasize!!6:3 0x4 ) Eq(tacCalldatasize!!6:3 0x4 ) )
		NopCmd
		AssumeExpCmd Eq(tacCalldatabufCANON0@10:2 0x18160ddd00000000000000000000000000000000000000000000000000000000 )
		LabelCmd:102 "Start procedure CurveTokenExample-totalSupply()"
		AnnotationCmd:102 JSON{"key":{"name":"fps.free-pointer-is-scalarized","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true}
		AssignExpCmd:102 R359:51 Select(tacExtcodesize!!7:4 Apply(to_skey:bif R28:100) )
		NopCmd
		AssumeExpCmd Gt(R359:51 0x0 )
		AnnotationCmd:102 JSON{"key":{"name":"internal.func.finder.info","type":"analysis.ip.InternalFunctionFinderReport","erasureStrategy":"Erased"},"value":"rO0ABXNyAChhbmFseXNpcy5pcC5JbnRlcm5hbEZ1bmN0aW9uRmluZGVyUmVwb3J0ian+bYn1VdACAAFMABN1bnJlc29sdmVkRnVuY3Rpb25zdAAPTGphdmEvdXRpbC9TZXQ7eHBzcgAhZGF0YXN0cnVjdHVyZXMuTGlua2VkQXJyYXlIYXNoU2V0AAAAAAAAAAEDAAJGAApsb2FkRmFjdG9yTAAJaGFzaFRhYmxldAAuTGRhdGFzdHJ1Y3R1cmVzL2FycmF5aGFzaHRhYmxlL0FycmF5SGFzaFRhYmxlO3hwdwgAAAAAQAAAAHg="}
		AnnotationCmd:102 JSON{"key":{"name":"fps.free-pointer-is-scalarized","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true}
		NopCmd
		AssumeExpCmd LNot(Lt(tacCalldatasize!!6:3 0x4 ) )
		NopCmd
		AssumeExpCmd Gt(0x40c10f19 tacSighash!!40:44 )
		NopCmd
		AssumeExpCmd LNot(Eq(0x6fdde03 tacSighash!!40:44 ) )
		NopCmd
		AssumeExpCmd LNot(Eq(0x95ea7b3 tacSighash!!40:44 ) )
		NopCmd
		AssumeExpCmd Eq(0x18160ddd tacSighash!!40:44 )
		AnnotationCmd:102 JSON{"key":{"name":"internal.func.start","type":"analysis.ip.InternalFuncStartAnnotation","erasureStrategy":"CallTrace"},"value":{"id":10,"startPc":1205,"args":[],"methodSignature":{"#class":"spec.cvlast.QualifiedMethodSignature.QualifiedMethodSig","qualifiedMethodName":{"#class":"spec.cvlast.QualifiedFunction","host":{"name":"CurveTokenExample"},"methodId":"totalSupply"},"params":[],"res":[{"#class":"spec.cvlast.VMParam.Unnamed","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256}}]},"stackOffsetToArgPos":{},"callSiteSrc":{"source":3,"begin":3954,"len":364,"jumpType":"ENTER","address":"ce4604a0000000000000000000000008","sourceContext":{"indexToFilepath":{"0":"contracts/Context.sol","1":"contracts/CurveToken.sol","2":"contracts/CurveTokenExample.sol","3":"contracts/ERC20.sol","4":"contracts/IERC20.sol","5":"contracts/IERC20Metadata.sol"},"sourceDir":".post_autofinders.0"}}}}
		AnnotationCmd:102 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet","value":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"CANON87!!25","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.scalarization.sort","type":"vc.data.ScalarizationSort","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.ScalarizationSort.Split","idx":"2"}},{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.storage.bit-width","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":256},{"key":{"name":"tac.storage.pretty.paths","type":"analysis.storage.DisplayPaths","erasureStrategy":"Erased"},"value":{"paths":[{"#class":"analysis.storage.DisplayPath.Root","name":"_totalSupply"}]}},{"key":{"name":"tac.slot.type","type":"spec.cvlast.typedescriptors.EVMTypeDescriptor$EVMValueType","erasureStrategy":"Canonical"},"value":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256}},{"key":{"name":"tac.storage.non-indexed-path","type":"analysis.storage.StorageAnalysisResult$NonIndexedPath","erasureStrategy":"Canonical"},"value":{"#class":"analysis.storage.StorageAnalysisResult.NonIndexedPath.Root","slot":"2"}},{"key":{"name":"tac.storage","type":"java.math.BigInteger","erasureStrategy":"Canonical"},"value":"ce4604a0000000000000000000000008"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1021}]},"displayPath":{"#class":"analysis.storage.DisplayPath.Root","name":"_totalSupply"},"storageType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256},"contractInstance":"ce4604a0000000000000000000000008","linkableStorageReadId":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet.Id","id":11}}}
		AnnotationCmd:102 JSON{"key":{"name":"internal.func.end","type":"analysis.ip.InternalFuncExitAnnotation","erasureStrategy":"Canonical"},"value":{"id":10,"rets":[{"s":{"namePrefix":"CANON87!!25","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.scalarization.sort","type":"vc.data.ScalarizationSort","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.ScalarizationSort.Split","idx":"2"}},{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.storage.bit-width","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":256},{"key":{"name":"tac.storage.pretty.paths","type":"analysis.storage.DisplayPaths","erasureStrategy":"Erased"},"value":{"paths":[{"#class":"analysis.storage.DisplayPath.Root","name":"_totalSupply"}]}},{"key":{"name":"tac.slot.type","type":"spec.cvlast.typedescriptors.EVMTypeDescriptor$EVMValueType","erasureStrategy":"Canonical"},"value":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256}},{"key":{"name":"tac.storage.non-indexed-path","type":"analysis.storage.StorageAnalysisResult$NonIndexedPath","erasureStrategy":"Canonical"},"value":{"#class":"analysis.storage.StorageAnalysisResult.NonIndexedPath.Root","slot":"2"}},{"key":{"name":"tac.storage","type":"java.math.BigInteger","erasureStrategy":"Canonical"},"value":"ce4604a0000000000000000000000008"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1023}]},"offset":0}],"functionLayout":{"0":{"#class":"analysis.ip.InternalFuncValueLocation.Scalar"}}}}
		AnnotationCmd:102 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.EVMFunctionReturnWrite","returnbufOffset":"0","returnValueSym":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"CANON87!!25","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.scalarization.sort","type":"vc.data.ScalarizationSort","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.ScalarizationSort.Split","idx":"2"}},{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.storage.bit-width","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":256},{"key":{"name":"tac.storage.pretty.paths","type":"analysis.storage.DisplayPaths","erasureStrategy":"Erased"},"value":{"paths":[{"#class":"analysis.storage.DisplayPath.Root","name":"_totalSupply"}]}},{"key":{"name":"tac.slot.type","type":"spec.cvlast.typedescriptors.EVMTypeDescriptor$EVMValueType","erasureStrategy":"Canonical"},"value":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256}},{"key":{"name":"tac.storage.non-indexed-path","type":"analysis.storage.StorageAnalysisResult$NonIndexedPath","erasureStrategy":"Canonical"},"value":{"#class":"analysis.storage.StorageAnalysisResult.NonIndexedPath.Root","slot":"2"}},{"key":{"name":"tac.storage","type":"java.math.BigInteger","erasureStrategy":"Canonical"},"value":"ce4604a0000000000000000000000008"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1023}]},"callIndex":10}}
		AnnotationCmd:102 JSON{"key":{"name":"tac.return.path","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		LabelCmd:102 "End procedure CurveTokenExample-totalSupply()"
		AssignExpCmd:102 tacReturndata!!368:75 Store(tacReturndata!!453:75 0x0 CANON87!!25:101 )
		AssignExpCmd:102 tacMCANON2!!369:10 Store(tacMCANON2!!450:10 0x140 CANON87!!25:101 )
		AnnotationCmd:102 JSON{"key":{"name":"call.trace.pop","type":"analysis.icfg.Inliner$CallStack$PopRecord","erasureStrategy":"Canonical"},"value":"rO0ABXNyAClhbmFseXNpcy5pY2ZnLklubGluZXIkQ2FsbFN0YWNrJFBvcFJlY29yZPAPfwSLdCWJAgABSQAIY2FsbGVlSWR4cAAAAAo="}
		JumpCmd:102 3_0_0_7_0_0
	}
	Block 1_0_0_1_0_0 Succ [0_0_0_3_0_0] {
		AssumeNotCmd:71 false
		AnnotationCmd:53 JSON{"key":{"name":"pta.fake-return.start","type":"analysis.CmdPointer","erasureStrategy":"Erased"},"value":{"block":{"#class":"tac.BlockIdentifier","origStartPc":1608,"stkTop":1009,"decompCopy":0,"calleeIdx":0,"topOfStackValue":2,"freshCopy":0},"pos":1}}
		AnnotationCmd:53 JSON{"key":{"name":"pta.fake-return.end","type":"analysis.CmdPointer","erasureStrategy":"Erased"},"value":{"block":{"#class":"tac.BlockIdentifier","origStartPc":1608,"stkTop":1009,"decompCopy":0,"calleeIdx":0,"topOfStackValue":2,"freshCopy":0},"pos":6}}
		AssumeNotCmd:126 false
		AssignExpCmd:127 R370:128 Select(tacMCANON2!!178:9 0x100 )
		NopCmd
		AssumeExpCmd LNot(Lt(R370:128 R145:69 ) )
		AssignExpCmd:129 R372:66 Sub(R370:128 R145:69 )
		AssignExpCmd:67 tacMCANON1!!373:7 Store(tacMCANON1!!144:7 0xe0 R372:66 )
		AnnotationCmd:53 JSON{"key":{"name":"pta.end-allocation","type":"analysis.alloc.AllocationAnalysis$AbstractLocation","erasureStrategy":"Erased"},"value":{"prevFPWriteIdx":1,"nextFPWriteCmd":{"block":{"#class":"tac.BlockIdentifier","origStartPc":16,"stkTop":1024,"decompCopy":0,"calleeIdx":0,"topOfStackValue":2,"freshCopy":0},"pos":44},"sort":{"#class":"analysis.alloc.AllocationAnalysis.Alloc.ConstBlock","sz":"40"}}}
		AnnotationCmd:53 JSON{"key":{"name":"internal.func.start","type":"analysis.ip.InternalFuncStartAnnotation","erasureStrategy":"CallTrace"},"value":{"id":2,"startPc":3822,"args":[],"methodSignature":{"#class":"spec.cvlast.QualifiedMethodSignature.QualifiedMethodSig","qualifiedMethodName":{"#class":"spec.cvlast.QualifiedFunction","host":{"name":"curve"},"methodId":"_A"},"params":[],"res":[{"#class":"spec.cvlast.VMParam.Unnamed","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256}}]},"stackOffsetToArgPos":{},"callSiteSrc":{"source":7,"begin":6351,"len":4,"jumpType":"ENTER","address":"ce4604a0000000000000000000000028","sourceContext":{"indexToFilepath":{"0":"contracts/Context.sol","1":"contracts/CurveToken.sol","2":"contracts/CurveTokenExample.sol","3":"contracts/ERC20.sol","4":"contracts/IERC20.sol","5":"contracts/IERC20Metadata.sol","6":"contracts/ReentrancyGuard.sol","7":"contracts/curve.sol"},"sourceDir":".post_autofinders.2"}}}}
		AnnotationCmd:53 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet","value":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"CANON99!!27","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.scalarization.sort","type":"vc.data.ScalarizationSort","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.ScalarizationSort.Split","idx":"5"}},{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.storage.bit-width","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":256},{"key":{"name":"tac.storage.pretty.paths","type":"analysis.storage.DisplayPaths","erasureStrategy":"Erased"},"value":{"paths":[{"#class":"analysis.storage.DisplayPath.Root","name":"future_A"}]}},{"key":{"name":"tac.slot.type","type":"spec.cvlast.typedescriptors.EVMTypeDescriptor$EVMValueType","erasureStrategy":"Canonical"},"value":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256}},{"key":{"name":"tac.storage.non-indexed-path","type":"analysis.storage.StorageAnalysisResult$NonIndexedPath","erasureStrategy":"Canonical"},"value":{"#class":"analysis.storage.StorageAnalysisResult.NonIndexedPath.Root","slot":"5"}},{"key":{"name":"tac.storage","type":"java.math.BigInteger","erasureStrategy":"Canonical"},"value":"ce4604a0000000000000000000000028"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1015}]},"displayPath":{"#class":"analysis.storage.DisplayPath.Root","name":"future_A"},"storageType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256},"contractInstance":"ce4604a0000000000000000000000028","linkableStorageReadId":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet.Id","id":2}}}
		AnnotationCmd:53 JSON{"key":{"name":"internal.func.end","type":"analysis.ip.InternalFuncExitAnnotation","erasureStrategy":"Canonical"},"value":{"id":2,"rets":[{"s":{"namePrefix":"CANON99!!27","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.scalarization.sort","type":"vc.data.ScalarizationSort","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.ScalarizationSort.Split","idx":"5"}},{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.storage.bit-width","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":256},{"key":{"name":"tac.storage.pretty.paths","type":"analysis.storage.DisplayPaths","erasureStrategy":"Erased"},"value":{"paths":[{"#class":"analysis.storage.DisplayPath.Root","name":"future_A"}]}},{"key":{"name":"tac.slot.type","type":"spec.cvlast.typedescriptors.EVMTypeDescriptor$EVMValueType","erasureStrategy":"Canonical"},"value":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256}},{"key":{"name":"tac.storage.non-indexed-path","type":"analysis.storage.StorageAnalysisResult$NonIndexedPath","erasureStrategy":"Canonical"},"value":{"#class":"analysis.storage.StorageAnalysisResult.NonIndexedPath.Root","slot":"5"}},{"key":{"name":"tac.storage","type":"java.math.BigInteger","erasureStrategy":"Canonical"},"value":"ce4604a0000000000000000000000028"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1017}]},"offset":0}],"functionLayout":{"0":{"#class":"analysis.ip.InternalFuncValueLocation.Scalar"}}}}
		AssignExpCmd:130 tacMCANON2!!376:9 Store(tacMCANON2!!178:9 0x120 0x3842f77600000000000000000000000000000000000000000000000000000000 )
		AnnotationCmd:53 JSON{"key":{"name":"dsa.assign.start","type":"java.lang.String","erasureStrategy":"Erased"},"value":"4639_1009_0_0_0_0 -> 4643_1007_0_0_0_0"}
		LabelCmd:53 "Parallel assignment for R4175:bv256, R4219:bv256, B4220:bool, R4221:bv256 := R6292:bv256, R397:bv256, B4076:bool, R4077:bv256"
		AnnotationCmd:53 JSON{"key":{"name":"dsa.assign.end","type":"java.lang.String","erasureStrategy":"Erased"},"value":"4639_1009_0_0_0_0 -> 4643_1007_0_0_0_0"}
		AnnotationCmd:53 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.LoopSnippet.StartLoopSnippet","loopIndex":0,"loopSource":"unknown loop source code"}}
		AnnotationCmd:53 JSON{"key":{"name":"start_loop.cmd","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		AnnotationCmd:53 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.LoopSnippet.StartIter","iteration":1}}
		AssignExpCmd:131 R377:132 Select(tacMCANON1!!373:7 0xc0 )
		AssignExpCmd:133 tacMCANON2!!378:9 Store(tacMCANON2!!376:9 0x124 R377:132 )
		AnnotationCmd:53 JSON{"key":{"name":"dsa.assign.start","type":"java.lang.String","erasureStrategy":"Erased"},"value":"4674_1005_0_0_0_0 -> 4643_1007_0_0_0_0"}
		LabelCmd:53 "Parallel assignment for R4175:bv256, R4219:bv256, B4220:bool, R4221:bv256 := R3948:bv256, R3993:bv256, B4217:bool, R4214:bv256"
		AnnotationCmd:53 JSON{"key":{"name":"dsa.assign.end","type":"java.lang.String","erasureStrategy":"Erased"},"value":"4674_1005_0_0_0_0 -> 4643_1007_0_0_0_0"}
		AnnotationCmd:53 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.LoopSnippet.EndIter","iteration":1}}
		AnnotationCmd:53 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.LoopSnippet.StartIter","iteration":2}}
		AssignExpCmd:131 R379:132 Select(tacMCANON1!!373:7 0xe0 )
		AssignExpCmd:133 tacMCANON2!!380:9 Store(tacMCANON2!!378:9 0x144 R379:132 )
		AnnotationCmd:53 JSON{"key":{"name":"dsa.assign.start","type":"java.lang.String","erasureStrategy":"Erased"},"value":"4674_1005_0_0_0_0 -> 4643_1007_0_0_0_0"}
		LabelCmd:53 "Parallel assignment for R4175:bv256, R4219:bv256, B4220:bool, R4221:bv256 := R3948:bv256, R3993:bv256, B4217:bool, R4214:bv256"
		AnnotationCmd:53 JSON{"key":{"name":"dsa.assign.end","type":"java.lang.String","erasureStrategy":"Erased"},"value":"4674_1005_0_0_0_0 -> 4643_1007_0_0_0_0"}
		AnnotationCmd:53 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.LoopSnippet.EndIter","iteration":2}}
		AnnotationCmd:53 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.LoopSnippet.EndLoopSnippet","loopId":0}}
		AnnotationCmd:53 JSON{"key":{"name":"end_loop.cmd","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		AssignExpCmd:134 tacMCANON2!!382:9 Store(tacMCANON2!!380:9 0x164 CANON99!!27:135 )
		AssignExpCmd:130 R383:90 0x120
		NopCmd
		AssignHavocCmd:130 R385:62
		AssignHavocCmd:53 tacReturndata!!386:75
		JumpCmd:53 0_0_0_3_0_0
	}
	Block 1_0_0_7_0_0 Succ [0_0_0_9_0_0] {
		AssumeNotCmd:109 false
		AnnotationCmd:102 JSON{"key":{"name":"pta.fake-return.start","type":"analysis.CmdPointer","erasureStrategy":"Erased"},"value":{"block":{"#class":"tac.BlockIdentifier","origStartPc":1608,"stkTop":1009,"decompCopy":0,"calleeIdx":0,"topOfStackValue":2,"freshCopy":0},"pos":1}}
		AnnotationCmd:102 JSON{"key":{"name":"pta.fake-return.end","type":"analysis.CmdPointer","erasureStrategy":"Erased"},"value":{"block":{"#class":"tac.BlockIdentifier","origStartPc":1608,"stkTop":1009,"decompCopy":0,"calleeIdx":0,"topOfStackValue":2,"freshCopy":0},"pos":6}}
		AssumeNotCmd:136 false
		AssignExpCmd:137 R387:128 Select(tacMCANON2!!321:10 0x100 )
		NopCmd
		AssumeExpCmd LNot(Lt(R387:128 R288:69 ) )
		AssignExpCmd:138 R389:66 Sub(R387:128 R288:69 )
		AssignExpCmd:107 tacMCANON1!!390:8 Store(tacMCANON1!!287:8 0xe0 R389:66 )
		AnnotationCmd:102 JSON{"key":{"name":"pta.end-allocation","type":"analysis.alloc.AllocationAnalysis$AbstractLocation","erasureStrategy":"Erased"},"value":{"prevFPWriteIdx":1,"nextFPWriteCmd":{"block":{"#class":"tac.BlockIdentifier","origStartPc":16,"stkTop":1024,"decompCopy":0,"calleeIdx":0,"topOfStackValue":2,"freshCopy":0},"pos":44},"sort":{"#class":"analysis.alloc.AllocationAnalysis.Alloc.ConstBlock","sz":"40"}}}
		AnnotationCmd:102 JSON{"key":{"name":"internal.func.start","type":"analysis.ip.InternalFuncStartAnnotation","erasureStrategy":"CallTrace"},"value":{"id":8,"startPc":3822,"args":[],"methodSignature":{"#class":"spec.cvlast.QualifiedMethodSignature.QualifiedMethodSig","qualifiedMethodName":{"#class":"spec.cvlast.QualifiedFunction","host":{"name":"curve"},"methodId":"_A"},"params":[],"res":[{"#class":"spec.cvlast.VMParam.Unnamed","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256}}]},"stackOffsetToArgPos":{},"callSiteSrc":{"source":7,"begin":6351,"len":4,"jumpType":"ENTER","address":"ce4604a0000000000000000000000028","sourceContext":{"indexToFilepath":{"0":"contracts/Context.sol","1":"contracts/CurveToken.sol","2":"contracts/CurveTokenExample.sol","3":"contracts/ERC20.sol","4":"contracts/IERC20.sol","5":"contracts/IERC20Metadata.sol","6":"contracts/ReentrancyGuard.sol","7":"contracts/curve.sol"},"sourceDir":".post_autofinders.2"}}}}
		AnnotationCmd:102 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet","value":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"CANON99!!27","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.scalarization.sort","type":"vc.data.ScalarizationSort","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.ScalarizationSort.Split","idx":"5"}},{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.storage.bit-width","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":256},{"key":{"name":"tac.storage.pretty.paths","type":"analysis.storage.DisplayPaths","erasureStrategy":"Erased"},"value":{"paths":[{"#class":"analysis.storage.DisplayPath.Root","name":"future_A"}]}},{"key":{"name":"tac.slot.type","type":"spec.cvlast.typedescriptors.EVMTypeDescriptor$EVMValueType","erasureStrategy":"Canonical"},"value":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256}},{"key":{"name":"tac.storage.non-indexed-path","type":"analysis.storage.StorageAnalysisResult$NonIndexedPath","erasureStrategy":"Canonical"},"value":{"#class":"analysis.storage.StorageAnalysisResult.NonIndexedPath.Root","slot":"5"}},{"key":{"name":"tac.storage","type":"java.math.BigInteger","erasureStrategy":"Canonical"},"value":"ce4604a0000000000000000000000028"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1015}]},"displayPath":{"#class":"analysis.storage.DisplayPath.Root","name":"future_A"},"storageType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256},"contractInstance":"ce4604a0000000000000000000000028","linkableStorageReadId":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet.Id","id":9}}}
		AnnotationCmd:102 JSON{"key":{"name":"internal.func.end","type":"analysis.ip.InternalFuncExitAnnotation","erasureStrategy":"Canonical"},"value":{"id":8,"rets":[{"s":{"namePrefix":"CANON99!!27","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.scalarization.sort","type":"vc.data.ScalarizationSort","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.ScalarizationSort.Split","idx":"5"}},{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.storage.bit-width","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":256},{"key":{"name":"tac.storage.pretty.paths","type":"analysis.storage.DisplayPaths","erasureStrategy":"Erased"},"value":{"paths":[{"#class":"analysis.storage.DisplayPath.Root","name":"future_A"}]}},{"key":{"name":"tac.slot.type","type":"spec.cvlast.typedescriptors.EVMTypeDescriptor$EVMValueType","erasureStrategy":"Canonical"},"value":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256}},{"key":{"name":"tac.storage.non-indexed-path","type":"analysis.storage.StorageAnalysisResult$NonIndexedPath","erasureStrategy":"Canonical"},"value":{"#class":"analysis.storage.StorageAnalysisResult.NonIndexedPath.Root","slot":"5"}},{"key":{"name":"tac.storage","type":"java.math.BigInteger","erasureStrategy":"Canonical"},"value":"ce4604a0000000000000000000000028"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1017}]},"offset":0}],"functionLayout":{"0":{"#class":"analysis.ip.InternalFuncValueLocation.Scalar"}}}}
		AssignExpCmd:139 tacMCANON2!!393:10 Store(tacMCANON2!!321:10 0x120 0x3842f77600000000000000000000000000000000000000000000000000000000 )
		AnnotationCmd:102 JSON{"key":{"name":"dsa.assign.start","type":"java.lang.String","erasureStrategy":"Erased"},"value":"4639_1009_0_0_0_0 -> 4643_1007_0_0_0_0"}
		LabelCmd:102 "Parallel assignment for R4175:bv256, R4219:bv256, B4220:bool, R4221:bv256 := R6292:bv256, R397:bv256, B4076:bool, R4077:bv256"
		AnnotationCmd:102 JSON{"key":{"name":"dsa.assign.end","type":"java.lang.String","erasureStrategy":"Erased"},"value":"4639_1009_0_0_0_0 -> 4643_1007_0_0_0_0"}
		AnnotationCmd:102 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.LoopSnippet.StartLoopSnippet","loopIndex":3,"loopSource":"unknown loop source code"}}
		AnnotationCmd:102 JSON{"key":{"name":"start_loop.cmd","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		AnnotationCmd:102 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.LoopSnippet.StartIter","iteration":1}}
		AssignExpCmd:140 R394:132 Select(tacMCANON1!!390:8 0xc0 )
		AssignExpCmd:141 tacMCANON2!!395:10 Store(tacMCANON2!!393:10 0x124 R394:132 )
		AnnotationCmd:102 JSON{"key":{"name":"dsa.assign.start","type":"java.lang.String","erasureStrategy":"Erased"},"value":"4674_1005_0_0_0_0 -> 4643_1007_0_0_0_0"}
		LabelCmd:102 "Parallel assignment for R4175:bv256, R4219:bv256, B4220:bool, R4221:bv256 := R3948:bv256, R3993:bv256, B4217:bool, R4214:bv256"
		AnnotationCmd:102 JSON{"key":{"name":"dsa.assign.end","type":"java.lang.String","erasureStrategy":"Erased"},"value":"4674_1005_0_0_0_0 -> 4643_1007_0_0_0_0"}
		AnnotationCmd:102 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.LoopSnippet.EndIter","iteration":1}}
		AnnotationCmd:102 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.LoopSnippet.StartIter","iteration":2}}
		AssignExpCmd:140 R396:132 Select(tacMCANON1!!390:8 0xe0 )
		AssignExpCmd:141 tacMCANON2!!397:10 Store(tacMCANON2!!395:10 0x144 R396:132 )
		AnnotationCmd:102 JSON{"key":{"name":"dsa.assign.start","type":"java.lang.String","erasureStrategy":"Erased"},"value":"4674_1005_0_0_0_0 -> 4643_1007_0_0_0_0"}
		LabelCmd:102 "Parallel assignment for R4175:bv256, R4219:bv256, B4220:bool, R4221:bv256 := R3948:bv256, R3993:bv256, B4217:bool, R4214:bv256"
		AnnotationCmd:102 JSON{"key":{"name":"dsa.assign.end","type":"java.lang.String","erasureStrategy":"Erased"},"value":"4674_1005_0_0_0_0 -> 4643_1007_0_0_0_0"}
		AnnotationCmd:102 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.LoopSnippet.EndIter","iteration":2}}
		AnnotationCmd:102 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.LoopSnippet.EndLoopSnippet","loopId":3}}
		AnnotationCmd:102 JSON{"key":{"name":"end_loop.cmd","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		AssignExpCmd:142 tacMCANON2!!399:10 Store(tacMCANON2!!397:10 0x164 CANON99!!27:135 )
		AssignExpCmd:139 R400:90 0x120
		NopCmd
		AssignHavocCmd:139 R402:62
		AssignHavocCmd:102 tacReturndata!!403:75
		JumpCmd:102 0_0_0_9_0_0
	}
	Block 3_0_0_1_0_0 Succ [4_0_0_0_0_0] {
		AssumeNotCmd:143 false
		AnnotationCmd:53 JSON{"key":{"name":"pta.fake-return.start","type":"analysis.CmdPointer","erasureStrategy":"Erased"},"value":{"block":{"#class":"tac.BlockIdentifier","origStartPc":3278,"stkTop":1016,"decompCopy":0,"calleeIdx":0,"topOfStackValue":2,"freshCopy":0},"pos":1}}
		AnnotationCmd:53 JSON{"key":{"name":"pta.fake-return.end","type":"analysis.CmdPointer","erasureStrategy":"Erased"},"value":{"block":{"#class":"tac.BlockIdentifier","origStartPc":3278,"stkTop":1016,"decompCopy":0,"calleeIdx":0,"topOfStackValue":2,"freshCopy":0},"pos":6}}
		AssumeNotCmd:126 false
		AssignExpCmd:127 R404:144 Select(tacMCANON2!!226:9 0x140 )
		NopCmd
		AssumeExpCmd Apply(mul_noofl:bif R434:64 0x8ac7230489e80000)
		NopCmd
		AssignExpCmd:145 I413:51 IntMul(Apply(safe_math_promotion:bif R434:64) 0x8ac7230489e80000)
		NopCmd
		NopCmd
		AssumeExpCmd Gt(R404:144 0x0 )
		AssignExpCmd:146 R416:147 Div(Apply(safe_math_narrow:bif I413:51) R404:144 )
		AnnotationCmd:53 JSON{"key":{"name":"internal.func.end","type":"analysis.ip.InternalFuncExitAnnotation","erasureStrategy":"Canonical"},"value":{"id":0,"rets":[{"s":{"namePrefix":"R416","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1023}]},"offset":0}],"functionLayout":{"0":{"#class":"analysis.ip.InternalFuncValueLocation.Scalar"}}}}
		AnnotationCmd:53 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.EVMFunctionReturnWrite","returnbufOffset":"0","returnValueSym":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R416","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1023}]},"callIndex":1}}
		AnnotationCmd:53 JSON{"key":{"name":"tac.return.path","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		LabelCmd:53 "End procedure curve-getVirtualPrice()"
		NopCmd
		AnnotationCmd:53 JSON{"key":{"name":"call.trace.pop","type":"analysis.icfg.Inliner$CallStack$PopRecord","erasureStrategy":"Canonical"},"value":"rO0ABXNyAClhbmFseXNpcy5pY2ZnLklubGluZXIkQ2FsbFN0YWNrJFBvcFJlY29yZPAPfwSLdCWJAgABSQAIY2FsbGVlSWR4cAAAAAE="}
	}
	Block 3_0_0_7_0_0 Succ [7_0_0_0_0_0] {
		AssumeNotCmd:148 false
		AnnotationCmd:102 JSON{"key":{"name":"pta.fake-return.start","type":"analysis.CmdPointer","erasureStrategy":"Erased"},"value":{"block":{"#class":"tac.BlockIdentifier","origStartPc":3278,"stkTop":1016,"decompCopy":0,"calleeIdx":0,"topOfStackValue":2,"freshCopy":0},"pos":1}}
		AnnotationCmd:102 JSON{"key":{"name":"pta.fake-return.end","type":"analysis.CmdPointer","erasureStrategy":"Erased"},"value":{"block":{"#class":"tac.BlockIdentifier","origStartPc":3278,"stkTop":1016,"decompCopy":0,"calleeIdx":0,"topOfStackValue":2,"freshCopy":0},"pos":6}}
		AssumeNotCmd:136 false
		AssignExpCmd:137 R419:144 Select(tacMCANON2!!369:10 0x140 )
		NopCmd
		AssumeExpCmd Apply(mul_noofl:bif R444:64 0x8ac7230489e80000)
		NopCmd
		AssignExpCmd:149 I428:51 IntMul(Apply(safe_math_promotion:bif R444:64) 0x8ac7230489e80000)
		NopCmd
		NopCmd
		AssumeExpCmd Gt(R419:144 0x0 )
		AssignExpCmd:150 R431:147 Div(Apply(safe_math_narrow:bif I428:51) R419:144 )
		AnnotationCmd:102 JSON{"key":{"name":"internal.func.end","type":"analysis.ip.InternalFuncExitAnnotation","erasureStrategy":"Canonical"},"value":{"id":6,"rets":[{"s":{"namePrefix":"R431","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1023}]},"offset":0}],"functionLayout":{"0":{"#class":"analysis.ip.InternalFuncValueLocation.Scalar"}}}}
		AnnotationCmd:102 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.EVMFunctionReturnWrite","returnbufOffset":"0","returnValueSym":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R431","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1023}]},"callIndex":7}}
		AnnotationCmd:102 JSON{"key":{"name":"tac.return.path","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		LabelCmd:102 "End procedure curve-getVirtualPrice()"
		NopCmd
		AnnotationCmd:102 JSON{"key":{"name":"call.trace.pop","type":"analysis.icfg.Inliner$CallStack$PopRecord","erasureStrategy":"Canonical"},"value":"rO0ABXNyAClhbmFseXNpcy5pY2ZnLklubGluZXIkQ2FsbFN0YWNrJFBvcFJlY29yZPAPfwSLdCWJAgABSQAIY2FsbGVlSWR4cAAAAAc="}
	}
	Block 2_0_0_1_0_0 Succ [0_0_0_4_0_0] {
		AssumeNotCmd:130 false
		AnnotationCmd:53 JSON{"key":{"name":"pta.fake-return.start","type":"analysis.CmdPointer","erasureStrategy":"Erased"},"value":{"block":{"#class":"tac.BlockIdentifier","origStartPc":3129,"stkTop":1017,"decompCopy":0,"calleeIdx":0,"topOfStackValue":2,"freshCopy":0},"pos":1}}
		AnnotationCmd:53 JSON{"key":{"name":"pta.fake-return.end","type":"analysis.CmdPointer","erasureStrategy":"Erased"},"value":{"block":{"#class":"tac.BlockIdentifier","origStartPc":3129,"stkTop":1017,"decompCopy":0,"calleeIdx":0,"topOfStackValue":2,"freshCopy":0},"pos":6}}
		AssumeNotCmd:126 false
		AssignExpCmd:127 R434:64 Select(tacMCANON2!!212:9 0x120 )
		AssignExpCmd:53 B436:51 Le(CANON19!!21:151 0xffffffffffffffffffffffffffffffffffffffff )
		AssignExpCmd:53 B437:51 Ge(CANON19!!21:151 0x0 )
		NopCmd
		AssumeExpCmd LAnd(B436:51 B437:51 )
		AnnotationCmd:53 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet","value":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"CANON19!!21","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.scalarization.sort","type":"vc.data.ScalarizationSort","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.ScalarizationSort.Packed","packedStart":{"#class":"vc.data.ScalarizationSort.Split","idx":"c"},"start":0}},{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.storage.bit-width","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":160},{"key":{"name":"tac.storage.pretty.paths","type":"analysis.storage.DisplayPaths","erasureStrategy":"Erased"},"value":{"paths":[{"#class":"analysis.storage.DisplayPath.Root","name":"lp_token"}]}},{"key":{"name":"tac.slot.type","type":"spec.cvlast.typedescriptors.EVMTypeDescriptor$EVMValueType","erasureStrategy":"Canonical"},"value":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.address"}},{"key":{"name":"tac.storage.non-indexed-path","type":"analysis.storage.StorageAnalysisResult$NonIndexedPath","erasureStrategy":"Canonical"},"value":{"#class":"analysis.storage.StorageAnalysisResult.NonIndexedPath.Root","slot":"c"}},{"key":{"name":"tac.storage","type":"java.math.BigInteger","erasureStrategy":"Canonical"},"value":"ce4604a0000000000000000000000028"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1018}]},"displayPath":{"#class":"analysis.storage.DisplayPath.Root","name":"lp_token"},"storageType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.address"},"contractInstance":"ce4604a0000000000000000000000028","linkableStorageReadId":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet.Id","id":3}}}
		AnnotationCmd:53 JSON{"key":{"name":"init.reorder.fence","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		AssignExpCmd:143 tacMCANON2!!440:9 Store(tacMCANON2!!212:9 0x140 0x18160ddd00000000000000000000000000000000000000000000000000000000 )
		AssignExpCmd:143 R441:147 0x140
		AssignHavocCmd:143 R442:64
		AssignHavocCmd:53 tacReturndata!!443:75
		JumpCmd:53 0_0_0_4_0_0
	}
	Block 2_0_0_7_0_0 Succ [0_0_0_10_0_0] {
		AssumeNotCmd:139 false
		AnnotationCmd:102 JSON{"key":{"name":"pta.fake-return.start","type":"analysis.CmdPointer","erasureStrategy":"Erased"},"value":{"block":{"#class":"tac.BlockIdentifier","origStartPc":3129,"stkTop":1017,"decompCopy":0,"calleeIdx":0,"topOfStackValue":2,"freshCopy":0},"pos":1}}
		AnnotationCmd:102 JSON{"key":{"name":"pta.fake-return.end","type":"analysis.CmdPointer","erasureStrategy":"Erased"},"value":{"block":{"#class":"tac.BlockIdentifier","origStartPc":3129,"stkTop":1017,"decompCopy":0,"calleeIdx":0,"topOfStackValue":2,"freshCopy":0},"pos":6}}
		AssumeNotCmd:136 false
		AssignExpCmd:137 R444:64 Select(tacMCANON2!!355:10 0x120 )
		AssignExpCmd:102 B446:51 Le(CANON19!!21:151 0xffffffffffffffffffffffffffffffffffffffff )
		AssignExpCmd:102 B447:51 Ge(CANON19!!21:151 0x0 )
		NopCmd
		AssumeExpCmd LAnd(B446:51 B447:51 )
		AnnotationCmd:102 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet","value":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"CANON19!!21","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.scalarization.sort","type":"vc.data.ScalarizationSort","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.ScalarizationSort.Packed","packedStart":{"#class":"vc.data.ScalarizationSort.Split","idx":"c"},"start":0}},{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.storage.bit-width","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":160},{"key":{"name":"tac.storage.pretty.paths","type":"analysis.storage.DisplayPaths","erasureStrategy":"Erased"},"value":{"paths":[{"#class":"analysis.storage.DisplayPath.Root","name":"lp_token"}]}},{"key":{"name":"tac.slot.type","type":"spec.cvlast.typedescriptors.EVMTypeDescriptor$EVMValueType","erasureStrategy":"Canonical"},"value":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.address"}},{"key":{"name":"tac.storage.non-indexed-path","type":"analysis.storage.StorageAnalysisResult$NonIndexedPath","erasureStrategy":"Canonical"},"value":{"#class":"analysis.storage.StorageAnalysisResult.NonIndexedPath.Root","slot":"c"}},{"key":{"name":"tac.storage","type":"java.math.BigInteger","erasureStrategy":"Canonical"},"value":"ce4604a0000000000000000000000028"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1018}]},"displayPath":{"#class":"analysis.storage.DisplayPath.Root","name":"lp_token"},"storageType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.address"},"contractInstance":"ce4604a0000000000000000000000028","linkableStorageReadId":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet.Id","id":10}}}
		AnnotationCmd:102 JSON{"key":{"name":"init.reorder.fence","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		AssignExpCmd:148 tacMCANON2!!450:10 Store(tacMCANON2!!355:10 0x140 0x18160ddd00000000000000000000000000000000000000000000000000000000 )
		AssignExpCmd:148 R451:147 0x140
		AssignHavocCmd:148 R452:64
		AssignHavocCmd:102 tacReturndata!!453:75
		JumpCmd:102 0_0_0_10_0_0
	}
	Block 4_0_0_0_0_0 Succ [0_0_0_5_0_0] {
		AssumeNotCmd:53 false
		AssumeNotCmd:53 false
		AnnotationCmd JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageGlobalChangeSnippet.StorageTakeSnapshot","lhs":{"namePrefix":"lastStorage","tag":{"#class":"tac.Tag.BlockchainState"},"callIndex":0,"meta":[{"key":{"name":"cvl.local","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true},{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"lastStorage"},{"key":{"name":"cvl.type","type":"spec.cvlast.CVLType$PureCVLType","erasureStrategy":"CallTrace"},"value":{"#class":"spec.cvlast.CVLType.PureCVLType.VMInternal.BlockchainState"}},{"key":{"name":"cvl","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true},{"key":{"name":"cvl.display","type":"java.lang.String","erasureStrategy":"CallTrace"},"value":"lastStorage"}]}}}
		AssignExpCmd:152 CANON141!!454:153 Eq(I23 R416:147 )
		AssumeCmd:53 CANON141!!454:153
		AnnotationCmd:53 JSON{"key":{"name":"cvl.label.end","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		AnnotationCmd:154 JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Cmd","cmd":{"cmd_type":"spec.cvlast.CVLCmd.Simple.Apply","cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/specs/ViewReentrancy.spec","start":{"line":27,"character":4},"end":{"line":27,"character":15}},"exp":{"#class":"spec.cvlast.CVLExp.ApplyExp.ContractFunction.Symbolic","methodIdWithCallContext":{"#class":"spec.cvlast.ParametricMethod","methodId":"f","host":{"name":"curve"}},"args":[{"#class":"spec.cvlast.CVLExp.VariableExp","id":"e","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":0}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"env","fields":[{"fieldName":"msg","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"msg","fields":[{"fieldName":"sender","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"value","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}}]}},{"fieldName":"tx","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"tx","fields":[{"fieldName":"origin","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}}]}},{"fieldName":"block","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"block","fields":[{"fieldName":"coinbase","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"difficulty","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"gaslimit","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"number","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"timestamp","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}}]}}]},"cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/specs/ViewReentrancy.spec","start":{"line":27,"character":4},"end":{"line":27,"character":15}}},"twoStateIndex":"NEITHER"},{"#class":"spec.cvlast.CVLExp.VariableExp","id":"data","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":0}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.VMInternal.RawArgs"},"cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/specs/ViewReentrancy.spec","start":{"line":27,"character":4},"end":{"line":27,"character":15}}},"twoStateIndex":"NEITHER"}],"noRevert":true,"storage":{"#class":"spec.cvlast.CVLExp.VariableExp","id":"lastStorage","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":0}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.VMInternal.BlockchainState"},"cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/specs/ViewReentrancy.spec","start":{"line":27,"character":4},"end":{"line":27,"character":15}}},"twoStateIndex":"NEITHER"},"tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":0}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Void"},"cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/specs/ViewReentrancy.spec","start":{"line":27,"character":4},"end":{"line":27,"character":5}}}},"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":0}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}}}}}
		NopCmd
		NopCmd
		NopCmd
		NopCmd
		NopCmd
		NopCmd
		AssignExpCmd R461:155 CANON150:6
		AnnotationCmd:154 JSON{"key":{"name":"call.trace.push","type":"analysis.icfg.Inliner$CallStack$PushRecord","erasureStrategy":"Canonical"},"value":"rO0ABXNyACphbmFseXNpcy5pY2ZnLklubGluZXIkQ2FsbFN0YWNrJFB1c2hSZWNvcmSX8+DCTLCH+AIAA0kACGNhbGxlZUlkTAAGY2FsbGVldAATTHZjL2RhdGEvTWV0aG9kUmVmO0wAB3N1bW1hcnl0ABVMdmMvZGF0YS9DYWxsU3VtbWFyeTt4cAAAAAVzcgARdmMuZGF0YS5NZXRob2RSZWbJlJTzzU9pGAIAA0wABGF0dHJ0ABdMc2NlbmUvTWV0aG9kQXR0cmlidXRlO0wACmNvbnRyYWN0SWR0ABZMamF2YS9tYXRoL0JpZ0ludGVnZXI7TAAHc2lnSGFzaHQAEExldm0vU2lnaGFzaEludDt4cHNyABxzY2VuZS5NZXRob2RBdHRyaWJ1dGUkQ29tbW9uNHjdebdr9XMCAAB4cgAVc2NlbmUuTWV0aG9kQXR0cmlidXRlcYg2pYWutuUCAAB4cHNyABRqYXZhLm1hdGguQmlnSW50ZWdlcoz8nx+pO/sdAwAGSQAIYml0Q291bnRJAAliaXRMZW5ndGhJABNmaXJzdE5vbnplcm9CeXRlTnVtSQAMbG93ZXN0U2V0Qml0SQAGc2lnbnVtWwAJbWFnbml0dWRldAACW0J4cgAQamF2YS5sYW5nLk51bWJlcoaslR0LlOCLAgAAeHD///////////////7////+AAAAAXVyAAJbQqzzF/gGCFTgAgAAeHAAAAAQzkYEoAAAAAAAAAAAAAAAKHhzcgAOZXZtLlNpZ2hhc2hJbnRUdcqNMXEgeAIAAUwAAW5xAH4ABnhwc3EAfgAM///////////////+/////gAAAAF1cQB+ABAAAAAEPSSja3hw"}
		AssignExpCmd:154 M463:51 ByteMapDefinition(CANON152:bv256 -> Ite(Lt(CANON152:51 CANON150:6 ) Unconstrained(bv256) 0x0 ) )
		AssignExpCmd tacCalldatabuf@5:156 LongStore(M463:51 0x0 CANON148:5 0x0 CANON150:6 )
		NopCmd
		AssumeExpCmd Ge(R461:157 0x24 )
		NopCmd
		AssumeExpCmd Ge(0x7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff R461:157 )
		AssignExpCmd:154 B468 LAnd(Ge(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff CANON20:21 ) Le(0x0 CANON20:21 ) )
		AssertCmd:154 B468 "sanity bounds check on cvl to vm encoding of tacTmp!5024:int failed"
		AssignExpCmd:154 R469:51 Apply(safe_math_narrow:bif CANON20:21)
		NopCmd
		AssumeExpCmd LAnd(Le(R469:54 0xffffffffffffffffffffffffffffffffffffffff ) Ge(R469:54 0x0 ) )
		AssignExpCmd:154 B473 LAnd(Ge(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff CANON21:22 ) Le(0x0 CANON21:22 ) )
		AssertCmd:154 B473 "sanity bounds check on cvl to vm encoding of tacTmp!5027:int failed"
		AssignExpCmd:154 R474:51 Apply(safe_math_narrow:bif CANON21:22)
		NopCmd
		AssumeExpCmd LAnd(Le(R474:55 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff ) Ge(R474:55 0x0 ) )
		AssignExpCmd:154 B479 LAnd(Ge(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff CANON22:23 ) Le(0x0 CANON22:23 ) )
		AssertCmd:154 B479 "sanity bounds check on cvl to vm encoding of tacTmp!5031:int failed"
		AssignExpCmd:154 R480:51 Apply(safe_math_narrow:bif CANON22:23)
		NopCmd
		AssumeExpCmd LAnd(Le(R480:56 0xffffffffffffffffffffffffffffffffffffffff ) Ge(R480:56 0x0 ) )
		AssignExpCmd:154 B484 LAnd(Ge(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff CANON26:27 ) Le(0x0 CANON26:27 ) )
		AssertCmd:154 B484 "sanity bounds check on cvl to vm encoding of tacTmp!5034:int failed"
		AssignExpCmd:154 R485:51 Apply(safe_math_narrow:bif CANON26:27)
		NopCmd
		AssumeExpCmd LAnd(Le(R485:57 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff ) Ge(R485:57 0x0 ) )
		AssignExpCmd:154 B489 LAnd(Ge(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff CANON27:28 ) Le(0x0 CANON27:28 ) )
		AssertCmd:154 B489 "sanity bounds check on cvl to vm encoding of tacTmp!5037:int failed"
		AssignExpCmd:154 R490:51 Apply(safe_math_narrow:bif CANON27:28)
		NopCmd
		AssumeExpCmd LAnd(Le(R490:58 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff ) Ge(R490:58 0x0 ) )
		AssignExpCmd:154 B494 LAnd(Ge(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff CANON21:22 ) Le(0x0 CANON21:22 ) )
		AssertCmd:154 B494 "sanity bounds check on cvl to vm encoding of tacTmp!5040:int failed"
		AssignExpCmd:154 R495:51 Apply(safe_math_narrow:bif CANON21:22)
		AssignExpCmd:154 B497 LAnd(Ge(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff CANON20:21 ) Le(0x0 CANON20:21 ) )
		AssertCmd:154 B497 "sanity bounds check on cvl to vm encoding of tacTmp!5043:int failed"
		AssignExpCmd:154 R498:51 Apply(safe_math_narrow:bif CANON20:21)
		AssignExpCmd:154 R501:51 Select(tacBalance!!127:14 Apply(to_skey:bif R498:51) )
		AssignExpCmd:158 I502:51 IntSub(R501:51 R495:51 )
		AssignExpCmd:158 tacBalance!!503:14 Store(tacBalance!!127:14 Apply(to_skey:bif R498:51) I502:51 )
		AssignExpCmd:154 R504:51 Select(tacBalance!!503:14 Apply(to_skey:bif R30:43) )
		AssignExpCmd:158 R505:51 Add(R504:51 R495:51)
		NopCmd
		AssumeExpCmd Apply(add_noofl:bif R504:51 R495:51)
		AssignExpCmd:158 tacBalance!!507:14 Store(tacBalance!!503:14 Apply(to_skey:bif R30:43) R505:51 )
		AnnotationCmd:154 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.BalanceSnippet","srcAccountInfo":{"old":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R501","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}]},"new":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"I502","tag":{"#class":"tac.Tag.Int"},"callIndex":0,"meta":[{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}]},"addr":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R498","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}]}},"trgAccountInfo":{"old":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R504","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}]},"new":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R505","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}]},"addr":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R30","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"tacContractAt"},{"key":{"name":"tac.contract.sym.addr.name","type":"java.lang.String","erasureStrategy":"Erased"},"value":"curve"},{"key":{"name":"tac.contract.sym.addr","type":"java.math.BigInteger","erasureStrategy":"Erased"},"value":"ce4604a0000000000000000000000028"}]}},"transferredAmount":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R495","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}]}}}
		JumpCmd 0_0_0_5_0_0
	}
	Block 7_0_0_0_0_0 Succ [] {
		AssumeNotCmd:102 false
		AssumeNotCmd:102 false
		AnnotationCmd JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageGlobalChangeSnippet.StorageTakeSnapshot","lhs":{"namePrefix":"lastStorage","tag":{"#class":"tac.Tag.BlockchainState"},"callIndex":0,"meta":[{"key":{"name":"cvl.local","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true},{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"lastStorage"},{"key":{"name":"cvl.type","type":"spec.cvlast.CVLType$PureCVLType","erasureStrategy":"CallTrace"},"value":{"#class":"spec.cvlast.CVLType.PureCVLType.VMInternal.BlockchainState"}},{"key":{"name":"cvl","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true},{"key":{"name":"cvl.display","type":"java.lang.String","erasureStrategy":"CallTrace"},"value":"lastStorage"}]}}}
		AssignExpCmd:159 CANON241!!508:153 Eq(I8 R431:147 )
		AssumeCmd:102 CANON241!!508:153
		AnnotationCmd:102 JSON{"key":{"name":"cvl.label.end","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		AnnotationCmd:160 JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Cmd","cmd":{"cmd_type":"spec.cvlast.CVLCmd.Simple.Assert","cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/specs/ViewReentrancy.spec","start":{"line":29,"character":4},"end":{"line":29,"character":16}},"exp":{"#class":"spec.cvlast.CVLExp.VariableExp","id":"cond","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":0}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"},"cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/specs/ViewReentrancy.spec","start":{"line":29,"character":4},"end":{"line":29,"character":16}}},"twoStateIndex":"NEITHER"},"description":"","scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":0}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}}}}}
		AssertCmd:161 B22 ""
		AnnotationCmd:160 JSON{"key":{"name":"cvl.label.end","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
	}
	Block 0_0_0_5_0_0 Succ [0_0_0_6_0_0] {
		LabelCmd "Start procedure curve-_balances(uint256)"
		AnnotationCmd JSON{"key":{"name":"fps.free-pointer-is-scalarized","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true}
		AssignExpCmd R510:51 Select(tacExtcodesize!!7:4 Apply(to_skey:bif R30:60) )
		NopCmd
		AssumeExpCmd Gt(R510:51 0x0 )
		AnnotationCmd JSON{"key":{"name":"internal.func.finder.info","type":"analysis.ip.InternalFunctionFinderReport","erasureStrategy":"Erased"},"value":"rO0ABXNyAChhbmFseXNpcy5pcC5JbnRlcm5hbEZ1bmN0aW9uRmluZGVyUmVwb3J0ian+bYn1VdACAAFMABN1bnJlc29sdmVkRnVuY3Rpb25zdAAPTGphdmEvdXRpbC9TZXQ7eHBzcgAhZGF0YXN0cnVjdHVyZXMuTGlua2VkQXJyYXlIYXNoU2V0AAAAAAAAAAEDAAJGAApsb2FkRmFjdG9yTAAJaGFzaFRhYmxldAAuTGRhdGFzdHJ1Y3R1cmVzL2FycmF5aGFzaHRhYmxlL0FycmF5SGFzaFRhYmxlO3hwdwgAAAAAQAAAAHg="}
		AnnotationCmd JSON{"key":{"name":"fps.free-pointer-is-scalarized","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true}
		NopCmd
		AssumeExpCmd Eq(R474:55 0x0 )
		NopCmd
		AssumeExpCmd LNot(Lt(R461:157 0x4 ) )
		NopCmd
		AssumeExpCmd Gt(0x82c63066 tacSighash!!35:44 )
		NopCmd
		AssumeExpCmd LNot(Eq(0x3842f776 tacSighash!!35:44 ) )
		NopCmd
		AssumeExpCmd Eq(0x3d24a36b tacSighash!!35:44 )
		AssignExpCmd:162 R517:80 Sub(CANON150:6 0x4 )
		NopCmd
		AssumeExpCmd LNot(Slt(R517:80 0x20 ) )
		AssignExpCmd:163 R519:69 Select(tacCalldatabuf@5:156 0x4 )
		AnnotationCmd JSON{"key":{"name":"pta.end-allocation","type":"analysis.alloc.AllocationAnalysis$AbstractLocation","erasureStrategy":"Erased"},"value":{"prevFPWriteIdx":0,"nextFPWriteCmd":{"block":{"#class":"tac.BlockIdentifier","origStartPc":4211,"stkTop":1012,"decompCopy":0,"calleeIdx":0,"topOfStackValue":0,"freshCopy":0},"pos":8},"sort":{"#class":"analysis.alloc.AllocationAnalysis.Alloc.ConstBlock","sz":"40"}}}
		AssignExpCmd:164 R520:80 Select(CANON77!!24:37 Apply(skey_basic:bif 0x8) )
		AnnotationCmd JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet","value":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R520","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1017}]},"displayPath":{"#class":"analysis.storage.DisplayPath.ArrayAccess","index":{"#class":"vc.data.TACSymbol.Const","value":"0"},"base":{"#class":"analysis.storage.DisplayPath.Root","name":"admin_balances"}},"storageType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256},"contractInstance":"ce4604a0000000000000000000000028","linkableStorageReadId":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet.None"}}}
		AssignExpCmd:165 R521:90 Select(tacBalance!!507:14 Apply(to_skey:bif R30:60) )
		NopCmd
		AssumeExpCmd LNot(Lt(R521:90 R520:80 ) )
		AssignExpCmd:166 R523:69 Sub(R521:90 R520:80 )
		NopCmd
		AssumeExpCmd LNot(Lt(R523:69 R519:69 ) )
		AssignExpCmd:167 R527:81 Select(CANON77!!24:37 Apply(skey_basic:bif 0x9) )
		AnnotationCmd JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet","value":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R527","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1018}]},"displayPath":{"#class":"analysis.storage.DisplayPath.ArrayAccess","index":{"#class":"vc.data.TACSymbol.Const","value":"1"},"base":{"#class":"analysis.storage.DisplayPath.Root","name":"admin_balances"}},"storageType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256},"contractInstance":"ce4604a0000000000000000000000028","linkableStorageReadId":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet.None"}}}
		AssignExpCmd B529:51 Le(CANON18!!20:168 0xffffffffffffffffffffffffffffffffffffffff )
		AssignExpCmd B530:51 Ge(CANON18!!20:168 0x0 )
		NopCmd
		AssumeExpCmd LAnd(B529:51 B530:51 )
		AnnotationCmd JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet","value":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"CANON18!!20","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.scalarization.sort","type":"vc.data.ScalarizationSort","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.ScalarizationSort.Packed","packedStart":{"#class":"vc.data.ScalarizationSort.Split","idx":"b"},"start":0}},{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.storage.bit-width","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":160},{"key":{"name":"tac.storage.pretty.paths","type":"analysis.storage.DisplayPaths","erasureStrategy":"Erased"},"value":{"paths":[{"#class":"analysis.storage.DisplayPath.Root","name":"coins_1"}]}},{"key":{"name":"tac.slot.type","type":"spec.cvlast.typedescriptors.EVMTypeDescriptor$EVMValueType","erasureStrategy":"Canonical"},"value":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.address"}},{"key":{"name":"tac.storage.non-indexed-path","type":"analysis.storage.StorageAnalysisResult$NonIndexedPath","erasureStrategy":"Canonical"},"value":{"#class":"analysis.storage.StorageAnalysisResult.NonIndexedPath.Root","slot":"b"}},{"key":{"name":"tac.storage","type":"java.math.BigInteger","erasureStrategy":"Canonical"},"value":"ce4604a0000000000000000000000028"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1016}]},"displayPath":{"#class":"analysis.storage.DisplayPath.Root","name":"coins_1"},"storageType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.address"},"contractInstance":"ce4604a0000000000000000000000028","linkableStorageReadId":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet.Id","id":5}}}
		AnnotationCmd JSON{"key":{"name":"init.reorder.fence","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		AssignExpCmd:169 tacMCANON6!!533:13 Store(tacMCANON6!!16:13 0x100 0x70a0823100000000000000000000000000000000000000000000000000000000 )
		AssignExpCmd:170 tacMCANON6!!535:13 Store(tacMCANON6!!533:13 0x104 R30:60 )
		AssignExpCmd:169 R536:69 0x100
		AssignHavocCmd:169 R537:66
		AssignHavocCmd tacReturndata!!538:75
		JumpCmd 0_0_0_6_0_0
	}
	Block 0_0_0_6_0_0 Succ [5_0_0_5_0_0] {
		AnnotationCmd JSON{"key":{"name":"call.trace.push","type":"analysis.icfg.Inliner$CallStack$PushRecord","erasureStrategy":"Canonical"},"value":"rO0ABXNyACphbmFseXNpcy5pY2ZnLklubGluZXIkQ2FsbFN0YWNrJFB1c2hSZWNvcmSX8+DCTLCH+AIAA0kACGNhbGxlZUlkTAAGY2FsbGVldAATTHZjL2RhdGEvTWV0aG9kUmVmO0wAB3N1bW1hcnl0ABVMdmMvZGF0YS9DYWxsU3VtbWFyeTt4cAAAAAZzcgARdmMuZGF0YS5NZXRob2RSZWbJlJTzzU9pGAIAA0wABGF0dHJ0ABdMc2NlbmUvTWV0aG9kQXR0cmlidXRlO0wACmNvbnRyYWN0SWR0ABZMamF2YS9tYXRoL0JpZ0ludGVnZXI7TAAHc2lnSGFzaHQAEExldm0vU2lnaGFzaEludDt4cHNyABxzY2VuZS5NZXRob2RBdHRyaWJ1dGUkQ29tbW9uNHjdebdr9XMCAAB4cgAVc2NlbmUuTWV0aG9kQXR0cmlidXRlcYg2pYWutuUCAAB4cHNyABRqYXZhLm1hdGguQmlnSW50ZWdlcoz8nx+pO/sdAwAGSQAIYml0Q291bnRJAAliaXRMZW5ndGhJABNmaXJzdE5vbnplcm9CeXRlTnVtSQAMbG93ZXN0U2V0Qml0SQAGc2lnbnVtWwAJbWFnbml0dWRldAACW0J4cgAQamF2YS5sYW5nLk51bWJlcoaslR0LlOCLAgAAeHD///////////////7////+AAAAAXVyAAJbQqzzF/gGCFTgAgAAeHAAAAAQzkYEoAAAAAAAAAAAAAAAEXhzcgAOZXZtLlNpZ2hhc2hJbnRUdcqNMXEgeAIAAUwAAW5xAH4ABnhwc3EAfgAM///////////////+/////gAAAAF1cQB+ABAAAAAEcKCCMXhzcgATdmMuZGF0YS5DYWxsU3VtbWFyeZQcmw5vl+FdAgAQSQAJc3VtbWFyeUlkTAAOY2FsbENvbnZlbnRpb250ACZMaW5zdHJ1bWVudGF0aW9uL2NhbGxzL0NhbGxDb252ZW50aW9uO0wACmNhbGxUYXJnZXR0ABpMYW5hbHlzaXMvaWNmZy9DYWxsVGFyZ2V0O0wACGNhbGxUeXBldAAVTHZjL2RhdGEvVEFDQ2FsbFR5cGU7TAAPY2Fubm90QmVJbmxpbmVkdAAtTGFuYWx5c2lzL2ljZmcvSW5saW5lciRJbGxlZ2FsSW5saW5pbmdSZWFzb247TAAGZ2FzVmFydAATTHZjL2RhdGEvVEFDU3ltYm9sO0wABmluQmFzZXEAfgAbTAAIaW5PZmZzZXRxAH4AG0wABmluU2l6ZXEAfgAbTAAMb3JpZ0NhbGxjb3JldAAgTHZjL2RhdGEvVEFDQ21kJFNpbXBsZSRDYWxsQ29yZTtMAAdvdXRCYXNlcQB+ABtMAAlvdXRPZmZzZXRxAH4AG0wAB291dFNpemVxAH4AG0wADXNpZ1Jlc29sdXRpb250AA9MamF2YS91dGlsL1NldDtMAAV0b1ZhcnEAfgAbTAAIdmFsdWVWYXJxAH4AG3hwAAAAA3NyACRpbnN0cnVtZW50YXRpb24uY2FsbHMuQ2FsbENvbnZlbnRpb25HtO1ulL788QIAA0kACGNhbGxlcklkTAAFaW5wdXR0ABlMYW5hbHlzaXMvaWNmZy9DYWxsSW5wdXQ7TAAGcmF3T3V0dAAiTGluc3RydW1lbnRhdGlvbi9jYWxscy9DYWxsT3V0cHV0O3hwAAAAAHNyABdhbmFseXNpcy5pY2ZnLkNhbGxJbnB1dJjJD1MhNUxQAgAHTAAHYmFzZVZhcnQAGUx2Yy9kYXRhL1RBQ0V4cHIkU3ltJFZhcjtMABBlbmNvZGVkQXJndW1lbnRzdAAjTGFuYWx5c2lzL2ljZmcvQUJJQXJndW1lbnRFbmNvZGluZztMABNpbnB1dFNpemVMb3dlckJvdW5kcQB+AAZMAAZvZmZzZXR0ABVMdmMvZGF0YS9UQUNFeHByJFN5bTtMABRyYW5nZVRvRGVjb21wb3NlZEFyZ3QAD0xqYXZhL3V0aWwvTWFwO0wAEHNpbXBsaWZpZWRPZmZzZXR0ABtMdmMvZGF0YS9UQUNFeHByJFN5bSRDb25zdDtMAARzaXplcQB+ACZ4cHNyABd2Yy5kYXRhLlRBQ0V4cHIkU3ltJFZhcskrg43eGgPnAgACTAABc3QAF0x2Yy9kYXRhL1RBQ1N5bWJvbCRWYXI7TAADdGFndAAJTHRhYy9UYWc7eHIAE3ZjLmRhdGEuVEFDRXhwciRTeW2iVj0S4YSNUAIAAHhyAA92Yy5kYXRhLlRBQ0V4cHJYhGlUu/v+yAIAAHhwc3IANnZjLmRhdGEuVEFDU3ltYm9sJFZhciRXaXRoRGVmYXVsdENhbGxJbmRleCRXaXRoQnl0ZU1hcJ7+oHF4CHAAAgACTAAEbWV0YXQALUxrb3RsaW54L2NvbGxlY3Rpb25zL2ltbXV0YWJsZS9QZXJzaXN0ZW50TWFwO0wACm5hbWVQcmVmaXh0ABJMamF2YS9sYW5nL1N0cmluZzt4cgAVdmMuZGF0YS5UQUNTeW1ib2wkVmFyCYrCGVl9SXYCAAB4cgARdmMuZGF0YS5UQUNTeW1ib2zd3Run/CoWswIAAHhwc3IAJmRhdGFzdHJ1Y3R1cmVzLnRyZWFwLkhhc2hUcmVhcE1hcCROb2Rlf2t9acJIPnQCAANMAANrZXl0ABJMamF2YS9sYW5nL09iamVjdDtMAARuZXh0dAA1TGRhdGFzdHJ1Y3R1cmVzL3RyZWFwL0hhc2hUcmVhcE1hcCRNb3JlS2V5VmFsdWVQYWlycztMAAV2YWx1ZXEAfgA3eHIAIWRhdGFzdHJ1Y3R1cmVzLnRyZWFwLkhhc2hUcmVhcE1hcPMJ/2vt3boKAgAAeHIAHWRhdGFzdHJ1Y3R1cmVzLnRyZWFwLlRyZWFwTWFw46LAyn3v5moCAAB4cgAaZGF0YXN0cnVjdHVyZXMudHJlYXAuVHJlYXA88f21zZwbdQIAAkwABGxlZnR0ABxMZGF0YXN0cnVjdHVyZXMvdHJlYXAvVHJlYXA7TAAFcmlnaHRxAH4APHhwcHNxAH4ANnBzcQB+ADZwcHNyAAt0YWMuTWV0YUtleVF/W3MiCfIZAgADTAAPZXJhc3VyZVN0cmF0ZWd5dAAdTHRhYy9NZXRhS2V5JEVyYXN1cmVTdHJhdGVneTtMAARuYW1lcQB+ADJMAAN0eXB0ABFMamF2YS9sYW5nL0NsYXNzO3hwfnIAG3RhYy5NZXRhS2V5JEVyYXN1cmVTdHJhdGVneQAAAAAAAAAAEgAAeHIADmphdmEubGFuZy5FbnVtAAAAAAAAAAASAAB4cHQACUNhbm9uaWNhbHQAF3RhYy5tZW1vcnkucGFydGl0aW9uLWlkdnIAEWphdmEubGFuZy5JbnRlZ2VyEuKgpPeBhzgCAAFJAAV2YWx1ZXhxAH4ADnBzcQB+AEkAAAAGc3EAfgBAcQB+AEZ0ABJUYWMuc3ltYm9sLmtleXdvcmR2cgAQamF2YS5sYW5nLlN0cmluZ6DwpDh6O7NCAgAAeHBwdAAEdGFjTXNxAH4AQHEAfgBGdAANdGFjLmlzLm1lbW9yeXZyACJ0YWMuTWV0YU1hcCRDb21wYW5pb24kTm90aGluZ1ZhbHVl8nsHH85ykpUCAAB4cHBzcQB+AFN0AA90YWNNQ0FOT042ISE1MzVzcgAPdGFjLlRhZyRCeXRlTWFwNb/Ry6GDRgkCAAB4cgALdGFjLlRhZyRNYXABJytzDV3P/QIAAHhyAAd0YWMuVGFnLk9V3gn2xngCAAB4cHBzcQB+AAz///////////////7////+AAAAAXVxAH4AEAAAAAEkeHNxAH4AKnNyADV2Yy5kYXRhLlRBQ1N5bWJvbCRWYXIkV2l0aERlZmF1bHRDYWxsSW5kZXgkV2l0aEJpdDI1NnqsyEgq0drPAgACTAAEbWV0YXEAfgAxTAAKbmFtZVByZWZpeHEAfgAyeHEAfgAzc3EAfgA2c3EAfgA2cHBxAH4ATHB0AAFMcHNxAH4AQHEAfgBGdAAQdGFjLnN0YWNrLmhlaWdodHEAfgBKcHNxAH4ASQAAA/V0AARSNTM2c3IADnRhYy5UYWckQml0MjU2IyLQT+LlKkgCAAB4cQB+AFlzcgARamF2YS51dGlsLkhhc2hNYXAFB9rBwxZg0QMAAkYACmxvYWRGYWN0b3JJAAl0aHJlc2hvbGR4cD9AAAAAAAADdwgAAAAEAAAAAnNyAB5hbmFseXNpcy5pY2ZnLlNjcmF0Y2hCeXRlUmFuZ2XBTLaPpUzj2gIAAkwABGZyb21xAH4ABkwAAnRvcQB+AAZ4cHNxAH4ADP///////////////v////4AAAAAdXEAfgAQAAAAAHhzcQB+AAz///////////////7////+AAAAAXVxAH4AEAAAAAEDeHNyAC1hbmFseXNpcy5pY2ZnLkRlY29tcG9zZWRDYWxsSW5wdXRBcmckQ29uc3RhbnSFavLdQafqPQIAA0wAAWN0ABlMdmMvZGF0YS9UQUNTeW1ib2wkQ29uc3Q7TAARY29udHJhY3RSZWZlcmVuY2V0AC9MYW5hbHlzaXMvaWNmZy9DYWxsR3JhcGhCdWlsZGVyJENhbGxlZENvbnRyYWN0O0wADHNjcmF0Y2hSYW5nZXQAIExhbmFseXNpcy9pY2ZnL1NjcmF0Y2hCeXRlUmFuZ2U7eHIAJGFuYWx5c2lzLmljZmcuRGVjb21wb3NlZENhbGxJbnB1dEFy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cGV0ABNMY29tcGlsZXIvSnVtcFR5cGU7TAANc291cmNlQ29udGV4dHQAGExjb21waWxlci9Tb3VyY2VDb250ZXh0O3hwcHNxAH4A5QAAFx8AAAAnAAAAB3EAfgCGfnIAEWNvbXBpbGVyLkp1bXBUeXBlAAAAAAAAAAASAAB4cQB+AEV0AAdSRUdVTEFSc3IAFmNvbXBpbGVyLlNvdXJjZUNvbnRleHSMy1vpQFzaEwIAAkwAD2luZGV4VG9GaWxlcGF0aHEAfgAnTAAJc291cmNlRGlycQB+ADJ4cHNxAH4AaT9AAAAAAAAMdwgAAAAQAAAACHNxAH4ASQAAAAB0ABVjb250cmFjdHMvQ29udGV4dC5zb2xzcQB+AEkAAAABdAAYY29udHJhY3RzL0N1cnZlVG9rZW4uc29sc3EAfgBJAAAAAnQAH2NvbnRyYWN0cy9DdXJ2ZVRva2VuRXhhbXBsZS5zb2xzcQB+AEkAAAADdAATY29udHJhY3RzL0VSQzIwLnNvbHNxAH4ASQAAAAR0ABRjb250cmFjdHMvSUVSQzIwLnNvbHNxAH4ASQAAAAV0ABxjb250cmFjdHMvSUVSQzIwTWV0YWRhdGEuc29scQB+AEt0AB1jb250cmFjdHMvUmVlbnRyYW5jeUd1YXJkLnNvbHNxAH4ASQAAAAd0ABNjb250cmFjdHMvY3VydmUuc29seHQAEy5wb3N0X2F1dG9maW5kZXJzLjJzcQB+ADBzcQB+ADZwc3EAfgA2cHNxAH4ANnBwcQB+AENwcQB+AEtxAH4ATHBxAH4AUHEAfgBRcHEAfgBVcQB+AFZzcQB+AF5zcQB+ADZzcQB+ADZwcHEAfgBMcHEAfgBicHEAfgBjcHEAfgCzcQB+AGZxAH4AtnNxAH4AXnNxAH4ANnNxAH4ANnNxAH4ANnNxAH4ANnBzcQB+ADZwcHEAfgBMcHEAfgBic3EAfgBAcQB+AEZ0ABZ0YWMuc2NhbGFyaXphdGlvbi5zb3J0dnIAGXZjLmRhdGEuU2NhbGFyaXphdGlvblNvcnQwznCd5GgNJgIAAHhwcHNyACB2Yy5kYXRhLlNjYWxhcml6YXRpb25Tb3J0JFBhY2tlZC5FrRKTiOT3AgACSQAFc3RhcnRMAAtwYWNrZWRTdGFydHQAG0x2Yy9kYXRhL1NjYWxhcml6YXRpb25Tb3J0O3hxAH4BDwAAAABzcgAfdmMuZGF0YS5TY2FsYXJpemF0aW9uU29ydCRTcGxpdFT/Wafxx7IFAgABTAADaWR4cQB+AAZ4cQB+AQ9zcQB+AAz///////////////7////+AAAAAXVxAH4AEAAAAAELeHNxAH4ANnBzcQB+ADZwc3EAfgA2cHBzcQB+AEBxAH4ARnQAHHRhYy5zdG9yYWdlLm5vbi1pbmRleGVkLXBhdGh2cgA1YW5hbHlzaXMuc3RvcmFnZS5TdG9yYWdlQW5hbHlzaXNSZXN1bHQkTm9uSW5kZXhlZFBhdGgIwaBLofo/RQIAAHhwcHNyADphbmFseXNpcy5zdG9yYWdlLlN0b3JhZ2VBbmFseXNpc1Jlc3VsdCROb25JbmRleGVkUGF0aCRSb290vzf12KXqCv8CAAFMAARzbG90cQB+AAZ4cQB+AR1xAH4BFnNxAH4AQHEAfgBGdAANdGFjLnNsb3QudHlwZXZyADpzcGVjLmN2bGFzdC50eXBlZGVzY3JpcHRvcnMuRVZNVHlwZURlc2NyaXB0b3IkRVZNVmFsdWVUeXBlxomvArrquCUCAAB4cgAtc3BlYy5jdmxhc3QudHlwZWRlc2NyaXB0b3JzLkVWTVR5cGVEZXNjcmlwdG9yyFGp8TzCah0CAAB4cHBzcgA1c3BlYy5jdmxhc3QudHlwZWRlc2NyaXB0b3JzLkVWTVR5cGVEZXNjcmlwdG9yJGFkZHJlc3N6+GX0b5egKQIAAHhyAERzcGVjLmN2bGFzdC50eXBlZGVzY3JpcHRvcnMuRVZNVHlwZURlc2NyaXB0b3IkRVZNSXNvbW9ycGhpY1ZhbHVlVHlwZfd1mJFuEKEPAgAAeHEAfgEjc3EAfgBAcQB+AJB0ABh0YWMuc3RvcmFnZS5wcmV0dHkucGF0aHN2cgAdYW5hbHlzaXMuc3RvcmFnZS5EaXNwbGF5UGF0aHP3REu3w/VRFgIAAUwABXBhdGhzcQB+AB14cHBzcQB+AStzcgAXamF2YS51dGlsLkxpbmtlZEhhc2hTZXTYbNdald0qHgIAAHhyABFqYXZhLnV0aWwuSGFzaFNldLpEhZWWuLc0AwAAeHB3DAAAABA/QAAAAAAAAXNyACFhbmFseXNpcy5zdG9yYWdlLkRpc3BsYXlQYXRoJFJvb3TTc6C9mdA8cgIAAkwABGJhc2V0AB5MYW5hbHlzaXMvc3RvcmFnZS9EaXNwbGF5UGF0aDtMAARuYW1lcQB+ADJ4cgAcYW5hbHlzaXMuc3RvcmFnZS5EaXNwbGF5UGF0aE9AY+pW0iAFAgAAeHBwdAAHY29pbnNfMXhzcQB+AEBxAH4ARnQAFXRhYy5zdG9yYWdlLmJpdC13aWR0aHEAfgBKcHNxAH4ASQAAAKBwc3EAfgBAcQB+AEZ0AAt0YWMuc3RvcmFnZXEAfgCZcHEAfgCGcHEAfgBjcHNxAH4ASQAAA/l0AAtDQU5PTjE4ISEyMHNxAH4Ad3EAfgBocQB+AG1zcQB+ADBzcQB+ADZwc3EAfgA2cHNxAH4ANnBwcQB+AENwcQB+AEtxAH4ATHBxAH4AUHEAfgBRcHEAfgBVcQB+AFZzcQB+AF5zcQB+ADZzcQB+ADZwcHEAfgBMcHEAfgBicHEAfgBjcHEAfgCzcQB+AGZxAH4AtnNyACJqYXZhLnV0aWwuQ29sbGVjdGlvbnMkU2luZ2xldG9uU2V0LFJBmCnAsb8CAAFMAAdlbGVtZW50cQB+ADd4cHEAfgAUc3EAfgBec3EAfgA2c3EAfgA2c3EAfgA2c3EAfgA2cHNxAH4ANnBwcQB+AExwcQB+AGJxAH4BDXBxAH4BE3NxAH4ANnBzcQB+ADZwc3EAfgA2cHBxAH4BG3BxAH4BIHEAfgEhcHEAfgEocQB+ASlwc3EAfgErc3EAfgEudwwAAAAQP0AAAAAAAAFxAH4BNHhxAH4BNnBxAH4BOHBxAH4BOXBxAH4AhnBxAH4AY3BxAH4BO3EAfgE8c3EAfgB3cQB+AGhxAH4AbQ=="}
		AnnotationCmd JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageGlobalChangeSnippet.StorageBackupPoint","calleeTxId":6}}
		NopCmd
		AssumeExpCmd LAnd(Eq(tacCalldatasize!!3:3 0x24 ) Eq(tacCalldatasize!!3:3 0x24 ) )
		NopCmd
		AssumeExpCmd Eq(tacCalldatabufCANON0@6:1 0x70a0823100000000000000000000000000000000000000000000000000000000 )
		AssignExpCmd tacCalldatabufCANON1@6:171 R30:172
		LabelCmd "Start procedure ERC20-balanceOf(address)"
		AnnotationCmd JSON{"key":{"name":"fps.free-pointer-is-scalarized","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true}
		AssignExpCmd R542:51 Select(tacExtcodesize!!7:4 Apply(to_skey:bif R29:78) )
		NopCmd
		AssumeExpCmd Gt(R542:51 0x0 )
		AnnotationCmd JSON{"key":{"name":"internal.func.finder.info","type":"analysis.ip.InternalFunctionFinderReport","erasureStrategy":"Erased"},"value":"rO0ABXNyAChhbmFseXNpcy5pcC5JbnRlcm5hbEZ1bmN0aW9uRmluZGVyUmVwb3J0ian+bYn1VdACAAFMABN1bnJlc29sdmVkRnVuY3Rpb25zdAAPTGphdmEvdXRpbC9TZXQ7eHBzcgAhZGF0YXN0cnVjdHVyZXMuTGlua2VkQXJyYXlIYXNoU2V0AAAAAAAAAAEDAAJGAApsb2FkRmFjdG9yTAAJaGFzaFRhYmxldAAuTGRhdGFzdHJ1Y3R1cmVzL2FycmF5aGFzaHRhYmxlL0FycmF5SGFzaFRhYmxlO3hwdwgAAAAAQAAAAHg="}
		AnnotationCmd JSON{"key":{"name":"fps.free-pointer-is-scalarized","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true}
		NopCmd
		AssumeExpCmd LNot(Lt(tacCalldatasize!!3:3 0x4 ) )
		NopCmd
		AssumeExpCmd LNot(Gt(0x39509351 tacSighash!!36:44 ) )
		NopCmd
		AssumeExpCmd LNot(Eq(0x39509351 tacSighash!!36:44 ) )
		NopCmd
		AssumeExpCmd Eq(0x70a08231 tacSighash!!36:44 )
		AssignExpCmd:173 R548:80 Sub(tacCalldatasize!!3:3 0x4 )
		AssignExpCmd B549:81 Slt(R548:80 0x20 )
		NopCmd
		AssumeExpCmd LNot(B549:81 )
		AssignExpCmd:174 R551:69 tacCalldatabufCANON1@6:175
		NopCmd
		AssumeExpCmd Eq(tacCalldatabufCANON1@6:175 tacCalldatabufCANON1@6:175 )
		AnnotationCmd JSON{"key":{"name":"internal.func.start","type":"analysis.ip.InternalFuncStartAnnotation","erasureStrategy":"CallTrace"},"value":{"id":5,"startPc":1712,"args":[{"s":{"namePrefix":"R551","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1013}]},"offset":1,"sort":"SCALAR"}],"methodSignature":{"#class":"spec.cvlast.QualifiedMethodSignature.QualifiedMethodSig","qualifiedMethodName":{"#class":"spec.cvlast.QualifiedFunction","host":{"name":"ERC20"},"methodId":"balanceOf"},"params":[{"#class":"spec.cvlast.VMParam.Named","name":"account","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$address"}}],"res":[{"#class":"spec.cvlast.VMParam.Unnamed","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256}}]},"stackOffsetToArgPos":{"1":0},"callSiteSrc":{"source":1,"begin":4376,"len":467,"jumpType":"ENTER","address":"ce4604a0000000000000000000000011","sourceContext":{"indexToFilepath":{"0":"contracts/Context.sol","1":"contracts/ERC20.sol","2":"contracts/IERC20.sol","3":"contracts/IERC20Metadata.sol"},"sourceDir":".post_autofinders.1"}}}}
		AssignExpCmd:176 R556:85 Apply(hash_3_keccak:bif Apply(skey_basic:bif 0x40) Apply(to_skey:bif tacCalldatabufCANON1@6:175) Apply(skey_basic:bif 0x0))
		AssignExpCmd:177 R557:85 Select(CANON93!!26:39 R556:178 )
		AnnotationCmd JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet","value":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R557","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1020}]},"displayPath":{"#class":"analysis.storage.DisplayPath.MapAccess","key":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R551","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1018}]},"keyTyp":{"#class":"tac.TACStorageType.IntegralType","typeLabel":"address","numBytes":"14","descriptor":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$address"},"lowerBound":null,"upperBound":null},"base":{"#class":"analysis.storage.DisplayPath.Root","name":"_balances"}},"storageType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256},"contractInstance":"ce4604a0000000000000000000000011","linkableStorageReadId":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet.None"}}}
		AnnotationCmd JSON{"key":{"name":"internal.func.end","type":"analysis.ip.InternalFuncExitAnnotation","erasureStrategy":"Canonical"},"value":{"id":5,"rets":[{"s":{"namePrefix":"R557","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1023}]},"offset":0}],"functionLayout":{"0":{"#class":"analysis.ip.InternalFuncValueLocation.Scalar"}}}}
		AnnotationCmd JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.EVMFunctionReturnWrite","returnbufOffset":"0","returnValueSym":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R557","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1023}]},"callIndex":6}}
		AnnotationCmd JSON{"key":{"name":"tac.return.path","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		LabelCmd "End procedure ERC20-balanceOf(address)"
		AssignExpCmd tacMCANON6!!559:13 Store(tacMCANON6!!535:13 0x100 R557:85 )
		AnnotationCmd JSON{"key":{"name":"call.trace.pop","type":"analysis.icfg.Inliner$CallStack$PopRecord","erasureStrategy":"Canonical"},"value":"rO0ABXNyAClhbmFseXNpcy5pY2ZnLklubGluZXIkQ2FsbFN0YWNrJFBvcFJlY29yZPAPfwSLdCWJAgABSQAIY2FsbGVlSWR4cAAAAAY="}
		JumpCmd 5_0_0_5_0_0
	}
	Block 6_0_0_0_0_0 Succ [0_0_0_7_0_0] {
		AnnotationCmd:154 JSON{"key":{"name":"call.trace.pop","type":"analysis.icfg.Inliner$CallStack$PopRecord","erasureStrategy":"Canonical"},"value":"rO0ABXNyAClhbmFseXNpcy5pY2ZnLklubGluZXIkQ2FsbFN0YWNrJFBvcFJlY29yZPAPfwSLdCWJAgABSQAIY2FsbGVlSWR4cAAAAAU="}
		AssumeNotCmd:154 false
		AssumeNotCmd:154 false
		AnnotationCmd JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageGlobalChangeSnippet.StorageTakeSnapshot","lhs":{"namePrefix":"lastStorage","tag":{"#class":"tac.Tag.BlockchainState"},"callIndex":0,"meta":[{"key":{"name":"cvl.local","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true},{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"lastStorage"},{"key":{"name":"cvl.type","type":"spec.cvlast.CVLType$PureCVLType","erasureStrategy":"CallTrace"},"value":{"#class":"spec.cvlast.CVLType.PureCVLType.VMInternal.BlockchainState"}},{"key":{"name":"cvl","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true},{"key":{"name":"cvl.display","type":"java.lang.String","erasureStrategy":"CallTrace"},"value":"lastStorage"}]}}}
		AnnotationCmd:154 JSON{"key":{"name":"cvl.label.end","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		AnnotationCmd:102 JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Cmd","cmd":{"cmd_type":"spec.cvlast.CVLCmd.Simple.AssumeCmd.Assume","cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/specs/ViewReentrancy.spec","start":{"line":28,"character":4},"end":{"line":28,"character":55}},"exp":{"#class":"spec.cvlast.CVLExp.RelopExp.EqExp","l":{"#class":"spec.cvlast.CVLExp.VariableExp","id":"after_func1","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":0}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256},"cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/specs/ViewReentrancy.spec","start":{"line":28,"character":4},"end":{"line":28,"character":55}}},"twoStateIndex":"NEITHER"},"r":{"#class":"spec.cvlast.CVLExp.ApplyExp.ContractFunction.Concrete","methodIdWithCallContext":{"#class":"spec.cvlast.ConcreteMethod","signature":{"#class":"spec.cvlast.ExternalQualifiedMethodSignature.ExternalQualifiedMethodSig","wrapped":{"#class":"spec.cvlast.QualifiedMethodSignature.QualifiedMethodSig","qualifiedMethodName":{"#class":"spec.cvlast.QualifiedFunction","host":{"name":"curve"},"methodId":"getVirtualPrice"},"params":[],"res":[{"#class":"spec.cvlast.VMParam.Unnamed","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256}}]},"sighashInt":{"n":"e25aa5fa"}}},"args":[{"#class":"spec.cvlast.CVLExp.VariableExp","id":"e_external","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":0}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"env","fields":[{"fieldName":"msg","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"msg","fields":[{"fieldName":"sender","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"value","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}}]}},{"fieldName":"tx","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"tx","fields":[{"fieldName":"origin","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}}]}},{"fieldName":"block","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"block","fields":[{"fieldName":"coinbase","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"difficulty","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"gaslimit","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"number","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"timestamp","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}}]}}]},"cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/specs/ViewReentrancy.spec","start":{"line":28,"character":4},"end":{"line":28,"character":55}}},"twoStateIndex":"NEITHER"}],"noRevert":true,"storage":{"#class":"spec.cvlast.CVLExp.VariableExp","id":"lastStorage","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":0}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.VMInternal.BlockchainState"},"cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/specs/ViewReentrancy.spec","start":{"line":28,"character":4},"end":{"line":28,"character":55}}},"twoStateIndex":"NEITHER"},"isWhole":false,"tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":0}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.VM","descriptor":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256},"context":{"#class":"spec.cvlast.typedescriptors.FromVMContext.ReturnValue"}},"cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/specs/ViewReentrancy.spec","start":{"line":28,"character":27},"end":{"line":28,"character":42}},"annotation":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.CallResolution$DirectPassing","target":{"methodSignature":{"#class":"spec.cvlast.ExternalQualifiedMethodSignature.ExternalQualifiedMethodSig","wrapped":{"#class":"spec.cvlast.QualifiedMethodSignature.QualifiedMethodSig","qualifiedMethodName":{"#class":"spec.cvlast.QualifiedFunction","host":{"name":"curve"},"methodId":"getVirtualPrice"},"params":[],"res":[{"#class":"spec.cvlast.VMParam.Unnamed","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256}}]},"sighashInt":{"n":"e25aa5fa"}},"definitelyNonPayable":true,"annotation":{"visibility":"EXTERNAL","envFree":false,"library":false},"stateMutability":"view","tag":{"#class":"spec.cvlast.CVLImportedFunctionTag.WithMethodInfo","evmMethodInfo":{"sigHash":"e25aa5fa","name":"getVirtualPrice","argTypes":[],"resultTypes":[{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256}],"stateMutability":"view","envfreeInfo":{"#class":"bridge.EnvfreeInfo.Unknown"},"isConstant":false,"isLibrary":false}}},"hasEnv":true}}},"tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":0}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"},"cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/specs/ViewReentrancy.spec","start":{"line":28,"character":12},"end":{"line":28,"character":54}}}},"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":0}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}}}}}
		NopCmd
		NopCmd
		NopCmd
		NopCmd
		NopCmd
	}
	Block 5_0_0_5_0_0 Succ [6_0_0_0_0_0] {
		AssumeNotCmd:169 false
		AnnotationCmd JSON{"key":{"name":"pta.fake-return.start","type":"analysis.CmdPointer","erasureStrategy":"Erased"},"value":{"block":{"#class":"tac.BlockIdentifier","origStartPc":1608,"stkTop":1014,"decompCopy":0,"calleeIdx":0,"topOfStackValue":2,"freshCopy":0},"pos":1}}
		AnnotationCmd JSON{"key":{"name":"pta.fake-return.end","type":"analysis.CmdPointer","erasureStrategy":"Erased"},"value":{"block":{"#class":"tac.BlockIdentifier","origStartPc":1608,"stkTop":1014,"decompCopy":0,"calleeIdx":0,"topOfStackValue":2,"freshCopy":0},"pos":6}}
		AssumeNotCmd:179 false
		AssignExpCmd:180 R566:73 Select(tacMCANON6!!559:13 0x100 )
		NopCmd
		AssumeExpCmd LNot(Lt(R566:73 R527:81 ) )
		AnnotationCmd JSON{"key":{"name":"pta.end-allocation","type":"analysis.alloc.AllocationAnalysis$AbstractLocation","erasureStrategy":"Erased"},"value":{"prevFPWriteIdx":3,"nextFPWriteCmd":{"block":{"#class":"tac.BlockIdentifier","origStartPc":4211,"stkTop":1012,"decompCopy":0,"calleeIdx":0,"topOfStackValue":0,"freshCopy":0},"pos":18},"sort":{"#class":"analysis.alloc.AllocationAnalysis.Alloc.ConstBlock","sz":"40"}}}
		AnnotationCmd JSON{"key":{"name":"dsa.assign.start","type":"java.lang.String","erasureStrategy":"Erased"},"value":"4639_1015_0_0_0_0 -> 4643_1013_0_0_0_0"}
		LabelCmd "Parallel assignment for R4180:bv256, R4231:bv256, B4232:bool, R4233:bv256 := R4254:bv256, R413:bv256, B4080:bool, R4081:bv256"
		AnnotationCmd JSON{"key":{"name":"dsa.assign.end","type":"java.lang.String","erasureStrategy":"Erased"},"value":"4639_1015_0_0_0_0 -> 4643_1013_0_0_0_0"}
		AnnotationCmd JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.LoopSnippet.StartLoopSnippet","loopIndex":2,"loopSource":"unknown loop source code"}}
		AnnotationCmd JSON{"key":{"name":"start_loop.cmd","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		AnnotationCmd JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.LoopSnippet.StartIter","iteration":1}}
		AnnotationCmd JSON{"key":{"name":"dsa.assign.start","type":"java.lang.String","erasureStrategy":"Erased"},"value":"4674_1011_0_0_0_0 -> 4643_1013_0_0_0_0"}
		LabelCmd "Parallel assignment for R4180:bv256, R4231:bv256, B4232:bool, R4233:bv256 := R3956:bv256, R4003:bv256, B4229:bool, R4226:bv256"
		AnnotationCmd JSON{"key":{"name":"dsa.assign.end","type":"java.lang.String","erasureStrategy":"Erased"},"value":"4674_1011_0_0_0_0 -> 4643_1013_0_0_0_0"}
		AnnotationCmd JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.LoopSnippet.EndIter","iteration":1}}
		AnnotationCmd JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.LoopSnippet.StartIter","iteration":2}}
		AnnotationCmd JSON{"key":{"name":"dsa.assign.start","type":"java.lang.String","erasureStrategy":"Erased"},"value":"4674_1011_0_0_0_0 -> 4643_1013_0_0_0_0"}
		LabelCmd "Parallel assignment for R4180:bv256, R4231:bv256, B4232:bool, R4233:bv256 := R3956:bv256, R4003:bv256, B4229:bool, R4226:bv256"
		AnnotationCmd JSON{"key":{"name":"dsa.assign.end","type":"java.lang.String","erasureStrategy":"Erased"},"value":"4674_1011_0_0_0_0 -> 4643_1013_0_0_0_0"}
		AnnotationCmd JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.LoopSnippet.EndIter","iteration":2}}
		AnnotationCmd JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.LoopSnippet.EndLoopSnippet","loopId":2}}
		AnnotationCmd JSON{"key":{"name":"end_loop.cmd","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		AnnotationCmd JSON{"key":{"name":"tac.return.path","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		LabelCmd "End procedure curve-_balances(uint256)"
		JumpCmd 6_0_0_0_0_0
	}
}
Axioms {
		CANON105
		CANON109
		CANON37
		CANON39
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
          "callIndex": 5,
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
  "2": [
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
          "callIndex": 7,
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
  "3": [
    {
      "key": {
        "name": "Tac.symbol.keyword",
        "type": "java.lang.String",
        "erasureStrategy": "Canonical"
      },
      "value": "tacCalldatasize"
    }
  ],
  "4": [
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
  "5": [
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
      "value": "data"
    }
  ],
  "6": [
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
      "value": "data"
    }
  ],
  "7": [
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
  "8": [
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
      "value": 8
    }
  ],
  "9": [
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
  "10": [
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
      "value": 9
    }
  ],
  "11": [
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
  "12": [
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
      "value": 10
    }
  ],
  "13": [
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
      "value": 6
    }
  ],
  "14": [
    {
      "key": {
        "name": "Tac.symbol.keyword",
        "type": "java.lang.String",
        "erasureStrategy": "Canonical"
      },
      "value": "tacBalance"
    }
  ],
  "15": [
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
  "16": [
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
  "17": [
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
          "callIndex": 7,
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
  "18": [
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
          "callIndex": 9,
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
  "19": [
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
      "value": "ce4604a0000000000000000000000028"
    }
  ],
  "20": [
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
      "value": "ce4604a0000000000000000000000028"
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
  "25": [
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
      "value": "e_external.msg.sender"
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
      "value": "e_external.msg.value"
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
      "value": "e_external.tx.origin"
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
      "value": "e_external.block.coinbase"
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
      "value": "e_external.block.difficulty"
    }
  ],
  "34": [
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
      "value": "e_external.block.gaslimit"
    }
  ],
  "35": [
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
      "value": "e_external.block.number"
    }
  ],
  "36": [
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
      "value": "e_external.block.timestamp"
    }
  ],
  "37": [
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
      "value": "ce4604a0000000000000000000000028"
    }
  ],
  "38": [
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
      "value": "ce4604a0000000000000000000000008"
    }
  ],
  "39": [
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
      "value": "ce4604a0000000000000000000000011"
    }
  ],
  "40": [
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
      "value": "ce4604a0000000000000000000000028"
    }
  ],
  "41": [
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
      "value": "ce4604a0000000000000000000000008"
    }
  ],
  "42": [
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
      "value": "ce4604a0000000000000000000000011"
    }
  ],
  "43": [
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
      "value": "curve"
    },
    {
      "key": {
        "name": "tac.contract.sym.addr",
        "type": "java.math.BigInteger",
        "erasureStrategy": "Erased"
      },
      "value": "ce4604a0000000000000000000000028"
    }
  ],
  "44": [
    {
      "key": {
        "name": "Tac.symbol.keyword",
        "type": "java.lang.String",
        "erasureStrategy": "Canonical"
      },
      "value": "tacSighash"
    }
  ],
  "45": [
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
  "46": [
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
  "47": [
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
  "48": [
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
  "49": [
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
  "50": [
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
  "51": [
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
        "name": "cvl.range",
        "type": "spec.cvlast.CVLRange",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "spec.cvlast.CVLRange.Range",
        "specFile": "certora/specs/ViewReentrancy.spec",
        "start": {
          "line": 25,
          "character": 4
        },
        "end": {
          "line": 25,
          "character": 17
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
        "specFile": "certora/specs/ViewReentrancy.spec",
        "start": {
          "line": 26,
          "character": 4
        },
        "end": {
          "line": 26,
          "character": 56
        }
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
  "55": [
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
  "56": [
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
  "57": [
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
  "58": [
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
  "59": [
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
        "specFile": "certora/specs/ViewReentrancy.spec",
        "start": {
          "line": 26,
          "character": 4
        },
        "end": {
          "line": 26,
          "character": 56
        }
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
      "value": "curve"
    },
    {
      "key": {
        "name": "tac.contract.sym.addr",
        "type": "java.math.BigInteger",
        "erasureStrategy": "Erased"
      },
      "value": "ce4604a0000000000000000000000028"
    }
  ],
  "61": [
    {
      "key": {
        "name": "cvl.range",
        "type": "spec.cvlast.CVLRange",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "spec.cvlast.CVLRange.Range",
        "specFile": "certora/specs/ViewReentrancy.spec",
        "start": {
          "line": 26,
          "character": 4
        },
        "end": {
          "line": 26,
          "character": 56
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
        "source": 7,
        "begin": 5879,
        "len": 17,
        "jumpType": "REGULAR",
        "address": "ce4604a0000000000000000000000028",
        "sourceContext": {
          "indexToFilepath": {
            "0": "contracts/Context.sol",
            "1": "contracts/CurveToken.sol",
            "2": "contracts/CurveTokenExample.sol",
            "3": "contracts/ERC20.sol",
            "4": "contracts/IERC20.sol",
            "5": "contracts/IERC20Metadata.sol",
            "6": "contracts/ReentrancyGuard.sol",
            "7": "contracts/curve.sol"
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
        "name": "cvl.range",
        "type": "spec.cvlast.CVLRange",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "spec.cvlast.CVLRange.Range",
        "specFile": "certora/specs/ViewReentrancy.spec",
        "start": {
          "line": 26,
          "character": 4
        },
        "end": {
          "line": 26,
          "character": 56
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
        "source": 7,
        "begin": 5855,
        "len": 21,
        "jumpType": "REGULAR",
        "address": "ce4604a0000000000000000000000028",
        "sourceContext": {
          "indexToFilepath": {
            "0": "contracts/Context.sol",
            "1": "contracts/CurveToken.sol",
            "2": "contracts/CurveTokenExample.sol",
            "3": "contracts/ERC20.sol",
            "4": "contracts/IERC20.sol",
            "5": "contracts/IERC20Metadata.sol",
            "6": "contracts/ReentrancyGuard.sol",
            "7": "contracts/curve.sol"
          },
          "sourceDir": ".post_autofinders.2"
        }
      }
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
      "value": 1011
    }
  ],
  "65": [
    {
      "key": {
        "name": "cvl.range",
        "type": "spec.cvlast.CVLRange",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "spec.cvlast.CVLRange.Range",
        "specFile": "certora/specs/ViewReentrancy.spec",
        "start": {
          "line": 26,
          "character": 4
        },
        "end": {
          "line": 26,
          "character": 56
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
      "value": 1009
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
        "specFile": "certora/specs/ViewReentrancy.spec",
        "start": {
          "line": 26,
          "character": 4
        },
        "end": {
          "line": 26,
          "character": 56
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
        "source": 7,
        "begin": 5834,
        "len": 145,
        "jumpType": "REGULAR",
        "address": "ce4604a0000000000000000000000028",
        "sourceContext": {
          "indexToFilepath": {
            "0": "contracts/Context.sol",
            "1": "contracts/CurveToken.sol",
            "2": "contracts/CurveTokenExample.sol",
            "3": "contracts/ERC20.sol",
            "4": "contracts/IERC20.sol",
            "5": "contracts/IERC20Metadata.sol",
            "6": "contracts/ReentrancyGuard.sol",
            "7": "contracts/curve.sol"
          },
          "sourceDir": ".post_autofinders.2"
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
        "specFile": "certora/specs/ViewReentrancy.spec",
        "start": {
          "line": 26,
          "character": 4
        },
        "end": {
          "line": 26,
          "character": 56
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
        "source": 7,
        "begin": 5961,
        "len": 17,
        "jumpType": "REGULAR",
        "address": "ce4604a0000000000000000000000028",
        "sourceContext": {
          "indexToFilepath": {
            "0": "contracts/Context.sol",
            "1": "contracts/CurveToken.sol",
            "2": "contracts/CurveTokenExample.sol",
            "3": "contracts/ERC20.sol",
            "4": "contracts/IERC20.sol",
            "5": "contracts/IERC20Metadata.sol",
            "6": "contracts/ReentrancyGuard.sol",
            "7": "contracts/curve.sol"
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
      "value": 1013
    }
  ],
  "70": [
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
      "value": "ce4604a0000000000000000000000028"
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
  "71": [
    {
      "key": {
        "name": "cvl.range",
        "type": "spec.cvlast.CVLRange",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "spec.cvlast.CVLRange.Range",
        "specFile": "certora/specs/ViewReentrancy.spec",
        "start": {
          "line": 26,
          "character": 4
        },
        "end": {
          "line": 26,
          "character": 56
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
        "source": 7,
        "begin": 5919,
        "len": 39,
        "jumpType": "REGULAR",
        "address": "ce4604a0000000000000000000000028",
        "sourceContext": {
          "indexToFilepath": {
            "0": "contracts/Context.sol",
            "1": "contracts/CurveToken.sol",
            "2": "contracts/CurveTokenExample.sol",
            "3": "contracts/ERC20.sol",
            "4": "contracts/IERC20.sol",
            "5": "contracts/IERC20Metadata.sol",
            "6": "contracts/ReentrancyGuard.sol",
            "7": "contracts/curve.sol"
          },
          "sourceDir": ".post_autofinders.2"
        }
      }
    }
  ],
  "72": [
    {
      "key": {
        "name": "cvl.range",
        "type": "spec.cvlast.CVLRange",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "spec.cvlast.CVLRange.Range",
        "specFile": "certora/specs/ViewReentrancy.spec",
        "start": {
          "line": 26,
          "character": 4
        },
        "end": {
          "line": 26,
          "character": 56
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
        "source": 8,
        "begin": 6816,
        "len": 37,
        "jumpType": "REGULAR",
        "address": "ce4604a0000000000000000000000028",
        "sourceContext": {
          "indexToFilepath": {
            "0": "contracts/Context.sol",
            "1": "contracts/CurveToken.sol",
            "2": "contracts/CurveTokenExample.sol",
            "3": "contracts/ERC20.sol",
            "4": "contracts/IERC20.sol",
            "5": "contracts/IERC20Metadata.sol",
            "6": "contracts/ReentrancyGuard.sol",
            "7": "contracts/curve.sol"
          },
          "sourceDir": ".post_autofinders.2"
        }
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
      "value": 1008
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
      "value": 1004
    }
  ],
  "75": [
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
  "76": [
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
  "77": [
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
      "value": "tacContractAt"
    },
    {
      "key": {
        "name": "tac.contract.sym.addr.name",
        "type": "java.lang.String",
        "erasureStrategy": "Erased"
      },
      "value": "curve"
    },
    {
      "key": {
        "name": "tac.contract.sym.addr",
        "type": "java.math.BigInteger",
        "erasureStrategy": "Erased"
      },
      "value": "ce4604a0000000000000000000000028"
    }
  ],
  "78": [
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
      "value": "ce4604a0000000000000000000000011"
    }
  ],
  "79": [
    {
      "key": {
        "name": "cvl.range",
        "type": "spec.cvlast.CVLRange",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "spec.cvlast.CVLRange.Range",
        "specFile": "certora/specs/ViewReentrancy.spec",
        "start": {
          "line": 26,
          "character": 4
        },
        "end": {
          "line": 26,
          "character": 56
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
        "source": 4,
        "begin": 4984,
        "len": 23,
        "jumpType": "REGULAR",
        "address": "ce4604a0000000000000000000000011",
        "sourceContext": {
          "indexToFilepath": {
            "0": "contracts/Context.sol",
            "1": "contracts/ERC20.sol",
            "2": "contracts/IERC20.sol",
            "3": "contracts/IERC20Metadata.sol"
          },
          "sourceDir": ".post_autofinders.1"
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
      "value": 1017
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
        "name": "cvl.range",
        "type": "spec.cvlast.CVLRange",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "spec.cvlast.CVLRange.Range",
        "specFile": "certora/specs/ViewReentrancy.spec",
        "start": {
          "line": 26,
          "character": 4
        },
        "end": {
          "line": 26,
          "character": 56
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
        "source": 4,
        "begin": 2157,
        "len": 20,
        "jumpType": "REGULAR",
        "address": "ce4604a0000000000000000000000011",
        "sourceContext": {
          "indexToFilepath": {
            "0": "contracts/Context.sol",
            "1": "contracts/ERC20.sol",
            "2": "contracts/IERC20.sol",
            "3": "contracts/IERC20Metadata.sol"
          },
          "sourceDir": ".post_autofinders.1"
        }
      }
    }
  ],
  "83": [
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
  "84": [
    {
      "key": {
        "name": "cvl.range",
        "type": "spec.cvlast.CVLRange",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "spec.cvlast.CVLRange.Range",
        "specFile": "certora/specs/ViewReentrancy.spec",
        "start": {
          "line": 26,
          "character": 4
        },
        "end": {
          "line": 26,
          "character": 56
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
        "source": 1,
        "begin": 4818,
        "len": 18,
        "jumpType": "REGULAR",
        "address": "ce4604a0000000000000000000000011",
        "sourceContext": {
          "indexToFilepath": {
            "0": "contracts/Context.sol",
            "1": "contracts/ERC20.sol",
            "2": "contracts/IERC20.sol",
            "3": "contracts/IERC20Metadata.sol"
          },
          "sourceDir": ".post_autofinders.1"
        }
      }
    }
  ],
  "85": [
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
  "86": [
    {
      "key": {
        "name": "cvl.range",
        "type": "spec.cvlast.CVLRange",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "spec.cvlast.CVLRange.Range",
        "specFile": "certora/specs/ViewReentrancy.spec",
        "start": {
          "line": 26,
          "character": 4
        },
        "end": {
          "line": 26,
          "character": 56
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
        "source": 1,
        "begin": 4818,
        "len": 18,
        "jumpType": "REGULAR",
        "address": "ce4604a0000000000000000000000011",
        "sourceContext": {
          "indexToFilepath": {
            "0": "contracts/Context.sol",
            "1": "contracts/ERC20.sol",
            "2": "contracts/IERC20.sol",
            "3": "contracts/IERC20Metadata.sol"
          },
          "sourceDir": ".post_autofinders.1"
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
                    "value": 1018
                  }
                ]
              },
              "baseSlot": {
                "#class": "vc.data.TACSymbol.Var.Full",
                "namePrefix": "CANON114",
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
                "namePrefix": "CANON113",
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
  "88": [
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
  "89": [
    {
      "key": {
        "name": "cvl.range",
        "type": "spec.cvlast.CVLRange",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "spec.cvlast.CVLRange.Range",
        "specFile": "certora/specs/ViewReentrancy.spec",
        "start": {
          "line": 26,
          "character": 4
        },
        "end": {
          "line": 26,
          "character": 56
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
        "source": 8,
        "begin": 3060,
        "len": 23,
        "jumpType": "REGULAR",
        "address": "ce4604a0000000000000000000000028",
        "sourceContext": {
          "indexToFilepath": {
            "0": "contracts/Context.sol",
            "1": "contracts/CurveToken.sol",
            "2": "contracts/CurveTokenExample.sol",
            "3": "contracts/ERC20.sol",
            "4": "contracts/IERC20.sol",
            "5": "contracts/IERC20Metadata.sol",
            "6": "contracts/ReentrancyGuard.sol",
            "7": "contracts/curve.sol"
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
      "value": 1016
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
        "name": "tac.stack.height",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 1021
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
        "specFile": "certora/specs/ViewReentrancy.spec",
        "start": {
          "line": 26,
          "character": 4
        },
        "end": {
          "line": 26,
          "character": 56
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
        "source": 8,
        "begin": 67,
        "len": 9,
        "jumpType": "REGULAR",
        "address": "ce4604a0000000000000000000000028",
        "sourceContext": {
          "indexToFilepath": {
            "0": "contracts/Context.sol",
            "1": "contracts/CurveToken.sol",
            "2": "contracts/CurveTokenExample.sol",
            "3": "contracts/ERC20.sol",
            "4": "contracts/IERC20.sol",
            "5": "contracts/IERC20Metadata.sol",
            "6": "contracts/ReentrancyGuard.sol",
            "7": "contracts/curve.sol"
          },
          "sourceDir": ".post_autofinders.2"
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
      "value": 1001
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
        "specFile": "certora/specs/ViewReentrancy.spec",
        "start": {
          "line": 26,
          "character": 4
        },
        "end": {
          "line": 26,
          "character": 56
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
        "source": 8,
        "begin": 907,
        "len": 88,
        "jumpType": "REGULAR",
        "address": "ce4604a0000000000000000000000028",
        "sourceContext": {
          "indexToFilepath": {
            "0": "contracts/Context.sol",
            "1": "contracts/CurveToken.sol",
            "2": "contracts/CurveTokenExample.sol",
            "3": "contracts/ERC20.sol",
            "4": "contracts/IERC20.sol",
            "5": "contracts/IERC20Metadata.sol",
            "6": "contracts/ReentrancyGuard.sol",
            "7": "contracts/curve.sol"
          },
          "sourceDir": ".post_autofinders.2"
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
          "namePrefix": "LCANON58",
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
  "95": [
    {
      "key": {
        "name": "cvl.range",
        "type": "spec.cvlast.CVLRange",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "spec.cvlast.CVLRange.Range",
        "specFile": "certora/specs/ViewReentrancy.spec",
        "start": {
          "line": 26,
          "character": 4
        },
        "end": {
          "line": 26,
          "character": 56
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
        "source": 8,
        "begin": 1833,
        "len": 20,
        "jumpType": "REGULAR",
        "address": "ce4604a0000000000000000000000028",
        "sourceContext": {
          "indexToFilepath": {
            "0": "contracts/Context.sol",
            "1": "contracts/CurveToken.sol",
            "2": "contracts/CurveTokenExample.sol",
            "3": "contracts/ERC20.sol",
            "4": "contracts/IERC20.sol",
            "5": "contracts/IERC20Metadata.sol",
            "6": "contracts/ReentrancyGuard.sol",
            "7": "contracts/curve.sol"
          },
          "sourceDir": ".post_autofinders.2"
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
      "value": 998
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
        "specFile": "certora/specs/ViewReentrancy.spec",
        "start": {
          "line": 26,
          "character": 4
        },
        "end": {
          "line": 26,
          "character": 56
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
        "source": 8,
        "begin": 2468,
        "len": 50,
        "jumpType": "REGULAR",
        "address": "ce4604a0000000000000000000000028",
        "sourceContext": {
          "indexToFilepath": {
            "0": "contracts/Context.sol",
            "1": "contracts/CurveToken.sol",
            "2": "contracts/CurveTokenExample.sol",
            "3": "contracts/ERC20.sol",
            "4": "contracts/IERC20.sol",
            "5": "contracts/IERC20Metadata.sol",
            "6": "contracts/ReentrancyGuard.sol",
            "7": "contracts/curve.sol"
          },
          "sourceDir": ".post_autofinders.2"
        }
      }
    }
  ],
  "98": [
    {
      "key": {
        "name": "cvl.range",
        "type": "spec.cvlast.CVLRange",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "spec.cvlast.CVLRange.Range",
        "specFile": "certora/specs/ViewReentrancy.spec",
        "start": {
          "line": 26,
          "character": 4
        },
        "end": {
          "line": 26,
          "character": 56
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
        "source": 7,
        "begin": 3683,
        "len": 5,
        "jumpType": "REGULAR",
        "address": "ce4604a0000000000000000000000028",
        "sourceContext": {
          "indexToFilepath": {
            "0": "contracts/Context.sol",
            "1": "contracts/CurveToken.sol",
            "2": "contracts/CurveTokenExample.sol",
            "3": "contracts/ERC20.sol",
            "4": "contracts/IERC20.sol",
            "5": "contracts/IERC20Metadata.sol",
            "6": "contracts/ReentrancyGuard.sol",
            "7": "contracts/curve.sol"
          },
          "sourceDir": ".post_autofinders.2"
        }
      }
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
        "specFile": "certora/specs/ViewReentrancy.spec",
        "start": {
          "line": 26,
          "character": 4
        },
        "end": {
          "line": 26,
          "character": 56
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
        "source": 7,
        "begin": 3675,
        "len": 5,
        "jumpType": "REGULAR",
        "address": "ce4604a0000000000000000000000028",
        "sourceContext": {
          "indexToFilepath": {
            "0": "contracts/Context.sol",
            "1": "contracts/CurveToken.sol",
            "2": "contracts/CurveTokenExample.sol",
            "3": "contracts/ERC20.sol",
            "4": "contracts/IERC20.sol",
            "5": "contracts/IERC20Metadata.sol",
            "6": "contracts/ReentrancyGuard.sol",
            "7": "contracts/curve.sol"
          },
          "sourceDir": ".post_autofinders.2"
        }
      }
    }
  ],
  "100": [
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
      "value": "ce4604a0000000000000000000000008"
    }
  ],
  "101": [
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
      "value": "ce4604a0000000000000000000000008"
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
        "specFile": "certora/specs/ViewReentrancy.spec",
        "start": {
          "line": 28,
          "character": 4
        },
        "end": {
          "line": 28,
          "character": 55
        }
      }
    }
  ],
  "103": [
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
        "specFile": "certora/specs/ViewReentrancy.spec",
        "start": {
          "line": 28,
          "character": 4
        },
        "end": {
          "line": 28,
          "character": 55
        }
      }
    }
  ],
  "104": [
    {
      "key": {
        "name": "cvl.range",
        "type": "spec.cvlast.CVLRange",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "spec.cvlast.CVLRange.Range",
        "specFile": "certora/specs/ViewReentrancy.spec",
        "start": {
          "line": 28,
          "character": 4
        },
        "end": {
          "line": 28,
          "character": 55
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
        "source": 7,
        "begin": 5879,
        "len": 17,
        "jumpType": "REGULAR",
        "address": "ce4604a0000000000000000000000028",
        "sourceContext": {
          "indexToFilepath": {
            "0": "contracts/Context.sol",
            "1": "contracts/CurveToken.sol",
            "2": "contracts/CurveTokenExample.sol",
            "3": "contracts/ERC20.sol",
            "4": "contracts/IERC20.sol",
            "5": "contracts/IERC20Metadata.sol",
            "6": "contracts/ReentrancyGuard.sol",
            "7": "contracts/curve.sol"
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
  "105": [
    {
      "key": {
        "name": "cvl.range",
        "type": "spec.cvlast.CVLRange",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "spec.cvlast.CVLRange.Range",
        "specFile": "certora/specs/ViewReentrancy.spec",
        "start": {
          "line": 28,
          "character": 4
        },
        "end": {
          "line": 28,
          "character": 55
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
        "source": 7,
        "begin": 5855,
        "len": 21,
        "jumpType": "REGULAR",
        "address": "ce4604a0000000000000000000000028",
        "sourceContext": {
          "indexToFilepath": {
            "0": "contracts/Context.sol",
            "1": "contracts/CurveToken.sol",
            "2": "contracts/CurveTokenExample.sol",
            "3": "contracts/ERC20.sol",
            "4": "contracts/IERC20.sol",
            "5": "contracts/IERC20Metadata.sol",
            "6": "contracts/ReentrancyGuard.sol",
            "7": "contracts/curve.sol"
          },
          "sourceDir": ".post_autofinders.2"
        }
      }
    }
  ],
  "106": [
    {
      "key": {
        "name": "cvl.range",
        "type": "spec.cvlast.CVLRange",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "spec.cvlast.CVLRange.Range",
        "specFile": "certora/specs/ViewReentrancy.spec",
        "start": {
          "line": 28,
          "character": 4
        },
        "end": {
          "line": 28,
          "character": 55
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
  "107": [
    {
      "key": {
        "name": "cvl.range",
        "type": "spec.cvlast.CVLRange",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "spec.cvlast.CVLRange.Range",
        "specFile": "certora/specs/ViewReentrancy.spec",
        "start": {
          "line": 28,
          "character": 4
        },
        "end": {
          "line": 28,
          "character": 55
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
        "source": 7,
        "begin": 5834,
        "len": 145,
        "jumpType": "REGULAR",
        "address": "ce4604a0000000000000000000000028",
        "sourceContext": {
          "indexToFilepath": {
            "0": "contracts/Context.sol",
            "1": "contracts/CurveToken.sol",
            "2": "contracts/CurveTokenExample.sol",
            "3": "contracts/ERC20.sol",
            "4": "contracts/IERC20.sol",
            "5": "contracts/IERC20Metadata.sol",
            "6": "contracts/ReentrancyGuard.sol",
            "7": "contracts/curve.sol"
          },
          "sourceDir": ".post_autofinders.2"
        }
      }
    }
  ],
  "108": [
    {
      "key": {
        "name": "cvl.range",
        "type": "spec.cvlast.CVLRange",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "spec.cvlast.CVLRange.Range",
        "specFile": "certora/specs/ViewReentrancy.spec",
        "start": {
          "line": 28,
          "character": 4
        },
        "end": {
          "line": 28,
          "character": 55
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
        "source": 7,
        "begin": 5961,
        "len": 17,
        "jumpType": "REGULAR",
        "address": "ce4604a0000000000000000000000028",
        "sourceContext": {
          "indexToFilepath": {
            "0": "contracts/Context.sol",
            "1": "contracts/CurveToken.sol",
            "2": "contracts/CurveTokenExample.sol",
            "3": "contracts/ERC20.sol",
            "4": "contracts/IERC20.sol",
            "5": "contracts/IERC20Metadata.sol",
            "6": "contracts/ReentrancyGuard.sol",
            "7": "contracts/curve.sol"
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
  "109": [
    {
      "key": {
        "name": "cvl.range",
        "type": "spec.cvlast.CVLRange",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "spec.cvlast.CVLRange.Range",
        "specFile": "certora/specs/ViewReentrancy.spec",
        "start": {
          "line": 28,
          "character": 4
        },
        "end": {
          "line": 28,
          "character": 55
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
        "source": 7,
        "begin": 5919,
        "len": 39,
        "jumpType": "REGULAR",
        "address": "ce4604a0000000000000000000000028",
        "sourceContext": {
          "indexToFilepath": {
            "0": "contracts/Context.sol",
            "1": "contracts/CurveToken.sol",
            "2": "contracts/CurveTokenExample.sol",
            "3": "contracts/ERC20.sol",
            "4": "contracts/IERC20.sol",
            "5": "contracts/IERC20Metadata.sol",
            "6": "contracts/ReentrancyGuard.sol",
            "7": "contracts/curve.sol"
          },
          "sourceDir": ".post_autofinders.2"
        }
      }
    }
  ],
  "110": [
    {
      "key": {
        "name": "cvl.range",
        "type": "spec.cvlast.CVLRange",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "spec.cvlast.CVLRange.Range",
        "specFile": "certora/specs/ViewReentrancy.spec",
        "start": {
          "line": 28,
          "character": 4
        },
        "end": {
          "line": 28,
          "character": 55
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
        "source": 8,
        "begin": 6816,
        "len": 37,
        "jumpType": "REGULAR",
        "address": "ce4604a0000000000000000000000028",
        "sourceContext": {
          "indexToFilepath": {
            "0": "contracts/Context.sol",
            "1": "contracts/CurveToken.sol",
            "2": "contracts/CurveTokenExample.sol",
            "3": "contracts/ERC20.sol",
            "4": "contracts/IERC20.sol",
            "5": "contracts/IERC20Metadata.sol",
            "6": "contracts/ReentrancyGuard.sol",
            "7": "contracts/curve.sol"
          },
          "sourceDir": ".post_autofinders.2"
        }
      }
    }
  ],
  "111": [
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
          "callIndex": 7,
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
  "112": [
    {
      "key": {
        "name": "cvl.range",
        "type": "spec.cvlast.CVLRange",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "spec.cvlast.CVLRange.Range",
        "specFile": "certora/specs/ViewReentrancy.spec",
        "start": {
          "line": 28,
          "character": 4
        },
        "end": {
          "line": 28,
          "character": 55
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
        "source": 4,
        "begin": 4984,
        "len": 23,
        "jumpType": "REGULAR",
        "address": "ce4604a0000000000000000000000011",
        "sourceContext": {
          "indexToFilepath": {
            "0": "contracts/Context.sol",
            "1": "contracts/ERC20.sol",
            "2": "contracts/IERC20.sol",
            "3": "contracts/IERC20Metadata.sol"
          },
          "sourceDir": ".post_autofinders.1"
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
  "113": [
    {
      "key": {
        "name": "cvl.range",
        "type": "spec.cvlast.CVLRange",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "spec.cvlast.CVLRange.Range",
        "specFile": "certora/specs/ViewReentrancy.spec",
        "start": {
          "line": 28,
          "character": 4
        },
        "end": {
          "line": 28,
          "character": 55
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
        "source": 4,
        "begin": 2157,
        "len": 20,
        "jumpType": "REGULAR",
        "address": "ce4604a0000000000000000000000011",
        "sourceContext": {
          "indexToFilepath": {
            "0": "contracts/Context.sol",
            "1": "contracts/ERC20.sol",
            "2": "contracts/IERC20.sol",
            "3": "contracts/IERC20Metadata.sol"
          },
          "sourceDir": ".post_autofinders.1"
        }
      }
    }
  ],
  "114": [
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
          "callIndex": 8,
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
  "115": [
    {
      "key": {
        "name": "cvl.range",
        "type": "spec.cvlast.CVLRange",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "spec.cvlast.CVLRange.Range",
        "specFile": "certora/specs/ViewReentrancy.spec",
        "start": {
          "line": 28,
          "character": 4
        },
        "end": {
          "line": 28,
          "character": 55
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
        "source": 1,
        "begin": 4818,
        "len": 18,
        "jumpType": "REGULAR",
        "address": "ce4604a0000000000000000000000011",
        "sourceContext": {
          "indexToFilepath": {
            "0": "contracts/Context.sol",
            "1": "contracts/ERC20.sol",
            "2": "contracts/IERC20.sol",
            "3": "contracts/IERC20Metadata.sol"
          },
          "sourceDir": ".post_autofinders.1"
        }
      }
    }
  ],
  "116": [
    {
      "key": {
        "name": "cvl.range",
        "type": "spec.cvlast.CVLRange",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "spec.cvlast.CVLRange.Range",
        "specFile": "certora/specs/ViewReentrancy.spec",
        "start": {
          "line": 28,
          "character": 4
        },
        "end": {
          "line": 28,
          "character": 55
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
        "source": 1,
        "begin": 4818,
        "len": 18,
        "jumpType": "REGULAR",
        "address": "ce4604a0000000000000000000000011",
        "sourceContext": {
          "indexToFilepath": {
            "0": "contracts/Context.sol",
            "1": "contracts/ERC20.sol",
            "2": "contracts/IERC20.sol",
            "3": "contracts/IERC20Metadata.sol"
          },
          "sourceDir": ".post_autofinders.1"
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
      "value": "rO0ABXNyADJhbmFseXNpcy5pY2ZnLkNhbGxHcmFwaEJ1aWxkZXIkQ29udHJhY3RTdG9yYWdlUmVhZLRpTKYiS4EFAgABSQACaWR4cAAAAAg="
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
  "117": [
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
              "namePrefix": "R312",
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
                "namePrefix": "R312",
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
                "namePrefix": "CANON114",
                "tag": {
                  "#class": "tac.Tag.Bit256"
                },
                "callIndex": 8,
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
                "namePrefix": "CANON113",
                "tag": {
                  "#class": "tac.Tag.Bit256"
                },
                "callIndex": 8,
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
  "118": [
    {
      "key": {
        "name": "tac.immutable.array",
        "type": "vc.data.ImmutableBound",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "sym": {
          "#class": "vc.data.TACSymbol.Var.Full",
          "namePrefix": "tacCalldatasize!!5",
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
  "119": [
    {
      "key": {
        "name": "cvl.range",
        "type": "spec.cvlast.CVLRange",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "spec.cvlast.CVLRange.Range",
        "specFile": "certora/specs/ViewReentrancy.spec",
        "start": {
          "line": 28,
          "character": 4
        },
        "end": {
          "line": 28,
          "character": 55
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
        "source": 8,
        "begin": 3060,
        "len": 23,
        "jumpType": "REGULAR",
        "address": "ce4604a0000000000000000000000028",
        "sourceContext": {
          "indexToFilepath": {
            "0": "contracts/Context.sol",
            "1": "contracts/CurveToken.sol",
            "2": "contracts/CurveTokenExample.sol",
            "3": "contracts/ERC20.sol",
            "4": "contracts/IERC20.sol",
            "5": "contracts/IERC20Metadata.sol",
            "6": "contracts/ReentrancyGuard.sol",
            "7": "contracts/curve.sol"
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
  "120": [
    {
      "key": {
        "name": "cvl.range",
        "type": "spec.cvlast.CVLRange",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "spec.cvlast.CVLRange.Range",
        "specFile": "certora/specs/ViewReentrancy.spec",
        "start": {
          "line": 28,
          "character": 4
        },
        "end": {
          "line": 28,
          "character": 55
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
        "source": 8,
        "begin": 67,
        "len": 9,
        "jumpType": "REGULAR",
        "address": "ce4604a0000000000000000000000028",
        "sourceContext": {
          "indexToFilepath": {
            "0": "contracts/Context.sol",
            "1": "contracts/CurveToken.sol",
            "2": "contracts/CurveTokenExample.sol",
            "3": "contracts/ERC20.sol",
            "4": "contracts/IERC20.sol",
            "5": "contracts/IERC20Metadata.sol",
            "6": "contracts/ReentrancyGuard.sol",
            "7": "contracts/curve.sol"
          },
          "sourceDir": ".post_autofinders.2"
        }
      }
    }
  ],
  "121": [
    {
      "key": {
        "name": "cvl.range",
        "type": "spec.cvlast.CVLRange",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "spec.cvlast.CVLRange.Range",
        "specFile": "certora/specs/ViewReentrancy.spec",
        "start": {
          "line": 28,
          "character": 4
        },
        "end": {
          "line": 28,
          "character": 55
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
        "source": 8,
        "begin": 907,
        "len": 88,
        "jumpType": "REGULAR",
        "address": "ce4604a0000000000000000000000028",
        "sourceContext": {
          "indexToFilepath": {
            "0": "contracts/Context.sol",
            "1": "contracts/CurveToken.sol",
            "2": "contracts/CurveTokenExample.sol",
            "3": "contracts/ERC20.sol",
            "4": "contracts/IERC20.sol",
            "5": "contracts/IERC20Metadata.sol",
            "6": "contracts/ReentrancyGuard.sol",
            "7": "contracts/curve.sol"
          },
          "sourceDir": ".post_autofinders.2"
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
          "namePrefix": "LCANON58",
          "tag": {
            "#class": "tac.Tag.Bool"
          },
          "callIndex": 9,
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
  "122": [
    {
      "key": {
        "name": "cvl.range",
        "type": "spec.cvlast.CVLRange",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "spec.cvlast.CVLRange.Range",
        "specFile": "certora/specs/ViewReentrancy.spec",
        "start": {
          "line": 28,
          "character": 4
        },
        "end": {
          "line": 28,
          "character": 55
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
        "source": 8,
        "begin": 1833,
        "len": 20,
        "jumpType": "REGULAR",
        "address": "ce4604a0000000000000000000000028",
        "sourceContext": {
          "indexToFilepath": {
            "0": "contracts/Context.sol",
            "1": "contracts/CurveToken.sol",
            "2": "contracts/CurveTokenExample.sol",
            "3": "contracts/ERC20.sol",
            "4": "contracts/IERC20.sol",
            "5": "contracts/IERC20Metadata.sol",
            "6": "contracts/ReentrancyGuard.sol",
            "7": "contracts/curve.sol"
          },
          "sourceDir": ".post_autofinders.2"
        }
      }
    }
  ],
  "123": [
    {
      "key": {
        "name": "cvl.range",
        "type": "spec.cvlast.CVLRange",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "spec.cvlast.CVLRange.Range",
        "specFile": "certora/specs/ViewReentrancy.spec",
        "start": {
          "line": 28,
          "character": 4
        },
        "end": {
          "line": 28,
          "character": 55
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
        "source": 8,
        "begin": 2468,
        "len": 50,
        "jumpType": "REGULAR",
        "address": "ce4604a0000000000000000000000028",
        "sourceContext": {
          "indexToFilepath": {
            "0": "contracts/Context.sol",
            "1": "contracts/CurveToken.sol",
            "2": "contracts/CurveTokenExample.sol",
            "3": "contracts/ERC20.sol",
            "4": "contracts/IERC20.sol",
            "5": "contracts/IERC20Metadata.sol",
            "6": "contracts/ReentrancyGuard.sol",
            "7": "contracts/curve.sol"
          },
          "sourceDir": ".post_autofinders.2"
        }
      }
    }
  ],
  "124": [
    {
      "key": {
        "name": "cvl.range",
        "type": "spec.cvlast.CVLRange",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "spec.cvlast.CVLRange.Range",
        "specFile": "certora/specs/ViewReentrancy.spec",
        "start": {
          "line": 28,
          "character": 4
        },
        "end": {
          "line": 28,
          "character": 55
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
        "source": 7,
        "begin": 3683,
        "len": 5,
        "jumpType": "REGULAR",
        "address": "ce4604a0000000000000000000000028",
        "sourceContext": {
          "indexToFilepath": {
            "0": "contracts/Context.sol",
            "1": "contracts/CurveToken.sol",
            "2": "contracts/CurveTokenExample.sol",
            "3": "contracts/ERC20.sol",
            "4": "contracts/IERC20.sol",
            "5": "contracts/IERC20Metadata.sol",
            "6": "contracts/ReentrancyGuard.sol",
            "7": "contracts/curve.sol"
          },
          "sourceDir": ".post_autofinders.2"
        }
      }
    }
  ],
  "125": [
    {
      "key": {
        "name": "cvl.range",
        "type": "spec.cvlast.CVLRange",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "spec.cvlast.CVLRange.Range",
        "specFile": "certora/specs/ViewReentrancy.spec",
        "start": {
          "line": 28,
          "character": 4
        },
        "end": {
          "line": 28,
          "character": 55
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
        "source": 7,
        "begin": 3675,
        "len": 5,
        "jumpType": "REGULAR",
        "address": "ce4604a0000000000000000000000028",
        "sourceContext": {
          "indexToFilepath": {
            "0": "contracts/Context.sol",
            "1": "contracts/CurveToken.sol",
            "2": "contracts/CurveTokenExample.sol",
            "3": "contracts/ERC20.sol",
            "4": "contracts/IERC20.sol",
            "5": "contracts/IERC20Metadata.sol",
            "6": "contracts/ReentrancyGuard.sol",
            "7": "contracts/curve.sol"
          },
          "sourceDir": ".post_autofinders.2"
        }
      }
    }
  ],
  "126": [
    {
      "key": {
        "name": "cvl.range",
        "type": "spec.cvlast.CVLRange",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "spec.cvlast.CVLRange.Range",
        "specFile": "certora/specs/ViewReentrancy.spec",
        "start": {
          "line": 26,
          "character": 4
        },
        "end": {
          "line": 26,
          "character": 56
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
        "source": 8,
        "begin": 9679,
        "len": 119,
        "jumpType": "REGULAR",
        "address": "ce4604a0000000000000000000000028",
        "sourceContext": {
          "indexToFilepath": {
            "0": "contracts/Context.sol",
            "1": "contracts/CurveToken.sol",
            "2": "contracts/CurveTokenExample.sol",
            "3": "contracts/ERC20.sol",
            "4": "contracts/IERC20.sol",
            "5": "contracts/IERC20Metadata.sol",
            "6": "contracts/ReentrancyGuard.sol",
            "7": "contracts/curve.sol"
          },
          "sourceDir": ".post_autofinders.2"
        }
      }
    }
  ],
  "127": [
    {
      "key": {
        "name": "cvl.range",
        "type": "spec.cvlast.CVLRange",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "spec.cvlast.CVLRange.Range",
        "specFile": "certora/specs/ViewReentrancy.spec",
        "start": {
          "line": 26,
          "character": 4
        },
        "end": {
          "line": 26,
          "character": 56
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
        "source": 8,
        "begin": 9525,
        "len": 13,
        "jumpType": "REGULAR",
        "address": "ce4604a0000000000000000000000028",
        "sourceContext": {
          "indexToFilepath": {
            "0": "contracts/Context.sol",
            "1": "contracts/CurveToken.sol",
            "2": "contracts/CurveTokenExample.sol",
            "3": "contracts/ERC20.sol",
            "4": "contracts/IERC20.sol",
            "5": "contracts/IERC20Metadata.sol",
            "6": "contracts/ReentrancyGuard.sol",
            "7": "contracts/curve.sol"
          },
          "sourceDir": ".post_autofinders.2"
        }
      }
    }
  ],
  "128": [
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
      "value": 1003
    }
  ],
  "129": [
    {
      "key": {
        "name": "cvl.range",
        "type": "spec.cvlast.CVLRange",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "spec.cvlast.CVLRange.Range",
        "specFile": "certora/specs/ViewReentrancy.spec",
        "start": {
          "line": 26,
          "character": 4
        },
        "end": {
          "line": 26,
          "character": 56
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
        "source": 8,
        "begin": 9422,
        "len": 9,
        "jumpType": "REGULAR",
        "address": "ce4604a0000000000000000000000028",
        "sourceContext": {
          "indexToFilepath": {
            "0": "contracts/Context.sol",
            "1": "contracts/CurveToken.sol",
            "2": "contracts/CurveTokenExample.sol",
            "3": "contracts/ERC20.sol",
            "4": "contracts/IERC20.sol",
            "5": "contracts/IERC20Metadata.sol",
            "6": "contracts/ReentrancyGuard.sol",
            "7": "contracts/curve.sol"
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
  "130": [
    {
      "key": {
        "name": "cvl.range",
        "type": "spec.cvlast.CVLRange",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "spec.cvlast.CVLRange.Range",
        "specFile": "certora/specs/ViewReentrancy.spec",
        "start": {
          "line": 26,
          "character": 4
        },
        "end": {
          "line": 26,
          "character": 56
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
        "source": 7,
        "begin": 6327,
        "len": 29,
        "jumpType": "REGULAR",
        "address": "ce4604a0000000000000000000000028",
        "sourceContext": {
          "indexToFilepath": {
            "0": "contracts/Context.sol",
            "1": "contracts/CurveToken.sol",
            "2": "contracts/CurveTokenExample.sol",
            "3": "contracts/ERC20.sol",
            "4": "contracts/IERC20.sol",
            "5": "contracts/IERC20Metadata.sol",
            "6": "contracts/ReentrancyGuard.sol",
            "7": "contracts/curve.sol"
          },
          "sourceDir": ".post_autofinders.2"
        }
      }
    }
  ],
  "131": [
    {
      "key": {
        "name": "cvl.range",
        "type": "spec.cvlast.CVLRange",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "spec.cvlast.CVLRange.Range",
        "specFile": "certora/specs/ViewReentrancy.spec",
        "start": {
          "line": 26,
          "character": 4
        },
        "end": {
          "line": 26,
          "character": 56
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
        "source": 8,
        "begin": 5461,
        "len": 13,
        "jumpType": "REGULAR",
        "address": "ce4604a0000000000000000000000028",
        "sourceContext": {
          "indexToFilepath": {
            "0": "contracts/Context.sol",
            "1": "contracts/CurveToken.sol",
            "2": "contracts/CurveTokenExample.sol",
            "3": "contracts/ERC20.sol",
            "4": "contracts/IERC20.sol",
            "5": "contracts/IERC20Metadata.sol",
            "6": "contracts/ReentrancyGuard.sol",
            "7": "contracts/curve.sol"
          },
          "sourceDir": ".post_autofinders.2"
        }
      }
    }
  ],
  "132": [
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
  "133": [
    {
      "key": {
        "name": "cvl.range",
        "type": "spec.cvlast.CVLRange",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "spec.cvlast.CVLRange.Range",
        "specFile": "certora/specs/ViewReentrancy.spec",
        "start": {
          "line": 26,
          "character": 4
        },
        "end": {
          "line": 26,
          "character": 56
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
        "source": 8,
        "begin": 4578,
        "len": 37,
        "jumpType": "REGULAR",
        "address": "ce4604a0000000000000000000000028",
        "sourceContext": {
          "indexToFilepath": {
            "0": "contracts/Context.sol",
            "1": "contracts/CurveToken.sol",
            "2": "contracts/CurveTokenExample.sol",
            "3": "contracts/ERC20.sol",
            "4": "contracts/IERC20.sol",
            "5": "contracts/IERC20Metadata.sol",
            "6": "contracts/ReentrancyGuard.sol",
            "7": "contracts/curve.sol"
          },
          "sourceDir": ".post_autofinders.2"
        }
      }
    }
  ],
  "134": [
    {
      "key": {
        "name": "cvl.range",
        "type": "spec.cvlast.CVLRange",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "spec.cvlast.CVLRange.Range",
        "specFile": "certora/specs/ViewReentrancy.spec",
        "start": {
          "line": 26,
          "character": 4
        },
        "end": {
          "line": 26,
          "character": 56
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
        "source": 8,
        "begin": 3538,
        "len": 37,
        "jumpType": "REGULAR",
        "address": "ce4604a0000000000000000000000028",
        "sourceContext": {
          "indexToFilepath": {
            "0": "contracts/Context.sol",
            "1": "contracts/CurveToken.sol",
            "2": "contracts/CurveTokenExample.sol",
            "3": "contracts/ERC20.sol",
            "4": "contracts/IERC20.sol",
            "5": "contracts/IERC20Metadata.sol",
            "6": "contracts/ReentrancyGuard.sol",
            "7": "contracts/curve.sol"
          },
          "sourceDir": ".post_autofinders.2"
        }
      }
    }
  ],
  "135": [
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
      "value": "ce4604a0000000000000000000000028"
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
  "136": [
    {
      "key": {
        "name": "cvl.range",
        "type": "spec.cvlast.CVLRange",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "spec.cvlast.CVLRange.Range",
        "specFile": "certora/specs/ViewReentrancy.spec",
        "start": {
          "line": 28,
          "character": 4
        },
        "end": {
          "line": 28,
          "character": 55
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
        "source": 8,
        "begin": 9679,
        "len": 119,
        "jumpType": "REGULAR",
        "address": "ce4604a0000000000000000000000028",
        "sourceContext": {
          "indexToFilepath": {
            "0": "contracts/Context.sol",
            "1": "contracts/CurveToken.sol",
            "2": "contracts/CurveTokenExample.sol",
            "3": "contracts/ERC20.sol",
            "4": "contracts/IERC20.sol",
            "5": "contracts/IERC20Metadata.sol",
            "6": "contracts/ReentrancyGuard.sol",
            "7": "contracts/curve.sol"
          },
          "sourceDir": ".post_autofinders.2"
        }
      }
    }
  ],
  "137": [
    {
      "key": {
        "name": "cvl.range",
        "type": "spec.cvlast.CVLRange",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "spec.cvlast.CVLRange.Range",
        "specFile": "certora/specs/ViewReentrancy.spec",
        "start": {
          "line": 28,
          "character": 4
        },
        "end": {
          "line": 28,
          "character": 55
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
        "source": 8,
        "begin": 9525,
        "len": 13,
        "jumpType": "REGULAR",
        "address": "ce4604a0000000000000000000000028",
        "sourceContext": {
          "indexToFilepath": {
            "0": "contracts/Context.sol",
            "1": "contracts/CurveToken.sol",
            "2": "contracts/CurveTokenExample.sol",
            "3": "contracts/ERC20.sol",
            "4": "contracts/IERC20.sol",
            "5": "contracts/IERC20Metadata.sol",
            "6": "contracts/ReentrancyGuard.sol",
            "7": "contracts/curve.sol"
          },
          "sourceDir": ".post_autofinders.2"
        }
      }
    }
  ],
  "138": [
    {
      "key": {
        "name": "cvl.range",
        "type": "spec.cvlast.CVLRange",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "spec.cvlast.CVLRange.Range",
        "specFile": "certora/specs/ViewReentrancy.spec",
        "start": {
          "line": 28,
          "character": 4
        },
        "end": {
          "line": 28,
          "character": 55
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
        "source": 8,
        "begin": 9422,
        "len": 9,
        "jumpType": "REGULAR",
        "address": "ce4604a0000000000000000000000028",
        "sourceContext": {
          "indexToFilepath": {
            "0": "contracts/Context.sol",
            "1": "contracts/CurveToken.sol",
            "2": "contracts/CurveTokenExample.sol",
            "3": "contracts/ERC20.sol",
            "4": "contracts/IERC20.sol",
            "5": "contracts/IERC20Metadata.sol",
            "6": "contracts/ReentrancyGuard.sol",
            "7": "contracts/curve.sol"
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
  "139": [
    {
      "key": {
        "name": "cvl.range",
        "type": "spec.cvlast.CVLRange",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "spec.cvlast.CVLRange.Range",
        "specFile": "certora/specs/ViewReentrancy.spec",
        "start": {
          "line": 28,
          "character": 4
        },
        "end": {
          "line": 28,
          "character": 55
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
        "source": 7,
        "begin": 6327,
        "len": 29,
        "jumpType": "REGULAR",
        "address": "ce4604a0000000000000000000000028",
        "sourceContext": {
          "indexToFilepath": {
            "0": "contracts/Context.sol",
            "1": "contracts/CurveToken.sol",
            "2": "contracts/CurveTokenExample.sol",
            "3": "contracts/ERC20.sol",
            "4": "contracts/IERC20.sol",
            "5": "contracts/IERC20Metadata.sol",
            "6": "contracts/ReentrancyGuard.sol",
            "7": "contracts/curve.sol"
          },
          "sourceDir": ".post_autofinders.2"
        }
      }
    }
  ],
  "140": [
    {
      "key": {
        "name": "cvl.range",
        "type": "spec.cvlast.CVLRange",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "spec.cvlast.CVLRange.Range",
        "specFile": "certora/specs/ViewReentrancy.spec",
        "start": {
          "line": 28,
          "character": 4
        },
        "end": {
          "line": 28,
          "character": 55
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
        "source": 8,
        "begin": 5461,
        "len": 13,
        "jumpType": "REGULAR",
        "address": "ce4604a0000000000000000000000028",
        "sourceContext": {
          "indexToFilepath": {
            "0": "contracts/Context.sol",
            "1": "contracts/CurveToken.sol",
            "2": "contracts/CurveTokenExample.sol",
            "3": "contracts/ERC20.sol",
            "4": "contracts/IERC20.sol",
            "5": "contracts/IERC20Metadata.sol",
            "6": "contracts/ReentrancyGuard.sol",
            "7": "contracts/curve.sol"
          },
          "sourceDir": ".post_autofinders.2"
        }
      }
    }
  ],
  "141": [
    {
      "key": {
        "name": "cvl.range",
        "type": "spec.cvlast.CVLRange",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "spec.cvlast.CVLRange.Range",
        "specFile": "certora/specs/ViewReentrancy.spec",
        "start": {
          "line": 28,
          "character": 4
        },
        "end": {
          "line": 28,
          "character": 55
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
        "source": 8,
        "begin": 4578,
        "len": 37,
        "jumpType": "REGULAR",
        "address": "ce4604a0000000000000000000000028",
        "sourceContext": {
          "indexToFilepath": {
            "0": "contracts/Context.sol",
            "1": "contracts/CurveToken.sol",
            "2": "contracts/CurveTokenExample.sol",
            "3": "contracts/ERC20.sol",
            "4": "contracts/IERC20.sol",
            "5": "contracts/IERC20Metadata.sol",
            "6": "contracts/ReentrancyGuard.sol",
            "7": "contracts/curve.sol"
          },
          "sourceDir": ".post_autofinders.2"
        }
      }
    }
  ],
  "142": [
    {
      "key": {
        "name": "cvl.range",
        "type": "spec.cvlast.CVLRange",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "spec.cvlast.CVLRange.Range",
        "specFile": "certora/specs/ViewReentrancy.spec",
        "start": {
          "line": 28,
          "character": 4
        },
        "end": {
          "line": 28,
          "character": 55
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
        "source": 8,
        "begin": 3538,
        "len": 37,
        "jumpType": "REGULAR",
        "address": "ce4604a0000000000000000000000028",
        "sourceContext": {
          "indexToFilepath": {
            "0": "contracts/Context.sol",
            "1": "contracts/CurveToken.sol",
            "2": "contracts/CurveTokenExample.sol",
            "3": "contracts/ERC20.sol",
            "4": "contracts/IERC20.sol",
            "5": "contracts/IERC20Metadata.sol",
            "6": "contracts/ReentrancyGuard.sol",
            "7": "contracts/curve.sol"
          },
          "sourceDir": ".post_autofinders.2"
        }
      }
    }
  ],
  "143": [
    {
      "key": {
        "name": "cvl.range",
        "type": "spec.cvlast.CVLRange",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "spec.cvlast.CVLRange.Range",
        "specFile": "certora/specs/ViewReentrancy.spec",
        "start": {
          "line": 26,
          "character": 4
        },
        "end": {
          "line": 26,
          "character": 56
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
        "source": 7,
        "begin": 6388,
        "len": 29,
        "jumpType": "REGULAR",
        "address": "ce4604a0000000000000000000000028",
        "sourceContext": {
          "indexToFilepath": {
            "0": "contracts/Context.sol",
            "1": "contracts/CurveToken.sol",
            "2": "contracts/CurveTokenExample.sol",
            "3": "contracts/ERC20.sol",
            "4": "contracts/IERC20.sol",
            "5": "contracts/IERC20Metadata.sol",
            "6": "contracts/ReentrancyGuard.sol",
            "7": "contracts/curve.sol"
          },
          "sourceDir": ".post_autofinders.2"
        }
      }
    }
  ],
  "144": [
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
  "145": [
    {
      "key": {
        "name": "cvl.range",
        "type": "spec.cvlast.CVLRange",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "spec.cvlast.CVLRange.Range",
        "specFile": "certora/specs/ViewReentrancy.spec",
        "start": {
          "line": 26,
          "character": 4
        },
        "end": {
          "line": 26,
          "character": 56
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
        "source": 8,
        "begin": 8848,
        "len": 9,
        "jumpType": "REGULAR",
        "address": "ce4604a0000000000000000000000028",
        "sourceContext": {
          "indexToFilepath": {
            "0": "contracts/Context.sol",
            "1": "contracts/CurveToken.sol",
            "2": "contracts/CurveTokenExample.sol",
            "3": "contracts/ERC20.sol",
            "4": "contracts/IERC20.sol",
            "5": "contracts/IERC20Metadata.sol",
            "6": "contracts/ReentrancyGuard.sol",
            "7": "contracts/curve.sol"
          },
          "sourceDir": ".post_autofinders.2"
        }
      }
    }
  ],
  "146": [
    {
      "key": {
        "name": "cvl.range",
        "type": "spec.cvlast.CVLRange",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "spec.cvlast.CVLRange.Range",
        "specFile": "certora/specs/ViewReentrancy.spec",
        "start": {
          "line": 26,
          "character": 4
        },
        "end": {
          "line": 26,
          "character": 56
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
        "source": 8,
        "begin": 9225,
        "len": 9,
        "jumpType": "REGULAR",
        "address": "ce4604a0000000000000000000000028",
        "sourceContext": {
          "indexToFilepath": {
            "0": "contracts/Context.sol",
            "1": "contracts/CurveToken.sol",
            "2": "contracts/CurveTokenExample.sol",
            "3": "contracts/ERC20.sol",
            "4": "contracts/IERC20.sol",
            "5": "contracts/IERC20Metadata.sol",
            "6": "contracts/ReentrancyGuard.sol",
            "7": "contracts/curve.sol"
          },
          "sourceDir": ".post_autofinders.2"
        }
      }
    }
  ],
  "147": [
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
  "148": [
    {
      "key": {
        "name": "cvl.range",
        "type": "spec.cvlast.CVLRange",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "spec.cvlast.CVLRange.Range",
        "specFile": "certora/specs/ViewReentrancy.spec",
        "start": {
          "line": 28,
          "character": 4
        },
        "end": {
          "line": 28,
          "character": 55
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
        "source": 7,
        "begin": 6388,
        "len": 29,
        "jumpType": "REGULAR",
        "address": "ce4604a0000000000000000000000028",
        "sourceContext": {
          "indexToFilepath": {
            "0": "contracts/Context.sol",
            "1": "contracts/CurveToken.sol",
            "2": "contracts/CurveTokenExample.sol",
            "3": "contracts/ERC20.sol",
            "4": "contracts/IERC20.sol",
            "5": "contracts/IERC20Metadata.sol",
            "6": "contracts/ReentrancyGuard.sol",
            "7": "contracts/curve.sol"
          },
          "sourceDir": ".post_autofinders.2"
        }
      }
    }
  ],
  "149": [
    {
      "key": {
        "name": "cvl.range",
        "type": "spec.cvlast.CVLRange",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "spec.cvlast.CVLRange.Range",
        "specFile": "certora/specs/ViewReentrancy.spec",
        "start": {
          "line": 28,
          "character": 4
        },
        "end": {
          "line": 28,
          "character": 55
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
        "source": 8,
        "begin": 8848,
        "len": 9,
        "jumpType": "REGULAR",
        "address": "ce4604a0000000000000000000000028",
        "sourceContext": {
          "indexToFilepath": {
            "0": "contracts/Context.sol",
            "1": "contracts/CurveToken.sol",
            "2": "contracts/CurveTokenExample.sol",
            "3": "contracts/ERC20.sol",
            "4": "contracts/IERC20.sol",
            "5": "contracts/IERC20Metadata.sol",
            "6": "contracts/ReentrancyGuard.sol",
            "7": "contracts/curve.sol"
          },
          "sourceDir": ".post_autofinders.2"
        }
      }
    }
  ],
  "150": [
    {
      "key": {
        "name": "cvl.range",
        "type": "spec.cvlast.CVLRange",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "spec.cvlast.CVLRange.Range",
        "specFile": "certora/specs/ViewReentrancy.spec",
        "start": {
          "line": 28,
          "character": 4
        },
        "end": {
          "line": 28,
          "character": 55
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
        "source": 8,
        "begin": 9225,
        "len": 9,
        "jumpType": "REGULAR",
        "address": "ce4604a0000000000000000000000028",
        "sourceContext": {
          "indexToFilepath": {
            "0": "contracts/Context.sol",
            "1": "contracts/CurveToken.sol",
            "2": "contracts/CurveTokenExample.sol",
            "3": "contracts/ERC20.sol",
            "4": "contracts/IERC20.sol",
            "5": "contracts/IERC20Metadata.sol",
            "6": "contracts/ReentrancyGuard.sol",
            "7": "contracts/curve.sol"
          },
          "sourceDir": ".post_autofinders.2"
        }
      }
    }
  ],
  "151": [
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
      "value": "ce4604a0000000000000000000000028"
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
  "152": [
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
            "id": "before_func1",
            "tag": {
              "scope": {
                "scopeStack": [
                  {
                    "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                  },
                  {
                    "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                    "scopeId": 0
                  }
                ],
                "innerScope": {
                  "scopeStack": [
                    {
                      "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                    }
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
                "specFile": "certora/specs/ViewReentrancy.spec",
                "start": {
                  "line": 26,
                  "character": 4
                },
                "end": {
                  "line": 26,
                  "character": 56
                }
              }
            },
            "twoStateIndex": "NEITHER"
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
                      "name": "curve"
                    },
                    "methodId": "getVirtualPrice"
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
                  "n": "e25aa5fa"
                }
              }
            },
            "args": [
              {
                "#class": "spec.cvlast.CVLExp.VariableExp",
                "id": "e_external",
                "tag": {
                  "scope": {
                    "scopeStack": [
                      {
                        "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                      },
                      {
                        "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                        "scopeId": 0
                      }
                    ],
                    "innerScope": {
                      "scopeStack": [
                        {
                          "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                        }
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
                    "specFile": "certora/specs/ViewReentrancy.spec",
                    "start": {
                      "line": 26,
                      "character": 4
                    },
                    "end": {
                      "line": 26,
                      "character": 56
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
                      "scopeId": 0
                    }
                  ],
                  "innerScope": {
                    "scopeStack": [
                      {
                        "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                      }
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
                  "specFile": "certora/specs/ViewReentrancy.spec",
                  "start": {
                    "line": 26,
                    "character": 4
                  },
                  "end": {
                    "line": 26,
                    "character": 56
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
                    "scopeId": 0
                  }
                ],
                "innerScope": {
                  "scopeStack": [
                    {
                      "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                    }
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
                "specFile": "certora/specs/ViewReentrancy.spec",
                "start": {
                  "line": 26,
                  "character": 28
                },
                "end": {
                  "line": 26,
                  "character": 43
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
                          "name": "curve"
                        },
                        "methodId": "getVirtualPrice"
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
                      "n": "e25aa5fa"
                    }
                  },
                  "definitelyNonPayable": true,
                  "annotation": {
                    "visibility": "EXTERNAL",
                    "envFree": false,
                    "library": false
                  },
                  "stateMutability": "view",
                  "tag": {
                    "#class": "spec.cvlast.CVLImportedFunctionTag.WithMethodInfo",
                    "evmMethodInfo": {
                      "sigHash": "e25aa5fa",
                      "name": "getVirtualPrice",
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
                "hasEnv": true
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
                  "scopeId": 0
                }
              ],
              "innerScope": {
                "scopeStack": [
                  {
                    "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                  }
                ],
                "innerScope": {
                  "scopeStack": [
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
              "specFile": "certora/specs/ViewReentrancy.spec",
              "start": {
                "line": 26,
                "character": 12
              },
              "end": {
                "line": 26,
                "character": 55
              }
            }
          }
        },
        "o1": {
          "out": {
            "#class": "vc.data.TACSymbol.Var.Full",
            "namePrefix": "I23",
            "tag": {
              "#class": "tac.Tag.Int"
            },
            "callIndex": 0
          },
          "exp": {
            "#class": "spec.cvlast.CVLExp.VariableExp",
            "id": "before_func1",
            "tag": {
              "scope": {
                "scopeStack": [
                  {
                    "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                  },
                  {
                    "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                    "scopeId": 0
                  }
                ],
                "innerScope": {
                  "scopeStack": [
                    {
                      "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                    }
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
                "specFile": "certora/specs/ViewReentrancy.spec",
                "start": {
                  "line": 26,
                  "character": 4
                },
                "end": {
                  "line": 26,
                  "character": 56
                }
              }
            },
            "twoStateIndex": "NEITHER"
          }
        },
        "o2": {
          "out": {
            "#class": "vc.data.TACSymbol.Var.Full",
            "namePrefix": "I418",
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
                      "name": "curve"
                    },
                    "methodId": "getVirtualPrice"
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
                  "n": "e25aa5fa"
                }
              }
            },
            "args": [
              {
                "#class": "spec.cvlast.CVLExp.VariableExp",
                "id": "e_external",
                "tag": {
                  "scope": {
                    "scopeStack": [
                      {
                        "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                      },
                      {
                        "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                        "scopeId": 0
                      }
                    ],
                    "innerScope": {
                      "scopeStack": [
                        {
                          "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                        }
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
                    "specFile": "certora/specs/ViewReentrancy.spec",
                    "start": {
                      "line": 26,
                      "character": 4
                    },
                    "end": {
                      "line": 26,
                      "character": 56
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
                      "scopeId": 0
                    }
                  ],
                  "innerScope": {
                    "scopeStack": [
                      {
                        "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                      }
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
                  "specFile": "certora/specs/ViewReentrancy.spec",
                  "start": {
                    "line": 26,
                    "character": 4
                  },
                  "end": {
                    "line": 26,
                    "character": 56
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
                    "scopeId": 0
                  }
                ],
                "innerScope": {
                  "scopeStack": [
                    {
                      "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                    }
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
                "specFile": "certora/specs/ViewReentrancy.spec",
                "start": {
                  "line": 26,
                  "character": 28
                },
                "end": {
                  "line": 26,
                  "character": 43
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
                          "name": "curve"
                        },
                        "methodId": "getVirtualPrice"
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
                      "n": "e25aa5fa"
                    }
                  },
                  "definitelyNonPayable": true,
                  "annotation": {
                    "visibility": "EXTERNAL",
                    "envFree": false,
                    "library": false
                  },
                  "stateMutability": "view",
                  "tag": {
                    "#class": "spec.cvlast.CVLImportedFunctionTag.WithMethodInfo",
                    "evmMethodInfo": {
                      "sigHash": "e25aa5fa",
                      "name": "getVirtualPrice",
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
                "hasEnv": true
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
        "specFile": "certora/specs/ViewReentrancy.spec",
        "start": {
          "line": 26,
          "character": 4
        },
        "end": {
          "line": 26,
          "character": 56
        }
      }
    }
  ],
  "153": [
    {
      "key": {
        "name": "cvl",
        "type": "java.lang.Boolean",
        "erasureStrategy": "Canonical"
      },
      "value": true
    }
  ],
  "154": [
    {
      "key": {
        "name": "cvl.range",
        "type": "spec.cvlast.CVLRange",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "spec.cvlast.CVLRange.Range",
        "specFile": "certora/specs/ViewReentrancy.spec",
        "start": {
          "line": 27,
          "character": 4
        },
        "end": {
          "line": 27,
          "character": 15
        }
      }
    }
  ],
  "155": [
    {
      "key": {
        "name": "cvl.local",
        "type": "java.lang.Boolean",
        "erasureStrategy": "Canonical"
      },
      "value": false
    }
  ],
  "156": [
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
          "callIndex": 5,
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
  "157": [
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
  "158": [
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
        "specFile": "certora/specs/ViewReentrancy.spec",
        "start": {
          "line": 27,
          "character": 4
        },
        "end": {
          "line": 27,
          "character": 15
        }
      }
    }
  ],
  "159": [
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
            "id": "after_func1",
            "tag": {
              "scope": {
                "scopeStack": [
                  {
                    "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                  },
                  {
                    "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                    "scopeId": 0
                  }
                ],
                "innerScope": {
                  "scopeStack": [
                    {
                      "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                    }
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
                "specFile": "certora/specs/ViewReentrancy.spec",
                "start": {
                  "line": 28,
                  "character": 4
                },
                "end": {
                  "line": 28,
                  "character": 55
                }
              }
            },
            "twoStateIndex": "NEITHER"
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
                      "name": "curve"
                    },
                    "methodId": "getVirtualPrice"
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
                  "n": "e25aa5fa"
                }
              }
            },
            "args": [
              {
                "#class": "spec.cvlast.CVLExp.VariableExp",
                "id": "e_external",
                "tag": {
                  "scope": {
                    "scopeStack": [
                      {
                        "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                      },
                      {
                        "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                        "scopeId": 0
                      }
                    ],
                    "innerScope": {
                      "scopeStack": [
                        {
                          "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                        }
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
                    "specFile": "certora/specs/ViewReentrancy.spec",
                    "start": {
                      "line": 28,
                      "character": 4
                    },
                    "end": {
                      "line": 28,
                      "character": 55
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
                      "scopeId": 0
                    }
                  ],
                  "innerScope": {
                    "scopeStack": [
                      {
                        "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                      }
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
                  "specFile": "certora/specs/ViewReentrancy.spec",
                  "start": {
                    "line": 28,
                    "character": 4
                  },
                  "end": {
                    "line": 28,
                    "character": 55
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
                    "scopeId": 0
                  }
                ],
                "innerScope": {
                  "scopeStack": [
                    {
                      "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                    }
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
                "specFile": "certora/specs/ViewReentrancy.spec",
                "start": {
                  "line": 28,
                  "character": 27
                },
                "end": {
                  "line": 28,
                  "character": 42
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
                          "name": "curve"
                        },
                        "methodId": "getVirtualPrice"
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
                      "n": "e25aa5fa"
                    }
                  },
                  "definitelyNonPayable": true,
                  "annotation": {
                    "visibility": "EXTERNAL",
                    "envFree": false,
                    "library": false
                  },
                  "stateMutability": "view",
                  "tag": {
                    "#class": "spec.cvlast.CVLImportedFunctionTag.WithMethodInfo",
                    "evmMethodInfo": {
                      "sigHash": "e25aa5fa",
                      "name": "getVirtualPrice",
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
                "hasEnv": true
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
                  "scopeId": 0
                }
              ],
              "innerScope": {
                "scopeStack": [
                  {
                    "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                  }
                ],
                "innerScope": {
                  "scopeStack": [
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
              "specFile": "certora/specs/ViewReentrancy.spec",
              "start": {
                "line": 28,
                "character": 12
              },
              "end": {
                "line": 28,
                "character": 54
              }
            }
          }
        },
        "o1": {
          "out": {
            "#class": "vc.data.TACSymbol.Var.Full",
            "namePrefix": "I8",
            "tag": {
              "#class": "tac.Tag.Int"
            },
            "callIndex": 0
          },
          "exp": {
            "#class": "spec.cvlast.CVLExp.VariableExp",
            "id": "after_func1",
            "tag": {
              "scope": {
                "scopeStack": [
                  {
                    "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                  },
                  {
                    "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                    "scopeId": 0
                  }
                ],
                "innerScope": {
                  "scopeStack": [
                    {
                      "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                    }
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
                "specFile": "certora/specs/ViewReentrancy.spec",
                "start": {
                  "line": 28,
                  "character": 4
                },
                "end": {
                  "line": 28,
                  "character": 55
                }
              }
            },
            "twoStateIndex": "NEITHER"
          }
        },
        "o2": {
          "out": {
            "#class": "vc.data.TACSymbol.Var.Full",
            "namePrefix": "I433",
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
                      "name": "curve"
                    },
                    "methodId": "getVirtualPrice"
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
                  "n": "e25aa5fa"
                }
              }
            },
            "args": [
              {
                "#class": "spec.cvlast.CVLExp.VariableExp",
                "id": "e_external",
                "tag": {
                  "scope": {
                    "scopeStack": [
                      {
                        "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                      },
                      {
                        "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                        "scopeId": 0
                      }
                    ],
                    "innerScope": {
                      "scopeStack": [
                        {
                          "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                        }
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
                    "specFile": "certora/specs/ViewReentrancy.spec",
                    "start": {
                      "line": 28,
                      "character": 4
                    },
                    "end": {
                      "line": 28,
                      "character": 55
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
                      "scopeId": 0
                    }
                  ],
                  "innerScope": {
                    "scopeStack": [
                      {
                        "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                      }
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
                  "specFile": "certora/specs/ViewReentrancy.spec",
                  "start": {
                    "line": 28,
                    "character": 4
                  },
                  "end": {
                    "line": 28,
                    "character": 55
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
                    "scopeId": 0
                  }
                ],
                "innerScope": {
                  "scopeStack": [
                    {
                      "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                    }
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
                "specFile": "certora/specs/ViewReentrancy.spec",
                "start": {
                  "line": 28,
                  "character": 27
                },
                "end": {
                  "line": 28,
                  "character": 42
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
                          "name": "curve"
                        },
                        "methodId": "getVirtualPrice"
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
                      "n": "e25aa5fa"
                    }
                  },
                  "definitelyNonPayable": true,
                  "annotation": {
                    "visibility": "EXTERNAL",
                    "envFree": false,
                    "library": false
                  },
                  "stateMutability": "view",
                  "tag": {
                    "#class": "spec.cvlast.CVLImportedFunctionTag.WithMethodInfo",
                    "evmMethodInfo": {
                      "sigHash": "e25aa5fa",
                      "name": "getVirtualPrice",
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
                "hasEnv": true
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
        "specFile": "certora/specs/ViewReentrancy.spec",
        "start": {
          "line": 28,
          "character": 4
        },
        "end": {
          "line": 28,
          "character": 55
        }
      }
    }
  ],
  "160": [
    {
      "key": {
        "name": "cvl.range",
        "type": "spec.cvlast.CVLRange",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "spec.cvlast.CVLRange.Range",
        "specFile": "certora/specs/ViewReentrancy.spec",
        "start": {
          "line": 29,
          "character": 4
        },
        "end": {
          "line": 29,
          "character": 16
        }
      }
    }
  ],
  "161": [
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
        "specFile": "certora/specs/ViewReentrancy.spec",
        "start": {
          "line": 29,
          "character": 4
        },
        "end": {
          "line": 29,
          "character": 16
        }
      }
    }
  ],
  "162": [
    {
      "key": {
        "name": "tac.meta",
        "type": "vc.data.TACMetaInfo",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "source": 8,
        "begin": 3898,
        "len": 23,
        "jumpType": "REGULAR",
        "address": "ce4604a0000000000000000000000028",
        "sourceContext": {
          "indexToFilepath": {
            "0": "contracts/Context.sol",
            "1": "contracts/CurveToken.sol",
            "2": "contracts/CurveTokenExample.sol",
            "3": "contracts/ERC20.sol",
            "4": "contracts/IERC20.sol",
            "5": "contracts/IERC20Metadata.sol",
            "6": "contracts/ReentrancyGuard.sol",
            "7": "contracts/curve.sol"
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
  "163": [
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
        "address": "ce4604a0000000000000000000000028",
        "sourceContext": {
          "indexToFilepath": {
            "0": "contracts/Context.sol",
            "1": "contracts/CurveToken.sol",
            "2": "contracts/CurveTokenExample.sol",
            "3": "contracts/ERC20.sol",
            "4": "contracts/IERC20.sol",
            "5": "contracts/IERC20Metadata.sol",
            "6": "contracts/ReentrancyGuard.sol",
            "7": "contracts/curve.sol"
          },
          "sourceDir": ".post_autofinders.2"
        }
      }
    }
  ],
  "164": [
    {
      "key": {
        "name": "tac.meta",
        "type": "vc.data.TACMetaInfo",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "source": 7,
        "begin": 5879,
        "len": 17,
        "jumpType": "REGULAR",
        "address": "ce4604a0000000000000000000000028",
        "sourceContext": {
          "indexToFilepath": {
            "0": "contracts/Context.sol",
            "1": "contracts/CurveToken.sol",
            "2": "contracts/CurveTokenExample.sol",
            "3": "contracts/ERC20.sol",
            "4": "contracts/IERC20.sol",
            "5": "contracts/IERC20Metadata.sol",
            "6": "contracts/ReentrancyGuard.sol",
            "7": "contracts/curve.sol"
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
  "165": [
    {
      "key": {
        "name": "tac.meta",
        "type": "vc.data.TACMetaInfo",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "source": 7,
        "begin": 5855,
        "len": 21,
        "jumpType": "REGULAR",
        "address": "ce4604a0000000000000000000000028",
        "sourceContext": {
          "indexToFilepath": {
            "0": "contracts/Context.sol",
            "1": "contracts/CurveToken.sol",
            "2": "contracts/CurveTokenExample.sol",
            "3": "contracts/ERC20.sol",
            "4": "contracts/IERC20.sol",
            "5": "contracts/IERC20Metadata.sol",
            "6": "contracts/ReentrancyGuard.sol",
            "7": "contracts/curve.sol"
          },
          "sourceDir": ".post_autofinders.2"
        }
      }
    }
  ],
  "166": [
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
        "address": "ce4604a0000000000000000000000028",
        "sourceContext": {
          "indexToFilepath": {
            "0": "contracts/Context.sol",
            "1": "contracts/CurveToken.sol",
            "2": "contracts/CurveTokenExample.sol",
            "3": "contracts/ERC20.sol",
            "4": "contracts/IERC20.sol",
            "5": "contracts/IERC20Metadata.sol",
            "6": "contracts/ReentrancyGuard.sol",
            "7": "contracts/curve.sol"
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
  "167": [
    {
      "key": {
        "name": "tac.meta",
        "type": "vc.data.TACMetaInfo",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "source": 7,
        "begin": 5961,
        "len": 17,
        "jumpType": "REGULAR",
        "address": "ce4604a0000000000000000000000028",
        "sourceContext": {
          "indexToFilepath": {
            "0": "contracts/Context.sol",
            "1": "contracts/CurveToken.sol",
            "2": "contracts/CurveTokenExample.sol",
            "3": "contracts/ERC20.sol",
            "4": "contracts/IERC20.sol",
            "5": "contracts/IERC20Metadata.sol",
            "6": "contracts/ReentrancyGuard.sol",
            "7": "contracts/curve.sol"
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
  "168": [
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
      "value": "ce4604a0000000000000000000000028"
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
  "169": [
    {
      "key": {
        "name": "tac.meta",
        "type": "vc.data.TACMetaInfo",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "source": 7,
        "begin": 5919,
        "len": 39,
        "jumpType": "REGULAR",
        "address": "ce4604a0000000000000000000000028",
        "sourceContext": {
          "indexToFilepath": {
            "0": "contracts/Context.sol",
            "1": "contracts/CurveToken.sol",
            "2": "contracts/CurveTokenExample.sol",
            "3": "contracts/ERC20.sol",
            "4": "contracts/IERC20.sol",
            "5": "contracts/IERC20Metadata.sol",
            "6": "contracts/ReentrancyGuard.sol",
            "7": "contracts/curve.sol"
          },
          "sourceDir": ".post_autofinders.2"
        }
      }
    }
  ],
  "170": [
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
        "address": "ce4604a0000000000000000000000028",
        "sourceContext": {
          "indexToFilepath": {
            "0": "contracts/Context.sol",
            "1": "contracts/CurveToken.sol",
            "2": "contracts/CurveTokenExample.sol",
            "3": "contracts/ERC20.sol",
            "4": "contracts/IERC20.sol",
            "5": "contracts/IERC20Metadata.sol",
            "6": "contracts/ReentrancyGuard.sol",
            "7": "contracts/curve.sol"
          },
          "sourceDir": ".post_autofinders.2"
        }
      }
    }
  ],
  "171": [
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
          "callIndex": 5,
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
  "172": [
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
      "value": "curve"
    },
    {
      "key": {
        "name": "tac.contract.sym.addr",
        "type": "java.math.BigInteger",
        "erasureStrategy": "Erased"
      },
      "value": "ce4604a0000000000000000000000028"
    }
  ],
  "173": [
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
        "address": "ce4604a0000000000000000000000011",
        "sourceContext": {
          "indexToFilepath": {
            "0": "contracts/Context.sol",
            "1": "contracts/ERC20.sol",
            "2": "contracts/IERC20.sol",
            "3": "contracts/IERC20Metadata.sol"
          },
          "sourceDir": ".post_autofinders.1"
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
  "174": [
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
        "address": "ce4604a0000000000000000000000011",
        "sourceContext": {
          "indexToFilepath": {
            "0": "contracts/Context.sol",
            "1": "contracts/ERC20.sol",
            "2": "contracts/IERC20.sol",
            "3": "contracts/IERC20Metadata.sol"
          },
          "sourceDir": ".post_autofinders.1"
        }
      }
    }
  ],
  "175": [
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
          "callIndex": 6,
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
  "176": [
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
        "address": "ce4604a0000000000000000000000011",
        "sourceContext": {
          "indexToFilepath": {
            "0": "contracts/Context.sol",
            "1": "contracts/ERC20.sol",
            "2": "contracts/IERC20.sol",
            "3": "contracts/IERC20Metadata.sol"
          },
          "sourceDir": ".post_autofinders.1"
        }
      }
    }
  ],
  "177": [
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
        "address": "ce4604a0000000000000000000000011",
        "sourceContext": {
          "indexToFilepath": {
            "0": "contracts/Context.sol",
            "1": "contracts/ERC20.sol",
            "2": "contracts/IERC20.sol",
            "3": "contracts/IERC20Metadata.sol"
          },
          "sourceDir": ".post_autofinders.1"
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
      "value": "rO0ABXNyADJhbmFseXNpcy5pY2ZnLkNhbGxHcmFwaEJ1aWxkZXIkQ29udHJhY3RTdG9yYWdlUmVhZLRpTKYiS4EFAgABSQACaWR4cAAAAAY="
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
  "178": [
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
              "namePrefix": "R551",
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
                "namePrefix": "R551",
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
                "namePrefix": "CANON114",
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
                "namePrefix": "CANON113",
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
  "179": [
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
        "address": "ce4604a0000000000000000000000028",
        "sourceContext": {
          "indexToFilepath": {
            "0": "contracts/Context.sol",
            "1": "contracts/CurveToken.sol",
            "2": "contracts/CurveTokenExample.sol",
            "3": "contracts/ERC20.sol",
            "4": "contracts/IERC20.sol",
            "5": "contracts/IERC20Metadata.sol",
            "6": "contracts/ReentrancyGuard.sol",
            "7": "contracts/curve.sol"
          },
          "sourceDir": ".post_autofinders.2"
        }
      }
    }
  ],
  "180": [
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
        "address": "ce4604a0000000000000000000000028",
        "sourceContext": {
          "indexToFilepath": {
            "0": "contracts/Context.sol",
            "1": "contracts/CurveToken.sol",
            "2": "contracts/CurveTokenExample.sol",
            "3": "contracts/ERC20.sol",
            "4": "contracts/IERC20.sol",
            "5": "contracts/IERC20Metadata.sol",
            "6": "contracts/ReentrancyGuard.sol",
            "7": "contracts/curve.sol"
          },
          "sourceDir": ".post_autofinders.2"
        }
      }
    }
  ]
}