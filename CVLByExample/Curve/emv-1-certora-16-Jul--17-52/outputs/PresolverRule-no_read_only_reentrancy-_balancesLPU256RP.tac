TACSymbolTable {
	UserDefined {
		UninterpSort skey
	}
	BuiltinFunctions {
		to_skey:JSON{"#class":"vc.data.TACBuiltInFunction.Hash.ToSkey"}
		skey_basic:JSON{"#class":"vc.data.TACBuiltInFunction.Hash.Basic"}
		add_noofl:JSON{"#class":"vc.data.TACBuiltInFunction.NoAddOverflowCheck"}
		safe_math_narrow:JSON{"#class":"vc.data.TACBuiltInFunction.SafeMathNarrow"}
		hash_3_keccak:JSON{"#class":"vc.data.TACBuiltInFunction.Hash.SimpleHashApplication","arity":3,"hashFamily":{"#class":"vc.data.HashFamily.Keccack"}}
		safe_math_promotion:JSON{"#class":"vc.data.TACBuiltInFunction.SafeMathPromotion"}
		mul_noofl:JSON{"#class":"vc.data.TACBuiltInFunction.NoMulOverflowCheck"}
	}
	UninterpretedFunctions {
		B26:JSON{"name":"B26","paramSorts":[],"returnSort":{"#class":"tac.Tag.Bool"},"attribute":"Ghost","cvlResultType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"},"cvlParamTypes":[],"declarationName":"CANON75"}
		CANON143:JSON{"name":"CANON143","paramSorts":[],"returnSort":{"#class":"tac.Tag.Int"},"attribute":"Ghost","cvlResultType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256},"cvlParamTypes":[],"declarationName":"CANON143"}
		CANON147:JSON{"name":"CANON147","paramSorts":[],"returnSort":{"#class":"tac.Tag.Int"},"attribute":"Ghost","cvlResultType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256},"cvlParamTypes":[],"declarationName":"CANON147"}
		CANON75:JSON{"name":"CANON75","paramSorts":[],"returnSort":{"#class":"tac.Tag.Bool"},"attribute":"Ghost","cvlResultType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"},"cvlParamTypes":[],"declarationName":"CANON75"}
		CANON77:JSON{"name":"CANON77","paramSorts":[],"returnSort":{"#class":"tac.Tag.Int"},"attribute":"Ghost","cvlResultType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256},"cvlParamTypes":[],"declarationName":"CANON77"}
		I12:JSON{"name":"I12","paramSorts":[],"returnSort":{"#class":"tac.Tag.Int"},"attribute":"Ghost","cvlResultType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256},"cvlParamTypes":[],"declarationName":"CANON143"}
		I27:JSON{"name":"I27","paramSorts":[],"returnSort":{"#class":"tac.Tag.Int"},"attribute":"Ghost","cvlResultType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256},"cvlParamTypes":[],"declarationName":"CANON77"}
	}
	tacM0x40@1:bv256
	tacM0x40@7:bv256
	tacMCANON1!!13:bytemap
	tacMCANON1!!14:bytemap
	tacMCANON2!!15:bytemap
	tacMCANON2!!16:bytemap
	tacMCANON3!!17:bytemap
	tacMCANON3!!18:bytemap
	tacNonce:wordmap
	tacMCANON5!!19:bytemap
	tacCaller@1:bv256
	tacCaller@5:bv256
	tacCaller@7:bv256
	tacMCANON2!!240:bytemap
	tacMCANON2!!242:bytemap
	tacMCANON2!!267:bytemap
	tacMCANON2!!301:bytemap
	tacMCANON2!!315:bytemap
	tacMCANON2!!383:bytemap
	tacMCANON2!!385:bytemap
	tacMCANON2!!410:bytemap
	tacMCANON2!!444:bytemap
	tacMCANON2!!458:bytemap
	tacMCANON2!!465:bytemap
	tacMCANON2!!467:bytemap
	tacMCANON2!!469:bytemap
	tacMCANON2!!471:bytemap
	tacMCANON2!!482:bytemap
	tacMCANON2!!484:bytemap
	tacMCANON2!!486:bytemap
	tacMCANON2!!488:bytemap
	tacMCANON2!!529:bytemap
	tacMCANON2!!539:bytemap
	tacCalldatabufCANON0@2:bv256
	tacCalldatabufCANON0@4:bv256
	tacCalldatabufCANON0@6:bv256
	tacCalldatabufCANON0@8:bv256
	tacCalldatabufCANON0@10:bv256
	tacCalldatabufCANON1@2:bv256
	tacCalldatabufCANON1@6:bv256
	tacCalldatabufCANON1@8:bv256
	tacMCANON6!!20:bytemap
	tacOrigNonceCANON0:wordmap
	tacOrigNonceCANON1:wordmap
	tacOrigNonceCANON2:wordmap
	tacMCANON4havocme5390@5:bytemap
	tacOrigin!!190:bv256
	tacOrigin!!333:bv256
	tacOrigin!!570:bv256
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
	CANON279!!597:bool
	tacM0x0!!262:bv256
	tacM0x0!!405:bv256
	tacM0x0!!644:bv256
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
	tacCalldatasize!!173:bv256
	tacCalldatasize!!316:bv256
	tacCalldatasize!!551:bv256
	tacMCANON3!!287:bytemap
	tacMCANON3!!289:bytemap
	tacMCANON3!!430:bytemap
	tacMCANON3!!432:bytemap
	tacCalldatabuf!!22@3:bytemap
	tacCalldatabuf!!23@9:bytemap
	tacM0x0@2:bv256
	tacM0x0@6:bv256
	tacM0x0@8:bv256
	tacRC@1:bv256
	tacRC@5:bv256
	tacRC@7:bv256
	tacExtcodesize:wordmap
	CANON100:int
	CANON101:bool
	CANON102:bv256
	CANON103:int
	CANON104:bool
	CANON105:bv256
	CANON106:bv256
	CANON107:bv256
	CANON108:bv256
	CANON109:int
	CANON110:bv256
	CANON111:bv256
	CANON112:bool
	CANON113@1:bv256
	CANON113@2:bv256
	CANON113@3:bv256
	CANON113@4:bv256
	CANON113@5:bv256
	CANON113@6:bv256
	CANON113@7:bv256
	CANON113@8:bv256
	CANON113@9:bv256
	CANON113@10:bv256
	CANON114@1:bool
	CANON114@2:bool
	CANON114@3:bool
	CANON114@4:bool
	CANON114@5:bool
	CANON114@6:bool
	CANON114@7:bool
	CANON114@8:bool
	CANON114@9:bool
	CANON114@10:bool
	CANON115:wordmap
	CANON116@1:bool
	CANON116@7:bool
	CANON117@1:bool
	CANON117@7:bool
	CANON118@1:bool
	CANON118@7:bool
	CANON119@1:bv256
	CANON119@7:bv256
	CANON120@1:bv256
	CANON120@7:bv256
	CANON121:wordmap
	CANON122:wordmap
	CANON123:wordmap
	CANON124:bv256
	CANON125:bv256
	CANON126:bv256
	CANON127:wordmap
	CANON128:wordmap
	CANON129:wordmap
	CANON130:wordmap
	CANON131:bv256
	CANON132:bv256
	CANON133:bv256
	CANON134:wordmap
	CANON135:bv256
	CANON136:bv256
	CANON137:bv256
	CANON138:bv256
	CANON139:bv256
	CANON140:bv256
	CANON141:bv256
	CANON142:int
	CANON143:int
	CANON144:int
	CANON145:bool
	CANON146:int
	CANON147:int
	CANON148@1:bool
	CANON148@5:bool
	CANON148@7:bool
	CANON149:bool
	CANON150:bool
	CANON153@2:bv256
	CANON153@3:bv256
	CANON153@4:bv256
	CANON153@6:bv256
	CANON153@8:bv256
	CANON153@9:bv256
	CANON153@10:bv256
	CANON154@1:bv256
	CANON154@7:bv256
	CANON155@1:bv256
	CANON155@7:bv256
	CANON156:int
	CANON157:int
	CANON158:bool
	CANON159:int
	CANON160:bool
	CANON161:bool
	CANON162:bool
	CANON163:bool
	CANON164:bool
	CANON165:bool
	CANON166:int
	CANON167:int
	CANON168:int
	CANON169@1:bool
	CANON169@7:bool
	CANON170@1:bool
	CANON170@7:bool
	CANON171@1:bool
	CANON171@7:bool
	CANON172@1:bv256
	CANON172@7:bv256
	CANON173:bool
	CANON174:int
	CANON175:int
	CANON176:int
	CANON177@1:bool
	CANON177@7:bool
	CANON178:int
	CANON179:bool
	CANON180:int
	CANON181:int
	CANON182:int
	CANON183:int
	CANON184:int
	CANON185:bytemap
	CANON186:bytemap
	CANON187:bv256
	CANON188:bv256
	CANON189:bytemap
	CANON191:bv256
	CANON192:bool
	CANON193:bool
	CANON194:int
	CANON195:bool
	CANON196:bv256
	CANON197:int
	CANON198:bool
	CANON199:bv256
	CANON200:int
	CANON201:bool
	CANON202:bv256
	CANON203:int
	CANON204:bool
	CANON205:bv256
	CANON206:int
	CANON207:bool
	CANON208:bv256
	CANON209:int
	CANON210:bool
	CANON211:bv256
	CANON212:int
	CANON213:bool
	CANON214:bv256
	CANON215@5:bool
	CANON216@5:bool
	CANON217@5:bool
	CANON218@5:bv256
	CANON219@5:bv256
	CANON220:int
	CANON221:int
	CANON222:bool
	CANON223:int
	CANON224:bool
	CANON225:bool
	CANON226:int
	CANON227:int
	CANON228:int
	CANON229:int
	CANON230:int
	CANON231:int
	CANON232:bool
	CANON233:bool
	CANON234:int
	CANON235:bool
	CANON236:bv256
	CANON237:int
	CANON238:bool
	CANON239:bv256
	CANON240:int
	CANON241:bool
	CANON242:bv256
	CANON243:int
	CANON244:bool
	CANON245:bv256
	CANON246:int
	CANON247:bool
	CANON248:bv256
	CANON249:int
	CANON250:bool
	CANON251:bv256
	CANON252:int
	CANON253:bool
	CANON254:bv256
	CANON255:int
	CANON256:int
	CANON257:bool
	CANON258:int
	CANON259:bool
	CANON260:bool
	CANON261:int
	CANON262:int
	CANON263:bool
	CANON264:int
	CANON265:bool
	CANON266:bool
	CANON267:bool
	CANON268:bool
	CANON269:bool
	CANON270:bool
	CANON271:int
	CANON272:int
	CANON273:int
	CANON274:bool
	CANON275:int
	CANON276:int
	CANON277:int
	CANON278:int
	CANON279:bool
	CANON280:bool
	tacMCANON0havocme5388@1:bytemap
	tacMCANON0havocme5389@7:bytemap
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
	tacTimestamp!!200:bv256
	tacTimestamp!!343:bv256
	tacTimestamp!!580:bv256
	tacBalance!!21:wordmap
	tacNumber@1:bv256
	tacNumber@5:bv256
	tacNumber@7:bv256
	CANON56!!24:bv256
	CANON57!!25:bv256
	tacCalldatabuf@1:bytemap
	tacCalldatabuf@3:bytemap
	tacCalldatabuf@5:bytemap
	tacCalldatabuf@7:bytemap
	tacCalldatabuf@9:bytemap
	B26:bool
	B44:bool
	B45:bool
	B46:bool
	B47:bool
	B48:bool
	B49:bool
	B50:bool
	B51:bool
	B52:bool
	B54:bool
	B56:bool
	B58:bool
	B60:bool
	B62:bool
	B64:bool
	B66:bool
	B68:bool
	B70:bool
	B72:bool
	B74:bool
	B76:bool
	B78:bool
	B80:bool
	B82:bool
	B84:bool
	B86:bool
	B88:bool
	B90:bool
	B92:bool
	B94:bool
	B96:bool
	B97:bool
	B98:bool
	B99:bool
	I12:int
	I27:int
	R28:bv256
	R29:bv256
	R30:bv256
	R31:bv256
	R32:bv256
	R33:bv256
	R53:bv256
	R55:bv256
	R57:bv256
	R59:bv256
	R61:bv256
	R63:bv256
	R65:bv256
	R67:bv256
	R69:bv256
	R71:bv256
	R73:bv256
	R75:bv256
	R77:bv256
	R79:bv256
	R81:bv256
	R83:bv256
	R85:bv256
	R87:bv256
	R89:bv256
	R91:bv256
	R93:bv256
	R95:bv256
	B100:bool
	B101:bool
	B102:bool
	B103:bool
	B104:bool
	B105:bool
	B106:bool
	B107:bool
	B108:bool
	B109:bool
	B110:bool
	B111:bool
	B112:bool
	B113:bool
	B114:bool
	B115:bool
	B116:bool
	B117:bool
	B118:bool
	B119:bool
	B120:bool
	B121:bool
	B122:bool
	B123:bool
	B124:bool
	B125:bool
	B126:bool
	B127:bool
	B128:bool
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
	B139:bool
	B140:bool
	B141:bool
	B142:bool
	B143:bool
	B144:bool
	B145:bool
	B146:bool
	B147:bool
	B148:bool
	B149:bool
	B150:bool
	B151:bool
	B152:bool
	B153:bool
	B154:bool
	B155:bool
	B156:bool
	B157:bool
	B158:bool
	B159:bool
	B160:bool
	B161:bool
	B162:bool
	B163:bool
	B164:bool
	B165:bool
	B166:bool
	B174:bool
	B175:bool
	B177:bool
	B180:bool
	B182:bool
	B185:bool
	B188:bool
	B191:bool
	B193:bool
	B196:bool
	B198:bool
	B201:bool
	B203:bool
	B206:bool
	B215:bool
	B218:bool
	B219:bool
	B220:bool
	B221:bool
	B222:bool
	B223:bool
	B224:bool
	B225:bool
	B226:bool
	B227:bool
	B231:bool
	B236:bool
	B237:bool
	B238:bool
	B247:bool
	B248:bool
	B250:bool
	B251:bool
	B252:bool
	B253:bool
	B254:bool
	B256:bool
	B257:bool
	B259:bool
	B260:bool
	B269:bool
	B270:bool
	B273:bool
	B274:bool
	B275:bool
	B276:bool
	B279:bool
	B280:bool
	B281:bool
	B282:bool
	B284:bool
	B285:bool
	B294:bool
	B303:bool
	B304:bool
	B306:bool
	B307:bool
	B308:bool
	B309:bool
	B310:bool
	B311:bool
	B317:bool
	B318:bool
	B320:bool
	B323:bool
	B325:bool
	B328:bool
	B331:bool
	B334:bool
	B336:bool
	B339:bool
	B341:bool
	B344:bool
	B346:bool
	B349:bool
	B358:bool
	B361:bool
	B362:bool
	B363:bool
	B364:bool
	B365:bool
	B366:bool
	B367:bool
	B368:bool
	B369:bool
	B370:bool
	B374:bool
	B379:bool
	B380:bool
	B381:bool
	B390:bool
	B391:bool
	B393:bool
	B394:bool
	B395:bool
	B396:bool
	B397:bool
	B399:bool
	B400:bool
	B402:bool
	B403:bool
	B412:bool
	B413:bool
	B416:bool
	B417:bool
	B418:bool
	B419:bool
	B422:bool
	B423:bool
	B424:bool
	B425:bool
	B427:bool
	B428:bool
	B437:bool
	B446:bool
	B447:bool
	B449:bool
	B450:bool
	B451:bool
	B452:bool
	B453:bool
	B454:bool
	B460:bool
	B477:bool
	B495:bool
	B497:bool
	B498:bool
	B500:bool
	B504:bool
	B510:bool
	B512:bool
	B513:bool
	B515:bool
	B519:bool
	B525:bool
	B526:bool
	B527:bool
	B535:bool
	B536:bool
	B537:bool
	B554:bool
	B555:bool
	B557:bool
	B560:bool
	B562:bool
	B565:bool
	B568:bool
	B571:bool
	B573:bool
	B576:bool
	B578:bool
	B581:bool
	B583:bool
	B586:bool
	B595:bool
	B598:bool
	B600:bool
	B601:bool
	B602:bool
	B603:bool
	B604:bool
	B605:bool
	B607:bool
	B611:bool
	B613:bool
	B618:bool
	B619:bool
	B620:bool
	B629:bool
	B630:bool
	B632:bool
	B633:bool
	B634:bool
	B635:bool
	B636:bool
	B638:bool
	B639:bool
	B641:bool
	B642:bool
	B656:bool
	I167:int
	I168:int
	I169:int
	I170:int
	I171:int
	I172:int
	I176:int
	I181:int
	I187:int
	I192:int
	I197:int
	I202:int
	I205:int
	I211:int
	I295:int
	I296:int
	I297:int
	I319:int
	I324:int
	I330:int
	I335:int
	I340:int
	I345:int
	I348:int
	I354:int
	I438:int
	I439:int
	I440:int
	I501:int
	I502:int
	I507:int
	I516:int
	I517:int
	I522:int
	I544:int
	I545:int
	I546:int
	I547:int
	I548:int
	I556:int
	I561:int
	I567:int
	I572:int
	I577:int
	I582:int
	I585:int
	I591:int
	I649:int
	I650:int
	I651:int
	I652:int
	I653:int
	I654:int
	M549:bytemap
	M552:bytemap
	R178:bv256
	R183:bv256
	R189:bv256
	R194:bv256
	R199:bv256
	R204:bv256
	R207:bv256
	R208:bv256
	R209:bv256
	R210:bv256
	R213:bv256
	R214:bv256
	R217:bv256
	R228:bv256
	R229:bv256
	R230:bv256
	R232:bv256
	R234:bv256
	R235:bv256
	R239:bv256
	R241:bv256
	R243:bv256
	R244:bv256
	R249:bv256
	R255:bv256
	R258:bv256
	R261:bv256
	R263:(uninterp) skey
	R264:bv256
	R265:bv256
	R272:bv256
	R277:bv256
	R278:bv256
	R283:bv256
	R286:bv256
	R288:bv256
	R290:bv256
	R291:bv256
	R292:bv256
	R293:bv256
	R298:bv256
	R299:bv256
	R305:bv256
	R312:bv256
	R313:bv256
	R321:bv256
	R326:bv256
	R332:bv256
	R337:bv256
	R342:bv256
	R347:bv256
	R350:bv256
	R351:bv256
	R352:bv256
	R353:bv256
	R356:bv256
	R357:bv256
	R360:bv256
	R371:bv256
	R372:bv256
	R373:bv256
	R375:bv256
	R377:bv256
	R378:bv256
	R382:bv256
	R384:bv256
	R386:bv256
	R387:bv256
	R392:bv256
	R398:bv256
	R401:bv256
	R404:bv256
	R406:(uninterp) skey
	R407:bv256
	R408:bv256
	R415:bv256
	R420:bv256
	R421:bv256
	R426:bv256
	R429:bv256
	R431:bv256
	R433:bv256
	R434:bv256
	R435:bv256
	R436:bv256
	R441:bv256
	R442:bv256
	R448:bv256
	R455:bv256
	R456:bv256
	R459:bv256
	R461:bv256
	R463:bv256
	R464:bv256
	R466:bv256
	R468:bv256
	R470:bv256
	R472:bv256
	R473:bv256
	R474:bv256
	R476:bv256
	R478:bv256
	R480:bv256
	R481:bv256
	R483:bv256
	R485:bv256
	R487:bv256
	R489:bv256
	R490:bv256
	R491:bv256
	R493:bv256
	R494:bv256
	R496:bv256
	R499:bv256
	R503:bv256
	R505:bv256
	R506:bv256
	R508:bv256
	R509:bv256
	R511:bv256
	R514:bv256
	R518:bv256
	R520:bv256
	R521:bv256
	R523:bv256
	R524:bv256
	R528:bv256
	R530:bv256
	R531:bv256
	R533:bv256
	R534:bv256
	R538:bv256
	R540:bv256
	R541:bv256
	R550:bv256
	R553:bv256
	R558:bv256
	R563:bv256
	R569:bv256
	R574:bv256
	R579:bv256
	R584:bv256
	R587:bv256
	R588:bv256
	R589:bv256
	R590:bv256
	R593:bv256
	R594:bv256
	R599:bv256
	R606:bv256
	R608:bv256
	R609:bv256
	R610:bv256
	R612:bv256
	R614:bv256
	R616:bv256
	R617:bv256
	R621:bv256
	R623:bv256
	R625:bv256
	R626:bv256
	R631:bv256
	R637:bv256
	R640:bv256
	R643:bv256
	R645:(uninterp) skey
	R646:bv256
	R647:bv256
	R655:bv256
	R657:bv256
	R659:bv256
	tacOrigSCANON0:wordmap
	tacOrigSCANON1:wordmap
	tacOrigSCANON2:wordmap
	tacOrigSCANON3:wordmap
	tacOrigSCANON4:bv256
	tacOrigSCANON5:bv256
	tacOrigSCANON6:bv256
	tacOrigSCANON7:wordmap
	tacOrigSCANON8:wordmap
	tacOrigSCANON9:wordmap
	CANON130!!10:wordmap
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
	CANON179!!543:bool
	CANON139!!11:bv256
	tacOrigBalanceCANON0:wordmap
	tacOrigBalanceCANON1:wordmap
	tacOrigBalanceCANON2:wordmap
	CANON115!!8:wordmap
	CANON124!!9:bv256
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
	tacCallvalue!!184:bv256
	tacCallvalue!!327:bv256
	tacCallvalue!!564:bv256
	tacOrigin@1:bv256
	tacOrigin@5:bv256
	tacOrigin@7:bv256
	CANON10:bv256
	CANON11:bool
	CANON12:bv256
	CANON13:bool
	CANON14:bv256
	CANON15:bool
	CANON16:bv256
	CANON17:bool
	CANON18:bv256
	CANON19:bool
	CANON20:bv256
	CANON21:bool
	CANON22:bv256
	CANON23:bool
	CANON24:bv256
	CANON25:bool
	CANON26:bv256
	CANON27:bool
	CANON28:bv256
	CANON29:bool
	CANON30:bv256
	CANON31:bool
	CANON32:bv256
	CANON33:bool
	CANON34:bv256
	CANON35:bool
	CANON36:bv256
	CANON37:bool
	CANON38:bv256
	CANON39:bool
	CANON40:bv256
	CANON41:bool
	CANON42:bv256
	CANON43:bool
	CANON44:bv256
	CANON45:bool
	CANON46:bv256
	CANON47:bool
	CANON48:bv256
	CANON49:bool
	CANON50:bv256
	CANON51:bool
	CANON52:bv256
	CANON53:bool
	CANON54:bool
	CANON55:bool
	CANON56:bv256
	CANON57:bv256
	CANON58:int
	CANON59:int
	CANON60:int
	CANON61:int
	CANON62:int
	CANON63:int
	CANON64:int
	CANON65:int
	CANON66:int
	CANON67:int
	CANON68:int
	CANON69:int
	CANON70:int
	CANON71:int
	CANON72:int
	CANON73:int
	CANON74:bool
	CANON75:bool
	CANON76:int
	CANON77:int
	CANON78:int
	CANON79:int
	CANON80:int
	CANON81:int
	CANON82:int
	CANON83:bool
	CANON84:bool
	CANON85:int
	CANON86:bool
	CANON87:bv256
	CANON88:int
	CANON89:bool
	CANON90:bv256
	CANON91:int
	CANON92:bool
	CANON93:bv256
	CANON94:int
	CANON95:bool
	CANON96:bv256
	CANON97:int
	CANON98:bool
	CANON99:bv256
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
	tacMCANON5!!615:bytemap
	tacMCANON5!!658:bytemap
	tacContractAtCANON0:bv256
	tacContractAtCANON1:bv256
	tacContractAtCANON2:bv256
	tacContractAtCANON3:bv256
	tacContractAtCANON4:bv256
	tacContractAtCANON5:bv256
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
	tacOrigSCANON29:wordmap
	tacOrigSCANON30:wordmap
	tacOrigSCANON31:bv256
	tacOrigSCANON32:bv256
	tacOrigSCANON33:bv256
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
	tacOrigSCANON54:wordmap
	tacOrigSCANON55:wordmap
	tacOrigSCANON56:wordmap
	tacOrigSCANON57:wordmap
	tacOrigSCANON58:bv256
	tacOrigSCANON59:bv256
	tacOrigSCANON60:bv256
	tacOrigSCANON61:wordmap
	tacOrigSCANON62:wordmap
	tacOrigSCANON63:wordmap
	tacOrigSCANON64:wordmap
	tacOrigSCANON65:wordmap
	tacOrigSCANON66:bv256
	tacOrigSCANON67:bv256
	tacOrigSCANON68:bv256
	tacOrigSCANON69:wordmap
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
	tacAddress!!186:bv256
	tacAddress!!246:bv256
	tacAddress!!268:bv256
	tacAddress!!302:bv256
	tacAddress!!329:bv256
	tacAddress!!389:bv256
	tacAddress!!411:bv256
	tacAddress!!445:bv256
	tacAddress!!566:bv256
	tacAddress!!628:bv256
	tacReturndata!!245:bytemap
	tacReturndata!!266:bytemap
	tacReturndata!!300:bytemap
	tacReturndata!!314:bytemap
	tacReturndata!!388:bytemap
	tacReturndata!!409:bytemap
	tacReturndata!!443:bytemap
	tacReturndata!!457:bytemap
	tacReturndata!!475:bytemap
	tacReturndata!!492:bytemap
	tacReturndata!!532:bytemap
	tacReturndata!!542:bytemap
	tacReturndata!!627:bytemap
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
	tacCalldatabuf!!271@3:bytemap
	tacCalldatabuf!!414@9:bytemap
	tacSCANON0:wordmap
	tacSCANON1:wordmap
	tacSCANON2:wordmap
	tacCaller!!179:bv256
	tacCaller!!322:bv256
	tacCaller!!559:bv256
	tacCalldatasize!!0:bv256
	tacCalldatasize!!1:bv256
	tacCalldatasize!!2:bv256
	tacCalldatasize!!3:bv256
	tacCalldatasize!!4:bv256
	tacCalldatasize!!5:bv256
	tacCalldatasize!!6:bv256
	tacMCANON1!!233:bytemap
	tacMCANON1!!376:bytemap
	tacMCANON1!!462:bytemap
	tacMCANON1!!479:bytemap
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
	tacBalance!!212:wordmap
	tacBalance!!216:wordmap
	tacBalance!!355:wordmap
	tacBalance!!359:wordmap
	tacBalance!!592:wordmap
	tacBalance!!596:wordmap
	tacMCANON6!!622:bytemap
	tacMCANON6!!624:bytemap
	tacMCANON6!!648:bytemap
	tacTimestamp@1:bv256
	tacTimestamp@5:bv256
	tacTimestamp@7:bv256
	tacSighash!!34:bv256
	tacSighash!!35:bv256
	tacSighash!!36:bv256
	tacSighash!!37:bv256
	tacSighash!!38:bv256
	tacSighash!!39:bv256
	tacSighash!!40:bv256
	tacSighash!!41:bv256
	tacSighash!!42:bv256
	tacSighash!!43:bv256
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
	tacNumber!!195:bv256
	tacNumber!!338:bv256
	tacNumber!!575:bv256
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
		AssignHavocCmd CANON115!!8:5
		AssignHavocCmd CANON124!!9:6
		AssignHavocCmd CANON130!!10:7
		AssignHavocCmd CANON139!!11:8
		AssignHavocCmd I12
		AssignHavocCmd CANON186:9
		AssignHavocCmd CANON188:10
		AssignExpCmd tacMCANON1!!13:11 ByteMapDefinition(i.5411:bv256 -> 0x0 )
		AssignExpCmd tacMCANON1!!14:12 ByteMapDefinition(i.5412:bv256 -> 0x0 )
		AssignExpCmd tacMCANON2!!15:13 ByteMapDefinition(i.5413:bv256 -> 0x0 )
		AssignExpCmd tacMCANON2!!16:14 ByteMapDefinition(i.5414:bv256 -> 0x0 )
		AssignExpCmd tacMCANON3!!17:15 ByteMapDefinition(i.5415:bv256 -> 0x0 )
		AssignExpCmd tacMCANON3!!18:16 ByteMapDefinition(i.5416:bv256 -> 0x0 )
		AssignExpCmd tacMCANON6!!20:17 ByteMapDefinition(i.5417:bv256 -> 0x0 )
		AssignHavocCmd tacBalance!!21:18
		AssignExpCmd tacCalldatabuf@1:19 ByteMapDefinition(i.5418:bv256 -> Ite(Lt(i.5418 tacCalldatasize@1:3 ) Unconstrained(bv256) 0x0 ) )
		AssignExpCmd tacCalldatabuf!!22@3:20 ByteMapDefinition(i.5419:bv256 -> Ite(Lt(i.5419 tacCalldatasize!!1:3 ) Unconstrained(bv256) 0x0 ) )
		AssignExpCmd tacCalldatabuf@7:21 ByteMapDefinition(i.5420:bv256 -> Ite(Lt(i.5420 tacCalldatasize@7:3 ) Unconstrained(bv256) 0x0 ) )
		AssignExpCmd tacCalldatabuf!!23@9:22 ByteMapDefinition(i.5421:bv256 -> Ite(Lt(i.5421 tacCalldatasize!!5:3 ) Unconstrained(bv256) 0x0 ) )
		AssignHavocCmd CANON56!!24:23
		AssignHavocCmd CANON57!!25:24
		AssignHavocCmd CANON58:25
		AssignHavocCmd CANON59:26
		AssignHavocCmd CANON60:27
		AssignHavocCmd CANON61:28
		AssignHavocCmd CANON62:29
		AssignHavocCmd CANON63:30
		AssignHavocCmd CANON64:31
		AssignHavocCmd CANON65:32
		AssignHavocCmd CANON66:33
		AssignHavocCmd CANON67:34
		AssignHavocCmd CANON68:35
		AssignHavocCmd CANON69:36
		AssignHavocCmd CANON70:37
		AssignHavocCmd CANON71:38
		AssignHavocCmd CANON72:39
		AssignHavocCmd CANON73:40
		AssignHavocCmd B26
		AssignHavocCmd I27
		AssignHavocCmd R28:41
		AssignHavocCmd R29:42
		AssignHavocCmd R30:43
		AssignHavocCmd R31:44
		AssignHavocCmd R32:45
		AssignHavocCmd R33:46
		AssignHavocCmd tacSighash!!34:47
		AssignHavocCmd tacSighash!!35:47
		AssignHavocCmd tacSighash!!36:47
		AssignHavocCmd tacSighash!!37:47
		AssignHavocCmd tacSighash!!38:47
		AssignHavocCmd tacSighash!!39:47
		AssignHavocCmd tacSighash!!40:47
		AssignHavocCmd tacSighash!!41:47
		AssignHavocCmd tacSighash!!42:47
		AssignHavocCmd tacSighash!!43:47
		AssignExpCmd CANON0:48 0x3d24a36b
		AssignExpCmd CANON1:49 false
		AssignExpCmd CANON2:50 true
		AssignExpCmd CANON3:51 false
		AssignExpCmd CANON4:52 0x1
		AssignExpCmd CANON5:53 false
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
		AssignExpCmd B44:54 Gt(Select(tacExtcodesize!!7:4 Apply(to_skey:bif R28:41) ) 0x0 )
		AssumeCmd B44:54
		AssignExpCmd B45:54 Gt(Select(tacExtcodesize!!7:4 Apply(to_skey:bif R29:42) ) 0x0 )
		AssumeCmd B45:54
		AssignExpCmd B46:54 Gt(Select(tacExtcodesize!!7:4 Apply(to_skey:bif R30:43) ) 0x0 )
		AssumeCmd B46:54
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
		AssumeCmd true
		AssumeCmd true
		AssumeCmd true
		AssumeCmd true
		AssumeCmd true
		AssumeCmd true
		AssumeCmd true
		AssumeCmd true
		AssumeCmd true
		AssumeCmd true
		AssumeCmd true
		AssumeCmd true
		AssumeCmd true
		AssumeCmd true
		AssumeCmd true
		AssumeCmd true
		AssumeCmd true
		AssumeCmd true
		AssumeCmd true
		AssumeCmd true
		AssumeCmd true
		AssumeCmd true
		AssumeCmd true
		AssumeCmd true
		AssumeCmd true
		AssumeCmd true
		AssumeCmd true
		AssumeCmd true
		AssumeCmd true
		AssumeCmd true
		AssumeCmd true
		AssumeCmd true
		AnnotationCmd JSON{"key":{"name":"cvl.label.end","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		AnnotationCmd JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Message","s":"assumptions about starting balances"}}
		AssignExpCmd R53:54 Select(tacBalance!!21:18 Apply(to_skey:bif R28:41) )
		NopCmd
		AssumeExpCmd Ge(R53:54 0x0 )
		AssignExpCmd R55:54 Select(tacBalance!!21:18 Apply(to_skey:bif R29:42) )
		NopCmd
		AssumeExpCmd Ge(R55:54 0x0 )
		AssignExpCmd R57:54 Select(tacBalance!!21:18 Apply(to_skey:bif R30:43) )
		NopCmd
		AssumeExpCmd Ge(R57:54 0x0 )
		AssignExpCmd R59:54 Select(tacBalance!!21:18 Apply(to_skey:bif R31:44) )
		NopCmd
		AssumeExpCmd Ge(R59:54 0x0 )
		AssignExpCmd R61:54 Select(tacBalance!!21:18 Apply(to_skey:bif R32:45) )
		NopCmd
		AssumeExpCmd Ge(R61:54 0x0 )
		AssignExpCmd R63:54 Select(tacBalance!!21:18 Apply(skey_basic:bif 0x3) )
		NopCmd
		AssumeExpCmd Ge(R63:54 0x0 )
		AssignExpCmd R65:54 Select(tacBalance!!21:18 Apply(to_skey:bif R33:46) )
		NopCmd
		AssumeExpCmd Ge(R65:54 0x0 )
		AssignExpCmd R67:54 Select(tacBalance!!21:18 Apply(skey_basic:bif 0x5) )
		NopCmd
		AssumeExpCmd Ge(R67:54 0x0 )
		AssignExpCmd R69:54 Select(tacBalance!!21:18 Apply(skey_basic:bif 0x6) )
		NopCmd
		AssumeExpCmd Ge(R69:54 0x0 )
		AssignExpCmd R71:54 Select(tacBalance!!21:18 Apply(skey_basic:bif 0x7) )
		NopCmd
		AssumeExpCmd Ge(R71:54 0x0 )
		AssignExpCmd R73:54 Select(tacBalance!!21:18 Apply(skey_basic:bif 0x8) )
		NopCmd
		AssumeExpCmd Ge(R73:54 0x0 )
		AssignExpCmd R75:54 Select(tacBalance!!21:18 Apply(skey_basic:bif 0xf4) )
		NopCmd
		AssumeExpCmd Ge(R75:54 0x0 )
		AssignExpCmd R77:54 Select(tacBalance!!21:18 Apply(skey_basic:bif 0xf5) )
		NopCmd
		AssumeExpCmd Ge(R77:54 0x0 )
		AssignExpCmd R79:54 Select(tacBalance!!21:18 Apply(skey_basic:bif 0xf6) )
		NopCmd
		AssumeExpCmd Ge(R79:54 0x0 )
		AssignExpCmd R81:54 Select(tacBalance!!21:18 Apply(skey_basic:bif 0xf7) )
		NopCmd
		AssumeExpCmd Ge(R81:54 0x0 )
		AssignExpCmd R83:54 Select(tacBalance!!21:18 Apply(skey_basic:bif 0xf8) )
		NopCmd
		AssumeExpCmd Ge(R83:54 0x0 )
		AssignExpCmd R85:54 Select(tacBalance!!21:18 Apply(skey_basic:bif 0xf9) )
		NopCmd
		AssumeExpCmd Ge(R85:54 0x0 )
		AssignExpCmd R87:54 Select(tacBalance!!21:18 Apply(skey_basic:bif 0xfa) )
		NopCmd
		AssumeExpCmd Ge(R87:54 0x0 )
		AssignExpCmd R89:54 Select(tacBalance!!21:18 Apply(skey_basic:bif 0xfb) )
		NopCmd
		AssumeExpCmd Ge(R89:54 0x0 )
		AssignExpCmd R91:54 Select(tacBalance!!21:18 Apply(skey_basic:bif 0xfc) )
		NopCmd
		AssumeExpCmd Ge(R91:54 0x0 )
		AssignExpCmd R93:54 Select(tacBalance!!21:18 Apply(skey_basic:bif 0xfd) )
		NopCmd
		AssumeExpCmd Ge(R93:54 0x0 )
		AssignExpCmd R95:54 Select(tacBalance!!21:18 Apply(skey_basic:bif 0xfe) )
		NopCmd
		AssumeExpCmd Ge(R95:54 0x0 )
		AnnotationCmd JSON{"key":{"name":"cvl.label.end","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		AnnotationCmd JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Message","s":"assumptions about static addresses"}}
		AnnotationCmd JSON{"key":{"name":"cvl.label.end","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		AnnotationCmd JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Message","s":"assumptions about uniqueness of contracts' addressses"}}
		NopCmd
		AssumeExpCmd LNot(Eq(R28:41 R29:42 ) )
		NopCmd
		AssumeExpCmd LNot(Eq(R28:41 R30:43 ) )
		NopCmd
		AssumeExpCmd LNot(Eq(R28:41 0x3 ) )
		NopCmd
		AssumeExpCmd LNot(Eq(R28:41 0x5 ) )
		NopCmd
		AssumeExpCmd LNot(Eq(R28:41 0x6 ) )
		NopCmd
		AssumeExpCmd LNot(Eq(R28:41 0x7 ) )
		NopCmd
		AssumeExpCmd LNot(Eq(R28:41 0x8 ) )
		NopCmd
		AssumeExpCmd LNot(Eq(R28:41 0xf4 ) )
		NopCmd
		AssumeExpCmd LNot(Eq(R28:41 0xf5 ) )
		NopCmd
		AssumeExpCmd LNot(Eq(R28:41 0xf6 ) )
		NopCmd
		AssumeExpCmd LNot(Eq(R28:41 0xf7 ) )
		NopCmd
		AssumeExpCmd LNot(Eq(R28:41 0xf8 ) )
		NopCmd
		AssumeExpCmd LNot(Eq(R28:41 0xf9 ) )
		NopCmd
		AssumeExpCmd LNot(Eq(R28:41 0xfa ) )
		NopCmd
		AssumeExpCmd LNot(Eq(R28:41 0xfb ) )
		NopCmd
		AssumeExpCmd LNot(Eq(R28:41 0xfc ) )
		NopCmd
		AssumeExpCmd LNot(Eq(R28:41 0xfd ) )
		NopCmd
		AssumeExpCmd LNot(Eq(R28:41 0xfe ) )
		NopCmd
		AssumeExpCmd LNot(Eq(R29:42 R30:43 ) )
		NopCmd
		AssumeExpCmd LNot(Eq(R29:42 0x3 ) )
		NopCmd
		AssumeExpCmd LNot(Eq(R29:42 0x5 ) )
		NopCmd
		AssumeExpCmd LNot(Eq(R29:42 0x6 ) )
		NopCmd
		AssumeExpCmd LNot(Eq(R29:42 0x7 ) )
		NopCmd
		AssumeExpCmd LNot(Eq(R29:42 0x8 ) )
		NopCmd
		AssumeExpCmd LNot(Eq(R29:42 0xf4 ) )
		NopCmd
		AssumeExpCmd LNot(Eq(R29:42 0xf5 ) )
		NopCmd
		AssumeExpCmd LNot(Eq(R29:42 0xf6 ) )
		NopCmd
		AssumeExpCmd LNot(Eq(R29:42 0xf7 ) )
		NopCmd
		AssumeExpCmd LNot(Eq(R29:42 0xf8 ) )
		NopCmd
		AssumeExpCmd LNot(Eq(R29:42 0xf9 ) )
		NopCmd
		AssumeExpCmd LNot(Eq(R29:42 0xfa ) )
		NopCmd
		AssumeExpCmd LNot(Eq(R29:42 0xfb ) )
		NopCmd
		AssumeExpCmd LNot(Eq(R29:42 0xfc ) )
		NopCmd
		AssumeExpCmd LNot(Eq(R29:42 0xfd ) )
		NopCmd
		AssumeExpCmd LNot(Eq(R29:42 0xfe ) )
		NopCmd
		AssumeExpCmd LNot(Eq(R30:43 0x3 ) )
		NopCmd
		AssumeExpCmd LNot(Eq(R30:43 0x5 ) )
		NopCmd
		AssumeExpCmd LNot(Eq(R30:43 0x6 ) )
		NopCmd
		AssumeExpCmd LNot(Eq(R30:43 0x7 ) )
		NopCmd
		AssumeExpCmd LNot(Eq(R30:43 0x8 ) )
		NopCmd
		AssumeExpCmd LNot(Eq(R30:43 0xf4 ) )
		NopCmd
		AssumeExpCmd LNot(Eq(R30:43 0xf5 ) )
		NopCmd
		AssumeExpCmd LNot(Eq(R30:43 0xf6 ) )
		NopCmd
		AssumeExpCmd LNot(Eq(R30:43 0xf7 ) )
		NopCmd
		AssumeExpCmd LNot(Eq(R30:43 0xf8 ) )
		NopCmd
		AssumeExpCmd LNot(Eq(R30:43 0xf9 ) )
		NopCmd
		AssumeExpCmd LNot(Eq(R30:43 0xfa ) )
		NopCmd
		AssumeExpCmd LNot(Eq(R30:43 0xfb ) )
		NopCmd
		AssumeExpCmd LNot(Eq(R30:43 0xfc ) )
		NopCmd
		AssumeExpCmd LNot(Eq(R30:43 0xfd ) )
		NopCmd
		AssumeExpCmd LNot(Eq(R30:43 0xfe ) )
		AssumeCmd true
		AssumeCmd true
		AssumeCmd true
		AssumeCmd true
		AssumeCmd true
		AssumeCmd true
		AssumeCmd true
		AssumeCmd true
		AssumeCmd true
		AssumeCmd true
		AssumeCmd true
		AssumeCmd true
		AssumeCmd true
		AssumeCmd true
		AssumeCmd true
		AssumeCmd true
		AssumeCmd true
		AssumeCmd true
		AssumeCmd true
		AssumeCmd true
		AssumeCmd true
		AssumeCmd true
		AssumeCmd true
		AssumeCmd true
		AssumeCmd true
		AssumeCmd true
		AssumeCmd true
		AssumeCmd true
		AssumeCmd true
		AssumeCmd true
		AssumeCmd true
		AssumeCmd true
		AssumeCmd true
		AssumeCmd true
		AssumeCmd true
		AssumeCmd true
		AssumeCmd true
		AssumeCmd true
		AssumeCmd true
		AssumeCmd true
		AssumeCmd true
		AssumeCmd true
		AssumeCmd true
		AssumeCmd true
		AssumeCmd true
		AssumeCmd true
		AssumeCmd true
		AssumeCmd true
		AssumeCmd true
		AssumeCmd true
		AssumeCmd true
		AssumeCmd true
		AssumeCmd true
		AssumeCmd true
		AssumeCmd true
		AssumeCmd true
		AssumeCmd true
		AssumeCmd true
		AssumeCmd true
		AssumeCmd true
		AssumeCmd true
		AssumeCmd true
		AssumeCmd true
		AssumeCmd true
		AssumeCmd true
		AssumeCmd true
		AssumeCmd true
		AssumeCmd true
		AssumeCmd true
		AssumeCmd true
		AssumeCmd true
		AssumeCmd true
		AssumeCmd true
		AssumeCmd true
		AssumeCmd true
		AssumeCmd true
		AssumeCmd true
		AssumeCmd true
		AssumeCmd true
		AssumeCmd true
		AssumeCmd true
		AssumeCmd true
		AssumeCmd true
		AssumeCmd true
		AssumeCmd true
		AssumeCmd true
		AssumeCmd true
		AssumeCmd true
		AssumeCmd true
		AssumeCmd true
		AssumeCmd true
		AssumeCmd true
		AssumeCmd true
		AssumeCmd true
		AssumeCmd true
		AssumeCmd true
		AssumeCmd true
		AssumeCmd true
		AssumeCmd true
		AssumeCmd true
		AssumeCmd true
		AssumeCmd true
		AssumeCmd true
		AssumeCmd true
		AssumeCmd true
		AssumeCmd true
		AssumeCmd true
		AssumeCmd true
		AssumeCmd true
		AssumeCmd true
		AssumeCmd true
		AssumeCmd true
		AssumeCmd true
		AssumeCmd true
		AssumeCmd true
		AssumeCmd true
		AssumeCmd true
		AssumeCmd true
		AssumeCmd true
		AssumeCmd true
		AnnotationCmd JSON{"key":{"name":"cvl.label.end","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		NopCmd
		AssumeExpCmd Eq(CANON56!!24:23 R29:42 )
		NopCmd
		AssumeExpCmd Eq(CANON57!!25:24 R28:41 )
		AnnotationCmd JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Message","s":"record starting nonces"}}
		AnnotationCmd JSON{"key":{"name":"cvl.label.end","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		AnnotationCmd JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Message","s":"cloned contracts have no balances"}}
		AnnotationCmd JSON{"key":{"name":"cvl.label.end","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		AnnotationCmd JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Message","s":"Linked immutable setup"}}
		AnnotationCmd JSON{"key":{"name":"cvl.label.end","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		AnnotationCmd JSON{"key":{"name":"cvl.label.end","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		NopCmd
		AssumeExpCmd LAnd(Le(CANON58:25 0xffffffffffffffffffffffffffffffffffffffff ) Ge(CANON58:25 0x0 ) )
		NopCmd
		AssumeExpCmd LAnd(Le(CANON59:26 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff ) Ge(CANON59:26 0x0 ) )
		NopCmd
		AssumeExpCmd LAnd(Le(CANON60:27 0xffffffffffffffffffffffffffffffffffffffff ) Ge(CANON60:27 0x0 ) )
		NopCmd
		AssumeExpCmd LAnd(Le(CANON61:28 0xffffffffffffffffffffffffffffffffffffffff ) Ge(CANON61:28 0x0 ) )
		NopCmd
		AssumeExpCmd LAnd(Le(CANON62:29 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff ) Ge(CANON62:29 0x0 ) )
		NopCmd
		AssumeExpCmd LAnd(Le(CANON63:30 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff ) Ge(CANON63:30 0x0 ) )
		NopCmd
		AssumeExpCmd LAnd(Le(CANON64:31 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff ) Ge(CANON64:31 0x0 ) )
		NopCmd
		AssumeExpCmd LAnd(Le(CANON65:32 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff ) Ge(CANON65:32 0x0 ) )
		NopCmd
		AssumeExpCmd LAnd(Le(CANON66:33 0xffffffffffffffffffffffffffffffffffffffff ) Ge(CANON66:33 0x0 ) )
		NopCmd
		AssumeExpCmd LAnd(Le(CANON67:34 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff ) Ge(CANON67:34 0x0 ) )
		NopCmd
		AssumeExpCmd LAnd(Le(CANON68:35 0xffffffffffffffffffffffffffffffffffffffff ) Ge(CANON68:35 0x0 ) )
		NopCmd
		AssumeExpCmd LAnd(Le(CANON69:36 0xffffffffffffffffffffffffffffffffffffffff ) Ge(CANON69:36 0x0 ) )
		NopCmd
		AssumeExpCmd LAnd(Le(CANON70:37 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff ) Ge(CANON70:37 0x0 ) )
		NopCmd
		AssumeExpCmd LAnd(Le(CANON71:38 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff ) Ge(CANON71:38 0x0 ) )
		NopCmd
		AssumeExpCmd LAnd(Le(CANON72:39 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff ) Ge(CANON72:39 0x0 ) )
		NopCmd
		AssumeExpCmd LAnd(Le(CANON73:40 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff ) Ge(CANON73:40 0x0 ) )
		AnnotationCmd:55 JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Cmd","cmd":{"cmd_type":"spec.cvlast.CVLCmd.Simple.AssumeCmd.Assume","cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/specs/ViewReentrancy.spec","start":{"line":25,"character":4},"end":{"line":25,"character":17}},"exp":{"#class":"spec.cvlast.CVLExp.VariableExp","id":"cond","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":0}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"},"cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/specs/ViewReentrancy.spec","start":{"line":25,"character":4},"end":{"line":25,"character":17}}},"twoStateIndex":"NEITHER"},"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":0}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}}}}}
		AssumeCmd:55 B26
		AnnotationCmd:55 JSON{"key":{"name":"cvl.label.end","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		AnnotationCmd:56 JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Cmd","cmd":{"cmd_type":"spec.cvlast.CVLCmd.Simple.AssumeCmd.Assume","cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/specs/ViewReentrancy.spec","start":{"line":26,"character":4},"end":{"line":26,"character":56}},"exp":{"#class":"spec.cvlast.CVLExp.RelopExp.EqExp","l":{"#class":"spec.cvlast.CVLExp.VariableExp","id":"before_func1","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":0}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256},"cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/specs/ViewReentrancy.spec","start":{"line":26,"character":4},"end":{"line":26,"character":56}}},"twoStateIndex":"NEITHER"},"r":{"#class":"spec.cvlast.CVLExp.ApplyExp.ContractFunction.Concrete","methodIdWithCallContext":{"#class":"spec.cvlast.ConcreteMethod","signature":{"#class":"spec.cvlast.ExternalQualifiedMethodSignature.ExternalQualifiedMethodSig","wrapped":{"#class":"spec.cvlast.QualifiedMethodSignature.QualifiedMethodSig","qualifiedMethodName":{"#class":"spec.cvlast.QualifiedFunction","host":{"name":"curve"},"methodId":"getVirtualPrice"},"params":[],"res":[{"#class":"spec.cvlast.VMParam.Unnamed","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256}}]},"sighashInt":{"n":"e25aa5fa"}}},"args":[{"#class":"spec.cvlast.CVLExp.VariableExp","id":"e_external","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":0}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"env","fields":[{"fieldName":"msg","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"msg","fields":[{"fieldName":"sender","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"value","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}}]}},{"fieldName":"tx","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"tx","fields":[{"fieldName":"origin","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}}]}},{"fieldName":"block","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"block","fields":[{"fieldName":"coinbase","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"difficulty","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"gaslimit","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"number","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"timestamp","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}}]}}]},"cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/specs/ViewReentrancy.spec","start":{"line":26,"character":4},"end":{"line":26,"character":56}}},"twoStateIndex":"NEITHER"}],"noRevert":true,"storage":{"#class":"spec.cvlast.CVLExp.VariableExp","id":"lastStorage","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":0}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.VMInternal.BlockchainState"},"cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/specs/ViewReentrancy.spec","start":{"line":26,"character":4},"end":{"line":26,"character":56}}},"twoStateIndex":"NEITHER"},"isWhole":false,"tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":0}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.VM","descriptor":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256},"context":{"#class":"spec.cvlast.typedescriptors.FromVMContext.ReturnValue"}},"cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/specs/ViewReentrancy.spec","start":{"line":26,"character":28},"end":{"line":26,"character":43}},"annotation":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.CallResolution$DirectPassing","target":{"methodSignature":{"#class":"spec.cvlast.ExternalQualifiedMethodSignature.ExternalQualifiedMethodSig","wrapped":{"#class":"spec.cvlast.QualifiedMethodSignature.QualifiedMethodSig","qualifiedMethodName":{"#class":"spec.cvlast.QualifiedFunction","host":{"name":"curve"},"methodId":"getVirtualPrice"},"params":[],"res":[{"#class":"spec.cvlast.VMParam.Unnamed","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256}}]},"sighashInt":{"n":"e25aa5fa"}},"definitelyNonPayable":true,"annotation":{"visibility":"EXTERNAL","envFree":false,"library":false},"stateMutability":"view","tag":{"#class":"spec.cvlast.CVLImportedFunctionTag.WithMethodInfo","evmMethodInfo":{"sigHash":"e25aa5fa","name":"getVirtualPrice","argTypes":[],"resultTypes":[{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256}],"stateMutability":"view","envfreeInfo":{"#class":"bridge.EnvfreeInfo.Unknown"},"isConstant":false,"isLibrary":false}}},"hasEnv":true}}},"tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":0}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"},"cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/specs/ViewReentrancy.spec","start":{"line":26,"character":12},"end":{"line":26,"character":55}}}},"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":0}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}}}}}
		NopCmd
		NopCmd
		NopCmd
		NopCmd
		NopCmd
	}
	Block 0_0_0_1_0_0 Succ [0_0_0_2_0_0] {
		AnnotationCmd:56 JSON{"key":{"name":"call.trace.push","type":"analysis.icfg.Inliner$CallStack$PushRecord","erasureStrategy":"Canonical"},"value":"rO0ABXNyACphbmFseXNpcy5pY2ZnLklubGluZXIkQ2FsbFN0YWNrJFB1c2hSZWNvcmSX8+DCTLCH+AIAA0kACGNhbGxlZUlkTAAGY2FsbGVldAATTHZjL2RhdGEvTWV0aG9kUmVmO0wAB3N1bW1hcnl0ABVMdmMvZGF0YS9DYWxsU3VtbWFyeTt4cAAAAAFzcgARdmMuZGF0YS5NZXRob2RSZWbJlJTzzU9pGAIAA0wABGF0dHJ0ABdMc2NlbmUvTWV0aG9kQXR0cmlidXRlO0wACmNvbnRyYWN0SWR0ABZMamF2YS9tYXRoL0JpZ0ludGVnZXI7TAAHc2lnSGFzaHQAEExldm0vU2lnaGFzaEludDt4cHNyABxzY2VuZS5NZXRob2RBdHRyaWJ1dGUkQ29tbW9uNHjdebdr9XMCAAB4cgAVc2NlbmUuTWV0aG9kQXR0cmlidXRlcYg2pYWutuUCAAB4cHNyABRqYXZhLm1hdGguQmlnSW50ZWdlcoz8nx+pO/sdAwAGSQAIYml0Q291bnRJAAliaXRMZW5ndGhJABNmaXJzdE5vbnplcm9CeXRlTnVtSQAMbG93ZXN0U2V0Qml0SQAGc2lnbnVtWwAJbWFnbml0dWRldAACW0J4cgAQamF2YS5sYW5nLk51bWJlcoaslR0LlOCLAgAAeHD///////////////7////+AAAAAXVyAAJbQqzzF/gGCFTgAgAAeHAAAAAQzkYEoAAAAAAAAAAAAAAAF3hzcgAOZXZtLlNpZ2hhc2hJbnRUdcqNMXEgeAIAAUwAAW5xAH4ABnhwc3EAfgAM///////////////+/////gAAAAF1cQB+ABAAAAAE4lql+nhw"}
		AssignHavocCmd:56 tacCalldatasize!!173:3
		NopCmd
		AssumeExpCmd Apply(add_noofl:bif 0x4 0x0)
		NopCmd
		AssumeExpCmd Eq(0x4 tacCalldatasize!!173:3 )
		AssignExpCmd:56 B177 LAnd(Ge(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff CANON66:33 ) Le(0x0 CANON66:33 ) )
		AssertCmd:56 B177 "sanity bounds check on cvl to vm encoding of tacTmp!4760:int failed"
		AssignExpCmd:56 R178:54 Apply(safe_math_narrow:bif CANON66:33)
		NopCmd
		AssumeExpCmd LAnd(Le(R178:57 0xffffffffffffffffffffffffffffffffffffffff ) Ge(R178:57 0x0 ) )
		AssignExpCmd:56 B182 LAnd(Ge(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff CANON67:34 ) Le(0x0 CANON67:34 ) )
		AssertCmd:56 B182 "sanity bounds check on cvl to vm encoding of tacTmp!4763:int failed"
		AssignExpCmd:56 R183:54 Apply(safe_math_narrow:bif CANON67:34)
		NopCmd
		AssumeExpCmd LAnd(Le(R183:58 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff ) Ge(R183:58 0x0 ) )
		AssignExpCmd:56 B188 LAnd(Ge(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff CANON68:35 ) Le(0x0 CANON68:35 ) )
		AssertCmd:56 B188 "sanity bounds check on cvl to vm encoding of tacTmp!4767:int failed"
		AssignExpCmd:56 R189:54 Apply(safe_math_narrow:bif CANON68:35)
		NopCmd
		AssumeExpCmd LAnd(Le(R189:59 0xffffffffffffffffffffffffffffffffffffffff ) Ge(R189:59 0x0 ) )
		AssignExpCmd:56 B193 LAnd(Ge(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff CANON72:39 ) Le(0x0 CANON72:39 ) )
		AssertCmd:56 B193 "sanity bounds check on cvl to vm encoding of tacTmp!4770:int failed"
		AssignExpCmd:56 R194:54 Apply(safe_math_narrow:bif CANON72:39)
		NopCmd
		AssumeExpCmd LAnd(Le(R194:60 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff ) Ge(R194:60 0x0 ) )
		AssignExpCmd:56 B198 LAnd(Ge(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff CANON73:40 ) Le(0x0 CANON73:40 ) )
		AssertCmd:56 B198 "sanity bounds check on cvl to vm encoding of tacTmp!4773:int failed"
		AssignExpCmd:56 R199:54 Apply(safe_math_narrow:bif CANON73:40)
		NopCmd
		AssumeExpCmd LAnd(Le(R199:61 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff ) Ge(R199:61 0x0 ) )
		AssignExpCmd:56 B203 LAnd(Ge(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff CANON67:34 ) Le(0x0 CANON67:34 ) )
		AssertCmd:56 B203 "sanity bounds check on cvl to vm encoding of tacTmp!4776:int failed"
		AssignExpCmd:56 R204:54 Apply(safe_math_narrow:bif CANON67:34)
		AssignExpCmd:56 B206 LAnd(Ge(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff CANON66:33 ) Le(0x0 CANON66:33 ) )
		AssertCmd:56 B206 "sanity bounds check on cvl to vm encoding of tacTmp!4779:int failed"
		AssignExpCmd:56 R207:54 Apply(safe_math_narrow:bif CANON66:33)
		AssignExpCmd:56 R210:54 Select(tacBalance!!21:18 Apply(to_skey:bif R207:54) )
		AssignExpCmd:62 I211:54 IntSub(R210:54 R204:54 )
		AssignExpCmd:62 tacBalance!!212:18 Store(tacBalance!!21:18 Apply(to_skey:bif R207:54) I211:54 )
		AssignExpCmd:56 R213:54 Select(tacBalance!!212:18 Apply(to_skey:bif R30:43) )
		AssignExpCmd:62 R214:54 Add(R213:54 R204:54)
		NopCmd
		AssumeExpCmd Apply(add_noofl:bif R213:54 R204:54)
		AssignExpCmd:62 tacBalance!!216:18 Store(tacBalance!!212:18 Apply(to_skey:bif R30:43) R214:54 )
		AnnotationCmd:56 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.BalanceSnippet","srcAccountInfo":{"old":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R210","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}]},"new":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"I211","tag":{"#class":"tac.Tag.Int"},"callIndex":0,"meta":[{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}]},"addr":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R207","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}]}},"trgAccountInfo":{"old":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R213","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}]},"new":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R214","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}]},"addr":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R30","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"tacContractAt"},{"key":{"name":"tac.contract.sym.addr.name","type":"java.lang.String","erasureStrategy":"Erased"},"value":"curve"},{"key":{"name":"tac.contract.sym.addr","type":"java.math.BigInteger","erasureStrategy":"Erased"},"value":"ce4604a0000000000000000000000017"}]}},"transferredAmount":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R204","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}]}}}
		LabelCmd:56 "Start procedure curve-getVirtualPrice()"
		AnnotationCmd:56 JSON{"key":{"name":"fps.free-pointer-is-scalarized","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true}
		AssignExpCmd:56 R217:54 Select(tacExtcodesize!!7:4 Apply(to_skey:bif R30:63) )
		NopCmd
		AssumeExpCmd Gt(R217:54 0x0 )
		AnnotationCmd:56 JSON{"key":{"name":"internal.func.finder.info","type":"analysis.ip.InternalFunctionFinderReport","erasureStrategy":"Erased"},"value":"rO0ABXNyAChhbmFseXNpcy5pcC5JbnRlcm5hbEZ1bmN0aW9uRmluZGVyUmVwb3J0ian+bYn1VdACAAFMABN1bnJlc29sdmVkRnVuY3Rpb25zdAAPTGphdmEvdXRpbC9TZXQ7eHBzcgAhZGF0YXN0cnVjdHVyZXMuTGlua2VkQXJyYXlIYXNoU2V0AAAAAAAAAAEDAAJGAApsb2FkRmFjdG9yTAAJaGFzaFRhYmxldAAuTGRhdGFzdHJ1Y3R1cmVzL2FycmF5aGFzaHRhYmxlL0FycmF5SGFzaFRhYmxlO3hwdwgAAAAAQAAAAHg="}
		AnnotationCmd:56 JSON{"key":{"name":"fps.free-pointer-is-scalarized","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true}
		NopCmd
		AssumeExpCmd Eq(R183:54 0x0 )
		NopCmd
		AssumeExpCmd LNot(Lt(tacCalldatasize!!173:3 0x4 ) )
		NopCmd
		AssumeExpCmd LNot(Gt(0x82c63066 tacSighash!!34:47 ) )
		NopCmd
		AssumeExpCmd LNot(Eq(0x82c63066 tacSighash!!34:47 ) )
		NopCmd
		AssumeExpCmd LNot(Eq(0x89295a45 tacSighash!!34:47 ) )
		NopCmd
		AssumeExpCmd LNot(Eq(0x9d1e1f25 tacSighash!!34:47 ) )
		NopCmd
		AssumeExpCmd LNot(Eq(0xac8c9059 tacSighash!!34:47 ) )
		NopCmd
		AssumeExpCmd LNot(Eq(0xd802e4f7 tacSighash!!34:47 ) )
		NopCmd
		AssumeExpCmd Eq(0xe25aa5fa tacSighash!!34:47 )
		AnnotationCmd:56 JSON{"key":{"name":"internal.func.start","type":"analysis.ip.InternalFuncStartAnnotation","erasureStrategy":"CallTrace"},"value":{"id":0,"startPc":2909,"args":[],"methodSignature":{"#class":"spec.cvlast.QualifiedMethodSignature.QualifiedMethodSig","qualifiedMethodName":{"#class":"spec.cvlast.QualifiedFunction","host":{"name":"curve"},"methodId":"getVirtualPrice"},"params":[],"res":[{"#class":"spec.cvlast.VMParam.Unnamed","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256}}]},"stackOffsetToArgPos":{},"callSiteSrc":{"source":0,"begin":6452,"len":476,"jumpType":"ENTER","address":"ce4604a0000000000000000000000017","sourceContext":{"indexToFilepath":{"0":"contracts/curve.sol","1":"Context.sol","2":"ERC20.sol","3":"IERC20.sol","4":"IERC20Metadata.sol","5":"ReentrancyGuard.sol"},"sourceDir":".post_autofinders.1"}}}}
		AnnotationCmd:56 JSON{"key":{"name":"pta.end-allocation","type":"analysis.alloc.AllocationAnalysis$AbstractLocation","erasureStrategy":"Erased"},"value":{"prevFPWriteIdx":0,"nextFPWriteCmd":{"block":{"#class":"tac.BlockIdentifier","origStartPc":16,"stkTop":1024,"decompCopy":0,"calleeIdx":0,"topOfStackValue":2,"freshCopy":0},"pos":34},"sort":{"#class":"analysis.alloc.AllocationAnalysis.Alloc.ConstBlock","sz":"40"}}}
		AssignExpCmd:64 R229:65 Select(CANON115!!8:5 Apply(skey_basic:bif 0x8) )
		AnnotationCmd:56 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet","value":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R229","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1012}]},"displayPath":{"#class":"analysis.storage.DisplayPath.ArrayAccess","index":{"#class":"vc.data.TACSymbol.Const","value":"0"},"base":{"#class":"analysis.storage.DisplayPath.Root","name":"admin_balances"}},"storageType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256},"contractInstance":"ce4604a0000000000000000000000017","linkableStorageReadId":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet.None"}}}
		AssignExpCmd:66 R230:67 Select(tacBalance!!216:18 Apply(to_skey:bif R30:63) )
		NopCmd
		AssumeExpCmd LNot(Lt(R230:67 R229:65 ) )
		AssignExpCmd:68 R232:69 Sub(R230:67 R229:65 )
		AssignExpCmd:70 tacMCANON1!!233:11 Store(tacMCANON1!!13:11 0xc0 R232:69 )
		AssignExpCmd:71 R234:72 Select(CANON115!!8:5 Apply(skey_basic:bif 0x9) )
		AnnotationCmd:56 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet","value":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R234","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1013}]},"displayPath":{"#class":"analysis.storage.DisplayPath.ArrayAccess","index":{"#class":"vc.data.TACSymbol.Const","value":"1"},"base":{"#class":"analysis.storage.DisplayPath.Root","name":"admin_balances"}},"storageType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256},"contractInstance":"ce4604a0000000000000000000000017","linkableStorageReadId":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet.None"}}}
		AssignExpCmd:56 B236:54 Le(CANON56!!24:73 0xffffffffffffffffffffffffffffffffffffffff )
		AssignExpCmd:56 B237:54 Ge(CANON56!!24:73 0x0 )
		NopCmd
		AssumeExpCmd LAnd(B236:54 B237:54 )
		AnnotationCmd:56 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet","value":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"CANON56!!24","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.scalarization.sort","type":"vc.data.ScalarizationSort","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.ScalarizationSort.Packed","packedStart":{"#class":"vc.data.ScalarizationSort.Split","idx":"b"},"start":0}},{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.storage.bit-width","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":160},{"key":{"name":"tac.storage.pretty.paths","type":"analysis.storage.DisplayPaths","erasureStrategy":"Erased"},"value":{"paths":[{"#class":"analysis.storage.DisplayPath.Root","name":"coins_1"}]}},{"key":{"name":"tac.slot.type","type":"spec.cvlast.typedescriptors.EVMTypeDescriptor$EVMValueType","erasureStrategy":"Canonical"},"value":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.address"}},{"key":{"name":"tac.storage.non-indexed-path","type":"analysis.storage.StorageAnalysisResult$NonIndexedPath","erasureStrategy":"Canonical"},"value":{"#class":"analysis.storage.StorageAnalysisResult.NonIndexedPath.Root","slot":"b"}},{"key":{"name":"tac.storage","type":"java.math.BigInteger","erasureStrategy":"Canonical"},"value":"ce4604a0000000000000000000000017"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1011}]},"displayPath":{"#class":"analysis.storage.DisplayPath.Root","name":"coins_1"},"storageType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.address"},"contractInstance":"ce4604a0000000000000000000000017","linkableStorageReadId":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet.Id","id":0}}}
		AnnotationCmd:56 JSON{"key":{"name":"init.reorder.fence","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		AssignExpCmd:74 tacMCANON2!!240:13 Store(tacMCANON2!!15:13 0x100 0x70a0823100000000000000000000000000000000000000000000000000000000 )
		AssignExpCmd:75 tacMCANON2!!242:13 Store(tacMCANON2!!240:13 0x104 R30:43 )
		AssignExpCmd:74 R243:76 0x100
		AssignHavocCmd:74 R244:77
		AssignHavocCmd:56 tacReturndata!!245:78
		JumpCmd:56 0_0_0_2_0_0
	}
	Block 0_0_0_2_0_0 Succ [1_0_0_1_0_0] {
		AnnotationCmd:56 JSON{"key":{"name":"call.trace.push","type":"analysis.icfg.Inliner$CallStack$PushRecord","erasureStrategy":"Canonical"},"value":"rO0ABXNyACphbmFseXNpcy5pY2ZnLklubGluZXIkQ2FsbFN0YWNrJFB1c2hSZWNvcmSX8+DCTLCH+AIAA0kACGNhbGxlZUlkTAAGY2FsbGVldAATTHZjL2RhdGEvTWV0aG9kUmVmO0wAB3N1bW1hcnl0ABVMdmMvZGF0YS9DYWxsU3VtbWFyeTt4cAAAAAJzcgARdmMuZGF0YS5NZXRob2RSZWbJlJTzzU9pGAIAA0wABGF0dHJ0ABdMc2NlbmUvTWV0aG9kQXR0cmlidXRlO0wACmNvbnRyYWN0SWR0ABZMamF2YS9tYXRoL0JpZ0ludGVnZXI7TAAHc2lnSGFzaHQAEExldm0vU2lnaGFzaEludDt4cHNyABxzY2VuZS5NZXRob2RBdHRyaWJ1dGUkQ29tbW9uNHjdebdr9XMCAAB4cgAVc2NlbmUuTWV0aG9kQXR0cmlidXRlcYg2pYWutuUCAAB4cHNyABRqYXZhLm1hdGguQmlnSW50ZWdlcoz8nx+pO/sdAwAGSQAIYml0Q291bnRJAAliaXRMZW5ndGhJABNmaXJzdE5vbnplcm9CeXRlTnVtSQAMbG93ZXN0U2V0Qml0SQAGc2lnbnVtWwAJbWFnbml0dWRldAACW0J4cgAQamF2YS5sYW5nLk51bWJlcoaslR0LlOCLAgAAeHD///////////////7////+AAAAAXVyAAJbQqzzF/gGCFTgAgAAeHAAAAAQzkYEoAAAAAAAAAAAAAAABHhzcgAOZXZtLlNpZ2hhc2hJbnRUdcqNMXEgeAIAAUwAAW5xAH4ABnhwc3EAfgAM///////////////+/////gAAAAF1cQB+ABAAAAAEcKCCMXhzcgATdmMuZGF0YS5DYWxsU3VtbWFyeZQcmw5vl+FdAgAQSQAJc3VtbWFyeUlkTAAOY2FsbENvbnZlbnRpb250ACZMaW5zdHJ1bWVudGF0aW9uL2NhbGxzL0NhbGxDb252ZW50aW9uO0wACmNhbGxUYXJnZXR0ABpMYW5hbHlzaXMvaWNmZy9DYWxsVGFyZ2V0O0wACGNhbGxUeXBldAAVTHZjL2RhdGEvVEFDQ2FsbFR5cGU7TAAPY2Fubm90QmVJbmxpbmVkdAAtTGFuYWx5c2lzL2ljZmcvSW5saW5lciRJbGxlZ2FsSW5saW5pbmdSZWFzb247TAAGZ2FzVmFydAATTHZjL2RhdGEvVEFDU3ltYm9sO0wABmluQmFzZXEAfgAbTAAIaW5PZmZzZXRxAH4AG0wABmluU2l6ZXEAfgAbTAAMb3JpZ0NhbGxjb3JldAAgTHZjL2RhdGEvVEFDQ21kJFNpbXBsZSRDYWxsQ29yZTtMAAdvdXRCYXNlcQB+ABtMAAlvdXRPZmZzZXRxAH4AG0wAB291dFNpemVxAH4AG0wADXNpZ1Jlc29sdXRpb250AA9MamF2YS91dGlsL1NldDtMAAV0b1ZhcnEAfgAbTAAIdmFsdWVWYXJxAH4AG3hwAAAAAHNyACRpbnN0cnVtZW50YXRpb24uY2FsbHMuQ2FsbENvbnZlbnRpb25HtO1ulL788QIAA0kACGNhbGxlcklkTAAFaW5wdXR0ABlMYW5hbHlzaXMvaWNmZy9DYWxsSW5wdXQ7TAAGcmF3T3V0dAAiTGluc3RydW1lbnRhdGlvbi9jYWxscy9DYWxsT3V0cHV0O3hwAAAAAHNyABdhbmFseXNpcy5pY2ZnLkNhbGxJbnB1dJjJD1MhNUxQAgAHTAAHYmFzZVZhcnQAGUx2Yy9kYXRhL1RBQ0V4cHIkU3ltJFZhcjtMABBlbmNvZGVkQXJndW1lbnRzdAAjTGFuYWx5c2lzL2ljZmcvQUJJQXJndW1lbnRFbmNvZGluZztMABNpbnB1dFNpemVMb3dlckJvdW5kcQB+AAZMAAZvZmZzZXR0ABVMdmMvZGF0YS9UQUNFeHByJFN5bTtMABRyYW5nZVRvRGVjb21wb3NlZEFyZ3QAD0xqYXZhL3V0aWwvTWFwO0wAEHNpbXBsaWZpZWRPZmZzZXR0ABtMdmMvZGF0YS9UQUNFeHByJFN5bSRDb25zdDtMAARzaXplcQB+ACZ4cHNyABd2Yy5kYXRhLlRBQ0V4cHIkU3ltJFZhcskrg43eGgPnAgACTAABc3QAF0x2Yy9kYXRhL1RBQ1N5bWJvbCRWYXI7TAADdGFndAAJTHRhYy9UYWc7eHIAE3ZjLmRhdGEuVEFDRXhwciRTeW2iVj0S4YSNUAIAAHhyAA92Yy5kYXRhLlRBQ0V4cHJYhGlUu/v+yAIAAHhwc3IANnZjLmRhdGEuVEFDU3ltYm9sJFZhciRXaXRoRGVmYXVsdENhbGxJbmRleCRXaXRoQnl0ZU1hcJ7+oHF4CHAAAgACTAAEbWV0YXQALUxrb3RsaW54L2NvbGxlY3Rpb25zL2ltbXV0YWJsZS9QZXJzaXN0ZW50TWFwO0wACm5hbWVQcmVmaXh0ABJMamF2YS9sYW5nL1N0cmluZzt4cgAVdmMuZGF0YS5UQUNTeW1ib2wkVmFyCYrCGVl9SXYCAAB4cgARdmMuZGF0YS5UQUNTeW1ib2zd3Run/CoWswIAAHhwc3IAJmRhdGFzdHJ1Y3R1cmVzLnRyZWFwLkhhc2hUcmVhcE1hcCROb2Rlf2t9acJIPnQCAANMAANrZXl0ABJMamF2YS9sYW5nL09iamVjdDtMAARuZXh0dAA1TGRhdGFzdHJ1Y3R1cmVzL3RyZWFwL0hhc2hUcmVhcE1hcCRNb3JlS2V5VmFsdWVQYWlycztMAAV2YWx1ZXEAfgA3eHIAIWRhdGFzdHJ1Y3R1cmVzLnRyZWFwLkhhc2hUcmVhcE1hcPMJ/2vt3boKAgAAeHIAHWRhdGFzdHJ1Y3R1cmVzLnRyZWFwLlRyZWFwTWFw46LAyn3v5moCAAB4cgAaZGF0YXN0cnVjdHVyZXMudHJlYXAuVHJlYXA88f21zZwbdQIAAkwABGxlZnR0ABxMZGF0YXN0cnVjdHVyZXMvdHJlYXAvVHJlYXA7TAAFcmlnaHRxAH4APHhwcHNxAH4ANnBzcQB+ADZwcHNyAAt0YWMuTWV0YUtleVF/W3MiCfIZAgADTAAPZXJhc3VyZVN0cmF0ZWd5dAAdTHRhYy9NZXRhS2V5JEVyYXN1cmVTdHJhdGVneTtMAARuYW1lcQB+ADJMAAN0eXB0ABFMamF2YS9sYW5nL0NsYXNzO3hwfnIAG3RhYy5NZXRhS2V5JEVyYXN1cmVTdHJhdGVneQAAAAAAAAAAEgAAeHIADmphdmEubGFuZy5FbnVtAAAAAAAAAAASAAB4cHQACUNhbm9uaWNhbHQAF3RhYy5tZW1vcnkucGFydGl0aW9uLWlkdnIAEWphdmEubGFuZy5JbnRlZ2VyEuKgpPeBhzgCAAFJAAV2YWx1ZXhxAH4ADnBzcQB+AEkAAAACc3EAfgBAcQB+AEZ0ABJUYWMuc3ltYm9sLmtleXdvcmR2cgAQamF2YS5sYW5nLlN0cmluZ6DwpDh6O7NCAgAAeHBwdAAEdGFjTXNxAH4AQHEAfgBGdAANdGFjLmlzLm1lbW9yeXZyACJ0YWMuTWV0YU1hcCRDb21wYW5pb24kTm90aGluZ1ZhbHVl8nsHH85ykpUCAAB4cHBzcQB+AFN0AA90YWNNQ0FOT04yISEyNDJzcgAPdGFjLlRhZyRCeXRlTWFwNb/Ry6GDRgkCAAB4cgALdGFjLlRhZyRNYXABJytzDV3P/QIAAHhyAAd0YWMuVGFnLk9V3gn2xngCAAB4cHBzcQB+AAz///////////////7////+AAAAAXVxAH4AEAAAAAEkeHNxAH4AKnNyADV2Yy5kYXRhLlRBQ1N5bWJvbCRWYXIkV2l0aERlZmF1bHRDYWxsSW5kZXgkV2l0aEJpdDI1NnqsyEgq0drPAgACTAAEbWV0YXEAfgAxTAAKbmFtZVByZWZpeHEAfgAyeHEAfgAzc3EAfgA2c3EAfgA2cHBxAH4ATHB0AAFMcHNxAH4AQHEAfgBGdAAQdGFjLnN0YWNrLmhlaWdodHEAfgBKcHNxAH4ASQAAA/B0AARSMjQzc3IADnRhYy5UYWckQml0MjU2IyLQT+LlKkgCAAB4cQB+AFlzcgARamF2YS51dGlsLkhhc2hNYXAFB9rBwxZg0QMAAkYACmxvYWRGYWN0b3JJAAl0aHJlc2hvbGR4cD9AAAAAAAADdwgAAAAEAAAAAnNyAB5hbmFseXNpcy5pY2ZnLlNjcmF0Y2hCeXRlUmFuZ2XBTLaPpUzj2gIAAkwABGZyb21xAH4ABkwAAnRvcQB+AAZ4cHNxAH4ADP///////////////v////4AAAAAdXEAfgAQAAAAAHhzcQB+AAz///////////////7////+AAAAAXVxAH4AEAAAAAEDeHNyAC1hbmFseXNpcy5pY2ZnLkRlY29tcG9zZWRDYWxsSW5wdXRBcmckQ29uc3RhbnSFavLdQafqPQIAA0wAAWN0ABlMdmMvZGF0YS9UQUNTeW1ib2wkQ29uc3Q7TAARY29udHJhY3RSZWZlcmVuY2V0AC9MYW5hbHlzaXMvaWNmZy9DYWxsR3JhcGhCdWlsZGVyJENhbGxlZENvbnRyYWN0O0wADHNjcmF0Y2hSYW5nZXQAIExhbmFseXNpcy9pY2ZnL1NjcmF0Y2hCeXRlUmFuZ2U7eHIAJGFuYWx5c2lzLmljZmcuRGVjb21wb3NlZENhbGxJbnB1dEFyZ82Nwhnirh8hAgAAeHBzcgAXdmMuZGF0YS5UQUNTeW1ib2wkQ29uc3QmHp5/l8IUcAIAAkwAA3RhZ3EAfgAsTAAFdmFsdWVxAH4ABnhxAH4ANHEAfgBoc3EAfgAM///////////////+/////gAAAAF1cQB+ABAAAAAgcKCCMQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAB4cHEAfgBsc3EAfgBrc3EAfgAM///////////////+/////gAAAAF1cQB+ABAAAAABBHhzcQB+AAz///////////////7////+AAAAAXVxAH4AEAAAAAEjeHNyAC1hbmFseXNpcy5pY2ZnLkRlY29tcG9zZWRDYWxsSW5wdXRBcmckVmFyaWFibGWV3y80jneopQIAA0wAEWNvbnRyYWN0UmVmZXJlbmNlcQB+AHNMAAxzY3JhdGNoUmFuZ2VxAH4AdEwAAXZxAH4AK3hxAH4AdXNyAERhbmFseXNpcy5pY2ZnLkNhbGxHcmFwaEJ1aWxkZXIkQ2FsbGVkQ29udHJhY3QkRnVsbHlSZXNvbHZlZCRTZWxmTGlua++8l8Aq7q6zAgABTAAKY29udHJhY3RJZHEAfgAGeHIAO2FuYWx5c2lzLmljZmcuQ2FsbEdyYXBoQnVpbGRlciRDYWxsZWRDb250cmFjdCRGdWxseVJlc29sdmVkotnIkxMAs6QCAAB4cgAtYW5hbHlzaXMuaWNmZy5DYWxsR3JhcGhCdWlsZGVyJENhbGxlZENvbnRyYWN00wt1rN/LodcCAAB4cHNxAH4ADP///////////////v////4AAAABdXEAfgAQAAAAEM5GBKAAAAAAAAAAAAAAABd4cQB+AHtzcQB+AF5zcQB+ADZwc3EAfgA2c3EAfgA2c3EAfgA2cHBxAH4ATHB0AA10YWNDb250cmFjdEF0cHNxAH4AQH5xAH4ARHQABkVyYXNlZHQAGnRhYy5jb250cmFjdC5zeW0uYWRkci5uYW1lcQB+AE9wdAAFY3VydmVwc3EAfgBAcQB+AI90ABV0YWMuY29udHJhY3Quc3ltLmFkZHJ2cQB+AAxwcQB+AIZzcQB+AEBxAH4ARnQAGHRhYy5kZWNvbXAtaW5zY2FsYXIuc29ydHZyAB10YWMuRGVjb21wb3NlZElucHV0U2NhbGFyU29ydCeGMd9jMFQFAgAAeHBwc3IAJHRhYy5EZWNvbXBvc2VkSW5wdXRTY2FsYXJTb3J0JFNpbXBsZXkHVfqoCbJbAgABTAAKYnl0ZU9mZnNldHEAfgAGeHEAfgCYcQB+AHx0AANSMzB4cHNxAH4AKnNyABp2Yy5kYXRhLlRBQ1N5bWJvbCRWYXIkRnVsbBPmPQsuB0CVAgAESQAJY2FsbEluZGV4TAAEbWV0YXEAfgAxTAAKbmFtZVByZWZpeHEAfgAyTAADdGFncQB+ACx4cQB+ADMAAAABc3EAfgA2c3EAfgA2cHBxAH4ATHBxAH4AYnBxAH4AY3BzcQB+AEkAAAPvdAAITENBTk9OMjJxAH4AaHEAfgBoc3IAIGluc3RydW1lbnRhdGlvbi5jYWxscy5DYWxsT3V0cHV0wsWbN8G9nHsCAANMAARiYXNlcQB+ACtMAAZvZmZzZXR0ABFMdmMvZGF0YS9UQUNFeHByO0wABHNpemVxAH4ApXhwc3EAfgAwc3EAfgA2cHNxAH4ANnBzcQB+ADZwcHEAfgBDcHEAfgBLcQB+AExwcQB+AFBxAH4AUXBxAH4AVXEAfgBWc3EAfgAqc3EAfgBec3EAfgA2c3EAfgA2cHBxAH4ATHBxAH4AYnBxAH4AY3BzcQB+AEkAAAPwcQB+AGZxAH4AaHNyABl2Yy5kYXRhLlRBQ0V4cHIkU3ltJENvbnN0U0iv8zJB2nYCAAJMAAFzcQB+AHJMAAN0YWdxAH4ALHhxAH4ALXNxAH4Ad3EAfgBoc3EAfgAM///////////////+/////gAAAAF1cQB+ABAAAAABIHhxAH4AaHNyAB5hbmFseXNpcy5pY2ZnLkNhbGxUYXJnZXQkVmFsaWS5phn2PatV+gIAAUwABmNhbGxlZXEAfgBzeHIAGGFuYWx5c2lzLmljZmcuQ2FsbFRhcmdldEbdPSx8dj4lAgAAeHBzcgBHYW5hbHlzaXMuaWNmZy5DYWxsR3JhcGhCdWlsZGVyJENhbGxlZENvbnRyYWN0JEZ1bGx5UmVzb2x2ZWQkU3RvcmFnZUxpbmvSgQnS0FaL1QIAAkkADXN0b3JhZ2VSZWFkSWRMAApjb250cmFjdElkcQB+AAZ4cQB+AIMAAAAncQB+AA9+cgATdmMuZGF0YS5UQUNDYWxsVHlwZQAAAAAAAAAAEgAAeHEAfgBFdAAGU1RBVElDcHNxAH4AXnNxAH4ANnNxAH4ANnBwcQB+AExwcQB+AGJwcQB+AGNwc3EAfgBJAAAD7HQABFIyNDRzcQB+ADBzcQB+ADZwc3EAfgA2cHNxAH4ANnBwcQB+AENwcQB+AEtxAH4ATHBxAH4AUHEAfgBRcHEAfgBVcQB+AFZzcQB+AF5zcQB+ADZzcQB+ADZwcHEAfgBMcHEAfgBicHEAfgBjcHEAfgBlcQB+AGZzcQB+AHdxAH4AaHEAfgBbc3IAHnZjLmRhdGEuVEFDQ21kJFNpbXBsZSRDYWxsQ29yZaEphUcEgWZ6AgALTAAIY2FsbFR5cGVxAH4AGUwAA2dhc3EAfgAbTAAGaW5CYXNlcQB+ACtMAAhpbk9mZnNldHEAfgAbTAAGaW5TaXplcQB+ABtMAARtZXRhcQB+ADFMAAdvdXRCYXNlcQB+ACtMAAlvdXRPZmZzZXRxAH4AG0wAB291dFNpemVxAH4AG0wAAnRvcQB+ABtMAAV2YWx1ZXEAfgAbeHIAFXZjLmRhdGEuVEFDQ21kJFNpbXBsZe0m1iUxBnXSAgAAeHIAE3ZjLmRhdGEuVEFDQ21kJFNwZWMbq/EA+MEDvgIAAHhyAA52Yy5kYXRhLlRBQ0NtZFTLD4g8OR/wAgAAeHBxAH4Au3NxAH4AXnNxAH4ANnNxAH4ANnBwcQB+AExwcQB+AGJwcQB+AGNwcQB+AMBxAH4AwXNxAH4AMHNxAH4ANnBzcQB+ADZwc3EAfgA2cHBxAH4AQ3BxAH4AS3EAfgBMcHEAfgBQcQB+AFFwcQB+AFVxAH4AVnNxAH4AXnNxAH4ANnNxAH4ANnBwcQB+AExwcQB+AGJwcQB+AGNwcQB+AGVxAH4AZnNxAH4AngAAAAFzcQB+ADZzcQB+ADZwcHEAfgBMcHEAfgBicHEAfgBjcHEAfgCicQB+AKNxAH4AaHNxAH4ANnBwc3EAfgBAfnEAfgBEdAAJQ2FsbFRyYWNldAAIdGFjLm1ldGF2cgATdmMuZGF0YS5UQUNNZXRhSW5mbzVgTP2lS6hxAgAGSQAFYmVnaW5JAANsZW5JAAZzb3VyY2VMAAdhZGRyZXNzcQB+AAZMAAhqdW1wVHlwZXQAE0xjb21waWxlci9KdW1wVHlwZTtMAA1zb3VyY2VDb250ZXh0dAAYTGNvbXBpbGVyL1NvdXJjZUNvbnRleHQ7eHBwc3EAfgDhAAAY6wAAACcAAAAAcQB+AIZ+cgARY29tcGlsZXIuSnVtcFR5cGUAAAAAAAAAABIAAHhxAH4ARXQAB1JFR1VMQVJzcgAWY29tcGlsZXIuU291cmNlQ29udGV4dIzLW+lAXNoTAgACTAAPaW5kZXhUb0ZpbGVwYXRocQB+ACdMAAlzb3VyY2VEaXJxAH4AMnhwc3EAfgBpP0AAAAAAAAx3CAAAABAAAAAGc3EAfgBJAAAAAHQAE2NvbnRyYWN0cy9jdXJ2ZS5zb2xzcQB+AEkAAAABdAALQ29udGV4dC5zb2xxAH4AS3QACUVSQzIwLnNvbHNxAH4ASQAAAAN0AApJRVJDMjAuc29sc3EAfgBJAAAABHQAEklFUkMyME1ldGFkYXRhLnNvbHNxAH4ASQAAAAV0ABNSZWVudHJhbmN5R3VhcmQuc29seHQAEy5wb3N0X2F1dG9maW5kZXJzLjFzcQB+ADBzcQB+ADZwc3EAfgA2cHNxAH4ANnBwcQB+AENwcQB+AEtxAH4ATHBxAH4AUHEAfgBRcHEAfgBVcQB+AFZzcQB+AF5zcQB+ADZzcQB+ADZwcHEAfgBMcHEAfgBicHEAfgBjcHEAfgCvcQB+AGZxAH4AsnNxAH4AXnNxAH4ANnNxAH4ANnNxAH4ANnNxAH4ANnBzcQB+ADZwcHEAfgBMcHEAfgBic3EAfgBAcQB+AEZ0ABZ0YWMuc2NhbGFyaXphdGlvbi5zb3J0dnIAGXZjLmRhdGEuU2NhbGFyaXphdGlvblNvcnQwznCd5GgNJgIAAHhwcHNyACB2Yy5kYXRhLlNjYWxhcml6YXRpb25Tb3J0JFBhY2tlZC5FrRKTiOT3AgACSQAFc3RhcnRMAAtwYWNrZWRTdGFydHQAG0x2Yy9kYXRhL1NjYWxhcml6YXRpb25Tb3J0O3hxAH4BBwAAAABzcgAfdmMuZGF0YS5TY2FsYXJpemF0aW9uU29ydCRTcGxpdFT/Wafxx7IFAgABTAADaWR4cQB+AAZ4cQB+AQdzcQB+AAz///////////////7////+AAAAAXVxAH4AEAAAAAELeHNxAH4ANnBzcQB+ADZwc3EAfgA2cHBzcQB+AEBxAH4ARnQAHHRhYy5zdG9yYWdlLm5vbi1pbmRleGVkLXBhdGh2cgA1YW5hbHlzaXMuc3RvcmFnZS5TdG9yYWdlQW5hbHlzaXNSZXN1bHQkTm9uSW5kZXhlZFBhdGgIwaBLofo/RQIAAHhwcHNyADphbmFseXNpcy5zdG9yYWdlLlN0b3JhZ2VBbmFseXNpc1Jlc3VsdCROb25JbmRleGVkUGF0aCRSb290vzf12KXqCv8CAAFMAARzbG90cQB+AAZ4cQB+ARVxAH4BDnNxAH4AQHEAfgBGdAANdGFjLnNsb3QudHlwZXZyADpzcGVjLmN2bGFzdC50eXBlZGVzY3JpcHRvcnMuRVZNVHlwZURlc2NyaXB0b3IkRVZNVmFsdWVUeXBlxomvArrquCUCAAB4cgAtc3BlYy5jdmxhc3QudHlwZWRlc2NyaXB0b3JzLkVWTVR5cGVEZXNjcmlwdG9yyFGp8TzCah0CAAB4cHBzcgA1c3BlYy5jdmxhc3QudHlwZWRlc2NyaXB0b3JzLkVWTVR5cGVEZXNjcmlwdG9yJGFkZHJlc3N6+GX0b5egKQIAAHhyAERzcGVjLmN2bGFzdC50eXBlZGVzY3JpcHRvcnMuRVZNVHlwZURlc2NyaXB0b3IkRVZNSXNvbW9ycGhpY1ZhbHVlVHlwZfd1mJFuEKEPAgAAeHEAfgEbc3EAfgBAcQB+AI90ABh0YWMuc3RvcmFnZS5wcmV0dHkucGF0aHN2cgAdYW5hbHlzaXMuc3RvcmFnZS5EaXNwbGF5UGF0aHP3REu3w/VRFgIAAUwABXBhdGhzcQB+AB14cHBzcQB+ASNzcgAXamF2YS51dGlsLkxpbmtlZEhhc2hTZXTYbNdald0qHgIAAHhyABFqYXZhLnV0aWwuSGFzaFNldLpEhZWWuLc0AwAAeHB3DAAAABA/QAAAAAAAAXNyACFhbmFseXNpcy5zdG9yYWdlLkRpc3BsYXlQYXRoJFJvb3TTc6C9mdA8cgIAAkwABGJhc2V0AB5MYW5hbHlzaXMvc3RvcmFnZS9EaXNwbGF5UGF0aDtMAARuYW1lcQB+ADJ4cgAcYW5hbHlzaXMuc3RvcmFnZS5EaXNwbGF5UGF0aE9AY+pW0iAFAgAAeHBwdAAHY29pbnNfMXhzcQB+AEBxAH4ARnQAFXRhYy5zdG9yYWdlLmJpdC13aWR0aHEAfgBKcHNxAH4ASQAAAKBwc3EAfgBAcQB+AEZ0AAt0YWMuc3RvcmFnZXEAfgCVcHEAfgCGcHEAfgBjcHNxAH4ASQAAA/R0AAtDQU5PTjU2ISEyNHNxAH4Ad3EAfgBocQB+AG1zcQB+ADBzcQB+ADZwc3EAfgA2cHNxAH4ANnBwcQB+AENwcQB+AEtxAH4ATHBxAH4AUHEAfgBRcHEAfgBVcQB+AFZzcQB+AF5zcQB+ADZzcQB+ADZwcHEAfgBMcHEAfgBicHEAfgBjcHEAfgCvcQB+AGZxAH4AsnNyACJqYXZhLnV0aWwuQ29sbGVjdGlvbnMkU2luZ2xldG9uU2V0LFJBmCnAsb8CAAFMAAdlbGVtZW50cQB+ADd4cHEAfgAUc3EAfgBec3EAfgA2c3EAfgA2c3EAfgA2c3EAfgA2cHNxAH4ANnBwcQB+AExwcQB+AGJxAH4BBXBxAH4BC3NxAH4ANnBzcQB+ADZwc3EAfgA2cHBxAH4BE3BxAH4BGHEAfgEZcHEAfgEgcQB+ASFwc3EAfgEjc3EAfgEmdwwAAAAQP0AAAAAAAAFxAH4BLHhxAH4BLnBxAH4BMHBxAH4BMXBxAH4AhnBxAH4AY3BxAH4BM3EAfgE0c3EAfgB3cQB+AGhxAH4AbQ=="}
		AnnotationCmd:56 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageGlobalChangeSnippet.StorageBackupPoint","calleeTxId":2}}
		NopCmd
		AssumeExpCmd LAnd(Eq(tacCalldatasize!!0:3 0x24 ) Eq(tacCalldatasize!!0:3 0x24 ) )
		NopCmd
		AssumeExpCmd Eq(tacCalldatabufCANON0@2:0 0x70a0823100000000000000000000000000000000000000000000000000000000 )
		AssignExpCmd:56 tacCalldatabufCANON1@2:79 R30:80
		LabelCmd:56 "Start procedure ERC20-balanceOf(address)"
		AnnotationCmd:56 JSON{"key":{"name":"fps.free-pointer-is-scalarized","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true}
		AssignExpCmd:56 R249:54 Select(tacExtcodesize!!7:4 Apply(to_skey:bif R29:81) )
		NopCmd
		AssumeExpCmd Gt(R249:54 0x0 )
		AnnotationCmd:56 JSON{"key":{"name":"internal.func.finder.info","type":"analysis.ip.InternalFunctionFinderReport","erasureStrategy":"Erased"},"value":"rO0ABXNyAChhbmFseXNpcy5pcC5JbnRlcm5hbEZ1bmN0aW9uRmluZGVyUmVwb3J0ian+bYn1VdACAAFMABN1bnJlc29sdmVkRnVuY3Rpb25zdAAPTGphdmEvdXRpbC9TZXQ7eHBzcgAhZGF0YXN0cnVjdHVyZXMuTGlua2VkQXJyYXlIYXNoU2V0AAAAAAAAAAEDAAJGAApsb2FkRmFjdG9yTAAJaGFzaFRhYmxldAAuTGRhdGFzdHJ1Y3R1cmVzL2FycmF5aGFzaHRhYmxlL0FycmF5SGFzaFRhYmxlO3hwdwgAAAAAQAAAAHg="}
		AnnotationCmd:56 JSON{"key":{"name":"fps.free-pointer-is-scalarized","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true}
		NopCmd
		AssumeExpCmd LNot(Lt(tacCalldatasize!!0:3 0x4 ) )
		NopCmd
		AssumeExpCmd LNot(Gt(0x39509351 tacSighash!!35:47 ) )
		NopCmd
		AssumeExpCmd LNot(Eq(0x39509351 tacSighash!!35:47 ) )
		NopCmd
		AssumeExpCmd Eq(0x70a08231 tacSighash!!35:47 )
		AssignExpCmd:82 R255:83 Sub(tacCalldatasize!!0:3 0x4 )
		AssignExpCmd:56 B256:84 Slt(R255:83 0x20 )
		NopCmd
		AssumeExpCmd LNot(B256:84 )
		AssignExpCmd:85 R258:72 tacCalldatabufCANON1@2:86
		NopCmd
		AssumeExpCmd Eq(tacCalldatabufCANON1@2:86 tacCalldatabufCANON1@2:86 )
		AnnotationCmd:56 JSON{"key":{"name":"internal.func.start","type":"analysis.ip.InternalFuncStartAnnotation","erasureStrategy":"CallTrace"},"value":{"id":1,"startPc":1712,"args":[{"s":{"namePrefix":"R258","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1013}]},"offset":1,"sort":"SCALAR"}],"methodSignature":{"#class":"spec.cvlast.QualifiedMethodSignature.QualifiedMethodSig","qualifiedMethodName":{"#class":"spec.cvlast.QualifiedFunction","host":{"name":"ERC20"},"methodId":"balanceOf"},"params":[{"#class":"spec.cvlast.VMParam.Named","name":"account","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$address"}}],"res":[{"#class":"spec.cvlast.VMParam.Unnamed","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256}}]},"stackOffsetToArgPos":{"1":0},"callSiteSrc":{"source":0,"begin":4374,"len":467,"jumpType":"ENTER","address":"ce4604a0000000000000000000000004","sourceContext":{"indexToFilepath":{"0":"contracts/ERC20.sol","1":"contracts/IERC20Metadata.sol","2":"Context.sol","3":"IERC20.sol"},"sourceDir":".post_autofinders.0"}}}}
		AssignExpCmd:87 R263:88 Apply(hash_3_keccak:bif Apply(skey_basic:bif 0x40) Apply(to_skey:bif tacCalldatabufCANON1@2:86) Apply(skey_basic:bif 0x0))
		AssignExpCmd:89 R264:88 Select(CANON130!!10:7 R263:90 )
		AnnotationCmd:56 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet","value":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R264","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1020}]},"displayPath":{"#class":"analysis.storage.DisplayPath.MapAccess","key":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R258","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1018}]},"keyTyp":{"#class":"tac.TACStorageType.IntegralType","typeLabel":"address","numBytes":"14","descriptor":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$address"},"lowerBound":null,"upperBound":null},"base":{"#class":"analysis.storage.DisplayPath.Root","name":"_balances"}},"storageType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256},"contractInstance":"ce4604a0000000000000000000000004","linkableStorageReadId":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet.None"}}}
		AnnotationCmd:56 JSON{"key":{"name":"internal.func.end","type":"analysis.ip.InternalFuncExitAnnotation","erasureStrategy":"Canonical"},"value":{"id":1,"rets":[{"s":{"namePrefix":"R264","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1023}]},"offset":0}],"functionLayout":{"0":{"#class":"analysis.ip.InternalFuncValueLocation.Scalar"}}}}
		AnnotationCmd:56 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.EVMFunctionReturnWrite","returnbufOffset":"0","returnValueSym":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R264","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1023}]},"callIndex":2}}
		AnnotationCmd:56 JSON{"key":{"name":"tac.return.path","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		LabelCmd:56 "End procedure ERC20-balanceOf(address)"
		AssignExpCmd:56 tacReturndata!!266:78 Store(tacReturndata!!245:78 0x0 R264:88 )
		AssignExpCmd:56 tacMCANON2!!267:13 Store(tacMCANON2!!242:13 0x100 R264:88 )
		AnnotationCmd:56 JSON{"key":{"name":"call.trace.pop","type":"analysis.icfg.Inliner$CallStack$PopRecord","erasureStrategy":"Canonical"},"value":"rO0ABXNyAClhbmFseXNpcy5pY2ZnLklubGluZXIkQ2FsbFN0YWNrJFBvcFJlY29yZPAPfwSLdCWJAgABSQAIY2FsbGVlSWR4cAAAAAI="}
		JumpCmd:56 1_0_0_1_0_0
	}
	Block 0_0_0_3_0_0 Succ [2_0_0_1_0_0] {
		AnnotationCmd:56 JSON{"key":{"name":"call.trace.push","type":"analysis.icfg.Inliner$CallStack$PushRecord","erasureStrategy":"Canonical"},"value":"rO0ABXNyACphbmFseXNpcy5pY2ZnLklubGluZXIkQ2FsbFN0YWNrJFB1c2hSZWNvcmSX8+DCTLCH+AIAA0kACGNhbGxlZUlkTAAGY2FsbGVldAATTHZjL2RhdGEvTWV0aG9kUmVmO0wAB3N1bW1hcnl0ABVMdmMvZGF0YS9DYWxsU3VtbWFyeTt4cAAAAANzcgARdmMuZGF0YS5NZXRob2RSZWbJlJTzzU9pGAIAA0wABGF0dHJ0ABdMc2NlbmUvTWV0aG9kQXR0cmlidXRlO0wACmNvbnRyYWN0SWR0ABZMamF2YS9tYXRoL0JpZ0ludGVnZXI7TAAHc2lnSGFzaHQAEExldm0vU2lnaGFzaEludDt4cHNyABxzY2VuZS5NZXRob2RBdHRyaWJ1dGUkQ29tbW9uNHjdebdr9XMCAAB4cgAVc2NlbmUuTWV0aG9kQXR0cmlidXRlcYg2pYWutuUCAAB4cHNyABRqYXZhLm1hdGguQmlnSW50ZWdlcoz8nx+pO/sdAwAGSQAIYml0Q291bnRJAAliaXRMZW5ndGhJABNmaXJzdE5vbnplcm9CeXRlTnVtSQAMbG93ZXN0U2V0Qml0SQAGc2lnbnVtWwAJbWFnbml0dWRldAACW0J4cgAQamF2YS5sYW5nLk51bWJlcoaslR0LlOCLAgAAeHD///////////////7////+AAAAAXVyAAJbQqzzF/gGCFTgAgAAeHAAAAAQzkYEoAAAAAAAAAAAAAAAF3hzcgAOZXZtLlNpZ2hhc2hJbnRUdcqNMXEgeAIAAUwAAW5xAH4ABnhwc3EAfgAM///////////////+/////gAAAAF1cQB+ABAAAAAEOEL3dnhzcgATdmMuZGF0YS5DYWxsU3VtbWFyeZQcmw5vl+FdAgAQSQAJc3VtbWFyeUlkTAAOY2FsbENvbnZlbnRpb250ACZMaW5zdHJ1bWVudGF0aW9uL2NhbGxzL0NhbGxDb252ZW50aW9uO0wACmNhbGxUYXJnZXR0ABpMYW5hbHlzaXMvaWNmZy9DYWxsVGFyZ2V0O0wACGNhbGxUeXBldAAVTHZjL2RhdGEvVEFDQ2FsbFR5cGU7TAAPY2Fubm90QmVJbmxpbmVkdAAtTGFuYWx5c2lzL2ljZmcvSW5saW5lciRJbGxlZ2FsSW5saW5pbmdSZWFzb247TAAGZ2FzVmFydAATTHZjL2RhdGEvVEFDU3ltYm9sO0wABmluQmFzZXEAfgAbTAAIaW5PZmZzZXRxAH4AG0wABmluU2l6ZXEAfgAbTAAMb3JpZ0NhbGxjb3JldAAgTHZjL2RhdGEvVEFDQ21kJFNpbXBsZSRDYWxsQ29yZTtMAAdvdXRCYXNlcQB+ABtMAAlvdXRPZmZzZXRxAH4AG0wAB291dFNpemVxAH4AG0wADXNpZ1Jlc29sdXRpb250AA9MamF2YS91dGlsL1NldDtMAAV0b1ZhcnEAfgAbTAAIdmFsdWVWYXJxAH4AG3hwAAAAAXNyACRpbnN0cnVtZW50YXRpb24uY2FsbHMuQ2FsbENvbnZlbnRpb25HtO1ulL788QIAA0kACGNhbGxlcklkTAAFaW5wdXR0ABlMYW5hbHlzaXMvaWNmZy9DYWxsSW5wdXQ7TAAGcmF3T3V0dAAiTGluc3RydW1lbnRhdGlvbi9jYWxscy9DYWxsT3V0cHV0O3hwAAAAAHNyABdhbmFseXNpcy5pY2ZnLkNhbGxJbnB1dJjJD1MhNUxQAgAHTAAHYmFzZVZhcnQAGUx2Yy9kYXRhL1RBQ0V4cHIkU3ltJFZhcjtMABBlbmNvZGVkQXJndW1lbnRzdAAjTGFuYWx5c2lzL2ljZmcvQUJJQXJndW1lbnRFbmNvZGluZztMABNpbnB1dFNpemVMb3dlckJvdW5kcQB+AAZMAAZvZmZzZXR0ABVMdmMvZGF0YS9UQUNFeHByJFN5bTtMABRyYW5nZVRvRGVjb21wb3NlZEFyZ3QAD0xqYXZhL3V0aWwvTWFwO0wAEHNpbXBsaWZpZWRPZmZzZXR0ABtMdmMvZGF0YS9UQUNFeHByJFN5bSRDb25zdDtMAARzaXplcQB+ACZ4cHNyABd2Yy5kYXRhLlRBQ0V4cHIkU3ltJFZhcskrg43eGgPnAgACTAABc3QAF0x2Yy9kYXRhL1RBQ1N5bWJvbCRWYXI7TAADdGFndAAJTHRhYy9UYWc7eHIAE3ZjLmRhdGEuVEFDRXhwciRTeW2iVj0S4YSNUAIAAHhyAA92Yy5kYXRhLlRBQ0V4cHJYhGlUu/v+yAIAAHhwc3IANnZjLmRhdGEuVEFDU3ltYm9sJFZhciRXaXRoRGVmYXVsdENhbGxJbmRleCRXaXRoQnl0ZU1hcJ7+oHF4CHAAAgACTAAEbWV0YXQALUxrb3RsaW54L2NvbGxlY3Rpb25zL2ltbXV0YWJsZS9QZXJzaXN0ZW50TWFwO0wACm5hbWVQcmVmaXh0ABJMamF2YS9sYW5nL1N0cmluZzt4cgAVdmMuZGF0YS5UQUNTeW1ib2wkVmFyCYrCGVl9SXYCAAB4cgARdmMuZGF0YS5UQUNTeW1ib2zd3Run/CoWswIAAHhwc3IAJmRhdGFzdHJ1Y3R1cmVzLnRyZWFwLkhhc2hUcmVhcE1hcCROb2Rlf2t9acJIPnQCAANMAANrZXl0ABJMamF2YS9sYW5nL09iamVjdDtMAARuZXh0dAA1TGRhdGFzdHJ1Y3R1cmVzL3RyZWFwL0hhc2hUcmVhcE1hcCRNb3JlS2V5VmFsdWVQYWlycztMAAV2YWx1ZXEAfgA3eHIAIWRhdGFzdHJ1Y3R1cmVzLnRyZWFwLkhhc2hUcmVhcE1hcPMJ/2vt3boKAgAAeHIAHWRhdGFzdHJ1Y3R1cmVzLnRyZWFwLlRyZWFwTWFw46LAyn3v5moCAAB4cgAaZGF0YXN0cnVjdHVyZXMudHJlYXAuVHJlYXA88f21zZwbdQIAAkwABGxlZnR0ABxMZGF0YXN0cnVjdHVyZXMvdHJlYXAvVHJlYXA7TAAFcmlnaHRxAH4APHhwcHNxAH4ANnBzcQB+ADZwcHNyAAt0YWMuTWV0YUtleVF/W3MiCfIZAgADTAAPZXJhc3VyZVN0cmF0ZWd5dAAdTHRhYy9NZXRhS2V5JEVyYXN1cmVTdHJhdGVneTtMAARuYW1lcQB+ADJMAAN0eXB0ABFMamF2YS9sYW5nL0NsYXNzO3hwfnIAG3RhYy5NZXRhS2V5JEVyYXN1cmVTdHJhdGVneQAAAAAAAAAAEgAAeHIADmphdmEubGFuZy5FbnVtAAAAAAAAAAASAAB4cHQACUNhbm9uaWNhbHQAF3RhYy5tZW1vcnkucGFydGl0aW9uLWlkdnIAEWphdmEubGFuZy5JbnRlZ2VyEuKgpPeBhzgCAAFJAAV2YWx1ZXhxAH4ADnBzcQB+AEkAAAACc3EAfgBAcQB+AEZ0ABJUYWMuc3ltYm9sLmtleXdvcmR2cgAQamF2YS5sYW5nLlN0cmluZ6DwpDh6O7NCAgAAeHBwdAAEdGFjTXNxAH4AQHEAfgBGdAANdGFjLmlzLm1lbW9yeXZyACJ0YWMuTWV0YU1hcCRDb21wYW5pb24kTm90aGluZ1ZhbHVl8nsHH85ykpUCAAB4cHBzcQB+AFN0AA90YWNNQ0FOT04yISE0NzFzcgAPdGFjLlRhZyRCeXRlTWFwNb/Ry6GDRgkCAAB4cgALdGFjLlRhZyRNYXABJytzDV3P/QIAAHhyAAd0YWMuVGFnLk9V3gn2xngCAAB4cHBzcQB+AAz///////////////7////+AAAAAXVxAH4AEAAAAAFkeHNxAH4AKnNyADV2Yy5kYXRhLlRBQ1N5bWJvbCRWYXIkV2l0aERlZmF1bHRDYWxsSW5kZXgkV2l0aEJpdDI1NnqsyEgq0drPAgACTAAEbWV0YXEAfgAxTAAKbmFtZVByZWZpeHEAfgAyeHEAfgAzc3EAfgA2c3EAfgA2cHBxAH4ATHB0AAFMcHNxAH4AQHEAfgBGdAAQdGFjLnN0YWNrLmhlaWdodHEAfgBKcHNxAH4ASQAAA/h0AARSNDcyc3IADnRhYy5UYWckQml0MjU2IyLQT+LlKkgCAAB4cQB+AFlzcgARamF2YS51dGlsLkhhc2hNYXAFB9rBwxZg0QMAAkYACmxvYWRGYWN0b3JJAAl0aHJlc2hvbGR4cD9AAAAAAAADdwgAAAAEAAAAAnNyAB5hbmFseXNpcy5pY2ZnLlNjcmF0Y2hCeXRlUmFuZ2XBTLaPpUzj2gIAAkwABGZyb21xAH4ABkwAAnRvcQB+AAZ4cHNxAH4ADP///////////////v////4AAAAAdXEAfgAQAAAAAHhzcQB+AAz///////////////7////+AAAAAXVxAH4AEAAAAAEDeHNyAC1hbmFseXNpcy5pY2ZnLkRlY29tcG9zZWRDYWxsSW5wdXRBcmckQ29uc3RhbnSFavLdQafqPQIAA0wAAWN0ABlMdmMvZGF0YS9UQUNTeW1ib2wkQ29uc3Q7TAARY29udHJhY3RSZWZlcmVuY2V0AC9MYW5hbHlzaXMvaWNmZy9DYWxsR3JhcGhCdWlsZGVyJENhbGxlZENvbnRyYWN0O0wADHNjcmF0Y2hSYW5nZXQAIExhbmFseXNpcy9pY2ZnL1NjcmF0Y2hCeXRlUmFuZ2U7eHIAJGFuYWx5c2lzLmljZmcuRGVjb21wb3NlZENhbGxJbnB1dEFyZ82Nwhnirh8hAgAAeHBzcgAXdmMuZGF0YS5UQUNTeW1ib2wkQ29uc3QmHp5/l8IUcAIAAkwAA3RhZ3EAfgAsTAAFdmFsdWVxAH4ABnhxAH4ANHEAfgBoc3EAfgAM///////////////+/////gAAAAF1cQB+ABAAAAAgOEL3dgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAB4cHEAfgBsc3EAfgBrc3EAfgAM///////////////+/////gAAAAF1cQB+ABAAAAABRHhzcQB+AAz///////////////7////+AAAAAXVxAH4AEAAAAAFjeHNyAC1hbmFseXNpcy5pY2ZnLkRlY29tcG9zZWRDYWxsSW5wdXRBcmckVmFyaWFibGWV3y80jneopQIAA0wAEWNvbnRyYWN0UmVmZXJlbmNlcQB+AHNMAAxzY3JhdGNoUmFuZ2VxAH4AdEwAAXZxAH4AK3hxAH4AdXNyADxhbmFseXNpcy5pY2ZnLkNhbGxHcmFwaEJ1aWxkZXIkQ2FsbGVkQ29udHJhY3QkVW5yZXNvbHZlZFJlYWRDhKJZ0RDzoAIAAUkADXN0b3JhZ2VSZWFkSWR4cgAtYW5hbHlzaXMuaWNmZy5DYWxsR3JhcGhCdWlsZGVyJENhbGxlZENvbnRyYWN00wt1rN/LodcCAAB4cAAAAAJxAH4Ae3NxAH4AXnNxAH4ANnNxAH4ANnBzcQB+ADZzcQB+ADZzcQB+ADZwc3EAfgA2cHBxAH4ATHBxAH4AYnNxAH4AQHEAfgBGdAAWdGFjLnNjYWxhcml6YXRpb24uc29ydHZyABl2Yy5kYXRhLlNjYWxhcml6YXRpb25Tb3J0MM5wneRoDSYCAAB4cHBzcgAfdmMuZGF0YS5TY2FsYXJpemF0aW9uU29ydCRTcGxpdFT/Wafxx7IFAgABTAADaWR4cQB+AAZ4cQB+AI5zcQB+AAz///////////////7////+AAAAAXVxAH4AEAAAAAEFeHNxAH4ANnBzcQB+ADZwc3EAfgA2cHBzcQB+AEBxAH4ARnQAHHRhYy5zdG9yYWdlLm5vbi1pbmRleGVkLXBhdGh2cgA1YW5hbHlzaXMuc3RvcmFnZS5TdG9yYWdlQW5hbHlzaXNSZXN1bHQkTm9uSW5kZXhlZFBhdGgIwaBLofo/RQIAAHhwcHNyADphbmFseXNpcy5zdG9yYWdlLlN0b3JhZ2VBbmFseXNpc1Jlc3VsdCROb25JbmRleGVkUGF0aCRSb290vzf12KXqCv8CAAFMAARzbG90cQB+AAZ4cQB+AJlxAH4AknNxAH4AQHEAfgBGdAANdGFjLnNsb3QudHlwZXZyADpzcGVjLmN2bGFzdC50eXBlZGVzY3JpcHRvcnMuRVZNVHlwZURlc2NyaXB0b3IkRVZNVmFsdWVUeXBlxomvArrquCUCAAB4cgAtc3BlYy5jdmxhc3QudHlwZWRlc2NyaXB0b3JzLkVWTVR5cGVEZXNjcmlwdG9yyFGp8TzCah0CAAB4cHBzcgAzc3BlYy5jdmxhc3QudHlwZWRlc2NyaXB0b3JzLkVWTVR5cGVEZXNjcmlwdG9yJFVJbnRL+xQfR/Nlf8ACAAFJAAhiaXR3aWR0aHhyAERzcGVjLmN2bGFzdC50eXBlZGVzY3JpcHRvcnMuRVZNVHlwZURlc2NyaXB0b3IkRVZNSXNvbW9ycGhpY1ZhbHVlVHlwZfd1mJFuEKEPAgAAeHEAfgCfAAABAHNxAH4AQH5xAH4ARHQABkVyYXNlZHQAGHRhYy5zdG9yYWdlLnByZXR0eS5wYXRoc3ZyAB1hbmFseXNpcy5zdG9yYWdlLkRpc3BsYXlQYXRoc/dES7fD9VEWAgABTAAFcGF0aHNxAH4AHXhwcHNxAH4AqXNyABdqYXZhLnV0aWwuTGlua2VkSGFzaFNldNhs11qV3SoeAgAAeHIAEWphdmEudXRpbC5IYXNoU2V0ukSFlZa4tzQDAAB4cHcMAAAAED9AAAAAAAABc3IAIWFuYWx5c2lzLnN0b3JhZ2UuRGlzcGxheVBhdGgkUm9vdNNzoL2Z0DxyAgACTAAEYmFzZXQAHkxhbmFseXNpcy9zdG9yYWdlL0Rpc3BsYXlQYXRoO0wABG5hbWVxAH4AMnhyABxhbmFseXNpcy5zdG9yYWdlLkRpc3BsYXlQYXRoT0Bj6lbSIAUCAAB4cHB0AAhmdXR1cmVfQXhzcQB+AEBxAH4ARnQAFXRhYy5zdG9yYWdlLmJpdC13aWR0aHEAfgBKcHNxAH4ASQAAAQBwc3EAfgBAcQB+AEZ0AAt0YWMuc3RvcmFnZXZxAH4ADHBxAH4AD3NxAH4AQHEAfgBGdAAYdGFjLmRlY29tcC1p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"}
		AnnotationCmd:56 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageGlobalChangeSnippet.StorageBackupPoint","calleeTxId":3}}
		NopCmd
		AssumeExpCmd LAnd(Eq(tacCalldatasize!!1:3 0x64 ) Eq(tacCalldatasize!!1:3 0x64 ) )
		AssignExpCmd:56 B270:54 Eq(Select(tacCalldatabuf!!22@3:91 0x0 ) 0x3842f77600000000000000000000000000000000000000000000000000000000 )
		AssumeCmd:56 B270:54
		AssignExpCmd:56 tacCalldatabuf!!271@3:20 LongStore(tacCalldatabuf!!22@3:91 0x4 tacMCANON2!!471:13 0x124 Sub(0x64 0x4 ) )
		LabelCmd:56 "Start procedure curve-get_D(uint256[2],uint256)"
		AnnotationCmd:56 JSON{"key":{"name":"fps.free-pointer-is-scalarized","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true}
		AssignExpCmd:56 R272:54 Select(tacExtcodesize!!7:4 Apply(to_skey:bif R30:63) )
		NopCmd
		AssumeExpCmd Gt(R272:54 0x0 )
		AnnotationCmd:56 JSON{"key":{"name":"internal.func.finder.info","type":"analysis.ip.InternalFunctionFinderReport","erasureStrategy":"Erased"},"value":"rO0ABXNyAChhbmFseXNpcy5pcC5JbnRlcm5hbEZ1bmN0aW9uRmluZGVyUmVwb3J0ian+bYn1VdACAAFMABN1bnJlc29sdmVkRnVuY3Rpb25zdAAPTGphdmEvdXRpbC9TZXQ7eHBzcgAhZGF0YXN0cnVjdHVyZXMuTGlua2VkQXJyYXlIYXNoU2V0AAAAAAAAAAEDAAJGAApsb2FkRmFjdG9yTAAJaGFzaFRhYmxldAAuTGRhdGFzdHJ1Y3R1cmVzL2FycmF5aGFzaHRhYmxlL0FycmF5SGFzaFRhYmxlO3hwdwgAAAAAQAAAAHg="}
		AnnotationCmd:56 JSON{"key":{"name":"fps.free-pointer-is-scalarized","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true}
		NopCmd
		AssumeExpCmd LNot(Lt(tacCalldatasize!!1:3 0x4 ) )
		NopCmd
		AssumeExpCmd Gt(0x82c63066 tacSighash!!36:47 )
		NopCmd
		AssumeExpCmd Eq(0x3842f776 tacSighash!!36:47 )
		AssignExpCmd:92 R278:93 Sub(tacCalldatasize!!1:3 0x4 )
		AssignExpCmd:56 B279:83 Slt(R278:93 0x60 )
		NopCmd
		AssumeExpCmd LNot(B279:83 )
		NopCmd
		AssumeExpCmd Slt(0x23 tacCalldatasize!!1:94 )
		AssignExpCmd:95 R283:96 0x80
		AssumeCmd:97 true
		AssignExpCmd:56 B284:77 Gt(0x44 tacCalldatasize!!1:94 )
		NopCmd
		AssumeExpCmd LNot(B284:77 )
		AnnotationCmd:56 JSON{"key":{"name":"dsa.assign.start","type":"java.lang.String","erasureStrategy":"Erased"},"value":"4280_1005_0_0_0_0 -> 4282_1004_0_0_0_0"}
		LabelCmd:56 "Parallel assignment for R3573:bv256, R3574:bv256 := R2326:bv256, R3653:bv256"
		AnnotationCmd:56 JSON{"key":{"name":"dsa.assign.end","type":"java.lang.String","erasureStrategy":"Erased"},"value":"4280_1005_0_0_0_0 -> 4282_1004_0_0_0_0"}
		AnnotationCmd:56 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.LoopSnippet.StartLoopSnippet","loopIndex":1,"loopSource":"unknown loop source code"}}
		AnnotationCmd:56 JSON{"key":{"name":"start_loop.cmd","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		AnnotationCmd:56 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.LoopSnippet.StartIter","iteration":1}}
		AssignExpCmd:98 R286:99 Select(tacCalldatabuf!!271@3:91 0x4 )
		AssignExpCmd:100 tacMCANON3!!287:15 Store(tacMCANON3!!17:15 0x80 R286:99 )
		AnnotationCmd:56 JSON{"key":{"name":"dsa.assign.start","type":"java.lang.String","erasureStrategy":"Erased"},"value":"4301_1002_0_0_0_0 -> 4282_1004_0_0_0_0"}
		LabelCmd:56 "Parallel assignment for R3573:bv256, R3574:bv256 := R3566:bv256, R3570:bv256"
		AnnotationCmd:56 JSON{"key":{"name":"dsa.assign.end","type":"java.lang.String","erasureStrategy":"Erased"},"value":"4301_1002_0_0_0_0 -> 4282_1004_0_0_0_0"}
		AnnotationCmd:56 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.LoopSnippet.EndIter","iteration":1}}
		AnnotationCmd:56 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.LoopSnippet.StartIter","iteration":2}}
		AssignExpCmd:98 R288:99 Select(tacCalldatabuf!!271@3:91 0x24 )
		AssignExpCmd:100 tacMCANON3!!289:15 Store(tacMCANON3!!287:15 0xa0 R288:99 )
		AnnotationCmd:56 JSON{"key":{"name":"dsa.assign.start","type":"java.lang.String","erasureStrategy":"Erased"},"value":"4301_1002_0_0_0_0 -> 4282_1004_0_0_0_0"}
		LabelCmd:56 "Parallel assignment for R3573:bv256, R3574:bv256 := R3566:bv256, R3570:bv256"
		AnnotationCmd:56 JSON{"key":{"name":"dsa.assign.end","type":"java.lang.String","erasureStrategy":"Erased"},"value":"4301_1002_0_0_0_0 -> 4282_1004_0_0_0_0"}
		AnnotationCmd:56 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.LoopSnippet.EndIter","iteration":2}}
		AnnotationCmd:56 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.LoopSnippet.EndLoopSnippet","loopId":1}}
		AnnotationCmd:56 JSON{"key":{"name":"end_loop.cmd","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		AnnotationCmd:56 JSON{"key":{"name":"pta.end-allocation","type":"analysis.alloc.AllocationAnalysis$AbstractLocation","erasureStrategy":"Erased"},"value":{"prevFPWriteIdx":0,"nextFPWriteCmd":{"block":{"#class":"tac.BlockIdentifier","origStartPc":4102,"stkTop":1000,"decompCopy":0,"calleeIdx":0,"topOfStackValue":0,"freshCopy":0},"pos":1},"sort":{"#class":"analysis.alloc.AllocationAnalysis.Alloc.ConstBlock","sz":"40"}}}
		AssignExpCmd:98 R290:65 Select(tacCalldatabuf!!271@3:91 0x44 )
		AnnotationCmd:56 JSON{"key":{"name":"internal.func.start","type":"analysis.ip.InternalFuncStartAnnotation","erasureStrategy":"CallTrace"},"value":{"id":3,"startPc":558,"args":[{"s":{"namePrefix":"R283","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1001}]},"offset":1,"sort":"SCALAR"},{"s":{"namePrefix":"R290","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1012}]},"offset":2,"sort":"SCALAR"}],"methodSignature":{"#class":"spec.cvlast.QualifiedMethodSignature.QualifiedMethodSig","qualifiedMethodName":{"#class":"spec.cvlast.QualifiedFunction","host":{"name":"curve"},"methodId":"get_D"},"params":[{"#class":"spec.cvlast.VMParam.Named","name":"xp","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$StaticArrayDescriptor","location":"memory","elementType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256},"numElements":"2"}},{"#class":"spec.cvlast.VMParam.Named","name":"amp","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256}}],"res":[{"#class":"spec.cvlast.VMParam.Unnamed","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256}}]},"stackOffsetToArgPos":{"1":0,"2":1},"callSiteSrc":{"source":0,"begin":3416,"len":1542,"jumpType":"ENTER","address":"ce4604a0000000000000000000000017","sourceContext":{"indexToFilepath":{"0":"contracts/curve.sol","1":"Context.sol","2":"ERC20.sol","3":"IERC20.sol","4":"IERC20Metadata.sol","5":"ReentrancyGuard.sol"},"sourceDir":".post_autofinders.1"}}}}
		AssignExpCmd:101 R291:83 Select(tacMCANON3!!289:15 0xa0 )
		AssignExpCmd:102 R292:93 Select(tacMCANON3!!289:15 0x80 )
		NopCmd
		AssumeExpCmd Apply(add_noofl:bif R292:93 R291:83)
		AssignExpCmd I295:54 Apply(safe_math_promotion:bif R292:93)
		AssignExpCmd I296:54 Apply(safe_math_promotion:bif R291:83)
		NopCmd
		AssignExpCmd R298:72 Apply(safe_math_narrow:bif IntAdd(I295:54 I296:54))
		AnnotationCmd:56 JSON{"key":{"name":"internal.func.end","type":"analysis.ip.InternalFuncExitAnnotation","erasureStrategy":"Canonical"},"value":{"id":3,"rets":[{"s":{"namePrefix":"R298","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1023}]},"offset":0}],"functionLayout":{"0":{"#class":"analysis.ip.InternalFuncValueLocation.Scalar"}}}}
		AnnotationCmd:56 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.EVMFunctionReturnWrite","returnbufOffset":"0","returnValueSym":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R298","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1023}]},"callIndex":3}}
		AnnotationCmd:56 JSON{"key":{"name":"tac.return.path","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		LabelCmd:56 "End procedure curve-get_D(uint256[2],uint256)"
		AssignExpCmd:56 tacReturndata!!300:78 Store(tacReturndata!!475:78 0x0 R298:72 )
		AssignExpCmd:56 tacMCANON2!!301:13 Store(tacMCANON2!!471:13 0x120 R298:72 )
		AnnotationCmd:56 JSON{"key":{"name":"call.trace.pop","type":"analysis.icfg.Inliner$CallStack$PopRecord","erasureStrategy":"Canonical"},"value":"rO0ABXNyAClhbmFseXNpcy5pY2ZnLklubGluZXIkQ2FsbFN0YWNrJFBvcFJlY29yZPAPfwSLdCWJAgABSQAIY2FsbGVlSWR4cAAAAAM="}
		JumpCmd:56 2_0_0_1_0_0
	}
	Block 0_0_0_4_0_0 Succ [3_0_0_1_0_0] {
		AnnotationCmd:56 JSON{"key":{"name":"call.trace.push","type":"analysis.icfg.Inliner$CallStack$PushRecord","erasureStrategy":"Canonical"},"value":"rO0ABXNyACphbmFseXNpcy5pY2ZnLklubGluZXIkQ2FsbFN0YWNrJFB1c2hSZWNvcmSX8+DCTLCH+AIAA0kACGNhbGxlZUlkTAAGY2FsbGVldAATTHZjL2RhdGEvTWV0aG9kUmVmO0wAB3N1bW1hcnl0ABVMdmMvZGF0YS9DYWxsU3VtbWFyeTt4cAAAAARzcgARdmMuZGF0YS5NZXRob2RSZWbJlJTzzU9pGAIAA0wABGF0dHJ0ABdMc2NlbmUvTWV0aG9kQXR0cmlidXRlO0wACmNvbnRyYWN0SWR0ABZMamF2YS9tYXRoL0JpZ0ludGVnZXI7TAAHc2lnSGFzaHQAEExldm0vU2lnaGFzaEludDt4cHNyABxzY2VuZS5NZXRob2RBdHRyaWJ1dGUkQ29tbW9uNHjdebdr9XMCAAB4cgAVc2NlbmUuTWV0aG9kQXR0cmlidXRlcYg2pYWutuUCAAB4cHNyABRqYXZhLm1hdGguQmlnSW50ZWdlcoz8nx+pO/sdAwAGSQAIYml0Q291bnRJAAliaXRMZW5ndGhJABNmaXJzdE5vbnplcm9CeXRlTnVtSQAMbG93ZXN0U2V0Qml0SQAGc2lnbnVtWwAJbWFnbml0dWRldAACW0J4cgAQamF2YS5sYW5nLk51bWJlcoaslR0LlOCLAgAAeHD///////////////7////+AAAAAXVyAAJbQqzzF/gGCFTgAgAAeHAAAAAQzkYEoAAAAAAAAAAAAAAAFHhzcgAOZXZtLlNpZ2hhc2hJbnRUdcqNMXEgeAIAAUwAAW5xAH4ABnhwc3EAfgAM///////////////+/////gAAAAF1cQB+ABAAAAAEGBYN3XhzcgATdmMuZGF0YS5DYWxsU3VtbWFyeZQcmw5vl+FdAgAQSQAJc3VtbWFyeUlkTAAOY2FsbENvbnZlbnRpb250ACZMaW5zdHJ1bWVudGF0aW9uL2NhbGxzL0NhbGxDb252ZW50aW9uO0wACmNhbGxUYXJnZXR0ABpMYW5hbHlzaXMvaWNmZy9DYWxsVGFyZ2V0O0wACGNhbGxUeXBldAAVTHZjL2RhdGEvVEFDQ2FsbFR5cGU7TAAPY2Fubm90QmVJbmxpbmVkdAAtTGFuYWx5c2lzL2ljZmcvSW5saW5lciRJbGxlZ2FsSW5saW5pbmdSZWFzb247TAAGZ2FzVmFydAATTHZjL2RhdGEvVEFDU3ltYm9sO0wABmluQmFzZXEAfgAbTAAIaW5PZmZzZXRxAH4AG0wABmluU2l6ZXEAfgAbTAAMb3JpZ0NhbGxjb3JldAAgTHZjL2RhdGEvVEFDQ21kJFNpbXBsZSRDYWxsQ29yZTtMAAdvdXRCYXNlcQB+ABtMAAlvdXRPZmZzZXRxAH4AG0wAB291dFNpemVxAH4AG0wADXNpZ1Jlc29sdXRpb250AA9MamF2YS91dGlsL1NldDtMAAV0b1ZhcnEAfgAbTAAIdmFsdWVWYXJxAH4AG3hwAAAAAnNyACRpbnN0cnVtZW50YXRpb24uY2FsbHMuQ2FsbENvbnZlbnRpb25HtO1ulL788QIAA0kACGNhbGxlcklkTAAFaW5wdXR0ABlMYW5hbHlzaXMvaWNmZy9DYWxsSW5wdXQ7TAAGcmF3T3V0dAAiTGluc3RydW1lbnRhdGlvbi9jYWxscy9DYWxsT3V0cHV0O3hwAAAAAHNyABdhbmFseXNpcy5pY2ZnLkNhbGxJbnB1dJjJD1MhNUxQAgAHTAAHYmFzZVZhcnQAGUx2Yy9kYXRhL1RBQ0V4cHIkU3ltJFZhcjtMABBlbmNvZGVkQXJndW1lbnRzdAAjTGFuYWx5c2lzL2ljZmcvQUJJQXJndW1lbnRFbmNvZGluZztMABNpbnB1dFNpemVMb3dlckJvdW5kcQB+AAZMAAZvZmZzZXR0ABVMdmMvZGF0YS9UQUNFeHByJFN5bTtMABRyYW5nZVRvRGVjb21wb3NlZEFyZ3QAD0xqYXZhL3V0aWwvTWFwO0wAEHNpbXBsaWZpZWRPZmZzZXR0ABtMdmMvZGF0YS9UQUNFeHByJFN5bSRDb25zdDtMAARzaXplcQB+ACZ4cHNyABd2Yy5kYXRhLlRBQ0V4cHIkU3ltJFZhcskrg43eGgPnAgACTAABc3QAF0x2Yy9kYXRhL1RBQ1N5bWJvbCRWYXI7TAADdGFndAAJTHRhYy9UYWc7eHIAE3ZjLmRhdGEuVEFDRXhwciRTeW2iVj0S4YSNUAIAAHhyAA92Yy5kYXRhLlRBQ0V4cHJYhGlUu/v+yAIAAHhwc3IANnZjLmRhdGEuVEFDU3ltYm9sJFZhciRXaXRoRGVmYXVsdENhbGxJbmRleCRXaXRoQnl0ZU1hcJ7+oHF4CHAAAgACTAAEbWV0YXQALUxrb3RsaW54L2NvbGxlY3Rpb25zL2ltbXV0YWJsZS9QZXJzaXN0ZW50TWFwO0wACm5hbWVQcmVmaXh0ABJMamF2YS9sYW5nL1N0cmluZzt4cgAVdmMuZGF0YS5UQUNTeW1ib2wkVmFyCYrCGVl9SXYCAAB4cgARdmMuZGF0YS5UQUNTeW1ib2zd3Run/CoWswIAAHhwc3IAJmRhdGFzdHJ1Y3R1cmVzLnRyZWFwLkhhc2hUcmVhcE1hcCROb2Rlf2t9acJIPnQCAANMAANrZXl0ABJMamF2YS9sYW5nL09iamVjdDtMAARuZXh0dAA1TGRhdGFzdHJ1Y3R1cmVzL3RyZWFwL0hhc2hUcmVhcE1hcCRNb3JlS2V5VmFsdWVQYWlycztMAAV2YWx1ZXEAfgA3eHIAIWRhdGFzdHJ1Y3R1cmVzLnRyZWFwLkhhc2hUcmVhcE1hcPMJ/2vt3boKAgAAeHIAHWRhdGFzdHJ1Y3R1cmVzLnRyZWFwLlRyZWFwTWFw46LAyn3v5moCAAB4cgAaZGF0YXN0cnVjdHVyZXMudHJlYXAuVHJlYXA88f21zZwbdQIAAkwABGxlZnR0ABxMZGF0YXN0cnVjdHVyZXMvdHJlYXAvVHJlYXA7TAAFcmlnaHRxAH4APHhwcHNxAH4ANnBzcQB+ADZwcHNyAAt0YWMuTWV0YUtleVF/W3MiCfIZAgADTAAPZXJhc3VyZVN0cmF0ZWd5dAAdTHRhYy9NZXRhS2V5JEVyYXN1cmVTdHJhdGVneTtMAARuYW1lcQB+ADJMAAN0eXB0ABFMamF2YS9sYW5nL0NsYXNzO3hwfnIAG3RhYy5NZXRhS2V5JEVyYXN1cmVTdHJhdGVneQAAAAAAAAAAEgAAeHIADmphdmEubGFuZy5FbnVtAAAAAAAAAAASAAB4cHQACUNhbm9uaWNhbHQAF3RhYy5tZW1vcnkucGFydGl0aW9uLWlkdnIAEWphdmEubGFuZy5JbnRlZ2VyEuKgpPeBhzgCAAFJAAV2YWx1ZXhxAH4ADnBzcQB+AEkAAAACc3EAfgBAcQB+AEZ0ABJUYWMuc3ltYm9sLmtleXdvcmR2cgAQamF2YS5sYW5nLlN0cmluZ6DwpDh6O7NCAgAAeHBwdAAEdGFjTXNxAH4AQHEAfgBGdAANdGFjLmlzLm1lbW9yeXZyACJ0YWMuTWV0YU1hcCRDb21wYW5pb24kTm90aGluZ1ZhbHVl8nsHH85ykpUCAAB4cHBzcQB+AFN0AA90YWNNQ0FOT04yISE1MjlzcgAPdGFjLlRhZyRCeXRlTWFwNb/Ry6GDRgkCAAB4cgALdGFjLlRhZyRNYXABJytzDV3P/QIAAHhyAAd0YWMuVGFnLk9V3gn2xngCAAB4cHBzcQB+AAz///////////////7////+AAAAAXVxAH4AEAAAAAEEeHNxAH4AKnNyADV2Yy5kYXRhLlRBQ1N5bWJvbCRWYXIkV2l0aERlZmF1bHRDYWxsSW5kZXgkV2l0aEJpdDI1NnqsyEgq0drPAgACTAAEbWV0YXEAfgAxTAAKbmFtZVByZWZpeHEAfgAyeHEAfgAzc3EAfgA2c3EAfgA2cHBxAH4ATHB0AAFMcHNxAH4AQHEAfgBGdAAQdGFjLnN0YWNrLmhlaWdodHEAfgBKcHNxAH4ASQAAA/d0AARSNTMwc3IADnRhYy5UYWckQml0MjU2IyLQT+LlKkgCAAB4cQB+AFlzcgARamF2YS51dGlsLkhhc2hNYXAFB9rBwxZg0QMAAkYACmxvYWRGYWN0b3JJAAl0aHJlc2hvbGR4cD9AAAAAAAABdwgAAAACAAAAAXNyAB5hbmFseXNpcy5pY2ZnLlNjcmF0Y2hCeXRlUmFuZ2XBTLaPpUzj2gIAAkwABGZyb21xAH4ABkwAAnRvcQB+AAZ4cHNxAH4ADP///////////////v////4AAAAAdXEAfgAQAAAAAHhzcQB+AAz///////////////7////+AAAAAXVxAH4AEAAAAAEDeHNyAC1hbmFseXNpcy5pY2ZnLkRlY29tcG9zZWRDYWxsSW5wdXRBcmckQ29uc3RhbnSFavLdQafqPQIAA0wAAWN0ABlMdmMvZGF0YS9UQUNTeW1ib2wkQ29uc3Q7TAARY29udHJhY3RSZWZlcmVuY2V0AC9MYW5hbHlzaXMvaWNmZy9DYWxsR3JhcGhCdWlsZGVyJENhbGxlZENvbnRyYWN0O0wADHNjcmF0Y2hSYW5nZXQAIExhbmFseXNpcy9pY2ZnL1NjcmF0Y2hCeXRlUmFuZ2U7eHIAJGFuYWx5c2lzLmljZmcuRGVjb21wb3NlZENhbGxJbnB1dEFy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5PcCAAJJAAVzdGFydEwAC3BhY2tlZFN0YXJ0dAAbTHZjL2RhdGEvU2NhbGFyaXphdGlvblNvcnQ7eHEAfgDpAAAAAHNyAB92Yy5kYXRhLlNjYWxhcml6YXRpb25Tb3J0JFNwbGl0VP9Zp/HHsgUCAAFMAANpZHhxAH4ABnhxAH4A6XNxAH4ADP///////////////v////4AAAABdXEAfgAQAAAAAQx4c3EAfgA2cHNxAH4ANnBzcQB+ADZwcHNxAH4AQHEAfgBGdAAcdGFjLnN0b3JhZ2Uubm9uLWluZGV4ZWQtcGF0aHZyADVhbmFseXNpcy5zdG9yYWdlLlN0b3JhZ2VBbmFseXNpc1Jlc3VsdCROb25JbmRleGVkUGF0aAjBoEuh+j9FAgAAeHBwc3IAOmFuYWx5c2lzLnN0b3JhZ2UuU3RvcmFnZUFuYWx5c2lzUmVzdWx0JE5vbkluZGV4ZWRQYXRoJFJvb3S/N/XYpeoK/wIAAUwABHNsb3RxAH4ABnhxAH4A93EAfgDwc3EAfgBAcQB+AEZ0AA10YWMuc2xvdC50eXBldnIAOnNwZWMuY3ZsYXN0LnR5cGVkZXNjcmlwdG9ycy5FVk1UeXBlRGVzY3JpcHRvciRFVk1WYWx1ZVR5cGXGia8Cuuq4JQIAAHhyAC1zcGVjLmN2bGFzdC50eXBlZGVzY3JpcHRvcnMuRVZNVHlwZURlc2NyaXB0b3LIUanxPMJqHQIAAHhwcHNyADVzcGVjLmN2bGFzdC50eXBlZGVzY3JpcHRvcnMuRVZNVHlwZURlc2NyaXB0b3IkYWRkcmVzc3r4ZfRvl6ApAgAAeHIARHNwZWMuY3ZsYXN0LnR5cGVkZXNjcmlwdG9ycy5FVk1UeXBlRGVzY3JpcHRvciRFVk1Jc29tb3JwaGljVmFsdWVUeXBl93WYkW4QoQ8CAAB4cQB+AP1zcQB+AEB+cQB+AER0AAZFcmFzZWR0ABh0YWMuc3RvcmFnZS5wcmV0dHkucGF0aHN2cgAdYW5hbHlzaXMuc3RvcmFnZS5EaXNwbGF5UGF0aHP3REu3w/VRFgIAAUwABXBhdGhzcQB+AB14cHBzcQB+AQdzcgAXamF2YS51dGlsLkxpbmtlZEhhc2hTZXTYbNdald0qHgIAAHhyABFqYXZhLnV0aWwuSGFzaFNldLpEhZWWuLc0AwAAeHB3DAAAABA/QAAAAAAAAXNyACFhbmFseXNpcy5zdG9yYWdlLkRpc3BsYXlQYXRoJFJvb3TTc6C9mdA8cgIAAkwABGJhc2V0AB5MYW5hbHlzaXMvc3RvcmFnZS9EaXNwbGF5UGF0aDtMAARuYW1lcQB+ADJ4cgAcYW5hbHlzaXMuc3RvcmFnZS5EaXNwbGF5UGF0aE9AY+pW0iAFAgAAeHBwdAAIbHBfdG9rZW54c3EAfgBAcQB+AEZ0ABV0YWMuc3RvcmFnZS5iaXQtd2lkdGhxAH4ASnBzcQB+AEkAAACgcHNxAH4AQHEAfgBGdAALdGFjLnN0b3JhZ2V2cQB+AAxwcQB+AMZwcQB+AGNwc3EAfgBJAAAD+3QAC0NBTk9ONTchITI1c3EAfgB3cQB+AGhxAH4AbXNxAH4AMHNxAH4ANnBzcQB+ADZwc3EAfgA2cHBxAH4AQ3BxAH4AS3EAfgBMcHEAfgBQcQB+AFFwcQB+AFVxAH4AVnNxAH4AXnNxAH4ANnNxAH4ANnBwcQB+AExwcQB+AGJwcQB+AGNwcQB+AI1xAH4AZnEAfgCQc3IAImphdmEudXRpbC5Db2xsZWN0aW9ucyRTaW5nbGV0b25TZXQsUkGYKcCxvwIAAUwAB2VsZW1lbnRxAH4AN3hwcQB+ABRzcQB+AF5zcQB+ADZzcQB+ADZzcQB+ADZzcQB+ADZwc3EAfgA2cHBxAH4ATHBxAH4AYnEAfgDncHEAfgDtc3EAfgA2cHNxAH4ANnBzcQB+ADZwcHEAfgD1cHEAfgD6cQB+APtwcQB+AQJxAH4BA3BzcQB+AQdzcQB+AQp3DAAAABA/QAAAAAAAAXEAfgEQeHEAfgEScHEAfgEUcHEAfgEVcHEAfgDGcHEAfgBjcHEAfgEYcQB+ARlzcQB+AHdxAH4AaHEAfgBt"}
		AnnotationCmd:56 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageGlobalChangeSnippet.StorageBackupPoint","calleeTxId":4}}
		NopCmd
		AssumeExpCmd LAnd(Eq(tacCalldatasize!!2:3 0x4 ) Eq(tacCalldatasize!!2:3 0x4 ) )
		NopCmd
		AssumeExpCmd Eq(tacCalldatabufCANON0@4:0 0x18160ddd00000000000000000000000000000000000000000000000000000000 )
		LabelCmd:56 "Start procedure CurveTokenExample-totalSupply()"
		AnnotationCmd:56 JSON{"key":{"name":"fps.free-pointer-is-scalarized","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true}
		AssignExpCmd:56 R305:54 Select(tacExtcodesize!!7:4 Apply(to_skey:bif R28:103) )
		NopCmd
		AssumeExpCmd Gt(R305:54 0x0 )
		AnnotationCmd:56 JSON{"key":{"name":"internal.func.finder.info","type":"analysis.ip.InternalFunctionFinderReport","erasureStrategy":"Erased"},"value":"rO0ABXNyAChhbmFseXNpcy5pcC5JbnRlcm5hbEZ1bmN0aW9uRmluZGVyUmVwb3J0ian+bYn1VdACAAFMABN1bnJlc29sdmVkRnVuY3Rpb25zdAAPTGphdmEvdXRpbC9TZXQ7eHBzcgAhZGF0YXN0cnVjdHVyZXMuTGlua2VkQXJyYXlIYXNoU2V0AAAAAAAAAAEDAAJGAApsb2FkRmFjdG9yTAAJaGFzaFRhYmxldAAuTGRhdGFzdHJ1Y3R1cmVzL2FycmF5aGFzaHRhYmxlL0FycmF5SGFzaFRhYmxlO3hwdwgAAAAAQAAAAHg="}
		AnnotationCmd:56 JSON{"key":{"name":"fps.free-pointer-is-scalarized","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true}
		NopCmd
		AssumeExpCmd LNot(Lt(tacCalldatasize!!2:3 0x4 ) )
		NopCmd
		AssumeExpCmd Gt(0x40c10f19 tacSighash!!37:47 )
		NopCmd
		AssumeExpCmd LNot(Eq(0x6fdde03 tacSighash!!37:47 ) )
		NopCmd
		AssumeExpCmd LNot(Eq(0x95ea7b3 tacSighash!!37:47 ) )
		NopCmd
		AssumeExpCmd Eq(0x18160ddd tacSighash!!37:47 )
		AnnotationCmd:56 JSON{"key":{"name":"internal.func.start","type":"analysis.ip.InternalFuncStartAnnotation","erasureStrategy":"CallTrace"},"value":{"id":4,"startPc":1205,"args":[],"methodSignature":{"#class":"spec.cvlast.QualifiedMethodSignature.QualifiedMethodSig","qualifiedMethodName":{"#class":"spec.cvlast.QualifiedFunction","host":{"name":"CurveTokenExample"},"methodId":"totalSupply"},"params":[],"res":[{"#class":"spec.cvlast.VMParam.Unnamed","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256}}]},"stackOffsetToArgPos":{},"callSiteSrc":{"source":2,"begin":3952,"len":364,"jumpType":"ENTER","address":"ce4604a0000000000000000000000014","sourceContext":{"indexToFilepath":{"0":"contracts/curve.sol","1":"Context.sol","2":"ERC20.sol","3":"IERC20.sol","4":"IERC20Metadata.sol","5":"ReentrancyGuard.sol"},"sourceDir":".post_autofinders.1"}}}}
		AnnotationCmd:56 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet","value":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"CANON124!!9","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.scalarization.sort","type":"vc.data.ScalarizationSort","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.ScalarizationSort.Split","idx":"2"}},{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.storage.bit-width","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":256},{"key":{"name":"tac.storage.pretty.paths","type":"analysis.storage.DisplayPaths","erasureStrategy":"Erased"},"value":{"paths":[{"#class":"analysis.storage.DisplayPath.Root","name":"_totalSupply"}]}},{"key":{"name":"tac.slot.type","type":"spec.cvlast.typedescriptors.EVMTypeDescriptor$EVMValueType","erasureStrategy":"Canonical"},"value":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256}},{"key":{"name":"tac.storage.non-indexed-path","type":"analysis.storage.StorageAnalysisResult$NonIndexedPath","erasureStrategy":"Canonical"},"value":{"#class":"analysis.storage.StorageAnalysisResult.NonIndexedPath.Root","slot":"2"}},{"key":{"name":"tac.storage","type":"java.math.BigInteger","erasureStrategy":"Canonical"},"value":"ce4604a0000000000000000000000014"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1021}]},"displayPath":{"#class":"analysis.storage.DisplayPath.Root","name":"_totalSupply"},"storageType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256},"contractInstance":"ce4604a0000000000000000000000014","linkableStorageReadId":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet.Id","id":4}}}
		AnnotationCmd:56 JSON{"key":{"name":"internal.func.end","type":"analysis.ip.InternalFuncExitAnnotation","erasureStrategy":"Canonical"},"value":{"id":4,"rets":[{"s":{"namePrefix":"CANON124!!9","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.scalarization.sort","type":"vc.data.ScalarizationSort","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.ScalarizationSort.Split","idx":"2"}},{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.storage.bit-width","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":256},{"key":{"name":"tac.storage.pretty.paths","type":"analysis.storage.DisplayPaths","erasureStrategy":"Erased"},"value":{"paths":[{"#class":"analysis.storage.DisplayPath.Root","name":"_totalSupply"}]}},{"key":{"name":"tac.slot.type","type":"spec.cvlast.typedescriptors.EVMTypeDescriptor$EVMValueType","erasureStrategy":"Canonical"},"value":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256}},{"key":{"name":"tac.storage.non-indexed-path","type":"analysis.storage.StorageAnalysisResult$NonIndexedPath","erasureStrategy":"Canonical"},"value":{"#class":"analysis.storage.StorageAnalysisResult.NonIndexedPath.Root","slot":"2"}},{"key":{"name":"tac.storage","type":"java.math.BigInteger","erasureStrategy":"Canonical"},"value":"ce4604a0000000000000000000000014"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1023}]},"offset":0}],"functionLayout":{"0":{"#class":"analysis.ip.InternalFuncValueLocation.Scalar"}}}}
		AnnotationCmd:56 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.EVMFunctionReturnWrite","returnbufOffset":"0","returnValueSym":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"CANON124!!9","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.scalarization.sort","type":"vc.data.ScalarizationSort","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.ScalarizationSort.Split","idx":"2"}},{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.storage.bit-width","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":256},{"key":{"name":"tac.storage.pretty.paths","type":"analysis.storage.DisplayPaths","erasureStrategy":"Erased"},"value":{"paths":[{"#class":"analysis.storage.DisplayPath.Root","name":"_totalSupply"}]}},{"key":{"name":"tac.slot.type","type":"spec.cvlast.typedescriptors.EVMTypeDescriptor$EVMValueType","erasureStrategy":"Canonical"},"value":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256}},{"key":{"name":"tac.storage.non-indexed-path","type":"analysis.storage.StorageAnalysisResult$NonIndexedPath","erasureStrategy":"Canonical"},"value":{"#class":"analysis.storage.StorageAnalysisResult.NonIndexedPath.Root","slot":"2"}},{"key":{"name":"tac.storage","type":"java.math.BigInteger","erasureStrategy":"Canonical"},"value":"ce4604a0000000000000000000000014"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1023}]},"callIndex":4}}
		AnnotationCmd:56 JSON{"key":{"name":"tac.return.path","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		LabelCmd:56 "End procedure CurveTokenExample-totalSupply()"
		AssignExpCmd:56 tacReturndata!!314:78 Store(tacReturndata!!532:78 0x0 CANON124!!9:104 )
		AssignExpCmd:56 tacMCANON2!!315:13 Store(tacMCANON2!!529:13 0x140 CANON124!!9:104 )
		AnnotationCmd:56 JSON{"key":{"name":"call.trace.pop","type":"analysis.icfg.Inliner$CallStack$PopRecord","erasureStrategy":"Canonical"},"value":"rO0ABXNyAClhbmFseXNpcy5pY2ZnLklubGluZXIkQ2FsbFN0YWNrJFBvcFJlY29yZPAPfwSLdCWJAgABSQAIY2FsbGVlSWR4cAAAAAQ="}
		JumpCmd:56 3_0_0_1_0_0
	}
	Block 0_0_0_7_0_0 Succ [0_0_0_8_0_0] {
		AnnotationCmd:105 JSON{"key":{"name":"call.trace.push","type":"analysis.icfg.Inliner$CallStack$PushRecord","erasureStrategy":"Canonical"},"value":"rO0ABXNyACphbmFseXNpcy5pY2ZnLklubGluZXIkQ2FsbFN0YWNrJFB1c2hSZWNvcmSX8+DCTLCH+AIAA0kACGNhbGxlZUlkTAAGY2FsbGVldAATTHZjL2RhdGEvTWV0aG9kUmVmO0wAB3N1bW1hcnl0ABVMdmMvZGF0YS9DYWxsU3VtbWFyeTt4cAAAAAdzcgARdmMuZGF0YS5NZXRob2RSZWbJlJTzzU9pGAIAA0wABGF0dHJ0ABdMc2NlbmUvTWV0aG9kQXR0cmlidXRlO0wACmNvbnRyYWN0SWR0ABZMamF2YS9tYXRoL0JpZ0ludGVnZXI7TAAHc2lnSGFzaHQAEExldm0vU2lnaGFzaEludDt4cHNyABxzY2VuZS5NZXRob2RBdHRyaWJ1dGUkQ29tbW9uNHjdebdr9XMCAAB4cgAVc2NlbmUuTWV0aG9kQXR0cmlidXRlcYg2pYWutuUCAAB4cHNyABRqYXZhLm1hdGguQmlnSW50ZWdlcoz8nx+pO/sdAwAGSQAIYml0Q291bnRJAAliaXRMZW5ndGhJABNmaXJzdE5vbnplcm9CeXRlTnVtSQAMbG93ZXN0U2V0Qml0SQAGc2lnbnVtWwAJbWFnbml0dWRldAACW0J4cgAQamF2YS5sYW5nLk51bWJlcoaslR0LlOCLAgAAeHD///////////////7////+AAAAAXVyAAJbQqzzF/gGCFTgAgAAeHAAAAAQzkYEoAAAAAAAAAAAAAAAF3hzcgAOZXZtLlNpZ2hhc2hJbnRUdcqNMXEgeAIAAUwAAW5xAH4ABnhwc3EAfgAM///////////////+/////gAAAAF1cQB+ABAAAAAE4lql+nhw"}
		AssignHavocCmd:105 tacCalldatasize!!316:3
		NopCmd
		AssumeExpCmd Apply(add_noofl:bif 0x4 0x0)
		NopCmd
		AssumeExpCmd Eq(0x4 tacCalldatasize!!316:3 )
		AssignExpCmd:105 B320 LAnd(Ge(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff CANON66:33 ) Le(0x0 CANON66:33 ) )
		AssertCmd:105 B320 "sanity bounds check on cvl to vm encoding of tacTmp!5085:int failed"
		AssignExpCmd:105 R321:54 Apply(safe_math_narrow:bif CANON66:33)
		NopCmd
		AssumeExpCmd LAnd(Le(R321:57 0xffffffffffffffffffffffffffffffffffffffff ) Ge(R321:57 0x0 ) )
		AssignExpCmd:105 B325 LAnd(Ge(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff CANON67:34 ) Le(0x0 CANON67:34 ) )
		AssertCmd:105 B325 "sanity bounds check on cvl to vm encoding of tacTmp!5088:int failed"
		AssignExpCmd:105 R326:54 Apply(safe_math_narrow:bif CANON67:34)
		NopCmd
		AssumeExpCmd LAnd(Le(R326:58 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff ) Ge(R326:58 0x0 ) )
		AssignExpCmd:105 B331 LAnd(Ge(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff CANON68:35 ) Le(0x0 CANON68:35 ) )
		AssertCmd:105 B331 "sanity bounds check on cvl to vm encoding of tacTmp!5092:int failed"
		AssignExpCmd:105 R332:54 Apply(safe_math_narrow:bif CANON68:35)
		NopCmd
		AssumeExpCmd LAnd(Le(R332:59 0xffffffffffffffffffffffffffffffffffffffff ) Ge(R332:59 0x0 ) )
		AssignExpCmd:105 B336 LAnd(Ge(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff CANON72:39 ) Le(0x0 CANON72:39 ) )
		AssertCmd:105 B336 "sanity bounds check on cvl to vm encoding of tacTmp!5095:int failed"
		AssignExpCmd:105 R337:54 Apply(safe_math_narrow:bif CANON72:39)
		NopCmd
		AssumeExpCmd LAnd(Le(R337:60 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff ) Ge(R337:60 0x0 ) )
		AssignExpCmd:105 B341 LAnd(Ge(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff CANON73:40 ) Le(0x0 CANON73:40 ) )
		AssertCmd:105 B341 "sanity bounds check on cvl to vm encoding of tacTmp!5098:int failed"
		AssignExpCmd:105 R342:54 Apply(safe_math_narrow:bif CANON73:40)
		NopCmd
		AssumeExpCmd LAnd(Le(R342:61 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff ) Ge(R342:61 0x0 ) )
		AssignExpCmd:105 B346 LAnd(Ge(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff CANON67:34 ) Le(0x0 CANON67:34 ) )
		AssertCmd:105 B346 "sanity bounds check on cvl to vm encoding of tacTmp!5101:int failed"
		AssignExpCmd:105 R347:54 Apply(safe_math_narrow:bif CANON67:34)
		AssignExpCmd:105 B349 LAnd(Ge(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff CANON66:33 ) Le(0x0 CANON66:33 ) )
		AssertCmd:105 B349 "sanity bounds check on cvl to vm encoding of tacTmp!5104:int failed"
		AssignExpCmd:105 R350:54 Apply(safe_math_narrow:bif CANON66:33)
		AssignExpCmd:105 R353:54 Select(tacBalance!!596:18 Apply(to_skey:bif R350:54) )
		AssignExpCmd:106 I354:54 IntSub(R353:54 R347:54 )
		AssignExpCmd:106 tacBalance!!355:18 Store(tacBalance!!596:18 Apply(to_skey:bif R350:54) I354:54 )
		AssignExpCmd:105 R356:54 Select(tacBalance!!355:18 Apply(to_skey:bif R30:43) )
		AssignExpCmd:106 R357:54 Add(R356:54 R347:54)
		NopCmd
		AssumeExpCmd Apply(add_noofl:bif R356:54 R347:54)
		AssignExpCmd:106 tacBalance!!359:18 Store(tacBalance!!355:18 Apply(to_skey:bif R30:43) R357:54 )
		AnnotationCmd:105 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.BalanceSnippet","srcAccountInfo":{"old":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R353","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}]},"new":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"I354","tag":{"#class":"tac.Tag.Int"},"callIndex":0,"meta":[{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}]},"addr":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R350","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}]}},"trgAccountInfo":{"old":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R356","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}]},"new":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R357","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}]},"addr":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R30","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"tacContractAt"},{"key":{"name":"tac.contract.sym.addr.name","type":"java.lang.String","erasureStrategy":"Erased"},"value":"curve"},{"key":{"name":"tac.contract.sym.addr","type":"java.math.BigInteger","erasureStrategy":"Erased"},"value":"ce4604a0000000000000000000000017"}]}},"transferredAmount":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R347","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}]}}}
		LabelCmd:105 "Start procedure curve-getVirtualPrice()"
		AnnotationCmd:105 JSON{"key":{"name":"fps.free-pointer-is-scalarized","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true}
		AssignExpCmd:105 R360:54 Select(tacExtcodesize!!7:4 Apply(to_skey:bif R30:63) )
		NopCmd
		AssumeExpCmd Gt(R360:54 0x0 )
		AnnotationCmd:105 JSON{"key":{"name":"internal.func.finder.info","type":"analysis.ip.InternalFunctionFinderReport","erasureStrategy":"Erased"},"value":"rO0ABXNyAChhbmFseXNpcy5pcC5JbnRlcm5hbEZ1bmN0aW9uRmluZGVyUmVwb3J0ian+bYn1VdACAAFMABN1bnJlc29sdmVkRnVuY3Rpb25zdAAPTGphdmEvdXRpbC9TZXQ7eHBzcgAhZGF0YXN0cnVjdHVyZXMuTGlua2VkQXJyYXlIYXNoU2V0AAAAAAAAAAEDAAJGAApsb2FkRmFjdG9yTAAJaGFzaFRhYmxldAAuTGRhdGFzdHJ1Y3R1cmVzL2FycmF5aGFzaHRhYmxlL0FycmF5SGFzaFRhYmxlO3hwdwgAAAAAQAAAAHg="}
		AnnotationCmd:105 JSON{"key":{"name":"fps.free-pointer-is-scalarized","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true}
		NopCmd
		AssumeExpCmd Eq(R326:54 0x0 )
		NopCmd
		AssumeExpCmd LNot(Lt(tacCalldatasize!!316:3 0x4 ) )
		NopCmd
		AssumeExpCmd LNot(Gt(0x82c63066 tacSighash!!40:47 ) )
		NopCmd
		AssumeExpCmd LNot(Eq(0x82c63066 tacSighash!!40:47 ) )
		NopCmd
		AssumeExpCmd LNot(Eq(0x89295a45 tacSighash!!40:47 ) )
		NopCmd
		AssumeExpCmd LNot(Eq(0x9d1e1f25 tacSighash!!40:47 ) )
		NopCmd
		AssumeExpCmd LNot(Eq(0xac8c9059 tacSighash!!40:47 ) )
		NopCmd
		AssumeExpCmd LNot(Eq(0xd802e4f7 tacSighash!!40:47 ) )
		NopCmd
		AssumeExpCmd Eq(0xe25aa5fa tacSighash!!40:47 )
		AnnotationCmd:105 JSON{"key":{"name":"internal.func.start","type":"analysis.ip.InternalFuncStartAnnotation","erasureStrategy":"CallTrace"},"value":{"id":6,"startPc":2909,"args":[],"methodSignature":{"#class":"spec.cvlast.QualifiedMethodSignature.QualifiedMethodSig","qualifiedMethodName":{"#class":"spec.cvlast.QualifiedFunction","host":{"name":"curve"},"methodId":"getVirtualPrice"},"params":[],"res":[{"#class":"spec.cvlast.VMParam.Unnamed","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256}}]},"stackOffsetToArgPos":{},"callSiteSrc":{"source":0,"begin":6452,"len":476,"jumpType":"ENTER","address":"ce4604a0000000000000000000000017","sourceContext":{"indexToFilepath":{"0":"contracts/curve.sol","1":"Context.sol","2":"ERC20.sol","3":"IERC20.sol","4":"IERC20Metadata.sol","5":"ReentrancyGuard.sol"},"sourceDir":".post_autofinders.1"}}}}
		AnnotationCmd:105 JSON{"key":{"name":"pta.end-allocation","type":"analysis.alloc.AllocationAnalysis$AbstractLocation","erasureStrategy":"Erased"},"value":{"prevFPWriteIdx":0,"nextFPWriteCmd":{"block":{"#class":"tac.BlockIdentifier","origStartPc":16,"stkTop":1024,"decompCopy":0,"calleeIdx":0,"topOfStackValue":2,"freshCopy":0},"pos":34},"sort":{"#class":"analysis.alloc.AllocationAnalysis.Alloc.ConstBlock","sz":"40"}}}
		AssignExpCmd:107 R372:65 Select(CANON115!!8:5 Apply(skey_basic:bif 0x8) )
		AnnotationCmd:105 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet","value":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R372","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1012}]},"displayPath":{"#class":"analysis.storage.DisplayPath.ArrayAccess","index":{"#class":"vc.data.TACSymbol.Const","value":"0"},"base":{"#class":"analysis.storage.DisplayPath.Root","name":"admin_balances"}},"storageType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256},"contractInstance":"ce4604a0000000000000000000000017","linkableStorageReadId":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet.None"}}}
		AssignExpCmd:108 R373:67 Select(tacBalance!!359:18 Apply(to_skey:bif R30:63) )
		NopCmd
		AssumeExpCmd LNot(Lt(R373:67 R372:65 ) )
		AssignExpCmd:109 R375:69 Sub(R373:67 R372:65 )
		AssignExpCmd:110 tacMCANON1!!376:12 Store(tacMCANON1!!14:12 0xc0 R375:69 )
		AssignExpCmd:111 R377:72 Select(CANON115!!8:5 Apply(skey_basic:bif 0x9) )
		AnnotationCmd:105 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet","value":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R377","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1013}]},"displayPath":{"#class":"analysis.storage.DisplayPath.ArrayAccess","index":{"#class":"vc.data.TACSymbol.Const","value":"1"},"base":{"#class":"analysis.storage.DisplayPath.Root","name":"admin_balances"}},"storageType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256},"contractInstance":"ce4604a0000000000000000000000017","linkableStorageReadId":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet.None"}}}
		AssignExpCmd:105 B379:54 Le(CANON56!!24:73 0xffffffffffffffffffffffffffffffffffffffff )
		AssignExpCmd:105 B380:54 Ge(CANON56!!24:73 0x0 )
		NopCmd
		AssumeExpCmd LAnd(B379:54 B380:54 )
		AnnotationCmd:105 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet","value":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"CANON56!!24","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.scalarization.sort","type":"vc.data.ScalarizationSort","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.ScalarizationSort.Packed","packedStart":{"#class":"vc.data.ScalarizationSort.Split","idx":"b"},"start":0}},{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.storage.bit-width","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":160},{"key":{"name":"tac.storage.pretty.paths","type":"analysis.storage.DisplayPaths","erasureStrategy":"Erased"},"value":{"paths":[{"#class":"analysis.storage.DisplayPath.Root","name":"coins_1"}]}},{"key":{"name":"tac.slot.type","type":"spec.cvlast.typedescriptors.EVMTypeDescriptor$EVMValueType","erasureStrategy":"Canonical"},"value":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.address"}},{"key":{"name":"tac.storage.non-indexed-path","type":"analysis.storage.StorageAnalysisResult$NonIndexedPath","erasureStrategy":"Canonical"},"value":{"#class":"analysis.storage.StorageAnalysisResult.NonIndexedPath.Root","slot":"b"}},{"key":{"name":"tac.storage","type":"java.math.BigInteger","erasureStrategy":"Canonical"},"value":"ce4604a0000000000000000000000017"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1011}]},"displayPath":{"#class":"analysis.storage.DisplayPath.Root","name":"coins_1"},"storageType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.address"},"contractInstance":"ce4604a0000000000000000000000017","linkableStorageReadId":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet.Id","id":7}}}
		AnnotationCmd:105 JSON{"key":{"name":"init.reorder.fence","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		AssignExpCmd:112 tacMCANON2!!383:14 Store(tacMCANON2!!16:14 0x100 0x70a0823100000000000000000000000000000000000000000000000000000000 )
		AssignExpCmd:113 tacMCANON2!!385:14 Store(tacMCANON2!!383:14 0x104 R30:43 )
		AssignExpCmd:112 R386:76 0x100
		AssignHavocCmd:112 R387:77
		AssignHavocCmd:105 tacReturndata!!388:78
		JumpCmd:105 0_0_0_8_0_0
	}
	Block 0_0_0_8_0_0 Succ [1_0_0_7_0_0] {
		AnnotationCmd:105 JSON{"key":{"name":"call.trace.push","type":"analysis.icfg.Inliner$CallStack$PushRecord","erasureStrategy":"Canonical"},"value":"rO0ABXNyACphbmFseXNpcy5pY2ZnLklubGluZXIkQ2FsbFN0YWNrJFB1c2hSZWNvcmSX8+DCTLCH+AIAA0kACGNhbGxlZUlkTAAGY2FsbGVldAATTHZjL2RhdGEvTWV0aG9kUmVmO0wAB3N1bW1hcnl0ABVMdmMvZGF0YS9DYWxsU3VtbWFyeTt4cAAAAAhzcgARdmMuZGF0YS5NZXRob2RSZWbJlJTzzU9pGAIAA0wABGF0dHJ0ABdMc2NlbmUvTWV0aG9kQXR0cmlidXRlO0wACmNvbnRyYWN0SWR0ABZMamF2YS9tYXRoL0JpZ0ludGVnZXI7TAAHc2lnSGFzaHQAEExldm0vU2lnaGFzaEludDt4cHNyABxzY2VuZS5NZXRob2RBdHRyaWJ1dGUkQ29tbW9uNHjdebdr9XMCAAB4cgAVc2NlbmUuTWV0aG9kQXR0cmlidXRlcYg2pYWutuUCAAB4cHNyABRqYXZhLm1hdGguQmlnSW50ZWdlcoz8nx+pO/sdAwAGSQAIYml0Q291bnRJAAliaXRMZW5ndGhJABNmaXJzdE5vbnplcm9CeXRlTnVtSQAMbG93ZXN0U2V0Qml0SQAGc2lnbnVtWwAJbWFnbml0dWRldAACW0J4cgAQamF2YS5sYW5nLk51bWJlcoaslR0LlOCLAgAAeHD///////////////7////+AAAAAXVyAAJbQqzzF/gGCFTgAgAAeHAAAAAQzkYEoAAAAAAAAAAAAAAABHhzcgAOZXZtLlNpZ2hhc2hJbnRUdcqNMXEgeAIAAUwAAW5xAH4ABnhwc3EAfgAM///////////////+/////gAAAAF1cQB+ABAAAAAEcKCCMXhzcgATdmMuZGF0YS5DYWxsU3VtbWFyeZQcmw5vl+FdAgAQSQAJc3VtbWFyeUlkTAAOY2FsbENvbnZlbnRpb250ACZMaW5zdHJ1bWVudGF0aW9uL2NhbGxzL0NhbGxDb252ZW50aW9uO0wACmNhbGxUYXJnZXR0ABpMYW5hbHlzaXMvaWNmZy9DYWxsVGFyZ2V0O0wACGNhbGxUeXBldAAVTHZjL2RhdGEvVEFDQ2FsbFR5cGU7TAAPY2Fubm90QmVJbmxpbmVkdAAtTGFuYWx5c2lzL2ljZmcvSW5saW5lciRJbGxlZ2FsSW5saW5pbmdSZWFzb247TAAGZ2FzVmFydAATTHZjL2RhdGEvVEFDU3ltYm9sO0wABmluQmFzZXEAfgAbTAAIaW5PZmZzZXRxAH4AG0wABmluU2l6ZXEAfgAbTAAMb3JpZ0NhbGxjb3JldAAgTHZjL2RhdGEvVEFDQ21kJFNpbXBsZSRDYWxsQ29yZTtMAAdvdXRCYXNlcQB+ABtMAAlvdXRPZmZzZXRxAH4AG0wAB291dFNpemVxAH4AG0wADXNpZ1Jlc29sdXRpb250AA9MamF2YS91dGlsL1NldDtMAAV0b1ZhcnEAfgAbTAAIdmFsdWVWYXJxAH4AG3hwAAAABHNyACRpbnN0cnVtZW50YXRpb24uY2FsbHMuQ2FsbENvbnZlbnRpb25HtO1ulL788QIAA0kACGNhbGxlcklkTAAFaW5wdXR0ABlMYW5hbHlzaXMvaWNmZy9DYWxsSW5wdXQ7TAAGcmF3T3V0dAAiTGluc3RydW1lbnRhdGlvbi9jYWxscy9DYWxsT3V0cHV0O3hwAAAAAHNyABdhbmFseXNpcy5pY2ZnLkNhbGxJbnB1dJjJD1MhNUxQAgAHTAAHYmFzZVZhcnQAGUx2Yy9kYXRhL1RBQ0V4cHIkU3ltJFZhcjtMABBlbmNvZGVkQXJndW1lbnRzdAAjTGFuYWx5c2lzL2ljZmcvQUJJQXJndW1lbnRFbmNvZGluZztMABNpbnB1dFNpemVMb3dlckJvdW5kcQB+AAZMAAZvZmZzZXR0ABVMdmMvZGF0YS9UQUNFeHByJFN5bTtMABRyYW5nZVRvRGVjb21wb3NlZEFyZ3QAD0xqYXZhL3V0aWwvTWFwO0wAEHNpbXBsaWZpZWRPZmZzZXR0ABtMdmMvZGF0YS9UQUNFeHByJFN5bSRDb25zdDtMAARzaXplcQB+ACZ4cHNyABd2Yy5kYXRhLlRBQ0V4cHIkU3ltJFZhcskrg43eGgPnAgACTAABc3QAF0x2Yy9kYXRhL1RBQ1N5bWJvbCRWYXI7TAADdGFndAAJTHRhYy9UYWc7eHIAE3ZjLmRhdGEuVEFDRXhwciRTeW2iVj0S4YSNUAIAAHhyAA92Yy5kYXRhLlRBQ0V4cHJYhGlUu/v+yAIAAHhwc3IANnZjLmRhdGEuVEFDU3ltYm9sJFZhciRXaXRoRGVmYXVsdENhbGxJbmRleCRXaXRoQnl0ZU1hcJ7+oHF4CHAAAgACTAAEbWV0YXQALUxrb3RsaW54L2NvbGxlY3Rpb25zL2ltbXV0YWJsZS9QZXJzaXN0ZW50TWFwO0wACm5hbWVQcmVmaXh0ABJMamF2YS9sYW5nL1N0cmluZzt4cgAVdmMuZGF0YS5UQUNTeW1ib2wkVmFyCYrCGVl9SXYCAAB4cgARdmMuZGF0YS5UQUNTeW1ib2zd3Run/CoWswIAAHhwc3IAJmRhdGFzdHJ1Y3R1cmVzLnRyZWFwLkhhc2hUcmVhcE1hcCROb2Rlf2t9acJIPnQCAANMAANrZXl0ABJMamF2YS9sYW5nL09iamVjdDtMAARuZXh0dAA1TGRhdGFzdHJ1Y3R1cmVzL3RyZWFwL0hhc2hUcmVhcE1hcCRNb3JlS2V5VmFsdWVQYWlycztMAAV2YWx1ZXEAfgA3eHIAIWRhdGFzdHJ1Y3R1cmVzLnRyZWFwLkhhc2hUcmVhcE1hcPMJ/2vt3boKAgAAeHIAHWRhdGFzdHJ1Y3R1cmVzLnRyZWFwLlRyZWFwTWFw46LAyn3v5moCAAB4cgAaZGF0YXN0cnVjdHVyZXMudHJlYXAuVHJlYXA88f21zZwbdQIAAkwABGxlZnR0ABxMZGF0YXN0cnVjdHVyZXMvdHJlYXAvVHJlYXA7TAAFcmlnaHRxAH4APHhwcHNxAH4ANnBzcQB+ADZwcHNyAAt0YWMuTWV0YUtleVF/W3MiCfIZAgADTAAPZXJhc3VyZVN0cmF0ZWd5dAAdTHRhYy9NZXRhS2V5JEVyYXN1cmVTdHJhdGVneTtMAARuYW1lcQB+ADJMAAN0eXB0ABFMamF2YS9sYW5nL0NsYXNzO3hwfnIAG3RhYy5NZXRhS2V5JEVyYXN1cmVTdHJhdGVneQAAAAAAAAAAEgAAeHIADmphdmEubGFuZy5FbnVtAAAAAAAAAAASAAB4cHQACUNhbm9uaWNhbHQAF3RhYy5tZW1vcnkucGFydGl0aW9uLWlkdnIAEWphdmEubGFuZy5JbnRlZ2VyEuKgpPeBhzgCAAFJAAV2YWx1ZXhxAH4ADnBzcQB+AEkAAAAJc3EAfgBAcQB+AEZ0ABJUYWMuc3ltYm9sLmtleXdvcmR2cgAQamF2YS5sYW5nLlN0cmluZ6DwpDh6O7NCAgAAeHBwdAAEdGFjTXNxAH4AQHEAfgBGdAANdGFjLmlzLm1lbW9yeXZyACJ0YWMuTWV0YU1hcCRDb21wYW5pb24kTm90aGluZ1ZhbHVl8nsHH85ykpUCAAB4cHBzcQB+AFN0AA90YWNNQ0FOT04yISEzODVzcgAPdGFjLlRhZyRCeXRlTWFwNb/Ry6GDRgkCAAB4cgALdGFjLlRhZyRNYXABJytzDV3P/QIAAHhyAAd0YWMuVGFnLk9V3gn2xngCAAB4cHBzcQB+AAz///////////////7////+AAAAAXVxAH4AEAAAAAEkeHNxAH4AKnNyADV2Yy5kYXRhLlRBQ1N5bWJvbCRWYXIkV2l0aERlZmF1bHRDYWxsSW5kZXgkV2l0aEJpdDI1NnqsyEgq0drPAgACTAAEbWV0YXEAfgAxTAAKbmFtZVByZWZpeHEAfgAyeHEAfgAzc3EAfgA2c3EAfgA2cHBxAH4ATHB0AAFMcHNxAH4AQHEAfgBGdAAQdGFjLnN0YWNrLmhlaWdodHEAfgBKcHNxAH4ASQAAA/B0AARSMzg2c3IADnRhYy5UYWckQml0MjU2IyLQT+LlKkgCAAB4cQB+AFlzcgARamF2YS51dGlsLkhhc2hNYXAFB9rBwxZg0QMAAkYACmxvYWRGYWN0b3JJAAl0aHJlc2hvbGR4cD9AAAAAAAADdwgAAAAEAAAAAnNyAB5hbmFseXNpcy5pY2ZnLlNjcmF0Y2hCeXRlUmFuZ2XBTLaPpUzj2gIAAkwABGZyb21xAH4ABkwAAnRvcQB+AAZ4cHNxAH4ADP///////////////v////4AAAAAdXEAfgAQAAAAAHhzcQB+AAz///////////////7////+AAAAAXVxAH4AEAAAAAEDeHNyAC1hbmFseXNpcy5pY2ZnLkRlY29tcG9zZWRDYWxsSW5wdXRBcmckQ29uc3RhbnSFavLdQafqPQIAA0wAAWN0ABlMdmMvZGF0YS9UQUNTeW1ib2wkQ29uc3Q7TAARY29udHJhY3RSZWZlcmVuY2V0AC9MYW5hbHlzaXMvaWNmZy9DYWxsR3JhcGhCdWlsZGVyJENhbGxlZENvbnRyYWN0O0wADHNjcmF0Y2hSYW5nZXQAIExhbmFseXNpcy9pY2ZnL1NjcmF0Y2hCeXRlUmFuZ2U7eHIAJGFuYWx5c2lzLmljZmcuRGVjb21wb3NlZENhbGxJbnB1dEFyZ82Nwhnirh8hAgAAeHBzcgAXdmMuZGF0YS5UQUNTeW1ib2wkQ29uc3QmHp5/l8IUcAIAAkwAA3RhZ3EAfgAsTAAFdmFsdWVxAH4ABnhxAH4ANHEAfgBoc3EAfgAM///////////////+/////gAAAAF1cQB+ABAAAAAgcKCCMQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAB4cHEAfgBsc3EAfgBrc3EAfgAM///////////////+/////gAAAAF1cQB+ABAAAAABBHhzcQB+AAz///////////////7////+AAAAAXVxAH4AEAAAAAEjeHNyAC1hbmFseXNpcy5pY2ZnLkRlY29tcG9zZWRDYWxsSW5wdXRBcmckVmFyaWFibGWV3y80jneopQIAA0wAEWNvbnRyYWN0UmVmZXJlbmNlcQB+AHNMAAxzY3JhdGNoUmFuZ2VxAH4AdEwAAXZxAH4AK3hxAH4AdXNyAERhbmFseXNpcy5pY2ZnLkNhbGxHcmFwaEJ1aWxkZXIkQ2FsbGVkQ29udHJhY3QkRnVsbHlSZXNvbHZlZCRTZWxmTGlua++8l8Aq7q6zAgABTAAKY29udHJhY3RJZHEAfgAGeHIAO2FuYWx5c2lzLmljZmcuQ2FsbEdyYXBoQnVpbGRlciRDYWxsZWRDb250cmFjdCRGdWxseVJlc29sdmVkotnIkxMAs6QCAAB4cgAtYW5hbHlzaXMuaWNmZy5DYWxsR3JhcGhCdWlsZGVyJENhbGxlZENvbnRyYWN00wt1rN/LodcCAAB4cHNxAH4ADP///////////////v////4AAAABdXEAfgAQAAAAEM5GBKAAAAAAAAAAAAAAABd4cQB+AHtzcQB+AF5zcQB+ADZwc3EAfgA2c3EAfgA2c3EAfgA2cHBxAH4ATHB0AA10YWNDb250cmFjdEF0cHNxAH4AQH5xAH4ARHQABkVyYXNlZHQAGnRhYy5jb250cmFjdC5zeW0uYWRkci5uYW1lcQB+AE9wdAAFY3VydmVwc3EAfgBAcQB+AI90ABV0YWMuY29udHJhY3Quc3ltLmFkZHJ2cQB+AAxwcQB+AIZzcQB+AEBxAH4ARnQAGHRhYy5kZWNvbXAtaW5zY2FsYXIuc29ydHZyAB10YWMuRGVjb21wb3NlZElucHV0U2NhbGFyU29ydCeGMd9jMFQFAgAAeHBwc3IAJHRhYy5EZWNvbXBvc2VkSW5wdXRTY2FsYXJTb3J0JFNpbXBsZXkHVfqoCbJbAgABTAAKYnl0ZU9mZnNldHEAfgAGeHEAfgCYcQB+AHx0AANSMzB4cHNxAH4AKnNyABp2Yy5kYXRhLlRBQ1N5bWJvbCRWYXIkRnVsbBPmPQsuB0CVAgAESQAJY2FsbEluZGV4TAAEbWV0YXEAfgAxTAAKbmFtZVByZWZpeHEAfgAyTAADdGFncQB+ACx4cQB+ADMAAAAHc3EAfgA2c3EAfgA2cHBxAH4ATHBxAH4AYnBxAH4AY3BzcQB+AEkAAAPvdAAITENBTk9OMjJxAH4AaHEAfgBoc3IAIGluc3RydW1lbnRhdGlvbi5jYWxscy5DYWxsT3V0cHV0wsWbN8G9nHsCAANMAARiYXNlcQB+ACtMAAZvZmZzZXR0ABFMdmMvZGF0YS9UQUNFeHByO0wABHNpemVxAH4ApXhwc3EAfgAwc3EAfgA2cHNxAH4ANnBzcQB+ADZwcHEAfgBDcHEAfgBLcQB+AExwcQB+AFBxAH4AUXBxAH4AVXEAfgBWc3EAfgAqc3EAfgBec3EAfgA2c3EAfgA2cHBxAH4ATHBxAH4AYnBxAH4AY3BzcQB+AEkAAAPwcQB+AGZxAH4AaHNyABl2Yy5kYXRhLlRBQ0V4cHIkU3ltJENvbnN0U0iv8zJB2nYCAAJMAAFzcQB+AHJMAAN0YWdxAH4ALHhxAH4ALXNxAH4Ad3EAfgBoc3EAfgAM///////////////+/////gAAAAF1cQB+ABAAAAABIHhxAH4AaHNyAB5hbmFseXNpcy5pY2ZnLkNhbGxUYXJnZXQkVmFsaWS5phn2PatV+gIAAUwABmNhbGxlZXEAfgBzeHIAGGFuYWx5c2lzLmljZmcuQ2FsbFRhcmdldEbdPSx8dj4lAgAAeHBzcgBHYW5hbHlzaXMuaWNmZy5DYWxsR3JhcGhCdWlsZGVyJENhbGxlZENvbnRyYWN0JEZ1bGx5UmVzb2x2ZWQkU3RvcmFnZUxpbmvSgQnS0FaL1QIAAkkADXN0b3JhZ2VSZWFkSWRMAApjb250cmFjdElkcQB+AAZ4cQB+AIMAAAAncQB+AA9+cgATdmMuZGF0YS5UQUNDYWxsVHlwZQAAAAAAAAAAEgAAeHEAfgBFdAAGU1RBVElDcHNxAH4AXnNxAH4ANnNxAH4ANnBwcQB+AExwcQB+AGJwcQB+AGNwc3EAfgBJAAAD7HQABFIzODdzcQB+ADBzcQB+ADZwc3EAfgA2cHNxAH4ANnBwcQB+AENwcQB+AEtxAH4ATHBxAH4AUHEAfgBRcHEAfgBVcQB+AFZzcQB+AF5zcQB+ADZzcQB+ADZwcHEAfgBMcHEAfgBicHEAfgBjcHEAfgBlcQB+AGZzcQB+AHdxAH4AaHEAfgBbc3IAHnZjLmRhdGEuVEFDQ21kJFNpbXBsZSRDYWxsQ29yZaEphUcEgWZ6AgALTAAIY2FsbFR5cGVxAH4AGUwAA2dhc3EAfgAbTAAGaW5CYXNlcQB+ACtMAAhpbk9mZnNldHEAfgAbTAAGaW5TaXplcQB+ABtMAARtZXRhcQB+ADFMAAdvdXRCYXNlcQB+ACtMAAlvdXRPZmZzZXRxAH4AG0wAB291dFNpemVxAH4AG0wAAnRvcQB+ABtMAAV2YWx1ZXEAfgAbeHIAFXZjLmRhdGEuVEFDQ21kJFNpbXBsZe0m1iUxBnXSAgAAeHIAE3ZjLmRhdGEuVEFDQ21kJFNwZWMbq/EA+MEDvgIAAHhyAA52Yy5kYXRhLlRBQ0NtZFTLD4g8OR/wAgAAeHBxAH4Au3NxAH4AXnNxAH4ANnNxAH4ANnBwcQB+AExwcQB+AGJwcQB+AGNwcQB+AMBxAH4AwXNxAH4AMHNxAH4ANnBzcQB+ADZwc3EAfgA2cHBxAH4AQ3BxAH4AS3EAfgBMcHEAfgBQcQB+AFFwcQB+AFVxAH4AVnNxAH4AXnNxAH4ANnNxAH4ANnBwcQB+AExwcQB+AGJwcQB+AGNwcQB+AGVxAH4AZnNxAH4AngAAAAdzcQB+ADZzcQB+ADZwcHEAfgBMcHEAfgBicHEAfgBjcHEAfgCicQB+AKNxAH4AaHNxAH4ANnBwc3EAfgBAfnEAfgBEdAAJQ2FsbFRyYWNldAAIdGFjLm1ldGF2cgATdmMuZGF0YS5UQUNNZXRhSW5mbzVgTP2lS6hxAgAGSQAFYmVnaW5JAANsZW5JAAZzb3VyY2VMAAdhZGRyZXNzcQB+AAZMAAhqdW1wVHlwZXQAE0xjb21waWxlci9KdW1wVHlwZTtMAA1zb3VyY2VDb250ZXh0dAAYTGNvbXBpbGVyL1NvdXJjZUNvbnRleHQ7eHBwc3EAfgDhAAAY6wAAACcAAAAAcQB+AIZ+cgARY29tcGlsZXIuSnVtcFR5cGUAAAAAAAAAABIAAHhxAH4ARXQAB1JFR1VMQVJzcgAWY29tcGlsZXIuU291cmNlQ29udGV4dIzLW+lAXNoTAgACTAAPaW5kZXhUb0ZpbGVwYXRocQB+ACdMAAlzb3VyY2VEaXJxAH4AMnhwc3EAfgBpP0AAAAAAAAx3CAAAABAAAAAGc3EAfgBJAAAAAHQAE2NvbnRyYWN0cy9jdXJ2ZS5zb2xzcQB+AEkAAAABdAALQ29udGV4dC5zb2xzcQB+AEkAAAACdAAJRVJDMjAuc29sc3EAfgBJAAAAA3QACklFUkMyMC5zb2xzcQB+AEkAAAAEdAASSUVSQzIwTWV0YWRhdGEuc29sc3EAfgBJAAAABXQAE1JlZW50cmFuY3lHdWFyZC5zb2x4dAATLnBvc3RfYXV0b2ZpbmRlcnMuMXNxAH4AMHNxAH4ANnBzcQB+ADZwc3EAfgA2cHBxAH4AQ3BxAH4AS3EAfgBMcHEAfgBQcQB+AFFwcQB+AFVxAH4AVnNxAH4AXnNxAH4ANnNxAH4ANnBwcQB+AExwcQB+AGJwcQB+AGNwcQB+AK9xAH4AZnEAfgCyc3EAfgBec3EAfgA2c3EAfgA2c3EAfgA2c3EAfgA2cHNxAH4ANnBwcQB+AExwcQB+AGJzcQB+AEBxAH4ARnQAFnRhYy5zY2FsYXJpemF0aW9uLnNvcnR2cgAZdmMuZGF0YS5TY2FsYXJpemF0aW9uU29ydDDOcJ3kaA0mAgAAeHBwc3IAIHZjLmRhdGEuU2NhbGFyaXphdGlvblNvcnQkUGFja2VkLkWtEpOI5PcCAAJJAAVzdGFydEwAC3BhY2tlZFN0YXJ0dAAbTHZjL2RhdGEvU2NhbGFyaXphdGlvblNvcnQ7eHEAfgEIAAAAAHNyAB92Yy5kYXRhLlNjYWxhcml6YXRpb25Tb3J0JFNwbGl0VP9Zp/HHsgUCAAFMAANpZHhxAH4ABnhxAH4BCHNxAH4ADP///////////////v////4AAAABdXEAfgAQAAAAAQt4c3EAfgA2cHNxAH4ANnBzcQB+ADZwcHNxAH4AQHEAfgBGdAAcdGFjLnN0b3JhZ2Uubm9uLWluZGV4ZWQtcGF0aHZyADVhbmFseXNpcy5zdG9yYWdlLlN0b3JhZ2VBbmFseXNpc1Jlc3VsdCROb25JbmRleGVkUGF0aAjBoEuh+j9FAgAAeHBwc3IAOmFuYWx5c2lzLnN0b3JhZ2UuU3RvcmFnZUFuYWx5c2lzUmVzdWx0JE5vbkluZGV4ZWRQYXRoJFJvb3S/N/XYpeoK/wIAAUwABHNsb3RxAH4ABnhxAH4BFnEAfgEPc3EAfgBAcQB+AEZ0AA10YWMuc2xvdC50eXBldnIAOnNwZWMuY3ZsYXN0LnR5cGVkZXNjcmlwdG9ycy5FVk1UeXBlRGVzY3JpcHRvciRFVk1WYWx1ZVR5cGXGia8Cuuq4JQIAAHhyAC1zcGVjLmN2bGFzdC50eXBlZGVzY3JpcHRvcnMuRVZNVHlwZURlc2NyaXB0b3LIUanxPMJqHQIAAHhwcHNyADVzcGVjLmN2bGFzdC50eXBlZGVzY3JpcHRvcnMuRVZNVHlwZURlc2NyaXB0b3IkYWRkcmVzc3r4ZfRvl6ApAgAAeHIARHNwZWMuY3ZsYXN0LnR5cGVkZXNjcmlwdG9ycy5FVk1UeXBlRGVzY3JpcHRvciRFVk1Jc29tb3JwaGljVmFsdWVUeXBl93WYkW4QoQ8CAAB4cQB+ARxzcQB+AEBxAH4Aj3QAGHRhYy5zdG9yYWdlLnByZXR0eS5wYXRoc3ZyAB1hbmFseXNpcy5zdG9yYWdlLkRpc3BsYXlQYXRoc/dES7fD9VEWAgABTAAFcGF0aHNxAH4AHXhwcHNxAH4BJHNyABdqYXZhLnV0aWwuTGlua2VkSGFzaFNldNhs11qV3SoeAgAAeHIAEWphdmEudXRpbC5IYXNoU2V0ukSFlZa4tzQDAAB4cHcMAAAAED9AAAAAAAABc3IAIWFuYWx5c2lzLnN0b3JhZ2UuRGlzcGxheVBhdGgkUm9vdNNzoL2Z0DxyAgACTAAEYmFzZXQAHkxhbmFseXNpcy9zdG9yYWdlL0Rpc3BsYXlQYXRoO0wABG5hbWVxAH4AMnhyABxhbmFseXNpcy5zdG9yYWdlLkRpc3BsYXlQYXRoT0Bj6lbSIAUCAAB4cHB0AAdjb2luc18xeHNxAH4AQHEAfgBGdAAVdGFjLnN0b3JhZ2UuYml0LXdpZHRocQB+AEpwc3EAfgBJAAAAoHBzcQB+AEBxAH4ARnQAC3RhYy5zdG9yYWdlcQB+AJVwcQB+AIZwcQB+AGNwc3EAfgBJAAAD9HQAC0NBTk9ONTYhITI0c3EAfgB3cQB+AGhxAH4AbXNxAH4AMHNxAH4ANnBzcQB+ADZwc3EAfgA2cHBxAH4AQ3BxAH4AS3EAfgBMcHEAfgBQcQB+AFFwcQB+AFVxAH4AVnNxAH4AXnNxAH4ANnNxAH4ANnBwcQB+AExwcQB+AGJwcQB+AGNwcQB+AK9xAH4AZnEAfgCyc3IAImphdmEudXRpbC5Db2xsZWN0aW9ucyRTaW5nbGV0b25TZXQsUkGYKcCxvwIAAUwAB2VsZW1lbnRxAH4AN3hwcQB+ABRzcQB+AF5zcQB+ADZzcQB+ADZzcQB+ADZzcQB+ADZwc3EAfgA2cHBxAH4ATHBxAH4AYnEAfgEGcHEAfgEMc3EAfgA2cHNxAH4ANnBzcQB+ADZwcHEAfgEUcHEAfgEZcQB+ARpwcQB+ASFxAH4BInBzcQB+ASRzcQB+ASd3DAAAABA/QAAAAAAAAXEAfgEteHEAfgEvcHEAfgExcHEAfgEycHEAfgCGcHEAfgBjcHEAfgE0cQB+ATVzcQB+AHdxAH4AaHEAfgBt"}
		AnnotationCmd:105 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageGlobalChangeSnippet.StorageBackupPoint","calleeTxId":8}}
		NopCmd
		AssumeExpCmd LAnd(Eq(tacCalldatasize!!4:3 0x24 ) Eq(tacCalldatasize!!4:3 0x24 ) )
		NopCmd
		AssumeExpCmd Eq(tacCalldatabufCANON0@8:2 0x70a0823100000000000000000000000000000000000000000000000000000000 )
		AssignExpCmd:105 tacCalldatabufCANON1@8:114 R30:80
		LabelCmd:105 "Start procedure ERC20-balanceOf(address)"
		AnnotationCmd:105 JSON{"key":{"name":"fps.free-pointer-is-scalarized","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true}
		AssignExpCmd:105 R392:54 Select(tacExtcodesize!!7:4 Apply(to_skey:bif R29:81) )
		NopCmd
		AssumeExpCmd Gt(R392:54 0x0 )
		AnnotationCmd:105 JSON{"key":{"name":"internal.func.finder.info","type":"analysis.ip.InternalFunctionFinderReport","erasureStrategy":"Erased"},"value":"rO0ABXNyAChhbmFseXNpcy5pcC5JbnRlcm5hbEZ1bmN0aW9uRmluZGVyUmVwb3J0ian+bYn1VdACAAFMABN1bnJlc29sdmVkRnVuY3Rpb25zdAAPTGphdmEvdXRpbC9TZXQ7eHBzcgAhZGF0YXN0cnVjdHVyZXMuTGlua2VkQXJyYXlIYXNoU2V0AAAAAAAAAAEDAAJGAApsb2FkRmFjdG9yTAAJaGFzaFRhYmxldAAuTGRhdGFzdHJ1Y3R1cmVzL2FycmF5aGFzaHRhYmxlL0FycmF5SGFzaFRhYmxlO3hwdwgAAAAAQAAAAHg="}
		AnnotationCmd:105 JSON{"key":{"name":"fps.free-pointer-is-scalarized","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true}
		NopCmd
		AssumeExpCmd LNot(Lt(tacCalldatasize!!4:3 0x4 ) )
		NopCmd
		AssumeExpCmd LNot(Gt(0x39509351 tacSighash!!41:47 ) )
		NopCmd
		AssumeExpCmd LNot(Eq(0x39509351 tacSighash!!41:47 ) )
		NopCmd
		AssumeExpCmd Eq(0x70a08231 tacSighash!!41:47 )
		AssignExpCmd:115 R398:83 Sub(tacCalldatasize!!4:3 0x4 )
		AssignExpCmd:105 B399:84 Slt(R398:83 0x20 )
		NopCmd
		AssumeExpCmd LNot(B399:84 )
		AssignExpCmd:116 R401:72 tacCalldatabufCANON1@8:117
		NopCmd
		AssumeExpCmd Eq(tacCalldatabufCANON1@8:117 tacCalldatabufCANON1@8:117 )
		AnnotationCmd:105 JSON{"key":{"name":"internal.func.start","type":"analysis.ip.InternalFuncStartAnnotation","erasureStrategy":"CallTrace"},"value":{"id":7,"startPc":1712,"args":[{"s":{"namePrefix":"R401","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1013}]},"offset":1,"sort":"SCALAR"}],"methodSignature":{"#class":"spec.cvlast.QualifiedMethodSignature.QualifiedMethodSig","qualifiedMethodName":{"#class":"spec.cvlast.QualifiedFunction","host":{"name":"ERC20"},"methodId":"balanceOf"},"params":[{"#class":"spec.cvlast.VMParam.Named","name":"account","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$address"}}],"res":[{"#class":"spec.cvlast.VMParam.Unnamed","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256}}]},"stackOffsetToArgPos":{"1":0},"callSiteSrc":{"source":0,"begin":4374,"len":467,"jumpType":"ENTER","address":"ce4604a0000000000000000000000004","sourceContext":{"indexToFilepath":{"0":"contracts/ERC20.sol","1":"contracts/IERC20Metadata.sol","2":"Context.sol","3":"IERC20.sol"},"sourceDir":".post_autofinders.0"}}}}
		AssignExpCmd:118 R406:88 Apply(hash_3_keccak:bif Apply(skey_basic:bif 0x40) Apply(to_skey:bif tacCalldatabufCANON1@8:117) Apply(skey_basic:bif 0x0))
		AssignExpCmd:119 R407:88 Select(CANON130!!10:7 R406:120 )
		AnnotationCmd:105 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet","value":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R407","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1020}]},"displayPath":{"#class":"analysis.storage.DisplayPath.MapAccess","key":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R401","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1018}]},"keyTyp":{"#class":"tac.TACStorageType.IntegralType","typeLabel":"address","numBytes":"14","descriptor":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$address"},"lowerBound":null,"upperBound":null},"base":{"#class":"analysis.storage.DisplayPath.Root","name":"_balances"}},"storageType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256},"contractInstance":"ce4604a0000000000000000000000004","linkableStorageReadId":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet.None"}}}
		AnnotationCmd:105 JSON{"key":{"name":"internal.func.end","type":"analysis.ip.InternalFuncExitAnnotation","erasureStrategy":"Canonical"},"value":{"id":7,"rets":[{"s":{"namePrefix":"R407","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1023}]},"offset":0}],"functionLayout":{"0":{"#class":"analysis.ip.InternalFuncValueLocation.Scalar"}}}}
		AnnotationCmd:105 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.EVMFunctionReturnWrite","returnbufOffset":"0","returnValueSym":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R407","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1023}]},"callIndex":8}}
		AnnotationCmd:105 JSON{"key":{"name":"tac.return.path","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		LabelCmd:105 "End procedure ERC20-balanceOf(address)"
		AssignExpCmd:105 tacReturndata!!409:78 Store(tacReturndata!!388:78 0x0 R407:88 )
		AssignExpCmd:105 tacMCANON2!!410:14 Store(tacMCANON2!!385:14 0x100 R407:88 )
		AnnotationCmd:105 JSON{"key":{"name":"call.trace.pop","type":"analysis.icfg.Inliner$CallStack$PopRecord","erasureStrategy":"Canonical"},"value":"rO0ABXNyAClhbmFseXNpcy5pY2ZnLklubGluZXIkQ2FsbFN0YWNrJFBvcFJlY29yZPAPfwSLdCWJAgABSQAIY2FsbGVlSWR4cAAAAAg="}
		JumpCmd:105 1_0_0_7_0_0
	}
	Block 0_0_0_9_0_0 Succ [2_0_0_7_0_0] {
		AnnotationCmd:105 JSON{"key":{"name":"call.trace.push","type":"analysis.icfg.Inliner$CallStack$PushRecord","erasureStrategy":"Canonical"},"value":"rO0ABXNyACphbmFseXNpcy5pY2ZnLklubGluZXIkQ2FsbFN0YWNrJFB1c2hSZWNvcmSX8+DCTLCH+AIAA0kACGNhbGxlZUlkTAAGY2FsbGVldAATTHZjL2RhdGEvTWV0aG9kUmVmO0wAB3N1bW1hcnl0ABVMdmMvZGF0YS9DYWxsU3VtbWFyeTt4cAAAAAlzcgARdmMuZGF0YS5NZXRob2RSZWbJlJTzzU9pGAIAA0wABGF0dHJ0ABdMc2NlbmUvTWV0aG9kQXR0cmlidXRlO0wACmNvbnRyYWN0SWR0ABZMamF2YS9tYXRoL0JpZ0ludGVnZXI7TAAHc2lnSGFzaHQAEExldm0vU2lnaGFzaEludDt4cHNyABxzY2VuZS5NZXRob2RBdHRyaWJ1dGUkQ29tbW9uNHjdebdr9XMCAAB4cgAVc2NlbmUuTWV0aG9kQXR0cmlidXRlcYg2pYWutuUCAAB4cHNyABRqYXZhLm1hdGguQmlnSW50ZWdlcoz8nx+pO/sdAwAGSQAIYml0Q291bnRJAAliaXRMZW5ndGhJABNmaXJzdE5vbnplcm9CeXRlTnVtSQAMbG93ZXN0U2V0Qml0SQAGc2lnbnVtWwAJbWFnbml0dWRldAACW0J4cgAQamF2YS5sYW5nLk51bWJlcoaslR0LlOCLAgAAeHD///////////////7////+AAAAAXVyAAJbQqzzF/gGCFTgAgAAeHAAAAAQzkYEoAAAAAAAAAAAAAAAF3hzcgAOZXZtLlNpZ2hhc2hJbnRUdcqNMXEgeAIAAUwAAW5xAH4ABnhwc3EAfgAM///////////////+/////gAAAAF1cQB+ABAAAAAEOEL3dnhzcgATdmMuZGF0YS5DYWxsU3VtbWFyeZQcmw5vl+FdAgAQSQAJc3VtbWFyeUlkTAAOY2FsbENvbnZlbnRpb250ACZMaW5zdHJ1bWVudGF0aW9uL2NhbGxzL0NhbGxDb252ZW50aW9uO0wACmNhbGxUYXJnZXR0ABpMYW5hbHlzaXMvaWNmZy9DYWxsVGFyZ2V0O0wACGNhbGxUeXBldAAVTHZjL2RhdGEvVEFDQ2FsbFR5cGU7TAAPY2Fubm90QmVJbmxpbmVkdAAtTGFuYWx5c2lzL2ljZmcvSW5saW5lciRJbGxlZ2FsSW5saW5pbmdSZWFzb247TAAGZ2FzVmFydAATTHZjL2RhdGEvVEFDU3ltYm9sO0wABmluQmFzZXEAfgAbTAAIaW5PZmZzZXRxAH4AG0wABmluU2l6ZXEAfgAbTAAMb3JpZ0NhbGxjb3JldAAgTHZjL2RhdGEvVEFDQ21kJFNpbXBsZSRDYWxsQ29yZTtMAAdvdXRCYXNlcQB+ABtMAAlvdXRPZmZzZXRxAH4AG0wAB291dFNpemVxAH4AG0wADXNpZ1Jlc29sdXRpb250AA9MamF2YS91dGlsL1NldDtMAAV0b1ZhcnEAfgAbTAAIdmFsdWVWYXJxAH4AG3hwAAAABXNyACRpbnN0cnVtZW50YXRpb24uY2FsbHMuQ2FsbENvbnZlbnRpb25HtO1ulL788QIAA0kACGNhbGxlcklkTAAFaW5wdXR0ABlMYW5hbHlzaXMvaWNmZy9DYWxsSW5wdXQ7TAAGcmF3T3V0dAAiTGluc3RydW1lbnRhdGlvbi9jYWxscy9DYWxsT3V0cHV0O3hwAAAAAHNyABdhbmFseXNpcy5pY2ZnLkNhbGxJbnB1dJjJD1MhNUxQAgAHTAAHYmFzZVZhcnQAGUx2Yy9kYXRhL1RBQ0V4cHIkU3ltJFZhcjtMABBlbmNvZGVkQXJndW1lbnRzdAAjTGFuYWx5c2lzL2ljZmcvQUJJQXJndW1lbnRFbmNvZGluZztMABNpbnB1dFNpemVMb3dlckJvdW5kcQB+AAZMAAZvZmZzZXR0ABVMdmMvZGF0YS9UQUNFeHByJFN5bTtMABRyYW5nZVRvRGVjb21wb3NlZEFyZ3QAD0xqYXZhL3V0aWwvTWFwO0wAEHNpbXBsaWZpZWRPZmZzZXR0ABtMdmMvZGF0YS9UQUNFeHByJFN5bSRDb25zdDtMAARzaXplcQB+ACZ4cHNyABd2Yy5kYXRhLlRBQ0V4cHIkU3ltJFZhcskrg43eGgPnAgACTAABc3QAF0x2Yy9kYXRhL1RBQ1N5bWJvbCRWYXI7TAADdGFndAAJTHRhYy9UYWc7eHIAE3ZjLmRhdGEuVEFDRXhwciRTeW2iVj0S4YSNUAIAAHhyAA92Yy5kYXRhLlRBQ0V4cHJYhGlUu/v+yAIAAHhwc3IANnZjLmRhdGEuVEFDU3ltYm9sJFZhciRXaXRoRGVmYXVsdENhbGxJbmRleCRXaXRoQnl0ZU1hcJ7+oHF4CHAAAgACTAAEbWV0YXQALUxrb3RsaW54L2NvbGxlY3Rpb25zL2ltbXV0YWJsZS9QZXJzaXN0ZW50TWFwO0wACm5hbWVQcmVmaXh0ABJMamF2YS9sYW5nL1N0cmluZzt4cgAVdmMuZGF0YS5UQUNTeW1ib2wkVmFyCYrCGVl9SXYCAAB4cgARdmMuZGF0YS5UQUNTeW1ib2zd3Run/CoWswIAAHhwc3IAJmRhdGFzdHJ1Y3R1cmVzLnRyZWFwLkhhc2hUcmVhcE1hcCROb2Rlf2t9acJIPnQCAANMAANrZXl0ABJMamF2YS9sYW5nL09iamVjdDtMAARuZXh0dAA1TGRhdGFzdHJ1Y3R1cmVzL3RyZWFwL0hhc2hUcmVhcE1hcCRNb3JlS2V5VmFsdWVQYWlycztMAAV2YWx1ZXEAfgA3eHIAIWRhdGFzdHJ1Y3R1cmVzLnRyZWFwLkhhc2hUcmVhcE1hcPMJ/2vt3boKAgAAeHIAHWRhdGFzdHJ1Y3R1cmVzLnRyZWFwLlRyZWFwTWFw46LAyn3v5moCAAB4cgAaZGF0YXN0cnVjdHVyZXMudHJlYXAuVHJlYXA88f21zZwbdQIAAkwABGxlZnR0ABxMZGF0YXN0cnVjdHVyZXMvdHJlYXAvVHJlYXA7TAAFcmlnaHRxAH4APHhwcHNxAH4ANnBzcQB+ADZwcHNyAAt0YWMuTWV0YUtleVF/W3MiCfIZAgADTAAPZXJhc3VyZVN0cmF0ZWd5dAAdTHRhYy9NZXRhS2V5JEVyYXN1cmVTdHJhdGVneTtMAARuYW1lcQB+ADJMAAN0eXB0ABFMamF2YS9sYW5nL0NsYXNzO3hwfnIAG3RhYy5NZXRhS2V5JEVyYXN1cmVTdHJhdGVneQAAAAAAAAAAEgAAeHIADmphdmEubGFuZy5FbnVtAAAAAAAAAAASAAB4cHQACUNhbm9uaWNhbHQAF3RhYy5tZW1vcnkucGFydGl0aW9uLWlkdnIAEWphdmEubGFuZy5JbnRlZ2VyEuKgpPeBhzgCAAFJAAV2YWx1ZXhxAH4ADnBzcQB+AEkAAAAJc3EAfgBAcQB+AEZ0ABJUYWMuc3ltYm9sLmtleXdvcmR2cgAQamF2YS5sYW5nLlN0cmluZ6DwpDh6O7NCAgAAeHBwdAAEdGFjTXNxAH4AQHEAfgBGdAANdGFjLmlzLm1lbW9yeXZyACJ0YWMuTWV0YU1hcCRDb21wYW5pb24kTm90aGluZ1ZhbHVl8nsHH85ykpUCAAB4cHBzcQB+AFN0AA90YWNNQ0FOT04yISE0ODhzcgAPdGFjLlRhZyRCeXRlTWFwNb/Ry6GDRgkCAAB4cgALdGFjLlRhZyRNYXABJytzDV3P/QIAAHhyAAd0YWMuVGFnLk9V3gn2xngCAAB4cHBzcQB+AAz///////////////7////+AAAAAXVxAH4AEAAAAAFkeHNxAH4AKnNyADV2Yy5kYXRhLlRBQ1N5bWJvbCRWYXIkV2l0aERlZmF1bHRDYWxsSW5kZXgkV2l0aEJpdDI1NnqsyEgq0drPAgACTAAEbWV0YXEAfgAxTAAKbmFtZVByZWZpeHEAfgAyeHEAfgAzc3EAfgA2c3EAfgA2cHBxAH4ATHB0AAFMcHNxAH4AQHEAfgBGdAAQdGFjLnN0YWNrLmhlaWdodHEAfgBKcHNxAH4ASQAAA/h0AARSNDg5c3IADnRhYy5UYWckQml0MjU2IyLQT+LlKkgCAAB4cQB+AFlzcgARamF2YS51dGlsLkhhc2hNYXAFB9rBwxZg0QMAAkYACmxvYWRGYWN0b3JJAAl0aHJlc2hvbGR4cD9AAAAAAAADdwgAAAAEAAAAAnNyAB5hbmFseXNpcy5pY2ZnLlNjcmF0Y2hCeXRlUmFuZ2XBTLaPpUzj2gIAAkwABGZyb21xAH4ABkwAAnRvcQB+AAZ4cHNxAH4ADP///////////////v////4AAAAAdXEAfgAQAAAAAHhzcQB+AAz///////////////7////+AAAAAXVxAH4AEAAAAAEDeHNyAC1hbmFseXNpcy5pY2ZnLkRlY29tcG9zZWRDYWxsSW5wdXRBcmckQ29uc3RhbnSFavLdQafqPQIAA0wAAWN0ABlMdmMvZGF0YS9UQUNTeW1ib2wkQ29uc3Q7TAARY29udHJhY3RSZWZlcmVuY2V0AC9MYW5hbHlzaXMvaWNmZy9DYWxsR3JhcGhCdWlsZGVyJENhbGxlZENvbnRyYWN0O0wADHNjcmF0Y2hSYW5nZXQAIExhbmFseXNpcy9pY2ZnL1NjcmF0Y2hCeXRlUmFuZ2U7eHIAJGFuYWx5c2lzLmljZmcuRGVjb21wb3NlZENhbGxJbnB1dEFyZ82Nwhnirh8hAgAAeHBzcgAXdmMuZGF0YS5UQUNTeW1ib2wkQ29uc3QmHp5/l8IUcAIAAkwAA3RhZ3EAfgAsTAAFdmFsdWVxAH4ABnhxAH4ANHEAfgBoc3EAfgAM///////////////+/////gAAAAF1cQB+ABAAAAAgOEL3dgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAB4cHEAfgBsc3EAfgBrc3EAfgAM///////////////+/////gAAAAF1cQB+ABAAAAABRHhzcQB+AAz///////////////7////+AAAAAXVxAH4AEAAAAAFjeHNyAC1hbmFseXNpcy5pY2ZnLkRlY29tcG9zZWRDYWxsSW5wdXRBcmckVmFyaWFibGWV3y80jneopQIAA0wAEWNvbnRyYWN0UmVmZXJlbmNlcQB+AHNMAAxzY3JhdGNoUmFuZ2VxAH4AdEwAAXZxAH4AK3hxAH4AdXNyADxhbmFseXNpcy5pY2ZnLkNhbGxHcmFwaEJ1aWxkZXIkQ2FsbGVkQ29udHJhY3QkVW5yZXNvbHZlZFJlYWRDhKJZ0RDzoAIAAUkADXN0b3JhZ2VSZWFkSWR4cgAtYW5hbHlzaXMuaWNmZy5DYWxsR3JhcGhCdWlsZGVyJENhbGxlZENvbnRyYWN00wt1rN/LodcCAAB4cAAAAAlxAH4Ae3NxAH4AXnNxAH4ANnNxAH4ANnBzcQB+ADZzcQB+ADZzcQB+ADZwc3EAfgA2cHBxAH4ATHBxAH4AYnNxAH4AQHEAfgBGdAAWdGFjLnNjYWxhcml6YXRpb24uc29ydHZyABl2Yy5kYXRhLlNjYWxhcml6YXRpb25Tb3J0MM5wneRoDSYCAAB4cHBzcgAfdmMuZGF0YS5TY2FsYXJpemF0aW9uU29ydCRTcGxpdFT/Wafxx7IFAgABTAADaWR4cQB+AAZ4cQB+AI5zcQB+AAz///////////////7////+AAAAAXVxAH4AEAAAAAEFeHNxAH4ANnBzcQB+ADZwc3EAfgA2cHBzcQB+AEBxAH4ARnQAHHRhYy5zdG9yYWdlLm5vbi1pbmRleGVkLXBhdGh2cgA1YW5hbHlzaXMuc3RvcmFnZS5TdG9yYWdlQW5hbHlzaXNSZXN1bHQkTm9uSW5kZXhlZFBhdGgIwaBLofo/RQIAAHhwcHNyADphbmFseXNpcy5zdG9yYWdlLlN0b3JhZ2VBbmFseXNpc1Jlc3VsdCROb25JbmRleGVkUGF0aCRSb290vzf12KXqCv8CAAFMAARzbG90cQB+AAZ4cQB+AJlxAH4AknNxAH4AQHEAfgBGdAANdGFjLnNsb3QudHlwZXZyADpzcGVjLmN2bGFzdC50eXBlZGVzY3JpcHRvcnMuRVZNVHlwZURlc2NyaXB0b3IkRVZNVmFsdWVUeXBlxomvArrquCUCAAB4cgAtc3BlYy5jdmxhc3QudHlwZWRlc2NyaXB0b3JzLkVWTVR5cGVEZXNjcmlwdG9yyFGp8TzCah0CAAB4cHBzcgAzc3BlYy5jdmxhc3QudHlwZWRlc2NyaXB0b3JzLkVWTVR5cGVEZXNjcmlwdG9yJFVJbnRL+xQfR/Nlf8ACAAFJAAhiaXR3aWR0aHhyAERzcGVjLmN2bGFzdC50eXBlZGVzY3JpcHRvcnMuRVZNVHlwZURlc2NyaXB0b3IkRVZNSXNvbW9ycGhpY1ZhbHVlVHlwZfd1mJFuEKEPAgAAeHEAfgCfAAABAHNxAH4AQH5xAH4ARHQABkVyYXNlZHQAGHRhYy5zdG9yYWdlLnByZXR0eS5wYXRoc3ZyAB1hbmFseXNpcy5zdG9yYWdlLkRpc3BsYXlQYXRoc/dES7fD9VEWAgABTAAFcGF0aHNxAH4AHXhwcHNxAH4AqXNyABdqYXZhLnV0aWwuTGlua2VkSGFzaFNldNhs11qV3SoeAgAAeHIAEWphdmEudXRpbC5IYXNoU2V0ukSFlZa4tzQDAAB4cHcMAAAAED9AAAAAAAABc3IAIWFuYWx5c2lzLnN0b3JhZ2UuRGlzcGxheVBhdGgkUm9vdNNzoL2Z0DxyAgACTAAEYmFzZXQAHkxhbmFseXNpcy9zdG9yYWdlL0Rpc3BsYXlQYXRoO0wABG5hbWVxAH4AMnhyABxhbmFseXNpcy5zdG9yYWdlLkRpc3BsYXlQYXRoT0Bj6lbSIAUCAAB4cHB0AAhmdXR1cmVfQXhzcQB+AEBxAH4ARnQAFXRhYy5zdG9yYWdlLmJpdC13aWR0aHEAfgBKcHNxAH4ASQAAAQBwc3EAfgBAcQB+AEZ0AAt0YWMuc3RvcmFnZXZxAH4ADHBxAH4AD3NxAH4AQHEAfgBGdAAYdGFjLmRlY29tcC1p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"}
		AnnotationCmd:105 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageGlobalChangeSnippet.StorageBackupPoint","calleeTxId":9}}
		NopCmd
		AssumeExpCmd LAnd(Eq(tacCalldatasize!!5:3 0x64 ) Eq(tacCalldatasize!!5:3 0x64 ) )
		AssignExpCmd:105 B413:54 Eq(Select(tacCalldatabuf!!23@9:121 0x0 ) 0x3842f77600000000000000000000000000000000000000000000000000000000 )
		AssumeCmd:105 B413:54
		AssignExpCmd:105 tacCalldatabuf!!414@9:22 LongStore(tacCalldatabuf!!23@9:121 0x4 tacMCANON2!!488:14 0x124 Sub(0x64 0x4 ) )
		LabelCmd:105 "Start procedure curve-get_D(uint256[2],uint256)"
		AnnotationCmd:105 JSON{"key":{"name":"fps.free-pointer-is-scalarized","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true}
		AssignExpCmd:105 R415:54 Select(tacExtcodesize!!7:4 Apply(to_skey:bif R30:63) )
		NopCmd
		AssumeExpCmd Gt(R415:54 0x0 )
		AnnotationCmd:105 JSON{"key":{"name":"internal.func.finder.info","type":"analysis.ip.InternalFunctionFinderReport","erasureStrategy":"Erased"},"value":"rO0ABXNyAChhbmFseXNpcy5pcC5JbnRlcm5hbEZ1bmN0aW9uRmluZGVyUmVwb3J0ian+bYn1VdACAAFMABN1bnJlc29sdmVkRnVuY3Rpb25zdAAPTGphdmEvdXRpbC9TZXQ7eHBzcgAhZGF0YXN0cnVjdHVyZXMuTGlua2VkQXJyYXlIYXNoU2V0AAAAAAAAAAEDAAJGAApsb2FkRmFjdG9yTAAJaGFzaFRhYmxldAAuTGRhdGFzdHJ1Y3R1cmVzL2FycmF5aGFzaHRhYmxlL0FycmF5SGFzaFRhYmxlO3hwdwgAAAAAQAAAAHg="}
		AnnotationCmd:105 JSON{"key":{"name":"fps.free-pointer-is-scalarized","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true}
		NopCmd
		AssumeExpCmd LNot(Lt(tacCalldatasize!!5:3 0x4 ) )
		NopCmd
		AssumeExpCmd Gt(0x82c63066 tacSighash!!42:47 )
		NopCmd
		AssumeExpCmd Eq(0x3842f776 tacSighash!!42:47 )
		AssignExpCmd:122 R421:93 Sub(tacCalldatasize!!5:3 0x4 )
		AssignExpCmd:105 B422:83 Slt(R421:93 0x60 )
		NopCmd
		AssumeExpCmd LNot(B422:83 )
		NopCmd
		AssumeExpCmd Slt(0x23 tacCalldatasize!!5:94 )
		AssignExpCmd:123 R426:96 0x80
		AssumeCmd:124 true
		AssignExpCmd:105 B427:77 Gt(0x44 tacCalldatasize!!5:94 )
		NopCmd
		AssumeExpCmd LNot(B427:77 )
		AnnotationCmd:105 JSON{"key":{"name":"dsa.assign.start","type":"java.lang.String","erasureStrategy":"Erased"},"value":"4280_1005_0_0_0_0 -> 4282_1004_0_0_0_0"}
		LabelCmd:105 "Parallel assignment for R3573:bv256, R3574:bv256 := R2326:bv256, R3653:bv256"
		AnnotationCmd:105 JSON{"key":{"name":"dsa.assign.end","type":"java.lang.String","erasureStrategy":"Erased"},"value":"4280_1005_0_0_0_0 -> 4282_1004_0_0_0_0"}
		AnnotationCmd:105 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.LoopSnippet.StartLoopSnippet","loopIndex":4,"loopSource":"unknown loop source code"}}
		AnnotationCmd:105 JSON{"key":{"name":"start_loop.cmd","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		AnnotationCmd:105 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.LoopSnippet.StartIter","iteration":1}}
		AssignExpCmd:125 R429:99 Select(tacCalldatabuf!!414@9:121 0x4 )
		AssignExpCmd:126 tacMCANON3!!430:16 Store(tacMCANON3!!18:16 0x80 R429:99 )
		AnnotationCmd:105 JSON{"key":{"name":"dsa.assign.start","type":"java.lang.String","erasureStrategy":"Erased"},"value":"4301_1002_0_0_0_0 -> 4282_1004_0_0_0_0"}
		LabelCmd:105 "Parallel assignment for R3573:bv256, R3574:bv256 := R3566:bv256, R3570:bv256"
		AnnotationCmd:105 JSON{"key":{"name":"dsa.assign.end","type":"java.lang.String","erasureStrategy":"Erased"},"value":"4301_1002_0_0_0_0 -> 4282_1004_0_0_0_0"}
		AnnotationCmd:105 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.LoopSnippet.EndIter","iteration":1}}
		AnnotationCmd:105 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.LoopSnippet.StartIter","iteration":2}}
		AssignExpCmd:125 R431:99 Select(tacCalldatabuf!!414@9:121 0x24 )
		AssignExpCmd:126 tacMCANON3!!432:16 Store(tacMCANON3!!430:16 0xa0 R431:99 )
		AnnotationCmd:105 JSON{"key":{"name":"dsa.assign.start","type":"java.lang.String","erasureStrategy":"Erased"},"value":"4301_1002_0_0_0_0 -> 4282_1004_0_0_0_0"}
		LabelCmd:105 "Parallel assignment for R3573:bv256, R3574:bv256 := R3566:bv256, R3570:bv256"
		AnnotationCmd:105 JSON{"key":{"name":"dsa.assign.end","type":"java.lang.String","erasureStrategy":"Erased"},"value":"4301_1002_0_0_0_0 -> 4282_1004_0_0_0_0"}
		AnnotationCmd:105 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.LoopSnippet.EndIter","iteration":2}}
		AnnotationCmd:105 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.LoopSnippet.EndLoopSnippet","loopId":4}}
		AnnotationCmd:105 JSON{"key":{"name":"end_loop.cmd","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		AnnotationCmd:105 JSON{"key":{"name":"pta.end-allocation","type":"analysis.alloc.AllocationAnalysis$AbstractLocation","erasureStrategy":"Erased"},"value":{"prevFPWriteIdx":0,"nextFPWriteCmd":{"block":{"#class":"tac.BlockIdentifier","origStartPc":4102,"stkTop":1000,"decompCopy":0,"calleeIdx":0,"topOfStackValue":0,"freshCopy":0},"pos":1},"sort":{"#class":"analysis.alloc.AllocationAnalysis.Alloc.ConstBlock","sz":"40"}}}
		AssignExpCmd:125 R433:65 Select(tacCalldatabuf!!414@9:121 0x44 )
		AnnotationCmd:105 JSON{"key":{"name":"internal.func.start","type":"analysis.ip.InternalFuncStartAnnotation","erasureStrategy":"CallTrace"},"value":{"id":9,"startPc":558,"args":[{"s":{"namePrefix":"R426","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1001}]},"offset":1,"sort":"SCALAR"},{"s":{"namePrefix":"R433","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1012}]},"offset":2,"sort":"SCALAR"}],"methodSignature":{"#class":"spec.cvlast.QualifiedMethodSignature.QualifiedMethodSig","qualifiedMethodName":{"#class":"spec.cvlast.QualifiedFunction","host":{"name":"curve"},"methodId":"get_D"},"params":[{"#class":"spec.cvlast.VMParam.Named","name":"xp","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$StaticArrayDescriptor","location":"memory","elementType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256},"numElements":"2"}},{"#class":"spec.cvlast.VMParam.Named","name":"amp","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256}}],"res":[{"#class":"spec.cvlast.VMParam.Unnamed","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256}}]},"stackOffsetToArgPos":{"1":0,"2":1},"callSiteSrc":{"source":0,"begin":3416,"len":1542,"jumpType":"ENTER","address":"ce4604a0000000000000000000000017","sourceContext":{"indexToFilepath":{"0":"contracts/curve.sol","1":"Context.sol","2":"ERC20.sol","3":"IERC20.sol","4":"IERC20Metadata.sol","5":"ReentrancyGuard.sol"},"sourceDir":".post_autofinders.1"}}}}
		AssignExpCmd:127 R434:83 Select(tacMCANON3!!432:16 0xa0 )
		AssignExpCmd:128 R435:93 Select(tacMCANON3!!432:16 0x80 )
		NopCmd
		AssumeExpCmd Apply(add_noofl:bif R435:93 R434:83)
		AssignExpCmd I438:54 Apply(safe_math_promotion:bif R435:93)
		AssignExpCmd I439:54 Apply(safe_math_promotion:bif R434:83)
		NopCmd
		AssignExpCmd R441:72 Apply(safe_math_narrow:bif IntAdd(I438:54 I439:54))
		AnnotationCmd:105 JSON{"key":{"name":"internal.func.end","type":"analysis.ip.InternalFuncExitAnnotation","erasureStrategy":"Canonical"},"value":{"id":9,"rets":[{"s":{"namePrefix":"R441","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1023}]},"offset":0}],"functionLayout":{"0":{"#class":"analysis.ip.InternalFuncValueLocation.Scalar"}}}}
		AnnotationCmd:105 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.EVMFunctionReturnWrite","returnbufOffset":"0","returnValueSym":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R441","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1023}]},"callIndex":9}}
		AnnotationCmd:105 JSON{"key":{"name":"tac.return.path","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		LabelCmd:105 "End procedure curve-get_D(uint256[2],uint256)"
		AssignExpCmd:105 tacReturndata!!443:78 Store(tacReturndata!!492:78 0x0 R441:72 )
		AssignExpCmd:105 tacMCANON2!!444:14 Store(tacMCANON2!!488:14 0x120 R441:72 )
		AnnotationCmd:105 JSON{"key":{"name":"call.trace.pop","type":"analysis.icfg.Inliner$CallStack$PopRecord","erasureStrategy":"Canonical"},"value":"rO0ABXNyAClhbmFseXNpcy5pY2ZnLklubGluZXIkQ2FsbFN0YWNrJFBvcFJlY29yZPAPfwSLdCWJAgABSQAIY2FsbGVlSWR4cAAAAAk="}
		JumpCmd:105 2_0_0_7_0_0
	}
	Block 0_0_0_10_0_0 Succ [3_0_0_7_0_0] {
		AnnotationCmd:105 JSON{"key":{"name":"call.trace.push","type":"analysis.icfg.Inliner$CallStack$PushRecord","erasureStrategy":"Canonical"},"value":"rO0ABXNyACphbmFseXNpcy5pY2ZnLklubGluZXIkQ2FsbFN0YWNrJFB1c2hSZWNvcmSX8+DCTLCH+AIAA0kACGNhbGxlZUlkTAAGY2FsbGVldAATTHZjL2RhdGEvTWV0aG9kUmVmO0wAB3N1bW1hcnl0ABVMdmMvZGF0YS9DYWxsU3VtbWFyeTt4cAAAAApzcgARdmMuZGF0YS5NZXRob2RSZWbJlJTzzU9pGAIAA0wABGF0dHJ0ABdMc2NlbmUvTWV0aG9kQXR0cmlidXRlO0wACmNvbnRyYWN0SWR0ABZMamF2YS9tYXRoL0JpZ0ludGVnZXI7TAAHc2lnSGFzaHQAEExldm0vU2lnaGFzaEludDt4cHNyABxzY2VuZS5NZXRob2RBdHRyaWJ1dGUkQ29tbW9uNHjdebdr9XMCAAB4cgAVc2NlbmUuTWV0aG9kQXR0cmlidXRlcYg2pYWutuUCAAB4cHNyABRqYXZhLm1hdGguQmlnSW50ZWdlcoz8nx+pO/sdAwAGSQAIYml0Q291bnRJAAliaXRMZW5ndGhJABNmaXJzdE5vbnplcm9CeXRlTnVtSQAMbG93ZXN0U2V0Qml0SQAGc2lnbnVtWwAJbWFnbml0dWRldAACW0J4cgAQamF2YS5sYW5nLk51bWJlcoaslR0LlOCLAgAAeHD///////////////7////+AAAAAXVyAAJbQqzzF/gGCFTgAgAAeHAAAAAQzkYEoAAAAAAAAAAAAAAAFHhzcgAOZXZtLlNpZ2hhc2hJbnRUdcqNMXEgeAIAAUwAAW5xAH4ABnhwc3EAfgAM///////////////+/////gAAAAF1cQB+ABAAAAAEGBYN3XhzcgATdmMuZGF0YS5DYWxsU3VtbWFyeZQcmw5vl+FdAgAQSQAJc3VtbWFyeUlkTAAOY2FsbENvbnZlbnRpb250ACZMaW5zdHJ1bWVudGF0aW9uL2NhbGxzL0NhbGxDb252ZW50aW9uO0wACmNhbGxUYXJnZXR0ABpMYW5hbHlzaXMvaWNmZy9DYWxsVGFyZ2V0O0wACGNhbGxUeXBldAAVTHZjL2RhdGEvVEFDQ2FsbFR5cGU7TAAPY2Fubm90QmVJbmxpbmVkdAAtTGFuYWx5c2lzL2ljZmcvSW5saW5lciRJbGxlZ2FsSW5saW5pbmdSZWFzb247TAAGZ2FzVmFydAATTHZjL2RhdGEvVEFDU3ltYm9sO0wABmluQmFzZXEAfgAbTAAIaW5PZmZzZXRxAH4AG0wABmluU2l6ZXEAfgAbTAAMb3JpZ0NhbGxjb3JldAAgTHZjL2RhdGEvVEFDQ21kJFNpbXBsZSRDYWxsQ29yZTtMAAdvdXRCYXNlcQB+ABtMAAlvdXRPZmZzZXRxAH4AG0wAB291dFNpemVxAH4AG0wADXNpZ1Jlc29sdXRpb250AA9MamF2YS91dGlsL1NldDtMAAV0b1ZhcnEAfgAbTAAIdmFsdWVWYXJxAH4AG3hwAAAABnNyACRpbnN0cnVtZW50YXRpb24uY2FsbHMuQ2FsbENvbnZlbnRpb25HtO1ulL788QIAA0kACGNhbGxlcklkTAAFaW5wdXR0ABlMYW5hbHlzaXMvaWNmZy9DYWxsSW5wdXQ7TAAGcmF3T3V0dAAiTGluc3RydW1lbnRhdGlvbi9jYWxscy9DYWxsT3V0cHV0O3hwAAAAAHNyABdhbmFseXNpcy5pY2ZnLkNhbGxJbnB1dJjJD1MhNUxQAgAHTAAHYmFzZVZhcnQAGUx2Yy9kYXRhL1RBQ0V4cHIkU3ltJFZhcjtMABBlbmNvZGVkQXJndW1lbnRzdAAjTGFuYWx5c2lzL2ljZmcvQUJJQXJndW1lbnRFbmNvZGluZztMABNpbnB1dFNpemVMb3dlckJvdW5kcQB+AAZMAAZvZmZzZXR0ABVMdmMvZGF0YS9UQUNFeHByJFN5bTtMABRyYW5nZVRvRGVjb21wb3NlZEFyZ3QAD0xqYXZhL3V0aWwvTWFwO0wAEHNpbXBsaWZpZWRPZmZzZXR0ABtMdmMvZGF0YS9UQUNFeHByJFN5bSRDb25zdDtMAARzaXplcQB+ACZ4cHNyABd2Yy5kYXRhLlRBQ0V4cHIkU3ltJFZhcskrg43eGgPnAgACTAABc3QAF0x2Yy9kYXRhL1RBQ1N5bWJvbCRWYXI7TAADdGFndAAJTHRhYy9UYWc7eHIAE3ZjLmRhdGEuVEFDRXhwciRTeW2iVj0S4YSNUAIAAHhyAA92Yy5kYXRhLlRBQ0V4cHJYhGlUu/v+yAIAAHhwc3IANnZjLmRhdGEuVEFDU3ltYm9sJFZhciRXaXRoRGVmYXVsdENhbGxJbmRleCRXaXRoQnl0ZU1hcJ7+oHF4CHAAAgACTAAEbWV0YXQALUxrb3RsaW54L2NvbGxlY3Rpb25zL2ltbXV0YWJsZS9QZXJzaXN0ZW50TWFwO0wACm5hbWVQcmVmaXh0ABJMamF2YS9sYW5nL1N0cmluZzt4cgAVdmMuZGF0YS5UQUNTeW1ib2wkVmFyCYrCGVl9SXYCAAB4cgARdmMuZGF0YS5UQUNTeW1ib2zd3Run/CoWswIAAHhwc3IAJmRhdGFzdHJ1Y3R1cmVzLnRyZWFwLkhhc2hUcmVhcE1hcCROb2Rlf2t9acJIPnQCAANMAANrZXl0ABJMamF2YS9sYW5nL09iamVjdDtMAARuZXh0dAA1TGRhdGFzdHJ1Y3R1cmVzL3RyZWFwL0hhc2hUcmVhcE1hcCRNb3JlS2V5VmFsdWVQYWlycztMAAV2YWx1ZXEAfgA3eHIAIWRhdGFzdHJ1Y3R1cmVzLnRyZWFwLkhhc2hUcmVhcE1hcPMJ/2vt3boKAgAAeHIAHWRhdGFzdHJ1Y3R1cmVzLnRyZWFwLlRyZWFwTWFw46LAyn3v5moCAAB4cgAaZGF0YXN0cnVjdHVyZXMudHJlYXAuVHJlYXA88f21zZwbdQIAAkwABGxlZnR0ABxMZGF0YXN0cnVjdHVyZXMvdHJlYXAvVHJlYXA7TAAFcmlnaHRxAH4APHhwcHNxAH4ANnBzcQB+ADZwcHNyAAt0YWMuTWV0YUtleVF/W3MiCfIZAgADTAAPZXJhc3VyZVN0cmF0ZWd5dAAdTHRhYy9NZXRhS2V5JEVyYXN1cmVTdHJhdGVneTtMAARuYW1lcQB+ADJMAAN0eXB0ABFMamF2YS9sYW5nL0NsYXNzO3hwfnIAG3RhYy5NZXRhS2V5JEVyYXN1cmVTdHJhdGVneQAAAAAAAAAAEgAAeHIADmphdmEubGFuZy5FbnVtAAAAAAAAAAASAAB4cHQACUNhbm9uaWNhbHQAF3RhYy5tZW1vcnkucGFydGl0aW9uLWlkdnIAEWphdmEubGFuZy5JbnRlZ2VyEuKgpPeBhzgCAAFJAAV2YWx1ZXhxAH4ADnBzcQB+AEkAAAAJc3EAfgBAcQB+AEZ0ABJUYWMuc3ltYm9sLmtleXdvcmR2cgAQamF2YS5sYW5nLlN0cmluZ6DwpDh6O7NCAgAAeHBwdAAEdGFjTXNxAH4AQHEAfgBGdAANdGFjLmlzLm1lbW9yeXZyACJ0YWMuTWV0YU1hcCRDb21wYW5pb24kTm90aGluZ1ZhbHVl8nsHH85ykpUCAAB4cHBzcQB+AFN0AA90YWNNQ0FOT04yISE1MzlzcgAPdGFjLlRhZyRCeXRlTWFwNb/Ry6GDRgkCAAB4cgALdGFjLlRhZyRNYXABJytzDV3P/QIAAHhyAAd0YWMuVGFnLk9V3gn2xngCAAB4cHBzcQB+AAz///////////////7////+AAAAAXVxAH4AEAAAAAEEeHNxAH4AKnNyADV2Yy5kYXRhLlRBQ1N5bWJvbCRWYXIkV2l0aERlZmF1bHRDYWxsSW5kZXgkV2l0aEJpdDI1NnqsyEgq0drPAgACTAAEbWV0YXEAfgAxTAAKbmFtZVByZWZpeHEAfgAyeHEAfgAzc3EAfgA2c3EAfgA2cHBxAH4ATHB0AAFMcHNxAH4AQHEAfgBGdAAQdGFjLnN0YWNrLmhlaWdodHEAfgBKcHNxAH4ASQAAA/d0AARSNTQwc3IADnRhYy5UYWckQml0MjU2IyLQT+LlKkgCAAB4cQB+AFlzcgARamF2YS51dGlsLkhhc2hNYXAFB9rBwxZg0QMAAkYACmxvYWRGYWN0b3JJAAl0aHJlc2hvbGR4cD9AAAAAAAABdwgAAAACAAAAAXNyAB5hbmFseXNpcy5pY2ZnLlNjcmF0Y2hCeXRlUmFuZ2XBTLaPpUzj2gIAAkwABGZyb21xAH4ABkwAAnRvcQB+AAZ4cHNxAH4ADP///////////////v////4AAAAAdXEAfgAQAAAAAHhzcQB+AAz///////////////7////+AAAAAXVxAH4AEAAAAAEDeHNyAC1hbmFseXNpcy5pY2ZnLkRlY29tcG9zZWRDYWxsSW5wdXRBcmckQ29uc3RhbnSFavLdQafqPQIAA0wAAWN0ABlMdmMvZGF0YS9UQUNTeW1ib2wkQ29uc3Q7TAARY29udHJhY3RSZWZlcmVuY2V0AC9MYW5hbHlzaXMvaWNmZy9DYWxsR3JhcGhCdWlsZGVyJENhbGxlZENvbnRyYWN0O0wADHNjcmF0Y2hSYW5nZXQAIExhbmFseXNpcy9pY2ZnL1NjcmF0Y2hCeXRlUmFuZ2U7eHIAJGFuYWx5c2lzLmljZmcuRGVjb21wb3NlZENhbGxJbnB1dEFy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Ra0Sk4jk9wIAAkkABXN0YXJ0TAALcGFja2VkU3RhcnR0ABtMdmMvZGF0YS9TY2FsYXJpemF0aW9uU29ydDt4cQB+AOoAAAAAc3IAH3ZjLmRhdGEuU2NhbGFyaXphdGlvblNvcnQkU3BsaXRU/1mn8ceyBQIAAUwAA2lkeHEAfgAGeHEAfgDqc3EAfgAM///////////////+/////gAAAAF1cQB+ABAAAAABDHhzcQB+ADZwc3EAfgA2cHNxAH4ANnBwc3EAfgBAcQB+AEZ0ABx0YWMuc3RvcmFnZS5ub24taW5kZXhlZC1wYXRodnIANWFuYWx5c2lzLnN0b3JhZ2UuU3RvcmFnZUFuYWx5c2lzUmVzdWx0JE5vbkluZGV4ZWRQYXRoCMGgS6H6P0UCAAB4cHBzcgA6YW5hbHlzaXMuc3RvcmFnZS5TdG9yYWdlQW5hbHlzaXNSZXN1bHQkTm9uSW5kZXhlZFBhdGgkUm9vdL839dil6gr/AgABTAAEc2xvdHEAfgAGeHEAfgD4cQB+APFzcQB+AEBxAH4ARnQADXRhYy5zbG90LnR5cGV2cgA6c3BlYy5jdmxhc3QudHlwZWRlc2NyaXB0b3JzLkVWTVR5cGVEZXNjcmlwdG9yJEVWTVZhbHVlVHlwZcaJrwK66rglAgAAeHIALXNwZWMuY3ZsYXN0LnR5cGVkZXNjcmlwdG9ycy5FVk1UeXBlRGVzY3JpcHRvcshRqfE8wmodAgAAeHBwc3IANXNwZWMuY3ZsYXN0LnR5cGVkZXNjcmlwdG9ycy5FVk1UeXBlRGVzY3JpcHRvciRhZGRyZXNzevhl9G+XoCkCAAB4cgBEc3BlYy5jdmxhc3QudHlwZWRlc2NyaXB0b3JzLkVWTVR5cGVEZXNjcmlwdG9yJEVWTUlzb21vcnBoaWNWYWx1ZVR5cGX3dZiRbhChDwIAAHhxAH4A/nNxAH4AQH5xAH4ARHQABkVyYXNlZHQAGHRhYy5zdG9yYWdlLnByZXR0eS5wYXRoc3ZyAB1hbmFseXNpcy5zdG9yYWdlLkRpc3BsYXlQYXRoc/dES7fD9VEWAgABTAAFcGF0aHNxAH4AHXhwcHNxAH4BCHNyABdqYXZhLnV0aWwuTGlua2VkSGFzaFNldNhs11qV3SoeAgAAeHIAEWphdmEudXRpbC5IYXNoU2V0ukSFlZa4tzQDAAB4cHcMAAAAED9AAAAAAAABc3IAIWFuYWx5c2lzLnN0b3JhZ2UuRGlzcGxheVBhdGgkUm9vdNNzoL2Z0DxyAgACTAAEYmFzZXQAHkxhbmFseXNpcy9zdG9yYWdlL0Rpc3BsYXlQYXRoO0wABG5hbWVxAH4AMnhyABxhbmFseXNpcy5zdG9yYWdlLkRpc3BsYXlQYXRoT0Bj6lbSIAUCAAB4cHB0AAhscF90b2tlbnhzcQB+AEBxAH4ARnQAFXRhYy5zdG9yYWdlLmJpdC13aWR0aHEAfgBKcHNxAH4ASQAAAKBwc3EAfgBAcQB+AEZ0AAt0YWMuc3RvcmFnZXZxAH4ADHBxAH4AxnBxAH4AY3BzcQB+AEkAAAP7dAALQ0FOT041NyEhMjVzcQB+AHdxAH4AaHEAfgBtc3EAfgAwc3EAfgA2cHNxAH4ANnBzcQB+ADZwcHEAfgBDcHEAfgBLcQB+AExwcQB+AFBxAH4AUXBxAH4AVXEAfgBWc3EAfgBec3EAfgA2c3EAfgA2cHBxAH4ATHBxAH4AYnBxAH4AY3BxAH4AjXEAfgBmcQB+AJBzcgAiamF2YS51dGlsLkNvbGxlY3Rpb25zJFNpbmdsZXRvblNldCxSQZgpwLG/AgABTAAHZWxlbWVudHEAfgA3eHBxAH4AFHNxAH4AXnNxAH4ANnNxAH4ANnNxAH4ANnNxAH4ANnBzcQB+ADZwcHEAfgBMcHEAfgBicQB+AOhwcQB+AO5zcQB+ADZwc3EAfgA2cHNxAH4ANnBwcQB+APZwcQB+APtxAH4A/HBxAH4BA3EAfgEEcHNxAH4BCHNxAH4BC3cMAAAAED9AAAAAAAABcQB+ARF4cQB+ARNwcQB+ARVwcQB+ARZwcQB+AMZwcQB+AGNwcQB+ARlxAH4BGnNxAH4Ad3EAfgBocQB+AG0="}
		AnnotationCmd:105 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageGlobalChangeSnippet.StorageBackupPoint","calleeTxId":10}}
		NopCmd
		AssumeExpCmd LAnd(Eq(tacCalldatasize!!6:3 0x4 ) Eq(tacCalldatasize!!6:3 0x4 ) )
		NopCmd
		AssumeExpCmd Eq(tacCalldatabufCANON0@10:2 0x18160ddd00000000000000000000000000000000000000000000000000000000 )
		LabelCmd:105 "Start procedure CurveTokenExample-totalSupply()"
		AnnotationCmd:105 JSON{"key":{"name":"fps.free-pointer-is-scalarized","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true}
		AssignExpCmd:105 R448:54 Select(tacExtcodesize!!7:4 Apply(to_skey:bif R28:103) )
		NopCmd
		AssumeExpCmd Gt(R448:54 0x0 )
		AnnotationCmd:105 JSON{"key":{"name":"internal.func.finder.info","type":"analysis.ip.InternalFunctionFinderReport","erasureStrategy":"Erased"},"value":"rO0ABXNyAChhbmFseXNpcy5pcC5JbnRlcm5hbEZ1bmN0aW9uRmluZGVyUmVwb3J0ian+bYn1VdACAAFMABN1bnJlc29sdmVkRnVuY3Rpb25zdAAPTGphdmEvdXRpbC9TZXQ7eHBzcgAhZGF0YXN0cnVjdHVyZXMuTGlua2VkQXJyYXlIYXNoU2V0AAAAAAAAAAEDAAJGAApsb2FkRmFjdG9yTAAJaGFzaFRhYmxldAAuTGRhdGFzdHJ1Y3R1cmVzL2FycmF5aGFzaHRhYmxlL0FycmF5SGFzaFRhYmxlO3hwdwgAAAAAQAAAAHg="}
		AnnotationCmd:105 JSON{"key":{"name":"fps.free-pointer-is-scalarized","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true}
		NopCmd
		AssumeExpCmd LNot(Lt(tacCalldatasize!!6:3 0x4 ) )
		NopCmd
		AssumeExpCmd Gt(0x40c10f19 tacSighash!!43:47 )
		NopCmd
		AssumeExpCmd LNot(Eq(0x6fdde03 tacSighash!!43:47 ) )
		NopCmd
		AssumeExpCmd LNot(Eq(0x95ea7b3 tacSighash!!43:47 ) )
		NopCmd
		AssumeExpCmd Eq(0x18160ddd tacSighash!!43:47 )
		AnnotationCmd:105 JSON{"key":{"name":"internal.func.start","type":"analysis.ip.InternalFuncStartAnnotation","erasureStrategy":"CallTrace"},"value":{"id":10,"startPc":1205,"args":[],"methodSignature":{"#class":"spec.cvlast.QualifiedMethodSignature.QualifiedMethodSig","qualifiedMethodName":{"#class":"spec.cvlast.QualifiedFunction","host":{"name":"CurveTokenExample"},"methodId":"totalSupply"},"params":[],"res":[{"#class":"spec.cvlast.VMParam.Unnamed","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256}}]},"stackOffsetToArgPos":{},"callSiteSrc":{"source":2,"begin":3952,"len":364,"jumpType":"ENTER","address":"ce4604a0000000000000000000000014","sourceContext":{"indexToFilepath":{"0":"contracts/curve.sol","1":"Context.sol","2":"ERC20.sol","3":"IERC20.sol","4":"IERC20Metadata.sol","5":"ReentrancyGuard.sol"},"sourceDir":".post_autofinders.1"}}}}
		AnnotationCmd:105 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet","value":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"CANON124!!9","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.scalarization.sort","type":"vc.data.ScalarizationSort","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.ScalarizationSort.Split","idx":"2"}},{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.storage.bit-width","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":256},{"key":{"name":"tac.storage.pretty.paths","type":"analysis.storage.DisplayPaths","erasureStrategy":"Erased"},"value":{"paths":[{"#class":"analysis.storage.DisplayPath.Root","name":"_totalSupply"}]}},{"key":{"name":"tac.slot.type","type":"spec.cvlast.typedescriptors.EVMTypeDescriptor$EVMValueType","erasureStrategy":"Canonical"},"value":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256}},{"key":{"name":"tac.storage.non-indexed-path","type":"analysis.storage.StorageAnalysisResult$NonIndexedPath","erasureStrategy":"Canonical"},"value":{"#class":"analysis.storage.StorageAnalysisResult.NonIndexedPath.Root","slot":"2"}},{"key":{"name":"tac.storage","type":"java.math.BigInteger","erasureStrategy":"Canonical"},"value":"ce4604a0000000000000000000000014"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1021}]},"displayPath":{"#class":"analysis.storage.DisplayPath.Root","name":"_totalSupply"},"storageType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256},"contractInstance":"ce4604a0000000000000000000000014","linkableStorageReadId":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet.Id","id":11}}}
		AnnotationCmd:105 JSON{"key":{"name":"internal.func.end","type":"analysis.ip.InternalFuncExitAnnotation","erasureStrategy":"Canonical"},"value":{"id":10,"rets":[{"s":{"namePrefix":"CANON124!!9","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.scalarization.sort","type":"vc.data.ScalarizationSort","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.ScalarizationSort.Split","idx":"2"}},{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.storage.bit-width","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":256},{"key":{"name":"tac.storage.pretty.paths","type":"analysis.storage.DisplayPaths","erasureStrategy":"Erased"},"value":{"paths":[{"#class":"analysis.storage.DisplayPath.Root","name":"_totalSupply"}]}},{"key":{"name":"tac.slot.type","type":"spec.cvlast.typedescriptors.EVMTypeDescriptor$EVMValueType","erasureStrategy":"Canonical"},"value":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256}},{"key":{"name":"tac.storage.non-indexed-path","type":"analysis.storage.StorageAnalysisResult$NonIndexedPath","erasureStrategy":"Canonical"},"value":{"#class":"analysis.storage.StorageAnalysisResult.NonIndexedPath.Root","slot":"2"}},{"key":{"name":"tac.storage","type":"java.math.BigInteger","erasureStrategy":"Canonical"},"value":"ce4604a0000000000000000000000014"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1023}]},"offset":0}],"functionLayout":{"0":{"#class":"analysis.ip.InternalFuncValueLocation.Scalar"}}}}
		AnnotationCmd:105 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.EVMFunctionReturnWrite","returnbufOffset":"0","returnValueSym":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"CANON124!!9","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.scalarization.sort","type":"vc.data.ScalarizationSort","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.ScalarizationSort.Split","idx":"2"}},{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.storage.bit-width","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":256},{"key":{"name":"tac.storage.pretty.paths","type":"analysis.storage.DisplayPaths","erasureStrategy":"Erased"},"value":{"paths":[{"#class":"analysis.storage.DisplayPath.Root","name":"_totalSupply"}]}},{"key":{"name":"tac.slot.type","type":"spec.cvlast.typedescriptors.EVMTypeDescriptor$EVMValueType","erasureStrategy":"Canonical"},"value":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256}},{"key":{"name":"tac.storage.non-indexed-path","type":"analysis.storage.StorageAnalysisResult$NonIndexedPath","erasureStrategy":"Canonical"},"value":{"#class":"analysis.storage.StorageAnalysisResult.NonIndexedPath.Root","slot":"2"}},{"key":{"name":"tac.storage","type":"java.math.BigInteger","erasureStrategy":"Canonical"},"value":"ce4604a0000000000000000000000014"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1023}]},"callIndex":10}}
		AnnotationCmd:105 JSON{"key":{"name":"tac.return.path","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		LabelCmd:105 "End procedure CurveTokenExample-totalSupply()"
		AssignExpCmd:105 tacReturndata!!457:78 Store(tacReturndata!!542:78 0x0 CANON124!!9:104 )
		AssignExpCmd:105 tacMCANON2!!458:14 Store(tacMCANON2!!539:14 0x140 CANON124!!9:104 )
		AnnotationCmd:105 JSON{"key":{"name":"call.trace.pop","type":"analysis.icfg.Inliner$CallStack$PopRecord","erasureStrategy":"Canonical"},"value":"rO0ABXNyAClhbmFseXNpcy5pY2ZnLklubGluZXIkQ2FsbFN0YWNrJFBvcFJlY29yZPAPfwSLdCWJAgABSQAIY2FsbGVlSWR4cAAAAAo="}
		JumpCmd:105 3_0_0_7_0_0
	}
	Block 1_0_0_1_0_0 Succ [0_0_0_3_0_0] {
		AssumeNotCmd:74 false
		AnnotationCmd:56 JSON{"key":{"name":"pta.fake-return.start","type":"analysis.CmdPointer","erasureStrategy":"Erased"},"value":{"block":{"#class":"tac.BlockIdentifier","origStartPc":1608,"stkTop":1009,"decompCopy":0,"calleeIdx":0,"topOfStackValue":2,"freshCopy":0},"pos":1}}
		AnnotationCmd:56 JSON{"key":{"name":"pta.fake-return.end","type":"analysis.CmdPointer","erasureStrategy":"Erased"},"value":{"block":{"#class":"tac.BlockIdentifier","origStartPc":1608,"stkTop":1009,"decompCopy":0,"calleeIdx":0,"topOfStackValue":2,"freshCopy":0},"pos":6}}
		AssumeNotCmd:129 false
		AssignExpCmd:130 R459:131 Select(tacMCANON2!!267:13 0x100 )
		NopCmd
		AssumeExpCmd LNot(Lt(R459:131 R234:72 ) )
		AssignExpCmd:132 R461:69 Sub(R459:131 R234:72 )
		AssignExpCmd:70 tacMCANON1!!462:11 Store(tacMCANON1!!233:11 0xe0 R461:69 )
		AnnotationCmd:56 JSON{"key":{"name":"pta.end-allocation","type":"analysis.alloc.AllocationAnalysis$AbstractLocation","erasureStrategy":"Erased"},"value":{"prevFPWriteIdx":1,"nextFPWriteCmd":{"block":{"#class":"tac.BlockIdentifier","origStartPc":16,"stkTop":1024,"decompCopy":0,"calleeIdx":0,"topOfStackValue":2,"freshCopy":0},"pos":44},"sort":{"#class":"analysis.alloc.AllocationAnalysis.Alloc.ConstBlock","sz":"40"}}}
		AnnotationCmd:56 JSON{"key":{"name":"internal.func.start","type":"analysis.ip.InternalFuncStartAnnotation","erasureStrategy":"CallTrace"},"value":{"id":2,"startPc":3822,"args":[],"methodSignature":{"#class":"spec.cvlast.QualifiedMethodSignature.QualifiedMethodSig","qualifiedMethodName":{"#class":"spec.cvlast.QualifiedFunction","host":{"name":"curve"},"methodId":"_A"},"params":[],"res":[{"#class":"spec.cvlast.VMParam.Unnamed","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256}}]},"stackOffsetToArgPos":{},"callSiteSrc":{"source":0,"begin":6811,"len":4,"jumpType":"ENTER","address":"ce4604a0000000000000000000000017","sourceContext":{"indexToFilepath":{"0":"contracts/curve.sol","1":"Context.sol","2":"ERC20.sol","3":"IERC20.sol","4":"IERC20Metadata.sol","5":"ReentrancyGuard.sol"},"sourceDir":".post_autofinders.1"}}}}
		AnnotationCmd:56 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet","value":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"CANON139!!11","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.scalarization.sort","type":"vc.data.ScalarizationSort","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.ScalarizationSort.Split","idx":"5"}},{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.storage.bit-width","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":256},{"key":{"name":"tac.storage.pretty.paths","type":"analysis.storage.DisplayPaths","erasureStrategy":"Erased"},"value":{"paths":[{"#class":"analysis.storage.DisplayPath.Root","name":"future_A"}]}},{"key":{"name":"tac.slot.type","type":"spec.cvlast.typedescriptors.EVMTypeDescriptor$EVMValueType","erasureStrategy":"Canonical"},"value":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256}},{"key":{"name":"tac.storage.non-indexed-path","type":"analysis.storage.StorageAnalysisResult$NonIndexedPath","erasureStrategy":"Canonical"},"value":{"#class":"analysis.storage.StorageAnalysisResult.NonIndexedPath.Root","slot":"5"}},{"key":{"name":"tac.storage","type":"java.math.BigInteger","erasureStrategy":"Canonical"},"value":"ce4604a0000000000000000000000017"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1015}]},"displayPath":{"#class":"analysis.storage.DisplayPath.Root","name":"future_A"},"storageType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256},"contractInstance":"ce4604a0000000000000000000000017","linkableStorageReadId":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet.Id","id":2}}}
		AnnotationCmd:56 JSON{"key":{"name":"internal.func.end","type":"analysis.ip.InternalFuncExitAnnotation","erasureStrategy":"Canonical"},"value":{"id":2,"rets":[{"s":{"namePrefix":"CANON139!!11","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.scalarization.sort","type":"vc.data.ScalarizationSort","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.ScalarizationSort.Split","idx":"5"}},{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.storage.bit-width","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":256},{"key":{"name":"tac.storage.pretty.paths","type":"analysis.storage.DisplayPaths","erasureStrategy":"Erased"},"value":{"paths":[{"#class":"analysis.storage.DisplayPath.Root","name":"future_A"}]}},{"key":{"name":"tac.slot.type","type":"spec.cvlast.typedescriptors.EVMTypeDescriptor$EVMValueType","erasureStrategy":"Canonical"},"value":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256}},{"key":{"name":"tac.storage.non-indexed-path","type":"analysis.storage.StorageAnalysisResult$NonIndexedPath","erasureStrategy":"Canonical"},"value":{"#class":"analysis.storage.StorageAnalysisResult.NonIndexedPath.Root","slot":"5"}},{"key":{"name":"tac.storage","type":"java.math.BigInteger","erasureStrategy":"Canonical"},"value":"ce4604a0000000000000000000000017"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1017}]},"offset":0}],"functionLayout":{"0":{"#class":"analysis.ip.InternalFuncValueLocation.Scalar"}}}}
		AssignExpCmd:133 tacMCANON2!!465:13 Store(tacMCANON2!!267:13 0x120 0x3842f77600000000000000000000000000000000000000000000000000000000 )
		AnnotationCmd:56 JSON{"key":{"name":"dsa.assign.start","type":"java.lang.String","erasureStrategy":"Erased"},"value":"4639_1009_0_0_0_0 -> 4643_1007_0_0_0_0"}
		LabelCmd:56 "Parallel assignment for R4175:bv256, R4219:bv256, B4220:bool, R4221:bv256 := R6292:bv256, R397:bv256, B4076:bool, R4077:bv256"
		AnnotationCmd:56 JSON{"key":{"name":"dsa.assign.end","type":"java.lang.String","erasureStrategy":"Erased"},"value":"4639_1009_0_0_0_0 -> 4643_1007_0_0_0_0"}
		AnnotationCmd:56 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.LoopSnippet.StartLoopSnippet","loopIndex":0,"loopSource":"unknown loop source code"}}
		AnnotationCmd:56 JSON{"key":{"name":"start_loop.cmd","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		AnnotationCmd:56 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.LoopSnippet.StartIter","iteration":1}}
		AssignExpCmd:134 R466:135 Select(tacMCANON1!!462:11 0xc0 )
		AssignExpCmd:136 tacMCANON2!!467:13 Store(tacMCANON2!!465:13 0x124 R466:135 )
		AnnotationCmd:56 JSON{"key":{"name":"dsa.assign.start","type":"java.lang.String","erasureStrategy":"Erased"},"value":"4674_1005_0_0_0_0 -> 4643_1007_0_0_0_0"}
		LabelCmd:56 "Parallel assignment for R4175:bv256, R4219:bv256, B4220:bool, R4221:bv256 := R3948:bv256, R3993:bv256, B4217:bool, R4214:bv256"
		AnnotationCmd:56 JSON{"key":{"name":"dsa.assign.end","type":"java.lang.String","erasureStrategy":"Erased"},"value":"4674_1005_0_0_0_0 -> 4643_1007_0_0_0_0"}
		AnnotationCmd:56 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.LoopSnippet.EndIter","iteration":1}}
		AnnotationCmd:56 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.LoopSnippet.StartIter","iteration":2}}
		AssignExpCmd:134 R468:135 Select(tacMCANON1!!462:11 0xe0 )
		AssignExpCmd:136 tacMCANON2!!469:13 Store(tacMCANON2!!467:13 0x144 R468:135 )
		AnnotationCmd:56 JSON{"key":{"name":"dsa.assign.start","type":"java.lang.String","erasureStrategy":"Erased"},"value":"4674_1005_0_0_0_0 -> 4643_1007_0_0_0_0"}
		LabelCmd:56 "Parallel assignment for R4175:bv256, R4219:bv256, B4220:bool, R4221:bv256 := R3948:bv256, R3993:bv256, B4217:bool, R4214:bv256"
		AnnotationCmd:56 JSON{"key":{"name":"dsa.assign.end","type":"java.lang.String","erasureStrategy":"Erased"},"value":"4674_1005_0_0_0_0 -> 4643_1007_0_0_0_0"}
		AnnotationCmd:56 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.LoopSnippet.EndIter","iteration":2}}
		AnnotationCmd:56 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.LoopSnippet.EndLoopSnippet","loopId":0}}
		AnnotationCmd:56 JSON{"key":{"name":"end_loop.cmd","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		AssignExpCmd:137 tacMCANON2!!471:13 Store(tacMCANON2!!469:13 0x164 CANON139!!11:138 )
		AssignExpCmd:133 R472:93 0x120
		NopCmd
		AssignHavocCmd:133 R474:65
		AssignHavocCmd:56 tacReturndata!!475:78
		JumpCmd:56 0_0_0_3_0_0
	}
	Block 1_0_0_7_0_0 Succ [0_0_0_9_0_0] {
		AssumeNotCmd:112 false
		AnnotationCmd:105 JSON{"key":{"name":"pta.fake-return.start","type":"analysis.CmdPointer","erasureStrategy":"Erased"},"value":{"block":{"#class":"tac.BlockIdentifier","origStartPc":1608,"stkTop":1009,"decompCopy":0,"calleeIdx":0,"topOfStackValue":2,"freshCopy":0},"pos":1}}
		AnnotationCmd:105 JSON{"key":{"name":"pta.fake-return.end","type":"analysis.CmdPointer","erasureStrategy":"Erased"},"value":{"block":{"#class":"tac.BlockIdentifier","origStartPc":1608,"stkTop":1009,"decompCopy":0,"calleeIdx":0,"topOfStackValue":2,"freshCopy":0},"pos":6}}
		AssumeNotCmd:139 false
		AssignExpCmd:140 R476:131 Select(tacMCANON2!!410:14 0x100 )
		NopCmd
		AssumeExpCmd LNot(Lt(R476:131 R377:72 ) )
		AssignExpCmd:141 R478:69 Sub(R476:131 R377:72 )
		AssignExpCmd:110 tacMCANON1!!479:12 Store(tacMCANON1!!376:12 0xe0 R478:69 )
		AnnotationCmd:105 JSON{"key":{"name":"pta.end-allocation","type":"analysis.alloc.AllocationAnalysis$AbstractLocation","erasureStrategy":"Erased"},"value":{"prevFPWriteIdx":1,"nextFPWriteCmd":{"block":{"#class":"tac.BlockIdentifier","origStartPc":16,"stkTop":1024,"decompCopy":0,"calleeIdx":0,"topOfStackValue":2,"freshCopy":0},"pos":44},"sort":{"#class":"analysis.alloc.AllocationAnalysis.Alloc.ConstBlock","sz":"40"}}}
		AnnotationCmd:105 JSON{"key":{"name":"internal.func.start","type":"analysis.ip.InternalFuncStartAnnotation","erasureStrategy":"CallTrace"},"value":{"id":8,"startPc":3822,"args":[],"methodSignature":{"#class":"spec.cvlast.QualifiedMethodSignature.QualifiedMethodSig","qualifiedMethodName":{"#class":"spec.cvlast.QualifiedFunction","host":{"name":"curve"},"methodId":"_A"},"params":[],"res":[{"#class":"spec.cvlast.VMParam.Unnamed","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256}}]},"stackOffsetToArgPos":{},"callSiteSrc":{"source":0,"begin":6811,"len":4,"jumpType":"ENTER","address":"ce4604a0000000000000000000000017","sourceContext":{"indexToFilepath":{"0":"contracts/curve.sol","1":"Context.sol","2":"ERC20.sol","3":"IERC20.sol","4":"IERC20Metadata.sol","5":"ReentrancyGuard.sol"},"sourceDir":".post_autofinders.1"}}}}
		AnnotationCmd:105 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet","value":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"CANON139!!11","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.scalarization.sort","type":"vc.data.ScalarizationSort","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.ScalarizationSort.Split","idx":"5"}},{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.storage.bit-width","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":256},{"key":{"name":"tac.storage.pretty.paths","type":"analysis.storage.DisplayPaths","erasureStrategy":"Erased"},"value":{"paths":[{"#class":"analysis.storage.DisplayPath.Root","name":"future_A"}]}},{"key":{"name":"tac.slot.type","type":"spec.cvlast.typedescriptors.EVMTypeDescriptor$EVMValueType","erasureStrategy":"Canonical"},"value":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256}},{"key":{"name":"tac.storage.non-indexed-path","type":"analysis.storage.StorageAnalysisResult$NonIndexedPath","erasureStrategy":"Canonical"},"value":{"#class":"analysis.storage.StorageAnalysisResult.NonIndexedPath.Root","slot":"5"}},{"key":{"name":"tac.storage","type":"java.math.BigInteger","erasureStrategy":"Canonical"},"value":"ce4604a0000000000000000000000017"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1015}]},"displayPath":{"#class":"analysis.storage.DisplayPath.Root","name":"future_A"},"storageType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256},"contractInstance":"ce4604a0000000000000000000000017","linkableStorageReadId":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet.Id","id":9}}}
		AnnotationCmd:105 JSON{"key":{"name":"internal.func.end","type":"analysis.ip.InternalFuncExitAnnotation","erasureStrategy":"Canonical"},"value":{"id":8,"rets":[{"s":{"namePrefix":"CANON139!!11","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.scalarization.sort","type":"vc.data.ScalarizationSort","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.ScalarizationSort.Split","idx":"5"}},{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.storage.bit-width","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":256},{"key":{"name":"tac.storage.pretty.paths","type":"analysis.storage.DisplayPaths","erasureStrategy":"Erased"},"value":{"paths":[{"#class":"analysis.storage.DisplayPath.Root","name":"future_A"}]}},{"key":{"name":"tac.slot.type","type":"spec.cvlast.typedescriptors.EVMTypeDescriptor$EVMValueType","erasureStrategy":"Canonical"},"value":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256}},{"key":{"name":"tac.storage.non-indexed-path","type":"analysis.storage.StorageAnalysisResult$NonIndexedPath","erasureStrategy":"Canonical"},"value":{"#class":"analysis.storage.StorageAnalysisResult.NonIndexedPath.Root","slot":"5"}},{"key":{"name":"tac.storage","type":"java.math.BigInteger","erasureStrategy":"Canonical"},"value":"ce4604a0000000000000000000000017"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1017}]},"offset":0}],"functionLayout":{"0":{"#class":"analysis.ip.InternalFuncValueLocation.Scalar"}}}}
		AssignExpCmd:142 tacMCANON2!!482:14 Store(tacMCANON2!!410:14 0x120 0x3842f77600000000000000000000000000000000000000000000000000000000 )
		AnnotationCmd:105 JSON{"key":{"name":"dsa.assign.start","type":"java.lang.String","erasureStrategy":"Erased"},"value":"4639_1009_0_0_0_0 -> 4643_1007_0_0_0_0"}
		LabelCmd:105 "Parallel assignment for R4175:bv256, R4219:bv256, B4220:bool, R4221:bv256 := R6292:bv256, R397:bv256, B4076:bool, R4077:bv256"
		AnnotationCmd:105 JSON{"key":{"name":"dsa.assign.end","type":"java.lang.String","erasureStrategy":"Erased"},"value":"4639_1009_0_0_0_0 -> 4643_1007_0_0_0_0"}
		AnnotationCmd:105 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.LoopSnippet.StartLoopSnippet","loopIndex":3,"loopSource":"unknown loop source code"}}
		AnnotationCmd:105 JSON{"key":{"name":"start_loop.cmd","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		AnnotationCmd:105 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.LoopSnippet.StartIter","iteration":1}}
		AssignExpCmd:143 R483:135 Select(tacMCANON1!!479:12 0xc0 )
		AssignExpCmd:144 tacMCANON2!!484:14 Store(tacMCANON2!!482:14 0x124 R483:135 )
		AnnotationCmd:105 JSON{"key":{"name":"dsa.assign.start","type":"java.lang.String","erasureStrategy":"Erased"},"value":"4674_1005_0_0_0_0 -> 4643_1007_0_0_0_0"}
		LabelCmd:105 "Parallel assignment for R4175:bv256, R4219:bv256, B4220:bool, R4221:bv256 := R3948:bv256, R3993:bv256, B4217:bool, R4214:bv256"
		AnnotationCmd:105 JSON{"key":{"name":"dsa.assign.end","type":"java.lang.String","erasureStrategy":"Erased"},"value":"4674_1005_0_0_0_0 -> 4643_1007_0_0_0_0"}
		AnnotationCmd:105 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.LoopSnippet.EndIter","iteration":1}}
		AnnotationCmd:105 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.LoopSnippet.StartIter","iteration":2}}
		AssignExpCmd:143 R485:135 Select(tacMCANON1!!479:12 0xe0 )
		AssignExpCmd:144 tacMCANON2!!486:14 Store(tacMCANON2!!484:14 0x144 R485:135 )
		AnnotationCmd:105 JSON{"key":{"name":"dsa.assign.start","type":"java.lang.String","erasureStrategy":"Erased"},"value":"4674_1005_0_0_0_0 -> 4643_1007_0_0_0_0"}
		LabelCmd:105 "Parallel assignment for R4175:bv256, R4219:bv256, B4220:bool, R4221:bv256 := R3948:bv256, R3993:bv256, B4217:bool, R4214:bv256"
		AnnotationCmd:105 JSON{"key":{"name":"dsa.assign.end","type":"java.lang.String","erasureStrategy":"Erased"},"value":"4674_1005_0_0_0_0 -> 4643_1007_0_0_0_0"}
		AnnotationCmd:105 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.LoopSnippet.EndIter","iteration":2}}
		AnnotationCmd:105 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.LoopSnippet.EndLoopSnippet","loopId":3}}
		AnnotationCmd:105 JSON{"key":{"name":"end_loop.cmd","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		AssignExpCmd:145 tacMCANON2!!488:14 Store(tacMCANON2!!486:14 0x164 CANON139!!11:138 )
		AssignExpCmd:142 R489:93 0x120
		NopCmd
		AssignHavocCmd:142 R491:65
		AssignHavocCmd:105 tacReturndata!!492:78
		JumpCmd:105 0_0_0_9_0_0
	}
	Block 3_0_0_1_0_0 Succ [4_0_0_0_0_0] {
		AssumeNotCmd:146 false
		AnnotationCmd:56 JSON{"key":{"name":"pta.fake-return.start","type":"analysis.CmdPointer","erasureStrategy":"Erased"},"value":{"block":{"#class":"tac.BlockIdentifier","origStartPc":3278,"stkTop":1016,"decompCopy":0,"calleeIdx":0,"topOfStackValue":2,"freshCopy":0},"pos":1}}
		AnnotationCmd:56 JSON{"key":{"name":"pta.fake-return.end","type":"analysis.CmdPointer","erasureStrategy":"Erased"},"value":{"block":{"#class":"tac.BlockIdentifier","origStartPc":3278,"stkTop":1016,"decompCopy":0,"calleeIdx":0,"topOfStackValue":2,"freshCopy":0},"pos":6}}
		AssumeNotCmd:129 false
		AssignExpCmd:130 R493:147 Select(tacMCANON2!!315:13 0x140 )
		NopCmd
		AssumeExpCmd Apply(mul_noofl:bif R523:67 0x8ac7230489e80000)
		NopCmd
		AssignExpCmd:148 I502:54 IntMul(Apply(safe_math_promotion:bif R523:67) 0x8ac7230489e80000)
		NopCmd
		NopCmd
		AssumeExpCmd Gt(R493:147 0x0 )
		AssignExpCmd:149 R505:150 Div(Apply(safe_math_narrow:bif I502:54) R493:147 )
		AnnotationCmd:56 JSON{"key":{"name":"internal.func.end","type":"analysis.ip.InternalFuncExitAnnotation","erasureStrategy":"Canonical"},"value":{"id":0,"rets":[{"s":{"namePrefix":"R505","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1023}]},"offset":0}],"functionLayout":{"0":{"#class":"analysis.ip.InternalFuncValueLocation.Scalar"}}}}
		AnnotationCmd:56 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.EVMFunctionReturnWrite","returnbufOffset":"0","returnValueSym":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R505","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1023}]},"callIndex":1}}
		AnnotationCmd:56 JSON{"key":{"name":"tac.return.path","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		LabelCmd:56 "End procedure curve-getVirtualPrice()"
		NopCmd
		AnnotationCmd:56 JSON{"key":{"name":"call.trace.pop","type":"analysis.icfg.Inliner$CallStack$PopRecord","erasureStrategy":"Canonical"},"value":"rO0ABXNyAClhbmFseXNpcy5pY2ZnLklubGluZXIkQ2FsbFN0YWNrJFBvcFJlY29yZPAPfwSLdCWJAgABSQAIY2FsbGVlSWR4cAAAAAE="}
	}
	Block 3_0_0_7_0_0 Succ [7_0_0_0_0_0] {
		AssumeNotCmd:151 false
		AnnotationCmd:105 JSON{"key":{"name":"pta.fake-return.start","type":"analysis.CmdPointer","erasureStrategy":"Erased"},"value":{"block":{"#class":"tac.BlockIdentifier","origStartPc":3278,"stkTop":1016,"decompCopy":0,"calleeIdx":0,"topOfStackValue":2,"freshCopy":0},"pos":1}}
		AnnotationCmd:105 JSON{"key":{"name":"pta.fake-return.end","type":"analysis.CmdPointer","erasureStrategy":"Erased"},"value":{"block":{"#class":"tac.BlockIdentifier","origStartPc":3278,"stkTop":1016,"decompCopy":0,"calleeIdx":0,"topOfStackValue":2,"freshCopy":0},"pos":6}}
		AssumeNotCmd:139 false
		AssignExpCmd:140 R508:147 Select(tacMCANON2!!458:14 0x140 )
		NopCmd
		AssumeExpCmd Apply(mul_noofl:bif R533:67 0x8ac7230489e80000)
		NopCmd
		AssignExpCmd:152 I517:54 IntMul(Apply(safe_math_promotion:bif R533:67) 0x8ac7230489e80000)
		NopCmd
		NopCmd
		AssumeExpCmd Gt(R508:147 0x0 )
		AssignExpCmd:153 R520:150 Div(Apply(safe_math_narrow:bif I517:54) R508:147 )
		AnnotationCmd:105 JSON{"key":{"name":"internal.func.end","type":"analysis.ip.InternalFuncExitAnnotation","erasureStrategy":"Canonical"},"value":{"id":6,"rets":[{"s":{"namePrefix":"R520","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1023}]},"offset":0}],"functionLayout":{"0":{"#class":"analysis.ip.InternalFuncValueLocation.Scalar"}}}}
		AnnotationCmd:105 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.EVMFunctionReturnWrite","returnbufOffset":"0","returnValueSym":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R520","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1023}]},"callIndex":7}}
		AnnotationCmd:105 JSON{"key":{"name":"tac.return.path","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		LabelCmd:105 "End procedure curve-getVirtualPrice()"
		NopCmd
		AnnotationCmd:105 JSON{"key":{"name":"call.trace.pop","type":"analysis.icfg.Inliner$CallStack$PopRecord","erasureStrategy":"Canonical"},"value":"rO0ABXNyAClhbmFseXNpcy5pY2ZnLklubGluZXIkQ2FsbFN0YWNrJFBvcFJlY29yZPAPfwSLdCWJAgABSQAIY2FsbGVlSWR4cAAAAAc="}
	}
	Block 2_0_0_1_0_0 Succ [0_0_0_4_0_0] {
		AssumeNotCmd:133 false
		AnnotationCmd:56 JSON{"key":{"name":"pta.fake-return.start","type":"analysis.CmdPointer","erasureStrategy":"Erased"},"value":{"block":{"#class":"tac.BlockIdentifier","origStartPc":3129,"stkTop":1017,"decompCopy":0,"calleeIdx":0,"topOfStackValue":2,"freshCopy":0},"pos":1}}
		AnnotationCmd:56 JSON{"key":{"name":"pta.fake-return.end","type":"analysis.CmdPointer","erasureStrategy":"Erased"},"value":{"block":{"#class":"tac.BlockIdentifier","origStartPc":3129,"stkTop":1017,"decompCopy":0,"calleeIdx":0,"topOfStackValue":2,"freshCopy":0},"pos":6}}
		AssumeNotCmd:129 false
		AssignExpCmd:130 R523:67 Select(tacMCANON2!!301:13 0x120 )
		AssignExpCmd:56 B525:54 Le(CANON57!!25:154 0xffffffffffffffffffffffffffffffffffffffff )
		AssignExpCmd:56 B526:54 Ge(CANON57!!25:154 0x0 )
		NopCmd
		AssumeExpCmd LAnd(B525:54 B526:54 )
		AnnotationCmd:56 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet","value":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"CANON57!!25","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.scalarization.sort","type":"vc.data.ScalarizationSort","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.ScalarizationSort.Packed","packedStart":{"#class":"vc.data.ScalarizationSort.Split","idx":"c"},"start":0}},{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.storage.bit-width","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":160},{"key":{"name":"tac.storage.pretty.paths","type":"analysis.storage.DisplayPaths","erasureStrategy":"Erased"},"value":{"paths":[{"#class":"analysis.storage.DisplayPath.Root","name":"lp_token"}]}},{"key":{"name":"tac.slot.type","type":"spec.cvlast.typedescriptors.EVMTypeDescriptor$EVMValueType","erasureStrategy":"Canonical"},"value":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.address"}},{"key":{"name":"tac.storage.non-indexed-path","type":"analysis.storage.StorageAnalysisResult$NonIndexedPath","erasureStrategy":"Canonical"},"value":{"#class":"analysis.storage.StorageAnalysisResult.NonIndexedPath.Root","slot":"c"}},{"key":{"name":"tac.storage","type":"java.math.BigInteger","erasureStrategy":"Canonical"},"value":"ce4604a0000000000000000000000017"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1018}]},"displayPath":{"#class":"analysis.storage.DisplayPath.Root","name":"lp_token"},"storageType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.address"},"contractInstance":"ce4604a0000000000000000000000017","linkableStorageReadId":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet.Id","id":3}}}
		AnnotationCmd:56 JSON{"key":{"name":"init.reorder.fence","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		AssignExpCmd:146 tacMCANON2!!529:13 Store(tacMCANON2!!301:13 0x140 0x18160ddd00000000000000000000000000000000000000000000000000000000 )
		AssignExpCmd:146 R530:150 0x140
		AssignHavocCmd:146 R531:67
		AssignHavocCmd:56 tacReturndata!!532:78
		JumpCmd:56 0_0_0_4_0_0
	}
	Block 2_0_0_7_0_0 Succ [0_0_0_10_0_0] {
		AssumeNotCmd:142 false
		AnnotationCmd:105 JSON{"key":{"name":"pta.fake-return.start","type":"analysis.CmdPointer","erasureStrategy":"Erased"},"value":{"block":{"#class":"tac.BlockIdentifier","origStartPc":3129,"stkTop":1017,"decompCopy":0,"calleeIdx":0,"topOfStackValue":2,"freshCopy":0},"pos":1}}
		AnnotationCmd:105 JSON{"key":{"name":"pta.fake-return.end","type":"analysis.CmdPointer","erasureStrategy":"Erased"},"value":{"block":{"#class":"tac.BlockIdentifier","origStartPc":3129,"stkTop":1017,"decompCopy":0,"calleeIdx":0,"topOfStackValue":2,"freshCopy":0},"pos":6}}
		AssumeNotCmd:139 false
		AssignExpCmd:140 R533:67 Select(tacMCANON2!!444:14 0x120 )
		AssignExpCmd:105 B535:54 Le(CANON57!!25:154 0xffffffffffffffffffffffffffffffffffffffff )
		AssignExpCmd:105 B536:54 Ge(CANON57!!25:154 0x0 )
		NopCmd
		AssumeExpCmd LAnd(B535:54 B536:54 )
		AnnotationCmd:105 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet","value":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"CANON57!!25","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.scalarization.sort","type":"vc.data.ScalarizationSort","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.ScalarizationSort.Packed","packedStart":{"#class":"vc.data.ScalarizationSort.Split","idx":"c"},"start":0}},{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.storage.bit-width","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":160},{"key":{"name":"tac.storage.pretty.paths","type":"analysis.storage.DisplayPaths","erasureStrategy":"Erased"},"value":{"paths":[{"#class":"analysis.storage.DisplayPath.Root","name":"lp_token"}]}},{"key":{"name":"tac.slot.type","type":"spec.cvlast.typedescriptors.EVMTypeDescriptor$EVMValueType","erasureStrategy":"Canonical"},"value":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.address"}},{"key":{"name":"tac.storage.non-indexed-path","type":"analysis.storage.StorageAnalysisResult$NonIndexedPath","erasureStrategy":"Canonical"},"value":{"#class":"analysis.storage.StorageAnalysisResult.NonIndexedPath.Root","slot":"c"}},{"key":{"name":"tac.storage","type":"java.math.BigInteger","erasureStrategy":"Canonical"},"value":"ce4604a0000000000000000000000017"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1018}]},"displayPath":{"#class":"analysis.storage.DisplayPath.Root","name":"lp_token"},"storageType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.address"},"contractInstance":"ce4604a0000000000000000000000017","linkableStorageReadId":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet.Id","id":10}}}
		AnnotationCmd:105 JSON{"key":{"name":"init.reorder.fence","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		AssignExpCmd:151 tacMCANON2!!539:14 Store(tacMCANON2!!444:14 0x140 0x18160ddd00000000000000000000000000000000000000000000000000000000 )
		AssignExpCmd:151 R540:150 0x140
		AssignHavocCmd:151 R541:67
		AssignHavocCmd:105 tacReturndata!!542:78
		JumpCmd:105 0_0_0_10_0_0
	}
	Block 4_0_0_0_0_0 Succ [0_0_0_5_0_0] {
		AssumeNotCmd:56 false
		AssumeNotCmd:56 false
		AnnotationCmd JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageGlobalChangeSnippet.StorageTakeSnapshot","lhs":{"namePrefix":"lastStorage","tag":{"#class":"tac.Tag.BlockchainState"},"callIndex":0,"meta":[{"key":{"name":"cvl.local","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true},{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"lastStorage"},{"key":{"name":"cvl.type","type":"spec.cvlast.CVLType$PureCVLType","erasureStrategy":"CallTrace"},"value":{"#class":"spec.cvlast.CVLType.PureCVLType.VMInternal.BlockchainState"}},{"key":{"name":"cvl","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true},{"key":{"name":"cvl.display","type":"java.lang.String","erasureStrategy":"CallTrace"},"value":"lastStorage"}]}}}
		AssignExpCmd:155 CANON179!!543:156 Eq(I27 R505:150 )
		AssumeCmd:56 CANON179!!543:156
		AnnotationCmd:56 JSON{"key":{"name":"cvl.label.end","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		AnnotationCmd:157 JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Cmd","cmd":{"cmd_type":"spec.cvlast.CVLCmd.Simple.Apply","cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/specs/ViewReentrancy.spec","start":{"line":27,"character":4},"end":{"line":27,"character":15}},"exp":{"#class":"spec.cvlast.CVLExp.ApplyExp.ContractFunction.Symbolic","methodIdWithCallContext":{"#class":"spec.cvlast.ParametricMethod","methodId":"f","host":{"name":"curve"}},"args":[{"#class":"spec.cvlast.CVLExp.VariableExp","id":"e","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":0}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"env","fields":[{"fieldName":"msg","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"msg","fields":[{"fieldName":"sender","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"value","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}}]}},{"fieldName":"tx","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"tx","fields":[{"fieldName":"origin","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}}]}},{"fieldName":"block","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"block","fields":[{"fieldName":"coinbase","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"difficulty","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"gaslimit","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"number","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"timestamp","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}}]}}]},"cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/specs/ViewReentrancy.spec","start":{"line":27,"character":4},"end":{"line":27,"character":15}}},"twoStateIndex":"NEITHER"},{"#class":"spec.cvlast.CVLExp.VariableExp","id":"data","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":0}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.VMInternal.RawArgs"},"cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/specs/ViewReentrancy.spec","start":{"line":27,"character":4},"end":{"line":27,"character":15}}},"twoStateIndex":"NEITHER"}],"noRevert":true,"storage":{"#class":"spec.cvlast.CVLExp.VariableExp","id":"lastStorage","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":0}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.VMInternal.BlockchainState"},"cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/specs/ViewReentrancy.spec","start":{"line":27,"character":4},"end":{"line":27,"character":15}}},"twoStateIndex":"NEITHER"},"tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":0}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Void"},"cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/specs/ViewReentrancy.spec","start":{"line":27,"character":4},"end":{"line":27,"character":5}}}},"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":0}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}}}}}
		NopCmd
		NopCmd
		NopCmd
		NopCmd
		NopCmd
		NopCmd
		AssignExpCmd R550:158 CANON188:10
		AnnotationCmd:157 JSON{"key":{"name":"call.trace.push","type":"analysis.icfg.Inliner$CallStack$PushRecord","erasureStrategy":"Canonical"},"value":"rO0ABXNyACphbmFseXNpcy5pY2ZnLklubGluZXIkQ2FsbFN0YWNrJFB1c2hSZWNvcmSX8+DCTLCH+AIAA0kACGNhbGxlZUlkTAAGY2FsbGVldAATTHZjL2RhdGEvTWV0aG9kUmVmO0wAB3N1bW1hcnl0ABVMdmMvZGF0YS9DYWxsU3VtbWFyeTt4cAAAAAVzcgARdmMuZGF0YS5NZXRob2RSZWbJlJTzzU9pGAIAA0wABGF0dHJ0ABdMc2NlbmUvTWV0aG9kQXR0cmlidXRlO0wACmNvbnRyYWN0SWR0ABZMamF2YS9tYXRoL0JpZ0ludGVnZXI7TAAHc2lnSGFzaHQAEExldm0vU2lnaGFzaEludDt4cHNyABxzY2VuZS5NZXRob2RBdHRyaWJ1dGUkQ29tbW9uNHjdebdr9XMCAAB4cgAVc2NlbmUuTWV0aG9kQXR0cmlidXRlcYg2pYWutuUCAAB4cHNyABRqYXZhLm1hdGguQmlnSW50ZWdlcoz8nx+pO/sdAwAGSQAIYml0Q291bnRJAAliaXRMZW5ndGhJABNmaXJzdE5vbnplcm9CeXRlTnVtSQAMbG93ZXN0U2V0Qml0SQAGc2lnbnVtWwAJbWFnbml0dWRldAACW0J4cgAQamF2YS5sYW5nLk51bWJlcoaslR0LlOCLAgAAeHD///////////////7////+AAAAAXVyAAJbQqzzF/gGCFTgAgAAeHAAAAAQzkYEoAAAAAAAAAAAAAAAF3hzcgAOZXZtLlNpZ2hhc2hJbnRUdcqNMXEgeAIAAUwAAW5xAH4ABnhwc3EAfgAM///////////////+/////gAAAAF1cQB+ABAAAAAEPSSja3hw"}
		AssignExpCmd:157 M552:54 ByteMapDefinition(CANON190:bv256 -> Ite(Lt(CANON190:54 CANON188:10 ) Unconstrained(bv256) 0x0 ) )
		AssignExpCmd tacCalldatabuf@5:159 LongStore(M552:54 0x0 CANON186:9 0x0 CANON188:10 )
		NopCmd
		AssumeExpCmd Ge(R550:160 0x24 )
		NopCmd
		AssumeExpCmd Ge(0x7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff R550:160 )
		AssignExpCmd:157 B557 LAnd(Ge(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff CANON58:25 ) Le(0x0 CANON58:25 ) )
		AssertCmd:157 B557 "sanity bounds check on cvl to vm encoding of tacTmp!5024:int failed"
		AssignExpCmd:157 R558:54 Apply(safe_math_narrow:bif CANON58:25)
		NopCmd
		AssumeExpCmd LAnd(Le(R558:57 0xffffffffffffffffffffffffffffffffffffffff ) Ge(R558:57 0x0 ) )
		AssignExpCmd:157 B562 LAnd(Ge(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff CANON59:26 ) Le(0x0 CANON59:26 ) )
		AssertCmd:157 B562 "sanity bounds check on cvl to vm encoding of tacTmp!5027:int failed"
		AssignExpCmd:157 R563:54 Apply(safe_math_narrow:bif CANON59:26)
		NopCmd
		AssumeExpCmd LAnd(Le(R563:58 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff ) Ge(R563:58 0x0 ) )
		AssignExpCmd:157 B568 LAnd(Ge(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff CANON60:27 ) Le(0x0 CANON60:27 ) )
		AssertCmd:157 B568 "sanity bounds check on cvl to vm encoding of tacTmp!5031:int failed"
		AssignExpCmd:157 R569:54 Apply(safe_math_narrow:bif CANON60:27)
		NopCmd
		AssumeExpCmd LAnd(Le(R569:59 0xffffffffffffffffffffffffffffffffffffffff ) Ge(R569:59 0x0 ) )
		AssignExpCmd:157 B573 LAnd(Ge(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff CANON64:31 ) Le(0x0 CANON64:31 ) )
		AssertCmd:157 B573 "sanity bounds check on cvl to vm encoding of tacTmp!5034:int failed"
		AssignExpCmd:157 R574:54 Apply(safe_math_narrow:bif CANON64:31)
		NopCmd
		AssumeExpCmd LAnd(Le(R574:60 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff ) Ge(R574:60 0x0 ) )
		AssignExpCmd:157 B578 LAnd(Ge(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff CANON65:32 ) Le(0x0 CANON65:32 ) )
		AssertCmd:157 B578 "sanity bounds check on cvl to vm encoding of tacTmp!5037:int failed"
		AssignExpCmd:157 R579:54 Apply(safe_math_narrow:bif CANON65:32)
		NopCmd
		AssumeExpCmd LAnd(Le(R579:61 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff ) Ge(R579:61 0x0 ) )
		AssignExpCmd:157 B583 LAnd(Ge(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff CANON59:26 ) Le(0x0 CANON59:26 ) )
		AssertCmd:157 B583 "sanity bounds check on cvl to vm encoding of tacTmp!5040:int failed"
		AssignExpCmd:157 R584:54 Apply(safe_math_narrow:bif CANON59:26)
		AssignExpCmd:157 B586 LAnd(Ge(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff CANON58:25 ) Le(0x0 CANON58:25 ) )
		AssertCmd:157 B586 "sanity bounds check on cvl to vm encoding of tacTmp!5043:int failed"
		AssignExpCmd:157 R587:54 Apply(safe_math_narrow:bif CANON58:25)
		AssignExpCmd:157 R590:54 Select(tacBalance!!216:18 Apply(to_skey:bif R587:54) )
		AssignExpCmd:161 I591:54 IntSub(R590:54 R584:54 )
		AssignExpCmd:161 tacBalance!!592:18 Store(tacBalance!!216:18 Apply(to_skey:bif R587:54) I591:54 )
		AssignExpCmd:157 R593:54 Select(tacBalance!!592:18 Apply(to_skey:bif R30:43) )
		AssignExpCmd:161 R594:54 Add(R593:54 R584:54)
		NopCmd
		AssumeExpCmd Apply(add_noofl:bif R593:54 R584:54)
		AssignExpCmd:161 tacBalance!!596:18 Store(tacBalance!!592:18 Apply(to_skey:bif R30:43) R594:54 )
		AnnotationCmd:157 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.BalanceSnippet","srcAccountInfo":{"old":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R590","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}]},"new":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"I591","tag":{"#class":"tac.Tag.Int"},"callIndex":0,"meta":[{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}]},"addr":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R587","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}]}},"trgAccountInfo":{"old":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R593","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}]},"new":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R594","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}]},"addr":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R30","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"tacContractAt"},{"key":{"name":"tac.contract.sym.addr.name","type":"java.lang.String","erasureStrategy":"Erased"},"value":"curve"},{"key":{"name":"tac.contract.sym.addr","type":"java.math.BigInteger","erasureStrategy":"Erased"},"value":"ce4604a0000000000000000000000017"}]}},"transferredAmount":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R584","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}]}}}
		JumpCmd 0_0_0_5_0_0
	}
	Block 7_0_0_0_0_0 Succ [] {
		AssumeNotCmd:105 false
		AssumeNotCmd:105 false
		AnnotationCmd JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageGlobalChangeSnippet.StorageTakeSnapshot","lhs":{"namePrefix":"lastStorage","tag":{"#class":"tac.Tag.BlockchainState"},"callIndex":0,"meta":[{"key":{"name":"cvl.local","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true},{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"lastStorage"},{"key":{"name":"cvl.type","type":"spec.cvlast.CVLType$PureCVLType","erasureStrategy":"CallTrace"},"value":{"#class":"spec.cvlast.CVLType.PureCVLType.VMInternal.BlockchainState"}},{"key":{"name":"cvl","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true},{"key":{"name":"cvl.display","type":"java.lang.String","erasureStrategy":"CallTrace"},"value":"lastStorage"}]}}}
		AssignExpCmd:162 CANON279!!597:156 Eq(I12 R520:150 )
		AssumeCmd:105 CANON279!!597:156
		AnnotationCmd:105 JSON{"key":{"name":"cvl.label.end","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		AnnotationCmd:163 JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Cmd","cmd":{"cmd_type":"spec.cvlast.CVLCmd.Simple.Assert","cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/specs/ViewReentrancy.spec","start":{"line":29,"character":4},"end":{"line":29,"character":16}},"exp":{"#class":"spec.cvlast.CVLExp.VariableExp","id":"cond","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":0}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"},"cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/specs/ViewReentrancy.spec","start":{"line":29,"character":4},"end":{"line":29,"character":16}}},"twoStateIndex":"NEITHER"},"description":"","scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":0}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}}}}}
		AssertCmd:164 B26 ""
		AnnotationCmd:163 JSON{"key":{"name":"cvl.label.end","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
	}
	Block 0_0_0_5_0_0 Succ [0_0_0_6_0_0] {
		LabelCmd "Start procedure curve-_balances(uint256)"
		AnnotationCmd JSON{"key":{"name":"fps.free-pointer-is-scalarized","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true}
		AssignExpCmd R599:54 Select(tacExtcodesize!!7:4 Apply(to_skey:bif R30:63) )
		NopCmd
		AssumeExpCmd Gt(R599:54 0x0 )
		AnnotationCmd JSON{"key":{"name":"internal.func.finder.info","type":"analysis.ip.InternalFunctionFinderReport","erasureStrategy":"Erased"},"value":"rO0ABXNyAChhbmFseXNpcy5pcC5JbnRlcm5hbEZ1bmN0aW9uRmluZGVyUmVwb3J0ian+bYn1VdACAAFMABN1bnJlc29sdmVkRnVuY3Rpb25zdAAPTGphdmEvdXRpbC9TZXQ7eHBzcgAhZGF0YXN0cnVjdHVyZXMuTGlua2VkQXJyYXlIYXNoU2V0AAAAAAAAAAEDAAJGAApsb2FkRmFjdG9yTAAJaGFzaFRhYmxldAAuTGRhdGFzdHJ1Y3R1cmVzL2FycmF5aGFzaHRhYmxlL0FycmF5SGFzaFRhYmxlO3hwdwgAAAAAQAAAAHg="}
		AnnotationCmd JSON{"key":{"name":"fps.free-pointer-is-scalarized","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true}
		NopCmd
		AssumeExpCmd Eq(R563:58 0x0 )
		NopCmd
		AssumeExpCmd LNot(Lt(R550:160 0x4 ) )
		NopCmd
		AssumeExpCmd Gt(0x82c63066 tacSighash!!38:47 )
		NopCmd
		AssumeExpCmd LNot(Eq(0x3842f776 tacSighash!!38:47 ) )
		NopCmd
		AssumeExpCmd Eq(0x3d24a36b tacSighash!!38:47 )
		AssignExpCmd:165 R606:83 Sub(CANON188:10 0x4 )
		NopCmd
		AssumeExpCmd LNot(Slt(R606:83 0x20 ) )
		AssignExpCmd:166 R608:72 Select(tacCalldatabuf@5:159 0x4 )
		AnnotationCmd JSON{"key":{"name":"pta.end-allocation","type":"analysis.alloc.AllocationAnalysis$AbstractLocation","erasureStrategy":"Erased"},"value":{"prevFPWriteIdx":0,"nextFPWriteCmd":{"block":{"#class":"tac.BlockIdentifier","origStartPc":4211,"stkTop":1012,"decompCopy":0,"calleeIdx":0,"topOfStackValue":0,"freshCopy":0},"pos":8},"sort":{"#class":"analysis.alloc.AllocationAnalysis.Alloc.ConstBlock","sz":"40"}}}
		AssignExpCmd:167 R609:83 Select(CANON115!!8:5 Apply(skey_basic:bif 0x8) )
		AnnotationCmd JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet","value":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R609","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1017}]},"displayPath":{"#class":"analysis.storage.DisplayPath.ArrayAccess","index":{"#class":"vc.data.TACSymbol.Const","value":"0"},"base":{"#class":"analysis.storage.DisplayPath.Root","name":"admin_balances"}},"storageType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256},"contractInstance":"ce4604a0000000000000000000000017","linkableStorageReadId":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet.None"}}}
		AssignExpCmd:168 R610:93 Select(tacBalance!!596:18 Apply(to_skey:bif R30:63) )
		NopCmd
		AssumeExpCmd LNot(Lt(R610:93 R609:83 ) )
		AssignExpCmd:169 R612:72 Sub(R610:93 R609:83 )
		NopCmd
		AssumeExpCmd LNot(Lt(R612:72 R608:72 ) )
		AssignExpCmd:170 R616:84 Select(CANON115!!8:5 Apply(skey_basic:bif 0x9) )
		AnnotationCmd JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet","value":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R616","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1018}]},"displayPath":{"#class":"analysis.storage.DisplayPath.ArrayAccess","index":{"#class":"vc.data.TACSymbol.Const","value":"1"},"base":{"#class":"analysis.storage.DisplayPath.Root","name":"admin_balances"}},"storageType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256},"contractInstance":"ce4604a0000000000000000000000017","linkableStorageReadId":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet.None"}}}
		AssignExpCmd B618:54 Le(CANON56!!24:171 0xffffffffffffffffffffffffffffffffffffffff )
		AssignExpCmd B619:54 Ge(CANON56!!24:171 0x0 )
		NopCmd
		AssumeExpCmd LAnd(B618:54 B619:54 )
		AnnotationCmd JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet","value":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"CANON56!!24","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.scalarization.sort","type":"vc.data.ScalarizationSort","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.ScalarizationSort.Packed","packedStart":{"#class":"vc.data.ScalarizationSort.Split","idx":"b"},"start":0}},{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.storage.bit-width","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":160},{"key":{"name":"tac.storage.pretty.paths","type":"analysis.storage.DisplayPaths","erasureStrategy":"Erased"},"value":{"paths":[{"#class":"analysis.storage.DisplayPath.Root","name":"coins_1"}]}},{"key":{"name":"tac.slot.type","type":"spec.cvlast.typedescriptors.EVMTypeDescriptor$EVMValueType","erasureStrategy":"Canonical"},"value":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.address"}},{"key":{"name":"tac.storage.non-indexed-path","type":"analysis.storage.StorageAnalysisResult$NonIndexedPath","erasureStrategy":"Canonical"},"value":{"#class":"analysis.storage.StorageAnalysisResult.NonIndexedPath.Root","slot":"b"}},{"key":{"name":"tac.storage","type":"java.math.BigInteger","erasureStrategy":"Canonical"},"value":"ce4604a0000000000000000000000017"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1016}]},"displayPath":{"#class":"analysis.storage.DisplayPath.Root","name":"coins_1"},"storageType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.address"},"contractInstance":"ce4604a0000000000000000000000017","linkableStorageReadId":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet.Id","id":5}}}
		AnnotationCmd JSON{"key":{"name":"init.reorder.fence","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		AssignExpCmd:172 tacMCANON6!!622:17 Store(tacMCANON6!!20:17 0x100 0x70a0823100000000000000000000000000000000000000000000000000000000 )
		AssignExpCmd:173 tacMCANON6!!624:17 Store(tacMCANON6!!622:17 0x104 R30:63 )
		AssignExpCmd:172 R625:72 0x100
		AssignHavocCmd:172 R626:69
		AssignHavocCmd tacReturndata!!627:78
		JumpCmd 0_0_0_6_0_0
	}
	Block 0_0_0_6_0_0 Succ [5_0_0_5_0_0] {
		AnnotationCmd JSON{"key":{"name":"call.trace.push","type":"analysis.icfg.Inliner$CallStack$PushRecord","erasureStrategy":"Canonical"},"value":"rO0ABXNyACphbmFseXNpcy5pY2ZnLklubGluZXIkQ2FsbFN0YWNrJFB1c2hSZWNvcmSX8+DCTLCH+AIAA0kACGNhbGxlZUlkTAAGY2FsbGVldAATTHZjL2RhdGEvTWV0aG9kUmVmO0wAB3N1bW1hcnl0ABVMdmMvZGF0YS9DYWxsU3VtbWFyeTt4cAAAAAZzcgARdmMuZGF0YS5NZXRob2RSZWbJlJTzzU9pGAIAA0wABGF0dHJ0ABdMc2NlbmUvTWV0aG9kQXR0cmlidXRlO0wACmNvbnRyYWN0SWR0ABZMamF2YS9tYXRoL0JpZ0ludGVnZXI7TAAHc2lnSGFzaHQAEExldm0vU2lnaGFzaEludDt4cHNyABxzY2VuZS5NZXRob2RBdHRyaWJ1dGUkQ29tbW9uNHjdebdr9XMCAAB4cgAVc2NlbmUuTWV0aG9kQXR0cmlidXRlcYg2pYWutuUCAAB4cHNyABRqYXZhLm1hdGguQmlnSW50ZWdlcoz8nx+pO/sdAwAGSQAIYml0Q291bnRJAAliaXRMZW5ndGhJABNmaXJzdE5vbnplcm9CeXRlTnVtSQAMbG93ZXN0U2V0Qml0SQAGc2lnbnVtWwAJbWFnbml0dWRldAACW0J4cgAQamF2YS5sYW5nLk51bWJlcoaslR0LlOCLAgAAeHD///////////////7////+AAAAAXVyAAJbQqzzF/gGCFTgAgAAeHAAAAAQzkYEoAAAAAAAAAAAAAAABHhzcgAOZXZtLlNpZ2hhc2hJbnRUdcqNMXEgeAIAAUwAAW5xAH4ABnhwc3EAfgAM///////////////+/////gAAAAF1cQB+ABAAAAAEcKCCMXhzcgATdmMuZGF0YS5DYWxsU3VtbWFyeZQcmw5vl+FdAgAQSQAJc3VtbWFyeUlkTAAOY2FsbENvbnZlbnRpb250ACZMaW5zdHJ1bWVudGF0aW9uL2NhbGxzL0NhbGxDb252ZW50aW9uO0wACmNhbGxUYXJnZXR0ABpMYW5hbHlzaXMvaWNmZy9DYWxsVGFyZ2V0O0wACGNhbGxUeXBldAAVTHZjL2RhdGEvVEFDQ2FsbFR5cGU7TAAPY2Fubm90QmVJbmxpbmVkdAAtTGFuYWx5c2lzL2ljZmcvSW5saW5lciRJbGxlZ2FsSW5saW5pbmdSZWFzb247TAAGZ2FzVmFydAATTHZjL2RhdGEvVEFDU3ltYm9sO0wABmluQmFzZXEAfgAbTAAIaW5PZmZzZXRxAH4AG0wABmluU2l6ZXEAfgAbTAAMb3JpZ0NhbGxjb3JldAAgTHZjL2RhdGEvVEFDQ21kJFNpbXBsZSRDYWxsQ29yZTtMAAdvdXRCYXNlcQB+ABtMAAlvdXRPZmZzZXRxAH4AG0wAB291dFNpemVxAH4AG0wADXNpZ1Jlc29sdXRpb250AA9MamF2YS91dGlsL1NldDtMAAV0b1ZhcnEAfgAbTAAIdmFsdWVWYXJxAH4AG3hwAAAAA3NyACRpbnN0cnVtZW50YXRpb24uY2FsbHMuQ2FsbENvbnZlbnRpb25HtO1ulL788QIAA0kACGNhbGxlcklkTAAFaW5wdXR0ABlMYW5hbHlzaXMvaWNmZy9DYWxsSW5wdXQ7TAAGcmF3T3V0dAAiTGluc3RydW1lbnRhdGlvbi9jYWxscy9DYWxsT3V0cHV0O3hwAAAAAHNyABdhbmFseXNpcy5pY2ZnLkNhbGxJbnB1dJjJD1MhNUxQAgAHTAAHYmFzZVZhcnQAGUx2Yy9kYXRhL1RBQ0V4cHIkU3ltJFZhcjtMABBlbmNvZGVkQXJndW1lbnRzdAAjTGFuYWx5c2lzL2ljZmcvQUJJQXJndW1lbnRFbmNvZGluZztMABNpbnB1dFNpemVMb3dlckJvdW5kcQB+AAZMAAZvZmZzZXR0ABVMdmMvZGF0YS9UQUNFeHByJFN5bTtMABRyYW5nZVRvRGVjb21wb3NlZEFyZ3QAD0xqYXZhL3V0aWwvTWFwO0wAEHNpbXBsaWZpZWRPZmZzZXR0ABtMdmMvZGF0YS9UQUNFeHByJFN5bSRDb25zdDtMAARzaXplcQB+ACZ4cHNyABd2Yy5kYXRhLlRBQ0V4cHIkU3ltJFZhcskrg43eGgPnAgACTAABc3QAF0x2Yy9kYXRhL1RBQ1N5bWJvbCRWYXI7TAADdGFndAAJTHRhYy9UYWc7eHIAE3ZjLmRhdGEuVEFDRXhwciRTeW2iVj0S4YSNUAIAAHhyAA92Yy5kYXRhLlRBQ0V4cHJYhGlUu/v+yAIAAHhwc3IANnZjLmRhdGEuVEFDU3ltYm9sJFZhciRXaXRoRGVmYXVsdENhbGxJbmRleCRXaXRoQnl0ZU1hcJ7+oHF4CHAAAgACTAAEbWV0YXQALUxrb3RsaW54L2NvbGxlY3Rpb25zL2ltbXV0YWJsZS9QZXJzaXN0ZW50TWFwO0wACm5hbWVQcmVmaXh0ABJMamF2YS9sYW5nL1N0cmluZzt4cgAVdmMuZGF0YS5UQUNTeW1ib2wkVmFyCYrCGVl9SXYCAAB4cgARdmMuZGF0YS5UQUNTeW1ib2zd3Run/CoWswIAAHhwc3IAJmRhdGFzdHJ1Y3R1cmVzLnRyZWFwLkhhc2hUcmVhcE1hcCROb2Rlf2t9acJIPnQCAANMAANrZXl0ABJMamF2YS9sYW5nL09iamVjdDtMAARuZXh0dAA1TGRhdGFzdHJ1Y3R1cmVzL3RyZWFwL0hhc2hUcmVhcE1hcCRNb3JlS2V5VmFsdWVQYWlycztMAAV2YWx1ZXEAfgA3eHIAIWRhdGFzdHJ1Y3R1cmVzLnRyZWFwLkhhc2hUcmVhcE1hcPMJ/2vt3boKAgAAeHIAHWRhdGFzdHJ1Y3R1cmVzLnRyZWFwLlRyZWFwTWFw46LAyn3v5moCAAB4cgAaZGF0YXN0cnVjdHVyZXMudHJlYXAuVHJlYXA88f21zZwbdQIAAkwABGxlZnR0ABxMZGF0YXN0cnVjdHVyZXMvdHJlYXAvVHJlYXA7TAAFcmlnaHRxAH4APHhwcHNxAH4ANnBzcQB+ADZwcHNyAAt0YWMuTWV0YUtleVF/W3MiCfIZAgADTAAPZXJhc3VyZVN0cmF0ZWd5dAAdTHRhYy9NZXRhS2V5JEVyYXN1cmVTdHJhdGVneTtMAARuYW1lcQB+ADJMAAN0eXB0ABFMamF2YS9sYW5nL0NsYXNzO3hwfnIAG3RhYy5NZXRhS2V5JEVyYXN1cmVTdHJhdGVneQAAAAAAAAAAEgAAeHIADmphdmEubGFuZy5FbnVtAAAAAAAAAAASAAB4cHQACUNhbm9uaWNhbHQAF3RhYy5tZW1vcnkucGFydGl0aW9uLWlkdnIAEWphdmEubGFuZy5JbnRlZ2VyEuKgpPeBhzgCAAFJAAV2YWx1ZXhxAH4ADnBzcQB+AEkAAAAGc3EAfgBAcQB+AEZ0ABJUYWMuc3ltYm9sLmtleXdvcmR2cgAQamF2YS5sYW5nLlN0cmluZ6DwpDh6O7NCAgAAeHBwdAAEdGFjTXNxAH4AQHEAfgBGdAANdGFjLmlzLm1lbW9yeXZyACJ0YWMuTWV0YU1hcCRDb21wYW5pb24kTm90aGluZ1ZhbHVl8nsHH85ykpUCAAB4cHBzcQB+AFN0AA90YWNNQ0FOT042ISE2MjRzcgAPdGFjLlRhZyRCeXRlTWFwNb/Ry6GDRgkCAAB4cgALdGFjLlRhZyRNYXABJytzDV3P/QIAAHhyAAd0YWMuVGFnLk9V3gn2xngCAAB4cHBzcQB+AAz///////////////7////+AAAAAXVxAH4AEAAAAAEkeHNxAH4AKnNyADV2Yy5kYXRhLlRBQ1N5bWJvbCRWYXIkV2l0aERlZmF1bHRDYWxsSW5kZXgkV2l0aEJpdDI1NnqsyEgq0drPAgACTAAEbWV0YXEAfgAxTAAKbmFtZVByZWZpeHEAfgAyeHEAfgAzc3EAfgA2c3EAfgA2cHBxAH4ATHB0AAFMcHNxAH4AQHEAfgBGdAAQdGFjLnN0YWNrLmhlaWdodHEAfgBKcHNxAH4ASQAAA/V0AARSNjI1c3IADnRhYy5UYWckQml0MjU2IyLQT+LlKkgCAAB4cQB+AFlzcgARamF2YS51dGlsLkhhc2hNYXAFB9rBwxZg0QMAAkYACmxvYWRGYWN0b3JJAAl0aHJlc2hvbGR4cD9AAAAAAAADdwgAAAAEAAAAAnNyAB5hbmFseXNpcy5pY2ZnLlNjcmF0Y2hCeXRlUmFuZ2XBTLaPpUzj2gIAAkwABGZyb21xAH4ABkwAAnRvcQB+AAZ4cHNxAH4ADP///////////////v////4AAAAAdXEAfgAQAAAAAHhzcQB+AAz///////////////7////+AAAAAXVxAH4AEAAAAAEDeHNyAC1hbmFseXNpcy5pY2ZnLkRlY29tcG9zZWRDYWxsSW5wdXRBcmckQ29uc3RhbnSFavLdQafqPQIAA0wAAWN0ABlMdmMvZGF0YS9UQUNTeW1ib2wkQ29uc3Q7TAARY29udHJhY3RSZWZlcmVuY2V0AC9MYW5hbHlzaXMvaWNmZy9DYWxsR3JhcGhCdWlsZGVyJENhbGxlZENvbnRyYWN0O0wADHNjcmF0Y2hSYW5nZXQAIExhbmFseXNpcy9pY2ZnL1NjcmF0Y2hCeXRlUmFuZ2U7eHIAJGFuYWx5c2lzLmljZmcuRGVjb21wb3NlZENhbGxJbnB1dEFy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ADZwc3EAfgA2cHBzcQB+AEBxAH4ARnQAHHRhYy5zdG9yYWdlLm5vbi1pbmRleGVkLXBhdGh2cgA1YW5hbHlzaXMuc3RvcmFnZS5TdG9yYWdlQW5hbHlzaXNSZXN1bHQkTm9uSW5kZXhlZFBhdGgIwaBLofo/RQIAAHhwcHNyADphbmFseXNpcy5zdG9yYWdlLlN0b3JhZ2VBbmFseXNpc1Jlc3VsdCROb25JbmRleGVkUGF0aCRSb290vzf12KXqCv8CAAFMAARzbG90cQB+AAZ4cQB+ARpxAH4BE3NxAH4AQHEAfgBGdAANdGFjLnNsb3QudHlwZXZyADpzcGVjLmN2bGFzdC50eXBlZGVzY3JpcHRvcnMuRVZNVHlwZURlc2NyaXB0b3IkRVZNVmFsdWVUeXBlxomvArrquCUCAAB4cgAtc3BlYy5jdmxhc3QudHlwZWRlc2NyaXB0b3JzLkVWTVR5cGVEZXNjcmlwdG9yyFGp8TzCah0CAAB4cHBzcgA1c3BlYy5jdmxhc3QudHlwZWRlc2NyaXB0b3JzLkVWTVR5cGVEZXNjcmlwdG9yJGFkZHJlc3N6+GX0b5egKQIAAHhyAERzcGVjLmN2bGFzdC50eXBlZGVzY3JpcHRvcnMuRVZNVHlwZURlc2NyaXB0b3IkRVZNSXNvbW9ycGhpY1ZhbHVlVHlwZfd1mJFuEKEPAgAAeHEAfgEgc3EAfgBAcQB+AJB0ABh0YWMuc3RvcmFnZS5wcmV0dHkucGF0aHN2cgAdYW5hbHlzaXMuc3RvcmFnZS5EaXNwbGF5UGF0aHP3REu3w/VRFgIAAUwABXBhdGhzcQB+AB14cHBzcQB+AShzcgAXamF2YS51dGlsLkxpbmtlZEhhc2hTZXTYbNdald0qHgIAAHhyABFqYXZhLnV0aWwuSGFzaFNldLpEhZWWuLc0AwAAeHB3DAAAABA/QAAAAAAAAXNyACFhbmFseXNpcy5zdG9yYWdlLkRpc3BsYXlQYXRoJFJvb3TTc6C9mdA8cgIAAkwABGJhc2V0AB5MYW5hbHlzaXMvc3RvcmFnZS9EaXNwbGF5UGF0aDtMAARuYW1lcQB+ADJ4cgAcYW5hbHlzaXMuc3RvcmFnZS5EaXNwbGF5UGF0aE9AY+pW0iAFAgAAeHBwdAAHY29pbnNfMXhzcQB+AEBxAH4ARnQAFXRhYy5zdG9yYWdlLmJpdC13aWR0aHEAfgBKcHNxAH4ASQAAAKBwc3EAfgBAcQB+AEZ0AAt0YWMuc3RvcmFnZXEAfgCZcHEAfgCGcHEAfgBjcHNxAH4ASQAAA/l0AAtDQU5PTjU2ISEyNHNxAH4Ad3EAfgBocQB+AG1zcQB+ADBzcQB+ADZwc3EAfgA2cHNxAH4ANnBwcQB+AENwcQB+AEtxAH4ATHBxAH4AUHEAfgBRcHEAfgBVcQB+AFZzcQB+AF5zcQB+ADZzcQB+ADZwcHEAfgBMcHEAfgBicHEAfgBjcHEAfgCzcQB+AGZxAH4AtnNyACJqYXZhLnV0aWwuQ29sbGVjdGlvbnMkU2luZ2xldG9uU2V0LFJBmCnAsb8CAAFMAAdlbGVtZW50cQB+ADd4cHEAfgAUc3EAfgBec3EAfgA2c3EAfgA2c3EAfgA2c3EAfgA2cHNxAH4ANnBwcQB+AExwcQB+AGJxAH4BCnBxAH4BEHNxAH4ANnBzcQB+ADZwc3EAfgA2cHBxAH4BGHBxAH4BHXEAfgEecHEAfgElcQB+ASZwc3EAfgEoc3EAfgErdwwAAAAQP0AAAAAAAAFxAH4BMXhxAH4BM3BxAH4BNXBxAH4BNnBxAH4AhnBxAH4AY3BxAH4BOHEAfgE5c3EAfgB3cQB+AGhxAH4AbQ=="}
		AnnotationCmd JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageGlobalChangeSnippet.StorageBackupPoint","calleeTxId":6}}
		NopCmd
		AssumeExpCmd LAnd(Eq(tacCalldatasize!!3:3 0x24 ) Eq(tacCalldatasize!!3:3 0x24 ) )
		NopCmd
		AssumeExpCmd Eq(tacCalldatabufCANON0@6:1 0x70a0823100000000000000000000000000000000000000000000000000000000 )
		AssignExpCmd tacCalldatabufCANON1@6:174 R30:175
		LabelCmd "Start procedure ERC20-balanceOf(address)"
		AnnotationCmd JSON{"key":{"name":"fps.free-pointer-is-scalarized","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true}
		AssignExpCmd R631:54 Select(tacExtcodesize!!7:4 Apply(to_skey:bif R29:81) )
		NopCmd
		AssumeExpCmd Gt(R631:54 0x0 )
		AnnotationCmd JSON{"key":{"name":"internal.func.finder.info","type":"analysis.ip.InternalFunctionFinderReport","erasureStrategy":"Erased"},"value":"rO0ABXNyAChhbmFseXNpcy5pcC5JbnRlcm5hbEZ1bmN0aW9uRmluZGVyUmVwb3J0ian+bYn1VdACAAFMABN1bnJlc29sdmVkRnVuY3Rpb25zdAAPTGphdmEvdXRpbC9TZXQ7eHBzcgAhZGF0YXN0cnVjdHVyZXMuTGlua2VkQXJyYXlIYXNoU2V0AAAAAAAAAAEDAAJGAApsb2FkRmFjdG9yTAAJaGFzaFRhYmxldAAuTGRhdGFzdHJ1Y3R1cmVzL2FycmF5aGFzaHRhYmxlL0FycmF5SGFzaFRhYmxlO3hwdwgAAAAAQAAAAHg="}
		AnnotationCmd JSON{"key":{"name":"fps.free-pointer-is-scalarized","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true}
		NopCmd
		AssumeExpCmd LNot(Lt(tacCalldatasize!!3:3 0x4 ) )
		NopCmd
		AssumeExpCmd LNot(Gt(0x39509351 tacSighash!!39:47 ) )
		NopCmd
		AssumeExpCmd LNot(Eq(0x39509351 tacSighash!!39:47 ) )
		NopCmd
		AssumeExpCmd Eq(0x70a08231 tacSighash!!39:47 )
		AssignExpCmd:176 R637:83 Sub(tacCalldatasize!!3:3 0x4 )
		AssignExpCmd B638:84 Slt(R637:83 0x20 )
		NopCmd
		AssumeExpCmd LNot(B638:84 )
		AssignExpCmd:177 R640:72 tacCalldatabufCANON1@6:178
		NopCmd
		AssumeExpCmd Eq(tacCalldatabufCANON1@6:178 tacCalldatabufCANON1@6:178 )
		AnnotationCmd JSON{"key":{"name":"internal.func.start","type":"analysis.ip.InternalFuncStartAnnotation","erasureStrategy":"CallTrace"},"value":{"id":5,"startPc":1712,"args":[{"s":{"namePrefix":"R640","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1013}]},"offset":1,"sort":"SCALAR"}],"methodSignature":{"#class":"spec.cvlast.QualifiedMethodSignature.QualifiedMethodSig","qualifiedMethodName":{"#class":"spec.cvlast.QualifiedFunction","host":{"name":"ERC20"},"methodId":"balanceOf"},"params":[{"#class":"spec.cvlast.VMParam.Named","name":"account","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$address"}}],"res":[{"#class":"spec.cvlast.VMParam.Unnamed","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256}}]},"stackOffsetToArgPos":{"1":0},"callSiteSrc":{"source":0,"begin":4374,"len":467,"jumpType":"ENTER","address":"ce4604a0000000000000000000000004","sourceContext":{"indexToFilepath":{"0":"contracts/ERC20.sol","1":"contracts/IERC20Metadata.sol","2":"Context.sol","3":"IERC20.sol"},"sourceDir":".post_autofinders.0"}}}}
		AssignExpCmd:179 R645:88 Apply(hash_3_keccak:bif Apply(skey_basic:bif 0x40) Apply(to_skey:bif tacCalldatabufCANON1@6:178) Apply(skey_basic:bif 0x0))
		AssignExpCmd:180 R646:88 Select(CANON130!!10:7 R645:181 )
		AnnotationCmd JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet","value":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R646","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1020}]},"displayPath":{"#class":"analysis.storage.DisplayPath.MapAccess","key":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R640","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1018}]},"keyTyp":{"#class":"tac.TACStorageType.IntegralType","typeLabel":"address","numBytes":"14","descriptor":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$address"},"lowerBound":null,"upperBound":null},"base":{"#class":"analysis.storage.DisplayPath.Root","name":"_balances"}},"storageType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256},"contractInstance":"ce4604a0000000000000000000000004","linkableStorageReadId":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet.None"}}}
		AnnotationCmd JSON{"key":{"name":"internal.func.end","type":"analysis.ip.InternalFuncExitAnnotation","erasureStrategy":"Canonical"},"value":{"id":5,"rets":[{"s":{"namePrefix":"R646","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1023}]},"offset":0}],"functionLayout":{"0":{"#class":"analysis.ip.InternalFuncValueLocation.Scalar"}}}}
		AnnotationCmd JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.EVMFunctionReturnWrite","returnbufOffset":"0","returnValueSym":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R646","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1023}]},"callIndex":6}}
		AnnotationCmd JSON{"key":{"name":"tac.return.path","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		LabelCmd "End procedure ERC20-balanceOf(address)"
		AssignExpCmd tacMCANON6!!648:17 Store(tacMCANON6!!624:17 0x100 R646:88 )
		AnnotationCmd JSON{"key":{"name":"call.trace.pop","type":"analysis.icfg.Inliner$CallStack$PopRecord","erasureStrategy":"Canonical"},"value":"rO0ABXNyAClhbmFseXNpcy5pY2ZnLklubGluZXIkQ2FsbFN0YWNrJFBvcFJlY29yZPAPfwSLdCWJAgABSQAIY2FsbGVlSWR4cAAAAAY="}
		JumpCmd 5_0_0_5_0_0
	}
	Block 6_0_0_0_0_0 Succ [0_0_0_7_0_0] {
		AnnotationCmd:157 JSON{"key":{"name":"call.trace.pop","type":"analysis.icfg.Inliner$CallStack$PopRecord","erasureStrategy":"Canonical"},"value":"rO0ABXNyAClhbmFseXNpcy5pY2ZnLklubGluZXIkQ2FsbFN0YWNrJFBvcFJlY29yZPAPfwSLdCWJAgABSQAIY2FsbGVlSWR4cAAAAAU="}
		AssumeNotCmd:157 false
		AssumeNotCmd:157 false
		AnnotationCmd JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageGlobalChangeSnippet.StorageTakeSnapshot","lhs":{"namePrefix":"lastStorage","tag":{"#class":"tac.Tag.BlockchainState"},"callIndex":0,"meta":[{"key":{"name":"cvl.local","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true},{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"lastStorage"},{"key":{"name":"cvl.type","type":"spec.cvlast.CVLType$PureCVLType","erasureStrategy":"CallTrace"},"value":{"#class":"spec.cvlast.CVLType.PureCVLType.VMInternal.BlockchainState"}},{"key":{"name":"cvl","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true},{"key":{"name":"cvl.display","type":"java.lang.String","erasureStrategy":"CallTrace"},"value":"lastStorage"}]}}}
		AnnotationCmd:157 JSON{"key":{"name":"cvl.label.end","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		AnnotationCmd:105 JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Cmd","cmd":{"cmd_type":"spec.cvlast.CVLCmd.Simple.AssumeCmd.Assume","cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/specs/ViewReentrancy.spec","start":{"line":28,"character":4},"end":{"line":28,"character":55}},"exp":{"#class":"spec.cvlast.CVLExp.RelopExp.EqExp","l":{"#class":"spec.cvlast.CVLExp.VariableExp","id":"after_func1","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":0}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256},"cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/specs/ViewReentrancy.spec","start":{"line":28,"character":4},"end":{"line":28,"character":55}}},"twoStateIndex":"NEITHER"},"r":{"#class":"spec.cvlast.CVLExp.ApplyExp.ContractFunction.Concrete","methodIdWithCallContext":{"#class":"spec.cvlast.ConcreteMethod","signature":{"#class":"spec.cvlast.ExternalQualifiedMethodSignature.ExternalQualifiedMethodSig","wrapped":{"#class":"spec.cvlast.QualifiedMethodSignature.QualifiedMethodSig","qualifiedMethodName":{"#class":"spec.cvlast.QualifiedFunction","host":{"name":"curve"},"methodId":"getVirtualPrice"},"params":[],"res":[{"#class":"spec.cvlast.VMParam.Unnamed","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256}}]},"sighashInt":{"n":"e25aa5fa"}}},"args":[{"#class":"spec.cvlast.CVLExp.VariableExp","id":"e_external","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":0}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"env","fields":[{"fieldName":"msg","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"msg","fields":[{"fieldName":"sender","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"value","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}}]}},{"fieldName":"tx","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"tx","fields":[{"fieldName":"origin","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}}]}},{"fieldName":"block","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"block","fields":[{"fieldName":"coinbase","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"difficulty","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"gaslimit","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"number","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"timestamp","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}}]}}]},"cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/specs/ViewReentrancy.spec","start":{"line":28,"character":4},"end":{"line":28,"character":55}}},"twoStateIndex":"NEITHER"}],"noRevert":true,"storage":{"#class":"spec.cvlast.CVLExp.VariableExp","id":"lastStorage","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":0}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.VMInternal.BlockchainState"},"cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/specs/ViewReentrancy.spec","start":{"line":28,"character":4},"end":{"line":28,"character":55}}},"twoStateIndex":"NEITHER"},"isWhole":false,"tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":0}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.VM","descriptor":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256},"context":{"#class":"spec.cvlast.typedescriptors.FromVMContext.ReturnValue"}},"cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/specs/ViewReentrancy.spec","start":{"line":28,"character":27},"end":{"line":28,"character":42}},"annotation":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.CallResolution$DirectPassing","target":{"methodSignature":{"#class":"spec.cvlast.ExternalQualifiedMethodSignature.ExternalQualifiedMethodSig","wrapped":{"#class":"spec.cvlast.QualifiedMethodSignature.QualifiedMethodSig","qualifiedMethodName":{"#class":"spec.cvlast.QualifiedFunction","host":{"name":"curve"},"methodId":"getVirtualPrice"},"params":[],"res":[{"#class":"spec.cvlast.VMParam.Unnamed","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256}}]},"sighashInt":{"n":"e25aa5fa"}},"definitelyNonPayable":true,"annotation":{"visibility":"EXTERNAL","envFree":false,"library":false},"stateMutability":"view","tag":{"#class":"spec.cvlast.CVLImportedFunctionTag.WithMethodInfo","evmMethodInfo":{"sigHash":"e25aa5fa","name":"getVirtualPrice","argTypes":[],"resultTypes":[{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256}],"stateMutability":"view","envfreeInfo":{"#class":"bridge.EnvfreeInfo.Unknown"},"isConstant":false,"isLibrary":false}}},"hasEnv":true}}},"tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":0}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"},"cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/specs/ViewReentrancy.spec","start":{"line":28,"character":12},"end":{"line":28,"character":54}}}},"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":0}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}}}}}
		NopCmd
		NopCmd
		NopCmd
		NopCmd
		NopCmd
	}
	Block 5_0_0_5_0_0 Succ [6_0_0_0_0_0] {
		AssumeNotCmd:172 false
		AnnotationCmd JSON{"key":{"name":"pta.fake-return.start","type":"analysis.CmdPointer","erasureStrategy":"Erased"},"value":{"block":{"#class":"tac.BlockIdentifier","origStartPc":1608,"stkTop":1014,"decompCopy":0,"calleeIdx":0,"topOfStackValue":2,"freshCopy":0},"pos":1}}
		AnnotationCmd JSON{"key":{"name":"pta.fake-return.end","type":"analysis.CmdPointer","erasureStrategy":"Erased"},"value":{"block":{"#class":"tac.BlockIdentifier","origStartPc":1608,"stkTop":1014,"decompCopy":0,"calleeIdx":0,"topOfStackValue":2,"freshCopy":0},"pos":6}}
		AssumeNotCmd:182 false
		AssignExpCmd:183 R655:76 Select(tacMCANON6!!648:17 0x100 )
		NopCmd
		AssumeExpCmd LNot(Lt(R655:76 R616:84 ) )
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
		CANON143
		CANON147
		CANON75
		CANON77
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
      "value": "ce4604a0000000000000000000000017"
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
      "value": "ce4604a0000000000000000000000014"
    }
  ],
  "7": [
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
      "value": "ce4604a0000000000000000000000004"
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
      "value": "ce4604a0000000000000000000000017"
    }
  ],
  "9": [
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
  "10": [
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
      "value": 1
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
      "value": 8
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
      "value": 2
    }
  ],
  "14": [
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
  "15": [
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
  "16": [
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
  "17": [
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
  "18": [
    {
      "key": {
        "name": "Tac.symbol.keyword",
        "type": "java.lang.String",
        "erasureStrategy": "Canonical"
      },
      "value": "tacBalance"
    }
  ],
  "19": [
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
  "20": [
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
  "21": [
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
  "22": [
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
  "23": [
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
      "value": "ce4604a0000000000000000000000017"
    }
  ],
  "24": [
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
      "value": "ce4604a0000000000000000000000017"
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
  "37": [
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
  "38": [
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
  "39": [
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
  "40": [
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
      "value": "ce4604a0000000000000000000000014"
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
      "value": "ce4604a0000000000000000000000004"
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
      "value": "ce4604a0000000000000000000000017"
    }
  ],
  "44": [
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
      "value": "ecrecover"
    },
    {
      "key": {
        "name": "tac.contract.sym.addr",
        "type": "java.math.BigInteger",
        "erasureStrategy": "Erased"
      },
      "value": "1"
    }
  ],
  "45": [
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
      "value": "sha256"
    },
    {
      "key": {
        "name": "tac.contract.sym.addr",
        "type": "java.math.BigInteger",
        "erasureStrategy": "Erased"
      },
      "value": "2"
    }
  ],
  "46": [
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
      "value": "identity"
    },
    {
      "key": {
        "name": "tac.contract.sym.addr",
        "type": "java.math.BigInteger",
        "erasureStrategy": "Erased"
      },
      "value": "4"
    }
  ],
  "47": [
    {
      "key": {
        "name": "Tac.symbol.keyword",
        "type": "java.lang.String",
        "erasureStrategy": "Canonical"
      },
      "value": "tacSighash"
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
  "51": [
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
  "52": [
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
  "53": [
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
  "54": [
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
  "56": [
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
  "57": [
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
  "58": [
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
  "59": [
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
  "60": [
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
  "61": [
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
  "62": [
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
  "63": [
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
      "value": "ce4604a0000000000000000000000017"
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
        "source": 0,
        "begin": 6339,
        "len": 17,
        "jumpType": "REGULAR",
        "address": "ce4604a0000000000000000000000017",
        "sourceContext": {
          "indexToFilepath": {
            "0": "contracts/curve.sol",
            "1": "Context.sol",
            "2": "ERC20.sol",
            "3": "IERC20.sol",
            "4": "IERC20Metadata.sol",
            "5": "ReentrancyGuard.sol"
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
        "source": 0,
        "begin": 6315,
        "len": 21,
        "jumpType": "REGULAR",
        "address": "ce4604a0000000000000000000000017",
        "sourceContext": {
          "indexToFilepath": {
            "0": "contracts/curve.sol",
            "1": "Context.sol",
            "2": "ERC20.sol",
            "3": "IERC20.sol",
            "4": "IERC20Metadata.sol",
            "5": "ReentrancyGuard.sol"
          },
          "sourceDir": ".post_autofinders.1"
        }
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
      "value": 1011
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
        "name": "optimization.overflow.safe",
        "type": "tac.MetaMap$Companion$NothingValue",
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
      "value": 1009
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
        "source": 0,
        "begin": 6294,
        "len": 145,
        "jumpType": "REGULAR",
        "address": "ce4604a0000000000000000000000017",
        "sourceContext": {
          "indexToFilepath": {
            "0": "contracts/curve.sol",
            "1": "Context.sol",
            "2": "ERC20.sol",
            "3": "IERC20.sol",
            "4": "IERC20Metadata.sol",
            "5": "ReentrancyGuard.sol"
          },
          "sourceDir": ".post_autofinders.1"
        }
      }
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
        "source": 0,
        "begin": 6421,
        "len": 17,
        "jumpType": "REGULAR",
        "address": "ce4604a0000000000000000000000017",
        "sourceContext": {
          "indexToFilepath": {
            "0": "contracts/curve.sol",
            "1": "Context.sol",
            "2": "ERC20.sol",
            "3": "IERC20.sol",
            "4": "IERC20Metadata.sol",
            "5": "ReentrancyGuard.sol"
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
  "72": [
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
  "73": [
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
      "value": "ce4604a0000000000000000000000017"
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
  "74": [
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
        "source": 0,
        "begin": 6379,
        "len": 39,
        "jumpType": "REGULAR",
        "address": "ce4604a0000000000000000000000017",
        "sourceContext": {
          "indexToFilepath": {
            "0": "contracts/curve.sol",
            "1": "Context.sol",
            "2": "ERC20.sol",
            "3": "IERC20.sol",
            "4": "IERC20Metadata.sol",
            "5": "ReentrancyGuard.sol"
          },
          "sourceDir": ".post_autofinders.1"
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
        "source": 6,
        "begin": 6816,
        "len": 37,
        "jumpType": "REGULAR",
        "address": "ce4604a0000000000000000000000017",
        "sourceContext": {
          "indexToFilepath": {
            "0": "contracts/curve.sol",
            "1": "Context.sol",
            "2": "ERC20.sol",
            "3": "IERC20.sol",
            "4": "IERC20Metadata.sol",
            "5": "ReentrancyGuard.sol"
          },
          "sourceDir": ".post_autofinders.1"
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
      "value": 1004
    }
  ],
  "78": [
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
  "80": [
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
      "value": "ce4604a0000000000000000000000017"
    }
  ],
  "81": [
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
      "value": "ce4604a0000000000000000000000004"
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
        "begin": 4984,
        "len": 23,
        "jumpType": "REGULAR",
        "address": "ce4604a0000000000000000000000004",
        "sourceContext": {
          "indexToFilepath": {
            "0": "contracts/ERC20.sol",
            "1": "contracts/IERC20Metadata.sol",
            "2": "Context.sol",
            "3": "IERC20.sol"
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
      "value": 1017
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
      "value": 1018
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
        "address": "ce4604a0000000000000000000000004",
        "sourceContext": {
          "indexToFilepath": {
            "0": "contracts/ERC20.sol",
            "1": "contracts/IERC20Metadata.sol",
            "2": "Context.sol",
            "3": "IERC20.sol"
          },
          "sourceDir": ".post_autofinders.0"
        }
      }
    }
  ],
  "86": [
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
  "87": [
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
        "source": 0,
        "begin": 4816,
        "len": 18,
        "jumpType": "REGULAR",
        "address": "ce4604a0000000000000000000000004",
        "sourceContext": {
          "indexToFilepath": {
            "0": "contracts/ERC20.sol",
            "1": "contracts/IERC20Metadata.sol",
            "2": "Context.sol",
            "3": "IERC20.sol"
          },
          "sourceDir": ".post_autofinders.0"
        }
      }
    }
  ],
  "88": [
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
        "source": 0,
        "begin": 4816,
        "len": 18,
        "jumpType": "REGULAR",
        "address": "ce4604a0000000000000000000000004",
        "sourceContext": {
          "indexToFilepath": {
            "0": "contracts/ERC20.sol",
            "1": "contracts/IERC20Metadata.sol",
            "2": "Context.sol",
            "3": "IERC20.sol"
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
              "namePrefix": "R258",
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
                "namePrefix": "R258",
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
                "namePrefix": "CANON152",
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
                "namePrefix": "CANON151",
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
  "91": [
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
        "source": 6,
        "begin": 3060,
        "len": 23,
        "jumpType": "REGULAR",
        "address": "ce4604a0000000000000000000000017",
        "sourceContext": {
          "indexToFilepath": {
            "0": "contracts/curve.sol",
            "1": "Context.sol",
            "2": "ERC20.sol",
            "3": "IERC20.sol",
            "4": "IERC20Metadata.sol",
            "5": "ReentrancyGuard.sol"
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
      "value": 1016
    }
  ],
  "94": [
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
        "source": 6,
        "begin": 67,
        "len": 9,
        "jumpType": "REGULAR",
        "address": "ce4604a0000000000000000000000017",
        "sourceContext": {
          "indexToFilepath": {
            "0": "contracts/curve.sol",
            "1": "Context.sol",
            "2": "ERC20.sol",
            "3": "IERC20.sol",
            "4": "IERC20Metadata.sol",
            "5": "ReentrancyGuard.sol"
          },
          "sourceDir": ".post_autofinders.1"
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
      "value": 1001
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
        "source": 6,
        "begin": 907,
        "len": 88,
        "jumpType": "REGULAR",
        "address": "ce4604a0000000000000000000000017",
        "sourceContext": {
          "indexToFilepath": {
            "0": "contracts/curve.sol",
            "1": "Context.sol",
            "2": "ERC20.sol",
            "3": "IERC20.sol",
            "4": "IERC20Metadata.sol",
            "5": "ReentrancyGuard.sol"
          },
          "sourceDir": ".post_autofinders.1"
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
        "source": 6,
        "begin": 1833,
        "len": 20,
        "jumpType": "REGULAR",
        "address": "ce4604a0000000000000000000000017",
        "sourceContext": {
          "indexToFilepath": {
            "0": "contracts/curve.sol",
            "1": "Context.sol",
            "2": "ERC20.sol",
            "3": "IERC20.sol",
            "4": "IERC20Metadata.sol",
            "5": "ReentrancyGuard.sol"
          },
          "sourceDir": ".post_autofinders.1"
        }
      }
    }
  ],
  "99": [
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
  "100": [
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
        "source": 6,
        "begin": 2468,
        "len": 50,
        "jumpType": "REGULAR",
        "address": "ce4604a0000000000000000000000017",
        "sourceContext": {
          "indexToFilepath": {
            "0": "contracts/curve.sol",
            "1": "Context.sol",
            "2": "ERC20.sol",
            "3": "IERC20.sol",
            "4": "IERC20Metadata.sol",
            "5": "ReentrancyGuard.sol"
          },
          "sourceDir": ".post_autofinders.1"
        }
      }
    }
  ],
  "101": [
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
        "source": 0,
        "begin": 4143,
        "len": 5,
        "jumpType": "REGULAR",
        "address": "ce4604a0000000000000000000000017",
        "sourceContext": {
          "indexToFilepath": {
            "0": "contracts/curve.sol",
            "1": "Context.sol",
            "2": "ERC20.sol",
            "3": "IERC20.sol",
            "4": "IERC20Metadata.sol",
            "5": "ReentrancyGuard.sol"
          },
          "sourceDir": ".post_autofinders.1"
        }
      }
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
        "source": 0,
        "begin": 4135,
        "len": 5,
        "jumpType": "REGULAR",
        "address": "ce4604a0000000000000000000000017",
        "sourceContext": {
          "indexToFilepath": {
            "0": "contracts/curve.sol",
            "1": "Context.sol",
            "2": "ERC20.sol",
            "3": "IERC20.sol",
            "4": "IERC20Metadata.sol",
            "5": "ReentrancyGuard.sol"
          },
          "sourceDir": ".post_autofinders.1"
        }
      }
    }
  ],
  "103": [
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
      "value": "ce4604a0000000000000000000000014"
    }
  ],
  "104": [
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
      "value": "ce4604a0000000000000000000000014"
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
    }
  ],
  "106": [
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
        "source": 0,
        "begin": 6339,
        "len": 17,
        "jumpType": "REGULAR",
        "address": "ce4604a0000000000000000000000017",
        "sourceContext": {
          "indexToFilepath": {
            "0": "contracts/curve.sol",
            "1": "Context.sol",
            "2": "ERC20.sol",
            "3": "IERC20.sol",
            "4": "IERC20Metadata.sol",
            "5": "ReentrancyGuard.sol"
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
        "source": 0,
        "begin": 6315,
        "len": 21,
        "jumpType": "REGULAR",
        "address": "ce4604a0000000000000000000000017",
        "sourceContext": {
          "indexToFilepath": {
            "0": "contracts/curve.sol",
            "1": "Context.sol",
            "2": "ERC20.sol",
            "3": "IERC20.sol",
            "4": "IERC20Metadata.sol",
            "5": "ReentrancyGuard.sol"
          },
          "sourceDir": ".post_autofinders.1"
        }
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
        "name": "optimization.overflow.safe",
        "type": "tac.MetaMap$Companion$NothingValue",
        "erasureStrategy": "Canonical"
      },
      "value": {
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
        "source": 0,
        "begin": 6294,
        "len": 145,
        "jumpType": "REGULAR",
        "address": "ce4604a0000000000000000000000017",
        "sourceContext": {
          "indexToFilepath": {
            "0": "contracts/curve.sol",
            "1": "Context.sol",
            "2": "ERC20.sol",
            "3": "IERC20.sol",
            "4": "IERC20Metadata.sol",
            "5": "ReentrancyGuard.sol"
          },
          "sourceDir": ".post_autofinders.1"
        }
      }
    }
  ],
  "111": [
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
        "source": 0,
        "begin": 6421,
        "len": 17,
        "jumpType": "REGULAR",
        "address": "ce4604a0000000000000000000000017",
        "sourceContext": {
          "indexToFilepath": {
            "0": "contracts/curve.sol",
            "1": "Context.sol",
            "2": "ERC20.sol",
            "3": "IERC20.sol",
            "4": "IERC20Metadata.sol",
            "5": "ReentrancyGuard.sol"
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
        "source": 0,
        "begin": 6379,
        "len": 39,
        "jumpType": "REGULAR",
        "address": "ce4604a0000000000000000000000017",
        "sourceContext": {
          "indexToFilepath": {
            "0": "contracts/curve.sol",
            "1": "Context.sol",
            "2": "ERC20.sol",
            "3": "IERC20.sol",
            "4": "IERC20Metadata.sol",
            "5": "ReentrancyGuard.sol"
          },
          "sourceDir": ".post_autofinders.1"
        }
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
        "source": 6,
        "begin": 6816,
        "len": 37,
        "jumpType": "REGULAR",
        "address": "ce4604a0000000000000000000000017",
        "sourceContext": {
          "indexToFilepath": {
            "0": "contracts/curve.sol",
            "1": "Context.sol",
            "2": "ERC20.sol",
            "3": "IERC20.sol",
            "4": "IERC20Metadata.sol",
            "5": "ReentrancyGuard.sol"
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
        "source": 4,
        "begin": 4984,
        "len": 23,
        "jumpType": "REGULAR",
        "address": "ce4604a0000000000000000000000004",
        "sourceContext": {
          "indexToFilepath": {
            "0": "contracts/ERC20.sol",
            "1": "contracts/IERC20Metadata.sol",
            "2": "Context.sol",
            "3": "IERC20.sol"
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
        "source": 4,
        "begin": 2157,
        "len": 20,
        "jumpType": "REGULAR",
        "address": "ce4604a0000000000000000000000004",
        "sourceContext": {
          "indexToFilepath": {
            "0": "contracts/ERC20.sol",
            "1": "contracts/IERC20Metadata.sol",
            "2": "Context.sol",
            "3": "IERC20.sol"
          },
          "sourceDir": ".post_autofinders.0"
        }
      }
    }
  ],
  "117": [
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
  "118": [
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
        "source": 0,
        "begin": 4816,
        "len": 18,
        "jumpType": "REGULAR",
        "address": "ce4604a0000000000000000000000004",
        "sourceContext": {
          "indexToFilepath": {
            "0": "contracts/ERC20.sol",
            "1": "contracts/IERC20Metadata.sol",
            "2": "Context.sol",
            "3": "IERC20.sol"
          },
          "sourceDir": ".post_autofinders.0"
        }
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
        "source": 0,
        "begin": 4816,
        "len": 18,
        "jumpType": "REGULAR",
        "address": "ce4604a0000000000000000000000004",
        "sourceContext": {
          "indexToFilepath": {
            "0": "contracts/ERC20.sol",
            "1": "contracts/IERC20Metadata.sol",
            "2": "Context.sol",
            "3": "IERC20.sol"
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
  "120": [
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
              "namePrefix": "R401",
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
                "namePrefix": "R401",
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
                "namePrefix": "CANON152",
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
                "namePrefix": "CANON151",
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
  "121": [
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
        "source": 6,
        "begin": 3060,
        "len": 23,
        "jumpType": "REGULAR",
        "address": "ce4604a0000000000000000000000017",
        "sourceContext": {
          "indexToFilepath": {
            "0": "contracts/curve.sol",
            "1": "Context.sol",
            "2": "ERC20.sol",
            "3": "IERC20.sol",
            "4": "IERC20Metadata.sol",
            "5": "ReentrancyGuard.sol"
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
        "source": 6,
        "begin": 67,
        "len": 9,
        "jumpType": "REGULAR",
        "address": "ce4604a0000000000000000000000017",
        "sourceContext": {
          "indexToFilepath": {
            "0": "contracts/curve.sol",
            "1": "Context.sol",
            "2": "ERC20.sol",
            "3": "IERC20.sol",
            "4": "IERC20Metadata.sol",
            "5": "ReentrancyGuard.sol"
          },
          "sourceDir": ".post_autofinders.1"
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
        "source": 6,
        "begin": 907,
        "len": 88,
        "jumpType": "REGULAR",
        "address": "ce4604a0000000000000000000000017",
        "sourceContext": {
          "indexToFilepath": {
            "0": "contracts/curve.sol",
            "1": "Context.sol",
            "2": "ERC20.sol",
            "3": "IERC20.sol",
            "4": "IERC20Metadata.sol",
            "5": "ReentrancyGuard.sol"
          },
          "sourceDir": ".post_autofinders.1"
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
        "source": 6,
        "begin": 1833,
        "len": 20,
        "jumpType": "REGULAR",
        "address": "ce4604a0000000000000000000000017",
        "sourceContext": {
          "indexToFilepath": {
            "0": "contracts/curve.sol",
            "1": "Context.sol",
            "2": "ERC20.sol",
            "3": "IERC20.sol",
            "4": "IERC20Metadata.sol",
            "5": "ReentrancyGuard.sol"
          },
          "sourceDir": ".post_autofinders.1"
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
        "source": 6,
        "begin": 2468,
        "len": 50,
        "jumpType": "REGULAR",
        "address": "ce4604a0000000000000000000000017",
        "sourceContext": {
          "indexToFilepath": {
            "0": "contracts/curve.sol",
            "1": "Context.sol",
            "2": "ERC20.sol",
            "3": "IERC20.sol",
            "4": "IERC20Metadata.sol",
            "5": "ReentrancyGuard.sol"
          },
          "sourceDir": ".post_autofinders.1"
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
        "source": 0,
        "begin": 4143,
        "len": 5,
        "jumpType": "REGULAR",
        "address": "ce4604a0000000000000000000000017",
        "sourceContext": {
          "indexToFilepath": {
            "0": "contracts/curve.sol",
            "1": "Context.sol",
            "2": "ERC20.sol",
            "3": "IERC20.sol",
            "4": "IERC20Metadata.sol",
            "5": "ReentrancyGuard.sol"
          },
          "sourceDir": ".post_autofinders.1"
        }
      }
    }
  ],
  "128": [
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
        "source": 0,
        "begin": 4135,
        "len": 5,
        "jumpType": "REGULAR",
        "address": "ce4604a0000000000000000000000017",
        "sourceContext": {
          "indexToFilepath": {
            "0": "contracts/curve.sol",
            "1": "Context.sol",
            "2": "ERC20.sol",
            "3": "IERC20.sol",
            "4": "IERC20Metadata.sol",
            "5": "ReentrancyGuard.sol"
          },
          "sourceDir": ".post_autofinders.1"
        }
      }
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
        "source": 6,
        "begin": 9679,
        "len": 119,
        "jumpType": "REGULAR",
        "address": "ce4604a0000000000000000000000017",
        "sourceContext": {
          "indexToFilepath": {
            "0": "contracts/curve.sol",
            "1": "Context.sol",
            "2": "ERC20.sol",
            "3": "IERC20.sol",
            "4": "IERC20Metadata.sol",
            "5": "ReentrancyGuard.sol"
          },
          "sourceDir": ".post_autofinders.1"
        }
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
        "source": 6,
        "begin": 9525,
        "len": 13,
        "jumpType": "REGULAR",
        "address": "ce4604a0000000000000000000000017",
        "sourceContext": {
          "indexToFilepath": {
            "0": "contracts/curve.sol",
            "1": "Context.sol",
            "2": "ERC20.sol",
            "3": "IERC20.sol",
            "4": "IERC20Metadata.sol",
            "5": "ReentrancyGuard.sol"
          },
          "sourceDir": ".post_autofinders.1"
        }
      }
    }
  ],
  "131": [
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
  "132": [
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
        "source": 6,
        "begin": 9422,
        "len": 9,
        "jumpType": "REGULAR",
        "address": "ce4604a0000000000000000000000017",
        "sourceContext": {
          "indexToFilepath": {
            "0": "contracts/curve.sol",
            "1": "Context.sol",
            "2": "ERC20.sol",
            "3": "IERC20.sol",
            "4": "IERC20Metadata.sol",
            "5": "ReentrancyGuard.sol"
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
        "source": 0,
        "begin": 6787,
        "len": 29,
        "jumpType": "REGULAR",
        "address": "ce4604a0000000000000000000000017",
        "sourceContext": {
          "indexToFilepath": {
            "0": "contracts/curve.sol",
            "1": "Context.sol",
            "2": "ERC20.sol",
            "3": "IERC20.sol",
            "4": "IERC20Metadata.sol",
            "5": "ReentrancyGuard.sol"
          },
          "sourceDir": ".post_autofinders.1"
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
        "source": 6,
        "begin": 5461,
        "len": 13,
        "jumpType": "REGULAR",
        "address": "ce4604a0000000000000000000000017",
        "sourceContext": {
          "indexToFilepath": {
            "0": "contracts/curve.sol",
            "1": "Context.sol",
            "2": "ERC20.sol",
            "3": "IERC20.sol",
            "4": "IERC20Metadata.sol",
            "5": "ReentrancyGuard.sol"
          },
          "sourceDir": ".post_autofinders.1"
        }
      }
    }
  ],
  "135": [
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
        "source": 6,
        "begin": 4578,
        "len": 37,
        "jumpType": "REGULAR",
        "address": "ce4604a0000000000000000000000017",
        "sourceContext": {
          "indexToFilepath": {
            "0": "contracts/curve.sol",
            "1": "Context.sol",
            "2": "ERC20.sol",
            "3": "IERC20.sol",
            "4": "IERC20Metadata.sol",
            "5": "ReentrancyGuard.sol"
          },
          "sourceDir": ".post_autofinders.1"
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
        "source": 6,
        "begin": 3538,
        "len": 37,
        "jumpType": "REGULAR",
        "address": "ce4604a0000000000000000000000017",
        "sourceContext": {
          "indexToFilepath": {
            "0": "contracts/curve.sol",
            "1": "Context.sol",
            "2": "ERC20.sol",
            "3": "IERC20.sol",
            "4": "IERC20Metadata.sol",
            "5": "ReentrancyGuard.sol"
          },
          "sourceDir": ".post_autofinders.1"
        }
      }
    }
  ],
  "138": [
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
      "value": "ce4604a0000000000000000000000017"
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
        "source": 6,
        "begin": 9679,
        "len": 119,
        "jumpType": "REGULAR",
        "address": "ce4604a0000000000000000000000017",
        "sourceContext": {
          "indexToFilepath": {
            "0": "contracts/curve.sol",
            "1": "Context.sol",
            "2": "ERC20.sol",
            "3": "IERC20.sol",
            "4": "IERC20Metadata.sol",
            "5": "ReentrancyGuard.sol"
          },
          "sourceDir": ".post_autofinders.1"
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
        "source": 6,
        "begin": 9525,
        "len": 13,
        "jumpType": "REGULAR",
        "address": "ce4604a0000000000000000000000017",
        "sourceContext": {
          "indexToFilepath": {
            "0": "contracts/curve.sol",
            "1": "Context.sol",
            "2": "ERC20.sol",
            "3": "IERC20.sol",
            "4": "IERC20Metadata.sol",
            "5": "ReentrancyGuard.sol"
          },
          "sourceDir": ".post_autofinders.1"
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
        "source": 6,
        "begin": 9422,
        "len": 9,
        "jumpType": "REGULAR",
        "address": "ce4604a0000000000000000000000017",
        "sourceContext": {
          "indexToFilepath": {
            "0": "contracts/curve.sol",
            "1": "Context.sol",
            "2": "ERC20.sol",
            "3": "IERC20.sol",
            "4": "IERC20Metadata.sol",
            "5": "ReentrancyGuard.sol"
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
        "source": 0,
        "begin": 6787,
        "len": 29,
        "jumpType": "REGULAR",
        "address": "ce4604a0000000000000000000000017",
        "sourceContext": {
          "indexToFilepath": {
            "0": "contracts/curve.sol",
            "1": "Context.sol",
            "2": "ERC20.sol",
            "3": "IERC20.sol",
            "4": "IERC20Metadata.sol",
            "5": "ReentrancyGuard.sol"
          },
          "sourceDir": ".post_autofinders.1"
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
        "source": 6,
        "begin": 5461,
        "len": 13,
        "jumpType": "REGULAR",
        "address": "ce4604a0000000000000000000000017",
        "sourceContext": {
          "indexToFilepath": {
            "0": "contracts/curve.sol",
            "1": "Context.sol",
            "2": "ERC20.sol",
            "3": "IERC20.sol",
            "4": "IERC20Metadata.sol",
            "5": "ReentrancyGuard.sol"
          },
          "sourceDir": ".post_autofinders.1"
        }
      }
    }
  ],
  "144": [
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
        "source": 6,
        "begin": 4578,
        "len": 37,
        "jumpType": "REGULAR",
        "address": "ce4604a0000000000000000000000017",
        "sourceContext": {
          "indexToFilepath": {
            "0": "contracts/curve.sol",
            "1": "Context.sol",
            "2": "ERC20.sol",
            "3": "IERC20.sol",
            "4": "IERC20Metadata.sol",
            "5": "ReentrancyGuard.sol"
          },
          "sourceDir": ".post_autofinders.1"
        }
      }
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
        "source": 6,
        "begin": 3538,
        "len": 37,
        "jumpType": "REGULAR",
        "address": "ce4604a0000000000000000000000017",
        "sourceContext": {
          "indexToFilepath": {
            "0": "contracts/curve.sol",
            "1": "Context.sol",
            "2": "ERC20.sol",
            "3": "IERC20.sol",
            "4": "IERC20Metadata.sol",
            "5": "ReentrancyGuard.sol"
          },
          "sourceDir": ".post_autofinders.1"
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
        "source": 0,
        "begin": 6848,
        "len": 29,
        "jumpType": "REGULAR",
        "address": "ce4604a0000000000000000000000017",
        "sourceContext": {
          "indexToFilepath": {
            "0": "contracts/curve.sol",
            "1": "Context.sol",
            "2": "ERC20.sol",
            "3": "IERC20.sol",
            "4": "IERC20Metadata.sol",
            "5": "ReentrancyGuard.sol"
          },
          "sourceDir": ".post_autofinders.1"
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
      "value": 1010
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
        "source": 6,
        "begin": 8848,
        "len": 9,
        "jumpType": "REGULAR",
        "address": "ce4604a0000000000000000000000017",
        "sourceContext": {
          "indexToFilepath": {
            "0": "contracts/curve.sol",
            "1": "Context.sol",
            "2": "ERC20.sol",
            "3": "IERC20.sol",
            "4": "IERC20Metadata.sol",
            "5": "ReentrancyGuard.sol"
          },
          "sourceDir": ".post_autofinders.1"
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
        "source": 6,
        "begin": 9225,
        "len": 9,
        "jumpType": "REGULAR",
        "address": "ce4604a0000000000000000000000017",
        "sourceContext": {
          "indexToFilepath": {
            "0": "contracts/curve.sol",
            "1": "Context.sol",
            "2": "ERC20.sol",
            "3": "IERC20.sol",
            "4": "IERC20Metadata.sol",
            "5": "ReentrancyGuard.sol"
          },
          "sourceDir": ".post_autofinders.1"
        }
      }
    }
  ],
  "150": [
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
  "151": [
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
        "source": 0,
        "begin": 6848,
        "len": 29,
        "jumpType": "REGULAR",
        "address": "ce4604a0000000000000000000000017",
        "sourceContext": {
          "indexToFilepath": {
            "0": "contracts/curve.sol",
            "1": "Context.sol",
            "2": "ERC20.sol",
            "3": "IERC20.sol",
            "4": "IERC20Metadata.sol",
            "5": "ReentrancyGuard.sol"
          },
          "sourceDir": ".post_autofinders.1"
        }
      }
    }
  ],
  "152": [
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
        "source": 6,
        "begin": 8848,
        "len": 9,
        "jumpType": "REGULAR",
        "address": "ce4604a0000000000000000000000017",
        "sourceContext": {
          "indexToFilepath": {
            "0": "contracts/curve.sol",
            "1": "Context.sol",
            "2": "ERC20.sol",
            "3": "IERC20.sol",
            "4": "IERC20Metadata.sol",
            "5": "ReentrancyGuard.sol"
          },
          "sourceDir": ".post_autofinders.1"
        }
      }
    }
  ],
  "153": [
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
        "source": 6,
        "begin": 9225,
        "len": 9,
        "jumpType": "REGULAR",
        "address": "ce4604a0000000000000000000000017",
        "sourceContext": {
          "indexToFilepath": {
            "0": "contracts/curve.sol",
            "1": "Context.sol",
            "2": "ERC20.sol",
            "3": "IERC20.sol",
            "4": "IERC20Metadata.sol",
            "5": "ReentrancyGuard.sol"
          },
          "sourceDir": ".post_autofinders.1"
        }
      }
    }
  ],
  "154": [
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
      "value": "ce4604a0000000000000000000000017"
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
  "155": [
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
            "namePrefix": "I27",
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
            "namePrefix": "I507",
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
  "156": [
    {
      "key": {
        "name": "cvl",
        "type": "java.lang.Boolean",
        "erasureStrategy": "Canonical"
      },
      "value": true
    }
  ],
  "157": [
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
  "158": [
    {
      "key": {
        "name": "cvl.local",
        "type": "java.lang.Boolean",
        "erasureStrategy": "Canonical"
      },
      "value": false
    }
  ],
  "159": [
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
  "160": [
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
  "161": [
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
  "162": [
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
            "namePrefix": "I12",
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
            "namePrefix": "I522",
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
  "163": [
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
  "164": [
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
  "165": [
    {
      "key": {
        "name": "tac.meta",
        "type": "vc.data.TACMetaInfo",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "source": 6,
        "begin": 3898,
        "len": 23,
        "jumpType": "REGULAR",
        "address": "ce4604a0000000000000000000000017",
        "sourceContext": {
          "indexToFilepath": {
            "0": "contracts/curve.sol",
            "1": "Context.sol",
            "2": "ERC20.sol",
            "3": "IERC20.sol",
            "4": "IERC20Metadata.sol",
            "5": "ReentrancyGuard.sol"
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
  "166": [
    {
      "key": {
        "name": "tac.meta",
        "type": "vc.data.TACMetaInfo",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "source": 6,
        "begin": 1833,
        "len": 20,
        "jumpType": "REGULAR",
        "address": "ce4604a0000000000000000000000017",
        "sourceContext": {
          "indexToFilepath": {
            "0": "contracts/curve.sol",
            "1": "Context.sol",
            "2": "ERC20.sol",
            "3": "IERC20.sol",
            "4": "IERC20Metadata.sol",
            "5": "ReentrancyGuard.sol"
          },
          "sourceDir": ".post_autofinders.1"
        }
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
        "source": 0,
        "begin": 6339,
        "len": 17,
        "jumpType": "REGULAR",
        "address": "ce4604a0000000000000000000000017",
        "sourceContext": {
          "indexToFilepath": {
            "0": "contracts/curve.sol",
            "1": "Context.sol",
            "2": "ERC20.sol",
            "3": "IERC20.sol",
            "4": "IERC20Metadata.sol",
            "5": "ReentrancyGuard.sol"
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
        "name": "tac.meta",
        "type": "vc.data.TACMetaInfo",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "source": 0,
        "begin": 6315,
        "len": 21,
        "jumpType": "REGULAR",
        "address": "ce4604a0000000000000000000000017",
        "sourceContext": {
          "indexToFilepath": {
            "0": "contracts/curve.sol",
            "1": "Context.sol",
            "2": "ERC20.sol",
            "3": "IERC20.sol",
            "4": "IERC20Metadata.sol",
            "5": "ReentrancyGuard.sol"
          },
          "sourceDir": ".post_autofinders.1"
        }
      }
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
        "source": 6,
        "begin": 9422,
        "len": 9,
        "jumpType": "REGULAR",
        "address": "ce4604a0000000000000000000000017",
        "sourceContext": {
          "indexToFilepath": {
            "0": "contracts/curve.sol",
            "1": "Context.sol",
            "2": "ERC20.sol",
            "3": "IERC20.sol",
            "4": "IERC20Metadata.sol",
            "5": "ReentrancyGuard.sol"
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
  "170": [
    {
      "key": {
        "name": "tac.meta",
        "type": "vc.data.TACMetaInfo",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "source": 0,
        "begin": 6421,
        "len": 17,
        "jumpType": "REGULAR",
        "address": "ce4604a0000000000000000000000017",
        "sourceContext": {
          "indexToFilepath": {
            "0": "contracts/curve.sol",
            "1": "Context.sol",
            "2": "ERC20.sol",
            "3": "IERC20.sol",
            "4": "IERC20Metadata.sol",
            "5": "ReentrancyGuard.sol"
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
  "171": [
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
      "value": "ce4604a0000000000000000000000017"
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
  "172": [
    {
      "key": {
        "name": "tac.meta",
        "type": "vc.data.TACMetaInfo",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "source": 0,
        "begin": 6379,
        "len": 39,
        "jumpType": "REGULAR",
        "address": "ce4604a0000000000000000000000017",
        "sourceContext": {
          "indexToFilepath": {
            "0": "contracts/curve.sol",
            "1": "Context.sol",
            "2": "ERC20.sol",
            "3": "IERC20.sol",
            "4": "IERC20Metadata.sol",
            "5": "ReentrancyGuard.sol"
          },
          "sourceDir": ".post_autofinders.1"
        }
      }
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
        "source": 6,
        "begin": 6816,
        "len": 37,
        "jumpType": "REGULAR",
        "address": "ce4604a0000000000000000000000017",
        "sourceContext": {
          "indexToFilepath": {
            "0": "contracts/curve.sol",
            "1": "Context.sol",
            "2": "ERC20.sol",
            "3": "IERC20.sol",
            "4": "IERC20Metadata.sol",
            "5": "ReentrancyGuard.sol"
          },
          "sourceDir": ".post_autofinders.1"
        }
      }
    }
  ],
  "174": [
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
  "175": [
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
      "value": "ce4604a0000000000000000000000017"
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
        "source": 4,
        "begin": 4984,
        "len": 23,
        "jumpType": "REGULAR",
        "address": "ce4604a0000000000000000000000004",
        "sourceContext": {
          "indexToFilepath": {
            "0": "contracts/ERC20.sol",
            "1": "contracts/IERC20Metadata.sol",
            "2": "Context.sol",
            "3": "IERC20.sol"
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
  "177": [
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
        "address": "ce4604a0000000000000000000000004",
        "sourceContext": {
          "indexToFilepath": {
            "0": "contracts/ERC20.sol",
            "1": "contracts/IERC20Metadata.sol",
            "2": "Context.sol",
            "3": "IERC20.sol"
          },
          "sourceDir": ".post_autofinders.0"
        }
      }
    }
  ],
  "178": [
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
  "179": [
    {
      "key": {
        "name": "tac.meta",
        "type": "vc.data.TACMetaInfo",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "source": 0,
        "begin": 4816,
        "len": 18,
        "jumpType": "REGULAR",
        "address": "ce4604a0000000000000000000000004",
        "sourceContext": {
          "indexToFilepath": {
            "0": "contracts/ERC20.sol",
            "1": "contracts/IERC20Metadata.sol",
            "2": "Context.sol",
            "3": "IERC20.sol"
          },
          "sourceDir": ".post_autofinders.0"
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
        "source": 0,
        "begin": 4816,
        "len": 18,
        "jumpType": "REGULAR",
        "address": "ce4604a0000000000000000000000004",
        "sourceContext": {
          "indexToFilepath": {
            "0": "contracts/ERC20.sol",
            "1": "contracts/IERC20Metadata.sol",
            "2": "Context.sol",
            "3": "IERC20.sol"
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
  "181": [
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
              "namePrefix": "R640",
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
                "namePrefix": "R640",
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
                "namePrefix": "CANON152",
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
                "namePrefix": "CANON151",
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
  "182": [
    {
      "key": {
        "name": "tac.meta",
        "type": "vc.data.TACMetaInfo",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "source": 6,
        "begin": 9679,
        "len": 119,
        "jumpType": "REGULAR",
        "address": "ce4604a0000000000000000000000017",
        "sourceContext": {
          "indexToFilepath": {
            "0": "contracts/curve.sol",
            "1": "Context.sol",
            "2": "ERC20.sol",
            "3": "IERC20.sol",
            "4": "IERC20Metadata.sol",
            "5": "ReentrancyGuard.sol"
          },
          "sourceDir": ".post_autofinders.1"
        }
      }
    }
  ],
  "183": [
    {
      "key": {
        "name": "tac.meta",
        "type": "vc.data.TACMetaInfo",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "source": 6,
        "begin": 9525,
        "len": 13,
        "jumpType": "REGULAR",
        "address": "ce4604a0000000000000000000000017",
        "sourceContext": {
          "indexToFilepath": {
            "0": "contracts/curve.sol",
            "1": "Context.sol",
            "2": "ERC20.sol",
            "3": "IERC20.sol",
            "4": "IERC20Metadata.sol",
            "5": "ReentrancyGuard.sol"
          },
          "sourceDir": ".post_autofinders.1"
        }
      }
    }
  ]
}