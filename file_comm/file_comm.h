#pragma once

#include <vector>
#include "../communication.h"
#include "file_comm_file_system.h"

class FileCommunication : public Communication
{
    public:

    FileCommunication(const std::string& rConnectionName, const bool IsConnectionMaster)
        : Communication(rConnectionName, IsConnectionMaster)
    {
        COMM_TESTS_ERROR << "not implemented yet" << std::endl;
    }

    ~FileCommunication() override
    {

    }

    void ConnectDetail() override
    {

    }

    void DisconnectDetail() override
    {

    }

    void SendDetail(const std::size_t SendSize, const std::size_t SendDataId) override
    {

    }

    void ReceiveDetail(const std::size_t SendSize, const std::size_t SendDataId) override
    {

    }
};
