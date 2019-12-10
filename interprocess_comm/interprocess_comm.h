#pragma once

#include <vector>
#include "../communication.h"
#include <boost/interprocess/managed_shared_memory.hpp>

class InterprocessCommunication : public Communication
{
    public:

    InterprocessCommunication(const std::string& rConnectionName, const bool IsConnectionMaster)
        : Communication(rConnectionName, IsConnectionMaster)
    {

    }

    ~InterprocessCommunication() override
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
