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

    void SendDetail(const std::size_t SendSize, const std::size_t SendDataId) override
    {

    }

    void ReceiveDetail(const std::size_t SendSize, const std::size_t SendDataId) override
    {

    }
};

