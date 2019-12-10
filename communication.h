#pragma once

#include <string>
#include "common.h"

class Communication
{
public:
    Communication(const std::string& rConnectionName, const bool IsConnectionMaster)
        : mConnectionName(rConnectionName), mIsConnectionMaster(IsConnectionMaster) { }

    virtual ~Communication() { }

    void Connect()
    {
        // TODO add timings (or other things) if required
        ConnectDetail();
    }

    void Disconnect()
    {
        // TODO add timings (or other things) if required
        DisconnectDetail();
    }

    void Send(const std::size_t SendSize, const std::size_t SendDataId)
    {

    }

    void Receive(const std::size_t SendSize, const std::size_t SendDataId)
    {

    }

protected:
    std::string GetConnectionName() const {return mConnectionName;}
    bool GetIsConnectionMaster() const    {return mIsConnectionMaster;}
    bool GetPrintTiming() const           {return mPrintTiming;}

private:
    std::string mConnectionName;
    bool mIsConnectionMaster = false;
    bool mPrintTiming = false;

    virtual void ConnectDetail() = 0;
    virtual void DisconnectDetail() = 0;
    virtual void SendDetail(const std::size_t SendSize, const std::size_t SendDataId) = 0;
    virtual void ReceiveDetail(const std::size_t SendSize, const std::size_t SendDataId) = 0;
};