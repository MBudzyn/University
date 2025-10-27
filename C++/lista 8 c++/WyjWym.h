#pragma once
#include <stdexcept>
#include <string>

class WyjWym : public std::logic_error {
public:
    explicit WyjWym(const std::string& what_arg);
};
