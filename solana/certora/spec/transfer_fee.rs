use std::cmp;
use cvt;
use crate::extension::transfer_fee::{MAX_FEE_BASIS_POINTS, ONE_IN_BASIS_POINTS};

/// Calculate ceiling-division
///
/// Ceiling-division
///     `ceil[ numerator / denominator ]`
/// can be represented as a floor-division
///     `floor[ (numerator + denominator - 1) / denominator]`
fn ceil_div(numerator: u128, denominator: u128) -> Option<u128> {
    numerator
        .checked_add(denominator)?
        .checked_sub(1)?
        .checked_div(denominator)
}

 /// Calculate the transfer fee
 #[inline(never)]
 pub fn calculate_fee(pre_fee_amount: u64, transfer_fee_basis_points: u128, maximum_fee: u64) -> Option<u64> {
     if transfer_fee_basis_points == 0 || pre_fee_amount == 0 {
         Some(0)
     } else {
         let numerator = (pre_fee_amount as u128).checked_mul(transfer_fee_basis_points)?;
         let raw_fee = ceil_div(numerator, ONE_IN_BASIS_POINTS)?
             .try_into() // guaranteed to be okay
             .ok()?;

         Some(cmp::min(raw_fee, maximum_fee))
     }
 }

#[no_mangle]
pub fn additivity_of_fee() {
    let pre_fee_amount_x: u64 = cvt::nondet();
    let pre_fee_amount_y: u64 = cvt::nondet();
    let transfer_fee_basic_points = cvt::CVT_nondet_i64() as u128;
    cvt::CVT_assume(transfer_fee_basic_points <= MAX_FEE_BASIS_POINTS as u128);
    let maximum_fee: u64 = cvt::nondet();

    let pre_fee_amount_xy = pre_fee_amount_x.checked_add(pre_fee_amount_y).unwrap();
    let fee_xy = calculate_fee(pre_fee_amount_xy, transfer_fee_basic_points, maximum_fee).unwrap();

    let fee_x  = calculate_fee(pre_fee_amount_x, transfer_fee_basic_points, maximum_fee).unwrap();
    let fee_y  = calculate_fee(pre_fee_amount_y, transfer_fee_basic_points, maximum_fee).unwrap();

    cvt::CVT_assert(fee_x.checked_add(fee_y).unwrap() >= fee_xy);
}

#[no_mangle]
pub fn maximum_fee() {
    let pre_fee_amount_x: u64 = cvt::nondet();
    let transfer_fee_basic_points = cvt::CVT_nondet_i64() as u128;
    cvt::CVT_assume(transfer_fee_basic_points <= MAX_FEE_BASIS_POINTS as u128);
    let maximum_fee: u64 = cvt::nondet();
    
    let fee  = calculate_fee(pre_fee_amount_x, transfer_fee_basic_points, maximum_fee).unwrap();
    cvt::CVT_assert(fee <= maximum_fee);
}

#[no_mangle]
pub fn monotonicity_of_fee() {
    let pre_fee_amount_x: u64 = cvt::nondet();
    let pre_fee_amount_y: u64 = cvt::nondet();
    let transfer_fee_basic_points = cvt::CVT_nondet_i64() as u128;
    cvt::CVT_assume(transfer_fee_basic_points <= MAX_FEE_BASIS_POINTS as u128);
    let maximum_fee: u64 = cvt::nondet();

    cvt::CVT_assume(pre_fee_amount_x > pre_fee_amount_y);
    let fee_x  = calculate_fee(pre_fee_amount_x, transfer_fee_basic_points, maximum_fee).unwrap();
    let fee_y  = calculate_fee(pre_fee_amount_y, transfer_fee_basic_points, maximum_fee).unwrap();
    cvt::CVT_assert(fee_x >= fee_y);
}