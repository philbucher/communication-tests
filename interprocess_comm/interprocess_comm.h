#pragma once

#include <string>
#include <vector>
#include <boost/interprocess/managed_shared_memory.hpp>

class InterprocessCommunication
{
    public:

    InterprocessCommunication(const std::string& rConnectionName, const bool IsConnectionMaster)
    {

    }

    ~InterprocessCommunication()
    {

    }

    void Connect()
    {

    }

    void Disconnect()
    {

    }

    void Send(const std::size_t SendSize, const std::size_t SendDataId)
    {

    }

    void Receive(const std::size_t SendSize, const std::size_t SendDataId)
    {

    }
};