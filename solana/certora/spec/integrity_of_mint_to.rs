//! Certora specs

use solana_program::program_error::ProgramError;
use {
    crate::{processor::Processor},
    solana_program::{account_info::AccountInfo},
    cvt
};

/** Rules
- [integrity_of_process_mint_to] expected true
- [integrity_of_process_mint_to_false] expected false
 **/

#[inline(never)]
/// todoc
pub fn get_account_amount(account_info: &AccountInfo) -> Result<u64, ProgramError> {
    let account_data = account_info.data.borrow();
    let amount = <&[u8; 8]>::try_from(&account_data[64..(64 + 8)]).unwrap();
    Ok(u64::from_le_bytes(*amount))
}

#[inline(never)]
/// todoc
pub fn get_mint_supply(mint_info: &AccountInfo) -> Result<u64, ProgramError> {
    let mint_data = mint_info.data.borrow();
    let supply_bytes = <&[u8; 8]>::try_from(&mint_data[36..(36 + 8)]).unwrap();
    Ok(u64::from_le_bytes(*supply_bytes))
}

#[no_mangle]
/// Rule to check functional correctness of process_mint_to
pub fn integrity_of_process_mint_to() {
    // Create environment for process_mint_to
    let program_id = cvt::nondet();
    let acc_infos = [cvt::nondet::<AccountInfo>(), cvt::nondet::<AccountInfo>(), cvt::nondet::<AccountInfo>()];
    let amount = cvt::nondet();
    cvt::CVT_assume(amount > 0 );
    let mint_info = &acc_infos[0];
    let destination_info = &acc_infos[1];
    let destination_amount_before = get_account_amount(destination_info).unwrap();
    let supply_amount_before = get_mint_supply(mint_info).unwrap();

    Processor::process_mint_to(&program_id, &acc_infos, amount, None).unwrap();

    // Check properties
    let destination_amount_after = get_account_amount(destination_info).unwrap();
    let supply_amount_after = get_mint_supply(mint_info).unwrap();

    cvt::CVT_assert(destination_amount_after == destination_amount_before + amount);
    cvt::CVT_assert(destination_amount_after > destination_amount_before);
    cvt::CVT_assert(supply_amount_after == supply_amount_before + amount);
    cvt::CVT_assert(supply_amount_after > supply_amount_before);
}

#[no_mangle]
/// Buggy spec
pub fn integrity_of_process_mint_to_false() {
    // Create environment for process_mint_to
    let program_id = cvt::nondet();
    let acc_infos = [cvt::nondet::<AccountInfo>(), cvt::nondet::<AccountInfo>(), cvt::nondet::<AccountInfo>()];
    let amount = cvt::nondet();
    let mint_info = &acc_infos[0];
    let destination_info = &acc_infos[1];
    let destination_amount_before = get_account_amount(destination_info).unwrap();
    let supply_amount_before = get_mint_supply(mint_info).unwrap();

    Processor::process_mint_to(&program_id, &acc_infos, amount, None).unwrap();

    // Check properties
    let destination_amount_after = get_account_amount(destination_info).unwrap();
    let supply_amount_after = get_mint_supply(mint_info).unwrap();

    cvt::CVT_assert(destination_amount_after == destination_amount_before + amount);
    cvt::CVT_assert(destination_amount_after > destination_amount_before);
    cvt::CVT_assert(supply_amount_after == supply_amount_before + amount);
    cvt::CVT_assert(supply_amount_after > supply_amount_before);
}

