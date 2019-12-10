#pragma once

#include <string>
#include <vector>
#include "mpi.h"

class MPICommunication
{
    public:

    MPICommunication(const std::string& rConnectionName, const bool IsConnectionMaster)
    {

    }

    ~MPICommunication()
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
