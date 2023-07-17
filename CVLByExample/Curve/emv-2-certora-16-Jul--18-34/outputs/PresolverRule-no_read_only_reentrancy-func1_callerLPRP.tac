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
		B26:JSON{"name":"B26","paramSorts":[],"returnSort":{"#class":"tac.Tag.Bool"},"attribute":"Ghost","cvlResultType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"},"cvlParamTypes":[],"declarationName":"CANON37"}
		CANON105:JSON{"name":"CANON105","paramSorts":[],"returnSort":{"#class":"tac.Tag.Int"},"attribute":"Ghost","cvlResultType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256},"cvlParamTypes":[],"declarationName":"CANON105"}
		CANON109:JSON{"name":"CANON109","paramSorts":[],"returnSort":{"#class":"tac.Tag.Int"},"attribute":"Ghost","cvlResultType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256},"cvlParamTypes":[],"declarationName":"CANON109"}
		CANON37:JSON{"name":"CANON37","paramSorts":[],"returnSort":{"#class":"tac.Tag.Bool"},"attribute":"Ghost","cvlResultType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"},"cvlParamTypes":[],"declarationName":"CANON37"}
		CANON39:JSON{"name":"CANON39","paramSorts":[],"returnSort":{"#class":"tac.Tag.Int"},"attribute":"Ghost","cvlResultType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256},"cvlParamTypes":[],"declarationName":"CANON39"}
		I10:JSON{"name":"I10","paramSorts":[],"returnSort":{"#class":"tac.Tag.Int"},"attribute":"Ghost","cvlResultType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256},"cvlParamTypes":[],"declarationName":"CANON105"}
		I27:JSON{"name":"I27","paramSorts":[],"returnSort":{"#class":"tac.Tag.Int"},"attribute":"Ghost","cvlResultType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256},"cvlParamTypes":[],"declarationName":"CANON39"}
	}
	tacM0x40@1:bv256
	tacM0x40@5:bv256
	tacM0x40@9:bv256
	tacMCANON1!!11:bytemap
	tacMCANON1!!12:bytemap
	tacMCANON2!!13:bytemap
	tacMCANON2!!14:bytemap
	tacMCANON3!!15:bytemap
	tacMCANON3!!16:bytemap
	tacMCANON3!!17:bytemap
	tacNonce:wordmap
	tacMCANON5!!18:bytemap
	tacCaller@1:bv256
	tacCaller@5:bv256
	tacCaller@9:bv256
	tacMCANON2!!157:bytemap
	tacMCANON2!!159:bytemap
	tacMCANON2!!184:bytemap
	tacMCANON2!!218:bytemap
	tacMCANON2!!232:bytemap
	tacMCANON2!!300:bytemap
	tacMCANON2!!302:bytemap
	tacMCANON2!!327:bytemap
	tacMCANON2!!361:bytemap
	tacMCANON2!!375:bytemap
	tacMCANON2!!382:bytemap
	tacMCANON2!!384:bytemap
	tacMCANON2!!386:bytemap
	tacMCANON2!!388:bytemap
	tacMCANON2!!399:bytemap
	tacMCANON2!!401:bytemap
	tacMCANON2!!403:bytemap
	tacMCANON2!!405:bytemap
	tacMCANON2!!446:bytemap
	tacMCANON2!!456:bytemap
	tacCalldatabufCANON0@2:bv256
	tacCalldatabufCANON0@4:bv256
	tacCalldatabufCANON0@6:bv256
	tacCalldatabufCANON0@8:bv256
	tacCalldatabufCANON0@10:bv256
	tacCalldatabufCANON0@12:bv256
	tacCalldatabufCANON1@2:bv256
	tacCalldatabufCANON1@6:bv256
	tacCalldatabufCANON1@10:bv256
	tacMCANON6!!19:bytemap
	tacOrigNonceCANON0:wordmap
	tacOrigNonceCANON1:wordmap
	tacOrigNonceCANON2:wordmap
	tacOrigNonceCANON3:wordmap
	CANON87!!29:bv256
	tacOrigin!!107:bv256
	tacOrigin!!250:bv256
	tacOrigin!!487:bv256
	tacMCANON4havocme8877@5:bytemap
	tacCallvalue@1:bv256
	tacCallvalue@5:bv256
	tacCallvalue@9:bv256
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
	lastReverted@11:bool
	lastReverted@12:bool
	tacM0x0!!179:bv256
	tacM0x0!!322:bv256
	tacM0x0!!564:bv256
	tacExtcodesize!!9:wordmap
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
	tacCalldatasize@11:bv256
	tacCalldatasize@12:bv256
	tacReturndata@1:bytemap
	tacReturndata@5:bytemap
	tacReturndata@9:bytemap
	tacReturnsize@1:bv256
	tacReturnsize@5:bv256
	tacReturnsize@9:bv256
	tacCalldatasize!!233:bv256
	tacCalldatasize!!468:bv256
	tacMCANON3!!204:bytemap
	tacMCANON3!!206:bytemap
	tacMCANON3!!347:bytemap
	tacMCANON3!!349:bytemap
	tacMCANON3!!589:bytemap
	tacMCANON3!!591:bytemap
	CANON93!!30:wordmap
	tacCalldatabuf!!21@3:bytemap
	tacCalldatabuf!!22@7:bytemap
	tacCalldatabuf!!23@11:bytemap
	tacOrigSCANON100:bv256
	tacOrigSCANON101:bv256
	tacOrigSCANON102:bv256
	tacOrigSCANON103:bv256
	tacOrigSCANON104:bv256
	tacOrigSCANON105:bv256
	tacOrigSCANON106:bv256
	tacOrigSCANON107:bv256
	tacM0x0@2:bv256
	tacM0x0@6:bv256
	tacM0x0@10:bv256
	tacRC@1:bv256
	tacRC@5:bv256
	tacRC@9:bv256
	CANON99!!31:bv256
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
	CANON110@9:bool
	CANON111:bool
	CANON112:bool
	CANON115@2:bv256
	CANON115@3:bv256
	CANON115@4:bv256
	CANON115@5:bv256
	CANON115@6:bv256
	CANON115@7:bv256
	CANON115@8:bv256
	CANON115@10:bv256
	CANON115@11:bv256
	CANON115@12:bv256
	CANON116@1:bv256
	CANON116@9:bv256
	CANON117@1:bv256
	CANON117@9:bv256
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
	CANON131@9:bool
	CANON132@1:bool
	CANON132@9:bool
	CANON133@1:bool
	CANON133@9:bool
	CANON134@1:bv256
	CANON134@9:bv256
	CANON135:bool
	CANON136:int
	CANON137:int
	CANON138:int
	CANON139@1:bool
	CANON139@9:bool
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
	CANON188@5:bv256
	CANON189@5:bv256
	CANON190:int
	CANON191:int
	CANON192:bool
	CANON193:int
	CANON194:bool
	CANON195:bool
	CANON196:bool
	CANON197:bool
	CANON198:bool
	CANON199:bool
	CANON200:int
	CANON201:int
	CANON202:int
	CANON203@5:bool
	CANON204@5:bool
	CANON205@5:bool
	CANON206@5:bv256
	CANON207:bool
	CANON208:int
	CANON209:int
	CANON210:int
	CANON211@5:bool
	CANON212:int
	CANON213:int
	CANON214:int
	CANON215:int
	CANON216:int
	CANON217:int
	CANON218:bool
	CANON219:bool
	CANON220:int
	CANON221:bool
	CANON222:bv256
	CANON223:int
	CANON224:bool
	CANON225:bv256
	CANON226:int
	CANON227:bool
	CANON228:bv256
	CANON229:int
	CANON230:bool
	CANON231:bv256
	CANON232:int
	CANON233:bool
	CANON234:bv256
	CANON235:int
	CANON236:bool
	CANON237:bv256
	CANON238:int
	CANON239:bool
	CANON240:bv256
	CANON241:int
	CANON242:int
	CANON243:bool
	CANON244:int
	CANON245:bool
	CANON246:bool
	CANON247:int
	CANON248:int
	CANON249:bool
	CANON250:int
	CANON251:bool
	CANON252:bool
	CANON253:bool
	CANON254:bool
	CANON255:bool
	CANON256:bool
	CANON257:int
	CANON258:int
	CANON259:int
	CANON260:bool
	CANON261:int
	CANON262:int
	CANON263:int
	CANON264:int
	CANON265:bool
	CANON266:bool
	tacCalldatasize!!90:bv256
	tacMCANON0havocme8875@1:bytemap
	tacMCANON0havocme8876@9:bytemap
	tacMCANON0@1:bytemap
	tacMCANON0@9:bytemap
	tacMCANON1@1:bytemap
	tacMCANON1@9:bytemap
	tacMCANON2@1:bytemap
	tacMCANON2@9:bytemap
	tacMCANON3@3:bytemap
	tacMCANON3@7:bytemap
	tacMCANON3@11:bytemap
	tacMCANON4@5:bytemap
	tacMCANON5@5:bytemap
	tacMCANON6@5:bytemap
	tacBalance:wordmap
	tacTimestamp!!117:bv256
	tacTimestamp!!260:bv256
	tacTimestamp!!497:bv256
	tacBalance!!20:wordmap
	tacNumber@1:bv256
	tacNumber@5:bv256
	tacNumber@9:bv256
	tacCalldatabuf@1:bytemap
	tacCalldatabuf@3:bytemap
	tacCalldatabuf@5:bytemap
	tacCalldatabuf@7:bytemap
	tacCalldatabuf@9:bytemap
	tacCalldatabuf@11:bytemap
	B26:bool
	B47:bool
	B48:bool
	B49:bool
	B50:bool
	B51:bool
	B52:bool
	B53:bool
	B54:bool
	B55:bool
	B57:bool
	B59:bool
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
	B78:bool
	B79:bool
	B80:bool
	B81:bool
	B82:bool
	B83:bool
	B91:bool
	B92:bool
	B94:bool
	B97:bool
	B99:bool
	I10:int
	I27:int
	I84:int
	I85:int
	I86:int
	I87:int
	I88:int
	I89:int
	I93:int
	I98:int
	R32:bv256
	R33:bv256
	R34:bv256
	R56:bv256
	R58:bv256
	R60:bv256
	R95:bv256
	B102:bool
	B105:bool
	B108:bool
	B110:bool
	B113:bool
	B115:bool
	B118:bool
	B120:bool
	B123:bool
	B132:bool
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
	B148:bool
	B153:bool
	B154:bool
	B155:bool
	B164:bool
	B165:bool
	B167:bool
	B168:bool
	B169:bool
	B170:bool
	B171:bool
	B173:bool
	B174:bool
	B176:bool
	B177:bool
	B186:bool
	B187:bool
	B190:bool
	B191:bool
	B192:bool
	B193:bool
	B196:bool
	B197:bool
	B198:bool
	B199:bool
	B201:bool
	B202:bool
	B211:bool
	B220:bool
	B221:bool
	B223:bool
	B224:bool
	B225:bool
	B226:bool
	B227:bool
	B228:bool
	B234:bool
	B235:bool
	B237:bool
	B240:bool
	B242:bool
	B245:bool
	B248:bool
	B251:bool
	B253:bool
	B256:bool
	B258:bool
	B261:bool
	B263:bool
	B266:bool
	B275:bool
	B278:bool
	B279:bool
	B280:bool
	B281:bool
	B282:bool
	B283:bool
	B284:bool
	B285:bool
	B286:bool
	B287:bool
	B291:bool
	B296:bool
	B297:bool
	B298:bool
	B307:bool
	B308:bool
	B310:bool
	B311:bool
	B312:bool
	B313:bool
	B314:bool
	B316:bool
	B317:bool
	B319:bool
	B320:bool
	B329:bool
	B330:bool
	B333:bool
	B334:bool
	B335:bool
	B336:bool
	B339:bool
	B340:bool
	B341:bool
	B342:bool
	B344:bool
	B345:bool
	B354:bool
	B363:bool
	B364:bool
	B366:bool
	B367:bool
	B368:bool
	B369:bool
	B370:bool
	B371:bool
	B377:bool
	B394:bool
	B412:bool
	B414:bool
	B415:bool
	B417:bool
	B421:bool
	B427:bool
	B429:bool
	B430:bool
	B432:bool
	B436:bool
	B442:bool
	B443:bool
	B444:bool
	B452:bool
	B453:bool
	B454:bool
	B471:bool
	B472:bool
	B474:bool
	B477:bool
	B479:bool
	B482:bool
	B485:bool
	B488:bool
	B490:bool
	B493:bool
	B495:bool
	B498:bool
	B500:bool
	B503:bool
	B512:bool
	B515:bool
	B517:bool
	B518:bool
	B519:bool
	B520:bool
	B521:bool
	B522:bool
	B523:bool
	B527:bool
	B532:bool
	B533:bool
	B534:bool
	B549:bool
	B550:bool
	B552:bool
	B553:bool
	B554:bool
	B555:bool
	B556:bool
	B558:bool
	B559:bool
	B561:bool
	B562:bool
	B571:bool
	B572:bool
	B575:bool
	B576:bool
	B577:bool
	B578:bool
	B581:bool
	B582:bool
	B583:bool
	B584:bool
	B586:bool
	B587:bool
	B596:bool
	B605:bool
	B606:bool
	B608:bool
	B609:bool
	B610:bool
	B611:bool
	B612:bool
	B613:bool
	B619:bool
	B637:bool
	B639:bool
	B640:bool
	B642:bool
	B646:bool
	B652:bool
	B653:bool
	B654:bool
	I104:int
	I109:int
	I114:int
	I119:int
	I122:int
	I128:int
	I212:int
	I213:int
	I214:int
	I236:int
	I241:int
	I247:int
	I252:int
	I257:int
	I262:int
	I265:int
	I271:int
	I355:int
	I356:int
	I357:int
	I418:int
	I419:int
	I424:int
	I433:int
	I434:int
	I439:int
	I461:int
	I462:int
	I463:int
	I464:int
	I465:int
	I473:int
	I478:int
	I484:int
	I489:int
	I494:int
	I499:int
	I502:int
	I508:int
	I542:int
	I543:int
	I544:int
	I545:int
	I546:int
	I547:int
	I597:int
	I598:int
	I599:int
	I643:int
	I644:int
	M466:bytemap
	M469:bytemap
	R100:bv256
	R106:bv256
	R111:bv256
	R116:bv256
	R121:bv256
	R124:bv256
	R125:bv256
	R126:bv256
	R127:bv256
	R130:bv256
	R131:bv256
	R134:bv256
	R145:bv256
	R146:bv256
	R147:bv256
	R149:bv256
	R151:bv256
	R152:bv256
	R156:bv256
	R158:bv256
	R160:bv256
	R161:bv256
	R166:bv256
	R172:bv256
	R175:bv256
	R178:bv256
	R180:(uninterp) skey
	R181:bv256
	R182:bv256
	R189:bv256
	R194:bv256
	R195:bv256
	R200:bv256
	R203:bv256
	R205:bv256
	R207:bv256
	R208:bv256
	R209:bv256
	R210:bv256
	R215:bv256
	R216:bv256
	R222:bv256
	R229:bv256
	R230:bv256
	R238:bv256
	R243:bv256
	R249:bv256
	R254:bv256
	R259:bv256
	R264:bv256
	R267:bv256
	R268:bv256
	R269:bv256
	R270:bv256
	R273:bv256
	R274:bv256
	R277:bv256
	R288:bv256
	R289:bv256
	R290:bv256
	R292:bv256
	R294:bv256
	R295:bv256
	R299:bv256
	R301:bv256
	R303:bv256
	R304:bv256
	R309:bv256
	R315:bv256
	R318:bv256
	R321:bv256
	R323:(uninterp) skey
	R324:bv256
	R325:bv256
	R332:bv256
	R337:bv256
	R338:bv256
	R343:bv256
	R346:bv256
	R348:bv256
	R350:bv256
	R351:bv256
	R352:bv256
	R353:bv256
	R358:bv256
	R359:bv256
	R365:bv256
	R372:bv256
	R373:bv256
	R376:bv256
	R378:bv256
	R380:bv256
	R381:bv256
	R383:bv256
	R385:bv256
	R387:bv256
	R389:bv256
	R390:bv256
	R391:bv256
	R393:bv256
	R395:bv256
	R397:bv256
	R398:bv256
	R400:bv256
	R402:bv256
	R404:bv256
	R406:bv256
	R407:bv256
	R408:bv256
	R410:bv256
	R411:bv256
	R413:bv256
	R416:bv256
	R420:bv256
	R422:bv256
	R423:bv256
	R425:bv256
	R426:bv256
	R428:bv256
	R431:bv256
	R435:bv256
	R437:bv256
	R438:bv256
	R440:bv256
	R441:bv256
	R445:bv256
	R447:bv256
	R448:bv256
	R450:bv256
	R451:bv256
	R455:bv256
	R457:bv256
	R458:bv256
	R467:bv256
	R470:bv256
	R475:bv256
	R480:bv256
	R486:bv256
	R491:bv256
	R496:bv256
	R501:bv256
	R504:bv256
	R505:bv256
	R506:bv256
	R507:bv256
	R510:bv256
	R511:bv256
	R516:bv256
	R524:bv256
	R525:bv256
	R526:bv256
	R528:bv256
	R530:bv256
	R531:bv256
	R535:bv256
	R537:bv256
	R539:bv256
	R540:bv256
	R551:bv256
	R557:bv256
	R560:bv256
	R563:bv256
	R565:(uninterp) skey
	R566:bv256
	R567:bv256
	R574:bv256
	R579:bv256
	R580:bv256
	R585:bv256
	R588:bv256
	R590:bv256
	R592:bv256
	R593:bv256
	R594:bv256
	R595:bv256
	R600:bv256
	R601:bv256
	R607:bv256
	R614:bv256
	R615:bv256
	R618:bv256
	R620:bv256
	R622:bv256
	R623:bv256
	R625:bv256
	R627:bv256
	R629:bv256
	R631:bv256
	R632:bv256
	R633:bv256
	R635:bv256
	R636:bv256
	R638:bv256
	R641:bv256
	R645:bv256
	R647:bv256
	R648:bv256
	R649:bv256
	R650:bv256
	R651:bv256
	R655:bv256
	R657:bv256
	R658:bv256
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
	tacAddress@11:bv256
	tacAddress@12:bv256
	tacOrigBalanceCANON0:wordmap
	tacOrigBalanceCANON1:wordmap
	tacOrigBalanceCANON2:wordmap
	tacOrigBalanceCANON3:wordmap
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
	LCANON0@11:bv256
	LCANON0@12:bv256
	LCANON1@1:bool
	LCANON1@5:bool
	LCANON1@9:bool
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
	LCANON2@11:bool
	LCANON2@12:bool
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
	LCANON3@11:bool
	LCANON3@12:bool
	LCANON4@1:bool
	LCANON4@2:bool
	LCANON4@6:bool
	LCANON4@9:bool
	LCANON4@10:bool
	LCANON5@1:bool
	LCANON5@2:bool
	LCANON5@6:bool
	LCANON5@9:bool
	LCANON5@10:bool
	LCANON6@1:bool
	LCANON6@9:bool
	LCANON7@1:bool
	LCANON7@9:bool
	LCANON8@1:bool
	LCANON8@9:bool
	LCANON9@1:bool
	LCANON9@9:bool
	tacCallvalue!!101:bv256
	tacCallvalue!!244:bv256
	tacCallvalue!!481:bv256
	tacOrigin@1:bv256
	tacOrigin@5:bv256
	tacOrigin@9:bv256
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
	CANON75@11:bv256
	CANON75@12:bv256
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
	CANON76@11:bool
	CANON76@12:bool
	CANON77:wordmap
	CANON78@1:bool
	CANON78@9:bool
	CANON79@1:bool
	CANON79@9:bool
	CANON80@1:bool
	CANON80@9:bool
	CANON81@1:bv256
	CANON81@9:bv256
	CANON82@1:bv256
	CANON82@9:bv256
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
	CANON18!!24:bv256
	CANON19!!25:bv256
	LCANON10@1:bv256
	LCANON10@9:bv256
	LCANON11@1:bv256
	LCANON11@9:bv256
	LCANON12@1:bv256
	LCANON12@9:bv256
	LCANON13@1:bv256
	LCANON13@9:bv256
	LCANON14@1:bv256
	LCANON14@9:bv256
	LCANON15@1:bool
	LCANON15@9:bool
	LCANON16@1:bv256
	LCANON16@9:bv256
	LCANON17@1:bv256
	LCANON17@9:bv256
	LCANON18@1:bv256
	LCANON18@9:bv256
	LCANON19@1:bv256
	LCANON19@9:bv256
	LCANON20@1:bv256
	LCANON20@9:bv256
	LCANON21@1:bv256
	LCANON21@9:bv256
	LCANON22@1:bv256
	LCANON22@9:bv256
	LCANON23@1:bv256
	LCANON23@9:bv256
	LCANON24@2:bv256
	LCANON24@6:bv256
	LCANON24@10:bv256
	LCANON25@2:bool
	LCANON25@6:bool
	LCANON25@10:bool
	LCANON26@2:bv256
	LCANON26@6:bv256
	LCANON26@10:bv256
	LCANON27@2:bool
	LCANON27@6:bool
	LCANON27@10:bool
	LCANON28@2:bv256
	LCANON28@4:bv256
	LCANON28@6:bv256
	LCANON28@8:bv256
	LCANON28@10:bv256
	LCANON28@12:bv256
	LCANON29@2:bv256
	LCANON29@6:bv256
	LCANON29@10:bv256
	LCANON30@2:bv256
	LCANON30@6:bv256
	LCANON30@10:bv256
	LCANON31@2:bv256
	LCANON31@6:bv256
	LCANON31@10:bv256
	LCANON32@1:bool
	LCANON32@9:bool
	LCANON33@1:bv256
	LCANON33@9:bv256
	LCANON34@1:bv256
	LCANON34@9:bv256
	LCANON35@1:bv256
	LCANON35@9:bv256
	LCANON36@1:bool
	LCANON36@9:bool
	LCANON37@1:bv256
	LCANON37@9:bv256
	LCANON38@1:bool
	LCANON38@9:bool
	LCANON39@1:bv256
	LCANON39@9:bv256
	LCANON40@1:bv256
	LCANON40@9:bv256
	LCANON41@1:bv256
	LCANON41@9:bv256
	LCANON42@1:bv256
	LCANON42@9:bv256
	LCANON43@1:bv256
	LCANON43@9:bv256
	LCANON44@1:bv256
	LCANON44@9:bv256
	LCANON45@1:bv256
	LCANON45@9:bv256
	LCANON46@1:bv256
	LCANON46@9:bv256
	LCANON47@1:bv256
	LCANON47@9:bv256
	LCANON48@1:bv256
	LCANON48@9:bv256
	LCANON49@1:bv256
	LCANON49@9:bv256
	LCANON50@3:bool
	LCANON50@5:bool
	LCANON50@7:bool
	LCANON50@11:bool
	LCANON51@3:bv256
	LCANON51@7:bv256
	LCANON51@11:bv256
	LCANON52@3:bv256
	LCANON52@7:bv256
	LCANON52@11:bv256
	LCANON53@3:bool
	LCANON53@7:bool
	LCANON53@11:bool
	LCANON54@3:bool
	LCANON54@7:bool
	LCANON54@11:bool
	LCANON55@3:bv256
	LCANON55@7:bv256
	LCANON55@11:bv256
	LCANON56@3:bool
	LCANON56@7:bool
	LCANON56@11:bool
	LCANON57@3:bv256
	LCANON57@7:bv256
	LCANON57@11:bv256
	LCANON58@3:bool
	LCANON58@7:bool
	LCANON58@11:bool
	LCANON59@3:bool
	LCANON59@7:bool
	LCANON59@11:bool
	LCANON60@3:bv256
	LCANON60@7:bv256
	LCANON60@11:bv256
	LCANON61@3:bv256
	LCANON61@7:bv256
	LCANON61@11:bv256
	LCANON62@3:bv256
	LCANON62@7:bv256
	LCANON62@11:bv256
	LCANON63@3:bv256
	LCANON63@7:bv256
	LCANON63@11:bv256
	LCANON64@3:bv256
	LCANON64@7:bv256
	LCANON64@11:bv256
	LCANON65@3:bool
	LCANON65@7:bool
	LCANON65@11:bool
	LCANON66@3:bv256
	LCANON66@7:bv256
	LCANON66@11:bv256
	LCANON67@3:bv256
	LCANON67@7:bv256
	LCANON67@11:bv256
	LCANON68@1:bool
	LCANON68@9:bool
	LCANON69@1:bv256
	LCANON69@9:bv256
	LCANON70@1:bv256
	LCANON70@9:bv256
	LCANON71@1:bv256
	LCANON71@9:bv256
	LCANON72@1:bv256
	LCANON72@9:bv256
	LCANON73@1:bool
	LCANON73@9:bool
	LCANON74@1:bv256
	LCANON74@9:bv256
	LCANON75@1:bv256
	LCANON75@9:bv256
	LCANON76@1:bv256
	LCANON76@9:bv256
	LCANON77@1:bv256
	LCANON77@9:bv256
	LCANON78@1:bv256
	LCANON78@9:bv256
	LCANON79@1:bv256
	LCANON79@9:bv256
	LCANON80@1:bv256
	LCANON80@9:bv256
	LCANON81@4:bool
	LCANON81@5:bool
	LCANON81@8:bool
	LCANON81@12:bool
	LCANON82@4:bool
	LCANON82@8:bool
	LCANON82@12:bool
	LCANON83@4:bool
	LCANON83@8:bool
	LCANON83@12:bool
	LCANON84@4:bv256
	LCANON84@8:bv256
	LCANON84@12:bv256
	LCANON85@1:bv256
	LCANON85@9:bv256
	LCANON86@1:bv256
	LCANON86@9:bv256
	LCANON87@1:bv256
	LCANON87@9:bv256
	LCANON88@1:bv256
	LCANON88@9:bv256
	LCANON89@1:bool
	LCANON89@9:bool
	LCANON90@1:bv256
	LCANON90@9:bv256
	LCANON91@1:bool
	LCANON91@9:bool
	LCANON92@1:bool
	LCANON92@9:bool
	LCANON93@1:bv256
	LCANON93@9:bv256
	LCANON94@1:bv256
	LCANON94@9:bv256
	LCANON95@1:bool
	LCANON95@9:bool
	LCANON96@1:bv256
	LCANON96@9:bv256
	LCANON97@1:bv256
	LCANON97@9:bv256
	LCANON98@1:bv256
	LCANON98@9:bv256
	LCANON99@5:bool
	tacMCANON5!!529:bytemap
	tacMCANON5!!621:bytemap
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
	lastHasThrown@11:bool
	lastHasThrown@12:bool
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
	tacOrigSCANON81:wordmap
	tacOrigSCANON82:wordmap
	tacOrigSCANON83:wordmap
	tacOrigSCANON84:wordmap
	tacOrigSCANON85:wordmap
	tacOrigSCANON86:bv256
	tacOrigSCANON87:bv256
	tacOrigSCANON88:bv256
	tacOrigSCANON89:wordmap
	tacOrigSCANON90:wordmap
	tacOrigSCANON91:wordmap
	tacOrigSCANON92:wordmap
	tacOrigSCANON93:wordmap
	tacOrigSCANON94:bv256
	tacOrigSCANON95:bv256
	tacOrigSCANON96:bv256
	tacOrigSCANON97:wordmap
	tacOrigSCANON98:wordmap
	tacOrigSCANON99:bv256
	CANON141!!460:bool
	tacCaller!!96:bv256
	tacAddress!!103:bv256
	tacAddress!!163:bv256
	tacAddress!!185:bv256
	tacAddress!!219:bv256
	tacAddress!!246:bv256
	tacAddress!!306:bv256
	tacAddress!!328:bv256
	tacAddress!!362:bv256
	tacAddress!!483:bv256
	tacAddress!!548:bv256
	tacAddress!!570:bv256
	tacAddress!!604:bv256
	tacReturndata!!162:bytemap
	tacReturndata!!183:bytemap
	tacReturndata!!217:bytemap
	tacReturndata!!231:bytemap
	tacReturndata!!305:bytemap
	tacReturndata!!326:bytemap
	tacReturndata!!360:bytemap
	tacReturndata!!374:bytemap
	tacReturndata!!392:bytemap
	tacReturndata!!409:bytemap
	tacReturndata!!449:bytemap
	tacReturndata!!459:bytemap
	tacReturndata!!541:bytemap
	tacReturndata!!568:bytemap
	tacReturndata!!602:bytemap
	tacReturndata!!616:bytemap
	tacReturndata!!634:bytemap
	tacReturndata!!659:bytemap
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
	tacCalldatabuf!!188@3:bytemap
	tacCalldatabuf!!331@11:bytemap
	tacCalldatabuf!!573@7:bytemap
	tacSCANON0:wordmap
	tacSCANON1:wordmap
	tacSCANON2:wordmap
	tacCaller!!239:bv256
	tacCaller!!476:bv256
	tacCalldatasize!!0:bv256
	tacCalldatasize!!1:bv256
	tacCalldatasize!!2:bv256
	tacCalldatasize!!3:bv256
	tacCalldatasize!!4:bv256
	tacCalldatasize!!5:bv256
	tacCalldatasize!!6:bv256
	tacCalldatasize!!7:bv256
	tacCalldatasize!!8:bv256
	tacMCANON1!!150:bytemap
	tacMCANON1!!293:bytemap
	tacMCANON1!!379:bytemap
	tacMCANON1!!396:bytemap
	LCANON100@5:bv256
	LCANON101@5:bv256
	LCANON102@5:bv256
	LCANON103@5:bv256
	LCANON104@5:bv256
	LCANON105@5:bool
	LCANON106@5:bv256
	LCANON107@5:bv256
	LCANON108@5:bv256
	LCANON109@5:bv256
	LCANON110@5:bv256
	LCANON111@5:bv256
	LCANON112@5:bv256
	LCANON113@5:bv256
	LCANON114@5:bool
	LCANON115@5:bv256
	LCANON116@5:bv256
	LCANON117@5:bv256
	LCANON118@5:bool
	LCANON119@5:bv256
	LCANON120@5:bool
	LCANON121@5:bv256
	LCANON122@5:bv256
	LCANON123@5:bv256
	LCANON124@5:bv256
	LCANON125@5:bv256
	LCANON126@5:bv256
	LCANON127@5:bv256
	LCANON128@5:bv256
	LCANON129@5:bv256
	LCANON130@5:bv256
	LCANON131@5:bv256
	LCANON132@5:bool
	LCANON133@5:bv256
	LCANON134@5:bv256
	LCANON135@5:bv256
	LCANON136@5:bv256
	LCANON137@5:bool
	LCANON138@5:bv256
	LCANON139@5:bv256
	LCANON140@5:bv256
	LCANON141@5:bv256
	LCANON142@5:bv256
	LCANON143@5:bv256
	LCANON144@5:bv256
	LCANON145@5:bv256
	LCANON146@5:bv256
	LCANON147@5:bv256
	LCANON148@5:bv256
	LCANON149@5:bool
	LCANON150@5:bv256
	LCANON151@5:bool
	LCANON152@5:bool
	LCANON153@5:bv256
	LCANON154@5:bv256
	LCANON155@5:bool
	LCANON156@5:bv256
	LCANON157@5:bv256
	LCANON158@5:bv256
	LCANON159@5:bv256
	tacBalance!!129:wordmap
	tacBalance!!133:wordmap
	tacBalance!!272:wordmap
	tacBalance!!276:wordmap
	tacBalance!!509:wordmap
	tacBalance!!513:wordmap
	tacMCANON6!!536:bytemap
	tacMCANON6!!538:bytemap
	tacMCANON6!!569:bytemap
	tacMCANON6!!603:bytemap
	tacMCANON6!!617:bytemap
	tacMCANON6!!624:bytemap
	tacMCANON6!!626:bytemap
	tacMCANON6!!628:bytemap
	tacMCANON6!!630:bytemap
	tacMCANON6!!656:bytemap
	CANON77!!28:wordmap
	tacTimestamp@1:bv256
	tacTimestamp@5:bv256
	tacTimestamp@9:bv256
	tacSighash!!35:bv256
	tacSighash!!36:bv256
	tacSighash!!37:bv256
	tacSighash!!38:bv256
	tacSighash!!39:bv256
	tacSighash!!40:bv256
	tacSighash!!41:bv256
	tacSighash!!42:bv256
	tacSighash!!43:bv256
	tacSighash!!44:bv256
	tacSighash!!45:bv256
	tacSighash!!46:bv256
	CANON265!!514:bool
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
	tacSighash@11:bv256
	tacSighash@12:bv256
	tacNumber!!112:bv256
	tacNumber!!255:bv256
	tacNumber!!492:bv256
}
Program {
	Block 0_0_0_0_0_0 Succ [0_0_0_1_0_0] {
		AssignHavocCmd tacCalldatabufCANON0@2:0
		AssignHavocCmd tacCalldatabufCANON0@4:0
		AssignHavocCmd tacCalldatabufCANON0@6:1
		AssignHavocCmd tacCalldatabufCANON0@8:1
		AssignHavocCmd tacCalldatabufCANON0@10:2
		AssignHavocCmd tacCalldatabufCANON0@12:2
		AssignHavocCmd tacCalldatasize!!0:3
		AssignHavocCmd tacCalldatasize!!1:3
		AssignHavocCmd tacCalldatasize!!2:3
		AssignHavocCmd tacCalldatasize!!3:3
		AssignHavocCmd tacCalldatasize!!4:3
		AssignHavocCmd tacCalldatasize!!5:3
		AssignHavocCmd tacCalldatasize!!6:3
		AssignHavocCmd tacCalldatasize!!7:3
		AssignHavocCmd tacCalldatasize!!8:3
		AssignHavocCmd tacExtcodesize!!9:4
		AssignHavocCmd I10
		AssignHavocCmd CANON148:5
		AssignHavocCmd CANON150:6
		AssignExpCmd tacMCANON1!!11:7 ByteMapDefinition(i.8879:bv256 -> 0x0 )
		AssignExpCmd tacMCANON1!!12:8 ByteMapDefinition(i.8880:bv256 -> 0x0 )
		AssignExpCmd tacMCANON2!!13:9 ByteMapDefinition(i.8881:bv256 -> 0x0 )
		AssignExpCmd tacMCANON2!!14:10 ByteMapDefinition(i.8882:bv256 -> 0x0 )
		AssignExpCmd tacMCANON3!!15:11 ByteMapDefinition(i.8883:bv256 -> 0x0 )
		AssignExpCmd tacMCANON3!!16:12 ByteMapDefinition(i.8884:bv256 -> 0x0 )
		AssignExpCmd tacMCANON3!!17:13 ByteMapDefinition(i.8885:bv256 -> 0x0 )
		AssignExpCmd tacMCANON5!!18:14 ByteMapDefinition(i.8886:bv256 -> 0x0 )
		AssignExpCmd tacMCANON6!!19:15 ByteMapDefinition(i.8887:bv256 -> 0x0 )
		AssignHavocCmd tacBalance!!20:16
		AssignExpCmd tacCalldatabuf@1:17 ByteMapDefinition(i.8888:bv256 -> Ite(Lt(i.8888 tacCalldatasize@1:3 ) Unconstrained(bv256) 0x0 ) )
		AssignExpCmd tacCalldatabuf!!21@3:18 ByteMapDefinition(i.8889:bv256 -> Ite(Lt(i.8889 tacCalldatasize!!1:3 ) Unconstrained(bv256) 0x0 ) )
		AssignExpCmd tacCalldatabuf!!22@7:19 ByteMapDefinition(i.8890:bv256 -> Ite(Lt(i.8890 tacCalldatasize!!4:3 ) Unconstrained(bv256) 0x0 ) )
		AssignExpCmd tacCalldatabuf@9:20 ByteMapDefinition(i.8891:bv256 -> Ite(Lt(i.8891 tacCalldatasize@9:3 ) Unconstrained(bv256) 0x0 ) )
		AssignExpCmd tacCalldatabuf!!23@11:21 ByteMapDefinition(i.8892:bv256 -> Ite(Lt(i.8892 tacCalldatasize!!7:3 ) Unconstrained(bv256) 0x0 ) )
		AssignHavocCmd CANON18!!24:22
		AssignHavocCmd CANON19!!25:23
		AssignHavocCmd CANON20:24
		AssignHavocCmd CANON21:25
		AssignHavocCmd CANON22:26
		AssignHavocCmd CANON23:27
		AssignHavocCmd CANON24:28
		AssignHavocCmd CANON25:29
		AssignHavocCmd CANON26:30
		AssignHavocCmd CANON27:31
		AssignHavocCmd CANON28:32
		AssignHavocCmd CANON29:33
		AssignHavocCmd CANON30:34
		AssignHavocCmd CANON31:35
		AssignHavocCmd CANON32:36
		AssignHavocCmd CANON33:37
		AssignHavocCmd CANON34:38
		AssignHavocCmd CANON35:39
		AssignHavocCmd B26
		AssignHavocCmd I27
		AssignHavocCmd CANON77!!28:40
		AssignHavocCmd CANON87!!29:41
		AssignHavocCmd CANON93!!30:42
		AssignHavocCmd CANON99!!31:43
		AssignHavocCmd R32:44
		AssignHavocCmd R33:45
		AssignHavocCmd R34:46
		AssignHavocCmd tacSighash!!35:47
		AssignHavocCmd tacSighash!!36:47
		AssignHavocCmd tacSighash!!37:47
		AssignHavocCmd tacSighash!!38:47
		AssignHavocCmd tacSighash!!39:47
		AssignHavocCmd tacSighash!!40:47
		AssignHavocCmd tacSighash!!41:47
		AssignHavocCmd tacSighash!!42:47
		AssignHavocCmd tacSighash!!43:47
		AssignHavocCmd tacSighash!!44:47
		AssignHavocCmd tacSighash!!45:47
		AssignHavocCmd tacSighash!!46:47
		AssignExpCmd CANON0:48 0x421b78d9
		AssignExpCmd CANON1:49 false
		AssignExpCmd CANON2:50 false
		AssignExpCmd CANON3:51 false
		AssignExpCmd CANON4:52 0x0
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
		AssignExpCmd B47:54 Gt(Select(tacExtcodesize!!9:4 Apply(to_skey:bif R32:44) ) 0x0 )
		AssumeCmd B47:54
		AssignExpCmd B48:54 Gt(Select(tacExtcodesize!!9:4 Apply(to_skey:bif R33:45) ) 0x0 )
		AssumeCmd B48:54
		AssignExpCmd B49:54 Gt(Select(tacExtcodesize!!9:4 Apply(to_skey:bif R34:46) ) 0x0 )
		AssumeCmd B49:54
		AnnotationCmd JSON{"key":{"name":"cvl.label.end","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		AnnotationCmd JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Message","s":"assumptions about contracts' addresses"}}
		NopCmd
		AssumeExpCmd Gt(R32:44 0x0 )
		NopCmd
		AssumeExpCmd Le(R32:44 0xffffffffffffffffffffffffffffffffffffffff )
		NopCmd
		AssumeExpCmd Gt(R33:45 0x0 )
		NopCmd
		AssumeExpCmd Le(R33:45 0xffffffffffffffffffffffffffffffffffffffff )
		NopCmd
		AssumeExpCmd Gt(R34:46 0x0 )
		NopCmd
		AssumeExpCmd Le(R34:46 0xffffffffffffffffffffffffffffffffffffffff )
		AnnotationCmd JSON{"key":{"name":"cvl.label.end","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		AnnotationCmd JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Message","s":"assumptions about starting balances"}}
		AssignExpCmd R56:54 Select(tacBalance!!20:16 Apply(to_skey:bif R32:44) )
		NopCmd
		AssumeExpCmd Ge(R56:54 0x0 )
		AssignExpCmd R58:54 Select(tacBalance!!20:16 Apply(to_skey:bif R33:45) )
		NopCmd
		AssumeExpCmd Ge(R58:54 0x0 )
		AssignExpCmd R60:54 Select(tacBalance!!20:16 Apply(to_skey:bif R34:46) )
		NopCmd
		AssumeExpCmd Ge(R60:54 0x0 )
		AnnotationCmd JSON{"key":{"name":"cvl.label.end","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		AnnotationCmd JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Message","s":"assumptions about static addresses"}}
		AnnotationCmd JSON{"key":{"name":"cvl.label.end","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		AnnotationCmd JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Message","s":"assumptions about uniqueness of contracts' addressses"}}
		NopCmd
		AssumeExpCmd LNot(Eq(R32:44 R33:45 ) )
		NopCmd
		AssumeExpCmd LNot(Eq(R32:44 R34:46 ) )
		NopCmd
		AssumeExpCmd LNot(Eq(R33:45 R34:46 ) )
		AnnotationCmd JSON{"key":{"name":"cvl.label.end","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		NopCmd
		AssumeExpCmd Eq(CANON18!!24:22 R33:45 )
		NopCmd
		AssumeExpCmd Eq(CANON19!!25:23 R32:44 )
		AnnotationCmd JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Message","s":"record starting nonces"}}
		AnnotationCmd JSON{"key":{"name":"cvl.label.end","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		AnnotationCmd JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Message","s":"cloned contracts have no balances"}}
		AnnotationCmd JSON{"key":{"name":"cvl.label.end","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		AnnotationCmd JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Message","s":"Linked immutable setup"}}
		AnnotationCmd JSON{"key":{"name":"cvl.label.end","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		AnnotationCmd JSON{"key":{"name":"cvl.label.end","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		NopCmd
		AssumeExpCmd LAnd(Le(CANON20:24 0xffffffffffffffffffffffffffffffffffffffff ) Ge(CANON20:24 0x0 ) )
		NopCmd
		AssumeExpCmd LAnd(Le(CANON21:25 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff ) Ge(CANON21:25 0x0 ) )
		NopCmd
		AssumeExpCmd LAnd(Le(CANON22:26 0xffffffffffffffffffffffffffffffffffffffff ) Ge(CANON22:26 0x0 ) )
		NopCmd
		AssumeExpCmd LAnd(Le(CANON23:27 0xffffffffffffffffffffffffffffffffffffffff ) Ge(CANON23:27 0x0 ) )
		NopCmd
		AssumeExpCmd LAnd(Le(CANON24:28 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff ) Ge(CANON24:28 0x0 ) )
		NopCmd
		AssumeExpCmd LAnd(Le(CANON25:29 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff ) Ge(CANON25:29 0x0 ) )
		NopCmd
		AssumeExpCmd LAnd(Le(CANON26:30 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff ) Ge(CANON26:30 0x0 ) )
		NopCmd
		AssumeExpCmd LAnd(Le(CANON27:31 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff ) Ge(CANON27:31 0x0 ) )
		NopCmd
		AssumeExpCmd LAnd(Le(CANON28:32 0xffffffffffffffffffffffffffffffffffffffff ) Ge(CANON28:32 0x0 ) )
		NopCmd
		AssumeExpCmd LAnd(Le(CANON29:33 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff ) Ge(CANON29:33 0x0 ) )
		NopCmd
		AssumeExpCmd LAnd(Le(CANON30:34 0xffffffffffffffffffffffffffffffffffffffff ) Ge(CANON30:34 0x0 ) )
		NopCmd
		AssumeExpCmd LAnd(Le(CANON31:35 0xffffffffffffffffffffffffffffffffffffffff ) Ge(CANON31:35 0x0 ) )
		NopCmd
		AssumeExpCmd LAnd(Le(CANON32:36 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff ) Ge(CANON32:36 0x0 ) )
		NopCmd
		AssumeExpCmd LAnd(Le(CANON33:37 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff ) Ge(CANON33:37 0x0 ) )
		NopCmd
		AssumeExpCmd LAnd(Le(CANON34:38 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff ) Ge(CANON34:38 0x0 ) )
		NopCmd
		AssumeExpCmd LAnd(Le(CANON35:39 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff ) Ge(CANON35:39 0x0 ) )
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
		AnnotationCmd:56 JSON{"key":{"name":"call.trace.push","type":"analysis.icfg.Inliner$CallStack$PushRecord","erasureStrategy":"Canonical"},"value":"rO0ABXNyACphbmFseXNpcy5pY2ZnLklubGluZXIkQ2FsbFN0YWNrJFB1c2hSZWNvcmSX8+DCTLCH+AIAA0kACGNhbGxlZUlkTAAGY2FsbGVldAATTHZjL2RhdGEvTWV0aG9kUmVmO0wAB3N1bW1hcnl0ABVMdmMvZGF0YS9DYWxsU3VtbWFyeTt4cAAAAAFzcgARdmMuZGF0YS5NZXRob2RSZWbJlJTzzU9pGAIAA0wABGF0dHJ0ABdMc2NlbmUvTWV0aG9kQXR0cmlidXRlO0wACmNvbnRyYWN0SWR0ABZMamF2YS9tYXRoL0JpZ0ludGVnZXI7TAAHc2lnSGFzaHQAEExldm0vU2lnaGFzaEludDt4cHNyABxzY2VuZS5NZXRob2RBdHRyaWJ1dGUkQ29tbW9uNHjdebdr9XMCAAB4cgAVc2NlbmUuTWV0aG9kQXR0cmlidXRlcYg2pYWutuUCAAB4cHNyABRqYXZhLm1hdGguQmlnSW50ZWdlcoz8nx+pO/sdAwAGSQAIYml0Q291bnRJAAliaXRMZW5ndGhJABNmaXJzdE5vbnplcm9CeXRlTnVtSQAMbG93ZXN0U2V0Qml0SQAGc2lnbnVtWwAJbWFnbml0dWRldAACW0J4cgAQamF2YS5sYW5nLk51bWJlcoaslR0LlOCLAgAAeHD///////////////7////+AAAAAXVyAAJbQqzzF/gGCFTgAgAAeHAAAAAQzkYEoAAAAAAAAAAAAAAAKHhzcgAOZXZtLlNpZ2hhc2hJbnRUdcqNMXEgeAIAAUwAAW5xAH4ABnhwc3EAfgAM///////////////+/////gAAAAF1cQB+ABAAAAAE4lql+nhw"}
		AssignHavocCmd:56 tacCalldatasize!!90:3
		NopCmd
		AssumeExpCmd Apply(add_noofl:bif 0x4 0x0)
		NopCmd
		AssumeExpCmd Eq(0x4 tacCalldatasize!!90:3 )
		AssignExpCmd:56 B94 LAnd(Ge(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff CANON28:32 ) Le(0x0 CANON28:32 ) )
		AssertCmd:56 B94 "sanity bounds check on cvl to vm encoding of tacTmp!4760:int failed"
		AssignExpCmd:56 R95:54 Apply(safe_math_narrow:bif CANON28:32)
		NopCmd
		AssumeExpCmd LAnd(Le(R95:57 0xffffffffffffffffffffffffffffffffffffffff ) Ge(R95:57 0x0 ) )
		AssignExpCmd:56 B99 LAnd(Ge(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff CANON29:33 ) Le(0x0 CANON29:33 ) )
		AssertCmd:56 B99 "sanity bounds check on cvl to vm encoding of tacTmp!4763:int failed"
		AssignExpCmd:56 R100:54 Apply(safe_math_narrow:bif CANON29:33)
		NopCmd
		AssumeExpCmd LAnd(Le(R100:58 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff ) Ge(R100:58 0x0 ) )
		AssignExpCmd:56 B105 LAnd(Ge(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff CANON30:34 ) Le(0x0 CANON30:34 ) )
		AssertCmd:56 B105 "sanity bounds check on cvl to vm encoding of tacTmp!4767:int failed"
		AssignExpCmd:56 R106:54 Apply(safe_math_narrow:bif CANON30:34)
		NopCmd
		AssumeExpCmd LAnd(Le(R106:59 0xffffffffffffffffffffffffffffffffffffffff ) Ge(R106:59 0x0 ) )
		AssignExpCmd:56 B110 LAnd(Ge(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff CANON34:38 ) Le(0x0 CANON34:38 ) )
		AssertCmd:56 B110 "sanity bounds check on cvl to vm encoding of tacTmp!4770:int failed"
		AssignExpCmd:56 R111:54 Apply(safe_math_narrow:bif CANON34:38)
		NopCmd
		AssumeExpCmd LAnd(Le(R111:60 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff ) Ge(R111:60 0x0 ) )
		AssignExpCmd:56 B115 LAnd(Ge(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff CANON35:39 ) Le(0x0 CANON35:39 ) )
		AssertCmd:56 B115 "sanity bounds check on cvl to vm encoding of tacTmp!4773:int failed"
		AssignExpCmd:56 R116:54 Apply(safe_math_narrow:bif CANON35:39)
		NopCmd
		AssumeExpCmd LAnd(Le(R116:61 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff ) Ge(R116:61 0x0 ) )
		AssignExpCmd:56 B120 LAnd(Ge(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff CANON29:33 ) Le(0x0 CANON29:33 ) )
		AssertCmd:56 B120 "sanity bounds check on cvl to vm encoding of tacTmp!4776:int failed"
		AssignExpCmd:56 R121:54 Apply(safe_math_narrow:bif CANON29:33)
		AssignExpCmd:56 B123 LAnd(Ge(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff CANON28:32 ) Le(0x0 CANON28:32 ) )
		AssertCmd:56 B123 "sanity bounds check on cvl to vm encoding of tacTmp!4779:int failed"
		AssignExpCmd:56 R124:54 Apply(safe_math_narrow:bif CANON28:32)
		AssignExpCmd:56 R127:54 Select(tacBalance!!20:16 Apply(to_skey:bif R124:54) )
		AssignExpCmd:62 I128:54 IntSub(R127:54 R121:54 )
		AssignExpCmd:62 tacBalance!!129:16 Store(tacBalance!!20:16 Apply(to_skey:bif R124:54) I128:54 )
		AssignExpCmd:56 R130:54 Select(tacBalance!!129:16 Apply(to_skey:bif R34:46) )
		AssignExpCmd:62 R131:54 Add(R130:54 R121:54)
		NopCmd
		AssumeExpCmd Apply(add_noofl:bif R130:54 R121:54)
		AssignExpCmd:62 tacBalance!!133:16 Store(tacBalance!!129:16 Apply(to_skey:bif R34:46) R131:54 )
		AnnotationCmd:56 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.BalanceSnippet","srcAccountInfo":{"old":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R127","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}]},"new":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"I128","tag":{"#class":"tac.Tag.Int"},"callIndex":0,"meta":[{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}]},"addr":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R124","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}]}},"trgAccountInfo":{"old":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R130","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}]},"new":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R131","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}]},"addr":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R34","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"tacContractAt"},{"key":{"name":"tac.contract.sym.addr.name","type":"java.lang.String","erasureStrategy":"Erased"},"value":"curve"},{"key":{"name":"tac.contract.sym.addr","type":"java.math.BigInteger","erasureStrategy":"Erased"},"value":"ce4604a0000000000000000000000028"}]}},"transferredAmount":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R121","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}]}}}
		LabelCmd:56 "Start procedure curve-getVirtualPrice()"
		AnnotationCmd:56 JSON{"key":{"name":"fps.free-pointer-is-scalarized","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true}
		AssignExpCmd:56 R134:54 Select(tacExtcodesize!!9:4 Apply(to_skey:bif R34:63) )
		NopCmd
		AssumeExpCmd Gt(R134:54 0x0 )
		AnnotationCmd:56 JSON{"key":{"name":"internal.func.finder.info","type":"analysis.ip.InternalFunctionFinderReport","erasureStrategy":"Erased"},"value":"rO0ABXNyAChhbmFseXNpcy5pcC5JbnRlcm5hbEZ1bmN0aW9uRmluZGVyUmVwb3J0ian+bYn1VdACAAFMABN1bnJlc29sdmVkRnVuY3Rpb25zdAAPTGphdmEvdXRpbC9TZXQ7eHBzcgAhZGF0YXN0cnVjdHVyZXMuTGlua2VkQXJyYXlIYXNoU2V0AAAAAAAAAAEDAAJGAApsb2FkRmFjdG9yTAAJaGFzaFRhYmxldAAuTGRhdGFzdHJ1Y3R1cmVzL2FycmF5aGFzaHRhYmxlL0FycmF5SGFzaFRhYmxlO3hwdwgAAAAAQAAAAHg="}
		AnnotationCmd:56 JSON{"key":{"name":"fps.free-pointer-is-scalarized","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true}
		NopCmd
		AssumeExpCmd Eq(R100:54 0x0 )
		NopCmd
		AssumeExpCmd LNot(Lt(tacCalldatasize!!90:3 0x4 ) )
		NopCmd
		AssumeExpCmd LNot(Gt(0x82c63066 tacSighash!!35:47 ) )
		NopCmd
		AssumeExpCmd LNot(Eq(0x82c63066 tacSighash!!35:47 ) )
		NopCmd
		AssumeExpCmd LNot(Eq(0x89295a45 tacSighash!!35:47 ) )
		NopCmd
		AssumeExpCmd LNot(Eq(0x9d1e1f25 tacSighash!!35:47 ) )
		NopCmd
		AssumeExpCmd LNot(Eq(0xac8c9059 tacSighash!!35:47 ) )
		NopCmd
		AssumeExpCmd LNot(Eq(0xd802e4f7 tacSighash!!35:47 ) )
		NopCmd
		AssumeExpCmd Eq(0xe25aa5fa tacSighash!!35:47 )
		AnnotationCmd:56 JSON{"key":{"name":"internal.func.start","type":"analysis.ip.InternalFuncStartAnnotation","erasureStrategy":"CallTrace"},"value":{"id":0,"startPc":2909,"args":[],"methodSignature":{"#class":"spec.cvlast.QualifiedMethodSignature.QualifiedMethodSig","qualifiedMethodName":{"#class":"spec.cvlast.QualifiedFunction","host":{"name":"curve"},"methodId":"getVirtualPrice"},"params":[],"res":[{"#class":"spec.cvlast.VMParam.Unnamed","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256}}]},"stackOffsetToArgPos":{},"callSiteSrc":{"source":7,"begin":5992,"len":476,"jumpType":"ENTER","address":"ce4604a0000000000000000000000028","sourceContext":{"indexToFilepath":{"0":"contracts/Context.sol","1":"contracts/CurveToken.sol","2":"contracts/CurveTokenExample.sol","3":"contracts/ERC20.sol","4":"contracts/IERC20.sol","5":"contracts/IERC20Metadata.sol","6":"contracts/ReentrancyGuard.sol","7":"contracts/curve.sol"},"sourceDir":".post_autofinders.2"}}}}
		AnnotationCmd:56 JSON{"key":{"name":"pta.end-allocation","type":"analysis.alloc.AllocationAnalysis$AbstractLocation","erasureStrategy":"Erased"},"value":{"prevFPWriteIdx":0,"nextFPWriteCmd":{"block":{"#class":"tac.BlockIdentifier","origStartPc":16,"stkTop":1024,"decompCopy":0,"calleeIdx":0,"topOfStackValue":2,"freshCopy":0},"pos":34},"sort":{"#class":"analysis.alloc.AllocationAnalysis.Alloc.ConstBlock","sz":"40"}}}
		AssignExpCmd:64 R146:65 Select(CANON77!!28:40 Apply(skey_basic:bif 0x8) )
		AnnotationCmd:56 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet","value":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R146","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1012}]},"displayPath":{"#class":"analysis.storage.DisplayPath.ArrayAccess","index":{"#class":"vc.data.TACSymbol.Const","value":"0"},"base":{"#class":"analysis.storage.DisplayPath.Root","name":"admin_balances"}},"storageType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256},"contractInstance":"ce4604a0000000000000000000000028","linkableStorageReadId":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet.None"}}}
		AssignExpCmd:66 R147:67 Select(tacBalance!!133:16 Apply(to_skey:bif R34:63) )
		NopCmd
		AssumeExpCmd LNot(Lt(R147:67 R146:65 ) )
		AssignExpCmd:68 R149:69 Sub(R147:67 R146:65 )
		AssignExpCmd:70 tacMCANON1!!150:7 Store(tacMCANON1!!11:7 0xc0 R149:69 )
		AssignExpCmd:71 R151:72 Select(CANON77!!28:40 Apply(skey_basic:bif 0x9) )
		AnnotationCmd:56 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet","value":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R151","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1013}]},"displayPath":{"#class":"analysis.storage.DisplayPath.ArrayAccess","index":{"#class":"vc.data.TACSymbol.Const","value":"1"},"base":{"#class":"analysis.storage.DisplayPath.Root","name":"admin_balances"}},"storageType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256},"contractInstance":"ce4604a0000000000000000000000028","linkableStorageReadId":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet.None"}}}
		AssignExpCmd:56 B153:54 Le(CANON18!!24:73 0xffffffffffffffffffffffffffffffffffffffff )
		AssignExpCmd:56 B154:54 Ge(CANON18!!24:73 0x0 )
		NopCmd
		AssumeExpCmd LAnd(B153:54 B154:54 )
		AnnotationCmd:56 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet","value":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"CANON18!!24","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.scalarization.sort","type":"vc.data.ScalarizationSort","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.ScalarizationSort.Packed","packedStart":{"#class":"vc.data.ScalarizationSort.Split","idx":"b"},"start":0}},{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.storage.bit-width","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":160},{"key":{"name":"tac.storage.pretty.paths","type":"analysis.storage.DisplayPaths","erasureStrategy":"Erased"},"value":{"paths":[{"#class":"analysis.storage.DisplayPath.Root","name":"coins_1"}]}},{"key":{"name":"tac.slot.type","type":"spec.cvlast.typedescriptors.EVMTypeDescriptor$EVMValueType","erasureStrategy":"Canonical"},"value":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.address"}},{"key":{"name":"tac.storage.non-indexed-path","type":"analysis.storage.StorageAnalysisResult$NonIndexedPath","erasureStrategy":"Canonical"},"value":{"#class":"analysis.storage.StorageAnalysisResult.NonIndexedPath.Root","slot":"b"}},{"key":{"name":"tac.storage","type":"java.math.BigInteger","erasureStrategy":"Canonical"},"value":"ce4604a0000000000000000000000028"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1011}]},"displayPath":{"#class":"analysis.storage.DisplayPath.Root","name":"coins_1"},"storageType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.address"},"contractInstance":"ce4604a0000000000000000000000028","linkableStorageReadId":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet.Id","id":0}}}
		AnnotationCmd:56 JSON{"key":{"name":"init.reorder.fence","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		AssignExpCmd:74 tacMCANON2!!157:9 Store(tacMCANON2!!13:9 0x100 0x70a0823100000000000000000000000000000000000000000000000000000000 )
		AssignExpCmd:75 tacMCANON2!!159:9 Store(tacMCANON2!!157:9 0x104 R34:46 )
		AssignExpCmd:74 R160:76 0x100
		AssignHavocCmd:74 R161:77
		AssignHavocCmd:56 tacReturndata!!162:78
		JumpCmd:56 0_0_0_2_0_0
	}
	Block 0_0_0_2_0_0 Succ [1_0_0_1_0_0] {
		AnnotationCmd:56 JSON{"key":{"name":"call.trace.push","type":"analysis.icfg.Inliner$CallStack$PushRecord","erasureStrategy":"Canonical"},"value":"rO0ABXNyACphbmFseXNpcy5pY2ZnLklubGluZXIkQ2FsbFN0YWNrJFB1c2hSZWNvcmSX8+DCTLCH+AIAA0kACGNhbGxlZUlkTAAGY2FsbGVldAATTHZjL2RhdGEvTWV0aG9kUmVmO0wAB3N1bW1hcnl0ABVMdmMvZGF0YS9DYWxsU3VtbWFyeTt4cAAAAAJzcgARdmMuZGF0YS5NZXRob2RSZWbJlJTzzU9pGAIAA0wABGF0dHJ0ABdMc2NlbmUvTWV0aG9kQXR0cmlidXRlO0wACmNvbnRyYWN0SWR0ABZMamF2YS9tYXRoL0JpZ0ludGVnZXI7TAAHc2lnSGFzaHQAEExldm0vU2lnaGFzaEludDt4cHNyABxzY2VuZS5NZXRob2RBdHRyaWJ1dGUkQ29tbW9uNHjdebdr9XMCAAB4cgAVc2NlbmUuTWV0aG9kQXR0cmlidXRlcYg2pYWutuUCAAB4cHNyABRqYXZhLm1hdGguQmlnSW50ZWdlcoz8nx+pO/sdAwAGSQAIYml0Q291bnRJAAliaXRMZW5ndGhJABNmaXJzdE5vbnplcm9CeXRlTnVtSQAMbG93ZXN0U2V0Qml0SQAGc2lnbnVtWwAJbWFnbml0dWRldAACW0J4cgAQamF2YS5sYW5nLk51bWJlcoaslR0LlOCLAgAAeHD///////////////7////+AAAAAXVyAAJbQqzzF/gGCFTgAgAAeHAAAAAQzkYEoAAAAAAAAAAAAAAAEXhzcgAOZXZtLlNpZ2hhc2hJbnRUdcqNMXEgeAIAAUwAAW5xAH4ABnhwc3EAfgAM///////////////+/////gAAAAF1cQB+ABAAAAAEcKCCMXhzcgATdmMuZGF0YS5DYWxsU3VtbWFyeZQcmw5vl+FdAgAQSQAJc3VtbWFyeUlkTAAOY2FsbENvbnZlbnRpb250ACZMaW5zdHJ1bWVudGF0aW9uL2NhbGxzL0NhbGxDb252ZW50aW9uO0wACmNhbGxUYXJnZXR0ABpMYW5hbHlzaXMvaWNmZy9DYWxsVGFyZ2V0O0wACGNhbGxUeXBldAAVTHZjL2RhdGEvVEFDQ2FsbFR5cGU7TAAPY2Fubm90QmVJbmxpbmVkdAAtTGFuYWx5c2lzL2ljZmcvSW5saW5lciRJbGxlZ2FsSW5saW5pbmdSZWFzb247TAAGZ2FzVmFydAATTHZjL2RhdGEvVEFDU3ltYm9sO0wABmluQmFzZXEAfgAbTAAIaW5PZmZzZXRxAH4AG0wABmluU2l6ZXEAfgAbTAAMb3JpZ0NhbGxjb3JldAAgTHZjL2RhdGEvVEFDQ21kJFNpbXBsZSRDYWxsQ29yZTtMAAdvdXRCYXNlcQB+ABtMAAlvdXRPZmZzZXRxAH4AG0wAB291dFNpemVxAH4AG0wADXNpZ1Jlc29sdXRpb250AA9MamF2YS91dGlsL1NldDtMAAV0b1ZhcnEAfgAbTAAIdmFsdWVWYXJxAH4AG3hwAAAAAHNyACRpbnN0cnVtZW50YXRpb24uY2FsbHMuQ2FsbENvbnZlbnRpb25HtO1ulL788QIAA0kACGNhbGxlcklkTAAFaW5wdXR0ABlMYW5hbHlzaXMvaWNmZy9DYWxsSW5wdXQ7TAAGcmF3T3V0dAAiTGluc3RydW1lbnRhdGlvbi9jYWxscy9DYWxsT3V0cHV0O3hwAAAAAHNyABdhbmFseXNpcy5pY2ZnLkNhbGxJbnB1dJjJD1MhNUxQAgAHTAAHYmFzZVZhcnQAGUx2Yy9kYXRhL1RBQ0V4cHIkU3ltJFZhcjtMABBlbmNvZGVkQXJndW1lbnRzdAAjTGFuYWx5c2lzL2ljZmcvQUJJQXJndW1lbnRFbmNvZGluZztMABNpbnB1dFNpemVMb3dlckJvdW5kcQB+AAZMAAZvZmZzZXR0ABVMdmMvZGF0YS9UQUNFeHByJFN5bTtMABRyYW5nZVRvRGVjb21wb3NlZEFyZ3QAD0xqYXZhL3V0aWwvTWFwO0wAEHNpbXBsaWZpZWRPZmZzZXR0ABtMdmMvZGF0YS9UQUNFeHByJFN5bSRDb25zdDtMAARzaXplcQB+ACZ4cHNyABd2Yy5kYXRhLlRBQ0V4cHIkU3ltJFZhcskrg43eGgPnAgACTAABc3QAF0x2Yy9kYXRhL1RBQ1N5bWJvbCRWYXI7TAADdGFndAAJTHRhYy9UYWc7eHIAE3ZjLmRhdGEuVEFDRXhwciRTeW2iVj0S4YSNUAIAAHhyAA92Yy5kYXRhLlRBQ0V4cHJYhGlUu/v+yAIAAHhwc3IANnZjLmRhdGEuVEFDU3ltYm9sJFZhciRXaXRoRGVmYXVsdENhbGxJbmRleCRXaXRoQnl0ZU1hcJ7+oHF4CHAAAgACTAAEbWV0YXQALUxrb3RsaW54L2NvbGxlY3Rpb25zL2ltbXV0YWJsZS9QZXJzaXN0ZW50TWFwO0wACm5hbWVQcmVmaXh0ABJMamF2YS9sYW5nL1N0cmluZzt4cgAVdmMuZGF0YS5UQUNTeW1ib2wkVmFyCYrCGVl9SXYCAAB4cgARdmMuZGF0YS5UQUNTeW1ib2zd3Run/CoWswIAAHhwc3IAJmRhdGFzdHJ1Y3R1cmVzLnRyZWFwLkhhc2hUcmVhcE1hcCROb2Rlf2t9acJIPnQCAANMAANrZXl0ABJMamF2YS9sYW5nL09iamVjdDtMAARuZXh0dAA1TGRhdGFzdHJ1Y3R1cmVzL3RyZWFwL0hhc2hUcmVhcE1hcCRNb3JlS2V5VmFsdWVQYWlycztMAAV2YWx1ZXEAfgA3eHIAIWRhdGFzdHJ1Y3R1cmVzLnRyZWFwLkhhc2hUcmVhcE1hcPMJ/2vt3boKAgAAeHIAHWRhdGFzdHJ1Y3R1cmVzLnRyZWFwLlRyZWFwTWFw46LAyn3v5moCAAB4cgAaZGF0YXN0cnVjdHVyZXMudHJlYXAuVHJlYXA88f21zZwbdQIAAkwABGxlZnR0ABxMZGF0YXN0cnVjdHVyZXMvdHJlYXAvVHJlYXA7TAAFcmlnaHRxAH4APHhwcHNxAH4ANnBzcQB+ADZwcHNyAAt0YWMuTWV0YUtleVF/W3MiCfIZAgADTAAPZXJhc3VyZVN0cmF0ZWd5dAAdTHRhYy9NZXRhS2V5JEVyYXN1cmVTdHJhdGVneTtMAARuYW1lcQB+ADJMAAN0eXB0ABFMamF2YS9sYW5nL0NsYXNzO3hwfnIAG3RhYy5NZXRhS2V5JEVyYXN1cmVTdHJhdGVneQAAAAAAAAAAEgAAeHIADmphdmEubGFuZy5FbnVtAAAAAAAAAAASAAB4cHQACUNhbm9uaWNhbHQAF3RhYy5tZW1vcnkucGFydGl0aW9uLWlkdnIAEWphdmEubGFuZy5JbnRlZ2VyEuKgpPeBhzgCAAFJAAV2YWx1ZXhxAH4ADnBzcQB+AEkAAAACc3EAfgBAcQB+AEZ0ABJUYWMuc3ltYm9sLmtleXdvcmR2cgAQamF2YS5sYW5nLlN0cmluZ6DwpDh6O7NCAgAAeHBwdAAEdGFjTXNxAH4AQHEAfgBGdAANdGFjLmlzLm1lbW9yeXZyACJ0YWMuTWV0YU1hcCRDb21wYW5pb24kTm90aGluZ1ZhbHVl8nsHH85ykpUCAAB4cHBzcQB+AFN0AA90YWNNQ0FOT04yISExNTlzcgAPdGFjLlRhZyRCeXRlTWFwNb/Ry6GDRgkCAAB4cgALdGFjLlRhZyRNYXABJytzDV3P/QIAAHhyAAd0YWMuVGFnLk9V3gn2xngCAAB4cHBzcQB+AAz///////////////7////+AAAAAXVxAH4AEAAAAAEkeHNxAH4AKnNyADV2Yy5kYXRhLlRBQ1N5bWJvbCRWYXIkV2l0aERlZmF1bHRDYWxsSW5kZXgkV2l0aEJpdDI1NnqsyEgq0drPAgACTAAEbWV0YXEAfgAxTAAKbmFtZVByZWZpeHEAfgAyeHEAfgAzc3EAfgA2c3EAfgA2cHBxAH4ATHB0AAFMcHNxAH4AQHEAfgBGdAAQdGFjLnN0YWNrLmhlaWdodHEAfgBKcHNxAH4ASQAAA/B0AARSMTYwc3IADnRhYy5UYWckQml0MjU2IyLQT+LlKkgCAAB4cQB+AFlzcgARamF2YS51dGlsLkhhc2hNYXAFB9rBwxZg0QMAAkYACmxvYWRGYWN0b3JJAAl0aHJlc2hvbGR4cD9AAAAAAAADdwgAAAAEAAAAAnNyAB5hbmFseXNpcy5pY2ZnLlNjcmF0Y2hCeXRlUmFuZ2XBTLaPpUzj2gIAAkwABGZyb21xAH4ABkwAAnRvcQB+AAZ4cHNxAH4ADP///////////////v////4AAAAAdXEAfgAQAAAAAHhzcQB+AAz///////////////7////+AAAAAXVxAH4AEAAAAAEDeHNyAC1hbmFseXNpcy5pY2ZnLkRlY29tcG9zZWRDYWxsSW5wdXRBcmckQ29uc3RhbnSFavLdQafqPQIAA0wAAWN0ABlMdmMvZGF0YS9UQUNTeW1ib2wkQ29uc3Q7TAARY29udHJhY3RSZWZlcmVuY2V0AC9MYW5hbHlzaXMvaWNmZy9DYWxsR3JhcGhCdWlsZGVyJENhbGxlZENvbnRyYWN0O0wADHNjcmF0Y2hSYW5nZXQAIExhbmFseXNpcy9pY2ZnL1NjcmF0Y2hCeXRlUmFuZ2U7eHIAJGFuYWx5c2lzLmljZmcuRGVjb21wb3NlZENhbGxJbnB1dEFyZ82Nwhnirh8hAgAAeHBzcgAXdmMuZGF0YS5UQUNTeW1ib2wkQ29uc3QmHp5/l8IUcAIAAkwAA3RhZ3EAfgAsTAAFdmFsdWVxAH4ABnhxAH4ANHEAfgBoc3EAfgAM///////////////+/////gAAAAF1cQB+ABAAAAAgcKCCMQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAB4cHEAfgBsc3EAfgBrc3EAfgAM///////////////+/////gAAAAF1cQB+ABAAAAABBHhzcQB+AAz///////////////7////+AAAAAXVxAH4AEAAAAAEjeHNyAC1hbmFseXNpcy5pY2ZnLkRlY29tcG9zZWRDYWxsSW5wdXRBcmckVmFyaWFibGWV3y80jneopQIAA0wAEWNvbnRyYWN0UmVmZXJlbmNlcQB+AHNMAAxzY3JhdGNoUmFuZ2VxAH4AdEwAAXZxAH4AK3hxAH4AdXNyAERhbmFseXNpcy5pY2ZnLkNhbGxHcmFwaEJ1aWxkZXIkQ2FsbGVkQ29udHJhY3QkRnVsbHlSZXNvbHZlZCRTZWxmTGlua++8l8Aq7q6zAgABTAAKY29udHJhY3RJZHEAfgAGeHIAO2FuYWx5c2lzLmljZmcuQ2FsbEdyYXBoQnVpbGRlciRDYWxsZWRDb250cmFjdCRGdWxseVJlc29sdmVkotnIkxMAs6QCAAB4cgAtYW5hbHlzaXMuaWNmZy5DYWxsR3JhcGhCdWlsZGVyJENhbGxlZENvbnRyYWN00wt1rN/LodcCAAB4cHNxAH4ADP///////////////v////4AAAABdXEAfgAQAAAAEM5GBKAAAAAAAAAAAAAAACh4cQB+AHtzcQB+AF5zcQB+ADZwc3EAfgA2c3EAfgA2c3EAfgA2cHBxAH4ATHB0AA10YWNDb250cmFjdEF0cHNxAH4AQH5xAH4ARHQABkVyYXNlZHQAGnRhYy5jb250cmFjdC5zeW0uYWRkci5uYW1lcQB+AE9wdAAFY3VydmVwc3EAfgBAcQB+AI90ABV0YWMuY29udHJhY3Quc3ltLmFkZHJ2cQB+AAxwcQB+AIZzcQB+AEBxAH4ARnQAGHRhYy5kZWNvbXAtaW5zY2FsYXIuc29ydHZyAB10YWMuRGVjb21wb3NlZElucHV0U2NhbGFyU29ydCeGMd9jMFQFAgAAeHBwc3IAJHRhYy5EZWNvbXBvc2VkSW5wdXRTY2FsYXJTb3J0JFNpbXBsZXkHVfqoCbJbAgABTAAKYnl0ZU9mZnNldHEAfgAGeHEAfgCYcQB+AHx0AANSMzR4cHNxAH4AKnNyABp2Yy5kYXRhLlRBQ1N5bWJvbCRWYXIkRnVsbBPmPQsuB0CVAgAESQAJY2FsbEluZGV4TAAEbWV0YXEAfgAxTAAKbmFtZVByZWZpeHEAfgAyTAADdGFncQB+ACx4cQB+ADMAAAABc3EAfgA2c3EAfgA2cHBxAH4ATHBxAH4AYnBxAH4AY3BzcQB+AEkAAAPvdAAITENBTk9OMjJxAH4AaHEAfgBoc3IAIGluc3RydW1lbnRhdGlvbi5jYWxscy5DYWxsT3V0cHV0wsWbN8G9nHsCAANMAARiYXNlcQB+ACtMAAZvZmZzZXR0ABFMdmMvZGF0YS9UQUNFeHByO0wABHNpemVxAH4ApXhwc3EAfgAwc3EAfgA2cHNxAH4ANnBzcQB+ADZwcHEAfgBDcHEAfgBLcQB+AExwcQB+AFBxAH4AUXBxAH4AVXEAfgBWc3EAfgAqc3EAfgBec3EAfgA2c3EAfgA2cHBxAH4ATHBxAH4AYnBxAH4AY3BzcQB+AEkAAAPwcQB+AGZxAH4AaHNyABl2Yy5kYXRhLlRBQ0V4cHIkU3ltJENvbnN0U0iv8zJB2nYCAAJMAAFzcQB+AHJMAAN0YWdxAH4ALHhxAH4ALXNxAH4Ad3EAfgBoc3EAfgAM///////////////+/////gAAAAF1cQB+ABAAAAABIHhxAH4AaHNyAB5hbmFseXNpcy5pY2ZnLkNhbGxUYXJnZXQkVmFsaWS5phn2PatV+gIAAUwABmNhbGxlZXEAfgBzeHIAGGFuYWx5c2lzLmljZmcuQ2FsbFRhcmdldEbdPSx8dj4lAgAAeHBzcgBHYW5hbHlzaXMuaWNmZy5DYWxsR3JhcGhCdWlsZGVyJENhbGxlZENvbnRyYWN0JEZ1bGx5UmVzb2x2ZWQkU3RvcmFnZUxpbmvSgQnS0FaL1QIAAkkADXN0b3JhZ2VSZWFkSWRMAApjb250cmFjdElkcQB+AAZ4cQB+AIMAAAAlcQB+AA9+cgATdmMuZGF0YS5UQUNDYWxsVHlwZQAAAAAAAAAAEgAAeHEAfgBFdAAGU1RBVElDcHNxAH4AXnNxAH4ANnNxAH4ANnBwcQB+AExwcQB+AGJwcQB+AGNwc3EAfgBJAAAD7HQABFIxNjFzcQB+ADBzcQB+ADZwc3EAfgA2cHNxAH4ANnBwcQB+AENwcQB+AEtxAH4ATHBxAH4AUHEAfgBRcHEAfgBVcQB+AFZzcQB+AF5zcQB+ADZzcQB+ADZwcHEAfgBMcHEAfgBicHEAfgBjcHEAfgBlcQB+AGZzcQB+AHdxAH4AaHEAfgBbc3IAHnZjLmRhdGEuVEFDQ21kJFNpbXBsZSRDYWxsQ29yZaEphUcEgWZ6AgALTAAIY2FsbFR5cGVxAH4AGUwAA2dhc3EAfgAbTAAGaW5CYXNlcQB+ACtMAAhpbk9mZnNldHEAfgAbTAAGaW5TaXplcQB+ABtMAARtZXRhcQB+ADFMAAdvdXRCYXNlcQB+ACtMAAlvdXRPZmZzZXRxAH4AG0wAB291dFNpemVxAH4AG0wAAnRvcQB+ABtMAAV2YWx1ZXEAfgAbeHIAFXZjLmRhdGEuVEFDQ21kJFNpbXBsZe0m1iUxBnXSAgAAeHIAE3ZjLmRhdGEuVEFDQ21kJFNwZWMbq/EA+MEDvgIAAHhyAA52Yy5kYXRhLlRBQ0NtZFTLD4g8OR/wAgAAeHBxAH4Au3NxAH4AXnNxAH4ANnNxAH4ANnBwcQB+AExwcQB+AGJwcQB+AGNwcQB+AMBxAH4AwXNxAH4AMHNxAH4ANnBzcQB+ADZwc3EAfgA2cHBxAH4AQ3BxAH4AS3EAfgBMcHEAfgBQcQB+AFFwcQB+AFVxAH4AVnNxAH4AXnNxAH4ANnNxAH4ANnBwcQB+AExwcQB+AGJwcQB+AGNwcQB+AGVxAH4AZnNxAH4AngAAAAFzcQB+ADZzcQB+ADZwcHEAfgBMcHEAfgBicHEAfgBjcHEAfgCicQB+AKNxAH4AaHNxAH4ANnBwc3EAfgBAfnEAfgBEdAAJQ2FsbFRyYWNldAAIdGFjLm1ldGF2cgATdmMuZGF0YS5UQUNNZXRhSW5mbzVgTP2lS6hxAgAGSQAFYmVnaW5JAANsZW5JAAZzb3VyY2VMAAdhZGRyZXNzcQB+AAZMAAhqdW1wVHlwZXQAE0xjb21waWxlci9KdW1wVHlwZTtMAA1zb3VyY2VDb250ZXh0dAAYTGNvbXBpbGVyL1NvdXJjZUNvbnRleHQ7eHBwc3EAfgDhAAAXHwAAACcAAAAHcQB+AIZ+cgARY29tcGlsZXIuSnVtcFR5cGUAAAAAAAAAABIAAHhxAH4ARXQAB1JFR1VMQVJzcgAWY29tcGlsZXIuU291cmNlQ29udGV4dIzLW+lAXNoTAgACTAAPaW5kZXhUb0ZpbGVwYXRocQB+ACdMAAlzb3VyY2VEaXJxAH4AMnhwc3EAfgBpP0AAAAAAAAx3CAAAABAAAAAIc3EAfgBJAAAAAHQAFWNvbnRyYWN0cy9Db250ZXh0LnNvbHNxAH4ASQAAAAF0ABhjb250cmFjdHMvQ3VydmVUb2tlbi5zb2xxAH4AS3QAH2NvbnRyYWN0cy9DdXJ2ZVRva2VuRXhhbXBsZS5zb2xzcQB+AEkAAAADdAATY29udHJhY3RzL0VSQzIwLnNvbHNxAH4ASQAAAAR0ABRjb250cmFjdHMvSUVSQzIwLnNvbHNxAH4ASQAAAAV0ABxjb250cmFjdHMvSUVSQzIwTWV0YWRhdGEuc29sc3EAfgBJAAAABnQAHWNvbnRyYWN0cy9SZWVudHJhbmN5R3VhcmQuc29sc3EAfgBJAAAAB3QAE2NvbnRyYWN0cy9jdXJ2ZS5zb2x4dAATLnBvc3RfYXV0b2ZpbmRlcnMuMnNxAH4AMHNxAH4ANnBzcQB+ADZwc3EAfgA2cHBxAH4AQ3BxAH4AS3EAfgBMcHEAfgBQcQB+AFFwcQB+AFVxAH4AVnNxAH4AXnNxAH4ANnNxAH4ANnBwcQB+AExwcQB+AGJwcQB+AGNwcQB+AK9xAH4AZnEAfgCyc3EAfgBec3EAfgA2c3EAfgA2c3EAfgA2c3EAfgA2cHNxAH4ANnBwcQB+AExwcQB+AGJzcQB+AEBxAH4ARnQAFnRhYy5zY2FsYXJpemF0aW9uLnNvcnR2cgAZdmMuZGF0YS5TY2FsYXJpemF0aW9uU29ydDDOcJ3kaA0mAgAAeHBwc3IAIHZjLmRhdGEuU2NhbGFyaXphdGlvblNvcnQkUGFja2VkLkWtEpOI5PcCAAJJAAVzdGFydEwAC3BhY2tlZFN0YXJ0dAAbTHZjL2RhdGEvU2NhbGFyaXphdGlvblNvcnQ7eHEAfgELAAAAAHNyAB92Yy5kYXRhLlNjYWxhcml6YXRpb25Tb3J0JFNwbGl0VP9Zp/HHsgUCAAFMAANpZHhxAH4ABnhxAH4BC3NxAH4ADP///////////////v////4AAAABdXEAfgAQAAAAAQt4c3EAfgA2cHNxAH4ANnBzcQB+ADZwcHNxAH4AQHEAfgBGdAAcdGFjLnN0b3JhZ2Uubm9uLWluZGV4ZWQtcGF0aHZyADVhbmFseXNpcy5zdG9yYWdlLlN0b3JhZ2VBbmFseXNpc1Jlc3VsdCROb25JbmRleGVkUGF0aAjBoEuh+j9FAgAAeHBwc3IAOmFuYWx5c2lzLnN0b3JhZ2UuU3RvcmFnZUFuYWx5c2lzUmVzdWx0JE5vbkluZGV4ZWRQYXRoJFJvb3S/N/XYpeoK/wIAAUwABHNsb3RxAH4ABnhxAH4BGXEAfgESc3EAfgBAcQB+AEZ0AA10YWMuc2xvdC50eXBldnIAOnNwZWMuY3ZsYXN0LnR5cGVkZXNjcmlwdG9ycy5FVk1UeXBlRGVzY3JpcHRvciRFVk1WYWx1ZVR5cGXGia8Cuuq4JQIAAHhyAC1zcGVjLmN2bGFzdC50eXBlZGVzY3JpcHRvcnMuRVZNVHlwZURlc2NyaXB0b3LIUanxPMJqHQIAAHhwcHNyADVzcGVjLmN2bGFzdC50eXBlZGVzY3JpcHRvcnMuRVZNVHlwZURlc2NyaXB0b3IkYWRkcmVzc3r4ZfRvl6ApAgAAeHIARHNwZWMuY3ZsYXN0LnR5cGVkZXNjcmlwdG9ycy5FVk1UeXBlRGVzY3JpcHRvciRFVk1Jc29tb3JwaGljVmFsdWVUeXBl93WYkW4QoQ8CAAB4cQB+AR9zcQB+AEBxAH4Aj3QAGHRhYy5zdG9yYWdlLnByZXR0eS5wYXRoc3ZyAB1hbmFseXNpcy5zdG9yYWdlLkRpc3BsYXlQYXRoc/dES7fD9VEWAgABTAAFcGF0aHNxAH4AHXhwcHNxAH4BJ3NyABdqYXZhLnV0aWwuTGlua2VkSGFzaFNldNhs11qV3SoeAgAAeHIAEWphdmEudXRpbC5IYXNoU2V0ukSFlZa4tzQDAAB4cHcMAAAAED9AAAAAAAABc3IAIWFuYWx5c2lzLnN0b3JhZ2UuRGlzcGxheVBhdGgkUm9vdNNzoL2Z0DxyAgACTAAEYmFzZXQAHkxhbmFseXNpcy9zdG9yYWdlL0Rpc3BsYXlQYXRoO0wABG5hbWVxAH4AMnhyABxhbmFseXNpcy5zdG9yYWdlLkRpc3BsYXlQYXRoT0Bj6lbSIAUCAAB4cHB0AAdjb2luc18xeHNxAH4AQHEAfgBGdAAVdGFjLnN0b3JhZ2UuYml0LXdpZHRocQB+AEpwc3EAfgBJAAAAoHBzcQB+AEBxAH4ARnQAC3RhYy5zdG9yYWdlcQB+AJVwcQB+AIZwcQB+AGNwc3EAfgBJAAAD9HQAC0NBTk9OMTghITI0c3EAfgB3cQB+AGhxAH4AbXNxAH4AMHNxAH4ANnBzcQB+ADZwc3EAfgA2cHBxAH4AQ3BxAH4AS3EAfgBMcHEAfgBQcQB+AFFwcQB+AFVxAH4AVnNxAH4AXnNxAH4ANnNxAH4ANnBwcQB+AExwcQB+AGJwcQB+AGNwcQB+AK9xAH4AZnEAfgCyc3IAImphdmEudXRpbC5Db2xsZWN0aW9ucyRTaW5nbGV0b25TZXQsUkGYKcCxvwIAAUwAB2VsZW1lbnRxAH4AN3hwcQB+ABRzcQB+AF5zcQB+ADZzcQB+ADZzcQB+ADZzcQB+ADZwc3EAfgA2cHBxAH4ATHBxAH4AYnEAfgEJcHEAfgEPc3EAfgA2cHNxAH4ANnBzcQB+ADZwcHEAfgEXcHEAfgEccQB+AR1wcQB+ASRxAH4BJXBzcQB+ASdzcQB+ASp3DAAAABA/QAAAAAAAAXEAfgEweHEAfgEycHEAfgE0cHEAfgE1cHEAfgCGcHEAfgBjcHEAfgE3cQB+AThzcQB+AHdxAH4AaHEAfgBt"}
		AnnotationCmd:56 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageGlobalChangeSnippet.StorageBackupPoint","calleeTxId":2}}
		NopCmd
		AssumeExpCmd LAnd(Eq(tacCalldatasize!!0:3 0x24 ) Eq(tacCalldatasize!!0:3 0x24 ) )
		NopCmd
		AssumeExpCmd Eq(tacCalldatabufCANON0@2:0 0x70a0823100000000000000000000000000000000000000000000000000000000 )
		AssignExpCmd:56 tacCalldatabufCANON1@2:79 R34:80
		LabelCmd:56 "Start procedure ERC20-balanceOf(address)"
		AnnotationCmd:56 JSON{"key":{"name":"fps.free-pointer-is-scalarized","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true}
		AssignExpCmd:56 R166:54 Select(tacExtcodesize!!9:4 Apply(to_skey:bif R33:81) )
		NopCmd
		AssumeExpCmd Gt(R166:54 0x0 )
		AnnotationCmd:56 JSON{"key":{"name":"internal.func.finder.info","type":"analysis.ip.InternalFunctionFinderReport","erasureStrategy":"Erased"},"value":"rO0ABXNyAChhbmFseXNpcy5pcC5JbnRlcm5hbEZ1bmN0aW9uRmluZGVyUmVwb3J0ian+bYn1VdACAAFMABN1bnJlc29sdmVkRnVuY3Rpb25zdAAPTGphdmEvdXRpbC9TZXQ7eHBzcgAhZGF0YXN0cnVjdHVyZXMuTGlua2VkQXJyYXlIYXNoU2V0AAAAAAAAAAEDAAJGAApsb2FkRmFjdG9yTAAJaGFzaFRhYmxldAAuTGRhdGFzdHJ1Y3R1cmVzL2FycmF5aGFzaHRhYmxlL0FycmF5SGFzaFRhYmxlO3hwdwgAAAAAQAAAAHg="}
		AnnotationCmd:56 JSON{"key":{"name":"fps.free-pointer-is-scalarized","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true}
		NopCmd
		AssumeExpCmd LNot(Lt(tacCalldatasize!!0:3 0x4 ) )
		NopCmd
		AssumeExpCmd LNot(Gt(0x39509351 tacSighash!!36:47 ) )
		NopCmd
		AssumeExpCmd LNot(Eq(0x39509351 tacSighash!!36:47 ) )
		NopCmd
		AssumeExpCmd Eq(0x70a08231 tacSighash!!36:47 )
		AssignExpCmd:82 R172:83 Sub(tacCalldatasize!!0:3 0x4 )
		AssignExpCmd:56 B173:84 Slt(R172:83 0x20 )
		NopCmd
		AssumeExpCmd LNot(B173:84 )
		AssignExpCmd:85 R175:72 tacCalldatabufCANON1@2:86
		NopCmd
		AssumeExpCmd Eq(R34:80 R34:80 )
		AnnotationCmd:56 JSON{"key":{"name":"internal.func.start","type":"analysis.ip.InternalFuncStartAnnotation","erasureStrategy":"CallTrace"},"value":{"id":1,"startPc":1712,"args":[{"s":{"namePrefix":"R175","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1013}]},"offset":1,"sort":"SCALAR"}],"methodSignature":{"#class":"spec.cvlast.QualifiedMethodSignature.QualifiedMethodSig","qualifiedMethodName":{"#class":"spec.cvlast.QualifiedFunction","host":{"name":"ERC20"},"methodId":"balanceOf"},"params":[{"#class":"spec.cvlast.VMParam.Named","name":"account","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$address"}}],"res":[{"#class":"spec.cvlast.VMParam.Unnamed","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256}}]},"stackOffsetToArgPos":{"1":0},"callSiteSrc":{"source":1,"begin":4376,"len":467,"jumpType":"ENTER","address":"ce4604a0000000000000000000000011","sourceContext":{"indexToFilepath":{"0":"contracts/Context.sol","1":"contracts/ERC20.sol","2":"contracts/IERC20.sol","3":"contracts/IERC20Metadata.sol"},"sourceDir":".post_autofinders.1"}}}}
		AssignExpCmd:87 R180:88 Apply(hash_3_keccak:bif Apply(skey_basic:bif 0x40) Apply(to_skey:bif R34:80) Apply(skey_basic:bif 0x0))
		AssignExpCmd:89 R181:88 Select(CANON93!!30:42 R180:90 )
		AnnotationCmd:56 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet","value":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R181","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1020}]},"displayPath":{"#class":"analysis.storage.DisplayPath.MapAccess","key":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R175","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1018}]},"keyTyp":{"#class":"tac.TACStorageType.IntegralType","typeLabel":"address","numBytes":"14","descriptor":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$address"},"lowerBound":null,"upperBound":null},"base":{"#class":"analysis.storage.DisplayPath.Root","name":"_balances"}},"storageType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256},"contractInstance":"ce4604a0000000000000000000000011","linkableStorageReadId":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet.None"}}}
		AnnotationCmd:56 JSON{"key":{"name":"internal.func.end","type":"analysis.ip.InternalFuncExitAnnotation","erasureStrategy":"Canonical"},"value":{"id":1,"rets":[{"s":{"namePrefix":"R181","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1023}]},"offset":0}],"functionLayout":{"0":{"#class":"analysis.ip.InternalFuncValueLocation.Scalar"}}}}
		AnnotationCmd:56 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.EVMFunctionReturnWrite","returnbufOffset":"0","returnValueSym":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R181","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1023}]},"callIndex":2}}
		AnnotationCmd:56 JSON{"key":{"name":"tac.return.path","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		LabelCmd:56 "End procedure ERC20-balanceOf(address)"
		AssignExpCmd:56 tacReturndata!!183:78 Store(tacReturndata!!162:78 0x0 R181:88 )
		AssignExpCmd:56 tacMCANON2!!184:9 Store(tacMCANON2!!159:9 0x100 R181:88 )
		AnnotationCmd:56 JSON{"key":{"name":"call.trace.pop","type":"analysis.icfg.Inliner$CallStack$PopRecord","erasureStrategy":"Canonical"},"value":"rO0ABXNyAClhbmFseXNpcy5pY2ZnLklubGluZXIkQ2FsbFN0YWNrJFBvcFJlY29yZPAPfwSLdCWJAgABSQAIY2FsbGVlSWR4cAAAAAI="}
		JumpCmd:56 1_0_0_1_0_0
	}
	Block 0_0_0_3_0_0 Succ [2_0_0_1_0_0] {
		AnnotationCmd:56 JSON{"key":{"name":"call.trace.push","type":"analysis.icfg.Inliner$CallStack$PushRecord","erasureStrategy":"Canonical"},"value":"rO0ABXNyACphbmFseXNpcy5pY2ZnLklubGluZXIkQ2FsbFN0YWNrJFB1c2hSZWNvcmSX8+DCTLCH+AIAA0kACGNhbGxlZUlkTAAGY2FsbGVldAATTHZjL2RhdGEvTWV0aG9kUmVmO0wAB3N1bW1hcnl0ABVMdmMvZGF0YS9DYWxsU3VtbWFyeTt4cAAAAANzcgARdmMuZGF0YS5NZXRob2RSZWbJlJTzzU9pGAIAA0wABGF0dHJ0ABdMc2NlbmUvTWV0aG9kQXR0cmlidXRlO0wACmNvbnRyYWN0SWR0ABZMamF2YS9tYXRoL0JpZ0ludGVnZXI7TAAHc2lnSGFzaHQAEExldm0vU2lnaGFzaEludDt4cHNyABxzY2VuZS5NZXRob2RBdHRyaWJ1dGUkQ29tbW9uNHjdebdr9XMCAAB4cgAVc2NlbmUuTWV0aG9kQXR0cmlidXRlcYg2pYWutuUCAAB4cHNyABRqYXZhLm1hdGguQmlnSW50ZWdlcoz8nx+pO/sdAwAGSQAIYml0Q291bnRJAAliaXRMZW5ndGhJABNmaXJzdE5vbnplcm9CeXRlTnVtSQAMbG93ZXN0U2V0Qml0SQAGc2lnbnVtWwAJbWFnbml0dWRldAACW0J4cgAQamF2YS5sYW5nLk51bWJlcoaslR0LlOCLAgAAeHD///////////////7////+AAAAAXVyAAJbQqzzF/gGCFTgAgAAeHAAAAAQzkYEoAAAAAAAAAAAAAAAKHhzcgAOZXZtLlNpZ2hhc2hJbnRUdcqNMXEgeAIAAUwAAW5xAH4ABnhwc3EAfgAM///////////////+/////gAAAAF1cQB+ABAAAAAEOEL3dnhzcgATdmMuZGF0YS5DYWxsU3VtbWFyeZQcmw5vl+FdAgAQSQAJc3VtbWFyeUlkTAAOY2FsbENvbnZlbnRpb250ACZMaW5zdHJ1bWVudGF0aW9uL2NhbGxzL0NhbGxDb252ZW50aW9uO0wACmNhbGxUYXJnZXR0ABpMYW5hbHlzaXMvaWNmZy9DYWxsVGFyZ2V0O0wACGNhbGxUeXBldAAVTHZjL2RhdGEvVEFDQ2FsbFR5cGU7TAAPY2Fubm90QmVJbmxpbmVkdAAtTGFuYWx5c2lzL2ljZmcvSW5saW5lciRJbGxlZ2FsSW5saW5pbmdSZWFzb247TAAGZ2FzVmFydAATTHZjL2RhdGEvVEFDU3ltYm9sO0wABmluQmFzZXEAfgAbTAAIaW5PZmZzZXRxAH4AG0wABmluU2l6ZXEAfgAbTAAMb3JpZ0NhbGxjb3JldAAgTHZjL2RhdGEvVEFDQ21kJFNpbXBsZSRDYWxsQ29yZTtMAAdvdXRCYXNlcQB+ABtMAAlvdXRPZmZzZXRxAH4AG0wAB291dFNpemVxAH4AG0wADXNpZ1Jlc29sdXRpb250AA9MamF2YS91dGlsL1NldDtMAAV0b1ZhcnEAfgAbTAAIdmFsdWVWYXJxAH4AG3hwAAAAAXNyACRpbnN0cnVtZW50YXRpb24uY2FsbHMuQ2FsbENvbnZlbnRpb25HtO1ulL788QIAA0kACGNhbGxlcklkTAAFaW5wdXR0ABlMYW5hbHlzaXMvaWNmZy9DYWxsSW5wdXQ7TAAGcmF3T3V0dAAiTGluc3RydW1lbnRhdGlvbi9jYWxscy9DYWxsT3V0cHV0O3hwAAAAAHNyABdhbmFseXNpcy5pY2ZnLkNhbGxJbnB1dJjJD1MhNUxQAgAHTAAHYmFzZVZhcnQAGUx2Yy9kYXRhL1RBQ0V4cHIkU3ltJFZhcjtMABBlbmNvZGVkQXJndW1lbnRzdAAjTGFuYWx5c2lzL2ljZmcvQUJJQXJndW1lbnRFbmNvZGluZztMABNpbnB1dFNpemVMb3dlckJvdW5kcQB+AAZMAAZvZmZzZXR0ABVMdmMvZGF0YS9UQUNFeHByJFN5bTtMABRyYW5nZVRvRGVjb21wb3NlZEFyZ3QAD0xqYXZhL3V0aWwvTWFwO0wAEHNpbXBsaWZpZWRPZmZzZXR0ABtMdmMvZGF0YS9UQUNFeHByJFN5bSRDb25zdDtMAARzaXplcQB+ACZ4cHNyABd2Yy5kYXRhLlRBQ0V4cHIkU3ltJFZhcskrg43eGgPnAgACTAABc3QAF0x2Yy9kYXRhL1RBQ1N5bWJvbCRWYXI7TAADdGFndAAJTHRhYy9UYWc7eHIAE3ZjLmRhdGEuVEFDRXhwciRTeW2iVj0S4YSNUAIAAHhyAA92Yy5kYXRhLlRBQ0V4cHJYhGlUu/v+yAIAAHhwc3IANnZjLmRhdGEuVEFDU3ltYm9sJFZhciRXaXRoRGVmYXVsdENhbGxJbmRleCRXaXRoQnl0ZU1hcJ7+oHF4CHAAAgACTAAEbWV0YXQALUxrb3RsaW54L2NvbGxlY3Rpb25zL2ltbXV0YWJsZS9QZXJzaXN0ZW50TWFwO0wACm5hbWVQcmVmaXh0ABJMamF2YS9sYW5nL1N0cmluZzt4cgAVdmMuZGF0YS5UQUNTeW1ib2wkVmFyCYrCGVl9SXYCAAB4cgARdmMuZGF0YS5UQUNTeW1ib2zd3Run/CoWswIAAHhwc3IAJmRhdGFzdHJ1Y3R1cmVzLnRyZWFwLkhhc2hUcmVhcE1hcCROb2Rlf2t9acJIPnQCAANMAANrZXl0ABJMamF2YS9sYW5nL09iamVjdDtMAARuZXh0dAA1TGRhdGFzdHJ1Y3R1cmVzL3RyZWFwL0hhc2hUcmVhcE1hcCRNb3JlS2V5VmFsdWVQYWlycztMAAV2YWx1ZXEAfgA3eHIAIWRhdGFzdHJ1Y3R1cmVzLnRyZWFwLkhhc2hUcmVhcE1hcPMJ/2vt3boKAgAAeHIAHWRhdGFzdHJ1Y3R1cmVzLnRyZWFwLlRyZWFwTWFw46LAyn3v5moCAAB4cgAaZGF0YXN0cnVjdHVyZXMudHJlYXAuVHJlYXA88f21zZwbdQIAAkwABGxlZnR0ABxMZGF0YXN0cnVjdHVyZXMvdHJlYXAvVHJlYXA7TAAFcmlnaHRxAH4APHhwcHNxAH4ANnBzcQB+ADZwcHNyAAt0YWMuTWV0YUtleVF/W3MiCfIZAgADTAAPZXJhc3VyZVN0cmF0ZWd5dAAdTHRhYy9NZXRhS2V5JEVyYXN1cmVTdHJhdGVneTtMAARuYW1lcQB+ADJMAAN0eXB0ABFMamF2YS9sYW5nL0NsYXNzO3hwfnIAG3RhYy5NZXRhS2V5JEVyYXN1cmVTdHJhdGVneQAAAAAAAAAAEgAAeHIADmphdmEubGFuZy5FbnVtAAAAAAAAAAASAAB4cHQACUNhbm9uaWNhbHQAF3RhYy5tZW1vcnkucGFydGl0aW9uLWlkdnIAEWphdmEubGFuZy5JbnRlZ2VyEuKgpPeBhzgCAAFJAAV2YWx1ZXhxAH4ADnBzcQB+AEkAAAACc3EAfgBAcQB+AEZ0ABJUYWMuc3ltYm9sLmtleXdvcmR2cgAQamF2YS5sYW5nLlN0cmluZ6DwpDh6O7NCAgAAeHBwdAAEdGFjTXNxAH4AQHEAfgBGdAANdGFjLmlzLm1lbW9yeXZyACJ0YWMuTWV0YU1hcCRDb21wYW5pb24kTm90aGluZ1ZhbHVl8nsHH85ykpUCAAB4cHBzcQB+AFN0AA90YWNNQ0FOT04yISEzODhzcgAPdGFjLlRhZyRCeXRlTWFwNb/Ry6GDRgkCAAB4cgALdGFjLlRhZyRNYXABJytzDV3P/QIAAHhyAAd0YWMuVGFnLk9V3gn2xngCAAB4cHBzcQB+AAz///////////////7////+AAAAAXVxAH4AEAAAAAFkeHNxAH4AKnNyADV2Yy5kYXRhLlRBQ1N5bWJvbCRWYXIkV2l0aERlZmF1bHRDYWxsSW5kZXgkV2l0aEJpdDI1NnqsyEgq0drPAgACTAAEbWV0YXEAfgAxTAAKbmFtZVByZWZpeHEAfgAyeHEAfgAzc3EAfgA2c3EAfgA2cHBxAH4ATHB0AAFMcHNxAH4AQHEAfgBGdAAQdGFjLnN0YWNrLmhlaWdodHEAfgBKcHNxAH4ASQAAA/h0AARSMzg5c3IADnRhYy5UYWckQml0MjU2IyLQT+LlKkgCAAB4cQB+AFlzcgARamF2YS51dGlsLkhhc2hNYXAFB9rBwxZg0QMAAkYACmxvYWRGYWN0b3JJAAl0aHJlc2hvbGR4cD9AAAAAAAADdwgAAAAEAAAAAnNyAB5hbmFseXNpcy5pY2ZnLlNjcmF0Y2hCeXRlUmFuZ2XBTLaPpUzj2gIAAkwABGZyb21xAH4ABkwAAnRvcQB+AAZ4cHNxAH4ADP///////////////v////4AAAAAdXEAfgAQAAAAAHhzcQB+AAz///////////////7////+AAAAAXVxAH4AEAAAAAEDeHNyAC1hbmFseXNpcy5pY2ZnLkRlY29tcG9zZWRDYWxsSW5wdXRBcmckQ29uc3RhbnSFavLdQafqPQIAA0wAAWN0ABlMdmMvZGF0YS9UQUNTeW1ib2wkQ29uc3Q7TAARY29udHJhY3RSZWZlcmVuY2V0AC9MYW5hbHlzaXMvaWNmZy9DYWxsR3JhcGhCdWlsZGVyJENhbGxlZENvbnRyYWN0O0wADHNjcmF0Y2hSYW5nZXQAIExhbmFseXNpcy9pY2ZnL1NjcmF0Y2hCeXRlUmFuZ2U7eHIAJGFuYWx5c2lzLmljZmcuRGVjb21wb3NlZENhbGxJbnB1dEFyZ82Nwhnirh8hAgAAeHBzcgAXdmMuZGF0YS5UQUNTeW1ib2wkQ29uc3QmHp5/l8IUcAIAAkwAA3RhZ3EAfgAsTAAFdmFsdWVxAH4ABnhxAH4ANHEAfgBoc3EAfgAM///////////////+/////gAAAAF1cQB+ABAAAAAgOEL3dgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAB4cHEAfgBsc3EAfgBrc3EAfgAM///////////////+/////gAAAAF1cQB+ABAAAAABRHhzcQB+AAz///////////////7////+AAAAAXVxAH4AEAAAAAFjeHNyAC1hbmFseXNpcy5pY2ZnLkRlY29tcG9zZWRDYWxsSW5wdXRBcmckVmFyaWFibGWV3y80jneopQIAA0wAEWNvbnRyYWN0UmVmZXJlbmNlcQB+AHNMAAxzY3JhdGNoUmFuZ2VxAH4AdEwAAXZxAH4AK3hxAH4AdXNyADxhbmFseXNpcy5pY2ZnLkNhbGxHcmFwaEJ1aWxkZXIkQ2FsbGVkQ29udHJhY3QkVW5yZXNvbHZlZFJlYWRDhKJZ0RDzoAIAAUkADXN0b3JhZ2VSZWFkSWR4cgAtYW5hbHlzaXMuaWNmZy5DYWxsR3JhcGhCdWlsZGVyJENhbGxlZENvbnRyYWN00wt1rN/LodcCAAB4cAAAAAJxAH4Ae3NxAH4AXnNxAH4ANnNxAH4ANnBzcQB+ADZzcQB+ADZzcQB+ADZwc3EAfgA2cHBxAH4ATHBxAH4AYnNxAH4AQHEAfgBGdAAWdGFjLnNjYWxhcml6YXRpb24uc29ydHZyABl2Yy5kYXRhLlNjYWxhcml6YXRpb25Tb3J0MM5wneRoDSYCAAB4cHBzcgAfdmMuZGF0YS5TY2FsYXJpemF0aW9uU29ydCRTcGxpdFT/Wafxx7IFAgABTAADaWR4cQB+AAZ4cQB+AI5zcQB+AAz///////////////7////+AAAAAXVxAH4AEAAAAAEFeHNxAH4ANnBzcQB+ADZwc3EAfgA2cHBzcQB+AEBxAH4ARnQAHHRhYy5zdG9yYWdlLm5vbi1pbmRleGVkLXBhdGh2cgA1YW5hbHlzaXMuc3RvcmFnZS5TdG9yYWdlQW5hbHlzaXNSZXN1bHQkTm9uSW5kZXhlZFBhdGgIwaBLofo/RQIAAHhwcHNyADphbmFseXNpcy5zdG9yYWdlLlN0b3JhZ2VBbmFseXNpc1Jlc3VsdCROb25JbmRleGVkUGF0aCRSb290vzf12KXqCv8CAAFMAARzbG90cQB+AAZ4cQB+AJlxAH4AknNxAH4AQHEAfgBGdAANdGFjLnNsb3QudHlwZXZyADpzcGVjLmN2bGFzdC50eXBlZGVzY3JpcHRvcnMuRVZNVHlwZURlc2NyaXB0b3IkRVZNVmFsdWVUeXBlxomvArrquCUCAAB4cgAtc3BlYy5jdmxhc3QudHlwZWRlc2NyaXB0b3JzLkVWTVR5cGVEZXNjcmlwdG9yyFGp8TzCah0CAAB4cHBzcgAzc3BlYy5jdmxhc3QudHlwZWRlc2NyaXB0b3JzLkVWTVR5cGVEZXNjcmlwdG9yJFVJbnRL+xQfR/Nlf8ACAAFJAAhiaXR3aWR0aHhyAERzcGVjLmN2bGFzdC50eXBlZGVzY3JpcHRvcnMuRVZNVHlwZURlc2NyaXB0b3IkRVZNSXNvbW9ycGhpY1ZhbHVlVHlwZfd1mJFuEKEPAgAAeHEAfgCfAAABAHNxAH4AQH5xAH4ARHQABkVyYXNlZHQAGHRhYy5zdG9yYWdlLnByZXR0eS5wYXRoc3ZyAB1hbmFseXNpcy5zdG9yYWdlLkRpc3BsYXlQYXRoc/dES7fD9VEWAgABTAAFcGF0aHNxAH4AHXhwcHNxAH4AqXNyABdqYXZhLnV0aWwuTGlua2VkSGFzaFNldNhs11qV3SoeAgAAeHIAEWphdmEudXRpbC5IYXNoU2V0ukSFlZa4tzQDAAB4cHcMAAAAED9AAAAAAAABc3IAIWFuYWx5c2lzLnN0b3JhZ2UuRGlzcGxheVBhdGgkUm9vdNNzoL2Z0DxyAgACTAAEYmFzZXQAHkxhbmFseXNpcy9zdG9yYWdlL0Rpc3BsYXlQYXRoO0wABG5hbWVxAH4AMnhyABxhbmFseXNpcy5zdG9yYWdlLkRpc3BsYXlQYXRoT0Bj6lbSIAUCAAB4cHB0AAhmdXR1cmVfQXhzcQB+AEBxAH4ARnQAFXRhYy5zdG9yYWdlLmJpdC13aWR0aHEAfgBKcHNxAH4ASQAAAQBwc3EAfgBAcQB+AEZ0AAt0YWMuc3RvcmFnZXZxAH4ADHBxAH4AD3NxAH4AQHEAfgBGdAAYdGFjLmRlY29tcC1p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"}
		AnnotationCmd:56 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageGlobalChangeSnippet.StorageBackupPoint","calleeTxId":3}}
		NopCmd
		AssumeExpCmd LAnd(Eq(tacCalldatasize!!1:3 0x64 ) Eq(tacCalldatasize!!1:3 0x64 ) )
		AssignExpCmd:56 B187:54 Eq(Select(tacCalldatabuf!!21@3:91 0x0 ) 0x3842f77600000000000000000000000000000000000000000000000000000000 )
		AssumeCmd:56 B187:54
		AssignExpCmd:56 tacCalldatabuf!!188@3:18 LongStore(tacCalldatabuf!!21@3:91 0x4 tacMCANON2!!388:9 0x124 Sub(0x64 0x4 ) )
		LabelCmd:56 "Start procedure curve-get_D(uint256[2],uint256)"
		AnnotationCmd:56 JSON{"key":{"name":"fps.free-pointer-is-scalarized","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true}
		AssignExpCmd:56 R189:54 Select(tacExtcodesize!!9:4 Apply(to_skey:bif R34:63) )
		NopCmd
		AssumeExpCmd Gt(R189:54 0x0 )
		AnnotationCmd:56 JSON{"key":{"name":"internal.func.finder.info","type":"analysis.ip.InternalFunctionFinderReport","erasureStrategy":"Erased"},"value":"rO0ABXNyAChhbmFseXNpcy5pcC5JbnRlcm5hbEZ1bmN0aW9uRmluZGVyUmVwb3J0ian+bYn1VdACAAFMABN1bnJlc29sdmVkRnVuY3Rpb25zdAAPTGphdmEvdXRpbC9TZXQ7eHBzcgAhZGF0YXN0cnVjdHVyZXMuTGlua2VkQXJyYXlIYXNoU2V0AAAAAAAAAAEDAAJGAApsb2FkRmFjdG9yTAAJaGFzaFRhYmxldAAuTGRhdGFzdHJ1Y3R1cmVzL2FycmF5aGFzaHRhYmxlL0FycmF5SGFzaFRhYmxlO3hwdwgAAAAAQAAAAHg="}
		AnnotationCmd:56 JSON{"key":{"name":"fps.free-pointer-is-scalarized","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true}
		NopCmd
		AssumeExpCmd LNot(Lt(tacCalldatasize!!1:3 0x4 ) )
		NopCmd
		AssumeExpCmd Gt(0x82c63066 tacSighash!!37:47 )
		NopCmd
		AssumeExpCmd Eq(0x3842f776 tacSighash!!37:47 )
		AssignExpCmd:92 R195:93 Sub(tacCalldatasize!!1:3 0x4 )
		AssignExpCmd:56 B196:83 Slt(R195:93 0x60 )
		NopCmd
		AssumeExpCmd LNot(B196:83 )
		NopCmd
		AssumeExpCmd Slt(0x23 tacCalldatasize!!1:94 )
		AssignExpCmd:95 R200:96 0x80
		AssumeCmd:97 true
		AssignExpCmd:56 B201:77 Gt(0x44 tacCalldatasize!!1:94 )
		NopCmd
		AssumeExpCmd LNot(B201:77 )
		AnnotationCmd:56 JSON{"key":{"name":"dsa.assign.start","type":"java.lang.String","erasureStrategy":"Erased"},"value":"4280_1005_0_0_0_0 -> 4282_1004_0_0_0_0"}
		LabelCmd:56 "Parallel assignment for R3573:bv256, R3574:bv256 := R2326:bv256, R3653:bv256"
		AnnotationCmd:56 JSON{"key":{"name":"dsa.assign.end","type":"java.lang.String","erasureStrategy":"Erased"},"value":"4280_1005_0_0_0_0 -> 4282_1004_0_0_0_0"}
		AnnotationCmd:56 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.LoopSnippet.StartLoopSnippet","loopIndex":1,"loopSource":"unknown loop source code"}}
		AnnotationCmd:56 JSON{"key":{"name":"start_loop.cmd","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		AnnotationCmd:56 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.LoopSnippet.StartIter","iteration":1}}
		AssignExpCmd:98 R203:99 Select(tacCalldatabuf!!188@3:91 0x4 )
		AssignExpCmd:100 tacMCANON3!!204:11 Store(tacMCANON3!!15:11 0x80 R203:99 )
		AnnotationCmd:56 JSON{"key":{"name":"dsa.assign.start","type":"java.lang.String","erasureStrategy":"Erased"},"value":"4301_1002_0_0_0_0 -> 4282_1004_0_0_0_0"}
		LabelCmd:56 "Parallel assignment for R3573:bv256, R3574:bv256 := R3566:bv256, R3570:bv256"
		AnnotationCmd:56 JSON{"key":{"name":"dsa.assign.end","type":"java.lang.String","erasureStrategy":"Erased"},"value":"4301_1002_0_0_0_0 -> 4282_1004_0_0_0_0"}
		AnnotationCmd:56 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.LoopSnippet.EndIter","iteration":1}}
		AnnotationCmd:56 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.LoopSnippet.StartIter","iteration":2}}
		AssignExpCmd:98 R205:99 Select(tacCalldatabuf!!188@3:91 0x24 )
		AssignExpCmd:100 tacMCANON3!!206:11 Store(tacMCANON3!!204:11 0xa0 R205:99 )
		AnnotationCmd:56 JSON{"key":{"name":"dsa.assign.start","type":"java.lang.String","erasureStrategy":"Erased"},"value":"4301_1002_0_0_0_0 -> 4282_1004_0_0_0_0"}
		LabelCmd:56 "Parallel assignment for R3573:bv256, R3574:bv256 := R3566:bv256, R3570:bv256"
		AnnotationCmd:56 JSON{"key":{"name":"dsa.assign.end","type":"java.lang.String","erasureStrategy":"Erased"},"value":"4301_1002_0_0_0_0 -> 4282_1004_0_0_0_0"}
		AnnotationCmd:56 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.LoopSnippet.EndIter","iteration":2}}
		AnnotationCmd:56 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.LoopSnippet.EndLoopSnippet","loopId":1}}
		AnnotationCmd:56 JSON{"key":{"name":"end_loop.cmd","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		AnnotationCmd:56 JSON{"key":{"name":"pta.end-allocation","type":"analysis.alloc.AllocationAnalysis$AbstractLocation","erasureStrategy":"Erased"},"value":{"prevFPWriteIdx":0,"nextFPWriteCmd":{"block":{"#class":"tac.BlockIdentifier","origStartPc":4102,"stkTop":1000,"decompCopy":0,"calleeIdx":0,"topOfStackValue":0,"freshCopy":0},"pos":1},"sort":{"#class":"analysis.alloc.AllocationAnalysis.Alloc.ConstBlock","sz":"40"}}}
		AssignExpCmd:98 R207:65 Select(tacCalldatabuf!!188@3:91 0x44 )
		AnnotationCmd:56 JSON{"key":{"name":"internal.func.start","type":"analysis.ip.InternalFuncStartAnnotation","erasureStrategy":"CallTrace"},"value":{"id":3,"startPc":558,"args":[{"s":{"namePrefix":"R200","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1001}]},"offset":1,"sort":"SCALAR"},{"s":{"namePrefix":"R207","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1012}]},"offset":2,"sort":"SCALAR"}],"methodSignature":{"#class":"spec.cvlast.QualifiedMethodSignature.QualifiedMethodSig","qualifiedMethodName":{"#class":"spec.cvlast.QualifiedFunction","host":{"name":"curve"},"methodId":"get_D"},"params":[{"#class":"spec.cvlast.VMParam.Named","name":"xp","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$StaticArrayDescriptor","location":"memory","elementType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256},"numElements":"2"}},{"#class":"spec.cvlast.VMParam.Named","name":"amp","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256}}],"res":[{"#class":"spec.cvlast.VMParam.Unnamed","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256}}]},"stackOffsetToArgPos":{"1":0,"2":1},"callSiteSrc":{"source":7,"begin":2956,"len":1542,"jumpType":"ENTER","address":"ce4604a0000000000000000000000028","sourceContext":{"indexToFilepath":{"0":"contracts/Context.sol","1":"contracts/CurveToken.sol","2":"contracts/CurveTokenExample.sol","3":"contracts/ERC20.sol","4":"contracts/IERC20.sol","5":"contracts/IERC20Metadata.sol","6":"contracts/ReentrancyGuard.sol","7":"contracts/curve.sol"},"sourceDir":".post_autofinders.2"}}}}
		AssignExpCmd:101 R208:83 Select(tacMCANON3!!206:11 0xa0 )
		AssignExpCmd:102 R209:93 Select(tacMCANON3!!206:11 0x80 )
		NopCmd
		AssumeExpCmd Apply(add_noofl:bif R209:93 R208:83)
		NopCmd
		NopCmd
		NopCmd
		AssignExpCmd R215:72 Apply(safe_math_narrow:bif IntAdd(Apply(safe_math_promotion:bif R209:93) Apply(safe_math_promotion:bif R208:83)))
		AnnotationCmd:56 JSON{"key":{"name":"internal.func.end","type":"analysis.ip.InternalFuncExitAnnotation","erasureStrategy":"Canonical"},"value":{"id":3,"rets":[{"s":{"namePrefix":"R215","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1023}]},"offset":0}],"functionLayout":{"0":{"#class":"analysis.ip.InternalFuncValueLocation.Scalar"}}}}
		AnnotationCmd:56 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.EVMFunctionReturnWrite","returnbufOffset":"0","returnValueSym":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R215","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1023}]},"callIndex":3}}
		AnnotationCmd:56 JSON{"key":{"name":"tac.return.path","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		LabelCmd:56 "End procedure curve-get_D(uint256[2],uint256)"
		AssignExpCmd:56 tacReturndata!!217:78 Store(tacReturndata!!392:78 0x0 R215:72 )
		AssignExpCmd:56 tacMCANON2!!218:9 Store(tacMCANON2!!388:9 0x120 R215:72 )
		AnnotationCmd:56 JSON{"key":{"name":"call.trace.pop","type":"analysis.icfg.Inliner$CallStack$PopRecord","erasureStrategy":"Canonical"},"value":"rO0ABXNyAClhbmFseXNpcy5pY2ZnLklubGluZXIkQ2FsbFN0YWNrJFBvcFJlY29yZPAPfwSLdCWJAgABSQAIY2FsbGVlSWR4cAAAAAM="}
		JumpCmd:56 2_0_0_1_0_0
	}
	Block 0_0_0_4_0_0 Succ [3_0_0_1_0_0] {
		AnnotationCmd:56 JSON{"key":{"name":"call.trace.push","type":"analysis.icfg.Inliner$CallStack$PushRecord","erasureStrategy":"Canonical"},"value":"rO0ABXNyACphbmFseXNpcy5pY2ZnLklubGluZXIkQ2FsbFN0YWNrJFB1c2hSZWNvcmSX8+DCTLCH+AIAA0kACGNhbGxlZUlkTAAGY2FsbGVldAATTHZjL2RhdGEvTWV0aG9kUmVmO0wAB3N1bW1hcnl0ABVMdmMvZGF0YS9DYWxsU3VtbWFyeTt4cAAAAARzcgARdmMuZGF0YS5NZXRob2RSZWbJlJTzzU9pGAIAA0wABGF0dHJ0ABdMc2NlbmUvTWV0aG9kQXR0cmlidXRlO0wACmNvbnRyYWN0SWR0ABZMamF2YS9tYXRoL0JpZ0ludGVnZXI7TAAHc2lnSGFzaHQAEExldm0vU2lnaGFzaEludDt4cHNyABxzY2VuZS5NZXRob2RBdHRyaWJ1dGUkQ29tbW9uNHjdebdr9XMCAAB4cgAVc2NlbmUuTWV0aG9kQXR0cmlidXRlcYg2pYWutuUCAAB4cHNyABRqYXZhLm1hdGguQmlnSW50ZWdlcoz8nx+pO/sdAwAGSQAIYml0Q291bnRJAAliaXRMZW5ndGhJABNmaXJzdE5vbnplcm9CeXRlTnVtSQAMbG93ZXN0U2V0Qml0SQAGc2lnbnVtWwAJbWFnbml0dWRldAACW0J4cgAQamF2YS5sYW5nLk51bWJlcoaslR0LlOCLAgAAeHD///////////////7////+AAAAAXVyAAJbQqzzF/gGCFTgAgAAeHAAAAAQzkYEoAAAAAAAAAAAAAAACHhzcgAOZXZtLlNpZ2hhc2hJbnRUdcqNMXEgeAIAAUwAAW5xAH4ABnhwc3EAfgAM///////////////+/////gAAAAF1cQB+ABAAAAAEGBYN3XhzcgATdmMuZGF0YS5DYWxsU3VtbWFyeZQcmw5vl+FdAgAQSQAJc3VtbWFyeUlkTAAOY2FsbENvbnZlbnRpb250ACZMaW5zdHJ1bWVudGF0aW9uL2NhbGxzL0NhbGxDb252ZW50aW9uO0wACmNhbGxUYXJnZXR0ABpMYW5hbHlzaXMvaWNmZy9DYWxsVGFyZ2V0O0wACGNhbGxUeXBldAAVTHZjL2RhdGEvVEFDQ2FsbFR5cGU7TAAPY2Fubm90QmVJbmxpbmVkdAAtTGFuYWx5c2lzL2ljZmcvSW5saW5lciRJbGxlZ2FsSW5saW5pbmdSZWFzb247TAAGZ2FzVmFydAATTHZjL2RhdGEvVEFDU3ltYm9sO0wABmluQmFzZXEAfgAbTAAIaW5PZmZzZXRxAH4AG0wABmluU2l6ZXEAfgAbTAAMb3JpZ0NhbGxjb3JldAAgTHZjL2RhdGEvVEFDQ21kJFNpbXBsZSRDYWxsQ29yZTtMAAdvdXRCYXNlcQB+ABtMAAlvdXRPZmZzZXRxAH4AG0wAB291dFNpemVxAH4AG0wADXNpZ1Jlc29sdXRpb250AA9MamF2YS91dGlsL1NldDtMAAV0b1ZhcnEAfgAbTAAIdmFsdWVWYXJxAH4AG3hwAAAAAnNyACRpbnN0cnVtZW50YXRpb24uY2FsbHMuQ2FsbENvbnZlbnRpb25HtO1ulL788QIAA0kACGNhbGxlcklkTAAFaW5wdXR0ABlMYW5hbHlzaXMvaWNmZy9DYWxsSW5wdXQ7TAAGcmF3T3V0dAAiTGluc3RydW1lbnRhdGlvbi9jYWxscy9DYWxsT3V0cHV0O3hwAAAAAHNyABdhbmFseXNpcy5pY2ZnLkNhbGxJbnB1dJjJD1MhNUxQAgAHTAAHYmFzZVZhcnQAGUx2Yy9kYXRhL1RBQ0V4cHIkU3ltJFZhcjtMABBlbmNvZGVkQXJndW1lbnRzdAAjTGFuYWx5c2lzL2ljZmcvQUJJQXJndW1lbnRFbmNvZGluZztMABNpbnB1dFNpemVMb3dlckJvdW5kcQB+AAZMAAZvZmZzZXR0ABVMdmMvZGF0YS9UQUNFeHByJFN5bTtMABRyYW5nZVRvRGVjb21wb3NlZEFyZ3QAD0xqYXZhL3V0aWwvTWFwO0wAEHNpbXBsaWZpZWRPZmZzZXR0ABtMdmMvZGF0YS9UQUNFeHByJFN5bSRDb25zdDtMAARzaXplcQB+ACZ4cHNyABd2Yy5kYXRhLlRBQ0V4cHIkU3ltJFZhcskrg43eGgPnAgACTAABc3QAF0x2Yy9kYXRhL1RBQ1N5bWJvbCRWYXI7TAADdGFndAAJTHRhYy9UYWc7eHIAE3ZjLmRhdGEuVEFDRXhwciRTeW2iVj0S4YSNUAIAAHhyAA92Yy5kYXRhLlRBQ0V4cHJYhGlUu/v+yAIAAHhwc3IANnZjLmRhdGEuVEFDU3ltYm9sJFZhciRXaXRoRGVmYXVsdENhbGxJbmRleCRXaXRoQnl0ZU1hcJ7+oHF4CHAAAgACTAAEbWV0YXQALUxrb3RsaW54L2NvbGxlY3Rpb25zL2ltbXV0YWJsZS9QZXJzaXN0ZW50TWFwO0wACm5hbWVQcmVmaXh0ABJMamF2YS9sYW5nL1N0cmluZzt4cgAVdmMuZGF0YS5UQUNTeW1ib2wkVmFyCYrCGVl9SXYCAAB4cgARdmMuZGF0YS5UQUNTeW1ib2zd3Run/CoWswIAAHhwc3IAJmRhdGFzdHJ1Y3R1cmVzLnRyZWFwLkhhc2hUcmVhcE1hcCROb2Rlf2t9acJIPnQCAANMAANrZXl0ABJMamF2YS9sYW5nL09iamVjdDtMAARuZXh0dAA1TGRhdGFzdHJ1Y3R1cmVzL3RyZWFwL0hhc2hUcmVhcE1hcCRNb3JlS2V5VmFsdWVQYWlycztMAAV2YWx1ZXEAfgA3eHIAIWRhdGFzdHJ1Y3R1cmVzLnRyZWFwLkhhc2hUcmVhcE1hcPMJ/2vt3boKAgAAeHIAHWRhdGFzdHJ1Y3R1cmVzLnRyZWFwLlRyZWFwTWFw46LAyn3v5moCAAB4cgAaZGF0YXN0cnVjdHVyZXMudHJlYXAuVHJlYXA88f21zZwbdQIAAkwABGxlZnR0ABxMZGF0YXN0cnVjdHVyZXMvdHJlYXAvVHJlYXA7TAAFcmlnaHRxAH4APHhwcHNxAH4ANnBzcQB+ADZwcHNyAAt0YWMuTWV0YUtleVF/W3MiCfIZAgADTAAPZXJhc3VyZVN0cmF0ZWd5dAAdTHRhYy9NZXRhS2V5JEVyYXN1cmVTdHJhdGVneTtMAARuYW1lcQB+ADJMAAN0eXB0ABFMamF2YS9sYW5nL0NsYXNzO3hwfnIAG3RhYy5NZXRhS2V5JEVyYXN1cmVTdHJhdGVneQAAAAAAAAAAEgAAeHIADmphdmEubGFuZy5FbnVtAAAAAAAAAAASAAB4cHQACUNhbm9uaWNhbHQAF3RhYy5tZW1vcnkucGFydGl0aW9uLWlkdnIAEWphdmEubGFuZy5JbnRlZ2VyEuKgpPeBhzgCAAFJAAV2YWx1ZXhxAH4ADnBzcQB+AEkAAAACc3EAfgBAcQB+AEZ0ABJUYWMuc3ltYm9sLmtleXdvcmR2cgAQamF2YS5sYW5nLlN0cmluZ6DwpDh6O7NCAgAAeHBwdAAEdGFjTXNxAH4AQHEAfgBGdAANdGFjLmlzLm1lbW9yeXZyACJ0YWMuTWV0YU1hcCRDb21wYW5pb24kTm90aGluZ1ZhbHVl8nsHH85ykpUCAAB4cHBzcQB+AFN0AA90YWNNQ0FOT04yISE0NDZzcgAPdGFjLlRhZyRCeXRlTWFwNb/Ry6GDRgkCAAB4cgALdGFjLlRhZyRNYXABJytzDV3P/QIAAHhyAAd0YWMuVGFnLk9V3gn2xngCAAB4cHBzcQB+AAz///////////////7////+AAAAAXVxAH4AEAAAAAEEeHNxAH4AKnNyADV2Yy5kYXRhLlRBQ1N5bWJvbCRWYXIkV2l0aERlZmF1bHRDYWxsSW5kZXgkV2l0aEJpdDI1NnqsyEgq0drPAgACTAAEbWV0YXEAfgAxTAAKbmFtZVByZWZpeHEAfgAyeHEAfgAzc3EAfgA2c3EAfgA2cHBxAH4ATHB0AAFMcHNxAH4AQHEAfgBGdAAQdGFjLnN0YWNrLmhlaWdodHEAfgBKcHNxAH4ASQAAA/d0AARSNDQ3c3IADnRhYy5UYWckQml0MjU2IyLQT+LlKkgCAAB4cQB+AFlzcgARamF2YS51dGlsLkhhc2hNYXAFB9rBwxZg0QMAAkYACmxvYWRGYWN0b3JJAAl0aHJlc2hvbGR4cD9AAAAAAAABdwgAAAACAAAAAXNyAB5hbmFseXNpcy5pY2ZnLlNjcmF0Y2hCeXRlUmFuZ2XBTLaPpUzj2gIAAkwABGZyb21xAH4ABkwAAnRvcQB+AAZ4cHNxAH4ADP///////////////v////4AAAAAdXEAfgAQAAAAAHhzcQB+AAz///////////////7////+AAAAAXVxAH4AEAAAAAEDeHNyAC1hbmFseXNpcy5pY2ZnLkRlY29tcG9zZWRDYWxsSW5wdXRBcmckQ29uc3RhbnSFavLdQafqPQIAA0wAAWN0ABlMdmMvZGF0YS9UQUNTeW1ib2wkQ29uc3Q7TAARY29udHJhY3RSZWZlcmVuY2V0AC9MYW5hbHlzaXMvaWNmZy9DYWxsR3JhcGhCdWlsZGVyJENhbGxlZENvbnRyYWN0O0wADHNjcmF0Y2hSYW5nZXQAIExhbmFseXNpcy9pY2ZnL1NjcmF0Y2hCeXRlUmFuZ2U7eHIAJGFuYWx5c2lzLmljZmcuRGVjb21wb3NlZENhbGxJbnB1dEFy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AH4ATHBxAH4AYnNxAH4AQHEAfgBGdAAWdGFjLnNjYWxhcml6YXRpb24uc29ydHZyABl2Yy5kYXRhLlNjYWxhcml6YXRpb25Tb3J0MM5wneRoDSYCAAB4cHBzcgAgdmMuZGF0YS5TY2FsYXJpemF0aW9uU29ydCRQYWNrZWQuRa0Sk4jk9wIAAkkABXN0YXJ0TAALcGFja2VkU3RhcnR0ABtMdmMvZGF0YS9TY2FsYXJpemF0aW9uU29ydDt4cQB+AO0AAAAAc3IAH3ZjLmRhdGEuU2NhbGFyaXphdGlvblNvcnQkU3BsaXRU/1mn8ceyBQIAAUwAA2lkeHEAfgAGeHEAfgDtc3EAfgAM///////////////+/////gAAAAF1cQB+ABAAAAABDHhzcQB+ADZwc3EAfgA2cHNxAH4ANnBwc3EAfgBAcQB+AEZ0ABx0YWMuc3RvcmFnZS5ub24taW5kZXhlZC1wYXRodnIANWFuYWx5c2lzLnN0b3JhZ2UuU3RvcmFnZUFuYWx5c2lzUmVzdWx0JE5vbkluZGV4ZWRQYXRoCMGgS6H6P0UCAAB4cHBzcgA6YW5hbHlzaXMuc3RvcmFnZS5TdG9yYWdlQW5hbHlzaXNSZXN1bHQkTm9uSW5kZXhlZFBhdGgkUm9vdL839dil6gr/AgABTAAEc2xvdHEAfgAGeHEAfgD7cQB+APRzcQB+AEBxAH4ARnQADXRhYy5zbG90LnR5cGV2cgA6c3BlYy5jdmxhc3QudHlwZWRlc2NyaXB0b3JzLkVWTVR5cGVEZXNjcmlwdG9yJEVWTVZhbHVlVHlwZcaJrwK66rglAgAAeHIALXNwZWMuY3ZsYXN0LnR5cGVkZXNjcmlwdG9ycy5FVk1UeXBlRGVzY3JpcHRvcshRqfE8wmodAgAAeHBwc3IANXNwZWMuY3ZsYXN0LnR5cGVkZXNjcmlwdG9ycy5FVk1UeXBlRGVzY3JpcHRvciRhZGRyZXNzevhl9G+XoCkCAAB4cgBEc3BlYy5jdmxhc3QudHlwZWRlc2NyaXB0b3JzLkVWTVR5cGVEZXNjcmlwdG9yJEVWTUlzb21vcnBoaWNWYWx1ZVR5cGX3dZiRbhChDwIAAHhxAH4BAXNxAH4AQH5xAH4ARHQABkVyYXNlZHQAGHRhYy5zdG9yYWdlLnByZXR0eS5wYXRoc3ZyAB1hbmFseXNpcy5zdG9yYWdlLkRpc3BsYXlQYXRoc/dES7fD9VEWAgABTAAFcGF0aHNxAH4AHXhwcHNxAH4BC3NyABdqYXZhLnV0aWwuTGlua2VkSGFzaFNldNhs11qV3SoeAgAAeHIAEWphdmEudXRpbC5IYXNoU2V0ukSFlZa4tzQDAAB4cHcMAAAAED9AAAAAAAABc3IAIWFuYWx5c2lzLnN0b3JhZ2UuRGlzcGxheVBhdGgkUm9vdNNzoL2Z0DxyAgACTAAEYmFzZXQAHkxhbmFseXNpcy9zdG9yYWdlL0Rpc3BsYXlQYXRoO0wABG5hbWVxAH4AMnhyABxhbmFseXNpcy5zdG9yYWdlLkRpc3BsYXlQYXRoT0Bj6lbSIAUCAAB4cHB0AAhscF90b2tlbnhzcQB+AEBxAH4ARnQAFXRhYy5zdG9yYWdlLmJpdC13aWR0aHEAfgBKcHNxAH4ASQAAAKBwc3EAfgBAcQB+AEZ0AAt0YWMuc3RvcmFnZXZxAH4ADHBxAH4AxnBxAH4AY3BzcQB+AEkAAAP7dAALQ0FOT04xOSEhMjVzcQB+AHdxAH4AaHEAfgBtc3EAfgAwc3EAfgA2cHNxAH4ANnBzcQB+ADZwcHEAfgBDcHEAfgBLcQB+AExwcQB+AFBxAH4AUXBxAH4AVXEAfgBWc3EAfgBec3EAfgA2c3EAfgA2cHBxAH4ATHBxAH4AYnBxAH4AY3BxAH4AjXEAfgBmcQB+AJBzcgAiamF2YS51dGlsLkNvbGxlY3Rpb25zJFNpbmdsZXRvblNldCxSQZgpwLG/AgABTAAHZWxlbWVudHEAfgA3eHBxAH4AFHNxAH4AXnNxAH4ANnNxAH4ANnNxAH4ANnNxAH4ANnBzcQB+ADZwcHEAfgBMcHEAfgBicQB+AOtwcQB+APFzcQB+ADZwc3EAfgA2cHNxAH4ANnBwcQB+APlwcQB+AP5xAH4A/3BxAH4BBnEAfgEHcHNxAH4BC3NxAH4BDncMAAAAED9AAAAAAAABcQB+ARR4cQB+ARZwcQB+ARhwcQB+ARlwcQB+AMZwcQB+AGNwcQB+ARxxAH4BHXNxAH4Ad3EAfgBocQB+AG0="}
		AnnotationCmd:56 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageGlobalChangeSnippet.StorageBackupPoint","calleeTxId":4}}
		NopCmd
		AssumeExpCmd LAnd(Eq(tacCalldatasize!!2:3 0x4 ) Eq(tacCalldatasize!!2:3 0x4 ) )
		NopCmd
		AssumeExpCmd Eq(tacCalldatabufCANON0@4:0 0x18160ddd00000000000000000000000000000000000000000000000000000000 )
		LabelCmd:56 "Start procedure CurveTokenExample-totalSupply()"
		AnnotationCmd:56 JSON{"key":{"name":"fps.free-pointer-is-scalarized","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true}
		AssignExpCmd:56 R222:54 Select(tacExtcodesize!!9:4 Apply(to_skey:bif R32:103) )
		NopCmd
		AssumeExpCmd Gt(R222:54 0x0 )
		AnnotationCmd:56 JSON{"key":{"name":"internal.func.finder.info","type":"analysis.ip.InternalFunctionFinderReport","erasureStrategy":"Erased"},"value":"rO0ABXNyAChhbmFseXNpcy5pcC5JbnRlcm5hbEZ1bmN0aW9uRmluZGVyUmVwb3J0ian+bYn1VdACAAFMABN1bnJlc29sdmVkRnVuY3Rpb25zdAAPTGphdmEvdXRpbC9TZXQ7eHBzcgAhZGF0YXN0cnVjdHVyZXMuTGlua2VkQXJyYXlIYXNoU2V0AAAAAAAAAAEDAAJGAApsb2FkRmFjdG9yTAAJaGFzaFRhYmxldAAuTGRhdGFzdHJ1Y3R1cmVzL2FycmF5aGFzaHRhYmxlL0FycmF5SGFzaFRhYmxlO3hwdwgAAAAAQAAAAHg="}
		AnnotationCmd:56 JSON{"key":{"name":"fps.free-pointer-is-scalarized","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true}
		NopCmd
		AssumeExpCmd LNot(Lt(tacCalldatasize!!2:3 0x4 ) )
		NopCmd
		AssumeExpCmd Gt(0x40c10f19 tacSighash!!38:47 )
		NopCmd
		AssumeExpCmd LNot(Eq(0x6fdde03 tacSighash!!38:47 ) )
		NopCmd
		AssumeExpCmd LNot(Eq(0x95ea7b3 tacSighash!!38:47 ) )
		NopCmd
		AssumeExpCmd Eq(0x18160ddd tacSighash!!38:47 )
		AnnotationCmd:56 JSON{"key":{"name":"internal.func.start","type":"analysis.ip.InternalFuncStartAnnotation","erasureStrategy":"CallTrace"},"value":{"id":4,"startPc":1205,"args":[],"methodSignature":{"#class":"spec.cvlast.QualifiedMethodSignature.QualifiedMethodSig","qualifiedMethodName":{"#class":"spec.cvlast.QualifiedFunction","host":{"name":"CurveTokenExample"},"methodId":"totalSupply"},"params":[],"res":[{"#class":"spec.cvlast.VMParam.Unnamed","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256}}]},"stackOffsetToArgPos":{},"callSiteSrc":{"source":3,"begin":3954,"len":364,"jumpType":"ENTER","address":"ce4604a0000000000000000000000008","sourceContext":{"indexToFilepath":{"0":"contracts/Context.sol","1":"contracts/CurveToken.sol","2":"contracts/CurveTokenExample.sol","3":"contracts/ERC20.sol","4":"contracts/IERC20.sol","5":"contracts/IERC20Metadata.sol"},"sourceDir":".post_autofinders.0"}}}}
		AnnotationCmd:56 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet","value":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"CANON87!!29","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.scalarization.sort","type":"vc.data.ScalarizationSort","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.ScalarizationSort.Split","idx":"2"}},{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.storage.bit-width","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":256},{"key":{"name":"tac.storage.pretty.paths","type":"analysis.storage.DisplayPaths","erasureStrategy":"Erased"},"value":{"paths":[{"#class":"analysis.storage.DisplayPath.Root","name":"_totalSupply"}]}},{"key":{"name":"tac.slot.type","type":"spec.cvlast.typedescriptors.EVMTypeDescriptor$EVMValueType","erasureStrategy":"Canonical"},"value":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256}},{"key":{"name":"tac.storage.non-indexed-path","type":"analysis.storage.StorageAnalysisResult$NonIndexedPath","erasureStrategy":"Canonical"},"value":{"#class":"analysis.storage.StorageAnalysisResult.NonIndexedPath.Root","slot":"2"}},{"key":{"name":"tac.storage","type":"java.math.BigInteger","erasureStrategy":"Canonical"},"value":"ce4604a0000000000000000000000008"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1021}]},"displayPath":{"#class":"analysis.storage.DisplayPath.Root","name":"_totalSupply"},"storageType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256},"contractInstance":"ce4604a0000000000000000000000008","linkableStorageReadId":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet.Id","id":4}}}
		AnnotationCmd:56 JSON{"key":{"name":"internal.func.end","type":"analysis.ip.InternalFuncExitAnnotation","erasureStrategy":"Canonical"},"value":{"id":4,"rets":[{"s":{"namePrefix":"CANON87!!29","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.scalarization.sort","type":"vc.data.ScalarizationSort","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.ScalarizationSort.Split","idx":"2"}},{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.storage.bit-width","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":256},{"key":{"name":"tac.storage.pretty.paths","type":"analysis.storage.DisplayPaths","erasureStrategy":"Erased"},"value":{"paths":[{"#class":"analysis.storage.DisplayPath.Root","name":"_totalSupply"}]}},{"key":{"name":"tac.slot.type","type":"spec.cvlast.typedescriptors.EVMTypeDescriptor$EVMValueType","erasureStrategy":"Canonical"},"value":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256}},{"key":{"name":"tac.storage.non-indexed-path","type":"analysis.storage.StorageAnalysisResult$NonIndexedPath","erasureStrategy":"Canonical"},"value":{"#class":"analysis.storage.StorageAnalysisResult.NonIndexedPath.Root","slot":"2"}},{"key":{"name":"tac.storage","type":"java.math.BigInteger","erasureStrategy":"Canonical"},"value":"ce4604a0000000000000000000000008"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1023}]},"offset":0}],"functionLayout":{"0":{"#class":"analysis.ip.InternalFuncValueLocation.Scalar"}}}}
		AnnotationCmd:56 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.EVMFunctionReturnWrite","returnbufOffset":"0","returnValueSym":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"CANON87!!29","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.scalarization.sort","type":"vc.data.ScalarizationSort","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.ScalarizationSort.Split","idx":"2"}},{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.storage.bit-width","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":256},{"key":{"name":"tac.storage.pretty.paths","type":"analysis.storage.DisplayPaths","erasureStrategy":"Erased"},"value":{"paths":[{"#class":"analysis.storage.DisplayPath.Root","name":"_totalSupply"}]}},{"key":{"name":"tac.slot.type","type":"spec.cvlast.typedescriptors.EVMTypeDescriptor$EVMValueType","erasureStrategy":"Canonical"},"value":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256}},{"key":{"name":"tac.storage.non-indexed-path","type":"analysis.storage.StorageAnalysisResult$NonIndexedPath","erasureStrategy":"Canonical"},"value":{"#class":"analysis.storage.StorageAnalysisResult.NonIndexedPath.Root","slot":"2"}},{"key":{"name":"tac.storage","type":"java.math.BigInteger","erasureStrategy":"Canonical"},"value":"ce4604a0000000000000000000000008"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1023}]},"callIndex":4}}
		AnnotationCmd:56 JSON{"key":{"name":"tac.return.path","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		LabelCmd:56 "End procedure CurveTokenExample-totalSupply()"
		AssignExpCmd:56 tacReturndata!!231:78 Store(tacReturndata!!449:78 0x0 CANON87!!29:104 )
		AssignExpCmd:56 tacMCANON2!!232:9 Store(tacMCANON2!!446:9 0x140 CANON87!!29:104 )
		AnnotationCmd:56 JSON{"key":{"name":"call.trace.pop","type":"analysis.icfg.Inliner$CallStack$PopRecord","erasureStrategy":"Canonical"},"value":"rO0ABXNyAClhbmFseXNpcy5pY2ZnLklubGluZXIkQ2FsbFN0YWNrJFBvcFJlY29yZPAPfwSLdCWJAgABSQAIY2FsbGVlSWR4cAAAAAQ="}
		JumpCmd:56 3_0_0_1_0_0
	}
	Block 0_0_0_9_0_0 Succ [0_0_0_10_0_0] {
		AnnotationCmd:105 JSON{"key":{"name":"call.trace.push","type":"analysis.icfg.Inliner$CallStack$PushRecord","erasureStrategy":"Canonical"},"value":"rO0ABXNyACphbmFseXNpcy5pY2ZnLklubGluZXIkQ2FsbFN0YWNrJFB1c2hSZWNvcmSX8+DCTLCH+AIAA0kACGNhbGxlZUlkTAAGY2FsbGVldAATTHZjL2RhdGEvTWV0aG9kUmVmO0wAB3N1bW1hcnl0ABVMdmMvZGF0YS9DYWxsU3VtbWFyeTt4cAAAAAlzcgARdmMuZGF0YS5NZXRob2RSZWbJlJTzzU9pGAIAA0wABGF0dHJ0ABdMc2NlbmUvTWV0aG9kQXR0cmlidXRlO0wACmNvbnRyYWN0SWR0ABZMamF2YS9tYXRoL0JpZ0ludGVnZXI7TAAHc2lnSGFzaHQAEExldm0vU2lnaGFzaEludDt4cHNyABxzY2VuZS5NZXRob2RBdHRyaWJ1dGUkQ29tbW9uNHjdebdr9XMCAAB4cgAVc2NlbmUuTWV0aG9kQXR0cmlidXRlcYg2pYWutuUCAAB4cHNyABRqYXZhLm1hdGguQmlnSW50ZWdlcoz8nx+pO/sdAwAGSQAIYml0Q291bnRJAAliaXRMZW5ndGhJABNmaXJzdE5vbnplcm9CeXRlTnVtSQAMbG93ZXN0U2V0Qml0SQAGc2lnbnVtWwAJbWFnbml0dWRldAACW0J4cgAQamF2YS5sYW5nLk51bWJlcoaslR0LlOCLAgAAeHD///////////////7////+AAAAAXVyAAJbQqzzF/gGCFTgAgAAeHAAAAAQzkYEoAAAAAAAAAAAAAAAKHhzcgAOZXZtLlNpZ2hhc2hJbnRUdcqNMXEgeAIAAUwAAW5xAH4ABnhwc3EAfgAM///////////////+/////gAAAAF1cQB+ABAAAAAE4lql+nhw"}
		AssignHavocCmd:105 tacCalldatasize!!233:3
		NopCmd
		AssumeExpCmd Apply(add_noofl:bif 0x4 0x0)
		NopCmd
		AssumeExpCmd Eq(0x4 tacCalldatasize!!233:3 )
		AssignExpCmd:105 B237 LAnd(Ge(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff CANON28:32 ) Le(0x0 CANON28:32 ) )
		AssertCmd:105 B237 "sanity bounds check on cvl to vm encoding of tacTmp!5085:int failed"
		AssignExpCmd:105 R238:54 Apply(safe_math_narrow:bif CANON28:32)
		NopCmd
		AssumeExpCmd LAnd(Le(R238:57 0xffffffffffffffffffffffffffffffffffffffff ) Ge(R238:57 0x0 ) )
		AssignExpCmd:105 B242 LAnd(Ge(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff CANON29:33 ) Le(0x0 CANON29:33 ) )
		AssertCmd:105 B242 "sanity bounds check on cvl to vm encoding of tacTmp!5088:int failed"
		AssignExpCmd:105 R243:54 Apply(safe_math_narrow:bif CANON29:33)
		NopCmd
		AssumeExpCmd LAnd(Le(R243:58 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff ) Ge(R243:58 0x0 ) )
		AssignExpCmd:105 B248 LAnd(Ge(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff CANON30:34 ) Le(0x0 CANON30:34 ) )
		AssertCmd:105 B248 "sanity bounds check on cvl to vm encoding of tacTmp!5092:int failed"
		AssignExpCmd:105 R249:54 Apply(safe_math_narrow:bif CANON30:34)
		NopCmd
		AssumeExpCmd LAnd(Le(R249:59 0xffffffffffffffffffffffffffffffffffffffff ) Ge(R249:59 0x0 ) )
		AssignExpCmd:105 B253 LAnd(Ge(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff CANON34:38 ) Le(0x0 CANON34:38 ) )
		AssertCmd:105 B253 "sanity bounds check on cvl to vm encoding of tacTmp!5095:int failed"
		AssignExpCmd:105 R254:54 Apply(safe_math_narrow:bif CANON34:38)
		NopCmd
		AssumeExpCmd LAnd(Le(R254:60 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff ) Ge(R254:60 0x0 ) )
		AssignExpCmd:105 B258 LAnd(Ge(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff CANON35:39 ) Le(0x0 CANON35:39 ) )
		AssertCmd:105 B258 "sanity bounds check on cvl to vm encoding of tacTmp!5098:int failed"
		AssignExpCmd:105 R259:54 Apply(safe_math_narrow:bif CANON35:39)
		NopCmd
		AssumeExpCmd LAnd(Le(R259:61 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff ) Ge(R259:61 0x0 ) )
		AssignExpCmd:105 B263 LAnd(Ge(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff CANON29:33 ) Le(0x0 CANON29:33 ) )
		AssertCmd:105 B263 "sanity bounds check on cvl to vm encoding of tacTmp!5101:int failed"
		AssignExpCmd:105 R264:54 Apply(safe_math_narrow:bif CANON29:33)
		AssignExpCmd:105 B266 LAnd(Ge(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff CANON28:32 ) Le(0x0 CANON28:32 ) )
		AssertCmd:105 B266 "sanity bounds check on cvl to vm encoding of tacTmp!5104:int failed"
		AssignExpCmd:105 R267:54 Apply(safe_math_narrow:bif CANON28:32)
		AssignExpCmd:105 R270:54 Select(tacBalance!!513:16 Apply(to_skey:bif R267:54) )
		AssignExpCmd:106 I271:54 IntSub(R270:54 R264:54 )
		AssignExpCmd:106 tacBalance!!272:16 Store(tacBalance!!513:16 Apply(to_skey:bif R267:54) I271:54 )
		AssignExpCmd:105 R273:54 Select(tacBalance!!272:16 Apply(to_skey:bif R34:46) )
		AssignExpCmd:106 R274:54 Add(R273:54 R264:54)
		NopCmd
		AssumeExpCmd Apply(add_noofl:bif R273:54 R264:54)
		AssignExpCmd:106 tacBalance!!276:16 Store(tacBalance!!272:16 Apply(to_skey:bif R34:46) R274:54 )
		AnnotationCmd:105 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.BalanceSnippet","srcAccountInfo":{"old":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R270","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}]},"new":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"I271","tag":{"#class":"tac.Tag.Int"},"callIndex":0,"meta":[{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}]},"addr":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R267","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}]}},"trgAccountInfo":{"old":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R273","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}]},"new":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R274","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}]},"addr":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R34","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"tacContractAt"},{"key":{"name":"tac.contract.sym.addr.name","type":"java.lang.String","erasureStrategy":"Erased"},"value":"curve"},{"key":{"name":"tac.contract.sym.addr","type":"java.math.BigInteger","erasureStrategy":"Erased"},"value":"ce4604a0000000000000000000000028"}]}},"transferredAmount":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R264","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}]}}}
		LabelCmd:105 "Start procedure curve-getVirtualPrice()"
		AnnotationCmd:105 JSON{"key":{"name":"fps.free-pointer-is-scalarized","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true}
		AssignExpCmd:105 R277:54 Select(tacExtcodesize!!9:4 Apply(to_skey:bif R34:63) )
		NopCmd
		AssumeExpCmd Gt(R277:54 0x0 )
		AnnotationCmd:105 JSON{"key":{"name":"internal.func.finder.info","type":"analysis.ip.InternalFunctionFinderReport","erasureStrategy":"Erased"},"value":"rO0ABXNyAChhbmFseXNpcy5pcC5JbnRlcm5hbEZ1bmN0aW9uRmluZGVyUmVwb3J0ian+bYn1VdACAAFMABN1bnJlc29sdmVkRnVuY3Rpb25zdAAPTGphdmEvdXRpbC9TZXQ7eHBzcgAhZGF0YXN0cnVjdHVyZXMuTGlua2VkQXJyYXlIYXNoU2V0AAAAAAAAAAEDAAJGAApsb2FkRmFjdG9yTAAJaGFzaFRhYmxldAAuTGRhdGFzdHJ1Y3R1cmVzL2FycmF5aGFzaHRhYmxlL0FycmF5SGFzaFRhYmxlO3hwdwgAAAAAQAAAAHg="}
		AnnotationCmd:105 JSON{"key":{"name":"fps.free-pointer-is-scalarized","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true}
		NopCmd
		AssumeExpCmd Eq(R243:54 0x0 )
		NopCmd
		AssumeExpCmd LNot(Lt(tacCalldatasize!!233:3 0x4 ) )
		NopCmd
		AssumeExpCmd LNot(Gt(0x82c63066 tacSighash!!43:47 ) )
		NopCmd
		AssumeExpCmd LNot(Eq(0x82c63066 tacSighash!!43:47 ) )
		NopCmd
		AssumeExpCmd LNot(Eq(0x89295a45 tacSighash!!43:47 ) )
		NopCmd
		AssumeExpCmd LNot(Eq(0x9d1e1f25 tacSighash!!43:47 ) )
		NopCmd
		AssumeExpCmd LNot(Eq(0xac8c9059 tacSighash!!43:47 ) )
		NopCmd
		AssumeExpCmd LNot(Eq(0xd802e4f7 tacSighash!!43:47 ) )
		NopCmd
		AssumeExpCmd Eq(0xe25aa5fa tacSighash!!43:47 )
		AnnotationCmd:105 JSON{"key":{"name":"internal.func.start","type":"analysis.ip.InternalFuncStartAnnotation","erasureStrategy":"CallTrace"},"value":{"id":11,"startPc":2909,"args":[],"methodSignature":{"#class":"spec.cvlast.QualifiedMethodSignature.QualifiedMethodSig","qualifiedMethodName":{"#class":"spec.cvlast.QualifiedFunction","host":{"name":"curve"},"methodId":"getVirtualPrice"},"params":[],"res":[{"#class":"spec.cvlast.VMParam.Unnamed","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256}}]},"stackOffsetToArgPos":{},"callSiteSrc":{"source":7,"begin":5992,"len":476,"jumpType":"ENTER","address":"ce4604a0000000000000000000000028","sourceContext":{"indexToFilepath":{"0":"contracts/Context.sol","1":"contracts/CurveToken.sol","2":"contracts/CurveTokenExample.sol","3":"contracts/ERC20.sol","4":"contracts/IERC20.sol","5":"contracts/IERC20Metadata.sol","6":"contracts/ReentrancyGuard.sol","7":"contracts/curve.sol"},"sourceDir":".post_autofinders.2"}}}}
		AnnotationCmd:105 JSON{"key":{"name":"pta.end-allocation","type":"analysis.alloc.AllocationAnalysis$AbstractLocation","erasureStrategy":"Erased"},"value":{"prevFPWriteIdx":0,"nextFPWriteCmd":{"block":{"#class":"tac.BlockIdentifier","origStartPc":16,"stkTop":1024,"decompCopy":0,"calleeIdx":0,"topOfStackValue":2,"freshCopy":0},"pos":34},"sort":{"#class":"analysis.alloc.AllocationAnalysis.Alloc.ConstBlock","sz":"40"}}}
		AssignExpCmd:107 R289:65 Select(CANON77!!28:40 Apply(skey_basic:bif 0x8) )
		AnnotationCmd:105 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet","value":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R289","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1012}]},"displayPath":{"#class":"analysis.storage.DisplayPath.ArrayAccess","index":{"#class":"vc.data.TACSymbol.Const","value":"0"},"base":{"#class":"analysis.storage.DisplayPath.Root","name":"admin_balances"}},"storageType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256},"contractInstance":"ce4604a0000000000000000000000028","linkableStorageReadId":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet.None"}}}
		AssignExpCmd:108 R290:67 Select(tacBalance!!276:16 Apply(to_skey:bif R34:63) )
		NopCmd
		AssumeExpCmd LNot(Lt(R290:67 R289:65 ) )
		AssignExpCmd:109 R292:69 Sub(R290:67 R289:65 )
		AssignExpCmd:110 tacMCANON1!!293:8 Store(tacMCANON1!!12:8 0xc0 R292:69 )
		AssignExpCmd:111 R294:72 Select(CANON77!!28:40 Apply(skey_basic:bif 0x9) )
		AnnotationCmd:105 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet","value":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R294","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1013}]},"displayPath":{"#class":"analysis.storage.DisplayPath.ArrayAccess","index":{"#class":"vc.data.TACSymbol.Const","value":"1"},"base":{"#class":"analysis.storage.DisplayPath.Root","name":"admin_balances"}},"storageType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256},"contractInstance":"ce4604a0000000000000000000000028","linkableStorageReadId":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet.None"}}}
		AssignExpCmd:105 B296:54 Le(CANON18!!24:73 0xffffffffffffffffffffffffffffffffffffffff )
		AssignExpCmd:105 B297:54 Ge(CANON18!!24:73 0x0 )
		NopCmd
		AssumeExpCmd LAnd(B296:54 B297:54 )
		AnnotationCmd:105 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet","value":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"CANON18!!24","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.scalarization.sort","type":"vc.data.ScalarizationSort","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.ScalarizationSort.Packed","packedStart":{"#class":"vc.data.ScalarizationSort.Split","idx":"b"},"start":0}},{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.storage.bit-width","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":160},{"key":{"name":"tac.storage.pretty.paths","type":"analysis.storage.DisplayPaths","erasureStrategy":"Erased"},"value":{"paths":[{"#class":"analysis.storage.DisplayPath.Root","name":"coins_1"}]}},{"key":{"name":"tac.slot.type","type":"spec.cvlast.typedescriptors.EVMTypeDescriptor$EVMValueType","erasureStrategy":"Canonical"},"value":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.address"}},{"key":{"name":"tac.storage.non-indexed-path","type":"analysis.storage.StorageAnalysisResult$NonIndexedPath","erasureStrategy":"Canonical"},"value":{"#class":"analysis.storage.StorageAnalysisResult.NonIndexedPath.Root","slot":"b"}},{"key":{"name":"tac.storage","type":"java.math.BigInteger","erasureStrategy":"Canonical"},"value":"ce4604a0000000000000000000000028"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1011}]},"displayPath":{"#class":"analysis.storage.DisplayPath.Root","name":"coins_1"},"storageType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.address"},"contractInstance":"ce4604a0000000000000000000000028","linkableStorageReadId":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet.Id","id":10}}}
		AnnotationCmd:105 JSON{"key":{"name":"init.reorder.fence","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		AssignExpCmd:112 tacMCANON2!!300:10 Store(tacMCANON2!!14:10 0x100 0x70a0823100000000000000000000000000000000000000000000000000000000 )
		AssignExpCmd:113 tacMCANON2!!302:10 Store(tacMCANON2!!300:10 0x104 R34:46 )
		AssignExpCmd:112 R303:76 0x100
		AssignHavocCmd:112 R304:77
		AssignHavocCmd:105 tacReturndata!!305:78
		JumpCmd:105 0_0_0_10_0_0
	}
	Block 0_0_0_10_0_0 Succ [1_0_0_9_0_0] {
		AnnotationCmd:105 JSON{"key":{"name":"call.trace.push","type":"analysis.icfg.Inliner$CallStack$PushRecord","erasureStrategy":"Canonical"},"value":"rO0ABXNyACphbmFseXNpcy5pY2ZnLklubGluZXIkQ2FsbFN0YWNrJFB1c2hSZWNvcmSX8+DCTLCH+AIAA0kACGNhbGxlZUlkTAAGY2FsbGVldAATTHZjL2RhdGEvTWV0aG9kUmVmO0wAB3N1bW1hcnl0ABVMdmMvZGF0YS9DYWxsU3VtbWFyeTt4cAAAAApzcgARdmMuZGF0YS5NZXRob2RSZWbJlJTzzU9pGAIAA0wABGF0dHJ0ABdMc2NlbmUvTWV0aG9kQXR0cmlidXRlO0wACmNvbnRyYWN0SWR0ABZMamF2YS9tYXRoL0JpZ0ludGVnZXI7TAAHc2lnSGFzaHQAEExldm0vU2lnaGFzaEludDt4cHNyABxzY2VuZS5NZXRob2RBdHRyaWJ1dGUkQ29tbW9uNHjdebdr9XMCAAB4cgAVc2NlbmUuTWV0aG9kQXR0cmlidXRlcYg2pYWutuUCAAB4cHNyABRqYXZhLm1hdGguQmlnSW50ZWdlcoz8nx+pO/sdAwAGSQAIYml0Q291bnRJAAliaXRMZW5ndGhJABNmaXJzdE5vbnplcm9CeXRlTnVtSQAMbG93ZXN0U2V0Qml0SQAGc2lnbnVtWwAJbWFnbml0dWRldAACW0J4cgAQamF2YS5sYW5nLk51bWJlcoaslR0LlOCLAgAAeHD///////////////7////+AAAAAXVyAAJbQqzzF/gGCFTgAgAAeHAAAAAQzkYEoAAAAAAAAAAAAAAAEXhzcgAOZXZtLlNpZ2hhc2hJbnRUdcqNMXEgeAIAAUwAAW5xAH4ABnhwc3EAfgAM///////////////+/////gAAAAF1cQB+ABAAAAAEcKCCMXhzcgATdmMuZGF0YS5DYWxsU3VtbWFyeZQcmw5vl+FdAgAQSQAJc3VtbWFyeUlkTAAOY2FsbENvbnZlbnRpb250ACZMaW5zdHJ1bWVudGF0aW9uL2NhbGxzL0NhbGxDb252ZW50aW9uO0wACmNhbGxUYXJnZXR0ABpMYW5hbHlzaXMvaWNmZy9DYWxsVGFyZ2V0O0wACGNhbGxUeXBldAAVTHZjL2RhdGEvVEFDQ2FsbFR5cGU7TAAPY2Fubm90QmVJbmxpbmVkdAAtTGFuYWx5c2lzL2ljZmcvSW5saW5lciRJbGxlZ2FsSW5saW5pbmdSZWFzb247TAAGZ2FzVmFydAATTHZjL2RhdGEvVEFDU3ltYm9sO0wABmluQmFzZXEAfgAbTAAIaW5PZmZzZXRxAH4AG0wABmluU2l6ZXEAfgAbTAAMb3JpZ0NhbGxjb3JldAAgTHZjL2RhdGEvVEFDQ21kJFNpbXBsZSRDYWxsQ29yZTtMAAdvdXRCYXNlcQB+ABtMAAlvdXRPZmZzZXRxAH4AG0wAB291dFNpemVxAH4AG0wADXNpZ1Jlc29sdXRpb250AA9MamF2YS91dGlsL1NldDtMAAV0b1ZhcnEAfgAbTAAIdmFsdWVWYXJxAH4AG3hwAAAABnNyACRpbnN0cnVtZW50YXRpb24uY2FsbHMuQ2FsbENvbnZlbnRpb25HtO1ulL788QIAA0kACGNhbGxlcklkTAAFaW5wdXR0ABlMYW5hbHlzaXMvaWNmZy9DYWxsSW5wdXQ7TAAGcmF3T3V0dAAiTGluc3RydW1lbnRhdGlvbi9jYWxscy9DYWxsT3V0cHV0O3hwAAAAAHNyABdhbmFseXNpcy5pY2ZnLkNhbGxJbnB1dJjJD1MhNUxQAgAHTAAHYmFzZVZhcnQAGUx2Yy9kYXRhL1RBQ0V4cHIkU3ltJFZhcjtMABBlbmNvZGVkQXJndW1lbnRzdAAjTGFuYWx5c2lzL2ljZmcvQUJJQXJndW1lbnRFbmNvZGluZztMABNpbnB1dFNpemVMb3dlckJvdW5kcQB+AAZMAAZvZmZzZXR0ABVMdmMvZGF0YS9UQUNFeHByJFN5bTtMABRyYW5nZVRvRGVjb21wb3NlZEFyZ3QAD0xqYXZhL3V0aWwvTWFwO0wAEHNpbXBsaWZpZWRPZmZzZXR0ABtMdmMvZGF0YS9UQUNFeHByJFN5bSRDb25zdDtMAARzaXplcQB+ACZ4cHNyABd2Yy5kYXRhLlRBQ0V4cHIkU3ltJFZhcskrg43eGgPnAgACTAABc3QAF0x2Yy9kYXRhL1RBQ1N5bWJvbCRWYXI7TAADdGFndAAJTHRhYy9UYWc7eHIAE3ZjLmRhdGEuVEFDRXhwciRTeW2iVj0S4YSNUAIAAHhyAA92Yy5kYXRhLlRBQ0V4cHJYhGlUu/v+yAIAAHhwc3IANnZjLmRhdGEuVEFDU3ltYm9sJFZhciRXaXRoRGVmYXVsdENhbGxJbmRleCRXaXRoQnl0ZU1hcJ7+oHF4CHAAAgACTAAEbWV0YXQALUxrb3RsaW54L2NvbGxlY3Rpb25zL2ltbXV0YWJsZS9QZXJzaXN0ZW50TWFwO0wACm5hbWVQcmVmaXh0ABJMamF2YS9sYW5nL1N0cmluZzt4cgAVdmMuZGF0YS5UQUNTeW1ib2wkVmFyCYrCGVl9SXYCAAB4cgARdmMuZGF0YS5UQUNTeW1ib2zd3Run/CoWswIAAHhwc3IAJmRhdGFzdHJ1Y3R1cmVzLnRyZWFwLkhhc2hUcmVhcE1hcCROb2Rlf2t9acJIPnQCAANMAANrZXl0ABJMamF2YS9sYW5nL09iamVjdDtMAARuZXh0dAA1TGRhdGFzdHJ1Y3R1cmVzL3RyZWFwL0hhc2hUcmVhcE1hcCRNb3JlS2V5VmFsdWVQYWlycztMAAV2YWx1ZXEAfgA3eHIAIWRhdGFzdHJ1Y3R1cmVzLnRyZWFwLkhhc2hUcmVhcE1hcPMJ/2vt3boKAgAAeHIAHWRhdGFzdHJ1Y3R1cmVzLnRyZWFwLlRyZWFwTWFw46LAyn3v5moCAAB4cgAaZGF0YXN0cnVjdHVyZXMudHJlYXAuVHJlYXA88f21zZwbdQIAAkwABGxlZnR0ABxMZGF0YXN0cnVjdHVyZXMvdHJlYXAvVHJlYXA7TAAFcmlnaHRxAH4APHhwcHNxAH4ANnBzcQB+ADZwcHNyAAt0YWMuTWV0YUtleVF/W3MiCfIZAgADTAAPZXJhc3VyZVN0cmF0ZWd5dAAdTHRhYy9NZXRhS2V5JEVyYXN1cmVTdHJhdGVneTtMAARuYW1lcQB+ADJMAAN0eXB0ABFMamF2YS9sYW5nL0NsYXNzO3hwfnIAG3RhYy5NZXRhS2V5JEVyYXN1cmVTdHJhdGVneQAAAAAAAAAAEgAAeHIADmphdmEubGFuZy5FbnVtAAAAAAAAAAASAAB4cHQACUNhbm9uaWNhbHQAF3RhYy5tZW1vcnkucGFydGl0aW9uLWlkdnIAEWphdmEubGFuZy5JbnRlZ2VyEuKgpPeBhzgCAAFJAAV2YWx1ZXhxAH4ADnBzcQB+AEkAAAAKc3EAfgBAcQB+AEZ0ABJUYWMuc3ltYm9sLmtleXdvcmR2cgAQamF2YS5sYW5nLlN0cmluZ6DwpDh6O7NCAgAAeHBwdAAEdGFjTXNxAH4AQHEAfgBGdAANdGFjLmlzLm1lbW9yeXZyACJ0YWMuTWV0YU1hcCRDb21wYW5pb24kTm90aGluZ1ZhbHVl8nsHH85ykpUCAAB4cHBzcQB+AFN0AA90YWNNQ0FOT04yISEzMDJzcgAPdGFjLlRhZyRCeXRlTWFwNb/Ry6GDRgkCAAB4cgALdGFjLlRhZyRNYXABJytzDV3P/QIAAHhyAAd0YWMuVGFnLk9V3gn2xngCAAB4cHBzcQB+AAz///////////////7////+AAAAAXVxAH4AEAAAAAEkeHNxAH4AKnNyADV2Yy5kYXRhLlRBQ1N5bWJvbCRWYXIkV2l0aERlZmF1bHRDYWxsSW5kZXgkV2l0aEJpdDI1NnqsyEgq0drPAgACTAAEbWV0YXEAfgAxTAAKbmFtZVByZWZpeHEAfgAyeHEAfgAzc3EAfgA2c3EAfgA2cHBxAH4ATHB0AAFMcHNxAH4AQHEAfgBGdAAQdGFjLnN0YWNrLmhlaWdodHEAfgBKcHNxAH4ASQAAA/B0AARSMzAzc3IADnRhYy5UYWckQml0MjU2IyLQT+LlKkgCAAB4cQB+AFlzcgARamF2YS51dGlsLkhhc2hNYXAFB9rBwxZg0QMAAkYACmxvYWRGYWN0b3JJAAl0aHJlc2hvbGR4cD9AAAAAAAADdwgAAAAEAAAAAnNyAB5hbmFseXNpcy5pY2ZnLlNjcmF0Y2hCeXRlUmFuZ2XBTLaPpUzj2gIAAkwABGZyb21xAH4ABkwAAnRvcQB+AAZ4cHNxAH4ADP///////////////v////4AAAAAdXEAfgAQAAAAAHhzcQB+AAz///////////////7////+AAAAAXVxAH4AEAAAAAEDeHNyAC1hbmFseXNpcy5pY2ZnLkRlY29tcG9zZWRDYWxsSW5wdXRBcmckQ29uc3RhbnSFavLdQafqPQIAA0wAAWN0ABlMdmMvZGF0YS9UQUNTeW1ib2wkQ29uc3Q7TAARY29udHJhY3RSZWZlcmVuY2V0AC9MYW5hbHlzaXMvaWNmZy9DYWxsR3JhcGhCdWlsZGVyJENhbGxlZENvbnRyYWN0O0wADHNjcmF0Y2hSYW5nZXQAIExhbmFseXNpcy9pY2ZnL1NjcmF0Y2hCeXRlUmFuZ2U7eHIAJGFuYWx5c2lzLmljZmcuRGVjb21wb3NlZENhbGxJbnB1dEFy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ZUNvbnRleHQ7eHBwc3EAfgDhAAAXHwAAACcAAAAHcQB+AIZ+cgARY29tcGlsZXIuSnVtcFR5cGUAAAAAAAAAABIAAHhxAH4ARXQAB1JFR1VMQVJzcgAWY29tcGlsZXIuU291cmNlQ29udGV4dIzLW+lAXNoTAgACTAAPaW5kZXhUb0ZpbGVwYXRocQB+ACdMAAlzb3VyY2VEaXJxAH4AMnhwc3EAfgBpP0AAAAAAAAx3CAAAABAAAAAIc3EAfgBJAAAAAHQAFWNvbnRyYWN0cy9Db250ZXh0LnNvbHNxAH4ASQAAAAF0ABhjb250cmFjdHMvQ3VydmVUb2tlbi5zb2xzcQB+AEkAAAACdAAfY29udHJhY3RzL0N1cnZlVG9rZW5FeGFtcGxlLnNvbHNxAH4ASQAAAAN0ABNjb250cmFjdHMvRVJDMjAuc29sc3EAfgBJAAAABHQAFGNvbnRyYWN0cy9JRVJDMjAuc29sc3EAfgBJAAAABXQAHGNvbnRyYWN0cy9JRVJDMjBNZXRhZGF0YS5zb2xzcQB+AEkAAAAGdAAdY29udHJhY3RzL1JlZW50cmFuY3lHdWFyZC5zb2xzcQB+AEkAAAAHdAATY29udHJhY3RzL2N1cnZlLnNvbHh0ABMucG9zdF9hdXRvZmluZGVycy4yc3EAfgAwc3EAfgA2cHNxAH4ANnBzcQB+ADZwcHEAfgBDcHEAfgBLcQB+AExwcQB+AFBxAH4AUXBxAH4AVXEAfgBWc3EAfgBec3EAfgA2c3EAfgA2cHBxAH4ATHBxAH4AYnBxAH4AY3BxAH4Ar3EAfgBmcQB+ALJzcQB+AF5zcQB+ADZzcQB+ADZzcQB+ADZzcQB+ADZwc3EAfgA2cHBxAH4ATHBxAH4AYnNxAH4AQHEAfgBGdAAWdGFjLnNjYWxhcml6YXRpb24uc29ydHZyABl2Yy5kYXRhLlNjYWxhcml6YXRpb25Tb3J0MM5wneRoDSYCAAB4cHBzcgAgdmMuZGF0YS5TY2FsYXJpemF0aW9uU29ydCRQYWNrZWQuRa0Sk4jk9wIAAkkABXN0YXJ0TAALcGFja2VkU3RhcnR0ABtMdmMvZGF0YS9TY2FsYXJpemF0aW9uU29ydDt4cQB+AQwAAAAAc3IAH3ZjLmRhdGEuU2NhbGFyaXphdGlvblNvcnQkU3BsaXRU/1mn8ceyBQIAAUwAA2lkeHEAfgAGeHEAfgEMc3EAfgAM///////////////+/////gAAAAF1cQB+ABAAAAABC3hzcQB+ADZwc3EAfgA2cHNxAH4ANnBwc3EAfgBAcQB+AEZ0ABx0YWMuc3RvcmFnZS5ub24taW5kZXhlZC1wYXRodnIANWFuYWx5c2lzLnN0b3JhZ2UuU3RvcmFnZUFuYWx5c2lzUmVzdWx0JE5vbkluZGV4ZWRQYXRoCMGgS6H6P0UCAAB4cHBzcgA6YW5hbHlzaXMuc3RvcmFnZS5TdG9yYWdlQW5hbHlzaXNSZXN1bHQkTm9uSW5kZXhlZFBhdGgkUm9vdL839dil6gr/AgABTAAEc2xvdHEAfgAGeHEAfgEacQB+ARNzcQB+AEBxAH4ARnQADXRhYy5zbG90LnR5cGV2cgA6c3BlYy5jdmxhc3QudHlwZWRlc2NyaXB0b3JzLkVWTVR5cGVEZXNjcmlwdG9yJEVWTVZhbHVlVHlwZcaJrwK66rglAgAAeHIALXNwZWMuY3ZsYXN0LnR5cGVkZXNjcmlwdG9ycy5FVk1UeXBlRGVzY3JpcHRvcshRqfE8wmodAgAAeHBwc3IANXNwZWMuY3ZsYXN0LnR5cGVkZXNjcmlwdG9ycy5FVk1UeXBlRGVzY3JpcHRvciRhZGRyZXNzevhl9G+XoCkCAAB4cgBEc3BlYy5jdmxhc3QudHlwZWRlc2NyaXB0b3JzLkVWTVR5cGVEZXNjcmlwdG9yJEVWTUlzb21vcnBoaWNWYWx1ZVR5cGX3dZiRbhChDwIAAHhxAH4BIHNxAH4AQHEAfgCPdAAYdGFjLnN0b3JhZ2UucHJldHR5LnBhdGhzdnIAHWFuYWx5c2lzLnN0b3JhZ2UuRGlzcGxheVBhdGhz90RLt8P1URYCAAFMAAVwYXRoc3EAfgAdeHBwc3EAfgEoc3IAF2phdmEudXRpbC5MaW5rZWRIYXNoU2V02GzXWpXdKh4CAAB4cgARamF2YS51dGlsLkhhc2hTZXS6RIWVlri3NAMAAHhwdwwAAAAQP0AAAAAAAAFzcgAhYW5hbHlzaXMuc3RvcmFnZS5EaXNwbGF5UGF0aCRSb29003OgvZnQPHICAAJMAARiYXNldAAeTGFuYWx5c2lzL3N0b3JhZ2UvRGlzcGxheVBhdGg7TAAEbmFtZXEAfgAyeHIAHGFuYWx5c2lzLnN0b3JhZ2UuRGlzcGxheVBhdGhPQGPqVtIgBQIAAHhwcHQAB2NvaW5zXzF4c3EAfgBAcQB+AEZ0ABV0YWMuc3RvcmFnZS5iaXQtd2lkdGhxAH4ASnBzcQB+AEkAAACgcHNxAH4AQHEAfgBGdAALdGFjLnN0b3JhZ2VxAH4AlXBxAH4AhnBxAH4AY3BzcQB+AEkAAAP0dAALQ0FOT04xOCEhMjRzcQB+AHdxAH4AaHEAfgBtc3EAfgAwc3EAfgA2cHNxAH4ANnBzcQB+ADZwcHEAfgBDcHEAfgBLcQB+AExwcQB+AFBxAH4AUXBxAH4AVXEAfgBWc3EAfgBec3EAfgA2c3EAfgA2cHBxAH4ATHBxAH4AYnBxAH4AY3BxAH4Ar3EAfgBmcQB+ALJzcgAiamF2YS51dGlsLkNvbGxlY3Rpb25zJFNpbmdsZXRvblNldCxSQZgpwLG/AgABTAAHZWxlbWVudHEAfgA3eHBxAH4AFHNxAH4AXnNxAH4ANnNxAH4ANnNxAH4ANnNxAH4ANnBzcQB+ADZwcHEAfgBMcHEAfgBicQB+AQpwcQB+ARBzcQB+ADZwc3EAfgA2cHNxAH4ANnBwcQB+ARhwcQB+AR1xAH4BHnBxAH4BJXEAfgEmcHNxAH4BKHNxAH4BK3cMAAAAED9AAAAAAAABcQB+ATF4cQB+ATNwcQB+ATVwcQB+ATZwcQB+AIZwcQB+AGNwcQB+AThxAH4BOXNxAH4Ad3EAfgBocQB+AG0="}
		AnnotationCmd:105 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageGlobalChangeSnippet.StorageBackupPoint","calleeTxId":10}}
		NopCmd
		AssumeExpCmd LAnd(Eq(tacCalldatasize!!6:3 0x24 ) Eq(tacCalldatasize!!6:3 0x24 ) )
		NopCmd
		AssumeExpCmd Eq(tacCalldatabufCANON0@10:2 0x70a0823100000000000000000000000000000000000000000000000000000000 )
		AssignExpCmd:105 tacCalldatabufCANON1@10:114 R34:80
		LabelCmd:105 "Start procedure ERC20-balanceOf(address)"
		AnnotationCmd:105 JSON{"key":{"name":"fps.free-pointer-is-scalarized","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true}
		AssignExpCmd:105 R309:54 Select(tacExtcodesize!!9:4 Apply(to_skey:bif R33:81) )
		NopCmd
		AssumeExpCmd Gt(R309:54 0x0 )
		AnnotationCmd:105 JSON{"key":{"name":"internal.func.finder.info","type":"analysis.ip.InternalFunctionFinderReport","erasureStrategy":"Erased"},"value":"rO0ABXNyAChhbmFseXNpcy5pcC5JbnRlcm5hbEZ1bmN0aW9uRmluZGVyUmVwb3J0ian+bYn1VdACAAFMABN1bnJlc29sdmVkRnVuY3Rpb25zdAAPTGphdmEvdXRpbC9TZXQ7eHBzcgAhZGF0YXN0cnVjdHVyZXMuTGlua2VkQXJyYXlIYXNoU2V0AAAAAAAAAAEDAAJGAApsb2FkRmFjdG9yTAAJaGFzaFRhYmxldAAuTGRhdGFzdHJ1Y3R1cmVzL2FycmF5aGFzaHRhYmxlL0FycmF5SGFzaFRhYmxlO3hwdwgAAAAAQAAAAHg="}
		AnnotationCmd:105 JSON{"key":{"name":"fps.free-pointer-is-scalarized","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true}
		NopCmd
		AssumeExpCmd LNot(Lt(tacCalldatasize!!6:3 0x4 ) )
		NopCmd
		AssumeExpCmd LNot(Gt(0x39509351 tacSighash!!44:47 ) )
		NopCmd
		AssumeExpCmd LNot(Eq(0x39509351 tacSighash!!44:47 ) )
		NopCmd
		AssumeExpCmd Eq(0x70a08231 tacSighash!!44:47 )
		AssignExpCmd:115 R315:83 Sub(tacCalldatasize!!6:3 0x4 )
		AssignExpCmd:105 B316:84 Slt(R315:83 0x20 )
		NopCmd
		AssumeExpCmd LNot(B316:84 )
		AssignExpCmd:116 R318:72 tacCalldatabufCANON1@10:117
		NopCmd
		AssumeExpCmd Eq(R34:80 R34:80 )
		AnnotationCmd:105 JSON{"key":{"name":"internal.func.start","type":"analysis.ip.InternalFuncStartAnnotation","erasureStrategy":"CallTrace"},"value":{"id":12,"startPc":1712,"args":[{"s":{"namePrefix":"R318","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1013}]},"offset":1,"sort":"SCALAR"}],"methodSignature":{"#class":"spec.cvlast.QualifiedMethodSignature.QualifiedMethodSig","qualifiedMethodName":{"#class":"spec.cvlast.QualifiedFunction","host":{"name":"ERC20"},"methodId":"balanceOf"},"params":[{"#class":"spec.cvlast.VMParam.Named","name":"account","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$address"}}],"res":[{"#class":"spec.cvlast.VMParam.Unnamed","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256}}]},"stackOffsetToArgPos":{"1":0},"callSiteSrc":{"source":1,"begin":4376,"len":467,"jumpType":"ENTER","address":"ce4604a0000000000000000000000011","sourceContext":{"indexToFilepath":{"0":"contracts/Context.sol","1":"contracts/ERC20.sol","2":"contracts/IERC20.sol","3":"contracts/IERC20Metadata.sol"},"sourceDir":".post_autofinders.1"}}}}
		AssignExpCmd:118 R323:88 Apply(hash_3_keccak:bif Apply(skey_basic:bif 0x40) Apply(to_skey:bif R34:80) Apply(skey_basic:bif 0x0))
		AssignExpCmd:119 R324:88 Select(CANON93!!30:42 R323:120 )
		AnnotationCmd:105 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet","value":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R324","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1020}]},"displayPath":{"#class":"analysis.storage.DisplayPath.MapAccess","key":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R318","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1018}]},"keyTyp":{"#class":"tac.TACStorageType.IntegralType","typeLabel":"address","numBytes":"14","descriptor":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$address"},"lowerBound":null,"upperBound":null},"base":{"#class":"analysis.storage.DisplayPath.Root","name":"_balances"}},"storageType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256},"contractInstance":"ce4604a0000000000000000000000011","linkableStorageReadId":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet.None"}}}
		AnnotationCmd:105 JSON{"key":{"name":"internal.func.end","type":"analysis.ip.InternalFuncExitAnnotation","erasureStrategy":"Canonical"},"value":{"id":12,"rets":[{"s":{"namePrefix":"R324","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1023}]},"offset":0}],"functionLayout":{"0":{"#class":"analysis.ip.InternalFuncValueLocation.Scalar"}}}}
		AnnotationCmd:105 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.EVMFunctionReturnWrite","returnbufOffset":"0","returnValueSym":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R324","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1023}]},"callIndex":10}}
		AnnotationCmd:105 JSON{"key":{"name":"tac.return.path","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		LabelCmd:105 "End procedure ERC20-balanceOf(address)"
		AssignExpCmd:105 tacReturndata!!326:78 Store(tacReturndata!!305:78 0x0 R324:88 )
		AssignExpCmd:105 tacMCANON2!!327:10 Store(tacMCANON2!!302:10 0x100 R324:88 )
		AnnotationCmd:105 JSON{"key":{"name":"call.trace.pop","type":"analysis.icfg.Inliner$CallStack$PopRecord","erasureStrategy":"Canonical"},"value":"rO0ABXNyAClhbmFseXNpcy5pY2ZnLklubGluZXIkQ2FsbFN0YWNrJFBvcFJlY29yZPAPfwSLdCWJAgABSQAIY2FsbGVlSWR4cAAAAAo="}
		JumpCmd:105 1_0_0_9_0_0
	}
	Block 0_0_0_11_0_0 Succ [2_0_0_9_0_0] {
		AnnotationCmd:105 JSON{"key":{"name":"call.trace.push","type":"analysis.icfg.Inliner$CallStack$PushRecord","erasureStrategy":"Canonical"},"value":"rO0ABXNyACphbmFseXNpcy5pY2ZnLklubGluZXIkQ2FsbFN0YWNrJFB1c2hSZWNvcmSX8+DCTLCH+AIAA0kACGNhbGxlZUlkTAAGY2FsbGVldAATTHZjL2RhdGEvTWV0aG9kUmVmO0wAB3N1bW1hcnl0ABVMdmMvZGF0YS9DYWxsU3VtbWFyeTt4cAAAAAtzcgARdmMuZGF0YS5NZXRob2RSZWbJlJTzzU9pGAIAA0wABGF0dHJ0ABdMc2NlbmUvTWV0aG9kQXR0cmlidXRlO0wACmNvbnRyYWN0SWR0ABZMamF2YS9tYXRoL0JpZ0ludGVnZXI7TAAHc2lnSGFzaHQAEExldm0vU2lnaGFzaEludDt4cHNyABxzY2VuZS5NZXRob2RBdHRyaWJ1dGUkQ29tbW9uNHjdebdr9XMCAAB4cgAVc2NlbmUuTWV0aG9kQXR0cmlidXRlcYg2pYWutuUCAAB4cHNyABRqYXZhLm1hdGguQmlnSW50ZWdlcoz8nx+pO/sdAwAGSQAIYml0Q291bnRJAAliaXRMZW5ndGhJABNmaXJzdE5vbnplcm9CeXRlTnVtSQAMbG93ZXN0U2V0Qml0SQAGc2lnbnVtWwAJbWFnbml0dWRldAACW0J4cgAQamF2YS5sYW5nLk51bWJlcoaslR0LlOCLAgAAeHD///////////////7////+AAAAAXVyAAJbQqzzF/gGCFTgAgAAeHAAAAAQzkYEoAAAAAAAAAAAAAAAKHhzcgAOZXZtLlNpZ2hhc2hJbnRUdcqNMXEgeAIAAUwAAW5xAH4ABnhwc3EAfgAM///////////////+/////gAAAAF1cQB+ABAAAAAEOEL3dnhzcgATdmMuZGF0YS5DYWxsU3VtbWFyeZQcmw5vl+FdAgAQSQAJc3VtbWFyeUlkTAAOY2FsbENvbnZlbnRpb250ACZMaW5zdHJ1bWVudGF0aW9uL2NhbGxzL0NhbGxDb252ZW50aW9uO0wACmNhbGxUYXJnZXR0ABpMYW5hbHlzaXMvaWNmZy9DYWxsVGFyZ2V0O0wACGNhbGxUeXBldAAVTHZjL2RhdGEvVEFDQ2FsbFR5cGU7TAAPY2Fubm90QmVJbmxpbmVkdAAtTGFuYWx5c2lzL2ljZmcvSW5saW5lciRJbGxlZ2FsSW5saW5pbmdSZWFzb247TAAGZ2FzVmFydAATTHZjL2RhdGEvVEFDU3ltYm9sO0wABmluQmFzZXEAfgAbTAAIaW5PZmZzZXRxAH4AG0wABmluU2l6ZXEAfgAbTAAMb3JpZ0NhbGxjb3JldAAgTHZjL2RhdGEvVEFDQ21kJFNpbXBsZSRDYWxsQ29yZTtMAAdvdXRCYXNlcQB+ABtMAAlvdXRPZmZzZXRxAH4AG0wAB291dFNpemVxAH4AG0wADXNpZ1Jlc29sdXRpb250AA9MamF2YS91dGlsL1NldDtMAAV0b1ZhcnEAfgAbTAAIdmFsdWVWYXJxAH4AG3hwAAAAB3NyACRpbnN0cnVtZW50YXRpb24uY2FsbHMuQ2FsbENvbnZlbnRpb25HtO1ulL788QIAA0kACGNhbGxlcklkTAAFaW5wdXR0ABlMYW5hbHlzaXMvaWNmZy9DYWxsSW5wdXQ7TAAGcmF3T3V0dAAiTGluc3RydW1lbnRhdGlvbi9jYWxscy9DYWxsT3V0cHV0O3hwAAAAAHNyABdhbmFseXNpcy5pY2ZnLkNhbGxJbnB1dJjJD1MhNUxQAgAHTAAHYmFzZVZhcnQAGUx2Yy9kYXRhL1RBQ0V4cHIkU3ltJFZhcjtMABBlbmNvZGVkQXJndW1lbnRzdAAjTGFuYWx5c2lzL2ljZmcvQUJJQXJndW1lbnRFbmNvZGluZztMABNpbnB1dFNpemVMb3dlckJvdW5kcQB+AAZMAAZvZmZzZXR0ABVMdmMvZGF0YS9UQUNFeHByJFN5bTtMABRyYW5nZVRvRGVjb21wb3NlZEFyZ3QAD0xqYXZhL3V0aWwvTWFwO0wAEHNpbXBsaWZpZWRPZmZzZXR0ABtMdmMvZGF0YS9UQUNFeHByJFN5bSRDb25zdDtMAARzaXplcQB+ACZ4cHNyABd2Yy5kYXRhLlRBQ0V4cHIkU3ltJFZhcskrg43eGgPnAgACTAABc3QAF0x2Yy9kYXRhL1RBQ1N5bWJvbCRWYXI7TAADdGFndAAJTHRhYy9UYWc7eHIAE3ZjLmRhdGEuVEFDRXhwciRTeW2iVj0S4YSNUAIAAHhyAA92Yy5kYXRhLlRBQ0V4cHJYhGlUu/v+yAIAAHhwc3IANnZjLmRhdGEuVEFDU3ltYm9sJFZhciRXaXRoRGVmYXVsdENhbGxJbmRleCRXaXRoQnl0ZU1hcJ7+oHF4CHAAAgACTAAEbWV0YXQALUxrb3RsaW54L2NvbGxlY3Rpb25zL2ltbXV0YWJsZS9QZXJzaXN0ZW50TWFwO0wACm5hbWVQcmVmaXh0ABJMamF2YS9sYW5nL1N0cmluZzt4cgAVdmMuZGF0YS5UQUNTeW1ib2wkVmFyCYrCGVl9SXYCAAB4cgARdmMuZGF0YS5UQUNTeW1ib2zd3Run/CoWswIAAHhwc3IAJmRhdGFzdHJ1Y3R1cmVzLnRyZWFwLkhhc2hUcmVhcE1hcCROb2Rlf2t9acJIPnQCAANMAANrZXl0ABJMamF2YS9sYW5nL09iamVjdDtMAARuZXh0dAA1TGRhdGFzdHJ1Y3R1cmVzL3RyZWFwL0hhc2hUcmVhcE1hcCRNb3JlS2V5VmFsdWVQYWlycztMAAV2YWx1ZXEAfgA3eHIAIWRhdGFzdHJ1Y3R1cmVzLnRyZWFwLkhhc2hUcmVhcE1hcPMJ/2vt3boKAgAAeHIAHWRhdGFzdHJ1Y3R1cmVzLnRyZWFwLlRyZWFwTWFw46LAyn3v5moCAAB4cgAaZGF0YXN0cnVjdHVyZXMudHJlYXAuVHJlYXA88f21zZwbdQIAAkwABGxlZnR0ABxMZGF0YXN0cnVjdHVyZXMvdHJlYXAvVHJlYXA7TAAFcmlnaHRxAH4APHhwcHNxAH4ANnBzcQB+ADZwcHNyAAt0YWMuTWV0YUtleVF/W3MiCfIZAgADTAAPZXJhc3VyZVN0cmF0ZWd5dAAdTHRhYy9NZXRhS2V5JEVyYXN1cmVTdHJhdGVneTtMAARuYW1lcQB+ADJMAAN0eXB0ABFMamF2YS9sYW5nL0NsYXNzO3hwfnIAG3RhYy5NZXRhS2V5JEVyYXN1cmVTdHJhdGVneQAAAAAAAAAAEgAAeHIADmphdmEubGFuZy5FbnVtAAAAAAAAAAASAAB4cHQACUNhbm9uaWNhbHQAF3RhYy5tZW1vcnkucGFydGl0aW9uLWlkdnIAEWphdmEubGFuZy5JbnRlZ2VyEuKgpPeBhzgCAAFJAAV2YWx1ZXhxAH4ADnBzcQB+AEkAAAAKc3EAfgBAcQB+AEZ0ABJUYWMuc3ltYm9sLmtleXdvcmR2cgAQamF2YS5sYW5nLlN0cmluZ6DwpDh6O7NCAgAAeHBwdAAEdGFjTXNxAH4AQHEAfgBGdAANdGFjLmlzLm1lbW9yeXZyACJ0YWMuTWV0YU1hcCRDb21wYW5pb24kTm90aGluZ1ZhbHVl8nsHH85ykpUCAAB4cHBzcQB+AFN0AA90YWNNQ0FOT04yISE0MDVzcgAPdGFjLlRhZyRCeXRlTWFwNb/Ry6GDRgkCAAB4cgALdGFjLlRhZyRNYXABJytzDV3P/QIAAHhyAAd0YWMuVGFnLk9V3gn2xngCAAB4cHBzcQB+AAz///////////////7////+AAAAAXVxAH4AEAAAAAFkeHNxAH4AKnNyADV2Yy5kYXRhLlRBQ1N5bWJvbCRWYXIkV2l0aERlZmF1bHRDYWxsSW5kZXgkV2l0aEJpdDI1NnqsyEgq0drPAgACTAAEbWV0YXEAfgAxTAAKbmFtZVByZWZpeHEAfgAyeHEAfgAzc3EAfgA2c3EAfgA2cHBxAH4ATHB0AAFMcHNxAH4AQHEAfgBGdAAQdGFjLnN0YWNrLmhlaWdodHEAfgBKcHNxAH4ASQAAA/h0AARSNDA2c3IADnRhYy5UYWckQml0MjU2IyLQT+LlKkgCAAB4cQB+AFlzcgARamF2YS51dGlsLkhhc2hNYXAFB9rBwxZg0QMAAkYACmxvYWRGYWN0b3JJAAl0aHJlc2hvbGR4cD9AAAAAAAADdwgAAAAEAAAAAnNyAB5hbmFseXNpcy5pY2ZnLlNjcmF0Y2hCeXRlUmFuZ2XBTLaPpUzj2gIAAkwABGZyb21xAH4ABkwAAnRvcQB+AAZ4cHNxAH4ADP///////////////v////4AAAAAdXEAfgAQAAAAAHhzcQB+AAz///////////////7////+AAAAAXVxAH4AEAAAAAEDeHNyAC1hbmFseXNpcy5pY2ZnLkRlY29tcG9zZWRDYWxsSW5wdXRBcmckQ29uc3RhbnSFavLdQafqPQIAA0wAAWN0ABlMdmMvZGF0YS9UQUNTeW1ib2wkQ29uc3Q7TAARY29udHJhY3RSZWZlcmVuY2V0AC9MYW5hbHlzaXMvaWNmZy9DYWxsR3JhcGhCdWlsZGVyJENhbGxlZENvbnRyYWN0O0wADHNjcmF0Y2hSYW5nZXQAIExhbmFseXNpcy9pY2ZnL1NjcmF0Y2hCeXRlUmFuZ2U7eHIAJGFuYWx5c2lzLmljZmcuRGVjb21wb3NlZENhbGxJbnB1dEFyZ82Nwhnirh8hAgAAeHBzcgAXdmMuZGF0YS5UQUNTeW1ib2wkQ29uc3QmHp5/l8IUcAIAAkwAA3RhZ3EAfgAsTAAFdmFsdWVxAH4ABnhxAH4ANHEAfgBoc3EAfgAM///////////////+/////gAAAAF1cQB+ABAAAAAgOEL3dgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAB4cHEAfgBsc3EAfgBrc3EAfgAM///////////////+/////gAAAAF1cQB+ABAAAAABRHhzcQB+AAz///////////////7////+AAAAAXVxAH4AEAAAAAFjeHNyAC1hbmFseXNpcy5pY2ZnLkRlY29tcG9zZWRDYWxsSW5wdXRBcmckVmFyaWFibGWV3y80jneopQIAA0wAEWNvbnRyYWN0UmVmZXJlbmNlcQB+AHNMAAxzY3JhdGNoUmFuZ2VxAH4AdEwAAXZxAH4AK3hxAH4AdXNyADxhbmFseXNpcy5pY2ZnLkNhbGxHcmFwaEJ1aWxkZXIkQ2FsbGVkQ29udHJhY3QkVW5yZXNvbHZlZFJlYWRDhKJZ0RDzoAIAAUkADXN0b3JhZ2VSZWFkSWR4cgAtYW5hbHlzaXMuaWNmZy5DYWxsR3JhcGhCdWlsZGVyJENhbGxlZENvbnRyYWN00wt1rN/LodcCAAB4cAAAAAxxAH4Ae3NxAH4AXnNxAH4ANnNxAH4ANnBzcQB+ADZzcQB+ADZzcQB+ADZwc3EAfgA2cHBxAH4ATHBxAH4AYnNxAH4AQHEAfgBGdAAWdGFjLnNjYWxhcml6YXRpb24uc29ydHZyABl2Yy5kYXRhLlNjYWxhcml6YXRpb25Tb3J0MM5wneRoDSYCAAB4cHBzcgAfdmMuZGF0YS5TY2FsYXJpemF0aW9uU29ydCRTcGxpdFT/Wafxx7IFAgABTAADaWR4cQB+AAZ4cQB+AI5zcQB+AAz///////////////7////+AAAAAXVxAH4AEAAAAAEFeHNxAH4ANnBzcQB+ADZwc3EAfgA2cHBzcQB+AEBxAH4ARnQAHHRhYy5zdG9yYWdlLm5vbi1pbmRleGVkLXBhdGh2cgA1YW5hbHlzaXMuc3RvcmFnZS5TdG9yYWdlQW5hbHlzaXNSZXN1bHQkTm9uSW5kZXhlZFBhdGgIwaBLofo/RQIAAHhwcHNyADphbmFseXNpcy5zdG9yYWdlLlN0b3JhZ2VBbmFseXNpc1Jlc3VsdCROb25JbmRleGVkUGF0aCRSb290vzf12KXqCv8CAAFMAARzbG90cQB+AAZ4cQB+AJlxAH4AknNxAH4AQHEAfgBGdAANdGFjLnNsb3QudHlwZXZyADpzcGVjLmN2bGFzdC50eXBlZGVzY3JpcHRvcnMuRVZNVHlwZURlc2NyaXB0b3IkRVZNVmFsdWVUeXBlxomvArrquCUCAAB4cgAtc3BlYy5jdmxhc3QudHlwZWRlc2NyaXB0b3JzLkVWTVR5cGVEZXNjcmlwdG9yyFGp8TzCah0CAAB4cHBzcgAzc3BlYy5jdmxhc3QudHlwZWRlc2NyaXB0b3JzLkVWTVR5cGVEZXNjcmlwdG9yJFVJbnRL+xQfR/Nlf8ACAAFJAAhiaXR3aWR0aHhyAERzcGVjLmN2bGFzdC50eXBlZGVzY3JpcHRvcnMuRVZNVHlwZURlc2NyaXB0b3IkRVZNSXNvbW9ycGhpY1ZhbHVlVHlwZfd1mJFuEKEPAgAAeHEAfgCfAAABAHNxAH4AQH5xAH4ARHQABkVyYXNlZHQAGHRhYy5zdG9yYWdlLnByZXR0eS5wYXRoc3ZyAB1hbmFseXNpcy5zdG9yYWdlLkRpc3BsYXlQYXRoc/dES7fD9VEWAgABTAAFcGF0aHNxAH4AHXhwcHNxAH4AqXNyABdqYXZhLnV0aWwuTGlua2VkSGFzaFNldNhs11qV3SoeAgAAeHIAEWphdmEudXRpbC5IYXNoU2V0ukSFlZa4tzQDAAB4cHcMAAAAED9AAAAAAAABc3IAIWFuYWx5c2lzLnN0b3JhZ2UuRGlzcGxheVBhdGgkUm9vdNNzoL2Z0DxyAgACTAAEYmFzZXQAHkxhbmFseXNpcy9zdG9yYWdlL0Rpc3BsYXlQYXRoO0wABG5hbWVxAH4AMnhyABxhbmFseXNpcy5zdG9yYWdlLkRpc3BsYXlQYXRoT0Bj6lbSIAUCAAB4cHB0AAhmdXR1cmVfQXhzcQB+AEBxAH4ARnQAFXRhYy5zdG9yYWdlLmJpdC13aWR0aHEAfgBKcHNxAH4ASQAAAQBwc3EAfgBAcQB+AEZ0AAt0YWMuc3RvcmFnZXZxAH4ADHBxAH4AD3NxAH4AQHEAfgBGdAAYdGFjLmRlY29tcC1pbnNjYWxhci5zb3J0dnIAHXRhYy5EZWNvbXBvc2VkSW5wdXRTY2FsYXJTb3J0J4Yx32MwVAUCAAB4cHBzcgAkdGFjLkRlY29tcG9zZWRJbnB1dFNjYWxhclNvcnQkU2ltcGxleQdV+qgJslsCAAFMAApieXRlT2Zmc2V0cQB+AAZ4cQB+ALxxAH4AfHBxAH4AY3BzcQB+AEkAAAP5dAALQ0FOT045OSEhMzF4cHNxAH4AKnNxAH4AXnNxAH4ANnNxAH4ANnBwcQB+AExwcQB+AGJwcQB+AGNwc3EAfgBJAAAD93QABFI0MDdxAH4AaHNyACBpbnN0cnVtZW50YXRpb24uY2FsbHMuQ2FsbE91dHB1dMLFmzfBvZx7AgADTAAEYmFzZXEAfgArTAAGb2Zmc2V0dAARTHZjL2RhdGEvVEFDRXhwcjtMAARzaXplcQB+AMl4cHNxAH4AMHNxAH4ANnBzcQB+ADZwc3EAfgA2cHBxAH4AQ3BxAH4AS3EAfgBMcHEAfgBQcQB+AFFwcQB+AFVxAH4AVnNxAH4AKnNxAH4AXnNxAH4ANnNxAH4ANnBwcQB+AExwcQB+AGJwcQB+AGNwc3EAfgBJAAAD+HEAfgBmcQB+AGhzcgAZdmMuZGF0YS5UQUNFeHByJFN5bSRDb25zdFNIr/MyQdp2AgACTAABc3EAfgByTAADdGFncQB+ACx4cQB+AC1zcQB+AHdxAH4AaHNxAH4ADP///////////////v////4AAAABdXEAfgAQAAAAASB4cQB+AGhzcgAeYW5hbHlzaXMuaWNmZy5DYWxsVGFyZ2V0JFZhbGlkuaYZ9j2rVfoCAAFMAAZjYWxsZWVxAH4Ac3hyABhhbmFseXNpcy5pY2ZnLkNhbGxUYXJnZXRG3T0sfHY+JQIAAHhwc3IARGFuYWx5c2lzLmljZmcuQ2FsbEdyYXBoQnVpbGRlciRDYWxsZWRDb250cmFjdCRGdWxseVJlc29sdmVkJFNlbGZMaW5r77yXwCrurrMCAAFMAApjb250cmFjdElkcQB+AAZ4cgA7YW5hbHlzaXMuaWNmZy5DYWxsR3JhcGhCdWlsZGVyJENhbGxlZENvbnRyYWN0JEZ1bGx5UmVzb2x2ZWSi2ciTEwCzpAIAAHhxAH4Ag3EAfgAPfnIAE3ZjLmRhdGEuVEFDQ2FsbFR5cGUAAAAAAAAAABIAAHhxAH4ARXQABlNUQVRJQ3BzcQB+AF5zcQB+ADZzcQB+ADZwcHEAfgBMcHEAfgBicHEAfgBjcHNxAH4ASQAAA/R0AARSNDA4c3EAfgAwc3EAfgA2cHNxAH4ANnBzcQB+ADZwcHEAfgBDcHEAfgBLcQB+AExwcQB+AFBxAH4AUXBxAH4AVXEAfgBWc3EAfgBec3EAfgA2c3EAfgA2cHBxAH4ATHBxAH4AYnBxAH4AY3BxAH4AZXEAfgBmc3EAfgB3cQB+AGhxAH4AW3NyAB52Yy5kYXRhLlRBQ0NtZCRTaW1wbGUkQ2FsbENvcmWhKYVHBIFmegIAC0wACGNhbGxUeXBlcQB+ABlMAANnYXNxAH4AG0wABmluQmFzZXEAfgArTAAIaW5PZmZzZXRxAH4AG0wABmluU2l6ZXEAfgAbTAAEbWV0YXEAfgAxTAAHb3V0QmFzZXEAfgArTAAJb3V0T2Zmc2V0cQB+ABtMAAdvdXRTaXplcQB+ABtMAAJ0b3EAfgAbTAAFdmFsdWVxAH4AG3hyABV2Yy5kYXRhLlRBQ0NtZCRTaW1wbGXtJtYlMQZ10gIAAHhyABN2Yy5kYXRhLlRBQ0NtZCRTcGVjG6vxAPjBA74CAAB4cgAOdmMuZGF0YS5UQUNDbWRUyw+IPDkf8AIAAHhwcQB+AOBzcQB+AF5zcQB+ADZzcQB+ADZwcHEAfgBMcHEAfgBicHEAfgBjcHEAfgDlcQB+AOZzcQB+ADBzcQB+ADZwc3EAfgA2cHNxAH4ANnBwcQB+AENwcQB+AEtxAH4ATHBxAH4AUHEAfgBRcHEAfgBVcQB+AFZzcQB+AF5zcQB+ADZzcQB+ADZwcHEAfgBMcHEAfgBicHEAfgBjcHEAfgBlcQB+AGZzcQB+AF5zcQB+ADZzcQB+ADZwcHEAfgBMcHEAfgBicHEAfgBjcHEAfgDGcQB+AMdzcQB+ADZwcHNxAH4AQH5xAH4ARHQACUNhbGxUcmFjZXQACHRhYy5tZXRhdnIAE3ZjLmRhdGEuVEFDTWV0YUluZm81YEz9pUuocQIABkkABWJlZ2luSQADbGVuSQAGc291cmNlTAAHYWRkcmVzc3EAfgAGTAAIanVtcFR5cGV0ABNMY29tcGlsZXIvSnVtcFR5cGU7TAANc291cmNlQ29udGV4dHQAGExjb21waWxlci9Tb3VyY2VDb250ZXh0O3hwcHNxAH4BBgAAGLcAAAAdAAAAB3EAfgAPfnIAEWNvbXBpbGVyLkp1bXBUeXBlAAAAAAAAAAASAAB4cQB+AEV0AAdSRUdVTEFSc3IAFmNvbXBpbGVyLlNvdXJjZUNvbnRleHSMy1vpQFzaEwIAAkwAD2luZGV4VG9GaWxlcGF0aHEAfgAnTAAJc291cmNlRGlycQB+ADJ4cHNxAH4AaT9AAAAAAAAMdwgAAAAQAAAACHNxAH4ASQAAAAB0ABVjb250cmFjdHMvQ29udGV4dC5zb2xzcQB+AEkAAAABdAAYY29udHJhY3RzL0N1cnZlVG9rZW4uc29sc3EAfgBJAAAAAnQAH2NvbnRyYWN0cy9DdXJ2ZVRva2VuRXhhbXBsZS5zb2xzcQB+AEkAAAADdAATY29udHJhY3RzL0VSQzIwLnNvbHNxAH4ASQAAAAR0ABRjb250cmFjdHMvSUVSQzIwLnNvbHNxAH4ASQAAAAV0ABxjb250cmFjdHMvSUVSQzIwTWV0YWRhdGEuc29sc3EAfgBJAAAABnQAHWNvbnRyYWN0cy9SZWVudHJhbmN5R3VhcmQuc29sc3EAfgBJAAAAB3QAE2NvbnRyYWN0cy9jdXJ2ZS5zb2x4dAATLnBvc3RfYXV0b2ZpbmRlcnMuMnNxAH4AMHNxAH4ANnBzcQB+ADZwc3EAfgA2cHBxAH4AQ3BxAH4AS3EAfgBMcHEAfgBQcQB+AFFwcQB+AFVxAH4AVnNxAH4AXnNxAH4ANnNxAH4ANnBwcQB+AExwcQB+AGJwcQB+AGNwcQB+ANNxAH4AZnEAfgDWc3EAfgBec3EAfgA2c3EAfgA2c3EAfgA2c3EAfgA2cHBxAH4ATHBxAH4AYnBzcQB+AEBxAH4ApnQAGnRhYy5jb250cmFjdC5zeW0uYWRkci5uYW1lcQB+AE9wdAAFY3VydmVwc3EAfgBAcQB+AKZ0ABV0YWMuY29udHJhY3Quc3ltLmFkZHJxAH4AuXBxAH4AD3BxAH4AY3BzcQB+AEkAAAP8dAADUjM0c3EAfgB3cQB+AGhxAH4AbXNxAH4AMHNxAH4ANnBzcQB+ADZwc3EAfgA2cHBxAH4AQ3BxAH4AS3EAfgBMcHEAfgBQcQB+AFFwcQB+AFVxAH4AVnNxAH4AXnNxAH4ANnNxAH4ANnBwcQB+AExwcQB+AGJwcQB+AGNwcQB+ANNxAH4AZnEAfgDWc3IAImphdmEudXRpbC5Db2xsZWN0aW9ucyRTaW5nbGV0b25TZXQsUkGYKcCxvwIAAUwAB2VsZW1lbnRxAH4AN3hwcQB+ABRzcQB+AF5zcQB+ADZzcQB+ADZzcQB+ADZzcQB+ADZwcHEAfgBMcHEAfgBicHEAfgEucHEAfgEwcHEAfgExcHEAfgAPcHEAfgBjcHEAfgEzcQB+ATRzcQB+AHdxAH4AaHEAfgBt"}
		AnnotationCmd:105 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageGlobalChangeSnippet.StorageBackupPoint","calleeTxId":11}}
		NopCmd
		AssumeExpCmd LAnd(Eq(tacCalldatasize!!7:3 0x64 ) Eq(tacCalldatasize!!7:3 0x64 ) )
		AssignExpCmd:105 B330:54 Eq(Select(tacCalldatabuf!!23@11:121 0x0 ) 0x3842f77600000000000000000000000000000000000000000000000000000000 )
		AssumeCmd:105 B330:54
		AssignExpCmd:105 tacCalldatabuf!!331@11:21 LongStore(tacCalldatabuf!!23@11:121 0x4 tacMCANON2!!405:10 0x124 Sub(0x64 0x4 ) )
		LabelCmd:105 "Start procedure curve-get_D(uint256[2],uint256)"
		AnnotationCmd:105 JSON{"key":{"name":"fps.free-pointer-is-scalarized","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true}
		AssignExpCmd:105 R332:54 Select(tacExtcodesize!!9:4 Apply(to_skey:bif R34:63) )
		NopCmd
		AssumeExpCmd Gt(R332:54 0x0 )
		AnnotationCmd:105 JSON{"key":{"name":"internal.func.finder.info","type":"analysis.ip.InternalFunctionFinderReport","erasureStrategy":"Erased"},"value":"rO0ABXNyAChhbmFseXNpcy5pcC5JbnRlcm5hbEZ1bmN0aW9uRmluZGVyUmVwb3J0ian+bYn1VdACAAFMABN1bnJlc29sdmVkRnVuY3Rpb25zdAAPTGphdmEvdXRpbC9TZXQ7eHBzcgAhZGF0YXN0cnVjdHVyZXMuTGlua2VkQXJyYXlIYXNoU2V0AAAAAAAAAAEDAAJGAApsb2FkRmFjdG9yTAAJaGFzaFRhYmxldAAuTGRhdGFzdHJ1Y3R1cmVzL2FycmF5aGFzaHRhYmxlL0FycmF5SGFzaFRhYmxlO3hwdwgAAAAAQAAAAHg="}
		AnnotationCmd:105 JSON{"key":{"name":"fps.free-pointer-is-scalarized","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true}
		NopCmd
		AssumeExpCmd LNot(Lt(tacCalldatasize!!7:3 0x4 ) )
		NopCmd
		AssumeExpCmd Gt(0x82c63066 tacSighash!!45:47 )
		NopCmd
		AssumeExpCmd Eq(0x3842f776 tacSighash!!45:47 )
		AssignExpCmd:122 R338:93 Sub(tacCalldatasize!!7:3 0x4 )
		AssignExpCmd:105 B339:83 Slt(R338:93 0x60 )
		NopCmd
		AssumeExpCmd LNot(B339:83 )
		NopCmd
		AssumeExpCmd Slt(0x23 tacCalldatasize!!7:94 )
		AssignExpCmd:123 R343:96 0x80
		AssumeCmd:124 true
		AssignExpCmd:105 B344:77 Gt(0x44 tacCalldatasize!!7:94 )
		NopCmd
		AssumeExpCmd LNot(B344:77 )
		AnnotationCmd:105 JSON{"key":{"name":"dsa.assign.start","type":"java.lang.String","erasureStrategy":"Erased"},"value":"4280_1005_0_0_0_0 -> 4282_1004_0_0_0_0"}
		LabelCmd:105 "Parallel assignment for R3573:bv256, R3574:bv256 := R2326:bv256, R3653:bv256"
		AnnotationCmd:105 JSON{"key":{"name":"dsa.assign.end","type":"java.lang.String","erasureStrategy":"Erased"},"value":"4280_1005_0_0_0_0 -> 4282_1004_0_0_0_0"}
		AnnotationCmd:105 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.LoopSnippet.StartLoopSnippet","loopIndex":5,"loopSource":"unknown loop source code"}}
		AnnotationCmd:105 JSON{"key":{"name":"start_loop.cmd","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		AnnotationCmd:105 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.LoopSnippet.StartIter","iteration":1}}
		AssignExpCmd:125 R346:99 Select(tacCalldatabuf!!331@11:121 0x4 )
		AssignExpCmd:126 tacMCANON3!!347:13 Store(tacMCANON3!!17:13 0x80 R346:99 )
		AnnotationCmd:105 JSON{"key":{"name":"dsa.assign.start","type":"java.lang.String","erasureStrategy":"Erased"},"value":"4301_1002_0_0_0_0 -> 4282_1004_0_0_0_0"}
		LabelCmd:105 "Parallel assignment for R3573:bv256, R3574:bv256 := R3566:bv256, R3570:bv256"
		AnnotationCmd:105 JSON{"key":{"name":"dsa.assign.end","type":"java.lang.String","erasureStrategy":"Erased"},"value":"4301_1002_0_0_0_0 -> 4282_1004_0_0_0_0"}
		AnnotationCmd:105 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.LoopSnippet.EndIter","iteration":1}}
		AnnotationCmd:105 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.LoopSnippet.StartIter","iteration":2}}
		AssignExpCmd:125 R348:99 Select(tacCalldatabuf!!331@11:121 0x24 )
		AssignExpCmd:126 tacMCANON3!!349:13 Store(tacMCANON3!!347:13 0xa0 R348:99 )
		AnnotationCmd:105 JSON{"key":{"name":"dsa.assign.start","type":"java.lang.String","erasureStrategy":"Erased"},"value":"4301_1002_0_0_0_0 -> 4282_1004_0_0_0_0"}
		LabelCmd:105 "Parallel assignment for R3573:bv256, R3574:bv256 := R3566:bv256, R3570:bv256"
		AnnotationCmd:105 JSON{"key":{"name":"dsa.assign.end","type":"java.lang.String","erasureStrategy":"Erased"},"value":"4301_1002_0_0_0_0 -> 4282_1004_0_0_0_0"}
		AnnotationCmd:105 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.LoopSnippet.EndIter","iteration":2}}
		AnnotationCmd:105 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.LoopSnippet.EndLoopSnippet","loopId":5}}
		AnnotationCmd:105 JSON{"key":{"name":"end_loop.cmd","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		AnnotationCmd:105 JSON{"key":{"name":"pta.end-allocation","type":"analysis.alloc.AllocationAnalysis$AbstractLocation","erasureStrategy":"Erased"},"value":{"prevFPWriteIdx":0,"nextFPWriteCmd":{"block":{"#class":"tac.BlockIdentifier","origStartPc":4102,"stkTop":1000,"decompCopy":0,"calleeIdx":0,"topOfStackValue":0,"freshCopy":0},"pos":1},"sort":{"#class":"analysis.alloc.AllocationAnalysis.Alloc.ConstBlock","sz":"40"}}}
		AssignExpCmd:125 R350:65 Select(tacCalldatabuf!!331@11:121 0x44 )
		AnnotationCmd:105 JSON{"key":{"name":"internal.func.start","type":"analysis.ip.InternalFuncStartAnnotation","erasureStrategy":"CallTrace"},"value":{"id":14,"startPc":558,"args":[{"s":{"namePrefix":"R343","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1001}]},"offset":1,"sort":"SCALAR"},{"s":{"namePrefix":"R350","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1012}]},"offset":2,"sort":"SCALAR"}],"methodSignature":{"#class":"spec.cvlast.QualifiedMethodSignature.QualifiedMethodSig","qualifiedMethodName":{"#class":"spec.cvlast.QualifiedFunction","host":{"name":"curve"},"methodId":"get_D"},"params":[{"#class":"spec.cvlast.VMParam.Named","name":"xp","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$StaticArrayDescriptor","location":"memory","elementType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256},"numElements":"2"}},{"#class":"spec.cvlast.VMParam.Named","name":"amp","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256}}],"res":[{"#class":"spec.cvlast.VMParam.Unnamed","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256}}]},"stackOffsetToArgPos":{"1":0,"2":1},"callSiteSrc":{"source":7,"begin":2956,"len":1542,"jumpType":"ENTER","address":"ce4604a0000000000000000000000028","sourceContext":{"indexToFilepath":{"0":"contracts/Context.sol","1":"contracts/CurveToken.sol","2":"contracts/CurveTokenExample.sol","3":"contracts/ERC20.sol","4":"contracts/IERC20.sol","5":"contracts/IERC20Metadata.sol","6":"contracts/ReentrancyGuard.sol","7":"contracts/curve.sol"},"sourceDir":".post_autofinders.2"}}}}
		AssignExpCmd:127 R351:83 Select(tacMCANON3!!349:13 0xa0 )
		AssignExpCmd:128 R352:93 Select(tacMCANON3!!349:13 0x80 )
		NopCmd
		AssumeExpCmd Apply(add_noofl:bif R352:93 R351:83)
		NopCmd
		NopCmd
		NopCmd
		AssignExpCmd R358:72 Apply(safe_math_narrow:bif IntAdd(Apply(safe_math_promotion:bif R352:93) Apply(safe_math_promotion:bif R351:83)))
		AnnotationCmd:105 JSON{"key":{"name":"internal.func.end","type":"analysis.ip.InternalFuncExitAnnotation","erasureStrategy":"Canonical"},"value":{"id":14,"rets":[{"s":{"namePrefix":"R358","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1023}]},"offset":0}],"functionLayout":{"0":{"#class":"analysis.ip.InternalFuncValueLocation.Scalar"}}}}
		AnnotationCmd:105 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.EVMFunctionReturnWrite","returnbufOffset":"0","returnValueSym":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R358","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1023}]},"callIndex":11}}
		AnnotationCmd:105 JSON{"key":{"name":"tac.return.path","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		LabelCmd:105 "End procedure curve-get_D(uint256[2],uint256)"
		AssignExpCmd:105 tacReturndata!!360:78 Store(tacReturndata!!409:78 0x0 R358:72 )
		AssignExpCmd:105 tacMCANON2!!361:10 Store(tacMCANON2!!405:10 0x120 R358:72 )
		AnnotationCmd:105 JSON{"key":{"name":"call.trace.pop","type":"analysis.icfg.Inliner$CallStack$PopRecord","erasureStrategy":"Canonical"},"value":"rO0ABXNyAClhbmFseXNpcy5pY2ZnLklubGluZXIkQ2FsbFN0YWNrJFBvcFJlY29yZPAPfwSLdCWJAgABSQAIY2FsbGVlSWR4cAAAAAs="}
		JumpCmd:105 2_0_0_9_0_0
	}
	Block 0_0_0_12_0_0 Succ [3_0_0_9_0_0] {
		AnnotationCmd:105 JSON{"key":{"name":"call.trace.push","type":"analysis.icfg.Inliner$CallStack$PushRecord","erasureStrategy":"Canonical"},"value":"rO0ABXNyACphbmFseXNpcy5pY2ZnLklubGluZXIkQ2FsbFN0YWNrJFB1c2hSZWNvcmSX8+DCTLCH+AIAA0kACGNhbGxlZUlkTAAGY2FsbGVldAATTHZjL2RhdGEvTWV0aG9kUmVmO0wAB3N1bW1hcnl0ABVMdmMvZGF0YS9DYWxsU3VtbWFyeTt4cAAAAAxzcgARdmMuZGF0YS5NZXRob2RSZWbJlJTzzU9pGAIAA0wABGF0dHJ0ABdMc2NlbmUvTWV0aG9kQXR0cmlidXRlO0wACmNvbnRyYWN0SWR0ABZMamF2YS9tYXRoL0JpZ0ludGVnZXI7TAAHc2lnSGFzaHQAEExldm0vU2lnaGFzaEludDt4cHNyABxzY2VuZS5NZXRob2RBdHRyaWJ1dGUkQ29tbW9uNHjdebdr9XMCAAB4cgAVc2NlbmUuTWV0aG9kQXR0cmlidXRlcYg2pYWutuUCAAB4cHNyABRqYXZhLm1hdGguQmlnSW50ZWdlcoz8nx+pO/sdAwAGSQAIYml0Q291bnRJAAliaXRMZW5ndGhJABNmaXJzdE5vbnplcm9CeXRlTnVtSQAMbG93ZXN0U2V0Qml0SQAGc2lnbnVtWwAJbWFnbml0dWRldAACW0J4cgAQamF2YS5sYW5nLk51bWJlcoaslR0LlOCLAgAAeHD///////////////7////+AAAAAXVyAAJbQqzzF/gGCFTgAgAAeHAAAAAQzkYEoAAAAAAAAAAAAAAACHhzcgAOZXZtLlNpZ2hhc2hJbnRUdcqNMXEgeAIAAUwAAW5xAH4ABnhwc3EAfgAM///////////////+/////gAAAAF1cQB+ABAAAAAEGBYN3XhzcgATdmMuZGF0YS5DYWxsU3VtbWFyeZQcmw5vl+FdAgAQSQAJc3VtbWFyeUlkTAAOY2FsbENvbnZlbnRpb250ACZMaW5zdHJ1bWVudGF0aW9uL2NhbGxzL0NhbGxDb252ZW50aW9uO0wACmNhbGxUYXJnZXR0ABpMYW5hbHlzaXMvaWNmZy9DYWxsVGFyZ2V0O0wACGNhbGxUeXBldAAVTHZjL2RhdGEvVEFDQ2FsbFR5cGU7TAAPY2Fubm90QmVJbmxpbmVkdAAtTGFuYWx5c2lzL2ljZmcvSW5saW5lciRJbGxlZ2FsSW5saW5pbmdSZWFzb247TAAGZ2FzVmFydAATTHZjL2RhdGEvVEFDU3ltYm9sO0wABmluQmFzZXEAfgAbTAAIaW5PZmZzZXRxAH4AG0wABmluU2l6ZXEAfgAbTAAMb3JpZ0NhbGxjb3JldAAgTHZjL2RhdGEvVEFDQ21kJFNpbXBsZSRDYWxsQ29yZTtMAAdvdXRCYXNlcQB+ABtMAAlvdXRPZmZzZXRxAH4AG0wAB291dFNpemVxAH4AG0wADXNpZ1Jlc29sdXRpb250AA9MamF2YS91dGlsL1NldDtMAAV0b1ZhcnEAfgAbTAAIdmFsdWVWYXJxAH4AG3hwAAAACHNyACRpbnN0cnVtZW50YXRpb24uY2FsbHMuQ2FsbENvbnZlbnRpb25HtO1ulL788QIAA0kACGNhbGxlcklkTAAFaW5wdXR0ABlMYW5hbHlzaXMvaWNmZy9DYWxsSW5wdXQ7TAAGcmF3T3V0dAAiTGluc3RydW1lbnRhdGlvbi9jYWxscy9DYWxsT3V0cHV0O3hwAAAAAHNyABdhbmFseXNpcy5pY2ZnLkNhbGxJbnB1dJjJD1MhNUxQAgAHTAAHYmFzZVZhcnQAGUx2Yy9kYXRhL1RBQ0V4cHIkU3ltJFZhcjtMABBlbmNvZGVkQXJndW1lbnRzdAAjTGFuYWx5c2lzL2ljZmcvQUJJQXJndW1lbnRFbmNvZGluZztMABNpbnB1dFNpemVMb3dlckJvdW5kcQB+AAZMAAZvZmZzZXR0ABVMdmMvZGF0YS9UQUNFeHByJFN5bTtMABRyYW5nZVRvRGVjb21wb3NlZEFyZ3QAD0xqYXZhL3V0aWwvTWFwO0wAEHNpbXBsaWZpZWRPZmZzZXR0ABtMdmMvZGF0YS9UQUNFeHByJFN5bSRDb25zdDtMAARzaXplcQB+ACZ4cHNyABd2Yy5kYXRhLlRBQ0V4cHIkU3ltJFZhcskrg43eGgPnAgACTAABc3QAF0x2Yy9kYXRhL1RBQ1N5bWJvbCRWYXI7TAADdGFndAAJTHRhYy9UYWc7eHIAE3ZjLmRhdGEuVEFDRXhwciRTeW2iVj0S4YSNUAIAAHhyAA92Yy5kYXRhLlRBQ0V4cHJYhGlUu/v+yAIAAHhwc3IANnZjLmRhdGEuVEFDU3ltYm9sJFZhciRXaXRoRGVmYXVsdENhbGxJbmRleCRXaXRoQnl0ZU1hcJ7+oHF4CHAAAgACTAAEbWV0YXQALUxrb3RsaW54L2NvbGxlY3Rpb25zL2ltbXV0YWJsZS9QZXJzaXN0ZW50TWFwO0wACm5hbWVQcmVmaXh0ABJMamF2YS9sYW5nL1N0cmluZzt4cgAVdmMuZGF0YS5UQUNTeW1ib2wkVmFyCYrCGVl9SXYCAAB4cgARdmMuZGF0YS5UQUNTeW1ib2zd3Run/CoWswIAAHhwc3IAJmRhdGFzdHJ1Y3R1cmVzLnRyZWFwLkhhc2hUcmVhcE1hcCROb2Rlf2t9acJIPnQCAANMAANrZXl0ABJMamF2YS9sYW5nL09iamVjdDtMAARuZXh0dAA1TGRhdGFzdHJ1Y3R1cmVzL3RyZWFwL0hhc2hUcmVhcE1hcCRNb3JlS2V5VmFsdWVQYWlycztMAAV2YWx1ZXEAfgA3eHIAIWRhdGFzdHJ1Y3R1cmVzLnRyZWFwLkhhc2hUcmVhcE1hcPMJ/2vt3boKAgAAeHIAHWRhdGFzdHJ1Y3R1cmVzLnRyZWFwLlRyZWFwTWFw46LAyn3v5moCAAB4cgAaZGF0YXN0cnVjdHVyZXMudHJlYXAuVHJlYXA88f21zZwbdQIAAkwABGxlZnR0ABxMZGF0YXN0cnVjdHVyZXMvdHJlYXAvVHJlYXA7TAAFcmlnaHRxAH4APHhwcHNxAH4ANnBzcQB+ADZwcHNyAAt0YWMuTWV0YUtleVF/W3MiCfIZAgADTAAPZXJhc3VyZVN0cmF0ZWd5dAAdTHRhYy9NZXRhS2V5JEVyYXN1cmVTdHJhdGVneTtMAARuYW1lcQB+ADJMAAN0eXB0ABFMamF2YS9sYW5nL0NsYXNzO3hwfnIAG3RhYy5NZXRhS2V5JEVyYXN1cmVTdHJhdGVneQAAAAAAAAAAEgAAeHIADmphdmEubGFuZy5FbnVtAAAAAAAAAAASAAB4cHQACUNhbm9uaWNhbHQAF3RhYy5tZW1vcnkucGFydGl0aW9uLWlkdnIAEWphdmEubGFuZy5JbnRlZ2VyEuKgpPeBhzgCAAFJAAV2YWx1ZXhxAH4ADnBzcQB+AEkAAAAKc3EAfgBAcQB+AEZ0ABJUYWMuc3ltYm9sLmtleXdvcmR2cgAQamF2YS5sYW5nLlN0cmluZ6DwpDh6O7NCAgAAeHBwdAAEdGFjTXNxAH4AQHEAfgBGdAANdGFjLmlzLm1lbW9yeXZyACJ0YWMuTWV0YU1hcCRDb21wYW5pb24kTm90aGluZ1ZhbHVl8nsHH85ykpUCAAB4cHBzcQB+AFN0AA90YWNNQ0FOT04yISE0NTZzcgAPdGFjLlRhZyRCeXRlTWFwNb/Ry6GDRgkCAAB4cgALdGFjLlRhZyRNYXABJytzDV3P/QIAAHhyAAd0YWMuVGFnLk9V3gn2xngCAAB4cHBzcQB+AAz///////////////7////+AAAAAXVxAH4AEAAAAAEEeHNxAH4AKnNyADV2Yy5kYXRhLlRBQ1N5bWJvbCRWYXIkV2l0aERlZmF1bHRDYWxsSW5kZXgkV2l0aEJpdDI1NnqsyEgq0drPAgACTAAEbWV0YXEAfgAxTAAKbmFtZVByZWZpeHEAfgAyeHEAfgAzc3EAfgA2c3EAfgA2cHBxAH4ATHB0AAFMcHNxAH4AQHEAfgBGdAAQdGFjLnN0YWNrLmhlaWdodHEAfgBKcHNxAH4ASQAAA/d0AARSNDU3c3IADnRhYy5UYWckQml0MjU2IyLQT+LlKkgCAAB4cQB+AFlzcgARamF2YS51dGlsLkhhc2hNYXAFB9rBwxZg0QMAAkYACmxvYWRGYWN0b3JJAAl0aHJlc2hvbGR4cD9AAAAAAAABdwgAAAACAAAAAXNyAB5hbmFseXNpcy5pY2ZnLlNjcmF0Y2hCeXRlUmFuZ2XBTLaPpUzj2gIAAkwABGZyb21xAH4ABkwAAnRvcQB+AAZ4cHNxAH4ADP///////////////v////4AAAAAdXEAfgAQAAAAAHhzcQB+AAz///////////////7////+AAAAAXVxAH4AEAAAAAEDeHNyAC1hbmFseXNpcy5pY2ZnLkRlY29tcG9zZWRDYWxsSW5wdXRBcmckQ29uc3RhbnSFavLdQafqPQIAA0wAAWN0ABlMdmMvZGF0YS9UQUNTeW1ib2wkQ29uc3Q7TAARY29udHJhY3RSZWZlcmVuY2V0AC9MYW5hbHlzaXMvaWNmZy9DYWxsR3JhcGhCdWlsZGVyJENhbGxlZENvbnRyYWN0O0wADHNjcmF0Y2hSYW5nZXQAIExhbmFseXNpcy9pY2ZnL1NjcmF0Y2hCeXRlUmFuZ2U7eHIAJGFuYWx5c2lzLmljZmcuRGVjb21wb3NlZENhbGxJbnB1dEFy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ADZwcHEAfgBMcHEAfgBic3EAfgBAcQB+AEZ0ABZ0YWMuc2NhbGFyaXphdGlvbi5zb3J0dnIAGXZjLmRhdGEuU2NhbGFyaXphdGlvblNvcnQwznCd5GgNJgIAAHhwcHNyACB2Yy5kYXRhLlNjYWxhcml6YXRpb25Tb3J0JFBhY2tlZC5FrRKTiOT3AgACSQAFc3RhcnRMAAtwYWNrZWRTdGFydHQAG0x2Yy9kYXRhL1NjYWxhcml6YXRpb25Tb3J0O3hxAH4A7gAAAABzcgAfdmMuZGF0YS5TY2FsYXJpemF0aW9uU29ydCRTcGxpdFT/Wafxx7IFAgABTAADaWR4cQB+AAZ4cQB+AO5zcQB+AAz///////////////7////+AAAAAXVxAH4AEAAAAAEMeHNxAH4ANnBzcQB+ADZwc3EAfgA2cHBzcQB+AEBxAH4ARnQAHHRhYy5zdG9yYWdlLm5vbi1pbmRleGVkLXBhdGh2cgA1YW5hbHlzaXMuc3RvcmFnZS5TdG9yYWdlQW5hbHlzaXNSZXN1bHQkTm9uSW5kZXhlZFBhdGgIwaBLofo/RQIAAHhwcHNyADphbmFseXNpcy5zdG9yYWdlLlN0b3JhZ2VBbmFseXNpc1Jlc3VsdCROb25JbmRleGVkUGF0aCRSb290vzf12KXqCv8CAAFMAARzbG90cQB+AAZ4cQB+APxxAH4A9XNxAH4AQHEAfgBGdAANdGFjLnNsb3QudHlwZXZyADpzcGVjLmN2bGFzdC50eXBlZGVzY3JpcHRvcnMuRVZNVHlwZURlc2NyaXB0b3IkRVZNVmFsdWVUeXBlxomvArrquCUCAAB4cgAtc3BlYy5jdmxhc3QudHlwZWRlc2NyaXB0b3JzLkVWTVR5cGVEZXNjcmlwdG9yyFGp8TzCah0CAAB4cHBzcgA1c3BlYy5jdmxhc3QudHlwZWRlc2NyaXB0b3JzLkVWTVR5cGVEZXNjcmlwdG9yJGFkZHJlc3N6+GX0b5egKQIAAHhyAERzcGVjLmN2bGFzdC50eXBlZGVzY3JpcHRvcnMuRVZNVHlwZURlc2NyaXB0b3IkRVZNSXNvbW9ycGhpY1ZhbHVlVHlwZfd1mJFuEKEPAgAAeHEAfgECc3EAfgBAfnEAfgBEdAAGRXJhc2VkdAAYdGFjLnN0b3JhZ2UucHJldHR5LnBhdGhzdnIAHWFuYWx5c2lzLnN0b3JhZ2UuRGlzcGxheVBhdGhz90RLt8P1URYCAAFMAAVwYXRoc3EAfgAdeHBwc3EAfgEMc3IAF2phdmEudXRpbC5MaW5rZWRIYXNoU2V02GzXWpXdKh4CAAB4cgARamF2YS51dGlsLkhhc2hTZXS6RIWVlri3NAMAAHhwdwwAAAAQP0AAAAAAAAFzcgAhYW5hbHlzaXMuc3RvcmFnZS5EaXNwbGF5UGF0aCRSb29003OgvZnQPHICAAJMAARiYXNldAAeTGFuYWx5c2lzL3N0b3JhZ2UvRGlzcGxheVBhdGg7TAAEbmFtZXEAfgAyeHIAHGFuYWx5c2lzLnN0b3JhZ2UuRGlzcGxheVBhdGhPQGPqVtIgBQIAAHhwcHQACGxwX3Rva2VueHNxAH4AQHEAfgBGdAAVdGFjLnN0b3JhZ2UuYml0LXdpZHRocQB+AEpwc3EAfgBJAAAAoHBzcQB+AEBxAH4ARnQAC3RhYy5zdG9yYWdldnEAfgAMcHEAfgDGcHEAfgBjcHNxAH4ASQAAA/t0AAtDQU5PTjE5ISEyNXNxAH4Ad3EAfgBocQB+AG1zcQB+ADBzcQB+ADZwc3EAfgA2cHNxAH4ANnBwcQB+AENwcQB+AEtxAH4ATHBxAH4AUHEAfgBRcHEAfgBVcQB+AFZzcQB+AF5zcQB+ADZzcQB+ADZwcHEAfgBMcHEAfgBicHEAfgBjcHEAfgCNcQB+AGZxAH4AkHNyACJqYXZhLnV0aWwuQ29sbGVjdGlvbnMkU2luZ2xldG9uU2V0LFJBmCnAsb8CAAFMAAdlbGVtZW50cQB+ADd4cHEAfgAUc3EAfgBec3EAfgA2c3EAfgA2c3EAfgA2c3EAfgA2cHNxAH4ANnBwcQB+AExwcQB+AGJxAH4A7HBxAH4A8nNxAH4ANnBzcQB+ADZwc3EAfgA2cHBxAH4A+nBxAH4A/3EAfgEAcHEAfgEHcQB+AQhwc3EAfgEMc3EAfgEPdwwAAAAQP0AAAAAAAAFxAH4BFXhxAH4BF3BxAH4BGXBxAH4BGnBxAH4AxnBxAH4AY3BxAH4BHXEAfgEec3EAfgB3cQB+AGhxAH4AbQ=="}
		AnnotationCmd:105 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageGlobalChangeSnippet.StorageBackupPoint","calleeTxId":12}}
		NopCmd
		AssumeExpCmd LAnd(Eq(tacCalldatasize!!8:3 0x4 ) Eq(tacCalldatasize!!8:3 0x4 ) )
		NopCmd
		AssumeExpCmd Eq(tacCalldatabufCANON0@12:2 0x18160ddd00000000000000000000000000000000000000000000000000000000 )
		LabelCmd:105 "Start procedure CurveTokenExample-totalSupply()"
		AnnotationCmd:105 JSON{"key":{"name":"fps.free-pointer-is-scalarized","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true}
		AssignExpCmd:105 R365:54 Select(tacExtcodesize!!9:4 Apply(to_skey:bif R32:103) )
		NopCmd
		AssumeExpCmd Gt(R365:54 0x0 )
		AnnotationCmd:105 JSON{"key":{"name":"internal.func.finder.info","type":"analysis.ip.InternalFunctionFinderReport","erasureStrategy":"Erased"},"value":"rO0ABXNyAChhbmFseXNpcy5pcC5JbnRlcm5hbEZ1bmN0aW9uRmluZGVyUmVwb3J0ian+bYn1VdACAAFMABN1bnJlc29sdmVkRnVuY3Rpb25zdAAPTGphdmEvdXRpbC9TZXQ7eHBzcgAhZGF0YXN0cnVjdHVyZXMuTGlua2VkQXJyYXlIYXNoU2V0AAAAAAAAAAEDAAJGAApsb2FkRmFjdG9yTAAJaGFzaFRhYmxldAAuTGRhdGFzdHJ1Y3R1cmVzL2FycmF5aGFzaHRhYmxlL0FycmF5SGFzaFRhYmxlO3hwdwgAAAAAQAAAAHg="}
		AnnotationCmd:105 JSON{"key":{"name":"fps.free-pointer-is-scalarized","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true}
		NopCmd
		AssumeExpCmd LNot(Lt(tacCalldatasize!!8:3 0x4 ) )
		NopCmd
		AssumeExpCmd Gt(0x40c10f19 tacSighash!!46:47 )
		NopCmd
		AssumeExpCmd LNot(Eq(0x6fdde03 tacSighash!!46:47 ) )
		NopCmd
		AssumeExpCmd LNot(Eq(0x95ea7b3 tacSighash!!46:47 ) )
		NopCmd
		AssumeExpCmd Eq(0x18160ddd tacSighash!!46:47 )
		AnnotationCmd:105 JSON{"key":{"name":"internal.func.start","type":"analysis.ip.InternalFuncStartAnnotation","erasureStrategy":"CallTrace"},"value":{"id":15,"startPc":1205,"args":[],"methodSignature":{"#class":"spec.cvlast.QualifiedMethodSignature.QualifiedMethodSig","qualifiedMethodName":{"#class":"spec.cvlast.QualifiedFunction","host":{"name":"CurveTokenExample"},"methodId":"totalSupply"},"params":[],"res":[{"#class":"spec.cvlast.VMParam.Unnamed","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256}}]},"stackOffsetToArgPos":{},"callSiteSrc":{"source":3,"begin":3954,"len":364,"jumpType":"ENTER","address":"ce4604a0000000000000000000000008","sourceContext":{"indexToFilepath":{"0":"contracts/Context.sol","1":"contracts/CurveToken.sol","2":"contracts/CurveTokenExample.sol","3":"contracts/ERC20.sol","4":"contracts/IERC20.sol","5":"contracts/IERC20Metadata.sol"},"sourceDir":".post_autofinders.0"}}}}
		AnnotationCmd:105 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet","value":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"CANON87!!29","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.scalarization.sort","type":"vc.data.ScalarizationSort","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.ScalarizationSort.Split","idx":"2"}},{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.storage.bit-width","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":256},{"key":{"name":"tac.storage.pretty.paths","type":"analysis.storage.DisplayPaths","erasureStrategy":"Erased"},"value":{"paths":[{"#class":"analysis.storage.DisplayPath.Root","name":"_totalSupply"}]}},{"key":{"name":"tac.slot.type","type":"spec.cvlast.typedescriptors.EVMTypeDescriptor$EVMValueType","erasureStrategy":"Canonical"},"value":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256}},{"key":{"name":"tac.storage.non-indexed-path","type":"analysis.storage.StorageAnalysisResult$NonIndexedPath","erasureStrategy":"Canonical"},"value":{"#class":"analysis.storage.StorageAnalysisResult.NonIndexedPath.Root","slot":"2"}},{"key":{"name":"tac.storage","type":"java.math.BigInteger","erasureStrategy":"Canonical"},"value":"ce4604a0000000000000000000000008"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1021}]},"displayPath":{"#class":"analysis.storage.DisplayPath.Root","name":"_totalSupply"},"storageType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256},"contractInstance":"ce4604a0000000000000000000000008","linkableStorageReadId":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet.Id","id":14}}}
		AnnotationCmd:105 JSON{"key":{"name":"internal.func.end","type":"analysis.ip.InternalFuncExitAnnotation","erasureStrategy":"Canonical"},"value":{"id":15,"rets":[{"s":{"namePrefix":"CANON87!!29","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.scalarization.sort","type":"vc.data.ScalarizationSort","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.ScalarizationSort.Split","idx":"2"}},{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.storage.bit-width","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":256},{"key":{"name":"tac.storage.pretty.paths","type":"analysis.storage.DisplayPaths","erasureStrategy":"Erased"},"value":{"paths":[{"#class":"analysis.storage.DisplayPath.Root","name":"_totalSupply"}]}},{"key":{"name":"tac.slot.type","type":"spec.cvlast.typedescriptors.EVMTypeDescriptor$EVMValueType","erasureStrategy":"Canonical"},"value":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256}},{"key":{"name":"tac.storage.non-indexed-path","type":"analysis.storage.StorageAnalysisResult$NonIndexedPath","erasureStrategy":"Canonical"},"value":{"#class":"analysis.storage.StorageAnalysisResult.NonIndexedPath.Root","slot":"2"}},{"key":{"name":"tac.storage","type":"java.math.BigInteger","erasureStrategy":"Canonical"},"value":"ce4604a0000000000000000000000008"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1023}]},"offset":0}],"functionLayout":{"0":{"#class":"analysis.ip.InternalFuncValueLocation.Scalar"}}}}
		AnnotationCmd:105 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.EVMFunctionReturnWrite","returnbufOffset":"0","returnValueSym":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"CANON87!!29","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.scalarization.sort","type":"vc.data.ScalarizationSort","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.ScalarizationSort.Split","idx":"2"}},{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.storage.bit-width","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":256},{"key":{"name":"tac.storage.pretty.paths","type":"analysis.storage.DisplayPaths","erasureStrategy":"Erased"},"value":{"paths":[{"#class":"analysis.storage.DisplayPath.Root","name":"_totalSupply"}]}},{"key":{"name":"tac.slot.type","type":"spec.cvlast.typedescriptors.EVMTypeDescriptor$EVMValueType","erasureStrategy":"Canonical"},"value":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256}},{"key":{"name":"tac.storage.non-indexed-path","type":"analysis.storage.StorageAnalysisResult$NonIndexedPath","erasureStrategy":"Canonical"},"value":{"#class":"analysis.storage.StorageAnalysisResult.NonIndexedPath.Root","slot":"2"}},{"key":{"name":"tac.storage","type":"java.math.BigInteger","erasureStrategy":"Canonical"},"value":"ce4604a0000000000000000000000008"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1023}]},"callIndex":12}}
		AnnotationCmd:105 JSON{"key":{"name":"tac.return.path","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		LabelCmd:105 "End procedure CurveTokenExample-totalSupply()"
		AssignExpCmd:105 tacReturndata!!374:78 Store(tacReturndata!!459:78 0x0 CANON87!!29:104 )
		AssignExpCmd:105 tacMCANON2!!375:10 Store(tacMCANON2!!456:10 0x140 CANON87!!29:104 )
		AnnotationCmd:105 JSON{"key":{"name":"call.trace.pop","type":"analysis.icfg.Inliner$CallStack$PopRecord","erasureStrategy":"Canonical"},"value":"rO0ABXNyAClhbmFseXNpcy5pY2ZnLklubGluZXIkQ2FsbFN0YWNrJFBvcFJlY29yZPAPfwSLdCWJAgABSQAIY2FsbGVlSWR4cAAAAAw="}
		JumpCmd:105 3_0_0_9_0_0
	}
	Block 1_0_0_1_0_0 Succ [0_0_0_3_0_0] {
		AssumeNotCmd:74 false
		AnnotationCmd:56 JSON{"key":{"name":"pta.fake-return.start","type":"analysis.CmdPointer","erasureStrategy":"Erased"},"value":{"block":{"#class":"tac.BlockIdentifier","origStartPc":1608,"stkTop":1009,"decompCopy":0,"calleeIdx":0,"topOfStackValue":2,"freshCopy":0},"pos":1}}
		AnnotationCmd:56 JSON{"key":{"name":"pta.fake-return.end","type":"analysis.CmdPointer","erasureStrategy":"Erased"},"value":{"block":{"#class":"tac.BlockIdentifier","origStartPc":1608,"stkTop":1009,"decompCopy":0,"calleeIdx":0,"topOfStackValue":2,"freshCopy":0},"pos":6}}
		AssumeNotCmd:129 false
		AssignExpCmd:130 R376:131 Select(tacMCANON2!!184:9 0x100 )
		NopCmd
		AssumeExpCmd LNot(Lt(R376:131 R151:72 ) )
		AssignExpCmd:132 R378:69 Sub(R376:131 R151:72 )
		AssignExpCmd:70 tacMCANON1!!379:7 Store(tacMCANON1!!150:7 0xe0 R378:69 )
		AnnotationCmd:56 JSON{"key":{"name":"pta.end-allocation","type":"analysis.alloc.AllocationAnalysis$AbstractLocation","erasureStrategy":"Erased"},"value":{"prevFPWriteIdx":1,"nextFPWriteCmd":{"block":{"#class":"tac.BlockIdentifier","origStartPc":16,"stkTop":1024,"decompCopy":0,"calleeIdx":0,"topOfStackValue":2,"freshCopy":0},"pos":44},"sort":{"#class":"analysis.alloc.AllocationAnalysis.Alloc.ConstBlock","sz":"40"}}}
		AnnotationCmd:56 JSON{"key":{"name":"internal.func.start","type":"analysis.ip.InternalFuncStartAnnotation","erasureStrategy":"CallTrace"},"value":{"id":2,"startPc":3822,"args":[],"methodSignature":{"#class":"spec.cvlast.QualifiedMethodSignature.QualifiedMethodSig","qualifiedMethodName":{"#class":"spec.cvlast.QualifiedFunction","host":{"name":"curve"},"methodId":"_A"},"params":[],"res":[{"#class":"spec.cvlast.VMParam.Unnamed","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256}}]},"stackOffsetToArgPos":{},"callSiteSrc":{"source":7,"begin":6351,"len":4,"jumpType":"ENTER","address":"ce4604a0000000000000000000000028","sourceContext":{"indexToFilepath":{"0":"contracts/Context.sol","1":"contracts/CurveToken.sol","2":"contracts/CurveTokenExample.sol","3":"contracts/ERC20.sol","4":"contracts/IERC20.sol","5":"contracts/IERC20Metadata.sol","6":"contracts/ReentrancyGuard.sol","7":"contracts/curve.sol"},"sourceDir":".post_autofinders.2"}}}}
		AnnotationCmd:56 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet","value":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"CANON99!!31","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.scalarization.sort","type":"vc.data.ScalarizationSort","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.ScalarizationSort.Split","idx":"5"}},{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.storage.bit-width","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":256},{"key":{"name":"tac.storage.pretty.paths","type":"analysis.storage.DisplayPaths","erasureStrategy":"Erased"},"value":{"paths":[{"#class":"analysis.storage.DisplayPath.Root","name":"future_A"}]}},{"key":{"name":"tac.slot.type","type":"spec.cvlast.typedescriptors.EVMTypeDescriptor$EVMValueType","erasureStrategy":"Canonical"},"value":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256}},{"key":{"name":"tac.storage.non-indexed-path","type":"analysis.storage.StorageAnalysisResult$NonIndexedPath","erasureStrategy":"Canonical"},"value":{"#class":"analysis.storage.StorageAnalysisResult.NonIndexedPath.Root","slot":"5"}},{"key":{"name":"tac.storage","type":"java.math.BigInteger","erasureStrategy":"Canonical"},"value":"ce4604a0000000000000000000000028"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1015}]},"displayPath":{"#class":"analysis.storage.DisplayPath.Root","name":"future_A"},"storageType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256},"contractInstance":"ce4604a0000000000000000000000028","linkableStorageReadId":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet.Id","id":2}}}
		AnnotationCmd:56 JSON{"key":{"name":"internal.func.end","type":"analysis.ip.InternalFuncExitAnnotation","erasureStrategy":"Canonical"},"value":{"id":2,"rets":[{"s":{"namePrefix":"CANON99!!31","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.scalarization.sort","type":"vc.data.ScalarizationSort","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.ScalarizationSort.Split","idx":"5"}},{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.storage.bit-width","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":256},{"key":{"name":"tac.storage.pretty.paths","type":"analysis.storage.DisplayPaths","erasureStrategy":"Erased"},"value":{"paths":[{"#class":"analysis.storage.DisplayPath.Root","name":"future_A"}]}},{"key":{"name":"tac.slot.type","type":"spec.cvlast.typedescriptors.EVMTypeDescriptor$EVMValueType","erasureStrategy":"Canonical"},"value":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256}},{"key":{"name":"tac.storage.non-indexed-path","type":"analysis.storage.StorageAnalysisResult$NonIndexedPath","erasureStrategy":"Canonical"},"value":{"#class":"analysis.storage.StorageAnalysisResult.NonIndexedPath.Root","slot":"5"}},{"key":{"name":"tac.storage","type":"java.math.BigInteger","erasureStrategy":"Canonical"},"value":"ce4604a0000000000000000000000028"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1017}]},"offset":0}],"functionLayout":{"0":{"#class":"analysis.ip.InternalFuncValueLocation.Scalar"}}}}
		AssignExpCmd:133 tacMCANON2!!382:9 Store(tacMCANON2!!184:9 0x120 0x3842f77600000000000000000000000000000000000000000000000000000000 )
		AnnotationCmd:56 JSON{"key":{"name":"dsa.assign.start","type":"java.lang.String","erasureStrategy":"Erased"},"value":"4639_1009_0_0_0_0 -> 4643_1007_0_0_0_0"}
		LabelCmd:56 "Parallel assignment for R4175:bv256, R4219:bv256, B4220:bool, R4221:bv256 := R6292:bv256, R397:bv256, B4076:bool, R4077:bv256"
		AnnotationCmd:56 JSON{"key":{"name":"dsa.assign.end","type":"java.lang.String","erasureStrategy":"Erased"},"value":"4639_1009_0_0_0_0 -> 4643_1007_0_0_0_0"}
		AnnotationCmd:56 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.LoopSnippet.StartLoopSnippet","loopIndex":0,"loopSource":"unknown loop source code"}}
		AnnotationCmd:56 JSON{"key":{"name":"start_loop.cmd","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		AnnotationCmd:56 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.LoopSnippet.StartIter","iteration":1}}
		AssignExpCmd:134 R383:135 Select(tacMCANON1!!379:7 0xc0 )
		AssignExpCmd:136 tacMCANON2!!384:9 Store(tacMCANON2!!382:9 0x124 R383:135 )
		AnnotationCmd:56 JSON{"key":{"name":"dsa.assign.start","type":"java.lang.String","erasureStrategy":"Erased"},"value":"4674_1005_0_0_0_0 -> 4643_1007_0_0_0_0"}
		LabelCmd:56 "Parallel assignment for R4175:bv256, R4219:bv256, B4220:bool, R4221:bv256 := R3948:bv256, R3993:bv256, B4217:bool, R4214:bv256"
		AnnotationCmd:56 JSON{"key":{"name":"dsa.assign.end","type":"java.lang.String","erasureStrategy":"Erased"},"value":"4674_1005_0_0_0_0 -> 4643_1007_0_0_0_0"}
		AnnotationCmd:56 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.LoopSnippet.EndIter","iteration":1}}
		AnnotationCmd:56 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.LoopSnippet.StartIter","iteration":2}}
		AssignExpCmd:134 R385:135 Select(tacMCANON1!!379:7 0xe0 )
		AssignExpCmd:136 tacMCANON2!!386:9 Store(tacMCANON2!!384:9 0x144 R385:135 )
		AnnotationCmd:56 JSON{"key":{"name":"dsa.assign.start","type":"java.lang.String","erasureStrategy":"Erased"},"value":"4674_1005_0_0_0_0 -> 4643_1007_0_0_0_0"}
		LabelCmd:56 "Parallel assignment for R4175:bv256, R4219:bv256, B4220:bool, R4221:bv256 := R3948:bv256, R3993:bv256, B4217:bool, R4214:bv256"
		AnnotationCmd:56 JSON{"key":{"name":"dsa.assign.end","type":"java.lang.String","erasureStrategy":"Erased"},"value":"4674_1005_0_0_0_0 -> 4643_1007_0_0_0_0"}
		AnnotationCmd:56 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.LoopSnippet.EndIter","iteration":2}}
		AnnotationCmd:56 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.LoopSnippet.EndLoopSnippet","loopId":0}}
		AnnotationCmd:56 JSON{"key":{"name":"end_loop.cmd","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		AssignExpCmd:137 tacMCANON2!!388:9 Store(tacMCANON2!!386:9 0x164 CANON99!!31:138 )
		AssignExpCmd:133 R389:93 0x120
		NopCmd
		AssignHavocCmd:133 R391:65
		AssignHavocCmd:56 tacReturndata!!392:78
		JumpCmd:56 0_0_0_3_0_0
	}
	Block 1_0_0_9_0_0 Succ [0_0_0_11_0_0] {
		AssumeNotCmd:112 false
		AnnotationCmd:105 JSON{"key":{"name":"pta.fake-return.start","type":"analysis.CmdPointer","erasureStrategy":"Erased"},"value":{"block":{"#class":"tac.BlockIdentifier","origStartPc":1608,"stkTop":1009,"decompCopy":0,"calleeIdx":0,"topOfStackValue":2,"freshCopy":0},"pos":1}}
		AnnotationCmd:105 JSON{"key":{"name":"pta.fake-return.end","type":"analysis.CmdPointer","erasureStrategy":"Erased"},"value":{"block":{"#class":"tac.BlockIdentifier","origStartPc":1608,"stkTop":1009,"decompCopy":0,"calleeIdx":0,"topOfStackValue":2,"freshCopy":0},"pos":6}}
		AssumeNotCmd:139 false
		AssignExpCmd:140 R393:131 Select(tacMCANON2!!327:10 0x100 )
		NopCmd
		AssumeExpCmd LNot(Lt(R393:131 R294:72 ) )
		AssignExpCmd:141 R395:69 Sub(R393:131 R294:72 )
		AssignExpCmd:110 tacMCANON1!!396:8 Store(tacMCANON1!!293:8 0xe0 R395:69 )
		AnnotationCmd:105 JSON{"key":{"name":"pta.end-allocation","type":"analysis.alloc.AllocationAnalysis$AbstractLocation","erasureStrategy":"Erased"},"value":{"prevFPWriteIdx":1,"nextFPWriteCmd":{"block":{"#class":"tac.BlockIdentifier","origStartPc":16,"stkTop":1024,"decompCopy":0,"calleeIdx":0,"topOfStackValue":2,"freshCopy":0},"pos":44},"sort":{"#class":"analysis.alloc.AllocationAnalysis.Alloc.ConstBlock","sz":"40"}}}
		AnnotationCmd:105 JSON{"key":{"name":"internal.func.start","type":"analysis.ip.InternalFuncStartAnnotation","erasureStrategy":"CallTrace"},"value":{"id":13,"startPc":3822,"args":[],"methodSignature":{"#class":"spec.cvlast.QualifiedMethodSignature.QualifiedMethodSig","qualifiedMethodName":{"#class":"spec.cvlast.QualifiedFunction","host":{"name":"curve"},"methodId":"_A"},"params":[],"res":[{"#class":"spec.cvlast.VMParam.Unnamed","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256}}]},"stackOffsetToArgPos":{},"callSiteSrc":{"source":7,"begin":6351,"len":4,"jumpType":"ENTER","address":"ce4604a0000000000000000000000028","sourceContext":{"indexToFilepath":{"0":"contracts/Context.sol","1":"contracts/CurveToken.sol","2":"contracts/CurveTokenExample.sol","3":"contracts/ERC20.sol","4":"contracts/IERC20.sol","5":"contracts/IERC20Metadata.sol","6":"contracts/ReentrancyGuard.sol","7":"contracts/curve.sol"},"sourceDir":".post_autofinders.2"}}}}
		AnnotationCmd:105 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet","value":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"CANON99!!31","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.scalarization.sort","type":"vc.data.ScalarizationSort","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.ScalarizationSort.Split","idx":"5"}},{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.storage.bit-width","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":256},{"key":{"name":"tac.storage.pretty.paths","type":"analysis.storage.DisplayPaths","erasureStrategy":"Erased"},"value":{"paths":[{"#class":"analysis.storage.DisplayPath.Root","name":"future_A"}]}},{"key":{"name":"tac.slot.type","type":"spec.cvlast.typedescriptors.EVMTypeDescriptor$EVMValueType","erasureStrategy":"Canonical"},"value":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256}},{"key":{"name":"tac.storage.non-indexed-path","type":"analysis.storage.StorageAnalysisResult$NonIndexedPath","erasureStrategy":"Canonical"},"value":{"#class":"analysis.storage.StorageAnalysisResult.NonIndexedPath.Root","slot":"5"}},{"key":{"name":"tac.storage","type":"java.math.BigInteger","erasureStrategy":"Canonical"},"value":"ce4604a0000000000000000000000028"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1015}]},"displayPath":{"#class":"analysis.storage.DisplayPath.Root","name":"future_A"},"storageType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256},"contractInstance":"ce4604a0000000000000000000000028","linkableStorageReadId":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet.Id","id":12}}}
		AnnotationCmd:105 JSON{"key":{"name":"internal.func.end","type":"analysis.ip.InternalFuncExitAnnotation","erasureStrategy":"Canonical"},"value":{"id":13,"rets":[{"s":{"namePrefix":"CANON99!!31","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.scalarization.sort","type":"vc.data.ScalarizationSort","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.ScalarizationSort.Split","idx":"5"}},{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.storage.bit-width","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":256},{"key":{"name":"tac.storage.pretty.paths","type":"analysis.storage.DisplayPaths","erasureStrategy":"Erased"},"value":{"paths":[{"#class":"analysis.storage.DisplayPath.Root","name":"future_A"}]}},{"key":{"name":"tac.slot.type","type":"spec.cvlast.typedescriptors.EVMTypeDescriptor$EVMValueType","erasureStrategy":"Canonical"},"value":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256}},{"key":{"name":"tac.storage.non-indexed-path","type":"analysis.storage.StorageAnalysisResult$NonIndexedPath","erasureStrategy":"Canonical"},"value":{"#class":"analysis.storage.StorageAnalysisResult.NonIndexedPath.Root","slot":"5"}},{"key":{"name":"tac.storage","type":"java.math.BigInteger","erasureStrategy":"Canonical"},"value":"ce4604a0000000000000000000000028"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1017}]},"offset":0}],"functionLayout":{"0":{"#class":"analysis.ip.InternalFuncValueLocation.Scalar"}}}}
		AssignExpCmd:142 tacMCANON2!!399:10 Store(tacMCANON2!!327:10 0x120 0x3842f77600000000000000000000000000000000000000000000000000000000 )
		AnnotationCmd:105 JSON{"key":{"name":"dsa.assign.start","type":"java.lang.String","erasureStrategy":"Erased"},"value":"4639_1009_0_0_0_0 -> 4643_1007_0_0_0_0"}
		LabelCmd:105 "Parallel assignment for R4175:bv256, R4219:bv256, B4220:bool, R4221:bv256 := R6292:bv256, R397:bv256, B4076:bool, R4077:bv256"
		AnnotationCmd:105 JSON{"key":{"name":"dsa.assign.end","type":"java.lang.String","erasureStrategy":"Erased"},"value":"4639_1009_0_0_0_0 -> 4643_1007_0_0_0_0"}
		AnnotationCmd:105 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.LoopSnippet.StartLoopSnippet","loopIndex":4,"loopSource":"unknown loop source code"}}
		AnnotationCmd:105 JSON{"key":{"name":"start_loop.cmd","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		AnnotationCmd:105 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.LoopSnippet.StartIter","iteration":1}}
		AssignExpCmd:143 R400:135 Select(tacMCANON1!!396:8 0xc0 )
		AssignExpCmd:144 tacMCANON2!!401:10 Store(tacMCANON2!!399:10 0x124 R400:135 )
		AnnotationCmd:105 JSON{"key":{"name":"dsa.assign.start","type":"java.lang.String","erasureStrategy":"Erased"},"value":"4674_1005_0_0_0_0 -> 4643_1007_0_0_0_0"}
		LabelCmd:105 "Parallel assignment for R4175:bv256, R4219:bv256, B4220:bool, R4221:bv256 := R3948:bv256, R3993:bv256, B4217:bool, R4214:bv256"
		AnnotationCmd:105 JSON{"key":{"name":"dsa.assign.end","type":"java.lang.String","erasureStrategy":"Erased"},"value":"4674_1005_0_0_0_0 -> 4643_1007_0_0_0_0"}
		AnnotationCmd:105 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.LoopSnippet.EndIter","iteration":1}}
		AnnotationCmd:105 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.LoopSnippet.StartIter","iteration":2}}
		AssignExpCmd:143 R402:135 Select(tacMCANON1!!396:8 0xe0 )
		AssignExpCmd:144 tacMCANON2!!403:10 Store(tacMCANON2!!401:10 0x144 R402:135 )
		AnnotationCmd:105 JSON{"key":{"name":"dsa.assign.start","type":"java.lang.String","erasureStrategy":"Erased"},"value":"4674_1005_0_0_0_0 -> 4643_1007_0_0_0_0"}
		LabelCmd:105 "Parallel assignment for R4175:bv256, R4219:bv256, B4220:bool, R4221:bv256 := R3948:bv256, R3993:bv256, B4217:bool, R4214:bv256"
		AnnotationCmd:105 JSON{"key":{"name":"dsa.assign.end","type":"java.lang.String","erasureStrategy":"Erased"},"value":"4674_1005_0_0_0_0 -> 4643_1007_0_0_0_0"}
		AnnotationCmd:105 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.LoopSnippet.EndIter","iteration":2}}
		AnnotationCmd:105 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.LoopSnippet.EndLoopSnippet","loopId":4}}
		AnnotationCmd:105 JSON{"key":{"name":"end_loop.cmd","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		AssignExpCmd:145 tacMCANON2!!405:10 Store(tacMCANON2!!403:10 0x164 CANON99!!31:138 )
		AssignExpCmd:142 R406:93 0x120
		NopCmd
		AssignHavocCmd:142 R408:65
		AssignHavocCmd:105 tacReturndata!!409:78
		JumpCmd:105 0_0_0_11_0_0
	}
	Block 3_0_0_1_0_0 Succ [4_0_0_0_0_0] {
		AssumeNotCmd:146 false
		AnnotationCmd:56 JSON{"key":{"name":"pta.fake-return.start","type":"analysis.CmdPointer","erasureStrategy":"Erased"},"value":{"block":{"#class":"tac.BlockIdentifier","origStartPc":3278,"stkTop":1016,"decompCopy":0,"calleeIdx":0,"topOfStackValue":2,"freshCopy":0},"pos":1}}
		AnnotationCmd:56 JSON{"key":{"name":"pta.fake-return.end","type":"analysis.CmdPointer","erasureStrategy":"Erased"},"value":{"block":{"#class":"tac.BlockIdentifier","origStartPc":3278,"stkTop":1016,"decompCopy":0,"calleeIdx":0,"topOfStackValue":2,"freshCopy":0},"pos":6}}
		AssumeNotCmd:129 false
		AssignExpCmd:130 R410:147 Select(tacMCANON2!!232:9 0x140 )
		NopCmd
		AssumeExpCmd Apply(mul_noofl:bif R440:67 0x8ac7230489e80000)
		NopCmd
		AssignExpCmd:148 I419:54 IntMul(Apply(safe_math_promotion:bif R440:67) 0x8ac7230489e80000)
		NopCmd
		NopCmd
		AssumeExpCmd Gt(R410:147 0x0 )
		AssignExpCmd:149 R422:150 Div(Apply(safe_math_narrow:bif I419:54) R410:147 )
		AnnotationCmd:56 JSON{"key":{"name":"internal.func.end","type":"analysis.ip.InternalFuncExitAnnotation","erasureStrategy":"Canonical"},"value":{"id":0,"rets":[{"s":{"namePrefix":"R422","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1023}]},"offset":0}],"functionLayout":{"0":{"#class":"analysis.ip.InternalFuncValueLocation.Scalar"}}}}
		AnnotationCmd:56 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.EVMFunctionReturnWrite","returnbufOffset":"0","returnValueSym":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R422","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1023}]},"callIndex":1}}
		AnnotationCmd:56 JSON{"key":{"name":"tac.return.path","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		LabelCmd:56 "End procedure curve-getVirtualPrice()"
		NopCmd
		AnnotationCmd:56 JSON{"key":{"name":"call.trace.pop","type":"analysis.icfg.Inliner$CallStack$PopRecord","erasureStrategy":"Canonical"},"value":"rO0ABXNyAClhbmFseXNpcy5pY2ZnLklubGluZXIkQ2FsbFN0YWNrJFBvcFJlY29yZPAPfwSLdCWJAgABSQAIY2FsbGVlSWR4cAAAAAE="}
	}
	Block 3_0_0_9_0_0 Succ [9_0_0_0_0_0] {
		AssumeNotCmd:151 false
		AnnotationCmd:105 JSON{"key":{"name":"pta.fake-return.start","type":"analysis.CmdPointer","erasureStrategy":"Erased"},"value":{"block":{"#class":"tac.BlockIdentifier","origStartPc":3278,"stkTop":1016,"decompCopy":0,"calleeIdx":0,"topOfStackValue":2,"freshCopy":0},"pos":1}}
		AnnotationCmd:105 JSON{"key":{"name":"pta.fake-return.end","type":"analysis.CmdPointer","erasureStrategy":"Erased"},"value":{"block":{"#class":"tac.BlockIdentifier","origStartPc":3278,"stkTop":1016,"decompCopy":0,"calleeIdx":0,"topOfStackValue":2,"freshCopy":0},"pos":6}}
		AssumeNotCmd:139 false
		AssignExpCmd:140 R425:147 Select(tacMCANON2!!375:10 0x140 )
		NopCmd
		AssumeExpCmd Apply(mul_noofl:bif R450:67 0x8ac7230489e80000)
		NopCmd
		AssignExpCmd:152 I434:54 IntMul(Apply(safe_math_promotion:bif R450:67) 0x8ac7230489e80000)
		NopCmd
		NopCmd
		AssumeExpCmd Gt(R425:147 0x0 )
		AssignExpCmd:153 R437:150 Div(Apply(safe_math_narrow:bif I434:54) R425:147 )
		AnnotationCmd:105 JSON{"key":{"name":"internal.func.end","type":"analysis.ip.InternalFuncExitAnnotation","erasureStrategy":"Canonical"},"value":{"id":11,"rets":[{"s":{"namePrefix":"R437","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1023}]},"offset":0}],"functionLayout":{"0":{"#class":"analysis.ip.InternalFuncValueLocation.Scalar"}}}}
		AnnotationCmd:105 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.EVMFunctionReturnWrite","returnbufOffset":"0","returnValueSym":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R437","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1023}]},"callIndex":9}}
		AnnotationCmd:105 JSON{"key":{"name":"tac.return.path","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		LabelCmd:105 "End procedure curve-getVirtualPrice()"
		NopCmd
		AnnotationCmd:105 JSON{"key":{"name":"call.trace.pop","type":"analysis.icfg.Inliner$CallStack$PopRecord","erasureStrategy":"Canonical"},"value":"rO0ABXNyAClhbmFseXNpcy5pY2ZnLklubGluZXIkQ2FsbFN0YWNrJFBvcFJlY29yZPAPfwSLdCWJAgABSQAIY2FsbGVlSWR4cAAAAAk="}
	}
	Block 2_0_0_1_0_0 Succ [0_0_0_4_0_0] {
		AssumeNotCmd:133 false
		AnnotationCmd:56 JSON{"key":{"name":"pta.fake-return.start","type":"analysis.CmdPointer","erasureStrategy":"Erased"},"value":{"block":{"#class":"tac.BlockIdentifier","origStartPc":3129,"stkTop":1017,"decompCopy":0,"calleeIdx":0,"topOfStackValue":2,"freshCopy":0},"pos":1}}
		AnnotationCmd:56 JSON{"key":{"name":"pta.fake-return.end","type":"analysis.CmdPointer","erasureStrategy":"Erased"},"value":{"block":{"#class":"tac.BlockIdentifier","origStartPc":3129,"stkTop":1017,"decompCopy":0,"calleeIdx":0,"topOfStackValue":2,"freshCopy":0},"pos":6}}
		AssumeNotCmd:129 false
		AssignExpCmd:130 R440:67 Select(tacMCANON2!!218:9 0x120 )
		AssignExpCmd:56 B442:54 Le(CANON19!!25:154 0xffffffffffffffffffffffffffffffffffffffff )
		AssignExpCmd:56 B443:54 Ge(CANON19!!25:154 0x0 )
		NopCmd
		AssumeExpCmd LAnd(B442:54 B443:54 )
		AnnotationCmd:56 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet","value":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"CANON19!!25","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.scalarization.sort","type":"vc.data.ScalarizationSort","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.ScalarizationSort.Packed","packedStart":{"#class":"vc.data.ScalarizationSort.Split","idx":"c"},"start":0}},{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.storage.bit-width","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":160},{"key":{"name":"tac.storage.pretty.paths","type":"analysis.storage.DisplayPaths","erasureStrategy":"Erased"},"value":{"paths":[{"#class":"analysis.storage.DisplayPath.Root","name":"lp_token"}]}},{"key":{"name":"tac.slot.type","type":"spec.cvlast.typedescriptors.EVMTypeDescriptor$EVMValueType","erasureStrategy":"Canonical"},"value":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.address"}},{"key":{"name":"tac.storage.non-indexed-path","type":"analysis.storage.StorageAnalysisResult$NonIndexedPath","erasureStrategy":"Canonical"},"value":{"#class":"analysis.storage.StorageAnalysisResult.NonIndexedPath.Root","slot":"c"}},{"key":{"name":"tac.storage","type":"java.math.BigInteger","erasureStrategy":"Canonical"},"value":"ce4604a0000000000000000000000028"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1018}]},"displayPath":{"#class":"analysis.storage.DisplayPath.Root","name":"lp_token"},"storageType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.address"},"contractInstance":"ce4604a0000000000000000000000028","linkableStorageReadId":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet.Id","id":3}}}
		AnnotationCmd:56 JSON{"key":{"name":"init.reorder.fence","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		AssignExpCmd:146 tacMCANON2!!446:9 Store(tacMCANON2!!218:9 0x140 0x18160ddd00000000000000000000000000000000000000000000000000000000 )
		AssignExpCmd:146 R447:150 0x140
		AssignHavocCmd:146 R448:67
		AssignHavocCmd:56 tacReturndata!!449:78
		JumpCmd:56 0_0_0_4_0_0
	}
	Block 2_0_0_9_0_0 Succ [0_0_0_12_0_0] {
		AssumeNotCmd:142 false
		AnnotationCmd:105 JSON{"key":{"name":"pta.fake-return.start","type":"analysis.CmdPointer","erasureStrategy":"Erased"},"value":{"block":{"#class":"tac.BlockIdentifier","origStartPc":3129,"stkTop":1017,"decompCopy":0,"calleeIdx":0,"topOfStackValue":2,"freshCopy":0},"pos":1}}
		AnnotationCmd:105 JSON{"key":{"name":"pta.fake-return.end","type":"analysis.CmdPointer","erasureStrategy":"Erased"},"value":{"block":{"#class":"tac.BlockIdentifier","origStartPc":3129,"stkTop":1017,"decompCopy":0,"calleeIdx":0,"topOfStackValue":2,"freshCopy":0},"pos":6}}
		AssumeNotCmd:139 false
		AssignExpCmd:140 R450:67 Select(tacMCANON2!!361:10 0x120 )
		AssignExpCmd:105 B452:54 Le(CANON19!!25:154 0xffffffffffffffffffffffffffffffffffffffff )
		AssignExpCmd:105 B453:54 Ge(CANON19!!25:154 0x0 )
		NopCmd
		AssumeExpCmd LAnd(B452:54 B453:54 )
		AnnotationCmd:105 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet","value":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"CANON19!!25","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.scalarization.sort","type":"vc.data.ScalarizationSort","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.ScalarizationSort.Packed","packedStart":{"#class":"vc.data.ScalarizationSort.Split","idx":"c"},"start":0}},{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.storage.bit-width","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":160},{"key":{"name":"tac.storage.pretty.paths","type":"analysis.storage.DisplayPaths","erasureStrategy":"Erased"},"value":{"paths":[{"#class":"analysis.storage.DisplayPath.Root","name":"lp_token"}]}},{"key":{"name":"tac.slot.type","type":"spec.cvlast.typedescriptors.EVMTypeDescriptor$EVMValueType","erasureStrategy":"Canonical"},"value":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.address"}},{"key":{"name":"tac.storage.non-indexed-path","type":"analysis.storage.StorageAnalysisResult$NonIndexedPath","erasureStrategy":"Canonical"},"value":{"#class":"analysis.storage.StorageAnalysisResult.NonIndexedPath.Root","slot":"c"}},{"key":{"name":"tac.storage","type":"java.math.BigInteger","erasureStrategy":"Canonical"},"value":"ce4604a0000000000000000000000028"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1018}]},"displayPath":{"#class":"analysis.storage.DisplayPath.Root","name":"lp_token"},"storageType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.address"},"contractInstance":"ce4604a0000000000000000000000028","linkableStorageReadId":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet.Id","id":13}}}
		AnnotationCmd:105 JSON{"key":{"name":"init.reorder.fence","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		AssignExpCmd:151 tacMCANON2!!456:10 Store(tacMCANON2!!361:10 0x140 0x18160ddd00000000000000000000000000000000000000000000000000000000 )
		AssignExpCmd:151 R457:150 0x140
		AssignHavocCmd:151 R458:67
		AssignHavocCmd:105 tacReturndata!!459:78
		JumpCmd:105 0_0_0_12_0_0
	}
	Block 4_0_0_0_0_0 Succ [0_0_0_5_0_0] {
		AssumeNotCmd:56 false
		AssumeNotCmd:56 false
		AnnotationCmd JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageGlobalChangeSnippet.StorageTakeSnapshot","lhs":{"namePrefix":"lastStorage","tag":{"#class":"tac.Tag.BlockchainState"},"callIndex":0,"meta":[{"key":{"name":"cvl.local","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true},{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"lastStorage"},{"key":{"name":"cvl.type","type":"spec.cvlast.CVLType$PureCVLType","erasureStrategy":"CallTrace"},"value":{"#class":"spec.cvlast.CVLType.PureCVLType.VMInternal.BlockchainState"}},{"key":{"name":"cvl","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true},{"key":{"name":"cvl.display","type":"java.lang.String","erasureStrategy":"CallTrace"},"value":"lastStorage"}]}}}
		AssignExpCmd:155 CANON141!!460:156 Eq(I27 R422:150 )
		AssumeCmd:56 CANON141!!460:156
		AnnotationCmd:56 JSON{"key":{"name":"cvl.label.end","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		AnnotationCmd:157 JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Cmd","cmd":{"cmd_type":"spec.cvlast.CVLCmd.Simple.Apply","cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/specs/ViewReentrancy.spec","start":{"line":27,"character":4},"end":{"line":27,"character":15}},"exp":{"#class":"spec.cvlast.CVLExp.ApplyExp.ContractFunction.Symbolic","methodIdWithCallContext":{"#class":"spec.cvlast.ParametricMethod","methodId":"f","host":{"name":"curve"}},"args":[{"#class":"spec.cvlast.CVLExp.VariableExp","id":"e","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":0}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"env","fields":[{"fieldName":"msg","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"msg","fields":[{"fieldName":"sender","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"value","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}}]}},{"fieldName":"tx","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"tx","fields":[{"fieldName":"origin","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}}]}},{"fieldName":"block","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"block","fields":[{"fieldName":"coinbase","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"difficulty","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"gaslimit","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"number","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"timestamp","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}}]}}]},"cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/specs/ViewReentrancy.spec","start":{"line":27,"character":4},"end":{"line":27,"character":15}}},"twoStateIndex":"NEITHER"},{"#class":"spec.cvlast.CVLExp.VariableExp","id":"data","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":0}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.VMInternal.RawArgs"},"cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/specs/ViewReentrancy.spec","start":{"line":27,"character":4},"end":{"line":27,"character":15}}},"twoStateIndex":"NEITHER"}],"noRevert":true,"storage":{"#class":"spec.cvlast.CVLExp.VariableExp","id":"lastStorage","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":0}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.VMInternal.BlockchainState"},"cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/specs/ViewReentrancy.spec","start":{"line":27,"character":4},"end":{"line":27,"character":15}}},"twoStateIndex":"NEITHER"},"tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":0}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Void"},"cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/specs/ViewReentrancy.spec","start":{"line":27,"character":4},"end":{"line":27,"character":5}}}},"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":0}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}}}}}
		NopCmd
		NopCmd
		NopCmd
		NopCmd
		NopCmd
		NopCmd
		NopCmd
		AnnotationCmd:157 JSON{"key":{"name":"call.trace.push","type":"analysis.icfg.Inliner$CallStack$PushRecord","erasureStrategy":"Canonical"},"value":"rO0ABXNyACphbmFseXNpcy5pY2ZnLklubGluZXIkQ2FsbFN0YWNrJFB1c2hSZWNvcmSX8+DCTLCH+AIAA0kACGNhbGxlZUlkTAAGY2FsbGVldAATTHZjL2RhdGEvTWV0aG9kUmVmO0wAB3N1bW1hcnl0ABVMdmMvZGF0YS9DYWxsU3VtbWFyeTt4cAAAAAVzcgARdmMuZGF0YS5NZXRob2RSZWbJlJTzzU9pGAIAA0wABGF0dHJ0ABdMc2NlbmUvTWV0aG9kQXR0cmlidXRlO0wACmNvbnRyYWN0SWR0ABZMamF2YS9tYXRoL0JpZ0ludGVnZXI7TAAHc2lnSGFzaHQAEExldm0vU2lnaGFzaEludDt4cHNyABxzY2VuZS5NZXRob2RBdHRyaWJ1dGUkQ29tbW9uNHjdebdr9XMCAAB4cgAVc2NlbmUuTWV0aG9kQXR0cmlidXRlcYg2pYWutuUCAAB4cHNyABRqYXZhLm1hdGguQmlnSW50ZWdlcoz8nx+pO/sdAwAGSQAIYml0Q291bnRJAAliaXRMZW5ndGhJABNmaXJzdE5vbnplcm9CeXRlTnVtSQAMbG93ZXN0U2V0Qml0SQAGc2lnbnVtWwAJbWFnbml0dWRldAACW0J4cgAQamF2YS5sYW5nLk51bWJlcoaslR0LlOCLAgAAeHD///////////////7////+AAAAAXVyAAJbQqzzF/gGCFTgAgAAeHAAAAAQzkYEoAAAAAAAAAAAAAAAKHhzcgAOZXZtLlNpZ2hhc2hJbnRUdcqNMXEgeAIAAUwAAW5xAH4ABnhwc3EAfgAM///////////////+/////gAAAAF1cQB+ABAAAAAEQht42Xhw"}
		AssignExpCmd:157 M469:54 ByteMapDefinition(CANON152:bv256 -> Ite(Lt(CANON152:54 CANON150:6 ) Unconstrained(bv256) 0x0 ) )
		AssignExpCmd tacCalldatabuf@5:158 LongStore(M469:54 0x0 CANON148:5 0x0 CANON150:6 )
		NopCmd
		AssumeExpCmd Ge(CANON150:6 0x4 )
		NopCmd
		AssumeExpCmd Ge(0x7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff CANON150:6 )
		AssignExpCmd:157 B474 LAnd(Ge(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff CANON20:24 ) Le(0x0 CANON20:24 ) )
		AssertCmd:157 B474 "sanity bounds check on cvl to vm encoding of tacTmp!4816:int failed"
		AssignExpCmd:157 R475:54 Apply(safe_math_narrow:bif CANON20:24)
		NopCmd
		AssumeExpCmd LAnd(Le(R475:57 0xffffffffffffffffffffffffffffffffffffffff ) Ge(R475:57 0x0 ) )
		AssignExpCmd:157 B479 LAnd(Ge(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff CANON21:25 ) Le(0x0 CANON21:25 ) )
		AssertCmd:157 B479 "sanity bounds check on cvl to vm encoding of tacTmp!4819:int failed"
		AssignExpCmd:157 R480:54 Apply(safe_math_narrow:bif CANON21:25)
		NopCmd
		AssumeExpCmd LAnd(Le(R480:58 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff ) Ge(R480:58 0x0 ) )
		AssignExpCmd:157 B485 LAnd(Ge(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff CANON22:26 ) Le(0x0 CANON22:26 ) )
		AssertCmd:157 B485 "sanity bounds check on cvl to vm encoding of tacTmp!4823:int failed"
		AssignExpCmd:157 R486:54 Apply(safe_math_narrow:bif CANON22:26)
		NopCmd
		AssumeExpCmd LAnd(Le(R486:59 0xffffffffffffffffffffffffffffffffffffffff ) Ge(R486:59 0x0 ) )
		AssignExpCmd:157 B490 LAnd(Ge(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff CANON26:30 ) Le(0x0 CANON26:30 ) )
		AssertCmd:157 B490 "sanity bounds check on cvl to vm encoding of tacTmp!4826:int failed"
		AssignExpCmd:157 R491:54 Apply(safe_math_narrow:bif CANON26:30)
		NopCmd
		AssumeExpCmd LAnd(Le(R491:60 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff ) Ge(R491:60 0x0 ) )
		AssignExpCmd:157 B495 LAnd(Ge(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff CANON27:31 ) Le(0x0 CANON27:31 ) )
		AssertCmd:157 B495 "sanity bounds check on cvl to vm encoding of tacTmp!4829:int failed"
		AssignExpCmd:157 R496:54 Apply(safe_math_narrow:bif CANON27:31)
		NopCmd
		AssumeExpCmd LAnd(Le(R496:61 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff ) Ge(R496:61 0x0 ) )
		AssignExpCmd:157 B500 LAnd(Ge(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff CANON21:25 ) Le(0x0 CANON21:25 ) )
		AssertCmd:157 B500 "sanity bounds check on cvl to vm encoding of tacTmp!4832:int failed"
		AssignExpCmd:157 R501:54 Apply(safe_math_narrow:bif CANON21:25)
		AssignExpCmd:157 B503 LAnd(Ge(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff CANON20:24 ) Le(0x0 CANON20:24 ) )
		AssertCmd:157 B503 "sanity bounds check on cvl to vm encoding of tacTmp!4835:int failed"
		AssignExpCmd:157 R504:54 Apply(safe_math_narrow:bif CANON20:24)
		AssignExpCmd:157 R507:54 Select(tacBalance!!133:16 Apply(to_skey:bif R504:54) )
		AssignExpCmd:159 I508:54 IntSub(R507:54 R501:54 )
		AssignExpCmd:159 tacBalance!!509:16 Store(tacBalance!!133:16 Apply(to_skey:bif R504:54) I508:54 )
		AssignExpCmd:157 R510:54 Select(tacBalance!!509:16 Apply(to_skey:bif R34:46) )
		AssignExpCmd:159 R511:54 Add(R510:54 R501:54)
		NopCmd
		AssumeExpCmd Apply(add_noofl:bif R510:54 R501:54)
		AssignExpCmd:159 tacBalance!!513:16 Store(tacBalance!!509:16 Apply(to_skey:bif R34:46) R511:54 )
		AnnotationCmd:157 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.BalanceSnippet","srcAccountInfo":{"old":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R507","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}]},"new":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"I508","tag":{"#class":"tac.Tag.Int"},"callIndex":0,"meta":[{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}]},"addr":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R504","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}]}},"trgAccountInfo":{"old":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R510","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}]},"new":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R511","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}]},"addr":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R34","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"tacContractAt"},{"key":{"name":"tac.contract.sym.addr.name","type":"java.lang.String","erasureStrategy":"Erased"},"value":"curve"},{"key":{"name":"tac.contract.sym.addr","type":"java.math.BigInteger","erasureStrategy":"Erased"},"value":"ce4604a0000000000000000000000028"}]}},"transferredAmount":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R501","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}]}}}
		JumpCmd 0_0_0_5_0_0
	}
	Block 9_0_0_0_0_0 Succ [] {
		AssumeNotCmd:105 false
		AssumeNotCmd:105 false
		AnnotationCmd JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageGlobalChangeSnippet.StorageTakeSnapshot","lhs":{"namePrefix":"lastStorage","tag":{"#class":"tac.Tag.BlockchainState"},"callIndex":0,"meta":[{"key":{"name":"cvl.local","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true},{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"lastStorage"},{"key":{"name":"cvl.type","type":"spec.cvlast.CVLType$PureCVLType","erasureStrategy":"CallTrace"},"value":{"#class":"spec.cvlast.CVLType.PureCVLType.VMInternal.BlockchainState"}},{"key":{"name":"cvl","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true},{"key":{"name":"cvl.display","type":"java.lang.String","erasureStrategy":"CallTrace"},"value":"lastStorage"}]}}}
		AssignExpCmd:160 CANON265!!514:156 Eq(I10 R437:150 )
		AssumeCmd:105 CANON265!!514:156
		AnnotationCmd:105 JSON{"key":{"name":"cvl.label.end","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		AnnotationCmd:161 JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Cmd","cmd":{"cmd_type":"spec.cvlast.CVLCmd.Simple.Assert","cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/specs/ViewReentrancy.spec","start":{"line":29,"character":4},"end":{"line":29,"character":16}},"exp":{"#class":"spec.cvlast.CVLExp.VariableExp","id":"cond","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":0}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"},"cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/specs/ViewReentrancy.spec","start":{"line":29,"character":4},"end":{"line":29,"character":16}}},"twoStateIndex":"NEITHER"},"description":"","scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":0}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}}}}}
		AssertCmd:162 B26 ""
		AnnotationCmd:161 JSON{"key":{"name":"cvl.label.end","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
	}
	Block 0_0_0_5_0_0 Succ [0_0_0_6_0_0] {
		LabelCmd "Start procedure curve-func1_caller()"
		AnnotationCmd JSON{"key":{"name":"fps.free-pointer-is-scalarized","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true}
		AssignExpCmd R516:54 Select(tacExtcodesize!!9:4 Apply(to_skey:bif R34:63) )
		NopCmd
		AssumeExpCmd Gt(R516:54 0x0 )
		AnnotationCmd JSON{"key":{"name":"internal.func.finder.info","type":"analysis.ip.InternalFunctionFinderReport","erasureStrategy":"Erased"},"value":"rO0ABXNyAChhbmFseXNpcy5pcC5JbnRlcm5hbEZ1bmN0aW9uRmluZGVyUmVwb3J0ian+bYn1VdACAAFMABN1bnJlc29sdmVkRnVuY3Rpb25zdAAPTGphdmEvdXRpbC9TZXQ7eHBzcgAhZGF0YXN0cnVjdHVyZXMuTGlua2VkQXJyYXlIYXNoU2V0AAAAAAAAAAEDAAJGAApsb2FkRmFjdG9yTAAJaGFzaFRhYmxldAAuTGRhdGFzdHJ1Y3R1cmVzL2FycmF5aGFzaHRhYmxlL0FycmF5SGFzaFRhYmxlO3hwdwgAAAAAQAAAAHg="}
		AnnotationCmd JSON{"key":{"name":"fps.free-pointer-is-scalarized","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true}
		NopCmd
		AssumeExpCmd Eq(R480:58 0x0 )
		NopCmd
		AssumeExpCmd LNot(Lt(CANON150:6 0x4 ) )
		NopCmd
		AssumeExpCmd Gt(0x82c63066 tacSighash!!39:47 )
		NopCmd
		AssumeExpCmd LNot(Eq(0x3842f776 tacSighash!!39:47 ) )
		NopCmd
		AssumeExpCmd LNot(Eq(0x3d24a36b tacSighash!!39:47 ) )
		NopCmd
		AssumeExpCmd Eq(0x421b78d9 tacSighash!!39:47 )
		AnnotationCmd JSON{"key":{"name":"internal.func.start","type":"analysis.ip.InternalFuncStartAnnotation","erasureStrategy":"CallTrace"},"value":{"id":5,"startPc":1664,"args":[],"methodSignature":{"#class":"spec.cvlast.QualifiedMethodSignature.QualifiedMethodSig","qualifiedMethodName":{"#class":"spec.cvlast.QualifiedFunction","host":{"name":"curve"},"methodId":"func1_caller"},"params":[],"res":[{"#class":"spec.cvlast.VMParam.Unnamed","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256}}]},"stackOffsetToArgPos":{},"callSiteSrc":{"source":7,"begin":984,"len":351,"jumpType":"ENTER","address":"ce4604a0000000000000000000000028","sourceContext":{"indexToFilepath":{"0":"contracts/Context.sol","1":"contracts/CurveToken.sol","2":"contracts/CurveTokenExample.sol","3":"contracts/ERC20.sol","4":"contracts/IERC20.sol","5":"contracts/IERC20Metadata.sol","6":"contracts/ReentrancyGuard.sol","7":"contracts/curve.sol"},"sourceDir":".post_autofinders.2"}}}}
		AnnotationCmd JSON{"key":{"name":"internal.func.start","type":"analysis.ip.InternalFuncStartAnnotation","erasureStrategy":"CallTrace"},"value":{"id":6,"startPc":2909,"args":[],"methodSignature":{"#class":"spec.cvlast.QualifiedMethodSignature.QualifiedMethodSig","qualifiedMethodName":{"#class":"spec.cvlast.QualifiedFunction","host":{"name":"curve"},"methodId":"getVirtualPrice"},"params":[],"res":[{"#class":"spec.cvlast.VMParam.Unnamed","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256}}]},"stackOffsetToArgPos":{},"callSiteSrc":{"source":7,"begin":1311,"len":17,"jumpType":"ENTER","address":"ce4604a0000000000000000000000028","sourceContext":{"indexToFilepath":{"0":"contracts/Context.sol","1":"contracts/CurveToken.sol","2":"contracts/CurveTokenExample.sol","3":"contracts/ERC20.sol","4":"contracts/IERC20.sol","5":"contracts/IERC20Metadata.sol","6":"contracts/ReentrancyGuard.sol","7":"contracts/curve.sol"},"sourceDir":".post_autofinders.2"}}}}
		AnnotationCmd JSON{"key":{"name":"pta.end-allocation","type":"analysis.alloc.AllocationAnalysis$AbstractLocation","erasureStrategy":"Erased"},"value":{"prevFPWriteIdx":0,"nextFPWriteCmd":{"block":{"#class":"tac.BlockIdentifier","origStartPc":16,"stkTop":1024,"decompCopy":0,"calleeIdx":0,"topOfStackValue":2,"freshCopy":0},"pos":34},"sort":{"#class":"analysis.alloc.AllocationAnalysis.Alloc.ConstBlock","sz":"40"}}}
		AssignExpCmd:163 R525:147 Select(CANON77!!28:40 Apply(skey_basic:bif 0x8) )
		AnnotationCmd JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet","value":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R525","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1010}]},"displayPath":{"#class":"analysis.storage.DisplayPath.ArrayAccess","index":{"#class":"vc.data.TACSymbol.Const","value":"0"},"base":{"#class":"analysis.storage.DisplayPath.Root","name":"admin_balances"}},"storageType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256},"contractInstance":"ce4604a0000000000000000000000028","linkableStorageReadId":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet.None"}}}
		AssignExpCmd:164 R526:69 Select(tacBalance!!513:16 Apply(to_skey:bif R34:63) )
		NopCmd
		AssumeExpCmd LNot(Lt(R526:69 R525:147 ) )
		AssignExpCmd:165 R528:166 Sub(R526:69 R525:147 )
		AssignExpCmd:167 tacMCANON5!!529:14 Store(tacMCANON5!!18:14 0xc0 R528:166 )
		AssignExpCmd:168 R530:67 Select(CANON77!!28:40 Apply(skey_basic:bif 0x9) )
		AnnotationCmd JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet","value":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R530","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1011}]},"displayPath":{"#class":"analysis.storage.DisplayPath.ArrayAccess","index":{"#class":"vc.data.TACSymbol.Const","value":"1"},"base":{"#class":"analysis.storage.DisplayPath.Root","name":"admin_balances"}},"storageType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256},"contractInstance":"ce4604a0000000000000000000000028","linkableStorageReadId":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet.None"}}}
		AssignExpCmd B532:54 Le(CANON18!!24:169 0xffffffffffffffffffffffffffffffffffffffff )
		AssignExpCmd B533:54 Ge(CANON18!!24:169 0x0 )
		NopCmd
		AssumeExpCmd LAnd(B532:54 B533:54 )
		AnnotationCmd JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet","value":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"CANON18!!24","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.scalarization.sort","type":"vc.data.ScalarizationSort","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.ScalarizationSort.Packed","packedStart":{"#class":"vc.data.ScalarizationSort.Split","idx":"b"},"start":0}},{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.storage.bit-width","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":160},{"key":{"name":"tac.storage.pretty.paths","type":"analysis.storage.DisplayPaths","erasureStrategy":"Erased"},"value":{"paths":[{"#class":"analysis.storage.DisplayPath.Root","name":"coins_1"}]}},{"key":{"name":"tac.slot.type","type":"spec.cvlast.typedescriptors.EVMTypeDescriptor$EVMValueType","erasureStrategy":"Canonical"},"value":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.address"}},{"key":{"name":"tac.storage.non-indexed-path","type":"analysis.storage.StorageAnalysisResult$NonIndexedPath","erasureStrategy":"Canonical"},"value":{"#class":"analysis.storage.StorageAnalysisResult.NonIndexedPath.Root","slot":"b"}},{"key":{"name":"tac.storage","type":"java.math.BigInteger","erasureStrategy":"Canonical"},"value":"ce4604a0000000000000000000000028"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1009}]},"displayPath":{"#class":"analysis.storage.DisplayPath.Root","name":"coins_1"},"storageType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.address"},"contractInstance":"ce4604a0000000000000000000000028","linkableStorageReadId":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet.Id","id":5}}}
		AnnotationCmd JSON{"key":{"name":"init.reorder.fence","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		AssignExpCmd:170 tacMCANON6!!536:15 Store(tacMCANON6!!19:15 0x100 0x70a0823100000000000000000000000000000000000000000000000000000000 )
		AssignExpCmd:171 tacMCANON6!!538:15 Store(tacMCANON6!!536:15 0x104 R34:63 )
		AssignExpCmd:170 R539:135 0x100
		AssignHavocCmd:170 R540:172
		AssignHavocCmd tacReturndata!!541:78
		JumpCmd 0_0_0_6_0_0
	}
	Block 8_0_0_0_0_0 Succ [0_0_0_9_0_0] {
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
	Block 0_0_0_6_0_0 Succ [5_0_0_5_0_0] {
		AnnotationCmd JSON{"key":{"name":"call.trace.push","type":"analysis.icfg.Inliner$CallStack$PushRecord","erasureStrategy":"Canonical"},"value":"rO0ABXNyACphbmFseXNpcy5pY2ZnLklubGluZXIkQ2FsbFN0YWNrJFB1c2hSZWNvcmSX8+DCTLCH+AIAA0kACGNhbGxlZUlkTAAGY2FsbGVldAATTHZjL2RhdGEvTWV0aG9kUmVmO0wAB3N1bW1hcnl0ABVMdmMvZGF0YS9DYWxsU3VtbWFyeTt4cAAAAAZzcgARdmMuZGF0YS5NZXRob2RSZWbJlJTzzU9pGAIAA0wABGF0dHJ0ABdMc2NlbmUvTWV0aG9kQXR0cmlidXRlO0wACmNvbnRyYWN0SWR0ABZMamF2YS9tYXRoL0JpZ0ludGVnZXI7TAAHc2lnSGFzaHQAEExldm0vU2lnaGFzaEludDt4cHNyABxzY2VuZS5NZXRob2RBdHRyaWJ1dGUkQ29tbW9uNHjdebdr9XMCAAB4cgAVc2NlbmUuTWV0aG9kQXR0cmlidXRlcYg2pYWutuUCAAB4cHNyABRqYXZhLm1hdGguQmlnSW50ZWdlcoz8nx+pO/sdAwAGSQAIYml0Q291bnRJAAliaXRMZW5ndGhJABNmaXJzdE5vbnplcm9CeXRlTnVtSQAMbG93ZXN0U2V0Qml0SQAGc2lnbnVtWwAJbWFnbml0dWRldAACW0J4cgAQamF2YS5sYW5nLk51bWJlcoaslR0LlOCLAgAAeHD///////////////7////+AAAAAXVyAAJbQqzzF/gGCFTgAgAAeHAAAAAQzkYEoAAAAAAAAAAAAAAAEXhzcgAOZXZtLlNpZ2hhc2hJbnRUdcqNMXEgeAIAAUwAAW5xAH4ABnhwc3EAfgAM///////////////+/////gAAAAF1cQB+ABAAAAAEcKCCMXhzcgATdmMuZGF0YS5DYWxsU3VtbWFyeZQcmw5vl+FdAgAQSQAJc3VtbWFyeUlkTAAOY2FsbENvbnZlbnRpb250ACZMaW5zdHJ1bWVudGF0aW9uL2NhbGxzL0NhbGxDb252ZW50aW9uO0wACmNhbGxUYXJnZXR0ABpMYW5hbHlzaXMvaWNmZy9DYWxsVGFyZ2V0O0wACGNhbGxUeXBldAAVTHZjL2RhdGEvVEFDQ2FsbFR5cGU7TAAPY2Fubm90QmVJbmxpbmVkdAAtTGFuYWx5c2lzL2ljZmcvSW5saW5lciRJbGxlZ2FsSW5saW5pbmdSZWFzb247TAAGZ2FzVmFydAATTHZjL2RhdGEvVEFDU3ltYm9sO0wABmluQmFzZXEAfgAbTAAIaW5PZmZzZXRxAH4AG0wABmluU2l6ZXEAfgAbTAAMb3JpZ0NhbGxjb3JldAAgTHZjL2RhdGEvVEFDQ21kJFNpbXBsZSRDYWxsQ29yZTtMAAdvdXRCYXNlcQB+ABtMAAlvdXRPZmZzZXRxAH4AG0wAB291dFNpemVxAH4AG0wADXNpZ1Jlc29sdXRpb250AA9MamF2YS91dGlsL1NldDtMAAV0b1ZhcnEAfgAbTAAIdmFsdWVWYXJxAH4AG3hwAAAAA3NyACRpbnN0cnVtZW50YXRpb24uY2FsbHMuQ2FsbENvbnZlbnRpb25HtO1ulL788QIAA0kACGNhbGxlcklkTAAFaW5wdXR0ABlMYW5hbHlzaXMvaWNmZy9DYWxsSW5wdXQ7TAAGcmF3T3V0dAAiTGluc3RydW1lbnRhdGlvbi9jYWxscy9DYWxsT3V0cHV0O3hwAAAAAHNyABdhbmFseXNpcy5pY2ZnLkNhbGxJbnB1dJjJD1MhNUxQAgAHTAAHYmFzZVZhcnQAGUx2Yy9kYXRhL1RBQ0V4cHIkU3ltJFZhcjtMABBlbmNvZGVkQXJndW1lbnRzdAAjTGFuYWx5c2lzL2ljZmcvQUJJQXJndW1lbnRFbmNvZGluZztMABNpbnB1dFNpemVMb3dlckJvdW5kcQB+AAZMAAZvZmZzZXR0ABVMdmMvZGF0YS9UQUNFeHByJFN5bTtMABRyYW5nZVRvRGVjb21wb3NlZEFyZ3QAD0xqYXZhL3V0aWwvTWFwO0wAEHNpbXBsaWZpZWRPZmZzZXR0ABtMdmMvZGF0YS9UQUNFeHByJFN5bSRDb25zdDtMAARzaXplcQB+ACZ4cHNyABd2Yy5kYXRhLlRBQ0V4cHIkU3ltJFZhcskrg43eGgPnAgACTAABc3QAF0x2Yy9kYXRhL1RBQ1N5bWJvbCRWYXI7TAADdGFndAAJTHRhYy9UYWc7eHIAE3ZjLmRhdGEuVEFDRXhwciRTeW2iVj0S4YSNUAIAAHhyAA92Yy5kYXRhLlRBQ0V4cHJYhGlUu/v+yAIAAHhwc3IANnZjLmRhdGEuVEFDU3ltYm9sJFZhciRXaXRoRGVmYXVsdENhbGxJbmRleCRXaXRoQnl0ZU1hcJ7+oHF4CHAAAgACTAAEbWV0YXQALUxrb3RsaW54L2NvbGxlY3Rpb25zL2ltbXV0YWJsZS9QZXJzaXN0ZW50TWFwO0wACm5hbWVQcmVmaXh0ABJMamF2YS9sYW5nL1N0cmluZzt4cgAVdmMuZGF0YS5UQUNTeW1ib2wkVmFyCYrCGVl9SXYCAAB4cgARdmMuZGF0YS5UQUNTeW1ib2zd3Run/CoWswIAAHhwc3IAJmRhdGFzdHJ1Y3R1cmVzLnRyZWFwLkhhc2hUcmVhcE1hcCROb2Rlf2t9acJIPnQCAANMAANrZXl0ABJMamF2YS9sYW5nL09iamVjdDtMAARuZXh0dAA1TGRhdGFzdHJ1Y3R1cmVzL3RyZWFwL0hhc2hUcmVhcE1hcCRNb3JlS2V5VmFsdWVQYWlycztMAAV2YWx1ZXEAfgA3eHIAIWRhdGFzdHJ1Y3R1cmVzLnRyZWFwLkhhc2hUcmVhcE1hcPMJ/2vt3boKAgAAeHIAHWRhdGFzdHJ1Y3R1cmVzLnRyZWFwLlRyZWFwTWFw46LAyn3v5moCAAB4cgAaZGF0YXN0cnVjdHVyZXMudHJlYXAuVHJlYXA88f21zZwbdQIAAkwABGxlZnR0ABxMZGF0YXN0cnVjdHVyZXMvdHJlYXAvVHJlYXA7TAAFcmlnaHRxAH4APHhwcHNxAH4ANnBzcQB+ADZwcHNyAAt0YWMuTWV0YUtleVF/W3MiCfIZAgADTAAPZXJhc3VyZVN0cmF0ZWd5dAAdTHRhYy9NZXRhS2V5JEVyYXN1cmVTdHJhdGVneTtMAARuYW1lcQB+ADJMAAN0eXB0ABFMamF2YS9sYW5nL0NsYXNzO3hwfnIAG3RhYy5NZXRhS2V5JEVyYXN1cmVTdHJhdGVneQAAAAAAAAAAEgAAeHIADmphdmEubGFuZy5FbnVtAAAAAAAAAAASAAB4cHQACUNhbm9uaWNhbHQAF3RhYy5tZW1vcnkucGFydGl0aW9uLWlkdnIAEWphdmEubGFuZy5JbnRlZ2VyEuKgpPeBhzgCAAFJAAV2YWx1ZXhxAH4ADnBzcQB+AEkAAAAGc3EAfgBAcQB+AEZ0ABJUYWMuc3ltYm9sLmtleXdvcmR2cgAQamF2YS5sYW5nLlN0cmluZ6DwpDh6O7NCAgAAeHBwdAAEdGFjTXNxAH4AQHEAfgBGdAANdGFjLmlzLm1lbW9yeXZyACJ0YWMuTWV0YU1hcCRDb21wYW5pb24kTm90aGluZ1ZhbHVl8nsHH85ykpUCAAB4cHBzcQB+AFN0AA90YWNNQ0FOT042ISE1MzhzcgAPdGFjLlRhZyRCeXRlTWFwNb/Ry6GDRgkCAAB4cgALdGFjLlRhZyRNYXABJytzDV3P/QIAAHhyAAd0YWMuVGFnLk9V3gn2xngCAAB4cHBzcQB+AAz///////////////7////+AAAAAXVxAH4AEAAAAAEkeHNxAH4AKnNyADV2Yy5kYXRhLlRBQ1N5bWJvbCRWYXIkV2l0aERlZmF1bHRDYWxsSW5kZXgkV2l0aEJpdDI1NnqsyEgq0drPAgACTAAEbWV0YXEAfgAxTAAKbmFtZVByZWZpeHEAfgAyeHEAfgAzc3EAfgA2c3EAfgA2cHBxAH4ATHB0AAFMcHNxAH4AQHEAfgBGdAAQdGFjLnN0YWNrLmhlaWdodHEAfgBKcHNxAH4ASQAAA+50AARSNTM5c3IADnRhYy5UYWckQml0MjU2IyLQT+LlKkgCAAB4cQB+AFlzcgARamF2YS51dGlsLkhhc2hNYXAFB9rBwxZg0QMAAkYACmxvYWRGYWN0b3JJAAl0aHJlc2hvbGR4cD9AAAAAAAADdwgAAAAEAAAAAnNyAB5hbmFseXNpcy5pY2ZnLlNjcmF0Y2hCeXRlUmFuZ2XBTLaPpUzj2gIAAkwABGZyb21xAH4ABkwAAnRvcQB+AAZ4cHNxAH4ADP///////////////v////4AAAAAdXEAfgAQAAAAAHhzcQB+AAz///////////////7////+AAAAAXVxAH4AEAAAAAEDeHNyAC1hbmFseXNpcy5pY2ZnLkRlY29tcG9zZWRDYWxsSW5wdXRBcmckQ29uc3RhbnSFavLdQafqPQIAA0wAAWN0ABlMdmMvZGF0YS9UQUNTeW1ib2wkQ29uc3Q7TAARY29udHJhY3RSZWZlcmVuY2V0AC9MYW5hbHlzaXMvaWNmZy9DYWxsR3JhcGhCdWlsZGVyJENhbGxlZENvbnRyYWN0O0wADHNjcmF0Y2hSYW5nZXQAIExhbmFseXNpcy9pY2ZnL1NjcmF0Y2hCeXRlUmFuZ2U7eHIAJGFuYWx5c2lzLmljZmcuRGVjb21wb3NlZENhbGxJbnB1dEFy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cGV0ABNMY29tcGlsZXIvSnVtcFR5cGU7TAANc291cmNlQ29udGV4dHQAGExjb21waWxlci9Tb3VyY2VDb250ZXh0O3hwcHNxAH4A5QAAFx8AAAAnAAAAB3EAfgCGfnIAEWNvbXBpbGVyLkp1bXBUeXBlAAAAAAAAAAASAAB4cQB+AEV0AAdSRUdVTEFSc3IAFmNvbXBpbGVyLlNvdXJjZUNvbnRleHSMy1vpQFzaEwIAAkwAD2luZGV4VG9GaWxlcGF0aHEAfgAnTAAJc291cmNlRGlycQB+ADJ4cHNxAH4AaT9AAAAAAAAMdwgAAAAQAAAACHNxAH4ASQAAAAB0ABVjb250cmFjdHMvQ29udGV4dC5zb2xzcQB+AEkAAAABdAAYY29udHJhY3RzL0N1cnZlVG9rZW4uc29sc3EAfgBJAAAAAnQAH2NvbnRyYWN0cy9DdXJ2ZVRva2VuRXhhbXBsZS5zb2xzcQB+AEkAAAADdAATY29udHJhY3RzL0VSQzIwLnNvbHNxAH4ASQAAAAR0ABRjb250cmFjdHMvSUVSQzIwLnNvbHNxAH4ASQAAAAV0ABxjb250cmFjdHMvSUVSQzIwTWV0YWRhdGEuc29scQB+AEt0AB1jb250cmFjdHMvUmVlbnRyYW5jeUd1YXJkLnNvbHNxAH4ASQAAAAd0ABNjb250cmFjdHMvY3VydmUuc29seHQAEy5wb3N0X2F1dG9maW5kZXJzLjJzcQB+ADBzcQB+ADZwc3EAfgA2cHNxAH4ANnBwcQB+AENwcQB+AEtxAH4ATHBxAH4AUHEAfgBRcHEAfgBVcQB+AFZzcQB+AF5zcQB+ADZzcQB+ADZwcHEAfgBMcHEAfgBicHEAfgBjcHEAfgCzcQB+AGZxAH4AtnNxAH4AXnNxAH4ANnNxAH4ANnNxAH4ANnNxAH4ANnBzcQB+ADZwcHEAfgBMcHEAfgBic3EAfgBAcQB+AEZ0ABZ0YWMuc2NhbGFyaXphdGlvbi5zb3J0dnIAGXZjLmRhdGEuU2NhbGFyaXphdGlvblNvcnQwznCd5GgNJgIAAHhwcHNyACB2Yy5kYXRhLlNjYWxhcml6YXRpb25Tb3J0JFBhY2tlZC5FrRKTiOT3AgACSQAFc3RhcnRMAAtwYWNrZWRTdGFydHQAG0x2Yy9kYXRhL1NjYWxhcml6YXRpb25Tb3J0O3hxAH4BDwAAAABzcgAfdmMuZGF0YS5TY2FsYXJpemF0aW9uU29ydCRTcGxpdFT/Wafxx7IFAgABTAADaWR4cQB+AAZ4cQB+AQ9zcQB+AAz///////////////7////+AAAAAXVxAH4AEAAAAAELeHNxAH4ANnBzcQB+ADZwc3EAfgA2cHBzcQB+AEBxAH4ARnQAHHRhYy5zdG9yYWdlLm5vbi1pbmRleGVkLXBhdGh2cgA1YW5hbHlzaXMuc3RvcmFnZS5TdG9yYWdlQW5hbHlzaXNSZXN1bHQkTm9uSW5kZXhlZFBhdGgIwaBLofo/RQIAAHhwcHNyADphbmFseXNpcy5zdG9yYWdlLlN0b3JhZ2VBbmFseXNpc1Jlc3VsdCROb25JbmRleGVkUGF0aCRSb290vzf12KXqCv8CAAFMAARzbG90cQB+AAZ4cQB+AR1xAH4BFnNxAH4AQHEAfgBGdAANdGFjLnNsb3QudHlwZXZyADpzcGVjLmN2bGFzdC50eXBlZGVzY3JpcHRvcnMuRVZNVHlwZURlc2NyaXB0b3IkRVZNVmFsdWVUeXBlxomvArrquCUCAAB4cgAtc3BlYy5jdmxhc3QudHlwZWRlc2NyaXB0b3JzLkVWTVR5cGVEZXNjcmlwdG9yyFGp8TzCah0CAAB4cHBzcgA1c3BlYy5jdmxhc3QudHlwZWRlc2NyaXB0b3JzLkVWTVR5cGVEZXNjcmlwdG9yJGFkZHJlc3N6+GX0b5egKQIAAHhyAERzcGVjLmN2bGFzdC50eXBlZGVzY3JpcHRvcnMuRVZNVHlwZURlc2NyaXB0b3IkRVZNSXNvbW9ycGhpY1ZhbHVlVHlwZfd1mJFuEKEPAgAAeHEAfgEjc3EAfgBAcQB+AJB0ABh0YWMuc3RvcmFnZS5wcmV0dHkucGF0aHN2cgAdYW5hbHlzaXMuc3RvcmFnZS5EaXNwbGF5UGF0aHP3REu3w/VRFgIAAUwABXBhdGhzcQB+AB14cHBzcQB+AStzcgAXamF2YS51dGlsLkxpbmtlZEhhc2hTZXTYbNdald0qHgIAAHhyABFqYXZhLnV0aWwuSGFzaFNldLpEhZWWuLc0AwAAeHB3DAAAABA/QAAAAAAAAXNyACFhbmFseXNpcy5zdG9yYWdlLkRpc3BsYXlQYXRoJFJvb3TTc6C9mdA8cgIAAkwABGJhc2V0AB5MYW5hbHlzaXMvc3RvcmFnZS9EaXNwbGF5UGF0aDtMAARuYW1lcQB+ADJ4cgAcYW5hbHlzaXMuc3RvcmFnZS5EaXNwbGF5UGF0aE9AY+pW0iAFAgAAeHBwdAAHY29pbnNfMXhzcQB+AEBxAH4ARnQAFXRhYy5zdG9yYWdlLmJpdC13aWR0aHEAfgBKcHNxAH4ASQAAAKBwc3EAfgBAcQB+AEZ0AAt0YWMuc3RvcmFnZXEAfgCZcHEAfgCGcHEAfgBjcHNxAH4ASQAAA/J0AAtDQU5PTjE4ISEyNHNxAH4Ad3EAfgBocQB+AG1zcQB+ADBzcQB+ADZwc3EAfgA2cHNxAH4ANnBwcQB+AENwcQB+AEtxAH4ATHBxAH4AUHEAfgBRcHEAfgBVcQB+AFZzcQB+AF5zcQB+ADZzcQB+ADZwcHEAfgBMcHEAfgBicHEAfgBjcHEAfgCzcQB+AGZxAH4AtnNyACJqYXZhLnV0aWwuQ29sbGVjdGlvbnMkU2luZ2xldG9uU2V0LFJBmCnAsb8CAAFMAAdlbGVtZW50cQB+ADd4cHEAfgAUc3EAfgBec3EAfgA2c3EAfgA2c3EAfgA2c3EAfgA2cHNxAH4ANnBwcQB+AExwcQB+AGJxAH4BDXBxAH4BE3NxAH4ANnBzcQB+ADZwc3EAfgA2cHBxAH4BG3BxAH4BIHEAfgEhcHEAfgEocQB+ASlwc3EAfgErc3EAfgEudwwAAAAQP0AAAAAAAAFxAH4BNHhxAH4BNnBxAH4BOHBxAH4BOXBxAH4AhnBxAH4AY3BxAH4BO3EAfgE8c3EAfgB3cQB+AGhxAH4AbQ=="}
		AnnotationCmd JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageGlobalChangeSnippet.StorageBackupPoint","calleeTxId":6}}
		NopCmd
		AssumeExpCmd LAnd(Eq(tacCalldatasize!!3:3 0x24 ) Eq(tacCalldatasize!!3:3 0x24 ) )
		NopCmd
		AssumeExpCmd Eq(tacCalldatabufCANON0@6:1 0x70a0823100000000000000000000000000000000000000000000000000000000 )
		AssignExpCmd tacCalldatabufCANON1@6:173 R34:174
		LabelCmd "Start procedure ERC20-balanceOf(address)"
		AnnotationCmd JSON{"key":{"name":"fps.free-pointer-is-scalarized","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true}
		AssignExpCmd R551:54 Select(tacExtcodesize!!9:4 Apply(to_skey:bif R33:81) )
		NopCmd
		AssumeExpCmd Gt(R551:54 0x0 )
		AnnotationCmd JSON{"key":{"name":"internal.func.finder.info","type":"analysis.ip.InternalFunctionFinderReport","erasureStrategy":"Erased"},"value":"rO0ABXNyAChhbmFseXNpcy5pcC5JbnRlcm5hbEZ1bmN0aW9uRmluZGVyUmVwb3J0ian+bYn1VdACAAFMABN1bnJlc29sdmVkRnVuY3Rpb25zdAAPTGphdmEvdXRpbC9TZXQ7eHBzcgAhZGF0YXN0cnVjdHVyZXMuTGlua2VkQXJyYXlIYXNoU2V0AAAAAAAAAAEDAAJGAApsb2FkRmFjdG9yTAAJaGFzaFRhYmxldAAuTGRhdGFzdHJ1Y3R1cmVzL2FycmF5aGFzaHRhYmxlL0FycmF5SGFzaFRhYmxlO3hwdwgAAAAAQAAAAHg="}
		AnnotationCmd JSON{"key":{"name":"fps.free-pointer-is-scalarized","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true}
		NopCmd
		AssumeExpCmd LNot(Lt(tacCalldatasize!!3:3 0x4 ) )
		NopCmd
		AssumeExpCmd LNot(Gt(0x39509351 tacSighash!!40:47 ) )
		NopCmd
		AssumeExpCmd LNot(Eq(0x39509351 tacSighash!!40:47 ) )
		NopCmd
		AssumeExpCmd Eq(0x70a08231 tacSighash!!40:47 )
		AssignExpCmd:175 R557:83 Sub(tacCalldatasize!!3:3 0x4 )
		AssignExpCmd B558:84 Slt(R557:83 0x20 )
		NopCmd
		AssumeExpCmd LNot(B558:84 )
		AssignExpCmd:176 R560:72 tacCalldatabufCANON1@6:177
		NopCmd
		AssumeExpCmd Eq(R34:174 R34:174 )
		AnnotationCmd JSON{"key":{"name":"internal.func.start","type":"analysis.ip.InternalFuncStartAnnotation","erasureStrategy":"CallTrace"},"value":{"id":7,"startPc":1712,"args":[{"s":{"namePrefix":"R560","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1013}]},"offset":1,"sort":"SCALAR"}],"methodSignature":{"#class":"spec.cvlast.QualifiedMethodSignature.QualifiedMethodSig","qualifiedMethodName":{"#class":"spec.cvlast.QualifiedFunction","host":{"name":"ERC20"},"methodId":"balanceOf"},"params":[{"#class":"spec.cvlast.VMParam.Named","name":"account","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$address"}}],"res":[{"#class":"spec.cvlast.VMParam.Unnamed","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256}}]},"stackOffsetToArgPos":{"1":0},"callSiteSrc":{"source":1,"begin":4376,"len":467,"jumpType":"ENTER","address":"ce4604a0000000000000000000000011","sourceContext":{"indexToFilepath":{"0":"contracts/Context.sol","1":"contracts/ERC20.sol","2":"contracts/IERC20.sol","3":"contracts/IERC20Metadata.sol"},"sourceDir":".post_autofinders.1"}}}}
		AssignExpCmd:178 R565:88 Apply(hash_3_keccak:bif Apply(skey_basic:bif 0x40) Apply(to_skey:bif R34:174) Apply(skey_basic:bif 0x0))
		AssignExpCmd:179 R566:88 Select(CANON93!!30:42 R565:180 )
		AnnotationCmd JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet","value":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R566","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1020}]},"displayPath":{"#class":"analysis.storage.DisplayPath.MapAccess","key":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R560","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1018}]},"keyTyp":{"#class":"tac.TACStorageType.IntegralType","typeLabel":"address","numBytes":"14","descriptor":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$address"},"lowerBound":null,"upperBound":null},"base":{"#class":"analysis.storage.DisplayPath.Root","name":"_balances"}},"storageType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256},"contractInstance":"ce4604a0000000000000000000000011","linkableStorageReadId":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet.None"}}}
		AnnotationCmd JSON{"key":{"name":"internal.func.end","type":"analysis.ip.InternalFuncExitAnnotation","erasureStrategy":"Canonical"},"value":{"id":7,"rets":[{"s":{"namePrefix":"R566","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1023}]},"offset":0}],"functionLayout":{"0":{"#class":"analysis.ip.InternalFuncValueLocation.Scalar"}}}}
		AnnotationCmd JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.EVMFunctionReturnWrite","returnbufOffset":"0","returnValueSym":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R566","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1023}]},"callIndex":6}}
		AnnotationCmd JSON{"key":{"name":"tac.return.path","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		LabelCmd "End procedure ERC20-balanceOf(address)"
		AssignExpCmd tacReturndata!!568:78 Store(tacReturndata!!541:78 0x0 R566:88 )
		AssignExpCmd tacMCANON6!!569:15 Store(tacMCANON6!!538:15 0x100 R566:88 )
		AnnotationCmd JSON{"key":{"name":"call.trace.pop","type":"analysis.icfg.Inliner$CallStack$PopRecord","erasureStrategy":"Canonical"},"value":"rO0ABXNyAClhbmFseXNpcy5pY2ZnLklubGluZXIkQ2FsbFN0YWNrJFBvcFJlY29yZPAPfwSLdCWJAgABSQAIY2FsbGVlSWR4cAAAAAY="}
		JumpCmd 5_0_0_5_0_0
	}
	Block 0_0_0_7_0_0 Succ [6_0_0_5_0_0] {
		AnnotationCmd JSON{"key":{"name":"call.trace.push","type":"analysis.icfg.Inliner$CallStack$PushRecord","erasureStrategy":"Canonical"},"value":"rO0ABXNyACphbmFseXNpcy5pY2ZnLklubGluZXIkQ2FsbFN0YWNrJFB1c2hSZWNvcmSX8+DCTLCH+AIAA0kACGNhbGxlZUlkTAAGY2FsbGVldAATTHZjL2RhdGEvTWV0aG9kUmVmO0wAB3N1bW1hcnl0ABVMdmMvZGF0YS9DYWxsU3VtbWFyeTt4cAAAAAdzcgARdmMuZGF0YS5NZXRob2RSZWbJlJTzzU9pGAIAA0wABGF0dHJ0ABdMc2NlbmUvTWV0aG9kQXR0cmlidXRlO0wACmNvbnRyYWN0SWR0ABZMamF2YS9tYXRoL0JpZ0ludGVnZXI7TAAHc2lnSGFzaHQAEExldm0vU2lnaGFzaEludDt4cHNyABxzY2VuZS5NZXRob2RBdHRyaWJ1dGUkQ29tbW9uNHjdebdr9XMCAAB4cgAVc2NlbmUuTWV0aG9kQXR0cmlidXRlcYg2pYWutuUCAAB4cHNyABRqYXZhLm1hdGguQmlnSW50ZWdlcoz8nx+pO/sdAwAGSQAIYml0Q291bnRJAAliaXRMZW5ndGhJABNmaXJzdE5vbnplcm9CeXRlTnVtSQAMbG93ZXN0U2V0Qml0SQAGc2lnbnVtWwAJbWFnbml0dWRldAACW0J4cgAQamF2YS5sYW5nLk51bWJlcoaslR0LlOCLAgAAeHD///////////////7////+AAAAAXVyAAJbQqzzF/gGCFTgAgAAeHAAAAAQzkYEoAAAAAAAAAAAAAAAKHhzcgAOZXZtLlNpZ2hhc2hJbnRUdcqNMXEgeAIAAUwAAW5xAH4ABnhwc3EAfgAM///////////////+/////gAAAAF1cQB+ABAAAAAEOEL3dnhzcgATdmMuZGF0YS5DYWxsU3VtbWFyeZQcmw5vl+FdAgAQSQAJc3VtbWFyeUlkTAAOY2FsbENvbnZlbnRpb250ACZMaW5zdHJ1bWVudGF0aW9uL2NhbGxzL0NhbGxDb252ZW50aW9uO0wACmNhbGxUYXJnZXR0ABpMYW5hbHlzaXMvaWNmZy9DYWxsVGFyZ2V0O0wACGNhbGxUeXBldAAVTHZjL2RhdGEvVEFDQ2FsbFR5cGU7TAAPY2Fubm90QmVJbmxpbmVkdAAtTGFuYWx5c2lzL2ljZmcvSW5saW5lciRJbGxlZ2FsSW5saW5pbmdSZWFzb247TAAGZ2FzVmFydAATTHZjL2RhdGEvVEFDU3ltYm9sO0wABmluQmFzZXEAfgAbTAAIaW5PZmZzZXRxAH4AG0wABmluU2l6ZXEAfgAbTAAMb3JpZ0NhbGxjb3JldAAgTHZjL2RhdGEvVEFDQ21kJFNpbXBsZSRDYWxsQ29yZTtMAAdvdXRCYXNlcQB+ABtMAAlvdXRPZmZzZXRxAH4AG0wAB291dFNpemVxAH4AG0wADXNpZ1Jlc29sdXRpb250AA9MamF2YS91dGlsL1NldDtMAAV0b1ZhcnEAfgAbTAAIdmFsdWVWYXJxAH4AG3hwAAAABHNyACRpbnN0cnVtZW50YXRpb24uY2FsbHMuQ2FsbENvbnZlbnRpb25HtO1ulL788QIAA0kACGNhbGxlcklkTAAFaW5wdXR0ABlMYW5hbHlzaXMvaWNmZy9DYWxsSW5wdXQ7TAAGcmF3T3V0dAAiTGluc3RydW1lbnRhdGlvbi9jYWxscy9DYWxsT3V0cHV0O3hwAAAAAHNyABdhbmFseXNpcy5pY2ZnLkNhbGxJbnB1dJjJD1MhNUxQAgAHTAAHYmFzZVZhcnQAGUx2Yy9kYXRhL1RBQ0V4cHIkU3ltJFZhcjtMABBlbmNvZGVkQXJndW1lbnRzdAAjTGFuYWx5c2lzL2ljZmcvQUJJQXJndW1lbnRFbmNvZGluZztMABNpbnB1dFNpemVMb3dlckJvdW5kcQB+AAZMAAZvZmZzZXR0ABVMdmMvZGF0YS9UQUNFeHByJFN5bTtMABRyYW5nZVRvRGVjb21wb3NlZEFyZ3QAD0xqYXZhL3V0aWwvTWFwO0wAEHNpbXBsaWZpZWRPZmZzZXR0ABtMdmMvZGF0YS9UQUNFeHByJFN5bSRDb25zdDtMAARzaXplcQB+ACZ4cHNyABd2Yy5kYXRhLlRBQ0V4cHIkU3ltJFZhcskrg43eGgPnAgACTAABc3QAF0x2Yy9kYXRhL1RBQ1N5bWJvbCRWYXI7TAADdGFndAAJTHRhYy9UYWc7eHIAE3ZjLmRhdGEuVEFDRXhwciRTeW2iVj0S4YSNUAIAAHhyAA92Yy5kYXRhLlRBQ0V4cHJYhGlUu/v+yAIAAHhwc3IANnZjLmRhdGEuVEFDU3ltYm9sJFZhciRXaXRoRGVmYXVsdENhbGxJbmRleCRXaXRoQnl0ZU1hcJ7+oHF4CHAAAgACTAAEbWV0YXQALUxrb3RsaW54L2NvbGxlY3Rpb25zL2ltbXV0YWJsZS9QZXJzaXN0ZW50TWFwO0wACm5hbWVQcmVmaXh0ABJMamF2YS9sYW5nL1N0cmluZzt4cgAVdmMuZGF0YS5UQUNTeW1ib2wkVmFyCYrCGVl9SXYCAAB4cgARdmMuZGF0YS5UQUNTeW1ib2zd3Run/CoWswIAAHhwc3IAJmRhdGFzdHJ1Y3R1cmVzLnRyZWFwLkhhc2hUcmVhcE1hcCROb2Rlf2t9acJIPnQCAANMAANrZXl0ABJMamF2YS9sYW5nL09iamVjdDtMAARuZXh0dAA1TGRhdGFzdHJ1Y3R1cmVzL3RyZWFwL0hhc2hUcmVhcE1hcCRNb3JlS2V5VmFsdWVQYWlycztMAAV2YWx1ZXEAfgA3eHIAIWRhdGFzdHJ1Y3R1cmVzLnRyZWFwLkhhc2hUcmVhcE1hcPMJ/2vt3boKAgAAeHIAHWRhdGFzdHJ1Y3R1cmVzLnRyZWFwLlRyZWFwTWFw46LAyn3v5moCAAB4cgAaZGF0YXN0cnVjdHVyZXMudHJlYXAuVHJlYXA88f21zZwbdQIAAkwABGxlZnR0ABxMZGF0YXN0cnVjdHVyZXMvdHJlYXAvVHJlYXA7TAAFcmlnaHRxAH4APHhwcHNxAH4ANnBzcQB+ADZwcHNyAAt0YWMuTWV0YUtleVF/W3MiCfIZAgADTAAPZXJhc3VyZVN0cmF0ZWd5dAAdTHRhYy9NZXRhS2V5JEVyYXN1cmVTdHJhdGVneTtMAARuYW1lcQB+ADJMAAN0eXB0ABFMamF2YS9sYW5nL0NsYXNzO3hwfnIAG3RhYy5NZXRhS2V5JEVyYXN1cmVTdHJhdGVneQAAAAAAAAAAEgAAeHIADmphdmEubGFuZy5FbnVtAAAAAAAAAAASAAB4cHQACUNhbm9uaWNhbHQAF3RhYy5tZW1vcnkucGFydGl0aW9uLWlkdnIAEWphdmEubGFuZy5JbnRlZ2VyEuKgpPeBhzgCAAFJAAV2YWx1ZXhxAH4ADnBzcQB+AEkAAAAGc3EAfgBAcQB+AEZ0ABJUYWMuc3ltYm9sLmtleXdvcmR2cgAQamF2YS5sYW5nLlN0cmluZ6DwpDh6O7NCAgAAeHBwdAAEdGFjTXNxAH4AQHEAfgBGdAANdGFjLmlzLm1lbW9yeXZyACJ0YWMuTWV0YU1hcCRDb21wYW5pb24kTm90aGluZ1ZhbHVl8nsHH85ykpUCAAB4cHBzcQB+AFN0AA90YWNNQ0FOT042ISE2MzBzcgAPdGFjLlRhZyRCeXRlTWFwNb/Ry6GDRgkCAAB4cgALdGFjLlRhZyRNYXABJytzDV3P/QIAAHhyAAd0YWMuVGFnLk9V3gn2xngCAAB4cHBzcQB+AAz///////////////7////+AAAAAXVxAH4AEAAAAAFkeHNxAH4AKnNyADV2Yy5kYXRhLlRBQ1N5bWJvbCRWYXIkV2l0aERlZmF1bHRDYWxsSW5kZXgkV2l0aEJpdDI1NnqsyEgq0drPAgACTAAEbWV0YXEAfgAxTAAKbmFtZVByZWZpeHEAfgAyeHEAfgAzc3EAfgA2c3EAfgA2cHBxAH4ATHB0AAFMcHNxAH4AQHEAfgBGdAAQdGFjLnN0YWNrLmhlaWdodHEAfgBKcHNxAH4ASQAAA/Z0AARSNjMxc3IADnRhYy5UYWckQml0MjU2IyLQT+LlKkgCAAB4cQB+AFlzcgARamF2YS51dGlsLkhhc2hNYXAFB9rBwxZg0QMAAkYACmxvYWRGYWN0b3JJAAl0aHJlc2hvbGR4cD9AAAAAAAADdwgAAAAEAAAAAnNyAB5hbmFseXNpcy5pY2ZnLlNjcmF0Y2hCeXRlUmFuZ2XBTLaPpUzj2gIAAkwABGZyb21xAH4ABkwAAnRvcQB+AAZ4cHNxAH4ADP///////////////v////4AAAAAdXEAfgAQAAAAAHhzcQB+AAz///////////////7////+AAAAAXVxAH4AEAAAAAEDeHNyAC1hbmFseXNpcy5pY2ZnLkRlY29tcG9zZWRDYWxsSW5wdXRBcmckQ29uc3RhbnSFavLdQafqPQIAA0wAAWN0ABlMdmMvZGF0YS9UQUNTeW1ib2wkQ29uc3Q7TAARY29udHJhY3RSZWZlcmVuY2V0AC9MYW5hbHlzaXMvaWNmZy9DYWxsR3JhcGhCdWlsZGVyJENhbGxlZENvbnRyYWN0O0wADHNjcmF0Y2hSYW5nZXQAIExhbmFseXNpcy9pY2ZnL1NjcmF0Y2hCeXRlUmFuZ2U7eHIAJGFuYWx5c2lzLmljZmcuRGVjb21wb3NlZENhbGxJbnB1dEFyZ82Nwhnirh8hAgAAeHBzcgAXdmMuZGF0YS5UQUNTeW1ib2wkQ29uc3QmHp5/l8IUcAIAAkwAA3RhZ3EAfgAsTAAFdmFsdWVxAH4ABnhxAH4ANHEAfgBoc3EAfgAM///////////////+/////gAAAAF1cQB+ABAAAAAgOEL3dgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAB4cHEAfgBsc3EAfgBrc3EAfgAM///////////////+/////gAAAAF1cQB+ABAAAAABRHhzcQB+AAz///////////////7////+AAAAAXVxAH4AEAAAAAFjeHNyAC1hbmFseXNpcy5pY2ZnLkRlY29tcG9zZWRDYWxsSW5wdXRBcmckVmFyaWFibGWV3y80jneopQIAA0wAEWNvbnRyYWN0UmVmZXJlbmNlcQB+AHNMAAxzY3JhdGNoUmFuZ2VxAH4AdEwAAXZxAH4AK3hxAH4AdXNyADxhbmFseXNpcy5pY2ZnLkNhbGxHcmFwaEJ1aWxkZXIkQ2FsbGVkQ29udHJhY3QkVW5yZXNvbHZlZFJlYWRDhKJZ0RDzoAIAAUkADXN0b3JhZ2VSZWFkSWR4cgAtYW5hbHlzaXMuaWNmZy5DYWxsR3JhcGhCdWlsZGVyJENhbGxlZENvbnRyYWN00wt1rN/LodcCAAB4cAAAAAdxAH4Ae3NxAH4AXnNxAH4ANnNxAH4ANnBzcQB+ADZzcQB+ADZzcQB+ADZwc3EAfgA2cHBxAH4ATHBxAH4AYnNxAH4AQHEAfgBGdAAWdGFjLnNjYWxhcml6YXRpb24uc29ydHZyABl2Yy5kYXRhLlNjYWxhcml6YXRpb25Tb3J0MM5wneRoDSYCAAB4cHBzcgAfdmMuZGF0YS5TY2FsYXJpemF0aW9uU29ydCRTcGxpdFT/Wafxx7IFAgABTAADaWR4cQB+AAZ4cQB+AI5zcQB+AAz///////////////7////+AAAAAXVxAH4AEAAAAAEFeHNxAH4ANnBzcQB+ADZwc3EAfgA2cHBzcQB+AEBxAH4ARnQAHHRhYy5zdG9yYWdlLm5vbi1pbmRleGVkLXBhdGh2cgA1YW5hbHlzaXMuc3RvcmFnZS5TdG9yYWdlQW5hbHlzaXNSZXN1bHQkTm9uSW5kZXhlZFBhdGgIwaBLofo/RQIAAHhwcHNyADphbmFseXNpcy5zdG9yYWdlLlN0b3JhZ2VBbmFseXNpc1Jlc3VsdCROb25JbmRleGVkUGF0aCRSb290vzf12KXqCv8CAAFMAARzbG90cQB+AAZ4cQB+AJlxAH4AknNxAH4AQHEAfgBGdAANdGFjLnNsb3QudHlwZXZyADpzcGVjLmN2bGFzdC50eXBlZGVzY3JpcHRvcnMuRVZNVHlwZURlc2NyaXB0b3IkRVZNVmFsdWVUeXBlxomvArrquCUCAAB4cgAtc3BlYy5jdmxhc3QudHlwZWRlc2NyaXB0b3JzLkVWTVR5cGVEZXNjcmlwdG9yyFGp8TzCah0CAAB4cHBzcgAzc3BlYy5jdmxhc3QudHlwZWRlc2NyaXB0b3JzLkVWTVR5cGVEZXNjcmlwdG9yJFVJbnRL+xQfR/Nlf8ACAAFJAAhiaXR3aWR0aHhyAERzcGVjLmN2bGFzdC50eXBlZGVzY3JpcHRvcnMuRVZNVHlwZURlc2NyaXB0b3IkRVZNSXNvbW9ycGhpY1ZhbHVlVHlwZfd1mJFuEKEPAgAAeHEAfgCfAAABAHNxAH4AQH5xAH4ARHQABkVyYXNlZHQAGHRhYy5zdG9yYWdlLnByZXR0eS5wYXRoc3ZyAB1hbmFseXNpcy5zdG9yYWdlLkRpc3BsYXlQYXRoc/dES7fD9VEWAgABTAAFcGF0aHNxAH4AHXhwcHNxAH4AqXNyABdqYXZhLnV0aWwuTGlua2VkSGFzaFNldNhs11qV3SoeAgAAeHIAEWphdmEudXRpbC5IYXNoU2V0ukSFlZa4tzQDAAB4cHcMAAAAED9AAAAAAAABc3IAIWFuYWx5c2lzLnN0b3JhZ2UuRGlzcGxheVBhdGgkUm9vdNNzoL2Z0DxyAgACTAAEYmFzZXQAHkxhbmFseXNpcy9zdG9yYWdlL0Rpc3BsYXlQYXRoO0wABG5hbWVxAH4AMnhyABxhbmFseXNpcy5zdG9yYWdlLkRpc3BsYXlQYXRoT0Bj6lbSIAUCAAB4cHB0AAhmdXR1cmVfQXhzcQB+AEBxAH4ARnQAFXRhYy5zdG9yYWdlLmJpdC13aWR0aHEAfgBKcHNxAH4ASQAAAQBwc3EAfgBAcQB+AEZ0AAt0YWMuc3RvcmFnZXZxAH4ADHBxAH4AD3NxAH4AQHEAfgBGdAAYdGFjLmRlY29tcC1pbnNjYWxhci5zb3J0dnIAHXRhYy5EZWNvbXBvc2VkSW5wdXRTY2FsYXJTb3J0J4Yx32MwVAUCAAB4cHBzcgAkdGFjLkRlY29tcG9zZWRJbnB1dFNjYWxhclNvcnQkU2ltcGxleQdV+qgJslsCAAFMAApieXRlT2Zmc2V0cQB+AAZ4cQB+ALxxAH4AfHBxAH4AY3BzcQB+AEkAAAP3dAALQ0FOT045OSEhMzF4cHNxAH4AKnNxAH4AXnNxAH4ANnNxAH4ANnBwcQB+AExwcQB+AGJwcQB+AGNwc3EAfgBJAAAD9XQABFI2MzJxAH4AaHNyACBpbnN0cnVtZW50YXRpb24uY2FsbHMuQ2FsbE91dHB1dMLFmzfBvZx7AgADTAAEYmFzZXEAfgArTAAGb2Zmc2V0dAARTHZjL2RhdGEvVEFDRXhwcjtMAARzaXplcQB+AMl4cHNxAH4AMHNxAH4ANnBzcQB+ADZwc3EAfgA2cHBxAH4AQ3BxAH4AS3EAfgBMcHEAfgBQcQB+AFFwcQB+AFVxAH4AVnNxAH4AKnNxAH4AXnNxAH4ANnNxAH4ANnBwcQB+AExwcQB+AGJwcQB+AGNwc3EAfgBJAAAD9nEAfgBmcQB+AGhzcgAZdmMuZGF0YS5UQUNFeHByJFN5bSRDb25zdFNIr/MyQdp2AgACTAABc3EAfgByTAADdGFncQB+ACx4cQB+AC1zcQB+AHdxAH4AaHNxAH4ADP///////////////v////4AAAABdXEAfgAQAAAAASB4cQB+AGhzcgAeYW5hbHlzaXMuaWNmZy5DYWxsVGFyZ2V0JFZhbGlkuaYZ9j2rVfoCAAFMAAZjYWxsZWVxAH4Ac3hyABhhbmFseXNpcy5pY2ZnLkNhbGxUYXJnZXRG3T0sfHY+JQIAAHhwc3IARGFuYWx5c2lzLmljZmcuQ2FsbEdyYXBoQnVpbGRlciRDYWxsZWRDb250cmFjdCRGdWxseVJlc29sdmVkJFNlbGZMaW5r77yXwCrurrMCAAFMAApjb250cmFjdElkcQB+AAZ4cgA7YW5hbHlzaXMuaWNmZy5DYWxsR3JhcGhCdWlsZGVyJENhbGxlZENvbnRyYWN0JEZ1bGx5UmVzb2x2ZWSi2ciTEwCzpAIAAHhxAH4Ag3EAfgAPfnIAE3ZjLmRhdGEuVEFDQ2FsbFR5cGUAAAAAAAAAABIAAHhxAH4ARXQABlNUQVRJQ3BzcQB+AF5zcQB+ADZzcQB+ADZwcHEAfgBMcHEAfgBicHEAfgBjcHNxAH4ASQAAA/J0AARSNjMzc3EAfgAwc3EAfgA2cHNxAH4ANnBzcQB+ADZwcHEAfgBDcHEAfgBLcQB+AExwcQB+AFBxAH4AUXBxAH4AVXEAfgBWc3EAfgBec3EAfgA2c3EAfgA2cHBxAH4ATHBxAH4AYnBxAH4AY3BxAH4AZXEAfgBmc3EAfgB3cQB+AGhxAH4AW3NyAB52Yy5kYXRhLlRBQ0NtZCRTaW1wbGUkQ2FsbENvcmWhKYVHBIFmegIAC0wACGNhbGxUeXBlcQB+ABlMAANnYXNxAH4AG0wABmluQmFzZXEAfgArTAAIaW5PZmZzZXRxAH4AG0wABmluU2l6ZXEAfgAbTAAEbWV0YXEAfgAxTAAHb3V0QmFzZXEAfgArTAAJb3V0T2Zmc2V0cQB+ABtMAAdvdXRTaXplcQB+ABtMAAJ0b3EAfgAbTAAFdmFsdWVxAH4AG3hyABV2Yy5kYXRhLlRBQ0NtZCRTaW1wbGXtJtYlMQZ10gIAAHhyABN2Yy5kYXRhLlRBQ0NtZCRTcGVjG6vxAPjBA74CAAB4cgAOdmMuZGF0YS5UQUNDbWRUyw+IPDkf8AIAAHhwcQB+AOBzcQB+AF5zcQB+ADZzcQB+ADZwcHEAfgBMcHEAfgBicHEAfgBjcHEAfgDlcQB+AOZzcQB+ADBzcQB+ADZwc3EAfgA2cHNxAH4ANnBwcQB+AENwcQB+AEtxAH4ATHBxAH4AUHEAfgBRcHEAfgBVcQB+AFZzcQB+AF5zcQB+ADZzcQB+ADZwcHEAfgBMcHEAfgBicHEAfgBjcHEAfgBlcQB+AGZzcQB+AF5zcQB+ADZzcQB+ADZwcHEAfgBMcHEAfgBicHEAfgBjcHEAfgDGcQB+AMdzcQB+ADZwcHNxAH4AQH5xAH4ARHQACUNhbGxUcmFjZXQACHRhYy5tZXRhdnIAE3ZjLmRhdGEuVEFDTWV0YUluZm81YEz9pUuocQIABkkABWJlZ2luSQADbGVuSQAGc291cmNlTAAHYWRkcmVzc3EAfgAGTAAIanVtcFR5cGV0ABNMY29tcGlsZXIvSnVtcFR5cGU7TAANc291cmNlQ29udGV4dHQAGExjb21waWxlci9Tb3VyY2VDb250ZXh0O3hwcHNxAH4BBgAAGLcAAAAdAAAAB3EAfgAPfnIAEWNvbXBpbGVyLkp1bXBUeXBlAAAAAAAAAAASAAB4cQB+AEV0AAdSRUdVTEFSc3IAFmNvbXBpbGVyLlNvdXJjZUNvbnRleHSMy1vpQFzaEwIAAkwAD2luZGV4VG9GaWxlcGF0aHEAfgAnTAAJc291cmNlRGlycQB+ADJ4cHNxAH4AaT9AAAAAAAAMdwgAAAAQAAAACHNxAH4ASQAAAAB0ABVjb250cmFjdHMvQ29udGV4dC5zb2xzcQB+AEkAAAABdAAYY29udHJhY3RzL0N1cnZlVG9rZW4uc29sc3EAfgBJAAAAAnQAH2NvbnRyYWN0cy9DdXJ2ZVRva2VuRXhhbXBsZS5zb2xzcQB+AEkAAAADdAATY29udHJhY3RzL0VSQzIwLnNvbHNxAH4ASQAAAAR0ABRjb250cmFjdHMvSUVSQzIwLnNvbHNxAH4ASQAAAAV0ABxjb250cmFjdHMvSUVSQzIwTWV0YWRhdGEuc29scQB+AEt0AB1jb250cmFjdHMvUmVlbnRyYW5jeUd1YXJkLnNvbHNxAH4ASQAAAAd0ABNjb250cmFjdHMvY3VydmUuc29seHQAEy5wb3N0X2F1dG9maW5kZXJzLjJzcQB+ADBzcQB+ADZwc3EAfgA2cHNxAH4ANnBwcQB+AENwcQB+AEtxAH4ATHBxAH4AUHEAfgBRcHEAfgBVcQB+AFZzcQB+AF5zcQB+ADZzcQB+ADZwcHEAfgBMcHEAfgBicHEAfgBjcHEAfgDTcQB+AGZxAH4A1nNxAH4AXnNxAH4ANnNxAH4ANnNxAH4ANnNxAH4ANnBwcQB+AExwcQB+AGJzcQB+ADZwcHNxAH4AQHEAfgCmdAAadGFjLmNvbnRyYWN0LnN5bS5hZGRyLm5hbWVxAH4AT3B0AAVjdXJ2ZXNxAH4AQHEAfgBGdAAXdGFjLmVudi5rbm93bi1iaXQtd2lkdGhxAH4ASnBzcQB+AEkAAACgcHNxAH4AQHEAfgCmdAAVdGFjLmNvbnRyYWN0LnN5bS5hZGRycQB+ALlwcQB+AA9wcQB+AGNwc3EAfgBJAAAD+nQAA1IzNHNxAH4Ad3EAfgBocQB+AG1zcQB+ADBzcQB+ADZwc3EAfgA2cHNxAH4ANnBwcQB+AENwcQB+AEtxAH4ATHBxAH4AUHEAfgBRcHEAfgBVcQB+AFZzcQB+AF5zcQB+ADZzcQB+ADZwcHEAfgBMcHEAfgBicHEAfgBjcHEAfgDTcQB+AGZxAH4A1nNyACJqYXZhLnV0aWwuQ29sbGVjdGlvbnMkU2luZ2xldG9uU2V0LFJBmCnAsb8CAAFMAAdlbGVtZW50cQB+ADd4cHEAfgAUc3EAfgBec3EAfgA2c3EAfgA2c3EAfgA2c3EAfgA2cHBxAH4ATHBxAH4AYnNxAH4ANnBwcQB+AS5wcQB+ATBxAH4BMXBxAH4BM3BxAH4BNHBxAH4AD3BxAH4AY3BxAH4BNnEAfgE3c3EAfgB3cQB+AGhxAH4AbQ=="}
		AnnotationCmd JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageGlobalChangeSnippet.StorageBackupPoint","calleeTxId":7}}
		NopCmd
		AssumeExpCmd LAnd(Eq(tacCalldatasize!!4:3 0x64 ) Eq(tacCalldatasize!!4:3 0x64 ) )
		AssignExpCmd B572:54 Eq(Select(tacCalldatabuf!!22@7:181 0x0 ) 0x3842f77600000000000000000000000000000000000000000000000000000000 )
		AssumeCmd B572:54
		AssignExpCmd tacCalldatabuf!!573@7:19 LongStore(tacCalldatabuf!!22@7:181 0x4 tacMCANON6!!630:15 0x124 Sub(0x64 0x4 ) )
		LabelCmd "Start procedure curve-get_D(uint256[2],uint256)"
		AnnotationCmd JSON{"key":{"name":"fps.free-pointer-is-scalarized","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true}
		AssignExpCmd R574:54 Select(tacExtcodesize!!9:4 Apply(to_skey:bif R34:63) )
		NopCmd
		AssumeExpCmd Gt(R574:54 0x0 )
		AnnotationCmd JSON{"key":{"name":"internal.func.finder.info","type":"analysis.ip.InternalFunctionFinderReport","erasureStrategy":"Erased"},"value":"rO0ABXNyAChhbmFseXNpcy5pcC5JbnRlcm5hbEZ1bmN0aW9uRmluZGVyUmVwb3J0ian+bYn1VdACAAFMABN1bnJlc29sdmVkRnVuY3Rpb25zdAAPTGphdmEvdXRpbC9TZXQ7eHBzcgAhZGF0YXN0cnVjdHVyZXMuTGlua2VkQXJyYXlIYXNoU2V0AAAAAAAAAAEDAAJGAApsb2FkRmFjdG9yTAAJaGFzaFRhYmxldAAuTGRhdGFzdHJ1Y3R1cmVzL2FycmF5aGFzaHRhYmxlL0FycmF5SGFzaFRhYmxlO3hwdwgAAAAAQAAAAHg="}
		AnnotationCmd JSON{"key":{"name":"fps.free-pointer-is-scalarized","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true}
		NopCmd
		AssumeExpCmd LNot(Lt(tacCalldatasize!!4:3 0x4 ) )
		NopCmd
		AssumeExpCmd Gt(0x82c63066 tacSighash!!41:47 )
		NopCmd
		AssumeExpCmd Eq(0x3842f776 tacSighash!!41:47 )
		AssignExpCmd:182 R580:93 Sub(tacCalldatasize!!4:3 0x4 )
		AssignExpCmd B581:83 Slt(R580:93 0x60 )
		NopCmd
		AssumeExpCmd LNot(B581:83 )
		NopCmd
		AssumeExpCmd Slt(0x23 tacCalldatasize!!4:94 )
		AssignExpCmd:183 R585:96 0x80
		AssumeCmd:184 true
		AssignExpCmd B586:77 Gt(0x44 tacCalldatasize!!4:94 )
		NopCmd
		AssumeExpCmd LNot(B586:77 )
		AnnotationCmd JSON{"key":{"name":"dsa.assign.start","type":"java.lang.String","erasureStrategy":"Erased"},"value":"4280_1005_0_0_0_0 -> 4282_1004_0_0_0_0"}
		LabelCmd "Parallel assignment for R3573:bv256, R3574:bv256 := R2326:bv256, R3653:bv256"
		AnnotationCmd JSON{"key":{"name":"dsa.assign.end","type":"java.lang.String","erasureStrategy":"Erased"},"value":"4280_1005_0_0_0_0 -> 4282_1004_0_0_0_0"}
		AnnotationCmd JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.LoopSnippet.StartLoopSnippet","loopIndex":3,"loopSource":"unknown loop source code"}}
		AnnotationCmd JSON{"key":{"name":"start_loop.cmd","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		AnnotationCmd JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.LoopSnippet.StartIter","iteration":1}}
		AssignExpCmd:185 R588:99 Select(tacCalldatabuf!!573@7:181 0x4 )
		AssignExpCmd:186 tacMCANON3!!589:12 Store(tacMCANON3!!16:12 0x80 R588:99 )
		AnnotationCmd JSON{"key":{"name":"dsa.assign.start","type":"java.lang.String","erasureStrategy":"Erased"},"value":"4301_1002_0_0_0_0 -> 4282_1004_0_0_0_0"}
		LabelCmd "Parallel assignment for R3573:bv256, R3574:bv256 := R3566:bv256, R3570:bv256"
		AnnotationCmd JSON{"key":{"name":"dsa.assign.end","type":"java.lang.String","erasureStrategy":"Erased"},"value":"4301_1002_0_0_0_0 -> 4282_1004_0_0_0_0"}
		AnnotationCmd JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.LoopSnippet.EndIter","iteration":1}}
		AnnotationCmd JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.LoopSnippet.StartIter","iteration":2}}
		AssignExpCmd:185 R590:99 Select(tacCalldatabuf!!573@7:181 0x24 )
		AssignExpCmd:186 tacMCANON3!!591:12 Store(tacMCANON3!!589:12 0xa0 R590:99 )
		AnnotationCmd JSON{"key":{"name":"dsa.assign.start","type":"java.lang.String","erasureStrategy":"Erased"},"value":"4301_1002_0_0_0_0 -> 4282_1004_0_0_0_0"}
		LabelCmd "Parallel assignment for R3573:bv256, R3574:bv256 := R3566:bv256, R3570:bv256"
		AnnotationCmd JSON{"key":{"name":"dsa.assign.end","type":"java.lang.String","erasureStrategy":"Erased"},"value":"4301_1002_0_0_0_0 -> 4282_1004_0_0_0_0"}
		AnnotationCmd JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.LoopSnippet.EndIter","iteration":2}}
		AnnotationCmd JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.LoopSnippet.EndLoopSnippet","loopId":3}}
		AnnotationCmd JSON{"key":{"name":"end_loop.cmd","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		AnnotationCmd JSON{"key":{"name":"pta.end-allocation","type":"analysis.alloc.AllocationAnalysis$AbstractLocation","erasureStrategy":"Erased"},"value":{"prevFPWriteIdx":0,"nextFPWriteCmd":{"block":{"#class":"tac.BlockIdentifier","origStartPc":4102,"stkTop":1000,"decompCopy":0,"calleeIdx":0,"topOfStackValue":0,"freshCopy":0},"pos":1},"sort":{"#class":"analysis.alloc.AllocationAnalysis.Alloc.ConstBlock","sz":"40"}}}
		AssignExpCmd:185 R592:65 Select(tacCalldatabuf!!573@7:181 0x44 )
		AnnotationCmd JSON{"key":{"name":"internal.func.start","type":"analysis.ip.InternalFuncStartAnnotation","erasureStrategy":"CallTrace"},"value":{"id":9,"startPc":558,"args":[{"s":{"namePrefix":"R585","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1001}]},"offset":1,"sort":"SCALAR"},{"s":{"namePrefix":"R592","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1012}]},"offset":2,"sort":"SCALAR"}],"methodSignature":{"#class":"spec.cvlast.QualifiedMethodSignature.QualifiedMethodSig","qualifiedMethodName":{"#class":"spec.cvlast.QualifiedFunction","host":{"name":"curve"},"methodId":"get_D"},"params":[{"#class":"spec.cvlast.VMParam.Named","name":"xp","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$StaticArrayDescriptor","location":"memory","elementType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256},"numElements":"2"}},{"#class":"spec.cvlast.VMParam.Named","name":"amp","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256}}],"res":[{"#class":"spec.cvlast.VMParam.Unnamed","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256}}]},"stackOffsetToArgPos":{"1":0,"2":1},"callSiteSrc":{"source":7,"begin":2956,"len":1542,"jumpType":"ENTER","address":"ce4604a0000000000000000000000028","sourceContext":{"indexToFilepath":{"0":"contracts/Context.sol","1":"contracts/CurveToken.sol","2":"contracts/CurveTokenExample.sol","3":"contracts/ERC20.sol","4":"contracts/IERC20.sol","5":"contracts/IERC20Metadata.sol","6":"contracts/ReentrancyGuard.sol","7":"contracts/curve.sol"},"sourceDir":".post_autofinders.2"}}}}
		AssignExpCmd:187 R593:83 Select(tacMCANON3!!591:12 0xa0 )
		AssignExpCmd:188 R594:93 Select(tacMCANON3!!591:12 0x80 )
		NopCmd
		AssumeExpCmd Apply(add_noofl:bif R594:93 R593:83)
		NopCmd
		NopCmd
		NopCmd
		AssignExpCmd R600:72 Apply(safe_math_narrow:bif IntAdd(Apply(safe_math_promotion:bif R594:93) Apply(safe_math_promotion:bif R593:83)))
		AnnotationCmd JSON{"key":{"name":"internal.func.end","type":"analysis.ip.InternalFuncExitAnnotation","erasureStrategy":"Canonical"},"value":{"id":9,"rets":[{"s":{"namePrefix":"R600","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1023}]},"offset":0}],"functionLayout":{"0":{"#class":"analysis.ip.InternalFuncValueLocation.Scalar"}}}}
		AnnotationCmd JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.EVMFunctionReturnWrite","returnbufOffset":"0","returnValueSym":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R600","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1023}]},"callIndex":7}}
		AnnotationCmd JSON{"key":{"name":"tac.return.path","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		LabelCmd "End procedure curve-get_D(uint256[2],uint256)"
		AssignExpCmd tacReturndata!!602:78 Store(tacReturndata!!634:78 0x0 R600:72 )
		AssignExpCmd tacMCANON6!!603:15 Store(tacMCANON6!!630:15 0x120 R600:72 )
		AnnotationCmd JSON{"key":{"name":"call.trace.pop","type":"analysis.icfg.Inliner$CallStack$PopRecord","erasureStrategy":"Canonical"},"value":"rO0ABXNyAClhbmFseXNpcy5pY2ZnLklubGluZXIkQ2FsbFN0YWNrJFBvcFJlY29yZPAPfwSLdCWJAgABSQAIY2FsbGVlSWR4cAAAAAc="}
		JumpCmd 6_0_0_5_0_0
	}
	Block 0_0_0_8_0_0 Succ [7_0_0_5_0_0] {
		AnnotationCmd JSON{"key":{"name":"call.trace.push","type":"analysis.icfg.Inliner$CallStack$PushRecord","erasureStrategy":"Canonical"},"value":"rO0ABXNyACphbmFseXNpcy5pY2ZnLklubGluZXIkQ2FsbFN0YWNrJFB1c2hSZWNvcmSX8+DCTLCH+AIAA0kACGNhbGxlZUlkTAAGY2FsbGVldAATTHZjL2RhdGEvTWV0aG9kUmVmO0wAB3N1bW1hcnl0ABVMdmMvZGF0YS9DYWxsU3VtbWFyeTt4cAAAAAhzcgARdmMuZGF0YS5NZXRob2RSZWbJlJTzzU9pGAIAA0wABGF0dHJ0ABdMc2NlbmUvTWV0aG9kQXR0cmlidXRlO0wACmNvbnRyYWN0SWR0ABZMamF2YS9tYXRoL0JpZ0ludGVnZXI7TAAHc2lnSGFzaHQAEExldm0vU2lnaGFzaEludDt4cHNyABxzY2VuZS5NZXRob2RBdHRyaWJ1dGUkQ29tbW9uNHjdebdr9XMCAAB4cgAVc2NlbmUuTWV0aG9kQXR0cmlidXRlcYg2pYWutuUCAAB4cHNyABRqYXZhLm1hdGguQmlnSW50ZWdlcoz8nx+pO/sdAwAGSQAIYml0Q291bnRJAAliaXRMZW5ndGhJABNmaXJzdE5vbnplcm9CeXRlTnVtSQAMbG93ZXN0U2V0Qml0SQAGc2lnbnVtWwAJbWFnbml0dWRldAACW0J4cgAQamF2YS5sYW5nLk51bWJlcoaslR0LlOCLAgAAeHD///////////////7////+AAAAAXVyAAJbQqzzF/gGCFTgAgAAeHAAAAAQzkYEoAAAAAAAAAAAAAAACHhzcgAOZXZtLlNpZ2hhc2hJbnRUdcqNMXEgeAIAAUwAAW5xAH4ABnhwc3EAfgAM///////////////+/////gAAAAF1cQB+ABAAAAAEGBYN3XhzcgATdmMuZGF0YS5DYWxsU3VtbWFyeZQcmw5vl+FdAgAQSQAJc3VtbWFyeUlkTAAOY2FsbENvbnZlbnRpb250ACZMaW5zdHJ1bWVudGF0aW9uL2NhbGxzL0NhbGxDb252ZW50aW9uO0wACmNhbGxUYXJnZXR0ABpMYW5hbHlzaXMvaWNmZy9DYWxsVGFyZ2V0O0wACGNhbGxUeXBldAAVTHZjL2RhdGEvVEFDQ2FsbFR5cGU7TAAPY2Fubm90QmVJbmxpbmVkdAAtTGFuYWx5c2lzL2ljZmcvSW5saW5lciRJbGxlZ2FsSW5saW5pbmdSZWFzb247TAAGZ2FzVmFydAATTHZjL2RhdGEvVEFDU3ltYm9sO0wABmluQmFzZXEAfgAbTAAIaW5PZmZzZXRxAH4AG0wABmluU2l6ZXEAfgAbTAAMb3JpZ0NhbGxjb3JldAAgTHZjL2RhdGEvVEFDQ21kJFNpbXBsZSRDYWxsQ29yZTtMAAdvdXRCYXNlcQB+ABtMAAlvdXRPZmZzZXRxAH4AG0wAB291dFNpemVxAH4AG0wADXNpZ1Jlc29sdXRpb250AA9MamF2YS91dGlsL1NldDtMAAV0b1ZhcnEAfgAbTAAIdmFsdWVWYXJxAH4AG3hwAAAABXNyACRpbnN0cnVtZW50YXRpb24uY2FsbHMuQ2FsbENvbnZlbnRpb25HtO1ulL788QIAA0kACGNhbGxlcklkTAAFaW5wdXR0ABlMYW5hbHlzaXMvaWNmZy9DYWxsSW5wdXQ7TAAGcmF3T3V0dAAiTGluc3RydW1lbnRhdGlvbi9jYWxscy9DYWxsT3V0cHV0O3hwAAAAAHNyABdhbmFseXNpcy5pY2ZnLkNhbGxJbnB1dJjJD1MhNUxQAgAHTAAHYmFzZVZhcnQAGUx2Yy9kYXRhL1RBQ0V4cHIkU3ltJFZhcjtMABBlbmNvZGVkQXJndW1lbnRzdAAjTGFuYWx5c2lzL2ljZmcvQUJJQXJndW1lbnRFbmNvZGluZztMABNpbnB1dFNpemVMb3dlckJvdW5kcQB+AAZMAAZvZmZzZXR0ABVMdmMvZGF0YS9UQUNFeHByJFN5bTtMABRyYW5nZVRvRGVjb21wb3NlZEFyZ3QAD0xqYXZhL3V0aWwvTWFwO0wAEHNpbXBsaWZpZWRPZmZzZXR0ABtMdmMvZGF0YS9UQUNFeHByJFN5bSRDb25zdDtMAARzaXplcQB+ACZ4cHNyABd2Yy5kYXRhLlRBQ0V4cHIkU3ltJFZhcskrg43eGgPnAgACTAABc3QAF0x2Yy9kYXRhL1RBQ1N5bWJvbCRWYXI7TAADdGFndAAJTHRhYy9UYWc7eHIAE3ZjLmRhdGEuVEFDRXhwciRTeW2iVj0S4YSNUAIAAHhyAA92Yy5kYXRhLlRBQ0V4cHJYhGlUu/v+yAIAAHhwc3IANnZjLmRhdGEuVEFDU3ltYm9sJFZhciRXaXRoRGVmYXVsdENhbGxJbmRleCRXaXRoQnl0ZU1hcJ7+oHF4CHAAAgACTAAEbWV0YXQALUxrb3RsaW54L2NvbGxlY3Rpb25zL2ltbXV0YWJsZS9QZXJzaXN0ZW50TWFwO0wACm5hbWVQcmVmaXh0ABJMamF2YS9sYW5nL1N0cmluZzt4cgAVdmMuZGF0YS5UQUNTeW1ib2wkVmFyCYrCGVl9SXYCAAB4cgARdmMuZGF0YS5UQUNTeW1ib2zd3Run/CoWswIAAHhwc3IAJmRhdGFzdHJ1Y3R1cmVzLnRyZWFwLkhhc2hUcmVhcE1hcCROb2Rlf2t9acJIPnQCAANMAANrZXl0ABJMamF2YS9sYW5nL09iamVjdDtMAARuZXh0dAA1TGRhdGFzdHJ1Y3R1cmVzL3RyZWFwL0hhc2hUcmVhcE1hcCRNb3JlS2V5VmFsdWVQYWlycztMAAV2YWx1ZXEAfgA3eHIAIWRhdGFzdHJ1Y3R1cmVzLnRyZWFwLkhhc2hUcmVhcE1hcPMJ/2vt3boKAgAAeHIAHWRhdGFzdHJ1Y3R1cmVzLnRyZWFwLlRyZWFwTWFw46LAyn3v5moCAAB4cgAaZGF0YXN0cnVjdHVyZXMudHJlYXAuVHJlYXA88f21zZwbdQIAAkwABGxlZnR0ABxMZGF0YXN0cnVjdHVyZXMvdHJlYXAvVHJlYXA7TAAFcmlnaHRxAH4APHhwcHNxAH4ANnBzcQB+ADZwcHNyAAt0YWMuTWV0YUtleVF/W3MiCfIZAgADTAAPZXJhc3VyZVN0cmF0ZWd5dAAdTHRhYy9NZXRhS2V5JEVyYXN1cmVTdHJhdGVneTtMAARuYW1lcQB+ADJMAAN0eXB0ABFMamF2YS9sYW5nL0NsYXNzO3hwfnIAG3RhYy5NZXRhS2V5JEVyYXN1cmVTdHJhdGVneQAAAAAAAAAAEgAAeHIADmphdmEubGFuZy5FbnVtAAAAAAAAAAASAAB4cHQACUNhbm9uaWNhbHQAF3RhYy5tZW1vcnkucGFydGl0aW9uLWlkdnIAEWphdmEubGFuZy5JbnRlZ2VyEuKgpPeBhzgCAAFJAAV2YWx1ZXhxAH4ADnBzcQB+AEkAAAAGc3EAfgBAcQB+AEZ0ABJUYWMuc3ltYm9sLmtleXdvcmR2cgAQamF2YS5sYW5nLlN0cmluZ6DwpDh6O7NCAgAAeHBwdAAEdGFjTXNxAH4AQHEAfgBGdAANdGFjLmlzLm1lbW9yeXZyACJ0YWMuTWV0YU1hcCRDb21wYW5pb24kTm90aGluZ1ZhbHVl8nsHH85ykpUCAAB4cHBzcQB+AFN0AA90YWNNQ0FOT042ISE2NTZzcgAPdGFjLlRhZyRCeXRlTWFwNb/Ry6GDRgkCAAB4cgALdGFjLlRhZyRNYXABJytzDV3P/QIAAHhyAAd0YWMuVGFnLk9V3gn2xngCAAB4cHBzcQB+AAz///////////////7////+AAAAAXVxAH4AEAAAAAEEeHNxAH4AKnNyADV2Yy5kYXRhLlRBQ1N5bWJvbCRWYXIkV2l0aERlZmF1bHRDYWxsSW5kZXgkV2l0aEJpdDI1NnqsyEgq0drPAgACTAAEbWV0YXEAfgAxTAAKbmFtZVByZWZpeHEAfgAyeHEAfgAzc3EAfgA2c3EAfgA2cHBxAH4ATHB0AAFMcHNxAH4AQHEAfgBGdAAQdGFjLnN0YWNrLmhlaWdodHEAfgBKcHNxAH4ASQAAA/V0AARSNjU3c3IADnRhYy5UYWckQml0MjU2IyLQT+LlKkgCAAB4cQB+AFlzcgARamF2YS51dGlsLkhhc2hNYXAFB9rBwxZg0QMAAkYACmxvYWRGYWN0b3JJAAl0aHJlc2hvbGR4cD9AAAAAAAABdwgAAAACAAAAAXNyAB5hbmFseXNpcy5pY2ZnLlNjcmF0Y2hCeXRlUmFuZ2XBTLaPpUzj2gIAAkwABGZyb21xAH4ABkwAAnRvcQB+AAZ4cHNxAH4ADP///////////////v////4AAAAAdXEAfgAQAAAAAHhzcQB+AAz///////////////7////+AAAAAXVxAH4AEAAAAAEDeHNyAC1hbmFseXNpcy5pY2ZnLkRlY29tcG9zZWRDYWxsSW5wdXRBcmckQ29uc3RhbnSFavLdQafqPQIAA0wAAWN0ABlMdmMvZGF0YS9UQUNTeW1ib2wkQ29uc3Q7TAARY29udHJhY3RSZWZlcmVuY2V0AC9MYW5hbHlzaXMvaWNmZy9DYWxsR3JhcGhCdWlsZGVyJENhbGxlZENvbnRyYWN0O0wADHNjcmF0Y2hSYW5nZXQAIExhbmFseXNpcy9pY2ZnL1NjcmF0Y2hCeXRlUmFuZ2U7eHIAJGFuYWx5c2lzLmljZmcuRGVjb21wb3NlZENhbGxJbnB1dEFy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cQB+AExwcQB+AGJzcQB+AEBxAH4ARnQAFnRhYy5zY2FsYXJpemF0aW9uLnNvcnR2cgAZdmMuZGF0YS5TY2FsYXJpemF0aW9uU29ydDDOcJ3kaA0mAgAAeHBwc3IAIHZjLmRhdGEuU2NhbGFyaXphdGlvblNvcnQkUGFja2VkLkWtEpOI5PcCAAJJAAVzdGFydEwAC3BhY2tlZFN0YXJ0dAAbTHZjL2RhdGEvU2NhbGFyaXphdGlvblNvcnQ7eHEAfgDtAAAAAHNyAB92Yy5kYXRhLlNjYWxhcml6YXRpb25Tb3J0JFNwbGl0VP9Zp/HHsgUCAAFMAANpZHhxAH4ABnhxAH4A7XNxAH4ADP///////////////v////4AAAABdXEAfgAQAAAAAQx4c3EAfgA2cHNxAH4ANnBzcQB+ADZwcHNxAH4AQHEAfgBGdAAcdGFjLnN0b3JhZ2Uubm9uLWluZGV4ZWQtcGF0aHZyADVhbmFseXNpcy5zdG9yYWdlLlN0b3JhZ2VBbmFseXNpc1Jlc3VsdCROb25JbmRleGVkUGF0aAjBoEuh+j9FAgAAeHBwc3IAOmFuYWx5c2lzLnN0b3JhZ2UuU3RvcmFnZUFuYWx5c2lzUmVzdWx0JE5vbkluZGV4ZWRQYXRoJFJvb3S/N/XYpeoK/wIAAUwABHNsb3RxAH4ABnhxAH4A+3EAfgD0c3EAfgBAcQB+AEZ0AA10YWMuc2xvdC50eXBldnIAOnNwZWMuY3ZsYXN0LnR5cGVkZXNjcmlwdG9ycy5FVk1UeXBlRGVzY3JpcHRvciRFVk1WYWx1ZVR5cGXGia8Cuuq4JQIAAHhyAC1zcGVjLmN2bGFzdC50eXBlZGVzY3JpcHRvcnMuRVZNVHlwZURlc2NyaXB0b3LIUanxPMJqHQIAAHhwcHNyADVzcGVjLmN2bGFzdC50eXBlZGVzY3JpcHRvcnMuRVZNVHlwZURlc2NyaXB0b3IkYWRkcmVzc3r4ZfRvl6ApAgAAeHIARHNwZWMuY3ZsYXN0LnR5cGVkZXNjcmlwdG9ycy5FVk1UeXBlRGVzY3JpcHRvciRFVk1Jc29tb3JwaGljVmFsdWVUeXBl93WYkW4QoQ8CAAB4cQB+AQFzcQB+AEB+cQB+AER0AAZFcmFzZWR0ABh0YWMuc3RvcmFnZS5wcmV0dHkucGF0aHN2cgAdYW5hbHlzaXMuc3RvcmFnZS5EaXNwbGF5UGF0aHP3REu3w/VRFgIAAUwABXBhdGhzcQB+AB14cHBzcQB+AQtzcgAXamF2YS51dGlsLkxpbmtlZEhhc2hTZXTYbNdald0qHgIAAHhyABFqYXZhLnV0aWwuSGFzaFNldLpEhZWWuLc0AwAAeHB3DAAAABA/QAAAAAAAAXNyACFhbmFseXNpcy5zdG9yYWdlLkRpc3BsYXlQYXRoJFJvb3TTc6C9mdA8cgIAAkwABGJhc2V0AB5MYW5hbHlzaXMvc3RvcmFnZS9EaXNwbGF5UGF0aDtMAARuYW1lcQB+ADJ4cgAcYW5hbHlzaXMuc3RvcmFnZS5EaXNwbGF5UGF0aE9AY+pW0iAFAgAAeHBwdAAIbHBfdG9rZW54c3EAfgBAcQB+AEZ0ABV0YWMuc3RvcmFnZS5iaXQtd2lkdGhxAH4ASnBzcQB+AEkAAACgcHNxAH4AQHEAfgBGdAALdGFjLnN0b3JhZ2V2cQB+AAxwcQB+AMZwcQB+AGNwc3EAfgBJAAAD+XQAC0NBTk9OMTkhITI1c3EAfgB3cQB+AGhxAH4AbXNxAH4AMHNxAH4ANnBzcQB+ADZwc3EAfgA2cHBxAH4AQ3BxAH4AS3EAfgBMcHEAfgBQcQB+AFFwcQB+AFVxAH4AVnNxAH4AXnNxAH4ANnNxAH4ANnBwcQB+AExwcQB+AGJwcQB+AGNwcQB+AI1xAH4AZnEAfgCQc3IAImphdmEudXRpbC5Db2xsZWN0aW9ucyRTaW5nbGV0b25TZXQsUkGYKcCxvwIAAUwAB2VsZW1lbnRxAH4AN3hwcQB+ABRzcQB+AF5zcQB+ADZzcQB+ADZzcQB+ADZzcQB+ADZwc3EAfgA2cHBxAH4ATHBxAH4AYnEAfgDrcHEAfgDxc3EAfgA2cHNxAH4ANnBzcQB+ADZwcHEAfgD5cHEAfgD+cQB+AP9wcQB+AQZxAH4BB3BzcQB+AQtzcQB+AQ53DAAAABA/QAAAAAAAAXEAfgEUeHEAfgEWcHEAfgEYcHEAfgEZcHEAfgDGcHEAfgBjcHEAfgEccQB+AR1zcQB+AHdxAH4AaHEAfgBt"}
		AnnotationCmd JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageGlobalChangeSnippet.StorageBackupPoint","calleeTxId":8}}
		NopCmd
		AssumeExpCmd LAnd(Eq(tacCalldatasize!!5:3 0x4 ) Eq(tacCalldatasize!!5:3 0x4 ) )
		NopCmd
		AssumeExpCmd Eq(tacCalldatabufCANON0@8:1 0x18160ddd00000000000000000000000000000000000000000000000000000000 )
		LabelCmd "Start procedure CurveTokenExample-totalSupply()"
		AnnotationCmd JSON{"key":{"name":"fps.free-pointer-is-scalarized","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true}
		AssignExpCmd R607:54 Select(tacExtcodesize!!9:4 Apply(to_skey:bif R32:103) )
		NopCmd
		AssumeExpCmd Gt(R607:54 0x0 )
		AnnotationCmd JSON{"key":{"name":"internal.func.finder.info","type":"analysis.ip.InternalFunctionFinderReport","erasureStrategy":"Erased"},"value":"rO0ABXNyAChhbmFseXNpcy5pcC5JbnRlcm5hbEZ1bmN0aW9uRmluZGVyUmVwb3J0ian+bYn1VdACAAFMABN1bnJlc29sdmVkRnVuY3Rpb25zdAAPTGphdmEvdXRpbC9TZXQ7eHBzcgAhZGF0YXN0cnVjdHVyZXMuTGlua2VkQXJyYXlIYXNoU2V0AAAAAAAAAAEDAAJGAApsb2FkRmFjdG9yTAAJaGFzaFRhYmxldAAuTGRhdGFzdHJ1Y3R1cmVzL2FycmF5aGFzaHRhYmxlL0FycmF5SGFzaFRhYmxlO3hwdwgAAAAAQAAAAHg="}
		AnnotationCmd JSON{"key":{"name":"fps.free-pointer-is-scalarized","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true}
		NopCmd
		AssumeExpCmd LNot(Lt(tacCalldatasize!!5:3 0x4 ) )
		NopCmd
		AssumeExpCmd Gt(0x40c10f19 tacSighash!!42:47 )
		NopCmd
		AssumeExpCmd LNot(Eq(0x6fdde03 tacSighash!!42:47 ) )
		NopCmd
		AssumeExpCmd LNot(Eq(0x95ea7b3 tacSighash!!42:47 ) )
		NopCmd
		AssumeExpCmd Eq(0x18160ddd tacSighash!!42:47 )
		AnnotationCmd JSON{"key":{"name":"internal.func.start","type":"analysis.ip.InternalFuncStartAnnotation","erasureStrategy":"CallTrace"},"value":{"id":10,"startPc":1205,"args":[],"methodSignature":{"#class":"spec.cvlast.QualifiedMethodSignature.QualifiedMethodSig","qualifiedMethodName":{"#class":"spec.cvlast.QualifiedFunction","host":{"name":"CurveTokenExample"},"methodId":"totalSupply"},"params":[],"res":[{"#class":"spec.cvlast.VMParam.Unnamed","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256}}]},"stackOffsetToArgPos":{},"callSiteSrc":{"source":3,"begin":3954,"len":364,"jumpType":"ENTER","address":"ce4604a0000000000000000000000008","sourceContext":{"indexToFilepath":{"0":"contracts/Context.sol","1":"contracts/CurveToken.sol","2":"contracts/CurveTokenExample.sol","3":"contracts/ERC20.sol","4":"contracts/IERC20.sol","5":"contracts/IERC20Metadata.sol"},"sourceDir":".post_autofinders.0"}}}}
		AnnotationCmd JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet","value":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"CANON87!!29","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.scalarization.sort","type":"vc.data.ScalarizationSort","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.ScalarizationSort.Split","idx":"2"}},{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.storage.bit-width","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":256},{"key":{"name":"tac.storage.pretty.paths","type":"analysis.storage.DisplayPaths","erasureStrategy":"Erased"},"value":{"paths":[{"#class":"analysis.storage.DisplayPath.Root","name":"_totalSupply"}]}},{"key":{"name":"tac.slot.type","type":"spec.cvlast.typedescriptors.EVMTypeDescriptor$EVMValueType","erasureStrategy":"Canonical"},"value":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256}},{"key":{"name":"tac.storage.non-indexed-path","type":"analysis.storage.StorageAnalysisResult$NonIndexedPath","erasureStrategy":"Canonical"},"value":{"#class":"analysis.storage.StorageAnalysisResult.NonIndexedPath.Root","slot":"2"}},{"key":{"name":"tac.storage","type":"java.math.BigInteger","erasureStrategy":"Canonical"},"value":"ce4604a0000000000000000000000008"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1021}]},"displayPath":{"#class":"analysis.storage.DisplayPath.Root","name":"_totalSupply"},"storageType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256},"contractInstance":"ce4604a0000000000000000000000008","linkableStorageReadId":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet.Id","id":9}}}
		AnnotationCmd JSON{"key":{"name":"internal.func.end","type":"analysis.ip.InternalFuncExitAnnotation","erasureStrategy":"Canonical"},"value":{"id":10,"rets":[{"s":{"namePrefix":"CANON87!!29","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.scalarization.sort","type":"vc.data.ScalarizationSort","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.ScalarizationSort.Split","idx":"2"}},{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.storage.bit-width","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":256},{"key":{"name":"tac.storage.pretty.paths","type":"analysis.storage.DisplayPaths","erasureStrategy":"Erased"},"value":{"paths":[{"#class":"analysis.storage.DisplayPath.Root","name":"_totalSupply"}]}},{"key":{"name":"tac.slot.type","type":"spec.cvlast.typedescriptors.EVMTypeDescriptor$EVMValueType","erasureStrategy":"Canonical"},"value":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256}},{"key":{"name":"tac.storage.non-indexed-path","type":"analysis.storage.StorageAnalysisResult$NonIndexedPath","erasureStrategy":"Canonical"},"value":{"#class":"analysis.storage.StorageAnalysisResult.NonIndexedPath.Root","slot":"2"}},{"key":{"name":"tac.storage","type":"java.math.BigInteger","erasureStrategy":"Canonical"},"value":"ce4604a0000000000000000000000008"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1023}]},"offset":0}],"functionLayout":{"0":{"#class":"analysis.ip.InternalFuncValueLocation.Scalar"}}}}
		AnnotationCmd JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.EVMFunctionReturnWrite","returnbufOffset":"0","returnValueSym":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"CANON87!!29","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.scalarization.sort","type":"vc.data.ScalarizationSort","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.ScalarizationSort.Split","idx":"2"}},{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.storage.bit-width","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":256},{"key":{"name":"tac.storage.pretty.paths","type":"analysis.storage.DisplayPaths","erasureStrategy":"Erased"},"value":{"paths":[{"#class":"analysis.storage.DisplayPath.Root","name":"_totalSupply"}]}},{"key":{"name":"tac.slot.type","type":"spec.cvlast.typedescriptors.EVMTypeDescriptor$EVMValueType","erasureStrategy":"Canonical"},"value":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256}},{"key":{"name":"tac.storage.non-indexed-path","type":"analysis.storage.StorageAnalysisResult$NonIndexedPath","erasureStrategy":"Canonical"},"value":{"#class":"analysis.storage.StorageAnalysisResult.NonIndexedPath.Root","slot":"2"}},{"key":{"name":"tac.storage","type":"java.math.BigInteger","erasureStrategy":"Canonical"},"value":"ce4604a0000000000000000000000008"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1023}]},"callIndex":8}}
		AnnotationCmd JSON{"key":{"name":"tac.return.path","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		LabelCmd "End procedure CurveTokenExample-totalSupply()"
		AssignExpCmd tacReturndata!!616:78 Store(tacReturndata!!659:78 0x0 CANON87!!29:104 )
		AssignExpCmd tacMCANON6!!617:15 Store(tacMCANON6!!656:15 0x140 CANON87!!29:104 )
		AnnotationCmd JSON{"key":{"name":"call.trace.pop","type":"analysis.icfg.Inliner$CallStack$PopRecord","erasureStrategy":"Canonical"},"value":"rO0ABXNyAClhbmFseXNpcy5pY2ZnLklubGluZXIkQ2FsbFN0YWNrJFBvcFJlY29yZPAPfwSLdCWJAgABSQAIY2FsbGVlSWR4cAAAAAg="}
		JumpCmd 7_0_0_5_0_0
	}
	Block 5_0_0_5_0_0 Succ [0_0_0_7_0_0] {
		AssumeNotCmd:170 false
		AnnotationCmd JSON{"key":{"name":"pta.fake-return.start","type":"analysis.CmdPointer","erasureStrategy":"Erased"},"value":{"block":{"#class":"tac.BlockIdentifier","origStartPc":1608,"stkTop":1007,"decompCopy":0,"calleeIdx":0,"topOfStackValue":2,"freshCopy":0},"pos":1}}
		AnnotationCmd JSON{"key":{"name":"pta.fake-return.end","type":"analysis.CmdPointer","erasureStrategy":"Erased"},"value":{"block":{"#class":"tac.BlockIdentifier","origStartPc":1608,"stkTop":1007,"decompCopy":0,"calleeIdx":0,"topOfStackValue":2,"freshCopy":0},"pos":6}}
		AssumeNotCmd:189 false
		AssignExpCmd:190 R618:96 Select(tacMCANON6!!569:15 0x100 )
		NopCmd
		AssumeExpCmd LNot(Lt(R618:96 R530:67 ) )
		AssignExpCmd:191 R620:166 Sub(R618:96 R530:67 )
		AssignExpCmd:167 tacMCANON5!!621:14 Store(tacMCANON5!!529:14 0xe0 R620:166 )
		AnnotationCmd JSON{"key":{"name":"pta.end-allocation","type":"analysis.alloc.AllocationAnalysis$AbstractLocation","erasureStrategy":"Erased"},"value":{"prevFPWriteIdx":1,"nextFPWriteCmd":{"block":{"#class":"tac.BlockIdentifier","origStartPc":16,"stkTop":1024,"decompCopy":0,"calleeIdx":0,"topOfStackValue":2,"freshCopy":0},"pos":44},"sort":{"#class":"analysis.alloc.AllocationAnalysis.Alloc.ConstBlock","sz":"40"}}}
		AnnotationCmd JSON{"key":{"name":"internal.func.start","type":"analysis.ip.InternalFuncStartAnnotation","erasureStrategy":"CallTrace"},"value":{"id":8,"startPc":3822,"args":[],"methodSignature":{"#class":"spec.cvlast.QualifiedMethodSignature.QualifiedMethodSig","qualifiedMethodName":{"#class":"spec.cvlast.QualifiedFunction","host":{"name":"curve"},"methodId":"_A"},"params":[],"res":[{"#class":"spec.cvlast.VMParam.Unnamed","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256}}]},"stackOffsetToArgPos":{},"callSiteSrc":{"source":7,"begin":6351,"len":4,"jumpType":"ENTER","address":"ce4604a0000000000000000000000028","sourceContext":{"indexToFilepath":{"0":"contracts/Context.sol","1":"contracts/CurveToken.sol","2":"contracts/CurveTokenExample.sol","3":"contracts/ERC20.sol","4":"contracts/IERC20.sol","5":"contracts/IERC20Metadata.sol","6":"contracts/ReentrancyGuard.sol","7":"contracts/curve.sol"},"sourceDir":".post_autofinders.2"}}}}
		AnnotationCmd JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet","value":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"CANON99!!31","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.scalarization.sort","type":"vc.data.ScalarizationSort","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.ScalarizationSort.Split","idx":"5"}},{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.storage.bit-width","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":256},{"key":{"name":"tac.storage.pretty.paths","type":"analysis.storage.DisplayPaths","erasureStrategy":"Erased"},"value":{"paths":[{"#class":"analysis.storage.DisplayPath.Root","name":"future_A"}]}},{"key":{"name":"tac.slot.type","type":"spec.cvlast.typedescriptors.EVMTypeDescriptor$EVMValueType","erasureStrategy":"Canonical"},"value":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256}},{"key":{"name":"tac.storage.non-indexed-path","type":"analysis.storage.StorageAnalysisResult$NonIndexedPath","erasureStrategy":"Canonical"},"value":{"#class":"analysis.storage.StorageAnalysisResult.NonIndexedPath.Root","slot":"5"}},{"key":{"name":"tac.storage","type":"java.math.BigInteger","erasureStrategy":"Canonical"},"value":"ce4604a0000000000000000000000028"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1013}]},"displayPath":{"#class":"analysis.storage.DisplayPath.Root","name":"future_A"},"storageType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256},"contractInstance":"ce4604a0000000000000000000000028","linkableStorageReadId":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet.Id","id":7}}}
		AnnotationCmd JSON{"key":{"name":"internal.func.end","type":"analysis.ip.InternalFuncExitAnnotation","erasureStrategy":"Canonical"},"value":{"id":8,"rets":[{"s":{"namePrefix":"CANON99!!31","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.scalarization.sort","type":"vc.data.ScalarizationSort","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.ScalarizationSort.Split","idx":"5"}},{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.storage.bit-width","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":256},{"key":{"name":"tac.storage.pretty.paths","type":"analysis.storage.DisplayPaths","erasureStrategy":"Erased"},"value":{"paths":[{"#class":"analysis.storage.DisplayPath.Root","name":"future_A"}]}},{"key":{"name":"tac.slot.type","type":"spec.cvlast.typedescriptors.EVMTypeDescriptor$EVMValueType","erasureStrategy":"Canonical"},"value":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256}},{"key":{"name":"tac.storage.non-indexed-path","type":"analysis.storage.StorageAnalysisResult$NonIndexedPath","erasureStrategy":"Canonical"},"value":{"#class":"analysis.storage.StorageAnalysisResult.NonIndexedPath.Root","slot":"5"}},{"key":{"name":"tac.storage","type":"java.math.BigInteger","erasureStrategy":"Canonical"},"value":"ce4604a0000000000000000000000028"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1015}]},"offset":0}],"functionLayout":{"0":{"#class":"analysis.ip.InternalFuncValueLocation.Scalar"}}}}
		AssignExpCmd:192 tacMCANON6!!624:15 Store(tacMCANON6!!569:15 0x120 0x3842f77600000000000000000000000000000000000000000000000000000000 )
		AnnotationCmd JSON{"key":{"name":"dsa.assign.start","type":"java.lang.String","erasureStrategy":"Erased"},"value":"4639_1007_0_0_0_0 -> 4643_1005_0_0_0_0"}
		LabelCmd "Parallel assignment for R4170:bv256, R4207:bv256, B4208:bool, R4209:bv256 := R6282:bv256, R365:bv256, B4072:bool, R4073:bv256"
		AnnotationCmd JSON{"key":{"name":"dsa.assign.end","type":"java.lang.String","erasureStrategy":"Erased"},"value":"4639_1007_0_0_0_0 -> 4643_1005_0_0_0_0"}
		AnnotationCmd JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.LoopSnippet.StartLoopSnippet","loopIndex":2,"loopSource":"unknown loop source code"}}
		AnnotationCmd JSON{"key":{"name":"start_loop.cmd","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		AnnotationCmd JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.LoopSnippet.StartIter","iteration":1}}
		AssignExpCmd:193 R625:77 Select(tacMCANON5!!621:14 0xc0 )
		AssignExpCmd:194 tacMCANON6!!626:15 Store(tacMCANON6!!624:15 0x124 R625:77 )
		AnnotationCmd JSON{"key":{"name":"dsa.assign.start","type":"java.lang.String","erasureStrategy":"Erased"},"value":"4674_1003_0_0_0_0 -> 4643_1005_0_0_0_0"}
		LabelCmd "Parallel assignment for R4170:bv256, R4207:bv256, B4208:bool, R4209:bv256 := R3940:bv256, R3983:bv256, B4205:bool, R4202:bv256"
		AnnotationCmd JSON{"key":{"name":"dsa.assign.end","type":"java.lang.String","erasureStrategy":"Erased"},"value":"4674_1003_0_0_0_0 -> 4643_1005_0_0_0_0"}
		AnnotationCmd JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.LoopSnippet.EndIter","iteration":1}}
		AnnotationCmd JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.LoopSnippet.StartIter","iteration":2}}
		AssignExpCmd:193 R627:77 Select(tacMCANON5!!621:14 0xe0 )
		AssignExpCmd:194 tacMCANON6!!628:15 Store(tacMCANON6!!626:15 0x144 R627:77 )
		AnnotationCmd JSON{"key":{"name":"dsa.assign.start","type":"java.lang.String","erasureStrategy":"Erased"},"value":"4674_1003_0_0_0_0 -> 4643_1005_0_0_0_0"}
		LabelCmd "Parallel assignment for R4170:bv256, R4207:bv256, B4208:bool, R4209:bv256 := R3940:bv256, R3983:bv256, B4205:bool, R4202:bv256"
		AnnotationCmd JSON{"key":{"name":"dsa.assign.end","type":"java.lang.String","erasureStrategy":"Erased"},"value":"4674_1003_0_0_0_0 -> 4643_1005_0_0_0_0"}
		AnnotationCmd JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.LoopSnippet.EndIter","iteration":2}}
		AnnotationCmd JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.LoopSnippet.EndLoopSnippet","loopId":2}}
		AnnotationCmd JSON{"key":{"name":"end_loop.cmd","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		AssignExpCmd:195 tacMCANON6!!630:15 Store(tacMCANON6!!628:15 0x164 CANON99!!31:196 )
		AssignExpCmd:192 R631:197 0x120
		NopCmd
		AssignHavocCmd:192 R633:147
		AssignHavocCmd tacReturndata!!634:78
		JumpCmd 0_0_0_7_0_0
	}
	Block 7_0_0_5_0_0 Succ [8_0_0_0_0_0] {
		AssumeNotCmd:198 false
		AnnotationCmd JSON{"key":{"name":"pta.fake-return.start","type":"analysis.CmdPointer","erasureStrategy":"Erased"},"value":{"block":{"#class":"tac.BlockIdentifier","origStartPc":3278,"stkTop":1014,"decompCopy":0,"calleeIdx":0,"topOfStackValue":2,"freshCopy":0},"pos":1}}
		AnnotationCmd JSON{"key":{"name":"pta.fake-return.end","type":"analysis.CmdPointer","erasureStrategy":"Erased"},"value":{"block":{"#class":"tac.BlockIdentifier","origStartPc":3278,"stkTop":1014,"decompCopy":0,"calleeIdx":0,"topOfStackValue":2,"freshCopy":0},"pos":6}}
		AssumeNotCmd:189 false
		AssignExpCmd:190 R635:76 Select(tacMCANON6!!617:15 0x140 )
		NopCmd
		AssumeExpCmd Apply(mul_noofl:bif R650:69 0x8ac7230489e80000)
		NopCmd
		AssignExpCmd:199 I644:54 IntMul(Apply(safe_math_promotion:bif R650:69) 0x8ac7230489e80000)
		NopCmd
		NopCmd
		AssumeExpCmd Gt(R635:76 0x0 )
		AssignExpCmd:200 R647:72 Div(Apply(safe_math_narrow:bif I644:54) R635:76 )
		AnnotationCmd JSON{"key":{"name":"internal.func.end","type":"analysis.ip.InternalFuncExitAnnotation","erasureStrategy":"Canonical"},"value":{"id":6,"rets":[{"s":{"namePrefix":"R647","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1021}]},"offset":0}],"functionLayout":{"0":{"#class":"analysis.ip.InternalFuncValueLocation.Scalar"}}}}
		AnnotationCmd JSON{"key":{"name":"internal.func.end","type":"analysis.ip.InternalFuncExitAnnotation","erasureStrategy":"Canonical"},"value":{"id":5,"rets":[{"s":{"namePrefix":"R647","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1023}]},"offset":0}],"functionLayout":{"0":{"#class":"analysis.ip.InternalFuncValueLocation.Scalar"}}}}
		AnnotationCmd JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.EVMFunctionReturnWrite","returnbufOffset":"0","returnValueSym":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R647","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1023}]},"callIndex":5}}
		AnnotationCmd JSON{"key":{"name":"tac.return.path","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		LabelCmd "End procedure curve-func1_caller()"
		JumpCmd 8_0_0_0_0_0
	}
	Block 6_0_0_5_0_0 Succ [0_0_0_8_0_0] {
		AssumeNotCmd:192 false
		AnnotationCmd JSON{"key":{"name":"pta.fake-return.start","type":"analysis.CmdPointer","erasureStrategy":"Erased"},"value":{"block":{"#class":"tac.BlockIdentifier","origStartPc":3129,"stkTop":1015,"decompCopy":0,"calleeIdx":0,"topOfStackValue":2,"freshCopy":0},"pos":1}}
		AnnotationCmd JSON{"key":{"name":"pta.fake-return.end","type":"analysis.CmdPointer","erasureStrategy":"Erased"},"value":{"block":{"#class":"tac.BlockIdentifier","origStartPc":3129,"stkTop":1015,"decompCopy":0,"calleeIdx":0,"topOfStackValue":2,"freshCopy":0},"pos":6}}
		AssumeNotCmd:189 false
		AssignExpCmd:190 R650:69 Select(tacMCANON6!!603:15 0x120 )
		AssignExpCmd B652:54 Le(CANON19!!25:201 0xffffffffffffffffffffffffffffffffffffffff )
		AssignExpCmd B653:54 Ge(CANON19!!25:201 0x0 )
		NopCmd
		AssumeExpCmd LAnd(B652:54 B653:54 )
		AnnotationCmd JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet","value":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"CANON19!!25","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.scalarization.sort","type":"vc.data.ScalarizationSort","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.ScalarizationSort.Packed","packedStart":{"#class":"vc.data.ScalarizationSort.Split","idx":"c"},"start":0}},{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.storage.bit-width","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":160},{"key":{"name":"tac.storage.pretty.paths","type":"analysis.storage.DisplayPaths","erasureStrategy":"Erased"},"value":{"paths":[{"#class":"analysis.storage.DisplayPath.Root","name":"lp_token"}]}},{"key":{"name":"tac.slot.type","type":"spec.cvlast.typedescriptors.EVMTypeDescriptor$EVMValueType","erasureStrategy":"Canonical"},"value":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.address"}},{"key":{"name":"tac.storage.non-indexed-path","type":"analysis.storage.StorageAnalysisResult$NonIndexedPath","erasureStrategy":"Canonical"},"value":{"#class":"analysis.storage.StorageAnalysisResult.NonIndexedPath.Root","slot":"c"}},{"key":{"name":"tac.storage","type":"java.math.BigInteger","erasureStrategy":"Canonical"},"value":"ce4604a0000000000000000000000028"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1016}]},"displayPath":{"#class":"analysis.storage.DisplayPath.Root","name":"lp_token"},"storageType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.address"},"contractInstance":"ce4604a0000000000000000000000028","linkableStorageReadId":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet.Id","id":8}}}
		AnnotationCmd JSON{"key":{"name":"init.reorder.fence","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		AssignExpCmd:198 tacMCANON6!!656:15 Store(tacMCANON6!!603:15 0x140 0x18160ddd00000000000000000000000000000000000000000000000000000000 )
		AssignExpCmd:198 R657:72 0x140
		AssignHavocCmd:198 R658:69
		AssignHavocCmd tacReturndata!!659:78
		JumpCmd 0_0_0_8_0_0
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
      "value": 9
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
      "value": 10
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
      "value": 7
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
      "value": 11
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
      "value": 5
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
      "value": 6
    }
  ],
  "16": [
    {
      "key": {
        "name": "Tac.symbol.keyword",
        "type": "java.lang.String",
        "erasureStrategy": "Canonical"
      },
      "value": "tacBalance"
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
          "callIndex": 11,
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
  "40": [
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
  "41": [
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
  "42": [
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
  "43": [
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
      "value": "ce4604a0000000000000000000000028"
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
      "value": "ce4604a0000000000000000000000028"
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
      "value": "ce4604a0000000000000000000000011"
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
              "namePrefix": "R175",
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
                "namePrefix": "R175",
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
      "value": "ce4604a0000000000000000000000008"
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
          "callIndex": 10,
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
      "value": "rO0ABXNyADJhbmFseXNpcy5pY2ZnLkNhbGxHcmFwaEJ1aWxkZXIkQ29udHJhY3RTdG9yYWdlUmVhZLRpTKYiS4EFAgABSQACaWR4cAAAAAs="
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
              "namePrefix": "R318",
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
                "namePrefix": "R318",
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
                "callIndex": 10,
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
                "callIndex": 10,
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
          "namePrefix": "tacCalldatasize!!7",
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
          "callIndex": 11,
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
            "namePrefix": "I424",
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
  "159": [
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
  "160": [
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
            "namePrefix": "I10",
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
            "namePrefix": "I439",
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
  "161": [
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
  "163": [
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
  "164": [
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
  "165": [
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
  "167": [
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
  "168": [
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
  "169": [
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
      "value": 1009
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
  "171": [
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
  "172": [
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
  "173": [
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
  "174": [
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
  "175": [
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
  "176": [
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
  "177": [
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
  "178": [
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
  "179": [
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
  "180": [
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
              "namePrefix": "R560",
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
                "namePrefix": "R560",
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
  "181": [
    {
      "key": {
        "name": "tac.immutable.array",
        "type": "vc.data.ImmutableBound",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "sym": {
          "#class": "vc.data.TACSymbol.Var.Full",
          "namePrefix": "tacCalldatasize!!4",
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
  "182": [
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
  "183": [
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
  "184": [
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
          "callIndex": 7,
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
  "185": [
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
  "186": [
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
  "187": [
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
  "188": [
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
  "189": [
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
  "190": [
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
  "191": [
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
  "192": [
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
  "193": [
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
  "194": [
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
  "195": [
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
  "196": [
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
      "value": 1015
    }
  ],
  "197": [
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
  "198": [
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
  "199": [
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
  "200": [
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
  "201": [
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
      "value": 1016
    }
  ]
}