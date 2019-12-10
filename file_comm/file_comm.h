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
