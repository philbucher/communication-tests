#pragma once

#include <iostream>
#include <stdexcept>
struct err {
err() {std::cout << "Error: ";}
~err() noexcept(false) { throw std::exception(); } // destructors are noexcept by default
};
#define COMM_TESTS_ERROR (err(), std::cout)

// TODO check configuration => I think Win by default builds debug! => works but has to be changed in case I do performace evaluations!