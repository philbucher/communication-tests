#pragma once

#include <string>
#include <vector>
#include "../communication.h"
#include "file_comm_file_system.h"

class FileCommunication : public Communication
{
    public:

    FileCommunication(const std::string& rConnectionName, const bool IsConnectionMaster)
        : Communication(rConnectionName, IsConnectionMaster)
    {

    }

    ~FileCommunication() override
    {

    }

    void Connect() override
    {

    }

    void Disconnect() override
    {

    }

    void Send(const std::size_t SendSize, const std::size_t SendDataId) override
    {

    }

    void Receive(const std::size_t SendSize, const std::size_t SendDataId) override
    {

    }
};
