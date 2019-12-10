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

    void SendDetail(const std::vector<int>& rSendData) override
    {

    }

    void SendDetail(const std::vector<double>& rSendData) override
    {

    }

    void ReceiveDetail(std::vector<int>& rRecvData) override
    {

    }

    void ReceiveDetail(std::vector<double>& rRecvData) override
    {

    }
};

