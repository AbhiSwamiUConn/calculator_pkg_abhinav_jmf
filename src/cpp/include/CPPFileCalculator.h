#pragma once
#include "Calculator.h"
#include <string>

class CPPFileCalculator:public Calculator{
public:
    CPPFileCalculator();
    long long sum_file(const std::string& path = "");
};
