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
        mCommFolderName = ".FileComm_" + GetConnectionName();

        RemoveLeftovers();

        if (GetIsConnectionMaster()) {
            fs::create_directory(mCommFolderName);
        }
    }

    ~FileCommunication() override
    {
        RemoveLeftovers();
    }

    // nothing needed for FileComm
    void ConnectDetail() override { }

    void DisconnectDetail() override
    {
        RemoveLeftovers();
    }

    void SendDetail(const std::size_t SendSize, const std::size_t SendDataId) override
    {

    }

    void ReceiveDetail(const std::size_t SendSize, const std::size_t SendDataId) override
    {

    }

private:
    std::string mCommFolderName;

    void RemoveLeftovers()
    {
        // it seems as if this can be called multiple times, won't throw even if the dir does not exist
        // TODO check the docu
        if (GetIsConnectionMaster()) {
            // clean up leftovers
            fs::remove_all(mCommFolderName);
        }
    }

};
