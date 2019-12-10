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

    void SendDetail(const std::vector<int>& rData) override { SendVector(rData); }
    void SendDetail(const std::vector<double>& rData) override { SendVector(rData); }
    void ReceiveDetail(std::vector<int>& rData) override { RecvVector(rData); }
    void ReceiveDetail(std::vector<double>& rData) override { RecvVector(rData); }

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

    template<typename TDataType>
    void SendVector(const std::vector<TDataType>& rData)
    {
        // TODO implement ...
    }

    template<typename TDataType>
    void RecvVector(std::vector<TDataType>& rData)
    {
        // TODO implement ...
    }

};
