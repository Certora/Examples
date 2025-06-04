/**
 * @title  Reasoning about Solidity events example
 *
 * This is an example specification for reasoning about events in CVL.
 */

methods {
    function emitBidEvent(address from) internal => cvlEmitBidEvent(from); 
}

persistent ghost bool isEventEmitted;
persistent ghost address emittedEventAddress;

function cvlEmitBidEvent(address from){
    isEventEmitted = true;
    emittedEventAddress = from;
}

/**
 * This rule checks that an event is emitted
 */
rule eventIsEmitted() {
    env e;
    isEventEmitted = false;
    bid(e);
    assert isEventEmitted;
}

/**
 * This rule checks that the emitted event address is the one
 * that initiated the bid operation. 
 */
rule eventEmitsMsgSender() {
    env e;
    bid(e);
    assert emittedEventAddress == e.msg.sender;
}