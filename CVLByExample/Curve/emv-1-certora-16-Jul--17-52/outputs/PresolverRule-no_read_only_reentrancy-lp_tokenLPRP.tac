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
		B23:JSON{"name":"B23","paramSorts":[],"returnSort":{"#class":"tac.Tag.Bool"},"attribute":"Ghost","cvlResultType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"},"cvlParamTypes":[],"declarationName":"CANON75"}
		CANON143:JSON{"name":"CANON143","paramSorts":[],"returnSort":{"#class":"tac.Tag.Int"},"attribute":"Ghost","cvlResultType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256},"cvlParamTypes":[],"declarationName":"CANON143"}
		CANON147:JSON{"name":"CANON147","paramSorts":[],"returnSort":{"#class":"tac.Tag.Int"},"attribute":"Ghost","cvlResultType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256},"cvlParamTypes":[],"declarationName":"CANON147"}
		CANON75:JSON{"name":"CANON75","paramSorts":[],"returnSort":{"#class":"tac.Tag.Bool"},"attribute":"Ghost","cvlResultType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"},"cvlParamTypes":[],"declarationName":"CANON75"}
		CANON77:JSON{"name":"CANON77","paramSorts":[],"returnSort":{"#class":"tac.Tag.Int"},"attribute":"Ghost","cvlResultType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256},"cvlParamTypes":[],"declarationName":"CANON77"}
		I11:JSON{"name":"I11","paramSorts":[],"returnSort":{"#class":"tac.Tag.Int"},"attribute":"Ghost","cvlResultType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256},"cvlParamTypes":[],"declarationName":"CANON143"}
		I24:JSON{"name":"I24","paramSorts":[],"returnSort":{"#class":"tac.Tag.Int"},"attribute":"Ghost","cvlResultType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256},"cvlParamTypes":[],"declarationName":"CANON77"}
	}
	tacM0x40@1:bv256
	tacM0x40@6:bv256
	tacMCANON1!!12:bytemap
	tacMCANON1!!13:bytemap
	tacMCANON2!!14:bytemap
	tacMCANON2!!15:bytemap
	tacMCANON3!!16:bytemap
	tacMCANON3!!17:bytemap
	tacNonce:wordmap
	tacCaller@1:bv256
	tacCaller@5:bv256
	tacCaller@6:bv256
	tacMCANON2!!236:bytemap
	tacMCANON2!!238:bytemap
	tacMCANON2!!263:bytemap
	tacMCANON2!!297:bytemap
	tacMCANON2!!311:bytemap
	tacMCANON2!!379:bytemap
	tacMCANON2!!381:bytemap
	tacMCANON2!!406:bytemap
	tacMCANON2!!440:bytemap
	tacMCANON2!!454:bytemap
	tacMCANON2!!461:bytemap
	tacMCANON2!!463:bytemap
	tacMCANON2!!465:bytemap
	tacMCANON2!!467:bytemap
	tacMCANON2!!478:bytemap
	tacMCANON2!!480:bytemap
	tacMCANON2!!482:bytemap
	tacMCANON2!!484:bytemap
	tacMCANON2!!525:bytemap
	tacMCANON2!!535:bytemap
	tacCalldatabufCANON0@2:bv256
	tacCalldatabufCANON0@4:bv256
	tacCalldatabufCANON0@7:bv256
	tacCalldatabufCANON0@9:bv256
	tacCalldatabufCANON1@2:bv256
	tacCalldatabufCANON1@7:bv256
	tacOrigNonceCANON0:wordmap
	tacOrigNonceCANON1:wordmap
	tacOrigin!!186:bv256
	tacOrigin!!329:bv256
	tacOrigin!!563:bv256
	tacCallvalue@1:bv256
	tacCallvalue@5:bv256
	tacCallvalue@6:bv256
	CANON266!!590:bool
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
	tacM0x0!!258:bv256
	tacM0x0!!401:bv256
	tacExtcodesize!!6:wordmap
	tacCalldatasize@1:bv256
	tacCalldatasize@2:bv256
	tacCalldatasize@3:bv256
	tacCalldatasize@4:bv256
	tacCalldatasize@5:bv256
	tacCalldatasize@6:bv256
	tacCalldatasize@7:bv256
	tacCalldatasize@8:bv256
	tacCalldatasize@9:bv256
	tacReturndata@1:bytemap
	tacReturndata@6:bytemap
	tacReturnsize@1:bv256
	tacReturnsize@6:bv256
	tacCalldatasize!!169:bv256
	tacCalldatasize!!312:bv256
	tacCalldatasize!!546:bv256
	tacMCANON3!!283:bytemap
	tacMCANON3!!285:bytemap
	tacMCANON3!!426:bytemap
	tacMCANON3!!428:bytemap
	tacCalldatabuf!!19@3:bytemap
	tacCalldatabuf!!20@8:bytemap
	tacM0x0@2:bv256
	tacM0x0@7:bv256
	tacRC@1:bv256
	tacRC@6:bv256
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
	CANON114@1:bool
	CANON114@2:bool
	CANON114@3:bool
	CANON114@4:bool
	CANON114@5:bool
	CANON114@6:bool
	CANON114@7:bool
	CANON114@8:bool
	CANON114@9:bool
	CANON115:wordmap
	CANON116@1:bool
	CANON116@6:bool
	CANON117@1:bool
	CANON117@6:bool
	CANON118@1:bool
	CANON118@6:bool
	CANON119@1:bv256
	CANON119@6:bv256
	CANON120@1:bv256
	CANON120@6:bv256
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
	CANON148@6:bool
	CANON149:bool
	CANON150:bool
	CANON153@2:bv256
	CANON153@3:bv256
	CANON153@4:bv256
	CANON153@5:bv256
	CANON153@7:bv256
	CANON153@8:bv256
	CANON153@9:bv256
	CANON154@1:bv256
	CANON154@6:bv256
	CANON155@1:bv256
	CANON155@6:bv256
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
	CANON169@6:bool
	CANON170@1:bool
	CANON170@6:bool
	CANON171@1:bool
	CANON171@6:bool
	CANON172@1:bv256
	CANON172@6:bv256
	CANON173:bool
	CANON174:int
	CANON175:int
	CANON176:int
	CANON177@1:bool
	CANON177@6:bool
	CANON178:int
	CANON179:bool
	CANON180:int
	CANON181:int
	CANON182:int
	CANON183:int
	CANON184:int
	CANON185:bv256
	CANON186:bv256
	CANON187:bool
	CANON188:bool
	CANON189:int
	CANON190:bool
	CANON191:bv256
	CANON192:int
	CANON193:bool
	CANON194:bv256
	CANON195:int
	CANON196:bool
	CANON197:bv256
	CANON198:int
	CANON199:bool
	CANON200:bv256
	CANON201:int
	CANON202:bool
	CANON203:bv256
	CANON204:int
	CANON205:bool
	CANON206:bv256
	CANON207:int
	CANON208:bool
	CANON209:bv256
	CANON210@5:bool
	CANON211@5:bool
	CANON212@5:bool
	CANON213:int
	CANON214:int
	CANON215:int
	CANON216:int
	CANON217:int
	CANON218:int
	CANON219:bool
	CANON220:bool
	CANON221:int
	CANON222:bool
	CANON223:bv256
	CANON224:int
	CANON225:bool
	CANON226:bv256
	CANON227:int
	CANON228:bool
	CANON229:bv256
	CANON230:int
	CANON231:bool
	CANON232:bv256
	CANON233:int
	CANON234:bool
	CANON235:bv256
	CANON236:int
	CANON237:bool
	CANON238:bv256
	CANON239:int
	CANON240:bool
	CANON241:bv256
	CANON242:int
	CANON243:int
	CANON244:bool
	CANON245:int
	CANON246:bool
	CANON247:bool
	CANON248:int
	CANON249:int
	CANON250:bool
	CANON251:int
	CANON252:bool
	CANON253:bool
	CANON254:bool
	CANON255:bool
	CANON256:bool
	CANON257:bool
	CANON258:int
	CANON259:int
	CANON260:int
	CANON261:bool
	CANON262:int
	CANON263:int
	CANON264:int
	CANON265:int
	CANON266:bool
	CANON267:bool
	tacMCANON0havocme5395@1:bytemap
	tacMCANON0havocme5396@6:bytemap
	tacMCANON0@1:bytemap
	tacMCANON0@6:bytemap
	tacMCANON1@1:bytemap
	tacMCANON1@6:bytemap
	tacMCANON2@1:bytemap
	tacMCANON2@6:bytemap
	tacMCANON3@3:bytemap
	tacMCANON3@8:bytemap
	tacBalance:wordmap
	tacTimestamp!!196:bv256
	tacTimestamp!!339:bv256
	tacTimestamp!!573:bv256
	tacBalance!!18:wordmap
	tacNumber@1:bv256
	tacNumber@5:bv256
	tacNumber@6:bv256
	CANON56!!21:bv256
	CANON57!!22:bv256
	tacCalldatabuf@1:bytemap
	tacCalldatabuf@3:bytemap
	tacCalldatabuf@6:bytemap
	tacCalldatabuf@8:bytemap
	B23:bool
	B40:bool
	B41:bool
	B42:bool
	B43:bool
	B44:bool
	B45:bool
	B46:bool
	B47:bool
	B48:bool
	B50:bool
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
	B93:bool
	B94:bool
	B95:bool
	B96:bool
	B97:bool
	B98:bool
	B99:bool
	I11:int
	I24:int
	R25:bv256
	R26:bv256
	R27:bv256
	R28:bv256
	R29:bv256
	R30:bv256
	R49:bv256
	R51:bv256
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
	B170:bool
	B171:bool
	B173:bool
	B176:bool
	B178:bool
	B181:bool
	B184:bool
	B187:bool
	B189:bool
	B192:bool
	B194:bool
	B197:bool
	B199:bool
	B202:bool
	B211:bool
	B214:bool
	B215:bool
	B216:bool
	B217:bool
	B218:bool
	B219:bool
	B220:bool
	B221:bool
	B222:bool
	B223:bool
	B227:bool
	B232:bool
	B233:bool
	B234:bool
	B243:bool
	B244:bool
	B246:bool
	B247:bool
	B248:bool
	B249:bool
	B250:bool
	B252:bool
	B253:bool
	B255:bool
	B256:bool
	B265:bool
	B266:bool
	B269:bool
	B270:bool
	B271:bool
	B272:bool
	B275:bool
	B276:bool
	B277:bool
	B278:bool
	B280:bool
	B281:bool
	B290:bool
	B299:bool
	B300:bool
	B302:bool
	B303:bool
	B304:bool
	B305:bool
	B306:bool
	B307:bool
	B313:bool
	B314:bool
	B316:bool
	B319:bool
	B321:bool
	B324:bool
	B327:bool
	B330:bool
	B332:bool
	B335:bool
	B337:bool
	B340:bool
	B342:bool
	B345:bool
	B354:bool
	B357:bool
	B358:bool
	B359:bool
	B360:bool
	B361:bool
	B362:bool
	B363:bool
	B364:bool
	B365:bool
	B366:bool
	B370:bool
	B375:bool
	B376:bool
	B377:bool
	B386:bool
	B387:bool
	B389:bool
	B390:bool
	B391:bool
	B392:bool
	B393:bool
	B395:bool
	B396:bool
	B398:bool
	B399:bool
	B408:bool
	B409:bool
	B412:bool
	B413:bool
	B414:bool
	B415:bool
	B418:bool
	B419:bool
	B420:bool
	B421:bool
	B423:bool
	B424:bool
	B433:bool
	B442:bool
	B443:bool
	B445:bool
	B446:bool
	B447:bool
	B448:bool
	B449:bool
	B450:bool
	B456:bool
	B473:bool
	B491:bool
	B493:bool
	B494:bool
	B496:bool
	B500:bool
	B506:bool
	B508:bool
	B509:bool
	B511:bool
	B515:bool
	B521:bool
	B522:bool
	B523:bool
	B531:bool
	B532:bool
	B533:bool
	B547:bool
	B548:bool
	B550:bool
	B553:bool
	B555:bool
	B558:bool
	B561:bool
	B564:bool
	B566:bool
	B569:bool
	B571:bool
	B574:bool
	B576:bool
	B579:bool
	B588:bool
	B591:bool
	B593:bool
	B594:bool
	B595:bool
	B596:bool
	B597:bool
	B599:bool
	B600:bool
	B601:bool
	I163:int
	I164:int
	I165:int
	I166:int
	I167:int
	I168:int
	I172:int
	I177:int
	I183:int
	I188:int
	I193:int
	I198:int
	I201:int
	I207:int
	I291:int
	I292:int
	I293:int
	I315:int
	I320:int
	I326:int
	I331:int
	I336:int
	I341:int
	I344:int
	I350:int
	I434:int
	I435:int
	I436:int
	I497:int
	I498:int
	I503:int
	I512:int
	I513:int
	I518:int
	I540:int
	I541:int
	I542:int
	I543:int
	I544:int
	I549:int
	I554:int
	I560:int
	I565:int
	I570:int
	I575:int
	I578:int
	I584:int
	I603:int
	I604:int
	I605:int
	I606:int
	I607:int
	I608:int
	R174:bv256
	R179:bv256
	R185:bv256
	R190:bv256
	R195:bv256
	R200:bv256
	R203:bv256
	R204:bv256
	R205:bv256
	R206:bv256
	R209:bv256
	R210:bv256
	R213:bv256
	R224:bv256
	R225:bv256
	R226:bv256
	R228:bv256
	R230:bv256
	R231:bv256
	R235:bv256
	R237:bv256
	R239:bv256
	R240:bv256
	R245:bv256
	R251:bv256
	R254:bv256
	R257:bv256
	R259:(uninterp) skey
	R260:bv256
	R261:bv256
	R268:bv256
	R273:bv256
	R274:bv256
	R279:bv256
	R282:bv256
	R284:bv256
	R286:bv256
	R287:bv256
	R288:bv256
	R289:bv256
	R294:bv256
	R295:bv256
	R301:bv256
	R308:bv256
	R309:bv256
	R317:bv256
	R322:bv256
	R328:bv256
	R333:bv256
	R338:bv256
	R343:bv256
	R346:bv256
	R347:bv256
	R348:bv256
	R349:bv256
	R352:bv256
	R353:bv256
	R356:bv256
	R367:bv256
	R368:bv256
	R369:bv256
	R371:bv256
	R373:bv256
	R374:bv256
	R378:bv256
	R380:bv256
	R382:bv256
	R383:bv256
	R388:bv256
	R394:bv256
	R397:bv256
	R400:bv256
	R402:(uninterp) skey
	R403:bv256
	R404:bv256
	R411:bv256
	R416:bv256
	R417:bv256
	R422:bv256
	R425:bv256
	R427:bv256
	R429:bv256
	R430:bv256
	R431:bv256
	R432:bv256
	R437:bv256
	R438:bv256
	R444:bv256
	R451:bv256
	R452:bv256
	R455:bv256
	R457:bv256
	R459:bv256
	R460:bv256
	R462:bv256
	R464:bv256
	R466:bv256
	R468:bv256
	R469:bv256
	R470:bv256
	R472:bv256
	R474:bv256
	R476:bv256
	R477:bv256
	R479:bv256
	R481:bv256
	R483:bv256
	R485:bv256
	R486:bv256
	R487:bv256
	R489:bv256
	R490:bv256
	R492:bv256
	R495:bv256
	R499:bv256
	R501:bv256
	R502:bv256
	R504:bv256
	R505:bv256
	R507:bv256
	R510:bv256
	R514:bv256
	R516:bv256
	R517:bv256
	R519:bv256
	R520:bv256
	R524:bv256
	R526:bv256
	R527:bv256
	R529:bv256
	R530:bv256
	R534:bv256
	R536:bv256
	R537:bv256
	R545:bv256
	R551:bv256
	R556:bv256
	R562:bv256
	R567:bv256
	R572:bv256
	R577:bv256
	R580:bv256
	R581:bv256
	R582:bv256
	R583:bv256
	R586:bv256
	R587:bv256
	R592:bv256
	R598:bv256
	R602:bv256
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
	tacAddress@1:bv256
	tacAddress@2:bv256
	tacAddress@3:bv256
	tacAddress@4:bv256
	tacAddress@5:bv256
	tacAddress@6:bv256
	tacAddress@7:bv256
	tacAddress@8:bv256
	tacAddress@9:bv256
	CANON179!!539:bool
	CANON139!!10:bv256
	tacOrigBalanceCANON0:wordmap
	tacOrigBalanceCANON1:wordmap
	CANON115!!7:wordmap
	CANON124!!8:bv256
	CANON130!!9:wordmap
	LCANON0@1:bv256
	LCANON0@2:bv256
	LCANON0@3:bv256
	LCANON0@4:bv256
	LCANON0@5:bv256
	LCANON0@6:bv256
	LCANON0@7:bv256
	LCANON0@8:bv256
	LCANON0@9:bv256
	LCANON1@1:bool
	LCANON1@5:bool
	LCANON1@6:bool
	LCANON2@1:bool
	LCANON2@2:bool
	LCANON2@3:bool
	LCANON2@4:bool
	LCANON2@5:bool
	LCANON2@6:bool
	LCANON2@7:bool
	LCANON2@8:bool
	LCANON2@9:bool
	LCANON3@1:bool
	LCANON3@2:bool
	LCANON3@3:bool
	LCANON3@4:bool
	LCANON3@5:bool
	LCANON3@6:bool
	LCANON3@7:bool
	LCANON3@8:bool
	LCANON3@9:bool
	LCANON4@1:bool
	LCANON4@2:bool
	LCANON4@5:bool
	LCANON4@6:bool
	LCANON4@7:bool
	LCANON5@1:bool
	LCANON5@2:bool
	LCANON5@6:bool
	LCANON5@7:bool
	LCANON6@1:bool
	LCANON6@6:bool
	LCANON7@1:bool
	LCANON7@6:bool
	LCANON8@1:bool
	LCANON8@6:bool
	LCANON9@1:bool
	LCANON9@6:bool
	tacCallvalue!!180:bv256
	tacCallvalue!!323:bv256
	tacCallvalue!!557:bv256
	tacOrigin@1:bv256
	tacOrigin@5:bv256
	tacOrigin@6:bv256
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
	LCANON10@6:bv256
	LCANON11@1:bv256
	LCANON11@6:bv256
	LCANON12@1:bv256
	LCANON12@6:bv256
	LCANON13@1:bv256
	LCANON13@6:bv256
	LCANON14@1:bv256
	LCANON14@6:bv256
	LCANON15@1:bool
	LCANON15@6:bool
	LCANON16@1:bv256
	LCANON16@6:bv256
	LCANON17@1:bv256
	LCANON17@6:bv256
	LCANON18@1:bv256
	LCANON18@6:bv256
	LCANON19@1:bv256
	LCANON19@6:bv256
	LCANON20@1:bv256
	LCANON20@6:bv256
	LCANON21@1:bv256
	LCANON21@6:bv256
	LCANON22@1:bv256
	LCANON22@6:bv256
	LCANON23@1:bv256
	LCANON23@6:bv256
	LCANON24@2:bv256
	LCANON24@7:bv256
	LCANON25@2:bool
	LCANON25@7:bool
	LCANON26@2:bv256
	LCANON26@7:bv256
	LCANON27@2:bool
	LCANON27@7:bool
	LCANON28@2:bv256
	LCANON28@4:bv256
	LCANON28@7:bv256
	LCANON28@9:bv256
	LCANON29@2:bv256
	LCANON29@7:bv256
	LCANON30@2:bv256
	LCANON30@7:bv256
	LCANON31@2:bv256
	LCANON31@7:bv256
	LCANON32@1:bool
	LCANON32@6:bool
	LCANON33@1:bv256
	LCANON33@6:bv256
	LCANON34@1:bv256
	LCANON34@6:bv256
	LCANON35@1:bv256
	LCANON35@6:bv256
	LCANON36@1:bool
	LCANON36@6:bool
	LCANON37@1:bv256
	LCANON37@6:bv256
	LCANON38@1:bool
	LCANON38@6:bool
	LCANON39@1:bv256
	LCANON39@6:bv256
	LCANON40@1:bv256
	LCANON40@6:bv256
	LCANON41@1:bv256
	LCANON41@6:bv256
	LCANON42@1:bv256
	LCANON42@6:bv256
	LCANON43@1:bv256
	LCANON43@6:bv256
	LCANON44@1:bv256
	LCANON44@6:bv256
	LCANON45@1:bv256
	LCANON45@6:bv256
	LCANON46@1:bv256
	LCANON46@6:bv256
	LCANON47@1:bv256
	LCANON47@6:bv256
	LCANON48@1:bv256
	LCANON48@6:bv256
	LCANON49@1:bv256
	LCANON49@6:bv256
	LCANON50@3:bool
	LCANON50@8:bool
	LCANON51@3:bv256
	LCANON51@8:bv256
	LCANON52@3:bv256
	LCANON52@8:bv256
	LCANON53@3:bool
	LCANON53@8:bool
	LCANON54@3:bool
	LCANON54@8:bool
	LCANON55@3:bv256
	LCANON55@8:bv256
	LCANON56@3:bool
	LCANON56@8:bool
	LCANON57@3:bv256
	LCANON57@8:bv256
	LCANON58@3:bool
	LCANON58@8:bool
	LCANON59@3:bool
	LCANON59@8:bool
	LCANON60@3:bv256
	LCANON60@8:bv256
	LCANON61@3:bv256
	LCANON61@8:bv256
	LCANON62@3:bv256
	LCANON62@8:bv256
	LCANON63@3:bv256
	LCANON63@8:bv256
	LCANON64@3:bv256
	LCANON64@8:bv256
	LCANON65@3:bool
	LCANON65@8:bool
	LCANON66@3:bv256
	LCANON66@8:bv256
	LCANON67@3:bv256
	LCANON67@8:bv256
	LCANON68@1:bool
	LCANON68@6:bool
	LCANON69@1:bv256
	LCANON69@6:bv256
	LCANON70@1:bv256
	LCANON70@6:bv256
	LCANON71@1:bv256
	LCANON71@6:bv256
	LCANON72@1:bv256
	LCANON72@6:bv256
	LCANON73@1:bool
	LCANON73@6:bool
	LCANON74@1:bv256
	LCANON74@6:bv256
	LCANON75@1:bv256
	LCANON75@6:bv256
	LCANON76@1:bv256
	LCANON76@6:bv256
	LCANON77@1:bv256
	LCANON77@6:bv256
	LCANON78@1:bv256
	LCANON78@6:bv256
	LCANON79@1:bv256
	LCANON79@6:bv256
	LCANON80@1:bv256
	LCANON80@6:bv256
	LCANON81@4:bool
	LCANON81@9:bool
	LCANON82@4:bool
	LCANON82@9:bool
	LCANON83@4:bool
	LCANON83@9:bool
	LCANON84@4:bv256
	LCANON84@9:bv256
	LCANON85@1:bv256
	LCANON85@6:bv256
	LCANON86@1:bv256
	LCANON86@6:bv256
	LCANON87@1:bv256
	LCANON87@6:bv256
	LCANON88@1:bv256
	LCANON88@6:bv256
	LCANON89@1:bool
	LCANON89@6:bool
	LCANON90@1:bv256
	LCANON90@6:bv256
	LCANON91@1:bool
	LCANON91@6:bool
	LCANON92@1:bool
	LCANON92@6:bool
	LCANON93@1:bv256
	LCANON93@6:bv256
	LCANON94@1:bv256
	LCANON94@6:bv256
	LCANON95@1:bool
	LCANON95@6:bool
	LCANON96@1:bv256
	LCANON96@6:bv256
	LCANON97@1:bv256
	LCANON97@6:bv256
	LCANON98@1:bv256
	LCANON98@6:bv256
	LCANON99@5:bv256
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
	tacAddress!!182:bv256
	tacAddress!!242:bv256
	tacAddress!!264:bv256
	tacAddress!!298:bv256
	tacAddress!!325:bv256
	tacAddress!!385:bv256
	tacAddress!!407:bv256
	tacAddress!!441:bv256
	tacAddress!!559:bv256
	tacReturndata!!241:bytemap
	tacReturndata!!262:bytemap
	tacReturndata!!296:bytemap
	tacReturndata!!310:bytemap
	tacReturndata!!384:bytemap
	tacReturndata!!405:bytemap
	tacReturndata!!439:bytemap
	tacReturndata!!453:bytemap
	tacReturndata!!471:bytemap
	tacReturndata!!488:bytemap
	tacReturndata!!528:bytemap
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
	tacCalldatabuf!!267@3:bytemap
	tacCalldatabuf!!410@8:bytemap
	tacSCANON0:wordmap
	tacSCANON1:wordmap
	tacSCANON2:wordmap
	tacCaller!!175:bv256
	tacCaller!!318:bv256
	tacCaller!!552:bv256
	tacCalldatasize!!0:bv256
	tacCalldatasize!!1:bv256
	tacCalldatasize!!2:bv256
	tacCalldatasize!!3:bv256
	tacCalldatasize!!4:bv256
	tacCalldatasize!!5:bv256
	tacMCANON1!!229:bytemap
	tacMCANON1!!372:bytemap
	tacMCANON1!!458:bytemap
	tacMCANON1!!475:bytemap
	LCANON100@5:bv256
	tacBalance!!208:wordmap
	tacBalance!!212:wordmap
	tacBalance!!351:wordmap
	tacBalance!!355:wordmap
	tacBalance!!585:wordmap
	tacBalance!!589:wordmap
	tacTimestamp@1:bv256
	tacTimestamp@5:bv256
	tacTimestamp@6:bv256
	tacSighash!!31:bv256
	tacSighash!!32:bv256
	tacSighash!!33:bv256
	tacSighash!!34:bv256
	tacSighash!!35:bv256
	tacSighash!!36:bv256
	tacSighash!!37:bv256
	tacSighash!!38:bv256
	tacSighash!!39:bv256
	tacSighash@1:bv256
	tacSighash@2:bv256
	tacSighash@3:bv256
	tacSighash@4:bv256
	tacSighash@5:bv256
	tacSighash@6:bv256
	tacSighash@7:bv256
	tacSighash@8:bv256
	tacSighash@9:bv256
	tacNumber!!191:bv256
	tacNumber!!334:bv256
	tacNumber!!568:bv256
}
Program {
	Block 0_0_0_0_0_0 Succ [0_0_0_1_0_0] {
		AssignHavocCmd tacCalldatabufCANON0@2:0
		AssignHavocCmd tacCalldatabufCANON0@4:0
		AssignHavocCmd tacCalldatabufCANON0@7:1
		AssignHavocCmd tacCalldatabufCANON0@9:1
		AssignHavocCmd tacCalldatasize!!0:2
		AssignHavocCmd tacCalldatasize!!1:2
		AssignHavocCmd tacCalldatasize!!2:2
		AssignHavocCmd tacCalldatasize!!3:2
		AssignHavocCmd tacCalldatasize!!4:2
		AssignHavocCmd tacCalldatasize!!5:2
		AssignHavocCmd tacExtcodesize!!6:3
		AssignHavocCmd CANON115!!7:4
		AssignHavocCmd CANON124!!8:5
		AssignHavocCmd CANON130!!9:6
		AssignHavocCmd CANON139!!10:7
		AssignHavocCmd I11
		AssignHavocCmd CANON186:8
		AssignExpCmd tacMCANON1!!12:9 ByteMapDefinition(i.5422:bv256 -> 0x0 )
		AssignExpCmd tacMCANON1!!13:10 ByteMapDefinition(i.5423:bv256 -> 0x0 )
		AssignExpCmd tacMCANON2!!14:11 ByteMapDefinition(i.5424:bv256 -> 0x0 )
		AssignExpCmd tacMCANON2!!15:12 ByteMapDefinition(i.5425:bv256 -> 0x0 )
		AssignExpCmd tacMCANON3!!16:13 ByteMapDefinition(i.5426:bv256 -> 0x0 )
		AssignExpCmd tacMCANON3!!17:14 ByteMapDefinition(i.5427:bv256 -> 0x0 )
		AssignHavocCmd tacBalance!!18:15
		AssignExpCmd tacCalldatabuf@1:16 ByteMapDefinition(i.5428:bv256 -> Ite(Lt(i.5428 tacCalldatasize@1:2 ) Unconstrained(bv256) 0x0 ) )
		AssignExpCmd tacCalldatabuf!!19@3:17 ByteMapDefinition(i.5429:bv256 -> Ite(Lt(i.5429 tacCalldatasize!!1:2 ) Unconstrained(bv256) 0x0 ) )
		AssignExpCmd tacCalldatabuf@6:18 ByteMapDefinition(i.5430:bv256 -> Ite(Lt(i.5430 tacCalldatasize@6:2 ) Unconstrained(bv256) 0x0 ) )
		AssignExpCmd tacCalldatabuf!!20@8:19 ByteMapDefinition(i.5431:bv256 -> Ite(Lt(i.5431 tacCalldatasize!!4:2 ) Unconstrained(bv256) 0x0 ) )
		AssignHavocCmd CANON56!!21:20
		AssignHavocCmd CANON57!!22:21
		AssignHavocCmd CANON58:22
		AssignHavocCmd CANON59:23
		AssignHavocCmd CANON60:24
		AssignHavocCmd CANON61:25
		AssignHavocCmd CANON62:26
		AssignHavocCmd CANON63:27
		AssignHavocCmd CANON64:28
		AssignHavocCmd CANON65:29
		AssignHavocCmd CANON66:30
		AssignHavocCmd CANON67:31
		AssignHavocCmd CANON68:32
		AssignHavocCmd CANON69:33
		AssignHavocCmd CANON70:34
		AssignHavocCmd CANON71:35
		AssignHavocCmd CANON72:36
		AssignHavocCmd CANON73:37
		AssignHavocCmd B23
		AssignHavocCmd I24
		AssignHavocCmd R25:38
		AssignHavocCmd R26:39
		AssignHavocCmd R27:40
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
		AssignExpCmd CANON0:45 0x82c63066
		AssignExpCmd CANON1:46 false
		AssignExpCmd CANON2:47 true
		AssignExpCmd CANON3:48 false
		AssignExpCmd CANON4:49 0x0
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
		AssignExpCmd B40:51 Gt(Select(tacExtcodesize!!6:3 Apply(to_skey:bif R25:38) ) 0x0 )
		AssumeCmd B40:51
		AssignExpCmd B41:51 Gt(Select(tacExtcodesize!!6:3 Apply(to_skey:bif R26:39) ) 0x0 )
		AssumeCmd B41:51
		AssignExpCmd B42:51 Gt(Select(tacExtcodesize!!6:3 Apply(to_skey:bif R27:40) ) 0x0 )
		AssumeCmd B42:51
		AnnotationCmd JSON{"key":{"name":"cvl.label.end","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		AnnotationCmd JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Message","s":"assumptions about contracts' addresses"}}
		NopCmd
		AssumeExpCmd Gt(R25:38 0x0 )
		NopCmd
		AssumeExpCmd Le(R25:38 0xffffffffffffffffffffffffffffffffffffffff )
		NopCmd
		AssumeExpCmd Gt(R26:39 0x0 )
		NopCmd
		AssumeExpCmd Le(R26:39 0xffffffffffffffffffffffffffffffffffffffff )
		NopCmd
		AssumeExpCmd Gt(R27:40 0x0 )
		NopCmd
		AssumeExpCmd Le(R27:40 0xffffffffffffffffffffffffffffffffffffffff )
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
		AssignExpCmd R49:51 Select(tacBalance!!18:15 Apply(to_skey:bif R25:38) )
		NopCmd
		AssumeExpCmd Ge(R49:51 0x0 )
		AssignExpCmd R51:51 Select(tacBalance!!18:15 Apply(to_skey:bif R26:39) )
		NopCmd
		AssumeExpCmd Ge(R51:51 0x0 )
		AssignExpCmd R53:51 Select(tacBalance!!18:15 Apply(to_skey:bif R27:40) )
		NopCmd
		AssumeExpCmd Ge(R53:51 0x0 )
		AssignExpCmd R55:51 Select(tacBalance!!18:15 Apply(to_skey:bif R28:41) )
		NopCmd
		AssumeExpCmd Ge(R55:51 0x0 )
		AssignExpCmd R57:51 Select(tacBalance!!18:15 Apply(to_skey:bif R29:42) )
		NopCmd
		AssumeExpCmd Ge(R57:51 0x0 )
		AssignExpCmd R59:51 Select(tacBalance!!18:15 Apply(skey_basic:bif 0x3) )
		NopCmd
		AssumeExpCmd Ge(R59:51 0x0 )
		AssignExpCmd R61:51 Select(tacBalance!!18:15 Apply(to_skey:bif R30:43) )
		NopCmd
		AssumeExpCmd Ge(R61:51 0x0 )
		AssignExpCmd R63:51 Select(tacBalance!!18:15 Apply(skey_basic:bif 0x5) )
		NopCmd
		AssumeExpCmd Ge(R63:51 0x0 )
		AssignExpCmd R65:51 Select(tacBalance!!18:15 Apply(skey_basic:bif 0x6) )
		NopCmd
		AssumeExpCmd Ge(R65:51 0x0 )
		AssignExpCmd R67:51 Select(tacBalance!!18:15 Apply(skey_basic:bif 0x7) )
		NopCmd
		AssumeExpCmd Ge(R67:51 0x0 )
		AssignExpCmd R69:51 Select(tacBalance!!18:15 Apply(skey_basic:bif 0x8) )
		NopCmd
		AssumeExpCmd Ge(R69:51 0x0 )
		AssignExpCmd R71:51 Select(tacBalance!!18:15 Apply(skey_basic:bif 0xf4) )
		NopCmd
		AssumeExpCmd Ge(R71:51 0x0 )
		AssignExpCmd R73:51 Select(tacBalance!!18:15 Apply(skey_basic:bif 0xf5) )
		NopCmd
		AssumeExpCmd Ge(R73:51 0x0 )
		AssignExpCmd R75:51 Select(tacBalance!!18:15 Apply(skey_basic:bif 0xf6) )
		NopCmd
		AssumeExpCmd Ge(R75:51 0x0 )
		AssignExpCmd R77:51 Select(tacBalance!!18:15 Apply(skey_basic:bif 0xf7) )
		NopCmd
		AssumeExpCmd Ge(R77:51 0x0 )
		AssignExpCmd R79:51 Select(tacBalance!!18:15 Apply(skey_basic:bif 0xf8) )
		NopCmd
		AssumeExpCmd Ge(R79:51 0x0 )
		AssignExpCmd R81:51 Select(tacBalance!!18:15 Apply(skey_basic:bif 0xf9) )
		NopCmd
		AssumeExpCmd Ge(R81:51 0x0 )
		AssignExpCmd R83:51 Select(tacBalance!!18:15 Apply(skey_basic:bif 0xfa) )
		NopCmd
		AssumeExpCmd Ge(R83:51 0x0 )
		AssignExpCmd R85:51 Select(tacBalance!!18:15 Apply(skey_basic:bif 0xfb) )
		NopCmd
		AssumeExpCmd Ge(R85:51 0x0 )
		AssignExpCmd R87:51 Select(tacBalance!!18:15 Apply(skey_basic:bif 0xfc) )
		NopCmd
		AssumeExpCmd Ge(R87:51 0x0 )
		AssignExpCmd R89:51 Select(tacBalance!!18:15 Apply(skey_basic:bif 0xfd) )
		NopCmd
		AssumeExpCmd Ge(R89:51 0x0 )
		AssignExpCmd R91:51 Select(tacBalance!!18:15 Apply(skey_basic:bif 0xfe) )
		NopCmd
		AssumeExpCmd Ge(R91:51 0x0 )
		AnnotationCmd JSON{"key":{"name":"cvl.label.end","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		AnnotationCmd JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Message","s":"assumptions about static addresses"}}
		AnnotationCmd JSON{"key":{"name":"cvl.label.end","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		AnnotationCmd JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Message","s":"assumptions about uniqueness of contracts' addressses"}}
		NopCmd
		AssumeExpCmd LNot(Eq(R25:38 R26:39 ) )
		NopCmd
		AssumeExpCmd LNot(Eq(R25:38 R27:40 ) )
		NopCmd
		AssumeExpCmd LNot(Eq(R25:38 0x3 ) )
		NopCmd
		AssumeExpCmd LNot(Eq(R25:38 0x5 ) )
		NopCmd
		AssumeExpCmd LNot(Eq(R25:38 0x6 ) )
		NopCmd
		AssumeExpCmd LNot(Eq(R25:38 0x7 ) )
		NopCmd
		AssumeExpCmd LNot(Eq(R25:38 0x8 ) )
		NopCmd
		AssumeExpCmd LNot(Eq(R25:38 0xf4 ) )
		NopCmd
		AssumeExpCmd LNot(Eq(R25:38 0xf5 ) )
		NopCmd
		AssumeExpCmd LNot(Eq(R25:38 0xf6 ) )
		NopCmd
		AssumeExpCmd LNot(Eq(R25:38 0xf7 ) )
		NopCmd
		AssumeExpCmd LNot(Eq(R25:38 0xf8 ) )
		NopCmd
		AssumeExpCmd LNot(Eq(R25:38 0xf9 ) )
		NopCmd
		AssumeExpCmd LNot(Eq(R25:38 0xfa ) )
		NopCmd
		AssumeExpCmd LNot(Eq(R25:38 0xfb ) )
		NopCmd
		AssumeExpCmd LNot(Eq(R25:38 0xfc ) )
		NopCmd
		AssumeExpCmd LNot(Eq(R25:38 0xfd ) )
		NopCmd
		AssumeExpCmd LNot(Eq(R25:38 0xfe ) )
		NopCmd
		AssumeExpCmd LNot(Eq(R26:39 R27:40 ) )
		NopCmd
		AssumeExpCmd LNot(Eq(R26:39 0x3 ) )
		NopCmd
		AssumeExpCmd LNot(Eq(R26:39 0x5 ) )
		NopCmd
		AssumeExpCmd LNot(Eq(R26:39 0x6 ) )
		NopCmd
		AssumeExpCmd LNot(Eq(R26:39 0x7 ) )
		NopCmd
		AssumeExpCmd LNot(Eq(R26:39 0x8 ) )
		NopCmd
		AssumeExpCmd LNot(Eq(R26:39 0xf4 ) )
		NopCmd
		AssumeExpCmd LNot(Eq(R26:39 0xf5 ) )
		NopCmd
		AssumeExpCmd LNot(Eq(R26:39 0xf6 ) )
		NopCmd
		AssumeExpCmd LNot(Eq(R26:39 0xf7 ) )
		NopCmd
		AssumeExpCmd LNot(Eq(R26:39 0xf8 ) )
		NopCmd
		AssumeExpCmd LNot(Eq(R26:39 0xf9 ) )
		NopCmd
		AssumeExpCmd LNot(Eq(R26:39 0xfa ) )
		NopCmd
		AssumeExpCmd LNot(Eq(R26:39 0xfb ) )
		NopCmd
		AssumeExpCmd LNot(Eq(R26:39 0xfc ) )
		NopCmd
		AssumeExpCmd LNot(Eq(R26:39 0xfd ) )
		NopCmd
		AssumeExpCmd LNot(Eq(R26:39 0xfe ) )
		NopCmd
		AssumeExpCmd LNot(Eq(R27:40 0x3 ) )
		NopCmd
		AssumeExpCmd LNot(Eq(R27:40 0x5 ) )
		NopCmd
		AssumeExpCmd LNot(Eq(R27:40 0x6 ) )
		NopCmd
		AssumeExpCmd LNot(Eq(R27:40 0x7 ) )
		NopCmd
		AssumeExpCmd LNot(Eq(R27:40 0x8 ) )
		NopCmd
		AssumeExpCmd LNot(Eq(R27:40 0xf4 ) )
		NopCmd
		AssumeExpCmd LNot(Eq(R27:40 0xf5 ) )
		NopCmd
		AssumeExpCmd LNot(Eq(R27:40 0xf6 ) )
		NopCmd
		AssumeExpCmd LNot(Eq(R27:40 0xf7 ) )
		NopCmd
		AssumeExpCmd LNot(Eq(R27:40 0xf8 ) )
		NopCmd
		AssumeExpCmd LNot(Eq(R27:40 0xf9 ) )
		NopCmd
		AssumeExpCmd LNot(Eq(R27:40 0xfa ) )
		NopCmd
		AssumeExpCmd LNot(Eq(R27:40 0xfb ) )
		NopCmd
		AssumeExpCmd LNot(Eq(R27:40 0xfc ) )
		NopCmd
		AssumeExpCmd LNot(Eq(R27:40 0xfd ) )
		NopCmd
		AssumeExpCmd LNot(Eq(R27:40 0xfe ) )
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
		AssumeExpCmd Eq(CANON56!!21:20 R26:39 )
		NopCmd
		AssumeExpCmd Eq(CANON57!!22:21 R25:38 )
		AnnotationCmd JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Message","s":"record starting nonces"}}
		AnnotationCmd JSON{"key":{"name":"cvl.label.end","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		AnnotationCmd JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Message","s":"cloned contracts have no balances"}}
		AnnotationCmd JSON{"key":{"name":"cvl.label.end","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		AnnotationCmd JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Message","s":"Linked immutable setup"}}
		AnnotationCmd JSON{"key":{"name":"cvl.label.end","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		AnnotationCmd JSON{"key":{"name":"cvl.label.end","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		NopCmd
		AssumeExpCmd LAnd(Le(CANON58:22 0xffffffffffffffffffffffffffffffffffffffff ) Ge(CANON58:22 0x0 ) )
		NopCmd
		AssumeExpCmd LAnd(Le(CANON59:23 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff ) Ge(CANON59:23 0x0 ) )
		NopCmd
		AssumeExpCmd LAnd(Le(CANON60:24 0xffffffffffffffffffffffffffffffffffffffff ) Ge(CANON60:24 0x0 ) )
		NopCmd
		AssumeExpCmd LAnd(Le(CANON61:25 0xffffffffffffffffffffffffffffffffffffffff ) Ge(CANON61:25 0x0 ) )
		NopCmd
		AssumeExpCmd LAnd(Le(CANON62:26 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff ) Ge(CANON62:26 0x0 ) )
		NopCmd
		AssumeExpCmd LAnd(Le(CANON63:27 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff ) Ge(CANON63:27 0x0 ) )
		NopCmd
		AssumeExpCmd LAnd(Le(CANON64:28 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff ) Ge(CANON64:28 0x0 ) )
		NopCmd
		AssumeExpCmd LAnd(Le(CANON65:29 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff ) Ge(CANON65:29 0x0 ) )
		NopCmd
		AssumeExpCmd LAnd(Le(CANON66:30 0xffffffffffffffffffffffffffffffffffffffff ) Ge(CANON66:30 0x0 ) )
		NopCmd
		AssumeExpCmd LAnd(Le(CANON67:31 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff ) Ge(CANON67:31 0x0 ) )
		NopCmd
		AssumeExpCmd LAnd(Le(CANON68:32 0xffffffffffffffffffffffffffffffffffffffff ) Ge(CANON68:32 0x0 ) )
		NopCmd
		AssumeExpCmd LAnd(Le(CANON69:33 0xffffffffffffffffffffffffffffffffffffffff ) Ge(CANON69:33 0x0 ) )
		NopCmd
		AssumeExpCmd LAnd(Le(CANON70:34 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff ) Ge(CANON70:34 0x0 ) )
		NopCmd
		AssumeExpCmd LAnd(Le(CANON71:35 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff ) Ge(CANON71:35 0x0 ) )
		NopCmd
		AssumeExpCmd LAnd(Le(CANON72:36 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff ) Ge(CANON72:36 0x0 ) )
		NopCmd
		AssumeExpCmd LAnd(Le(CANON73:37 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff ) Ge(CANON73:37 0x0 ) )
		AnnotationCmd:52 JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Cmd","cmd":{"cmd_type":"spec.cvlast.CVLCmd.Simple.AssumeCmd.Assume","cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/specs/ViewReentrancy.spec","start":{"line":25,"character":4},"end":{"line":25,"character":17}},"exp":{"#class":"spec.cvlast.CVLExp.VariableExp","id":"cond","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":0}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"},"cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/specs/ViewReentrancy.spec","start":{"line":25,"character":4},"end":{"line":25,"character":17}}},"twoStateIndex":"NEITHER"},"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":0}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}}}}}
		AssumeCmd:52 B23
		AnnotationCmd:52 JSON{"key":{"name":"cvl.label.end","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		AnnotationCmd:53 JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Cmd","cmd":{"cmd_type":"spec.cvlast.CVLCmd.Simple.AssumeCmd.Assume","cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/specs/ViewReentrancy.spec","start":{"line":26,"character":4},"end":{"line":26,"character":56}},"exp":{"#class":"spec.cvlast.CVLExp.RelopExp.EqExp","l":{"#class":"spec.cvlast.CVLExp.VariableExp","id":"before_func1","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":0}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256},"cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/specs/ViewReentrancy.spec","start":{"line":26,"character":4},"end":{"line":26,"character":56}}},"twoStateIndex":"NEITHER"},"r":{"#class":"spec.cvlast.CVLExp.ApplyExp.ContractFunction.Concrete","methodIdWithCallContext":{"#class":"spec.cvlast.ConcreteMethod","signature":{"#class":"spec.cvlast.ExternalQualifiedMethodSignature.ExternalQualifiedMethodSig","wrapped":{"#class":"spec.cvlast.QualifiedMethodSignature.QualifiedMethodSig","qualifiedMethodName":{"#class":"spec.cvlast.QualifiedFunction","host":{"name":"curve"},"methodId":"getVirtualPrice"},"params":[],"res":[{"#class":"spec.cvlast.VMParam.Unnamed","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256}}]},"sighashInt":{"n":"e25aa5fa"}}},"args":[{"#class":"spec.cvlast.CVLExp.VariableExp","id":"e_external","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":0}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"env","fields":[{"fieldName":"msg","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"msg","fields":[{"fieldName":"sender","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"value","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}}]}},{"fieldName":"tx","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"tx","fields":[{"fieldName":"origin","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}}]}},{"fieldName":"block","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"block","fields":[{"fieldName":"coinbase","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"difficulty","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"gaslimit","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"number","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"timestamp","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}}]}}]},"cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/specs/ViewReentrancy.spec","start":{"line":26,"character":4},"end":{"line":26,"character":56}}},"twoStateIndex":"NEITHER"}],"noRevert":true,"storage":{"#class":"spec.cvlast.CVLExp.VariableExp","id":"lastStorage","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":0}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.VMInternal.BlockchainState"},"cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/specs/ViewReentrancy.spec","start":{"line":26,"character":4},"end":{"line":26,"character":56}}},"twoStateIndex":"NEITHER"},"isWhole":false,"tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":0}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.VM","descriptor":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256},"context":{"#class":"spec.cvlast.typedescriptors.FromVMContext.ReturnValue"}},"cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/specs/ViewReentrancy.spec","start":{"line":26,"character":28},"end":{"line":26,"character":43}},"annotation":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.CallResolution$DirectPassing","target":{"methodSignature":{"#class":"spec.cvlast.ExternalQualifiedMethodSignature.ExternalQualifiedMethodSig","wrapped":{"#class":"spec.cvlast.QualifiedMethodSignature.QualifiedMethodSig","qualifiedMethodName":{"#class":"spec.cvlast.QualifiedFunction","host":{"name":"curve"},"methodId":"getVirtualPrice"},"params":[],"res":[{"#class":"spec.cvlast.VMParam.Unnamed","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256}}]},"sighashInt":{"n":"e25aa5fa"}},"definitelyNonPayable":true,"annotation":{"visibility":"EXTERNAL","envFree":false,"library":false},"stateMutability":"view","tag":{"#class":"spec.cvlast.CVLImportedFunctionTag.WithMethodInfo","evmMethodInfo":{"sigHash":"e25aa5fa","name":"getVirtualPrice","argTypes":[],"resultTypes":[{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256}],"stateMutability":"view","envfreeInfo":{"#class":"bridge.EnvfreeInfo.Unknown"},"isConstant":false,"isLibrary":false}}},"hasEnv":true}}},"tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":0}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"},"cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/specs/ViewReentrancy.spec","start":{"line":26,"character":12},"end":{"line":26,"character":55}}}},"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":0}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}}}}}
		NopCmd
		NopCmd
		NopCmd
		NopCmd
		NopCmd
	}
	Block 0_0_0_1_0_0 Succ [0_0_0_2_0_0] {
		AnnotationCmd:53 JSON{"key":{"name":"call.trace.push","type":"analysis.icfg.Inliner$CallStack$PushRecord","erasureStrategy":"Canonical"},"value":"rO0ABXNyACphbmFseXNpcy5pY2ZnLklubGluZXIkQ2FsbFN0YWNrJFB1c2hSZWNvcmSX8+DCTLCH+AIAA0kACGNhbGxlZUlkTAAGY2FsbGVldAATTHZjL2RhdGEvTWV0aG9kUmVmO0wAB3N1bW1hcnl0ABVMdmMvZGF0YS9DYWxsU3VtbWFyeTt4cAAAAAFzcgARdmMuZGF0YS5NZXRob2RSZWbJlJTzzU9pGAIAA0wABGF0dHJ0ABdMc2NlbmUvTWV0aG9kQXR0cmlidXRlO0wACmNvbnRyYWN0SWR0ABZMamF2YS9tYXRoL0JpZ0ludGVnZXI7TAAHc2lnSGFzaHQAEExldm0vU2lnaGFzaEludDt4cHNyABxzY2VuZS5NZXRob2RBdHRyaWJ1dGUkQ29tbW9uNHjdebdr9XMCAAB4cgAVc2NlbmUuTWV0aG9kQXR0cmlidXRlcYg2pYWutuUCAAB4cHNyABRqYXZhLm1hdGguQmlnSW50ZWdlcoz8nx+pO/sdAwAGSQAIYml0Q291bnRJAAliaXRMZW5ndGhJABNmaXJzdE5vbnplcm9CeXRlTnVtSQAMbG93ZXN0U2V0Qml0SQAGc2lnbnVtWwAJbWFnbml0dWRldAACW0J4cgAQamF2YS5sYW5nLk51bWJlcoaslR0LlOCLAgAAeHD///////////////7////+AAAAAXVyAAJbQqzzF/gGCFTgAgAAeHAAAAAQzkYEoAAAAAAAAAAAAAAAF3hzcgAOZXZtLlNpZ2hhc2hJbnRUdcqNMXEgeAIAAUwAAW5xAH4ABnhwc3EAfgAM///////////////+/////gAAAAF1cQB+ABAAAAAE4lql+nhw"}
		AssignHavocCmd:53 tacCalldatasize!!169:2
		NopCmd
		AssumeExpCmd Apply(add_noofl:bif 0x4 0x0)
		NopCmd
		AssumeExpCmd Eq(0x4 tacCalldatasize!!169:2 )
		AssignExpCmd:53 B173 LAnd(Ge(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff CANON66:30 ) Le(0x0 CANON66:30 ) )
		AssertCmd:53 B173 "sanity bounds check on cvl to vm encoding of tacTmp!4760:int failed"
		AssignExpCmd:53 R174:51 Apply(safe_math_narrow:bif CANON66:30)
		NopCmd
		AssumeExpCmd LAnd(Le(R174:54 0xffffffffffffffffffffffffffffffffffffffff ) Ge(R174:54 0x0 ) )
		AssignExpCmd:53 B178 LAnd(Ge(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff CANON67:31 ) Le(0x0 CANON67:31 ) )
		AssertCmd:53 B178 "sanity bounds check on cvl to vm encoding of tacTmp!4763:int failed"
		AssignExpCmd:53 R179:51 Apply(safe_math_narrow:bif CANON67:31)
		NopCmd
		AssumeExpCmd LAnd(Le(R179:55 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff ) Ge(R179:55 0x0 ) )
		AssignExpCmd:53 B184 LAnd(Ge(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff CANON68:32 ) Le(0x0 CANON68:32 ) )
		AssertCmd:53 B184 "sanity bounds check on cvl to vm encoding of tacTmp!4767:int failed"
		AssignExpCmd:53 R185:51 Apply(safe_math_narrow:bif CANON68:32)
		NopCmd
		AssumeExpCmd LAnd(Le(R185:56 0xffffffffffffffffffffffffffffffffffffffff ) Ge(R185:56 0x0 ) )
		AssignExpCmd:53 B189 LAnd(Ge(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff CANON72:36 ) Le(0x0 CANON72:36 ) )
		AssertCmd:53 B189 "sanity bounds check on cvl to vm encoding of tacTmp!4770:int failed"
		AssignExpCmd:53 R190:51 Apply(safe_math_narrow:bif CANON72:36)
		NopCmd
		AssumeExpCmd LAnd(Le(R190:57 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff ) Ge(R190:57 0x0 ) )
		AssignExpCmd:53 B194 LAnd(Ge(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff CANON73:37 ) Le(0x0 CANON73:37 ) )
		AssertCmd:53 B194 "sanity bounds check on cvl to vm encoding of tacTmp!4773:int failed"
		AssignExpCmd:53 R195:51 Apply(safe_math_narrow:bif CANON73:37)
		NopCmd
		AssumeExpCmd LAnd(Le(R195:58 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff ) Ge(R195:58 0x0 ) )
		AssignExpCmd:53 B199 LAnd(Ge(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff CANON67:31 ) Le(0x0 CANON67:31 ) )
		AssertCmd:53 B199 "sanity bounds check on cvl to vm encoding of tacTmp!4776:int failed"
		AssignExpCmd:53 R200:51 Apply(safe_math_narrow:bif CANON67:31)
		AssignExpCmd:53 B202 LAnd(Ge(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff CANON66:30 ) Le(0x0 CANON66:30 ) )
		AssertCmd:53 B202 "sanity bounds check on cvl to vm encoding of tacTmp!4779:int failed"
		AssignExpCmd:53 R203:51 Apply(safe_math_narrow:bif CANON66:30)
		AssignExpCmd:53 R206:51 Select(tacBalance!!18:15 Apply(to_skey:bif R203:51) )
		AssignExpCmd:59 I207:51 IntSub(R206:51 R200:51 )
		AssignExpCmd:59 tacBalance!!208:15 Store(tacBalance!!18:15 Apply(to_skey:bif R203:51) I207:51 )
		AssignExpCmd:53 R209:51 Select(tacBalance!!208:15 Apply(to_skey:bif R27:40) )
		AssignExpCmd:59 R210:51 Add(R209:51 R200:51)
		NopCmd
		AssumeExpCmd Apply(add_noofl:bif R209:51 R200:51)
		AssignExpCmd:59 tacBalance!!212:15 Store(tacBalance!!208:15 Apply(to_skey:bif R27:40) R210:51 )
		AnnotationCmd:53 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.BalanceSnippet","srcAccountInfo":{"old":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R206","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}]},"new":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"I207","tag":{"#class":"tac.Tag.Int"},"callIndex":0,"meta":[{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}]},"addr":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R203","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}]}},"trgAccountInfo":{"old":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R209","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}]},"new":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R210","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}]},"addr":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R27","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"tacContractAt"},{"key":{"name":"tac.contract.sym.addr.name","type":"java.lang.String","erasureStrategy":"Erased"},"value":"curve"},{"key":{"name":"tac.contract.sym.addr","type":"java.math.BigInteger","erasureStrategy":"Erased"},"value":"ce4604a0000000000000000000000017"}]}},"transferredAmount":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R200","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}]}}}
		LabelCmd:53 "Start procedure curve-getVirtualPrice()"
		AnnotationCmd:53 JSON{"key":{"name":"fps.free-pointer-is-scalarized","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true}
		AssignExpCmd:53 R213:51 Select(tacExtcodesize!!6:3 Apply(to_skey:bif R27:60) )
		NopCmd
		AssumeExpCmd Gt(R213:51 0x0 )
		AnnotationCmd:53 JSON{"key":{"name":"internal.func.finder.info","type":"analysis.ip.InternalFunctionFinderReport","erasureStrategy":"Erased"},"value":"rO0ABXNyAChhbmFseXNpcy5pcC5JbnRlcm5hbEZ1bmN0aW9uRmluZGVyUmVwb3J0ian+bYn1VdACAAFMABN1bnJlc29sdmVkRnVuY3Rpb25zdAAPTGphdmEvdXRpbC9TZXQ7eHBzcgAhZGF0YXN0cnVjdHVyZXMuTGlua2VkQXJyYXlIYXNoU2V0AAAAAAAAAAEDAAJGAApsb2FkRmFjdG9yTAAJaGFzaFRhYmxldAAuTGRhdGFzdHJ1Y3R1cmVzL2FycmF5aGFzaHRhYmxlL0FycmF5SGFzaFRhYmxlO3hwdwgAAAAAQAAAAHg="}
		AnnotationCmd:53 JSON{"key":{"name":"fps.free-pointer-is-scalarized","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true}
		NopCmd
		AssumeExpCmd Eq(R179:51 0x0 )
		NopCmd
		AssumeExpCmd LNot(Lt(tacCalldatasize!!169:2 0x4 ) )
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
		AnnotationCmd:53 JSON{"key":{"name":"internal.func.start","type":"analysis.ip.InternalFuncStartAnnotation","erasureStrategy":"CallTrace"},"value":{"id":0,"startPc":2909,"args":[],"methodSignature":{"#class":"spec.cvlast.QualifiedMethodSignature.QualifiedMethodSig","qualifiedMethodName":{"#class":"spec.cvlast.QualifiedFunction","host":{"name":"curve"},"methodId":"getVirtualPrice"},"params":[],"res":[{"#class":"spec.cvlast.VMParam.Unnamed","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256}}]},"stackOffsetToArgPos":{},"callSiteSrc":{"source":0,"begin":6452,"len":476,"jumpType":"ENTER","address":"ce4604a0000000000000000000000017","sourceContext":{"indexToFilepath":{"0":"contracts/curve.sol","1":"Context.sol","2":"ERC20.sol","3":"IERC20.sol","4":"IERC20Metadata.sol","5":"ReentrancyGuard.sol"},"sourceDir":".post_autofinders.1"}}}}
		AnnotationCmd:53 JSON{"key":{"name":"pta.end-allocation","type":"analysis.alloc.AllocationAnalysis$AbstractLocation","erasureStrategy":"Erased"},"value":{"prevFPWriteIdx":0,"nextFPWriteCmd":{"block":{"#class":"tac.BlockIdentifier","origStartPc":16,"stkTop":1024,"decompCopy":0,"calleeIdx":0,"topOfStackValue":2,"freshCopy":0},"pos":34},"sort":{"#class":"analysis.alloc.AllocationAnalysis.Alloc.ConstBlock","sz":"40"}}}
		AssignExpCmd:61 R225:62 Select(CANON115!!7:4 Apply(skey_basic:bif 0x8) )
		AnnotationCmd:53 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet","value":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R225","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1012}]},"displayPath":{"#class":"analysis.storage.DisplayPath.ArrayAccess","index":{"#class":"vc.data.TACSymbol.Const","value":"0"},"base":{"#class":"analysis.storage.DisplayPath.Root","name":"admin_balances"}},"storageType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256},"contractInstance":"ce4604a0000000000000000000000017","linkableStorageReadId":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet.None"}}}
		AssignExpCmd:63 R226:64 Select(tacBalance!!212:15 Apply(to_skey:bif R27:60) )
		NopCmd
		AssumeExpCmd LNot(Lt(R226:64 R225:62 ) )
		AssignExpCmd:65 R228:66 Sub(R226:64 R225:62 )
		AssignExpCmd:67 tacMCANON1!!229:9 Store(tacMCANON1!!12:9 0xc0 R228:66 )
		AssignExpCmd:68 R230:69 Select(CANON115!!7:4 Apply(skey_basic:bif 0x9) )
		AnnotationCmd:53 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet","value":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R230","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1013}]},"displayPath":{"#class":"analysis.storage.DisplayPath.ArrayAccess","index":{"#class":"vc.data.TACSymbol.Const","value":"1"},"base":{"#class":"analysis.storage.DisplayPath.Root","name":"admin_balances"}},"storageType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256},"contractInstance":"ce4604a0000000000000000000000017","linkableStorageReadId":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet.None"}}}
		AssignExpCmd:53 B232:51 Le(CANON56!!21:70 0xffffffffffffffffffffffffffffffffffffffff )
		AssignExpCmd:53 B233:51 Ge(CANON56!!21:70 0x0 )
		NopCmd
		AssumeExpCmd LAnd(B232:51 B233:51 )
		AnnotationCmd:53 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet","value":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"CANON56!!21","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.scalarization.sort","type":"vc.data.ScalarizationSort","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.ScalarizationSort.Packed","packedStart":{"#class":"vc.data.ScalarizationSort.Split","idx":"b"},"start":0}},{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.storage.bit-width","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":160},{"key":{"name":"tac.storage.pretty.paths","type":"analysis.storage.DisplayPaths","erasureStrategy":"Erased"},"value":{"paths":[{"#class":"analysis.storage.DisplayPath.Root","name":"coins_1"}]}},{"key":{"name":"tac.slot.type","type":"spec.cvlast.typedescriptors.EVMTypeDescriptor$EVMValueType","erasureStrategy":"Canonical"},"value":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.address"}},{"key":{"name":"tac.storage.non-indexed-path","type":"analysis.storage.StorageAnalysisResult$NonIndexedPath","erasureStrategy":"Canonical"},"value":{"#class":"analysis.storage.StorageAnalysisResult.NonIndexedPath.Root","slot":"b"}},{"key":{"name":"tac.storage","type":"java.math.BigInteger","erasureStrategy":"Canonical"},"value":"ce4604a0000000000000000000000017"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1011}]},"displayPath":{"#class":"analysis.storage.DisplayPath.Root","name":"coins_1"},"storageType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.address"},"contractInstance":"ce4604a0000000000000000000000017","linkableStorageReadId":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet.Id","id":0}}}
		AnnotationCmd:53 JSON{"key":{"name":"init.reorder.fence","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		AssignExpCmd:71 tacMCANON2!!236:11 Store(tacMCANON2!!14:11 0x100 0x70a0823100000000000000000000000000000000000000000000000000000000 )
		AssignExpCmd:72 tacMCANON2!!238:11 Store(tacMCANON2!!236:11 0x104 R27:40 )
		AssignExpCmd:71 R239:73 0x100
		AssignHavocCmd:71 R240:74
		AssignHavocCmd:53 tacReturndata!!241:75
		JumpCmd:53 0_0_0_2_0_0
	}
	Block 0_0_0_2_0_0 Succ [1_0_0_1_0_0] {
		AnnotationCmd:53 JSON{"key":{"name":"call.trace.push","type":"analysis.icfg.Inliner$CallStack$PushRecord","erasureStrategy":"Canonical"},"value":"rO0ABXNyACphbmFseXNpcy5pY2ZnLklubGluZXIkQ2FsbFN0YWNrJFB1c2hSZWNvcmSX8+DCTLCH+AIAA0kACGNhbGxlZUlkTAAGY2FsbGVldAATTHZjL2RhdGEvTWV0aG9kUmVmO0wAB3N1bW1hcnl0ABVMdmMvZGF0YS9DYWxsU3VtbWFyeTt4cAAAAAJzcgARdmMuZGF0YS5NZXRob2RSZWbJlJTzzU9pGAIAA0wABGF0dHJ0ABdMc2NlbmUvTWV0aG9kQXR0cmlidXRlO0wACmNvbnRyYWN0SWR0ABZMamF2YS9tYXRoL0JpZ0ludGVnZXI7TAAHc2lnSGFzaHQAEExldm0vU2lnaGFzaEludDt4cHNyABxzY2VuZS5NZXRob2RBdHRyaWJ1dGUkQ29tbW9uNHjdebdr9XMCAAB4cgAVc2NlbmUuTWV0aG9kQXR0cmlidXRlcYg2pYWutuUCAAB4cHNyABRqYXZhLm1hdGguQmlnSW50ZWdlcoz8nx+pO/sdAwAGSQAIYml0Q291bnRJAAliaXRMZW5ndGhJABNmaXJzdE5vbnplcm9CeXRlTnVtSQAMbG93ZXN0U2V0Qml0SQAGc2lnbnVtWwAJbWFnbml0dWRldAACW0J4cgAQamF2YS5sYW5nLk51bWJlcoaslR0LlOCLAgAAeHD///////////////7////+AAAAAXVyAAJbQqzzF/gGCFTgAgAAeHAAAAAQzkYEoAAAAAAAAAAAAAAABHhzcgAOZXZtLlNpZ2hhc2hJbnRUdcqNMXEgeAIAAUwAAW5xAH4ABnhwc3EAfgAM///////////////+/////gAAAAF1cQB+ABAAAAAEcKCCMXhzcgATdmMuZGF0YS5DYWxsU3VtbWFyeZQcmw5vl+FdAgAQSQAJc3VtbWFyeUlkTAAOY2FsbENvbnZlbnRpb250ACZMaW5zdHJ1bWVudGF0aW9uL2NhbGxzL0NhbGxDb252ZW50aW9uO0wACmNhbGxUYXJnZXR0ABpMYW5hbHlzaXMvaWNmZy9DYWxsVGFyZ2V0O0wACGNhbGxUeXBldAAVTHZjL2RhdGEvVEFDQ2FsbFR5cGU7TAAPY2Fubm90QmVJbmxpbmVkdAAtTGFuYWx5c2lzL2ljZmcvSW5saW5lciRJbGxlZ2FsSW5saW5pbmdSZWFzb247TAAGZ2FzVmFydAATTHZjL2RhdGEvVEFDU3ltYm9sO0wABmluQmFzZXEAfgAbTAAIaW5PZmZzZXRxAH4AG0wABmluU2l6ZXEAfgAbTAAMb3JpZ0NhbGxjb3JldAAgTHZjL2RhdGEvVEFDQ21kJFNpbXBsZSRDYWxsQ29yZTtMAAdvdXRCYXNlcQB+ABtMAAlvdXRPZmZzZXRxAH4AG0wAB291dFNpemVxAH4AG0wADXNpZ1Jlc29sdXRpb250AA9MamF2YS91dGlsL1NldDtMAAV0b1ZhcnEAfgAbTAAIdmFsdWVWYXJxAH4AG3hwAAAAAHNyACRpbnN0cnVtZW50YXRpb24uY2FsbHMuQ2FsbENvbnZlbnRpb25HtO1ulL788QIAA0kACGNhbGxlcklkTAAFaW5wdXR0ABlMYW5hbHlzaXMvaWNmZy9DYWxsSW5wdXQ7TAAGcmF3T3V0dAAiTGluc3RydW1lbnRhdGlvbi9jYWxscy9DYWxsT3V0cHV0O3hwAAAAAHNyABdhbmFseXNpcy5pY2ZnLkNhbGxJbnB1dJjJD1MhNUxQAgAHTAAHYmFzZVZhcnQAGUx2Yy9kYXRhL1RBQ0V4cHIkU3ltJFZhcjtMABBlbmNvZGVkQXJndW1lbnRzdAAjTGFuYWx5c2lzL2ljZmcvQUJJQXJndW1lbnRFbmNvZGluZztMABNpbnB1dFNpemVMb3dlckJvdW5kcQB+AAZMAAZvZmZzZXR0ABVMdmMvZGF0YS9UQUNFeHByJFN5bTtMABRyYW5nZVRvRGVjb21wb3NlZEFyZ3QAD0xqYXZhL3V0aWwvTWFwO0wAEHNpbXBsaWZpZWRPZmZzZXR0ABtMdmMvZGF0YS9UQUNFeHByJFN5bSRDb25zdDtMAARzaXplcQB+ACZ4cHNyABd2Yy5kYXRhLlRBQ0V4cHIkU3ltJFZhcskrg43eGgPnAgACTAABc3QAF0x2Yy9kYXRhL1RBQ1N5bWJvbCRWYXI7TAADdGFndAAJTHRhYy9UYWc7eHIAE3ZjLmRhdGEuVEFDRXhwciRTeW2iVj0S4YSNUAIAAHhyAA92Yy5kYXRhLlRBQ0V4cHJYhGlUu/v+yAIAAHhwc3IANnZjLmRhdGEuVEFDU3ltYm9sJFZhciRXaXRoRGVmYXVsdENhbGxJbmRleCRXaXRoQnl0ZU1hcJ7+oHF4CHAAAgACTAAEbWV0YXQALUxrb3RsaW54L2NvbGxlY3Rpb25zL2ltbXV0YWJsZS9QZXJzaXN0ZW50TWFwO0wACm5hbWVQcmVmaXh0ABJMamF2YS9sYW5nL1N0cmluZzt4cgAVdmMuZGF0YS5UQUNTeW1ib2wkVmFyCYrCGVl9SXYCAAB4cgARdmMuZGF0YS5UQUNTeW1ib2zd3Run/CoWswIAAHhwc3IAJmRhdGFzdHJ1Y3R1cmVzLnRyZWFwLkhhc2hUcmVhcE1hcCROb2Rlf2t9acJIPnQCAANMAANrZXl0ABJMamF2YS9sYW5nL09iamVjdDtMAARuZXh0dAA1TGRhdGFzdHJ1Y3R1cmVzL3RyZWFwL0hhc2hUcmVhcE1hcCRNb3JlS2V5VmFsdWVQYWlycztMAAV2YWx1ZXEAfgA3eHIAIWRhdGFzdHJ1Y3R1cmVzLnRyZWFwLkhhc2hUcmVhcE1hcPMJ/2vt3boKAgAAeHIAHWRhdGFzdHJ1Y3R1cmVzLnRyZWFwLlRyZWFwTWFw46LAyn3v5moCAAB4cgAaZGF0YXN0cnVjdHVyZXMudHJlYXAuVHJlYXA88f21zZwbdQIAAkwABGxlZnR0ABxMZGF0YXN0cnVjdHVyZXMvdHJlYXAvVHJlYXA7TAAFcmlnaHRxAH4APHhwcHNxAH4ANnBzcQB+ADZwcHNyAAt0YWMuTWV0YUtleVF/W3MiCfIZAgADTAAPZXJhc3VyZVN0cmF0ZWd5dAAdTHRhYy9NZXRhS2V5JEVyYXN1cmVTdHJhdGVneTtMAARuYW1lcQB+ADJMAAN0eXB0ABFMamF2YS9sYW5nL0NsYXNzO3hwfnIAG3RhYy5NZXRhS2V5JEVyYXN1cmVTdHJhdGVneQAAAAAAAAAAEgAAeHIADmphdmEubGFuZy5FbnVtAAAAAAAAAAASAAB4cHQACUNhbm9uaWNhbHQAF3RhYy5tZW1vcnkucGFydGl0aW9uLWlkdnIAEWphdmEubGFuZy5JbnRlZ2VyEuKgpPeBhzgCAAFJAAV2YWx1ZXhxAH4ADnBzcQB+AEkAAAACc3EAfgBAcQB+AEZ0ABJUYWMuc3ltYm9sLmtleXdvcmR2cgAQamF2YS5sYW5nLlN0cmluZ6DwpDh6O7NCAgAAeHBwdAAEdGFjTXNxAH4AQHEAfgBGdAANdGFjLmlzLm1lbW9yeXZyACJ0YWMuTWV0YU1hcCRDb21wYW5pb24kTm90aGluZ1ZhbHVl8nsHH85ykpUCAAB4cHBzcQB+AFN0AA90YWNNQ0FOT04yISEyMzhzcgAPdGFjLlRhZyRCeXRlTWFwNb/Ry6GDRgkCAAB4cgALdGFjLlRhZyRNYXABJytzDV3P/QIAAHhyAAd0YWMuVGFnLk9V3gn2xngCAAB4cHBzcQB+AAz///////////////7////+AAAAAXVxAH4AEAAAAAEkeHNxAH4AKnNyADV2Yy5kYXRhLlRBQ1N5bWJvbCRWYXIkV2l0aERlZmF1bHRDYWxsSW5kZXgkV2l0aEJpdDI1NnqsyEgq0drPAgACTAAEbWV0YXEAfgAxTAAKbmFtZVByZWZpeHEAfgAyeHEAfgAzc3EAfgA2c3EAfgA2cHBxAH4ATHB0AAFMcHNxAH4AQHEAfgBGdAAQdGFjLnN0YWNrLmhlaWdodHEAfgBKcHNxAH4ASQAAA/B0AARSMjM5c3IADnRhYy5UYWckQml0MjU2IyLQT+LlKkgCAAB4cQB+AFlzcgARamF2YS51dGlsLkhhc2hNYXAFB9rBwxZg0QMAAkYACmxvYWRGYWN0b3JJAAl0aHJlc2hvbGR4cD9AAAAAAAADdwgAAAAEAAAAAnNyAB5hbmFseXNpcy5pY2ZnLlNjcmF0Y2hCeXRlUmFuZ2XBTLaPpUzj2gIAAkwABGZyb21xAH4ABkwAAnRvcQB+AAZ4cHNxAH4ADP///////////////v////4AAAAAdXEAfgAQAAAAAHhzcQB+AAz///////////////7////+AAAAAXVxAH4AEAAAAAEDeHNyAC1hbmFseXNpcy5pY2ZnLkRlY29tcG9zZWRDYWxsSW5wdXRBcmckQ29uc3RhbnSFavLdQafqPQIAA0wAAWN0ABlMdmMvZGF0YS9UQUNTeW1ib2wkQ29uc3Q7TAARY29udHJhY3RSZWZlcmVuY2V0AC9MYW5hbHlzaXMvaWNmZy9DYWxsR3JhcGhCdWlsZGVyJENhbGxlZENvbnRyYWN0O0wADHNjcmF0Y2hSYW5nZXQAIExhbmFseXNpcy9pY2ZnL1NjcmF0Y2hCeXRlUmFuZ2U7eHIAJGFuYWx5c2lzLmljZmcuRGVjb21wb3NlZENhbGxJbnB1dEFy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aXMuc3RvcmFnZS5TdG9yYWdlQW5hbHlzaXNSZXN1bHQkTm9uSW5kZXhlZFBhdGgIwaBLofo/RQIAAHhwcHNyADphbmFseXNpcy5zdG9yYWdlLlN0b3JhZ2VBbmFseXNpc1Jlc3VsdCROb25JbmRleGVkUGF0aCRSb290vzf12KXqCv8CAAFMAARzbG90cQB+AAZ4cQB+ARVxAH4BDnNxAH4AQHEAfgBGdAANdGFjLnNsb3QudHlwZXZyADpzcGVjLmN2bGFzdC50eXBlZGVzY3JpcHRvcnMuRVZNVHlwZURlc2NyaXB0b3IkRVZNVmFsdWVUeXBlxomvArrquCUCAAB4cgAtc3BlYy5jdmxhc3QudHlwZWRlc2NyaXB0b3JzLkVWTVR5cGVEZXNjcmlwdG9yyFGp8TzCah0CAAB4cHBzcgA1c3BlYy5jdmxhc3QudHlwZWRlc2NyaXB0b3JzLkVWTVR5cGVEZXNjcmlwdG9yJGFkZHJlc3N6+GX0b5egKQIAAHhyAERzcGVjLmN2bGFzdC50eXBlZGVzY3JpcHRvcnMuRVZNVHlwZURlc2NyaXB0b3IkRVZNSXNvbW9ycGhpY1ZhbHVlVHlwZfd1mJFuEKEPAgAAeHEAfgEbc3EAfgBAcQB+AI90ABh0YWMuc3RvcmFnZS5wcmV0dHkucGF0aHN2cgAdYW5hbHlzaXMuc3RvcmFnZS5EaXNwbGF5UGF0aHP3REu3w/VRFgIAAUwABXBhdGhzcQB+AB14cHBzcQB+ASNzcgAXamF2YS51dGlsLkxpbmtlZEhhc2hTZXTYbNdald0qHgIAAHhyABFqYXZhLnV0aWwuSGFzaFNldLpEhZWWuLc0AwAAeHB3DAAAABA/QAAAAAAAAXNyACFhbmFseXNpcy5zdG9yYWdlLkRpc3BsYXlQYXRoJFJvb3TTc6C9mdA8cgIAAkwABGJhc2V0AB5MYW5hbHlzaXMvc3RvcmFnZS9EaXNwbGF5UGF0aDtMAARuYW1lcQB+ADJ4cgAcYW5hbHlzaXMuc3RvcmFnZS5EaXNwbGF5UGF0aE9AY+pW0iAFAgAAeHBwdAAHY29pbnNfMXhzcQB+AEBxAH4ARnQAFXRhYy5zdG9yYWdlLmJpdC13aWR0aHEAfgBKcHNxAH4ASQAAAKBwc3EAfgBAcQB+AEZ0AAt0YWMuc3RvcmFnZXEAfgCVcHEAfgCGcHEAfgBjcHNxAH4ASQAAA/R0AAtDQU5PTjU2ISEyMXNxAH4Ad3EAfgBocQB+AG1zcQB+ADBzcQB+ADZwc3EAfgA2cHNxAH4ANnBwcQB+AENwcQB+AEtxAH4ATHBxAH4AUHEAfgBRcHEAfgBVcQB+AFZzcQB+AF5zcQB+ADZzcQB+ADZwcHEAfgBMcHEAfgBicHEAfgBjcHEAfgCvcQB+AGZxAH4AsnNyACJqYXZhLnV0aWwuQ29sbGVjdGlvbnMkU2luZ2xldG9uU2V0LFJBmCnAsb8CAAFMAAdlbGVtZW50cQB+ADd4cHEAfgAUc3EAfgBec3EAfgA2c3EAfgA2c3EAfgA2c3EAfgA2cHNxAH4ANnBwcQB+AExwcQB+AGJxAH4BBXBxAH4BC3NxAH4ANnBzcQB+ADZwc3EAfgA2cHBxAH4BE3BxAH4BGHEAfgEZcHEAfgEgcQB+ASFwc3EAfgEjc3EAfgEmdwwAAAAQP0AAAAAAAAFxAH4BLHhxAH4BLnBxAH4BMHBxAH4BMXBxAH4AhnBxAH4AY3BxAH4BM3EAfgE0c3EAfgB3cQB+AGhxAH4AbQ=="}
		AnnotationCmd:53 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageGlobalChangeSnippet.StorageBackupPoint","calleeTxId":2}}
		NopCmd
		AssumeExpCmd LAnd(Eq(tacCalldatasize!!0:2 0x24 ) Eq(tacCalldatasize!!0:2 0x24 ) )
		NopCmd
		AssumeExpCmd Eq(tacCalldatabufCANON0@2:0 0x70a0823100000000000000000000000000000000000000000000000000000000 )
		AssignExpCmd:53 tacCalldatabufCANON1@2:76 R27:77
		LabelCmd:53 "Start procedure ERC20-balanceOf(address)"
		AnnotationCmd:53 JSON{"key":{"name":"fps.free-pointer-is-scalarized","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true}
		AssignExpCmd:53 R245:51 Select(tacExtcodesize!!6:3 Apply(to_skey:bif R26:78) )
		NopCmd
		AssumeExpCmd Gt(R245:51 0x0 )
		AnnotationCmd:53 JSON{"key":{"name":"internal.func.finder.info","type":"analysis.ip.InternalFunctionFinderReport","erasureStrategy":"Erased"},"value":"rO0ABXNyAChhbmFseXNpcy5pcC5JbnRlcm5hbEZ1bmN0aW9uRmluZGVyUmVwb3J0ian+bYn1VdACAAFMABN1bnJlc29sdmVkRnVuY3Rpb25zdAAPTGphdmEvdXRpbC9TZXQ7eHBzcgAhZGF0YXN0cnVjdHVyZXMuTGlua2VkQXJyYXlIYXNoU2V0AAAAAAAAAAEDAAJGAApsb2FkRmFjdG9yTAAJaGFzaFRhYmxldAAuTGRhdGFzdHJ1Y3R1cmVzL2FycmF5aGFzaHRhYmxlL0FycmF5SGFzaFRhYmxlO3hwdwgAAAAAQAAAAHg="}
		AnnotationCmd:53 JSON{"key":{"name":"fps.free-pointer-is-scalarized","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true}
		NopCmd
		AssumeExpCmd LNot(Lt(tacCalldatasize!!0:2 0x4 ) )
		NopCmd
		AssumeExpCmd LNot(Gt(0x39509351 tacSighash!!32:44 ) )
		NopCmd
		AssumeExpCmd LNot(Eq(0x39509351 tacSighash!!32:44 ) )
		NopCmd
		AssumeExpCmd Eq(0x70a08231 tacSighash!!32:44 )
		AssignExpCmd:79 R251:80 Sub(tacCalldatasize!!0:2 0x4 )
		AssignExpCmd:53 B252:81 Slt(R251:80 0x20 )
		NopCmd
		AssumeExpCmd LNot(B252:81 )
		AssignExpCmd:82 R254:69 tacCalldatabufCANON1@2:83
		NopCmd
		AssumeExpCmd Eq(tacCalldatabufCANON1@2:83 tacCalldatabufCANON1@2:83 )
		AnnotationCmd:53 JSON{"key":{"name":"internal.func.start","type":"analysis.ip.InternalFuncStartAnnotation","erasureStrategy":"CallTrace"},"value":{"id":1,"startPc":1712,"args":[{"s":{"namePrefix":"R254","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1013}]},"offset":1,"sort":"SCALAR"}],"methodSignature":{"#class":"spec.cvlast.QualifiedMethodSignature.QualifiedMethodSig","qualifiedMethodName":{"#class":"spec.cvlast.QualifiedFunction","host":{"name":"ERC20"},"methodId":"balanceOf"},"params":[{"#class":"spec.cvlast.VMParam.Named","name":"account","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$address"}}],"res":[{"#class":"spec.cvlast.VMParam.Unnamed","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256}}]},"stackOffsetToArgPos":{"1":0},"callSiteSrc":{"source":0,"begin":4374,"len":467,"jumpType":"ENTER","address":"ce4604a0000000000000000000000004","sourceContext":{"indexToFilepath":{"0":"contracts/ERC20.sol","1":"contracts/IERC20Metadata.sol","2":"Context.sol","3":"IERC20.sol"},"sourceDir":".post_autofinders.0"}}}}
		AssignExpCmd:84 R259:85 Apply(hash_3_keccak:bif Apply(skey_basic:bif 0x40) Apply(to_skey:bif tacCalldatabufCANON1@2:83) Apply(skey_basic:bif 0x0))
		AssignExpCmd:86 R260:85 Select(CANON130!!9:6 R259:87 )
		AnnotationCmd:53 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet","value":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R260","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1020}]},"displayPath":{"#class":"analysis.storage.DisplayPath.MapAccess","key":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R254","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1018}]},"keyTyp":{"#class":"tac.TACStorageType.IntegralType","typeLabel":"address","numBytes":"14","descriptor":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$address"},"lowerBound":null,"upperBound":null},"base":{"#class":"analysis.storage.DisplayPath.Root","name":"_balances"}},"storageType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256},"contractInstance":"ce4604a0000000000000000000000004","linkableStorageReadId":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet.None"}}}
		AnnotationCmd:53 JSON{"key":{"name":"internal.func.end","type":"analysis.ip.InternalFuncExitAnnotation","erasureStrategy":"Canonical"},"value":{"id":1,"rets":[{"s":{"namePrefix":"R260","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1023}]},"offset":0}],"functionLayout":{"0":{"#class":"analysis.ip.InternalFuncValueLocation.Scalar"}}}}
		AnnotationCmd:53 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.EVMFunctionReturnWrite","returnbufOffset":"0","returnValueSym":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R260","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1023}]},"callIndex":2}}
		AnnotationCmd:53 JSON{"key":{"name":"tac.return.path","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		LabelCmd:53 "End procedure ERC20-balanceOf(address)"
		AssignExpCmd:53 tacReturndata!!262:75 Store(tacReturndata!!241:75 0x0 R260:85 )
		AssignExpCmd:53 tacMCANON2!!263:11 Store(tacMCANON2!!238:11 0x100 R260:85 )
		AnnotationCmd:53 JSON{"key":{"name":"call.trace.pop","type":"analysis.icfg.Inliner$CallStack$PopRecord","erasureStrategy":"Canonical"},"value":"rO0ABXNyAClhbmFseXNpcy5pY2ZnLklubGluZXIkQ2FsbFN0YWNrJFBvcFJlY29yZPAPfwSLdCWJAgABSQAIY2FsbGVlSWR4cAAAAAI="}
		JumpCmd:53 1_0_0_1_0_0
	}
	Block 0_0_0_3_0_0 Succ [2_0_0_1_0_0] {
		AnnotationCmd:53 JSON{"key":{"name":"call.trace.push","type":"analysis.icfg.Inliner$CallStack$PushRecord","erasureStrategy":"Canonical"},"value":"rO0ABXNyACphbmFseXNpcy5pY2ZnLklubGluZXIkQ2FsbFN0YWNrJFB1c2hSZWNvcmSX8+DCTLCH+AIAA0kACGNhbGxlZUlkTAAGY2FsbGVldAATTHZjL2RhdGEvTWV0aG9kUmVmO0wAB3N1bW1hcnl0ABVMdmMvZGF0YS9DYWxsU3VtbWFyeTt4cAAAAANzcgARdmMuZGF0YS5NZXRob2RSZWbJlJTzzU9pGAIAA0wABGF0dHJ0ABdMc2NlbmUvTWV0aG9kQXR0cmlidXRlO0wACmNvbnRyYWN0SWR0ABZMamF2YS9tYXRoL0JpZ0ludGVnZXI7TAAHc2lnSGFzaHQAEExldm0vU2lnaGFzaEludDt4cHNyABxzY2VuZS5NZXRob2RBdHRyaWJ1dGUkQ29tbW9uNHjdebdr9XMCAAB4cgAVc2NlbmUuTWV0aG9kQXR0cmlidXRlcYg2pYWutuUCAAB4cHNyABRqYXZhLm1hdGguQmlnSW50ZWdlcoz8nx+pO/sdAwAGSQAIYml0Q291bnRJAAliaXRMZW5ndGhJABNmaXJzdE5vbnplcm9CeXRlTnVtSQAMbG93ZXN0U2V0Qml0SQAGc2lnbnVtWwAJbWFnbml0dWRldAACW0J4cgAQamF2YS5sYW5nLk51bWJlcoaslR0LlOCLAgAAeHD///////////////7////+AAAAAXVyAAJbQqzzF/gGCFTgAgAAeHAAAAAQzkYEoAAAAAAAAAAAAAAAF3hzcgAOZXZtLlNpZ2hhc2hJbnRUdcqNMXEgeAIAAUwAAW5xAH4ABnhwc3EAfgAM///////////////+/////gAAAAF1cQB+ABAAAAAEOEL3dnhzcgATdmMuZGF0YS5DYWxsU3VtbWFyeZQcmw5vl+FdAgAQSQAJc3VtbWFyeUlkTAAOY2FsbENvbnZlbnRpb250ACZMaW5zdHJ1bWVudGF0aW9uL2NhbGxzL0NhbGxDb252ZW50aW9uO0wACmNhbGxUYXJnZXR0ABpMYW5hbHlzaXMvaWNmZy9DYWxsVGFyZ2V0O0wACGNhbGxUeXBldAAVTHZjL2RhdGEvVEFDQ2FsbFR5cGU7TAAPY2Fubm90QmVJbmxpbmVkdAAtTGFuYWx5c2lzL2ljZmcvSW5saW5lciRJbGxlZ2FsSW5saW5pbmdSZWFzb247TAAGZ2FzVmFydAATTHZjL2RhdGEvVEFDU3ltYm9sO0wABmluQmFzZXEAfgAbTAAIaW5PZmZzZXRxAH4AG0wABmluU2l6ZXEAfgAbTAAMb3JpZ0NhbGxjb3JldAAgTHZjL2RhdGEvVEFDQ21kJFNpbXBsZSRDYWxsQ29yZTtMAAdvdXRCYXNlcQB+ABtMAAlvdXRPZmZzZXRxAH4AG0wAB291dFNpemVxAH4AG0wADXNpZ1Jlc29sdXRpb250AA9MamF2YS91dGlsL1NldDtMAAV0b1ZhcnEAfgAbTAAIdmFsdWVWYXJxAH4AG3hwAAAAAXNyACRpbnN0cnVtZW50YXRpb24uY2FsbHMuQ2FsbENvbnZlbnRpb25HtO1ulL788QIAA0kACGNhbGxlcklkTAAFaW5wdXR0ABlMYW5hbHlzaXMvaWNmZy9DYWxsSW5wdXQ7TAAGcmF3T3V0dAAiTGluc3RydW1lbnRhdGlvbi9jYWxscy9DYWxsT3V0cHV0O3hwAAAAAHNyABdhbmFseXNpcy5pY2ZnLkNhbGxJbnB1dJjJD1MhNUxQAgAHTAAHYmFzZVZhcnQAGUx2Yy9kYXRhL1RBQ0V4cHIkU3ltJFZhcjtMABBlbmNvZGVkQXJndW1lbnRzdAAjTGFuYWx5c2lzL2ljZmcvQUJJQXJndW1lbnRFbmNvZGluZztMABNpbnB1dFNpemVMb3dlckJvdW5kcQB+AAZMAAZvZmZzZXR0ABVMdmMvZGF0YS9UQUNFeHByJFN5bTtMABRyYW5nZVRvRGVjb21wb3NlZEFyZ3QAD0xqYXZhL3V0aWwvTWFwO0wAEHNpbXBsaWZpZWRPZmZzZXR0ABtMdmMvZGF0YS9UQUNFeHByJFN5bSRDb25zdDtMAARzaXplcQB+ACZ4cHNyABd2Yy5kYXRhLlRBQ0V4cHIkU3ltJFZhcskrg43eGgPnAgACTAABc3QAF0x2Yy9kYXRhL1RBQ1N5bWJvbCRWYXI7TAADdGFndAAJTHRhYy9UYWc7eHIAE3ZjLmRhdGEuVEFDRXhwciRTeW2iVj0S4YSNUAIAAHhyAA92Yy5kYXRhLlRBQ0V4cHJYhGlUu/v+yAIAAHhwc3IANnZjLmRhdGEuVEFDU3ltYm9sJFZhciRXaXRoRGVmYXVsdENhbGxJbmRleCRXaXRoQnl0ZU1hcJ7+oHF4CHAAAgACTAAEbWV0YXQALUxrb3RsaW54L2NvbGxlY3Rpb25zL2ltbXV0YWJsZS9QZXJzaXN0ZW50TWFwO0wACm5hbWVQcmVmaXh0ABJMamF2YS9sYW5nL1N0cmluZzt4cgAVdmMuZGF0YS5UQUNTeW1ib2wkVmFyCYrCGVl9SXYCAAB4cgARdmMuZGF0YS5UQUNTeW1ib2zd3Run/CoWswIAAHhwc3IAJmRhdGFzdHJ1Y3R1cmVzLnRyZWFwLkhhc2hUcmVhcE1hcCROb2Rlf2t9acJIPnQCAANMAANrZXl0ABJMamF2YS9sYW5nL09iamVjdDtMAARuZXh0dAA1TGRhdGFzdHJ1Y3R1cmVzL3RyZWFwL0hhc2hUcmVhcE1hcCRNb3JlS2V5VmFsdWVQYWlycztMAAV2YWx1ZXEAfgA3eHIAIWRhdGFzdHJ1Y3R1cmVzLnRyZWFwLkhhc2hUcmVhcE1hcPMJ/2vt3boKAgAAeHIAHWRhdGFzdHJ1Y3R1cmVzLnRyZWFwLlRyZWFwTWFw46LAyn3v5moCAAB4cgAaZGF0YXN0cnVjdHVyZXMudHJlYXAuVHJlYXA88f21zZwbdQIAAkwABGxlZnR0ABxMZGF0YXN0cnVjdHVyZXMvdHJlYXAvVHJlYXA7TAAFcmlnaHRxAH4APHhwcHNxAH4ANnBzcQB+ADZwcHNyAAt0YWMuTWV0YUtleVF/W3MiCfIZAgADTAAPZXJhc3VyZVN0cmF0ZWd5dAAdTHRhYy9NZXRhS2V5JEVyYXN1cmVTdHJhdGVneTtMAARuYW1lcQB+ADJMAAN0eXB0ABFMamF2YS9sYW5nL0NsYXNzO3hwfnIAG3RhYy5NZXRhS2V5JEVyYXN1cmVTdHJhdGVneQAAAAAAAAAAEgAAeHIADmphdmEubGFuZy5FbnVtAAAAAAAAAAASAAB4cHQACUNhbm9uaWNhbHQAF3RhYy5tZW1vcnkucGFydGl0aW9uLWlkdnIAEWphdmEubGFuZy5JbnRlZ2VyEuKgpPeBhzgCAAFJAAV2YWx1ZXhxAH4ADnBzcQB+AEkAAAACc3EAfgBAcQB+AEZ0ABJUYWMuc3ltYm9sLmtleXdvcmR2cgAQamF2YS5sYW5nLlN0cmluZ6DwpDh6O7NCAgAAeHBwdAAEdGFjTXNxAH4AQHEAfgBGdAANdGFjLmlzLm1lbW9yeXZyACJ0YWMuTWV0YU1hcCRDb21wYW5pb24kTm90aGluZ1ZhbHVl8nsHH85ykpUCAAB4cHBzcQB+AFN0AA90YWNNQ0FOT04yISE0NjdzcgAPdGFjLlRhZyRCeXRlTWFwNb/Ry6GDRgkCAAB4cgALdGFjLlRhZyRNYXABJytzDV3P/QIAAHhyAAd0YWMuVGFnLk9V3gn2xngCAAB4cHBzcQB+AAz///////////////7////+AAAAAXVxAH4AEAAAAAFkeHNxAH4AKnNyADV2Yy5kYXRhLlRBQ1N5bWJvbCRWYXIkV2l0aERlZmF1bHRDYWxsSW5kZXgkV2l0aEJpdDI1NnqsyEgq0drPAgACTAAEbWV0YXEAfgAxTAAKbmFtZVByZWZpeHEAfgAyeHEAfgAzc3EAfgA2c3EAfgA2cHBxAH4ATHB0AAFMcHNxAH4AQHEAfgBGdAAQdGFjLnN0YWNrLmhlaWdodHEAfgBKcHNxAH4ASQAAA/h0AARSNDY4c3IADnRhYy5UYWckQml0MjU2IyLQT+LlKkgCAAB4cQB+AFlzcgARamF2YS51dGlsLkhhc2hNYXAFB9rBwxZg0QMAAkYACmxvYWRGYWN0b3JJAAl0aHJlc2hvbGR4cD9AAAAAAAADdwgAAAAEAAAAAnNyAB5hbmFseXNpcy5pY2ZnLlNjcmF0Y2hCeXRlUmFuZ2XBTLaPpUzj2gIAAkwABGZyb21xAH4ABkwAAnRvcQB+AAZ4cHNxAH4ADP///////////////v////4AAAAAdXEAfgAQAAAAAHhzcQB+AAz///////////////7////+AAAAAXVxAH4AEAAAAAEDeHNyAC1hbmFseXNpcy5pY2ZnLkRlY29tcG9zZWRDYWxsSW5wdXRBcmckQ29uc3RhbnSFavLdQafqPQIAA0wAAWN0ABlMdmMvZGF0YS9UQUNTeW1ib2wkQ29uc3Q7TAARY29udHJhY3RSZWZlcmVuY2V0AC9MYW5hbHlzaXMvaWNmZy9DYWxsR3JhcGhCdWlsZGVyJENhbGxlZENvbnRyYWN0O0wADHNjcmF0Y2hSYW5nZXQAIExhbmFseXNpcy9pY2ZnL1NjcmF0Y2hCeXRlUmFuZ2U7eHIAJGFuYWx5c2lzLmljZmcuRGVjb21wb3NlZENhbGxJbnB1dEFyZ82Nwhnirh8hAgAAeHBzcgAXdmMuZGF0YS5UQUNTeW1ib2wkQ29uc3QmHp5/l8IUcAIAAkwAA3RhZ3EAfgAsTAAFdmFsdWVxAH4ABnhxAH4ANHEAfgBoc3EAfgAM///////////////+/////gAAAAF1cQB+ABAAAAAgOEL3dgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAB4cHEAfgBsc3EAfgBrc3EAfgAM///////////////+/////gAAAAF1cQB+ABAAAAABRHhzcQB+AAz///////////////7////+AAAAAXVxAH4AEAAAAAFjeHNyAC1hbmFseXNpcy5pY2ZnLkRlY29tcG9zZWRDYWxsSW5wdXRBcmckVmFyaWFibGWV3y80jneopQIAA0wAEWNvbnRyYWN0UmVmZXJlbmNlcQB+AHNMAAxzY3JhdGNoUmFuZ2VxAH4AdEwAAXZxAH4AK3hxAH4AdXNyADxhbmFseXNpcy5pY2ZnLkNhbGxHcmFwaEJ1aWxkZXIkQ2FsbGVkQ29udHJhY3QkVW5yZXNvbHZlZFJlYWRDhKJZ0RDzoAIAAUkADXN0b3JhZ2VSZWFkSWR4cgAtYW5hbHlzaXMuaWNmZy5DYWxsR3JhcGhCdWlsZGVyJENhbGxlZENvbnRyYWN00wt1rN/LodcCAAB4cAAAAAJxAH4Ae3NxAH4AXnNxAH4ANnNxAH4ANnBzcQB+ADZzcQB+ADZzcQB+ADZwc3EAfgA2cHBxAH4ATHBxAH4AYnNxAH4AQHEAfgBGdAAWdGFjLnNjYWxhcml6YXRpb24uc29ydHZyABl2Yy5kYXRhLlNjYWxhcml6YXRpb25Tb3J0MM5wneRoDSYCAAB4cHBzcgAfdmMuZGF0YS5TY2FsYXJpemF0aW9uU29ydCRTcGxpdFT/Wafxx7IFAgABTAADaWR4cQB+AAZ4cQB+AI5zcQB+AAz///////////////7////+AAAAAXVxAH4AEAAAAAEFeHNxAH4ANnBzcQB+ADZwc3EAfgA2cHBzcQB+AEBxAH4ARnQAHHRhYy5zdG9yYWdlLm5vbi1pbmRleGVkLXBhdGh2cgA1YW5hbHlzaXMuc3RvcmFnZS5TdG9yYWdlQW5hbHlzaXNSZXN1bHQkTm9uSW5kZXhlZFBhdGgIwaBLofo/RQIAAHhwcHNyADphbmFseXNpcy5zdG9yYWdlLlN0b3JhZ2VBbmFseXNpc1Jlc3VsdCROb25JbmRleGVkUGF0aCRSb290vzf12KXqCv8CAAFMAARzbG90cQB+AAZ4cQB+AJlxAH4AknNxAH4AQHEAfgBGdAANdGFjLnNsb3QudHlwZXZyADpzcGVjLmN2bGFzdC50eXBlZGVzY3JpcHRvcnMuRVZNVHlwZURlc2NyaXB0b3IkRVZNVmFsdWVUeXBlxomvArrquCUCAAB4cgAtc3BlYy5jdmxhc3QudHlwZWRlc2NyaXB0b3JzLkVWTVR5cGVEZXNjcmlwdG9yyFGp8TzCah0CAAB4cHBzcgAzc3BlYy5jdmxhc3QudHlwZWRlc2NyaXB0b3JzLkVWTVR5cGVEZXNjcmlwdG9yJFVJbnRL+xQfR/Nlf8ACAAFJAAhiaXR3aWR0aHhyAERzcGVjLmN2bGFzdC50eXBlZGVzY3JpcHRvcnMuRVZNVHlwZURlc2NyaXB0b3IkRVZNSXNvbW9ycGhpY1ZhbHVlVHlwZfd1mJFuEKEPAgAAeHEAfgCfAAABAHNxAH4AQH5xAH4ARHQABkVyYXNlZHQAGHRhYy5zdG9yYWdlLnByZXR0eS5wYXRoc3ZyAB1hbmFseXNpcy5zdG9yYWdlLkRpc3BsYXlQYXRoc/dES7fD9VEWAgABTAAFcGF0aHNxAH4AHXhwcHNxAH4AqXNyABdqYXZhLnV0aWwuTGlua2VkSGFzaFNldNhs11qV3SoeAgAAeHIAEWphdmEudXRpbC5IYXNoU2V0ukSFlZa4tzQDAAB4cHcMAAAAED9AAAAAAAABc3IAIWFuYWx5c2lzLnN0b3JhZ2UuRGlzcGxheVBhdGgkUm9vdNNzoL2Z0DxyAgACTAAEYmFzZXQAHkxhbmFseXNpcy9zdG9yYWdlL0Rpc3BsYXlQYXRoO0wABG5hbWVxAH4AMnhyABxhbmFseXNpcy5zdG9yYWdlLkRpc3BsYXlQYXRoT0Bj6lbSIAUCAAB4cHB0AAhmdXR1cmVfQXhzcQB+AEBxAH4ARnQAFXRhYy5zdG9yYWdlLmJpdC13aWR0aHEAfgBKcHNxAH4ASQAAAQBwc3EAfgBAcQB+AEZ0AAt0YWMuc3RvcmFnZXZxAH4ADHBxAH4AD3NxAH4AQHEAfgBGdAAYdGFjLmRlY29tcC1p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"}
		AnnotationCmd:53 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageGlobalChangeSnippet.StorageBackupPoint","calleeTxId":3}}
		NopCmd
		AssumeExpCmd LAnd(Eq(tacCalldatasize!!1:2 0x64 ) Eq(tacCalldatasize!!1:2 0x64 ) )
		AssignExpCmd:53 B266:51 Eq(Select(tacCalldatabuf!!19@3:88 0x0 ) 0x3842f77600000000000000000000000000000000000000000000000000000000 )
		AssumeCmd:53 B266:51
		AssignExpCmd:53 tacCalldatabuf!!267@3:17 LongStore(tacCalldatabuf!!19@3:88 0x4 tacMCANON2!!467:11 0x124 Sub(0x64 0x4 ) )
		LabelCmd:53 "Start procedure curve-get_D(uint256[2],uint256)"
		AnnotationCmd:53 JSON{"key":{"name":"fps.free-pointer-is-scalarized","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true}
		AssignExpCmd:53 R268:51 Select(tacExtcodesize!!6:3 Apply(to_skey:bif R27:60) )
		NopCmd
		AssumeExpCmd Gt(R268:51 0x0 )
		AnnotationCmd:53 JSON{"key":{"name":"internal.func.finder.info","type":"analysis.ip.InternalFunctionFinderReport","erasureStrategy":"Erased"},"value":"rO0ABXNyAChhbmFseXNpcy5pcC5JbnRlcm5hbEZ1bmN0aW9uRmluZGVyUmVwb3J0ian+bYn1VdACAAFMABN1bnJlc29sdmVkRnVuY3Rpb25zdAAPTGphdmEvdXRpbC9TZXQ7eHBzcgAhZGF0YXN0cnVjdHVyZXMuTGlua2VkQXJyYXlIYXNoU2V0AAAAAAAAAAEDAAJGAApsb2FkRmFjdG9yTAAJaGFzaFRhYmxldAAuTGRhdGFzdHJ1Y3R1cmVzL2FycmF5aGFzaHRhYmxlL0FycmF5SGFzaFRhYmxlO3hwdwgAAAAAQAAAAHg="}
		AnnotationCmd:53 JSON{"key":{"name":"fps.free-pointer-is-scalarized","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true}
		NopCmd
		AssumeExpCmd LNot(Lt(tacCalldatasize!!1:2 0x4 ) )
		NopCmd
		AssumeExpCmd Gt(0x82c63066 tacSighash!!33:44 )
		NopCmd
		AssumeExpCmd Eq(0x3842f776 tacSighash!!33:44 )
		AssignExpCmd:89 R274:90 Sub(tacCalldatasize!!1:2 0x4 )
		AssignExpCmd:53 B275:80 Slt(R274:90 0x60 )
		NopCmd
		AssumeExpCmd LNot(B275:80 )
		NopCmd
		AssumeExpCmd Slt(0x23 tacCalldatasize!!1:91 )
		AssignExpCmd:92 R279:93 0x80
		AssumeCmd:94 true
		AssignExpCmd:53 B280:74 Gt(0x44 tacCalldatasize!!1:91 )
		NopCmd
		AssumeExpCmd LNot(B280:74 )
		AnnotationCmd:53 JSON{"key":{"name":"dsa.assign.start","type":"java.lang.String","erasureStrategy":"Erased"},"value":"4280_1005_0_0_0_0 -> 4282_1004_0_0_0_0"}
		LabelCmd:53 "Parallel assignment for R3573:bv256, R3574:bv256 := R2326:bv256, R3653:bv256"
		AnnotationCmd:53 JSON{"key":{"name":"dsa.assign.end","type":"java.lang.String","erasureStrategy":"Erased"},"value":"4280_1005_0_0_0_0 -> 4282_1004_0_0_0_0"}
		AnnotationCmd:53 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.LoopSnippet.StartLoopSnippet","loopIndex":1,"loopSource":"unknown loop source code"}}
		AnnotationCmd:53 JSON{"key":{"name":"start_loop.cmd","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		AnnotationCmd:53 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.LoopSnippet.StartIter","iteration":1}}
		AssignExpCmd:95 R282:96 Select(tacCalldatabuf!!267@3:88 0x4 )
		AssignExpCmd:97 tacMCANON3!!283:13 Store(tacMCANON3!!16:13 0x80 R282:96 )
		AnnotationCmd:53 JSON{"key":{"name":"dsa.assign.start","type":"java.lang.String","erasureStrategy":"Erased"},"value":"4301_1002_0_0_0_0 -> 4282_1004_0_0_0_0"}
		LabelCmd:53 "Parallel assignment for R3573:bv256, R3574:bv256 := R3566:bv256, R3570:bv256"
		AnnotationCmd:53 JSON{"key":{"name":"dsa.assign.end","type":"java.lang.String","erasureStrategy":"Erased"},"value":"4301_1002_0_0_0_0 -> 4282_1004_0_0_0_0"}
		AnnotationCmd:53 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.LoopSnippet.EndIter","iteration":1}}
		AnnotationCmd:53 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.LoopSnippet.StartIter","iteration":2}}
		AssignExpCmd:95 R284:96 Select(tacCalldatabuf!!267@3:88 0x24 )
		AssignExpCmd:97 tacMCANON3!!285:13 Store(tacMCANON3!!283:13 0xa0 R284:96 )
		AnnotationCmd:53 JSON{"key":{"name":"dsa.assign.start","type":"java.lang.String","erasureStrategy":"Erased"},"value":"4301_1002_0_0_0_0 -> 4282_1004_0_0_0_0"}
		LabelCmd:53 "Parallel assignment for R3573:bv256, R3574:bv256 := R3566:bv256, R3570:bv256"
		AnnotationCmd:53 JSON{"key":{"name":"dsa.assign.end","type":"java.lang.String","erasureStrategy":"Erased"},"value":"4301_1002_0_0_0_0 -> 4282_1004_0_0_0_0"}
		AnnotationCmd:53 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.LoopSnippet.EndIter","iteration":2}}
		AnnotationCmd:53 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.LoopSnippet.EndLoopSnippet","loopId":1}}
		AnnotationCmd:53 JSON{"key":{"name":"end_loop.cmd","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		AnnotationCmd:53 JSON{"key":{"name":"pta.end-allocation","type":"analysis.alloc.AllocationAnalysis$AbstractLocation","erasureStrategy":"Erased"},"value":{"prevFPWriteIdx":0,"nextFPWriteCmd":{"block":{"#class":"tac.BlockIdentifier","origStartPc":4102,"stkTop":1000,"decompCopy":0,"calleeIdx":0,"topOfStackValue":0,"freshCopy":0},"pos":1},"sort":{"#class":"analysis.alloc.AllocationAnalysis.Alloc.ConstBlock","sz":"40"}}}
		AssignExpCmd:95 R286:62 Select(tacCalldatabuf!!267@3:88 0x44 )
		AnnotationCmd:53 JSON{"key":{"name":"internal.func.start","type":"analysis.ip.InternalFuncStartAnnotation","erasureStrategy":"CallTrace"},"value":{"id":3,"startPc":558,"args":[{"s":{"namePrefix":"R279","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1001}]},"offset":1,"sort":"SCALAR"},{"s":{"namePrefix":"R286","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1012}]},"offset":2,"sort":"SCALAR"}],"methodSignature":{"#class":"spec.cvlast.QualifiedMethodSignature.QualifiedMethodSig","qualifiedMethodName":{"#class":"spec.cvlast.QualifiedFunction","host":{"name":"curve"},"methodId":"get_D"},"params":[{"#class":"spec.cvlast.VMParam.Named","name":"xp","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$StaticArrayDescriptor","location":"memory","elementType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256},"numElements":"2"}},{"#class":"spec.cvlast.VMParam.Named","name":"amp","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256}}],"res":[{"#class":"spec.cvlast.VMParam.Unnamed","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256}}]},"stackOffsetToArgPos":{"1":0,"2":1},"callSiteSrc":{"source":0,"begin":3416,"len":1542,"jumpType":"ENTER","address":"ce4604a0000000000000000000000017","sourceContext":{"indexToFilepath":{"0":"contracts/curve.sol","1":"Context.sol","2":"ERC20.sol","3":"IERC20.sol","4":"IERC20Metadata.sol","5":"ReentrancyGuard.sol"},"sourceDir":".post_autofinders.1"}}}}
		AssignExpCmd:98 R287:80 Select(tacMCANON3!!285:13 0xa0 )
		AssignExpCmd:99 R288:90 Select(tacMCANON3!!285:13 0x80 )
		NopCmd
		AssumeExpCmd Apply(add_noofl:bif R288:90 R287:80)
		AssignExpCmd I291:51 Apply(safe_math_promotion:bif R288:90)
		AssignExpCmd I292:51 Apply(safe_math_promotion:bif R287:80)
		NopCmd
		AssignExpCmd R294:69 Apply(safe_math_narrow:bif IntAdd(I291:51 I292:51))
		AnnotationCmd:53 JSON{"key":{"name":"internal.func.end","type":"analysis.ip.InternalFuncExitAnnotation","erasureStrategy":"Canonical"},"value":{"id":3,"rets":[{"s":{"namePrefix":"R294","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1023}]},"offset":0}],"functionLayout":{"0":{"#class":"analysis.ip.InternalFuncValueLocation.Scalar"}}}}
		AnnotationCmd:53 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.EVMFunctionReturnWrite","returnbufOffset":"0","returnValueSym":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R294","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1023}]},"callIndex":3}}
		AnnotationCmd:53 JSON{"key":{"name":"tac.return.path","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		LabelCmd:53 "End procedure curve-get_D(uint256[2],uint256)"
		AssignExpCmd:53 tacReturndata!!296:75 Store(tacReturndata!!471:75 0x0 R294:69 )
		AssignExpCmd:53 tacMCANON2!!297:11 Store(tacMCANON2!!467:11 0x120 R294:69 )
		AnnotationCmd:53 JSON{"key":{"name":"call.trace.pop","type":"analysis.icfg.Inliner$CallStack$PopRecord","erasureStrategy":"Canonical"},"value":"rO0ABXNyAClhbmFseXNpcy5pY2ZnLklubGluZXIkQ2FsbFN0YWNrJFBvcFJlY29yZPAPfwSLdCWJAgABSQAIY2FsbGVlSWR4cAAAAAM="}
		JumpCmd:53 2_0_0_1_0_0
	}
	Block 0_0_0_4_0_0 Succ [3_0_0_1_0_0] {
		AnnotationCmd:53 JSON{"key":{"name":"call.trace.push","type":"analysis.icfg.Inliner$CallStack$PushRecord","erasureStrategy":"Canonical"},"value":"rO0ABXNyACphbmFseXNpcy5pY2ZnLklubGluZXIkQ2FsbFN0YWNrJFB1c2hSZWNvcmSX8+DCTLCH+AIAA0kACGNhbGxlZUlkTAAGY2FsbGVldAATTHZjL2RhdGEvTWV0aG9kUmVmO0wAB3N1bW1hcnl0ABVMdmMvZGF0YS9DYWxsU3VtbWFyeTt4cAAAAARzcgARdmMuZGF0YS5NZXRob2RSZWbJlJTzzU9pGAIAA0wABGF0dHJ0ABdMc2NlbmUvTWV0aG9kQXR0cmlidXRlO0wACmNvbnRyYWN0SWR0ABZMamF2YS9tYXRoL0JpZ0ludGVnZXI7TAAHc2lnSGFzaHQAEExldm0vU2lnaGFzaEludDt4cHNyABxzY2VuZS5NZXRob2RBdHRyaWJ1dGUkQ29tbW9uNHjdebdr9XMCAAB4cgAVc2NlbmUuTWV0aG9kQXR0cmlidXRlcYg2pYWutuUCAAB4cHNyABRqYXZhLm1hdGguQmlnSW50ZWdlcoz8nx+pO/sdAwAGSQAIYml0Q291bnRJAAliaXRMZW5ndGhJABNmaXJzdE5vbnplcm9CeXRlTnVtSQAMbG93ZXN0U2V0Qml0SQAGc2lnbnVtWwAJbWFnbml0dWRldAACW0J4cgAQamF2YS5sYW5nLk51bWJlcoaslR0LlOCLAgAAeHD///////////////7////+AAAAAXVyAAJbQqzzF/gGCFTgAgAAeHAAAAAQzkYEoAAAAAAAAAAAAAAAFHhzcgAOZXZtLlNpZ2hhc2hJbnRUdcqNMXEgeAIAAUwAAW5xAH4ABnhwc3EAfgAM///////////////+/////gAAAAF1cQB+ABAAAAAEGBYN3XhzcgATdmMuZGF0YS5DYWxsU3VtbWFyeZQcmw5vl+FdAgAQSQAJc3VtbWFyeUlkTAAOY2FsbENvbnZlbnRpb250ACZMaW5zdHJ1bWVudGF0aW9uL2NhbGxzL0NhbGxDb252ZW50aW9uO0wACmNhbGxUYXJnZXR0ABpMYW5hbHlzaXMvaWNmZy9DYWxsVGFyZ2V0O0wACGNhbGxUeXBldAAVTHZjL2RhdGEvVEFDQ2FsbFR5cGU7TAAPY2Fubm90QmVJbmxpbmVkdAAtTGFuYWx5c2lzL2ljZmcvSW5saW5lciRJbGxlZ2FsSW5saW5pbmdSZWFzb247TAAGZ2FzVmFydAATTHZjL2RhdGEvVEFDU3ltYm9sO0wABmluQmFzZXEAfgAbTAAIaW5PZmZzZXRxAH4AG0wABmluU2l6ZXEAfgAbTAAMb3JpZ0NhbGxjb3JldAAgTHZjL2RhdGEvVEFDQ21kJFNpbXBsZSRDYWxsQ29yZTtMAAdvdXRCYXNlcQB+ABtMAAlvdXRPZmZzZXRxAH4AG0wAB291dFNpemVxAH4AG0wADXNpZ1Jlc29sdXRpb250AA9MamF2YS91dGlsL1NldDtMAAV0b1ZhcnEAfgAbTAAIdmFsdWVWYXJxAH4AG3hwAAAAAnNyACRpbnN0cnVtZW50YXRpb24uY2FsbHMuQ2FsbENvbnZlbnRpb25HtO1ulL788QIAA0kACGNhbGxlcklkTAAFaW5wdXR0ABlMYW5hbHlzaXMvaWNmZy9DYWxsSW5wdXQ7TAAGcmF3T3V0dAAiTGluc3RydW1lbnRhdGlvbi9jYWxscy9DYWxsT3V0cHV0O3hwAAAAAHNyABdhbmFseXNpcy5pY2ZnLkNhbGxJbnB1dJjJD1MhNUxQAgAHTAAHYmFzZVZhcnQAGUx2Yy9kYXRhL1RBQ0V4cHIkU3ltJFZhcjtMABBlbmNvZGVkQXJndW1lbnRzdAAjTGFuYWx5c2lzL2ljZmcvQUJJQXJndW1lbnRFbmNvZGluZztMABNpbnB1dFNpemVMb3dlckJvdW5kcQB+AAZMAAZvZmZzZXR0ABVMdmMvZGF0YS9UQUNFeHByJFN5bTtMABRyYW5nZVRvRGVjb21wb3NlZEFyZ3QAD0xqYXZhL3V0aWwvTWFwO0wAEHNpbXBsaWZpZWRPZmZzZXR0ABtMdmMvZGF0YS9UQUNFeHByJFN5bSRDb25zdDtMAARzaXplcQB+ACZ4cHNyABd2Yy5kYXRhLlRBQ0V4cHIkU3ltJFZhcskrg43eGgPnAgACTAABc3QAF0x2Yy9kYXRhL1RBQ1N5bWJvbCRWYXI7TAADdGFndAAJTHRhYy9UYWc7eHIAE3ZjLmRhdGEuVEFDRXhwciRTeW2iVj0S4YSNUAIAAHhyAA92Yy5kYXRhLlRBQ0V4cHJYhGlUu/v+yAIAAHhwc3IANnZjLmRhdGEuVEFDU3ltYm9sJFZhciRXaXRoRGVmYXVsdENhbGxJbmRleCRXaXRoQnl0ZU1hcJ7+oHF4CHAAAgACTAAEbWV0YXQALUxrb3RsaW54L2NvbGxlY3Rpb25zL2ltbXV0YWJsZS9QZXJzaXN0ZW50TWFwO0wACm5hbWVQcmVmaXh0ABJMamF2YS9sYW5nL1N0cmluZzt4cgAVdmMuZGF0YS5UQUNTeW1ib2wkVmFyCYrCGVl9SXYCAAB4cgARdmMuZGF0YS5UQUNTeW1ib2zd3Run/CoWswIAAHhwc3IAJmRhdGFzdHJ1Y3R1cmVzLnRyZWFwLkhhc2hUcmVhcE1hcCROb2Rlf2t9acJIPnQCAANMAANrZXl0ABJMamF2YS9sYW5nL09iamVjdDtMAARuZXh0dAA1TGRhdGFzdHJ1Y3R1cmVzL3RyZWFwL0hhc2hUcmVhcE1hcCRNb3JlS2V5VmFsdWVQYWlycztMAAV2YWx1ZXEAfgA3eHIAIWRhdGFzdHJ1Y3R1cmVzLnRyZWFwLkhhc2hUcmVhcE1hcPMJ/2vt3boKAgAAeHIAHWRhdGFzdHJ1Y3R1cmVzLnRyZWFwLlRyZWFwTWFw46LAyn3v5moCAAB4cgAaZGF0YXN0cnVjdHVyZXMudHJlYXAuVHJlYXA88f21zZwbdQIAAkwABGxlZnR0ABxMZGF0YXN0cnVjdHVyZXMvdHJlYXAvVHJlYXA7TAAFcmlnaHRxAH4APHhwcHNxAH4ANnBzcQB+ADZwcHNyAAt0YWMuTWV0YUtleVF/W3MiCfIZAgADTAAPZXJhc3VyZVN0cmF0ZWd5dAAdTHRhYy9NZXRhS2V5JEVyYXN1cmVTdHJhdGVneTtMAARuYW1lcQB+ADJMAAN0eXB0ABFMamF2YS9sYW5nL0NsYXNzO3hwfnIAG3RhYy5NZXRhS2V5JEVyYXN1cmVTdHJhdGVneQAAAAAAAAAAEgAAeHIADmphdmEubGFuZy5FbnVtAAAAAAAAAAASAAB4cHQACUNhbm9uaWNhbHQAF3RhYy5tZW1vcnkucGFydGl0aW9uLWlkdnIAEWphdmEubGFuZy5JbnRlZ2VyEuKgpPeBhzgCAAFJAAV2YWx1ZXhxAH4ADnBzcQB+AEkAAAACc3EAfgBAcQB+AEZ0ABJUYWMuc3ltYm9sLmtleXdvcmR2cgAQamF2YS5sYW5nLlN0cmluZ6DwpDh6O7NCAgAAeHBwdAAEdGFjTXNxAH4AQHEAfgBGdAANdGFjLmlzLm1lbW9yeXZyACJ0YWMuTWV0YU1hcCRDb21wYW5pb24kTm90aGluZ1ZhbHVl8nsHH85ykpUCAAB4cHBzcQB+AFN0AA90YWNNQ0FOT04yISE1MjVzcgAPdGFjLlRhZyRCeXRlTWFwNb/Ry6GDRgkCAAB4cgALdGFjLlRhZyRNYXABJytzDV3P/QIAAHhyAAd0YWMuVGFnLk9V3gn2xngCAAB4cHBzcQB+AAz///////////////7////+AAAAAXVxAH4AEAAAAAEEeHNxAH4AKnNyADV2Yy5kYXRhLlRBQ1N5bWJvbCRWYXIkV2l0aERlZmF1bHRDYWxsSW5kZXgkV2l0aEJpdDI1NnqsyEgq0drPAgACTAAEbWV0YXEAfgAxTAAKbmFtZVByZWZpeHEAfgAyeHEAfgAzc3EAfgA2c3EAfgA2cHBxAH4ATHB0AAFMcHNxAH4AQHEAfgBGdAAQdGFjLnN0YWNrLmhlaWdodHEAfgBKcHNxAH4ASQAAA/d0AARSNTI2c3IADnRhYy5UYWckQml0MjU2IyLQT+LlKkgCAAB4cQB+AFlzcgARamF2YS51dGlsLkhhc2hNYXAFB9rBwxZg0QMAAkYACmxvYWRGYWN0b3JJAAl0aHJlc2hvbGR4cD9AAAAAAAABdwgAAAACAAAAAXNyAB5hbmFseXNpcy5pY2ZnLlNjcmF0Y2hCeXRlUmFuZ2XBTLaPpUzj2gIAAkwABGZyb21xAH4ABkwAAnRvcQB+AAZ4cHNxAH4ADP///////////////v////4AAAAAdXEAfgAQAAAAAHhzcQB+AAz///////////////7////+AAAAAXVxAH4AEAAAAAEDeHNyAC1hbmFseXNpcy5pY2ZnLkRlY29tcG9zZWRDYWxsSW5wdXRBcmckQ29uc3RhbnSFavLdQafqPQIAA0wAAWN0ABlMdmMvZGF0YS9UQUNTeW1ib2wkQ29uc3Q7TAARY29udHJhY3RSZWZlcmVuY2V0AC9MYW5hbHlzaXMvaWNmZy9DYWxsR3JhcGhCdWlsZGVyJENhbGxlZENvbnRyYWN0O0wADHNjcmF0Y2hSYW5nZXQAIExhbmFseXNpcy9pY2ZnL1NjcmF0Y2hCeXRlUmFuZ2U7eHIAJGFuYWx5c2lzLmljZmcuRGVjb21wb3NlZENhbGxJbnB1dEFyZ82Nwhnirh8hAgAAeHBzcgAXdmMuZGF0YS5UQUNTeW1ib2wkQ29uc3QmHp5/l8IUcAIAAkwAA3RhZ3EAfgAsTAAFdmFsdWVxAH4ABnhxAH4ANHEAfgBoc3EAfgAM///////////////+/////gAAAAF1cQB+ABAAAAAgGBYN3QAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAB4cHEAfgBseHBzcQB+ACpzcgAadmMuZGF0YS5UQUNTeW1ib2wkVmFyJEZ1bGwT5j0LLgdAlQIABEkACWNhbGxJbmRleEwABG1ldGFxAH4AMUwACm5hbWVQcmVmaXhxAH4AMkwAA3RhZ3EAfgAseHEAfgAzAAAAAXNxAH4ANnNxAH4ANnBwcQB+AExwcQB+AGJwcQB+AGNwc3EAfgBJAAAD9nQACExDQU5PTjc5cQB+AGhxAH4AaHNyACBpbnN0cnVtZW50YXRpb24uY2FsbHMuQ2FsbE91dHB1dMLFmzfBvZx7AgADTAAEYmFzZXEAfgArTAAGb2Zmc2V0dAARTHZjL2RhdGEvVEFDRXhwcjtMAARzaXplcQB+AIN4cHNxAH4AMHNxAH4ANnBzcQB+ADZwc3EAfgA2cHBxAH4AQ3BxAH4AS3EAfgBMcHEAfgBQcQB+AFFwcQB+AFVxAH4AVnNxAH4AKnNxAH4AXnNxAH4ANnNxAH4ANnBwcQB+AExwcQB+AGJwcQB+AGNwc3EAfgBJAAAD93EAfgBmcQB+AGhzcgAZdmMuZGF0YS5UQUNFeHByJFN5bSRDb25zdFNIr/MyQdp2AgACTAABc3EAfgByTAADdGFncQB+ACx4cQB+AC1zcQB+AHdxAH4AaHNxAH4ADP///////////////v////4AAAABdXEAfgAQAAAAASB4cQB+AGhzcgAeYW5hbHlzaXMuaWNmZy5DYWxsVGFyZ2V0JFZhbGlkuaYZ9j2rVfoCAAFMAAZjYWxsZWVxAH4Ac3hyABhhbmFseXNpcy5pY2ZnLkNhbGxUYXJnZXRG3T0sfHY+JQIAAHhwc3IAR2FuYWx5c2lzLmljZmcuQ2FsbEdyYXBoQnVpbGRlciRDYWxsZWRDb250cmFjdCRGdWxseVJlc29sdmVkJFN0b3JhZ2VMaW5r0oEJ0tBWi9UCAAJJAA1zdG9yYWdlUmVhZElkTAAKY29udHJhY3RJZHEAfgAGeHIAO2FuYWx5c2lzLmljZmcuQ2FsbEdyYXBoQnVpbGRlciRDYWxsZWRDb250cmFjdCRGdWxseVJlc29sdmVkotnIkxMAs6QCAAB4cgAtYW5hbHlzaXMuaWNmZy5DYWxsR3JhcGhCdWlsZGVyJENhbGxlZENvbnRyYWN00wt1rN/LodcCAAB4cAAAAChxAH4AD35yABN2Yy5kYXRhLlRBQ0NhbGxUeXBlAAAAAAAAAAASAAB4cQB+AEV0AAZTVEFUSUNwc3EAfgBec3EAfgA2c3EAfgA2cHBxAH4ATHBxAH4AYnBxAH4AY3BzcQB+AEkAAAPzdAAEUjUyN3NxAH4AMHNxAH4ANnBzcQB+ADZwc3EAfgA2cHBxAH4AQ3BxAH4AS3EAfgBMcHEAfgBQcQB+AFFwcQB+AFVxAH4AVnNxAH4AXnNxAH4ANnNxAH4ANnBwcQB+AExwcQB+AGJwcQB+AGNwcQB+AGVxAH4AZnNxAH4Ad3EAfgBocQB+AFtzcgAedmMuZGF0YS5UQUNDbWQkU2ltcGxlJENhbGxDb3JloSmFRwSBZnoCAAtMAAhjYWxsVHlwZXEAfgAZTAADZ2FzcQB+ABtMAAZpbkJhc2VxAH4AK0wACGluT2Zmc2V0cQB+ABtMAAZpblNpemVxAH4AG0wABG1ldGFxAH4AMUwAB291dEJhc2VxAH4AK0wACW91dE9mZnNldHEAfgAbTAAHb3V0U2l6ZXEAfgAbTAACdG9xAH4AG0wABXZhbHVlcQB+ABt4cgAVdmMuZGF0YS5UQUNDbWQkU2ltcGxl7SbWJTEGddICAAB4cgATdmMuZGF0YS5UQUNDbWQkU3BlYxur8QD4wQO+AgAAeHIADnZjLmRhdGEuVEFDQ21kVMsPiDw5H/ACAAB4cHEAfgCbc3EAfgBec3EAfgA2c3EAfgA2cHBxAH4ATHBxAH4AYnBxAH4AY3BxAH4AoHEAfgChc3EAfgAwc3EAfgA2cHNxAH4ANnBzcQB+ADZwcHEAfgBDcHEAfgBLcQB+AExwcQB+AFBxAH4AUXBxAH4AVXEAfgBWc3EAfgBec3EAfgA2c3EAfgA2cHBxAH4ATHBxAH4AYnBxAH4AY3BxAH4AZXEAfgBmc3EAfgB8AAAAAXNxAH4ANnNxAH4ANnBwcQB+AExwcQB+AGJwcQB+AGNwcQB+AIBxAH4AgXEAfgBoc3EAfgA2cHBzcQB+AEB+cQB+AER0AAlDYWxsVHJhY2V0AAh0YWMubWV0YXZyABN2Yy5kYXRhLlRBQ01ldGFJbmZvNWBM/aVLqHECAAZJAAViZWdpbkkAA2xlbkkABnNvdXJjZUwAB2FkZHJlc3NxAH4ABkwACGp1bXBUeXBldAATTGNvbXBpbGVyL0p1bXBUeXBlO0wADXNvdXJjZUNvbnRleHR0ABhMY29tcGlsZXIvU291cmNlQ29udGV4dDt4cHBzcQB+AMEAABrAAAAAHQAAAABzcQB+AAz///////////////7////+AAAAAXVxAH4AEAAAABDORgSgAAAAAAAAAAAAAAAXeH5yABFjb21waWxlci5KdW1wVHlwZQAAAAAAAAAAEgAAeHEAfgBFdAAHUkVHVUxBUnNyABZjb21waWxlci5Tb3VyY2VDb250ZXh0jMtb6UBc2hMCAAJMAA9pbmRleFRvRmlsZXBhdGhxAH4AJ0wACXNvdXJjZURpcnEAfgAyeHBzcQB+AGk/QAAAAAAADHcIAAAAEAAAAAZzcQB+AEkAAAAAdAATY29udHJhY3RzL2N1cnZlLnNvbHNxAH4ASQAAAAF0AAtDb250ZXh0LnNvbHEAfgBLdAAJRVJDMjAuc29sc3EAfgBJAAAAA3QACklFUkMyMC5zb2xzcQB+AEkAAAAEdAASSUVSQzIwTWV0YWRhdGEuc29sc3EAfgBJAAAABXQAE1JlZW50cmFuY3lHdWFyZC5zb2x4dAATLnBvc3RfYXV0b2ZpbmRlcnMuMXNxAH4AMHNxAH4ANnBzcQB+ADZwc3EAfgA2cHBxAH4AQ3BxAH4AS3EAfgBMcHEAfgBQcQB+AFFwcQB+AFVxAH4AVnNxAH4AXnNxAH4ANnNxAH4ANnBwcQB+AExwcQB+AGJwcQB+AGNwcQB+AI1xAH4AZnEAfgCQc3EAfgBec3EAfgA2c3EAfgA2c3EAfgA2c3EAfgA2cHNxAH4ANnBwcQB+AExwcQB+AGJzcQB+AEBxAH4ARnQAFnRhYy5zY2FsYXJpemF0aW9uLnNvcnR2cgAZdmMuZGF0YS5TY2FsYXJpemF0aW9uU29ydDDOcJ3kaA0mAgAAeHBwc3IAIHZjLmRhdGEuU2NhbGFyaXphdGlvblNvcnQkUGFja2VkLkWtEpOI5PcCAAJJAAVzdGFydEwAC3BhY2tlZFN0YXJ0dAAbTHZjL2RhdGEvU2NhbGFyaXphdGlvblNvcnQ7eHEAfgDpAAAAAHNyAB92Yy5kYXRhLlNjYWxhcml6YXRpb25Tb3J0JFNwbGl0VP9Zp/HHsgUCAAFMAANpZHhxAH4ABnhxAH4A6XNxAH4ADP///////////////v////4AAAABdXEAfgAQAAAAAQx4c3EAfgA2cHNxAH4ANnBzcQB+ADZwcHNxAH4AQHEAfgBGdAAcdGFjLnN0b3JhZ2Uubm9uLWluZGV4ZWQtcGF0aHZyADVhbmFseXNpcy5zdG9yYWdlLlN0b3JhZ2VBbmFseXNpc1Jlc3VsdCROb25JbmRleGVkUGF0aAjBoEuh+j9FAgAAeHBwc3IAOmFuYWx5c2lzLnN0b3JhZ2UuU3RvcmFnZUFuYWx5c2lzUmVzdWx0JE5vbkluZGV4ZWRQYXRoJFJvb3S/N/XYpeoK/wIAAUwABHNsb3RxAH4ABnhxAH4A93EAfgDwc3EAfgBAcQB+AEZ0AA10YWMuc2xvdC50eXBldnIAOnNwZWMuY3ZsYXN0LnR5cGVkZXNjcmlwdG9ycy5FVk1UeXBlRGVzY3JpcHRvciRFVk1WYWx1ZVR5cGXGia8Cuuq4JQIAAHhyAC1zcGVjLmN2bGFzdC50eXBlZGVzY3JpcHRvcnMuRVZNVHlwZURlc2NyaXB0b3LIUanxPMJqHQIAAHhwcHNyADVzcGVjLmN2bGFzdC50eXBlZGVzY3JpcHRvcnMuRVZNVHlwZURlc2NyaXB0b3IkYWRkcmVzc3r4ZfRvl6ApAgAAeHIARHNwZWMuY3ZsYXN0LnR5cGVkZXNjcmlwdG9ycy5FVk1UeXBlRGVzY3JpcHRvciRFVk1Jc29tb3JwaGljVmFsdWVUeXBl93WYkW4QoQ8CAAB4cQB+AP1zcQB+AEB+cQB+AER0AAZFcmFzZWR0ABh0YWMuc3RvcmFnZS5wcmV0dHkucGF0aHN2cgAdYW5hbHlzaXMuc3RvcmFnZS5EaXNwbGF5UGF0aHP3REu3w/VRFgIAAUwABXBhdGhzcQB+AB14cHBzcQB+AQdzcgAXamF2YS51dGlsLkxpbmtlZEhhc2hTZXTYbNdald0qHgIAAHhyABFqYXZhLnV0aWwuSGFzaFNldLpEhZWWuLc0AwAAeHB3DAAAABA/QAAAAAAAAXNyACFhbmFseXNpcy5zdG9yYWdlLkRpc3BsYXlQYXRoJFJvb3TTc6C9mdA8cgIAAkwABGJhc2V0AB5MYW5hbHlzaXMvc3RvcmFnZS9EaXNwbGF5UGF0aDtMAARuYW1lcQB+ADJ4cgAcYW5hbHlzaXMuc3RvcmFnZS5EaXNwbGF5UGF0aE9AY+pW0iAFAgAAeHBwdAAIbHBfdG9rZW54c3EAfgBAcQB+AEZ0ABV0YWMuc3RvcmFnZS5iaXQtd2lkdGhxAH4ASnBzcQB+AEkAAACgcHNxAH4AQHEAfgBGdAALdGFjLnN0b3JhZ2V2cQB+AAxwcQB+AMZwcQB+AGNwc3EAfgBJAAAD+3QAC0NBTk9ONTchITIyc3EAfgB3cQB+AGhxAH4AbXNxAH4AMHNxAH4ANnBzcQB+ADZwc3EAfgA2cHBxAH4AQ3BxAH4AS3EAfgBMcHEAfgBQcQB+AFFwcQB+AFVxAH4AVnNxAH4AXnNxAH4ANnNxAH4ANnBwcQB+AExwcQB+AGJwcQB+AGNwcQB+AI1xAH4AZnEAfgCQc3IAImphdmEudXRpbC5Db2xsZWN0aW9ucyRTaW5nbGV0b25TZXQsUkGYKcCxvwIAAUwAB2VsZW1lbnRxAH4AN3hwcQB+ABRzcQB+AF5zcQB+ADZzcQB+ADZzcQB+ADZzcQB+ADZwc3EAfgA2cHBxAH4ATHBxAH4AYnEAfgDncHEAfgDtc3EAfgA2cHNxAH4ANnBzcQB+ADZwcHEAfgD1cHEAfgD6cQB+APtwcQB+AQJxAH4BA3BzcQB+AQdzcQB+AQp3DAAAABA/QAAAAAAAAXEAfgEQeHEAfgEScHEAfgEUcHEAfgEVcHEAfgDGcHEAfgBjcHEAfgEYcQB+ARlzcQB+AHdxAH4AaHEAfgBt"}
		AnnotationCmd:53 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageGlobalChangeSnippet.StorageBackupPoint","calleeTxId":4}}
		NopCmd
		AssumeExpCmd LAnd(Eq(tacCalldatasize!!2:2 0x4 ) Eq(tacCalldatasize!!2:2 0x4 ) )
		NopCmd
		AssumeExpCmd Eq(tacCalldatabufCANON0@4:0 0x18160ddd00000000000000000000000000000000000000000000000000000000 )
		LabelCmd:53 "Start procedure CurveTokenExample-totalSupply()"
		AnnotationCmd:53 JSON{"key":{"name":"fps.free-pointer-is-scalarized","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true}
		AssignExpCmd:53 R301:51 Select(tacExtcodesize!!6:3 Apply(to_skey:bif R25:100) )
		NopCmd
		AssumeExpCmd Gt(R301:51 0x0 )
		AnnotationCmd:53 JSON{"key":{"name":"internal.func.finder.info","type":"analysis.ip.InternalFunctionFinderReport","erasureStrategy":"Erased"},"value":"rO0ABXNyAChhbmFseXNpcy5pcC5JbnRlcm5hbEZ1bmN0aW9uRmluZGVyUmVwb3J0ian+bYn1VdACAAFMABN1bnJlc29sdmVkRnVuY3Rpb25zdAAPTGphdmEvdXRpbC9TZXQ7eHBzcgAhZGF0YXN0cnVjdHVyZXMuTGlua2VkQXJyYXlIYXNoU2V0AAAAAAAAAAEDAAJGAApsb2FkRmFjdG9yTAAJaGFzaFRhYmxldAAuTGRhdGFzdHJ1Y3R1cmVzL2FycmF5aGFzaHRhYmxlL0FycmF5SGFzaFRhYmxlO3hwdwgAAAAAQAAAAHg="}
		AnnotationCmd:53 JSON{"key":{"name":"fps.free-pointer-is-scalarized","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true}
		NopCmd
		AssumeExpCmd LNot(Lt(tacCalldatasize!!2:2 0x4 ) )
		NopCmd
		AssumeExpCmd Gt(0x40c10f19 tacSighash!!34:44 )
		NopCmd
		AssumeExpCmd LNot(Eq(0x6fdde03 tacSighash!!34:44 ) )
		NopCmd
		AssumeExpCmd LNot(Eq(0x95ea7b3 tacSighash!!34:44 ) )
		NopCmd
		AssumeExpCmd Eq(0x18160ddd tacSighash!!34:44 )
		AnnotationCmd:53 JSON{"key":{"name":"internal.func.start","type":"analysis.ip.InternalFuncStartAnnotation","erasureStrategy":"CallTrace"},"value":{"id":4,"startPc":1205,"args":[],"methodSignature":{"#class":"spec.cvlast.QualifiedMethodSignature.QualifiedMethodSig","qualifiedMethodName":{"#class":"spec.cvlast.QualifiedFunction","host":{"name":"CurveTokenExample"},"methodId":"totalSupply"},"params":[],"res":[{"#class":"spec.cvlast.VMParam.Unnamed","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256}}]},"stackOffsetToArgPos":{},"callSiteSrc":{"source":2,"begin":3952,"len":364,"jumpType":"ENTER","address":"ce4604a0000000000000000000000014","sourceContext":{"indexToFilepath":{"0":"contracts/curve.sol","1":"Context.sol","2":"ERC20.sol","3":"IERC20.sol","4":"IERC20Metadata.sol","5":"ReentrancyGuard.sol"},"sourceDir":".post_autofinders.1"}}}}
		AnnotationCmd:53 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet","value":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"CANON124!!8","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.scalarization.sort","type":"vc.data.ScalarizationSort","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.ScalarizationSort.Split","idx":"2"}},{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.storage.bit-width","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":256},{"key":{"name":"tac.storage.pretty.paths","type":"analysis.storage.DisplayPaths","erasureStrategy":"Erased"},"value":{"paths":[{"#class":"analysis.storage.DisplayPath.Root","name":"_totalSupply"}]}},{"key":{"name":"tac.slot.type","type":"spec.cvlast.typedescriptors.EVMTypeDescriptor$EVMValueType","erasureStrategy":"Canonical"},"value":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256}},{"key":{"name":"tac.storage.non-indexed-path","type":"analysis.storage.StorageAnalysisResult$NonIndexedPath","erasureStrategy":"Canonical"},"value":{"#class":"analysis.storage.StorageAnalysisResult.NonIndexedPath.Root","slot":"2"}},{"key":{"name":"tac.storage","type":"java.math.BigInteger","erasureStrategy":"Canonical"},"value":"ce4604a0000000000000000000000014"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1021}]},"displayPath":{"#class":"analysis.storage.DisplayPath.Root","name":"_totalSupply"},"storageType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256},"contractInstance":"ce4604a0000000000000000000000014","linkableStorageReadId":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet.Id","id":4}}}
		AnnotationCmd:53 JSON{"key":{"name":"internal.func.end","type":"analysis.ip.InternalFuncExitAnnotation","erasureStrategy":"Canonical"},"value":{"id":4,"rets":[{"s":{"namePrefix":"CANON124!!8","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.scalarization.sort","type":"vc.data.ScalarizationSort","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.ScalarizationSort.Split","idx":"2"}},{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.storage.bit-width","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":256},{"key":{"name":"tac.storage.pretty.paths","type":"analysis.storage.DisplayPaths","erasureStrategy":"Erased"},"value":{"paths":[{"#class":"analysis.storage.DisplayPath.Root","name":"_totalSupply"}]}},{"key":{"name":"tac.slot.type","type":"spec.cvlast.typedescriptors.EVMTypeDescriptor$EVMValueType","erasureStrategy":"Canonical"},"value":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256}},{"key":{"name":"tac.storage.non-indexed-path","type":"analysis.storage.StorageAnalysisResult$NonIndexedPath","erasureStrategy":"Canonical"},"value":{"#class":"analysis.storage.StorageAnalysisResult.NonIndexedPath.Root","slot":"2"}},{"key":{"name":"tac.storage","type":"java.math.BigInteger","erasureStrategy":"Canonical"},"value":"ce4604a0000000000000000000000014"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1023}]},"offset":0}],"functionLayout":{"0":{"#class":"analysis.ip.InternalFuncValueLocation.Scalar"}}}}
		AnnotationCmd:53 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.EVMFunctionReturnWrite","returnbufOffset":"0","returnValueSym":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"CANON124!!8","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.scalarization.sort","type":"vc.data.ScalarizationSort","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.ScalarizationSort.Split","idx":"2"}},{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.storage.bit-width","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":256},{"key":{"name":"tac.storage.pretty.paths","type":"analysis.storage.DisplayPaths","erasureStrategy":"Erased"},"value":{"paths":[{"#class":"analysis.storage.DisplayPath.Root","name":"_totalSupply"}]}},{"key":{"name":"tac.slot.type","type":"spec.cvlast.typedescriptors.EVMTypeDescriptor$EVMValueType","erasureStrategy":"Canonical"},"value":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256}},{"key":{"name":"tac.storage.non-indexed-path","type":"analysis.storage.StorageAnalysisResult$NonIndexedPath","erasureStrategy":"Canonical"},"value":{"#class":"analysis.storage.StorageAnalysisResult.NonIndexedPath.Root","slot":"2"}},{"key":{"name":"tac.storage","type":"java.math.BigInteger","erasureStrategy":"Canonical"},"value":"ce4604a0000000000000000000000014"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1023}]},"callIndex":4}}
		AnnotationCmd:53 JSON{"key":{"name":"tac.return.path","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		LabelCmd:53 "End procedure CurveTokenExample-totalSupply()"
		AssignExpCmd:53 tacReturndata!!310:75 Store(tacReturndata!!528:75 0x0 CANON124!!8:101 )
		AssignExpCmd:53 tacMCANON2!!311:11 Store(tacMCANON2!!525:11 0x140 CANON124!!8:101 )
		AnnotationCmd:53 JSON{"key":{"name":"call.trace.pop","type":"analysis.icfg.Inliner$CallStack$PopRecord","erasureStrategy":"Canonical"},"value":"rO0ABXNyAClhbmFseXNpcy5pY2ZnLklubGluZXIkQ2FsbFN0YWNrJFBvcFJlY29yZPAPfwSLdCWJAgABSQAIY2FsbGVlSWR4cAAAAAQ="}
		JumpCmd:53 3_0_0_1_0_0
	}
	Block 0_0_0_6_0_0 Succ [0_0_0_7_0_0] {
		AnnotationCmd:102 JSON{"key":{"name":"call.trace.push","type":"analysis.icfg.Inliner$CallStack$PushRecord","erasureStrategy":"Canonical"},"value":"rO0ABXNyACphbmFseXNpcy5pY2ZnLklubGluZXIkQ2FsbFN0YWNrJFB1c2hSZWNvcmSX8+DCTLCH+AIAA0kACGNhbGxlZUlkTAAGY2FsbGVldAATTHZjL2RhdGEvTWV0aG9kUmVmO0wAB3N1bW1hcnl0ABVMdmMvZGF0YS9DYWxsU3VtbWFyeTt4cAAAAAZzcgARdmMuZGF0YS5NZXRob2RSZWbJlJTzzU9pGAIAA0wABGF0dHJ0ABdMc2NlbmUvTWV0aG9kQXR0cmlidXRlO0wACmNvbnRyYWN0SWR0ABZMamF2YS9tYXRoL0JpZ0ludGVnZXI7TAAHc2lnSGFzaHQAEExldm0vU2lnaGFzaEludDt4cHNyABxzY2VuZS5NZXRob2RBdHRyaWJ1dGUkQ29tbW9uNHjdebdr9XMCAAB4cgAVc2NlbmUuTWV0aG9kQXR0cmlidXRlcYg2pYWutuUCAAB4cHNyABRqYXZhLm1hdGguQmlnSW50ZWdlcoz8nx+pO/sdAwAGSQAIYml0Q291bnRJAAliaXRMZW5ndGhJABNmaXJzdE5vbnplcm9CeXRlTnVtSQAMbG93ZXN0U2V0Qml0SQAGc2lnbnVtWwAJbWFnbml0dWRldAACW0J4cgAQamF2YS5sYW5nLk51bWJlcoaslR0LlOCLAgAAeHD///////////////7////+AAAAAXVyAAJbQqzzF/gGCFTgAgAAeHAAAAAQzkYEoAAAAAAAAAAAAAAAF3hzcgAOZXZtLlNpZ2hhc2hJbnRUdcqNMXEgeAIAAUwAAW5xAH4ABnhwc3EAfgAM///////////////+/////gAAAAF1cQB+ABAAAAAE4lql+nhw"}
		AssignHavocCmd:102 tacCalldatasize!!312:2
		NopCmd
		AssumeExpCmd Apply(add_noofl:bif 0x4 0x0)
		NopCmd
		AssumeExpCmd Eq(0x4 tacCalldatasize!!312:2 )
		AssignExpCmd:102 B316 LAnd(Ge(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff CANON66:30 ) Le(0x0 CANON66:30 ) )
		AssertCmd:102 B316 "sanity bounds check on cvl to vm encoding of tacTmp!5085:int failed"
		AssignExpCmd:102 R317:51 Apply(safe_math_narrow:bif CANON66:30)
		NopCmd
		AssumeExpCmd LAnd(Le(R317:54 0xffffffffffffffffffffffffffffffffffffffff ) Ge(R317:54 0x0 ) )
		AssignExpCmd:102 B321 LAnd(Ge(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff CANON67:31 ) Le(0x0 CANON67:31 ) )
		AssertCmd:102 B321 "sanity bounds check on cvl to vm encoding of tacTmp!5088:int failed"
		AssignExpCmd:102 R322:51 Apply(safe_math_narrow:bif CANON67:31)
		NopCmd
		AssumeExpCmd LAnd(Le(R322:55 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff ) Ge(R322:55 0x0 ) )
		AssignExpCmd:102 B327 LAnd(Ge(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff CANON68:32 ) Le(0x0 CANON68:32 ) )
		AssertCmd:102 B327 "sanity bounds check on cvl to vm encoding of tacTmp!5092:int failed"
		AssignExpCmd:102 R328:51 Apply(safe_math_narrow:bif CANON68:32)
		NopCmd
		AssumeExpCmd LAnd(Le(R328:56 0xffffffffffffffffffffffffffffffffffffffff ) Ge(R328:56 0x0 ) )
		AssignExpCmd:102 B332 LAnd(Ge(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff CANON72:36 ) Le(0x0 CANON72:36 ) )
		AssertCmd:102 B332 "sanity bounds check on cvl to vm encoding of tacTmp!5095:int failed"
		AssignExpCmd:102 R333:51 Apply(safe_math_narrow:bif CANON72:36)
		NopCmd
		AssumeExpCmd LAnd(Le(R333:57 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff ) Ge(R333:57 0x0 ) )
		AssignExpCmd:102 B337 LAnd(Ge(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff CANON73:37 ) Le(0x0 CANON73:37 ) )
		AssertCmd:102 B337 "sanity bounds check on cvl to vm encoding of tacTmp!5098:int failed"
		AssignExpCmd:102 R338:51 Apply(safe_math_narrow:bif CANON73:37)
		NopCmd
		AssumeExpCmd LAnd(Le(R338:58 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff ) Ge(R338:58 0x0 ) )
		AssignExpCmd:102 B342 LAnd(Ge(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff CANON67:31 ) Le(0x0 CANON67:31 ) )
		AssertCmd:102 B342 "sanity bounds check on cvl to vm encoding of tacTmp!5101:int failed"
		AssignExpCmd:102 R343:51 Apply(safe_math_narrow:bif CANON67:31)
		AssignExpCmd:102 B345 LAnd(Ge(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff CANON66:30 ) Le(0x0 CANON66:30 ) )
		AssertCmd:102 B345 "sanity bounds check on cvl to vm encoding of tacTmp!5104:int failed"
		AssignExpCmd:102 R346:51 Apply(safe_math_narrow:bif CANON66:30)
		AssignExpCmd:102 R349:51 Select(tacBalance!!589:15 Apply(to_skey:bif R346:51) )
		AssignExpCmd:103 I350:51 IntSub(R349:51 R343:51 )
		AssignExpCmd:103 tacBalance!!351:15 Store(tacBalance!!589:15 Apply(to_skey:bif R346:51) I350:51 )
		AssignExpCmd:102 R352:51 Select(tacBalance!!351:15 Apply(to_skey:bif R27:40) )
		AssignExpCmd:103 R353:51 Add(R352:51 R343:51)
		NopCmd
		AssumeExpCmd Apply(add_noofl:bif R352:51 R343:51)
		AssignExpCmd:103 tacBalance!!355:15 Store(tacBalance!!351:15 Apply(to_skey:bif R27:40) R353:51 )
		AnnotationCmd:102 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.BalanceSnippet","srcAccountInfo":{"old":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R349","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}]},"new":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"I350","tag":{"#class":"tac.Tag.Int"},"callIndex":0,"meta":[{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}]},"addr":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R346","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}]}},"trgAccountInfo":{"old":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R352","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}]},"new":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R353","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}]},"addr":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R27","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"tacContractAt"},{"key":{"name":"tac.contract.sym.addr.name","type":"java.lang.String","erasureStrategy":"Erased"},"value":"curve"},{"key":{"name":"tac.contract.sym.addr","type":"java.math.BigInteger","erasureStrategy":"Erased"},"value":"ce4604a0000000000000000000000017"}]}},"transferredAmount":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R343","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}]}}}
		LabelCmd:102 "Start procedure curve-getVirtualPrice()"
		AnnotationCmd:102 JSON{"key":{"name":"fps.free-pointer-is-scalarized","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true}
		AssignExpCmd:102 R356:51 Select(tacExtcodesize!!6:3 Apply(to_skey:bif R27:60) )
		NopCmd
		AssumeExpCmd Gt(R356:51 0x0 )
		AnnotationCmd:102 JSON{"key":{"name":"internal.func.finder.info","type":"analysis.ip.InternalFunctionFinderReport","erasureStrategy":"Erased"},"value":"rO0ABXNyAChhbmFseXNpcy5pcC5JbnRlcm5hbEZ1bmN0aW9uRmluZGVyUmVwb3J0ian+bYn1VdACAAFMABN1bnJlc29sdmVkRnVuY3Rpb25zdAAPTGphdmEvdXRpbC9TZXQ7eHBzcgAhZGF0YXN0cnVjdHVyZXMuTGlua2VkQXJyYXlIYXNoU2V0AAAAAAAAAAEDAAJGAApsb2FkRmFjdG9yTAAJaGFzaFRhYmxldAAuTGRhdGFzdHJ1Y3R1cmVzL2FycmF5aGFzaHRhYmxlL0FycmF5SGFzaFRhYmxlO3hwdwgAAAAAQAAAAHg="}
		AnnotationCmd:102 JSON{"key":{"name":"fps.free-pointer-is-scalarized","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true}
		NopCmd
		AssumeExpCmd Eq(R322:51 0x0 )
		NopCmd
		AssumeExpCmd LNot(Lt(tacCalldatasize!!312:2 0x4 ) )
		NopCmd
		AssumeExpCmd LNot(Gt(0x82c63066 tacSighash!!36:44 ) )
		NopCmd
		AssumeExpCmd LNot(Eq(0x82c63066 tacSighash!!36:44 ) )
		NopCmd
		AssumeExpCmd LNot(Eq(0x89295a45 tacSighash!!36:44 ) )
		NopCmd
		AssumeExpCmd LNot(Eq(0x9d1e1f25 tacSighash!!36:44 ) )
		NopCmd
		AssumeExpCmd LNot(Eq(0xac8c9059 tacSighash!!36:44 ) )
		NopCmd
		AssumeExpCmd LNot(Eq(0xd802e4f7 tacSighash!!36:44 ) )
		NopCmd
		AssumeExpCmd Eq(0xe25aa5fa tacSighash!!36:44 )
		AnnotationCmd:102 JSON{"key":{"name":"internal.func.start","type":"analysis.ip.InternalFuncStartAnnotation","erasureStrategy":"CallTrace"},"value":{"id":5,"startPc":2909,"args":[],"methodSignature":{"#class":"spec.cvlast.QualifiedMethodSignature.QualifiedMethodSig","qualifiedMethodName":{"#class":"spec.cvlast.QualifiedFunction","host":{"name":"curve"},"methodId":"getVirtualPrice"},"params":[],"res":[{"#class":"spec.cvlast.VMParam.Unnamed","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256}}]},"stackOffsetToArgPos":{},"callSiteSrc":{"source":0,"begin":6452,"len":476,"jumpType":"ENTER","address":"ce4604a0000000000000000000000017","sourceContext":{"indexToFilepath":{"0":"contracts/curve.sol","1":"Context.sol","2":"ERC20.sol","3":"IERC20.sol","4":"IERC20Metadata.sol","5":"ReentrancyGuard.sol"},"sourceDir":".post_autofinders.1"}}}}
		AnnotationCmd:102 JSON{"key":{"name":"pta.end-allocation","type":"analysis.alloc.AllocationAnalysis$AbstractLocation","erasureStrategy":"Erased"},"value":{"prevFPWriteIdx":0,"nextFPWriteCmd":{"block":{"#class":"tac.BlockIdentifier","origStartPc":16,"stkTop":1024,"decompCopy":0,"calleeIdx":0,"topOfStackValue":2,"freshCopy":0},"pos":34},"sort":{"#class":"analysis.alloc.AllocationAnalysis.Alloc.ConstBlock","sz":"40"}}}
		AssignExpCmd:104 R368:62 Select(CANON115!!7:4 Apply(skey_basic:bif 0x8) )
		AnnotationCmd:102 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet","value":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R368","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1012}]},"displayPath":{"#class":"analysis.storage.DisplayPath.ArrayAccess","index":{"#class":"vc.data.TACSymbol.Const","value":"0"},"base":{"#class":"analysis.storage.DisplayPath.Root","name":"admin_balances"}},"storageType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256},"contractInstance":"ce4604a0000000000000000000000017","linkableStorageReadId":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet.None"}}}
		AssignExpCmd:105 R369:64 Select(tacBalance!!355:15 Apply(to_skey:bif R27:60) )
		NopCmd
		AssumeExpCmd LNot(Lt(R369:64 R368:62 ) )
		AssignExpCmd:106 R371:66 Sub(R369:64 R368:62 )
		AssignExpCmd:107 tacMCANON1!!372:10 Store(tacMCANON1!!13:10 0xc0 R371:66 )
		AssignExpCmd:108 R373:69 Select(CANON115!!7:4 Apply(skey_basic:bif 0x9) )
		AnnotationCmd:102 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet","value":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R373","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1013}]},"displayPath":{"#class":"analysis.storage.DisplayPath.ArrayAccess","index":{"#class":"vc.data.TACSymbol.Const","value":"1"},"base":{"#class":"analysis.storage.DisplayPath.Root","name":"admin_balances"}},"storageType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256},"contractInstance":"ce4604a0000000000000000000000017","linkableStorageReadId":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet.None"}}}
		AssignExpCmd:102 B375:51 Le(CANON56!!21:70 0xffffffffffffffffffffffffffffffffffffffff )
		AssignExpCmd:102 B376:51 Ge(CANON56!!21:70 0x0 )
		NopCmd
		AssumeExpCmd LAnd(B375:51 B376:51 )
		AnnotationCmd:102 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet","value":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"CANON56!!21","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.scalarization.sort","type":"vc.data.ScalarizationSort","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.ScalarizationSort.Packed","packedStart":{"#class":"vc.data.ScalarizationSort.Split","idx":"b"},"start":0}},{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.storage.bit-width","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":160},{"key":{"name":"tac.storage.pretty.paths","type":"analysis.storage.DisplayPaths","erasureStrategy":"Erased"},"value":{"paths":[{"#class":"analysis.storage.DisplayPath.Root","name":"coins_1"}]}},{"key":{"name":"tac.slot.type","type":"spec.cvlast.typedescriptors.EVMTypeDescriptor$EVMValueType","erasureStrategy":"Canonical"},"value":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.address"}},{"key":{"name":"tac.storage.non-indexed-path","type":"analysis.storage.StorageAnalysisResult$NonIndexedPath","erasureStrategy":"Canonical"},"value":{"#class":"analysis.storage.StorageAnalysisResult.NonIndexedPath.Root","slot":"b"}},{"key":{"name":"tac.storage","type":"java.math.BigInteger","erasureStrategy":"Canonical"},"value":"ce4604a0000000000000000000000017"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1011}]},"displayPath":{"#class":"analysis.storage.DisplayPath.Root","name":"coins_1"},"storageType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.address"},"contractInstance":"ce4604a0000000000000000000000017","linkableStorageReadId":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet.Id","id":6}}}
		AnnotationCmd:102 JSON{"key":{"name":"init.reorder.fence","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		AssignExpCmd:109 tacMCANON2!!379:12 Store(tacMCANON2!!15:12 0x100 0x70a0823100000000000000000000000000000000000000000000000000000000 )
		AssignExpCmd:110 tacMCANON2!!381:12 Store(tacMCANON2!!379:12 0x104 R27:40 )
		AssignExpCmd:109 R382:73 0x100
		AssignHavocCmd:109 R383:74
		AssignHavocCmd:102 tacReturndata!!384:75
		JumpCmd:102 0_0_0_7_0_0
	}
	Block 0_0_0_7_0_0 Succ [1_0_0_6_0_0] {
		AnnotationCmd:102 JSON{"key":{"name":"call.trace.push","type":"analysis.icfg.Inliner$CallStack$PushRecord","erasureStrategy":"Canonical"},"value":"rO0ABXNyACphbmFseXNpcy5pY2ZnLklubGluZXIkQ2FsbFN0YWNrJFB1c2hSZWNvcmSX8+DCTLCH+AIAA0kACGNhbGxlZUlkTAAGY2FsbGVldAATTHZjL2RhdGEvTWV0aG9kUmVmO0wAB3N1bW1hcnl0ABVMdmMvZGF0YS9DYWxsU3VtbWFyeTt4cAAAAAdzcgARdmMuZGF0YS5NZXRob2RSZWbJlJTzzU9pGAIAA0wABGF0dHJ0ABdMc2NlbmUvTWV0aG9kQXR0cmlidXRlO0wACmNvbnRyYWN0SWR0ABZMamF2YS9tYXRoL0JpZ0ludGVnZXI7TAAHc2lnSGFzaHQAEExldm0vU2lnaGFzaEludDt4cHNyABxzY2VuZS5NZXRob2RBdHRyaWJ1dGUkQ29tbW9uNHjdebdr9XMCAAB4cgAVc2NlbmUuTWV0aG9kQXR0cmlidXRlcYg2pYWutuUCAAB4cHNyABRqYXZhLm1hdGguQmlnSW50ZWdlcoz8nx+pO/sdAwAGSQAIYml0Q291bnRJAAliaXRMZW5ndGhJABNmaXJzdE5vbnplcm9CeXRlTnVtSQAMbG93ZXN0U2V0Qml0SQAGc2lnbnVtWwAJbWFnbml0dWRldAACW0J4cgAQamF2YS5sYW5nLk51bWJlcoaslR0LlOCLAgAAeHD///////////////7////+AAAAAXVyAAJbQqzzF/gGCFTgAgAAeHAAAAAQzkYEoAAAAAAAAAAAAAAABHhzcgAOZXZtLlNpZ2hhc2hJbnRUdcqNMXEgeAIAAUwAAW5xAH4ABnhwc3EAfgAM///////////////+/////gAAAAF1cQB+ABAAAAAEcKCCMXhzcgATdmMuZGF0YS5DYWxsU3VtbWFyeZQcmw5vl+FdAgAQSQAJc3VtbWFyeUlkTAAOY2FsbENvbnZlbnRpb250ACZMaW5zdHJ1bWVudGF0aW9uL2NhbGxzL0NhbGxDb252ZW50aW9uO0wACmNhbGxUYXJnZXR0ABpMYW5hbHlzaXMvaWNmZy9DYWxsVGFyZ2V0O0wACGNhbGxUeXBldAAVTHZjL2RhdGEvVEFDQ2FsbFR5cGU7TAAPY2Fubm90QmVJbmxpbmVkdAAtTGFuYWx5c2lzL2ljZmcvSW5saW5lciRJbGxlZ2FsSW5saW5pbmdSZWFzb247TAAGZ2FzVmFydAATTHZjL2RhdGEvVEFDU3ltYm9sO0wABmluQmFzZXEAfgAbTAAIaW5PZmZzZXRxAH4AG0wABmluU2l6ZXEAfgAbTAAMb3JpZ0NhbGxjb3JldAAgTHZjL2RhdGEvVEFDQ21kJFNpbXBsZSRDYWxsQ29yZTtMAAdvdXRCYXNlcQB+ABtMAAlvdXRPZmZzZXRxAH4AG0wAB291dFNpemVxAH4AG0wADXNpZ1Jlc29sdXRpb250AA9MamF2YS91dGlsL1NldDtMAAV0b1ZhcnEAfgAbTAAIdmFsdWVWYXJxAH4AG3hwAAAAA3NyACRpbnN0cnVtZW50YXRpb24uY2FsbHMuQ2FsbENvbnZlbnRpb25HtO1ulL788QIAA0kACGNhbGxlcklkTAAFaW5wdXR0ABlMYW5hbHlzaXMvaWNmZy9DYWxsSW5wdXQ7TAAGcmF3T3V0dAAiTGluc3RydW1lbnRhdGlvbi9jYWxscy9DYWxsT3V0cHV0O3hwAAAAAHNyABdhbmFseXNpcy5pY2ZnLkNhbGxJbnB1dJjJD1MhNUxQAgAHTAAHYmFzZVZhcnQAGUx2Yy9kYXRhL1RBQ0V4cHIkU3ltJFZhcjtMABBlbmNvZGVkQXJndW1lbnRzdAAjTGFuYWx5c2lzL2ljZmcvQUJJQXJndW1lbnRFbmNvZGluZztMABNpbnB1dFNpemVMb3dlckJvdW5kcQB+AAZMAAZvZmZzZXR0ABVMdmMvZGF0YS9UQUNFeHByJFN5bTtMABRyYW5nZVRvRGVjb21wb3NlZEFyZ3QAD0xqYXZhL3V0aWwvTWFwO0wAEHNpbXBsaWZpZWRPZmZzZXR0ABtMdmMvZGF0YS9UQUNFeHByJFN5bSRDb25zdDtMAARzaXplcQB+ACZ4cHNyABd2Yy5kYXRhLlRBQ0V4cHIkU3ltJFZhcskrg43eGgPnAgACTAABc3QAF0x2Yy9kYXRhL1RBQ1N5bWJvbCRWYXI7TAADdGFndAAJTHRhYy9UYWc7eHIAE3ZjLmRhdGEuVEFDRXhwciRTeW2iVj0S4YSNUAIAAHhyAA92Yy5kYXRhLlRBQ0V4cHJYhGlUu/v+yAIAAHhwc3IANnZjLmRhdGEuVEFDU3ltYm9sJFZhciRXaXRoRGVmYXVsdENhbGxJbmRleCRXaXRoQnl0ZU1hcJ7+oHF4CHAAAgACTAAEbWV0YXQALUxrb3RsaW54L2NvbGxlY3Rpb25zL2ltbXV0YWJsZS9QZXJzaXN0ZW50TWFwO0wACm5hbWVQcmVmaXh0ABJMamF2YS9sYW5nL1N0cmluZzt4cgAVdmMuZGF0YS5UQUNTeW1ib2wkVmFyCYrCGVl9SXYCAAB4cgARdmMuZGF0YS5UQUNTeW1ib2zd3Run/CoWswIAAHhwc3IAJmRhdGFzdHJ1Y3R1cmVzLnRyZWFwLkhhc2hUcmVhcE1hcCROb2Rlf2t9acJIPnQCAANMAANrZXl0ABJMamF2YS9sYW5nL09iamVjdDtMAARuZXh0dAA1TGRhdGFzdHJ1Y3R1cmVzL3RyZWFwL0hhc2hUcmVhcE1hcCRNb3JlS2V5VmFsdWVQYWlycztMAAV2YWx1ZXEAfgA3eHIAIWRhdGFzdHJ1Y3R1cmVzLnRyZWFwLkhhc2hUcmVhcE1hcPMJ/2vt3boKAgAAeHIAHWRhdGFzdHJ1Y3R1cmVzLnRyZWFwLlRyZWFwTWFw46LAyn3v5moCAAB4cgAaZGF0YXN0cnVjdHVyZXMudHJlYXAuVHJlYXA88f21zZwbdQIAAkwABGxlZnR0ABxMZGF0YXN0cnVjdHVyZXMvdHJlYXAvVHJlYXA7TAAFcmlnaHRxAH4APHhwcHNxAH4ANnBzcQB+ADZwcHNyAAt0YWMuTWV0YUtleVF/W3MiCfIZAgADTAAPZXJhc3VyZVN0cmF0ZWd5dAAdTHRhYy9NZXRhS2V5JEVyYXN1cmVTdHJhdGVneTtMAARuYW1lcQB+ADJMAAN0eXB0ABFMamF2YS9sYW5nL0NsYXNzO3hwfnIAG3RhYy5NZXRhS2V5JEVyYXN1cmVTdHJhdGVneQAAAAAAAAAAEgAAeHIADmphdmEubGFuZy5FbnVtAAAAAAAAAAASAAB4cHQACUNhbm9uaWNhbHQAF3RhYy5tZW1vcnkucGFydGl0aW9uLWlkdnIAEWphdmEubGFuZy5JbnRlZ2VyEuKgpPeBhzgCAAFJAAV2YWx1ZXhxAH4ADnBzcQB+AEkAAAAGc3EAfgBAcQB+AEZ0ABJUYWMuc3ltYm9sLmtleXdvcmR2cgAQamF2YS5sYW5nLlN0cmluZ6DwpDh6O7NCAgAAeHBwdAAEdGFjTXNxAH4AQHEAfgBGdAANdGFjLmlzLm1lbW9yeXZyACJ0YWMuTWV0YU1hcCRDb21wYW5pb24kTm90aGluZ1ZhbHVl8nsHH85ykpUCAAB4cHBzcQB+AFN0AA90YWNNQ0FOT04yISEzODFzcgAPdGFjLlRhZyRCeXRlTWFwNb/Ry6GDRgkCAAB4cgALdGFjLlRhZyRNYXABJytzDV3P/QIAAHhyAAd0YWMuVGFnLk9V3gn2xngCAAB4cHBzcQB+AAz///////////////7////+AAAAAXVxAH4AEAAAAAEkeHNxAH4AKnNyADV2Yy5kYXRhLlRBQ1N5bWJvbCRWYXIkV2l0aERlZmF1bHRDYWxsSW5kZXgkV2l0aEJpdDI1NnqsyEgq0drPAgACTAAEbWV0YXEAfgAxTAAKbmFtZVByZWZpeHEAfgAyeHEAfgAzc3EAfgA2c3EAfgA2cHBxAH4ATHB0AAFMcHNxAH4AQHEAfgBGdAAQdGFjLnN0YWNrLmhlaWdodHEAfgBKcHNxAH4ASQAAA/B0AARSMzgyc3IADnRhYy5UYWckQml0MjU2IyLQT+LlKkgCAAB4cQB+AFlzcgARamF2YS51dGlsLkhhc2hNYXAFB9rBwxZg0QMAAkYACmxvYWRGYWN0b3JJAAl0aHJlc2hvbGR4cD9AAAAAAAADdwgAAAAEAAAAAnNyAB5hbmFseXNpcy5pY2ZnLlNjcmF0Y2hCeXRlUmFuZ2XBTLaPpUzj2gIAAkwABGZyb21xAH4ABkwAAnRvcQB+AAZ4cHNxAH4ADP///////////////v////4AAAAAdXEAfgAQAAAAAHhzcQB+AAz///////////////7////+AAAAAXVxAH4AEAAAAAEDeHNyAC1hbmFseXNpcy5pY2ZnLkRlY29tcG9zZWRDYWxsSW5wdXRBcmckQ29uc3RhbnSFavLdQafqPQIAA0wAAWN0ABlMdmMvZGF0YS9UQUNTeW1ib2wkQ29uc3Q7TAARY29udHJhY3RSZWZlcmVuY2V0AC9MYW5hbHlzaXMvaWNmZy9DYWxsR3JhcGhCdWlsZGVyJENhbGxlZENvbnRyYWN0O0wADHNjcmF0Y2hSYW5nZXQAIExhbmFseXNpcy9pY2ZnL1NjcmF0Y2hCeXRlUmFuZ2U7eHIAJGFuYWx5c2lzLmljZmcuRGVjb21wb3NlZENhbGxJbnB1dEFy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bmFseXNpcy5zdG9yYWdlLlN0b3JhZ2VBbmFseXNpc1Jlc3VsdCROb25JbmRleGVkUGF0aAjBoEuh+j9FAgAAeHBwc3IAOmFuYWx5c2lzLnN0b3JhZ2UuU3RvcmFnZUFuYWx5c2lzUmVzdWx0JE5vbkluZGV4ZWRQYXRoJFJvb3S/N/XYpeoK/wIAAUwABHNsb3RxAH4ABnhxAH4BFnEAfgEPc3EAfgBAcQB+AEZ0AA10YWMuc2xvdC50eXBldnIAOnNwZWMuY3ZsYXN0LnR5cGVkZXNjcmlwdG9ycy5FVk1UeXBlRGVzY3JpcHRvciRFVk1WYWx1ZVR5cGXGia8Cuuq4JQIAAHhyAC1zcGVjLmN2bGFzdC50eXBlZGVzY3JpcHRvcnMuRVZNVHlwZURlc2NyaXB0b3LIUanxPMJqHQIAAHhwcHNyADVzcGVjLmN2bGFzdC50eXBlZGVzY3JpcHRvcnMuRVZNVHlwZURlc2NyaXB0b3IkYWRkcmVzc3r4ZfRvl6ApAgAAeHIARHNwZWMuY3ZsYXN0LnR5cGVkZXNjcmlwdG9ycy5FVk1UeXBlRGVzY3JpcHRvciRFVk1Jc29tb3JwaGljVmFsdWVUeXBl93WYkW4QoQ8CAAB4cQB+ARxzcQB+AEBxAH4Aj3QAGHRhYy5zdG9yYWdlLnByZXR0eS5wYXRoc3ZyAB1hbmFseXNpcy5zdG9yYWdlLkRpc3BsYXlQYXRoc/dES7fD9VEWAgABTAAFcGF0aHNxAH4AHXhwcHNxAH4BJHNyABdqYXZhLnV0aWwuTGlua2VkSGFzaFNldNhs11qV3SoeAgAAeHIAEWphdmEudXRpbC5IYXNoU2V0ukSFlZa4tzQDAAB4cHcMAAAAED9AAAAAAAABc3IAIWFuYWx5c2lzLnN0b3JhZ2UuRGlzcGxheVBhdGgkUm9vdNNzoL2Z0DxyAgACTAAEYmFzZXQAHkxhbmFseXNpcy9zdG9yYWdlL0Rpc3BsYXlQYXRoO0wABG5hbWVxAH4AMnhyABxhbmFseXNpcy5zdG9yYWdlLkRpc3BsYXlQYXRoT0Bj6lbSIAUCAAB4cHB0AAdjb2luc18xeHNxAH4AQHEAfgBGdAAVdGFjLnN0b3JhZ2UuYml0LXdpZHRocQB+AEpwc3EAfgBJAAAAoHBzcQB+AEBxAH4ARnQAC3RhYy5zdG9yYWdlcQB+AJVwcQB+AIZwcQB+AGNwc3EAfgBJAAAD9HQAC0NBTk9ONTYhITIxc3EAfgB3cQB+AGhxAH4AbXNxAH4AMHNxAH4ANnBzcQB+ADZwc3EAfgA2cHBxAH4AQ3BxAH4AS3EAfgBMcHEAfgBQcQB+AFFwcQB+AFVxAH4AVnNxAH4AXnNxAH4ANnNxAH4ANnBwcQB+AExwcQB+AGJwcQB+AGNwcQB+AK9xAH4AZnEAfgCyc3IAImphdmEudXRpbC5Db2xsZWN0aW9ucyRTaW5nbGV0b25TZXQsUkGYKcCxvwIAAUwAB2VsZW1lbnRxAH4AN3hwcQB+ABRzcQB+AF5zcQB+ADZzcQB+ADZzcQB+ADZzcQB+ADZwc3EAfgA2cHBxAH4ATHBxAH4AYnEAfgEGcHEAfgEMc3EAfgA2cHNxAH4ANnBzcQB+ADZwcHEAfgEUcHEAfgEZcQB+ARpwcQB+ASFxAH4BInBzcQB+ASRzcQB+ASd3DAAAABA/QAAAAAAAAXEAfgEteHEAfgEvcHEAfgExcHEAfgEycHEAfgCGcHEAfgBjcHEAfgE0cQB+ATVzcQB+AHdxAH4AaHEAfgBt"}
		AnnotationCmd:102 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageGlobalChangeSnippet.StorageBackupPoint","calleeTxId":7}}
		NopCmd
		AssumeExpCmd LAnd(Eq(tacCalldatasize!!3:2 0x24 ) Eq(tacCalldatasize!!3:2 0x24 ) )
		NopCmd
		AssumeExpCmd Eq(tacCalldatabufCANON0@7:1 0x70a0823100000000000000000000000000000000000000000000000000000000 )
		AssignExpCmd:102 tacCalldatabufCANON1@7:111 R27:77
		LabelCmd:102 "Start procedure ERC20-balanceOf(address)"
		AnnotationCmd:102 JSON{"key":{"name":"fps.free-pointer-is-scalarized","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true}
		AssignExpCmd:102 R388:51 Select(tacExtcodesize!!6:3 Apply(to_skey:bif R26:78) )
		NopCmd
		AssumeExpCmd Gt(R388:51 0x0 )
		AnnotationCmd:102 JSON{"key":{"name":"internal.func.finder.info","type":"analysis.ip.InternalFunctionFinderReport","erasureStrategy":"Erased"},"value":"rO0ABXNyAChhbmFseXNpcy5pcC5JbnRlcm5hbEZ1bmN0aW9uRmluZGVyUmVwb3J0ian+bYn1VdACAAFMABN1bnJlc29sdmVkRnVuY3Rpb25zdAAPTGphdmEvdXRpbC9TZXQ7eHBzcgAhZGF0YXN0cnVjdHVyZXMuTGlua2VkQXJyYXlIYXNoU2V0AAAAAAAAAAEDAAJGAApsb2FkRmFjdG9yTAAJaGFzaFRhYmxldAAuTGRhdGFzdHJ1Y3R1cmVzL2FycmF5aGFzaHRhYmxlL0FycmF5SGFzaFRhYmxlO3hwdwgAAAAAQAAAAHg="}
		AnnotationCmd:102 JSON{"key":{"name":"fps.free-pointer-is-scalarized","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true}
		NopCmd
		AssumeExpCmd LNot(Lt(tacCalldatasize!!3:2 0x4 ) )
		NopCmd
		AssumeExpCmd LNot(Gt(0x39509351 tacSighash!!37:44 ) )
		NopCmd
		AssumeExpCmd LNot(Eq(0x39509351 tacSighash!!37:44 ) )
		NopCmd
		AssumeExpCmd Eq(0x70a08231 tacSighash!!37:44 )
		AssignExpCmd:112 R394:80 Sub(tacCalldatasize!!3:2 0x4 )
		AssignExpCmd:102 B395:81 Slt(R394:80 0x20 )
		NopCmd
		AssumeExpCmd LNot(B395:81 )
		AssignExpCmd:113 R397:69 tacCalldatabufCANON1@7:114
		NopCmd
		AssumeExpCmd Eq(tacCalldatabufCANON1@7:114 tacCalldatabufCANON1@7:114 )
		AnnotationCmd:102 JSON{"key":{"name":"internal.func.start","type":"analysis.ip.InternalFuncStartAnnotation","erasureStrategy":"CallTrace"},"value":{"id":6,"startPc":1712,"args":[{"s":{"namePrefix":"R397","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1013}]},"offset":1,"sort":"SCALAR"}],"methodSignature":{"#class":"spec.cvlast.QualifiedMethodSignature.QualifiedMethodSig","qualifiedMethodName":{"#class":"spec.cvlast.QualifiedFunction","host":{"name":"ERC20"},"methodId":"balanceOf"},"params":[{"#class":"spec.cvlast.VMParam.Named","name":"account","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$address"}}],"res":[{"#class":"spec.cvlast.VMParam.Unnamed","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256}}]},"stackOffsetToArgPos":{"1":0},"callSiteSrc":{"source":0,"begin":4374,"len":467,"jumpType":"ENTER","address":"ce4604a0000000000000000000000004","sourceContext":{"indexToFilepath":{"0":"contracts/ERC20.sol","1":"contracts/IERC20Metadata.sol","2":"Context.sol","3":"IERC20.sol"},"sourceDir":".post_autofinders.0"}}}}
		AssignExpCmd:115 R402:85 Apply(hash_3_keccak:bif Apply(skey_basic:bif 0x40) Apply(to_skey:bif tacCalldatabufCANON1@7:114) Apply(skey_basic:bif 0x0))
		AssignExpCmd:116 R403:85 Select(CANON130!!9:6 R402:117 )
		AnnotationCmd:102 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet","value":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R403","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1020}]},"displayPath":{"#class":"analysis.storage.DisplayPath.MapAccess","key":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R397","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1018}]},"keyTyp":{"#class":"tac.TACStorageType.IntegralType","typeLabel":"address","numBytes":"14","descriptor":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$address"},"lowerBound":null,"upperBound":null},"base":{"#class":"analysis.storage.DisplayPath.Root","name":"_balances"}},"storageType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256},"contractInstance":"ce4604a0000000000000000000000004","linkableStorageReadId":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet.None"}}}
		AnnotationCmd:102 JSON{"key":{"name":"internal.func.end","type":"analysis.ip.InternalFuncExitAnnotation","erasureStrategy":"Canonical"},"value":{"id":6,"rets":[{"s":{"namePrefix":"R403","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1023}]},"offset":0}],"functionLayout":{"0":{"#class":"analysis.ip.InternalFuncValueLocation.Scalar"}}}}
		AnnotationCmd:102 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.EVMFunctionReturnWrite","returnbufOffset":"0","returnValueSym":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R403","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1023}]},"callIndex":7}}
		AnnotationCmd:102 JSON{"key":{"name":"tac.return.path","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		LabelCmd:102 "End procedure ERC20-balanceOf(address)"
		AssignExpCmd:102 tacReturndata!!405:75 Store(tacReturndata!!384:75 0x0 R403:85 )
		AssignExpCmd:102 tacMCANON2!!406:12 Store(tacMCANON2!!381:12 0x100 R403:85 )
		AnnotationCmd:102 JSON{"key":{"name":"call.trace.pop","type":"analysis.icfg.Inliner$CallStack$PopRecord","erasureStrategy":"Canonical"},"value":"rO0ABXNyAClhbmFseXNpcy5pY2ZnLklubGluZXIkQ2FsbFN0YWNrJFBvcFJlY29yZPAPfwSLdCWJAgABSQAIY2FsbGVlSWR4cAAAAAc="}
		JumpCmd:102 1_0_0_6_0_0
	}
	Block 0_0_0_8_0_0 Succ [2_0_0_6_0_0] {
		AnnotationCmd:102 JSON{"key":{"name":"call.trace.push","type":"analysis.icfg.Inliner$CallStack$PushRecord","erasureStrategy":"Canonical"},"value":"rO0ABXNyACphbmFseXNpcy5pY2ZnLklubGluZXIkQ2FsbFN0YWNrJFB1c2hSZWNvcmSX8+DCTLCH+AIAA0kACGNhbGxlZUlkTAAGY2FsbGVldAATTHZjL2RhdGEvTWV0aG9kUmVmO0wAB3N1bW1hcnl0ABVMdmMvZGF0YS9DYWxsU3VtbWFyeTt4cAAAAAhzcgARdmMuZGF0YS5NZXRob2RSZWbJlJTzzU9pGAIAA0wABGF0dHJ0ABdMc2NlbmUvTWV0aG9kQXR0cmlidXRlO0wACmNvbnRyYWN0SWR0ABZMamF2YS9tYXRoL0JpZ0ludGVnZXI7TAAHc2lnSGFzaHQAEExldm0vU2lnaGFzaEludDt4cHNyABxzY2VuZS5NZXRob2RBdHRyaWJ1dGUkQ29tbW9uNHjdebdr9XMCAAB4cgAVc2NlbmUuTWV0aG9kQXR0cmlidXRlcYg2pYWutuUCAAB4cHNyABRqYXZhLm1hdGguQmlnSW50ZWdlcoz8nx+pO/sdAwAGSQAIYml0Q291bnRJAAliaXRMZW5ndGhJABNmaXJzdE5vbnplcm9CeXRlTnVtSQAMbG93ZXN0U2V0Qml0SQAGc2lnbnVtWwAJbWFnbml0dWRldAACW0J4cgAQamF2YS5sYW5nLk51bWJlcoaslR0LlOCLAgAAeHD///////////////7////+AAAAAXVyAAJbQqzzF/gGCFTgAgAAeHAAAAAQzkYEoAAAAAAAAAAAAAAAF3hzcgAOZXZtLlNpZ2hhc2hJbnRUdcqNMXEgeAIAAUwAAW5xAH4ABnhwc3EAfgAM///////////////+/////gAAAAF1cQB+ABAAAAAEOEL3dnhzcgATdmMuZGF0YS5DYWxsU3VtbWFyeZQcmw5vl+FdAgAQSQAJc3VtbWFyeUlkTAAOY2FsbENvbnZlbnRpb250ACZMaW5zdHJ1bWVudGF0aW9uL2NhbGxzL0NhbGxDb252ZW50aW9uO0wACmNhbGxUYXJnZXR0ABpMYW5hbHlzaXMvaWNmZy9DYWxsVGFyZ2V0O0wACGNhbGxUeXBldAAVTHZjL2RhdGEvVEFDQ2FsbFR5cGU7TAAPY2Fubm90QmVJbmxpbmVkdAAtTGFuYWx5c2lzL2ljZmcvSW5saW5lciRJbGxlZ2FsSW5saW5pbmdSZWFzb247TAAGZ2FzVmFydAATTHZjL2RhdGEvVEFDU3ltYm9sO0wABmluQmFzZXEAfgAbTAAIaW5PZmZzZXRxAH4AG0wABmluU2l6ZXEAfgAbTAAMb3JpZ0NhbGxjb3JldAAgTHZjL2RhdGEvVEFDQ21kJFNpbXBsZSRDYWxsQ29yZTtMAAdvdXRCYXNlcQB+ABtMAAlvdXRPZmZzZXRxAH4AG0wAB291dFNpemVxAH4AG0wADXNpZ1Jlc29sdXRpb250AA9MamF2YS91dGlsL1NldDtMAAV0b1ZhcnEAfgAbTAAIdmFsdWVWYXJxAH4AG3hwAAAABHNyACRpbnN0cnVtZW50YXRpb24uY2FsbHMuQ2FsbENvbnZlbnRpb25HtO1ulL788QIAA0kACGNhbGxlcklkTAAFaW5wdXR0ABlMYW5hbHlzaXMvaWNmZy9DYWxsSW5wdXQ7TAAGcmF3T3V0dAAiTGluc3RydW1lbnRhdGlvbi9jYWxscy9DYWxsT3V0cHV0O3hwAAAAAHNyABdhbmFseXNpcy5pY2ZnLkNhbGxJbnB1dJjJD1MhNUxQAgAHTAAHYmFzZVZhcnQAGUx2Yy9kYXRhL1RBQ0V4cHIkU3ltJFZhcjtMABBlbmNvZGVkQXJndW1lbnRzdAAjTGFuYWx5c2lzL2ljZmcvQUJJQXJndW1lbnRFbmNvZGluZztMABNpbnB1dFNpemVMb3dlckJvdW5kcQB+AAZMAAZvZmZzZXR0ABVMdmMvZGF0YS9UQUNFeHByJFN5bTtMABRyYW5nZVRvRGVjb21wb3NlZEFyZ3QAD0xqYXZhL3V0aWwvTWFwO0wAEHNpbXBsaWZpZWRPZmZzZXR0ABtMdmMvZGF0YS9UQUNFeHByJFN5bSRDb25zdDtMAARzaXplcQB+ACZ4cHNyABd2Yy5kYXRhLlRBQ0V4cHIkU3ltJFZhcskrg43eGgPnAgACTAABc3QAF0x2Yy9kYXRhL1RBQ1N5bWJvbCRWYXI7TAADdGFndAAJTHRhYy9UYWc7eHIAE3ZjLmRhdGEuVEFDRXhwciRTeW2iVj0S4YSNUAIAAHhyAA92Yy5kYXRhLlRBQ0V4cHJYhGlUu/v+yAIAAHhwc3IANnZjLmRhdGEuVEFDU3ltYm9sJFZhciRXaXRoRGVmYXVsdENhbGxJbmRleCRXaXRoQnl0ZU1hcJ7+oHF4CHAAAgACTAAEbWV0YXQALUxrb3RsaW54L2NvbGxlY3Rpb25zL2ltbXV0YWJsZS9QZXJzaXN0ZW50TWFwO0wACm5hbWVQcmVmaXh0ABJMamF2YS9sYW5nL1N0cmluZzt4cgAVdmMuZGF0YS5UQUNTeW1ib2wkVmFyCYrCGVl9SXYCAAB4cgARdmMuZGF0YS5UQUNTeW1ib2zd3Run/CoWswIAAHhwc3IAJmRhdGFzdHJ1Y3R1cmVzLnRyZWFwLkhhc2hUcmVhcE1hcCROb2Rlf2t9acJIPnQCAANMAANrZXl0ABJMamF2YS9sYW5nL09iamVjdDtMAARuZXh0dAA1TGRhdGFzdHJ1Y3R1cmVzL3RyZWFwL0hhc2hUcmVhcE1hcCRNb3JlS2V5VmFsdWVQYWlycztMAAV2YWx1ZXEAfgA3eHIAIWRhdGFzdHJ1Y3R1cmVzLnRyZWFwLkhhc2hUcmVhcE1hcPMJ/2vt3boKAgAAeHIAHWRhdGFzdHJ1Y3R1cmVzLnRyZWFwLlRyZWFwTWFw46LAyn3v5moCAAB4cgAaZGF0YXN0cnVjdHVyZXMudHJlYXAuVHJlYXA88f21zZwbdQIAAkwABGxlZnR0ABxMZGF0YXN0cnVjdHVyZXMvdHJlYXAvVHJlYXA7TAAFcmlnaHRxAH4APHhwcHNxAH4ANnBzcQB+ADZwcHNyAAt0YWMuTWV0YUtleVF/W3MiCfIZAgADTAAPZXJhc3VyZVN0cmF0ZWd5dAAdTHRhYy9NZXRhS2V5JEVyYXN1cmVTdHJhdGVneTtMAARuYW1lcQB+ADJMAAN0eXB0ABFMamF2YS9sYW5nL0NsYXNzO3hwfnIAG3RhYy5NZXRhS2V5JEVyYXN1cmVTdHJhdGVneQAAAAAAAAAAEgAAeHIADmphdmEubGFuZy5FbnVtAAAAAAAAAAASAAB4cHQACUNhbm9uaWNhbHQAF3RhYy5tZW1vcnkucGFydGl0aW9uLWlkdnIAEWphdmEubGFuZy5JbnRlZ2VyEuKgpPeBhzgCAAFJAAV2YWx1ZXhxAH4ADnBzcQB+AEkAAAAGc3EAfgBAcQB+AEZ0ABJUYWMuc3ltYm9sLmtleXdvcmR2cgAQamF2YS5sYW5nLlN0cmluZ6DwpDh6O7NCAgAAeHBwdAAEdGFjTXNxAH4AQHEAfgBGdAANdGFjLmlzLm1lbW9yeXZyACJ0YWMuTWV0YU1hcCRDb21wYW5pb24kTm90aGluZ1ZhbHVl8nsHH85ykpUCAAB4cHBzcQB+AFN0AA90YWNNQ0FOT04yISE0ODRzcgAPdGFjLlRhZyRCeXRlTWFwNb/Ry6GDRgkCAAB4cgALdGFjLlRhZyRNYXABJytzDV3P/QIAAHhyAAd0YWMuVGFnLk9V3gn2xngCAAB4cHBzcQB+AAz///////////////7////+AAAAAXVxAH4AEAAAAAFkeHNxAH4AKnNyADV2Yy5kYXRhLlRBQ1N5bWJvbCRWYXIkV2l0aERlZmF1bHRDYWxsSW5kZXgkV2l0aEJpdDI1NnqsyEgq0drPAgACTAAEbWV0YXEAfgAxTAAKbmFtZVByZWZpeHEAfgAyeHEAfgAzc3EAfgA2c3EAfgA2cHBxAH4ATHB0AAFMcHNxAH4AQHEAfgBGdAAQdGFjLnN0YWNrLmhlaWdodHEAfgBKcHNxAH4ASQAAA/h0AARSNDg1c3IADnRhYy5UYWckQml0MjU2IyLQT+LlKkgCAAB4cQB+AFlzcgARamF2YS51dGlsLkhhc2hNYXAFB9rBwxZg0QMAAkYACmxvYWRGYWN0b3JJAAl0aHJlc2hvbGR4cD9AAAAAAAADdwgAAAAEAAAAAnNyAB5hbmFseXNpcy5pY2ZnLlNjcmF0Y2hCeXRlUmFuZ2XBTLaPpUzj2gIAAkwABGZyb21xAH4ABkwAAnRvcQB+AAZ4cHNxAH4ADP///////////////v////4AAAAAdXEAfgAQAAAAAHhzcQB+AAz///////////////7////+AAAAAXVxAH4AEAAAAAEDeHNyAC1hbmFseXNpcy5pY2ZnLkRlY29tcG9zZWRDYWxsSW5wdXRBcmckQ29uc3RhbnSFavLdQafqPQIAA0wAAWN0ABlMdmMvZGF0YS9UQUNTeW1ib2wkQ29uc3Q7TAARY29udHJhY3RSZWZlcmVuY2V0AC9MYW5hbHlzaXMvaWNmZy9DYWxsR3JhcGhCdWlsZGVyJENhbGxlZENvbnRyYWN0O0wADHNjcmF0Y2hSYW5nZXQAIExhbmFseXNpcy9pY2ZnL1NjcmF0Y2hCeXRlUmFuZ2U7eHIAJGFuYWx5c2lzLmljZmcuRGVjb21wb3NlZENhbGxJbnB1dEFyZ82Nwhnirh8hAgAAeHBzcgAXdmMuZGF0YS5UQUNTeW1ib2wkQ29uc3QmHp5/l8IUcAIAAkwAA3RhZ3EAfgAsTAAFdmFsdWVxAH4ABnhxAH4ANHEAfgBoc3EAfgAM///////////////+/////gAAAAF1cQB+ABAAAAAgOEL3dgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAB4cHEAfgBsc3EAfgBrc3EAfgAM///////////////+/////gAAAAF1cQB+ABAAAAABRHhzcQB+AAz///////////////7////+AAAAAXVxAH4AEAAAAAFjeHNyAC1hbmFseXNpcy5pY2ZnLkRlY29tcG9zZWRDYWxsSW5wdXRBcmckVmFyaWFibGWV3y80jneopQIAA0wAEWNvbnRyYWN0UmVmZXJlbmNlcQB+AHNMAAxzY3JhdGNoUmFuZ2VxAH4AdEwAAXZxAH4AK3hxAH4AdXNyADxhbmFseXNpcy5pY2ZnLkNhbGxHcmFwaEJ1aWxkZXIkQ2FsbGVkQ29udHJhY3QkVW5yZXNvbHZlZFJlYWRDhKJZ0RDzoAIAAUkADXN0b3JhZ2VSZWFkSWR4cgAtYW5hbHlzaXMuaWNmZy5DYWxsR3JhcGhCdWlsZGVyJENhbGxlZENvbnRyYWN00wt1rN/LodcCAAB4cAAAAAhxAH4Ae3NxAH4AXnNxAH4ANnNxAH4ANnBzcQB+ADZzcQB+ADZzcQB+ADZwc3EAfgA2cHBxAH4ATHBxAH4AYnNxAH4AQHEAfgBGdAAWdGFjLnNjYWxhcml6YXRpb24uc29ydHZyABl2Yy5kYXRhLlNjYWxhcml6YXRpb25Tb3J0MM5wneRoDSYCAAB4cHBzcgAfdmMuZGF0YS5TY2FsYXJpemF0aW9uU29ydCRTcGxpdFT/Wafxx7IFAgABTAADaWR4cQB+AAZ4cQB+AI5zcQB+AAz///////////////7////+AAAAAXVxAH4AEAAAAAEFeHNxAH4ANnBzcQB+ADZwc3EAfgA2cHBzcQB+AEBxAH4ARnQAHHRhYy5zdG9yYWdlLm5vbi1pbmRleGVkLXBhdGh2cgA1YW5hbHlzaXMuc3RvcmFnZS5TdG9yYWdlQW5hbHlzaXNSZXN1bHQkTm9uSW5kZXhlZFBhdGgIwaBLofo/RQIAAHhwcHNyADphbmFseXNpcy5zdG9yYWdlLlN0b3JhZ2VBbmFseXNpc1Jlc3VsdCROb25JbmRleGVkUGF0aCRSb290vzf12KXqCv8CAAFMAARzbG90cQB+AAZ4cQB+AJlxAH4AknNxAH4AQHEAfgBGdAANdGFjLnNsb3QudHlwZXZyADpzcGVjLmN2bGFzdC50eXBlZGVzY3JpcHRvcnMuRVZNVHlwZURlc2NyaXB0b3IkRVZNVmFsdWVUeXBlxomvArrquCUCAAB4cgAtc3BlYy5jdmxhc3QudHlwZWRlc2NyaXB0b3JzLkVWTVR5cGVEZXNjcmlwdG9yyFGp8TzCah0CAAB4cHBzcgAzc3BlYy5jdmxhc3QudHlwZWRlc2NyaXB0b3JzLkVWTVR5cGVEZXNjcmlwdG9yJFVJbnRL+xQfR/Nlf8ACAAFJAAhiaXR3aWR0aHhyAERzcGVjLmN2bGFzdC50eXBlZGVzY3JpcHRvcnMuRVZNVHlwZURlc2NyaXB0b3IkRVZNSXNvbW9ycGhpY1ZhbHVlVHlwZfd1mJFuEKEPAgAAeHEAfgCfAAABAHNxAH4AQH5xAH4ARHQABkVyYXNlZHQAGHRhYy5zdG9yYWdlLnByZXR0eS5wYXRoc3ZyAB1hbmFseXNpcy5zdG9yYWdlLkRpc3BsYXlQYXRoc/dES7fD9VEWAgABTAAFcGF0aHNxAH4AHXhwcHNxAH4AqXNyABdqYXZhLnV0aWwuTGlua2VkSGFzaFNldNhs11qV3SoeAgAAeHIAEWphdmEudXRpbC5IYXNoU2V0ukSFlZa4tzQDAAB4cHcMAAAAED9AAAAAAAABc3IAIWFuYWx5c2lzLnN0b3JhZ2UuRGlzcGxheVBhdGgkUm9vdNNzoL2Z0DxyAgACTAAEYmFzZXQAHkxhbmFseXNpcy9zdG9yYWdlL0Rpc3BsYXlQYXRoO0wABG5hbWVxAH4AMnhyABxhbmFseXNpcy5zdG9yYWdlLkRpc3BsYXlQYXRoT0Bj6lbSIAUCAAB4cHB0AAhmdXR1cmVfQXhzcQB+AEBxAH4ARnQAFXRhYy5zdG9yYWdlLmJpdC13aWR0aHEAfgBKcHNxAH4ASQAAAQBwc3EAfgBAcQB+AEZ0AAt0YWMuc3RvcmFnZXZxAH4ADHBxAH4AD3NxAH4AQHEAfgBGdAAYdGFjLmRlY29tcC1p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"}
		AnnotationCmd:102 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageGlobalChangeSnippet.StorageBackupPoint","calleeTxId":8}}
		NopCmd
		AssumeExpCmd LAnd(Eq(tacCalldatasize!!4:2 0x64 ) Eq(tacCalldatasize!!4:2 0x64 ) )
		AssignExpCmd:102 B409:51 Eq(Select(tacCalldatabuf!!20@8:118 0x0 ) 0x3842f77600000000000000000000000000000000000000000000000000000000 )
		AssumeCmd:102 B409:51
		AssignExpCmd:102 tacCalldatabuf!!410@8:19 LongStore(tacCalldatabuf!!20@8:118 0x4 tacMCANON2!!484:12 0x124 Sub(0x64 0x4 ) )
		LabelCmd:102 "Start procedure curve-get_D(uint256[2],uint256)"
		AnnotationCmd:102 JSON{"key":{"name":"fps.free-pointer-is-scalarized","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true}
		AssignExpCmd:102 R411:51 Select(tacExtcodesize!!6:3 Apply(to_skey:bif R27:60) )
		NopCmd
		AssumeExpCmd Gt(R411:51 0x0 )
		AnnotationCmd:102 JSON{"key":{"name":"internal.func.finder.info","type":"analysis.ip.InternalFunctionFinderReport","erasureStrategy":"Erased"},"value":"rO0ABXNyAChhbmFseXNpcy5pcC5JbnRlcm5hbEZ1bmN0aW9uRmluZGVyUmVwb3J0ian+bYn1VdACAAFMABN1bnJlc29sdmVkRnVuY3Rpb25zdAAPTGphdmEvdXRpbC9TZXQ7eHBzcgAhZGF0YXN0cnVjdHVyZXMuTGlua2VkQXJyYXlIYXNoU2V0AAAAAAAAAAEDAAJGAApsb2FkRmFjdG9yTAAJaGFzaFRhYmxldAAuTGRhdGFzdHJ1Y3R1cmVzL2FycmF5aGFzaHRhYmxlL0FycmF5SGFzaFRhYmxlO3hwdwgAAAAAQAAAAHg="}
		AnnotationCmd:102 JSON{"key":{"name":"fps.free-pointer-is-scalarized","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true}
		NopCmd
		AssumeExpCmd LNot(Lt(tacCalldatasize!!4:2 0x4 ) )
		NopCmd
		AssumeExpCmd Gt(0x82c63066 tacSighash!!38:44 )
		NopCmd
		AssumeExpCmd Eq(0x3842f776 tacSighash!!38:44 )
		AssignExpCmd:119 R417:90 Sub(tacCalldatasize!!4:2 0x4 )
		AssignExpCmd:102 B418:80 Slt(R417:90 0x60 )
		NopCmd
		AssumeExpCmd LNot(B418:80 )
		NopCmd
		AssumeExpCmd Slt(0x23 tacCalldatasize!!4:91 )
		AssignExpCmd:120 R422:93 0x80
		AssumeCmd:121 true
		AssignExpCmd:102 B423:74 Gt(0x44 tacCalldatasize!!4:91 )
		NopCmd
		AssumeExpCmd LNot(B423:74 )
		AnnotationCmd:102 JSON{"key":{"name":"dsa.assign.start","type":"java.lang.String","erasureStrategy":"Erased"},"value":"4280_1005_0_0_0_0 -> 4282_1004_0_0_0_0"}
		LabelCmd:102 "Parallel assignment for R3573:bv256, R3574:bv256 := R2326:bv256, R3653:bv256"
		AnnotationCmd:102 JSON{"key":{"name":"dsa.assign.end","type":"java.lang.String","erasureStrategy":"Erased"},"value":"4280_1005_0_0_0_0 -> 4282_1004_0_0_0_0"}
		AnnotationCmd:102 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.LoopSnippet.StartLoopSnippet","loopIndex":3,"loopSource":"unknown loop source code"}}
		AnnotationCmd:102 JSON{"key":{"name":"start_loop.cmd","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		AnnotationCmd:102 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.LoopSnippet.StartIter","iteration":1}}
		AssignExpCmd:122 R425:96 Select(tacCalldatabuf!!410@8:118 0x4 )
		AssignExpCmd:123 tacMCANON3!!426:14 Store(tacMCANON3!!17:14 0x80 R425:96 )
		AnnotationCmd:102 JSON{"key":{"name":"dsa.assign.start","type":"java.lang.String","erasureStrategy":"Erased"},"value":"4301_1002_0_0_0_0 -> 4282_1004_0_0_0_0"}
		LabelCmd:102 "Parallel assignment for R3573:bv256, R3574:bv256 := R3566:bv256, R3570:bv256"
		AnnotationCmd:102 JSON{"key":{"name":"dsa.assign.end","type":"java.lang.String","erasureStrategy":"Erased"},"value":"4301_1002_0_0_0_0 -> 4282_1004_0_0_0_0"}
		AnnotationCmd:102 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.LoopSnippet.EndIter","iteration":1}}
		AnnotationCmd:102 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.LoopSnippet.StartIter","iteration":2}}
		AssignExpCmd:122 R427:96 Select(tacCalldatabuf!!410@8:118 0x24 )
		AssignExpCmd:123 tacMCANON3!!428:14 Store(tacMCANON3!!426:14 0xa0 R427:96 )
		AnnotationCmd:102 JSON{"key":{"name":"dsa.assign.start","type":"java.lang.String","erasureStrategy":"Erased"},"value":"4301_1002_0_0_0_0 -> 4282_1004_0_0_0_0"}
		LabelCmd:102 "Parallel assignment for R3573:bv256, R3574:bv256 := R3566:bv256, R3570:bv256"
		AnnotationCmd:102 JSON{"key":{"name":"dsa.assign.end","type":"java.lang.String","erasureStrategy":"Erased"},"value":"4301_1002_0_0_0_0 -> 4282_1004_0_0_0_0"}
		AnnotationCmd:102 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.LoopSnippet.EndIter","iteration":2}}
		AnnotationCmd:102 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.LoopSnippet.EndLoopSnippet","loopId":3}}
		AnnotationCmd:102 JSON{"key":{"name":"end_loop.cmd","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		AnnotationCmd:102 JSON{"key":{"name":"pta.end-allocation","type":"analysis.alloc.AllocationAnalysis$AbstractLocation","erasureStrategy":"Erased"},"value":{"prevFPWriteIdx":0,"nextFPWriteCmd":{"block":{"#class":"tac.BlockIdentifier","origStartPc":4102,"stkTop":1000,"decompCopy":0,"calleeIdx":0,"topOfStackValue":0,"freshCopy":0},"pos":1},"sort":{"#class":"analysis.alloc.AllocationAnalysis.Alloc.ConstBlock","sz":"40"}}}
		AssignExpCmd:122 R429:62 Select(tacCalldatabuf!!410@8:118 0x44 )
		AnnotationCmd:102 JSON{"key":{"name":"internal.func.start","type":"analysis.ip.InternalFuncStartAnnotation","erasureStrategy":"CallTrace"},"value":{"id":8,"startPc":558,"args":[{"s":{"namePrefix":"R422","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1001}]},"offset":1,"sort":"SCALAR"},{"s":{"namePrefix":"R429","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1012}]},"offset":2,"sort":"SCALAR"}],"methodSignature":{"#class":"spec.cvlast.QualifiedMethodSignature.QualifiedMethodSig","qualifiedMethodName":{"#class":"spec.cvlast.QualifiedFunction","host":{"name":"curve"},"methodId":"get_D"},"params":[{"#class":"spec.cvlast.VMParam.Named","name":"xp","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$StaticArrayDescriptor","location":"memory","elementType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256},"numElements":"2"}},{"#class":"spec.cvlast.VMParam.Named","name":"amp","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256}}],"res":[{"#class":"spec.cvlast.VMParam.Unnamed","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256}}]},"stackOffsetToArgPos":{"1":0,"2":1},"callSiteSrc":{"source":0,"begin":3416,"len":1542,"jumpType":"ENTER","address":"ce4604a0000000000000000000000017","sourceContext":{"indexToFilepath":{"0":"contracts/curve.sol","1":"Context.sol","2":"ERC20.sol","3":"IERC20.sol","4":"IERC20Metadata.sol","5":"ReentrancyGuard.sol"},"sourceDir":".post_autofinders.1"}}}}
		AssignExpCmd:124 R430:80 Select(tacMCANON3!!428:14 0xa0 )
		AssignExpCmd:125 R431:90 Select(tacMCANON3!!428:14 0x80 )
		NopCmd
		AssumeExpCmd Apply(add_noofl:bif R431:90 R430:80)
		AssignExpCmd I434:51 Apply(safe_math_promotion:bif R431:90)
		AssignExpCmd I435:51 Apply(safe_math_promotion:bif R430:80)
		NopCmd
		AssignExpCmd R437:69 Apply(safe_math_narrow:bif IntAdd(I434:51 I435:51))
		AnnotationCmd:102 JSON{"key":{"name":"internal.func.end","type":"analysis.ip.InternalFuncExitAnnotation","erasureStrategy":"Canonical"},"value":{"id":8,"rets":[{"s":{"namePrefix":"R437","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1023}]},"offset":0}],"functionLayout":{"0":{"#class":"analysis.ip.InternalFuncValueLocation.Scalar"}}}}
		AnnotationCmd:102 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.EVMFunctionReturnWrite","returnbufOffset":"0","returnValueSym":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R437","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1023}]},"callIndex":8}}
		AnnotationCmd:102 JSON{"key":{"name":"tac.return.path","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		LabelCmd:102 "End procedure curve-get_D(uint256[2],uint256)"
		AssignExpCmd:102 tacReturndata!!439:75 Store(tacReturndata!!488:75 0x0 R437:69 )
		AssignExpCmd:102 tacMCANON2!!440:12 Store(tacMCANON2!!484:12 0x120 R437:69 )
		AnnotationCmd:102 JSON{"key":{"name":"call.trace.pop","type":"analysis.icfg.Inliner$CallStack$PopRecord","erasureStrategy":"Canonical"},"value":"rO0ABXNyAClhbmFseXNpcy5pY2ZnLklubGluZXIkQ2FsbFN0YWNrJFBvcFJlY29yZPAPfwSLdCWJAgABSQAIY2FsbGVlSWR4cAAAAAg="}
		JumpCmd:102 2_0_0_6_0_0
	}
	Block 0_0_0_9_0_0 Succ [3_0_0_6_0_0] {
		AnnotationCmd:102 JSON{"key":{"name":"call.trace.push","type":"analysis.icfg.Inliner$CallStack$PushRecord","erasureStrategy":"Canonical"},"value":"rO0ABXNyACphbmFseXNpcy5pY2ZnLklubGluZXIkQ2FsbFN0YWNrJFB1c2hSZWNvcmSX8+DCTLCH+AIAA0kACGNhbGxlZUlkTAAGY2FsbGVldAATTHZjL2RhdGEvTWV0aG9kUmVmO0wAB3N1bW1hcnl0ABVMdmMvZGF0YS9DYWxsU3VtbWFyeTt4cAAAAAlzcgARdmMuZGF0YS5NZXRob2RSZWbJlJTzzU9pGAIAA0wABGF0dHJ0ABdMc2NlbmUvTWV0aG9kQXR0cmlidXRlO0wACmNvbnRyYWN0SWR0ABZMamF2YS9tYXRoL0JpZ0ludGVnZXI7TAAHc2lnSGFzaHQAEExldm0vU2lnaGFzaEludDt4cHNyABxzY2VuZS5NZXRob2RBdHRyaWJ1dGUkQ29tbW9uNHjdebdr9XMCAAB4cgAVc2NlbmUuTWV0aG9kQXR0cmlidXRlcYg2pYWutuUCAAB4cHNyABRqYXZhLm1hdGguQmlnSW50ZWdlcoz8nx+pO/sdAwAGSQAIYml0Q291bnRJAAliaXRMZW5ndGhJABNmaXJzdE5vbnplcm9CeXRlTnVtSQAMbG93ZXN0U2V0Qml0SQAGc2lnbnVtWwAJbWFnbml0dWRldAACW0J4cgAQamF2YS5sYW5nLk51bWJlcoaslR0LlOCLAgAAeHD///////////////7////+AAAAAXVyAAJbQqzzF/gGCFTgAgAAeHAAAAAQzkYEoAAAAAAAAAAAAAAAFHhzcgAOZXZtLlNpZ2hhc2hJbnRUdcqNMXEgeAIAAUwAAW5xAH4ABnhwc3EAfgAM///////////////+/////gAAAAF1cQB+ABAAAAAEGBYN3XhzcgATdmMuZGF0YS5DYWxsU3VtbWFyeZQcmw5vl+FdAgAQSQAJc3VtbWFyeUlkTAAOY2FsbENvbnZlbnRpb250ACZMaW5zdHJ1bWVudGF0aW9uL2NhbGxzL0NhbGxDb252ZW50aW9uO0wACmNhbGxUYXJnZXR0ABpMYW5hbHlzaXMvaWNmZy9DYWxsVGFyZ2V0O0wACGNhbGxUeXBldAAVTHZjL2RhdGEvVEFDQ2FsbFR5cGU7TAAPY2Fubm90QmVJbmxpbmVkdAAtTGFuYWx5c2lzL2ljZmcvSW5saW5lciRJbGxlZ2FsSW5saW5pbmdSZWFzb247TAAGZ2FzVmFydAATTHZjL2RhdGEvVEFDU3ltYm9sO0wABmluQmFzZXEAfgAbTAAIaW5PZmZzZXRxAH4AG0wABmluU2l6ZXEAfgAbTAAMb3JpZ0NhbGxjb3JldAAgTHZjL2RhdGEvVEFDQ21kJFNpbXBsZSRDYWxsQ29yZTtMAAdvdXRCYXNlcQB+ABtMAAlvdXRPZmZzZXRxAH4AG0wAB291dFNpemVxAH4AG0wADXNpZ1Jlc29sdXRpb250AA9MamF2YS91dGlsL1NldDtMAAV0b1ZhcnEAfgAbTAAIdmFsdWVWYXJxAH4AG3hwAAAABXNyACRpbnN0cnVtZW50YXRpb24uY2FsbHMuQ2FsbENvbnZlbnRpb25HtO1ulL788QIAA0kACGNhbGxlcklkTAAFaW5wdXR0ABlMYW5hbHlzaXMvaWNmZy9DYWxsSW5wdXQ7TAAGcmF3T3V0dAAiTGluc3RydW1lbnRhdGlvbi9jYWxscy9DYWxsT3V0cHV0O3hwAAAAAHNyABdhbmFseXNpcy5pY2ZnLkNhbGxJbnB1dJjJD1MhNUxQAgAHTAAHYmFzZVZhcnQAGUx2Yy9kYXRhL1RBQ0V4cHIkU3ltJFZhcjtMABBlbmNvZGVkQXJndW1lbnRzdAAjTGFuYWx5c2lzL2ljZmcvQUJJQXJndW1lbnRFbmNvZGluZztMABNpbnB1dFNpemVMb3dlckJvdW5kcQB+AAZMAAZvZmZzZXR0ABVMdmMvZGF0YS9UQUNFeHByJFN5bTtMABRyYW5nZVRvRGVjb21wb3NlZEFyZ3QAD0xqYXZhL3V0aWwvTWFwO0wAEHNpbXBsaWZpZWRPZmZzZXR0ABtMdmMvZGF0YS9UQUNFeHByJFN5bSRDb25zdDtMAARzaXplcQB+ACZ4cHNyABd2Yy5kYXRhLlRBQ0V4cHIkU3ltJFZhcskrg43eGgPnAgACTAABc3QAF0x2Yy9kYXRhL1RBQ1N5bWJvbCRWYXI7TAADdGFndAAJTHRhYy9UYWc7eHIAE3ZjLmRhdGEuVEFDRXhwciRTeW2iVj0S4YSNUAIAAHhyAA92Yy5kYXRhLlRBQ0V4cHJYhGlUu/v+yAIAAHhwc3IANnZjLmRhdGEuVEFDU3ltYm9sJFZhciRXaXRoRGVmYXVsdENhbGxJbmRleCRXaXRoQnl0ZU1hcJ7+oHF4CHAAAgACTAAEbWV0YXQALUxrb3RsaW54L2NvbGxlY3Rpb25zL2ltbXV0YWJsZS9QZXJzaXN0ZW50TWFwO0wACm5hbWVQcmVmaXh0ABJMamF2YS9sYW5nL1N0cmluZzt4cgAVdmMuZGF0YS5UQUNTeW1ib2wkVmFyCYrCGVl9SXYCAAB4cgARdmMuZGF0YS5UQUNTeW1ib2zd3Run/CoWswIAAHhwc3IAJmRhdGFzdHJ1Y3R1cmVzLnRyZWFwLkhhc2hUcmVhcE1hcCROb2Rlf2t9acJIPnQCAANMAANrZXl0ABJMamF2YS9sYW5nL09iamVjdDtMAARuZXh0dAA1TGRhdGFzdHJ1Y3R1cmVzL3RyZWFwL0hhc2hUcmVhcE1hcCRNb3JlS2V5VmFsdWVQYWlycztMAAV2YWx1ZXEAfgA3eHIAIWRhdGFzdHJ1Y3R1cmVzLnRyZWFwLkhhc2hUcmVhcE1hcPMJ/2vt3boKAgAAeHIAHWRhdGFzdHJ1Y3R1cmVzLnRyZWFwLlRyZWFwTWFw46LAyn3v5moCAAB4cgAaZGF0YXN0cnVjdHVyZXMudHJlYXAuVHJlYXA88f21zZwbdQIAAkwABGxlZnR0ABxMZGF0YXN0cnVjdHVyZXMvdHJlYXAvVHJlYXA7TAAFcmlnaHRxAH4APHhwcHNxAH4ANnBzcQB+ADZwcHNyAAt0YWMuTWV0YUtleVF/W3MiCfIZAgADTAAPZXJhc3VyZVN0cmF0ZWd5dAAdTHRhYy9NZXRhS2V5JEVyYXN1cmVTdHJhdGVneTtMAARuYW1lcQB+ADJMAAN0eXB0ABFMamF2YS9sYW5nL0NsYXNzO3hwfnIAG3RhYy5NZXRhS2V5JEVyYXN1cmVTdHJhdGVneQAAAAAAAAAAEgAAeHIADmphdmEubGFuZy5FbnVtAAAAAAAAAAASAAB4cHQACUNhbm9uaWNhbHQAF3RhYy5tZW1vcnkucGFydGl0aW9uLWlkdnIAEWphdmEubGFuZy5JbnRlZ2VyEuKgpPeBhzgCAAFJAAV2YWx1ZXhxAH4ADnBzcQB+AEkAAAAGc3EAfgBAcQB+AEZ0ABJUYWMuc3ltYm9sLmtleXdvcmR2cgAQamF2YS5sYW5nLlN0cmluZ6DwpDh6O7NCAgAAeHBwdAAEdGFjTXNxAH4AQHEAfgBGdAANdGFjLmlzLm1lbW9yeXZyACJ0YWMuTWV0YU1hcCRDb21wYW5pb24kTm90aGluZ1ZhbHVl8nsHH85ykpUCAAB4cHBzcQB+AFN0AA90YWNNQ0FOT04yISE1MzVzcgAPdGFjLlRhZyRCeXRlTWFwNb/Ry6GDRgkCAAB4cgALdGFjLlRhZyRNYXABJytzDV3P/QIAAHhyAAd0YWMuVGFnLk9V3gn2xngCAAB4cHBzcQB+AAz///////////////7////+AAAAAXVxAH4AEAAAAAEEeHNxAH4AKnNyADV2Yy5kYXRhLlRBQ1N5bWJvbCRWYXIkV2l0aERlZmF1bHRDYWxsSW5kZXgkV2l0aEJpdDI1NnqsyEgq0drPAgACTAAEbWV0YXEAfgAxTAAKbmFtZVByZWZpeHEAfgAyeHEAfgAzc3EAfgA2c3EAfgA2cHBxAH4ATHB0AAFMcHNxAH4AQHEAfgBGdAAQdGFjLnN0YWNrLmhlaWdodHEAfgBKcHNxAH4ASQAAA/d0AARSNTM2c3IADnRhYy5UYWckQml0MjU2IyLQT+LlKkgCAAB4cQB+AFlzcgARamF2YS51dGlsLkhhc2hNYXAFB9rBwxZg0QMAAkYACmxvYWRGYWN0b3JJAAl0aHJlc2hvbGR4cD9AAAAAAAABdwgAAAACAAAAAXNyAB5hbmFseXNpcy5pY2ZnLlNjcmF0Y2hCeXRlUmFuZ2XBTLaPpUzj2gIAAkwABGZyb21xAH4ABkwAAnRvcQB+AAZ4cHNxAH4ADP///////////////v////4AAAAAdXEAfgAQAAAAAHhzcQB+AAz///////////////7////+AAAAAXVxAH4AEAAAAAEDeHNyAC1hbmFseXNpcy5pY2ZnLkRlY29tcG9zZWRDYWxsSW5wdXRBcmckQ29uc3RhbnSFavLdQafqPQIAA0wAAWN0ABlMdmMvZGF0YS9UQUNTeW1ib2wkQ29uc3Q7TAARY29udHJhY3RSZWZlcmVuY2V0AC9MYW5hbHlzaXMvaWNmZy9DYWxsR3JhcGhCdWlsZGVyJENhbGxlZENvbnRyYWN0O0wADHNjcmF0Y2hSYW5nZXQAIExhbmFseXNpcy9pY2ZnL1NjcmF0Y2hCeXRlUmFuZ2U7eHIAJGFuYWx5c2lzLmljZmcuRGVjb21wb3NlZENhbGxJbnB1dEFy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Ra0Sk4jk9wIAAkkABXN0YXJ0TAALcGFja2VkU3RhcnR0ABtMdmMvZGF0YS9TY2FsYXJpemF0aW9uU29ydDt4cQB+AOoAAAAAc3IAH3ZjLmRhdGEuU2NhbGFyaXphdGlvblNvcnQkU3BsaXRU/1mn8ceyBQIAAUwAA2lkeHEAfgAGeHEAfgDqc3EAfgAM///////////////+/////gAAAAF1cQB+ABAAAAABDHhzcQB+ADZwc3EAfgA2cHNxAH4ANnBwc3EAfgBAcQB+AEZ0ABx0YWMuc3RvcmFnZS5ub24taW5kZXhlZC1wYXRodnIANWFuYWx5c2lzLnN0b3JhZ2UuU3RvcmFnZUFuYWx5c2lzUmVzdWx0JE5vbkluZGV4ZWRQYXRoCMGgS6H6P0UCAAB4cHBzcgA6YW5hbHlzaXMuc3RvcmFnZS5TdG9yYWdlQW5hbHlzaXNSZXN1bHQkTm9uSW5kZXhlZFBhdGgkUm9vdL839dil6gr/AgABTAAEc2xvdHEAfgAGeHEAfgD4cQB+APFzcQB+AEBxAH4ARnQADXRhYy5zbG90LnR5cGV2cgA6c3BlYy5jdmxhc3QudHlwZWRlc2NyaXB0b3JzLkVWTVR5cGVEZXNjcmlwdG9yJEVWTVZhbHVlVHlwZcaJrwK66rglAgAAeHIALXNwZWMuY3ZsYXN0LnR5cGVkZXNjcmlwdG9ycy5FVk1UeXBlRGVzY3JpcHRvcshRqfE8wmodAgAAeHBwc3IANXNwZWMuY3ZsYXN0LnR5cGVkZXNjcmlwdG9ycy5FVk1UeXBlRGVzY3JpcHRvciRhZGRyZXNzevhl9G+XoCkCAAB4cgBEc3BlYy5jdmxhc3QudHlwZWRlc2NyaXB0b3JzLkVWTVR5cGVEZXNjcmlwdG9yJEVWTUlzb21vcnBoaWNWYWx1ZVR5cGX3dZiRbhChDwIAAHhxAH4A/nNxAH4AQH5xAH4ARHQABkVyYXNlZHQAGHRhYy5zdG9yYWdlLnByZXR0eS5wYXRoc3ZyAB1hbmFseXNpcy5zdG9yYWdlLkRpc3BsYXlQYXRoc/dES7fD9VEWAgABTAAFcGF0aHNxAH4AHXhwcHNxAH4BCHNyABdqYXZhLnV0aWwuTGlua2VkSGFzaFNldNhs11qV3SoeAgAAeHIAEWphdmEudXRpbC5IYXNoU2V0ukSFlZa4tzQDAAB4cHcMAAAAED9AAAAAAAABc3IAIWFuYWx5c2lzLnN0b3JhZ2UuRGlzcGxheVBhdGgkUm9vdNNzoL2Z0DxyAgACTAAEYmFzZXQAHkxhbmFseXNpcy9zdG9yYWdlL0Rpc3BsYXlQYXRoO0wABG5hbWVxAH4AMnhyABxhbmFseXNpcy5zdG9yYWdlLkRpc3BsYXlQYXRoT0Bj6lbSIAUCAAB4cHB0AAhscF90b2tlbnhzcQB+AEBxAH4ARnQAFXRhYy5zdG9yYWdlLmJpdC13aWR0aHEAfgBKcHNxAH4ASQAAAKBwc3EAfgBAcQB+AEZ0AAt0YWMuc3RvcmFnZXZxAH4ADHBxAH4AxnBxAH4AY3BzcQB+AEkAAAP7dAALQ0FOT041NyEhMjJzcQB+AHdxAH4AaHEAfgBtc3EAfgAwc3EAfgA2cHNxAH4ANnBzcQB+ADZwcHEAfgBDcHEAfgBLcQB+AExwcQB+AFBxAH4AUXBxAH4AVXEAfgBWc3EAfgBec3EAfgA2c3EAfgA2cHBxAH4ATHBxAH4AYnBxAH4AY3BxAH4AjXEAfgBmcQB+AJBzcgAiamF2YS51dGlsLkNvbGxlY3Rpb25zJFNpbmdsZXRvblNldCxSQZgpwLG/AgABTAAHZWxlbWVudHEAfgA3eHBxAH4AFHNxAH4AXnNxAH4ANnNxAH4ANnNxAH4ANnNxAH4ANnBzcQB+ADZwcHEAfgBMcHEAfgBicQB+AOhwcQB+AO5zcQB+ADZwc3EAfgA2cHNxAH4ANnBwcQB+APZwcQB+APtxAH4A/HBxAH4BA3EAfgEEcHNxAH4BCHNxAH4BC3cMAAAAED9AAAAAAAABcQB+ARF4cQB+ARNwcQB+ARVwcQB+ARZwcQB+AMZwcQB+AGNwcQB+ARlxAH4BGnNxAH4Ad3EAfgBocQB+AG0="}
		AnnotationCmd:102 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageGlobalChangeSnippet.StorageBackupPoint","calleeTxId":9}}
		NopCmd
		AssumeExpCmd LAnd(Eq(tacCalldatasize!!5:2 0x4 ) Eq(tacCalldatasize!!5:2 0x4 ) )
		NopCmd
		AssumeExpCmd Eq(tacCalldatabufCANON0@9:1 0x18160ddd00000000000000000000000000000000000000000000000000000000 )
		LabelCmd:102 "Start procedure CurveTokenExample-totalSupply()"
		AnnotationCmd:102 JSON{"key":{"name":"fps.free-pointer-is-scalarized","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true}
		AssignExpCmd:102 R444:51 Select(tacExtcodesize!!6:3 Apply(to_skey:bif R25:100) )
		NopCmd
		AssumeExpCmd Gt(R444:51 0x0 )
		AnnotationCmd:102 JSON{"key":{"name":"internal.func.finder.info","type":"analysis.ip.InternalFunctionFinderReport","erasureStrategy":"Erased"},"value":"rO0ABXNyAChhbmFseXNpcy5pcC5JbnRlcm5hbEZ1bmN0aW9uRmluZGVyUmVwb3J0ian+bYn1VdACAAFMABN1bnJlc29sdmVkRnVuY3Rpb25zdAAPTGphdmEvdXRpbC9TZXQ7eHBzcgAhZGF0YXN0cnVjdHVyZXMuTGlua2VkQXJyYXlIYXNoU2V0AAAAAAAAAAEDAAJGAApsb2FkRmFjdG9yTAAJaGFzaFRhYmxldAAuTGRhdGFzdHJ1Y3R1cmVzL2FycmF5aGFzaHRhYmxlL0FycmF5SGFzaFRhYmxlO3hwdwgAAAAAQAAAAHg="}
		AnnotationCmd:102 JSON{"key":{"name":"fps.free-pointer-is-scalarized","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true}
		NopCmd
		AssumeExpCmd LNot(Lt(tacCalldatasize!!5:2 0x4 ) )
		NopCmd
		AssumeExpCmd Gt(0x40c10f19 tacSighash!!39:44 )
		NopCmd
		AssumeExpCmd LNot(Eq(0x6fdde03 tacSighash!!39:44 ) )
		NopCmd
		AssumeExpCmd LNot(Eq(0x95ea7b3 tacSighash!!39:44 ) )
		NopCmd
		AssumeExpCmd Eq(0x18160ddd tacSighash!!39:44 )
		AnnotationCmd:102 JSON{"key":{"name":"internal.func.start","type":"analysis.ip.InternalFuncStartAnnotation","erasureStrategy":"CallTrace"},"value":{"id":9,"startPc":1205,"args":[],"methodSignature":{"#class":"spec.cvlast.QualifiedMethodSignature.QualifiedMethodSig","qualifiedMethodName":{"#class":"spec.cvlast.QualifiedFunction","host":{"name":"CurveTokenExample"},"methodId":"totalSupply"},"params":[],"res":[{"#class":"spec.cvlast.VMParam.Unnamed","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256}}]},"stackOffsetToArgPos":{},"callSiteSrc":{"source":2,"begin":3952,"len":364,"jumpType":"ENTER","address":"ce4604a0000000000000000000000014","sourceContext":{"indexToFilepath":{"0":"contracts/curve.sol","1":"Context.sol","2":"ERC20.sol","3":"IERC20.sol","4":"IERC20Metadata.sol","5":"ReentrancyGuard.sol"},"sourceDir":".post_autofinders.1"}}}}
		AnnotationCmd:102 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet","value":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"CANON124!!8","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.scalarization.sort","type":"vc.data.ScalarizationSort","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.ScalarizationSort.Split","idx":"2"}},{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.storage.bit-width","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":256},{"key":{"name":"tac.storage.pretty.paths","type":"analysis.storage.DisplayPaths","erasureStrategy":"Erased"},"value":{"paths":[{"#class":"analysis.storage.DisplayPath.Root","name":"_totalSupply"}]}},{"key":{"name":"tac.slot.type","type":"spec.cvlast.typedescriptors.EVMTypeDescriptor$EVMValueType","erasureStrategy":"Canonical"},"value":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256}},{"key":{"name":"tac.storage.non-indexed-path","type":"analysis.storage.StorageAnalysisResult$NonIndexedPath","erasureStrategy":"Canonical"},"value":{"#class":"analysis.storage.StorageAnalysisResult.NonIndexedPath.Root","slot":"2"}},{"key":{"name":"tac.storage","type":"java.math.BigInteger","erasureStrategy":"Canonical"},"value":"ce4604a0000000000000000000000014"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1021}]},"displayPath":{"#class":"analysis.storage.DisplayPath.Root","name":"_totalSupply"},"storageType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256},"contractInstance":"ce4604a0000000000000000000000014","linkableStorageReadId":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet.Id","id":10}}}
		AnnotationCmd:102 JSON{"key":{"name":"internal.func.end","type":"analysis.ip.InternalFuncExitAnnotation","erasureStrategy":"Canonical"},"value":{"id":9,"rets":[{"s":{"namePrefix":"CANON124!!8","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.scalarization.sort","type":"vc.data.ScalarizationSort","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.ScalarizationSort.Split","idx":"2"}},{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.storage.bit-width","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":256},{"key":{"name":"tac.storage.pretty.paths","type":"analysis.storage.DisplayPaths","erasureStrategy":"Erased"},"value":{"paths":[{"#class":"analysis.storage.DisplayPath.Root","name":"_totalSupply"}]}},{"key":{"name":"tac.slot.type","type":"spec.cvlast.typedescriptors.EVMTypeDescriptor$EVMValueType","erasureStrategy":"Canonical"},"value":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256}},{"key":{"name":"tac.storage.non-indexed-path","type":"analysis.storage.StorageAnalysisResult$NonIndexedPath","erasureStrategy":"Canonical"},"value":{"#class":"analysis.storage.StorageAnalysisResult.NonIndexedPath.Root","slot":"2"}},{"key":{"name":"tac.storage","type":"java.math.BigInteger","erasureStrategy":"Canonical"},"value":"ce4604a0000000000000000000000014"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1023}]},"offset":0}],"functionLayout":{"0":{"#class":"analysis.ip.InternalFuncValueLocation.Scalar"}}}}
		AnnotationCmd:102 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.EVMFunctionReturnWrite","returnbufOffset":"0","returnValueSym":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"CANON124!!8","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.scalarization.sort","type":"vc.data.ScalarizationSort","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.ScalarizationSort.Split","idx":"2"}},{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.storage.bit-width","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":256},{"key":{"name":"tac.storage.pretty.paths","type":"analysis.storage.DisplayPaths","erasureStrategy":"Erased"},"value":{"paths":[{"#class":"analysis.storage.DisplayPath.Root","name":"_totalSupply"}]}},{"key":{"name":"tac.slot.type","type":"spec.cvlast.typedescriptors.EVMTypeDescriptor$EVMValueType","erasureStrategy":"Canonical"},"value":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256}},{"key":{"name":"tac.storage.non-indexed-path","type":"analysis.storage.StorageAnalysisResult$NonIndexedPath","erasureStrategy":"Canonical"},"value":{"#class":"analysis.storage.StorageAnalysisResult.NonIndexedPath.Root","slot":"2"}},{"key":{"name":"tac.storage","type":"java.math.BigInteger","erasureStrategy":"Canonical"},"value":"ce4604a0000000000000000000000014"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1023}]},"callIndex":9}}
		AnnotationCmd:102 JSON{"key":{"name":"tac.return.path","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		LabelCmd:102 "End procedure CurveTokenExample-totalSupply()"
		AssignExpCmd:102 tacReturndata!!453:75 Store(tacReturndata!!538:75 0x0 CANON124!!8:101 )
		AssignExpCmd:102 tacMCANON2!!454:12 Store(tacMCANON2!!535:12 0x140 CANON124!!8:101 )
		AnnotationCmd:102 JSON{"key":{"name":"call.trace.pop","type":"analysis.icfg.Inliner$CallStack$PopRecord","erasureStrategy":"Canonical"},"value":"rO0ABXNyAClhbmFseXNpcy5pY2ZnLklubGluZXIkQ2FsbFN0YWNrJFBvcFJlY29yZPAPfwSLdCWJAgABSQAIY2FsbGVlSWR4cAAAAAk="}
		JumpCmd:102 3_0_0_6_0_0
	}
	Block 1_0_0_1_0_0 Succ [0_0_0_3_0_0] {
		AssumeNotCmd:71 false
		AnnotationCmd:53 JSON{"key":{"name":"pta.fake-return.start","type":"analysis.CmdPointer","erasureStrategy":"Erased"},"value":{"block":{"#class":"tac.BlockIdentifier","origStartPc":1608,"stkTop":1009,"decompCopy":0,"calleeIdx":0,"topOfStackValue":2,"freshCopy":0},"pos":1}}
		AnnotationCmd:53 JSON{"key":{"name":"pta.fake-return.end","type":"analysis.CmdPointer","erasureStrategy":"Erased"},"value":{"block":{"#class":"tac.BlockIdentifier","origStartPc":1608,"stkTop":1009,"decompCopy":0,"calleeIdx":0,"topOfStackValue":2,"freshCopy":0},"pos":6}}
		AssumeNotCmd:126 false
		AssignExpCmd:127 R455:128 Select(tacMCANON2!!263:11 0x100 )
		NopCmd
		AssumeExpCmd LNot(Lt(R455:128 R230:69 ) )
		AssignExpCmd:129 R457:66 Sub(R455:128 R230:69 )
		AssignExpCmd:67 tacMCANON1!!458:9 Store(tacMCANON1!!229:9 0xe0 R457:66 )
		AnnotationCmd:53 JSON{"key":{"name":"pta.end-allocation","type":"analysis.alloc.AllocationAnalysis$AbstractLocation","erasureStrategy":"Erased"},"value":{"prevFPWriteIdx":1,"nextFPWriteCmd":{"block":{"#class":"tac.BlockIdentifier","origStartPc":16,"stkTop":1024,"decompCopy":0,"calleeIdx":0,"topOfStackValue":2,"freshCopy":0},"pos":44},"sort":{"#class":"analysis.alloc.AllocationAnalysis.Alloc.ConstBlock","sz":"40"}}}
		AnnotationCmd:53 JSON{"key":{"name":"internal.func.start","type":"analysis.ip.InternalFuncStartAnnotation","erasureStrategy":"CallTrace"},"value":{"id":2,"startPc":3822,"args":[],"methodSignature":{"#class":"spec.cvlast.QualifiedMethodSignature.QualifiedMethodSig","qualifiedMethodName":{"#class":"spec.cvlast.QualifiedFunction","host":{"name":"curve"},"methodId":"_A"},"params":[],"res":[{"#class":"spec.cvlast.VMParam.Unnamed","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256}}]},"stackOffsetToArgPos":{},"callSiteSrc":{"source":0,"begin":6811,"len":4,"jumpType":"ENTER","address":"ce4604a0000000000000000000000017","sourceContext":{"indexToFilepath":{"0":"contracts/curve.sol","1":"Context.sol","2":"ERC20.sol","3":"IERC20.sol","4":"IERC20Metadata.sol","5":"ReentrancyGuard.sol"},"sourceDir":".post_autofinders.1"}}}}
		AnnotationCmd:53 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet","value":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"CANON139!!10","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.scalarization.sort","type":"vc.data.ScalarizationSort","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.ScalarizationSort.Split","idx":"5"}},{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.storage.bit-width","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":256},{"key":{"name":"tac.storage.pretty.paths","type":"analysis.storage.DisplayPaths","erasureStrategy":"Erased"},"value":{"paths":[{"#class":"analysis.storage.DisplayPath.Root","name":"future_A"}]}},{"key":{"name":"tac.slot.type","type":"spec.cvlast.typedescriptors.EVMTypeDescriptor$EVMValueType","erasureStrategy":"Canonical"},"value":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256}},{"key":{"name":"tac.storage.non-indexed-path","type":"analysis.storage.StorageAnalysisResult$NonIndexedPath","erasureStrategy":"Canonical"},"value":{"#class":"analysis.storage.StorageAnalysisResult.NonIndexedPath.Root","slot":"5"}},{"key":{"name":"tac.storage","type":"java.math.BigInteger","erasureStrategy":"Canonical"},"value":"ce4604a0000000000000000000000017"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1015}]},"displayPath":{"#class":"analysis.storage.DisplayPath.Root","name":"future_A"},"storageType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256},"contractInstance":"ce4604a0000000000000000000000017","linkableStorageReadId":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet.Id","id":2}}}
		AnnotationCmd:53 JSON{"key":{"name":"internal.func.end","type":"analysis.ip.InternalFuncExitAnnotation","erasureStrategy":"Canonical"},"value":{"id":2,"rets":[{"s":{"namePrefix":"CANON139!!10","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.scalarization.sort","type":"vc.data.ScalarizationSort","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.ScalarizationSort.Split","idx":"5"}},{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.storage.bit-width","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":256},{"key":{"name":"tac.storage.pretty.paths","type":"analysis.storage.DisplayPaths","erasureStrategy":"Erased"},"value":{"paths":[{"#class":"analysis.storage.DisplayPath.Root","name":"future_A"}]}},{"key":{"name":"tac.slot.type","type":"spec.cvlast.typedescriptors.EVMTypeDescriptor$EVMValueType","erasureStrategy":"Canonical"},"value":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256}},{"key":{"name":"tac.storage.non-indexed-path","type":"analysis.storage.StorageAnalysisResult$NonIndexedPath","erasureStrategy":"Canonical"},"value":{"#class":"analysis.storage.StorageAnalysisResult.NonIndexedPath.Root","slot":"5"}},{"key":{"name":"tac.storage","type":"java.math.BigInteger","erasureStrategy":"Canonical"},"value":"ce4604a0000000000000000000000017"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1017}]},"offset":0}],"functionLayout":{"0":{"#class":"analysis.ip.InternalFuncValueLocation.Scalar"}}}}
		AssignExpCmd:130 tacMCANON2!!461:11 Store(tacMCANON2!!263:11 0x120 0x3842f77600000000000000000000000000000000000000000000000000000000 )
		AnnotationCmd:53 JSON{"key":{"name":"dsa.assign.start","type":"java.lang.String","erasureStrategy":"Erased"},"value":"4639_1009_0_0_0_0 -> 4643_1007_0_0_0_0"}
		LabelCmd:53 "Parallel assignment for R4175:bv256, R4219:bv256, B4220:bool, R4221:bv256 := R6292:bv256, R397:bv256, B4076:bool, R4077:bv256"
		AnnotationCmd:53 JSON{"key":{"name":"dsa.assign.end","type":"java.lang.String","erasureStrategy":"Erased"},"value":"4639_1009_0_0_0_0 -> 4643_1007_0_0_0_0"}
		AnnotationCmd:53 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.LoopSnippet.StartLoopSnippet","loopIndex":0,"loopSource":"unknown loop source code"}}
		AnnotationCmd:53 JSON{"key":{"name":"start_loop.cmd","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		AnnotationCmd:53 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.LoopSnippet.StartIter","iteration":1}}
		AssignExpCmd:131 R462:132 Select(tacMCANON1!!458:9 0xc0 )
		AssignExpCmd:133 tacMCANON2!!463:11 Store(tacMCANON2!!461:11 0x124 R462:132 )
		AnnotationCmd:53 JSON{"key":{"name":"dsa.assign.start","type":"java.lang.String","erasureStrategy":"Erased"},"value":"4674_1005_0_0_0_0 -> 4643_1007_0_0_0_0"}
		LabelCmd:53 "Parallel assignment for R4175:bv256, R4219:bv256, B4220:bool, R4221:bv256 := R3948:bv256, R3993:bv256, B4217:bool, R4214:bv256"
		AnnotationCmd:53 JSON{"key":{"name":"dsa.assign.end","type":"java.lang.String","erasureStrategy":"Erased"},"value":"4674_1005_0_0_0_0 -> 4643_1007_0_0_0_0"}
		AnnotationCmd:53 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.LoopSnippet.EndIter","iteration":1}}
		AnnotationCmd:53 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.LoopSnippet.StartIter","iteration":2}}
		AssignExpCmd:131 R464:132 Select(tacMCANON1!!458:9 0xe0 )
		AssignExpCmd:133 tacMCANON2!!465:11 Store(tacMCANON2!!463:11 0x144 R464:132 )
		AnnotationCmd:53 JSON{"key":{"name":"dsa.assign.start","type":"java.lang.String","erasureStrategy":"Erased"},"value":"4674_1005_0_0_0_0 -> 4643_1007_0_0_0_0"}
		LabelCmd:53 "Parallel assignment for R4175:bv256, R4219:bv256, B4220:bool, R4221:bv256 := R3948:bv256, R3993:bv256, B4217:bool, R4214:bv256"
		AnnotationCmd:53 JSON{"key":{"name":"dsa.assign.end","type":"java.lang.String","erasureStrategy":"Erased"},"value":"4674_1005_0_0_0_0 -> 4643_1007_0_0_0_0"}
		AnnotationCmd:53 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.LoopSnippet.EndIter","iteration":2}}
		AnnotationCmd:53 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.LoopSnippet.EndLoopSnippet","loopId":0}}
		AnnotationCmd:53 JSON{"key":{"name":"end_loop.cmd","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		AssignExpCmd:134 tacMCANON2!!467:11 Store(tacMCANON2!!465:11 0x164 CANON139!!10:135 )
		AssignExpCmd:130 R468:90 0x120
		NopCmd
		AssignHavocCmd:130 R470:62
		AssignHavocCmd:53 tacReturndata!!471:75
		JumpCmd:53 0_0_0_3_0_0
	}
	Block 1_0_0_6_0_0 Succ [0_0_0_8_0_0] {
		AssumeNotCmd:109 false
		AnnotationCmd:102 JSON{"key":{"name":"pta.fake-return.start","type":"analysis.CmdPointer","erasureStrategy":"Erased"},"value":{"block":{"#class":"tac.BlockIdentifier","origStartPc":1608,"stkTop":1009,"decompCopy":0,"calleeIdx":0,"topOfStackValue":2,"freshCopy":0},"pos":1}}
		AnnotationCmd:102 JSON{"key":{"name":"pta.fake-return.end","type":"analysis.CmdPointer","erasureStrategy":"Erased"},"value":{"block":{"#class":"tac.BlockIdentifier","origStartPc":1608,"stkTop":1009,"decompCopy":0,"calleeIdx":0,"topOfStackValue":2,"freshCopy":0},"pos":6}}
		AssumeNotCmd:136 false
		AssignExpCmd:137 R472:128 Select(tacMCANON2!!406:12 0x100 )
		NopCmd
		AssumeExpCmd LNot(Lt(R472:128 R373:69 ) )
		AssignExpCmd:138 R474:66 Sub(R472:128 R373:69 )
		AssignExpCmd:107 tacMCANON1!!475:10 Store(tacMCANON1!!372:10 0xe0 R474:66 )
		AnnotationCmd:102 JSON{"key":{"name":"pta.end-allocation","type":"analysis.alloc.AllocationAnalysis$AbstractLocation","erasureStrategy":"Erased"},"value":{"prevFPWriteIdx":1,"nextFPWriteCmd":{"block":{"#class":"tac.BlockIdentifier","origStartPc":16,"stkTop":1024,"decompCopy":0,"calleeIdx":0,"topOfStackValue":2,"freshCopy":0},"pos":44},"sort":{"#class":"analysis.alloc.AllocationAnalysis.Alloc.ConstBlock","sz":"40"}}}
		AnnotationCmd:102 JSON{"key":{"name":"internal.func.start","type":"analysis.ip.InternalFuncStartAnnotation","erasureStrategy":"CallTrace"},"value":{"id":7,"startPc":3822,"args":[],"methodSignature":{"#class":"spec.cvlast.QualifiedMethodSignature.QualifiedMethodSig","qualifiedMethodName":{"#class":"spec.cvlast.QualifiedFunction","host":{"name":"curve"},"methodId":"_A"},"params":[],"res":[{"#class":"spec.cvlast.VMParam.Unnamed","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256}}]},"stackOffsetToArgPos":{},"callSiteSrc":{"source":0,"begin":6811,"len":4,"jumpType":"ENTER","address":"ce4604a0000000000000000000000017","sourceContext":{"indexToFilepath":{"0":"contracts/curve.sol","1":"Context.sol","2":"ERC20.sol","3":"IERC20.sol","4":"IERC20Metadata.sol","5":"ReentrancyGuard.sol"},"sourceDir":".post_autofinders.1"}}}}
		AnnotationCmd:102 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet","value":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"CANON139!!10","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.scalarization.sort","type":"vc.data.ScalarizationSort","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.ScalarizationSort.Split","idx":"5"}},{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.storage.bit-width","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":256},{"key":{"name":"tac.storage.pretty.paths","type":"analysis.storage.DisplayPaths","erasureStrategy":"Erased"},"value":{"paths":[{"#class":"analysis.storage.DisplayPath.Root","name":"future_A"}]}},{"key":{"name":"tac.slot.type","type":"spec.cvlast.typedescriptors.EVMTypeDescriptor$EVMValueType","erasureStrategy":"Canonical"},"value":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256}},{"key":{"name":"tac.storage.non-indexed-path","type":"analysis.storage.StorageAnalysisResult$NonIndexedPath","erasureStrategy":"Canonical"},"value":{"#class":"analysis.storage.StorageAnalysisResult.NonIndexedPath.Root","slot":"5"}},{"key":{"name":"tac.storage","type":"java.math.BigInteger","erasureStrategy":"Canonical"},"value":"ce4604a0000000000000000000000017"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1015}]},"displayPath":{"#class":"analysis.storage.DisplayPath.Root","name":"future_A"},"storageType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256},"contractInstance":"ce4604a0000000000000000000000017","linkableStorageReadId":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet.Id","id":8}}}
		AnnotationCmd:102 JSON{"key":{"name":"internal.func.end","type":"analysis.ip.InternalFuncExitAnnotation","erasureStrategy":"Canonical"},"value":{"id":7,"rets":[{"s":{"namePrefix":"CANON139!!10","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.scalarization.sort","type":"vc.data.ScalarizationSort","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.ScalarizationSort.Split","idx":"5"}},{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.storage.bit-width","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":256},{"key":{"name":"tac.storage.pretty.paths","type":"analysis.storage.DisplayPaths","erasureStrategy":"Erased"},"value":{"paths":[{"#class":"analysis.storage.DisplayPath.Root","name":"future_A"}]}},{"key":{"name":"tac.slot.type","type":"spec.cvlast.typedescriptors.EVMTypeDescriptor$EVMValueType","erasureStrategy":"Canonical"},"value":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256}},{"key":{"name":"tac.storage.non-indexed-path","type":"analysis.storage.StorageAnalysisResult$NonIndexedPath","erasureStrategy":"Canonical"},"value":{"#class":"analysis.storage.StorageAnalysisResult.NonIndexedPath.Root","slot":"5"}},{"key":{"name":"tac.storage","type":"java.math.BigInteger","erasureStrategy":"Canonical"},"value":"ce4604a0000000000000000000000017"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1017}]},"offset":0}],"functionLayout":{"0":{"#class":"analysis.ip.InternalFuncValueLocation.Scalar"}}}}
		AssignExpCmd:139 tacMCANON2!!478:12 Store(tacMCANON2!!406:12 0x120 0x3842f77600000000000000000000000000000000000000000000000000000000 )
		AnnotationCmd:102 JSON{"key":{"name":"dsa.assign.start","type":"java.lang.String","erasureStrategy":"Erased"},"value":"4639_1009_0_0_0_0 -> 4643_1007_0_0_0_0"}
		LabelCmd:102 "Parallel assignment for R4175:bv256, R4219:bv256, B4220:bool, R4221:bv256 := R6292:bv256, R397:bv256, B4076:bool, R4077:bv256"
		AnnotationCmd:102 JSON{"key":{"name":"dsa.assign.end","type":"java.lang.String","erasureStrategy":"Erased"},"value":"4639_1009_0_0_0_0 -> 4643_1007_0_0_0_0"}
		AnnotationCmd:102 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.LoopSnippet.StartLoopSnippet","loopIndex":2,"loopSource":"unknown loop source code"}}
		AnnotationCmd:102 JSON{"key":{"name":"start_loop.cmd","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		AnnotationCmd:102 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.LoopSnippet.StartIter","iteration":1}}
		AssignExpCmd:140 R479:132 Select(tacMCANON1!!475:10 0xc0 )
		AssignExpCmd:141 tacMCANON2!!480:12 Store(tacMCANON2!!478:12 0x124 R479:132 )
		AnnotationCmd:102 JSON{"key":{"name":"dsa.assign.start","type":"java.lang.String","erasureStrategy":"Erased"},"value":"4674_1005_0_0_0_0 -> 4643_1007_0_0_0_0"}
		LabelCmd:102 "Parallel assignment for R4175:bv256, R4219:bv256, B4220:bool, R4221:bv256 := R3948:bv256, R3993:bv256, B4217:bool, R4214:bv256"
		AnnotationCmd:102 JSON{"key":{"name":"dsa.assign.end","type":"java.lang.String","erasureStrategy":"Erased"},"value":"4674_1005_0_0_0_0 -> 4643_1007_0_0_0_0"}
		AnnotationCmd:102 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.LoopSnippet.EndIter","iteration":1}}
		AnnotationCmd:102 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.LoopSnippet.StartIter","iteration":2}}
		AssignExpCmd:140 R481:132 Select(tacMCANON1!!475:10 0xe0 )
		AssignExpCmd:141 tacMCANON2!!482:12 Store(tacMCANON2!!480:12 0x144 R481:132 )
		AnnotationCmd:102 JSON{"key":{"name":"dsa.assign.start","type":"java.lang.String","erasureStrategy":"Erased"},"value":"4674_1005_0_0_0_0 -> 4643_1007_0_0_0_0"}
		LabelCmd:102 "Parallel assignment for R4175:bv256, R4219:bv256, B4220:bool, R4221:bv256 := R3948:bv256, R3993:bv256, B4217:bool, R4214:bv256"
		AnnotationCmd:102 JSON{"key":{"name":"dsa.assign.end","type":"java.lang.String","erasureStrategy":"Erased"},"value":"4674_1005_0_0_0_0 -> 4643_1007_0_0_0_0"}
		AnnotationCmd:102 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.LoopSnippet.EndIter","iteration":2}}
		AnnotationCmd:102 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.LoopSnippet.EndLoopSnippet","loopId":2}}
		AnnotationCmd:102 JSON{"key":{"name":"end_loop.cmd","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		AssignExpCmd:142 tacMCANON2!!484:12 Store(tacMCANON2!!482:12 0x164 CANON139!!10:135 )
		AssignExpCmd:139 R485:90 0x120
		NopCmd
		AssignHavocCmd:139 R487:62
		AssignHavocCmd:102 tacReturndata!!488:75
		JumpCmd:102 0_0_0_8_0_0
	}
	Block 3_0_0_1_0_0 Succ [4_0_0_0_0_0] {
		AssumeNotCmd:143 false
		AnnotationCmd:53 JSON{"key":{"name":"pta.fake-return.start","type":"analysis.CmdPointer","erasureStrategy":"Erased"},"value":{"block":{"#class":"tac.BlockIdentifier","origStartPc":3278,"stkTop":1016,"decompCopy":0,"calleeIdx":0,"topOfStackValue":2,"freshCopy":0},"pos":1}}
		AnnotationCmd:53 JSON{"key":{"name":"pta.fake-return.end","type":"analysis.CmdPointer","erasureStrategy":"Erased"},"value":{"block":{"#class":"tac.BlockIdentifier","origStartPc":3278,"stkTop":1016,"decompCopy":0,"calleeIdx":0,"topOfStackValue":2,"freshCopy":0},"pos":6}}
		AssumeNotCmd:126 false
		AssignExpCmd:127 R489:144 Select(tacMCANON2!!311:11 0x140 )
		NopCmd
		AssumeExpCmd Apply(mul_noofl:bif R519:64 0x8ac7230489e80000)
		NopCmd
		AssignExpCmd:145 I498:51 IntMul(Apply(safe_math_promotion:bif R519:64) 0x8ac7230489e80000)
		NopCmd
		NopCmd
		AssumeExpCmd Gt(R489:144 0x0 )
		AssignExpCmd:146 R501:147 Div(Apply(safe_math_narrow:bif I498:51) R489:144 )
		AnnotationCmd:53 JSON{"key":{"name":"internal.func.end","type":"analysis.ip.InternalFuncExitAnnotation","erasureStrategy":"Canonical"},"value":{"id":0,"rets":[{"s":{"namePrefix":"R501","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1023}]},"offset":0}],"functionLayout":{"0":{"#class":"analysis.ip.InternalFuncValueLocation.Scalar"}}}}
		AnnotationCmd:53 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.EVMFunctionReturnWrite","returnbufOffset":"0","returnValueSym":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R501","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1023}]},"callIndex":1}}
		AnnotationCmd:53 JSON{"key":{"name":"tac.return.path","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		LabelCmd:53 "End procedure curve-getVirtualPrice()"
		NopCmd
		AnnotationCmd:53 JSON{"key":{"name":"call.trace.pop","type":"analysis.icfg.Inliner$CallStack$PopRecord","erasureStrategy":"Canonical"},"value":"rO0ABXNyAClhbmFseXNpcy5pY2ZnLklubGluZXIkQ2FsbFN0YWNrJFBvcFJlY29yZPAPfwSLdCWJAgABSQAIY2FsbGVlSWR4cAAAAAE="}
	}
	Block 3_0_0_6_0_0 Succ [6_0_0_0_0_0] {
		AssumeNotCmd:148 false
		AnnotationCmd:102 JSON{"key":{"name":"pta.fake-return.start","type":"analysis.CmdPointer","erasureStrategy":"Erased"},"value":{"block":{"#class":"tac.BlockIdentifier","origStartPc":3278,"stkTop":1016,"decompCopy":0,"calleeIdx":0,"topOfStackValue":2,"freshCopy":0},"pos":1}}
		AnnotationCmd:102 JSON{"key":{"name":"pta.fake-return.end","type":"analysis.CmdPointer","erasureStrategy":"Erased"},"value":{"block":{"#class":"tac.BlockIdentifier","origStartPc":3278,"stkTop":1016,"decompCopy":0,"calleeIdx":0,"topOfStackValue":2,"freshCopy":0},"pos":6}}
		AssumeNotCmd:136 false
		AssignExpCmd:137 R504:144 Select(tacMCANON2!!454:12 0x140 )
		NopCmd
		AssumeExpCmd Apply(mul_noofl:bif R529:64 0x8ac7230489e80000)
		NopCmd
		AssignExpCmd:149 I513:51 IntMul(Apply(safe_math_promotion:bif R529:64) 0x8ac7230489e80000)
		NopCmd
		NopCmd
		AssumeExpCmd Gt(R504:144 0x0 )
		AssignExpCmd:150 R516:147 Div(Apply(safe_math_narrow:bif I513:51) R504:144 )
		AnnotationCmd:102 JSON{"key":{"name":"internal.func.end","type":"analysis.ip.InternalFuncExitAnnotation","erasureStrategy":"Canonical"},"value":{"id":5,"rets":[{"s":{"namePrefix":"R516","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1023}]},"offset":0}],"functionLayout":{"0":{"#class":"analysis.ip.InternalFuncValueLocation.Scalar"}}}}
		AnnotationCmd:102 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.EVMFunctionReturnWrite","returnbufOffset":"0","returnValueSym":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R516","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1023}]},"callIndex":6}}
		AnnotationCmd:102 JSON{"key":{"name":"tac.return.path","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		LabelCmd:102 "End procedure curve-getVirtualPrice()"
		NopCmd
		AnnotationCmd:102 JSON{"key":{"name":"call.trace.pop","type":"analysis.icfg.Inliner$CallStack$PopRecord","erasureStrategy":"Canonical"},"value":"rO0ABXNyAClhbmFseXNpcy5pY2ZnLklubGluZXIkQ2FsbFN0YWNrJFBvcFJlY29yZPAPfwSLdCWJAgABSQAIY2FsbGVlSWR4cAAAAAY="}
	}
	Block 2_0_0_1_0_0 Succ [0_0_0_4_0_0] {
		AssumeNotCmd:130 false
		AnnotationCmd:53 JSON{"key":{"name":"pta.fake-return.start","type":"analysis.CmdPointer","erasureStrategy":"Erased"},"value":{"block":{"#class":"tac.BlockIdentifier","origStartPc":3129,"stkTop":1017,"decompCopy":0,"calleeIdx":0,"topOfStackValue":2,"freshCopy":0},"pos":1}}
		AnnotationCmd:53 JSON{"key":{"name":"pta.fake-return.end","type":"analysis.CmdPointer","erasureStrategy":"Erased"},"value":{"block":{"#class":"tac.BlockIdentifier","origStartPc":3129,"stkTop":1017,"decompCopy":0,"calleeIdx":0,"topOfStackValue":2,"freshCopy":0},"pos":6}}
		AssumeNotCmd:126 false
		AssignExpCmd:127 R519:64 Select(tacMCANON2!!297:11 0x120 )
		AssignExpCmd:53 B521:51 Le(CANON57!!22:151 0xffffffffffffffffffffffffffffffffffffffff )
		AssignExpCmd:53 B522:51 Ge(CANON57!!22:151 0x0 )
		NopCmd
		AssumeExpCmd LAnd(B521:51 B522:51 )
		AnnotationCmd:53 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet","value":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"CANON57!!22","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.scalarization.sort","type":"vc.data.ScalarizationSort","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.ScalarizationSort.Packed","packedStart":{"#class":"vc.data.ScalarizationSort.Split","idx":"c"},"start":0}},{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.storage.bit-width","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":160},{"key":{"name":"tac.storage.pretty.paths","type":"analysis.storage.DisplayPaths","erasureStrategy":"Erased"},"value":{"paths":[{"#class":"analysis.storage.DisplayPath.Root","name":"lp_token"}]}},{"key":{"name":"tac.slot.type","type":"spec.cvlast.typedescriptors.EVMTypeDescriptor$EVMValueType","erasureStrategy":"Canonical"},"value":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.address"}},{"key":{"name":"tac.storage.non-indexed-path","type":"analysis.storage.StorageAnalysisResult$NonIndexedPath","erasureStrategy":"Canonical"},"value":{"#class":"analysis.storage.StorageAnalysisResult.NonIndexedPath.Root","slot":"c"}},{"key":{"name":"tac.storage","type":"java.math.BigInteger","erasureStrategy":"Canonical"},"value":"ce4604a0000000000000000000000017"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1018}]},"displayPath":{"#class":"analysis.storage.DisplayPath.Root","name":"lp_token"},"storageType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.address"},"contractInstance":"ce4604a0000000000000000000000017","linkableStorageReadId":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet.Id","id":3}}}
		AnnotationCmd:53 JSON{"key":{"name":"init.reorder.fence","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		AssignExpCmd:143 tacMCANON2!!525:11 Store(tacMCANON2!!297:11 0x140 0x18160ddd00000000000000000000000000000000000000000000000000000000 )
		AssignExpCmd:143 R526:147 0x140
		AssignHavocCmd:143 R527:64
		AssignHavocCmd:53 tacReturndata!!528:75
		JumpCmd:53 0_0_0_4_0_0
	}
	Block 2_0_0_6_0_0 Succ [0_0_0_9_0_0] {
		AssumeNotCmd:139 false
		AnnotationCmd:102 JSON{"key":{"name":"pta.fake-return.start","type":"analysis.CmdPointer","erasureStrategy":"Erased"},"value":{"block":{"#class":"tac.BlockIdentifier","origStartPc":3129,"stkTop":1017,"decompCopy":0,"calleeIdx":0,"topOfStackValue":2,"freshCopy":0},"pos":1}}
		AnnotationCmd:102 JSON{"key":{"name":"pta.fake-return.end","type":"analysis.CmdPointer","erasureStrategy":"Erased"},"value":{"block":{"#class":"tac.BlockIdentifier","origStartPc":3129,"stkTop":1017,"decompCopy":0,"calleeIdx":0,"topOfStackValue":2,"freshCopy":0},"pos":6}}
		AssumeNotCmd:136 false
		AssignExpCmd:137 R529:64 Select(tacMCANON2!!440:12 0x120 )
		AssignExpCmd:102 B531:51 Le(CANON57!!22:151 0xffffffffffffffffffffffffffffffffffffffff )
		AssignExpCmd:102 B532:51 Ge(CANON57!!22:151 0x0 )
		NopCmd
		AssumeExpCmd LAnd(B531:51 B532:51 )
		AnnotationCmd:102 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet","value":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"CANON57!!22","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.scalarization.sort","type":"vc.data.ScalarizationSort","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.ScalarizationSort.Packed","packedStart":{"#class":"vc.data.ScalarizationSort.Split","idx":"c"},"start":0}},{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.storage.bit-width","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":160},{"key":{"name":"tac.storage.pretty.paths","type":"analysis.storage.DisplayPaths","erasureStrategy":"Erased"},"value":{"paths":[{"#class":"analysis.storage.DisplayPath.Root","name":"lp_token"}]}},{"key":{"name":"tac.slot.type","type":"spec.cvlast.typedescriptors.EVMTypeDescriptor$EVMValueType","erasureStrategy":"Canonical"},"value":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.address"}},{"key":{"name":"tac.storage.non-indexed-path","type":"analysis.storage.StorageAnalysisResult$NonIndexedPath","erasureStrategy":"Canonical"},"value":{"#class":"analysis.storage.StorageAnalysisResult.NonIndexedPath.Root","slot":"c"}},{"key":{"name":"tac.storage","type":"java.math.BigInteger","erasureStrategy":"Canonical"},"value":"ce4604a0000000000000000000000017"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1018}]},"displayPath":{"#class":"analysis.storage.DisplayPath.Root","name":"lp_token"},"storageType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.address"},"contractInstance":"ce4604a0000000000000000000000017","linkableStorageReadId":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet.Id","id":9}}}
		AnnotationCmd:102 JSON{"key":{"name":"init.reorder.fence","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		AssignExpCmd:148 tacMCANON2!!535:12 Store(tacMCANON2!!440:12 0x140 0x18160ddd00000000000000000000000000000000000000000000000000000000 )
		AssignExpCmd:148 R536:147 0x140
		AssignHavocCmd:148 R537:64
		AssignHavocCmd:102 tacReturndata!!538:75
		JumpCmd:102 0_0_0_9_0_0
	}
	Block 4_0_0_0_0_0 Succ [0_0_0_5_0_0] {
		AssumeNotCmd:53 false
		AssumeNotCmd:53 false
		AnnotationCmd JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageGlobalChangeSnippet.StorageTakeSnapshot","lhs":{"namePrefix":"lastStorage","tag":{"#class":"tac.Tag.BlockchainState"},"callIndex":0,"meta":[{"key":{"name":"cvl.local","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true},{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"lastStorage"},{"key":{"name":"cvl.type","type":"spec.cvlast.CVLType$PureCVLType","erasureStrategy":"CallTrace"},"value":{"#class":"spec.cvlast.CVLType.PureCVLType.VMInternal.BlockchainState"}},{"key":{"name":"cvl","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true},{"key":{"name":"cvl.display","type":"java.lang.String","erasureStrategy":"CallTrace"},"value":"lastStorage"}]}}}
		AssignExpCmd:152 CANON179!!539:153 Eq(I24 R501:147 )
		AssumeCmd:53 CANON179!!539:153
		AnnotationCmd:53 JSON{"key":{"name":"cvl.label.end","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		AnnotationCmd:154 JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Cmd","cmd":{"cmd_type":"spec.cvlast.CVLCmd.Simple.Apply","cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/specs/ViewReentrancy.spec","start":{"line":27,"character":4},"end":{"line":27,"character":15}},"exp":{"#class":"spec.cvlast.CVLExp.ApplyExp.ContractFunction.Symbolic","methodIdWithCallContext":{"#class":"spec.cvlast.ParametricMethod","methodId":"f","host":{"name":"curve"}},"args":[{"#class":"spec.cvlast.CVLExp.VariableExp","id":"e","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":0}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"env","fields":[{"fieldName":"msg","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"msg","fields":[{"fieldName":"sender","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"value","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}}]}},{"fieldName":"tx","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"tx","fields":[{"fieldName":"origin","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}}]}},{"fieldName":"block","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"block","fields":[{"fieldName":"coinbase","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"difficulty","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"gaslimit","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"number","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"timestamp","value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}}]}}]},"cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/specs/ViewReentrancy.spec","start":{"line":27,"character":4},"end":{"line":27,"character":15}}},"twoStateIndex":"NEITHER"},{"#class":"spec.cvlast.CVLExp.VariableExp","id":"data","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":0}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.VMInternal.RawArgs"},"cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/specs/ViewReentrancy.spec","start":{"line":27,"character":4},"end":{"line":27,"character":15}}},"twoStateIndex":"NEITHER"}],"noRevert":true,"storage":{"#class":"spec.cvlast.CVLExp.VariableExp","id":"lastStorage","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":0}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.VMInternal.BlockchainState"},"cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/specs/ViewReentrancy.spec","start":{"line":27,"character":4},"end":{"line":27,"character":15}}},"twoStateIndex":"NEITHER"},"tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":0}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Void"},"cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/specs/ViewReentrancy.spec","start":{"line":27,"character":4},"end":{"line":27,"character":5}}}},"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":0}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}}}}}
		NopCmd
		NopCmd
		NopCmd
		NopCmd
		NopCmd
		AssignExpCmd R545:155 CANON186:8
		AnnotationCmd:154 JSON{"key":{"name":"call.trace.push","type":"analysis.icfg.Inliner$CallStack$PushRecord","erasureStrategy":"Canonical"},"value":"rO0ABXNyACphbmFseXNpcy5pY2ZnLklubGluZXIkQ2FsbFN0YWNrJFB1c2hSZWNvcmSX8+DCTLCH+AIAA0kACGNhbGxlZUlkTAAGY2FsbGVldAATTHZjL2RhdGEvTWV0aG9kUmVmO0wAB3N1bW1hcnl0ABVMdmMvZGF0YS9DYWxsU3VtbWFyeTt4cAAAAAVzcgARdmMuZGF0YS5NZXRob2RSZWbJlJTzzU9pGAIAA0wABGF0dHJ0ABdMc2NlbmUvTWV0aG9kQXR0cmlidXRlO0wACmNvbnRyYWN0SWR0ABZMamF2YS9tYXRoL0JpZ0ludGVnZXI7TAAHc2lnSGFzaHQAEExldm0vU2lnaGFzaEludDt4cHNyABxzY2VuZS5NZXRob2RBdHRyaWJ1dGUkQ29tbW9uNHjdebdr9XMCAAB4cgAVc2NlbmUuTWV0aG9kQXR0cmlidXRlcYg2pYWutuUCAAB4cHNyABRqYXZhLm1hdGguQmlnSW50ZWdlcoz8nx+pO/sdAwAGSQAIYml0Q291bnRJAAliaXRMZW5ndGhJABNmaXJzdE5vbnplcm9CeXRlTnVtSQAMbG93ZXN0U2V0Qml0SQAGc2lnbnVtWwAJbWFnbml0dWRldAACW0J4cgAQamF2YS5sYW5nLk51bWJlcoaslR0LlOCLAgAAeHD///////////////7////+AAAAAXVyAAJbQqzzF/gGCFTgAgAAeHAAAAAQzkYEoAAAAAAAAAAAAAAAF3hzcgAOZXZtLlNpZ2hhc2hJbnRUdcqNMXEgeAIAAUwAAW5xAH4ABnhwc3EAfgAM///////////////+/////gAAAAF1cQB+ABAAAAAEgsYwZnhw"}
		NopCmd
		AssumeExpCmd Ge(R545:156 0x4 )
		NopCmd
		AssumeExpCmd Ge(0x7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff R545:156 )
		AssignExpCmd:154 B550 LAnd(Ge(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff CANON58:22 ) Le(0x0 CANON58:22 ) )
		AssertCmd:154 B550 "sanity bounds check on cvl to vm encoding of tacTmp!4972:int failed"
		AssignExpCmd:154 R551:51 Apply(safe_math_narrow:bif CANON58:22)
		NopCmd
		AssumeExpCmd LAnd(Le(R551:54 0xffffffffffffffffffffffffffffffffffffffff ) Ge(R551:54 0x0 ) )
		AssignExpCmd:154 B555 LAnd(Ge(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff CANON59:23 ) Le(0x0 CANON59:23 ) )
		AssertCmd:154 B555 "sanity bounds check on cvl to vm encoding of tacTmp!4975:int failed"
		AssignExpCmd:154 R556:51 Apply(safe_math_narrow:bif CANON59:23)
		NopCmd
		AssumeExpCmd LAnd(Le(R556:55 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff ) Ge(R556:55 0x0 ) )
		AssignExpCmd:154 B561 LAnd(Ge(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff CANON60:24 ) Le(0x0 CANON60:24 ) )
		AssertCmd:154 B561 "sanity bounds check on cvl to vm encoding of tacTmp!4979:int failed"
		AssignExpCmd:154 R562:51 Apply(safe_math_narrow:bif CANON60:24)
		NopCmd
		AssumeExpCmd LAnd(Le(R562:56 0xffffffffffffffffffffffffffffffffffffffff ) Ge(R562:56 0x0 ) )
		AssignExpCmd:154 B566 LAnd(Ge(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff CANON64:28 ) Le(0x0 CANON64:28 ) )
		AssertCmd:154 B566 "sanity bounds check on cvl to vm encoding of tacTmp!4982:int failed"
		AssignExpCmd:154 R567:51 Apply(safe_math_narrow:bif CANON64:28)
		NopCmd
		AssumeExpCmd LAnd(Le(R567:57 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff ) Ge(R567:57 0x0 ) )
		AssignExpCmd:154 B571 LAnd(Ge(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff CANON65:29 ) Le(0x0 CANON65:29 ) )
		AssertCmd:154 B571 "sanity bounds check on cvl to vm encoding of tacTmp!4985:int failed"
		AssignExpCmd:154 R572:51 Apply(safe_math_narrow:bif CANON65:29)
		NopCmd
		AssumeExpCmd LAnd(Le(R572:58 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff ) Ge(R572:58 0x0 ) )
		AssignExpCmd:154 B576 LAnd(Ge(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff CANON59:23 ) Le(0x0 CANON59:23 ) )
		AssertCmd:154 B576 "sanity bounds check on cvl to vm encoding of tacTmp!4988:int failed"
		AssignExpCmd:154 R577:51 Apply(safe_math_narrow:bif CANON59:23)
		AssignExpCmd:154 B579 LAnd(Ge(0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff CANON58:22 ) Le(0x0 CANON58:22 ) )
		AssertCmd:154 B579 "sanity bounds check on cvl to vm encoding of tacTmp!4991:int failed"
		AssignExpCmd:154 R580:51 Apply(safe_math_narrow:bif CANON58:22)
		AssignExpCmd:154 R583:51 Select(tacBalance!!212:15 Apply(to_skey:bif R580:51) )
		AssignExpCmd:157 I584:51 IntSub(R583:51 R577:51 )
		AssignExpCmd:157 tacBalance!!585:15 Store(tacBalance!!212:15 Apply(to_skey:bif R580:51) I584:51 )
		AssignExpCmd:154 R586:51 Select(tacBalance!!585:15 Apply(to_skey:bif R27:40) )
		AssignExpCmd:157 R587:51 Add(R586:51 R577:51)
		NopCmd
		AssumeExpCmd Apply(add_noofl:bif R586:51 R577:51)
		AssignExpCmd:157 tacBalance!!589:15 Store(tacBalance!!585:15 Apply(to_skey:bif R27:40) R587:51 )
		AnnotationCmd:154 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.BalanceSnippet","srcAccountInfo":{"old":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R583","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}]},"new":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"I584","tag":{"#class":"tac.Tag.Int"},"callIndex":0,"meta":[{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}]},"addr":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R580","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}]}},"trgAccountInfo":{"old":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R586","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}]},"new":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R587","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}]},"addr":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R27","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"tacContractAt"},{"key":{"name":"tac.contract.sym.addr.name","type":"java.lang.String","erasureStrategy":"Erased"},"value":"curve"},{"key":{"name":"tac.contract.sym.addr","type":"java.math.BigInteger","erasureStrategy":"Erased"},"value":"ce4604a0000000000000000000000017"}]}},"transferredAmount":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R577","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}]}}}
		JumpCmd 0_0_0_5_0_0
	}
	Block 6_0_0_0_0_0 Succ [] {
		AssumeNotCmd:102 false
		AssumeNotCmd:102 false
		AnnotationCmd JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageGlobalChangeSnippet.StorageTakeSnapshot","lhs":{"namePrefix":"lastStorage","tag":{"#class":"tac.Tag.BlockchainState"},"callIndex":0,"meta":[{"key":{"name":"cvl.local","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true},{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"lastStorage"},{"key":{"name":"cvl.type","type":"spec.cvlast.CVLType$PureCVLType","erasureStrategy":"CallTrace"},"value":{"#class":"spec.cvlast.CVLType.PureCVLType.VMInternal.BlockchainState"}},{"key":{"name":"cvl","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true},{"key":{"name":"cvl.display","type":"java.lang.String","erasureStrategy":"CallTrace"},"value":"lastStorage"}]}}}
		AssignExpCmd:158 CANON266!!590:153 Eq(I11 R516:147 )
		AssumeCmd:102 CANON266!!590:153
		AnnotationCmd:102 JSON{"key":{"name":"cvl.label.end","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		AnnotationCmd:159 JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Cmd","cmd":{"cmd_type":"spec.cvlast.CVLCmd.Simple.Assert","cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/specs/ViewReentrancy.spec","start":{"line":29,"character":4},"end":{"line":29,"character":16}},"exp":{"#class":"spec.cvlast.CVLExp.VariableExp","id":"cond","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":0}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"},"cvlRange":{"#class":"spec.cvlast.CVLRange.Range","specFile":"certora/specs/ViewReentrancy.spec","start":{"line":29,"character":4},"end":{"line":29,"character":16}}},"twoStateIndex":"NEITHER"},"description":"","scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":0}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}}}}}
		AssertCmd:160 B23 ""
		AnnotationCmd:159 JSON{"key":{"name":"cvl.label.end","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
	}
	Block 0_0_0_5_0_0 Succ [5_0_0_0_0_0] {
		LabelCmd "Start procedure curve-lp_token()"
		AnnotationCmd JSON{"key":{"name":"fps.free-pointer-is-scalarized","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true}
		AssignExpCmd R592:51 Select(tacExtcodesize!!6:3 Apply(to_skey:bif R27:60) )
		NopCmd
		AssumeExpCmd Gt(R592:51 0x0 )
		AnnotationCmd JSON{"key":{"name":"internal.func.finder.info","type":"analysis.ip.InternalFunctionFinderReport","erasureStrategy":"Erased"},"value":"rO0ABXNyAChhbmFseXNpcy5pcC5JbnRlcm5hbEZ1bmN0aW9uRmluZGVyUmVwb3J0ian+bYn1VdACAAFMABN1bnJlc29sdmVkRnVuY3Rpb25zdAAPTGphdmEvdXRpbC9TZXQ7eHBzcgAhZGF0YXN0cnVjdHVyZXMuTGlua2VkQXJyYXlIYXNoU2V0AAAAAAAAAAEDAAJGAApsb2FkRmFjdG9yTAAJaGFzaFRhYmxldAAuTGRhdGFzdHJ1Y3R1cmVzL2FycmF5aGFzaHRhYmxlL0FycmF5SGFzaFRhYmxlO3hwdwgAAAAAQAAAAHg="}
		AnnotationCmd JSON{"key":{"name":"fps.free-pointer-is-scalarized","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true}
		NopCmd
		AssumeExpCmd Eq(R556:55 0x0 )
		NopCmd
		AssumeExpCmd LNot(Lt(R545:156 0x4 ) )
		NopCmd
		AssumeExpCmd LNot(Gt(0x82c63066 tacSighash!!35:44 ) )
		NopCmd
		AssumeExpCmd Eq(0x82c63066 tacSighash!!35:44 )
		AssignExpCmd B599:51 Le(CANON57!!22:161 0xffffffffffffffffffffffffffffffffffffffff )
		AssignExpCmd B600:51 Ge(CANON57!!22:161 0x0 )
		NopCmd
		AssumeExpCmd LAnd(B599:51 B600:51 )
		AnnotationCmd JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet","value":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"CANON57!!22","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.scalarization.sort","type":"vc.data.ScalarizationSort","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.ScalarizationSort.Packed","packedStart":{"#class":"vc.data.ScalarizationSort.Split","idx":"c"},"start":0}},{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.storage.bit-width","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":160},{"key":{"name":"tac.storage.pretty.paths","type":"analysis.storage.DisplayPaths","erasureStrategy":"Erased"},"value":{"paths":[{"#class":"analysis.storage.DisplayPath.Root","name":"lp_token"}]}},{"key":{"name":"tac.slot.type","type":"spec.cvlast.typedescriptors.EVMTypeDescriptor$EVMValueType","erasureStrategy":"Canonical"},"value":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.address"}},{"key":{"name":"tac.storage.non-indexed-path","type":"analysis.storage.StorageAnalysisResult$NonIndexedPath","erasureStrategy":"Canonical"},"value":{"#class":"analysis.storage.StorageAnalysisResult.NonIndexedPath.Root","slot":"c"}},{"key":{"name":"tac.storage","type":"java.math.BigInteger","erasureStrategy":"Canonical"},"value":"ce4604a0000000000000000000000017"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1021}]},"displayPath":{"#class":"analysis.storage.DisplayPath.Root","name":"lp_token"},"storageType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.address"},"contractInstance":"ce4604a0000000000000000000000017","linkableStorageReadId":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet.Id","id":5}}}
		AnnotationCmd JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.EVMFunctionReturnWrite","returnbufOffset":"0","returnValueSym":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"CANON57!!22","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.scalarization.sort","type":"vc.data.ScalarizationSort","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.ScalarizationSort.Packed","packedStart":{"#class":"vc.data.ScalarizationSort.Split","idx":"c"},"start":0}},{"key":{"name":"Tac.symbol.keyword","type":"java.lang.String","erasureStrategy":"Canonical"},"value":"L"},{"key":{"name":"tac.storage.bit-width","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":160},{"key":{"name":"tac.storage.pretty.paths","type":"analysis.storage.DisplayPaths","erasureStrategy":"Erased"},"value":{"paths":[{"#class":"analysis.storage.DisplayPath.Root","name":"lp_token"}]}},{"key":{"name":"tac.slot.type","type":"spec.cvlast.typedescriptors.EVMTypeDescriptor$EVMValueType","erasureStrategy":"Canonical"},"value":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.address"}},{"key":{"name":"tac.storage.non-indexed-path","type":"analysis.storage.StorageAnalysisResult$NonIndexedPath","erasureStrategy":"Canonical"},"value":{"#class":"analysis.storage.StorageAnalysisResult.NonIndexedPath.Root","slot":"c"}},{"key":{"name":"tac.storage","type":"java.math.BigInteger","erasureStrategy":"Canonical"},"value":"ce4604a0000000000000000000000017"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1009}]},"callIndex":5}}
		AnnotationCmd JSON{"key":{"name":"tac.return.path","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		LabelCmd "End procedure curve-lp_token()"
		JumpCmd 5_0_0_0_0_0
	}
	Block 5_0_0_0_0_0 Succ [0_0_0_6_0_0] {
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
        "name": "Tac.symbol.keyword",
        "type": "java.lang.String",
        "erasureStrategy": "Canonical"
      },
      "value": "tacCalldatasize"
    }
  ],
  "3": [
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
  "5": [
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
  "7": [
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
  "8": [
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
      "value": 1
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
      "value": 5
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
      "value": 2
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
      "value": 6
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
      "value": 3
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
      "value": 7
    }
  ],
  "15": [
    {
      "key": {
        "name": "Tac.symbol.keyword",
        "type": "java.lang.String",
        "erasureStrategy": "Canonical"
      },
      "value": "tacBalance"
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
  "21": [
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
  "38": [
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
  "39": [
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
  "40": [
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
      "value": "ce4604a0000000000000000000000017"
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
      "value": "ce4604a0000000000000000000000017"
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
      "value": "ce4604a0000000000000000000000004"
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
              "namePrefix": "R254",
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
                "namePrefix": "R254",
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
      "value": "ce4604a0000000000000000000000014"
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
      "value": "rO0ABXNyADJhbmFseXNpcy5pY2ZnLkNhbGxHcmFwaEJ1aWxkZXIkQ29udHJhY3RTdG9yYWdlUmVhZLRpTKYiS4EFAgABSQACaWR4cAAAAAc="
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
              "namePrefix": "R397",
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
                "namePrefix": "R397",
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
                "callIndex": 7,
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
                "callIndex": 7,
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
          "callIndex": 8,
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
            "namePrefix": "I24",
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
            "namePrefix": "I503",
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
  "157": [
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
  "158": [
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
            "namePrefix": "I11",
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
            "namePrefix": "I518",
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
  "159": [
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
  "160": [
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
  "161": [
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
      "value": 1021
    }
  ]
}