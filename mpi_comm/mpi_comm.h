#pragma once

#include <vector>
#include "../communication.h"
#include "mpi.h"

class MPICommunication : public Communication
{
    public:

    MPICommunication(const std::string& rConnectionName, const bool IsConnectionMaster)
        : Communication(rConnectionName, IsConnectionMaster)
    {

    }

    ~MPICommunication() override
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

