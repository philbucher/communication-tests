#pragma once

#include <vector>
#include "../communication.h"
#include <boost/asio.hpp>

class SocketsCommunication : public Communication
{
    public:

    SocketsCommunication(const std::string& rConnectionName, const bool IsConnectionMaster)
        : Communication(rConnectionName, IsConnectionMaster)
    {
        COMM_TESTS_ERROR << "not implemented yet" << std::endl;
    }

    ~SocketsCommunication() override
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

