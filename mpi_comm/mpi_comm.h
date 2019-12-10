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
        COMM_TESTS_ERROR << "not implemented yet" << std::endl;
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

    void SendDetail(const std::vector<int>& rData) override
    {

    }

    void SendDetail(const std::vector<double>& rData) override
    {

    }

    void ReceiveDetail(std::vector<int>& rData) override
    {

    }

    void ReceiveDetail(std::vector<double>& rData) override
    {

    }
};

