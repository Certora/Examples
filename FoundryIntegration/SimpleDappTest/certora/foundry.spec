use builtin rule verifyFoundryFuzzTestsNoRevert;

override function init_fuzz_tests(method f, env e) {
    reset_storage currentContract;
}